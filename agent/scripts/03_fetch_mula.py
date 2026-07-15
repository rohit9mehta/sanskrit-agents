"""Fetch the Triṃśikā root text and build agent/data/mula/trimsika.json
(Phase 0, CLAUDE.md item 2).

Sources (GRETIL plaintext, CC BY-NC-SA 4.0):
  - sa_vasubandhu-triMzikAvijJaptikArikA.txt        — vulgate kārikās (DSBC)
  - sa_vasubandhu-triMzikAvijJaptikArikA-comm.txt   — Buescher bhāṣya e-text,
    whose kārikā quote lines carry pāda labels ("| 1ab", "|| 1d", "2cd", "13")

The bhāṣya reading (assembled from the comm file's labeled lines) is PRIMARY —
it is what trbh.txt quotes; the vulgate is kept as a comparison column and
variant candidates are surfaced by skeleton diff.

Coverage check: every quote unit must fuzzy-hit a 1–3-line window of trbh.txt
(dry run of the pratīka-matcher's scorer). Report: data/mula/coverage_report.md
"""

import json
import re
import sys
from difflib import SequenceMatcher

import requests
from rapidfuzz import fuzz

from shastrartha import texts
from shastrartha.normalize import skeleton
from shastrartha.texts import DATA_DIR

RAW = DATA_DIR / "raw"
MULA = DATA_DIR / "mula"
BASE = "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext"
FILES = {
    "vulgate": "sa_vasubandhu-triMzikAvijJaptikArikA.txt",
    "comm": "sa_vasubandhu-triMzikAvijJaptikArikA-comm.txt",
}

PADAS = "abcd"
# A kārikā quote line: text, then an optional daṇḍa, then verse number 1-30
# with optional pāda letters, at end of line. Parenthesized labels — (25ab),
# (29a) — mark REQUOTES (pratīkas inside the exposition); unparenthesized
# labels mark the primary quote that introduces the verse.
LABEL_RE = re.compile(
    r"^(?P<text>.*?)[\s|]*(?P<paren>\()?(?P<num>[1-9]|[12][0-9]|30)"
    r"(?P<padas>[a-d]{1,4})?\)?\s*$"
)
PAGINATION_RE = re.compile(r"\s*\[tvbh_\d+\]\s*")
# One anuṣṭubh pāda ≈ 8 syllables ≈ 13+ skeleton chars; a captured unit much
# shorter than its label promises means the quote continues on the line above.
MIN_SKELETON_PER_PADA = 11


def fetch() -> dict[str, list[str]]:
    RAW.mkdir(parents=True, exist_ok=True)
    out = {}
    for key, name in FILES.items():
        path = RAW / name
        if not path.exists():
            r = requests.get(f"{BASE}/{name}", timeout=60)
            r.raise_for_status()
            path.write_text(r.text, encoding="utf-8")
            print(f"fetched {name}")
        out[key] = path.read_text(encoding="utf-8").split("\n")
    return out


def parse_vulgate(lines: list[str]) -> dict[int, dict[str, str]]:
    """{verse: {"ab": ..., "cd": ...}} from `... / ... // tvk_N //` blocks."""
    verses: dict[int, dict[str, str]] = {}
    buf: list[str] = []
    started = False
    for line in lines:
        line = line.strip()
        if line == "# Text":
            started = True
            continue
        if not started:
            continue
        m = re.search(r"//\s*tvk_(\d+)\s*//\s*$", line)
        if m:
            n = int(m.group(1))
            buf.append(re.sub(r"//\s*tvk_\d+\s*//\s*$", "", line).strip(" /|"))
            halves = [b.strip(" /|") for b in buf if b.strip(" /|")]
            if len(halves) != 2:
                raise ValueError(f"vulgate tvk_{n}: expected 2 halves, got {halves}")
            verses[n] = {"ab": halves[0], "cd": halves[1]}
            buf = []
        elif line and not line.startswith("#") and "tvk)" not in line:
            buf.append(line)
    return verses


def parse_comm_units(lines: list[str]) -> list[dict]:
    """Labeled kārikā quote units from the comm file (after '# Text').

    Handles quotes that span two physical lines with the label only on the
    second (e.g. v.29): if the captured text is too short for the label's
    pāda count, the preceding verse-text line is merged in."""
    units = []
    started = False
    for i, line in enumerate(lines, start=1):
        if line.strip() == "# Text":
            started = True
            continue
        if not started:
            continue
        clean = PAGINATION_RE.sub(" ", line).strip()
        if not clean or len(clean) > 130:  # quote lines are single kārikā lines
            continue
        m = LABEL_RE.match(clean)
        if not m or not m.group("text").strip(" |"):
            continue
        text = m.group("text").strip(" |")
        # Must look like Sanskrit verse text, not a stray numbered heading.
        if not re.search(r"[a-zāīūṛṝḷṃḥśṣñṅṇṭḍ]{4}", text):
            continue
        num = int(m.group("num"))
        padas = m.group("padas") or "abcd"
        if len(skeleton(text)) < MIN_SKELETON_PER_PADA * len(padas) and i >= 2:
            prev = PAGINATION_RE.sub(" ", lines[i - 2]).strip()
            if (
                prev
                and len(prev) <= 130
                and not LABEL_RE.match(prev)
                and re.search(r"[a-zāīūṛṝḷṃḥśṣñṅṇṭḍ]{4}", prev)
            ):
                text = prev.strip(" |") + " " + text
        units.append(
            {
                "verse": num,
                "padas": padas,
                "kind": "requote" if m.group("paren") else "primary",
                "text": text,
                "comm_line": i,
            }
        )
    return units


