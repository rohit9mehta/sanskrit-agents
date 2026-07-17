# Triṃśikā v.1 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 11 pass / 0 fail / 0 unsupported.

## Verse

> **ātmadharmopacāro hi vividho yaḥ pravartate vijñānapariṇāme 'sau pariṇāmaḥ sa ca tridhā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| ātmadharmopacāraḥ | ātmadharmopacāra | Pum. Prathama/Eka; tatpurusa ⟨ātmā ca dharmāś ca, teṣām upacāraḥ⟩ | pass |
| hi | hi | indecl. | pass |
| vividhaḥ | vividha | Pum. Prathama/Eka | pass |
| yaḥ | yad | Pum. Prathama/Eka | pass |
| pravartate | vṛt | pra-vṛt, Kartari/Lat/Prathama/Eka | pass |
| vijñānapariṇāme | vijñānapariṇāma | Pum. Saptami/Eka; tatpurusa ⟨vijñānasya pariṇāmaḥ⟩ | pass |
| asau | adas | Pum. Prathama/Eka | pass |
| pariṇāmaḥ | pariṇāma | Pum. Prathama/Eka | pass |
| saḥ | tad | Pum. Prathama/Eka | pass |
| ca | ca | indecl. | pass |
| tridhā | tridhā | indecl. | pass |

## Justifications

**J1. The final member upacāraḥ is the singular masculine head; ātma- and dharma- are best taken as the objects/topics of that upacāra. Grammatically I construe the whole as an external ṣaṣṭhī-tatpuruṣa with an internal coordination: ātmā ca dharmāś ca, teṣām upacāraḥ.**
- chosen: ātmadharmopacāraḥ means a usage/attribution concerning self and dharmas, not “a property of the self” or “service to the self’s dharma.” (depends on commentary: no)
- trbh []: `No trbh commentary used. Grammar/dictionary basis: upacāra is a masculine nominal head; ātma- and dharma- are prior compound members; vividhaḥ and yaḥ agree with the resulting masculine nominative singular compound.` — The compound is read as “the manifold upacāra of/with respect to self and dharmas.”

**J2. The middle present form pravartate from pra-√vṛt commonly functions intransitively. The nominative subject is the relative phrase yaḥ ātmadharmopacāraḥ vividhaḥ.**
- chosen: pravartate is intransitive kartari: “proceeds, occurs, comes into operation.” (depends on commentary: no)
- trbh []: `No trbh commentary used. Grammar/dictionary basis: MW gives pra-√vṛt Ā. -vartate with senses such as “proceed,” “arise,” “occur,” “take place.”` — The verse says that the manifold upacāra occurs/proceeds; it does not say that something else sets it in motion.

**J3. The compound is naturally genitival, vijñānasya pariṇāmaḥ. The locative supplies the domain or locus for pravartate.**
- chosen: vijñānapariṇāme is a locative singular tatpuruṣa: “in the transformation of consciousness.” (depends on commentary: no)
- trbh []: `No trbh commentary used. Grammar/dictionary basis: pariṇāma is a masculine noun “change, alteration, transformation”; vijñāna is a neuter noun “consciousness/knowledge”; the form -e is locative singular of the masculine compound.` — The manifold upacāra proceeds in/with respect to the transformation of consciousness.

**J4. Although asau could grammatically point back to the nominative ātmadharmopacāraḥ, the immediate repetition of pariṇāmaḥ after the locative vijñānapariṇāme makes it more economical to take asau pariṇāmaḥ as resuming the transformation just mentioned; saḥ then resumes pariṇāmaḥ before tridhā.**
- chosen: asau pariṇāmaḥ sa ca tridhā is an elliptical nominal sentence: “that transformation is threefold.” (depends on commentary: no)
- trbh []: `No trbh commentary used. Grammar basis: asau and saḥ are masculine nominative singular demonstratives, and pariṇāmaḥ is also masculine nominative singular; Sanskrit nominal sentences commonly omit asti.` — The second half classifies the transformation just named: it is threefold.

## Translation

> For the manifold usage/attribution (upacāra)
of self (ātman) and dharmas (dharma), which proceeds
in the transformation of consciousness (vijñāna-pariṇāma):
that transformation (pariṇāma) is threefold.

## Analyzer disagreements

- No substantive disagreement with the ByT5 features. Normalization: ByT5 reports pravartate_pravṛt; per the requested format this is recorded as bare root vṛt with prefix pra.
- No substantive disagreement with the compound segmentation. Normalization: ByT5 segments ātma_dharma_upacāraḥ, while the apparatus gives the inflected nominal’s lemma as the whole compound stem ātmadharmopacāra and records the samāsa separately.
- No substantive disagreement with the compound segmentation. Normalization: ByT5 segments vijñāna_pariṇāme, while the apparatus gives the inflected nominal’s lemma as the whole compound stem vijñānapariṇāma and records the samāsa separately.

## One-shot delta

- Because this is deliberately commentary-blind, the technical value of upacāra is not secured from the bhāṣya. A purely dictionary-led rendering might produce the unsuitable “service/attendance”; I have used the broader philosophical “usage/attribution” while marking the Sanskrit.
- A commentary-blind reader may take ātmadharma as “the dharma/property of the self.” The translation instead takes ātman and dharma as coordinated topics, “self and dharmas,” but this remains a grammatical choice without commentary confirmation.
- The demonstrative asau could be attached to ātmadharmopacāraḥ by gender and number alone. The translation takes it to resume pariṇāma, because the verse immediately repeats pariṇāmaḥ and then says sa ca tridhā.
- Without the commentary or the following verse, the contents of the “threefold” division are not supplied here; the translation therefore does not name the three transformations.

## Open questions

- Whether upacāra should be translated more specifically as “metaphorical designation” or “imputation” requires commentary evidence not available in this ablation run.
- Whether ātmadharma must doctrinally mean “self and dharmas” rather than any alternative compound relation would be confirmed by the bhāṣya or broader Yogācāra context.
- The verse states that the transformation is threefold, but the three members are not identified within this verse alone.
