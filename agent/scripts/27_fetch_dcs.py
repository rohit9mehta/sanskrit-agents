"""Fetch a genre-stratified sample of the DCS (Digital Corpus of Sanskrit)
and convert it to our claim schema (Phase 3 prep).

DCS: github.com/OliverHellwig/sanskrit, dcs/data/conllu — CC BY 4.0,
manually validated morphology, 270 texts. We sample texts chosen to fill
the gaps in agent/data/training/coverage.md (narrative/kāvya genres carry
the past tenses and moods that śāstric commentary prose lacks).

Outputs:
  agent/data/dcs/raw/<text>/<chapter>.conllu   — cached downloads
  agent/data/dcs/README.md                     — license + citation
  agent/data/training/dcs_pool.jsonl           — converted records
  agent/data/training/dcs_summary.md           — what we got, by genre/feature

Feature mapping notes (see conllu/readme.md upstream):
  * DCS FEATS are UD-coarse. Tense=Past does not distinguish Luṅ/Liṭ/Laṅ,
    and Tense=Fut does not distinguish Lṛṭ/Luṭ — we emit `lakara_candidates`
    and let vidyut arbitrate at benchmark-build time (derive each candidate,
    keep whichever generates the attested form).
  * Case=Cpd marks compound members → kind=compound_member (samāsa data).
  * VerbForm=Part/Conv/Gdv/Inf are kṛdantas → kind=krdanta (outside the
    current Morph schema; retained raw for future use).
  * Mood=Jus (Vedic injunctive) and other Vedic-only categories are skipped:
    vidyut derives classical Pāṇinian forms.
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
RAW = AGENT / "data" / "dcs" / "raw"
TRAIN = AGENT / "data" / "training"
API = "https://api.github.com/repos/OliverHellwig/sanskrit/contents/dcs/data/conllu/files"
RAW_BASE = "https://raw.githubusercontent.com/OliverHellwig/sanskrit/master/dcs/data/conllu/files"

# (text dir name, genre tag, max chapters to sample)
TARGETS = [
    ("Daśakumāracarita", "prose-kavya", 6),
    ("Kathāsaritsāgara", "narrative-verse", 6),
    ("Hitopadeśa", "narrative-prose", 6),
    ("Rāmāyaṇa", "epic", 6),
    ("Meghadūta", "lyric-kavya", 2),
    ("Kirātārjunīya", "mahakavya", 4),
    ("Buddhacarita", "buddhist-kavya", 4),
    ("Arthaśāstra", "shastra-prose", 4),
    ("Viṣṇupurāṇa", "purana", 4),
]

CASE_MAP = {"Nom": "Prathama", "Acc": "Dvitiya", "Ins": "Trtiya",
            "Dat": "Caturthi", "Abl": "Panchami", "Gen": "Sasthi",
            "Loc": "Saptami", "Voc": "Sambodhana"}
GENDER_MAP = {"Masc": "Pum", "Fem": "Stri", "Neut": "Napumsaka"}
NUMBER_MAP = {"Sing": "Eka", "Dual": "Dvi", "Plur": "Bahu"}
PERSON_MAP = {"3": "Prathama", "2": "Madhyama", "1": "Uttama"}
KRDANTA_FORMS = {"Part", "Conv", "Gdv", "Inf"}
AVYAYA_UPOS = {"ADV", "PART", "CCONJ", "SCONJ", "ADP", "INTJ"}


def lakara_candidates(feats: dict) -> list[str]:
    tense, mood = feats.get("Tense"), feats.get("Mood")
    if mood == "Jus":
        return []                        # Vedic injunctive — out of scope
    if mood == "Imp":
        return ["Lot"]
    if mood == "Opt":
        return ["VidhiLin"]
    if mood == "Cnd":
        return ["Lrn"]
    if mood == "Ben":
        return ["AshirLin"]
    if tense == "Pres":
        return ["Lat"]
    if tense == "Impf":
        return ["Lan"]
    if tense == "Fut":
        return ["Lrt", "Lut"]            # vidyut arbitrates
    if tense == "Past":
        return ["Lun", "Lit", "Lan"]     # vidyut arbitrates
    if tense == "Perf":
        return ["Lit"]
    if tense == "Aor":
        return ["Lun"]
    return []


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "shastrartha-dcs-sampler"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def list_chapters(text: str) -> list[str]:
    data = json.loads(fetch(f"{API}/{urllib.parse.quote(text)}"))
    return sorted(e["name"] for e in data if e["name"].endswith(".conllu"))


def download_text(text: str, max_chapters: int) -> list[Path]:
    tdir = RAW / text
    tdir.mkdir(parents=True, exist_ok=True)
    cached = sorted(tdir.glob("*.conllu"))
    if cached:
        return cached[:max_chapters]
    paths = []
    for name in list_chapters(text)[:max_chapters]:
        dest = tdir / name
        if not dest.exists():
            url = f"{RAW_BASE}/{urllib.parse.quote(text)}/{urllib.parse.quote(name)}"
            dest.write_bytes(fetch(url))
            time.sleep(0.3)
        paths.append(dest)
    return paths


def parse_conllu(path: Path, text: str, genre: str):
    chapter = path.stem
    sent_id = None
    for line in path.open(encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("# sent_id"):
            sent_id = line.split("=", 1)[1].strip()
            continue
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 10 or not cols[0].isdigit():
            continue                     # skip multiword range rows etc.
        _, form, lemma, upos, _, feats_s, _, _, _, misc_s = cols[:10]
        feats = dict(kv.split("=", 1) for kv in feats_s.split("|")
                     if "=" in kv) if feats_s != "_" else {}
        misc = dict(kv.split("=", 1) for kv in misc_s.split("|")
                    if "=" in kv) if misc_s != "_" else {}
        surface = misc.get("Unsandhied") or form
        rec = {"source": "dcs", "text": text, "genre": genre,
               "chapter": chapter, "sent_id": sent_id,
               "surface": surface, "form": form, "lemma": lemma,
               "upos": upos, "feats": feats}

        if feats.get("Case") == "Cpd":
            rec["kind"] = "compound_member"
        elif feats.get("VerbForm") in KRDANTA_FORMS:
            rec["kind"] = "krdanta"
        elif upos == "VERB" and "Person" in feats:
            cands = lakara_candidates(feats)
            if not cands:
                rec["kind"] = "skipped_vedic_or_unmapped"
            else:
                rec["kind"] = "tinanta"
                rec["claim"] = {
                    "pos": "tinanta", "root": lemma,
                    "purusha": PERSON_MAP.get(feats.get("Person")),
                    "vacana": NUMBER_MAP.get(feats.get("Number")),
                    "lakara_candidates": cands,
                }
        elif upos in ("NOUN", "ADJ", "PRON", "NUM") and "Case" in feats:
            rec["kind"] = "subanta"
            rec["claim"] = {
                "pos": "subanta", "stem": lemma,
                "linga": GENDER_MAP.get(feats.get("Gender")),
                "vibhakti": CASE_MAP.get(feats.get("Case")),
                "vacana": NUMBER_MAP.get(feats.get("Number")),
            }
        elif upos in AVYAYA_UPOS:
            rec["kind"] = "avyaya"
            rec["claim"] = {"pos": "avyaya", "lemma": lemma}
        else:
            rec["kind"] = "other"
        yield rec


LICENSE_MD = """# DCS sample — license and attribution

