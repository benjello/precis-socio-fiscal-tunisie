# Finances locales — histoire, compétences, notions : fiche de plan de l'architecte

Rendue le 9 octobre 2026, pour arbitrage du propriétaire avant toute réécriture. Chapitres lus dans
le worktree `fl-transferts` : `precis/fr/finances_locales/_histoire.qmd` (156 lignes),
`_competences.qmd` (149 lignes), `_notions.qmd` (228 lignes). Notes : `finances-locales-histoire.md`,
`finances-locales-competences.md`, `fiscalite-locale-plan.md`, les deux notes de lectures du
9 octobre, les deux fiches de plan du volume. Aucun texte de loi n'a été relu : tout ce qui est
classé ici vient des notes et des chapitres, avec leur degré de certitude.

Les mots « cœur », « épine », « fiche » sont des mots de travail ; ils ne paraissent dans aucun
chapitre.

**En trois lignes.** Ces trois chapitres ne décrivent pas un dispositif : ils donnent le cadre.
L'histoire devient le chapitre des **grandes réformes du volume** (un tableau, cinq dates) ; les
compétences deviennent son **état du droit** (qui fait quoi, qui décide, qui contrôle) ; les notions
**restent un chapitre**, où les définitions, les tableaux et les formules sont au premier plan et les
développements de la doctrine repliés. Premier plan : 11 150 mots aujourd'hui, 6 750 visés (− 39 %).

---

## 1. Le constat

### 1.1 Mesures de départ (à refaire sur une copie gardée hors du dépôt avant de convertir)

| Chapitre | Mots (hors commentaires) | Sections (niv. 2 / niv. 3) | Tableaux | Lignes de tableau | Appels de citation | Clés distinctes | Ancres de glossaire | Formules | `TODO` | `RECHERCHE` | Blocs repliés |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `_notions` | 4 103 | 6 / 15 | 4 | 31 | 53 | 1 | 40 | 6 | 0 | 0 | 0 |
| `_histoire` | 3 337 | 6 / 12 | 3 | 16 | 72 | 27 | 6 | 0 | 1 | 4 | 0 |
| `_competences` | 3 708 | 5 / 12 | 2 | 6 | 77 | 11 | 14 | 0 | 2 | 2 | 0 |
| **Ensemble** | **11 148** | 17 / 39 | 9 | 53 | 202 | — | — | 6 | 3 | 6 | 0 |

Tableaux, avec leurs lignes de données : `tbl-fl-budget-decentralise` 4 ; `tbl-fl-tutelles` 2 ;
`tbl-fl-types-subventions` 5 ; `tbl-fl-notations` 20 ; `tbl-fl-hist-modifs-communes` 5 ;
`tbl-fl-hist-communes` 3 ; `tbl-fl-hist-chronologie` 8 ; `tbl-fl-comp-commune` 3 ;
`tbl-fl-comp-controle` 3. Aucune figure. Tout est au premier plan : aucun des trois chapitres n'a de
bloc replié ni de registre.

### 1.2 `_notions` : tout vit déjà au glossaire, sauf les tableaux et les formules

- **Un quart du chapitre double le glossaire.** Les 40 notions marquées ont toutes leur entrée
  (`precis/glossaire.yml`, 1 287 mots de définitions). Mesure faite, mot à mot, entre chaque
  définition et l'alinéa du chapitre qui marque la notion : 23 définitions sur 40 s'y retrouvent à
  80 % ou plus (six à 100 % : « collectivité locale », « libre administration », « autonomie
  budgétaire », « épargne nette », « impôt exclusif », « impôt partagé »), 34 à 60 % ou plus ; les
  six autres sont marquées dans un alinéa et définies dans un autre. Au total, environ 1 000 mots
  du chapitre sur 4 103 sont ceux du glossaire, que l'infobulle donne déjà partout dans le volume.
- **Ce que le glossaire ne porte pas, environ 3 100 mots** : le chapeau et les notations (420) ;
  trois tableaux de classement, six formules et la définition de leurs vingt symboles (550) ; les
  développements de Dafflon et Gilbert — conditions, nuances, classements, pratiques observées —
  (2 100, dont 800 tiennent en points au premier plan et 1 300 se replient).
- **Une douzaine de notions sont définies au fil du texte sans entrée de glossaire** : coopération,
  solidarité, responsabilité budgétaire, patrimoine administratif, déséquilibres locaux, effets de
  débordement, externalité fiscale, principe de dérivation, autonomie fiscale, péréquation verticale
  et horizontale, subventions d'incitation et correctrices. Question pour le terminologue, non pour
  ce plan.
- **Le chapitre est appelé 22 fois par les autres** : 14 de ses 15 sous-sections reçoivent au moins
  un renvoi, en comptant ceux de `_histoire` et de `_competences` (`_budgets` 5, `_impots_immeubles` 4, `_impots_activite` 3, `_taxes_redevances` 2,
  `_transferts` 5, `_longue_periode` 3) ; `_histoire` et `_competences` l'appellent 8 fois. Seule
  `sec-fl-potentiel-effort` n'est appelée par personne.
- **La table des notations (214 mots, 20 lignes)** redonne des symboles tous définis là où ils
  servent ; les deux fiches précédentes ont dissous les tables de ce genre.
- **Deux tournures contraires aux règles** : « Il ne décrit pas le droit en vigueur » (l. 3) ;
  l'annonce des notations en fin de chapitre (l. 7).
- **Une seule source** (Dafflon et Gilbert, 2018), citée 53 fois : aucune loi, donc aucun registre à
  créer et pas de `.domicile-unique`.
- **C'est le seul chapitre déclaré dans le livre arabe** (`precis/ar/finances_locales/_quarto.yml`).

### 1.3 `_histoire` : douze sous-sections sur le même plan, et le tableau de synthèse à la fin

- **Le tableau qui résume tout est en dernière section** (`tbl-fl-hist-chronologie`, 8 lignes : qui
  sont les collectivités, comment leurs conseils sont désignés, qui contrôle leur budget). C'est
  déjà le tableau court des ruptures ; il lui manque « ce que la loi cherche ».
- **Douze sous-sections de même rang** : la Constitution de 1959 (un article, 94 mots) pèse autant
  dans le plan que les six lois de 1975.
- **72 appels de citation dans le fil**, dont des suites d'articles (Constitution de 2014 :
  neuf appels en un paragraphe).
- **Le chapitre s'arrête à 2025** : il ignore le décret-loi n° 2026-4, que `_taxes_redevances`
  porte déjà dans deux registres.
- **Tournures à corriger** : « Seul l'objet des quatre premières lois est rappelé ici » (l. 66) ;
  « Les états intermédiaires […] ne sont pas établis ici » sans série (l. 102) ; la promesse « sera
  suivi au chapitre de la longue période » (l. 156, déjà reprise par la branche des budgets).

### 1.4 `_competences` : un tiers d'histoire redite, et l'organisation au même rang que l'argent

- **1 124 mots sur 3 708 racontent une seconde fois ce que dit `_histoire`** : la commune de 1975
  (art. 1, délégation spéciale), le conseil régional de 1989 (art. 1 et 6), la dissolution de 2023,
  la loi organique de 2025 — ces deux dernières presque mot pour mot.
- **Ce qui commande les finances est noyé** : le transfert de compétence « avec les moyens »
  (art. 16 et 244), le pouvoir de fixer les droits, le plafond des rémunérations, le rôle de la Haute
  instance des finances locales sont au milieu de la composition des conseils, des modes de gestion
  et des délais de publication.
- **La région et le district du code de 2018 (206 mots)** n'ont jamais eu de conseil élu et sont
  abrogés depuis le 18 mars 2025 : le chapitre le dit en dernière phrase.
- **La règle de datation des textes** (loi n° 93-64) est dans le chapeau, dans le fil.
- **Deux articles pour une même règle, deux fois** : le pouvoir de fixer les droits (art. 237 ici,
  art. 139 dans `_taxes_redevances`) ; le plafond des rémunérations (art. 9 ici, art. 135 dans
  `_budgets`).
