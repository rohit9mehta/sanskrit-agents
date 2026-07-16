# Phase 1 comparison: commentary-grounded agent vs baselines

- **agent**: pipeline reasoner `gpt-5.5-2026-04-23` + ByT5 analyses + bhāṣya span retrieval + MW + vidyut verification loop
- **raw-LLM**: same model, verse text only (gpt-5.5-2026-04-23)
- **MITRA**: https://dharmamitra.org/api-search/cat-translate/v1/translate (style: balanced)
- **human**: Dharmavardhana Jñānagarbha (Mattia Salvini) — *Ācārya Vasubandhu's Thirty Verses (Triṁśikā): A Manual for S...*, June 2022, 9–19 (Translation of the Thirty Verses) (web-sourced, transcribed from page images; translates the vulgate text)

## Aggregate

| metric | value |
|---|---|
| verses completed | 30/30 |
| word-claims pass / fail / unsupported / tool_error | 328 / 0 / 5 / 0 |
| verses needing a verify-feedback retry | 9 |
| justification objects (commentary-dependent) | 184 (182) |
| analyzer overrides recorded | 107 |
| tokens (prompt / completion / reasoning) | 302490 / 524135 / 369461 |
| estimated pipeline cost | $8.77 |

---

## v.1

*verification: 11 pass / 0 fail / 0 unsupported*

**agent** — For, in world and śāstra, the manifold figurative imputation (upacāra) of self (ātman) and dharmas (dharma) that is current—
this is upon the transformation of consciousness (vijñāna-pariṇāma);
and that transformation (pariṇāma) is threefold.

**raw-LLM** — Indeed, the manifold conventional designation of self and dharmas that arises occurs in the transformation of consciousness; and that transformation is threefold.

**MITRA** — The various metaphorical designations of "self" and "phenomena" that arise do so within the transformation of consciousness, and that transformation is threefold.

**human (Salvini 2022)** — The manifold approximation, such as "self" and "dharmas", that goes on, refers to the transformation of consciousness, and that transformation is threefold:

commentary-grounded decisions: J1 (C; trbh [[25]]); J2 (C; trbh [[28, 29, 30], [49, 50, 51, 52, 53]]); J3 (C; trbh [[31, 32], [33, 34, 35], [36]]); J4 (C; trbh [[26, 27], [36, 37, 38], [55, 56]]); J5 (C; trbh [[39, 40, 41, 42, 43], [61, 62, 63]]); J6 (C; trbh [[149, 150, 151, 152], [153, 154], [164]]); J7 (C; trbh [[98, 99], [147, 148]])

## v.2

*verification: 11 pass / 0 fail / 0 unsupported*

**agent** — The transformation is threefold:
maturation-result (vipāka), the one called mentation (manana),
and presentation of an object (viṣaya-vijñapti).
Among these, the consciousness called the storehouse (ālaya)
is the maturation-result, all-seeded (sarvabījaka).

**raw-LLM** — It is maturation, that called mentation, and the representation of objects; among these, the consciousness called the storehouse is maturation, containing all seeds.

**MITRA** — [The three transformations of consciousness are] maturation, that which is called mentation, and the representation of objects. Among these, the consciousness known as the *ālaya* (storehouse) is the maturation, which contains all seeds.

**human (Salvini 2022)** — maturation; the one called "thinking"; and the cognition of a domain. Among these, the consciousness called ālaya is the maturation, and contains all the seeds.

commentary-grounded decisions: J1 (C; trbh [[169]]); J2 (C; trbh [[170, 171], [188]]); J3 (C; trbh [[172]]); J4 (C; trbh [[173, 174]]); J5 (C; trbh [[179, 180, 181]]); J6 (C; trbh [[183, 184], [185, 186]]); J7 (C; trbh [[187]]); J8 (C; trbh [[189]])

## v.3

*verification: 5 pass / 0 fail / 0 unsupported*

**agent** — And that storehouse consciousness (ālayavijñāna)
has unapprehended appropriation (upādi)
and an unapprehended place-presentation (sthānavijñapti);
for as long as it is, it is accompanied
by contact (sparśa), attention (manaskāra), feeling (vedanā),
recognition (saṃjñā), and volition (cetanā).

**raw-LLM** — It has an unperceived representation of appropriation and place, and is always accompanied by contact, attention, feeling, perception, and volition.

**MITRA** — It is characterized by representations of the environment and of appropriation that are not consciously perceived, and it is always accompanied by contact, attention, feeling, perception, and volition.

**human (Salvini 2022)** — In it, clinging, and the cognition of a locus, are not cognized; it is always accompanied by contact, mental placement, feeling, notion and intention.

commentary-grounded decisions: J1 (C; trbh [[203, 204]]); J2 (C; trbh [[205, 206, 207, 208], [212, 213, 214]]); J3 (C; trbh [[210, 211], [220, 221], [223, 224]]); J4 (C; trbh [[222], [223, 224]]); J5 (C; trbh [[203, 204], [231, 232, 233, 234, 235, 236, 237]]); J6 (C; trbh [[239, 240, 241], [497, 498, 499, 500]]); J7 (C; trbh [[242], [302, 303], [268, 269, 270, 271, 272, 273, 274]]); J8 (C; trbh [[243, 244, 245, 246, 247, 248, 249], [258, 259, 260, 261, 262, 263, 264], [291, 292, 293, 294, 295, 296], [297, 298]])

