"""Phase 2, item 3a: blinded human-eval packets.

Per verse: the Sanskrit (bhāṣya reading), the published human translation as
reference, and the three systems (agent translation stripped of apparatus,
raw-LLM, MITRA) under labels A/B/C randomized per verse with a fixed seed.

Outputs:
  data/eval/packets/eval_packet.md          — give this to graders
  data/eval/packets/response_TEMPLATE.csv   — graders fill one per person
  data/eval/answer_key.json                 — label→system map; DO NOT SHARE
"""

import csv
import json
import random
import sys

from shastrartha.texts import AGENT_DIR, DATA_DIR

EVAL = DATA_DIR / "eval"
PACKETS = EVAL / "packets"
OUTPUT = AGENT_DIR / "output"
SEED = 20260716
HARD_SUBSET_N = 10

INSTRUCTIONS = """# Triṃśikā translation evaluation

Thank you! You are comparing three anonymous machine translation systems
(A/B/C — the assignment changes every verse) on the 30 verses of
Vasubandhu's Triṃśikā. A published human translation is shown as reference;
you may also rely on your own reading of the Sanskrit. The reference
translates the vulgate text, which occasionally differs from the bhāṣya
reading shown (e.g. v.13 uddhataḥ vs uddhavaḥ).

For each verse, answer three questions (write A, B, C, or `tie`; add `-` if
none is acceptable):

1. **term_fidelity** — Which system best renders the technical terms as the
   Yogācāra tradition understands them (e.g. vipāka, vijñapti, ālaya,
   upādi, parāvṛtti)? Generic dictionary glosses that miss the technical
   sense count against a system.
2. **compound_resolution** — Which system best resolves the compounds
   (correct member division, correct relation — e.g. bahuvrīhi vs
   tatpuruṣa — and correct construal in context)?
3. **overall** — Which translation is the most faithful rendering of the
   verse overall (accuracy first, fluency second)?

Fill the CSV template (one row per verse) and add free comments wherever a
system does something notably right or wrong. Expected effort: 3–6 hours.
"""


def main() -> int:
    mula = json.loads((DATA_DIR / "mula" / "trimsika.json").read_text())
    human = json.loads((EVAL / "human_baseline.json").read_text())
    raw = json.loads((EVAL / "raw_llm.json").read_text())
    mitra = json.loads((EVAL / "mitra.json").read_text())

    rng = random.Random(SEED)
    key, hard_scores = {}, {}
    lines = [INSTRUCTIONS, "\n---\n"]
    for v in mula["verses"]:
        n = v["verse"]
        app = json.loads((OUTPUT / f"v{n:02d}" / "apparatus.json").read_text())
        systems = [("agent", app["translation"]),
                   ("raw_llm", raw["verses"][str(n)]),
                   ("mitra", mitra["verses"][str(n)])]
        rng.shuffle(systems)
        key[str(n)] = {label: name for label, (name, _) in zip("ABC", systems)}
        hard_scores[n] = sum(1 for j in app["justifications"] if j["depends_on_commentary"])

        lines += [f"## Verse {n}", "",
                  f"**Sanskrit (bhāṣya reading):** {v['bhasya_text']}", "",
                  f"**Reference (human):** {human['verses'][str(n)]}", ""]
        for label, (_, text) in zip("ABC", systems):
            lines += [f"**{label}.** {text}", ""]
        lines.append("---\n")

    hard = [n for n, _ in sorted(hard_scores.items(), key=lambda x: -x[1])[:HARD_SUBSET_N]]

    PACKETS.mkdir(parents=True, exist_ok=True)
    (PACKETS / "eval_packet.md").write_text("\n".join(lines), encoding="utf-8")
    (EVAL / "answer_key.json").write_text(json.dumps(
        {"seed": SEED, "labels": key, "hard_subset": sorted(hard),
         "hard_subset_rule": f"top {HARD_SUBSET_N} verses by commentary-dependent justifications"},
        indent=1), encoding="utf-8")
    with (PACKETS / "response_TEMPLATE.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["verse", "term_fidelity", "compound_resolution", "overall", "comments"])
        for n in range(1, 31):
            w.writerow([n, "", "", "", ""])

    print(f"wrote {PACKETS/'eval_packet.md'}, response_TEMPLATE.csv, answer_key.json")
    print(f"hard subset (by commentary-dependent Js): {sorted(hard)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
