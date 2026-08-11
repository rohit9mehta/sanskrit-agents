# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.30 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 14 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| dehī | dehin | Pum. Prathama/Eka | pass |
| nityam | nityam | indecl. | pass |
| avadhyaḥ | avadhya | Pum. Prathama/Eka | pass |
| ayam | idam | Pum. Prathama/Eka | pass |
| dehe | deha | Pum. Saptami/Eka | pass |
| sarvasya | sarva | Pum. Sasthi/Eka | pass |
| bhārata | bhārata | Pum. Sambodhana/Eka | pass |
| tasmāt | tasmāt | indecl. | pass |
| sarvāṇi | sarva | Napumsaka. Dvitiya/Bahu | pass |
| bhūtāni | bhūta | Napumsaka. Dvitiya/Bahu | pass |
| na | na | indecl. | pass |
| tvam | tvad | Pum. Prathama/Eka | pass |
| śocitum | śuc | indecl. | pass |
| arhasi | arh | arh, Kartari/Lat/Madhyama/Eka | pass |

## Justifications

**J1. dehī is not taken as the gross body itself. The bhāṣya glosses it as śarīrī, the possessor of a body, so the translation keeps “embodied one” rather than “body.”**
- chosen: “the embodied one (dehī)” (depends on commentary: **yes**)
- gita [1]: `dehī śarīrī` — “dehī” means “the embodied one / the possessor of a body.”

**J2. nityam is adverbial, qualifying the unslayability as holding at all times and in all conditions, not merely an attributive adjective “eternal” attached to dehī in English.**
- chosen: “always” (depends on commentary: **yes**)
- gita [1]: `nityaṃ sarvadā sarvāvasthāsu` — “nityam” means “always, in all states.”

**J3. avadhyaḥ is read ontologically, not as a merely moral injunction “not to be killed.” Śaṅkara grounds it in partlessness and eternality and explicitly says that even when the body is being killed, this dehī is not killed.**
- chosen: “unslayable / cannot be slain” (depends on commentary: **yes**)
- gita [1]: `avadhyaḥ niravayavatvān nityatvāc ca` — It is “unslayable” because it is partless and eternal.
- gita [2]: `dehe vadhyamāne 'py ayaṃ dehī na vadhyo yasmāt` — Because, even when the body is being killed, this embodied one is not to be slain / is not slain.

**J4. dehe is the locative “in the body,” and sarvasya is construed with an implied living being/class, not as “in all of the body.” The commentary glosses dehe by śarīre and expands sarvasya as prāṇi-jātasya.**
- chosen: “in the body of every living being” (depends on commentary: **yes**)
- gita [2]: `dehe śarīre` — “dehe” means “in the body.”
- gita [2]: `sarvasya prāṇi-jātasya dehe` — “in the body of every living being/class.”

**J5. tasmāt is causal-conclusive, picking up Śaṅkara’s yasmāt: because the dehī is not slain, therefore Arjuna should not grieve.**
- chosen: “therefore” as the conclusion from the dehī’s unslayability (depends on commentary: **yes**)
- gita [2]: `na vadhyo yasmāt, tasmād` — “because [it] is not slain, therefore …”

**J6. sarvāṇi bhūtāni is taken as the accusative object-domain of grieving, not as “all elements.” Śaṅkara’s uddiśya makes the accusative relation explicit and his bhīṣmādīni identifies the relevant beings as persons on the battlefield and the living beings associated with them.**
- chosen: “with regard to all beings (bhūtāni), such as Bhīṣma and the others” (depends on commentary: **yes**)
- gita [2]: `tasmād bhīṣmādīni sarvāṇi bhūtāni uddiśya na tvaṃ śocitum arhasi` — Therefore, with all beings such as Bhīṣma and the others in view, you ought not to grieve.

**J7. The construction na + infinitive śocitum + arhasi is rendered idiomatically as “you ought not to grieve.” This rests on Sanskrit grammar and MW s.v. arh, 93,3: arh with an infinitive can mean “to be allowed/required to do”; the commentary does not separately gloss arhasi here.**
- chosen: “you ought not to grieve” (depends on commentary: no)

## Translation

> The embodied one (dehī), this one, is always unslayable
in the body of every living being, O Bhārata.
Therefore, with regard to all beings (bhūtāni),
you ought not to grieve.

## Analyzer disagreements

- tvam: supplied masculine linga for the subanta analysis because the verifier requires linga/vibhakti/vacana and the addressee Arjuna is masculine; the surface form itself is common across genders.
- śocitum: the analyzer marks an infinitive (In). Since the response schema has no separate infinitive category, I encode the tumun infinitive as pos=avyaya with root śuc; this is an encoding adaptation, not a lexical disagreement.

## One-shot delta

- A commentary-blind translation might render avadhyaḥ as a moral “must not be killed”; Śaṅkara makes it metaphysical: the dehī is not slain even when the body is killed.
- It might take dehe sarvasya as “in the whole body” or “in all of the body”; the bhāṣya construes it as “in the body of every living being.”
- It might translate bhūtāni as “elements”; Śaṅkara points to Bhīṣma and others, so “beings” is required here.
- It might flatten nityam into the adjective “eternal”; the bhāṣya glosses it adverbially as “always, in all states.”
