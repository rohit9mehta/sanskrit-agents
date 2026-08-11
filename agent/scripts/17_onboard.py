"""Onboard GRETIL text+commentary files into the library (Phase 3, L2).

Usage: 17_onboard.py {isa|yogasutra|gita}

Each parser converts its source's pre-aligned markers into library units
(mūla passage + line-numbered commentary). Commentary paragraphs are split
into citable lines at daṇḍa/sentence boundaries.
"""

import re
import sys

from shastrartha.library import save_text
from shastrartha.texts import DATA_DIR

RAW = DATA_DIR / "raw"


def body_after_text_marker(path) -> str:
    raw = path.read_text(encoding="utf-8")
    return raw.split("\n# Text\n", 1)[1]


def split_citable(paragraphs: list[str], danda: str = "/") -> list[str]:
    """Split prose into citable lines at daṇḍa (or sentence) boundaries,
    keeping the delimiter; drop empties."""
    lines: list[str] = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if danda == "/":
            parts = re.split(r"(?<=/)\s+", para)
        elif danda == "|":  # Gītā-bhāṣya daṇḍa (single pipe; '||' markers gone)
            parts = re.split(r"(?<=\|)\s+(?!\|)", para)
        else:  # YS bhāṣya uses '.' as daṇḍa
            parts = re.split(r"(?<=\.)\s+", para)
        for p in parts:
            p = p.strip()
            if p:
                lines.append(p)
    return lines


def onboard_isa() -> tuple[str, list[dict]]:
    body = body_after_text_marker(
        RAW / "sa_IzopaniSad-or-IzAvAsyopaniSadkANva-recension-comm.txt")
    # mantra: text ending `|| isup_N ||`; bhāṣya: until `//isupbh_N//`
    units = []
    pat = re.compile(
        r"(?P<mula>[^\n]+?)\s*\|\|\s*isup_(?P<n>\d+)\s*\|\|"
        r"(?P<comm>.*?)//\s*isupbh_(?P=n)\s*//",
        re.S)
    for m in pat.finditer(body):
        comm_paras = m.group("comm").split("\n")
        units.append({
            "id": m.group("n"),
            "mula": re.sub(r"\s+", " ", m.group("mula")).strip(),
            "commentary": split_citable(comm_paras, danda="/"),
        })
    return "Īśopaniṣad (Kāṇva) with Śaṅkara-bhāṣya", units


def onboard_yogasutra() -> tuple[str, list[dict]]:
    body = body_after_text_marker(RAW / "sa_pataJjali-yogasUtra-with-bhASya.txt")
    marker = re.compile(r"\|\|\s*ys_(\d+\.\d+)\s*\|\|")
    parts = marker.split(body)
    # parts = [pre, id1, seg1, id2, seg2, ...]; each seg = bhāṣya of idN
    # + possibly the avatāraṇikā and sūtra text of id(N+1) at its tail.
    # The sūtra text of unit i sits at the END of the previous segment,
    # after the last sentence daṇḍa ('.') or '---'.
    units = []
    prev_tail = parts[0]
    for i in range(1, len(parts) - 1, 2):
        uid, seg = parts[i], parts[i + 1]
        # sūtra = last chunk of prev_tail after '---' or final '.'
        tail = prev_tail.strip()
        m = re.search(r"---\s*(?P<s>[^.]*?)$", tail, re.S)
        if m and m.group("s").strip():
            sutra = m.group("s")
        else:
            sutra = tail.rsplit(".", 1)[-1] if "." in tail else tail
            if len(sutra.split()) > 25:  # opening invocation etc.
                sutra = " ".join(sutra.split()[-25:])
        # bhāṣya of this unit = seg minus the NEXT unit's trailing sūtra
        units.append({"id": uid,
                      "mula": re.sub(r"\s+", " ", sutra).strip(" -—"),
                      "commentary": None,  # filled below
                      "_seg": seg})
        prev_tail = seg
    for i, u in enumerate(units):
        seg = u.pop("_seg")
        if i + 1 < len(units):
            nxt_sutra = units[i + 1]["mula"]
            cut = seg.rfind(nxt_sutra[:40])
            if cut > 0:
                seg = seg[:cut]
            m = re.search(r"---", seg[-400:])
            if m:
                seg = seg[: len(seg) - 400 + m.start()]
        u["commentary"] = split_citable(seg.split("\n"), danda=".")
    return "Pātañjala-yogasūtra with Vyāsa-bhāṣya (Āgāśe 1904)", units


