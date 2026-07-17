# Triṃśikā v.20 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 14 pass / 0 fail / 0 unsupported.

## Verse

> **yena yena vikalpena yad yad vastu vikalpyate | parikalpita evāsau svabhāvo na sa vidyate**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| yena | yad | Pum. Trtiya/Eka | pass |
| yena | yad | Pum. Trtiya/Eka | pass |
| vikalpena | vikalpa | Pum. Trtiya/Eka | pass |
| yat | yad | Napumsaka. Prathama/Eka | pass |
| yat | yad | Napumsaka. Prathama/Eka | pass |
| vastu | vastu | Napumsaka. Prathama/Eka | pass |
| vikalpyate | kḷp | vi-kḷp, Karmani/Lat/Prathama/Eka | pass |
| parikalpitaḥ | parikalpita | Pum. Prathama/Eka | pass |
| eva | eva | indecl. | pass |
| asau | adas | Pum. Prathama/Eka | pass |
| svabhāvaḥ | svabhāva | Pum. Prathama/Eka; tatpurusa ⟨svasya bhāvaḥ⟩ | pass |
| na | na | indecl. | pass |
| saḥ | tad | Pum. Prathama/Eka | pass |
| vidyate | vid | vid, Karmani/Lat/Prathama/Eka | pass |

## Justifications

**J1. The repeated instrumental relative yena yena agrees with the masculine instrumental singular vikalpena and supplies the means or mode for the passive vikalpyate. I do not take vikalpena adverbially as “optionally,” despite that lexical possibility, because the relative adjective requires a nominal head.**
- chosen: yena yena vikalpena is construed as an instrumental phrase: “by whatever conceptual construction.” (depends on commentary: no)
- trbh []: `yena yena vikalpena ... vikalpyate` — by whichever conceptual construction ... is conceptualized

**J2. Because vikalpyate is passive, the neuter singular vastu is best read as the grammatical subject: “whatever object is conceptualized.” The form yad/yat is formally nominative or accusative neuter singular, but syntax decides for nominative.**
- chosen: yad yad vastu is nominative subject of the passive verb vikalpyate. (depends on commentary: no)
- trbh []: `yad yad vastu vikalpyate` — whatever object is conceptualized

**J3. parikalpitaḥ, asau, and svabhāvaḥ are all masculine nominative singular, so they construe together. The demonstrative asau agrees with svabhāvaḥ, not with neuter vastu. eva marks identity/restriction: the nature so described is precisely the imagined one.**
- chosen: parikalpitaḥ eva asau svabhāvaḥ is a nominal predication: “that is just the imagined nature.” (depends on commentary: no)
- trbh []: `parikalpita evāsau svabhāvo` — that is just the imagined nature

**J4. The pronoun sa is masculine nominative singular, matching svabhāvaḥ. It cannot grammatically refer directly to neuter vastu without gender mismatch.**
- chosen: sa in na sa vidyate refers to svabhāvaḥ, not to vastu. (depends on commentary: no)
- trbh []: `svabhāvo na sa vidyate` — the nature—it does not exist

**J5. The passive/middle form vidyate commonly bears the sense “is found, is present, exists.” With na and the subject svabhāvaḥ, the philosophical force is existential: “that nature does not exist,” rather than merely epistemic “is not known.”**
- chosen: vidyate is translated existentially: “is found / exists.” (depends on commentary: no)
- trbh []: `na sa vidyate` — it does not exist / is not found

## Translation

> By whatever conceptual construction (vikalpa),
whatever object (vastu) is conceptualized—
that is just the imagined nature (parikalpita-svabhāva);
that does not exist.

## Analyzer disagreements

- vikalpyate: ByT5 lemmatizes the verb as vikalpay; I record the bare verbal root kḷp with prefix vi, as required for tinanta analysis. The passive-present features are retained.
- parikalpitaḥ: ByT5 gives lemma parikalpay; because this is a subanta participial adjective in the verse, I give the nominal stem parikalpita as lemma. Its masculine nominative singular analysis is retained.
- yat/yad: ByT5’s sandhied token yad is retained as surface_in_sandhi, but the pausal surface is given as yat.
- sa: ByT5’s sandhied token sa is retained as surface_in_sandhi, but the pausal surface is given as saḥ.

## One-shot delta

- A commentary-blind or dictionary-only rendering might take vikalpena as the adverb “optionally”; the grammar of yena yena vikalpena instead makes it an instrumental nominal phrase.
- It might translate yad yad vastu as an accusative object, but the passive vikalpyate makes it the nominative subject: “whatever object is conceptualized.”
- It might let sa refer back to vastu; gender shows that sa refers to svabhāvaḥ.
- It might render vidyate as “is known,” but the idiom and the negated svabhāva-context call for “exists / is found.”
