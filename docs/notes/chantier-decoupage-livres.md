# Chantier — le découpage des livres (doctrine C)

Décidé le 17 octobre 2026 : le propriétaire retient la doctrine C de la réflexion du même jour.
Hors de la protection sociale, les livres restent tels quels. Dans la protection sociale, on
cesse de couper deux fois. Plan à lancer plus tard, phase par phase, une PR par phase.

## La doctrine, en une page

**Le site en cinq parties**, sur la page d'accueil :

| Partie | Livres |
|---|---|
| I. Les revenus du travail | Le marché du travail ; Les rémunérations publiques |
| II. Les prélèvements | La fiscalité ; Les finances locales ; Le financement et les caisses de la sécurité sociale |
| III. Les transferts | Les retraites ; Les prestations sociales ; La santé ; La compensation |
| IV. Les institutions | Les entreprises publiques |
| V. La synthèse | La redistribution (à écrire quand `ceq-tunisie` donnera des séries sourcées) |

Le livre « Le financement et les caisses » est rangé en II parce que son objet premier est ce
qui est prélevé ; il porte aussi les caisses comme institutions. Les finances locales restent
en II, avec leurs chapitres sur les collectivités.

**La règle de domicile au niveau du livre**, écrite une seule fois, sur la page d'accueil et
dans `docs/conventions-redaction.md` :

- ce qui est prélevé (taux, assiette, ventilation entre branches), l'organisme qui le gère et
  ses comptes → **Le financement et les caisses** ;
- ce qui est servi en espèces (pension, allocation, indemnité) → **Les retraites** ou
  **Les prestations sociales** ;
- ce qui est servi en nature (les soins) → **La santé** ;
- un prix ou un tarif administré → **La compensation** ;
- une règle de salaire → **Les revenus du travail** ;
- le statut et les comptes d'une entreprise publique → **Les entreprises publiques**.

L'autre livre reçoit une phrase et un lien en tête de section ; ou, quand la lecture ne peut
pas avancer sans, une figure ou un tableau court tiré des mêmes données, jamais la prose
recopiée.

