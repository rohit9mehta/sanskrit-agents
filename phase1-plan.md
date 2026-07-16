# Phase 1 Plan — Pipeline MVP (weeks 3–8 of the Śāstrārtha plan)

**Goal (plan doc §4, Phase 1):** orchestrate the four-stage loop (ANALYZE →
RETRIEVE → REASON → VERIFY) for single verses, output JSON apparatus + rendered
Markdown, run all 30 Triṃśikā verses, and compare against (a) MITRA Translate,
(b) a raw frontier LLM, (c) Buescher 2007.

**Spec base:** Phase 0 is complete (all deliverables committed; exit criterion
met with the v.2 hand-run). The orchestration requirements are the friction
list in `agent/handrun/v02/notes.md`; this plan turns each item into a
workstream. The hand-run apparatus (`agent/handrun/v02/apparatus.json`) is the
reference output shape and the regression baseline.

---

## Prerequisites — RESOLVED 2026-07-15 (provider decision by Rohit)

1. ~~Anthropic API credential~~ → **OpenAI API key** supplied in `.env`
   (gitignored, never committed). Budget authorized: **< $50**; pipeline
   hard-stops at $25 estimated spend. Reasoner + raw-LLM baseline both use
   the same OpenAI model for a fair A/B.
2. ~~Buescher 2007 typed in by Rohit~~ → **human baseline sourced from the
   web**: find a digitized published scholarly translation of the 30 kārikās
   (Buescher if findable; else another published translation, e.g. Anacker
   1984), fetched from a real URL and stored with full citation + source URL
   in `agent/data/eval/human_baseline.json`. NEVER filled from model memory;
   verses not found online stay "pending". Rohit may supply the physical
   Buescher within a week if web sourcing fails.
3. Optional: a decision on the MITRA baseline if endpoint discovery fails
   (see W5 fallback).

## Design decisions (grounded in Phase 0 + live checks, 2026-07-15)

- **Reasoner: `gpt-5.5-2026-04-23`** (dated snapshot pinned for
  reproducibility; best non-pro flagship on the supplied key, verified via
  `/v1/models`). OpenAI Python SDK, Chat Completions with structured outputs
  (`parse()` + Pydantic schema), `reasoning_effort="high"` where supported,
  no temperature (unsupported on reasoning models).
- **Structured outputs, not tool use.** The loop is code-controlled (a
  workflow, not a model-driven agent): we assemble context, make ONE
  `client.messages.parse()` call with a Pydantic apparatus schema, verify
  claims in code, and make at most one retry call with the vidyut errors
  appended. `parse()` returns a validated object — no JSON scraping.
- **Cost is a non-issue:** ~30 verses × ≤2 calls × (~8k in + ~3k out) ≈
  $4–8 at $5/$25 per MTok, plus ~$1 for the raw-LLM baseline. **No Batch API**
  (saves ~$3, adds async complexity to an iterative loop). **Prompt caching
  on** (stable system prompt with `cache_control`; the retry turn reuses the
  conversation prefix; keep the template free of timestamps).
- **Every LLM request/response cached to disk** (`agent/data/cache/llm/`,
  keyed by payload hash — same pattern as the Dharmamitra client) so reruns
  are reproducible and re-rendering is free.
- **Verification logging continues** in `agent/logs/vidyut_verifications.jsonl`
  with `stage: "pipeline"`, `run_id: "pipeline-v{NN}-{attempt}"` — this log is
  the Phase 3 "Pāṇini as reward function" dataset, so the retry loop must log
  the FAILED first-attempt claims too, not just the final passing ones.

## Workstreams

