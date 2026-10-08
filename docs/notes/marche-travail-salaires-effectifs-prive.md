# Salaires effectifs du secteur privé et part des salariés au SMIG — note documentaire

Volume « Marché du travail », longue période. Relevé du 8 octobre 2026. Chemins relatifs à
`~/projets/tunisia-data` (branche `main`) sauf mention contraire. Rien n'a été modifié dans les
dépôts ; quatre PDF ont été téléchargés dans le bac de travail pour lecture (§ 5.2).

## 0. Constat

**Le backlog est périmé.** `docs/notes/backlog-precis.md` (l. 1187) et le TODO de
`precis/fr/marche_travail/_longue_periode.qmd` (l. 7-9) disent « aucune série réunie ». Le dépôt
de données porte en réalité :

- un **niveau** du salaire annuel moyen déclaré à la CNSS (régime des salariés non agricoles),
  **1970-1999 et 2002-2006** dans une édition, **2000-2018** dans une autre, déjà en CSV ;
- un **taux d'évolution** du salaire du privé non agricole (INS d'après la CNSS), 2001-2025 ;
- la **pyramide des salaires déclarés en multiples du SMIG**, 2000-2010 en CSV, et jusqu'en 2018
  dans des PDF déjà présents ;
- trois enquêtes de l'INS auprès des entreprises (2012, 2014, 2022), téléchargées et non
  exploitées, qui donnent le salaire de base moyen **rapporté au SMIG par l'INS lui-même**.

Deux autres documents sont en retard sur les fichiers : dans `tunisia-data`,
`docs/croissances-revenus-prix.md` (« 1976-1983 : aucune source de salaire moyen ou de masse
déclarée retrouvée ») est contredit par `cnss_annuaire_2006_brut.csv`, versé le 5 octobre 2026 ;
et, dans le précis, la note `docs/notes/marche-travail-smig-smag.md` (§ 6-7 : « part des salariés payés
au SMIG : aucune source trouvée ») par les pyramides de la CNSS.

Ce qui manque vraiment : tout niveau après 2018 ; une part « au SMIG » sur un champ propre
(salariés à temps complet sur l'année) en série ; les années 1960-1969 en niveau continu.

## 1. Inventaire de ce que `tunisia-data` porte

### 1.1 Données des producteurs (CNSS, INS)

| Série | Producteur | Définition exacte | Période, fréquence | Fichier produit (`data/processed/`) | Fiche, entrée du catalogue | Réserves |
|---|---|---|---|---|---|---|
| Employeurs, salariés déclarés, masse salariale, **salaire annuel moyen déclaré**, RSNA | CNSS, annuaire statistique 2006 (scan français, p. imprimée 1 / PDF 14) | masse des salaires déclarés ÷ salariés déclarés dans l'année, dinars par an ; salaire soumis à cotisation — brut du salarié, hors cotisations patronales : **déduit**, la source ne le dit pas (la Banque mondiale, 2004, note 18, dit l'ignorer) | 1970-1999, 2002-2006, annuelle (2000-2001 masquées par le pli du scan) | `caisses/cnss_annuaire_2006_brut.csv` (indicateurs `masse salariale déclarée`, `salariés déclarés`, `salaire annuel moyen déclaré`) | `sources/cnss-annuaires.md` ; `cnss-annuaire-2006-brut` | lecture à l'image ; ICP hors assiette de 1981 à 1987, incluse avec « MIT » à partir de 1988 ; taxis et louages sortis en 2003 ; 2000-2006 **non comparables** aux éditions suivantes (voir 1.4) ; aucune URL d'origine |
| Idem | CNSS, annuaire 2018 (français, PDF 16) ; mêmes valeurs dans les éditions 2010 (PDF 22), 2013 (PDF 26), 2016 (PDF 26), 2017 (PDF 23) | idem ; le salaire moyen publié divise par les salariés **hors non-assujettis** ; l'édition 2013 exclut explicitement les employeurs déclarant néant | 2000-2018, annuelle | `caisses/cnss_annuaire_2018_brut.csv` ; aussi `cnss_annuaire_2016_brut.csv`, `cnss_rsna_annuaires.csv` (2000-2017, éditions 2013 et 2017) | idem ; `cnss-annuaire-2018-brut`, `cnss-annuaire-2016-brut`, `cnss-rsna-annuaires` | rupture de 2003 (employeurs −12,26 %, taxis et louages) ; **rien après 2018** ; édition 2018 sans URL d'origine |
| Pyramide des salaires mensuels déclarés **en multiples du SMIG**, treize classes | CNSS, annuaire 2010 (arabe, PDF 29) | effectif de salariés déclarés par classe : ≤ 2/3 SMIG, 2/3-1, 1-1,5, … , > 6 | 2000-2010, annuelle | `caisses/cnss_annuaire_2010_pyramide_smig_brut.csv` | `sources/cnss-annuaires.md` ; `cnss-annuaire-2010-pyramide-smig-brut` | classe basse gonflée par les déclarations partielles (voir § 4.1) ; SMIG de référence et calcul du « salaire mensuel » non écrits par la source |
| Idem, édition 2006 | CNSS, annuaire 2006 (PDF 21) | idem | 2000-2006 | `caisses/cnss_annuaire_2006_pyramide_smig_brut.csv` | idem ; `cnss-annuaire-2006-pyramide-smig-brut` | autre univers que l'édition 2010 : en 2000, 972 979 salariés et 10,9 % sous 2/3 SMIG, contre 771 884 et 27,4 % |
| Ventilations par branche et par taille (employeurs, salariés, masse) | CNSS, annuaires 2006, 2016, 2018 | une année par édition | 2006, 2016, 2018 | `caisses/cnss_annuaire_<édition>_ventilation_<activite\|taille>_brut.csv` | idem | catégories non raccordées d'une édition à l'autre |
| **Taux d'évolution trimestriel du salaire, privé non agricole** | INS d'après la CNSS (BMS, tableau 2.2 ; portail, page `statistiques/99` ; premier portail, indicateur 0402040) | variation du salaire moyen d'un **panel de salariés permanents** (déclarés cinq trimestres de suite ; salaires trimestriels < 300 D ou > 60 000 D exclus ; évolutions individuelles hors [−5 % ; +10 %] exclues) | T1 2001 - T4 2025, trimestrielle | `ins-bms/salaires_prive_trimestriel_retenu.csv`, `…_editions.csv` | `sources/ins-bms-salaires-prive.md` ; `ins-salaires-prive-trimestriel`, `-editions` | **taux seulement, aucun niveau** ; 2001-2007 par deux pages archivées qui ne nomment ni la CNSS ni la méthode ; méthode connue par le seul guide de 2026 ; 52 trimestres sur 75 révisés |
| Taux annuel correspondant | idem | chaînage des quatre trimestres (colonne `taux_chaine`) ; taux annuels publiés par l'INS 2010-2022 (colonne `taux_annuel_ins`) | 2001-2025, annuelle | `ins-bms/salaires_prive_annuel.csv` | idem ; `ins-salaires-prive-annuel` | 2025 provisoire ; écart de 1,01 point avec l'INS en 2022 (révisions) |
| SMIG (48 h, 40 h) et SMAG | décrets ; série du précis | montants mensuels par date d'effet ; moyenne annuelle du SMIG 48 h | 1961-2028 par date d'effet ; moyenne annuelle 1962-2023 | précis : `precis/fr/marche_travail/figdata/fig_mt_nominal.csv`, `fig_mt_reel.csv` (série `marche-travail-smig-smag`) | `sources/jort-smig-smag.md` ; `jort/smig_smag_decrets.csv` (liste de décrets) | avant 1974, conversion du minimum horaire de la première zone ; `bct/smig_smag_ra.csv` : trois valeurs sans date, inutilisable |
| Occupés par statut (part des salariés) | INS, enquête emploi | effectifs | 1999-2012 | `ins-enquete-emploi/occupes_statut.csv` | `enpe-occupes-statut` | dénominateur possible, pas un salaire |

