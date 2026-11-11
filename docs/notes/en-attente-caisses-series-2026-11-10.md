# En attente — chantier « séries de la longue période » des caisses (10 novembre 2026)

Note-relais du chantier `chantier/caisses-series`. Elle consigne ce qui est fait, ce qui reste,
et les reports **routés par destination** (cf. `docs/backlog-routage.md`). Rien ici n'est committé :
la revue humaine précède tout commit, dans ce dépôt comme dans `tunisia-data`.

## Fait (à relire avant commit)

Les quatre séries du § 3 de `cadre-budgetaire-comptable-caisses.md` sont instruites, et la série (1)
est extraite dans l'entrepôt.

| Série | Livrable | Verdict |
|---|---|---|
| (1) Comptes des organismes S1314, INS 2001-2025 | note `caisses-serie-comptes-organismes-notedoc-2026-11-10.md` + **extraction tunisia-data** | couverture pleine, 2 segments (base 1983 2001-2014 ; base 2015 2015-2025) ; contrôles § 3 exacts ; rupture de base quasi nulle pour le S1314 |
| (2) Versements des caisses au tableau A, 1985-2004 | note `caisses-serie-versements-tableau-a-notedoc-2026-11-10.md` (337 l.) | couverture **pleine 1985-2005, 100 % [T]** ; réalisations des lois de règlement **introuvables au JORT** |
| (3) CNSS post-2004 (autre session) | note `caisses-serie-cnss-post-2004-notedoc-2026-11-10.md` (430 l.) | couverture 2005-2023 par morceaux ; **trous honnêtes 2005-2008, 2011, 2014** ; comptes par régime jamais publiés après 2004 |
| (4) Répartition de la CSS | note `caisses-serie-css-repartition-notedoc-2026-11-10.md` (297 l.) | seule la **part CNRPS** (200/450/460/500/195/420 MD, 2018-2023) chiffrable ; produit total et parts CNSS/CNAM = trou ; **arrêtés de répartition introuvables** (jugés non publiés au JORT) |

**Bibliographie versée** (5 clés, FR+AR, `caisses/references.json`, dry-run propre, 0 perte) :
`dgi-nc-28-2019`, `dgi-nc-1-2023`, `dgi-nc-1-2026` (notes communes CSS), `cnss-annuaire-statistique`,
`cnss-etats-financiers-2018`. Report bibliographe consigné dans `biblio-a-rapatrier.md`.

