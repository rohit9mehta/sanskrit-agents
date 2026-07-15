"""Śāstrārtha: commentary-grounded, grammar-verified Sanskrit translation agent.

Phase 0 modules:
  texts      — canonical access to trbh.txt (1,560 lines, 1-indexed, never edited)
  normalize  — IAST folding/skeletons for fuzzy matching
  analyze    — Dharmamitra API client + local ByT5-Sanskrit multitask model
  verify     — vidyut wrappers (lipi/kosha/prakriya) + verification logger
  match      — pratīka-matcher: kārikā ↔ commentary-span alignment
"""

__version__ = "0.1.0"
