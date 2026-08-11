"""CLI for the ask-box: 19_ask.py "your question" [--effort low|medium|high]"""

import sys

from shastrartha.ask import ask


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 1
    effort = "medium"
    if "--effort" in sys.argv:
        effort = sys.argv[sys.argv.index("--effort") + 1]
    res = ask(" ".join(args), effort=effort)
    print(res["answer"])
    print("\n--- sources ---")
    for c in res["citations"][:6]:
        print(f"  [{c['key']}] ({c['kind']}, score {c['score']})")
    if res.get("usage"):
        print(f"  tokens: {res['usage']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
