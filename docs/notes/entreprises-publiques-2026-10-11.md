# Note documentaire — les entreprises publiques : la relation financière entre l'État et ses entreprises (11 octobre 2026)

Premier passage pour un texte nouveau (volume court ou chapitre : non arrêté, voir § 8). Objet :
périmètre, transferts budgétaires, garanties et dette, résultats, dividendes, cessions, effectifs.
L'économique et le temps long d'abord ; le droit seulement pour dater les ruptures.

**Niveaux de preuve**, en clair : « lu à l'image » (page rendue et lue) ; « couche texte »
(`pdftotext`, non relue à l'image) ; « intitulé seul » (notice de `jort_cache.db`) ; « classeur »
(cellules d'un fichier `.xls` lues par programme). Pages : « p. » = numéro imprimé sur la page ;
« p. PDF » = rang dans le fichier, quand les deux diffèrent.

**Trois familles de chiffres, jamais sur le même plan** : (A) budgétaire — ministère des Finances
(annexes n° 7, 8 et 9 des projets de loi de finances), Direction générale de la privatisation ;
(B) rapport officiel de réforme (Livre blanc de 2018, Présidence du gouvernement), qui cite des
ratios sans méthode ; (C) rapports extérieurs et évaluation (Banque mondiale, FMI, ITCEQ).

**Fichiers** : `~/projets/tunisia-data/data/raw/caisses/minfin/` (annexes) et
`~/projets/tunisia-data/data/raw/entreprises-publiques/` (privatisation, Livre blanc, études) ;
catalogue `sources/entreprises-publiques-urls.csv`, fiche `sources/entreprises-publiques.md`.

---

## 1. Ce qui est établi, série par série

### 1.0 Les éditions en main, leur périmètre, leurs tableaux

**Constat de départ, qui commande tout le reste.** L'inventaire est meilleur que prévu — l'annexe
n° 9 est en main pour **six** lois de finances (LF 2020 à LF 2025), l'annexe n° 8 pour six aussi
depuis ce passage (LF 2023 récupérée) — mais **le périmètre change à chaque édition**, et le
ministère ne publie aucune série longue. La série de rapports **commence avec la LF 2020** : le
rapport dit lui-même qu'il existe en application de l'article 46 de la loi organique du budget
n° 2019-15 du 13 février 2019 (annexe 9, LF 2020, p. 12 et 19, couche texte).

#### Annexe n° 9 — « Rapport sur les entreprises publiques » (التقرير حول المنشآت العمومية)

| Édition | Fichier, langue, pages | Entreprises publiques recensées | Agrégats d'ensemble | Échantillon analysé | Années |
|---|---|---|---|---|---|
| LF 2020 (oct. 2019) | `Annexe_9_LF2020-Entreprises_publiques.pdf`, fr, 159 p. ; `annexe9_LF2020_ar.pdf`, ar, 105 p. | 110 (tableau 1, p. 21) | **aucun tableau agrégé** ; prose sur « le reste des établissements » (87) pour 2016 | 31 : 3 banques, Poste, CPSCL, 3 caisses, 23 autres | 2016, 2017, 2018 « probable » |
| LF 2021 | `Annexe_9_LF2021_Entreprises_Publiques.pdf`, fr, 179 p. | 110, dont 64 sociétés anonymes et 46 EPNA (p. 7) ; 71 à participation directe de l'État, 39 indirecte (p. 8) | **78** (tableau 1, p. 20) | 33 | 2017, 2018 ; 2019 probable ; 2020 prévisionnel |
| LF 2022 | `annexe9_2022.pdf`, ar, 128 p. | 111 (p. 13) | **77** (tableau 2, p. 14) | 50, dont 40 hors finance et caisses | 2018-2019 (agrégats) ; 2018-2020 (échantillon) |
| LF 2023 | `rapport_ep_2023.pdf`, ar, 242 p. | 111 (p. 21) | **81** (tableau 1, p. 21) | 50 (48 pour les flux avec l'État) | 2019-2020 ; 2019-2021 |
| LF 2024 | `rapport_ep_LF2024.pdf`, ar, 186 p. | 114 (p. 23) | **88** (tableau 1, p. 23) | 50 (48 pour les flux) | 2020-2021 ; 2020-2022 |
| LF 2025 | `rapport_ep_LF2025.pdf`, ar, 128 p. | 115 (p. 13) | **85** (tableau 1, p. 13) | 50 (42 pour les dettes croisées) | 2021-2022 ; 2021-2023 |
| LF 2026 | **non trouvée** (§ 5.1) | | | | |

Niveau de preuve : éditions françaises en couche texte ; éditions arabes — tableaux 1 ou 2 et
flux avec l'État — **lus à l'image**. L'édition française de la LF 2021 dit en page de garde de
l'annexe 8 sœur : « Traduction française élaborée dans le cadre du projet d'appui aux réformes
budgétaire et comptable […] La version arabe officielle fait foi » ; l'original arabe de
l'annexe 9 LF 2021 existe sur gbo.tn (`2021-04/تقرير حول المنشات العمومية.pdf`, vu dans les
résultats de recherche, non téléchargé).

**Ce que chaque agrégat exclut** (toujours : les entreprises du secteur financier et assimilé, 7 ;
les 3 caisses sociales ; 1 entreprise à l'arrêt ; celles qui n'ont pas transmis leurs comptes) :
LF 2021, 110 − 32 = 78 (12 sans états financiers 2018, 6 créations récentes, 3 en retard, 7
financières, 3 caisses, 1 à l'arrêt ; p. 20) ; LF 2022, 111 − 34 = 77 (16 + 7 + 7 + 3 + 1 ; p. 13) ;
LF 2023, 111 − 30 = 81 (19 + 7 + 3 + 1) ; LF 2024, 114 − 26 = 88 (15 + 7 + 3 + 1) ; LF 2025,
115 − 30 = 85 (19 + 7 + 3 + 1). **Les banques publiques et les caisses ne sont jamais dans les
agrégats de résultats** ; elles sont dans l'échantillon des flux avec l'État.

**Qualité des comptes sous-jacents**, que le rapport dit lui-même : en 2020, sur 81 entreprises,
65 états financiers définitifs, 3 provisoires, 13 « documents d'orientation » (LF 2023, p. 21) ;
en 2021, sur 88 : 63, 4 et 21 (LF 2024, p. 23) ; en 2022, sur 85 : 62 états arrêtés au
31 décembre 2022 et 23 documents d'orientation (LF 2025, p. 13). Les données de dettes croisées
« sont pour l'essentiel fournies par les entreprises ; les services du ministère des Finances
n'assument aucune responsabilité quant à leur fiabilité » (LF 2025, p. 124, lu à l'image).

**Liste des tableaux.** LF 2020 : 25 tableaux (liste p. 10-11) — tableau 1 sélection de
l'échantillon ; 2 à 15 indicateurs par secteur et par tutelle (banques, caisses, tabac, transport,
énergie, industrie, agriculture, santé, équipement) pour 2016-2018 ; 16 à 25 contrats-programmes
des banques et contrats de performance (Office des céréales, RNTA, STIR). LF 2021 : 47 tableaux au
moins — 1 agrégats ; 2 à 8 « dix premières entreprises » (produits, charges, charges de personnel,
résultats d'exploitation positifs et négatifs, résultats nets positifs et négatifs) ; 9 à 11
échantillon ; 12 à 25 indicateurs par tutelle ; **26 à 28 décaissements au budget** ; **29 à 31
transferts de l'État** ; 32 à 35 besoins en fonds propres (art. 388 du code des sociétés
commerciales) et crédits de restructuration ; 36 à 47 liquidité et découverts. Les éditions arabes
reprennent ce plan : agrégats (tableau 1 ou 2), dix premières (2 à 8 ou 3 à 9), liquidité,
échantillon de 50 par tutelle, puis flux avec l'État (LF 2022 : tableaux 33 à 38 ; LF 2023 : 35 à
40 ; LF 2024 : 40 à 45). **La LF 2025 abandonne décaissements et transferts** pour une partie
nouvelle, « relation financière entre l'État et les entreprises publiques » : dettes et créances
croisées, puis revenus des participations (p. 113-126).

#### Annexe n° 8 — « Rapport sur les transferts et les garanties au profit des entreprises publiques et des établissements publics non administratifs »

| Édition | Fichier, langue, pages | Réalisations | Loi de finances | Garanties accordées |
|---|---|---|---|---|
| LF 2020 | `annexe8_transferts_LF2020.pdf`, fr, 147 p. | 2016, 2017, 2018 | 2019 | 2016, 2017, 2018, 1er sem. 2019 |
| LF 2021 | `annexe8_transferts_LF2021.pdf`, fr (traduction), 94 p. | 2017, 2018, 2019 | 2020 | 2017-2019, 1er sem. 2020 |
| LF 2022 | `annexe8_transferts_LF2022.pdf`, ar, 110 p. | 2018, 2019, 2020 | 2021 | 2018-2020, juin 2021 |
| LF 2023 | `annexe8_transferts_LF2023.pdf`, ar, 110 p. — **récupérée le 11/10/2026** | 2019, 2020, 2021 | 2022 | 2019-2021, juin 2022 |
| LF 2024 | `annexe8_transferts_LF2024.pdf`, ar, 118 p. | 2020, 2021, 2022 | 2023 | 2020-2022, juin 2023 |
| LF 2025 | `annexe8_transferts_LF2025.pdf`, ar, 126 p. | 2021, 2022, 2023 | 2024 | 2021-2023, juin 2024 |

Périmètre : **tous** les établissements publics non administratifs et entreprises publiques,
caisses sociales comprises, classés en quatre « secteurs » (social, économique, éducatif et
culturel, souveraineté) d'après le ministère qui porte le crédit. Chaque édition porte en annexe
les transferts **par établissement et par nature de dépense** (LF 2020 : annexe 1, p. 62-123) —
non dépouillés ici.

### 1.1 Les transferts du budget à l'ensemble des entreprises et établissements publics (annexe 8) — 2016-2024

