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
- ByT5-Sanskrit: pip `dharmamitra-sanskrit-grammar`; HF `sebastian-nehrdich/byt5-sanskrit-multitask`
- Vidyut (Pāṇinian derivation, Rust + Python bindings): github.com/ambuda-org/vidyut —
  good tiṅanta/kṛdanta/subanta coverage, PARTIAL samāsa coverage (verify compound members,
  not the compound relation)
- MITRA models/embeddings/corpora: HF org `buddhist-nlp`; MITRA-parallel: github.com/dharmamitra/mitra-parallel
- Corpora: GRETIL, DCS (github.com/OliverHellwig/sanskrit), dharmamitra.org tools
- Human baseline translation for eval: Buescher 2007 (Sthiramati's Triṃśikāvijñaptibhāṣya)

## Current phase: Phase 0 (see plan §4)
1. `pip install dharmamitra-sanskrit-grammar` and vidyut Python bindings; sanity-check both
   on lines from `data/input/trbh.txt.unsandhied`
2. Pull Triṃśikā root text (GRETIL/DCS); confirm bhāṣya covers all 30 kārikās
3. Build the pratīka-matcher: align each kārikā to its commentary span in trbh.txt
   (commentaries quote the mūla + `iti`; combine string match with embedding similarity)
4. Hand-run the full agent loop on ONE verse before writing orchestration code

## Conventions
- IAST transliteration throughout; keep Devanagari conversion as a display concern
- Every translation output must carry its apparatus (analysis, commentary citation
  with line numbers, grammar-check status); no bare translations
- Log every Vidyut verification outcome — this data seeds the follow-on
  "Pāṇini as reward function" research thread (plan §4, Phase 3)
- Old TF 1.x code in `code/` is reference-only; new code goes in a new `agent/` directory
