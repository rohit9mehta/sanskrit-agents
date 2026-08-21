"""Score the current analyzer (local ByT5-Sanskrit) on the frozen benchmark.

This produces the BASELINE NUMBER every later candidate (other base models,
the post-trained analyzer) is compared against.

ByT5's SLM morph tags (SNM, SPr3In, …) are undocumented, so step A learns
the tag→feature mapping empirically: run the model over vidyut-verified DCS
items that are NOT in the benchmark (split_v1.json exclusions respected),
align tokens by surface, majority-vote each tag against gold features.
Step B then scores the benchmark through that mapping.

The mapping is decoding of ByT5's fixed tagset, not training — but it is
still learned strictly from training-side data to keep the benchmark clean.

Outputs (agent/data/benchmark/):
  byt5_tagmap.json          learned tag → features (with vote counts)
  results_byt5_v1.jsonl     per-item predictions & verdicts
  baseline_report.md        headline numbers + per-stratum table
Cache: agent/data/cache/byt5_slm/<sha>.json per sentence.
"""

import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AGENT / "src"))

from shastrartha.analyze import local_analyze, parse_slm  # noqa: E402

TRAIN = AGENT / "data" / "training"
BENCH = AGENT / "data" / "benchmark"
CACHE = AGENT / "data" / "cache" / "byt5_slm"

MAX_LEARN_SENTENCES = 700
MAX_LEARN_CHARS = 160     # short sentences: fast decode, no truncation risk
MIN_VOTES = 3          # a tag needs this many gold votes to enter the map
BATCH = 16

SUB_FIELDS = ("vibhakti", "vacana", "linga")
TIN_FIELDS = ("lakara", "purusha", "vacana")


