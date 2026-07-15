# ByT5-Sanskrit sanity report

Lines tested: [1, 24, 61, 147, 167, 172, 177, 188, 202, 1052]

| line | api=2022 | local=2022 | api=local | local-vs-2022 sim |
|---|---|---|---|---|
| 1 | ✗ | ✓ | ✗ | 1.000 |
| 24 | ✓ | ✓ | ✓ | 1.000 |
| 61 | ✗ | ✗ | ✓ | 0.909 |
| 147 | ✓ | ✓ | ✓ | 1.000 |
| 167 | ✓ | ✓ | ✓ | 1.000 |
| 172 | ✓ | ✓ | ✓ | 1.000 |
| 177 | ✗ | ✓ | ✗ | 1.000 |
| 188 | ✓ | ✓ | ✓ | 1.000 |
| 202 | ✗ | ✗ | ✗ | 0.667 |
| 1052 | ✗ | ✗ | ✓ | 0.833 |

2-of-3 consensus: 9/10; zero-consensus lines: [202]

## Decision

The **local model is the primary ANALYZE provider** (S for segmentation, SLM for lemma+morphosyntax). The API under-splits compounds relative to both other sources (lines 1, 177: `apratipanna|vipratipanna` and `sarva|bījakam` not split) and silently dropped the long opening compound of line 202. Keep the API as a fast cross-check only.

## Notable finding (line 202)

`asaṃviditakopādisthānavijñaptikaṃ` — both the local model and the 2022 file segment `...ka|upādi...` as `kopa|ādi` ('anger' + 'etc.'), but Sthiramati's own gloss (trbh 203–215, `upādānam upādiḥ ...`) shows the correct division is `asaṃviditaka|upādi|sthāna|vijñaptika`. This is precisely the failure mode the commentary-grounding loop exists to fix, reproduced by the sanity check itself.

## line 1

- **raw**: `pudgaladharmanairātmyayor apratipannavipratipannānām`
- **2022**: `pudgala-dharma-nairātmyayoḥ apratipanna-vipratipannānām`
- **API**: `pudgala_dharma_nairātmyayoḥ_apratipannavipratipannānām_`
- **local S**: `pudgala_dharma_nairātmyayoḥ_apratipanna_vipratipannānām_`
- **local SLM**: `pudgala_pudgala_Cp dharma_dharma_Cp nairātmyayoḥ_nairātmya_DuLNe apratipanna_apratipanna_Cp vipratipannānām_vipratipad_PGPaM`

## line 24

- **raw**: `ātmadharmopacāro hi vividho yaḥ pravartate`
- **2022**: `ātma-dharma-upacāraḥ hi vividhaḥ yaḥ pravartate`
- **API**: `ātma_dharma_upacāraḥ_hi_vividhaḥ_yaḥ_pravartate_`
- **local S**: `ātma_dharma_upacāraḥ_hi_vividhaḥ_yaḥ_pravartate_`
- **local SLM**: `ātma_ātman_Cp dharma_dharma_Cp upacāraḥ_upacāra_SNM hi_hi_ vividhaḥ_vividha_SNM yaḥ_yad_SNM pravartate_pravṛt_SPr3In`

## line 61

- **raw**: `evañ ca sarvaṃ vijñeyaṃ parikalpitasvabhāvatvād vastuto na vidyate vijñānaṃ`
- **2022**: `evan ca sarvam vijñeyam parikalpita-svabhāva-tvāt vastutas na vidyate vijñānam`
- **API**: `evam_ca_sarvam_vijñeyam_parikalpita_svabhāva_tvāt_vastutas_na_vidyate_vijñānam_`
- **local S**: `evam_ca_sarvam_vijñeyam_parikalpita_svabhāva_tvāt_vastutas_na_vidyate_vijñānam_`
- **local SLM**: `evam_evam_ ca_ca_ sarvam_sarva_SNNe vijñeyam_vijñā_SNNeGd parikalpita_parikalpay_PaCp svabhāva_svabhāva_Cp tvāt_tva_SBNe vastutas_vastutas_ na_na_ vidyate_vid_SPr3InPv vijñānam_vijñāna_SNNe`

## line 147

- **raw**: `tatra yad uktaṃ asaty ātmani mukhye dharmeṣu copacāro na yukta iti`
- **2022**: `tatra yat uktam asati ātmani mukhye dharmeṣu ca-upacāraḥ na yuktaḥ iti`
- **API**: `tatra_yat_uktam_asati_ātmani_mukhye_dharmeṣu_ca_upacāraḥ_na_yuktaḥ_iti_`
- **local S**: `tatra_yat_uktam_asati_ātmani_mukhye_dharmeṣu_ca_upacāraḥ_na_yuktaḥ_iti_`
- **local SLM**: `tatra_tatra_ yat_yad_SNNe uktam_vac_SNPaNe asati_asat_SLM ātmani_ātman_SLM mukhye_mukhya_SLM dharmeṣu_dharma_PLM ca_ca_ upacāraḥ_upacāra_SNM na_na_ yuktaḥ_yuj_SNPaM iti_iti_`

