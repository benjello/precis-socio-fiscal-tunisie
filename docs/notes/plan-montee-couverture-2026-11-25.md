# Plan de montée en couverture : sociétés non financières (S11) et ménages (S14)

Relevé du 25/11/2026. Source des montants : tableau économique d'ensemble de l'INS, édition 2020-2024,
année 2020 (`ins-cnat-2015`), lu par `scripts/comptes_tee.py` dans `precis/fr/compte-secteurs-tee.csv`.
Page : `precis/fr/compte-secteurs.qmd`, section `#sec-csec-tee-couverture` (même tableau, engendré à
partir du CSV et du dictionnaire `SOURCES` de la page).

Règle de classement : les dix opérations les plus lourdes du secteur en 2020, en valeur absolue, hors
soldes (B.), compte financier (F.) et lignes sans libellé ; D.41 (« dont intérêts ») n'est pas compté
à part de D.4 ; D.2 − D.3 ne l'est que par D.29 − D.39, seul inscrit aux secteurs.

Recherche des séries : catalogue de l'entrepôt de données (dépôt `tunisia-data`, `catalog.yml`,
279 entrées), lecture seule ; années vérifiées dans les fichiers `data/processed/` indiqués par le
catalogue. « Pas de série au catalogue » : aucune entrée du catalogue ne chiffre l'opération. Les
séries `cnat-*`, `ins-va-branche-base2015` et `ins-comptes-organismes-securite-sociale` sont tirées
des comptes nationaux : elles ne comptent pas comme sources indépendantes. Fichiers présents sous
`data/processed/` mais hors catalogue, non retenus : `bct/bct_series_long_full.csv` (situations
monétaires, paiements extérieurs sans transferts de revenus), `bct/epargne_cep.csv`, `bct/bsf-tables/`.

## S11, sociétés non financières (2020, millions de dinars courants)

| Rang | Opération | Montant | Séries du catalogue | Couverture |
|--:|---|--:|---|---|
| 1 | P.1 production (ressources) | 100 437,0 | `entreprises-publiques-comptes-primaires`, `steg-etats-financiers`, `etap-rapports-annuels` | entreprises publiques seulement (13 entités en 2020, non rangées par secteur) ; 2000-2025, 2013-2023, 2004-2024 |
| 2 | P.2 consommation intermédiaire | 61 661,9 | `entreprises-publiques-comptes-primaires` | achats consommés, autres charges d'exploitation ; mêmes entités |
| 3 | D.1 rémunération des salariés (emplois) | 21 593,9 | `entreprises-publiques-effectifs-ensemble` ; `cnss-annuaire-2018-brut` | charges de personnel des entreprises publiques hors banques et caisses (2018, 2019, 2020, 2022) ; masse salariale déclarée au RSNA, tous employeurs privés, 2000-2018 (2020 non couverte) |
| 4 | D.4 revenus de la propriété (emplois) | 9 617,0 | `entreprises-publiques-dividendes-etat` | dividendes versés à l'État par les entreprises publiques, 2017-2023 ; intérêts : pas de série |
| 5 | P.51g formation brute de capital fixe | 7 079,3 | pas de série au catalogue | |
| 6 | D.5 impôts courants (emplois) | 5 238,9 | `recettes-fiscales-composition` (impôt sur les sociétés) | S11 et S12 ensemble, 1986-2025 |
| 7 | P.52 variations des stocks | −3 762,4 | pas de série au catalogue | |
| 8 | D.7 autres transferts courants (emplois) | 1 243,0 | pas de série au catalogue | |
| 9 | D.4 revenus de la propriété (ressources) | 1 085,5 | pas de série au catalogue | |
| 10 | D.9 transferts en capital à recevoir | 845,5 | `entreprises-publiques-transferts-budget` | transferts du budget aux entreprises et EPNA par nature (dont investissement), 2016-2024 ; le total mêle caisses sociales et compensation |

## S14, ménages (2020, millions de dinars courants)

| Rang | Opération | Montant | Séries du catalogue | Couverture |
|--:|---|--:|---|---|
| 1 | P.3 dépense de consommation finale | 86 936,9 | `ins-enbcnv-2021-logement`, `education-depense-menages` (INS, hors comptes nationaux) | structure du poste logement (2021) ; dépense d'enseignement par personne (2015, 2021) ; pas de niveau total, 2020 non couverte |
| 2 | P.1 production (ressources) | 64 030,4 | pas de série au catalogue hors comptes nationaux | |
| 3 | D.1 rémunération des salariés (ressources) | 51 729,6 | `masse-salariale-ratios` ; `entreprises-publiques-effectifs-ensemble` ; `cnss-annuaire-2018-brut` | rémunérations du budget de l'État 1990-2025 ; entreprises publiques 2018-2022 ; RSNA 2000-2018 |
| 4 | P.2 consommation intermédiaire | 21 636,8 | pas de série au catalogue | |
| 5 | D.63 transferts sociaux en nature (ressources) | 13 690,9 | `ins-budget-sante-2018-2023` ; `cnam-comptes-2011-2021` | département de la Santé 2018-2023 ; prestations décaissées CNAM 2011-2021 ; enseignement : pas de série couvrant 2020 |
| 6 | D.61 cotisations sociales (emplois) | 13 272,2 | `cnss-cotisations` ; `cnrps-regime-general-finances` | CNSS 2000-2020 (hors maladie et accidents du travail depuis 2006) ; CNRPS régime général 2014-2020 ; CNAM : pas de série |
| 7 | D.62 prestations sociales en espèces (ressources) | 12 393,3 | `cnrps-pensions` ; `cnss-annuaire-2018-brut` | dépenses du régime de retraite CNRPS 2000-2020 ; pensions et prestations familiales RSNA 2000-2018 |
| 8 | D.7 autres transferts courants (ressources) | 8 460,4 | pas de série au catalogue | aucun relevé des transferts reçus de l'étranger |
| 9 | D.1 rémunération des salariés (emplois) | 6 832,2 | `ins-repertoire-emploi-forme` (INS, hors comptes nationaux) | salariés des entreprises « personne physique », 2000-2024, effectifs sans montant |
| 10 | D.4 revenus de la propriété (ressources) | 6 448,6 | pas de série au catalogue | |

## Ce qui en ressort

- S11 : seules les entreprises publiques sont chiffrables hors comptes nationaux, et pour leurs
  comptes primaires seulement. Les sociétés privées n'ont aucune série de production, de charges ou
  d'investissement au catalogue ; l'impôt sur les sociétés ne distingue pas S11 de S12.
- S14 : les ressources tirées des administrations (rémunérations publiques, prestations, transferts
  en nature) et les cotisations sont couvertes, en partie, par les séries des caisses et du budget ;
  la production, la consommation intermédiaire et le niveau de la consommation finale ne le sont pas.
- Séries à chercher en priorité : balance des paiements (transferts courants reçus par les ménages),
  masse salariale CNSS après 2018, cotisations de la CNAM, investissement des entreprises privées.
