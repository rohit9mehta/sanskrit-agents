"""Environment smoke test: imports, data presence, canonical text invariants."""

import sys

def main() -> int:
    ok = True

    import requests, rapidfuzz, vidyut  # noqa: F401
    from shastrartha import texts, normalize, verify

    n = len(texts.trbh_lines())
    print(f"trbh.txt lines: {n} (expect {texts.TRBH_LINE_COUNT})")
    ok &= n == texts.TRBH_LINE_COUNT
    n2 = len(texts.unsandhied_lines())
    print(f"trbh.txt.unsandhied lines: {n2}")
    ok &= n2 == texts.TRBH_LINE_COUNT

    print(f"sentence-end lines: {sum(texts.is_sentence_end(i) for i in range(1, n + 1))} (expect 1010)")
    print(f"normalize.skeleton(line 1): {normalize.skeleton(texts.line(1))!r}")

    print(f"vidyut data dir: {verify.VIDYUT_DATA} exists={verify.VIDYUT_DATA.exists()}")
    ok &= verify.VIDYUT_DATA.exists()
    k = verify.kosha()
    hit = k.get("pravartate")
    print(f"kosha loads; get('pravartate') -> {len(hit)} entries")
    ok &= len(hit) > 0
    print(f"lipi: vipākaḥ -> {verify.to_slp1('vipākaḥ')}")
    ok &= verify.to_slp1("vipākaḥ") == "vipAkaH"

    try:
        from shastrartha.analyze import dharmamitra_tag
        res = dharmamitra_tag(["tathā"], use_cache=True)
        print(f"Dharmamitra API: ok -> {res[0]!r}")
    except Exception as e:
        print(f"Dharmamitra API: UNAVAILABLE ({type(e).__name__}: {e}) — local model is the fallback")

    print("SETUP", "OK" if ok else "BROKEN")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
