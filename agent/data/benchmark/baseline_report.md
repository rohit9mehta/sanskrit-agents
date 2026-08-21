# Analyzer baseline: ByT5-Sanskrit (chronbmm/sanskrit5-multitask)

Benchmark: `analyzer_benchmark_v1.jsonl` (985 items, frozen 2026-08-21). Scoring: learned tag map `byt5_tagmap.json` (majority vote on non-benchmark DCS gold; decoding, not training).

## Headline

* aligned (surface found in SLM output): **95.1%** (937/985)
* tag mapped: 99.7% of aligned
* lemma accuracy (of aligned): **98.0%**
* morph features all-correct (of all items, unaligned/unmapped count as wrong): **90.1%**
* full claim (lemma + features): **88.3%**

## Per-field (of items where the model's tag was decodable; denominator = items with that field)

| field | acc | n |
|---|---|---|
| vibhakti | 98.9% | 609 |
| vacana | 99.7% | 934 |
| linga | 97.2% | 609 |
| lakara | 93.5% | 325 |
| purusha | 99.7% | 325 |

## Per-stratum (top by size)

| stratum | n | features-full | lemma |
|---|---|---|---|
| sub:Prathama:Eka | 47 | 91.5% | 93.6% |
| sub:Saptami:Bahu | 46 | 93.5% | 95.7% |
| tin:Lan:Kartari | 44 | 95.5% | 95.5% |
| sub:Trtiya:Eka | 44 | 93.2% | 97.7% |
| tin:VidhiLin:Kartari | 43 | 95.3% | 97.7% |
| tin:Lat:Karmani | 43 | 100.0% | 97.7% |
| sub:Caturthi:Eka | 42 | 100.0% | 100.0% |
| tin:Lrt:Kartari | 41 | 100.0% | 100.0% |
| sub:Saptami:Eka | 41 | 90.2% | 92.7% |
| sub:Prathama:Bahu | 41 | 82.9% | 87.8% |
| sub:Panchami:Eka | 41 | 68.3% | 80.5% |
| sub:Sasthi:Bahu | 40 | 95.0% | 97.5% |
| sub:Trtiya:Bahu | 39 | 100.0% | 100.0% |
| sub:Prathama:Dvi | 39 | 94.9% | 94.9% |
| tin:Lit:Kartari | 39 | 97.4% | 100.0% |
| tin:Lot:Kartari | 39 | 97.4% | 100.0% |
| sub:Dvitiya:Bahu | 38 | 92.1% | 94.7% |
| sub:Dvitiya:Eka | 36 | 80.6% | 91.7% |
| pipeline-hard | 35 | 68.6% | 28.6% |
| tin:Lat:Kartari | 35 | 97.1% | 97.1% |
| sub:Sasthi:Eka | 33 | 90.9% | 100.0% |
| sub:Sambodhana:Eka | 23 | 95.7% | 95.7% |
| sub:Dvitiya:Dvi | 21 | 95.2% | 100.0% |
| tin:Lun:Kartari | 20 | 5.0% | 90.0% |
| sub:Sasthi:Dvi | 17 | 88.2% | 94.1% |
| tin:Lot:Karmani | 13 | 100.0% | 100.0% |
| sub:Trtiya:Dvi | 12 | 100.0% | 100.0% |
| sub:Panchami:Bahu | 9 | 77.8% | 88.9% |
| sub:Caturthi:Bahu | 7 | 85.7% | 85.7% |
| tin:Lun:Karmani | 5 | 100.0% | 100.0% |
| tin:Lan:Karmani | 3 | 100.0% | 100.0% |
| sub:Sambodhana:Bahu | 3 | 100.0% | 100.0% |
| tin:Lut:Kartari | 2 | 0.0% | 100.0% |
| sub:Saptami:Dvi | 2 | 50.0% | 50.0% |
| sub:Panchami:Dvi | 1 | 100.0% | 100.0% |
| tin:VidhiLin:Karmani | 1 | 100.0% | 100.0% |

Tags decoded by the learned map where present, else positionally (128 items). ByT5's `Ps` tag is DCS's coarse Tense=Past — the model's tagset cannot distinguish perfect (Liṭ) from aorist (Luṅ); aorist items therefore score wrong by construction. This is a structural gap the fine-tune's explicit lakāra target closes.

Failure modes count against the model: unaligned (48) usually means wrong segmentation; unmapped tag (3) means the model emitted a tag too rare to decode (or hallucinated).
