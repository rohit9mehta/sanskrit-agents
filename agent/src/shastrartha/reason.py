"""REASON stage (Phase 1, W4): OpenAI structured-output call.

Provider decision (Rohit, 2026-07-15): OpenAI key from PROJECT_ROOT/.env,
model pinned to a dated flagship snapshot. Every request/response is cached
to disk keyed by payload hash (reproducible reruns; free re-renders), and
every live call appends a usage record to agent/logs/llm_usage.jsonl.
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Optional

from .retrieve import RetrievalBundle
from .schema import Apparatus
from .texts import AGENT_DIR, DATA_DIR, LOGS_DIR, PROJECT_ROOT

MODEL = "gpt-5.5-2026-04-23"  # verified available on the supplied key, 2026-07-15
REASONING_EFFORT = "high"
MAX_COMPLETION_TOKENS = 32000
PROMPT_PATH = AGENT_DIR / "prompts" / "reasoner_v1.md"
LLM_CACHE = DATA_DIR / "cache" / "llm"
USAGE_LOG = LOGS_DIR / "llm_usage.jsonl"

# Conservative $/1M estimates for cost accounting (exact gpt-5.5 pricing not
# in local references; the run-level hard stop uses these upper bounds).
PRICE_IN, PRICE_OUT = 3.0, 15.0

_client = None


def load_env() -> None:
    env = PROJECT_ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def client():
    global _client
    if _client is None:
        load_env()
        from openai import OpenAI

        _client = OpenAI()
    return _client


def estimated_cost(usage: dict) -> float:
    return (usage.get("prompt_tokens", 0) * PRICE_IN
            + usage.get("completion_tokens", 0) * PRICE_OUT) / 1e6


def total_spend() -> float:
    if not USAGE_LOG.exists():
        return 0.0
    return sum(
        json.loads(x).get("est_cost", 0.0)
        for x in USAGE_LOG.read_text().splitlines() if x.strip()
    )


def _log_usage(tag: str, usage: dict) -> None:
    USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tag": tag, "model": MODEL, **usage, "est_cost": estimated_cost(usage),
    }
    with USAGE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


def _chat(messages: list[dict], response_format, tag: str, use_cache: bool = True):
    """Structured-output chat call with disk cache. Returns (parsed_or_text, usage)."""
    payload = {
        "model": MODEL, "messages": messages, "effort": REASONING_EFFORT,
        "schema": getattr(response_format, "__name__", str(response_format)),
    }
    key = hashlib.sha256(
        json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()[:32]
    cache_file = LLM_CACHE / f"{key}.json"
    if use_cache and cache_file.exists():
        blob = json.loads(cache_file.read_text())
        parsed = (response_format.model_validate(blob["parsed"])
                  if response_format is not str else blob["parsed"])
        return parsed, blob["usage"]

    kwargs = dict(model=MODEL, messages=messages,
                  max_completion_tokens=MAX_COMPLETION_TOKENS)
    if REASONING_EFFORT:
        kwargs["reasoning_effort"] = REASONING_EFFORT
    try:
        resp = _do_call(kwargs, response_format)
    except Exception as e:
        if "reasoning_effort" in str(e):
            kwargs.pop("reasoning_effort", None)
            resp = _do_call(kwargs, response_format)
        else:
            raise

    choice = resp.choices[0]
    if getattr(choice.message, "refusal", None):
        raise RuntimeError(f"model refusal: {choice.message.refusal[:200]}")
    if response_format is str:
        parsed = choice.message.content
        dump = parsed
    else:
        parsed = choice.message.parsed
        if parsed is None:
            raise RuntimeError(f"no parsed output (finish_reason={choice.finish_reason})")
        dump = parsed.model_dump()
    usage = {
        "prompt_tokens": resp.usage.prompt_tokens,
        "completion_tokens": resp.usage.completion_tokens,
    }
    details = getattr(resp.usage, "completion_tokens_details", None)
    if details is not None and getattr(details, "reasoning_tokens", None) is not None:
        usage["reasoning_tokens"] = details.reasoning_tokens
    _log_usage(tag, usage)

    LLM_CACHE.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(
        json.dumps({"payload": payload, "parsed": dump, "usage": usage},
                   ensure_ascii=False))
    return parsed, usage


def _do_call(kwargs: dict, response_format):
    c = client()
    if response_format is str:
        return c.chat.completions.create(**kwargs)
    return c.chat.completions.parse(**kwargs, response_format=response_format)


NO_COMMENTARY_NOTE = (
    "\n\n## NOTE (ablation run)\n\nNo commentary is available for this run. "
    "Base every decision on the grammar, the analyzer output, and the "
    "dictionary alone. Justifications must NOT cite trbh lines (use empty "
    "`lines` lists and set depends_on_commentary=false); describe your "
    "grammatical/lexical reasoning instead."
)


def _user_turn(b: RetrievalBundle, include_commentary: bool = True) -> str:
    variants = ("\n".join(f"- bhāṣya `{v['bhasya']}` vs vulgate `{v['vulgate']}`"
                          for v in b.variants) or "none")
    analyze_txt = json.dumps(
        {k: v for k, v in b.analyze.items() if k != "slm_parsed"},
        ensure_ascii=False, indent=1)
    mw_txt = "\n".join(
        f"- {lem}: " + " | ".join(f"[{e['citation']}] {e['text']}" for e in entries)
        for lem, entries in b.mw.items()) or "none retrieved"
    shared = (f"\nNOTE: verses {b.verse} and {b.shared_with} are quoted back-to-back "
              "and share this exposition." if b.shared_with else "")
    commentary_sections = (
        f"""

## COMMENTARY SPAN (trbh {b.span[0]}–{b.span[1]}, line-numbered)

{b.commentary_block()}

## SEGMENTED COUNTERPART (2022 model output — convenience gloss, known ~15% line error rate)

{chr(10).join(b.unsandhied_lines)}"""
        if include_commentary else NO_COMMENTARY_NOTE
    )
    return f"""## VERSE {b.verse} (bhāṣya reading; quoted at trbh {b.anchor})

{b.verse_text}

Vulgate reading (for variants only): {b.vulgate_text}
Variant readings (skeleton-diff hunks): {variants}{shared}

## ANALYZE (ByT5-Sanskrit on the verse lines)

{analyze_txt}{commentary_sections}

## DICTIONARY (MW, cite as given)

{mw_txt}

Produce the apparatus now."""


def reason(
    bundle: RetrievalBundle,
    feedback: Optional[str] = None,
    prior: Optional[Apparatus] = None,
    include_commentary: bool = True,
) -> tuple[Apparatus, dict]:
    messages = [
        {"role": "system", "content": PROMPT_PATH.read_text(encoding="utf-8")},
        {"role": "user", "content": _user_turn(bundle, include_commentary)},
    ]
    if feedback and prior is not None:
        messages += [
            {"role": "assistant", "content": prior.model_dump_json()},
            {"role": "user", "content":
                "The Pāṇinian verifier (vidyut-prakriya) rejected these claims:\n"
                f"{feedback}\n\nRevise the apparatus per the system instructions "
                "(correct only what is wrong; keep everything else stable)."},
        ]
    tag = (f"reason-v{bundle.verse:02d}"
           + ("" if include_commentary else "-nocomm")
           + ("-retry" if feedback else ""))
    return _chat(messages, Apparatus, tag)
