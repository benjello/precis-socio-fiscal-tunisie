# Note documentaire — Structure de la fonction publique (INS) : matière à figures

> Matière sourcée pour les figures du chapitre **Rémunérations publiques**
> (`precis/fr/remunerations_publiques/`). Figure(s) à produire dans une session
> dédiée. Cette note fige **la structure de la source, ce qui est exploitable, et
> les enseignements/réserves** — elle ne produit pas encore les graphiques.

## Source

INS, **« Caractéristiques des agents de la fonction publique et leurs salaires
2010-2021 »** (publication juin 2023 ; tableaux salaires nov. 2022). Tableaux
bilingues AR/FR.

- URL : <https://www.ins.tn/enquetes/caracteristiques-des-agents-de-la-fonction-publique-et-leurs-salaires-2010-2021>
- **Raw rapatrié** (37 fichiers Excel) : dépôt `tunisia-data`,
  `data/raw/ins-fonction-publique-salaires-2010-2021/`.
- Fiche de source complète + manifeste des 37 fichiers :
  `tunisia-data/sources/ins-fonction-publique-salaires-2010-2021.md`.
- Catalogue : entrée `fonction-publique-effectifs` dans `tunisia-data/catalog.yml`.
- **Déjà nettoyé** (`tunisia-data/scripts/clean_ins_fonction_publique.py`) : seulement
  `tab1` → `effectifs_evolution.csv` et `tab18` → `salaire_mensuel_evolution.csv`.
  Les tableaux de structure ci-dessous sont **dans le raw mais pas encore extraits**.

## Périmètre / dénominateurs (à rappeler en légende de figure)

- Champ = **fonction publique** (agents civils de l'État). Décliné **hors
  collectivités locales / collectivités locales / total**. **Exclut** entreprises
  publiques et secteur public consolidé.
- Effectifs en **milliers d'agents** ; salaires en **dinars courants/mois**, brut
  (avec et sans contributions) et net.
- Couverture : effectifs surtout **2015-2021** (photo 2021) ; salaires **2015-2020** ;
  annexes annuelles complètes **2010-2020**.

## Tableaux exploitables par type de figure

| Figure envisageable | Tableau(x) INS | Variable |
|---|---|---|
| Évolution des effectifs FP (hors/avec coll. locales) | `tab1` (✓ nettoyé) | milliers d'agents, 2015-2021 |
| Effectifs par **sexe** ; pyramide des **âges** | `tab2`, `tab3`, `tab4` | milliers / % |
| Effectifs par **catégorie statutaire** (A1/A2/A3/B/C/D) | `tab5`–`tab8` | milliers / structure % |
| **Ouvriers** par unité (I–X) | `tab9` | milliers |
| Effectifs par **ministère** | `tab10`, `tab11` | milliers |
| Effectifs par **fonction** | `tab12`, `tab13` | milliers |
| **Flux** entrants/sortants (âge, sexe, type, ministère) | `tab14`–`tab17` | milliers |
| Salaire mensuel brut moyen, série | `tab18` (✓ nettoyé), `tab19` | dinars/mois |
| Salaire brut moyen **par catégorie** | `tab20_0` | dinars/mois |
| Salaire brut **ouvriers** par unité | `tab21_0` | dinars/mois |
| **Distribution** par tranches de salaire (fonctionnaires / ouvriers) | `tab22`–`tab24` | % |
| Salaire moyen brut & net **par ministère** (2020) | `tab25`, `tab26` | dinars/mois |

Figures les plus parlantes pour le chapitre : **structure par catégorie** (tab5-8,
empilé/structure %), **salaire moyen par catégorie** (tab20), **salaire par
ministère** (tab25-26), **pyramide des âges 2021** (tab3).

## Enseignements / réserves (à NE PAS oublier en produisant les figures)

- **Rupture de série collectivités locales 2016→2017** : effectif ~6,7 k → ~17,7 k
  dans `tab1` = changement de périmètre/comptage probable. Signaler avant tout usage
  en série longue ; préférer la série **hors collectivités locales** pour la tendance.
- En-têtes d'années **bruités** (espaces insécables `\xa0`, années en texte) → la
  fonction `to_year`/`to_num` du script de nettoyage les normalise ; réutiliser la même.
- Annexes **2015-2019 en `.xls`** (binaire ancien, code page 1256) ; le reste `.xlsx`.
- Libellé **FR = dernière colonne**, AR = colonne A. Toujours retenir le FR.
- La source donne **effectifs + salaires moyens**, **pas** la masse salariale en
  % du PIB/budget (pour ça → `docs/notes/perimetre-masse-salariale.md`, FMI/BM).
- Source primaire tunisienne → **prioritaire sur FMI/BM pour les effectifs** FP.

## Lien avec le micro-simulateur (hors champ figures, pour mémoire)

Granularité INS = **catégorie statutaire + ministère**, pas le corps/grade. Le calage
des cas-types `salaire_base` d'openfisca-tunisia se fera donc en **agrégeant les ~100
corps par catégorie** puis en calant sur tab5-8 (effectifs) + tab20 (salaire moyen)
comme validation des masses reconstruites. Travail à mener côté openfisca-tunisia,
distinct des figures du précis.