**Rédaction série (1) faite.** Vue consolidée S1314 2001-2025 ajoutée à
`precis/fr/caisses/_comptes_longue_periode.qmd` (section `#sec-caisses-s1314`, figure
`fig-caisses-s1314-organismes`), module `precis/fr/caisses/figures/s1314_organismes_2001_2025.py`,
figdata engendrée. Quatre vues (cotisations vs prestations ; capacité/besoin de financement en MD et
en % PIB ; transferts entre APU), deux segments base 1983/2015 jamais raccordés, points 2024-2025
évidés. Snapshot `precis/_seriescache/ins-comptes-organismes-securite-sociale.csv` produit.
`scripts/verifier.sh caisses` : tout passé, 0 citation `[?]`. Glossaire non touché.
**Rédaction séries (2) et (4) faite.** `_comptes_longue_periode.qmd` : section
`#sec-caisses-versements-budget` (série 2, figure `fig-caisses-versements-budget`, module
`figures/tableau_a_caisses_1985_2005.py`, série `lf-tableau-a-caisses` construite dans tunisia-data +
snapshot) et `#sec-caisses-css-cnrps` (série 4, figure `fig-caisses-css-cnrps`, module
`figures/cnrps_css_2018_2023.py`, séries `cnrps-ratios-charges-produits` + `cnrps-ue-jumelage-2021`).
Valeurs exactes (16/37/57/62,5 ; CSS 200/450/460/500/195/420), rupture 1994→1995 montrée, trous
honnîtes (réalisations hors JORT ; produit total CSS et parts CNSS/CNAM inconnus). `verifier.sh
caisses` tout passé, 0 `[?]`, glossaire intact. Clés biblio versées (3 rapports série 4 + 2 lois de
règlement témoins reglement-1992/2001).
**Dette biblio (traitée).** Les 10 clés « provisoires » du rédacteur sont en fait les sources
déclarées par le catalogue tunisia-data (`cnrps-ratios-charges-produits`, l. 2050-2051) : `mas-rap`,
`mas-pap-2025` et les `lf-YYYY`. Les 8 `lf-YYYY` résolvent déjà en AR via le fonds partagé
`precis/ar/references.json` (alias transitoires). `mas-rap`/`mas-pap-2025` manquaient en AR →
**ajoutés à `precis/ar/caisses/references.json`** (identiques à FR, cohérence verte) pour éviter un
`[?]` au rendu arabe après traduction. Reste, pour la clôture bibliographe : éclater `mas-rap` par
édition RAP (polissage Zotero, non bloquant) ; `minfin-ep-2021` si citée nommément. Coexistence
`lf-YYYY`/`loiNN-NN-lfYYYY` = dette préexistante transversale, hors chantier.
**Rédaction série (3) faite.** `_comptes_longue_periode.qmd` : section `#sec-caisses-cnss-post-2004`
(figure `fig-cnss-comptes-post-2004`, module `figures/cnss_comptes_post_2004.py`), séries
`cnss-produits-charges-techniques` (2000-2020) et `cnss-resultat-exercice` (2009-2023 lacunaire)
construites dans tunisia-data + concordance `sources/cnss-concordance-perimetres-post-2004.md`.
Solde technique R−D **distingué** du résultat (2012 : +38,8 vs −78,1 ; 2018 : −332 vs −530,5 ;
2020 : −754 vs −1091,5), trous honnîtes 2005-2008/2011/2014, rupture CNAM 2007-2008 marquée,
financement 2016-2018 dit sans trancher. `verifier.sh caisses` passé, 0 `[?]`, glossaire intact.
**Les quatre séries sont rédigées** : le chapitre longue période a six sections.
**Report** : comptes par régime et emplois par branche post-2004, placements/réserves en série,
revenus de la propriété et transferts APU avant 2005 — non tracés (passes ultérieures). Clé
`minfin-ep-2021` à créer si l'édition LF 2021 doit être citée nommément (bibliographe).

## Fusion origin/master (PR #794 santé) — à faire

Master est 15 commits en avance. Mon arbre ne recouvre ses changements que sur DEUX fichiers de type
« ajout en fin » : `docs/notes/biblio-a-rapatrier.md` et `precis/_seriescache/catalog.snapshot.yml`
(union des séries). Les fichiers engendrés du glossaire ne sont pas dans mon arbre (glossaire.yml
non touché) → prendre master puis `uv run python scripts/build_glossary.py`. Les `references.json`
caisses ne sont pas touchés par #794. Prérequis : git mutatif (/toggle-allow-git) ET commit du
chantier (revue humaine) avant merge d'un arbre non propre.

**Invariant éditorial maintenu** : le solde technique (produits − charges) de la série (3) **ne
remplace pas** le résultat (écart mesuré 60-350 MD/an) — approximation refusée ; aucun raccord muet
entre segments ou entre bases.

## Fichiers à placer sur les bonnes branches (git mutatif bloqué en session)

**Dépôt précis (ici, branche `chantier/caisses-series`)** — nouveaux :
`docs/notes/caisses-serie-comptes-organismes-notedoc-2026-11-10.md`,
`caisses-serie-versements-tableau-a-notedoc-2026-11-10.md`,
`caisses-serie-css-repartition-notedoc-2026-11-10.md`,
`caisses-serie-cnss-post-2004-notedoc-2026-11-10.md`, cette note ; modifiés :
`precis/fr/caisses/references.json`, `precis/ar/caisses/references.json` (+108 l. chacun, additions
pures), `docs/notes/biblio-a-rapatrier.md` (+26 l.), `precis/fr/caisses/_comptes_longue_periode.qmd`
(section S1314), `precis/_seriescache/catalog.snapshot.yml` (snapshot S1314) ; nouveaux non suivis :
`precis/fr/caisses/figures/s1314_organismes_2001_2025.py`,
`precis/_seriescache/ins-comptes-organismes-securite-sociale.csv`,
`precis/fr/caisses/figdata/fig_caisses_s1314_organismes.csv(.yml)`.

