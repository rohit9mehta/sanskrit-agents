"""Mine lemma mismatches between ByT5's SLM output and the reasoner's chosen
lemma, across every translated unit (Phase 3 prep → lemma normalization).

For each apparatus word: find the ByT5 token with the same surface in the
unit's SLM output; if ByT5's lemma ≠ the chosen lemma, record the pair and a
mechanical pattern label. The pattern table is what the normalization layer
(src/shastrartha/lemma.py) is built from; rerunning this after wiring it in
measures the residual.

Outputs (agent/data/training/):
  lemma_mismatches.jsonl   {unit, surface, byt5, chosen, pos, pattern, note}
  lemma_patterns.md        counts per pattern + examples
"""

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AGENT / "src"))
from shastrartha.analyze import local_analyze_cached, parse_slm  # noqa: E402
from shastrartha.normalize import fold  # noqa: E402
from shastrartha.lemma import canonicalize  # noqa: E402
from shastrartha.verify import normalize_nasals, to_slp1  # noqa: E402

OUT = AGENT / "output"
TRAIN = AGENT / "data" / "training"


def units():
    mula = json.loads((AGENT / "data" / "mula" / "trimsika.json").read_text())
    by_v = {str(v["verse"]): v["bhasya_text"] for v in mula["verses"]}
    for p in sorted(OUT.glob("v[0-9][0-9]/apparatus.json")):
        d = json.loads(p.read_text())
        yield f"trimsika {d['verse']}", by_v.get(str(d["verse"]), ""), d
    for p in sorted(OUT.glob("*/*/apparatus.json")):
        d = json.loads(p.read_text())
        yield f"{p.parent.parent.name} {d.get('unit')}", d.get("mula", ""), d


def nfc(s):
    return unicodedata.normalize("NFC", s or "")


def pattern(byt5: str, chosen: str, pos: str) -> str:
    b, c = nfc(byt5), nfc(chosen)
    if b == c:
        return "identical"
    if fold(b) == fold(c):
        # same skeleton: diacritic/nasal/avagraha/hyphen-level difference
        if re.sub(r"[ṃṁ]", "N", b).replace("ṅ", "N").replace("ñ", "N").replace("ṇ", "N").replace("n", "N").replace("m", "N") == \
           re.sub(r"[ṃṁ]", "N", c).replace("ṅ", "N").replace("ñ", "N").replace("ṇ", "N").replace("n", "N").replace("m", "N"):
            return "nasal-orthography"
        if "-" in c or "-" in b:
            return "hyphenation"
        return "diacritic/other-orthography"
    if "-" in c and c.replace("-", "") == b:
        return "compound-hyphenated-by-reasoner"
    if c.replace("-", "").startswith(b) or b.startswith(c.replace("-", "")):
        return "prefix/affix-boundary"
    if b.endswith("ay") and (c.endswith("ita") or c.endswith("aya") or c.endswith("ana") or c.endswith("ayitṛ")):
        return "causative-root→derived-stem"
    if pos == "tinanta" and (c.endswith(b) or b.endswith(c)):
        return "verb-prefix-citation"
    if b.endswith(("at", "ant")) and c.endswith(("at", "ant", "an")):
        return "participle-stem-citation"
    if b.endswith("in") and c.endswith("in") or b.endswith("vat") and c.endswith(("vat", "vant")) or b.endswith("mat") and c.endswith(("mat", "mant")):
        return "in/vat/mat-stem-citation"
    if (b.endswith("a") and c.endswith("ā")) or (b.endswith("ā") and c.endswith("a")):
        return "gender-stem-a/ā"
    if b in ("mad", "asmad", "tvad", "yuṣmad", "idam", "etad", "tad", "enad", "adas", "kim", "yad") or c in ("mad", "asmad", "tvad", "yuṣmad", "enad"):
        return "pronoun-stem-citation"
    return "other"


def same(a, b):
    return normalize_nasals(to_slp1(nfc(a))) == normalize_nasals(to_slp1(nfc(b)))


def main():
    canon = '--canonical' in sys.argv
    items = list(units())
    texts = [t for _, t, _ in items if t]
    slm = local_analyze_cached(texts, task="SLM")
    mism, total, aligned = [], 0, 0
    for uid, text, d in items:
        parsed = parse_slm(slm.get(text, "")) if text else []
        for w in d.get("analysis", []):
            total += 1
            want = fold(w["surface"])
            tok = next((t for t in parsed if "surface" in t and fold(t["surface"]) == want), None)
            if tok is None:
                continue
            aligned += 1
            lem = tok["lemma"]
            if canon:
                c = canonicalize(tok["surface"], tok["lemma"], tok["tag"])
                lem = c.lemma
                # verbs: chosen lemma may cite root or prefix-root; accept either
                chosen_ok = same(lem, w["lemma"]) or (
                    c.root and same(c.root, w["lemma"])) or (
                    c.prefixes and same("".join(to_slp1(x) for x in c.prefixes) + to_slp1(c.root or ""), w["lemma"]))
            else:
                chosen_ok = same(lem, w["lemma"])
            if not chosen_ok:
                pos = (w.get("morph") or {}).get("pos")
                mism.append({"unit": uid, "surface": w["surface"], "byt5": tok["lemma"],
                             "canonical": lem if canon else None,
                             "byt5_tag": tok["tag"], "chosen": w["lemma"], "pos": pos,
                             "pattern": pattern(lem, w["lemma"], pos),
                             "note": (w.get("note") or "")[:160]})
    TRAIN.mkdir(parents=True, exist_ok=True)
    with (TRAIN / ("lemma_residual.jsonl" if canon else "lemma_mismatches.jsonl")).open("w", encoding="utf-8") as f:
        for m in mism:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    pc = Counter(m["pattern"] for m in mism)
    ex = defaultdict(list)
    for m in mism:
        if len(ex[m["pattern"]]) < 4:
            ex[m["pattern"]].append(f"{m.get('canonical') or m['byt5']} → {m['chosen']} ({m['surface']}, {m['unit']})")
    md = [("# Canonical (normalized) vs chosen lemma: RESIDUAL" if canon else "# ByT5 vs chosen lemma: mismatch patterns"), "",
          f"{total} apparatus words; {aligned} aligned to a ByT5 token; "
          f"**{len(mism)} lemma mismatches** ({100*len(mism)/max(1,aligned):.1f}% of aligned).", "",
          "| pattern | n | examples |", "|---|---|---|",
          *[f"| {k} | {n} | {'; '.join(ex[k])} |" for k, n in pc.most_common()], ""]
    (TRAIN / ("lemma_residual.md" if canon else "lemma_patterns.md")).write_text("\n".join(md), encoding="utf-8")
    print(f"{total} words, {aligned} aligned, {len(mism)} mismatches → lemma_patterns.md")
    for k, n in pc.most_common():
        print(f"  {n:4d} {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
