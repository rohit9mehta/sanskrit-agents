"""Lemma normalization: ByT5 citation conventions → the verifier's.

Why: across 171 translated units, 15% of ByT5 lemmas differed from the
reasoner's chosen lemma, and an audit (data/training/lemma_patterns.md)
showed almost all of it is CONVENTION, not error:
  * verbs cited with fused prefixes (pravṛt) where our schema wants bare
    root + prefix list (vṛt, [pra]); likewise absolutives/infinitives
  * ṇic/san citation forms (janay, jijīviṣ) for jan, jīv
  * participles lemmatized to the root (sthā for sthitam) — vidyut's kosha
    does the same (PratipadikaEntry.Krdanta) — where the reasoner cites the
    derived stem (sthita) when the kosha also has it as a Basic stem
  * pronoun/indeclinable citation (ka→kim, yat→yad, tena→tad)
  * feminine stems cited in masculine (śāśvata for śāśvatībhyaḥ)
Every one of these cost a reasoner override (and tokens) for no information.

Canonical convention (applied to ByT5 output BEFORE the reasoner sees it):
  tinanta / absolutive / infinitive → bare root (no prefixes, no ṇic/san),
      prefixes listed separately
  subanta → a Basic stem from vidyut's kosha that matches the surface and the
      tagged features (sthita, tad, kim, śāśvatī) when one exists; else the
      kosha's root citation is kept and flagged as kṛdanta
  compound members / avyayas → unchanged
  nasal orthography → untouched (verifier is spelling-insensitive)

The kosha is the authority because it is what verify.py derives against —
so a canonical lemma is by construction a lemma the verifier can check.
"""

import re
from dataclasses import dataclass, field

from . import verify
from functools import lru_cache

from .verify import dhatu_entries, find_dhatus, kosha_lookup, to_iast, to_slp1, vyakarana

# ByT5 (DCS-style) morph tags — see scripts/30_score_analyzer.py
_NOM_RE = re.compile(r"^(Du|S|P)([NAIDBGLV])([A-Za-z]*)$")
_VERB_RE = re.compile(r"^(Du|S|P)(Pr|Ps|Fu)?([123])(Im)?(In|O|Im)")
_CASE = {"N": "praTamA", "A": "dvitIyA", "I": "tftIyA", "D": "caturTI",
         "B": "paYcamI", "G": "zazWI", "L": "saptamI", "V": "samboDanam"}
_NUM = {"S": "eka", "Du": "dvi", "P": "bahu"}
_GEN = {"M": "puM", "F": "strI", "Ne": "napuMsaka"}

# Upasargas in SLP1, longest first; canonical IAST citation per variant.
_UPASARGAS = [
    ("prati", "prati"), ("pari", "pari"), ("parA", "parā"), ("abhi", "abhi"),
    ("anu", "anu"), ("ava", "ava"), ("adhi", "adhi"), ("ati", "ati"),
    ("api", "api"), ("apa", "apa"), ("upa", "upa"), ("nis", "nis"),
    ("nir", "nis"), ("niz", "nis"), ("dus", "dus"), ("dur", "dus"),
    ("duz", "dus"), ("sam", "sam"), ("saM", "sam"), ("saY", "sam"),
    ("saR", "sam"), ("san", "sam"), ("pra", "pra"), ("vi", "vi"),
    ("ni", "ni"), ("ud", "ud"), ("ut", "ud"), ("su", "su"), ("A", "ā"),
]
# boundary-sandhi variants: (variant, canonical, required initial of the rest)
_UPASARGA_SANDHI = [
    ("prat", "prati", "I"), ("par", "pari", "I"), ("aB", "abhi", "I"),
    ("aD", "adhi", "I"), ("praty", "prati", "aAiuUeoEOf"), ("pary", "pari", "aAiuUeoEOf"),
    ("aBy", "abhi", "aAiuUeoEOf"), ("aDy", "adhi", "aAiuUeoEOf"),
    ("anv", "anu", "aAiIeoEOf"), ("apy", "api", "aAiuUeoEOf"), ("aty", "ati", "aAiuUeoEOf"),
    ("vy", "vi", "aAiuUeoEOf"), ("ny", "ni", "aAiuUeoEOf"),
    ("up", "upa", "AeoEO"), ("pr", "pra", "AeoEO"), ("av", "ava", "AeoEO"),
    ("ap", "apa", "AeoEO"), ("par", "parā", "AeoEO"), ("sam", "sam", "AeoEO"),
]
_PRONOUN_CITATION = {"ka": "kim", "kA": "kim", "yat": "yad", "tat": "tad",
                     "etat": "etad", "ena": "enad", "tena": "tad"}
