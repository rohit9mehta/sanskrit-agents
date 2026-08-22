"""Vyākaraṇī — our post-trained grammar analyzer (ByT5-Sanskrit fine-tuned on
vidyut-verified + vidyut-derived gold; see data/benchmark/runs/vyakarani-v1/).

Job: (surface word, its sentence) → claim in the verifier's own schema
    pos=tinanta root=gam prayoga=Kartari lakara=Lun purusha=Prathama vacana=Eka
    pos=subanta stem=deva linga=Pum vibhakti=Prathama vacana=Eka
It does NOT segment: surfaces come from the ByT5 segmenter (analyze.local_analyze
task "S"/"SLM"); it replaces ByT5's undocumented morph tags, and its output
feeds verify.py without any tag decoding.

Weights: agent/models/vyakarani-v1/ (gitignored; Modal volume
`shastrartha-models/vyakarani-v1/model`). Tokenizer = the ByT5 byte tokenizer.
Outputs are disk-cached per (model, surface, sentence).
"""

import hashlib
import json
import os
from pathlib import Path

from .texts import AGENT_DIR, DATA_DIR

VYAKARANI_DIR = Path(os.environ.get(
    "VYAKARANI_DIR", str(AGENT_DIR / "models" / "vyakarani-v1")))
VYAKARANI_NAME = os.environ.get("VYAKARANI_NAME", "vyakarani-v1")
TOKENIZER_ID = "chronbmm/sanskrit5-multitask"     # byte tokenizer; checkpoints carry weights only
CACHE_DIR = DATA_DIR / "cache" / "vyakarani"
MAX_INPUT_BYTES = 384
MAX_NEW_TOKENS = 96

FIELD_ORDER = ["pos", "stem", "linga", "vibhakti", "vacana",
               "root", "prefixes", "prayoga", "lakara", "purusha", "lemma"]

_model = None


def available() -> bool:
    return (VYAKARANI_DIR / "config.json").exists() or \
        (VYAKARANI_DIR / "model" / "config.json").exists()


def _weights_dir() -> Path:
    return VYAKARANI_DIR if (VYAKARANI_DIR / "config.json").exists() else VYAKARANI_DIR / "model"


def _load():
    global _model
    if _model is None:
        import torch
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        tok = AutoTokenizer.from_pretrained(TOKENIZER_ID)
        model = AutoModelForSeq2SeqLM.from_pretrained(str(_weights_dir())).to(device).eval()
        _model = (tok, model, device)
    return _model


def to_input(surface: str, sentence: str | None) -> str:
    return f"A {surface} ‖ {sentence or surface}"


def parse_target(s: str) -> dict:
    out = {}
    for tok in s.split():
        if "=" in tok:
            k, v = tok.split("=", 1)
            out[k] = v.split("+") if k == "prefixes" else v
    if out.get("prefixes") == ["-"]:
        out["prefixes"] = []
    return out


def analyze(pairs: list[tuple[str, str | None]], batch_size: int = 32) -> list[dict]:
    """[(surface, sentence)] → [{surface, raw, claim}] (disk-cached)."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    def cpath(surface, sentence):
        key = hashlib.sha256(f"{VYAKARANI_NAME}|{to_input(surface, sentence)}".encode()).hexdigest()[:24]
        return CACHE_DIR / f"{key}.json"

    results: dict[int, dict] = {}
    missing: list[int] = []
    for i, (sfc, sent) in enumerate(pairs):
        p = cpath(sfc, sent)
        if p.exists():
            results[i] = json.loads(p.read_text(encoding="utf-8"))
        else:
            missing.append(i)
    if missing:
        import torch
        tok, model, device = _load()
        order = sorted(missing, key=lambda i: len(to_input(*pairs[i])))
        for b in range(0, len(order), batch_size):
            idx = order[b:b + batch_size]
            enc = tok([to_input(*pairs[i]) for i in idx], return_tensors="pt",
                      padding=True, truncation=True, max_length=MAX_INPUT_BYTES).to(device)
            with torch.no_grad():
                gen = model.generate(**enc, max_new_tokens=MAX_NEW_TOKENS, num_beams=1)
            for i, raw in zip(idx, tok.batch_decode(gen, skip_special_tokens=True)):
                rec = {"surface": pairs[i][0], "raw": raw, "claim": parse_target(raw),
                       "model": VYAKARANI_NAME}
                cpath(*pairs[i]).write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8")
                results[i] = rec
    return [results[i] for i in range(len(pairs))]


def analyze_lines(lines: list[str], parsed_slm: list[list[dict]]) -> list[list[dict]]:
    """For each line, analyze every ByT5-segmented surface in the context of
    its line. Verbal roots are cited bare + prefixes via the lemma layer when
    the model emitted a fused root (training data mixed conventions)."""
    from .lemma import _split_prefixes
    from .verify import to_iast, to_slp1
    pairs, where = [], []
    out: list[list[dict]] = [[] for _ in lines]
    for li, toks in enumerate(parsed_slm):
        for ti, t in enumerate(toks):
            if "surface" not in t or t.get("tag") == "Cp":
                continue
            if not t.get("tag"):
                # indeclinable per the segmenter: v1 saw no avyaya training
                # examples (arbitration verified only subanta/tinanta) → route
                out[li].append({"surface": t["surface"], "pos": "avyaya",
                                "lemma": t.get("lemma"), "note": "indeclinable (segmenter)"})
                continue
            pairs.append((t["surface"], lines[li]))
            where.append((li, ti))
    if not pairs:
        return out
    for (li, ti), rec in zip(where, analyze(pairs)):
        c = dict(rec["claim"])
        if c.get("pos") == "tinanta" and c.get("root") and not c.get("prefixes"):
            root, pre = _split_prefixes(to_slp1(c["root"]))
            if pre:
                c["root"], c["prefixes"] = to_iast(root), pre
        out[li].append({"surface": rec["surface"], **{k: c.get(k) for k in FIELD_ORDER if c.get(k) is not None}})
    return out
