# Rendre compte et vérifier

<!-- Détail déplacé d'AGENTS.md le 17/11/2026 (source unique) ; AGENTS.md y renvoie en une ligne. -->

## Rendre compte à l'humain

- **Annonce des heures, pas des durées.** Dès qu'une étape doit prendre plus de trois minutes —
  un rendu, une vérification, une CI, un sous-agent, une suite d'étapes —, donne son **heure de fin
  estimée**, à l'horloge (« fin vers 10 h 40 »), et non une durée (« une dizaine de minutes »).
  Pour une suite d'étapes, donne un tableau : étape, heure de début, heure de fin, état. Lis
  l'heure avec `date` avant de l'écrire ; ne la calcule pas de tête. Quand une étape déborde,
  redonne l'heure révisée sans attendre qu'on la demande, et dis ce qui a pris plus longtemps.
- **Ouvre dans le navigateur ce qui est à relire.** Un rendu prêt pour la relecture — chapitre,
  figure, prototype, aperçu d'une PR — s'ouvre dans le navigateur, sur l'ancre de la section
  concernée, à chaque nouvelle version ; un chemin de fichier ne suffit pas. Copie d'abord le rendu
  sous le répertoire personnel si le navigateur ne lit que lui, et dis dans le message quels
  onglets ont été ouverts.

## Rapport final d'un sous-agent

Le contenu est celui du « Livrable » de chaque rôle ; la forme est la même pour tout agent — au plus quinze lignes :

- **Fait** : les fichiers touchés (chemins) et le hash du commit, s'il y en a un.
- **Contrôles** : une ligne — la commande lancée (`scripts/verifier.sh <livre>` de préférence à
  une chaîne de contrôles séparés) et son résultat, pas son journal détaillé.
- **Points à trancher** : ce qui attend un arbitrage humain, s'il y en a.

Rien d'autre : ni récit du cheminement, ni code cité en entier — les chemins et le hash suffisent
à le retrouver.

## Vérifier avant de rendre la main

```
scripts/verifier.sh [livre…]                                # glossaire, contrôles, liens, tests, rendu
uv run python scripts/build_glossary.py                    # verrou de synchro du glossaire
cd precis/fr/<livre> && uv run quarto render --to html     # zéro citation [?] non résolue
uv run python scripts/check_pas_de_modele.py               # le précis ne parle pas du modèle
./build.sh                                                  # les volumes disponibles, FR et AR
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
