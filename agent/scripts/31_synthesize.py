"""Synthetic gold generator (Phase 3 prep): run vidyut FORWARD.

The verifier doubles as a generator: give it (dhātu, prayoga, lakāra,
puruṣa, vacana) or (stem, liṅga, vibhakti, vacana) and it derives the
correct surface form by actually applying Pāṇini's rules. Each derivation
is a perfectly-labeled training pair — surface → analysis — including
categories no corpus attests in quantity (Lṛṅ conditional, Luṭ periphrastic
future, Bhāve prayoga, duals, rare vibhaktis).

Root inventory: every root attested in our verified data (pipeline + DCS),
plus a deterministic sample of the wider dhātupāṭha. Stem inventory:
(stem, liṅga) pairs attested in verified data — liṅga is known-good there.

Budgets are per-cell so the OUTPUT distribution is flat where the corpus
is skewed. Benchmark keys (split_v1.json) are excluded.

Outputs (agent/data/training/):
  synthetic_pool.jsonl    {surface, claim, source:"synthetic", derived_by}
  synthetic_summary.md
"""

import json
import random
import sys
from collections import Counter
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AGENT / "src"))

from shastrartha import verify  # noqa: E402
from shastrartha.verify import (  # noqa: E402
    derive_subanta, derive_tinanta, dhatu_entries, to_iast, to_slp1,
)
from vidyut import prakriya as pk  # noqa: E402

verify.LOG_PATH = AGENT / "logs" / "synthetic_generation.jsonl"

TRAIN = AGENT / "data" / "training"
SEED = 20260821

LAKARAS = ["Lat", "Lit", "Lut", "Lrt", "Lot", "Lan",
           "VidhiLin", "AshirLin", "Lun", "Lrn"]
PRAYOGAS = ["Kartari", "Karmani", "Bhave"]
PURUSHAS = ["Prathama", "Madhyama", "Uttama"]
VACANAS = ["Eka", "Dvi", "Bahu"]
VIBHAKTIS = ["Prathama", "Dvitiya", "Trtiya", "Caturthi",
             "Panchami", "Sasthi", "Saptami", "Sambodhana"]

TIN_PER_CELL = 600        # per (lakāra, prayoga) cell
SUB_PER_CELL = 700        # per (vibhakti, vacana) cell
MAX_EXTRA_DHATUS = 400    # dhātupāṭha sample beyond attested roots


def attested_roots() -> set[str]:
    roots = set()
    for name in ("pool.jsonl", "dcs_verified.jsonl"):
        p = TRAIN / name
        if not p.exists():
            continue
        for line in p.open(encoding="utf-8"):
            r = json.loads(line)
            c = r.get("claim") or {}
            ana = c.get("analysis") if "analysis" in c else c
            if (ana or {}).get("pos") == "tinanta" and ana.get("root"):
                roots.add(to_slp1(ana["root"]))
    return roots


def attested_stems() -> list[tuple[str, str]]:
    pairs = set()
    for name in ("pool.jsonl", "dcs_verified.jsonl"):
        p = TRAIN / name
        if not p.exists():
            continue
        for line in p.open(encoding="utf-8"):
            r = json.loads(line)
            c = r.get("claim") or {}
            ana = c.get("analysis") if "analysis" in c else c
            if (ana or {}).get("pos") == "subanta" and ana.get("stem") and ana.get("linga"):
                if r.get("result", r.get("vidyut", {}).get("result")) == "pass":
                    pairs.add((to_slp1(ana["stem"]), ana["linga"]))
    return sorted(pairs)


def pick_dhatus(rng: random.Random):
    roots = attested_roots()
    entries = dhatu_entries()
    attested, extra = [], []
    for e in entries:
        bare = verify._clean_aupadeshika(e.dhatu.aupadeshika)
        (attested if bare in roots else extra).append(e)
    rng.shuffle(extra)
    chosen = attested + extra[:MAX_EXTRA_DHATUS]
    rng.shuffle(chosen)
    print(f"dhātus: {len(attested)} attested + {min(len(extra), MAX_EXTRA_DHATUS)} sampled")
    return chosen


