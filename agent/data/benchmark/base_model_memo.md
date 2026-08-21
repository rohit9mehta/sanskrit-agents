# Base-model decision memo — analyzer post-training (Phase 3)

Status: DRAFT 2026-08-21, baseline measured. Decision is gated on the Phase 2
human-eval go/no-go; benchmark numbers are in (`baseline_report.md`,
`leaderboard.md`).
Everything below is the reasoning that makes the decision a table lookup
once those numbers exist.

## Baseline (measured 2026-08-21)

ByT5-Sanskrit as-is on `analyzer_benchmark_v1` (985 items): **90.1%**
morph-features-correct, **88.3%** full claim (features + lemma); lemma 98%
of aligned; 4.9% unaligned (segmentation misses). Where it fails:

* **Luṅ (aorist) 5%** — structural: ByT5's DCS-derived `Ps` tag conflates
  perfect/aorist/imperfect-past; the model cannot emit the distinction.
  Our gold (vidyut-resolved) can. The fine-tune's explicit `lakara=` target
  closes this by construction.
* **Luṭ (periphrastic future) 0%**, pipeline-hard stratum 68.6% features /
  28.6% lemma (in-domain śāstric hard cases — lemma disagreements are partly
  citation-convention, partly real).
* Everything common (Prathama/Dvitiya/…, Laṭ/Liṭ/Loṭ/Laṅ) is 88–100%.

So the fine-tune target is not "beat 90% overall" in the abstract — it is:
keep the common cells, fix the aorist/Luṭ cells (structurally), reduce
segmentation misses, and move the pipeline-hard stratum. Report per-stratum,
not just headline.

## What is being decided

Which pretrained checkpoint to fine-tune into the pipeline's *grammar
analyzer* — the component that maps (sentence, word) → morphological claim,
which today is ByT5-Sanskrit with GPT-5.5 overriding it on hard cases (107
overrides in Phase 1). The reasoner/translator stays an API model; this
decision concerns the analyzer only.

## Criteria (in priority order)

1. **Benchmark accuracy after fine-tuning** on `analyzer_benchmark_v1`
   (985 items; features-full and full-claim metrics). Untrained
   benchmark score is informative but not decisive — the fine-tune is the
   product.
2. **Tokenization fit for IAST.** Diacritics (ā ī ū ṛ ṝ ḷ ṃ ḥ ś ṣ ñ ṅ ṇ ṭ ḍ)
   are phonemic. Subword vocabularies built on English/Hindi fragment them
   into multi-token sequences and sometimes normalize them away — a direct
   hit to a morphology task, where a single diacritic IS the feature
   (devā vs deva, gacchet vs gacchat). Byte-level models read them losslessly.
3. **Size / inference cost.** Target: runs locally on Apple Silicon or a
   cheap GPU at ≥10 words/s; the point is to remove the frontier-model
   override loop, not to relocate it.
4. **License** permitting research + redistribution of weights.
5. **Engineering risk** — how far the training recipe is from known-good.

## Candidates

| candidate | params | tokenizer | Sanskrit pretraining | license | notes |
|---|---|---|---|---|---|
| **ByT5-Sanskrit** (`chronbmm/sanskrit5-multitask`) | ~580M | byte | yes (EMNLP-F 2024; segmentation/lemma/morph multitask) | Apache-2.0 (per upstream ByT5; confirm card) | our current analyzer; continues from a Sanskrit-adapted state; byte-level → criterion 2 perfect |
| ByT5-base (google) | 580M | byte | no | Apache-2.0 | same architecture minus Sanskrit adaptation — dominated by the above |
| Qwen2.5-0.5B / 1.5B-Instruct | 0.5–1.5B | BPE | incidental | Apache-2.0 | byte-fallback BPE mangles IAST; decoder-only formatting flexibility isn't needed for a fixed-schema task |
| Gemma-2-2B | 2.6B | SentencePiece | incidental | Gemma ToU | 4× larger for unclear gain; tokenizer same concern |
| mT5-base | 580M | SentencePiece | incidental (Hindi/Marathi adjacency) | Apache-2.0 | diacritics survive better than BPE but still fragmented |

## Recommendation (pending numbers)

**Default: continue from ByT5-Sanskrit.** It wins criteria 2, 3, 4, 5
outright and is the only candidate that starts Sanskrit-aware. The
fine-tune replaces its undocumented multitask tag format with our explicit
`pos=… lakara=…` schema (see `scripts/33_train_analyzer.py`), so the
verifier's claim fields are emitted directly — no tag-map decoding.

**Tie-break rule:** a non-byte candidate must beat the ByT5 fine-tune on
full-claim accuracy by ≥3 points on the benchmark *and* match it on the
rare-lakāra strata (Luṅ, Lṛṅ, Luṭ, Āśīrliṅ) to justify the tokenizer risk
and size. Otherwise ByT5-Sanskrit.

**Run order when the gate opens:** (1) ByT5-Sanskrit SFT on
`trainset_v1` (46k records, weighted); (2) if budget allows, one
Qwen2.5-0.5B SFT as the control; (3) RL/rejection-sampling pass on the
winner with vidyut pass/fail as reward.

## Compute estimate

ByT5-Sanskrit SFT, 46k examples × 3 epochs, seq ≤512 bytes: ~2–4 GPU-hours
on a single A10/L4-class card (≈$5–15 rented), or overnight on an M-series
Mac via MPS. Not covered by the $50 LLM-API authorization — needs its own
line.
