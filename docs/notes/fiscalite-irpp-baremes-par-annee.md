# Barèmes de l'IRPP par millésime — tableau de travail

> **Note subordonnée.** Ce tableau a été construit à partir des seuls paramètres openfisca,
> puis corrigé sur textes officiels. La source qui fait foi est désormais
> **`fiscalite-irpp-bloc-a-documentation.md`** (agent documentaliste, dépouillement complet
> 1989-2026). En cas de divergence, c'est elle qui prime, puis
> `fiscalite-irpp-besoins-documentation.md`.
> Corrections déjà intégrées ci-dessous ; le tableau reste un pense-bête de travail, pas une
> source.
>
> - **§1 est désormais établi sur le texte officiel** (JORT n° 1 du 2-5 janvier 1990, p. 9),
>   et il contredit à la fois le précis et openfisca. Voir §2.
> - Le **véhicule du barème 2017** est établi : article 14-1 de la loi n° 2016-78 du
>   17 décembre 2016, JORT n° 105 du 27 décembre 2016.
> - **Pagination LF 2025 : les DEUX valeurs sont exactes, ce sont deux éditions.**
>   L'article 36 est en **p. 3429-3430 de l'édition française** et en **p. 6429 de l'édition
>   arabe**. La notice `jort_cache.db` (recid 189500, `pages: 6429-6429`) décrit l'édition
>   arabe. J'avais d'abord conclu que « 3430 » était erronée : c'était faux, et cette
>   conclusion a été propagée avant d'être corrigée. Toute citation doit préciser l'édition.

**Statut : note de travail, à consolider.** Source principale de ce tableau :
`openfisca-tunisia/openfisca_tunisia/parameters/impot_revenu/bareme.yaml` (paramètres
datés, avec métadonnées de référence). Ce fichier ne connaît que **trois millésimes**
de barème : 1990, 2017, 2025 — datés en **années de revenus** (voir §5). Toute autre modification doit être vérifiée dans le JORT
avant d'entrer dans le précis.

## 1. Avant 1990 — la contribution personnelle d'État (CPE)

> **Convention de décompte des tranches, à appliquer partout.** On compte **toutes les lignes
> du tableau, y compris la tranche à 0 %**. C'est la convention implicite du précis lui-même :
> elle seule rend cohérents ses propres décomptes (5 tranches en 2017 — 0, 26, 28, 32, 35 % ;
> 8 tranches en 2025 — 0, 15, 25, 30, 33, 36, 38, 40 %). Sous cette convention : **CPE 1986 =
> 18 tranches**, **code de 1989 = 6 tranches**, **2017 = 5**, **2025 = 8**.

Il n'existait pas, avant 1990, d'« impôt général sur le revenu » portant ce nom. L'impôt
progressif sur le revenu global s'appelait **contribution personnelle d'État**, institué par
le **décret du 31 mars 1932** et remanié à plusieurs reprises. Il coexistait avec les impôts
cédulaires. La nomenclature budgétaire du JORT de fin 1989 les fait d'ailleurs apparaître sur
deux lignes distinctes (« Contribution Personnelle d'État » ; « Impôts sur les Traitements et
Salaires »).

L'article 2 de la loi n° 89-114 énumère les prélèvements supprimés à compter du 1er janvier
1990, avec leurs textes fondateurs : impôt sur les BIC (art. 9 de la loi n° 85-109 du
31 décembre 1985) ; impôt sur les bénéfices des professions non commerciales (arrêté du
30 mars 1954) ; taxe sur le revenu des valeurs mobilières et sur les intérêts des créances
hypothécaires ou privilégiées (décret organique du 23 décembre 1918) ; impôt sur le revenu
des créances (décret organique du 20 décembre 1919) ; **contribution personnelle d'État**
(décret du 31 mars 1932) ; contribution de solidarité (loi n° 73-72 du 19 novembre 1973).

### 1.1 Dernier barème de la CPE avant la réforme — **établi sur texte officiel**

**Article 8 de la loi n° 85-109 du 31 décembre 1985 portant loi de finances pour la gestion
1986**, JORT **n° 91 du 31 décembre 1985, page 1731** (tome 128). Lu à l'image.
PDF : https://www.pist.tn/jort/1985/1985F/Jo09185.pdf ; copie locale
`PDFs/JORT/1985/fr/Jo09185.pdf`, page 3.

Cet article abroge et remplace l'article 8 du décret du 31 mars 1932 (dans sa rédaction issue
de l'article 9 de la loi n° 82-91 du 31 décembre 1982). Le tableau est intitulé
« BAREME DE LA C.P.E. » :

