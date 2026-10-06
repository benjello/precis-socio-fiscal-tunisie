# Note documentaire — les études d'incidence des subventions : données, calculs pas à pas, résultats, limites

Passe du 6 octobre 2026. **Famille de tout ce qui suit : « rapport extérieur » / évaluation économique.** Aucun de ces chiffres n'est budgétaire ; aucun ne se mêle aux séries du ministère des Finances. Niveau de preuve : **couche texte** des PDF (nés numériques), lue en continu, sauf les trois pièces marquées **image** (tableau 1, figures 11 et 12 de la note de 2013). Pagination : « p. N du rapport / p. M du fichier ». Rien de versionné n'a été modifié. Textes de travail : `scratchpad/relu/etudes/*.sq.txt` (un marqueur `=== p.M ===` par page du fichier) ; images `relu/etudes/t1-18.png`, `f11-24.png`, `f12-25.png`.

Lecture effective : note de 2013 — sommaire exécutif, chapitres I à III, § 51-53 du chapitre IV, annexes 1 à 3 (les chapitres IV et V sur le PNAFN et les recommandations n'ont été que parcourus) ; document de 2015 — en entier ; document CEQ — résumé, § 2 à 5 (méthode, hypothèses, résultats sur les subventions), le reste parcouru ; étude INS-CRES-BAD — chapitres 2 et 3, conclusion, annexe 1 (début), le chapitre 4 (transferts directs) parcouru.

---

## A. Banque mondiale, novembre 2013 — « Vers une meilleure équité : les subventions énergétiques, le ciblage et la protection sociale en Tunisie » (rapport n° 82712-TN, note de politique, 59 p.) — clé `bm-2013-82712`

**(a) Question.** Trois questions (p. viii et § 4, p. 1 / p. 9 et 14 du fichier) : qui bénéficie des subventions énergétiques ; quel effet auraient différents scénarios de réforme sur la croissance et la consommation ; quelles options de réforme. Assistance technique demandée par l'administration tunisienne (préface, p. vi).

**(b) Données.**
- Ménages : enquêtes de l'INS sur le budget, la consommation et le niveau de vie (« EBCM ») de **2005 et 2010** ; l'incidence est calculée sur 2010 (le PNAFN sur 2005). Taille d'échantillon non donnée.
- Prix et subventions : ministère des Finances et ministère de l'Industrie (« calculs du staff ») ; STEG pour l'électricité ; prix de référence d'**avril 2013** (annexe 2, p. 40 / p. 53).
- Macroéconomie : matrice de comptabilité sociale de l'INS de **2005** (37 branches, 47 produits) — « la plus récente à compter de septembre 2013 » (tableau 6, p. 15 / p. 28).
- Cadrage : base de données *World Economic Outlook* du FMI, 2013 (tableau 15, p. 40 / p. 53) : PIB à prix courants 70,40 milliards de dinars en 2012, 76,24 en 2013. **Base du PIB non précisée par la source.**

**(c) Le calcul, pas à pas.**
1. *Subvention par produit (tableau 1).* Méthode de l'**écart de prix** : « Les subventions implicites dans cette analyse ont été calculées sur la base de la méthodologie de l'analyse de "price-gap" qui tient compte des différences entre les prix globaux et les prix au détail » (note 10, p. 4 / p. 17). Les « prix globaux » sont des prix franco à bord, « pas directement comparables aux prix au détail, mais [qui] constituent les seules valeurs qui existent » (note 7, p. 2 / p. 15). La note ne donne **ni la formule ni le détail des frais et taxes ajoutés** au prix de référence. Elle donne le résultat par unité (tableau 16, p. 41 / p. 54) : « prix réel » = prix de vente + subvention unitaire, en dinars, avril 2013 :

   | | GPL (kg) | Pétrole lampant (l) | Essence (l) | Gasoil (l) |
   |---|---:|---:|---:|---:|
   | Prix de vente | 0,57 | 0,81 | 1,57 | 1,40 |
   | Subvention unitaire | 1,21 | 0,47 | 0,28 | 0,27 |
   | « Prix réel » | 1,78 | 1,28 | 1,85 | 1,67 |
   | Hausse nécessaire pour supprimer la subvention (%) | 211,58 | 58,02 | 17,96 | 19,00 |

   Réserve : la note ne dit pas de quel gasoil il s'agit (ordinaire à 0,2 % de soufre, ou 50 ppm) ; le prix de 1,40 D est à rapprocher des prix publics de mars 2013 du chapitre sur les carburants avant citation.
   La dépense par produit (tableau 1) se lit alors comme : *consommation totale au prix de vente* × *taux de hausse nécessaire*. **Vérification de la note documentaire** (calcul, non lu) : GPL 483 / 225 = 215 % (publié : 214) ; essence 199 / 884 = 22,5 % (23) ; gasoil 50 ppm 50 / 230 = 21,7 % (22) ; gasoil 693 / 1 739 = 39,9 % (40) ; fuel lourd 170 / 103 = 165 % (165) ; pétrole lampant 23 / 36 = 64 % (66). **L'électricité échappe à cette règle** : 1 671 / 2 169 = 77 %, pour un taux de hausse publié de 30 %.
2. *Électricité.* L'annexe 1 le dit : « Pour calculer le niveau de ces dernières [subventions sur l'électricité], on s'est basés sur la subvention d'exploitation que la STEG fait apparaître dans son bilan, et on a essayé de calculer l'équivalent-prix de cette subvention » (p. 35 / p. 48) ; et, dans les limites : « la structure des subventions publiques aux principaux opérateurs énergétiques n'a pas pu être identifiée, ce qui nous a obligés à mettre des hypothèses concernant les taux de subvention de l'électricité » (p. 39 / p. 52). Le montant de l'électricité (1 671 MD en avril 2013) n'est donc pas un écart de prix mesuré : c'est une grandeur comptable de la STEG convertie.
3. *Explicite et implicite.* « Subventions directes (explicites) » : la dépense budgétaire (ministère des Finances). « Subventions indirectes (implicites) » : celles « aux producteurs » — raffinage et production d'énergie —, par exemple le brut cédé par l'ETAP à la STIR « à 50 DTN le baril, ce qui correspond au tiers du prix du marché » (§ 11, p. 5 / p. 18).
4. *Incidence entre ménages.* Classement des personnes par **quintile de dépense de consommation par tête et par an** (figure 7, p. 9 / p. 22 : moyennes de 794, 1 368, 1 905, 2 670 et 5 064 D par tête en 2010 ; 2 360 D pour l'ensemble) ; « Q » = 20 % de la population. Le bénéfice d'un ménage est sa consommation du produit multipliée par la subvention unitaire, avec le modèle d'équilibre partiel **SUBSIM** (Araar et Verme, 2012). La note ne dit pas comment les quantités sont tirées de l'enquête ; l'outil lui-même (Araar et Verme, 2012) n'a pas été ouvert ici. Le seul contrôle lu est celui du document de 2015 (voir B) : quantité × subvention unitaire. Les valeurs sont « ajustées sur la base des prix des carburants à partir d'avril 2013 » ; l'extrapolation 2010-2013 repose sur les estimations démographiques et économiques de 2013 (annexe 2). **Effets directs seulement** dans les figures 11 à 13 et dans les scénarios de transfert.
5. *Effets indirects.* Deux instruments distincts : (i) une simulation d'une hausse de 10 % des prix (figure 19, p. 19 / p. 32), dont la source technique n'est pas précisée ; (ii) un **modèle calculable d'équilibre général** dynamique séquentiel inspiré du modèle SELMA de Marouani et Robalino (2012), consommation en système linéaire de dépenses, calé sur la matrice de 2005 ; scénarios : suppression en cinq ans (2014-2018) de toutes les subventions énergétiques, ou du GPL et de l'essence seuls ; hypothèse centrale : **toute l'économie budgétaire est réinvestie**, aucune mesure d'atténuation ; bouclage : dépenses publiques exogènes, déficit endogène, taux de change variable d'ajustement (annexe 1).
6. *Élasticités.* Effets directs à consommation inchangée ; pour l'électricité, la figure 18 est « basée sur une élasticité égale à 0 », l'effet étant « la moitié » avec −0,3. Les niveaux de consommation incompressible du modèle macroéconomique sont des hypothèses (« on ne connaît pas les niveaux de consommation incompressible des produits pétroliers en Tunisie »).

**(d) Résultats chiffrés.**

*Tableau 1 (p. 5 / p. 18), lu à l'image* — « Dépenses totales (implicites et explicites) des subventions énergétiques, 2013 » :

| | GPL | Essence | Gasoil 50 ppm | Gasoil 0,2 % | Fuel lourd | Pétrole lampant | Électricité | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Taux de subvention, avril 2013 (%) | 68 | 15 | 16 | 26 | 62 | **37** | **27 / 50** | — |
| Consommation totale au prix de vente, avril 2013 (MD) | 225 | 884 | 230 | 1 739 | 103 | 36 | 2 169 | 5 385 |
| Hausse de prix estimée pour supprimer la subvention (%) | 214 | 23 | 22 | 40 | 165 | 66 | 30 | — |
| Montant en avril 2013 (MD) | 483 | 199 | 50 | 693 | 170 | 23 | 1 671 | 3 290 |
| en % du PIB | 0,7 | 0,3 | 0,07 | 1 | 0,2 | 0,03 | 2,4 | 4,7 |
| Montant prévu fin 2013 (MD) | 749 | 321 | 75 | 1 071 | 214 | 32 | 2 569 | 5 032 |
| en % du PIB | 1,0 | 0,4 | 0,1 | 1,4 | 0,3 | 0,0 | 3,4 | 6,6 |

Note du tableau : « PIB en 2012 : 70,400 MD. PIB prévu en 2013 : 76,240 MD. […] Montants prévus fin-2013 en pourcentage du PIB : subventions explicites : 4.7 % ; subventions implicites : 1.9 % ; total : 6.6 % ». Vérification (calcul) : 3 290 / 70 400 = 4,67 % — le montant d'avril est rapporté au **PIB de 2012** ; 5 032 / 76 240 = 6,60 % — celui de fin d'année au **PIB prévu de 2013**. Les deux pourcentages n'ont donc pas le même dénominateur. Décomposition d'avril (§ 9) : 3,3 % de subventions directes aux prix et 1,4 % de subventions indirectes aux producteurs. Parts dans le total (figure 5) : électricité 51 %, gasoil 21 % (plus 2 % pour le 50 ppm), GPL 15 %, essence 6 %, fuel lourd 5 %, pétrole lampant 1 %.

*Structure de la dépense des ménages (tableau 4, p. 10 / p. 23, enquête de 2010), en % de la dépense totale :*

| Quintile | Électricité et gaz | Essence | GPL | Gasoil | Pétrole | Ensemble énergie |
|---|---:|---:|---:|---:|---:|---:|
| 1 (le plus bas) | 4,0 | 0,1 | 2,3 | 0,1 | 0,01 | 6,5 |
| 2 | 3,4 | 0,2 | 1,6 | 0,2 | 0,01 | 5,6 |
| 3 | 3,1 | 0,6 | 1,3 | 0,2 | 0,01 | 5,2 |
| 4 | 2,9 | 1,3 | 1,0 | 0,2 | 0,00 | 5,5 |
| 5 (le plus élevé) | 2,7 | 2,6 | 0,5 | 0,4 | 0,01 | 6,3 |
| Ensemble | 3,0 | 1,6 | 1,0 | 0,3 | 0,0 | 5,9 |

*Tableau 5 (p. 10 / p. 23)* — population selon le bloc tarifaire de l'électricité : 0-50 kWh (0,075 D) : 1,3 %, 12,8 kWh par tête ; 50-300 kWh (0,092-0,135 D) : 55,1 %, 286,8 ; 300 kWh et plus (0,135-0,230 D) : 43,6 %, 591,0. Ce sont les prix de la grille du 1er septembre 2012 (75 ; 92 / 135 ; 135 / 200), sauf la borne haute « 0,230 », qui n'est pas dans la grille de la STEG (200).

*Figure 12 (p. 12 / p. 25), lue à l'image* — **part de chaque quintile dans les bénéfices directs, par produit (%)** :

| Produit | Q1 | Q2 | Q3 | Q4 | Q5 |
|---|---:|---:|---:|---:|---:|
| Électricité et gaz | 13 | 17 | 19 | 22 | 29 |
| Essence | 1 | 3 | 8 | 20 | 67 |
| GPL | 15 | 19 | 21 | 23 | 22 |
| Gasoil | 2 | 7 | 13 | 19 | 59 |
| Pétrole lampant | 9 | 11 | 10 | 29 | 41 |
| Ensemble des subventions énergétiques (figure 11, p. 11 / p. 24, lue à l'image) | 13 | 16 | 19 | 23 | 29 |
| Subventions alimentaires, pour comparaison (figure 11, image) | 16 | 18 | 20 | 21 | 25 |

*Figure 13 (p. 13 / p. 26)* — **bénéfice direct par tête et par an (dinars), prix d'avril 2013** :

| Quintile | GPL | Électricité | Essence | Gasoil | Pétrole | Ensemble |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 44 | 17 | 1 | 0 | 0 | 62 |
| 2 | 55 | 22 | 2 | 1 | 0 | 80 |
| 3 | 60 | 26 | 5 | 1 | 0 | 91 |
| 4 | 66 | 30 | 12 | 2 | 0 | 110 |
| 5 | 60 | 39 | 35 | 4 | 0 | 139 |
| Moyenne | 56 | 27 | 9 | 1 | 0 | 94 |

(Alimentaire, même figure : 80, 100, 107, 114, 129 ; moyenne 106.) Les parts de la figure 11 se retrouvent à l'arrondi près : 62 / 482 = 13 %, 80 / 482 = 17 % (figure : 16), 139 / 482 = 29 % (calcul).

*Réforme, effets macroéconomiques (tableau 6, p. 15 / p. 28)* — moyenne sur cinq ans par rapport à la situation sans réforme, toutes subventions / GPL et essence seuls : PIB +0,21 / +0,12 point ; investissement +12,5 % / +4,5 % ; déficit public −47,9 % / −16 % ; dette publique −8 % / −2,7 % ; consommation des ménages −3,7 % / −1,3 % ; demande de travail −0,41 % / −0,1 % ; taux de chômage +0,34 / +0,1 point. Secteurs : +1,8 à +10,9 % (bâtiment, industries non métalliques et métalliques, transport aérien) ; −3,8 à −6,7 % (électricité, transport terrestre, agriculture et pêche, textile, services domestiques).
*Pauvreté* : la suppression de la subvention au GPL relèverait le taux de pauvreté « de près de 1.8 pour cent, sur la base d'un seuil de pauvreté de 1025 DTN par tête » (§ 31, p. 18 / p. 31).
*Compensation (tableaux 11 et 12, p. 29 / p. 42)* : transfert couvrant les effets directs d'une suppression totale en douze mois : 66 D par tête et par an (essence 9, gasoil 1, GPL 56 — **l'électricité n'y est pas**), soit 300 D pour un ménage de 4,5 personnes ; budget : 145 MD pour 20 % de la population (398 803 ménages), 278 MD pour 40 %, 406 pour 60 %, 528 pour 80 % ; « épargne nette » 573 MD dans le premier cas, 440 dans le second.

**(e) Limites dites par l'étude.** Estimation macroéconomique « à considérer avec prudence car elle suppose un réinvestissement des épargnes » ; résultats à utiliser « plutôt à titre indicatif de tendances d'évolution » ; tableaux entrées-sorties de 2005, structure des consommations intermédiaires « probablement » changée ; consommations incompressibles inconnues ; production locale de produits pétroliers « difficile à modéliser » ; structure des subventions aux opérateurs non identifiée, d'où des hypothèses sur l'électricité ; pas de microsimulation greffée au modèle ; prix franco à bord non comparables aux prix de détail ; effets indirects exclus des figures de répartition.

**(f) Incohérences relevées.**
1. **Le taux de subvention de l'électricité d'avril 2013 — TRANCHÉ.** La cellule imprimée est « 27 / 50 » ; « 37 » est la cellule voisine, celle du **pétrole lampant**. La lecture « 37 % pour l'électricité » de la note sur les tarifs est un décalage d'une colonne ; la lecture « 27 à 50 % » est celle que fait le document de 2015 de la même cellule (« Its subsidized price share oscillated between 27 and 50% », p. 11 / p. 13). La note de 2013 n'explique nulle part ces deux nombres (ni deux catégories d'abonnés, ni une fourchette) : **à citer tel quel — « 27 / 50, sans explication dans la source » — ou à ne pas citer.** Aucun des deux n'est cohérent avec les autres lignes de la colonne (hausse nécessaire de 30 % ; 1 671 / (2 169 + 1 671) = 44 %).
2. Le « montant en avril 2013 » n'est pas défini (dépense annualisée aux prix d'avril ? prévision initiale ?) : 3 290 MD « en avril » contre 5 032 MD « prévu fin 2013 », avec des dénominateurs différents.
3. § 20 : « le total des bénéfices directs […] est de 162 MD par an pour les 20 pour cent de la population aux revenus les plus élevés, soit près de 627 000 ménages » et 118 MD pour le premier quintile (400 000 ménages). Or 139 D × un cinquième de 10,9 millions d'habitants = 303 MD, et 62 D × 2,18 millions = 135 MD (calcul) : les montants en MD du § 20 ne se déduisent pas de la figure 13. Ne citer que les montants par tête.
4. Sommaire exécutif : gasoil « 60 pour cent » pour le dernier quintile ; § 19 et figure 12 : 59.
5. Chômage : 16,7 % daté de 2013 dans le sommaire, de 2012 au § 6.
6. Figure 13 : le GPL fait 56 / 94 = 60 % du bénéfice direct moyen alors qu'il ne pèse que 15 % de la dépense totale du tableau 1 : les deux grandeurs ne se comparent pas (l'une est la part des ménages, effets directs ; l'autre toute l'économie) — à dire au lecteur.

