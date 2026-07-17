# Triṃśikā v.22 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 14 pass / 0 fail / 2 unsupported.

## Verse

> **ata eva sa naivānyo nānanyaḥ paratantrataḥ anityatādivad vācyo nādṛṣṭe 'smin sa dṛśyate**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| ataḥ | atas | indecl. | pass |
| eva | eva | indecl. | pass |
| saḥ | tad | Pum. Prathama/Eka | pass |
| na | na | indecl. | pass |
| eva | eva | indecl. | pass |
| anyaḥ | anya | Pum. Prathama/Eka | pass |
| na | na | indecl. | pass |
| ananyaḥ | ananya | Pum. Prathama/Eka; tatpurusa ⟨na anyaḥ⟩ | pass |
| paratantrataḥ | paratantra | indecl.; bahuvrihi ⟨parasya tantraṃ yasya⟩ | unsupported |
| anityatādivat | anityatādivat | indecl.; bahuvrihi ⟨anityatā ādir yasya dṛṣṭāntasamūhasya⟩ | unsupported |
| vācyaḥ | vācya | Pum. Prathama/Eka | pass |
| na | na | indecl. | pass |
| adṛṣṭe | adṛṣṭa | Pum. Saptami/Eka; tatpurusa ⟨na dṛṣṭaḥ⟩ | pass |
| asmin | idam | Pum. Saptami/Eka | pass |
| saḥ | tad | Pum. Prathama/Eka | pass |
| dṛśyate | dṛś | dṛś, Karmani/Lat/Prathama/Eka | pass |

## Justifications

**J1. Construe atas/ataḥ as a causal-deictic indeclinable, with eva intensifying the immediately preceding reason.**
- chosen: ata eva = ‘for that very reason’ (depends on commentary: no)
- trbh []: `ata eva` — Grammatically, atas/ataḥ means ‘hence/from this’, and eva strengthens it: ‘just for this reason’.

**J2. Take anyaḥ and ananyaḥ as masculine nominative singular predicate adjectives agreeing with saḥ; paratantrataḥ supplies the ablatival standard ‘from/than the dependent’ for both predicates.**
- chosen: saḥ … anyaḥ / ananyaḥ paratantrataḥ = ‘that is neither different nor non-different from the dependent’ (depends on commentary: no)
- trbh []: `sa na eva anyaḥ na ananyaḥ paratantrataḥ` — The nominative predicate adjectives match saḥ; Sanskrit anya commonly construes with an ablatival expression for ‘different from’, and the same standard is carried over to ananyaḥ.

**J3. Read -vat as the likeness affix, not as possessive -vat; anityatādi supplies an example-class beginning with impermanence.**
- chosen: anityatādivat = ‘like impermanence and so on’ (depends on commentary: no)
- trbh []: `anityatādivat` — The vati/-vat formation is lexically and grammatically used for resemblance: ‘as/like X’; ādi indicates ‘X and the rest’.

**J4. Analyze vācyaḥ as a gerundive/passive verbal adjective used predicatively with saḥ, rather than as a finite verb.**
- chosen: vācyaḥ = ‘is to be said/declared’ (depends on commentary: no)
- trbh []: `vācyo` — The form is masculine nominative singular and agrees with saḥ; gerundive vācya means ‘to be said, to be called, to be declared’.

**J5. Take adṛṣṭe asmin as a locative absolute and take na with the main passive dṛśyate.**
- chosen: na adṛṣṭe asmin sa dṛśyate = ‘when this is not seen, that is not seen’ (depends on commentary: no)
- trbh []: `na adṛṣṭe asmin sa dṛśyate` — A locative singular participle plus a locative singular pronoun forms a locative absolute; dṛśyate is a present passive, ‘is seen’, negated by na.

**J6. Use the deictic contrast: asmin points to the nearer dependent term signaled by paratantrataḥ, while saḥ continues the nominative subject of the verse.**
- chosen: asmin refers to ‘this [dependent]’ and saḥ to the other term under discussion (depends on commentary: no)
- trbh []: `paratantrataḥ … adṛṣṭe 'smin sa dṛśyate` — The nearest explicit comparative standard is paratantra; the locative asmin naturally resumes it as ‘this’, while saḥ remains the entity being predicated and seen/not seen.

## Translation

> For that very reason, that is to be declared
neither different nor non-different from the dependent (paratantra),
like impermanence and the like;
when this [dependent] is not seen, that is not seen.

## Analyzer disagreements

- The analyzer’s api_seg offers paratantrāt, but the printed bhāṣya reading is paratantrataḥ; I analyze it as an ablatival tasil-type indeclinable from paratantra, not as the regular ablative singular paratantrāt.
- The analyzer treats paratantrataḥ as if it were a case-form of paratantra; grammatically the -taḥ ending here is better taken as an indeclinable ablatival formation meaning ‘from/than the dependent’.
- The analyzer splits anitya_tā_ādi_vat; I treat anityatā as one derived abstract stem within anityatādi, with vati/-vat expressing likeness: ‘like impermanence and so on’.
- The analyzer splits a separately in na_a_dṛṣṭe; I analyze adṛṣṭe as one privative participial adjective, a nañ-tatpuruṣa/PPP form, in a locative absolute with asmin.
- The analyzer lists vācyo under the verbal root vac; for this apparatus it is a subanta gerundive stem vācya, masculine nominative singular, though derived from √vac.

## One-shot delta

- A commentary-blind or overly mechanical rendering could take paratantrataḥ as ‘because of dependence’ rather than ‘from/than the dependent’, obscuring the different/non-different construction.
- It could read anityatādivat as possessive, ‘having impermanence and so on’, instead of the likeness expression ‘like impermanence and so on’.
- It could attach na to the locative phrase nādṛṣṭe rather than to the main verb dṛśyate; the better grammatical construal is ‘when this is unseen, that is not seen’.
- It could translate dṛśyate as active/middle ‘sees’ rather than passive ‘is seen’.
- Without commentary, the precise antecedents of saḥ and asmin remain partly inferential, so naming the first as a specific Yogācāra technical nature would go beyond the evidence supplied in this ablation run.

## Open questions

- No commentary is available in this run, so the precise doctrinal antecedent of saḥ is not fixed here beyond ‘that [term/nature]’.
- The items included under ādi in anityatādi cannot be specified from the verse grammar alone.
- The locative adṛṣṭe/asmin is formally compatible with masculine or neuter singular; masculine has been chosen for agreement with the implied masculine term, but this remains context-dependent without commentary.