Famille A. Millions de dinars courants (les tableaux sont en milliers de dinars ; arrondi au
dixième). Édition retenue : la plus récente qui donne l'année en réalisation. Résumés des
éditions : LF 2020 p. [5]-[6] et LF 2021 p. [3]-[4] (fr, couche texte) ; LF 2022 p. 7-8, LF 2023
p. 7-8, LF 2024 p. 7-8, LF 2025 p. 7-8 (ar, **lus à l'image**).

| Année | Statut | Total | Social | Économique | Éducatif et culturel | Souveraineté | Édition |
|---|---|---:|---:|---:|---:|---:|---|
| 2016 | réalisé, **ancien périmètre** | 4 152,2 | 719,7 | 2 959,9 | 302,8 | 169,8 | LF 2020 |
| 2017 | réalisé | 6 852,6 | 1 542,2 | 4 618,7 | 317,4 | 372,7 | LF 2021 |
| 2018 | réalisé | 8 392,3 | 1 735,5 | 5 856,4 | 381,1 | 419,2 | LF 2022 |
| 2019 | réalisé | 8 668,9 | 2 049,9 | 5 698,1 | 426,0 | 494,9 | LF 2023 |
| 2020 | réalisé | 9 895,9 | 2 931,0 | 5 738,6 | 581,8 | 644,6 | LF 2024 |
| 2021 | réalisé | 10 772,8 | 2 273,0 | 7 324,6 | 492,0 | 683,3 | LF 2025 |
| 2022 | réalisé | 17 078,6 | 2 521,6 | 13 398,2 | 500,3 | 658,4 | LF 2025 |
| 2023 | réalisé | 17 104,8 | 3 080,0 | 12 734,5 | 593,6 | 696,7 | LF 2025 |
| 2024 | loi de finances | 17 332,2 | 3 204,3 | 12 758,5 | 622,9 | 746,5 | LF 2025 |

Par nature de dépense (mêmes pages) :

| Année | Rémunération | Fonctionnement | Interventions | Investissement |
|---|---:|---:|---:|---:|
| 2016 (ancien périmètre ; **colonne douteuse**) | 389,7 | 120,3 | 2 886,7 | 414,7 |
| 2017 | 807,0 | 115,2 | 5 546,4 | 384,0 |
| 2018 | 896,1 | 107,7 | 6 971,1 | 417,4 |
| 2019 | 1 007,2 | 171,3 | 6 826,7 | 663,7 |
| 2020 | 1 182,0 | 209,3 | 7 758,6 | 746,0 |
| 2021 | 1 144,4 | 362,3 | 8 717,3 | 548,7 |
| 2022 | 1 176,4 | 204,9 | 15 054,7 | 642,5 |
| 2023 (**une case à relire**) | 1 248,3 | 428,3 | 14 710,3 | 695,0 |
| 2024 (LF) | 1 312,1 | 487,2 | 14 637,2 | 895,7 |

Contrôle de sommes (calcul de la note) : les quatre natures font le total à 0,1 près pour 2017 à
2022 et pour 2024. **Deux lignes ne se somment pas** : 2016, 3 811,5 pour un total imprimé de
4 152,2 — et le même tableau de la LF 2020 imprime ailleurs « 451 895 » là où « 895 451 »
ferait tomber la colonne de 2018 : la ventilation par nature de cette édition n'est pas fiable ;
2023, 17 081,9 pour 17 104,8 (22,9 d'écart) alors que les secteurs et les sources de la même
page font bien 17 104,8 : une des quatre cases est mal imprimée ou mal lue, à relire.

Par source de financement, les ressources propres du budget portent 91 à 95 % du total chaque
année (2021 : 10 230,9 sur 10 772,8 ; 2023 : 15 662,7 sur 17 104,8) ; le reste vient des comptes
spéciaux du Trésor (521,2 en 2021 ; 1 395,0 en 2023), des crédits extérieurs affectés et des dons.

**Ruptures et réserves, à écrire avec la série.**

- **Révision de périmètre entre la LF 2020 et la LF 2021.** La LF 2020 donnait 6 161,8 MD pour
  2017 et 7 712,3 pour 2018 ; la LF 2021 donne 6 852,6 et 8 392,1. L'écart est dans le secteur
  social (995,8 → 1 542,2 en 2017) et la souveraineté (229,9 → 372,7). **2016 n'existe que dans
  l'ancien périmètre** : on ne le chaîne pas à 2017 ; la série se trace en deux segments.
- **Révisions mineures ensuite** : 2019 passe de 8 489,1 (LF 2021) à 8 613,2 (LF 2022) puis
  8 668,9 (LF 2023) ; 2020 de 9 897,1 (LF 2022) à 9 895,9 (LF 2023 et LF 2024). Les réalisations
  2021 et 2022 sont identiques dans les LF 2024 et LF 2025.
- **Loi de finances contre réalisation** : 2020, 8 155,1 en loi de finances (LF 2021) contre
  9 895,9 réalisés ; 2021, 7 729,6 contre 10 772,8 ; 2022, 12 436,6 contre 17 078,6 ; 2023,
  14 514,5 contre 17 104,8. L'exécution dépasse la loi de finances de 18 à 39 % quatre années de
  suite (calcul de la note sur les valeurs ci-dessus).
- **Ce total n'est pas « le coût des entreprises publiques »**. Il réunit les caisses sociales
  (secteur social), les établissements d'enseignement et de culture, et — dans le secteur
  économique — **la compensation** : chaque édition avertit que « de nombreux transferts à
  caractère social », subvention des produits alimentaires et du transport public, « ont été
  classés au sein du secteur économique » parce que les crédits vont à des établissements sous
  tutelle de ministères classés économiques (LF 2021, p. [5] ; LF 2022 à LF 2025, p. 8). Le saut
  de 2022 (+ 6,3 milliards, tout en interventions du secteur économique) est celui de la
  compensation : voir § 7. Le calcul « hors compensation » demande les annexes par
  établissement ; non fait, à ne pas approximer.
- **Ratios imprimés**, donnés tels quels, base du PIB non dite : 7,1 % du PIB en 2017, 7,9 % en
  2018, 7,7 % en 2019, 6,5 % en loi de finances 2020 ; 25,1 %, 28,1 %, 26,0 % et 22,9 % du budget
  de l'État (LF 2021, tableau 1.1, p. [13]). Loi de finances 2021 : 21,3 % du budget et 6,3 % du
  PIB (LF 2022, p. 7). Loi de finances 2022 : 29,0 % du budget et 9,3 % du PIB (LF 2023, p. 7). À
  partir de la LF 2024 le rapport ne donne plus de part du PIB mais une part des dépenses hors
  service de la dette : 29,7 % en loi de finances 2023, 28,9 % en loi de finances 2024.

### 1.2 Les garanties de l'État : plafond, garanties accordées, encours garanti — 2016-juin 2024

Famille A. **Trois grandeurs distinctes** : le plafond annuel (paramètre légal, article de la loi
de finances) ; les garanties accordées dans l'année (flux) ; l'encours de la dette garantie
(stock). Sources : annexe 8 (résumés cités au § 1.1) et annexe 7 « Rapport sur la dette publique »
— LF 2022, p. 56-58, et LF 2025, p. 62-65, **lues à l'image**.

| Année | Plafond de la loi de finances | Garanties accordées | dont prêts extérieurs | dont prêts intérieurs |
|---|---:|---:|---:|---:|
| 2016 | 3 000 | 2 362,2 | 877,3 | 1 484,9 |
| 2017 | 3 000 | 2 659,2 | 1 818,2 | 841,0 |
| 2018 | 3 000 | 2 592,7 | 734,9 | 1 857,8 |
| 2019 | 4 790 (4 500 en loi de finances initiale) | 4 589,0 | 2 198,7 | 2 390,3 |
| 2020 | 7 000 (5 000 en loi de finances initiale) | 4 603,4 | 1 730,6 | 2 872,8 |
| 2021 | 7 000 | 2 487,6 | 2 232,9 | 254,7 |
| 2022 | 7 000 | 2 558,8 | 568,7 | 1 990,1 |
| 2023 | 8 000 | 5 155,0 | 2 099,3 | 3 055,7 |
| 1er sem. 2024 | 8 000 | 1 840,7 | 1 165,0 | 675,8 |

| Fin d'année | Encours garanti | Extérieur | Intérieur | % du PIB imprimé (LF 2022) | % du PIB imprimé (LF 2025) |
|---|---:|---:|---:|---:|---:|
| 2016 | 11 269,5 | 9 261,9 | 2 007,6 | 11,83 | — |
| 2017 | 13 671,8 | 11 302,8 | 2 369,0 | 13,40 | — |
| 2018 | 16 713,4 | 13 719,2 | 2 994,2 | 14,83 | — |
| 2019 | 16 702,0 | 12 714,5 | 3 987,5 | 13,62 | 13,6 |
| 2020 | 17 208,1 | 13 213,5 | 3 994,6 | 14,70 | 14,4 |
| 2021 | 18 742,0 | 12 209,3 | 6 532,7 | — | 14,3 |
| 2022 | 20 363,1 | 11 770,6 | 8 592,5 | — | 14,1 |
| 2023 | 21 383,3 | 12 539,8 | 8 843,5 | — | 13,5 |
| juin 2024 (estimation) | 21 515,9 | 12 215,9 | 9 300,0 | — | 13,4 |

Points sûrs :

- **Le plafond a plus que doublé en quatre ans** (3 000 MD de 2016 à 2018 ; 7 000 à partir de
  2020 ; 8 000 depuis 2023), et **la nature des garanties a changé** : après 2020 elles couvrent
  des opérations d'exploitation et non plus seulement l'investissement. L'annexe 7 de la LF 2025
  le chiffre (p. 64) : garanties intérieures de 2023, 3 055,7 MD en 36 opérations, dont 1 215,2
  pour financer l'importation de produits de base (pétrole, gaz, céréales, engrais, sucre, café),
  1 550,4 au titre de l'audit complet des banques publiques, 141,0 de rééchelonnements, 25,1
  d'investissement. Le même poste « importations de produits de base » : 188,2 en 2021, 956,1 en
  2022, 321,2 au premier semestre 2024.
- **L'encours garanti intérieur a plus que quadruplé** de 2016 (2 007,6) à 2023 (8 843,5) quand
  l'encours extérieur augmentait d'un tiers (9 261,9 → 12 539,8) : le risque s'est déplacé vers
  les banques locales.
- **Garanties liées à l'audit des banques publiques** (engagements d'entreprises publiques envers
  la STB, la BH et la BNA) : 1 390,0 MD en 2016, 11,1 en 2017, 1 092,1 en 2018, 1 357,7 en 2019,
  1 810,8 en 2020, 1 815,6 en 2021, dont BNA 1 575,6 (LF 2022, annexe 7, p. 57). Le rapport
  précise que ces garanties sont données pour un an au titre des engagements de l'année écoulée.
- **Cadre** (annexe 8, LF 2020, p. [38], couche texte) : article 45 de la loi organique du budget
  de 2019 (la loi de finances fixe « le plafond des garanties de l'État et le plafond des prêts
  du Trésor ») ; article 9 de la loi de finances de l'année ; arrêté du 3 avril 1993 sur la
  commission de garantie (le rapport écrit « décret ministériel » ; non lu au JORT).
- **Écarts entre éditions à signaler** : le plafond de 2020 après loi de finances rectificative
  est de 7 500 MD dans la traduction française de l'annexe 8 LF 2021 (p. [5]) et de 7 000 MD dans
  toutes les éditions arabes postérieures — à trancher sur le texte de la loi de finances
  rectificative ; les garanties de 2020 sont 4 603,4 (annexe 7 ; annexe 8 LF 2022 et LF 2023) et
  4 603,7 (annexe 8 LF 2024) ; le ratio au PIB de 2020 passe de 14,70 % (LF 2022) à 14,4 %
  (LF 2025), PIB révisé sans que la base soit dite.
- **Profondeur possible bien au-delà de 2016 pour le plafond** : `jort_cache` indexe un article
  « octroi de la garantie de l'État » dans chaque loi de finances de 1961 (loi n° 60-38) à 1994
  (loi n° 93-125), intitulés seuls ; 147 notices portent « garantie de l'Etat » ou « ضمان
  الدولة ». Série légale à dépouiller en second passage (§ 6).

### 1.3 Résultats agrégés des entreprises publiques (annexe 9) — exercices 2017 à 2022

Famille A. Millions de dinars. Hors banques, hors caisses, hors entreprises sans comptes.
LF 2021 : tableau 1, p. 20 (fr, couche texte). LF 2022 : tableau 2, p. 14 ; LF 2023 : tableau 1,
p. 21 ; LF 2024 : tableau 1, p. 23 ; LF 2025 : tableau 1, p. 13 (ar, **lus à l'image**).

| Exercice | Édition (nombre d'entreprises) | Produits d'exploitation | Charges de personnel | Charges d'exploitation | Résultat d'exploitation | Somme des résultats nets positifs | Somme des résultats nets négatifs | Résultat net agrégé |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2017 | LF 2021 (78) | 25 445,8 | 3 372,9 | 25 944,3 | −498,5 | 308,7 | −3 031,9 | −2 723,1 |
| 2018 | LF 2021 (78) | 30 745,2 | 3 578,6 | 31 565,5 | −820,2 | 546,5 | −4 733,6 | −4 187,1 |
| 2018 | LF 2022 (77) | 30 850,6 | 3 492,1 | 31 259,0 | −408,4 | 515,9 | −4 489,7 | −3 973,8 |
| 2019 | LF 2022 (77) | 32 192,2 | 3 839,9 | 33 227,4 | −1 255,4 | 1 100,1 | −1 811,5 | −711,5 |
| 2019 | LF 2023 (81) | 32 950,8 | 3 770,3 | 33 613,5 | −662,8 | 1 101,9 | −1 279,8 | −177,9 |
| 2020 | LF 2023 (81) | 27 015,4 | 3 867,9 | 28 176,1 | −1 160,7 | 188,0 | −2 643,3 | −2 455,3 |
| 2020 | LF 2024 (88) | 26 906,4 | 4 113,1 | 28 470,0 | −1 563,6 | 174,6 | −3 156,3 | −2 981,7 |
| 2021 | LF 2024 (88) | 34 535,0 | 4 175,0 | 34 022,6 | 512,4 | 576,9 | −1 706,2 | −1 129,3 |
| 2021 | LF 2025 (85) | 34 479,3 | 4 144,1 | 34 013,9 | 466,0 | 602,2 | −2 146,8 | −1 544,6 |
| 2022 | LF 2025 (85) | 49 118,1 | 4 279,3 | 48 371,4 | 746,5 | 1 763,2 | −4 302,9 | −2 539,7 |

Lecture, et limites :

- **Chaque exercice est donné deux fois, par deux échantillons** : on présente les couples
  d'années d'une même édition (la variation est à périmètre constant à l'intérieur d'une
  édition), jamais une série de 2017 à 2022 d'un seul trait. L'écart entre éditions peut être
  grand : résultat net agrégé de 2019, −711,5 (77 entreprises) puis −177,9 (81).
- **Le résultat net agrégé est négatif pour tous les exercices publiés, 2017 à 2022**, entre
  −0,2 et −4,2 milliards de dinars.
- **Les produits d'exploitation contiennent les subventions d'exploitation** : la hausse de 2022
  (+ 14,6 milliards) vient pour beaucoup des subventions (STEG : subvention d'exploitation en
  hausse de 3 338,6 MD, LF 2025, p. 14). Le résultat d'exploitation positif de 2021 et 2022 est
  donc un résultat **après compensation**.
- **Défaut du tableau de la LF 2022** : le résultat d'exploitation imprimé (−408,4 en 2018,
  −1 255,4 en 2019) n'est pas la somme des deux lignes qui le précèdent (1 138,7 − 1 747,1 =
  −608,4 ; 1 018,2 − 2 035,2 = −1 017,0). Les résultats nets, eux, se somment. À dire si l'on
  cite ces deux valeurs.
- **Concentration** : les dix premières entreprises font 78 à 85 % des produits d'exploitation
  (77,9 % en 2017, 79,9 % en 2018, LF 2021 p. 23 ; 81,8 % en 2021, 84,5 % en 2022, LF 2025 p. 18)
  et 66 à 72 % des charges de personnel.
- **Prose de la LF 2020, autre périmètre** (87 établissements hors finance et caisses, exercice
  2016, p. 14-15) : produits d'exploitation 21 173 MD, charges 20 930 MD, bénéfices nets 170,5 MD
  contre 1 326 MD de pertes nettes ; charges de personnel 2 939,3 MD, en hausse de 40 % sur 2011,
  quand les produits d'exploitation baissaient de 2 %. Seul repère antérieur à 2017, et seule
  comparaison avec 2011, dans les annexes.
- **Valeur ajoutée, chiffre d'affaires au sens strict, total de bilan** : aucun agrégat publié.

### 1.4 Ce que les entreprises versent au budget, ce qu'elles en reçoivent (annexe 9, échantillon) — 2017-2022

Famille A. Échantillon **banques et caisses comprises**, donc autre périmètre que le § 1.3, et
autre périmètre que l'annexe 8 (§ 1.1). LF 2021 : tableaux 26, 27, 29, 30, p. 143-149 (fr, couche
texte). LF 2022 : tableaux 33, 34, 36, 37, p. 100-104 ; LF 2023 : p. 195-199 ; LF 2024 :
p. 149-153 (ar, **lus à l'image**).

| Année | Édition (échantillon) | Versements au budget | dont fiscaux et douaniers | dont bénéfices transférés et commissions de garantie | Transferts reçus | dont subventions d'exploitation et d'équilibre | dont investissement et capital | dont prêts du Trésor et rétrocédés |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2017 | LF 2021 (33) | 5 619,7 | 3 734,1 | 25,6 | 4 201,2 | 3 438,9 | 194,8 | 567,5 |
| 2018 | LF 2021 (33) | 6 321,6 | 4 133,5 | 153,7 | 5 270,2 | 4 759,6 | 427,6 | 83,0 |
| 2018 | LF 2022 (50) | 5 860,8 | 4 492,9 | 157,6 | 5 863,6 | 5 248,1 | 529,1 | 86,4 |
| 2019 | LF 2022 (50) | 6 590,3 | 5 160,8 | 346,1 | 6 198,0 | 5 401,2 | 686,8 | 110,0 |
| 2019 | LF 2023 (48) | 6 457,6 | 5 030,0 | 351,0 | 6 629,5 | 6 088,2 | 428,8 | 112,5 |
| 2020 | LF 2023 (48) | 6 122,3 | 4 761,0 | 191,7 | 4 609,7 | 3 677,7 | 407,8 | 524,2 |
| 2020 | LF 2024 (48) | 6 192,4 | 4 775,0 | 191,7 | 6 466,4 | 5 488,4 | 443,2 | 534,8 |
| 2021 | LF 2024 (48) | 6 433,7 | 5 216,7 | 115,1 | 8 402,2 | 7 394,8 | 566,4 | 441,2 |
| 2022 (provisoire) | LF 2024 (48) | 7 620,8 | 6 384,1 | 167,0 | 14 560,6 | 13 638,3 | 555,2 | 367,1 |

- **Solde versements − transferts de l'échantillon**, tel que le rapport le calcule (LF 2024,
  p. 149) : −274 MD en 2020, −1 968,5 en 2021, −6 939,8 en 2022 (provisoire). La LF 2023 (p. 195)
  donnait −171,9 en 2019, + 1 512,6 en 2020 et + 202,5 en 2021 provisoire — avant révision des
  transferts de 2020 (4 609,7 → 6 466,4) et de 2021 (6 085,1 → 8 402,2).
