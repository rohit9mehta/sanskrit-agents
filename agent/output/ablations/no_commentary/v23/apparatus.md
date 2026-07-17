# Triṃśikā v.23 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 8 pass / 0 fail / 0 unsupported.

## Verse

> **trividhasya svabhāvasya trividhāṃ niḥsvabhāvatām | sandhāya sarvadharmāṇāṃ deśitā niḥsvabhāvatā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| trividhasya | trividha | Pum. Sasthi/Eka; bahuvrihi ⟨trayo vidhāḥ yasya saḥ⟩ | pass |
| svabhāvasya | svabhāva | Pum. Sasthi/Eka; tatpurusa ⟨svasya bhāvaḥ⟩ | pass |
| trividhām | trividha | Stri. Dvitiya/Eka; bahuvrihi ⟨trayo vidhāḥ yasyāḥ sā⟩ | pass |
| niḥsvabhāvatām | niḥsvabhāvatā | Stri. Dvitiya/Eka | pass |
| sandhāya | dhā | indecl. | pass |
| sarvadharmāṇām | sarvadharma | Pum. Sasthi/Bahu; karmadharaya ⟨sarve dharmāḥ⟩ | pass |
| deśitā | deśita | Stri. Prathama/Eka | pass |
| niḥsvabhāvatā | niḥsvabhāvatā | Stri. Prathama/Eka | pass |

## Justifications

**J1. trividhasya is an adjective in the genitive singular agreeing with masculine svabhāvasya, not a separate substantive genitive. The phrase supplies the genitive complement to trividhām niḥsvabhāvatām.**
- chosen: trividhasya svabhāvasya = “of the threefold nature” (depends on commentary: no)
- trbh []: `MW s.v. trividha: “mfn. of 3 kinds, triple, threefold”; MW s.v. svabhāva: “own condition or state of being ... nature.”` — Lexically and morphologically, the phrase is “of the threefold nature.”

**J2. trividhām and niḥsvabhāvatām are both feminine accusative singular, so trividhām modifies niḥsvabhāvatām. niḥsvabhāvatām is best analyzed as the accusative singular of abstract niḥsvabhāvatā, not as niḥsvabhāva plus an independent tām.**
- chosen: trividhāṃ niḥsvabhāvatām = “the threefold absence of nature” (depends on commentary: no)
- trbh []: `MW s.v. niḥsvabhāva: “mfn. ... void of peculiarities”; Sanskrit -tā forms feminine abstract nouns, with acc. sg. -tām and nom. sg. -tā.` — The form means “absence/state of being without svabhāva,” and trividhām makes that absence threefold.

**J3. The absolutive sandhāya is construed with the accusative trividhāṃ niḥsvabhāvatām. In this abstract context, a literal physical “joining” is less apt than “holding/fixing in view,” hence “having in view” or “with reference to.”**
- chosen: sandhāya = “having in view / with reference to” (depends on commentary: no)
- trbh []: `MW s.v. saṃ-√dhā: “to place or hold or put or draw or join or fasten or fix ... unite.”` — The core sense “hold/fix” supports the contextual rendering “having in view.”

**J4. sarvadharmāṇām is genitive plural and most naturally supplies the possessor/objective genitive for the nominative niḥsvabhāvatā: “the absence of nature of all dharmas.”**
- chosen: sarvadharmāṇāṃ depends on niḥsvabhāvatā (depends on commentary: no)
- trbh []: `MW s.v. sarva: “all, every”; MW s.v. dharma: “that which is established or firm ... law ... duty.”` — The compound sarvadharma is “all dharmas,” and the genitive plural gives “of all dharmas.”

**J5. deśitā is feminine nominative singular and agrees with niḥsvabhāvatā, the nominative subject. As a past passive participial predicate, it yields “has been taught / was taught.”**
- chosen: deśitā niḥsvabhāvatā = “the absence of nature has been taught” (depends on commentary: no)
- trbh []: `The endings -ā ... -tā are feminine nominative singular in deśitā niḥsvabhāvatā; the participial form deśita- functions adjectivally as “taught/pointed out.”` — The predicate construction is “the absence of nature was taught.”

## Translation

> Having in view the threefold absence of nature (niḥsvabhāvatā)
of the threefold nature (svabhāva),
the absence of nature of all dharmas
has been taught.

## Analyzer disagreements

- The analyzer splits niḥsvabhāvatām and niḥsvabhāvatā as niḥsvabhāva_Cp + tām/tā. I instead analyze each as the single abstract feminine noun-stem niḥsvabhāvatā, because -tā here is the regular abstract-forming suffix, not an independent noun/pronoun.
- The analyzer gives sandhāya with lemma saṃdhā. I normalize this to bare root √dhā with prefix sam, per the requested format for verbal derivation, while retaining its indeclinable absolutive function.
- The analyzer treats sarvadharmāṇām by segmenting sarva_Cp + dharmāṇām. I record the inflected nominal stem as the whole compound sarvadharma, as requested for inflected compounds.
- The analyzer leaves trividha unsplit. I add a compound analysis tri + vidha, taking the lexical adjective “threefold” as a bahuvrīhi-type formation; this does not change its inflectional analysis.

## One-shot delta

- A grammar-only or analyzer-led reading could wrongly split niḥsvabhāvatām/niḥsvabhāvatā into niḥsvabhāva + tām/tā instead of recognizing the abstract noun niḥsvabhāvatā.
- It could translate sandhāya too literally as “having joined,” whereas the abstract accusative favors “having in view / with reference to.”
- It could fail to keep the two “threefold” expressions aligned: trividhasya qualifies svabhāvasya, while trividhām qualifies niḥsvabhāvatām.
- Without commentary, the verse itself does not identify which three natures or which three absences of nature are meant; the translation therefore remains generic.
- It could render dharmāṇām as “laws/duties” from a general dictionary sense; preserving “dharmas” avoids over-specifying the technical sense without commentary.

## Open questions

- The verse alone does not specify the members of the “threefold nature” or the “threefold absence of nature.”
- The exact doctrinal scope of niḥsvabhāvatā cannot be fixed from the supplied grammar and dictionary alone.
- The agent of deśitā, presumably an authoritative teacher, is not expressed in the verse.