# tvad/mad (traditional) and yuṣmad/asmad (vidyut) are both verifier-valid;
# the reasoner cites tvad/mad, so we leave those alone.
_PRONOUNS = {"tad", "etad", "idam", "kim", "yad", "asmad", "yuzmad", "adas",
             "enad", "sarva", "anya", "sva", "bhavat"}

# kosha stores prefixes by technical name (AN for ā, sam for saṃ/san…);
# clean_text carries their surface form — strip by variant, not by length.
_PREFIX_SURFACE = {"AN": ["A"], "sam": ["sam", "saM", "saY", "saR", "san", "sa"],
                   "nis": ["nis", "nir", "niz", "niH"], "dus": ["dus", "dur", "duz", "duH"],
                   "ud": ["ud", "ut", "un", "uj", "ul"], "prati": ["prati", "praty"],
                   "abhi": ["abhi", "aBi", "aBy"], "adhi": ["adhi", "aDi", "aDy"],
                   "anu": ["anu", "anv"], "api": ["api", "apy"], "ati": ["ati", "aty"],
                   "vi": ["vi", "vy"], "ni": ["ni", "ny"], "pari": ["pari", "pary"]}
_PREFIX_CITE = {"AN": "ā", "sam": "sam", "nis": "nis", "dus": "dus", "ud": "ud"}


def _strip_prefixes(clean_text: str, prefixes: list[str]) -> tuple[str, list[str]]:
    cur = clean_text
    for p in prefixes:
        for v in _PREFIX_SURFACE.get(p, []) + [p]:
            if cur.startswith(v):
                cur = cur[len(v):]
                break
    cites = [_PREFIX_CITE.get(p) or next((c for u, c in _UPASARGAS if u == p), to_iast(p))
             for p in prefixes]
    return cur, cites


@dataclass
class Canonical:
    surface: str
    byt5_lemma: str
    lemma: str                      # canonical citation (IAST)
    kind: str                       # tinanta|krdanta|subanta|compound-member|avyaya|unknown
    root: str | None = None         # bare root for verbs/kṛdantas
    prefixes: list[str] = field(default_factory=list)
    sanadi: str | None = None       # "ṇic" | "san" | None
    note: str = ""

    @property
    def changed(self) -> bool:
        if self.kind in ("tinanta", "krdanta"):
            return self.lemma != self.byt5_lemma or bool(self.prefixes) or bool(self.sanadi)
        return self.lemma != self.byt5_lemma

    def as_hint(self) -> str:
        """One line for the reasoner prompt."""
        s = f"{self.surface}: lemma {self.lemma}"
        if self.prefixes:
            s += f" (root {self.root}, prefixes {self.prefixes})"
        if self.sanadi:
            s += f" [{self.sanadi}]"
        if self.note:
            s += f" — {self.note}"
        return s


@lru_cache(maxsize=1)
def _roots() -> frozenset:
    """Bare roots (SLP1) as vidyut cites them — clean_text, which handles
    it-markers the aupadeshika heuristic in verify.find_dhatus misses."""
    out = set()
    for e in dhatu_entries():
        ct = getattr(e, "clean_text", None)
        out.add(_root_from_aupadeshika(e.dhatu.aupadeshika))
        if ct:
            out.add(ct)
    return frozenset(out)


_VOWELS = "aAiIuUfFxXeEoO"


def _root_from_aupadeshika(aup: str) -> str:
    """quDAY → DA, kfY → kf, o~hAk → hA, SriY → Sri, zWA\\ → sTA, gamx~ → gam.
    Leading it-syllables and the accent marks go; if the entry has a nasal
    it-vowel (X~) everything from it on goes; otherwise a final consonant
    after a vowel is an it-letter (P. 1.3.3) and goes."""
    s = aup.replace("\\", "").replace("/", "").replace("^", "")
    for pre in ("o~", "qu", "Yi", "wu"):
        if s.startswith(pre):
            s = s[len(pre):]
            break
    m = re.search(r"[aAiIuUfFxXeEoO]~", s)
    if m:
        s = s[: m.start()]
    elif len(s) > 2 and s[-1] not in _VOWELS and s[-2] in _VOWELS and s[-1] in "YNkKwqzr":
        s = s[:-1]
    return _cite_root(s)


