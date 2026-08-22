"""LLM client plumbing: model pin, .env key loading, disk cache, usage log.

Shared by the pipeline (reason.py), the ask-box (ask.py), and the deployed
Space. Import surface: chat(), MODEL, total_spend(), estimated_cost().
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from .texts import AGENT_DIR, DATA_DIR, LOGS_DIR, PROJECT_ROOT

# Model roles (2026-08-21: moved to the GPT-5.6 suite; 5.5 retained in the
# table because the 171 stored apparatuses and the human-eval packets were
# produced with it).  SHASTRARTHA_MODEL overrides the reasoner for A/B runs.
REASONER_MODEL = os.environ.get("SHASTRARTHA_MODEL", "gpt-5.6-sol")
ASK_MODEL = os.environ.get("SHASTRARTHA_ASK_MODEL", "gpt-5.6-luna")
MODEL = REASONER_MODEL  # back-compat alias (reason.py, runner meta)
REASONING_EFFORT = "high"
ASK_EFFORT = "medium"
MAX_COMPLETION_TOKENS = 32000
LLM_CACHE = DATA_DIR / "cache" / "llm"
USAGE_LOG = LOGS_DIR / "llm_usage.jsonl"

# $/1M tokens (input, output). 5.6 per developers.openai.com/api/docs/models
# (2026-08-21); 5.5 is the conservative estimate used since Phase 1.
PRICES = {
    "gpt-5.5-2026-04-23": (3.0, 15.0), "gpt-5.5": (3.0, 15.0),
    "gpt-5.6-sol": (4.0, 20.0), "gpt-5.6-terra": (2.0, 12.0), "gpt-5.6-luna": (0.20, 1.20),
}
PRICE_IN, PRICE_OUT = PRICES.get(REASONER_MODEL, (4.0, 20.0))

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


def estimated_cost(usage: dict, model: str | None = None) -> float:
    pi, po = PRICES.get(model or REASONER_MODEL, (PRICE_IN, PRICE_OUT))
    return (usage.get("prompt_tokens", 0) * pi
            + usage.get("completion_tokens", 0) * po) / 1e6


def total_spend() -> float:
    if not USAGE_LOG.exists():
        return 0.0
    return sum(
        json.loads(x).get("est_cost", 0.0)
        for x in USAGE_LOG.read_text().splitlines() if x.strip()
    )


def _log_usage(tag: str, usage: dict, model: str) -> None:
    USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tag": tag, "model": model, **usage, "est_cost": estimated_cost(usage, model),
    }
    with USAGE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


def chat(messages: list[dict], response_format, tag: str, use_cache: bool = True,
          effort: str | None = None, model: str | None = None):
    """Structured-output chat call with disk cache. Returns (parsed_or_text, usage).
    `model` defaults to the reasoner; the ask-box passes ASK_MODEL."""
    effort = effort or REASONING_EFFORT
    model = model or REASONER_MODEL
    payload = {
        "model": model, "messages": messages, "effort": effort,
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

    kwargs = dict(model=model, messages=messages,
                  max_completion_tokens=MAX_COMPLETION_TOKENS)
    if effort:
        kwargs["reasoning_effort"] = effort
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
    usage["est_cost"] = round(estimated_cost(usage, model), 4)
    _log_usage(tag, usage, model)

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




_chat = chat  # back-compat alias
