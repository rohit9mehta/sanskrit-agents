# Project: Commentary-Grounded Translation Agent for Sanskrit

## Context
Rohit did Sanskrit NLP research with Kurt Keutzer and Sebastian Nehrdich (UC Berkeley) in 2022.
This folder contains that work: a fork of Hellwig & Nehrdich's EMNLP 2018 sandhi/compound
splitter (char-level BiLSTM+CNN, TF 1.x), applied to the Triṃśikā-bhāṣya (Sthiramati's
Yogācāra commentary on Vasubandhu's Triṃśikā):
- `data/input/trbh.txt` — the bhāṣya, sandhi'd IAST, 1,560 lines
- `data/input/trbh.txt.unsandhied` — its segmented (padapāṭha) form, produced in 2022
- `code/` — upstream Hellwig-Nehrdich splitter (superseded; do not build on it)

That task (segmentation) is now solved by Nehrdich's ByT5-Sanskrit
(pip: `dharmamitra-sanskrit-grammar`, EMNLP Findings 2024). The new project is described in
**`commentary-grounded-translation-plan.md`** — read it first. Summary: an agent that
translates hard Sanskrit by (1) analyzing with ByT5-Sanskrit, (2) retrieving the verse's own
commentary (bhāṣya/ṭīkā) to resolve compounds/terms, (3) verifying morphology with
vidyut-prakriya (Pāṇinian derivation engine), (4) outputting translation + cited apparatus
justifying each contested choice.

## Why (evidence base)
- All models (frontier + MITRA) fail on complex compounds, philosophical terms, layered
  metaphor — per Mitrasaṃgraha (arXiv 2601.07314), IndicParam (arXiv 2512.00333),
  "Still Not There" (arXiv 2511.08145).
- Commentaries literally resolve these; no system retrieves them at inference time.
- Validated mechanism on 3 lines from trbh.txt (July 2026 session): one-shot translation
  was under-specified on v.2cd (gloss at lines 188–189), flattened the twofold upādi on
  v.3a (gloss at lines 203–215), and inverted authorial voice on line 147 (pūrvapakṣa
  marked by `iti ... tad ayuktam`). Commentary grounding fixed all three.

## Key resources
- ByT5-Sanskrit: HF `chronbmm/sanskrit5-multitask` (the published EMNLP-2024 multitask
  model; `sebastian-nehrdich/byt5-sanskrit-multitask` is 401/not public, and pip
  `dharmamitra-sanskrit-grammar` 0.1.7 is broken against the live API — we speak the
  current API schema directly in `agent/src/shastrartha/analyze.py`; see
  `agent/data/MANIFEST.md`)
- Vidyut (Pāṇinian derivation, Rust + Python bindings): github.com/ambuda-org/vidyut —
  good tiṅanta/kṛdanta/subanta coverage, PARTIAL samāsa coverage (verify compound members,
  not the compound relation)
- MITRA models/embeddings/corpora: HF org `buddhist-nlp`; MITRA-parallel: github.com/dharmamitra/mitra-parallel
- Corpora: GRETIL, DCS (github.com/OliverHellwig/sanskrit), dharmamitra.org tools
- Human baseline translation for eval: Buescher 2007 (Sthiramati's Triṃśikāvijñaptibhāṣya)

## Phase 0: COMPLETE (2026-07-15; see plan §4)
1. ✅ Toolbox sanity-checked (`agent/scripts/00–02`): local ByT5 primary analyzer
   (the API under-splits compounds — `agent/logs/sanity/byt5_report.md`), vidyut
   derivations + designed-negative + `unsupported` class all working
2. ✅ Mūla built from GRETIL (`agent/data/mula/trimsika.json`): 30/30 kārikās covered,
   bhāṣya reading primary, variants tabled (e.g. v.13 uddhataḥ vs vulgate uddhavaḥ)
3. ✅ Pratīka-matcher (`agent/src/shastrartha/match.py`): 30/30 anchors + spans,
   validated against a gold projection of GRETIL-comm pāda labels (72/72 units;
   embeddings not needed — lexical matching sufficed, see alignment/spot_check.md)
4. ✅ Hand-run on v.2 (`agent/handrun/v02/`): apparatus.md/.json with 5 commentary-
   dependent decisions, 15 vidyut-logged claims (12 pass, 3 unsupported samāsa
   relations), one-shot delta documented

## Next: Phase 1 (pipeline MVP, plan §4)
- Orchestrate the loop for single verses; the spec is the friction list in
  `agent/handrun/v02/notes.md` (claim-JSON → verify runner, verify_compound_claim
  helper, pinned MW source, span lookahead, requote retrieval)
- Run all 30 verses; compare vs MITRA Translate, raw frontier LLM, Buescher 2007
  (Buescher must come from the physical book — never from model memory)

## Conventions
- IAST transliteration throughout; keep Devanagari conversion as a display concern
- Every translation output must carry its apparatus (analysis, commentary citation
  with line numbers, grammar-check status); no bare translations
- Log every Vidyut verification outcome — this data seeds the follow-on
  "Pāṇini as reward function" research thread (plan §4, Phase 3)
- Old TF 1.x code in `code/` is reference-only; new code goes in a new `agent/` directory
