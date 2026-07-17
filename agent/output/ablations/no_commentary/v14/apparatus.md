# Triṃśikā v.14 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 15 pass / 0 fail / 0 unsupported.

## Verse

> **vikṣepo 'saṃprajanyañ ca kaukṛtyaṃ middham eva ca | vitarkaś ca vicāraś cety upakleśā dvaye dvidhā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| vikṣepaḥ | vikṣepa | Pum. Prathama/Eka | pass |
| asaṃprajanyam | asaṃprajanya | Napumsaka. Prathama/Eka; tatpurusa ⟨na saṃprajanyam; saṃprajanyasyābhāvaḥ⟩ | pass |
| ca | ca | indecl. | pass |
| kaukṛtyam | kaukṛtya | Napumsaka. Prathama/Eka | pass |
| middham | middha | Napumsaka. Prathama/Eka | pass |
| eva | eva | indecl. | pass |
| ca | ca | indecl. | pass |
| vitarkaḥ | vitarka | Pum. Prathama/Eka | pass |
| ca | ca | indecl. | pass |
| vicāraḥ | vicāra | Pum. Prathama/Eka | pass |
| ca | ca | indecl. | pass |
| iti | iti | indecl. | pass |
| upakleśāḥ | upakleśa | Pum. Prathama/Bahu | pass |
| dvaye | dvaya | Napumsaka. Saptami/Eka | pass |
| dvidhā | dvidhā | indecl. | pass |

## Justifications

**J1. The verse’s sandhi vikṣepo 'saṃprajanyañ ca is analyzed as vikṣepaḥ + asaṃprajanyam + ca. The avagraha marks loss of the initial a- of asaṃprajanyam after vikṣepaḥ > vikṣepo; the final -m of asaṃprajanyam is printed as ñ before palatal ca.**
- chosen: vikṣepaḥ asaṃprajanyam ca, not vikṣepaḥ ca with asaṃprajanyam omitted (depends on commentary: no)
- trbh []: `vikṣepo 'saṃprajanyañ ca` — ‘Distraction and non-clear awareness’—with ca following asaṃprajanyam.

**J2. The masculine items have nominative singular -aḥ, while the neuter items in -am are taken as nominative singular, not accusative, because the list is closed by iti and no finite transitive verb governs an accusative. Upakleśāḥ is nominative plural and supplies the classification.**
- chosen: The listed items are nominative terms, with upakleśāḥ as predicate nominative plural. (depends on commentary: no)
- trbh []: `vikṣepo 'saṃprajanyañ ca kaukṛtyaṃ middham eva ca | vitarkaś ca vicāraś cety upakleśā` — ‘Distraction, non-clear awareness, remorse, torpor, supposition, and investigation—these are subsidiary afflictions.’

**J3. The analyzer’s locative-singular analysis is grammatically possible for dvaye. Since upakleśāḥ is masculine nominative plural, dvaye does not agree with it; I therefore construe dvaye adverbially/substantivally, ‘in the pair/twofold set’. The form could also be neuter nominative/accusative dual ‘two pairs’, but this cannot be settled from grammar and dictionary alone.**
- chosen: dvaye as locative singular of neuter dvaya; dvidhā as indeclinable ‘twofold/in two ways’. (depends on commentary: no)
- trbh []: `upakleśā dvaye dvidhā` — ‘subsidiary afflictions, in the pair/twofold set, twofold.’

**J4. These English equivalents follow the supplied dictionary senses where available: vikṣepa as scattering/dispersion, kaukṛtya as repentance, middha as sloth, vitarka as conjecture/supposition, vicāra as examination/investigation, and upakleśa as a lesser kleśa. Asaṃprajanya is analyzed by privative a- plus saṃprajanya.**
- chosen: Lexical renderings: vikṣepa ‘distraction/dispersion’, asaṃprajanya ‘non-clear awareness’, kaukṛtya ‘remorse’, middha ‘torpor/sloth’, vitarka ‘supposition’, vicāra ‘investigation’, upakleśa ‘subsidiary affliction’. (depends on commentary: no)
- trbh []: `vikṣepo 'saṃprajanyañ ca kaukṛtyaṃ middham eva ca | vitarkaś ca vicāraś cety upakleśā` — The list names mental factors classified as upakleśas.

**J5. The printed cety is best segmented as ca + iti before upakleśāḥ: ca iti first contracts to ceti, and the final i of iti forms y before the following u-. Thus iti marks the preceding series as a cited/enumerated set.**
- chosen: cety = ca iti, with iti closing the list. (depends on commentary: no)
- trbh []: `vicāraś cety upakleśā` — ‘and investigation—thus: subsidiary afflictions.’

## Translation

> Distraction (vikṣepa), non-clear awareness (asaṃprajanya),
remorse (kaukṛtya), and torpor (middha) too;
supposition (vitarka) and investigation (vicāra)—
these are subsidiary afflictions (upakleśa), twofold in the pair.

## Analyzer disagreements

- The ByT5 segmentation omits asaṃprajanyam and instead gives vikṣepaḥ_ca; the verse text reads vikṣepo 'saṃprajanyañ ca, so I restore asaṃprajanyam and place ca after it.
- The bhāṣya reading has asaṃprajanyañ ca rather than the vulgate asaṃprajanyaṃ ca; I analyze the pausal form as asaṃprajanyam with sandhi/orthographic ñ before ca.
- For the fused cety, I segment the underlying words as ca + iti, assigning the printed fragments c and ety in surface_in_sandhi.

## One-shot delta

- Without commentary, the referent of dvaye remains uncertain: it may be read as locative singular ‘in the pair/twofold set’ or as neuter dual ‘two pairs’.
- A commentary-blind translation may classify all six listed factors uniformly as upakleśas, although broader Yogācāra doctrinal context could require a more nuanced grouping.
- The tagger-blind-to-text segmentation would miss asaṃprajanya entirely and incorrectly put ca immediately after vikṣepaḥ.

## Open questions

- What exactly dvaye refers to is not decidable from the verse grammar and dictionary alone.
- Whether kaukṛtya, middha, vitarka, and vicāra should be grouped separately from vikṣepa and asaṃprajanya requires contextual or commentarial evidence not available in this run.
- The technical nuance of asaṃprajanya is inferred from privative morphology rather than supplied dictionary evidence.
