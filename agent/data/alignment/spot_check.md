# Alignment spot-check log

Checked by the agent (Claude) on 2026-07-15 against trbh.txt content;
`checked_by_human` in trimsika_alignment.json stays `false` until Rohit's own
pass. Every verse below was verified by reading the anchor line, the first
and last span lines, and the lines just outside the span.

| verse | verdict | note |
|---|---|---|
| 1 | OK | unmarked quote at 24 (no āha/iti); span opens with `lokaśāstrayor iti vākyaśeṣaḥ`, ends before v.2's avatāraṇikā (165–166) |
| 3 | OK | syntactically integrated quote at 202; span opens with the upādi vigraha (`asaṃviditaka upādir yasmin...`) — the CLAUDE.md-validated gloss |
| 7 | OK | truncated pratīka `yatrajas tanmayair` (partial_ratio catch); gloss `yatra jāto yatrajaḥ` at 427; span start correctly skips the `iti` at 426 |
| 11 | OK | 11d quoted at 681 jointly with 12a (682) before one `iti` (683); span 577–681 |
| 12 | OK | span starts 684, after the shared `iti` |
| 17 | OK | two-line anchor 1093–1094; gloss restates the verse at 1096 |
| 19 | OK | anchor 1157–1158 carries Sthiramati's `'nyaṃ vipākaṃ` reading (vulgate `'nyad`) |
| 25 | OK | quote at 1402 directly follows v.24's gloss with no avatāraṇikā |
| 26 | OK | span-last 1469 `kiṃ tarhi` is arguably v.27's lead-in ("what then?") but has no `āha`, so the walk-back keeps it; harmless for retrieval |
| 29 | OK | quoted back-to-back with v.30 (`ślokadvayena`, 1499–1502); shares span 1504–1558, flagged `shared_with: 30`; pāda-by-pāda requotes 29a–d located at 1508–1519 |
| 30 | OK | joint exposition span 1504–1558, ends before colophon (1559–1560) |

Cross-validation: gold projection (global difflib token alignment of trbh ↔
GRETIL-comm, similarity 0.9954) agrees with the matcher on 72/72 units and
30/30 verse anchors — see gold_projection.json.
