# Triṃśikā v.8 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 10 pass / 0 fail / 0 unsupported.

## Verse

> **dvitīyaḥ pariṇāmo 'yam tṛtīyaḥ ṣaḍvidhasya yā | viṣayasyopalabdhiḥ sā kuśalākuśalādvayā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| dvitīyaḥ | dvitīya | Pum. Prathama/Eka | pass |
| pariṇāmaḥ | pariṇāma | Pum. Prathama/Eka | pass |
| ayam | idam | Pum. Prathama/Eka | pass |
| tṛtīyaḥ | tṛtīya | Pum. Prathama/Eka | pass |
| ṣaḍvidhasya | ṣaḍvidha | Pum. Sasthi/Eka; bahuvrihi ⟨ṣaḍ vidhāḥ yasya saḥ⟩ | pass |
| yā | yad | Stri. Prathama/Eka | pass |
| viṣayasya | viṣaya | Pum. Sasthi/Eka | pass |
| upalabdhiḥ | upalabdhi | Stri. Prathama/Eka | pass |
| sā | tad | Stri. Prathama/Eka | pass |
| kuśalākuśalādvayā | kuśalākuśalādvaya | Stri. Prathama/Eka; dvandva ⟨kuśalā ca akuśalā ca advayā ca⟩ | pass |

## Justifications

**J1. The first clause supplies the masculine head pariṇāmaḥ. Since upalabdhiḥ is feminine, tṛtīyaḥ cannot grammatically agree with it; the natural construal is “the third [transformation].”**
- chosen: tṛtīyaḥ is masculine because it construes with ellipsed pariṇāmaḥ, not directly with upalabdhiḥ. (depends on commentary: no)
- trbh []: `dvitīyaḥ pariṇāmo 'yam tṛtīyaḥ ... yā ... upalabdhiḥ` — “This is the second transformation; the third [transformation] is the apprehension ...”

**J2. Both ṣaḍvidhasya and viṣayasya are masculine genitive singular, and their proximity supports adjective-head agreement: “of the sixfold object.” Reading ṣaḍvidhasya as dependent on tṛtīyaḥ would leave viṣayasya less naturally integrated with upalabdhiḥ.**
- chosen: ṣaḍvidhasya modifies viṣayasya. (depends on commentary: no)
- trbh []: `tṛtīyaḥ ṣaḍvidhasya yā | viṣayasyopalabdhiḥ` — “the third: the apprehension of the sixfold object”

**J3. The dictionary gives upalabdhi as “observation, perceiving, perception,” and viṣaya as “scope/range/object.” In this collocation, “apprehension of an object” is grammatically and contextually preferable to “acquisition of a territory/domain.”**
- chosen: viṣayasya is an objective genitive with upalabdhiḥ, and upalabdhiḥ means “apprehension/perception.” (depends on commentary: no)
- trbh []: `viṣayasyopalabdhiḥ` — “apprehension of the object”

**J4. The relative yā and correlative sā are both feminine nominative singular, matching upalabdhiḥ. Thus sā does not resume pariṇāmaḥ but the apprehension just named.**
- chosen: yā ... sā is a relative-correlative frame referring to upalabdhiḥ. (depends on commentary: no)
- trbh []: `yā ... upalabdhiḥ sā` — “whatever apprehension ... that [apprehension]”

**J5. The expression coordinates kuśala, akuśala, and advaya as nominative feminine predicates agreeing with sā/upālabdhiḥ. Since advaya follows the pair kuśala/akuśala, a privative reading “neither of the two” is preferable here to an abstract metaphysical “non-dual.”**
- chosen: kuśalākuśalādvayā is unpacked as “wholesome, unwholesome, or neither.” (depends on commentary: no)
- trbh []: `sā kuśalākuśalādvayā` — “that is wholesome, unwholesome, or neither”

## Translation

> This is the second transformation (pariṇāma).
The third is the apprehension (upalabdhi)
of the sixfold object (ṣaḍvidha viṣaya);
that is wholesome (kuśala), unwholesome (akuśala), or neither (advaya).

## Analyzer disagreements

- The api_seg output missegments the last pāda as maya_akuśala_advayā; the printed verse and local_S/local_SLM support kuśala-akuśala-advayā, so maya is rejected.
- ByT5 exposes kuśala/akuśala/a/dvayā as components. I report the printed expression as the single inflected coordinate compound kuśalākuśalādvayā while preserving those components in the samāsa analysis.

## One-shot delta

- Without commentary, the exact referents of “sixfold object” are not fixed here; the grammar only supports “object of six kinds.”
- A commentary-blind rendering could mistranslate upalabdhiḥ as “acquisition” rather than “apprehension/perception.”
- A commentary-blind rendering could take advayā as doctrinal “non-dual” rather than the third alternative, “neither wholesome nor unwholesome.”
- A commentary-blind rendering could miss the ellipsis in tṛtīyaḥ and try to make it agree with feminine upalabdhiḥ.

## Open questions

- No commentary was supplied in this ablation, so the specific six objects meant by ṣaḍvidhasya viṣayasya cannot be established from the present evidence.
- No commentary was supplied, so whether advayā is intended to correspond technically to avyākṛta/indeterminate remains unconfirmed.
- The final expression may be represented either as a tight coordinate compound or as three sandhi-joined feminine predicates; I adopt the compound analysis because it matches the printed continuous form and the analyzer’s component analysis.
