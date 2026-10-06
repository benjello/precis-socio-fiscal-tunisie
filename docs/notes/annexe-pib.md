# Note documentaire — annexe « Le PIB et ses changements de base »

Note du documentaliste, arrêtée au 6 octobre 2026. Elle rassemble la matière d'une annexe du site
(`precis/fr/annexe-pib.qmd`, à écrire par le rédacteur) ; elle ne rédige pas l'annexe.

Demande de l'humain : « Chaque fois que l'on utilise un PIB, il faut savoir en quelle base il est et
s'il est rétropolé. Si ce n'est pas le cas, il faut le préciser. Et de toute façon il faut créer une
annexe sur le PIB et expliquer les changements de base. On pourra s'y référer quand on signalera des
ruptures de série. »

**Niveaux de preuve** employés ci-dessous :

- **[lu]** — phrase ou tableau lu dans la publication, page donnée (page du fichier PDF, non le
  folio imprimé) ;
- **[calculé]** — tiré d'une série de `tunisia-data` par un script, fichier et colonne donnés ;
- **[rapproché]** — déduit de l'égalité, à moins de 0,06 %, d'une valeur avec une série de base
  connue ; ce n'est pas une mention de la source ;
- **[non établi]** — rien de lu ; où chercher est dit en § 5.

Fichiers de `~/projets/tunisia-data` : `R/` abrège `data/raw/`, `P/` abrège `data/processed/`.
Éditions de l'INS : `R/ins-publications/comptes-de-la-nation/<édition>.pdf`. Rapports de la BCT :
`R/bct-archives/109/`.

---

## 0. Trois constats à retenir avant le détail

1. **L'INS ne reconnaît que trois bases : 1983, 1997, 2015.** « Depuis son instauration dans les
   années quatre-vingt avec la première base 1983, le Système de Comptabilité Nationale Tunisien
   (SCNT) aura connu deux changements de base : 1997 et maintenant 2015 » (`2015-2020-base-2015.pdf`,
   p. 11) **[lu]**.
2. **« 1990 », « 2005 » et « 2010 » ne sont pas des bases des comptes** mais des **années de prix**
   des séries en volume, à l'intérieur de la base 1983 (prix constants de 1990) puis de la base 1997
   (prix de 2005, puis de 2010 — cette dernière attestée par la BCT et le FMI, non par une
   édition de l'INS). Elles ne changent rien au PIB aux prix courants. La « base 2010 » prêtée au
   FMI et à la Banque mondiale est, pour les niveaux nominaux, **la base 1997 de l'INS** : le FMI
   écrit lui-même « constant (2010) prices according to the System of National Accounts 1993 »
   (§ 1.5).
3. **L'INS a rétropolé la base 2015 jusqu'en 2010**, dans le classeur joint à son communiqué du
   15 août 2021 — et non dans une édition des *Comptes de la nation*. C'est l'origine, jusqu'ici non
   rattachée, des valeurs 2010-2014 du ministère des Finances et de la Banque mondiale (§ 1.4, § 3).

Deux séries de l'entrepôt que le précis publie portent, de ce fait, une étiquette de base
inexacte (§ 4.3).

---

## 1. Les bases des comptes nationaux tunisiens

### 1.1 Tableau d'ensemble

| Base | Système suivi | Première publication lue | Années publiées par l'INS dans cette base | Rétropolation par l'INS | Niveau de preuve |
|---|---|---|---|---|---|
| Avant 1983 | non établi | — | — | — | **[non établi]** : des comptes existent (BCT, rapports annuels, agrégats aux prix de 1957, 1960, 1966, 1972, 1980), aucune « base » n'est nommée par un texte lu |
| **1983** | SCN 1968 | la plus ancienne édition lue est le volume n° 11, 2001-2005, déc. 2006 ; la première publication n'est pas identifiée | éditions lues : 2001-2008 ; transmis aux Nations unies : 1992-2009 (série 30) ; la série 20 (1970-1997) est au même niveau, sa base n'est pas dite | étendue vers le passé non établie | **[lu]** pour le système et les éditions ; **[non établi]** pour la date d'entrée en service et la profondeur |
| **1997** | SCN 1993 (« SCNT97 ») | adoptée « début 2010 » selon le FMI ; premier emploi par la BCT : rapport annuel 2009 ; première édition de l'INS lue : volume n° 15, 2005-2009, déc. 2010 | éditions : 2005-2017 ; transmis aux Nations unies : 1997-2017 (série 100) ; comptes poursuivis jusqu'en 2020 | **jusqu'en 1997** : « le CD accompagnant ce volume contient la série des comptes 1997-2007 » | **[lu]** |
| **2015** | SCN 2008 | communiqué et classeur du 15 août 2021 ; édition 2015-2020, vol. A et B, « Edition 2022 » | éditions : 2015-2025 ; transmis aux Nations unies : 2015-2023 (série 1000) | **jusqu'en 2010**, PIB et emplois aux prix courants et aux prix de l'année précédente, classeur du 15 août 2021 | **[lu]** |
| « 1990 », « 2005 », « 2010 » | — | — | — | — | **[lu]** : années de prix des volumes, pas des bases (§ 1.5) |

### 1.2 Base 1983 (SCN 1968)

- **Mention de la base** : bandeau « Les Comptes de la Nation Base 1983 » sur chaque page des
  éditions 2001-2005 (volume n° 11, « Décembre 2006 »), 2002-2006 (n° 12, déc. 2007), 2003-2007
  (n° 13, déc. 2008), 2004-2008 (n° 14, déc. 2009) **[lu]**.
- **Système** : « Les comptes nationaux présentés dans ce volume respectent les concepts et les
  définitions du système des Nations Unies de 1968 (SCN 68) » (`2001-2005.pdf`, p. 8) **[lu]**.
- **Prix constants** : « aux prix courants et aux prix constants de l'année de référence 1990 »
  (`2001-2005.pdf`, p. 3) **[lu]**. C'est l'origine du « PIB aux prix constants de 1990 » et du
  « Déflateur du PIB (1990=100) » des rapports de la BCT jusqu'à celui de 2008 (`rapport2008.pdf`,
  p. 72) **[lu]**.
- **Couverture de l'informel** : enquête annuelle auprès des entreprises « de plus de 6 salariés »,
  complétée par « une enquête quinquennale (1997, 2002…) sur les entreprises de moins de 6 salariés
  (secteur non structuré) », ou son actualisation (`2001-2005.pdf`, p. 8) **[lu]**.
- **Entrée en service** : l'INS écrit « instauration dans les années quatre-vingt » (`2015-2020-base-2015.pdf`,
  p. 11) **[lu]**. Le rapport annuel 1992 de la BCT note : « À partir de 1990, les taux
  d'accroissement de la valeur ajoutée en termes réels sont calculés selon le nouveau système des
  Comptes Nationaux qui a été harmonisé avec celui de l'Organisation des Nations-Unies. Cela s'est
  traduit par des écarts assez importants pour l'année de base 1990 […] par comparaison aux taux
  obtenus selon l'ancien système des Comptes Nationaux » (`RA_fr_1992.pdf`, p. 52 ; même note p. 43 ;
  pp. 98 : des prévisions encore « selon l'ancien système ») **[lu]**. Lecture prudente : un
  « nouveau système » harmonisé avec celui des Nations unies entre dans les rapports de la BCT
  avec l'exercice 1992, avec 1990 pour année de prix ; **qu'il s'agisse de la base 1983 n'est écrit
  par aucun des deux textes** **[non établi]**.
- **Profondeur vers le passé** : UNdata, tableau 1.1, porte pour la Tunisie une série 10 (1960-1969),
  une série 20 (1970-1997) et une série 30 (1992-2009), toutes « SNA 1968 ». Séries 20 et 30
  coïncident à 0,01 % près sur 1992-1997 : la série 30 **ne relève pas le niveau** de la série 20
  **[calculé]** (script `pib-scripts/sources_vs_bases.py` du scratchpad, § 2.5). Que la série 20 soit
  la base 1983 rétropolée jusqu'en 1970, ou une série antérieure dont la base 1983 n'aurait pas
  modifié le niveau, n'est dit nulle part **[non établi]**.

### 1.3 Base 1997 (SCN 1993, « SCNT97 »)

- **Première publication** : `2005-2009.pdf`, couverture « NOUVEAU SYSTEME DE COMPTABILITE NATIONALE
  TUNISIEN — METHODOLOGIE ET PRINCIPAUX RESULTATS — Les Comptes de la Nation Base 1997 […]
  2005-2009 — Décembre 2010 — N° 15 » (p. 1) **[lu]**.
