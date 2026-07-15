# Reasoner prompt template (Phase 0 hand-run; feeds Phase 1 orchestration)

You are translating one verse of a Sanskrit śāstra with its own commentary as
primary evidence. Produce no bare translation: every contested choice must
carry a justification object citing the commentary by line number.

## Inputs

1. VERSE (IAST), with source line numbers in the commentary text:
   {verse_text_with_lines}

2. ANALYZE output (segmentation + lemma + morphosyntax per token, from
   ByT5-Sanskrit; tag scheme: [Number][Case][Gender] for nominals,
   [Number][Tense][Person][Mood] for verbs, Cp = prior compound member):
   {analyze_json}

3. COMMENTARY SPAN (the verse's own bhāṣya, line-numbered; from the
   pratīka-matcher alignment):
   {commentary_span}

4. DICTIONARY entries (MW, cited as `MW s.v. X, page,col`):
   {mw_entries}

## Task

1. Read the commentary span FIRST; note where it glosses, defines
   (`X iti Y`, `...tvāt`, `X = Y paryāyau`), or argues (pūrvapakṣa marked by
   `iti` + rejection like `tad ayuktam`). Mind authorial voice: opponents'
   views are quoted, not asserted.
2. For each word of the verse: adopt or correct the ANALYZE morphology; for
   compounds state members AND the samāsa relation; every claim must be in
   checkable form (stem/root + liṅga/vibhakti/vacana or tiṅ features) for
   Vidyut verification.
3. Identify the CONTESTED points (compound relations, technical terms,
   construal of cases, voice) and decide each on commentary evidence.
4. Output, in order:
   a. word-by-word analysis table (surface | lemma | morph | note)
   b. justification objects: {decision, options, chosen, evidence: [{lines,
      quote, translation}], depends_on_commentary: bool}
   c. translation (verse-shaped, technical terms parenthesized on first use)
   d. one-shot delta: what a commentary-blind translation would plausibly
      get wrong here
   e. open questions / uncertainties.

Rules: IAST only; cite evidence as `trbh <line>`; do not assert anything the
commentary contradicts; morphological claims you cannot support must be
flagged, not silently dropped.
