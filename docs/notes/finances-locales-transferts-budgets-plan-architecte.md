# Finances locales — transferts, budgets et dissolution de la longue période : fiche de plan de l'architecte

Rendue le 9 octobre 2026. Chapitres lus dans leur état de `master` :
`precis/fr/finances_locales/_transferts.qmd` (138 lignes), `_budgets.qmd` (171 lignes),
`_longue_periode.qmd` (268 lignes). Notes : `finances-locales-transferts.md`,
`finances-locales-budgets.md`, `fiscalite-locale-plan.md`. Aucun texte de loi n'a été relu : tout ce
qui est classé ici vient des notes et des chapitres, avec leur degré de certitude.

Une autre fiche, `finances-locales-impots-plan-architecte.md`, couvre les trois chapitres d'impôts.
Lue en fin de travail, dans un état encore en cours d'écriture, elle converge avec celle-ci sur
quatre points : la figure du rendement des impôts est scindée (elle prévoit
`fig-fl-immeubles-rendement` et `fig-fl-immeubles-recouvrement`) ; ses chapitres renvoient à
`@tbl-fl-lp-sources`, qui doit donc garder son identifiant ; les tables de notations
disparaissent ; `@sec-fl-fccl-2018` reste la cible du renvoi vers les fonds. Les destinations qui
tombent dans ses chapitres restent marquées **à concilier avec la fiche impôts**.

Les mots « cœur », « épine », « fiche » sont des mots de travail ; ils ne paraissent dans aucun
chapitre.

---

## 1. Le constat

### 1.1 Mesures de départ (à refaire sur une copie gardée hors du dépôt avant de convertir)

| Chapitre | Mots | Appels de citation | Clés distinctes | Ancres de glossaire | Identifiants | `TODO` | `RECHERCHE` | Tableaux | Lignes de tableau | Figures | Formules |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `_transferts` | 3 207 | 45 | 21 | 9 | 18 | 8 | 1 | 3 | 18 | 0 | 1 |
| `_budgets` | 4 020 | 84 | 25 | 11 | 20 | 4 | 2 | 5 | 31 | 0 | 0 |
| `_longue_periode` | 4 031 | 39 | 12 | 2 | 13 | 2 | 0 | 3 | 26 | 6 | 2 |
| **Ensemble** | 11 258 | 168 | — | 22 | 51 | 14 | 3 | **11** | **75** | **6** | 3 |

Tableaux, avec leur nombre de lignes de données : `tbl-fl-fccl-prelevements` 5 ;
`tbl-fl-fccl-repartition` 7 (sur 7 colonnes de dates) ; `tbl-fl-transferts-notations` 6 ;
`tbl-fl-budg-modifications` 4 ; `tbl-fl-budg-nomenclature` 5 ; `tbl-fl-budg-seuils` 11 ;
`tbl-fl-budg-art135` 7 ; `tbl-fl-budg-controle` 4 ; `tbl-fl-lp-sources` 7 ; `tbl-fl-lp-ecarts` 9 ;
`tbl-fl-lp-notations` 10.

### 1.2 `_transferts` : ce qui noie le lecteur

- **Aucune figure, aucun montant suivi.** Le chapitre des transferts ne dit pas ce que pèse le
  fonds : son seul chiffre de montant est la subvention de 1990 (80 MD), isolée, et sa « longue
  période » (l. 121-125) renvoie tout au dernier chapitre du volume. Les séries existent pourtant
  (crédit global, réserve, quotes-parts, 2008-2019 ; caisse de prêts, 2005-2024).
- **Sept réformes sur le même plan** (« Les réformes, une à une », l. 47-101) : la fin des parts
  d'impôts (1987) et l'entrée de la péréquation (2001) y ont le même rang que le tiers de la part de
  Tunis affectable au fonctionnement (1985).
- **Trois objets mêlés dans chaque paragraphe** : le partage entre collectivités et ses critères, la
  réserve et ses bénéficiaires, les prélèvements annuels des lois de finances. La réserve n'a pas de
  section à elle : son histoire est dispersée sur cinq sous-sections (l. 31, 51, 57, 73-75, 85, 89).
- **Des pourcentages en rafale dans la prose** (l. 23-31, 51, 83-89), que le tableau de synthèse
  redonne plus loin (l. 105-115).
- **Trois endroits disent ce que le chapitre ne fait pas** (l. 13, 75, 93), et la l. 75 se répète
  (« de 1993 à 2013 ; ceux de 1993 à 2013 »).
- **Aucun registre** : 45 appels de citation dans le fil des phrases.

### 1.3 `_budgets` : ce qui noie le lecteur

- **Aucune donnée.** La « longue période » (l. 169-171) tient en deux phrases de promesse. Le
  chapitre énonce des plafonds (rémunérations ≤ la moitié des recettes du titre I, art. 135) sans
  jamais montrer où se situent les communes ; la série existe (rémunérations et recettes du titre I,
  2008-2019).
- **La procédure avant l'économique.** Calendriers (fin mai, troisième session, 31 octobre, 30 juin,
  10 septembre, 1er décembre, 5 avril, 31 juillet…), renumérotation des articles en 2007, délais de
  transmission : ces précisions occupent le premier plan sur une quarantaine de lignes (l. 21-25, 64,
  68, 132-136, 153).
- **L'ordre n'est pas chronologique** : le seuil d'approbation (1975-2017, l. 70-98) est intercalé
  entre la refonte de 2007 et le code de 2018.
- **Quatre ruptures nettes, non hiérarchisées** : elles se devinent sous les titres, mais les quatre
  retouches de 1979-1997 et les onze décrets de seuil ont le même poids visuel.
- **84 appels de citation dans le fil**, dont une soixantaine d'« art. … » du code.

### 1.4 `_longue_periode` : ce qui noie le lecteur

- **Les chiffres sont loin des règles** : le lecteur du fonds commun doit changer de chapitre pour en
  voir le montant ; celui de la taxe sur les immeubles bâtis aussi.
- **Les sources avant les grandeurs** : le chapitre s'ouvre sur sept sources et trois ruptures de
  série (l. 7-29) avant toute figure.
- **Un tableau d'écarts de neuf lignes** (l. 237-249) sur le même plan que les résultats.
- **Deux faits racontés deux fois** avec `_transferts` : la réserve à 18 % et la quote-part
  communale de 70,4 à 70,7 % (LP l. 146 ; transferts l. 125) ; la divergence de 1990, 80 / 82 /
  50,8 MD (LP l. 163-170, 174, 245 ; transferts l. 123).
- **Un paragraphe local sur les bases du PIB** (l. 29) que l'annexe du site remplace, et une phrase
  (l. 73) qui traverse trois bases sans le dire (constat déjà inscrit dans `backlog-precis.md` et
  `annexe-pib.md`, lignes 21-25).

---

## 2. `_transferts` : frontière, ruptures, plan cible

### 2.1 La frontière

- **Les règles de base** : le fonds commun des collectivités locales — d'où vient l'argent
  (alimentation, montant), comment il se partage entre collectivités (parts des communes et des
  conseils), selon quels critères. Sans cela il n'y a pas de transfert.
- **Dispositions secondaires**, chacune sa section :
  - **la réserve du fonds** (le « solde ») : la fraction attribuée hors critères à des bénéficiaires
    désignés — elle aménage le fonds pour quelques collectivités et organismes ; elle a sa propre
    histoire (loi, puis décret, puis plafonds légaux) ;
  - **la caisse des prêts et de soutien des collectivités locales** : autre instrument, autre
    financement (prêts, subventions d'investissement), né le même jour que le fonds.
- **Ajustements annuels**, repliés : les prélèvements des lois de finances sur les crédits du fonds
  (1987-1991).
- **Hors du plan tant qu'ils ne sont connus que par leur intitulé** : le fonds de coopération de 2013,
  le fonds de 2021, les dotations du code de 2018. Ils gardent le paragraphe qu'ils ont, sans section.

### 2.2 Les ruptures retenues

Trois ruptures tiennent sur un article lu. C'est peu, et c'est assumé : les autres textes relèvent
des niveaux ou règlent la réserve.

| # | Rupture | Texte et article (lecture selon la note) | Date d'effet | Ce que la loi cherche, dans ses mots | Avant → après |
|---|---|---|---|---|---|
| T1 | **Mise en place** : un fonds unique et une caisse | loi n° 75-36, art. 1 à 3 et 5 (FR lue à l'image) ; loi n° 75-37, art. 1 à 4 et 6 (FR lue à l'image) | 1er janvier 1976 | intitulés : loi « relative au fonds commun des collectivités locales » ; loi « portant transformation de la caisse des prêts aux communes en une caisse des prêts et de soutien des collectivités locales » ; art. 1 : deux fonds fusionnés en « un seul fonds spécial » | deux fonds spéciaux de 1948 et une caisse des prêts aux communes de 1902 → un fonds alimenté par des parts d'impôts d'État, partagé par la loi ; une caisse qui prête et subventionne |
| T2 | **Un autre financeur** : la subvention du budget remplace les parts d'impôts | loi de finances pour 1987, art. 92 (FR lue à l'image) | gestion 1987 | **objet non relevé** : la note ne donne pas la rubrique de l'article ; le texte cité dit seulement que les impôts affectés aux fonds spéciaux « reviennent au profit du budget général de l'État » | ressources = pourcentages de six impôts d'État → montant inscrit chaque année au tableau des fonds spéciaux de la loi de finances |
| T3 | **Un public nouveau** : une part réservée aux communes dont les recettes fiscales sont inférieures à la moyenne | loi n° 2000-60, art. 1 (FR et AR lues à l'image) | 1er janvier 2001 | **objet non relevé** : l'intitulé dit « modifiant la loi n° 75-36 » ; l'article désigne le public (« communes dont la moyenne… est inférieure à celle de l'ensemble des communes ») sans nommer l'objectif | communes : 10 % égalité, 45 % population, 45 % propriété bâtie → 10 / 45 / 41 % et 4 % pour ces communes ; conseils : part égale 15 → 25 % |

