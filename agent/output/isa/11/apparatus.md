# Īśopaniṣad (Kāṇva) with Śaṅkara-bhāṣya — 11 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 14 pass / 0 fail / 1 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| vidyām | vidyā | Stri. Dvitiya/Eka | pass |
| ca | ca | indecl. | pass |
| avidyām | avidyā | Stri. Dvitiya/Eka | pass |
| ca | ca | indecl. | pass |
| yaḥ | yad | Pum. Prathama/Eka | pass |
| tat | tad | Napumsaka. Dvitiya/Eka | pass |
| veda | vid | vid, Kartari/Lit/Prathama/Eka | unsupported |
| ubhayam | ubhaya | Napumsaka. Dvitiya/Eka | pass |
| saha | saha | indecl. | pass |
| avidyayā | avidyā | Stri. Trtiya/Eka | pass |
| mṛtyum | mṛtyu | Pum. Dvitiya/Eka | pass |
| tīrtvā | tṝ | indecl. | pass |
| vidyayā | vidyā | Stri. Trtiya/Eka | pass |
| amṛtam | amṛta | Napumsaka. Dvitiya/Eka | pass |
| aśnute | aś | aś, Kartari/Lat/Prathama/Eka | pass |

## Justifications

**J1. Technical meanings of vidyā and avidyā.**
- chosen: vidyā is ‘deity-knowledge’ (devatājñāna), and avidyā is ritual action (karma), not generic knowledge and ignorance. (depends on commentary: **yes**)
- isup [1]: `yata evamato vidyāṃ cāvidyāṃ ca devatājñānaṃ karma cetyarthaḥ /` — Therefore, since this is so, ‘knowledge and ignorance’ means deity-knowledge and action.
- isup [3]: `avidyayā karmaṇā agnihotrādinā ... vidyayā devatājñānenāmṛtaṃ devatātmabhāvamaśnute prāpnoti /` — By avidyā, by action such as the Agnihotra ... by vidyā, by deity-knowledge, he attains the immortal, the state of deity-selfhood.

**J2. Construe yas tad vedobhayaṃ saha.**
- chosen: tat and ubhayam form the accusative object ‘that pair’; saha means ‘together’, i.e. the two are known as jointly to be undertaken by one person. (depends on commentary: **yes**)
- isup [2]: `yastadetadubhayaṃ sahaikena puruṣeṇa anuṣṭheyaṃ veda tasyaivaṃ samuccayakāriṇa eva ekapuruṣārthasambandhaḥ krameṇa syādityucyate /` — He who knows this very pair together as to be performed by one person—for him alone, who thus makes the combination, connection with the one human goal would occur in sequence; this is being stated.

**J3. Force of avidyayā mṛtyuṃ tīrtvā.**
- chosen: avidyayā means ‘by ritual action such as Agnihotra’; tīrtvā means ‘having transcended’; mṛtyu is a technical ‘death’ rather than merely physical dying. (depends on commentary: **yes**)
- isup [3]: `avidyayā karmaṇā agnihotrādinā mṛtyuṃ svābhāvikaṃ karma jñānaṃ ca mṛtyuśabdavācyamubhayaṃ tīrtvā atikramya` — By avidyā, by action such as the Agnihotra, having crossed—having transcended—death: the natural action and knowledge, both denoted by the word ‘death’.

**J4. Force of vidyayāmṛtam aśnute.**
- chosen: vidyayā means ‘by deity-knowledge’; aśnute means ‘attains’; amṛtam is the deity-self state or going to deity-selfhood, not nectar or absolute liberation. (depends on commentary: **yes**)
- isup [3]: `vidyayā devatājñānenāmṛtaṃ devatātmabhāvamaśnute prāpnoti /` — By vidyā, by deity-knowledge, he attains—obtains—the immortal, the state of deity-selfhood.
- isup [4]: `taddhyamṛtamucyate yaddevatātmagamanam` — For that is called immortal which is going to deity-selfhood.

**J5. Tense/aspect of veda in English.**
- chosen: Render veda as present ‘knows’ despite its perfect morphology, because this is the normal gnomic force of this form in such relative clauses. (depends on commentary: no)

## Translation

> Knowledge (vidyā, deity-knowledge) and ignorance (avidyā, ritual action)—
whoever knows that pair together,
having crossed death—natural action and knowledge so called—by ignorance/action,
by knowledge attains the immortal: the state of deity-selfhood.

## Analyzer disagreements

- ByT5 tags veda as vid_SPs3In. I retain veda as √vid, Kartari, liṭ, Prathama, Eka: although the verifier generates regular liṭ forms such as viveda and rejects veda, this Upaniṣadic veda is the established unreduplicated perfect of √vid ‘know’ used with present meaning, so changing it to a different lakāra merely to satisfy the verifier would be false.
- ByT5 gives the absolutive root as tṛ. I normalize it to the long-vowel dhātu √tṝ ‘cross’ for tīrtvā; the commentary supports the sense by glossing tīrtvā as atikramya at line 3.

## One-shot delta

- A commentary-blind translation would likely take avidyā as simple ignorance; Śaṅkara instead glosses it as karma, specifically action such as Agnihotra.
- It might take vidyā as liberating Self-knowledge and amṛta as final mokṣa; the bhāṣya restricts them here to deity-knowledge and the deity-self state.
- It might miss the samuccaya: line 2 says the two are to be known as jointly undertaken by one person, with the result connected in sequence.
