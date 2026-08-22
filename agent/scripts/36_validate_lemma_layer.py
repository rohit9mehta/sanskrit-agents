"""Validate the lemma-normalization layer on real pipeline runs.

Re-runs a few previously translated units with the current code (canonical
lemma hints + prompt rule) into a SCRATCH output dir, then diffs against the
stored apparatus: analyzer overrides, attempts (retries), tokens / est cost,
verification summary, and how many chosen lemmas now equal the canonical
citation. Does not touch agent/output/.

Usage: .venv/bin/python scripts/36_validate_lemma_layer.py [gita:2.19 isa:4 trimsika:10]
"""

import json
import sys
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AGENT / "src"))

from shastrartha import pipeline  # noqa: E402
from shastrartha.pipeline import default_analyze_fn, run_unit, run_verse  # noqa: E402

SCRATCH = AGENT / "data" / "validation" / "lemma_layer"
STORED = AGENT / "output"
DEFAULT = ["gita:2.19", "isa:4", "trimsika:10"]


def stored_path(slug, unit):
    if slug == "trimsika":
        return STORED / f"v{int(unit):02d}" / "apparatus.json"
    return STORED / slug / unit.replace(".", "_") / "apparatus.json"


def new_path(slug, unit):
    if slug == "trimsika":
        return SCRATCH / f"v{int(unit):02d}" / "apparatus.json"
    return SCRATCH / slug / unit.replace(".", "_") / "apparatus.json"


def summarize(d):
    run = d.get("run", {})
    usage = run.get("usage") or {}
    if isinstance(usage, list):
        tok = sum((u.get("total_tokens") or u.get("total") or 0) for u in usage if isinstance(u, dict))
    else:
        tok = usage.get("total_tokens") or usage.get("total") or 0
    return {
        "overrides": len(d.get("analyzer_disagreements", [])),
        "attempts": run.get("attempts"),
        "tokens": tok,
        "est_cost": run.get("est_cost"),
        "verification": d.get("verification_summary"),
        "n_words": len(d.get("analysis", [])),
        "disagreements": d.get("analyzer_disagreements", []),
        "lemmas": {w["surface"]: w["lemma"] for w in d.get("analysis", [])},
    }


def main():
    targets = sys.argv[1:] or DEFAULT
    pipeline.OUTPUT_DIR = SCRATCH
    SCRATCH.mkdir(parents=True, exist_ok=True)
    fn = default_analyze_fn()
    rows = []
    for t in targets:
        slug, unit = t.split(":")
        print(f"== running {slug} {unit}", flush=True)
        try:
            if slug == "trimsika":
                s = run_verse(int(unit), fn, force=True)
            else:
                s = run_unit(slug, unit, fn, force=True)
            print(json.dumps(s, ensure_ascii=False)[:300], flush=True)
        except Exception as e:
            print(f"  ! {type(e).__name__}: {e}", flush=True)
            continue
        old = json.loads(stored_path(slug, unit).read_text())
        new = json.loads(new_path(slug, unit).read_text())
        rows.append((t, summarize(old), summarize(new)))

    md = ["# Lemma-layer validation: stored vs re-run", "",
          "| unit | overrides old→new | attempts | tokens | est $ | verify (pass/fail/unsup) |",
          "|---|---|---|---|---|---|"]
    for t, o, n in rows:
        def v(x):
            vs = x["verification"] or {}
            return f"{vs.get('pass','?')}/{vs.get('fail','?')}/{vs.get('unsupported','?')}"
        md.append(f"| {t} | {o['overrides']} → **{n['overrides']}** | {o['attempts']} → {n['attempts']} "
                  f"| {o['tokens']} → {n['tokens']} | {o['est_cost']} → {n['est_cost']} | {v(o)} → {v(n)} |")
    md += ["", "## Remaining disagreements (new run)", ""]
    for t, o, n in rows:
        md.append(f"### {t}")
        for s in n["disagreements"]:
            md.append(f"- {s[:220]}")
        changed = [(w, o["lemmas"].get(w), l) for w, l in n["lemmas"].items() if o["lemmas"].get(w) not in (None, l)]
        if changed:
            md.append("\nLemma citations that changed vs stored: " + "; ".join(f"{w}: {a} → {b}" for w, a, b in changed[:12]))
        md.append("")
    (SCRATCH / "report.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md[:len(rows) + 4]))
    print(f"report → {SCRATCH / 'report.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