- **Système et année de base** : « L'INS a entrepris […] la révision du système de comptabilité
  nationale tunisien afin de l'adapter au SCN93. Cette adaptation a été menée sur la base de l'année
  1997 et donné lieu au SCNT97 » (p. 11) ; « l'année de base des comptes qui est l'année 1997 »
  (p. 14) **[lu]**.
- **Ce qui change, selon l'INS** : « les nouveaux concepts et définitions du SCN93 des Nations
  Unies, les nouvelles nomenclatures tunisiennes des activités et des produits (NAT1996 et CTP2002),
  les nouvelles enquêtes économiques, les estimations actualisées des champs non couverts par des
  enquêtes directes et la 5ème Edition du manuel de la balance des paiements du FMI » (p. 3)
  **[lu]**. Les tableaux de synthèse changent de nom : TES → TRE, TEE → TCEI.
- **Prix constants** : « aux prix de l'année précédente (n-1) » ; « des comptes aux prix constants
  d'une année fixe (année 2005) sont aussi élaborés » (p. 3) **[lu]**. La mention de l'année fixe
  2005 figure dans les éditions 2005-2009 à 2009-2013 et disparaît des préfaces à partir de
  l'édition 2010-2014 **[lu]** (recherche plein texte des dix-neuf éditions).
- **Rétropolation** : « le CD accompagnant ce volume contient la série des comptes 1997-2007
  élaborées selon le nouveau système SCNT97 » (p. 3) **[lu]**. Le CD lui-même n'est pas dans
  l'entrepôt ; les valeurs 1997-2004 sont connues par UNdata (série 100) **[calculé]**.
- **Date d'adoption et ampleur, selon le FMI** : « In early 2010, the Tunisian authorities adopted
  a new national accounts system for the period 1997–2008 to comply with the 1993 United Nations
  national accounts system. […] The total effect of the introduction of new system has been an
  increase of around 10 percent in nominal GDP figures each year. Constant price aggregates are now
  calculated based on last year's prices » (rapport n° 10/282, annexe 5, p. 39 du PDF, avec un
  tableau « Old GDP / New GDP » 2002-2008 et l'effet sur le déficit, le solde courant et la dette,
  « Source: Tunisian authorities ») ; « a revised national accounts series covering the period
  1997–2009 based on SNA 1993 (instead of, as before, SNA 1968) » (p. 48) **[lu]**. La
  rétropolation 1997-2004 précède donc l'édition de décembre 2010. Le « New GDP » 2002-2004 du FMI
  (32 901,2 ; 35 373,3 ; 38 838,5) est celui de la série 100 des Nations unies **[calculé]**.
- **Premier emploi par la BCT** : le rapport annuel 2008 donne encore le PIB « aux prix constants de
  1990 » et 50 325 MD pour 2008 (`rapport2008.pdf`, p. 72) ; le rapport 2009 donne 55 297 MD pour
  la même année et cite le « Nouveau Système des Comptes Nationaux » (`rapport2009.pdf`, pp. 73, 91,
  143) **[lu]**.
- **Fin** : la dernière édition en base 1997 est 2013-2017 (« Edition 2019 ») **[lu]**. Les comptes
  en base 1997 ont pourtant été tenus jusqu'en 2020 : le communiqué de 2021 compare, pour 2019 et
  2020, croissance, déficit et dette « dans l'ancienne base » et en base 2015 (§ 1.4), et le rapport
  annuel 2020 de la BCT donne des PIB 2018-2020 de ce niveau (`RA_2020_fr.pdf`, p. 59) **[lu]**.

### 1.4 Base 2015 (SCN 2008)

- **Première publication** : communiqué « Les Comptes Nationaux changent de base », daté du
  15 août 2021 sur le site de l'INS, avec une « Note explicative du changement de base des comptes
  nationaux tunisiens, base 2015 » (4 p.) et un classeur « Données » **[lu]** (fichiers déposés,
  § 7). Puis l'édition 2015-2020, « Base 2015 », volumes A et B, « Edition 2022 »
  (`2015-2020-base-2015.pdf`, p. 1), dont les travaux « ont été lancés dès 2017 et se sont étalés
  sur cinq années » (p. 3) **[lu]**.
- **Ce qu'est une base, selon l'INS** : « on appelle base un ensemble fixé de concepts,
  nomenclatures, et méthodes mis en œuvre pour un exercice ou une année déterminée […] et qui seront
  répliqués pour l'élaboration des comptes économiques des années qui suivent » (p. 11) ; « au fur
  et à mesure qu'on s'écarte de l'année de base, la qualité des comptes nationaux se dégrade »
  (p. 11) **[lu]**. L'opération est dite « "rebasage" ou "changement de base" » (p. 3).
- **Ampleur** : « Le PIB se situe pour 2015 à 89 802,2 millions de dinars, soit une révision à la
  hausse de 5 113 millions de dinars (ou +6 %) par rapport à son niveau dans les comptes de la base
  1997, dont 4 781,8 millions de dinars liés aux activités marchandes et seulement 331,2 millions
  […] à l'activité non marchande » (note du 15 août 2021, p. 1) **[lu]**. Contributions à la
  réévaluation : consommation finale + 3,2 points, FBCF + 2,4 points, solde extérieur − 0,2 point
  (p. 2) **[lu]**.
- **Ce qui change, selon l'INS** (note, pp. 1-4 ; édition 2015-2020, pp. 10-21) **[lu]** :
  - passage au SCN 2008, dont « l'impact net […] dans la réévaluation du PIB de 2015 est
    relativement modeste » (édition, p. 12) : recherche-développement et armement en FBCF,
    sous-traitance internationale en net (sans effet sur le PIB), SIFIM, production de la banque
    centrale et de l'assurance, production agricole rattachée à l'exercice (l'huile d'olive n'est
    plus toute affectée à l'année N+1) ;
  - nomenclatures NAT 2009 et CTP 2009 (édition, pp. 3, 21) ;
  - sources : répertoire national des entreprises et liasses fiscales, à côté de l'enquête annuelle ;
  - **économie informelle** : définition formalisée, dispositif d'enquêtes « 1-2-3 » ; les unités
    non connues de l'administration, auparavant estimées de façon « exogène et plutôt
    "grossière" », sont estimées par l'emploi de l'enquête emploi (édition, pp. 19-20). Poids de
    l'informel : « 27,4 % dans le total des revenus créés en 2015 » (note, p. 2) ;
  - **activités illégales** : « intègrent partiellement, et pour la première fois, une estimation
    de la production illégale liée à la contrebande et au trafic de stupéfiants » (édition, p. 20) ;
  - comptes de patrimoine financier (volume B).
  La note résume : « peu de changements conceptuels, […] quasi maintien des nomenclatures, mais
  davantage […] un effort particulier pour améliorer les méthodes d'évaluation » (p. 1).
- **Effet sur les ratios, dit par l'INS** : « les ratios usuels du compte des administrations
  publiques, comme le déficit budgétaire, la pression fiscale et le taux d'endettement sont
  mécaniquement tirés vers le bas par le relèvement du niveau du PIB […]. Ainsi […] le déficit
  budgétaire en 2020 passe de 11,8 % à 11,1 % et la dette publique pour la même année est réévaluée
  de 88,6 % à 83,5 % » ; PIB par habitant 2015 : 8 044,9 dinars contre 7 586,8 ; taux
  d'investissement : 21 % contre 19,8 % (note, p. 2) **[lu]**. **C'est la citation à mettre en tête
  du « comment lire une part du PIB ».**
- **Rétropolation** : principe — « Lorsque Statistiques Tunisie procède à un changement de base, de
  nouvelles estimations sont publiées pour le passé » (édition, p. 10 ; note, p. 1) **[lu]**. Fait —
  le classeur du 15 août 2021 donne le PIB et ses emplois **de 2010 à 2020** en base 2015, aux prix
  courants et aux prix de l'année précédente (feuilles « PIB & VA Courant », « Emplois PIB
  courant », « PIB & VA N-1 », « Emplois PIB N-1 ») **[lu]** ; l'édition 2015-2020, elle, « couvre
  les six années pour lesquelles les comptes sont disponibles en base 2015 » (p. 3) et ne reprend
  pas 2010-2014 **[lu]**. Les Nations unies n'ont reçu que 2015-2023 (série 1000) **[calculé]**.
  **Aucune publication lue ne rétropole la base 2015 avant 2010.** La méthode de la rétropolation
  2010-2014 n'est pas décrite **[non établi]**.

  PIB aux prix courants en base 2015, classeur du 15 août 2021, feuille « Emplois PIB courant »,
  ligne « Produit Intérieur Brut (p.m) », millions de dinars **[lu]** :

  | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 (*) | 2020 (**) |
  |---|---|---|---|---|---|---|---|---|---|---|
  | 66 139,7 | 67 747,3 | 73 895,4 | 79 096,6 | 85 345,7 | 89 802,2 | 95 286,9 | 102 011,5 | 112 985,5 | 122 578,4 | 119 526,4 |

  2019 et 2020 ont été révisés depuis (122 969,3 et 119 502,1 dans les éditions suivantes).