---

## B. Cuesta, El-Lahga et Lara Ibarra, juin 2015 — « The Socioeconomic Impacts of Energy Reform in Tunisia: A Simulation Approach », Banque mondiale, *Policy Research Working Paper* n° 7312, 28 p. — clé `bm-2015-wps7312`

**(a) Question.** Effets budgétaires et distributifs de la réforme annoncée fin 2014 — suppression des subventions à l'essence, au gasoil et au GPL, hausse uniforme de 10 % des prix de l'électricité des ménages — et de trois façons de redistribuer l'économie réalisée.

**(b) Données.**
- Enquête nationale sur le budget, la consommation et le niveau de vie des ménages de **2010** (INS). **Un sous-échantillon**, non l'échantillon complet : celui qui permet de repérer les titulaires de la carte de soins (note du tableau 11, p. 20 / p. 22) ; taille non donnée ; après repondération, taux de pauvreté de 15,3 % au lieu des 15,4 % officiels.
- Dépenses de 2010 actualisées à (janvier) 2014 par l'indice des prix, la croissance du PIB et celle de la population (p. 7 / p. 9).
- Prix : structure tarifaire en vigueur depuis le **1er mai 2014** ; prix intérieurs du ministère des Finances ; prix de référence internationaux obtenus de la direction générale de l'énergie du ministère de l'Industrie (encadré 1).
- **Tableau entrées-sorties de 2010** de l'INS, pour les effets indirects.
- Seuil de pauvreté : seuil **haut** de l'INS, de la BAD et de la Banque mondiale (2012), ajusté par milieu.