def _cite_root(slp1: str) -> str:
    """Dhātupāṭha initial ṣ/ṇ → citation s/n (ṣṭhā→sthā, ṇī→nī; P. 6.1.64)."""
    if slp1.startswith("z"):
        r = "s" + slp1[1:]
        if len(r) > 1 and r[1] in "wWqQ":
            r = r[0] + {"w": "t", "W": "T", "q": "d", "Q": "D"}[r[1]] + r[2:]
        return r
    if slp1.startswith("R"):
        return "n" + slp1[1:]
    return slp1


def _uncite_root(slp1: str) -> str:
    """Inverse of _cite_root: sthā → ṣṭhā for dhātupāṭha lookup."""
    if slp1.startswith("s"):
        r = "z" + slp1[1:]
        if len(r) > 1 and r[1] in "tTdD":
            r = r[0] + {"t": "w", "T": "W", "d": "q", "D": "Q"}[r[1]] + r[2:]
        return r
    if slp1.startswith("n"):
        return "R" + slp1[1:]
    return slp1


def _dhatus_for(root_slp1: str) -> list:
    return find_dhatus(root_slp1) or find_dhatus(_uncite_root(root_slp1))


def _is_root(slp1: str) -> bool:
    return slp1 in _roots() or bool(_dhatus_for(slp1))


def _split_prefixes(root_slp1: str) -> tuple[str, list[str]]:
    """Greedy upasarga stripping, validated against the dhātupāṭha: only
    strip when what remains is (eventually) a known root."""
    prefixes: list[str] = []
    cur = root_slp1
    for _ in range(3):
        hit = None
        cands = [(u, c, None) for u, c in _UPASARGAS] + \
                [(u, c, need) for u, c, need in _UPASARGA_SANDHI]
        for up, cite, need in cands:
            rest = cur[len(up):]
            if not (cur.startswith(up) and len(rest) >= 1):
                continue
            if need is not None and rest[0] not in need:
                continue
            if (_is_root(rest) or (rest.endswith("ay") and _is_root(rest[:-2]))
                    or any(rest.startswith(u) for u, _ in _UPASARGAS)):
                hit = (up, cite, rest)
                break
        if hit is None:
            break
        prefixes.append(hit[1])
        cur = hit[2]
    if prefixes and not (_is_root(cur) or (cur.endswith("ay") and _is_root(cur[:-2]))):
        return root_slp1, []            # never reached a real root: don't split
    return _cite_root(cur), prefixes


def _strip_sanadi(root_slp1: str) -> tuple[str, str | None]:
    if root_slp1.endswith("ay") and _is_root(root_slp1[:-2]):
        return root_slp1[:-2], "ṇic"
    if root_slp1.endswith("iz") and len(root_slp1) > 4:
        # desiderative citation (jijIviz → jIv): reduplicated; strip and test
        core = root_slp1[:-2]
        for n in (2, 3):
            cand = core[n:]
            if _is_root(cand):
                return cand, "san"
    return root_slp1, None


def _verbal(surface: str, lemma: str, tag: str) -> Canonical:
    lemma_slp1 = to_slp1(lemma)
    _, entries = kosha_lookup(surface)
    for e in entries:
        if verify._is_tinanta(e):
            de = e.dhatu_entry
            pre = list(de.dhatu.prefixes or [])
            bare, cites = _strip_prefixes(de.clean_text, pre)
            if verify.normalize_nasals(de.clean_text) == verify.normalize_nasals(lemma_slp1) or not pre:
                aup = _root_from_aupadeshika(de.dhatu.aupadeshika)
                if not de.dhatu.sanadi and (not _is_root(bare) or bare != aup) and _is_root(aup):
                    bare = aup                      # utTA → sTA
                if str(de.dhatu.gana).endswith("Curadi") and bare.endswith("a") and len(bare) > 2:
                    bare = bare[:-1]                # curādi kaTa → kaT
                # suppletion: kosha files uvāca under brū; cite the root ByT5 gave
                # when it is itself a dhātu and no prefix is involved
                own, own_pre = _split_prefixes(lemma_slp1)
                if not pre and not own_pre and _is_root(own) and own != bare and not de.dhatu.sanadi:
                    return Canonical(surface, lemma, to_iast(own), "tinanta", root=to_iast(own),
                                     note=f"kosha files this under {to_iast(bare)} (suppletive)")
                if de.dhatu.sanadi:
                    base = _root_from_aupadeshika(de.dhatu.aupadeshika)
                    root = base if _is_root(base) else bare
                    san = {"Ric": "ṇic", "san": "san", "yaN": "yaṅ"}.get(
                        str(de.dhatu.sanadi[0]).split(".")[-1], str(de.dhatu.sanadi[0]))
                else:
                    root, san = _strip_sanadi(bare)
                return Canonical(surface, lemma, to_iast(root), "tinanta",
                                 root=to_iast(root), prefixes=cites, sanadi=san,
                                 note="kosha dhātu" if cites or san else "")
    root, pre = _split_prefixes(lemma_slp1)
    root, san = _strip_sanadi(root)
    return Canonical(surface, lemma, to_iast(root), "tinanta",
                     root=to_iast(root), prefixes=pre, sanadi=san,
                     note="prefixes split by dhātupāṭha" if pre else "")