Data in `raw/` is sampled from the Digital Corpus of Sanskrit (DCS),
github.com/OliverHellwig/sanskrit (dcs/data/conllu), licensed **CC BY 4.0**.

Citation (per upstream readme):

    @Manual{dcs,
      title  = {{The Digital Corpus of Sanskrit (DCS)}},
      author = {Hellwig, Oliver},
      year   = {2010--2024}}

Sampled by `agent/scripts/27_fetch_dcs.py` (genre-stratified, chosen to fill
morphological coverage gaps — see `agent/data/training/coverage.md`).
Converted records: `agent/data/training/dcs_pool.jsonl`.
"""


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    (AGENT / "data" / "dcs" / "README.md").write_text(LICENSE_MD, encoding="utf-8")
    TRAIN.mkdir(parents=True, exist_ok=True)

    all_recs, per_text = [], Counter()
    kinds, lakaras, vibhaktis = Counter(), Counter(), Counter()
    for text, genre, maxch in TARGETS:
        try:
            paths = download_text(text, maxch)
        except Exception as e:  # noqa: BLE001 — report and continue with the rest
            print(f"  ! {text}: {e}")
            continue
        n0 = len(all_recs)
        for p in paths:
            for rec in parse_conllu(p, text, genre):
                all_recs.append(rec)
                kinds[rec["kind"]] += 1
                if rec["kind"] == "tinanta":
                    for lk in rec["claim"]["lakara_candidates"]:
                        lakaras[lk] += 1
                elif rec["kind"] == "subanta":
                    vibhaktis[rec["claim"]["vibhakti"]] += 1
        per_text[text] = len(all_recs) - n0
        print(f"  {text}: {len(paths)} chapters, {per_text[text]} tokens")

    with (TRAIN / "dcs_pool.jsonl").open("w", encoding="utf-8") as f:
        for r in all_recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    def tbl(ctr):
        return "\n".join(f"| {k} | {n} |" for k, n in ctr.most_common())

    md = [
        "# DCS sample summary", "",
        f"{len(all_recs)} token records from {len(per_text)} texts "
        "(genre-stratified; see 27_fetch_dcs.py TARGETS).", "",
        "| text | tokens |", "|---|---|", tbl(per_text), "",
        "## Record kinds", "", "| kind | n |", "|---|---|", tbl(kinds), "",
        "## Tinanta lakāra candidates (pre-arbitration; ambiguous tags "
        "count once per candidate)", "",
        "| lakāra | n |", "|---|---|", tbl(lakaras), "",
        "## Subanta vibhakti", "", "| vibhakti | n |", "|---|---|",
        tbl(vibhaktis), "",
        "Ambiguous lakāras (Past→Luṅ/Liṭ/Laṅ, Fut→Lṛṭ/Luṭ) are resolved by "
        "vidyut derivation when the benchmark/training sets are built.", "",
    ]
    (TRAIN / "dcs_summary.md").write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {TRAIN}/dcs_pool.jsonl ({len(all_recs)} records) and dcs_summary.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
