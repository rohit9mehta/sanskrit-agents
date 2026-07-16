"""Phase 2, item 1: mechanical audit of every justification citation.

Each Evidence object claims `quote` (IAST, 'verbatim') comes from trbh lines
`lines`. Check: is the skeleton-normalized quote contained in the skeleton of
the cited lines (± CONTEXT_PAD lines of tolerance for off-by-one citations)?

Verdicts per quote:
  verbatim  — quote skeleton is a substring of the cited lines' skeleton
  near      — fuzzy (partial_ratio ≥ 90) against cited lines, or verbatim
              only within the padded window (off-by-one citation)
  MISS      — neither: the quote does not come from where it claims

Output: agent/output/citation_audit.{md,json}; exit 1 if any MISS.
"""

import json
import sys

from rapidfuzz import fuzz

from shastrartha import texts
from shastrartha.normalize import skeleton
from shastrartha.texts import AGENT_DIR

OUTPUT = AGENT_DIR / "output"
CONTEXT_PAD = 1
NEAR_THRESHOLD = 90.0


import re

_SEG_SPLIT = re.compile(r"\n|\.\.\.|…")


def _runs(lines: list[int]) -> list[tuple[int, int]]:
    """Contiguous runs among the cited line numbers ([475,476,481] →
    [(475,476),(481,481)]) — quotes may stitch non-adjacent excerpts."""
    ls = sorted(set(lines))
    runs, start = [], ls[0]
    for a, b in zip(ls, ls[1:]):
        if b != a + 1:
            runs.append((start, a))
            start = b
    runs.append((start, ls[-1]))
    return runs


def _run_skeleton(lo: int, hi: int, pad: int) -> str:
    lo = max(1, lo - pad)
    hi = min(texts.TRBH_LINE_COUNT, hi + pad)
    return "".join(skeleton(texts.line(n)) for n in range(lo, hi + 1))


def audit_quote(quote: str, lines: list[int]) -> tuple[str, float]:
    """Each quote segment (split on newlines / ellipses) must appear in some
    contiguous run of the cited lines. Verdict = worst segment."""
    if not lines:
        return "MISS", 0.0
    all_segments = [skeleton(s) for s in _SEG_SPLIT.split(quote)]
    segments = [s for s in all_segments if len(s) >= 6]
    if not segments:  # very short quotes (single words) are still checkable
        segments = [s for s in all_segments if s]
    if not segments:
        return "MISS", 0.0
    runs = _runs(lines)
    exact = [_run_skeleton(lo, hi, 0) for lo, hi in runs]
    padded = [_run_skeleton(lo, hi, CONTEXT_PAD) for lo, hi in runs]
    worst, worst_score = "verbatim", 100.0
    order = {"verbatim": 0, "near": 1, "MISS": 2}
    for seg in segments:
        if any(seg in sk for sk in exact):
            verdict, score = "verbatim", 100.0
        elif any(seg in sk for sk in padded):
            verdict, score = "near", 99.0
        else:
            score = max(fuzz.partial_ratio(seg, sk) for sk in padded)
            verdict = "near" if score >= NEAR_THRESHOLD else "MISS"
            score = round(score, 1)
        if order[verdict] > order[worst]:
            worst, worst_score = verdict, score
    return worst, worst_score


def main() -> int:
    rows, totals = [], {"verbatim": 0, "near": 0, "MISS": 0}
    n_quotes = 0
    for n in range(1, 31):
        d = json.loads((OUTPUT / f"v{n:02d}" / "apparatus.json").read_text())
        for j in d["justifications"]:
            for k, e in enumerate(j["evidence"]):
                verdict, score = audit_quote(e["quote"], e["lines"])
                totals[verdict] += 1
                n_quotes += 1
                rows.append({
                    "verse": n, "j": j["id"], "ev": k, "lines": e["lines"],
                    "verdict": verdict, "score": score,
                    "quote": e["quote"][:90],
                })

    (OUTPUT / "citation_audit.json").write_text(
        json.dumps({"totals": totals, "n_quotes": n_quotes, "rows": rows},
                   ensure_ascii=False, indent=1), encoding="utf-8")

    with (OUTPUT / "citation_audit.md").open("w", encoding="utf-8") as f:
        f.write("# Citation audit — do the apparatus quotes come from where they claim?\n\n")
        f.write(f"Method: skeleton-normalized containment in cited trbh lines "
                f"(±{CONTEXT_PAD} line tolerance → 'near'; fuzzy ≥{NEAR_THRESHOLD} → 'near').\n\n")
        f.write(f"| verdict | count | share |\n|---|---|---|\n")
        for k in ("verbatim", "near", "MISS"):
            f.write(f"| {k} | {totals[k]} | {totals[k]/max(1,n_quotes):.1%} |\n")
        f.write(f"\nTotal evidence quotes audited: {n_quotes} across 30 verses.\n")
        bad = [r for r in rows if r["verdict"] == "MISS"]
        nears = [r for r in rows if r["verdict"] == "near"]
        if bad:
            f.write("\n## MISSES (quote not found at cited lines)\n\n")
            for r in bad:
                f.write(f"- v.{r['verse']} {r['j']} ev{r['ev']} lines {r['lines']} "
                        f"(score {r['score']}): `{r['quote']}`\n")
        if nears:
            f.write("\n## Near matches (off-by-one citation or minor divergence)\n\n")
            for r in nears:
                f.write(f"- v.{r['verse']} {r['j']} ev{r['ev']} lines {r['lines']} "
                        f"(score {r['score']}): `{r['quote']}`\n")

    print(f"audited {n_quotes} quotes: {totals}")
    print(f"wrote {OUTPUT/'citation_audit.md'}")
    return 1 if totals["MISS"] else 0


if __name__ == "__main__":
    sys.exit(main())
