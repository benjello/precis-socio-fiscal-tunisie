# Chantier — les ruptures au premier plan, le détail replié

Ouvert le 7 octobre 2026. Chantier à part : il touche la manière d'écrire tous les volumes, pas un
chapitre. Il se teste d'abord sur la TVA ; rien n'est étendu avant que le prototype soit jugé.

## Le constat

Les longs tableaux qui listent, date par date, toutes les réformes et tous les petits changements
d'un dispositif mettent sur le même plan une rupture de politique publique et un ajustement de
paramètre. Le lecteur reçoit trop d'informations d'un coup et doit faire le tri lui-même. Ces
tableaux sont pourtant précieux : ce sont presque des frises chronologiques, et il ne faut pas
les perdre.

## Le principe (consigne du propriétaire, 7 octobre 2026)

- **Au premier plan : les ruptures de politique publique et leur mise en œuvre progressive.**
- **En dessous, replié : le long tableau historique**, entier, dans un encadré escamotable (ou en
  annexe). On garde le détail sans le donner d'un seul coup.
- **Ce qu'est une rupture.** Elle est politique, et elle se lit dans les textes de loi :
  l'arrivée d'un nouveau dispositif — même s'il échoue ensuite —, un nouveau public cible, un
  nouvel objectif. Un changement de niveau d'un paramètre n'en est pas une ; il est une étape de
  mise en œuvre ou un ajustement.
- Classer est un jugement, et il est assumé. Le texte dit ce que la loi cherche à faire, sans
  commentaire sur son bien-fondé ; le ton reste documentaire.

## La forme, telle que le prototype la met en œuvre

Section « Le crédit et sa restitution » du chapitre de la TVA (`precis/fr/fiscalite/_tva.qmd`,
`#sec-tva-credit-restitution`), branche `chantier/ruptures-au-premier-plan`.

1. **Le mécanisme**, en deux paragraphes (inchangés).
2. **Un tableau des ruptures**, court (trois lignes ici), à quatre colonnes : la rupture et sa
   date ; ce que la loi cherche ; l'état avant → après ; la mise en œuvre, étape par étape.
3. **Le récit**, qui suit les ruptures (les « trois temps » déjà écrits).
4. **L'état du droit aujourd'hui**, en un paragraphe.
5. **La chronologie complète, repliée** : le tableau de 19 lignes, avec une colonne « Portée » qui
   dit de chaque ligne si elle est une rupture, une étape (et de quelle rupture) ou un ajustement.

Mécanique : un bloc `:::: {.chronologie-repliable titre="…"}` autour du tableau.
`precis/legendes.html` le place dans un `<details>` replié ; un renvoi `@tbl-…` ou une adresse en
`#tbl-…` vers un élément du bloc le déplie avant de défiler ; l'impression le déplie. Sans script,
et en PDF, le bloc reste visible tel quel. Style dans `precis/legendes.scss`.

## Ce que le test doit établir

- [ ] La lecture y gagne-t-elle : voit-on la politique avant le détail ?
- [ ] Les trois ruptures retenues sont-elles les bonnes (apurer le stock en 1999 ; tout restituer
      en 2007 ; restituer vite en 2010) ? La colonne « Portée » aide-t-elle ou alourdit-elle ?
- [ ] Le tableau des ruptures ne porte pas de citation : il renvoie à la chronologie repliée, qui
      les porte toutes. Est-ce acceptable, ou chaque rupture doit-elle citer son texte ?
- [ ] Comportement du repli dans le navigateur : dépliage par un renvoi, recherche dans la page
      (un contenu replié peut échapper à la recherche selon le navigateur), impression. À
      contrôler à l'œil : le rendu sans tête n'a pas pu être vérifié ici.
- [ ] Rendu PDF : le tableau doit y rester entier.
- [ ] Version arabe : l'attribut `titre` du bloc doit être traduit ; le script ne lit que cet
      attribut.
- [ ] Les ruptures se retrouvent-elles sur les figures de longue période (marques de rupture) ?
      Ici, aucune série budgétaire n'encadre une réforme : rien à marquer.

## Ce qui ne se replie pas

Un tableau court ; un tableau dont dépend la lecture d'une figure ; un tableau engendré de
paramètres en vigueur. Les tableaux engendrés ne peuvent pas porter la colonne « Portée » : la
hiérarchie se dit alors dans le texte.

## Extension, si le test est concluant

