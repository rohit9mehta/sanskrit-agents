# Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904) — 1.28 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 2 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| tajjapaḥ | tajjapa | Pum. Prathama/Eka; tatpurusa ⟨tasya (praṇavasya) japaḥ⟩ | pass |
| tadarthabhāvanam | tadarthabhāvana | Napumsaka. Prathama/Eka; tatpurusa ⟨tasya (praṇavasya) arthaḥ tadarthaḥ; tadarthasya (praṇavābhidheyasya īśvarasya) bhāvanam⟩ | pass |

## Justifications

**J1. The first tad is not a vague “that” nor directly Īśvara; Vyāsa glosses it as praṇava. The compound is therefore a genitive tatpuruṣa, “repetition of praṇava.”**
- chosen: tajjapaḥ = praṇavasya japaḥ, “repetition of that praṇava.” (depends on commentary: **yes**)
- ys [1]: `praṇavasya japaḥ` — the repetition of praṇava

**J2. The word artha is taken as “meaning, referent,” not as “purpose” or “benefit.” Vyāsa identifies that artha with Īśvara as the abhidheya, the entity denoted by praṇava.**
- chosen: tadartha = the referent/signified of praṇava, namely Īśvara. (depends on commentary: **yes**)
- ys [1]: `praṇavābhidheyasya ceśvarasya` — and of Īśvara, the one denoted by praṇava

**J3. The head bhāvanam is a noun of contemplation/mental cultivation, with the tadartha as its object. Vyāsa’s gloss makes the object of contemplation Īśvara, not the phonetic syllable alone. The supplied line prints final bhāvana; I use it as a nominal semantic gloss, while retaining the sūtra’s inflected bhāvanam in the analysis.**
- chosen: tadarthabhāvanam = contemplation of that referent, Īśvara. (depends on commentary: **yes**)
- ys [1]: `praṇavābhidheyasya ceśvarasya bhāvana` — the contemplation of Īśvara, the one denoted by praṇava

**J4. The sūtra has no finite verb; tajjapaḥ is unambiguously nominative singular, so the neuter tadarthabhāvanam is construed as nominative singular in a nominal coordination rather than as an accusative governed by an unexpressed verb.**
- chosen: Two coordinated practice-nouns: tajjapaḥ and tadarthabhāvanam. (depends on commentary: no)

## Translation

> Repetition (japa) of that [praṇava], and contemplation (bhāvana) of its meaning—the Īśvara denoted by praṇava.

## Analyzer disagreements

- For tadarthabhāvanam, the ByT5 output gives bhāvanam_bhāvanā_SNNe. I take the full compound stem as tadarthabhāvana, not an ā-stem bhāvanā, because the sūtra form -am requires a neuter -a stem if nominative/accusative singular; the commentary supports the sense of bhāvana but not an ā-stem inflection.
- The ByT5 segmentation lists compound components separately; the apparatus analyzes the two inflected sūtra-words as whole compound subantas, as required for compound stems.

## One-shot delta

- A commentary-blind rendering might take tajjapaḥ as “repetition of him/that” and miss Vyāsa’s specification that what is repeated is praṇava.
- It might translate tadartha as “for that purpose” or “the benefit of that,” whereas Vyāsa takes it as the abhidheya, the signified referent, Īśvara.
- It might collapse the sūtra into “meaningful recitation,” rather than two coordinated practices: japa and bhāvana.

## Open questions

- The supplied commentary line ends with bhāvana rather than the sūtra’s bhāvanam or the expected feminine bhāvanā; I have treated this as a semantic nominal gloss and not as decisive evidence for the sūtra-word’s inflection.
