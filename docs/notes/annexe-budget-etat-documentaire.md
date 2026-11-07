# Note documentaire — Annexe « Le budget de l'État » (chantier evolution-budgets)

Matière sourcée pour deux sections encore vides de `precis/fr/annexe-budget-etat.qmd` :
`#sec-bud-definitions` (« Ce que recouvre le budget ») et `#sec-bud-sources`
(« Sources et périmètres »). Ne rédige pas l'annexe ; fournit les faits, les textes et les
clés de citation. Toutes les dates, numéros et pages ci-dessous ont été vérifiés le
30 octobre 2026 contre `jort_cache.db`, les `references.json` du dépôt, le texte des deux lois
organiques et les fiches de source de `tunisia-data`. Les points non vérifiables sont en § Lacunes.

---

## A. Le texte de référence : les deux lois organiques du budget (LOB)

### A.1 Les deux régimes, avec références JORT exactes

| | Loi organique **67-53** | Loi organique **2019-15** |
|---|---|---|
| Intitulé | Loi n° 67-53 du 8 décembre 1967, portant loi organique du budget | Loi organique n° 2019-15 du 13 février 2019, relative à la loi organique du budget |
| Signature | 8 décembre 1967 | 13 février 2019 |
| Publication JORT | **JORT n° 52 du 12 décembre 1967, p. 1574-1577** (éd. française) | **JORT n° 15 du 19 février 2019** (le texte commence p. 395 ; art. 14 p. 396-397, art. 73 p. 405, éd. française) |
| recid `jort_cache` | 117149 | 108554 |
| Clé de citation existante | `loi-67-53-lob` (precis/fr/fiscalite/references.json) | `loi-org-2019-15-lob` (precis/fr/references.json) |
| Statut | abrogée (dispositions contraires) par l'art. 73 de la LOB 2019-15 | en vigueur |

- **Antécédent** : le 67-53 a lui-même abrogé, par son **art. 50**, la **loi n° 60-1 du 12 mars
  1960 portant loi organique du budget** (JORT n° 13 du 11 mars 1960, p. 324-325 ; recid de
  `jort_cache`). La LOB 2019 s'inscrit donc dans une troisième génération (1960 → 1967 → 2019).
- **67-53, « plusieurs fois modifiée »** — modificatives repérées dans `jort_cache` (titres fr) :
  loi org. **83-51** du 10 juin 1983 (JORT n° 44), **89-41** du 8 mars 1989 (JORT n° 20, p. 451),
  **89-112** du 26 décembre 1989 (JORT n° 87, p. 2124), **96-103** du 25 novembre 1996
  (JORT n° 96 du 29 nov. 1996, p. 2391-2392 ; clé existante `loi-org-96-103-lob`) et **2004-42**
  du 13 mai 2004 (JORT n° 40 du 18 mai 2004, p. 1292-1295). La 96-103 a refondu la nomenclature
  en titres/parties/sections ; la 2004-42 a introduit programmes et missions et a été abrogée
  nommément par l'art. 73 de la LOB 2019.

### A.2 À partir de quel exercice la LOB 2019 s'applique (entrée en vigueur progressive)

La LOB 2019-15 ne fixe pas une date unique d'entrée en vigueur ; elle **échelonne** celle de
certaines dispositions (titre VII, « dispositions transitoires et finales ») :
- **Art. 70** : entrent en vigueur **au plus tard fin 2020** le plafond de l'effectif global du
  personnel (art. 45, 48) et le rapport sur les dépenses fiscales (art. 46, 12ᵉ tiret).
- **Art. 71** : évaluation de la performance confiée aux organismes de contrôle administratif
  **jusqu'en 2020**, en attendant le cadre réglementaire.
- **Art. 72** : la **comptabilité générale et analytique** (art. 27, 28) et le délai de
  présentation de la loi de règlement (art. 66, dernier alinéa) entrent en vigueur **en 2022** ;
  les **états financiers certifiés par la Cour des comptes** (art. 68, §2-3) **au plus tard en 2023**.
