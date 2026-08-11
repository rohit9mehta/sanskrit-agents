# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.19 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 16 pass / 0 fail / 2 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| yaḥ | yad | Pum. Prathama/Eka | pass |
| enam | etad | Pum. Dvitiya/Eka | unsupported |
| vetti | vid | vid, Kartari/Lat/Prathama/Eka | pass |
| hantāram | hantṛ | Pum. Dvitiya/Eka | pass |
| yaḥ | yad | Pum. Prathama/Eka | pass |
| ca | ca | indecl. | pass |
| enam | etad | Pum. Dvitiya/Eka | unsupported |
| manyate | man | man, Kartari/Lat/Prathama/Eka | pass |
| hatam | hata | Pum. Dvitiya/Eka | pass |
| ubhau | ubha | Pum. Prathama/Dvi | pass |
| tau | tad | Pum. Prathama/Dvi | pass |
| na | na | indecl. | pass |
| vijānītaḥ | jñā | vi-jñā, Kartari/Lat/Prathama/Dvi | pass |
| na | na | indecl. | pass |
| ayam | idam | Pum. Prathama/Eka | pass |
| hanti | han | han, Kartari/Lat/Prathama/Eka | pass |
| na | na | indecl. | pass |
| hanyate | han | han, Karmani/Lat/Prathama/Eka | pass |

## Justifications

**J1. Translate the object as ‘this embodied self (dehin/ātman)’ and the later subject as ‘this self.’**
- chosen: enam/ayam refer to the embodied self, the ātman, not to the physical body as such. (depends on commentary: **yes**)
- gita [1]: `ya enaṃ prakṛtaṃ dehinaṃ vetti vijānāti` — ‘Who knows this, the embodied one under discussion.’
- gita [2]: `tau ubhau na vijānītaḥ na jñātavantau avivekena ātmānam` — ‘Those two both do not know—have not known, through non-discrimination—the self.’
- gita [4]: `yasmāt na ayam atmā hanti` — ‘Because this self does not kill’ (the plaintext prints atmā, understood as ātmā).

**J2. Render ya enaṃ vetti hantāram as ‘whoever takes this self to be the slayer’ and yaś cainaṃ manyate hatam as ‘whoever thinks this self slain.’**
- chosen: hantāram is a predicative accusative meaning the agent of the killing-action; hatam is the corresponding patient/object of that action. (depends on commentary: **yes**)
- gita [1]: `ya enaṃ prakṛtaṃ dehinaṃ vetti vijānāti hantāraṃ hanana-kriyāyāḥ kartāraṃ ya ca enam anyo manyate hataṃ deha-hananena hato 'ham iti hanana-kriyāyāḥ karma-bhūtam` — ‘Who knows this embodied one under discussion, i.e. knows it as the killer, the agent of the act of killing; and another who thinks this to be killed—“I am killed” by the killing of the body—as become the object of the act of killing.’
- gita [4]: `na ayam atmā hanti na hanana-kriyāyāḥ kartā bhavati, na ca hanyate na ca karma bhavatīty arthaḥ` — ‘This self does not kill, does not become the agent of the act of killing; nor is it killed, nor does it become the object.’

**J3. Translate ubhau tau na vijānītaḥ as ‘both of those two do not understand,’ not as a mere absence of information about killing.**
- chosen: na vijānītaḥ means that the two do not truly know the self’s nature. (depends on commentary: **yes**)
- gita [2]: `tau ubhau na vijānītaḥ na jñātavantau avivekena ātmānam` — ‘Those two both do not know—have not known, through non-discrimination—the self.’
- gita [3]: `hantā ahaṃ, hato 'smy aham iti deha-hananena ātmānam ahaṃ pratyaya-viṣayaṃ yau vijānītaḥ tau ātma-svarūpānabhijñau ity arthaḥ` — ‘Those two who know the self, the object of the “I”-notion, as “I am the killer” or “I am killed” through the killing of the body are ignorant of the self’s own nature—this is the meaning.’

**J4. Use a colon/causal sense in translation: their view is ignorance, for this self neither slays nor is slain.**
- chosen: The last half states the reason: the self neither acts as killer nor undergoes being killed, because it is changeless. (depends on commentary: **yes**)
- gita [4]: `yasmāt na ayam atmā hanti na hanana-kriyāyāḥ kartā bhavati, na ca hanyate na ca karma bhavatīty arthaḥ, avikriyatvāt` — ‘Because this self does not kill, does not become the agent of the act of killing; nor is it killed, nor does it become the object—because of being changeless.’

**J5. Render ubhau tau explicitly as ‘both of those two.’**
- chosen: ubhau tau resumes the two relative clauses, the one who takes the self as killer and the one who takes it as killed. (depends on commentary: **yes**)
- gita [2]: `tau ubhau na vijānītaḥ` — ‘Those two both do not know.’
- gita [3]: `yau vijānītaḥ tau ātma-svarūpānabhijñau` — ‘The two who so know are ignorant of the self’s own nature.’

## Translation

> Whoever takes this embodied self (dehin/ātman) to be the slayer,
and whoever thinks this self slain—
both of those two do not understand:
this self neither slays nor is slain.

## Analyzer disagreements

- enam (both occurrences): ByT5 tags lemma enad; I revise to etad because the verifier rejects enad as a stem, deriving enadam. The syntactic role and referent are unchanged: masculine accusative singular referring to the self under discussion.
- ubhau: the analyzer gave lemma ubh; I record the nominal/pronominal stem ubha, masculine nominative dual, since it agrees with tau and refers to the two masculine yaḥ-subjects.
- vijānītaḥ: the analyzer’s prefixed lemma vijñā is decomposed as required into bare root jñā with prefix vi; tense/person/number are otherwise retained.
- hatam: the analyzer lemmatized the form to root han as a participial form; for a nominal word-analysis I record the actual participial stem hata, masculine accusative singular.

## One-shot delta

- Without the bhāṣya one might take enam as the body or a person in general; Śaṅkara identifies it as the dehin/ātman under discussion.
- A commentary-blind version might render vetti as straightforward true knowledge (‘knows him to be the killer’), whereas Śaṅkara says both cognizers are avivekin and ignorant of the self’s nature.
- One might miss the agent/patient analysis: hantāram is ‘agent of the killing-action’ and hatam/hanyate is ‘object/patient of that action,’ both explicitly denied of the self.
- One might translate the last half as merely another assertion; Śaṅkara marks it with yasmāt and explains it through avikriyatva, making it the reason the two views are ignorance.

## Open questions

- Line 4 prints atmā; I have treated this as ātmā, a likely plaintext or editional typo, because the same commentarial explanation uses ātmānam in lines 2–3 and ātmeti in line 5.
