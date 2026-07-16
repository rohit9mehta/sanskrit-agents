"""Verify runner (Phase 1, W2): map every WordAnalysis in an Apparatus to the
right vidyut verifier, with NO silent drops — every word gets a status:

  pass        — claim licensed (for compounds: opaque-stem derivation passes)
  fail        — claim checked and rejected (feeds the retry prompt)
  unsupported — not expressible in vidyut (samāsa relations, unknown avyayas)
  tool_error  — vidyut raised; surfaced, not hidden
"""

import re
from dataclasses import dataclass, field

from . import verify
from .schema import Apparatus, WordAnalysis

_IND_RE = re.compile(r"(^|[\s(¦])ind\.")


def _mw_says_indeclinable(surface_iast: str) -> bool:
    from .dictionary import mw_entries

    try:
        return any(_IND_RE.search(e["text"]) for e in mw_entries(surface_iast, limit=8))
    except Exception:
        return False


@dataclass
class WordResult:
    surface: str
    status: str
    detail: str = ""
    expected: list[str] = field(default_factory=list)


@dataclass
class VerifyReport:
    words: list[WordResult]

    @property
    def n(self) -> dict:
        out = {"pass": 0, "fail": 0, "unsupported": 0, "tool_error": 0}
        for w in self.words:
            out[w.status] = out.get(w.status, 0) + 1
        return out

    @property
    def failures(self) -> list[WordResult]:
        return [w for w in self.words if w.status in ("fail", "tool_error")]

    def feedback(self) -> str:
        """Error report for the retry turn."""
        lines = []
        for w in self.failures:
            lines.append(
                f"- {w.surface}: {w.detail}"
                + (f" (the claimed analysis derives: {', '.join(w.expected[:8])})"
                   if w.expected else "")
            )
        return "\n".join(lines)


def _ctx(verse: int) -> dict:
    return {"text": "trbh", "line": None, "verse": str(verse), "stage": "pipeline"}


def verify_word(w: WordAnalysis, verse: int, run_id: str) -> WordResult:
    ctx = _ctx(verse)
    m = w.morph
    try:
        if w.samasa is not None:
            if m.pos != "subanta" or not (m.linga and m.vibhakti and m.vacana):
                return WordResult(
                    w.surface, "fail",
                    "compound claimed but subanta features (linga/vibhakti/vacana) missing",
                )
            res = verify.verify_compound_claim(
                w.surface, w.lemma, m.linga, m.vibhakti, m.vacana,
                w.samasa.type, w.samasa.vigraha, w.samasa.members,
                run_id=run_id, context=ctx, source="reasoner",
            )
            stem = res["stem"]
            detail = (
                f"compound stem {w.lemma} as {m.linga}/{m.vibhakti}/{m.vacana}: "
                f"{stem['result']}; relation {w.samasa.type}: unsupported (logged)"
            )
            return WordResult(w.surface, res["status"], detail, stem["expected_forms"])

        if m.pos == "subanta":
            if not (m.linga and m.vibhakti and m.vacana):
                return WordResult(w.surface, "fail", "subanta missing linga/vibhakti/vacana")
            rec = verify.verify_subanta_claim(
                w.surface, w.lemma, m.linga, m.vibhakti, m.vacana,
                run_id=run_id, context=ctx, source="reasoner",
            )
            return WordResult(
                w.surface, rec["result"],
                f"{w.lemma} {m.linga}/{m.vibhakti}/{m.vacana}: {rec['result']}",
                rec["expected_forms"],
            )

        if m.pos == "tinanta":
            if not (m.root and m.prayoga and m.lakara and m.purusha and m.vacana):
                return WordResult(w.surface, "fail", "tinanta missing root/prayoga/lakara/purusha/vacana")
            rec = verify.verify_tinanta_claim(
                w.surface, m.root, m.prefixes or [], m.prayoga, m.lakara, m.purusha, m.vacana,
                run_id=run_id, context=ctx, source="reasoner",
            )
            return WordResult(
                w.surface, rec["result"],
                f"{'-'.join((m.prefixes or []) + [m.root])} {m.lakara}/{m.purusha}/{m.vacana}: {rec['result']}",
                rec["expected_forms"],
            )

        # avyaya: kosha known-form check first; where the kosha lacks an
        # avyaya entry (a known coverage gap for taddhita adverbs like
        # tridhā, sadā), MW arbitrates: an "ind." marker on the headword
        # passes the claim with method recorded as MW, not Pāṇini.
        key, entries = verify.kosha_lookup(w.surface)
        if entries and any(e.is_avyaya for e in entries):
            verify.kosha_check(w.surface, run_id=run_id, context=ctx, source="reasoner")
            return WordResult(w.surface, "pass", "avyaya known to kosha")
        if _mw_says_indeclinable(w.surface):
            verify.mark_unsupported(
                w.surface,
                "avyaya not in kosha (coverage gap); MW marks the headword 'ind.' "
                "— accepted on MW's authority",
                run_id=run_id, context=ctx, source="reasoner",
            )
            return WordResult(w.surface, "pass", "avyaya per MW (kosha gap; logged unsupported)")
        if entries:
            verify.kosha_check(w.surface, run_id=run_id, context=ctx, source="reasoner",
                               notes="claimed avyaya; kosha entries are inflected forms")
            return WordResult(
                w.surface, "fail",
                "claimed avyaya, but kosha knows this form only as an inflected pada "
                "and MW does not mark it 'ind.'",
            )
        verify.mark_unsupported(
            w.surface, "claimed avyaya; not in kosha, no MW 'ind.' entry",
            run_id=run_id, context=ctx, source="reasoner",
        )
        return WordResult(w.surface, "unsupported", "avyaya not in kosha or MW")
    except Exception as e:  # defensive: a schema surprise must not kill the run
        return WordResult(w.surface, "tool_error", f"{type(e).__name__}: {e}")


def pipeline_verify(app: Apparatus, run_id: str) -> VerifyReport:
    return VerifyReport([verify_word(w, app.verse, run_id) for w in app.analysis])
