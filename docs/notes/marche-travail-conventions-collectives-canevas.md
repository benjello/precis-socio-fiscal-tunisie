# Conventions collectives sectorielles — canevas d'une fiche de branche

Note de travail du 8 octobre 2026, pour la suite du chantier. Elle fixe **le canevas que chaque
convention de branche remplira** : sa création, ses éléments essentiels, et la suite datée de ses
avenants. Elle ne contient aucune donnée nouvelle.

## Pourquoi un canevas

Le chapitre « Les conventions collectives » porte aujourd'hui deux branches lues en profondeur —
le textile (1974, 1990-1992, 1994-2026) et le bâtiment-travaux publics (1975, 1990, 1996-2024) —
et un inventaire de 57 branches tiré des intitulés du *Journal officiel*. Les deux branches ont été
lues sans grille commune : ce qui a été relevé pour l'une ne l'a pas toujours été pour l'autre
(hauts de grille, indemnités, date d'effet de la convention d'origine).

Le canevas sert à trois choses :

- relever **les mêmes éléments, dans le même ordre**, pour chaque branche, de sorte qu'elles se
  comparent ;
- séparer ce qui est **établi** de ce qui est **à confirmer** ou **non lu**, case par case ;
- produire directement les lignes des séries du dépôt de données, sans ressaisie.

## Ce qui existe déjà et que le canevas prolonge

| Objet | Où | Ce qu'il porte |
|---|---|---|
| Inventaire des branches | `tunisia-data`, série `jort-conventions-collectives-branches` | une ligne par branche : agrément, *Journal officiel*, nombre d'avenants, dernier avenant ; rattachement par mots-clés, non relu |
| Agréments par année | série `jort-conventions-collectives-agrements-par-annee` | conventions et avenants agréés, 1969-2025 |
| Salaire d'entrée | série `conventions-collectives-salaire-entree` | textile et bâtiment : 62 dates d'effet, avec l'origine de chaque lecture |
| Notes documentaires | `docs/notes/marche-travail-conventions-collectives-fond.md` et `…-grilles-1996-2022.md` | requêtes rejouables, chaîne des textes, lectures, réserves |

Le canevas ne remplace aucune de ces séries : il dit ce qu'une branche doit apporter pour y entrer
complètement.

## Le canevas

