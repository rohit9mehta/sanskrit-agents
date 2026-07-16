"""Baselines (Phase 1, W5).

raw-LLM: the SAME model as the pipeline reasoner, given ONLY the verse text
(bhāṣya reading) and a minimal instruction — no commentary, no analyses, no
dictionary. This is the A/B that the Phase 2 decision gate cares about.
Output: agent/data/eval/raw_llm.json

MITRA: dharmamitra cat-translate endpoint (found in the org's
dharmamitra-claude-code-agent repo; unauthenticated). One call per verse,
politely paced. Output: agent/data/eval/mitra.json
"""

import json
import sys
import time

import requests

from shastrartha.reason import MODEL, _chat, total_spend
from shastrartha.texts import DATA_DIR

MULA = DATA_DIR / "mula" / "trimsika.json"
OUT_RAW = DATA_DIR / "eval" / "raw_llm.json"
OUT_MITRA = DATA_DIR / "eval" / "mitra.json"

PROMPT = (
    "Translate this Sanskrit verse from Vasubandhu's Triṃśikā into English. "
    "Give only the translation.\n\n{verse}"
)
MITRA_URL = "https://dharmamitra.org/api-search/cat-translate/v1/translate"


def run_raw_llm(mula: dict) -> None:
    out = {"model": MODEL, "prompt_template": PROMPT, "verses": {}}
    for v in mula["verses"]:
        n = v["verse"]
        text, _ = _chat(
            [{"role": "user", "content": PROMPT.format(verse=v["bhasya_text"])}],
            str, tag=f"rawllm-v{n:02d}",
        )
        out["verses"][str(n)] = text.strip()
        print(f"raw v.{n}: {text.strip()[:70]}...", flush=True)
    OUT_RAW.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")


def run_mitra(mula: dict) -> None:
    verses = {}
    if OUT_MITRA.exists():
        verses = {k: v for k, v in json.loads(OUT_MITRA.read_text())["verses"].items()
                  if not v.startswith("[ERROR")}
    out = {"endpoint": MITRA_URL, "style_instruction": "balanced",
           "fetched": "2026-07-16", "verses": verses}
    for v in mula["verses"]:
        n = str(v["verse"])
        if n in verses:
            continue
        for attempt in range(3):
            try:
                r = requests.post(
                    MITRA_URL, timeout=120,
                    json={"input_sanskrit": v["bhasya_text"],
                          "target_language": "english",
                          "style_instruction": "balanced"},
                )
                r.raise_for_status()
                verses[n] = r.json()["translation"].strip()
                print(f"mitra v.{n}: {verses[n][:70]}...", flush=True)
                break
            except Exception as e:
                if attempt == 2:
                    verses[n] = f"[ERROR: {type(e).__name__}: {e}]"
                    print(f"mitra v.{n}: ERROR {e}", flush=True)
                else:
                    time.sleep(30 * (attempt + 1))
        OUT_MITRA.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                             encoding="utf-8")
        time.sleep(8)


def main() -> int:
    mula = json.loads(MULA.read_text(encoding="utf-8"))
    OUT_RAW.parent.mkdir(parents=True, exist_ok=True)
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "raw"):
        run_raw_llm(mula)
    if which in ("all", "mitra"):
        run_mitra(mula)
    print(f"done; cumulative est LLM spend ${total_spend():.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
