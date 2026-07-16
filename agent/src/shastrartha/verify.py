"""VERIFY stage: check morphological claims against Pāṇinian grammar (vidyut).

Two methods:
  prakriya — generative check: derive all surface forms the claimed analysis
             licenses (vidyut-prakriya) and require the observed surface to be
             among them. Produces a sūtra-numbered derivation trace.
  kosha    — lexicon check: look the surface form up in vidyut-kosha and test
             whether any stored analysis is consistent with the claim.

Every check — pass or fail — is appended to
agent/logs/vidyut_verifications.jsonl (CLAUDE.md convention: this log seeds
the "Pāṇini as reward function" research thread).

Result classes:
  pass        — claim licensed by the grammar/lexicon
  fail        — claim checked and rejected
  unsupported — claim not expressible in vidyut (e.g. a samāsa *relation*;
                verify compound members instead). Distinct from fail.
  tool_error  — vidyut raised; no verdict.

Conventions: claims arrive in IAST; vidyut speaks SLP1; enum fields use
vidyut member names (Linga: Pum/Stri/Napumsaka; Vibhakti: Prathama..Saptami,
Sambodhana; Vacana: Eka/Dvi/Bahu; Prayoga: Kartari/Karmani/Bhave;
Lakara: Lat/Lan/Lit/Lut/Lrt/Lot/Lun/Lrn/VidhiLin/AshirLin;
Purusha: Prathama/Madhyama/Uttama).
"""

import json
import re
from datetime import datetime, timezone
from functools import lru_cache
from typing import Any

from vidyut import lipi
from vidyut.kosha import Kosha
from vidyut import prakriya as pk

from .texts import DATA_DIR, LOGS_DIR

VIDYUT_DATA = DATA_DIR / "vidyut-0.4.0"
LOG_PATH = LOGS_DIR / "vidyut_verifications.jsonl"

MAX_TRACE_STEPS = 60


# ---------------------------------------------------------------- lipi

def to_slp1(iast: str) -> str:
    return lipi.transliterate(iast, lipi.Scheme.Iast, lipi.Scheme.Slp1)


def to_iast(slp1: str) -> str:
    return lipi.transliterate(slp1, lipi.Scheme.Slp1, lipi.Scheme.Iast)


# ---------------------------------------------------------------- singletons

@lru_cache(maxsize=1)
def kosha() -> Kosha:
    return Kosha(str(VIDYUT_DATA / "kosha"))


@lru_cache(maxsize=1)
def vyakarana() -> pk.Vyakarana:
    return pk.Vyakarana()


@lru_cache(maxsize=1)
def dhatu_entries() -> list:
    return pk.Data(str(VIDYUT_DATA / "prakriya")).load_dhatu_entries()


# ---------------------------------------------------------------- helpers

def _enum(cls, name: str):
    """Resolve a claim's enum field ('Sasthi') to a vidyut enum member."""
    member = getattr(cls, name, None)
    if member is not None:
        return member
    try:
        return cls.from_string(name)
    except Exception:
        raise ValueError(
            f"{cls.__name__}: unknown value {name!r}; choices: "
            f"{[str(c) for c in cls.choices()]}"
        ) from None


# Anusvāra vs homorganic nasal are orthographic variants of the same word
# (text: saṃjñita; vidyut derivation: saYjYita). Canonicalize any nasal
# before a stop to M so surface matching is spelling-insensitive.
_NASAL_EQ = re.compile(r"[NYRnm](?=[kKgGcCjJwWqQtTdDpPbB])")


def normalize_nasals(slp1: str) -> str:
    return _NASAL_EQ.sub("M", slp1)


def forms_match(surface_slp1: str, derived: list[str]) -> str | None:
    """The derived form equal to the surface up to nasal orthography."""
    want = normalize_nasals(surface_slp1)
    for d in derived:
        if normalize_nasals(d) == want:
            return d
    return None


def kosha_key_candidates(surface_slp1: str) -> list[str]:
    """The kosha stores pausal/underlying finals (devas, not devaH)."""
    cands = [surface_slp1]
    if surface_slp1.endswith("H"):
        cands += [surface_slp1[:-1] + "s", surface_slp1[:-1] + "r"]
    if surface_slp1.endswith("M"):
        cands.append(surface_slp1[:-1] + "m")
    return cands


