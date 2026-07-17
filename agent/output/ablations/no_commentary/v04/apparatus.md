# Triṃśikā v.4 — commentary-grounded translation with apparatus

Pipeline run — reasoner: `gpt-5.5-2026-04-23`, attempts: 1, verification: 13 pass / 0 fail / 0 unsupported.

## Verse

> **upekṣā vedanā tatrānivṛtāvyākṛtañ ca tat tathā sparśādayaḥ tac ca vartate srotasaughavat**

## Word-by-word analysis

| surface | lemma | morphology | vidyut |
|---|---|---|---|
| upekṣā | upekṣā | Stri. Prathama/Eka | pass |
| vedanā | vedanā | Stri. Prathama/Eka | pass |
| tatra | tatra | indecl. | pass |
| anivṛtāvyākṛtam | anivṛtāvyākṛta | Napumsaka. Prathama/Eka; karmadharaya ⟨anivṛtam avyākṛtam⟩ | pass |
| ca | ca | indecl. | pass |
| tat | tad | Napumsaka. Prathama/Eka | pass |
| tathā | tathā | indecl. | pass |
| sparśādayaḥ | sparśādi | Pum. Prathama/Bahu; bahuvrihi ⟨sparśa ādir yeṣāṃ te⟩ | pass |
| tat | tad | Napumsaka. Prathama/Eka | pass |
| ca | ca | indecl. | pass |
| vartate | vṛt | vṛt, Kartari/Lat/Prathama/Eka | pass |
| srotasā | srotas | Napumsaka. Trtiya/Eka | pass |
| oghavat | oghavat | Napumsaka. Prathama/Eka | pass |

## Justifications

**J1. Construe the two feminine nominative singulars predicatively rather than as a single compound or as two coordinated subjects.**
- chosen: upekṣā is a predicate nominative and vedanā the subject: “the feeling is equanimity.” (depends on commentary: no)
- trbh []: `upekṣā vedanā tatra` — Both upekṣā and vedanā are feminine nominative singular; with no overt verb, the natural construal is an implied copula: “there, feeling is equanimity.”

**J2. Read anivṛta + avyākṛta as a compound meaning “unobstructed/uncovered and indeterminate/neutral,” not as anivṛtā feminine plus avyākṛtam neuter.**
- chosen: anivṛtāvyākṛtam is one neuter singular karmadhāraya compound agreeing with tat. (depends on commentary: no)
- trbh []: `tatrānivṛtāvyākṛtañ ca tat` — The final -ñ before ca points to an underlying neuter -am; the following tat is neuter nominative singular, supporting agreement with anivṛtāvyākṛtam.

**J3. The plural sparśādayaḥ is elliptical with tathā; it is not made into a kind of vedanā, since sparśa ‘contact’ is distinct from feeling.**
- chosen: tathā makes sparśādayaḥ inherit the immediately preceding qualification: “contact and the rest are likewise [unobstructed-indeterminate].” (depends on commentary: no)
- trbh []: `anivṛtāvyākṛtañ ca tat tathā sparśādayaḥ` — The adverb tathā follows the predication anivṛtāvyākṛtam ca tat and precedes sparśādayaḥ, so it most naturally carries that predication forward: “so too contact and the rest.”

**J4. Because sparśādayaḥ is masculine plural, neuter singular tac cannot grammatically refer to it as its subject; vartate is singular.**
- chosen: The second tac is neuter singular subject of vartate, referring to the same singular ‘that,’ not to sparśādayaḥ. (depends on commentary: no)
- trbh []: `sparśādayaḥ tac ca vartate` — The pronoun tac and the verb vartate are singular; sparśādayaḥ is plural. Hence tac ca vartate must resume a neuter singular antecedent.

**J5. Translate the phrase idiomatically as a current/torrent simile while retaining the grammatical split: instrumental srotasā plus neuter oghavat.**
- chosen: srotasaughavat is resolved as srotasā oghavat in this ablation, following the analyzer and regular ā + o → au sandhi. (depends on commentary: no)
- trbh []: `vartate srotasaughavat` — The printed au is directly explained by srotasā + oghavat. Thus the words can be read as “it continues, flood-like/torrential, with a current.”

## Translation

> There, feeling (vedanā) is equanimity (upekṣā);
and that is unobstructed–indeterminate (anivṛtāvyākṛta).
Contact and the rest (sparśādayaḥ) are likewise;
and that goes on, flood-like, with a current.

## Analyzer disagreements

- The api_seg output inserts ca after vedanā and omits tatra; I follow the supplied verse and the local_S segmentation, reading vedanā tatra, not vedanā ca.
- ByT5 separates anivṛtā and avyākṛtam; I analyze anivṛtāvyākṛtam as a single neuter nominative singular karmadhāraya compound agreeing with tat. The split feminine anivṛtā would not construe with neuter tat/avyākṛtam.
- ByT5 represents sparśādayaḥ as sparśa_Cp + ādayaḥ; I record the same analysis as the inflected compound stem sparśādi, since the verse has the single compound form sparśādayaḥ.

## One-shot delta

- Without commentary, the antecedent of tat remains inferred only from grammar and the preceding context not supplied here; a blind translation could wrongly attach tac ca vartate to the plural sparśādayaḥ.
- A dictionary-only reading could take upekṣā as mere ‘neglect/indifference’ rather than the technical affective tone ‘equanimity.’
- The scope of tathā is uncertain without commentary; grammar favors carrying forward anivṛtāvyākṛtam to sparśādayaḥ, but a blind reading might instead connect it with upekṣā vedanā.
- The final simile is especially vulnerable: the analyzer-supported split srotasā oghavat is phonologically regular, while many interpretive translations may prefer the compound-like idiom “like a stream-current.”

## Open questions

- No commentary was supplied in this ablation, so the exact scholastic force of anivṛta and avyākṛta cannot be confirmed from trbh evidence.
- The singular antecedent of tat is grammatically clear as neuter singular, but its doctrinal referent depends on the preceding verse/context not included in the ablation data.
- Whether srotasaughavat should ultimately be read as the sandhi of srotasā oghavat or as an idiomatized compound-like simile needs commentary or manuscript evidence beyond the ablation instructions.
