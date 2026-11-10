# Routage des reports et lacunes — où verser quoi

Doc canonique, lu par **tous les rôles** (une ligne de consigne commune renvoie ici depuis chaque
agent engendré, et l'`AGENTS.md` y renvoie aussi). Il répond à une seule question : *quand je
rencontre un report — ce qui n'a pas pu être fait, une donnée manquante, une piste non suivie — où
est-ce que je l'écris, pour qu'il ne se perde pas ?*

## L'invariant

**Aucun report ne vit uniquement dans la conversation ou dans une liste de session** : l'une et
l'autre disparaissent. À chaque **point d'arrêt** (fin d'un livrable, pivot, fermeture de session),
tout report est versé à une **destination durable** ci-dessous. Le backlog est **différencié** (une
destination par nature de report), pas consolidé en un seul fichier : chaque item vit près de son
propriétaire et de son contrôle CI, et les chantiers parallèles ne se marchent pas dessus.

## La carte

| Nature du report | Destination durable | Contrôle CI | Propriétaire |
|---|---|---|---|
| Lacune ou point **d'un chapitre du précis** (texte à écrire, valeur à sourcer, OCR à demander) | `docs/notes/backlog-precis.md` | `scripts/check_backlog.py` | `archiviste-backlog` |
| **État manquant / correctif du modèle** openfisca-tunisia (paramètre, date, formule, test) | `docs/notes/backlog-modele.md` | — | `modeliste` |
| **Recherche infructueuse** d'un texte attendu au JORT (décret, arrêté introuvable) | `docs/recherches.yml` **+** ancre `<!-- RECHERCHE r-… : … -->` dans le `.qmd` | `scripts/recherches.py` | `documentaliste` / `redacteur` |
| **Bibliographie** à créer, fusionner ou rapatrier dans Zotero | `docs/notes/biblio-a-rapatrier.md` | — | `bibliographe` |
| **Donnée, série ou OCR de l'entrepôt** `tunisia-data` (extraction à refaire, série à cataloguer) | notes du dépôt **`tunisia-data`** (privé) + section « Backlog » de **sa** PR | — | agent data |
| **Report propre à un chantier en cours** (pas encore mûr pour une destination durable) | note de chantier `docs/notes/<chantier>.md` | — | l'agent du chantier |

## Règles qui conditionnent le routage

- **Chantiers parallèles → ne pas écrire dans `backlog-precis.md`.** Quand plusieurs chantiers
  tournent, propose tes lignes de backlog (points fermés, lacunes nouvelles, état « lisible / OCR /
  à obtenir ») sous un titre **« Backlog »** dans le corps de ta PR. L'`archiviste-backlog` les
  applique en une passe, après les fusions, en vérifiant chaque point. Cela vaut aussi, par
  analogie, pour `backlog-modele.md` et les notes partagées.
- **Une fiche `recherches.yml` suppose son ancre.** Elle n'a de sens que si le texte rendu porte le
  constat et l'ancre `<!-- RECHERCHE r-… -->` qui la vise (contrôle `recherches.py`). Pas d'ancre
  dans le texte → la fiche est **orpheline** : garde le report en note de chantier jusqu'à ce que le
  texte porte le constat.
- **Rien de l'infrastructure de sauvegarde ni des données brutes dans le dépôt public.** Les reports
  qui touchent l'entrepôt, le corpus ou la sauvegarde vont dans `tunisia-data` (privé), jamais ici.
- **Dates du jour, lues avec `date`** ; jamais de date future (sauf `<!-- futur-ok -->` pour une
  entrée en vigueur annoncée). `check_backlog.py` refuse dates futures proches, marqueurs de conflit
  et clés de citation absentes des `references.json`.
- **Signale, ne tranche pas**, ce qui relève de la revue humaine (forme d'un chapitre, classement
  d'une réforme) : compte rendu, pas décision.

## Pour un sous-agent délégué

Quand tu délègues une tâche, demande au sous-agent de **signaler ses reports dans son compte rendu**
(ce qui n'a pu être fait, données manquantes, pistes non suivies). Le parent les **route** ensuite
selon cette carte et **vérifie** le travail (fichiers produits, chiffres) avant de le reprendre à
son compte.