def kosha_lookup(surface_iast: str) -> tuple[str | None, list]:
    """Return (keys_that_hit, union of entries) across ALL pausal-key
    candidates — visarga forms can hide distinct words under -s and -r
    finals (punaḥ: subanta junk under `punas`, the avyaya under `punar`)."""
    hits, entries = [], []
    for key in kosha_key_candidates(to_slp1(surface_iast)):
        found = kosha().get(key)
        if found:
            hits.append(key)
            entries.extend(found)
    return (",".join(hits) if hits else None), entries


def _clean_aupadeshika(aupadeshika: str) -> str:
    """Bare root from a dhātupāṭha aupadeshika (SLP1): strip accent marks,
    leading it-syllables (qu/Yi/wu), and everything from the first nasalized
    it-vowel (X~) on. Heuristic — misses rare nasal-internal roots (e.g. nand),
    which is fine: this is only the fallback when the kosha lacks the surface."""
    s = aupadeshika.replace("\\", "").replace("/", "").replace("^", "")
    for pre in ("qu", "Yi", "wu"):
        if s.startswith(pre):
            s = s[len(pre):]
            break
    m = _IT_VOWEL_RE.search(s)
    return s[: m.start()] if m else s


_IT_VOWEL_RE = re.compile(r"[aAiIuUfFxe]~")


def find_dhatus(
    root_slp1: str, gana: str | None = None, surface_slp1: str | None = None
) -> list[tuple]:
    """Candidate (bare_dhatu, aupadeshika) pairs for a claimed root.

    Primary source: kosha entries for the observed surface form (their dhātu
    is re-built bare so the CLAIM's prefixes/features drive the derivation).
    Fallback: dhātupāṭha scan matching the cleaned aupadeshika."""
    want_gana = _enum(pk.Gana, gana) if gana is not None else None
    out: list[tuple] = []
    seen: set[tuple] = set()

    def add(aupadeshika: str, g) -> None:
        if want_gana is not None and g != want_gana:
            return
        key = (aupadeshika, str(g))
        if key not in seen:
            seen.add(key)
            out.append((pk.Dhatu.mula(aupadeshika, g), aupadeshika))

    if surface_slp1:
        for key in kosha_key_candidates(surface_slp1):
            for e in kosha().get(key):
                if _is_tinanta(e):
                    de = e.dhatu_entry
                    prefixes = list(de.dhatu.prefixes or [])
                    bare = de.clean_text[len("".join(prefixes)):] if prefixes else de.clean_text
                    if bare == root_slp1:
                        add(de.dhatu.aupadeshika, de.dhatu.gana)
    for e in dhatu_entries():
        if _clean_aupadeshika(e.dhatu.aupadeshika) == root_slp1:
            add(e.dhatu.aupadeshika, e.dhatu.gana)
    return out


def _trace(prakriya) -> list[str]:
    steps = [
        f"{s.source} {s.code} → {''.join(s.result)}" for s in prakriya.history
    ]
    if len(steps) > MAX_TRACE_STEPS:
        steps = steps[:MAX_TRACE_STEPS] + [f"... ({len(steps) - MAX_TRACE_STEPS} more)"]
    return steps


# ---------------------------------------------------------------- logging

def log_verification(record: dict) -> dict:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record


def _record(
    *,
    run_id: str,
    context: dict,
    surface_iast: str,
    claim: dict,
    method: str,
    result: str,
    expected_forms: list[str],
    prakriya_rules: list[str],
    notes: str,
) -> dict:
    return log_verification(
        {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "run_id": run_id,
            "context": context,  # {"text","line","verse","stage"}
            "surface_iast": surface_iast,
            "surface_slp1": to_slp1(surface_iast),
            "claim": claim,  # {"source","lemma","analysis"}
            "method": method,
            "result": result,
            "expected_forms": expected_forms,
            "prakriya_rules": prakriya_rules,
            "notes": notes,
        }
    )


# ---------------------------------------------------------------- derivation

def derive_subanta(
    stem_slp1: str, linga: str, vibhakti: str, vacana: str
) -> list:
    """All prakriyās for the claimed (stem, liṅga, vibhakti, vacana).

    Feminine ā/ī stems must go through nyāp-anta derivation — basic() does
    NOT fail on them, it silently produces wrong forms (mAyA+Trtiya → mAyA),
    so nyap comes FIRST for those and both result sets are merged."""
    args = dict(
        linga=_enum(pk.Linga, linga),
        vibhakti=_enum(pk.Vibhakti, vibhakti),
        vacana=_enum(pk.Vacana, vacana),
    )

    def _derive(pratipadika):
        try:
            return list(vyakarana().derive(pk.Pada.Subanta(pratipadika=pratipadika, **args)))
        except Exception:
            return []

    makers = [lambda: pk.Pratipadika.basic(stem_slp1)]
    if stem_slp1[-1] in ("A", "I"):
        nyap = lambda: pk.Pratipadika.nyap(stem_slp1)  # noqa: E731
        makers = ([nyap] + makers) if linga == "Stri" else (makers + [nyap])

    prakriyas, seen = [], set()
    for make in makers:
        for p in _derive(make()):
            if p.text not in seen:
                seen.add(p.text)
                prakriyas.append(p)
    return prakriyas