## v.4

*verification: 13 pass / 0 fail / 0 unsupported*

**agent** — There, in the store-consciousness (ālayavijñāna),
the feeling (vedanā) is equanimity (upekṣā);
and that [store-consciousness] is unobscured-indeterminate (anivṛtāvyākṛta).
Contact and the rest (sparśādayaḥ) are likewise;
and this [store-consciousness] goes on, in a stream-continuum (srotas), like a flood (ogha).

**raw-LLM** — In it, feeling is neutral; it is unobscured and morally indeterminate, and so too are contact and the other mental factors. It flows on like a current.

**MITRA** — In that state, the feeling is equanimity, which is both unobscured and morally indeterminate; mental contact and the other associated factors are likewise. Its continuity proceeds like the current of a flowing stream.

**human (Salvini 2022)** — In it, feeling is neutral. It is unobstructed and undetermined, and so are contact, etc.; it goes on in a flow, like a stream.

commentary-grounded decisions: J1 (C; trbh [[308]]); J2 (C; trbh [[309, 310, 311]]); J3 (C; trbh [[312, 313], [314, 315, 316, 317, 318]]); J4 (C; trbh [[319, 320, 321, 322, 323, 324, 325], [326, 327]]); J5 (C; trbh [[330, 331, 332, 333, 334, 335]]); J6 (C; trbh [[336, 337, 338, 339], [340, 341, 342]])

## v.5

*verification: 10 pass / 0 fail / 0 unsupported*

**agent** — Its cessation is in arhatship (arhattva).
Relying on that—the storehouse consciousness (ālayavijñāna)—it proceeds.
Having that as its object-support (ālambana),
it is a consciousness (vijñāna) named mind (manas),
whose nature is cogitation (manana).

**raw-LLM** — It ceases in the state of arhatship. Depending on it and taking it as its object, there arises the consciousness called manas, whose nature is mentation.

**MITRA** — Its cessation occurs at the stage of the arhat. Depending upon that [store-consciousness] as its support and taking it as its object, there functions the consciousness known as *manas*, which is characterized by the nature of mentation.

**human (Salvini 2022)** — Its cessation comes about at the state of an Arhat; on its basis, there comes forth a consciousness called "thought", having the former as its support, and having the nature of thinking;

commentary-grounded decisions: J1 (C; trbh [[345, 346, 349, 350, 351, 352]]); J2 (C; trbh [[363, 364, 365], [366, 367, 368]]); J3 (C; trbh [[369, 370], [371, 372, 373, 374]]); J4 (C; trbh [[375, 376, 377]]); J5 (C; trbh [[378, 379, 381, 382]]); J6 (C; trbh [[353, 354], [357, 358, 359, 360], [375, 376, 377]])

## v.6

*verification: 6 pass / 0 fail / 0 unsupported*

**agent** — Always, so long as it exists, this [mind (manas)]
is conjoined (saṃprayukta) with four obscured-neutral afflictions
(kleśa; nivṛtāvyākṛta):
those called self-view (ātmadṛṣṭi), delusion about self (ātmamoha),
self-conceit (ātmamāna), and self-love/attachment (ātmasneha).

**raw-LLM** — It is always accompanied by four afflictions, obscured and indeterminate: self-view, self-delusion, self-conceit, and self-love.

**MITRA** — It is always accompanied by four afflictions that are obscured and morally indeterminate, known as the view of self, the delusion of self, the pride of self, and the love of self.

**human (Salvini 2022)** — it is always accompanied by four afflictions, obscured and undetermined, called: view of self, delusion of self, presumption of self, affection towards the self.

commentary-grounded decisions: J1 (C; trbh [[417, 418, 419]]); J2 (C; trbh [[386, 387, 388]]); J3 (C; trbh [[389, 390]]); J4 (C; trbh [[391], [401]]); J5 (C; trbh [[392, 393, 394, 395], [396, 397, 398]]); J6 (C; trbh [[399, 400, 401]]); J7 (C; trbh [[402, 403], [404, 405, 406, 407, 408, 409, 410]]); J8 (C; trbh [[411, 412, 413, 414, 415, 416]])

## v.7

*verification: 11 pass / 0 fail / 0 unsupported*

**agent** — Wherever it is born, it is associated only with factors of that same realm (dhātu) and level (bhūmi);
for an arhat, that defiled mind (kliṣṭaṃ manas) is not.
Nor is it present in cessation-attainment (nirodha-samāpatti),
nor on the supramundane path (lokottara-mārga).

**raw-LLM** — Arising on whatever plane, it is accompanied by factors belonging to that plane; it is not present in the arhat, nor in the attainment of cessation, nor on the supramundane path.

**MITRA** — Wherever it arises, it is conjoined with factors of the same nature, such as contact; yet it does not exist in the Arhat, nor in the attainment of cessation (*nirodhasamāpatti*), nor in the supramundane path (*lokottaramārga*). (Some versions omit the initial clause regarding birth and contact, focusing exclusively on the absence of the afflicted *manas* in these three states.)

