# Bhagavad-Gītā with Śaṅkara-bhāṣya — 2.47 (commentary-grounded, with apparatus)

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 2, verification: 13 pass / 0 fail / 2 unsupported.

## Verse

> ****

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| karmaṇi | karman | Napumsaka. Saptami/Eka | pass |
| eva | eva | indecl. | pass |
| adhikāraḥ | adhikāra | Pum. Prathama/Eka | pass |
| te | tvad | Pum. Sasthi/Eka | pass |
| mā | mā | indecl. | pass |
| phaleṣu | phala | Napumsaka. Saptami/Bahu | pass |
| kadācana | kadācana | indecl. | unsupported |
| mā | mā | indecl. | pass |
| karma-phala-hetuḥ | karma-phala-hetu | Pum. Prathama/Eka; tatpurusa ⟨karmaṇaḥ phalasya prāpter hetuḥ⟩ | pass |
| bhūḥ | bhū | bhū, Kartari/Lun/Madhyama/Eka | unsupported |
| mā | mā | indecl. | pass |
| te | tvad | Pum. Sasthi/Eka | pass |
| saṅgaḥ | saṅga | Pum. Prathama/Eka | pass |
| astu | as | as, Kartari/Lot/Prathama/Eka | pass |
| akarmaṇi | akarman | Napumsaka. Saptami/Eka; tatpurusa ⟨na karma; akaraṇam⟩ | pass |

## Justifications

**J1. The first pāda is not merely a general statement that action matters; Śaṅkara explicitly construes “karmaṇy eva adhikāraḥ te” as “your adhikāra is only in action,” and adds the exclusion “not in steadfastness in knowledge.”**
- chosen: adhikāra is restricted to karma, with eva excluding jñāna-niṣṭhā (depends on commentary: **yes**)
- gita [1]: `karmaṇy evādhikāro na jñāna-niṣṭhāyāṃ te tava |` — Your adhikāra is only in action, not in steadfastness in knowledge.

**J2. The enclitic te is taken as genitive singular, not dative, because the commentary twice glosses te with tava.**
- chosen: te is genitive, “your” (depends on commentary: **yes**)
- gita [1]: `te tava` — te means tava, “your.”
- gita [5]: `mā te tava saṅgo 'stv akarmaṇi` — Let there not be your attachment to non-action.

**J3. The second clause has an ellipsis: Śaṅkara supplies adhikāro ’stu with phaleṣu and further explains it as the absence of karma-phala-tṛṣṇā, thirst for the fruit of action, in any state whatsoever.**
- chosen: mā phaleṣu means ‘let there be no adhikāra over the fruits,’ i.e. no craving for action-results (depends on commentary: **yes**)
- gita [2]: `tatra ca karma kurvataḥ mā phaleṣu adhikāro 'stu, karma-phala-tṛṣṇā mā bhūt kadācana kasyāṃcid apy avasthāyām ity arthaḥ |` — And there, while you perform action, let there be no adhikāra over the fruits; the meaning is: let there be no craving for the fruit of action ever, in any condition at all.

**J4. The compound is not treated merely as ‘one whose motive is fruit.’ Śaṅkara explains that if thirst for the fruit arises, one becomes the hetu of karma-phala-prāpti; action prompted by that thirst makes one the cause of the fruit of action, namely birth.**
- chosen: karma-phala-hetuḥ is ‘cause of obtaining the fruit of action,’ especially the fruit that is birth (depends on commentary: **yes**)
- gita [3]: `yadā karma-phale tṛṣṇā te syāt tadā karma-phala-prāpter hetuḥ syāḥ, evaṃ mā karma-phala-hetuḥ bhūḥ |` — When thirst for the fruit of action would be yours, then you would be the cause of obtaining the fruit of action; thus, do not become the cause of the fruit of action.
- gita [4]: `yadā hi karma-phala-tṛṣṇā-prayuktaḥ karmaṇi pravartate tadā karma-phalasyaiva janmano hetur bhavet |` — For when one proceeds in action impelled by thirst for the fruit of action, then one would become the cause of birth itself, which is the fruit of action.

**J5. The last prohibition is directed against attachment to not acting. Śaṅkara glosses akarmaṇi as akaraṇe and saṅga as prīti; he frames it against the mistaken thought that if fruit is not desired, painful action should be abandoned.**
- chosen: akarmaṇi means ‘in non-performance,’ and saṅga is ‘attachment/fondness’ (depends on commentary: **yes**)
- gita [5]: `yadi karma-phalaṃ neṣyate, kiṃ karmaṇā duḥkha-rūpeṇa ? iti mā te tava saṅgo 'stv akarmaṇi akaraṇe prītir mā bhūt ||bhgs_2.47||` — If the fruit of action is not desired, what is the use of action, which is of the nature of pain? Thinking thus, let there not be your attachment to non-action, to non-performance; let there be no fondness for it.

## Translation

> Your entitlement (adhikāra) is only with respect to action (karma), not to steadfastness in knowledge (jñāna-niṣṭhā);
never, in any condition, may it be with respect to the fruits.
Do not become the cause of obtaining the fruit of action (karma-phala);
do not let attachment (saṅga) to non-action (akarman), to non-performance, be yours.

## Analyzer disagreements

- ByT5 reports te only as tvad_SG, without explicit case or gender. Śaṅkara’s te tava at lines 1 and 5 fixes the case as Ṣaṣṭhī singular; masculine is supplied contextually from Arjuna as addressee, while the form itself remains gender-common.
- The verifier reported tool_error/unsupported for karma-phala-hetuḥ as a tatpuruṣa compound. This is not taken as a grammatical rejection: the whole compound stem karma-phala-hetu is required by the instructions, and Śaṅkara’s karma-phala-prāpter hetuḥ supports the tatpuruṣa vigraha.

## One-shot delta

- A commentary-blind rendering might take “only over action” as a generic ethic of action, missing Śaṅkara’s explicit exclusion of jñāna-niṣṭhā in this context.
- It might translate “do not be karma-phala-hetuḥ” as only “do not be motivated by results”; Śaṅkara instead explains becoming the cause of obtaining action-fruit, ultimately birth, through fruit-craving.
- It might take akarmaṇi as ‘inaction’ in an abstract philosophical sense or as ‘bad action’; Śaṅkara glosses it concretely as akaraṇa, non-performance, and saṅga as prīti, fond attachment.
