"""Re-run the whole library with the current analyzer stack (Vyākaraṇī +
ByT5 segmenter + lemma layer) and reasoner (GPT-5.6 Sol), overwriting the
stored apparatus so every served translation traces to Vyākaraṇī.

Order: trimsika (30 verses) → isa → yogasutra → gita (cheap first).
Spend guard: stops if cumulative est. LLM spend rises by more than --budget
(default $60) over the run's start. Resumable: re-running skips units whose
apparatus.json already records analyzer == vyakarani (unless --force-all).

Usage: .venv/bin/python scripts/37_rerun_library.py [--budget 60] [--only trimsika,isa]
"""

import json
import sys
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AGENT / "src"))

from shastrartha.library import load_text  # noqa: E402
from shastrartha.pipeline import OUTPUT_DIR, default_analyze_fn, run_unit, run_verse  # noqa: E402
from shastrartha.reason import total_spend  # noqa: E402


def done_with_vyakarani(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        d = json.loads(path.read_text())
        return str((d.get("run") or {}).get("analyzer", "")).startswith("vyakarani")
    except Exception:
        return False


def main():
    args = sys.argv[1:]
    budget = float(args[args.index("--budget") + 1]) if "--budget" in args else 60.0
    only = set(args[args.index("--only") + 1].split(",")) if "--only" in args else None
    force_all = "--force-all" in args
    start = total_spend()
    fn = default_analyze_fn()
    print(f"start spend ${start:.2f}; budget +${budget:.0f}", flush=True)

    def guard():
        spent = total_spend() - start
        if spent > budget:
            print(f"BUDGET STOP: +${spent:.2f}", flush=True)
            sys.exit(2)

    if only is None or "trimsika" in only:
        for n in range(1, 31):
            if not force_all and done_with_vyakarani(OUTPUT_DIR / f"v{n:02d}" / "apparatus.json"):
                continue
            guard()
            s = run_verse(n, fn, force=True)
            print(json.dumps({"text": "trimsika", **s}, ensure_ascii=False)[:220], flush=True)
    for slug in ("isa", "yogasutra", "gita"):
        if only is not None and slug not in only:
            continue
        lt = load_text(slug)
        for uid in lt.order:
            p = OUTPUT_DIR / slug / uid.replace(".", "_") / "apparatus.json"
            if not p.exists():          # never translated (no commentary) — leave as is
                continue
            if not force_all and done_with_vyakarani(p):
                continue
            guard()
            try:
                s = run_unit(slug, uid, fn, force=True)
            except Exception as e:
                s = {"unit": uid, "error": f"{type(e).__name__}: {str(e)[:120]}"}
            print(json.dumps({"text": slug, **s}, ensure_ascii=False)[:220], flush=True)
    print(f"== done. run spend +${total_spend() - start:.2f}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
