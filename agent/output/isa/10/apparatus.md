# Īśopaniṣad (Kāṇva) with Śaṅkara-bhāṣya — 10 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 14 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| anyat | anya | Napumsaka. Prathama/Eka | pass |
| eva | eva | indecl. | pass |
| āhuḥ | ah | ah, Kartari/Lit/Prathama/Bahu | pass |
| vidyayā | vidyā | Stri. Trtiya/Eka | pass |
| anyat | anya | Napumsaka. Prathama/Eka | pass |
| āhuḥ | ah | ah, Kartari/Lit/Prathama/Bahu | pass |
| avidyayā | avidyā | Stri. Trtiya/Eka | pass |
| iti | iti | indecl. | pass |
| śuśruma | śru | śru, Kartari/Lit/Uttama/Bahu | pass |
| dhīrāṇām | dhīra | Pum. Sasthi/Bahu | pass |
| ye | yad | Pum. Prathama/Bahu | pass |
| naḥ | mad | Pum. Caturthi/Bahu | pass |
| tat | tad | Napumsaka. Dvitiya/Eka | pass |
| vicacakṣire | cakṣ | vi-cakṣ, Kartari/Lit/Prathama/Bahu | pass |

## Justifications

**J1. The first anyat, and by parallelism the second, is not an adverbial ‘otherwise’ nor a relative yad; it qualifies an understood phalam, ‘fruit/result’. The supplied mūla-spacing ‘vidyayān yad’ is therefore read as vidyayānyad = vidyayā + anyat.**
- chosen: anyat … anyat: ‘a distinct fruit … a distinct fruit’, with phalam supplied and pṛthag eva giving the force of eva. (depends on commentary: **yes**)
- isup [1]: `anyatpṛthageva vidyayā kriyate phalamityāhur` — ‘A different, separate fruit is produced by vidyā,’ they say.

**J2. The verse is not contrasting liberating knowledge with sheer psychological ignorance. Śaṅkara reads vidyā as jñāna whose fruit is devaloka, and avidyā as karma whose fruit is pitṛloka.**
- chosen: vidyā is knowledge/meditative knowledge, while avidyā is here ritual action (karma); the instrumentals denote means producing distinct fruits. (depends on commentary: **yes**)
- isup [1]: `vidyayā kriyate phalamityāhur ... "vidyayā devalokaḥ"` — They say a fruit is produced by vidyā; ‘by vidyā, the world of the gods.’
- isup [3]: `karmaṇā pitṛlokaḥ` — By karma, the world of the ancestors.
- isup [7]: `tatkarma ca jñānaṃ ca` — That—both karma and knowledge.

**J3. dhīrāṇām is a genitive dependent on an understood/commentarial vacanam, not an accusative object; śuśruma is first plural perfect, ‘we have heard’.**
- chosen: iti śuśruma dhīrāṇām = ‘thus have we heard the utterance of the wise’. (depends on commentary: **yes**)
- isup [6]: `ityevaṃ śuśruma śrutavanto vayaṃ dhīrāṇāṃ dhīmatāṃ vacanam` — Thus, śuśruma: we have heard the utterance of the wise, of the intelligent.

**J4. ye refers to the wise as teachers; naḥ is dative, ‘to us’; tat refers to karma and jñāna; vicacakṣire means ‘explained’, not merely ‘saw’ or ‘perceived’.**
- chosen: ye nas tad vicacakṣire = ‘those teachers who explained that to us’. (depends on commentary: **yes**)
- isup [7]: `ye ācāryā no 'smabhyaṃ tatkarma ca jñānaṃ ca vicacakṣire vyākhyātavantasteṣāmayamāgamaḥ pāramparyāgata ityarthaḥ` — Those teachers who explained to us that—both karma and knowledge; this tradition of theirs has come down by succession.

## Translation

> One thing indeed, distinct, they say, is the fruit through knowledge (vidyā);
another, they say, is the fruit through non-knowledge (avidyā, that is, ritual action).
Thus have we heard the utterance of the wise—
of those who explained that, action and knowledge, to us.

## Analyzer disagreements

- ByT5 treats vidyayān as vidyā_SNM. This is overridden to vidyayā, feminine instrumental singular; the supplied spacing ‘vidyayān yad’ is handled as the standard sandhi vidyayānyad = vidyayā + anyat.
- ByT5 treats yat as the relative pronoun yad. This is overridden to anya- neuter singular anyat, because the commentary glosses anyat … phalam and the mantra’s sandhi requires vidyayānyad rather than vidyayā yad.
- ByT5’s likely accusative analysis for the two anyat forms is overridden to nominative singular, since Śaṅkara paraphrases the construction as a passive proposition, vidyayā kriyate phalam. The surface form is, however, identical in nominative and accusative neuter singular.
- ByT5 marks naḥ as genitive. The commentary’s no ’smabhyaṃ requires dative plural: ‘to us’. In this revision, linga is explicitly supplied as Pum for the verifier’s required subanta feature set, without implying a gendered English reference.
- ByT5 lemmatizes vicacakṣire as vicakṣ. For the required bare-root analysis this is split into prefix vi + root cakṣ; the verbal meaning is fixed by the commentary’s vyākhyātavantaḥ.

## One-shot delta

- A commentary-blind translation could take the printed ‘vidyayān yad’ as involving a relative pronoun yad; Śaṅkara’s anyat … phalam requires vidyayā + anyat, ‘a distinct fruit through vidyā’.
- It could render avidyā simply as ‘ignorance’; Śaṅkara identifies it here with karma, ritual action, contrasted with jñāna/vidyā.
- It could translate vicacakṣire as ‘saw’ and naḥ as ‘our’; the bhāṣya explicitly gives no ’smabhyaṃ and vyākhyātavantaḥ, ‘explained to us’.
- It could miss the supplied vacanam after dhīrāṇām; the point is that the speaker has heard the utterance/tradition of the wise teachers.