**human (Salvini 2022)** — Wherever one is born, they correspond to that level; it also has others, contact, etc.; it does not exist for an Arhat, nor during the absorption of cessation, nor in the supramundane path:

commentary-grounded decisions: J1 (C; trbh [[427], [428]]); J2 (C; trbh [[428, 429, 430, 431], [441, 442]]); J3 (C; trbh [[432, 433, 434, 435, 436, 437, 438], [443, 444, 445, 446]]); J4 (C; trbh [[447, 448, 449, 450, 451, 452, 453, 454], [456, 457, 458]]); J5 (C; trbh [[459, 460, 461, 462]]); J6 (C; trbh [[463, 464, 465, 466], [467, 468, 469, 470]])

## v.8

*verification: 12 pass / 0 fail / 0 unsupported*

**agent** — This is the second transformation (pariṇāma).
The third consciousness-transformation (vijñāna-pariṇāma)
is whatever apprehension (upalabdhi) there is
of the sixfold object (viṣaya):
that is wholesome (kuśala), unwholesome (akuśala),
or neither—the undetermined (advayā/avyākṛta).

**raw-LLM** — This is the second transformation. The third is the apprehension of the sixfold object; it is wholesome, unwholesome, or neither.

**MITRA** — This is the third transformation of consciousness, which consists of the perception of six kinds of objects; it may be wholesome, unwholesome, or indeterminate.

**human (Salvini 2022)** — this is the second transformation. The third is the perception of the sixfold domain, and it can be virtuous, non-virtuous, or neither.

commentary-grounded decisions: J1 (C; trbh [[473, 474], [475, 476, 477]]); J2 (C; trbh [[478, 479]]); J3 (C; trbh [[479, 480]]); J4 (C; trbh [[475, 476, 481]]); J5 (C; trbh [[481, 482, 483], [484, 485, 486, 487]])

## v.9

*verification: 10 pass / 0 fail / 0 unsupported*

**agent** — With universal (sarvatraga), determinate (viniyata),
and wholesome mental factors (caitasa), this [apprehension] is conjoined;
likewise with afflictions (kleśa) and secondary afflictions (upakleśa):
it has three feelings (tri-vedanā).

**raw-LLM** — It is associated with the omnipresent, the determinate, and the wholesome mental factors, as well as with the afflictions and secondary afflictions, and it has the three kinds of feeling.

**MITRA** — It is associated with the omnipresent, the object-determined, and the wholesome mental factors, as well as with the primary and secondary afflictions, and it is accompanied by the three types of feeling.

**human (Salvini 2022)** — It is joined by the omnipresent mental states; by those of delimited occurrence; by virtuous ones; by afflictions; and by secondary afflictions. It has three types of feeling.

commentary-grounded decisions: J1 (C; trbh [[493]]); J2 (C; trbh [[491, 492], [493]]); J3 (–; trbh [[491, 492]]); J4 (–; trbh [[492]])

## v.10

*verification: 10 pass / 0 fail / 0 unsupported*

**agent** — The initial ones (ādyāḥ)—those beginning with contact (sparśa)—are the omnipresent (sarvatraga);
desire (chanda), resolve (adhimokṣa), and mindfulness (smṛti),
together with concentration (samādhi) and discernment (dhī/prajñā), are the object-specific determinate factors (niyata/viniyata);
then come faith (śraddhā), shame (hrī), and compunction (apatrapā).

**raw-LLM** — The first are contact and the rest; desire, resolve, and mindfulness, together with concentration and discernment, are the specific ones; then come faith, shame, and moral scruple.

**MITRA** — The first [group of mental factors] consists of contact and the rest. The specific factors are desire, resolve, and mindfulness, together with concentration and wisdom. Then follow the wholesome factors: faith, conscience, and a sense of shame.

**human (Salvini 2022)** — The first are contact, etc. Zest, conviction and mindfulness, plus samādhi and wisdom, are the delimited; faith, modesty, shame,

commentary-grounded decisions: J1 (C; trbh [[496], [498, 499]]); J2 (C; trbh [[500], [501, 502], [503, 504]]); J3 (C; trbh [[505, 506, 507], [568, 569, 570, 571]]); J4 (C; trbh [[508, 509], [572]]); J5 (C; trbh [[510], [515], [517], [524, 525], [529], [533, 534], [538, 539, 540, 541], [545, 546, 547, 548, 549, 550]]); J6 (C; trbh [[572, 573, 574]])

## v.11

*verification: 8 pass / 0 fail / 0 unsupported*

**agent** — The triad beginning with non-greed (alobha)—non-greed, non-hatred (adveṣa), non-delusion (amoha)—energy in the wholesome (vīrya), pliancy (praśrabdhi), equanimity (upekṣā) together with heedfulness (apramāda), and non-harming (ahiṃsā, glossed avihiṃsā): these complete the wholesome factors (kuśala). The afflictions (kleśa) are attachment (rāga), aversion (pratigha), and delusion (mūḍhi).