### 1.5 Ce que sont « 1990 » et « 2010 » — et la « base 2010 » du FMI et de la Banque mondiale

- **1990** : année de prix des volumes de la base 1983 (§ 1.2). Pas de niveau nominal propre.
- **2005** : année fixe des volumes dans les premières éditions de la base 1997 (§ 1.3).
- **2010** : année de prix des volumes de la base 1997 dans ses dernières années. Les rapports
  annuels de la BCT écrivent « Aux prix constants de 2010 » de 2016 à 2020 (`RA_2016_fr.pdf`, p. 116 ;
  `RA_2018_fr.pdf`, pp. 114, 121 ; `RA_2020_fr.pdf`, p. 142), puis « Aux prix constants de 2015 » à
  partir du rapport 2021 (`ANNUALREPORT2021FRENCH.pdf`, p. 136) **[lu]**. Le rapport 2018 écrit en
  note : « Les chiffres pour l'inflation et la croissance pour cette partie, sont exprimés dans la
  base 2010 » (p. 95) **[lu]** — « base 2010 » y désigne à la fois la base de l'indice des prix et
  l'année de prix du PIB en volume. Aucune édition des *Comptes de la nation* ne porte la mention
  « base 2010 » (recherche plein texte des dix-neuf éditions) **[lu]**.
- **Conséquence** : il n'existe **pas de PIB nominal « base 2010 »** distinct. Les valeurs que
  `tunisia-data` étiquette « base 2010 » (`docs/reconciliation-masse-salariale-pib.md` : PIB 2015 =
  84 648, PIB 2017 = 96 325) sont, au chiffre près, celles des éditions 2012-2016 et 2013-2017, que
  l'INS intitule « Base 1997 » **[calculé]** (`P/ins-comptes-nationaux/pib_nominal_editions.csv`).
  **Le FMI le dit lui-même** : « The National Institute of Statistics (NSI) publishes annual and
  quarterly GDP by production in current and constant (2010) prices according to the System of
  National Accounts 1993 (SNA 1993) » (rapport n° 21/44, février 2021, annexe d'information,
  « Statistical Issues », p. 91 du PDF) ; ses tableaux portent « Real GDP (at 2010 prices) » et un
  PIB nominal de 95 865, 106 242, 114 939 et 111 251 MD pour 2017-2020 (p. 33) **[lu]** — niveaux
  de la base 1997, identiques pour 2018 et 2019 à ceux du rapport annuel 2020 de la BCT. Sa masse
  salariale de 17,6 % du PIB en 2020 est rapportée à ce PIB. Aucune édition de l'INS lue n'imprime
  « prix de 2010 » : l'année de prix 2010 n'est attestée que par la BCT et le FMI. Le libellé
  « base 2010 (FMI/BM) » du précis et de l'entrepôt est à remplacer par « base 1997 (SCN 1993,
  volumes aux prix de 2010) ». Pour la Banque mondiale (revue des dépenses publiques de 2020), la
  mention n'a pas été relue **[non établi]**.

---

## 2. Les écarts de niveau entre bases

Rien n'est recalculé à la main. Scripts (scratchpad, non commités) :
`…/scratchpad/pib-scripts/recouvrement.py` et `…/scratchpad/pib-scripts/sources_vs_bases.py`.

### 2.1 Base 1983 → base 1997 : treize années de recouvrement, 1997-2009

Source : UNdata, tableau 1.1 (dépenses du PIB), ligne B.1*g, séries 30 et 100 — et
`P/ins-comptes-nationaux/pib_undata.csv` (tableau 4.1, colonnes `serie`, `valeur_mdt`), qui donne
les mêmes valeurs sauf 2001 (28 757 au tableau 4.1, 28 729 au tableau 1.1). Millions de dinars
courants **[calculé]**.

| Année | Base 1983 (série 30) | Base 1997 (série 100) | Écart (MD) | Écart (%) |
|---|---|---|---|---|
| 1997 | 20 898,0 | 22 943,9 | 2 045,9 | 9,79 |
| 1998 | 22 561,0 | 24 827,6 | 2 266,6 | 10,05 |
| 1999 | 24 672,0 | 27 215,9 | 2 543,9 | 10,31 |
| 2000 | 26 651,0 | 29 433,3 | 2 782,3 | 10,44 |
| 2001 | 28 757,0 | 31 746,5 | 2 989,5 | 10,40 |
| 2002 | 29 924,0 | 32 901,4 | 2 977,4 | 9,95 |
| 2003 | 32 170,3 | 35 373,3 | 3 203,0 | 9,96 |
| 2004 | 35 216,8 | 38 838,6 | 3 621,8 | 10,28 |
| 2005 | 37 751,2 | 41 871,0 | 4 119,8 | 10,91 |
| 2006 | 41 384,7 | 45 756,2 | 4 371,5 | 10,56 |
| 2007 | 45 638,1 | 49 857,5 | 4 219,4 | 9,25 |
| 2008 | 50 440,5 | 55 267,8 | 4 827,3 | 9,57 |
| 2009 | 53 419,1 | 58 677,2 | 5 258,1 | 9,84 |

Dans les seules éditions de l'INS (`pib_nominal_editions.csv`, dernière édition de chaque base),
le recouvrement est 2005-2008, avec les mêmes écarts. **L'écart n'est pas constant** : de 9,3 à
10,9 % ; on ne passe pas d'une base à l'autre par un coefficient.

### 2.2 Base 1997 → base 2015 : huit années, 2010-2017 (dont cinq rétropolées)

Base 1997 : dernière édition qui porte l'année (`pib_nominal_editions.csv`). Base 2015 : classeur de
l'INS du 15 août 2021 pour 2010-2014 (rétropolé), éditions pour 2015-2017 **[calculé]**.

| Année | Base 1997 | Base 2015 | Écart (MD) | Écart (%) | Base 2015 : rétropolé ? |
|---|---|---|---|---|---|
| 2010 | 63 054,8 | 66 139,7 | 3 084,9 | 4,89 | oui |
| 2011 | 64 492,2 | 67 747,3 | 3 255,1 | 5,05 | oui |
| 2012 | 70 354,4 | 73 895,4 | 3 541,0 | 5,03 | oui |
| 2013 | 75 144,1 | 79 096,6 | 3 952,5 | 5,26 | oui |
| 2014 | 80 865,5 | 85 345,7 | 4 480,2 | 5,54 | oui |
| 2015 | 84 689,2 | 89 802,2 | 5 113,0 | 6,04 | non (année de base) |
| 2016 | 89 792,2 | 95 286,9 | 5 494,7 | 6,12 | non |
| 2017 | 96 324,7 | 102 011,5 | 5 686,8 | 5,90 | non |

Le 5 113 de 2015 est exactement le chiffre du communiqué de l'INS. Pour 2018-2020, la base 1997
n'est connue que par des estimations : BCT, rapport annuel 2020, p. 59 — 106 242, 114 939 et
110 295 MD — et FMI, rapport n° 21/44, p. 33 — 106 242, 114 939 et 111 251 MD **[lu]** ; d'après
la BCT, la base 2015 d'aujourd'hui est 6,3 %, 7,0 % et 8,3 % au-dessus — et, pour 2020,
par les ratios du communiqué de l'INS (11,8 → 11,1 ; 88,6 → 83,5), qui impliquent un écart
d'environ 6,1 à 6,3 %. Les deux ne concordent pas pour 2020 : ne pas en tirer une valeur.

### 2.3 Avant 1997 et avant 1970

Le tableau 1.1 d'UNdata, d'où viennent les séries 10 et 20, n'est pas une série de l'entrepôt.
Il se rejoue année par année à l'adresse
`https://data.un.org/Data.aspx?d=SNA&f=group_code%3a101%3bcountry_code%3a788%3bfiscal_year%3aAAAA`
(AAAA de 1960 à 2023) : ligne « Equals: GROSS DOMESTIC PRODUCT », code B.1*g, colonnes « Series »
et « SNA System ». Les 64 pages lues le 6 octobre 2026 sont déposées sous
`R/undata/sna_101_tunisie_AAAA.html` (répertoire ignoré par git).

Aucune année antérieure à 1997 n'est publiée dans deux bases dans les sources réunies
**[non établi]**. UNdata : série 10 (1960-1969) et série 20 (1970-1997) ne se recouvrent pas ; la
Banque mondiale s'écarte de la série 10 sur 1961-1969 (de − 2,7 % à + 0,6 %) et de la série 20 en
1983 et 1984 (5 668,1 et 6 412,4 contre 5 497,4 et 6 240,0, soit + 3,1 % et + 2,8 %) **[calculé]**.