1. `docs/conventions-redaction.md` : le plan type d'un dispositif devient — historique ;
   description ; **ruptures et mise en œuvre** ; chronologie repliée ; longue période et données.
2. `docs/agents/redacteur.md` : la consigne ci-dessus, avec le critère de la rupture.
3. Un rôle nouveau, en amont du rédacteur : **architecte** (nom validé par le propriétaire le 7 octobre 2026 ; rôle écrit dans `docs/agents/architecte.md` et déclaré dans `roles.yml`, sur cette branche — il n'entre dans la chaîne `/rediger` qu'après le verdict du prototype). Il lit la note
   documentaire et rend un plan d'ensemble : les grandes sections ; ce qui est au premier plan
   (ruptures, publics, objectifs, ordres de grandeur) ; ce qui passe en détail escamotable ou en
   annexe ; les figures attendues. Il n'écrit pas le texte. Place dans la chaîne : documentaliste
   → bibliographe (versement) → terminologue (termes) → **architecte** → rédacteur → … Niveau
   « raisonnement ».  Autres noms envisagés : « éditeur » (ambigu avec l'éditeur d'un
   livre), « planificateur » (ne dit pas la hiérarchie des plans).
4. Reprise des chapitres, par ordre d'intérêt : politiques de l'emploi (cadres de 1993, 2009,
   2019 ; tableau des textes) ; salaire minimum ; compensation (réformes) ; cotisations (taux) ;
   retraites.

## Décisions du propriétaire, au fil du test

- **7 octobre 2026 — les études extérieures ne sont pas urgentes.** La place des rapports
  extérieurs et des études d'incidence dans le plan d'un chapitre (où, à quel niveau, repliés ou
  non) sera fixée dans la doctrine de l'architecte, dans un second temps. D'ici là, l'architecte
  ne leur cherche pas de place nouvelle : il laisse là où ils sont ceux que le chapitre porte
  déjà, et le récit économique se construit d'abord sur le budgétaire.
- **7 octobre 2026 — l'épine chronologique.** Le premier plan de l'architecte pour la TVA rangeait
  tout par dispositif et réduisait la chronologie à un tableau : refusé. Il faut garder la
  dimension chronologique, bien expliquer la mise en place et les grandes réformes, et s'appuyer
  dessus pour décrire les dispositifs. Doctrine retenue (« Parfait ») : une épine chronologique
  — mise en place, puis grandes réformes dans l'ordre — qui suit le cœur du dispositif et annonce
  chaque nouveau dispositif à sa naissance ; puis une fiche par disposition secondaire, qui garde
  sa section ; un fait raconté une seule fois en entier. Nouveau plan type : en bref ; mise en
  place ; grandes réformes ; état du droit ; dispositifs ; longue période. Versé dans
  `docs/agents/architecte.md`, avec le retour du premier essai (registre de destination, deux
  niveaux de ruptures, questions au documentaliste, degrés de lecture).

## Ce que la conversion de la TVA a appris — mode d'emploi pour les autres chapitres

Écrit le 7 octobre 2026, après la conversion complète du chapitre de la TVA (11 000 mots, 62
références, une matinée). À relire avant de convertir un autre chapitre ; à corriger à chaque
conversion.

### L'ordre qui a marché

1. **L'architecte d'abord, sur le chapitre tel qu'il est.** Il rend une fiche de plan :
   frontière entre le cœur et le secondaire, épine (mise en place, grandes réformes), fiches,
   classement des textes, et surtout le **registre de destination** — chaque section, tableau,
   figure, `TODO` et ancre du chapitre, avec sa place dans le nouveau plan. Sans ce registre,
   « ne rien perdre » ne se prouve pas. Compter une demi-heure, et un second passage : le premier
   plan a été refusé (tout par dispositif, la chronologie réduite à un tableau).
2. **Le propriétaire tranche** les points que l'architecte laisse ouverts (bornes des réformes,
   place d'une figure, forme d'un tableau). Cinq questions courtes ont suffi.