**Étape de T3** : loi de finances pour 2014, art. 12, rubrique « Rationalisation des critères de
répartition du fonds commun » (« ترشيد مقاييس توزيع المال المشترك للجماعات المحلية »), 1er janvier
2014 : part réservée 4 → 8 %, part selon la taxe sur les immeubles bâtis 41 → 37 %.

**Le terme, qui n'est pas classé rupture en l'état** : loi de finances pour 2018, art. 11 —
suppression du compte et abrogation de la loi n° 75-36. La note et le chapitre n'en connaissent que
l'intitulé, et la date d'effet n'est pas relevée : ce texte a sa ligne de registre, signalée comme
telle, et sa section (le lecteur doit savoir que le fonds a disparu), mais il ne porte pas une
rupture tant que l'article n'est pas lu. **Première question au documentaliste** (§ 9). Conséquence :
**l'état du droit d'aujourd'hui n'est pas établi** ; il ne s'écrit pas. La section finale dit ce qui
est su : le fonds est supprimé par la loi de finances pour 2018 ; les budgets des communes de 2022 et
2023 portent une « dotation annuelle ».

**Ruptures propres à la réserve** (dans sa section) :

| # | Rupture ou étape | Texte | Effet | Avant → après |
|---|---|---|---|---|
| R1 | point de départ : parts fixées par la loi | loi n° 75-36, art. 3 | 1er janvier 1976 | 25 % du fonds : Tunis 5 %, caisse 6 %, quatre grandes communes 4 %, Office national de l'assainissement 8 %, District de Tunis 2 % |
| R2 | étape, **à promouvoir en rupture propre après relecture** : l'attribution passe de la loi au décret annuel | loi de finances pour 1992, art. 80, rubrique « Distribution du solde du fonds commun » — **lue par océrisation seulement** ; corroborée par la loi n° 95-45, art. 1 (lue en texte : « fixées par décret ») et par le visa du décret n° 92-308 | gestion 1992 | pourcentages fixes → répartition par décret entre six bénéficiaires ; une partie peut rejoindre la part des communes |
| R3 | étape : la réserve réduite et recentrée | loi de finances pour 2007, art. 11, rubrique « Révision des critères de répartition du fonds commun » | 1er janvier 2007 | 25 → 18 % ; sept bénéficiaires → quatre (sortent le District, l'Office de l'assainissement, l'Office de la protection civile) |
| R4 | étape : des plafonds légaux par bénéficiaire | loi de finances pour 2014, art. 12 | 1er janvier 2014 | décret libre → plafonds de 24, 3, 30, 27 % et 16 % « aux exigences de l'autorité de tutelle centrale » |

R2 repose sur une lecture que la note marque [OCR] : elle est classée **étape** par défaut, et
la colonne « Portée » dit « étape ». La relecture à l'image (question au documentaliste) la
promeut en rupture propre à la réserve : c'est le seul moment où la décision passe de la loi au
gouvernement.

### 2.3 Les lectures concurrentes (à trancher : arbitrage A1)

- **2007, la part des collectivités portée de 75 à 82 %.** *Lecture retenue* : étape — elle relève
  un niveau (quote-part des communes 64,5 → 70,5 % du fonds, conseils 10,5 → 11,5 %) sans changer
  de public ni d'objectif pour le partage ; la rubrique de l'article ne dit que « Révision des
  critères ». *Lecture concurrente* : grande réforme — c'est le plus gros déplacement d'argent de
  l'histoire du fonds, et la réserve cesse de financer trois organismes qui ne sont pas des
  collectivités. Dans le plan retenu, 2007 est racontée en une phrase chiffrée entre 2001 et 2014,
  figure dans la vue d'ensemble (point 2) et dans le tableau de la répartition, et a sa ligne dans
  la section de la réserve.
- **1982, la part égale.** *Lecture retenue* : ajustement des critères (rubrique « Finances
  locales », sans objet dit). *Lecture concurrente* : un critère nouveau, donc un objectif nouveau
  (un plancher par collectivité) — mais la loi ne le dit pas, et la note non plus.

### 2.4 Le plan cible, section par section

`.domicile-unique` sur le titre de niveau 1 du chapitre, comme à la TVA et comme le prévoit la
fiche impôts ; les registres portent des ancres `[]{#r-fl-tr-…}` (`r-fl-budg-…` au chapitre des
budgets). Convention commune aux deux fiches : l'identifiant d'une section qui disparaît devient
une ancre `[]{#…}` à l'endroit où son contenu arrive.

**Chapeau** (sans titre). Garde les deux premiers paragraphes (l. 3 et 5, notions et définition). Le
guide de lecture (l. 7) est récrit : il annonce ce que le chapitre donne — le montant du fonds et
qui le reçoit ; sa mise en place ; trois réformes ; la répartition légale de 1976 à 2017 ; la
réserve ; la caisse ; les séries.

**`## Vue d'ensemble {#sec-fl-transferts-vue-ensemble}`** (nouvelle)
- *Essentiel* : de 1976 à 2017, l'État verse aux collectivités, par le fonds commun, une dotation
  dont elles disposent librement et que la loi répartit selon la population, une part égale, le
  rendement de l'impôt foncier et, depuis 2001, la faiblesse des recettes fiscales ; à côté, une
  caisse leur prête et subventionne leurs investissements.
- *Vue d'ensemble* : **la figure `fig-fl-lp-fccl`** (montée de la longue période, étiquette
  conservée), puis un **tableau court des réformes** (trois lignes T1 à T3 et la ligne du terme de
  2018 ; colonnes : réforme — date d'effet — ce que la loi cherche — avant → après ; pas de
  citation, liens `#r-…`).
- *Points* (trois) : (1) le montant — le crédit global du fonds passe de 162 MD en 2008 à 394 MD en
  2017, dont 114 puis 278 MD de quote-part des communes ; dit à part, parce que ce n'est pas la
  même grandeur : la dotation annuelle inscrite aux budgets des communes, fonctionnement et
  investissement, est de 591 MD en 2022 et de 611 MD en 2023 ; (2) qui reçoit —
  depuis 2007, 70,5 % aux communes, 11,5 % aux conseils régionaux, 18 % à la réserve, ce que les
  agrégats confirment à l'arrondi près ; (3) ce que cela pèse dans les recettes de fonctionnement
  des communes — renvoi, en une phrase chiffrée, à la figure des recettes propres et des transferts
  du chapitre des budgets.
- *Replié* : rien.

**`## La mise en place, 1975-1976 {#sec-fl-transferts-1975}`**
- *Essentiel* : deux lois du 14 mai 1975 créent, au 1er janvier 1976, un fonds unique alimenté par
  des parts d'impôts d'État et une caisse de prêts et de soutien.
- *Premier plan* : ce avec quoi la loi rompt (les deux fonds de 1948, la caisse de 1902 — contenu de
  l'actuelle section « Les origines », en un paragraphe) ; l'alimentation en une phrase (des parts
  de six impôts d'État, de 3 à 50 % selon l'impôt) ; le partage (trois quarts aux collectivités,
  dont 20 % aux conseils et 80 % aux communes ; un quart de réserve) ; **la formule de la
  quote-part $F_j$**, avec ses symboles définis sur place ; l'annonce, une ligne chacune, de la
  réserve et de la caisse, avec renvoi à leur section.
- *Sous-sections* : `### Avant 1975 : deux fonds et une caisse {#sec-fl-transferts-origines}` ;
  `### Le fonds commun {#sec-fl-fccl-1975}`. (La caisse quitte cette section : voir sa section.)
- *Replié* :
  - « Fonds commun des collectivités locales : impôts d'État affectés et taux de prélèvement,
    1976-1986 » — tableau de six lignes tiré de la liste l. 25-29 (impôt — part affectée) ;
  - « Fonds commun et caisse de prêts : textes fondateurs de 1975 et textes antérieurs qu'ils
    visent » — registre (loi n° 75-36, loi n° 75-37, décret de 1948, décrets de 1902 et 1932 connus
    par les lois de 1975).

**`## Les grandes réformes {#sec-fl-fccl-reformes}`**
- *En tête* : une phrase d'entre-temps — de 1982 à 1986, la loi ajoute une part égale entre
  bénéficiaires et porte la part des communes de 80 à 86 % ; renvoi au registre.
- **`### 1987 : la subvention du budget remplace les parts d'impôts {#sec-fl-fccl-1987}`**
  - *Essentiel* : à partir de 1987, le fonds ne reçoit plus un pourcentage d'impôts ; son montant
    est inscrit chaque année dans la loi de finances.
  - *Points* : ce qui change pour les collectivités (une ressource indexée sur des impôts → un
    crédit voté) ; les prélèvements que chaque loi de finances autorise sur ce crédit, en une
    phrase ; renvoi à la longue période pour les montants.
  - *Replié* : « Fonds commun des collectivités locales : prélèvements autorisés par les lois de
    finances au profit de la caisse de prêts, de la protection civile et des agents, montants par
    gestion, 1987-1991 » (`tbl-fl-fccl-prelevements`, cinq lignes, inchangé).
- **`### 2001 : une part pour les communes aux recettes fiscales inférieures à la moyenne {#sec-fl-fccl-2001-2007}`**
  - *Essentiel* : depuis 2001, une fraction de la part des communes ne va qu'à celles dont les
    recettes fiscales moyennes sont inférieures à celles de l'ensemble ; c'est une péréquation des
    ressources au sens du chapitre des notions.
  - *Points* : le critère (quatre recettes, moyenne triennale, partage selon la population) ; la
    part égale des conseils 15 → 25 % ; l'étape de 2014 (4 → 8 %, immeubles bâtis 41 → 37 %), avec
    la rubrique de la loi citée ; une phrase d'entre-temps sur 2007 (75 → 82 %, quote-part des
    communes 64,5 → 70,5 %).
  - *Replié* : rien de propre ; renvoi au registre général.

