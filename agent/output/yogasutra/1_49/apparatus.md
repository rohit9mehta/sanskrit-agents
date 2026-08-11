# Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904) — 1.49 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 3 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| śrutānumānaprajñābhyām | śrutānumānaprajñā | Stri. Panchami/Dvi; dvandva ⟨śrutaprajñā ca anumānaprajñā ca⟩ | pass |
| anyaviṣayā | anyaviṣaya | Stri. Prathama/Eka; bahuvrihi ⟨anyaḥ viṣayaḥ yasyāḥ sā⟩ | pass |
| viśeṣārthatvāt | viśeṣārthatva | Napumsaka. Panchami/Eka; bahuvrihi ⟨viśeṣaḥ arthaḥ yasyāḥ sā, tasyā bhāvaḥ⟩ | pass |

## Justifications

**J1. Translate śrutānumānaprajñābhyām as “from the insights/cognitions of scriptural testimony and inference,” not merely “from what is heard and inferred.”**
- chosen: śruta means āgama-vijñāna, and anumāna is the parallel inferential cognition; together they form the two prajñās contrasted with samādhi-prajñā. (depends on commentary: **yes**)
- ys [1]: `śrutam āgamavijñānaṃ tat sāmānyaviṣayam.` — Śruta is knowledge from authoritative tradition; it has a general object.
- ys [3]: `tathānumānaṃ sāmānyaviṣayam eva.` — Likewise inference too has a general object.
- ys [9]: `tasmāc chrutānumānaprajñābhyām anyaviṣayā sā prajñā viśeṣārthatvād iti.` — Therefore that prajñā has an object different from the prajñās of śruta and inference, because it has the particular as its object.

**J2. Supply “that insight” as the subject and construe anyaviṣayā as feminine singular bahuvrīhi, “having a different object.”**
- chosen: anyaviṣayā qualifies sā prajñā, the samādhi-born insight, as having an object different from śruta- and anumāna-prajñā. (depends on commentary: **yes**)
- ys [9]: `tasmāc chrutānumānaprajñābhyām anyaviṣayā sā prajñā viśeṣārthatvād iti.` — Therefore that prajñā has an object different from the prajñās of śruta and inference, because it has the particular as its object.

**J3. Construe it with anya in the sense “different from,” yielding “different from the two cognitions of testimony and inference.”**
- chosen: The -bhyām ending in śrutānumānaprajñābhyām is ablative dual. (depends on commentary: no)

**J4. Take viśeṣa as the particular not accessible to scripture, inference, or ordinary perception, and artha as object/content rather than purpose.**
- chosen: viśeṣārthatvāt means “because its object is the particular.” (depends on commentary: **yes**)
- ys [6]: `tasmāc chrutānumānaviṣayo na viśeṣaḥ kaścid astīti.` — Therefore no particular at all is an object of śruta and inference.
- ys [7]: `na cāsya sūkṣmavyavahitaviprakṛṣṭasya vastuno lokapratyakṣeṇa grahaṇam asti.` — Nor is there grasping of this subtle, hidden, or remote thing by ordinary perception.
- ys [8]: `na cāsya viśeṣasyāpramāṇakasyābhāvo 'stīti samādhiprajñānirgrāhya eva sa viśeṣo bhavati bhūtasūkṣmagato vā puruṣagato vā.` — And it is not that this particular, because lacking a means of knowledge, is nonexistent; rather that particular is graspable only by samādhi-prajñā, whether it belongs to subtle elements or to puruṣa.
- ys [9]: `tasmāc chrutānumānaprajñābhyām anyaviṣayā sā prajñā viśeṣārthatvād iti.` — Therefore that prajñā has an object different from the prajñās of śruta and inference, because it has the particular as its object.

## Translation

> That insight (prajñā) has an object different from the insights of scriptural testimony (śruta/āgama) and inference (anumāna), because its object is the particular (viśeṣa).

## Analyzer disagreements

- ByT5 prints/analyzes anya_viṣayāḥ as viṣaya_PNM, but the unit has anyaviṣayā; the bhāṣya’s sā prajñā (line 9) confirms feminine nominative singular qualifying prajñā, not masculine nominative plural.
- ByT5 leaves śrutānumānaprajñābhyām only as a dual feminine form; I resolve -bhyām as ablative dual, not instrumental, because anya in the sense “different from” governs separation.
- ByT5 segments viśeṣa_artha_tvāt as though tva were the nominal base separately; I analyze the word as the neuter ablative singular of the abstract stem viśeṣārthatva, with -tva as suffix.

## One-shot delta

- A commentary-blind translation might render śruta as simply “what is heard”; Vyāsa specifies śruta as āgamavijñāna, cognition from authoritative tradition, and says it has only a general object.
- It might take viśeṣārthatvāt as “because of a special purpose”; the bhāṣya makes viśeṣa the particular grasped by samādhi-prajñā and denied as an object of śruta and anumāna.
- It might follow the analyzer’s anyaviṣayāḥ and read “other objects” in the plural; line 9 supplies sā prajñā, confirming feminine singular “that prajñā has a different object.”
