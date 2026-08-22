# vyakarani-v1 vs ByT5 baseline — per stratum (features-full, lemma)

Overall: features-full 90% → **92%**; lemma 93% → **96%**; claim 88% → **90%** (n=985)

| stratum | n | features: base → v1 | lemma: base → v1 | Δfeat |
|---|---|---|---|---|
| sub:Prathama:Eka | 47 | 91% → **98%** | 94% → 98% | +3 |
| sub:Saptami:Bahu | 46 | 93% → **93%** | 96% → 100% | +0 |
| tin:Lan:Kartari | 44 | 95% → **98%** | 95% → 98% | +1 |
| sub:Trtiya:Eka | 44 | 93% → **98%** | 98% → 100% | +2 |
| tin:VidhiLin:Kartari | 43 | 95% → **95%** | 98% → 100% | +0 |
| tin:Lat:Karmani | 43 | 100% → **100%** | 98% → 88% | +0 |
| sub:Caturthi:Eka | 42 | 100% → **93%** | 100% → 95% | -3 |
| tin:Lrt:Kartari | 41 | 100% → **100%** | 100% → 100% | +0 |
| sub:Saptami:Eka | 41 | 90% → **98%** | 93% → 100% | +3 |
| sub:Prathama:Bahu | 41 | 83% → **90%** | 88% → 100% | +3 |
| sub:Panchami:Eka | 41 | 68% → **85%** | 80% → 100% | +7 |
| sub:Sasthi:Bahu | 40 | 95% → **92%** | 98% → 100% | -1 |
| sub:Trtiya:Bahu | 39 | 100% → **90%** | 100% → 100% | -4 |
| sub:Prathama:Dvi | 39 | 95% → **97%** | 95% → 100% | +1 |
| tin:Lit:Kartari | 39 | 97% → **100%** | 100% → 95% | +1 |
| tin:Lot:Kartari | 39 | 97% → **92%** | 100% → 95% | -2 |
| sub:Dvitiya:Bahu | 38 | 92% → **100%** | 95% → 95% | +3 |
| sub:Dvitiya:Eka | 36 | 81% → **86%** | 92% → 100% | +2 |
| pipeline-hard | 35 | 69% → **74%** | 29% → 43% | +2 |
| tin:Lat:Kartari | 35 | 97% → **94%** | 97% → 94% | -1 |
| sub:Sasthi:Eka | 33 | 91% → **97%** | 100% → 100% | +2 |
| sub:Sambodhana:Eka | 23 | 96% → **78%** | 96% → 96% | -4 |
| sub:Dvitiya:Dvi | 21 | 95% → **67%** | 100% → 100% | -6 |
| tin:Lun:Kartari | 20 | 5% → **80%** | 90% → 85% | +15 |
| sub:Sasthi:Dvi | 17 | 88% → **88%** | 94% → 100% | +0 |
| tin:Lot:Karmani | 13 | 100% → **100%** | 100% → 92% | +0 |
| sub:Trtiya:Dvi | 12 | 100% → **100%** | 100% → 100% | +0 |
| sub:Panchami:Bahu | 9 | 78% → **78%** | 89% → 100% | +0 |
| sub:Caturthi:Bahu | 7 | 86% → **100%** | 86% → 100% | +1 |
| tin:Lun:Karmani | 5 | 100% → **100%** | 100% → 80% | +0 |
| tin:Lan:Karmani | 3 | 100% → **100%** | 100% → 100% | +0 |
| sub:Sambodhana:Bahu | 3 | 100% → **67%** | 100% → 100% | -1 |
| tin:Lut:Kartari | 2 | 0% → **100%** | 100% → 100% | +2 |
| sub:Saptami:Dvi | 2 | 50% → **0%** | 50% → 100% | -1 |
| sub:Panchami:Dvi | 1 | 100% → **0%** | 100% → 100% | -1 |
| tin:VidhiLin:Karmani | 1 | 100% → **100%** | 100% → 100% | +0 |

## Biggest movers (items)

gains: tin:Lun:Kartari +15/20, sub:Panchami:Eka +7/41, sub:Prathama:Eka +3/47, sub:Saptami:Eka +3/41, sub:Prathama:Bahu +3/41, sub:Dvitiya:Bahu +3/38, sub:Trtiya:Eka +2/44, sub:Dvitiya:Eka +2/36, pipeline-hard +2/35, sub:Sasthi:Eka +2/33

losses: sub:Dvitiya:Dvi -6/21, sub:Trtiya:Bahu -4/39, sub:Sambodhana:Eka -4/23, sub:Caturthi:Eka -3/42, tin:Lot:Kartari -2/39, sub:Sasthi:Bahu -1/40, tin:Lat:Kartari -1/35, sub:Sambodhana:Bahu -1/3, sub:Saptami:Dvi -1/2, sub:Panchami:Dvi -1/1

## Structural cells (categories ByT5's tagset cannot express)

| cell | n | base | v1 |
|---|---|---|---|
| tin:Lun:Kartari | 20 | 5% | **80%** |
| tin:Lun:Karmani | 5 | 100% | **100%** |
| tin:Lut:Kartari | 2 | 0% | **100%** |
| tin:Lrt:Kartari | 41 | 100% | **100%** |
| tin:Lit:Kartari | 39 | 97% | **100%** |
| tin:Lan:Kartari | 44 | 95% | **98%** |
| pipeline-hard | 35 | 69% | **74%** |

## v1 misses by type

| miss | n |
|---|---|
| linga | 27 |
| vibhakti | 19 |
| pos wrong | 8 |
| vibhakti+linga | 6 |
| lakara | 5 |
| vibhakti+vacana | 4 |
| vacana | 2 |
| purusha+vacana | 2 |
| vacana+linga | 1 |