- **La « longue période » tient en 34 mots de promesse** : aucune série de dépenses par fonction
  n'existe (`precis/_seriescache/finances-locales-communes-agregats.csv` suit des articles
  budgétaires, non des fonctions).
- **Tournure à corriger** : « ces modificatifs ne sont pas exposés ici » (l. 21).

### 1.5 Doublons avec les chapitres convertis

| Fait | Où il est raconté aujourd'hui | Domicile proposé | Ce que disent les autres |
|---|---|---|---|
| Les six lois du 14 mai 1975 | `_histoire` (liste) ; `_impots_activite`, `_transferts`, `_budgets` (chacun la sienne, en entier) | la liste à `_histoire`, une ligne par loi ; le contenu dans chaque chapitre | rien de plus |
| Entrée en vigueur du code de 2018 par étapes (art. 383) | `_histoire`, `_budgets`, `_taxes_redevances` (registre des dates) | `_histoire` | `_budgets` ne garde que la conséquence budgétaire (budgets de 2019) |
| Dissolution du 14 mars 2023 | `_histoire`, `_competences`, `_taxes_redevances` (registre et texte), `_budgets` | l'événement à `_histoire` ; ce que le secrétaire général décide à `_competences` | les autres renvoient à `@sec-fl-comp-dissolution-2023`, comme aujourd'hui |
| Décret-loi n° 2026-4 | `_taxes_redevances` (deux registres), `_transferts` (un `TODO`) | l'événement à `_histoire` ; chaque chapitre garde sa conséquence | — |
| Pouvoir de fixer les droits | `_competences` (art. 237), `_taxes_redevances` (art. 139) | `_taxes_redevances` (`@sec-fl-moduler-droits`) | `_competences` : une proposition et le renvoi |
| Plafond des rémunérations | `_competences` (art. 9), `_budgets` (art. 135) | `_budgets` | `_competences` : une proposition et le renvoi |
| Caisse des prêts et de soutien, 1975 | `_competences`, `_histoire`, `_transferts` | `_transferts` (`@sec-fl-cpscl`) | une proposition et le renvoi |
| Contrôle du budget, 1975 → 2018 | `_competences` (`tbl-fl-comp-controle`, 1re ligne), `_budgets` (`tbl-fl-budg-controle`) | `_budgets` pour le budget ; `_competences` pour les autres actes | la 1re ligne de `tbl-fl-comp-controle` devient un renvoi |

Relevé en passant : le `TODO` de `_transferts.qmd` (l. 199) dit que le décret-loi n° 2026-4 « n'a
pas de clé » ; `decretloi2026-4` est dans `references.json`. À corriger par qui touchera ce chapitre.

---

## 2. La forme proposée, et le plan cible

### 2.1 Pourquoi le plan type ne s'applique pas tel quel, et ce qui en tient lieu

Le plan type va de la mise en place à la longue période d'**un** dispositif. Ici, la matière se
répartit sur trois chapitres qui en sont chacun un morceau :

| Morceau du plan type | Chapitre | Forme |
|---|---|---|
| (avant le droit) le vocabulaire | `_notions` | chapitre de doctrine : pour chaque notion, la définition, le tableau ou la formule, puis le développement replié |
| vue d'ensemble, mise en place, grandes réformes | `_histoire` | l'ordre des dates : un tableau de cinq réformes, une section courte par réforme, un registre replié par réforme |
| état du droit et dispositions | `_competences` | par question — que font les collectivités, qui fixe, qui contrôle — avec, pour chacune, l'état de 1975, de 2018 et de 2026 |
| longue période | `_budgets` (en cours) | les figures du volume ; `_histoire` ne garde que le nombre de communes |

**L'état du droit ne s'écrit qu'une fois, à `_competences`** (`#sec-fl-comp-depuis-2023`) : `_histoire`
s'arrête à la dernière réforme et y renvoie. Frontière entre les deux chapitres d'institutions : **à l'histoire, qui sont les collectivités et
comment leurs conseils sont désignés et contrôlés ; aux compétences, ce qu'elles font et qui décide
de la dépense et de la recette.** Un texte commun (loi de 1975, code de 2018, décret-loi de 2023) a
une ligne dans le registre de chacun, pour des articles différents.

### 2.2 Les réformes qui découpent `_histoire`, vérifiées une à une

La liste proposée par le propriétaire est confrontée à ce que les notes ont lu.

| Date proposée | Verdict | Motif |
|---|---|---|
| Protectorat | **pas une réforme** | aucun texte lu : visas et abrogations seulement ; la note dit de ne rien écrire sur 1858 ni sur les commissions municipales. Un paragraphe court dans la mise en place |
| Indépendance, 1957 | **mise en place** | loi municipale du 14 mars 1957 et loi n° 57-12, lues |
| Lois de 1975 | **grande réforme** | six lois du même jour, lues |
| (1989, absente de la liste) | **étape**, autre lecture possible | loi organique n° 89-11, lue ; voir ci-dessous |
| Code de 1997 | **hors de ce chapitre** | la note d'histoire ne l'établit pas ; il est la mise en place des trois chapitres d'impôts. Une ligne sur la frise, un renvoi |
| Dissolutions de 2011 | **à trancher (A2)** | décrets n° 2011-383 et 2011-384 lus ; le reste connu par ses intitulés |
| Constitution de 2014 | **ne peut pas porter une réforme** | connue par la traduction que reproduisent Dafflon et Gilbert ; son numéro spécial n'est pas identifié. Elle entre comme fondement du code de 2018 |
| Code de 2018 | **grande réforme** | édition arabe lue (art. 1, 2, 4, 5, 383, 384) |
| Dissolution de 2023 | **grande réforme**, groupée avec 2025 | décrets-lois n° 2023-9 et 2023-10 lus en arabe |
| Loi organique de 2025 | groupée avec 2023 | lue dans les deux éditions |
| Décret-loi n° 2026-4 | **grande réforme, publiée et non entrée en vigueur** | lu à l'image pour les art. 1 à 13, 28 à 34, 57 à 99, 132 à 140 ; le reste parcouru |

Les réformes retenues :

| # | Réforme | Textes et articles (lus selon les notes) | Date d'effet | Ce que la loi cherche, dans ses mots | Avant → après |
|---|---|---|---|---|---|
| H0 | **Mise en place, 1957** | décret du 14 mars 1957 portant loi municipale, art. 1, 3, 6, 104 à 115 ; loi n° 57-12, art. 1 à 3, 16 à 23 | publication du 15 mars 1957 ; date d'effet non relevée | art. 1 : des « collectivités de droit public dotées de la personnalité civile et de l'autonomie financière et chargées de la gestion des intérêts municipaux » | décrets de 1945 à 1954, connus par leurs visas → 94 communes à conseil élu, budget arrêté par deux ministres ; un conseil de gouvernorat nommé |
| H1 | **1975 : six lois refondent ensemble l'organisation et les finances** | lois n° 75-33 (art. 1, 2, 12, 13, 36 à 46), 75-34, 75-35, 75-36, 75-37, 75-38 (intitulé), 75-39 | 1er janvier 1976 pour le budget, le fonds et la caisse ; loi n° 75-33 : non relevée | art. 1 de la loi organique : la commune participe, « dans le cadre du plan national de développement », à la promotion de la localité | loi municipale de 1957 → loi organique des communes, loi organique du budget, fonds commun, caisse de prêts et de soutien, deux taxes sur l'activité |
| H2 | **2018 : le code des collectivités locales** | loi organique n° 2018-29, édition arabe, art. 1, 2, 4, 5, 383, 384 ; Constitution de 2014, ch. VII, en fondement | par étapes, après les élections de chaque catégorie ; règles budgétaires des communes : budgets de 2019 | art. 1 : organiser les structures du pouvoir local « en vue de réaliser la décentralisation et le développement global, équitable et durable dans le cadre de l'unité de l'État » | conseils élus sous approbation préalable → communes, régions et districts à conseils élus, libre administration, contrôle par le juge |
| H3 | **2023-2025 : les conseils municipaux dissous ; des conseils locaux, régionaux et de districts** | Constitution de 2022, art. 81, 84, 133 ; décrets-lois n° 2023-9 (art. 1 à 3) et 2023-10 (art. 1, 3, 6 à 8, 43) ; loi organique n° 2025-4 (art. 1, 5, 7 à 10) | 14 mars 2023 ; 18 mars 2025 | intitulés : « relatif à la dissolution des conseils municipaux » ; loi « relative aux conseils locaux, conseils régionaux et conseils de districts » ; pour le reste **objet non relevé** | communes, régions, districts du code → communes sans conseil, gérées par leur secrétaire général sous la supervision du gouverneur ; trois niveaux de conseils qui délibèrent sur les plans de développement |
| H4 | **2026 : un décret-loi relatif aux conseils municipaux, en attente d'élections** | décret-loi n° 2026-4, art. 12, 29, 30, 136, 139 | après la proclamation des résultats des prochaines élections municipales (art. 136) | intitulé : « relatif aux conseils municipaux » ; **objet non relevé** au-delà | code de 2018, délibérations exécutoires sous le contrôle du juge → code abrogé, délibérations sur le budget et les droits soumises à l'approbation du gouverneur |

