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

## Phase 1: COMPLETE (2026-07-16; plan in `phase1-plan.md`)
- Reasoner: OpenAI `gpt-5.5-2026-04-23` (Rohit's key in `.env`, gitignored),
  structured outputs, one verify-feedback retry; ~$11.6 total spend
- 30/30 verses: `agent/output/vNN/apparatus.{json,md}` — 328 word-claims
  pass / 0 fail / 5 unsupported (avyayībhāva, tasil); 184 justification
  objects, 182 commentary-dependent; 107 analyzer overrides recorded
- Baselines in `agent/data/eval/`: raw-LLM (same model, verse-only), MITRA
  (endpoint: dharmamitra.org/api-search/cat-translate/v1/translate), human =
  Salvini 2022 (web-sourced, transcribed from page images, freely-distributed;
  Buescher 2007 still not digitized — add if physical copy obtained)
- 4-way comparison + aggregate stats: `agent/output/comparison.md`
- Verification log: 1,403 records (1,368 pipeline incl. failed first attempts
  — the Pāṇini-as-reward dataset); verifier gaps found and fixed during
  triage: ā/ī-stem nyap, anusvāra-vs-homorganic-nasal matching, ṇic sanādi,
  avyaya coverage (MW arbitration), avyayībhāva/tasil classes

## Phase 2: IN PROGRESS (automated parts done 2026-07-16)
- ✅ Citation audit: 304 evidence quotes vs cited trbh lines — 287 verbatim,
  17 near (≥98 fuzzy), 0 fabricated (`agent/output/citation_audit.md`)
- ✅ Ablations (`agent/output/ablations/ablation_report.md`): −verify-retry
  → 5 genuine claim failures return; −commentary → morphology unaffected but
  translations change substantially on 18/30 verses and commentary-dependent
  justifications drop 182→0. Orthogonal contributions demonstrated.
- ✅ Blinded eval harness: `agent/data/eval/packets/eval_packet.md` +
  response_TEMPLATE.csv (graders), answer_key.json + hard subset
  [1,2,3,6,11,13,14,16,29,30]; scoring = `scripts/15_score_eval.py`
  (win rates, exact sign tests, kappa) reading
  `agent/data/eval/packets/responses/grader_*.csv`
- ⏳ HUMAN STEP (Rohit): recruit 1–2 Sanskrit readers, send them
  eval_packet.md + the CSV template (~3–6 h each; honorarium customary);
  optional: physical Buescher 2007 → second reference column
- Then: run scoring, write the decision-gate memo (go/no-go for Phase 3)
- LLM spend to date: ~$17.5 est (hard stop $25, authorized $50)

## Phase 3 PREP: data + benchmark ready, training gated (2026-08-21)
Everything post-training needs EXCEPT the go decision (which waits on the
Phase 2 human eval) is built. Scripts 26–33; all outputs under agent/data/.
- ✅ Curation (`26`): 10,633 pipeline verification records → 2,047 deduped
  claims, 38 hard-negative pairs, `training/coverage.md` (genre skew
  quantified: Lṛṅ 0, Luṅ 7, Bhāve 0, subanta:tinanta 6:1)
- ✅ DCS sample (`27`, CC BY 4.0): 9 texts / 63k tokens, genre-stratified
  (narrative/kāvya for past tenses); `28` arbitrated with vidyut → 13,065
  gold claims (coarse DCS tags resolved by derivation)
- ✅ Benchmark FROZEN (`29`): `data/benchmark/analyzer_benchmark_v1.jsonl`,
  985 items (35 pipeline-hard + 950 DCS stratified), sha256 in MANIFEST.json.
  NEVER train on it; `training/split_v1.json` lists excluded keys.
- ✅ Synthetic (`31`): vidyut forward derivation, 34,719 pairs, flat across
  all 10 lakāras × 3 prayogas and 8 vibhaktis × 3 vacanas
- ✅ Train set (`32`): `training/trainset_v1.jsonl`, 46,379 records,
  weighted (pipeline 1.5 / hard 3.0 / dcs 1.0 / synthetic 0.5)
- ✅ Baseline scorer (`30`) + training skeleton (`33`, SFT of ByT5-Sanskrit
  on our explicit `pos=… lakara=…` target format; `--smoke` proves plumbing)
- Base-model memo: `data/benchmark/base_model_memo.md` (default: continue
  from ByT5-Sanskrit; tie-break rule stated). Compute for a real run is
  NOT covered by the $50 LLM authorization — separate decision.
- Leaderboard of every scored model: `data/benchmark/leaderboard.md`
- Critical path: aunty's grader CSV → `15_score_eval.py` → decision memo →
  if go: `33_train_analyzer.py` full run → compare vs baseline_report.md
- DECISION 2026-08-21: training PARKED. Override audit (519 reasoner
  overrides of ByT5 across 171 units): 46% segmentation/compound boundary
  (interpretive — commentary decides), 33% lemma convention, 14% case/
  number/gender, 1.5% tense/mood. The analyzer is not the bottleneck for
  these texts; revisit training when scaling to narrative/kāvya genres (then
  as joint segmentation+analysis).
- ✅ Lemma-normalization layer (`src/shastrartha/lemma.py`, 2026-08-21):
  ByT5 citations → verifier conventions (bare root + prefixes via kosha
  dhātu entries; ṇic/san stripped; participle stems from kosha Basic entries
  or derived by vidyut from the kosha's own Krdanta prātipadika; pronoun
  citations; feminine stems). Wired into `pipeline.default_analyze_fn` as
  `canonical_lemmas` hints + prompt rule (reasoner_v1/v2: cite canonical,
  don't log convention-only overrides). Measured by `35_mine_lemmas.py`
  (`--canonical` = residual): mismatches 218 → 80 of 1,459 aligned words
  (14.9% → 5.5%); remaining residual is mostly reasoner inconsistency
  (kim/ka, enad/etad/idam, -at/-ant) that the prompt rule now settles.
  verify.py `_stem_candidates` gained the śatṛ -at→-ant fallback.
- 2026-08-22: models moved to GPT-5.6 — reasoner `gpt-5.6-sol` (high),
  ask-box `gpt-5.6-luna` (medium); A/B vs terra in data/validation/ab_*.
  Human eval packets remain 5.5 output (kept deliberately).
- ✅ POST-TRAINING PoC DONE (2026-08-22, Modal A100, 35 min, ~$2; run 1 on
  A10G fp32 timed out at 5 h — bf16/checkpoints/streaming added):
  `analyzer-v1` = ByT5-Sanskrit SFT on trainset_v1 (46k, 3 ep) emitting our
  explicit `pos=… lakara=…` schema. Benchmark (985): features 90.1→92.5%,
  lemma 93.3→95.6%, claim 88.3→89.5%. Structural cells: aorist (Luṅ) 5→80%,
  Luṭ 0→100%, pipeline-hard 69→74% (lemma 29→43%). Regressions: duals
  (Dvitiya:Dvi 95→67%), vocative 96→78% — syncretic forms where context-free
  synthetic data teaches an arbitrary label; v2 fix = drop/deweight syncretic
  synthetic items, upweight DCS context. Report:
  data/benchmark/runs/analyzer-v1/report.md; weights on Modal volume
  `shastrartha-models/analyzer-v1/model`. Scripts 33/34 are the trainer +
  launcher (`modal run scripts/34_train_modal.py --run-name <tag>`).
- analyzer-v2 (2026-08-22): NEGATIVE. Dropping syncretic-surface synthetic
  items (−7,096) + context ×2 → 90.3/95.0/87.4; duals/vocatives unchanged,
  rare cells lost. Synthetic coverage is valuable; v1 remains the PoC. Run was
  cancelled externally at 92% (checkpoint-9000 evaluated via `--eval-only`).
  Open: why v1 dips on syncretic forms (context use? DCS label consistency?).
  Narrative draft: agent/docs/demo_narrative.md.

## Conventions
- IAST transliteration throughout; keep Devanagari conversion as a display concern
- Every translation output must carry its apparatus (analysis, commentary citation
  with line numbers, grammar-check status); no bare translations
- Log every Vidyut verification outcome — this data seeds the follow-on
  "Pāṇini as reward function" research thread (plan §4, Phase 3)
- Old TF 1.x code in `code/` is reference-only; new code goes in a new `agent/` directory
