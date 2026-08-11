# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.72 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 13 pass / 0 fail / 1 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| eṣā | etad | Stri. Prathama/Eka | pass |
| brāhmī | brāhmī | Stri. Prathama/Eka | pass |
| sthitiḥ | sthiti | Stri. Prathama/Eka | pass |
| pārtha | pārtha | Pum. Sambodhana/Eka | pass |
| na | na | indecl. | pass |
| enām | enad | Stri. Dvitiya/Eka | unsupported |
| prāpya | āp | indecl. | pass |
| vimuhyati | muh | vi-muh, Kartari/Lat/Prathama/Eka | pass |
| sthitvā | sthā | indecl. | pass |
| asyām | idam | Stri. Saptami/Eka | pass |
| anta-kāle | anta-kāla | Pum. Saptami/Eka; tatpurusa ⟨antasya kālaḥ⟩ | pass |
| api | api | indecl. | pass |
| brahma-nirvāṇam | brahma-nirvāṇa | Napumsaka. Dvitiya/Eka; tatpurusa ⟨brahmaṇi nirvāṇam⟩ | pass |
| ṛcchati | ṛch | ṛch, Kartari/Lat/Prathama/Eka | pass |

## Justifications

**J1. brāhmī sthitiḥ is not merely a generic “holy/scriptural state” or a state belonging to the deity Brahmā. Śaṅkara glosses brāhmī as brahmaṇi bhavā and defines the sthiti as abiding as Brahman itself after renouncing all karma; eṣā points back to the state just described.**
- chosen: “This is the state in Brahman (brāhmī sthitiḥ)” (depends on commentary: **yes**)
- gita [1]: `eṣā yathoktā brāhmī brahmaṇi bhavā iyaṃ sthitiḥ sarvaṃ karma saṃnyasya brahma-rūpeṇaiva avasthānam ity etat |` — “This, as described, is brāhmī—being in Brahman—this state: namely, having renounced all karma, abiding only in the form of Brahman.”

**J2. Śaṅkara explicitly supplies sthitim after enām, glosses prāpya with labdhvā, and paraphrases na vimuhyati as na mohaṃ prāpnoti. This also supports taking vimuhyati as active/intransitive rather than a passive form.**
- chosen: enām refers to the sthiti; prāpya means “having attained/obtained”; vimuhyati means “becomes deluded,” construed as attaining delusion (depends on commentary: **yes**)
- gita [2]: `he pārtha, naināṃ sthitiṃ prāpya labdhvā na vimuhyati na mohaṃ prāpnoti |` — “O Pārtha, having attained, obtained, this state, he is not deluded; he does not attain delusion.”

**J3. The locative asyām is not an abstract adverbial “therein” without antecedent; Śaṅkara makes its antecedent explicit as the brāhmī sthiti and glosses sthitvā accordingly.**
- chosen: “having abided in this [state]” (depends on commentary: **yes**)
- gita [3]: `sthitvāsyāṃ sthitau brāhmyāṃ yathoktāyāṃ anta-kāle 'pi antye vayasy api brahma-nirvāṇaṃ brahma-nirvṛtiṃ mokṣam ṛcchati gacchati |` — “Having stood in this state, the brāhmī one as described, even at the final time, even in the final age, he reaches—goes to—Brahman-nirvāṇa, Brahman-nirvṛti, liberation.”

**J4. anta-kāle ’pi is taken in relation to a person’s final stage/time of life, not as the end of the world or merely the close of a discourse. Śaṅkara’s antye vayasi and his a-fortiori comment about one who abides in Brahman for life establish the sense.**
- chosen: “even at life’s final time” (depends on commentary: **yes**)
- gita [3]: `anta-kāle 'pi antye vayasy api` — “Even at the final time, even in the final age/stage of life.”
- gita [4]: `kim u vaktavyaṃ brahmacaryād eva saṃnyasya yāvaj jīvaṃ yo brahmaṇy eva avatiṣṭhate sa brahma-nirvāṇam ṛcchati iti ||bhgs_2.72||` — “How much more need be said of one who, having renounced from the brahmacarya stage itself, abides only in Brahman for as long as he lives: he reaches Brahman-nirvāṇa.”

**J5. brahma-nirvāṇam is not to be translated as the destruction of Brahman or as an unspecified Buddhist-style extinction. Śaṅkara glosses it as brahma-nirvṛti and mokṣa, and glosses ṛcchati as gacchati, “goes/reaches.” The locative compound relation “nirvāṇa in Brahman” is further supported by line 4’s brahmaṇy eva avatiṣṭhate.**
- chosen: “reaches Brahman-nirvāṇa, liberation” (depends on commentary: **yes**)
- gita [3]: `brahma-nirvāṇaṃ brahma-nirvṛtiṃ mokṣam ṛcchati gacchati` — “He reaches—goes to—Brahman-nirvāṇa, Brahman-nirvṛti, liberation.”
- gita [4]: `yo brahmaṇy eva avatiṣṭhate sa brahma-nirvāṇam ṛcchati` — “He who abides only in Brahman reaches Brahman-nirvāṇa.”

## Translation

> This, O Pārtha, is the state in Brahman (brāhmī sthitiḥ):
having attained this, one is not bewildered.
Having abided in this even at life’s final time,
one reaches Brahman-nirvāṇa (brahma-nirvāṇam), liberation.

## Analyzer disagreements

- The api_seg output has brāhmā, but the unit text, local_S, and Śaṅkara line 1 read brāhmī; I analyze brāhmī as Stri Prathama Eka agreeing with sthitiḥ.
- ByT5 reports brāhmī with lemma brāhma; because the requested field is the nominal stem, I give the feminine stem brāhmī, while noting it is the feminine of brāhma mf(ī)n.
- ByT5 gives prāpya_prāp_Co; per the instruction to give bare roots separately from prefixes, I analyze it as pra + √āp, an absolutive/avyaya.
- ByT5 gives vimuhyati_vimuh; per the instruction to give bare roots separately from prefixes, I analyze it as vi + √muh.
- For anta-kāle and brahma-nirvāṇam, ByT5 marks a compound member plus final inflected member; I record each as a single inflected compound stem with samāsa details.

## One-shot delta

- Without Śaṅkara, brāhmī sthitiḥ might be flattened to “holy state” or misread as a condition of Brahmā; the commentary makes it the state in Brahman, abiding as Brahman after renunciation of all karma.
- A commentary-blind translation might let enām and asyām remain vague; Śaṅkara explicitly ties both pronouns to the brāhmī sthiti.
- anta-kāle ’pi might be rendered as a cosmic “end-time” or simply “at death”; Śaṅkara glosses it as the final stage/time of life and adds an a-fortiori contrast with lifelong abiding in Brahman.
- brahma-nirvāṇam could be rendered as bare “extinction”; Śaṅkara identifies it with brahma-nirvṛti and mokṣa, liberation.