def derive_tinanta(
    dhatu, prayoga: str, lakara: str, purusha: str, vacana: str
) -> list:
    return list(
        vyakarana().derive(
            pk.Pada.Tinanta(
                dhatu=dhatu,
                prayoga=_enum(pk.Prayoga, prayoga),
                lakara=_enum(pk.Lakara, lakara),
                purusha=_enum(pk.Purusha, purusha),
                vacana=_enum(pk.Vacana, vacana),
            )
        )
    )


# ---------------------------------------------------------------- verifiers

def verify_subanta_claim(
    surface_iast: str,
    stem_iast: str,
    linga: str,
    vibhakti: str,
    vacana: str,
    *,
    run_id: str,
    context: dict,
    source: str = "llm",
    notes: str = "",
) -> dict:
    """Prakriya-check a nominal claim: does stem+features derive the surface?"""
    claim = {
        "source": source,
        "lemma": stem_iast,
        "analysis": {
            "pos": "subanta",
            "stem": stem_iast,
            "linga": linga,
            "vibhakti": vibhakti,
            "vacana": vacana,
        },
    }
    surface_slp1 = to_slp1(surface_iast)
    try:
        prakriyas = derive_subanta(to_slp1(stem_iast), linga, vibhakti, vacana)
        derived = [p.text for p in prakriyas]
        matched = forms_match(surface_slp1, derived)
        hit = next((p for p in prakriyas if p.text == matched), None)
        result = "pass" if hit else "fail"
        trace = _trace(hit) if hit else (_trace(prakriyas[0]) if prakriyas else [])
        return _record(
            run_id=run_id,
            context=context,
            surface_iast=surface_iast,
            claim=claim,
            method="prakriya",
            result=result,
            expected_forms=[to_iast(t) for t in derived],
            prakriya_rules=trace,
            notes=notes,
        )
    except Exception as e:
        return _record(
            run_id=run_id,
            context=context,
            surface_iast=surface_iast,
            claim=claim,
            method="prakriya",
            result="tool_error",
            expected_forms=[],
            prakriya_rules=[],
            notes=f"{notes} [{type(e).__name__}: {e}]".strip(),
        )


