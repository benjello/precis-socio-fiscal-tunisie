# Consignes pour les agents

Ce fichier s'adresse à tout agent — quel que soit l'outil — qui travaille sur le « Précis de la
législation socio-fiscale de la Tunisie », ou sur les dépôts de modèle qui l'alimentent. Il est
versionné : c'est ici que les conventions vivent, pas dans la mémoire d'un assistant.

## Le dépôt en deux phrases

Cinq livres Quarto bilingues (`precis/fr/<livre>/`, `precis/ar/<livre>/`) — retraites, cotisations
sociales, prestations sociales, rémunérations publiques, fiscalité —, un glossaire bilingue
engendré depuis `precis/glossaire.yml`, une bibliographie CSL-JSON, et des tableaux de paramètres
engendrés depuis le dépôt `openfisca-tunisia`, qui porte aussi les retraites depuis sa version 0.93.

Le travail documentaire s'appuie sur le *Journal officiel* : métadonnées dans
`~/projets/PDFs-legislation-tunisie/jort_cache.db`, fascicules dans le corpus local du même dépôt,
et sur `pist.tn` en ligne. Voir `docs/notes/outillage-sources.md`.

## Invariants, quel que soit le rôle

- **Toujours `uv run`** pour Python — jamais `python3` ni `.venv/bin/python3`.
- **Le français est la source de vérité.** N'écris jamais un `.qmd` sous `precis/ar/` : la version
  arabe est produite par la CI. Les `references.json`, eux, se tiennent à la main dans les deux
  langues — et les **`_quarto.yml` aussi**.
- **Ne remets jamais les `_quarto.yml` dans la synchronisation de traduction.** Ils en sont exclus
  par le filtre du workflow *et* par `translate_sync.fichier_a_traduire()`. Motif : le fichier arabe
  porte des éléments qui n'ont **aucun original français** — `dir: rtl`, le bloc `language:` des
  libellés d'interface, les titres des parties du livre. Le traducteur ne peut pas les déduire du
  fichier français et les effaçait à chaque passage ; le livre arabe rendait alors 404 jusqu'au
  rattrapage à la main. Conséquence pratique : **quand tu ajoutes un chapitre côté français, ajoute-le
  toi-même au `_quarto.yml` arabe**, une fois sa traduction livrée — sans quoi il ne sera servi dans
  aucune des deux langues. Un fichier malformé ou des chapitres qui dérivent sont attrapés par
  `rendre-les-livres.yml`, qui rend les dix livres sur chaque PR.
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
  Seule exception : l'onglet « Base législative » des tableaux engendrés, qui lie chaque
  grandeur à sa page sur `parameters.tn.tax-benefit.org`. Ses liens sont engendrés avec le
  tableau (`tables/<nom>.liens.yml`), jamais écrits à la main.
- **Pas de jargon de dépouillement dans le texte visible** : ni « objet seul », ni « non lu », ni
  « métadonnées seules », ni `[T]`/`[M]`/`[D]`. On dit en clair ce qui est connu — « seul l'intitulé
  de ce texte est connu ici » —, ou on lit le texte.
- **Une recherche infructueuse ne se raconte pas** : ni « n'a pas été retrouvé », ni « au
  *Journal officiel* jusqu'au numéro du… ». Le texte dit le constat (« ce décret n'est pas
  identifié ici ») et porte une ancre `<!-- RECHERCHE r-… : … -->` vers une fiche rejouable de
  `docs/recherches.yml` — requêtes, sources, couverture datée, résultat. `scripts/recherches.py`
  la vérifie (CI), la relance et l'élargit.
- **Aucun chiffre ponctuel isolé** : toute valeur vient avec sa vue d'évolution datée. Et dans un
  tableau de textes, la colonne de contenu donne le changement concret — article, avant → après —,
  sinon la ligne n'a rien à y faire.

Les rôles éditoriaux — documentaliste, rédacteur, terminologue, bibliographe, relecteur-ar,
modeliste — sont décrits dans `docs/agents/<role>.md`, en texte neutre, indépendant de l'outil et
du fournisseur de LLM. La chaîne éditoriale va du premier au dernier, et s'arrête pour revue
humaine. Voir « Économiser » pour le lien vers `.claude/agents/`.

