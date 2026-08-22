# Lemma-layer validation: stored vs re-run

| unit | overrides old→new | attempts | tokens | est $ | verify (pass/fail/unsup) |
|---|---|---|---|---|---|
| gita:2.19 | 4 → **0** | 2 → 1 | 0 → 0 | 0.3594 → 0.1477 | 16/0/2 → 16/0/2 |
| isa:4 | 2 → **2** | 2 → 2 | 0 → 0 | 0.4157 → 0.4143 | 19/0/0 → 19/0/0 |
| trimsika:10 | 5 → **1** | 2 → 1 | 0 → 0 | 0.4863 → 0.3382 | 10/0/0 → 10/0/0 |

## Remaining disagreements (new run)

### gita:2.19

Lemma citations that changed vs stored: enam: etad → enad

### isa:4
- ByT5 segmented anejat as an + ejat and cited ejat; this apparatus treats the printed word as a single nañ-tatpuruṣa/adjectival stem anejat, because the mūla has one word and Śaṅkara glosses ‘anejat na ejat’ (lines 1–2).
- ByT5’s canonical lemma for dhāvataḥ was sarat; this apparatus uses the form-deriving participial stem dhāvat from √dhāv, supported by the surface form and Śaṅkara’s gloss ‘dhāvato drutaṃ gacchataḥ’ (line 11).

Lemma citations that changed vs stored: pūrvam: pūrvam → pūrva

### trimsika:10
- ByT5 analyzes the opening as adyāḥ with lemma adya/ad; Sthiramati’s ādau nirdiṣṭatvād ādyāḥ requires ādyāḥ from ādya ‘first-mentioned.’ I therefore override the analyzer and record the printed form separately as surface_

Lemma citations that changed vs stored: śraddhā: śraddha → śraddhā; apatrapā: apatrapa → apatrapā
