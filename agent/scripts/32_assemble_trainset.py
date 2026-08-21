"""Assemble the analyzer training set from all curated pools (Phase 3 prep).

Sources (agent/data/training/):
  pool.jsonl          pipeline verified passes (+ fails as negatives)
  contrastive.jsonl   rejected→accepted pairs (hard negatives)
  dcs_verified.jsonl  vidyut-confirmed DCS claims (with sentence context)
  synthetic_pool.jsonl vidyut forward derivations (no context)

Rules:
  * every record whose (surface, claim) key is in split_v1.json is DROPPED —
    the benchmark is frozen and nothing in it may be trained on
  * one unified record shape so the trainer is source-agnostic:
      {id, source, surface, sentence|null, claim, negatives:[claim...],
       weight}
  * weights: pipeline-hard 3.0 (rare, in-domain, hardest), dcs 1.0,
    synthetic 0.5 (unlimited supply; don't let it swamp real text)

Outputs: trainset_v1.jsonl, trainset_summary.md
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
TRAIN = AGENT / "data" / "training"
RAW = AGENT / "data" / "dcs" / "raw"

KEEP = ("pos", "stem", "linga", "vibhakti", "vacana",
        "root", "prefixes", "prayoga", "lakara", "purusha", "lemma")


def norm(claim):
    ana = claim.get("analysis") if "analysis" in claim else claim
    if not ana:
        return None
    return {k: ana[k] for k in KEEP if ana.get(k) is not None}


def key(surface, c):
    return surface + "‖" + json.dumps(c, sort_keys=True, ensure_ascii=False)


def dcs_sentences():
    sents = {}
    for path in RAW.glob("*/*.conllu"):
        text = sid = None
        for line in path.open(encoding="utf-8"):
            if line.startswith("# text = "):
                text = line[9:].strip()
            elif line.startswith("# sent_id"):
                sid = line.split("=", 1)[1].strip()
            elif not line.strip() and sid and text:
                sents[sid] = text
                text = sid = None
    return sents


def main():
    excluded = set(json.loads((TRAIN / "split_v1.json").read_text())["excluded_keys"])
    recs, dropped = {}, Counter()

    def add(source, surface, c, sentence=None, weight=1.0, negative=None):
        if c is None or not c.get("pos"):
            return
        k = key(surface, c)
        if k in excluded:
            dropped[source] += 1
            return
        r = recs.get(k)
        if r is None:
            r = recs[k] = {"source": source, "surface": surface,
                           "sentence": sentence, "claim": c,
                           "negatives": [], "weight": weight}
        elif sentence and not r["sentence"]:
            r["sentence"] = sentence
        if negative and negative not in r["negatives"]:
            r["negatives"].append(negative)
        r["weight"] = max(r["weight"], weight)

    # pipeline passes; fails become negatives attached to the same surface
    fails = defaultdict(list)
    for line in (TRAIN / "pool.jsonl").open(encoding="utf-8"):
        p = json.loads(line)
        c = norm(p["claim"])
        if p["result"] == "pass" and c:
            add("pipeline", p["surface_iast"], c, weight=1.5)
        elif p["result"] == "fail" and c:
            fails[p["surface_iast"]].append(c)
    for line in (TRAIN / "contrastive.jsonl").open(encoding="utf-8"):
        p = json.loads(line)
        add("pipeline-hard", p["surface_iast"], norm(p["accepted"]["claim"]),
            weight=3.0, negative=norm(p["rejected"]["claim"]))
    for surface, negs in fails.items():
        for k, r in recs.items():
            if r["surface"] == surface and r["source"].startswith("pipeline"):
                for n in negs:
                    if n != r["claim"] and n not in r["negatives"]:
                        r["negatives"].append(n)

    sents = dcs_sentences()
    for line in (TRAIN / "dcs_verified.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        add("dcs", d["surface"], norm(d["claim"]), sentence=sents.get(d["sent_id"]))

    for line in (TRAIN / "synthetic_pool.jsonl").open(encoding="utf-8"):
        s = json.loads(line)
        add("synthetic", s["surface"], norm(s["claim"]), weight=0.5)

    out = []
    for i, (k, r) in enumerate(sorted(recs.items(), key=lambda kv: kv[0]), 1):
        r["id"] = f"tr-{i:06d}"
        out.append(r)
    with (TRAIN / "trainset_v1.jsonl").open("w", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    by_src = Counter(r["source"] for r in out)
    with_ctx = sum(1 for r in out if r["sentence"])
    with_neg = sum(1 for r in out if r["negatives"])
    lak = Counter(r["claim"].get("lakara") for r in out if r["claim"]["pos"] == "tinanta")
    md = ["# Training set v1", "",
          f"{len(out)} records (benchmark-excluded: {dict(dropped)}).", "",
          "| source | n |", "|---|---|",
          *[f"| {s} | {n} |" for s, n in by_src.most_common()], "",
          f"* with sentence context: {with_ctx}",
          f"* with hard negatives: {with_neg}", "",
          "## Tinanta lakāra (all sources)", "", "| lakāra | n |", "|---|---|",
          *[f"| {k} | {n} |" for k, n in lak.most_common()], ""]
    (TRAIN / "trainset_summary.md").write_text("\n".join(md), encoding="utf-8")
    print(f"trainset_v1: {len(out)} records {dict(by_src)}; dropped {dict(dropped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
