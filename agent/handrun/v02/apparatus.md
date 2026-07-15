# Triṃśikā v.2 — commentary-grounded translation with apparatus

Hand-run of the full agent loop (Phase 0, CLAUDE.md item 4). Reasoner: Claude
(2026-07-15). Tools: ByT5-Sanskrit (`chronbmm/sanskrit5-multitask`, local MPS)
+ Dharmamitra API for ANALYZE; pratīka-matcher alignment for RETRIEVE; MW
(Cologne 2020 scan) for dictionary; vidyut-prakriya/kosha for VERIFY
(run_id `handrun-v02-01` in `agent/logs/vidyut_verifications.jsonl`).

## Verse (bhāṣya reading; quoted at trbh 167 + 177, each closed by `iti`)

> **vipāko mananākhyaś ca vijñaptir viṣayasya ca |** (2ab = trbh 167)
> **tatrālayākhyaṃ vijñānaṃ vipākaḥ sarvabījakam ||** (2cd = trbh 177)

Context: continues v.1d `pariṇāmaḥ sa ca tridhā` ("and that transformation is
threefold", quoted at trbh 152); 2ab names the three, 2cd begins defining the
first. No bhāṣya/vulgate variants in this verse (trimsika.json).

## Word-by-word analysis

| # | surface | lemma | morphology | vidyut | note |
|---|---------|-------|------------|--------|------|
| 1 | vipākaḥ | vipāka | m. nom. sg. | pass (prakriyā) | name of pariṇāma #1 |
| 2 | mananākhyaḥ | mananākhya | m. nom. sg., bahuvrīhi ⟨manana-ākhyā yasya⟩ | stem pass; relation unsupported; member `manana` pass | = kliṣṭa manas (trbh 172) |
| 3 | ca | ca | indecl. | pass (kosha) | |
| 4 | vijñaptiḥ | vijñapti | f. nom. sg. | pass (prakriyā) | pariṇāma #3 (with 5) |
| 5 | viṣayasya | viṣaya | m. **gen.** sg. | pass (prakriyā) | objective genitive with vijñaptiḥ |
| 6 | ca | ca | indecl. | — (as 3) | postponed for metre |
| 7 | tatra | tatra | indecl. | pass (kosha) | "among these [three]" (trbh 179) |
| 8 | ālayākhyam | ālayākhya | n. nom. sg., bahuvrīhi ⟨ālaya ākhyā yasya⟩ | stem pass; relation unsupported | agrees with vijñānam |
| 9 | vijñānam | vijñāna | n. nom. sg. | pass (prakriyā) | `vijānātīti vijñānam` (trbh 187) |
| 10 | vipākaḥ | vipāka | m. nom. sg., predicative | pass (prakriyā) | = vipākapariṇāmaḥ (trbh 180–181) |
| 11 | sarvabījakam | sarvabījaka | n. nom. sg., bahuvrīhi ⟨sarvāṇi bījāni yasmin⟩ + samāsānta -ka | stem pass; relation unsupported; member `bījakam` pass | justified trbh 189 |

Sandhi in situ: `mananākhyaś ca` (ḥ→ś before c); `tatrālayākhyaṃ` (a+ā);
`vijñānaṃ` (m→ṃ). ANALYZE (local SLM) agreed on every lemma and tag
(`tool_outputs/analyze.json`); the samāsa analyses are the reasoner's,
grounded in the commentary below — exactly the division of labor the
verify-log's `unsupported` class records.

## Justification objects

**J1. The three pariṇāmas are named, not described — and the third is the
sixfold sense-consciousness.**
- Options: (a) 2ab is a loose description of mental change; (b) 2ab
  enumerates three technical transformations.
- Chosen: (b). Evidence: trbh 169 `sa eṣa trividhaḥ pariṇāmo vipākākhyo
  mananākhyo viṣayavijñaptyākhyaś ca` ("this threefold transformation is
  the one called vipāka, the one called manana, and the one called
  viṣaya-vijñapti"); trbh 173–174 `rūpādiviṣayapratyavabhāsatvāc
  cakṣurādivijñānaṃ ṣaṭprakāram api viṣayavijñaptiḥ` ("because it makes
  appear objects such as form, the sixfold eye-consciousness etc. is the
  object-representation").
- Depends on commentary: **yes** — "vijñaptir viṣayasya" alone does not say
  *whose* vijñapti or that it is sixfold.

**J2. mananākhya = the defiled mind (kliṣṭa manas).**
- Options: (a) "called thinking" generically; (b) the second-transformation
  manas of Yogācāra.
- Chosen: (b). Evidence: trbh 172 `kliṣṭaṃ mano nityaṃ mananātmakatvān
  mananākhyam` ("the defiled manas, because it always consists of mentation,
  is 'that called mentation'").
- Depends on commentary: **yes**.

**J3. viṣayasya is an objective genitive construing with vijñaptiḥ.**
- Options: (a) possessive ("the object's cognition"); (b) objective
  ("the making-known *of* objects").
- Chosen: (b), per trbh 173–174 (the compound restatement
  `viṣayavijñaptiḥ` resolves the case relation as karmaṇi).
- Vidyut: gen. sg. claim verified (designed dative counter-claim fails —
  see sanity log).

**J4. In 2cd `vipākaḥ` is predicative and identifies transformation #1 with
the ālaya-vijñāna alone.**
- Options: (a) "the ālaya-consciousness is maturation, all-seeded" as fresh
  description; (b) "among these [three], the [transformation called]
  maturation is the consciousness called ālaya".
- Chosen: (b). Evidence: trbh 175–176 `yasya yat svarūpaṃ tad yathākramaṃ
  pradarśayann āha` (the definitions come *in order*); trbh 179 `tatreti yo
  'yam anantaroktas trividhaḥ pariṇāmaḥ`; trbh 180–181 `ālayākhyam ity
  ālayavijñānasaṃjñakaṃ yad vijñānaṃ sa vipākapariṇāmaḥ`; trbh 188
  `sarvadhātugatiyonijātiṣu kuśalākuśalakarmavipākatvād vipākaḥ` (why the
  *name* applies: it is the maturation of good/bad karma across all realms,
  destinies, wombs, births).
- Depends on commentary: **yes** (this was the July-2026 "under-specified"
  case; glosses at trbh 188–189).

**J5. sarvabījakam is a bahuvrīhi: "possessing all seeds," not "the
universal seed."**
- Evidence: trbh 189 `sarvadharmabījāśrayatvāt sarvabījakam` ("because it is
  the substrate of the seeds of *all dharmas*, it has all seeds").
- Vidyut: whole-stem derivation passes; bahuvrīhi relation logged
  `unsupported` (vidyut samāsa gap) with the commentary as the warrant.

**J6 (apparatus bonus). ālaya carries a double etymology in the bhāṣya.**
- trbh 182–183 `sarvasāṃkleśikadharmabījasthānatvād ālayaḥ` + 184 `ālayaḥ
  sthānam iti paryāyau` (receptacle/place); trbh 185–186 alternative active
  and passive derivations from ā-√lī ("all dharmas nestle in it as effects;
  it nestles in all dharmas as cause"). MW s.v. ālaya (154,1): "receptacle,
  asylum" — cf. `himālaya`. Translation keeps "repository" in parentheses.

## Translation

> **(2)** [That transformation is threefold:] **maturation** (*vipāka*), that
> **called 'mentation'** (*manana*, i.e. the defiled mind), and the
> **making-known of objects** (*viṣaya-vijñapti*, the sixfold sense
> consciousness). Among these, the maturation[-transformation] is the
> consciousness called **ālaya** (the 'repository'), which **holds all the
> seeds**.

## One-shot delta (what commentary-blindness gets wrong here)

A commentary-blind rendering (cf. the July-2026 validation session recorded
in CLAUDE.md) plausibly yields: *"Maturation, that which is called thinking,
and the representation of the object; there, the consciousness called ālaya
is maturation, having all seeds."* Deficits fixed above: (i) no
identification of manana with the kliṣṭa manas (J2); (ii) "representation of
the object" left unresolved — not marked as the sixfold sense-consciousness
(J1, J3); (iii) 2cd read as description rather than as the first of three
ordered definitions (J4); (iv) sarvabījaka's bahuvrīhi force ("substrate of
the seeds of all dharmas") not secured (J5).

## Baseline comparison

- **Buescher 2007**: not digitized in this session — comparison pending
  Rohit's copy (do not fill from memory).
- **MITRA Translate / raw frontier LLM**: Phase 1 work (all 30 verses).

## Open questions

1. Whether to render *vijñapti* as "representation," "making-known," or
   leave untranslated; the bhāṣya's causative gloss (`...pratyavabhāsatvāt`,
   trbh 173) mildly favors an active rendering.
2. v.2's span [169, 201] ends where the ālambana discussion (190–201) is
   already pivoting to v.3ab (quoted at 202); border verses may want
   span_raw for retrieval.
3. The requote of 2c at trbh 231 (`tatrālayākhyaṃ vijñānam iti...`) opens
   the sthiti-section — Phase 1 retrieval could rank requote contexts too.
