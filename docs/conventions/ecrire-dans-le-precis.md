# Écrire dans le précis : les règles qu'on oublie le plus

<!-- Détail déplacé d'AGENTS.md le 17/11/2026 (source unique) ; AGENTS.md y renvoie en une ligne. -->

`docs/conventions-redaction.md` fait foi ; ce mémento en rappelle les règles les plus souvent oubliées.


- **Le découpage des livres** (six parties, domicile d'un dispositif entre livres, types de
  chapitres, critère de scission, antécédent et contexte, section « Ce qu'en dit l'économie ») est
  énoncé dans `docs/conventions-redaction.md`, § 4 ; le chantier, dans
  `docs/notes/chantier-decoupage-livres.md`.

- **Tiens `docs/notes/backlog-precis.md` à jour quand tu modifies un chapitre.** Dans le même
  changement, retire les tâches closes, inscris les lacunes nouvelles et indique si le texte
  est lisible dans le corpus, demande un OCR, ou reste à obtenir. Vérifie avant de reprendre
  les chiffres et localisations d'un inventaire daté : `docs/notes/todo-localisation.md` est
  une photographie du 20 septembre 2026, pas un état du corpus en temps réel. La revue
  humaine contrôle que le backlog et le chapitre racontent le même état.
  **Quand plusieurs chantiers tournent en parallèle**, n'écris pas dans le fichier : propose
  tes lignes de backlog (points fermés, lacunes nouvelles, état « lisible / OCR / à obtenir »)
  dans le corps de ta PR, sous un titre « Backlog ». Le rôle `archiviste-backlog` les applique
  en une passe, après les fusions, et vérifie chaque point dans les chapitres : cela évite les
  conflits sur ce fichier et les « restes » qui survivent à leur chantier. Les dates que tu
  écris sont celles du jour (`date`), jamais une date future ; `scripts/check_backlog.py`
  refuse les marqueurs de conflit, les dates futures proches et les clés de citation absentes
  des `references.json`.
- **Où verser quel report : `docs/backlog-routage.md`.** Le backlog est **différencié** — une
  destination par nature de report (chapitre du précis → `backlog-precis.md` ; modèle openfisca →
  `backlog-modele.md` ; recherche JORT infructueuse → `docs/recherches.yml` + ancre `RECHERCHE` ;
  bibliographie → `biblio-a-rapatrier.md` ; donnée/série/OCR de l'entrepôt → notes de
  `tunisia-data`). La carte complète, les contrôles CI et la règle des chantiers parallèles sont
  dans `docs/backlog-routage.md`, auquel chaque rôle engendré renvoie. Invariant : **aucun report
  ne vit uniquement dans la conversation ou une liste de session**.
- **Une clé de références dit la même chose dans tous les livres.** Quand tu ajoutes ou corriges
  une notice dans le `references.json` d'un livre, cherche la même clé dans les autres
  (`grep -l '"id": "<clé>"' precis/*/references.json precis/*/*/references.json`) et aligne
  type, titre, recueil, volume, numéro, pages, date et adresse. Une pagination dépend de
  l'édition (française ou arabe) : si tu cites l'édition arabe, crée une clé distincte
  (`<clé>-ar`) au lieu de modifier celle de l'édition française.
  `scripts/check_references_coherentes.py` refuse deux définitions divergentes ; un cas non
  résolu se déclare, daté et motivé, dans `scripts/references_tolerances.yml`.

- **Les volumes documentent la loi, jamais le modèle.** Ni `openfisca`, ni « le modèle », ni « les
  paramètres » dans le texte rendu d'un volume. La documentation générale — README, page
  « À propos » — peut, elle, dire d'où viennent les tableaux et nommer `openfisca-tunisia`. Un constat sur le modèle va dans un `<!-- TODO (rôle) : … -->`,
  dans une *issue*, ou dans `docs/notes/backlog-modele.md`. `scripts/check_pas_de_modele.py` le
  vérifie.
  Seule exception : l'onglet « Base législative » des tableaux engendrés, qui lie chaque
  grandeur à sa page sur `parameters.tn.tax-benefit.org`. Ses liens sont engendrés avec le
  tableau (`tables/<nom>.liens.yml`), jamais écrits à la main.
- **Pas de jargon de dépouillement dans le texte visible** : ni « objet seul », ni « non lu », ni
  « métadonnées seules », ni `[T]`/`[M]`/`[D]`. Ce qui n'est pas lu ou pas établi ne s'écrit pas
  dans le texte rendu : on lit le texte, ou on laisse un commentaire `<!-- TODO (rôle) : … -->`.
