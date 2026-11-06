# EP — consolidation des sources (qui fait foi pour quoi)

**6 novembre 2026.** Deux jeux de données sourcés existent, **complémentaires**. Cette note dit lequel
fait foi par variable, pour ne pas dupliquer. Voir aussi `ep-bilan-couverture.md` et
`ep-agregats-tendances-et-couverture.md`.

## Les deux gisements
1. **Précis — `precis/_seriescache/entreprises-publiques-*.csv`** (engendrés des **rapports annuels du
   ministère des Finances**, éditions LF2020→LF2025, **multi-édition et recoupés**, sourcés fichier +
   page + `derniere_edition` + divergences) :
   - `…-effectifs-par-entreprise.csv` (571 l.) : **effectif + charges de personnel** par EP/exercice.
   - `…-effectifs-ensemble.csv`, `…-resultats-agreges.csv` (90 l.) : **agrégats de secteur**.
   - `…-resultats-nets-dix-premieres.csv` (220 l.) : top-10 par résultat.
   - `…-fiches-entreprises.csv` (**8436 l.**) : **bilan + résultat par EP/exercice/indicateur**
     (LF2024/2025, bilingue).
   - `…-transferts-*`, `…-dividendes-etat`, `cdc-cloture-*` (Cour des comptes), `…-dettes-creances`.
2. **tunisia-data — `sources/entreprises-publiques/`** (lus des **états financiers primaires**,
   consolidés dans `consolidation-provenance.csv`, 1968 l., **0 valeur sans source**) :
   - `grandeurs-productivite-ep.csv` (BVMT + STEG), `grandeurs-ep-non-cotees.csv` (TT, GCT, CPG).

## Qui fait foi, par variable
| Variable | Source canonique | Remarque |
|---|---|---|
| **Effectif** par EP | **Précis** (rapports MdF, multi-édition) | couvre tunisair, steg, sotrapil, gct, cpg, etap, onas, sncft, transtu, ciments_bizerte… ; **pas sotumag** |
| **Agrégats de secteur** (produits/charges/subventions) | **Précis** (`resultats-agreges`) | mon `agregats-secteur-ep.csv` en est un sous-ensemble grossier → à abandonner au profit du précis |
| **Résultat net, CA, bilan** par EP (récent) | **Précis** (`fiches-entreprises`) | 2020-2024, issu des rapports MdF |
| **Valeur ajoutée (VA)** | **tunisia-data** (unique) | **absente** des rapports MdF ; calculée/ lue sur les EF primaires |
| **Résultat net / masse sal. longue durée** (cotées, banques) | **tunisia-data** | séries 2000-2024/25 depuis EF BVMT |
| **PNB** (banques) | **tunisia-data** | — |

**Complémentarité clé** : le précis apporte les **effectifs** (que les EF primaires n'ont pas) ;
tunisia-data apporte la **VA** (que les rapports MdF n'ont pas). Leur **jointure** produit la VA/agent.

## Produit de la jointure VA (tunisia-data) × effectif (précis) — VA/agent
- **Tunisair** (2016-2022) : 74k → 64k (2018) → 80k (2019) → **19k (2020, Covid)** → 51k (2022) DT/agent.
- **STEG** (2017-2023) : 64k → **37k (2018, creux)** → 42k → **111-118k (2021-2023)** DT/agent.
- **Ciments de Bizerte** (2018-2023) : 36k → 113k (2020) → 28k (2023) DT/agent. *(nouveau : aucun
  effectif ciments auparavant.)*
Non joignables faute de recouvrement temporel (VA ancienne, effectifs MdF récents) : CPG (VA 2006-10),
GCT (2012-13), Tunisie Télécom (2007-09), SOTRAPIL (VA →2017, effectifs MdF 2018→).

## Vérification indépendante (effectifs, 6 nov. 2026)
- **Tunisair** : série **société mère** officielle via les **indicateurs d'activité trimestriels**
  (CMF / BVMT) : 2017=3765, 2018=3781, 2019=3708, 2020=3432, 2021=3280, 2022=3193, 2023=3107,
  **2024=2852**. Elle **recoupe** les effectifs du précis (mêmes valeurs) et ajoute 2024. **Point
  validé** : ce sont des effectifs **société mère** (~3000-3800) ; le **groupe consolidé** (filiales
  Technics/Handling/Express) fait ~7000-7800 (presse, Cour des comptes). Notre VA Tunisair venant des
  **EF individuels (mère)**, la VA/agent est **homogène** — ne jamais y mêler l'effectif groupe.
  Lacune : effectif mère **2003-2016** non extrait (anciens PDF scannés/absents) → bloque la VA/agent
  Tunisair avant 2016.
- **SOTUMAG** : effectif **introuvable publiquement** (EF CMF 2007-2025, BVMT, rapports MdF, presse ne
  donnent que « charges de personnel », jamais un nombre d'agents). Seule voie : rapport de gestion AGO
  (papier) ou base payante. **Lacune ferme** → VA/agent SOTUMAG hors de portée.

## Conséquences pratiques
- **Ne plus produire** `agregats-secteur-ep.csv` ni rechercher des effectifs d'EP déjà dans le précis :
  le précis fait foi. Mon `effectifs-ep-rapports.csv` est **redondant** avec le précis (le garder comme
  recoupement, ou le retirer).
- **Seul SOTUMAG** manque vraiment côté effectif (recherche web en cours, ciblée).
- Pour la **VA/agent longue durée de Tunisair** (avant 2016), il faut des effectifs antérieurs
  (rapports de gestion Tunisair) — hors rapports MdF.
- Les **fiches-entreprises** du précis (8436 l., bilan+résultat récents) ouvrent des recoupements de
  nos CA/résultats, et un volet **financier** (ROE/ROA via bilan) sans extraction nouvelle.
