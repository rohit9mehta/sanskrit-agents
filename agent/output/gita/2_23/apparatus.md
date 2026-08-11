# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.23 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 16 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| na | na | indecl. | pass |
| enam | ena | Pum. Dvitiya/Eka | pass |
| chindanti | chid | chid, Kartari/Lat/Prathama/Bahu | pass |
| śastrāṇi | śastra | Napumsaka. Prathama/Bahu | pass |
| na | na | indecl. | pass |
| enam | ena | Pum. Dvitiya/Eka | pass |
| dahati | dah | dah, Kartari/Lat/Prathama/Eka | pass |
| pāvakaḥ | pāvaka | Pum. Prathama/Eka | pass |
| na | na | indecl. | pass |
| ca | ca | indecl. | pass |
| enam | ena | Pum. Dvitiya/Eka | pass |
| kledayanti | klid | klid, Kartari/Lat/Prathama/Bahu | pass |
| āpaḥ | ap | Stri. Prathama/Bahu | pass |
| na | na | indecl. | pass |
| śoṣayati | śuṣ | śuṣ, Kartari/Lat/Prathama/Eka | pass |
| mārutaḥ | māruta | Pum. Prathama/Eka | pass |

## Justifications

**J1. Translate the repeated enam as ‘this self,’ with the commentary’s dehin/ātman as the referent.**
- chosen: enam = the self/embodied self under discussion, not the physical body as a cuttable object (depends on commentary: **yes**)
- gita [1]: `enaṃ prakṛtaṃ dehinaṃ na chindanti śastrāṇi, niravayavatvāt nāvayava-vibhāgaṃ kurvanti |` — ‘Weapons do not cut this embodied one under discussion; because it is without parts, they do not make a division of parts.’
- gita [8]: `enaṃ tv ātmānaṃ na śoṣayati māruto 'pi ||bhgs_2.23||` — ‘But even wind does not dry this self.’

**J2. Render the first pāda as weapons’ inability to cut the partless self, not merely a general inability to injure it.**
- chosen: chindanti = divide/cut into parts; śastrāṇi = weapons such as swords (depends on commentary: **yes**)
- gita [1]: `enaṃ prakṛtaṃ dehinaṃ na chindanti śastrāṇi, niravayavatvāt nāvayava-vibhāgaṃ kurvanti |` — ‘Weapons do not cut this embodied one under discussion; because it is without parts, they do not make a division of parts.’
- gita [2]: `śastrāṇi asy-ādīni |` — ‘Weapons are swords etc.’ The printed “asy-ādīni” is likely a noisy reading for “asi-ādīni.”

**J3. Render pāvakaḥ as ‘fire’ and dahati as ‘burns,’ with Śaṅkara’s bhasmīkaroti specifying combustion rather than purification.**
- chosen: pāvakaḥ = fire; dahati = burn to ash (depends on commentary: **yes**)
- gita [3]: `tathā nainaṃ dahati pāvakaḥ, agnir api na bhasmīkaroti |` — ‘Likewise, fire does not burn this one; even Agni does not reduce it to ashes.’

**J4. Translate waters as unable to moisten the partless self; Śaṅkara explains wetting as something water can do only to a composite object by making it moist and separating its parts.**
- chosen: kledayanti = moisten/soak by making wet; āpaḥ = waters (depends on commentary: **yes**)
- gita [4, 5, 6]: `tathā na cainaṃ kledayanti āpaḥ |
apāṃ hi sāvayavasya vastuna ādrībhāva-karaṇena avayava-viśleṣāpādane sāmarthyam |
tan na niravayave ātmani saṃbhavati |` — ‘Likewise, waters do not moisten this one. For waters have the capacity, in the case of an object with parts, to cause separation of parts by producing wetness. That does not occur in the partless self.’

**J5. Render the last pāda as wind’s inability to dry the self, not as a mythological Marut’s action; Śaṅkara glosses māruta with vāyuḥ and defines the mode as drying moisture.**
- chosen: mārutaḥ = wind; śoṣayati = dry up by removing moisture (depends on commentary: **yes**)
- gita [7, 8]: `tathā snehavat dravyaṃ sneha-śoṣaṇena nāśayati vāyuḥ |
enaṃ tv ātmānaṃ na śoṣayati māruto 'pi ||bhgs_2.23||` — ‘Likewise, wind destroys an oily substance by drying up its moisture. But even wind does not dry this self.’

**J6. Keep the repeated negation in English: ‘do not cut … does not burn … nor … do not moisten … does not dry.’**
- chosen: Each na negates its own finite verb in a fourfold denial (depends on commentary: no)

## Translation

> Weapons do not cut this self (ātman);
fire does not burn this self.
Nor do waters moisten this self;
wind does not dry it.

## Analyzer disagreements

- enam (all three occurrences): ByT5 gives lemma enad; revised to the inflected pronominal stem ena because enad + Pum/Dvitiya/Eka was rejected by the verifier as deriving enadam. The case/gender/number are retained.
- kledayanti: ByT5 effectively lemmatizes as kleday; I analyze it as a causative present from the bare verbal root klid, since the form is kledaya- + anti and Śaṅkara explains the action as ādrībhāva-karaṇa, ‘making moist’ (line 5).
- śoṣayati: ByT5 effectively lemmatizes as śoṣay; I analyze it as a causative present from the bare verbal root śuṣ, since the form is śoṣaya- + ti and Śaṅkara explains it by śoṣaṇa, ‘drying’ (line 7).

## One-shot delta

- A commentary-blind translation might take enam as the visible body; Śaṅkara explicitly identifies it as the dehin/ātman, the self under discussion (lines 1, 8).
- It might render chindanti as ordinary ‘cut’ without the philosophical point that cutting means producing a division of parts; Śaṅkara makes partlessness the reason cutting is impossible (line 1).
- It might take pāvaka chiefly as ‘purifier’ or a proper name; Śaṅkara glosses it with agni and bhasmīkaroti, fire’s reducing to ashes (line 3).
- It might miss the sequence of physical modes—cutting, burning, moistening, drying—as failures to affect a partless self; Śaṅkara spells out the mechanisms for water and wind in terms of part-separation and removal of moisture (lines 5–8).

## Open questions

- The commentary line “śastrāṇi asy-ādīni” is likely an unproofread form for “śastrāṇi asi-ādīni,” ‘weapons are swords etc.’; I have not normalized the quoted evidence.
