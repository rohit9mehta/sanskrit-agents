# Data manifest

External data used by the agent. Everything here is re-fetchable; `raw/`, `cache/`,
and `vidyut-*/` are gitignored.

## vidyut-0.4.0/
- Source: https://github.com/ambuda-org/vidyut/releases/download/py-0.4.0/data-0.4.0.zip
- Fetched: 2026-07-15 via `vidyut.download_data("data/vidyut-0.4.0")`
- Contents: chandas/ cheda/ kosha/ prakriya/ sandhi/
- All vidyut I/O is SLP1; convert from IAST with `vidyut.lipi`.

## raw/ (GRETIL plaintexts, fetched by scripts/03_fetch_mula.py)
- sa_vasubandhu-triMzikAvijJaptikArikA.txt — vulgate kārikās (DSBC input).
  Known typos: v.6 `ātmaduṣṭy-` (for `ātmadṛṣṭy-`), v.27 `hayupalambhataḥ`, v.30 `evānasravo`.
- sa_vasubandhu-triMzikAvijJaptikArikA-comm.txt — Triṃśikāvijñaptibhāṣya
  (Buescher 2007 critical-edition e-text, Fukita/Wille input) WITH pāda labels.
- License: GRETIL texts are CC BY-NC-SA 4.0 — the NC clause constrains any future
  dataset re-release (decide at Phase 3).

## Relationship of ../data/input/trbh.txt to GRETIL-comm
- Same e-text lineage (~0.994 token similarity, shared typos, e.g. `nāvatiṣṭḥata` ~line 1452).
- trbh.txt is the CANONICAL line space for this project: 1,560 lines, 1-indexed,
  never edited. All commentary citations are trbh.txt line numbers.

### KNOWN_GAPS (clauses present in GRETIL-comm but absent from trbh.txt — do NOT patch)
Full inventory from the gold projection (scripts/05_project_gold.py, ≥3-token
gaps; comm line → nearest trbh line):
- comm 50–52 → trbh 1: title line + `namo buddhāya` invocation
- comm 70 → trbh 45: `ātmādinirbhāso vikalpo rūpādinirbhāsaś cotpadyate tam`
- comm 88 → trbh 97: `...asattvāt utpannāvasthāyāṃ vijñānasyāpi tadākāreṇotpannatvān`
- comm 114 → trbh 196: `...tarhy aparicchinnālambanākāram kiṃ kāraṇam yasmād`
- comm 140 → trbh 249: `...evendriyasya sukhādivedanānukūlo yo vikāras tena sadṛśo`
- comm 316 → trbh 629: `praśrabdhisadbhāvāt tatra kāyakarmaṇyatā kāyasya svakāryeṣu`
- comm 336 → trbh 714: `saṃniśrayadānakarma mūḍhasyaiva hi`
- comm 382 → trbh 802: `ayañ ca kaukṛtyasparśasaṃniśrayadānakarmakaḥ dharmataiṣā yad`
- comm 668 → trbh 1494: `api pratipadyate na kevalaṃ grāhyābhāvam evaṃ hi`

## Hugging Face models (cached in ~/.cache/huggingface)
- chronbmm/sanskrit5-multitask (~2.3 GB) — ByT5-Sanskrit multitask (EMNLP Findings 2024).
  Task prefixes: `S ` segmentation, `L ` lemma, `M ` morphosyntax, `SL `, `SM `, `SLM `.
  NOTE: CLAUDE.md's `sebastian-nehrdich/byt5-sanskrit-multitask` returns 401 (not public);
  this is the published equivalent per the byt5-sanskrit-analyzers README.

## Dharmamitra API
- Endpoint: https://dharmamitra.org/api/tagging/
- Schema (verified 2026-07-14): request `{"texts": [...], "mode": ..., "input_encoding": "auto",
  "human_readable_tags": true}` → response `{"results": [...]}`. Currently returns
  segmentation regardless of mode. The pip package `dharmamitra-sanskrit-grammar` 0.1.7
  still sends `input_sentence` and gets HTTP 422 — do not depend on it.
- All responses cached under cache/ keyed by payload hash (see shastrartha/analyze.py).
