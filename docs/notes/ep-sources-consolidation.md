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

## Mise à jour — extraction autonome (6 novembre 2026, rôle collecteur-donnees)

**VA/agent consolidée après cette salve** (kDT/agent) :
- **Tunisair** : 2006:77, 2007:79, 2016:74, 2018:64, 2019:80, **2020:19 (Covid)**, 2022:51, 2023:48.
- **STEG** : 2017:64, 2018:37, 2019:42, 2021:111, 2022:118, 2023:112.
- **Ciments de Bizerte** : 2015:36, 2016:35, 2017:33, 2018:36, 2019:80, 2020:113, 2021:91, 2022:46, 2023:28.
- **SOTRAPIL** : 2018:137, 2019:137, 2020:119, 2021:139 (la plus productive).

**Ajouts sourcés et vérifiés** :
- **Tunisair VA 2023** = 148,1 MD (EF individuel 2023, SIG, CMF ; déposé au corpus).
- **SOTRAPIL VA 2018-2021** (EF arabes, parseur NFKC, recoupé 2017 à 0,6 %).
- **Ciments effectifs 2015-2017** (538/518/553 ; rapports d'activité SCB, CMF ; 2016/2017 recoupés au document) → VA/agent remonte à 2015.
- **Tunisair effectifs mère 2006=2 966 et 2007=3 103** (indicateurs trimestriels CMF, couche texte, **vérifiés** ; corrigés hors personnel détaché aux filiales).

**Réserves / lacunes fermes** :
- **SOTRAPIL 2022-2025** : EF scannés trop dégradés → **OCR arabe inexploitable** (38-44 car.). VA s'arrête à 2021.
- **Tunisair effectifs mère 2008-2015** : lus par le collecteur dans les rapports annuels (scans OCR fra) **mais non re-vérifiables** (les scans déposés n'ont pas de couche texte) → **à re-vérifier par OCR** avant usage ; non ingérés. 2003-2005 absents en ligne.
- **Tunisair : rupture 2010→2011** (≈3 009→3 766) **non économique** (intégration statutaire d'agents de filiales, accord UGTT fév. 2011) + couture de définition « en activité » vs « total » → à expliciter dans toute figure VA/agent avant 2016.
- **Cour des comptes** : le catalogue tunisia-data (`cour-des-comptes-comptes-*`) ne donne que des **instantanés** CA + charges de personnel (±effectif) pour ~9 EP non cotées (SONEDE 2010, ONAS 2012, SNCFT 1998-99…) — **aucune consommation intermédiaire → pas de VA**, pas de série. Les utilities restent hors productivité.

**Outillage** : pack tesseract **arabe** sauvegardé (`~/.local/share/tessdata/ara.traineddata`) + méthode OCR arabe dans `tunisia-data/docs/methode-annuaires-scannes.md`.

### Bug parseur à corriger (modéliste) — Tunisair VA 2009/2010
`extraire_grandeurs_ep.py` lit la ligne **« Marge sur coût matières »** au lieu de **« Valeur
Ajoutée Brute »** pour Tunisair 2009 (770,765 au lieu de **260,636**) et 2010 (781,150 au lieu de
**254,643**) — le SIG Tunisair est en **colonnes multiples** (PRODUITS / CHARGES / SOLDES), et la
régex VA tombe sur la mauvaise colonne. 2008 (228,97) est correct. Correction provisoire versée à la
main dans `grandeurs-ep-non-cotees.csv` (prime). À corriger dans le parseur (ancrer la VA sur la
colonne SOLDES), puis régénérer et retirer l'override. **Vérifier les autres EP à SIG multi-colonnes**
(même risque).

## Couverture VA/agent FINALE (6 collecteurs, 6 nov. 2026) — 7 EP, 56 points
- **Tunisair 2006-2023** (16 pts ; trous 2017, 2021) — VA 2009/2010 corrigées (bug parseur) ; rupture effectif 2010→2011 (intégration statutaire, non-économique).
- **SOTRAPIL 2007-2021** (13 pts ; effectifs 2007-2017 lus des rapports annuels CMF, recoupés) — la plus productive (62k→139k).
- **Ciments de Bizerte 2015-2023** (9) ; **STEG 2014-2023** (8) ; **CPG 2006-2010** (5, pic 2008) ; **GCT 2012-2013** (2) ; **Tunisie Télécom 2007-2009** (3, mère 96-99k).
Lacunes fermes : SOTUMAG (effectif seul 2021, hors VA) ; Ciments 2010-2014 et 2024, Tunisair 2003-2005, SOTRAPIL 2022-2025 (scans dégradés) — introuvables/OCR impossible. Provenance : 0 valeur sans source.

## Complétions A+B (données en main, 6 nov. 2026)
- **A — Tunisair VA 2017 (277,7 MD) et 2021 (76,2 MD)** lues des SIG (colonne SOLDES) → **VA/agent Tunisair CONTINU 2006-2023 (18 ans, zéro trou)**.
- **A — non comblables** : STEG 2015/2020 et SOTRAPIL 2010/2011 → EF **scannés dégradés**, OCR (FR et AR) inexploitable. Lacunes fermes.
- **B — pas d'autre bug parseur** : Ciments 2013 (VA 3,6 MD, VA/revenus 7 %) et Sotumag (VA/revenus 90 %) sont des valeurs **réelles** correctement extraites (mauvaise année pour Ciments ; peu d'intrants pour Sotumag). Le bug « marge au lieu de VA » était isolé à Tunisair 2009/2010 (corrigé).
