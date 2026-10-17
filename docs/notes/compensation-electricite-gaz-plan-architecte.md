# Fiche de plan : « L'électricité et le gaz » (`precis/fr/compensation/_electricite_gaz.qmd`)

Proposition d'emplacement : `docs/notes/compensation-electricite-gaz-plan-architecte.md`. J'ai travaillé en lecture seule et n'ai écrit aucun fichier.

## Résumé

- **Ruptures possibles.** Après 1992, aucune rupture du tarif ne repose sur un texte dont la note a lu l'article. Seules deux réformes passent la règle :
  - 1984, la tranche économique ;
  - 1991-1992, le prix hors taxe et homologué.
- **Plan proposé.** Vue d'ensemble ; une mise en place jusqu'en 1982 ; quatre grandes réformes (1984, 1991-1992, 2014, 2015) ; l'état du droit au 1er janvier 2024 ; deux sections de dispositifs (le gaz des ménages, les tarifs des entreprises) ; la longue période.
  - **2014** est retenue à titre d'exception. Elle repose sur la grille de la STEG lue à l'image ; l'acte qui l'homologue n'est pas identifié. C'est la question Q1.
  - **2015** tient en trois phrases et renvoie au chapitre des carburants, qui la raconte déjà en entier.
- **Bornes refusées.** Les bornes actuelles 1970-1992, 1993-2003 et 2004-2024 découpent selon les sources disponibles, pas selon des réformes. Elles ne servent plus qu'à construire et légender les tableaux repliés.
- **Identifiants.** Les 25 identifiants sont conservés. Deux sections gardent leur identifiant parce que `docs/recherches.yml` les vise : `sec-compensation-eg-autorite` et `sec-compensation-eg-grilles`. Aucun tableau ne fusionne deux familles de sources.
- **Croissance.** Environ +33 % au total (8 300 → 11 000 mots). Le texte visible baisse d'un tiers environ (7 800 → 5 200 mots).

Les degrés de lecture viennent des notes : **[JO]** Journal officiel lu à l'image ; **[JO partiel]** ; **[intitulé]** seul l'intitulé est connu ; **[STEG-I]** document de la STEG lu à l'image ; **[STEG-H]** page archivée de la STEG portant sa date d'effet ; **[relais]** agence publique tunisienne ; **[ext]** rapport extérieur ; **[cité]** acte connu parce qu'un tiers le cite. Seuls [JO] et, si le propriétaire l'accepte (Q1), [STEG-I] portent une rupture.

Notes citées : **NE** = `compensation-tarifs-electricite-gaz.md` ; **N93** = `compensation-tarifs-1993-2004.md` ; **NMT** = `compensation-tarifs-mt-ht-gaz.md` ; **N14** = `compensation-rapport-2014.md` ; **N15** = `compensation-rupture-2015.md` ; **NC** = `compensation.md`.

---

## 1. La frontière

**Les règles de base**, c'est-à-dire ce sans quoi le dispositif n'existe pas :
- le tarif de l'électricité en basse tension des ménages : structure (tranches, prix, redevance) et niveau ;
- l'autorité qui le fixe ;
- les accessoires qui changent sa base (passage hors TVA en 1991, taxe du Fonds de transition énergétique) ;
- la manière dont l'écart au coût est financé.

Ce financement (circuit ETAP-STIR-STEG, prix de cession du gaz de 1993, rupture de 2015) a déjà sa place dans `_carburants.qmd` : `#sec-compensation-circuit`, `#sec-compensation-cout-economique`, `#sec-compensation-rupture-2015`. Ici, il se dit en une à trois phrases avec renvoi.

**Les dispositions secondaires**, qui aménagent le tarif pour un produit ou un public :
- **le gaz des ménages** (basse pression). Ses grilles changent aux mêmes dates, et le chapitre dit qu'il « suit la même évolution » ;
- **les tarifs des entreprises** : moyenne et haute tension, gaz en moyenne et haute pression. Leur logique est propre (prime de puissance, postes horaires, formule indexée sur le fuel lourd), et ils naissent groupés dans la mise en place (1975, 1978, 1987).

**« Qui fixe les tarifs » n'a pas sa propre section** (question Q2). Ses seuls événements écrits — les arrêtés, l'homologation de 1991-1992 — sont précisément ceux de la mise en place et de la deuxième réforme. Une section séparée les raconterait une seconde fois. L'autorité en vigueur va dans l'état du droit, qui reprend l'identifiant `sec-compensation-eg-autorite`.

**Ce qui n'est pas un dispositif.** Le coût, le prix de vente moyen, la recette moyenne et le rapprochement des subventions sont des données. Ils vont dans la longue période.

---

## 2. Le plan

Chaque section suit le même ordre : l'essentiel en une phrase, une vue courte, deux à quatre points, puis le bloc replié.

### `# L'électricité et le gaz {#sec-compensation-electricite-gaz}`

Le paragraphe d'ouverture (l. 3) est récrit pour annoncer le nouveau plan. On y garde, en tête :
- le renvoi vers les carburants (`@sec-compensation-carburants-chapitre`), pour le financement ;
- le renvoi vers l'incidence (`@sec-compensation-incidence-energie`) ;
- la phrase sur les rapports extérieurs, employés seulement de 1993 à 2004 et présentés à part ;
- le lien `#g-steg`.

### `## Vue d'ensemble {#sec-compensation-eg-vue}` (nouvelle)

- **Essentiel.** La STEG vend l'électricité et le gaz à des tarifs administrés, inférieurs à leur coût. L'écart est couvert par une subvention, que le budget porte seul depuis 2015.
- **Vue.** Un tableau court, nouveau : « Le tarif des ménages en cinq dates ».

  | Date | Structure | Prix (millimes par kWh) |
  |---|---|---|
  | 1970 | dégressif | 45 à 25 |
  | 1984 | tranche économique | 51 / 70 |
  | 1992 | hors taxe, homologué | 59 / 76 |
  | 2014 | six tranches | 75 à 350 |
  | 2022 | prix de la tranche atteinte | 62 à 414 |

  Les valeurs sont toutes déjà dans le chapitre.