### 2.4 Ce que cela fait à une part du PIB

À numérateur inchangé, part(nouvelle base) = part(ancienne base) ÷ (1 + écart).

| Une dépense de 5 % du PIB… | …vaut, la même année | Soit |
|---|---|---|
| en base 1983, en 1997 | 4,55 % en base 1997 | − 0,45 point |
| en base 1983, en 2005 | 4,51 % en base 1997 | − 0,49 point |
| en base 1997, en 2010 | 4,77 % en base 2015 | − 0,23 point |
| en base 1997, en 2015 | 4,72 % en base 2015 | − 0,28 point |
| en base 1983, en 1997, portée en base 2015 | non calculable : aucune année commune aux bases 1983 et 2015 | — |

Sur une grandeur de l'ordre de 15 % du PIB (masse salariale de l'État), le changement de 2015
déplace la part de 0,8 à 0,9 point ; sur 85 % (dette), de 5 points — c'est l'exemple de l'INS.

### 2.5 À ne pas confondre : les révisions à l'intérieur d'une base

D'une édition à l'autre, dans une même base, le PIB d'une année bouge de **moins de 0,9 %**
(maximum : 0,83 % pour 2021, 0,79 % pour 2022, 0,77 % pour 2010 ; `pib_nominal_editions.csv`,
écart max/min par année) **[calculé]**. Les comptes sont « définitifs » pour les trois premières
années d'une édition, « semi-définitifs » pour la quatrième, « provisoires » pour la cinquième
(`2005-2009.pdf`, p. 3) **[lu]**. Un changement de base est dix fois plus grand.

---

## 3. Quel PIB chaque source utilise

