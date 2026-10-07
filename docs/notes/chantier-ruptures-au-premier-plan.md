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
3. Un rôle nouveau, en amont du rédacteur — nom proposé : **architecte**. Il lit la note
   documentaire et rend un plan d'ensemble : les grandes sections ; ce qui est au premier plan
   (ruptures, publics, objectifs, ordres de grandeur) ; ce qui passe en détail escamotable ou en
   annexe ; les figures attendues. Il n'écrit pas le texte. Place dans la chaîne : documentaliste
   → bibliographe (versement) → terminologue (termes) → **architecte** → rédacteur → … Niveau
   « raisonnement ». À créer dans `docs/agents/architecte.md` et `docs/agents/roles.yml`, puis
   `scripts/sync_agents.py`. Autres noms envisagés : « éditeur » (ambigu avec l'éditeur d'un
   livre), « planificateur » (ne dit pas la hiérarchie des plans).
4. Reprise des chapitres, par ordre d'intérêt : politiques de l'emploi (cadres de 1993, 2009,
   2019 ; tableau des textes) ; salaire minimum ; compensation (réformes) ; cotisations (taux) ;
   retraites.