**raw-LLM** — Non-greed, non-hatred, and non-delusion, energy, pliancy, heedfulness, and non-harming are wholesome; the afflictions are attachment, aversion, and delusion.

**MITRA** — The triad beginning with non-greed, along with vigor, serenity, heedfulness, and non-violence, constitute the wholesome factors; the afflictions are attachment, aversion, and delusion.

**human (Salvini 2022)** — the three starting from non-greed, heroism, ease, that which comes with non-heedlessness, and non-harming, are the virtuous. The afflictions are attraction, aversion and delusion,

commentary-grounded decisions: J1 (C; trbh [[577], [679]]); J2 (C; trbh [[601, 602, 603, 604, 605], [607, 608, 609, 610, 611], [613, 614, 615, 616, 617]]); J3 (C; trbh [[619, 620, 621, 622, 623, 624]]); J4 (C; trbh [[625, 626, 627, 628, 629, 630, 631, 632, 633]]); J5 (C; trbh [[638, 639, 640, 641, 642, 643, 644, 645], [646, 647, 648, 649, 650], [654]]); J6 (C; trbh [[670, 671, 672, 673, 674, 675, 676, 677, 678]]); J7 (C; trbh [[679, 680, 681]])

## v.12

*verification: 9 pass / 0 fail / 0 unsupported*

**agent** — Conceit (māna), the afflictive views (dṛg), and doubt (vicikitsā);
concealment (mrakṣa), spite (pradāśa), envy (īrṣyā)—then
stinginess (mātsarya), together with deceit (māyā).

**raw-LLM** — Conceit, wrong views, and doubt; concealment, spite, jealousy, then stinginess, together with deceit.

**MITRA** — Pride, wrong views, and doubt, along with concealment, spite, jealousy, and avarice, together with deceit. (Note: While the Sanskrit source provided focuses on the latter list, the broader canonical context often includes anger and hostility as preceding elements in this sequence of secondary afflictions.)

**human (Salvini 2022)** — presumption, view, doubt. Furthermore, anger and grudge, dissimulation, biting, envy, stinginess, illusionism,

commentary-grounded decisions: J1 (C; trbh [[715], [752], [767, 768], [772]]); J2 (C; trbh [[716, 717, 718, 719, 720, 721]]); J3 (C; trbh [[752, 753, 754]]); J4 (C; trbh [[767, 768, 769, 770, 771]]); J5 (C; trbh [[774]]); J6 (C; trbh [[772], [774]])

## v.13

*verification: 13 pass / 0 fail / 0 unsupported*

**agent** — Deceitful crookedness (śāṭhya), self-intoxicated pride (mada), harmfulness (vihiṃsā);
shamelessness in oneself (ahrī/āhrīkya), no compunction before others (atrapā/anapatrāpya), torpor (styāna), restlessness (auddhatya);
then faithlessness (āśraddhya), sloth (kausīdya), heedlessness (pramāda),
and corrupted mindfulness—afflicted mindfulness (muṣitā smṛtiḥ).

**raw-LLM** — Deceit, vanity, cruelty, shamelessness, lack of moral restraint, torpor, agitation, faithlessness, laziness, heedlessness, and forgetfulness.

**MITRA** — Deception, intoxication, harmfulness (some versions read *ahrī* and *anapatrāpya* as distinct qualities of shamelessness and lack of moral dread), shamelessness, lack of moral dread, lethargy, restlessness, lack of faith, indolence, heedlessness, and lapsed mindfulness.

**human (Salvini 2022)** — deceitfulness, intoxication, harming, non-modesty, non-shame, sloth, excitement, non-faith, laziness, heedlessness, deceived mindfulness,

commentary-grounded decisions: J1 (C; trbh [[841, 842, 843, 844, 845], [849, 850, 851, 852, 853]]); J2 (C; trbh [[856, 857, 858, 859, 860, 861, 862]]); J3 (C; trbh [[863, 864, 865, 866, 867, 868, 869]]); J4 (C; trbh [[870, 871, 872], [873, 874, 875, 876]]); J5 (C; trbh [[881, 882, 883, 884, 885, 886, 887]]); J6 (C; trbh [[888, 889, 890, 891]]); J7 (C; trbh [[892, 893, 894, 895, 896, 897, 898, 899]]); J8 (C; trbh [[900, 901, 902, 903, 904]]); J9 (C; trbh [[905, 906, 907, 908, 909, 910]]); J10 (C; trbh [[911, 912, 913, 914]])

## v.14

*verification: 15 pass / 0 fail / 0 unsupported*

**agent** — Distraction (vikṣepa), lack of clear comprehension (asaṃprajanya),
regret (kaukṛtya), and torpor (middha) too;
searching inner speech (vitarka) and examining inner speech (vicāra):
secondary afflictions (upakleśa).
The two dyads—regret/torpor and searching/examining—are twofold;
only their defiled forms count as such.

**raw-LLM** — Distraction, lack of clear awareness, remorse, drowsiness, initial thought, and examination—these are secondary afflictions; the two pairs are twofold.

