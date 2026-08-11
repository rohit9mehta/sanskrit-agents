# Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904) — 1.33 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 3 pass / 0 fail / 1 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| maitrīkaruṇāmuditopekṣāṇām | maitrīkaruṇāmuditopekṣā | Stri. Sasthi/Bahu; dvandva ⟨maitrī ca karuṇā ca muditā ca upekṣā ca⟩ | pass |
| sukhaduḥkhapuṇyāpuṇyaviṣayāṇām | sukhaduḥkhapuṇyāpuṇyaviṣayā | Stri. Sasthi/Bahu; bahuvrihi ⟨sukha-duḥkha-puṇyāpuṇyāni viṣayāḥ yāsām tāḥ⟩ | pass |
| bhāvanātaḥ | bhāvanātaḥ | indecl. | unsupported |
| cittaprasādanam | cittaprasādana | Napumsaka. Prathama/Eka; tatpurusa ⟨cittasya prasādanam⟩ | pass |

## Justifications

**J1. The compound lists are not to be read as two undifferentiated groups. Vyāsa explicitly expands the sūtra into four separate prescriptions, assigning each attitude to its own object-class.**
- chosen: A one-to-one pairing: maitrī toward beings enjoying happiness, karuṇā toward the distressed, muditā toward the virtuous, and upekṣā toward those of unvirtuous conduct. (depends on commentary: **yes**)
- ys [1, 2, 3, 4]: `tatra sarvaprāṇiṣu sukhasaṃbhogāpanneṣu maitrīṃ bhāvayet.
duḥkhiteṣu karuṇām.
puṇyātmakeṣu muditām.
apuṇyaśīleṣūpekṣām.` — There, toward all living beings who have come into the enjoyment of happiness, one should cultivate friendliness; toward the distressed, compassion; toward those whose nature is virtuous, glad joy; toward those of unvirtuous conduct, equanimous overlooking.

**J2. Although the sūtra’s compound says “having happiness, suffering, virtue, and vice as their viṣaya,” Vyāsa interprets the practical targets in the locative plural as living beings: those enjoying happiness, the distressed, the virtuous, and those of unvirtuous conduct.**
- chosen: sukha, duḥkha, puṇya, and apuṇya are taken, in translation, as qualifying classes of beings rather than merely abstract objects. (depends on commentary: **yes**)
- ys [1, 2, 3, 4]: `sarvaprāṇiṣu sukhasaṃbhogāpanneṣu ... duḥkhiteṣu ... puṇyātmakeṣu ... apuṇyaśīleṣūpekṣām` — Among all living beings who are in the enjoyment of happiness … among the distressed … among the virtuous … among those of unvirtuous conduct.

**J3. Vyāsa glosses the sūtra’s bhāvanā with the verbal instruction bhāvayet and then with bhāvayataḥ, showing an intentional practice of cultivating these dispositions.**
- chosen: bhāvanātaḥ means “from/through cultivation,” not merely “from imagination” or “from feeling.” (depends on commentary: **yes**)
- ys [1, 5]: `maitrīṃ bhāvayet.
evam asya bhāvayataḥ śuklo dharma upajāyate.` — One should cultivate friendliness. Thus, for him who is cultivating in this way, white dharma arises.

**J4. Vyāsa explains the result by saying that the mind becomes prasanna; he further characterizes that clarified mind as one-pointed and attaining a stable state.**
- chosen: cittaprasādanam is the clarification or serenity of the mind, with one-pointed steadiness following from that clarity. (depends on commentary: **yes**)
- ys [5, 6, 7]: `evam asya bhāvayataḥ śuklo dharma upajāyate.
tataś ca cittaṃ prasīdati.
prasannam ekāgraṃ sthitipadaṃ labhate.` — Thus, for him who cultivates in this way, white dharma arises. And from that the mind becomes clear/serene. Being clear, it becomes one-pointed and obtains a state of steadiness.

## Translation

> Through cultivating friendliness (maitrī), compassion (karuṇā), appreciative joy (muditā), and equanimous overlooking (upekṣā), respectively in regard to beings enjoying happiness, the distressed, the virtuous, and those of unvirtuous conduct, there is clarification of the mind (citta-prasādana).

## Analyzer disagreements

- ByT5 tagged sukhaduḥkhapuṇyāpuṇyaviṣayāṇām as viṣaya_PGM, i.e. masculine genitive plural. I analyze it as feminine genitive plural bahuvrīhi adjective agreeing with maitrī-karuṇā-muditā-upekṣāṇām; Vyāsa’s four accusative attitudes with four locative target-classes support this construal.
- ByT5 tagged bhāvanātaḥ as bhāvanā_SBF, apparently a feminine ablative singular subanta. I treat bhāvanātaḥ as an ablatival indeclinable in -taḥ, since the regular ā-stem ablative would be bhāvanāyāḥ; syntactically it still means “from/through cultivation.”

## One-shot delta

- A commentary-blind rendering might take sukha, duḥkha, puṇya, and apuṇya as abstract objects only; Vyāsa makes them practical target-classes of beings.
- It might miss the one-to-one distribution of the four attitudes across the four classes; Vyāsa spells out the pairing line by line.
- It might parse viṣayāṇām as an independent masculine genitive plural, “of the objects,” rather than as a feminine genitive plural adjective qualifying the four attitudes.
- It might translate prasādanam as generic “propitiation” or “soothing”; Vyāsa defines the result as the mind becoming prasanna, then ekāgra and stable.
