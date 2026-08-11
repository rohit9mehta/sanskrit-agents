"""Run the library pipeline over a text's units (Phase 3).

Usage:
  18_run_text.py <slug>                      # all units with commentary
  18_run_text.py gita --prefix 2.            # chapter 2 only
  18_run_text.py yogasutra --prefix 1.       # samādhi-pāda only
  18_run_text.py isa --units 1,2,3
  [--force]

Budget: hard stop when cumulative estimated LLM spend exceeds $90.
"""

import json
import sys

from shastrartha.library import load_text
from shastrartha.pipeline import default_analyze_fn, run_unit
from shastrartha.reason import total_spend

HARD_STOP_USD = 90.0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    slug = args[0]
    force = "--force" in args
    prefix = None
    only = None
    if "--prefix" in args:
        prefix = args[args.index("--prefix") + 1]
    if "--units" in args:
        only = set(args[args.index("--units") + 1].split(","))

    lt = load_text(slug)
    unit_ids = [u for u in lt.order
                if (only is None or u in only)
                and (prefix is None or u.startswith(prefix))]
    print(f"{slug}: {len(unit_ids)} units to run")

    analyze_fn = default_analyze_fn()
    totals = {"pass": 0, "fail": 0, "unsupported": 0, "tool_error": 0}
    for uid in unit_ids:
        if total_spend() > HARD_STOP_USD:
            print(f"HARD STOP: cumulative est spend ${total_spend():.2f}")
            return 1
        try:
            s = run_unit(slug, uid, analyze_fn, force=force)
        except Exception as e:
            s = {"unit": uid, "error": f"{type(e).__name__}: {str(e)[:150]}"}
        print(json.dumps(s, ensure_ascii=False), flush=True)
        for k in totals:
            totals[k] += s.get(k, 0)
    print(f"== done. words: {totals} | cumulative est spend ${total_spend():.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