**MITRA** — Distraction, lack of introspection, regret, drowsiness, as well as initial thought and sustained thought—these are the secondary afflictions, the latter two of which are of two kinds (some traditions classify these as indeterminate, whereas others categorize them strictly as secondary afflictions).

**human (Salvini 2022)** — scatteredness, lack of discerning awareness, what derives from bad deeds, torpor, deliberation and analysis, are the secondary afflictions. The two pairs are twofold.

commentary-grounded decisions: J1 (C; trbh [[915, 916, 917, 918, 919, 920]]); J2 (C; trbh [[921, 922, 923, 924]]); J3 (C; trbh [[925, 926, 927, 928, 929, 930], [971, 972, 973]]); J4 (C; trbh [[931, 932, 933, 934, 935, 936, 937, 938, 939]]); J5 (C; trbh [[940, 941, 942, 943, 944, 945, 946], [954, 955, 956, 957, 958, 959, 960, 961, 962]]); J6 (C; trbh [[966, 967, 968, 969, 970]]); J7 (C; trbh [[976, 977, 978, 979, 980, 981]])

## v.15

*verification: 10 pass / 0 fail / 1 unsupported*

**agent** — Based in the root consciousness (mūlavijñāna, the ālayavijñāna),
the five consciousnesses (vijñāna)—eye and the rest, with attendant mind-consciousness (manovijñāna)—
come into being (udbhava) according to the condition present (yathāpratyayam):
together, or not together,
as waves [arise] in water.

**raw-LLM** — The five consciousnesses arise in the root consciousness according to conditions, together or separately, like waves in water.

**MITRA** — The five consciousnesses arise from the root consciousness according to their respective conditions; they may manifest either simultaneously or separately, just as waves arise upon the water.

**human (Salvini 2022)** — The arising of the five consciosunesses [sic] in the root consciousness is according to conditions; it may occur together or not, just like the arising of waves on water.

commentary-grounded decisions: J1 (C; trbh [[1010], [1033, 1034]]); J2 (C; trbh [[1012, 1013], [1030, 1031]]); J3 (C; trbh [[1014, 1015]]); J4 (C; trbh [[1016, 1017], [1018, 1019]]); J5 (C; trbh [[1021, 1022, 1023, 1024, 1025, 1026], [1030, 1031, 1032, 1033, 1034]]); J6 (C; trbh [[1039, 1040, 1041, 1042], [1047]])

## v.16

*verification: 9 pass / 0 fail / 0 unsupported*

**agent** — The arising of mental consciousness (manovijñāna)
is at all times—whether with the eye-consciousnesses and the rest, or without them—
except in the unconscious state (āsaṃjñika),
in the two attainments (samāpatti-dvaya),
in mindless torpor (acittaka middha),
and also in mindless fainting (mūrcchā).

**raw-LLM** — Mental consciousness arises at all times, except among the non-percipient beings, in the two meditative attainments, in deep sleep, in fainting, and in other mindless states.

**MITRA** — The mental consciousness arises at all times, except in the state of non-perception, the two meditative attainments, deep sleep (or torpor), and fainting, which are devoid of thought.

**human (Salvini 2022)** — The thought-consciousness always comes about, except for: the notionless, the two attainments, mind-less torpor and swoon.

commentary-grounded decisions: J1 (C; trbh [[1081, 1082], [1083, 1084, 1085, 1086]]); J2 (C; trbh [[1055]]); J3 (C; trbh [[1056, 1057, 1058], [1081, 1082]]); J4 (C; trbh [[1059, 1060]]); J5 (C; trbh [[1061], [1064, 1065], [1072, 1073, 1074]]); J6 (C; trbh [[1075, 1076]]); J7 (C; trbh [[1077, 1078, 1079, 1080]])

## v.17

*verification: 13 pass / 0 fail / 0 unsupported*

**agent** — This transformation of consciousness (vijñānapariṇāma) is conceptual construction (vikalpa):
whatever object is imagined by it—that is not there.
Therefore all this is representation-only (vijñaptimātraka),
‘all’ meaning the three realms and the unconditioned.

**raw-LLM** — This transformation of consciousness is conceptual construction; what is constructed by it does not exist. Therefore all this is mere representation.

**MITRA** — This transformation of consciousness is conceptual construction, and that which is constructed by it does not exist. Therefore, all of this is representation-only.

**human (Salvini 2022)** — This transformation of consciousness is a concept. What is conceptualized by it, does not exist: therefore, all of this is cognition-only.

commentary-grounded decisions: J1 (C; trbh [[1096], [1100]]); J2 (C; trbh [[1097, 1098, 1099]]); J3 (C; trbh [[1100, 1101, 1102], [1125, 1126]]); J4 (C; trbh [[1103], [1108, 1109, 1110, 1111, 1112, 1113, 1114], [1119, 1120]]); J5 (C; trbh [[1121, 1122, 1123, 1124, 1125, 1126]]); J6 (C; trbh [[1127, 1128, 1129, 1130, 1131]])

## v.18

*verification: 13 pass / 0 fail / 0 unsupported*

**agent** — For consciousness—store-consciousness (ālayavijñāna)—is all-seeded (sarvabīja):
by mutual influence its transformation (pariṇāma)
reaches such-and-such states,
and thereby this or that construction (vikalpa) arises.

