# Lemma-layer validation: stored vs re-run

Re-run model: gpt-5.6-sol (stored: gpt-5.5-2026-04-23)

| unit | overrides old→new | attempts | tokens | est $ | verify (pass/fail/unsup) |
|---|---|---|---|---|---|
| gita:2.19 | 4 → **0** | 2 → 1 | 0 → 0 | 0.3594 → 0.2103 | 16/0/2 → 16/0/2 |
| isa:4 | 2 → **3** | 2 → 2 | 0 → 0 | 0.4157 → 0.4658 | 19/0/0 → 18/1/0 |
| trimsika:10 | 5 → **0** | 2 → 1 | 0 → 0 | 0.4863 → 0.3007 | 10/0/0 → 10/0/0 |

## Remaining disagreements (new run)

### gita:2.19

Lemma citations that changed vs stored: enam: etad → enad

### isa:4
- arṣat: the analyzer labels it a neuter accusative singular present participle. It is instead analyzed as a finite Vedic augmentless imperfect (injunctive), third-person singular Kartari; Śaṅkara paraphrases pūrvam arṣat 
- tat: the analyzer selects neuter accusative singular. It is nominative singular, the subject of atyeti; the nominative and accusative forms are syncretic, but the syntax and commentary at line 11 require the nominative c
- tiṣṭhat: the analyzer selects neuter accusative singular. It is nominative singular agreeing with subject tat; Śaṅkara explains that it indicates the Self itself remains changeless (line 12).

Lemma citations that changed vs stored: anejat: anejat → ejat; pūrvam: pūrvam → pūrva; arṣat: arṣat → ṛṣ

### trimsika:10

Lemma citations that changed vs stored: śraddhā: śraddha → śraddhā; apatrapā: apatrapa → apatrapā
