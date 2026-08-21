"""Arbitrate DCS claims with vidyut (Phase 3 prep, stage 2).

Runs every schema-mapped DCS record (data/training/dcs_pool.jsonl) through
the same verifiers the pipeline uses:

  * subanta claims  → verify_subanta_claim (stem+features ⊢ surface?)
  * tinanta claims  → verify_tinanta_claim over the lakāra candidates the
    coarse DCS tags allow (Past → Luṅ/Liṭ/Laṅ; Fut → Lṛṭ/Luṭ), crossed with
    prayoga ∈ {Kartari, Karmani}; whichever derivations actually generate
    the attested surface win

Products (agent/data/training/):
  dcs_verified.jsonl    — records vidyut confirmed, with resolved features
  dcs_ambiguous.jsonl   — >1 (prayoga, lakāra) derives the same surface
  dcs_unverified.jsonl  — nothing derived the surface (DCS/mapping/vidyut gap)
  dcs_arbitration.md    — counts + resolved lakāra distribution

Verification records go to logs/dcs_arbitration.jsonl (NOT the pipeline log —
that file is pipeline provenance).

Dedupes on (surface, claim) first: narrative texts repeat forms heavily.
"""

import json
import sys
from collections import Counter
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AGENT / "src"))

from shastrartha import verify  # noqa: E402

verify.LOG_PATH = AGENT / "logs" / "dcs_arbitration.jsonl"

TRAIN = AGENT / "data" / "training"
RUN_ID = "dcs-arb-01"


def main():
    subanta, tinanta = {}, {}
    occ = Counter()
    for line in (TRAIN / "dcs_pool.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        c = r.get("claim")
        if not c:
            continue
        if r["kind"] == "subanta":
            if not (c["linga"] and c["vibhakti"] and c["vacana"]):
                continue
            key = (r["surface"], c["stem"], c["linga"], c["vibhakti"], c["vacana"])
            occ[("s",) + key] += 1
            subanta.setdefault(key, r)
        elif r["kind"] == "tinanta":
            if not (c["purusha"] and c["vacana"]):
                continue
            key = (r["surface"], c["root"], c["purusha"], c["vacana"],
                   tuple(c["lakara_candidates"]))
            occ[("t",) + key] += 1
            tinanta.setdefault(key, r)

    print(f"deduped: {len(subanta)} subanta, {len(tinanta)} tinanta claims")
    verified, ambiguous, unverified = [], [], []
    n = 0

    for key, r in subanta.items():
        surface, stem, linga, vibhakti, vacana = key
        rec = verify.verify_subanta_claim(
            surface, stem, linga, vibhakti, vacana,
            run_id=RUN_ID, source="dcs",
            context={"text": r["text"], "stage": "dcs-arb",
                     "unit": r["sent_id"], "line": None},
        )
        out = {**r, "occurrences": occ[("s",) + key],
               "vidyut": {"result": rec["result"], "method": rec["method"]}}
        (verified if rec["result"] == "pass" else unverified).append(out)
        n += 1
        if n % 2000 == 0:
            print(f"  ...{n}")

    for key, r in tinanta.items():
        surface, root, purusha, vacana, cands = key
        passes = []
        for prayoga in ("Kartari", "Karmani"):
            for lakara in cands:
                rec = verify.verify_tinanta_claim(
                    surface, root, [], prayoga, lakara, purusha, vacana,
                    run_id=RUN_ID, source="dcs",
                    context={"text": r["text"], "stage": "dcs-arb",
                             "unit": r["sent_id"], "line": None},
                )
                if rec["result"] == "pass":
                    passes.append({"prayoga": prayoga, "lakara": lakara,
                                   "method": rec["method"]})
            if passes:
                break  # Kartari suffices; don't shop for a Karmani reading too
        out = {**r, "occurrences": occ[("t",) + key]}
        if len(passes) == 1:
            out["claim"] = {**r["claim"], "prayoga": passes[0]["prayoga"],
                            "lakara": passes[0]["lakara"]}
            out["claim"].pop("lakara_candidates", None)
            out["vidyut"] = {"result": "pass", "method": passes[0]["method"]}
            verified.append(out)
        elif passes:
            out["vidyut"] = {"result": "ambiguous", "options": passes}
            ambiguous.append(out)
        else:
            out["vidyut"] = {"result": "fail"}
            unverified.append(out)
        n += 1
        if n % 2000 == 0:
            print(f"  ...{n}")

    for name, rows in [("dcs_verified.jsonl", verified),
                       ("dcs_ambiguous.jsonl", ambiguous),
                       ("dcs_unverified.jsonl", unverified)]:
        with (TRAIN / name).open("w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")

    res_lak = Counter(r["claim"]["lakara"] for r in verified
                      if r["kind"] == "tinanta")
    kinds = Counter(r["kind"] for r in verified)
    md = [
        "# DCS arbitration report", "",
        f"Deduped claims checked: {len(subanta)} subanta + {len(tinanta)} tinanta.",
        "",
        f"* verified: **{len(verified)}** ({dict(kinds)})",
        f"* ambiguous (≥2 derivations fit): **{len(ambiguous)}**",
        f"* unverified: **{len(unverified)}**", "",
        "## Resolved lakāra distribution (verified tinantas)", "",
        "| lakāra | n |", "|---|---|",
        "\n".join(f"| {k} | {v} |" for k, v in res_lak.most_common()), "",
        "Unverified ≠ wrong: DCS reads Vedic/epic irregulars and vidyut's "
        "dhātupāṭha differs on some citation forms. Unverified records are "
        "excluded from gold sets; that is the point of arbitration.", "",
    ]
    (TRAIN / "dcs_arbitration.md").write_text("\n".join(md), encoding="utf-8")
    print(f"verified {len(verified)}, ambiguous {len(ambiguous)}, "
          f"unverified {len(unverified)} → {TRAIN}/dcs_*.jsonl, dcs_arbitration.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
