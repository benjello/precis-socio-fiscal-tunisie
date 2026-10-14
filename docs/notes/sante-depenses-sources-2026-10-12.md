# Santé — dépenses budgétaires et paiements directs : lectures du 12 octobre 2026

Lecture **de la couche texte et des tableaux**, sans ouverture d'images.
Trois plans distincts : budget du département de la Santé (gestion **et**
développement, y compris capital) ; comptes de la CNAM (assurance maladie,
assurances sociales et accidents du travail, charges du compte de résultat
et décaissements de trésorerie) ; dépense **courante** de santé et financeurs
dans les comptes OMS, dont le financement privé comprend les paiements directs.
Les postes de facturation à l'hôpital et en clinique relèvent d'une quatrième
vue, par prestataire, détaillée dans `sante-cnam-comptes-2026-10-12.md` : la
facture réglée par la caisse peut être une recette de l'établissement, et non
une nouvelle dépense à ajouter. Aucun total national n'est obtenu en additionnant
ces colonnes.

## Dépenses du département « Santé publique », 2018-2023

INS, *Annuaire statistique de la Tunisie*, éditions 2017-2021 et 2019-2023,
chapitre 16, tableaux 16.8 (« Dépenses du titre I par chapitre ») et 16.10
(« Dépenses du titre II (équipement) par chapitre »), pp. 267 et 269 dans la première édition,
269 et 271 dans la seconde. Producteur des chiffres : ministère des Finances.
PDF locaux : `tunisia-data/data/raw/ins-publications/annuaire-statistique/2017-2021.pdf`
et `2019-2023.pdf`, déjà catalogués dans `sources/ins-publications-urls.csv`.
Unité imprimée : **milliers de dinars courants** ; conversion ci-dessous en millions
de dinars par division par 1 000. Les éditions se recoupent : pour 2020,
la seconde reproduit les deux valeurs de la première ; pour 2021 et 2022,
la troisième reprend les valeurs de l'édition 2018-2022.

| Exercice | Gestion, titre I (milliers de D) | Développement, titre II (milliers de D) | Somme (MD) | Édition utilisée |
|---|---:|---:|---:|---|
| 2018 | 1 741 511 | 207 421 | 1 948,932 | 2017-2021 |
| 2019 | 1 948 111 | 287 734 | 2 235,845 | 2017-2021 |
| 2020 | 2 539 822 | 283 951 | 2 823,773 | 2017-2021 |
| 2021 | 2 736 483 | 476 702 | 3 213,185 | 2019-2023 |
| 2022 | 2 743 200 | 265 934 | 3 009,134 | 2019-2023 |
| 2023 | 3 056 017 | 351 479 | 3 407,496 | 2019-2023 |

Les tableaux de l'INS portent le libellé « dépenses », sans explication à ces
pages sur le stade comptable (crédits votés, dépensés ou exécutés) ; ne pas
nommer ces sommes « dépenses exécutées » avant confrontation aux rapports de
clôture de la Cour des comptes et aux PAP/RAP de la mission Santé. Le périmètre
est celui du **département ministériel**, pas la dépense totale de santé :
ni les comptes de la CNAM, ni les autres financeurs, ni les dépenses directes
des ménages ne sont inclus dans cette ligne.

**Dénominateurs des ratios budgétaires.** Les mêmes tableaux 16.8 et 16.10
publient les totaux de gestion et de développement **de tous les départements**.
Leur somme est retenue comme dénominateur de « part du budget » : hors intérêts
et principal de la dette, fonds spéciaux et prêts. Ce n'est pas le « total des
dépenses » du tableau 16.7, qui inclut ces autres postes. Pour le PIB nominal,
tableau 17.1 « Ressources et emplois des biens et services aux prix courants »
des mêmes éditions : 2018, édition 2017-2021 p. 275 ; 2019-2023, édition
2019-2023 p. 277. **Base des comptes 2015**, années 2018-2023 directement
établies dans cette base, sans rétropolation (voir `precis/fr/annexe-pib.qmd`).
Les PIB 2019 et 2020 sont concordants entre les deux éditions ; les années
2021-2023 retiennent l'édition la plus récente.

| Exercice | Total gestion + développement, tous départements (MD) | PIB nominal base 2015 (MD) | Santé / budget comparable (%) | Santé / PIB (%) |
|---|---:|---:|---:|---:|
| 2018 | 28 612,505 | 112 985,5 | 6,81 | 1,73 |
| 2019 | 31 370,204 | 122 969,3 | 7,13 | 1,82 |
| 2020 | 35 691,563 | 119 502,1 | 7,91 | 2,36 |
| 2021 | 37 667,506 | 131 544,6 | 8,53 | 2,44 |
| 2022 | 43 488,550 | 139 503,0 | 6,92 | 2,16 |
| 2023 | 44 809,082 | 149 705,7 | 7,60 | 2,28 |

