"""Comparison document + aggregate stats (Phase 1, W5) → agent/output/comparison.md

Per verse: agent translation vs raw-LLM (same model) vs MITRA vs the
web-sourced human baseline, plus which decisions were commentary-dependent.
Aggregate: verification outcomes, retry rate, disagreements, tokens/cost.
"""

import json
import sys
from collections import Counter

from shastrartha.texts import AGENT_DIR, DATA_DIR

OUTPUT = AGENT_DIR / "output"
EVAL = DATA_DIR / "eval"


def load(p, default=None):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def main() -> int:
    raw = load(EVAL / "raw_llm.json", {})
    mitra = load(EVAL / "mitra.json", {})
    human = load(EVAL / "human_baseline.json", {})
    human_src = human.get("source", {})

    rows, agg = [], Counter()
    tok = Counter()
    for n in range(1, 31):
        d = load(OUTPUT / f"v{n:02d}" / "apparatus.json")
        if not d:
            rows.append({"verse": n, "missing": True})
            continue
        vs = d["verification_summary"]
        agg.update({k: v for k, v in vs.items()})
        agg["verses"] += 1
        agg["attempts"] += d["run"]["attempts"]
        agg["retries"] += 1 if d["run"]["attempts"] > 1 else 0
        agg["j_total"] += len(d["justifications"])
        agg["j_commentary"] += sum(1 for j in d["justifications"] if j["depends_on_commentary"])
        agg["disagreements"] += len(d.get("analyzer_disagreements", []))
        for k, v in d["run"]["usage"].items():
            tok[k] += v
        tok["cost"] += d["run"].get("est_cost", 0)
        rows.append({
            "verse": n,
            "translation": d["translation"],
            "vs": vs,
            "j": [(j["id"], j["decision"], j["depends_on_commentary"],
                   [e["lines"] for e in j["evidence"]]) for j in d["justifications"]],
            "unverified": [w["surface"] for w in d["analysis"]
                           if w.get("verification", {}).get("flag") == "UNVERIFIED"],
        })

    lines = [
        "# Phase 1 comparison: commentary-grounded agent vs baselines",
        "",
        f"- **agent**: pipeline reasoner `{load(OUTPUT / 'v02' / 'apparatus.json')['run']['model']}` "
        "+ ByT5 analyses + bhāṣya span retrieval + MW + vidyut verification loop",
        f"- **raw-LLM**: same model, verse text only ({raw.get('model', 'n/a')})",
        f"- **MITRA**: {mitra.get('endpoint', 'n/a')} (style: {mitra.get('style_instruction')})",
        f"- **human**: {human_src.get('translator')} — *{human_src.get('title', '')[:60]}...*, "
        f"{human_src.get('edition')}, {human_src.get('pages')} (web-sourced, transcribed from page "
        "images; translates the vulgate text)",
        "",
        "## Aggregate",
        "",
        f"| metric | value |",
        f"|---|---|",
        f"| verses completed | {agg['verses']}/30 |",
        f"| word-claims pass / fail / unsupported / tool_error | "
        f"{agg['pass']} / {agg['fail']} / {agg['unsupported']} / {agg['tool_error']} |",
        f"| verses needing a verify-feedback retry | {agg['retries']} |",
        f"| justification objects (commentary-dependent) | {agg['j_total']} ({agg['j_commentary']}) |",
        f"| analyzer overrides recorded | {agg['disagreements']} |",
        f"| tokens (prompt / completion / reasoning) | {tok['prompt_tokens']} / "
        f"{tok['completion_tokens']} / {tok['reasoning_tokens']} |",
        f"| estimated pipeline cost | ${tok['cost']:.2f} |",
        "",
        "---",
        "",
    ]
    for r in rows:
        n = r["verse"]
        if r.get("missing"):
            lines += [f"## v.{n} — MISSING", ""]
            continue
        lines += [f"## v.{n}", ""]
        vs = r["vs"]
        status = f"{vs['pass']} pass / {vs['fail']} fail / {vs['unsupported']} unsupported"
        if r["unverified"]:
            status += f" — UNVERIFIED: {', '.join(r['unverified'])}"
        lines += [f"*verification: {status}*", ""]
        lines += [f"**agent** — {r['translation']}", ""]
        if raw.get("verses", {}).get(str(n)):
            lines += [f"**raw-LLM** — {raw['verses'][str(n)]}", ""]
        if mitra.get("verses", {}).get(str(n)):
            lines += [f"**MITRA** — {mitra['verses'][str(n)]}", ""]
        if human.get("verses", {}).get(str(n)):
            lines += [f"**human (Salvini 2022)** — {human['verses'][str(n)]}", ""]
        if r["j"]:
            dep = [f"{jid} ({'C' if c else '–'}; trbh {ev})" for jid, _, c, ev in r["j"]]
            lines += ["commentary-grounded decisions: " + "; ".join(dep), ""]

    (OUTPUT / "comparison.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUTPUT / 'comparison.md'}")
    print(dict(agg), dict(tok))
    return 0


if __name__ == "__main__":
    sys.exit(main())
