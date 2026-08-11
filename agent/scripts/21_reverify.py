"""Re-verify stored library apparatuses after verifier fixes — no LLM calls.

Rebuilds each apparatus's verification fields (per-word status, summary,
rendered md) from the CURRENT verifier. The reasoner's claims are untouched.
"""

import json
import sys
from pathlib import Path

from shastrartha.ask import TEXT_META
from shastrartha.library import load_text
from shastrartha.pipeline import OUTPUT_DIR, _merge
from shastrartha.render import render_apparatus
from shastrartha.runner import pipeline_verify
from shastrartha.schema import LibApparatus

WORD_KEYS = ("surface", "surface_in_sandhi", "lemma", "morph", "samasa", "note")
APP_KEYS = ("unit", "justifications", "translation", "one_shot_delta",
            "analyzer_disagreements", "open_questions")


def reverify(slug: str) -> dict:
    lt = load_text(slug)
    tot = {"pass": 0, "fail": 0, "unsupported": 0, "tool_error": 0}
    for f in sorted((OUTPUT_DIR / slug).glob("*/apparatus.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        clean = {k: d[k] for k in APP_KEYS}
        clean["analysis"] = [{k: w.get(k) for k in WORD_KEYS} for w in d["analysis"]]
        app = LibApparatus.model_validate(clean)
        report = pipeline_verify(app, run_id=f"reverify-{slug}-{app.unit}", text=slug)
        meta = dict(d.get("run", {}))
        meta["reverified"] = True
        merged = _merge(app, report, meta)
        merged["mula"] = d.get("mula", "")
        merged["commentary_lines"] = d.get("commentary_lines", [])
        f.write_text(json.dumps(merged, ensure_ascii=False, indent=1),
                     encoding="utf-8")
        (f.parent / "apparatus.md").write_text(
            render_apparatus(
                merged,
                title=f"# {lt.title} — {app.unit} (commentary-grounded, with apparatus)",
                tag=lt.citation_tag),
            encoding="utf-8")
        for k in tot:
            tot[k] += report.n[k]
    return tot


def main() -> int:
    grand = {"pass": 0, "fail": 0, "unsupported": 0, "tool_error": 0}
    for slug in [s for s in TEXT_META if s != "trimsika"]:
        t = reverify(slug)
        print(slug, t)
        for k in grand:
            grand[k] += t[k]
    print("ALL:", grand)
    return 0


if __name__ == "__main__":
    sys.exit(main())
