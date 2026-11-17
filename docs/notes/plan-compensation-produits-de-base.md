# Fiche de plan : « Les produits de base » (`precis/fr/compensation/_produits_base.qmd`, chapitre nouveau)

Architecte, 17 novembre 2026. Branche `compensation/produits-de-base`. Aucun `.qmd` écrit, rien
commité. Le rôle prévoit `docs/notes/compensation-produits-base-plan-architecte.md` ; le nom
retenu ici est celui que l'appelant a demandé.

**Statut.** Ce chapitre n'a pas encore de note documentaire propre. Le plan est construit sur les
matériaux que le précis porte déjà, dans les chapitres du volume, dans les registres des offices
du volume « Les entreprises publiques » et dans les notes `compensation*.md`. Il fixe la
charpente et désigne ce qui manque. Une grande réforme ne figure ici que si un article a été lu.
Pour tout le reste, le documentaliste doit passer d'abord (§ 9).

**Dépendance.** La mise en place s'appuie sur des faits de 1941, 1945, 1947 et 1975 qui viennent
de `docs/notes/compensation-textes-fondateurs-2026-11-17.md`. Cette note appartient à la PR #810
(« Compensation : la Caisse de compensation créée en 1941, refondue en 1945 ; fonctionnement de
la Caisse générale »), n'est pas fusionnée et n'est pas dans ce worktree. Les faits concernés sont
signalés par **[#810]**. Ils ne s'écrivent qu'après la fusion de cette PR.

**Degrés de lecture.** **[JO]** : article lu au *Journal officiel*, à l'image ou dans une couche
texte relue. **[JO-EP]** : article lu, avec une ligne au registre des offices
(`precis/fr/entreprises_publiques/_offices.qmd`). **[intitulé]** : seul l'intitulé du texte est
connu. **[visa]** : le texte n'est connu que par les visas d'autres textes. **[BCT]**, **[MF]** :
chiffre ou constat d'un rapport annuel de la Banque centrale ou d'un document du ministère des
Finances. **[ext]** : rapport extérieur (Banque mondiale, FMI) ou compilation extérieure.

Notes citées : **NC** = `compensation.md` ; **NA70** = `compensation-avant-1970-et-plans.md` ;
**NEG** = `compensation-electricite-gaz-objets-des-reformes.md` (loi n° 91-64, décret n° 91-1996) ;
**NI** = `compensation-etudes-incidence-calculs.md` ; **NTF** = `compensation-textes-fondateurs-2026-11-17.md` [#810] ;
**AGR** = `agriculture-plan-livre.md`.

---

## Résumé

- **Place et nom.** Fichier `_produits_base.qmd`, identifiant de chapitre
  `sec-compensation-produits-base`, préfixe des sections `sec-compensation-pb-`. Je recommande de
  le placer juste avant `_carburants.qmd`, pour suivre l'ordre dans lequel le volume énumère partout
  ses postes et l'ordre historique : les produits de base sont le premier poste de la Caisse jusqu'en
  2010. `chantier-decoupage-livres.md` le range après le transport, sans motiver cet ordre. La
  décision revient au propriétaire (P2).
- **Ce qui constitue le dispositif.** Je recommande la lecture (a) :
  - les règles qui en font partie sont la liste des produits à prix administré, l'autorité qui fixe
    ces prix et le paiement par la Caisse de l'écart entre le coût de l'opérateur et le prix de vente ;
  - chaque produit a sa section, et les céréales viennent en premier ;
  - la lecture (b), où la filière des céréales forme le dispositif à elle seule, est exposée au § 2.
- **Les grandes réformes.** Deux seulement reposent sur un article lu :
  - **1984** : la loi de finances supprime la compensation des céréales et dérivés, et la loi de
    finances complémentaire de mars abroge l'article ;
  - **1991-1992** : la liberté des prix devient la règle, et les produits de première nécessité en
    sont exclus par une liste fixée par décret.

  La mise en place (1970-1975) les précède. La période qui suit 1992 n'a aucune grande réforme
  sourcée : le ciblage, les transferts de substitution et les entrées et sorties de produits ne sont
  connus par aucun texte lu. Le seuil de trois réformes n'est pas atteint. Je ne l'atteins pas en
  élargissant le critère ; la question est posée au propriétaire (P9).
- **Ce qui est déplacé.** Quatre éléments :
  - de `_institution.qmd`, la sous-section « Les charges par produit », avec son tableau et sa
    figure ;
  - de `_depense.qmd`, la sous-section « Les produits de base par produit, selon le ministère » ;
  - de `_reformes.qmd`, le premier alinéa de la section sur 1984 ;
  - de `_institution.qmd`, la moitié d'un TODO.

  Rien n'est déplacé dans les sections « Avant 1970 » et « 1970-1971 », qui relèvent de la PR #810.
  Le registre des décrets de campagne des céréales reste aux entreprises publiques : le propriétaire
  l'a décidé le 2 novembre 2026, en notant « à reconsidérer » (P3).
- **Figures.** Trois sont faisables avec des séries déjà construites : les charges de la Caisse par
  produit, le poste « produits de base » de 2003 à 2026, et les prix de campagne de 2010 à 2026. Les
  autres attendent un travail de données ou un texte lu.

---

## 1. Place dans le livre

| Point | Proposition |
|---|---|
| Fichier | `precis/fr/compensation/_produits_base.qmd` (convention `_<objet>.qmd` du volume) |
| Identifiant | `# Les produits de base {#sec-compensation-produits-base}` ; sections `sec-compensation-pb-*` ; lignes de registre `r-comp-pb-*` |
| Type | chapitre de dispositif (épine chronologique et fiches), sur le gabarit de `_transport.qmd` et `_electricite_gaz.qmd`, qui sont déjà convertis ; `_carburants.qmd`, pas encore converti, ne sert que pour l'idée d'une section « Le circuit » |
| Ordre | recommandé : `index`, `_institution`, `_reformes`, **`_produits_base`**, `_carburants`, `_electricite_gaz`, `_transport`, `_depense`, `_exterieurs`, `_incidence` ; alternative de `chantier-decoupage-livres.md` : après `_transport` |
| Taille visée | 6 000 à 9 000 mots, dont environ 900 déplacés |
| Câblage | `_quarto.yml` (liste `chapters:`), puis `uv run python scripts/arabe_cablage.py`, qui pose la page-relais arabe ; liste du plan de `index.qmd`, à renuméroter |

## 2. Ce qui constitue le dispositif, et ce qui l'aménage

**Lecture (a), recommandée.** Le dispositif est le même pour tous les produits :

- une liste de produits « de première nécessité » soustraits à la liberté des prix ;
- une autorité qui fixe ces prix ;
- un opérateur, le plus souvent un office public, qui achète ou importe et revend au prix fixé ;
- la Caisse générale, qui paie à cet opérateur l'écart entre son coût et le prix de vente.

Sans ces quatre éléments, il n'y a pas de compensation des produits de base. C'est ce que la
section « Les grandes réformes » suit.

Chaque produit est un aménagement de ce dispositif : un opérateur, un circuit, un prix, une
évolution propre. Il a sa section :

1. les céréales et dérivés ;
2. les huiles végétales ;
3. le sucre ;
4. le lait ;
5. les autres produits ;
6. le ciblage, s'il est documenté.

Le prix à la production des céréales relève de la section des céréales.

Pourquoi (a). Les deux réformes qui passent la règle s'appliquent à toute la liste :

- la loi de 1970 crée la Caisse et les régimes de prix ;
- la loi de 1991 libère les prix et exclut la liste.

La réforme de 1984 vise les céréales, mais elle engage la Caisse entière : les céréales sont alors
69 % de ses dépenses, et la loi de finances complémentaire reconstitue les ressources de toute la
Caisse.

**Lecture (b).** Le dispositif est la filière des céréales : prix à la production, prix de
rétrocession, prix des dérivés. Elle pèse de 61 à 83 % des charges aux six dates du tableau
(`tbl-compensation-charges-produits`). Dans cette lecture, l'épine suit les décrets de campagne,
et l'huile, le sucre, le lait et les autres produits sont les aménagements.

Ce qu'elle coûte : les décrets de campagne de 1970 à 2009 ne sont connus que par leurs visas.
L'épine serait vide avant 2010, et la loi de 1991 deviendrait un détail.

**Domiciles** (règle du § 4 des conventions) :

| Sujet | Domicile | Ce que l'autre endroit reçoit |
|---|---|---|
| Prix administrés des produits de base, à la consommation et à la production ; subvention par produit | ce chapitre | le livre « L'agriculture », un renvoi (déjà au tableau de voisinage de `precis/fr/agriculture/index.qmd`, l. 35) |
| Office des céréales, ONH, Office du commerce : statut, comptes, garanties, dettes croisées avec l'État | `entreprises_publiques/_offices.qmd` | ce chapitre : une phrase et un lien en tête de la section « Le circuit » et de chaque fiche |
| Registre des décrets de campagne des céréales, récoltes 2010-2026 (`tbl-ep-registre-oc-campagnes`) | `_offices.qmd` par décision du 2 novembre 2026, « à reconsidérer » | ce chapitre : un tableau court ou une figure tirés des mêmes lignes, et un lien ; P3 |
| Caisse générale : création, compte, ressources, prélèvements à l'importation, dotation | `_institution.qmd` | ce chapitre : des renvois |
| Prélèvements à l'importation au profit de la Caisse (poudre de lait, viandes, beurre, fruits) | `_institution.qmd` (`#sec-compensation-prelevements-importation`), parce que ce sont des ressources de la Caisse | la fiche du lait : une phrase et un renvoi. Autre lecture : ce sont des prix de péréquation par produit, à verser aux fiches. Je ne la retiens pas |
| Taxe sur le sucre de la loi de finances pour 2021 (art. 23) | fiscalité ; registre de l'Office du commerce (`r-ep-otc-2021`) | la fiche du sucre : une phrase et un lien |
| Engrais, aliments du bétail (maïs, tourteaux de soja) | le livre « L'agriculture », dès qu'il traite les intrants ; la compensation garde la trace historique dans les charges de la Caisse | une phrase et un renvoi croisé |
| Papier scolaire | ce chapitre (prix administré) | le livre « L'éducation » : une phrase et un lien, à poser |
| Études d'incidence alimentaire (INS, CRES et BAD, 2013) | `_incidence.qmd` (`#sec-compensation-incidence-alimentaire`) | ce chapitre : un renvoi dans la vue d'ensemble et dans la section du ciblage |
| Rapports extérieurs par produit (Banque mondiale 1977 et 1985, FMI 1996 et 2000) | `_exterieurs.qmd` | un renvoi |
| Transferts monétaires ciblés (PNAFN, AMEN social) | `prestations_sociales/_non_contributives.qmd` | un renvoi |

## 3. Le plan, section par section

Le texte visible se suffit à lui-même. Les mots « cœur », « épine » et « fiche » n'apparaissent
pas dans le chapitre.

### `# Les produits de base {#sec-compensation-produits-base}`

Chapeau de trois phrases.
- L'objet : les céréales et leurs dérivés, les huiles végétales, le sucre, le lait et quelques
  autres produits.
- Le mécanisme : un prix fixé par l'administration, un office qui achète et revend, la Caisse qui
  paie l'écart.
- Le poids : le premier poste de la Caisse jusqu'en 2010.

Renvois de tête :
- l'institution : `@sec-compensation-caisse` ;
- la dépense globale : `@sec-compensation-longue-periode` ;
- les opérateurs : `../entreprises_publiques/_offices.html#sec-ep-ge-oc`.

### `## Vue d'ensemble {#sec-compensation-pb-vue}`

**Ce qu'elle établit.**
- Ce que fait le dispositif.
- Les produits concernés, avec leur opérateur : céréales et Office des céréales ; huile végétale
  et ONH ; sucre et Office du commerce ; lait, opérateur non relevé (D8).
- Ce que la compensation de ces produits pèse :
  - charges de la Caisse en 1986, 2008 et 2011 ;
  - poste « produits de base » en 2003, 2008, 2022 et 2024, en millions de dinars et en part des
    dépenses de l'État.
- La part des céréales.

**Au premier plan.**
- La figure de longue période `fig-compensation-pb-poids`, décrite au § 8.
- Une frise : création des offices en 1962 ; Caisse générale en 1970-1971 ; passage à la
  subvention en 1974-1975 ; 1984 ; 1991-1992 ; décret-loi de 2025 sur l'autorité qui fixe les prix
  de campagne. Les entrées et sorties de produits, connues par la BCT, sont posées sur la frise en
  trait fin, avec la mention de leur source.
- Un tableau court des réformes, à quatre colonnes : la réforme et sa date ; ce que la loi
  cherche ; avant → après ; ce qui en découle.

**Replié.** Rien.

### `## La mise en place : la Caisse générale, les offices et le prix fixé, 1962-1975 {#sec-compensation-pb-mise-en-place .domicile-unique}`

**Ce qu'elle établit.**

*L'antécédent*, en deux ou trois phrases et un renvoi à `@sec-compensation-avant-1970`, qui n'est
pas recopiée :
- la caisse du Protectorat [#810] ;
- le fonds des farines et semoules de 1941, et la péréquation des céréales confiée en 1947 à la
  section tunisienne de l'Office national interprofessionnel des céréales, sur son budget propre
  [#810] ;
- de 1956 à 1964, des redevances sur les huiles de graines et le sucre importés : la caisse
  prélève, elle ne subventionne pas [JO, NA70] ;
- des indemnités et redevances compensatrices sur les stocks de blés, farines et semoules, qui
  égalisent les stocks à chaque changement de prix de campagne et ne sont pas des subventions
  [intitulé, NA70].

*Les opérateurs de 1962.* Les décrets-lois n° 62-10, 62-6 et 62-24 créent l'Office des céréales,
l'Office du commerce et l'Office national de l'huile [JO-EP].

*Les textes de 1970*, ce qui constitue la mise en place proprement dite :
- la loi n° 70-26, art. 2 et 3, qui pose les cinq régimes de prix et crée la Caisse générale
  [JO] ;
- le décret-loi n° 70-7, art. 2 et 12. L'Office des céréales reçoit le monopole des importations
  et exportations des céréales et produits dérivés et l'achat à la production ; prix à la
  production, rétrocession, prélèvements et taxes sont fixés pour chaque campagne par décret
  [JO-EP] ;
- le décret-loi n° 70-13 : l'ONH reçoit le monopole de l'importation des huiles végétales
  comestibles et de leur vente en gros [JO-EP] ;
- la loi de finances pour 1971, art. 48 : la Caisse devient un fonds spécial [JO].

*L'entrée en vigueur comme subvention*, en 1974-1975.
- La loi de finances pour 1975, art. 83, rend « évaluatives », à compter du 1er janvier 1974, les
  prévisions de dépenses de la Caisse [JO, #810].
- Le rapport de la BCT pour 1974 détaille les produits soutenus et qualifie la contribution du
  budget d'« intervention nouvelle du budget de l'État » [BCT]. Ce paragraphe reste dans
  `_institution` ; ce chapitre y renvoie, il ne le recopie pas.
- La Banque mondiale date de 1975 les prix fixes subventionnés des céréales et des huiles. C'est
  une lecture extérieure, citée comme telle avec un renvoi à `@sec-compensation-bm-1985`.

**Contexte.** Les mots des sources de l'époque sont à relever (D3). À défaut, la phrase de
contexte se borne à la hausse des dépenses (27,3 → 49,2 MD), sans interprétation.

**Au premier plan.** Un paragraphe sur l'antécédent ; trois puces : les opérateurs, les prix,
la Caisse ; l'entrée en vigueur.

**Replié.** `:::: {.chronologie-repliable titre="La mise en place des produits de base : textes de 1962 à 1975, avec l'article et la page de chacun"}`.
Lignes : 62-10, 62-6, 62-24, 70-26, 70-7, 70-13, LF 1971 art. 48, LF 1975 art. 83 [#810].

Les lignes 62-* et 70-7/70-13 existent déjà au registre des offices. Comme le contrôle des sections
`.domicile-unique` impose que toute ancre `#r-` soit dans le même fichier, il faut décider entre :
- des lignes propres à ce chapitre, qui recopient la référence mais pas la prose ;
- des liens vers `../entreprises_publiques/_offices.html#r-ep-oc-1970`, sans infobulle.

Je recommande des lignes propres pour 70-26, 70-7 (art. 2 et 12) et 70-13, qui portent sur les
prix, et des liens vers le registre des offices pour les textes de statut (62-*).

### `## Les grandes réformes {#sec-compensation-pb-reformes .domicile-unique}`

Un paragraphe d'entrée, puis une sous-section par réforme. Chacune suit le même ordre : le
contexte (les sources de l'époque) ; ce que la loi cherche (ses mots) ; avant → après ; ce qui en
découle. Les intervalles entre réformes tiennent en une phrase qui renvoie aux registres.

#### `### 1984 : la suppression de la compensation des céréales, votée puis abrogée {#sec-compensation-pb-1984}`

Établit :
- ce que la loi cherche : « la suppression de la compensation des céréales et dérivés », et des
  « mesures d'accompagnement » financées en 1984 sur les disponibilités de la Caisse (LF 1984,
  art. 87 [JO]) ;
- l'abrogation de l'article par la loi de finances complémentaire du 21 mars 1984, art. 27 [JO] ;
- le poids des céréales : 103,5 MD sur 149,3 MD de dépenses du fonds en 1983, puis 159,2 MD sur
  245,8 MD en 1984 [BCT 1984, p. 154]. Ce texte vient de `_reformes.qmd`, l. 38.

La reconstitution des ressources de la Caisse — 28 % de la taxe sur les alcools, 8 MD de la
contribution exceptionnelle de solidarité, 98 MD de subvention — reste à `@sec-compensation-1984`.
Elle y est annoncée en une phrase.

Contexte :
- les mouvements de janvier 1984 n'ont aucune source primaire (backlog, NC § 6, point 13) ;
- les prix du pain et de la semoule fixés fin 1983, et leur retour en janvier 1984, ne sont
  connus par aucun texte lu (D5).

Le texte dit les deux articles et ce qu'ils changent. Il ne dit rien de plus tant que D5 n'est pas
levée.

#### `### 1991-1992 : la liberté des prix, sauf les produits de première nécessité {#sec-compensation-pb-1991}`

Établit :
- ce que la loi cherche, dans ses mots : « définir les dispositions régissant la liberté des
  prix », « les prix … sont librement déterminés par le jeu de la concurrence » ; en sont exclus
  « les biens, produits et services de première nécessité », dont la liste est fixée par décret
  (loi n° 91-64, art. 1 à 3 [JO, NEG § 2.1]) ;
- l'effet au 1er janvier 1992, et l'abrogation de la loi n° 70-26 (art. 62 [JO]) ;
- la liste : décret n° 91-1996, tableau A (homologation à tous les stades), remplacé par le décret
  n° 95-1142 [JO pour les seuls points 8 et 9, NEG § 2.2]. Les produits alimentaires de la liste ne
  sont pas relevés (D6). Sans eux, la section ne peut pas dire quels produits de base restent
  administrés ;
- ce qui précède : l'arrêté du 30 août 1989, qui arrête la liste des produits de base confiés à
  l'Office du commerce (sucre, café, thé, riz…) [JO-EP]. Il se place ici comme antécédent, ou dans
  la fiche du sucre (P5).

Dans les années qui suivent, des produits sortent du champ (BCT ; Banque mondiale 1995) :
maïs en 1992, tourteaux de soja en 1993, certains engrais et le sucre produit localement en 1999.
Ces sorties sont rapportées en une phrase d'intervalle, avec leurs sources, et ne sont pas
présentées comme des réformes.

En 1994, l'ONH perd l'exclusivité de l'importation des huiles végétales (loi n° 94-37 [JO-EP]).
L'épine n'en dit qu'une proposition, avec un renvoi à la fiche des huiles.

#### Après 1992 : pas de grande réforme sourcée

Une phrase d'intervalle, sans sous-section :
- le champ change encore — sortie du lait en 2008, extension de 2011 [BCT ; MF 2011, p. 30] ;
- en 2015, la loi n° 2015-36 reprend l'exclusion de la liberté des prix et maintient les textes
  d'application de 1991 (art. 3 et 78 [JO, NEG]) : c'est un ajustement ;
- en 2025, l'autorité qui fixe les prix de campagne des céréales change (décret-loi n° 2025-2) :
  c'est un ajustement, raconté dans la fiche des céréales.

Si le documentaliste trouve un texte sur le ciblage ou les transferts de substitution, avec un
article lu (D9), une troisième réforme vient ici.

**Replié, en fin de section.** `:::: {.chronologie-repliable titre="Les textes des produits de base, 1962-2026 : liste des produits, autorité qui fixe les prix, financement, avec l'article et la page de chaque texte"}`.
C'est le registre des règles communes, complet, avec la colonne « Portée » (§ 6, registre R0).

### `## L'état du droit {#sec-compensation-pb-etat-du-droit .domicile-unique}`

**Ce qui est établi** pour une date donnée :
- l'autorité qui fixe les prix de campagne des céréales : arrêté conjoint des ministres des
  Finances et de l'Agriculture depuis le décret-loi n° 2025-2 ;
- les prix de base de la récolte 2026 : blé dur 100 D/q, blé tendre 80 D/q ; prix normaux de
  rétrocession 156,456 et 124,671 D/q (arrêté du 24 juillet 2026 [JO-EP]) ;
- la règle générale de la loi n° 2015-36, art. 3.

**Ce qui n'est pas établi** :
- la liste en vigueur des produits alimentaires exclus de la liberté des prix (D6) ;
- les prix de vente au consommateur (D10) ;
- l'autorité qui les fixe (D10).

Ces points ne s'écrivent pas. Ils restent en TODO. La section ne porte une date que pour ce qui
est établi : « au 25 juillet 2026 » pour les prix de campagne.

**Colonne « population couverte »** (§ 4 des conventions) : le dispositif n'a pas de condition
d'accès, et la population couverte est celle des consommateurs. Le complément et la série
n'existent pas. Une phrase le dit, avec un renvoi à l'étude d'incidence.

**Replié.** Rien : l'état du droit ne se replie pas.

### `## Le circuit : qui achète, qui vend, qui paie {#sec-compensation-pb-circuit .domicile-unique}`

Une section transversale, sur le modèle de `#sec-compensation-circuit` des carburants.

**Ce qu'elle établit.**
- Les offices et leur rôle pour chaque produit.
- Le chemin de l'argent. La Caisse est d'abord un fonds spécial, puis une dotation du budget ; le
  poste « produits de base » apparaît en 2003. L'écart entre ce poste et les transferts du budget
  à l'Office des céréales et à l'ONH (191 à 307 MD par an, 2018-2023) est donné sans attribution
  (D12).
- Les arriérés. Les prêts du Trésor de 1981 et 1992 remboursent l'Office des céréales et l'ONH ;
  ils sont exposés dans `_institution` (l. 287) et repris ici par un renvoi. La compensation des
  créances de 2023 (décret n° 2023-35) a son domicile aux entreprises publiques, avec un renvoi.

**Au premier plan.** Le tableau court `tbl-compensation-pb-circuit`, à quatre colonnes : produit,
opérateur, ce que l'opérateur fait, texte. Puis deux paragraphes.

**Replié.** Rien de propre. Les transferts par établissement de 2017 à 2023 vont en tableau court
s'ils tiennent en six lignes, sinon dans un bloc replié (« Transferts du budget à l'Office des
céréales et à l'ONH, 2017-2023 »).

### `## Les céréales et leurs dérivés {#sec-compensation-pb-cereales .domicile-unique}`

**Situation.** Née avec la mise en place ; touchée par la réforme de 1984.

**Le mécanisme.**
- L'Office achète la récolte au prix de base à la production et importe le reste.
- Il rétrocède aux minoteries au prix normal de rétrocession.
- La prime de compensation couvre l'écart. L'unité est à préciser : par quintal, ou en montant
  global.
- Les dérivés : farine, semoule, pain, pâtes et couscous.

Les notions sont à soumettre au terminologue : « prix de base à la production », « prix normal de
rétrocession », « prime de compensation ».

**Évolution.**
- 2010-2026 : les prix de campagne, tirés du registre des offices.
- Avant 2010 : un TODO (D2).
- Les pâtes et le couscous entrent dans le champ vers 2011 (D14).

**Ruptures propres** (§ 5) : 1970 (prix de campagne fixés par décret) et, éventuellement, 2022 (P6).
L'ajustement de 2025 se raconte ici.

**Au premier plan.**
- La figure `fig-compensation-pb-prix-campagne` : prix de base et prix normaux de rétrocession du
  blé dur et du blé tendre, récoltes 2010-2026.
- Les charges des céréales dans la Caisse et dans le poste budgétaire : une phrase et un renvoi à
  la longue période.

**Replié.** Si P3 retient le déplacement, le registre des campagnes vient ici, entier :
`:::: {.chronologie-repliable titre="Les décrets de campagne des céréales, récoltes 2010-2026 : prix de base à la production, prix normaux de rétrocession, prime de compensation, avec la page de chaque texte"}`.
Sinon, le chapitre porte un lien vers `../entreprises_publiques/_offices.html#tbl-ep-registre-oc-campagnes`.

### `## Les huiles végétales {#sec-compensation-pb-huiles .domicile-unique}`

**Situation.** Née avec la mise en place (décret-loi n° 70-13).

**Antécédent.**
- La redevance de 1956 sur les huiles de graines (renvoi).
- La taxe sur l'huile d'olive exportée affectée à la Caisse en 1974 (décret n° 74-876
  [intitulé, NA70]). Elle relève de ce chapitre si le texte est lu.

**Mécanisme.** L'ONH importe et vend l'huile végétale subventionnée « pour le compte de
l'État », sur le titre III de son budget (décret n° 2000-2579 [JO-EP]).

**Évolution.**
- 1994 : la fin de l'exclusivité (loi n° 94-37 [JO-EP]), rupture propre à la fiche ou étape (P7).
- Les quantités subventionnées de 2021 à 2023 (RAP du Commerce ; unités à vérifier, D16).

**Premier plan.** Trois puces et la ligne « huiles » des charges.

**Replié.** Le registre des huiles végétales (R2).

### `## Le sucre {#sec-compensation-pb-sucre .domicile-unique}`

**Antécédent.** La redevance sur le sucre importé, de 1956 à 1964, suspendue en 1964 (renvoi).

**Opérateur.** L'Office du commerce. L'arrêté du 30 août 1989 range le sucre roux et le sucre
blanc parmi ses produits de base [JO-EP].

**Évolution.**
- 15 MD en 1974, première ligne des produits soutenus [BCT].
- La sortie du sucre produit localement en 1999 [BCT].
- 10,8 MD en 2011 [MF].

**Renvoi.** La taxe de 2021 sur le sucre, qui a son domicile en fiscalité.

**Premier plan.** Deux paragraphes. **Replié.** Le registre (R3), court : il peut rester visible
s'il a moins de six lignes.

### `## Le lait {#sec-compensation-pb-lait .domicile-unique}`

**Chiffres.** Charges de 9,2 MD en 1986, 25,7 MD en 1996, 2,8 MD en 2008 et 23,1 MD en 2011
[BCT, MF]. Sortie en 2008 et retour en 2011, d'après les sources secondaires.

**Renvoi en tête.** Les prélèvements à l'importation sur la poudre de lait, ressource de la
Caisse (`@sec-compensation-prelevements-importation`).

**Matière manquante.** L'opérateur et les textes de prix ne sont pas relevés (D8). La section
reste courte, avec un TODO.

### `## Les autres produits : papier scolaire, concentré de tomate, et les produits sortis du champ {#sec-compensation-pb-autres .domicile-unique}`

**Le papier scolaire.**
- Charges de 1996 à 2011 [BCT].
- 17 MD pris en charge par le Centre national pédagogique en 1995 [BCT].
- Renvoi vers le livre de l'éducation.

**Le double concentré de tomate.** 9,6 MD en 2011 [BCT].

**Les pâtes et le couscous.** S'ils ne vont pas dans la fiche des céréales, ils viennent ici :
4,2 MD en 2011.

**Les produits sortis du champ.** La viande en 1974 ; les engrais (10 MD en 1974, 16,9 MD en
1986, fin en 1999) ; le maïs et les tourteaux de soja (1992-1993). Ils sont exposés en un tableau
court avec leurs sources, qui sont toutes de seconde main, et un renvoi à l'agriculture pour les
intrants.

**Replié.** Rien. **Point de vigilance.** Aucune de ces lignes ne repose sur un texte lu ; la
section le reflète par des sources budgétaires, pas par des articles.

### `## Le ciblage et les transferts de substitution {#sec-compensation-pb-ciblage}` (conditionnelle)

**Objet non relevé.** Aucun texte lu (backlog, « Hors texte, faute de source » ; NC § 6, point 8).

Si D9 ne trouve rien, la section se réduit à deux phrases :
- le renvoi à l'étude d'incidence de 2010 (`@sec-compensation-incidence-alimentaire`) ;
- le renvoi aux transferts monétaires ciblés des prestations sociales.

Elle n'emploie pas « auto-ciblage » tant qu'aucune source ne porte le terme. L'ancre du glossaire
`#g-auto-ciblage` reste inemployée.

Les rapports extérieurs de 1993 et 1995 sur l'auto-ciblage restent dans `_exterieurs` ou dans
`_incidence` (consigne du 7 octobre 2026 : ne pas leur chercher de place nouvelle).

### `## La longue période {#sec-compensation-pb-longue-periode}`

Le budgétaire seul, en entonnoir. Les figures et tableaux sont détaillés au § 8.

#### `### Les charges de la Caisse par produit, 1985-2011`

Déplacée de `_institution.qmd`, l. 170-210. Les identifiants sont gardés :
`tbl-compensation-charges-produits` et `fig-compensation-par-produit`.

Les marques de rupture de la figure sont déjà posées (1991, 1992-1994, 1999, 2008, 2011). On y
ajoute 1992, effet de la loi n° 91-64, si P5 retient 1991-1992 comme grande réforme.

Le tableau des six dates est court et la figure en dépend : il ne se replie pas.

#### `### Le poste « produits de base » du budget, 2003-2026`

Nouvelle figure `fig-compensation-pb-poste`, décrite au § 8 ; ou un renvoi à `fig-compensation-par-poste`
si le propriétaire juge le doublon inutile (P10).

#### `### Le détail par produit selon le ministère des Finances, 2009-2011`

Déplacée de `_depense.qmd`, l. 197-213, identifiant gardé (`tbl-compensation-produits-2009-2011`),
avec la phrase sur la non-coïncidence avec les charges de la Caisse.

#### `### Ce que reçoivent l'Office des céréales et l'ONH, 2017-2023`

Tableau court, ou renvoi à `../entreprises_publiques/_transferts.html` si le tableau y existe déjà
(`tbl-ep-transferts-compensation`). Je recommande le renvoi avec deux chiffres.

Les rapports extérieurs (Banque mondiale 1970-1984 par produit ; FMI 1988-1998) n'entrent pas
ici. Ils restent dans `_exterieurs`, avec un renvoi.

### `## Ce qu'en dit l'économie {#sec-compensation-pb-economie}`

Une page au plus, sur le gabarit fixe du § 4. Elle est tirée de
`docs/notes/eco-compensation-produits-de-base.md`, **à produire par l'économiste**.
`eco-compensation-energie.md` ne couvre pas l'alimentaire.

Questions à couvrir :
- l'incidence des subventions alimentaires généralisées et l'auto-ciblage par la qualité ;
- les fuites hors ménages ;
- les effets sur les filières, céréales en tête ;
- le passage des subventions aux transferts monétaires.

C'est la première section de ce type dans le volume : la retenir ici implique de la prévoir aussi
pour les autres chapitres de dispositif (backlog, § 11).

## 4. Les grandes réformes : sources, avant → après, ce que la loi cherche

| Réforme | Textes et articles (lecture) | Contexte (sources de l'époque) | Ce que la loi cherche (ses mots) | Avant → après | Dispositifs qui y naissent |
|---|---|---|---|---|---|
| Mise en place, 1970-1975 | loi n° 70-26, art. 2, 3 [JO] ; DL 70-7, art. 2, 12 [JO-EP] ; DL 70-13 [JO-EP] ; LF 1971, art. 48 [JO] ; LF 1975, art. 83 [JO, #810] | BCT 1974 : « intervention nouvelle du budget de l'État » ; autres mots à relever (D3) | « agir sur les prix des marchandises, produits et services de première nécessité notamment au moyen de subvention et de péréquation » (70-26, art. 3) | un compte de péréquation qui prélève et reverse au budget → une Caisse générale, des offices à monopole et des prix fixés par campagne ; en 1974-1975, une subvention dont la dépense n'est plus plafonnée | céréales (Office), huiles végétales (ONH) ; sucre, lait, engrais et viande à des dates non sourcées |
| 1984 | LF 1984 (loi n° 83-113), art. 87 [JO] ; LFC 1984 (loi n° 84-2), art. 27 [JO] | à relever (D5) ; janvier 1984 sans source primaire | « suppression de la compensation des céréales et dérivés » ; « mesures d'accompagnement » | 103,5 MD de compensation des céréales en 1983 → suppression votée au 1er janvier 1984 → article abrogé le 21 mars 1984 ; 159,2 MD en 1984 | aucun |
| 1991-1992 | loi n° 91-64, art. 1, 2, 3, 62 [JO] ; décret n° 91-1996 et décret n° 95-1142, tableau A [JO, points 8-9 seulement] ; antécédent : arrêté du 30 août 1989 [JO-EP] | à relever (D6) | « définir les dispositions régissant la liberté des prix » (art. 1) ; exclusion des « biens, produits et services de première nécessité » (art. 3) | des prix fixés sous cinq régimes (loi n° 70-26) → une liberté des prix dont la liste des produits de première nécessité est exclue | aucun ; le champ se resserre ensuite (sources de seconde main) |

Candidats refusés comme grandes réformes, et pourquoi :
- **1974-1975, le passage à la subvention** : pas de texte de prix lu. Ce passage est intégré à la
  mise en place, comme entrée en vigueur.
- **2007-2008, la hausse des charges** : un effet de volume, pas un texte.
- **2008, la sortie du lait, et 2011, l'extension** : connues seulement par la BCT et le rapport
  du ministère des Finances de 2011.
- **2015, la loi n° 2015-36** : elle reprend la règle de 1991 ; c'est un ajustement.
- **2022, la campagne des céréales** : c'est un relèvement de niveau, une étape de la section des
  céréales (P6).
- **2025, le décret-loi n° 2025-2** : il change l'autorité ; c'est un ajustement.
- **Ciblage, 2013-2026** : aucun texte lu (D9).

## 5. Ruptures propres aux sections de produits

| Section | Rupture ou étape | Texte (lecture) | Classement proposé |
|---|---|---|---|
| Céréales | 1970 : monopole, achat à la production, prix de campagne par décret | DL 70-7, art. 2 et 12 [JO-EP] | rupture (partagée avec la mise en place ; racontée dans la mise en place, la section détaille le mécanisme) |
| Céréales | récolte 2022 : prix de base de 65 à 90 D/q (blé dur) et de 50 à 70 D/q (blé tendre) | décret n° 2022-581 [JO-EP] | étape. Le registre des offices dit « rupture » : désaccord à trancher (P6) |
| Céréales | 2025 : arrêté conjoint au lieu du décret | DL 2025-2 [JO-EP] | ajustement |
| Céréales | récoltes 2010-2021, 2023-2026 | décrets de campagne [JO-EP] | étapes et ajustements, comme au registre des offices |
| Huiles | 1994 : fin de l'exclusivité de l'ONH | loi n° 94-37, décret n° 94-1166 [JO-EP] | rupture propre à la fiche (registre des offices : « rupture ») ou étape (P7) |
| Huiles | 2000 : huile végétale subventionnée pour le compte de l'État, titre III du budget de l'ONH | décret n° 2000-2579 [JO-EP] | étape de 1970 |
| Sucre | 1989 : le sucre parmi les produits de base de l'Office du commerce | arrêté du 30 août 1989 [JO-EP] | étape (antécédent de 1991-1992) |
| Sucre | 2021 : taxe sur le sucre | LF 2021, art. 23 [JO-EP] | hors sujet ici (fiscalité) ; une phrase |
| Lait | prélèvements sur la poudre, 1990-2015 | décrets n° 90-1194 à 2015-50 [JO] | hors de la section (ressource de la Caisse, `_institution`) ; renvoi |

## 6. Classement des textes, par registre

R0, les règles communes (bloc replié de « Les grandes réformes ») :

| Texte | Lecture | Portée |
|---|---|---|
| décrets du 5 août 1941, du 28 juin 1945 et du 26 juin 1947 (art. 3) | [JO arabe, #810] | antécédent ; renvoi à `_institution`, pas de ligne propre |
| DL 62-10, 62-6, 62-24 (1962) | [JO-EP] | antécédent (opérateurs) ; lien vers le registre des offices |
| loi n° 70-26, art. 2, 3 et 41 | [JO] | rupture (mise en place) |
| DL 70-7, art. 2 et 12 | [JO-EP] | rupture (mise en place) |
| DL 70-13 | [JO-EP] | rupture (mise en place) |
| décret n° 70-543 (régimes de prix) | [intitulé] | à classer après lecture (D1) ; aucune rupture |
| LF 1971, art. 48 | [JO] | étape de la mise en place (forme budgétaire) ; domicile `_institution` |
| LF 1975, art. 83 | [JO, #810] | étape de la mise en place (entrée en vigueur comme subvention) |
| LF 1984, art. 87 | [JO] | rupture (1984) |
| LFC 1984, art. 27 | [JO] | rupture (1984), abrogation |
| LFC 1984, art. 6, 28, 29 ; décret n° 84-259 | [JO] | hors sujet ici (ressources de la Caisse) ; domicile `_reformes` / `_institution` |
| LF 1981, art. 58 ; LF 1992, art. 77 (prêts du Trésor pour l'Office des céréales et l'ONH) | [JO] | ajustement (financement des arriérés) ; domicile `_institution`, renvoi |
| arrêté du 30 août 1989 | [JO-EP] | étape (antécédent de 1991-1992) |
| loi n° 91-64, art. 1-3, 62 | [JO] | rupture (1991-1992) |
| décret n° 91-1996 ; rétablissements de 1992 ; décret n° 93-59 | [intitulé] pour les rétablissements et 93-59 | étape de 1991-1992 |
| décret n° 95-1142, tableau A | [JO, points 8-9 seulement] | étape de 1991-1992 (liste) |
| décret n° 2015-307 | [JO] | ajustement (délai de l'homologation) |
| loi n° 2015-36, art. 3 et 78 | [JO] | ajustement (reprise de la règle de 1991) |
| décret n° 2002-2145 ; décret n° 2005-2934 ; décrets n° 2001-2965 et 2001-2966 | [intitulé ou visa, #810] | hors sujet sauf « qui décide » : organisation administrative ; ajustement |
| DL 2025-2 | [JO-EP] | ajustement (autorité des prix de campagne) |

R1, les céréales : les lignes du registre des campagnes de 2010 à 2026, avec le classement du
registre des offices, sauf 2022 (P6). Les décrets de campagne 70-261, 71-253 et 72-244 [visa,
#810] n'ont pas de ligne tant qu'ils ne sont pas lus (D2).

R2, les huiles : DL 70-13, loi n° 94-37, décret n° 94-1166, arrêté du 8 janvier 1996 (collecte
de l'huile d'olive : hors sujet, c'est un soutien au producteur oléicole, P8), décret
n° 2000-2579, loi n° 2006-52 (garantie d'un prêt pour importer des huiles végétales : étape, avec
un renvoi aux entreprises publiques). Décret n° 74-876 [intitulé] : à lire.

R3, le sucre : arrêtés de 1956 et décret n° 58-163 (antécédent, renvoi) ; arrêté du 30 août 1989 ;
LF 2021, art. 23 (renvoi).

Textes connus par leur seul intitulé, ou non relus : décret n° 70-543 ; décret n° 74-876 ;
décret n° 93-59 ; rétablissements du décret n° 91-1996 de 1992 ; décrets n° 67-407 à 67-410 et
68-279 (stocks de blés) ; décrets de campagne de 1970 à 2009. Aucun ne porte une rupture.

## 7. Registre de destination (ce qui change dans les autres fichiers)

| Fichier, lignes | Élément | Destination |
|---|---|---|
| `_institution.qmd`, l. 5-63 (« Avant 1970 ») et 65-79 (« 1970-1971 ») | toute la section, y compris le paragraphe « Trois faits » de 1974 | **en place** (PR #810). Ce chapitre y renvoie. |
| `_institution.qmd`, l. 83-90 (« Comment la Caisse fonctionne ») | liste des charges par produit | en place ; une proposition de renvoi vers `@sec-compensation-produits-base` est ajoutée |
| `_institution.qmd`, l. 92-168 | `tbl-compensation-compte-caisse`, `fig-compensation-compte-caisse` | en place |
| `_institution.qmd`, l. 170-210 (« Les charges par produit ») | alinéa, `tbl-compensation-charges-produits`, `fig-compensation-par-produit` | **déplacé** vers `#sec-compensation-pb-longue-periode`, identifiants gardés. Il reste en place une phrase (« Les charges par produit sont exposées au chapitre des produits de base ») et un renvoi. Les renvois `@` de `_depense.qmd`, l. 102 et 213, restent valides dans le livre. |
| `_institution.qmd`, l. 212-284 (« Les recettes propres ») | tableaux et figure des recettes | en place |
| `_institution.qmd`, l. 285 | TODO « produit annuel de la redevance… Opérateurs… entrées et sorties de produits » | **scindé** : la moitié sur la redevance reste ; la moitié sur les opérateurs et les entrées et sorties de produits va à `#sec-compensation-pb-circuit`, réécrite avec les points D8, D12 et D14 |
| `_institution.qmd`, l. 287 | prêts du Trésor de 1981 et 1992 pour l'Office des céréales et l'ONH | en place ; renvoi depuis la section du circuit |
| `_institution.qmd`, l. 335-413 (prélèvements à l'importation) | tableaux, TODO, RECHERCHE `r-prelevements-importation-cgc` | en place ; renvoi depuis la section du lait |
| `_institution.qmd`, l. 415-441 (dotation) | texte, tableaux, RECHERCHE `r-cgc-dotation-annees-manquantes` | en place |
| `_reformes.qmd`, l. 15 (ligne LF 1984, art. 87, de `tbl-compensation-reformes`) | ligne du tableau | en place, tant que ce tableau n'est pas fondu dans le registre de la Caisse (chantier du découpage) ; ce chapitre a sa propre ligne `r-comp-pb-1984` |
| `_reformes.qmd`, l. 36-38 (titre et premier alinéa de `#sec-compensation-1984`) | art. 87 ; céréales premier poste (BCT 1984) | **déplacé** vers `#sec-compensation-pb-1984`. Le titre de la section restante devient « 1984 : les ressources de la Caisse reconstituées », et **l'identifiant `sec-compensation-1984` est gardé**, parce que `fiscalite/_contributions_conjoncturelles.qmd`, l. 70, y renvoie pour les 8 MD de la contribution exceptionnelle de solidarité. Une phrase de tête renvoie vers le nouveau chapitre. |
| `_reformes.qmd`, l. 40-48 | reconstitution des ressources (LFC 1984, décret n° 84-259, BCT) | en place |
| `_reformes.qmd`, l. 48-52 | caisse des transports routiers, deux TODO | en place (`_transport` la raconte déjà) |
| `_depense.qmd`, l. 102 | puce « Les produits de base » | en place ; le renvoi est ajouté |
| `_depense.qmd`, constat « 2007-2008 : les produits de base » | constat | en place (il porte sur le poste) |
| `_depense.qmd`, l. 197-213 (« Les produits de base par produit, selon le ministère ») | `tbl-compensation-produits-2009-2011` et alinéa de non-coïncidence | **déplacé** vers `#sec-compensation-pb-longue-periode`, identifiant gardé ; il reste une phrase et un renvoi |
| `_exterieurs.qmd`, l. 68-114 (Banque mondiale 1977 et 1985, par produit) ; l. 116-134 (FMI) | tableaux `tbl-compensation-1982-1984` et suivants | en place ; renvoi depuis la mise en place et la longue période |
| `_incidence.qmd`, l. 7-62 | étude alimentaire, trois tableaux, TODO | en place ; renvoi depuis la vue d'ensemble et la section du ciblage |
| `index.qmd`, « Le plan du volume » | liste numérotée | **à modifier** : ajouter le chapitre, renuméroter ; l'item 2 (« Les réformes ») reste |
| `_quarto.yml` | `chapters:` | **à modifier** ; puis `uv run python scripts/arabe_cablage.py` |
| `entreprises_publiques/_offices.qmd`, l. 7 | lien `../compensation/_reformes.html#sec-compensation-1984` pour « la réforme de 1984 » des céréales | **à corriger** : il doit viser `../compensation/_produits_base.html#sec-compensation-pb-1984` ; ajouter un lien vers `#sec-compensation-pb-cereales` |
| `entreprises_publiques/_offices.qmd`, `tbl-ep-registre-oc-campagnes` | registre des campagnes de 2010 à 2026 | en place, par décision du 2 novembre 2026 ; à reconsidérer (P3) |
| `entreprises_publiques/_offices.qmd`, sections de l'ONH et de l'Office du commerce | tête de section | ajouter une phrase et un lien vers les sections des huiles et du sucre |
| `agriculture/index.qmd`, l. 35 | tableau de voisinage | ajouter le lien vers le chapitre |
| livre de l'éducation | papier scolaire | une phrase et un lien à poser, si le livre traite des fournitures |
| `fiscalite/_droits_douane.qmd`, l. 551 (prélèvement sur la banane au profit de la Caisse) | texte | en place |

Aucune ligne n'est supprimée.

## 8. Figures et tableaux

| Élément | Source | Famille | État |
|---|---|---|---|
| `fig-compensation-pb-poids` (vue d'ensemble) : charges des produits de base de 1985 à 2011 (BCT) et poste « produits de base » de 2003 à 2026 (ministère des Finances), en millions de dinars et en part des dépenses de l'État | séries `compensation-compte-caisse` et `compensation-parts` (`precis/_seriescache/`) | budgétaire, deux grandeurs distinctes (charges dues, dépense versée), deux traits, jamais raccordés | faisable maintenant ; marques 1984 et 1992 |
| `fig-compensation-par-produit` et `tbl-compensation-charges-produits` (déplacés) | `compensation-compte-caisse` | budgétaire (BCT) | existe |
| `fig-compensation-pb-poste` : poste « produits de base », 2003-2026 | `compensation-parts` | budgétaire | faisable ; doublon possible de `fig-compensation-par-poste` (P10) |
| `tbl-compensation-produits-2009-2011` (déplacé) | ministère des Finances 2011 | budgétaire | existe |
| `fig-compensation-pb-prix-campagne` : prix de base et prix normaux de rétrocession, blé dur et blé tendre, récoltes 2010-2026 | registre `tbl-ep-registre-oc-campagnes` (JO lu) ; aucune série dans `tunisia-data` | prix administrés | faisable après un travail de données : verser une série `cereales-prix-campagne` dans `tunisia-data`, depuis les lignes du registre, avant tout module de figure (`figtools.series()`) |
| `tbl-compensation-pb-circuit` : produit, opérateur, rôle, texte | registres des offices | droit | faisable maintenant |
| Transferts du budget à l'Office des céréales et à l'ONH, 2017-2023 | série `entreprises-publiques-transferts-par-etablissement` (`tunisia-data`) | budgétaire | faisable ; tableau court ou renvoi |
| Compensation des céréales par type et par origine (blé dur, blé tendre, orge ; local, importé), 2007-2021 | agridata, Office des céréales (`tunisia-data`, `agriculture/agridata/OC/`) | données de l'opérateur | après un travail de données : unités mélangées (2021 en dinars), série à construire et à cataloguer |
| Quantités subventionnées (farine, huile végétale), 2021-2023 | RAP du ministère du Commerce (`gbo/`) | budgétaire (performance) | à documenter d'abord (unités, D16) |
| Charges par produit 1970-1984 | Banque mondiale 1985, tableau III-1 | extérieur | en place dans `_exterieurs` ; ne pas tracer ici |
| Subventions par produit 2015-2022 (classeur CEQ, feuilles Food_1 et Food_2) | compilation de la Banque mondiale, non publiée | extérieur | à ne pas employer en budgétaire ; au mieux dans `_exterieurs`, avec sa méthode, si les sources déclarées (Office du commerce, ministère des Finances) sont retrouvées |
| Prix de vente au consommateur (pain, farine, semoule, huile, sucre, lait), longue période | aucune série localisée | prix administrés | à documenter d'abord (D10) |
| Série budgétaire par produit, 2012-2026 | aucune | budgétaire | à documenter d'abord (D13) |

## 9. Questions au documentaliste, par section

**Mise en place**
- **D1.** Décret n° 70-543 du 24 octobre 1970 (régimes de fixation des prix) : quels produits de
  base sont placés sous la « taxation » ? Rubriques et article.
- **D2.** Décrets de campagne des céréales de 1970 à 2009 (70-261, 71-253 et 72-244 connus par
  les visas) : prix de base, prix normaux de rétrocession, prime de compensation ; au moins les
  années charnières (1970, 1974-1975, 1984, 1992, 2008).
- **D3.** 1974-1975 : un texte qui fixe pour la première fois un prix de vente des céréales ou de
  l'huile inférieur au coût, et sa date d'effet ; les mots des rapports de la BCT pour 1974 et 1975
  sur le contexte (cours mondiaux) ; confirmation de l'art. 83 de la loi de finances pour 1975 [#810].
- **D4.** (facultatif) Un des décrets n° 67-407 à 67-410 ou 68-279 (stocks de blés), pour fonder la
  phrase d'antécédent.

**1984**
- **D5.** Les textes qui fixent les prix du pain, de la semoule et de la farine fin décembre 1983,
  puis ceux du retour en janvier 1984 ; les « mesures d'accompagnement » de l'art. 87, si un texte
  les fixe ; les mots du rapport de la BCT pour 1984 sur le contexte.

**1991-1992**
- **D6.** Tableau A du décret n° 91-1996 et du décret n° 95-1142 (et les rétablissements de 1992,
  JORT n° 11 p. 215 et n° 30 p. 581-582 ; décret n° 93-59) : relever les produits alimentaires et
  leur régime (homologation à tous les stades, tableaux B et C). Vérifier si un texte postérieur à
  2015 remplace la liste.
- **D7.** Les textes des sorties du champ : maïs (1992), tourteaux de soja (1993), engrais et sucre
  produit localement (1999).

**Sections des produits**
- **D8.** Le lait : opérateur, textes de prix, sortie en 2008 et retour en 2011.
- **D14.** Pâtes, couscous et double concentré de tomate : date d'entrée dans le champ et texte.
- **D15.** Papier scolaire : texte, opérateur ; prise en charge par le Centre national pédagogique
  en 1995.
- **D16.** Huile végétale : texte de la concession d'approvisionnement (non identifié, backlog) ;
  unités des quantités subventionnées des RAP du Commerce de 2021 à 2023 ; décret n° 74-876 (taxe
  sur l'huile d'olive exportée affectée à la Caisse).

**Circuit et longue période**
- **D12.** Bénéficiaire de l'écart de 191 à 307 MD par an entre le poste « produits de base » et
  les transferts à l'Office des céréales et à l'ONH (Office du commerce ? centrales laitières ?
  papier ?).
- **D13.** Une série budgétaire par produit après 2011 : rapports de la BCT 2015-2025, budgets
  citoyens, PAP et RAP de la mission Commerce, lois de règlement.

**État du droit et ciblage**
- **D9.** Ciblage et transferts de substitution, de 2013 à 2026 : articles de loi de finances, décrets
  ou arrêtés, avec la rubrique. L'objet n'est pas relevé. Ne pas le déduire des annonces.
- **D10.** Les prix de vente au consommateur en vigueur et leur texte (arrêtés ou décisions du
  ministre du Commerce ?), avec leur date d'effet ; l'autorité qui les fixe.
- **D11.** Le décret n° 2002-2145 (unité de compensation des produits de base au ministère des
  Finances) et le décret n° 2005-2934 (rattachement au Commerce) : à lire pour la phrase « qui
  décide » [#810 pour les intitulés].

## 10. Questions au propriétaire, désaccords de classement et risques

**Questions au propriétaire**

- **P1.** Ce qui constitue le dispositif : (a), la liste, l'autorité et la Caisse, ou (b), la
  filière des céréales ? Recommandé : (a).
- **P2.** Place du chapitre : avant `_carburants` (recommandé) ou après `_transport`.
- **P3.** Registre des campagnes des céréales : le laisser aux entreprises publiques (décision du
  2 novembre), avec une figure ici, ou le déplacer dans la section des céréales, comme prix
  administré. Recommandé : déplacer le registre et ne laisser aux entreprises publiques que le
  lien. Le prix à la production est le seul instrument de ce chapitre qui ait une série lue de 2010
  à 2026.
- **P4.** Déplacer « Les charges par produit » de `_institution` : je recommande oui. L'institution
  garde le total des charges, et le détail par produit est l'objet de ce chapitre. Autre lecture :
  le compte de la Caisse est une seule pièce, à ne pas couper.
- **P5.** 1991-1992 : grande réforme ou ajustement ? Pour les produits de base, le prix reste
  fixé. Ce qui change est la règle générale, dont ils deviennent l'exception. Je retiens « grande
  réforme », parce que la loi change d'objectif. L'arrêté de 1989 vient ici ou dans la section du
  sucre.
- **P6.** Récolte 2022 : « rupture » au registre des offices, « étape » selon la doctrine (un
  relèvement de niveau). Il faut aligner les deux registres.
- **P7.** Loi n° 94-37 (ONH) : rupture propre à la section des huiles (l'opérateur perd
  l'exclusivité) ou étape ?
- **P8.** Collecte et prix de l'huile d'olive (arrêté de 1996, campagnes oléicoles) : soutien au
  producteur, donc agriculture, ou prix administré, donc ce chapitre ? Recommandé : l'agriculture,
  puisque l'huile d'olive n'est pas un produit subventionné à la consommation.
- **P9.** Deux grandes réformes seulement, sous le seuil de trois : écrire avec cette épine courte,
  ou attendre D5, D6 et D9 ? Recommandé : attendre D6 et D9 au moins.
- **P10.** Une figure propre au poste « produits de base », ou un simple renvoi à
  `fig-compensation-par-poste` ?

**Risques**
- **Le repli peut cacher la face « producteur ».** Si le registre des campagnes est replié dans
  la section des céréales, le prix à la production disparaît du premier plan. La figure des prix
  de campagne doit rester visible.
- **Deux grandeurs proches.** Les charges de la Caisse (dues, BCT) et le poste budgétaire (versé,
  ministère des Finances) sont proches et se confondent facilement ; la figure de vue d'ensemble
  doit les tenir sur deux traits.
- **Des sources qui ne fondent pas une rupture.** Le champ des produits (entrées et sorties)
  repose entièrement sur des sources de seconde main. Le lecteur ne doit pas le lire comme du droit :
  ces sources restent signalées comme budgétaires dans la frise et dans la section « Les autres
  produits ».
- **Un trou après 1992.** L'absence de réforme sourcée après 1992 peut se lire comme une absence
  de politique. La phrase d'intervalle dit ce qui change (champ, prix de campagne) sans le
  qualifier.
- **Une dépendance à la PR #810.** Si elle change ses formulations de 1941, 1945, 1947 ou 1975, la
  mise en place s'ajuste.

## 11. Backlog (lignes proposées, à verser par l'archiviste ; rien n'est écrit dans `backlog-precis.md`)

- **Compensation, chapitre « Les produits de base » (`_produits_base.qmd`) : plan de l'architecte
  du 17 novembre 2026** (`docs/notes/plan-compensation-produits-de-base.md`). Il faut d'abord une
  note documentaire. Les points D1 à D16 sont à lire : JORT au corpus local pour D1, D2, D4 à D7,
  D11 et D14 ; rapports de la BCT au corpus de `tunisia-data` pour D3, D5 et D13 ; RAP du Commerce
  au corpus de `tunisia-data` pour D16 ; D9 et D10 sont à chercher.
- Série `cereales-prix-campagne` (récoltes 2010-2026) à constituer dans `tunisia-data` depuis
  `tbl-ep-registre-oc-campagnes` ; série agridata « compensation des céréales » 2007-2021 à
  construire (unités mélangées).
- Fiche économiste `docs/notes/eco-compensation-produits-de-base.md` à produire ; section « Ce qu'en
  dit l'économie » absente de tous les chapitres de dispositif du volume.
- Classement « rupture » de la récolte 2022 au registre `tbl-ep-registre-oc-campagnes` : à
  aligner sur la doctrine (P6).
- Décision du 2 novembre 2026 sur le domicile des décrets de campagne (« à reconsidérer ») : à
  trancher avec P3.
- Liens à corriger quand le chapitre existera : `entreprises_publiques/_offices.qmd`, l. 7 ;
  `agriculture/index.qmd`, l. 35.

## Fichiers utiles

- `precis/fr/compensation/_institution.qmd`, `_reformes.qmd`, `_depense.qmd`, `_exterieurs.qmd`, `_incidence.qmd`
- `precis/fr/compensation/_transport.qmd`, `_electricite_gaz.qmd` (gabarits convertis)
- `precis/fr/entreprises_publiques/_offices.qmd` (registres de l'Office des céréales, de l'ONH et de l'Office du commerce)
- `docs/notes/compensation.md`, `compensation-avant-1970-et-plans.md`, `compensation-electricite-gaz-objets-des-reformes.md`, `compensation-etudes-incidence-calculs.md`, `agriculture-plan-livre.md`
- `docs/notes/compensation-textes-fondateurs-2026-11-17.md` (PR #810, hors de ce worktree)
- `precis/_seriescache/compensation-compte-caisse.csv`, `compensation-parts.csv`
- `tunisia-data/sources/ministere-agriculture-tic-sante-finances.md` (agridata, Office des céréales), `ministere-energie-industrie-commerce.md` (RAP du Commerce)
