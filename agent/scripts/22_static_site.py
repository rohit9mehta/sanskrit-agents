"""Export the demo as a static site for GitHub Pages (repo /docs).

The live server needs the OpenAI key for free-form questions; a public static
page must not carry the key. So the static site ships:
  * every apparatus page (full library, browsable);
  * the shelf/coverage section;
  * PRE-COMPUTED answers for the curated questions (from the committed
    store, agent/data/canned_answers.json; a question the store lacks is
    computed once through the exact same ask() path and persisted);
  * a free-text box that matches against the canned set and otherwise
    explains how to run the live version.

Layout (relative links, works under any subpath):
  docs/index.html
  docs/unit/<slug>/<unit>.html
"""

import json
import re
import sys

from shastrartha.canned import canned_answer
from shastrartha.texts import PROJECT_ROOT
from shastrartha.webui import (ABOUT_HTML, CANNED_QUESTIONS, apparatus_body,
                               chips_html, md_lite, page, shelf_html)

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
    for q in CANNED_QUESTIONS:
        res = canned_answer(q)
        answers[q] = {
            "answer_html": link_cites(md_lite(res["answer"])),
            "citations": res["citations"],
        }
        print("canned |", q)

    chips = chips_html("show")
    body = """
<div class="searchrow">
  <input type="text" id="q" placeholder="Pick a question below, or type to search them"
         onkeydown="if(event.key==='Enter')free()">
  <button onclick="free()">Ask</button>
</div>
<div class="samples">""" + chips + """</div>
""" + ABOUT_HTML + """
<div id="out"></div>
<div class="note" style="margin-top:1rem">This page answers the curated
questions above, pre-computed through the full pipeline. To ask anything in your
own words, use the live version at
<a class="cite" href="https://shastrartha.onrender.com">shastrartha.onrender.com</a>
(rate-limited; may take a minute to wake). Source:
github.com/rohit9mehta/sanskrit-agents</div>
{shelf}
<script>
var A = """ + json.dumps(answers, ensure_ascii=False) + """;
function render(q) {
  var d = A[q];
  var h = '<div class="answer">' + d.answer_html + '</div>';
  if (d.citations.length) {
    var seen = {};
    var uniq = d.citations.filter(function(c){
      return seen[c.key] ? false : (seen[c.key] = true);
    });
    h += '<div class="src"><b>Sources consulted:</b> ' + uniq.map(function(c){
      return '<a href="unit/' + c.slug + '/' + c.unit + '.html">' + c.key + '</a>';
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
    document.getElementById('out').innerHTML = '<div class="answer">This page only ' +
    'answers the curated questions above. For your own questions, use the live version: ' +
    '<a class="cite" href="https://shastrartha.onrender.com">shastrartha.onrender.com</a> ' +
    '(it composes answers from the same cited library and refuses anything outside it).</div>';
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
