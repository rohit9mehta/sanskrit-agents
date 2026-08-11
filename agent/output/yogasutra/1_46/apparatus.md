# Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904) — 1.46 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 4 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| tāḥ | tad | Stri. Prathama/Bahu | pass |
| eva | eva | indecl. | pass |
| sabījaḥ | sabīja | Pum. Prathama/Eka; bahuvrihi ⟨bījena saha vartamānaḥ / bījaṃ yasya saḥ⟩ | pass |
| samādhiḥ | samādhi | Pum. Prathama/Eka | pass |

## Justifications

**J1. Translate tā eva as “these very [four attainments],” not as an independent feminine plural with no supplied referent.**
- chosen: tāḥ refers to the four samāpattis previously taught. (depends on commentary: **yes**)
- ys [1]: `tāś catasraḥ samāpattayo bahirvastubījā iti samādhir api sabījaḥ.` — Those four attainments, having external objects as their seed, therefore the samādhi too is with seed.

**J2. Take bīja technically as the objective support or germ of these samāpattis, not as a literal plant-seed; render “seeded concentration (sabīja samādhi).”**
- chosen: sabījaḥ means “seeded,” i.e. possessing an external-object seed. (depends on commentary: **yes**)
- ys [1]: `bahirvastubījā iti samādhir api sabījaḥ` — because they have external objects as seed, the samādhi too is seeded
- ys [2]: `tatra sthūle 'rthe savitarko nirvitarkaḥ, sūkṣme 'rthe savicāro nirvicāra iti caturdhopasaṃkhyātaḥ samādhir iti.` — There, with a gross object: savitarka and nirvitarka; with a subtle object: savicāra and nirvicāra—thus samādhi is counted fourfold.

**J3. Although tāḥ is feminine plural, samādhiḥ is singular masculine because the sūtra identifies the four samāpattis collectively as the seeded form of samādhi.**
- chosen: The singular samādhiḥ is a class-name comprising those four attainments. (depends on commentary: **yes**)
- ys [1]: `tāś catasraḥ samāpattayo ... samādhir api sabījaḥ` — those four samāpattis ... the samādhi too is seeded
- ys [2]: `caturdhopasaṃkhyātaḥ samādhir iti` — samādhi is counted fourfold

## Translation

> These very [four attainments] are the seeded concentration (sabīja samādhi).

## Analyzer disagreements

- ByT5 split sabījaḥ as sa + bījaḥ. I treat sabījaḥ as one inflected bahuvrīhi compound adjective, because the sūtra is traditionally read sabījaḥ and the bhāṣya glosses the point with samādhir api sabījaḥ after explaining the samāpattis as bahirvastubījāḥ (line 1).
- ByT5’s segmentation gives surface tāḥ, while the printed sandhi form is tā before eva. I record surface as the pausal tāḥ and surface_in_sandhi as tā.

## One-shot delta

- A commentary-blind translation might leave tāḥ vague; Vyāsa identifies it as the four samāpattis.
- It might split sabījaḥ into sa + bījaḥ or read bīja as an ordinary seed; the bhāṣya makes it a technical ‘external-object seed.’
- It might treat samādhiḥ as a fifth samādhi beyond the four, whereas the bhāṣya says samādhi is counted fourfold through them.
