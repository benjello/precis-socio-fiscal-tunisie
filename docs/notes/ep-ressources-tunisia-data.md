# EP — ressources déjà présentes dans tunisia-data + état sauvegarde

**6 novembre 2026.** Mémo durable pour **ne pas refaire** le travail de découverte. Deux constats :
(1) `tunisia-data/sources/` est un **catalogue de sources déjà très fourni** ; (2) la sauvegarde
du corpus fonctionne. Voir aussi `ep-sources-consolidation.md`, `ep-volet-financier.md`, `ep-bilan-couverture.md`.

## 1. Le catalogue `tunisia-data/sources/` (convention d'indexation)
Chaque famille de sources a : une fiche `<nom>.md` (description, couverture), un `<nom>-urls.csv`
(URLs), et parfois des `.csv` de données extraites. **C'est l'index autoritaire** — avant toute chasse
web, chercher ici. Fiches EP-pertinentes repérées (à exploiter, pas re-chercher) :

**Entreprises publiques / modèle**
- `entreprises-publiques/` (dossier), `entreprises-publiques.md`, `entreprises-publiques-urls.csv`,
  `eco-ep-urls.csv`, `rne-entreprises-publiques.csv`.
- `minfin-entreprises-publiques-caisses.md`, `minfin-rapport-ep-divers-2020-06.md`,
  `minfin-ep-cnrps-finances.md`, `minfin-transferts-par-etablissement.md`, `minfin-transferts-transport.md`.

**Cour des comptes (comptes d'EP — ce que je croyais inaccessible y est déjà catalogué !)**
- `cour-des-comptes-comptes-energie-industrie.csv`, `...-offices-finance-caisses.csv`,
  `...-transport-eau-habitat.csv` (comptes chiffrés) ; `...-observations-*.csv`,
  `...-sources-citees-*.csv` ; `cour-des-comptes-catalog.csv`, `cour-des-comptes-entreprises-pages.csv`,
  `cour-des-comptes-telechargements.csv`.
- `cdc-cloture-entreprises-publiques.md` + `...-2003-2009.md` (données de clôture d'EP).

**Marché / rapports d'entreprise**
- `bvmt-rapports-annuels-urls.csv`, `bvmt-rapports-archives-urls.csv`, `bvmt-societes-cotees.md`,
  `bvmt-societes-cotees-urls.csv` — **c'est ici qu'on indexe les rapports annuels des cotées**
  (Tunisair, Ciments, Sotrapil, Sotumag…).
- `minenergie-steg-urls.csv` (STEG), `gbo-*` (lois de finances), `minfinances-*`.

→ **Pistes non encore exploitées** : la Cour des comptes (`cour-des-comptes-comptes-*`) peut porter des
comptes d'EP permettant VA/effectif pour des EP non cotées (SONEDE, ONAS, SNCFT, TRANSTU…) — à lire
avant de conclure « hors de portée ». `cdc-cloture-*` donne des résultats de clôture.

## 2. Documents ajoutés aujourd'hui — À INDEXER (sinon re-téléchargés)
Versés dans le corpus mais **pas encore inscrits** dans un `-urls.csv` :
- `data/raw/entreprises-publiques/bvmt-etats-financiers/tunisair/2023_individuel.pdf` (EF 2023, CMF)
  → à inscrire dans `bvmt-rapports-archives-urls.csv` ou l'équivalent EF.
- `data/raw/entreprises-publiques/rapports-entreprises/tunisair/{2020,2021,2022,2023}_rapport-de-gestion.pdf`
  (CMF rapports-societes) → à inscrire dans `bvmt-rapports-annuels-urls.csv`.
- Déjà rangés plus tôt : `rapports-ep-loi-finances/annexe9_LF20{20,21,22,24,25}*.pdf`,
  `etats-financiers-non-cotees/{tunisie_telecom_doc_reference_2010,gct_rapport_annuel_2013_part2,cpg_documentation_448656(+_ocr)}.pdf`.
  → à inscrire aussi.
- **Scratch de sous-agents à nettoyer** : `/tmp/verif/`, `/tmp/pq/` contiennent des copies de travail
  (onas2012, steg2023, sotumag/ciments fiches…) — **non autoritaires** ; re-télécharger dans le corpus
  si besoin, puis supprimer `/tmp`.

## 3. Donnée extraite en attente d'enregistrement
- **Tunisair VA brute** (EF 2023 individuel, état de soldes de gestion) : **148,085 MD (2023)** ;
  **161,889 MD (2022)**. Prolonge la VA Tunisair à 2023 (on s'arrêtait à 2022). VA/agent 2023 ≈
  148,085e6 / 3107 = **47 660 DT/agent**. À ajouter aux grandeurs, sourcé `…/tunisair/2023_individuel.pdf`.

## 4. (retiré)

Cette section portait un instantané opérationnel qui n'a pas sa place dans ce dépôt public ;
les notes et procédures correspondantes vivent dans le dépôt privé `tunisia-data` (son
`AGENTS.md` fait foi).
