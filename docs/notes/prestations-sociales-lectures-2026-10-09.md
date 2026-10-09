# Prestations sociales — lectures du documentaliste (ticket D0 à D13 et section d'études)

Note rendue le 9 octobre 2026. Ordre suivi, sur consigne du coordinateur : études et rapports
chiffrés, puis D2, D3, D5, D11, puis D6, puis le reste. Aucun dépôt modifié ; aucune fiche de
`docs/recherches.yml` rejouée par `scripts/recherches.py` (les sous-commandes réécrivent le
registre) : les recherches infructueuses sont rendues ici en fiches proposées (§ 8).

Conventions de cette note. « Lu à l'image » : page du fascicule rendue en image et lue. « Couche
texte » : `pdftotext` sur le fascicule du corpus local (`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`).
« Couche texte décodée » : police décalée de 29, décodée, apostrophes et accents à relire à
l'image avant citation. Les adresses pist.tn citées ont toutes répondu `200 application/pdf` le
9 octobre 2026 (certificat échu, vérification TLS désactivée pour pist.tn seulement) ; le contenu
français a été lu sur la copie du corpus local, non sur le fichier servi ce jour.
Pages des documents de la Banque mondiale : « PDF n » est le rang de la page dans le fichier,
« p. n » le folio imprimé.

---

## 1. Études et rapports chiffrés sur l'Amen social, le PNAFN et les allocations pour enfants

Neuf pièces : le rapport du ministère des Affaires sociales (source administrative nationale) et
les huit pièces de `sources/banque-mondiale-rapports-urls.csv` (rapports extérieurs). Dans chaque
fiche, les chiffres sont rangés en **constaté** (fichier administratif, budget, décompte du
projet) et **simulé ou estimé** (enquête, microsimulation, incidence).

**Aucune de ces pièces ne dit la base du PIB qu'elle emploie** (ni l'année de base, ni si la série
est rétropolée) : toute part du PIB ci-dessous est à écrire « base non dite par la source ».

### 1.1 Ministère des Affaires sociales, rapport de suivi et d'évaluation de l'Amen social pour 2023

- **Référence.** Ministère des Affaires sociales, Instance générale de la promotion sociale,
  « تقرير المتابعة والتقييم لبرنامج الأمان الاجتماعي لسنة 2023 », 48 p., arabe. Fichier
  `tunisia-data/data/raw/caisses/mas/amen_social_suivi_evaluation_2023_ar.pdf`, SHA-256
  `977bad7b…7d2b` (fiche `sources/mas-amen-social-2023.md`). **Aucune adresse d'origine
  vérifiée** (exemplaire transmis par le propriétaire). Les traductions ci-dessous sont de travail.
- **Famille.** Administratif national (fichiers de paiement et crédits du ministère) ; ce n'est
  ni la loi de finances ni un rapport extérieur. Pages 24-26 et 40-41 : enquête auprès des
  bénéficiaires (« IBM »), à ne pas mêler aux décomptes.
- **Méthode.** Stocks de décembre des bénéficiaires actifs du transfert mensuel ; entrées,
  sorties, retours par suivi individuel (identifiant CNSS comme clé) ; crédits « affectés » par
  intervention (tableau 1) ; définitions des indicateurs au tableau 3 (PDF 17).
- **État.** Déjà dépouillé dans `tunisia-data` (`mas-amen-social-2023-credits-bruts`,
  `…-beneficiaires-bruts`). Relu ici, sur la couche texte arabe : PDF 13, 17, 36-38.

**Constaté — bénéficiaires du transfert mensuel, stock de décembre (tableau 4, PDF 17, « منتفع »)** :

| Année | Stock | Entrées | Sorties | Solde |
|---|---:|---:|---:|---:|
| 2018 | 242 833 | | | |
| 2019 | 255 508 | 21 764 | 9 089 | 12 675 |
| 2020 | 261 802 | 16 385 | 10 091 | 6 294 |
| 2021 | 268 258 | 19 267 | 12 811 | 6 456 |
| 2022 | 305 930 | 44 059 | 6 387 | 37 672 |
| 2023 | 337 199 | 46 972 | 15 703 | 31 269 |

Tableau 5 (PDF 18) : retours après interruption 0, 744, 883, 1 587, 485 (2019-2023) ; taux de
renouvellement 12,1 ; 10,1 ; 12,0 ; 16,5 ; 18,6 % ; taux de continuité 91,5 ; 93,7 ; 92,8 ; 85,6 ;
86,1 %.

**Les trois totaux de 2023, tels quels, et ce que chacun recouvre** :

| Valeur | Où | Ce qu'elle compte | Unité imprimée |
|---:|---|---|---|
| 337 178 | texte introductif, PDF 13 : « 337.178 منتفعا مع موفى سنة 2023 » | bénéficiaires en fin d'année, sans tableau | « منتفع » (bénéficiaire) |
| 337 199 | PDF 17, texte et tableau 4 : « من 242833 منتفعا في ديسمبر 2018 إلى 337199 منتفعا في ديسمبر 2023 » | stock de décembre du tableau des flux ; seule valeur cohérente avec entrées − sorties | « منتفع » ; définition du tableau 3 : « bénéficiaires actifs inscrits en décembre de chaque année » |
| 337 200 | tableau 7 (PDF 22), somme des cinq tranches de montant (230 278 à 220 D ; 37 332 à 230 D ; 34 519 à 240 D ; 21 395 à 250 D ; 13 676 de 260 à 340 D) ; et tableau 10 (PDF 32) : 287 547 classés par le score + 49 653 non classés | répartition par montant versé ; répartition classés / non classés | « personnes » au tableau 7 ; **« ménages »** au tableau 10 (fiche `tunisia-data`) |

Réponse à l'ajout de D4 sur l'unité : le rapport écrit « منتفع » (bénéficiaire) aux tableaux des
flux et « ménages » au tableau du classement pour des totaux égaux à une unité près ; le
bénéficiaire du transfert est donc l'unité allocataire (individu ou famille, au sens de l'arrêté
du 19 mai 2020, art. 2 : « للفرد أو للأسرة الواحدة »), non un nombre de personnes couvertes. À
écrire « allocataires (individus ou familles) ». De même décembre 2022 : 305 930 (tableau 4)
contre 218 082 + 87 844 = 305 926 (tableau 10).

**Constaté — classement par le score (tableau 10, PDF 32, ménages)** : juin 2022, 191 388 classés
et 93 399 non classés ; décembre 2022, 218 082 et 87 844 ; décembre 2023, 287 547 et 49 653.

**Constaté — crédits affectés (tableau 1, PDF 7, milliers de dinars)** :

| Intervention | 2021 | 2022 | 2023 |
|---|---:|---:|---:|
| Transfert mensuel direct | 645 000 | 687 400 | 867 000 |
| Allocation des enfants de moins de 6 ans | non imprimé | 40 057 | 45 827 |
| Transferts des fêtes et occasions | 27 091 | 26 726 | 30 451 |
| *Sous-total transferts directs* | 672 091 | 754 183 | 943 278 |
| Aides de rentrée scolaire et universitaire | 50 978 | 53 888 | 60 900 |
| Transport gratuit des enfants | 2 870,3 | 2 837,3 | 3 406,3 |
| *Sous-total dépenses sociales des familles* | 53 848,3 | 56 725,3 | 64 306,3 |
| Microprojets, familles pauvres et à revenu limité | 4 819,2 | 4 560,7 | 5 143,4 |
| Microprojets, personnes handicapées | 4 373,4 | 2 984 | 2 736,4 |
| *Sous-total insertion économique* | 9 192,6 | 7 544,7 | 7 879,8 |
| **Total** | 735 131,9 | 818 453,0 | 1 015 464,1 |

Le budget des soins (cartes de soins gratuits et à tarif réduit) n'y est pas : il relève du
ministère de la Santé (dit par la Banque mondiale, § 1.3, encadré 1).

**Constaté — allocations pour enfants (PDF 36-38)** :