Calcul : `100 × (gestion Santé + développement Santé) / (gestion tous
départements + développement tous départements)` ou `/ PIB nominal`.
Les ratios sont calculés sur les montants **non arrondis** des deux premières
colonnes du premier tableau, puis arrondis au centième de point.

## Charges techniques de la CNAM dans les annexes budgétaires, 2016-2018

Ministère des Finances, *Rapport sur les entreprises publiques* annexé aux
projets de loi de finances pour 2020 et 2021, chapitre des caisses sociales.
PDF français catalogués dans `tunisia-data/sources/minfin-entreprises-publiques-caisses.md` :
`data/raw/caisses/minfin/Annexe_9_LF2020-Entreprises_publiques.pdf`, p. 45 ;
`Annexe_9_LF2021_Entreprises_Publiques.pdf`, p. 52. Les valeurs sont des
**charges d'exploitation techniques de l'ensemble des régimes de la CNAM**,
et non les seules prestations de soins remboursées au malade.

| Exercice | Charges techniques (MD) | Source et statut |
|---|---:|---|
| 2016 | 2 074 | rapport annexé au PLF 2020, valeur rétrospective |
| 2017 | 2 191 | même rapport, valeur rétrospective ; confirmée dans le rapport suivant |
| 2018 | 2 236 | rapport annexé au PLF 2021, valeur rétrospective |

Le PLF 2020 **prévoyait 2 244 MD pour 2018** (p. 46 de son rapport) : ne pas
recopier cette prévision comme un réalisé ; le rapport suivant donne 2 236 MD.
Le périmètre CNAM englobe assurance maladie, assurances sociales et AT/MP.
Ne pas additionner ces charges au département Santé : elles peuvent inclure
des soins déjà financés dans un autre circuit et n'ont pas le même périmètre.
Les **états financiers primaires de la CNAM**, plus précis et prolongés jusqu'en
2021, ainsi que les postes sanitaires identifiés, sont relevés à part dans
`sante-cnam-comptes-2026-10-12.md` : ce sont ces montants qui figurent dans
la figure et son onglet « Données », les annexes budgétaires servant au recoupement.

## Comptes de la santé de l'OMS, 2018-2023

OMS, *Global Health Expenditure Database* (GHED), séries
`GHED_CHEGDP_SHA2011` (dépense courante de santé / PIB),
`GHED_GGHE-DCHE_SHA2011` (financement public intérieur / dépense courante),
`GHED_GGHE-DGDP_SHA2011` (financement public intérieur / PIB),
`GHED_GGHE-DGGE_SHA2011` (financement public intérieur / dépense publique),
`GHED_PVT-DCHE_SHA2011` (financement privé intérieur / dépense courante),
`GHED_EXTCHE_SHA2011` (financement extérieur / dépense courante),
`GHED_CHE_pc_US_SHA2011` (dépense courante par habitant en dollars courants),
`GHED_OOPSCHE_SHA2011` (paiements directs / dépense courante) et
`GHED_OOP_pc_US_SHA2011` (paiements directs par habitant). Données Tunisie récupérées dans l'API GHO le
12 octobre 2026 ; les mêmes décimales sont servies par l'API des indicateurs
`SH.XPD.OOPC.CH.ZS` et `SH.XPD.OOPC.PC.CD` de la Banque mondiale, qui attribue
la série à la GHED de l'OMS. La fiche de l'indicateur définit les paiements
directs comme les dépenses de santé réglées directement par les ménages. Ce
n'est **ni** le ticket modérateur propre à une filière CNAM **ni** une enquête
sur les frais d'un ménage particulier.

