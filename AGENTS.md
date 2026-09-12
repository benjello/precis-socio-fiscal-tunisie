# Consignes pour les agents

Ce fichier s'adresse à tout agent — quel que soit l'outil — qui travaille sur le « Précis de la
législation socio-fiscale de la Tunisie », ou sur les dépôts de modèle qui l'alimentent. Il est
versionné : c'est ici que les conventions vivent, pas dans la mémoire d'un assistant.

## Le dépôt en deux phrases

Cinq livres Quarto bilingues (`precis/fr/<livre>/`, `precis/ar/<livre>/`) — retraites, cotisations
sociales, prestations sociales, rémunérations publiques, fiscalité —, un glossaire bilingue
engendré depuis `precis/glossaire.yml`, une bibliographie CSL-JSON, et des tableaux de paramètres
engendrés depuis les dépôts `openfisca-tunisia` et `openfisca-tunisia-pension`.

Le travail documentaire s'appuie sur le *Journal officiel* : métadonnées dans
`~/projets/PDFs-legislation-tunisie/jort_cache.db`, fascicules dans le corpus local du même dépôt,
et sur `pist.tn` en ligne. Voir `docs/notes/outillage-sources.md`.

## Invariants, quel que soit le rôle

- **Toujours `uv run`** pour Python — jamais `python3` ni `.venv/bin/python3`.
- **Le français est la source de vérité.** N'écris jamais un `.qmd` sous `precis/ar/` : la version
  arabe est produite par la CI. Les `references.json`, eux, se tiennent à la main dans les deux
  langues.
- **Ne modifie pas les fichiers engendrés** : `_glossaire.qmd`, `translation_glossary.generated.md`,
  `precis/*/*/tables/*`.
- **Aucune valeur, aucune date, aucune URL sans source vérifiée.** Une case vide honnête vaut mieux
  qu'une valeur plausible. URL du JORT sur `pist.tn` uniquement, dans l'édition de la langue du
  fichier.
- **Ne committe pas** sans que l'humain ait relu, sauf consigne explicite. N'ouvre ni PR ni issue de
  ta propre initiative.
- **OCR** : lance les océrisations au premier plan ou attends-les, et ne laisse aucun processus
  tourner en fin de tâche. **N'emploie jamais `pkill` sans cibler tes propres processus** : d'autres
  agents travaillent en parallèle dans le même répertoire de session.

## Écrire dans le précis

`docs/conventions-redaction.md` fait foi. Les trois règles qu'on oublie le plus :

- **Le précis documente la loi, jamais le modèle.** Ni `openfisca`, ni « le modèle », ni « les
  paramètres » dans le texte rendu. Un constat sur le modèle va dans un `<!-- TODO (rôle) : … -->`,
  dans une *issue*, ou dans `docs/notes/backlog-modele.md`. `scripts/check_pas_de_modele.py` le
  vérifie.
- **Pas de jargon de dépouillement dans le texte visible** : ni « objet seul », ni « non lu », ni
  « métadonnées seules », ni `[T]`/`[M]`/`[D]`. On dit en clair ce qui est connu — « seul l'intitulé
  de ce texte est connu ici » —, ou on lit le texte.
- **Aucun chiffre ponctuel isolé** : toute valeur vient avec sa vue d'évolution datée. Et dans un
  tableau de textes, la colonne de contenu donne le changement concret — article, avant → après —,
  sinon la ligne n'a rien à y faire.

Les rôles éditoriaux sont décrits dans `.claude/agents/` : documentaliste, rédacteur, terminologue,
bibliographe. La chaîne va du premier au dernier, et s'arrête pour revue humaine.

## Travailler sur les dépôts de modèle (rôle « modéliste »)

Dépôts concernés : `openfisca-tunisia` (fiscalité, cotisations, prestations) et
`openfisca-tunisia-pension` (retraites). Ces conventions valent pour toute PR qu'un agent y prépare.

### Dater