| Source | Années | Base | Rétropolé ? | Comment on le sait |
|---|---|---|---|---|
| **INS, *Comptes de la nation*** | éd. 2001-2005 à 2004-2008 | 1983 | non | bandeau « Base 1983 » **[lu]** |
| | éd. 2005-2009 à 2013-2017 | 1997 | non (1997-2004 sur CD, non lu) | couverture « Base 1997 » **[lu]** |
| | éd. 2015-2020 à 2021-2025 | 2015 | non | couverture « Base 2015 » **[lu]** |
| **INS, classeur du 15 août 2021** | 2010-2020 | 2015 | **oui pour 2010-2014** | intitulé du communiqué **[lu]** |
| **Nations unies, UNdata** (chiffres de l'INS) | 1960-1969 série 10 ; 1970-1997 série 20 ; 1992-2009 série 30 | « SNA 1968 » ; base non précisée par la source | non établi | colonne « SNA System » ; séries 20 = 30 sur 1992-1997 **[calculé]** |
| | 1997-2017 série 100 | « SNA 1993 » = base 1997 | oui pour 1997-2004 | égalité avec les éditions **[rapproché]** |
| | 2015-2023 série 1000 | « SNA 2008 » = base 2015 | non | idem **[rapproché]** |
| **Ministère des Finances**, classeurs « indicateurs des finances publiques » (PIB déduit du déficit en dinars et en % du PIB) | 1986-1996 | égale à la série 20 des Nations unies (base 1983 présumée) | — | base non précisée par la source **[rapproché]** |
| | 1997-2001, 2005-2008 | 1997 | oui pour 1997-2001 | **[rapproché]** |
| | 2002-2004 | **non rattachée** : 32 112,0 ; 34 630,0 ; 37 601,2 — 2,1 à 3,2 % sous la base 1997, environ 7 % au-dessus de la base 1983 | — | **[non établi]** |
| | 2009 | 1997, valeur d'une édition périmée (58 883,3 ; édition 2006-2010 : 58 890,3 ; ensuite 58 677,2) | — | **[rapproché]** |
| | 2010-2014 | **2015, rétropolation de l'INS** | **oui** | égalité, à 0,1 MD, avec le classeur du 15 août 2021 **[rapproché]** |
| | 2015-2024 | 2015 | non | **[rapproché]** |
| | 2025 | estimation propre (172 614,0 ; INS, éd. 2021-2025 : 171 642,1) | — | **[calculé]** |
| **Banque mondiale, WDI** `NY.GDP.MKTP.CN` (mise à jour du 13 juillet 2026) | 1961-1969 | non rattachée (proche de la série 10) | — | **[calculé]** |
| | 1970-1996 | série 20 des Nations unies, sauf 1983-1984 | — | **[rapproché]** |
| | 1997-2009 | 1997 | oui pour 1997-2004 | **[rapproché]** |
| | 2010-2024 | 2015 | **oui pour 2010-2014** | **[rapproché]** ; métadonnées du pays : « Nationalaccountsbaseyear = 2015 », « Country uses the 1993 System of National Accounts methodology » (mention périmée) **[lu]** |
| **Banque mondiale, rapports** (PER 2020 ; rapport de 1992 sur les communes) | selon le rapport | base non précisée par la source ; base 1997 pour ceux de 2010-2021, par la date | — | **[non établi]** |
| **BCT, rapports annuels** | jusqu'au rapport 2008 | 1983 (volumes aux prix de 1990) | — | « PIB (aux prix constants de 1990) », p. 72 **[lu]** |
| | rapports 2009 à 2020 | 1997 (volumes aux prix de l'année précédente, puis « prix constants de 2010 ») | — | « Nouveau Système des Comptes Nationaux » **[lu]** |
| | rapports 2021 et suivants | 2015 | — | « Aux prix constants de 2015 » ; PIB 2019 = 122 578 (p. 55) **[lu]** |
| **FMI**, rapport n° 10/282 (article IV 2010) | 2002-2008, deux séries | 1983 (« Old GDP », volumes « in 1990 prices ») et 1997 (« New GDP ») | oui (1997-2008) | annexe 5, p. 39 **[lu]** |
| **FMI**, rapport n° 21/44 (article IV 2021) | 2017-2025 | **1997** (SCN 1993), volumes aux prix de 2010 ; c'est la « base 2010 » de l'entrepôt | non | « constant (2010) prices according to the System of National Accounts 1993 », p. 91 ; PIB nominal p. 33 **[lu]** |

Ce que ce tableau établit de neuf : **les séries longues du ministère des Finances et de la Banque
mondiale sont la même série accolée**, qui change de niveau en **1997 (+ 9,8 %)** et en
**2010 (+ 4,9 %)** — et non en 2015. La Banque mondiale tient en outre les années 2002-2004 en
base 1997, là où le ministère porte des valeurs propres : sa série à lui a deux ruptures de plus,
en 2002 (− 2,4 %) et en 2005 (+ 3,2 %).

---

## 4. L'usage dans le précis aujourd'hui

Recherche : `PIB|produit intérieur brut` dans `precis/fr/*/*.qmd` et `precis/fr/*/figures/*.py`,
et colonnes de `precis/_seriescache/*.csv`. Les trois modules `cnss_*` de
`cotisations_sociales/figures/` sont des liens symboliques vers `caisses/figures/`.

### 4.1 Séries du cache qui portent un PIB

| Série (`precis/_seriescache/`) | Colonne | Base réelle | Étiquette actuelle | Conforme ? |
|---|---|---|---|---|
| `cnat-pib-nominal.csv` | `valeur`, `base`, `edition` | 1983 / 1997 / 2015 selon l'édition, non rétropolé | exacte | oui |
| `irpp-ratios.csv` | `pib_minfin_MDT` | accolage du § 3 : ruptures 1997, 2002, 2005, 2010, 2025 | « PIB déduit du déficit » ; base non dite | **non** |
| `irpp-ratios.csv` | `pib_cnat_MDT` | 1990-2011 : copie du PIB du ministère ; **2012-2014 : base 1997** ; 2015-2024 : base 2015 | « PIB des comptes nationaux » | **non** |
| `masse-salariale-ratios.csv` | `pib_nominal_MDT`, `ms_sur_pib_pct`, `source_pib` | même colonne que `pib_cnat_MDT` : 1990-1996 série 20, 1997-2001 base 1997, 2002-2004 non rattaché, 2005-2009 base 1997, 2010-2011 base 2015 rétropolée, **2012-2014 base 1997**, 2015-2024 base 2015 | `base_pib: 2015` ; `source_pib` = « Min.Fin retro (b2015) » ou « CNAT b2015 » | **non** |
| `masse-salariale-reconciliation.csv` | `pib_base2010_MDT` | 2017 : édition 2013-2017, **base 1997** ; 2019 et 2020 : base 2015 ÷ 1,06, valeur non publiée | « base 2010 (FMI/BM) » | **non** |
| `croissances-revenus-prix.csv` | taux du PIB nominal | 1962-1992 : WDI (jusqu'en 1969, valeurs qu'aucune série des Nations unies ne porte, puis série 20 : le taux de 1970 est à cheval ; ceux de 1983 et 1985 reposent sur des valeurs de 1983-1984 que la série 20 ne porte pas) ; 1993-1997 série 30 ; 1998-2001 série 100 ; 2002-2025 éditions, taux intra-édition | exacte depuis 1993 ; « non vérifié dans une même base » avant | oui, réserve à compléter |

Conséquence chiffrée de l'étiquette inexacte de 2012-2014 **[calculé]** : la part de la masse
salariale de l'État dans le PIB publiée par le précis vaut 12,30 %, 12,79 % et 13,03 % en 2012,
2013 et 2014 (PIB base 1997) ; rapportée au PIB base 2015 rétropolé de l'INS, elle vaut 11,71 %,
12,15 % et 12,35 %. Entre 2011 et 2012, la série publiée monte de 11,34 à 12,30 % : dans une base
constante, elle ne monte que de 11,34 à 11,71 % — 0,6 point de la hausse publiée vient du
dénominateur, plus petit de 5 %. Et le « reflux » de 2014 à 2015 (13,03 → 12,90) est un effet de
base : dans une base constante, la part monte de 12,35 à 12,90.

### 4.2 Inventaire des endroits où une grandeur est rapportée au PIB

| # | Volume | Chapitre | Figure, tableau ou phrase | Série du PIB | Base employée | Rétropolé | Rupture signalée | Conforme |
|---|---|---|---|---|---|---|---|---|
| 1 | Fiscalité | `_impot_revenu.qmd` | fig. rendement de l'IRPP, 1986-2025 (`figures/irpp.py`) | `irpp-ratios`, `irpp_sur_pib_pct` (PIB du ministère) | non dite | en partie (2010-2014) | seule 1990 (création de l'IRPP) | **non** |
| 2 | Fiscalité | `_impot_revenu.qmd` l. 886 | « de 1,9 % à plus de 6 % du produit intérieur brut » (1990-2016) | idem | non dite | — | non | **non** |
| 3 | Fiscalité | `_impot_societes.qmd` | fig. rendement de l'IS (`figures/impot_societes.py`) ; onglet « Données » à deux colonnes de PIB | `pib_minfin_MDT`, `pib_cnat_MDT` | non dite ; la légende dit que les deux PIB « ne divergent que pour sept exercices, dont 2012 à 2014 où l'écart atteint 5 % », sans dire que c'est un écart de base | en partie | non | **non** |
| 4 | Fiscalité | `_impot_societes.qmd` l. 326 | « de 1,86 % pour les bénéfices de 1990 à 3,77 % en 2025 » | idem | non dite | — | non | **non** |
| 5 | Fiscalité | `_tva.qmd` | fig. rendement de la TVA, 1986-2025 (`figures/tva.py`) | idem | « Le PIB retenu est celui du ministère des Finances » ; base non dite | en partie | non | **non** |
| 6 | Fiscalité | `_tva.qmd` l. 195-199 | « 6,5 % en 1988, 5,1 % en 1997, 7,3 % en 2022 et 6,8 % en 2025 » ; « 6,0 % » en 2020 | idem | non dite ; **1997 est l'année du saut de 9,8 %** | — | non | **non** |
| 7 | Fiscalité | `_droits_consommation.qmd` | fig. rendement des droits de consommation (`figures/droits_consommation.py`) | idem | idem TVA | en partie | non | **non** |
| 8 | Fiscalité | `_droits_consommation.qmd` l. 406 | « culmine au milieu des années 1990 […] maximum […] en 1994, à 3,7 % » | idem | non dite ; **le maximum est en base 1983, la suite en base 1997** : la comparaison traverse le saut de 1997 | — | non | **non** |
| 9 | Caisses | `_comptes_longue_periode.qmd` | fig-cnss-regimes, 1990-2004 (`cnss_regimes_1990_2004.py`) | `irpp-ratios`, `pib_minfin_MDT` | dite : « passage, en 1997, de la base 1983 à la base 1997 » | oui pour 1997-2001 | 1997 tracée ; **2002 non** (valeurs non rattachées 2002-2004) | partiel |
| 10 | Caisses | idem | fig-cnss-assurances-sociales, 1990-2004 | idem | idem | idem | idem | partiel |
| 11 | Caisses | idem | fig-cnss-atmp-pst, 1995-2004 | idem | idem | idem | idem | partiel |
| 12 | Cotisations | `_bilan.qmd` | fig. cotisations par branche, 1990-2004 (`cotisations_branches_1990_2004.py`) | idem | idem | idem | idem | partiel |
| 13 | Prestations | `_prestations_familiales.qmd` | fig. allocations familiales, 1990-2004 (`cnss_allocations_familiales.py`) | idem | idem | idem | idem | partiel |
| 14 | Retraites | `_secteur_prive.qmd` l. 777 | fig. branche des pensions du RSNA, 1990-2004 (`rsna_resultat_1990_2004.py`) | idem | idem | idem | idem | partiel |
| 15 | Retraites | `_secteur_prive.qmd` l. 309 et 361 | deux fig. barème d'actualisation et croissance du PIB nominal (`bareme_actualisation.py`) | `croissances-revenus-prix` | dite : « depuis 1993, chaque taux compare deux années d'une même base » | non | sans objet depuis 1993 ; réserve écrite avant, sans années | partiel : avec les niveaux de la Banque mondiale, les taux de 1983 et 1985 s'écartent de + 3,6 et − 3,0 points de ceux de la série 20 des Nations unies ; 1970 est à cheval sur deux séries |
| 16 | Rémunérations publiques | `index.qmd` | fig-masse-salariale-ratios, 1990-2025 (`masse_salariale.py`, fig. A) ; reprise dans `_demo_figure_onglets.qmd` | `masse-salariale-ratios` | dite, **à tort** : « PIB en base 2015 » | dit rétropolé, ne l'est que pour 2010-2011 | **aucune**, alors que la série en porte en 1997, 2002, 2005, 2010, 2012, 2015 | **non** |
| 17 | Rémunérations publiques | `index.qmd` l. 79 | « 11 à 12 % du PIB au début des années 1990, reflue jusqu'à environ 10 % vers 2010 […] 16,1 % en 2020 […] 13,5 % en 2025 » | idem | idem | — | non | **non** (le début est en base 1983, « vers 2010 » en base 2015 rétropolée) |
| 18 | Rémunérations publiques | `masse_salariale.py`, fig. B et figdata `fig_B_reconciliation.csv` | « Recalculé en PIB base 2010 (×1,06) » ; `FACTOR = 1.060` | `masse-salariale-reconciliation` | « base 2010 » : n'existe pas comme base nominale (§ 1.5) ; coefficient unique appliqué à 1990-2025 | — | — | **non** |
| 19 | Rémunérations publiques | `index.qmd` l. 44, 103, 117 | FMI : 17,6 % du PIB en 2020 ; Banque mondiale : 14,7 % en 2017, 10,7 % en 2010 | PIB des rapports | non dite dans le texte | — | — | **non** (à dire : FMI, base 1997, établi § 1.5 ; Banque mondiale, non relu) |
| 20 | Rémunérations publiques | `_regime_conventionnel.qmd` l. 83 | Banque mondiale : transferts aux entreprises publiques, 8,9 % du PIB en 2013, 7,5 % en 2014 | PIB du rapport | non dite | — | — | **non** |
| 21 | Finances locales | `_longue_periode.qmd` | fig-fl-lp-ressources, 1990-2023 | `cnat-pib-nominal`, édition la plus récente | dite, exacte : « base 1983 jusqu'en 2004, base 1997 de 2005 à 2014, base 2015 ensuite » | non | oui (`_ruptures_pib`) | oui |
| 22 | Finances locales | idem | fig-fl-lp-impots | idem | idem | non | oui | oui |
| 23 | Finances locales | idem | fig-fl-lp-fccl, 1985-2023 ; points de 1985-1991 rapportés au « PIB du même rapport » (Banque mondiale, 1992) | idem ; PIB du rapport pour 1985-1991 | dite pour l'INS ; non dite pour le rapport de 1992 | non | oui | oui, sauf 1985-1991 |
| 24 | Finances locales | idem | fig-fl-lp-ins, compte des collectivités locales | `cnat-pib-nominal` par base | dite : « chaque valeur est rapportée au PIB de sa propre base » | non | oui, deux points par année commune | oui |
| 25 | Finances locales | `_longue_periode.qmd` l. 73 | « de 0,74 % en 2002 à 0,61-0,64 % en 2008-2010 […] 0,41 % en 2011 […] 0,66 % en 2019 » | idem | dite au § des ruptures, pas dans la phrase : 2002 en base 1983, 2008-2011 en base 1997, 2019 en base 2015 | non | — | partiel |

**Bilan** : 25 emplois relevés (17 figures ou groupes de figures, 8 phrases chiffrées) dans six
volumes ; aucun dans « Marché du travail » ni dans les deux autres figures de longue période des
finances locales (autonomie, caisse des prêts), qui n'ont pas de vue au PIB. **Conformes : 4** (les quatre figures des finances
locales). **Partiels : 8** (six figures de la CNSS 1990-2004, où 1997 est tracée mais non 2002 ;
les figures du barème d'actualisation, pour 1970 et 1983-1985 ; une phrase des finances
locales). **Non conformes :
13** : les quatre figures de rendement de la fiscalité et leurs quatre phrases, la figure de la masse
salariale, sa phrase et sa « réconciliation », et les deux passages qui citent le FMI et la Banque
mondiale.