- **Points.**
  - Le tarif est devenu progressif en 1984 ; depuis 2014, les hausses portent sur les fortes consommations.
  - Le prix de vente moyen est de 133 millimes en 2012, pour un coût de 259,6. De 2022 à 2025, il représente 58 à 64 % du coût selon l'Observatoire, en données provisoires. Ce sont des chiffres datés, avec renvoi à leurs tableaux.
  - Depuis 1992, les grilles ne paraissent plus au *Journal officiel*.
- **Commentaire.** Le TODO « figures » de la l. 27 vient ici, complété de la part « TVA et surtaxe » du TODO de la l. 174.

### `## La mise en place : un prix maximum arrêté par le ministre, jusqu'en 1982 {#sec-compensation-eg-mise-en-place .domicile-unique}` (nouvelle)

- **Essentiel.** La STEG propose, le ministre arrête des « prix de vente maxima », publiés au *Journal officiel*.
- **Points.**
  - **L'autorité.** On reprend l. 9 : la délibération de la STEG visée en 1970 et 1975 ; l'arrêté conjoint de 1978 ; les visas de la loi du 19 mai 1970 à partir de 1982.
  - **Du dégressif au prix unique.** Tarif dégressif en 1970 et 1975 ; prix unique de l'éclairage en 1978 ; tarif général unique en 1981.
  - **Naissances groupées**, une ligne chacune, avec renvoi : tarif de la moyenne tension à postes horaires (1975) ; haute tension (1978) ; gaz, avec la formule indexée sur le fuel lourd pour la haute pression (1987, premier texte lu).
- **Replié.** Bloc « Tarifs de l'électricité et du gaz fixés par décret et par arrêté : textes, date par date, 1961-1982 ». Nouveau tableau `tbl-compensation-eg-textes-1961-1982`, colonnes Effet | Portée | Texte | Avant → après. Il réunit :
  - les lignes 1970-1982 de `tbl-…-grilles-jo` ;
  - les lignes 1978, 1981 et 1982 déplacées de `tbl-…-ajustements` ;
  - les intitulés du TODO de la l. 21, signalés en clair : « seul l'intitulé de ce texte est connu ici ».

### `## Les grandes réformes, 1984-2015 {#sec-compensation-eg-reformes .domicile-unique}` (nouvelle)

En tête, un tableau court sans citations, `tbl-compensation-eg-reformes` (nouveau), colonnes Date | Ce qui change | Portée : quatre lignes en gras « rupture », et les étapes 2006, 2018 et 2022.

#### `### 1984 : un prix réduit pour les cinquante premiers kilowattheures des petits abonnés {#sec-compensation-eg-1984}`