def onboard_gita() -> tuple[str, list[dict]]:
    body = body_after_text_marker(RAW / "sa_bhagavadgItA-comm.txt")
    marker = re.compile(r"\|\|\s*bhg[_ ](\d+\.\d+)\s*\|\|")
    parts = marker.split(body)
    units = []
    prev_tail = parts[0]
    for i in range(1, len(parts) - 1, 2):
        uid, seg = parts[i], parts[i + 1]
        # verse text = trailing verse lines of prev_tail (from last blank line
        # that precedes verse-looking lines)
        tail_lines = [ln for ln in prev_tail.strip().split("\n")]
        verse_lines = []
        for ln in reversed(tail_lines):
            s = ln.strip()
            if not s:
                break
            if s.startswith("=") or s.startswith("bhg "):
                break
            verse_lines.append(s)
        verse = " ".join(reversed(verse_lines))
        units.append({"id": uid,
                      "mula": re.sub(r"\s+", " ", verse).strip(" |"),
                      "commentary": None, "_seg": seg})
        prev_tail = seg
    for i, u in enumerate(units):
        seg = u.pop("_seg")
        # commentary of unit i = seg minus the next verse block at its tail
        lines = seg.strip().split("\n")
        if i + 1 < len(units):
            nxt_first_words = " ".join(units[i + 1]["mula"].split()[:4])
            for j, ln in enumerate(lines):
                if nxt_first_words and nxt_first_words in re.sub(r"\s+", " ", ln):
                    lines = lines[:j]
                    break
        comm = [ln for ln in lines
                if ln.strip() and not ln.strip().startswith("=")
                and not re.match(r"^bhg \d+\s*$", ln.strip())]
        u["commentary"] = split_citable(comm, danda="|")
    return "Bhagavad-Gītā with Śaṅkara-bhāṣya", units


REGISTRY = {
    "isa": (onboard_isa, "isup",
            {"file": "sa_IzopaniSad-or-IzAvAsyopaniSadkANva-recension-comm.txt",
             "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_IzopaniSad-or-IzAvAsyopaniSadkANva-recension-comm.txt",
             "license": "CC BY-NC-SA 4.0 (GRETIL)",
             "caveats": "commentary unproofread and largely unsegmented (per file header); mūla checked against Limaye/Vadekar 1958"}),
    "yogasutra": (onboard_yogasutra, "ys",
                  {"file": "sa_pataJjali-yogasUtra-with-bhASya.txt",
                   "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_pataJjali-yogasUtra-with-bhASya.txt",
                   "edition": "Āgāśe 1904 (Ānandāśrama Sanskrit Series 47)",
                   "license": "CC BY-NC-SA 4.0 (GRETIL)"}),
    "gita": (onboard_gita, "gita",
             {"file": "sa_bhagavadgItA-comm.txt",
              "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_bhagavadgItA-comm.txt",
              "license": "CC BY-NC-SA 4.0 (GRETIL)",
              "caveats": "plaintext header lists no edition; Śaṅkara-bhāṣya per in-file title"}),
}


def main() -> int:
    slug = sys.argv[1] if len(sys.argv) > 1 else ""
    if slug not in REGISTRY:
        print(f"usage: 17_onboard.py {{{'|'.join(REGISTRY)}}}")
        return 1
    fn, tag, source = REGISTRY[slug]
    title, units = fn()
    n_comm = sum(1 for u in units if u["commentary"])
    n_lines = sum(len(u["commentary"]) for u in units)
    save_text(slug, title, tag, source, units)
    print(f"{slug}: {len(units)} units ({n_comm} with commentary, "
          f"{n_lines} citable lines) -> data/texts/{slug}/text.json")
    empty_mula = [u["id"] for u in units if len(u["mula"]) < 10]
    if empty_mula:
        print("  WARN short mūla:", empty_mula[:10])
    return 0


if __name__ == "__main__":
    sys.exit(main())
