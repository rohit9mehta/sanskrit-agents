"""Ask-box (Phase 3, L6): cited question-answering over the library.

Design constraints (the whole point):
  * retrieval targets are the APPARATUSES (verified translations, term
    glosses, line-cited justifications) — never raw un-interpreted Sanskrit;
  * the answer is composed ONLY from retrieved passages, every claim
    carrying a citation the reader can click through;
  * if retrieval comes back empty/weak, the system says the library doesn't
    cover it — without calling the LLM at all;
  * citations in the answer are validated against the retrieved set; any
    fabricated reference is flagged, never silently shown.
"""

import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache

from .normalize import fold
from .texts import AGENT_DIR, DATA_DIR

OUTPUT = AGENT_DIR / "output"
MIN_SCORE = 3.0          # retrieval floor: below this → "not in my library"
TOP_K = 10

TEXT_META = {
    "trimsika": {"title": "Triṃśikā (Vasubandhu) with Sthiramati's bhāṣya",
                 "commentator": "Sthiramati", "tag": "trbh"},
    "isa": {"title": "Īśopaniṣad with Śaṅkara's bhāṣya",
            "commentator": "Śaṅkara", "tag": "isup"},
    "gita": {"title": "Bhagavad-Gītā with Śaṅkara's bhāṣya",
             "commentator": "Śaṅkara", "tag": "gita"},
    "yogasutra": {"title": "Yoga-sūtra with Vyāsa's bhāṣya",
                  "commentator": "Vyāsa", "tag": "ys"},
}


@dataclass
class Chunk:
    key: str            # e.g. "gita 2.47"
    slug: str
    unit: str
    kind: str           # translation | justification | term
    text: str           # what the LLM sees
    tokens: Counter     # folded token counts


def _tokens(text: str) -> Counter:
    return Counter(t for t in re.findall(r"[a-zA-Zāīūṛṝḷṃḥśṣñṅṇṭḍ']+", fold(text))
                   if len(t) > 1)


def _iter_apparatus_files():
    # Triṃśikā (legacy layout: output/vNN/)
    for p in sorted(OUTPUT.glob("v[0-9][0-9]/apparatus.json")):
        yield "trimsika", p
    # Library texts: output/<slug>/<unit_dir>/
    for slug in TEXT_META:
        if slug == "trimsika":
            continue
        for p in sorted((OUTPUT / slug).glob("*/apparatus.json")):
            yield slug, p


def _unit_of(slug: str, d: dict, path) -> str:
    if slug == "trimsika":
        return str(d.get("verse") or int(path.parent.name[1:]))
    return d.get("unit") or path.parent.name.replace("_", ".")


@lru_cache(maxsize=1)
def build_index() -> tuple[list[Chunk], dict]:
    chunks: list[Chunk] = []
    mula_by_key: dict[str, str] = {}
    for slug, path in _iter_apparatus_files():
        d = json.loads(path.read_text(encoding="utf-8"))
        unit = _unit_of(slug, d, path)
        key = f"{slug} {unit}"
        mula = d.get("mula") or d.get("verse_text") or ""
        if not mula and slug == "trimsika":
            mula = _trimsika_mula(unit)
        mula_by_key[key] = mula

        tr = d.get("translation", "")
        chunks.append(Chunk(key, slug, unit, "translation",
                            f"Verse/unit {key}: {mula}\nTranslation: {tr}",
                            _tokens(mula + " " + tr)))
        for j in d.get("justifications", []):
            ev = " ".join(f"[line {e['lines']}] {e['quote']} — {e['translation']}"
                          for e in j.get("evidence", []))
            body = (f"On {key} ({TEXT_META[slug]['commentator']}): "
                    f"{j['decision']} Chosen: {j['chosen']}. Evidence: {ev}")
            chunks.append(Chunk(key, slug, unit, "justification", body,
                                _tokens(body)))
        terms = "; ".join(
            f"{w['surface']} = {w['lemma']}" + (f" ({w['note']})" if w.get("note") else "")
            for w in d.get("analysis", []))
        if terms:
            chunks.append(Chunk(key, slug, unit, "term",
                                f"Word analyses for {key}: {terms}", _tokens(terms)))

    df: Counter = Counter()
    for c in chunks:
        df.update(set(c.tokens))
    n = max(1, len(chunks))
    idf = {t: math.log(n / (1 + k)) + 1 for t, k in df.items()}

    # Unit adjacency (numeric order within each text) + each unit's
    # translation chunk, for neighbor expansion in retrieve().
    def _ukey(u: str):
        try:
            return [int(x) for x in u.split(".")]
        except ValueError:
            return [0]
    unit_order = {slug: sorted({c.unit for c in chunks if c.slug == slug},
                               key=_ukey) for slug in TEXT_META}
    unit_pos = {(slug, u): i for slug, us in unit_order.items()
                for i, u in enumerate(us)}
    translation_chunk = {(c.slug, c.unit): c for c in chunks
                         if c.kind == "translation"}
    return chunks, {"idf": idf, "mula": mula_by_key, "unit_order": unit_order,
                    "unit_pos": unit_pos, "translation_chunk": translation_chunk}


