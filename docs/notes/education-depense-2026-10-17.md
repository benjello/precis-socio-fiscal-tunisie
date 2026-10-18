# La dépense d'éducation : note documentaire (chapitre 6)

Note du documentaliste, 17 octobre 2026, branche `chantier/education-v1`. Elle sert le chapitre 6
du plan (`docs/notes/education-plan-2026-10-17.md`), et les chapitres 0 et 8 pour les séries qui
leur reviennent. Aucun `.qmd`, aucun `references.json`, aucun `glossaire.yml` n'est modifié.

Les séries sont dans `docs/notes/education-depense-series/` : un CSV par série, avec les colonnes
`annee, valeur, unite, source, page`. La colonne `source` donne l'édition, le tableau, la ligne
imprimée et le stade comptable. La colonne `page` donne la page imprimée.

Chaque valeur budgétaire tirée de l'Annuaire a été recopiée depuis le texte extrait, puis
**contrôlée par programme** : elle doit apparaître sur la ligne de son libellé, à la page citée. Le
script de contrôle se trouve dans `/tmp/education-ocr-D/scripts/budget.py`, hors dépôt. Les pages
sans couche texte ont été lues à l'image. Ce sont les pages imprimées des éditions 1998-2006, le
JORT n° 102 de 2009 et les projets annuels de performance de 2014.

---

## 1. Ce qui existait avant cette note

