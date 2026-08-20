"""REASON stage (Phase 1, W4): prompt assembly + structured-output calls.

Provider decision (Rohit, 2026-07-15): OpenAI, model pinned in llm.py.
LLM plumbing (cache, usage log, cost accounting) lives in llm.py.
"""

import json
from typing import Optional

from .llm import (MAX_COMPLETION_TOKENS, MODEL, REASONING_EFFORT,  # noqa: F401
                  chat as _chat, client, estimated_cost, load_env, total_spend)
from .retrieve import RetrievalBundle
from .schema import Apparatus
from .texts import AGENT_DIR

PROMPT_PATH = AGENT_DIR / "prompts" / "reasoner_v1.md"

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


PROMPT_V2_PATH = AGENT_DIR / "prompts" / "reasoner_v2.md"


def _lib_user_turn(lt, unit, analyze: dict, mw: dict) -> str:
    analyze_txt = json.dumps(
        {k: v for k, v in analyze.items() if k != "slm_parsed"},
        ensure_ascii=False, indent=1)
    mw_txt = "\n".join(
        f"- {lem}: " + " | ".join(f"[{e['citation']}] {e['text']}" for e in entries)
        for lem, entries in mw.items()) or "none retrieved"
    caveats = lt.source.get("caveats")
    caveat_note = f"\nSOURCE CAVEATS: {caveats}" if caveats else ""
    comm = (unit.commentary_numbered()
            or "(the commentary is silent on this unit — grammar and dictionary only)")
    return f"""## UNIT {unit.id} of {lt.title}{caveat_note}

Set `unit` to: {unit.id}

{unit.mula}

## ANALYZE (ByT5-Sanskrit on the unit text)

{analyze_txt}

## COMMENTARY on this unit (cite these line numbers; tag: {lt.citation_tag} {unit.id})

{comm}

## DICTIONARY (MW, cite as given)

{mw_txt}

Produce the apparatus now."""


def reason_unit(
    lt, unit, analyze: dict, mw: dict,
    feedback: Optional[str] = None,
    prior=None,
):
    from .schema import LibApparatus

    messages = [
        {"role": "system", "content": PROMPT_V2_PATH.read_text(encoding="utf-8")},
        {"role": "user", "content": _lib_user_turn(lt, unit, analyze, mw)},
    ]
    if feedback and prior is not None:
        messages += [
            {"role": "assistant", "content": prior.model_dump_json()},
            {"role": "user", "content":
                "The Pāṇinian verifier (vidyut-prakriya) rejected these claims:\n"
                f"{feedback}\n\nRevise the apparatus per the system instructions "
                "(correct only what is wrong; keep everything else stable)."},
        ]
    tag = f"reason-{lt.slug}-{unit.id}" + ("-retry" if feedback else "")
    return _chat(messages, LibApparatus, tag)


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