def _kosha_krdanta_dhatu(surface: str, root_slp1: str | None = None):
    """(bare_root_slp1, prefixes_iast, sanadi) from the first kosha entry
    whose prātipadika is a Krdanta — authoritative prefix/root split.
    With root_slp1, only entries of that root qualify."""
    _, entries = kosha_lookup(surface)
    for e in entries:
        pe = getattr(e, "pratipadika_entry", None)
        if pe is None or not str(pe).startswith("PratipadikaEntry.Krdanta"):
            continue
        if root_slp1 and _entry_root(e) not in (root_slp1, _cite_root(root_slp1)):
            continue
        de = pe.dhatu_entry
        pre = list(de.dhatu.prefixes or [])
        bare, cites = _strip_prefixes(de.clean_text, pre)
        aup = _root_from_aupadeshika(de.dhatu.aupadeshika)
        if not de.dhatu.sanadi and (not _is_root(bare) or bare != aup) and _is_root(aup):
            bare = aup
        san = None
        if de.dhatu.sanadi:
            base = _root_from_aupadeshika(de.dhatu.aupadeshika)
            bare = base if _is_root(base) else bare
            san = {"Ric": "ṇic", "san": "san", "yaN": "yaṅ"}.get(
                str(de.dhatu.sanadi[0]).split(".")[-1], str(de.dhatu.sanadi[0]))
        return bare, cites, san
    return None


def _krdanta_avyaya(surface: str, lemma: str, tag: str) -> Canonical:
    k = _kosha_krdanta_dhatu(surface)
    if k:
        root, pre, san = k
    else:
        root, pre = _split_prefixes(to_slp1(lemma))
        root, san = _strip_sanadi(root)
    kind = "absolutive" if tag == "Co" else "infinitive"
    return Canonical(surface, lemma, to_iast(root), "krdanta",
                     root=to_iast(root), prefixes=pre, sanadi=san, note=kind)


def _entry_root(e) -> str | None:
    try:
        de = e.pratipadika_entry.dhatu_entry
        pre = list(de.dhatu.prefixes or [])
        bare, _ = _strip_prefixes(de.clean_text, pre)
        aup = _root_from_aupadeshika(de.dhatu.aupadeshika)
        return aup if _is_root(aup) else _cite_root(bare)
    except Exception:
        return None


def _derive_krdanta_stem(surface: str, want: tuple, root_slp1: str | None = None
                         ) -> tuple[str | None, str | None]:
    """Run the kosha's own Krdanta prātipadika through the engine → stem text
    (sthita, ukta, viniyata). Prefers the entry matching the tagged features.
    If root_slp1 is given, only entries of THAT root qualify (the kosha files
    dhāvataḥ under sṛ as well — we must not cite sarat for dhāv)."""
    _, entries = kosha_lookup(surface)
    if root_slp1:
        entries = [e for e in entries if _entry_root(e) in (root_slp1, _cite_root(root_slp1))]
    pref = ["kta", "ktavatu", "Satf", "SAnac", "kvasu", "kAnac", "tavya", "tavyat",
            "anIyar", "yat", "Ryat", "kyap", "lyuw", "Rvul", "tfc", "GaY", "ac", "ka"]

    def _rank(e):
        krt = str(e.pratipadika_entry.krt)
        return ((str(e.vibhakti), str(e.vacana)) != want,
                pref.index(krt) if krt in pref else len(pref))
    ranked = sorted((e for e in entries if verify._is_subanta(e)
                     and str(e.pratipadika_entry).startswith("PratipadikaEntry.Krdanta")),
                    key=_rank)
    for e in ranked:
        try:
            prs = list(vyakarana().derive(e.pratipadika_entry.to_prakriya_args()))
        except Exception:
            continue
        if prs:
            return prs[0].text, str(e.pratipadika_entry.krt)
    return None, None


