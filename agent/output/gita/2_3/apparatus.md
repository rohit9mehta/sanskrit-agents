# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.3 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 13 pass / 0 fail / 1 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| klaibyam | klaibya | Napumsaka. Dvitiya/Eka | pass |
| mā | mā | indecl. | pass |
| sma | sma | indecl. | pass |
| gamaḥ | gam | gam, Kartari/Lun/Madhyama/Eka | unsupported |
| pārtha | pārtha | Pum. Sambodhana/Eka | pass |
| na | na | indecl. | pass |
| etat | etad | Napumsaka. Prathama/Eka | pass |
| tvayi | tvad | Pum. Saptami/Eka | pass |
| upapadyate | pad | upa-pad, Kartari/Lat/Prathama/Eka | pass |
| kṣudram | kṣudra | Napumsaka. Dvitiya/Eka | pass |
| hṛdaya-daurbalyam | hṛdaya-daurbalya | Napumsaka. Dvitiya/Eka; tatpurusa ⟨hṛdayasya daurbalyam⟩ | pass |
| tyaktvā | tyaj | indecl. | pass |
| uttiṣṭha | sthā | ud-sthā, Kartari/Lot/Madhyama/Eka | pass |
| paraṃtapa | paraṃtapa | Pum. Sambodhana/Eka; tatpurusa ⟨parān tapati iti⟩ | pass |

## Justifications

**J1. The commentary is absent for this unit, so the construal rests on grammar and dictionary. mā sma forms a prohibition with the augmentless aorist gamaḥ, and klaibyam is taken as an accusative state/goal with √gam. MW s.v. klaibya, 324,1 gives “unmanliness, weakness, timidity, cowardice,” so “cowardice/unmanliness” is preferable to a narrowly physical “impotence.”**
- chosen: “Do not lapse into cowardice/unmanliness” for klaibyaṃ mā sma gamaḥ. (depends on commentary: no)

**J2. etat is neuter nominative singular, the subject of upapadyate; tvayi is locative singular, “in/with regard to you.” MW s.v. upapad, 201,3 gives senses including “to reach, obtain,” “to enter into any state,” and “to take place”; with a locative subject-construal the idiomatic English is “befit” or “be appropriate to,” not “you do not obtain this.”**
- chosen: naitat tvayy upapadyate = “this does not befit you.” (depends on commentary: no)

**J3. hṛdaya-daurbalya is analyzed as a ṣaṣṭhī-tatpuruṣa, hṛdayasya daurbalyam, “weakness of the heart/mind.” MW s.v. hṛdaya, 1302,3 includes “heart” and “mind”; MW s.v. daurbalya, 499,2 gives “weakness”; MW s.v. kṣudra, 330,2 includes “mean, low, vile” as well as “small.” In context, kṣudram qualifies the accusative compound and is rendered “petty.”**
- chosen: kṣudraṃ hṛdaya-daurbalyaṃ as “petty weakness of heart.” (depends on commentary: no)

**J4. tyaktvā is an absolutive of √tyaj, so it gives prior or attendant action relative to the imperative uttiṣṭha. MW s.v. tyaj, 456,3 gives “leave, abandon, quit,” and MW s.v. utthā, 179,3 gives “stand up, rise.” The printed tyaktvottiṣṭha is sandhi of tyaktvā + uttiṣṭha, not one finite verbal form.**
- chosen: tyaktvā uttiṣṭha = “having cast off, stand up.” (depends on commentary: no)

**J5. Both forms are vocative masculine singular addresses. paraṃtapa is not a separate predicate or command; MW s.v. paraṃtapa, 586,3 gives “destroying foes,” so it is translated as the epithet “O scorcher/destroyer of foes.”**
- chosen: pārtha and paraṃtapa as vocative epithets. (depends on commentary: no)

## Translation

> Do not lapse into cowardice (klaibya), O Pārtha;
this does not befit you.
Having cast off petty weakness of heart (hṛdaya-daurbalya),
stand up, O scorcher of foes (paraṃtapa).

## Analyzer disagreements

- gamaḥ: ByT5 gives gam_SPs2 without an explicit lakāra; I specify it as an augmentless prohibitive Lūṅ form after mā sma.
- etat: ByT5’s SNNe tag does not disambiguate nominative from accusative; I take etat as Prathama Eka because it is the subject of upapadyate.
- upapadyate: ByT5 lemmatizes as upapad; in the required format this is split into bare root pad with prefix upa.
- hṛdaya-daurbalyam: ByT5 marks hṛdaya as a compound member and daurbalyam as the inflected head; per instructions the inflected compound is analyzed with the whole stem hṛdaya-daurbalya. The later verifier’s tool_error/unsupported-compound note is treated as a tool limitation, so the compound analysis is retained.
- uttiṣṭha: ByT5 lemmatizes as utthā; per the supplied MW entry and the required prefix/root format, I analyze it as root sthā with prefix ud and lakāra Lot.
- tvayi: revised after verifier report to include linga=Pum, since the pronoun refers to the masculine addressee Arjuna and the verifier requires a full nominal feature set.

## One-shot delta

- The bhāṣya is silent here, so there is no commentary-controlled semantic correction; the main risks are grammatical rather than exegetical.
- A quick translation might treat mā sma gamaḥ as an ordinary “you go” form; it is a prohibition with an augmentless aorist/injunctive: “do not lapse.”
- naitat must be segmented as na etat, with etat as the subject and tvayi as locative; otherwise one might mistranslate it as “you do not obtain this.”
- tyaktvottiṣṭha is tyaktvā + uttiṣṭha by sandhi, preserving the absolutive-plus-imperative structure: “having cast off, stand up.”
