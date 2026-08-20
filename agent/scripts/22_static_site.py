"""Export the demo as a static site for GitHub Pages (repo /docs).

The live server needs the OpenAI key for free-form questions; a public static
page must not carry the key. So the static site ships:
  * every apparatus page (full library, browsable);
  * the shelf/coverage section;
  * PRE-COMPUTED answers for the curated questions (computed here, once,
    through the exact same ask() path — citations and refusal included);
  * a free-text box that matches against the canned set and otherwise
    explains how to run the live version.

Layout (relative links, works under any subpath):
  docs/index.html
  docs/unit/<slug>/<unit>.html
"""

import json
import re
import sys

from shastrartha.ask import ask
from shastrartha.texts import PROJECT_ROOT
from shastrartha.webui import (CANNED_QUESTIONS, apparatus_body, chips_html,
                               md_lite, page, shelf_html)

DOCS = PROJECT_ROOT / "docs"


def root_unit_href(slug: str, unit: str) -> str:
    return f"unit/{slug}/{unit}.html"


def nested_unit_href(slug: str, unit: str) -> str:
    return f"../../unit/{slug}/{unit}.html"


def link_cites(html_text: str) -> str:
    return re.sub(
        r"\[([a-z]+) ([0-9][0-9.]*)\]",
        lambda m: (f"<a class='cite' href='unit/{m.group(1)}/{m.group(2)}.html'>"
                   f"[{m.group(1)} {m.group(2)}]</a>"),
        html_text)


def main() -> int:
    answers = {}
    for q, label in CANNED_QUESTIONS:
        res = ask(q)
        answers[q] = {
            "label": label,
            "answer_html": link_cites(md_lite(res["answer"])),
            "citations": [
                {"key": c["key"], "slug": c["slug"], "unit": c["unit"],
                 "kind": c["kind"]} for c in res.get("citations", [])
            ],
        }
        print(("canned" if res.get("llm") else "refusal"), "|", q)

    chips = chips_html("show")
    body = """
<div class="searchrow">
  <input type="text" id="q" placeholder="Pick a question below, or type to search them"
         onkeydown="if(event.key==='Enter')free()">
  <button onclick="free()">Ask</button>
</div>
<div class="samples">""" + chips + """</div>
<div id="out"></div>
<div class="note" style="margin-top:1rem">This public demo answers the curated
questions above, pre-computed through the full pipeline. Free-form questions run
in the local/live deployment, where the language model composes from the same
cited library at question time (github.com/rohit9mehta/sanskrit-agents).</div>
{shelf}
<script>
var A = """ + json.dumps(answers, ensure_ascii=False) + """;
function render(q) {
  var d = A[q];
  var h = '<div class="answer">' + d.answer_html + '</div>';
  if (d.citations.length) {
    h += '<div class="src"><b>Sources consulted:</b> ' + d.citations.map(function(c){
      return '<a href="unit/' + c.slug + '/' + c.unit + '.html">' + c.key + '</a> (' + c.kind + ')';
    }).join(' · ') + '</div>';
  }
  document.getElementById('out').innerHTML = h;
}
function show(q) { document.getElementById('q').value = q; render(q); return false; }
function free() {
  var q = document.getElementById('q').value.trim().toLowerCase();
  if (!q) return;
  var keys = Object.keys(A);
  var best = null, bestScore = 0;
  keys.forEach(function(k){
    var words = q.split(/\\s+/), score = 0;
    words.forEach(function(w){ if (k.toLowerCase().indexOf(w) >= 0) score++; });
    if (score > bestScore) { bestScore = score; best = k; }
  });
  if (best && bestScore >= 2) { document.getElementById('q').value = best; render(best); }
  else {
    document.getElementById('out').innerHTML = '<div class="answer">This public page ' +
    'answers the curated questions above. For free-form questions, run the live ' +
    'server (see the note below) — it composes answers from the same cited library ' +
    'and refuses anything outside it.</div>';
  }
}
</script>"""

    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "index.html").write_text(
        page(body.replace("{shelf}", shelf_html(root_unit_href)), home_href="index.html"),
        encoding="utf-8")

    n = 0
    from shastrartha.webui import units_of
    from shastrartha.ask import TEXT_META
    for slug in TEXT_META:
        for unit in units_of(slug):
            out = DOCS / "unit" / slug / f"{unit}.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(
                page(apparatus_body(slug, unit, "../../index.html", nested_unit_href),
                     home_href="../../index.html"),
                encoding="utf-8")
            n += 1
    print(f"wrote docs/: index + {n} unit pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