| Tranches de revenus imposables (dinars) | Taux de la tranche | Taux d'imposition du revenu global à la limite supérieure |
|---|---|---|
| 0 à 900 | 0 % | 0 % |
| 900,001 à 1 300 | 5 % | 1,53 % |
| 1 300,001 à 1 500 | 10 % | 2,66 % |
| 1 500,001 à 2 000 | 15 % | 5,75 % |
| 2 000,001 à 2 500 | 20 % | 8,60 % |
| 2 500,001 à 3 000 | 25 % | 11,33 % |
| 3 000,001 à 3 500 | 30 % | 14,00 % |
| 3 500,001 à 4 000 | 36 % | 16,75 % |
| 4 000,001 à 5 000 | 42 % | 21,80 % |
| 5 000,001 à 6 000 | 48 % | 26,16 % |
| 6 000,001 à 8 000 | 54 % | 33,12 % |
| 8 000,001 à 10 000 | 56 % | 37,70 % |
| 10 000,001 à 14 000 | 58 % | 43,50 % |
| 14 000,001 à 25 000 | 60 % | 50,76 % |
| 25 000,001 à 40 000 | 62 % | 54,97 % |
| 40 000,001 à 60 000 | 64 % | 57,98 % |
| 60 000,001 à 80 000 | 66 % | 59,98 % |
| au-delà de 80 000 | 68 % | — |

**Dix-huit tranches, taux marginal supérieur de 68 % au-delà de 80 000 dinars.**

Dispositions attenantes du même article : les contribuables dont les revenus annuels ne
dépassent pas le SMIG sont exonérés, et l'impôt ne peut excéder l'excédent des revenus par
rapport au SMIG ; la cotisation effective ne peut excéder **60 % du revenu global imposable** ;
un décret fixe un barème par tranches de 20 dinars à partir de 900 dinars — c'est l'objet du
**décret n° 86-1188 du 12 novembre 1986** (JORT n° 71 du 5 décembre 1986, p. 1426-1431), qui
publie la table des cotes d'impôt et non des taux.

### 1.2 Ce que cela règle dans le texte du précis

**Les deux chiffres litigieux du précis viennent d'ici, et d'une seule et même confusion :
des paramètres de la CPE d'avant 1990 attribués au code IRPP d'après 1990.**

- Le **« taux marginal maximal de 68 % »** est celui de la CPE (loi 85-109), pas celui du code
  de 1989, qui plafonne à 35 % dès l'origine (§2). Le nombre de tranches avancé par
  `@touaiti2026` (« 16 tranches ») est inexact : sous la convention de décompte ci-dessus, le
  barème de la CPE en compte **dix-huit** (dix-sept tranches effectivement imposées, plus la
  tranche à 0 %).
- Le **« plafond de 80 000 dinars »**, que le précis présente comme le seuil du taux marginal
  supérieur de l'IRPP avant 2017, est en réalité le seuil d'entrée dans la tranche à 68 % de
  la CPE. Le seuil du taux marginal de l'IRPP était de 50 000 dinars depuis 1990.

Autrement dit, la rupture de 1989-1990 est **beaucoup plus radicale** que ce que raconte
aujourd'hui le précis : le taux marginal supérieur passe de 68 % à 35 % en une fois, et le
nombre de tranches de dix-huit à six. Il n'y a pas eu de « simplification de 1991 » : la
simplification, c'est la réforme de 1989 elle-même. C'est le récit à réécrire.

### 1.3 Antériorités à documenter

La chaîne des barèmes de la CPE est identifiable par ses textes modificatifs successifs :
article 8 du décret du 31 mars 1932, puis notamment l'article 9 de la **loi n° 82-91 du
31 décembre 1982** (LF 1983, présentée comme une « réforme »), la **loi n° 79-66 du
31 décembre 1979** (LF 1980, visée par le décret n° 80-248 du 26 février 1980, JORT n° 16 des
11-14 mars 1980, p. 787), et des dispositions dans les LF 1974, 1975, 1976, 1978, 1979 et
1989. Ces barèmes intermédiaires ne sont pas encore relevés.

## 2. Barème d'origine du code de 1989 — **établi sur texte officiel**

**Source primaire, vérifiée à l'image.** Le code annexé à la loi n° 89-114 du 30 décembre 1989
n'a **pas** été publié dans le JORT n° 88 du 31 décembre 1989 (qui ne porte que la loi de
promulgation), mais dans le **JORT n° 1 du 2-5 janvier 1990, pages 3 à 21** (tome 133).
Article 44 §I, page 9 du fascicule.
PDF : https://www.pist.tn/jort/1990/1990F/Jo00190.pdf (édition française) ;
https://www.pist.tn/jort/1990/1990A/Ja00190.pdf (arabe).
Copie locale : `PDFs-legislation-tunisie/PDFs/JORT/1990/fr/Jo00190.pdf`, page 9.

