"""Pratīka-matcher: align kārikā quote units to trbh.txt lines and derive
each verse's commentary span.

Design (reusable beyond the Triṃśikā):
  * match unit = a mūla quote unit (pāda / half-verse / full verse) scored by
    rapidfuzz against skeletons of 1–3-line windows of the commentary;
  * context signals raise confidence but are never required — quotes may be
    syntactically integrated with no āha/iti marking (e.g. v.3ab at trbh 202);
  * global monotonicity: quote units occur in commentary order, so each unit
    takes its best candidate at-or-after the previous unit's anchor;
  * span for verse N = after its first primary unit, up to just before the
    avatāraṇikā (intro sentence ending in `āha`) of verse N+1's first unit.

The 2022 .unsandhied file is deliberately NOT used here (model output with
known errors); matching runs on trbh.txt only.
"""

from dataclasses import asdict, dataclass, field

from rapidfuzz import fuzz

from . import texts
from .normalize import skeleton

DEFAULT_THRESHOLD = 85.0
MAX_WINDOW = 3


@dataclass
class Window:
    start: int
    end: int
    skeleton: str


@dataclass
class UnitHit:
    verse: int
    padas: str
    kind: str            # primary | requote
    comm_line: int       # line in the GRETIL comm file (provenance)
    text: str
    lines: list[int]     # matched trbh lines [start, end]
    score: float
    signals: list[str] = field(default_factory=list)


def build_windows(max_window: int = MAX_WINDOW) -> list[Window]:
    n = texts.TRBH_LINE_COUNT
    line_sk = [skeleton(texts.line(i)) for i in range(1, n + 1)]
    windows = []
    for width in range(1, max_window + 1):
        for start in range(1, n - width + 2):
            windows.append(
                Window(start, start + width - 1, "".join(line_sk[start - 1 : start + width - 1]))
            )
    return windows


def signals_for(start: int, end: int) -> list[str]:
    sig = []
    if start > 1 and texts.line(start - 1).endswith("āha"):
        sig.append("prev-āha")
    if end < texts.TRBH_LINE_COUNT and texts.line(end + 1) == "iti":
        sig.append("next-iti")
    if any(texts.is_sentence_end(i) for i in range(start, end + 1)):
        sig.append("sentence-end")
    return sig


def candidates(
    unit_text: str, windows: list[Window], threshold: float = DEFAULT_THRESHOLD
) -> list[tuple[Window, float]]:
    """Score a unit against every window; keep hits ≥ threshold.
    Uses ratio for full quotes and partial_ratio to catch truncated pratīkas
    quoted inside a longer line."""
    sk = skeleton(unit_text)
    hits = []
    for w in windows:
        score = fuzz.ratio(sk, w.skeleton)
        if score < threshold and len(sk) <= len(w.skeleton):
            score = fuzz.partial_ratio(sk, w.skeleton) * 0.98  # slight penalty
        if score >= threshold:
            hits.append((w, round(score, 1)))
    return hits


def _dedupe_overlapping(hits: list[tuple[Window, float]]) -> list[tuple[Window, float]]:
    """Among overlapping windows keep the best-scoring, narrowest one."""
    hits = sorted(hits, key=lambda h: (-h[1], h[0].end - h[0].start, h[0].start))
    kept: list[tuple[Window, float]] = []
    for w, s in hits:
        if not any(w.start <= k.end and k.start <= w.end for k, _ in kept):
            kept.append((w, s))
    return sorted(kept, key=lambda h: h[0].start)


def align_units(
    units: list[dict], windows: list[Window] | None = None,
    threshold: float = DEFAULT_THRESHOLD,
) -> tuple[list[UnitHit], list[dict]]:
    """Assign each quote unit (in commentary order) its trbh location,
    enforcing global monotonicity. Returns (hits, unmatched)."""
    windows = windows or build_windows()
    hits: list[UnitHit] = []
    unmatched: list[dict] = []
    cursor = 0
    for u in sorted(units, key=lambda u: u["comm_line"]):
        cands = _dedupe_overlapping(candidates(u["text"], windows, threshold))
        viable = [(w, s) for w, s in cands if w.start >= cursor]
        if not viable:
            unmatched.append(u)
            continue
        best_score = max(s for _, s in viable)
        w, s = next((w, s) for w, s in viable if s >= best_score - 0.5)
        hits.append(
            UnitHit(
                verse=u["verse"],
                padas=u["padas"],
                kind=u["kind"],
                comm_line=u["comm_line"],
                text=u["text"],
                lines=[w.start, w.end],
                score=s,
                signals=signals_for(w.start, w.end),
            )
        )
        cursor = w.start
    return hits, unmatched


def avataranika_start(anchor_start: int) -> int:
    """If the line before an anchor ends in `āha`, the whole sentence that
    ends there is the avatāraṇikā introducing the quote; return its first
    line. Otherwise return the anchor itself."""
    j = anchor_start - 1
    if j < 1:
        return anchor_start
    if not texts.line(j).endswith("āha"):
        return anchor_start
    k = j - 1
    while k >= 1 and not texts.is_sentence_end(k):
        k -= 1
    return k + 1


def derive_spans(hits: list[UnitHit]) -> dict[int, dict]:
    """Per-verse commentary spans from the aligned unit hits."""
    anchors: dict[int, UnitHit] = {}
    for h in hits:
        if h.kind == "primary" and h.verse not in anchors:
            anchors[h.verse] = h

    verses = sorted(anchors)
    spans: dict[int, dict] = {}
    for i, v in enumerate(verses):
        a = anchors[v]
        raw_start = a.lines[1] + 1
        while raw_start <= texts.TRBH_LINE_COUNT and texts.line(raw_start) == "iti":
            raw_start += 1  # quote-closing iti belongs to the quote, not the gloss
        if i + 1 < len(verses):
            nxt = anchors[verses[i + 1]]
            raw_end = nxt.lines[0] - 1
            adj_end = avataranika_start(nxt.lines[0]) - 1
        else:
            raw_end = adj_end = texts.TRBH_LINE_COUNT - 2  # before colophon
        spans[v] = {
            "anchor": [a.lines[0], a.lines[1]],
            "span_raw": [raw_start, raw_end],
            "span": [raw_start, max(raw_start, adj_end)],
        }
    # Verses quoted back-to-back (e.g. 29+30 `ślokadvayena`) share the
    # following exposition: an empty raw span inherits the next verse's span.
    for v in reversed(verses):
        s = spans[v]
        if s["span_raw"][1] < s["span_raw"][0]:
            nxt = next((u for u in verses if u > v and spans[u]["span_raw"][1] >= spans[u]["span_raw"][0]), None)
            if nxt is not None:
                s["span"] = list(spans[nxt]["span"])
                s["shared_with"] = nxt
    return spans


def align(mula: dict, threshold: float = DEFAULT_THRESHOLD) -> dict:
    """Full alignment from a trimsika.json-shaped mūla dict."""
    units = [u for v in mula["verses"] for u in v["bhasya_units"]]
    windows = build_windows()
    hits, unmatched = align_units(units, windows, threshold)
    spans = derive_spans(hits)

    verses = []
    for v in mula["verses"]:
        n = v["verse"]
        vhits = [h for h in hits if h.verse == n]
        verses.append(
            {
                "verse": n,
                "units": [asdict(h) for h in vhits],
                "requotes": [asdict(h) for h in vhits if h.kind == "requote"],
                **spans.get(n, {}),
                "confidence": min((h.score for h in vhits), default=0.0),
                "checked_by_human": False,
            }
        )
    return {
        "threshold": threshold,
        "unmatched": unmatched,
        "verses": verses,
    }
