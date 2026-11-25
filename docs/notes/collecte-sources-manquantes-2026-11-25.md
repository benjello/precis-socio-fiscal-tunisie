# Collecte de sources manquantes — 25 novembre 2026

Récupération de sept lots de sources demandés par l'humain. Fichiers déposés hors dépôt dans
`~/Downloads/` (le dépôt est public : aucune donnée brute n'y est versée). Récupération via les
sites officiels vivants et, à défaut, la Wayback Machine (snapshot le plus proche `…/2id_/<URL>`).

⚠️ Captures Wayback tronquées : plusieurs fichiers n'existent qu'en version coupée à 1 048 576 o
(1 Mo) au moment du crawl — écartés car incomplets (voir CNRPS ci-dessous).

## Obtenu

| Lot | Emplacement `~/Downloads/` | Contenu | Couverture |
|---|---|---|---|
| **1. EBCNV INS** | `EBCNV2021_*.pdf/.xlsx` | Note de synthèse (15 p.), communiqués FR/AR, données Excel | 2021 |
| **2. Masse salariale CNSS** | `CNSS_publication_2020/` (18 tableaux FR + sommaire) | Dont `08-Fr-evolution_cotisations_cnss_2000-2020` ; effectifs, pensions, prestations | séries 2000‑2020 |
| **3. Stats fiscales DGI** | `DGI_stats_fiscales/` (5 fichiers) | Série recettes par **type d'impôt** 1986‑2025 ; contrôle fiscal 2016 (créations par secteur) ; IACE 2025 (chiffres DGI par secteur, **secondaire**) ; rapports d'activité DGI 2014‑2015 | variable |
| **4. Cotisations CNAM** | `CNAM_cotisations/` (9 PDF) | Rapports branche **AT/MP** (ANNUEL 2018‑2021, statistiques 2018‑2022) ; 2 fichiers de faible valeur (AO, accès info) | 2018‑2022 |
| **5. Transferts aux ménages** | `transferts_menages/` (14 PDF) | AMEN Social (rapports activité 2022, 2023 ; éval. impact 2021), CRES, Banque mondiale, UNICEF | 2017‑2023 |
| **6. CNRPS retraites** | `CNRPS_rapports/` | Rapports annuels `ra_2019`, `ra_2020` ; `rapport_ada_2019…2022` | 2019‑2022 |
| **7. Comptes communaux** | `comptes_communaux/` (9 fichiers) | 2020 réalisé par commune (CSV+XLSX) ; 2021 budgets détaillés + réalisé décembre | 2020‑2021 |

Déjà en main avant cette collecte (non repris) : annuaires CNSS 2016 et 2018, rétrospective CNSS
1990‑2004, BILAN CNAM 2010/2016‑2018/2018‑2019/2020‑2021.

## Lacunes confirmées (à verser au backlog durable)

- **Rapports annuels / publications statistiques CNSS et CNRPS 2021, 2022, 2023 : INTROUVABLES**
  publiquement (sites vivants + Wayback). Dernières éditions : **CNSS 2020** (série 2000‑2020),
  **CNRPS `ra_2020`** et recueil `gstat_2010-2019`. ⇒ les **pensions 2021‑2023 restent vides** tant
  que ces données ne sont pas obtenues directement auprès des caisses.
- **Recettes fiscales DGI ventilées par secteur** (IS/IRPP par branche, nombre de contribuables par
  secteur) : **aucune série officielle**. La ventilation sectorielle n'existe qu'en partiel (contrôle
  fiscal 2016) ou en source secondaire (IACE 2025, qui reprend des chiffres DGI). data.gov.tn muet.
- **Cotisations d'assurance maladie CNAM détaillées** (produits par régime, taux) : absentes de tout
  document public ; ne figurent que dans les BILAN CNAM déjà récupérés. Pas d'ANNUEL/statistiques
  CNAM 2023 en ligne.
- **CNRPS `bilan2019`, `budget_2019`, `gstat_2010-2019`** : seules des captures Wayback **tronquées à
  1 Mo** existent — à récupérer entières auprès de la CNRPS si besoin.
- Pistes non explorées : CGSS / ministère des Affaires sociales et Conseil du marché financier pour
  les comptes CNAM ; CPSCL pour des comptes communaux antérieurs à 2020.