- **Les « versements » sont d'abord des « décaissements fiscaux et douaniers »** : 64 à 66 % du
  total de 2017 à 2019 dans la LF 2021 (tableau 27, p. 145), 77 à 84 % dans les éditions
  suivantes (76,6 % en 2018, 78,3 % en 2019, LF 2022 ; 77,1 % en 2020, 81,1 % en 2021, 83,8 % en
  2022, LF 2024). Le reste, dit le rapport, ce sont des « autres décaissements provenant
  principalement de la régie nationale des tabacs et des allumettes, de la manufacture des
  tabacs de Kairouan et de l'entreprise tunisienne des activités pétrolières » (LF 2021,
  p. 145). Ce n'est pas un rendement du capital public ; le rendement proprement dit est au
  § 1.5.
- **Rupture de définition entre la LF 2021 et la LF 2022** : la RNTA verse 1 559,2 MD en 2018
  selon la LF 2021 (tableau 28, p. 147) et 910,1 selon la LF 2022 (tableau 35, p. 102) ; la
  Manufacture des tabacs de Kairouan 566,2 puis 338,0. Les deux éditions ne comptent pas les
  mêmes prélèvements ; ne pas chaîner 2017 aux années suivantes.
- **Deux valeurs imprimées pour les transferts de 2022 dans la LF 2024, sans départage possible.**
  14 506,6 : tableau 43 et prose (p. 153), et c'est sur elle que sont calculés la hausse imprimée
  de 72,7 % et la part de 31,3 % des dépenses hors service de la dette. 14 560,6 : tableau de
  comparaison (p. 149), somme des trois composantes du tableau 44 (13 638,3 + 555,2 + 367,1),
  total du tableau 45 par entreprise (p. 155, lu à l'image) et solde imprimé (7 620,8 −
  14 560,6 = −6 939,8). Le tableau ci-dessus porte 14 560,6, valeur que retrouvent les détails ;
  toute citation donne les deux.
- **Pourquoi 2020 et 2021 changent d'une édition à l'autre** — le rapport le dit (LF 2024,
  p. 155, lu à l'image) : pour 2020, mise à jour des transferts à la CNSS (exclue de l'édition
  précédente faute de données transmises) et à la CNRPS ; pour 2021, mise à jour de l'Office des
  céréales après certification de ses comptes, et de la CNSS. La révision de 2020 (4 609,7 →
  6 466,4, soit + 1 856,7) est presque entièrement celle des caisses : CNSS 0 → 1 321,6 et CNRPS
  460 → 970,6, ensemble + 1 832,2. **C'est l'entrée des caisses qui renverse le solde de 2020,
  de + 1 512,6 à −274.**
- **Règlement d'arriérés de 2020.** La LF 2021 (p. 142, couche texte) signale l'« affectation
  dans le cadre du projet de la loi de finances complémentaire pour l'année 2020 de crédits
  d'environ 4 100 MD au titre du règlement des dettes arriérés à la charge de l'État surtout
  envers l'Office des céréales, la Société tunisienne de l'électricité et du gaz, la Société
  tunisienne des industries de raffinage et la Société nationale de distribution du pétrole »,
  et la création d'une commission de liquidation des dettes et créances croisées. Les transferts
  de 2020 de l'échantillon ne laissent pas voir ces 4 100 MD (STEG 100, STIR 594) : leur
  traitement — exécutés ou non, comptés en transferts ou en apurement — n'est pas établi.
- Ratios imprimés : versements de l'échantillon, 23,5 % des ressources propres de l'État en 2017,
  22,6 % en 2018 (LF 2021) ; 21 % en 2018, 20,4 % en 2019 (LF 2022) ; 20,3 % en 2020, 19,2 % en
  2021, 18,5 % en 2022 (LF 2024). Transferts de l'échantillon : 15,4 % des dépenses de l'État hors
  service de la dette en 2017, 17,7 % en 2018 (LF 2021) ; 17,4 % en 2020, 21,1 % en 2021, 31,3 %
  en 2022 (LF 2024).