@lru_cache(maxsize=1)
def _trimsika_mula_map() -> dict:
    mula = json.loads((DATA_DIR / "mula" / "trimsika.json").read_text())
    return {str(v["verse"]): v["bhasya_text"] for v in mula["verses"]}


def _trimsika_mula(unit: str) -> str:
    return _trimsika_mula_map().get(str(unit), "")


def retrieve(query: str, top_k: int = TOP_K) -> list[tuple[float, Chunk]]:
    chunks, aux = build_index()
    q = _tokens(query)
    scored = []
    for c in chunks:
        s = sum(aux["idf"].get(t, 0.0) * min(c.tokens[t], 3)
                for t in q if t in c.tokens)
        if s > 0:
            scored.append((s, c))
    scored.sort(key=lambda x: -x[0])
    top = scored[:top_k]

    # Continuation expansion: sūtra-style units continue each other ("tataḥ
    # ..." = "from that ..."), so the unit stating a topic's effect shares no
    # vocabulary with the question that names the topic. For each matched
    # unit (rank order), add the NEXT unit's translation chunk as context
    # (score 0 = context, not a match), a few at most.
    if top:
        have = {(c.slug, c.unit) for _, c in top}
        extras: list[tuple[float, Chunk]] = []
        for _, c in top:
            if len(extras) >= 5:
                break
            i = aux["unit_pos"].get((c.slug, c.unit))
            units = aux["unit_order"][c.slug]
            if i is None or i + 1 >= len(units) or (c.slug, units[i + 1]) in have:
                continue
            t = aux["translation_chunk"].get((c.slug, units[i + 1]))
            if t is not None:
                extras.append((0.0, t))
                have.add((c.slug, units[i + 1]))
        top += extras
    return top


ANSWER_SYSTEM = """You answer questions about Sanskrit śāstra using ONLY the numbered
passages provided. Write like a knowledgeable person talking to a curious
reader — plainly, briefly, no essay scaffolding.

Form:
1. Open with the answer itself, in one to three plain sentences. No labels
   ("Direct answer:", "In summary:"), no preamble, no restating the question.
2. If support helps, follow with at most three short bullets ("- "). Each
   bullet must ADD something — a distinction, the commentator's specific
   move, a caveat — never restate the opening in other words.
3. Keep the whole answer under about 120 words (citations excluded). Shorter
   is better if it answers the question.
4. Use at most two or three Sanskrit terms, in IAST, each with a short
   parenthetical gloss on first use. Do not gloss every word you translate;
   the reader asked a question, not for a vocabulary lesson.

Grounding, in priority order:
5. Every claim carries its citation in square brackets using the KEY shown in
   parentheses at the start of each passage — e.g. [gita 2.47] or
   [trimsika 2]. Never cite by passage number ([1], [2]); never invent keys.
   One citation per claim; do not stack three keys where one suffices.
6. Different commentators may disagree; attribute positions by commentator
   and text — never blend them into an unattributed consensus.
7. If the passages do not answer the question, say plainly that the texts in
   this library don't address it, and what is missing — do not fill gaps from
   your own knowledge. Never mention "passages", "provided", or retrieval;
   the reader sees a library, not a prompt.
"""


def _validate_citations(answer: str, allowed: set[str]) -> tuple[str, list[str]]:
    bad = []
    for m in re.findall(r"\[([a-z]+ [0-9][0-9.]*)\]", answer):
        if m not in allowed:
            bad.append(m)
    if bad:
        answer += ("\n\n⚠ The following citations did not match any retrieved "
                   f"passage and should be distrusted: {sorted(set(bad))}")
    return answer, bad


def ask(query: str, effort: str = "medium") -> dict:
    hits = retrieve(query)
    if not hits or hits[0][0] < MIN_SCORE:
        texts = ", ".join(sorted({TEXT_META[s]["title"] for s in
                                  {c.slug for _, c in (hits or [])}} |
                                 {m["title"] for m in TEXT_META.values()
                                  if (OUTPUT / "v01").exists()}))
        return {
            "answer": ("My library doesn't cover this yet. I can only answer "
                       "from texts on my shelf — currently: "
                       + "; ".join(sorted({m['title'] for m in TEXT_META.values()}))
                       + ". Onboarding a new text takes its digitized commentary "
                         "and about a day."),
            "citations": [], "passages": [], "llm": False,
        }

    passages = []
    for i, (s, c) in enumerate(hits, 1):
        passages.append(f"[{i}] ({c.key}, {c.kind}) {c.text}")
    user = (f"QUESTION: {query}\n\nPASSAGES:\n" + "\n\n".join(passages)
            + "\n\nAnswer per the rules.")

    from .llm import chat as _chat

    answer, usage = _chat(
        [{"role": "system", "content": ANSWER_SYSTEM},
         {"role": "user", "content": user}],
        str, tag="ask", effort=effort,
    )
    allowed = {c.key for _, c in hits}
    answer, bad = _validate_citations(answer, allowed)
    _, aux = build_index()
    return {
        "answer": answer,
        "citations": [
            {"key": c.key, "slug": c.slug, "unit": c.unit, "kind": c.kind,
             "score": round(s, 1), "mula": aux["mula"].get(c.key, "")}
            for s, c in hits
        ],
        "invalid_citations": bad,
        "usage": usage, "llm": True,
    }
