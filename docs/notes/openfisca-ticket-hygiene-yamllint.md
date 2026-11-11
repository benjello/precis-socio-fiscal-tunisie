# Ticket (brouillon, à ouvrir sur accord) — hygiène : `make check-all-yaml` rouge sur quatre fichiers

## Titre
`make check-all-yaml` échoue sur quatre fichiers de paramètres (une erreur, trois avertissements)

## Corps
La cible `make check-all-yaml` (`yamllint openfisca_tunisia/parameters` puis `yamllint tests`) est
rouge sur `master`, indépendamment de toute PR en cours. En cause, quatre fichiers **déjà présents
sur `master`** (vérifié : chacun est tracé par `origin/master`) :

| Fichier | Ligne | Règle | Niveau |
|---|---|---|---|
| `parameters/marche_travail/temps_travail/travail_domestique/index.yaml` | 15:1 | `trailing-spaces` | **error** |
| `parameters/retraite/rsna/salaire_reference/duree_mois.yaml` | 37:1 | `empty-lines` (too many blank lines) | warning |
| `parameters/impot_revenu/tspr/smig_ext.yaml` | 22:1 | `empty-lines` (too many blank lines) | warning |
| `parameters/prestations/non_contributives/pnafn/index.yaml` | 1:14 | `colons` (too many spaces after colon) | warning |

La CI ne l'attrape pas : le job `lint-files` ne lint que les fichiers modifiés par la PR, pas
l'arbre entier. Le défaut reste donc invisible en CI mais fait échouer la cible locale, que la
procédure de contribution demande de lancer avant de pousser.

## Correctif proposé
- Retirer l'espace de fin ligne 15 de `travail_domestique/index.yaml` (erreur bloquante).
- Retirer la ligne vide excédentaire en fin de `duree_mois.yaml` et de `smig_ext.yaml`.
- Réduire l'espacement après le `:` de la première ligne de `pnafn/index.yaml`.

Changements purement cosmétiques, sans effet sur les valeurs ni sur les calculs : un seul commit
« Technical improvement », sans bump de version fonctionnel.

## Note
Découvert en lançant `make check-all-yaml` lors de la préparation des PR #523/#524/#525 (dont les
fichiers, eux, passent yamllint).