**raw-LLM** — For consciousness contains all seeds; its transformation proceeds in various ways through mutual influence, and from this arises this or that conceptual construction.

**MITRA** — Consciousness contains all seeds, and its transformation proceeds in various ways through mutual influence, whereby such and such conceptual constructions arise.

**human (Salvini 2022)** — The consciousness which contains all the seeds reaches manyfold ways of transformation, due to mutual influence; due to this, the concept arises in manyfold ways.

commentary-grounded decisions: J1 (C; trbh [[1136], [1137, 1138, 1139], [1140, 1141]]); J2 (C; trbh [[1142, 1143, 1144, 1145]]); J3 (C; trbh [[1146, 1147, 1148, 1149, 1150, 1151]]); J4 (C; trbh [[1150, 1151, 1152], [1153, 1154]])

## v.19

*verification: 10 pass / 0 fail / 0 unsupported*

**agent** — The karmic impressions (karmavāsanāḥ), together with the impression of the twofold grasping (grāhadvayavāsanā),
when the previous maturation (pūrvavipāka) has been exhausted,
generate that—ālaya-consciousness (ālayavijñāna)—as another maturation (vipāka).

**raw-LLM** — The latent impressions of karma, together with the impressions of the twofold grasping, generate another maturation when the previous maturation has been exhausted.

**MITRA** — The habit-energies (*vāsanā*) of actions, together with the habit-energies of twofold grasping, generate a subsequent maturation once the previous maturation has been exhausted.

**human (Salvini 2022)** — The perfumings from karma, together with the imprint of two types of grasping, when the previous maturation has vanished produce another maturation.

commentary-grounded decisions: J1 (C; trbh [[1160, 1161, 1162], [1176, 1177], [1182, 1183]]); J2 (C; trbh [[1163], [1164, 1165, 1166, 1167], [1168, 1169], [1172, 1173, 1174], [1178, 1179]]); J3 (C; trbh [[1181, 1182], [1185, 1186, 1187]]); J4 (C; trbh [[1180], [1183, 1184], [1449, 1450, 1451]])

## v.20

*verification: 14 pass / 0 fail / 0 unsupported*

**agent** — By whatever conceptual construction (vikalpa),
whatever object is construed,
that nature (svabhāva) is just the imagined (parikalpita);
it is not found to exist.

**raw-LLM** — Whatever thing is imagined by whatever conceptual construction is only the imagined nature; it does not exist.

**MITRA** — Whatever object is conceptualized by whatever conceptual construction, that is merely the imagined nature; it does not exist.

**human (Salvini 2022)** — By whichever concept such and such a thing is conceptualized, that thing is only a thoroughly imagined own-existence: it does not exist.

commentary-grounded decisions: J1 (C; trbh [[1297, 1298, 1299, 1300]]); J2 (C; trbh [[1299, 1304]]); J3 (C; trbh [[1301, 1305, 1306, 1307], [1313]]); J4 (C; trbh [[1302, 1303, 1304], [1315]]); J5 (C; trbh [[1308, 1309, 1310, 1311, 1312, 1313]])

## v.21

*verification: 11 pass / 0 fail / 0 unsupported*

**agent** — But the dependent nature (paratantra-svabhāva)
is construction (vikalpa), born of conditions (pratyaya).
The perfected nature (pariniṣpanna-svabhāva) is
its always being devoid of the former—
the imagined grasper-and-grasped.

**raw-LLM** — The dependent nature, however, is conceptual construction arising from conditions; the perfected nature is its perpetual absence of the former.

**MITRA** — The dependent nature (*paratantra-svabhāva*) is conceptualization arising from conditions, while the perfected nature (*niṣpanna*) is that very state eternally devoid of the former (imagined) nature.

**human (Salvini 2022)** — The other-dependent own-existence, on the other hand, is the concept, arisen due to conditions. The accomplished is the latter's being always bereft of the former.

commentary-grounded decisions: J1 (C; trbh [[1320, 1321, 1322]]); J2 (C; trbh [[1323, 1324, 1325, 1326]]); J3 (C; trbh [[1327, 1328, 1329]]); J4 (C; trbh [[1331, 1332, 1333], [1340]]); J5 (C; trbh [[1334, 1335, 1336, 1337, 1338]]); J6 (C; trbh [[1339, 1340]])

## v.22

*verification: 14 pass / 0 fail / 2 unsupported*

**agent** — For just this reason, it is neither different
nor non-different from the other-dependent (paratantra);
as with impermanence and the rest, it is to be so stated.
When this perfected nature (pariniṣpanna) has not been seen,
that other-dependent nature is not seen.

**raw-LLM** — For this very reason, it is to be said to be neither different from nor identical with the dependent nature, like impermanence and the like; when this is not seen, that is not seen.

**MITRA** — Therefore, in relation to the dependent nature (*paratantra*), it is to be described as neither different nor non-different, much like the nature of impermanence and the like; for when the one is not perceived, the other is not perceived (some versions imply that when the dependent nature is not seen, the nature of reality is not seen).

