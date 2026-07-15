"""Vidyut sanity check (Phase 0, CLAUDE.md item 1).

Positives : derive vipākaḥ (subanta) and pravartate (tiṅanta with upasarga);
kosha     : known-form + claim-consistency lookups;
negative  : a DESIGNED failure (viṣayasya claimed as dative) must log `fail`;
unsupported: a samāsa-relation claim must log `unsupported`.

Every check writes one record to agent/logs/vidyut_verifications.jsonl.
Exit 0 only if all expectations hold and ≥6 schema-valid records were written.
"""

import json
import sys

from shastrartha import verify

RUN_ID = "sanity-vidyut-01"
SCHEMA_KEYS = {
    "ts", "run_id", "context", "surface_iast", "surface_slp1",
    "claim", "method", "result", "expected_forms", "prakriya_rules", "notes",
}


def ctx(line: int, verse: str) -> dict:
    return {"text": "trbh", "line": line, "verse": verse, "stage": "sanity"}


def main() -> int:
    checks: list[tuple[str, dict, str]] = []  # (label, record, expected_result)

    # 1. Positive subanta: vipākaḥ = vipāka, masc. nom. sg. (trbh 167, v.2a)
    r = verify.verify_subanta_claim(
        "vipākaḥ", "vipāka", "Pum", "Prathama", "Eka",
        run_id=RUN_ID, context=ctx(167, "2a"), source="sanity",
    )
    checks.append(("subanta vipākaḥ nom.sg.", r, "pass"))
    print("vipākaḥ prakriyā trace:")
    for step in r["prakriya_rules"]:
        print("   ", step)

    # 2. Positive tiṅanta: pravartate = pra+√vṛt, laṭ 3sg. (trbh 24, v.1ab)
    r = verify.verify_tinanta_claim(
        "pravartate", "vṛt", ["pra"], "Kartari", "Lat", "Prathama", "Eka",
        run_id=RUN_ID, context=ctx(24, "1ab"), source="sanity",
    )
    checks.append(("tiṅanta pravartate laṭ 3sg.", r, "pass"))

    # 3. Kosha known-form checks
    for form, line, verse in [("vipākaḥ", 167, "2a"), ("vijñaptiḥ", 167, "2b")]:
        r = verify.kosha_check(form, run_id=RUN_ID, context=ctx(line, verse), source="sanity")
        checks.append((f"kosha known-form {form}", r, "pass"))

    # 4. Kosha claim-consistency: viṣayasya rightly genitive
    r = verify.kosha_check(
        "viṣayasya",
        claim={"source": "sanity", "lemma": "viṣaya",
               "analysis": {"pos": "subanta", "stem": "viṣaya",
                            "linga": "Pum", "vibhakti": "Sasthi", "vacana": "Eka"}},
        run_id=RUN_ID, context=ctx(167, "2b"),
    )
    checks.append(("kosha viṣayasya gen.sg. consistent", r, "pass"))

    # 5. DESIGNED NEGATIVE: viṣayasya claimed as dative — must FAIL
    r = verify.verify_subanta_claim(
        "viṣayasya", "viṣaya", "Pum", "Caturthi", "Eka",
        run_id=RUN_ID, context=ctx(167, "2b"), source="sanity",
        notes="designed negative: dative claim for a genitive form",
    )
    checks.append(("DESIGNED NEGATIVE viṣayasya dat.", r, "fail"))
    print(f"\ndesigned negative derived: {r['expected_forms']} (surface viṣayasya) -> {r['result']}")

    # 6. Unsupported: samāsa relation (bahuvrīhi) — not expressible in vidyut
    r = verify.mark_unsupported(
        "sarvabījakam",
        "samāsa relation claim (bahuvrīhi 'having all seeds') not expressible in "
        "vidyut-prakriya; members sarva/bīja(ka) verified separately",
        run_id=RUN_ID, context=ctx(177, "2d"), source="sanity",
    )
    checks.append(("unsupported samāsa relation", r, "unsupported"))

    # ------------------------------------------------------------- verdict
    print("\n== results ==")
    all_ok = True
    for label, rec, want in checks:
        got = rec["result"]
        mark = "OK " if got == want else "BAD"
        if got != want:
            all_ok = False
        print(f"[{mark}] {label}: {got} (want {want})")

    with verify.LOG_PATH.open(encoding="utf-8") as f:
        records = [json.loads(ln) for ln in f if ln.strip()]
    mine = [x for x in records if x["run_id"] == RUN_ID]
    schema_ok = all(SCHEMA_KEYS <= set(x) for x in mine)
    print(f"\nlog: {len(mine)} records for {RUN_ID} in {verify.LOG_PATH.name}; "
          f"schema {'OK' if schema_ok else 'BAD'}")
    all_ok &= len(mine) >= 6 and schema_ok

    print("VIDYUT SANITY", "PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
