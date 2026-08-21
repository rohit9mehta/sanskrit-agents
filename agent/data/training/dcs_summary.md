# DCS sample summary

63433 token records from 9 texts (genre-stratified; see 27_fetch_dcs.py TARGETS).

| text | tokens |
|---|---|
| Hitopadeśa | 25040 |
| Kathāsaritsāgara | 9900 |
| Daśakumāracarita | 9698 |
| Buddhacarita | 5627 |
| Kirātārjunīya | 3680 |
| Meghadūta | 3393 |
| Rāmāyaṇa | 3030 |
| Viṣṇupurāṇa | 2656 |
| Arthaśāstra | 409 |

## Record kinds

| kind | n |
|---|---|
| subanta | 29398 |
| compound_member | 11295 |
| avyaya | 9400 |
| krdanta | 6406 |
| tinanta | 5032 |
| other | 1883 |
| skipped_vedic_or_unmapped | 19 |

## Tinanta lakāra candidates (pre-arbitration; ambiguous tags count once per candidate)

| lakāra | n |
|---|---|
| Lat | 2049 |
| Lan | 1812 |
| Lun | 1189 |
| Lit | 1189 |
| Lot | 601 |
| VidhiLin | 361 |
| Lrt | 209 |
| Lut | 209 |

## Subanta vibhakti

| vibhakti | n |
|---|---|
| Prathama | 12240 |
| Dvitiya | 6904 |
| Trtiya | 3377 |
| Sasthi | 2845 |
| Saptami | 2318 |
| Panchami | 764 |
| Sambodhana | 605 |
| Caturthi | 345 |

Ambiguous lakāras (Past→Luṅ/Liṭ/Laṅ, Fut→Lṛṭ/Luṭ) are resolved by vidyut derivation when the benchmark/training sets are built.
