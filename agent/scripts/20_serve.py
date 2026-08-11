"""Local demo server for the ask-box + library explorer (Phase 3, L6).

  uv run python scripts/20_serve.py        # http://localhost:8008

Routes:
  /                     ask box
  /api/ask?q=...        JSON answer
  /unit/<slug>/<unit>   apparatus view (citations click through to here)
Stdlib only; the OpenAI key is read server-side (never sent to the page).
"""

import html
import json
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

from shastrartha.ask import TEXT_META, ask, build_index
from shastrartha.texts import AGENT_DIR

OUTPUT = AGENT_DIR / "output"

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
.samples a { color:var(--accent); text-decoration:none; margin-right:.9rem; }
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
"""

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<title>Śāstrārtha — ask the śāstras</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{css}</style></head><body><div class="wrap">
<h1><a href="/">Śāstrārtha</a></h1>
<div class="sub">Ask the śāstras — every answer cited to the tradition's own commentaries.</div>
<div class="searchrow">
  <input type="text" id="q" placeholder="e.g. What is the storehouse consciousness?"
         onkeydown="if(event.key==='Enter')go()">
  <button onclick="go()">Ask</button>
</div>
<div class="samples">Try:
  <a href="#" onclick="return pre('What is the storehouse consciousness?')">storehouse consciousness</a>
  <a href="#" onclick="return pre('What does the Gita say about acting without attachment to results?')">karma without attachment</a>
  <a href="#" onclick="return pre('How does Vyasa define yoga?')">definition of yoga</a>
  <a href="#" onclick="return pre('What happens to one who worships only ignorance?')">Īśopaniṣad on ignorance</a>
</div>
<div class="spin" id="spin">Reading the commentaries…</div>
<div id="out"></div>
</div>
<script>
function pre(t) { document.getElementById('q').value = t; go(); return false; }
function linkCites(t) {
  return t.replace(/\[([a-z]+) ([0-9][0-9.]*)\]/g,
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
}
</script></body></html>"""


def _md_lite(text: str) -> str:
    t = html.escape(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", t)
    return t


def _apparatus_page(slug: str, unit: str) -> str:
    meta = TEXT_META.get(slug, {"title": slug, "tag": slug})
    if slug == "trimsika":
        path = OUTPUT / f"v{int(unit):02d}" / "apparatus.json"
    else:
        path = OUTPUT / slug / unit.replace(".", "_") / "apparatus.json"
    if not path.exists():
        return f"<p>No apparatus for {slug} {unit} yet.</p><p><a href='/'>← back</a></p>"
    d = json.loads(path.read_text(encoding="utf-8"))
    from shastrartha.ask import _trimsika_mula

    mula = d.get("mula") or (_trimsika_mula(unit) if slug == "trimsika" else "")
    vs = d.get("verification_summary", {})
    parts = [f"<p><a href='/'>← ask</a></p>",
             f"<h2>{html.escape(meta['title'])} — {html.escape(unit)}</h2>",
             f"<div class='mula'>{html.escape(mula)}</div>",
             f"<p><b>Translation.</b> {_md_lite(d.get('translation',''))}</p>",
             f"<p>Verification: {vs.get('pass',0)} pass"
             f" / {vs.get('fail',0)} fail / {vs.get('unsupported',0)} unsupported"
             f"<span class='badge'>grammar-checked</span></p>",
             "<h3>Word by word</h3><table><tr><th>surface</th><th>lemma</th><th>vidyut</th></tr>"]
    for w in d.get("analysis", []):
        v = w.get("verification", {})
        badge = ("<span class='badge'>pass</span>" if v.get("status") == "pass"
                 else f"<span class='badge bad'>{v.get('status','?')}</span>")
        parts.append(f"<tr><td>{html.escape(w['surface'])}</td>"
                     f"<td>{html.escape(w['lemma'])}</td><td>{badge}</td></tr>")
    parts.append("</table><h3>Commentary-grounded decisions</h3>")
    for j in d.get("justifications", []):
        ev = "".join(
            f"<div class='commline'><span class='n'>{meta['tag']} {e['lines']}</span>"
            f"{html.escape(e['quote'])}<br><i>{html.escape(e['translation'])}</i></div>"
            for e in j.get("evidence", []))
        parts.append(f"<div class='j'><b>{html.escape(j['decision'])}</b>"
                     f"<br>→ {html.escape(j['chosen'])}{ev}</div>")
    comm = d.get("commentary_lines")
    if comm:
        parts.append("<h3>The commentary (this unit)</h3>")
        parts += [f"<div class='commline'><span class='n'>{i}</span>"
                  f"{html.escape(ln)}</div>" for i, ln in enumerate(comm, 1)]
    return "\n".join(parts)


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
            self._send(PAGE.replace("{css}", CSS))
        elif u.path == "/api/ask":
            q = parse_qs(u.query).get("q", [""])[0]
            res = ask(q)
            res["answer_html"] = _md_lite(res.pop("answer"))
            self._send(json.dumps(res, ensure_ascii=False),
                       "application/json; charset=utf-8")
        elif u.path.startswith("/unit/"):
            _, _, slug, unit = u.path.split("/", 3)
            body = _apparatus_page(slug, unquote(unit))
            self._send(PAGE.replace("{css}", CSS).split("<div class=\"searchrow\">")[0]
                       + body + "</div></body></html>")
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
