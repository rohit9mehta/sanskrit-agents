"""Multi-text library registry (Phase 3).

Each onboarded text lives at agent/data/texts/<slug>/text.json:

  {"slug", "title", "citation_tag",       # e.g. "gita" → cite as "gita 2.11:3"
   "source": {file, url, edition, caveats},
   "units": [{"id": "2.11", "mula": "...", "commentary": ["line1", ...]}]}

Units are pre-aligned (mūla passage + its commentary, line-numbered from 1
within the unit). The Triṃśikā keeps its legacy pipeline; texts onboarded via
scripts/17_onboard.py use this registry and pipeline.run_unit().
"""

import json
from dataclasses import dataclass, field
from functools import lru_cache

from .texts import DATA_DIR

TEXTS_DIR = DATA_DIR / "texts"


@dataclass
class TextUnit:
    id: str
    mula: str
    commentary: list[str] = field(default_factory=list)

    def commentary_numbered(self) -> str:
        return "\n".join(f"{i}\t{ln}" for i, ln in enumerate(self.commentary, 1))


@dataclass
class LibText:
    slug: str
    title: str
    citation_tag: str
    source: dict
    units: dict[str, TextUnit]
    order: list[str]

    def unit(self, unit_id: str) -> TextUnit:
        return self.units[unit_id]


@lru_cache(maxsize=None)
def load_text(slug: str) -> LibText:
    d = json.loads((TEXTS_DIR / slug / "text.json").read_text(encoding="utf-8"))
    units = {u["id"]: TextUnit(u["id"], u["mula"], u.get("commentary", []))
             for u in d["units"]}
    return LibText(
        slug=d["slug"], title=d["title"], citation_tag=d["citation_tag"],
        source=d.get("source", {}), units=units,
        order=[u["id"] for u in d["units"]],
    )


def list_texts() -> list[str]:
    if not TEXTS_DIR.exists():
        return []
    return sorted(p.name for p in TEXTS_DIR.iterdir() if (p / "text.json").exists())


def save_text(slug: str, title: str, citation_tag: str, source: dict,
              units: list[dict]) -> None:
    out = TEXTS_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "text.json").write_text(
        json.dumps({"slug": slug, "title": title, "citation_tag": citation_tag,
                    "source": source, "units": units}, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )
    load_text.cache_clear()