## line 167

- **raw**: `vipāko mananākhyaś ca vijñaptir viṣayasya ca`
- **2022**: `vipākaḥ mananā-ākhyaḥ ca vijñaptiḥ viṣayasya ca`
- **API**: `vipākaḥ_manana_ākhyaḥ_ca_vijñaptiḥ_viṣayasya_ca_`
- **local S**: `vipākaḥ_manana_ākhyaḥ_ca_vijñaptiḥ_viṣayasya_ca_`
- **local SLM**: `vipākaḥ_vipāka_SNM manana_manana_Cp ākhyaḥ_ākhyā_SNM ca_ca_ vijñaptiḥ_vijñapti_SNF viṣayasya_viṣaya_SGM ca_ca_`

## line 172

- **raw**: `kliṣṭaṃ mano nityaṃ mananātmakatvān mananākhyam`
- **2022**: `kliṣṭam manaḥ nityam mananā-ātmaka-tvāt manana-ākhyam`
- **API**: `kliṣṭam_manaḥ_nityam_manana_ātmaka_tvāt_manana_ākhyam_`
- **local S**: `kliṣṭam_manaḥ_nityam_manana_ātmaka_tvāt_manana_ākhyam_`
- **local SLM**: `kliṣṭam_kliś_SNPaNe manaḥ_manas_SNNe nityam_nitya_SNNe manana_manana_Cp ātmaka_ātmaka_Cp tvāt_tva_SBNe manana_manana_Cp ākhyam_ākhyā_SNNe`

## line 177

- **raw**: `tatrālayākhyaṃ vijñānaṃ vipākaḥ sarvabījakam`
- **2022**: `tatra-ālaya-ākhyam vijñānam vipākaḥ sarva-bījakam`
- **API**: `tatra_ālaya_ākhyam_vijñānam_vipākaḥ_sarvabījakam_`
- **local S**: `tatra_ālaya_ākhyam_vijñānam_vipākaḥ_sarva_bījakam_`
- **local SLM**: `tatra_tatra_ ālaya_ālaya_Cp ākhyam_ākhyā_SNNe vijñānam_vijñāna_SNNe vipākaḥ_vipāka_SNM sarva_sarva_Cp bījakam_bījaka_SNNe`

## line 188

- **raw**: `sarvadhātugatiyonijātiṣu kuśalākuśalakarmavipākatvād vipākaḥ`
- **2022**: `sarva-dhātu-gati-yoni-jātiṣu kuśala-akuśala-karma-vipāka-tvāt vipākaḥ`
- **API**: `sarva_dhātu_gati_yoni_jātiṣu_kuśala_akuśala_karma_vipāka_tvāt_vipākaḥ_`
- **local S**: `sarva_dhātu_gati_yoni_jātiṣu_kuśala_akuśala_karma_vipāka_tvāt_vipākaḥ_`
- **local SLM**: `sarva_sarva_Cp dhātu_dhātu_Cp gati_gati_Cp yoni_yoni_Cp jātiṣu_jāti_PLF kuśala_kuśala_Cp akuśala_akuśala_Cp karma_karman_Cp vipāka_vipāka_Cp tvāt_tva_SBNe vipākaḥ_vipāka_SNM`

## line 202

- **raw**: `asaṃviditakopādisthānavijñaptikañ ca tat`
- **2022**: `asaṃvidita-kopa-ādi-sthāna-vijñaptikan ca tat-`
- **API**: `ca_tat_`
- **local S**: `a_saṃvidita_kopa_ādi_sthāna_vijñaptikam_ca_tat_`
- **local SLM**: `a_a_ saṃvidita_saṃvid_PaCp kopa_kopa_Cp ādi_ādi_Cp sthāna_sthāna_Cp vijñaptikam_vijñaptika_SNNe ca_ca_ tat_tad_SNNe`

## line 1052

- **raw**: `manovijñānasaṃbhūtiḥ sarvadāsaṃjñikād ṛte`
- **2022**: `manaḥ-vijñāna-saṃbhūtiḥ sarvadā-saṃjñikāt ṛte`
- **API**: `manaḥ_vijñāna_saṃbhūtiḥ_sarvadā_āsaṃjñikāt_ṛte_`
- **local S**: `manaḥ_vijñāna_saṃbhūtiḥ_sarvadā_āsaṃjñikāt_ṛte_`
- **local SLM**: `manaḥ_manas_Cp vijñāna_vijñāna_Cp saṃbhūtiḥ_sambhūti_SNF sarvadā_sarvadā_ āsaṃjñikāt_āsaṃjñika_SBM ṛte_ṛte_`

