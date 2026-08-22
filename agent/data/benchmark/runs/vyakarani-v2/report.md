# vyakarani-v2 — negative result (2026-08-22)

Hypothesis: v1's regressions on duals/vocatives came from context-free
synthetic items on syncretic surfaces (voc = nom, acc.du = nom.du) teaching an
arbitrary label. Change: drop synthetic items whose surface carries >1 gold
claim (−7,096), repeat context-bearing records ×2 (trainset_v2: 39,283 records).
Run cancelled externally at epoch 2.76/3; evaluated checkpoint-9000 (LR at 8%
of peak — effectively final).

| metric | baseline | v1 | v2 |
|---|---|---|---|
| features-full | 90.1% | **92.5%** | 90.3% |
| lemma | 93.3% | **95.6%** | 95.0% |
| claim | 88.3% | **89.5%** | 87.4% |

Targeted strata did NOT recover: Sambodhana:Eka 78% → 78%, Dvitiya:Dvi 67% → 62%.
Collateral losses where synthetic coverage was doing work: Panchami:Eka 85 → 73%,
Lut:Kartari 100 → 0% (n=2), pipeline-hard 74 → 66%.

Conclusion: the syncretism dip is not label ambiguity in the synthetic set;
the synthetic coverage is valuable. v1 stands as the PoC. Open hypotheses for
v3: (a) the model ignores sentence context for case decisions — try longer
training / a context-emphasising input format; (b) DCS gold itself labels
syncretic forms inconsistently — audit the benchmark's dual/vocative items.