**La LF 2025 remplace ces flux par des encours croisés** (échantillon de 42 entreprises, hors
banques ; p. 115-123, **lu à l'image**) :

| Fin d'année | Dettes des entreprises envers l'État | Créances des entreprises sur l'État | Écart |
|---|---:|---:|---:|
| 2021 | 8 391,8 | 9 864,4 | −1 472,6 |
| 2022 | 10 899,3 | 12 184,3 | −1 285,0 |
| 2023 | 11 246,3 | 11 960,7 | −714,4 |

Composition en 2023 — dettes envers l'État : impôts et taxes 6 561,5 (58,3 %) ; prêts et avances
du Trésor 3 456,7 (30,7 %) ; autres dettes 757,6 ; deux petites lignes de 371,1 et 99,3 dont les
libellés arabe et français du graphique se contredisent (« حصص أرباح / Redevances » et « أتاوات /
Dividendes et excédents ») — à ne pas nommer sans relecture. Créances sur l'État : **subventions
non réglées 6 956,8 (58,2 %)**, dont STEG 3 151,6, Office des céréales 2 185,3, STIR 762, Office
national de l'huile 512,6 ; prestations rendues 3 312,3 ; impôts et taxes 1 049,0 ; autres. Le
rapport précise que la créance de la STEG au titre du complément de subvention (3 423,1 MD fin
2022, 3 151,6 fin 2023) est calculée par la société et **n'est pas confirmée** par le ministère
(p. 124).

Autrement dit : **fin 2023, l'État doit à ses entreprises un peu plus qu'elles ne lui doivent**,
et ce qu'il leur doit est d'abord de la compensation impayée.

### 1.5 Dividendes : la part de l'État dans les bénéfices et excédents — exercices 2017 à 2023

Famille A. « Part de l'État dans les excédents et bénéfices enregistrés par les entreprises
publiques au titre de l'exercice comptable » (حصة الدولة من الفوائض والأرباح), entreprises à
participation directe (71).

| Exercice | MD | Révision | Édition, page, preuve |
|---|---:|---|---|
| 2017 | 163 | | LF 2021, p. 150, couche texte ; 9 entreprises distributrices |
| 2018 | 333 | | LF 2021, p. 150 ; dont ETAP 295 (85 %) ; 7 distributrices |
| 2019 | 263,8 | 230 dans la LF 2022 | LF 2023, couche texte ; ETAP 146,5 |
| 2020 | 98,3 | 67,1 dans la LF 2023 | LF 2024, couche texte ; la CPSCL fait près de 60 % du montant de la LF 2023 |
| 2021 | 145,4 | 140,1 dans la LF 2024 | LF 2025, p. 125, **lu à l'image** ; 14 distributrices |
| 2022 | 204,6 | | LF 2025, p. 125 ; 12 distributrices sur 71 |
| 2023 (provisoire) | 195,6 | | LF 2025, p. 125 |

Sur 2021-2023 cumulés, 545,6 MD, dont Poste 100, Tunisie Télécom 64,6, CPSCL 58,6, BNA 57,2, CPG
50, OMMP 50, BH 46,7, OACA 45, SNDP 45 — neuf entreprises pour 95 % (LF 2025, p. 126). **Ordre de
grandeur : 0,1 à 0,3 milliard de dividendes par an, contre 8 à 17 milliards de transferts.** La
LF 2020 donnait pour 2018 des « revenus de l'État provenant de ces établissements » de 263,5 MD,
« 5,1 % du total des transferts accordés » (p. 17) : autre définition, non raccordée.

### 1.6 Les plus lourdes, entreprise par entreprise

**Transferts du budget** (échantillon de l'annexe 9 ; édition la plus récente pour chaque année ;
LF 2021 tableau 31, p. 149-150, couche texte ; LF 2022 tableau 38, p. 105 ; LF 2023 tableau 40,
p. 200 ; LF 2024 tableau 45, p. 154 — lus à l'image). MD.

| Entreprise | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 (prov.) |
|---|---:|---:|---:|---:|---:|---:|
| STIR (raffinage) | 869,4 | 1 846,1 | 1 905,3 | 594,0 | 2 293,0 | 4 321,0 |
| Office des céréales | 980,2 | 1 403,5 | 1 800,2 | 1 726,5 | 1 687,5 | 3 237,4 |
| STEG | 914,6 | 1 200,0 | 1 242,0 | 100,0 | 1 034,0 | 3 307,0 |
| CNSS | 0 | 0 | 0 | 1 321,6 | 842,0 | 943,5 |
| CNRPS | 500 | 200 | 450,0 | 970,6 | 762,3 | 579,5 |
| SONEDE | 180,7 | 156,0 | 169,9 | 378,8 | 366,1 | 369,1 |
| Office national de l'huile | 286,5 | 305,0 | 292,4 | 310,1 | 322,9 | 345,5 |
| ONAS | 58,0 | 155,9 | 210,7 | 201,3 | 222,5 | 185,5 |
| Tunisie Autoroutes | 0 | 0 | 180,0 | 163,4 | 180,9 | 170,0 |
| Transtu | 154,4 | 144,2 | 138,6 | 179,3 | 161,9 | 147,5 |
| SNCFT | 104,6 | 86,6 | 93,2 | 152,9 | 135,4 | 129,8 |
| Tunisair | 0 | 0 | 0 | 35,4 | 41,2 | 0 |
| Office du commerce | 16,9 | 20,2 | 24,0 | 20,1 | 10,2 | 0,8 |

Réserves : 2017 vient de la seule LF 2021. Les éditions se contredisent sur plusieurs cases —
STIR 2018 : 1 500 (LF 2021) puis 1 846,1 (LF 2022) ; STIR 2019 : 1 296 (LF 2021, LF 2022) puis
1 905,3 (LF 2023) ; Office des céréales 2018 : 1 320,3 puis 1 403,5 ; 2019 : 1 324,1 puis
1 800,2 ; ONAS 2018 : 59,4 puis 155,9 ; SNCFT 2018 : 96,2 puis 86,6. Les révisions vont presque
toutes à la hausse : la subvention d'une année est soldée les années suivantes. Les lignes CNSS
et CNRPS relèvent du volume « Caisses » ; STIR, STEG et Office des céréales du volume
« Compensation » ; Transtu et SNCFT de la note sur le transport (§ 7).

**Résultat net** (tableaux « dix premières entreprises » des éditions LF 2021 à LF 2025, p. citées
au § 1.3 et pages suivantes ; une entreprise absente du classement d'une année n'a pas de valeur
— « — »). MD.

| Entreprise | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---|---:|---:|---:|---:|---:|---:|
| STEG | −1 193,7 | −2 093,5 | +106,4 | −60,2 | −42,7 | −381,2 |
| STIR | −429,9 | −1 159,5 (LF 2021) ; −813,4 (LF 2022) | −612,3 | +59,1 | +3,8 (LF 2025, p. 70) | −1 902,9 |
| ETAP | +111,2 | +297,5 | +150,0 | −407,1 | −139,0 | +352,2 |
| Office des céréales | — | −76,0 | −175,6 | −340,6 | −477,2 | −701,4 |
| CPG (phosphates) | −128,9 | −130,8 | +640,6 | −293,3 | +47,0 | +445,0 |
| GCT (chimie) | −122,2 | −108,8 | −204,7 | −593,3 (LF 2024) ; −205,0 (LF 2023) | +148,9 | +63,1 |
| Tunisair | −206,6 | −96,8 (LF 2021) ; −192,6 (LF 2022) | — | −234,0 | −414,1 | −176,3 |
| Transtu | −167,3 | −187,5 | −202,2 | −215,1 | −229,8 | −226,5 |
| SNCFT | −82,2 | −91,1 | −113,8 | −103,4 | −137,3 | −199,8 |
| Office du commerce | −43 (prose, LF 2021) | +6,4 (prose, LF 2021) | — | +8,4 | −128,2 | −424,0 |
| RNTA (tabacs) | −49,6 | −49,5 (prose, LF 2021) | −54,7 | +12,0 | +96,9 | +130,7 |
| Pharmacie centrale | −144,8 | −234,6 | +11,9 | — | +45,5 | — |

Réserves : valeurs de classements, pas de séries ; plusieurs sont révisées d'une édition à
l'autre (les deux valeurs sont données quand l'écart est grand). Le résultat de la CPG en 2019
(+ 640,6) et celui de la STEG avant et après « modifications comptables » (2021 : −42,7 avant,
+ 3 469,6 après ; 2022 : −381,2 avant, −2 716,1 après ; LF 2025, p. 70, lu à l'image après
rotation) tiennent à des écritures exceptionnelles que le rapport ne détaille pas dans les pages
lues. La STEG perd 2,1 milliards en 2018 **après** 1,2 milliard de subvention ; pour l'ensemble des
78 entreprises, le rapport attribue la dégradation de 2018 à l'« augmentation des charges
financières agrégées suite à l'évolution des pertes de change sur les crédits extérieurs »
(LF 2021, p. 22), et 67,9 % de la dette de la STEG est due à des banques étrangères.

**Dette, effectifs, subvention d'exploitation — ce qui a été relevé** (non exhaustif) :

| Entreprise | Grandeur | Valeurs | Source |
|---|---|---|---|
| STEG | dettes totales | 8 594,5 MD (2017) ; 11 397,4 (2018), dont banques étrangères 7 745,1 ; 12 104,5 (2019 probable) | LF 2021, fiche STEG § 4.5, couche texte |
| STEG | total des passifs | 13 838,6 (2021) ; 16 441,8 (2022) ; 17 885,8 (2023 provisoire) | LF 2025, p. 70, image |
| STEG | effectifs | 12 031 (2018) ; 13 063 (2019) ; 13 854 (2021) ; 13 473 (2022) ; 13 979 (2023) | LF 2021 ; LF 2025, p. 70 |
| STEG | subvention d'exploitation | 1 368,8 (2021) ; 4 707,4 (2022) ; 3 365,0 (2023) | LF 2025, p. 70 |
| STIR | dettes | 1 699,8 (2017) ; 2 743,6 (2018) ; 3 304,5 (2019 probable) | LF 2021, fiche STIR § 2.5 |
| STIR | effectifs ; subvention d'exploitation | 538, 546, 598 (2021-2023) ; 2 073,0, 4 101,0, 2 840,1 | LF 2025, p. 70 |
| Tunisair | dettes | 2 567,5 (2017) ; 3 098,8 (2018), dont banques 1 065,7 | LF 2021, fiche Tunisair § 1.5 |
| Tunisair | effectifs ; charges de personnel ; revenus ; résultat net | 3 303, 3 193, 3 107 agents (2021-2023, provisoire) ; 209,7, 234,9, 259,7 ; 560,9, 1 362,6, 1 656,6 ; −414,1, −176,3, −211,1. **Bilan non publié : « la société n'a pas approuvé ses états financiers pour la période 2021-2023 »** | LF 2025, p. 56, image après rotation |
| Transtu | effectifs ; charges de personnel ; revenus ; subvention d'exploitation ; résultat net ; résultats reportés | 7 350, 7 089, 6 791 agents (2021 provisoire, 2022 et 2023 probables) ; 287,0, 293,1, 301,7 ; **52,6, 52,6, 51,4** ; 135,0, 140,0, 141,0 ; −229,8, −226,5, −225,4 ; −1 621,2, −1 851,0, −2 077,5. Bilan « non disponible à la date du rapport » | LF 2025, p. 60, image après rotation |
| SNCFT | effectifs ; charges de personnel ; subvention d'exploitation ; résultat net ; résultats reportés ; total des passifs | 4 790, 4 690, 4 539 agents (2021-2023, 2023 probable) ; 133,0, 135,5, 140,7 ; 84,5, 70,0, 95,0 ; −137,3, −199,8, −115,3 ; −891,8, −1 068,6, −1 188 ; 1 680,5 (2021), 1 873,6 (2022) | LF 2025, p. 60, image après rotation |
| SONEDE | effectifs ; résultat net ; total des passifs | 6 632, 6 784, 6 488 agents (2021-2023) ; −37,4, −21,1, −8,9 ; 1 664,0 (2021), 1 869,7 (2022) | LF 2025, p. 88, image après rotation |
| Transtu | dettes | 862 (2017) ; 969 (2018) ; 1 187 (2019 probable) ; dont caisses sociales 197 (2018) | LF 2021, fiche § 5.5 |
| SNCFT | dettes ; effectifs | 1 326 (2017), 1 096,3 (2018), dont banques 824,8 ; 4 612 agents (2018) | LF 2021, fiche § 6.2 et 6.5 |
| GCT | dettes ; effectifs | 1 217,5 (2017), 1 495,9 (2018), 1 565,9 (2019 probable) ; 5 852 agents (2018) | LF 2021 |
| CPG | dettes ; effectifs | 488,3 (2017), 510,8 (2018) ; 6 098 agents (2018), 7 421 prévus en 2019 | LF 2021 |
| ETAP | dettes ; effectifs | 916 (2018), 789 (2019) ; 802 agents (2018) | LF 2021 |
| Office des céréales | dettes ; effectifs | 939,5 (2017), 1 221,5 (2018), 2 229,5 (2019 probable) ; 1 223 agents (2018) | LF 2021 |
| RNTA | dettes ; effectifs | 395,8 (2017), 491,5 (2018) ; 1 336 agents (2018) | LF 2021 |

**Dettes et créances croisées avec l'État fin 2023, dix premières** (LF 2025, p. 119 et 123, lu à
l'image). Dettes envers l'État : CNRPS 2 968,8 ; Office des céréales 1 631,1 ; Transtu 1 509,3 ;
CNSS 800,2 ; ETAP 486,4 ; OACA 473,6 ; SNCPA 320,0 ; CPG 290,0 ; ONAS 252,0 ; Tunisair 232,4 — dix
entreprises pour environ 80 % du total. Créances sur l'État : STEG 3 974,1 ; Office des céréales
2 193,0 ; SONEDE 809,2 ; STIR 784,7 ; Pharmacie centrale 578,0 ; CPSCL 532,9 ; Office de l'huile
513,3 ; Transtu 365,2 ; CNSS 345,8 ; SNDP 322,4 — la STEG seule pour un tiers.

**Niveau de preuve à dire au rédacteur** : les tableaux par entreprise des éditions arabes (un
par tutelle, une vingtaine de colonnes : effectifs, charges de personnel, revenus, subventions
d'exploitation, résultat d'exploitation, charges financières nettes, résultat net avant et après
modifications comptables, immobilisations, capitaux propres, emprunts, fournisseurs, total des
passifs) sont **imprimés tournés d'un quart de tour** ; illisibles à la résolution courante, ils
se lisent après rendu à 170 dpi et rotation. Fait pour quatre pages de la LF 2025 (p. 56
Tunisair ; p. 60 SNCFT et Transtu ; p. 70 STEG et STIR ; p. 88 SONEDE et Office des terres
domaniales). Restent, dans la seule LF 2025 : ETAP et GCT (p. 72-73), CPG (p. 71), Office des
céréales (p. 89), RNTA (p. 50), Office du commerce (p. 107) ; et les éditions LF 2022 à LF 2024
pour 2018-2020 (§ 6). **Deux constats tirés de ces pages** : les revenus propres de la Transtu
(52,6 MD en 2022) couvrent moins d'un cinquième de ses charges de personnel (293,1 MD), et ses
pertes reportées dépassent 2 milliards fin 2023 ; trois des plus lourdes — Tunisair, Transtu,
et la SNCFT pour 2023 — n'ont pas de bilan dans le rapport.

### 1.7 Effectifs et masse salariale d'ensemble

- **Correction du 11 octobre 2026 (second passage, séries versées dans `tunisia-data`, PR n° 61
  « Entreprises publiques : effectifs par entreprise (2016-2023) et effectif total publié »)** :
  la phrase qui suit est fausse. Un effectif total **est** publié, dans le chapitre
  d'introduction des éditions arabes de l'annexe 9, avec les charges de personnel : exercice
  2018, 99 836 agents et 3 596,5 MD (84 entreprises pour les agents, 82 pour les charges ;
  LF 2022) ; 2019, 99 523 agents et 3 939,53 MD (86 ; LF 2023) ; 2020, 96 305,5 agents et
  4 113,1 MD (88 ; LF 2024) ; 2022, 97 208 agents et 4 279,3 MD (85 ; LF 2025). Hors secteur
  financier et hors caisses ; quatre points, quatre périmètres, pas une série ; rien pour 2021
  ni avant 2018 ; le total de 2020 ne recoupe pas la somme des fiches. Voir
  `sources/entreprises-publiques.md`, section « Effectifs ».
- ~~**Aucun effectif total n'est publié dans les annexes.**~~ Seule la masse existe : charges de
  personnel agrégées, 3,4 à 4,3 milliards de dinars de 2017 à 2022 (§ 1.3), hors banques et
  caisses ; 2 939,3 MD en 2016 pour 87 établissements, + 40 % sur 2011 (LF 2020, p. 14).
- Dix premières par charges de personnel, 2022 (LF 2025, p. 19, image) : STEG 615,7 ; Tunisie
  Télécom 338,5 ; GCT 337,0 ; CPG 331,0 ; Transtu 293,1 ; Tunisair 234,9 ; OACA 228,9 ; SONEDE
  227,3 ; SNCFT 135,5 ; ONAS 109,5 — 2 608,9 MD imprimés, 66,3 % des 85 entreprises (la somme des
  dix lignes fait 2 851,4 : total imprimé à ne pas reprendre sans réserve). En 2017 (LF 2021,
  p. 25) : STEG 428,0 ; Tunisie Télécom 265,8 ; GCT 256,2 ; Tunisair 242,6 ; Transtu 239,4 ; CPG
  231,2.
- Familles B et C, séparément : « 4 % de la population active occupée et près de 12 % de la masse
  salariale totale » en 2014 (Livre blanc, p. 8 ; p. PDF 16) ; « an estimated 190,000 workers or
  2.2 percent of the working-age population, which represents 5 percent of employment » (Banque
  mondiale 2020, p. PDF 11).
- Les grilles, augmentations et statuts des agents sont au volume « Rémunérations publiques »
  (§ 7) ; la statistique INS de l'emploi par secteur institutionnel n'a pas été cherchée ici.

### 1.8 Cessions : recettes de privatisation — 1987-2009

Famille A. Source : Direction générale de la privatisation (Premier ministère), classeur
« Recettes des opérations de privatisation et de restructuration des entreprises à participations
publiques par année », retrouvé dans les archives du web — édition 1987-2005 (classeur enregistré
le 2 février 2006) et édition arabe 1987-2009 (enregistré le 17 février 2010). Milliers de dinars
courants. Niveau de preuve : **classeur**.

| Année | Recettes | Année | Recettes | Année | Recettes |
|---|---:|---|---:|---|---:|
| 1987 | 6 772 | 1995 | 68 413 | 2003 | 35 468,5 |
| 1988 | 26 992 | 1996 | 57 185 | 2004 | 27 227,2 |
| 1989 | 50 644 | 1997 | 80 621 | 2005 | 80 441,4 |
| 1990 | 16 581 | 1998 | 456 650 | 2006 | 3 110 480,1 |
| 1991 | 24 939 | 1999 | 43 495,2 | 2007 | 135 568,6 |
| 1992 | 18 414 | 2000 | 433 237 | 2008 | 302 562,2 |
| 1993 | 22 319 | 2001 | 125 084 | 2009 | 12 142,0 |
| 1994 | 23 609 | 2002 | 817 531 | **Total** | **5 976 376,2** |

- **Contrôle** : les sommes par plan retrouvent la page officielle « par période » encore en
  ligne (privatisation.pm.gov.tn, consultée le 11/10/2026) — VIIe Plan 1987-1991 : 126 MD,
  37 entreprises ; VIIIe 1992-1996 : 190 MD, 44 ; IXe 1997-2001 : 1 139 MD, 75 ; Xe 2002-2006 :
  4 071 MD, 51 ; XIe 2007-2009 : 438 MD, 10 ; total 5 963 MD, 217 entreprises, 425 opérations « du
  31/12/1987 au 31/01/2009 ». L'écart avec le classeur (5 976,4) est l'année 2009 après janvier.
- **Bilan par mode** (même site) : 114 privatisations totales, 29 partielles, 10 ouvertures de
  capital par offre publique de vente, 5 concessions, 41 liquidations, 18 autres.
- **Révisions entre les deux classeurs** : 1998, 481 394 (éd. 2006) puis 456 650 ; 1999, 68 859
  puis 43 495,2 ; 2003 à 2005, écarts inférieurs à 150. L'édition de 2010 est retenue.
- **Une seule opération fait la moitié du total** : 2006, 3,1 milliards, l'ouverture du capital
  de Tunisie Télécom (3 052 MD selon l'ITCEQ, famille C, p. 29-30).
- **Après 2009 : aucune série trouvée** (§ 5.2). Le site officiel dit lui-même que ses
  statistiques « couvrent la période allant du 31/12/1987 au 31/01/2009 ».

### 1.9 Les études et rapports extérieurs — familles B et C, à part

| Document | Qui, quand | Données, périmètre | Méthode | Chiffres d'ensemble (tels quels) |
|---|---|---|---|---|
| **Livre blanc — rapport de synthèse sur la réforme de la gouvernance des entreprises publiques** (famille B) | Présidence du gouvernement, mars 2018, 58 p. | Cite le « Rapport annuel sur les résultats des établissements publics durant la période 2010-2014 » de l'Unité de suivi du système de productivité des établissements et entreprises publics (Présidence du gouvernement) — **rapport non retrouvé** (§ 5.3) ; « données de 2014 qui sont certifiées » | Synthèse de réforme ; aucun calcul exposé ; base du PIB non dite | 102 entreprises publiques (dont 46 sociétés anonymes), 73 EPNA non considérés comme entreprises publiques, 24 établissements publics de santé (p. 7 ; plus loin le même rapport écrit 74 et 23, « 199 structures ») ; « environ 190 entreprises publiques » au milieu des années 1980, « 30 % des emplois dans le secteur formel » ; contribution de 9,5 % du PIB en 2014 contre 13 % en 2010 ; revenus agrégés + 27 % et bénéfices −55 % de 2010 à 2014 ; subventions d'exploitation et d'investissement de 8,9 % du PIB en 2013 et 7,5 % en 2014 ; dette extérieure garantie de 12 % du PIB en 2015 contre 10 % en 2013, la STEG pour plus de la moitié ; dette bancaire d'environ 5 % du PIB (p. 7-12 ; p. PDF 15-20) |
| **Tunisia Public Expenditure Review — A New Pact for the Transition**, rapport de synthèse (famille C) | Banque mondiale, 2020, 79 p. | Données budgétaires détaillées (initiative BOOST) « complemented by a year-long data collection effort among key SOEs » ; exercices 2015-2016 ; énergie, eau, transport | Revue de dépenses ; agrégats sur les 20 plus grandes ; passifs éventuels = « total of guarantees, on-lending, and treasury loans to SOEs in 2016 » (note 1) | Passifs éventuels de 14 % du PIB ; pertes des 20 plus grandes, 1,3 milliard de dinars en 2016 (1,5 % du PIB), dont 26 % pour la STEG ; dette extérieure garantie de la STEG, 5,4 milliards (6 % du PIB), « about 50 percent of total guarantees on external debt of SOEs » ; transferts aux entreprises de transport, 564 MD en 2016 ; déficit de l'eau et de l'assainissement hors subventions, 300 MD en 2015 ; 190 000 salariés ; « the government estimates that they make up between 9 and 10 percent of GDP » ; prime salariale de 34 % pour les salariés des entreprises publiques — **de seconde main** : la note 5 renvoie à Tamirisa et Duenwald, FMI, 2017, non récupéré (p. PDF 8, 11, 25, 57) |
| **Tunisia: 2021 Article IV Consultation**, Country Report No. 21/44 (famille C) | FMI, février 2021, 97 p. ; annexe IV « SOE Reform » | « Data on financial information for 30 SOEs » ; « full data on all SOEs is not available » ; budget des autorités et calculs des services | Addition des dettes de 30 entreprises ; test de résistance de la dette publique (réalisation de 10 % des garanties, 3 % de recapitalisation) | Dette des 30 entreprises d'environ 40 % du PIB fin 2019, dont 20 % envers banques et fournisseurs ; garanties d'environ 15 % du PIB à la mi-2020 ; transferts budgétaires annuels de 7 à 8 % du PIB, dont près de 40 % pour trois entreprises (céréales, carburants, électricité) ; crédits bancaires aux entreprises publiques d'environ 17 % du PIB ; **fin juin 2020, arriérés des entreprises envers l'État 6,2 milliards de dinars, arriérés de l'État envers elles 8,8 milliards** (§ 7 et notes 5-6, p. PDF 13-14 ; analyse de viabilité, p. PDF 50) |
| **Privatisation et développement du secteur privé**, MEDPRO WP5, rapport d'étape (famille C) | ITCEQ, décembre 2010, 53 p. | Recoupements INS, ministère du Développement, Direction générale de la privatisation | Bilan descriptif ; suivi des entreprises privatisées | 219 entreprises cédées depuis 1987 ; « de l'ordre de 6 milliards de dinars », « dont environ 90 % sous forme d'investissement direct étranger » ; services 84,5 % des recettes ; Tunisie Télécom 3 052 MD (p. 29-30) |

Concordances utiles, à présenter sur un graphique plutôt que dans un tableau commun : garanties
de 14-15 % du PIB (Banque mondiale 2016, FMI mi-2020) contre encours garanti de 11,8 à 14,8 % du
PIB imprimé par l'annexe 7 (2016-2020) ; arriérés croisés du FMI à juin 2020 (6,2 et 8,8
milliards) contre dettes et créances croisées de l'annexe 9 fin 2021 (8,4 et 9,9). Périmètres
différents (30 entreprises ; 42 hors banques) : la comparaison se commente, elle ne se chaîne pas.

**OCDE** : aucun examen consacré aux entreprises publiques tunisiennes n'a été trouvé (deux
requêtes) ; sont apparus l'examen d'évaluation de l'impact sur la concurrence (Tunisie, 2023) et
la note « Le droit de la concurrence et les entreprises publiques » (DAF/COMP/GF/WD(2018)71),
non lus. **Cour des comptes** (famille de contrôle, à part) : le catalogue de `tunisia-data`
porte des rapports par entreprise — STEG, secteur de l'électricité (2011) ; STIR (2006) ; SNDP
(2014) ; SONEDE (2012) ; ONAS (2014) ; Tunisie Autoroutes (2016) ; flotte de Tunisair (2018) ;
RNTA (2009) ; OACA (2011) ; Poste (2018) ; BNA (2009), STB (2008), BH (2021) ; sociétés
régionales de transport ; dette publique extérieure (2018) — rubriques 61, 74, 79 et 81 **non
téléchargées**, 82 et 90 téléchargées ; aucun n'a été ouvert ici.

