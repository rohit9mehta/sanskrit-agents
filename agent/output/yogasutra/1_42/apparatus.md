# Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904) — 1.42 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 5 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| tatra | tatra | indecl. | pass |
| śabdārthajñānavikalpaiḥ | śabdārthajñānavikalpa | Pum. Trtiya/Bahu; tatpurusa ⟨śabdaś ca arthaś ca jñānaṃ ca; teṣāṃ vikalpāḥ⟩ | pass |
| saṃkīrṇā | saṃkīrṇa | Stri. Prathama/Eka | pass |
| savitarkā | savitarka | Stri. Prathama/Eka; bahuvrihi ⟨vitarkeṇa saha vartamānā samāpattiḥ⟩ | pass |
| samāpattiḥ | samāpatti | Stri. Prathama/Eka | pass |

## Justifications

**J1. The compound is not best read as a simple list “word, object, knowledge, and vikalpa.” Vyāsa first isolates three items—śabda, artha, and jñāna—each illustrated by gauḥ, then says that although they are distinct, they are apprehended without division. The sūtra’s vikalpas are therefore the conflating/conceptual constructions concerning these three factors.**
- chosen: śabdārthajñānavikalpaiḥ = “with/by the conceptual constructions of word, object, and cognition” (depends on commentary: **yes**)
- ys [1]: `tadyathā gaur iti śabdo gaur ity artho gaur iti jñānam ity avibhāgena vibhaktānām api grahaṇaṃ dṛṣṭam.` — For example, the word ‘cow,’ the object ‘cow,’ and the cognition ‘cow’ are seen to be apprehended without division, even though they are distinct.
- ys [2]: `vibhajyamānāś cānye śabdadharmā anye 'rthadharmā anye vijñānadharmā ity eteṣāṃ vibhaktaḥ panthāḥ.` — And when they are being distinguished, the properties of word are one thing, those of object another, and those of cognition another; their paths are distinct.
- ys [3]: `sa cec chabdārthajñānavikalpānuviddha upāvartate sā saṃkīrṇā samāpattiḥ savitarkety ucyate.` — If that [object] recurs as penetrated by the conceptual construction of word, object, and cognition, that mixed samāpatti is called savitarkā.

**J2. The instrumental plural marks what the samāpatti is mixed with. Vyāsa glosses the condition as the meditative object being anuviddha, “pervaded/penetrated,” by the śabda-artha-jñāna-vikalpa; that condition is then explicitly called saṃkīrṇā samāpattiḥ.**
- chosen: saṃkīrṇā construes with instrumental śabdārthajñānavikalpaiḥ (depends on commentary: **yes**)
- ys [3]: `tatra samāpannasya yogino yo gavādyarthaḥ samādhiprajñāyāṃ samārūḍhaḥ sa cec chabdārthajñānavikalpānuviddha upāvartate sā saṃkīrṇā samāpattiḥ savitarkety ucyate.` — There, if the object such as a cow, having arisen in the samādhi-cognition of the yogin in samāpatti, recurs as penetrated by the conceptual construction of word, object, and cognition, that is the mixed samāpatti and is called savitarkā.

**J3. The word is not the pronoun sa plus vitarkā. Vyāsa treats it as the name of the mixed samāpatti and contrasts it with nirvitarkā samāpatti, where the samādhi-cognition is empty of such vikalpa. Hence the sa- is the ‘with’ element of a compound, and vitarka is understood in this context through the presence of word-object-cognition vikalpa, not as mere ordinary ‘doubt.’**
- chosen: savitarkā is a single technical adjective: “with conceptual examination/discursiveness” (depends on commentary: **yes**)
- ys [3]: `sā saṃkīrṇā samāpattiḥ savitarkety ucyate.` — That mixed samāpatti is called savitarkā.
- ys [5, 6]: `yadā punaḥ śabdasaṃketasmṛtipariśuddhau śrutānumānajñānavikalpaśūnyāyāṃ samādhiprajñāyāṃ svarūpamātreṇāvasthito 'rthas tatsvarūpākāramātratayaivāvacchidyate. sā ca nirvitarkā samāpattiḥ.` — But when, with the memory of verbal convention purified, the object rests in its own form alone in a samādhi-cognition empty of the vikalpa of knowledge from testimony and inference, and is delimited only by the form of its own nature—that is nirvitarkā samāpatti.

**J4. Rather than translating tatra as a merely spatial “there,” I take it contextually: “in that case/context.” Vyāsa expands it as the situation of a yogin in samāpatti whose object has arisen in samādhi-cognition.**
- chosen: tatra refers to the meditative context of the yogin’s samāpatti (depends on commentary: **yes**)
- ys [3]: `tatra samāpannasya yogino yo gavādyarthaḥ samādhiprajñāyāṃ samārūḍhaḥ` — There, the object such as a cow which has arisen in the samādhi-cognition of the yogin in samāpatti …

## Translation

> In that meditative context, the absorptive attainment (samāpatti) that is mixed with conceptual constructions (vikalpa) concerning word, object, and cognition is “with conceptual examination” (savitarkā).

## Analyzer disagreements

- The ByT5 output split savitarkā as sa + vitarkā. I analyze savitarkā as one bahuvrīhi/adjectival technical compound, because Vyāsa has savitarkety ucyate at line 3 and contrasts nirvitarkā samāpattiḥ at line 6.
- The ByT5 output marked śabda, artha, and jñāna only as compound pre-members and vikalpaiḥ as the inflected word, without specifying the compound relation. I resolve the whole as a genitive tatpuruṣa with an embedded dvandva: “vikalpas of word, object, and cognition,” on the basis of lines 1–3.
- The ByT5 lemma for saṃkīrṇā was given as verbal/root-like saṃkṛ. For nominal analysis I give the inflected participial/adjectival stem saṃkīrṇa, Stri Prathama Eka.

## One-shot delta

- A commentary-blind translation might take śabdārthajñānavikalpaiḥ as four separate factors—“word, meaning, knowledge, and imagination”—whereas Vyāsa’s explanation makes word, object, and cognition the three distinguished factors whose undivided apprehension is the vikalpa at issue.
- It might translate savitarkā as involving ordinary “doubt” or “guesswork.” Vyāsa instead defines it technically as the mixed samāpatti in which the samādhi-object is still penetrated by word-object-cognition vikalpa.
- It might follow the analyzer’s split sa + vitarkā, but the bhāṣya treats savitarkā as a single named type of samāpatti, contrasted with nirvitarkā.