def tile(units: list[dict]) -> list[dict]:
    """Minimal non-overlapping subset of one verse's units covering a→d.
    Prefers longer units; drops anticipatory partial re-quotes (e.g. 7b
    inside 7bcd)."""
    chosen: list[dict] = []
    covered: set[str] = set()
    for u in sorted(
        units,
        key=lambda u: (
            PADAS.index(u["padas"][0]),
            -len(u["padas"]),
            u["kind"] != "primary",
        ),
    ):
        letters = set(u["padas"])
        if letters & covered:
            continue
        chosen.append(u)
        covered |= letters
    return sorted(chosen, key=lambda u: PADAS.index(u["padas"][0]))


def variant_hunks(bhasya: str, vulgate: str) -> list[dict]:
    """Skeleton-level diff hunks between the two readings, with context."""
    a, b = skeleton(bhasya), skeleton(vulgate)
    hunks = []
    for tag, i1, i2, j1, j2 in SequenceMatcher(None, a, b).get_opcodes():
        if tag == "equal":
            continue
        hunks.append(
            {
                "bhasya": a[max(0, i1 - 8): i2 + 8],
                "vulgate": b[max(0, j1 - 8): j2 + 8],
            }
        )
    return hunks


def best_window_hit(unit_text: str, windows: list[tuple[int, int, str]]) -> dict:
    """Best-scoring 1–3-line trbh window for a quote unit's skeleton."""
    sk = skeleton(unit_text)
    best = {"score": -1.0, "start": 0, "end": 0}
    for start, end, wsk in windows:
        score = fuzz.ratio(sk, wsk)
        if score > best["score"]:
            best = {"score": round(score, 1), "start": start, "end": end}
    return best


def trbh_windows(max_width: int = 3) -> list[tuple[int, int, str]]:
    n = texts.TRBH_LINE_COUNT
    line_sk = [skeleton(texts.line(i)) for i in range(1, n + 1)]
    windows = []
    for width in range(1, max_width + 1):
        for start in range(1, n - width + 2):
            windows.append(
                (start, start + width - 1, "".join(line_sk[start - 1: start + width - 1]))
            )
    return windows


def main() -> int:
    raw = fetch()
    vulgate = parse_vulgate(raw["vulgate"])
    units = parse_comm_units(raw["comm"])

    by_verse: dict[int, list[dict]] = {}
    for u in units:
        by_verse.setdefault(u["verse"], []).append(u)

    print(f"vulgate verses: {len(vulgate)}; comm quote units: {len(units)} "
          f"covering verses {sorted(by_verse)}")

    windows = trbh_windows()
    verses, problems = [], []
    for n in range(1, 31):
        vu = vulgate.get(n)
        cu = by_verse.get(n, [])
        tiled = tile(cu)
        covered = "".join(sorted(set("".join(u["padas"] for u in tiled))))
        bhasya_text = " ".join(u["text"] for u in tiled)
        if not vu:
            problems.append(f"v.{n}: missing from vulgate")
        if covered != "abcd":
            problems.append(f"v.{n}: comm units cover only '{covered}'")

        for u in cu:
            u["trbh_hit"] = best_window_hit(u["text"], windows)
            if u["trbh_hit"]["score"] < 70:
                problems.append(
                    f"v.{n} unit {u['padas']}: weak trbh hit "
                    f"{u['trbh_hit']['score']} at {u['trbh_hit']['start']}"
                )

        verses.append(
            {
                "verse": n,
                "vulgate": vu,
                "bhasya_units": cu,
                "bhasya_text": bhasya_text,
                "variants": variant_hunks(
                    bhasya_text, f"{vu['ab']} {vu['cd']}" if vu else ""
                ),
            }
        )

    MULA.mkdir(parents=True, exist_ok=True)
    (MULA / "trimsika.json").write_text(
        json.dumps(
            {
                "sources": {
                    "vulgate": f"{BASE}/{FILES['vulgate']}",
                    "comm": f"{BASE}/{FILES['comm']}",
                    "fetched": "2026-07-15",
                    "license": "CC BY-NC-SA 4.0 (GRETIL)",
                },
                "verses": verses,
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )

    with (MULA / "coverage_report.md").open("w", encoding="utf-8") as f:
        f.write("# Triṃśikā coverage check: mūla ↔ trbh.txt\n\n")
        f.write("| verse | comm units | pādas | best trbh hits (lines @ score) | variants |\n")
        f.write("|---|---|---|---|---|\n")
        for v in verses:
            hits = "; ".join(
                f"{u['padas']}→{u['trbh_hit']['start']}"
                + (f"–{u['trbh_hit']['end']}" if u['trbh_hit']['end'] != u['trbh_hit']['start'] else "")
                + f"@{u['trbh_hit']['score']}"
                for u in v["bhasya_units"]
            )
            nvar = len(v["variants"])
            f.write(
                f"| {v['verse']} | {len(v['bhasya_units'])} | "
                f"{''.join(sorted(set(''.join(u['padas'] for u in v['bhasya_units']))))} | "
                f"{hits} | {nvar} |\n"
            )
        f.write(f"\ncolophon (trbh {texts.TRBH_LINE_COUNT - 1}–{texts.TRBH_LINE_COUNT}): "
                f"`{texts.line(texts.TRBH_LINE_COUNT - 1)} / {texts.line(texts.TRBH_LINE_COUNT)}`\n")
        if problems:
            f.write("\n## Problems\n\n" + "\n".join(f"- {p}" for p in problems) + "\n")
        else:
            f.write("\nNo problems: 30/30 verses, full pāda coverage, all units hit trbh.\n")

    print(f"wrote {MULA/'trimsika.json'} and coverage_report.md")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print(" -", p)
    print("MULA COVERAGE", "PASS" if not problems else "FAIL")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
