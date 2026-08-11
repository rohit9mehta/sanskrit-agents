# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.43 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 6 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| kāmātmānaḥ | kāmātman | Pum. Prathama/Bahu; bahuvrihi ⟨kāma ātmā svabhāvo yeṣāṃ te⟩ | pass |
| svarga-parāḥ | svarga-para | Pum. Prathama/Bahu; bahuvrihi ⟨svargaḥ paraḥ puruṣārtho yeṣāṃ te⟩ | pass |
| janma-karma-phala-pradām | janma-karma-phala-pradā | Stri. Dvitiya/Eka; tatpurusa ⟨karmaṇaḥ phalaṃ karma-phalam; janma eva karma-phalaṃ; tat pradadāti iti⟩ | pass |
| kriyā-viśeṣa-bahulām | kriyā-viśeṣa-bahulā | Stri. Dvitiya/Eka; bahuvrihi ⟨kriyāṇāṃ viśeṣā bahulā yasyāṃ vāci sā⟩ | pass |
| bhogaiśvarya-gatim | bhogaiśvarya-gati | Stri. Dvitiya/Eka; tatpurusa ⟨bhogaś ca aiśvaryaṃ ca bhogaiśvarye; tayor gatiḥ prāptiḥ⟩ | pass |
| prati | prati | indecl. | pass |

## Justifications

**J1. The compound is read as a bahuvrīhi describing the speakers: their nature is desire, or desire is their chief concern.**
- chosen: kāmātmānaḥ = ‘desire-natured,’ not merely ‘having selves of desire’ in a literal sense. (depends on commentary: **yes**)
- gita [1]: `kāmātmānaḥ kāmasvabhāvāḥ, kāmaparā ity arthaḥ |` — ‘kāmātmānaḥ’ means ‘having desire as their nature’; the sense is ‘intent on desire.’

**J2. The compound is a bahuvrīhi: heaven is para/puruṣārtha for them, hence they are heaven-dominant.**
- chosen: svarga-parāḥ = ‘those for whom heaven is the supreme human goal.’ (depends on commentary: **yes**)
- gita [2]: `svarga-parāḥ svargaḥ paraḥ puruṣārthaḥ yeṣāṃ te svarga-parāḥ svarga-pradhānāḥ |` — ‘svarga-parāḥ’: those for whom heaven is the supreme human goal; they are heaven-dominant.

**J3. Śaṅkara supplies vācam as the qualified noun and parses the compound so that birth itself is the fruit of action, which the speech gives/promises.**
- chosen: janma-karma-phala-pradām qualifies the understood vācam and means ‘granting birth as the fruit of karma/action.’ (depends on commentary: **yes**)
- gita [3]: `janma-karma-phala-pradāṃ karmaṇaḥ phalaṃ karma-phalaṃ janmaiva karma-phalaṃ janma-karma-phalaṃ tat pradadātīti janma-karma-phala-pradā, tāṃ vācam |` — ‘janma-karma-phala-pradā’: the fruit of action is karma-phala; birth itself is the fruit of action, janma-karma-phala; that which gives it is janma-karma-phala-pradā—namely that speech.
- gita [4]: `pravadanti ity anuṣajyate |` — The verb ‘they proclaim’ is to be supplied.

**J4. The outer compound is bahuvrīhi qualifying the understood speech: in that speech, many particular ritual actions are set forth, especially for aims such as heaven, cattle, and sons.**
- chosen: kriyā-viśeṣa-bahulām = ‘abounding in special ritual acts/details.’ (depends on commentary: **yes**)
- gita [5]: `kriyā-viśeṣa-bahulāṃ kriyāṇāṃ viśeṣāḥ kriyā-viśeṣāḥ te bahulā yasyāṃ vāci tāṃ svarga-paśu-putrādy-arthāḥ yayā vācā bāhulyena prakāśyante |` — ‘kriyā-viśeṣa-bahulām’: the special forms of rites are kriyā-viśeṣāḥ; that speech in which they are numerous, by which aims such as heaven, cattle, and sons are abundantly displayed.

**J5. Śaṅkara defines gati here as prāpti, ‘attainment,’ and construes the ritual particulars as means to enjoyment and aiśvarya.**
- chosen: bhogaiśvarya-gatim prati = ‘toward/for the attainment of enjoyment and lordly power.’ (depends on commentary: **yes**)
- gita [6]: `bhogaiśvarya-gatiṃ prati bhogaś ca aiśvaryaṃ ca bhogaiśvarye, tayor gatiḥ prāptiḥ bhogaiśvarya-gatiḥ, tāṃ prati sādhana-bhūtāḥ ye kriyā-viśeṣāḥ tad-bahulāṃ tāṃ vācaṃ pravadantaḥ mūḍhāḥ saṃsāre parivartante ity abhiprāyaḥ ||bhgs_2.43||` — Regarding ‘bhogaiśvarya-gati’: enjoyment and lordly power are bhogaiśvarya; their gati is attainment. The special rites are means toward that; proclaiming that speech full of them, fools revolve in saṃsāra—such is the intention.

**J6. This unit is not a complete sentence by itself; the commentary explicitly says pravadanti is supplied and repeatedly identifies the accusative adjectives as qualifying vācam.**
- chosen: The finite verb ‘they proclaim’ and object ‘speech’ are syntactically carried over from 2.42. (depends on commentary: **yes**)
- gita [3, 4, 6]: `tāṃ vācam | pravadanti ity anuṣajyate | ... tāṃ vācaṃ pravadantaḥ` — ‘That speech’; ‘they proclaim’ is to be supplied; ‘proclaiming that speech.’

## Translation

> Desire-natured, with heaven as their highest goal, [they proclaim] that speech
which grants rebirth as the fruit of action,
abounding in special ritual acts,
for the attainment of enjoyment and lordly power.

## Analyzer disagreements

- Rejected the api_seg reading svarga_pare; the local analysis has svarga_parāḥ, and Śaṅkara explicitly reads svarga-parāḥ in line 2.
- For janma-karma-phala-pradām, ByT5 gives the lexical final-member base prada; for the lemma field I record the checkable feminine whole-compound stem janma-karma-phala-pradā, while retaining prada as the compound member stem.
- For kriyā-viśeṣa-bahulām, ByT5 gives the lexical final-member base bahula; for the lemma field I record the checkable feminine whole-compound stem kriyā-viśeṣa-bahulā, while retaining bahula as the compound member stem.

## One-shot delta

- Without Śaṅkara, janma-karma-phala-pradām might be taken as ‘giving birth, action, and fruit’ or ‘giving the fruits of birth and action’; the commentary instead makes birth itself the fruit of karma/action.
- A commentary-blind reading might treat kriyā-viśeṣa-bahulām as merely ‘full of varied activity’; Śaṅkara anchors it in numerous ritual particulars aimed at heaven, cattle, sons, and similar ends.
- One might translate bhogaiśvarya-gati as a ‘path of enjoyment and sovereignty’; Śaṅkara glosses gati as prāpti, ‘attainment.’
- The half-verse could be mistranslated as an independent sentence; Śaṅkara explicitly carries over vācam and pravadanti from the preceding verse.
