"""Local demo server for the ask-box + library explorer (Phase 3, L6).

  uv run python scripts/20_serve.py        # http://localhost:8008

Routes:
  /                     ask box + library shelf
  /api/ask?q=...        JSON answer (OpenAI key stays server-side)
  /unit/<slug>/<unit>   apparatus view (citations click through to here)
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

from shastrartha.ask import ask, build_index
from shastrartha.webui import (apparatus_body, chips_html, md_lite, page,
                               shelf_html)


def _unit_href(slug: str, unit: str) -> str:
    return f"/unit/{slug}/{unit}"


CHIPS = chips_html("pre")

HOME_BODY = """
<div class="searchrow">
  <input type="text" id="q" placeholder="e.g. What is the storehouse consciousness?"
         onkeydown="if(event.key==='Enter')go()">
  <button onclick="go()">Ask</button>
</div>
<div class="samples">Try: """ + CHIPS + """</div>
<div class="spin" id="spin">Reading the commentaries…</div>
<div id="out"></div>
""" + "{shelf}" + """
<script>
function pre(t) { document.getElementById('q').value = t; go(); return false; }
function linkCites(t) {
  return t.replace(/\\[([a-z]+) ([0-9][0-9.]*)\\]/g,
    (m, s, u) => `<a class="cite" href="/unit/${s}/${u}">[${s} ${u}]</a>`);
}
async function go() {
  const q = document.getElementById('q').value.trim();
  if (!q) return;
  document.getElementById('spin').style.display = 'block';
  document.getElementById('out').innerHTML = '';
  const r = await fetch('/api/ask?q=' + encodeURIComponent(q));
  const d = await r.json();
  document.getElementById('spin').style.display = 'none';
  let h = '<div class="answer">' + linkCites(d.answer_html) + '</div>';
  if (d.citations.length) {
    h += '<div class="src"><b>Sources consulted:</b> ' + d.citations.map(c =>
      `<a href="/unit/${c.slug}/${c.unit}">${c.key}</a> (${c.kind})`
    ).join(' · ') + '</div>';
  }
  document.getElementById('out').innerHTML = h;
  window.scrollTo({top: 0, behavior: 'smooth'});
}
</script>"""


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, body: str, ctype="text/html; charset=utf-8", code=200):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/":
            self._send(page(HOME_BODY.replace("{shelf}", shelf_html(_unit_href))))
        elif u.path == "/api/ask":
            q = parse_qs(u.query).get("q", [""])[0]
            res = ask(q)
            res["answer_html"] = md_lite(res.pop("answer"))
            self._send(json.dumps(res, ensure_ascii=False),
                       "application/json; charset=utf-8")
        elif u.path.startswith("/unit/"):
            _, _, slug, unit = u.path.split("/", 3)
            self._send(page(apparatus_body(slug, unquote(unit), "/", _unit_href)))
        else:
            self._send("not found", code=404)


def main() -> int:
    n_chunks = len(build_index()[0])
    port = 8008
    print(f"index: {n_chunks} chunks | http://localhost:{port}")
    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
