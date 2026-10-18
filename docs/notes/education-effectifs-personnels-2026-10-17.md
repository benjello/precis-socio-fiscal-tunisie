# Effectifs des personnels de l'éducation : note documentaire (figure 7.4)

Note du documentaliste, 17 octobre 2026, branche `chantier/education-v1`. Elle sert la section
`sec-educ-depense-personnels` de `precis/fr/education/_depense.qmd`, figure `fig-educ-enseignants`
(`figdata/fig_educ_depense_enseignants.csv`). La figure rapporte aujourd'hui la masse salariale de tout
le ministère (tableau 16.9 de l'Annuaire) au nombre d'enseignants du public. La note cherche de quoi
remplacer ce ratio. Aucun `.qmd`, aucun `references.json`, aucun `glossaire.yml` n'est modifié.

Les séries sont dans `docs/notes/education-depense-series/`, fichiers `personnels-*.csv`, avec les
colonnes des CSV voisins (`annee, valeur, unite, source, page`). La colonne `source` donne l'édition,
le tableau, la ligne, la colonne et le stade comptable. La colonne `page` donne la page imprimée.
Elle est vide pour les classeurs Excel de l'INS, qui n'ont pas de pagination ; la feuille est
alors indiquée dans `source`.

Les budgets du ministère des Finances sont en arabe et leur couche texte est en formes de présentation
arabes. Elle a été lue après normalisation NFKC (`pdftotext -layout`, puis `unicodedata.normalize`).
Les scripts sont hors dépôt, dans le dossier temporaire de la session. Toutes les valeurs ont été
relevées sur la page citée. Aucune n'a été lue à l'image.

---

## 0. Résultat en bref

| Question | Réponse | Fichiers |
|---|---|---|
| (1) Agents des ministères, par année | **Trouvé.** INS (base INSAF) : Éducation et Enseignement supérieur, 2010-2020 (annexes annuelles), puis 2018-2025 (rapport d'août 2026, tableau 8, p. 11). Budgets de l'État : postes occupés et autorisés de l'Éducation, 2012-2017 ; de l'Enseignement supérieur, 2012-2013 et 2015-2017. **La formation professionnelle n'a pas de ligne propre à l'INS.** Le budget 2013 la chiffre (8 352 postes), puis plus rien n'a été trouvé. | `personnels-ins-agents-*`, `personnels-budget-*-total-agents.csv`, `personnels-budget-education-en-fonction-*`, `personnels-budget-education-autorises-*` |
| (2) Enseignants en ETP | **Introuvable.** Aucune source lue ne donne d'ETP. On a trouvé : la répartition **statutaires / contractuels à plein temps** du supérieur, 2004-2005 à 2023-2024 (Annuaire de l'INS). On a aussi la part des permanents parmi les enseignants universitaires, 2009-2015 (budget GBO 2013). Les **vacataires** n'apparaissent dans aucune série. Le nombre d'enseignants du supérieur de la figure 7.4 correspond aux enseignants **à plein temps** (statutaires et contractuels). Les totaux sont égaux de 2004-2005 à 2017-2018 et en 2022-2023 et 2023-2024. Ils diffèrent en 2018-2019 (21 823 contre 21 880) et en 2021-2022 (23 498 contre 23 489). 2020-2021 est décalé d'une année (§ 3.1). | `personnels-ins-superieur-plein-temps-*`, `personnels-budget-esrs-enseignants-*` |
| (3) Masse salariale par programme, enseignants séparés | **Non.** Les budgets ventilent la rémunération par programme et sous-programme, et par paragraphe : permanents ou non permanents, traitement de base, indemnités, cotisations. **Ils ne la ventilent pas par corps.** Aucune rémunération des seuls enseignants n'est publiée. | — |

Ce qui devient calculable (§ 5) :

- **la rémunération par agent** de chaque ministère, pour les années où le tableau 16.9 existe entre 2010 et 2023 : masse salariale du tableau 16.9
  rapportée aux agents INSAF du même ministère. Le rapprochement est contrôlé pour 2020 : le salaire
  moyen INS × 12 × effectif redonne 96,6 % de la masse salariale budgétaire de l'Éducation et 94,0 %
  de celle de l'Enseignement supérieur ;
- **la rémunération par poste budgétaire** de l'Éducation, 2012-2017, avec la masse et les postes tirés
  du même document ;
- **pas la rémunération par enseignant**, ni à plus forte raison par enseignant ETP. On ne peut publier
  que la **part des enseignants dans les postes** : environ 76 % à l'Éducation de 2013 à 2016, 43 à 52 %
  dans la partie Enseignement supérieur du budget.

---

## 1. Le nombre d'agents des ministères (INS, base INSAF)

### 1.1 La série `ins-ministere-effectifs-2018-2025` retrouvée

- **Où** : catalogue `~/projets/tunisia-data/catalog.yml`, entrée `ins-ministere-effectifs-2018-2025`.
  Fichier traité : `data/processed/ins-fonction-publique-2018-2025/ministere_effectifs.csv`, construit par
  `scripts/extract_ins_fonction_publique_2018_2025.py`. Fiche : `sources/ins-fonction-publique-2018-2025.md`.
- **Édition** : INS, *Évolution des effectifs et des rémunérations des agents de la fonction publique
  tunisienne 2018-2025*, août 2026 (métadonnées du PDF : 10 août 2026), 19 p. Page :
  <https://www.ins.tn/publication/evolution-des-effectifs-et-des-remunerations-des-agents-de-la-fonction-publique>.
  PDF : <https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/La%20fonction%20publique%20-%202018-2025.pdf>.
  Copie locale : `tunisia-data/data/raw/ins-fonction-publique-2018-2025/La fonction publique - 2018-2025.pdf`, hors git.
- **Tableau** : tableau 8, « Évolution des effectifs de la fonction publique par ministère, 2018-2025 »,
  **p. 11** (page imprimée et page PDF). Sous le tableau : « Source : Base INSAF, données administratives
  de la fonction publique ». Effectif de décembre (le rapport le précise pour 2025, p. 4).
- **Valeurs relues sur la page** (agents) :

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ministère de l'Éducation | 194 430 | 194 178 | 195 391 | 196 700 | 196 354 | 195 779 | 191 054 | 197 836 |
| Ministère de l'Enseignement supérieur | 34 465 | 33 982 | 33 832 | 34 363 | 33 561 | 33 564 | 32 371 | 32 181 |
| Total fonction publique | 652 225 | 658 881 | 664 195 | 669 290 | 664 727 | 659 008 | 647 155 | 652 498 |

- La formation professionnelle n'a pas de ligne. Les quatorze entités sont : Présidence, Défense,
  Intérieur, Justice, Finances, Agriculture, Équipement, Jeunesse et sports, Santé, Éducation,
  Enseignement supérieur, Affaires sociales, collectivités locales, autres établissements.
- Le texte du rapport (p. 10, puis p. 11) dit que l'Éducation est « le principal département en termes
  d'effectifs avec 197836 » agents en 2025. Il dit aussi que l'Enseignement supérieur « enregistre une
  baisse sur la période ». En 2025, l'Éducation a le plus fort solde positif d'entrées et sorties :
  + 6 787 agents (p. 13, figure non chiffrée en tableau).
- **Clé de citation** : `ins-fonction-publique-2025`. Elle est dans
  `precis/fr/remunerations_publiques/references.json` mais pas dans `precis/fr/references.json` ni dans
  `precis/fr/education/references.json`. Il faut la verser au fonds commun (entrée CSL au § 7). C'est
  le TODO du bibliographe à la ligne 345 de `_depense.qmd`.

### 1.2 Les années 2010-2020 : annexes annuelles (clé `ins-fonction-publique-2021`, déjà au fonds commun)

Source : INS, *Caractéristiques des agents de la fonction publique et leurs salaires 2010-2021*,
annexes annuelles, tableau 1 « La distribution des agents de la fonction publique selon le ministère
ou l'établissement et le sexe ». Il s'agit de classeurs Excel, sans pagination. Les copies locales sont
dans `tunisia-data/data/raw/ins-fonction-publique-salaires-2010-2021/`. Il y a un fichier par année :
`AnnexeAAAA.xlsx` pour 2010-2014 et 2020, `annexeAAAA.xls` pour 2015-2019.

| Année | Éducation | Enseignement supérieur | Total |
|---|---:|---:|---:|
| 2010 | 181 560 | 33 027 | 417 924 |
| 2011 | 182 015 | 31 878 | 439 416 |
| 2012 | 185 100 | 34 584 | 537 066 |
| 2013 | 188 212 | 36 854 | 563 060 |
| 2014 | 190 711 | 36 242 | 571 742 |
| 2015 | 191 047 | 35 954 | 601 908 |
| 2016 | 197 884 | 35 856 | 622 442 |
| 2017 | 196 729 | 35 623 | 642 918 |
| 2018 | 194 430 | 34 384 | 652 225 |
| 2019 | 194 178 | 33 902 | 658 881 |
| 2020 | 195 390 | 33 752 | 664 184 |

- **2017** : l'annexe replie la Défense, l'Intérieur et les collectivités locales dans « Autres
  ministères » (231 590 agents). Les lignes Éducation et Enseignement supérieur restent séparées
  (feuille `tab1` de `annexe2017.xls`). **2018** : feuille `tab1` de `annexe2018.xls`, quatorze lignes.
  `tab11` (série reconstituée par l'INS, en milliers ; `ins-ministere-effectifs` au catalogue) donne
  196,7 et 194,4 milliers pour l'Éducation, 35,5 et 34,4 pour l'Enseignement supérieur, en accord avec ces
  annexes.
- **Rupture 2011-2012** : avant 2012, l'Intérieur ne compte pas les forces de sécurité, d'où le saut du
  total. La rupture ne touche pas les lignes Éducation et Enseignement supérieur.
- **Concordance avec le rapport 2025** (§ 1.1) : l'Éducation concorde à l'unité ou presque (2019 :
  194 178 dans les deux sources ; 2020 : 195 390 contre 195 391). L'Enseignement supérieur ne concorde
  pas exactement : 34 384 contre 34 465 en 2018, 33 902 contre 33 982 en 2019, 33 752 contre 33 832 en 2020, 34,285 milliers (`tab11`)
  contre 34 363 en 2021. Pour une série longue de l'Éducation, on peut prendre les annexes jusqu'en 2017,
  puis le rapport 2025 à partir de 2018, en le disant. Pour le supérieur, le raccord crée une marche
  d'environ 80 agents.
- CSV : `personnels-ins-agents-education-annexes-2010-2020.csv`,
  `personnels-ins-agents-enseignement-superieur-annexes-2010-2020.csv`,
  `personnels-ins-agents-education-2018-2025.csv`, `personnels-ins-agents-enseignement-superieur-2018-2025.csv`.

### 1.3 Agents par corps enseignant, tous ministères, 2015-2018 (INSAF)

Les annexes 2015 à 2019 portent un tableau 11, « La distribution des agents de la fonction publique
selon le corps et le sexe ». C'est la seule source INSAF qui isole les enseignants. Elle couvre toute
la fonction publique, pas un ministère.

| Corps (ligne du tableau 11) | 2015 | 2016 | 2017 | 2018 |
|---|---:|---:|---:|---:|
| Enseignants de l'enseignement primaire (سلك التعليم الابتدائي) | 66 400 | 67 909 | 66 298 | 65 163 |
| Enseignants de l'enseignement secondaire (سلك التعليم الثانوي) | 81 626 | 82 128 | 81 288 | 78 830 |
| Enseignants de l'enseignement supérieur (سلك التعليم العالي) | 12 589 | 12 825 | 12 827 | 12 436 |
| Surveillants du ministère de l'Éducation (سلك القيّمين) | 11 725 | 12 050 | 12 032 | 12 010 |

Réserves :

- **2018** : les colonnes sont inversées (pourcentages d'abord). La première ligne (« سلك الإطار
  المشترك », libellée en français « Corps médical ») porte 11 020, comme la ligne du corps médical.
  Les trois lignes enseignantes sont cohérentes avec 2017. **À vérifier au fichier.**
- **2019 est écartée** : libellés et valeurs sont décalés. La ligne « سلك متفقدي المصالح المالية »
  porte 114 657 agents, l'ordre de grandeur des ouvriers. Le total du tableau (658 670) diffère de celui
  du tableau 1 (658 881).
- Les annexes 2010-2014 et 2020 n'ont pas ce tableau.
- Les corps du primaire et du secondaire concordent avec les postes budgétaires du ministère de
  l'Éducation (§ 2.1) : 66 400 enseignants du primaire à l'INSAF en 2015, contre 66 898 postes occupés
  fin 2015 au budget. Le corps du supérieur (environ 12 600) est **bien inférieur** aux 20 478
  « statutaires » de l'Annuaire en 2015-2016 (§ 3.1). Le calcul suivant le suggère, sans que le tableau le dise. En 2015-2016, l'Annuaire compte
  2 393 « Prof. + M. conf. » et 10 122 « M. ass. + Ass. », soit 12 515, contre 12 589 agents pour le corps
  INSAF du supérieur. Le corps exclurait donc les technologues et les hospitalo-universitaires. C'est
  une **inférence** : le tableau ne publie pas cette égalité.
- CSV : `personnels-ins-corps-enseignants-{primaire,secondaire,superieur}-2015-2018.csv`.

### 1.4 Salaire moyen par ministère, 2020 (INS, tableau 25)

Source : `ins-fonction-publique-2021`, tableau 25 « Le salaire moyen brut et net selon le ministère en
2020 », fichier `tab25_0.xlsx` (feuille nommée `tab18`). Unité : dinars courants par mois.

| | Brut + contributions | Brut | Net |
|---|---:|---:|---:|
| Ministère de l'Éducation | 2 386 | 1 997 | 1 392 |
| Ministère de l'Enseignement supérieur | 2 910 | 2 433 | 1 682 |
| Ensemble de la fonction publique | 2 262 | 1 905 | 1 309 |

C'est la seule **rémunération moyenne par agent d'un ministère** publiée par l'INS. Elle couvre une
année. Le tableau 26 (`tab26_0.xlsx`) donne aussi le brut par type d'agent en 2020 : à l'Éducation,
fonctionnaires 2 509 D et ouvriers 1 383 D ; à l'Enseignement supérieur, fonctionnaires 3 514 D et
ouvriers 1 437 D. Le tableau 10 (`tab10.xlsx`) répartit les agents de 2021 par type, en milliers. Pour
l'Éducation : 175,991 fonctionnaires, 20,591 ouvriers et 0,118 autres. Pour l'Enseignement
supérieur : 23,805, 9,710 et 0,770.
CSV : `personnels-ins-salaire-moyen-ministere-2020.csv`.

---

## 2. Les postes budgétaires (budgets de l'État par ministère, 2013-2017)

Source : ministère des Finances, *ميزانية الدولة لسنة N* (budget de l'État pour l'année N), fascicule par
ministère. Ces fascicules sont déjà dans `tunisia-data/data/raw/minfinances/portail_ancien/budgets_ministeres/`
et au catalogue `sources/minfinances-portail-ancien-urls.csv`. Leurs clés existent dans
`precis/fr/education/references.json` : `budget-men-2013` à `budget-men-2017`, `budget-mesrs-2013-gbo`,
`budget-mesrs-2014-gbo`, `budget-mesrs-2015` à `budget-mesrs-2017`. La rubrique utile se trouve en tête du
titre I, sur la page « معطيات عامة حول مشروع ميزانية N ». Elle s'intitule « **II - الوسائل البشرية المتوفرة** »
(moyens humains disponibles) et est placée sous le rappel des crédits du titre I, dont « نفقات التأجير ».
Les rémunérations et les postes viennent donc **du même document et du même périmètre**.

**Stade et notion.** La page met en regard deux colonnes :

- la colonne N-1 (« ق .م محين », loi de finances actualisée) : le tableau détaillé des pages suivantes
  montre qu'elle donne les **agents en fonction en fin d'année N-1** (« المباشرون الى موفى N-1 »). Les
  totaux concordent pour 2013, 2014 et 2015 : 188 211, 192 981 et 193 312 ;
- la colonne N (« تقديرات ») : les **postes autorisés en fin d'année N** (« المرخص فيهم الى موفى N »),
  c'est-à-dire une prévision.

Pour le ministère de l'Éducation, les CSV séparent les deux notions dans deux jeux de fichiers. Pour
l'Enseignement supérieur (§ 2.2), chaque fichier mêle les colonnes N-1 et les prévisions, et le stade
est indiqué ligne par ligne dans `source`.

Le total de la colonne N-1 est égal à celui du tableau détaillé. Par catégorie, les deux diffèrent de
quelques unités à une centaine : en 2013, les techniciens de laboratoire sont 3 388 sur la page de
synthèse et 3 486 au tableau détaillé. Le tableau détaillé répartit aussi dans les catégories les
agents des établissements.

### 2.1 Ministère de l'Éducation

| Fascicule | Page (PDF) | Ligne |
|---|---|---|
| `budget-men-2013` (jd40, novembre 2012) | 12 (15) | tableau détaillé p. 24 (PDF 30) |
| `budget-men-2014` (jd646) | 23 (27) | tableau détaillé p. 28 (PDF 33) |
| `budget-men-2015` (jd795) | 22 (26) | tableau détaillé p. 27 (PDF 32) |
| `budget-men-2016` (jd1042) | 22 (26) | tableau détaillé p. 27 (PDF 32) |
| `budget-men-2017` (jd1172) | 22 (26) | pas de tableau détaillé repéré |

**Agents en fonction en fin d'année** (colonne N-1) :

| Fin | Enseignants 1er cycle de base / primaire | Enseignants 2e cycle de base et secondaire | Inspecteurs pédagogiques | Surveillants | Administratifs | Ouvriers | Total général | Part des deux corps enseignants |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2012 | 64 225 | 81 208 | 1 416 | 11 134 | 7 622 | 19 044 | 188 211 | 77,3 % |
| 2013 | 65 439 | 81 418 | 1 468 | 12 431 | 7 982 | 20 611 | 192 981 | 76,1 % |
| 2014 | 66 606 | 81 036 | 1 352 | 12 122 | 7 829 | 20 739 | 193 312 | 76,4 % |
| 2015 | 66 898 | 80 780 | 1 359 | 11 907 | 9 166 | 21 946 | 195 702 | 75,5 % |
| 2016 | 67 020 | 80 008 | 1 295 | 11 581 | 10 481 | 20 772 | 194 624 | 75,5 % |

**Postes autorisés en fin d'année** (colonne N, prévision) : 1er cycle 64 946 (2013), 65 417 (2014),
67 236 (2015), 64 093 (2016), 64 652 (2017). 2e cycle et secondaire 81 628, 81 489, 81 676, 78 600,
77 596. Total général 190 493, 193 799, 195 188, 190 048, 188 966.

**Rémunérations** (« نفقات التأجير », milliers de dinars) : 2 925 957 (2012, LF actualisée),
3 161 911 (2013), 3 375 340 (2014), 3 692 940 (2015), 4 198 409 (2016) et 4 520 965 (2017, prévision).
La valeur 2017 est **identique** à celle du tableau 16.9 de l'Annuaire 2015-2019, comme celle de
l'Enseignement supérieur (918 356). Ce n'est pas une règle. En 2016, le tableau 16.9 donne 4 348 250 et
le budget 4 198 409 ; en 2015, le tableau donne 3 718 760 et le budget 3 692 940 (LF actualisée) ou
3 506 821 (projet). Le stade des valeurs du tableau 16.9 reste donc à établir année par année.

Remarques :

- Le budget 2016 prévoyait de ne pas remplacer 5 654 départs à la retraite. Les postes autorisés
  devaient tomber à 190 048 fin 2016. Le budget 2017 donne 194 624 pour 2016, dans une colonne sans mention
  de stade et sans tableau détaillé. Si cette colonne compte bien les agents en fonction, comme en
  2013-2016, la prévision n'a pas été tenue. C'est une inférence.
- L'INSAF compte 197 884 agents en 2016 et 196,7 milliers en 2017, soit 2 000 à 3 000 de plus que les
  postes en fonction du budget. L'écart n'est pas expliqué. Il peut venir des agents des établissements
  publics, de contractuels hors postes ou de la date de l'effectif.
- **Les suppléants** (instituteurs et professeurs suppléants) ne figurent pas dans ces postes : la LF
  2026, art. 107, prévoit leur intégration (déjà cité dans `_depense.qmd`). Leur nombre n'a été trouvé
  dans aucune source lue.
- Les budgets mentionnent les recrutements de l'année. En 2013, 5 648 recrutements sont prévus, dont
  2 700 au 1er cycle et 1 505 au 2e cycle et au secondaire (p. 24). En 2012, « 5.667 عونا من بينهم
  3.900 مدرسا » ont été recrutés (p. 25).

La valeur fin 2016 des fichiers « en fonction » provient de cette colonne (voir ci-dessus).

CSV : `personnels-budget-education-en-fonction-{premier-cycle,second-cycle-secondaire,total-agents}.csv`,
`personnels-budget-education-autorises-{…}.csv`, `personnels-budget-education-remunerations.csv`.

### 2.2 Ministère de l'Enseignement supérieur (partie enseignement supérieur)

| Fascicule | Page (PDF) | Colonnes |
|---|---|---|
| `budget-mesrs-2013-gbo` (jd43, novembre 2012) | 7 (12) | 2012 « قم », 2013 « تقديرات » |
| `budget-mesrs-2016` (jd1039) | 15 (23) | 2015 « ق م محين », 2016 « تقديرات » |
| `budget-mesrs-2017` (jd1173) | 15 (24) | 2016 « ميزانية », 2017 « تقديرات » |

| | 2012 | 2013 (prév.) | 2015 | 2016 | 2017 (prév.) |
|---|---:|---:|---:|---:|---:|
| Encadrement enseignant (« إطار تدريس ») | 20 857 | 21 036 | 17 579 | 16 891 | 16 398 |
| Total des agents | 39 897 | 40 414 | 40 887 | 36 490 | 35 207 |
| Rémunérations (milliers de D) | 725 963 | 819 049 | 955 277 | 1 033 352 | 918 356 |

- **2014 et 2015 manquent** : les fascicules `budget-mesrs-2014-gbo` (jd648) et `budget-mesrs-2015` (jd853)
  n'ont pas de page « الوسائل البشرية » repérable par recherche de texte. Recherches faites : « الوسائل
  البشرية », « القارون », « إطار تدريس », « العملة ». Une lecture à l'image reste à faire.
- **Ruptures non expliquées.** L'encadrement enseignant passe de 21 036 (prévision 2013) à 17 579
  (2015). Le total tombe de 40 887 (2015) à 36 490 (2016). Le budget 2016 comptait encore une ligne
  « أسلاك أخرى » de 2 713 agents, absente en 2017. La rémunération baisse de 11 % entre 2016 et 2017,
  et la valeur 2017 est identique au tableau 16.9 de l'Annuaire. Aucun de ces fascicules ne commente
  ces changements de périmètre. Ces chiffres ne se comparent pas d'une année à l'autre sans
  vérification.
- Les postes budgétaires de l'enseignement supérieur se situent entre le corps INSAF (environ 12 600)
  et les statutaires de l'Annuaire (environ 20 500). Les trois mesures ne se raccordent pas.
- CSV : `personnels-budget-esrs-encadrement-enseignant.csv`, `personnels-budget-esrs-total-agents.csv`,
  `personnels-budget-esrs-remunerations.csv`.

### 2.3 Formation professionnelle (budget 2013 seulement)

`2013_budget_formation_professionnelle_emploi_jd41.pdf`, page 7 (PDF 12), « مشروع ميزانية 2013 », rubrique
« الوسائل البشرية المتوفرة ». Aucune clé n'existe : proposition au § 7.

| | 2012 (« ق م ») | 2013 (prévision) |
|---|---:|---:|
| Total des agents | 8 118 | 8 352 |
| dont agents du ministère | 135 | 123 |
| dont permanents des établissements (ATFP, CENAFFIF) | 6 614 | 6 844 |
| dont non permanents (« الأعوان غير القارين ») | 1 369 | 1 385 |
| Rémunérations (milliers de D) | 145 654 | 164 075 |

Les formateurs ne sont pas isolés. Les fascicules 2014-2017 (jd650, jd796, jd1021, jd1174) n'ont pas
donné de page équivalente à la recherche de texte : les occurrences de « عدد الأعوان » tombent sur des
indicateurs de performance. Rien n'est versé en CSV pour la formation professionnelle.

### 2.4 La masse salariale par programme

Les fascicules détaillés ventilent « نفقات التأجير العمومي » par programme et sous-programme. Ainsi, en
2014 et 2016, le programme « تعليم عالي شمال » est découpé par université. Chaque sous-programme est
ventilé par paragraphe : traitement de base, indemnités, cotisations des « الأعوان القارين », puis « الأعوان
غير القارين — الأعوان المتعاقدون والعاملون بالحصة » (contractuels et vacataires) (`budget-mesrs-2016`,
p. 42, PDF 53). **Aucune ventilation par corps n'existe** : la rémunération des enseignants ne s'y lit pas.
Le paragraphe 031 donnerait, une fois sommé sur les sous-programmes, la **dépense en contractuels et
vacataires**. La somme n'a pas été faite : il faudrait lire chaque sous-programme, plusieurs dizaines
de pages par fascicule.

---

## 3. Enseignants du supérieur : statutaires, contractuels, vacataires

### 3.1 Annuaire de l'INS : « Personnel enseignant à plein temps »

Source : `ins-annuaire-statistique`, chapitre « Enseignement et culture », tableau 3.22 (éditions
1995-2001 à 2002-2006), 3.1.22, 2.1.22, puis 2.1.21 depuis l'édition 2010-2014. Titre : « Personnel
enseignant à plein temps » (« المدرسون المباشرون كامل الوقت »). Il cite pour source le ministère de
l'Enseignement supérieur. Les lignes sont « Statutaires » (« المدرسون القارون ») et « Contractuels »
(« المتعاقدون »). Les colonnes vont par grade : Prof. + M. conf., M. ass. + Ass., hospitalo-universitaires,
technologues, autres (« PES, ingénieurs, experts, médecins »), étrangers.

| Année | Édition (p.) | Statutaires | Contractuels | Total | Part des contractuels |
|---|---|---:|---:|---:|---:|
| 2004-2005 | 2000-2004 (77) | 12 474 | 4 197 | 16 671 | 25,2 % |
| 2005-2006 | 2001-2005 (77) | 12 979 | 3 940 | 16 919 | 23,3 % |
| 2006-2007 | 2002-2006 (77) | 13 978 | 4 139 | 18 117 | 22,8 % |
| 2007-2008 | 2003-2007 (75) | 14 384 | 4 224 | 18 608 | 22,7 % |
| 2008-2009 | 2004-2008 (75) | 15 158 | 4 891 | 20 049 | 24,4 % |
| 2009-2010 | 2005-2009 (67) | 14 358 | 4 635 | 18 993 | 24,4 % |
| 2010-2011 | 2006-2010 (67) | 16 486 | 5 066 | 21 552 | 23,5 % |
| 2011-2012 | 2007-2011 (69) | 17 619 | 4 792 | 22 411 | 21,4 % |
| 2012-2013 | 2008-2012 (69) | 18 873 | 4 005 | 22 878 | 17,5 % |
| 2014-2015 | 2010-2014 (62) | 19 909 | 2 652 | 22 561 | 11,8 % |
| 2015-2016 | 2011-2015 (62) | 20 478 | 2 170 | 22 648 | 9,6 % |
| 2016-2017 | 2012-2016 (62) | 20 736 | 2 110 | 22 846 | 9,2 % |
| 2017-2018 | 2013-2017 (62) | 20 511 | 1 832 | 22 343 | 8,2 % |
| 2018-2019 | 2014-2018 (62) | 19 882 | 1 941 | 21 823 | 8,9 % |
| 2019-2020 | 2015-2019 (62) | 20 424 | 1 648 | 22 072 | 7,5 % |
| 2020-2021 | 2016-2020 (62) | 20 047 | 2 039 | 22 086 | 9,2 % |
| 2021-2022 | 2017-2021 (62) | 20 517 | (« ... ») | 23 498 | — |
| 2022-2023 | 2018-2022 (62) | 21 462 | 2 064 | 23 526 | 8,8 % |
| 2023-2024 | 2019-2023 (62) | 21 365 | 2 180 | 23 545 | 9,3 % |

- **Rattachement aux années.** Les éditions 2000-2004 à 2014-2018 ne donnent pas l'année scolaire
  dans le titre du tableau. L'année est déduite de l'égalité du total avec la ligne « enseignement
  supérieur » du tableau des données générales (`enseignants-public-superieur.csv`), sauf pour 2018-2019.
  Pour 2018-2019, le total est 21 823 ici, contre 21 880 dans le tableau des données générales retenu
  par le précis. L'édition 2016-2020 titre « en 2020 - 2021 » le total de 22 086 que le précis range en
  2019-2020 : c'est le « décalage » déjà signalé dans `_depense.qmd`. Les éditions plus anciennes portent
  le tableau sans découpage lisible par le texte (1998-2002, 1999-2003 : seule la ligne Total) ou avec
  des colonnes ambiguës (1995-2001). Elles ne sont pas reprises.
- **2021-2022** : le total des contractuels est imprimé « ... ». Par différence on trouve 2 981, mais ce
  chiffre n'est pas publié et n'est pas versé.
- **Conséquence pour la figure 7.4** : les enseignants du supérieur de la figure sont les enseignants
  **à plein temps**, statutaires et contractuels. Ils n'incluent pas les vacataires. Ce n'est pas un
  ETP, mais ce n'est pas non plus un effectif qui mêle temps plein et temps partiel.
- **Pages des éditions 2015-2019 à 2019-2023** : page 62. Le pied de page imprimé porte 62, égal à la
  page du PDF.
- CSV : `personnels-ins-superieur-plein-temps-statutaires.csv`, `personnels-ins-superieur-plein-temps-contractuels.csv`.

### 3.2 Budget GBO 2013 : part des permanents parmi les enseignants universitaires

Source : `2013_budget_enseignement_superieure_recherche_scientifique_jd42.pdf`, version « gestion du
budget par objectifs ». Fiche de l'indicateur « نسبة المدرسين الجامعيين القارين من مجموع المدرسين
الجامعيين », mise à jour en juillet 2012, page 31 (PDF 33). Le champ exclut les technologues.

| | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Enseignants universitaires permanents | 10 900 | 11 456 | 12 075 | 13 711 | 14 111 | 14 511 | 14 911 |
| Total des enseignants universitaires | 14 500 | 15 003 | 15 568 | 17 111 | 17 411 | 17 711 | 18 011 |
| Part des permanents | 75,17 % | 76,36 % | 77,56 % | 80,13 % | 81,05 % | 81,93 % | 82,79 % |
| Stade | réal. | réal. | réal. | LF | prév. | prév. | prév. |

- Les totaux ronds de 2012-2015 sont des prévisions. Le « total » comprend des non-permanents qui ne
  sont pas nommés.
- La fiche voisine (p. 29, PDF 31) donne le nombre d'étudiants par enseignant permanent : 30,2 (2009),
  28,6, 26,4, 22,7, 20,9, 20,5 et 20,3 (2015).
- **Le même indicateur change de valeur d'un budget à l'autre.** `budget-mesrs-2014-gbo` (p. 9, PDF 15)
  donne 83,3 % (2012, réalisation), 83,6 % (2013) et 83,9 % (2014). `budget-mesrs-2015` (p. 9, PDF 18)
  donne 87,5 % (2013, réalisation), 84,3 % (2014) et 87,4 % (2015). La définition n'est pas reprise dans
  ces deux fascicules. Ces valeurs restent dans la note et ne sont pas versées.
- Le fichier jd42 n'a pas de clé : `budget-mesrs-2013-gbo` renvoie au fichier jd43 (voir la note de
  l'entrée). Une clé est proposée au § 7.
- CSV : `personnels-budget-esrs-enseignants-permanents-hors-technologues.csv`,
  `personnels-budget-esrs-enseignants-total-hors-technologues.csv`.

### 3.3 ETP et vacataires : rien

- **Vacataires** : aucun effectif trouvé, ni dans l'Annuaire de l'INS (qui ne compte que le temps
  plein), ni dans les budgets, ni par recherche web. Requêtes web lancées : « Tunisie enseignement
  supérieur en chiffres enseignants permanents contractuels vacataires 2022-2023 mes.tn » et
  « "المدرسون الجامعيون" القارون المتعاقدون العرضيون إحصائيات التعليم العالي تونس 2023-2024 ». Elles
  n'ont rendu que des sources françaises et des appels à candidatures d'universités tunisiennes. La
  publication du ministère « L'enseignement supérieur et la recherche scientifique en chiffres » n'a pas
  été atteinte.
- **ETP** : aucune source ne publie d'ETP enseignants pour la Tunisie. La recherche « Tunisia teachers
  full-time equivalent UIS » renvoie aux définitions de l'UIS (effectif ou ETP) et à l'indicateur
  SE.SEC.TCHR de la Banque mondiale, qui compte temps plein et temps partiel. Le navigateur de données
  de l'UIS n'a pas été interrogé directement : **non vérifié**, pas « inexistant ».
- **Heures de service** : non cherchées dans cette passe. Les obligations de service sont fixées par
  les statuts particuliers des corps, qui relèvent du livre « Rémunérations publiques ».

---

## 4. Contrôle de périmètre : masse salariale du tableau 16.9 et agents INSAF

Le contrôle porte sur 2020. Il multiplie le salaire moyen INS (brut + contributions, § 1.4) par 12 et
par l'effectif du rapport 2025, puis compare le résultat à la masse salariale budgétaire.

| 2020 | Salaire moyen × 12 × agents | Tableau 16.9 « Rémunération » (édition 2016-2020, chiffre provisoire) | Rapport |
|---|---:|---:|---:|
| Éducation | 2 386 × 12 × 195 391 = 5 594 M D | 5 791 M D | 0,966 |
| Enseignement supérieur | 2 910 × 12 × 33 832 = 1 181 M D | 1 257 M D | 0,940 |

L'écart est de 3,4 % à l'Éducation et de 6 % à l'Enseignement supérieur. Trois causes possibles :

- le tableau 16.9 donne un chiffre provisoire, peut-être une prévision (§ 2.1) ;
- la masse budgétaire comprend des dépenses hors salaire moyen (rémunération des contractuels hors
  INSAF, heures de vacation, subventions de rémunération aux établissements) ;
- pour le supérieur, la part de la recherche dans le chiffre de 2020 n'est pas établie (`_depense.qmd`).

Le périmètre est donc **à peu près commun** : diviser la masse salariale du tableau 16.9 par les agents
INSAF du ministère donne un **ordre de grandeur défendable de la rémunération par agent**, qui dépasse
d'environ 3 à 6 % le salaire moyen publié.

---

## 5. Ce qui devient calculable

1. **Rémunération par agent du ministère** : tableau 16.9 (`nature-*-remunerations.csv`) ÷ agents INSAF
   (§ 1), même ministère, même année. La jointure des fichiers donne les années suivantes (dinars courants
   par an ; agents des annexes jusqu'en 2017, du rapport 2025 ensuite) :
   - Éducation : 2010 (14 810), 2011 (14 940), 2012 (15 660), 2014 (17 850), 2015 (19 470), 2016 (21 970),
     2017 (22 980), 2020 (29 640), 2022 (31 160), 2023 (31 120). **2010** : le tableau 16.9 comprend la
     formation professionnelle, pas le dénominateur INSAF ; à écarter ou à signaler ;
   - Enseignement supérieur : 2010 (18 700), 2011 (20 780), 2012 (22 000), 2014 (23 820), 2015 (25 810),
     2016 (27 350), 2017 (25 780), 2020 (37 160), 2022 (42 040), 2023 (44 230). La part de la recherche
     dans le numérateur n'est pas établie en 2020, 2022 et 2023 (`_depense.qmd`).
   - Le tableau 16.9 n'existe pas en 2013, 2018, 2019 ni 2021. L'en-tête de colonne devient « par
     agent du ministère » ; le mot « enseignant » disparaît.
2. **Rémunération par poste budgétaire de l'Éducation**, 2012-2017, avec la masse et les postes d'un
   même document, 2012-2016 (2017 n'a que des postes autorisés) : 3 692 940 / 195 702 = 18 870 D par
   an en 2015. C'est plus cohérent que (1), mais
   la série est courte.
3. **Part des enseignants dans les agents** : environ 76 % des postes du ministère de l'Éducation
   (2012-2016) ; 43 à 52 % de la partie enseignement supérieur du budget (2013-2017, avec ruptures).
   Pour la fonction publique dans son ensemble : les trois corps enseignants INSAF de 2015-2017.
4. **Supérieur** : part des contractuels parmi les enseignants à plein temps, 2004-2005 à 2023-2024.
   Elle tombe d'environ 25 % à environ 9 %.
5. **Non calculable** : la rémunération moyenne d'un enseignant et celle d'un enseignant ETP. Pour la
   calculer, il faudrait le salaire moyen par corps, que l'INS ne publie pas (seulement par catégorie
   A1-D et par ministère, et pour 2020 seulement par ministère), ou la masse salariale par corps, que
   les budgets ne publient pas. Une piste reste ouverte : la grille indiciaire du corps (livre
   « Rémunérations publiques ») appliquée à la pyramide des grades du tableau 3.1 de l'Annuaire. Cela
   donnerait une **estimation** et non une donnée publiée. Ce serait une évaluation (famille 3).

**Familles des chiffres** (`docs/conventions-redaction.md`, § 3) : les tableaux 16.9 et les budgets
relèvent du budgétaire et du ministère des Finances. Les séries INS-INSAF et l'Annuaire sont des données
administratives relayées par l'INS (famille budgétaire et administrative, non une évaluation). Le
rapprochement du § 4 est un calcul de la note : il ne se publie pas comme un chiffre de source.

---

## 6. Lacunes

- **Formation professionnelle** : pas d'effectif INSAF propre ; un seul budget lu (2013) ; formateurs
  non isolés.
- **Budgets 2018-2026** (fascicules par mission, projets et rapports annuels de performance) : non
  obtenus. L'ancien portail (`v2.portail.finances.gov.tn`) est inaccessible, comme le notent les entrées
  `budget-men-*`. Une page supposée du nouveau portail (<https://www.finances.gov.tn/ar/budget-de-letat>)
  répond 404. La recherche « مشروع ميزانية مهمة التربية 2024 عدد الأعوان حسب البرامج إطار التدريس » ne
  renvoie que la presse et un procès-verbal de la commission des finances de l'ARP (8 janvier 2024, prêt
  BEI, sans effectifs). Ces documents donneraient les postes **par programme** (primaire, préparatoire et
  secondaire, pilotage) et prolongeraient le § 2 jusqu'en 2026.
- **MESRS 2014 et 2015** : page des moyens humains non trouvée à la recherche de texte (§ 2.2).
- **Vacataires du supérieur, suppléants de l'Éducation, ETP** : rien (§ 3.3, § 2.1).
- **Pages imprimées** des éditions 2015-2019 à 2019-2023 de l'Annuaire, tableau 2.1.21 : à vérifier au
  fascicule.
- **INSAF 2018 et 2019 par corps** : fichiers défectueux (§ 1.3).
- **Non parcouru dans cette passe** : `jort_cache.db` (les effectifs ne sont pas au Journal officiel,
  mais les tableaux annexés aux lois de règlement pourraient porter des postes), `~/projets/PDFs-legislation-tunisie`,
  les rapports de la Cour des comptes, la revue de la dépense publique de la Banque mondiale
  (`wb-tunisia-per-2020`, absente de l'entrepôt, qui traite de la masse salariale), l'Observatoire, le
  navigateur de données de l'UIS, le portail gbo.tn. La fiche `r-educ-cout-unitaire-ministere-2021`
  (`docs/recherches.yml`) vise les mêmes PAP et RAP 2019-2023 pour un autre objet. La fiche voisine des
  entreprises publiques signale gbo.tn : 587 fichiers, lois de finances et rapports annexes,
  rapports annuels de performance.

---

## 7. Références candidates

**Déjà présentes** (`precis/fr/education/references.json`) : `ins-annuaire-statistique`,
`budget-men-2013` … `budget-men-2017`, `budget-mesrs-2013-gbo`, `budget-mesrs-2014-gbo`,
`budget-mesrs-2015` … `budget-mesrs-2017`. Au fonds commun (`precis/fr/references.json`) :
`ins-fonction-publique-2021`.

**À verser au fonds commun** (présente seulement dans `precis/fr/remunerations_publiques/references.json`,
recopiée telle quelle) :

```json
{"id": "ins-fonction-publique-2025", "type": "dataset", "note": "citation-key: ins-fonction-publique-2025", "publisher": "Institut National de la Statistique, Tunisie", "title": "Évolution des effectifs et des rémunérations des agents de la fonction publique tunisienne 2018-2025", "URL": "https://www.ins.tn/publication/evolution-des-effectifs-et-des-remunerations-des-agents-de-la-fonction-publique", "author": [{"literal": "Institut national de la statistique"}], "issued": {"date-parts": [[2026, 8]]}}
```

**À créer** :

```json
{"id": "budget-mesrs-2013-gbo-indicateurs", "type": "report", "title": "ميزانية الدولة لسنة 2013 : وزارة التعليم العالي والبحث العلمي، حسب منهجية التصرف في الميزانية حسب الأهداف [Budget de l'État pour 2013 : ministère de l'Enseignement supérieur et de la Recherche scientifique, selon la gestion du budget par objectifs]", "author": [{"literal": "Ministère des Finances"}], "publisher": "Ministère des Finances, Tunisie", "issued": {"date-parts": [[2012, 11]]}, "URL": "http://web.archive.org/web/20170821030423/http://finances.gov.tn/index.php?option=com_jdownloads&Itemid=712&view=finish&cid=42&catid=1&lang=fr", "language": "ar", "note": "citation-key: budget-mesrs-2013-gbo-indicateurs\nFichier jd42 (173 p.), sha256 82f4e6ca…2a2e64, catalogue tunisia-data sources/minfinances-portail-ancien-urls.csv. Fiches d'indicateurs mises à jour en juillet 2012. Date d'émission à vérifier en couverture. Note : docs/notes/education-effectifs-personnels-2026-10-17.md, § 3.2."}
```

```json
{"id": "budget-mfpe-2013", "type": "report", "title": "ميزانية الدولة لسنة 2013 : وزارة التشغيل والتكوين المهني [Budget de l'État pour 2013 : ministère de la Formation professionnelle et de l'Emploi]", "author": [{"literal": "Ministère des Finances"}], "publisher": "Ministère des Finances, Tunisie", "issued": {"date-parts": [[2012]]}, "URL": "http://web.archive.org/web/20160303175058/http://v2.portail.finances.gov.tn/index.php?option=com_jdownloads&Itemid=613&view=finish&cid=41&catid=1&lang=fr", "language": "ar", "note": "citation-key: budget-mfpe-2013\nFichier jd41 (198 p.), sha256 05280de3…abc5030. Mois de parution à relever en couverture. Note : docs/notes/education-effectifs-personnels-2026-10-17.md, § 2.3."}
```

---

## 8. Notions à glossaire

| FR | AR | Source canonique pressentie |
|---|---|---|
| agents en fonction (postes occupés) | الأعوان المباشرون | budgets `budget-men-*`, tableau « المباشرون الى موفى السنة » |
| postes autorisés | الأعوان المرخص فيهم | idem |
| enseignant statutaire / permanent | مدرس قار | Annuaire INS, tableau 2.1.21 ; budgets GBO |
| enseignant contractuel | مدرس متعاقد | idem |
| agent non permanent (contractuels et vacataires) | الأعوان غير القارين — الأعوان المتعاقدون والعاملون بالحصة | `budget-mesrs-2016`, paragraphe 031 |
| corps (de la fonction publique) | سلك | INS, annexes, tableau 11 |
| équivalent temps plein | (pas de terme rencontré dans les sources tunisiennes lues) | UIS, glossaire |

---

## 9. Recherches infructueuses : fiches proposées

Le registre `docs/recherches.yml` n'est pas modifié. Ces recherches portent sur des documents
budgétaires et statistiques, hors Journal officiel. Le format est celui de `education-recherches-A.yml`.
Les clés `requetes` ne contiennent que ce qui a été réellement lancé. Faute de source JORT, elles sont
consignées sous `web` et `corpus_local`, à adapter si l'outil `scripts/recherches.py` ne les accepte pas.

```yaml
- id: r-budget-missions-education-effectifs-2018-2026
  objet: fascicules budgétaires par mission (Éducation, Enseignement supérieur et recherche scientifique, Formation professionnelle et emploi) des lois de finances 2018 à 2026, avec la rubrique des moyens humains (« الوسائل البشرية » ou « الموارد البشرية ») par programme
  ou: [precis/fr/education/_depense.qmd#sec-educ-depense-personnels]
  requetes:
    web: ['مشروع ميزانية مهمة التربية 2024 عدد الأعوان حسب البرامج إطار التدريس finances.gov.tn', '"مشروع القدرة على الأداء" مهمة التربية 2023 pdf "الموارد البشرية"']
    corpus_local: [tunisia-data/data/raw/minfinances/portail_ancien/budgets_ministeres (2013-2017 seulement)]
    depuis: 2017-12-01
  periode:
    jusqu_au: 2026-10-17
    motif: l'entrepôt s'arrête aux budgets 2017
  passes:
  - date: 2026-10-17
    role: documentaliste
    sources: [web, corpus_local]
    couverture: "deux recherches web (presse, procès-verbal ARP du 8 janvier 2024 sans effectifs) ; https://www.finances.gov.tn/ar/budget-de-letat : 404 ; captures Wayback du nouveau portail non essayées ; site de l'ARP (rapports des commissions sur les missions) non parcouru"
    couvert_jusqu_au: 2026-10-17
    resultat: aucun
  a_faire: [parcourir la page « Loi de Finance et rapports annexes » de gbo.tn et finances.gov.tn (rubrique budget, projets et rapports annuels de performance) et leurs captures Wayback, mutualiser avec r-educ-cout-unitaire-ministere-2021, chercher sur arp.tn les rapports de la commission des finances sur les missions Éducation et Enseignement supérieur, lire les budgets MESRS 2014 (jd648) et 2015 (jd853) à l'image pour la page des moyens humains]
- id: r-superieur-vacataires-etp
  objet: effectif des enseignants vacataires de l'enseignement supérieur public et enseignants en équivalent temps plein (supérieur et scolaire)
  ou: [precis/fr/education/_depense.qmd#sec-educ-depense-personnels]
  requetes:
    web: ['Tunisie enseignement supérieur en chiffres enseignants permanents contractuels vacataires 2022-2023 mes.tn', '"المدرسون الجامعيون" القارون المتعاقدون العرضيون إحصائيات التعليم العالي تونس 2023-2024', 'Tunisia teachers full-time equivalent UIS data primary secondary tertiary']
    corpus_local: [Annuaire statistique de l'INS, 22 éditions (« vacataire », « contractuel », « plein temps »), budgets MESRS 2013-2017]
    depuis: 2004-09-01
  periode:
    jusqu_au: 2026-10-17
    motif: le temps plein est connu depuis 2004-2005 (Annuaire) ; l'objet est le temps partiel et l'ETP sur la même période
  passes:
  - date: 2026-10-17
    role: documentaliste
    sources: [web, corpus_local]
    couverture: "Annuaire : seul le temps plein (statutaires, contractuels) est publié ; budgets : paragraphe 031 « الأعوان المتعاقدون والعاملون بالحصة » en dinars, sans effectif, non sommé ; web : aucune publication tunisienne atteinte ; navigateur de données UIS non interrogé"
    couvert_jusqu_au: 2026-10-17
    resultat: aucun
  a_faire: [obtenir « L'enseignement supérieur et la recherche scientifique en chiffres » (mes.tn, éditions annuelles), interroger le navigateur de données UIS (enseignants, ETP, Tunisie), sommer le paragraphe 031 des budgets MESRS 2013-2017 par sous-programme]
```