| Lieu | Contenu utile au chapitre 6 | État |
|---|---|---|
| `precis/_seriescache/catalog.snapshot.yml` | Aucune série d'éducation. Trois séries servent de **dénominateurs** et de **personnels** : `denominateurs-depenses-etat-pib` (dépenses de l'État hors dette, réalisations du classeur du ministère des Finances, 1986-2025 ; PIB par segment de base), `ins-ministere-effectifs` (2015-2021) et `ins-ministere-effectifs-2018-2025`. Ces deux dernières comptent les agents du ministère de l'Éducation : 194 430 en 2018, 197 836 en 2025. Le ministère de l'Enseignement supérieur en compte 34 465 en 2018 et 32 181 en 2025. Ce sont **tous les agents** du ministère, pas les seuls enseignants. Elles ne se raccordent pas entre elles. | prêt à l'emploi |
| `precis/_seriescache/ins-budget-sante-2018-2023.csv` | **Le modèle à suivre.** Même source (Annuaire de l'INS, tableaux 16.8 et 16.10), même construction de la part du budget. | modèle |
| `tunisia-data/data/raw/ins-publications/annuaire-statistique/` | 22 éditions de l'*Annuaire statistique de la Tunisie*, de 1995-2001 à 2019-2023, sans l'édition 2009-2013. Chapitre 16, « Budget de l'État », tableaux 16.8, 16.9 et 16.10. Chapitre 2 (chapitre 3 avant 2005), « Enseignement et culture », tableau des données générales. | déjà catalogué (`sources/ins-publications-urls.csv`) ; **lu** |
| `tunisia-data/data/raw/minfinances/portail_ancien/budgets_ministeres/` | Budgets détaillés 2013-2017 des missions Éducation, Enseignement supérieur et recherche scientifique, Formation professionnelle et emploi. **Projets annuels de performance (PAP) 2014** : `jd647` (Éducation), `jd649` (Enseignement supérieur et recherche), `jd651` (Formation professionnelle et emploi). Les éditions 2015-2017 sont en arabe. | déjà catalogué (`sources/minfinances-portail-ancien-urls.csv`) ; PAP 2014 **lus** aux pages des programmes ; budgets 2013 et 2015-2017 **non lus** |
| `tunisia-data/data/raw/minfinances/repartition_depenses.xls` | Répartition **économique** des dépenses de l'État, 1986-2025. Aucune ventilation par ministère. | sert au dénominateur seulement |
| `tunisia-data/data/raw/banque-mondiale/` | Rien sur l'éducation. Les indicateurs UIS ont été téléchargés pour cette note (§ 6). | — |
| `~/projets/ceq-tunisie/CEQ_TUN21_March2025/` | Exercice d'incidence 2021 : coûts unitaires et méthode (§ 5). | **lu** |
| `minfinances/portail_ancien/series_statistiques/` (fiches-séries des dépenses totales, de fonctionnement et d'équipement), `rapports_finances_publiques/` 2005-2016, `lois_finances/` (budgets citoyens 2014-2018, notes de présentation des LF 2005-2012) | Recherche de « éducation », « enseignement », التربية, التعليم dans le texte extrait. Aucune occurrence dans les fiches-séries, dont la couche texte est quasi vide (630 caractères pour une page), ni dans les budgets citoyens, qui n'ont **pas de couche texte** (12 à 24 caractères). Une occurrence dans le rapport 2010, deux dans la note de la LF 2010, quatre dans celle de la LF 2005. **Douze occurrences dans le CDMT 2012** (`2012_cdmt.pdf`). | **non lus** : budgets citoyens à lire à l'image (**OCR ou lecture nécessaire**) ; CDMT 2012 à lire |
| `banque-mondiale-rapports/wb_1995_13993_poverty_vol2_annexes.pdf` | **Étude d'incidence de la dépense d'éducation en 1990** : annexe D.1, « Éducation » (§ 8). | **lu** (p. 1-2 de l'annexe D.1, à l'image) ; déjà catalogué (`sources/bm-1995-pauvrete-annexes.md`) |
| `banque-mondiale-rapports/imf_2001_037_statistical_appendix_tunisia.pdf` | Aucune occurrence de l'éducation dans le texte extrait. | écarté |
| `precis/fr/references.json` : `wb-tunisia-per-2020` | Revue de la dépense publique de la Banque mondiale, 2020 (*Overview Report*). Elle n'est **pas dans l'entrepôt**. | **à obtenir et à lire** pour le chapitre 8 |
| Livres du précis | Les rémunérations publiques ne parlent d'aucun corps enseignant (constat du plan, § 1.2). Le modèle de chapitre budgétaire est la santé (`ins-budget-sante-2018-2023`). | — |

---

## 2. Le budgétaire : dépense de l'État par ministère, 1997-2023

### 2.1 Source et méthode

La source est l'**INS, *Annuaire statistique de la Tunisie***, chapitre 16, « Budget de l'État »,
avec la mention « Source : Ministère des Finances » sous chaque tableau. C'est donc du
**budgétaire relayé** par l'INS, qui cite le ministère des Finances.

- **Tableau 16.8** : dépenses du titre I par chapitre. On en retient la section 1, dépenses de
  gestion hors intérêts.
- **Tableau 16.10** : dépenses du titre II par chapitre. On en retient la section 3, dépenses de
  développement hors principal de la dette.
- **Tableau 16.9** : dépenses du titre I par catégorie, c'est-à-dire par nature. Seule l'année la
  plus récente de chaque édition y figure.

L'unité est le millier de dinars courants.

**Stade comptable.** L'Annuaire ne le précise pas. Chaque édition donne trois années, cinq pour
celle de 1995-2001 ; les valeurs d'une même année changent d'une édition à l'autre.

- **L'année la plus récente** d'un tableau est un chiffre provisoire ou une prévision. Jusqu'en 2009,
  ces chiffres sont arrondis à la centaine de milliers de dinars. Par exemple, l'Éducation et la
  Formation affichent 2 043 900 pour 2006 dans l'édition 2002-2006, puis 2 043 935 dans l'édition
  2004-2008.
- **La troisième année** d'un tableau, ou une année plus ancienne, correspond aux **réalisations**.
  C'est vérifié en 2012 : l'Éducation y vaut 3 007 491 en gestion et 276 267 en développement
  (édition 2010-2014, p. 265 et 267). Ce sont exactement les « إنجازات 2012 » du PAP 2014 de
  l'Éducation (tableau 1, p. 6). De même, la Formation professionnelle (163 603) et l'Emploi (49 429)
  font ensemble 213 032, ce qui égale les réalisations 2012 de gestion du PAP 2014 de la mission
  Formation professionnelle et emploi (p. 6 imprimée).
- **Ce ne sont ni les crédits initiaux de la loi de finances ni le total payé de la loi de
  règlement.**
  - En 2010, l'Annuaire donne 2 792 787 pour l'Éducation et la Formation (dernière année de l'édition
    2006-2010). Le décret de répartition des crédits donne 2 792 572 000 dinars (§ 2.5).
  - En 2017, la gestion totale de l'Annuaire vaut 21 199 829. La loi n° 2024-18 donne 21 237 640 250
    dinars payés en section I (JORT n° 35 de 2024, p. 800).
  - Les totaux ne coïncident pas non plus avec les réalisations du classeur `repartition_depenses.xls`.
    Pour 2020, l'Annuaire donne 29 573 799 en gestion, contre 29 950,6 MD de fonctionnement dans le
    classeur.

**Règle de construction.** Pour chaque année, on retient l'édition **la plus récente qui la
contient**. C'est presque toujours son troisième rang, donc une réalisation, avec quatre exceptions :

- **1999-2001** : rangs 1 à 3 de l'édition 1995-2001.
- **2002 et 2003** : seules existent les valeurs arrondies des éditions 2000-2004 et 2001-2005.
- **2015-2017** : les éditions 2014-2018 et 2015-2019 **reprennent telles quelles** les colonnes
  2017-2015 de l'édition 2013-2017. Le chiffre de 2017 est donc celui de la dernière année de
  l'édition 2013-2017 : 4 959 579 pour l'Éducation, au-dessus du réalisé 2018 de 4 732 500.
  **Cette baisse apparente de 2017 à 2018 est un artefact de stade**, à signaler et à revoir avec la
  loi de règlement 2017.
- **2022-2023** : rangs 1 et 2 de l'édition 2019-2023.

Le stade de chaque valeur est écrit dans la colonne `source` du CSV.

### 2.2 Tableau par année

Unités : milliers de dinars courants. G = gestion (tableau 16.8), D = développement (tableau 16.10).
La part dans l'État et la part dans le PIB sont **calculées par la note** (§ 2.4).

| Année | Éducation G | Éducation D | Ens. sup. G | Ens. sup. D | Recherche G | Recherche D | FP G | FP D | Emploi G | Emploi D | Part État % | Part PIB % | Édition (p. G / p. D) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1997 | 956 273 | 72 953 | 204 053 | 44 751 |  |  | 48 529 | 24 436 |  |  |  |  | 1995-2001 (243 / 245) |
| 1998 | 1 033 264 | 60 094 | 224 206 | 43 086 |  |  | 54 869 | 28 917 |  |  |  |  | 1995-2001 (243 / 245) |
| 1999 | 1 123 153 | 78 547 | 249 828 | 47 274 |  |  | 67 874 | 30 300 |  |  |  |  | 1995-2001 (243 / 245) |
| 2000 | 1 192 348 | 75 900 | 288 777 | 59 600 |  |  | 75 485 | 5 300 |  |  |  |  | 1995-2001 (243 / 245) |
| 2001 | 1 306 747 | 83 900 | 331 106 | 77 000 |  |  | 84 625 | 6 900 |  |  |  |  | 1995-2001 (243 / 245) |
| 2002 | 1 424 200 | 94 100 | 387 400 | 91 300 |  |  |  |  | 91 100 | 10 400 |  |  | 2000-2004 (260 / 262) |
| 2003 | 1 586 800 | 112 300 | 443 600 | 118 200 |  |  |  |  | 24 200 | 24 000 |  |  | 2001-2005 (262 / 264) |
| 2004 | 1 720 326 | 105 061 | 504 596 | 139 612 |  |  |  |  | 22 557 | 24 487 |  |  | 2002-2006 (263 / 265) |
| 2005 | 1 901 526 | 99 264 | 527 108 | 90 972 | 22 496 | 32 706 |  |  | 23 944 | 27 481 |  |  | 2003-2007 (271 / 273) |
| 2006 | 2 043 935 | 99 600 | 581 812 | 115 100 | 25 445 | 37 900 |  |  | 25 486 | 45 900 |  |  | 2004-2008 (271 / 273) |
| 2007 | 2 241 400 | 119 800 | 628 400 | 117 500 | 28 100 | 31 100 |  |  | 27 200 | 61 800 |  |  | 2005-2009 (275 / 277) |
| 2008 | 2 433 162 | 132 377 | 682 093 | 123 316 | 30 586 | 43 907 |  |  | 28 688 | 80 579 | (exclu) |  | 2006-2010 (277 / 279) |
| 2009 | 2 541 221 | 195 576 | 720 730 | 137 787 | 24 014 | 38 022 | 90 705 | 14 149 | 35 502 | 114 933 | 29,28 |  | 2007-2011 (279 / 281) |
| 2010 | 2 664 054 | 195 506 | 796 539 | 189 128 | 27 443 | 37 670 | 105 933 | 607 | 39 068 | 29 208 | 29,20 | 5,91 | 2008-2012 (277 / 279) |
| 2011 | 2 824 708 | 239 310 | 860 814 | 152 338 | 32 458 | 53 174 | 123 702 | 3 196 | 43 832 | 23 489 | 25,77 | 6,14 | 2008-2012 (277 / 279) |
| 2012 | 3 007 491 | 276 267 | 982 727 | 116 252 | 34 848 | 46 900 | 163 603 | 455 | 49 429 | 24 632 | 24,06 | 6,04 | 2010-2014 (265 / 267) |
| 2013 | 3 236 103 | 193 360 | 1 054 149 | 94 640 | 37 824 | 32 673 | 174 947 | 382 | 52 649 | 12 677 | 22,00 | 5,88 | 2011-2015 (263 / 265) |
| 2014 | 3 544 934 | 168 701 | 1 070 265 | 84 677 | 39 390 | 50 270 | « - » | 504 | 245 750 | 13 044 | 23,27 | 5,81 | 2012-2016 (263 / 265) |
| 2015 | 3 856 676 | 175 483 | 1 176 001 | 94 067 | 42 834 | 47 631 | « - » | 597 | 268 010 | 11 911 | 25,42 | 6,01 | 2015-2019 (267 / 269) |
| 2016 | 4 481 632 | 202 247 | 1 223 175 | 96 761 | 45 543 | 53 670 | « - » | 602 | 279 315 | 10 950 | 26,50 | 6,40 | 2015-2019 (267 / 269) |
| 2017 | 4 959 579 | 202 569 | 1 261 038 | 78 580 | 41 559 | 44 727 | « - » | 692 | 305 462 | 12 737 | 25,03 | 6,46 | 2015-2019 (267 / 269) |
| 2018 | 4 732 500 | 214 044 | 1 300 184 | 82 524 | 44 321 | 59 891 | « - » | 741 | 330 722 | 3 252 | 22,48 | 5,69 | 2017-2021 (267 / 269) |
| 2019 | 5 698 966 | 314 176 | 1 487 557 | 92 470 | « - » | 64 597 | « - » | 1 914 | 385 936 | 1 645 | 24,41 | 6,23 | 2017-2021 (267 / 269) |
| 2020 | 6 181 511 | 270 481 | 1 564 023 | 146 450 | « - » | 79 136 | 413 517 | 1 467 | 94 623 | 13 960 | 23,09 | 6,90 | 2018-2022 (267 / 269) |
| 2021 | 6 449 652 | 265 697 | 1 726 567 | 78 156 | « - » | 62 900 | 337 007 | 1 272 | 84 526 | 11 973 | 22,79 | 6,52 | 2019-2023 (269 / 271) |
| 2022 | 6 562 366 | 271 430 | 1 738 859 | 92 336 | « - » | 79 570 | 339 931 | 405 | 84 665 | 8 782 | 20,11 | 6,27 | 2019-2023 (269 / 271) |
| 2023 | 6 525 584 | 497 932 | 1 857 135 | 194 533 | « - » | 10 887 | 376 030 | 1 917 | 94 851 | 12 674 | 20,28 | 6,07 | 2019-2023 (269 / 271) |

« - » : tiret imprimé dans la source. Une case vide signifie que la ligne n'existe pas dans
l'édition retenue.

**CSV** :
- gestion : `gestion-education.csv`, `gestion-enseignement-superieur.csv`,
  `gestion-recherche-scientifique.csv`, `gestion-formation-professionnelle.csv`, `gestion-emploi.csv` ;
- développement : `developpement-*.csv`, mêmes ministères ;
- totaux de l'État sur les mêmes pages : `etat-gestion-hors-interets.csv` (2004-2023) et
  `etat-developpement-hors-principal.csv` (2008-2023 ; rupture entre 2008 et 2009, voir § 2.3, point 6).

### 2.3 Ruptures de périmètre, une à une

Les libellés sont ceux imprimés dans les tableaux. Chaque changement est une rupture : **jamais
de somme silencieuse**.

1. **Éducation.**
   - 1997-2001 : « Education Nationale ».
   - 2002-2008 : « Education et Formation Professionnelle » au tableau 16.8, « Education Nationale et
     Formation » au tableau 16.10. **La formation professionnelle y est comprise.**
   - Depuis 2009 : « Education », la formation professionnelle étant comptée à part.
   - En 2009, l'édition 2006-2010 donne 2 631 926 pour l'Éducation et la Formation, ce qui égale
     2 541 221 + 90 705 de l'édition 2007-2011 : la rupture se raccorde exactement en gestion. En
     développement, en revanche, l'édition 2006-2010 donne 155 084 pour 2009, contre 195 576 + 14 149
     dans l'édition 2007-2011. Cette révision n'est pas expliquée.
2. **Formation professionnelle.**
   - 1997-2001 : « Formation Professionnelle et Emploi », qui inclut l'emploi.
   - 2002-2008 : comprise dans l'Éducation.
   - 2009-2013 : ligne propre.
   - **2014-2019** : « - » en gestion. Elle est alors comptée dans « Emploi », qui saute de 52 649
     (2013) à 245 750 (2014) : c'est la mission « Formation professionnelle et emploi ». En
     développement, elle garde une petite ligne propre (504 à 1 914).
   - Depuis 2020 : ligne propre.
   - Au tableau 16.9 de 2022 et de 2023, elle est de nouveau fondue dans « Emploi » : 424 596 =
     339 931 + 84 665 en 2022.
   - Une série « formation professionnelle » cohérente n'existe donc que pour 2009-2013 et 2020-2023.
3. **Enseignement supérieur et recherche.**
   - 1997-2001 : « Enseignement Supérieur ».
   - 2002-2004 : « Enseig. Sup. et recherche scientifique », recherche comprise.
   - 2005-2018 : recherche scientifique en ligne propre, d'abord « recherche scientifique et
     Technologie », puis « … et développement des compétences » en 2008.
   - **Depuis 2019, la recherche n'a plus de ligne en gestion** (« - ») : elle est comprise dans
     l'Enseignement supérieur. En développement, elle garde sa ligne.
   - La question Q10 du plan (retirer ou non la recherche) n'est tranchable qu'en 2005-2018.
4. **Écart Enseignement supérieur.** Pour 2012, l'Enseignement supérieur et la Recherche de l'Annuaire
   (982 727 + 34 848 = 1 017 575) ne valent pas tout à fait les réalisations de gestion du PAP 2014 de
   la mission (1 018 212, tableau 1, p. 13). L'écart est de 637, non expliqué.
5. **Nomenclature par nature (tableau 16.9).**
   - En 2001, le tableau a quatre colonnes : rémunération, biens et services, subventions, autres.
   - Depuis 2003, trois colonnes : rémunération, biens et services, autres dépenses.
   - Deux sauts sans commentaire de la source, en « autres dépenses » de l'Éducation : 44 670 (2016)
     puis 338 570 (2017) ; et en « biens et services » : 100 044 (2017) puis 373 586 (2020). Ils ont
     l'allure de reclassements, à confirmer sur les budgets détaillés.
   - Les PAP 2014 confirment que « Biens et services » vaut « moyens des services » (وسائل المصالح) et
     que « Autres dépenses » vaut « interventions publiques » (التدخل العمومي).
6. **Développement : rupture entre 2008 et 2009 dans toutes les séries.** Pour 2009, le
   développement total vaut 2 594 045 dans l'édition 2006-2010, contre 3 274 255 dans l'édition
   2007-2011. Pour l'Éducation, c'est 155 084 contre 195 576 + 14 149. L'ampleur de l'écart
   indique un **changement de périmètre**, pas une révision.
   - Depuis l'édition 2007-2011, le tableau 16.10 porte « Section 3 : dépenses de développement ».
   - En 2017, ce total (5 123 802) est proche de la section III de la loi de règlement
     (5 125 717 213 D), qui comprend la 9e partie, « dépenses de développement sur ressources
     extérieures affectées ».
   - Hypothèse, non vérifiée : les éditions antérieures excluent cette partie.
   - Tous les `developpement-*.csv` sont donc **à tracer en deux segments, 1997-2008 et
     2009-2023**, et la part dans l'État commence en 2009.
7. **Emploi en 2002.** La ligne vaut 91 100 en 2002, puis 24 200 en 2003 (éditions 2000-2004 et
   2001-2005). La source ne dit pas pourquoi : c'est une autre rupture.
8. **Totaux de l'État.** Avant 2008, les totaux imprimés comprennent les intérêts (titre I, « Total
   Brut ») et le principal de la dette (titre II). Le « Total Net » du titre I est hors intérêts
   depuis l'édition 2002-2006 seulement. Avec la rupture du point 6, la part dans le budget n'est
   calculée qu'à partir de 2009.
9. **Mauvaises impressions repérées, non retenues.**
   - Édition 1998-2002, tableau 16.8, p. 258 : les libellés sont décalés d'une ligne. Le montant de
     l'Éducation (1 424 200) se trouve en face de « Enseig. Sup. et recherche scientifique », et
     celui-ci (387 400) en face de « Emploi ».
   - Même édition, tableau 16.9, p. 259 : « 1 424 00 » et « 1 363 00 » sont imprimés tels quels.
   - Cette édition n'est utilisée pour aucune valeur.

### 2.4 Parts calculées

Ces deux séries sont **calculées par la note**, donc à refaire par le générateur.

- **`calcul-part-education-superieur-depenses-etat.csv`** (2009-2023).
  - Numérateur : gestion + développement de l'Éducation, de l'Enseignement supérieur et de la
    Recherche, tous lus aux tableaux 16.8 et 16.10.
  - Dénominateur : total des dépenses de gestion hors intérêts + total des dépenses de développement
    hors principal, lus sur les mêmes pages.
  - Cette part ne dépend d'aucune base de PIB. Elle passe de 29,3 % en 2009 à 20,3 % en 2023.
  - 2008 est exclu à cause de la rupture du développement (§ 2.3, point 6).
  - La formation professionnelle est **exclue**. Depuis 2019, la recherche est comprise dans
    l'Enseignement supérieur en gestion.
- **`calcul-part-education-superieur-pib.csv`** (2010-2023).
  - Même numérateur, rapporté au PIB nominal de `denominateurs-depenses-etat-pib`.
  - **Base 2015** de l'INS ; les années **2010-2014 sont rétropolées par l'INS**.
  - Résultat : de 5,8 % à 6,9 %.
  - Avant 2010, le PIB de cette série est en base 1997 (2005-2009). Le segment n'est pas calculé ici
    et devra se tracer à part, avec renvoi à `precis/fr/annexe-pib.qmd`.

### 2.5 Crédits initiaux de la loi de finances (JORT) : la source longue période

Les **décrets, puis arrêtés, portant répartition des crédits du budget de l'État** paraissent au
JORT chaque fin d'année. Leur tableau « A » ventile le titre I par chapitre (un ministère), par
partie (rémunérations, moyens des services, interventions) et par article. Le tableau « B »
ventile le titre II.

- `jort_cache` donne **59 notices de 1956 à 1994** pour la requête FTS « repartition credits budget ».
  Ce sont des arrêtés de 1956 et des décrets de répartition par article : n° 65-356 (1965), puis
  1971 et 1973 à 1977, avec des trous. Leur liste complète reste à dresser ; et **une cinquantaine de 1995 à 2026**. Les derniers sont l'arrêté du
  9 mars 2026 (JORT 2026/027, p. 370-383) et celui du 28 avril 2025 (JORT 2025/051, p. 1042-1056).
- **Lu à l'image, un exemple** : décret n° 2009-3750 du 21 décembre 2009, loi de finances pour 2010,
  JORT n° 102 du 22 décembre 2009, éd. fr., p. 4112 (articles) et p. 4126-4127 (tableau A). En
  dinars :
  - Chapitre 27, « Ministère de l'Éducation et de la Formation », « 1- Éducation » : **2 686 605 000**,
    dont rémunérations publiques 2 583 983 000, moyens des services 73 136 000, interventions
    publiques 29 486 000 (p. 4126).
  - Même chapitre, « 2- Formation » : **105 967 000** ; total du chapitre 27 : **2 792 572 000**
    (p. 4126).
  - Chapitre 28, « Ministère de l'Enseignement supérieur, de la Recherche scientifique et de la
    Technologie », « 1- L'enseignement supérieur » : **818 596 000**, dont rémunérations
    625 045 000, moyens 76 401 000, interventions 117 150 000 (p. 4127).
  - Même chapitre, « 3- La recherche scientifique et la technologie » : **30 513 000** ; total du
    chapitre 28 : **849 109 000** (p. 4127).
  - CSV : `jort-credits-initiaux-gestion-{education,formation-professionnelle,enseignement-superieur,recherche-scientifique}.csv`,
    une ligne chacun.
- **État : OCR nécessaire.** Dans les fascicules, ces pages n'ont pas de couche texte. L'essai
  tesseract (`fra`, 200 ppp, pages 205-236 du fichier) retrouve les en-têtes et les totaux des
  chapitres, mais chaque montant doit être relu à l'image. Les pages sont connues pour chaque année
  par `jort_cache`. C'est la voie pour remonter **avant 1997**, et pour donner la série des crédits
  votés à côté de celle des réalisations.

### 2.6 Lois de règlement

`jort_cache` indexe les lois de règlement des gestions 1954-55 à 2020 : en français jusqu'en 2009
et pour 2017-2020, en arabe (« يتعلق بغلق ميزانية الدولة ») pour 2010-2016. Elles donnent, en
articles, les dépenses payées par partie, pas par ministère.

Exemple : gestion 2017, loi n° 2024-18, JORT n° 35 de 2024, p. 800 :

- section I, dépenses de fonctionnement : 21 237 640 250,881 D ;
- rémunérations publiques : 14 352 388 707,921 D ;
- section III, développement : 5 125 717 213,086 D.

La ventilation par chapitre se trouve dans des « tableaux n° 2, 2-1 et 2-2 annexés », qui
n'apparaissent pas dans le texte extrait des fascicules français lus (JORT 2010/097 et 2024/035).
Fiche `r-educ-lois-reglement-tableaux-par-chapitre`.

Aucune loi de règlement n'est indexée pour 2021 et après : fiche `r-educ-lois-reglement-2021-et-apres`.

---

## 3. Par niveau : le budget par programmes (PAP 2014)

Ce sont les projets annuels de performance 2014 (décembre 2013), sur l'ancien portail du ministère
des Finances. Ils sont déjà dans l'entrepôt, lus à l'image. Unité : millier de dinars, crédits de
paiement. On a trois stades : **réalisations 2012** (إنجازات), **loi de finances 2013** (ق م),
**propositions 2014**.

| Programme | 2012 réal. | 2013 LF | 2014 prop. | Source | Page |
|---|---|---|---|---|---|
| Éducation, P1 : primaire (المرحلة الابتدائية) | 1 079 074 | 1 167 454 | 1 212 059 | PAP Éducation 2014, tableau 2 | 6 |
| Éducation, P2 : préparatoire et secondaire (المرحلة الإعدادية والتعليم الثانوي) | 2 049 506 | 2 151 340 | 2 257 288 | idem | 6 |
| Éducation, P3 : pilotage et appui (القيادة والمساندة) | 155 178 | 188 541 | 189 366 | idem | 6 |
| Éducation, total | 3 283 758 | 3 507 335 | 3 658 713 | idem (tableau 1 : gestion 2012 = 3 007 491, dont rémunérations 2 898 046) | 6 |
| ESRS, P1 : enseignement supérieur | 808 057 | 894 469 | 974 090 | PAP ESRS 2014, tableau 2 | 14 |
| ESRS, P2 : recherche scientifique | 81 011 | 105 530 | 97 932 | idem | 14 |
| ESRS, P3 : services universitaires (الخدمات الجامعية) | 247 991 | 278 747 | 275 927 | idem | 14 |
| ESRS, P4 : pilotage et appui | 44 305 | 60 328 | 57 331 | idem | 14 |
| ESRS, total | 1 181 364 | 1 339 074 | 1 405 280 | idem | 14 |
| FPE, programme formation professionnelle | 228 275 | 263 043 | 254 639 | PAP FPE 2014, tableau par programmes, **y compris le Fonds national de l'emploi 21-21 et les ressources propres des établissements** (note * du tableau) | 7 |

CSV : `programme-*.csv`.

Le PAP de l'Éducation (p. 5) dit que le découpage des programmes a été choisi **par cycle** plutôt
que par fonction. Le primaire et le « préparatoire et secondaire » y sont donc des niveaux, pas des
fonctions. Le préscolaire public n'a pas de programme propre.

**Mise en place du budget par programmes** (question du plan, § 8.3) : les PAP de 2014 sont les
plus anciens trouvés dans l'entrepôt. Le PAP de la Formation professionnelle et de l'Emploi
(p. 4-5) parle d'un passage « progressif » à la gestion budgétaire par objectifs. La date du
premier budget voté par programmes reste **à établir**, avec la loi organique du budget n° 2019-15
du 13 février 2019 (JORT 2019/015, index ; à lire).

**À lire** : les budgets 2015-2017 en arabe (`2015_budget_leducation_ar_jd795.pdf`, etc.), puis les
PAP et RAP 2018-2026 sur finances.gov.tn (non téléchargés). Ils prolongent la série par programme.

---

## 4. Effectifs et personnels (statistique, relayée par l'INS)

La source est l'INS, *Annuaire statistique*, chapitre « Enseignement et culture », tableau des
données générales de l'enseignement. Les sources citées sont le ministère de l'Éducation et le
ministère de l'Enseignement supérieur.

Les pages :
- p. 53 de l'édition 1995-2001 ;
- p. 57 des éditions 1999-2003, 2000-2004, 2001-2005 et 2002-2006 ;
- p. 55 des éditions 2003-2007 et 2004-2008 ;
- p. 47 des éditions 2005-2009 et 2006-2010 ;
- p. 49 des éditions 2007-2011 et 2008-2012 ;
- p. 43 depuis l'édition 2010-2014.

Une valeur par année scolaire, prise dans l'édition la plus récente qui la contient.

| Année scolaire | Élèves, 1er cycle de base, public | Élèves, 2e cycle et secondaire, public | Privé, 1er cycle | Privé, 2e cycle et sec. | Enseignants, 1er cycle (public) | Enseignants, 2e cycle et sec. (public) | Étudiants (total) | dont ministère de l'Ens. sup. | Enseignants du supérieur (public) | Édition (p.) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1995-1996 | 1 460 101 | 725 926 | 8 897 | 68 468 | 59 432 | 30 170 | 112 634 |  | 6 481 | 1995-2001 (53) |
| 2000-2001 | 1 363 393 | 962 985 | 10 511 | 53 011 | 60 072 | 45 803 | 207 388 |  | 10 293 | 2000-2004 (57) |
| 2005-2006 | 1 120 424 | 1 075 517 | 13 990 | 58 660 | 58 281 | 62 528 | 321 838 | 301 138 | 16 919 | 2005-2009 (47) |
| 2010-2011 | 1 003 017 | 936 398 | 24 953 | 54 918 | 57 349 | 72 454 | 336 017 | 310 365 | 21 552 | 2010-2014 (43) |
| 2012-2013 | 1 029 559 | 908 600 | 33 732 | 63 784 | 59 786 | 73 490 | 304 365 | 283 189 | 22 878 | 2012-2016 (43) |
| 2015-2016 | 1 079 001 | 893 348 | 60 313 | 58 706 | 64 944 | 75 056 | 255 783 | 237 901 | 22 648 | 2015-2019 (43) |
| 2020-2021 | 1 202 667 | 980 463 | 101 091 | 82 180 | 68 871 | 73 474 | 232 614 | 216 167 | 23 016 | 2019-2023 (43) |
| 2023-2024 | 1 205 640 | 1 034 515 | 128 513 | 108 591 | 72 213 | 70 695 | 266 837 | 250 249 | 23 545 | 2019-2023 (43) |

Les séries complètes couvrent 1995-1996 à 2023-2024, 29 années scolaires. La colonne « dont
ministère de l'Enseignement supérieur » commence en 2001-2002.

CSV : `eleves-public-premier-cycle-base.csv`, `eleves-public-second-cycle-base-secondaire.csv`,
`eleves-prive-*.csv`, `enseignants-public-premier-cycle-base.csv`,
`enseignants-public-second-cycle-base-secondaire.csv`, `enseignants-public-superieur.csv`,
`etudiants-total.csv`, `etudiants-ministere-enseignement-superieur.csv`.

**Réserves.**

- **Désignation des années.** Les éditions écrivent l'année scolaire « 24-23 » pour 2023-2024.
  L'édition 2002-2006 imprime « 05-06 » en tête de la colonne 2006-2007. Les années ont donc été
  attribuées par la position de la colonne, et contrôlées par recoupement entre éditions.
- **Révisions entre éditions.**
  - Enseignants du 2e cycle en 2009-2010 : 75 104 (édition 2005-2009), puis 72 194 (édition
    2006-2010).
  - Enseignants du supérieur, 2018-2019 à 2020-2021 : l'édition 2016-2020 paraît décalée d'une année
    par rapport aux suivantes (22 086 pour 2020-2021, que l'édition 2017-2021 donne pour 2019-2020).
  - La dernière édition est retenue.
- **Erreur d'addition dans la source.** Édition 1995-2001, total du 1er cycle en 1999-2000 :
  1 440 795 est imprimé, alors que public + privé = 1 403 729 + 10 066 = 1 413 795, ce que donne
  l'édition 1999-2003. Seuls les effectifs du public et du privé sont repris.
- **Périmètre.**
  - La ligne « Ecole de qualification technique » (EQT) est hors public et hors privé ; elle n'est
    pas reprise.
  - Les enseignants sont ceux du **public**.
  - Le **préscolaire** n'est pas dans ce tableau.
  - La **formation professionnelle** non plus. Ses effectifs sont **à obtenir** (Agence tunisienne
    de la formation professionnelle).
- **Année scolaire et année budgétaire.** L'année scolaire N/N+1 chevauche deux exercices
  budgétaires. Le coût par élève de l'exercice N se rapporte soit à N-1/N, soit à N/N+1, soit à leur
  moyenne. La méthode doit le dire.
- **Agents des ministères.** Les agents des ministères (`ins-ministere-effectifs-2018-2025`) ne sont
  pas des enseignants. Le ministère de l'Éducation compte 194 430 agents en 2018, pour 72 887 +
  63 228 = 136 115 enseignants du public en 2018-2019.
- **Masse salariale.** La masse salariale des ministères est la colonne « Rémunération » du tableau
  16.9 (`nature-*-remunerations.csv`, 2001 à 2023 avec des trous). Exemple : Éducation 6 093 395
  milliers de dinars en 2023 (édition 2019-2023, p. 270). C'est celle **de tout le ministère**, non
  des seuls enseignants ; pour les années les plus récentes d'une édition, c'est un chiffre
  provisoire.

---

## 5. Le coût public par élève et par étudiant

### 5.1 Ce que publient les sources budgétaires

Aucune source lue ne publie un **coût par élève** budgétaire. Les PAP 2014 ont des fiches
d'indicateurs (Éducation, annexes p. 33 et suivantes, et p. 67 et suivantes), qui n'ont **pas été
lues**. Un indicateur de coût y est possible : à lire.

### 5.2 Calcul indicatif possible (pour la méthode, non pour publication en l'état)

Numérateur : programmes du PAP 2014, réalisations 2012, crédits de paiement, ressources propres
exclues. Dénominateur : élèves du public de l'Annuaire.

| Niveau | Numérateur (milliers DT) | Effectifs 2011-2012 | DT par élève | Effectifs 2012-2013 | DT par élève |
|---|---|---|---|---|---|
| Primaire (1er cycle de base) | 1 079 074 (P1) | 1 014 836 | 1 063 | 1 029 559 | 1 048 |
| Préparatoire et secondaire | 2 049 506 (P2) | 922 458 | 2 222 | 908 600 | 2 256 |
| Supérieur, programme enseignement supérieur seul | 808 057 | 306 443 (étudiants du ministère) | 2 637 | 283 189 | 2 853 |
| Supérieur avec les services universitaires | 1 056 048 (P1 + P3) | 306 443 | 3 446 | 283 189 | 3 729 |

**Méthode à arrêter (Q9).**
- Le pilotage et appui de l'Éducation (155 178) est à répartir ou non.
- Le développement est inclus dans les crédits de paiement des programmes.
- La recherche est exclue du supérieur.
- Les services universitaires (restauration, logement, bourses) sont-ils un coût d'enseignement ou
  une aide du chapitre 5 ?

### 5.3 Les coûts unitaires de l'exercice d'incidence 2021 (évaluation)

Source : `~/projets/ceq-tunisie/CEQ_TUN21_March2025/3.Results/TUN_FiscalSim21_Sim2024_11March2025.xlsm`,
feuille « Parameters », bloc « Éducation », ligne « Dépenses par étudiant en DTN ». C'est un
classeur **non publié**.

| Niveau | 2021 (col. C) | Cellule |
|---|---|---|
| Enseignement primaire | 1 931 | C185 |
| Éducation secondaire | 3 612,9 | C186 |
| Éducation tertiaire | 8 057 | C187 |

**Méthode lue dans `2.DoFiles/09_Education.do`.**

- **Bénéficiaires.** Tout individu de l'enquête EBNCV 2021 scolarisé dans le public, au primaire, au
  secondaire (collège et lycée) ou au supérieur, compté à la pondération de l'enquête.
- **Coût unitaire moyen**, imputé en espèces au ménage puis rapporté par tête.
- **Ce qui n'est pas imputé.** Le préscolaire est commenté « Not available ». La formation
  professionnelle n'est pas imputée. Rien n'est imputé au privé.
- **Provenance déclarée.** « Unit cost reported by the ministry of education » pour le primaire et
  le secondaire, « … by the ministry of high education » pour le supérieur. **Aucun document ni
  date n'est donné.**

**Deux pièges du classeur.**
- La colonne D (2341,48 ; 3960,04 ; 8454,46) donne des valeurs **revalorisées pour 2024**, non des
  valeurs de source.
- La feuille « Education » lit `TRANSPOSE(Parameters!D185:D187)*1000`. Les valeurs qu'elle contient
  ne sont donc pas en dinars.

À comparer : les 8 057 DT du supérieur dépassent de loin le calcul du § 5.2 pour 2012 (2 637 à
3 729 DT). Le périmètre de la source CEQ (recherche, œuvres universitaires, ou les deux) est
inconnu. Fiche `r-educ-cout-unitaire-ministere-2021`.

CSV : `evaluation-ceq-2021-cout-unitaire-{primaire,secondaire,superieur}.csv`. Ils sont à ranger
dans la famille « évaluations », pas dans le budgétaire.

---

## 6. Rapports extérieurs : UNESCO-UIS par la Banque mondiale (chapitre 8)

**Qui, quoi.** Banque mondiale, *World Development Indicators*, indicateurs de source UNESCO-UIS.
API `api.worldbank.org/v2/country/TUN/indicator/<code>?format=json`, consultée le 17 octobre 2026
(mise à jour du 8 octobre 2026). Copies JSON dans `/tmp/education-ocr-D/raw/wb/`, avec leur SHA-256.
**À verser dans `tunisia-data`** (`data/raw/banque-mondiale/`).

**Méthode** (note de l'indicateur, lue) : « General government expenditure on education (current,
capital, and transfers) … includes expenditure funded by transfers from international sources to
government. General government usually refers to local, regional and central governments. »

Le périmètre est donc celui des **administrations publiques**, transferts compris (bourses), et
non celui des seuls ministères. La base du PIB n'est pas précisée par la source.

| Code | Intitulé | Années disponibles | CSV |
|---|---|---|---|
| SE.XPD.TOTL.GD.ZS | dépense publique d'éducation, % du PIB | 1980-1986, 1990-1997, 1999-2010, 2012, 2015, 2019-2023 (6,73 % en 2023) | `rapport-uis-depense-education-pct-pib.csv` |
| SE.XPD.TOTL.GB.ZS | % des dépenses des administrations publiques | 1992-2025 avec trous (27,83 % en 2004 ; 17,28 % en 2025) | `rapport-uis-depense-education-pct-depenses-publiques.csv` |
| SE.XPD.PRIM.PC.ZS | par élève du primaire, % du PIB par habitant | 1997-2008 (9 années) | `rapport-uis-depense-par-eleve-primaire-pct-pib-hab.csv` |
| SE.XPD.SECO.PC.ZS | par élève du secondaire | 1997-2015 (10 années) | `rapport-uis-depense-par-eleve-secondaire-pct-pib-hab.csv` |
| SE.XPD.TERT.PC.ZS | par étudiant du supérieur | 1997-2015 (17 années) | `rapport-uis-depense-par-etudiant-superieur-pct-pib-hab.csv` |

**Anomalie de la source.** SE.XPD.TOTL.GB.ZS vaut **0** pour 1981-1986, 1990 et 1991, des zéros
qui notent manifestement l'absence de donnée. Ils sont exclus du CSV.

La part UIS de 2022 (19,97 %) et la part budgétaire calculée (20,11 %) sont proches. Elles ne se
superposent qu'en figure, familles distinguées, puisque leurs périmètres diffèrent.

---

## 7. La dépense des ménages (chapitre 6, section 8)

Source : INS, *Enquête nationale sur le budget, la consommation et le niveau de vie des ménages
2021*, communiqué de presse. Fichier `EBCNV2021_Communiqué_Fr.pdf`, téléchargé le 17 octobre 2026
dans `/tmp/education-ocr-D/raw/ins/`, SHA-256 `00428c8b04be5290b7834304be0e300980fb1f1876c868c8586f6f187aa56f17`,
**à verser dans `tunisia-data`**.

Tableau « Structure de la dépense moyenne par personne et par an 2015-2021 », ligne « Education,
enseignement » (COICOP), page 2 du fichier, non numérotée :

| Année | DT courants par personne et par an | Coefficient budgétaire |
|---|---|---|
| 2015 | 84 | 2,2 % |
| 2021 | 81 | 1,5 % |

CSV : `menages-depense-education-par-personne.csv`, `menages-coefficient-budgetaire-education.csv`.

La ventilation (frais de scolarité du privé, cours particuliers, fournitures) et la répartition
**par décile** sont **à obtenir** dans le volume détaillé. Fiche `r-educ-ebcnv-volume-depenses`.

Les chiffres de presse sur le « coût d'un élève pour les familles » (FTDES 2021, OTIC, ODC) sont des
estimations d'associations, sans méthode lisible. Ils ne sont pas retenus.

---

## 8. Bénéficiaires par décile (chapitre 6, section 9 ; chapitre 8)

### 8.1 Une étude publiée lue : Banque mondiale, 1995, sur l'enquête de 1990 (rapport extérieur)

Référence : Banque mondiale, *République tunisienne. Allégement de la pauvreté : bâtir sur les
acquis pour préparer l'avenir*, vol. II : Annexes, rapport n° 13993-TUN, août 1995. **Clé
existante : `bm-1995-pauvrete-annexes`** (`precis/fr/retraites/references.json`). Fichier
`tunisia-data/data/raw/banque-mondiale-rapports/wb_1995_13993_poverty_vol2_annexes.pdf`, annexe
D.1 « Éducation », section A « Répartition des subventions de l'éducation ». Pages 1 et 2 de
l'annexe, soit les pages 53 et 54 du fichier. Le document est scanné et sa couche texte est
fautive : les chiffres ont été lus à l'image.

**Méthode** (§ 1 de l'annexe, p. 1).
- Les bénéficiaires sont identifiés par les inscriptions de l'*Enquête 1990 sur le budget et la
  consommation des ménages* de l'INS.
- « Les inscriptions au secteur public sont multipliées par la subvention moyenne par étudiant
  (définie comme étant la charge courante moyenne par programme, nette d'amortissement) en 1990. »
- Les classes sont des classes de dépense de consommation par habitant (déciles).
- C'est un coût moyen ; le privé est hors champ.

**Résultats rapportés (1990).**

Page 1 de l'annexe :
- subvention moyenne de « 71 DT » par habitant et par an, tous programmes confondus ;
- « environ 50 DT » pour les 10 % les plus pauvres, contre le double pour les 10 % les plus
  riches, « jusqu'à environ 100 DT » ;
- 52 DT en milieu rural, contre 84 DT dans les centres urbains ;
- au primaire, « en moyenne à 40 DT par habitant parmi les 3 % les plus pauvres », et « moins de
  20 DT » pour le décile supérieur ;
- au secondaire et au supérieur, les 10 % les plus riches perçoivent des subventions « trois et
  vingt fois plus importantes » que les 10 % les plus pauvres.

Page 2 de l'annexe :
- la subvention représente « environ 10 % des dépenses totales par habitant » en moyenne, 35 %
  pour le décile le plus pauvre et 6 % pour le plus riche ;
- entre 1985 et 1990, la subvention par habitant a augmenté de « plus de 7 % » au primaire,
  d'« un peu moins de 7 % » au secondaire et d'« environ 9 % » au supérieur.

Ces valeurs sont citées, non mises en série (pas de CSV). Elles reviennent au chapitre 8,
section 1. Les graphiques 1 à 3 de l'annexe (pages suivantes) ne sont pas lus.

### 8.2 Le reste

L'exercice CEQ 2021 compte les bénéficiaires dans la microdonnée EBNCV 2021 (§ 5.3). Ses tableaux
par décile (feuilles « beneficiaries », « income_by_decile » du classeur) sont **non publiés** :
aucune valeur n'en est reprise. La première étude CEQ sur la Tunisie (enquête 2010) reste **à
identifier et à obtenir**. Les annexes D.1, pages 3 à 6, et les graphiques sont **à lire** ; une
étude d'incidence sur l'enquête de 1985 y est peut-être citée.

---

## 9. Collectivités locales (Q8)

Rien de lu dans cette passe. Le tableau des dépenses communales par fonction, s'il existe, relève
des séries `finances-locales-*` déjà en cache. **À vérifier** dans `finances-locales-ins-comptes`.

---

## 10. Références candidates

**Déjà présentes** (à réutiliser) :
- `ins-annuaire-2019-2023-sante` et `ins-annuaire-2017-2021-sante` (`precis/fr/sante/references.json`).
  Ce sont des éditions de l'Annuaire citées pour la santé ; on peut en créer une par édition pour
  l'éducation, sur ce modèle.
- `loi2024-18` et `loi2024-19` (`precis/fr/marche_travail/references.json`).
- `wb-wdi` (`precis/fr/references.json`) ; `ins-cnat-2015` et `minfin-indicateurs-fp` (dénominateurs).
- `bm-1995-pauvrete-annexes` (`precis/fr/retraites/references.json`).
- `wb-tunisia-per-2020` (`precis/fr/references.json`), à lire.

**À créer** (CSL-JSON ci-dessous) :

```json
[
 {"id": "ins-annuaire-statistique", "type": "book", "title": "Annuaire statistique de la Tunisie",
  "author": [{"literal": "Institut national de la statistique"}], "publisher": "INS", "publisher-place": "Tunis",
  "note": "éditions 1995-2001 à 2019-2023 ; chapitre 16 « Budget de l'État », tableaux 16.8-16.10 ; chapitre « Enseignement et culture », données générales"},
 {"id": "mineducation-pap-2014", "type": "report", "title": "المشروع السنوي للقدرة على الأداء لوزارة التربية لسنة 2014",
  "author": [{"literal": "Ministère de l'Éducation"}], "issued": {"date-parts": [[2013, 12]]}, "language": "ar",
  "note": "ancien portail du ministère des Finances, jdownloads cid 647 ; tunisia-data minfinances/portail_ancien/budgets_ministeres"},
 {"id": "mesrs-pap-2014", "type": "report", "title": "المشروع السنوي للقدرة على الأداء لوزارة التعليم العالي والبحث العلمي لسنة 2014",
  "author": [{"literal": "Ministère de l'Enseignement supérieur et de la Recherche scientifique"}], "issued": {"date-parts": [[2013]]}, "language": "ar",
  "note": "cid 649"},
 {"id": "mfpe-pap-2014", "type": "report", "title": "المشروع السنوي للقدرة على الأداء لمهمة التكوين المهني والتشغيل لسنة 2014",
  "author": [{"literal": "Ministère de la Formation professionnelle et de l'Emploi"}], "issued": {"date-parts": [[2013]]}, "language": "ar",
  "note": "cid 651"},
 {"id": "decret-2009-3750", "type": "legislation", "title": "Décret n° 2009-3750 du 21 décembre 2009, portant répartition des crédits du budget de l'État ouverts par la loi n° 2009-71 du 21 décembre 2009 portant loi de finances pour l'année 2010",
  "container-title": "Journal officiel de la République tunisienne", "issue": "102", "issued": {"date-parts": [[2009, 12, 22]]}, "page": "4112-4144",
  "URL": "https://www.pist.tn/jort/2009/2009F/Jo1022009.pdf"},
 {"id": "ins-ebcnv-2021-communique", "type": "report", "title": "Enquête nationale sur le budget, la consommation et le niveau de vie des ménages 2021 : communiqué",
  "author": [{"literal": "Institut national de la statistique"}], "issued": {"date-parts": [[2023]]},
  "URL": "https://ins.tn/sites/default/files-ftp3/files/publication/pdf/EBCNV2021_Communiqu%C3%A9_Fr.pdf", "note": "date de publication à vérifier (note de synthèse de février 2023)"},
 {"id": "unesco-uis-depense-education", "type": "dataset", "title": "UNESCO Institute for Statistics : dépense publique d'éducation (indicateurs repris par WDI : SE.XPD.TOTL.GD.ZS, SE.XPD.TOTL.GB.ZS, SE.XPD.PRIM.PC.ZS, SE.XPD.SECO.PC.ZS, SE.XPD.TERT.PC.ZS)",
  "author": [{"literal": "UNESCO Institute for Statistics"}], "accessed": {"date-parts": [[2026, 10, 17]]}, "URL": "https://databrowser.uis.unesco.org/resources", "note": "ou citer simplement wb-wdi avec le code d'indicateur"}
]
```

L'URL pist.tn du JORT n° 102 de 2009, édition française, a été vérifiée le 17 octobre 2026 :
`200 application/pdf 12067079`, et la première page porte « TRADUCTION FRANÇAISE ». Même
vérification pour le n° 35 de 2024 : `200 application/pdf 21293312`, en français.

---

## 11. Notions à glossaire

Aucune de ces notions n'existe dans `precis/glossaire.yml`, recherche faite sur les termes
français et arabes le 17 octobre 2026. Elles sont toutes **à créer**.

| FR | AR (forme des sources) | Source canonique pressentie |
|---|---|---|
| dépenses de gestion (titre I, section 1) | نفقات التصرف | loi organique du budget n° 67-53 ; Annuaire 16.8 |
| dépenses de développement (titre II, section 3) | نفقات التنمية | idem ; Annuaire 16.10 |
| rémunérations publiques / moyens des services / interventions publiques | التأجير العمومي / وسائل المصالح / التدخل العمومي | décret n° 99-529 (nomenclature des dépenses), visé par le décret n° 2009-3750 ; PAP 2014 |
| crédits de paiement, crédits d'engagement | اعتمادات الدفع / اعتمادات التعهد | PAP 2014 ; arrêtés de répartition depuis 2023 |
| mission, programme, projet annuel de performance (PAP), rapport annuel de performance (RAP) | مهمة، برنامج، المشروع السنوي للقدرة على الأداء | PAP 2014 ; loi organique du budget n° 2019-15 du 13 février 2019 (JORT 2019/015, index ; à lire) |
| loi de règlement du budget | قانون غلق ميزانية الدولة | loi n° 67-53, art. 45-46 (cités par la loi n° 2024-18) |
| répartition des crédits (tableaux A, B, C) | توزيع الاعتمادات | décret n° 2009-3750 |
| coût unitaire (coût public par élève) | كلفة التلميذ | à définir par le chapitre (Q9) |
| coefficient budgétaire (des ménages) | — | INS, EBCNV 2021 |
| 1er cycle / 2e cycle de l'enseignement de base, enseignement secondaire | المرحلة الأولى / الثانية من التعليم الأساسي، التعليم الثانوي | Annuaire, chapitre « Enseignement et culture » ; loi n° 2002-80 |
| services universitaires (œuvres universitaires) | الخدمات الجامعية | PAP ESRS 2014 |

---

## 12. Lacunes : lisible, OCR nécessaire, à obtenir

| Objet | État | Où |
|---|---|---|
| Dépense par ministère avant 1997 | **lisible ou OCR** : annuaires antérieurs à 1995-2001 absents de l'entrepôt (**à obtenir**) ; décrets de répartition des crédits 1965-1994 au JORT (**OCR nécessaire**, pages connues de `jort_cache`) | § 2.5 |
| Crédits initiaux 1995-2026 par ministère et par nature | **OCR nécessaire** (tableau A des décrets et arrêtés de répartition) ; 2010 lu | § 2.5 |
| Réalisations par chapitre (lois de règlement) | **à obtenir** : tableaux annexés absents des fascicules lus | fiche `r-educ-lois-reglement-tableaux-par-chapitre` |
| Édition 2009-2013 de l'Annuaire | **à obtenir** ; sans effet sur la série (années couvertes par les éditions voisines), mais elle donnerait la nature 2013 | — |
| Nature (16.9) pour 2002, 2013, 2018, 2019, 2021 | 2002 : misprint ; 2013 : édition manquante ; 2018, 2019, 2021 : les éditions ne donnent pas ces années | budgets détaillés ou lois de règlement |
| Budget par programmes 2015-2026 | **lisible** pour 2015-2017 (budgets ar de l'entrepôt, à lire) ; **à obtenir** pour 2018-2026 (PAP et RAP sur finances.gov.tn) | § 3 |
| Coût par élève publié par les ministères ; source des coûts CEQ 2021 | **à obtenir** | fiche `r-educ-cout-unitaire-ministere-2021` |
| Effectifs de la formation professionnelle et du préscolaire public | **à obtenir** (ATFP ; ministère chargé de l'enfance) | § 4 |
| Dépense des ménages par poste et par décile | **à obtenir** (volume EBCNV 2021 et 2015) | fiche `r-educ-ebcnv-volume-depenses` |
| Bénéficiaires par décile publiés ; étude CEQ sur l'enquête 2010 | **à obtenir** | § 8 |
| Indicateurs de coût des PAP 2014 (annexes) | **lisible**, non lu | § 5.1 |
| Loi de finances 2026, art. 107 (enseignants suppléants) | index seulement (plan) ; non lu ici | — |
| Copies WB/UIS et INS (communiqué EBCNV) dans `tunisia-data` | à verser (copies dans `/tmp/education-ocr-D/raw/`, SHA-256 au § 6 et au § 7) | — |

---

## 13. Recherches infructueuses

Quatre fiches **nouvelles**, proposées dans `docs/notes/education-recherches-D.yml`. Le registre
`docs/recherches.yml` n'a pas été modifié. Le champ `ou` vise le fichier pressenti
`precis/fr/education/_depense.qmd`, qui n'existe pas encore : l'ancre sera à poser à la rédaction.

- `r-educ-lois-reglement-tableaux-par-chapitre`
- `r-educ-lois-reglement-2021-et-apres`
- `r-educ-cout-unitaire-ministere-2021`
- `r-educ-ebcnv-volume-depenses`

`recherches.py lister` ne montrait aucune fiche existante sur ces objets.

Contrôle fait sur une copie du registre augmentée des quatre fiches
(`/tmp/education-ocr-D/recherches-test.yml`, chargée par `recherches.charger`) :
`erreurs_fiche` ne signale aucune erreur. `verifie` les déclare **orphelines**, faute d'ancre dans
`precis/fr` : c'est attendu tant que le chapitre n'est pas écrit.

Pour les fiches de la source `web` (coût unitaire, volume EBCNV), les termes JORT ont été joués
mais ne sont pas pertinents en eux-mêmes : la pièce attendue n'est pas un texte du *Journal
officiel*.