**human (Salvini 2022)** — Precisely due to this, it is neither other nor not other than the other-dependent. It should be explained just like impermanence, etc. That is not seen as long as this is not seen.

commentary-grounded decisions: J1 (C; trbh [[1342, 1343, 1344, 1345, 1346, 1347, 1348]]); J2 (C; trbh [[1349, 1350, 1351, 1352, 1353, 1354, 1355]]); J3 (C; trbh [[1356, 1357], [1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365]]); J4 (C; trbh [[1366, 1367, 1368, 1369, 1370], [1371, 1372, 1373, 1374]]); J5 (C; trbh [[1375, 1376], [1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385]])

## v.23

*verification: 8 pass / 0 fail / 0 unsupported*

**agent** — Having in view the threefold absence of own-nature (niḥsvabhāvatā)
of the threefold own-nature (svabhāva),
the absence of own-nature of all dharmas (sarvadharmāḥ) was taught—
dharmas whose nature is imagined, dependent, and perfected.

**raw-LLM** — With reference to the threefold lack of intrinsic nature in the threefold nature, the lack of intrinsic nature of all phenomena was taught.

**MITRA** — With reference to the three kinds of intrinsic nature and their corresponding three kinds of non-self-nature, the non-self-nature of all phenomena has been taught.

**human (Salvini 2022)** — The lack of own-existence of all the dharmas was taught intending to refer to the threefold lack of own-existence of the threefold own-existence.

commentary-grounded decisions: J1 (C; trbh [[1391]]); J2 (C; trbh [[1392, 1393]]); J3 (C; trbh [[1394, 1395]]); J4 (C; trbh [[1396, 1397]]); J5 (C; trbh [[1394, 1395], [1396, 1397]])

## v.24

*verification: 12 pass / 0 fail / 0 unsupported*

**agent** — The first—the imagined nature (parikalpita-svabhāva)—is natureless (niḥsvabhāva)
by its defining-character (lakṣaṇa) alone.
The other—the dependent nature (paratantra-svabhāva)—again has no self-arising;
“there is no self-arising of this”: that is the other naturelessness (niḥsvabhāvatā).

**raw-LLM** — The first is without intrinsic nature by its very characteristic; the other, again, because it does not arise by itself—this is another absence of intrinsic nature.

**MITRA** — The first is natureless by its very characteristic; the second, moreover, lacks self-origination, which constitutes the other absence of intrinsic nature.

**human (Salvini 2022)** — The first has no own-existence just in terms of its defining trait; while for the next, it means that it has no coming into existence on its own accord. There is another type of own-existence-less-ness:

commentary-grounded decisions: J1 (C; trbh [[1403]]); J2 (C; trbh [[1404, 1405, 1406, 1407]]); J3 (C; trbh [[1408]]); J4 (C; trbh [[1409, 1410, 1411, 1412]])

## v.25

*verification: 13 pass / 0 fail / 0 unsupported*

**agent** — Since that [perfected nature (pariniṣpanna-svabhāva)] is the ultimate reality (paramārtha) of dharmas (dharma),
it too is suchness (tathatā);
for at every time it is just so—
that very suchness is representation-only-ness (vijñaptimātratā).

**raw-LLM** — It is the ultimate reality of all phenomena, and therefore it is also suchness; because it is such at all times, it is itself mere cognition.

**MITRA** — This is the ultimate reality of all phenomena; because it is so, it is also Suchness (*tathatā*). Since it remains thus at all times, it is itself the state of Consciousness-Only (*vijñaptimātratā*).

**human (Salvini 2022)** — due to being the ultimate of the dharmas; it is also thusness, being thus at all time; that itself is cognition-only-ness.

commentary-grounded decisions: J1 (C; trbh [[1414], [1415, 1416, 1417], [1418, 1419, 1420]]); J2 (C; trbh [[1418, 1419, 1420, 1421]]); J3 (C; trbh [[1426, 1427, 1428, 1429]]); J4 (C; trbh [[1430, 1431, 1432, 1433]]); J5 (C; trbh [[1434, 1435, 1436, 1437], [1444]])

## v.26

*verification: 10 pass / 0 fail / 0 unsupported*

**agent** — So long as the yogin’s consciousness (vijñāna) does not abide
in representation-only (vijñaptimātratva),
so long the latent seed (anuśaya) of the twofold grasping (grāhadvaya)—
grouting grasped object and grasper—does not cease.

**raw-LLM** — As long as consciousness does not abide in mere representation, the latent tendency toward the twofold grasping does not cease.

**MITRA** — As long as consciousness does not abide in the state of representation-only, the latent tendency toward the twofold grasping does not cease.

**human (Salvini 2022)** — As long as consciousness does not remain in cognition-only-ness, for that long the insidious growth of the two types of grasping does not cease.

commentary-grounded decisions: J1 (C; trbh [[1460, 1461, 1462]]); J2 (C; trbh [[1454, 1455], [1460]]); J3 (C; trbh [[1454, 1455], [1460, 1461]]); J4 (C; trbh [[1455, 1456, 1457], [1463, 1464]]); J5 (C; trbh [[1458, 1459], [1449, 1450, 1451]]); J6 (C; trbh [[1461, 1462], [1451]])

