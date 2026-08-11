# Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904) — 1.45 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 3 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| sūkṣmaviṣayatvam | sūkṣmaviṣayatva | Napumsaka. Prathama/Eka; bahuvrihi ⟨sūkṣmo viṣayo yasya, tasya bhāvaḥ⟩ | pass |
| ca | ca | indecl. | pass |
| aliṅgaparyavasānam | aliṅgaparyavasāna | Napumsaka. Prathama/Eka; bahuvrihi ⟨aliṅgaṃ paryavasānaṃ yasya tat⟩ | pass |

## Justifications

**J1. The bhāṣya repeatedly explains the relevant relation as ‘X is the subtle object’ of the preceding level. This supports taking sūkṣmaviṣaya as a bahuvrīhi-type expression—‘one whose object is subtle’—abstracted by -tva.**
- chosen: sūkṣmaviṣayatva = ‘the condition of having a subtle object’, not merely ‘subtlety of the object-domain’. (depends on commentary: **yes**)
- ys [1, 2, 3, 4, 5, 6, 7, 8]: `pārthivasyāṇor gandhatanmātraṃ sūkṣmo viṣayaḥ. āpyasya rasatanmātram. taijasasya rūpatanmātram. vāyavīyasya sparśatanmātram. ākāśasya śabdatanmātram iti. teṣām ahaṃkāraḥ. asyāpi liṅgamātraṃ sūkṣmo viṣayaḥ. liṅgamātrasyāpy aliṅgaṃ sūkṣmo viṣayaḥ.` — For the earth-atom the smell-tanmātra is the subtle object; for the watery, the taste-tanmātra; for the fiery, the form-tanmātra; for the airy, the touch-tanmātra; for space, the sound-tanmātra. For these, ahaṃkāra; for that too, the liṅga-mātra is the subtle object; and for the liṅga-mātra too, the aliṅga is the subtle object.

**J2. The bhāṣya makes the aliṅga the last subtle object and explicitly says there is nothing subtler beyond it in this series. It then raises the possible objection that puruṣa is subtle, but answers that puruṣa is not the anvayin/material-continuing cause of the liṅga; hence unsurpassed subtlety is explained in the pradhāna.**
- chosen: aliṅgaparyavasānam = ‘having the aliṅga as its endpoint’; aliṅga here is the pradhāna, not puruṣa. (depends on commentary: **yes**)
- ys [8, 9]: `liṅgamātrasyāpy aliṅgaṃ sūkṣmo viṣayaḥ. na cāliṅgāt paraṃ sūkṣmam asti.` — For the liṅga-mātra too, the aliṅga is the subtle object. And there is nothing subtle beyond the aliṅga.
- ys [10, 11, 12, 13]: `nanv asti puruṣaḥ sūkṣma iti satyam. yathā liṅgāt param aliṅgasya saukṣmyaṃ na caivaṃ puruṣasya. kiṃtu, liṅgasyānvayikāraṇaṃ puruṣo na bhavati, hetus tu bhavatīti. ataḥ pradhāne saukṣmyaṃ niratiśayaṃ vyākhyātam.` — ‘But is there not puruṣa, which is subtle?’ True; but the subtlety of the aliṅga is beyond the liṅga in a way that is not the case for puruṣa. Rather, puruṣa is not the continuing cause of the liṅga, though it is a causal condition. Therefore unsurpassed subtlety has been explained in the pradhāna.

**J3. The neuter -am forms are construed as a nominal sentence: ‘subtle-objectedness is aliṅga-ended’. The compound is not ‘the termination of the aliṅga’ but ‘that whose termination is the aliṅga’, because the commentary’s sequence culminates at aliṅga/pradhāna.**
- chosen: aliṅgaparyavasānam is a bahuvrīhi predicate agreeing with sūkṣmaviṣayatvam. (depends on commentary: **yes**)
- ys [8, 9, 13]: `liṅgamātrasyāpy aliṅgaṃ sūkṣmo viṣayaḥ. na cāliṅgāt paraṃ sūkṣmam asti. ataḥ pradhāne saukṣmyaṃ niratiśayaṃ vyākhyātam.` — For the liṅga-mātra too, the aliṅga is the subtle object. There is nothing subtle beyond the aliṅga. Therefore unsurpassed subtlety has been explained in the pradhāna.

**J4. The forms are formally ambiguous between nominative and accusative neuter singular, but the sūtra has no finite verb governing an accusative object. The most economical construction is subject plus predicate: ‘the condition of having subtle objects is aliṅga-ended’.**
- chosen: Both sūkṣmaviṣayatvam and aliṅgaparyavasānam are read as Prathamā Ekavacana in a nominal sentence. (depends on commentary: no)

## Translation

> And the condition of having subtle objects has the unmarked (aliṅga, the pradhāna) as its endpoint.

## Analyzer disagreements

- ByT5 represents tvam as the final simple item tva_SNNe; here the analyzable inflected word is the full derived compound stem sūkṣmaviṣayatva, Napuṃsaka Prathamā Ekavacana.
- ByT5 represents paryavasānam under the simple lemma paryavasāna with aliṅga as a compound pre-member; here the inflected word is the full compound stem aliṅgaparyavasāna, Napuṃsaka Prathamā Ekavacana.
- The tagger does not mark the external sandhi ca + aliṅga- > cāliṅga-; the apparatus separates ca and aliṅgaparyavasānam and notes the shared ā.

## One-shot delta

- Without the bhāṣya one might extend the culmination to puruṣa on the ground that puruṣa is subtle; Vyāsa explicitly considers this and excludes it as the endpoint of this causal series.
- One might translate aliṅga generically as ‘absence of marks’; the commentary directs it to the Sāṃkhya pradhāna as the unsurpassed subtle terminus.
- One might flatten sūkṣmaviṣayatva into ‘the subtlety of objects’; the bhāṣya instead lays out a hierarchy in which each prior level has a subtler object.
