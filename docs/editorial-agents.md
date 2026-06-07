# Activité éditoriale orchestrée par agents

Organisation incrémentale de la rédaction du précis autour de sous-agents Claude Code,
articulés avec l'automatisation CI existante.

## Colonne vertébrale (CI déjà en place)

Le français est la **source de vérité** ; l'arabe et sa vérification sont automatisés :

```
rédaction FR (agents Claude) → PR
   → translation-sync.yml   : traduit FR→AR et committe l'AR sur la branche
   → verify-translation.yml : Checker AI commente la PR (échoue si anomalie)
   → revue humaine → merge
   → deploy.yml             : build.sh (régénère le glossaire) + déploiement Pages
```

Les agents Claude ne rédigent donc **jamais** l'arabe : ils produisent un FR de qualité,
le glossaire et la bibliographie, puis laissent le CI faire l'AR.

## Phase 0 — implémentée

Unité de travail = **un ticket GitHub**. Chaîne FR :

- `.claude/agents/documentaliste.md` — rassemble la matière sourcée (lois, académique, presse).
- `.claude/agents/redacteur.md` — écrit le `.qmd` FR à partir de la note, avec citations.
- `.claude/agents/terminologue.md` — met à jour `precis/glossaire.yml`, régénère le glossaire.
- `.claude/commands/rediger.md` — commande `/rediger <issue#>` qui orchestre la chaîne
  depuis la session principale, exécute les **gates**, puis s'arrête pour revue humaine.

**Gates de qualité** (invariants du dépôt) : `uv run python scripts/build_glossary.py`
(verrou de synchro FR/AR, exit 0), rendu `uv run quarto render --to html` sans erreur ni
citation non résolue.

**Garde-fous** : revue humaine obligatoire avant merge (exactitude juridique) ; aucune
action sortante automatique (pas de push/PR par la commande).

Invariant transverse encodé dans chaque agent : toujours `uv run` (jamais `python3` / `.venv`).

## Parties différées (design, à confirmer)

- **Sous-agent `bibliographe`** — complète `references.json`, vérifie la résolution des
  `[@clés]`, prépare le rapatriement Zotero (issue #17). Une clé Zotero en écriture existe
  déjà côté projet.
- **Sous-agent `relecteur-FR`** — relecture adversariale de l'exactitude juridique/historique
  (la vérification AR est déjà couverte par `verify-translation`).
- **Workflow d'éventail (Phase 2)** — traitement parallèle de plusieurs chapitres
  (p. ex. B.1–B.4) une fois la chaîne Phase 0 éprouvée. Nécessite un feu vert explicite
  (coût en tokens).

## Trajectoire

1. Phase 0 (faite) → tester `/rediger 6` (A.2 périmètre) sur un cas réel.
2. Phase 1 → ajouter `bibliographe` + `relecteur-FR`.
3. Phase 2 → industrialiser via Workflow en éventail.
