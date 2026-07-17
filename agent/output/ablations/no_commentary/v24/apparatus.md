# Triṃśikā v.24 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 12 pass / 0 fail / 0 unsupported.

## Verse

> **prathamo lakṣaṇenaiva niḥsvabhāvo 'paraḥ punaḥ na svayaṃbhāva etasyety aparā niḥsvabhāvatā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| prathamaḥ | prathama | Pum. Prathama/Eka | pass |
| lakṣaṇena | lakṣaṇa | Napumsaka. Trtiya/Eka | pass |
| eva | eva | indecl. | pass |
| niḥsvabhāvaḥ | niḥsvabhāva | Pum. Prathama/Eka; bahuvrihi ⟨niḥ/vigataḥ svabhāvo yasya⟩ | pass |
| aparaḥ | apara | Pum. Prathama/Eka | pass |
| punaḥ | punar | indecl. | pass |
| na | na | indecl. | pass |
| svayaṃbhāvaḥ | svayaṃbhāva | Pum. Prathama/Eka; tatpurusa ⟨svayaṃ bhāvaḥ⟩ | pass |
| etasya | etad | Pum. Sasthi/Eka | pass |
| iti | iti | indecl. | pass |
| aparā | apara | Stri. Prathama/Eka | pass |
| niḥsvabhāvatā | niḥsvabhāvatā | Stri. Prathama/Eka | pass |

## Justifications

**J1. prathamaḥ is a substantivized masculine nominative subject and niḥsvabhāvaḥ is its masculine nominative predicate adjective; lakṣaṇenaiva gives the instrumental basis or respect.**
- chosen: “The first is without own-being precisely by its defining mark.” (depends on commentary: no)
- trbh []: `` — Grammatical reasoning: prathamaḥ and niḥsvabhāvaḥ are both masculine nominative singular, making subject plus predicate adjective the natural construal. lakṣaṇena is instrumental singular and eva strengthens or restricts it: “by/through the defining mark precisely.”

**J2. aparaḥ is a second substantivized masculine nominative subject parallel to prathamaḥ; punaḥ is an indeclinable discourse/adverbial particle, not part of a nominal compound.**
- chosen: aparaḥ is “the other/latter,” with punaḥ marking “again/in turn.” (depends on commentary: no)
- trbh []: `` — Grammatical reasoning: aparaḥ is masculine nominative singular, parallel to prathamaḥ. punar/punaḥ is indeclinable and therefore most naturally modifies the clause as “again, in turn.”

**J3. na svayaṃbhāvaḥ etasya is read as an existentially negated nominal clause; etasya is genitive dependent on svayaṃbhāvaḥ, and iti marks this preceding clause as the explanatory formulation.**
- chosen: “There is no self-arising/self-being of this.” (depends on commentary: no)
- trbh []: `` — Grammatical reasoning: na plus a nominative noun can express non-existence, “there is no X.” etasya is genitive singular and fits as a dependent genitive, “of this.” iti commonly marks the immediately preceding expression as quoted or explanatory.

**J4. aparā niḥsvabhāvatā is a feminine nominative phrase; niḥsvabhāvatā is one abstract noun, not niḥsvabhāva plus an independent tā.**
- chosen: “another absence of own-being (niḥsvabhāvatā).” (depends on commentary: no)
- trbh []: `` — Grammatical reasoning: aparā is feminine nominative singular and agrees with niḥsvabhāvatā. The ending -tā is the regular abstract-forming suffix, giving “-ness/absence,” while an independent word tā would leave aparā without a coherent head noun.

## Translation

> The first is without own-being (niḥsvabhāva)
precisely by its defining mark (lakṣaṇa);
the other, again: “this has no self-arising (svayaṃbhāva)”—
that is another absence of own-being (niḥsvabhāvatā).

## Analyzer disagreements

- ByT5 segmented niḥsvabhāva_tā and analyzed tā as an independent feminine nominative singular item. I treat niḥsvabhāvatā as one abstract feminine nominative singular noun formed with the -tā suffix; aparā agrees with this single noun, and an independent tā does not fit the syntax here.
- ByT5 gives svayambhāva as lemma. I normalize lemma and surface to the supplied bhāṣya-reading orthography svayaṃbhāva; this is an orthographic normalization, not a different case/number/gender analysis.
- ByT5’s segmentation gives punar. Since the verse has pāda-final punaḥ, I record surface and surface_in_sandhi as punaḥ while retaining punar as the lemma.

## One-shot delta

- A dictionary-only rendering could wrongly take niḥsvabhāvaḥ as the MW masculine noun “poverty/lack of property” rather than as the predicate adjective “without svabhāva/own-being.”
- A tagger-led rendering could split niḥsvabhāvatā into niḥsvabhāva + tā and produce an impossible separate “tā,” instead of the abstract noun in -tā.
- A commentary-blind reading cannot securely identify from this verse alone which doctrinally enumerated “first” and “other” natures are meant; the translation therefore keeps “the first” and “the other/latter” rather than naming them.
- The form svayaṃbhāvaḥ is easily blurred with svabhāvaḥ; the translation preserves the svayam element by rendering it “self-arising/self-being.”

## Open questions

- Without commentary, the precise doctrinal antecedents of prathamaḥ and aparaḥ remain underdetermined by the verse alone.
- The exact technical nuance of svayaṃbhāva—whether best rendered “self-arising,” “self-production,” or more generally “self-being”—cannot be fixed by grammar and the supplied dictionary alone.
