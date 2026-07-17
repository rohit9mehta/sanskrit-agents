# Triṃśikā v.28 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 12 pass / 0 fail / 0 unsupported.

## Verse

> **yadā tv ālambanaṃ jñānaṃ naivopalabhate tadā | sthitaṃ vijñaptimātratve grāhyābhābhāve tadagrahāt**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| yadā | yadā | indecl. | pass |
| tu | tu | indecl. | pass |
| ālambanam | ālambana | Napumsaka. Dvitiya/Eka | pass |
| jñānam | jñāna | Napumsaka. Prathama/Eka | pass |
| na | na | indecl. | pass |
| eva | eva | indecl. | pass |
| upalabhate | labh | upa-labh, Kartari/Lat/Prathama/Eka | pass |
| tadā | tadā | indecl. | pass |
| sthitam | sthita | Napumsaka. Prathama/Eka | pass |
| vijñaptimātratve | vijñaptimātratva | Napumsaka. Saptami/Eka; karmadharaya ⟨vijñaptir eva mātram; tasya bhāvaḥ vijñaptimātratvam⟩ | pass |
| grāhyābhābhāve | grāhyābhābhāva | Pum. Saptami/Eka; tatpurusa ⟨grāhyasya ābhā; tasyāḥ abhāvaḥ⟩ | pass |
| tadagrahāt | tadagraha | Pum. Panchami/Eka; tatpurusa ⟨tasya agrahaḥ⟩ | pass |

## Justifications

**J1. yadā and tadā are read as a matched temporal pair, with tu as an intervening contrastive particle.**
- chosen: Temporal-correlative construal: ‘when ... then ...’. (depends on commentary: no)
- trbh []: `MW s.v. yadā: ‘when, at what time, whenever (generally followed by the correlatives tadā...)’; MW s.v. tadā: ‘at that time, then ... correlative of yadā’.` — The grammar and lexicon support a ‘when ... then’ construction.

**J2. The clause is construed as ‘cognition does not apprehend an object-support’, not as ‘it does not apprehend knowledge’ or as a compound-like phrase.**
- chosen: jñānam is the nominative subject; ālambanam is the accusative object. (depends on commentary: no)
- trbh []: `MW s.v. upa-√labh: ‘to perceive, behold ... understand, learn, know’; MW s.v. ālambana: ‘depending on or resting upon ... supporting’; MW s.v. jñāna: ‘knowing ... knowledge’.` — upalabhate is semantically transitive; ālambanam is the natural object, while jñānam is the neuter nominative subject and is resumed by sthitam.

**J3. eva strengthens na rather than adding a separate assertion such as ‘indeed’.**
- chosen: na eva is rendered as emphatic negation, ‘does not ... at all’. (depends on commentary: no)
- trbh []: `MW s.v. na: ‘not, no’; MW s.v. eva: ‘strengthening the idea expressed by any word ... just, exactly, only, even, alone, merely’.` — In the fused form naivopalabhate, eva intensifies the negative predication.

**J4. The word is parsed as locative singular of vijñapti-mātra-tva, not normalized to the vulgate vijñāna-mātratve.**
- chosen: vijñaptimātratve means ‘in representation-only-ness’ / ‘in the state of mere vijñapti’. (depends on commentary: no)
- trbh []: `The supplied bhāṣya reading has vijñaptimātratve; MW s.v. vijñapti: ‘information, report ...’; MW s.v. mātra: ‘ifc. measure, quantity’; -tva forms an abstract state.` — Grammatically this is the state or condition of being ‘vijñapti-mātra’. In Yogācāra context I render vijñapti as ‘representation’ while retaining the Sanskrit.

**J5. The bhāṣya reading is parsed as grāhya-ābhā-abhāva, a nested tatpuruṣa, rather than as simple grāhyābhāva ‘absence of the graspable’.**
- chosen: grāhyābhābhāve is ‘in the absence of the appearance of the graspable/object’. (depends on commentary: no)
- trbh []: `grāhya + ābhā + abhāve gives grāhyābhābhāve by internal sandhi; MW s.v. grāhya: ‘to be seized or taken’; MW s.v. ābhā: ‘splendour, light’; MW s.v. abhāva: ‘nonexistence, nullity, absence’.` — The extra ābhā in the supplied reading makes the absent item an ‘appearance’ of the grāhya, not simply the grāhya itself.

**J6. tadagrahāt is analysed as a tatpuruṣa tasya agrahaḥ in the ablative singular, giving the reason for sthitam vijñaptimātratve.**
- chosen: tadagrahāt is a causal ablative: ‘because of non-grasping of that’. (depends on commentary: no)
- trbh []: `MW s.v. tad: ‘it, that’; MW s.v. agraha: ‘non-acceptance’; the ending -āt marks ablative singular.` — The transparent compound and ablative case support a causal construal, ‘because of the non-grasping/non-apprehension of that’.

## Translation

> When, however, cognition (jñāna)
does not apprehend an object-support (ālambana) at all,
then it is established in representation-only-ness (vijñaptimātratva):
for, when the graspable-object appearance is absent,
there is non-grasping of that.

## Analyzer disagreements

- jñānam: ByT5 gives jñāna_SANe, apparently accusative/neuter singular. I choose Prathama Eka because jñānam supplies the subject of upalabhate, while ālambanam is the accusative object; sthitam also agrees with jñānam as a predicate. If SANe was intended as nom./acc. ambiguity, this is a disambiguation rather than a substantive disagreement.
- sthitam: ByT5 lemmatizes the form to √sthā. For the requested subanta analysis I give the inflected nominal stem sthita, Napumsaka Prathama Eka, while noting its derivation from √sthā.
- upalabhate: ByT5 effectively treats upalabh as the lemma. Per instruction, I separate the bare root labh from the prefix upa.
- vijñaptimātratve and tadagrahāt: ByT5 splits the compounds to final members tva and agraha. Per instruction, I give the whole inflected compound stems vijñaptimātratva and tadagraha.

## One-shot delta

- A commentary-blind or variant-normalizing translation could easily replace the supplied bhāṣya reading vijñaptimātratve with the vulgate vijñānamātratve and thereby shift the technical term from vijñapti to vijñāna.
- It could miss the extra ābhā in grāhyābhābhāve and translate merely ‘in the absence of the object’ rather than ‘in the absence of the object-appearance’.
- It could take both ālambanam and jñānam as accusatives, yielding an awkward ‘does not apprehend object-support knowledge’, rather than taking jñānam as the subject and ālambanam as the object.

## Open questions

- No commentary span was supplied in this ablation run; the exact antecedent intended by tad in tadagrahāt cannot be fixed beyond the grammatical ‘that’.
- The English rendering ‘representation’ for vijñapti is contextually Yogācāra, but the supplied MW entry alone would also allow more general renderings such as ‘notification’ or ‘information’.
