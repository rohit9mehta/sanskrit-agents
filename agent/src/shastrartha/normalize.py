"""IAST normalization for fuzzy matching.

Two levels:
  fold(s)     — NFC, lowercase, diacritics folded to ASCII, separator noise
                (hyphens/underscores/daṇḍas/avagraha/digits) removed, spaces kept.
  skeleton(s) — fold + all whitespace removed. Absorbs word-spacing and most
                word-boundary sandhi notation differences; residual differences
                (real variants, vowel sandhi) are the fuzzy scorer's job.
"""

import re
import unicodedata

# IAST -> ASCII skeleton. Applied after NFC + casefold, so only lowercase
# precomposed forms need entries.
_FOLD_MAP = {
    "ā": "a", "ī": "i", "ū": "u",
    "ṛ": "r", "ṝ": "r", "ḷ": "l", "ḹ": "l",
    "ṃ": "m", "ṁ": "m",  # candrabindu (m̐) is handled by the NFD strip below
    "ḥ": "h",
    "ś": "s", "ṣ": "s",
    "ñ": "n", "ṅ": "n", "ṇ": "n",
    "ṭ": "t", "ḍ": "d",
}
_FOLD_TABLE = str.maketrans(_FOLD_MAP)

# Characters that are notation, not text: avagraha/apostrophes, hyphens,
# underscores (Dharmamitra separators), daṇḍas, digits, brackets, dots.
_NOISE_RE = re.compile(r"[''`\-_—–|।॥\[\]().:;,!?\"0-9]")
_WS_RE = re.compile(r"\s+")


def fold(s: str) -> str:
    s = unicodedata.normalize("NFC", s).casefold()
    s = s.translate(_FOLD_TABLE)
    # Strip any remaining combining marks (defensive: decomposed input)
    s = "".join(
        c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)
    )
    s = _NOISE_RE.sub("", s)
    return _WS_RE.sub(" ", s).strip()


def skeleton(s: str) -> str:
    return fold(s).replace(" ", "")


def seg_tokens(s: str) -> list[str]:
    """Tokens of a segmented string, treating '-', '_' and whitespace all as
    boundaries — makes Dharmamitra output, the 2022 .unsandhied file, and
    local-model output comparable."""
    s = unicodedata.normalize("NFC", s).casefold()
    s = re.sub(r"[-_=+]", " ", s)
    return [skeleton(t) for t in s.split() if skeleton(t)]