def fold(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[̀-ͯ']", "", s)


def slm_cached(sentences: list[str]) -> dict[str, str]:
    """sentence → raw SLM output, disk-cached."""
    CACHE.mkdir(parents=True, exist_ok=True)
    out, missing = {}, []
    for s in sentences:
        key = hashlib.sha256(("SLM " + s).encode()).hexdigest()[:24]
        p = CACHE / f"{key}.json"
        if p.exists():
            out[s] = json.loads(p.read_text(encoding="utf-8"))["output"]
        else:
            missing.append(s)
    missing.sort(key=len)          # length buckets → less padding, right-sized decode
    for i in range(0, len(missing), BATCH):
        batch = missing[i:i + BATCH]
        budget = min(1024, 3 * max(len(b) for b in batch) + 64)
        for s, o in zip(batch, local_analyze(batch, task="SLM",
                                             max_new_tokens=budget)):
            key = hashlib.sha256(("SLM " + s).encode()).hexdigest()[:24]
            (CACHE / f"{key}.json").write_text(
                json.dumps({"sentence": s, "output": o}, ensure_ascii=False),
                encoding="utf-8")
            out[s] = o
        done = min(i + BATCH, len(missing))
        print(f"  byt5 {done}/{len(missing)}")
    return out


def align(surface: str, parsed: list[dict]) -> dict | None:
    want = fold(surface)
    for tok in parsed:
        if "surface" in tok and fold(tok["surface"]) == want:
            return tok
    return None


def gold_tuple(gold: dict) -> tuple:
    fields = TIN_FIELDS if gold["pos"] == "tinanta" else SUB_FIELDS
    return tuple(gold.get(f) for f in fields)


def gold_lemma(gold: dict) -> str:
    if gold["pos"] == "tinanta":
        return "".join(gold.get("prefixes") or []) + (gold.get("root") or "")
    return gold.get("stem") or gold.get("lemma") or ""

# ByT5 (DCS-derived) tag grammar, recovered from the learned map:
#   nominal  [S|Du|P][N|A|I|D|B|G|L|V](extras)[M|F|Ne]
#   verbal   [S|Du|P](Pr|Ps|Fu)?[1-3](Im)?(In|O|Im)(extras)
# NOTE `Ps` is DCS's coarse Tense=Past: ByT5 cannot distinguish Liṭ/Luṅ/Laṅ-
# perfect from aorist; we decode it to Liṭ (the majority in the learned map),
# so aorist items score as wrong — a structural gap, not a scoring artifact.
_NUM = {"S": "Eka", "Du": "Dvi", "P": "Bahu"}
_CASE = {"N": "Prathama", "A": "Dvitiya", "I": "Trtiya", "D": "Caturthi",
         "B": "Panchami", "G": "Sasthi", "L": "Saptami", "V": "Sambodhana"}
_GEN = {"M": "Pum", "F": "Stri", "Ne": "Napumsaka"}
_PERS = {"1": "Uttama", "2": "Madhyama", "3": "Prathama"}
_NOM_RE = re.compile(r"^(Du|S|P)([NAIDBGLV])(?:.*?)(Ne|M|F)$")
_VERB_RE = re.compile(r"^(Du|S|P)(Pr|Ps|Fu)?([123])(Im)?(In|O|Im)")


def decode_tag(pos: str, tag: str):
    """Positional decode → feature tuple (SUB_FIELDS / TIN_FIELDS order) or None."""
    if pos == "subanta":
        m = _NOM_RE.match(tag)
        if not m:
            return None
        return (_CASE[m.group(2)], _NUM[m.group(1)], _GEN[m.group(3)])
    m = _VERB_RE.match(tag)
    if not m:
        return None
    num, tense, pers, impf, mood = m.groups()
    if impf and mood == "In":
        lak = "Lan"
    elif mood == "O":
        lak = "VidhiLin"
    elif mood == "Im":
        lak = "Lot"
    elif tense == "Fu":
        lak = "Lrt"
    elif tense == "Ps":
        lak = "Lit"
    else:
        lak = "Lat"
    return (lak, _PERS[pers], _NUM[num])


def learn_tagmap() -> dict:
    excluded = set(json.loads((TRAIN / "split_v1.json")
                              .read_text(encoding="utf-8"))["excluded_keys"])
    def item_key(surface, claim):
        keep = ("pos", "stem", "linga", "vibhakti", "vacana",
                "root", "prefixes", "prayoga", "lakara", "purusha", "lemma")
        norm = {k: claim[k] for k in keep if claim.get(k) is not None}
        return surface + "‖" + json.dumps(norm, sort_keys=True, ensure_ascii=False)

    by_sent = defaultdict(list)
    for line in (TRAIN / "dcs_verified.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        if item_key(r["surface"], r["claim"]) in excluded:
            continue
        by_sent[r["sent_id"]].append(r)

    # sentences with the most verified tokens give the most votes
    sents_text = {}
    for path in (AGENT / "data" / "dcs" / "raw").glob("*/*.conllu"):
        text = sid = None
        for line in path.open(encoding="utf-8"):
            if line.startswith("# text = "):
                text = line[9:].strip()
            elif line.startswith("# sent_id"):
                sid = line.split("=", 1)[1].strip()
            elif not line.strip() and sid and text:
                sents_text[sid] = text
                text = sid = None

    ranked = sorted((s for s in by_sent if s in sents_text
                     and len(sents_text[s]) <= MAX_LEARN_CHARS),
                    key=lambda s: -len(by_sent[s]) / (1 + len(sents_text[s]) / 40))
    chosen = ranked[:MAX_LEARN_SENTENCES]
    outputs = slm_cached([sents_text[s] for s in chosen])

    votes = defaultdict(Counter)
    for sid in chosen:
        parsed = parse_slm(outputs[sents_text[sid]])
        for r in by_sent[sid]:
            tok = align(r["surface"], parsed)
            if tok is None:
                continue
            pos = r["claim"]["pos"]
            votes[(pos, tok["tag"])][gold_tuple(r["claim"])] += 1

    tagmap = {}
    for (pos, tag), ctr in votes.items():
        tup, n = ctr.most_common(1)[0]
        if sum(ctr.values()) >= MIN_VOTES:
            tagmap[f"{pos}|{tag}"] = {"features": list(tup), "votes": n,
                                      "total": sum(ctr.values())}
    (BENCH / "byt5_tagmap.json").write_text(
        json.dumps(tagmap, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"tagmap: {len(tagmap)} (pos, tag) entries "
          f"from {len(chosen)} sentences")
    return tagmap


def score(tagmap: dict):
    items = [json.loads(l) for l in
             (BENCH / "analyzer_benchmark_v1.jsonl").open(encoding="utf-8")]
    outputs = slm_cached(sorted({it["sentence"] for it in items if it["sentence"]}))

    rows, agg = [], Counter()
    per_stratum = defaultdict(Counter)
    for it in items:
        gold = it["gold"]
        fields = TIN_FIELDS if gold["pos"] == "tinanta" else SUB_FIELDS
        stratum = it.get("stratum", "pipeline-hard")
        verdict = {"id": it["id"], "source": it["source"], "stratum": stratum}
        parsed = parse_slm(outputs.get(it["sentence"], ""))
        tok = align(it["surface"], parsed)
        agg["n"] += 1
        per_stratum[stratum]["n"] += 1
        if tok is None:
            verdict["status"] = "unaligned"
            agg["unaligned"] += 1
            rows.append(verdict)
            continue
        verdict["byt5"] = tok
        lemma_ok = fold(tok.get("lemma", "")) == fold(gold_lemma(gold))
        agg["lemma_ok"] += lemma_ok
        per_stratum[stratum]["lemma_ok"] += lemma_ok
        verdict["lemma_ok"] = lemma_ok

        entry = tagmap.get(f"{gold['pos']}|{tok['tag']}")
        feats = entry["features"] if entry else decode_tag(gold["pos"], tok["tag"])
        verdict["decoded_by"] = "map" if entry else ("positional" if feats else None)
        if feats is None:
            verdict["status"] = "tag_unmapped"
            agg["tag_unmapped"] += 1
            rows.append(verdict)
            continue
        if not entry:
            agg["positional"] += 1
        pred = dict(zip(fields, feats))
        verdict["pred"] = pred
        ok_fields = {f: pred.get(f) == gold.get(f) for f in fields}
        full = all(ok_fields.values())
        for f, ok in ok_fields.items():
            agg[f"{f}_ok"] += ok
            agg[f"{f}_n"] += 1
        agg["features_full_ok"] += full
        agg["claim_ok"] += (full and lemma_ok)
        per_stratum[stratum]["full_ok"] += full
        verdict["fields_ok"] = ok_fields
        verdict["status"] = "scored"
        rows.append(verdict)

    with (BENCH / "results_byt5_v1.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    n = agg["n"]
    aligned = n - agg["unaligned"]
    scored = aligned - agg["tag_unmapped"]

    def pct(x, d):
        return f"{100*x/d:.1f}%" if d else "—"

    strat_rows = "\n".join(
        f"| {s} | {c['n']} | {pct(c['full_ok'], c['n'])} | "
        f"{pct(c['lemma_ok'], c['n'])} |"
        for s, c in sorted(per_stratum.items(), key=lambda kv: -kv[1]["n"]))
    md = [
        "# Analyzer baseline: ByT5-Sanskrit (chronbmm/sanskrit5-multitask)",
        "",
        f"Benchmark: `analyzer_benchmark_v1.jsonl` ({n} items, frozen "
        "2026-08-21). Scoring: learned tag map `byt5_tagmap.json` "
        "(majority vote on non-benchmark DCS gold; decoding, not training).",
        "",
        "## Headline", "",
        f"* aligned (surface found in SLM output): **{pct(aligned, n)}** ({aligned}/{n})",
        f"* tag mapped: {pct(scored, aligned)} of aligned",
        f"* lemma accuracy (of aligned): **{pct(agg['lemma_ok'], aligned)}**",
        f"* morph features all-correct (of all items, unaligned/unmapped count "
        f"as wrong): **{pct(agg['features_full_ok'], n)}**",
        f"* full claim (lemma + features): **{pct(agg['claim_ok'], n)}**", "",
        "## Per-field (of items where the model's tag was decodable; "
        "denominator = items with that field)", "",
        "| field | acc | n |", "|---|---|---|",
        "\n".join(f"| {f} | {pct(agg[f + '_ok'], agg[f + '_n'])} | {agg[f + '_n']} |"
                  for f in ("vibhakti", "vacana", "linga",
                            "lakara", "purusha")), "",
        "## Per-stratum (top by size)", "",
        "| stratum | n | features-full | lemma |", "|---|---|---|---|",
        strat_rows, "",
        f"Tags decoded by the learned map where present, else positionally "
        f"({agg['positional']} items). ByT5's `Ps` tag is DCS's coarse "
        "Tense=Past — the model's tagset cannot distinguish perfect (Liṭ) from "
        "aorist (Luṅ); aorist items therefore score wrong by construction. "
        "This is a structural gap the fine-tune's explicit lakāra target closes.",
        "",
        "Failure modes count against the model: unaligned "
        f"({agg['unaligned']}) usually means wrong segmentation; unmapped tag "
        f"({agg['tag_unmapped']}) means the model emitted a tag too rare to "
        "decode (or hallucinated).", "",
    ]
    (BENCH / "baseline_report.md").write_text("\n".join(md), encoding="utf-8")
    print(f"scored {n} items → baseline_report.md; "
          f"features-full {pct(agg['features_full_ok'], n)}, "
          f"claim {pct(agg['claim_ok'], n)}")


def main():
    tagmap = learn_tagmap()
    score(tagmap)
    return 0


if __name__ == "__main__":
    sys.exit(main())
