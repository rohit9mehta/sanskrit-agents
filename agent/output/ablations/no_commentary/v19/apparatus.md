# Triṃśikā v.19 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 10 pass / 0 fail / 0 unsupported.

## Verse

> **karmaṇo vāsanā grāhadvayavāsanayā saha | kṣīṇe pūrvavipāke 'nyaṃ vipākaṃ janayanti tat**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| karmaṇaḥ | karman | Napumsaka. Sasthi/Eka | pass |
| vāsanāḥ | vāsanā | Stri. Prathama/Bahu | pass |
| grāhadvayavāsanayā | grāhadvayavāsanā | Stri. Trtiya/Eka; tatpurusa ⟨grāhadvayasya vāsanā; grāhadvaya = grāhayoḥ dvayam⟩ | pass |
| saha | saha | indecl. | pass |
| kṣīṇe | kṣīṇa | Pum. Saptami/Eka | pass |
| pūrvavipāke | pūrvavipāka | Pum. Saptami/Eka; karmadharaya ⟨pūrvo vipākaḥ⟩ | pass |
| anyam | anya | Pum. Dvitiya/Eka | pass |
| vipākam | vipāka | Pum. Dvitiya/Eka | pass |
| janayanti | jan | jan, Kartari/Lat/Prathama/Bahu | pass |
| tat | tad | Napumsaka. Dvitiya/Eka | pass |

## Justifications

**J1. The printed/sandhi form vāsanā is read as underlying vāsanāḥ, not as nominative singular vāsanā, because the finite verb janayanti is plural.**
- chosen: vāsanāḥ as nominative plural subject of janayanti (depends on commentary: no)
- trbh []: `vāsanā ... janayanti` — “impressions … generate”; the plural verb points to a plural subject.

**J2. saha is construed with the instrumental singular grāhadvayavāsanayā. The compound is read as a genitive tatpuruṣa: the vāsanā belonging to grāhadvaya.**
- chosen: grāhadvayavāsanayā saha = “together with the impression of the twofold grasping” (depends on commentary: no)
- trbh []: `grāhadvayavāsanayā saha` — “together with the impression of the twofold grasping.”

**J3. Both kṣīṇe and pūrvavipāke are masculine/neuter-form locative singulars; with vipāka treated lexically as masculine, kṣīṇe agrees with pūrvavipāke and forms a temporal locative absolute: “when the former maturation has been exhausted.”**
- chosen: kṣīṇe pūrvavipāke as locative absolute (depends on commentary: no)
- trbh []: `kṣīṇe pūrvavipāke` — “when the former maturation/result has been exhausted.”

**J4. The supplied bhāṣya reading has anyaṃ vipākam. Since vipāka is masculine in the dictionary and in the analyzer output, anyaṃ is read as masculine accusative singular agreeing with vipākam.**
- chosen: anyaṃ vipākam as masculine accusative phrase (depends on commentary: no)
- trbh []: `'nyaṃ vipākaṃ` — “another maturation.”

**J5. tat is analyzed as neuter accusative singular of tad. Because vipākam is masculine, tat cannot simply be an agreeing adjective of vipākam. A grammatical construal is: janayanti tat anyaṃ vipākam, “they generate that as another maturation,” with anyaṃ vipākam functioning predicatively/appositionally.**
- chosen: tat as a separate neuter accusative pronoun (depends on commentary: no)
- trbh []: `'nyaṃ vipākaṃ janayanti tat` — “they generate that as another maturation.”

## Translation

> Impressions (vāsanāḥ) of action (karman),
together with the impression of the twofold grasping (grāha-dvaya),
when the former maturation (vipāka) has been exhausted,
generate that as another maturation.

## Analyzer disagreements

- vāsanā: ByT5 local_SLM gives vāsanā_SNF, i.e. nominative singular feminine. I override to vāsanāḥ, nominative plural feminine, because vāsanāḥ before gr- can appear as vāsanā by external sandhi and because janayanti is 3rd plural.
- kṣīṇe: ByT5 lemmatizes the form as kṣi. For the required nominal analysis I give the inflected participial/adjectival stem kṣīṇa, masculine locative singular, agreeing with pūrvavipāke.

## One-shot delta

- A parser may take the printed vāsanā as singular and miss that the plural verb janayanti requires underlying vāsanāḥ.
- The vulgate-like anyad-vipākam reading would encourage a neuter or compound analysis; the supplied bhāṣya reading supports anyaṃ vipākam as a masculine accusative phrase.
- The final tat is easy either to omit in translation or to force into agreement with vipākam; grammatically it is better treated as a separate neuter accusative pronoun, though its antecedent needs wider context.

## Open questions

- Without commentary or the preceding verse supplied in this run, the exact antecedent of tat cannot be fixed with certainty from this verse alone.
- The technical identity of grāhadvaya—e.g. which two graspings are intended—can be inferred lexically as “twofold grasping,” but not specified further without commentary.