### W1 — Dictionary module (`agent/src/shastrartha/dictionary.py`)
Replace the ad-hoc Cologne HTML scrape (hand-run friction #2):
- Fetch MW from the `sanskrit-lexicon/csl-json` GitHub repo (verified
  reachable) into `agent/data/raw/mw/` (gitignored, recorded in MANIFEST.md
  with license note); build a lemma→entries index keyed by SLP1, IAST in/out.
- API: `mw_entries(lemma_iast) -> [{text, page_col, ids}]`, citation string
  `MW s.v. X, page,col` baked in.
- Fallback if the bulk fetch disappoints: keep the working
  `getword.php` scrape as a cached secondary path.

### W2 — Claim schema + verify runner (friction #1 and #3)
- Pydantic models mirroring `apparatus.json`: `WordAnalysis` (surface, lemma,
  morph features, optional `samasa` with members+relation+vigraha),
  `Justification` (decision, options, chosen, evidence[{lines, quote}],
  depends_on_commentary), `Apparatus` (verse, analysis[], justifications[],
  translation, one_shot_delta, open_questions). Schema constraints kept
  simple (no unsupported JSON-schema features).
- `verify_compound_claim()` in `verify.py`: whole-inflected-compound as
  opaque stem (prakriya) + relation → `unsupported` + member kosha checks —
  the pattern assembled by hand three times in the hand-run.
- `pipeline_verify(apparatus) -> VerifyReport`: maps every `WordAnalysis` to
  the right verifier (subanta/tinanta/avyaya/compound), returns pass/fail/
  unsupported per word + formatted error feedback for the retry prompt.
  **No silent drops:** a claim the runner cannot express is logged
  `unsupported` with a reason.

### W3 — Retrieval bundle (`agent/src/shastrartha/retrieve.py`; friction #4, #5)
`retrieve(verse_n) -> RetrievalBundle` assembling, from existing artifacts:
- verse text (bhāṣya reading) + vulgate variants from `trimsika.json`;
- anchor lines + commentary span text WITH line numbers from
  `trimsika_alignment.json`, plus a **2–3 line lookahead** past the next
  anchor, marked `[lookahead]` (border-verse fix);
- **requote loci** with ±2 lines of context each, marked `[requote @line]`;
- the `.unsandhied` counterpart of the span (convenience gloss, labeled as
  known-imperfect);
- ANALYZE outputs (local S + SLM on the anchor lines; API cross-check) —
  model kept resident across verses (friction #7);
- MW entries for every SLM lemma (W1).

### W4 — Reasoner + orchestration (`reason.py`, `pipeline.py`, `render.py`)
- `reason.py`: promote `agent/handrun/v02/prompts/reasoner_prompt.md` to
  `agent/prompts/reasoner_v1.md` (versioned; the system prompt is frozen for
  the whole run); assemble user turn from the RetrievalBundle;
  `client.messages.parse(..., output_format=Apparatus)`; handle
  `stop_reason == "refusal"`/`max_tokens` explicitly.
- `pipeline.py`: `run_verse(n)` = retrieve → reason → verify → (if any FAIL:
  one retry turn appending the vidyut error report) → final `Apparatus` with
  per-word verification status; words still failing are flagged
  `UNVERIFIED` in the apparatus rather than dropped.
- `render.py`: apparatus.md from the JSON, mirroring the hand-run format
  (verse / analysis table / justifications / translation / one-shot delta /
  baselines / open questions).
- `scripts/06_run_verse.py N` — single-verse entry point; writes
  `agent/output/v{NN}/apparatus.{json,md}` + raw tool outputs.

### W5 — Full run, baselines, comparison
- `scripts/07_run_all.py`: all 30 verses, resumable (skips verses whose
  apparatus.json exists unless `--force`), progress + cost tally from
  `usage`.
- **Baselines** (`scripts/08_baselines.py`):
  - *raw-LLM*: same model, same translation instruction, verse text ONLY (no
    commentary, no analyses) → `agent/data/eval/raw_llm.json`;
  - *MITRA Translate*: discovery task — inspect dharmamitra.org's frontend
    network calls / dharmamitra GitHub clients for the translation endpoint
    (the obvious `/api/translation/` 404s, checked 2026-07-15). Fallback:
    run the 30 verses manually through the web UI into
    `agent/data/eval/mitra.json`, or defer the column to Phase 2;
  - *Buescher*: read `agent/data/eval/buescher.json` if Rohit has supplied it.
- `scripts/09_compare.py` → `agent/output/comparison.md`: per verse, the four
  translations side by side + which J-objects were commentary-dependent; and
  the aggregate table (verify outcomes by class, commentary-dependent
  decisions per verse, retry rate, token/cost totals). This table is the
  input to Phase 2's human-graded eval and decision gate.

## Acceptance criteria (Phase 1 exit)

1. 30/30 verses have `apparatus.json` + `apparatus.md` with per-word
   verification status; zero silently-dropped claims.
2. Every morphological claim (including failed first attempts) has a record
   in `vidyut_verifications.jsonl` with `stage: "pipeline"`.
3. Each verse has ≥1 justification citing trbh lines, or an explicit
   `no_contested_points` note.
4. `comparison.md` exists with agent + raw-LLM columns populated; MITRA and
   Buescher columns populated or explicitly pending (never fabricated).
5. Pipeline v.2 output is consistent with the hand-run apparatus (regression
   check — same analyses, same J-object citations ±phrasing).

## Verification path (in order, before the full run)

1. Unit-ish: W2 runner on the hand-run's 15 known claims → identical
   outcomes (12 pass / 3 unsupported).
2. Regression: `06_run_verse.py 2` vs `agent/handrun/v02/apparatus.json`.
3. Stress: v.9 (single-line full-verse quote), v.25 (requote-heavy), v.29
   (shared span with v.30), v.7 (truncated pratīka) — eyeball each.
4. Full run + baselines + comparison.

## Risks / fallbacks

- **No API credential** — blocks W4/W5 only; W1–W3 proceed. (Prerequisite #1.)
- **MITRA endpoint unknown** — manual-UI fallback or defer column; the
  decision-gate comparison that matters most (agent vs raw same-model LLM)
  doesn't depend on it.
- **Buescher availability** — Rohit-dependent; column stays pending.
- **SLM analysis errors on rare forms** — the reasoner may override the SLM
  with commentary evidence; when it does, that disagreement is logged in the
  apparatus (`analyzer_disagreement: true`) — valuable eval data, not a bug.
- **Refusals/timeouts** — handled branches in reason.py; at 30 verses,
  rate limits are irrelevant.
- **Cost ceiling** — hard stop in 07_run_all at $25 cumulative (from usage
  accounting); expected spend is ~$5–10.

## Out of scope (later phases)

Strict-checker mode (reject-and-retry-until-derivable), the 3-system human
eval and decision gate (Phase 2); embeddings, Gītā/Nyāya second testbed,
release packaging, the reward-function paper (Phase 3).

## Suggested session breakdown

- **S1:** W1 + W2 (offline; no credential needed) + verification step 1.
- **S2:** W3 + W4 + verification steps 2–3 (needs credential).
- **S3:** W5 full run + baselines + comparison.md.