- **Dans les faits**, la présentation du budget **par missions et programmes** (le cœur de la
  réforme GBO) s'applique **à partir de la loi de finances pour 2020 / exercice 2020** : c'est le
  passage du régime « onze parties/sections » (1997-2019) au régime « missions » (2020→), tel que
  la fiche `tunisia-data/sources/jort-lf-budget-etat.md` le documente loi par loi. Les exercices
  1959-2019 relèvent donc de la logique **titres I/II** du 67-53 ; 2020→ de la logique
  **missions/programmes** de la LOB 2019.

> **⚠ Réserve** (voir § Lacunes & recherche R1) : une proposition de loi organique de 2020
> (Marsad 2020/128) visait à remplacer « 2022 » et « 2023 » de l'art. 72 par « 2028 » et « 2029 »
> (report de la comptabilité générale et des états financiers certifiés). **Aucune loi organique
> modifiant la LOB 2019 n'a été trouvée dans `jort_cache` (couverture jusqu'au 29 oct. 2026)** :
> ce report est à l'état de **proposition non confirmée**. À citer comme tel.

---

## B. Section « Ce que recouvre le budget » (`#sec-bud-definitions`) — faits sourcés

### B.1 Budget voté (loi de finances) vs budget réalisé (loi de règlement)

- **Trois catégories de lois de finances** (LOB 2019, **art. 3**) : la loi de finances de l'année,
  la loi de finances rectificative, la **loi de règlement du budget**. [`loi-org-2019-15-lob`]
- **Voté** — la loi de finances de l'année **prévoit et autorise** l'ensemble des ressources et des
  charges et **arrête l'équilibre budgétaire** (LOB 2019 **art. 4** ; LOB 67-53 **art. 1**). Elle
  autorise la perception des recettes et fixe le plafond des dépenses (LOB 2019 **art. 45** ;
  67-53 **art. 26**). [`loi-org-2019-15-lob`, `loi-67-53-lob`]
- **Réalisé** — la **loi de règlement** « fixe le montant définitif des recettes recouvrées et des
  ordonnances de paiement visées au cours d'une même gestion » (LOB 2019 **art. 65** ; formulation
  quasi identique au 67-53 **art. 46** : « constate le montant définitif des encaissements de
  recettes et des ordonnancements de dépenses »). C'est l'exécution, non la prévision.
  [`loi-org-2019-15-lob`, `loi-67-53-lob`]
- Le règlement est tardif : le projet de loi de règlement d'une année N est transmis au Parlement
  **en même temps que le PLF de N+2** (LOB 2019 **art. 66**). Conséquence éditoriale : la série
  réalisée du précis vient des **rapports du ministère des Finances**, pas des lois de règlement
  publiées (voir § C).

### B.2 La structure en titres (67-53) vs missions/programmes (LOB 2019)

**Régime 67-53** — le budget de l'État est structuré en **deux titres** (art. 3, 5, 6 ;
nomenclature consolidée par la loi 96-103) :
- **Titre I** = **dépenses de gestion** (fonctionnement) **+ intérêts de la dette** (67-53
  **art. 3 et 4** : parties 1 rémunérations publiques, 2 moyens des services, 3 interventions
  publiques, 4 dépenses de gestion imprévues, 5 intérêts de la dette ; section 1 = gestion,
  section 2 = intérêts).
- **Titre II** = **dépenses de développement + remboursement du principal de la dette** (67-53
  **art. 5** : parties 6 investissements directs, 7 financement public, 8 développement imprévu,
  9 développement sur ressources extérieures affectées, 10 remboursement du principal). La loi
  précise : « **les dépenses de développement sont destinées à l'exécution des programmes prévus
  par les plans de développement** ». [`loi-67-53-lob`, `loi-org-96-103-lob`]
- Côté ressources, symétrie (67-53 **art. 6-8**) : **titre I** = recettes fiscales ordinaires +
  non fiscales ordinaires ; **titre II** = recettes exceptionnelles + **ressources d'emprunts**.

