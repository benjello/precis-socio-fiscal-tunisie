# Revue — « précis ajouts.docx » : suggestions pour le livre *Rémunérations publiques*

Source relue : `~/Downloads/prcis/précis ajouts.docx` (2 pages de texte + 2 images).
Chapitres visés : `precis/fr/remunerations_publiques/{index,_regime_indiciaire,_regime_statutaire_autonome}.qmd`.

## Statut d'application (26/08/2026)

Les suggestions des § 1 à 8 ci-dessous ont été **appliquées** au chapitre FR, sauf mention
contraire. Rendus locaux `quarto render` **FR et AR : OK**, aucune citation ni référence
croisée non résolue.

| § | Suggestion | État |
|---|---|---|
| 1 | Art. 13 loi 83-112 — service fait + légalité | **appliqué** (`_regime_indiciaire`, nouvelle sous-section) |
| 2 | Sous-section « L'ancien système indiciaire (1949-1997) » | **appliqué** (socle JORT + bloc 1949 attribué) |
| 3.1 | Date d'effet au 1^er^ janvier 1998 | **appliqué, attribué** — vérification JORT impossible (pist.tn injoignable), TODO posé |
| 3.2 | Indemnités compensatrices (décret n°97-2127) | **appliqué** |
| 4 | Généalogie 1956-1959-1968-1983 + fil « ouvriers » | **appliqué** (sous-section des Repères historiques) |
| 5 (a,b,d) | Légalité reclassée ; promotion (art. 28) et reclassement (art. 33) ajoutés | **appliqué** |
| 5 (c) | Art. 19 de la Constitution de 2022 | **écarté** — voir ci-dessous |
| 6 | Formulation « accords sans valeur juridique / reformulés par décret » | **appliqué**, adossée à l'art. 13 |
| 7.4 | CNRPS / assurance maladie | **corrigé** : bullet CNAM (loi n°2004-71) + bullet AT/MP (loi n°95-56) |
| 8 | Réserve trop large de `_regime_statutaire_autonome` | **appliqué** (@tbl-textes-statutaires + chaîne indemnité de magistrature) |
| 9 | 15 références CSL FR + AR | **appliqué** + inbox `biblio-a-rapatrier.md` |
| 10 | 6 entrées de glossaire + 2 entrées améliorées | **appliqué**, glossaire régénéré |

**Le § 5 (c) — art. 19 de la Constitution de 2022 — a été écarté**, et c'est un écart
délibéré par rapport au document source. Cet article régit le rapport de l'administration
**aux citoyens** (« au service du citoyen », non-discrimination entre citoyens) ; il ne dit
rien du rapport de l'administration à **ses agents**. En faire le fondement d'un principe
d'égalité des *rémunérations* serait un détournement de texte. Le principe qui gouverne
réellement la matière — la légalité de la rémunération — est textuel et se trouve à
l'article 13 de la loi n°83-112, désormais cité.

**Non appliqué, en attente** : la vérification du JORT n°76 de 1997 (date d'effet et
structure des annexes du décret n°97-1832) et celle de l'ordre du 23 mai 1949, l'une et
l'autre bloquées par l'indisponibilité de pist.tn ; les chronologies chiffrées de
l'indemnité de magistrature et de la solde militaire, qui demandent la lecture des textes.
Chaque point porte un commentaire `TODO` à l'endroit exact du chapitre.

### Deux points laissés ouverts à dessein

**L'articulation art. 33 loi 83-112 / art. 10 décret n°2007-268 n'est pas tranchée.**
L'article 33 (dans sa rédaction issue de la loi n°97-83) pose la règle protectrice du
reclassement après promotion ; l'article 10 du décret n°2007-268 traite lui aussi du
reclassement. Faute d'avoir pu lire le décret, le chapitre expose les deux textes côte à
côte sans affirmer que le second applique le premier — il pourrait tout aussi bien y
déroger pour les grades placés sur la grille de 2007. TODO posé.