**`## La répartition légale du fonds, 1976-2017 {#sec-fl-transferts-textes}`**
- *Essentiel* : en quarante-deux ans, la part des collectivités passe des trois quarts à 82 % du
  fonds, celle des communes de 60 à 70,5 % ; le dernier état est celui du 1er janvier 2014.
- *Premier plan* : **`tbl-fl-fccl-repartition`**, non replié (il dit le dernier état légal et la
  lecture de la figure en dépend). Deux corrections de forme : ajouter la colonne de 1992 (la
  réserve attribuée par décret y commence, non en 1995) ou retirer la ligne « Réserve » au profit
  de la section de la réserve ; sortir la ligne « Texte » en liens `#r-…`.
- *Replié* : « Fonds commun des collectivités locales : ressources, partage et critères — textes,
  date par date, 1975-2018 » — **le registre du chapitre**, avec colonne « Portée » (classement du
  § 2.5), ancres `r-fl-tr-…`, la ligne de 2018 signalée « seul l'intitulé de cet article est connu
  ici ».
- Les deux `TODO` (rédacteur : tableau engendré ; documentaliste : montant loi de finances par loi
  de finances) restent ici.

**`## Depuis 2018 : le fonds supprimé {#sec-fl-fccl-2018}`**
- *Essentiel* : la loi de finances pour 2018 supprime le compte du fonds et abroge la loi de 1975 ;
  les budgets des communes portent ensuite une dotation annuelle.
- *Premier plan* : le paragraphe actuel (l. 93), sans date d'effet (elle n'est pas relevée) ; la
  dotation annuelle de 2022 et 2023 (fait unique, ici) ; les deux fonds de nom voisin (l. 95),
  inchangés ; la réserve de 15 % des agrégats de 2018-2019, dont le fondement n'est pas identifié.
- *Replié* : rien. Les trois `TODO` documentaliste (l. 97, 99, 101) restent ici.
- **Pas de section « état du droit aujourd'hui »** : il n'est pas établi.

**`## La réserve du fonds {#sec-fl-fccl-reserve}`** (identifiant conservé : la fiche
`r-fccl-repartition-reserve-2014-2017` de `docs/recherches.yml` le vise)
- *Objet, en tête* : la réserve — « le solde » de la loi de 1975 — est la fraction du fonds
  attribuée hors des critères généraux à des bénéficiaires désignés.
- *Vue d'ensemble* : tableau court R1 à R4 (quatre lignes).
- *Points* : qui décide (la loi, puis le décret annuel de 1992 à 2013, puis des plafonds légaux) ;
  qui reçoit (sept bénéficiaires, puis quatre en 2007 ; une ligne pour la tutelle en 2014) ; ce
  qu'elle pèse (25 puis 18 % ; 18 % observés de 2008 à 2017, 15 % en 2018-2019, renvoi à la
  figure) ; la répartition de 1992, seule connue (24 MD).
- *Replié* :
  - « Réserve du fonds commun : bénéficiaires et parts, textes date par date, 1976-2014 » —
    registre (lois de 1975, 1982, 1985, reconductions de 1988-1991, 1992, 1995, 2007, 2014) ;
  - « Réserve du fonds commun : répartition de la gestion 1992 par bénéficiaire, en dinars » — six
    lignes tirées de la l. 73 (décret n° 92-308), avec le `TODO` de relecture et celui des décrets
    de 1993 à 2013.
- L'ancre `RECHERCHE` (l. 77) reste dans cette section.

**`## La caisse des prêts et de soutien des collectivités locales {#sec-fl-cpscl}`** (nouvel
identifiant)
- *Objet, en tête* : la caisse prête aux collectivités et leur accorde des subventions
  d'investissement ; elle reçoit une part de la réserve du fonds et des dotations de l'État.
- `### L'institution, en 1975 {#sec-fl-cpscl-1975}` — le paragraphe actuel (l. 43), le lien entre
  prêt et subvention, le `TODO` des décrets (l. 45).
- `### Dotations, subventions, prêts et impayés, 2005-2024 {#sec-fl-lp-cpscl}` — **la figure
  `fig-fl-lp-cpscl`** et les trois paragraphes de la longue période (l. 180, 202, 204).
- *Replié* : « Caisse des prêts et de soutien : textes de 1975, article par article » (registre,
  deux ou trois lignes). La ligne d'écart sur les subventions et prêts de 2006-2009 devient une
  phrase de la seconde sous-section, ouverte par « Selon l'évaluation technique de la Banque
  mondiale de 2014 » (§ 4.4).

**`## La longue période {#sec-fl-transferts-longue-periode}`**
- *Essentiel* : aucune série ne couvre seule 1985-2023 ; trois sources se relaient, tracées à part.
- *Sous-sections* :
  - `### Le fonds et la dotation qui lui succède, 1985-2023 {#sec-fl-lp-fccl}` — le texte de la
    longue période (l. 146), qui ne porte que sur l'administration, renvoi à la figure de la vue
    d'ensemble ; puis, en paragraphe à part ouvert par « Selon les documents de la Banque mondiale
    de 2014 », l'écart sur 2008-2012 (112,2 à 176,3 MD contre 114 à 176 MD : ligne 4 du tableau des
    écarts, devenue phrase) ; **lieu unique** de la réserve
    à 18 % et de la quote-part de 70,4 à 70,7 % ;
  - `### Le montant de 1990 : trois chiffres {#sec-fl-transferts-1990}` — **lieu unique** de la
    divergence : d'abord le budgétaire (80 MD votés, loi de finances pour 1990), ensuite, titré
    comme tel, « selon les rapports de la Banque mondiale » (82 et 50,8 MD) ; la divergence n'est
    pas tranchée. La note de lecture de la figure s'aligne sur cette prudence (elle dit aujourd'hui
    « vraisemblablement… »).
- *En tête* : renvoi à la section des sources et de leurs ruptures du chapitre des budgets.
- *Replié* : rien de propre (voir § 4.4).

**Supprimé comme tableau** : `tbl-fl-transferts-notations` (six lignes). Motif : les six symboles ne
servent que dans une section, où ils sont déjà définis (l. 39) ; les chapitres convertis n'ont plus
de table de notations. L'information subsiste dans le texte de `#sec-fl-fccl-1975`.

### 2.5 Le classement des textes de la note

| Texte | Lecture | Dispositif | Portée |
|---|---|---|---|
| Décret du 25 juin 1948, art. 56-58 | objet connu par la loi n° 75-36 | fonds | antécédent (ligne signalée) |
| Décrets du 15 décembre 1902 et du 1er mars 1932 | objet connu par la loi n° 75-37 | caisse | antécédent (ligne signalée) |
| Loi n° 75-36, art. 1-5 | image | fonds ; réserve | **rupture T1** ; point de départ R1 |
| Loi n° 75-37, art. 1-6 | image | caisse | **rupture T1** (naissance groupée) |
| Arrêtés de 1975, 1977-1979, 1982-1983 (recettes et dépenses du fonds) | intitulé seul | fonds | hors registre du chapitre (non cités) ; au `TODO` |
| Lois de finances 1977-1979 (prélèvements) | intitulé seul | fonds | ajustements, ligne signalée si le rédacteur les cite ; sinon `TODO` |
| LF 1982, art. 27 | image | fonds ; réserve | ajustement (part égale) ; ajustement (Tunis 5 → 6 %, 3 % aux sièges de gouvernorat) |
| LF 1985, art. 63 | lu | réserve | ajustement |
| LF 1986, art. 68 | image | fonds | ajustement (conseils 20 → 14 %) |
| LF 1987, art. 92 | image | fonds | **rupture T2** |
| LF 1987, art. 44 et 94 ; LF 1988, art. 69-71 ; LF 1989, art. 100-102 ; LF 1990, art. 53-54 ; LF 1991, art. 79-80 | lu, montants de 1990-1991 par océrisation | fonds | ajustements annuels (prélèvements) |
| LF 1988, art. 72 ; LF 1989, art. 103 ; LF 1990, art. 55 ; LF 1991, art. 81 | lu | réserve | ajustements (reconduction) |
| LF 1990, tableau « L » | image | fonds | donnée budgétaire (80 MD), non un texte de réforme |
| LF 1992, art. 80 | océrisation | réserve | étape R2 ; rupture propre après relecture à l'image |
| LF 1992, art. 81 (dispense d'échéances) | océrisation | caisse | ajustement ; absent du chapitre, n'y entre pas sans relecture |
| Décret n° 92-308 | océrisation | réserve | étape (première répartition par décret) |
| Décrets n° 93-155 à 2013-1503 (22 textes) | intitulé seul | réserve | étapes (répartitions annuelles), connues par leur seul intitulé : au `TODO`, sans ligne tant qu'ils n'ont pas de clé |
| Loi n° 95-45 | texte | réserve | ajustement (un bénéficiaire de plus) |
| Loi n° 2000-60 | image | fonds | **rupture T3** |
| LF 2007, art. 11 | image | fonds ; réserve | étape (niveau) — lecture concurrente : rupture ; étape R3 |
| LF 2014, art. 12 | texte | fonds ; réserve | étape de T3 ; étape R4 |
| LF 2018, art. 11 | intitulé seul | fonds | terme, **ne porte pas de rupture en l'état** |
| LF 2013, art. 13-15 ; décret n° 2013-2797 ; LF 2021, art. 13 | intitulé seul | autres fonds | hors sujet du fonds commun ; paragraphe conservé, lignes signalées |
| Code des collectivités locales, articles sur les ressources transférées | non lus | — | à documenter d'abord |
| Décrets et arrêtés de la caisse (77-212 … 2021-505), loi n° 2001-56 | intitulé seul | caisse | au `TODO` |

---

## 3. `_budgets` : frontière, ruptures, plan cible

### 3.1 La frontière

- **Les règles de base** : ce qu'est le budget (deux titres), la règle d'équilibre, la place de
  l'emprunt, et qui contrôle le budget voté (approbation, puis juge financier).
- **Dispositions secondaires**, chacune sa section : le seuil de l'approbation ministérielle (un
  paramètre fixé par décret, onze fois) ; la nomenclature ; le comptable public et la reddition des
  comptes.
