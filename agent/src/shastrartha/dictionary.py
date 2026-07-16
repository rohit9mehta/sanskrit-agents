"""Monier-Williams dictionary module (Phase 1, W1).

Primary source: Cologne csl-orig master file (mw.txt, SLP1 headwords with
native page,column fields), parsed once into data/mw/mw.sqlite by
scripts/10_build_mw.py. Lookups are IAST in / IAST out, with a ready-made
citation string ("MW s.v. X, page,col").

Fallback (sqlite absent): the live Cologne getword.php scrape used in the
Phase 0 hand-run, cached to disk.
"""

import html
import json
import re
import sqlite3
from functools import lru_cache

import requests

from .texts import DATA_DIR
from .verify import to_iast, to_slp1

MW_SQLITE = DATA_DIR / "mw" / "mw.sqlite"
MW_RAW = DATA_DIR / "raw" / "mw" / "mw.txt"
SCRAPE_CACHE = DATA_DIR / "cache" / "mw_scrape"
GETWORD_URL = (
    "https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php"
)

_S_TAG_RE = re.compile(r"<s>(.*?)</s>")
_S1_TAG_RE = re.compile(r"<s1>(.*?)</s1>")
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def _render_body(body: str) -> str:
    """Cologne markup → readable IAST text: <s>SLP1</s> transliterated,
    other tags stripped (their visible content kept)."""
    body = _S_TAG_RE.sub(lambda m: to_iast(m.group(1).replace("—", "-")), body)
    body = _S1_TAG_RE.sub(lambda m: m.group(1), body)
    body = _TAG_RE.sub("", body)
    return _WS_RE.sub(" ", html.unescape(body)).strip()


@lru_cache(maxsize=1)
def _conn() -> sqlite3.Connection | None:
    if not MW_SQLITE.exists():
        return None
    conn = sqlite3.connect(f"file:{MW_SQLITE}?mode=ro", uri=True, check_same_thread=False)
    return conn


def mw_entries(lemma_iast: str, limit: int = 8) -> list[dict]:
    """MW entries for a lemma (IAST). Each: {lemma, key_slp1, lnum, page_col,
    text, citation}. Empty list if the headword is absent."""
    key = to_slp1(lemma_iast.strip())
    conn = _conn()
    if conn is not None:
        rows = conn.execute(
            "SELECT lnum, pc, body FROM entries WHERE key = ? ORDER BY CAST(lnum AS REAL) LIMIT ?",
            (key, limit),
        ).fetchall()
        return [
            {
                "lemma": lemma_iast,
                "key_slp1": key,
                "lnum": lnum,
                "page_col": pc,
                "text": _render_body(body),
                "citation": f"MW s.v. {lemma_iast}, {pc}",
            }
            for lnum, pc, body in rows
        ]
    return _scrape_entries(lemma_iast, key, limit)


def _scrape_entries(lemma_iast: str, key: str, limit: int) -> list[dict]:
    """Live-scrape fallback, disk-cached. Coarser: one blob per headword,
    no per-entry page/col split."""
    SCRAPE_CACHE.mkdir(parents=True, exist_ok=True)
    cache = SCRAPE_CACHE / f"{key}.json"
    if cache.exists():
        blob = json.loads(cache.read_text())
    else:
        resp = requests.post(
            GETWORD_URL,
            data={"key": key, "filter": "deva", "accent": "no", "transLit": "slp1"},
            timeout=30,
        )
        resp.raise_for_status()
        text = _TAG_RE.sub(" ", resp.text)
        text = _WS_RE.sub(" ", html.unescape(text)).strip()
        m = re.search(r"\[Printed book page (\d+\s*,\s*\d+)\]", text)
        blob = {"text": text[:4000], "page_col": m.group(1).replace(" ", "") if m else "?"}
        cache.write_text(json.dumps(blob, ensure_ascii=False))
    if not blob["text"]:
        return []
    return [
        {
            "lemma": lemma_iast,
            "key_slp1": key,
            "lnum": None,
            "page_col": blob["page_col"],
            "text": blob["text"],
            "citation": f"MW s.v. {lemma_iast}, {blob['page_col']} (scrape)",
        }
    ][:limit]
