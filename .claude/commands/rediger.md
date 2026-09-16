---
description: Orchestre la rédaction d'une section du précis à partir d'un ticket GitHub (documentaliste → bibliographe/versement → terminologue/termes → rédacteur → terminologue/définitions → bibliographe/clôture), avec un gate après chaque passe, puis s'arrête pour revue humaine.
argument-hint: [issue-number]
allowed-tools: Bash(gh issue view *), Bash(uv run *), Bash(git status *), Bash(git diff *), Bash(git add *), Bash(git log *), Read, Grep, Glob, Agent
---

## Ticket à traiter
!`gh issue view $1 --json number,title,body,labels,milestone -q '"#\(.number) — \(.title)\n\nLabels: \([.labels[].name]|join(", "))\nMilestone: \(.milestone.title // "—")\n\n\(.body)"' 2>/dev/null || echo "Ticket #$1 introuvable — précise un numéro d'issue valide."`

## Mission

Tu orchestres la rédaction de la section décrite par le ticket #$1 ci-dessus, de façon **incrémentale** et **vérifiable**. Le français est la source de vérité ; l'arabe est produit ensuite par le CI — **ne rédige pas l'arabe à la main**.

## L'ordre suit les dépendances de données, pas le confort du récit

On serait tenté d'enchaîner « documenter, écrire, nommer, sourcer ». Les données vont dans l'autre sens, et l'ordre naïf a coûté cher :

- une entrée de glossaire porte `source_definition: {ref: …}`, rendue en `[@clé]`. **`build_glossary.py` ne valide pas les refs** : une clé absente ne fait donc échouer aucun gate, elle produit une **citation morte dans la page publiée**. La bibliographie doit précéder le glossaire.
- `build_glossary.py` **échoue** si la prose ancre `#g-x` sans entrée (⇒ terminologue avant rédacteur), mais il ne **rend** que les notions qu'un livre ancre (⇒ terminologue après rédacteur). Aucun ordre simple ne résout ce cycle : **le terminologue passe deux fois**.

Déroule la chaîne suivante, en t'arrêtant si une étape ou son gate échoue.

### 1. Documentaliste
Délègue à `documentaliste` la collecte de la matière sourcée. Transmets le ticket et le chemin du chapitre. Récupère sa note documentaire, ses références candidates et ses notions à glossaire.

### 2. Bibliographe — versement
Délègue à `bibliographe` le **versement des clés CSL** issues de la note, dans `precis/fr/<book>/references.json` **et** son homologue arabe.

**Gate** : chaque clé que la section citera existe et résout. Sans cela, le glossaire et la prose citeront dans le vide.

### 3. Terminologue — passe 1, les termes
Délègue à `terminologue` la création des entrées **avec leurs `id`, leurs termes FR et AR, et leur `source_definition`** pointant les clés versées à l'étape 2. Les définitions peuvent attendre ; le statut reste `provisoire` tant que l'arabe n'est pas validé.

**Gate** : `uv run python scripts/build_glossary.py` → exit 0. Les ancres `#g-…` existent désormais, et le rédacteur peut les employer sans casser la génération.

### 4. Rédacteur
Délègue à `redacteur` la rédaction du `.qmd` **français**, en lui passant la note documentaire, **la liste des ancres disponibles** et **la liste des clés qui résolvent**. Il n'invente ni l'une ni l'autre. Il ne touche qu'à `precis/fr/`.

**Gate** : `cd precis/fr/<book> && uv run quarto render --to html` → sans erreur, **zéro `[?]`**.

### 5. Terminologue — passe 2, les définitions
Délègue à `terminologue` les **définitions FR et AR**, les sources, et le passage en `statut: valide` de ce qui peut l'être. Les notions sont maintenant **ancrées par la prose**, donc réellement rendues : c'est ici qu'elles cessent d'être dormantes.

**Gate** : `uv run python scripts/build_glossary.py` → exit 0, et le compte de notions retenues par le livre a augmenté.

### 6. Bibliographe — clôture
Délègue à `bibliographe` le contrôle de résolution **et l'exécution d'un `dry-run` Zotero** (action `dry-run` du workflow `biblio-zotero`, en lecture seule).

**Ce `dry-run` n'est pas optionnel.** Le 15/09/2026, un champ `number-of-pages` sur **une** entrée bloquait la conversion des **333** références vers Zotero — donc tout rapatriement — et le défaut a dormi des mois parce que rien, dans cette chaîne, ne lançait jamais cette action.

### 7. Synthèse pour revue humaine
Affiche `git status` et un résumé : fichiers modifiés, sources ajoutées, notions ancrées, lacunes laissées en clair, TODO restants. **Ne committe pas, ne pousse pas, n'ouvre pas de PR** : laisse l'humain valider l'exactitude juridique.

## Après la fusion, l'arabe n'est pas fini

La fusion déclenche `translation-sync`, qui livre les `.qmd` arabes — mais **pas** leur déclaration dans `precis/ar/<book>/_quarto.yml`, exclu de la traduction. Un chapitre non déclaré rend **404** sans que rien ne le signale. C'est le rôle de `relecteur-ar`, à lancer sur la PR de traduction.

## Rappels
- Toujours `uv run` pour Python (jamais `python3` / `.venv` directement).
- **Ne lis jamais la conclusion d'un job de traduction : lis ses étapes, et désigne-les par leur NOM.** Le Checker AI — étape « Run verification script » — échoue dès que sa réponse n'est pas exactement « OK », alors que les gardes déterministes, « Check FR/AR parity » et « Render the touched Arabic books », sont vertes. Ne compte pas les étapes : leurs numéros suivent le workflow, et cette consigne a elle-même dit « deux étapes plus haut » jusqu'au 16/09/2026, jour où la garde se trouvait à l'étape 4.
- Si le ticket est mal cadré ou ambigu, signale-le et demande une précision avant de lancer la chaîne.