Étapes et ajustements, rattachés : Constitution de 1959, ch. VIII (H0, consécration en un article) ;
loi n° 63-54 (H0, le conseil de gouvernorat devient collectivité) ; loi constitutionnelle n° 2002-51
(ajustement) ; lois organiques n° 85-43, 91-24, 95-68, 2006-48 (H1, **connues par leur seul
intitulé**) et n° 2008-57 (H1, ajustement) ; communes nouvelles de 2015 à 2017, décret de convocation
de 2017, proclamations de 2018 (H2, étapes) ; décrets n° 2023-588 et 2023-589, décret n° 2025-177
(H3, étapes) ; décret-loi n° 2023-8 (H3, ligne de registre, intérêt secondaire selon la note).

Lectures concurrentes, à trancher :

- **1989.** Retenue comme étape de H1 : le conseil régional n'a pas d'élection propre, reste présidé
  par le gouverneur et sous la tutelle du ministre. Autre lecture : une réforme, parce que le
  gouvernorat devient à la fois circonscription de l'État et collectivité, avec un plan régional.
- **2011.** Voir l'arbitrage A2.
- **2023 et 2025.** Groupés parce que les textes de 2025 organisent ce que ceux de 2023 créent.
  Autre lecture : deux réformes, la dissolution (qui touche les communes) et les nouveaux conseils
  (qui remplacent les régions).

### 2.3 `_histoire` : plan cible

```
# Les collectivités locales, de 1957 à 2026 {#sec-fl-histoire .domicile-unique}
## Vue d'ensemble {#sec-fl-hist-vue-ensemble}
## La mise en place, 1957-1963 {#sec-fl-hist-1957}
### Ce que la loi municipale remplace {#sec-fl-hist-avant-1956}
### La commune de 1957 {#sec-fl-hist-loi-municipale}
### Les conseils de gouvernorat et la Constitution de 1959 {#sec-fl-hist-conseils-gouvernorat}
## Les grandes réformes {#sec-fl-hist-reformes}
### 1975 : six lois refondent l'organisation et les finances {#sec-fl-hist-lois-1975}
### De 1975 à 2011 : le conseil régional, et cinq retouches {#sec-fl-hist-modifications}
### 2011-2018 : des délégations spéciales nommées {#sec-fl-hist-2011}
### 2018 : le code des collectivités locales {#sec-fl-hist-code-2018}
#### Le fondement : la Constitution de 2014 {#sec-fl-hist-2014}
#### Communes nouvelles, élections et entrée en vigueur par étapes {#sec-fl-hist-carte}
### 2023-2025 : conseils municipaux dissous, nouveaux conseils {#sec-fl-hist-2023-2025}
#### La Constitution de 2022 {#sec-fl-hist-2022}
#### Les décrets-lois de 2023 et la loi organique de 2025 {#sec-fl-hist-2023-textes}
### 2026 : un décret-loi en attente d'élections {#sec-fl-hist-2026}
## La longue période : le nombre de communes {#sec-fl-hist-longue-periode}
```

Identifiants : quatorze restent des titres. Cinq perdent leur titre (`sec-fl-hist-1959`,
`sec-fl-hist-1975`, `sec-fl-hist-1989`, `sec-fl-hist-2011-2022`, `sec-fl-hist-apres-2022`) : aucun renvoi `@` ne les vise, ni dans le volume,
ni dans `docs/recherches.yml` ; ils deviennent une ancre `[]{#…}` en tête du passage d'accueil.
Préfixe des registres : `r-fl-hist-`.

