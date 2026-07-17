# Triṃśikā v.13 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 13 pass / 0 fail / 0 unsupported.

## Verse

> **śāṭhyaṃ mado 'vihiṃsāhrīr atrapā styānam uddhataḥ āśraddhyam atha kausīdyaṃ pramādo muṣitā smṛtiḥ**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| śāṭhyam | śāṭhya | Napumsaka. Prathama/Eka | pass |
| madaḥ | mada | Pum. Prathama/Eka | pass |
| avihiṃsā | avihiṃsā | Stri. Prathama/Eka; tatpurusa ⟨na vihiṃsā⟩ | pass |
| ahrīḥ | ahrī | Stri. Prathama/Eka; tatpurusa ⟨na hrīḥ⟩ | pass |
| atrapā | atrapā | Stri. Prathama/Eka; tatpurusa ⟨na trapā⟩ | pass |
| styānam | styāna | Napumsaka. Prathama/Eka | pass |
| uddhataḥ | uddhata | Pum. Prathama/Eka | pass |
| āśraddhyam | āśraddhya | Napumsaka. Prathama/Eka | pass |
| atha | atha | indecl. | pass |
| kausīdyam | kausīdya | Napumsaka. Prathama/Eka | pass |
| pramādaḥ | pramāda | Pum. Prathama/Eka | pass |
| muṣitā | muṣita | Stri. Prathama/Eka | pass |
| smṛtiḥ | smṛti | Stri. Prathama/Eka | pass |

## Justifications

**J1. The masculine and feminine forms madaḥ, ahrīḥ, pramādaḥ, and smṛtiḥ are unambiguously nominative singular; therefore the neuter -am forms are read as nominative singular rather than accusative singular.**
- chosen: All listed items are construed as nominative singulars in a verbless enumeration. (depends on commentary: no)
- trbh []: `` — Grammatical evidence only: the verse is a coordinated list without a finite verb, and it contains several unambiguous nominative singular forms.

**J2. The printed mado 'vihiṃsā indicates an initial a after madaḥ; similarly, vihiṃsāhrīr is naturally avihiṃsā + ahrīḥ with vowel coalescence, and ahrīr atrapā shows visarga sandhi before the following a-. Treating a as an independent particle would leave an unsuitable vocative/letter-particle inside a technical nominal list.**
- chosen: avihiṃsā, ahrīḥ, and atrapā are privative a-/nañ compounds. (depends on commentary: no)
- trbh []: `` — Grammatical and lexical evidence only: MW’s supplied entry for a as a letter/vocative particle does not fit the syntax; productive privative a- yields meaningful nominal items, ‘non-/lack of X’.

**J3. The supplied base text has uddhataḥ, not the vulgate uddhavaḥ. The form -aḥ fits Pum Prathama Eka in the same list; deriving it from or associating it with ud-√han does not make the surface word a finite verb.**
- chosen: uddhataḥ is read as a masculine nominative singular substantive/adjective from stem uddhata. (depends on commentary: no)
- trbh []: `` — Grammatical evidence only: uddhataḥ has the ordinary masculine nominative singular ending -aḥ and is coordinated with other nominative list-items.

**J4. The form āśraddhyam is well-formed as a neuter nominative singular and fits the surrounding neuter abstract nouns. The vulgate āśraddham is not adopted because the requested base text gives āśraddhyam.**
- chosen: āśraddhyam is the supplied reading and is analyzed as neuter nominative singular of āśraddhya. (depends on commentary: no)
- trbh []: `` — Textual and grammatical evidence only: the prompt specifies the bhāṣya reading āśraddhyam; syntactically it aligns with śāṭhyam, styānam, and kausīdyam.

**J5. muṣitā is feminine nominative singular and agrees with smṛtiḥ, also feminine nominative singular. It is therefore read as a participial adjective modifying smṛtiḥ, not as a finite future form or as an uncompounded independent item.**
- chosen: muṣitā smṛtiḥ is a two-word phrase, ‘memory stolen/removed’. (depends on commentary: no)
- trbh []: `` — Grammatical and lexical evidence only: MW s.v. muṣ gives the sense ‘steal, carry off’; the feminine adjective muṣitā agrees with smṛtiḥ ‘memory’.

## Translation

> Deceit (śāṭhya), intoxicated pride (mada), non-injury (avihiṃsā),
shamelessness (ahrī), lack of bashfulness (atrapā), torpor or stiffness (styāna), the agitated/haughty state (uddhata);
then lack of faith (āśraddhya), indolence (kausīdya), heedlessness (pramāda),
and memory stolen away (muṣitā smṛti).

## Analyzer disagreements

- ByT5 segmented a_vihiṃsā_a_hrīḥ_a_trapā with independent a. I instead analyze avihiṃsā, ahrīḥ, and atrapā as privative nañ-compounds, because an independent vocative/letter-particle a is syntactically implausible in this nominal list, while the printed avagraha and vowel sandhi fit initial privative a- forms.
- ByT5 gives uddhataḥ with lemma uddhan. I treat the inflected nominal stem as uddhata, Pum Prathama Eka; ud-√han is at most a derivational source, not the nominal stem of the surface form.
- ByT5 gives muṣitā with lemma muṣ. I record the nominal stem as muṣita, Stri Prathama Eka, noting its participial derivation from √muṣ.
- For neuter -am forms such as śāṭhyam, styānam, āśraddhyam, and kausīdyam, I choose Prathama rather than Dvitiya because they are coordinated with unambiguous nominatives such as madaḥ, pramādaḥ, and smṛtiḥ in a verbless enumeration.

## One-shot delta

- Without commentary, the most plausible uncertainty is whether the printed 'vihiṃsā should be taken literally as avihiṃsā ‘non-injury’ or whether the technical context would require vihiṃsā ‘harmfulness’; this apparatus follows the supplied sandhi and grammar only.
- A commentary-blind analysis can identify uddhataḥ grammatically, but cannot securely determine whether it is intended as the technical mental-factor equivalent of auddhatya or another traditional label.
- Technical Yogācāra senses of styāna, āśraddhya, pramāda, and muṣitā smṛtiḥ may be narrower than their dictionary meanings; without commentary they are translated conservatively from grammar and lexicon.

## Open questions

- The literal grammatical reading avihiṃsā ‘non-injury/non-violence’ is odd if the verse is expected to enumerate defiled subsidiary factors; commentary would be needed to confirm or correct this segmentation.
- The exact intended technical value of uddhataḥ, and its relation to the vulgate uddhavaḥ, remains unresolved without commentary.
- Whether muṣitā smṛtiḥ should be treated as merely a phrase ‘memory stolen away’ or as a fixed technical expression cannot be settled from the supplied grammar alone.
