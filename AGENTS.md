# Consignes pour les agents

Ce fichier s'adresse à tout agent — quel que soit l'outil — qui travaille sur le « Précis des
politiques publiques de la Tunisie », ou sur les dépôts de modèle qui l'alimentent. Il est
versionné : c'est ici que les conventions vivent, pas dans la mémoire d'un assistant.

## Le dépôt en deux phrases

Neuf volumes bilingues — des livres Quarto, `precis/fr/<livre>/` et `precis/ar/<livre>/` — :
fiscalité, cotisations sociales, prestations sociales, retraites, caisses de sécurité sociale,
rémunérations publiques, finances locales, marché du travail, compensation ; quatre volumes
supplémentaires, les entreprises publiques, la santé, l'éducation et l'informel, en français seulement tant que leurs
traductions ne sont pas livrées ; un glossaire bilingue
engendré depuis `precis/glossaire.yml`, une bibliographie CSL-JSON, et des tableaux de paramètres
engendrés depuis le dépôt `openfisca-tunisia`, qui porte aussi les retraites depuis sa version 0.93.

Le travail documentaire s'appuie sur le *Journal officiel* : métadonnées dans
`~/projets/PDFs-legislation-tunisie/jort_cache.db`, fascicules dans le corpus local du même dépôt,
et sur `pist.tn` en ligne. Voir `docs/notes/outillage-sources.md`.

## Invariants, quel que soit le rôle

- **Toujours `uv run`** pour Python — jamais `python3` ni `.venv/bin/python3`.
- **Le français est la source de vérité.** N'écris jamais un `.qmd` sous `precis/ar/` : la version
  arabe est produite par la CI (traduction, et pages-relais engendrées par `scripts/arabe_cablage.py`). Les `references.json`, eux, se tiennent à la main dans les deux
  langues ; les **`_quarto.yml` arabes** aussi, sauf leurs listes de chapitres (engendrées).
- **Traduction arabe** (exclusion des `_quarto.yml`, `scripts/arabe_cablage.py` après tout ajout ou renommage de chapitre, pipeline Gemini, auto-fusion) : `docs/conventions/traduction-arabe.md`.
- **Ne modifie pas les fichiers engendrés** : `_glossaire.qmd`, `_glossaire.infobulles.html`, `translation_glossary.generated.md`,
  `precis/*/*/tables/*`.
- **Ce dépôt est public (GitHub Pages) : rien sur l'infrastructure de sauvegarde.** Les notes et
  procédures de la sauvegarde du corpus vivent dans le dépôt privé `tunisia-data`, dont l'`AGENTS.md`
  fait foi. `scripts/check_pas_d_infra.py` contrôle les fichiers suivis ; la liste des mots qu'il
  cherche est hors dépôt (fichier de configuration local, décrit dans le script, ou secret de CI
  `PAS_D_INFRA_MOTS`) : ne la recopie nulle part ici.
- **Sources** (aucune valeur, date ni URL sans source vérifiée ; textes juridiques et base législative ; séries à fenêtre de trente ans) : `docs/conventions/sources-et-datation.md`.
- **Ne committe pas** sans que l'humain ait relu, sauf consigne explicite. N'ouvre ni PR ni issue de
  ta propre initiative.
- **OCR** : lance les océrisations au premier plan ou attends-les, et ne laisse aucun processus
  tourner en fin de tâche. **N'emploie jamais `pkill` sans cibler tes propres processus** : d'autres
  agents travaillent en parallèle dans le même répertoire de session.

## Écrire dans le précis

`docs/conventions-redaction.md` fait foi ; mémento des règles les plus oubliées : `docs/conventions/ecrire-dans-le-precis.md`.

## Dépôts de modèle (rôle « modéliste »)

Dater, découper, tester, publier, rendre au précis : `docs/conventions/modele.md`.

## Économiser

**Économie de tokens et de temps** (consigne du propriétaire, 17/11/2026) : un seul fil de travail ; pas de sous-agents en parallèle sans demande explicite ; outils et scripts existants avant toute relecture à la main, un script dès qu'une opération se répète ; titres et sommaires avant toute OCR ; ne rendre que le chapitre modifié pendant le travail (`scripts/verifier.sh` le fait par défaut), le volume une fois avant la PR ; pas de nouveau `verifier.sh` après une fusion de master sans conflit ; petits lots, rapports de cinq lignes au plus.

Un seul appel (`scripts/verifier.sh`), le modèle suit la tâche, rôles éditoriaux et sous-agents engendrés, indexation des documents : `docs/conventions/economiser.md`.

## Rendre compte et vérifier

Heures plutôt que durées, rendu ouvert dans le navigateur, contrôles avant de rendre la main, gabarit du rapport final d'un sous-agent : `docs/conventions/rendre-compte.md`.
