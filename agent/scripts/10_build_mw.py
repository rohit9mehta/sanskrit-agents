"""Build the MW sqlite index from the Cologne csl-orig master file (W1).

Downloads mw.txt if absent (scripts normally rely on the pre-fetched copy in
data/raw/mw/), parses <L>...<LEND> entries, writes data/mw/mw.sqlite keyed by
the SLP1 headword (k1). Idempotent: rebuilds only with --force.
"""

import re
import sqlite3
import sys

import requests

from shastrartha.texts import DATA_DIR

MW_RAW = DATA_DIR / "raw" / "mw" / "mw.txt"
MW_SQLITE = DATA_DIR / "mw" / "mw.sqlite"
URL = "https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-orig/v02/mw/mw.txt"

HEADER_RE = re.compile(r"<L>(?P<lnum>[^<]+)<pc>(?P<pc>[^<]+)<k1>(?P<k1>[^<]+)")


def main() -> int:
    force = "--force" in sys.argv
    if MW_SQLITE.exists() and not force:
        n = sqlite3.connect(MW_SQLITE).execute("SELECT COUNT(*) FROM entries").fetchone()[0]
        print(f"mw.sqlite exists ({n} entries); use --force to rebuild")
        return 0

    if not MW_RAW.exists():
        print("downloading mw.txt (~50 MB)...")
        MW_RAW.parent.mkdir(parents=True, exist_ok=True)
        with requests.get(URL, stream=True, timeout=600) as r:
            r.raise_for_status()
            with MW_RAW.open("wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)

    MW_SQLITE.parent.mkdir(parents=True, exist_ok=True)
    if MW_SQLITE.exists():
        MW_SQLITE.unlink()
    conn = sqlite3.connect(MW_SQLITE)
    conn.execute("CREATE TABLE entries (key TEXT, lnum TEXT, pc TEXT, body TEXT)")

    n, batch = 0, []
    header, body_lines = None, []
    with MW_RAW.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("<L>"):
                m = HEADER_RE.match(line)
                header = m.groupdict() if m else None
                body_lines = []
            elif line.startswith("<LEND>"):
                if header:
                    batch.append(
                        (header["k1"], header["lnum"], header["pc"], "\n".join(body_lines))
                    )
                    n += 1
                    if len(batch) >= 5000:
                        conn.executemany("INSERT INTO entries VALUES (?,?,?,?)", batch)
                        batch = []
                header = None
            else:
                body_lines.append(line)
    if batch:
        conn.executemany("INSERT INTO entries VALUES (?,?,?,?)", batch)
    conn.execute("CREATE INDEX idx_key ON entries(key)")
    conn.commit()
    conn.close()
    print(f"built {MW_SQLITE} with {n} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
