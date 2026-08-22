"""Per-verse orchestration (Phase 1, W4):
retrieve → reason (structured output) → verify → at most ONE retry carrying
the verifier's error report → final apparatus with per-word verification
status. Words still failing after the retry are flagged UNVERIFIED in the
output — never silently dropped.
"""

import json
from pathlib import Path

from .reason import MODEL, estimated_cost, reason
from .retrieve import retrieve
from .runner import VerifyReport, pipeline_verify
from .schema import Apparatus
from .texts import AGENT_DIR

OUTPUT_DIR = AGENT_DIR / "output"


def default_analyze_fn():
    """ANALYZE provider with the local model kept resident across verses."""
    from .analyze import dharmamitra_tag, local_analyze, parse_slm

    def fn(lines: list[str]) -> dict:
        out: dict = {}
        try:
            out["api_seg"] = dharmamitra_tag(lines)
        except Exception as e:
            out["api_seg"] = f"unavailable ({type(e).__name__})"
        out["local_S"] = local_analyze(lines, task="S")
        out["local_SLM"] = local_analyze(lines, task="SLM")
        out["slm_parsed"] = [parse_slm(o) for o in out["local_SLM"]]
        try:
            from .lemma import canonical_hints
            hints = [h for parsed in out["slm_parsed"] for h in canonical_hints(parsed)]
            if hints:
                out["canonical_lemmas"] = hints
        except Exception as e:  # normalization is advisory; never block the run
            out["canonical_lemmas"] = f"unavailable ({type(e).__name__})"
        return out

    return fn


def _merge(app: Apparatus, report: VerifyReport, meta: dict) -> dict:
    d = app.model_dump()
    for w, r in zip(d["analysis"], report.words):
        w["verification"] = {"status": r.status, "detail": r.detail}
        if r.status in ("fail", "tool_error"):
            w["verification"]["flag"] = "UNVERIFIED"
            if r.expected:
                w["verification"]["claim_derives"] = r.expected[:8]
    d["verification_summary"] = report.n
    d["run"] = meta
    return d


def _mw_for_analyze(analyze: dict) -> dict:
    from .dictionary import mw_entries

    lemmas: list[str] = []
    for parsed in analyze.get("slm_parsed", []):
        for tok in parsed:
            lem = tok.get("lemma")
            if lem and lem not in lemmas:
                lemmas.append(lem)
    mw = {}
    for lem in lemmas:
        try:
            entries = mw_entries(lem, limit=4)
        except Exception:
            entries = []
        if entries:
            mw[lem] = [{"citation": x["citation"], "text": x["text"][:400]}
                       for x in entries[:3]]
    return mw


def run_unit(slug: str, unit_id: str, analyze_fn, force: bool = False) -> dict:
    """Library-text pipeline: pre-aligned unit → reason → verify → ≤1 retry."""
    from .library import load_text
    from .reason import reason_unit
    from .render import render_apparatus

    lt = load_text(slug)
    unit = lt.unit(unit_id)
    out_dir = OUTPUT_DIR / slug / unit_id.replace(".", "_")
    out_json = out_dir / "apparatus.json"
    if out_json.exists() and not force:
        d = json.loads(out_json.read_text())
        return {"unit": unit_id, "skipped": True, **d["verification_summary"],
                "est_cost": d["run"].get("est_cost", 0.0)}

    analyze = analyze_fn([unit.mula]) if analyze_fn else {}
    mw = _mw_for_analyze(analyze)

    app, usage1 = reason_unit(lt, unit, analyze, mw)
    report = pipeline_verify(app, run_id=f"lib-{slug}-{unit_id}-a1", text=slug)
    attempts, usages = 1, [usage1]

    if report.failures:
        app2, usage2 = reason_unit(lt, unit, analyze, mw,
                                   feedback=report.feedback(), prior=app)
        report2 = pipeline_verify(app2, run_id=f"lib-{slug}-{unit_id}-a2", text=slug)
        app, report = app2, report2
        attempts, usages = 2, [usage1, usage2]

    usage_total = {
        k: sum(u.get(k, 0) for u in usages)
        for k in ("prompt_tokens", "completion_tokens", "reasoning_tokens")
    }
    meta = {
        "model": MODEL, "mode": "library", "text": slug, "attempts": attempts,
        "usage": usage_total, "est_cost": round(estimated_cost(usage_total), 4),
    }
    merged = _merge(app, report, meta)
    merged["mula"] = unit.mula
    merged["commentary_lines"] = unit.commentary

    out_dir.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(merged, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    (out_dir / "apparatus.md").write_text(
        render_apparatus(
            merged,
            title=f"# {lt.title} — {unit_id} (commentary-grounded, with apparatus)",
            tag=lt.citation_tag,
        ),
        encoding="utf-8",
    )
    return {"unit": unit_id, "skipped": False, "attempts": attempts,
            **report.n, "est_cost": meta["est_cost"]}


def run_verse(n: int, analyze_fn, force: bool = False, mode: str = "full") -> dict:
    """mode: 'full' | 'no_commentary' (retrieval ablated) | 'no_verify'
    (verify-feedback retry ablated; attempt-1 accepted as-is)."""
    out_dir = (OUTPUT_DIR / f"v{n:02d}" if mode == "full"
               else OUTPUT_DIR / "ablations" / mode / f"v{n:02d}")
    out_json = out_dir / "apparatus.json"
    if out_json.exists() and not force:
        d = json.loads(out_json.read_text())
        return {"verse": n, "skipped": True, **d["verification_summary"],
                "est_cost": d["run"].get("est_cost", 0.0)}

    bundle = retrieve(n, analyze_fn)
    include_commentary = mode != "no_commentary"
    run_tag = "pipeline" if mode == "full" else f"ablation-{mode}"

    app, usage1 = reason(bundle, include_commentary=include_commentary)
    report = pipeline_verify(app, run_id=f"{run_tag}-v{n:02d}-a1")
    attempts, usages = 1, [usage1]

    if report.failures and mode != "no_verify":
        app2, usage2 = reason(bundle, feedback=report.feedback(), prior=app,
                              include_commentary=include_commentary)
        report2 = pipeline_verify(app2, run_id=f"{run_tag}-v{n:02d}-a2")
        app, report = app2, report2
        attempts, usages = 2, [usage1, usage2]

    usage_total = {
        k: sum(u.get(k, 0) for u in usages)
        for k in ("prompt_tokens", "completion_tokens", "reasoning_tokens")
    }
    meta = {
        "model": MODEL,
        "mode": mode,
        "attempts": attempts,
        "usage": usage_total,
        "est_cost": round(estimated_cost(usage_total), 4),
        "retrieval": {"anchor": bundle.anchor, "span": bundle.span,
                      "shared_with": bundle.shared_with,
                      "requotes": [r["lines"] for r in bundle.requotes]},
    }
    merged = _merge(app, report, meta)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(merged, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    from .render import render_apparatus

    (out_dir / "apparatus.md").write_text(render_apparatus(merged, bundle),
                                          encoding="utf-8")
    return {"verse": n, "skipped": False, "attempts": attempts,
            **report.n, "est_cost": meta["est_cost"]}
