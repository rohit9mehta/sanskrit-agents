"""ANALYZE stage: Sanskrit segmentation / lemmatization / morphosyntax.

Two providers:

1. Dharmamitra API (https://dharmamitra.org/api/tagging/) — fast, no local
   model. Schema verified 2026-07-14; the pip package
   `dharmamitra-sanskrit-grammar` 0.1.7 predates it and 422s, so we speak the
   current schema directly. Currently the API returns segmentation only.
   Every response is cached under agent/data/cache/dharmamitra/ keyed by
   payload hash, so reruns are reproducible and work offline.

2. Local ByT5-Sanskrit multitask (chronbmm/sanskrit5-multitask) — the
   EMNLP Findings 2024 model. Task prefixes:
     S  = segmentation            L  = lemmatization
     M  = morphosyntax            SL / SM / SLM = joint tasks
   Runs on Apple-Silicon MPS when available, else CPU.
"""

import hashlib
import json
from typing import Any

import requests

from .texts import DATA_DIR

DHARMAMITRA_URL = "https://dharmamitra.org/api/tagging/"
CACHE_DIR = DATA_DIR / "cache" / "dharmamitra"

MODEL_ID = "chronbmm/sanskrit5-multitask"
LOCAL_TASKS = ("S", "L", "M", "SL", "SM", "SLM")


# ---------------------------------------------------------------- Dharmamitra

def dharmamitra_tag(
    texts: list[str],
    mode: str = "unsandhied",
    human_readable_tags: bool = True,
    use_cache: bool = True,
    timeout: int = 120,
) -> list[str]:
    """POST to the Dharmamitra tagging API; returns one result string per input."""
    payload: dict[str, Any] = {
        "texts": [t.strip() for t in texts],
        "mode": mode,
        "input_encoding": "auto",
        "human_readable_tags": human_readable_tags,
    }
    key = hashlib.sha256(
        json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()[:24]
    cache_file = CACHE_DIR / f"{key}.json"

    if use_cache and cache_file.exists():
        return json.loads(cache_file.read_text())["response"]["results"]

    resp = requests.post(DHARMAMITRA_URL, json=payload, timeout=timeout)
    resp.raise_for_status()
    body = resp.json()
    if "results" not in body:
        raise ValueError(f"unexpected Dharmamitra response shape: {list(body)}")

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(
        json.dumps({"payload": payload, "response": body}, ensure_ascii=False, indent=1)
    )
    return body["results"]


# ---------------------------------------------------------------- local ByT5

# SLM output: space-separated tokens, each `surface_lemma_tag` (tag may be
# empty for indeclinables). Verified 2026-07-15 on trbh lines 24/167:
#   vipākaḥ_vipāka_SNM   manana_manana_Cp   ca_ca_   pravartate_pravṛt_SPr3In
# Nominal tag = [Number][Case][Gender] (SNM = sg. nom. masc.); verbal tag =
# [Number][Tense][Person][Mood] (SPr3In = sg. present 3rd indicative);
# Cp = prior compound member (samāsa-internal, uninflected).

_local = None  # (tokenizer, model, device) — loaded once, ~2.3 GB


def _load_local():
    global _local
    if _local is None:
        import torch
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

        device = "mps" if torch.backends.mps.is_available() else "cpu"
        tok = AutoTokenizer.from_pretrained(MODEL_ID)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID).to(device).eval()
        _local = (tok, model, device)
    return _local


def local_analyze(
    texts: list[str],
    task: str = "SLM",
    max_new_tokens: int = 1024,
    batch_size: int = 8,
) -> list[str]:
    """Run the local multitask model; returns one decoded string per input."""
    if task not in LOCAL_TASKS:
        raise ValueError(f"task must be one of {LOCAL_TASKS}")
    import torch

    tok, model, device = _load_local()
    out: list[str] = []
    for i in range(0, len(texts), batch_size):
        batch = [f"{task} {t.strip()}" for t in texts[i : i + batch_size]]
        enc = tok(batch, return_tensors="pt", padding=True).to(device)
        with torch.no_grad():
            gen = model.generate(**enc, max_new_tokens=max_new_tokens, num_beams=1)
        out.extend(tok.batch_decode(gen, skip_special_tokens=True))
    return out


def parse_slm(output: str) -> list[dict]:
    """Parse one SLM output line into [{surface, lemma, tag}]. Tokens that do
    not have the three-field shape are kept raw under 'unparsed'."""
    parsed = []
    for token in output.split():
        parts = token.split("_")
        if len(parts) == 3:
            parsed.append({"surface": parts[0], "lemma": parts[1], "tag": parts[2]})
        else:
            parsed.append({"unparsed": token})
    return parsed