**(c) Le calcul, pas à pas.**
1. *Subvention unitaire — écart de prix (encadré 1, p. 10 / p. 12).* Prix non subventionné NP = prix de référence international + **toutes les taxes locales et les coûts intérieurs de distribution** ; subvention S = NP − DP (prix de vente intérieur) ; taux SR = S / NP. Le taux est donc rapporté au prix non subventionné, non au prix payé.
2. *Quantités.* La distribution des dépenses d'énergie de 2014 est convertie en quantités en lui appliquant la grille tarifaire : « The current energy tariff structures are applied to that distribution of household spending on energy to derive a distribution of household consumption » (p. 7-8 / p. 9-10). Pour l'électricité, la dépense est donc inversée à travers les tranches de la grille de mai 2014.
3. *Classement.* Quintiles de consommation par tête (individus et ménages).
4. *Effet direct.* Consommations inchangées : « No immediate changes in consumption are assumed […]. Everyone consumes the same, but at higher prices » (p. 16-17 / p. 18-19). La hausse de prix équivaut à un relèvement proportionnel du seuil de pauvreté du ménage. **Aucune élasticité.**
5. *Effet indirect.* Les hausses des prix de l'énergie sont répercutées sur les produits qui l'emploient comme intrant, par le tableau entrées-sorties de 2010 — « a simple approximation » ; les résultats complets ne sont pas publiés (« available from the authors upon request », note 8).
6. *Économie budgétaire* = somme des subventions retirées aux ménages, sans réaction de comportement : elle reproduit donc la répartition initiale des subventions.
7. *Compensation, trois scénarios à budget constant* (toute l'économie redistribuée, sans coût de gestion) : transfert universel ; « ciblage actuel » par les cartes de soins à tarif réduit ; « ciblage parfait » des pauvres d'après réforme.
Outil : SUBSIM (Araar et Verme, 2012).

**(d) Résultats chiffrés.**

*Tableau 3 (p. 11 / p. 13) — subvention unitaire, structure de mai 2014 (dinars) :*

| | Prix non subventionné | Subvention | Taux (%) | Prix de vente |
|---|---:|---:|---:|---:|
| Essence (litre) | 1,856 | 0,186 | 10 | 1,670 |
| GPL (kg) | 1,790 | 1,220 | 68 | 0,570 |
| Gasoil (litre) | 1,584 | 0,334 | 21 | 1,250 |
| Électricité, ménages de moins de 200 kWh par mois : 0-50 | 0,268 | 0,193 | 72 | 0,075 |
| 0-100 | 0,268 | 0,160 | 60 | 0,108 |
| 0-200 | 0,268 | 0,128 | 47 | 0,140 |
| Électricité, ménages de plus de 200 kWh : 0-200 | 0,268 | 0,117 | 43 | 0,151 |
| 201-300 | 0,268 | 0,084 | 31 | 0,184 |
| 301-500 | 0,268 | −0,012 | −4 | 0,280 |
| plus de 500 | 0,268 | −0,082 | −31 | 0,350 |

Le prix de référence de l'électricité est unique : **0,268 D le kWh** ; au-delà de 300 kWh par mois le ménage paie plus que ce prix et finance les autres (subvention négative).

*Tableau 5 (p. 13 / p. 15) — consommation résidentielle par quintile :* essence 292 millions de litres (parts : 0,3 ; 1,7 ; 6,3 ; 18,7 ; 73,0 %) ; GPL 521 milliers de tonnes (15,3 ; 18,9 ; 20,5 ; 23,4 ; 21,9) ; gasoil 63 millions de litres (1,6 ; 6,8 ; 12,9 ; 19,4 ; 59,4) ; électricité 4 702 GWh (12,5 ; 16,2 ; 18,7 ; 22,0 ; 30,6).

*Tableaux 7 et 8 (p. 15 / p. 17) — subvention reçue par les ménages :*

| Quintile | Essence (D par tête) | Gasoil | GPL | Électricité | Total par tête | Part du total (%) |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 0,09 | 0,15 | 44,53 | 36,99 | 81,76 | 14,9 |
| 2 | 0,43 | 0,65 | 55,33 | 41,42 | 97,82 | 17,9 |
| 3 | 1,57 | 1,24 | 59,88 | 46,06 | 108,74 | 19,9 |
| 4 | 4,65 | 1,86 | 68,30 | 47,85 | 122,67 | 22,4 |
| 5 | 18,18 | 5,70 | 63,91 | 48,89 | 136,69 | 25,0 |
| Ensemble | 4,98 | 1,92 | 58,39 | 44,24 | 109,53 | 100 |

**Part de chaque quintile dans la subvention de chaque produit — CALCUL de la note documentaire sur le tableau 8** (les quintiles ayant le même effectif, part = montant par tête du quintile / somme des cinq) : essence 0,4 ; 1,7 ; 6,3 ; 18,7 ; 73,0 % — GPL 15,3 ; 19,0 ; 20,5 ; 23,4 ; 21,9 — gasoil 1,6 ; 6,8 ; 12,9 ; 19,4 ; 59,4 — électricité 16,7 ; 18,7 ; 20,8 ; 21,6 ; 22,1. Pour les trois carburants ce sont les parts de consommation du tableau 5 (subvention unitaire uniforme) ; pour l'électricité la part du premier quintile dans la subvention (16,7 %) dépasse sa part dans la consommation (12,5 %), effet des tranches. Composition : GPL 53,3 %, électricité 40,4 %, essence 4,5 %, gasoil 1,8 % ; total 1 192 (le tableau écrit « millimes TND » ; c'est en millions de dinars : 109,53 D × 10,9 millions = 1 194, calcul). Vérification du mode de calcul sur le GPL : 521 000 tonnes × 1,220 D le kg = 635,6 MD, exactement l'économie du tableau 12 — **la subvention est bien quantité × subvention unitaire**.
*Tableau 9 (p. 16 / p. 18) — subvention en % de la dépense du ménage :* 8,8 ; 6,0 ; 5,0 ; 3,9 ; 2,4 du premier au cinquième quintile ; 3,9 pour l'ensemble (GPL 2,1 ; électricité 1,6 ; essence 0,2 ; gasoil 0,1).

