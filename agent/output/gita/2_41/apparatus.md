# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.41 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 11 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| vyavasāyātmikā | vyavasāyātmikā | Stri. Prathama/Eka; bahuvrihi ⟨vyavasāyaḥ, niścayaḥ, ātmā/svabhāvaḥ yasyāḥ sā⟩ | pass |
| buddhiḥ | buddhi | Stri. Prathama/Eka | pass |
| ekā | eka | Stri. Prathama/Eka | pass |
| iha | iha | indecl. | pass |
| kuru-nandana | kuru-nandana | Pum. Sambodhana/Eka; tatpurusa ⟨kurūṇāṃ nandanaḥ⟩ | pass |
| bahu-śākhāḥ | bahu-śākhā | Stri. Prathama/Bahu; bahuvrihi ⟨bahvyaḥ śākhāḥ yāsāṃ tāḥ⟩ | pass |
| hi | hi | indecl. | pass |
| anantāḥ | ananta | Stri. Prathama/Bahu | pass |
| ca | ca | indecl. | pass |
| buddhayaḥ | buddhi | Stri. Prathama/Bahu | pass |
| avyavasāyinām | avyavasāyin | Pum. Sasthi/Bahu | pass |

## Justifications

**J1. The compound is not taken as “effortful” or merely “purposive”; Śaṅkara explicitly equates vyavasāyātmikā with niścaya-svabhāvā and connects this buddhi with valid cognition.**
- chosen: vyavasāyātmikā buddhiḥ = “understanding whose nature is settled determination.” (depends on commentary: **yes**)
- gita [1]: `vyavasāyātmikā niścaya-svabhāvā` — ‘Vyavasāyātmikā’ means ‘having determination as its nature.’
- gita [1]: `samyak-pramāṇa-janitatvāt` — Because it is produced by a correct means of knowledge.

**J2. ekā is emphatic, not merely numeral, and iha is not “in this world” but “on the śreyas-path” in Śaṅkara’s construal.**
- chosen: ekā iha = “one alone here, on the path to the highest good.” (depends on commentary: **yes**)
- gita [1]: `ekā eva buddhir` — The understanding is one alone.
- gita [1]: `iha śreyo-mārge` — Here, on the path to the highest good.

**J3. The compound qualifies buddhayaḥ and is not an independent noun phrase “many branches”; Śaṅkara gives the yāsām-bahuvrīhi vigraha and glosses it as bahu-bhedāḥ.**
- chosen: bahu-śākhāḥ = bahuvrīhi, “many-branched,” i.e. “many-divided.” (depends on commentary: **yes**)
- gita [2]: `tā buddhayo bahu-śākhāḥ bahvvayaḥ śākhāḥ yāsāṃ tāḥ bahu-śākhāḥ, bahu-bhedā ity etat` — Those understandings are ‘many-branched’: those whose branches are many (printed bahvvayaḥ, likely for bahvyaḥ), that is, many-divided.
- gita [2]: `yāḥ punar itarā viparīta-buddhayaḥ` — But the other ones are contrary understandings.

**J4. The endlessness is the unlimited proliferation of these contrary understandings by branch and sub-branch, not merely an abstract epithet; Śaṅkara explicitly says the buddhayaḥ are anantāḥ by pratiśākhā-bheda.**
- chosen: anantāḥ = “endless,” predicated of the plural buddhayaḥ. (depends on commentary: **yes**)
- gita [3]: `pratiśākhā-bhedena hy anantā ca buddhayaḥ` — For by the distinction of each branch the understandings too are endless.
- gita [2]: `yāsāṃ śākhā-bheda-pracāra-vaśāt ananto 'pāro 'nuparataḥ saṃsāro nitya-pratato vistīrṇo bhavati` — Because of the spread of their branch-distinctions, saṃsāra becomes endless, boundless, unceasing, ever-extended, and vast.

**J5. Although the dictionary may suggest ‘inactive/negligent,’ Śaṅkara defines the avyavasāyins epistemically: they lack pramāṇa-generated viveka-buddhi. The genitive answers keṣām, “of whom?” and depends on buddhayaḥ.**
- chosen: avyavasāyinām = “of the irresolute,” specifically those lacking valid-knowledge-born discriminative understanding. (depends on commentary: **yes**)
- gita [4]: `keṣām ? avyavasāyināṃ pramāṇa-janita-viveka-buddhi-rahitānām ity arthaḥ` — Of whom? Of the avyavasāyins, that is, of those bereft of discriminative understanding born of a means of knowledge.

**J6. The commentary only repeats the address; the compound relation is decided grammatically from Kuru + nandana as a standard vocative address to Arjuna.**
- chosen: kuru-nandana is a vocative ṣaṣṭhī-tatpuruṣa, “O delight/descendant of the Kurus.” (depends on commentary: no)

## Translation

> On this path to the highest good, O delight of the Kurus,
the understanding (buddhi) whose nature is settled determination is one alone;
for the understandings of the irresolute (avyavasāyin)
are many-branched and endless.

## Analyzer disagreements

- The ByT5 api_seg gives vyavasāya_ātmakā, but the unit text and the local analyses read vyavasāyātmikā; I now analyze the printed feminine compound stem as vyavasāyātmikā rather than the mfn stem vyavasāyātmaka, since the latter derives vyavasāyātmakā.
- ByT5 segments vyavasāyātmikā and bahu-śākhāḥ into their members; per instruction, I give each as a single compound subanta with a whole-compound stem and add samāsa analysis.
- ByT5 treats kuru and nandana as separate compound/member tokens; I analyze the printed address kuru-nandana as one vocative tatpuruṣa compound.

## One-shot delta

- A commentary-blind translation might render vyavasāya as “effort” and avyavasāyinām as “inactive/negligent”; Śaṅkara instead makes the contrast one of pramāṇa-born determinative understanding versus the lack of such discriminative understanding.
- It might translate iha simply as “in this world”; Śaṅkara narrows it to “on the path to the highest good” (śreyo-mārga).
- It might miss that bahu-śākhāḥ is explicitly a bahuvrīhi, “those whose branches are many,” glossed as “many-divided,” and that anantāḥ refers to the endless proliferation of these contrary buddhis.
