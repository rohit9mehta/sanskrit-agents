# Hand-run postmortem (v.2) — friction list = Phase 1 orchestration spec

What was done manually this run, and what Phase 1 must automate or fix.

## What worked without friction
1. **Alignment → retrieval is one lookup.** `trimsika_alignment.json` gave
   anchor + span; span text (with line numbers) is the whole RETRIEVE stage
   for a bhāṣya-internal verse. No embeddings needed at this scale.
2. **SLM output is directly usable.** Every v.2 token's lemma+tag from
   `chronbmm/sanskrit5-multitask` was correct and parseable; the reasoner
   only ADDED the samāsa analyses (which the tag scheme marks `Cp` but does
   not resolve) — confirming the division of labor.
3. **The verify loop caught nothing false here** (all 12 checkable claims
   pass), but the sanity run's designed negative proves failures would be
   caught and logged. The `unsupported` class (3 samāsa relations this run)
   is accumulating exactly the data the Pāṇini-as-reward thread needs.

## Friction → Phase 1 requirements
1. **Claim extraction is manual.** I hand-translated my analysis table into
   `verify_claims.py`. Phase 1: the reasoner must emit claims in a JSON
   schema (surface, stem/root, features, compound members+relation) that a
   runner feeds to verify.py mechanically. The reasoner prompt already
   demands "checkable form"; wire it end to end.
2. **MW lookup is ad hoc.** curl→Cologne getword.php worked but is fragile
   HTML scraping. Phase 1: pin a proper MW source (CSL JSON dumps or local
   copy), lemma→entry function with page/col citation baked in.
3. **Compound policy needs one canonical helper.** "Whole-inflected-compound
   as opaque stem (prakriya) + relation `unsupported` + member kosha checks"
   was assembled by hand three times. Make `verify_compound_claim()`.
4. **Span borders.** v.2's span [169,201] already contains the ālambana
   discussion pivoting to v.3ab (190–201 lead directly to the quote at 202,
   with a KNOWN_GAP dropped clause near trbh 196). Retrieval should hand the
   reasoner span + a 2–3 line lookahead past the next anchor, marked as such.
5. **Requotes are retrieval gold.** 2c's requote at trbh 231 opens the
   sthiti section. Phase 1 retrieval: include requote loci (already in the
   alignment JSON) as secondary evidence.
6. **Baseline discipline.** Buescher comparison must come from the physical
   book (or a scan Rohit provides) — the apparatus explicitly refuses
   model-memory fills. Same rule for MITRA baselines: run, don't recall.
7. **Cost/latency note.** Local SLM on 2 lines: ~seconds on MPS after a
   ~30 s model load; keep the model resident in the Phase 1 runner.

## Phase 0 exit criterion — met
- apparatus.md + apparatus.json exist with per-word analysis, line-cited
  commentary evidence, and translation;
- every morphological claim has a logged vidyut outcome
  (`run_id=handrun-v02-01`: 12 pass, 3 unsupported, 0 fail, 0 tool_error);
- J1–J5 each cite commentary that changed a decision vs the one-shot delta.