`finances_locales.py` (`_pib`, `_pib_par_base`, `_ruptures_pib`) est le modèle à généraliser : il
lit la base dans la série, rapporte chaque valeur au PIB de sa base et trace les changements.

### 4.3 Ce qu'il faudra corriger en amont (constats pour `tunisia-data`, hors précis)

1. `catalog.yml`, `masse-salariale-ratios` : `base_pib: 2015` est inexact ;
   `docs/hypotheses-series-masse-salariale.md`, hypothèse H3 (« base 2015 homogène », « pas de
   rupture de base sur 1990-2025 », « 2012-2024 : CNAT base 2015 ») est contredite : les valeurs
   2012-2014 sont celles des éditions en base 1997. `docs/compensation-ratios.md` (branche
   `data/compensation-serie-longue`) l'avait relevé pour 2010-2014 et 2002-2004 ; il qualifiait
   2010-2014 de « non rattachée » : elle se rattache au classeur de l'INS du 15 août 2021.
2. `irpp-ratios`, colonne `pib_cnat_MDT` : même défaut pour 2012-2014.
3. `masse-salariale-reconciliation` et `docs/reconciliation-masse-salariale-pib.md` : « base 2010 »
   à renommer ; le facteur 1,06 n'est mesuré que sur 2015-2017.
4. Série à créer : le PIB en base 2015 de 2010 à 2020 du classeur de l'INS (§ 6).
5. `sources/ins-comptes-nationaux-publications.md` s'intitule « publications, base 2015 » alors que
   treize des dix-neuf éditions sont en base 1983 ou 1997.

---

## 5. Ce qui reste non établi, et où chercher

| # | Lacune | Où chercher |
|---|---|---|
| L1 | Comptes d'avant la base 1983 : producteur, système, années de référence ; s'il a existé des « bases » nommées | Rapports annuels de la BCT 1959-1985 (les agrégats y sont « aux prix de 1957 », « de 1960 », « prix constants de 1966 » — rapport 1973, p. 3 —, « de 1972 » — rapport 1981, p. 64 —, « de 1980 » — rapport 1989, p. 56) ; mémorandums de la Banque mondiale de 1985 (`wb_1985_5328_cem_b.pdf` : comptes « in 1980 prices », source « Ministry of Plan ») ; annuaire des statistiques des comptes nationaux des Nations unies ; les fichiers `wb_1978_2201_cem.pdf` et `wb_1981_3399_cem.pdf` n'ont pas de couche texte (OCR à faire) |
| L2 | Date et publication d'entrée en service de la base 1983 ; volumes n° 1 à 10 des *Comptes de la nation* | Bibliothèque de l'INS ; rapports de la BCT 1990-1993  ; recherche R1 ci-dessous |
| L3 | Profondeur de la rétropolation de la base 1983 (la série 20 des Nations unies, 1970-1997, en est-elle une ?) | Notes par série de l'annuaire des Nations unies ; volumes anciens de l'INS |
| L4 | Contenu du CD de l'édition 2005-2009 (comptes 1997-2007 en base 1997) | INS ; à défaut, UNdata série 100 fait foi pour le seul PIB |
| L5 | Méthode de la rétropolation 2010-2014 en base 2015 ; existence d'une rétropolation avant 2010 | « Une note méthodologique plus complète accompagne la publication des résultats » (note du 15 août 2021, p. 3, n. 1) : non identifiée ; portail de données de l'INS (accès fermé)  ; recherche R2 ci-dessous |
| L6 | Mention de la base du PIB dans la revue des dépenses publiques de la Banque mondiale (2020) ; date exacte et support de la diffusion de « début 2010 » de la base 1997 | Le rapport de la Banque mondiale, à relire ; pour le FMI, la question est close (§ 1.3 et 1.5 ; imf.org refusant le téléchargement automatique, les deux rapports ont été pris dans les archives du web, § 7.2) |
| L7 | Origine des valeurs 2002-2004 du PIB du ministère des Finances (32 112,0 ; 34 630,0 ; 37 601,2) | Lois de finances et rapports sur le budget 2003-2006 ; budgets économiques |
| L8 | PIB en base 1997 définitif pour 2018-2020 | Communiqués trimestriels de l'INS de 2019-2021 ; la page `les-comptes-de-la-nation-en-2018` n'expose aucun PDF |
| L9 | Termes arabes de « rétropolation » et de « changement de base » | Version arabe du communiqué du 15 août 2021 (l'adresse `/ar/publication/les-comptes-nationaux-changent-de-base` renvoie 404) ; rapport annuel de la BCT en arabe (aucun dans l'entrepôt) |

### Recherches infructueuses

Aucune fiche de `docs/recherches.yml` ne porte sur les comptes nationaux
(`scripts/recherches.py lister`, 6 octobre 2026). **Les deux recherches ci-dessous ne peuvent pas
entrer au registre** : son schéma n'admet que des requêtes sur le *Journal officiel*
(`titres_fts`, `titres_like`, `iort_ar`, `plein_texte` des fascicules) et des sources de passe
closes (`jort_cache`, `iort`, `corpus_local`, `pist`, `mcp_jort`, `visas`, `presse`) ; or elles
portent sur des publications statistiques. Elles restent donc ici, dans la forme du registre, et
l'annexe n'aura pas d'ancre `RECHERCHE` pour elles. Si l'humain veut les y verser, il faut d'abord
étendre `scripts/recherches.py`.

**R1 — première publication des *Comptes de la nation* en base 1983** (volumes n° 1 à 10) et date
d'entrée en service du système.

- Requêtes lancées : expression régulière
  `base (19|20)[0-9]{2}|ann[ée]e de base|changement de base|r[ée]tropol|SCN ?(68|93|1968|1993|2008)|syst[èe]me de comptabilit`
  sur le texte (`pdftotext -layout`) des dix-neuf éditions de
  `R/ins-publications/comptes-de-la-nation/` ; expression
  `syst[èe]me (des|de) compt(es|abilit[ée]) nation|ancien syst[èe]me|nouveau syst[èe]me (de|des) compt|base (19|20)[0-9]{2}|changement de base|rebasage|ann[ée]e de base|r[ée]tropol`
  sur le texte des rapports annuels de la BCT 1985-2025 (`R/bct-archives/109/`).
- Passe du 2026-10-06, documentaliste. Résultat : aucun. Couverture : éditions 2001-2005
  (déc. 2006) à 2021-2025 (« Edition 2026 ») ; aucune édition antérieure dans l'entrepôt. BCT :
  seul le rapport 1992 répond (pp. 43, 52, 98) ; les rapports 1959-1984 n'ont été interrogés que
  sur « prix (constants) de AAAA » et « comptabilité nationale ». Non lus : rapports de la Banque
  mondiale de 1978 et 1981 (sans couche texte). Couvert jusqu'au : 2026-10-06 pour l'entrepôt tel
  qu'il est ce jour.

**R2 — note méthodologique de la base 2015 décrivant la rétropolation 2010-2014**, et toute série
en base 2015 antérieure à 2010.

- Requêtes lancées : recherche web « INS Tunisie comptes nationaux base 2015 rétropolation séries
  2010-2014 "base 2015" PIB révisé changement de base » ; expression `r[ée]tropol` sur le texte des
  six éditions en base 2015 et des rapports de la BCT 2020-2025 (aucune occurrence) ; lecture de la
  page `https://ins.tn/publication/les-comptes-nationaux-changent-de-base` et de ses deux pièces.
- Passe du 2026-10-06, documentaliste. Résultat : aucun pour la note méthodologique et pour les
  années antérieures à 2010 ; trouvé, le classeur 2010-2020 (`ins-pib-base-2015-2010-2020`, § 7.2).
  Couverture : site de l'INS par ces seules pages ; portail de données de l'INS non interrogé
  (accès fermé) ; UNdata, tableaux 1.1 et 4.1 : série 1000 à partir de 2015 seulement. Couvert
  jusqu'au : 2026-10-06.

---

