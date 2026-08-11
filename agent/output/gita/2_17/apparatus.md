# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.17 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 15 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| avināśi | avināśin | Napumsaka. Dvitiya/Eka | pass |
| tu | tu | indecl. | pass |
| tat | tad | Napumsaka. Dvitiya/Eka | pass |
| viddhi | vid | vid, Kartari/Lot/Madhyama/Eka | pass |
| yena | yad | Napumsaka. Trtiya/Eka | pass |
| sarvam | sarva | Napumsaka. Prathama/Eka | pass |
| idam | idam | Napumsaka. Prathama/Eka | pass |
| tatam | tata | Napumsaka. Prathama/Eka | pass |
| vināśam | vināśa | Pum. Dvitiya/Eka | pass |
| avyayasya | avyaya | Napumsaka. Sasthi/Eka | pass |
| asya | idam | Napumsaka. Sasthi/Eka | pass |
| na | na | indecl. | pass |
| kaścit | kaścit | Pum. Prathama/Eka | pass |
| kartum | kṛ | indecl. | pass |
| arhati | arh | arh, Kartari/Lat/Prathama/Eka | pass |

## Justifications

**J1. The verse’s syntax is tat ... viddhi with avināśi predicated of tat. Śaṅkara glosses avināśi as that whose nature is not to perish, and glosses tat viddhi simply as ‘understand that’.**
- chosen: avināśi is translated ‘imperishable’ as an object-complement to tat: ‘know that to be imperishable.’ (depends on commentary: **yes**)
- gita [1]: `avināśi na vinaṣṭuṃ śīlaṃ yasyeti |` — ‘Imperishable’: that whose nature is not to perish.
- gita [3]: `tat viddhi vijānīhi |` — ‘Know that’: understand it.

**J2. Śaṅkara explicitly assigns the particle a distinguishing/qualifying function with respect to asat, so it should not be left as a weak filler such as ‘indeed’.**
- chosen: tu is rendered contrastively, ‘but’. (depends on commentary: **yes**)
- gita [2]: `tu-śabdo 'sato viśeṣaṇārthaḥ |` — The word tu is for distinguishing/qualifying from the unreal (asat).

**J3. The relative clause is passive: ‘by which this whole world is pervaded.’ Śaṅkara identifies the instrumental agent as sad-ākhya brahman and glosses tataṃ with vyāptam, adding the comparison of pots pervaded by space.**
- chosen: yena refers to the Brahman called sat, and tatam means ‘pervaded’. (depends on commentary: **yes**)
- gita [4]: `kim ? yena sarvam idaṃ jagat tataṃ vyāptaṃ sad-ākhyena brahmaṇā sākāśam, ākāśenaiva ghaṭādayaḥ |` — What? That by which this whole world, including space, is spread/pervaded—by Brahman called sat; just as pots and the like are [pervaded] by space.

**J4. Although the words alone could mean ‘all this/everything,’ Śaṅkara supplies jagat and even says sākāśam, ‘including space’.**
- chosen: sarvam idam is ‘this whole world,’ not an abstract ‘everything’ without contextual referent. (depends on commentary: **yes**)
- gita [4]: `yena sarvam idaṃ jagat tataṃ vyāptaṃ sad-ākhyena brahmaṇā sākāśam` — By which this whole world is spread/pervaded by Brahman called sat, including space.

**J5. Śaṅkara defines avyaya not merely as ‘inexhaustible’ but as not undergoing increase or decrease and not deviating from its own form; he then restates the phrase as avyayasya asya brahmaṇaḥ.**
- chosen: avyayasya asya means ‘of this changeless/undeclining [Brahman]’. (depends on commentary: **yes**)
- gita [6]: `avyayasya na vyeti upacayāpacayau na yāti iti avyayaṃ tasya avyayasya |` — ‘Of the avyaya’: it does not pass away; it does not undergo increase and decrease—therefore it is avyaya; of that avyaya.
- gita [7]: `naitat sadākhyaṃ brahma svena rūpeṇa vyeti vyabhicarati, niravayavatvāt, dehādivat |` — This Brahman called sat does not depart from, or deviate from, its own form, because it is partless, unlike body and the like.
- gita [10]: `ato 'vyayasya asya brahmaṇaḥ vināśaṃ na kaścit kartum arhati, na kaścit atmānaṃ vināśayituṃ śaknoti īśvaro 'pi |` — Therefore no one is able to bring about the destruction of this avyaya Brahman; no one can destroy the Self, not even the Lord.

**J6. The noun is not restricted here to bodily death; Śaṅkara glosses it as adarśana and abhāva and applies it to the impossibility of destroying Brahman/the Self.**
- chosen: vināśam is rendered ‘destruction’ with the nuance ‘disappearance/absence’. (depends on commentary: **yes**)
- gita [5]: `vināśam adarśanam abhāvam |` — ‘Destruction’: disappearance, absence.
- gita [10]: `avyayasya asya brahmaṇaḥ vināśaṃ na kaścit kartum arhati` — No one is able to bring about the destruction of this changeless Brahman.

**J7. With the infinitive kartum, arhati can be read several ways, but Śaṅkara glosses it with śaknoti, ‘is able,’ and explicitly includes even īśvara in the negated scope.**
- chosen: na kaścit kartum arhati means ‘no one can bring about,’ not ‘no one deserves/ought to bring about’. (depends on commentary: **yes**)
- gita [10]: `na kaścit atmānaṃ vināśayituṃ śaknoti īśvaro 'pi |` — No one can destroy the Self, even the Lord.
- gita [11]: `ātmā hi brahma, svātmani ca kriyāvirodhāt ||bhgs_2.17||` — For the Self is Brahman, and action with regard to oneself is contradictory.

## Translation

> But know that to be imperishable
by which this whole world is pervaded.
No one can bring about the destruction
of this changeless Brahman (brahman), the Self (ātman).

## Analyzer disagreements

- ByT5’s api_seg omits avināśi, but the printed unit and ByT5 local_S/local_SLM include it; the analysis follows the printed unit.
- ByT5 gives tatam with lemma tan; per the requested subanta format it is analyzed with the nominal participial stem tata, with the note that it is a past passive participle from √tan.
- ByT5’s segmented/sandhi output has kaścid before kartum, but the printed unit has kaścit and regular sandhi before k does not voice final t; surface_in_sandhi is therefore kept as kaścit.

## One-shot delta

- A commentary-blind translation might leave tu as a negligible ‘indeed’; Śaṅkara makes it contrastive with asat.
- It might fail to identify the ‘by which’ as Brahman called sat and the ‘this’ as the whole world; Śaṅkara states both.
- It might translate avyaya simply as another word for ‘imperishable’; Śaṅkara narrows it to absence of increase, decrease, and deviation from its own form.
- It might render arhati morally as ‘ought/deserves’; Śaṅkara glosses it by śaknoti, ‘can/is able,’ and extends the impossibility even to īśvara.
