# Śāstrārtha: A Commentary-Grounded, Grammar-Verified Translation Agent for Sanskrit

*Working plan — July 2026. Assumes solo, part-time work with open components; no institutional dependencies.*

---

## 1. What this is, in one paragraph

An agent that translates hard Sanskrit (śāstra, commentary, philosophical verse) the way a trained paṇḍita does: it segments and parses the verse with tools, retrieves the traditional commentaries that gloss it, mechanically verifies its own morphological claims against Pāṇinian grammar, and outputs a translation **with a cited justification for every contested choice** — which compound analysis it took, which commentator it followed, and why. Every existing system (Dharmamitra's MITRA, Google, Claude, GPT) translates in one shot from parametric memory and fails on exactly the cases where the tradition already wrote the answer down.

## 2. Why it matters (the impact story)

- **It attacks the field's admitted #1 open problem.** The Jan 2026 Mitrasaṃgraha paper (Nehrdich, Keutzer, et al.) explicitly names complex compounds, philosophical terminology, and layered metaphor as unsolved. Commentaries exist *precisely to resolve these* — bhāṣyas gloss compounds word by word. Nobody has closed that loop.
- **It converts MT from "draft tool" to "auditable scholarship."** Scholars don't distrust MT because it's wrong sometimes; they distrust it because it can't say *why*. A translation with a per-decision apparatus (analysis, commentarial citation, grammar check) is something a Sanskritist can verify, correct, and cite.
- **The exhaust is as valuable as the engine.** Building it forces creation of a verse-aligned root-text↔commentary dataset and a corpus of tool-verified reasoning traces — both are training data for the next generation of models, and neither exists today.
- **It's the missing evaluation lens.** The agent's disagreements with baseline MT, adjudicated against commentaries, is itself a new benchmark: "translation faithfulness under commentarial ground truth."
- **Uniqueness of Sanskrit as a domain.** Among all ancient languages, only Sanskrit has (a) a complete formal generative grammar (Aṣṭādhyāyī) with working code implementations, and (b) an unbroken 2,000-year native tradition of self-annotation. This project is the first to use both as *agent tools* rather than trivia.

## 3. Architecture

```
Input verse (IAST/Devanagari)
   │
   ├─ 1. ANALYZE      ByT5-Sanskrit multitask (pip: dharmamitra-sanskrit-grammar):
   │                  segmentation, lemmata, morphosyntax → candidate analyses
   │
   ├─ 2. RETRIEVE     MITRA-E embeddings + BM25 hybrid over:
   │                  • the text's own commentary stack (bhāṣya/ṭīkā), verse-aligned
   │                  • parallel passages (MITRA-parallel, DharmaNexus)
   │                  • dictionary entries (Monier-Williams, Apte)
   │
   ├─ 3. REASON       Frontier LLM agent loop: reconcile analyses with commentarial
   │                  glosses; identify contested points; choose readings; draft
   │                  translation with inline justification objects
   │
   ├─ 4. VERIFY       • Vidyut-prakriya as derivation checker: every claimed form
   │                    must be derivable (tiṅanta/kṛdanta/subanta coverage is good)
   │                  • Consistency check: does the translation entail the chosen
   │                    compound analysis? (LLM-as-checker with the analysis as spec)
   │                  • Failures loop back to step 3 with the error as feedback
   │
   └─ OUTPUT          Translation + apparatus: per-word analysis, commentary
                      citations, grammar-check status, flagged uncertainties
```

The **verify** step is the embedded seed of the grammar-as-reward-model research thread: log every verification outcome. After a few hundred verses you'll know empirically whether the signal is strong enough to train against (rejection sampling / RL) — that's the follow-on paper.

## 4. Build plan

### Phase 0 — Testbed and alignment (weeks 1–3)
- **Testbed text: Triṃśikā + Sthiramati's bhāṣya.** You already have the bhāṣya segmented from 2022 (`trbh.txt.unsandhied`); the root text is 30 verses; a scholarly English translation (Buescher 2007) exists for evaluation. Poetic and practical.
- Build the **verse↔commentary aligner**: commentaries quote the mūla in pratīka form ("pudgaladharma... iti"); combine pratīka string-matching with MITRA-E similarity. This tool is reusable across every text and is a shareable artifact by itself.
- Wire up the toolbox: `dharmamitra-sanskrit-grammar`, `vidyut-prakriya` (Python bindings), MW dictionary lookup, embedding index over the bhāṣya.

### Phase 1 — Pipeline MVP (weeks 3–8)
- Implement the four-stage loop above for single verses. Frontier LLM (Claude/GPT) as the reasoner; everything else is tools.
- Output format: JSON apparatus + rendered Markdown ("verse / analysis / commentary evidence / translation / confidence").
- Run all 30 Triṃśikā verses. Compare against (a) MITRA Translate, (b) raw frontier LLM, (c) Buescher's human translation.

### Phase 2 — Verification & measurement (weeks 8–12)
- Turn Vidyut into a strict checker: reject analyses whose forms aren't derivable; log every rejection and retry.
- Small human-graded eval: 30 verses × 3 systems, graded on term fidelity and compound resolution (recruit 1–2 Sanskrit readers; the Sanskrit-programmers and academic Twitter communities will help).
- **Decision gate:** does commentary-grounding measurably beat one-shot MT on the hard cases? If yes → Phase 3. If marginal → the diagnosis of *why* is still a publishable/postable finding.

### Phase 3 — Scale and share (months 3–6)
- Second testbed with a deeper commentary stack: Bhagavad-gītā (Śaṅkara + Rāmānuja — famous *disagreements*, so the agent can surface "Śaṅkara reads X, Rāmānuja reads Y") or a Nyāya text for maximal compound difficulty.
- Release: repo, dataset, demo, writeup (see §6).
- Follow-on research thread: use the accumulated verify-step logs to test grammar-verifier-guided rejection sampling on an open model (Gemma-2-MITRA) — the "Pāṇini as reward function" paper.

## 5. Differentiators (vs. everything that exists)

| Existing | This project |
|---|---|
| MITRA / Google / frontier LLMs: one-shot translation from parametric memory | Multi-step agent that *reads the tradition* before translating |
| RAG-over-scripture apps (GitaGPT etc.): retrieve *translations* for QA | Retrieves *primary commentaries* to resolve source-language ambiguity |
| Dharmamitra Deep Research: retrieval as context | Per-decision citations + mechanical grammar verification — an auditable apparatus, not just context |
| ByT5/Vidyut: standalone analyzers | Same tools composed into a closed reasoning loop with verification feedback |
| All MT evaluation: BLEU/chrF/LLM-judge | New eval dimension: faithfulness against commentarial ground truth |

No one — including Dharmamitra, per their own July 2026 roadmap ("agentic philology": announced, not delivered) — has shipped this. The window is open but probably not for long.

## 6. Sharing strategy

**Open source everything (MIT/Apache for code, CC BY-SA for data — matching Dharmamitra's norms).** The audiences and channels, in order:

1. **GitHub repo** with a killer README: one animated/screenshot example of a verse → apparatus → translation, before/after vs. GPT-5 and MITRA. The repo *is* the pitch.
2. **Hugging Face**: the aligned Triṃśikā↔bhāṣya dataset + eval set as a dataset card. Datasets get discovered and cited; this makes you a node in the ecosystem.
3. **X/Twitter thread**: the compelling artifact is a side-by-side — "GPT-5 translates this Yogācāra compound wrong; here's the agent citing a 6th-century commentator and getting it right, with the derivation checked against Pāṇini." That's a genuinely novel demo at the AI×humanities intersection, which travels extremely well on X (cf. Vesuvius Challenge, Aeneas). Tag the ecosystem: Dharmamitra, Ambuda/Vidyut (Arun Prasad), AI4Bharat folks.
4. **Interactive demo** (simple web page, even static): paste a Gītā verse, watch the agent work. Demos convert skeptics.
5. **Workshops/venues** if you want the academic stamp: **ML4AL** (Machine Learning for Ancient Languages, ACL workshop), **NLP4DH**, **ISCLS 2026+** (the computational Sanskrit home venue), WSC's CSDH track. A workshop paper is very achievable from Phase 2 results.
6. **Reconnect with Nehrdich/Keutzer** — with the working prototype, not before. They're funded to move toward agentic philology and a knowledge graph; a demonstrated commentary-grounding pipeline is exactly the collaboration ticket, and Keutzer already knows you.

**Positioning line:** *"The first translation system that reads the commentaries — every translation ships with its evidence."*

## 7. Risks and honest caveats

- **Digitized commentary availability** is the binding constraint at scale. Mitigation: start where digitization is best (Yogācāra corpus, Gītā commentaries, Vedānta prasthānatrayī — all on GRETIL/DCS).
- **Vidyut's samāsa coverage is partial** — and compounds are the heart of the problem. Mitigation: verify the *members* of compounds (well-covered) and use the LLM-consistency check for the compound relation itself; contribute upstream if gaps block you.
- **Commentators can disagree or be "wrong."** That's a feature — surface the disagreement — but it complicates "ground truth" evaluation. Define fidelity as "consistent with a cited commentarial reading," not "matches one true answer."
- **Latency/cost:** the loop is many LLM calls per verse. Fine for scholarship (verses/minute beats verses/decade); don't position it as bulk MT.
- **Someone else ships first.** Dharmamitra is closest. Mitigation is speed to a public Phase 1 demo — 8 weeks — and the fact that your artifact (per-decision apparatus + grammar verification) is differentiated even from their retrieval work.

## 8. First actions (this week)

1. `pip install dharmamitra-sanskrit-grammar vidyut` — sanity-check both on lines from your 2022 `trbh.txt.unsandhied`.
2. Pull the Triṃśikā root text (GRETIL/DCS) and confirm your bhāṣya file covers all 30 verses.
3. Write the pratīka-matcher prototype (verse → commentary spans).
4. Hand-run the full loop on **one verse** with Claude as the reasoner, manually — before writing any orchestration code. This tells you more than a week of architecture work.
