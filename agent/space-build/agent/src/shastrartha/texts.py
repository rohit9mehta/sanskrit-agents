"""Canonical access to the Triṃśikā-bhāṣya text files.

Invariant: trbh.txt is the project's line space — 1,560 lines, 1-indexed,
never edited. All commentary citations everywhere in the project are
trbh.txt line numbers. Two trailing spaces on a line mark a sentence
(daṇḍa) boundary; the ~5 clauses missing vs. GRETIL-comm are recorded in
agent/data/MANIFEST.md and must NOT be patched in.
"""

from functools import lru_cache
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
AGENT_DIR = PROJECT_ROOT / "agent"
DATA_DIR = AGENT_DIR / "data"
LOGS_DIR = AGENT_DIR / "logs"

TRBH_PATH = PROJECT_ROOT / "data" / "input" / "trbh.txt"
UNSANDHIED_PATH = PROJECT_ROOT / "data" / "input" / "trbh.txt.unsandhied"
TRBH_LINE_COUNT = 1560


def _load(path: Path) -> tuple[str, ...]:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()  # file-final newline
    if len(lines) != TRBH_LINE_COUNT:
        raise AssertionError(
            f"{path.name}: expected {TRBH_LINE_COUNT} lines, got {len(lines)} — "
            "the file must never be edited"
        )
    return tuple(lines)


@lru_cache(maxsize=1)
def trbh_lines() -> tuple[str, ...]:
    """All lines of trbh.txt, trailing spaces preserved (they carry meaning)."""
    return _load(TRBH_PATH)


@lru_cache(maxsize=1)
def unsandhied_lines() -> tuple[str, ...]:
    """All lines of trbh.txt.unsandhied (2022 model output — known ~15% line
    error rate; convenience gloss only, never an alignment source)."""
    return _load(UNSANDHIED_PATH)


def line(n: int) -> str:
    """1-indexed trbh.txt line, trailing whitespace stripped."""
    return trbh_lines()[n - 1].rstrip()


def unsandhied_line(n: int) -> str:
    return unsandhied_lines()[n - 1].rstrip()


def is_sentence_end(n: int) -> bool:
    """True if 1-indexed line n ends a sentence (two trailing spaces in trbh.txt)."""
    return trbh_lines()[n - 1].endswith("  ")


def span(start: int, end: int) -> list[tuple[int, str]]:
    """Inclusive 1-indexed range of (line_number, stripped_text)."""
    return [(n, line(n)) for n in range(start, end + 1)]
