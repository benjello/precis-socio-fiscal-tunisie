# Travailler sur les dépôts de modèle (rôle « modéliste »)

<!-- Détail déplacé d'AGENTS.md le 17/11/2026 (source unique) ; AGENTS.md y renvoie en une ligne. -->


Dépôt concerné : `openfisca-tunisia`. Depuis sa version 0.93, il livre deux systèmes socio-fiscaux
qui lisent le même arbre de paramètres : le système fiscal (`openfisca_tunisia` — fiscalité,
cotisations, prestations) et celui des pensions (`openfisca_tunisia_pension`, extra `[pension]`),
qui n'en lit que `retraite/` et `marche_travail/`. Ce que chacun lit est déclaré dans
`openfisca_tunisia/sous_ensembles.py`. L'ancien dépôt `openfisca-tunisia-pension` n'est plus le
lieu des corrections. Ces conventions valent pour toute PR qu'un agent y prépare.

### Dater

- **La date d'effet est très importante : cherche-la, dans cet ordre.**
  1. **Une date d'effet énoncée par le texte est reprise telle quelle**, sans report au premier du
     mois. Une clause relative (« six mois à compter de sa publication ») se calcule, quantième à
     quantième, à partir de la publication.
  2. **Sinon, la date calculée par la règle d'entrée en vigueur**, quand elle s'applique, avec le
     calcul écrit dans la `note` :
     - avant 1993, « un jour franc après la publication au Journal Officiel » — article 3 nouveau du
       décret du 27 janvier 1883, rédaction du décret du 13 septembre 1956 ;
     - de 1993 au 13 avril 2020, « cinq jours après le dépôt du journal officiel au siège du
       gouvernorat de Tunis », jour du dépôt non compté — loi n° 93-64, article 2 ;
     - depuis le 14 avril 2020, « le lendemain de la publication dans l'édition électronique » du
       Journal Officiel et de son dépôt électronique, « contrairement aux dispositions de la loi
       n° 93-64 » — décret-loi n° 2020-1 (JORT n° 32 de 2020, p. 767). Règle tranchée par le
       propriétaire le 20 octobre 2026. La date de publication est celle du fascicule.
  3. **Si le texte ne dit rien et que le calcul n'est pas sûr**, donne la date de publication
     (« publié le … ») au lieu de laisser la disposition sans date ou d'en déduire une.
- **La date de publication au JORT se relève et s'écrit toujours** (numéro et date du fascicule), en
  plus de la date d'effet, y compris quand une clause énonce l'effet.
- **Jamais la date de signature.** La date de publication ne se donne qu'au cas 3, présentée comme telle (« publié le … »), jamais comme date d'effet.
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
  Le 14/09/2026, la PR #208 du dépôt corrigeait précisément la propagation de ce drapeau aux commits
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

### Rendre à l'ouvrage

Les tableaux de paramètres de l'ouvrage doivent venir des dépôts de modèle **par un générateur**
(`scripts/generate_*_tables.py`), jamais être recopiés à la main. Un tableau fait main est toléré
en attendant que les paramètres soient datés et sourcés en amont, et porte alors un
`<!-- TODO (rédacteur) : remplacer par un tableau engendré -->`. On ne régénère jamais un tableau
qui dépend d'une PR openfisca non fusionnée : la CI régénère depuis `master`.

**Déplacer un paramètre casse l'ouvrage, qui le lit par son chemin.** Un renommage ou un passage de
feuille à nœud rend le générateur muet — « paramètre introuvable ou vide » — et le contrôle
hebdomadaire de fraîcheur échoue sans qu'aucun commit du dépôt soit en cause. L'ordre n'est donc
jamais indifférent :

1. la PR du modèle annonce la dépendance dans son corps, et un ticket la consigne dans le dépôt de l'ouvrage ;
2. la version est **publiée** ;
3. la borne de version du paquet est relevée dans `scripts/openfisca_tables.py`, avec son motif ;
4. les chemins sont corrigés, les snapshots régénérés, et l'on vérifie qu'ils sortent **identiques** —
   seul le chemin a changé, pas la valeur.

Corriger l'ouvrage avant la publication casse ses tableaux ; corriger après la publication, mais
trop tard, casse sa CI. Le 14 septembre 2026, deux paramètres déplacés le même jour ont produit les
deux cas.
