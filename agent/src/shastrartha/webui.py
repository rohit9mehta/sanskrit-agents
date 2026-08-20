"""Shared HTML rendering for the demo: used by the local server
(scripts/20_serve.py) and the static-site exporter (scripts/22_static_site.py).

All hrefs go through link helpers so the same pages work served from "/" and
from a GitHub Pages subpath (relative links).
"""

import html
import json
import re
from pathlib import Path

from .ask import TEXT_META
from .texts import AGENT_DIR

OUTPUT = AGENT_DIR / "output"

COVERAGE_NOTE = {
    "trimsika": "complete (30 verses)",
    "isa": "complete (18 mantras)",
    "gita": "chapter 2 (72 verses)",
    "yogasutra": "chapter 1 (51 sūtras)",
}

CSS = """
:root { --ink:#1a1613; --paper:#faf7f1; --accent:#7c2d12; --soft:#e7ded0; }
* { box-sizing:border-box; }
body { font-family: Georgia, 'Times New Roman', serif; background:var(--paper);
       color:var(--ink); margin:0; line-height:1.55; }
.wrap { max-width: 860px; margin: 0 auto; padding: 2rem 1.2rem 4rem; }
h1 { font-size:1.7rem; margin:0 0 .2rem; }
h1 a { color:inherit; text-decoration:none; }
.sub { color:#6b5f4e; font-style:italic; margin-bottom:1.6rem; }
.searchrow { display:flex; gap:.6rem; }
input[type=text] { flex:1; font:inherit; font-size:1.05rem; padding:.65rem .8rem;
  border:1.5px solid var(--soft); border-radius:8px; background:#fff; }
button { font:inherit; padding:.65rem 1.1rem; border:0; border-radius:8px;
  background:var(--accent); color:#fff; cursor:pointer; }
.answer { background:#fff; border:1.5px solid var(--soft); border-radius:10px;
  padding:1.1rem 1.3rem; margin-top:1.4rem; white-space:pre-wrap; }
.cite { color:var(--accent); text-decoration:none; border-bottom:1px dotted; }
.samples { margin-top:.8rem; color:#6b5f4e; font-size:.92rem; }
.samples a { color:var(--accent); text-decoration:none; margin-right:.9rem;
  display:inline-block; margin-bottom:.35rem; }
.src { margin-top:1rem; font-size:.9rem; color:#6b5f4e; }
.src a { color:var(--accent); }
table { border-collapse:collapse; width:100%; margin:.6rem 0 1rem; font-size:.95rem; }
td,th { border-bottom:1px solid var(--soft); padding:.35rem .5rem; text-align:left; }
.mula { font-size:1.1rem; background:#fff; border-left:3px solid var(--accent);
  padding:.7rem 1rem; margin:.8rem 0; }
.commline { padding:.15rem 0 .15rem 2.2rem; text-indent:-2.2rem; }
.commline .n { color:#a89a83; font-size:.8rem; margin-right:.5rem; }
.j { background:#fff; border:1.5px solid var(--soft); border-radius:10px;
  padding: .8rem 1rem; margin:.7rem 0; }
.badge { font-size:.75rem; padding:.1rem .45rem; border-radius:99px;
  background:#e8f0e4; color:#265226; margin-left:.4rem; }
.badge.bad { background:#f6e0d8; color:#8a2f12; }
.spin { display:none; color:#6b5f4e; margin-top:1rem; }
.shelf { background:#fff; border:1.5px solid var(--soft); border-radius:10px;
  padding:1rem 1.2rem; margin-top:2rem; }
.shelf h3 { margin:.1rem 0 .5rem; font-size:1.05rem; }
.shelf td { font-size:.92rem; }
.note { color:#6b5f4e; font-size:.85rem; }
.explain { color:#6b5f4e; font-size:.85rem; margin:-.2rem 0 .6rem; }
"""

TITLE = "Śāstrārtha: ask the śāstras"
SUBTITLE = ("Ask the śāstras. Every answer is cited to the tradition's own "
            "commentaries, and every translation behind it is grammar-checked.")

CANNED_QUESTIONS = [
    ("What is the storehouse consciousness?", "storehouse consciousness"),
    ("What are the three transformations of consciousness?", "three transformations"),
    ("What does representation-only (vijñapti-mātra) mean?", "representation-only"),
    ("What does the Gita say about acting without attachment to results?",
     "karma without attachment"),
    ("Why does Krishna tell Arjuna not to grieve for the dead?", "why not grieve"),
    ("Who is the person of steady wisdom (sthita-prajna)?", "steady wisdom"),
    ("What happens to the soul at death, according to the Gita?", "the soul at death"),
    ("How does Vyasa define yoga?", "definition of yoga"),
    ("What is the role of practice and dispassion in yoga?", "practice and dispassion"),
    ("What does Patanjali say about Om?", "Om"),
    ("How can the mind be made calm and clear?", "calming the mind"),
    ("What does 'all this is pervaded by the Lord' mean?", "īśāvāsyam"),
    ("What happens to one who worships only ignorance?", "worshipping ignorance"),
    ("Can one wish to live a hundred years performing works?", "a hundred years of works"),
    ("What are the yamas and niyamas?", "outside the library? watch it refuse"),
]


