"""Run the pratīka-matcher over all 30 verses (Phase 0, CLAUDE.md item 3).

Writes data/alignment/trimsika_alignment.json and alignment_report.md
(the report prints each verse's anchor lines and span edges in full for the
human spot-check protocol).
"""

import json
import sys

from shastrartha import texts
from shastrartha.match import align
from shastrartha.texts import DATA_DIR

MULA = DATA_DIR / "mula" / "trimsika.json"
OUT = DATA_DIR / "alignment"


def main() -> int:
    mula = json.loads(MULA.read_text(encoding="utf-8"))
    result = align(mula)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "trimsika_alignment.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    problems = []
    if result["unmatched"]:
        for u in result["unmatched"]:
            problems.append(
                f"unmatched unit v.{u['verse']}{u['padas']} (comm {u['comm_line']}): {u['text'][:60]}"
            )
    with (OUT / "alignment_report.md").open("w", encoding="utf-8") as f:
        f.write("# Triṃśikā ↔ bhāṣya alignment report\n\n")
        f.write("| verse | anchor | span | conf | units (padas@lines score signals) |\n")
        f.write("|---|---|---|---|---|\n")
        for v in result["verses"]:
            if "anchor" not in v:
                problems.append(f"v.{v['verse']}: no anchor derived")
                f.write(f"| {v['verse']} | — | — | — | NO ANCHOR |\n")
                continue
            units = "; ".join(
                f"{h['padas']}@{h['lines'][0]}"
                + (f"–{h['lines'][1]}" if h['lines'][1] != h['lines'][0] else "")
                + f" {h['score']}"
                + (f" [{','.join(h['signals'])}]" if h["signals"] else "")
                + (" (re)" if h["kind"] == "requote" else "")
                for h in v["units"]
            )
            f.write(
                f"| {v['verse']} | {v['anchor'][0]}–{v['anchor'][1]} | "
                f"{v['span'][0]}–{v['span'][1]} | {v['confidence']} | {units} |\n"
            )
        f.write("\n## Span edges (for human spot-check)\n\n")
        for v in result["verses"]:
            if "anchor" not in v:
                continue
            s, e = v["span"]
            f.write(f"### v.{v['verse']} — anchor {v['anchor']}, span {s}–{e}\n\n")
            f.write(f"- anchor line {v['anchor'][0]}: `{texts.line(v['anchor'][0])}`\n")
            f.write(f"- span first {s}: `{texts.line(s)}`\n")
            f.write(f"- span last {e}: `{texts.line(e)}`\n")
            if e + 1 <= texts.TRBH_LINE_COUNT:
                f.write(f"- next after span {e + 1}: `{texts.line(e + 1)}`\n")
            f.write("\n")

    n_anchored = sum("anchor" in v for v in result["verses"])
    print(f"anchored: {n_anchored}/30; unmatched units: {len(result['unmatched'])}")
    for p in problems:
        print(" -", p)
    print(f"wrote {OUT/'trimsika_alignment.json'} and alignment_report.md")
    print("ALIGN", "PASS" if n_anchored == 30 and not problems else "FAIL")
    return 0 if n_anchored == 30 and not problems else 1


if __name__ == "__main__":
    sys.exit(main())