Le texte introduit le barème par la règle d'arrondissement (« décompter la fraction du dinar
comme un dinar entier »), puis donne le tableau suivant — reproduit ici avec sa troisième
colonne, que le précis devra conserver car elle est dans le texte :

| Tranches (dinars) | Taux | Taux effectif à la limite supérieure |
|---|---|---|
| 0 à 1 500 | 0 % | 0 % |
| 1 500,001 à 5 000 | 15 % | 10,50 % |
| 5 000,001 à 10 000 | 20 % | 15,25 % |
| 10 000,001 à 20 000 | 25 % | 20,12 % |
| 20 000,001 à 50 000 | 30 % | 26,05 % |
| au-delà de 50 000 | 35 % | — |

**Six tranches, taux marginal supérieur de 35 % au-delà de 50 000 dinars, dès l'origine.**

Trois conséquences immédiates, toutes défavorables au récit actuel du précis :

1. **Les « 16 tranches / 68 % » ne sont pas celles du code de 1989.** Le barème promulgué
   compte six tranches et plafonne à 35 %. Si ces caractéristiques ont existé, elles
   appartiennent au régime antérieur (IGR / contribution personnelle d'État), pas au code
   IRPP-IS. À vérifier côté Q18, mais l'attribution actuelle est fausse.
2. **La « simplification de 1991 » perd son objet.** Le barème à six tranches et 35 % n'est pas
   le produit d'une réforme de 1991 : c'est le barème d'origine. Combiné au fait que le code
   consolidé n'annote l'article 44 §I que d'une modification unique (LF 2016-78), l'hypothèse
   la plus probable devient : **aucune modification du §I entre 1990 et 2016**. Reste à
   confirmer formellement (Q3), mais tout le paragraphe « La simplification de 1991 » du
   précis est à réécrire.
3. **Le seuil pré-2017 était 50 000 dinars, pas 80 000** (Q4 tranchée). La phrase « 35 % pour
   un plafond de 50 000 dinars, contre 80 000 dinars auparavant » inverse la réalité : le
   seuil de 50 000 D existait depuis 1990. Ce que la LF 2017 a changé, c'est la structure des
   tranches basses et le relèvement du seuil d'exonération à 5 000 D, pas le seuil du taux
   marginal supérieur.

**L'encodage openfisca daté `1990-01-01` est erroné, pas seulement incomplet** : il s'arrête à
« au-delà de 20 000 D : 30 % » et **omet purement et simplement la tranche supérieure**
(20 000,001–50 000 à 30 %, puis au-delà de 50 000 à 35 %). À corriger dans
`openfisca-tunisia`, avec la référence ci-dessus.

Autres paragraphes de l'article 44 dans leur version d'origine (même page) :
§II minimum d'impôt de 0,5 % du chiffre d'affaires brut, plafonné à 500 dinars ;
§III régime des plus-values (15 % ; 25 % ou 50 % selon l'acquéreur) ;
§IV régime forfaitaire des petits exploitants, artisans et commerçants, avec des seuils de
chiffre d'affaires de 15 000 D (services), 20 000 D (consommation sur place) et 30 000 D
(production, transformation, achat pour revente).

## 2 bis. Stabilité 1990-2016 — **attestée**

Le §I de l'article 44 **n'a pas été modifié entre 1990 et 2016**. Le barème du §2 ci-dessus
vaut donc pour vingt-sept années de revenus, de 1990 à 2016 incluses. Établi par trois voies
convergentes (détail dans `fiscalite-irpp-bloc-a-documentation.md`) : chaîne d'annotation du
code consolidé, où le §II porte des mentions remontant à 1997 alors que le §I n'en porte
qu'une, de 2016 — le silence est donc significatif ; identité stricte des barèmes de 1990 et
de 2016, taux effectifs compris ; dépouillement sur texte des dix lois de finances de
1990-1999, de la LFC 1991 et de la loi n° 98-73. Contrôle : note commune n° 3/2017 de la DGI.

La loi de finances pour 1991 (loi n° 90-111, JORT n° 86, p. 2049) ne contient aucune
occurrence du mot « barème ». Le mot « simplification » apparaît bien dans la décennie, mais
appliqué au **régime forfaitaire** (art. 101 de la LF 1993) et aux **procédures fiscales**
(loi n° 98-73) — origine probable de la confusion.

## 3. Barème applicable aux revenus à compter de 2017

Texte : **article 14-1 de la loi n° 2016-78 du 17 décembre 2016** (loi de finances pour 2017),
JORT n° 105 du 27 décembre 2016, **p. 3831** (la loi commence p. 3829).

| Tranche de revenu net annuel (DT) | Taux marginal |
|---|---|
| 0 – 5 000 | 0 % |
| 5 000 – 20 000 | 26 % |
| 20 000 – 30 000 | 28 % |
| 30 000 – 50 000 | 32 % |
| au-delà de 50 000 | 35 % |

## 4. Barème applicable aux revenus à compter de 2025

Texte : article 36 de la loi n° 2024-48 du 9 décembre 2024 portant loi de finances pour
l'année 2025, JORT n° 149 du 10 décembre 2024, tome 167, **p. 3429-3430 (édition française)**,
**p. 6429 (édition arabe)**. Fascicule : https://www.pist.tn/jort/2024/2024A/Ja1492024.pdf
(édition arabe ; pas d'édition française référencée dans la notice).
L'article 36 modifie le **§I de l'article 44** du code de l'IRPP et de l'IS et s'applique
aux revenus réalisés à compter du 1er janvier 2025.

| Tranche de revenu net annuel (DT) | Taux marginal |
|---|---|
| 0 – 5 000 | 0 % |
| 5 000 – 10 000 | 15 % |
| 10 000 – 20 000 | 25 % |
| 20 000 – 30 000 | 30 % |
| 30 000 – 40 000 | 33 % |
| 40 000 – 50 000 | 36 % |
| 50 000 – 70 000 | 38 % |
| au-delà de 70 000 | 40 % |

## 5. Convention d'année : revenus vs imposition (décalage d'un an)

**Avertissement de lecture. Les dates de ce tableau sont des années de *revenus*, pas des
années d'*imposition*.** Le décalage d'un an entre les deux conventions est la première
source d'erreur sur ce sujet, et il faut que le précis annonce explicitement laquelle il
retient avant de publier le moindre barème.

Les trois conventions qui circulent :

| Convention | Ce que « barème 2025 » désigne alors |
|---|---|
| Année des revenus | Revenus réalisés en 2025, déclarés et liquidés en 2026 |
| Année d'imposition / de déclaration | Revenus réalisés en 2024, déclarés en 2025 |
| Année de la loi de finances | La LF votée fin 2024 pour l'exercice 2025 |

Ce que l'on peut établir :

- **Le texte officiel lui-même raisonne en année de revenus.** La notice JORT de
  l'article 36 de la LF 2025 (recid 189500) précise : « وتطبق أحكام هذا الفصل على
  المداخيل المحققة ابتداء من غرة جانفي 2025 » — les dispositions s'appliquent aux
  **revenus réalisés à compter du 1er janvier 2025**. La convention « année de revenus »
  est donc celle du législateur, et c'est celle que le précis doit retenir.
- **openfisca-tunisia raisonne en année de revenus.** La variable `irpp`
  (`variables/prelevements_obligatoires/impot_revenu/irpp.py:583`) a un
  `definition_period = YEAR` et se calcule sur la même période que les revenus qui
  l'alimentent ; les tests (`tests/formulas/impot_revenu/`) déclarent revenus et impôt
  sur une même `period`. Une valeur datée `2025-01-01` dans `bareme.yaml` s'applique donc
  aux **revenus de 2025**.
- **Les métadonnées du fichier mélangent les deux repères** sans le dire : pour le
  millésime 2025, la date d'effet du paramètre est `2025-01-01` (revenus 2025) tandis que
  `official_journal_date` vaut `2024-12-10` (publication de la LF au JORT). Les deux sont
  correctes, mais elles ne parlent pas de la même année — d'où le risque de recopier
  « 2024 » ou « 2025 » au hasard dans le précis.

Conséquences pratiques :

1. Toute affirmation du type « le barème a changé en 2017 » doit préciser *revenus 2017*
   ou *déclaration 2017*. La loi de finances 2017 et le barème applicable aux revenus 2017
   portent le même millésime ici, mais ce n'est une coïncidence de convention, pas une règle.
2. Le rapprochement avec des **données statistiques** (INS, DGI, recettes budgétaires)
   est le point le plus dangereux : les recettes d'IRPP encaissées une année N mêlent des
   retenues à la source sur revenus N et des régularisations sur revenus N-1. Un graphique
   d'évolution qui superpose barème et recettes doit expliciter ce décalage, sinon il
   attribue à un barème des recettes qui relèvent du précédent.
3. Pour chaque texte, la note documentaire devra donc relever **trois dates distinctes** :
   date de la loi, date de publication au JORT, et **date d'effet en termes de revenus**
   telle que l'énonce l'article lui-même (« applicable aux revenus réalisés à compter du
   1er janvier … »). C'est cette troisième date, souvent la seule qui compte, qui est
   absente de nos sources actuelles.

## 6. Écarts à trancher avec le texte actuel du précis

Le texte de `precis/fr/fiscalite/index.qmd` contredit sur trois points les paramètres
openfisca. Aucun des deux ne peut être retenu sans retour au JORT.

1. **Le barème initial de 1990 et la simplification de 1991.** Le précis décrit un IRPP
   initial « très progressif avec 16 tranches et un taux marginal maximal de 68 % »
   [@touaiti2026], simplifié en 1991 à « 6 tranches, taux marginal maximal 35 % ».
   Or openfisca ne connaît aucun millésime 1991, et son barème daté de 1990 compte
   **5 tranches avec un taux marginal supérieur de 30 %** — ce qui ne correspond ni au
   barème d'origine décrit par le précis, ni à la simplification telle qu'il la décrit.
   Hypothèse à vérifier : le barème « 1990 » d'openfisca serait en réalité un barème
   postérieur, saisi sans sa date d'effet réelle. À trancher sur le texte du Code de 1989
   et sur la loi de finances ayant opéré la simplification.
2. **Le seuil du taux marginal supérieur en 2025.** Le précis écrit que la LF 2025 porte
   « le taux marginal supérieur à 40 % au-delà de 50 000 dinars ». Les paramètres placent
   les 40 % **au-delà de 70 000 dinars**, les 50 000–70 000 DT étant à 38 %.
3. **Le nombre de tranches entre 1991 et 2016.** Le précis parle d'un barème à 6 tranches
   stable jusqu'en 2016 puis ramené à 5 tranches en 2017. Le barème 2017 ci-dessus compte
   bien 5 tranches, mais le barème antérieur qu'on lit dans openfisca en compte 5 aussi,
   pas 6. Le décompte dépend de la convention retenue (la tranche à 0 % est-elle comptée ?)
   — à harmoniser explicitement dans le précis.

## 7. Paramètres périphériques déjà datés dans openfisca

À intégrer au récit du barème, car ils en modifient la portée réelle :

- `impot_revenu/exoneration/seuil.yaml` : 5 000 DT au **1er janvier 2014**, **sans date de
  fin — encodage erroné**. Il s'agit d'une **exonération catégorielle** des salariés et
  pensionnés (art. 73-1 de la LF 2014, JORT n° 105 du 31 décembre 2013, p. 3691), applicable
  aux **revenus 2014 à 2016 seulement** et **abrogée** par l'article 14-5 de la LF 2017. Ce
  n'est pas l'ancêtre de la tranche à 0 % du barème, qui est un dispositif distinct créé par
  l'article 14-1 de la LF 2017.
- `impot_revenu/deductions/famille/` : déductions pour charges de famille (enfants,
  4e enfant, enfants supplémentaires).
- `impot_revenu/minimum_impot/` : minimum d'impôt et son taux.
- `impot_revenu/tspr/` : abattements sur traitements, salaires et pensions
  (dont `abattement_pour_salaire_minimum`).
- `impot_revenu/regimes_speciaux/forfaitaire/` et `retenue_liberatoire/`.
- `impot_revenu/contribution_budget_etat.yaml`.

## 8. LF 2026 — barème inchangé

**JORT n° 148 du 12 décembre 2025**, tome 168, p. 4231-4331 (loi n° 2025-17). Le barème de
l'article 44 §I **n'est pas modifié**. À signaler avec réserve, l'édition **française** du
fascicule n'étant pas encore publiée (lecture faite sur l'édition arabe, à faire relire) :
l'article 91 crée un régime estimatif optionnel, et l'article 56 porte l'abattement sur
pensions de 25 % à 30 % en 2027, 40 % en 2028 et 50 % en 2029.

## 9. Ce qu'il reste à obtenir du JORT

Pour chaque millésime : numéro et date de la loi, numéro d'article, numéro et page du
JORT, URL pist.tn. Manquent aujourd'hui les références de **1989/1990**, de la
**simplification de 1991**, de la **loi de finances 2014** (seuil d'exonération) et de la
**loi de finances 2017**. Il faut également vérifier s'il existe des modifications
intermédiaires du barème entre 1991 et 2016 qu'openfisca n'aurait pas enregistrées,
et l'état du barème en **loi de finances 2026**.
