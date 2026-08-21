"""Freeze the analyzer benchmark (Phase 3 prep, stage 2b).

The held-out test set every later decision scores against — the current
ByT5 analyzer, base-model candidates, and any post-trained model. Built
BEFORE the training set is assembled; nothing here may be trained on.

Composition:
  * pipeline-hard — the a1-fail→a2-pass contrastive surfaces (gold = the
    accepted claim; the rejected claim rides along as a hard negative)
  * dcs — stratified sample of vidyut-verified DCS claims: common strata
    capped (flattened distribution), rare strata split ~50/50 with training
    so both sides keep examples

Leakage rule: the split unit is (surface, claim-json). split_v1.json lists
every benchmark key; the training-set builder must exclude them.

Outputs:
  agent/data/benchmark/analyzer_benchmark_v1.jsonl   (frozen)
  agent/data/benchmark/MANIFEST.json                 (sha256, counts, date)
  agent/data/training/split_v1.json                  (exclusion keys)

Deterministic: random.Random(20260821).
"""

import hashlib
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
TRAIN = AGENT / "data" / "training"
BENCH = AGENT / "data" / "benchmark"
RAW = AGENT / "data" / "dcs" / "raw"
OUTPUT = AGENT / "output"

SEED = 20260821
TARGET_DCS = 950          # + pipeline-hard items ≈ 1k total
STRATUM_CAP = 60          # max benchmark items per stratum (flattens Lat/Nom-Sing)
RARE_MAX = 30             # rare stratum: take min(half, RARE_MAX)
RARE_THRESHOLD = 80       # stratum smaller than this = rare → 50/50 split


def claim_norm(claim: dict) -> dict:
    """Analysis fields only, ordered, for keys/comparison."""
    keep = ("pos", "stem", "linga", "vibhakti", "vacana",
            "root", "prefixes", "prayoga", "lakara", "purusha", "lemma")
    return {k: claim[k] for k in keep if claim.get(k) is not None}


def item_key(surface: str, claim: dict) -> str:
    return surface + "‖" + json.dumps(claim_norm(claim), sort_keys=True,
                                      ensure_ascii=False)


def stratum(claim: dict) -> str:
    if claim["pos"] == "tinanta":
        return f"tin:{claim.get('lakara')}:{claim.get('prayoga')}"
    return f"sub:{claim.get('vibhakti')}:{claim.get('vacana')}"


def dcs_sentences() -> dict:
    """sent_id → sandhi'd sentence text, from the cached conllu files."""
    sents = {}
    for path in RAW.glob("*/*.conllu"):
        text, sid = None, None
        for line in path.open(encoding="utf-8"):
            if line.startswith("# text = "):
                text = line[len("# text = "):].strip()
            elif line.startswith("# sent_id"):
                sid = line.split("=", 1)[1].strip()
            elif not line.strip():
                if sid and text:
                    sents[sid] = text
                text = sid = None
        if sid and text:
            sents[sid] = text
    return sents


def unit_text(text: str, unit: str) -> str:
    """Verse/unit source text for pipeline items, from the apparatus files."""
    if text == "trbh":
        try:
            mula = json.loads((AGENT / "data" / "mula" / "trimsika.json")
                              .read_text(encoding="utf-8"))
            for v in mula["verses"]:
                if str(v["verse"]) == str(int(float(unit))):
                    return v["bhasya_text"]
        except Exception:
            return ""
    slug = {"isa": "isa", "gita": "gita", "yogasutra": "yogasutra"}.get(text)
    if slug:
        d = OUTPUT / slug / unit.replace(".", "_")
        for cand in [d, OUTPUT / slug / unit]:
            p = cand / "apparatus.json"
            if p.exists():
                j = json.loads(p.read_text(encoding="utf-8"))
                return j.get("mula") or j.get("verse_text") or ""
    return ""


def main():
    rng = random.Random(SEED)
    items = []

    # ---- pipeline-hard: contrastive accepted claims -------------------
    for line in (TRAIN / "contrastive.jsonl").open(encoding="utf-8"):
        p = json.loads(line)
        acc = p["accepted"]["claim"]["analysis"]
        if not acc:
            continue
        items.append({
            "source": "pipeline-hard",
            "text": p["text"], "unit": p["unit"],
            "sentence": unit_text(p["text"], p["unit"]),
            "surface": p["surface_iast"],
            "gold": claim_norm(acc),
            "hard_negative": claim_norm(p["rejected"]["claim"]["analysis"])
            if p["rejected"]["claim"].get("analysis") else None,
        })

    # ---- dcs: stratified sample ---------------------------------------
    sents = dcs_sentences()
    strata = defaultdict(list)
    for line in (TRAIN / "dcs_verified.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        strata[stratum(r["claim"])].append(r)

    picked = []
    for name in sorted(strata):
        rows = strata[name]
        rng.shuffle(rows)
        if len(rows) < RARE_THRESHOLD:
            take = min(len(rows) // 2, RARE_MAX)
        else:
            take = min(STRATUM_CAP, len(rows))
        picked.extend((name, r) for r in rows[:take])
    rng.shuffle(picked)
    picked = picked[:TARGET_DCS]

    for name, r in picked:
        items.append({
            "source": "dcs", "text": r["text"], "genre": r["genre"],
            "unit": r["sent_id"],
            "sentence": sents.get(r["sent_id"], ""),
            "surface": r["surface"],
            "gold": claim_norm(r["claim"]),
            "stratum": name,
        })

    # ---- dedupe on key, freeze ---------------------------------------
    seen, final = set(), []
    for it in items:
        k = item_key(it["surface"], it["gold"])
        if k in seen:
            continue
        seen.add(k)
        it["id"] = f"bm-{len(final)+1:04d}"
        final.append(it)

    BENCH.mkdir(parents=True, exist_ok=True)
    bpath = BENCH / "analyzer_benchmark_v1.jsonl"
    with bpath.open("w", encoding="utf-8") as f:
        for it in final:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    digest = hashlib.sha256(bpath.read_bytes()).hexdigest()

    strata_counts = Counter(it.get("stratum", "pipeline-hard") for it in final)
    (BENCH / "MANIFEST.json").write_text(json.dumps({
        "file": bpath.name, "sha256": digest, "items": len(final),
        "seed": SEED, "frozen": "2026-08-21",
        "sources": dict(Counter(it["source"] for it in final)),
        "strata": dict(strata_counts),
        "rule": "Nothing in this file may be used for training. "
                "Split unit = (surface, claim); see training/split_v1.json.",
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    (TRAIN / "split_v1.json").write_text(json.dumps({
        "benchmark": bpath.name, "sha256": digest,
        "excluded_keys": sorted(seen),
    }, ensure_ascii=False, indent=0), encoding="utf-8")

    n_sent = sum(1 for it in final if it["sentence"])
    print(f"benchmark frozen: {len(final)} items "
          f"({dict(Counter(it['source'] for it in final))}), "
          f"{n_sent} with sentence context, {len(strata_counts)} strata")
    print(f"sha256 {digest[:16]}…  → {bpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