## 6. Plan proposé pour l'annexe (`precis/fr/annexe-pib.qmd`)

Page de site au niveau de `a-propos.qmd`, à déclarer dans les deux `_quarto.yml` (l'arabe à la
main, une fois la traduction livrée). Ancres stables, pour qu'une légende de figure puisse y
renvoyer.

1. **Pourquoi cette annexe** (`#sec-pib-pourquoi`) — trois phrases : toute part du PIB dépend du PIB
   retenu ; les comptes tunisiens ont changé deux fois de base ; l'INS dit lui-même que les ratios
   sont « mécaniquement tirés vers le bas ».
2. **Ce qu'est une base** (`#sec-pib-base`) — définition de l'INS (édition 2015-2020, p. 11) ;
   distinguer la **base des comptes** (niveaux, concepts, sources) de l'**année de prix** des
   volumes (1990, 2005, 2010, 2015) ; pourquoi on change (norme internationale, nomenclatures,
   sources, informel).
3. **Les bases successives** (`#sec-pib-bases`) — le tableau du § 1.1, puis un paragraphe par base
   (§ 1.2-1.4) ; un encadré « la "base 2010" n'en est pas une » (§ 1.5).
4. **Les écarts de niveau** (`#sec-pib-ecarts`) — **figure** : PIB aux prix courants par base sur
   les années de recouvrement, 1997-2017, trois courbes non raccordées (base 1983, base 1997, base
   2015 en trait plein à partir de 2015 et en tireté pour 2010-2014 rétropolé), avec un second
   panneau ou un onglet « écart en % » ; onglet « Données » = tableaux des § 2.1 et 2.2 ; une phrase
   sur les révisions intra-base (§ 2.5).
5. **La rétropolation** (`#sec-pib-retropolation`) — ce que l'INS a recalculé (1997-2004 en base
   1997 ; 2010-2014 en base 2015), où, et ce qui ne l'est pas (rien avant 1997 en base 1997, rien
   avant 2010 en base 2015) ; conséquence : **aucune série de PIB tunisien n'est homogène de 1990 à
   aujourd'hui**.
6. **Quel PIB dans quelle source** (`#sec-pib-sources`) — le tableau du § 3, réduit aux sources que
   le précis cite ; mise en garde sur les séries accolées (ministère des Finances, Banque mondiale).
7. **Comment le précis signale une rupture de série** (`#sec-pib-ruptures`) — la convention :
   légende qui nomme la base et dit « rétropolé » ou « non rétropolé » ; trait vertical
   (`figtools.marque_rupture`) aux années de changement ; jamais de raccord ; une année publiée dans
   deux bases porte deux points ; renvoi à cette annexe.
8. **Comment lire une part du PIB** (`#sec-pib-lire`) — court : la règle de trois du § 2.4 et son
   tableau ; l'exemple de l'INS (déficit 2020 : 11,8 % → 11,1 % ; dette : 88,6 % → 83,5 %) ; ne pas
   comparer une part d'avant et d'après un changement sans le dire.

Ton : documentaire. Pas de nom de fichier, de script ni de modèle dans le texte rendu.

## 7. Références

### 7.1 Déjà présentes

| Clé | Où | Remarque |
|---|---|---|
| `ins-cnat-2015` | `precis/fr/references.json`, `precis/ar/references.json` | couvre les dix-neuf éditions ; pour l'annexe, citer avec localisateur (« éd. 2015-2020, p. 11 ») |
| `undata-sna` | `precis/{fr,ar}/retraites/references.json` | à remonter au niveau commun ; son titre ne vise que le tableau 4.1 : l'annexe emploie aussi le tableau 1.1 (séries 10 et 20) |
| `wb-wdi` | `precis/{fr,ar}/retraites/references.json` | à remonter au niveau commun |
| `bct-ra` | `marche_travail`, `remunerations_publiques`, `retraites` (fr et ar) | à remonter au niveau commun ; citer avec millésime et page |
| `minfin-indicateurs-fp` | `precis/{fr,ar}/references.json` | URL générique : à préciser par le bibliographe |
| `imf-tunisia-art4-2020` | `remunerations_publiques` (fr et ar) | c'est le rapport n° 21/44 (adresse `1tunea2021001`) ; son titre imprimé est « 2021 Article IV Consultation » (février 2021), non « 2020 » : à signaler au bibliographe. Base du PIB établie (§ 1.5) |
| `wb-tunisia-per-2020` | `remunerations_publiques` (fr et ar) | base du PIB à relire (L6) |

### 7.2 À créer (ébauches CSL-JSON)

