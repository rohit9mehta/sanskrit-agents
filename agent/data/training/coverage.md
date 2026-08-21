# Training-data coverage report

Source: `agent/logs/vidyut_verifications.jsonl` — 10633 pipeline/handrun records kept (skipped: {'stage:sanity': 14, 'stage:test': 6, 'tool_error': 115}).

* Pool: **2047** deduped (surface, claim, result) entries → `pool.jsonl`
* Contrastive pairs (a1-fail → a2-pass): **38** → `contrastive.jsonl` (52 fails had no paired pass — surface was re-segmented on retry)
* Distinct nominal stems: **703**; distinct verbal roots: **71**

## Verified passes by part of speech

| pos | n |
|---|---|
| subanta | 4214 |
| tinanta | 702 |

## Subanta features

| vibhakti | n |
|---|---|
| Prathama | 2207 |
| Dvitiya | 790 |
| Trtiya | 225 |
| Caturthi | 56 |
| Panchami | 122 |
| Sasthi | 407 |
| Saptami | 266 |
| Sambodhana | 141 |

| vacana | n |
|---|---|
| Eka | 3409 |
| Dvi | 67 |
| Bahu | 738 |

| linga | n |
|---|---|
| Pum | 2287 |
| Stri | 656 |
| Napumsaka | 1271 |

## Tinanta features

| lakāra | n |
|---|---|
| Lat | 421 |
| Lit | 62 |
| Lut | 7 |
| Lrt | 59 |
| Lot | 82 |
| Lan | 16 |
| VidhiLin | 41 |
| AshirLin | 7 |
| Lun | 7 |
| Lrn | 0 |

| puruṣa | n |
|---|---|
| Prathama | 497 |
| Madhyama | 150 |
| Uttama | 55 |

| prayoga | n |
|---|---|
| Kartari | 627 |
| Karmani | 75 |
| Bhave | 0 |

## Samāsa relations (from `unsupported` notes)

| type | n |
|---|---|
| tatpurusa | 590 |
| karmadharaya | 118 |
| bahuvrihi | 372 |
| dvandva | 83 |
| avyayibhava | 0 |
| dvigu | 0 |

## Per text

| text | records |
|---|---|
| gita | 5126 |
| trbh | 2607 |
| yogasutra | 1657 |
| isa | 1243 |

## Gaps (feature values with < 20 verified examples)

These are the priority targets for the synthetic generator (vidyut forward derivation) and for choosing the next texts to onboard.

| feature | value | n |
|---|---|---|
| lakāra | Lut | 7 |
| lakāra | Lan | 16 |
| lakāra | AshirLin | 7 |
| lakāra | Lun | 7 |
| lakāra | Lrn | 0 |
| prayoga | Bhave | 0 |
| samāsa | avyayibhava | 0 |
| samāsa | dvigu | 0 |