def main():
    rng = random.Random(SEED)
    excluded = set(json.loads((TRAIN / "split_v1.json")
                              .read_text(encoding="utf-8"))["excluded_keys"])

    def key(surface, norm):
        return surface + "‖" + json.dumps(norm, sort_keys=True, ensure_ascii=False)

    out, seen = [], set()
    cell_counts = Counter()

    # ---------------- tinanta ----------------
    dhatus = pick_dhatus(rng)
    for lakara in LAKARAS:
        for prayoga in PRAYOGAS:
            cell = f"tin:{lakara}:{prayoga}"
            combos = [(p, v) for p in PURUSHAS for v in VACANAS]
            di = 0
            while cell_counts[cell] < TIN_PER_CELL and di < len(dhatus) * 2:
                e = dhatus[di % len(dhatus)]
                di += 1
                purusha, vacana = combos[di % len(combos)]
                if prayoga == "Bhave":
                    purusha, vacana = "Prathama", "Eka"   # bhāve is impersonal
                d = pk.Dhatu.mula(e.dhatu.aupadeshika, e.dhatu.gana)
                try:
                    prakriyas = derive_tinanta(d, prayoga, lakara, purusha, vacana)
                except Exception:
                    continue
                if not prakriyas:
                    continue
                surface = to_iast(prakriyas[0].text)
                bare = verify._clean_aupadeshika(e.dhatu.aupadeshika)
                norm = {"pos": "tinanta", "root": to_iast(bare),
                        "prayoga": prayoga, "lakara": lakara,
                        "purusha": purusha, "vacana": vacana}
                k = key(surface, norm)
                if k in seen or k in excluded:
                    continue
                seen.add(k)
                cell_counts[cell] += 1
                out.append({"source": "synthetic", "kind": "tinanta",
                            "surface": surface, "claim": norm,
                            "derived_by": {"aupadeshika": e.dhatu.aupadeshika,
                                           "gana": str(e.dhatu.gana)}})
        print(f"  {lakara}: " + ", ".join(
            f"{p}={cell_counts[f'tin:{lakara}:{p}']}" for p in PRAYOGAS))

    # ---------------- subanta ----------------
    stems = attested_stems()
    print(f"stems: {len(stems)} attested (stem, liṅga) pairs")
    for vibhakti in VIBHAKTIS:
        for vacana in VACANAS:
            cell = f"sub:{vibhakti}:{vacana}"
            si = 0
            order = list(range(len(stems)))
            rng.shuffle(order)
            while cell_counts[cell] < SUB_PER_CELL and si < len(order):
                stem_slp1, linga = stems[order[si]]
                si += 1
                try:
                    prakriyas = derive_subanta(stem_slp1, linga, vibhakti, vacana)
                except Exception:
                    continue
                if not prakriyas:
                    continue
                surface = to_iast(prakriyas[0].text)
                norm = {"pos": "subanta", "stem": to_iast(stem_slp1),
                        "linga": linga, "vibhakti": vibhakti, "vacana": vacana}
                k = key(surface, norm)
                if k in seen or k in excluded:
                    continue
                seen.add(k)
                cell_counts[cell] += 1
                out.append({"source": "synthetic", "kind": "subanta",
                            "surface": surface, "claim": norm})
        print(f"  {vibhakti}: " + ", ".join(
            f"{v}={cell_counts[f'sub:{vibhakti}:{v}']}" for v in VACANAS))

    with (TRAIN / "synthetic_pool.jsonl").open("w", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    tin_n = sum(v for c, v in cell_counts.items() if c.startswith("tin:"))
    sub_n = sum(v for c, v in cell_counts.items() if c.startswith("sub:"))
    md = [
        "# Synthetic pool summary", "",
        f"{len(out)} derivation-gold pairs (tinanta {tin_n}, subanta {sub_n}); "
        f"seed {SEED}; benchmark keys excluded.", "",
        "Every pair is generated BY the Pāṇinian engine, so the label is "
        "correct by construction. Cells the corpus starves (Lṛṅ, Luṭ, "
        "AshirLin, Bhāve, duals, Caturthi) are filled to the same budget "
        "as common cells.", "",
        "| cell | n |", "|---|---|",
        "\n".join(f"| {c} | {n} |" for c, n in sorted(cell_counts.items())),
        "",
    ]
    (TRAIN / "synthetic_summary.md").write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {len(out)} pairs → synthetic_pool.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