3. **Le documentaliste comble « ce que la loi cherche ».** Les notes documentaires ne relèvent
   presque jamais les rubriques sous lesquelles les lois rangent leurs articles : quatre des cinq
   réformes n'avaient pas d'objet. Un ticket borné (liste d'articles, rubriques mot pour mot,
   dates d'effet douteuses) a pris une demi-heure et a aussi corrigé trois erreurs des notes.
   À l'avenir, **le documentaliste relève ces rubriques dès la première passe**.
4. **Le rédacteur réorganise, il ne récrit pas.** Consigne : une réorganisation, aucun fait
   nouveau hors de la note complémentaire, tous les identifiants conservés. Les passages
   inchangés se recopient mécaniquement depuis une copie de départ. Une demi-heure.
5. **Le domicile unique vient en dernier, sur le chapitre déjà réorganisé** : ancres sur les
   lignes des registres, puis les références de loi sortent du fil de la prose. Un quart
   d'heure, parce que les registres existaient déjà.

### Les contrôles à ne pas sauter

- **Mesurer avant.** Mots, appels de citation, clés distinctes, couples (clé, localisateur),
  ancres de glossaire, identifiants, `TODO`, ancres `RECHERCHE` — sur une copie de départ
  gardée hors du dépôt. À l'arrivée : toutes les clés, tous les couples, toutes les ancres, tous
  les identifiants ; chaque manque justifié un par un.
- **`scripts/check_domicile_references.py`** : aucune loi citée dans le fil d'une section
  `.domicile-unique`, tout lien `#r-…` a son ancre, toute ancre est sur une ligne qui cite.
- **Voir dans un vrai navigateur.** Le rendu ne suffit pas : les infobulles, le dépliage et le
  retour se vérifient avec Playwright (`uv run --with playwright`, Firefox, en `file://`, qui
  est le mode de relecture du propriétaire). Le Chromium du système, lancé sans tête, rend des
  pages blanches.
- **`scripts/verifier.sh --sans-reseau <livre>`** après chaque étape ; la numérotation refuse
  une section à une seule sous-section, ce que la réorganisation produit facilement.

### Les pièges rencontrés

- **Le chapitre grossit.** 11 000 → 22 000 mots, le premier plan + 57 % : registres nouveaux,
  rubriques citées, phrases de situation. Le propriétaire l'accepte tant que le détail est
  replié ; à surveiller, et à dire.
- **Les références s'empilent dans les cellules de registre** quand on y regroupe les appels
  de plusieurs phrases : la même loi trois fois, avec des articles presque identiques. Dédoublonner
  (un localisateur contenu dans un autre disparaît) avant de regarder les infobulles.
- **Un tableau engendré ne porte pas d'ancre.** Lui adjoindre, dans le même bloc replié, un petit
  tableau de textes fait main (date d'effet — texte et article — ce qui change).
- **Des références n'ont pas de ligne où loger** (clauses de date, textes cités une fois pour
  situer) : prévoir un registre de plus plutôt que de laisser la citation dans le fil.
- **Un texte sert plusieurs dispositifs.** Une ligne dans chaque registre ; le lien de la prose va
  au registre du dispositif dont parle la phrase.
- **Les exposants de note ne conviennent pas en HTML** (essayés, refusés) ; un lien vers le
  tableau sans retour non plus. Le modèle retenu : signal sur le mot, infobulle où l'on peut
  cliquer, bouton « Revenir au texte ». Les notes de bas de page ne reviendront que pour le PDF.
- **Le glossaire est sur une autre page**, et `fetch()` ne marche pas en `file://` : les
  définitions sont embarquées par `build_glossary.py` (`_glossaire.infobulles.html`), et chaque
  livre doit l'inclure dans son `_quarto.yml`, dans les deux langues, à la main.
- **Squash et branches empilées.** Fusionner en squash la branche de dessous met la branche du
  dessus en conflit sur tout ce qu'elles partagent ; prendre la version de master pour ce que
  la branche du dessus ne modifie pas, la sienne pour le reste, puis vérifier le diff.
- **Deux agents, jamais le même worktree.** Chaque étape a eu sa branche et son répertoire.

### Ce qui reste à décider avant de généraliser

- Brancher `check_domicile_references.py` dans `verifier.sh` et la CI.
- Inclure les infobulles du glossaire dans les dix-huit `_quarto.yml`.
- La colonne « Texte » des tableaux engendrés, à remplacer par une infobulle.
- La place des études et des rapports extérieurs dans le plan (doctrine de l'architecte).
- La frise de tête ; le PDF (filtre qui change un lien `#r-…` en note de bas de page) ; l'arabe
  (attributs `titre` des blocs, libellés, chapitres en retard de structure).
- L'ordre des volumes : commencer par les chapitres dont les registres existent déjà.
