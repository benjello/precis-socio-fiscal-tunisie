# Bulletins MdF « Résultats de l'exécution du budget de l'État » — charge d'intérêt & solde

Note documentaire (documentaliste). Objet : repérer et **vérifier** les éditions annuelles
(« A fin Décembre » / « A fin [année] ») du bulletin du ministère des Finances (D.G.R.E.) qui
portent la table **« Équilibre du Budget de l'État »** avec, en lignes isolées et bilingues, la
charge d'intérêt (« Intérêts de la Dette » puis « Les charges de Financement (Intérêts de la
Dette) » / `فائدة الدين`) et le solde (« Solde Budgétaire » / `النتيجة`). But : série nationale
longue de la charge d'intérêt et du solde pour l'annexe dette, en comblant **2013-2020** (la BM
GFS `GC.XPN.INTP.CN` s'arrête à 2012) et en fournissant la **source nationale** pour toutes les
années atteignables.

Vérifications curl exécutées le **2026-11-10** (toutes HTTP 200). PDF à **couche texte** exploitable
(`pdftotext -layout`) sauf 2018 (Word .doc, texte). Rien n'est téléchargé dans un dépôt : URL
vérifiées pour rapatriement par `collecteur-donnees`. Les éditions antérieures à 2019 sont déjà au
catalogue `tunisia-data` (`data/raw/minfinances/portail_ancien/budget_execution/`,
`sources/minfinances-portail-ancien-urls.csv`) ; **les éditions 2019→2024 sont vives** sur
`finances.gov.tn` (nouveau site Drupal, `/sites/default/files/<AAAA-MM>/…`) **et pas encore au
catalogue**.

## Tableau des bulletins vérifiés

| Édition | AAAA-MM | Années d'exécution tabulées | Vif / Wayback | HTTP | Format | Clé suggérée |
|---|---|---|---|---|---|---|
| A fin Mai 2012 | 2012-05 | 2008-2011 (+ partiels) | Wayback | 200 | texte | `minfin-resultats-provisoires-2012-05` |
| A fin 2012 et Mars 2013 | 2013-03 | 2008-2012 (+ partiels) | Wayback | 200 | texte | `minfin-resultats-provisoires-2013-03` ✓ déjà en réf. |
| A fin Sept.+Oct. 2013 | 2013-10 | 2008-2012 (+ partiels) | Wayback (miroir dev) | 200 | texte | `minfin-resultats-provisoires-2013-10` |
| Rapport sem. A fin Déc. 2014 (ar) | 2014-12 | ~2010-2014 | Wayback | 200 | texte (ar) | `minfin-rapport-semestriel-execution-2014-12` |
| **A fin Décembre 2015** | 2015-12 | **2010-2015** (+ LF2016) | Wayback | 200 | texte | `minfin-resultats-provisoires-2015-12` ✓ déjà en réf. |
| Rapport sem. A fin Déc. 2016 (ar) | 2016-12 | ~2012-2016 | Wayback | 200 | texte (ar) | `minfin-rapport-semestriel-execution-2016-12` |
| A fin 2016 et Janvier 2017 | 2017-01 | **2012-2016** (+ LF2017) | Wayback | 200 | texte | `minfin-resultats-provisoires-2017-01` ✓ déjà en réf. |
| Note A fin Décembre 2018 | 2018-12 | **2014-2018** | Wayback | 200 | Word .doc (texte) | `minfin-note-execution-2018-12` ✓ déjà en réf. |
| **A fin 2019** | 2019-12 | **~2013-2019** (+ LF) | **Vif** (new site) | 200 | texte | `minfin-resultats-provisoires-2019-12` |
| **A fin Décembre 2020** | 2020-12 | **2016-2020** (+ LFR/LF) | **Vif** | 200 | texte | `minfin-resultats-provisoires-2020-12` |
| A fin Décembre 2021 | 2021-12 | ~2019-2021 (+ LFR/LF) | Vif | 200 | texte | `minfin-resultats-provisoires-2021-12` |
| A fin Décembre 2022 | 2022-12 | 2018-2022 (+ LFR/LF) | Vif | 200 | texte | `minfin-resultats-provisoires-2022-12` |
| A fin Décembre 2023 | 2023-12 | 2019-2023 (+ LFR/LF) | Vif | 200 | texte | `minfin-resultats-provisoires-2023-12` |
| A fin Décembre 2024 | 2024-12 | 2021-2024 (+ LF2025) | Vif | 200 | texte | `minfin-resultats-provisoires-2024-12` ✓ déjà en réf. |

URL exactes : voir `dette-execution-bulletins.csv` (colonne `url`).

## Ce que j'ai lu dans les tables (extraits vérifiés par pdftotext)

- **2015-12** : ligne `3.2 Intérêts de la Dette / فائدة الدين` = 1 152,0 / 1 189,6 / 1 267,6 /
  1 414,1 / 1 515,7 / 1 641,1 (prov. 2015) / 1 750,0 (LFC) / 1 850,0 (LF2016) ; ligne
  `5 Solde Budgetaire / النتيجة` = −650,4 … −4 043,7 / −3 664,0. Note de bas de table :
  « 5- Une mise à jour a été effectuée pour les années 2013-2014. » → **chiffres provisoires,
  révisés d'une édition à l'autre**.
- **Dec 2019** (« A fin 2019 ») : `3.2 Intérêts de la Dette` 9 colonnes (1 986,4 … 3 253,0 /
  3 191,5) ; `5 Solde Budgetaire` (−5 510,4 … −4 071,0 / −4 039,8). **Ajoute 2017, 2018, 2019.**
- **Dec 2020** : `3.2 Intérêts de la Dette` (1 986,4 / 2 259,6 / 2 801,9 / 3 204,5 / 4 134,0 /
  3 735,0 / 4 030,0) ; `5 Solde Budgetaire` (−5 510,4 / −5 986,7 / −5 055,4 / −4 059,7 /
  −13 015,0 / −11 603,2 / −7 944,0). **Ajoute 2020.**
- **Dep. Dec 2021** le libellé devient `6.2 Les charges de Financement (Intérêts de la Dette) /
  نفقات التمويل (فائدة الدين)` ; en **2022-2023** `6 Les charges de Financement` et
  `III Solde Budgetaire / Budget Balance / النتيجة`. **Colonnes : End December / End November /
  LF / LFR / LF** — bien distinguer les colonnes d'exécution des colonnes LF/LFR.

## Couverture et trous

- **2013-2020 (cible BM manquante) : intégralement couvrable en source nationale.**
  2013-2014-2015 ← 2015-12 ; 2016 ← 2017-01 (et Dec 2019/2020) ; 2017-2018-2019 ← Dec 2019 ;
  2020 ← Dec 2020.
- **2005-2024 : couvrable à partir de 2008** (2008-2012 ← 2012-05 / 2013-03 / 2013-10 ;
  2010-2024 ← chaîne Déc. ci-dessus). **TROU : 2005, 2006, 2007** — aucune édition trouvée dans
  le catalogue ni en ligne (les bulletins pré-2012 ne sont pas sur l'ancien portail archivé).
  Sur 2005-2012 la BM GFS reste disponible ; le **national** n'est atteint que 2008→.
- Les montants sont **provisoires** et **révisés** entre éditions : pour une série homogène,
  préférer, pour chaque année, la lecture **de l'édition de décembre la plus récente qui la porte**
  (p. ex. 2018 depuis Dec 2022 plutôt que depuis la note 2018-12), et garder une colonne de
  provenance par année.

## Lacunes / TODO pour le backlog

- **Bulletins exécution 2005-2007** introuvables (national) : à chercher dans les rapports annuels
  BCT (chap. finances publiques) ou le JORT — fiche de recherche à ouvrir si le national est exigé
  avant 2008.
- **Éditions 2019→2024 absentes de `tunisia-data`** : à rapatrier dans
  `data/raw/minfinances/…/budget_execution/` avec lignes au catalogue
  `sources/minfinances-portail-ancien-urls.csv` (ou nouveau CSV new-site), SHA-256 + date.
- Vérifier, à la lecture image, le **mapping exact colonne→année** des éditions 2021-2023
  (colonnes End December/End November/LF/LFR dédoublées) avant extraction chiffrée.

## Références candidates (CSL-JSON, clé = `minfin-resultats-provisoires-AAAA-MM`)

À créer (déjà en réf. : 2013-03, 2015-12, 2017-01, 2018-07, note-execution-2018-12, 2024-12) :
`-2019-12`, `-2020-12`, `-2021-12`, `-2022-12`, `-2023-12` (type `report`, author
« Tunisie. Ministère des Finances, D.G.R.E. », title « Résultats provisoires de l'exécution du
budget de l'État — A fin [Décembre] AAAA », URL = colonne `url` du CSV, issued = année d'édition).
