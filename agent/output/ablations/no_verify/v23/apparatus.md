# Triṃśikā v.23 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 8 pass / 0 fail / 0 unsupported.

## Verse

> **trividhasya svabhāvasya trividhāṃ niḥsvabhāvatām | sandhāya sarvadharmāṇāṃ deśitā niḥsvabhāvatā**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| trividhasya | trividha | Pum. Sasthi/Eka; bahuvrihi ⟨trayo vidhāḥ yasya saḥ⟩ | pass |
| svabhāvasya | svabhāva | Pum. Sasthi/Eka; tatpurusa ⟨svasya bhāvaḥ⟩ | pass |
| trividhām | trividha | Stri. Dvitiya/Eka; bahuvrihi ⟨trayo vidhāḥ yasyāḥ sā⟩ | pass |
| niḥsvabhāvatām | niḥsvabhāvatā | Stri. Dvitiya/Eka | pass |
| sandhāya | dhā | indecl. | pass |
| sarvadharmāṇām | sarvadharma | Pum. Sasthi/Bahu; karmadharaya ⟨sarve dharmāḥ⟩ | pass |
| deśitā | deśita | Stri. Prathama/Eka | pass |
| niḥsvabhāvatā | niḥsvabhāvatā | Stri. Prathama/Eka | pass |

## Justifications

**J1. The numerical expression is restrictive: there are three svabhāvas and no fourth.**
- chosen: trividhasya svabhāvasya = ‘of the threefold own-nature,’ i.e. the doctrinal triad of exactly three svabhāvas, not a loose adjective ‘various’ or an open-ended plurality. (depends on commentary: **yes**)
- trbh [1391]: `traya eva svabhāvā na caturtho 'stīti jñāpanārthaṃ saṃkhyānirdeśaḥ` — The numerical specification is for making known: there are just three svabhāvas; there is no fourth.

**J2. Do not translate svabhāva as ordinary ‘character’ or as an unqualified ultimately real essence; the commentary defines it through seeming existence by its own lakṣaṇa.**
- chosen: svabhāva is rendered ‘own-nature/own-being,’ with ‘own’ tied to a thing’s own characteristic and with vidyamānavat marking ‘as though existent.’ (depends on commentary: **yes**)
- trbh [1392, 1393]: `svena
svena lakṣaṇena vidyamānavad bhavatīti svbhāvaḥ` — It is svabhāva because it comes to be as though existent by its own, by its own characteristic.

**J3. The first niḥsvabhāvatā is not a single undifferentiated negation; it has three specified modes.**
- chosen: trividhāṃ niḥsvabhāvatām = the threefold absence of own-nature: absence with respect to characteristic, arising, and ultimate reality. (depends on commentary: **yes**)
- trbh [1394, 1395]: `trividhā niḥsvabhāvatā lakṣaṇaniḥsvabhāvatā utpattiniḥsvabhāvatā
paramārthaniḥsvabhāvatā ca` — The absence of own-nature is threefold: absence of own-nature with respect to characteristic, absence of own-nature with respect to arising, and absence of own-nature with respect to ultimate reality.

**J4. The genitive does not mean ‘of all moral laws’ or ‘to all teachings’; the commentary identifies all dharmas by the Yogācāra three-nature scheme.**
- chosen: sarvadharmāṇām is ‘of all dharmas/phenomena,’ where the domain is constituted by the imagined, dependent, and perfected natures. (depends on commentary: **yes**)
- trbh [1396, 1397]: `sarvadharmāḥ
parikalpitaparatantrapariniṣpannātmakāḥ` — All dharmas are those whose nature consists of the imagined, the dependent, and the perfected.

**J5. The universal teaching ‘the absence of own-nature of all dharmas was taught’ is to be read as made with reference to the threefold niḥsvabhāvatā of the three svabhāvas, not as a physical ‘joining’ or as an unrelated absolutist denial.**
- chosen: sandhāya is construed with the preceding accusative trividhāṃ niḥsvabhāvatām and rendered ‘having in view / with reference to.’ (depends on commentary: **yes**)
- trbh [1394, 1395]: `trividhā niḥsvabhāvatā lakṣaṇaniḥsvabhāvatā utpattiniḥsvabhāvatā
paramārthaniḥsvabhāvatā ca` — The absence of own-nature is threefold: absence with respect to characteristic, arising, and ultimate reality.
- trbh [1396, 1397]: `sarvadharmāḥ
parikalpitaparatantrapariniṣpannātmakāḥ` — All dharmas are those whose nature consists of the imagined, the dependent, and the perfected.

## Translation

> Having in view the threefold absence of own-nature (niḥsvabhāvatā)
of the threefold own-nature (svabhāva),
the absence of own-nature of all dharmas (sarvadharmāḥ) was taught—
dharmas whose nature is imagined, dependent, and perfected.

## Analyzer disagreements

- For niḥsvabhāvatām and niḥsvabhāvatā, ByT5 segments niḥsvabhāva + tām/tā; I treat each as one abstract noun stem niḥsvabhāvatā with suffix -tā, since the verse has a single technical abstract and the bhāṣya at trbh 1394 says trividhā niḥsvabhāvatā.
- For sarvadharmāṇām, ByT5 reports sarva_Cp plus inflected head dharma; per the requested compound convention, the lemma is the whole inflected compound stem sarvadharma. The bhāṣya re-quotes the unit as sarvadharmāḥ at trbh 1396.
- For sandhāya, ByT5 gives the lexical compound verb saṃdhā; I normalize it as an indeclinable gerund of bare root dhā with prefix sam, as requested for verbal forms.
- For deśitā, ByT5’s deśay lemma is normalized to the nominal participial stem deśita, feminine nominative singular, while retaining the causative-passive sense ‘taught.’

## One-shot delta

- A commentary-blind translation might render trividhasya as merely ‘various’ or ‘triple’ and miss Sthiramati’s restriction: exactly three svabhāvas and no fourth.
- It might flatten trividhāṃ niḥsvabhāvatām into a single generic ‘essencelessness,’ missing the three modes: lakṣaṇa-, utpatti-, and paramārtha-niḥsvabhāvatā.
- It might take sarvadharmāṇām as ‘all laws/teachings’ rather than all dharmas constituted by the imagined, dependent, and perfected natures.
- It might translate sandhāya literally as ‘joining’ rather than ‘having in view / with reference to’ the threefold niḥsvabhāvatā.
