# DCS sample — license and attribution

Data in `raw/` is sampled from the Digital Corpus of Sanskrit (DCS),
github.com/OliverHellwig/sanskrit (dcs/data/conllu), licensed **CC BY 4.0**.

Citation (per upstream readme):

    @Manual{dcs,
      title  = {{The Digital Corpus of Sanskrit (DCS)}},
      author = {Hellwig, Oliver},
      year   = {2010--2024}}

Sampled by `agent/scripts/27_fetch_dcs.py` (genre-stratified, chosen to fill
morphological coverage gaps — see `agent/data/training/coverage.md`).
Converted records: `agent/data/training/dcs_pool.jsonl`.