| Section | L'essentiel, en une phrase | Vue d'ensemble | Points au premier plan | Bloc replié (titre exact) |
|---|---|---|---|---|
| Chapeau | Qui sont les collectivités locales, comment leurs conseils sont désignés et qui contrôle leurs décisions : le chapitre le suit de 1957 à 2026 | — | deux notions rappelées d'un mot (libre administration, tutelle), avec leur renvoi ; ce que le chapitre donne pour chaque réforme | — |
| Vue d'ensemble | Depuis 1957, les conseils sont tour à tour élus, nommés ou dissous ; leur budget, approuvé d'avance depuis 1957, ne l'est plus sous le code de 2018 | **`tbl-fl-hist-chronologie` remonté**, réduit à cinq lignes (H0 à H4), colonnes : la réforme ; ce que la loi cherche ; les conseils ; le contrôle du budget ; où sont les finances (`@sec-fl-budg-1975`, `@sec-fl-budg-ccl`, `@sec-fl-activite-code`, `@sec-fl-transferts-1975`, `@sec-fl-ccl-2018`). Frise : `<!-- TODO (rédacteur) : frise -->` | 1. deux questions reviennent : élus ou nommés ? approbation ou recours ? 2. les finances suivent : 1975 (budget, fonds, caisse, taxes), 1997 (code de la fiscalité locale, `@sec-fl-code-1997`), 2018 ; 3. aucune commune n'a de conseil élu depuis le 14 mars 2023 : l'état du droit est au chapitre des compétences (`@sec-fl-comp-depuis-2023`) | « Dates d'application des textes des collectivités locales : la règle générale et les clauses propres, 1957-2026 » |
| Mise en place — ce que la loi remplace | Les textes beylicaux et du protectorat ne sont connus ici que par les visas et les abrogations des textes de 1957 et de 1997 | — | une phrase, un renvoi à `@sec-fl-immeubles-origines` | « Textes antérieurs à 1957 visés ou abrogés par les lois de 1957 et de 1997 : décrets de 1922 à 1954 » |
| La commune de 1957 | La commune est une collectivité à conseil élu, dont le budget est arrêté par deux ministres | — | 1. 94 communes, créées par décret, conseil élu au suffrage universel direct ; 2. budget voté puis « arrêté » par les ministres de l'Intérieur et des Finances ; 3. ressources : taxes locales, quote-part des fonds communs, patrimoine, subventions | « Loi municipale du 14 mars 1957 : statut, budget, tutelle et ressources, article par article » |
| Conseils de gouvernorat, Constitution de 1959 | Auprès du gouverneur, un conseil nommé, qui devient collectivité en 1963 ; la Constitution consacre les deux niveaux en un article | — | 1. 1957 : membres nommés, budget ordonnancé par le gouverneur ; 2. 1963 : « collectivité publique », membres ès qualités ; 3. 1959, puis 2002 : un article, sans liste de compétences ni principe d'autonomie | « Conseils de gouvernorat et Constitution de 1959 : lois n° 57-12 et 63-54, chapitre VIII, article 71 de 2002 — articles et pages » |
| 1975 | Six lois du même jour refondent la commune, son budget, le fonds commun, la caisse de prêts et deux taxes | la liste des six lois, une ligne chacune, avec renvoi (elle reste au premier plan : elle est courte et annonce quatre chapitres) | 1. la commune participe au plan national ; 2. un conseil dissous est remplacé par une délégation spéciale nommée ; 3. tutelle étendue : renvoi à `@sec-fl-comp-communes-1975` | « Lois du 14 mai 1975 : les six lois, articles et pages » |
| De 1975 à 2011 | En 1989, un conseil régional sans élection propre remplace le conseil de gouvernorat ; la loi organique des communes est retouchée cinq fois | — | 1. 1989 : le gouvernorat, circonscription et collectivité ; 2. cinq lois de 1985 à 2008, dont une seule est lue ; Dafflon et Gilbert tiennent celle de 2006 pour la plus importante | « Loi organique des communes et conseils régionaux : textes, date par date, avec leur portée, 1985-2008 » (reçoit `tbl-fl-hist-modifs-communes` et la loi de 1989) |
| 2011-2018 | Après la révolution, des conseils municipaux sont dissous par décret et remplacés par des délégations spéciales nommées, jusqu'aux élections de 2018 | — | 1. 8 avril 2011 : premier décret, délégations nommées pour un an au plus ; 2. d'autres décrets suivent jusqu'en 2012, puis les conseils régionaux ; 3. le nombre des conseils dissous n'est pas établi ici (ancre `RECHERCHE` conservée) | « Dissolutions de conseils municipaux et délégations spéciales : décrets, date par date, 2011-2012 » (voir § 4, question 1) |
| 2018, le code | Le code fait des communes, des régions et des districts des collectivités à conseils élus, sous le contrôle du juge | — | 1. ce que le code cherche (art. 1) ; 2. trois catégories, libre administration, conseils élus ; 3. renvois : compétences `@sec-fl-comp-code-2018`, budget `@sec-fl-budg-ccl`, droits `@sec-fl-ccl-2018` | « Code des collectivités locales de 2018 : principes, catégories de collectivités et entrée en vigueur (art. 1, 2, 4, 5, 383 et 384), édition arabe » |
| — la Constitution de 2014 | Le chapitre VII fonde le pouvoir local sur la décentralisation | — | quatre points au lieu de neuf appels : collectivités et libre administration ; conseils élus ; compétences et ressources ; contrôle *a posteriori*. La phrase sur l'édition citée et son ancre `RECHERCHE` restent | « Constitution de 2014, chapitre VII “Le pouvoir local” : articles 131 à 141 » |
| — communes, élections, entrée en vigueur | Le territoire est entièrement couvert de communes avant les élections du 6 mai 2018 ; le code s'applique ensuite par étapes | renvoi à `tbl-fl-hist-communes` | 1. 86 communes nouvelles, selon Dafflon et Gilbert ; 2. élections du 6 mai 2018 ; 3. règles budgétaires au 1er janvier suivant : budgets de 2019 ; aucune élection régionale | (registre du code, ci-dessus) |
| 2023-2025 | Les conseils municipaux sont dissous le 14 mars 2023 ; des conseils locaux, régionaux et de districts sont élus puis dotés d'un statut en 2025 | — | 1. dissolution, secrétaire général sous la supervision du gouverneur ; 2. trois niveaux de conseils, élus de proche en proche ; 3. 2025 : les nouveaux conseils reçoivent le statut de collectivités ; la région et le district du code, et la loi de 1989, sont abrogés. Le budget de ces conseils et le sort des biens des anciens conseils régionaux ne sont dits qu'à `@sec-fl-comp-conseils-2025` | « Constitution de 2022, décrets-lois de 2023 et loi organique de 2025 : articles, dates et pages » |
| — la Constitution de 2022 | Un article, sur la trame de 1959 ; une seconde chambre élue par les conseils régionaux et de districts | — | les deux paragraphes actuels, resserrés | (même registre) |
| 2026 | Un décret-loi publié le 30 septembre 2026 abroge le code de 2018 ; il n'entrera en vigueur qu'après les prochaines élections municipales | — | 1. la condition d'entrée en vigueur, dans ses mots ; 2. ce qui change alors : approbation du gouverneur sur le budget et les droits (`@sec-fl-moduler-droits`) ; 3. jusque-là, le décret-loi de 2023 reste applicable. Le chapitre s'achève sur cette phrase et sur le renvoi à l'état du droit (`@sec-fl-comp-depuis-2023`) | « Décret-loi n° 2026-4 relatif aux conseils municipaux : articles 12, 29, 30, 136 et 139, édition arabe » |
| Longue période | Le nombre de communes passe de 94 en 1957 à 350 à la fin de 2017 | `tbl-fl-hist-communes` (3 lignes, non replié) | la réserve sur les dates intermédiaires et son ancre ; renvoi à `@sec-fl-budg-longue-periode` pour le poids financier | — |

### 2.4 `_competences` : ce qui commande les finances, et ce qui se replie

| Au premier plan : ce qui commande la dépense et la recette | Replié : l'organisation |
|---|---|
| les trois catégories de compétences, et la compétence générale de la commune | la composition des conseils, l'élection du président et des adjoints |
| le tableau des compétences de la commune (`tbl-fl-comp-commune`) : qui dépense pour quoi | les attributions du président, article par article |
| le transfert de compétence « avec les moyens » (art. 16 et 244) | la composition du Conseil supérieur et de la Haute instance |
| qui fixe les droits et redevances (une proposition, renvoi) | les modes de gestion des services (régie, concession, entreprises locales) |
| le plafond des rémunérations et la part de la formation (une proposition, renvoi) | les délais de publication et d'exécution des arrêtés |
| qui contrôle les actes : approbation préalable, puis juge (`tbl-fl-comp-controle`) | la liste des douze matières soumises à approbation en 1975 |
| la Haute instance des finances locales : coût des transferts, critères, endettement | la région et le district du code de 2018, abrogés |
| les organismes nationaux qui exercent des tâches locales, selon Dafflon et Gilbert | le pouvoir réglementaire local et le *Journal officiel des collectivités locales* |
| ce que décide une commune sans conseil, depuis 2023 | le fonctionnement interne des conseils de 2025 (décret n° 2025-177) |

Contenu exact du tableau de tête `tbl-fl-comp-etats` — le rédacteur n'y ajoute rien :

| | Loi de 1975 | Code de 2018 | Octobre 2026 |
|---|---|---|---|
| Liste de compétences | aucune : le conseil « règle par ses délibérations les affaires de la commune » | propres, partagées, transférées ; compétence générale de la commune | commune : celles du code, sans conseil élu pour les exercer ; nouveaux conseils : délibération sur les plans de développement |
| Qui fixe les droits et redevances | renvoi à `@sec-fl-moduler-droits` | le conseil élu | **non établi** : le décret-loi de 2023 ne le dit pas (`@sec-fl-moduler-droits`) |
| Qui contrôle les actes | approbation préalable ; nullité déclarée par le gouverneur | le juge, saisi par le gouverneur ou par un intéressé | le secrétaire général gère « sous la supervision du gouverneur » ; rien de plus n'est établi |
| Moyens des compétences transférées | — | fixés par la loi, avec les crédits et les moyens | **aucune loi de transfert identifiée** (ancre `r-fl-loi-competences-partagees`) |

Les trois passages de doctrine (« délégation ou dévolution ? », la « double casquette » du
gouvernorat, les agences) **restent où ils sont et visibles** : la place des études n'est pas encore
fixée.

```
# Les compétences : qui fait quoi, qui décide {#sec-fl-competences .domicile-unique}
## Vue d'ensemble {#sec-fl-comp-vue-ensemble}
## Avant 2018 : pas de liste de compétences, une approbation préalable {#sec-fl-comp-avant-2018}
### La commune de 1975 {#sec-fl-comp-communes-1975}
### Le conseil régional de 1989 {#sec-fl-comp-conseils-regionaux}
## 2018 : trois catégories de compétences {#sec-fl-comp-code-2018}
### Compétences propres, partagées, transférées {#sec-fl-comp-categories}
### Les compétences de la commune {#sec-fl-comp-commune}
### La région et le district {#sec-fl-comp-region-district}
### Délégation ou dévolution : la lecture de la doctrine {#sec-fl-comp-delegation-devolution}
## Qui décide, qui contrôle {#sec-fl-comp-organisation}
### Le contrôle des actes {#sec-fl-comp-controle}
### Les instances nationales {#sec-fl-comp-instances}
### Conseil, président, administration {#sec-fl-comp-organes}
### Services, entreprises et organismes nationaux {#sec-fl-comp-agences}
## L'état du droit en octobre 2026 {#sec-fl-comp-depuis-2023}
### La commune sans conseil élu {#sec-fl-comp-dissolution-2023}
### Conseils locaux, régionaux et de districts {#sec-fl-comp-conseils-2025}
```

