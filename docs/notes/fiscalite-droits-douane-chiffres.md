# Note documentaire : les droits de douane en chiffres

Documentaliste (chiffres), 23 octobre 2026. Matière du chapitre « Droits de douane » du livre
Fiscalité. Un autre documentaliste tient l'histoire et les textes
(`docs/notes/fiscalite-droits-douane-documentation.md`). Aucun `.qmd`, ni `references.json`, ni
`recherches.yml`, ni backlog n'est modifié : ce qui les concerne est proposé ici (§ 9 à § 12).

Fichiers joints :

- `docs/notes/fiscalite-droits-douane-series.csv` : 665 lignes, une valeur et une année par ligne (point décimal), avec
  famille, nature, année, article, libellé imprimé, valeur, unité, clé, document, page, édition,
  mode de lecture, remarque.
- `docs/notes/fiscalite-droits-douane-ratios-1986-2025.csv` : table annuelle proposée pour
  `tunisia-data/data/processed/precis/` (non écrite là-bas) : rendement, parts, PIB avec sa base,
  importations, taux de perception implicite, prévisions du tableau A, ventilation de la Cour des
  comptes.

Familles (conventions, § 3) : **budgétaire** (lois de finances, classeur du ministère, rapports
sur les dépenses fiscales ; la Cour des comptes et la BCT comme relais) ; **rapports extérieurs**
(GATT, OMC, FMI, Banque mondiale, WDI) ; **évaluations économiques** (études d'auteurs ; ici
Ayadi et al. 2013 ; le reste renvoyé à la fiche de l'économiste). Les importations sont une **statistique publique**
(INS, BCT), employée seulement comme dénominateur.

Mode de lecture : « fichier » (classeur ou JSON lu par script), « texte » (couche texte),
« image » (page lue à l'écran). Pages imprimées, sauf mention.

---

## 0. Ce qu'il faut savoir avant de lire les séries

1. **La rubrique « Droits de Douanes » du ministère comprend les redevances.** Dans le classeur
   des recettes fiscales, elle égale, pour chaque prévision contrôlée, la somme des trois
   articles du tableau A : 21-01 « droits de douane à l'importation », 21-02 « redevances sur
   prestations douanières à l'importation », 21-03 « redevances … à l'exportation » (2015 :
   685 + 150 + 9 = 844 ; 2017 : 519 + 177 + 4 = 700 ; 2018 : 870 + 211 + 8 = 1 089 ; 2019 :
   1 051 + 256 + 31 = 1 338) ; depuis 2020, 17-01 + 17-02 (2020 : 1 200 + 321 = 1 521). Les
   redevances font de 11 % (prévision 2001) à 26 % (prévision 2017) de la rubrique, et 17 à 22 %
   des réalisations 2018-2024 (Cour des comptes). Toute « part des droits de douane » ou tout
   « taux implicite » calculé sur cette rubrique inclut donc la redevance, qui est assise sur
   l'ensemble des droits et taxes perçus à l'importation (TVA et droit de consommation compris :
   3 % en 2016 selon l'OMC, 2 % en 1995 selon le FMI).
2. **Les autres séries ne mesurent pas toutes la même chose.** Le FMI de 1996 donne pour
   1991-1995 des « import duties » inférieures d'environ 30 MD à la rubrique du ministère
   (redevances vraisemblablement exclues, non établi). Les GFS du FMI reprises par les WDI
   (« customs and other import duties ») couvrent davantage : 587,4 MD en 1986 contre 277,8 MD.
   Le tableau IV.1 du GATT (1994, p. 56) est incohérent avec lui-même : sa ligne « import duties
   as a share of total imports » (12,4 à 11,3 % en 1988-1993) coïncide à 0,4 point près avec le
   ratio calculé ici sur la rubrique du ministère (§ 5), alors que sa ligne « import duties as a
   share of total tax revenue » (31,6 à 35,5 % en 1987-1992) ne peut pas reposer sur le même
   numérateur rapporté aux recettes fiscales (21 à 24 % pour la rubrique) ; non résolu. Pour la
   notion large, le GATT écrit (§ 19, p. 57) que les « customs payments, including DCP » font
   « some 48 per cent of total fiscal receipts in 1993 » ; le « régime douanier » du ministère fait
   46,1 % la même année (1 418,8 / 3 080,5) : rapprochement, non identité.
3. **Aucune série de PIB n'est chaînée.** La part du PIB se donne par segment de base
   (`docs/notes/annexe-pib.md`, § 3 ; ruptures 1997, 2002, 2005, 2010, 2025).
4. **Le recul de la part des douanes commence en 1996**, et son attribution à l'accord avec l'UE
   n'est faite, dans les sources lues, que par l'OMC et toujours avec un second facteur, les
   exonérations (§ 7.1).

---

## 1. Sources lues

| Source | Famille | Ce qu'on en tire | Lecture | Copie locale (tunisia-data) |
|---|---|---|---|---|
| Ministère des Finances, `Série Recettes_fiscales_fr.xls` (classeur du 30 juin 2026) | budgétaire | réalisations 1986-2025 de la rubrique « Droits de Douanes » (ligne 27), du « Régime Douanier » (ligne 48), du total ; colonnes LF et LFC 2013-2026 | fichier | `data/raw/minfinances/recettes_fiscales.xls` (fiche `sources/minfinances-recettes-fiscales.md`) |
| Ministère des Finances, indicateurs des finances publiques LF 2026 | budgétaire | PIB déduit (déficit ÷ déficit en % du PIB), par la table `irpp_ratios_1986_2025.csv` | fichier | `data/raw/minfinances/indicateurs_fp_LF2026.xls` |
| Ministère des Finances, répartition économique des dépenses | budgétaire | dépenses de l'État hors service de la dette 1986-2025, par `denominateurs_depenses_etat_pib_1984_2025.csv` | fichier | `data/raw/minfinances/repartition_depenses.xls` |
| Lois de finances 2001-2026, tableau A | budgétaire | prévisions article par article, total de la première partie | image 2001-2010, 2019-2026 ; texte 2011-2018 | corpus JORT (`PDFs-legislation-tunisie/PDFs/JORT/`) |
| Cour des comptes, rapports sur les projets de lois de règlement 2019-2022, rapports sur la clôture 2023 et 2024 | budgétaire (relais) | réalisations 2018-2024 par article ; motifs des variations dans les mots de la Cour | texte | `data/raw/cour-des-comptes/18/` |
| Rapports sur les dépenses fiscales annexés aux PLF 2021 à 2025 | budgétaire (évaluation du ministère) | coût des dispositifs « droits de douane » 2017-2023, par millésime | texte, fichier | `data/raw/gbo/` |
| BCT, rapports annuels 1975 et 1998 | budgétaire (relais) ; statistique publique | droits de douane à l'importation 1972-1975 ; importations CAF 1988-1998 | image (1975), texte (1998) | `data/raw/bct-archives/109/` |
| INS, *Annuaire statistique*, tableau 14.2 (22 éditions) | statistique publique | importations 1998-2023, ensemble, régime général, régime off shore | fichier | série `ins-commerce-exterieur-par-regime` |
| GATT, *Trade Policy Review: Tunisia*, C/RM/S/47, 24 mai 1994 | rapport extérieur | taux moyens 1987-1989 et 1994, droits / importations 1987-1993, fourchette des taux | texte | **téléchargé** : `data/raw/droits-douane/omc/gatt_1994_tpr_c-rm-s-47_en.pdf` |
| OMC, *Examen des politiques commerciales : Tunisie*, WT/TPR/S/152, 2005 | rapport extérieur | moyennes 1994, 2004, 2005, nombre de taux, taux maximum, préférences UE, part des recettes | texte (.doc publiés par l'OMC) | **téléchargé** : `data/raw/droits-douane/omc/wto_2005_tpr_s152-{0..4}_fr.doc` |
| OMC, idem, WT/TPR/S/341, 8 juin 2016 | rapport extérieur | moyenne simple et taux maximum par année 2005-2016 (graphique 3.2), préférences UE, redevance | texte, image | **téléchargé** : `wto_2016_tpr_s341_fr.pdf` |
| OMC, *Trade Policy Review: Tunisia*, WT/TPR/S/479/Rev.1, 14 octobre 2025 | rapport extérieur | moyenne 2025, nombre de taux, préférences, recettes 2018-2024 droits / redevance | texte | **téléchargé** : `wto_2025_tpr_s479r1_en.pdf` |
| FMI, *Recent Economic Developments*, n° 96/27, avril 1996 | rapport extérieur | taux maximum 1986-1988, structure 1994, import duties 1991-1995, explication du recul 1992-1995 | texte | déjà présent : `data/raw/banque-mondiale-rapports/imf_1996_027_red_tunisia.pdf` |
| FMI, *Selected Issues*, n° 97/57, juillet 1997, chapitre sur l'accord avec l'UE | rapport extérieur | taux 1986 et 1996, perception implicite 1996, **perte de recettes estimée** (méthode décrite) | texte | déjà présent : `imf_1997_057_red_tunisia.pdf` |
| FMI, n° 15/285 (2015) et n° 16/138 (2016) | rapport extérieur | rendement estimé de la réforme tarifaire de 2016 | texte | déjà présents |
| Banque mondiale, *Tunisie : vers le XXIe siècle*, rapport n° 14375-TUN, vol. II, 1995 | rapport extérieur | moyennes 1983-1995, fourchettes | texte | **téléchargé** : `data/raw/droits-douane/banque-mondiale/wb_1995_14375_vers_21e_siecle_annexes_fr.pdf` |
| Banque mondiale, *The Unfinished Revolution*, rapport n° 86179, 2014 | rapport extérieur | moyenne NPF 2002 et 2011, évasion tarifaire, commerce informel | texte | déjà présent : `wb_2014_86179_unfinished_revolution_en.pdf` |
| Banque mondiale, WDI (WITS/TRAINS ; GFS du FMI) | rapport extérieur | taux moyens appliqués et NPF, 1990-2016 ; part GFS 1972-2012 | fichier | **téléchargé** : `data/raw/droits-douane/wdi/*.json` |
| Accord d'association UE-Tunisie, JOCE L 97 du 30 mars 1998, art. 11 | texte (calendrier) | calendrier du démantèlement | texte | déjà téléchargé par l'autre documentaliste : `data/raw/accords-commerciaux/ue_tunisie_accord_association_1995_jocel97.pdf` |

Catalogue des fichiers téléchargés ce jour et des rapports déjà présents mais non catalogués :
`tunisia-data/sources/droits-douane-urls.csv` (adresse, date, taille, SHA-256). Le répertoire
`data/raw/droits-douane/` porte son propre `.gitignore` (`*`) pour rester hors de git sans
toucher au `.gitignore` racine, modifié en parallèle par un autre agent ; **une ligne
`data/raw/droits-douane/` est à ajouter au `.gitignore` racine** lors de la prochaine fusion.

---

## 2. Rendement : les réalisations (budgétaire)

### 2.1 Série du ministère, 1986-2025

Rubrique « Droits de Douanes » du classeur [@minfin-recettes-fiscales], millions de dinars
courants. Table complète dans le CSV des ratios.

| Année | Droits de douane | Recettes fiscales | Part (%) |
|---|---:|---:|---:|
| 1986 | 277,8 | 1 632,0 | 17,02 |
| 1989 | 458,0 | 1 946,0 | 23,54 (maximum) |
| 1990 | 495,6 | 2 169,2 | 22,85 |
| 1995 | 773,0 | 3 492,4 | 22,13 (niveau dépassé pour la première fois en 2014) |
| 1996 | 741,0 | 3 780,2 | 19,60 |
| 2000 | 641,6 | 5 678,4 | 11,30 |
| 2006 | 489,9 | 8 469,7 | 5,78 (niveau le plus bas depuis 1989) |
| 2011 | 561,2 | 13 629,9 | 4,12 |
| 2015 | 832,5 | 18 545,8 | 4,49 |
| 2016 | 639,7 | 18 702,0 | 3,42 (minimum en part) |
| 2017 | 741,9 | 21 186,5 | 3,50 |
| 2018 | 1 208,3 | 24 503,3 | 4,93 |
| 2025 | 2 278,9 | 44 749,8 | 5,09 |

Lecture : le niveau en dinars courants baisse de 1995 à 2006 (773 → 490 MD), puis remonte ; la
part dans les recettes fiscales passe de 22-24 % (1988-1995) à 3,4 % (2016) et remonte à 5 %
depuis 2018. Deux sauts d'une année à l'autre : 2015 → 2016 (− 23 %) et 2017 → 2018 (+ 63 %). Ce
sont des faits de série ; leur rattachement à des textes (réforme tarifaire de la LF 2016,
relèvements de la LF 2018) relève de la note textes et n'est pas fait ici.

**Contrôle sur une autre source.** Pour 1993-1995, le rapport annuel 1995 de la BCT imprime 697,0 ;
735,4 ; 773,0, valeurs du classeur (relais). Pour 2018-2024, la Cour des comptes donne 1 210,3 ;
1 286,8 ; 1 228,4 ; 1 420,0 ; 1 783,1 ; 1 849,0 ; 2 071,3, contre 1 208,3 ; 1 284,4 ; 1 228,4 ;
1 420,1 ; 1 784,2 ; 1 849,0 ; 2 071,3 au classeur : écarts de 2 MD en 2018-2019, nuls ensuite.

### 2.2 Ventilation droits / redevances : Cour des comptes, 2018-2024

[@cdc-loireg-2019, p. 55 ; @cdc-loireg-2020, p. 45 ; @cdc-loireg-2021, p. 54 ;
@cdc-loireg-2022, p. 44 ; @cdc-rapport-budget-2023, p. 38 ; rapport 2024, pp. 34-35], dinars
arrondis au millier de dinars ici.

| Année | Droits (21-01 / 17-01) | Redevance à l'importation | Redevance à l'exportation | Total | Part des redevances |
|---|---:|---:|---:|---:|---:|
| 2018 | 949,7 | 225,0 | 35,6 | 1 210,3 | 21,5 % |
| 2019 | 1 018,5 | 238,9 | 29,5 | 1 286,8 | 20,9 % |
| 2020 | 986,8 | 219,4 | 22,2 | 1 228,4 | 19,7 % |
| 2021 | 1 138,4 | 249,9 | 31,7 | 1 420,0 | 19,8 % |
| 2022 | 1 446,4 | 296,6 | 40,1 | 1 783,1 | 18,9 % |
| 2023 | 1 519,7 | 290,7 | 38,6 | 1 849,0 | 17,8 % |
| 2024 | 1 715,1 | 328,6 | 27,6 | 2 071,3 | 17,2 % |

L'OMC (2025, tableau 3.2, p. 38, « information provided by the authorities ») reprend les mêmes
montants arrondis (droits 951 … 1 715 ; redevance 222 … 328, celle-ci limitée à l'importation).
Pour 2015, l'OMC (2016, § 3.30, p. 50) donne 142,1 MD de redevance de prestations douanières.

**Motifs donnés par la Cour (ses mots, résumés ; contexte, non intention de la loi)** :
2020 — recul des importations (− 18,7 %) et des exportations (− 11,7 %) ; 2021 — hausse des
importations du régime général hors énergie (+ 22,8 %) ; 2022 — importations (+ 32,4 %) et
« مراجعة المعاليم الديوانية الموظفة على المنتجات الاستهلاكية التي لها مثيل مصنوع محليا وذلك
بالترفيع في نسبها » (décret-loi n° 2021-21, art. 57) ; 2023 — « ترشيد منح الإعفاء » sur les camions
des Tunisiens résidents à l'étranger, taxés à 10 % (décret-loi n° 2022-79, art. 70) ; 2024 —
mesures tarifaires exceptionnelles sur les produits d'origine turque et fruits secs (LF 2024,
art. 44 et 55) ; redevance à l'importation : minimum porté de 10 à 20 dinars (LF 2024, art. 66).

### 2.3 Avant 1986

Le rapport annuel 1975 de la BCT donne les « droits de douane à l'importation » de 1972 à 1975 :
13,6 ; 17,4 ; 23,2 ; 26,2, avec leur assiette (importations hors régimes suspensifs) 201,8 ;
247,5 ; 386,9 ; 449,2 [@bct-ra-1975, p. 107, lu à l'image]. L'en-tête imprime « en milliers de
dinars » ; l'ordre de grandeur (recettes fiscales 1975 : 275 126 milliers au tableau suivant)
indique des millions, et les GFS du FMI (WDI, `GC.TAX.IMPT.CN`) donnent 102,8 millions de dinars
de « customs and other import duties » pour 1975, à comparer aux 84,2 d'« impôts liés aux
importations » du tableau de la BCT : même ordre de grandeur, en millions. Le même rapport commente : « Les droits de douane, la taxe à la production
(régime importation) et la taxe de consommation (régime importation), impôts liés aux
importations, ont été sensiblement affectés par la politique d'encadrement du commerce extérieur
destinée à redresser la balance commerciale. » **Piste** : les rapports annuels 1959-1985 de la
BCT (`data/raw/bct-archives/109/`) portent vraisemblablement une ligne « droits de douane »
chaque année ; non relevés (couche texte de qualité variable ; RA 1985 : la recherche « Droits de
douane » ne rend rien et demande un examen à l'image).

### 2.4 « Régime douanier » : toutes les recettes perçues en douane

La ligne 48 du classeur (« Régime Douanier ») et la ligne 47 (« Régime Intérieur ») somment
exactement au total chaque année (contrôlé 1986-2026). Le régime douanier comprend vraisemblablement les droits de
douane, la TVA, le droit de consommation à l'importation et les autres prélèvements perçus à la
frontière : composition non détaillée par le classeur, contenu déduit du libellé. Il fait 31,7 % des recettes fiscales en
1986, 45,5 % en 1995, 27,3 % en 2005, 24,5 % en 2025 ; la rubrique « droits de douane » en
représente 53,7 % (1986), 48,6 % (1995), 23,4 % (2005), 13,0 % (2017), 20,8 % (2025). L'OMC
(2016, graphique 3.1, p. 45) écrit que les recettes fiscales au titre des importations
représentent « près d'un quart des recettes fiscales totales de l'État » en 2014.

---

## 3. Rendement : les prévisions du tableau A (budgétaire)

Lois de finances initiales [@lf-2001 … @lf-2026], tableau A. Millions de dinars courants.
Pages et éditions dans le CSV.

| LF | Droits à l'importation | Redevances (import + export) | Total | Réalisation (classeur) | Écart réal. / prév. |
|---|---:|---:|---:|---:|---:|
| 2001 | 557 | 68 | 625 | 655,2 | + 4,8 % |
| 2002 | 603 | 77 | 680 | 594,8 | − 12,5 % |
| 2003 | 564 | 71 | 635 | 553,6 | − 12,8 % |
| 2004 | 535 | 70 | 605 | 556,7 | − 8,0 % |
| 2005 | 506 | 69 | 575 | 505,9 | − 12,0 % |
| 2006 | 488 | 72 | 560 | 489,9 | − 12,5 % |
| 2007 | 344 | 71 | 415 | 514,3 | + 23,9 % |
| 2008 | 376 | 84 | 460 | 584,7 | + 27,1 % |
| 2009 | 384 | 86 | 470 | 520,2 | + 10,7 % |
| 2010 | 430 | 85 | 515 | 563,9 | + 9,5 % |
| 2011 | 406 | 100 | 506 | 561,2 | + 10,9 % |
| 2012 | 469 | 110 | 579 | 715,5 | + 23,6 % |
| 2013 | 604 | 146 | 750 | 728,9 | − 2,8 % |
| 2014 | 634 | 146 | 780 | 825,3 | + 5,8 % |
| 2015 | 685 | 159 | 844 | 832,5 | − 1,4 % |
| 2016 | 415 | 108 | 523 | 639,7 | + 22,3 % |
| 2017 | 519 | 181 | 700 | 741,9 | + 6,0 % |
| 2018 | 870 | 219 | 1 089 | 1 208,3 | + 11,0 % |
| 2019 | 1 051 | 287 | 1 338 | 1 284,4 | − 4,0 % |
| 2020 | 1 200 | 321 | 1 521 | 1 228,4 | − 19,2 % |
| 2021 | 1 032 | 271 | 1 303 | 1 420,1 | + 9,0 % |
| 2022 | 1 573 | 283 | 1 856 | 1 784,2 | − 3,9 % |
| 2023 | 1 684 | 376 | 2 060 | 1 849,0 | − 10,2 % |
| 2024 | 1 560 | 340 | 1 900 | 2 071,3 | + 9,0 % |
| 2025 | 1 745 | 366 | 2 111 | 2 278,9 | + 8,0 % |
| 2026 | 1 939 | 449 | 2 388 | — | — |

Remarques :

- **Nomenclature.** 2001 : articles 121-01 à 121-03 ; 2002-2019 : 21-01 à 21-03, titre 1
  « Droits de Douane » de la catégorie 2 « Impôts et Taxes Indirects Ordinaires » ; depuis 2020
  (loi organique du budget de 2019) : catégorie 4 « Impôt sur le commerce extérieur et les
  transactions » (« معاليم على التجارة الخارجية و المعاملات الدولية »), titre 7 « Droits et
  redevances douaniers », 17-01 « Droits de douane » et 17-02 « Redevance sur les prestations
  douanières » (les deux redevances fondues). La série se raccorde : 17-01 = 21-01 ; 17-02 =
  21-02 + 21-03 (même total que la rubrique du ministère).
- **Libellés fautifs.** En 2009 et 2013, l'article 21-02 est imprimé « Droits de Douane à
  l'exportation » ; en 2013 sa valeur (118) est celle que la LF 2014 imprime pour 21-02
  « redevances … à l'importation ». Lu comme une erreur de libellé, non comme un droit de sortie.
- **2022.** Le tableau A imprime 1 856 ; le classeur du ministère porte 2 056 en colonne « LF
  2022 » et 1 856 en « LFC 2022 », pour un même total général (35 091). Le tableau A fait foi ; la
  colonne du classeur est à signaler.
- **Colonnes sans millésime du classeur** (2013-2016) : l'ordre « prévision, puis réalisation de
  la même année » est établi par les tableaux A de 2014, 2015, 2016, 2017 et 2018 (780, 844, 523,
  700, 1 089). La première colonne « L.F.C » (730) est donc la LFC 2013 (la LFC 2012 imprime 475 +
  95 + 15 = 585 : `portail_ancien/lois_finances/2012_lfc_2012_ar.pdf`) ; la LFC 2013 n'est pas lue
  au JORT.
- **Dénominateur des parts de prévision.** Le « total de la première partie » comprend certaines
  années des lignes non fiscales (2015 : 790 MD d'excédents des fonds spéciaux ; 2019 : 26-06,
  1 417,8 ; 2020-2026 : 18-07, de 1 043 à 2 452 MD). Ces totaux sont dans le CSV ; une part de
  prévision ne se calcule qu'après les avoir retirés.
- **Avant 2001.** Pages du tableau A des LF 1970-1993 connues par
  `docs/notes/fiscalite-patrimoine-immobilier-series-tableau-A-ocr.csv` ; non lues pour les
  douanes. À lire à l'image en priorité : LF 1989, 1995, 1996, 1997 (avant et après l'accord).

---

## 4. Parts : recettes fiscales, PIB par segment, dépenses de l'État (budgétaire)

Numérateur : rubrique du ministère (droits + redevances). PIB : PIB déduit du classeur des
indicateurs du ministère (`pib_minfin_MDT` de `irpp_ratios_1986_2025.csv`), avec sa base telle
qu'établie dans `docs/notes/annexe-pib.md`, § 3. Pour 2023 et 2024, ce PIB (149 733,8 et
159 760,6) diffère de moins de 0,1 % de la dernière édition de l'INS (149 793,6 et 159 852,7) : le
CSV garde celui du ministère. Dépenses : dépenses de l'État hors service de la dette
(réalisations du classeur `repartition_depenses.xls`).

**Part du PIB, par segment (jamais chaînés)** :

| Segment | Base | Rétropolé | Valeurs (%) |
|---|---|---|---|
| 1986-1991 | base 1983 présumée (égale à la série 20 des Nations unies) | non précisé | 1986 3,88 ; 1987 4,34 ; 1988 4,60 ; 1989 4,78 ; 1990 4,58 ; 1991 4,74 |
| 1992-1996 | base 1983 | non précisé | 1992 4,82 ; 1993 4,75 ; 1994 4,65 ; 1995 4,53 ; 1996 3,89 |
| 1997-2001 | base 1997 | oui (rétropolée par l'INS) | 1997 3,07 ; 1998 2,88 ; 1999 2,52 ; 2000 2,18 ; 2001 2,06 |
| 2002-2004 | valeurs propres au ministère, non rattachées | — | 2002 1,85 ; 2003 1,60 ; 2004 1,48 |
| 2005-2009 | base 1997 | non | 2005 1,21 ; 2006 1,07 ; 2007 1,03 ; 2008 1,06 ; 2009 0,88 |
| 2010-2024 | base 2015 | oui pour 2010-2014 | 2010 0,85 ; 2011 0,83 ; 2012 0,97 ; 2013 0,92 ; 2014 0,97 ; 2015 0,93 ; 2016 0,67 ; 2017 0,73 ; 2018 1,07 ; 2019 1,04 ; 2020 1,03 ; 2021 1,08 ; 2022 1,28 ; 2023 1,23 ; 2024 1,30 |
| 2025 | valeur propre au ministère, non rattachée | — | 1,32 |

Rupture à dire : le passage 1996 → 1997 (3,89 → 3,07) mêle une baisse du numérateur (741 → 704 MD)
et le relèvement du PIB de 9,8 % du changement de base ; à numérateur égal, 1997 vaudrait environ
3,4 % en base 1983 (calcul indicatif, annexe PIB § 2.4 ; ne pas publier comme valeur). Le FMI
(1997, p. 12) écrit que la recette des droits de douane faisait « 4.3 percent of GDP » en 1995
(PIB de l'époque, base 1983) : même ordre que 4,53 % ici.

**Part des recettes fiscales et des dépenses (sans question de base)** :

| Année | Part des recettes fiscales | Part des dépenses hors dette |
|---|---:|---:|
| 1986 | 17,02 | 11,60 |
| 1990 | 22,85 | 15,58 |
| 1992 | 23,51 | 18,06 (maximum) |
| 1995 | 22,13 | 16,86 |
| 2000 | 11,30 | 9,67 |
| 2005 | 6,40 | 5,50 |
| 2010 | 4,44 | 3,95 |
| 2016 | 3,42 | 2,65 (minimum) |
| 2018 | 4,93 | 4,05 |
| 2025 | 5,09 | 4,34 |

La phrase de `precis/fr/fiscalite/index.qmd` (« de 22,9 % des recettes fiscales en 1990 à 5,1 % en
2025 ») est conforme à la série.

---

## 5. Taux de perception implicite : droits / importations

Numérateur : rubrique du ministère (budgétaire). Dénominateurs (statistique publique) :
importations CAF de la BCT pour 1988-1997 (rapport annuel 1998, tableau « Évolution du commerce
extérieur de la Tunisie 1988-1998 », p. 129, arrondies au million ; 1998 : 9 489 contre 9 489,5 à
l'INS), importations de l'INS pour 1998-2023 (ensemble et régime général ; l'annuaire ne définit
pas les régimes, et le libellé arabe du régime off shore est « نظام غير مقيم »). Le ratio est un
calcul de la note, non une valeur publiée. Il inclut les redevances au numérateur (§ 0).

| Année | Droits / importations totales | Droits / importations du régime général |
|---|---:|---:|
| 1988 | 12,59 | — |
| 1990 | 10,27 | — |
| 1995 | 10,36 | — |
| 1996 | 9,88 | — |
| 1997 | 8,01 | — |
| 1998 | 7,52 | 11,40 |
| 2000 | 5,47 | 7,78 |
| 2005 | 2,93 | 4,42 |
| 2008 | 1,93 | 2,70 |
| 2011 | 1,67 | 2,47 |
| 2016 | 1,53 | 2,26 |
| 2017 | 1,48 | 2,19 (minimum) |
| 2018 | 2,01 | 3,00 |
| 2020 | 2,38 | 3,56 |
| 2023 | 2,34 | 3,46 |

Rapports extérieurs, à ne pas mêler (même grandeur, autres sources) : GATT (1994, tableau IV.1,
p. 56) « import duties as a share of total imports (c.i.f.) » 13,5 (1987), 12,4, 10,8, 10,2,
11,5, 11,9, 11,3 (1993) — à 0,4 point près le ratio calculé ici pour 1988-1993 (12,59 ; 11,00 ;
10,27 ; 11,90 ; 11,61 ; 11,29), ce qui recoupe à la fois la rubrique du ministère et les
importations de la BCT ; FMI (1997, p. 9) 10,3 % en 1996 (« reflecting the importance of the
off-shore sector, which took in 32 percent of total imports, and exemptions »). Le GATT écrit
(p. 57) que l'écart entre le taux moyen pondéré (22 % en 1989) et ce ratio (11 %) « suggests the
existence of substantial duty-free imports entering under special regimes, such as temporary
admission and the free zone regime ».

Réserves : les importations INS de 2003 et avant ne sont imprimées dans aucune édition postérieure
à la révision du régime off shore de 2004-2005 (catalogue `ins-commerce-exterieur-par-regime`) ;
2023 n'est imprimé qu'une fois. 2024-2025 : importations non relevées (lacune).

---

## 6. Taux, barèmes et nombre de taux (rapports extérieurs)

Toutes ces valeurs viennent de rapports extérieurs, chacune avec sa définition ; elles ne
s'additionnent ni ne se chaînent d'une source à l'autre.

### 6.1 Taux maximum et fourchette

| Date | Fourchette ou maximum | Source |
|---|---|---|
| « early 1980s » / « à la veille de l'ajustement structurel » / 1986 | 5 à 236 %, moyenne supérieure à 40 % | GATT 1994, p. 55 ; Banque mondiale 1995, annexe 2, p. 5 ; FMI 1997, p. 9 (« Custom duties ranged from 5 percent to 236 percent, with the average rate exceeding 40 percent », pour 1986) ; FMI 1996, p. 29 (« from 236 percent in 1986 to 43 percent in 1988 ») et p. 53 (« 236 percent in the early 1980s ») |
| 1988 | 17-43 % (GATT) ; 10-43 % (FMI 1997, phase 1986-88) | GATT 1994, p. 55 ; FMI 1997, p. 9 |
| 1990 | 15-43 % | Banque mondiale 1995, annexe 2, p. 5 |
| 1994 | 26 taux, 0-43 % (calcul OMC 2005 sur les données de 1994) ; 0-73 % avec les DCP (FMI 1996, p. 53) | OMC 2005, § III.22 |
| oct. 1995 | 10-43 % (droit de douane) ; DCP 10-30 % en sus | FMI 1996, « Summary of the Tax System as of October 15, 1995 », p. 16 de l'annexe (pagination à vérifier à l'image) |
| 1996 | 0-53 % | FMI 1997, p. 9 |
| 2004 | maximum 200 % | OMC 2005, § III.22 |
| 2005 | 15 taux, 0-150 %, taux modal 43 % | OMC 2005, § III.22 |
| 2005-2016 | maximum 150 (2005), 150 (2006), 73 (2007), 60 (2008), 36 (2009-2016) | OMC 2016, graphique 3.2, p. 46 |
| 2016 | 6 taux, 0-36 % (§ 3.24, p. 46) ; « seulement trois taux en 2016 : zéro, 20 % et 36 % » (résumé, § 9, p. 9) | OMC 2016 ; l'OMC 2025 (note 39) énumère six taux en 2016 : 0, 15, 20, 27, 34, 36 % |
| 2025 | 11 taux, 0 à 50 % (0, 7, 10, 15, 17, 20, 27, 30, 36, 43, 50 %) | OMC 2025, § 3.26, p. 39 |

Le « 200-250 % » évoqué dans le ticket se rattache à deux choses distinctes : le maximum de
236 % du début des années 1980 (tarif appliqué), et les taux **consolidés** agricoles à l'OMC,
de 25 à 200 % (FMI 1996, p. 53 ; OMC 2005, § III.17 : 17 à 200 %, moyenne 117,5 % ; OMC 2016,
§ 3.32 : moyenne 120,8 %), plus le maximum appliqué de 200 % en 2004.

### 6.2 Taux moyens

| Année | Valeur | Définition | Source |
|---|---:|---|---|
| 1983-1986 | « > 40 » | moyenne des droits | Banque mondiale 1995, annexe 2, p. 5 |
| 1987 ; 1988 ; 1989 | 32,5 ; 30,2 ; 28,5 | moyenne simple | GATT 1994, tableau IV.1, p. 56 |
| 1987 ; 1988 ; 1989 | 24,9 ; 25,0 ; 22,2 | moyenne pondérée par les importations | idem |
| 1987-1990 | 24 | moyenne | Banque mondiale 1995, annexe 2, p. 5 |
| 1994 | 33,2 (DCP compris, estimation du Secrétariat) ; 30,7 (calcul OMC 2005, NPF) | moyenne simple | GATT 1994 ; OMC 2005, tableau III.1 |
| mi-1994 | 40 (agricoles) ; 33 (non agricoles) | moyenne | FMI 1996, p. 53 |
| 1995 | ≈ 35 (DCP compris) | moyenne | Banque mondiale 1995, annexe 2, p. 5 |
| 1996 | 32 | moyenne pondérée | FMI 1997, p. 9 |
| 2002 ; 2011 | 30 ; 16 | moyenne simple NPF, SH6 | Banque mondiale 2014, encadré 1.5, p. 56 |
| 2004 ; 2005 | 32,7 ; 31,7 | moyenne simple NPF appliquée, hors taux sous contingent | OMC 2005, tableau III.1 |
| 2005 → 2016 | 31,3 ; 44,7 ; 26,1 ; 24,7 ; 22,9 ; 18,8 ; 18,7 ; 18,2 ; 16,4 ; (2014 non notifié) ; 18,2 ; 14,1 | moyenne simple NPF, lignes à 9 chiffres | OMC 2016, graphique 3.2, p. 46 (2005-2006 tels qu'imprimés) |
| 2025 | 23,8 (11 chiffres) ; 22,3 (9 chiffres, comparable à 2016) | moyenne simple NPF | OMC 2025, tableau 3.3, pp. 39-40 |
| 1990-2016 | voir CSV | moyennes simples et pondérées, appliquées et NPF | WDI (WITS/TRAINS), indicateurs TM.TAX.MRCH.* |

**WDI, réserve.** Les taux « appliqués » des WDI retiennent le taux préférentiel quand il est
connu, sinon le taux NPF : la série saute en 2005 (simple 13,28 contre 25,92 en 2004 et 22,99 en
2006) et en 2013 (6,69, puis 10,21 en 2016). Les séries NPF sont plus régulières (simple : 28,94
en 1990, 33,91 en 2002, 15,53 en 2012, 11,56 en 2016) mais diffèrent des moyennes de l'OMC pour
les mêmes années (2016 : 11,56 contre 14,1 ; nomenclatures et niveaux d'agrégation différents).
Aucune valeur WDI après 2016.

### 6.3 Préférences UE (taux réalisés)

| Année | Importations d'origine UE | Source |
|---|---|---|
| 2005 | moyenne simple du tarif préférentiel UE 18,0 % (NPF 31,7) ; produits non agricoles 6,3 % (NPF 23 %) ; près de la moitié des lignes non agricoles en franchise en 2004, 99,1 % prévus en 2008 | OMC 2005, tableau III.2, § III.28 |
| 2016 | non agricoles : franchise sauf 122 lignes, moyenne 0,3 % (NPF 9,6 %) ; agricoles : 32,1 % (NPF 32,1 %) | OMC 2016, tableau 3.7, p. 55 |
| 2025 | ensemble 7,6 % ; non agricoles 1,7 % (NPF 21,0 %) ; agricoles 30,6 % (NPF 34,5 %) | OMC 2025, tableau 3.4, p. 42 |

---

## 7. Le démantèlement tarifaire avec l'UE

### 7.1 Calendrier (texte) et ce qu'en disent les rapports

Accord d'association, art. 11 (JOCE L 97 du 30 mars 1998) : droits supprimés dès l'entrée en
vigueur sauf annexes 3 à 6 ; annexe 3 : 85 % du droit de base à l'entrée en vigueur, puis 70, 55,
40, 25 %, suppression à cinq ans ; annexe 4 : 92 % puis − 8 points par an jusqu'à 4 % à onze ans,
suppression à douze ans ; annexe 5 : 88 % à quatre ans, − 11 points par an, suppression à douze
ans ; annexe 6 (art. 12) : hors démantèlement, régime réexaminé à quatre ans. Droit de base : le
droit appliqué à l'égard de la Communauté au 1er janvier 1995, remplacé par toute réduction erga
omnes postérieure (art. 11, § 5-6). **La date de départ effective du calendrier relève de la note
textes** : l'OMC (2005, § III.27) écrit « démantèlement … graduellement jusqu'en 2007, avec une
entrée en franchise totale dès 2008 » et le FMI (1997) chiffre des pertes dès 1996, ce qui suppose
une application anticipée à 1996 ; non établi ici.

Attribution du recul des recettes (rapports extérieurs, mots de la source) :

- OMC 2005, § III.15 : les droits de douane font 4,9 % des recettes budgétaires totales en 2003,
  6,5 % en 2000, 13,2 % en 1994 ; « Cette baisse résulte de plusieurs facteurs, notamment les
  réductions tarifaires progressives portant sur les produits non-agricoles dans le cadre de
  l'Accord avec l'Union européenne, et l'augmentation des exemptions de droits de douanes
  accordées aux industries locales pour l'importation de leurs intrants. »
- OMC 2016, § 3.22, p. 45 : même phrase pour 2005-2015 (6,4 % → 4,3 % des recettes totales de
  l'État).
- FMI 1996, p. 35 : le recul de 1992-1995 (en % du PIB) « can be attributed to the granting of
  exemptions or rate reductions, including those under the investment code, and the increased
  share of imports by the offshore sector, which remained exempt from taxes on imports ».

Proposition pour `index.qmd` (TODO existant, l. 58) : remplacer « l'effet du démantèlement
tarifaire engagé avec l'accord d'association de 1995 » par l'attribution de l'OMC, citée comme
telle, avec ses deux facteurs.

### 7.2 Pertes de recettes estimées

Une seule estimation avec méthode décrite a été lue.

- **FMI, 1997** [@fmi-1997-selected-issues, pp. 12-13]. Méthode : services du FMI ; « simplifying
  assumption of no change in the geographical origin and level of imports and of GDP from their
  1995 magnitudes » ; hors perte liée à la suppression des droits complémentaires provisoires au
  1er janvier 1998 (0,2 % du PIB en 1997). Résultat : perte « from 0.2 percent of GDP in 1996 to
  0.5 percent in 1997 and further to 2.4 percent of GDP by 2008 » ; « nearly half of custom duty
  receipts would still remain » (31 % des importations taxables hors UE ; produits industriels à
  contenu agricole exclus). Perte estimée de 1996, libéralisation multilatérale et DCP compris :
  55 MD, contre environ 80 MD de mesures compensatoires ; 1997 : 136 MD (0,7 % du PIB) contre
  125 MD. Taux effectif moyen : « from 10.5 percent to an estimated 6.0 percent » (p. 15). Le
  rapport ajoute que la perte « is likely to be higher if account is taken of the impact of trade
  diversion ». PIB : base non précisée par la source (ratio cité tel quel).
- Le FMI cite pour l'accord Jbili et Enders (1996) et Havrylyshyn (1996) : non récupérés (§ 11).
- Évaluations académiques de l'effet de l'accord sur les recettes : aucune lue ici ; la fiche de
  l'économiste (`docs/notes/eco-droits-douane.md`, à venir) est le lieu de ces études.

---

## 8. Dépenses fiscales en droits de douane (budgétaire, évaluation du ministère)

Rapports sur les dépenses fiscales annexés aux PLF. Millions de dinars. Les millésimes ne se
chaînent pas : chaque rapport réévalue les exercices précédents.

| Exercice | PLF 2021 | PLF 2022 | PLF 2023 | PLF 2024 | PLF 2025 |
|---|---:|---:|---:|---:|---:|
| 2017 | 382,3 | | | | |
| 2018 | 834,8 | | | | |
| 2019 | 815,0 | 815,1 | 812 | | |
| 2020 | | 754,9 | 751 | 790,2 | |
| 2021 | | | 898 | 937,1 | 937,1 |
| 2022 | | | | 1 411,9 | 1 452,6 |
| 2023 | | | | | 1 517,4 |

Sources : PLF 2021, tableau n° 3, p. 24 (fr) ; PLF 2022, p. 29 (ar) [@minfin-depenses-fiscales-plf2022] ;
PLF 2023, pp. 31-32 (ar, valeurs arrondies au million) [@minfin-depenses-fiscales-plf2023] ; PLF
2024 et 2025 : série `depenses_fiscales_par_impot_2017_2023.csv` (contrôlée sur les totaux
imprimés, fiche `sources/gbo-depenses-fiscales.md`).

- **Rapportées aux recettes de droits de douane**, selon les rapports eux-mêmes : 63,45 % en 2019
  (PLF 2021, tableau n° 4) ; 63,2 % (2019), 61,1 % (2020), 63,2 % (2021) (PLF 2023, p. 32, sur des
  recettes de 1 284, 1 228 et 1 420 MD, c'est-à-dire la rubrique avec redevances).
- **2017 → 2018 (382 → 835).** Le rapport l'explique : les dépenses fiscales des impôts indirects
  ont augmenté de plus de mille millions de dinars en 2018 « après l'annulation des réductions des
  droits de douane et du droit de consommation décidée à grande échelle en 2017 » (PLF 2021,
  p. 25). Dans le détail, un seul dispositif (code 213472601, « Exonération des droits de douane
  dus à l'importation des matières premières, produits semi-finis … n'ayant pas de similaires
  fabriqués localement destinés à l'industrie locale ») passe de 99,9 à 453,8 MD (2019 : 449,9 ;
  PLF 2021, tableau détaillé des droits de douane, p. 58). Le nombre de dispositifs est le même
  (72) les deux années.
- **Ruptures.** Nombre de dispositifs : 72 (2017-2018), 73 (2019-2020), 69 (2021, PLF 2023), 71 /
  67 valorisés (PLF 2024), 68 / 66 (PLF 2025) ; le PLF 2025 sort médicaments et engrais ;
  révisions entre millésimes jusqu'à 4 % (2020 : 754,9 → 790,2 ; 2022 : 1 411,9 → 1 452,6).
- **Manques.** Exercices antérieurs à 2017 (premier rapport : PLF 2021) ; exercices 2024-2026 : le
  rapport annexé au PLF 2026 n'est pas proposé sur `gbo.tn` (fiche, 11 octobre 2026) et n'a pas été
  trouvé par une recherche web le 23 octobre 2026. Une estimation antérieure existe hors du
  budgétaire : diaporama de la Banque mondiale de septembre 2014, « déductions douanières » de 405,
  504 et 394 MD en 2009-2011 (note `fiscalite-depenses-fiscales.md`, l. 257 ; famille rapport
  extérieur ; méthode non décrite).

---

## 9. Études et rapports pour la section « études » (distincts du budgétaire)

Chaque entrée : qui, quand, méthode, périmètre, page.

| Document | Méthode et périmètre | Chiffres retenus (page) | PDF |
|---|---|---|---|
| GATT 1994, C/RM/S/47 | calculs du Secrétariat sur les données des autorités ; tarif NPF ; 1987-1994 | taux moyens, fourchettes, droits / importations, part des recettes (pp. 55-57) | téléchargé |
| OMC 2005, WT/TPR/S/152 | idem ; 16 232 lignes à 11 chiffres (SH 2002) | tableaux III.1-III.2, § III.15-29 | téléchargé (.doc) |
| OMC 2016, WT/TPR/S/341 | idem ; 11 502 lignes à 9 chiffres (SH 2012) | graphique 3.2 (p. 46), tableaux 3.1-3.7 (pp. 44-55) | téléchargé |
| OMC 2025, WT/TPR/S/479/Rev.1 | idem ; 17 511 lignes à 11 chiffres (SH 2022) ; recettes « provided by the authorities » | tableaux 3.2-3.4 (pp. 38-42) | téléchargé (anglais ; français non trouvé) |
| FMI 1996, n° 96/27 | services du FMI ; sources ministère des Finances | pp. 29, 35, 53, 71 | présent |
| FMI 1997, n° 97/57 | services du FMI ; estimation de perte à importations et PIB de 1995 gelés | pp. 9, 12-13, 15 | présent |
| FMI 2015, n° 15/285 | « Tunisian authorities; and IMF staff estimates » ; méthode non décrite | mesure douanière : 0,22 / 0,20 / 0,09 % du PIB en 2016-2018 (p. 18) ; « seven tariff rates » (p. 71) | présent |
| FMI 2016, n° 16/138 | « Tunisian authorities; USAID; and IMF staff estimates » ; méthode non décrite | harmonisation tarifaire (de sept à deux taux) : − 316 MD, − 0,4 % du PIB en 2016 (p. 21) | présent |
| Banque mondiale 1995, n° 14375-TUN, annexe 2 | protection nominale et effective, 1983-1995 | moyennes et fourchettes (p. 5) | téléchargé |
| Banque mondiale 2014, n° 86179 | écarts miroir (importations déclarées / exportations des partenaires, SH6) ; enquête commerce informel | évasion : « at least US$100 million », dit 0,22 % du PIB (p. 17) et 0,15 % (p. 118) ; commerce informel : reprend Ayadi et al. 2013 (1,2 milliard de dinars), mais écrit « the equivalent of a quarter of total customs revenues » (encadré 3.4, p. 120) là où l'étude écrit, pour les seuls droits de douane, « more than one-sixth » | présent |
| Ayadi, Benjamin, Bensassi, Raballand 2013, WPS 6731 (évaluation économique) | statistiques miroir et enquête de terrain (Ras Jedir, Kasserine), commerce avec la Libye et l'Algérie, 2013 ; perte calculée au « lowest rate of tax burden on imports for this category of goods, or 72% of its value and 30% for customs duties » (note 39) | commerce informel d'au moins 1,8 milliard de dinars (terrain) ou 2,4 (valeurs unitaires) (tableau 1, p. 10) ; perte de recettes « at least around 1.2 billion TND (of which around 500 TND for customs duties or more than one-sixth of total customs duties) » (p. 27 ; « 500 » imprimé sans unité, millions d'après le contexte) ; source de l'encadré 3.4 de la Banque mondiale 2014 | téléchargé |
| Rijkers, Baghdadi, Raballand ; Rijkers, Freund, Nucifora | évasion tarifaire et entreprises liées au clan Ben Ali | à la charge de l'économiste | déjà dans `data/raw/eco-droits-douane/` (autre agent) |

---

## 10. Références candidates

### 10.1 Déjà présentes (vérifiées le 23 octobre 2026)

`minfin-recettes-fiscales`, `minfin-indicateurs-fp`, `lf-2001` à `lf-2026` (`precis/fr/references.json` ;
`lf-2002` et `lf-2008` dans `fiscalite/references.json`), `cdc-loireg-2019` à `cdc-loireg-2022`,
`cdc-rapport-budget-2023`, `gbo-depenses-fiscales`, `minfin-depenses-fiscales-plf2022`,
`minfin-depenses-fiscales-plf2023`, `fmi-1996-red`, `fmi-1997-selected-issues`,
`fmi-2015-article-iv`, `fmi-2016-cr16138`, `bct-ra-1998`, `bct-ra-1975` (livre compensation ; à
reporter dans fiscalité), `wb-wdi`, `ins-annuaire`.

### 10.2 À créer (ébauches CSL-JSON)

```json
[
  {"id": "gatt-1994-tpr-tunisie", "type": "report", "title": "Trade Policy Review Mechanism. Tunisia. Report by the Secretariat",
   "author": [{"literal": "GATT, Secrétariat"}], "number": "C/RM/S/47", "issued": {"date-parts": [[1994, 5, 24]]},
   "publisher": "GATT", "publisher-place": "Genève", "language": "en",
   "URL": "https://purl.stanford.edu/vs441dh1090",
   "note": "citation-key: gatt-1994-tpr-tunisie\nCopie : tunisia-data, data/raw/droits-douane/omc/gatt_1994_tpr_c-rm-s-47_en.pdf (GATT Digital Library, Stanford)."},
  {"id": "omc-2005-tpr-tunisie", "type": "report", "title": "Examen des politiques commerciales. Tunisie. Rapport du Secrétariat",
   "author": [{"literal": "OMC, Secrétariat"}], "number": "WT/TPR/S/152", "issued": {"date-parts": [[2005]]},
   "publisher": "Organisation mondiale du commerce", "publisher-place": "Genève", "language": "fr",
   "URL": "https://www.wto.org/french/tratop_f/tpr_f/s152-3_f.doc",
   "note": "citation-key: omc-2005-tpr-tunisie\nPublié en cinq fichiers .doc (s152-0 à s152-4) ; date exacte du document à relever sur la page de garde. Copie : data/raw/droits-douane/omc/."},
  {"id": "omc-2016-tpr-tunisie", "type": "report", "title": "Examen des politiques commerciales. Tunisie. Rapport du Secrétariat",
   "author": [{"literal": "OMC, Secrétariat"}], "number": "WT/TPR/S/341", "issued": {"date-parts": [[2016, 6, 8]]},
   "publisher": "Organisation mondiale du commerce", "publisher-place": "Genève", "language": "fr",
   "URL": "https://www.wto.org/french/tratop_f/tpr_f/s341_f.pdf",
   "note": "citation-key: omc-2016-tpr-tunisie"},
  {"id": "omc-2025-tpr-tunisie", "type": "report", "title": "Trade Policy Review. Tunisia. Report by the Secretariat. Revision",
   "author": [{"literal": "OMC, Secrétariat"}], "number": "WT/TPR/S/479/Rev.1", "issued": {"date-parts": [[2025, 10, 14]]},
   "publisher": "Organisation mondiale du commerce", "publisher-place": "Genève", "language": "en",
   "URL": "https://www.wto.org/english/news_e/news_docs/S479R1.pdf",
   "note": "citation-key: omc-2025-tpr-tunisie\nVersion française non trouvée (l'adresse homologue rend une page HTML)."},
  {"id": "bm-1995-vers-21e-siecle", "type": "report", "title": "République tunisienne : vers le XXIe siècle. Volume II : annexes",
   "author": [{"literal": "Banque mondiale"}], "number": "14375-TUN", "issued": {"date-parts": [[1995, 10]]},
   "publisher": "Banque mondiale", "publisher-place": "Washington", "language": "fr",
   "URL": "http://documents.worldbank.org/curated/en/448421468117264581/pdf/143750SR0v20FRENCH0Box109821B00PUBLIC0.pdf",
   "note": "citation-key: bm-1995-vers-21e-siecle"},
  {"id": "bm-2014-revolution-inachevee", "type": "report", "title": "The Unfinished Revolution: Bringing Opportunity, Good Jobs and Greater Wealth to All Tunisians",
   "author": [{"literal": "Banque mondiale"}], "number": "86179-TN", "issued": {"date-parts": [[2014, 5]]},
   "publisher": "Banque mondiale", "publisher-place": "Washington", "language": "en",
   "URL": "http://documents.worldbank.org/curated/en/658461468312323813/pdf/861790DPR0P12800Box385314B00PUBLIC0.pdf",
   "note": "citation-key: bm-2014-revolution-inachevee\nVérifier qu'aucune clé n'existe déjà sous un autre nom (wb-2014-…) dans les livres marché du travail ou entreprises publiques."},
  {"id": "ayadi-2013-commerce-informel", "type": "report", "title": "Estimating Informal Trade across Tunisia's Land Borders",
   "author": [{"family": "Ayadi", "given": "Lotfi"}, {"family": "Benjamin", "given": "Nancy"}, {"family": "Bensassi", "given": "Sami"}, {"family": "Raballand", "given": "Gaël"}],
   "collection-title": "Policy Research Working Paper", "number": "6731", "issued": {"date-parts": [[2013, 12]]},
   "publisher": "Banque mondiale", "publisher-place": "Washington", "language": "en",
   "URL": "https://documents.worldbank.org/curated/en/856231468173645854/pdf/WPS6731.pdf",
   "note": "citation-key: ayadi-2013-commerce-informel\nPrénoms à vérifier sur la page de titre."},
  {"id": "cdc-rapport-budget-2024", "type": "report", "title": "التقرير حول غلق ميزانية الدولة لسنة 2024",
   "author": [{"literal": "Cour des comptes"}], "issued": {"date-parts": [[2025]]}, "language": "ar",
   "URL": "https://www.courdescomptes.nat.tn/wp-content/uploads/pdf_rapport/%D8%AA%D9%82%D8%B1%D9%8A%D8%B1-%D8%AD%D9%88%D9%84-%D8%BA%D9%84%D9%82-%D9%85%D9%8A%D8%B2%D8%A7%D9%86%D9%8A%D9%91%D8%A9-%D8%A7%D9%84%D8%AF%D9%91%D9%88%D9%84%D8%A9-%D9%84%D8%B3%D9%86%D8%A9-2024.pdf",
   "note": "citation-key: cdc-rapport-budget-2024\nDate de mise en ligne à relever au catalogue de tunisia-data (sources/cour-des-comptes-catalog.csv)."},
  {"id": "minfin-depenses-fiscales-plf2021", "type": "report", "title": "Rapport sur les dépenses fiscales et les avantages financiers, annexe n° 14 au projet de loi de finances pour 2021",
   "author": [{"literal": "Ministère des Finances"}], "issued": {"date-parts": [[2020]]}, "language": "fr",
   "note": "citation-key: minfin-depenses-fiscales-plf2021\nÀ créer seulement si l'architecte préfère une clé par millésime à gbo-depenses-fiscales ; idem plf2024 et plf2025."}
]
```

---

## 11. PDF à rapatrier (pour `docs/notes/biblio-a-rapatrier.md`)

- Jbili, A. et Enders, K., « The Association Agreement between Tunisia and the European Union »,
  *Finance & Development*, juin 1996 ; Havrylyshyn, O. (1996) : cités par le FMI (1997, p. 12) ;
  non cherchés.
- Étude d'impact (Trade SIA) de l'ALECA UE-Tunisie, rapport final de 2013 : non trouvée (deux
  recherches web, 23 octobre 2026).
- Rapports annuels de la Direction générale des douanes tunisienne : non trouvés (une recherche
  web) ; à chercher sur `douane.gov.tn`.
- OMC 2025 en français : `https://www.wto.org/french/news_f/news_docs/S479R1.pdf` rend une page
  HTML.

---

## 12. Ruptures de série et lacunes

**Ruptures (à porter sur toute figure)** :

1. Rubrique du ministère = droits + redevances (toute la série) ; ventilation connue en prévision
   depuis 2001 et en réalisation depuis 2018 seulement.
2. Nomenclature budgétaire 2020 (21-xx → 17-xx), raccord établi.
3. PIB : segments 1986-1996 (base 1983), 1997-2001 (base 1997), 2002-2004 (non rattaché),
   2005-2009 (base 1997), 2010-2024 (base 2015), 2025 (non rattaché).
4. Importations : BCT jusqu'en 1997, INS depuis 1998 (raccord 1998 : 9 489 / 9 489,5) ;
   révision INS du régime off shore en 2004-2005.
5. GFS (WDI) : 1996 → 1997, part de 37,3 à 20,1 %.
6. Tarif : nombre de lignes 6 000 (1994), 16 232 (2005), 11 502 (2016), 17 511 (2025) ; les
   moyennes simples de l'OMC changent de base avec la nomenclature (2025 : 23,8 à 11 chiffres,
   22,3 à 9 chiffres).
7. Dépenses fiscales : millésimes non chaînables ; PLF 2025 hors médicaments et engrais.

**Lacunes** (aucune valeur inventée) :

- Prévisions du tableau A avant 2001 (lisibles à l'image, pages connues pour 1970-1993 ; 1994-2000
  à localiser).
- Ventilation droits / redevances des réalisations avant 2018 : rapports de la Cour des comptes
  antérieurs (`loireg2018.pdf` sans couche texte, autres non rassemblés) ; lois de règlement.
- Droits de douane 1960-1985 : rapports annuels de la BCT (1972-1975 seulement relevés).
- Importations 2024-2025 et avant 1988.
- Taux moyens annuels hors années couvertes par le GATT, l'OMC et les WDI (1990-1993, 1996-2001,
  2017-2024).
- Aucune estimation de perte de recettes liée à l'accord avec l'UE postérieure à 1997, avec
  méthode, n'a été lue.
- Dépenses fiscales avant 2017 et après 2023.
- Date d'application effective du démantèlement (1996 ou 1998) : note textes.
- Non cherchés : études de l'ITCEQ, évaluations de la Commission européenne (hors l'étude d'impact
  de l'ALECA, cherchée sans succès). EUR-Lex n'a pas répondu (réponse vide, 23 octobre 2026) : le
  texte de l'accord vient du répertoire de l'autre documentaliste.
- Taux effectif moyen du FMI 1997 (« from 10.5 percent to an estimated 6.0 percent », p. 15) :
  l'année de départ n'est pas dite ; laissé hors du CSV.

---

## 13. Pour `docs/notes/backlog-precis.md`

- `precis/fr/fiscalite/index.qmd`, l. 56-58 : la phrase « l'effet du démantèlement tarifaire
  engagé avec l'accord d'association de 1995 » n'a pas de source ; la remplacer par l'attribution
  de l'OMC (2005, § III.15 ; 2016, § 3.22), citée comme telle, avec ses deux facteurs (§ 7.1), et
  fermer le TODO. Même fichier, l. 62 : « ils n'ont pas de chapitre propre dans ce livre » devient
  faux quand le chapitre paraît.
- `_depenses_fiscales.qmd`, TODO l. 161 : la répartition par impôt des rapports PLF 2022 et 2023
  est relevée ici pour les droits de douane (§ 8) ; les autres impôts sont sur les mêmes pages
  (PLF 2022, p. 29 ; PLF 2023, pp. 31-32).

## 14. Propositions de figures

1. **Part des droits de douane dans les recettes fiscales et dans les dépenses de l'État hors
   dette, 1986-2025** (budgétaire ; aucune question de base). Marque du passage aux tableaux 2020.
2. **Part du PIB par segments de base** (même numérateur), six segments non reliés, ruptures
   1997, 2002, 2005, 2010, 2025 renvoyant à `annexe-pib.qmd` ; module à calquer sur
   `finances_locales.py` (`_pib_par_base`, `_ruptures_pib`).
3. **Taux de perception implicite, 1988-2023**, deux courbes (importations totales ; régime
   général depuis 1998), avec en superposition, légende distincte, les moyennes simples NPF de
   l'OMC/GATT (1987-1989, 1994, 2004-2016, 2025) : même dispositif, familles différentes ; l'écart
   entre les deux mesures est l'objet de la figure (exonérations, offshore, préférences).
4. **Droits et redevances, prévision 2001-2026 et réalisation 2018-2024** (barres empilées ;
   budgétaire).
5. **Dépenses fiscales en droits de douane par millésime de rapport, 2017-2023**, points reliés
   par millésime seulement, à côté des recettes de la rubrique.

---

## 15. Notions à glossaire

| Terme FR | Terme AR | Source canonique pressentie |
|---|---|---|
| droits de douane (à l'importation) | المعاليم الديوانية (عند التوريد) | tableau A des LF ; tarif de la loi n° 89-113 |
| redevance sur les prestations douanières | الأتاوة على الخدمات الديوانية ; أتاوة الخدمات الديوانية | tableau A (17-02 / 21-02) ; texte d'institution : note textes |
| droits complémentaires provisoires (DCP ; « droits compensatoires provisoires » avant 1994) | à relever au JORT | FMI 1996, GATT 1994 ; texte : note textes |
| régime douanier / régime intérieur (des recettes) | نظام ديواني / نظام داخلي | classeur du ministère ; tableau A (TVA, droit de consommation) |
| régime off shore (statistique du commerce extérieur) | نظام غير مقيم | INS, annuaire, tableau 14.2 |
| taux NPF ; taux consolidé ; taux préférentiel | — (à relever) | rapports de l'OMC |
| taux de perception implicite | — | notion de la note ; à définir dans le chapitre |
| dépense fiscale (déjà au glossaire : `depense-fiscale`) | النفقة الجبائية | rapports annexés aux PLF |

---

## 16. Recherches infructueuses

Aucune recherche de texte au *Journal officiel* n'a été menée pour cette note (les textes sont à
l'autre documentaliste) : aucune fiche `docs/recherches.yml` n'est proposée. Les documents non
trouvés sont des rapports, listés au § 11 pour `biblio-a-rapatrier.md`.
