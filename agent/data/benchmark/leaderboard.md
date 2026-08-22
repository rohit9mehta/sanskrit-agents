# Analyzer leaderboard — analyzer_benchmark_v1 (985 items, frozen 2026-08-21)

features-full = all morph features right; claim = features + lemma. Rows appended by scripts 30/33.

| model | n | features-full | lemma | claim |
|---|---|---|---|---|
| byt5-sanskrit (baseline, learned+positional tag decode) | 985 | 90.1% | 93.3% | 88.3% |
| smoke — plumbing only, 20 steps on 200 ex (NOT a result) | 40 | 0.0% | 0.0% | 0.0% |
| analyzer-v1 — ByT5-Sanskrit SFT on trainset_v1 (3 ep, bf16, A100, 35 min) | 985 | 92.5% | 95.6% | 89.5% |
| analyzer-v2 — v1 recipe minus 7,096 syncretic synthetic items, context ×2; checkpoint 9000/9.8k (run cancelled at 92%) — NEGATIVE: duals/vocatives unchanged, rare cells lost | 985 | 90.3% | 95.0% | 87.4% |