- **Avant → après.** Un prix unique de 61 millimes devient une tranche économique à 51 (abonnements de 1 à 2 kVA, jusqu'à 50 kWh par mois) et une tranche normale à 70. Le tarif des ménages devient progressif.
- **La réserve reste au premier plan** : c'est « la première apparition établie ici », les arrêtés de 1980 et de janvier 1981 n'étant connus que par leur intitulé.
- **Entre-temps.** Une phrase sur les niveaux de 1987, avec renvoi au registre.

#### `### 1991-1992 : un prix hors taxe, homologué par l'administration {#sec-compensation-eg-1992}`

- **Ce qui change.**
  - Des prix hors TVA à partir du 1er janvier 1991.
  - La loi de 1991 sur la concurrence et les prix et le décret 91-1996, qui range « Électricité, eau et gaz » parmi les produits soumis à l'homologation des prix à tous les stades.
  - La décision du 11 août 1992, art. 1.
  - On reprend l. 13 en entier.
- **Point au premier plan.** Les prix ne se comparent pas d'un côté et de l'autre de 1987-1991 : taxes comprises avant, hors TVA après.
- **Conséquence.** C'est le dernier acte tarifaire publié. La décision du 10 août 2000 n'est connue que parce que l'API la cite (l. 17, une phrase).
- **Entre-temps, 1993-2013**, en deux ou trois phrases :
  - des grilles qui ne paraissent plus au *Journal officiel* ;
  - six ans sans ajustement, de 1994 à 2000 ;
  - en 2006, une seconde tranche au-delà de 300 kWh (étape de 1984) ;
  - quatre hausses en quatorze mois en 2007-2008 (on reprend l. 149) ;
  - un renvoi vers les carburants pour le prix de cession du gaz de 1993 et la première ligne budgétaire de 2004 ;
  - un renvoi vers la section des entreprises pour le tarif interruptible de 2013.

#### `### 2014 : six tranches, et un prix unique pour les petites consommations {#sec-compensation-eg-2014}`

- **Rupture.** Le 1er mai 2014, on passe de trois prix à six tranches. En deçà de 200 kWh, un prix unique s'applique à toute la consommation (on reprend l. 100). La réserve « acte d'homologation non identifié » est dite au premier plan.
- **Le même jour**, en deux phrases avec renvoi :
  - les postes horaires de la moyenne et de la haute tension changent de sens ;
  - le gaz en haute pression n'est plus indexé sur le fuel lourd ;
  - le gaz des ménages passe à quatre tranches.
- **Mise en œuvre.**
  - 1er septembre 2018 : le seuil du prix unique passe de 200 à 100 kWh.
  - 1er mai 2022 : toute la consommation est facturée au prix de la tranche atteinte (l. 101-102).
  - On reprend l. 104 sur 2019 et l'impossibilité de comparer les prix de tranche.
- **Variante possible**, à trancher (§ 7) : le partage entre ménages et autres abonnés de l'électricité en 2014 est dans NE (ii), pas dans le chapitre. Le rédacteur ne peut l'ajouter qu'avec l'accord du propriétaire.

#### `### 2015 : la STEG achète son gaz au prix mondial {#sec-compensation-eg-2015}`

- **Contenu.** Trois phrases. Jusqu'en 2014, la STEG reçoit son gaz à un prix de cession préférentiel : c'est la subvention indirecte, qui n'est inscrite nulle part en dépense. Avec liens `#g-prix-de-cession-preferentiel`, `#g-subvention-indirecte` et `#g-subvention-directe`. On reprend l. 368, première moitié.
- **Ce qui change.** À partir de 2015, la ligne budgétaire versée à la STEG et la subvention d'exploitation inscrite dans ses comptes coïncident : 858 MD.
- **Renvois.** `@sec-compensation-rupture-2015` pour le récit, et la longue période pour le rapprochement.
- **Entre-temps, 2017-2024.** Une phrase : 2017 et 2019 sont des ajustements, 2024 est la taxe du Fonds de transition énergétique (renvoi à l'état du droit).

#### `### Les grilles des ménages, date par date {#sec-compensation-eg-grilles}` (identifiant conservé)

- **Essentiel.** Les grilles viennent de trois familles de sources selon les années, et les prix d'une date ne se comparent pas tels quels à ceux d'une autre.
- **Points.**
  - Le *Journal officiel* jusqu'en 1992 ; des agences publiques ou un rapport extérieur de 1993 à 2003 ; la STEG depuis 2004 (on reprend l. 25).
  - Les changements de base fiscale et de structure : 2006, 2014, 2018, 2022.
- **Replié, trois blocs :**
  - **B1** « Le tarif de l'électricité des ménages, grille par grille, 1970-2022 » : `tbl-…-grilles-jo` (lignes 1984-1992 ; les lignes 1970-1982 sont recopiées au registre de la mise en place ou y renvoient, voir Q3) et `tbl-…-grilles-steg`, chacun avec une colonne « Portée ». On y met l. 45, sauf la réserve de 1984, qui reste au premier plan. On y met aussi le morceau du TODO de la l. 174 sur la grille du 1er janvier 2014, celle de mars 2013 et la contradiction de juin 2010.
  - **B2** « Les grilles des ménages de 1993 à 2003 : deux familles de sources, et la contradiction de 2003 ». On y met l. 49 et 51, `tbl-…-grilles-relais`, l. 61, `tbl-…-grilles-exterieures`, l. 70, 72 et 74, et l'ancre `RECHERCHE r-tarifs-electricite-grilles-1993-2003`. Les deux tableaux restent séparés.
  - **B3** « Les ajustements du tarif des ménages, date par date, 1984-2024, avec leur portée ». C'est le **registre des règles de base**, qui porte les ancres `#r-…`. On y met `tbl-…-ajustements`, élargi d'une colonne Portée et d'une colonne Texte (article), et `tbl-…-ajustements-1992-2006`, dont la colonne « Famille » est gardée et à qui l'on ajoute une colonne Portée. Il faut deux lignes nouvelles, tirées des notes : le décret 91-1996 et la loi de finances complémentaire pour 2015.

### `## L'état du droit au 1er janvier 2024 {#sec-compensation-eg-etat-du-droit .domicile-unique}` (nouvelle ; rien n'y est replié)

#### `### La grille des ménages`
- La grille du 1er mai 2022, avec ses prix en une phrase, et la redevance de 700 millimes.
- La taxe du Fonds de transition énergétique : 5 millimes par kWh à compter du 1er janvier 2024, sauf pour la tranche économique jusqu'à 100 kWh par mois.
- On reprend la légende de `tbl-…-grilles-steg`.

#### `### Qui fixe les tarifs {#sec-compensation-eg-autorite}` (identifiant conservé)
- L'acte qui fixe les grilles depuis 1992 n'est pas identifié ici (l. 17, seconde moitié).
- L'ancre `RECHERCHE r-tarifs-electricite-gaz-apres-1992`.
- Le morceau du TODO de la l. 21 sur le décret 2015-307.

### `## Le gaz des ménages {#sec-compensation-eg-gaz .domicile-unique}` (titre nouveau ; la sous-section n'avait pas d'identifiant)

- **D'abord, l'objet** : le gaz naturel en basse pression, en millimes par thermie.
- **Situation.** Le gaz paraît dans les textes lus à partir de 1987, dans la mise en place.
- **Points.**
  - Un prix unique jusqu'en 1992 (l. 153).
  - Trois tranches en 2008.
  - Quatre tranches en 2014 (étape de 2014).
  - Les ménages distingués des autres abonnés en 2018.
  - Depuis 2014, la première tranche ne bouge presque plus et la dernière double (l. 170).
- **Replié.** Bloc « Tarif du gaz naturel en basse pression, grille par grille, 1987-2022 » : `tbl-…-gaz`, avec une colonne Portée, et le morceau du TODO de la l. 174 sur les grilles du gaz.

### `## Les tarifs des entreprises : moyenne et haute tension, gaz en moyenne et haute pression {#sec-compensation-eg-mt-ht .domicile-unique}` (identifiant conservé)

- **Situation.** Ces tarifs naissent dans la mise en place (1975, 1978, 1987), et ils changent de structure en 2014.
- **`### Comment se lit un tarif de moyenne ou de haute tension`** : rien n'est replié. On garde l. 182-198 et `tbl-…-postes`, qui est court et nécessaire pour lire la suite. On y ajoute la phrase sur le tarif interruptible de 2013, signalée comme connue parce que la STEG la cite.
- **`### La moyenne tension`**
  - Premier plan : l. 239 (de 2004 à 2022, kWh de jour de 58 à 290 millimes, prime de 3 000 à 11 000 ; la plus forte hausse en septembre 2018).
  - Replié : bloc « Tarif de l'électricité en moyenne tension, grille par grille, 1975-2022 », avec `tbl-…-mt-jo`, `-mt-2004` et `-mt-2014`, une colonne Portée chacun. On y met l. 202.
  - La réserve « valeurs de 1975 à 1990 d'une première transcription » reste dans la légende.
- **`### La haute tension`**
  - Premier plan : l. 270-273 (pas de hausse en 2019 ; deux dates en 2022).
  - Replié : bloc « …haute tension, 1978-2022 », avec `tbl-…-ht-jo`, `-ht-2004` et le TODO bibliographe de la l. 172.
- **`### Le gaz en moyenne et haute pression`**
  - Premier plan : l. 296 et la fin de l'indexation en 2014.
  - Replié : `tbl-…-gaz-mp-hp`, et le morceau du TODO de la l. 174 sur la grille de la FIPA et les grilles de 1994 à 2003.

### `## La longue période : subvention, coût et prix de vente {#sec-compensation-eg-longue-periode}` (nouvelle ; le budgétaire d'abord)

#### `### La subvention à la STEG {#sec-compensation-eg-lien}` (identifiant conservé, descendu d'un niveau)
- On garde l. 368 (la ligne « carburants » versée à la STEG ; les notions redéfinies), l. 370, `tbl-…-rapprochement` visible, l. 381 et 383, et le TODO de la l. 385.

#### `### Coût et prix de vente du kilowattheure {#sec-compensation-eg-cout}` (identifiant conservé)
- On garde l. 314.
- Les sous-sections viennent dans cet ordre : 2008-2012, d'après le rapport de contrôle ; depuis 2017, d'après l'Observatoire ; « La recette moyenne par kilowattheure : un calcul » (déplacée de la section des entreprises, avec un renvoi depuis celle-ci) ; « 2000-2004, selon un rapport extérieur » en dernier, titrée comme telle.
- Les tableaux restent visibles tant qu'aucune figure ne les remplace (Q4).

---

## 3. Les grandes réformes : sources, avant → après, ce que la loi cherche

| | Texte et lecture | Avant → après | Ce que la loi cherche | Dispositifs qui y naissent |
|---|---|---|---|---|
| **Mise en place (jusqu'en 1982)** | arrêtés des 7 août 1970, 15 avril 1975, 30 septembre 1982 [JO] ; 27 novembre 1978 et 1er septembre 1981 [JO partiel] ; décret 61-47 et arrêtés de 1963 [intitulé] | — | les mots des arrêtés : « prix de vente maxima », sur délibération de la STEG (1970, 1975). Rien de plus | moyenne tension (1975), haute tension (1978), formule du gaz en haute pression (1987) |
| **G1, 31 mai 1984** | arrêté du 4 juin 1984, JORT n° 38, p. 1378-1379 [JO] | prix unique 61 → tranche économique 51 (1-2 kVA, ≤ 50 kWh par mois) et tranche normale 70 | **objet non relevé** : l'intitulé dit seulement « fixant les tarifs de l'électricité » | — |
| **G2, 1er janvier 1991 - 1er août 1992** | arrêté du 19 décembre 1990 (prix hors TVA) [JO] ; décret 91-1996, art. 2 et tableau A [JO] ; décision du 11 août 1992, art. 1 [JO] ; loi 91-64, art. 3 : visée seulement, article non lu | « prix de vente maxima » arrêtés en vertu de la loi de 1970 → prix hors taxe soumis à « l'homologation des prix à tous les stades » | **relevé** : intitulé du décret (« produits et services exclus du régime de la liberté des prix et […] modalités de leur encadrement ») ; titre du tableau A ; définition de l'art. 2 (« fixation préalable par l'administration du niveau des prix ou de leurs variations ») ; art. 1 de la décision | — (le régime de l'autorité tarifaire) |
| **G3, 1er mai 2014** (sous réserve de Q1) | grille de la STEG du 1er mai 2014 [STEG-I] ; acte d'homologation non identifié | trois prix → six tranches, prix unique sur toute la consommation en deçà de 200 kWh ; postes horaires redéfinis ; gaz en haute pression désindexé | **objet non relevé** | — (changements de structure dans les deux autres sections) |
| **G4, 1er janvier 2015** | loi n° 2015-30 (loi de finances complémentaire), tableau A, art. 40-01 [texte, sans article sur le sujet] ; rapport du projet de loi de finances complémentaire, § 19-20 [image] — exposé officiel ; aucun texte qui l'institue (N15 (i) 5-6) | gaz cédé à 90,8 D par tonne équivalent pétrole, subvention indirecte → gaz au prix mondial, subvention entièrement budgétaire | **relevé dans l'exposé officiel**, à citer comme tel : « séparation entre les sociétés », « opération blanche ». La formule des bulletins (« adoption du principe de séparation des opérations de commercialisation des hydrocarbures ») n'est lue qu'en couche texte | — |

**Ce que le documentaliste doit lire**, liste bornée :
1. **G1.** L'arrêté du 4 juin 1984 : les mots qui désignent la tranche et ses conditions, et tout visa. Les arrêtés du 12 juillet 1980 (n° 42, p. 1909-1910), du 10 octobre 1980 (n° 59, p. 2586-2587 ; rectificatif n° 66, p. 2808) et du 23 janvier 1981 (n° 5, p. 126-127), pour fixer la première apparition de la tranche. Le prix de l'éclairage en 1978, illisible.
2. **G2.** La loi 91-64 du 29 juillet 1991, art. 3 et intitulé. Le décret 2015-307 du 1er juin 2015 : l'électricité et le gaz restent-ils au tableau A ?
3. **G3.** Le rapport de contrôle de 2014, p. 75 et 97. Il date des hausses au 1er janvier et au **1er juin** 2014, alors que la grille porte le 1er mai (N14 § 3 C) : la date d'effet est à vérifier. Le préambule ou les visas des documents de la STEG de 2014. Tout acte d'homologation (fiche `r-tarifs-electricite-gaz-apres-1992`).
4. **G4.** Relire à l'image la note (2) des bulletins. Lire l'arrêté du 8 octobre 1993 sur le prix de cession du gaz, dans les fascicules de l'automne 1993. S'il est lu, il fait de 1993 une réforme candidate pour la naissance de la subvention indirecte, racontée dans le chapitre des carburants.
5. **Autres.** La décision du 10 août 2000, citée par l'API. La décision du 5 mars 2013 sur le tarif interruptible, citée par la STEG. Le texte qui institue la taxe du Fonds de transition énergétique, et la source du « 1 millime » antérieur (NMT § 7).

---

## 4. Le classement des textes et des grilles, par registre

Une grille qui sert plusieurs dispositifs a une ligne dans chaque registre.

### R0 — Mise en place (`tbl-compensation-eg-textes-1961-1982`, nouveau)

| Effet | Texte (lecture) | Portée | Raison |
|---|---|---|---|
| 1961 | décret 61-47 [intitulé] | point de départ, signalé | tarifs maxima ; ne porte rien |
| 1963 | arrêtés des 29 janvier (électricité) et 25 octobre (gaz de ville) [intitulé] | ajustement, signalé | — |
| 1er janvier 1970 | arrêté du 7 août 1970 [JO] | mise en place | premier texte lu : prix maxima, délibération de la STEG, tarif dégressif |
| 20 avril 1975 | arrêté du 15 avril 1975 [JO] | ajustement | toujours dégressif (par kVA) ; moyenne tension, voir R5 |
| 1976-1978 | arrêtés du 31 août 1976 (haute tension), 16 juin 1977, 27 février 1978 [intitulé] | ajustement, signalé | — |
| 30 novembre 1978 | arrêté conjoint du 27 novembre 1978 [JO partiel] | ajustement de structure | prix unique de l'éclairage ; texte partiel, ne peut porter une rupture |
| 1980-1981 | arrêtés des 12 juillet et 10 octobre 1980, 23 janvier 1981 [intitulé] | signalé | pourraient changer la date de première apparition de la tranche (G1) |
| 31 août 1981 | arrêté du 1er septembre 1981 [JO partiel] | ajustement de structure | tarif général unique, 58 |
| 29 septembre 1982 | arrêté du 30 septembre 1982 [JO] | ajustement | 61 ; visas de la loi de 1970, la délibération n'est plus visée |

### R1 — Règles de base (`tbl-…-ajustements`, élargi, avec `-ajustements-1992-2006`, `-grilles-jo`, `-grilles-steg`, `-grilles-relais` et `-grilles-exterieures`)

| Effet | Source (lecture) | Portée | Raison |
|---|---|---|---|
| 31 mai 1984 | arrêté du 4 juin 1984 [JO] | **rupture G1** | nouveau public : les petits abonnés |
| 16 juin 1987 | arrêté du 8 juin 1987 [JO] | ajustement | 59 et 72 |
| 1er janvier 1991 | arrêté du 19 décembre 1990 [JO] | étape de G2 | prix hors TVA |
| décembre 1991 | décret 91-1996 [JO] ; loi 91-64 [visée] | **rupture G2** | régime de l'homologation |
| 1er août 1992 | décision du 11 août 1992 [JO] | **rupture G2** (application) | dernier acte publié |
| octobre 1993 | ESMAP [ext] ; la BCT pour le mois [relais] | ajustement | +3 % |
| juin 1994 | FIPA [relais] ; date [ext] | ajustement | +5,9 % |
| 1995-1999 | Banque mondiale, BAD [ext] | constat | aucun ajustement |
| 1999 | BCT | hors sujet, reste en légende | mesure propre au textile |
| 15 août 2000 | décision du 10 août 2000 [cité] ; grille de l'API [relais] | ajustement, signalé | acte non lu |
| 1er août 2001 | [ext] | ajustement | — |
| 1er avril 2003 | FIPA [relais] ; date [ext] | ajustement | contradiction entre 90 et 94 |
| 1er mai 2004 ; 1er février 2005 | [STEG-H] | ajustements | — |
| 1er juillet 2005 | BAD [ext] | ajustement | — |
| 1er janvier 2006 | [STEG-H] | étape de G1 | seconde tranche au-delà de 300 kWh. Autre lecture : ajustement de structure |
| juillet et décembre 2007, avril 2008 | rapports annuels de la STEG | ajustements | pourcentages seuls |
| 1er septembre 2008 ; 1er septembre 2012 | [STEG-I] | ajustements | — |
| 1er juin 2010 | [STEG-I], contredit par le rapport annuel de 2010 | ajustement | contradiction gardée en légende |
| 1er mai 2014 | [STEG-I] | **rupture G3** (Q1) | nouvelle structure |
| 1er janvier 2015 | loi de finances complémentaire pour 2015 ; exposé officiel | **rupture G4** | nouveau financeur ; ligne nouvelle, avec renvoi |
| 1er janvier 2017 | [STEG-I] | ajustement | tranche 101-200 kWh de 140 à 162 |
| 1er septembre 2018 | [STEG-I] | étape de G3 | seuil 200 → 100 |
| 1er juin 2019 | [STEG-I] | ajustement | autre lecture : étape de G1, la tranche économique baisse de 75 à 62 |
| 1er mai 2022 | [STEG-I] | étape de G3 | prix de la tranche atteinte |
| 1er janvier 2024 | [STEG-I] | ajustement (accessoire du prix) | taxe du Fonds de transition énergétique ; exemption des petites consommations |

Deux textes restent dans le chapitre des carburants (ou de la dépense) et ne reçoivent qu'un renvoi : l'arrêté du 8 octobre 1993 [cité] et la première ligne budgétaire de 2004 (constat).

### R2 — Gaz des ménages (`tbl-…-gaz`)
- 1987, 1991, 1992 [JO] : ajustements.
- 2008 [STEG, couche texte ; non relu à l'image, NMT § 0] : trois tranches. Étape de G1, la progressivité gagnant le gaz. Ne peut porter une rupture.
- 2010 : ajustement.
- 2014 : étape de G3 (quatre tranches).
- 2017 : ajustement.
- 2018 : étape de G3 (ménages distingués).
- 2019 et 2022 : ajustements.
- La note relève aussi 1963 [intitulé] et 1982 (146 millimes le m3 [JO]), que le chapitre ne reprend pas. Ce serait un ajout tiré de la note.

### R3 — Moyenne tension (`-mt-jo`, `-mt-2004`, `-mt-2014`)
- 1975 [JO] : naissance (mise en place groupée).
- 1978, 1981, 1982, 1984, 1987, 1991 : ajustements, tirés d'une première transcription, à relire.
- 1992 : ajustement, relu.
- 2004 [STEG-H] : ajustement de structure, quatre postes ; la date du passage de trois à quatre postes n'est pas établie.
- 2006, 2008, 2010, 2012, mars 2013 : ajustements.
- Juin 2013 : tarif interruptible [cité]. Naissance d'un dispositif dans cette section, signalée ; ne porte pas de rupture.
- 1er mai 2014 [STEG-I] : étape de G3 (postes redéfinis).
- 2017, mai 2018 : ajustements.
- Septembre 2018 : ajustement (la plus forte hausse).
- 2019, 1er octobre 2022 : ajustements.

### R4 — Haute tension (`-ht-jo`, `-ht-2004`)
- 1978 [JO] : naissance. L'arrêté de 1976 sur la haute tension 150-90 kV n'est connu que par son intitulé.
- 1981, 1982, 1984, 1987 : ajustements.
- 1991 : ajustement (la prime devient mensuelle).
- 1992 : ajustement.
- 2004, 2006, 2008, 2010, 2013 [STEG-H] : ajustements. La grille de 2012 n'est pas établie.
- 2014 : étape de G3.
- 2017, mai 2018, septembre 2018 : ajustements.
- 2019 : constat, pas de changement.
- Mai 2022 : ajustement.

### R5 — Gaz en moyenne et haute pression (`-gaz-mp-hp`)
- 1987 [JO] : formule indexée sur le fuel lourd. Premier texte lu ; naissance groupée.
- 1991, 1992 : ajustements.
- 2004 (1er mai, et 1er août pour la moyenne pression), 2006 : ajustements.
- 2008 : ajustement de structure (prix fixes en haute pression, formule au-delà de 2 000 tep).
- 2010, 2012, 2013 : ajustements.
- **1er mai 2014 [STEG-I] : rupture propre de cette section**, qui tombe dans G3 : fin de l'indexation (Q1).
- 2017, mai 2018, septembre 2018, 2022 : ajustements.

La note mentionne aussi des faits que le chapitre ne reprend pas : formule de la haute pression en 2000, tarif propre des cimentiers en 2016, grille dite « Mai 2004 » de la FIPA. Ce serait un ajout ; à voir avec le propriétaire.

Hors classement, parce que ce sont des données et non des textes : `-postes`, `-recette-moyenne`, `-cout-2008-2012`, `-cout-one`, `-cout-bad`, `-rapprochement`.

---

## 5. Le registre de destination (chapitre actuel → nouveau plan)

| Élément (ligne) | Destination |
|---|---|
| H1 `#sec-compensation-electricite-gaz` ; l. 3 (lien `#g-steg`) | en tête, récrit pour annoncer le plan ; le lien `#g-steg` reste à la première mention |
| `## Qui fixe les tarifs` `#sec-compensation-eg-autorite` | l'identifiant passe à l'état du droit, sous-section « Qui fixe les tarifs » ; le titre de section disparaît, son contenu est réparti ci-dessous |
| `### Jusqu'en 1990` (l. 7-9) | fusionné dans la mise en place (premier plan) |
| `### 1992` (l. 11-13) | fusionné dans la réforme de 1991-1992 (premier plan) |
| `### Après 1992` (l. 15-17) | la phrase sur l'API va dans la réforme de 1991-1992 ; le constat sur l'acte non identifié va dans l'état du droit |
| `RECHERCHE r-tarifs-electricite-gaz-apres-1992` (l. 19) | état du droit, « Qui fixe les tarifs » : le `ou:` de `recherches.yml` reste juste |
| TODO documentaliste (l. 21) | coupé en deux : les intitulés 1961-1981 près du registre R0 ; le décret 2015-307 dans l'état du droit |
| `## Les grilles de l'électricité` `#sec-compensation-eg-grilles` ; l. 25 | l'identifiant passe à la dernière sous-section des grandes réformes ; l. 25 y reste au premier plan |
| TODO figures (l. 27) | Vue d'ensemble |
| `### 1970-1992` (titre, l. 29) | supprimé comme borne ; contenu dans R0 et B1 |
| `tbl-…-grilles-jo` (l. 31-43) | B1, avec une colonne Portée ; les lignes 1970-1982 sont recopiées dans R0 ou y renvoient (Q3) |
| l. 45 « Trois faits » | la réserve sur 1984 au premier plan (réforme de 1984) ; le passage du dégressif au prix unique dans la mise en place ; le reste dans B1 |
| `### 1993-2003` (titre, l. 47) ; l. 49, 51, 61, 70, 72, 74 | bloc B2. Une phrase de l. 70 (1994-2000 sans hausse ; 59 → 65 et 76 → 99 en douze ans) au premier plan, dans l'entre-temps de 1991-1992 |
| `tbl-…-grilles-relais`, `tbl-…-grilles-exterieures` | B2, séparés, chacun avec une colonne Portée |
| `RECHERCHE r-tarifs-electricite-grilles-1993-2003` (l. 76) | B2, sous `#sec-compensation-eg-grilles` : le `ou:` reste juste |
| `### 2004-2024` ; `tbl-…-grilles-steg` (lien entrant depuis `_incidence.qmd`) | B1 ; identifiant conservé ; la légende de 2024 est reprise dans l'état du droit |
| `### Trois réformes de structure` (l. 96-104) | fusionné : 2014 au premier plan (réforme de 2014) ; 2018 et 2022 comme étapes de 2014 ; l. 104 dans la réforme de 2014 |
| `### Les ajustements datés` (titre) | supprimé comme titre ; devient le bloc B3 |
| `tbl-…-ajustements` | B3, registre des règles de base (Portée, Texte, ancres `#r-…`) ; lignes 1978-1982 déplacées dans R0 |
| `tbl-…-ajustements-1992-2006` | B3, colonne « Famille » gardée et colonne Portée ajoutée |
| l. 149 (comparaison avec les carburants) | coupée : les entre-temps de 1991-1992 et de 2015, premier plan |
| `### Le gaz` (l. 151-170) ; `tbl-…-gaz` | section « Le gaz des ménages », nouvel identifiant `sec-compensation-eg-gaz` ; l. 153 et 170 au premier plan ; le tableau replié |
| TODO bibliographe (l. 172) | bloc replié de la haute tension |
| TODO documentaliste (l. 174) | coupé en quatre : grilles de 1993-1994, de janvier 2014, de mars 2013 et contradiction de 2010 → B1 et B2 ; gaz des ménages → sa section ; moyenne et haute tension et gaz de 1994 à 2003, grille de la FIPA → section des entreprises ; TVA et surtaxe → TODO figures. Aucun élément perdu |
| `## La moyenne et la haute tension…` `#sec-compensation-eg-mt-ht` ; l. 178 | identifiant conservé, titre nouveau ; l. 178 réduit à la phrase de situation |
| `### Comment se lit…` (l. 180-198) ; `tbl-…-postes` | inchangé, premier plan |
| `### La moyenne tension` : l. 202, `-mt-jo`, `-mt-2004`, `-mt-2014`, l. 239 | l. 239 au premier plan ; le reste replié |
| `### La haute tension` : `-ht-jo`, `-ht-2004`, l. 270-273 | l. 270-273 au premier plan ; les tableaux repliés |
| `### Le gaz en moyenne et haute pression` : `-gaz-mp-hp`, l. 296 | l. 296 au premier plan ; le tableau replié |
| `### La recette moyenne…` (l. 298-310) ; `tbl-…-recette-moyenne` | déplacé dans la longue période, sous `eg-cout`, avec un renvoi depuis la section des entreprises |
| `## Prix de vente moyen et coût de revient` `#sec-compensation-eg-cout` ; l. 314 | devient une sous-section de la longue période ; identifiant conservé |
| sous-sections 2008-2012, depuis 2017, 2000-2004 ; `-cout-2008-2012`, `-cout-one`, `-cout-bad` ; l. 318, 331, 335, 351, 355, 364 | même ordre ; le rapport extérieur en dernier ; visibles |
| `## Le lien avec la compensation` `#sec-compensation-eg-lien` ; l. 368 (`#g-prix-de-cession-preferentiel`, `#g-subvention-indirecte`) | sous-section de la longue période ; l. 368 y reste. La définition de la subvention directe et indirecte est **reformulée** dans la réforme de 2015, avec les liens vers le glossaire. C'est permis : le texte principal doit se suffire |
| l. 370, `tbl-…-rapprochement` (lien entrant ; `#g-subvention-directe`), l. 381, 383 | longue période, visibles |
| TODO documentaliste (l. 385) | longue période, sous `eg-lien` |

**Identifiants.** Les 25 sont conservés : 6 `sec-` et 19 `tbl-`. Il faut créer 9 sections (`-eg-vue`, `-eg-mise-en-place`, `-eg-reformes`, `-eg-1984`, `-eg-1992`, `-eg-2014`, `-eg-2015`, `-eg-etat-du-droit`, `-eg-gaz`, `-eg-longue-periode`) et 2 tableaux (`-eg-reformes`, `-eg-textes-1961-1982`), plus les ancres `#r-…`.

**Ce qui est dit plusieurs fois aujourd'hui, et son lieu unique :**
- les lignes 1978-1992 sont dans `grilles-jo` et dans `ajustements` → B1 pour les grilles, R0 et B3 pour les portées ;
- les lignes 2008-2022 sont dans `grilles-steg` et dans `ajustements` → idem ;
- 2014, 2018 et 2022 sont dans « Trois réformes » et dans `ajustements` → la réforme de 2014 au premier plan, B3 pour la référence ;
- 1995-1999 est dans l. 70 et dans `ajustements-1992-2006` → idem ;
- la part de la ligne « carburants » versée à la STEG est dans l. 368, dans `rapprochement` et dans `_carburants.qmd` → la longue période ici, avec renvoi.

---

## 6. Figures et vues d'ensemble

Le chapitre n'en porte **aucune** aujourd'hui.

| Vue | Données | État |
|---|---|---|
| Tableau « Le tarif des ménages en cinq dates » (Vue d'ensemble) | valeurs du chapitre | faisable maintenant |
| Tableau `tbl-…-eg-reformes` | chapitre et notes | faisable maintenant |
| Ligne « carburants » versée à la STEG, rupture de 2015 marquée | `_seriescache/compensation-carburants-beneficiaires.csv` : STEG 2010, 2011, 2012, 2014, 2015, 2016 ; 2013 manque | faisable maintenant, mais maigre. Plus complète si l'on verse le tableau de la p. 72 du rapport de 2014 (aide directe et indirecte, 2007-2013, N14 lot 6) |
| Prix de vente moyen et coût de revient, trois familles distinguées (rapport de 2014 de 2008 à 2012 ; Observatoire de 2017 à 2025 ; BAD de 2000 à 2004, rapport extérieur), non raccordées | les trois tableaux du chapitre | après versement dans `tunisia-data`. Superposition permise, familles distinguées |
| `fig-compensation-facture-electricite`, facture type à 50-600 kWh | grilles 1970-1992 et 2004-2022 en série ; TVA, surtaxe et taxe du Fonds de transition énergétique date par date ; indice des prix déjà en cache (`ipc-longue-periode`, `bct-ipc-base2015`) | il faut documenter la TVA et la surtaxe d'abord. Une variante hors taxe 2004-2022 est possible après le seul versement des grilles |
| Tranche économique et prix le plus élevé, 1970-2022, changements de base fiscale marqués | grilles | après versement ; vue secondaire (NE (viii)) |
| Moyenne tension : jour, nuit et prime, 1975-2022, coupure en 2014 | tableaux de la moyenne tension | après versement |

---

## 7. Questions au propriétaire (avec ma recommandation)

1. **Qui peut porter une rupture après 1992 ?** Une grille de la STEG lue à l'image, quand l'acte d'homologation n'est pas identifié, peut-elle porter une grande réforme ?
   - *Je recommande* oui pour le 1er mai 2014 seulement, dit au premier plan avec sa réserve. 2006, 2018 et 2022 restent des étapes.
   - Le 1er janvier 2015 est porté par la loi de finances complémentaire et par son exposé officiel, avec la mention qu'aucun texte ne l'institue.
   - Autre choix : une épine réduite à 1984, 1991-1992 et 2015, où 2014 devient une étape de 1984. Mais la refonte la plus lourde passerait alors dans un entre-temps.
2. **« Qui fixe les tarifs »** se répartit entre la mise en place, la réforme de 1991-1992 et l'état du droit, sans section propre. *Je recommande* oui : une section séparée raconterait deux fois les seuls événements lus.
3. **Les tableaux qui se recouvrent.** *Je recommande* :
   - de garder tous les tableaux et leurs identifiants ;
   - de faire de `-ajustements` le registre des règles de base (Portée, Texte) ;
   - de déplacer ses lignes 1978-1982 dans R0 ;
   - de garder les grilles comme barèmes repliés ;
   - de laisser séparés les tableaux des relais et du rapport extérieur.

   Autre choix : fusionner `grilles-jo`, `grilles-steg` et `ajustements`. Cela économise environ 600 mots, mais casse un identifiant visé par `_incidence.qmd`.
4. **Les tableaux du coût et du prix** restent visibles dans la longue période tant qu'aucune figure ne les remplace. Ensuite, ils passent dans un encadré replié, comme pour le transport. *Je recommande* oui.
5. **Les points de détail.**
   - Le passage du dégressif au prix unique (1978-1981) reste dans la mise en place. Les textes ne sont lus qu'en partie : ils ne peuvent pas porter une rupture.
   - *Je recommande* oui. Pour 2019, je recommande « ajustement » plutôt qu'« étape de 1984 ».
   - Faut-il permettre au rédacteur de reprendre des notes trois faits absents du chapitre ? Ce sont le partage entre ménages et autres abonnés de l'électricité en 2014, le tarif du gaz de 1982 et le tarif des cimentiers en 2016. *Je recommande* non pour cette réorganisation : les inscrire au backlog.

## 8. Risques du repli

- **Ce qui doit rester au premier plan :**
  - la contradiction de 2003 (90 ou 94) : une demi-phrase dans l'entre-temps, le détail en B2 ;
  - la contradiction de 2010 entre la grille et le rapport annuel ;
  - la réserve sur la première apparition de la tranche en 1984 ;
  - la rupture de base fiscale en 1987-1991, nécessaire pour lire tout prix.
- **Les tableaux de la moyenne et de la haute tension** de 1975 à 1990 viennent d'une première transcription. La réserve doit rester dans les légendes, même repliées.
- **Les dates de 2014.** L'écart entre le 1er juin, donné par le rapport de 2014, et le 1er mai, donné par la grille, n'est pas dans le chapitre. Le rédacteur ne doit pas trancher (documentaliste, point 3).
- **2015** ne doit être raconté qu'une fois en entier, dans `_carburants.qmd`. La section d'ici s'arrête à trois phrases.

## 9. Croissance du texte

Le chapitre compte aujourd'hui 8 276 mots :
- tableaux et légendes : environ 4 850 ;
- texte courant : 2 800 ;
- commentaires : 450.

Estimation après conversion :
- texte courant : environ 4 300 (+1 500 : Vue d'ensemble, phrases de situation, sections de réforme, état du droit) ;
- tableaux : environ 6 100 (+1 250 : R0, `tbl-…-reformes`, colonnes Portée et Texte, lignes de 1991 et de 2015).

**Le total passe à environ 11 000 mots (+33 %). Le texte visible passe d'environ 7 800 à environ 5 200 mots (environ −33 %)**, puisque près de 4 100 mots de tableaux sont repliés. La croissance est moindre que pour la TVA (+100 %), parce que le chapitre est fait surtout de barèmes qui existent déjà.

## Fichiers utiles

- `/home/benjello/projets/precis-socio-fiscal-tunisie/precis/fr/compensation/_electricite_gaz.qmd`
- `/home/benjello/projets/precis-socio-fiscal-tunisie/precis/fr/compensation/_carburants.qmd` (lieu unique du circuit et de 2015)
- `/home/benjello/projets/precis-socio-fiscal-tunisie/docs/recherches.yml` (champs `ou:` vers `#sec-compensation-eg-autorite` et `#sec-compensation-eg-grilles`)
- `/home/benjello/projets/precis-socio-fiscal-tunisie/precis/fr/compensation/_incidence.qmd` (liens entrants vers `-grilles-steg` et `-rapprochement`)
- `/home/benjello/projets/precis-socio-fiscal-tunisie/precis/_seriescache/compensation-carburants-beneficiaires.csv`
- Les notes : `docs/notes/compensation-tarifs-electricite-gaz.md`, `compensation-tarifs-1993-2004.md`, `compensation-tarifs-mt-ht-gaz.md`, `compensation-rapport-2014.md`, `compensation-rupture-2015.md`, `compensation.md`

## Décisions du propriétaire (17 octobre 2026)

Les cinq recommandations du § 7 sont acceptées telles quelles :
1. Le 1er mai 2014 porte une grande réforme, avec sa réserve au premier plan ; 2006, 2018 et 2022 restent des étapes, 2019 un ajustement.
2. « Qui fixe les tarifs » n'a plus de section propre : mise en place, réforme de 1991-1992, état du droit.
3. Tous les tableaux et identifiants sont gardés ; `-ajustements` devient le registre des règles de base ; ses lignes 1978-1982 passent en R0 ; relais et rapport extérieur restent séparés.
4. Les tableaux du coût et du prix restent visibles tant qu'aucune figure ne les remplace.
5. Pas d'ajout tiré des notes (partage ménages / autres abonnés en 2014, gaz de 1982, cimentiers en 2016) : inscrits au backlog.

## Corrections apportées par la note documentaire (17 octobre 2026)

Voir `compensation-electricite-gaz-objets-des-reformes.md`, § 0 et § 6. Pour le rédacteur :
- 1984 : la tranche économique est **maintenue à 61 millimes** (prix unique de 1982), la tranche normale passe à 70 ; le titre de la section devient « 1984 : les cinquante premiers kilowattheures des petits abonnés gardent leur prix » ; la réserve sur la première apparition est levée (arrêtés de 1980-1981 lus, sans tranche) ;
- 1991-1992 : la date de la rupture est le 1er janvier 1992 (loi n° 91-64, art. 62) ; le tableau A en vigueur est celui du décret n° 95-1142 (n° 9) ; le décret n° 2015-307 ne touche pas au tableau A ;
- 2014 : phrase d'objet dans le rapport de contrôle (p. 75, exposé de l'administration) ; dates 1er janvier et 1er juin (rapport) contre 1er mai (grille), à exposer sans trancher ;
- 2015 : « décision (قرار) du 8 octobre 1993 », nature de l'acte non établie ;
- taxe du Fonds de transition énergétique : LF 2019, art. 68 (1 millime), LF 2024, art. 51 (5 millimes) ; affichée dans les grilles depuis 2022.