**Entrepôt `tunisia-data`** — l'arbre est sur `chantier/donnees-dette-publique` et contient AUSSI des
travaux d'autres agents (éducation, santé/OMS, CTAMA) : **ne committer que les fichiers S1314**.
Nouveaux : `scripts/extract_cnat_s1314.py`,
`data/processed/ins-comptes-nationaux/s1314_toutes_editions.csv`, `…/s1314_serie_retenue.csv`,
`…/s1314_concordance_2015_2017.csv`, `docs/cnat-s1314-comptes-organismes-securite-sociale.md` ;
modifiés (additions seules, 104 l.) : `catalog.yml`, `sources/ins-comptes-nationaux-publications.md`.

## Backlog durable, routé par destination

### Chapitre du précis (`backlog-precis.md` — proposé ici, à appliquer par l'archiviste-backlog)
- **Longue période des caisses rédigeable** une fois les séries validées : vue consolidée S1314
  (série 1), versements au budget (série 2), CNSS post-2004 par morceaux (série 3), part CNRPS de la
  CSS (série 4). Garder les **trous honnêtes** visibles (2005-2008, 2011, 2014 ; comptes par régime
  absents après 2004) et la rupture de base/périmètre jamais lissée.
- `_etat_caisses.qmd` : 4 TODO / 2 RECHERCHE encore ouverts, à solder avec les séries.
- Section « Ce qu'en dit l'économie » **absente** du volume (gouvernance, placements, compensation
  entre régimes) — à confier à l'économiste.

### Données / séries / OCR de l'entrepôt (notes de `tunisia-data`)
- **S1314** : L-s1.1 détail par caisse hors source ; L-s1.2 composition du S1314 inconnue ;
  L-s1.3 2024 semi-déf. / 2025 prov. à rafraîchir à l'édition 2022-2026 ; L-s1.4 page 2018 sans PDF ;
  L-s1.6 édition 2003-2007 décalée (labels par heuristique, valeurs justes) ; L-s1.7 compte financier
  non réconcilié ; L-s1.8 recoupement TOFE FMI / rapport EP à faire.
- **Série (3)** (§ 9 de sa note) : index des pages financières des annuaires CNSS à dresser ; OCR de
  la page « indicateurs » de l'annuaire 2006 ; **Wayback à relancer** (éditions CNSS en ligne).
- **Série (2)** : OCR ciblé des 21 folios de tableaux A recensés ; arrêté du 6 janvier 1987 (L14,
  contribution familles nécessiteuses par organisme) à océriser → série courte des montants.

### Fiches de recherche (`docs/recherches.yml` — passes proposées, non appliquées)
- `r-css-arretes-repartition` : passe datée (balayage plein texte 712 fascicules 2022-2026 négatif ;
  seule occurrence « تنويع مصادر الضمان الاجتماعي » = LF 2022 création et LF 2026 art. 20).
- `r-recettes-caisses-realisees` (série 2, L-R1) : réalisations des caisses introuvables au JORT ;
  pistes projet de loi de règlement / Cour des comptes / exécution MinFin.
- `r-forfait-hospitalier-caisses-origine` (série 2, L-R2) : antériorité des forfaits hospitaliers
  avant 1985.

### Bibliographie (`biblio-a-rapatrier.md` — déjà consigné)
- Rapatriement Zotero des 5 clés ; **fiches base législative** `tunisia-legislative-references` à
  créer pour NC 28/2019 et NC 1/2026 (NC 1/2023 déjà cataloguée `note_commune_2023_001`).
- **Point à trancher** : id CSL `dgi-nc-1-2023` vs id de catalogue `note_commune_2023_001`.
- Clés à créer pour rendre citables les séries (2)-(4) : `lf-1985,-1986,-1987,-1989,-1990,-1991,
  -1992,-2002`, compléter `loi-87-83-lf-1988`, 20 clés `reglement-<gestion>` ; `minfin-rapport-ep-2022`,
  `ue-jumelage-retraite-2021`, `mas-rap-cnrps-2022` ; vérifier `lf-2022` (art. 12, pp. 3081-3082) et
  `lf-2026` (art. 20).

## En attente de décision / hors de ma main
- Les **comptes par régime de la CNSS après 2004** n'existent dans aucune source lue : lacune de
  fond, pas un défaut de dépouillement.
- Rédaction du chapitre « longue période » : à lancer (rédacteur) une fois les séries validées et les
  données S1314 placées/commitées côté entrepôt.