def page(body: str, home_href: str = "/") -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>{TITLE}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style></head><body><div class="wrap">
<h1><a href="{home_href}">Śāstrārtha</a></h1>
<div class="sub">{SUBTITLE}</div>
{body}
</div></body></html>"""


def md_lite(text: str) -> str:
    t = html.escape(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", t)
    return t


def units_of(slug: str) -> list[str]:
    if slug == "trimsika":
        return [str(int(p.parent.name[1:]))
                for p in sorted(OUTPUT.glob("v[0-9][0-9]/apparatus.json"))]
    def key(u):
        return [int(x) for x in u.split(".")]
    us = [p.parent.name.replace("_", ".")
          for p in sorted((OUTPUT / slug).glob("*/apparatus.json"))]
    try:
        return sorted(us, key=key)
    except ValueError:
        return sorted(us)


def shelf_html(unit_href) -> str:
    rows = []
    for slug, meta in TEXT_META.items():
        us = units_of(slug)
        if not us:
            continue
        links = " ".join(
            f"<a class='cite' href='{unit_href(slug, u)}'>{u}</a>" for u in us)
        rows.append(
            f"<tr><td><b>{html.escape(meta['title'])}</b><br>"
            f"<span class='note'>coverage: {COVERAGE_NOTE.get(slug, '')} · "
            f"commentator: {meta['commentator']}</span>"
            f"<div class='note' style='margin-top:.3rem'>{links}</div></td></tr>")
    return ("<div class='shelf'><h3>In the library right now</h3>"
            "<p class='note'>The system answers only from these texts and "
            "their commentaries. Anything else is refused, not improvised.</p>"
            "<table>" + "".join(rows) + "</table></div>")


def apparatus_body(slug: str, unit: str, home_href: str, unit_href) -> str:
    meta = TEXT_META.get(slug, {"title": slug, "tag": slug, "commentator": "?"})
    if slug == "trimsika":
        path = OUTPUT / f"v{int(unit):02d}" / "apparatus.json"
    else:
        path = OUTPUT / slug / unit.replace(".", "_") / "apparatus.json"
    if not path.exists():
        return (f"<p>No apparatus for {html.escape(slug)} {html.escape(unit)} yet.</p>"
                f"<p><a href='{home_href}'>back</a></p>")
    d = json.loads(path.read_text(encoding="utf-8"))
    from .ask import _trimsika_mula

    mula = d.get("mula") or (_trimsika_mula(unit) if slug == "trimsika" else "")
    vs = d.get("verification_summary", {})
    parts = [
        f"<p><a href='{home_href}'>back to questions</a></p>",
        f"<h2>{html.escape(meta['title'])} · {html.escape(unit)}</h2>",
        f"<div class='mula'>{html.escape(mula)}</div>",
        f"<p><b>Translation.</b> {md_lite(d.get('translation', ''))}</p>",
        f"<p><b>Grammar check:</b> {vs.get('pass', 0)} words pass / "
        f"{vs.get('fail', 0)} flagged / {vs.get('unsupported', 0)} beyond the "
        f"checker<span class='badge'>Pāṇini-verified</span></p>",
        "<div class='explain'>Every word's claimed grammar is re-derived "
        "with vidyut-prakriya, software implementing Pāṇini's rules. "
        "Flags are shown, never hidden; some are the text taking epic or "
        "Vedic liberties the classical rules do not generate.</div>",
        "<h3>Word by word</h3>"
        "<table><tr><th>surface</th><th>lemma</th><th>grammar</th></tr>",
    ]
    for w in d.get("analysis", []):
        v = w.get("verification", {})
        badge = ("<span class='badge'>pass</span>" if v.get("status") == "pass"
                 else f"<span class='badge bad'>{v.get('status', '?')}</span>")
        parts.append(f"<tr><td>{html.escape(w['surface'])}</td>"
                     f"<td>{html.escape(w['lemma'])}</td><td>{badge}</td></tr>")
    parts.append("</table><h3>How the commentary settled it</h3>"
                 "<div class='explain'>Where the verse alone is ambiguous, the "
                 f"reading follows {html.escape(meta['commentator'])}'s "
                 "commentary; the deciding lines are quoted below each "
                 "decision.</div>")
    for j in d.get("justifications", []):
        ev = "".join(
            f"<div class='commline'><span class='n'>{meta['tag']} {e['lines']}</span>"
            f"{html.escape(e['quote'])}<br><i>{html.escape(e['translation'])}</i></div>"
            for e in j.get("evidence", []))
        parts.append(f"<div class='j'><b>{html.escape(j['decision'])}</b>"
                     f"<br>→ {html.escape(j['chosen'])}{ev}</div>")
    comm = d.get("commentary_lines")
    if comm:
        parts.append(f"<h3>{html.escape(meta['commentator'])}'s commentary on this unit</h3>")
        parts += [f"<div class='commline'><span class='n'>{i}</span>"
                  f"{html.escape(ln)}</div>" for i, ln in enumerate(comm, 1)]
    return "\n".join(parts)
