# Triṃśikā v.29 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 10 pass / 0 fail / 1 unsupported.

## Verse

> **acitto 'nupalambo 'sau jñānaṃ lokottarañ ca tat āśrayasya parāvṛttir dvidhādauṣṭhulyahānitaḥ**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| acittaḥ | acitta | Pum. Prathama/Eka; tatpurusa ⟨na cittaḥ⟩ | pass |
| anupalambaḥ | anupalamba | Pum. Prathama/Eka; tatpurusa ⟨na upalambaḥ⟩ | pass |
| asau | adas | Pum. Prathama/Eka | pass |
| jñānam | jñāna | Napumsaka. Prathama/Eka | pass |
| lokottaram | lokottara | Napumsaka. Prathama/Eka; tatpurusa ⟨lokād uttaram⟩ | pass |
| ca | ca | indecl. | pass |
| tat | tad | Napumsaka. Prathama/Eka | pass |
| āśrayasya | āśraya | Pum. Sasthi/Eka | pass |
| parāvṛttiḥ | parāvṛtti | Stri. Prathama/Eka | pass |
| dvidhā | dvidhā | indecl. | pass |
| dauṣṭhulyahānitaḥ | dauṣṭhulyahānitaḥ | indecl.; tatpurusa ⟨dauṣṭhulyasya hāniḥ; tasmāt⟩ | unsupported |

## Justifications

**J1. The gender mismatch is best handled by grouping the three masculine forms together and the three neuter forms together, rather than forcing acittaḥ/anupalambaḥ to agree with jñānam.**
- chosen: acittaḥ anupalambaḥ asau forms a masculine nominative predication, while jñānam lokottaram ca tat forms a neuter nominative predication. (depends on commentary: no)
- trbh []: `acitto 'nupalambo 'sau jñānaṃ lokottarañ ca tat` — The printed sequence contains masculine nominative singular acittaḥ, anupalambaḥ, asau, followed by neuter nominative singular jñānam, lokottaram, tat.

**J2. The neuter nominative singular adjective lokottaram agrees with neuter nominative singular jñānam and tat. The dictionary sense ‘surpassing the world, extraordinary’ supports ‘supramundane’ in a Buddhist philosophical verse.**
- chosen: lokottaram modifies jñānam: ‘supramundane/beyond-the-world knowledge’. (depends on commentary: no)
- trbh []: `jñānaṃ lokottarañ ca tat` — jñānam, lokottaram, and tat are all neuter singular forms, naturally read in apposition/predication.

**J3. The genitive āśrayasya is construed dependently on the nominative noun parāvṛttiḥ. Nothing in the grammar requires an ablatival ‘from the basis’; the given case is genitive.**
- chosen: āśrayasya parāvṛttiḥ means ‘the turning/transformation of the basis’. (depends on commentary: no)
- trbh []: `āśrayasya parāvṛttir` — ‘parāvṛttiḥ of āśraya’: a genitive relation between ‘basis/support’ and ‘turning/transformation’.

**J4. The ending -taḥ is not the normal ablative singular of the feminine i-stem hāni; therefore the form is better understood as an indeclinable -taḥ formation from the compound dauṣṭhulya-hāni. dvidhā is translated broadly as ‘twofold/in two ways’.**
- chosen: dauṣṭhulyahānitaḥ is a causal/ablatival indeclinable: ‘because of the abandonment/removal of badness’. (depends on commentary: no)
- trbh []: `dvidhādauṣṭhulyahānitaḥ` — The sequence is read as dvidhā + dauṣṭhulya-hānitaḥ: ‘twofold / because of abandonment of badness’.

**J5. Grammar alone does not decide whether dvidhā primarily qualifies the abandonment/removal or the badness removed. A compact ‘twofold abandonment of badness’ preserves the ambiguity better than a fully specified doctrinal paraphrase.**
- chosen: dvidhā is left with a broad ‘twofold’ scope in translation. (depends on commentary: no)
- trbh []: `dvidhā dauṣṭhulyahānitaḥ` — dvidhā is an indeclinable immediately preceding the compound; either ‘in two ways’ or ‘twofold’ is grammatically possible.

## Translation

> Non-mind (acitta), non-apprehension (anupalambha)—this;
and that is supramundane knowledge (lokottara-jñāna).
It is the turning of the basis (āśraya-parāvṛtti),
because of the twofold abandonment of badness (dauṣṭhulya).

## Analyzer disagreements

- ByT5 api_seg offers dauṣṭhulya_hānyāḥ, but the supplied bhāṣya line and local_S read dauṣṭhulya_hānitaḥ; I analyze the printed form dauṣṭhulyahānitaḥ.
- ByT5 local_SLM treats hānitaḥ as hāni_SBF, i.e. a subanta-like feminine ablative analysis. I instead take dauṣṭhulyahānitaḥ as an indeclinable -taḥ/tasil causal form, since a regular feminine i-stem ablative singular of hāni would not be hānitaḥ.
- ByT5 tokenizes dauṣṭhulya and hānitaḥ separately; I record the syntactic word as the compound-derived indeclinable dauṣṭhulyahānitaḥ.

## One-shot delta

- With no commentary, the referent of the masculine asau and the reason for the switch to neuter tat/jñānam remain inferential rather than secured by exposition.
- A commentary-blind translation may over-specify dvidhā as either ‘two kinds of badness’ or ‘two kinds of abandonment’; the grammar by itself does not force one scope.
- A purely dictionary-based rendering of acitta as ‘inconceivable’ or ‘unnoticed’ is possible from MW, but the verse’s pairing with anupalambha and jñāna favors the more technical ‘non-mind/non-mental’ rendering.

## Open questions

- The precise antecedent or implied masculine noun for acittaḥ anupalambaḥ asau is not recoverable from the verse grammar alone.
- The exact doctrinal content of the ‘twofold’ in dvidhā is not determined without commentary or context.
- The technical nuance of āśraya in āśrayasya parāvṛttiḥ is rendered as ‘basis’, but the verse alone does not define it.