Publications récupérées le 6 octobre 2026 et déposées dans
`~/projets/tunisia-data/data/raw/ins-publications/comptes-de-la-nation/` (répertoire ignoré par git :
`.gitignore:24:data/raw/ins-publications/`). **Écart à la consigne** : le répertoire désigné,
`data/raw/ins-comptes-nationaux-publications/`, est **versionné** (ses PDF sont suivis par git,
`git check-ignore` n'y répond rien) ; rien n'y a été laissé.

| Fichier déposé | Adresse | SHA-256 |
|---|---|---|
| `INS_2021-08-15_note_changement_de_base_2015.pdf` (4 p.) | `https://ins.tn/sites/default/files-ftp3/files/publication/pdf/15082021%20SCNT%20Base%202015%20Document%20synthese.pdf` | `499e51976ec5bce54cac0b4ddd0bbd09706787a6b7943f73d79dde325490de34` |
| `INS_2021-08-15_donnees_annuelles_base_2015_2010-2020.xlsx` | `https://ins.tn/sites/default/files-ftp3/files/publication/pdf/Données%20anuelles_2.xlsx` | `7e3737f84ad701d1df7c4c7bea1687df34c7f8374d0f1920d05f08bf10fbf43c` |
| `INS_2021-03_cnat_presentation_SCNT97.pdf` (25 p. ; préface et méthodologie de l'édition 2008-2012, base 1997 ; non cité, gardé pour mémoire) | `https://www.ins.tn/sites/default/files-ftp3/files/2021-03/cnat-presentation.pdf` | `43873eec90f16205239d3453094ef62cc20d7b63333c81826f866b44408e324a` |

| `R/banque-mondiale-rapports/imf_2021_044_art4_tunisia.pdf` (FMI, rapport n° 21/44) | `https://web.archive.org/web/20211114144956id_/https://www.imf.org/-/media/Files/Publications/CR/2021/English/1TUNEA2021001.ashx` | `f6f6792d2a60e7f65f92a9ca509ee7a8cc73a13c4074c97caf06e6594ad7c16e` |
| `R/banque-mondiale-rapports/imf_2010_282_art4_tunisia.pdf` (FMI, rapport n° 10/282) | `https://web.archive.org/web/20110804234937id_/http://www.imf.org/external/pubs/ft/scr/2010/cr10282.pdf` | `be97d6a7663780686a936a9bcbb795924c55216e525d7476ac48dc6cc9c70d56` |
| `R/undata/sna_101_tunisie_AAAA.html` (64 pages, 1960-2023) | adresse du § 2.3 | non relevée (pages dynamiques) |

Les deux rapports du FMI sont dans `R/banque-mondiale-rapports/`, ignoré par git, où l'entrepôt
range déjà les rapports du FMI ; imf.org répondant 403, ils viennent des archives du web.

Page d'accueil des deux premiers : `https://ins.tn/publication/les-comptes-nationaux-changent-de-base`
(date affichée : 15-08-2021).

Français :

```json
[
  {
    "id": "ins-changement-base-2015",
    "type": "report",
    "title": "Les comptes nationaux changent de base. Note explicative du changement de base des comptes nationaux tunisiens, base 2015",
    "title-short": "INS, Les comptes nationaux changent de base",
    "author": [{"literal": "Institut national de la statistique"}],
    "publisher": "Institut national de la statistique, Tunisie",
    "publisher-place": "Tunis",
    "issued": {"date-parts": [[2021, 8, 15]]},
    "number-of-pages": "4",
    "language": "fr",
    "URL": "https://ins.tn/publication/les-comptes-nationaux-changent-de-base",
    "accessed": {"date-parts": [[2026, 10, 6]]},
    "note": "citation-key: ins-changement-base-2015\nCommuniqué du 15 août 2021, accompagné d'une note de quatre pages et d'un classeur « Données » qui porte le PIB et ses emplois en base 2015 de 2010 à 2020."
  },
  {
    "id": "ins-pib-base-2015-2010-2020",
    "type": "dataset",
    "title": "Comptes nationaux annuels en base 2015, 2010-2020 : valeur ajoutée par secteur et emplois du PIB, aux prix courants et aux prix de l'année précédente",
    "title-short": "INS, Comptes annuels en base 2015, 2010-2020",
    "author": [{"literal": "Institut national de la statistique"}],
    "publisher": "Institut national de la statistique, Tunisie",
    "publisher-place": "Tunis",
    "issued": {"date-parts": [[2021, 8, 15]]},
    "language": "fr",
    "URL": "https://ins.tn/publication/les-comptes-nationaux-changent-de-base",
    "accessed": {"date-parts": [[2026, 10, 6]]},
    "note": "citation-key: ins-pib-base-2015-2010-2020\nClasseur « Données » joint au communiqué du 15 août 2021 ; le titre est descriptif, le fichier n'en porte pas. Seule publication lue qui donne 2010-2014 en base 2015."
  }
]
```

Troisième entrée à créer, identique dans les deux langues (document en anglais ; en arabe,
`publisher` : « صندوق النقد الدولي ») :

```json
{
  "id": "imf-tunisia-art4-2010",
  "type": "report",
  "title": "Tunisia: 2010 Article IV Consultation — Staff Report; Public Information Notice on the Executive Board Discussion; and Statement by the Executive Director for Tunisia",
  "title-short": "FMI, Tunisia: 2010 Article IV Consultation",
  "author": [{"literal": "International Monetary Fund"}],
  "collection-title": "IMF Country Report",
  "number": "10/282",
  "publisher": "Fonds monétaire international",
  "publisher-place": "Washington, D.C.",
  "issued": {"date-parts": [[2010, 9]]},
  "language": "en",
  "URL": "https://www.imf.org/external/pubs/ft/scr/2010/cr10282.pdf",
  "accessed": {"date-parts": [[2026, 10, 6]]},
  "note": "citation-key: imf-tunisia-art4-2010\nAnnexe 5, « Tunisia's New National Accounts » : adoption début 2010 de comptes 1997-2008 conformes au SCN 1993, PIB nominal relevé d'environ 10 %, tableau des deux séries 2002-2008. Lu dans la copie des archives du web du 4 août 2011."
}
```

Arabe (mêmes clés ; l'INS ne publie pas ce communiqué en arabe à l'adresse correspondante : le
titre reste en français, la note est traduite — à valider par le relecteur-ar) :

```json
[
  {
    "id": "ins-changement-base-2015",
    "type": "report",
    "title": "Les comptes nationaux changent de base. Note explicative du changement de base des comptes nationaux tunisiens, base 2015",
    "title-short": "المعهد الوطني للإحصاء، تغيير سنة أساس الحسابات القومية",
    "author": [{"literal": "المعهد الوطني للإحصاء"}],
    "publisher": "المعهد الوطني للإحصاء، تونس",
    "publisher-place": "تونس",
    "issued": {"date-parts": [[2021, 8, 15]]},
    "number-of-pages": "4",
    "language": "fr",
    "URL": "https://ins.tn/publication/les-comptes-nationaux-changent-de-base",
    "accessed": {"date-parts": [[2026, 10, 6]]},
    "note": "citation-key: ins-changement-base-2015\nبلاغ بتاريخ 15 أوت 2021 (بالفرنسية)، مرفق بمذكّرة من أربع صفحات وبجدول بيانات يتضمّن الناتج المحلي الإجمالي واستخداماته حسب أساس 2015 من 2010 إلى 2020."
  },
  {
    "id": "ins-pib-base-2015-2010-2020",
    "type": "dataset",
    "title": "Comptes nationaux annuels en base 2015, 2010-2020",
    "title-short": "المعهد الوطني للإحصاء، الحسابات السنوية حسب أساس 2015، 2010-2020",
    "author": [{"literal": "المعهد الوطني للإحصاء"}],
    "publisher": "المعهد الوطني للإحصاء، تونس",
    "publisher-place": "تونس",
    "issued": {"date-parts": [[2021, 8, 15]]},
    "language": "fr",
    "URL": "https://ins.tn/publication/les-comptes-nationaux-changent-de-base",
    "accessed": {"date-parts": [[2026, 10, 6]]},
    "note": "citation-key: ins-pib-base-2015-2010-2020\nجدول البيانات المرفق ببلاغ 15 أوت 2021؛ العنوان وصفي."
  }
]
```

Au bibliographe : `undata-sna` gagnerait une mention du tableau 1.1
(`https://data.un.org/Data.aspx?d=SNA&f=group_code%3a101%3bcountry_code%3a788%3bfiscal_year%3a1997`,
consulté le 6 octobre 2026) ; `wb-wdi`, celle des métadonnées du pays
(`https://api.worldbank.org/v2/sources/2/country/TUN/metadata?format=json`, même date).

## 8. Notions à glossaire

Aucune n'est dans `precis/glossaire.yml` (recherche `PIB|base|rétropol|prix courants`). Le
glossaire rend aujourd'hui « comptes nationaux » par « الحسابات الوطنية » ; le site arabe de l'INS
écrit **les deux** : « الحسابات القومية الثلاثية (الأساس 2015) » et « الحسابات الوطنية 2015-2020
(سنة الاساس 2015) » (`https://www.ins.tn/ar/statistiques/72`, lu le 6 octobre 2026) — au
terminologue de trancher.

| Terme FR | Terme AR | Attestation de l'arabe | Source canonique de la définition |
|---|---|---|---|
| produit intérieur brut (PIB) | الناتج المحلي الإجمالي | INS, site arabe, page citée **[lu]** | INS, *Comptes de la nation* |
| PIB aux prix courants ; aux prix du marché | الناتج المحلي الإجمالي بالأسعار الجارية ؛ بأسعار السوق | non attesté dans un document arabe lu (forme du catalogue de `tunisia-data`) | ligne « Produit Intérieur Brut (p.m) » des éditions |
| base des comptes nationaux ; année de base | الأساس ؛ سنة الأساس | INS, site arabe : « (الأساس 2015) », « سنة الاساس 2015 » **[lu]** | INS, éd. 2015-2020, p. 11 |
| changement de base (rebasage) | تغيير سنة الأساس | non attesté pour les comptes nationaux dans un document officiel lu (la presse l'emploie pour l'indice des prix) | INS, note du 15 août 2021, p. 1 |
| rétropolation | — | **non attesté** | à définir d'après l'INS : « de nouvelles estimations sont publiées pour le passé » ; le mot « rétropolation » n'apparaît dans aucun texte de l'INS lu |
| système de comptabilité nationale (SCN 1968, 1993, 2008) ; SCNT | نظام الحسابات القومية | non attesté dans un document tunisien lu | Nations unies ; INS |
| prix constants ; prix de l'année précédente ; année de prix | — | non attesté | INS, éd. 2005-2009, p. 3 |
| rupture de série | — | non attesté | convention du précis |
| économie informelle (secteur informel) | — | non attesté | INS, éd. 2015-2020, p. 20 (définition citée au § 1.4) |

## 9. Séries de `tunisia-data` à snapshoter pour la figure

| Série | Fichier | Emploi | État |
|---|---|---|---|
| `cnat-pib-nominal` | `P/ins-comptes-nationaux/pib_nominal_editions.csv` (`edition`, `base`, `annee`, `valeur`) | bases 1983 (2001-2008), 1997 (2005-2017), 2015 (2015-2025) ; révisions intra-base | **déjà au cache** (`precis/_seriescache/cnat-pib-nominal.csv`) |
| `undata-pib` | `P/ins-comptes-nationaux/pib_undata.csv` (`annee`, `serie`, `systeme`, `valeur_mdt`) | base 1983 de 1992 à 2009, base 1997 de 1997 à 2011 : le recouvrement 1997-2004 n'existe que là | **à snapshoter** ; s'arrête à 2011 pour la série 100 (tableau 4.1), les éditions prennent le relais |
| à créer : PIB en base 2015, 2010-2020, classeur de l'INS du 15 août 2021 | fichier brut déposé (§ 7.2) ; série et entrée de catalogue à écrire dans `tunisia-data` (clé proposée `ins-pib-base2015-retropole`) | le segment rétropolé 2010-2014 | **à créer en amont**, puis à snapshoter |
| facultatif : UNdata, tableau 1.1, séries 10 et 20 | à extraire (le script de l'entrepôt ne lit que le tableau 4.1) | PIB de 1960 à 1996 tel que transmis aux Nations unies, pour un tableau « avant 1997 » | à créer si l'annexe remonte avant 1992 |
| `wdi-tunisie` | `P/banque-mondiale/wdi_tunisie.csv` | montrer l'accolage (sauts de 1997 et 2010) dans « quel PIB dans quelle source » | pas au cache sous ce nom |
| `irpp-ratios` (`pib_minfin_MDT`) | `P/precis/irpp_ratios_1986_2025.csv` | idem pour le ministère des Finances | déjà au cache |

Les figures lisent `figtools.series()` ; aucune ne doit lire l'entrepôt directement.