Une fiche par branche. Chaque case dit sa source (*Journal officiel* : numéro, date, page, édition)
et son état : **lu** (dans le texte ou à l'image), **à confirmer**, **non lu**, **non précisé par
le texte**.

### 1. Identité

| Élément | À relever |
|---|---|
| Nom de la branche | l'intitulé exact de la convention, en français et en arabe |
| Champ d'application | les activités couvertes, telles que la convention les énumère ; les exclusions qu'elle écrit |
| Parties signataires | organisations d'employeurs et de salariés nommées par le texte |
| Branches voisines | scissions, fusions, conventions qui se recouvrent (par exemple la mécanique-électricité, scindée en 1999-2000) |

### 2. Création

| Élément | À relever |
|---|---|
| Date de signature de la convention | telle que le texte la donne |
| Arrêté d'agrément | date de l'arrêté ; *Journal officiel* (numéro, date, pages) |
| Publication du texte de la convention | *Journal officiel* (numéro, date, pages), s'il paraît à part de l'arrêté |
| Date d'effet | la clause du texte ; à défaut, la date à laquelle l'arrêté devient exécutoire, avec son calcul |
| Ce qui précède | sentence arbitrale, règlement de salaires ou convention antérieure que le texte remplace, s'il le dit |

### 3. Éléments essentiels, dans la rédaction d'origine

Ce qui commande le salaire et le coût du travail, et rien d'autre.

| Élément | À relever |
|---|---|
| Classification | nombre de catégories et d'échelons ; intitulé de la catégorie la plus basse et de la plus haute de la grille d'exécution |
| Salaire de base | grille d'origine : bas de grille, haut de grille, une catégorie médiane ; unité (heure, mois) ; régime horaire (48 ou 40 heures) |
| Ce que le salaire de base comprend | indemnités intégrées ou exclues, dont l'indemnité complémentaire provisoire |
| Indemnités forfaitaires | transport, présence, panier, autres : nom, montant, périodicité |
| Primes | ancienneté, rendement, fin d'année ou treizième mois : règle de calcul |
| Durée du travail | durée hebdomadaire, majoration des heures supplémentaires si la convention s'écarte du code |
| Avancement | règle de passage d'un échelon à l'autre, si elle joue sur le salaire |

### 4. Avenants, datés

Une ligne par avenant, dans l'ordre des numéros, **sans en sauter** : un numéro non retrouvé a sa
ligne, marquée « non lu ».

| Colonne | Contenu |
|---|---|
| Numéro | tel que l'avenant se nomme lui-même |
| Date de signature | de l'avenant |
| Arrêté d'agrément | date ; *Journal officiel* (numéro, date, pages, édition française ou arabe) |
| Objet | salaires ; classification ; indemnités ; autre — d'après l'intitulé et le texte |
| Dates d'effet | chaque date à laquelle une grille prend effet (un avenant triennal en porte trois) |
| Avant → après | bas de grille, haut de grille, indemnités : la valeur précédente et la nouvelle, à chaque date |
| Origine de la lecture | édition française ; édition arabe ; reproduction sur un site tiers, nommée |
| État | lu ; à confirmer (et pourquoi) ; non lu |

### 5. Ce que la fiche calcule

À chaque date d'effet, à partir de la série du SMIG : le SMIG horaire du régime correspondant, et
le rapport du bas de grille au SMIG. Les grilles qui excluent une indemnité que le SMIG comprend
ne portent pas de rapport (cas des grilles de 1990-1992).

### 6. État du droit et hausses par décret

| Élément | À relever |
|---|---|
| Dernière grille conventionnelle | date d'effet, valeurs, avenant |
| Hausses fixées par décret | décrets de majoration applicables à la branche (dont le décret n° 2026-68), avec ce que le texte dit de leur articulation avec la grille conventionnelle ; si rien n'est dit, l'écrire |
| Avenant le plus récent identifié | numéro et date ; fiche de recherche si la suite n'est pas identifiée |

### 7. Lacunes de la fiche

Liste courte : numéros d'avenant non lus, pages à contrôler, éléments non précisés par le texte.
C'est elle qui alimente `docs/notes/backlog-precis.md`.

## Destination : les paramètres d'openfisca-tunisia et une grande annexe

Décision du propriétaire, le 8 octobre 2026 : les fiches de branche iront **dans les paramètres
d'`openfisca-tunisia`** et **dans une grande annexe** du volume.

- **Les paramètres.** Chaque élément chiffré et daté d'une convention devient un paramètre, sous
  une arborescence par branche (par exemple
  `marche_travail/conventions_collectives/<branche>/salaire_base/<categorie>/<echelon>`, et de même
  pour les indemnités) : une valeur par date d'effet, la référence de l'avenant et du *Journal
  officiel* à chaque date. Les conventions du dépôt s'y appliquent telles quelles : date d'effet
  énoncée par le texte reprise sans report, sinon date d'exécution avec son calcul en note ;
  aucune valeur antérieure non sourcée ; unités déclarées ; aucune mention de variable ni de
  formule dans un fichier de paramètre. Une lecture faite sur une reproduction se dit dans la
  note de la valeur. Les sections 1 et 2 du canevas (identité, création) vont dans la description
  et les métadonnées du nœud de la branche.
- **L'annexe.** Elle est **engendrée depuis ces paramètres** par un générateur
  (`scripts/generate_*_tables.py`), comme tout tableau de paramètres du précis : une section par
  branche — sa création, sa grille à chaque date d'effet, ses avenants datés —, avec les
  composants déjà en place (état du droit à des dates repères, figure en escalier, onglet « Base
  législative »). Le chapitre garde le récit et les figures de synthèse, et renvoie à l'annexe
  pour le détail.
- **L'ordre.** Paramètres versés et datés dans une PR du modèle, version publiée, borne de version
  relevée dans `scripts/openfisca_tables.py`, puis annexe engendrée : jamais l'inverse. Les séries
  de `tunisia-data` versées le 8 octobre 2026 (salaire d'entrée du textile et du bâtiment) servent
  entre-temps aux figures du chapitre, et de contrôle : les paramètres devront redonner les mêmes
  valeurs aux mêmes dates.
- **Ce que cela implique pour la lecture.** Verser une grille en paramètres demande **toute la
  grille** — chaque catégorie et chaque échelon —, non le seul bas de grille relevé jusqu'ici pour
  le textile et le bâtiment. Le coût par branche est donc supérieur à celui observé le 8 octobre.

## Par où commencer

1. **Reprendre le textile et le bâtiment dans le canevas.** Cela fait apparaître ce qui leur
   manque encore : date d'effet des conventions de 1974 et de 1975, hauts de grille de certaines
   années, indemnités, avenants antérieurs à 1990 et de 1993 (textile), de 1991 à 1995 (bâtiment).
2. **Trois branches ensuite**, choisies pour leur poids dans l'emploi et parce que leurs grilles
   de 1996 sont déjà repérées : commerce de gros, demi-gros et détail ; industrie hôtelière ;
   mécanique générale et électricité (plus coûteuse, la branche se scindant en 1999-2000).
3. **Les autres branches par vagues**, en commençant par celles qui comptent le plus d'avenants
   (pétrole, boissons alcoolisées, pharmacies d'officine, imprimerie, industrie laitière,
   bonneterie et confection).

Coût observé le 8 octobre 2026 : lire neuf avenants de 1996 à 2009 dans l'édition arabe a pris une
dizaine de minutes une fois les fascicules repérés ; compter une passe d'environ quarante minutes
par branche pour la chaîne complète des avenants, hors indemnités.

## Règles à tenir en remplissant

- Une valeur lue sur une reproduction ou un site tiers se marque comme telle ; elle ne passe
  jamais pour une lecture du *Journal officiel*.
- Aucune interpolation : une date sans grille lue n'a pas de valeur.
- Le rattachement d'un avenant à une branche se fait sur son texte, non sur les mots-clés de son
  intitulé : quatre avenants sont aujourd'hui comptés dans deux branches (mécanique générale et
  pétrole ; gardiennage et assurances).
- Depuis les avenants de 1996, les grilles ne paraissent que dans l'édition arabe : c'est elle
  qu'on lit, et la référence le dit.
- L'économique d'abord : classification, salaire, indemnités, durée. Les clauses de procédure,
  de discipline et de représentation ne sont pas relevées.

## Questions à trancher

1. Grille entière ou grille résumée dans les paramètres : toutes les catégories et tous les
   échelons, ou le bas, le haut et une catégorie médiane ? La première voie permet de calculer un
   salaire conventionnel ; la seconde suffit aux figures.
2. Les indemnités forfaitaires entrent-elles dans le salaire comparé au SMIG, ou restent-elles à
   part comme aujourd'hui ?
3. Jusqu'où remonter : aux conventions d'origine seulement, ou aux sentences et règlements de
   salaires qui les précèdent ?
4. Combien de branches le chapitre doit-il porter en figure avant que celle-ci ne devienne
   illisible — et faut-il alors une figure par famille de branches ?
