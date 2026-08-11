# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.27 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 15 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| jātasya | jāta | Pum. Sasthi/Eka | pass |
| hi | hi | indecl. | pass |
| dhruvaḥ | dhruva | Pum. Prathama/Eka | pass |
| mṛtyuḥ | mṛtyu | Pum. Prathama/Eka | pass |
| dhruvam | dhruva | Napumsaka. Prathama/Eka | pass |
| janma | janman | Napumsaka. Prathama/Eka | pass |
| mṛtasya | mṛta | Pum. Sasthi/Eka | pass |
| ca | ca | indecl. | pass |
| tasmāt | tasmāt | indecl. | pass |
| aparihārye | aparihārya | Pum. Saptami/Eka | pass |
| arthe | artha | Pum. Saptami/Eka | pass |
| na | na | indecl. | pass |
| tvam | yuṣmad | None. Prathama/Eka | pass |
| śocitum | śuc | indecl. | pass |
| arhasi | arh | arh, Kartari/Lat/Madhyama/Eka | pass |

## Justifications

**J1. The genitive is not taken as an abstract “of birth” but as a substantivized participle referring to a born person or being.**
- chosen: jātasya = “of one who has obtained birth / one born” (depends on commentary: **yes**)
- gita [1]: `jātasya hi labdha-janmanaḥ` — “jātasya, that is, of one who has obtained birth.”

**J2. Both occurrences of dhruva are translated as “certain,” not merely “fixed” in a physical sense, because Śaṅkara glosses dhruvaḥ with avyabhicārī, “not deviating/failing.”**
- chosen: dhruvaḥ/dhruvam = “certain, invariable” (depends on commentary: **yes**)
- gita [1]: `dhruvo 'vyabhicārī mṛtyur maraṇaṃ dhruva janma mṛtasya ca` — “dhruvaḥ means invariable; mṛtyuḥ is death; and birth is certain for one who has died.”

**J3. The verse’s mṛtyuḥ is ordinary death/dying, not Death personified, since the commentary glosses it by maraṇam.**
- chosen: mṛtyuḥ = “death,” specifically maraṇam (depends on commentary: **yes**)
- gita [1]: `mṛtyur maraṇaṃ` — “mṛtyuḥ is maraṇam, death.”

**J4. artha is not rendered as “purpose” or “wealth,” but as the matter/state of affairs constituted by birth and death; the locative is construed with the following prohibition of grief: in such an unavoidable matter, grief is not appropriate.**
- chosen: aparihārye arthe = “in/regarding this unavoidable matter” (depends on commentary: **yes**)
- gita [2, 3]: `tasmād aparihāryo 'yaṃ janma-maraṇa-lakṣaṇo 'rthaḥ | tasminn aparihārye 'rthe na tvaṃ śocitum arhasi` — “Therefore this matter, characterized by birth and death, is unavoidable. In that unavoidable matter you ought not to grieve.”

**J5. arhasi with the infinitive śocitum is modal: “you are not entitled/fit/required to grieve,” idiomatically “you should not grieve.”**
- chosen: na tvaṃ śocitum arhasi = “you should not grieve” (depends on commentary: **yes**)
- gita [3]: `na tvaṃ śocitum arhasi` — “you ought not to grieve.”

**J6. The particle introduces the reason for the preceding teaching: birth entails death and death entails birth. This is decided from ordinary grammar and usage rather than an explicit gloss in the commentary.**
- chosen: hi = “for” (depends on commentary: no)

## Translation

> For one who is born, death is certain;
and for one who has died, birth is certain.
Therefore, in this unavoidable matter (artha),
you should not grieve.

## Analyzer disagreements

- jātasya: ByT5 reports lemma/root jan; here it is analyzed as the inflected participial nominal stem jāta, masculine genitive singular, supported by Śaṅkara’s gloss labdha-janmanaḥ.
- mṛtasya: ByT5 reports lemma/root mṛ; here it is analyzed as the inflected participial nominal stem mṛta, masculine genitive singular.
- tasmāt: ByT5 leaves it effectively as an uninflected segment; here it is represented as an avyaya causal adverb, in line with its idiomatic use and Śaṅkara’s inferential explanation.
- tvam: ByT5 reports lemma tvad and the prior apparatus assigned masculine gender; corrected to the pronoun stem yuṣmad, nominative singular, with no grammatical linga assigned to the common-gender form.
- śocitum: ByT5 marks an infinitive from śuc; retained, but represented in this schema as an avyaya infinitive with root śuc rather than as a finite verb.

## One-shot delta

- A commentary-blind translation might take artha in aparihārye 'rthe as “purpose” or “object,” whereas Śaṅkara identifies it as the unavoidable matter characterized by birth and death.
- It might render dhruva merely as “fixed” or “permanent”; Śaṅkara’s avyabhicārī points to “certain/invariable.”
- It might miss that jātasya and mṛtasya are substantivized participles—“of one born” and “of one dead”—rather than abstract nouns.
- It might over-literalize na śocitum arhasi as “you do not deserve to grieve,” while the bhāṣya supports the idiomatic modal sense “you should not grieve.”

## Open questions

- Line 1 of the supplied commentary reads “dhruva janma” without the expected neuter ending in the verse’s dhruvaṃ janma; this appears to be a surface/segmentation irregularity in the plaintext, not a different interpretation.