Tous les identifiants actuels restent des titres, y compris les quatre appelés de l'extérieur
(`sec-fl-comp-dissolution-2023`, `sec-fl-comp-instances`, `sec-fl-comp-communes-1975`,
`sec-fl-comp-conseils-regionaux`). Seul `sec-fl-comp-longue-periode` disparaît (ancre posée dans la
vue d'ensemble ; la branche des budgets en a déjà repris la phrase). Préfixe : `r-fl-comp-`.

| Section | L'essentiel, en une phrase | Vue d'ensemble | Points au premier plan | Bloc replié (titre exact) |
|---|---|---|---|---|
| Chapeau | Ce que les collectivités font, qui décide de la dépense et de la recette, qui contrôle | — | renvoi en tête à `@sec-fl-histoire` pour la suite des textes ; trois notions d'un mot (délégation, dévolution, subsidiarité) | — |
| Vue d'ensemble | La loi de 1975 ne donne pas de liste de compétences ; le code de 2018 en donne trois catégories ; depuis 2023 la commune n'a plus de conseil pour les exercer | **tableau court nouveau**, `tbl-fl-comp-etats`, quatre lignes × trois états ; son contenu est fixé ci-dessus, cases « non établi » comprises | 1. ce que cela coûte se lit au chapitre des budgets (`@sec-fl-budg-longue-periode`) : aucune série par fonction ; 2. la loi des compétences partagées n'est pas identifiée | « Dates d'application des textes des compétences : la règle générale et les clauses propres, 1975-2025 » (reçoit la règle de la loi n° 93-64) |
| La commune de 1975 | Le conseil « règle par ses délibérations les affaires de la commune », sans liste, et ses décisions financières attendent l'approbation | — | 1. budget, programme d'équipement, avis ; 2. approbation préalable du budget, des emprunts, des taxes et droits, acquise tacitement après quinze jours ; 3. Dafflon et Gilbert reconstituent les compétences par inférence | « Loi organique des communes de 1975 : attributions du conseil, matières soumises à approbation, nullité et dissolution (art. 1, 2, 12, 13, 36 à 46) » |
| Le conseil régional de 1989 | Il élabore le plan régional dans le cadre du plan national et arrête le budget du gouvernorat | — | 1. attributions ; 2. la « double casquette » selon Dafflon et Gilbert | « Loi organique n° 89-11 sur les conseils régionaux : attributions et tutelle (art. 1 à 3, 6, 18 à 21) » |
| Trois catégories | Le code distingue des compétences propres, partagées et transférées | — | les quatre règles actuelles, en quatre points sans appels : exclusivité ; subsidiarité ; transfert par la loi, avec les moyens ; compétence générale de la commune. Puis le constat et son ancre `RECHERCHE` | « Code des collectivités locales : les compétences, principes et pouvoir réglementaire (art. 11 à 20 et 25 à 28), édition arabe » |
| Les compétences de la commune | Services de proximité en propre ; économie, réseaux et écoles en partage ; santé, éducation, culture et sport par transfert | `tbl-fl-comp-commune` (3 lignes, non replié) | 1. le conseil fixe les droits : une proposition, `@sec-fl-moduler-droits` ; 2. tout transfert s'accompagne « obligatoirement » des ressources, par convention ; 3. l'avis sur les projets de l'État est obligatoire sans être bloquant | « Compétences de la commune dans le code de 2018 : articles 234 à 244, édition arabe » |
| La région et le district | Leurs compétences, jamais exercées par des conseils élus, sont abrogées depuis le 18 mars 2025 | — | une phrase, renvoi à `@sec-fl-comp-conseils-2025` | « Région et district dans le code de 2018 : compétences propres, partagées et transférées (art. 293 à 298 et 356 à 358), abrogées en 2025 » |
| Délégation ou dévolution | Le code ne dit ni l'un ni l'autre ; la doctrine n'est pas unanime | — | les trois points actuels, inchangés | — |
| Le contrôle des actes | En 2018, le juge remplace l'approbation préalable | `tbl-fl-comp-controle` (non replié ; sa première ligne renvoie à `@sec-fl-budg-ccl-controle`) | 1. arrêtés exécutoires après publication ; 2. recours du gouverneur ou d'un intéressé ; 3. dissolution : par décret motivé, sous le contrôle du juge | « Contrôle des actes de la commune : articles de 1975 et de 2018 (art. 197, 204, 276 à 279) » |
| Les instances nationales | Une Haute instance des finances locales propose les ressources à transférer, chiffre le coût des transferts de compétences et suit l'endettement | — | 1. la Haute instance ; 2. le Conseil supérieur : avis obligatoire sur les lois de finances locales ; 3. la décentralisation « progressive » et la loi d'orientation | « Conseil supérieur des collectivités locales et Haute instance des finances locales : composition et attributions (art. 47 à 68) » |
| Conseil, président, administration | Le président prépare le budget et en ordonnance les dépenses ; un secrétaire général dirige l'administration | — | 1. président ordonnateur ; 2. agents payés sur le budget communal, plafond de moitié (`@sec-fl-budg-ccl-principes`) ; 3. le secrétaire général, qui gère seul depuis 2023 | « Organes de la commune dans le code de 2018 : conseil, président, administration (art. 9, 203, 256, 257, 271 à 273, 299) » |
| Services, entreprises et organismes nationaux | Une partie des tâches locales est exercée par des organismes nationaux | — | 1. la liste des organismes et l'appréciation de Dafflon et Gilbert, attribuée ; 2. la caisse de prêts : `@sec-fl-cpscl` ; 3. la formation des élus et sa part du budget | « Gestion des services locaux : régie, concession, entreprises publiques locales, formation (art. 43, 44, 80 à 83, 103 et 104) » |
| La commune sans conseil élu | Depuis le 14 mars 2023, le secrétaire général gère les affaires courantes sous la supervision du gouverneur | — | 1. ce que le texte confie ; 2. ce qu'il ne dit pas (vote du budget : `@sec-fl-budg-2025` ; droits : `@sec-fl-moduler-droits`) ; 3. la réserve, une seule fois dans le volume : aucun texte convoquant des élections municipales n'est identifié (ancre `r-fl-elections-municipales-apres-2023`) ; le décret-loi de 2026 attend ces élections (`@sec-fl-hist-2026`) | « Dissolution des conseils municipaux : décret-loi n° 2023-9, articles 1 à 3 » |
| Conseils de 2025 | Ils délibèrent sur les plans de développement ; ils n'ont pas de liste de compétences | — | 1. compétence de délibération ; 2. budget sous la loi de 1975 : `@sec-fl-budg-2025` ; 3. biens des anciens conseils régionaux à l'État | « Conseils locaux, régionaux et de districts : loi organique n° 2025-4 et décret n° 2025-177, articles et pages » |

### 2.5 `_notions` : plan cible

Le chapitre garde son titre, sa place, ses cinq sections et **tous ses identifiants**. Dans chaque
sous-section : la phrase de définition (elle reste, parce que le PDF n'a pas d'infobulles), le
tableau ou la formule avec ses symboles, deux à quatre points, puis le développement de Dafflon et
Gilbert dans un bloc replié — un par section de niveau 2.

| Section | Reste au premier plan | Bloc replié (titre exact) |
|---|---|---|
| Chapeau | la source et sa réserve ; l'écart entre les mots du droit tunisien et les notions ; l'ordre du chapitre. Sortent : « Il ne décrit pas le droit en vigueur » et l'annonce des notations | — |
| Décentraliser | les trois volets, en trois points ; la collectivité locale et la libre administration, en une définition et deux volets ; la subsidiarité et « fonctions, finances, fonctionnaires » | « Décentralisation, libre administration et subsidiarité selon Dafflon et Gilbert : délégation qui tourne à la déconcentration, coopération et solidarité, sens historique de la subsidiarité » |
| Le budget local | `tbl-fl-budget-decentralise` ; déséquilibre vertical ; la règle d'or en deux principes ; les deux formules de la capacité d'emprunt et leurs dix symboles ; `tbl-fl-tutelles` | « Budget local selon Dafflon et Gilbert : place de l'emprunt, patrimoine financier et administratif, déséquilibres locaux, budget global ou dédoublé, pratiques de tutelle observées » |
| Les ressources propres | impôt, taxe, redevance : les trois critères et les trois définitions ; les trois autonomies ; impôt exclusif, impôt partagé, part aux recettes | « Ressources propres selon Dafflon et Gilbert : quatre conditions de la redevance, classement des ressources par degré d'autonomie, partage selon l'origine ou selon une clé, externalités fiscales » |
| Les transferts | quatre objectifs ; trois critères ; `tbl-fl-types-subventions` ; péréquation des ressources et des besoins, verticale et horizontale | « Transferts et péréquation selon Dafflon et Gilbert : autres corrections du déséquilibre, effet des subventions conditionnelles, différences et disparités, conditions d'accès » |
| Mesurer | les quatre formules (autonomie financière, potentiel fiscal, facturation, recouvrement), chaque symbole défini sur place | « Mesure de l'autonomie et de l'effort fiscal selon Dafflon et Gilbert : limites du périmètre des recettes propres, produit élevé et effort élevé » |
| Notations | **dissoute** : chaque symbole est déjà défini là où il sert | — |

Le chapitre n'entre pas dans `.domicile-unique` : il ne cite aucune loi.

### 2.6 L'ordre des chapitres du volume

| # | Chapitre | Fichier | Rôle |
|---|---|---|---|
| 1 | Présentation | `index.qmd` | ce que le volume donne ; trois mouvements au lieu de quatre |
| 2 | Les notions | `_notions.qmd` | le vocabulaire |
| 3 | Les collectivités locales, de 1957 à 2026 | `_histoire.qmd` | mise en place et grandes réformes du volume |
| 4 | Les compétences : qui fait quoi, qui décide | `_competences.qmd` | état du droit des institutions |
| 5 | Budgets et comptes | `_budgets.qmd` | règles budgétaires, et les chiffres d'ensemble du volume |
| 6 | Les impôts sur les immeubles | `_impots_immeubles.qmd` | |
| 7 | Les impôts sur l'activité | `_impots_activite.qmd` | |
| 8 | Taxes, redevances et autonomie fiscale | `_taxes_redevances.qmd` | |
| 9 | Les transferts de l'État | `_transferts.qmd` | |
| A | Glossaire | `_glossaire.qmd` | |

L'ordre actuel est donc conservé, moins `_longue_periode`. Deux autres ordres ont été pesés et
écartés : les transferts avant les impôts (ils pèsent davantage, mais les notions, la présentation
et le chapitre des budgets vont tous des ressources propres aux transferts) ; les notions en annexe
(voir A3). `index.qmd` est déjà repris par la branche des budgets ; il y faudra en plus les deux
nouveaux titres et la suppression de la phrase « les trois chapitres des institutions sont à
écrire », périmée.

---

## 3. Le registre de destination

« 1er plan » : texte principal. « Replié » : dans le bloc nommé au § 2. Rien n'est supprimé sans
que l'information subsiste ailleurs.

### 3.1 `_histoire`

| Élément actuel | Destination |
|---|---|
| Chapeau, l. 3 (cinq notions rappelées) | 1er plan, réduit à deux notions ; les trois autres sont rappelées à `_competences` |
| Chapeau, l. 5 (« va de l'indépendance à 2025 », édition arabe, « traduits par nous ») | 1er plan, borne portée à 2026 ; la mention des éditions va dans le registre des dates |
| `#sec-fl-hist-avant-1956` | 1er plan, une phrase ; la liste des décrets visés → replié, registre des textes antérieurs |
| `#sec-fl-hist-loi-municipale` (3 alinéas) | 1er plan : trois points ; articles 104 à 115, déséquilibre et redressement → replié, registre de la loi municipale |
| `#sec-fl-hist-conseils-gouvernorat` | 1er plan : deux points ; taxes régionales, retenue de 5 %, liste des recettes de 1963 → replié |
| `#sec-fl-hist-1959` | fusionné dans la section des conseils de gouvernorat (troisième point) ; identifiant en ancre |
| `#sec-fl-hist-lois-1975`, liste des six lois | 1er plan, inchangée |
| idem, alinéa sur la loi organique des communes | 1er plan pour l'objet et la délégation spéciale ; la définition (art. 1) n'est plus redite à `_competences` |
| `#sec-fl-hist-1989` | fusionné dans « De 1975 à 2011 » (premier point) ; composition du conseil et patrimoine → replié ; identifiant en ancre |
| `#sec-fl-hist-modifications`, `tbl-fl-hist-modifs-communes` | le tableau → replié, avec une colonne « Portée » ; la phrase sur Dafflon et Gilbert reste au 1er plan |
| `TODO` (l. 68, quatre lois organiques à lire) | conservé, sous le bloc ; repris au ticket (§ 4, question 6) |
| `#sec-fl-hist-2011` et ancre `r-fl-dissolutions-2011` | 1er plan, section propre ; ancre conservée au même endroit |
| `#sec-fl-hist-2014`, alinéa de publication et ancre `r-fl-constitution-2014-numero-special` | 1er plan, conservés |
| idem, alinéa des art. 131 à 141 | 1er plan en quatre points ; les neuf appels → replié |
| idem, « Au regard des notions… » (l. 86) | 1er plan, fondu dans le premier point |
| `#sec-fl-hist-carte` : communes nouvelles, élections | 1er plan |
| `tbl-fl-hist-communes`, réserve et ancre `r-fl-nombre-communes` | **déplacés** à « La longue période : le nombre de communes » ; `docs/recherches.yml`, champ `ou` : `#sec-fl-hist-carte` → `#sec-fl-hist-longue-periode` |
| `#sec-fl-hist-code-2018`, 1er alinéa | 1er plan |
| idem, 2e alinéa (entrée en vigueur par étapes) | 1er plan, dans la sous-section des élections ; `_budgets` n'en garde que la conséquence |
| `#sec-fl-hist-2022` (2 alinéas) | 1er plan, resserrés ; articles → replié |
| `#sec-fl-hist-2023-2025` : trois décrets-lois, deux décrets, loi de 2025 | 1er plan en trois points ; détail des élections de proche en proche, mandats, districts → replié |
| idem, alinéa de 2025 : budget sous la loi de 1975, biens transférés à l'État | **cédés à `_competences`** (`#sec-fl-comp-conseils-2025`), qui les porte déjà |
| idem, réserve finale et ancre `r-fl-elections-municipales-apres-2023` | **cédées à `_competences`** (`#sec-fl-comp-dissolution-2023`), qui les porte déjà ; `docs/recherches.yml`, champ `ou` : l'entrée `_histoire.qmd#sec-fl-hist-2023-2025` est retirée |
| `#sec-fl-hist-longue-periode`, `tbl-fl-hist-chronologie` (8 lignes) | **remonté en vue d'ensemble**, réduit à cinq lignes ; les lignes de 1957 (loi n° 57-12), 1963 et 1989 → registres de leurs sections |
| idem, ligne de sources (dix clés) | → replié (registre des dates) |
| idem, dernière phrase (promesse) | remplacée par un renvoi (déjà fait sur la branche des budgets) |
| **Matière nouvelle** : décret-loi n° 2026-4 | section « 2026 », d'après la note de lectures du 9 octobre (§ D.5) ; une ligne au tableau de tête |
| **Matière nouvelle** : six décrets de l'automne 2011 | registre replié de la section 2011, **après lecture** (§ 4, question 1) ; rien avant |

### 3.2 `_competences`

| Élément actuel | Destination |
|---|---|
| Chapeau, l. 3 (quatre notions) | 1er plan, réduit à trois d'un mot ; la tutelle est rappelée à `_histoire` et à la section du contrôle |
| Chapeau, l. 5 (ordre du chapitre, édition arabe, règle de date) | ordre : récrit ; règle de date et éditions → replié, registre des dates |
| `#sec-fl-comp-communes-1975`, définition de la commune (art. 1, 2) | **cédée à `_histoire`** ; ici, une proposition |
| idem, « pas de liste », art. 36, Dafflon et Gilbert | 1er plan |
| idem, trois puces de tutelle (art. 12, 13, 38 à 46) | 1er plan : une phrase par puce ; la liste des douze matières et les délais → replié |
| idem, phrase sur les modificatifs (l. 21) et `TODO` (l. 23) | la phrase disparaît (elle dit ce que le chapitre ne fait pas ; l'information est à `_histoire`, « De 1975 à 2011 ») ; le `TODO` est conservé |
| `#sec-fl-comp-conseils-regionaux` | 1er plan pour les attributions et la « double casquette » ; statut et composition (art. 1, 6) **cédés à `_histoire`** ; nullité → replié |
| `#sec-fl-comp-categories` : définition du code, trois catégories | 1er plan |
| idem, quatre règles | 1er plan, sans appels |
| idem, pouvoir réglementaire (art. 25 à 28) | → replié |
| idem, constat et ancre `r-fl-loi-competences-partagees` | 1er plan, conservés |
| `#sec-fl-comp-commune`, `tbl-fl-comp-commune` | 1er plan, non replié |
| idem, pouvoir de fixer les droits (art. 237) | une proposition et `@sec-fl-moduler-droits` ; l'article va au registre, avec l'art. 139 (§ 4, question 4) |
| `#sec-fl-comp-region-district` | une phrase au 1er plan ; le reste → replié |
| `#sec-fl-comp-delegation-devolution` | 1er plan, inchangé |
| `#sec-fl-comp-organes`, 1er alinéa | 1er plan en trois points ; attributions détaillées → replié |
| idem, plafond des rémunérations (art. 9) | une proposition et renvoi à `_budgets` (§ 4, question 5) |
| idem, 2e alinéa (dissolution d'un conseil, art. 204) | fusionné avec la troisième ligne de `tbl-fl-comp-controle` ; le détail → replié |
| `#sec-fl-comp-instances` | 1er plan : attributions ; composition (art. 48, 63) → replié |
| `#sec-fl-comp-controle`, `tbl-fl-comp-controle` | 1er plan, non replié ; première ligne en renvoi |
| `#sec-fl-comp-agences`, modes de gestion (art. 80 à 83, 103, 104) | → replié |
| idem, caisse de prêts | une proposition et `@sec-fl-cpscl` ; le reste est déjà à `_transferts` |
| idem, formation (art. 43, 44, « au moins 0,5 % ») | 1er plan, un point : c'est une règle, non une donnée |
| idem, organismes nationaux et Dafflon et Gilbert | 1er plan |
| `TODO` (l. 125, agences et centre de formation) | conservé |
| `#sec-fl-comp-dissolution-2023` | 1er plan, récrit en état du droit ; la réserve et l'ancre `RECHERCHE` restent ici, seules du volume |
| `#sec-fl-comp-conseils-2025` | 1er plan en trois points (délibération, budget, biens) ; siège et décret n° 2025-177 → replié ; statut et abrogations **cédés à `_histoire`** |
| `#sec-fl-comp-longue-periode` | dissoute dans la vue d'ensemble (une phrase, un renvoi) ; identifiant en ancre |

### 3.3 `_notions`

| Élément actuel | Destination |
|---|---|
| Chapeau (3 alinéas) | 1er plan, moins deux phrases (§ 2.5) |
| Les 14 sous-sections, phrases de définition | 1er plan, inchangées |
| `tbl-fl-budget-decentralise`, `tbl-fl-tutelles`, `tbl-fl-types-subventions` | 1er plan, non repliés (`tbl-fl-tutelles` est appelé par `_competences`) |
| Les six formules et la définition de leurs symboles | 1er plan |
| Développements de Dafflon et Gilbert (conditions, nuances, classements, pratiques observées) | → repliés, cinq blocs (§ 2.5) |
| `#sec-fl-notations`, `tbl-fl-notations` | **supprimés** : les vingt symboles sont définis là où ils servent, mot pour mot ; seul le chapeau y renvoyait |

### 3.4 Le compte, avant et après

| Chapitre | Mots au premier plan, avant | Cible | Écart | D'où vient la baisse |
|---|---|---|---|---|
| `_notions` | 4 103 | 2 500 | − 39 % | notations − 210 ; chapeau − 60 ; développements repliés − 1 330 |
| `_histoire` | 3 337 | 1 950 | − 42 % | articles et visas repliés − 1 150 ; tableau de tête réduit − 130 ; chapeau − 80 ; ajout (2026) + 70 ; doublons cédés à `_competences` − 100 |
| `_competences` | 3 708 | 2 300 | − 38 % | histoire redite cédée − 620 ; organisation repliée − 760 ; région et district − 150 ; chapeau − 90 ; ajout (vue d'ensemble) + 200 |
| **Ensemble** | **11 148** | **6 750** | **− 39 %** | |

Ce qui plafonne la baisse : les définitions et les tableaux des notions (protégés), les trois
passages de doctrine des compétences (400 mots environ, laissés en place), les deux tableaux courts.

| Objet | Avant | Après |
|---|---|---|
| Tableaux au premier plan | 9 (53 lignes) | 8 (29 lignes) : `tbl-fl-notations` et `tbl-fl-hist-modifs-communes` sortent, `tbl-fl-comp-etats` entre |
| Blocs repliés | 0 | 28 : `_notions` 5, `_histoire` 11, `_competences` 12 |
| Lignes de registre (estimation) | 0 | 95 : `_histoire` 50, `_competences` 45 |
| Appels de citation de loi dans le fil | 135 environ | 0 |
| Identifiants de section | 59 | 58 conservés, dont 6 en ancre ; `sec-fl-notations` supprimé ; 5 nouveaux |
| `TODO`, `RECHERCHE` | 3 ; 6 | 3 plus la frise ; 5 (l'ancre des élections municipales, écrite deux fois, ne l'est plus qu'à `_competences`) |
| Longueur totale, registres compris | 11 148 | 13 000 à 14 000 (les registres ajoutent des lignes) |

---

## 4. Ce qu'il faut lire avant d'écrire (ticket du documentaliste, borné à une matinée)

1. **Dissolutions de 2011-2012.** Lire l'article 1er de chaque décret de dissolution — la vingtaine
   que la note d'histoire énumère au § 1.6, dont les six de l'automne 2011 (n° 2011-2407, JORT n° 74,
   p. 1988 ; 2011-2409, n° 74, p. 1990 ; 2011-2907, n° 78, p. 2164 ; 2011-3292, n° 84, p. 2444 ;
   2011-3388, n° 86, p. 2501 ; 2011-4253, n° 92, page à relever) — et **compter les communes**, sans
   reprendre de noms ; **relever leurs visas et leurs considérants** (ce que le décret dit chercher).
   Recompter les communes du décret n° 2011-383. Chercher dans les mêmes
   fascicules les décrets de nomination (n° 2011-2408, 2011-2410, 2011-2908, 2011-3293), qui n'ont
   pas de notice. Résultat attendu : un tableau date — décret — nombre de communes — page, et la
   mise à jour de `r-fl-dissolutions-2011`. **Tant que ce n'est pas fait, les six décrets n'entrent
   pas au chapitre** : une liste partielle tromperait, et une ligne sans contenu n'a pas sa place
   dans un registre.
2. **Ce que la loi cherche, en 2023 et en 2025** : rubriques ou considérants des décrets-lois
   n° 2023-9 et 2023-10 et de la loi organique n° 2025-4, mot pour mot (les deux « objet non
   relevé » de H3).
3. **Décret-loi n° 2026-4** : intitulés des titres et des chapitres ; articles 1 à 13 relus pour
   l'objet ; parmi les articles non lus (14 à 27, 35 à 56, 100 à 131), ceux qui disent ce que fait
   la commune et qui la contrôle. Dire s'il nomme le secrétaire général et les délégations spéciales.
4. **Art. 237 et art. 139 du code de 2018** : disent-ils la même chose (l'un pour le conseil
   municipal, l'autre pour toute collectivité) ? Une phrase de réponse, avec les deux citations.
5. **Art. 9 et art. 135 du code de 2018** : même question pour le plafond des rémunérations.
6. **Lois organiques n° 85-43, 91-24, 95-68 et 2006-48** : pour chacune, l'article qui touche
   l'élection du conseil, la tutelle ou le budget, avant → après. C'est le `TODO` de l'histoire ; à
   défaut, les quatre lignes restent au registre comme « connues par leur seul intitulé ».
7. **Dates d'effet non relevées** : loi municipale de 1957, loi n° 75-33 (rectificatif du 1er août
   1975 compris).
8. **La Haute instance des finances locales et le Conseil supérieur ont-ils fonctionné ?** La note
   de lectures du 9 octobre relève la nomination des membres de la Haute instance (JORT n° 31 de
   2019) et un décret sur leurs indemnités (n° 2020-31) : à lire, deux lignes.

Hors ticket, pour le bibliographe : une clé par décret de 2011 retenu au registre, la décision de
l'Assemblée constituante si elle manque, le décret-loi n° 2023-8. Pour le terminologue : les douze
notions sans entrée (§ 1.2).

---

## 5. Les arbitrages soumis au propriétaire

| # | Question | Recommandation | Ce que l'autre choix coûterait |
|---|---|---|---|
| A1 | **`_histoire` et `_competences` restent-ils deux chapitres, ou n'en font-ils qu'un ?** | **Deux**, avec la frontière du § 2.1 : l'histoire porte les réformes de tout le volume, que les chapitres de budgets, d'impôts et de transferts appellent ; les compétences en sont l'état du droit. | Un seul chapitre (« Les collectivités locales et leurs compétences ») suivrait le plan type de bout en bout et économiserait un chapeau, environ 150 mots. Il ferait une page de 23 blocs repliés, mêlerait les réformes du volume aux détails des compétences, et demanderait de renommer les renvois d'`index.qmd`. Aucun des deux n'est traduit : le livre arabe n'y perd rien. |
| A2 | **Les dissolutions de 2011 sont-elles une grande réforme ?** | **Non : une étape, avec sa section datée.** La délégation spéciale existe depuis la loi de 1975 (art. 13) ; les décrets de 2011 l'appliquent. Elle a sa ligne sur la frise et sa section, pas sa ligne au tableau de tête. À promouvoir si la lecture des décrets (§ 4, question 1) y trouve un objet nouveau, dit par leurs visas ou leurs considérants : c'est ce critère qui compte, non le nombre de communes. | La compter comme réforme donne six lignes au tableau, dont une qui repose sur deux décrets lus sur une vingtaine. |
| A3 | **Les notions restent-elles le chapitre 2 ?** | **Oui**, raccourcies de 39 %. C'est la demande du 4 octobre (« clarifier les concepts avant d'entrer dans le juridique »), le seul chapitre traduit en arabe, et 22 renvois y mènent. | En annexe, à côté du glossaire : le lecteur entre plus vite dans le droit, mais la demande du 4 octobre est renversée et le livre arabe perd son seul chapitre. Fondu dans la présentation : `index.qmd` passe de 640 à 3 000 mots. |
| A4 | **Dans les notions, les développements de Dafflon et Gilbert peuvent-ils être repliés ?** | **Oui** : définitions, tableaux et formules restent au premier plan ; nuances, conditions et classements passent dans cinq blocs titrés. Le texte principal se suffit, et rien ne change de section. | Tout garder visible : le chapitre ne perd que les notations et deux phrases (4 103 → 3 830 mots, − 7 %), et l'objectif de raccourcir n'est pas tenu pour lui. |
| A5 | **Le décret-loi n° 2026-4 entre-t-il comme grande réforme alors qu'il n'est pas en vigueur ?** | **Oui**, avec sa ligne au tableau, marquée « publié, non entré en vigueur » ; l'état du droit reste celui du 14 mars 2023 et se dit une seule fois. | L'attendre : le tableau s'arrête à 2025 et le lecteur apprend l'abrogation du code de 2018 au détour du chapitre des taxes. |
| A6 | **Convertit-on avant ou après le ticket du documentaliste ?** | **Le ticket d'abord pour les questions 1 à 5**, la conversion ensuite ; les questions 6 à 8 peuvent suivre. Les notions n'attendent rien : elles se convertissent tout de suite. | Convertir d'abord : la section de 2011 et les deux « objet non relevé » de 2023-2025 seraient à reprendre. |

Pris par défaut, à renverser au besoin : 1989 est une étape ; 2023 et 2025 forment une seule
réforme ; la Constitution de 2014 est le fondement du code de 2018, non une réforme à elle seule ;
les deux chapitres changent de titre (§ 2.3, § 2.4) ; l'ordre des chapitres est conservé.

---

## 6. Les risques du plan

- **La Constitution de 2014 sous le code de 2018** : un lecteur la cherche à sa date. Le titre de la
  sous-section la nomme, la frise la porte.
- **La tutelle de 1975 repliée** : la liste des matières soumises à approbation est ce qui montre
  l'étendue du contrôle. Le texte principal doit en nommer quatre (budget, emprunts, taxes et
  droits, aliénations).
- **La région et le district repliés** : ils reviendraient au premier plan si un texte les
  rétablissait ; le titre du bloc dit « abrogées en 2025 ».
- **L'histoire sans état du droit** : le lecteur qui n'ouvre qu'elle doit y lire, en vue d'ensemble
  et en dernière phrase, qu'aucune commune n'a de conseil élu depuis le 14 mars 2023, avec le renvoi.
- **Les notions repliées en PDF** : le bloc y reste visible tel quel ; le chapitre imprimé ne
  raccourcit pas.
- **Dépendance à la branche des budgets** : elle touche déjà `index.qmd`, `_histoire.qmd` (l. 156)
  et `_competences.qmd` (l. 149), et peut renommer les sections que ce plan vise (`@sec-fl-budg-ccl-principes`, `-ccl-controle`,
  `-2025`, `-longue-periode`). Convertir après sa fusion, ou
  sur une branche empilée.
- **Aucun autre volume ne vise ces trois chapitres** (recherche des identifiants et des noms de
  fichier sur tout `precis/fr` ; la seule réponse hors du volume, dans
  `cotisations_sociales/_regimes.qmd`, vise le chapitre d'histoire d'un autre livre).

---

## 7. Ordre de travail et volume pour le rédacteur

| Ordre | Travail | Dépend de | Volume estimé |
|---|---|---|---|
| 1 | `_notions` : chapeau, cinq blocs repliés, suppression des notations | rien | une demi-heure ; aucun registre |
| 2 | Ticket du documentaliste, questions 1 à 5 | — | une matinée (la question 1 en prend la moitié) |
| 3 | `_histoire` : réorganisation, onze blocs, 50 lignes de registre, section 2026 | 2 ; fusion de la branche des budgets | une heure et demie, puis une demi-heure pour le domicile unique |
| 4 | `_competences` : réorganisation, douze blocs, 45 lignes de registre, tableau de tête | 3 (les cessions vont dans les deux sens) | une heure et demie, puis une demi-heure |
| 5 | `index.qmd`, `docs/recherches.yml` (deux champs `ou`), `docs/notes/backlog-precis.md`, `TODO` de `_transferts` l. 199 | 3, 4 | un quart d'heure |

Liste de contrôle : copie de départ hors du dépôt et mesures du § 1.1 refaites ; réorganiser, ne pas
récrire ; aucun fait nouveau hors des notes et du ticket ; `scripts/check_domicile_references.py` ;
`uv run python scripts/recherches.py verifier` ; `scripts/check_numerotation.py` (les deux sections
de niveau 3 qui portent des sous-sections en ont deux chacune) ; `scripts/verifier.sh --sans-reseau
finances_locales` ; rendu ouvert dans le navigateur sur `#sec-fl-hist-vue-ensemble`,
`#sec-fl-comp-vue-ensemble` et `#sec-fl-decentraliser`.