**La réserve de l'article 41 du Code de la comptabilité publique a été circonscrite après
lecture.** Les articles 108 à 118 ont été lus (109 à 114 sont abrogés par la loi
n°2003-43) : tous visent les marchés et conventions passés avec des entrepreneurs ou des
fournisseurs. Le chapitre dit donc que cette réserve ne joue pas pour la rémunération des
agents, sans pour autant affirmer que la règle du service fait serait absolue — ce qui
entrerait en contradiction avec le TODO sur les exceptions jurisprudentielles.

---

## 0. Provenance et niveaux de preuve

Le docx est une **paraphrase française** d'une source doctrinale arabe. L'image jointe
(`image2.JPG`) est le scan de la page 10 de cet ouvrage ; elle paraissait illisible
mais elle était simplement **retournée à 180°** — redressée (`convert -rotate 180`),
elle est parfaitement lisible et j'ai pu la relire directement.

**Ouvrage source** (bandeau de la page) :
> سلسلة قانون الوظيفة العمومية في تونس — الجزء الرابع — نظام التأجير بالوظيفة العمومية
> (Salah Eddine Chérif & Maher Kammoun)

Les affirmations ci-dessous sont classées par **niveau de preuve**, à respecter dans la
rédaction :

| Niveau | Ce que ça vaut | Éléments concernés |
|---|---|---|
| **P — primaire, lu mot pour mot** | citable directement | art. 13 loi 83-112 (texte intégral extrait du PDF) |
| **J — métadonnées JORT vérifiées** | numéro, date, intitulé, fascicule sûrs ; **contenu non lu** | décrets 73-316, 73-384, 79-93, 79-94, 60-328, 97-2127, 97-2131 à 97-2134, 71-222, 73-58, chaîne 79-96, chaîne indemnité de magistrature, loi 59-12 |
| **W — synthèse web** | à re-vérifier sur source primaire avant citation | art. 41 Code de la comptabilité publique ; art. 19 Constitution 2022 |
| **D — doctrinal, tierce main** | à **attribuer explicitement**, jamais à affirmer | tout le bloc 1949 (art. 103-105, plages d'indices, décisions du directeur des finances) |

---

## 1. Priorité 1 — Article 13 de la loi 83-112 : le fondement manquant

C'est le meilleur apport du document, et c'est une **lacune réelle** du chapitre :
`_regime_indiciaire.qmd` cite l'**art. 14** (encadrement des indemnités) mais jamais
l'**art. 13**, qui est pourtant le fondement légal de tout le chapitre.

**Texte vérifié mot pour mot** (niveau **P**) :

> **Article 13.** Les agents de l'État, des collectivités publiques locales ou des
> établissements publics à caractère administratif ont droit, **après service fait**, à
> une rémunération. Cette rémunération est **fixée par décret pris sur avis du ministre
> des finances**.
>
> Ils bénéficient, en outre, des régimes de retraite et de prévoyance dans les conditions
> prévues par la loi.

Cet article seul porte **trois** apports :

1. **La règle du service fait** — condition du droit à rémunération. Absente du précis.
2. **Le principe de légalité de la rémunération** — « fixée par décret pris sur avis du
   ministre des finances ». C'est exactement ce que le docx appelle (mal) « principe de
   l'égalité des rémunérations » ; c'est en réalité le **principe de légalité**, et il est
   textuel, pas doctrinal. Il **explique** aussi pourquoi le chapitre a raison d'écrire
   que « la source primaire opposable est le décret JORT » (§ Repères historiques) : la
   base juridique de cette affirmation, c'est l'art. 13.
3. **L'alinéa 2** (retraite et prévoyance) fait une charnière naturelle vers la section
   « Les prélèvements sur la rémunération ».

**Corroboration** (niveau **W**, à revérifier) : art. 41 du Code de la comptabilité
publique (loi n°73-81 du 31 décembre 1973) — aucun paiement n'est fait qu'au véritable
créancier justifiant de ses droits et **pour service fait**.

### Placement suggéré
Nouvelle sous-section en tête de « La construction de la rémunération », avant
« Le traitement de base et la grille en dinars » :

> `### Le droit à rémunération : service fait et base réglementaire`

### Réserve à tenir
Le docx ajoute des **exceptions jurisprudentielles** (interruption d'activité pour motifs
de sécurité, suspension conservatoire ordonnée par le juge, annulation juridictionnelle
d'un licenciement). **Aucune décision n'est citée.** Soit on les présente attribuées
(« la doctrine relève que… »), soit on les laisse en TODO — mais pas d'affirmation nue,
conformément à la discipline du reste du chapitre.

---

## 2. Priorité 1 — Le régime indiciaire d'avant 1998 : combler le trou historique

Le chapitre explique très bien que **le point d'indice n'opère pas en droit positif**.
Mais il ne dit jamais **ce que la grille en dinars a remplacé**. Le lecteur reste avec
une question : pourquoi parle-t-on de « régime indiciaire » si rien n'est indiciaire ?

> ⚠️ **Ne pas toucher à la phrase de droit positif du chapitre.** Elle est exacte et
> vérifiée. Ce qui suit s'y **ajoute** au passé, ça ne la corrige pas.

### 2.1 Ce que JORT confirme (niveau **J**) — le socle solide

**Il existait bien un mécanisme opérant de conversion indice → dinars**, sous forme d'une
série datée de décrets « **fixant le traitement global annuel** » :

| Décret | Date | JORT |
|---|---|---|
| 75-353 | 3 juin 1975 | 1975/038 |
| 77-122 | 16 février 1977 | 1977/012 |
| 78-53 | 25 janvier 1978 | 1978/008 |
| 78-923 | 23 octobre 1978 | 1978/071 |
| **79-93** | **11 janvier 1979** | 1979/005 |
| 80-128 | 12 février 1980 | 1980/009 |

C'est l'équivalent tunisien d'une « valeur du point », et c'est **une série** — donc une
vue d'évolution, conforme à la règle « jamais de chiffre ponctuel ».

**Trois populations, trois chaînes de textes** — ce qui corrobore de façon indépendante
l'affirmation du docx selon laquelle les grilles de 1998 sont publiées en **trois
tableaux** (fonctionnaires / agents temporaires / ouvriers) :

- **Fonctionnaires** → décrets « traitement global annuel » ci-dessus ;
- **Agents temporaires** → **décret n°73-316 du 27 juin 1973**, *relatif au classement
  hiérarchique et à l'échelonnement indiciaire applicables aux agents temporaires de
  l'État, des collectivités publiques locales et des établissements publics* (JORT 1973/025) ;
- **Ouvriers** → **décret n°73-384 du 10 août 1973**, *fixant le statut du personnel
  ouvrier de l'État, des collectivités publiques locales et des EPA* (JORT 1973/031),
  modifié par le **décret n°79-94 du 11 janvier 1979** (JORT 1979/005).

Le docx cite précisément ces trois textes (79-93, 79-94, 73-316) comme les textes de
« valeur des indices ». **Les trois sont vérifiés, aux dates exactes.** La convergence
est forte.

**Le corpus indiciaire par corps est massif et daté** : les décrets « relatif au classement
hiérarchique et à l'échelonnement indiciaire applicables à… » forment une série continue
qui remonte au moins au **décret n°60-328 du 17 septembre 1960** (JORT 1960/044) et court
jusqu'aux années 1990 — plus de 40 textes retrouvés en cache JORT. Certains sont **encore
modifiés après 1997** (ex. décret n°97-2131 du 10 nov. 1997, corps des conseillers des
services publics ; décret n°97-2132, même date).

> Le glossaire possède déjà une entrée `echelonnement-indiciaire` : elle est aujourd'hui
> orpheline dans le texte. Ce bloc historique lui donnerait enfin son ancrage.

### 2.2 Ce que le docx apporte seul (niveau **D**) — à attribuer, pas à affirmer

D'après la note (6) de Chérif & Kammoun, lue sur le scan redressé :

- Le système des **chiffres indiciaires** (`الأرقام القياسية`) est institué par
  **l'ordre (أمر علي) du 23 mai 1949**, articles 103, 104 et 105.
- **Art. 103** — chaque poste ou fonction reçoit un chiffre indiciaire variant de
  **100 à 800** ; certains postes supérieurs peuvent être classés hors des catégories de
  l'art. 104, avec des indices **supérieurs à 800**.
- **Art. 104** — quatre catégories : **أ (A) 225-800 · ب (B) 185-360 · ت (C) 130-250 ·
  ث (D) 100-195**.
- **Art. 105** — le traitement résulte de l'application du chiffre indiciaire attribué,
  **par décisions du directeur des finances**.

**Intérêt** : la structure **A/B/C/D** du décret n°99-12 (1999) — pivot du @tbl-categories-grades —
ne serait pas une création de 1999 mais un héritage de 1949, avec un **critère de classement
changé** (indice hiérarchique en 1949 → niveau de diplôme en 1999). C'est une belle idée,
et c'est précisément pour ça qu'il faut se retenir : **une seule source secondaire ne
l'achète pas.**

**Rédaction recommandée** : attribution explicite (« selon Chérif et Kammoun… »), + TODO
pour retrouver l'ordre de 1949. Jamais de citation façon `[@…]` primaire tant que le texte
n'est pas retrouvé.

**Deux points à ne pas recopier du docx :**
- Le docx rattache l'ordre de 1949 au « **budget de l'État tunisien pour l'exercice
  1949-1950** ». **Ce rattachement n'est pas dans la note arabe**, qui dit seulement
  « الأمر العلي المؤرخ في 23 ماي 1949 ». C'est un ajout du contributeur. À vérifier avant
  écriture — un texte budgétaire est un siège inhabituel pour une grille indiciaire
  (pas impossible pour l'époque, mais non confirmé).
- Le cache JORT ne remonte pas à 1949 : la vérification devra passer par une autre voie.

### Placement suggéré
Nouvelle sous-section dans `_regime_indiciaire.qmd`, juste **avant**
« Le traitement de base et la grille en dinars » :

> `### L'ancien système indiciaire (1949-1997)`

---

## 3. Priorité 1 — Le basculement de 1997-1998 : deux éléments manquants

### 3.1 La date d'effet
Le chapitre date le décret 97-1832 (16 septembre 1997) mais **ne dit jamais quand la
grille prend effet**. Le livre est net sur ce point (texte principal de la p. 10) :

> « Ainsi, **depuis le 1er janvier 1998**, le traitement de base est fixé sur la base des
> grilles suivantes. »

→ TODO simple et rentable : extraire `https://www.pist.tn/jort/1997/1997F/Jo07697.pdf`
(déjà en référence) au `pdftotext`. **Une seule extraction** confirmerait à la fois
(a) la date d'effet et (b) la structure des annexes en trois grilles (§ 2.1).

### 3.2 Les indemnités compensatrices — trouvaille non présente dans le précis

Découvert en vérifiant l'erreur de date du livre (niveau **J**) :

> **Décret n°97-2127 du 10 novembre 1997**, *relatif aux indemnités compensatrices
> instituées par le décret n°97-1832 du 16 septembre 1997 fixant le traitement de base
> des personnels de l'État…* (JORT n°93 de 1997)

C'est le mécanisme qui **neutralise les pertes individuelles** au moment de la bascule
indice → dinars. Le chapitre décrit déjà très bien l'opération de 2007 comme « à somme
largement constante » : **le parallèle avec 1997-1998 est exactement le même** et
renforce la démonstration. Sa place est dans « Le traitement de base et la grille en dinars ».

Ce décret fait partie d'un **lot du 10 novembre 1997** entièrement consacré à
l'accompagnement de la réforme (97-2127 à 97-2134). C'est là, très probablement,
**l'origine de l'erreur de date du livre** (voir § 7).

---

## 4. Priorité 2 — Généalogie des statuts généraux

Le docx donne la filiation : 1956 (ouvriers permanents) → 1959 → 1968 → 1983. Aujourd'hui
cette chronologie n'apparaît **que** dans `_regime_statutaire_autonome.qmd`, où elle sert
un autre propos (l'antériorité des statuts militaire/magistrat). Elle manque là où elle
compte, dans `_regime_indiciaire.qmd`.

| Texte | Statut de vérification |
|---|---|
| Décret du **15 novembre 1956**, statut général des ouvriers permanents | **non trouvé** en cache JORT (le cache démarre ~1959) — TODO |
| **Loi n°59-12 du 5 février 1959** (JORT 1959/008) | vérifié **J** — intitulé JORT : « *fixant le statut des fonctionnaires de l'État* », **pas** « portant statut général des fonctionnaires » comme l'écrit le docx |
| **Loi n°68-12 du 3 juin 1968** | déjà dans `references.json` ; la note y mentionne déjà l'abrogation de 59-12 et du décret de 1956 |
| **Loi n°83-112 du 12 décembre 1983** | déjà cité |

**Le fil intéressant** : la scission **ouvriers / fonctionnaires** date de 1956 et n'a
jamais été refermée. Elle explique (a) la grille « ouvriers » distincte de 1998,
(b) la chaîne 73-384 / 79-94, et (c) la mention « **et ouvriers de la 3ᵉ unité** » qui
apparaît aujourd'hui sans explication dans @tbl-ugtt-2022. Ce serait une vraie
amélioration de lisibilité.

---

## 5. Priorité 2 — Les « cinq principes » : à démonter avant usage

Le docx propose cinq principes de la politique salariale. La matière est bonne, la mise
en forme est fautive. Trois problèmes :

**(a) La liste est mal construite.** Le paragraphe placé sous « principe de l'égalité des
rémunérations » (« Aucune rémunération ne peut être instituée ou modifiée sans base légale
ou réglementaire ») n'est pas l'égalité : c'est le **principe de légalité**, et il est
**textuel** (art. 13 loi 83-112, § 1 ci-dessus). À reclasser.

**(b) Les périmètres ne coïncident pas** — c'est rédhibitoire pour un placement en
introduction :

| Principe | Fondement | Périmètre réel |
|---|---|---|
| Égalité / neutralité | art. 19 Constitution 2022 | administration publique (constitutionnel) |
| Légalité | art. 13-14 loi 83-112 | **statut général seulement** : État, CL, EPA |
| Égalité de traitement, hiérarchie, ancienneté | statut général + statuts particuliers | **statut général seulement** |
| Soutenabilité budgétaire | budgétaire, non juridique | transversal |

→ Les placer en bloc dans `index.qmd` comme « principes de la politique salariale
**publique** » **sur-généralise** : ils ne valent ni pour le régime conventionnel public
ni pour le régime de marché contrôlé. **Recommandation** : le bloc légalité / égalité de
traitement / hiérarchie / ancienneté va dans `_regime_indiciaire.qmd` ; `index.qmd` ne
reçoit au plus qu'un renvoi. La soutenabilité budgétaire est déjà traitée par
`index.qmd` (quatre périodes) et @fig-masse-salariale-ratios — ne pas dupliquer.

**(c) La citation de l'art. 19 varie selon les traductions.** Deux rendus français
concurrents d'un original arabe :

- docx : « L'administration publique et l'ensemble des services de l'État sont **au service
  du citoyen** sur la base de la **neutralité** et de l'égalité. »
- autre rendu : « … sont **à la disposition du citoyen** sur la base de l'**impartialité**
  et de l'égalité. »

→ Citer depuis **une** source identifiée (décret présidentiel n°2022-691 du 17 août 2022
portant promulgation, JORT) et signaler la variation, ou citer l'arabe. **Ne pas mélanger
les deux rendus.**

**(d) Un vrai manque à combler au passage** : le chapitre traite l'**avancement d'échelon**
(art. 23-24) mais pas l'**avancement de grade** (au choix ou à l'examen professionnel), que
le docx mentionne. C'est une lacune réelle du § « Le traitement de base et la grille en
dinars ». À sourcer sur les articles correspondants de la loi 83-112.

---

## 6. Priorité 2 — Négociation salariale : une formulation doctrinale à reprendre

Le docx offre une formulation nettement plus nette que celle du chapitre :

> « Ces accords n'ont en eux-mêmes **aucune valeur juridique**, c'est pourquoi les pouvoirs
> publics veillent à en **reformuler le contenu dans le cadre de dispositions
> réglementaires** afin de leur conférer la force exécutoire nécessaire. »

C'est exactement la thèse du § « Repères historiques » (« la source primaire opposable est
le décret JORT ; les accords en constituent le cadre »), mais énoncée comme une règle
plutôt que comme une précaution méthodologique. **Suggestion : adopter cette formulation**,
et l'adosser à l'art. 13 (§ 1) qui en donne le fondement textuel.

**Réserve** : la périodisation du docx (« élément régulier du dialogue social à partir des
années 1970 », « institutionnalisées depuis les années 1990 ») **n'est pas sourcée**. Ne pas
l'affirmer. La note `b1-regime-indiciaire-consolidation.md` § 5 bis contient déjà des cycles
sourcés (2017-2018, 2018-2020, 2023-2025) : c'est là qu'est la matière solide.

---

## 7. À NE PAS reprendre — erreurs de la source

| # | Affirmation du docx | Ce qui est établi |
|---|---|---|
| 1 | « décret n°97-1832 du **10 novembre 1997** » | **Faux.** 97-1832 = **16 septembre 1997**, JORT n°76 publié le 23 sept. 1997 (résolution unique en cache JORT). **Le précis a raison, ne rien changer.** L'erreur vient du livre lui-même (visible sur le scan). Origine probable : le lot d'application du **10 novembre 1997** (97-2127 à 97-2134). |
| 2 | Ordre de 1949 « portant fixation du budget de l'État pour 1949-1950 » | Le rattachement budgétaire **n'est pas dans la source arabe**. Ajout du contributeur. À vérifier. |
| 3 | « loi n°59-12 … portant **statut général** des fonctionnaires » | Intitulé JORT : « **fixant le statut** des fonctionnaires de l'État ». |
| 4 | CNRPS finance retraite + **assurance maladie** + prestations familiales + ATMP | **Anachronique.** L'assurance maladie relève de la **CNAM** depuis 2004 (loi n°2004-71). Reprendre tel quel injecterait une erreur dans un chapitre aujourd'hui exact. Le point mérite d'être traité — les branches réellement couvertes par la CNRPS et l'articulation avec la CNAM manquent au chapitre — mais **sur textes**, pas sur cette liste. Le régime ATMP du secteur public demande son propre texte : à vérifier, pas à affirmer. |
| 5 | Les « cinq principes » | Liste malformée + périmètres hétérogènes (§ 5). |
| 6 | Exceptions jurisprudentielles au service fait | Aucune décision citée (§ 1). |

---

## 8. Bonus — gains pour `_regime_statutaire_autonome.qmd`

Trouvé en vérifiant le docx, hors de son périmètre. Le chapitre affirme aujourd'hui :

> « Les montants par grade figurent dans des arrêtés et annexes qui ne sont pas accessibles
> de façon fiable dans le corpus consulté ; le présent chapitre en documente donc la
> **structure**, sans en restituer les barèmes chiffrés. »

**Cette réserve est trop large.** Le cache JORT donne des chaînes datées, exploitables,
pour chacun des corps — de quoi construire des **chronologies** (donc des vues d'évolution,
conformes à la règle) même sans restituer les montants :

- **Cour des comptes** — décret n°**71-222 du 29 mai 1971** fixant la rémunération du
  personnel de la Cour des comptes, modifié notamment par le décret n°97-2134 du
  10 nov. 1997.
- **Tribunal administratif** — décret n°**73-58 du 14 février 1973** relatif aux indemnités
  servies aux membres du TA, modifié par le décret n°97-2133 du 10 nov. 1997.
- **Indemnité de magistrature** — chaîne parallèle et distincte pour les **trois** corps
  (ordre judiciaire / TA / Cour des comptes) : décrets 2001-2125, 2001-2775, 2001-2776,
  puis 2009-2791/2792/2826, 2010-1749/1751/2521, 2012-3552/3553/3554,
  2017-1361/1362/1364, et 2018-73 (indemnité spécifique, pôles judiciaires antiterroriste
  et économique). **83 textes** en cache sur la requête « rémunération magistrats ».
- **Militaires** — chaîne de modification du décret 79-96 : 87-878, 88-263, 88-909,
  2002-1973, 2004-2127, 2005-3382, 2007-2408, 2010-2935.

**Correction de citation à vérifier.** Le chapitre cite l'intitulé du décret 79-96 comme
« … non classés dans la **grille des salaires mensuels** de la fonction publique ». Le
cache JORT donne, pour 79-96 **comme pour ses modificatifs jusqu'en 2010** :

> « … fixant la solde des militaires **non classés dans la grille indiciaire de la fonction
> publique** et le régime de l'alimentation dans l'armée »

À vérifier sur le PDF. Si l'intitulé officiel est bien « grille indiciaire », c'est un
**argument supplémentaire** pour la sous-section du § 2 : en 1979, la grille de la fonction
publique *était* indiciaire, et l'intitulé du texte militaire en porte encore la trace.

---

## 9. Références à créer — inbox bibliographe

À porter dans `docs/notes/biblio-a-rapatrier.md` (et **non** directement dans
`references.json`) :

**Ancien régime indiciaire** — décrets 60-328, 73-316, 73-384, 79-93, 79-94, et la série
« traitement global annuel » (75-353, 77-122, 78-53, 78-923, 80-128).
**Bascule 1997-1998** — décret 97-2127 (indemnités compensatrices) ; le cas échéant
97-2131 et 97-2132.
**Généalogie statutaire** — loi n°59-12 du 5 février 1959 ; décret du 15 novembre 1956
(à retrouver).
**Fondements transversaux** — loi n°73-81 du 31 décembre 1973 (Code de la comptabilité
publique) ; Constitution du 25 juillet 2022 (décret présidentiel n°2022-691 du
17 août 2022).
**Statutaire autonome** — décrets 71-222, 73-58, et la chaîne indemnité de magistrature.
**Doctrine** — Chérif (Salah Eddine) & Kammoun (Maher),
*سلسلة قانون الوظيفة العمومية في تونس، الجزء الرابع : نظام التأجير بالوظيفة العمومية*
(éditeur, année et ISBN à compléter — le scan de couverture est trop dégradé).
**À retrouver** — ordre beylical du 23 mai 1949.

Toutes les entrées JORT disposent d'une URL `pist.tn` canonique reconstructible
(`https://www.pist.tn/jort/<annee>/<annee>F/Jo<num><aa>.pdf`).

---

## 10. Glossaire (`precis/glossaire.yml`)

Entrées nouvelles suggérées : `service-fait`, `chiffre-indiciaire` (**رقم قياسي** — à
distinguer de l'entrée existante `point-indice`), `indemnite-compensatrice`,
`agent-temporaire`, `ouvrier-de-l-etat`, `traitement-global-annuel`,
`avancement-de-grade`, `indemnite-de-magistrature`.

Entrée existante à rattacher enfin au texte : `echelonnement-indiciaire` (§ 2.1).

---

## 11. En aval

Toute modification FR déclenche la synchro FR → AR. Rappel des pièges déjà documentés :
`_quarto.yml` `chapters` non synchronisé par la pipeline (404 AR), et rendu AR local
obligatoire avant merge.

---

## Ordre d'exécution suggéré

1. Extraire `Jo07697.pdf` → confirme la date d'effet **et** la structure en trois grilles
   (une seule opération, deux gains).
2. Rédiger le § art. 13 / service fait (matière déjà vérifiée mot pour mot, coût nul).
3. Rédiger le § « ancien système indiciaire (1949-1997) », socle JORT d'abord, bloc 1949
   attribué ensuite.
4. Ajouter les indemnités compensatrices de 1997 au § grille en dinars.
5. Généalogie 1956-1959-1968-1983 + fil « ouvriers ».
6. Reclasser les principes (légalité, égalité de traitement, hiérarchie, ancienneté) +
   combler l'avancement de grade.
7. Reprendre la formulation « accords sans valeur juridique / reformulés par voie
   réglementaire ».
8. Séparément : relever la réserve trop large de `_regime_statutaire_autonome.qmd` (§ 8).
