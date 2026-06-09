---
description: Orchestre la rédaction d'une section du précis à partir d'un ticket GitHub (documentaliste → rédacteur FR → terminologue → bibliographe → gates), puis s'arrête pour revue humaine.
argument-hint: [issue-number]
allowed-tools: Bash(gh issue view *), Bash(uv run *), Bash(git status *), Bash(git diff *), Bash(git add *), Bash(git log *), Read, Grep, Glob, Agent
---

## Ticket à traiter
!`gh issue view $1 --json number,title,body,labels,milestone -q '"#\(.number) — \(.title)\n\nLabels: \([.labels[].name]|join(", "))\nMilestone: \(.milestone.title // "—")\n\n\(.body)"' 2>/dev/null || echo "Ticket #$1 introuvable — précise un numéro d'issue valide."`

## Mission

Tu orchestres la rédaction de la section décrite par le ticket #$1 ci-dessus, de façon **incrémentale** et **vérifiable**. Le français est la source de vérité ; l'arabe et sa vérification sont produits ensuite par le CI (workflows `translation-sync` puis `verify-translation`) — **ne rédige pas l'arabe à la main**.

Déroule la chaîne suivante, en t'arrêtant si une étape échoue :

1. **Documentaliste** — délègue au sous-agent `documentaliste` (via l'outil Agent) la collecte de la matière sourcée pour cette section. Transmets-lui le contenu du ticket et le chemin du chapitre concerné. Récupère sa note documentaire.

2. **Rédacteur** — délègue au sous-agent `redacteur` la rédaction/complétion du `.qmd` **français** correspondant, en lui passant la note documentaire. Il ne touche qu'à `precis/fr/`.

3. **Terminologue** — délègue au sous-agent `terminologue` la mise à jour de `precis/glossaire.yml` pour les notions de la section, puis la régénération du glossaire.

4. **Bibliographe** — délègue au sous-agent `bibliographe` l'intégration et la vérification des références citées : compléter/corriger les entrées CSL-JSON, contrôler la résolution des `[@clés]`, et alimenter l'inbox de rapatriement Zotero (`docs/notes/biblio-a-rapatrier.md`). Il ne pousse rien dans Zotero sans feu vert humain.

5. **Gates** (exécute-les toi-même, ne les délègue pas) :
   - `uv run python scripts/build_glossary.py` → doit retourner exit 0 (verrou de synchro).
   - `cd precis/fr/<book> && uv run quarto render --to html` → rendu sans erreur, aucune citation `[?]` non résolue.
   Si un gate échoue, renvoie le problème au sous-agent concerné et recommence l'étape.

6. **Synthèse pour revue humaine** — affiche `git status` et un résumé : fichiers modifiés, sources ajoutées, notions de glossaire, TODO restants (références manquantes pour le bibliographe). **Ne committe pas, ne pousse pas, n'ouvre pas de PR** : laisse l'humain valider l'exactitude juridique avant toute action sortante.

## Rappels
- Toujours `uv run` pour Python (jamais `python3` / `.venv` directement).
- Si le ticket est mal cadré ou ambigu, signale-le et demande une précision avant de lancer la chaîne.