*Tableau 10 (p. 18-19 / p. 20-21) — effet de la réforme sur la dépense par tête (dinars) :*

| Quintile | Total | dont direct | dont indirect | Total en % de la dépense (figure 5, texte) |
|---|---:|---:|---:|---:|
| 1 | −60,5 | −48,4 | −12,1 | −6,7 |
| 2 | −83,5 | −62,0 | −21,5 | |
| 3 | −99,7 | −69,5 | −30,3 | |
| 4 | −125,5 | −83,7 | −41,9 | |
| 5 | −177,1 | −102,9 | −74,3 | −3,1 |
| Ensemble | −109,3 | −73,3 | −36,0 | −4,7 |

Par produit, ensemble : GPL −68,2 (direct −58,4 ; indirect −9,8) ; gasoil −17,4 (−1,9 ; −15,5) ; électricité −13,5 (−8,0 ; −5,5) ; essence −10,2 (−5,0 ; −5,2). Le gasoil pèse peu en direct et le plus en indirect (43 % des effets indirects).

*Tableau 11 (p. 20 / p. 22) — pauvreté et inégalité :* taux de pauvreté 14,93 % avant, 17,61 % après (+2,68 points), dont GPL +1,91, électricité +0,20, gasoil +0,19, essence +0,09 ; effets directs seuls +1,95. Indice de Gini 35,81 → 36,42 (+0,61), dont GPL +0,62.
*Tableau 12 (p. 20-21 / p. 22-23) — économie budgétaire :* 817,5 MD, dont GPL 635,6 (77 %), électricité 106,7 (13 %), essence 54,2, gasoil 20,9 ; 13 % proviennent du premier quintile (109,1 MD), 28 % du cinquième (227,6 MD).
*Tableau 13 (p. 21-22 / p. 23-24) — compensation, 817,51 MD redistribués :*

