# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.34 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 12 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| akīrtim | akīrti | Stri. Dvitiya/Eka | pass |
| ca | ca | indecl. | pass |
| api | api | indecl. | pass |
| bhūtāni | bhūta | Napumsaka. Prathama/Bahu | pass |
| kathayiṣyanti | kath | kath, Kartari/Lrt/Prathama/Bahu | pass |
| te | tvad | Pum. Sasthi/Eka | pass |
| avyayām | avyaya | Stri. Dvitiya/Eka | pass |
| saṃbhāvitasya | saṃbhāvita | Pum. Sasthi/Eka | pass |
| ca | ca | indecl. | pass |
| akīrtiḥ | akīrti | Stri. Prathama/Eka | pass |
| maraṇāt | maraṇa | Napumsaka. Panchami/Eka | pass |
| atiricyate | ric | ati-ric, Karmani/Lat/Prathama/Eka | pass |

## Justifications

**J1. The enclitic te is construed as genitive singular dependent on akīrtim, not as dative ‘to you’. Thus bhūtāni kathayiṣyanti te akīrtim means ‘people will tell of your disgrace’, not ‘will tell disgrace to you’.**
- chosen: te = tava, ‘your’ (depends on commentary: **yes**)
- gita [1]: `te tava` — te means ‘of you/your’ (tava).

**J2. Although avyaya can mean ‘imperishable’ or ‘unchanging’, Śaṅkara glosses the accusative feminine here as dīrgha-kālām, so it qualifies akīrtim as a disgrace that lasts a long time.**
- chosen: avyayām = dīrgha-kālām, ‘long-lasting’ (depends on commentary: **yes**)
- gita [1]: `avyayāṃ dīrgha-kālām` — avyayām means ‘of long duration’.

**J3. The genitive saṃbhāvitasya is a substantive participial adjective referring to someone esteemed because of qualities such as being righteous and brave; it is not a finite or active notion such as ‘of one who has imagined/considered’.**
- chosen: saṃbhāvitasya = ‘of one held in esteem’ (depends on commentary: **yes**)
- gita [2]: `dharmātmā śūra ity evam ādibhiḥ guṇaiḥ saṃbhāvitasya` — of one esteemed by qualities such as ‘righteous-souled’ and ‘brave’. 

**J4. The ablative maraṇāt is comparative with atiricyate. Śaṅkara’s paraphrase makes the value judgment explicit: for an esteemed person, death is preferable to disgrace.**
- chosen: akīrtiḥ maraṇāt atiricyate = ‘disgrace is worse than death’ (depends on commentary: **yes**)
- gita [2]: `akīrtiḥ maraṇāt atiricyate, saṃbhāvitasya ca akīrteḥ varaṃ maraṇam ity arthaḥ` — disgrace surpasses death; the meaning is that, for one held in esteem, death is better than disgrace.

**J5. Grammatically the neuter plural bhūtāni is the subject of the third plural verb kathayiṣyanti. In context it is best rendered ‘people’ or ‘living beings’, not ‘elements’ or inert ‘things’.**
- chosen: bhūtāni = living beings/people as the plural subject (depends on commentary: no)

## Translation

> And people too will recount
 your long-lasting disgrace;
and, for one who has been held in honour,
 disgrace is worse than death.

## Analyzer disagreements

- kathayiṣyanti: ByT5 gives lemma kathay; following the requested format I give the bare root kath, noting the kathay- stem formation.
- te: ByT5 marks tvad only generally; Śaṅkara’s gloss te tava fixes the case as genitive singular rather than dative singular. I record masculine for the nominal feature set, since the addressed referent is Arjuna, while noting that the second-person form is not semantically gender-marked.
- saṃbhāvitasya: ByT5 gives sambhāvay as lemma; I analyze the verse-form as an inflected nominal/participial stem saṃbhāvita, masculine genitive singular, as required for subantas.
- atiricyate: ByT5 effectively gives the prefixed verbal base atiric; following the requested format I split this into bare root ric with prefix ati.

## One-shot delta

- A commentary-blind rendering might take te as dative, producing ‘they will tell infamy to you’; Śaṅkara fixes it as tava, ‘your’ (line 1).
- It might render avyayām as a metaphysical ‘imperishable’; Śaṅkara’s dīrgha-kālām shows the intended sense is ‘long-lasting’ reputation (line 1).
- It might miss that saṃbhāvitasya refers to a person esteemed for qualities like righteousness and courage; Śaṅkara supplies that social-honor context (line 2).
- It might translate atiricyate blandly as ‘exceeds’; Śaṅkara’s paraphrase makes the practical force explicit: death is preferable to ill fame for such a person (line 2).

## Open questions

- Commentary line 1 contains an apparent corrupt or intrusive ‘yuddhā’ between cāpi and bhūtāni; I have not relied on that reading.
