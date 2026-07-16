"""RETRIEVE stage (Phase 1, W3): assemble everything the reasoner sees for one
verse, from the Phase 0 artifacts. Hand-run friction items #4 (span lookahead)
and #5 (requote loci) are addressed here.
"""

import json
from dataclasses import dataclass, field
from functools import lru_cache

from . import texts
from .dictionary import mw_entries
from .texts import DATA_DIR

MULA = DATA_DIR / "mula" / "trimsika.json"
ALIGNMENT = DATA_DIR / "alignment" / "trimsika_alignment.json"
LOOKAHEAD = 3  # lines shown past the next verse's anchor, marked as such


@dataclass
class RetrievalBundle:
    verse: int
    verse_text: str                      # bhāṣya reading
    vulgate_text: str
    variants: list[dict]
    anchor: list[int]
    span: list[int]
    shared_with: int | None
    span_lines: list[str]                # "N\ttext" with [lookahead] markers
    requotes: list[dict]                 # {padas, lines, context: ["N\ttext"...]}
    unsandhied_lines: list[str]
    analyze: dict                        # per anchor line: api_seg / local_S / local_SLM
    mw: dict                             # lemma -> [entries]

    def commentary_block(self) -> str:
        out = "\n".join(self.span_lines)
        for r in self.requotes:
            out += f"\n\n[requote of {r['padas']} at trbh {r['lines']}]:\n" + "\n".join(r["context"])
        return out


@lru_cache(maxsize=1)
def _mula() -> dict:
    return json.loads(MULA.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _alignment() -> dict:
    return json.loads(ALIGNMENT.read_text(encoding="utf-8"))


def _numbered(a: int, b: int, tag: str = "") -> list[str]:
    b = min(b, texts.TRBH_LINE_COUNT)
    return [f"{n}\t{texts.line(n)}{tag}" for n in range(a, b + 1)]


def retrieve(verse_n: int, analyze_fn=None) -> RetrievalBundle:
    """analyze_fn(lines: list[str]) -> dict — injected so the (heavy) model
    load stays in the caller and stays resident across verses."""
    mv = next(v for v in _mula()["verses"] if v["verse"] == verse_n)
    av = next(v for v in _alignment()["verses"] if v["verse"] == verse_n)

    s, e = av["span"]
    span_lines = _numbered(s, e)
    span_lines += [x + "   [lookahead]" for x in _numbered(e + 1, e + LOOKAHEAD)]

    requotes = []
    for h in av.get("requotes", []):
        a, b = h["lines"]
        if s <= a <= e:  # inside the span already shown
            continue
        requotes.append(
            {"padas": h["padas"], "lines": h["lines"],
             "context": _numbered(max(1, a - 1), min(texts.TRBH_LINE_COUNT, b + 2))}
        )

    # ANALYZE every primary quote line of the verse (not just the first
    # anchor): v.2's cd-pāda lives in a second unit at trbh 177.
    quote_line_nums: list[int] = []
    for u in av.get("units", []):
        if u["kind"] == "primary":
            quote_line_nums.extend(range(u["lines"][0], u["lines"][1] + 1))
    quote_line_nums = sorted(set(quote_line_nums)) or list(
        range(av["anchor"][0], av["anchor"][1] + 1)
    )
    analyze = analyze_fn([texts.line(n) for n in quote_line_nums]) if analyze_fn else {}
    if analyze:
        analyze["lines_analyzed"] = quote_line_nums

    # MW lookups: lemmas from the SLM analysis (3rd field of each triple)
    lemmas: list[str] = []
    for parsed in analyze.get("slm_parsed", []):
        for tok in parsed:
            lem = tok.get("lemma")
            if lem and lem not in lemmas:
                lemmas.append(lem)
    mw = {}
    for lem in lemmas:
        try:
            entries = mw_entries(lem, limit=4)
        except Exception:
            entries = []
        if entries:
            mw[lem] = [
                {"citation": x["citation"], "text": x["text"][:400]} for x in entries[:3]
            ]

    return RetrievalBundle(
        verse=verse_n,
        verse_text=mv["bhasya_text"],
        vulgate_text=(f"{mv['vulgate']['ab']} / {mv['vulgate']['cd']}" if mv["vulgate"] else ""),
        variants=mv["variants"],
        anchor=av["anchor"],
        span=av["span"],
        shared_with=av.get("shared_with"),
        span_lines=span_lines,
        requotes=requotes,
        unsandhied_lines=[
            f"{n}\t{texts.unsandhied_line(n)}" for n in range(s, min(e, texts.TRBH_LINE_COUNT) + 1)
        ],
        analyze=analyze,
        mw=mw,
    )