## v.27

*verification: 12 pass / 0 fail / 1 unsupported*

**agent** — For even as he apprehends—grasps and pictures—
“This is mere representation (vijñapti-mātra) alone,”
mentally setting some support (ālambana) before him,
he does not abide in that mere [representation] (tanmātra).

**raw-LLM** — Even while holding, “This is mere representation only,” one does not abide in that mere representation, for one still apprehends something set before oneself.

**MITRA** — Even if one perceives that "this is only cognitive representation," as long as one posits something as an object before oneself, one does not truly abide in the state of mere representation.

**human (Salvini 2022)** — Since by perceiving even that "this is only just cognition", one is placing something in front, one is not remaining in that only.

commentary-grounded decisions: J1 (C; trbh [[1472, 1473], [1474, 1475]]); J2 (C; trbh [[1476]]); J3 (C; trbh [[1477], [1481]]); J4 (C; trbh [[1477], [1478], [1479, 1480]]); J5 (C; trbh [[1473], [1480, 1481]]); J6 (C; trbh [[1474]])

## v.28

*verification: 12 pass / 0 fail / 0 unsupported*

**agent** — When cognition (jñāna), however, does not at all apprehend
an object-support (ālambana) outside mind,
then it stands established in representation-only (vijñaptimātratva):
for, when the graspable-appearance (grāhyābhā) is absent,
there is no grasping of that.

**raw-LLM** — But when cognition no longer apprehends an object, then it is established in mere representation, since, in the absence of what is grasped, there is no grasping of it.

**MITRA** — When cognition no longer apprehends an object of dependence, it abides in the state of representation-only, for in the absence of a graspable object, there is no grasping (of a subject).

**human (Salvini 2022)** — On the other hand, when awareness does not apprehend a support, then it is placed within consciousness-only-ness, since in the absence of an object to be grasped, it does not grasp that.

commentary-grounded decisions: J1 (C; trbh [[1486, 1488]]); J2 (C; trbh [[1486, 1487]]); J3 (C; trbh [[1487], [1488]]); J4 (C; trbh [[1488, 1489], [1495, 1496]]); J5 (C; trbh [[1484, 1485], [1494]]); J6 (C; trbh [[1490, 1491], [1492, 1493]])

## v.29

*verification: 10 pass / 0 fail / 1 unsupported*

**agent** — It is without grasping mind (acitta), non-apprehension (anupalamba);
and that is world-transcending knowledge (lokottara-jñāna).
Then comes the turning-about of the basis (āśraya-parāvṛtti),
through the abandonment of the twofold unwieldiness (dauṣṭhulya).

**raw-LLM** — It is without mind, without apprehension; and that is supramundane knowledge—the transformation of the basis through the abandonment of the twofold affliction.

**MITRA** — That state is devoid of mind and free from apprehension; it is supramundane wisdom, and the transformation of the basis occurs through the twofold abandonment of coarseness (or, alternatively, the twofold abandonment of the two types of defilement).

**human (Salvini 2022)** — That is the mind-less non-perception; it is supramundane awareness; it is the revolution of the basis, thanks to the destruction of the twofold badness.

commentary-grounded decisions: J1 (C; trbh [[1507, 1508]]); J2 (C; trbh [[1509, 1510]]); J3 (C; trbh [[1510, 1511]]); J4 (C; trbh [[1511, 1513]]); J5 (C; trbh [[1514, 1516]]); J6 (C; trbh [[1519, 1521], [1529]]); J7 (C; trbh [[1521, 1523]]); J8 (C; trbh [[1517, 1519], [1525, 1528]])

## v.30

*verification: 13 pass / 0 fail / 0 unsupported*

**agent** — That very basis-transformation (āśraya-parāvṛtti) is the uncontaminated element-source (anāsrava dhātu)—
inconceivable, wholesome, constant, blissful.
That, for the śrāvakas, is the liberation-body (vimuktikāya);
this, of the Great Sage (mahāmuni), is called the Dharma-body (dharmakāya).

**raw-LLM** — That very state is the undefiled realm, inconceivable, wholesome, constant, and blissful; it is the body of liberation, called the Dharma-body of the Great Sage.

**MITRA** — That very realm is untainted, inconceivable, wholesome, and constant; it is bliss and the body of liberation, which the Great Sage has termed the Dharma-body.

**human (Salvini 2022)** — That itself is the dhātu without fluxes, inconceivable, virtuous, permanent; it is the blissful body of liberation, and this is called "Dharma" for the Great Muni.

commentary-grounded decisions: J1 (C; trbh [[1511, 1512, 1513, 1514, 1515, 1516], [1537, 1538, 1539]]); J2 (C; trbh [[1539, 1540, 1541, 1542, 1543]]); J3 (C; trbh [[1544]]); J4 (C; trbh [[1545, 1546]]); J5 (C; trbh [[1547, 1548, 1549, 1550]]); J6 (C; trbh [[1525, 1526, 1527, 1528, 1529], [1551]]); J7 (C; trbh [[1552, 1553, 1554, 1555], [1556, 1557], [1558]])
