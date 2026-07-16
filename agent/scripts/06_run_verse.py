"""Run the full pipeline on one verse: uv run --group ml python scripts/06_run_verse.py N [--force]"""

import json
import sys

from shastrartha.pipeline import OUTPUT_DIR, default_analyze_fn, run_verse


def main() -> int:
    n = int(sys.argv[1])
    force = "--force" in sys.argv
    summary = run_verse(n, default_analyze_fn(), force=force)
    print(json.dumps(summary, ensure_ascii=False))
    print(f"wrote {OUTPUT_DIR / f'v{n:02d}'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
