"""Run the pipeline over all 30 verses (Phase 1, W5).

Resumable: verses with an existing apparatus.json are skipped unless --force.
Hard cost stop: aborts if cumulative estimated LLM spend exceeds $25.
"""

import json
import sys
import time

from shastrartha.pipeline import default_analyze_fn, run_verse
from shastrartha.reason import total_spend

HARD_STOP_USD = 25.0


def main() -> int:
    force = "--force" in sys.argv
    analyze_fn = default_analyze_fn()
    results = []
    t0 = time.time()
    for n in range(1, 31):
        if total_spend() > HARD_STOP_USD:
            print(f"HARD STOP: estimated spend ${total_spend():.2f} > ${HARD_STOP_USD}")
            return 2
        try:
            s = run_verse(n, analyze_fn, force=force)
        except Exception as e:
            s = {"verse": n, "error": f"{type(e).__name__}: {e}"}
        results.append(s)
        print(json.dumps(s, ensure_ascii=False), flush=True)

    done = [r for r in results if not r.get("error")]
    errs = [r for r in results if r.get("error")]
    n_pass = sum(r.get("pass", 0) for r in done)
    n_fail = sum(r.get("fail", 0) for r in done)
    n_unsup = sum(r.get("unsupported", 0) for r in done)
    print(f"\n== {len(done)}/30 verses in {time.time()-t0:.0f}s | words: "
          f"{n_pass} pass / {n_fail} fail / {n_unsup} unsupported | "
          f"cumulative est spend ${total_spend():.2f}")
    for r in errs:
        print("ERROR:", r)
    return 0 if not errs else 1


if __name__ == "__main__":
    sys.exit(main())