## Travailler sur les dépôts de modèle (rôle « modéliste »)

Dépôt concerné : `openfisca-tunisia`. Depuis sa version 0.93, il livre deux systèmes socio-fiscaux
qui lisent le même arbre de paramètres : le système fiscal (`openfisca_tunisia` — fiscalité,
cotisations, prestations) et celui des pensions (`openfisca_tunisia_pension`, extra `[pension]`),
qui n'en lit que `retraite/` et `marche_travail/`. Ce que chacun lit est déclaré dans
`openfisca_tunisia/sous_ensembles.py`. L'ancien dépôt `openfisca-tunisia-pension` n'est plus le
lieu des corrections. Ces conventions valent pour toute PR qu'un agent y prépare.

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
- **Ferme les tickets avec un mot-clé que GitHub reconnaît** : `Closes #30`, `Fixes #30`, `Resolves #30`.
  « Ferme l'issue #30 » n'en est pas un — le ticket reste ouvert après la fusion, et le correctif
  livré passe pour du travail en souffrance. Six tickets d'`openfisca-tunisia-pension` ont traîné
  ainsi (#27, #29, #30, #37, #40, #46) avant d'être fermés à la main, plusieurs jours après leur
  correction.
- **N'écris jamais le drapeau de saut d'intégration continue dans un titre de PR ni dans un message
  de commit**, même pour en parler. La fusion en squash fait du titre le sujet du commit ; GitHub y
  lit le drapeau et supprime **toutes** les exécutions sur `master` — déploiement et release-please
  compris. Les variantes comptent aussi : `[ci skip]`, `[no ci]`, `***NO_CI***`.
  Le 14/09/2026, la PR #208 du précis corrigeait précisément la propagation de ce drapeau aux commits
  de squash. Son titre le citait ; le commit de fusion `21ac558` n'a déclenché aucun workflow. Le
  correctif contre le drapeau a été éteint par le drapeau, et la release qui devait suivre n'a jamais
  été proposée.
  Le symptôme est une **absence**, jamais un échec : quand une pousse sur `master` ne produit aucune
  exécution, soupçonne le sujet du commit avant de soupçonner GitHub.

### Tester

- **Les tests s'écrivent en YAML OpenFisca**, dans `tests/formulas/` pour le système fiscal et dans
  `tests_pension/formulas/` pour celui des pensions, selon la convention déjà en place
  (`tests_pension/formulas/cnrps/pension.yaml`, `test_depart_anticipe.yaml`, `test_accessoires.yaml`). Les
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

**Déplacer un paramètre casse le précis, qui le lit par son chemin.** Un renommage ou un passage de
feuille à nœud rend le générateur muet — « paramètre introuvable ou vide » — et le contrôle
hebdomadaire de fraîcheur échoue sans qu'aucun commit du précis soit en cause. L'ordre n'est donc
jamais indifférent :

1. la PR du modèle annonce la dépendance dans son corps, et un ticket la consigne côté précis ;
2. la version est **publiée** ;
3. la borne de version du paquet est relevée dans `scripts/openfisca_tables.py`, avec son motif ;
4. les chemins sont corrigés, les snapshots régénérés, et l'on vérifie qu'ils sortent **identiques** —
   seul le chemin a changé, pas la valeur.

Corriger le précis avant la publication casse ses tableaux ; corriger après la publication, mais
trop tard, casse sa CI. Le 14 septembre 2026, deux paramètres déplacés le même jour ont produit les
deux cas.

## Économiser

- **Un seul appel plutôt qu'une chaîne à la main** : `scripts/verifier.sh [livre…]` enchaîne le
  glossaire, les contrôles de contenu, les liens, les tests et le rendu FR/AR des livres touchés,
  et n'affiche qu'un bilan compact (une ligne par étape). N'enchaîne les commandes une à une que
  pour diagnostiquer l'étape qui a échoué — le journal détaillé dont `verifier.sh` affiche le
  chemin sert à ça.
- **Le modèle suit la tâche.** Une tâche mécanique et bornée — fusion d'une branche, régénération
  d'un tableau ou d'un snapshot, rendu d'un livre, renumérotation d'un CHANGELOG — va sur un modèle
  léger : le résultat se vérifie par un contrôle (exit code, diff, test), pas par jugement. La
  lecture d'un texte de loi et la rédaction restent sur le modèle principal : c'est là que le
  jugement porte.
- **Ne relis pas un fichier que tu viens de lire ou d'écrire toi-même, sans raison de le croire
  changé.** Une Edit ou un Write réussis suffisent à savoir que le fichier est dans l'état voulu.
  Ceci ne vaut que pour TES propres appels dans la même tâche : un script (`build_glossary.py`,
  un rendu) ou un autre agent peut avoir réécrit le fichier entre-temps — relis-le si l'un des deux
  a pu s'exécuter depuis.
- **Les rôles éditoriaux sont indépendants de l'outil.** Le texte de chaque rôle vit dans
  `docs/agents/<role>.md` — prose simple, sans en-tête ni syntaxe propre à un outil. Ses
  métadonnées (`name`, `description`, `tools`) et un NIVEAU abstrait (`raisonnement` : la lecture
  d'un texte de loi et la rédaction, où le jugement porte ; `standard` : une méthode réglée sans
  arbitrage juridique ; `mecanique` : fusions, régénérations, rendus) vivent dans
  `docs/agents/roles.yml`, avec une table `modeles` qui traduit chaque niveau en nom de modèle,
  par outil. `.claude/agents/<role>.md` est **engendré** depuis les deux par
  `uv run python scripts/sync_agents.py` (`--verifier` pour la CI et `scripts/verifier.sh`) : ne
  l'édite jamais à la main, édite `docs/agents/<role>.md` ou `roles.yml` et régénère. Pour un
  autre outil (Codex, Cursor…) : charge `docs/agents/<role>.md` comme consigne et choisis le
  modèle dans `modeles.<outil>` de `roles.yml` selon le niveau du rôle — `sync_agents.py` ne
  fournit aucun générateur pour ces outils tant que leur format de sous-agent n'y est pas
  vérifié. Le lancement de sous-agents avec un modèle choisi par niveau est, lui, propre à Claude
  Code.

## Vérifier avant de rendre la main

```
scripts/verifier.sh [livre…]                                # glossaire, contrôles, liens, tests, rendu
uv run python scripts/build_glossary.py                    # verrou de synchro du glossaire
cd precis/fr/<livre> && uv run quarto render --to html     # zéro citation [?] non résolue
uv run python scripts/check_pas_de_modele.py               # le précis ne parle pas du modèle
./build.sh                                                  # les cinq livres, FR et AR
```

**Rends TOUS les livres que la PR touche, pas seulement celui qui l'occupe.** Aucun job de CI ne
rend les livres : un chapitre qui ne compile plus passe la revue sans que rien ne le signale. Le
14 septembre 2026, une figure a cassé le rendu des « Prestations sociales » — `IndexError` sur une
série vide — parce qu'elle lisait un paramètre openfisca absent du build ; le livre de la fiscalité,
lui, rendait parfaitement. Un seul rendu aurait laissé passer l'autre. `scripts/verifier.sh` sans
argument déduit les livres touchés du diff avec `origin/master` et de l'arbre de travail ; passe-les
en argument quand tu sais mieux que lui ce qu'il faut rendre.

Un module de figure lit **`figtools.series()`** — l'entrepôt ou son snapshot — et jamais directement
les paramètres du modèle : le build du site est autonome, `openfisca-tunisia` n'y est ni installé ni
déclaré.

`scripts/verifier.sh` restaure lui-même, après rendu, les `figdata` dont seule la date de génération
a changé. En dehors de lui — après un `./build.sh` ou un `quarto render` isolé — restaure-les à la
main : `git checkout -- precis/<langue>/<livre>/figdata`.
