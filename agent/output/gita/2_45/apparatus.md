# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.45 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 9 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| traiguṇya-viṣayāḥ | traiguṇya-viṣaya | Pum. Prathama/Bahu; bahuvrihi ⟨traiguṇyaṃ viṣayaḥ prakāśayitavyaḥ yeṣāṃ te⟩ | pass |
| vedāḥ | veda | Pum. Prathama/Bahu | pass |
| nistraiguṇyaḥ | nistraiguṇya | Pum. Prathama/Eka; tatpurusa ⟨traiguṇyāt nirgataḥ; niṣkāmaḥ⟩ | pass |
| bhava | bhū | bhū, Kartari/Lot/Madhyama/Eka | pass |
| arjuna | arjuna | Pum. Sambodhana/Eka | pass |
| nirdvandvaḥ | nirdvandva | Pum. Prathama/Eka; tatpurusa ⟨dvandvāt nirgataḥ⟩ | pass |
| nitya-sattva-sthaḥ | nitya-sattva-stha | Pum. Prathama/Eka; tatpurusa ⟨nityaṃ sattva-guṇe sthaḥ; sadā sattva-guṇāśritaḥ⟩ | pass |
| niryoga-kṣemaḥ | niryoga-kṣema | Pum. Prathama/Eka; tatpurusa ⟨yoga-kṣemābhyāṃ nirgataḥ⟩ | pass |
| ātmavān | ātmavant | Pum. Prathama/Eka | pass |

## Justifications

**J1. The compound is taken as a bahuvrīhi qualifying vedāḥ, not as a mere karmadhāraya 'three-guṇa subjects' nor as an abstract 'Vedas are objects of traiguṇya.'**
- chosen: traiguṇya-viṣayāḥ = Vedas whose subject to be revealed is traiguṇya, glossed as saṃsāra. (depends on commentary: **yes**)
- gita [1]: `traiguṇya-viṣayāḥ traiguṇyaṃ saṃsāro viṣayaḥ prakāśayitavyaḥ yeṣāṃ te vedāḥ traiguṇya-viṣayāḥ |` — “Traiguṇya-subject”: traiguṇya, namely saṃsāra, is the subject to be made manifest for them; those Vedas are traiguṇya-viṣayāḥ.

**J2. Śaṅkara does not let the imperative mean only metaphysical absence of the three guṇas; he glosses its intended sense here as niṣkāmaḥ, free from desire.**
- chosen: nistraiguṇyaḥ is rendered practically as 'free from the three-guṇa sphere—desireless.' (depends on commentary: **yes**)
- gita [2]: `tvaṃ tu nistraiguṇyo bhava arjuna, niṣkāmo bhava ity arthaḥ |` — But you, Arjuna, be nistraiguṇya; the meaning is: be desireless.

**J3. The commentary specifies dvandva as opposed objects connected with pleasure and pain, and explains nir- as being gone out from them.**
- chosen: nirdvandvaḥ = free from opposed pairs that cause pleasure and pain. (depends on commentary: **yes**)
- gita [3]: `nirdvandvaḥ sukha-duḥkha-hetū sa-pratipakṣau padārthau dvandva-śabda-vācyau |` — The two objects that are causes of pleasure and pain, together with their opposites, are denoted by the word dvandva.
- gita [4]: `tataḥ nirgataḥ nirdvandvo bhava |` — Having gone out from those, be nirdvandva.

**J4. Sattva is construed as sattva-guṇa, and nitya as sadā, 'always'; not as 'eternal being' or an ontological absolute.**
- chosen: nitya-sattva-sthaḥ = always established in the sattva-quality. (depends on commentary: **yes**)
- gita [5]: `nitya-sattva-sthaḥ sadā sattva-guṇāśrito bhava |` — Be nitya-sattva-stha: always resorting to the sattva-guṇa.

**J5. The commentary defines yoga as acquiring what has not been acquired and kṣema as protecting what has been acquired; it further says that one for whom yoga-kṣema is primary has difficulty entering the good, hence the verse enjoins freedom from it.**
- chosen: niryoga-kṣemaḥ = free from concern for acquisition and safeguarding. (depends on commentary: **yes**)
- gita [6]: `tathā niryoga-kṣemo 'nupāttasya upādānaṃ yogaḥ, upāttasya rakṣaṇaṃ kṣemaḥ, yoga-kṣema-pradhānasya śreyasi pravṛttir duṣkarā ity ataḥ niryoga-kṣemo bhava |` — Likewise be niryoga-kṣema: yoga is acquiring what has not been acquired, kṣema is guarding what has been acquired; because progress toward the good is difficult for one whose main concern is yoga-kṣema, therefore be niryoga-kṣema.

**J6. Rather than the literal 'having a self/soul,' Śaṅkara glosses the ethical-ascetic force as apramattaḥ, not negligent.**
- chosen: ātmavān = self-possessed, vigilant/not heedless. (depends on commentary: **yes**)
- gita [7]: `ātmavān apramattaś ca bhava |` — Be ātmavān, and not heedless.

## Translation

> The Vedas have the three-guṇa saṃsāra as their subject.
But you, Arjuna, be free of that three-guṇa sphere—desireless;
free from the opposed pairs, ever established in the sattva-quality,
free from concern for acquisition (yoga) and safeguarding (kṣema), self-possessed and vigilant.

## Analyzer disagreements

- For inflected compounds the ByT5 output gives head lemmas viṣaya, stha, and kṣema; per the requested analysis I use the whole compound stems traiguṇya-viṣaya, nitya-sattva-stha, and niryoga-kṣema.
- For niryoga-kṣemaḥ, ByT5's niryoga_Cp kṣemaḥ segmentation could suggest a compound headed simply by kṣema. Śaṅkara line 6 defines yoga and kṣema separately and treats yoga-kṣema as the concern to abandon, so I analyze the whole as nis + yoga-kṣema, 'free from acquisition and safeguarding.'
- I normalize the tagger's nirdvaṃdva spelling to the verse/commentary spelling nirdvandva; this is orthographic, not a change of grammatical features.
- I add samāsa analyses for the prefixed adjectives nistraiguṇyaḥ and nirdvandvaḥ, which ByT5 left as simple nominal stems.
- For ātmavān, ByT5 gives ātmavat_SNM; after the verifier report I record the derivational possessive stem as ātmavant for Pum/Prathama/Eka, while noting that ātmavat is the dictionary headword.

## One-shot delta

- A commentary-blind translation might make traiguṇya merely 'the three guṇas'; Śaṅkara glosses it here as saṃsāra, the three-guṇa worldly sphere that the Vedas reveal.
- It might render nistraiguṇyaḥ as only metaphysical guṇa-transcendence; Śaṅkara gives the immediate practical sense: niṣkāmaḥ, desireless.
- It might take nitya-sattva-sthaḥ as 'established in eternal being'; Śaṅkara says 'always resorting to the sattva-guṇa.'
- It might translate yoga-kṣema as 'yoga and welfare/security'; Śaṅkara defines yoga as acquisition of the unacquired and kṣema as protection of the acquired.
- It might render ātmavān literally as 'having a soul'; Śaṅkara's gloss points to vigilance or self-possession: apramattaḥ.
