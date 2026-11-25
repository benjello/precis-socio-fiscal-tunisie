# Sources pour chiffrer S11 et S14 hors comptes de l'INS

Relevé du 25/11/2026. Point de départ : `docs/notes/plan-montee-couverture-2026-11-25.md` (PR #896, branche
`comptes/tee-secteurs`), qui classe les dix opérations les plus lourdes de 2020 de chaque secteur
(tableau économique d'ensemble, édition 2020-2024, `precis/_seriescache/cnat-tee.csv`). Entrepôt lu :
copie `tunisia-data-wt-merge`, commit `34c35e7` (25/11/2026), lecture seule. Détail par couple source ×
opération : `sources-societes-menages.csv` (26 lignes).

## Règle de calcul

- Dénominateur : somme des montants absolus des dix opérations du plan. S11 : 212 564,4 M ; S14 : 285 431,3 M
  (sommes recalculées, elles concordent avec le plan).
- Part du montant : valeur de la source en 2020 ÷ montant INS 2020 de l'opération. Étiquettes : « mesurée »
  (deux valeurs de l'entrepôt), « estimée » (rapport d'une autre année), « borne haute » (rien ne mesure la
  part couverte : on compte l'opération entière), « non évaluable » (existence ou contenu de la source non
  établis dans l'entrepôt).
- Gain net = montant de l'opération × part couverte − couverture déjà dans l'entrepôt, divisé par le
  dénominateur du secteur, en points. Les gains de deux sources sur une même opération ne s'additionnent pas.
- Classement : somme des points S11 et S14 (poids égal par secteur, non pondéré par les montants).
- Une série n'est dite disponible que si l'entrepôt en porte une trace autre qu'une description de publication.

## Trois corrections au plan du 25/11/2026

1. D.7 des ménages (8 460,4 M) : le plan écrit « aucun relevé des transferts reçus de l'étranger ». La balance
   des paiements de la BCT figure dans l'entrepôt : transferts personnels reçus 2020 = 5 105,1 M (dont envois de
   fonds des travailleurs 4 969,0 M), soit 60,3 % de D.7 (`bct/bct_balance_paiements.csv`, édition 2022, p. 45,
   fichier présent sous `data/processed` mais sans entrée de catalogue ; en MBP5, catalogue
   `bct-balance-paiements-mbp5`, « économies sur salaires » 5 262,4 M, édition 2021).
2. D.63 des ménages (13 690,9 M) : le plan écrit « enseignement : pas de série couvrant 2020 ». L'entrepôt a les
   dépenses de gestion de l'éducation (6 181,5 M), de l'enseignement supérieur (1 564,0 M) et le budget de la
   santé (2 823,8 M) en 2020 (`education-depense-ministeres`, `ins-budget-sante-2018-2023`) : 77,2 % de D.63 en
   ordre de grandeur, concepts non rapprochés.
3. Pour S11, le plan cite les 13 entités des comptes primaires. L'annexe 9 du rapport sur les entreprises publiques
   (`entreprises-publiques-resultats-agreges`, LF 2024, 88 entreprises, 2020) donne produits d'exploitation
   26 906,4 M et charges de personnel 4 113,1 M.

## Tableau par opération, S11 (2020, M de dinars)

| Opération | Montant INS | Déjà dans l'entrepôt (2020) | Candidate à collecter |
|---|--:|---|---|
| P.1 production | 100 437,0 | EP, annexe 9 : 26 906,4 (26,8 %, 12,7 pts) ; produits d'exploitation, subventions comprises | Centrale des bilans BCT, enquêtes ou liasses sur les entreprises : non évaluable |
| P.2 consommation intermédiaire | 61 661,9 | non isolée (charges d'exploitation 28 470,0 mêlent personnel et amortissements) | mêmes : non évaluable |
| D.1 rémunérations (emplois) | 21 593,9 | EP : 4 113,1 (19,0 %, 1,9 pt) | CNSS masse salariale 2019-2020 : +3,14 pts (estimée) |
| D.4 revenus de la propriété (emplois) | 9 617,0 | dividendes à l'État : 98,3 (1,0 %) ; balance des paiements : revenus versés à l'extérieur 4 704,1, tous secteurs, dont investissements directs 2 481,3 | pas de série d'intérêts ; non évaluable |
| P.51g FBCF | 7 079,3 | aucune | investissements déclarés (APII : simple mention dans l'entrepôt), enquêtes : non évaluable |
| D.5 impôts courants (emplois) | 5 238,9 | IS total 3 123,0 ; correspondance avec S11 à vérifier | DGI par secteur : +2,46 pts (borne haute) |
| P.52 variation des stocks | −3 762,4 | aucune | non évaluable |
| D.7 autres transferts (emplois) | 1 243,0 | aucune | non évaluable |
| D.4 revenus de la propriété (ressources) | 1 085,5 | aucune | non évaluable |
| D.9 transferts en capital à recevoir | 845,5 | `entreprises-publiques-transferts-budget` (2016-2024) ; montant 2020 non relevé ici, à vérifier | |

Acquis hors comptes de l'INS : 14,6 points de S11 en ordre de grandeur (12,66 + 1,93 + 0,05), tous issus des
entreprises publiques. Le privé n'a aucune série de production, de charges ou d'investissement.

## Tableau par opération, S14 (2020, M de dinars)

| Opération | Montant INS | Déjà dans l'entrepôt (2020) | Candidate à collecter |
|---|--:|---|---|
| P.3 consommation finale | 86 936,9 | ENBCNV 2021 : poste logement seulement (annexe 2) | ENBCNV, annexe 3 : +30,46 pts (borne haute) |
| P.1 production | 64 030,4 | aucune | non évaluable (production des ménages : informel, agriculture, loyers imputés) |
| D.1 rémunérations (ressources) | 51 729,6 | fonction publique et entreprises publiques (INS exclu) ; balance des paiements : reçue des non-résidents 1 279,8 (2,5 %) | CNSS masse salariale : +5,99 pts (estimée) |
| P.2 consommation intermédiaire | 21 636,8 | aucune | non évaluable |
| D.63 transferts en nature | 13 690,9 | santé + éducation + supérieur 10 569,3 (77,2 %, 3,7 pts) ; CNAM prestations 2 094,3 | résidu 3 121,6 : 1,09 pt, sans source identifiée |
| D.61 cotisations (emplois) | 13 272,2 | CNSS 3 430,0 (25,8 %) + CNRPS reconstituées 4 333,0 (32,6 %) = 58,4 % (2,72 pts) | CNAM recettes 2020 : +1,93 pt (borne haute) |
| D.62 prestations en espèces | 12 393,3 | CNRPS 5 925,4 + CNSS pensions 4 013,6 = 9 939,0 (80,2 %, 3,48 pts) | |
| D.7 autres transferts (ressources) | 8 460,4 | balance des paiements : transferts personnels 5 105,1 (60,3 %, 1,79 pt) | résidu 3 355,3 : transferts de l'État aux ménages, +1,18 pt (borne haute) |
| D.1 rémunérations (emplois) | 6 832,2 | effectifs seulement (répertoire INS : 109 920 salariés en personne physique, 10,2 %) | CNSS masse salariale : +1,20 pt (estimée) |
| D.4 revenus de la propriété (ressources) | 6 448,6 | balance des paiements : reçus 280,3 (4,3 %) | pas de série d'intérêts ni de dividendes |

Acquis hors comptes de l'INS : environ 12,2 points de S14 en ordre de grandeur (2,72 + 3,48 + 3,70 + 1,79 + 0,45
+ 0,10 pour D.1 et D.4 de la balance des paiements).

## Cinq sources prioritaires à collecter

| Rang | Source | Calcul | Points S11 | Points S14 | Total |
|--:|---|---|--:|--:|--:|
| 1 | ENBCNV (INS), annexe 3, dépense annuelle moyenne par personne selon le produit (2021 ; édition 2015 à vérifier) | P.3 : 86 936,9 ÷ 285 431,3 | 0 | 30,46 (borne haute) | 30,46 |
| 2 | Masse salariale déclarée à la CNSS, annuaires 2019 et 2020, par activité et par taille | 2018 : 14 921,3 ÷ (D.1 total 45 213,9 − administration centrale 15 369,5) = 50,0 % ; ÷ D.1 ressources S14 45 182,0 = 33,0 % ; S11 : (50,0 % − 19,0 % déjà couverts par les EP) × 21 593,9 = 6 683,2 ÷ 212 564,4 ; S14 : 33,0 % × 51 729,6 = 17 083,6 et 50,0 % × 6 832,2 = 3 415,9 ÷ 285 431,3 | 3,14 | 7,19 (5,99 + 1,20) | 10,33 |
| 3 | Statistiques fiscales de la DGI par secteur (IS, retenues, IRPP par catégorie) | D.5 S11 : 5 238,9 ÷ 212 564,4 | 2,46 (borne haute) | 0 | 2,46 |
| 4 | Recettes (cotisations) de la CNAM, bilan 2020-2021 | D.61 : (13 272,2 − 3 430,0 − 4 333,0) ÷ 285 431,3 | 0 | 1,93 (borne haute) | 1,93 |
| 5 | Transferts monétaires de l'État aux ménages en 2020 (AMEN, programmes d'aide) | D.7 : (8 460,4 − 5 105,1) ÷ 285 431,3 | 0 | 1,18 (borne haute) | 1,18 |

Lecture :

- Le rang 1 est une borne haute sans mesure de la part couverte : une enquête auprès des ménages sous-estime en
  général la consommation des comptes nationaux, mais l'écart n'est documenté nulle part dans l'entrepôt. L'année
  est 2021, pas 2020. Le classeur brut n'est pas dans la copie lue (`data/raw` hors git) : le contenu de l'annexe 3
  est à vérifier à l'ouverture.
- Le rang 2 est le seul gain estimé à partir de mesures. La masse CNSS est une masse de salaires (D.11), D.1
  contient en plus les cotisations patronales (D.12) : on rapporte la masse à D.1, par prudence (rapport à D.11 :
  62,2 %). Le RSNA mêle S11, S12, les employeurs « personne physique » (S14) et « services, œuvres et associations »
  (S15) : le taux de 50,0 % est uniforme, sans clé de partage. La clé possible est la ventilation par activité de
  l'annuaire 2018 (`cnss-annuaire-2018-ventilation-activite-brut`) et le répertoire INS (`ins-repertoire-emploi-forme`).
  La masse déclarée 2019 et 2020 n'est pas dans l'entrepôt : la fiche `cnss-annuaires.md` ne reçoit que les
  éditions 2006, 2016 et 2018, et la planche 2020 de « La CNSS en chiffres » ne porte que les effectifs et les
  cotisations. L'existence des annuaires 2019 et 2020 est à vérifier.
- Le rang 3 : l'INS classe 5 238,9 M d'impôts courants en S11, plus que l'IS total de 2020 (3 123,0 M). La
  correspondance IS ≈ S11 + S12 échoue telle quelle. En revanche IRPP + IS (12 068,3) valent 103,7 % du D.5 total
  des comptes (11 634,5) : le total concorde, c'est la répartition par secteur qui manque. Aucune publication par
  secteur n'est établie : adresse à vérifier.
- Les rangs 4 et 5 sont des résidus calculés par soustraction, non des mesures. Leur contenu n'est pas établi.
- Superpositions : les rangs 2 et 5 ne se recoupent pas (salaires contre transferts). Les entreprises publiques
  (19,0 % de D.1 S11) sont déduites du rang 2 par prudence.

## Sources non classées : gain non évaluable

| Source | Pourquoi non classée |
|---|---|
| Centrale des bilans (BCT) | Aucune trace dans l'entrepôt : grep du dépôt entier (centrale des bilans, centrale de bilans, ratios sectoriels) ; `catalog.yml`, `sources/bct-catalog.csv`, `sources/bct-publications.md`, `docs/catalogue/inventaire-2026-11-04.md`, `docs/tables-a-extraire-pdf.md`. Seule proche : « Centrale des risques » (BSF, rubrique VI), non extraite. Existence, périodicité, années et adresse : à vérifier. Si elle existait avec production et consommation intermédiaire, le potentiel est P.1 + P.2 = 76,3 points de S11 (borne haute, non un gain attendu). |
| Enquêtes ou liasses sur les entreprises (INS, DGI), investissements déclarés (APII) | Les sources que l'INS emploie pour S11 ne sont documentées nulle part dans l'entrepôt (`inventaire-tableaux.csv`, `cnat_textes_*`). APII : seule mention comme source complémentaire du répertoire (`sources/ins-rne-statistiques.md`). À vérifier. |
| États financiers des sociétés cotées (BVMT) | 75 pages de sociétés et 18 rapports (exercice 2021 surtout) ; échantillon qui mêle banques et assurances ; part de S11 non mesurable. |
| Crédits à l'économie (BCT, PL050010, 2018-2023) | F.4 : hors liste. Ligne « Services et crédits aux particuliers » (73 012 M en 2020) : mêle entreprises de services et ménages. Fichier hors catalogue (`bct/bct_series_long_full.csv`). Sans taux, D.4 n'en découle pas. |
| Répertoire INS des entreprises, enquête sur la population et l'emploi, enquête emploi et salaires, micro-entreprises | Effectifs, parts et salaires moyens : aucun montant agrégé, gain direct nul. Le répertoire sert de clé de partage S11 / S14. Pas de revenu des indépendants (statut : 1999-2012 seulement). |

## Ce qui reste à vérifier

- Années réelles du classeur ENBCNV (annexe 3) et existence de l'édition 2015 ; passage des moyennes par personne à un total national.
- Existence et contenu des annuaires CNSS 2019 et 2020 ; part de S15 et des employés de maison dans le RSNA.
- Recettes de la CNAM dans `BILAN_2020-2021.pdf` (le fichier est cité par `cnam-comptes-2011-2021`, les lignes de recettes n'ont pas été lues).
- Écart IRPP / D.5 des ménages : l'IRPP 2020 (8 945,3 M) vaut 168,6 % de D.5 S14 (5 305,7 M, hors liste du plan).
- Rattachement des 88 entreprises publiques à S11 ou S13, et chevauchement avec le RSNA.
- Aucun téléchargement, aucune lecture de PDF ni de classeur brut n'a été faite : tout vient des CSV, catalogues et fiches de l'entrepôt.
