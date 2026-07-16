# Triṃśikā v.9 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 10 pass / 0 fail / 0 unsupported.

## Verse

> **sarvatragair viniyataiḥ kuśalaiś caitasair asau | saṃprayuktā tathā kleśair upakleśais trivedanā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| sarvatragaiḥ | sarvatraga | Pum. Trtiya/Bahu; tatpurusa ⟨sarvatra gacchatīti gaḥ⟩ | pass |
| viniyataiḥ | viniyata | Pum. Trtiya/Bahu | pass |
| kuśalaiḥ | kuśala | Pum. Trtiya/Bahu | pass |
| caitasaiḥ | caitasa | Pum. Trtiya/Bahu | pass |
| asau | adas | Stri. Prathama/Eka | pass |
| saṃprayuktā | saṃprayukta | Stri. Prathama/Eka | pass |
| tathā | tathā | indecl. | pass |
| kleśaiḥ | kleśa | Pum. Trtiya/Bahu | pass |
| upakleśaiḥ | upakleśa | Pum. Trtiya/Bahu | pass |
| trivedanā | trivedanā | Stri. Prathama/Eka; bahuvrihi ⟨tisro vedanāḥ yasyāḥ sā⟩ | pass |

## Justifications

**J1. The series beginning with sarvatragaiḥ is not translated merely as ordinary adjectives such as “all-pervading, restrained, good” nor kleśa as generic “pain”; Sthiramati treats the items beginning with sarvatraga as headings already mentioned and requiring subsequent display.**
- chosen: technical class-names: universal, determinate, wholesome mental factors, afflictions, and secondary afflictions (depends on commentary: **yes**)
- trbh [493]: `ya ete sarvatragādaya uddiṣṭās te na vijñāyanta ity atas tatpradarśanārtham` — Since these, beginning with the sarvatragas, have been stated but are not understood, therefore, for the purpose of displaying them...

**J2. The verse says that the feminine subject is “conjoined/associated” with the listed classes. tathā is therefore taken as “likewise/also,” adding kleśaiḥ and upakleśaiḥ to the same instrumental construction rather than starting an independent clause.**
- chosen: all the instrumental plurals are governed by saṃprayuktā, with tathā continuing the same construction (depends on commentary: **yes**)
- trbh [491, 492]: `sarvatragair viniyataiḥ kuśalaiś caitasair asau | saṃprayuktā tathā kleśair upakleśais trivedanā` — With universal, determinate, and wholesome mental factors this is conjoined; likewise with afflictions and secondary afflictions; it has three feelings.
- trbh [493]: `ya ete sarvatragādaya uddiṣṭās te na vijñāyanta` — These, beginning with the sarvatragas, have been mentioned but are not understood.

**J3. Although asau can be masculine or feminine in form, the feminine nominative predicates saṃprayuktā and trivedanā require the feminine reading here.**
- chosen: asau is feminine nominative singular, with saṃprayuktā and trivedanā as feminine predicates (depends on commentary: no)
- trbh [491, 492]: `caitasair asau | saṃprayuktā ... trivedanā` — this [feminine] is conjoined with mental factors ... [and is] three-feelinged.

**J4. The printed verse has trivedanā as one word, and its feminine nominative singular form agrees predicatively with asau/saṃprayuktā. It is therefore not split as tri + vedanā, nor taken as an independent dvigu noun “the three feelings.”**
- chosen: trivedanā is a bahuvrīhi predicate: “having three feelings” (depends on commentary: no)
- trbh [492]: `saṃprayuktā tathā kleśair upakleśais trivedanā` — conjoined likewise with afflictions and secondary afflictions, [it is] three-feelinged.

## Translation

> With universal (sarvatraga), determinate (viniyata),
and wholesome mental factors (caitasa), this [apprehension] is conjoined;
likewise with afflictions (kleśa) and secondary afflictions (upakleśa):
it has three feelings (tri-vedanā).

## Analyzer disagreements

- viniyataiḥ: the analyzer lemmatized it under viniyam; here it is analyzed as the nominal stem viniyata, Pum Trtiya Bahu, a technical class-name in the verse’s list.
- asau: the analyzer marked nominative masculine singular; agreement with saṃprayuktā and trivedanā requires nominative feminine singular of adas.
- saṃprayuktā: treated here as a subanta past passive participial adjective, Stri Prathama Eka, not as a finite verbal form.
- tri_vedanā: the analyzer split the printed trivedanā into tri + vedanā; here it is one compound, Stri Prathama Eka, a predicative bahuvrīhi.

## One-shot delta

- A commentary-blind rendering could treat sarvatraga, viniyata, kuśala, kleśa, and upakleśa as ordinary dictionary words; Sthiramati’s sarvatragādaya uddiṣṭāḥ shows they are technical headings to be displayed next.
- It could follow the analyzer and make asau masculine; the verse’s feminine predicates require a feminine subject.
- It could split trivedanā into tri + vedanā and translate “three feelings” as an independent noun phrase; the verse requires a predicative compound, “having three feelings.”
- It could over-explain the individual members of these classes from the following verse; line 493 marks verse 9 only as the uddesa/listing whose pradarśana begins next.

## Open questions

- The supplied commentary on this verse does not define the individual items within the sarvatraga and following classes; that exposition begins in the lookahead to the next verse and is not used here as verse-9 evidence.
- The explicit antecedent of asau lies outside this verse’s supplied span; the translation supplies “[apprehension]” only to make the feminine demonstrative intelligible in English.