_KRT_BY_TAG = [("Pa", ["kta", "ktavatu"]), ("Pr", ["Satf", "SAnac"]),
               ("Ps", ["kvasu", "kAnac"]), ("Gd", ["tavya", "anIyar", "yat", "Ryat", "kyap"])]


def _derive_krdanta_by_tag(surface, root_slp1, prefixes_iast, sanadi, extra, want):
    """No kosha entry: build the kṛdanta from root + a krt implied by the tag
    (Pa→kta, Pr→śatṛ/śānac, Gd→tavya…), then confirm by declining the
    derived stem with the tagged features back to the surface."""
    from vidyut import prakriya as pk
    from .verify import forms_match
    if not root_slp1:
        return None, None
    krts = [k for key, ks in _KRT_BY_TAG if key in extra for k in ks]
    if not krts:
        return None, None
    dhatus = _dhatus_for(root_slp1)
    if not dhatus:
        return None, None
    surf_slp1 = to_slp1(surface)
    vib_name = {v: k for k, v in _CASE.items()}.get(want[0])
    for d, _ in dhatus[:3]:
        if sanadi == "ṇic":
            d = d.with_sanadi([pk.Sanadi.Ric])
        if prefixes_iast:
            d = d.with_prefixes([to_slp1(x) for x in prefixes_iast])
        for krt in krts:
            try:
                prs = list(vyakarana().derive(pk.Pratipadika.krdanta(d, getattr(pk.Krt, krt))))
            except Exception:
                continue
            prati = pk.Pratipadika.krdanta(d, getattr(pk.Krt, krt))
            vib = {"praTamA": "Prathama", "dvitIyA": "Dvitiya", "tftIyA": "Trtiya",
                   "caturTI": "Caturthi", "paYcamI": "Panchami", "zazWI": "Sasthi",
                   "saptamI": "Saptami", "samboDanam": "Sambodhana"}[want[0]]
            vac = {"eka": "Eka", "dvi": "Dvi", "bahu": "Bahu"}[want[1]]
            for linga in ("Pum", "Stri", "Napumsaka"):
                try:
                    forms = [x.text for x in vyakarana().derive(pk.Pada.Subanta(
                        pratipadika=prati, linga=getattr(pk.Linga, linga),
                        vibhakti=getattr(pk.Vibhakti, vib), vacana=getattr(pk.Vacana, vac)))]
                except Exception:
                    forms = []
                if forms_match(surf_slp1, forms):
                    return prs[0].text, krt
    return None, None


def _split_nominal_rest(rest: str) -> tuple[str, str | None]:
    """'PaPrM' → ('PaPr', 'M'); 'NeGd' → ('Gd', 'Ne'); '' → ('', None)."""
    for g in ("Ne", "F", "M"):
        if g in rest:
            return rest.replace(g, "", 1), g
    return rest, None


