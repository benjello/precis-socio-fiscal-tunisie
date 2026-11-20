# Économiser

<!-- Détail déplacé d'AGENTS.md le 17/11/2026 (source unique) ; AGENTS.md y renvoie en une ligne. -->

**Économie de tokens et de temps (consigne du propriétaire, 17 novembre 2026).**
- Un seul fil de travail par défaut ; pas de sous-agents en parallèle sans demande explicite.
- Les outils existants avant toute relecture à la main : `verifier.sh`, générateurs
  `scripts/generate_*`, `figtools`/figdata, index et OCR du corpus JORT
  (`PDFs-legislation-tunisie/scripts/`), serveur MCP `jort`. Un script dès qu'une opération se
  répète.
- Titres et sommaires avant toute OCR ; OCR des seules pages utiles.
- Pendant le travail, ne rendre que le chapitre modifié (`quarto render <fichier>.qmd`) ; le
  volume une seule fois, avant la PR. Pas de nouveau `verifier.sh` après une fusion de master,
  sauf conflit.
- Petits lots ; rapports de cinq lignes au plus.


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
  vérifié.
- **Mobilise le bon RÔLE, pas un agent générique.** Dès qu'une tâche relève d'un rôle, c'est ce
  rôle qu'on lance, pas un sous-agent « généraliste » : rassembler de la matière sourcée →
  `documentaliste` ; corriger `openfisca-tunisia` (paramètres, formules, parseur de données,
  tests) → `modeliste` ; état des connaissances économiques d'un dispositif → `economiste` ;
  bibliographie → `bibliographe` ; glossaire → `terminologue` ; plan de chapitre → `architecte` ;
  rédaction `.qmd` → `redacteur` ; tenue du backlog → `archiviste-backlog`. Un sous-agent
  généraliste lancé là où un rôle existe perd la consigne du rôle (garde-fous, place dans la
  chaîne éditoriale, livrable attendu) — défaut à éviter.
- **Le dossier d'agents engendré dépend du harnais.** `.claude/agents/<role>.md` n'est lu QUE par
  Claude Code ; `pi` lit `.pi/agents/<role>.md` (puis `.agents/agents/`, puis le global) ;
  `opencode` (V1, binaire 1.x) lit `.opencode/agent/<role>.md`.
  `scripts/sync_agents.py` engendre désormais **les trois** (`engendrer_claude_code()`,
  `engendrer_pi()`, `engendrer_opencode()`), et `--verifier` contrôle les trois — édite
  `docs/agents/<role>.md` ou `roles.yml` puis régénère, ne touche jamais les fichiers engendrés à
  la main. Sous pi comme sous opencode, les rôles sont donc **invocables par leur nom**
  (`subagent_type: documentaliste`) — au prochain démarrage de session (les agents sont chargés au
  lancement). **Vocabulaire d'outils neutre** : `roles.yml` écrit des noms d'outils neutres
  (`read, write, edit, grep, glob, bash, web_search, web_fetch`) que `sync_agents.py` TRADUIT par
  harnais (`glob`→`Glob` sous Claude mais `find` sous pi/opencode ; `web_search`→`WebSearch` sous
  Claude, `web_search` sous pi/opencode). C'est le correctif de la réserve « outils web » : les
  rôles documentaliste/économiste/bibliographe démarrent désormais **avec** le web sous pi et
  opencode (auparavant les noms Claude `WebSearch`/`WebFetch`, inconnus de pi, étaient ignorés et
  ces rôles n'avaient pas de web). Reste une réserve, **le modèle par niveau** : `modeles.pi` et
  `modeles.opencode` de `roles.yml` sont à null tant que l'humain n'a pas confirmé les modèles de
  son abonnement ; tant que c'est null, `sync_agents.py` omet la ligne `model:` et l'agent hérite
  du modèle de la session parente (sûr mais sans tiering). Les agents écrits à la main qui
  fonctionnent (`~/.pi/agent/agents/`, `~/.config/opencode/agent/`) emploient `claude-sonnet-4-5`
  et `claude-haiku-4-5` : reprendre ces identifiants vérifiés dans `modeles.pi`/`modeles.opencode`
  pour activer le choix par niveau. Si un rôle ne s'invoque pas (harnais tiers sans générateur),
  procédé manuel : `Read docs/agents/<role>.md` comme consigne du sous-agent + modèle par niveau
  depuis `modeles.<outil>`.
- **Ne te rabats sur un agent généraliste que si le rôle requis n'existe pas.**
- **Tâches mécaniques sur modèle léger, même déléguées.** Régénérer un CSV de provenance, déplacer
  et indexer un PDF dans le corpus, lancer un OCR, un rendu, un snapshot : modèle `mécanique` et
  vérification par contrôle (exit code, diff, intégrité), jamais par jugement — garde le modèle
  principal pour la lecture d'un texte de loi et la rédaction.
- **Indexe tout document téléchargé dans `tunisia-data`.** Tout PDF récupéré va dans le corpus
  (`tunisia-data/data/raw/…`), avec un nommage cohérent, ET s'inscrit dans le catalogue
  `tunisia-data/sources/` (fiche `<famille>.md` + `<famille>-urls.csv`) — jamais laissé en `/tmp`
  ni cité depuis `/tmp`. Avant toute chasse web, lire d'abord `sources/` : il est déjà très fourni
  (EP, Cour des comptes, BVMT, rapports MdF). Un sous-agent de recherche ne télécharge pas dans le
  dépôt ; ce qu'il rapporte d'utile est re-téléchargé et indexé proprement ensuite.