| Scénario | Transfert moyen | Bénéficiaires | Pauvreté (%) | Gini |
|---|---:|---:|---:|---:|
| Avant réforme | — | — | 15,27 | 36,57 |
| Réforme sans compensation | — | — | 17,84 | 37,18 |
| Transfert universel | 75 D | 10,9 millions | 14,87 | 36,29 |
| Ciblage actuel (cartes de soins) | 264 D | 3,1 millions | 13,83 | 35,46 |
| Ciblage parfait | 420 D | 1,9 million | 5,25 | 34,22 |

**(e) Limites dites par les auteurs.** Pas de réaction de comportement (effets « immédiats ») ; structure de consommation de 2010 supposée valoir pour 2014 ; sous-échantillon, d'où des taux de départ qui ne sont pas les taux officiels ; scénarios de compensation « unrealistic » (ciblage parfait et sans coût ; toute l'économie réinvestie dans la lutte contre la pauvreté ; aucun coût administratif) ; réforme simulée « still vaguely defined » ; effets indirects par une « simple approximation », résultats détaillés non publiés ; analyse limitée à la consommation résidentielle.

**(f) Incohérences relevées.**
1. **Les tranches 0,158 / 0,301 / 0,501 D — TRANCHÉ : erreur du texte courant, non de la simulation.** Ces trois prix n'apparaissent que dans le paragraphe de la p. 8 (p. 10 du fichier). Sur la même page, le **tableau 2** du document donne 184 ; 280 (250 pour le non résidentiel) ; 350 (295) — la grille de la STEG du 1er mai 2014, lue à l'image dans `note-tarifs-mt-ht-gaz.md` — et le **tableau 3**, qui sert au calcul, emploie 0,184 ; 0,280 ; 0,350. Deux hypothèses testées et rejetées : (i) prix toutes taxes comprises — 184 × 1,12 + 5 de surtaxe = 211, non 158 ; (ii) grille de janvier-avril 2014 de l'annexe 1 du document — 157 ; 240 ; 330. Aucune ne redonne 158 / 301 / 501. Le texte se contredit d'ailleurs lui-même page suivante (« the residential tariff increase is 25 % or 70 millimes », soit 280 → 350). **Conséquence pour le volume : la réserve sur l'électricité peut être levée ; citer les tableaux 2 et 3, non le paragraphe.**
2. *Deux points de départ.* Tableau 11 : pauvreté 14,93 → 17,61 (+2,68), Gini 35,81 → 36,42. Tableau 13 : 15,27 → 17,84 (+2,57), Gini 36,57 → 37,18. Le résumé dit « 2.5 percentage points », le texte « almost 3 percentage points (2.69) ». La note du tableau 11 l'explique (prix actualisés à 2013 d'un côté, sous-échantillon de l'enquête de 2010 de l'autre) mais intervertit ses propres chiffres (« Gini of 36.5 % differs slightly from the official 35.8 % »). Citer un seul tableau et dire lequel.
3. Le commentaire du tableau 13 intervertit les numéros des simulations 1 et 2.
4. Tableau 6 : consommation d'électricité « par individu » de 80,40 kWh (unité de temps non dite), alors que 4 702 GWh pour 10,9 millions d'habitants font 431 kWh par an, soit 36 par mois (calcul). Ne pas citer le tableau 6.
5. Tableau 4 reprend le tableau 1 de la note de 2013 en omettant la colonne du pétrole lampant et écrit « April 2013 GDP in 2012 prices estimated at 70,400 million TND » là où la note de 2013 écrit « PIB en 2012 » : même nombre, deux libellés ; **base non précisée**.
6. « Energy subsidies […] account for one-fifth of all public spending, or 7 % of the GDP in 2013 » (p. 4 / p. 6) contredit la phrase précédente (4,7 % du PIB pour l'énergie ; 7 % pour l'ensemble énergie, alimentation et transport).
7. L'économie sur l'électricité (106,7 MD) pour une hausse uniforme de 10 % : la formule n'est pas donnée ; elle ne se déduit pas de l'effet direct par tête (8,0 D × 10,9 millions = 87 MD, calcul).

