# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.36 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 13 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| avācyavādān | avācyavāda | Pum. Dvitiya/Bahu; karmadharaya ⟨avācyāḥ vādāḥ⟩ | pass |
| ca | ca | indecl. | pass |
| bahūn | bahu | Pum. Dvitiya/Bahu | pass |
| vadiṣyanti | vad | vad, Kartari/Lrt/Prathama/Bahu | pass |
| tava | tvad | Pum. Sasthi/Eka | pass |
| ahitāḥ | ahita | Pum. Prathama/Bahu | pass |
| nindantaḥ | nindant | Pum. Prathama/Bahu | pass |
| tava | tvad | Pum. Sasthi/Eka | pass |
| sāmarthyam | sāmarthya | Napumsaka. Dvitiya/Eka | pass |
| tatas | tatas | indecl. | pass |
| duḥkhataram | duḥkhatara | Napumsaka. Prathama/Eka | pass |
| nu | nu | indecl. | pass |
| kim | kim | Napumsaka. Prathama/Eka | pass |

## Justifications

**J1. The compound is not merely ‘speeches about the unspeakable’; Śaṅkara directly glosses avācya with avaktavya and keeps vāda as the utterance/speech to be said by the enemies.**
- chosen: avācya-vādān = ‘statements not fit to be uttered’, a karmadhāraya compound qualifying the accusative object of vadiṣyanti. (depends on commentary: **yes**)
- gita [1]: `avācya-vādān avaktavya-vādāṃś ca` — ‘avācya-vādān’ means ‘statements that are not to be spoken.’

**J2. The accusative plural bahūn qualifies avācya-vādān, and Śaṅkara expands it as aneka-prakārān, ‘of many sorts’.**
- chosen: bahūn means ‘many, of many kinds’. (depends on commentary: **yes**)
- gita [1]: `bahūn aneka-prakārān` — ‘many’ means ‘of numerous kinds.’

**J3. Rather than a vague ‘ill-wishers’ or ‘hostile ones’, Śaṅkara explicitly glosses the nominative subject as śatravaḥ, ‘enemies’.**
- chosen: ahitāḥ means ‘enemies’. (depends on commentary: **yes**)
- gita [1]: `tavāhitāḥ śatravaḥ` — ‘your ahitāḥ’ are ‘enemies.’

**J4. Śaṅkara glosses nindantaḥ by kutsayantaḥ, ‘reviling, disparaging’, and takes tava as tvadīyam modifying sāmarthyam. His added nivāta-kavacādi-yuddha-nimittam shows the sense is martial capacity/prowess rather than abstract logical ‘fitness’.**
- chosen: nindantaḥ tava sāmarthyam = ‘disparaging your prowess/capacity’. (depends on commentary: **yes**)
- gita [1]: `nindantaḥ kutsayantaḥ tava tvadīyaṃ sāmarthyaṃ nivāta-kavacādi-yuddha-nimittam` — ‘nindantaḥ’ means ‘disparaging’; ‘your sāmarthyam’ means ‘your own capacity/prowess, with reference to the battles with the Nivātakavacas and the like.’

**J5. The word is not temporal ‘thereafter’. Śaṅkara explains tatas as tasmāt nindā-prāpter duḥkhāt, making it the standard of comparison for duḥkhataram.**
- chosen: tatas is comparative/ablatival: ‘than that’, namely than the pain arising from the receipt of censure. (depends on commentary: **yes**)
- gita [2]: `tatas tasmāt nindā-prāpter duḥkhāt duḥkhataraṃ nu kim ?` — ‘tatas’ means ‘than that pain from the obtaining of censure—what is more painful?’

**J6. Śaṅkara paraphrases the question as a negative assertion: there is no more grievous pain than that.**
- chosen: duḥkhataraṃ nu kim is a rhetorical question: ‘what could be more painful than that?’ (depends on commentary: **yes**)
- gita [2]: `tataḥ kaṣṭataraṃ duḥkhaṃ nāstīty arthaḥ` — The meaning is: ‘There is no pain more grievous than that.’

## Translation

> Your enemies, while disparaging your prowess (sāmarthya), will utter many statements not fit to be spoken. What, then, could be more painful than that?

## Analyzer disagreements

- The api_seg alternative gives nindantaḥ te, but the unit text, local_S/local_SLM, and Śaṅkara’s line 1 read tava; I analyze the word as tava, genitive singular of tvad.
- ByT5 represents avācya-vādān internally as avācya + vādān; for the apparatus I treat the printed hyphenated expression as a single inflected compound stem avācyavāda, with the printed hyphen retained only in surface_in_sandhi.
- For both occurrences of tava, ByT5 marks only tvad_SG; I supply Ṣaṣṭhī singular and Pum. The form itself is gender-common in the second-person pronoun, but the addressee Arjuna is masculine and the verifier requires a linga value.
- For nindantaḥ, the inflectional participial stem is nindant, not nindat; nindant correctly yields nominative plural masculine nindantaḥ.
- For kim, ByT5 gives the dictionary base ka; I use the inflectional lemma kim for the neuter nominative singular form.

## One-shot delta

- A commentary-blind translation might take tato/tatas temporally as ‘afterwards’; Śaṅkara makes it comparative: ‘than the pain of receiving censure’ (line 2).
- It might render ahitāḥ only as ‘unfriendly people’; Śaṅkara specifies śatravaḥ, ‘enemies’ (line 1).
- It might treat sāmarthya as abstract ‘fitness’ or ‘adequacy’; Śaṅkara’s nivāta-kavacādi-yuddha-nimittam points to Arjuna’s martial prowess/capacity (line 1).
- It might miss that the final question is rhetorical; Śaṅkara paraphrases it as ‘there is no greater pain’ (line 2).
