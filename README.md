# Śāstrārtha — a commentary-grounded, grammar-verified translation agent for Sanskrit

Frontier LLMs and dedicated MT systems translate hard Sanskrit — śāstra,
philosophical verse, layered compounds — in one shot from parametric memory,
and fail on exactly the cases where the tradition already wrote the answer
down. This agent translates the way a trained paṇḍita reads:

1. **ANALYZE** — segment and tag the verse with
   [ByT5-Sanskrit](https://huggingface.co/chronbmm/sanskrit5-multitask)
   (EMNLP Findings 2024);
2. **RETRIEVE** — pull the verse's *own commentary* (aligned by a
   pratīka-matcher), plus Monier-Williams entries;
3. **REASON** — a frontier LLM drafts the translation as a structured
   *apparatus*: every contested choice carries a justification citing the
   commentary by line number;
4. **VERIFY** — every morphological claim is checked against Pāṇinian
   grammar with [vidyut-prakriya](https://github.com/ambuda-org/vidyut);
   failures are fed back for one revision, and anything still unverified is
   flagged, never hidden.

**No bare translations**: the output is translation + apparatus, and every
Vidyut verification outcome (pass/fail/unsupported) is logged — that log is
the seed corpus for a planned "Pāṇini as reward function" study.

## Status

**Testbed**: Vasubandhu's *Triṃśikā* (30 verses) with Sthiramati's bhāṣya.

- **Phase 0 (complete)** — toolbox sanity checks; mūla built from GRETIL
  with variant readings; pratīka-matcher aligning all 30 kārikās to their
  commentary spans (validated 72/72 quote units against a projected gold
  standard); one verse hand-run end to end.
- **Phase 1 (complete)** — full pipeline over all 30 verses:
  **328 word-claims pass / 0 fail / 5 unsupported**, 184 justification
  objects (182 commentary-dependent), compared four ways against a raw
  same-model LLM, MITRA translate, and a published human translation.
  See [`agent/output/comparison.md`](agent/output/comparison.md).
- **Phase 2 (next)** — human-graded eval on term fidelity and compound
  resolution; decision gate.

Plans: [`commentary-grounded-translation-plan.md`](commentary-grounded-translation-plan.md)
(project) and [`phase1-plan.md`](phase1-plan.md) (pipeline MVP).

## Example (v.17, `agent/output/v17/`)

> **agent** — "This transformation of consciousness (vijñānapariṇāma) is
> conceptual construction (vikalpa): whatever object is imagined by it —
> that is not there. Therefore all this is representation-only
> (vijñaptimātraka), **'all' meaning the three realms and the
> unconditioned**."

That last clause is Sthiramati's gloss (trbh 1121–1126), cited in the
apparatus; the raw-LLM and MT baselines translate the bare verse. The
apparatus records six justification objects for this verse, each quoting
the bhāṣya lines it rests on, and a Pāṇinian derivation trace for every
inflected form (e.g. `vikalpyate` verified as *karmaṇi* laṭ — vi-√kḷp-ṇic —
independently confirming the reasoner's voice analysis).

## Running it

```sh
cd agent
uv sync --group ml                      # python 3.13; torch/transformers for local ByT5
uv run python scripts/00_setup_check.py # env + data sanity
uv run python scripts/10_build_mw.py    # fetch + index Monier-Williams (~50 MB, one-time)
echo 'OPENAI_API_KEY=sk-...' > ../.env  # reasoner credential (gitignored)
uv run --group ml python scripts/06_run_verse.py 2   # one verse
uv run --group ml python scripts/07_run_all.py       # all 30 (cost-capped)
```

Vidyut data (~32 MB) and the ByT5 model (~2.3 GB) download on first use.
Scripts `01–05` reproduce the Phase 0 artifacts (sanity checks, mūla,
alignment, gold-projection validation).

## Layout

```
agent/src/shastrartha/   texts, normalize, match (pratīka-matcher), analyze,
                         dictionary (MW), schema, reason, runner, pipeline, render
agent/scripts/           00–11: setup, sanity, mūla, alignment, gold check,
                         run-verse, run-all, baselines, compare, MW build, tests
agent/output/            30 apparatuses + comparison.md
agent/data/              mula, alignment, eval baselines, manifests
agent/logs/              vidyut_verifications.jsonl (append-only), LLM usage
agent/handrun/v02/       Phase 0 manual run of the full loop
data/input/              Triṃśikā-bhāṣya e-text (see licenses below)
code/                    2018 Hellwig–Nehrdich splitter fork (reference only)
```

## Licenses & attribution

**Code**: MIT (see `LICENSE`).

**Data** carries its own terms:

- `data/input/trbh.txt(.unsandhied)` and `agent/data/mula/trimsika.json`
  derive from **GRETIL** e-texts (Triṃśikāvijñaptibhāṣya input by Takamichi
  Fukita & Klaus Wille after Buescher's 2007 edition; kārikās by the Digital
  Sanskrit Buddhist Canon project) — **CC BY-NC-SA 4.0**.
- The human-baseline translation (`agent/data/eval/human_baseline.json`) is
  by **Dharmavardhana Jñānagarbha (Mattia Salvini)**, *Ācārya Vasubandhu's
  Thirty Verses: A Manual for Students*, Saugatam 2022 — a Dharma
  publication "to be distributed freely, at no cost"; full citation inside
  the file.
- MITRA baseline outputs were produced by the
  [Dharmamitra](https://dharmamitra.org) cat-translate API.
- Monier-Williams data is fetched at build time from the
  [Cologne Digital Sanskrit Dictionaries](https://www.sanskrit-lexicon.uni-koeln.de/)
  (not redistributed in this repo).
- Grammar engine: [Vidyut](https://github.com/ambuda-org/vidyut) (Ambuda);
  analyzer: ByT5-Sanskrit by Sebastian Nehrdich et al.

Built on the evidence that commentaries resolve precisely the phenomena
where all current MT fails (Mitrasaṃgraha, arXiv 2601.07314; IndicParam,
arXiv 2512.00333; "Still Not There", arXiv 2511.08145).
