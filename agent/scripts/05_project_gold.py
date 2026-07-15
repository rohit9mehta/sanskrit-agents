"""Validate the pratīka-matcher against a gold projection (Phase 0 item 3).

Independent mechanism: globally align the token streams of trbh.txt and the
GRETIL comm file (same e-text lineage, ~0.994 similar) with difflib, project
each labeled kārikā line's tokens onto trbh line numbers, and require every
matcher anchor to overlap its unit's projected gold lines.

Also inventories the comm-only gaps (clauses missing from trbh.txt) for
MANIFEST.md's KNOWN_GAPS section.
"""

import json
import re
import sys
from difflib import SequenceMatcher

from shastrartha import texts
from shastrartha.normalize import skeleton
from shastrartha.texts import DATA_DIR

RAW_COMM = DATA_DIR / "raw" / "sa_vasubandhu-triMzikAvijJaptikArikA-comm.txt"
ALIGNMENT = DATA_DIR / "alignment" / "trimsika_alignment.json"
OUT = DATA_DIR / "alignment" / "gold_projection.json"

LABEL_TOKEN_RE = re.compile(r"^\(?\d{1,2}[a-d]{0,4}\)?$")
PAGINATION_RE = re.compile(r"\s*\[tvbh_\d+\]\s*")


def trbh_tokens() -> list[tuple[int, str]]:
    out = []
    for n in range(1, texts.TRBH_LINE_COUNT + 1):
        for tok in texts.line(n).split():
            sk = skeleton(tok)
            if sk:
                out.append((n, sk))
    return out


def comm_tokens() -> list[tuple[int, str]]:
    lines = RAW_COMM.read_text(encoding="utf-8").split("\n")
    out = []
    started = False
    for i, line in enumerate(lines, start=1):
        if line.strip() == "# Text":
            started = True
            continue
        if not started:
            continue
        for tok in PAGINATION_RE.sub(" ", line).split():
            if LABEL_TOKEN_RE.match(tok):
                continue
            sk = skeleton(tok)
            if sk:
                out.append((i, sk))
    return out


def main() -> int:
    a = trbh_tokens()
    b = comm_tokens()
    sm = SequenceMatcher(None, [t for _, t in a], [t for _, t in b], autojunk=False)

    # comm token index -> trbh line (only inside 'equal' blocks)
    comm_to_trbh_line: dict[int, int] = {}
    gaps: list[dict] = []
    ratio = sm.ratio()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                comm_to_trbh_line[j1 + k] = a[i1 + k][0]
        elif tag in ("delete", "replace") and (j2 - j1) < 3 and (i2 - i1) >= 3:
            pass  # trbh-only extra text: irrelevant here
        elif tag in ("insert", "replace") and (j2 - j1) >= 3:
            gaps.append(
                {
                    "comm_lines": sorted({b[j][0] for j in range(j1, j2)}),
                    "tokens": " ".join(t for _, t in b[j1:j2])[:100],
                    "near_trbh_line": a[min(i1, len(a) - 1)][0],
                }
            )

    # comm line -> set of projected trbh lines
    by_comm_line: dict[int, set[int]] = {}
    for j, (comm_line, _) in enumerate(b):
        if j in comm_to_trbh_line:
            by_comm_line.setdefault(comm_line, set()).add(comm_to_trbh_line[j])

    alignment = json.loads(ALIGNMENT.read_text(encoding="utf-8"))
    rows, disagreements = [], []
    for v in alignment["verses"]:
        for h in v["units"]:
            gold = sorted(by_comm_line.get(h["comm_line"], set()))
            got = set(range(h["lines"][0], h["lines"][1] + 1))
            ok = bool(got & set(gold)) if gold else None
            rows.append(
                {
                    "verse": h["verse"],
                    "padas": h["padas"],
                    "kind": h["kind"],
                    "comm_line": h["comm_line"],
                    "matcher_lines": h["lines"],
                    "gold_lines": gold,
                    "agree": ok,
                }
            )
            if ok is False:
                disagreements.append(rows[-1])

    anchor_ok = 0
    for v in alignment["verses"]:
        prim = next((r for r in rows if r["verse"] == v["verse"] and r["kind"] == "primary"), None)
        if prim and prim["agree"]:
            anchor_ok += 1

    OUT.write_text(
        json.dumps(
            {"token_similarity": round(ratio, 4), "units": rows, "gaps": gaps},
            ensure_ascii=False, indent=1,
        ),
        encoding="utf-8",
    )

    print(f"token similarity trbh↔comm: {ratio:.4f}")
    print(f"unit agreement: {sum(1 for r in rows if r['agree'])}/{len(rows)} "
          f"(unprojectable: {sum(1 for r in rows if r['agree'] is None)})")
    print(f"verse anchors agreeing with gold: {anchor_ok}/30")
    if disagreements:
        for d in disagreements:
            print(" DISAGREE:", d)
    print(f"comm-only gaps (≥3 tokens): {len(gaps)}")
    for g in gaps:
        print(f"  comm {g['comm_lines']}: {g['tokens'][:70]} (near trbh {g['near_trbh_line']})")
    print("GOLD PROJECTION", "PASS" if anchor_ok == 30 and not disagreements else "FAIL")
    return 0 if anchor_ok == 30 and not disagreements else 1


if __name__ == "__main__":
    sys.exit(main())