### 1.2 Banque centrale (rapports annuels) — ni source ni méthode publiées

| Série | Définition | Période | Fichier | Réserves |
|---|---|---|---|---|
| Masse des salaires déclarés à la CNSS, effectif déclaré | « salaires déclarés à la Caisse », toutes branches | masse 1959-1971, 1973-1975 ; effectif 1963-1971, 1973-1974 | `bct-archives/salaires_declares_cnss_1959_1975.csv` (`bct-salaires-cnss`) ; `sources/bct-archives.md` | plafond de 500 D par an supprimé en 1961 ; libellé de l'effectif changé quatre fois (rupture établie en 1971) ; trous 1962, 1972 ; niveaux révisés d'un rapport au suivant |
| Salaire annuel moyen des « secteurs productifs non agricoles » | hors agriculture et pêche, hors administration ; prose de la section « Salaires » | niveaux 1999-2005 (4 510 D en 1999, RA 1999 p. 111 du PDF ; 5 938 D en 2005) ; taux imprimés 1999-2007 ; 1998 : 4 938 MD pour 1 176 milliers de salariés | `bct-archives/salaire_moyen_secteurs_1998_2007.csv` (`bct-salaire-moyen-secteurs`) | niveaux révisés d'un rapport à l'autre (2005 : +5,7 % d'après les niveaux, +3,1 % imprimé) ; origine non dite (vraisemblablement le Plan) |

### 1.3 Rapports extérieurs déjà en dépôt (à ne pas mêler aux précédents ; une ligne chacun)

- Banque mondiale, rapport 13993-TUN (1995), tableau 41 : salaire moyen « Non Agr. & ADM », 1983-1993, source ministère du Plan, salariés estimés — `rapports-internationaux/bm1995_salaires_secteurs.csv`.
- FMI, rapport 97/57, tableau 5 : salaire annuel moyen « Other », huit années de 1981 à 1994 — `rapports-internationaux/fmi1997_salaires.csv`.
- Banque mondiale, rapport 25456-TUN (2004), tableau 8.1 : salaire annuel moyen déclaré à la CNSS, 1994-2000 — `caisses/bm2004_cnss_salaire_moyen.csv` ; niveau jugé inutilisable par sa propre fiche (voir 1.4).
- Présents en brut, non dépouillés : annuaires du BIT 1945-1999 (`data/raw/banque-mondiale-rapports/ilo_yearbook_labour_statistics_*.pdf` ; l'édition 1996 porte une ligne « Tunisie — Wage earners — Dinars »), Banque mondiale 2015 *Labor Policy to Promote Good Jobs in Tunisia* (`data/raw/emploi/wb_2015_…_92871.pdf`).

### 1.4 Incohérences entre sources, à connaître avant tout tracé

- **Deux millésimes de l'annuaire de la CNSS sur 2000-2006.** Pour 2006 : 1 179 025 salariés, 5 807 877 150 D, 4 926 D par an (édition 2006) contre 936 103 salariés, 4 637 238 747 D, 4 954 D (éditions 2010 à 2018). Les effectifs diffèrent d'un quart, le salaire moyen de 0,6 %. En 2002, l'écart du salaire moyen est plus fort : 4 525 contre 3 856 D. Aucune note de la source ne l'explique ; diagnostic dans `sources/cnss-diagnostic-ecarts-annuaires-2006-2016.md`.
- **Le tableau 8.1 de la Banque mondiale (2004) ne redonne pas l'annuaire** : 1 772 D en 1995 et 2 244 D en 2000, contre 3 243 D (édition 2006, 1995) et 3 469 D (édition 2018, 2000). Il porte pourtant « source : CNSS ». Sa lecture en dinars reste à confirmer (la fiche lit la virgule comme séparateur de milliers) ; ne pas l'employer en niveau.
- **Taux de l'INS et salaire moyen de la CNSS ne mesurent pas le même objet** : de 2011 à 2013 le salaire moyen déclaré croît de 10,6 %, 11,3 % et 10,7 %, le taux chaîné de l'INS de 6,4 %, 7,4 % et 6,1 % ; en 2018, 4,6 % contre 6,0 %. Le premier suit tous les déclarés (composition et durée déclarée comprises), le second un panel de permanents écrêté.

## 2. Ce qui donne un niveau

### 2.1 Salaire annuel moyen déclaré à la CNSS — immédiatement disponible

Formule : `salaire annuel moyen déclaré` = `masse salariale déclarée` ÷ `salariés déclarés`
(colonnes `annee`, `indicateur`, `valeur` ; la colonne `page` donne la page). La source imprime
le quotient ; les scripts le contrôlent à l'unité.

Valeurs de contrôle :

| Année | Masse (D) | Salariés | Salaire moyen (D/an) | Source |
|---|---|---|---|---|
| 1970 | 74 205 000 | 201 532 | 368 | annuaire 2006, PDF 14 |
| 1987 → 1988 | 671 717 000 → 939 352 468 | 468 064 → 485 291 | 1 435 → 1 936 (+34,9 %) | annuaire 2006, PDF 14 ; rupture d'assiette (ICP et « MIT ») |
| 2000 | 2 677 461 453 | 771 898 | 3 469 | annuaire 2018, PDF 16 |
| 2013 | 9 842 490 396 | 1 158 655 | 8 495 | annuaire 2018, PDF 16 ; annuaire 2013, PDF 26 |
| 2018 | 14 921 270 502 | 1 289 940 | 11 567 | annuaire 2018, PDF 16 |

Limite de fond : le dénominateur compte **toute personne déclarée au moins une fois dans
l'année**. Le quotient est un salaire par tête déclarée, pas le salaire d'un emploi à l'année.

### 2.2 Salaire moyen d'une année complète — dans les PDF, non extrait

Les annuaires ventilent salariés et masse selon les trimestres déclarés, ce qui donne un niveau
plus proche d'un salaire à temps complet sur l'année. **La définition des colonnes change entre
éditions sous un titre presque identique :**

- **Annuaire 2013 (PDF 36)** : colonnes « 1, 2, 3, 4 trimestres » = nombre de trimestres
  déclarés (elles se somment au total, 1 158 655). Salariés déclarés quatre trimestres : 800 558,
  masse 8 834 648 773 D, soit **11 036 D par an**, contre 8 495 D pour l'ensemble.
- **Annuaires 2016 (PDF 36) et 2018 (PDF 20, 22, 25, 26)** : colonnes = effectif déclaré à chaque
  trimestre civil (2018 : 1 085 758, 1 106 904, 1 117 539, 1 123 883 ; les masses se somment à
  14 921 270 502 D). Masse annuelle ÷ effectif trimestriel moyen (1 108 521) = **13 461 D par
  an**, contre 11 567 D publié.

Ces deux mesures ne sont pas la même (salariés présents toute l'année ; effectif moyen) et ne se
raccordent pas. Les éditions 2010 et 2017 ne sont pas vérifiées sur ce point.

### 2.3 INS, enquête « Emploi et salaires auprès des entreprises » — en brut, non extraite

`data/raw/ins-enquete-emploi/enquete_emploi_salaire_2012.pdf` (42 p.), `enquête_emploi_salaires_2014.pdf`
(44 p.), `enquête_empl_salair-2022_0.pdf` (37 p.) ; adresses dans `sources/ins-enquete-emploi-urls.csv`.

- **Champ** : entreprises publiques et entreprises privées de **six salariés et plus**, tirées du
  répertoire national des entreprises ; taux de réponse 38,6 % (2012, p. 7), 46,6 % (2014, p. 6),
  58 % (2022, p. 5).
- **Grandeur** : **salaire de base** mensuel moyen versé aux **permanents** (hors heures
  supplémentaires et primes), par catégorie professionnelle et section d'activité, et le même
  « en pourcentage du SMIG » — SMIG retenu par l'INS : 301 D (2012), 320 D (2014), 460 D (2022),
  soit le régime de 48 heures.

| Année | Total (D/mois) | % du SMIG | Ouvriers (D/mois) | % du SMIG | Page |
|---|---|---|---|---|---|
| 2012 | 535 | 178 % | 380 | 126 % | p. 15, tableaux 15-16 |
| 2014 | 600 | 188 % | 447 | 140 % | p. 14 |
| 2022 | 924 | 201 % | 658 | 143 % | p. 13, tableaux 13-14 |

Réserves : entreprises publiques comprises (ce n'est pas le seul privé) ; salaire de base et non
brut ; les tableaux par division donnent 534 et 177 % pour 2012 (p. 36-37, arrondis) ; les
tableaux de quartiles « rapportés au SMIG » (2012 p. 16 ; 2014 ; 2022 p. 14) sont à lire à
l'image : l'ordre des colonnes diffère entre éditions, et la source ne dit pas s'il s'agit de
quartiles de salariés ou de moyennes d'entreprises. Les seules éditions en ligne sont 2012, 2014
et 2022 (catalogue du dépôt ; recherche web du 8 octobre 2026 ; la rubrique « Salaires » du
portail ne porte que le SMIG, le SMAG et le taux d'évolution).

### 2.4 INS, enquête quinquennale sur les micro-entreprises — en ligne, hors dépôt

Champ : entreprises non agricoles de **moins de six salariés** du répertoire (2007 : 503 536
unités, 8 172 répondantes, taux de réponse 56,6 %, rapport 2007 p. 7-8 du PDF). Complément exact
du champ de l'enquête précédente.

| Année | Salaire mensuel moyen (D) | SMIG retenu par l'INS (D) | Rapport | Source |
|---|---|---|---|---|
| 2002 | 219 | 204 | 1,0 (texte) | rapport 2007, p. 17-18 du PDF |
| 2007 | 241 | 240 | 1,0 | rapport 2007, p. 10 et 35 |
| 2012 | 343 | 301 | 1,1 | rapport 2012, p. 11, 16, 34 |
| 2016 | 432 | 357 | 1,2 | rapport 2016, p. 10, 16 |

Le SMIG de 204 D donné pour 2002 ne coïncide pas avec la série du précis (202,592 D au 1er juillet
2002, régime de 48 heures) : à signaler, non à corriger. Enquêtes de 1997 et de 2002 : rapports
non trouvés en ligne (une seule recherche ; à confirmer). L'adresse de l'édition 2022 répond 404.

### 2.5 CRES et BIT, enquête sur la structure des salaires, avril 2011 — en ligne, hors dépôt

Enquête ponctuelle (rapport final, octobre 2012, 58 p.) : 336 entreprises privées et 2 042
salariés, extrapolés à 47 000 entreprises du fichier des déclarations à la CNSS du quatrième
trimestre 2010 (p. 6 du PDF). Rémunération mensuelle moyenne totale 557 D, dont salaire **net**
de base 482,5 D ; distribution (p. 25, tableau 17) : premier décile 277 D, premier quartile
332 D, médiane 422 D, troisième quartile 576 D, neuvième décile 915 D. Le SMIG de 48 heures
valait alors 272,480 D. Incohérence interne : le texte (p. 7 et 25) dit une médiane de 442 D, le
tableau 422 D. C'est la seule distribution individuelle trouvée ; une année, salaires nets.

### 2.6 Ce qui ne donne pas de niveau

- INS, portail : taux seulement (1.1). Rubrique « Salaires » : SMIG, SMAG, taux d'évolution.
- INS, annuaires statistiques (22 éditions, 1995-2023) : le chapitre 6 « Emploi et salaire » ne
  porte que les tableaux du SMIG et du SMAG (vérifié sur les éditions 1995-2001, 2004-2008 et
  2019-2023).
- INS, enquête nationale sur la population et l'emploi : aucun salaire dans les rapports
  2005-2012 présents (recherche sur `emploi_2012.pdf` seulement ; à confirmer sur les autres).
- Recensements : non examinés.

## 3. Rapport au SMIG

**Oui, sur 1970-2018, avec ce qui est déjà produit**, sous la forme
salaire annuel moyen déclaré ÷ (12 × SMIG 48 h en moyenne annuelle) — numérateur : colonnes
ci-dessus ; dénominateur : colonne « SMIG 48 h, moyenne annuelle (D courants) » de
`fig_mt_reel.csv` (1962-2023).

Valeurs de contrôle : 1970 : 368 ÷ (12 × 17,472) = 1,76 ; 1980 : 1,60 ; 1987 : 1,19 ; 1988 : 1,48 ;
2000 : 3 469 ÷ (12 × 184,981) = 1,56 (édition 2018) ; 2013 : 2,35 ; 2018 : 11 567 ÷ (12 × 371,419)
= 2,60. Sur le recouvrement, l'édition 2006 donne 1,89 en 2002 là où l'édition 2018 donne 1,61 ;
elles se rejoignent en 2006 (1,80 et 1,81).

Segments et ruptures :

| Segment | Source | Rupture à son terme |
|---|---|---|
| 1970-1980 | annuaire 2006 | **1981** : l'indemnité complémentaire provisoire (10 D par mois au 1er avril 1981, 30,368 D au 1er février 1982) entre dans le SMIG mais reste **hors assiette des cotisations** (décret n° 81-437, art. 7 ; note `docs/notes/marche-travail-smig-smag.md` du précis, § 1.4-1.5). Le dénominateur la compte, le numérateur non |
| 1981-1987 | annuaire 2006 | rapport abaissé par construction (1,60 en 1980 ; 1,19 en 1985 et en 1987) ; **1988** : le tableau signale l'inclusion de l'ICP et de « MIT » à partir de 1988 (+34,9 % du salaire moyen ; sigle « MIT » non développé par la fiche). Le texte qui fait entrer l'ICP dans l'assiette en 1988 n'est pas identifié ici ; à lui seul, il n'explique pas toute la hausse |
| 1988-1999 | annuaire 2006 | 2000-2001 illisibles dans le scan |
| 2002-2006 | annuaire 2006 | **changement de millésime** : ne pas chaîner avec le segment suivant |
| 2000-2018 | annuaires 2010 à 2018 | **2003** : taxis et louages ; fin de la source en 2018 |
| 2001-2025 (indice) | INS, taux chaînés | autre objet (panel de permanents) : à tracer en indice base 100 face au SMIG en indice, sur un second panneau, jamais en prolongement du niveau |

Biais commun : le rapport est **tiré vers le bas** par les déclarations d'une partie de l'année
(§ 2.1). En 2013, le rapport passe de 2,35 à 3,05 pour les salariés déclarés quatre trimestres
(11 036 ÷ 3 621,7). Avant 1970 : les rapports de la BCT donnent masse et effectif pour 1963-1971
et 1973-1974, donc un salaire moyen, mais avec quatre définitions de l'effectif ; un rapport au
minimum légal (taux horaires par zone avant 1974) y serait fragile.

Points de repère indépendants, rapportés au SMIG par l'INS lui-même : entreprises de six salariés
et plus, 178 % (2012), 188 % (2014), 201 % (2022) ; micro-entreprises, 1,0 (2002, 2007), 1,1
(2012), 1,2 (2016).

## 4. Part des salariés au SMIG ou à son voisinage

Aucune source ne publie « la part des salariés payés au SMIG ». Trois sources l'approchent, sur
trois champs.

### 4.1 CNSS : pyramide des salaires déclarés en SMIG (RSNA), 2000-2018

- 2000-2010 : en CSV (annuaire 2010). 2000-2013 : annuaire 2013, PDF 37. 2005-2018 : annuaire
  2018, PDF 27. Les trois éditions concordent sur les années communes relues (2005, 2010, 2013).
  **2011-2018 restent à extraire** (couche texte, aucune océrisation).
- Lecture brute, part des déclarés sous 1 SMIG : 40,8 % en 2000, 34,9 % en 2010, 27,8 % en 2013,
  24,0 % en 2018 ; classe 1-1,5 SMIG : 24,8 %, 22,5 %, 18,1 %, 17,8 %.
- **Cette lecture brute ne mesure pas des salariés payés sous le SMIG.** En 2013, 115 611 des
  220 996 salariés de la classe « moins de 2/3 SMIG » n'ont qu'un trimestre déclaré (annuaire
  2013, PDF 36) : la classe basse est faite de déclarations partielles. Le « salaire mensuel »
  est donc vraisemblablement une masse annuelle rapportée à douze mois — **déduit, non écrit**.
- Mesure plus propre, **une année seulement** : salariés déclarés quatre trimestres en 2013
  (800 558) : 1,2 % sous 2/3 SMIG, 4,5 % de 2/3 à 1, **20,8 % de 1 à 1,5 SMIG**. Ces parts ne
  valent que pour les trois classes basses, à cause d'un **défaut de la source (PDF 36, vérifié
  à l'image)** : aucune ligne ne se somme à son total (ligne 1,5-2 : 101 697 pour 195 882
  imprimé ; ligne 2-2,5 : 207 150 pour 113 066), alors que les totaux de colonne et le total
  général bouclent. Les cellules par nombre de trimestres et la colonne « total » viennent de
  deux classements différents. Les trois classes basses ont des salaires moyens cohérents avec
  leurs bornes ; la ligne 2-2,5 SMIG ne l'est pas (567 D par mois pour une classe de 604 à 755 D).
- **2018, par trimestre civil (PDF 26)** : au premier trimestre (1 085 758 déclarés), 5,0 % sous
  2/3 SMIG, 4,5 % de 2/3 à 1, **21,9 % de 1 à 1,5 SMIG**. Le quatrième trimestre est à écarter :
  il porte les primes de fin d'année (masse de 4 261 MD contre 3 486 à 3 642 MD aux trois
  premiers ; 146 515 salariés à six SMIG et plus contre 100 398 à 107 335). Écart à retenir :
  9,5 % sous le SMIG au trimestre, 24,0 % dans la colonne annuelle de la même année — la
  différence est l'effet des années incomplètes. Non comparable à 2013 (définitions du § 2.2).
- **SMIG de référence** : non dit. Les salaires moyens par classe de 2013 (251 D par mois pour
  2/3-1 ; 364 D pour 1-1,5 ; 538 D pour 1,5-2) ne s'accordent qu'avec le régime de 48 heures
  (301,808 D), non avec celui de 40 heures (259,479 D) — déduit. La classe « 1 à 1,5 » confond
  le salarié au SMIG et celui payé 45 % de plus : la CNSS ne permet pas d'isoler « au SMIG ».
- Édition 2006 (2000-2006) : autre univers, 10,9 % sous 2/3 SMIG en 2000 contre 27,4 % dans
  l'édition 2010. Ne pas mêler.

### 4.2 INS, micro-entreprises (moins de six salariés) : la seule part publiée telle quelle

| Année | Sous le SMIG | Sous 0,5 SMIG | De 1 à 1,25 SMIG | Source |
|---|---|---|---|---|
| 2007 | 54,5 % (femmes 73,1 %, hommes 47,6 %) | — | « plus d'un quart » | rapport 2007, p. 10 du PDF |
| 2012 | 49,9 % (femmes 76,7 %, hommes 37,7 %) | 10,3 % | 18,4 % | rapport 2012, p. 11, 18 (tableau 8), 34, 38-40 (tableaux 2.7.1 à 2.7.3) |
| 2016 | 32,3 % | 6,8 % | 20,6 % | rapport 2016, p. 10, 17 (tableau 8) |

Détail par branche dans les tableaux 8 (industries, textile, construction, commerce, services).
Salaire déclaré par l'entreprise enquêtée ; la durée du travail n'est pas contrôlée dans ces
passages (à vérifier dans les chapitres de méthode avant d'écrire « payés sous le SMIG »).

### 4.3 CRES-BIT, avril 2011 : distribution individuelle, une année

La source imprime des quantiles de salaire **net** (premier décile 277 D, premier quartile
332 D, § 2.5) et ne calcule aucune part au SMIG. Le SMIG de 48 heures alors en vigueur,
272,480 D, est un montant brut : les deux ne se comparent pas sans le taux de cotisation salariale
de 2011, à prendre au volume des cotisations. Aucune part n'en est tirée ici. Famille à part :
enquête ponctuelle du CRES avec le BIT, ni budgétaire ni série de producteur.

### 4.4 Ce qui n'a pas été trouvé

Ni les annuaires de l'INS, ni l'enquête emploi ne donnent de part au SMIG ; les fiches des deux
documents du ministère des Affaires sociales présents au dépôt (annuaire social 2012, profil
2023) ne mentionnent aucun salaire (fiches lues, pas les documents). Une
recherche web sur la part des salariés au SMIG ne rend que des pages sur les montants. Deux
voies seulement : ne pas écrire « n'existe pas » sur cette base ; restent à sonder les rapports
de l'ITCEQ, l'ONEQ, les rapports de négociation du ministère et les publications de l'UGTT.

## 5. Lacunes et plan de collecte, par coût

### 5.1 Lecture d'un fichier déjà téléchargé (couche texte)

1. Pyramide en SMIG **2011-2018** : annuaire 2018, PDF 27 (2005-2018), contrôle par l'annuaire
   2013, PDF 37. Un script sur le modèle de `scripts/extract_cnss_pyramide_2010.py`.
2. Pyramides **selon les trimestres déclarés** : annuaire 2013 PDF 36 (2013), 2016 PDF 36
   (2016, arabe), 2018 PDF 25-26 (2018) ; chercher les mêmes pages dans les annuaires 2010 et
   2017. Consigner la définition des colonnes par édition.
3. Pyramide **en dinars** (paliers de 20 D) : annuaire 2013 PDF 34 (2000-2013), 2018 PDF 24 ;
   permet de recalculer la part sous un SMIG choisi, au lieu des classes de la CNSS.
4. Salaire annuel moyen **par branche et par bureau régional** : annuaire 2018 PDF 20-23,
   éditions 2013 et 2016 aux pages voisines.
5. INS, enquêtes Emploi et salaires 2012, 2014, 2022 : tableaux du salaire de base moyen par
   section et catégorie, en dinars et en % du SMIG ; quartiles à l'image.
6. Recherche des notes de méthode des annuaires (SMIG de référence, calcul du salaire mensuel) :
   non trouvées dans les 60 premières pages de l'édition 2013 ; à chercher dans les pages de
   garde et le glossaire des éditions 2010 et 2018.

### 5.2 Téléchargement ciblé (adresses vérifiées le 8 octobre 2026, réponse 200)

| Document | Adresse | Taille | SHA-256 de la copie de travail |
|---|---|---|---|
| INS, *Résultats de l'enquête auprès des micro-entreprises en 2007* (124 p.) | <https://www.ins.tn/sites/default/files/publication/pdf/micro_entreprise%202007.pdf> | 4,0 Mo | `47b6cd65cd72c237d452f3575f1e20c136541031d1fd875cea51bfd8a21d342f` |
| INS, *Enquête sur les micro-entreprises en 2012* (125 p.) | <https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/micro_entreprises%202012.pdf> | 6,6 Mo | `b057f60d9f346c73592727d557ab4f13567a3d0eecadf7db246a5d749eea1315` |
| INS, *Le secteur des micro-entreprises en Tunisie 2016* (175 p.) | <https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/micro-entreprises%202016.pdf> | 3,4 Mo | `5017c97dcad99652c2a6dac2df7e3fdc69e12ee09808ffd7bdb600c73516ffe3` |
| CRES et BIT, *Enquête sur la structure des salaires, Tunisie 2011*, rapport final, octobre 2012 (58 p.) | <http://www.cres.tn/uploads/tx_wdbiblio/Enquete_structure_salaire.pdf> | 3,8 Mo | `cda0225c57331b60e6ee8d3752f8c270e8a43ee024c9034a4e35652c6c25ceab` |

Copies rangées le 8 octobre 2026 dans `tunisia-data`, hors git :
`data/raw/ins-publications/micro-entreprises/`
(`ins_micro_2007.pdf`, `ins_micro_2012.pdf`, `ins_micro_2016.pdf`, `cres_structure_salaires.pdf`) ;
leur ligne de catalogue dans `sources/` reste à écrire.
Tous ont une couche texte. Pages de publication de l'INS (version anglaise, réponse 200) :
<https://www.ins.tn/en/publication/micro-companies-survey-2012>,
<https://www.ins.tn/en/publication/micro-companies-survey-2016> ; les pages françaises
correspondantes répondaient 500 le 8 octobre 2026.

### 5.3 Océrisation ou lecture à l'image

- Annuaire CNSS 2006 (scan) : lignes 2000 et 2001 du tableau salarial masquées par le pli (huit
  cellules, `sources/scan/cnss-annuaire-2006-valeurs-a-relire.csv`) ; pyramide en dinars PDF 20 ;
  éventuels tableaux par trimestres déclarés.
- Rapports de la BCT 1976-1998 : la section « Salaires » ne donne plus les salaires déclarés
  après 1975 (`docs/croissances-revenus-prix.md`) ; le salaire moyen sectoriel avant 1998 n'a pas
  été cherché rapport par rapport.
- Annuaires du BIT (966 à 1 166 pages) : lignes « Tunisie » des tableaux de salaires.

### 5.4 Publié nulle part à ce jour (constat provisoire)

- **Salaire moyen déclaré et pyramides après 2018** : aucun annuaire de la CNSS postérieur à
  2018 trouvé (recherches consignées dans `sources/cnss-annuaires.md` : archives du web, site de
  la caisse, CRES, ministère, data.gov.tn) ; les planches « La CNSS en chiffres » 2019-2020 ne
  portent pas la masse salariale.
- **Niveau du salaire sous-jacent au taux de l'INS** : jamais publié.
- **Annuaires de la CNSS antérieurs à 2006** (pyramides avant 2000) : aucune édition localisée.
- **Micro-entreprises 1997, 2002 (rapports) et 2022** : non trouvés (une seule voie essayée).
- **Part des salariés au SMIG sur l'ensemble du privé, en série** : non publiée ; ne s'obtient
  que par recalcul sur les pyramides.

## 6. Proposition de vue d'évolution (matière pour l'architecte et le rédacteur)

**Figure A — niveaux, dinars courants par mois, 1970-2018 (segments, pas de raccord).**
Salaire annuel moyen déclaré ÷ 12 : quatre segments (1970-1980 ; 1981-1987 ; 1988-1999 et
2002-2006, édition 2006 ; 2000-2018, édition 2018), face au SMIG 48 h en moyenne annuelle.
Ruptures annotées : 1981 (ICP dans le SMIG, hors assiette), 1988 (ICP et « MIT » dans
l'assiette), 2000-2006 (deux millésimes, les deux tracés), 2003 (taxis et louages), 2018 (fin).
Points isolés, marqués autrement : salariés déclarés quatre trimestres (2013), effectif
trimestriel moyen (2018).

**Figure B — rapport au SMIG, 1970-2018**, mêmes segments. Points de l'INS en surimpression,
famille distinguée : entreprises de six salariés et plus (2012, 2014, 2022, salaire de base des
permanents), micro-entreprises (2002, 2007, 2012, 2016).

**Figure C — indices base 100 en 2001, 2001-2025** : taux chaîné de l'INS (panel de permanents),
SMIG 48 h, prix à la consommation. Seule vue qui dépasse 2018 ; titre et note disent qu'il
s'agit d'une évolution à composition constante, pas d'un niveau.

**Figure D — bas de la distribution** : pyramide de la CNSS en trois bandes (< 1 SMIG, 1-1,5,
> 1,5), 2000-2018, avec la note sur les déclarations partielles ; à côté, non superposée, la part
sous le SMIG dans les micro-entreprises (2007, 2012, 2016).

**Tableau court de repères** (une ligne par année repère : 1970, 1980, 1988, 2000, 2010, 2018) :
SMIG 48 h mensuel moyen ; salaire moyen déclaré mensuel ; rapport ; part des déclarés sous
1,5 SMIG (2000 et après). Second tableau, titré comme enquêtes : INS 2012, 2014, 2022 et
micro-entreprises 2002-2016.

Hors figures : rapports extérieurs (Banque mondiale 1995 et 2004, FMI 1997) et BCT 1999-2005,
qui ne se superposent pas aux séries de la CNSS sans instruction de leur champ.

À corriger par ailleurs (hors de cette note) : `docs/croissances-revenus-prix.md` (« Ce qui
manque encore », 1976-1983) et `docs/notes/marche-travail-smig-smag.md` § 6-7.

## 7. Recherches infructueuses

`uv run python scripts/recherches.py lister` : aucune fiche ne porte sur les salaires effectifs
ou le SMIG. Aucune fiche proposée : le registre porte sur des textes du *Journal officiel* ; les
manques d'ici sont des publications statistiques, consignées au § 5.4 avec les voies essayées.
Un texte reste à chercher, sans qu'aucune recherche ait été lancée ici (donc sans fiche) : celui
qui, vers 1988, fait entrer l'indemnité complémentaire provisoire dans l'assiette des cotisations
— TODO documentaliste, à ouvrir en fiche `r-…` à la première passe.

## Références candidates (bibliographe)

Clés existantes à vérifier dans `precis/fr/marche_travail/references.json` : `bct-ra`,
`ins-annuaire`. À créer (clés suggérées) :

- `cnss-annuaire-2006`, `cnss-annuaire-2010`, `cnss-annuaire-2013`, `cnss-annuaire-2018` — CNSS,
  *Annuaire statistique*, type `report` ; pas d'URL d'origine établie pour 2006 et 2018.
- `ins-bms` — INS, *Bulletin mensuel de la statistique*, tableau 2.2 ; <https://www.ins.tn/publication>.
- `ins-salaires-prive-guide-2026` — INS, *Guide méthodologique pour le calcul du taux d'évolution
  trimestriel des salaires. Secteur privé non agricole*, 2026 (adresse dans la fiche du dépôt).
- `ins-ees-2012`, `ins-ees-2014`, `ins-ees-2022` — INS, *Enquête Emploi et Salaires auprès des
  Entreprises en 2012 / 2014 / 2022* (PDF créés en 2015, 2016, 2024) ; adresses dans
  `sources/ins-enquete-emploi-urls.csv`.
- `ins-micro-entreprises-2007`, `-2012`, `-2016` — INS, rapports de l'enquête sur les
  micro-entreprises (adresses au § 5.2 ; date de mise en ligne affichée : 29/12/2014 pour 2012,
  18/09/2018 pour 2016).
- `cres-bit-2012-structure-salaires` — CRES et BIT, *Enquête sur la structure des salaires,
  Tunisie 2011. Rapport final*, octobre 2012 (adresse au § 5.2).
- Études extérieures, non instruites, pour mémoire : Banque mondiale 13993-TUN (1995) et
  25456-TUN (2004), FMI 97/57 (déjà au dépôt) ; Fondation Friedrich-Ebert, *Étude de l'évolution
  des salaires réels en Tunisie avant et après la révolution*
  (<https://library.fes.de/pdf-files/bueros/tunesien/14391.pdf>, redirigée vers la notice
  `collections.fes.de`, réponse 200, non lue) ; ITCEQ, note n° 39 (août 2016), « Mesure de la
  taxation du travail salarié en Tunisie » : adresse connue en 404, à retrouver.

## Notions à glossaire (terminologue)

- **salaire déclaré** (à la CNSS) / **masse salariale déclarée** — الأجور المصرّح بها (**provisoire**, non relevé dans un annuaire
  arabe) ; source : annuaires de la CNSS.
- **salaire annuel moyen déclaré** — masse ÷ salariés déclarés ; à distinguer du salaire moyen.
- **salarié déclaré** / **non-assujetti** — annuaires de la CNSS.
- **salarié permanent** — deux sens à ne pas confondre : panel de l'INS (cinq trimestres
  déclarés, guide de 2026) ; « permanent » par opposition à « occasionnel » dans l'enquête Emploi
  et salaires (définition déclarative, rapport 2012, p. 5).
- **salaire de base** (hors primes et heures supplémentaires) — enquête Emploi et salaires.
- **pyramide des salaires** / **palier de salaire** — annuaires de la CNSS.
- **micro-entreprise** (moins de six salariés) et **entreprise « structurée »** (six salariés et
  plus) — INS.
- **régime des salariés non agricoles (RSNA)** — vérifier s'il est déjà au glossaire.
- **indemnité complémentaire provisoire (ICP)** — composante du SMIG depuis 1981, hors assiette
  jusqu'en 1987 ; vérifier l'entrée existante (« المنحة التكميلية الوقتية », provisoire).
- Termes arabes à relever dans les annuaires arabes de la CNSS (2010, 2016, 2017), non relevés ici.