- **Une date d'effet énoncée par le texte est reprise telle quelle**, sans report au premier du mois.
- **Sans clause d'effet**, retiens la date à laquelle le texte devient exécutoire, et écris le calcul
  dans la `note` :
  - avant 1993, « un jour franc après la publication au Journal Officiel » — article 3 nouveau du
    décret du 27 janvier 1883, rédaction du décret du 13 septembre 1956 ;
  - depuis 1993, « cinq jours après le dépôt du journal officiel au siège du gouvernorat de Tunis »,
    jour du dépôt non compté — loi n° 93-64, article 2.
- **Jamais la date de signature ni la date de publication brute.**
- **Une valeur antérieure identique à la valeur sourcée, laissée sans référence, n'est pas un état du
  droit** : elle disparaît, et le paramètre commence à la date sourcée — même si des calculs
  antérieurs cessent alors d'aboutir. Une erreur explicite vaut mieux qu'une valeur inventée. À ne
  pas confondre avec un état antérieur réellement établi par un autre texte, qui se garde avec sa
  propre référence.

### Découper

- **Une PR, un sujet.** Empile les branches plutôt que de grouper : chaque PR se relit et se date.
- **Crée les variables d'entrée nécessaires** quand une règle est conditionnelle — droit acquis,
  option de l'employeur, indemnité exclue d'une assiette. Donne-leur une valeur par défaut qui ne
  change rien aux cas courants. Ne t'arrête pas à une demi-correction en posant une « question
  ouverte » là où une variable réglerait le sujet.
- Le corps de chaque PR porte une section **« Questions ouvertes »** pour ce que la revue doit
  trancher.
- **Ne fusionne jamais**, et attends la CI.

### Tester

- **Les tests s'écrivent en YAML OpenFisca dans `tests/formulas/`**, dans la convention déjà en place
  (`tests/formulas/cnrps/pension.yaml`, `test_depart_anticipe.yaml`, `test_accessoires.yaml`). Les
  valeurs attendues y sont écrites en clair, tirées du droit et des paramètres.
- Une démonstration « à résultats inchangés » se rend par **une table de cas explicite**, avec les
  bornes de chaque seuil, et non en reconstruisant en Python l'arithmétique que la PR supprime.
- **Deux pièges connus** :
  - un test YAML dont la période annuelle commence en cours d'année (`period: year:1985-06-01`)
    **ignore silencieusement ses entrées**. C'est le seul cas qui justifie un test Python, et il doit
    alors être déclaré dans le corps de la PR ;
  - **`make test` ne lance pas `yamllint`**, dont la CI tient compte : lance la cible YAML avant de
    pousser.
- Si un résultat existant change, ne modifie pas le test en silence : explique-le dans le rapport et
  dans le CHANGELOG, et ne corrige le test que si la nouvelle valeur est celle du texte.

### Publier

- Lis le `CONTRIBUTING.md` du dépôt : le niveau d'incrément de version suit la nature du changement,
  et l'entrée de CHANGELOG en épouse le niveau de titre. Vérifie avec
  `.github/is-version-number-acceptable.sh`.
- Régénère ce qui se régénère — notamment `reports/openfisca/pension_source_audit.md` — et vérifie
  que le diff ne porte que sur ton sujet.

### Rendre au précis

Les tableaux de paramètres du précis doivent venir des dépôts de modèle **par un générateur**
(`scripts/generate_*_tables.py`), jamais être recopiés à la main. Un tableau fait main est toléré
en attendant que les paramètres soient datés et sourcés en amont, et porte alors un
`<!-- TODO (rédacteur) : remplacer par un tableau engendré -->`. On ne régénère jamais un tableau
qui dépend d'une PR openfisca non fusionnée : la CI régénère depuis `master`.

## Vérifier avant de rendre la main

```
uv run python scripts/build_glossary.py                    # verrou de synchro du glossaire
cd precis/fr/<livre> && uv run quarto render --to html     # zéro citation [?] non résolue
uv run python scripts/check_pas_de_modele.py               # le précis ne parle pas du modèle
./build.sh                                                  # les cinq livres, FR et AR
```

Et restaure les `figdata` dont seule la date de génération a changé :
`git checkout -- precis/<langue>/<livre>/figdata`.