> C'est exactement la grandeur de la série votée 1959-1986 du précis : « budget ordinaire voté
> (titre I) » (fiche `jort-lf-budget-ordinaire.md` ; CSV : « budget ordinaire voté par la loi de
> finances (titre I), non un total de l'État »). **Titre I ≠ total** : l'investissement (titre II)
> est voté à part, et ses voies et moyens incluent une « contribution du budget ordinaire »
> (3 MD en 1961, art. 23 de la loi n° 60-38) — additionner titre I et titre II la compterait deux fois.

**Régime LOB 2019** — la terminologie « titres I/II » **disparaît**. Les dépenses sont classées
**par missions et programmes** (art. 15, 18), et, à l'intérieur de chaque programme, par **parties**
selon la nature : rémunération, gestion, interventions, investissement, opérations financières,
charges de financement, dépenses imprévues et non réparties (**art. 15**). [`loi-org-2019-15-lob`]

> **Rupture de vocabulaire à signaler au rédacteur** : « titre I / titre II » n'a de sens que
> jusqu'à 2019. Pour 2020→, parler de « budget de fonctionnement/d'investissement » reste une
> glose économique, mais la loi ne structure plus en titres. La fiche `jort-lf-budget-etat.md`
> recense cinq régimes de présentation successifs du voté : *budget ordinaire + budget de capital*
> (1986) ; *budget général* (1987-1993) ; *titres I et II* (1994-1996) ; *onze parties/sections*
> (1997-2019) ; *missions* (2020-2026). **Ne jamais chaîner un régime à l'autre.**

### B.3 Recettes vs dépenses ; fiscales, non fiscales, dons, emprunt

- **LOB 2019, art. 13-14** : les ressources budgétaires sont retracées sous forme de **recettes**,
  classées en trois parties — **recettes fiscales, recettes non fiscales, dons** ; les charges
  budgétaires sous forme de **dépenses**. [`loi-org-2019-15-lob`]
- **L'emprunt n'est pas une recette** sous la LOB 2019 : les ressources d'emprunt (dette, sukuks)
  sont des **ressources de trésorerie** (art. 12, 17), distinctes des recettes du budget. Le total
  voté 2020→ imprime recettes (fiscales + non fiscales + dons), dépenses hors principal, déficit,
  puis ressources du Trésor (`jort-lf-budget-etat.md`, régime « missions »).
- **Sous le 67-53, au contraire**, les **ressources d'emprunt** faisaient partie des ressources du
  budget (titre II, **art. 6 et 8** : 7ᵉ-9ᵉ catégories, emprunt intérieur/extérieur). Les **dons**
  n'apparaissent comme catégorie propre qu'avec la LOB 2019. **Donc la liste « recettes fiscales,
  non fiscales, dons, ressources d'emprunt » mélange deux régimes** : à ventiler selon l'époque.

### B.4 « Budget général de l'État » / « total de l'État » : ce qu'il agrège

- Le terme « **budget général de l'État** » est **l'ancienne dénomination** du 67-53 d'origine,
  **remplacée par « budget de l'État »** par la loi 96-103 (note de concordance terminologique de
  la version consolidée : « le budget et budget général, budget général de l'État : le budget de
  l'État »). [`loi-67-53-lob`, `loi-org-96-103-lob`]
- Un « **total de l'État** » agrège **titre I + titre II** (fonctionnement + développement), plus
  les fonds/comptes spéciaux ; il n'est **pas** le budget ordinaire voté. Exemple sourcé : la loi
  de finances pour 1983 (loi n° 82-91, art. 1-2) fixe un **budget général de 1 753 MD** (954 de
  dépenses courantes + 799 d'investissement), tandis que le budget ordinaire voté de 1983 (titre I)
  est celui des art. 4 et 6 (`jort-lf-budget-ordinaire.md`). D'où le piège central de l'annexe :
  **la série votée titre I 1959-1986 n'est qu'une part du budget**, et le point de 1986 (1 970 MD
  titre I voté vs 2 395 MD dépenses réalisées hors dette) matérialise l'écart — à montrer comme
  rupture, jamais comme raccord.

---

## C. Section « Sources et périmètres » (`#sec-bud-sources`) — faits sourcés

| Série du précis | Ce que la source mesure | Couverture | Source primaire | Périmètre / rupture de champ |
|---|---|---|---|---|
| `jort-lf-budget-ordinaire` | budget ordinaire **voté**, titre I (recettes ordinaires art. 1 = crédits de dépenses de gestion/courantes) | 1959-60, 1961→1986 | **Lois de finances, JORT éd. française** (art. 1 et 3, ou 6 en 1983), corpus local `PDFs-legislation-tunisie` | **Voté, pas réalisé** ; **titre I seul** (hors investissement titre II) ; la loi ne dit pas si le service de la dette est inclus ; s'arrête en 1986 ; 1958-59, gestion 1960 et budgets d'équipement non lus |
| `denominateurs-depenses-etat-pib` (dépenses hors dette) | dépenses de l'État **réalisées, hors service de la dette** + PIB déduit | 1986-2025 (PIB dès 1984) | **Ministère des Finances** : `repartition_economique_des_depenses_fr.xls` (répartition économique des dépenses, 1990-2025) et `indicateurs des fin pub`.xls (déficit, pression fiscale, dette, depuis 1986) | **Réalisé ≠ voté** ; **hors principal de la dette** ; PIB **non publié**, déduit (déficit MD ÷ déficit %PIB) ; **PIB à bases multiples accolées** (1983 présumée → 1997 → 2015), ruptures 1997, 2002, 2005, 2010, 2025 ; avant 1986, PIB = Banque mondiale (WDI) |
| `recettes-fiscales-composition` | composition des **recettes fiscales réalisées** (IRPP, IS, douanes, TVA, consommation, autres indirects) | 1986-2025 (réalisations ; puis prévisions LF/LFC) | **Ministère des Finances** : `Série Recettes_fiscales_fr.xls` (page « Indicateurs → Ressources ») | **Recettes fiscales seulement** (hors non fiscales, dons, emprunt) ; **rupture 1990** : la ligne « impôts sur le revenu » agrège, avant 1990, impôts cédulaires + contribution personnelle d'État (IRPP créé par la loi n° 89-114 du 30 déc. 1989, applicable aux revenus 1990→) |

**Le pivot 1986.** La bascule voté (JORT) → réalisé (minfin) coïncide avec le début des séries
du ministère des Finances (1986). Les deux segments **ne se raccordent pas** (voté/titre I vs
réalisé/hors dette) : à présenter par segments, avec la rupture documentée.

**Fiches de source de l'entrepôt `tunisia-data`** (provenance, URL, SHA, date de collecte) :
`sources/jort-lf-budget-ordinaire.md`, `sources/jort-lf-budget-etat.md`,
`sources/minfinances-recettes-fiscales.md`, `sources/minfinances-indicateurs.md`.
Fichiers minfin déjà versés dans `data/raw/minfinances/` (recettes_fiscales.xls,
repartition_depenses.xls, indicateurs_fp_*.xls), consultés les 9 juin / 9 sept. 2026.

---

## D. Références candidates (pour le bibliographe)

**Déjà présentes — réutiliser la clé (ne rien recréer) :**
- `loi-67-53-lob` — *Loi n° 67-53 du 8 déc. 1967, portant loi organique du budget*,
  JORT n° 52 du 12 déc. 1967, p. 1574-1577 (precis/fr/fiscalite/references.json).
- `loi-org-96-103-lob` — *Loi organique n° 96-103 du 25 nov. 1996…*, JORT n° 96, p. 2391-2392
  (precis/fr/fiscalite/references.json).
- `loi-org-2019-15-lob` — *Loi organique n° 2019-15 du 13 fév. 2019, relative à la loi organique
  du budget*, JORT n° 15 du 19 fév. 2019, p. 395 sqq (precis/fr/references.json).

**À créer (CSL-JSON) si le rédacteur en a besoin** — proposées, non présentes :
```json
[
  {"id":"loi-org-2004-42-lob","type":"legislation","title":"Loi organique n° 2004-42 du 13 mai 2004, modifiant et complétant la loi organique du budget n° 67-53 du 8 décembre 1967","issued":{"date-parts":[[2004,5,13]]},"references":"JORT n° 40 du 18 mai 2004, p. 1292-1295","note":"Introduit programmes et missions ; abrogée nommément par l'art. 73 de la LOB 2019-15. recid jort_cache à confirmer."},
  {"id":"loi-60-1-lob-1960","type":"legislation","title":"Loi n° 60-1 du 12 mars 1960, portant loi organique du budget","issued":{"date-parts":[[1960,3,12]]},"references":"JORT n° 13 du 11 mars 1960, p. 324-325","note":"Première LOB de l'indépendance ; abrogée par l'art. 50 de la loi n° 67-53."},
  {"id":"minfin-recettes-fiscales-xls","type":"dataset","title":"Série des recettes fiscales de l'État, 1986-2025 (réalisations)","author":[{"literal":"Ministère des Finances (Tunisie)"}],"URL":"https://www.finances.gov.tn/sites/default/files/users/user93/Série Recettes_fiscales_fr.xls","accessed":{"date-parts":[[2026,9,9]]},"note":"Fiche tunisia-data : sources/minfinances-recettes-fiscales.md."},
  {"id":"minfin-repartition-depenses-xls","type":"dataset","title":"Série de la répartition économique des dépenses de l'État, 1990-2025","author":[{"literal":"Ministère des Finances (Tunisie)"}],"URL":"https://www.finances.gov.tn/.../Série repartition_economique_des_depenses_fr.xls","accessed":{"date-parts":[[2026,6,9]]},"note":"Fiche tunisia-data : sources/minfinances-indicateurs.md."},
  {"id":"minfin-indicateurs-fp-xls","type":"dataset","title":"Indicateurs des finances publiques (déficit, pression fiscale, dette), depuis 1986","author":[{"literal":"Ministère des Finances (Tunisie)"}],"URL":"https://www.finances.gov.tn/sites/default/files/users/user93/indicateurs des fin pub LF2026.xls","accessed":{"date-parts":[[2026,9,9]]},"note":"PIB non publié, déduit du déficit MD ÷ déficit %PIB. Fiche : sources/minfinances-indicateurs.md."}
]
```
Les modificatives 83-51, 89-41, 89-112 existent dans `jort_cache` (réfs ci-dessus § A.1) :
à créer seulement si citées.

---

## E. Notions à glossaire (pour le terminologue)

| Terme FR | AR (indicatif) | Source canonique pressentie |
|---|---|---|
| Loi de finances (de l'année) | قانون المالية | LOB 2019 art. 3-4 / 67-53 art. 1 |
| Loi de finances rectificative / complémentaire | قانون مالية تكميلي | LOB 2019 art. 5 / 67-53 art. 43 |
| Loi de règlement du budget | قانون غلق الميزانية | LOB 2019 art. 65 / 67-53 art. 46 |
| Budget voté / budget réalisé (exécuté) | — | distinction LOB 2019 art. 4 vs 65 |
| Titre I (budget de fonctionnement/gestion) | العنوان الأول | 67-53 art. 3-4 |
| Titre II (dépenses de développement/investissement) | العنوان الثاني | 67-53 art. 3, 5 |
| Budget de l'État / budget général de l'État | ميزانية الدولة | 67-53 (concordance 96-103) |
| Recettes fiscales / non fiscales / dons | موارد جبائية / غير جبائية / هبات | LOB 2019 art. 14 |
| Ressources d'emprunt / ressources de trésorerie | موارد الاقتراض / موارد الخزينة | 67-53 art. 6, 8 ; LOB 2019 art. 12, 17 |
| Mission / programme | مهمة / برنامج | LOB 2019 art. 15, 18 |
| Pression fiscale | الضغط الجبائي | indicateurs minfin (recettes fiscales ÷ PIB) |
| Fonds spéciaux du Trésor / comptes spéciaux | صناديق الخزينة / حسابات خاصة | 67-53 art. 19 ; LOB 2019 art. 29-33 |

(Vérifier l'existence préalable dans `precis/glossaire.yml` : `pression-fiscale`, `loi-de-finances`,
`irpp` y figurent sous une forme ou une autre ; ne pas doublonner.)

---

## F. Lacunes et pistes (à verser au backlog)

1. **R1 — report d'entrée en vigueur de la LOB 2019 (2028/2029)** : la proposition Marsad 2020/128
   remplace « 2022/2023 » (art. 72) par « 2028/2029 ». **Aucune loi organique modifiant la LOB 2019
   trouvée dans `jort_cache` (couverture au 29 oct. 2026).** Statut du report : **non confirmé**.
   Piste : vérifier au JORT 2020-2021 (recherche arabe sur « القانون الأساسي للميزانية ») et sur
   Marsad l'issue de la proposition. → voir fiche R1 ci-dessous.
2. **Page JORT exacte de la LOB 2019** : `jort_cache` ne porte que l'édition arabe (titre arabe
   seul, année 2019 ≈ 76 % de notices arabes) ; `pages` et `pdf_fr` sont vides en base. La page
   française (p. 395 sqq) vient du corpus local et de la note de `loi-org-2019-15-lob` (vérifiée
   4 oct. 2026), **pas** de `jort_cache`. Un relevé page à page (art. 70-73, entrée en vigueur) de
   `PDFs/JORT/2019/fr/Jo0152019.pdf` reste à faire si le rédacteur cite ces pages.
3. **Service de la dette dans le titre I voté (1959-1986)** : le 67-53 range les intérêts de la
   dette en titre I (section 2, 5ᵉ partie), mais les articles 1/3 des lois de finances lues ne
   disent pas si le montant voté du budget ordinaire les inclut (`jort-lf-budget-ordinaire.md`,
   « la loi ne dit pas […] si le montant comprend le service de la dette »). Non tranché.
4. **Texte original 67-53 (1967) vs consolidé** : les définitions de titres ci-dessus sont lues sur
   la version **consolidée** (telle que modifiée par 96-103 et 2004-42, via legislation-securite.tn,
   source de commodité). Le JORT d'origine (`loi-67-53-lob`, p. 1574-1577) porte la rédaction de
   1967, dont la nomenclature des parties diffère. Pour une citation au mot sur l'état 1959-1986,
   lire le fascicule d'origine `PDFs/JORT/1967/fr/Jo05267.pdf`.
5. **Pas de série longue des recettes totales ni du déficit/dette en cache** (note de conception,
   § 2) : à sourcer (minfin indicateurs, BCT) si le récit « entrées/sorties » doit être bouclé.

---

## G. Recherches infructueuses — fiche proposée

> Fiche NOUVELLE (non enregistrée ; à créer via `scripts/recherches.py` si le rédacteur la retient).

```
id: r-lob2019-report-entree-vigueur
objet: loi organique modifiant la LOB n° 2019-15 (report d'entrée en vigueur des art. 27, 28, 66, 68)
ou: jort_cache.db ; pist.tn (éd. fr) ; Marsad Majles (suivi parlementaire)
requetes:
  titres_fts: ["الميزانية 2019", "organique budget 2019"]
  titres_like: ["%2019-15%", "%organique du budget%"]
  iort_ar: ["القانون الأساسي للميزانية", "15 لسنة 2019", "تنقيح القانون الأساسي عدد 15"]
  plein_texte: ["2028", "2029 الفصل 72"]
passe:
  resultat: aucun
  couverture: "jort_cache textes type 'Loi organique' 2019-2026 ; aucune modificative de la LOB 2019 ; proposition Marsad 2020/128 repérée mais statut d'adoption non vérifié"
  couvert-jusqu-au: 2026-10-29
  sources: [titres_fts, titres_like, iort_ar]
```