---

## 2. Les ruptures proposées, dans l'ordre des dates

Pour chacune : ce qu'elle change pour le périmètre et pour l'argent. URL : fascicules du JORT sur
pist.tn, édition française (existence vérifiée par requête HEAD le 11/10/2026 ; contenu lu sur la
copie locale du corpus).

| Date | Texte | Ce qui change — périmètre | Ce qui change — argent | Preuve |
|---|---|---|---|---|
| 1969 | Loi n° 69-50 du 26 juillet 1969, relative à la tutelle de l'État sur les entreprises publiques et leurs filiales — JORT n° 28 des 25-29 juillet-1er août 1969, p. 911-912 — `https://www.pist.tn/jort/1969/1969F/Jo02869.pdf` | Étend le contrôle financier (décret du 1er avril 1948) aux « Sociétés filiales des Offices, Sociétés Nationales et Sociétés ou Groupements dans lesquels l'État détient une participation au capital » ; filiale = participation directe ou indirecte « au moins égale à 10 % du capital » (art. 1er) ; idem pour les collectivités publiques (art. 2) | Contrôleurs économiques et financiers nommés par arrêté (art. 3) | lu à l'image, art. 1 à 3 |
| 1985 | Loi n° 85-72 du 20 juillet 1985, relative à la tutelle et aux obligations mises à la charge des établissements publics à caractère industriel et commercial et des sociétés dans lesquelles l'État et les collectivités publiques locales détiennent une participation en capital — JORT n° 56 des 26-30 juillet 1985, p. 958-961 — `https://www.pist.tn/jort/1985/1985F/Jo05685.pdf` | Seuil de **34 %** : « entreprises-mères » = EPIC et sociétés dont le capital est détenu par l'État ou une collectivité locale « à raison de 34 % au moins » ; filiales à plus de 50 % (art. 1er) | Le conseil d'administration arrête les budgets et **établit avec la tutelle les contrats-programmes** (art. 11) ; contrôleurs financiers (art. 14-15) | lu à l'image, p. 958-959 ; p. 960-961 non lues |
| 1987 | Loi n° 87-47 du 2 août 1987, relative à la restructuration des entreprises publiques — JORT n° 56 du 14 août 1987, p. 958-959 (rectificatif au n° 69, p. 1204, intitulé seul) — `https://www.pist.tn/jort/1987/1987F/Jo05687.pdf` | Première autorisation générale de cession : « L'État est, dans ce cadre, autorisé à céder tout ou partie de ses participations directes ou indirectes » (art. 1er) ; liste des entreprises à restructurer fixée par décret (art. 2) | Commission de restructuration qui évalue et propose les conditions de cession (art. 4-6) ; avantages aux acquéreurs — dégrèvement des revenus réinvestis, exonération d'impôt sur les bénéfices cinq ans, exonération de la plus-value (art. 11) ; paiement possible à 50 % en bons d'équipement (art. 12) ; **renonciation de l'État au privilège du Trésor**, rééchelonnement ou abandon partiel de créances (art. 13) | lu à l'image, entier |
| 1989 | Loi n° 89-9 du 1er février 1989, relative aux participations et entreprises publiques — JORT n° 9 du 7 février 1989, p. 203-205 — `https://www.pist.tn/jort/1989/1989F/Jo00989.pdf` | **Définition** (art. 8) : établissements publics n'ayant pas un caractère administratif ; sociétés à capital entièrement détenu par l'État ; sociétés détenues **à plus de 50 %** par l'État, les collectivités locales, les établissements publics et les sociétés à capital entièrement public. Transitoire (art. 9) : jusqu'au 31 décembre 1991 au plus tard, restent régies par la loi les entreprises détenues à 34 % ou plus et inscrites sur une liste fixée par décret. Le seuil passe donc de 34 à 50 % | Contrôle général sur tout organisme recevant « participations en capital, subventions, prêts, avances ou garanties » (art. 7) ; contrats-programmes approuvés par le conseil (art. 10) ; publication des comptes au JORT avant le 31 août (art. 14) ; contrôleurs d'État (art. 15-17). Titre III : « Le gouvernement est, dans ce cadre, autorisé à céder tout ou partie des participations de l'État » (art. 23) ; commission d'assainissement et de restructuration (art. 24-26) ; décisions arrêtées par le Premier ministre (art. 27) ; avantages aux salariés et aux acquéreurs (art. 29-30) Paiement possible à 50 % en bons d'équipement et obligations d'État (art. 31) ; renonciation au privilège du Trésor, rééchelonnement ou abandon partiel de créances (art. 32). **Art. 34 : abroge les lois n° 85-72 et n° 85-73 du 20 juillet 1985 et la loi n° 87-47 du 2 août 1987** | lu à l'image, entier (p. 203-205) |
| 1993 | Loi n° 93-124 du 27 décembre 1993, portant prorogation des dispositions de l'article 9 de la loi n° 89-9 — JORT n° 99, p. 2185 | Proroge le régime transitoire des 34 % | — | intitulé seul |
| 1994 | Loi n° 94-102 du 1er août 1994 — JORT n° 62 du 9 août 1994, p. 1290-1291 — `https://www.pist.tn/jort/1994/1994F/Jo06294.pdf` | À partir du 1er janvier 1995 (date dite par le texte), art. 9 nouveau : « sont également considérées entreprises publiques les banques et les sociétés d'assurance dont le capital est détenu par l'État de manière directe ou indirecte à 34 % ou plus » | Outils de privatisation : **action spécifique** de l'État (art. 33-2, 33-3), vente de blocs d'actions par appel d'offres sur cahier des charges (art. 33-4 à 33-6) | couche texte, entier |
| 1996 | Loi n° 96-74 du 29 juillet 1996 — JORT n° 62 du 2 août 1996, p. 1638-1639 — `https://www.pist.tn/jort/1996/1996F/Jo06296.pdf` | La loi devient « relative aux participations, entreprises et établissements publics ». Art. 8 nouveau : sont entreprises publiques « les établissements publics à caractère non administratif **et dont la liste est fixée par décret** », les sociétés à capital entièrement d'État, les sociétés détenues à plus de 50 %. La liste : décret n° 97-564 du 31 mars 1997, puis décret n° 2004-2265 du 27 septembre 2004 (intitulés seuls) | Délibérations du conseil soumises à l'**approbation de la tutelle** (art. 10 nouveau) ; conseil limité à 12 membres ; il arrête budgets et contrats-programmes ; la tutelle, désignée par décret, approuve budgets prévisionnels et contrats-programmes et en suit l'exécution (article annoncé « 22 (bis) » et imprimé « 12 (bis) » dans la couche texte : numéro à relire à l'image) ; recrutement par concours (art. 11 bis) ; organigramme par décret (art. 10 bis) Les établissements publics **non** considérés comme entreprises publiques reçoivent un régime propre (art. 33-7 et suivants) : directeur général nommé par décret, conseil d'entreprise consultatif à la place du conseil d'administration, marchés et loi des cadres par décret | couche texte, art. 1 à 3 ; art. 33-8 à 33-12 lus à l'image (p. 1639) ; art. 33-7 non lu |
| 1999 | Loi n° 99-38 du 3 mai 1999 — JORT n° 37 du 7 mai 1999, p. 684 — `https://www.pist.tn/jort/1999/1999F/Jo03799.pdf` | — | Titre VI, liquidation à l'amiable des entreprises et établissements publics : priorité aux dettes nées après l'approbation du programme de liquidation, suspension des poursuites, durée de trois ans au plus | lu à l'image, entier |
| 2001 | Loi n° 2001-33 du 29 mars 2001 — JORT n° 26 du 30 mars 2001, p. 712 — `https://www.pist.tn/jort/2001/2001F/Jo0262001.pdf` | **Abroge l'article 9** : les banques et sociétés d'assurance détenues entre 34 et 50 % sortent du périmètre | — | lu à l'image, entier |
| 2002 | Décret n° 2002-2197 du 7 octobre 2002 (modalités d'exercice de la tutelle, approbation des actes de gestion, représentation des participants publics), JORT n° 83, p. 2364-2367 ; modifié par le décret gouvernemental n° 2016-510 du 13 avril 2016 | — | Texte d'application que l'annexe 9 cite comme cadre (LF 2021, p. 6), avec les décrets n° 2002-2131, 2002-2130, 96-271, 2011-2856, 2013-5093 et 2005-910 | intitulé seul |
| 2006 | Loi n° 2006-36 du 12 juin 2006 — JORT n° 47 du 13 juin 2006, p. 1533 — `https://www.pist.tn/jort/2006/2006F/Jo0472006.pdf` | Art. 22 ter : les entreprises publiques « qui opèrent dans un environnement compétitif ou qui ont fait l'objet d'un programme de restructuration » peuvent être exclues des articles 10, 10 bis, 11, 11 bis, 15, 18 à 22 bis ; liste par décret (décrets n° 2006-1555, 2009-2965, 2013-4953 ; décret gouvernemental n° 2020-1061 : intitulés seuls) | Allègement de la tutelle et du contrôle d'État pour les entreprises concurrentielles | couche texte, entier |
| 2015-2019 | Stratégie de réforme : conseil ministériel du 24 novembre 2015 ; Livre blanc de mars 2018 ; conseil ministériel du 19 juin 2018 (19 objectifs, 58 mesures) ; décret gouvernemental n° 2018-618 du 26 juillet 2018 (unité de gestion par objectifs à la Présidence du gouvernement) ; arrêté du Chef du gouvernement du 25 février 2019 (comité de pilotage) | Quatre classes annoncées — secteur concurrentiel, stratégique, service public, monopole — dont « la liste définitive […] n'a pas été arrêtée » (annexe 9, LF 2021, p. 8) | Contrats de performance (Office des céréales, RNTA, STIR) et contrats-programmes des trois banques publiques, évalués dans l'annexe 9 de la LF 2020 (p. 136-158) | annexe 9 LF 2020, p. 17, couche texte ; décret n° 2018-618 : intitulé (arabe) seul |
| 2019 | Loi organique du budget n° 2019-15 du 13 février 2019 : art. 45 (la loi de finances fixe le plafond des garanties et celui des prêts du Trésor) ; art. 46 (rapports annexés, dont celui sur les entreprises publiques) | **Rupture d'information** : avant la LF 2020, aucun rapport annuel annexé | — | cité par les annexes ; loi non lue au JORT |
| 2020-2023 | Relèvement du plafond des garanties : 3 000 MD (2016-2018), 4 790 (2019), 7 000 (2020-2022), 8 000 (2023-2024) | — | Garantie étendue au financement de l'exploitation (importations de produits de base, rééchelonnements) | § 1.2 |

**Ce que l'État paie, dans les lois de finances** — articles repérés par leur seul intitulé dans
`jort_cache`, à lire en second passage ; ils jalonnent le versant budgétaire que les lois
ci-dessus ne disent pas : loi n° 80-88 (LF 1981, « assainissement… », p. 3282-3283) ; loi
n° 83-113 (LF 1984, création d'un fonds spécial du Trésor au ministère du Plan, p. 3384) ; loi
n° 85-109 (LF 1986, création d'un fonds spécial et suppression du « fonds de consolidat… »,
p. 1741) ; **loi n° 89-115 (LF 1990, « fonds de restructuration du capital des entreprises
publiques », p. 2153)**, modifié par la loi n° 2002-101 (LF 2003, art. 13) ; loi n° 91-98
(LF 1992, « participation de l'État au capital des entreprises publiques », p. 2090) ; loi
n° 96-113 (LF 1997, art. 17, « garantie de l'État des dettes de l'office des céréales et de
l'office national de l'huile ») ; loi n° 98-111 (LF 1999, « garantie ou prise en charge par
l'État des créances bancaires à la charge des établissements… », p. 2502-2503) ; lois de
finances pour 2007 à 2010, prélèvement sur le « compte d'emploi des frais de contrôle
financier, des jetons de présence et tantièmes revenant à l'État » ; loi de finances pour 2024
(loi n° 2023-13 du 11 décembre 2023), assainissement de la situation financière de la Société
générale d'entreprises, de matériel et de travaux (intitulé arabe).

**Dates d'effet.** Lois de 1969, 1985, 1987 et 1989 : aucune clause d'effet dans les pages lues ;
règle d'avant 1993, un jour franc après la publication — loi n° 87-47 : 14 août 1987 + un jour
franc = **16 août 1987** ; loi n° 89-9 : 7 février 1989 + un jour franc = **9 février 1989** ; loi
n° 85-72 et loi n° 69-50 : fascicules multi-datés (26-30 juillet 1985 ; 25-29 juillet-1er août
1969), date **en fourchette**, à fixer selon la convention du dépôt. Loi n° 94-102 : **1er janvier
1995** pour l'article 9 nouveau (dit par le texte). Lois de 1996, 1999, 2001 et 2006 : règle de
1993 (cinq jours après le dépôt du fascicule au gouvernorat de Tunis) ; la date de dépôt n'a pas
été relevée — dates d'effet **non calculées**.

**Proposition de plan des ruptures** (pour l'architecte) : 1969 et 1985, la tutelle et le seuil de
34 % ; **1987-1989, la cession autorisée et la définition à 50 %** (la loi de 1989 abroge celles
de 1985 et de 1987 et les refond) ; 1994-2001, les outils de la
privatisation, les banques dedans puis dehors ; 1996, la tutelle resserrée et la liste par
décret ; 2006, les entreprises concurrentielles allégées ; **1998-2006, les grandes cessions**
(cimenteries, seconde licence, Tunisie Télécom : à documenter opération par opération) ; **après
2011, plus de cessions et la relation inversée** — transferts, garanties d'exploitation et
arriérés croisés ; 2019, l'obligation de rapport.

---

## 3. Références candidates

### Déjà présentes (recherche par motif dans `precis/fr/references.json` et les `references.json` des volumes)

| Clé existante | Document | Où |
|---|---|---|
| `minfin-ep-2020` | annexe 9, LF 2020 | `precis/fr/references.json` |
| `minfin-ep` | annexe 9, LF 2021 | idem |
| `minfin-ep-2022`, `minfin-ep-2023`, `minfin-ep-2024`, `minfin-ep-2025` | annexe 9, LF 2022 à LF 2025 | idem |
| `wb-tunisia-per-2020` | Banque mondiale, revue des dépenses publiques, rapport de synthèse | `remunerations_publiques/references.json` |
| `imf-tunisia-art4-2020` | FMI, Country Report No. 21/44 — **titre à corriger** : l'entrée dit « 2020 Article IV Consultation », la page de garde du document dit « 2021 Article IV Consultation », février 2021 | `remunerations_publiques/references.json` |
| `loi89-9` | loi n° 89-9 du 1er février 1989 | `precis/fr/references.json` |
| `loi85-78` | statut général des agents des offices, EPIC et sociétés (cité par les rémunérations ; hors sujet ici) | idem |
| `decret97-564`, `decret2004-2265` | listes des EPNA considérés comme entreprises publiques | `caisses/references.json` |
| `decret-95-2487` | liste d'entreprises publiques (rémunération des chefs d'entreprise) | `remunerations_publiques/references.json` |

Non trouvées (même recherche) : annexes 7 et 8 ; lois n° 69-50, 85-72, 87-47, 93-124, 94-102,
96-74, 99-38, 2001-33, 2006-36 ; décret n° 2002-2197 ; Livre blanc ; privatisation ; ITCEQ. Les
entrées `fmi-2016-cr16138` et `fmi-2014-cr14362` de `compensation/references.json` sont d'autres
rapports du FMI. `legislation.bib` n'a pas été parcouru.

### À créer (format du dépôt : `id`, et `note` commençant par `citation-key:`)

```json
[
 {
  "id": "minfin-transferts-2020",
  "type": "report",
  "title": "Rapport sur les transferts et les garanties au profit des entreprises publiques et des établissements publics non administratifs",
  "author": [
   {
    "literal": "Ministère des Finances"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2019,
     10
    ]
   ]
  },
  "genre": "Annexe n° 8 au projet de loi de finances pour 2020",
  "URL": "http://www.gbo.tn/sites/default/files/2021-02/Annexe_8_LF2020-Transferts_et_Garantie.pdf",
  "note": "citation-key: minfin-transferts-2020"
 },
 {
  "id": "minfin-transferts-2021",
  "type": "report",
  "title": "Rapport sur les transferts et les garanties au profit des entreprises publiques et des établissements publics non administratifs",
  "author": [
   {
    "literal": "Ministère de l'Économie, des Finances et de l'Appui à l'investissement"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2020
    ]
   ]
  },
  "genre": "Annexe n° 8 au projet de loi de finances pour 2021 (traduction française ; la version arabe fait foi)",
  "URL": "http://www.gbo.tn/sites/default/files/2021-04/Annexe 8 LF2021 Transferts Garantie.pdf",
  "note": "citation-key: minfin-transferts-2021"
 },
 {
  "id": "minfin-transferts-2022",
  "type": "report",
  "title": "التقرير حول التحويلات والضمانات لفائدة المنشآت العمومية والمؤسسات العمومية غير الإدارية",
  "author": [
   {
    "literal": "Ministère des Finances"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2021
    ]
   ]
  },
  "genre": "Annexe n° 8 à la loi de finances pour 2022",
  "language": "ar",
  "URL": "http://www.gbo.tn/sites/default/files/2022-01/ANNEXE_08 Transferts et garanties.pdf",
  "note": "citation-key: minfin-transferts-2022"
 },
 {
  "id": "minfin-transferts-2023",
  "type": "report",
  "title": "التقرير حول التحويلات والضمانات لفائدة المنشآت العمومية والمؤسسات العمومية غير الإدارية",
  "author": [
   {
    "literal": "Ministère des Finances"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2022
    ]
   ]
  },
  "genre": "Annexe n° 8 au projet de loi de finances pour 2023",
  "language": "ar",
  "URL": "https://www.finances.gov.tn/sites/default/files/2023-01/1.pdf",
  "note": "citation-key: minfin-transferts-2023"
 },
 {
  "id": "minfin-transferts-2024",
  "type": "report",
  "title": "التقرير حول التحويلات والضمانات",
  "author": [
   {
    "literal": "Ministère des Finances"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2023
    ]
   ]
  },
  "genre": "Annexe n° 8 au projet de loi de finances pour 2024",
  "language": "ar",
  "URL": "http://www.gbo.tn/sites/default/files/2024-01/التقرير حول التحويلات والضمانات ملحق عدد _08.pdf",
  "note": "citation-key: minfin-transferts-2024"
 },
 {
  "id": "minfin-transferts-2025",
  "type": "report",
  "title": "التقرير حول التحويلات والضمانات",
  "author": [
   {
    "literal": "Ministère des Finances"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2024
    ]
   ]
  },
  "genre": "Annexe n° 8 au projet de loi de finances pour 2025",
  "language": "ar",
  "URL": "http://www.gbo.tn/sites/default/files/2025-03/ملحق 8 تحويلات وضمانات الدولة لفائدة المنشآت.pdf",
  "note": "citation-key: minfin-transferts-2025"
 },
 {
  "id": "minfin-dette-2022",
  "type": "report",
  "title": "التقرير حول الدين العمومي",
  "author": [
   {
    "literal": "Ministère des Finances"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2021
    ]
   ]
  },
  "genre": "Annexe n° 7 à la loi de finances pour 2022",
  "language": "ar",
  "URL": "http://www.gbo.tn/sites/default/files/2022-01/ANNEXE_07 Dette publique.pdf",
  "note": "citation-key: minfin-dette-2022"
 },
 {
  "id": "minfin-dette-2025",
  "type": "report",
  "title": "التقرير حول الدين العمومي",
  "author": [
   {
    "literal": "Ministère des Finances, Direction générale de la gestion de la dette et de la coopération financière"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2024
    ]
   ]
  },
  "genre": "Annexe n° 7 au projet de loi de finances pour 2025",
  "language": "ar",
  "URL": "http://www.gbo.tn/sites/default/files/2025-03/ملحق 7 الدين العمومي.pdf",
  "note": "citation-key: minfin-dette-2025"
 },
 {
  "id": "dgpv-recettes-annuelles-1987-2009",
  "type": "dataset",
  "title": "إيرادات عمليات التخصيص وإعادة هيكلة المنشآت ذات المساهمات العمومية سنويا من 1987 إلى 2009",
  "author": [
   {
    "literal": "Premier ministère, Direction générale de la privatisation"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2010,
     2,
     17
    ]
   ]
  },
  "language": "ar",
  "URL": "http://web.archive.org/web/20131218014417/http://www.privatisation.gov.tn/www/ar/download/recettes%20annuelles%20ar.xls",
  "note": "citation-key: dgpv-recettes-annuelles-1987-2009"
 },
 {
  "id": "dgpv-bilan-global-2009",
  "type": "webpage",
  "title": "Bilan global des privatisations — résultats enregistrés du 31/12/1987 au 31/01/2009",
  "author": [
   {
    "literal": "Présidence du gouvernement, Direction générale de la privatisation"
   }
  ],
  "accessed": {
   "date-parts": [
    [
     2026,
     10,
     11
    ]
   ]
  },
  "URL": "https://privatisation.pm.gov.tn/fr/bilan-global-des-privatisations",
  "note": "citation-key: dgpv-bilan-global-2009"
 },
 {
  "id": "pm-livre-blanc-ep-2018",
  "type": "report",
  "title": "Livre blanc — Rapport de synthèse sur la réforme de la gouvernance des entreprises publiques en Tunisie",
  "author": [
   {
    "literal": "Présidence du gouvernement"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2018,
     3
    ]
   ]
  },
  "URL": "http://web.archive.org/web/20180403125015/http://www.leaders.com.tn:80/uploads/FCK_files/Livre%20Blanc%20(Rapport%20de%20synth%C3%A8se%20sur%20la%20r%C3%A9forme%20de%20la%20gouvernance%20et%20des%20entreprises%20publiques%20en%20Tunisie%20).pdf",
  "note": "citation-key: pm-livre-blanc-ep-2018\nTitre et date à relever sur la page de garde ; copie hébergée par un site de presse."
 },
 {
  "id": "itceq-privatisation-2010",
  "type": "report",
  "title": "Privatization and Private Sector Development — rapport d'étape (MEDPRO, Work Package 5)",
  "author": [
   {
    "literal": "Institut tunisien de la compétitivité et des études quantitatives"
   }
  ],
  "issued": {
   "date-parts": [
    [
     2010,
     12
    ]
   ]
  },
  "URL": "http://web.archive.org/web/20250621113107/http://www.itceq.tn/files/investissement-et-croissance/rapport-privatisation.pdf",
  "note": "citation-key: itceq-privatisation-2010"
 }
]
```

Textes du JORT à créer (clé au format du dépôt, fascicule, pages ; URL au § 2) : `loi69-50`
(n° 28 de 1969, p. 911-912) ; `loi85-72` (n° 56 de 1985, p. 958-961) ; `loi87-47` (n° 56 de
1987, p. 958-959) ; `loi93-124` (n° 99 de 1993, p. 2185) ; `loi94-102` (n° 62 de 1994,
p. 1290-1291) ; `loi96-74` (n° 62 de 1996, p. 1638-1639) ; `loi99-38` (n° 37 de 1999, p. 684) ;
`loi2001-33` (n° 26 de 2001, p. 712) ; `loi2006-36` (n° 47 de 2006, p. 1533) ;
`decret2002-2197` (n° 83 de 2002, p. 2364-2367). La loi n° 89-9 existe déjà (`loi89-9`) :
pages 203-205.

---

## 4. Notions à glossaire

Déjà au glossaire (`precis/glossaire.yml`) : « Établissement public à caractère non
administratif », « Établissement public à caractère industriel et commercial »,
« Contrat-programme » (id `contrat-programme`), et des entrées par entreprise (ETAP, STIR, STEG).
À vérifier ou créer :

| Terme (FR) | AR | Définition légale, dans les mots du texte | Date et source |
|---|---|---|---|
| Entreprise publique | منشأة عمومية | « Sont considérés des entreprises publiques […] : les établissements publics à caractère non administratif et dont la liste est fixée par décret ; les sociétés dont le capital est entièrement détenu par l'État ; les sociétés dont le capital est détenu par l'État, les collectivités locales, les établissements publics et les sociétés dont le capital est détenu entièrement par l'État à plus de 50 % chacun individuellement ou conjointement » | Loi n° 89-9, art. 8, rédaction de la loi n° 96-74 du 29 juillet 1996. Rédaction de 1989 : « les établissements publics n'ayant pas un caractère administratif », sans liste. De 1985 à 1989, seuil de 34 % (loi n° 85-72, art. 1er) |
| Participation publique | مساهمة عمومية | « Sont considérées participations publiques, les participations de l'État, des collectivités locales, des établissements publics et des sociétés dont le capital est entièrement détenu par l'État » | Loi n° 89-9, art. 8, second alinéa (1989, repris en 1996) |
| Participation directe, participation indirecte | مساهمة مباشرة، غير مباشرة | Directe : celle de l'État « en son nom » ; indirecte : celle des collectivités locales, des EPNA de la liste et des sociétés à capital entièrement d'État | Annexe 9, LF 2021, p. 7-8 (définition administrative) ; loi n° 94-102, art. 9 nouveau, pour 1995-2001 |
| Établissement public à caractère non administratif considéré comme entreprise publique | مؤسسة عمومية لا تكتسي صبغة إدارية تعتبر منشأة عمومية | EPNA inscrit sur la liste fixée par décret ; 46 sur 110 entreprises publiques en 2020 | Loi n° 96-74 ; décrets n° 97-564 et n° 2004-2265 (intitulés seuls) ; annexe 9, LF 2021, p. 7 |
| Entreprise-mère, filiale | — | Notions de 1985 : société ou EPIC détenu à 34 % au moins ; filiale détenue à plus de 50 % par l'État, les collectivités ou les entreprises-mères | Loi n° 85-72, art. 1er — notion historique |
| Contrat-programme | عقد برنامج | Arrêté par le conseil d'administration, approuvé par la tutelle qui en suit l'exécution | Loi n° 85-72, art. 11 ; loi n° 89-9, art. 10 ; loi n° 96-74, art. 10 nouveau et article sur la tutelle (22 bis, numéro à relire) |
| Contrat de performance | عقد أداء / عقد تحسين الأداء | Contrats « d'amélioration de performance » signés avec l'Office des céréales, la RNTA et la STIR | Annexe 9, LF 2020, p. 142-158 ; pas de définition légale relevée |
| Autorité de tutelle | سلطة الإشراف | Désignée par décret ; approuve budgets, contrats-programmes et délibérations | Loi n° 96-74, article sur la tutelle (22 bis, numéro à relire) ; décret n° 2005-910 (cité par l'annexe 9, non lu) |
| Contrôleur d'État | مراقب الدولة | Fonctionnaire placé auprès de l'entreprise publique pour une « mission générale de contrôle » | Loi n° 89-9, art. 15-17 (contrôleur financier en 1985) |
| Garantie de l'État | ضمان الدولة | « l'État se substitue au débiteur principal […] dans tous ses engagements financiers et contractuels envers le bailleur » ; garantie extérieure activée automatiquement, garantie intérieure après épuisement des poursuites contre le débiteur (traduction de la note) | Annexe 7, LF 2025, p. 61 ; plafond : loi organique n° 2019-15, art. 45 |
| Dette garantie (encours) | حجم الدين المضمون | Encours des prêts des entreprises et établissements publics garantis par l'État, extérieur et intérieur | Annexe 7 |
| Prêt rétrocédé | قرض معاد إقراضه | Prêt extérieur contracté par l'État et reprêté à l'entreprise ; rubrique « prêts du Trésor et prêts rétrocédés » | Annexe 9, tableaux de composition des transferts ; pas de définition dans les pages lues |
| Subvention d'exploitation et d'équilibre | منحة استغلال وتوازن | Rubrique des transferts | Annexe 9 |
| Action spécifique | سهم خصوصي | Action ordinaire de l'État transformée par décret avant la perte du caractère public ; droits de nomination, d'agrément des franchissements de seuil, d'opposition | Loi n° 94-102, art. 33-2 et 33-3 |
| Restructuration (des entreprises à participations publiques) | إعادة هيكلة | Cession ou échange d'actions, fusion, absorption, scission, cession d'éléments d'actif | Loi n° 87-47, art. 3 ; loi n° 89-9, art. 24 |
| Commission d'assainissement et de restructuration des entreprises à participations publiques (CAREPP) | لجنة تطهير وإعادة هيكلة المنشآت ذات المساهمات العمومية | Donne son avis sur les opérations de restructuration ; décisions arrêtées par le Premier ministre | Loi n° 89-9, art. 24-27 |
| Privatisation | تخصيص | Terme de la Direction générale de la privatisation (الإدارة العامة للتخصيص) ; la loi dit « restructuration » et « cession » | Classeur de 2010 ; à faire trancher par le terminologue |
| Document d'orientation | الوثيقة التوجيهية | Document transmis par l'entreprise au ministère, employé à défaut d'états financiers | Annexe 9, LF 2023 à LF 2025 — traduction à valider |

---

## 5. Ce qui n'est pas établi

### 5.1 Éditions manquantes des rapports du ministère (documents, hors registre du JORT)

- **Annexes n° 8 et n° 9 du projet de loi de finances pour 2026** : non trouvées. Essayé le
  11/10/2026 : page « Loi de Finance et rapports annexes » de gbo.tn (587 fichiers listés ; le
  dernier dépôt d'annexes est de mars 2025, pour la LF 2025 ; un dépôt de décembre 2025 ne porte
  qu'un rapport annuel de performance) ; une recherche web sur l'intitulé arabe. Non essayé :
  l'arborescence « documents » de finances.gov.tn, l'Assemblée des représentants du peuple.
- **Avant la LF 2020** : la série n'existe pas sous cette forme (obligation née de la loi
  organique de 2019). Constat que la fiche `sources/minfin-entreprises-publiques-caisses.md`
  laissait ouvert.
- **Annexe 9 de la LF 2021 en arabe** (la version qui fait foi) : adresse vue sur gbo.tn, non
  téléchargée.

### 5.2 Séries longues non établies

- **Transferts aux entreprises publiques avant 2016** : rien dans les annexes. Pistes non
  ouvertes : rapports annuels de la BCT (`sources/bct-archives.md`), lois de règlement et
  rapports de la Cour des comptes sur la clôture du budget (rubrique 18, téléchargée), plans de
  développement. Seul repère : ratios du Livre blanc pour 2013 et 2014 (famille B).
- **Encours de dette garantie avant 2016** : idem ; pistes : rapports annuels de la BCT, rapport
  de la Cour des comptes sur la dette publique extérieure (2018, rubrique 90, téléchargé, non
  ouvert), annexe 7 de la LF 2021 (téléchargée, non dépouillée).
- **Dette rétrocédée** : seule la ligne de flux « prêts du Trésor et prêts rétrocédés » de
  l'annexe 9 est relevée (§ 1.4) ; l'encours n'est pas établi. L'annexe 7 en parle — le mot
  « إقراض » apparaît aux p. PDF 19, 22-23, 49-57 de l'édition LF 2025 et 16-20, 35, 48-50 de
  l'édition LF 2022 — pages **non lues**.
- **Recettes de cession après 2009** : aucune série ; à chercher dans les lois de règlement
  (recettes non fiscales, « revenus des participations » et « recettes de privatisation ») et
  dans les rapports sur le budget de l'État.
- **Effectif total des entreprises publiques** : non publié dans les annexes ; à chercher à
  l'INS (emploi par secteur institutionnel) et dans les rapports de l'Unité de suivi (§ 5.3).
- **Nombre d'entreprises publiques avant 2019** : « environ 190 » au milieu des années 1980 et
  102 en 2018 selon le Livre blanc ; non recoupé. Les listes par décret (1997, 2004) le
  donneraient pour les EPNA.
- **Valeur ajoutée, part dans le PIB** : seuls existent « 9,5 % du PIB en 2014 contre 13 % en
  2010 » (Livre blanc) et « between 9 and 10 percent of GDP » (Banque mondiale, citant le
  gouvernement), sans méthode ni base.

### 5.3 Document introuvable

- **« Rapport annuel sur les résultats des établissements publics durant la période 2010-2014 »**,
  Unité de suivi du système de productivité des établissements et entreprises publics, Présidence
  du gouvernement — source des graphiques du Livre blanc ; un billet de la Banque mondiale
  signale une édition 2010-2012 « publiée sur le site du chef du gouvernement » et les résultats
  de recherche une édition 2010-2016. Essayé : `pm.gov.tn/pm/entreprise/listetablissement.php`
  (redirige vers le nouveau portail, sans le rapport) ; index des archives du web pour
  `pm.gov.tn/pm/entreprise*` et `pm.gov.tn/pm/upload/fck/File/*` (aucun fichier de ce nom parmi
  les captures listées). Non essayé : `pm.gov.tn/pm/upload/` sous d'autres préfixes, le dépôt de
  la Banque mondiale, une recherche par titre arabe exact. **C'est la pièce qui donnerait 2010-2016.**

### 5.4 Fiches de recherche proposées pour `docs/recherches.yml`

```yaml
- id: r-loi89-9-modificatifs-apres-2006
  objet: texte modifiant ou remplaçant la loi n° 89-9 du 1er février 1989 (participations, entreprises et établissements publics) postérieur à la loi n° 2006-36 du 12 juin 2006, ou loi nouvelle sur la gouvernance des participations et entreprises publiques (projet évoqué par le FMI en 2021)
  ou: [docs/notes/entreprises-publiques-2026-10-11.md]
  requetes:
    titres_like: ['%entreprises publiques%', '%participations publiques%', '%etablissements publics%', '%89-9 %']
    titres_fts: ['gouvernance AND (entreprises OR participations) AND publi*']
    iort_ar: [المنشآت العمومية, المنشات العمومية, المساهمات العمومية, المساهمات والمنشآت, حوكمة المنشآت, 9 لسنة 1989]
    depuis: 2006-07-01
  passes:
  - date: 2026-10-11
    role: documentaliste
    sources: [jort_cache]
    couverture: 'jort_cache jusqu''au 2 octobre 2026, titres seuls (LIKE français sans accents, LIKE arabe, FTS), lois et décrets-lois postérieurs au 1er juillet 2006 : aucune loi modifiant la loi n° 89-9 ; ne ressortent que des articles de lois de finances, la loi n° 2007-33 (audiovisuel), le décret-loi n° 2020-7 et les décrets d''application de l''article 22 ter (2006-1555, 2009-2965, 2013-4953, 2020-1061). Ni le corpus local en plein texte, ni iort, ni pist n''ont été parcourus ; les fascicules inconnus de la base (outillage-sources, § 1 f) non plus.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - rejouer en plein texte sur le corpus local depuis 2011 (« 89-9 », « 9 لسنة 1989 »)

- id: r-epna-liste-modificatifs-apres-2007
  objet: décret modifiant ou remplaçant, après le décret n° 2007-2560 du 23 octobre 2007, la liste des établissements publics à caractère non administratif considérés comme entreprises publiques (décret n° 2004-2265 du 27 septembre 2004)
  ou: [docs/notes/entreprises-publiques-2026-10-11.md]
  requetes:
    titres_like: ['%liste des etablissements publics a caractere non administratif%', '%consideres comme entreprises publiques%', '%2004-2265%', '%97-564%']
    iort_ar: [قائمة المؤسسات العمومية التي لا تكتسي صبغة إدارية, 2265 لسنة 2004]
    depuis: 2007-10-24
  passes:
  - date: 2026-10-11
    role: documentaliste
    sources: [jort_cache]
    couverture: 'jort_cache jusqu''au 2 octobre 2026, titres seuls : chaîne retrouvée — décrets n° 97-564, 98-752, 99-2378, 2002-2199, 2004-2265, 2006-2579, 2007-1865, 2007-2560 ; rien après 2007. Un seul terme arabe essayé, alors que 40 à 80 % des notices de 2015 à 2019 n''ont qu''un intitulé arabe : silence non concluant. Aucun des décrets n''a été lu.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - prendre l'intitulé arabe exact du décret n° 2004-2265 au miroir iort et le rejouer
  - lire les décrets n° 97-564 et n° 2004-2265 pour compter les EPNA à chaque date

- id: r-garantie-etat-plafond-2020-lfr
  objet: article de la loi de finances rectificative pour 2020 fixant le plafond des garanties de l'État (7 000 ou 7 500 millions de dinars selon les éditions de l'annexe n° 8)
  ou: [docs/notes/entreprises-publiques-2026-10-11.md]
  requetes:
    titres_like: ['%garantie de l''Etat%']
    iort_ar: [ضمان الدولة]
    depuis: 2020-01-01
  passes:
  - date: 2026-10-11
    role: documentaliste
    sources: [jort_cache]
    couverture: 'jort_cache, titres : 147 notices portent « garantie de l''Etat » ou « ضمان الدولة » toutes années confondues ; la suite annuelle des articles de loi de finances est indexée de 1961 à 1994, puis l''index cesse de détailler les articles. La loi de finances rectificative pour 2020 n''a pas été ouverte.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - ouvrir la loi de finances rectificative pour 2020 dans le corpus local et lire l'article sur le plafond
```

---

## 6. Séries à verser dans `tunisia-data`

| Série | Profondeur | Source, pages | État |
|---|---|---|---|
| `ep_transferts_budget_total` — transferts aux EP et EPNA, par secteur, nature, source de financement | 2016 (ancien périmètre) ; 2017-2023 réalisé ; 2019-2024 loi de finances | annexe 8 : LF 2020 p. [5]-[6] ; LF 2021 p. [3]-[4] ; LF 2022 à LF 2025 p. 7-8 | transcrit ici (§ 1.1) ; à coder avec colonnes `statut`, `edition`, `perimetre`, à l'image de `extract_cnrps_tutelle.py` |
| `ep_transferts_par_etablissement` | 2016-2023 | annexes de l'annexe 8 (LF 2020 : p. 62-123 ; éditions arabes : seconde moitié du rapport) | **à faire** ; c'est elle qui permet de retirer compensation et caisses |
| `garanties_etat_plafond_flux` | 2016-juin 2024 | annexe 7 : LF 2022 p. 56 ; LF 2025 p. 62 ; annexe 8, résumés | transcrit (§ 1.2) |
| `garanties_etat_plafond_legal` | 1961-2026 | article « octroi de la garantie de l'État » de chaque loi de finances (`jort_cache`, intitulés) | **à faire** : lire les montants |
| `dette_garantie_encours` | 2016-juin 2024 | annexe 7 : LF 2022 p. 58 ; LF 2025 p. 65 | transcrit (§ 1.2) ; annexes 7 LF 2021 et LF 2024 téléchargées, à dépouiller pour recoupement |
| `ep_resultats_agreges` | exercices 2017-2022, deux par édition | annexe 9 : LF 2021 p. 20 ; LF 2022 p. 14 ; LF 2023 p. 21 ; LF 2024 p. 23 ; LF 2025 p. 13 | transcrit (§ 1.3) |
| `ep_dix_premieres` — sept classements par exercice | 2017-2022 | annexe 9 : LF 2021 p. 23-28 ; LF 2022 p. 15-19 ; LF 2023 p. 24-27 ; LF 2024 p. 26-29 ; LF 2025 p. 17-21 | résultats nets et charges de personnel lus ; produits et charges d'exploitation lus en partie |
| `ep_versements_transferts_echantillon` — totaux, composition, par entreprise | 2017-2022 | annexe 9 : LF 2021 tableaux 26-31, p. 143-150 ; LF 2022 tableaux 33-38, p. 100-106 ; LF 2023 tableaux 35-40, p. 195-200 ; LF 2024 tableaux 40-45, p. 149-154 | totaux et composition transcrits (§ 1.4) ; tableaux par entreprise lus, transcrits pour treize entreprises (§ 1.6) |
| `ep_dettes_creances_croisees` | 2021-2023 ; par entreprise 2023 | annexe 9 LF 2025, p. 115-123 | transcrit (§ 1.4, § 1.6) |
| `ep_dividendes_etat` | exercices 2017-2023 | annexe 9 : LF 2021 p. 150 ; LF 2022 à LF 2024 (paragraphe « عائدات مساهمات الدولة ») ; LF 2025 p. 125-126 | transcrit (§ 1.5) ; 2019 et 2020 en couche texte seulement |
| `ep_fiches_par_entreprise` — une vingtaine d'indicateurs par entreprise | 2016-2023 | annexe 9, tableaux par tutelle | **à faire** : éditions arabes tournées d'un quart de tour (rendu à 170 dpi, rotation) ; éditions françaises en couche texte |
| `privatisation_recettes_annuelles` | 1987-2009 | classeurs de la Direction générale de la privatisation (éd. 2006 et 2010) ; page « par période » | transcrit (§ 1.8) ; feuilles par mode de cession (1994-2003) et par secteur (1994-1998) non transcrites |

---

## 7. Frontières constatées avec les quatre volumes

- **Compensation.** La frontière passe **au milieu de la série centrale** : le secteur
  « économique » de l'annexe 8 contient la subvention des produits de base, des carburants, de
  l'électricité et du transport, et les trois premiers bénéficiaires de l'échantillon de
  l'annexe 9 sont la STIR, l'Office des céréales et la STEG (10,9 milliards sur 14,6 en 2022
  provisoire ; « trois entreprises représentent plus de 75 % du total des transferts » en
  2017-2019, LF 2021, p. 149). Ce texte-ci ne doit pas refaire la dépense de compensation. Vérifié dans le
  volume : il traite les arriérés comme une **réserve de lecture** — série « tenue en base
  caisse : les arriérés et les régularisations entre l'État et les entreprises déplacent la
  charge d'une année à l'autre » (`_depense.qmd`), impayés de 2016 (`_carburants.qmd`), décrets
  de compensation de créances État-ETAP et État-Office des céréales (`docs/notes/compensation.md`)
  — sans donner l'**encours**. C'est ce que ce texte apporte : subventions non réglées de
  5 934,8 MD fin 2021, 7 680,5 fin 2022 et 6 956,8 fin 2023 selon les entreprises (dont 3 151,6
  pour la STEG, non confirmés par le ministère ; LF 2025, p. 121), règlement de 4 100 MD annoncé
  en 2020, résultat net et dette des entreprises qui portent la compensation, garantie de l'État
  sur leurs achats (1 215,2 MD en 2023). Proposition : renvoi croisé dans les deux sens, et une
  figure qui superpose subvention versée et créance restante par entreprise.
- **Caisses.** CNSS, CNRPS et CNAM sont dans le recensement (111 à 115 entreprises), dans
  l'échantillon des flux (elles y pèsent : CNRPS première débitrice de l'État fin 2023, 2 968,8
  MD) et dans le secteur social de l'annexe 8 ; elles sont **hors** des agrégats de résultats.
  **Concordance constatée** : les transferts à la CNRPS de l'annexe 9 égalent ceux de l'annexe 8
  pour 2020-2022 (970,6, 762,3, 579,5 contre 970,628, 762,257, 579,516,
  `minfin-transferts-cnrps.md`), mais pas pour 2017-2019 (500, 200, 450 contre 660,6, 900,1,
  740,8) : les deux annexes ne comptaient pas alors les mêmes versements. Et la « Caisse
  nationale de solidarité sociale » de la traduction française de la LF 2021 est la CNSS
  (versement de 214 MD en 2018 dans les deux éditions). Le
  volume « Caisses » exploite déjà ces rapports pour leurs comptes (`minfin-ep-cnrps-finances.md`,
  `minfin-transferts-cnrps.md`) : ici, n'en garder que le poids dans les totaux, et dire à chaque
  total si elles y sont.
- **Rémunérations publiques.** Sections « Repères budgétaires » relues. Celle du régime
  conventionnel (`_regime_conventionnel.qmd`, § sec-conventionnel-budget) ne porte **aucun
  chiffre du ministère** : elle cite le rapport [@minfin-ep], laisse en TODO « construire les
  séries pluriannuelles (effectifs, masse salariale par entreprise, transferts/PIB) », et donne
  une seule valeur, « environ 8,9 % du PIB en 2013 et 7,5 % en 2014 », attribuée à la Banque
  mondiale [@wb-tunisia-per-2020]. **Attribution à vérifier** : ces deux ratios sont, mot pour
  mot, dans le Livre blanc de 2018 (p. PDF 20), et la couche texte du rapport de synthèse de la
  Banque mondiale ne porte ni « 8.9 percent » ni « 7.5 percent ». Celle du marché contrôlé
  (`_regime_marche_controle.qmd`, § sec-marche-controle-budget) ne donne que le capital et la
  part publique des trois banques, et laisse en TODO les effectifs du secteur financier public.
  Pas de doublon donc : le § 1.3 (charges de personnel agrégées, 2017-2022), le § 1.7 (dix
  premières) et le § 1.6 (effectifs de STEG, STIR, Tunisair, Transtu, SNCFT, SONEDE) **lèvent le
  TODO** du régime conventionnel ; ce texte-ci garde la masse et les effectifs, les
  rémunérations publiques gardent les grilles et les augmentations.
- **Transport (note du 11 octobre 2026).** Elle établit la subvention par société et les tarifs.
  Ici : les comptes — Transtu, résultat net de −167 à −230 MD chaque année de 2017 à 2022, dettes
  de 969 MD en 2018 dont 197 envers les caisses sociales, troisième débitrice de l'État fin 2023
  (1 509,3 MD) ; SNCFT, −82 à −200 MD, dettes de 1 096 MD en 2018 dont 824,8 envers les banques ;
  Tunisair, −97 à −414 MD, dettes de 3 099 MD en 2018. Rapprochement fait avec les interventions par
  société de la note transport (annexe 8) : **Transtu concorde par la subvention d'exploitation
  de ses comptes** — 135,0, 140,0 et 141,0 MD en 2021, 2022 et 2023 (annexe 9, LF 2025, p. 60)
  contre 135,0, 140,0 et 141,0 (annexe 8) — mais **pas par la ligne « transferts » de
  l'annexe 9** (161,9 en 2021, 147,5 en 2022 ; 144,2 en 2018 contre 162,0 ; 138,6 en 2019 contre
  131,4), dont le contenu n'est pas détaillé. **La SNCFT ne concorde sur aucune des deux** :
  subvention d'exploitation de 84,5, 70,0 et 95,0 MD en 2021-2023 dans ses comptes, transferts
  de 135,4 et 129,8 MD en 2021-2022 dans l'annexe 9, interventions de 71,9, 86,6 et 82,5 MD dans
  l'annexe 8 — l'échec de recoupement que la note transport relevait déjà pour 2016-2017 se
  prolonge.
- **Fiscalité** (cinquième frontière, constatée) : les « versements » des entreprises sont
  surtout des « décaissements fiscaux et douaniers » (§ 1.4), que le rapport ne ventile pas par
  impôt ; la RNTA et la Manufacture des tabacs de Kairouan, premières contributrices, renvoient
  au chapitre des droits de consommation.

---

## 8. Avis : volume ou chapitre

**Un chapitre long, pas un volume — du moins pas encore.** La matière sourcée aujourd'hui tient
en trois blocs inégaux. Le premier est solide et neuf : 2016-2024, transferts, garanties, encours
garanti, dettes croisées, dividendes — huit années, six éditions, des tableaux prêts. Le
deuxième est court mais propre : la définition légale et ses seuils (34 % en 1985, 50 % en 1989,
les banques dedans de 1995 à 2001, la liste par décret en 1996), et les recettes de privatisation
année par année de 1987 à 2009. Le troisième manque : **entre 2010 et 2016, rien de budgétaire**,
et avant 1987 rien du tout ; pas d'effectif total, pas de valeur ajoutée, pas de transferts longs.
Un volume de quatre chapitres (périmètre et droit ; flux budgétaires ; dette et garanties ;
cessions) aurait deux chapitres appuyés sur huit ans de données et un sur un classeur : le plan
type — « longue période économique » en fin de chaque section — ne serait pas tenu.

Le découpage par ailleurs joue contre le volume : la moitié de l'argent est de la compensation
(déjà un volume), un cinquième va aux caisses (déjà un volume), et la masse salariale est aux
rémunérations publiques. Ce qui reste en propre — la relation de bilan entre l'État et ses
entreprises : garanties, arriérés croisés, dividendes, cessions — fait un chapitre cohérent,
avec une thèse lisible dans les chiffres : jusqu'en 2009 l'État vend (6 milliards de dinars de
recettes, dont la moitié en 2006) ; depuis 2017 le budget verse 7 à 17 milliards par an à
l'ensemble des entreprises et établissements publics — caisses, compensation et établissements
d'enseignement compris, la part propre aux entreprises hors compensation restant à isoler —,
l'État garantit 21 milliards de leur dette, reçoit 0,1 à 0,3 milliard de dividendes, et les
entreprises tiennent sur lui 7 milliards de créances de subvention, dont 3,2 milliards que le
ministère ne confirme pas.

**Où le placer.** Pas dans « Compensation » (il le déborde), ni dans « Rémunérations publiques »
(il n'y serait qu'un appendice). Deux places possibles : (a) un chapitre du volume
« Compensation », rebaptisé alors pour couvrir « les transferts de l'État aux entreprises » — peu
souhaitable, le volume a son objet ; (b) **un dixième volume court, d'un seul chapitre pour
commencer**, « Entreprises publiques », avec le plan type d'un dispositif (mise en place ;
ruptures 1987-1989, 1994-2006, après 2011 ; bilan ; sections secondaires : garanties, dividendes,
cessions ; longue période). C'est la forme recommandée : elle n'engage pas quatre chapitres, et
elle s'étoffera si le second passage trouve 2010-2016 (rapports de l'Unité de suivi), les
transferts par établissement, et la série légale du plafond des garanties depuis 1961 — ce
dernier filon est le seul temps long déjà à portée de main.

**Ce qu'un second passage devrait faire, par ordre d'utilité** : (0) trancher 14 506,6 ou
14 560,6 pour 2022 et relire la ventilation par nature de 2023 ; (1) les annexes par
établissement de l'annexe 8, pour isoler « hors compensation, hors caisses » ; (2) les tableaux
par entreprise des éditions arabes, pour la dizaine des plus lourdes, 2018-2023 ; (3) le rapport
2010-2014 ou 2010-2016 de l'Unité de suivi ; (4) BCT et lois de règlement pour les transferts et
les revenus de participations avant 2016 et les cessions après 2009 ; (5) les plafonds de
garantie des lois de finances depuis 1961, et les articles de lois de finances sur les fonds de
restructuration (§ 2) ; (6) les décrets de liste de 1997 et 2004 ; (7) l'encours des prêts
rétrocédés, que l'annexe 7 traite (pages repérées, non lues).
