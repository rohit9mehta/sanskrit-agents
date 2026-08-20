"""Śāstrārtha demo server for Hugging Face Spaces (Docker Space, port 7860).

Same UI as the local demo, plus the protections a public ask-box needs:

  * canned questions are served from canned.json — no LLM call, no cap charge;
  * live questions are rate-limited per visitor (per-IP sliding windows) and
    globally capped per UTC day by call count AND estimated dollars;
  * when a cap trips, the visitor gets a friendly note and the canned set —
    the library stays fully browsable at all times;
  * questions are length-capped; the OpenAI key exists only as a Space
    secret (env var), never in the repo or the page.

Limits are env-tunable: RL_PER_MIN, RL_PER_DAY, RL_GLOBAL_CALLS_PER_DAY,
RL_GLOBAL_USD_PER_DAY, RL_MAX_QLEN.
"""

import json
import os
import sys
import time
from collections import defaultdict, deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import parse_qs, unquote, urlparse

sys.path.insert(0, str(Path(__file__).parent / "agent" / "src"))

from shastrartha.ask import ask  # noqa: E402
from shastrartha.llm import estimated_cost  # noqa: E402
from shastrartha.webui import (apparatus_body, chips_html, md_lite,  # noqa: E402
                               page, shelf_html)

CANNED = json.loads((Path(__file__).parent / "canned.json").read_text(encoding="utf-8"))

PER_MIN = int(os.environ.get("RL_PER_MIN", "4"))
PER_DAY = int(os.environ.get("RL_PER_DAY", "20"))
GLOBAL_CALLS_PER_DAY = int(os.environ.get("RL_GLOBAL_CALLS_PER_DAY", "150"))
GLOBAL_USD_PER_DAY = float(os.environ.get("RL_GLOBAL_USD_PER_DAY", "3.0"))
MAX_QLEN = int(os.environ.get("RL_MAX_QLEN", "300"))

_lock = Lock()
_per_ip_min: dict[str, deque] = defaultdict(deque)   # timestamps, 60s window
_per_ip_day: dict[str, deque] = defaultdict(deque)   # timestamps, 86400s window
_day_key = [""]
_global_calls = [0]
_global_usd = [0.0]

LIMIT_MSG = ("The public demo has reached its budget for now (it runs on a "
             "capped research account). The pre-computed questions below still "
             "work, the whole library stays browsable, and the project is "
             "open source if you want to run unlimited asking locally: "
             "github.com/rohit9mehta/sanskrit-agents")
IP_MSG = ("You've hit the per-visitor limit for live questions (they cost "
          "real inference money on a research budget). The pre-computed "
          "questions and the full library remain open — or come back in a "
          "bit.")


def _utc_day() -> str:
    return time.strftime("%Y-%m-%d", time.gmtime())


def _roll_day() -> None:
    d = _utc_day()
    if _day_key[0] != d:
        _day_key[0] = d
        _global_calls[0] = 0
        _global_usd[0] = 0.0
        _per_ip_day.clear()


def _window_ok(dq: deque, window: float, cap: int, now: float) -> bool:
    while dq and now - dq[0] > window:
        dq.popleft()
    return len(dq) < cap


def check_limits(ip: str) -> str | None:
    """None if allowed; else a user-facing message. Reserves the slot."""
    now = time.time()
    with _lock:
        _roll_day()
        if _global_calls[0] >= GLOBAL_CALLS_PER_DAY or _global_usd[0] >= GLOBAL_USD_PER_DAY:
            return LIMIT_MSG
        if not _window_ok(_per_ip_min[ip], 60, PER_MIN, now):
            return IP_MSG
        if not _window_ok(_per_ip_day[ip], 86400, PER_DAY, now):
            return IP_MSG
        _per_ip_min[ip].append(now)
        _per_ip_day[ip].append(now)
        _global_calls[0] += 1
        return None


def record_usage(usage: dict) -> None:
    with _lock:
        _global_usd[0] += estimated_cost(usage or {})


def _unit_href(slug: str, unit: str) -> str:
    return f"/unit/{slug}/{unit}"


CHIPS = chips_html("pre")

HOME_BODY = """
<div class="searchrow">
  <input type="text" id="q" maxlength="300"
         placeholder="Ask in English; answers come only from the library, cited"
         onkeydown="if(event.key==='Enter')go()">
  <button onclick="go()">Ask</button>
</div>
<div class="samples">Try: """ + CHIPS + """</div>
<div class="spin" id="spin">Reading the commentaries…</div>
<div id="out"></div>
""" + "{shelf}" + """
<div class="note" style="margin-top:1rem">A research prototype: translations are
machine drafts, commentary-grounded and grammar-checked, awaiting expert review.
Live questions are rate-limited; the curated questions are always available.
Source: github.com/rohit9mehta/sanskrit-agents</div>
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
  if (d.citations && d.citations.length) {
    h += '<div class="src"><b>Sources consulted:</b> ' + d.citations.map(c =>
      `<a href="/unit/${c.slug}/${c.unit}">${c.key}</a> (${c.kind})`
    ).join(' · ') + '</div>';
  }
  document.getElementById('out').innerHTML = h;
}
</script>"""


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _ip(self) -> str:
        fwd = self.headers.get("X-Forwarded-For", "")
        return fwd.split(",")[0].strip() if fwd else (self.client_address[0] or "?")

    def _send(self, body: str, ctype="text/html; charset=utf-8", code=200):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _api_ask(self, q: str) -> dict:
        if q in CANNED:
            c = CANNED[q]
            return {"answer_html": c["answer_html_plain"],
                    "citations": c["citations"], "canned": True}
        if len(q) > MAX_QLEN:
            return {"answer_html": md_lite("Please keep questions under "
                                           f"{MAX_QLEN} characters."),
                    "citations": []}
        msg = check_limits(self._ip())
        if msg is not None:
            return {"answer_html": md_lite(msg), "citations": [], "limited": True}
        try:
            res = ask(q)
        except Exception as e:  # never an empty body toward the visitor
            print(f"ask error: {type(e).__name__}: {e}", flush=True)
            return {"answer_html": md_lite(
                "Something went wrong composing the answer. The curated "
                "questions and the library below still work."), "citations": []}
        if res.get("llm"):
            record_usage(res.get("usage", {}))
        return {"answer_html": md_lite(res["answer"]),
                "citations": res.get("citations", [])}

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/":
            self._send(page(HOME_BODY.replace("{shelf}", shelf_html(_unit_href))))
        elif u.path == "/healthz":
            self._send("ok", "text/plain")
        elif u.path == "/api/ask":
            q = parse_qs(u.query).get("q", [""])[0].strip()
            self._send(json.dumps(self._api_ask(q), ensure_ascii=False),
                       "application/json; charset=utf-8")
        elif u.path.startswith("/unit/"):
            _, _, slug, unit = u.path.split("/", 3)
            self._send(page(apparatus_body(slug, unquote(unit), "/", _unit_href)))
        else:
            self._send("not found", code=404)


def main() -> int:
    port = int(os.environ.get("PORT", "7860"))
    print(f"listening on 0.0.0.0:{port} | limits: {PER_MIN}/min "
          f"{PER_DAY}/day/ip, {GLOBAL_CALLS_PER_DAY} calls "
          f"${GLOBAL_USD_PER_DAY}/day global")
    ThreadingHTTPServer(("0.0.0.0", port), H).serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