- **Replié** : calendriers, délais, renumérotation de 2007, liste des dépenses obligatoires, détail
  des recettes et dépenses de 1975.

### 3.2 Les ruptures retenues

| # | Rupture | Texte et article (lecture selon la note) | Date d'effet | Ce que la loi cherche, dans ses mots | Avant → après |
|---|---|---|---|---|---|
| B1 | **Mise en place** | loi n° 75-35 (lue), art. 3, 13, 16, 27, 28 | 1er janvier 1976 | intitulé : « loi organique du budget des collectivités publiques locales » ; art. 3 : « Chaque titre doit être équilibré en recettes et en dépenses » | dispositions budgétaires d'un décret de 1937 et des lois de 1961 et 1963 → un budget en deux titres, approuvé avant exécution par le gouverneur ou les ministres |
| B2 | **La refonte de 2007** : la dépense limitée aux recettes réalisées | loi organique n° 2007-65 (FR, texte), art. 1 (art. 3, 21 bis, 23 bis nouveaux), 2, 4, 6 | budget de 2008 | **objet non relevé** (intitulé : « modifiant et complétant » ; art. 1 nouveau : le budget s'inscrit « dans le cadre des objectifs du plan de développement économique et social ») | équilibre de chaque titre en prévision → dépenses ordonnancées limitées aux recettes « effectivement réalisées », engagements du titre I plafonnés, faute de gestion ; titres « gestion » et « développement » |
| B3 | **Le code de 2018** : plus d'approbation, la règle d'or écrite | loi organique n° 2018-29 (édition arabe, lue), art. 126, 131-135, 174-175, 182, 383 | exécutoire le 22 mai 2018 ; règles budgétaires des communes : budgets de 2019 | art. 126 : « la règle de l'équilibre réel du budget » ; art. 134 : « il n'est pas permis d'emprunter pour financer le budget de fonctionnement » ; art. 131 : faire des ressources propres la part la plus importante | approbation préalable par la tutelle → budget exécutoire, recours du gouverneur devant la chambre de la Cour des comptes ; plafonds de moitié sur les rémunérations et le remboursement du principal |
| B4 | **2025 : deux régimes** | loi organique n° 2025-4 (FR et AR), art. 5, 8, 10 | 18 mars 2025 | intitulé : loi « relative aux conseils locaux, conseils régionaux et conseils de districts » ; art. 8 : leur budget obéit à la loi n° 75-35 « dans la mesure où » elle n'est pas contraire | code pour toutes les collectivités (jamais appliqué aux régions) → code pour les communes, loi de 1975 pour les nouveaux conseils |

Étapes et ajustements : loi de finances pour 1980 (cinq parties : ajustement, lue par
océrisation) ; loi organique n° 85-44 (le délégué n'approuve plus : ajustement de B1) ; loi
organique n° 94-44 (crédits de programme : ajustement) ; loi organique n° 97-1 (renvoi au code de la
fiscalité locale : ajustement) ; arrêté du 31 mars 2008 (étape de B2) ; proclamations de l'ISIE de
mai-juin 2018 (étape de B3 : date d'application) ; onze décrets de seuil (ajustements, dans leur
section).

Lectures concurrentes. **2007** : faute d'objet relevé, la refonte peut se lire comme une étape de
B1 — même loi, même approbation préalable, des règles d'exécution plus strictes ; elle est retenue
comme grande réforme parce qu'elle récrit la loi entière et introduit un mécanisme absent de 1975
(la dépense bornée par l'encaissé, sanctionnée). **1985** pourrait se lire comme une rupture (un niveau de tutelle disparaît).
Non retenue : le contrôle reste une approbation préalable, seul son titulaire change pour les
petites communes.

### 3.3 Le plan cible, section par section

**Chapeau.** Garde le premier paragraphe (notions). Le second est scindé : « deux textes se
succèdent » monte dans la vue d'ensemble ; la convention de datation reste en une phrase.

**`## Vue d'ensemble {#sec-fl-budg-vue-ensemble}`** (nouvelle)
- *Essentiel* : le budget d'une collectivité est voté en deux titres, fonctionnement et
  investissement ; jusqu'en 2018 il ne s'exécute qu'approuvé par la tutelle ; depuis le code, il
  s'exécute sans approbation, sous le contrôle du juge financier, avec l'interdiction d'emprunter
  pour le fonctionnement.
- *Vue d'ensemble* : **la figure `fig-fl-lp-ressources`** (recettes de fonctionnement des communes :
  recettes propres et transferts ; étiquette conservée), précédée d'une phrase qui définit les deux
  grandeurs (recettes propres = recettes du titre I moins transferts de fonctionnement de l'État) ;
  puis le **tableau court des réformes** (B1 à B4).
- *Points* (quatre) : (1) l'équilibre — par titre en 1976, borné par les recettes réalisées en
  2008, « réel » et assorti de plafonds en 2019 ; (2) le contrôle — de l'approbation au recours ;
  (3) l'ordre de grandeur — recettes de fonctionnement des communes de 458 MD en 2008 à 1 169 MD en
  2019, 1 456 MD en 2023 selon la somme des budgets par commune ; (4) la part des transferts — un
  quart avant 2011, la moitié en 2011, 30 % en 2017.
- *Replié* : « Recettes propres et transferts des communes : définition des transferts de
  fonctionnement selon la source » (le détail par source de l'actuelle l. 41 de la longue période).

**`## La mise en place : la loi organique du budget de 1975 {#sec-fl-budg-1975}`**
- *Essentiel* : au 1er janvier 1976, le budget local a deux titres dont chacun doit être équilibré,
  et il n'est exécutoire qu'approuvé.
- `### Deux titres, chacun en équilibre {#sec-fl-budg-1975-texte}` — ce que la loi remplace ; les
  deux titres ; la contribution du titre I au titre II ; l'emprunt rangé parmi les « ressources
  propres » du titre II (le rapprochement avec le budget de référence des notions reste) ; les
  dépenses obligatoires en une phrase.
- `### L'approbation par la tutelle {#sec-fl-budg-procedure}` — qui approuve (gouverneur, ministres
  au-delà d'un seuil — renvoi à la section du seuil —, délégué en deçà) ; ce que la tutelle peut
  faire (rejeter, réduire, inscrire d'office, arrêter d'office) ; l'appréciation de Dafflon et
  Gilbert, laissée où elle est.
- *Replié* :
  - « Budget des collectivités locales sous la loi de 1975 : recettes, dépenses et dépenses
    obligatoires, article par article » ;
  - « Budget des collectivités locales sous la loi de 1975 : calendrier, vote, approbation et compte
    financier, article par article » (les délais et le compte financier des l. 21 et 25).

**`## Les grandes réformes {#sec-fl-budg-reformes}`**
- *En tête* : phrase d'entre-temps — quatre textes retouchent la loi entre 1980 et 1997 sans en
  changer l'équilibre ni le contrôle ; bloc replié : « Loi organique du budget des collectivités
  locales : modifications de 1979 à 1997, texte par texte » (`tbl-fl-budg-modifications`, quatre
  lignes, avec une colonne « Portée » ; le renvoi venu du chapitre d'histoire le déplie).
- **`### 2007 : la dépense limitée aux recettes réalisées {#sec-fl-budg-2007}`**
  - *Essentiel* : à partir du budget de 2008, une commune ne peut ordonnancer plus qu'elle n'a
    encaissé, et dépasser les recettes réalisées du titre I est une faute de gestion.
  - *Points* : les deux règles d'exécution ; les titres deviennent « gestion » et
    « développement », en onze parties et douze catégories (renvoi à la section de la
    nomenclature) ; l'« équilibre réel », que la loi ne définit pas selon Dafflon et Gilbert.
  - *Replié* : « Budget des collectivités locales dans la rédaction de 2007 : calendrier, douzièmes
    et renumérotation des articles » (l. 64 et 68).
- **`### 2018 : le code des collectivités locales {#sec-fl-budg-ccl}`**
  - *Essentiel* : le code supprime l'approbation du budget, écrit la règle d'or et plafonne les
    rémunérations et le remboursement de la dette.
  - `#### Principes et équilibre {#sec-fl-budg-ccl-principes}` — art. 126, 130-134 ; la règle d'or
    citée ; renvoi au tableau des règles de prévision (section de l'état du droit).
  - `#### De l'approbation au recours devant le juge financier {#sec-fl-budg-ccl-controle}` — **le
    tableau avant → après `tbl-fl-budg-controle`** (quatre lignes, non replié) ; le déficit
    d'exécution de plus de 5 %.
  - `#### Entrée en vigueur {#sec-fl-budg-ccl-vigueur}` — inchangé.
  - *Replié* : « Budget communal sous le code de 2018 : calendrier de préparation, de vote et de
    transmission, article par article » (l. 132, délais de la l. 134).
- **`### 2025 : deux régimes budgétaires {#sec-fl-budg-2025}`** — le paragraphe actuel (l. 165),
  avec son `TODO`.

**`## L'état du droit en mars 2025 {#sec-fl-budg-etat-du-droit}`** (nouvelle)
- *Essentiel* : deux régimes coexistent — le code pour les communes, la loi de 1975 dans sa
  rédaction de 2007 pour les conseils locaux, régionaux et de districts.
- *Premier plan* : **`tbl-fl-budg-art135`** (sept lignes, non replié : droit en vigueur) ; un renvoi
  à `tbl-fl-budg-controle`, qui se lit aussi comme le tableau des deux régimes ; le seuil en vigueur
  pour les budgets encore approuvés (18 MD depuis juin 2017, renvoi) ; la réserve, dite une fois :
  les budgets communaux sont préparés sans conseil élu depuis 2023.
- *Replié* : « Budget des collectivités locales : textes, date par date, 1975-2025 » — **le registre
  du chapitre**, avec colonne « Portée », ancres `r-fl-budg-…` ; les articles du code y sont
  regroupés par objet (principes, équilibre, nomenclature, calendrier, contrôle, comptes).

**`## Le seuil de l'approbation ministérielle {#sec-fl-budg-seuils}`** (identifiant conservé :
`r-lob-cl-seuil-approbation-apres-2017` le vise)
- *Objet, en tête* : sous la loi de 1975, le budget d'une commune dont les recettes dépassent un
  seuil fixé par décret est approuvé par les ministres de l'Intérieur et des Finances, non par le
  gouverneur.
- *Vue d'ensemble* : la suite des paliers dans une phrase (0,5 MD en 1976, 1 MD en 1977, 2 MD en
  1989, 4 MD en 1997, 6 MD en 2010, puis un relèvement presque chaque année jusqu'à 18 MD en juin
  2017) ; figure en escalier quand la série existera (§ 6).
- *Points* : l'assiette change deux fois (prévisions, réalisations en 1986, prévisions courantes en
  1989) ; le second seuil, celui du délégué (75 000 D), disparaît en 1985 ; l'agrément des
  investissements (100 000 et 50 000 D, décret n° 75-782), aujourd'hui noyé dans la procédure,
  vient ici.
- *Replié* : « Seuil de recettes au-delà duquel le budget communal est approuvé par les ministres :
  montants, assiette et décrets, date par date, 1976-2017 » (`tbl-fl-budg-seuils`, onze lignes,
  colonne « Portée » : point de départ puis ajustements). L'ancre `RECHERCHE` et les deux `TODO`
  restent ici.

**`## La nomenclature du budget {#sec-fl-budg-nomenclature}`** (nouvelle)
- *Objet, en tête* : la nomenclature range les recettes par catégories et les dépenses par parties ;
  les séries du chapitre se lisent dans celle de 2008.
- *Premier plan* : **`tbl-fl-budg-nomenclature`** (cinq lignes, non replié : la lecture des figures
  en dépend — catégories 6, 7 et 12) ; ce que le code change (six catégories au titre I, la
  sixième change d'objet, une section pour les fonds de concours) ; l'appréciation de Dafflon,
  laissée où elle est ; le décret de nomenclature non identifié.
- *Replié* : « Nomenclature du budget des collectivités locales : chapitres de 1975, parties de
  1980, arrêté de 2008, articles du code de 2018 ».
- **Attention** : l'ancre `RECHERCHE r-ccl-2018-nomenclature-art167` déménage ici ; le champ `ou:`
  de sa fiche (`docs/recherches.yml`, l. 1152) vise `#sec-fl-budg-ccl-principes` et doit être
  corrigé dans le même changement, sinon `recherches.py verifier` échoue.

**`## Comptable public et reddition des comptes {#sec-fl-budg-ccl-comptes}`**
- *Objet, en tête* : qui paie, qui tient les comptes, à qui ils sont rendus.
- *Premier plan* : le comptable public de l'État ; le compte arrêté par le conseil et transmis à la
  chambre de la Cour des comptes ; la publication des documents budgétaires ; sous la loi de 1975,
  le compte financier approuvé par la tutelle et le fonds de réserve (remonté de la l. 25).
- *Replié* : « Comptes des collectivités locales : dates de clôture, d'arrêt et de transmission,
  article par article ».

**`## La longue période {#sec-fl-budg-longue-periode}`**
- *Essentiel* : les séries disponibles portent sur les communes ; six sources se relaient de 1985 à
  2025, tracées séparément.
- `### Les sources et leurs ruptures {#sec-fl-lp-sources}` — **`tbl-fl-lp-sources`** (sept lignes,
  non replié : la lecture de toutes les figures du volume en dépend) ; le périmètre communal de
  2016 ; la fin du fonds commun (sans date d'effet, voir § 8) ; le tableau est réordonné —
  l'administration d'abord (Direction générale, caisse, Institut national de la statistique), les
  trois rapports de la Banque mondiale ensuite, sous un intertitre de ligne ; pour le PIB, **un renvoi à l'annexe
  du site** remplace le paragraphe local, et la phrase dit la base de chaque segment.
- `### Recettes propres et transferts {#sec-fl-lp-ressources}` — la formule $P_1 = R_1 - T_1$,
  $a_1 = P_1/R_1$, symboles redéfinis sur place. **Les paragraphes des l. 71 et 73 ne se recopient pas
  tels quels** : ils enchaînent la Banque mondiale et l'administration. D'abord un paragraphe sur
  les agrégats de la Direction générale (2008-2019) et la somme des budgets par commune
  (2018-2023) ; ensuite un paragraphe à part, ouvert par « Selon les rapports de la Banque
  mondiale », pour 1990-1996 et 2002-2010, avec la phrase qui dit leur accord ou leur écart avec
  l'administration sur 2008-2012. La phrase sur le PIB est récrite segment par segment (base 1983
  pour 2002, base 1997 pour 2008-2011, base 2015 pour 2019). Renvoi à la figure de la vue
  d'ensemble.
- `### L'autonomie financière {#sec-fl-lp-autonomie}` — formule $Q$, **figure
  `fig-fl-lp-autonomie`** ; texte repris (il ne commente que l'administration).
- `### Dépenses, rémunérations et service de la dette {#sec-fl-budg-depenses}` (nouvelle) — figure à
  créer (§ 6) : les rémunérations rapportées aux recettes du titre I, en regard du plafond de
  moitié ; le service de la dette. Remplace la promesse de la l. 171 et le `TODO` de la l. 251 de
  la longue période.
- `### Épargne et investissement dans les comptes de la nation {#sec-fl-lp-ins}` — **figure
  `fig-fl-lp-ins`**, texte inchangé.
- *Replié*, deux tableaux qui ne mêlent pas les familles (détail au § 4.4) :
  - « Finances des communes : écarts entre les agrégats de la Direction générale, la somme des
    budgets par commune et le tableau du ministère des Finances, 2010 et 2018-2019 »
    (`tbl-fl-lp-ecarts`, trois lignes) ;
  - « Finances des communes en 1990 selon la Banque mondiale : écarts entre le rapport de 1992 et
    celui de 1997 » (`tbl-fl-lp-ecarts-bm`, deux lignes).

### 3.4 Le classement des textes de la note

| Texte | Lecture | Dispositif | Portée |
|---|---|---|---|
| Décret de 1937, loi de 1961, loi de 1963 (abrogés par l'art. 27) | connus par la loi n° 75-35 ; dates mal lues | règles de base | antécédents (ligne signalée) |
| Loi n° 75-35 | lue | règles de base | **rupture B1** |
| Décret n° 75-485 | lu | seuil | point de départ |
| Décret n° 75-782 | image | seuil (agrément des investissements) | étape de B1 |
| Arrêté du 6 novembre 1975 (nomenclature) | intitulé seul | nomenclature | ligne signalée |
| Loi n° 75-38 (allègement de la dette) | intitulé seul | emprunt | hors chapitre aujourd'hui ; n'y entre pas |
| LF 1980, art. 38-41 | océrisation | nomenclature | ajustement |
| LF 1980, art. 37 (prêts autorisés par décret) | océrisation | emprunt | absent du chapitre ; n'y entre pas sans relecture |
| Décret n° 77-320 | image | seuil | ajustement |
| Loi organique n° 85-44 | image | contrôle | ajustement de B1 (lecture concurrente : rupture) |
| Décrets n° 86-1036, 89-280, 97-1837, 2010-3179, 2012-2475, 2013-3235, 2014-2232, 2015-1739, 2017-758 | lus | seuil | ajustements |
| Arrêté du 11 mai 1991 (conseils régionaux) | intitulé seul | nomenclature | absent du chapitre |
| Loi organique n° 94-44 | texte | crédits | ajustement ; date d'effet non établie |
| Loi organique n° 97-1 | texte | recettes | ajustement |
| Loi organique n° 2007-65 | texte | règles de base ; nomenclature | **rupture B2** |
| Arrêté du 31 mars 2008 | lu (modèles non lus) | nomenclature | étape de B2 |
| Loi n° 73-81 (comptabilité publique), loi n° 68-8 (Cour des comptes) | non lues | comptes | à documenter d'abord |
| Loi organique n° 2018-29, livre I, titre IV | édition arabe | toutes | **rupture B3** |
| Décisions de l'ISIE n° 2018-12 à 2018-361 | relevées | — | étape de B3 (date d'application) |
| Décret de nomenclature du code (art. 167) | non identifié (fiche de recherche) | nomenclature | — |
| Loi organique n° 2025-4 | FR et AR | règles de base | **rupture B4** |
| Décrets n° 2025-177 et 2025-178 | intitulé seul | — | hors sujet |
| Décret-loi n° 2023-9 | chapitre d'histoire | — | renvoi, `TODO` |

---

## 4. `_longue_periode` : destination, et suppression du chapitre

### 4.1 Les neuf sections et l'en-tête

| Section actuelle | Destination |
|---|---|
| En-tête (l. 1-5) | dissous ; ce qu'il annonce est redit par la vue d'ensemble de chaque chapitre d'accueil |
| Les sources et leurs ruptures `#sec-fl-lp-sources` | `_budgets`, « La longue période », sous-section du même identifiant ; les chapitres des transferts et des impôts y renvoient en tête de leur propre longue période |
| Recettes propres et transferts `#sec-fl-lp-ressources` | `_budgets` : figure en vue d'ensemble, formule et commentaire en longue période (identifiant conservé) |
| L'autonomie financière `#sec-fl-lp-autonomie` | `_budgets`, longue période (identifiant conservé) — autre lecture : `_taxes_redevances`, qui annonce ce ratio (arbitrage A2) |
| Le rendement des impôts locaux `#sec-fl-lp-impots` | **scindée**, à concilier avec la fiche impôts : taxe sur les immeubles bâtis, taxe sur les terrains non bâtis et taux de recouvrement → `_impots_immeubles` ; taxe sur les établissements et taxe hôtelière → `_impots_activite` ; l'identifiant devient une ancre dans le chapitre des immeubles (le seul renvoi entrant, depuis la table de notations, disparaît avec elle) |
| Le fonds commun et la dotation qui lui succède `#sec-fl-lp-fccl` | `_transferts` : figure en vue d'ensemble, texte en longue période (identifiant conservé) |
| La caisse de prêts et de soutien `#sec-fl-lp-cpscl` | `_transferts`, section de la caisse (identifiant conservé) |
| Le compte des collectivités locales dans les comptes de la nation `#sec-fl-lp-ins` | `_budgets`, longue période (identifiant conservé) |
| Les écarts entre sources `#sec-fl-lp-ecarts` | réparti par famille de sources (§ 4.4) : deux tableaux repliés à `_budgets`, quatre phrases dans les passages qui citent chaque rapport ; l'identifiant de section devient une ancre à `_budgets` |
| Notations `#sec-fl-lp-notations` | dissoute : chaque symbole est redéfini dans la sous-section qui l'emploie |

### 4.2 Les six figures

| Figure | Destination | Travail |
|---|---|---|
| `fig-fl-lp-ressources` | `_budgets`, vue d'ensemble | déplacer la cellule ; note de lecture : dire la base du PIB par segment |
| `fig-fl-lp-autonomie` | `_budgets`, longue période | déplacer |
| `fig-fl-lp-impots` | **scindée en deux** : `_impots_immeubles` (deux taxes, plus la vue du taux de recouvrement) et `_impots_activite` (deux taxes) — à concilier avec la fiche impôts | `figures/finances_locales.py` : `vues_impots()` et `table_impots()` reçoivent la liste des taxes ; deux étiquettes et deux `slug` nouveaux ; `figdata/fig_fl_impots.csv` remplacé par deux fichiers |
| `fig-fl-lp-fccl` | `_transferts`, vue d'ensemble | déplacer ; note de lecture : « le rapport de 1992 ne dit pas la base de son PIB » ; prudence sur 1990 |
| `fig-fl-lp-cpscl` | `_transferts`, section de la caisse | déplacer |
| `fig-fl-lp-ins` | `_budgets`, longue période | déplacer |

Les six cellules importent le même module (`figures/finances_locales.py`), dans le même livre : un
déplacement ne demande aucun changement de code, sauf la scission.

### 4.3 Ce qui resterait, et ce que la suppression demande

**Il ne reste rien** : le chapitre peut être supprimé. La suppression demande, dans le même
changement :

1. `precis/fr/finances_locales/_quarto.yml` : retirer `- _longue_periode.qmd`.
2. `precis/ar/finances_locales/_quarto.yml` : retirer la ligne commentée `# - _longue_periode.qmd`
   (à la main ; aucun `.qmd` arabe du chapitre n'existe).
3. `precis/fr/finances_locales/index.qmd`, l. 12 : le quatrième mouvement « Les chiffres » et son
   renvoi `@sec-fl-longue-periode` disparaissent — le volume a trois mouvements, et chaque chapitre
   porte ses chiffres ; l. 14 : « et celui de la longue période » à retirer (la phrase est d'ailleurs
   périmée : elle dit les chapitres des institutions « à écrire »). Relancer
   `scripts/check_numerotation.py`.
4. Renvois `@…` entrants (liste complète, par `grep` sur tout `precis/fr`) : `index.qmd` l. 12
   (`@sec-fl-longue-periode`) ; `_transferts.qmd` l. 93 (`@sec-fl-lp-fccl`), l. 125
   (`@fig-fl-lp-fccl`, `@fig-fl-lp-cpscl`, `@sec-fl-lp-fccl`). **Aucun autre volume, ni le
   glossaire, ni `docs/recherches.yml` ne visent ce chapitre.**
5. Renvois en prose « au chapitre de la longue période », à récrire en renvoi vers la section
   d'accueil : `_budgets.qmd` l. 171 ; `_histoire.qmd` l. 156 (→ `@sec-fl-budg-longue-periode`) ;
   `_competences.qmd` l. 149 (aucune série par fonction n'existe : la phrase dit le constat, sans
   promesse) ; `_impots_immeubles.qmd` l. 283, `_impots_activite.qmd` l. 209,
   `_taxes_redevances.qmd` l. 135 (à concilier avec la fiche impôts).
6. Renvois sortants du chapitre vers `@sec-fl-transferts-longue-periode` (l. 174) et
   `@sec-fl-fccl-2001-2007` (l. 146) : ils suivent le texte.
7. `docs/notes/backlog-precis.md` (l. 1900-1914 et 2027-2031) et `docs/notes/annexe-pib.md`
   (lignes 21 à 25 du tableau, l. 403-407) : mettre à jour le fichier d'accueil.
   `docs/notes/fiscalite-locale-plan.md` : une ligne disant que le chapitre 10 a été fondu.
8. `figdata/` : les `slug` sont inchangés, sauf `fig_fl_impots` (scission).

Seconde vérification, hors renvois `@` : aucun lien en clair, aucun `_quarto.yml`, aucune page du
site (`precis/fr/*.qmd`) ne cite `longue_periode` ou `fl-lp` en dehors des fichiers ci-dessus.

### 4.4 Le tableau des écarts : une famille de sources par tableau

La règle du précis — le budgétaire ne se mêle pas aux rapports extérieurs, pas dans le même
tableau — interdit de garder les neuf lignes ensemble. Répartition, ligne par ligne :

| Ligne de `tbl-fl-lp-ecarts` | Familles en présence | Destination |
|---|---|---|
| 1. Recettes du titre 1, 2018-2019 | administration des deux côtés | tableau replié « administration », `_budgets` |
| 2. Dépenses des titres 1 et 2, 2018-2019 | administration des deux côtés | idem |
| 5. Impôts et fonds commun, 2010 | tableau du ministère des Finances, connu par Dafflon et Gilbert, contre les agrégats : **classé administration**, la voie de transmission dite dans la cellule | idem (à faire confirmer : c'est une donnée administrative lue de seconde main) |
| 7. Fonds commun, 1990 | deux rapports de la Banque mondiale | tableau replié « Banque mondiale », `_budgets` ; la sous-section de 1990 du chapitre des transferts y renvoie |
| 8. Recettes courantes des communes, 1990 | deux rapports de la Banque mondiale | idem |
| 3. Budgets agrégés, 2008-2012 | rapport contre administration | phrase, `_budgets`, paragraphe « Selon les rapports de la Banque mondiale » de `#sec-fl-lp-ressources` |
| 4. Fonds commun, 2008-2012 | rapport contre administration | phrase, `_transferts`, `#sec-fl-lp-fccl` |
| 6. Taxe sur les immeubles bâtis, 2006-2007 | rapport seul | phrase, `_impots_immeubles`, longue période (à concilier avec la fiche impôts) |
| 9. Subventions et prêts de la caisse, 2006-2009 | rapport contre états financiers | phrase, `_transferts`, `#sec-fl-lp-cpscl` |

---

## 5. Le registre de destination

PP = premier plan ; R = bloc replié (titre au § 2.4 ou 3.3).

### 5.1 `_transferts`

| Élément actuel | Destination |
|---|---|
| l. 3, notions | PP, chapeau |
| l. 5, définition et critères | PP, chapeau, resserré ; le détail est dans la vue d'ensemble |
| l. 7, guide de lecture | récrit (annonce ce qui est présenté) ; la convention « désignée par la gestion » passe dans le registre |
| « Les origines » l. 9-15, `#sec-fl-transferts-origines` | PP, sous-section de la mise en place ; l. 13 récrite ; `TODO` conservé |
| l. 21, fusion et effet | PP, `#sec-fl-fccl-1975` |
| l. 23-29, ressources (cinq puces) | une phrase PP + R « impôts d'État affectés et taux de prélèvement, 1976-1986 » |
| l. 31, répartition | PP pour le partage ; les parts du solde → section de la réserve (R1) |
| l. 33-39, formule $F_j$ | PP, inchangée |
| `#sec-fl-cpscl-1975` l. 41-45 | déplacée dans la section de la caisse ; annonce d'une ligne dans la mise en place ; `TODO` conservé |
| `#sec-fl-fccl-1982-1986` l. 49-51 | fusionnée : phrase d'entre-temps + lignes du registre ; part de Tunis et sièges de gouvernorat → réserve ; identifiant gardé en ancre sur la phrase d'entre-temps |
| `#sec-fl-fccl-1987` l. 53-57 | PP ; le chiffre de 1990 → longue période (lieu unique) ; reconductions → réserve |
| `tbl-fl-fccl-prelevements` (5 lignes) + `TODO` l. 69 | R, dans 1987 |
| `#sec-fl-fccl-reserve` l. 71-79 | devient la section de la réserve ; montants de 1992 → R ; l. 75 récrite ; `RECHERCHE` et `TODO` conservés |
| `#sec-fl-fccl-2001-2007` l. 81-85 | PP pour 2001 ; 2007 : phrase d'entre-temps, point 2 de la vue d'ensemble, R3 de la réserve |
| `#sec-fl-fccl-2014` l. 87-89 | fusionnée : étape de 2001 et R4 de la réserve ; identifiant gardé en ancre sur l'étape de 2014 |
| `#sec-fl-fccl-2018` l. 91-101 | PP, section « Depuis 2018 » ; trois `TODO` conservés |
| `#sec-fl-transferts-textes`, `tbl-fl-fccl-repartition` (7 lignes), l. 117, `TODO` l. 119 | PP, section « La répartition légale » ; la l. 117 passe en colonnes de dates d'effet |
| `#sec-fl-transferts-longue-periode` l. 121-125 | PP ; l. 123 → sous-section de 1990 ; l. 125 remplacée par le texte venu de la longue période |
| `#sec-fl-transferts-notations`, `tbl-fl-transferts-notations` (6 lignes) | supprimés ; les définitions subsistent l. 39 |

### 5.2 `_budgets`

| Élément actuel | Destination |
|---|---|
| l. 3, notions | PP, chapeau |
| l. 5, deux textes, traduction, datation | scindé : vue d'ensemble ; une phrase de convention |
| `#sec-fl-budg-1975-texte` l. 11-17 | PP resserré ; détail des art. 4-7 et 10 → R |
| `#sec-fl-budg-procedure` l. 21-25 | PP pour qui approuve et ce que peut la tutelle ; délais → R ; compte financier → section des comptes ; agrément des investissements → section du seuil |
| `#sec-fl-budg-reformes` | devient « Les grandes réformes » |
| `#sec-fl-budg-1979-1997`, `tbl-fl-budg-modifications` (4 lignes), sources, `TODO` | phrase d'entre-temps + R ; identifiant de section gardé en ancre sur la phrase, tableau et `TODO` conservés |
| `#sec-fl-budg-2007` l. 48 | PP |
| l. 50, nomenclature, et `tbl-fl-budg-nomenclature` (5 lignes) | section de la nomenclature, PP |
| l. 64, procédure | R |
| l. 66, exécution | PP (c'est la rupture) |
| l. 68, renumérotation et équilibre réel | R pour la renumérotation ; PP pour l'équilibre réel et la remarque de Dafflon et Gilbert |
| `#sec-fl-budg-seuils`, `tbl-fl-budg-seuils` (11 lignes), sources, l. 94, `RECHERCHE`, deux `TODO` | section du seuil ; tableau R ; l. 94 récrite (état dit par sa date, juin 2017) |
| `#sec-fl-budg-ccl-principes` l. 104-106 | PP |
| `tbl-fl-budg-art135` (7 lignes) et l. 120-122 | PP, section de l'état du droit |
| l. 124-128, nomenclature du code, `RECHERCHE` | section de la nomenclature (corriger `ou:`) |
| `#sec-fl-budg-ccl-controle` l. 132 | R (calendrier) |
| l. 134-138 | PP |
| `tbl-fl-budg-controle` (4 lignes) | PP |
| `#sec-fl-budg-ccl-comptes` l. 153-155 | section des comptes ; dates → R |
| `#sec-fl-budg-ccl-vigueur` l. 159-161 | PP, inchangé |
| `#sec-fl-budg-2025` l. 165-167 | PP, dans les grandes réformes ; `TODO` conservé |
| `#sec-fl-budg-longue-periode` l. 169-171 | remplacée par le contenu venu de la longue période |

### 5.3 `_longue_periode`

| Élément actuel | Destination |
|---|---|
| `tbl-fl-lp-sources` (7 lignes), l. 9, 23 | `_budgets`, PP |
| l. 25-29, trois ruptures | `_budgets`, PP ; le paragraphe sur les bases → renvoi à l'annexe du PIB |
| Formule $P_1$, $a_1$ ; l. 33 et 41 | `_budgets`, longue période ; définitions par source → R |
| `fig-fl-lp-ressources` | `_budgets`, vue d'ensemble |
| l. 71 et 73 | `_budgets`, longue période ; l. 73 récrite par base |
| Formule $Q$, l. 77-85, `fig-fl-lp-autonomie`, l. 110 | `_budgets`, longue période |
| l. 114, `fig-fl-lp-impots`, l. 138-142 | `_impots_immeubles` et `_impots_activite` (à concilier) : l. 142 et les phrases sur les immeubles → immeubles ; la comparaison des quatre taxes (l. 138) → activité, avec renvoi ; l. 140 partagée par taxe |
| l. 146, `fig-fl-lp-fccl`, l. 174, `TODO` l. 176 | `_transferts` (le `TODO` double celui de la l. 69 : un seul subsiste) |
| l. 180, `fig-fl-lp-cpscl`, l. 202-204 | `_transferts`, section de la caisse |
| l. 208, `fig-fl-lp-ins`, l. 231 | `_budgets`, longue période |
| `tbl-fl-lp-ecarts` (9 lignes), l. 235 | § 4.4 : 3 lignes R (administration), 2 lignes R (Banque mondiale), 4 lignes devenues phrases |
| `TODO` l. 251 (dépenses, endettement) | `_budgets`, sous-section des dépenses ; levé si la figure est faite |
| `tbl-fl-lp-notations` (10 lignes) | supprimé ; définitions dans les sous-sections ; $\rho$ → `_impots_immeubles` |

### 5.4 Le compte, avant et après

| | Avant | Après |
|---|---|---|
| Tableaux existants | 11 | 9 conservés, dont celui des écarts scindé en deux : 55 lignes restent des lignes de tableau, 4 lignes d'écart deviennent des phrases ; 2 tables de notations (16 lignes) dissoutes dans le texte. Total : 55 + 4 + 16 = 75, rien de perdu |
| dont au premier plan | 11 | 5 : répartition (7), nomenclature (5), règles de prévision (7), contrôle (4), sources (7) |
| dont repliés | 0 | 5 : prélèvements (5), modifications (4), seuils (11), écarts de l'administration (3), écarts de la Banque mondiale (2) |
| Tableaux nouveaux, tirés de la prose ou des notes | — | courts : réformes des transferts (4), réserve (4), réformes des budgets (4) ; repliés : impôts affectés de 1976 (6), répartition de la réserve en 1992 (6), six à huit registres de textes |
| Figures | 6 | 5 déplacées telles quelles, 1 scindée en 2 (soit 7), plus 1 ou 2 à créer (§ 6) |
| Formules | 3 | 3 |
| `TODO` | 14 | 13 (un doublon réuni) ; un quatorzième levé si la figure des dépenses est faite |
| `RECHERCHE` | 3 | 3 (un champ `ou:` à corriger) |
| Identifiants de section | 51 | tous gardés ; deviennent une simple ancre `[]{#…}` là où leur contenu arrive (aucun n'a de renvoi `@` entrant hors des tables de notations) : `sec-fl-fccl-1982-1986`, `sec-fl-fccl-2014`, `sec-fl-transferts-notations`, `sec-fl-budg-1979-1997`, `sec-fl-longue-periode`, `sec-fl-lp-impots`, `sec-fl-lp-ecarts`, `sec-fl-lp-notations` ; créés : `sec-fl-transferts-vue-ensemble`, `sec-fl-cpscl`, `sec-fl-transferts-1990`, `sec-fl-budg-vue-ensemble`, `sec-fl-budg-etat-du-droit`, `sec-fl-budg-nomenclature`, `sec-fl-budg-depenses` |

Le texte grossira : compter 4 500 mots pour `_transferts` (3 200 aujourd'hui) et 7 500 pour
`_budgets` (4 000), l'apport de la longue période compris ; le premier plan des deux chapitres
devrait rester sous 6 500 mots au total.

---

## 6. Les figures à créer

| Figure | Chapitre | Série vérifiée | État |
|---|---|---|---|
| **Rémunérations rapportées aux recettes du titre I, et plafond de moitié** (`fig-fl-budg-remunerations`) | `_budgets`, longue période | `finances-locales-communes-agregats` : `remunerations` et `recettes_t1` (agrégats, 2008-2019, 12 points : 201 → 544 MD ; ratio publié `ratio_remunerations`, 0,43 à 0,50) ; `remunerations` (somme des communes, 2022 et 2023 seulement) | **faisable maintenant**, par une fonction de plus dans `figures/finances_locales.py`. Le plafond de l'art. 135 ne se trace qu'à partir de 2019 ; le ratio publié n'a pas de définition publiée : tracer le ratio calculé et le ratio publié à part, comme pour l'autonomie |
| **Dépenses des deux titres et service de la dette** (`fig-fl-budg-depenses`) | `_budgets`, longue période | même série : `depenses_t1`, `depenses_t2` (agrégats 2008-2019 ; somme des communes 2018-2023) ; `interets_dette`, `remboursement_principal`, `emprunts_interieurs` (2018-2023) ; `finances-locales-bm-1985-2012` : `depenses_t1`, `remboursement_capital`, `investissements` (2002-2012) | **faisable maintenant** ; sources tracées à part ; le plafond du remboursement (moitié du budget de fonctionnement) est loin au-dessus des valeurs observées — à dire en une phrase |
| Scission de `fig-fl-lp-impots` | chapitres d'impôts | séries existantes | **faisable maintenant**, travail de module ; à concilier |
| Seuil de l'approbation ministérielle, en escalier | `_budgets`, section du seuil | **aucune série** : ni dans `precis/_seriescache/`, ni dans les paramètres du modèle | **après un travail de données** : verser les onze valeurs datées (§ 7), puis figure en escalier commune ; en attendant, la phrase des paliers et le tableau replié suffisent |
| Montant du fonds voté, loi de finances par loi de finances, 1987-2017 | `_transferts` | une seule valeur lue (1990) | **à documenter d'abord** (`TODO` l. 69) ; ne rien tracer |
| Frise des réformes en tête de chapitre | les deux | — | non proposée : le tableau court des réformes en tient lieu, et les traits verticaux des figures existantes marquent déjà 2016 et 2018 |

Sur les figures existantes, marquer les grandes réformes que la série encadre, et elles seules.
Sur `fig-fl-lp-fccl` : 1987 (série de 1985-1991) et l'étape de 2014 (série de 2008-2019) ; 2001
n'est encadrée par aucune série (l'une s'arrête en 1996, l'autre commence en 2002) et ne se marque
pas ; 2007 est encadrée (série de 2002-2012) mais ne se marque que si l'arbitrage A1 en fait une
grande réforme. Sur les figures des budgets : 2008 et 2019.

---

## 7. Tableaux faits main qui devraient être engendrés (constat pour `backlog-modele.md`)

Aucun paramètre des finances locales n'existe dans l'arbre du modèle (vérifié par deux voies :
recherche de fichiers et de contenu sur `local`, `fccl`, `collectiv`). Le volume n'a pas de
répertoire `tables/`. Sans en faire une condition de la conversion :

| Tableau | Ce qu'il faudrait verser | Sourçage |
|---|---|---|
| `tbl-fl-fccl-repartition` | part des collectivités, part des communes et des conseils, poids des critères (égalité, population, propriété bâtie, péréquation), taux de la réserve : sept dates | complet, textes lus (clauses d'effet de 1982 et 1986 à contrôler) — `TODO` déjà posé l. 119 |
| `tbl-fl-budg-seuils` | seuil de recettes, onze dates ; seuil du délégué (75 000 D, 1976-1985) | complet, décrets lus — `TODO` déjà posé l. 92 |
| `tbl-fl-budg-art135` | deux plafonds de moitié ; seuil de 5 % du déficit d'exécution (art. 182) | une date, édition arabe |
| Agrément des investissements | 100 000 et 50 000 D (décret n° 75-782) | une date ; aucun texte postérieur identifié |
| Impôts affectés au fonds, 1976-1986 | six taux de prélèvement | une date ; utile seulement si la série du fonds est reconstituée |

Ne relèvent pas des paramètres : `tbl-fl-fccl-prelevements` (montants votés, donnée budgétaire),
les nomenclatures, les tableaux de sources et d'écarts.

---

## 8. Erreurs, contradictions et tournures contraires aux règles, relevées en lisant

1. **Date de suppression du fonds.** `_longue_periode` l. 28 et l. 146 écrivent « au 1er janvier
   2018 » ; `_transferts` l. 93 dit que la date d'effet n'est pas relevée, et la note la dit
   « probable ». À aligner sur « la loi de finances pour 2018 », sans date, jusqu'à la lecture.
2. **1990.** La note de lecture de `fig-fl-lp-fccl` et le tableau des écarts disent
   « vraisemblablement le fonds entier contre la quote-part des communes » ; `_transferts` l. 123
   dit la divergence non tranchée ; la note avance une autre hypothèse (montant net des
   prélèvements). Une seule formulation, la plus prudente.
3. **Colonne « 1995 » de `tbl-fl-fccl-repartition`** : l'attribution de la réserve par décret y
   apparaît, alors qu'elle date de la gestion 1992 (le texte sous le tableau le rattrape).
4. **Tournures « ne sont pas exposés ici »** (`_transferts` l. 13, 75, 93 ; `_budgets` l. 171) :
   contraires à la règle « on annonce ce que l'on présente ».
5. **`_budgets` l. 94**, « en l'état des textes identifiés, le dernier fixé » : l'état se dit par
   sa date.
6. **PIB** : `_longue_periode` l. 73 traverse trois bases ; les points de 1985-1991 sont rapportés
   au PIB d'un rapport dont la base n'est pas dite.
7. **`index.qmd` l. 14** dit les trois chapitres des institutions « à écrire » alors qu'ils
   existent.
8. **Budgétaire et rapports extérieurs dans une même phrase** : `_longue_periode` l. 71 et 138
   enchaînent Banque mondiale et Direction générale. À réordonner : les agrégats de
   l'administration d'abord, les rapports ensuite, nommés.

---

## 9. Questions au documentaliste (ticket borné, avant le rédacteur)

1. **Loi de finances pour 2018, art. 11** : texte, pages française et arabe, rubrique, date
   d'effet. Sans cela, la fin du fonds reste hors des ruptures.
2. **Rubriques ou exposés** de la loi de finances pour 1987, art. 92, et de la loi n° 2000-60 :
   ce que la loi dit chercher (les deux « objet non relevé » de T2 et T3).
3. **Loi organique n° 2007-65** : exposé des motifs ou rubriques, pour l'objet de B2.
4. **Loi de finances pour 1992, art. 80** : relecture à l'image (R2) ; montants du décret n° 92-308.
5. **Rubriques du code de 2018** (intitulés du titre et des chapitres du régime financier), pour
   dire B3 dans les mots du code.
6. Clauses générales d'effet des lois de finances pour 1982, 1986 et 1992 ; date d'effet de la loi
   organique n° 94-44.
7. Fondement de la réserve de 15 % en 2018-2019 ; nature de la « dotation annuelle » de 2022-2023.
8. Définitions du « ratio d'autonomie financière », du « ratio des rémunérations » et du taux de
   recouvrement publiés par la Direction générale.

---

## 10. Arbitrages soumis au propriétaire

| # | Question | Recommandation |
|---|---|---|
| A1 | **2007 (part des collectivités 75 → 82 %, réserve 25 → 18 %) : étape ou grande réforme du fonds ?** | **Étape.** Elle relève un niveau ; la loi ne dit que « révision des critères ». Elle reste visible : point 2 de la vue d'ensemble, tableau de la répartition, section de la réserve. À promouvoir si le propriétaire veut que le plus gros déplacement d'argent ait son titre. |
| A2 | **Où vont la figure des recettes propres et des transferts et celle de l'autonomie ?** | **Au chapitre des budgets** (la première en vue d'ensemble) : elles partagent leurs grandeurs et leur notation, et se lisent dans la nomenclature. Autres lectures : la première au chapitre des transferts ; la seconde à « Taxes, redevances et autonomie fiscale », qui l'annonce. |
| A3 | **La figure du rendement des quatre impôts : scindée ou entière ?** | **Scindée en deux**, une par chapitre d'impôts, la comparaison des quatre restant dite dans le texte du chapitre de l'activité. La fiche impôts fait le même choix. Autre lecture : entière au chapitre des budgets, avec renvois. |
| A4 | **Les sources des séries : un seul lieu, ou redites dans chaque chapitre ?** | **Un seul lieu, la longue période du chapitre des budgets** (`tbl-fl-lp-sources`, l'administration d'abord, la Banque mondiale ensuite) ; les autres chapitres y renvoient en tête de leur longue période, comme le prévoit déjà la fiche impôts. Le tableau des écarts, lui, n'est pas un arbitrage : il est réparti par famille de sources (§ 4.4) pour respecter la règle. Seul point à confirmer : le tableau du ministère des Finances repris par Dafflon et Gilbert est classé avec l'administration. |
| A5 | **Convertir avant ou après la lecture de l'art. 11 de la loi de finances pour 2018 ?** | **Lancer le ticket du documentaliste d'abord** (§ 9, une demi-heure), convertir ensuite : le plan tient dans les deux cas, mais la section « Depuis 2018 » et le tableau des réformes changent d'une ligne. |

Arbitrages pris par défaut, à renverser au besoin : les deux tables de notations sont dissoutes dans
le texte ; les titres de réforme portent l'année du texte (2007, 2018), la date d'effet a sa
colonne ; les identifiants `fig-fl-lp-…`, `tbl-fl-lp-…` et `sec-fl-lp-…` gardent leur nom après le
déménagement, bien qu'ils disent « lp ».

---

## 11. Les risques du plan

- **Le repli de `tbl-fl-budg-seuils`** cache un paramètre en vigueur pour les nouveaux conseils : le
  texte principal doit dire 18 MD et sa date, deux fois (section du seuil, état du droit).
- **Le calendrier budgétaire replié** : un praticien le cherche. Les trois titres de bloc disent
  « calendrier ».
- **La réserve sortie des grandes réformes** : le passage de 1992 au décret n'est plus dans l'épine. La vue
  d'ensemble et la phrase d'entre-temps doivent la signaler.
- **La figure des recettes propres en tête du chapitre des budgets, son commentaire en fin** : le
  lecteur de la longue période doit trouver un renvoi en tête de la sous-section.
- **Trois ruptures seulement pour les transferts** : si le documentaliste établit 2018, il y en a
  quatre ; si le propriétaire promeut 2007, cinq.
- **Trois chapitres changent ensemble, et trois autres reçoivent une figure** : une seule branche et
  un seul rendu du livre, après accord des deux fiches sur la scission.
- **Niveau 4 de titre** dans la section du code (`####`) : `number-depth: 4` le permet ; vérifier
  qu'aucune section n'a une seule sous-section.

---

## 12. Liste de contrôle pour le rédacteur

1. Copie de départ des trois chapitres hors du dépôt ; mesures du § 1.1 refaites.
2. Réorganiser, ne pas récrire : aucun fait nouveau hors de la note complémentaire du
   documentaliste.
3. Chaque section de disposition dit son objet avant son évolution ; chaque symbole est redéfini
   où il sert.
4. Registres d'abord, domicile unique ensuite ; `scripts/check_domicile_references.py`.
5. `docs/recherches.yml` : corriger le champ `ou:` de `r-ccl-2018-nomenclature-art167` ;
   `uv run python scripts/recherches.py verifier`.
6. Supprimer `_longue_periode.qmd` et suivre la liste du § 4.3 ; `scripts/check_numerotation.py`.
7. `scripts/verifier.sh --sans-reseau finances_locales` ; restaurer les `figdata` non modifiés.
8. `docs/notes/backlog-precis.md` et `docs/notes/backlog-modele.md` (§ 7) dans le même changement.
9. Vérifier que les ancres `[]{#sec-…}` posées à la place d'anciens titres rendent sans
   avertissement de renvoi (convention partagée avec la fiche impôts).
10. Ouvrir le rendu dans le navigateur, sur `#sec-fl-transferts-vue-ensemble` et
   `#sec-fl-budg-vue-ensemble`.