**Pièce utile au chapitre sur l'électricité.** L'annexe 1 du document (p. 25 / p. 27, couche texte, disposition à contrôler à l'image) donne la **grille basse tension du 1er janvier 2014**, que le volume n'a pas : redevance 500 ; 75 ; 108 ; 123 (101-200) ; puis 136 (1-200) ; 157 (201-300) ; 240 résidentiel / 210 non résidentiel (301-500) ; 330 / 270 (501 et plus). Source seconde (les auteurs citent « STEG 2014, Tables des tarifs ») : à publier comme telle, ou à confirmer par une pièce de la STEG. Le document date aussi les hausses : +10 % en janvier 2014 et +10 % en mai 2014 pour la basse et la moyenne tension ; subvention des cimentiers réduite de moitié en janvier 2014 et supprimée en juin 2014 (d'après le FMI, 2014).

---

## C. Jouini, Lustig, Moummi et Shimeles — « Fiscal Incidence and Poverty Reduction: Evidence from Tunisia », *CEQ Working Paper* n° 38, mai 2016, révisé en juin 2017, 26 p. (chapitre 18 du *Commitment to Equity Handbook*, 2018) — clé à créer `jouini-lustig-moummi-shimeles-2017-ceq38`

**Constat d'abord : ce document ne donne AUCUNE répartition par produit.** Les subventions y sont un seul agrégat — produits de base, énergie et transport confondus. Il ne peut pas nourrir un tableau « énergie ».

**(a) Question.** Effet de l'ensemble des prélèvements et des transferts sur l'inégalité et la pauvreté, et qui bénéficie des dépenses d'éducation et de santé (méthode *Commitment to Equity*).

**(b) Données.** Enquête de l'INS de 2010 ; seuls les individus présents dans les trois volets (dépenses, niveau de vie, alimentation) : **23 764 individus, 5 456 ménages**, « about half of the households in the full expenditure component » (p. 14 du fichier). Impôts indirects et subventions (produits de base et énergie) : direction générale des études et de la législation fiscale du ministère des Finances. Budgets des ministères pour l'éducation et la santé.

**(c) Calcul.** L'enquête ne donnant pas les revenus, la consommation est posée égale au revenu disponible, et l'on remonte au revenu de marché en ajoutant impôts directs et cotisations simulés, en retranchant les transferts (PNAFN, bourses). Cinq concepts : revenu de marché, revenu de marché net, revenu disponible, revenu « post-fiscal » (après impôts indirects et subventions), revenu final (avec éducation et santé en nature). Subventions : « calculated based on information reported on food and non-food consumption […]. The amount of subsidies is adjusted downward to match their ratio to disposable income in administrative accounts and the household survey » (p. 17 du fichier) — imputation selon la consommation déclarée, puis **mise à l'échelle vers le bas** ; ni prix de référence ni formule par produit. Classement par déciles de revenu de marché par tête. Ni effets indirects, ni comportements.

**(d) Résultats sur les subventions (tous produits).** En 2010, subventions = 2,4 % du PIB, dont 1,2 pour l'alimentation, 1 pour l'énergie, 0,3 pour le transport (p. 12 ; base du PIB non précisée) ; 6,9 % du PIB en 2013. Part de chaque décile dans les subventions indirectes (tableau 18-8, p. 21 ; colonne identifiée par recoupement avec le texte) : 5,2 ; 6,5 ; 7,6 ; 8,3 ; 8,7 ; 9,3 ; 10,7 ; 11,8 ; 13,7 ; 18,3 % — les 20 % les plus modestes en reçoivent 11,7 %, le dixième le plus aisé 18,3 %. Subventions en % du revenu de marché (tableau 18-7, p. 20) : 23,6 % au premier décile, 5,1 % au dixième, 9,0 % pour l'ensemble. Coefficient de concentration : 0,21 (tableau 18-9). Ensemble du système : Gini de 0,43 (revenu de marché) à 0,39 (disponible), 0,38 (post-fiscal) et 0,35 (final) ; pauvreté au seuil national : 12,90 % → 13,14 % → 13,00 % — elle ne baisse pas, les impôts indirects pesant plus que les subventions à partir du troisième décile (tableau 18-5).

**(e) Limites dites.** Pas de données de revenu ; transferts directs réduits au PNAFN et aux bourses ; montants imputés depuis les comptes administratifs et remis à l'échelle ; impôt sur le revenu simulé.
**(f) Incohérences.** « indirect subsidies, which account for 2.3 percent of government spending » (p. 21) contre « 2.4 percent of the GDP » (p. 12). Tableau 18-8 : alignement des colonnes à contrôler à l'image avant toute citation décile par décile. Le document attribue à l'étude INS-CRES-BAD « the poor received only 9.2 percent of total subsidies and 12 percent of food subsidies » — or 9,2 % est la part du **budget de la Caisse** et 12 % la part des subventions **reçues par les ménages**, toutes deux alimentaires (voir D).

---

## D. INS, CRES et BAD, 2013 — « Analyse de l'impact des subventions alimentaires et des programmes d'assistance sociale sur la population pauvre et vulnérable », 52 p. — clé `ins-cres-bad-2013-subventions`

**(a) Question.** Quelles classes bénéficient des subventions alimentaires ; quel serait le niveau de pauvreté sans elles ; comment se comparent-elles aux transferts directs (PNAFN, carte de soins).

**(b) Données.** Enquête nationale sur le budget, la consommation et le niveau de vie des ménages de **2010** : volet budgétaire **11 281 ménages** ; volet « accès aux services » (module III) **5 690 ménages**, « soit la moitié » (p. 40). Prix de vente et **prix de revient** des produits de base : services du ministère du Commerce (annexe 1, p. 49). Dix produits : semoule, couscous, pâtes alimentaires, farine, gros pain, baguette, tomate industrielle, lait, sucre, huile végétale.

**(c) Le calcul, pas à pas.**
1. *Subvention reçue par un ménage* (annexe 1, p. 49, « incidence immédiate […] à composition du panier de consommation constant ») : somme, sur les produits, de la quantité consommée × (prix de revient − prix de vente). La subvention unitaire est donc un écart au **prix de revient** intérieur, non à un prix international.
2. *Classement.* Quintiles de dépense par tête (« quintiles de revenu » dans les titres) ; dépense réelle moyenne par tête : 815, 1 422, 2 008, 2 871, 5 890 D (2 601 pour l'ensemble). Et pauvres / non pauvres au seuil national (15,5 % de la population en 2010).
3. *Taux de transfert* : « relatif » = subvention / dépense ; « réel » = subvention / (dépense + subvention) — 7,7 % au premier quintile, 1,5 % au cinquième, 3,1 % pour l'ensemble (tableaux 1 et 4, p. 16 et 20).
4. *« Hors ménages »* : c'est un **solde**. Subventions reçues par les ménages d'après l'enquête : 888 MD ; budget de la Caisse : « environ 1 150 MD » ; différence : 262 MD, 22,8 %, « transférés hors ménages (restaurants, cafés, hôtels, commerce illégal aux frontières) » (p. 19). Remarque de la note documentaire : ce solde absorbe aussi tout écart entre consommation déclarée à l'enquête et consommation réelle ; l'étude ne le dit pas.
5. *Indices de ciblage* (p. 22-25) : indice relatif = part du quintile dans la subvention / sa part dans la dépense totale ; indice absolu = part du quintile dans la subvention / sa part dans la population (20 %) : 0,82 au premier quintile (il reçoit 16,3 % du total), 1,07 au cinquième (21,3 %).
6. *Suppression, effet immédiat (court terme)* (p. 32-33) : revenu nominal fixe, **consommation inchangée** ; la perte = poids du produit dans la dépense × pourcentage de hausse du prix ; on recompte les pauvres. L'étude écrit que cette approche « surestime » l'effet.
7. *Suppression, après adaptation (long terme)* (p. 35-36 et annexe 2, p. 50) : estimation d'un **système de demande quadratique presque idéal** (« le modèle AIDS devient ainsi le modèle QAIDS », annexe 2, p. 50) donnant la matrice des élasticités-prix et le vecteur des élasticités-revenu ; les ménages substituent ; on recompte. Les élasticités elles-mêmes n'ont pas été relevées dans cette passe.

**(d) Résultats.** Subvention par tête et par an : 68,156 ; 84,159 ; 87,458 ; 89,873 ; 89,121 D par quintile, 83,752 pour l'ensemble ; pauvres 64,777, non-pauvres 87,231. Gros pain : 20,644 (Q1) à 28,508 (Q5) ; semoule : 16,953 à 12,069 ; baguette : 0,287 à 7,912 ; huile : 12,712 à 12,272 (tableau 1, p. 16). Part des pauvres dans la subvention de chaque produit : semoule 14,5 %, couscous 14,2 %, huile 12,9 %, gros pain 11,7 %, sucre 11,6 %, lait 6,0 %, baguette 2,2 % ; ensemble 12,0 % (tableau 3, p. 18). Pauvreté : 15,5 % → 19,1 % dans l'effet immédiat (+3,6 points ; rural 22,6 → 27,6 ; grandes villes 9,0 → 11,5) ; 16,8 % après adaptation ; pauvreté extrême 4,6 → 6,3 (+1,7) dans l'effet immédiat, 5,2 après adaptation (+0,6) ; écart de pauvreté 3,8 → 5,0 ; par produit : gros pain +1,20 point, semoule +0,70, huile +0,60, pâtes et sucre +0,30 chacun (p. 33-35). Gini : 37,4 % avec, 38,5 % sans (p. 48 ; l'étude date ce Gini de « 2011 »).

**La définition des classes — ce que l'étude dit et ne dit pas.**
- Elle répartit le **budget de la Caisse** ainsi : « seulement 9,2 % […] profite aux ménages les plus démunis, 60,5 % aux ménages de la classe moyenne, 7,5 % à la population aisée et 22,8 % sont transférés hors ménages » (p. 19, graphique 4).
- « Pauvres » = sous le seuil national de pauvreté : le 9,2 % est 12 % × 888 / 1 150 (note 7 de la p. 19 : le 12 % est rapporté aux subventions reçues par les ménages, le 9,2 % au budget total).
- **« Classe moyenne » et « classe aisée » ne sont définies nulle part dans le document** (recherche de « classe », « aisé », « riche », « moyenne » dans tout le texte : quatre mentions de la classe moyenne, aucune définition, aucun seuil). Ce n'est pas le cinquième quintile : celui-ci reçoit 21,3 % des subventions des ménages, soit 16 % du budget (calcul), non 7,5 %. Ailleurs, l'étude appelle pourtant « population aisée » le cinquième quintile (p. 19 et 20). Le renvoi probable est au rapport INS-BAD-Banque mondiale de 2012 sur la pauvreté et la polarisation, qui n'a pas été ouvert ici.
- **Conséquence : la répartition 9,2 / 60,5 / 7,5 / 22,8 n'est publiable qu'avec la mention « classes moyenne et aisée non définies par l'étude »** ; le volume peut publier sans réserve la part des pauvres (12 % des subventions reçues par les ménages ; 9,2 % du budget) et le solde hors ménages.

**(e) Limites dites.** L'effet immédiat surestime ; résultats tirés du module III, « des analyses supplémentaires sont nécessaires » (p. 48).
**(f) Incohérences.** Tableau 2 (p. 17) : non-pauvres « 78,231 » — c'est 87,231 (texte p. 15 et tableau 5) ; tableau 5 (p. 20) : pauvres « 46,777 » — c'est 64,777 : deux inversions de chiffres ; **les valeurs du volume (64,8 et 87,2) sont les bonnes.** Tableau 4 : cellules décalées au deuxième quintile (« 1,344 » en farine). Tableau 1 de la p. 33 : signes erratiques. L'indice de Gini de 37,4 % est daté de 2010 dans le résumé (p. 7) et de « 2011 » dans la conclusion (p. 48). (Le « 0,6 point » de pauvreté extrême du résumé n'est pas une incohérence : c'est l'effet après adaptation — 4,6 % → 5,2 % —, contre +1,7 point dans l'effet immédiat.)

---

## E. Ce que ces quatre pièces autorisent, mises côte à côte

| | Banque mondiale 2013 | Cuesta et al. 2015 | CEQ 2017 | INS-CRES-BAD 2013 |
|---|---|---|---|---|
| Champ | énergie, toute l'économie et ménages | énergie, ménages | tous prélèvements et transferts | alimentaire, ménages |
| Enquête | 2005 et 2010 | 2010, sous-échantillon, actualisée à 2014 | 2010, 5 456 ménages | 2010, 11 281 et 5 690 ménages |
| Prix de référence | prix « globaux » franco à bord ; électricité : subvention d'exploitation de la STEG | prix international + taxes + distribution ; électricité 0,268 D/kWh | aucun (mise à l'échelle sur les comptes) | prix de revient (ministère du Commerce) |
| Date des prix | avril 2013 | mai 2014 | 2010 | 2010 |
| Classement | quintiles de dépense par tête | quintiles de consommation par tête | déciles de revenu de marché | quintiles de dépense par tête ; pauvres / non-pauvres |
| Effets indirects | modèle d'équilibre général (matrice de 2005) ; simulation à +10 % | tableau entrées-sorties de 2010 | non | non |
| Comportements | inchangés (élasticité 0 ; variante −0,3 pour l'électricité) | inchangés | inchangés | inchangés, puis système de demande |

Les deux études de la Banque mondiale ne se raccordent pas terme à terme : subvention directe moyenne par tête de 94 D (2013, prix d'avril 2013, électricité 27 D) contre 109,5 D (2015, prix de mai 2014, électricité 44,2 D) ; part du premier quintile 13 % contre 14,9 %, du cinquième 29 % contre 25 %. L'écart tient surtout à l'électricité, dont la subvention n'est pas calculée de la même façon (grandeur comptable de la STEG en 2013 ; écart à un prix de référence unique par tranche en 2015). À présenter en deux tableaux séparés, chacun avec sa date de prix.

## F. Références candidates

Déjà présentes : `bm-2013-82712`, `bm-2015-wps7312`, `ins-cres-bad-2013-subventions`. À créer :
```json
[
 {"id": "jouini-lustig-moummi-shimeles-2017-ceq38", "type": "report", "title": "Fiscal Incidence and Poverty Reduction: Evidence from Tunisia", "author": [{"family": "Jouini", "given": "Nizar"}, {"family": "Lustig", "given": "Nora"}, {"family": "Moummi", "given": "Ahmed"}, {"family": "Shimeles", "given": "Abebe"}], "issued": {"date-parts": [[2017, 6]]}, "collection-title": "CEQ Working Paper", "number": "38", "publisher": "Commitment to Equity Institute, Tulane University", "note": "citation-key: jouini-lustig-moummi-shimeles-2017-ceq38 ; mai 2016, révisé en juin 2017 ; chapitre 18 du Commitment to Equity Handbook (2018). Fichier : tunisia-data/data/raw/banque-mondiale-rapports/ceq_2017_wp38_jouini_lustig_moummi_shimeles_tunisia.pdf. URL à reprendre du catalogue (non vérifiée dans cette passe)."},
 {"id": "araar-verme-2012-subsim", "type": "report", "title": "Reforming Subsidies: A Tool-Kit for Policy Simulations", "author": [{"family": "Araar", "given": "Abdelkrim"}, {"family": "Verme", "given": "Paolo"}], "issued": {"date-parts": [[2012]]}, "collection-title": "Policy Research Working Paper", "number": "6148", "publisher": "Banque mondiale", "note": "citation-key: araar-verme-2012-subsim ; cité par les deux études de la Banque mondiale comme source de l'outil SUBSIM ; NON OUVERT ici — à récupérer avant citation (règle : aller chercher l'étude que l'étude rapporte)."}
]
```
Non récupérés, cités de seconde main par ces études : INS-BAD-Banque mondiale (2012), *Mesure de la pauvreté, des inégalités et de la polarisation en Tunisie 2000-2010* (seuils de pauvreté ; définition probable des classes) ; FMI (2014), *Subsidy Reform in the Middle East and North Africa* ; Marouani et Robalino (2012).

## G. Notions à glossaire

- **méthode de l'écart de prix** (*price-gap*) : subvention unitaire = prix de référence (international, majoré des taxes et des coûts de distribution) − prix intérieur ; source canonique : encadré 1 du document de 2015.
- **subvention explicite / implicite** ; **effet direct / effet indirect** ; **prix non subventionné** ; **tableau entrées-sorties**, **matrice de comptabilité sociale**, **modèle calculable d'équilibre général** ; **indice de ciblage absolu / relatif** ; **taux de transfert indirect réel** ; **système de demande** ; **test d'éligibilité multidimensionnel** (*proxy means test*).

## H. Lacunes

- Définition des classes « moyenne » et « aisée » de l'étude INS-CRES-BAD : absente du document ; rapport INS-BAD-Banque mondiale de 2012 à ouvrir.
- Taille des échantillons des deux études de la Banque mondiale : non donnée.
- Formule exacte du prix de référence (frais et taxes ajoutés) dans la note de 2013 ; origine du prix de référence de l'électricité de 0,268 D dans le document de 2015 ; signification de « 27 / 50 » : non données par les sources.
- Élasticités de l'étude INS-CRES-BAD (annexe 2) : non relevées. Chapitres IV et V de la note de 2013 et chapitre 4 de l'étude INS-CRES-BAD : parcourus, non dépouillés.
- Tableaux lus dans la couche texte et non à l'image (à contrôler avant publication cellule par cellule) : document de 2015, tableaux 3, 5, 7 à 13 et annexe 1 ; CEQ, tableaux 18-7 et 18-8 ; INS-CRES-BAD, tableaux 1 à 5. Seuls le tableau 1 et les figures 11 et 12 de la note de 2013 ont été lus à l'image.
- Rapport n° 47294 de 2008 (subventions par produit de 2000, 2006 et 2007) : non rouvert ici.
- Recherches infructueuses au sens de `docs/recherches.yml` : sans objet (aucun texte juridique cherché).