- Moins de 6 ans, décembre 2022 : 138 266 enfants de 96 366 familles ; décembre 2023 :
  156 418 enfants de 110 848 familles (+13,1 %) ; 51 % de garçons. Répartition de décembre 2023
  (figure 9) : 79 % carte à tarif réduit, 17 % transfert mensuel, 3 % et 1 % pour les deux
  dernières rubriques (carte de soins gratuits, sans couverture — attribution des deux petites
  parts à relire à l'image).
- Moins de 6 ans, financement (PDF 36) : pilote de décembre 2020 à janvier 2022 financé par la
  banque allemande de développement avec l'UNICEF ; puis « 40 millions de dinars » sur le prêt
  de la Banque mondiale du projet de protection sociale, « entré en vigueur en juin 2021 », pour
  « 150 mille enfants sur deux ans ». Montant de 2023 au texte : « 54،943.4 م د » ; au tableau 1 :
  45 827 milliers de dinars. Les deux sont à garder séparés.
- 6 à 18 ans, décembre 2023 (PDF 38) : 422 542 enfants de 217 157 familles, « soit en moyenne
  deux allocations par famille », pour un crédit total de **124,6 millions de dinars** « financé
  par le don susmentionné ».
- Tableau 13 (PDF 38), décembre 2023, par type de couverture : transfert mensuel 27 270 (0-5 ans),
  123 602 (6-18 ans), 144 023 enfants aidés sur 172 911 enregistrés (83,3 %) ; carte à tarif
  réduit 123 234, 253 804, 377 292 sur 502 659 (75,1 %) ; carte de soins gratuits 1 156, 3 613,
  4 656 sur 8 438 (55,2 %) ; total publié 156 418, 422 542, 525 971 sur 684 008 (76,9 %). Le
  texte de la même page écrit **127 911** enfants pour les familles du transfert mensuel, le
  tableau 144 023 : quatrième discordance interne, non signalée par la fiche de `tunisia-data`.
- Projets d'insertion (tableau 17, PDF 45) : 95, 198, 220, 307 projets de 2020 à 2023 ; 2 ; 5 ; 5 ;
  4,3 millions de dinars.

**Ce que le rapport ne permet pas de dire.** Rien sur le ciblage par décile ni sur l'effet sur la
pauvreté ; rien en part du PIB ; pas de nombre de personnes couvertes ; pas de cartes de soins en
stock par année (seulement des enfants par type de carte) ; crédits « affectés », non dépenses
exécutées.

**D4 — réponse.** Voir § 5.

### 1.2 Banque mondiale, document d'évaluation du projet, 2021 (PAD4414)

- **Référence.** Banque mondiale, *Tunisia COVID-19 Social Protection Emergency Response Support
  Project (P176352), Project Appraisal Document*, rapport n° PAD4414, 21 mars 2021 (date du
  catalogue), 92 pages PDF, folios « Page n of 86 ». Fichier
  `data/raw/banque-mondiale-rapports/wb_2021_covid19_social_protection_pad4414.pdf`, SHA-256
  `4da44c86…b942`.
- **Famille.** Rapport extérieur (bailleur). Il cite des décomptes du ministère (constaté) et
  des simulations (CRES et BAD 2017 ; Banque mondiale sur l'enquête de 2015).
- **Méthode des simulations.** (a) « Simulations conducted by CRES and the AfDB in 2017 »
  (note 33 : *Vers l'adoption d'un modèle de ciblage optimal des pauvres par les programmes
  d'assistance sociale en Tunisie*, CRES et BAD, 2017) — étude non récupérée, citée ici de
  seconde main. (b) Simulations de la Banque mondiale « using official survey data (ENBCM
  2015) » : application de la formule de score (PMT) à l'enquête nationale sur le budget, la
  consommation et le niveau de vie des ménages de 2015 ; déciles de la population ; note 34 de
  la source du tableau 6 non relevée. Aucune description du modèle, des poids ni des erreurs
  d'échantillonnage dans le document.

**Constaté (cité du ministère, sans tableau source)** :

- Programme : « 880,000 poor and vulnerable households, representing about 30 percent of the
  population » ; transfert permanent : « about 260,000 poor households (roughly 8 percent of
  the population) » ; « a cash transfer of TND 180 (US$65) per month » ; « a supplemental child
  cash transfer of TND 10 (US$4) per 0-5 years-old-child per month » [sic : l'arrêté du
  19 mai 2020 dit « chaque enfant à charge de moins de 18 ans »] ; carte de soins à tarif
  réduit : « about 620,000 vulnerable households (roughly 21 percent of the population) », dont
  450 000 enregistrés au registre (§ 20, PDF 20, p. 14).
- « The number of PCT beneficiaries increased from 130,000 households in 2010 to 260,000
  households in 2020 » (§ 84, PDF 42, p. 36). Le financement additionnel de 2022 écrit 124 000
  pour 2010 : les deux valeurs coexistent.
- Mesures de 2020 : complément de 50 D pendant deux mois aux 260 000 ménages du transfert ;
  deux transferts de 200 D à 450 000 ménages titulaires de la carte à tarif réduit ; un
  transfert de 200 D à 300 000 ménages supplémentaires (§ 23, PDF 21, p. 15).
- Tableau 3 (PDF 34-35, p. 28-29), coûts du projet en dollars : transferts temporaires
  100 millions ; transfert permanent, 260 000 ménages, 65 USD par mois, 120 millions ; extension
  à 50 000 ménages, 25 millions ; allocation familiale, 120 000 enfants de 0 à 5 ans, 11 USD par
  mois, 20 millions. Coût total du projet : 318 millions de dollars.

**Estimé ou simulé** :

- Dépense : « the AMEN Social PCT accounted for about 0.6 percent of GDP in 2020; the share has
  gradually risen from only 0.4 percent in 2008 » (§ 84, PDF 42, p. 36) — base du PIB non dite ;
  extension à 10 % de la population : + 0,1 point, de 0,6 à 0,7 % (§ 86, PDF 43, p. 37) ;
  allocation familiale de 30 D à tous les enfants de 0 à 5 ans du programme : 0,05 % du PIB
  (§ 88, PDF 43) — **0,03 % au § 80 (PDF 41, p. 35)** : les deux valeurs sont dans le même
  document ; subventions à l'énergie : « more than two percent of GDP » (§ 80).
- Montant relatif : le transfert de 180 D « averages about one-third of the per capita
  consumption for the poorest quintile (… ENBCM … 2015) » (§ 84).
- Ciblage (CRES-BAD 2017) : « only 40 percent of benefits of the PCT are directed to the poorest
  quintile » ; effet : « PCTs reduce the incidence of poverty by 0.8 percentage points » (§ 85,
  PDF 42).
- Tableau 5 (PDF 43, p. 37), part du premier décile couverte par le transfert, en % : couverture
  de 8 % de la population, ancien mode de sélection 17,4, nouveau score pour tous 46,9 ;
  couverture de 10 %, ancien mode 22,5, nouveau score 56,0, mode mixte (2 points ajoutés par le
  score) 33,2.
- Tableau 6 (PDF 44, p. 38), répartition des bénéficiaires ou de la dépense par décile (D1 à
  D10), en % :

  | Intervention | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
  | Subventions à l'énergie | 6,1 | 7,4 | 8,0 | 8,6 | 9,2 | 9,7 | 10,3 | 11,5 | 12,8 | 16,4 |
  | Subventions alimentaires | 8,7 | 9,6 | 9,7 | 10,0 | 10,2 | 10,3 | 10,4 | 10,5 | 10,5 | 10,0 |
  | Transfert permanent, ancienne sélection | 22,1 | 17,7 | 15,3 | 11,6 | 9,9 | 7,6 | 6,3 | 5,2 | 2,9 | 1,4 |
  | Transfert permanent, score | 59,3 | 21,8 | 9,3 | 5,1 | 2,4 | 1,0 | 0,5 | 0,1 | 0,2 | 0,3 |
  | Enfants de 0 à 5 ans des ménages hors régime contributif | 29,6 | 17,3 | 13,6 | 11,6 | 8,6 | 6,4 | 5,5 | 3,8 | 2,5 | 1,4 |

  Le titre dit « Incidence of different social protection intervention » sans préciser s'il
  s'agit de la part des bénéficiaires ou de la dépense, ni l'année, ni la variable de classement.
- Allocation familiale de 30 D aux 0-5 ans : + 2 % environ de la consommation moyenne du premier
  décile ; pauvreté − 0,6 point, pauvreté des enfants − 1 point (§ 88, PDF 43). Taux de pauvreté
  par taille : 11 % sans enfant, 26 % avec trois enfants ; pauvreté des enfants 24 % (même §).
- Ancienneté : « approximately 30 percent of the current cash transfer beneficiaries have been
  in the program for more than 20 years » (§ 87, renvoi à CRES-BAD 2017).
- Effet de la crise : hausse simulée du taux de pauvreté de 7,3 points (§ 83, PDF 42).

**Ce que le document ne permet pas de dire.** Aucun décompte daté par mois ; « 8 % de la
population » sans le nombre de personnes ni la taille moyenne du ménage ; les simulations
portent sur l'enquête de 2015, antérieure au programme ; le tableau 6 est sans unité explicite.

### 1.3 Banque mondiale, premier financement additionnel, 2022 (PAD4815)

- **Référence.** Banque mondiale, *Tunisia COVID-19 Social Protection Emergency Response Support
  Project, Additional Financing (P177821), Project Paper*, rapport n° PAD4815, mars 2022,
  88 pages PDF, folios « Page n of 83 ». Fichier `wb_2022_covid19_social_protection_af_pad4815.pdf`,
  SHA-256 `00a1956a…37ce`.
- **Famille.** Rapport extérieur. Chiffres du ministère (constaté) ; simulations CRES-BAD 2017 et
  **CRES et Banque mondiale (2021)**, *Identification des ménages pauvres et vulnérables en
  Tunisie : rapport technique de ciblage sur le modèle d'approximation des moyens des ménages*
  (note 19, PDF 39) — non récupéré.
- **Méthode de l'étude CRES-Banque mondiale, telle que le document la rapporte (§ 64-66,
  PDF 39-40, p. 34-35).** Le nouveau modèle de score « was applied to the 2015 National
  Household Budget and Expenditure Survey … data to test its performance » ; résultats présentés
  par le CRES en décembre 2021 ; déciles de dépense par tête ; critères d'exclusion de la loi
  organique (affiliation à la CNRPS, logement secondaire, voiture) ajoutés en variante. Ni
  l'échantillon ni la formule ne sont donnés.

**Constaté** :

- « the coverage and budget of the PCT increased from 124,000 households in 2010 to 265,000
  households in 2021 » (§ 11, PDF 16, p. 11) ; croissance annuelle moyenne de 7,2 % (§ 61,
  PDF 37, p. 32) ; carte à tarif réduit : 620 000 ménages, « about 21 percent » (§ 11) puis
  « roughly 20 percent » (§ 14) de la population ; ensemble du programme : environ 30 % de la
  population (§ 60).
- Prestations de 2021 (§ 14, PDF 17, p. 12) : transfert de 180 D ; « a supplemental Family
  Allowance of TND 10 … for each child 0-18 years old, which will continue until the age of 25
  for children in education or training » ; 20 D pour l'enfant handicapé ; rentrée scolaire 50 D
  par élève, 120 D par étudiant ; 60 D pour chacune des trois fêtes ; carte à tarif réduit
  contre un droit annuel de 10 D.
- **Encadré 1 (PDF 18, p. 13), budget de 2021 en millions de dollars** : transfert permanent
  228,9 (« 0.6 percent of GDP », « 88 percent of the program's total budget ») ; rentrée scolaire
  6,5 ; fêtes religieuses 18,2 ; aide ponctuelle 1,4 ; transport gratuit 2,5 ; activités
  génératrices de revenu 1,8 ; total 259,3. « The budget of health care … is managed separately
  from the AMEN Social budget by the Ministry of Health. » À rapprocher du tableau 1 du
  ministère (735,1 millions de dinars en 2021) : les rubriques ne se recoupent pas terme à terme
  (rentrée scolaire 50 978 milliers de dinars au ministère, 6,5 millions de dollars ici).
- Transferts temporaires versés à plus de 890 000 ménages à fin février 2022 (PDF 21 environ).
- Figure 4 (PDF 38, p. 33), « Evolution of Cash Transfer as Share of Minimum Wage », source
  « Institut National de la Statistique and MoSA data » : transfert mensuel du PNAFN et salaire
  minimum, 1987-2021. Étiquettes extraites de la couche texte, dans l'ordre des années 1987,
  1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015, 2018, 2019, 2020, 2021 — transfert :
  7,7 ; 15 ; 25,8 ; 36,3 ; 43,3 ; 56,7 ; 68,3 ; 92,5 ; 105 ; 115 ; 150 ; 180 ; 180 ; 180 ; 180 D ;
  salaire minimum : 105 ; 120 ; 154 ; 187 ; 224 ; 272 ; 286 ; 302 ; 302 ; 320 ; 338 ; 379 ; 403 ;
  429 ; 429 D. **L'appariement étiquette-année est reconstitué, à relire à l'image avant tout
  usage** ; le régime du salaire minimum n'est pas dit. C'est la seule série longue du montant
  du PNAFN rencontrée dans ces pièces (les onze paliers de 1987 à 2018 n'ont aucun texte selon
  la note de l'assistance).
- Montant relatif : en 2018, 47 % du salaire minimum (« about 38 percent of per capita
  consumption for the poorest quintile ») ; 42 % en 2021 (§ 61).

**Estimé ou simulé** :

- Part du PIB : « around 0.56 percent of the GDP » ; 0,75 % après extension à 310 000 ménages et
  relèvement à 200 D ; « the universal subsidy program that accounts around 5.6 percent of the
  GDP in 2020 » (§ 61, PDF 37, p. 32) ; ensemble des réformes : « about 1 percent of GDP » (§ 46,
  PDF 32, p. 27). Base du PIB non dite.
- Erreurs de ciblage de l'ancien mode de sélection (§ 62, PDF 38, p. 33, renvoi à CRES-BAD
  2017) : « of 8.3 percent of households that were supposed to be covered by the PCTs,
  4.6 percent were not, which represents an exclusion rate of 53.1 percent » ; effet sur la
  pauvreté − 0,8 point.
- Figure 6 (PDF 39, p. 34), couverture du transfert par décile de dépense par tête, 2015, en %
  des ménages du décile, D1 à D10 : 17,4 ; 13,9 ; 12,1 ; 9,2 ; 7,8 ; 6 ; 5 ; 4,1 ; 2,2 ; 1,1.
  Figure 7, couverture de la carte de soins : 55,8 ; 39,9 ; 32,6 ; 26,2 ; 20,8 ; 16,8 ; 13,1 ;
  9,5 ; 6,8 ; 2,6 (une étiquette « 22,4 » reste sans décile : à relire à l'image). Source :
  « CRES et Banque mondiale (2021) ».
- Score : pour un programme couvrant 10 % de la population, 54 % des bénéficiaires dans le
  premier décile et 23 % dans le deuxième ; avec les critères d'exclusion, 65 % dans le premier
  décile (§ 64-65 ; figures 8 et 9, PDF 40).
- Pauvreté et inégalité (figure 10, PDF 40, p. 35) : taux de pauvreté officiel de 2015 15,2 % ;
  14,3 % « PCT – Current approach » ; 13,0 % avec le score ; indice de Gini 32,8 ; 32,5 ; 32,0.
  Le texte ne dit pas si 15,2 % est avant ou après transferts : la lecture « sans transfert →
  avec » est celle de la figure, non une phrase du rapport.
- Consommation des bénéficiaires du transfert : 134 D « with the support of the monthly
  monetary benefit », source CRES 2016 (note 18) ; unité et période non dites (§ 63).

**Ce que le document ne permet pas de dire.** Rien d'observé sur le ciblage du nouveau score
(pilote lancé en février 2022 à Kairouan, Nabeul et Jendouba, § 67) ; tout le ciblage est simulé
sur 2015.

### 1.4 Banque mondiale, second financement additionnel, 2026 (PPIAF000292)

- **Référence.** Banque mondiale, *Tunisia Social Development Promotion Support Project –
  Second Additional Financing, Project Paper on a Proposed Second Additional Loan in the Amount
  of EUR 75.4 Million (US$90 Million Equivalent)*, rapport n° PPIAF000292, **6 mars 2026**,
  80 pages PDF (le corps commence au PDF 12, folio 1), mention « For official use only » en
  couverture. Fichier `wb_2026_social_protection_af2_ppiaf000292.pdf`, SHA-256 `071edb22…db8c`.
- **Famille.** Rapport extérieur. Décomptes du ministère (constaté) ; **analyse d'incidence
  fiscale** (estimée).
- **Méthode de l'incidence (notes 27 et 28, PDF 27, p. 16).** « The Fiscal Incidence Analysis
  employs the CEQ methodology using the 2021 National Survey on Budget, Consumption and
  Household Living Standards (… EBCNV), along with administrative data and regulations for the
  year 2024. The fiscal incidence analysis is a collaboration between the World Bank and the
  Ministry of Finance. » Contribution marginale : « the difference between the inequality/poverty
  indicator without the fiscal intervention and with it (Lustig, 2022) ». Déciles de **revenu de
  marché** (figures 5 et 6). L'étude elle-même n'est ni nommée ni jointe ; le document renvoie
  aussi (note 4, PDF 14) au *Tunisia Economic Monitor, Strengthening Social Safety Nets for
  Increased Efficiency and Equity, Fall 2025* — non récupéré.

**Constaté** :

- Transfert permanent : 124 000 ménages en 2010, 386 000 en 2025, « 10 percent of the
  population » ; un million de ménages environ inscrits au programme ; 620 000 ménages à revenu
  limité, « roughly 20 percent of the population » (§ 11, PDF 14, p. 3 ; § 54-55, PDF 27, p. 16).
- Transferts temporaires : plus de 895 000 ménages en 2021 (§ 3, PDF 12, p. 1).
- Allocation des moins de 6 ans : plus de 150 000 enfants en mars 2025 (§ 4, PDF 13).
- Allocation des 6-18 ans : cible de 450 000 enfants ; « The FA annual financing amounts to
  US$50 million, corresponding to 30 TND per child per month for 450,000 children » ; pilote
  « executed by UNICEF until December 2024 » ; « the GoT decided in October 2025 to
  institutionalize the child allowance for children 6-18 » ; financement rétroactif jusqu'à
  20 % du prêt pour les allocations de 2025 ; appui de l'Union européenne en 2026 et 2027
  (§ 13, PDF 15 ; § 28, PDF 18, p. 7).
- Recertification : critères d'éligibilité du transfert permanent révisés par la « Ministerial
  Circular No. 53, issued in October 2025 » (§ 4, PDF 12) — **le rapport de suivi de novembre
  2025 écrit « Circular No. 5 on October 3, 2025 »** : numéro discordant entre deux pièces de la
  même institution ; tranches de ménages recertifiés : 114 000 ; 186 000 ; 214 000 ; 244 000 ;
  270 000 (note 15, PDF 17 environ).
- Montant relatif : « In 2025, this transfer accounted for close to 50 percent of the minimum
  wage, and just 7.9 percent in 1987 » (§ 55 ; figure 3, 1987-2025, « Source: MoSA, World Bank
  staff calculations » — valeurs non lisibles dans la couche texte).
- Coût des composantes en dollars, projet et premier financement additionnel puis après le
  second : transferts 599,0 → 599,0 millions ; capital humain 66,0 → 106,0 ; système 51,25 →
  101,025 ; total 716,25 → 806,025 (tableau des composantes, PDF 34 environ ; tableau 2, PDF 21,
  non relu).
- Handicap : recensement de 2024, 3,3 % des cinq ans et plus, environ 375 600 personnes ;
  180 273 [titulaires de carte, phrase tronquée à l'extraction] (§ 16, PDF 16 environ).

**Estimé ou simulé** :

- Part du PIB du transfert : « from 0.61 percent in 2022 to 0.91 percent in 2025 », « without
  exceeding 1 percent of GDP » (§ 55 ; figure 4, 2010-2025, « Source: INS, MoF, World Bank staff
  calculations »). Base du PIB non dite.
- Ciblage observé : « the proportion of PCT beneficiaries in the poorest two deciles rose from
  30 percent in 2022 to 44 percent in 2025 » (§ 54) — source et méthode non dites.
- Incidence (CEQ, enquête de 2021, règles de 2024 ; § 56-57, PDF 27-28, p. 16-17) : « more than
  50 percent of total PCT expenditure is received by the poorest 20 percent of households » ;
  « less than 7 percent of the PCT goes to the top 30 percent » ; le programme réduit
  l'inégalité de **1,09 point de Gini** et la pauvreté de **2,14 points de pourcentage**,
  « with the majority driven by PCTs ». Allocation des 6-18 ans : 55,9 % de la dépense dans les
  deux premiers déciles ; 1 % du revenu de marché en incidence ; contribution marginale à la
  pauvreté − 0,35 point, à l'inégalité − 0,141 point de Gini.
- Pauvreté (INS) : 20,2 % en 2010, 16,6 % en 2021 ; vulnérabilité 27 % (enquête de 2021,
  méthode de Günther et Harttgen) ; ménages avec au moins un enfant d'âge scolaire : 23 % ; par
  nombre d'enfants de 6 à 18 ans : 13,8 % (un), 22,2 % (deux), 33,9 % (trois), 48,9 % (« three
  or more » [sic, sans doute quatre et plus]) (§ 10 et 12, PDF 14-15).

**Ce que le document ne permet pas de dire.** L'incidence combine une enquête de 2021 et des
règles de 2024 : c'est une simulation, non une mesure après réforme. Aucun tableau par décile
n'est imprimé (figures sans valeurs). La part du PIB n'a ni base ni série annuelle lisible.

### 1.5 Banque mondiale, rapport de suivi n° 9, novembre 2025 (ISR04716) — pièce non dépouillée jusqu'ici

- **Référence.** Banque mondiale, *Implementation Status & Results Report, Tunisia COVID-19
  Social Protection Emergency Response Support Project (P176352)*, séquence n° 9, archivé le
  25 novembre 2025, **ISR04716**, 21 p. Fichier `wb_2025-11_social_protection_isr.pdf`, SHA-256
  `56b28b84…8a0`.
- **Famille et méthode.** Rapport extérieur ; indicateurs de résultat du projet, renseignés par
  l'unité de gestion du ministère (fichiers de paiement, registre, données de La Poste) et, pour
  la satisfaction et la préscolarisation, par la deuxième vague de l'enquête itérative auprès
  des bénéficiaires (« IBM ») d'août 2025 — échantillon non dit. Tout est constaté ou d'enquête ;
  rien de simulé.

| Indicateur | Valeur précédente (30 nov. 2024) | Valeur (31 oct. 2025) | Cible | Page |
|---|---:|---:|---:|---|
| Ménages ayant reçu un transfert temporaire | 896 675 | 896 675 (dernier versement en 2022) | 900 000 | 4 |
| dont part de femmes cheffes de ménage | | 31,4 % | | 4 |
| Ménages éligibles déjà inscrits au registre | | 636 916 | | 6 |
| Enfants de 0 à 5 ans recevant l'allocation familiale | 158 779 | 143 806 | 120 000 | 4 |
| part de filles | | 49 % | | 4 |
| Enfants de 0 à 5 ans aidés parmi ceux du registre | 75,95 % | 73,3 % (143 806 sur 196 202) | 100 % | 7-8 |
| Ménages du transfert permanent | 367 550 | 385 231 (septembre 2025) ; 383 192 (octobre 2025, p. 2 et 5) | 310 000 | 2, 5, 7 |
| dont sélectionnés par la nouvelle procédure | 85 925 | 85 930 vérifiés ; 135 237 en attente ; plus de 220 000 « potentially eligible according to the new circular » | 248 000 | 5 |
| part de femmes cheffes de ménage (nouvelle procédure) | 25,1 % | 26,3 % | | 5 |
| Ménages payés par moyen numérique | 43 % | 46 % (198 400 ménages en août 2025) | 80 % | 5 |
| Bénéficiaires satisfaits | 67 % | 73 % (femmes 79 %) | 60 % | 7 |
| Garçons de 3 à 5 ans allocataires en éducation préscolaire | 43 % | 63 % (filles 51 %) | 25 % | 8-9 |

Autres constats : dernière échéance de l'allocation des 0-5 ans payée en octobre 2025 pour avril
à juin 2025 (p. 4) — versement trimestriel à terme échu de quatre mois ; l'écart à 100 % de
couverture des 0-5 ans tient aux contrôles croisés avec la CNSS, la CNRPS et l'ATTT (p. 8) ;
163 ménages du transfert hors registre en septembre 2025 (p. 7) ; le rapport annuel de l'Amen
social pour 2022 « was finalized and published », celui de 2023 « is being finalized » (p. 9) —
**donc, pour la Banque, le rapport de 2023 du § 1.1 n'était pas publié le 25 novembre 2025** ;
« Circular No. 5 on October 3, 2025 » (p. 2).

**Ce qu'il ne permet pas de dire.** Aucune dépense, aucun montant moyen, aucun ciblage.

### 1.6 Banque mondiale, rapport de suivi n° 10, juillet 2026 (ISR08116)

- **Référence.** Même titre, séquence n° 10, archivé le 7 juillet 2026, **ISR08116**, 30 p.,
  « Official Use Only » en pied. Fichier `wb_2026-07_social_protection_isr08116.pdf`, SHA-256
  `4d780ccf…cbfd`. Même méthode qu'au § 1.5.

| Indicateur | 31 oct. 2025 | 22 mai 2026 | Cible (mars 2030) | Page |
|---|---:|---:|---:|---|
| Ménages du transfert permanent | 385 231 | 386 351 (avril 2026) ; 387 668 au commentaire de la p. 5 | 370 000 | 2, 5, 9 |
| dont vérifiés éligibles par les commissions régionales numériques | 85 930 | 128 326 | 270 000 | 5, 16 |
| Enfants de 0 à 5 ans recevant l'allocation | 143 806 | 137 014 | 120 000 | 4 |
| **Enfants de 6 à 18 ans recevant l'allocation** | 0 (27 mars 2026) | **463 903** | 450 000 | 5 |
| part de filles, 6-18 ans | | 48,7 % | 49 % | 5 |
| Ménages payés par moyen numérique | 198 400 | 209 600 | 300 000 | 6, 13, 20 |
| Enquêtes sociales réalisées | | 868 172, dont environ 500 000 géolocalisées | | 11 |
| Achèvement du premier cycle du secondaire, allocataires de 6-18 ans | | 46,6 % (référence de mars 2026) | 47,8 % | 6 |

Constats : dernier versement des deux allocations en mai 2026 pour janvier à mars 2026 (p. 4-5) ;
la baisse des 0-5 ans s'explique par le passage d'enfants à l'allocation des 6-18 ans et par la
baisse de la natalité (p. 4) ; 3 811 ménages du transfert hors registre en avril 2026 (p. 9) ;
clôture du projet reportée à mars 2030. **Coquille de la source**, p. 2 : « 463,903 children
under the age of six against a target of 450,000 » — il s'agit des 6-18 ans (tableau, p. 5).
Deux totaux pour avril 2026 : 386 351 et 387 668.

### 1.7 Banque mondiale, accord de prêt n° 9230-TN, 2021 — pièce non dépouillée jusqu'ici

- **Référence.** *Loan Agreement (COVID-19 Social Protection Emergency Response Support Project)
  between Republic of Tunisia and International Bank for Reconstruction and Development, Loan
  Number 9230-TN*, 19 p., « dated as of the Signature Date ». Fichier
  `wb_2021_loan_9230_tn_agreement.pdf`, SHA-256 `c5081269…00b4`. La date de signature n'est pas
  lisible dans la couche texte de l'accord (mentions manuscrites, PDF 3) ; **le *Journal officiel*
  la donne** : l'arrêté du 1er avril 2022 sur les allocations familiales vise « la loi
  n° 2021-28 du 22 juin 2021, portant approbation de l'accord de prêt conclu le 2 avril 2021
  entre la République Tunisienne et la Banque internationale pour la reconstitution [sic] et le
  développement pour la contribution au financement du projet d'appui à la riposte d'urgence
  contre le Covid 19 en matière de protection sociale » (JORT n° 38 du 8 avril 2022, p. 973,
  couche texte). Le rapport du ministère dit le prêt « entré en vigueur en juin 2021 » (§ 1.1).
  La loi n° 2021-28 n'a pas été lue.
- **Famille.** Acte contractuel : conditions du financement, aucune statistique.
- **Contenu chiffré** (PDF 2, 11, 13-15) : montant **247 800 000 euros** (art. 2.01) ;
  commission d'ouverture 0,25 % (619 500 euros) ; commission d'engagement 0,25 % l'an ; intérêt
  au taux de référence plus marge fixe ; échéances les 1er juin et 1er décembre ; remboursement
  du principal du 1er décembre 2025 au 1er décembre 2039 (dernière échéance : 3,40 %) ; clôture
  au 31 mars 2024 (reportée depuis à mars 2030, § 1.6). Catégories de dépense : transferts
  temporaires 82 600 000 euros ; transfert permanent, dans la limite de 99 120 000 euros ;
  allocations familiales 16 520 000 euros ; dépenses éligibles sous conditions de résultat
  47 082 000 euros ; autres 1 858 500 euros (ventilation recoupée par le tableau de
  décaissement du second financement additionnel). Conditions de résultat (annexe 4, PDF 15) :
  25 000 puis 50 000 ménages supplémentaires au transfert permanent, 310 000 au total ;
  évaluation publiée du pilote d'allocation familiale ; extension de l'allocation à tous les
  enfants de 0 à 5 ans ; formule de score mise à jour ; deux rapports annuels publiés ;
  paiements numériques.
- **Ce qu'il apporte au chapitre.** Le fondement du visa d'un accord de prêt dans l'arrêté du
  1er avril 2022 (N3 du plan) et le fait que la publication d'un rapport annuel de l'Amen social
  est une condition de décaissement. Second prêt (premier financement additionnel) :
  357 200 000 euros, dont transfert permanent 222 357 000 et allocations familiales
  21 432 000 (tableau de décaissement du § 1.4, page non relevée ; numéro de prêt non relevé).
- **Ce qu'il ne permet pas de dire.** Rien sur les bénéficiaires ni sur la dépense nationale.

### 1.8 UNICEF, rapport de recherche sur l'allocation des 6-18 ans, mai 2024

- **Référence.** UNICEF Tunisie, *Rapport de recherche sur le programme d'allocations familiales
  pour les 6-18 ans en Tunisie*, mai 2024, 124 p. (auteurs et bureau d'étude non relevés : à
  prendre en page de crédits). Fichier `unicef_2024_allocations_enfants_6_18_rapport.pdf`,
  SHA-256 `8011292c…9eb7`, adresse du catalogue `https://www.unicef.org/tunisia/media/7871/file`.
  Le second financement additionnel de la Banque date de « May 2025 » le « pilot assessment
  report » (§ 28) : soit une autre édition, soit une erreur — la couverture du fichier porte
  « MAI 2024 ».
- **Famille.** Évaluation d'un programme par l'organisme qui le finance et l'accompagne :
  rapport extérieur, à dire tel.
- **Méthode (p. 24-25 ; annexe 1, p. 88-105).** Méthodes mixtes. (1) Enquête téléphonique
  longitudinale, quatre vagues sur douze mois (2023-2024), auprès d'un échantillon
  « représentatif de ménages bénéficiaires AMEN Social ayant des enfants de 6-18 ans », stratifié
  par catégorie (PNAFN, AMG1, AMG2) ; échantillon visé 2 012 ménages, **2 239 à la vague 1**,
  **1 975 à la vague 4** (attrition 12 %, plus faible chez les allocataires du PNAFN) ; taux de
  réponse 52 % (p. 89, 93). (2) Volet qualitatif : entretiens avec des informateurs clés,
  groupes de discussion de bénéficiaires et de travailleurs sociaux, protocole d'impact
  qualitatif (QuIP). **Pas de groupe de contrôle** : « l'absence de groupe contrôle » « prévient
  l'estimation de l'impact du programme » (p. 104). Les évolutions d'indicateurs sont donc des
  évolutions observées chez les bénéficiaires, non des effets.

**Constaté (données du programme, UNICEF et ministère)** :

- Chronologie (p. 2) : allocation de 30 D aux 0-5 ans des familles pauvres et vulnérables de
  décembre 2020 à janvier 2022, « institutionnalisée en 2022 » ; doublement de l'allocation de
  rentrée scolaire de 50 D « à partir de la rentrée 2020-2021 » ; allocation des 6-18 ans
  « qui a démarré en juillet 2022 », 30 D par enfant et par mois, versée au chef de ménage.
  Financements BMZ/KfW et USAID. Note 4, p. 19 : « le programme pour les enfants de 6 à 18 ans
  ne l'est pas encore » (institutionnalisé).
- Public (p. 20) : ménages des catégories PNAFN et AMG1, « rejoints par AMG2 à partir de février
  2023 » ; en juin 2023, ouverture aux ménages hors registre ayant fait l'objet d'une enquête
  sociale (p. 28) : 23 198 enfants au troisième trimestre 2023, 28 777 au quatrième, 29 567 au
  premier trimestre 2024 (figure 4, p. 29).
- Bénéficiaires de l'allocation mensuelle : **111 682 enfants en juillet 2022, 422 683 en
  décembre 2023** (p. 20, figure 2 ; + 278 % p. 20, + 273 % p. 27). Le ministère écrit 422 542
  pour décembre 2023 (§ 1.1) : écart de 141.
- Allocation de rentrée scolaire : **deux séries dans le même rapport** — « de 240 000 enfants
  en 2022 à plus de 500 000 enfants en 2023 » (p. 20 et fiche) et « de 465 397 enfants en 2022 à
  512 204 enfants en 2023 » (p. 27-28).
- Répartition par couverture, données du programme de mars 2024 (figure 3, p. 28) : AMG2 58 %,
  sans couverture environ 7 % (texte) ; les parts de 34 % et de 1 % reviennent au PNAFN et à
  l'AMG1 — attribution à confirmer à l'image.
- Montant du transfert permanent cité : « mensualités permanentes de 240 DT » (p. 19).
- Paiement (p. 20, 31-32) : mandat postal, ou carte pour les seuls allocataires du PNAFN ; fonds
  de l'UNICEF versés à la CNSS puis à La Poste ; fréquence mensuelle prévue, non tenue.
- Financement (p. 55) : prévu jusqu'en décembre 2023, prolongé à avril 2024 par les mandats non
  retirés et une extension de la KfW ; en octobre 2023, « les finances publiques n'étaient pas
  en mesure de prendre en charge le financement du programme en 2024 ».

**Estimé** :

- « le programme des 6-18 ans couvre 73 % de tous les enfants vivant dans la pauvreté en
  Tunisie » (p. 20) : rapport du nombre d'allocataires à une estimation des enfants pauvres
  (26 % des enfants fin 2021, INS) ; le dénominateur n'est pas donné et les allocataires ne sont
  pas tous pauvres : ce n'est pas un taux de couverture des pauvres au sens d'une enquête.
- Pauvreté des enfants : 21,1 % en 2015, 26 % en 2021 (fiche) ; 16,6 % pour la population
  (CRES, 2024, p. 2).
- Enquête : 29,5 % des ménages relevant de l'AMG1 passés au PNAFN entre les vagues (tableau 2,
  p. 30 environ ; résumé p. 3) ; 20 % des ménages ont une carte de handicap pour au moins un
  enfant (p. 94) ; cheffes de ménage : 31 % au PNAFN, 22 % à l'AMG1, 3 % à l'AMG2 (p. 94).
  Les indicateurs de nutrition, de santé, de scolarité et de dépense (§ 6, p. 56-75) n'ont pas
  été relevés.

**Ce que le rapport ne permet pas de dire.** Aucun effet causal ; aucun coût total du programme
(le ministère donne 124,6 millions de dinars pour décembre 2023, § 1.1, et une convention de
191 millions) ; rien sur le ciblage par décile.

### 1.9 UNICEF, fiche de deux pages, 2024

- **Référence.** UNICEF Tunisie, *Recherche sur le programme d'allocations familiales pour les
  6-18 ans en Tunisie* (fiche de synthèse), 2024, 2 p. Fichier
  `unicef_2024_allocations_enfants_6_18_fiche.pdf`, SHA-256 `67be51d3…20c8`, adresse
  `https://www.unicef.org/tunisia/media/7916/file`.
- **Contenu.** Résumé du § 1.8, sans méthode : 111 682 → 422 683 enfants (juillet 2022 →
  décembre 2023) ; rentrée scolaire 240 000 → 512 000 (septembre 2022 → septembre 2023) ;
  « allocation mensuelle de 30 DT et doublement de l'allocation de rentrée scolaire à 100 DT
  pour les enfants de 5 à 18 ans » ; taux d'inscription scolaire de 95 à 100 %, assiduité 93 % ;
  « amélioration de 38 % du bien-être des ménages bénéficiaires » (indicateur non défini dans la
  fiche).
- **Usage.** Ne pas citer seule : tout chiffre se prend au rapport, avec sa méthode. Le « 38 % »
  n'est pas citable sans la définition de l'indicateur (section 6.2.4 du rapport, non lue).

### 1.10 Études citées par ces pièces et non récupérées (à aller chercher, non à citer de seconde main)

| Étude | Citée par | Adresse donnée par la source | État |
|---|---|---|---|
| CRES et BAD, *Vers l'adoption d'un modèle de ciblage optimal des pauvres par les programmes d'assistance sociale en Tunisie*, 2017 | PAD4414, note 33 ; PAD4815, note 17 | `http://www.cres.tn/uploads/tx_wdbiblio/Rapport_CRES_mai_2017.pdf` (non essayée) | à récupérer : c'est la source du taux d'exclusion de 53,1 %, des 40 % au premier quintile et de l'effet de − 0,8 point |
| CRES et Banque mondiale, *Identification des ménages pauvres et vulnérables en Tunisie : rapport technique de ciblage sur le modèle d'approximation des moyens des ménages*, 2021 | PAD4815, notes 19 à 21 | aucune | à récupérer : source des figures 6 à 10 |
| CRES, étude sur le secteur informel, 2016 | PAD4815, note 18 | `http://www.cres.tn/uploads/tx_wdbiblio/Secteur_informel_Tunisie.pdf` (non essayée) | secondaire |
| Banque mondiale, *Tunisia Economic Monitor, Strengthening Social Safety Nets for Increased Efficiency and Equity*, automne 2025 | PPIAF000292, note 4 | aucune | à récupérer : porte vraisemblablement l'incidence CEQ avec ses tableaux |
| Banque mondiale et ministère des Finances, analyse d'incidence fiscale CEQ (enquête de 2021, règles de 2024) | PPIAF000292, note 27 | aucune | non identifiée comme publication ; voir aussi le dépôt `ceq-tunisie` |
| Rapport annuel de l'Amen social pour 2022 (« finalized and published ») | ISR04716, p. 9 | aucune | à chercher sur le site du ministère (certificat non vérifiable ce jour, § 8) |

### 1.11 Séries qui mériteraient d'entrer au dépôt de données (non versées)

| Grandeur | Années | Pièce | Pages | Nature |
|---|---|---|---|---|
| Ménages du transfert permanent, points datés des rapports de suivi | nov. 2024, sept. et oct. 2025, avril 2026 | ISR04716, ISR08116 | 2, 5, 7 ; 2, 5, 9 | constaté ; prolonge la série du ministère (2018-2023) |
| Enfants de 0 à 5 ans allocataires | déc. 2022, déc. 2023 (ministère) ; nov. 2024, oct. 2025, mai 2026 (Banque) | § 1.1, ISR04716, ISR08116 | PDF 36 ; 4 ; 4 | constaté, deux sources |
| Enfants de 6 à 18 ans allocataires | juil. 2022, déc. 2023 (UNICEF) ; déc. 2023 (ministère) ; mai 2026 (Banque) | UNICEF 2024, § 1.1, ISR08116 | 20 ; PDF 38 ; 5 | constaté ; pilote sur don puis allocation légale |
| Ménages recertifiés par la nouvelle procédure | nov. 2024, oct. 2025, mai 2026 | ISR04716, ISR08116 | 5 ; 5, 16 | constaté |
| Ménages payés par moyen numérique | août 2025, mai 2026 | idem | 5 ; 6 | constaté |
| Budget des transferts de l'Amen social par rubrique, en dollars | 2021 | PAD4815, encadré 1 | PDF 18 | constaté (rapporté) ; double le tableau 1 du ministère |
| Transfert mensuel du PNAFN et salaire minimum | 1987-2021 (quinze points) | PAD4815, figure 4 | PDF 38 | constaté (rapporté), **à relire à l'image** |
| Part du PIB du transfert permanent | 2008, 2020, 2021, 2022, 2025 | PAD4414 § 84 ; PAD4815 § 61 ; PPIAF000292 § 55 | PDF 42 ; 37 ; 27 | estimé, base du PIB non dite : à ne pas chaîner |
| Couverture par décile, transfert et carte de soins | 2015 | PAD4815, figures 6 et 7 | PDF 39 | simulé sur enquête |
| Répartition par décile de cinq interventions | non datée (enquête de 2015) | PAD4414, tableau 6 | PDF 44 | simulé |
| Pauvreté selon le nombre d'enfants de 6 à 18 ans | 2021 | PPIAF000292, § 12 | PDF 15 | enquête |

---

## 2. D2 — Le salaire minimum de référence des plafonds de ressources

**Réponse.** Aucun texte publié ne dit quel régime de salaire minimum sert de référence : le
décret gouvernemental n° 2020-317 écrit « salaire minimum interprofessionnel garanti des
différentes professions » dans les deux éditions, sans régime horaire ; ni circulaire ni
formulaire n'ont pu être lus.

- **Texte.** Décret gouvernemental n° 2020-317 du 19 mai 2020, art. 5. JORT n° 45 du 20 mai
  2020, édition française p. 1093, <https://www.pist.tn/jort/2020/2020F/Jo0452020.pdf> ; édition
  arabe p. 1248, <https://www.pist.tn/jort/2020/2020A/Ja0452020.pdf>. **Lu à l'image, deux
  éditions.**
- **Citation (français).** « Art. 5 - Le demandeur du bénéfice ne doit avoir aucun revenu ou la
  moyenne de son revenu mensuel ne doit dépasser un montant : - égal à deux tiers du salaire
  minimum interprofessionnel garanti des différentes professions pour l'individu, - égal au
  salaire minimum interprofessionnel garanti des différentes professions pour les familles dont
  le nombre de leurs membres est égal à deux personnes, - égal à une fois et demi du salaire
  minimum interprofessionnel des différentes professions pour les familles dont le nombre de
  leurs membres varie entre trois et quatre personnes, - égal à deux fois du salaire minimum
  interprofessionnel des différentes professions pour les familles dont le nombre de leurs
  membres est égal ou supérieur à cinq personnes. »
- **Citation (arabe).** « ثلثي الأجر الأدنى المضمون لمختلف المهن بالنسبة للفرد » ; « الأجر الأدنى
  المضمون لمختلف المهن بالنسبة للأسر التي يساوي عدد أفرادها اثنين » ; « مرة ونصف الأجر الأدنى
  المضمون لمختلف المهن … بين ثلاثة وأربعة » ; « مرتين الأجر الأدنى المضمون لمختلف المهن … يساوي
  أو يفوق عدد أفرادها خمسة ».
- **Deux points de comparaison, lus.** (a) Quand le législateur veut un régime, il l'écrit : loi
  n° 96-65 du 22 juillet 1996, art. 54 nouveau de la loi n° 60-30 — « 75 % du salaire minimum
  interprofessionnel garanti, afférent au régime 48 heures » (JORT n° 60 du 26 juillet 1996,
  p. 1603, couche texte). (b) Le décret n° 98-409 du 18 février 1998, art. 2 (cartes à tarifs
  réduits), emploie déjà la formule sans régime : « un montant égal au salaire minimum inter
  professionnel garanti des différentes professions » (JORT n° 17 du 27 février 1998, p. 405,
  couche texte) ; il raisonne en revenu **annuel** de la famille.
- **Ce que disent les rapports.** Le document de projet de la Banque mondiale résume « a monthly
  income between two-thirds and two times the minimum inter-professional wage according to
  household size » (PAD4414, § 21), sans régime. La figure 4 du financement additionnel de 2022
  compare le transfert à un salaire minimum de 429 D en 2020 et 2021 : valeur à rapprocher du
  tableau du salaire minimum du volume « Marché du travail » pour dire de quel régime il
  s'agit ; ce n'est de toute façon pas le plafond de ressources.
- **État.** Texte lu ; pratique administrative **non identifiée** (fiche proposée
  `r-amen-smig-regime`, § 8).
- **Ce que cela change au plan.** Le tableau engendré des plafonds ne peut afficher que des
  multiples du salaire minimum (2/3, 1, 1,5, 2), sans les convertir en dinars, ou bien les
  convertir en disant que le régime retenu est une hypothèse. La formule de la notice du
  paramètre (« le texte ne le précise pas ») est confirmée.

## 3. D3 — La majoration pour handicap lourd et les quatre paliers

**Réponse.** Selon le texte, dans les deux éditions, la majoration d'un demi-salaire minimum
porte sur « la moyenne de revenu mensuel mentionnée au premier alinéa » de l'article 5, et ce
premier alinéa est l'alinéa qui contient les quatre tirets : elle s'applique donc aux quatre
paliers. La mention « portée ambiguë » du § 3.2 de `prestations-assistance.md` est à corriger ;
ma lecture reste à valider par la revue, car elle repose sur le décompte des alinéas.

- **Texte.** Décret gouvernemental n° 2020-317, art. 5, troisième alinéa, et art. 7. Mêmes
  fascicules et pages qu'en D2. **Lu à l'image, deux éditions.**
- **Citations.** Français, art. 5 : « La moyenne de revenu mensuel mentionnée au premier alinéa
  du présent article est majorée d'un demi salaire minimum interprofessionnel des différentes
  professions si un des membres de la famille est lourdement handicapé. » Arabe : « ويرفّع معدّل
  الدخل الشهري المشار إليه بالفقرة الأولى من هذا الفصل بنصف الأجر الأدنى المضمون لمختلف المهن
  إذا كان أحد أفراد الأسرة في الكفالة من ذوي الإعاقة العميقة. »
  Français, art. 7 : « Le demandeur du bénéfice ou l'un des membres de sa famille au sens du
  deuxième alinéa de l'article 5 du présent décret gouvernemental, ne doit pas avoir réalisé des
  opérations d'achat ou de vente dont la valeur dépasse 30 fois le salaire minimum, au cours des
  trois dernières années qui ont précédé la date de dépôt de la demande. » Arabe : « على معنى
  الفقرة الثانية من الفصل 5 ».
- **Raisonnement.** L'article 7 appelle « deuxième alinéa de l'article 5 » l'alinéa qui définit
  les membres de la famille (« Il est pris en considération dans la détermination du nombre des
  membres de la famille… »). Le premier alinéa est donc la phrase d'ouverture avec ses quatre
  tirets, et la « moyenne de revenu mensuel mentionnée au premier alinéa » désigne le plafond,
  quel que soit le tiret. Rien dans le texte ne réserve la majoration à un palier.
- **Deux réserves à écrire.** (1) L'édition arabe ajoute « في الكفالة » : le membre lourdement
  handicapé doit être **à charge** ; l'édition française dit seulement « un des membres de la
  famille ». L'arabe fait foi. (2) Le plafond est en même temps « aucun revenu ou… » : la
  majoration relève un plafond, non un montant versé.
- **Ce que cela change au plan.** Le tableau des plafonds avec un membre lourdement handicapé
  (`…/eligibilite/handicap_lourd/*`) peut être engendré, sous la même réserve que D2 sur le
  régime du salaire minimum. Le paragraphe « Ce chapitre ne tranche pas cette lecture » peut
  être remplacé par la règle, avec la précision « à charge » de l'édition arabe. Le désaccord
  signalé au § 8 du plan tombe si la revue admet le décompte des alinéas.

## 4. D5 — Le seuil de score

**Réponse.** Aucun texte publié au *Journal officiel* ne fixe de seuil de score ni de
pondérations : la loi organique renvoie à un arrêté, et l'arrêté du 19 mai 2020 ne donne que les
dimensions du modèle. La circulaire n° 12 de mai 2022 n'a pas pu être lue ; elle n'est pas
établie par cette note.

- **Textes publiés.**
  - Loi organique n° 2019-10 du 30 janvier 2019, art. 2, alinéas 2 et 3 (JORT n° 11 du 5 février
    2019, p. 276, <https://www.pist.tn/jort/2019/2019F/Jo0112019.pdf>, couche texte) : « Le
    ministère chargé des affaires sociales instaure un modèle de score sur la base des dimensions
    de privation susvisées au premier alinéa du présent article, en vue d'identifier les
    catégories éligibles au programme « AMEN SOCIAL » et de les classer en catégories pauvres et
    en catégories à revenu limité. Le modèle de score est fixé par arrêté du ministre chargé des
    affaires sociales. »
  - Arrêté du ministre des affaires sociales du 19 mai 2020 relatif au modèle de score (JORT
    n° 45 du 20 mai 2020, **édition arabe p. 1251, lue à l'image** ; pagination française non
    relevée) : art. 2, le modèle « يعتمد … على اختبار "سبل المعيشة البديلة PMT" ويستند على مفهوم
    الفقر متعدد الأبعاد » et énumère sept familles de caractéristiques (démographiques,
    géographiques, éducation, santé, situation professionnelle et économique, logement, proximité
    des services publics de base) ; art. 3 : « يتم تحيين أنموذج التنقيط كل خمس سنوات وكلّما دعت
    الحاجة إلى ذلك ». **Ni seuil, ni décile, ni coefficient.** Traduction de travail : « le
    modèle de score est actualisé tous les cinq ans et chaque fois que nécessaire ».
  - Décret gouvernemental n° 2020-317, art. 9 (arabe p. 1248, lu à l'image) : outre les
    conditions de l'article 5, « يتمّ تطبيق أنموذج التنقيط » pour désigner et classer les
    bénéficiaires.
- **La circulaire.** Adresse de la notice du paramètre,
  `http://www.ijtimaia.tn/fileadmin/Nouveau%20dossier/Circulaire12.PDF` : redirection 302 vers
  une adresse mal formée de `social.gov.tn` ; `https://www.social.gov.tn/fileadmin/Nouveau%20dossier/Circulaire12.PDF` :
  connexion refusée par la vérification du certificat (non contournée : l'autorisation ne vaut
  que pour pist.tn) ; archives du web : aucune capture par l'interface de disponibilité (réponse
  429 à la seconde requête), 404 sur l'adresse directe. Une recherche en ligne renvoie, sans que
  la page ait pu être ouverte, à la rubrique « التشريعات » du site du ministère et à un intitulé
  « منشور عدد 12 بتاريخ 10 ماي 2022 … الإجراءات العملية للانتفاع بالمنحة الشهرية القارة والعلاج
  المجاني والعلاج بالتعريفة المنخفضة ضمن برنامج الأمان الاجتماعي » : **date du 10 mai, non du
  12**, objet « procédures pratiques du bénéfice du transfert mensuel, des soins gratuits et des
  soins à tarif réduit » — résumé de moteur de recherche, non vérifié, à ne pas citer.
- **Ce que disent les rapports de la Banque mondiale (extérieurs, non normatifs).** Le
  financement additionnel de 2022 décrit les nouveaux bénéficiaires comme ceux « who meet the
  eligibility criteria and have score below the first decile » (§ 34, PDF 25, p. 20). Les critères ont ensuite été révisés par une
  circulaire d'octobre 2025 — « Circular No. 5 on October 3, 2025 » (ISR04716, p. 2) ou
  « Ministerial Circular No. 53, issued in October 2025 » (PPIAF000292, § 4) : **la circulaire de
  2022, si elle fixait le seuil, n'est plus le dernier état.**
- **État.** Seuil : **non identifié dans un texte publié.** Fiche proposée
  `r-amen-seuil-score-circulaires` (§ 8).
- **Ce que cela change au plan.** Le chapitre peut dire, sourcé : le classement par un score est
  prévu par la loi organique, le modèle est fixé par arrêté, l'arrêté publie les dimensions et
  non le seuil. Il ne peut pas écrire « premier décile » comme règle de droit ; il peut le
  rapporter comme description par la Banque mondiale, dans la section d'études. Le paramètre
  `amen_social/decile` repose sur une circulaire non lue, d'une date incertaine (10 ou 12 mai),
  et révisée en octobre 2025 : constat pour `backlog-modele.md`.

## 5. D11 et D4 — Supplément de 10 D et allocation de 30 D des 6-18 ans

**Réponse à D11.** Aucun texte publié ne règle le cumul : depuis le 1er février 2022 le
supplément de 10 D vise exactement la même tranche d'âge (6 à 18 ans) que l'allocation de 30 D
instituée en 2025, l'arrêté du 3 novembre 2025 ne modifie ni n'abroge l'alinéa du supplément et
ne le vise pas ; les arrêtés de 2023, 2024, 2025 et 2026 ne touchent que l'alinéa 1. Pendant le
pilote de 2022-2023, le ministère écrit que les deux **ne se cumulaient pas** : le don complétait
le supplément à hauteur de 30 D.

- **Textes, tous lus en couche texte dans l'édition française, sauf mention.**
  - Arrêté conjoint du 19 mai 2020 (transferts directs), art. 2, rédaction d'origine (JORT n° 45
    du 20 mai 2020, **arabe p. 1251, lu à l'image**) : « منحة إضافية قدرها 10 دنانير شهريا لكل أسرة
    بعنوان كلّ ابن في الكفالة سنّه دون 18 سنة دون أي شرط وإلى حدود سن 25 سنة … ويضاعف مقدار المنحة
    الإضافية مرة واحدة بعنوان كل طفل حامل لبطاقة إعاقة » — traduction de travail : supplément de
    10 D par mois pour chaque enfant à charge de moins de 18 ans, sans condition, et jusqu'à
    25 ans en cas d'études ou de formation ; doublé pour l'enfant titulaire d'une carte de
    handicap. Le document de projet de la Banque mondiale le résume à tort en supplément « per
    0-5 years-old-child » (§ 1.2).
  - Arrêté du 1er avril 2022 modifiant l'arrêté du 19 mai 2020 (JORT n° 38 du 8 avril 2022,
    p. 972-973, <https://www.pist.tn/jort/2022/2022F/Jo0382022.pdf>), article premier : « alinéa 2
    (nouveau) : Une allocation supplémentaire égale à 10 dinars au titre de chaque enfant à
    charge âgé de 6 ans et ne dépassant pas l'âge de 18 ans sans condition, jusqu'à l'âge de
    25 ans aux enfants à charge justifiant la poursuite d'études, d'apprentissage ou d'une
    formation professionnelle et ce à compter du 1er février 2022. Le montant de l'allocation
    supplémentaire est doublé au titre de chaque enfant titulaire d'une carte de handicap. »
  - Arrêté du 1er avril 2022 fixant les allocations familiales (même fascicule, p. 973), art. 2
    et 3 : enfants à charge « âgés de moins de six (6) ans » ; « trente (30) dinars par mois » ;
    exclusion des catégories à revenu limité affiliées à un régime de sécurité sociale. Sans
    clause d'effet ; fascicule déposé au gouvernorat de Tunis le 8 avril 2022 (mention finale),
    donc exécutoire le 13 avril 2022.
  - Décret n° 2025-426 du 2 octobre 2025 (JORT n° 121 du 3 octobre 2025, p. 2518,
    <https://www.pist.tn/jort/2025/2025F/Jo1212025.pdf>) : citation en D0. **Il ne vise que la
    Constitution** : ni la loi organique n° 2019-10, ni l'arrêté de 2020.
  - Arrêté conjoint du 3 novembre 2025 (JORT n° 132 du 4 novembre 2025, p. 2963,
    <https://www.pist.tn/jort/2025/2025F/Jo1322025.pdf>) : citation en D0. Visas : Constitution,
    loi organique n° 2019-10 complétée par le décret-loi n° 2022-8, décret n° 2025-426. **L'arrêté
    du 19 mai 2020 n'est pas visé.**
  - Arrêtés des 3 avril 2023, 28 février 2024, 29 janvier 2025 et 21 avril 2026 : chacun abroge
    et remplace « l'alinéa 1 de l'article 2 » seulement (JORT n° 34 de 2023, n° 33 de 2024, n° 12
    de 2025, n° 40 de 2026 ; couche texte). L'alinéa 2 nouveau de 2022 est donc toujours en
    vigueur dans sa lettre.
- **Pratique administrative du pilote (rapport du ministère pour 2023, PDF 37, couche texte
  arabe, traduction de travail).** « وينتفع أبناء العائلات المنتفعة ببطاقة علاج مجاني بمبلغ شهري
  قدره 30 دينار للطفل و50 دينار للطفل من ذوي الإعاقة. أمّا بالنسبة لأبناء العائلات المنتفعة بالمنحة
  الشهرية القارّة، فقد تقرّر إسنادهم 20 دينار على حساب الهبة إضافة إلى 10 دينار مموّلة من ميزانية
  الوزارة و30 دينار إضافية للطفل من ذوي الإعاقة. » — les enfants des familles titulaires de la
  carte de soins reçoivent 30 D par mois (50 D pour l'enfant handicapé) ; pour ceux des familles
  du transfert mensuel, « il a été décidé de leur attribuer 20 D sur le don, en plus de 10 D
  financés par le budget du ministère, et 30 D supplémentaires pour l'enfant handicapé ».
  L'ordre des mots de la couche texte arabe est perturbé : **à confirmer à l'image** avant
  citation.
- **État.** Règle de cumul depuis 2025 : **non identifiée** (fiche proposée
  `r-amen-cumul-supplement-6-18`, § 8).
- **Ce que cela change au plan.** Le chapitre peut écrire trois choses sûres : la tranche d'âge
  est la même ; l'arrêté de 2025 se tait ; pendant le pilote le total était de 30 D par enfant
  pour les familles du transfert. Il ne peut pas écrire 40 D ni 30 D comme règle depuis 2025.
  Les tableaux engendrés du supplément et de l'allocation des 6-18 ans doivent rester deux
  tableaux, avec la réserve entre eux.

**Réponse à D4.** Les 422 542 enfants de 6 à 18 ans aidés en décembre 2023 le sont au titre
d'un **second programme pilote d'allocation familiale financé par un don**, non d'un texte
publié.

- **Libellés (rapport du ministère, § 6.2, PDF 37-38, couche texte, traduction de travail).**
  Titre : « المنحة العائلية بعنوان الأطفال الذين تتراوح أعمارهم بين 6 و18 سنة ». Fondement :
  « تمّ الشروع في إنجاز برنامج نموذجي ثان يتعلق بالمنحة العائلية في إطار تنفيذ الاتفاقية الممضاة
  بتاريخ 28 سبتمبر 2022 بين وزارة الشؤون الاجتماعية والوكالة الأمريكية للتنمية الدولية (USAID)
  وبرنامج الأمم المتحدة للطفولة » — convention du 28 septembre 2022 entre le ministère, l'USAID et
  l'UNICEF, pour deux programmes financés par la banque allemande de développement et par
  l'USAID, « باعتماد قدره 191 مليون دينار منها 188 مليون دينار بعنوان التحويلات المالية (المنح
  العائلية والمساعدات المدرسية) » de septembre 2022 à décembre 2023, visant « حوالي 418 ألف طفل ».
  Total de décembre 2023 : 217 157 familles, 422 542 enfants, 124,6 millions de dinars
  « ممول عن طريق الهبة المذكورة ».
- **Recoupement.** UNICEF 2024 : démarrage en juillet 2022, 422 683 enfants en décembre 2023,
  « le programme pour les enfants de 6 à 18 ans ne l'est pas encore » institutionnalisé (p. 19,
  note 4). Deux dates de départ coexistent : juillet 2022 (UNICEF) et convention du 28 septembre
  2022 couvrant « de septembre 2022 » (ministère).
- **Ce que cela change au plan.** L'allocation des 6-18 ans a une préhistoire de pilote
  (2022-2024) à dire dans la sous-section N3 avant le décret de 2025 ; la série des enfants
  aidés se trace en deux segments, don puis budget. Recommandation de l'architecte (« étape de
  N3 ») confortée : même montant, même public, institutionnalisation en 2025.

## 6. D6 — Ce que les textes disent chercher, dans leurs propres mots

Constat d'ensemble : **aucun de ces textes ne porte d'exposé des motifs au *Journal officiel*** ;
les lois renvoient en note à leurs « travaux préparatoires » (séance d'adoption), sans plus.
L'objet se lit dans l'intitulé, dans les rubriques et dans l'article premier ; plusieurs lois
modificatives n'en disent rien au-delà de leur dispositif, ce qui est dit ci-dessous.

| Texte | JORT (édition française) | État | Intitulé, rubriques, objet, mot pour mot |
|---|---|---|---|
| **Loi n° 60-30 du 14 décembre 1960** | n° 57 des 13-16 décembre 1960, p. 1602-1613 ; <https://www.pist.tn/jort/1960/1960F/Jo05760.pdf> | lu à l'image (p. 1602, 1606-1608, 1612-1613) | Intitulé : « relative à l'organisation des régimes de Sécurité Sociale ». « TITRE PREMIER — Organisation générale de la Sécurité Sociale », « Chapitre 1er — Dispositions générales ». **Art. 1er** : « Il est institué une organisation de la Sécurité Sociale, destinée à protéger les travailleurs et leur famille contre les risques inhérents à la nature humaine, susceptibles d'affecter les conditions matérielles et morales de leur existence. » **Art. 2** : « Cette organisation assure, en faveur des travailleurs salariés, dans le cadre des prescriptions fixées par la présente loi, le service des prestations définies par un régime de prestations familiales et un régime d'assurances sociales. » « TITRE II — Les régimes de sécurité sociale » ; « Chapitre 1er — Les prestations familiales » (art. 51 : « Les prestations familiales prévues par la présente loi comprennent : 1° les allocations familiales ; 2° les allocations pour congés de naissance ; 3° les allocations pour congés de jeunes travailleurs ») ; « Section I — Les allocations familiales » (art. 52-65) ; « Section II — Allocations pour congés de naissance » (art. 66) ; « Section III — Allocations pour congés de jeunes travailleurs » (art. 67) ; « Chapitre II — Les assurances sociales » (art. 68 : « Les assurances sociales comprennent : 1° des indemnités en espèces, en cas de maladie, de maternité ou de décès, dont le service est assuré par la Caisse Nationale ; 2° l'octroi des soins, en cas de consultations ou d'hospitalisation dans les établissements sanitaires et hospitaliers relevant du Secrétariat d'État à la Santé Publique et aux Affaires Sociales ») ; « Section I — Prestations en espèces », « Sous-section I — Indemnités de maladie » (art. 71 et suivants). Les intitulés des subdivisions des art. 76 à 98 n'ont pas été relevés (p. 1609-1610 non lues). Note : « Projet de loi n° 60-26-1. Discussion et adoption par l'Assemblée Nationale dans sa séance du 6 décembre 1960 ». |
| **Loi n° 75-82 du 30 décembre 1975** | n° 87 des 30-31 décembre 1975, p. 2852 ; <https://www.pist.tn/jort/1975/1975F/Jo08775.pdf> | lu à l'image | Intitulé : « modifiant la loi numéro 60-30 du 14 décembre 1960, relative à l'organisation des régimes de sécurité sociale ». **Le texte ne dit pas son objet** : article premier remplaçant le deuxième alinéa de l'art. 61 — « Le montant trimestriel de l'allocation est calculé en pourcentage de la rémunération globale trimestrielle du travailleur plafonnée à 72 D, 000 soit : 18 % pour le premier enfant, 16 % pour le deuxième enfant, 14 % pour le troisième enfant, 12 % pour le quatrième enfant. » Art. 2 : effet au 1er janvier 1976. Séance du 29 décembre 1975. |
| **Loi n° 80-36 du 28 mai 1980** | n° 32 des 27-30 mai 1980, p. 1478 ; <https://www.pist.tn/jort/1980/1980F/Jo03280.pdf> | lu à l'image | Intitulé : « complétant la loi n° 60-30 du 14 décembre 1960, organisant les Régimes de Sécurité Sociale ». Rubrique créée : « **SECTION I bis — Majoration pour Salaire Unique** », ajoutée au chapitre 1er du titre II. Art. 65 bis : « Il est attribué à l'assuré ayant des enfants à charge au sens de l'article 53 précédent ouvrant droit au bénéfice des allocations familiales et dont le conjoint n'exerce aucune activité professionnelle une indemnité dite « majoration pour salaire unique » dont le montant trimestriel est de : 9d,375 si le foyer comporte un enfant à charge, 18d,750 si le foyer comporte 2 enfants à charge, 23d,475 si le foyer comporte 3 enfants ou plus à charge. » « La Caisse Nationale de Sécurité Sociale se substitue aux employeurs affiliés qui assurent à leurs salariés, à la date de la promulgation de la présente loi le service d'une indemnité de même nature dans la limite des taux sus-mentionnés. » Art. 2 : effet au 1er mai 1980. Pas d'objet au-delà de la rubrique. Séance du 21 mai 1980. |
| **Loi n° 88-38 du 6 mai 1988** | n° 33 des 13-17 mai 1988, p. 735 ; <https://www.pist.tn/jort/1988/1988F/Jo03388.pdf> | lu à l'image | Intitulé : « complétant et modifiant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale ». **Le texte ne dit pas son objet.** Art. 52, alinéa 2 nouveau : « Elles ne sont dues que pour les trois premiers enfants du travailleur ou ceux adoptés par lui ou vis-à-vis desquels il exerce le droit de garde et dans la mesure où ils sont à sa charge. » Art. 61, alinéa 2 nouveau : rémunération « plafonnée à 122,000 soit : 18 % pour le premier enfant ; 16 % pour le deuxième enfant ; 14 % pour le troisième enfant ». Art. 5 : « Les dispositions de l'article premier de la présente loi entrent en vigueur à partir du 1er janvier 1989, les droits acquis antérieurement à cette date sont maintenus. » La loi modifie aussi l'art. 110 (prescription) et ajoute un art. 111 bis. Séance du 3 mai 1988. |
| **Loi n° 88-39 du 6 mai 1988** | même fascicule, p. 735 | lu à l'image | Intitulé : « relative à l'octroi des indemnités familiales dans le secteur public ». Article unique : « L'indemnité familiale est servie aux agents de l'État, des collectivités publiques locales, des établissements publics des offices et des sociétés nationales autres que ceux soumis au régime de sécurité sociale institué par la loi n° 60-30 du 14 décembre 1960, dans les conditions et selon les modalités prévues par le décret du 22 novembre 1918 tel qu'amendé ou modifié par les textes subséquents, et dans la limite des trois premiers enfants. Le montant des indemnités est fixé par décret. Les dispositions de la présente loi ne s'appliquent pas aux droits acquis antérieurement au 1er janvier 1989. » Pas d'objet au-delà. |
| **Loi n° 89-73 du 2 septembre 1989** | n° 60 des 5-8 septembre 1989, p. 1338-1339 ; <https://www.pist.tn/jort/1989/1989F/Jo06089.pdf> | lu à l'image | Intitulé : « modifiant et complétant la loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole ». Rubrique créée : « **Titre III : Dispositions particulières applicables aux salariés employés par certaines entreprises agricoles** » (art. 86 à 101 nouveaux). Art. 91 : « Les assurés soumis au régime prévu par le présent titre, bénéficient des prestations prévues par la présente loi ainsi que des allocations familiales. » Art. 92 : allocations « servies du chef des trois premiers enfants de l'assuré selon les mêmes conditions et aux mêmes taux que ceux prévus par les articles 52 à 65 de la loi n° 60-30 ». Art. 90 : cotisation de 15 % (10 % employeur, 5 % salarié ou coopérateur). Art. 4 : « La présente loi entrera en vigueur le 1er octobre 1989. » Le plan dit « régime agricole amélioré » : **l'expression n'est pas dans la loi**. Séance du 29 août 1989. |
| **Loi n° 94-88 du 26 juillet 1994** | n° 60 du 2 août 1994, p. 1255 ; <https://www.pist.tn/jort/1994/1994F/Jo06094.pdf> | couche texte | Intitulé : « relative à la contribution aux frais de prise en charge des enfants dans les crèches ». **Art. 1er** : « Est instituée une contribution aux frais de prise en charge des enfants dans les crèches autorisées par le ministère de tutelle conformément à un cahier des charges établi à cet effet et adopté par décret. » Art. 2 : « La contribution est servie au titre des enfants des assurées sociales et des affiliées aux caisses de sécurité sociale dont le salaire mensuel y compris les indemnités ne dépasse pas un montant qui sera fixé par décret. » Art. 4 : servie « directement à la crèche », enfants de « deux et trente six mois », « onze mois par année ». Aucune rubrique. Sans clause d'effet. Séance du 19 juillet 1994. |
| **Loi n° 94-28 du 21 février 1994** | n° 15 du 22 février 1994, p. 308-318 ; <https://www.pist.tn/jort/1994/1994F/Jo01594.pdf> | couche texte | Intitulé : « portant régime de réparation des préjudices résultant des accidents du travail et des maladies professionnelles ». « TITRE PREMIER — Dispositions générales ». **Art. 1er** : « Il est institué un régime de réparation des préjudices résultant des accidents du travail et des maladies professionnelles au profit des victimes ou de leurs ayants droit. La réparation se fait conformément aux conditions et procédures prévues par la présente loi. » Art. 2 : gestion « confiée à la Caisse Nationale de Sécurité Sociale ». |
| **Loi n° 95-56 du 28 juin 1995** | n° 53 du 4 juillet 1995, p. 1419-1424 ; <https://www.pist.tn/jort/1995/1995F/Jo05395.pdf> | couche texte | Intitulé : « portant régime particulier de réparation des préjudices résultant des accidents de travail et des maladies professionnelles dans le secteur public ». « TITRE PREMIER — DISPOSITIONS GENERALES ». **Art. 1er** : « Il est institué un régime particulier de réparation des préjudices résultant des accidents de travail ou des maladies professionnelles au profit des agents du secteur public ou de leurs ayants droit. » Art. 2 : agents affiliés à la CNRPS, « à l'exclusion des militaires et des forces de sécurité intérieures ». |
| **Loi n° 96-101 du 18 novembre 1996** | n° 94 du 22 novembre 1996, p. 2319-2320 ; <https://www.pist.tn/jort/1996/1996F/Jo09496.pdf> ; rectificatif au JORT n° 7 du 24 janvier 1997, p. 114 (non lu) | couche texte | Intitulé : « relatif [sic] à la protection sociale des travailleurs ». **Art. 1er** : « La présente loi a pour objet de déterminer les mesures de la protection sociale en faveur des travailleurs ayant cessé leur travail pour des raisons économiques ou technologiques. » « CHAPITRE I — La prise en charge des indemnités de licenciement pour raisons économiques ou technologiques » (art. 2-6 ; art. 5 : « une cotisation complémentaire de 0,4 % des salaires à prélever sur le taux global des cotisations de sécurité sociale ») ; « CHAPITRE II — Octroi des prestations familiales et de soins en faveur des travailleurs ayant cessé leur travail pour des raisons économiques ou technologiques » (art. 7 : maintien des allocations familiales et de la majoration pour salaire unique « au titre des quatre trimestres suivant celui au cours duquel ils ont cessé leur activité »). **La loi ne parle ni d'« assurance chômage » ni de « perte d'emploi »** : le titre de la rupture au plan doit reprendre ses mots. Séance du 12 novembre 1996. |
| **Loi n° 2004-71 du 2 août 2004** | n° 63 du 6 août 2004, p. 2228-2230 ; <https://www.pist.tn/jort/2004/2004F/Jo0632004.pdf> | couche texte décodée (police décalée) : accents et apostrophes à relire à l'image | Intitulé : « portant institution d'un régime d'assurance maladie ». « TITRE PREMIER — DISPOSITIONS GENERALES ». **Art. 1er** : « Il est institué un régime d'assurance maladie, au profit des assurés sociaux et de leurs ayants droit, fondé sur les principes de la solidarité et l'égalité des droits dans le cadre d'un système sanitaire complémentaire qui englobe les prestations servies dans les secteurs public et privé de la santé. » Art. 2 : « un régime de base obligatoire et des régimes complémentaires facultatifs ». Art. 3 : « Les étapes d'application de la présente loi pour les différentes catégories d'assurés sont fixées par décret. » |
| **Décret n° 2007-1366 du 11 juin 2007** | n° 47 du 12 juin 2007, p. 1982-1983 ; <https://www.pist.tn/jort/2007/2007F/Jo0472007.pdf> | couche texte | Intitulé : « portant détermination des étapes d'application de la loi n° 2004-71 du 2 août 2004, portant institution d'un régime d'assurance maladie aux différentes catégories d'assurés sociaux mentionnés dans les différents régimes légaux de sécurité sociale ». **Art. 1er** : « A compter du 1er juillet 2007, les dispositions de la loi n° 2004-71 … s'appliquent aux assurés sociaux ci-après mentionnées » : affiliés à la CNRPS ; affiliés à la CNSS des régimes des salariés non agricoles (loi n° 60-30), agricole (loi n° 81-6 modifiée par la loi n° 89-73), des artistes (loi n° 2002-104), des travailleurs tunisiens à l'étranger (décret n° 89-107), des non-salariés (décret n° 95-1166). Art. 2 : extension possible « dans une étape ultérieure ». |
| **Loi n° 2024-44 du 12 août 2024** | n° 99 du 12 août 2024, p. 2215 et suivantes ; <https://www.pist.tn/jort/2024/2024F/Jo0992024.pdf> | couche texte | Intitulé : « relative à l'organisation des congés de maternité et de paternité dans la fonction publique et les secteurs public et privé ». « Titre Premier — Dispositions générales ». **Art. 1er** : « Les dispositions de la présente loi s'appliquent à tous les agents de la fonction publique et du secteur public affiliés à la Caisse nationale de retraite et de prévoyance sociale et aux salariés et non-salariés du secteur privé affiliés et déclarés à la Caisse nationale de sécurité sociale. » Art. 2 : définitions (congé prénatal, postnatal, de paternité, d'accouchement, repos d'allaitement). « Titre II — Des congés de maternité et de paternité ». La loi dit son champ, non un but. Séance du 31 juillet 2024. |
| **Loi n° 86-83 du 1er septembre 1986, art. 13** | n° 48 des 2-5 septembre 1986, p. 928 ; <https://www.pist.tn/jort/1986/1986F/Jo04886.pdf> | lu à l'image | Loi de finances rectificative pour la gestion 1986. « Chapitre 3 — Dispositions diverses », rubrique « **Contribution des organismes de sécurité sociale pour l'aide aux familles nécessiteuses** ». Art. 13 : « Les organismes de sécurité sociale, y compris la caisse de retraite du personnel des services publics de l'électricité, du gaz et du transport sont autorisés à participer au financement du programme national d'aide aux familles nécessiteuses. La contribution annuelle de chaque organisme sera fixée par arrêté conjoint des ministres des affaires sociales et du plan et des finances. » |
| **Loi n° 87-29 du 12 juin 1987** | n° 43 du 16 juin 1987, p. 767 ; <https://www.pist.tn/jort/1987/1987F/Jo04387.pdf> | lu à l'image | Intitulé : « relative au régime de l'assistance médicale gratuite ». Aucune rubrique. **Art. 1er** : « Le bénéfice de l'assistance médicale gratuite dans les établissements publics hospitaliers et sanitaires relevant du ministère de la santé publique est accordé aux titulaires de livrets de soins délivrés par les services du ministère de la santé publique. Il est institué deux catégories de livrets d'assistance médicale gratuite. Ils sont délivrés en fonction du revenu de la famille et ouvrent droit à la gratuité des soins et de l'hospitalisation… » Art. 2 : « droit annuel d'affiliation », dont « les titulaires de livrets … de première catégories [sic] sont exonérés ». Art. 4 : effet « à compter du 1er janvier 1988 ». **Coquille du fascicule** : la formule finale porte « Fait à Mornag, le 12 juin 1986 » alors que l'intitulé dit 1987. Séance du 9 juin 1987. |
| **Décret n° 98-409 du 18 février 1998** | n° 17 du 27 février 1998, p. 405-408 ; <https://www.pist.tn/jort/1998/1998F/Jo01798.pdf> | couche texte | Intitulé : « fixant les catégories des bénéficiaires des tarifs réduits de soins et d'hospitalisation dans les structures sanitaires publiques relevant du ministère de la santé publique ainsi que les modalités de leur prise en charge et les tarifs auxquels ils sont assujettis ». Art. 1er : reprend l'intitulé. « Chapitre premier — Les catégories des bénéficiaires des tarifs réduits et les modalités de leur prise en charge ». Art. 2 : revenu annuel de la famille en multiples du salaire minimum ; non-affiliation ; « dans la limite du nombre global des cartes et des quotas régionaux ». |
| **Décret n° 98-1812 du 21 septembre 1998** | n° 78 du 29 septembre 1998, p. 1975-1976 ; <https://www.pist.tn/jort/1998/1998F/Jo07898.pdf> | couche texte | Intitulé : « fixant les conditions et les modalités d'attribution et de retrait de la carte de soins gratuits ». Art. 2 : « Le bénéfice de la gratuité des soins et de l'hospitalisation … est accordé à tout tunisien indigent, à son conjoint et à ses enfants légalement à charge. … La carte de soins gratuits est attribuée dans la limite du nombre global de cartes de soins gratuits et des quotas régionaux qui sont fixés par arrêté conjoint des ministres des affaires sociales et de la santé publique. » |
| **Loi organique n° 2019-10 du 30 janvier 2019** | n° 11 du 5 février 2019, p. 276 et suivantes ; <https://www.pist.tn/jort/2019/2019F/Jo0112019.pdf> | couche texte | Intitulé : « relative à la création du programme « AMEN SOCIAL » ». « Chapitre premier — Dispositions générales ». **Art. 1er** : « Il est créé en vertu de la présente loi un programme “AMEN SOCIAL” …, pour la promotion des catégories pauvres et des catégories à revenu limité. » Art. 2 : « les individus ou les familles qui souffrent de privation multidimensionnelle touchant le revenu, la santé, l'éducation, le logement, l'accès aux services publics et les conditions de vie ». « Chapitre II — Du programme « AMEN SOCIAL » ». **Art. 7** : « Le programme « AMEN SOCIAL » a pour but de : garantir le droit à un revenu minimum et le droit aux prestations de soins au profit des catégories pauvres et des catégories à revenu limité ; promouvoir les catégories pauvres et les catégories à revenu limité, améliorer leurs conditions de vie et assurer leur accès aux services de base tels que les soins, l'éducation, l'enseignement, la formation professionnelle, l'emploi, le logement et le transport ; renforcer les mécanismes d'inclusion et d'autonomisation économique et concrétisation du principe de « compter sur soi-même » ; réduire la pauvreté, d'éviter d'y retomber et de la transmettre de génération en génération ; lutter contre l'exclusion, de réduire les disparités sociales et régionales, renforcer l'égalité des chances et consacrer la justice sociale et la solidarité. » « Chapitre III — Les prestations allouées aux bénéficiaires du programme “AMEN SOCIAL” » : « Section première — Les transferts et le soutien financier » ; « Section 2 — Les prestations de soins » ; « Section 3 — Les mécanismes d'inclusion et d'autonomisation économique ». Séance du 16 janvier 2019. **L'article 7, non relevé par le plan, est l'énoncé de but le plus complet du volume.** |
| **Décret gouvernemental n° 2020-317 du 19 mai 2020** | n° 45 du 20 mai 2020, p. 1092-1096 ; <https://www.pist.tn/jort/2020/2020F/Jo0452020.pdf> | lu à l'image (p. 1092-1093) | Intitulé : « fixant les conditions et les procédures de bénéfice, de retrait et d'opposition au programme « AMEN SOCIAL » ». « Chapitre premier — Dispositions générales » ; art. 1er : reprend l'intitulé, « prévu par l'article 8 de la loi organique » ; art. 2 : s'applique « aux catégories pauvres et aux catégories à revenu limité ». « Chapitre II — Conditions de bénéfice du programme « AMEN SOCIAL » » (art. 3 : conditions « relatives à l'âge, au revenu et aux propriétés »). Chapitre III (arabe) : « إجراءات الإنتفاع ببرنامج الأمان الإجتماعي ». Texte de procédure : pas de but propre. |
| **Décret-loi n° 2022-8 du 31 janvier 2022** | n° 13 du 2 février 2022, p. 336 ; <https://www.pist.tn/jort/2022/2022F/Jo0132022.pdf> | couche texte | Intitulé : « complétant la loi organique n° 2019-10 du 30 janvier 2019, relative à la création du programme « AMEN SOCIAL » ». Visas : Constitution ; décret présidentiel n° 2021-117 du 22 septembre 2021 relatif aux mesures exceptionnelles. **Art. 11 bis** : « Les catégories pauvres et les catégories à revenu limité bénéficient d'une allocation familiale payable mensuellement, au titre des enfants âgés de moins de 6 ans. Les situations d'octroi et le montant de l'allocation familiale précitée, sont fixés par arrêté conjoint du ministre chargé des affaires sociales et du ministre chargé des finances. » **Le texte ne dit pas son objet** et ne vise aucun accord de prêt ; c'est l'arrêté du 1er avril 2022 sur les allocations familiales qui vise la loi n° 2021-28 du 22 juin 2021 approuvant l'accord de prêt du 2 avril 2021 (p. 973, couche texte ; citation au § 1.7). |
| **Décret n° 2025-426 du 2 octobre 2025** | n° 121 du 3 octobre 2025, p. 2518 ; <https://www.pist.tn/jort/2025/2025F/Jo1212025.pdf> | couche texte | Voir D0. Rubrique « Ministère des affaires sociales ». Ni rubrique interne ni objet au-delà de l'article premier ; visas : Constitution seule. |

**Ce que cela change au plan.** La colonne « ce que la loi cherche » peut être remplie mot pour
mot pour : 1960 (art. 1er et 2), 1980 (rubrique « Majoration pour Salaire Unique »), 1989
(intitulé du titre III), 1994 crèches (art. 1er), 1994 et 1995 accidents du travail (art. 1er),
1996 (art. 1er), 2004 (art. 1er), 1986 (rubrique et art. 13), 1987 (art. 1er), 2019 (art. 1er et
7). Elle reste « le texte ne dit pas son objet » pour : lois n° 75-82, n° 88-38, n° 88-39,
décret-loi n° 2022-8, décret n° 2025-426, et la loi n° 2024-44 (champ et définitions seulement).

## 7. Les autres questions

### D0 — Note complémentaire pour `prestations-assistance.md`

Pour les cinq objets que le rédacteur lit lui-même, seulement la référence et la citation.

| Objet | Référence | Citation | État |
|---|---|---|---|
| (a) Exécution du décret gouvernemental n° 2020-317 et des arrêtés du 19 mai 2020 | JORT n° 45 du 20 mai 2020 ; mention finale de l'édition arabe, p. 1252 : « تم إيداع هذا العدد من الرائد الرسمي للجمهورية التونسية بمقر ولاية تونس العاصمة يوم 20 ماي 2020 » | Aucune clause d'effet dans le décret (art. 1 à 9 lus) ni dans l'arrêté sur les transferts (art. 1-3) ; dépôt le 20 mai 2020 ; exécutoires cinq jours après, jour du dépôt non compté : **25 mai 2020** (loi n° 93-64, art. 2). | lu à l'image (arabe) ; la mention de dépôt de l'édition française n'a pas été relue |
| Arrêté conjoint du 19 mai 2020, transferts directs, art. 2 | même fascicule, arabe p. 1251 (pagination française non relevée) | « مقدار أساسي للتحويل المالي بمبلغ قدره 180 دينار شهريًا للفرد أو للأسرة الواحدة » ; supplément : voir § 5 | lu à l'image (arabe) |
| Arrêté conjoint du 19 mai 2020, appui occasionnel, art. 4 | même fascicule, arabe p. 1252 | 60 D pour le Ramadan, 60 D pour l'Aïd el-Fitr, 60 D pour l'Aïd el-Idha, par individu ou famille ; « 50 دينارا بمناسبة العودة المدرسية بعنوان كل طفل متمدرس » ; « 120 دينارا بمناسبة العودة الجامعية » ; art. 3 : les catégories à revenu limité n'ont que l'appui de rentrée scolaire et universitaire | lu à l'image (arabe) |
| (b) Palier de 280 D | Arrêté conjoint du 21 avril 2026, JORT n° 40 du 21 avril 2026, p. 786, <https://www.pist.tn/jort/2026/2026F/Jo0402026.pdf> ; déposé le 21 avril 2026 | « Article 2 (l'alinéa 1 nouveau) - Un montant de base mensuel égal à 280 dinars servi pour l'individu ou pour la famille. » « Art. 2 - Le présent arrêté prend effet à compter du 1er janvier 2026. » | couche texte, édition française |
| (c) Allocation des 6-18 ans, institution | Décret n° 2025-426 du 2 octobre 2025, JORT n° 121 du 3 octobre 2025, p. 2518 | « Article premier - Il est institué une allocation familiale au profit des familles pauvres et à faible revenu au titre des enfants âgés de 6 ans à 18 ans. Les conditions d'attribution de la dite allocation familiale et son montant sont fixés par arrêté conjoint du ministre chargé des affaires sociales et du ministre chargé des finances. Art. 2 - Les dispositions de l'article premier du présent décret entrent en vigueur à compter du 1er janvier 2025. » | couche texte, édition française |
| (c) Allocation des 6-18 ans, montant | Arrêté conjoint du 3 novembre 2025, JORT n° 132 du 4 novembre 2025, p. 2963 ; déposé le 4 novembre 2025 | « Article premier - Le bénéfice de l'allocation familiale au titre des enfants âgés de 6 à 18 ans est subordonné à la condition que les familles pauvres et les familles à revenu limité bénéficient des avantages sociaux conformément au registre des données sociales prévus par la loi organique n° 2019-10… Les familles à revenu limité affiliées à l'un des régimes de sécurité sociale sont exclues… Art. 2 - Le montant de l'allocation familiale au titre des enfants âgés de 6 à 18 ans est fixé à trente (30) dinars par mois pour chaque enfant à charge. » Sans clause d'effet : exécutoire le **9 novembre 2025** ; le droit, lui, est ouvert au 1er janvier 2025 par le décret. | couche texte, édition française |
| (d) Majoration de handicap | voir D3 | voir D3 | lu à l'image, deux éditions |
| Arrêté du 5 août 2026 | voir D1 | voir D1 | couche texte |
| Rentrée scolaire à 100 D | Arrêté conjoint du 10 juillet 2025 modifiant l'arrêté du 8 décembre 2022, JORT n° 88 du 11 juillet 2025 ; l'index donne la p. 2058 (pagination arabe ; le plan le dit lu dans l'édition arabe) | non relu ici | non relu (laissé au rédacteur) |

À verser aussi : le décret n° 2025-426 parle de « familles pauvres et à faible revenu », l'arrêté
de « familles pauvres et familles à revenu limité » ; le vocabulaire de la loi organique est
« catégories pauvres et catégories à revenu limité ».

### D1 — Arrêté conjoint du 5 août 2026

**Réponse.** Il remplace l'article premier de l'arrêté du 10 juillet 2024 : l'allocation
monétaire des catégories pauvres, « fixée à 260 dinars à la date de la publication », est
relevée dans la limite du transfert de l'Amen social, « fixé à 280 dinars », avec effet au
1er janvier 2026 ; l'index ne connaît aucun arrêté analogue entre le 29 août 2025 et le
5 août 2026.

- **Texte.** Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du
  5 août 2026, JORT n° 80 du 7 août 2026, p. 1611-1612 (dispositif p. 1612),
  <https://www.pist.tn/jort/2026/2026F/Jo0802026.pdf> ; déposé le 7 août 2026. Couche texte,
  édition française.
- **Citation.** « Article premier (nouveau) : L'allocation monétaire mensuelle attribuée aux
  catégories pauvres conformément à la législation et à la règlementation en vigueur, fixée à
  260 dinars à la date de la publication du présent arrêté conjoint, est augmentée sans que le
  montant de cette allocation ne dépasse le montant des transferts monétaires mensuels directs
  attribués dans le cadre du programme « AMEN SOCIAL », fixé à 280 dinars. Art. 2 - Le présent
  arrêté entre en application à partir du 1er janvier 2026. »
- **À signaler au rédacteur.** Les visas (p. 1611-1612) citent la loi n° 2002-32, la loi
  n° 2003-8, la loi n° 2004-71, le décret-loi n° 2020-30 du 10 juin 2020 « notamment son article
  premier », les décrets n° 74-499, n° 95-1166, n° 2002-916 et n° 2003-1128 — des textes de
  pensions et de sécurité sociale —, avant le décret n° 2020-317 et les arrêtés de 2020 : l'objet
  « allocation monétaire attribuée aux catégories pauvres » n'est donc pas, par ses visas, le
  seul PNAFN. Le dispositif ne dit pas qui la perçoit. Le livre « Retraites » cite déjà la clé
  `arrete-2026-08-05-allocation-pauvres` : les deux volumes doivent dire la même chose.
- **Couverture de la recherche d'arrêtés analogues.** `jort_cache.db`, titres français et
  arabes (« AMEN SOCIAL », « الأمان الاجتماعي », « pauvres », « familles nécessiteuses »,
  « allocation familiale »), années 2022 à 2026, dernière publication indexée le 2 octobre 2026.
  Lacunes : les fascicules inconnus de la base (§ 1 f de la note d'outillage) n'ont pas été
  parcourus en plein texte.

### D7, D8, D10, D12, D13 — non traités

Budget consommé par le changement de priorité. État laissé :

- **D7** (lois de finances pour 2025, art. 26, et pour 2026, art. 35, 71, 81, 96) : non lus.
  L'index confirme les notices arabes : loi n° 2024-48 du 9 décembre 2024, JORT n° 149, art. 26
  (maladie cœliaque), pagination arabe 6425 ; loi n° 2025-17 du 12 décembre 2025, JORT n° 148,
  art. 35 (pagination arabe 4228 : allocation mensuelle de « 130 دينار لكل فرد » pour les
  personnes atteintes de xeroderma pigmentosum, d'après le résumé de la notice), art. 71
  (p. 4249, enfants diabétiques), art. 81 (p. 4252, autisme). L'article 96 n'apparaît pas dans
  les notices trouvées. Rappel : le fichier « fr » du n° 148 de 2025 du corpus est l'arabe.
- **D8** : non lu.
- **D10** : fiche `r-lf2025-art17-decret` non rejouée par l'outil (il réécrit le registre) ; une
  requête directe sur les titres de 2025-2026 (« article 17 de la loi … 2024-48 », « fonds …
  protection sociale », « الفصل 17 من القانون عدد 48 », « فقدان مواطن الشغل ») ne rend aucun
  candidat, index au 2 octobre 2026 — ce n'est pas une passe au sens de la fiche.
- **D12** et **D13** : non traités.

### D9 — Dates d'effet (partiel)

| Texte | Clause d'effet | Dépôt du fascicule | Date retenue | État |
|---|---|---|---|---|
| Loi n° 60-30, art. 68 à 98 | Art. 130 : « La présente loi entre en vigueur le 1er avril 1961, sauf en ce qui concerne les dispositions prévues par les articles 1 à 33, 119, 124 à 126 et 129, qui sont d'application immédiate. » | sans objet | **1er avril 1961** pour les art. 34 à 118 (donc 51 à 98) | lu à l'image, p. 1612 |
| Loi n° 96-65 du 22 juillet 1996 | aucune dans l'article unique (début lu ; fin de l'article non relue) | JORT n° 60 du 26 juillet 1996, mention : « déposé au siège du gouvernorat de Tunis le 30 juillet 1996 » | 4 août 1996 (cinq jours après le dépôt, jour du dépôt non compté), sous réserve de la fin de l'article | couche texte |
| Loi n° 96-101 du 18 novembre 1996 | aucune (onze articles parcourus ; art. 11 : abrogation des dispositions contraires) | mention de dépôt du JORT n° 94 non extraite | **non établie** : relever la mention de dépôt à l'image, puis + 5 jours ; lire aussi le rectificatif du JORT n° 7 de 1997 | couche texte |
| Loi n° 2002-32 du 12 mars 2002 | non vérifiée | JORT n° 22 du 15 mars 2002 : « déposé … le 16 mars 2002 » (couche texte décodée) | 21 mars 2002 si aucune clause : **à confirmer par lecture des articles finaux** | partiel |
| Loi n° 2002-104 du 30 décembre 2002 | non vérifiée pour la loi (les « prend effet » trouvés concernent l'option de l'assuré) | JORT n° 106 du 31 décembre 2002 : « déposé … le 31 décembre 2002 » | 5 janvier 2003 si aucune clause : **à confirmer** | partiel |
| Décret n° 95-1166 du 3 juillet 1995 | aucune clause générale repérée (art. 39 : abrogations) ; articles finaux non relus | JORT n° 55 du 11 juillet 1995 : « déposé … le 14 juillet 1995 » | 19 juillet 1995 si aucune clause : **à confirmer** | partiel |
| Décret n° 89-107 du 10 janvier 1989 | non lu | avant 1993 : un jour franc après la publication (JORT n° 4 du 17 janvier 1989) | non établie | non lu |
| Décret-loi n° 2024-4 du 22 octobre 2024 | non vérifiée | JORT n° 129 du 23 octobre 2024 : « déposé … le 23 octobre 2024 » | 28 octobre 2024 si aucune clause : **à confirmer** | partiel |

## 8. Recherches infructueuses — fiches proposées pour `docs/recherches.yml`

Aucune fiche existante ne couvre ces objets (lecture de `docs/recherches.yml` sur `origin/master`,
recherche des mots « amen », « score », « circulaire », « supplément », « 6-18 »). Les trois
fiches ci-dessous ne contiennent que ce qui a été fait.

```yaml
- id: r-amen-seuil-score-circulaires
  objet: circulaire du ministre des affaires sociales fixant le seuil de score (décile) ouvrant le transfert monétaire permanent de l'Amen social — circulaire n° 12 de mai 2022 (datée du 12 mai par la notice du paramètre, du 10 mai par un résumé de moteur de recherche), puis circulaire d'octobre 2025 révisant les critères (« Circular No. 5 on October 3, 2025 » selon le rapport de suivi ISR04716 de la Banque mondiale, « Ministerial Circular No. 53, issued in October 2025 » selon le document PPIAF000292)
  ou: site du ministère des affaires sociales (rubrique « التشريعات »), archives du web ; hors Journal officiel
  requetes:
    web:
      - "http://www.ijtimaia.tn/fileadmin/Nouveau%20dossier/Circulaire12.PDF"
      - "https://www.social.gov.tn/fileadmin/Nouveau%20dossier/Circulaire12.PDF"
      - "https://web.archive.org/web/2023id_/http://www.ijtimaia.tn/fileadmin/Nouveau%20dossier/Circulaire12.PDF"
      - "منشور عدد 12 لسنة 2022 وزير الشؤون الاجتماعية الأمان الاجتماعي التنقيط العشير الأول التحويلات المالية"
      - "Amen Social circulaire n° 12 du 12 mai 2022 ministre des affaires sociales score premier décile transferts monétaires permanents"
    titres_like:
      - "%AMEN SOCIAL%"
    iort_ar:
      - "الأمان الاجتماعي"
  passes:
    - date: 2026-10-09
      resultat: aucun
      couvert_jusqu_au: 2026-10-02
      couverture: >
        Journal officiel : titres français et arabes de jort_cache 2019-2026 (index au 2 octobre 2026) ; lus : loi organique
        n° 2019-10, art. 2 ; arrêté du 19 mai 2020 sur le modèle de score (arabe, p. 1251) ; décret gouvernemental n° 2020-317,
        art. 9 — aucun seuil. Hors Journal officiel : première adresse, redirection 302 vers une adresse mal formée ; deuxième,
        certificat non vérifiable (non contourné) ; archives du web, 404 sur l'adresse directe et 429 sur l'interface de
        disponibilité ; page « التشريعات » du ministère non ouverte (certificat). Lacunes : aucune circulaire lue ; fascicules
        inconnus de jort_cache non parcourus en plein texte.
      sources: [jort_cache, corpus_local, web]

- id: r-amen-smig-regime
  objet: texte, circulaire ou formulaire de demande disant quel régime du salaire minimum interprofessionnel garanti (48 ou 40 heures) sert de référence aux plafonds de ressources de l'article 5 du décret gouvernemental n° 2020-317 du 19 mai 2020 (et aux « 30 fois le salaire minimum » de l'article 7)
  ou: Journal officiel (modificatifs du décret) ; circulaires et formulaire du ministère des affaires sociales
  requetes:
    titres_like:
      - "%2020-317%"
    iort_ar:
      - "317 لسنة 2020"
  passes:
    - date: 2026-10-09
      resultat: aucun
      couvert_jusqu_au: 2026-10-02
      couverture: >
        Lus à l'image : art. 5 et 7 du décret dans les deux éditions (JORT n° 45 de 2020, p. 1093 et p. 1248 arabe) — « salaire
        minimum interprofessionnel garanti des différentes professions », sans régime. Titres de jort_cache 2022-2026 portant
        « AMEN SOCIAL » ou « الأمان الاجتماعي » : aucun modificatif du décret parmi les intitulés listés. Lacunes : la requête
        par numéro (« 2020-317 », « 317 لسنة 2020 ») sur les titres n'a pas été lancée en tant que telle ; aucune circulaire ni
        formulaire lu (site du ministère inaccessible ce jour).
      sources: [jort_cache, corpus_local]

- id: r-amen-cumul-supplement-6-18
  objet: texte, circulaire ou document du ministère disant si le supplément de 10 dinars par enfant de 6 à 18 ans (arrêté conjoint du 19 mai 2020, art. 2, alinéa 2 dans sa rédaction de l'arrêté du 1er avril 2022) se cumule avec l'allocation familiale de 30 dinars des 6-18 ans (décret n° 2025-426 ; arrêté conjoint du 3 novembre 2025), ou tout arrêté abrogeant ou modifiant cet alinéa 2
  ou: Journal officiel ; circulaires du ministère des affaires sociales ; rapports annuels de l'Amen social pour 2024 et 2025
  requetes:
    titres_like:
      - "%AMEN SOCIAL%"
      - "%allocation familiale%"
      - "%pauvres%"
    iort_ar:
      - "الأمان الاجتماعي"
  passes:
    - date: 2026-10-09
      resultat: aucun
      couvert_jusqu_au: 2026-10-02
      couverture: >
        Titres de jort_cache 2022-2026 (index au 2 octobre 2026). Lus au fascicule français : arrêtés du 1er avril 2022 (JORT
        n° 38, p. 972-973), du 3 avril 2023 (n° 34), du 28 février 2024 (n° 33), du 29 janvier 2025 (n° 12), du 21 avril 2026
        (n° 40), décret n° 2025-426 (n° 121 de 2025), arrêté du 3 novembre 2025 (n° 132) : seul l'alinéa 1 de l'article 2 est
        modifié après 2022 ; l'arrêté de 2025 ne vise pas l'arrêté de 2020. Pratique du pilote de 2022-2023 connue par le
        rapport du ministère pour 2023 (PDF 37) : 20 D du don ajoutés aux 10 D du budget. Lacunes : aucun document postérieur
        à 2023 ; fascicules inconnus de jort_cache non parcourus.
      sources: [jort_cache, corpus_local, tunisia-data]
```

Documents à récupérer, non des recherches de textes : les études du § 1.10.

## 9. Ce qui contredit ou corrige le plan

1. **§ 3.5.1, point 7 et § 8 du plan (handicap lourd).** Le texte n'est pas ambigu sur les quatre
   paliers (D3) ; il l'est sur un autre point, que ni le plan ni la notice ne relèvent : « à
   charge » dans l'édition arabe seulement.
2. **§ 3.5.2, ligne N3.** Le « avant → après » est à préciser : le supplément de 10 D de 2020
   allait, pour les catégories pauvres, à tout enfant à charge de moins de 18 ans (25 ans en
   études) ; l'arrêté du 1er avril 2022 le borne aux 6-18 ans à compter du 1er février 2022,
   quand l'allocation de 30 D prend les moins de six ans. Le supplément ne disparaît pas. La Banque mondiale
   (PAD4414, § 20) écrit à tort « per 0-5 years-old-child ».
3. **Allocation des 6-18 ans.** Elle n'apparaît pas en 2025 : pilote sur don depuis juillet ou
   septembre 2022, 422 542 enfants en décembre 2023, 124,6 millions de dinars ; le décret de
   2025 l'institue en droit et la porte au budget, sans viser la loi organique.
4. **Supplément et allocation des 6-18 ans** visent la même tranche d'âge depuis 2022 : le
   plan ne le voit pas (D11).
5. **Loi n° 96-101.** Son objet, dans ses mots, est « la protection sociale en faveur des
   travailleurs ayant cessé leur travail pour des raisons économiques ou technologiques » ;
   « perte d'emploi » n'y est pas.
6. **Loi n° 89-73.** « Régime agricole amélioré » n'est pas dans la loi : « Dispositions
   particulières applicables aux salariés employés par certaines entreprises agricoles ».
7. **Loi organique n° 2019-10.** Le plan cite l'article 1er ; l'article 7 énonce cinq buts, dont
   « garantir le droit à un revenu minimum ».
8. **Arrêté du 5 août 2026.** Ses visas sont ceux des régimes de pensions : à ne pas ranger
   sans examen parmi les « étapes » du seul PNAFN.
9. **Rapport du ministère pour 2023.** Une quatrième discordance interne (127 911 contre
   144 023 enfants) ; et, pour la Banque mondiale, ce rapport n'était pas publié le 25 novembre
   2025 : à citer comme document du ministère sans adresse publique vérifiée.
10. **Seuil de score.** La circulaire de 2022 a été suivie d'une circulaire d'octobre 2025 qui
    révise les critères : le paramètre daté du 1er juin 2022 n'est pas le dernier état.
11. **Bénéficiaires de 2010.** 124 000 ménages (documents de 2022 et 2026) ou 130 000 (document
    de 2021) : ne pas écrire l'un sans l'autre.

## 10. Références candidates pour le bibliographe

**Clés existantes à réemployer (non vérifiées une à une dans `references.json`)** :
`arrete-2026-08-05-allocation-pauvres` ; les notices de la loi n° 87-29 et des textes de
l'assistance proposées dans `prestations-assistance.md`.

**Notices à créer** (CSL-JSON, URL pist.tn vérifiées en existence le 9 octobre 2026) :

```json
[
  {"id": "arrete-2026-04-21-amen-transferts", "type": "legislation",
   "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 21 avril 2026, modifiant l'arrêté conjoint du 19 mai 2020 fixant le mode de calcul et le montant des transferts monétaires directs au profit des catégories pauvres bénéficiant du programme « AMEN SOCIAL »",
   "container-title": "Journal officiel de la République tunisienne", "number": "40", "page": "786",
   "issued": {"date-parts": [[2026, 4, 21]]}, "URL": "https://www.pist.tn/jort/2026/2026F/Jo0402026.pdf"},
  {"id": "decret-2025-426", "type": "legislation",
   "title": "Décret n° 2025-426 du 2 octobre 2025, portant institution d'une allocation familiale pour les enfants âgés de 6 à 18 ans",
   "container-title": "Journal officiel de la République tunisienne", "number": "121", "page": "2518",
   "issued": {"date-parts": [[2025, 10, 3]]}, "URL": "https://www.pist.tn/jort/2025/2025F/Jo1212025.pdf"},
  {"id": "arrete-2025-11-03-allocation-6-18", "type": "legislation",
   "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 3 novembre 2025, fixant les conditions d'octroi de l'allocation familiale au titre des enfants âgés de 6 à 18 ans et son montant",
   "container-title": "Journal officiel de la République tunisienne", "number": "132", "page": "2963",
   "issued": {"date-parts": [[2025, 11, 4]]}, "URL": "https://www.pist.tn/jort/2025/2025F/Jo1322025.pdf"},
  {"id": "mas-amen-social-2023", "type": "report",
   "title": "تقرير المتابعة والتقييم لبرنامج الأمان الاجتماعي لسنة 2023 [Rapport de suivi et d'évaluation du programme Amen social pour l'année 2023]",
   "author": [{"literal": "Ministère des Affaires sociales, Instance générale de la promotion sociale"}],
   "number-of-pages": "48", "language": "ar",
   "note": "Date de parution et adresse de publication non établies ; exemplaire transmis, SHA-256 977bad7bedd8de52baae49a269c7285eb97666c1f05795dd2bee5914198c7d2b"},
  {"id": "banquemondiale2021pad4414", "type": "report",
   "title": "Tunisia COVID-19 Social Protection Emergency Response Support Project (P176352): Project Appraisal Document",
   "author": [{"literal": "Banque mondiale"}], "number": "PAD4414", "publisher": "Banque mondiale",
   "issued": {"date-parts": [[2021, 3, 21]]},
   "URL": "https://documents.worldbank.org/curated/en/500821617501635181/pdf/Tunisia-COVID-19-Social-Protection-Emergency-Response-Project.pdf"},
  {"id": "banquemondiale2022pad4815", "type": "report",
   "title": "Tunisia COVID-19 Social Protection Emergency Response Support Project, Additional Financing (P177821): Project Paper",
   "author": [{"literal": "Banque mondiale"}], "number": "PAD4815", "publisher": "Banque mondiale",
   "issued": {"date-parts": [[2022, 3]]},
   "URL": "https://documents.worldbank.org/curated/en/346691649086515363/pdf/Tunisia-COVID-19-Social-Protection-Emergency-Response-Support-Project-Additional-Financing.pdf"},
  {"id": "banquemondiale2026ppiaf000292", "type": "report",
   "title": "Tunisia Social Development Promotion Support Project – Second Additional Financing: Project Paper",
   "author": [{"literal": "Banque mondiale"}], "number": "PPIAF000292", "publisher": "Banque mondiale",
   "issued": {"date-parts": [[2026, 3, 6]]},
   "URL": "https://documents.worldbank.org/curated/en/099031026105517065/pdf/BOSIB-4b996e72-5f8f-4efa-a0b6-e58471608bd1.pdf"},
  {"id": "banquemondiale2025isr04716", "type": "report",
   "title": "Tunisia COVID-19 Social Protection Emergency Response Support Project (P176352): Implementation Status & Results Report, Seq. No. 9",
   "author": [{"literal": "Banque mondiale"}], "number": "ISR04716", "publisher": "Banque mondiale",
   "issued": {"date-parts": [[2025, 11, 25]]},
   "URL": "https://documents.worldbank.org/curated/en/099112525165032162/pdf/P176352-09990b44-c8cc-4790-b6d0-facb04836a65.pdf"},
  {"id": "banquemondiale2026isr08116", "type": "report",
   "title": "Tunisia COVID-19 Social Protection Emergency Response Support Project (P176352): Implementation Status & Results Report, Seq. No. 10",
   "author": [{"literal": "Banque mondiale"}], "number": "ISR08116", "publisher": "Banque mondiale",
   "issued": {"date-parts": [[2026, 7, 7]]},
   "URL": "https://documents.worldbank.org/curated/en/099070726095526116/pdf/P176352-89002ab8-7377-4188-bc7f-05770921a269.pdf"},
  {"id": "banquemondiale2021pret9230tn", "type": "legal_case",
   "title": "Loan Agreement (COVID-19 Social Protection Emergency Response Support Project) between Republic of Tunisia and International Bank for Reconstruction and Development, Loan Number 9230-TN",
   "author": [{"literal": "Banque mondiale"}], "issued": {"date-parts": [[2021, 4, 2]]},
   "note": "Accord conclu le 2 avril 2021 selon le visa de l'arrêté du 1er avril 2022 (JORT n° 38 de 2022, p. 973) ; approuvé par la loi n° 2021-28 du 22 juin 2021, non lue ; type CSL à arbitrer par le bibliographe",
   "URL": "https://documents.worldbank.org/curated/en/640411619625751047/pdf/Official-Documents-Loan-Agreement-for-Loan-No-9230-TN.pdf"},
  {"id": "unicef2024allocations618", "type": "report",
   "title": "Rapport de recherche sur le programme d'allocations familiales pour les 6-18 ans en Tunisie",
   "author": [{"literal": "UNICEF Tunisie"}], "publisher": "UNICEF", "number-of-pages": "124",
   "issued": {"date-parts": [[2024, 5]]}, "URL": "https://www.unicef.org/tunisia/media/7871/file"},
  {"id": "unicef2024allocations618fiche", "type": "pamphlet",
   "title": "Recherche sur le programme d'allocations familiales pour les 6-18 ans en Tunisie (fiche de synthèse)",
   "author": [{"literal": "UNICEF Tunisie"}], "publisher": "UNICEF",
   "issued": {"date-parts": [[2024]]}, "URL": "https://www.unicef.org/tunisia/media/7916/file"}
]
```

Les adresses de la Banque mondiale et de l'UNICEF sont celles du catalogue de `tunisia-data`
(collecte du 9 octobre 2026) ; je ne les ai pas rouvertes. Les notices des lois du § 6 (lois
n° 75-82, 80-36, 88-38, 88-39, 89-73, 94-88, 94-28, 95-56, 96-65, 96-101, 2004-71, 2024-44,
86-83, décrets n° 98-409, 98-1812, 2007-1366, décret-loi n° 2022-8, arrêtés du 1er avril 2022)
sont à confronter d'abord à `precis/fr/prestations_sociales/references.json` : numéros, dates et
pages de leur notice figurent au tableau du § 6.

## 11. Notions à glossaire (à vérifier dans `precis/glossaire.yml`)

| Terme français | Terme arabe du texte | Source canonique |
|---|---|---|
| catégories pauvres ; catégories à revenu limité | الفئات الفقيرة ؛ الفئات محدودة الدخل | loi organique n° 2019-10, art. 1er et 2 |
| privation multidimensionnelle | (non relevé en arabe) | loi organique n° 2019-10, art. 2 |
| modèle de score | أنموذج التنقيط | loi organique n° 2019-10, art. 2 ; arrêté du 19 mai 2020 |
| transfert monétaire direct ; montant de base | التحويلات المالية المباشرة ؛ مقدار أساسي | arrêté conjoint du 19 mai 2020, art. 2 |
| allocation supplémentaire (supplément par enfant) | منحة إضافية | même arrêté, art. 2 |
| appui financier occasionnel | الدعم المادي الظرفي | arrêté conjoint du 19 mai 2020, art. 1er |
| allocation familiale (Amen social) | المنحة العائلية | décret-loi n° 2022-8, art. 11 bis ; rapport du ministère pour 2023 |
| lourdement handicapé | ذوو الإعاقة العميقة | décret gouvernemental n° 2020-317, art. 5 |
| carte de soins gratuits ; carte à tarifs réduits | بطاقة العلاج المجاني ؛ بطاقة العلاج بالتعريفة المنخفضة | décrets n° 98-1812 et n° 98-409 ; rapport du ministère pour 2023 |
| majoration pour salaire unique | (non relevé) | loi n° 80-36, section I bis, art. 65 bis |
| contribution aux frais de prise en charge des enfants dans les crèches | (non relevé) | loi n° 94-88, art. 1er |
| registre des données sociales | (non relevé) | arrêté conjoint du 3 novembre 2025, art. 1er |

« PNAFN », « AMG1 », « AMG2 » sont des sigles d'usage (Banque mondiale, UNICEF) : aucun texte lu
ici ne les emploie.

## 12. Lacunes

- Seuil de score, régime du salaire minimum, règle de cumul depuis 2025 : non identifiés (§ 8).
- D7, D8, D10, D12, D13 : non traités ; D9 partiel (cinq dates « à confirmer »).
- Loi n° 60-30 : intitulés des subdivisions des art. 76 à 98 non relevés.
- Loi n° 2004-71 : citation de l'article premier à relire à l'image (police décalée).
- Rapport du ministère pour 2023, PDF 36-38 : citations arabes prises à la couche texte, dont
  l'ordre des mots est perturbé — à relire à l'image, en particulier la phrase des 20 D et 10 D.
- Financement additionnel de 2022, figure 4 (transfert du PNAFN, 1987-2021) : valeurs à relire à
  l'image avant tout versement.
- Études de seconde main (§ 1.10) : six documents à récupérer.
- Aucun PIB de ces pièces ne dit sa base.
- Pagination française des trois arrêtés du 19 mai 2020 et de l'arrêté du 10 juillet 2025 non
  relevée.
