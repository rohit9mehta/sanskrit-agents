"""Apparatus schema (Phase 1, W2) — the reasoner's structured output.

Mirrors the Phase 0 hand-run apparatus (agent/handrun/v02/apparatus.json) in a
form that is (a) mechanically checkable by the verify runner and (b) valid
under OpenAI strict structured outputs: every field required, optionals
nullable, no free-form dicts, enums as Literals.

Feature names use vidyut member names so claims feed verify.py directly.
"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Samasa(Strict):
    type: Literal[
        "tatpurusa", "karmadharaya", "bahuvrihi", "dvandva", "avyayibhava", "dvigu"
    ] = Field(description="Compound class")
    vigraha: str = Field(description="Analytical paraphrase, IAST (e.g. 'manana-ākhyā yasya')")
    members: list[str] = Field(description="Member stems in order, IAST")


class Morph(Strict):
    pos: Literal["subanta", "tinanta", "avyaya"]
    # subanta features (null unless pos == subanta)
    linga: Optional[Literal["Pum", "Stri", "Napumsaka"]]
    vibhakti: Optional[
        Literal[
            "Prathama", "Dvitiya", "Trtiya", "Caturthi",
            "Panchami", "Sasthi", "Saptami", "Sambodhana",
        ]
    ]
    vacana: Optional[Literal["Eka", "Dvi", "Bahu"]]
    # tinanta features (null unless pos == tinanta)
    root: Optional[str] = Field(description="Bare verbal root, IAST, no prefixes (e.g. 'vṛt')")
    prefixes: Optional[list[str]] = Field(description="Upasargas in order, IAST (e.g. ['pra'])")
    prayoga: Optional[Literal["Kartari", "Karmani", "Bhave"]]
    lakara: Optional[
        Literal["Lat", "Lit", "Lut", "Lrt", "Lot", "Lan", "VidhiLin", "AshirLin", "Lun", "Lrn"]
    ]
    purusha: Optional[Literal["Prathama", "Madhyama", "Uttama"]]


class WordAnalysis(Strict):
    surface: str = Field(
        description="Pausal (pre-sandhi) form as verified, IAST — e.g. 'vipākaḥ' not 'vipāko'"
    )
    surface_in_sandhi: str = Field(description="The form as it appears in the verse line")
    lemma: str = Field(description="Nominal stem or verbal root, IAST")
    morph: Morph
    samasa: Optional[Samasa]
    note: Optional[str]


class Evidence(Strict):
    lines: list[int] = Field(description="trbh.txt line numbers cited")
    quote: str = Field(description="The Sanskrit cited, IAST, verbatim from those lines")
    translation: str


class Justification(Strict):
    id: str = Field(description="J1, J2, ...")
    decision: str
    options_considered: list[str]
    chosen: str
    evidence: list[Evidence]
    depends_on_commentary: bool


class Apparatus(Strict):
    verse: int
    analysis: list[WordAnalysis]
    justifications: list[Justification]
    translation: str = Field(
        description="Verse-shaped English translation; technical terms parenthesized on first use"
    )
    one_shot_delta: list[str] = Field(
        description="What a commentary-blind translation would plausibly get wrong"
    )
    analyzer_disagreements: list[str] = Field(
        description="Where this analysis overrides the ByT5 tagger, with reason"
    )
    open_questions: list[str]
