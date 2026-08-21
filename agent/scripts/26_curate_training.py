"""Curate the vidyut verification log into a training-data pool (Phase 3 prep).

Reads logs/vidyut_verifications.jsonl and writes agent/data/training/:

  pool.jsonl        — deduped (surface, claim, result) records with aggregated
                      provenance; the raw material for analyzer training
  contrastive.jsonl — (rejected claim, accepted claim) pairs for the same
                      surface in the same unit, from the verify-feedback retry
                      (run_id ...-a1 fail → ...-a2 pass): hard negatives no
                      corpus provides
  coverage.json     — machine-readable phenomenon distribution
  coverage.md       — human-readable coverage report incl. gaps (which
                      features the corpus under-represents → targets for
                      synthetic generation / next-text onboarding)

Scope: stage == pipeline or handrun (real verified runs); sanity/test excluded.
tool_error records are excluded from the pool but counted in the report.
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
LOG = AGENT / "logs" / "vidyut_verifications.jsonl"
OUT = AGENT / "data" / "training"

# Feature spaces (mirror schema.py / vidyut enums) — used to report gaps,
# i.e. values with zero or thin coverage among verified passes.
VIBHAKTIS = ["Prathama", "Dvitiya", "Trtiya", "Caturthi",
             "Panchami", "Sasthi", "Saptami", "Sambodhana"]
VACANAS = ["Eka", "Dvi", "Bahu"]
LINGAS = ["Pum", "Stri", "Napumsaka"]
LAKARAS = ["Lat", "Lit", "Lut", "Lrt", "Lot", "Lan",
           "VidhiLin", "AshirLin", "Lun", "Lrn"]
PURUSHAS = ["Prathama", "Madhyama", "Uttama"]
PRAYOGAS = ["Kartari", "Karmani", "Bhave"]
SAMASA_TYPES = ["tatpurusa", "karmadharaya", "bahuvrihi",
                "dvandva", "avyayibhava", "dvigu"]

THIN = 20  # below this many verified examples a feature value counts as a gap

ATTEMPT_RE = re.compile(r"-a(\d)$")


def load_records():
    kept, skipped = [], Counter()
    for line in LOG.open(encoding="utf-8"):
        d = json.loads(line)
        stage = (d.get("context") or {}).get("stage")
        if stage not in ("pipeline", "handrun"):
            skipped[f"stage:{stage}"] += 1
            continue
        if d["result"] == "tool_error":
            skipped["tool_error"] += 1
            continue
        kept.append(d)
    return kept, skipped


def claim_key(claim: dict) -> str:
    return json.dumps(claim, sort_keys=True, ensure_ascii=False)


def build_pool(records):
    """Dedupe on (surface, claim, result); aggregate provenance."""
    pool = {}
    for d in records:
        ctx = d["context"]
        key = (d["surface_slp1"], claim_key(d["claim"]), d["result"])
        e = pool.get(key)
        if e is None:
            e = pool[key] = {
                "surface_iast": d["surface_iast"],
                "surface_slp1": d["surface_slp1"],
                "claim": d["claim"],
                "result": d["result"],
                "method": d["method"],
                "expected_forms": d.get("expected_forms") or [],
                "notes": d.get("notes") or "",
                "count": 0,
                "sources": [],
            }
        e["count"] += 1
        src = f"{ctx.get('text')}:{ctx.get('verse') or ctx.get('unit')}"
        if src not in e["sources"] and len(e["sources"]) < 8:
            e["sources"].append(src)
    return list(pool.values())


def build_contrastive(records):
    """Pair a1-fail with a2-pass for the same (text, unit, surface)."""
    groups = defaultdict(lambda: {"fail": [], "pass": []})
    for d in records:
        m = ATTEMPT_RE.search(d.get("run_id") or "")
        if not m or d["result"] not in ("fail", "pass"):
            continue
        ctx = d["context"]
        gkey = (ctx.get("text"), str(ctx.get("verse") or ctx.get("unit")),
                d["surface_slp1"])
        groups[gkey][d["result"]].append((int(m.group(1)), d))

    pairs, unpaired_fails = [], 0
    for (text, unit, surface), g in groups.items():
        fails = [d for a, d in g["fail"] if a == 1]
        passes = [d for a, d in g["pass"] if a == 2]
        if not fails:
            continue
        if not passes:
            unpaired_fails += len(fails)
            continue
        acc = passes[0]
        seen = set()
        for f in fails:
            ck = claim_key(f["claim"])
            if ck in seen or ck == claim_key(acc["claim"]):
                continue
            seen.add(ck)
            pairs.append({
                "text": text, "unit": unit,
                "surface_iast": f["surface_iast"],
                "surface_slp1": surface,
                "rejected": {"claim": f["claim"],
                             "expected_forms": f.get("expected_forms") or [],
                             "method": f["method"]},
                "accepted": {"claim": acc["claim"], "method": acc["method"]},
            })
    return pairs, unpaired_fails


def coverage(records):
    cov = {
        "per_text": Counter(), "results": Counter(), "pos": Counter(),
        "vibhakti": Counter(), "vacana": Counter(), "linga": Counter(),
        "vibhakti_x_vacana": Counter(), "lakara": Counter(),
        "purusha": Counter(), "prayoga": Counter(), "samasa": Counter(),
        "stems": set(), "roots": set(),
    }
    for d in records:
        cov["per_text"][d["context"].get("text")] += 1
        cov["results"][d["result"]] += 1
        if d["result"] == "unsupported":
            m = re.search(r"samāsa relation \((\w+)", d.get("notes") or "")
            if m:
                cov["samasa"][m.group(1)] += 1
            continue
        if d["result"] != "pass":
            continue
        ana = (d.get("claim") or {}).get("analysis")
        if not ana:
            continue
        pos = ana.get("pos")
        cov["pos"][pos] += 1
        if pos == "subanta":
            cov["vibhakti"][ana.get("vibhakti")] += 1
            cov["vacana"][ana.get("vacana")] += 1
            cov["linga"][ana.get("linga")] += 1
            cov["vibhakti_x_vacana"][f"{ana.get('vibhakti')}/{ana.get('vacana')}"] += 1
            if ana.get("stem"):
                cov["stems"].add(ana["stem"])
        elif pos == "tinanta":
            cov["lakara"][ana.get("lakara")] += 1
            cov["purusha"][ana.get("purusha")] += 1
            cov["prayoga"][ana.get("prayoga")] += 1
            if ana.get("root"):
                cov["roots"].add(ana["root"])
    return cov


def gaps(cov):
    out = []
    for label, space, ctr in [
        ("vibhakti", VIBHAKTIS, cov["vibhakti"]),
        ("vacana", VACANAS, cov["vacana"]),
        ("linga", LINGAS, cov["linga"]),
        ("lakāra", LAKARAS, cov["lakara"]),
        ("puruṣa", PURUSHAS, cov["purusha"]),
        ("prayoga", PRAYOGAS, cov["prayoga"]),
        ("samāsa", SAMASA_TYPES, cov["samasa"]),
    ]:
        for v in space:
            n = ctr.get(v, 0)
            if n < THIN:
                out.append((label, v, n))
    return out


def fmt_counter(ctr, space=None):
    items = ([(v, ctr.get(v, 0)) for v in space] if space
             else sorted(ctr.items(), key=lambda x: -x[1]))
    return "\n".join(f"| {k} | {n} |" for k, n in items)


def main():
    records, skipped = load_records()
    pool = build_pool(records)
    pairs, unpaired = build_contrastive(records)
    cov = coverage(records)
    gap_list = gaps(cov)

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "pool.jsonl").open("w", encoding="utf-8") as f:
        for e in sorted(pool, key=lambda e: (-e["count"], e["surface_slp1"])):
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    with (OUT / "contrastive.jsonl").open("w", encoding="utf-8") as f:
        for p in pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    cov_json = {k: (sorted(v) if isinstance(v, set) else dict(v))
                for k, v in cov.items()}
    cov_json["gaps"] = [{"feature": a, "value": b, "count": c}
                        for a, b, c in gap_list]
    cov_json["pool_size"] = len(pool)
    cov_json["contrastive_pairs"] = len(pairs)
    cov_json["unpaired_fails"] = unpaired
    cov_json["skipped"] = dict(skipped)
    (OUT / "coverage.json").write_text(
        json.dumps(cov_json, ensure_ascii=False, indent=1), encoding="utf-8")

    md = [
        "# Training-data coverage report",
        "",
        f"Source: `agent/logs/vidyut_verifications.jsonl` — {len(records)} "
        f"pipeline/handrun records kept (skipped: {dict(skipped)}).",
        "",
        f"* Pool: **{len(pool)}** deduped (surface, claim, result) entries → `pool.jsonl`",
        f"* Contrastive pairs (a1-fail → a2-pass): **{len(pairs)}** → "
        f"`contrastive.jsonl` ({unpaired} fails had no paired pass — "
        "surface was re-segmented on retry)",
        f"* Distinct nominal stems: **{len(cov['stems'])}**; "
        f"distinct verbal roots: **{len(cov['roots'])}**",
        "",
        "## Verified passes by part of speech",
        "", "| pos | n |", "|---|---|", fmt_counter(cov["pos"]),
        "", "## Subanta features", "",
        "| vibhakti | n |", "|---|---|", fmt_counter(cov["vibhakti"], VIBHAKTIS),
        "", "| vacana | n |", "|---|---|", fmt_counter(cov["vacana"], VACANAS),
        "", "| linga | n |", "|---|---|", fmt_counter(cov["linga"], LINGAS),
        "", "## Tinanta features", "",
        "| lakāra | n |", "|---|---|", fmt_counter(cov["lakara"], LAKARAS),
        "", "| puruṣa | n |", "|---|---|", fmt_counter(cov["purusha"], PURUSHAS),
        "", "| prayoga | n |", "|---|---|", fmt_counter(cov["prayoga"], PRAYOGAS),
        "", "## Samāsa relations (from `unsupported` notes)", "",
        "| type | n |", "|---|---|", fmt_counter(cov["samasa"], SAMASA_TYPES),
        "", "## Per text", "",
        "| text | records |", "|---|---|", fmt_counter(cov["per_text"]),
        "", f"## Gaps (feature values with < {THIN} verified examples)", "",
        "These are the priority targets for the synthetic generator "
        "(vidyut forward derivation) and for choosing the next texts to onboard.",
        "", "| feature | value | n |", "|---|---|---|",
        "\n".join(f"| {a} | {b} | {c} |" for a, b, c in gap_list),
        "",
    ]
    (OUT / "coverage.md").write_text("\n".join(md), encoding="utf-8")

    print(f"kept {len(records)} records; pool {len(pool)}; "
          f"pairs {len(pairs)} (+{unpaired} unpaired fails); "
          f"gaps {len(gap_list)}")
    print(f"wrote {OUT}/pool.jsonl, contrastive.jsonl, coverage.json, coverage.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