def _nominal(surface: str, lemma: str, tag: str, m) -> Canonical:
    num, case, rest = m.groups()
    _extra, gen = _split_nominal_rest(rest)
    lemma_slp1 = to_slp1(lemma)
    if lemma_slp1 in _PRONOUN_CITATION:
        return Canonical(surface, lemma, to_iast(_PRONOUN_CITATION[lemma_slp1]),
                         "subanta", note="pronoun citation")
    _, entries = kosha_lookup(surface)
    want = (_CASE[case], _NUM[num])
    basic, krd = {}, set()
    for e in entries:
        if not verify._is_subanta(e):
            continue
        feats = (str(e.vibhakti), str(e.vacana))
        if feats != want:
            continue
        is_basic = str(e.pratipadika_entry).startswith("PratipadikaEntry.Basic")
        if is_basic:
            basic.setdefault(e.lemma, gen is not None and str(e.linga) == _GEN[gen])
        else:
            krd.add(e.lemma)
    participle_tag = any(x in _extra for x in ("Pa", "Pr", "Gd", "Ps"))
    if lemma_slp1 in basic:
        return Canonical(surface, lemma, lemma, "subanta")
    if lemma_slp1 in krd:
        # ByT5 cited the root of a kṛdanta (kosha convention): the kosha's own
        # Krdanta prātipadika derives the stem (sthita, kṛta, arhat, ākhya)
        own_root, own_pre = _split_prefixes(lemma_slp1)
        own_root, _ = _strip_sanadi(own_root)
        stem, krt = _derive_krdanta_stem(surface, want, own_root)
        if stem:
            k = _kosha_krdanta_dhatu(surface, own_root)
            root, pre, san = k if k else (own_root, own_pre, None)
            return Canonical(surface, lemma, to_iast(stem), "subanta",
                             root=to_iast(root) if root else None, prefixes=pre, sanadi=san,
                             note=f"kṛdanta stem derived by vidyut (krt {krt})")
    if basic:
        # prefer gender match, then pronouns, then the shortest stem
        ranked = sorted(basic, key=lambda l: (not basic[l], l not in _PRONOUNS, len(l)))
        fem_of_lemma = [l for l in basic if l in (lemma_slp1 + "A", lemma_slp1[:-1] + "I")
                        and gen == "F"]
        # replace ByT5's lemma ONLY when it is a root-citation of a participle,
        # a failed lemmatization (lemma == surface), or the masculine of an
        # attested feminine stem — never merely because the kosha has others
        # participle tags: prefer participle-shaped stems (-ta/-na/-at/-āna/-tavya…)
        if participle_tag:
            shaped = [l for l in ranked if l.endswith(("ta", "na", "at", "Ana", "tavya",
                                                       "anIya", "ya", "vas", "tavat"))]
            if shaped:
                ranked = shaped + [l for l in ranked if l not in shaped]
        if (lemma_slp1 in krd or lemma_slp1 == to_slp1(surface) or fem_of_lemma
                or (participle_tag and _is_root(lemma_slp1))):
            pick = fem_of_lemma[0] if fem_of_lemma else ranked[0]
            note = ("kṛdanta stem (kosha Basic)" if lemma_slp1 in krd
                    else "feminine stem (kosha Basic)" if fem_of_lemma else "kosha Basic stem")
            if len(ranked) > 1 and not fem_of_lemma:
                note += f"; alternatives {[to_iast(x) for x in ranked[1:3]]}"
            return Canonical(surface, lemma, to_iast(pick), "subanta", note=note)
    if lemma_slp1 in krd or (krd and not basic) or (participle_tag and not basic):
        own_root, _ = _split_prefixes(lemma_slp1)
        own_root, _ = _strip_sanadi(own_root)
        k = _kosha_krdanta_dhatu(surface, own_root if _is_root(own_root) else None)
        if k:
            root, pre, san = k
        else:
            root, pre = _split_prefixes(lemma_slp1)
            root, san = _strip_sanadi(root)
        stem, krt = _derive_krdanta_stem(surface, want, root)
        if not stem:
            stem, krt = _derive_krdanta_by_tag(surface, root, pre, san, _extra, want)
        if stem:
            return Canonical(surface, lemma, to_iast(stem), "subanta", root=to_iast(root),
                             prefixes=pre, sanadi=san,
                             note=f"kṛdanta stem derived by vidyut (krt {krt}) from root {to_iast(root)}")
        return Canonical(surface, lemma, lemma, "krdanta", root=to_iast(root),
                         prefixes=pre, sanadi=san,
                         note="participle/kṛdanta cited by root (stem not derivable)")
    return Canonical(surface, lemma, lemma, "subanta")


def canonicalize(surface: str, lemma: str, tag: str) -> Canonical:
    tag = tag or ""
    if tag == "Cp":
        return Canonical(surface, lemma, lemma, "compound-member")
    if tag in ("Co", "In"):
        return _krdanta_avyaya(surface, lemma, tag)
    if _VERB_RE.match(tag):
        return _verbal(surface, lemma, tag)
    m = _NOM_RE.match(tag)
    if m:
        try:
            return _nominal(surface, lemma, tag, m)
        except Exception:
            return Canonical(surface, lemma, lemma, "subanta", note="kosha lookup failed")
    if not tag:
        lemma_slp1 = to_slp1(lemma)
        if lemma_slp1 in _PRONOUN_CITATION:
            return Canonical(surface, lemma, to_iast(_PRONOUN_CITATION[lemma_slp1]),
                             "avyaya", note="citation")
        return Canonical(surface, lemma, lemma, "avyaya")
    return Canonical(surface, lemma, lemma, "unknown")


def canonical_hints(parsed_tokens: list[dict]) -> list[str]:
    """For a parse_slm() token list: one hint line per token whose canonical
    citation differs from ByT5's (what the reasoner should cite)."""
    out = []
    for t in parsed_tokens:
        if "surface" not in t:
            continue
        c = canonicalize(t["surface"], t.get("lemma", ""), t.get("tag", ""))
        if c.changed:
            out.append(c.as_hint())
    return out
