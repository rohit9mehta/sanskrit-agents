"""Phase 2, item 2: ablations.

no_verify     — attempt-1 accepted as-is (reuses the full run's cached LLM
                responses; isolates what the verify-feedback retry fixes)
no_commentary — commentary retrieval removed from the prompt (grammar +
                analyzer + MW only; isolates what the bhāṣya contributes)

Writes agent/output/ablations/<mode>/vNN/apparatus.{json,md} and
agent/output/ablations/ablation_report.md with the comparison table.
"""

import json
import sys
from difflib import SequenceMatcher

from shastrartha.pipeline import OUTPUT_DIR, default_analyze_fn, run_verse
from shastrartha.reason import total_spend

MODES = ["no_verify", "no_commentary"]
HARD_STOP_USD = 25.0


def run_mode(mode: str, analyze_fn, force: bool) -> list[dict]:
    out = []
    for n in range(1, 31):
        if total_spend() > HARD_STOP_USD:
            print(f"HARD STOP at ${total_spend():.2f}")
            break
        try:
            s = run_verse(n, analyze_fn, force=force, mode=mode)
        except Exception as e:
            s = {"verse": n, "error": f"{type(e).__name__}: {e}"}
        out.append(s)
        print(mode, json.dumps(s, ensure_ascii=False), flush=True)
    return out


def load(mode: str, n: int) -> dict | None:
    p = (OUTPUT_DIR / f"v{n:02d}" if mode == "full"
         else OUTPUT_DIR / "ablations" / mode / f"v{n:02d}") / "apparatus.json"
    return json.loads(p.read_text()) if p.exists() else None


def report() -> None:
    rows = []
    for n in range(1, 31):
        full = load("full", n)
        row = {"verse": n, "full": full}
        for m in MODES:
            row[m] = load(m, n)
        rows.append(row)

    def agg(mode_key):
        t = {"pass": 0, "fail": 0, "unsupported": 0, "j": 0, "jc": 0, "verses": 0}
        for r in rows:
            d = r[mode_key]
            if not d:
                continue
            t["verses"] += 1
            for k in ("pass", "fail", "unsupported"):
                t[k] += d["verification_summary"][k]
            t["j"] += len(d["justifications"])
            t["jc"] += sum(1 for j in d["justifications"] if j["depends_on_commentary"])
        return t

    def drift(a: str, b: str) -> float:
        return 1 - SequenceMatcher(None, a.lower(), b.lower()).ratio()

    lines = [
        "# Ablation report",
        "",
        "| variant | verses | claims pass/fail/unsup | J-objects (commentary-dep) |",
        "|---|---|---|---|",
    ]
    for key, label in [("full", "full pipeline"), ("no_verify", "− verify retry"),
                       ("no_commentary", "− commentary")]:
        t = agg(key)
        lines.append(f"| {label} | {t['verses']} | {t['pass']}/{t['fail']}/{t['unsupported']} "
                     f"| {t['j']} ({t['jc']}) |")

    lines += ["", "## Translation drift vs full pipeline (1 − similarity)", "",
              "| verse | no_verify | no_commentary |", "|---|---|---|"]
    big_drift = []
    for r in rows:
        if not r["full"]:
            continue
        ds = {}
        for m in MODES:
            ds[m] = drift(r["full"]["translation"], r[m]["translation"]) if r[m] else None
        lines.append(f"| {r['verse']} | "
                     f"{ds['no_verify']:.2f} | {ds['no_commentary']:.2f} |"
                     if None not in ds.values() else f"| {r['verse']} | — | — |")
        if ds.get("no_commentary") and ds["no_commentary"] > 0.35:
            big_drift.append(r["verse"])

    lines += ["", f"Verses where removing the commentary changes the translation "
              f"substantially (drift > 0.35): {big_drift}", ""]
    lines += ["## Per-verse translations (full vs − commentary)", ""]
    for r in rows:
        if not (r["full"] and r["no_commentary"]):
            continue
        lines += [f"### v.{r['verse']}", "",
                  f"**full** — {r['full']['translation']}", "",
                  f"**− commentary** — {r['no_commentary']['translation']}", ""]

    out = OUTPUT_DIR / "ablations" / "ablation_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")


def main() -> int:
    force = "--force" in sys.argv
    if "--report-only" not in sys.argv:
        analyze_fn = default_analyze_fn()
        run_mode("no_verify", analyze_fn, force)
        run_mode("no_commentary", analyze_fn, force)
    report()
    print(f"cumulative est spend ${total_spend():.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
