# Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904) — 1.22 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 4 pass / 0 fail / 0 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| mṛdumadhyādhimātratvāt | mṛdu-madhya-adhimātratva | Napumsaka. Panchami/Eka; dvandva ⟨mṛduś ca madhyaś cādhimātraś ca; tad-bhāvaḥ⟩ | pass |
| tataḥ | tatas | indecl. | pass |
| api | api | indecl. | pass |
| viśeṣaḥ | viśeṣa | Pum. Prathama/Eka | pass |

## Justifications

**J1. Translate the compound as “because [that intense ardour] has mild, middling, and extreme degrees,” rather than as an abstract physical softness/middleness/excessiveness.**
- chosen: mṛdu, madhya, and adhimātra are not merely “soft/middle/excessive” in isolation; they mark sub-grades of the already ‘intense’ saṃvega. (depends on commentary: **yes**)
- ys [1]: `mṛdutīvro madhyatīvro 'dhimātratīvra iti.` — “It is ‘mildly intense,’ ‘middling-intense,’ and ‘extremely intense.’”
- ys [3]: `tadviśeṣād api mṛdutīvrasaṃvegasyāsannaḥ tato madhyatīvrasaṃvegasyāsannataraḥ, tasmād adhimātratīvrasaṃvegasyādhimātropāyasyāpy āsannatamaḥ samādhilābhaḥ samādhiphalaṃ ceti.` — “Because of that distinction too, for one whose ardour is mildly intense [samādhi-attainment] is near; for one whose ardour is middling-intense, nearer than that; for one whose ardour is extremely intense and whose means are also extreme, samādhi-attainment and the fruit of samādhi are nearest.”

**J2. Render tato 'pi as “even within that / even there,” not as an unrelated “thereafter also.”**
- chosen: tataḥ api refers back to the immediately preceding tīvra-saṃvega class and means that even within that class there is further differentiation. (depends on commentary: **yes**)
- ys [2, 3]: `tato 'pi viśeṣaḥ. tadviśeṣād api mṛdutīvrasaṃvegasyāsannaḥ tato madhyatīvrasaṃvegasyāsannataraḥ, tasmād adhimātratīvrasaṃvegasyādhimātropāyasyāpy āsannatamaḥ samādhilābhaḥ samādhiphalaṃ ceti.` — “There is a distinction even from/within that. Because of that distinction too, for one whose ardour is mildly intense [attainment] is near; for one whose ardour is middling-intense, nearer than that; from that, for one whose ardour and means are extremely intense, samādhi-attainment and its fruit are nearest.”

**J3. Supply the contextual sense of viśeṣaḥ as a gradation of āsannatā—near, nearer, nearest—in the result.**
- chosen: viśeṣaḥ is specifically a distinction in the nearness of samādhi-attainment and its fruit. (depends on commentary: **yes**)
- ys [3]: `mṛdutīvrasaṃvegasyāsannaḥ tato madhyatīvrasaṃvegasyāsannataraḥ, tasmād adhimātratīvrasaṃvegasyādhimātropāyasyāpy āsannatamaḥ samādhilābhaḥ samādhiphalaṃ ceti.` — “For one whose ardour is mildly intense [samādhi-attainment] is near; for one whose ardour is middling-intense, nearer than that; for one whose ardour is extremely intense and whose means are also extreme, samādhi-attainment and the fruit of samādhi are nearest.”

**J4. Render mṛdumadhyādhimātratvāt as “because of being mild, middling, and extreme / because of the mild-middling-extreme gradation.”**
- chosen: -tvāt is an ablative of cause. (depends on commentary: **yes**)
- ys [3]: `tadviśeṣād api` — “Because of that distinction too.”

## Translation

> Because [that intense ardour] has mild, middling, and extreme degrees, there is a further distinction even within that [in the nearness of samādhi-attainment].

## Analyzer disagreements

- ByT5 segmented mṛdu/madhya/adhimātra as compound-elements plus tvāt_tva_SBNe; I have consolidated the printed word into one neuter ablative singular abstract stem mṛdu-madhya-adhimātratva. This is not a semantic split of four independent words: -tva forms the abstract noun, and Vyāsa’s line 1 supplies the three grade-members as mṛdu-, madhya-, and adhimātra- applied to tīvra.
- Vidyut-prakriya reported a tool_error for deriving mṛdu-madhya-adhimātratva and logged the dvandva relation as unsupported, but gave no contrary derivation; I therefore keep the regular -tva neuter ablative singular and mark the dvandva as an exegetical analysis of the base triad.

## One-shot delta

- A commentary-blind translation might take mṛdu simply as “soft/gentle” and adhimātra as “excessive,” missing that Vyāsa reads all three as sub-degrees of the prior tīvra-saṃvega: mildly intense, middling-intense, and extremely intense.
- It might render tato 'pi mechanically as “after that also,” whereas Vyāsa uses it to mark a further distinction even within the class just mentioned.
- It might leave viśeṣaḥ as a vague “difference”; Vyāsa specifies the difference as near/nearer/nearest attainment of samādhi and its fruit.