def verify_tinanta_claim(
    surface_iast: str,
    root_iast: str,
    prefixes: list[str],
    prayoga: str,
    lakara: str,
    purusha: str,
    vacana: str,
    *,
    gana: str | None = None,
    run_id: str,
    context: dict,
    source: str = "llm",
    notes: str = "",
) -> dict:
    """Prakriya-check a verbal claim. The bare root (IAST, no prefixes) is
    looked up in the Dhātupāṭha; every matching dhātu is tried."""
    claim = {
        "source": source,
        "lemma": (("-".join(prefixes) + "-") if prefixes else "") + root_iast,
        "analysis": {
            "pos": "tinanta",
            "root": root_iast,
            "prefixes": prefixes,
            "gana": gana,
            "prayoga": prayoga,
            "lakara": lakara,
            "purusha": purusha,
            "vacana": vacana,
        },
    }
    surface_slp1 = to_slp1(surface_iast)
    try:
        derived: list[str] = []
        hit = None
        tried: list[str] = []

        # Primary: kosha-driven — if the surface is a known tiṅanta, rebuild
        # each entry's dhātu FAITHFULLY (aupadeshika + gaṇa + sanādi + its own
        # prefixes) and re-derive under the CLAIMED features. Root naming is
        # convention-laden (kalpay/kalpi/kḷp are one dhātu), so a name
        # mismatch is noted, not failed — the feature check is the verdict.
        root_note = ""
        for key in kosha_key_candidates(surface_slp1):
            for e in kosha().get(key):
                if not _is_tinanta(e):
                    continue
                de = e.dhatu_entry
                d = pk.Dhatu.mula(de.dhatu.aupadeshika, de.dhatu.gana)
                if de.dhatu.sanadi:
                    d = d.with_sanadi(list(de.dhatu.sanadi))
                if de.dhatu.prefixes:
                    d = d.with_prefixes(list(de.dhatu.prefixes))
                tried.append(
                    de.dhatu.aupadeshika
                    + (f"+{list(de.dhatu.sanadi)}" if de.dhatu.sanadi else "")
                )
                for p in derive_tinanta(d, prayoga, lakara, purusha, vacana):
                    derived.append(p.text)
                    if hit is None and normalize_nasals(p.text) == normalize_nasals(surface_slp1):
                        hit = p
                        claimed_full = "".join(to_slp1(x) for x in prefixes) + to_slp1(root_iast)
                        if claimed_full not in (de.clean_text, e.lemma):
                            root_note = (
                                f"claimed root {claim['lemma']!r}; kosha dhātu is "
                                f"{de.clean_text} ({de.dhatu.aupadeshika})"
                            )
            if hit is not None:
                break

        # Fallback: dhātupāṭha scan by cleaned aupadeshika, claim's prefixes.
        if hit is None:
            for dhatu, aupadeshika in find_dhatus(to_slp1(root_iast), gana):
                if prefixes:
                    dhatu = dhatu.with_prefixes([to_slp1(p) for p in prefixes])
                tried.append(aupadeshika)
                for p in derive_tinanta(dhatu, prayoga, lakara, purusha, vacana):
                    derived.append(p.text)
                    if hit is None and normalize_nasals(p.text) == normalize_nasals(surface_slp1):
                        hit = p

        if not tried:
            return _record(
                run_id=run_id, context=context, surface_iast=surface_iast,
                claim=claim, method="prakriya", result="fail",
                expected_forms=[], prakriya_rules=[],
                notes=f"{notes} [surface not in kosha and no dhātupāṭha entry "
                f"for root {root_iast!r}{f' in gana {gana}' if gana else ''}]".strip(),
            )
        result = "pass" if hit else "fail"
        return _record(
            run_id=run_id,
            context=context,
            surface_iast=surface_iast,
            claim=claim,
            method="prakriya",
            result=result,
            expected_forms=sorted({to_iast(t) for t in derived}),
            prakriya_rules=_trace(hit) if hit else [],
            notes=f"{notes} [dhātus tried: {', '.join(tried[:6])}]"
            + (f" [{root_note}]" if root_note else ""),
        )
    except Exception as e:
        return _record(
            run_id=run_id,
            context=context,
            surface_iast=surface_iast,
            claim=claim,
            method="prakriya",
            result="tool_error",
            expected_forms=[],
            prakriya_rules=[],
            notes=f"{notes} [{type(e).__name__}: {e}]".strip(),
        )


def verify_compound_claim(
    surface_iast: str,
    stem_iast: str,
    linga: str,
    vibhakti: str,
    vacana: str,
    samasa_type: str,
    vigraha: str,
    members: list[str],
    *,
    run_id: str,
    context: dict,
    source: str = "llm",
) -> dict:
    """Canonical compound policy (vidyut samāsa coverage is partial):
    1. the whole inflected compound is checked as an opaque stem (prakriya);
    2. the samāsa RELATION is logged `unsupported` with the claim recorded;
    3. each member is kosha-checked (known-form).
    Returns {"stem": rec, "relation": rec, "members": [recs], "status": ...}
    where status rolls up to the stem check's result."""
    stem_rec = verify_subanta_claim(
        surface_iast, stem_iast, linga, vibhakti, vacana,
        run_id=run_id, context=context, source=source,
        notes=f"{samasa_type} checked as opaque stem",
    )
    relation_rec = mark_unsupported(
        surface_iast,
        f"samāsa relation ({samasa_type}: {vigraha}) not expressible in vidyut; "
        f"members {', '.join(members)} checked separately",
        run_id=run_id, context=context, source=source,
    )
    member_recs = []
    for m in members:
        key, entries = kosha_lookup(m)
        member_recs.append(
            _record(
                run_id=run_id, context=context, surface_iast=m,
                claim={"source": source, "lemma": m, "analysis": None},
                method="kosha",
                result="pass" if entries else "unsupported",
                expected_forms=[], prakriya_rules=[],
                notes=f"compound member of {surface_iast}"
                + ("" if entries else " [not in kosha as bare form]"),
            )
        )
    return {
        "stem": stem_rec,
        "relation": relation_rec,
        "members": member_recs,
        "status": stem_rec["result"],
    }