| Exercice | Dépense courante / PIB (%) | Publique intérieure / dépense courante (%) | Publique intérieure / PIB (%) | Publique intérieure / dépenses publiques (%) | Privée intérieure / dépense courante (%) | Extérieure / dépense courante (%) | Dépense courante par habitant (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2018 | 5,94 | 52,10 | 3,09 | 10,78 | 47,42 | 0,48 | 215,42 |
| 2019 | 6,02 | 59,21 | 3,57 | 12,08 | 40,76 | 0,03 | 212,60 |
| 2020 | 7,06 | 61,11 | 4,31 | 12,49 | 38,41 | 0,47 | 250,40 |
| 2021 | 7,34 | 56,02 | 4,11 | 12,39 | 42,05 | 1,93 | 285,25 |
| 2022 | 7,51 | 52,65 | 3,96 | 10,84 | 41,33 | 6,01 | 276,46 |
| 2023 | 7,99 | 54,09 | 4,32 | 12,10 | 42,78 | 3,14 | 317,71 |

La part extérieure grimpe en 2022 puis recule ; ne pas lui attribuer une cause
sans lire les sources primaires de la GHED. La fiche de l'indicateur publiée
par la Banque mondiale (source OMS),
<https://api.worldbank.org/v2/indicator/SH.XPD.EHEX.CH.ZS?format=json>,
définit les ressources extérieures comme les transferts étrangers à la santé,
directs ou répartis par l'État, y compris ceux passant par des ONG ou d'autres
circuits. La série n'identifie pas les bailleurs ni les projets ; un financement
qui entre par le budget reste classé ici selon son **origine extérieure**.
Publique + privée intérieure +
extérieure = 100 % à l'arrondi près. Le paiement direct est **compris dans le
financement privé intérieur** ; il ne forme pas un quatrième bloc à ajouter.
Le périmètre public OMS comprend les recettes publiques intérieures et les
prélèvements obligatoires affectés à l'assurance maladie : **ce n'est pas le
seul budget de l'État**. Les indicateurs de PIB de l'OMS ne précisent pas ici
la **base des comptes nationaux** ni une éventuelle rétropolation ; ne pas les
présenter comme des ratios calculés sur le PIB INS en base 2015 du tableau précédent.
La dépense courante exclut les dépenses en capital (bâtiments, matériel…).

| Exercice | Part de la dépense courante de santé (%) | Dollars courants par habitant | Taux officiel annuel (D/USD) | IPC BCT (2015 = 100) | D courants par habitant (calcul) | D de 2025 par habitant (calcul) |
|---|---:|---:|---:|---:|---:|---:|
| 2018 | 41,92 | 90,29 | 2,6468667 | 117,1 | 238,99 | 380,23 |
| 2019 | 35,58 | 75,64 | 2,9344333 | 125,0 | 221,95 | 330,79 |
| 2020 | 33,44 | 83,74 | 2,8123583 | 132,0 | 235,50 | 332,38 |
| 2021 | 37,22 | 106,16 | 2,7944667 | 139,6 | 296,66 | 395,91 |
| 2022 | 36,29 | 100,33 | 3,1036000 | 151,1 | 311,38 | 383,92 |
| 2023 | 37,94 | 120,54 | 3,1061667 | 165,2 | 374,41 | 422,23 |

API : <https://ghoapi.azureedge.net/api/GHED_OOPSCHE_SHA2011?$filter=SpatialDim%20eq%20'TUN'%20and%20TimeDim%20ge%202018&$select=TimeDim,NumericValue,Value,SpatialDim&$orderby=TimeDim> ;
<https://ghoapi.azureedge.net/api/GHED_OOP_pc_US_SHA2011?$filter=SpatialDim%20eq%20'TUN'%20and%20TimeDim%20ge%202018&$select=TimeDim,NumericValue,Value,SpatialDim&$orderby=TimeDim>.
La fiche Banque mondiale : <https://api.worldbank.org/v2/indicator/SH.XPD.OOPC.CH.ZS?format=json>.
La série publique commence en 2000 et s'arrête en 2023 à la consultation ; aucune
valeur n'est livrée pour 2024-2025. Les dollars courants ne sont pas convertis
en dinars par l'OMS. Les deux colonnes en dinars sont **nos calculs** sur les
valeurs non arrondies : dollars courants par habitant × taux de change officiel moyen
de l'année, série `PA.NUS.FCRF` de la Banque mondiale (producteur : base
*International Financial Statistics* du FMI),
<https://api.worldbank.org/v2/country/TUN/indicator/PA.NUS.FCRF?format=json&date=2018:2023>.
Les **dinars de 2025** multiplient ensuite le montant courant par
`IPC(2025) / IPC(année)` ; l'IPC annuel BCT en base 100 en 2015 vaut **186,3 en
2025** et ses valeurs annuelles figurent au tableau. Série cataloguée dans
`tunisia-data` comme `bct-ipc-base2015` (rapports annuels BCT 2018-2025 ;
2025 : tableau 2-1, p. 57), disponible dans
`precis/_seriescache/bct-ipc-base2015.csv`. La conversion en dinars courants
n'est pas une observation directe et la correction par l'IPC ne mesure pas la
quantité de soins reçue. Aucun paiement direct **de l'année 2025** n'est publié
dans la série OMS consultée.

## Pistes de rapprochement

- Lire les rapports de clôture du budget de l'État publiés par la Cour des
  comptes, pour qualifier les montants du département et leur exécution ;
  distinguer les transferts à la CNAM des dépenses directes du ministère.
- Lire les PAP et RAP Santé, les états financiers de la CNAM et les dépenses
  des EPS à périmètre constant ; ces flux ne se déduisent pas de la ligne INS.
- Les volumes A des enquêtes INS sur la consommation des ménages de 2015 et 2021
  ont des tableaux textuels de dépenses médicales en dinars, mais leur traitement
  des remboursements et leur comparabilité avec les comptes OMS demandent une
  lecture méthodologique avant de les appeler « reste à charge ». Deux PDF ont
  été récupérés temporairement pour cette vérification, sans les citer au volume.
