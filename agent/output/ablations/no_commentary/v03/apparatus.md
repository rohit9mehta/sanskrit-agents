# Triṃśikā v.3 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 5 pass / 0 fail / 0 unsupported.

## Verse

> **asaṃviditakopādisthānavijñaptikañ ca tat sadā sparśamanaskāravitsaṃjñācetanānvitam**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| asaṃviditakopādisthānavijñaptikam | asaṃviditakopādisthānavijñaptika | Napumsaka. Prathama/Eka; tatpurusa ⟨asaṃviditasya kopa-ādeḥ sthānasya vijñaptikam⟩ | pass |
| ca | ca | indecl. | pass |
| tat | tad | Napumsaka. Prathama/Eka | pass |
| sadā | sadā | indecl. | pass |
| sparśamanaskāravitsaṃjñācetanānvitam | sparśamanaskāravitsaṃjñācetanānvita | Napumsaka. Prathama/Eka; tatpurusa ⟨sparśa-manaskāra-vid-saṃjñā-cetanābhiḥ anvitam⟩ | pass |

## Justifications

**J1. Segmentation and broad compound relation of asaṃviditakopādisthānavijñaptikam.**
- chosen: a-saṃvidita-kopa-ādi-sthāna-vijñaptika (depends on commentary: no)
- trbh []: `asaṃviditakopādisthānavijñaptikañ` — No commentary used: adopting the analyzer’s segmentation a + saṃvidita + kopa + ādi + sthāna + vijñaptika. MW gives kopa as 'morbid irritation' and also 'passion, wrath, anger'; ādi as an ifc. element means 'beginning with, and so on'. The negative a- plus saṃvidita gives 'unrecognized/unperceived'.

**J2. Case construal of asaṃviditakopādisthānavijñaptikam and sparśamanaskāravitsaṃjñācetanānvitam.**
- chosen: neuter nominative singular predication to tat (depends on commentary: no)
- trbh []: `vijñaptikañ ca tat sadā ... anvitam` — The -am forms are neuter nominative/accusative singular. Since tat is a neuter nominative singular pronoun and there is no finite verb governing an accusative, the adjectives are best construed as nominative predicate adjectives in a nominal sentence.

**J3. Interpretation of vit in sparśamanaskāravitsaṃjñā-.**
- chosen: vid as the member stem underlying vit before saṃjñā (depends on commentary: no)
- trbh []: `manaskāravitsaṃjñā` — The printed vit is explained grammatically as vid + saṃjñā, with final d devoiced to t before s. MW s.v. vid gives 'knowing, understanding, a knower', so the ablation translation uses 'knowing' rather than introducing an unsupported technical equivalent.

**J4. Scope of anvitam in sparśa-manaskāra-vid-saṃjñā-cetanā-anvitam.**
- chosen: X-anvita as 'accompanied by X', with the preceding members forming a coordinated list (depends on commentary: no)
- trbh []: `sadā sparśamanaskāravitsaṃjñācetanānvitam` — MW s.v. anvita gives 'joined, attended, accompanied by, endowed with'. Therefore the preceding members are construed together as what the referent is accompanied by, while sadā modifies the whole predication as 'always'.

**J5. Reading of the nasal in vitsaṃjñā- versus vulgate vitsañjñā-.**
- chosen: saṃjñā (depends on commentary: no)
- trbh []: `vitsaṃjñācetanā` — The supplied bhāṣya reading has saṃjñā, and MW lists the lemma as saṃjñā. The vulgate sañjñā is not taken to require a different morphological analysis in this ablation.

## Translation

> And that, too, is presentational (vijñaptika) of an unrecognized locus (sthāna) of anger/irritation and the like (kopa-ādi); it is always accompanied by contact (sparśa), attention (manaskāra), knowing (vid), conception (saṃjñā), and volition (cetanā).

## Analyzer disagreements

- ByT5 marks vid as an independent-looking vid_SNM; here it is treated as the compound-member stem vid inside the single printed compound sparśamanaskāravitsaṃjñācetanānvitam, because vit is sandhi for vid before saṃjñā.
- ByT5’s abbreviated tag for anvitam appears not to record the required neuter nominative singular agreement; here sparśamanaskāravitsaṃjñācetanānvitam is analyzed as Napuṃsaka Prathama Eka, predicative to tat.

## One-shot delta

- Because no commentary is used, the sandhi sequence kopādi is vulnerable: a blind parse naturally follows kopa + ādi, yielding 'anger/irritation and the like', even though the context may require a different technical segmentation.
- Without commentary, vit is taken from vid 'knowing/understanding'; a technical Yogācāra value cannot be established from the supplied MW entries alone.
- The technical force of vijñaptika is only inferred as 'presentational/representational' from the form and the analyzer, since no dictionary entry for vijñaptika/vijñapti was supplied.

## Open questions

- The first compound is semantically insecure under the provided lexicon: kopa + ādi is grammatical and dictionary-supported, but the sandhi could in principle hide another technical term.
- The exact technical sense of vijñaptika remains underdetermined without a lexicon entry or commentary.
- The role of vid in the mental-factor list may be more technical than the dictionary meaning 'knowing'; this cannot be resolved in the ablation run.
