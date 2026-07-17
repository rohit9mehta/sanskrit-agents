# Triṃśikā v.12 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 9 pass / 0 fail / 0 unsupported.

## Verse

> **mānadṛgvicikitsāś ca mrakṣaḥ pradāśa īrṣyātha mātsaryaṃ saha māyayā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| mānadṛgvicikitsāḥ | mānadṛgvicikitsā | Stri. Prathama/Bahu; dvandva ⟨mānaś ca dṛk ca vicikitsā ca⟩ | pass |
| ca | ca | indecl. | pass |
| mrakṣaḥ | mrakṣa | Pum. Prathama/Eka | pass |
| pradāśaḥ | pradāśa | Pum. Prathama/Eka | pass |
| īrṣyā | īrṣyā | Stri. Prathama/Eka | pass |
| atha | atha | indecl. | pass |
| mātsaryam | mātsarya | Napumsaka. Prathama/Eka | pass |
| saha | saha | indecl. | pass |
| māyayā | māyā | Stri. Trtiya/Eka | pass |

## Justifications

**J1. The printed form is one compound-word ending in -āḥ through the final member vicikitsā. The preceding elements māna and dṛś/dṛg are therefore compound members, not separately inflected syntactic nouns. The following ca coordinates the compound-list with the larger enumeration.**
- chosen: mānadṛgvicikitsāḥ as a feminine nominative plural itaretara-dvandva: ‘conceit, view, and doubt’. (depends on commentary: no)
- trbh []: `` — Grammar/analyzer: māna and dṛś are marked as compound pre-members, while vicikitsāḥ bears the feminine nominative plural ending; this supports an itaretara-dvandva analysis.

**J2. The sequence is best explained by regular vowel coalescence: īrṣyā + atha gives printed īrṣyātha. Thus atha is an indeclinable list-particle, not part of a noun such as artha.**
- chosen: īrṣyātha = īrṣyā + atha. (depends on commentary: no)
- trbh []: `` — Grammar/analyzer: the supplied segmentation reads īrṣyā_atha; ā + a contracts to ā in the printed īrṣyātha.

**J3. Although mātsaryam is formally ambiguous between nominative and accusative singular, the surrounding items are nominative members of an enumeration, and there is no finite verb requiring an accusative object. The instrumental māyayā is governed by saha, not by mātsaryam.**
- chosen: mātsaryam as neuter Prathama singular, not an accusative object. (depends on commentary: no)
- trbh []: `` — Grammar/analyzer: mātsaryam is tagged as neuter nominative singular; the list-context favors nominative continuation after mrakṣaḥ, pradāśaḥ, and īrṣyā.

**J4. saha is taken as an indeclinable preposition/postposition construed with the instrumental māyayā. It is not an adjective qualifying mātsaryam.**
- chosen: saha māyayā = ‘together with deceit’. (depends on commentary: no)
- trbh []: `` — Grammar: saha commonly construes with an instrumental; māyayā is Stri Trtiya Eka.

**J5. The verse is a catalogue of mental factors/defilements, so the lexical choices are the ethical senses where available: vicikitsā as doubt, mrakṣa as concealment of faults/hypocrisy, īrṣyā as envy, mātsarya as jealousy or stinginess, and māyā as deceit/fraud. māna is rendered in the standard Buddhist-technical sense ‘conceit’, and dṛg as ‘view’.**
- chosen: Ethical/afflictive lexical senses for the list-items. (depends on commentary: no)
- trbh []: `MW s.v. vicikitsā: ‘doubt, uncertainty’; MW s.v. mrakṣa: ‘concealment of one’s vices, hypocrisy’; MW s.v. īrṣyā: ‘envy’; MW s.v. mātsarya: ‘envy, jealousy’; MW s.v. māyā: ‘deception, fraud’.` — These dictionary senses fit an enumerative list of afflictive mental terms better than physical or non-ethical senses such as mere seeing, magic, or neutral uncertainty.

## Translation

> Conceit (māna), view (dṛg), and doubt (vicikitsā) too; / concealment of faults (mrakṣa), spite (pradāśa), envy (īrṣyā), then / jealousy or stinginess (mātsarya), together with deceit (māyā).

## Analyzer disagreements

- The tagger displays māna and dṛś as compound pre-members and vicikitsāḥ as the inflected final member; I report the whole verse-word as the inflected dvandva compound mānadṛgvicikitsāḥ, as requested for compounds.
- For atha, I record the actual printed sandhi contribution as tha within īrṣyātha, rather than the analyzer’s unsandhied segment atha.
- No substantive disagreement with the analyzer’s nominal tags for mrakṣaḥ, pradāśaḥ, īrṣyā, mātsaryam, or māyayā.

## One-shot delta

- Without commentary, māna and dṛg are especially vulnerable to being flattened into ‘opinion’ and ‘seeing’ rather than the technical pair ‘conceit’ and ‘view’.
- The sandhi īrṣyātha could be misread as involving artha, producing an erroneous ‘for the sake of envy’ or ‘envy-object’ construal.
- The neuter mātsaryam could be mistaken for an accusative object rather than a nominative member of the list.
- Without the bhāṣya reading supplied here, one might import the vulgate krodhopanahane punaḥ into the verse even though it is absent from the present reading.

## Open questions

- No commentary was available in this ablation run, so the precise Yogācāra definitions of māna, dṛg, pradāśa, mātsarya, and māyā are not independently established here.
- The rendering of mātsarya as general ‘jealousy’ versus more technical ‘stinginess/avarice’ would need commentary or a Buddhist lexicon to settle more securely.
