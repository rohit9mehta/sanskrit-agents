# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.32 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 11 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| yadṛcchayā | yadṛcchā | Stri. Trtiya/Eka | pass |
| ca | ca | indecl. | pass |
| upapannam | upapanna | Napumsaka. Dvitiya/Eka | pass |
| svargadvāram | svargadvāra | Napumsaka. Dvitiya/Eka; tatpurusa ⟨svargasya dvāram⟩ | pass |
| apāvṛtam | apāvṛta | Napumsaka. Dvitiya/Eka | pass |
| sukhinaḥ | sukhin | Pum. Prathama/Bahu | pass |
| kṣatriyāḥ | kṣatriya | Pum. Prathama/Bahu | pass |
| pārtha | pārtha | Pum. Sambodhana/Eka | pass |
| labhante | labh | labh, Kartari/Lat/Prathama/Bahu | pass |
| yuddham | yuddha | Napumsaka. Dvitiya/Eka | pass |
| īdṛśam | īdṛśa | Napumsaka. Dvitiya/Eka | pass |

## Justifications

**J1. The instrumental yadṛcchayā is taken adverbially to mark that the battle has come without being sought.**
- chosen: yadṛcchayā = “unsolicitedly / of itself,” not primarily “by one’s own will.” (depends on commentary: **yes**)
- gita [1]: `yadṛcchayā ca aprārthitatayā` — “yadṛcchayā—i.e. by not having been asked for / unsolicitedly.”

**J2. The participle is not translated here as “fitting” or “reasonable,” but as describing the battle as having presented itself.**
- chosen: upapannam = “come, arrived.” (depends on commentary: **yes**)
- gita [1]: `upapannam āgataṃ` — “upapannam—come/arrived.”

**J3. svargadvāram is a tatpuruṣa, ‘gate of/to heaven,’ and apāvṛtam means ‘opened.’ The commentary explicitly glosses apāvṛtam by udghāṭitam; the precise compound relation is grammatical rather than explicitly explained by Śaṅkara.**
- chosen: svargadvāram apāvṛtam = “an opened gate to heaven.” (depends on commentary: **yes**)
- gita [1]: `svarga-dvāram apāvṛtam udghāṭitaṃ` — “the gate to heaven, opened—unbarred/opened up.”

**J4. Śaṅkara recasts the syntax as a relative sentence: those kṣatriyas who obtain such a battle—are they not sukhinaḥ? This prevents reading sukhinaḥ merely as an attributive adjective, ‘happy kṣatriyas obtain…’.**
- chosen: sukhinaḥ is predicative: “fortunate/happy are the kṣatriyas who obtain…” (depends on commentary: **yes**)
- gita [1]: `ya etad īdṛśaṃ yuddhaṃ labhante kṣatriyāḥ he pārtha, kiṃ na sukhinas te ?` — “Those kṣatriyas who obtain this such battle, O Pārtha—are they not happy/fortunate?”

**J5. The commentary’s order etad īdṛśaṃ yuddhaṃ labhante makes yuddham the object and confirms īdṛśam as its qualifier; upapannam, svarga-dvāram, and apāvṛtam are construed with the same accusative object phrase.**
- chosen: yuddham īdṛśam is the direct object of labhante; the preceding accusative neuters describe that battle. (depends on commentary: **yes**)
- gita [1]: `ya etad īdṛśaṃ yuddhaṃ labhante kṣatriyāḥ` — “the kṣatriyas who obtain this such battle.”

## Translation

> And when such a battle comes of itself, unsolicited—
an opened gate to heaven—
fortunate are the kṣatriyas, O Pārtha,
who obtain it.

## Analyzer disagreements

- upapannam: the tagger gave lemma/root upapad and a nominative-looking tag; I analyze the word-form as the accusative singular neuter nominal stem upapanna, a kta-participle from upa-√pad, because it agrees with yuddham as the object phrase and is glossed upapannam āgatam in the commentary (line 1).
- apāvṛtam: the tagger gave lemma/root apāvṛ and a nominative-looking tag; I analyze the word-form as the accusative singular neuter nominal stem apāvṛta, a kta-participle, agreeing with svarga-dvāram/yuddham and glossed apāvṛtam udghāṭitam in the commentary (line 1).
- For neuter forms upapannam, svarga-dvāram, apāvṛtam, yuddham, and īdṛśam, nominative and accusative are formally identical; I select accusative because Śaṅkara construes etad īdṛśaṃ yuddhaṃ as the object of labhante (line 1).

## One-shot delta

- Without the commentary, sukhinaḥ could easily be read as merely attributive, “happy kṣatriyas obtain…,” whereas Śaṅkara makes it a predicate: those who obtain such a battle are fortunate.
- upapannam might be flattened to “suitable” or “proper”; Śaṅkara’s āgatam shows the intended sense is “come/presented itself.”
- yadṛcchayā might be translated vaguely as “by chance”; Śaṅkara sharpens it to aprārthitatayā, “without being sought.”
- apāvṛtam should be taken as “opened/unbarred,” not just “uncovered,” because Śaṅkara glosses it with udghāṭitam.
