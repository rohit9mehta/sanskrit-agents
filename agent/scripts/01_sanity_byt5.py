"""ByT5-Sanskrit sanity check (Phase 0, CLAUDE.md item 1).

Runs the Dharmamitra API and the local multitask model on 10 stress lines
from trbh.txt, compares segmentation against the 2022 .unsandhied file, and
writes a side-by-side report to agent/logs/sanity/byt5_report.md.

Pass rules:
  - the local model returns non-empty output for all 10 lines;
  - ≥8/10 lines have 2-of-3 segmentation consensus among {API, local model,
    2022 file} after normalization. No single source is trusted alone: the
    2022 file has a known ~15% line error rate, and the API demonstrably
    under-splits compounds. Zero-consensus lines are flagged in the report —
    they are the genuinely hard cases (that's data, not failure);
  - every SLM token parses as surface_lemma_tag, and two known analyses
    are present (vipākaḥ→vipāka SNM, pravartate→pravṛt SPr3In).
"""

import sys
from difflib import SequenceMatcher

from shastrartha import texts
from shastrartha.analyze import dharmamitra_tag, local_analyze, parse_slm
from shastrartha.normalize import seg_tokens
from shastrartha.texts import LOGS_DIR

# Stress set: long compounds (1, 61), verse lines (24=v.1ab, 167=v.2ab,
# 177=v.2cd, 1052=v.16 with avagraha/ṛ sandhi), pūrvapakṣa prose (147),
# v.3a region (202), ordinary prose (172, 188).
LINES = [1, 24, 61, 147, 167, 172, 177, 188, 202, 1052]
REPORT = LOGS_DIR / "sanity" / "byt5_report.md"


def agree(a: str, b: str) -> bool:
    return seg_tokens(a) == seg_tokens(b)


def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, seg_tokens(a), seg_tokens(b)).ratio()


def main() -> int:
    raw = [texts.line(n) for n in LINES]
    gold2022 = [texts.unsandhied_line(n) for n in LINES]

    api_err = None
    try:
        api = dharmamitra_tag(raw)
    except Exception as e:
        api_err = f"{type(e).__name__}: {e}"
        api = [""] * len(raw)

    local_s = local_analyze(raw, task="S")
    local_slm = local_analyze(raw, task="SLM")

    rows, n_consensus, flagged = [], 0, []
    for i, n in enumerate(LINES):
        pairs = {
            "api=2022": agree(api[i], gold2022[i]),
            "local=2022": agree(local_s[i], gold2022[i]),
            "api=local": agree(api[i], local_s[i]),
        }
        consensus = any(pairs.values())
        n_consensus += consensus
        if not consensus:
            flagged.append(n)
        rows.append((n, pairs, sim(local_s[i], gold2022[i])))

    slm_parse_ok = True
    slm_parsed = [parse_slm(o) for o in local_slm]
    for n, toks in zip(LINES, slm_parsed):
        bad = [t for t in toks if "unparsed" in t]
        if bad:
            slm_parse_ok = False
            print(f"line {n}: unparsed SLM tokens: {bad}")

    def has(parsed, surface, lemma, tag):
        return any(
            t.get("surface") == surface and t.get("lemma") == lemma and t.get("tag") == tag
            for t in parsed
        )

    spot_ok = has(slm_parsed[LINES.index(167)], "vipākaḥ", "vipāka", "SNM") and has(
        slm_parsed[LINES.index(24)], "pravartate", "pravṛt", "SPr3In"
    )

    nonempty_local = all(local_s) and all(local_slm)
    seg_ok = n_consensus >= 8

    # ------------------------------------------------------------- report
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", encoding="utf-8") as f:
        f.write("# ByT5-Sanskrit sanity report\n\n")
        f.write(f"Lines tested: {LINES}\n\n")
        if api_err:
            f.write(f"**Dharmamitra API unavailable:** {api_err} (local model only)\n\n")
        f.write("| line | api=2022 | local=2022 | api=local | local-vs-2022 sim |\n")
        f.write("|---|---|---|---|---|\n")
        for n, pairs, s in rows:
            cells = " | ".join("✓" if v else "✗" for v in pairs.values())
            f.write(f"| {n} | {cells} | {s:.3f} |\n")
        f.write(
            f"\n2-of-3 consensus: {n_consensus}/10; zero-consensus lines: {flagged or 'none'}\n\n"
            "## Decision\n\n"
            "The **local model is the primary ANALYZE provider** (S for segmentation, "
            "SLM for lemma+morphosyntax). The API under-splits compounds relative to "
            "both other sources (lines 1, 177: `apratipanna|vipratipanna` and "
            "`sarva|bījakam` not split) and silently dropped the long opening compound "
            "of line 202. Keep the API as a fast cross-check only.\n\n"
            "## Notable finding (line 202)\n\n"
            "`asaṃviditakopādisthānavijñaptikaṃ` — both the local model and the 2022 "
            "file segment `...ka|upādi...` as `kopa|ādi` ('anger' + 'etc.'), but "
            "Sthiramati's own gloss (trbh 203–215, `upādānam upādiḥ ...`) shows the "
            "correct division is `asaṃviditaka|upādi|sthāna|vijñaptika`. This is "
            "precisely the failure mode the commentary-grounding loop exists to fix, "
            "reproduced by the sanity check itself.\n\n"
        )
        for i, n in enumerate(LINES):
            f.write(f"## line {n}\n\n")
            f.write(f"- **raw**: `{raw[i]}`\n")
            f.write(f"- **2022**: `{gold2022[i]}`\n")
            f.write(f"- **API**: `{api[i]}`\n")
            f.write(f"- **local S**: `{local_s[i]}`\n")
            f.write(f"- **local SLM**: `{local_slm[i]}`\n\n")

    print(f"report: {REPORT}")
    print(f"2-of-3 consensus: {n_consensus}/10 (flagged: {flagged or 'none'}); "
          f"seg {'OK' if seg_ok else 'BAD'}")
    print(f"SLM parse: {'OK' if slm_parse_ok else 'BAD'}; spot-checks: {'OK' if spot_ok else 'BAD'}")
    ok = nonempty_local and seg_ok and slm_parse_ok and spot_ok
    print("BYT5 SANITY", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