def kosha_check(
    surface_iast: str,
    *,
    run_id: str,
    context: dict,
    claim: dict | None = None,
    source: str = "llm",
    notes: str = "",
) -> dict:
    """Lexicon check: is the surface form known, and (if a claim is given) is
    any stored analysis consistent with it? Secondary to the prakriya check —
    kosha lemmas for kṛdantas are the dhātu, not the nominal stem."""
    full_claim = claim or {"source": source, "lemma": None, "analysis": None}
    try:
        key, entries = kosha_lookup(surface_iast)
        if not entries:
            return _record(
                run_id=run_id,
                context=context,
                surface_iast=surface_iast,
                claim=full_claim,
                method="kosha",
                result="fail",
                expected_forms=[],
                prakriya_rules=[],
                notes=f"{notes} [form not in kosha]".strip(),
            )
        analyses = [_describe_entry(e) for e in entries]
        result = "pass"
        extra = f"key={key}; {len(entries)} entries: " + "; ".join(analyses[:6])
        if full_claim.get("analysis"):
            ok = any(_entry_matches(e, full_claim["analysis"]) for e in entries)
            result = "pass" if ok else "fail"
            if not ok:
                extra = "no entry consistent with claim. " + extra
        return _record(
            run_id=run_id,
            context=context,
            surface_iast=surface_iast,
            claim=full_claim,
            method="kosha",
            result=result,
            expected_forms=[],
            prakriya_rules=[],
            notes=f"{notes} [{extra}]".strip(),
        )
    except Exception as e:
        return _record(
            run_id=run_id,
            context=context,
            surface_iast=surface_iast,
            claim=full_claim,
            method="kosha",
            result="tool_error",
            expected_forms=[],
            prakriya_rules=[],
            notes=f"{notes} [{type(e).__name__}: {e}]".strip(),
        )


def mark_unsupported(
    surface_iast: str,
    reason: str,
    *,
    run_id: str,
    context: dict,
    claim: dict | None = None,
    source: str = "llm",
) -> dict:
    """Log a claim vidyut cannot express (e.g. a samāsa relation)."""
    return _record(
        run_id=run_id,
        context=context,
        surface_iast=surface_iast,
        claim=claim or {"source": source, "lemma": None, "analysis": None},
        method="none",
        result="unsupported",
        expected_forms=[],
        prakriya_rules=[],
        notes=reason,
    )


# ------------------------------------------------- kosha-entry introspection

def _is_subanta(e) -> bool:
    return hasattr(e, "vibhakti")


def _is_tinanta(e) -> bool:
    return hasattr(e, "lakara")


def _describe_entry(e) -> str:
    if _is_subanta(e):
        return f"subanta({e.lemma}: {e.linga}/{e.vibhakti}/{e.vacana})"
    if _is_tinanta(e):
        return f"tinanta({e.lemma}: {e.prayoga}/{e.lakara}/{e.purusha}/{e.vacana})"
    return f"avyaya({e.lemma})" if e.is_avyaya else repr(e)[:60]


def _same(a, b) -> bool:
    return a == b or str(a) == str(b)


def _entry_matches(e, analysis: dict) -> bool:
    pos = analysis.get("pos")
    if pos == "subanta" and _is_subanta(e):
        want = (
            _enum(pk.Linga, analysis["linga"]),
            _enum(pk.Vibhakti, analysis["vibhakti"]),
            _enum(pk.Vacana, analysis["vacana"]),
        )
        if not all(_same(g, w) for g, w in zip((e.linga, e.vibhakti, e.vacana), want)):
            return False
        stem_slp1 = to_slp1(analysis["stem"])
        pe = e.pratipadika_entry
        lemmas = {e.lemma, getattr(pe, "lemma", None)}
        basic = getattr(pe, "pratipadika", None)
        if basic is not None:
            lemmas.add(basic.text)
        # Kṛdanta kosha lemma is the dhātu; feature agreement suffices there
        # (stem identity is the prakriya check's job).
        return stem_slp1 in lemmas or getattr(pe, "dhatu_entry", None) is not None
    if pos == "tinanta" and _is_tinanta(e):
        want = (
            _enum(pk.Prayoga, analysis["prayoga"]),
            _enum(pk.Lakara, analysis["lakara"]),
            _enum(pk.Purusha, analysis["purusha"]),
            _enum(pk.Vacana, analysis["vacana"]),
        )
        got = (e.prayoga, e.lakara, e.purusha, e.vacana)
        if not all(_same(g, w) for g, w in zip(got, want)):
            return False
        root_slp1 = to_slp1(analysis["root"])
        de = e.dhatu_entry
        clean = de.clean_text
        prefixes = list(de.dhatu.prefixes or [])
        bare = clean[len("".join(prefixes)):] if prefixes else clean
        return root_slp1 in (clean, bare) or root_slp1 == e.lemma
    return False
