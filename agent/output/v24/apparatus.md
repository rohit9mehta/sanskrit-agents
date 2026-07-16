# Triṃśikā v.24 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 10 pass / 2 fail / 0 unsupported.

## Verse

> **prathamo lakṣaṇenaiva niḥsvabhāvo 'paraḥ punaḥ na svayaṃbhāva etasyety aparā niḥsvabhāvatā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| prathamaḥ | prathama | Pum. Prathama/Eka | pass |
| lakṣaṇena | lakṣaṇa | Napumsaka. Trtiya/Eka | pass |
| eva | eva | indecl. | pass |
| niḥsvabhāvaḥ | niḥsvabhāva | Pum. Prathama/Eka; bahuvrihi ⟨na vidyate svabhāvo yasya saḥ⟩ | pass |
| aparaḥ | apara | Pum. Prathama/Eka | pass |
| punaḥ | punar | indecl. | **fail — UNVERIFIED** |
| na | na | indecl. | pass |
| svayambhāvaḥ | svayambhāva | Pum. Prathama/Eka; tatpurusa ⟨svayaṃ bhāvaḥ⟩ | pass |
| etasya | etad | Pum. Sasthi/Eka | pass |
| iti | iti | indecl. | pass |
| aparā | apara | Stri. Prathama/Eka | pass |
| niḥsvabhāvatā | niḥsvabhāvatā | Stri. Prathama/Eka | **fail — UNVERIFIED** |

## Justifications

**J1. The masculine prathamaḥ is not taken as modifying the feminine niḥsvabhāvatā; it elliptically denotes the first svabhāva, supplied by Sthiramati as parikalpitaḥ svabhāvaḥ.**
- chosen: prathamaḥ refers to the imagined nature (parikalpita-svabhāva). (depends on commentary: **yes**)
- trbh [1403]: `prathamaḥ parikalpitaḥ svabhāvo 'yaṃ ca lakṣaṇenaiva niḥsvabhāvas` — ‘First’ means the imagined nature; and this is natureless by the defining-character itself.

**J2. The instrumental is not a positive means (‘by a mark it is natureless’) but the respect in which the parikalpita is natureless: its very lakṣaṇa/svarūpa is projected and absent, like a sky-flower.**
- chosen: lakṣaṇenaiva means ‘by/in respect of its defining-character alone,’ because that characteristic is imagined and so lacks own-form. (depends on commentary: **yes**)
- trbh [1404, 1405, 1406, 1407]: `tallakṣaṇasyotprekṣitatvāt
rūpalakṣaṇaṃ rūpam
anubhavalakṣaṇā vedanetyādi
ataś ca svarūpābhāvāt khapuṣpavat svarūpeṇaiva niḥsvabhāvaḥ` — Because its defining-character is imagined. Form is what has form as its characteristic; feeling has experience as its characteristic, and so on. Therefore, because its own-form is absent, like a sky-flower it is natureless by its own-form itself.

**J3. The ‘other’ is not the perfected nature and not an unspecified second item; Sthiramati explicitly glosses aparaḥ punar as paratantrasvabhāvaḥ.**
- chosen: aparaḥ punar denotes the dependent nature (paratantra-svabhāva). (depends on commentary: **yes**)
- trbh [1408]: `aparaḥ punar iti paratantrasvabhāvaḥ` — ‘The other, again’ means the dependent nature.

**J4. Although svayaṃbhāva/svayambhāva could be translated mechanically as ‘own-being,’ the commentary explains it by dependent origination from other conditions and names the resulting type utpatti-niḥsvabhāvatā. Thus the point is lack of independent arising, not sheer non-existence like the parikalpita.**
- chosen: na svayaṃbhāva etasya is rendered ‘there is no self-arising of this,’ and aparā niḥsvabhāvatā is the arising-naturelessness of the dependent nature. (depends on commentary: **yes**)
- trbh [1409, 1410, 1411, 1412]: `na svayaṃbhāva etasya māyāvat
parapratyayenotpatteḥ
ataś ca yathā prakhyāti tathāsyotpattir nāstīty ato
'syotpattiniḥsvabhāvatety ucyate` — There is no self-arising of this, as with an illusion, because it arises through another condition. Therefore, because its arising does not exist in the way it appears, this is called its arising-naturelessness.

## Translation

> The first—the imagined nature (parikalpita-svabhāva)—is natureless (niḥsvabhāva)
by its defining-character (lakṣaṇa) alone.
The other—the dependent nature (paratantra-svabhāva)—again has no self-arising;
“there is no self-arising of this”: that is the other naturelessness (niḥsvabhāvatā).

## Analyzer disagreements

- ByT5 gives punar as the analyzed surface; since the verse has pāda-final/pausal punaḥ, I record surface punaḥ and lemma punar.
- ByT5’s lemma svayambhāva is adopted, but its segmented surface svayaṃbhāvaḥ is normalized in the pausal surface field to svayambhāvaḥ for vidyut derivation; the printed sandhi-form remains svayaṃbhāva.
- ByT5 splits niḥsvabhāvatā as niḥsvabhāva_Cp + tā_SNF; I analyze it as one feminine nominal stem niḥsvabhāvatā, Prathama singular.

## One-shot delta

- A commentary-blind rendering might make prathamaḥ and aparaḥ refer to two abstract niḥsvabhāvatās; Sthiramati instead identifies them as the parikalpita and paratantra svabhāvas.
- It might translate lakṣaṇenaiva as ‘by means of a mark’ or ‘with a characteristic’; the commentary makes it ‘in respect of defining-character/own-form,’ because that characteristic is imagined and absent.
- It might render svayaṃbhāva as generic ‘own-being’ and flatten the second case into the first; Sthiramati explains it specifically as absence of independent arising, since the paratantra arises through other conditions.
- It might miss that aparā niḥsvabhāvatā is, in Sthiramati’s terminology, utpatti-niḥsvabhāvatā, ‘arising-naturelessness.’