**Les types de chapitres**, reconnaissables à leur titre : dispositif (plan type à épine
chronologique) ; institution (naissance, statut, ce qu'elle sert, comptes, longue période) ;
cadre (notions, un seul par livre, en tête) ; longue période du livre (budgétaire seul) ;
rapports et études (chacun avec sa méthode). Les notations, listes, textes modificatifs et
tableaux annexés sont des annexes déclarées comme telles dans `_quarto.yml`.

**La présentation d'un livre** : l'objet en une phrase ; la carte des dispositifs ou
institutions (texte fondateur, date d'application, où lire) ; une figure de ce que pèse
l'ensemble ; le plan ; les conventions de lecture ; un **tableau de voisinage** (sujet
limitrophe → livre où il vit), qui remplace les sections « ce que ce livre ne traite pas ».

**Le critère de scission d'un chapitre** : un chapitre suit une seule épine chronologique —
trois à six grandes réformes d'un même dispositif — et ses fiches. Au-delà d'environ
25 000 mots de fichier, ou quand un fichier porte plusieurs épines, il se scinde, avant toute
conversion au format « ruptures au premier plan ».

## Les phases

Chaque phase : une branche, un worktree, `scripts/verifier.sh` sur tous les livres touchés,
rendu FR et AR, aperçu ouvert dans Firefox, PR, fusion sur accord du propriétaire. Le niveau
de modèle est indiqué pour chaque étape (voir la dernière section).

### Phase 0 — Écrire la doctrine (une PR, petite)

1. Verser la doctrine ci-dessus dans `docs/conventions-redaction.md` (section nouvelle « Le
   découpage des livres ») et une ligne de renvoi dans `AGENTS.md`. — *raisonnement*
2. Mettre à jour `docs/agents/architecte.md` : le critère de scission, les types de chapitres,
   la règle de domicile entre livres. Régénérer `.claude/agents/` (`scripts/sync_agents.py`).
   — *standard*

### Phase 1 — Les parties sur la page d'accueil (une PR, petite)

1. `precis/fr/index.qmd` : les cartes des livres rangées en cinq parties, la règle de domicile
   en un paragraphe ; les entreprises publiques et la santé y entrent (elles sont aujourd'hui
   hors page d'accueil ou à part). — *standard*
2. L'arabe suit par la traduction ; ne pas écrire `precis/ar/index.qmd`. — *rien à faire*

### Phase 2 — La fusion « Le financement et les caisses de la sécurité sociale » (la plus lourde)

**À trancher avant de lancer** (recommandation entre parenthèses) :

- Le dossier : garder `precis/fr/cotisations_sociales/` et y verser les chapitres des caisses
  (recommandé : moins de liens, générateurs, `tables/` et collection Zotero à toucher), ou un
  dossier neuf `securite_sociale/`.
- L'arabe : déplacer les `.qmd` arabes par `git mv` dans le même commit que les français, sans
  en modifier le contenu (recommandé : évite une retraduction complète sous plafond Gemini),
  ou les laisser retraduire. Le `git mv` n'écrit aucun texte arabe, mais l'invariant « jamais
  de `.qmd` sous `precis/ar/` » doit être levé explicitement pour cette opération.

Étapes :

1. **Inventaire de départ** (copie hors dépôt) : identifiants `sec-`/`tbl-`/`fig-` des deux
   livres, collisions éventuelles, liens entrants (`../caisses/…` : environ 60 dans 20 fichiers
   français), clés de `references.json` des deux livres. — *standard*
2. **Déplacement** : les chapitres de `caisses/` dans le dossier retenu, avec un nouveau nom
   pour `caisses/index.qmd` (son contenu devient un chapitre « Les caisses » ou se fond dans la
   présentation commune) ; `figures/`, `figdata/`, `_fig/` réunis ; `references.json` fusionnés
   sans doublon, FR et AR ; `_quarto.yml` FR et AR réécrits à la main avec des parties
   (`part:`) : « Les caisses », « Les cotisations », « Les comptes ». — *standard*
3. **Scripts** : `build.sh` (`BOOKS`), `scripts/build_glossary.py`, `verifier_livres.py`,
   `translate_sync.py`, `sync_biblio.py` et `push_biblio.py` (collections Zotero « Cotisations
   sociales » et « Caisses de sécurité sociale » réunies), `generate_encadre_caisses.py` (le
   livre fusionné n'a plus besoin de l'encadré ; prestations et retraites le gardent),
   `generate_cotisations_tables.py`, `generate_retraites_tables.py`, les tests. — *standard*
4. **Liens** : réécrire par script les liens français `../caisses/<page>.html#…` vers leur
   nouvelle page ; les liens internes au nouveau livre deviennent des `@sec-`. — *standard*
5. **Redirections** : GitHub Pages ne fait pas de redirection serveur. `build.sh` écrit, après
   rendu, une page de redirection (`<meta http-equiv="refresh">` + lien) à chaque ancienne
   adresse `fr/caisses/*.html` et `ar/caisses/*.html`. Elle sert les liens des mails déjà
   envoyés (six brouillons de diffusion en contiennent) et les liens arabes non réécrits. —
   *standard*
6. **Le texte** (*raisonnement*) :
   - une présentation commune (carte, figure de ce que pèsent les cotisations et les comptes
     des caisses, tableau de voisinage) ;
   - un seul domicile pour la ventilation du taux global, aujourd'hui dans
     `cotisations_sociales/_taux_global.qmd` (« Du taux global aux taux par branche ») et dans
     `caisses/_comptes_regimes.qmd` (« L'équilibrage par la ventilation du taux global ») ;
   - les sections « ce que ce livre ne traite pas » remplacées par le tableau de voisinage.
7. **Vérification** : `verifier.sh` sur le livre fusionné, retraites, prestations, santé,
   rémunérations publiques, marché du travail, entreprises publiques, fiscalité (tous ont des
   liens entrants) ; rendu arabe du livre fusionné ; redirections testées dans Firefox. —
   *mécanique*

### Phase 3 — L'assurance maladie à un seul endroit par livre

1. `prestations_sociales/_autres_risques.qmd`, section `#sec-ar-assurance-maladie` (l. 511-583
   au 17 octobre 2026) : vérifier que chaque fait qu'elle porte (bénéficiaires, filières,
   cotisation, caisse) est dans `sante/_couverture.qmd` ou dans le livre fusionné ; verser
   ce qui manque ; réduire la section à un renvoi en tête et aux indemnités en espèces. —
   *raisonnement*
2. Même contrôle pour `cotisations_sociales/_maladie.qmd` contre `sante/_couverture.qmd` :
   la cotisation reste au livre fusionné, les soins à la santé. — *raisonnement*

### Phase 4 — Les retraites scindées avant leur conversion

1. `retraites/_secteur_prive.qmd` (36 850 mots) en quatre chapitres sous une partie « Le
   secteur privé » :
   - le régime des salariés non agricoles (`#sec-rsna`, environ 15 800 mots) ;
   - les régimes agricoles (`#sec-agricoles`) ;
   - le régime complémentaire (`#sec-regime-complementaire`) ;
   - les non-salariés et les régimes particuliers (`#sec-regimes-particuliers`).

   « Vue d'ensemble : les deux secteurs » (`#sec-vue-ensemble`) passe dans la présentation du
   livre ; les deux annexes (notations, textes modificatifs du décret n° 74-499) deviennent
   des annexes déclarées. — découpe *standard*, phrases de raccord *raisonnement*
2. `retraites/_secteur_public.qmd` (25 760 mots) : une seule épine (loi n° 85-12 et ses
   réformes) ; on ne scinde pas, mais les régimes spéciaux et les militaires peuvent devenir
   un chapitre à part si l'architecte le demande ; les deux annexes deviennent des annexes
   déclarées. — *standard*
3. Identifiants inchangés ; liens entrants (`../retraites/_secteur_prive.html#…`) réécrits par
   script ; pages de redirection pour l'ancienne adresse. Même question arabe qu'en phase 2.
   — *standard*

### Phase 5 — Les présentations des autres livres

Le tableau de voisinage à la place des sections « ce que ce livre ne traite pas » (cinq
présentations), et la carte là où elle manque. — *standard*, relu par le propriétaire.

### Plus tard

- Le livre de synthèse sur la redistribution (partie V), quand `ceq-tunisie` donnera des
  séries sourcées.
- Le titre du marché du travail : inchangé ; le droit du travail qui détermine les revenus y
  entrera (manque n° 3 du backlog).

## L'ordre avec le chantier « ruptures au premier plan »

- Continuer sans attendre : compensation, fiscalité, finances locales — non touchées.
- Après la phase 2 seulement : les chapitres des cotisations et des caisses.
- Après la phase 4 seulement : les retraites.

## Le niveau de modèle, pour ne pas consommer trop de jetons

Table `modeles.claude-code` de `docs/agents/roles.yml` : *raisonnement* = Opus, *standard* =
Sonnet, *mécanique* = Haiku. Fable n'est utile que pour une réflexion de doctrine comme celle
du 17 octobre ; aucune phase d'exécution n'en a besoin.

| Travail | Niveau | Pourquoi |
|---|---|---|
| Écrire la doctrine, une présentation, un texte qui fond deux sections | raisonnement (Opus) | jugement sur le fond et la forme |
| Déplacer des fichiers, réécrire des liens par script, `_quarto.yml`, scripts de build, fusion des `references.json`, redirections | standard (Sonnet) | méthode réglée, résultat contrôlé par `verifier.sh` et les tests |
| Rendus, `verifier.sh`, régénérations, surveillance de la CI | mécanique (Haiku) | le résultat se lit dans un code de sortie |

Autres économies :

- La session principale arbitre et vérifie ; les phases 2 à 5 se lancent en sous-agents au
  niveau indiqué, une phase à la fois.
- Donner aux sous-agents les plages de lignes plutôt que des fichiers de 37 000 mots entiers.
- Les inventaires et la réécriture des liens se font par script, pas par lecture.
