"""Render an apparatus dict to Markdown, mirroring the Phase 0 hand-run
format (agent/handrun/v02/apparatus.md)."""


def _morph_str(w: dict) -> str:
    m = w["morph"]
    if m["pos"] == "subanta":
        s = f"{m['linga']}. {m['vibhakti']}/{m['vacana']}"
    elif m["pos"] == "tinanta":
        pre = "-".join((m.get("prefixes") or []) + [m.get("root") or "?"])
        s = f"{pre}, {m['prayoga']}/{m['lakara']}/{m['purusha']}/{m['vacana']}"
    else:
        s = "indecl."
    if w.get("samasa"):
        s += f"; {w['samasa']['type']} ⟨{w['samasa']['vigraha']}⟩"
    return s


def render_apparatus(d: dict, bundle=None) -> str:
    run = d.get("run", {})
    vs = d.get("verification_summary", {})
    lines = [
        f"# Triṃśikā v.{d['verse']} — commentary-grounded translation with apparatus",
        "",
        f"Pipeline run — reasoner: `{run.get('model')}`, attempts: {run.get('attempts')}, "
        f"verification: {vs.get('pass', 0)} pass / {vs.get('fail', 0)} fail / "
        f"{vs.get('unsupported', 0)} unsupported.",
        "",
        "## Verse",
        "",
        f"> **{d.get('verse_text') or (bundle.verse_text if bundle else '')}**",
        "",
        "## Word-by-word analysis",
        "",
        "| surface | lemma | morphology | vidyut |",
        "|---|---|---|---|",
    ]
    for w in d["analysis"]:
        v = w.get("verification", {})
        status = v.get("status", "?")
        if v.get("flag") == "UNVERIFIED":
            status = f"**{status} — UNVERIFIED**"
        lines.append(
            f"| {w['surface']} | {w['lemma']} | {_morph_str(w)} | {status} |"
        )
    lines += ["", "## Justifications", ""]
    for j in d["justifications"]:
        dep = "**yes**" if j["depends_on_commentary"] else "no"
        lines += [f"**{j['id']}. {j['decision']}**",
                  f"- chosen: {j['chosen']} (depends on commentary: {dep})"]
        for e in j["evidence"]:
            lines.append(f"- trbh {e['lines']}: `{e['quote']}` — {e['translation']}")
        lines.append("")
    lines += ["## Translation", "", f"> {d['translation']}", ""]
    if d.get("analyzer_disagreements"):
        lines += ["## Analyzer disagreements", ""]
        lines += [f"- {x}" for x in d["analyzer_disagreements"]] + [""]
    if d.get("one_shot_delta"):
        lines += ["## One-shot delta", ""]
        lines += [f"- {x}" for x in d["one_shot_delta"]] + [""]
    if d.get("open_questions"):
        lines += ["## Open questions", ""]
        lines += [f"- {x}" for x in d["open_questions"]] + [""]
    return "\n".join(lines)
