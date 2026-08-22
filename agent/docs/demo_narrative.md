# Śāstrārtha — demo narrative (draft, 2026-08-22)

Audience: Sanskrit/NLP researchers and potential funders. Goal: show a working,
auditable system and invite collaboration on the research thread. Every number
below is reproducible from the repo; the caveats are part of the script, not an
appendix.

## One-sentence version

A translation agent for hard Sanskrit that reads the text's own commentary
before it translates, proves every grammatical claim with a Pāṇinian derivation
engine, shows its evidence with line-cited quotes — and whose grammar checker
turned out to be a teacher: it generated the data that taught an analyzer
categories the state-of-the-art model could not express.

## The problem (30 seconds)

Frontier LLMs and specialised Sanskrit models fail on the same things: long
compounds, philosophical terms, layered metaphor, and *who is speaking*
(benchmarks: Mitrasaṃgraha, IndicParam, "Still Not There"). Traditional
commentaries resolve exactly these — they split the compounds, gloss the
terms, and mark the opponent's view — and no system reads them at inference
time. Google-Translate-style MT guesses from training data; we want a system
that *reasons from the text's own exegesis and can be audited*.

## Beat 1 — Commentary-grounded translation with an apparatus (the product)

Show one verse (Triṃśikā 2 or Gītā 2.47). Walk the apparatus:

* word-by-word analysis (stem/root, case/tense) — every line carries a
  verification status from the Pāṇinian engine
* the commentary passages the decision rests on, with **line numbers into the
  source file** — click through
* "what a commentary-blind translation gets wrong" (one-shot delta)

Numbers to say out loud: 4 texts, 4 commentators (Sthiramati, Śaṅkara ×2,
Vyāsa), 171 units; 182 of 184 interpretive decisions on the Triṃśikā depended
on the commentary; citation audit: 304 quotes, **0 fabricated**.

Honest line: "Whether these translations are *better* is being judged by
Sanskrit readers in a blinded comparison against a raw LLM, a specialised
model, and a published human translation. The result is pending / is X."

## Beat 2 — Verification: the grammar is proved, not guessed

The analyzer claims "*vijñānapariṇāme* is locative singular of
*vijñāna-pariṇāma*". We hand stem + features to vidyut-prakriya and ask it to
**derive** the form by applying Pāṇini's rules. If the derivation produces
the word in the text, the claim passes; if not, the reasoner gets the error
back and retries once. Phase 1: 328 pass / 0 fail / 5 unsupported. Every
outcome is logged — 10,000+ verification records to date.

What this buys: an LLM cannot self-certify its grammar. A rule engine can.
The limits are stated on screen: compound *relations* are verified member by
member (the engine's samāsa coverage is partial); Vedic injunctives and a few
classes come back `unsupported`, not `pass`.

## Beat 3 — The verifier is also a teacher (the research invitation)

This is the part for researchers.

1. **Audit the analyzer.** We benchmarked the SOTA Sanskrit analyzer
   (ByT5-Sanskrit) on a frozen, checksummed 985-item test set built from
   vidyut-verified gold (our pipeline's hard cases + a genre-stratified DCS
   sample whose coarse tags vidyut *arbitrated* by derivation). Overall it is
   good: 90.1% morph-features-correct. But its tagset inherits DCS's coarse
   "past" — **it structurally cannot say aorist vs perfect vs imperfect**.
   Aorist accuracy: 5%. Periphrastic future: 0%.
2. **Manufacture the data.** The verifier derives forms; run it *forward* and
   it is a gold-data generator: 34,719 derivation-labelled pairs, flat across
   all 10 lakāras × 3 prayogas — including categories no corpus attests in
   quantity. Plus 13,065 vidyut-confirmed DCS claims and our own hard cases.
3. **Teach the student.** Fine-tune ByT5-Sanskrit to emit our explicit schema
   (`pos=tinanta root=gam lakara=Lun …`). 35 minutes on one A100, ~$2.
4. **Grade on the sealed exam.** `analyzer-v1`: features 90.1 → 92.5%, lemma
   93.3 → 95.6%, full claim 88.3 → 89.5%. **Aorist 5% → 80%. Periphrastic
   future 0 → 100%.** Our in-domain hard cases 69 → 74%.
   Regressions we understand: duals and vocatives dipped — syncretic forms
   where the model defaults to nominative. We tested the obvious explanation
   (ambiguous context-free synthetic labels) with a v2 run that removed them:
   it did NOT help (duals/vocatives unchanged) and cost accuracy where the
   synthetic coverage was working (features 92.5 → 90.3%). v1 stands; the
   dip is an open question worth saying out loud — it is what the next
   iteration is for.

Say plainly: the headline moved a little because the common cells were
already 88–100%; the structural cells moved a lot because the baseline was
blind there. This is a proof of the loop — *verifier → data → model →
verifier* — not a claim that translation quality rose. The next step is the
obvious one: use the verifier's pass/fail as the **reward** (rejection
sampling / RL), the "Pāṇini as reward function" thread. Everything needed —
benchmark, generator, trainer, launcher — is in the repo and runs for dollars.

Invitation: collaborators who want to (a) extend the verifier's coverage
(samāsa relations, Vedic), (b) run the RL loop, (c) bring a text + commentary
and test whether grounding generalises to their genre.

## Beat 4 — Ask the library (30 seconds)

Type a question. The answer is composed only from retrieved, verified
apparatus passages, every claim with a clickable citation; if the library
doesn't cover it, it says so *without calling the model*; any citation the
model invents is flagged, never shown silently. Run a question it can answer
and one it can't ("what are the chakras" → "not on my shelf").

## Caveats to volunteer before anyone asks

* Human evaluation is pending / single-grader (state it).
* Library is 4 texts — a demonstration, not a corpus.
* Analyzer training improves the analyzer, not the translations; the
  pipeline's real bottleneck is interpretive (46% of reasoner overrides are
  compound-boundary decisions the commentary settles).
* The reasoner is an API model (GPT-5.6); the verifier, retrieval, citation
  audit, and benchmark are ours and open.

## Numbers sheet (for slides)

| item | value |
|---|---|
| texts / commentators / units | 4 / 4 / 171 |
| Triṃśikā word-claims verified | 328 pass / 0 fail / 5 unsupported |
| citation audit | 304 quotes, 0 fabricated |
| verification records logged | 10,768 |
| analyzer benchmark | 985 items, frozen, sha256 in MANIFEST |
| ByT5 baseline | 90.1% features / 88.3% claim; aorist 5% |
| analyzer-v1 | 92.5% / 89.5%; aorist 80%; Luṭ 100% |
| synthetic gold | 34,719 pairs, flat over 30 tense×voice cells |
| DCS arbitrated gold | 13,065 claims |
| lemma-normalization | reasoner overrides −60% on re-run; cost −37% |
| cost of the training run | ~$2 (A100, 35 min) |
