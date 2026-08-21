"""Canonical store of pre-computed canned answers: agent/data/canned_answers.json.

Canned answers are versioned data, not a build-time byproduct: recomputing
one costs real LLM money and the phrasings are retrieval-tested. The site
builders (scripts 22/23) read the store and fall back to ask() — persisting
the result — only for a question the store has never seen, so routine
rebuilds need no API key. Keys are exact question strings (the store may
hold retired questions beyond the live webui.CANNED_QUESTIONS set); values
are {"answer": raw answer text, "citations": [{key, slug, unit, kind}]}.
"""

import json

from .texts import DATA_DIR

STORE = DATA_DIR / "canned_answers.json"


def canned_answer(q: str) -> dict:
    store = json.loads(STORE.read_text(encoding="utf-8")) if STORE.exists() else {}
    if q not in store:
        from .ask import ask

        res = ask(q)
        store[q] = {
            "answer": res["answer"],
            "citations": [
                {"key": c["key"], "slug": c["slug"], "unit": c["unit"],
                 "kind": c["kind"]} for c in res.get("citations", [])],
        }
        STORE.write_text(json.dumps(store, ensure_ascii=False, indent=1),
                         encoding="utf-8")
    return store[q]
