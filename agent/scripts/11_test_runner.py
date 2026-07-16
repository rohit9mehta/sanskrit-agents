"""W2 regression test: the verify runner must reproduce the Phase 0 hand-run
outcomes on v.2's known-good analysis (all 11 words pass, compounds via the
opaque-stem policy), and must reject designed negatives."""

import sys

from shastrartha.runner import pipeline_verify
from shastrartha.schema import Apparatus, Morph, Samasa, WordAnalysis

RUN = "test-runner-01"


def sub(surface, sandhi, lemma, linga, vibhakti, vacana, samasa=None, note=None):
    return WordAnalysis(
        surface=surface, surface_in_sandhi=sandhi, lemma=lemma,
        morph=Morph(pos="subanta", linga=linga, vibhakti=vibhakti, vacana=vacana,
                    root=None, prefixes=None, prayoga=None, lakara=None, purusha=None),
        samasa=samasa, note=note,
    )


def avy(surface):
    return WordAnalysis(
        surface=surface, surface_in_sandhi=surface, lemma=surface,
        morph=Morph(pos="avyaya", linga=None, vibhakti=None, vacana=None,
                    root=None, prefixes=None, prayoga=None, lakara=None, purusha=None),
        samasa=None, note=None,
    )


def main() -> int:
    good = Apparatus(
        verse=2,
        analysis=[
            sub("vipākaḥ", "vipāko", "vipāka", "Pum", "Prathama", "Eka"),
            sub("mananākhyaḥ", "mananākhyaś", "mananākhya", "Pum", "Prathama", "Eka",
                samasa=Samasa(type="bahuvrihi", vigraha="manana-ākhyā yasya",
                              members=["manana", "ākhyā"])),
            avy("ca"),
            sub("vijñaptiḥ", "vijñaptir", "vijñapti", "Stri", "Prathama", "Eka"),
            sub("viṣayasya", "viṣayasya", "viṣaya", "Pum", "Sasthi", "Eka"),
            avy("tatra"),
            sub("ālayākhyam", "ālayākhyaṃ", "ālayākhya", "Napumsaka", "Prathama", "Eka",
                samasa=Samasa(type="bahuvrihi", vigraha="ālaya ākhyā yasya",
                              members=["ālaya", "ākhyā"])),
            sub("vijñānam", "vijñānaṃ", "vijñāna", "Napumsaka", "Prathama", "Eka"),
            sub("sarvabījakam", "sarvabījakam", "sarvabījaka", "Napumsaka", "Prathama", "Eka",
                samasa=Samasa(type="bahuvrihi", vigraha="sarvāṇi bījāni yasmin",
                              members=["sarva", "bīja"])),
        ],
        justifications=[], translation="", one_shot_delta=[],
        analyzer_disagreements=[], open_questions=[],
    )
    rep = pipeline_verify(good, RUN)
    print("good apparatus:", rep.n)
    ok = rep.n["pass"] == 9 and rep.n["fail"] == 0 and rep.n["tool_error"] == 0

    bad = Apparatus(
        verse=2,
        analysis=[
            sub("viṣayasya", "viṣayasya", "viṣaya", "Pum", "Caturthi", "Eka"),  # dative lie
            avy("vipākaḥ"),                                                     # fake avyaya
            sub("vijñaptiḥ", "vijñaptir", "vijñapti", "Pum", "Prathama", "Eka",
                samasa=None, note=None) if False else
            WordAnalysis(surface="pravartate", surface_in_sandhi="pravartate",
                         lemma="vṛt",
                         morph=Morph(pos="tinanta", linga=None, vibhakti=None, vacana="Eka",
                                     root="vṛt", prefixes=["pra"], prayoga="Kartari",
                                     lakara="Lot", purusha="Prathama"),
                         samasa=None, note=None),                               # wrong lakāra
        ],
        justifications=[], translation="", one_shot_delta=[],
        analyzer_disagreements=[], open_questions=[],
    )
    rep2 = pipeline_verify(bad, RUN)
    print("bad apparatus:", rep2.n)
    for w in rep2.failures:
        print("  FAIL:", w.surface, "—", w.detail, w.expected[:4])
    ok &= rep2.n["fail"] == 3
    print("feedback preview:\n" + rep2.feedback())

    print("RUNNER TEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
