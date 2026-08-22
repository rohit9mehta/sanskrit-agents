# Lemma-layer validation: stored vs re-run

Re-run model: gpt-5.6-sol (stored: gpt-5.5-2026-04-23)

| unit | overrides old→new | attempts | tokens | est $ | verify (pass/fail/unsup) |
|---|---|---|---|---|---|
| gita:2.19 | 4 → **1** | 2 → 1 | 0 → 0 | 0.3594 → 0.1782 | 16/0/2 → 16/0/2 |
| isa:4 | 2 → **9** | 2 → 2 | 0 → 0 | 0.4157 → 0.5369 | 19/0/0 → 18/1/0 |
| trimsika:10 | 5 → **4** | 2 → 1 | 0 → 0 | 0.4863 → 0.2768 | 10/0/0 → 10/0/0 |

## Remaining disagreements (new run)

### gita:2.19
- For ubhau, Vyākaraṇī gives the stem ubh. This is overridden by the supplied canonical lemma ubha; ubh is a verbal root, whereas ubhau is the masculine nominative dual of the nominal ubha.

Lemma citations that changed vs stored: enam: etad → enad

### isa:4
- Vyākaraṇī splits anejat into an + na + ejat and analyzes only ejat as an inflected nominal. The commentary’s explicit anejat na ejat and the syntax require one inflected nañ-compound, anejat, neuter nominative singular.
- Vyākaraṇī assigns ekam Dvitiya singular. Because it is predicated of the neuter subject together with anejat and javīyaḥ, it is analyzed as Prathama singular; the two cases are formally syncretic.
- Vyākaraṇī assigns manasaḥ Sasthi singular. The comparative javīyaḥ and Śaṅkara’s javavattaram establish a standard of comparison, so it is construed as Panchami singular; the forms are syncretic.
- Vyākaraṇī assigns javīyaḥ Dvitiya singular. It is a neuter Prathama singular predicate of the Self-reality; the nominative and accusative forms are syncretic.
- Vyākaraṇī treats arṣat as a neuter accusative nominal. The clause and Śaṅkara’s pūrvam eva gatam require a finite third-person singular past verb from √ṛṣ; it is represented as augmentless Lan/injunctive.
- Vyākaraṇī assigns tat Dvitiya singular. It is the Prathama singular subject of atyeti.
- Vyākaraṇī assigns dhāvataḥ Pum Sasthi Eka. Śaṅkara paraphrases it with drutaṃ gacchataḥ and construes it with accusative plural anyān, requiring Pum Dvitiya Bahu.
- Vyākaraṇī assigns tiṣṭhat Napumsaka Dvitiya Eka. It agrees with nominative tat as a circumstantial participle and is therefore Napumsaka Prathama Eka.
- Vyākaraṇī assigns apaḥ Dvitiya Eka. The form and Śaṅkara’s plural karmāṇi require Stri Dvitiya Bahu.

Lemma citations that changed vs stored: pūrvam: pūrvam → pūrva; arṣat: arṣat → ṛṣ

### trimsika:10
- For adyāḥ, Vyākaraṇī proposed a second-person singular benedictive of ad. The supplied canonical lemma adya, nominative-plural syntax, and Sthiramati’s explicit explanation ādyāḥ sarvatragā rule out that verbal parse.
- ByT5 split sparśādayaḥ into sparśa plus ādayaḥ, and Vyākaraṇī analyzed only ādayaḥ. Line 500 explicitly derives the whole bahuvrīhi sparśādayaḥ, so the adopted stem is sparśādi.
- ByT5 split chandādhimokṣasmṛtayaḥ into three members, and Vyākaraṇī analyzed only smṛtayaḥ. The commentary treats the expression as three coordinated members of a five-factor set, so the adopted lemma is the whole dvandv
- ByT5 split samādhidhībhyām into samādhi plus dhībhyām, and Vyākaraṇī assigned the latter the simple stem dhī. Its coordination under saha and the commentary’s count of five require the whole dvandva stem samādhidhī. The 

Lemma citations that changed vs stored: śraddhā: śraddha → śraddhā; apatrapā: apatrapa → apatrapā