- **Une recherche infructueuse ne se raconte pas** : ni « n'a pas été retrouvé », ni « au
  *Journal officiel* jusqu'au numéro du… ». Le texte dit le constat (« ce décret n'est pas
  identifié ici ») et porte une ancre `<!-- RECHERCHE r-… : … -->` vers une fiche rejouable de
  `docs/recherches.yml` — requêtes, sources, couverture datée, résultat. `scripts/recherches.py`
  la vérifie (CI), la relance et l'élargit.
- **Le budgétaire ne se mêle pas aux rapports extérieurs (FMI, Banque mondiale, OCDE) ni aux
  évaluations économiques** : pas
  dans le même tableau, pas sur le même plan, et jamais une étude sans sa méthode (qui, quelles
  données, quel périmètre, quel calcul). Le budgétaire d'abord, en entonnoir ; les études ensuite,
  titrées comme telles. Les superposer **sur un graphique** est permis quand elles sont censées
  traiter des mêmes dispositifs, familles distinguées et ruptures expliquées.
- **Tout PIB dit sa base, et s'il est rétropolé** ; si la source ne le dit pas, on l'écrit. Jamais
  deux bases chaînées en silence : la série se trace par segments, le changement de base est une
  rupture, et la rupture renvoie à l'annexe du site sur le PIB (`precis/fr/annexe-pib.qmd`).
  La règle vaut pour un PIB que le précis **emploie lui-même** — série, ratio calculé, figure. Un
  ratio au PIB simplement **cité** d'une étude ou d'un rapport, entre guillemets et avec sa
  référence, se donne tel quel : on n'écrit pas que la source n'en précise ni la base ni le calcul.
- **Les études citées sont récupérées** : le PDF de toute étude citée est rangé dans
  `tunisia-data` (`data/raw/`, hors git, catalogué dans `sources/`). On ne cite pas de seconde
  main ce qu'on peut obtenir.
- **Les ruptures au premier plan, le détail replié.** Un chapitre se lit dans cet ordre : vue
  d'ensemble ; mise en place ; grandes réformes, dans l'ordre des dates, avec ce que la loi
  cherche dans ses propres mots (rubriques des lois) ; bilan et état du droit ; une section par
  disposition secondaire ; longue période économique. Dans chaque section : l'essentiel en une
  phrase, la vue d'ensemble (figure ou tableau court), deux à quatre points, puis le détail dans
  un bloc `.chronologie-repliable` — le long tableau des textes, entier, avec sa colonne
  « Portée » (rupture, étape, ajustement). `docs/agents/architecte.md` donne le plan,
  `docs/agents/redacteur.md` l'écriture, `docs/notes/chantier-ruptures-au-premier-plan.md` le
  mode d'emploi de la conversion d'un chapitre.
- **Le texte principal se suffit.** On écrit comme si le lecteur ne lisait que lui, et pas dans
  l'ordre : une section dit son objet avant son évolution ; une notation se redéfinit là où elle
  sert ; rien ne dépend d'un bloc replié ; un renvoi vers une autre section se place en tête ;
  pas de métaphore pour nommer une chose du droit. On annonce ce que l'on présente, jamais ce que
  l'on laisse de côté ; l'état du droit se dit par sa date, pas par la façon dont il a été établi ;
  et l'on décrit ce qui est — le sujet de la phrase est l'État, le programme, le bénéficiaire —
  plutôt que ce que font les textes.
- **Les références de loi sortent du fil de la phrase.** Dans une section `.domicile-unique`, le
  nom du texte ou la date est un lien `[…](#r-…)` vers sa ligne de registre, qui porte la
  référence complète (texte, article, page) et alimente l'infobulle ; les autres sources
  (budget, rapports, études, recueils) restent citées sur place. Un seul modèle de renvoi pour
  les lois, le glossaire et les sections : signal sur le mot, infobulle où l'on peut cliquer,
  retour d'un geste. `scripts/check_domicile_references.py` le vérifie.
- **Un paramètre de la législation se retrouve toujours.** Replié ne veut pas dire caché : le
  bloc porte un titre qui dit ce qu'il contient, « Tout déplier » l'ouvre, la recherche l'ouvre.
- **Aucun chiffre ponctuel isolé** : toute valeur vient avec sa vue d'évolution datée. Et dans un
  tableau de textes, la colonne de contenu donne le changement concret — article, avant → après —,
  sinon la ligne n'a rien à y faire.

Les rôles éditoriaux — documentaliste, architecte, rédacteur, terminologue, bibliographe,
relecteur-ar, modeliste, économiste, archiviste-backlog — sont décrits dans `docs/agents/<role>.md`, en texte neutre, indépendant de l'outil et
du fournisseur de LLM. La chaîne éditoriale va du premier au dernier, et s'arrête pour revue
humaine. Voir `docs/conventions/economiser.md` pour le lien vers `.claude/agents/`.
