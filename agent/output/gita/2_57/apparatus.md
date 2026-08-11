# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.57 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 14 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| yaḥ | yad | Pum. Prathama/Eka | pass |
| sarvatra | sarvatra | indecl. | pass |
| anabhisnehaḥ | anabhisneha | Pum. Prathama/Eka; bahuvrihi ⟨na vidyamānaḥ abhisnehaḥ yasya saḥ⟩ | pass |
| tat | tad | Napumsaka. Dvitiya/Eka | pass |
| tat | tad | Napumsaka. Dvitiya/Eka | pass |
| prāpya | āp | indecl. | pass |
| śubhāśubham | śubhāśubha | Napumsaka. Dvitiya/Eka; dvandva ⟨śubham aśubhaṃ vā⟩ | pass |
| na | na | indecl. | pass |
| abhinandati | nand | abhi-nand, Kartari/Lat/Prathama/Eka | pass |
| na | na | indecl. | pass |
| dveṣṭi | dviṣ | dviṣ, Kartari/Lat/Prathama/Eka | pass |
| tasya | tad | Pum. Sasthi/Eka | pass |
| prajñā | prajñā | Stri. Prathama/Eka | pass |
| pratiṣṭhitā | pratiṣṭhita | Stri. Prathama/Eka | pass |

## Justifications

**J1. sarvatra sets the range of anabhisnehaḥ broadly, and anabhisnehaḥ is not mere coldness but absence of abhisneha/attachment. Śaṅkara explicitly includes deha-jīvita-ādi, ‘body, life, etc.’**
- chosen: ‘without clinging everywhere,’ including even body and life (depends on commentary: **yes**)
- gita [1]: `yaḥ muniḥ sarvatra deha-jīvitādiṣv api anabhisneho 'bhisneha-varjitas` — ‘The sage who, everywhere, even with regard to body, life, and the like, is anabhisneha—devoid of attachment.’

**J2. tat tat is taken distributively with śubhāśubham as the object-range of prāpya; prāpya is explained as labdhvā, ‘having obtained,’ and śubhāśubham is resolved as śubham aśubham vā, ‘good or bad.’**
- chosen: ‘having obtained this or that—good or bad’ (depends on commentary: **yes**)
- gita [1]: `tat tat prāpya śubhāśubhaṃ tat tat śubhaṃ aśubhaṃ vā labdhvā` — ‘Having reached/obtained that and that, good-or-bad: having obtained this or that good thing or bad thing.’

**J3. abhinandati is construed as emotional delight/exultation, not greeting or verbal praise; dveṣṭi is the adverse reaction to aśubha. Śaṅkara maps them to not being pleased/exultant on obtaining good and not hating on obtaining bad.**
- chosen: ‘neither rejoices nor hates’ (depends on commentary: **yes**)
- gita [1]: `nābhinandati na dveṣṭi śubhaṃ prāpya na tuṣyati na hṛṣyati, aśubhaṃ ca prāpya na dveṣṭi ity arthaḥ` — ‘He does not rejoice and does not hate: on obtaining good he is not pleased, does not exult; and on obtaining bad he does not hate—this is the meaning.’

**J4. tasya is the genitive correlative of yaḥ; prajñā is the subject, pratiṣṭhitā the predicate, with ‘is/becomes’ supplied. Śaṅkara further characterizes the person as free from joy and sorrow and the wisdom as vivekajā, born of discrimination.**
- chosen: ‘that one’s discrimination-born wisdom is established’ (depends on commentary: **yes**)
- gita [2]: `tasya evaṃ harṣa-viṣāda-varjitasya vivekajā prajñā pratiṣṭhitā bhavati` — ‘Of that one, thus free from joy and sorrow, the wisdom born of discrimination becomes established.’

## Translation

> The sage who, everywhere, is without clinging (anabhisneha),
who, having obtained this or that—good or bad—
neither rejoices nor hates:
that one’s discrimination-born wisdom (prajñā) is established.

## Analyzer disagreements

- prāpya was tagged with lemma prāp; per the instruction to give bare verbal roots without prefixes, it is analyzed as √āp with prefix pra, an indeclinable absolutive rather than a finite verb.
- śubhāśubham was split by the analyzer as śubha_Cp + aśubham; it is analyzed here as one neuter accusative singular dvandva compound stem śubhāśubha, supported semantically by Śaṅkara’s gloss śubhaṃ aśubhaṃ vā.
- abhinandati was tagged with lemma abhinand; per the instruction to give bare roots without prefixes, it is analyzed as √nand with prefix abhi.
- pratiṣṭhitā was lemmatized by the analyzer as pratiṣṭhā; the form is feminine nominative singular of the participial stem pratiṣṭhita, not the noun pratiṣṭhā.

## One-shot delta

- A commentary-blind translation might render anabhisnehaḥ as mere emotional coldness; Śaṅkara makes it absence of clinging even toward body and life.
- It might take abhinandati in the lexical sense ‘praise/congratulate’; Śaṅkara’s gloss requires ‘be pleased, exult’ at śubha.
- It might flatten śubhāśubham into an abstract ‘good and evil’; Śaṅkara treats it as each encountered good-or-bad item.
- It might miss the supplied bhavati and the qualification vivekajā, so that prajñā pratiṣṭhitā becomes only ‘knowledge fixed’ rather than ‘discrimination-born wisdom is established.’
