"""VERIFY stage of the v.2 hand-run: every morphological claim from the
REASON stage, run through vidyut and logged with stage="handrun".

Compound policy (vidyut samāsa coverage is partial): the inflected compound
is checked as an opaque stem (does stem+features derive the surface?), the
samāsa RELATION is logged `unsupported`, and members are kosha-checked."""

import sys

from shastrartha import verify

RUN = "handrun-v02-01"


def ctx(line: int, verse: str) -> dict:
    return {"text": "trbh", "line": line, "verse": verse, "stage": "handrun"}


def main() -> int:
    r = []

    # ---- v.2ab = trbh 167: vipāko mananākhyaś ca vijñaptir viṣayasya ca
    r.append(("vipākaḥ nom.sg.m.", "pass", verify.verify_subanta_claim(
        "vipākaḥ", "vipāka", "Pum", "Prathama", "Eka",
        run_id=RUN, context=ctx(167, "2a"), source="claude-reasoner")))
    r.append(("mananākhyaḥ (whole stem) nom.sg.m.", "pass", verify.verify_subanta_claim(
        "mananākhyaḥ", "mananākhya", "Pum", "Prathama", "Eka",
        run_id=RUN, context=ctx(167, "2a"), source="claude-reasoner",
        notes="bahuvrīhi 'whose name is manana' checked as opaque stem")))
    r.append(("mananākhya relation", "unsupported", verify.mark_unsupported(
        "mananākhyaḥ",
        "samāsa relation (bahuvrīhi: manana-ākhyā yasya) not expressible in "
        "vidyut; members manana (kosha), ākhyā (MW s.v.) checked separately",
        run_id=RUN, context=ctx(167, "2a"), source="claude-reasoner")))
    r.append(("manana member known", "pass", verify.kosha_check(
        "manana", run_id=RUN, context=ctx(167, "2a"), source="claude-reasoner")))
    r.append(("ca known", "pass", verify.kosha_check(
        "ca", run_id=RUN, context=ctx(167, "2ab"), source="claude-reasoner")))
    r.append(("vijñaptiḥ nom.sg.f.", "pass", verify.verify_subanta_claim(
        "vijñaptiḥ", "vijñapti", "Stri", "Prathama", "Eka",
        run_id=RUN, context=ctx(167, "2b"), source="claude-reasoner")))
    r.append(("viṣayasya gen.sg.m.", "pass", verify.verify_subanta_claim(
        "viṣayasya", "viṣaya", "Pum", "Sasthi", "Eka",
        run_id=RUN, context=ctx(167, "2b"), source="claude-reasoner",
        notes="objective genitive construing with vijñaptiḥ (trbh 173–174)")))

    # ---- v.2cd = trbh 177: tatrālayākhyaṃ vijñānaṃ vipākaḥ sarvabījakam
    r.append(("tatra known", "pass", verify.kosha_check(
        "tatra", run_id=RUN, context=ctx(177, "2c"), source="claude-reasoner")))
    r.append(("ālayākhyam (whole stem) nom.sg.n.", "pass", verify.verify_subanta_claim(
        "ālayākhyam", "ālayākhya", "Napumsaka", "Prathama", "Eka",
        run_id=RUN, context=ctx(177, "2c"), source="claude-reasoner",
        notes="bahuvrīhi 'whose name is ālaya' checked as opaque stem")))
    r.append(("ālayākhya relation", "unsupported", verify.mark_unsupported(
        "ālayākhyam",
        "samāsa relation (bahuvrīhi: ālaya ākhyā yasya) not expressible in vidyut",
        run_id=RUN, context=ctx(177, "2c"), source="claude-reasoner")))
    r.append(("vijñānam nom.sg.n.", "pass", verify.verify_subanta_claim(
        "vijñānam", "vijñāna", "Napumsaka", "Prathama", "Eka",
        run_id=RUN, context=ctx(177, "2c"), source="claude-reasoner")))
    r.append(("vipākaḥ (2c, predicative) nom.sg.m.", "pass", verify.verify_subanta_claim(
        "vipākaḥ", "vipāka", "Pum", "Prathama", "Eka",
        run_id=RUN, context=ctx(177, "2c"), source="claude-reasoner",
        notes="predicative: = vipākapariṇāmaḥ (trbh 180–181)")))
    r.append(("sarvabījakam (whole stem) nom.sg.n.", "pass", verify.verify_subanta_claim(
        "sarvabījakam", "sarvabījaka", "Napumsaka", "Prathama", "Eka",
        run_id=RUN, context=ctx(177, "2d"), source="claude-reasoner",
        notes="bahuvrīhi with samāsānta -ka, checked as opaque stem")))
    r.append(("sarvabījaka relation", "unsupported", verify.mark_unsupported(
        "sarvabījakam",
        "samāsa relation (bahuvrīhi: sarvāṇi bījāni yasmin, samāsānta ka) not "
        "expressible in vidyut; justified by trbh 189 sarvadharmabījāśrayatvāt",
        run_id=RUN, context=ctx(177, "2d"), source="claude-reasoner")))
    r.append(("bījaka member known", "pass", verify.kosha_check(
        "bījakam", run_id=RUN, context=ctx(177, "2d"), source="claude-reasoner")))

    ok = True
    for label, want, rec in r:
        got = rec["result"]
        mark = "OK " if got == want else "BAD"
        ok &= got == want
        extra = f" expected={rec['expected_forms']}" if got == "fail" else ""
        print(f"[{mark}] {label}: {got}{extra}")
    print(f"\n{len(r)} claims logged to {verify.LOG_PATH.name} (run_id={RUN})")
    print("VERIFY STAGE", "ALL AS EXPECTED" if ok else "HAS SURPRISES")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
