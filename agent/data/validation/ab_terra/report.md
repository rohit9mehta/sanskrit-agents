# Lemma-layer validation: stored vs re-run

Re-run model: gpt-5.6-terra (stored: gpt-5.5-2026-04-23)

| unit | overrides old→new | attempts | tokens | est $ | verify (pass/fail/unsup) |
|---|---|---|---|---|---|
| gita:2.19 | 4 → **2** | 2 → 1 | 0 → 0 | 0.3594 → 0.1127 | 16/0/2 → 16/0/2 |
| isa:4 | 2 → **3** | 2 → 2 | 0 → 0 | 0.4157 → 0.2278 | 19/0/0 → 17/1/1 |
| trimsika:10 | 5 → **1** | 2 → 1 | 0 → 0 | 0.4863 → 0.1261 | 10/0/0 → 10/0/0 |

## Remaining disagreements (new run)

### gita:2.19
- For enam, the analyzer cites enad. I cite the nominal lemma idam, the dictionary headword supplied for this demonstrative; enam is its enclitic masculine accusative singular form.
- For ubhau, the analyzer's material links the form to verbal ubh and describes it as a kṛdanta. Here ubhau is instead the masculine nominative dual of the pronominal/adjectival stem ubha, agreeing appositionally with tau;

Lemma citations that changed vs stored: enam: etad → idam

### isa:4
- The analyzer separates anejat into an and ejat. I analyze an- as the privative prefix in the nañ-tatpuruṣa anejat, following the explicit gloss “anejat na ejat” (lines 1–2), rather than as an independent verbal item.
- The analyzer’s local tag for arṣat is nonfinite/nominal in form. arṣat is instead a finite Vedic augmentless imperfect (injunctive), third-person singular active, from ṛṣ; it is not a luṅ/aorist form.
- The analyzer labels apaḥ as feminine plural, which would yield ‘waters.’ I override this: it is neuter accusative plural from Vedic ap ‘work,’ because Śaṅkara explicitly says “apaḥ karmāṇi” (line 13).

Lemma citations that changed vs stored: enat: enad → etad; pūrvam: pūrvam → pūrva; arṣat: arṣat → ṛṣ

### trimsika:10
- adyāḥ: the tagger analyzes this as ad/adya. It is instead ādyāḥ, Prathama Bahu Pum of ādi, as required by Sthiramati's gloss “ādau nirdiṣṭatvād ādyāḥ” (trbh 496).

Lemma citations that changed vs stored: ādyāḥ: ādya → ādi; śraddhā: śraddha → śraddhā; apatrapā: apatrapa → apatrapā
