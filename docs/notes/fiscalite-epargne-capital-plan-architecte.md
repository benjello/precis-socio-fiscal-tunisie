# Fiche de plan : « Les revenus de l'épargne et du capital », section du chapitre de l'IRPP (livre « La fiscalité »)

Rôle : architecte. Établie le 20 octobre 2026, worktree `precis-epargne-capital`, branche
`chantier/fiscalite-epargne-capital`.

**Sources de cette fiche.**
- La note documentaire `docs/notes/fiscalite-epargne-capital.md`, désignée « N » ; « N § 4.1 » renvoie à sa section.
- Le chapitre `precis/fr/fiscalite/_impot_revenu.qmd`, 26 285 mots au 20 octobre 2026.
- Les 13 clés versées dans `precis/fr/fiscalite/references.json` et les 11 entrées de la passe 1 dans `precis/glossaire.yml`.
- Le cache des séries `precis/_seriescache/`.

**Degrés de lecture repris de N.**
- Peuvent porter une rupture : « lu image », « lu texte » (couche décodée comprise) et « lu AR ».
- Ont une ligne au registre, jamais une rupture :
  - « lu NC », c'est-à-dire le contenu tiré d'une note commune, articles non relus au fascicule ;
  - « annotation », c'est-à-dire un texte connu par le seul code consolidé.

  Leur ligne cite la note commune, qui est une source de type `report`. Quand rien n'est lu, la ligne ne figure pas dans le rendu : elle est remplacée par un TODO HTML adjacent.

**Décision du propriétaire (20 octobre 2026).** La matière s'écrit dans `_impot_revenu.qmd`, et non dans un chapitre neuf, contrairement à N § 2. La fiche applique cette décision. Le § 9 dit ce qu'elle coûte au regard du critère de scission et donne les options, sans trancher.

## Résumé

- **Domicile.** Une section `##` nouvelle, « Les revenus de l'épargne et du capital » `{#sec-irpp-epargne .domicile-unique}`. Elle se place **juste après le régime forfaitaire** et avant la contribution sociale de solidarité, à l'endroit où se trouve le TODO de la l. 989 qu'elle remplace.

  Le chapitre range déjà la retenue libératoire parmi les régimes qui sortent de la chaîne de calcul :
  - point 9 de `#sec-irpp-calcul` ;
  - paragraphe qui suit $D = I - V$.

  La section y rejoint le forfait.
- **Ce qu'elle reprend du chapitre, une seule fois chaque chose** (le détail est au § 5) :
  - `#sec-irpp-capitaux` garde les définitions (art. 29 à 35) et l'absence d'abattement ;
  - le paragraphe des exonérations et celui sur la fin de l'exonération des dividendes passent dans la section neuve, et une phrase et un lien les remplacent ;
  - l'assurance-vie, `#tbl-epargne` (identifiant gardé), le CEA, le CEI et l'art. 39 *ter* quittent `#sec-irpp-deductions` pour leurs fiches ;
  - le plafonnement de l'art. 12 *bis* (`#tbl-plafonnement`) reste dans `#sec-irpp-deductions`, parce qu'il vaut pour tous les avantages.
- **Les règles de base (le cœur)** : ce que l'impôt prélève sur les revenus du capital d'une personne physique résidente, en trois éléments :
  - (A) la retenue sur les intérêts ;
  - (B) les revenus distribués ;
  - (C) la plus-value de cession de titres.

  Sept dispositions secondaires ont chacune leur fiche. Les épargnes aidées, les fonds et les non-résidents sont secondaires.
- **L'épine : cinq grandes réformes**, toutes portées par des articles lus :
  1. **1992**, harmoniser les formes d'épargne, avec l'étape de 1997, l'unification à 20 % ;
  2. **1999**, relancer le marché financier, qui fait naître le CEA ;
  3. **2004**, la plus-value sur actions entre dans l'impôt, avec les étapes de 2011 et de 2023 ;
  4. **2014**, imposer les dividendes (distributions de 2015), avec l'étape de 2018 ;
  5. **2020-2022**, trois régimes en trois ans pour les intérêts.

  Deux classements restent à trancher (§ 8) : 1997 comme étape, et 2023 comme étape.
- **Libératoire ou imputable, d'un coup d'œil.** Le caractère de chaque retenue est une colonne à part entière, jamais repliée, dans trois tableaux : celui de la vue d'ensemble, l'état du droit et chacun des trois registres. Il est défini une fois dans le texte principal, avec les notations $R$ et $V$ que le chapitre emploie déjà.
- **Données.** La figure du coût des déductions se fait dès maintenant : `depenses-fiscales-detail` est dans le cache, avec les rapports de 2021, 2024 et 2025. N § 7 et sa lacune 8 sont en partie dépassés. Trois tableaux de paramètres seront faits main, avec un TODO du rédacteur, parce que l'arbre ne porte rien de juste. La figure des taux attend un générateur de séries.
- **Taille.** La section ajoute environ 9 000 mots au fichier, dont environ 4 750 visibles, et en retire environ 1 000. Le fichier passerait d'environ 26 300 à environ 34 000 mots. Les options de scission sont au § 9.
- **« Ce qu'en dit l'économie ».** La fiche `docs/notes/eco-epargne-capital.md` n'existait pas à mon arrivée : la section est prévue, pas remplie.

---

## 1. La frontière

**Les règles de base.** C'est ce sans quoi la section n'a pas d'objet : comment l'impôt saisit le revenu d'un placement de la personne physique résidente. Le droit le décide par deux choix :
- son taux ;
- son caractère : la retenue est imputable et le revenu reste au barème, ou bien elle est libératoire ou définitive et le revenu sort du revenu global.

Trois éléments, chacun avec son registre replié :

| Élément | Articles du code | Pourquoi dans les règles de base |
|---|---|---|
| A. Retenue sur les intérêts (revenus de capitaux mobiliers) | 34-35, 52-I-b, c, d, 52-II, 54 | taux et caractère de la retenue ; c'est là que portent 1992, 1997 et 2020-2022 |
| B. Revenus distribués (dividendes, parts de fonds, jetons de présence puis rémunérations des administrateurs) | 29-30, 38-10, 52-I-c *bis* | exonérés de 1990 à 2014, puis retenue libératoire |
| C. Plus-value de cession de titres | 31 *bis*, 33, 38-17 et 18, 44-III-3 | hors champ avant 2004, puis taux proportionnel hors barème |

**Les dispositions secondaires.** Elles aménagent la règle pour un placement ou un public.
1. Comptes spéciaux d'épargne et emprunts obligataires (39 § II et II *bis*), compte d'épargne-emprunts obligataires de 1992-1996.
2. Épargne exonérée : épargne logement, livrets de la CENT jusqu'en 1991, dépôts en devises ou en dinars convertibles, comptes d'épargne pour les études (38-7, 38-8, 38-12).
3. Assurance-vie : déduction des primes (39 § I-2) et rentes exonérées (38-16).
4. Compte épargne en actions (CEA, 39 § VIII).
5. Compte épargne pour l'investissement (CEI, 39 *bis*, 38-15).
6. Fonds et organismes exonérés. Ils ont en commun la retenue définitive de l'art. 52-II-2 (1992, 2002, 2021, 2022) : personnes morales exonérées, FCP, fonds communs de créances, fonds d'amorçage, FCPR, 39 *ter*.
7. Non-résidents : 52-I-b, c et c *bis* servis aux non-résidents, e, e *bis*, plus-values (art. 3 et 45-III).

**Ce que je ne fais pas.**
- **Les jetons de présence n'ont pas de fiche.** Ils sont des revenus de valeurs mobilières (art. 30). Ils entrent au registre B, avec trois lignes (1995, 2005, 2017) et une phrase dans l'entre-temps 1992-2014. Une fiche coûterait 200 mots visibles pour trois ajustements.
- **Les personnes morales exonérées n'ont pas de fiche propre.** Elles sont réunies aux fonds parce qu'une même disposition, 52-II-2, les régit.

**Ce qui vit ailleurs** (une phrase et un lien, en tête de la sous-section qui en a besoin) :

| Sujet | Domicile | Renvoi depuis |
|---|---|---|
| Plus-value immobilière | `_patrimoine_immobilier.qmd` (`#sec-pi-1977` et suivantes) ; définition et assiette à `#sec-irpp-foncier` | vue d'ensemble, une phrase |
| Régime boursier de la loi n° 2010-29 (IS à 20 % cinq ans) | `_impot_societes.qmd`, « Un régime hors du code : l'admission en bourse » | réforme de 1999 |
| Baisse de l'IS de 30 % à 25 % (LF 2014, art. 18), contrepartie de l'imposition des dividendes | `_impot_societes.qmd`, « 2014 — abaisser à 25 % » | réforme de 2014 |
| Retenues réalignées sur les taux de l'IS (LF 2021, art. 14 ; LF 2025, art. 37) | `_impot_societes.qmd`, « 2021 — aplatir » et « 2024 — remonter » | fiche des non-résidents |
| Coût de l'ensemble des dépenses fiscales et méthode du rapport | `_depenses_fiscales.qmd` (`#sec-df-rapport`, `#sec-df-cout`) | longue période |
| Minimum d'impôt au titre des avantages (art. 12 *bis*) | `#sec-irpp-deductions`, `#tbl-plafonnement` | fiches 3, 4 et 5 |
| Jeux de pari (art. 38) | `#sec-irpp-autres` (catégorie VII) | aucun renvoi |

**Les sous-titres de l'IS n'ont pas d'identifiant.** Je propose d'ajouter `{#sec-is-bourse}` et `{#sec-is-2014}` à `_impot_societes.qmd` : c'est la seule retouche hors du chapitre. À défaut, le lien mène à `#sec-impot-societes`, et le titre de la sous-section est écrit en clair.

**Le régime boursier de la loi n° 99-92 (art. 1 à 3) manque au chapitre de l'IS**, qui ne commence qu'en 2010. Ce régime soumet à l'IS à 20 % pendant cinq ans les sociétés qui admettent au moins 30 % de leur capital à la cote. Son domicile est l'IS. La réforme de 1999, ici, le nomme d'une proposition. Une ligne est à inscrire au backlog pour le chapitre de l'IS.

## 2. Le plan

Ces règles valent partout :
- **Profondeur.** La section est un `##`, les blocs du plan sont des `###`, chaque réforme et chaque fiche est un `####`. Le livre numérote jusqu'à quatre niveaux. Les ruptures propres à une fiche n'ont donc pas de titre : elles s'écrivent en prose, et la colonne « Portée » du registre les porte. Aucun `###` ne doit avoir un seul `####`.
- **Références.** La section porte la classe `.domicile-unique`. Les lois sortent du fil, par un lien `[…](#r-…)` vers leur ligne de registre. Les notes communes et le rapport de 2013 (type `report`) restent cités sur place. **Les tableaux courts au premier plan y sont soumis aussi** : `#tbl-irpp-epargne-taux`, `#tbl-irpp-epargne-etat`, `#tbl-epargne`, `#tbl-irpp-epargne-assurance-vie`, `#tbl-irpp-epargne-cea`. Toute référence de type `legislation` y passe par un lien `#r-…`, jamais par `[@…]`. Les crochets du tableau 4.1 de cette fiche disent seulement d'où vient chaque valeur.
- **Dates.** Une retenue se date au paiement (« revenus payés à partir du… »). Une déduction ou une exonération se date en années de revenus, selon la convention du chapitre (callout de tête). Une date qui n'est pas établie prend le tiret « — » déjà employé par `#tbl-irpp-reformes`, avec un TODO HTML adjacent.
- **Mots de travail.** Les mots « cœur », « épine » et « fiche » ne paraissent pas dans le rendu.

### `## Les revenus de l'épargne et du capital {#sec-irpp-epargne .domicile-unique}`

**L'essentiel, en une phrase.** Un revenu de placement peut rester dans le revenu global et subir le barème, la retenue opérée par le payeur s'imputant sur l'impôt. Il peut aussi en sortir, frappé d'une retenue libératoire ou d'un taux proportionnel. Il peut enfin échapper à l'impôt, dans la limite d'un plafond. L'histoire de 1990 à 2026 est celle de la frontière entre ces trois régimes, placement par placement.

**Chapeau, trois à quatre phrases.**
- Il donne la définition opératoire, que le lecteur doit trouver sans aller plus loin :
  - une retenue **imputable** laisse le revenu dans le revenu net global $R$, et la retenue entre dans $V$, les retenues et acomptes imputables de $D = I - V$ ;
  - une retenue **libératoire** fait sortir le revenu de $R$, et la retenue de $V$ : l'impôt est acquitté une fois pour toutes ;
  - une retenue **définitive et non restituable** n'est jamais rendue. Le chapeau n'en donne pas de définition générale : la NC 1/2022 la qualifie de libératoire pour 2021, mais N ne dit pas si les revenus frappés des 35 % de juin 2020 sortaient de $R$ (D3). La définition vient de la passe 2 du terminologue (T2), sur source.

  Les notations se redéfinissent ici, puisque la section doit se lire seule.
- Il porte le renvoi en tête vers la plus-value immobilière (`_patrimoine_immobilier.qmd`) et vers l'IS (régime boursier).
- Glossaire : `#g-retenue-a-la-source`, `#g-retenue-liberatoire`, `#g-retenue-definitive-non-restituable`, `#g-revenus-capitaux-mobiliers`, `#g-revenus-valeurs-mobilieres`.

### `### Vue d'ensemble {#sec-irpp-epargne-vue}`

- **Essentiel.** Le taux d'un dinar de revenu supplémentaire dépend du placement plus que du revenu de son titulaire. En 2026, la retenue est de 20 % imputable sur les intérêts : les intérêts restent au barème, jusqu'à 40 %. Les dividendes subissent 10 % libératoires. La plus-value sur titres est imposée à 0, 10 ou 15 % selon la cotation et la durée de détention.
- **Vue d'ensemble, au premier plan et non repliée** : `#tbl-irpp-epargne-taux`, « Taux marginal légal d'un dinar de revenu de placement, pour un contribuable de la dernière tranche du barème, aux dates des réformes ». Contenu détaillé au § 4.1.
- **Méthode du tableau, deux phrases sous le tableau, dans le texte principal** :
  - il donne un taux **marginal légal**, pas un taux effectif ;
  - il vaut au-delà des plafonds d'exonération ou de déduction ;
  - la contribution sociale de solidarité n'est pas comptée ; son renvoi est fait ;
  - le taux porte sur le rendement nominal, avant inflation et hors impôt payé en amont par la société ;
  - au bas du barème, la retenue imputable de 20 % peut dépasser l'impôt dû et devient restituable (art. 54), sauf en 2021.
- **Les points à dire, trois** :
  1. De 1990 à 2014, les dividendes et la plus-value sur actions cotées sont hors de l'impôt sur le revenu. Les intérêts sont au barème, jusqu'à 35 %, sauf les titres anonymes jusqu'en 1996.
  2. Depuis 2015, le dividende supporte une retenue libératoire : 5 %, puis 10 % depuis 2018. Les intérêts restent au barème, sauf en 2021 (20 % libératoires). Le tableau ne compte pas l'IS payé en amont par la société : il ne dit donc pas quel placement est le moins imposé au total, et le rendu ne classe pas les placements.
  3. Les épargnes aidées (comptes spéciaux, CEA, CEI, assurance-vie) jouent par des plafonds en dinars : ils sont décrits dans leurs fiches et tracés sur la figure de la longue période.
- **Frise** : non prévue ici. Le tableau de vue d'ensemble en tient lieu, parce que ses lignes sont les dates des réformes.
- **Rien n'est replié dans cette sous-section.**

### `### La mise en place : des taxes cédulaires au code de 1990 {#sec-irpp-epargne-1990}`

- **Essentiel.** Le code de 1990 soumet les intérêts au barème, avec une retenue imputable de 10 ou 15 %. Les bons de caisse anonymes paient 35 % libératoires. Les dividendes sont exonérés.
- **Antécédent.**
  - Une phrase et un lien vers « La suppression de 1990 », qui nomme déjà la taxe sur le revenu des valeurs mobilières (décret organique du 23 décembre 1918) et l'impôt sur le revenu des créances (décret organique du 20 décembre 1919), abrogés par la loi n° 89-114, art. 2. Cette sous-section n'a pas d'identifiant : ajouter `{#sec-irpp-suppression-1990}`.
  - Ce que le code reprend de ces impôts n'est pas établi par N, faute de leurs taux et de leur régime. **Le texte rendu ne dit pas que le code « reprend » ou « écarte »**. Un TODO HTML renvoie à la question D1 (§ 7).
- **Points, trois** :
  1. Art. 52 de 1990 : 10 % sur les comptes spéciaux d'épargne des banques, 15 % sur les autres revenus de capitaux mobiliers, imputables (art. 54). 35 % sur les bons de caisse au porteur anonymes, libératoires (52-II).
  2. Art. 38-10 : les revenus de valeurs mobilières des art. 29 à 31 sont exonérés. Aucune retenue sur les distributions.
  3. **Naissances groupées, une ligne chacune, avec un renvoi aux fiches** :
     - déduction des intérêts des comptes spéciaux, 1 000 D (fiche 1) ;
     - exonération de l'épargne logement, des livrets de la CENT et des dépôts en devises (fiche 2) ;
     - déduction des primes d'assurance-vie, 200 D et majorations (fiche 3) ;
     - retenue libératoire de 15 % sur les revenus servis aux non-résidents (fiche 7).
- **Repli** : aucun. Les lignes de 1990 ouvrent chacun des registres.
- **Clés** : `code-irpp-is-1990` (art. 38, 39, 52, 54, p. 8 et 11), `loi-irpp-is-1989` (art. 2).

### `### Les grandes réformes {#sec-irpp-epargne-reformes}`

**Chapeau, deux phrases.** Il annonce les cinq réformes. Il précise que les taux et les caractères successifs, élément par élément, sont dans les trois registres repliés à la fin de la sous-section.

Gabarit de chaque `####`, à suivre partout :
1. Une phrase : ce que la loi cherche, dans ses mots, c'est-à-dire la rubrique citée entre guillemets.
2. Une ligne « contexte », avec les mots des sources de l'époque, ou rien et un TODO.
3. Avant → après, en deux à quatre points.
4. Les dispositifs qui y naissent, en deux ou trois phrases, avec un renvoi à leur fiche.
5. Les étapes de mise en œuvre, une phrase chacune.

Aucun tableau propre à une réforme : les registres portent le détail. Le tableau des réformes (§ 3) peut, au choix du rédacteur, ouvrir la sous-section sous forme courte (date, ce que la loi cherche, avant → après), sans citation. Je le recommande : c'est la forme du prototype de la TVA.

#### `#### 1992 : harmoniser les formes d'épargne, puis unifier le taux (1997) {#sec-irpp-epargne-1992}`

- **Ce que la loi cherche.** Titre III de la LF 1992, « Dispositions portant harmonisation du régime fiscal applicable aux différentes formes d'épargne ». Rubriques : « Déduction des intérêts de l'épargne », « Dispositions relatives à la retenue à la source ».
- **Contexte** : non relevé (question D2). Aucune ligne dans le rendu tant qu'il manque, seulement un TODO.
- **Avant → après** :
  - comptes spéciaux 10 % et autres revenus 15 % → 15 % sur tous les dépôts (CENT comprise) et toutes les obligations, imputables ;
  - bons de caisse anonymes 35 % → 25 % sur les obligations anonymes et 35 % sur les autres titres anonymes, libératoires ;
  - nouveau 52-II-2 : 20 % définitive et non restituable pour les personnes morales non soumises à l'IS ou exonérées ;
  - livrets de la CENT : de l'exonération (38-7) à la déduction plafonnée (39 § II), plafond porté à 1 500 D, dont 1 000 D au titre des comptes spéciaux.
- **Dispositifs qui y naissent** :
  - le compte d'épargne-emprunts obligataires : 15 % libératoires sous blocage de cinq ans (fiche 1) ;
  - la retenue définitive des organismes exonérés (fiche 6).
- **Étape : 1997.** « Unification des taux de la retenue à la source sur les revenus de capitaux mobiliers » (LF 1997, art. 30-33) : 15 % → 20 % ; fin des taux libératoires sur les titres anonymes et du libératoire du compte d'épargne-emprunts obligataires. La rubrique dit « unification » : c'est l'achèvement de l'harmonisation, d'où le classement en étape. L'autre lecture est au § 8.
- **Entre-temps 1997-1999, une phrase.** Les jetons de présence quittent l'exonération des dividendes en 1995 (retenue de 15 %) ; des ajustements suivent ; renvoi aux registres A et B.
- **Clés** : `lf-1992` (art. 30, 31, 33, p. 2084-2085), `lf-1997` (art. 30 à 33, p. 2581 ; art. 54 pour la date).

#### `#### 1999 : relancer le marché financier {#sec-irpp-epargne-1999}`

- **Ce que la loi cherche.** Intitulé de la loi n° 99-92 : « relative à la relance du marché financier ».
- **Contexte** : non relevé (D2).
- **Pourquoi c'est une grande réforme.** Elle ne touche pas aux règles de base, mais elle crée un dispositif, le CEA (art. 4, lu texte). La règle de l'architecte le veut ainsi. Le critère suivi partout : la naissance d'un dispositif qui a sa propre fiche est une grande réforme ; une modalité née à l'intérieur d'une fiche est une rupture propre (comptes d'études en 1999, obligations vertes en 2022). L'autre lecture est au § 8.
- **Avant → après** : aucune déduction liée au placement en actions → déduction de 50 % des dépôts sur un CEA, dans la limite de 5 000 D, avec un blocage de cinq ans, en actions cotées et en bons du Trésor assimilables.
- **Ce qui y naît** :
  - le CEA (fiche 4) ;
  - le régime de l'IS à 20 % pour les sociétés admises à la cote (art. 1 à 3), une proposition et un lien vers l'IS.
- **Entre-temps 1999-2004, une phrase et des renvois.**
  - Les fonds communs de placement reçoivent un régime en 2002 (fiche 6).
  - Le CEI est créé en 2003 (fiche 5).
  - Ces deux naissances ne sont pas racontées ici : leurs articles ne sont connus que par les notes communes 45/2002 et 35/2003. Elles sont dites dans leur fiche d'après ces notes communes, et le TODO D5 demande la lecture des articles.
- **Clés** : `loi-99-92-relance-marche-financier` (art. 1 à 4, p. 1463-1464).

#### `#### 2004 : la plus-value sur actions entre dans l'impôt {#sec-irpp-epargne-2004}`

- **Ce que la loi cherche.** Rubriques de la LF 2004 : « Soumission de la plus-value provenant de la cession des actions et des parts sociales à l'impôt sur le revenu » et « Exonération de la plus-value réalisée dans le cadre d'une opération d'introduction en bourse ».
- **Contexte** : non relevé (D2).
- **Avant → après** :
  - la plus-value de cession d'actions ou de parts sociales d'une personne physique, hors activité, n'est rattachée à aucune catégorie → revenu de valeurs mobilières (31 *bis*), imposé à 10 % de son montant (44-III-3), hors barème ;
  - exonérations : actions cotées, introductions en bourse, actions de SICAV, cessions par les SICAR (38-17) ;
  - franchise de 10 000 D par an (38-18).
- **Ajustement de la même loi, une phrase prudente.**
  - L'art. 71 récrit 52-II-1. L'administration a maintenu l'imputation de la retenue de 20 % pour les résidents (note commune n° 8/2004, citée sur place).
  - La LF 2005 (art. 69) a récrit le texte en ce sens, le caractère libératoire étant réservé aux non-résidents.
  - **Ni la lettre de l'art. 71 ni une recherche ne se racontent dans le rendu.** Le détail est à la ligne du registre A, dont la colonne de contenu dit : « texte récrit ; retenue maintenue imputable pour les résidents (note commune n° 8/2004) ».
- **Étapes de la plus-value.**
  - **2011.** « Rationalisation de l'exonération de la plus value provenant de la cession des titres » (LF 2011, art. 41) : l'exonération des actions cotées acquises à partir de 2011 est réservée aux cessions intervenues après la fin de l'année suivant l'acquisition. La même loi impose les plus-values des non-résidents (fiche 7).
  - **2023.** Deux taux selon la durée de détention et la cotation (10 % et 15 %), franchise de 10 000 D abrogée (LF 2023, art. 42, édition arabe ; rubrique à relever, D3).

  Les deux sont rattachées à la rupture de 2004. L'autre lecture de 2023 est au § 8.
- **Ce qui y naît d'autre**, une phrase et des renvois :
  - les rentes viagères des contrats d'assurance-vie sont exonérées (art. 44, fiche 3) ;
  - le plafond du CEA est porté à 20 000 D (art. 45-46, fiche 4).
- **Clés** : `lf-2004` (art. 61 à 63, p. 3730 ; art. 71, p. 3732), `dgi-nc-8-2004`, `lf-2005` (art. 69, p. 3442), `lf-2011` (art. 41, p. 3474-3476), `lf-2023` (art. 42, p. 4068), `dgi-nc-3-2023`.

#### `#### 2014 : imposer les dividendes {#sec-irpp-epargne-2014}`

- **Ce que la loi cherche.** Rubrique des art. 18 et 19 de la LF 2014 : « Réduction du taux de l'impôt sur les sociétés et imposition des bénéfices distribués ».
- **Contexte : la seule réforme dont N donne le contexte.** Deux citations du rapport de synthèse des groupes de travail de la réforme fiscale, ministère des Finances, novembre 2013, p. 24, partie « Diagnostic du système fiscal » (`minfin-cnf-2013-synthese`) :
  - « les dividendes se trouvent totalement défiscalisés peu importe que les bénéfices générés au niveau de la société distributrice aient fait l'objet d'une imposition ou pas » ;
  - et, pour les intérêts, « la combinaison du prélèvement à la source de 20 % et du respect d'un secret bancaire fait que de nombreux contribuables préfèrent ne pas déclarer les revenus mobiliers ».

  Le rapport est attribué au ministère, comme N le demande. **Les estimations de −116,3 et −221,6 MD ne sont pas prévues** : elles sont tirées d'un inventaire, non relues, et leur méthode n'est pas décrite.
- **Avant → après** :
  - art. 38-10 abrogé : exonération générale → retenue de 5 % sur les revenus distribués (52-I-c *bis*), parts de FCP comprises, **libératoire**, pour les distributions faites à partir du 1^er^ janvier 2015 ;
  - distributions prélevées sur les fonds propres au 31 décembre 2013, mentionnées dans les notes aux états financiers : exclues ;
  - personnes physiques dont les revenus distribués ne dépassent pas 10 000 D par an : retenue déductible ou restituable (§ 6).

  L'articulation entre cette restitution et le caractère libératoire est à confirmer (D4). Le rendu dit ce que dit l'article, et un TODO porte la question.
- **La contrepartie à l'IS** : une phrase. IS de 30 % → 25 % par la même loi (art. 18), avec un lien vers l'IS, sans recopie.
- **Étapes** :
  - 2015 : établissements stables des non-résidents (LF 2015, art. 25) ;
  - **2018** : « Relèvement du taux d'imposition des bénéfices distribués », 5 % → 10 % pour les distributions à partir du 1^er^ janvier 2018 (LF 2018, art. 46 ; NC 14/2018). La rubrique dit « relèvement » : c'est une étape.
- **Entre-temps 2018-2020, une phrase** : le régime des jetons de présence est étendu aux rémunérations des membres des conseils en 2017 (registre B).
- **Clés** : `lf-2014` (art. 18 et 19, p. 3670-3671), `minfin-cnf-2013-synthese` (p. 24), `lf-2015` (art. 25, p. 3466), `lf-2018` (art. 46, p. 4286), `dgi-nc-14-2018`.

#### `#### 2020-2022 : trois régimes en trois ans pour les intérêts {#sec-irpp-epargne-2020}`

- **Pourquoi une seule réforme.** Trois textes voisins, de même objet (art. 52-II), chacun lu, défont l'un après l'autre ce que le précédent a posé. L'autre lecture, trois réformes, est au § 8.
- **Les trois temps.** Chacun a sa phrase « ce que la loi cherche » et son avant → après.
  1. **10 juin 2020.** Décret-loi n° 2020-30, art. 12, lu en édition arabe. Intitulé du décret-loi : « portant des mesures pour la consolidation des assises de la solidarité nationale et le soutien des personnes et des entreprises suite aux répercussions de la propagation du Coronavirus ». C'est le contexte, en ses mots. L'objet propre de l'art. 12 n'est pas relevé (D3).

     Nouveau 52-II-2 *bis* : les dépôts à terme et produits similaires rémunérés au-delà du TMM moins un point au 1^er^ janvier subissent une retenue **définitive et non restituable de 35 %**, quel que soit le bénéficiaire, devises et dinars convertibles exclus. Glossaire : `#g-tmm`.

     Ne pas écrire que ces revenus sortent du revenu global : ce n'est pas établi (D3). Un TODO HTML porte la question.
  2. **1^er^ janvier 2021.** « Révision du régime fiscal des revenus de capitaux mobiliers » (LF 2021, art. 17) :
     - fin des 35 % et de 52-II-2 ;
     - la retenue de 20 % devient « définitive et non restituable […] nonobstant le régime fiscal du bénéficiaire », donc **libératoire** pour tous (NC 1/2022) ;
     - les intérêts sortent du barème ; exonérations et déductions maintenues.
  3. **1^er^ janvier 2022.** « Réinstauration de la retenue à la source déductible due sur les revenus de capitaux mobiliers » (LF 2022, art. 38) :
     - la retenue de 20 % redevient **imputable** ;
     - 52-II-2 est rétabli, étendu aux fonds d'amorçage et aux FCPR (fiche 6) ;
     - objet donné par la NC 1/2022, citée sur place comme note commune : « encourager les personnes physiques à adhérer aux différents mécanismes d'épargne, […] renforcer la justice fiscale ».
- **Point de date, dans le texte principal** : ni restitution ni rattrapage des montants de 2021 (NC 1/2022).
- **Clés** : `decret-loi-2020-30` (art. 12 et 17, p. 1410 et 1413, édition arabe), `lf-2021` (art. 17, p. 3129-3130 ; art. 42 pour la date), `lf-2022` (art. 38, p. 3090), `dgi-nc-1-2022`.

#### `#### Les registres des textes {#sec-irpp-epargne-registres}`

**Une phrase** : chaque registre donne, pour un élément, tous les textes dans l'ordre des dates, avec leur portée. Trois blocs repliés, colonnes « Date d'effet | Texte, article (lien d'ancre `#r-…`) | Ce qui change (avant → après) | Caractère de la retenue | Portée ». Contenu ligne par ligne au § 3.

- `:::: {.chronologie-repliable titre="La retenue sur les intérêts, 1990-2026 : taux, caractère libératoire ou imputable, textes"}` → `#tbl-irpp-epargne-registre-interets`
- `:::: {.chronologie-repliable titre="Les revenus distribués, 1990-2026 : exonération, retenue, jetons de présence, textes"}` → `#tbl-irpp-epargne-registre-distribues`
- `:::: {.chronologie-repliable titre="La plus-value de cession de titres, 2004-2026 : champ, taux, exonérations, franchise, textes"}` → `#tbl-irpp-epargne-registre-plus-values`

**Pas de chronologie générale de plus.** `#tbl-irpp-reformes` en tient lieu pour le chapitre (§ 5, point R12).

### `### L'état du droit au 1er janvier 2026 {#sec-irpp-epargne-etat}`

- **Essentiel.** En 2026, trois revenus, trois régimes :
  - intérêts au barème, 20 % imputables ;
  - dividendes à 10 % libératoires ;
  - plus-values à 0, 10 ou 15 %, hors barème.
- **Vue d'ensemble, au premier plan et non repliée** : `#tbl-irpp-epargne-etat`, une ligne par nature de revenu. Colonnes :
  - Revenu ;
  - Taux ;
  - **Caractère (libératoire, imputable, définitive)** ;
  - Exonérations et plafonds en vigueur ;
  - Population couverte.

  Lignes : intérêts (dépôts, obligations, bons du Trésor) ; intérêts des comptes spéciaux et des emprunts obligataires sous plafond ; dividendes et parts de fonds ; plus-value sur action cotée ; plus-value sur action non cotée ou part sociale ; revenus servis aux non-résidents (renvoi à la fiche 7).
- **La colonne « population couverte »** est exigée par le § 4 des conventions. N ne donne aucun chiffre : les cases restent vides, avec un `<!-- TODO (documentaliste) : … -->` par ligne (nombre de titulaires de CEA ou de contrats d'assurance-vie, foyers déclarant des revenus de capitaux). Rien n'est écrit dans le rendu sur cette absence.
- **Points, deux** :
  - la restitution des retenues sur les dividendes sous 10 000 D figure toujours à l'art. 52-II-1 (code consolidé de 2025), avec le TODO D4 ;
  - l'exonération des actions cotées détenues au-delà de l'année suivant l'acquisition demeure (38-17).
- **Repli** : aucun. C'est l'état du droit en vigueur.
- **Clés** : celles des dernières lignes des registres, par lien `#r-…`.

### `### Les dispositifs d'épargne aidée {#sec-irpp-epargne-dispositifs}`

**Chapeau, deux phrases.** Les avantages se cumulent dans la limite du minimum d'impôt de l'art. 12 *bis* de la loi n° 89-114, avec un lien vers `#tbl-plafonnement` ; le chapeau dit lesquels y sont soumis. Glossaire : `#g-minimum-impot`, `#g-deductions-communes`.

Gabarit de chaque `####` :
1. Objet, en une phrase.
2. « Né de… » : la réforme de l'épine ou le texte.
3. Le mécanisme, en deux ou trois phrases.
4. L'évolution, avec ses ruptures propres en prose.
5. Un bloc replié « registre ».

Viser 150 à 250 mots visibles par fiche.

#### `#### Les comptes spéciaux d'épargne et les emprunts obligataires {#sec-irpp-epargne-comptes-speciaux}`

- **Objet.** Déduction des intérêts du revenu imposable, dans la limite d'un plafond (39 § II). Glossaire : `#g-comptes-speciaux-epargne`.
- **Né en 1990**, élargi en 1992 (CENT, plafond global de 1 500 D).
- **Ruptures propres** :
  - 1992, le compte d'épargne-emprunts obligataires, supprimé en 1997 ;
  - 2022, la déduction distincte des emprunts obligataires verts, socialement responsables et durables (II *bis*).
- **Ajustements** : 2017 (5 000 D, dont 3 000 D) ; 2022 (10 000 D, dont 6 000 D) ; 2024 (bons du Trésor assimilables admis, plafonds inchangés).
- **Premier plan : `#tbl-epargne`, déplacé avec son identifiant.** C'est un tableau court, qui ne se replie pas.
  - Sa ligne « 1990 → 1991 ? » et la cellule « l'année de bascule… n'est pas établie… » sont à corriger : la LF 1992, art. 30, est lue à l'image.
  - L'année de revenus reste à fixer (D6). En attendant : « — » et un TODO, jamais « n'est pas établi ici ».
  - La colonne « Texte » reçoit les liens `#r-…` vers le registre.
- **Repli** : `:::: {.chronologie-repliable titre="Comptes spéciaux d'épargne et emprunts obligataires, 1990-2026 : textes et plafonds"}`. Il contient aussi le compte d'épargne-emprunts obligataires (1992, 1997).
- **Clés** : `code-irpp-is-1990` (art. 39), `lf-1992` (art. 30, 33), `lf-1997` (art. 33), `lf-2017` (art. 13), `dgi-nc-2-2017`, `lf-2022` (art. 24, 29), `dgi-nc-1-2022`, `lf-2024` (art. 34).

#### `#### L'épargne exonérée : logement, devises, études {#sec-irpp-epargne-exoneree}`

- **Objet.** Intérêts exonérés sans plafond (38-7, 38-8, 38-12).
- **Né en 1990** (naissances groupées). En 1992, les livrets de la CENT passent à la déduction plafonnée (fiche précédente). En 1999, les dépôts en devises sortent du champ de la retenue (LF 1999, art. 43).
- **Rupture propre** : 1999, les comptes d'épargne pour les études (LF 1999, art. 45).
- **Repli** : `:::: {.chronologie-repliable titre="Épargne exonérée, 1990-2026 : textes"}`. Le décret n° 99-1923 n'y figure pas tant qu'il n'est pas lu (TODO).
- La phrase actuelle de `#sec-irpp-capitaux` sur les comptes courants entre industriels, commerçants ou exploitants agricoles **reste** dans `#sec-irpp-capitaux`, parce que ce n'est pas de l'épargne.
- **Clés** : `code-irpp-is-1990` (art. 38), `lf-1992` (art. 30), `lf-1999` (art. 43, 45, p. 2505-2506).

#### `#### L'assurance-vie {#sec-irpp-epargne-assurance-vie}`

- **Objet.** Déduction des primes des contrats d'assurance-vie et de capitalisation (39 § I-2) ; rentes exonérées depuis 2004 (38-16).
- **Né en 1990**, sous forme d'une déduction familiale : 200 D, plus 100 D pour le conjoint et 50 D par enfant, pour les quatre premiers.
- **Ruptures propres, deux** :
  1. **LFC 2012, art. 42** : plafond unique de 10 000 D, majorations familiales supprimées. La déduction cesse d'être familiale pour devenir une déduction d'épargne. La date de rattachement n'est pas établie (D6), d'où « — » et un TODO.
  2. **LF 2021, art. 16**, « Encouragement de l'épargne à moyen et long terme via les comptes épargne en actions et les contrats d'assurance-vie et de capitalisation » : 100 000 D (revenus de 2020), et première soumission au minimum de l'art. 12 *bis*.
- **Étapes et ajustements** :
  - 800 D (LF 1998, revenus 1997, date dérivée) ;
  - 1 200 D et rachat sans pénalités après cinq ans (LF 2008, primes de 2007) ;
  - durée minimale de dix ans et contrats collectifs (LF 2014, étape de 2012) ;
  - durée de huit ans (LF 2018).
- **Premier plan** : un tableau court des plafonds, `#tbl-irpp-epargne-assurance-vie`, fait main, avec `<!-- TODO (rédacteur) : remplacer par un tableau engendré -->`. Le paramètre de l'arbre date le palier de 10 000 D de 2013 et le source à la LF 2014 : il est faux (backlog-modele).
- **Remplace** le paragraphe actuel de `#sec-irpp-deductions` (l. 608), dont la phrase « le contenu de sept textes modificatifs n'est pas encore établi ici » enfreint la règle sur le jargon de dépouillement et disparaît. Remplace aussi les deux TODO des l. 610 et 612-617 : six des sept textes sont lus. Il reste un TODO, plus court, pour la LF 2020, art. 12, pour la LF 2002, art. 45 (D7) et pour le rattachement de la LFC 2012.
- **Repli** : `:::: {.chronologie-repliable titre="Assurance-vie, 1990-2026 : plafonds de la déduction des primes, durées, textes"}`.
- **Clés** : `code-irpp-is-1990` (art. 39), `lf-1998` (art. 52, p. 2439), `lf-2004` (art. 44), `loi-2007-70-lf-2008` (art. 23, p. 4360), `dgi-nc-10-2008`, `lfc-2012` (art. 42, p. 929), `lf-2014` (art. 24, p. 3671), `lf-2018` (art. 27, p. 4275), `dgi-nc-2-2018`, `lf-2021` (art. 16), `dgi-nc-1-2021`.

#### `#### Le compte épargne en actions {#sec-irpp-epargne-cea}`

- **Objet.** Déduction des sommes déposées sur un compte bloqué cinq ans et investi en actions cotées et en bons du Trésor assimilables (39 § VIII). Glossaire : `#g-compte-epargne-actions`.
- **Né de la réforme de 1999** : 50 % des dépôts, dans la limite de 5 000 D.
- **Étapes** :
  - 2002 : OPCVM admis (LF 2002, art. 30-31, lu texte, page à recouper) ;
  - revenus 2003 : 20 000 D, sans quote-part (LF 2004, art. 45-46 ; NC 16/2004) ;
  - 50 000 D (décret-loi n° 2011-28, art. 4 ; rattachement non établi, D6) ;
  - revenus 2020 : 100 000 D (LF 2021, art. 16, même rubrique que l'assurance-vie).
- **Pas de rupture propre**, la naissance appartenant à l'épine. La loi relève le plafond par paliers : ce sont des étapes de la rupture de 1999.
- **Premier plan** : `#tbl-irpp-epargne-cea`, tableau court fait main, avec le TODO du rédacteur. Le paramètre de l'arbre est faux : 50 000 D en 2001, art. 24 au lieu de l'art. 16.
- **Repli** : `:::: {.chronologie-repliable titre="Compte épargne en actions, 1999-2026 : plafonds et textes"}`.
- **Clés** : `loi-99-92-relance-marche-financier` (art. 4), `lf-2002` ou `loi2001-123-lf2002` (art. 30-31 ; clé à trancher par le bibliographe, B1), `lf-2004` (art. 45-46), `dgi-nc-16-2004`, `decret-loi-2011-28` (art. 4, p. 488), `lf-2021` (art. 16), `dgi-nc-1-2021`.

#### `#### Le compte épargne pour l'investissement {#sec-irpp-epargne-cei}`

- **Objet.** Déduction des dépôts destinés à financer, dans les cinq ans, un projet d'investissement (39 *bis*), et exonération des intérêts dans une limite (38-15). Glossaire : `#g-compte-epargne-investissement`.
- **Né en 2003.** Les articles 21 à 23 de la LF 2003 ne sont connus que par la NC 35/2003. La fiche décrit le compte **d'après la note commune**, citée sur place : déduction de 20 000 D, intérêts exonérés dans la limite de 2 000 D. Sa ligne de registre porte « — » dans la colonne « Portée », avec le TODO D5.
- **Ajustement** : 2017, dépôts 50 000 D, intérêts 4 000 D (LF 2018, art. 27 ; NC 2/2018).
- **Repli** : `:::: {.chronologie-repliable titre="Compte épargne pour l'investissement, 2003-2026 : plafonds et textes"}`. Le tableau des deux plafonds y est fait main, avec le TODO du rédacteur.
- **Clés** : `dgi-nc-35-2003`, `lf-2018` (art. 27), `dgi-nc-2-2018`.

#### `#### Les fonds et les organismes exonérés : la retenue définitive {#sec-irpp-epargne-fonds}`

- **Objet.** Pour une personne morale qui ne paie pas l'IS, ou pour un fonds, la retenue sur les revenus de capitaux mobiliers est définitive et non restituable (52-II-2). Glossaire : `#g-opcvm`, `#g-retenue-definitive-non-restituable`.
- **Né de la réforme de 1992.**
  - 2002 : extension aux FCP en valeurs mobilières, d'après la NC 45/2002. Fonds communs de créances : 20 %, imputables sur la retenue due aux copropriétaires.
  - 2021 : 52-II-2 abrogé (réforme 2020-2022).
  - 2022 : rétabli et étendu aux fonds d'amorçage et aux FCPR (réforme 2020-2022).
- **Points qui restent en TODO, sans phrase dans le rendu** :
  - le régime des SICAV (D8) ;
  - la déduction de l'art. 39 *ter* (loi n° 2005-59, annotation seule, D5) ;
  - le décret-loi n° 2011-100 (parts de fonds, plus-values, D5).

  L'art. 39 *ter* reste nommé d'une proposition, comme aujourd'hui à la l. 632 : « parts de fonds d'amorçage et de fonds communs de placement à risque (article 39 *ter*) ». Aucun contenu tant qu'il n'est pas lu.
- **Fiche courte, 150 mots au plus.**
- **Repli** : `:::: {.chronologie-repliable titre="Retenue définitive des organismes exonérés et des fonds, 1992-2026 : textes"}`.
- **Clés** : `lf-1992` (art. 31), `lf-1999` (art. 43), `dgi-nc-45-2002`, `lf-2021` (art. 17), `lf-2022` (art. 38), `dgi-nc-1-2022`.

#### `#### Les non-résidents {#sec-irpp-epargne-non-residents}`

- **Objet.** Pour un bénéficiaire non résident et non établi, la retenue est libératoire : elle est le seul impôt dû en Tunisie sur ce revenu.
- **Né en 1990.** 15 % libératoires, puis 20 % en 1997, aligné sur le régime commun.
- **Rupture propre** : 2011. Les plus-values de cession de titres des non-résidents deviennent imposables, d'abord par une retenue sur le prix (LF 2011, art. 41), puis sur la plus-value (« e *bis* », LF 2012, art. 15), avec un plafond en pourcentage du prix (LFC 2012, art. 12).
- **Ajustements alignés sur les taux de l'IS** : 30 → 25 % (2014), → 15 % (2021), → 20 % (2025), avec un lien vers l'IS.
- **Intérêts des prêts des banques non établies (e)** : 2,5 % (1995), 5 % (2011), 10 % (2018).
- **Le taux de 25 %** pour les États à régime fiscal privilégié (LF 2014, art. 44 ; LF 2019, art. 35) reste en TODO, en annotation seule (D5).
- **Premier plan** : rien d'autre que la prose, 150 mots.
- **Repli** : `:::: {.chronologie-repliable titre="Non-résidents, 1990-2026 : retenues sur les intérêts, les dividendes et les plus-values, textes"}`.
- **Clés** : `code-irpp-is-1990` (art. 52), `lf-1992` (art. 31), `lf-1995` (art. 54, p. 2046), `lf-1997`, `lf-2005` (art. 69), `lf-2011` (art. 41, 43), `lf-2012` (art. 15, p. 5), `lfc-2012` (art. 12, p. 923), `lf-2014` (art. 18), `lf-2015` (art. 25), `lf-2018` (art. 47), `lf-2021` (art. 14), `lf-2025` (art. 37, p. 3431).

### `### La longue période : ce que coûtent les avantages à l'épargne {#sec-irpp-epargne-longue-periode}`

- **Essentiel.** Selon les rapports du ministère des Finances, les déductions liées à l'épargne coûtent quelques dizaines de millions de dinars par an de 2017 à 2023, principalement au titre du CEA et de l'assurance-vie. Les intérêts exonérés ne sont pas valorisés.
- **Vue d'ensemble : `#fig-irpp-epargne-depenses-fiscales`, faisable dès maintenant.**
  - Source : série `depenses-fiscales-detail` du cache, rapports annexés aux lois de finances de 2021, 2024 et 2025.
  - Mesures : CEA `111103909`, CEI `111103912`, assurance-vie `111103901`, plus-value sur actions `111103809`, parts de fonds d'amorçage et de fonds communs de placement (39 *ter*) `111103913`, SICAR et FCPR `111107701` et `111107703`. Les mesures `111103906` à `111103911`, `111103914` et `111103915` visent d'autres revenus (logement et restauration d'étudiants, courtage, Fonds national de l'emploi, entreprises en difficulté, PME) : hors de la figure.
  - **L'assurance-vie n'est pas valorisée dans le rapport de 2021** (exercices 2017-2019, « non valorisée » dans le cache). Elle n'apparaît qu'à partir de l'exercice 2020, l'année où le plafond passe à 100 000 D. La légende le dit, pour que le saut ne passe pas pour l'effet de la réforme. À confirmer sur le rapport (p. 36-37) avant d'écrire.
  - **Règle des millésimes, à dire en légende** : une courbe par mesure, prise dans le rapport le plus récent pour chaque exercice, avec des marques distinctes pour les valeurs révisées d'un rapport à l'autre. Les écarts sont grands pour 2022 : CEA 13,71 MD (rapport de 2024) contre 36,43 MD (rapport de 2025) ; assurance-vie 15,96 contre 44,30 MD.
  - Méthode du rapport : renvoi à `#sec-df-rapport`, perte de recettes à comportement inchangé.
  - Famille : budgétaire seul.
- **Points, trois** :
  1. Le domaine « Intérêts dépôts et épargne » du rapport de 2021 (26,64 / 30,23 / 2,70 MD pour 2017-2019) est **exactement la somme CEA + CEI** du même rapport (24,631 + 2,007 = 26,638, etc.). Ce ne sont pas des intérêts exonérés. N § 1 (« coût des exonérations d'intérêts ») et N § 7 sont à corriger sur ce point, et le rendu ne doit pas reprendre ce libellé.
  2. Épargne logement, devises, comptes d'études et comptes spéciaux : « non valorisées » par les rapports. On le dit en une phrase : c'est un constat sur la source, pas une recherche.
  3. La chute de 2019 dans le rapport de 2021, puis la remontée dans les rapports suivants, n'est pas expliquée par le rapport. Le rendu la constate sans l'expliquer.
- **Figure seconde, faisable après un travail de données** : `#fig-irpp-epargne-plafonds`. Plafonds de la déduction (comptes spéciaux, assurance-vie, CEA, CEI) en dinars courants et constants, 1990-2026.
  - Données : un générateur `scripts/generate_epargne_capital_series.py`, sur le modèle de `generate_forfait_bic_series.py`, écrit `precis/_seriescache/epargne-plafonds.csv` depuis un YAML de paramètres datés tiré de N § 4.5, une référence par ligne. L'indice de prix vient de `ipc-longue-periode`.
  - Un `<!-- TODO (modéliste) : … -->` demande de remplacer le générateur par une lecture de l'arbre quand les paramètres seront versés.
  - Le rendu ne nomme pas le modèle.
- **Encours de l'épargne, figure tierce**, faisable après un travail de données : épargne bancaire et postale, dépôts à terme, 2003-2024, rapportés au PIB avec sa base dite.
  - Les données sont dans `tunisia-data/data/processed/bct/agregats_monnaie_2003_2024.csv`, mais **absentes de `catalog.yml`** : il faut une entrée de catalogue, une fiche `sources/` et une version dans le cache.
  - La provenance de `epargne_cep.csv` n'est pas documentée.
  - Facultative : à décider selon la place.
- **Recettes des retenues** : aucune série ventilée (N § 7). Aucune phrase dans le rendu, un TODO (documentaliste) seulement.
- **Repli** : la table des valeurs de la figure, par mesure et par millésime, dans `:::: {.chronologie-repliable titre="Coût des déductions liées à l'épargne selon les rapports des dépenses fiscales, 2017-2023, par rapport"}`.
- **Clés** : `gbo-depenses-fiscales` (rapport de 2021, p. 32 et 36-37 ; rapports de 2024 et 2025 à verser si leurs clés manquent, B2).

### `### Ce qu'en dit l'économie {#sec-irpp-epargne-economie}`

- **La fiche source n'existe pas** au 20 octobre 2026 : `docs/notes/eco-epargne-capital.md`. La section est prévue et pas remplie. Le rédacteur pose un titre et un `<!-- TODO (économiste) : … -->`, ou attend la fiche.
- **Questions que la fiche devrait traiter**, pour l'économiste, selon le gabarit fixe d'une page au plus :
  1. l'imposition duale ou synthétique des revenus du capital : ce que coûte un taux proportionnel séparé du barème, en recettes et en progressivité ;
  2. l'effet du taux sur les dividendes sur les distributions et sur leur calendrier. La Tunisie offre deux dates nettes, 2015 et 2018, et l'exclusion des fonds propres de 2013 invite à anticiper ;
  3. l'effet de verrouillage de la plus-value (`#g-effet-de-verrouillage`) et la condition de durée de détention (2011, 2023) ;
  4. l'efficacité des déductions plafonnées pour l'épargne (CEA, assurance-vie) : épargne nouvelle ou déplacée, et incidence par décile ;
  5. le prélèvement à la source et la déclaration : ce que dit le rapport de 2013, et ce que dit la littérature sur le secret bancaire.
- **Garde-fous** : aucun chiffre de cette section n'entre dans un tableau ou une figure de série ; dernière ligne « Littérature arrêtée au <mois année> ».
- **Hors du gabarit de fin de chapitre, à signaler.** La section est un `###` à l'intérieur de `#sec-irpp-epargne`, et non la dernière section du chapitre. C'est un effet direct de la décision de loger une seconde épine dans le fichier (§ 9).

---

## 3. Les grandes réformes et le classement des textes

### 3.1 Tableau des réformes (vue d'ensemble de `### Les grandes réformes`)

| Réforme | Textes, articles (lus) | Ce que la loi cherche (ses mots) | Avant → après | Naissances | Étapes |
|---|---|---|---|---|---|
| 1992 | LF 1992, art. 30, 31, 33 (image) | « harmonisation du régime fiscal applicable aux différentes formes d'épargne » | 10 % et 15 % → 15 % uniforme ; anonymes 35 % → 25 et 35 %, libératoires ; 52-II-2 à 20 % définitive | compte d'épargne-emprunts obligataires ; retenue définitive des organismes exonérés | 1997 « unification » à 20 %, fin des libératoires anonymes |
| 1999 | loi n° 99-92, art. 4 (texte décodé) | « relance du marché financier » | — → CEA, 50 % des dépôts, 5 000 D | CEA (et IS à 20 % des sociétés cotées : IS) | CEA 2002, 2003, 2011, 2020 (fiche) |
| 2004 | LF 2004, art. 61-63 (texte décodé ; relecture à l'image demandée par N) | « Soumission de la plus-value provenant de la cession des actions et des parts sociales à l'impôt sur le revenu » | plus-value hors champ → 10 %, actions cotées exonérées, franchise de 10 000 D | rentes d'assurance-vie exonérées | 2011 « Rationalisation de l'exonération… » ; 2023 deux taux |
| 2014 | LF 2014, art. 19 (image) | « imposition des bénéfices distribués » | dividendes exonérés → 5 % libératoires (2015) | — | 2015 établissements stables ; 2018 « Relèvement du taux… », 10 % |
| 2020-2022 | DL 2020-30, art. 12 (AR) ; LF 2021, art. 17 (texte) ; LF 2022, art. 38 (texte) | « Révision du régime fiscal des revenus de capitaux mobiliers » ; « Réinstauration de la retenue à la source déductible » | 20 % imputable → 35 % définitive sur certains dépôts à terme → 20 % libératoire → 20 % imputable | — | — |

### 3.2 Registre A : la retenue sur les intérêts (`#tbl-irpp-epargne-registre-interets`)

| Date d'effet | Texte | Contenu (avant → après) | Caractère | Portée | État (N) |
|---|---|---|---|---|---|
| revenus 1990 | code, art. 52, 54 | 10 % comptes spéciaux ; 15 % autres ; 35 % bons de caisse anonymes | imputable ; libératoire (anonymes, non-résidents) | mise en place | image |
| 2 janvier 1992 (dérivée) | LF 1992, art. 31 | 15 % uniforme ; 25 % et 35 % anonymes ; 52-II-2 | imputable ; libératoire (anonymes) ; définitive (organismes exonérés) | **rupture 1992** | image |
| 1^er^ janvier 1997 | LF 1997, art. 30-32 | 15 % → 20 % ; fin du 35 % et du libératoire anonyme | imputable | étape (1992) ; autre lecture : rupture | texte |
| 1^er^ janvier 1999 | LF 1999, art. 43 | devises et dinars convertibles hors retenue ; mention des banques offshore retirée | — | ajustement | texte |
| 1^er^ janvier 2004 | LF 2004, art. 71 ; NC 8/2004 | 52-II-1 récrit : la retenue est « libératoire de l'impôt sur le revenu ou de l'impôt sur les sociétés au titre des sommes prévues par les alinéas b, c et e », sans réserve des non-résidents ; la NC 8/2004 la dit imputable pour les résidents, qui déclarent ces revenus dans leur revenu global | imputable (NC 8/2004) | ajustement | image ; NC lue |
| 1^er^ janvier 2005 | LF 2005, art. 69 ; NC 13/2005 | 52-II-1 récrit : libératoire au titre des alinéas b et c « servies aux non résidents et non établis », et de l'alinéa e ; jetons de présence à 20 % (registre B) | imputable | ajustement | texte |
| 10 juin 2020 | DL 2020-30, art. 12 | 35 % sur les dépôts à terme au-delà du TMM moins un point | définitive | étape (2020-2022) ; autre lecture : rupture | AR |
| 1^er^ janvier 2021 | LF 2021, art. 17 ; NC 1/2022 | 35 % abrogé ; 20 % définitive pour tous | libératoire | **rupture 2020-2022** | texte |
| 1^er^ janvier 2022 | LF 2022, art. 38 ; NC 1/2022 | « Réinstauration… déductible » | imputable | étape (2020-2022 : retour) | texte |

Restent hors du rendu, en TODO :
- LF 2000, art. 57, et décret n° 2007-1870 (titres d'emprunt négociables), non lus ;
- bons du Trésor : aucune modification, une phrase seulement (art. 34-1).

### 3.3 Registre B : les revenus distribués (`#tbl-irpp-epargne-registre-distribues`)

| Date d'effet | Texte | Contenu | Caractère | Portée | État |
|---|---|---|---|---|---|
| revenus 1990 | code, art. 38-10 | dividendes exonérés | — | mise en place | OCR ; relecture à l'image demandée par N |
| 1^er^ janvier 1995 | LF 1995, art. 50-53 | jetons de présence : exclus de l'exonération, 15 % | imputable | ajustement | texte ; page à confirmer (D9) |
| 1^er^ janvier 2005 | LF 2005, art. 69 | jetons 15 % → 20 % | imputable | ajustement | texte |
| distributions à partir du 1^er^ janvier 2015 | LF 2014, art. 19 | 38-10 abrogé ; 5 % ; restitution sous 10 000 D ; fonds propres de 2013 exclus | libératoire | **rupture 2014** | image |
| 1^er^ janvier 2015 | LF 2015, art. 25 | c *bis* étendu aux établissements stables | libératoire | étape (2014) | texte |
| montants payés à partir du 1^er^ janvier 2017 | LF 2017, art. 30 | jetons → rémunérations des membres des conseils, directoires et comités | imputable | ajustement | texte |
| distributions à partir du 1^er^ janvier 2018 | LF 2018, art. 46 ; NC 14/2018 | 5 % → 10 % | libératoire | étape (2014) | texte |

Contexte et contrepartie : la ligne de la LF 2014, art. 18 (IS 25 %) vit à l'IS. Elle n'entre pas ici.

### 3.4 Registre C : la plus-value de cession de titres (`#tbl-irpp-epargne-registre-plus-values`)

| Date d'effet | Texte | Contenu | Caractère | Portée | État |
|---|---|---|---|---|---|
| cessions à partir du 1^er^ janvier 2004 | LF 2004, art. 61-63 | 31 *bis* ; 10 % ; exonérations 38-17 ; franchise de 10 000 D | proportionnel, hors barème | **rupture 2004** | texte décodé |
| cessions à partir du 1^er^ janvier 2011 | LF 2011, art. 41 § 5 | exonération des cotées acquises depuis 2011 sous condition de durée | proportionnel | étape (2004) | texte |
| cessions à partir du 1^er^ janvier 2023 | LF 2023, art. 42 ; NC 3/2023 | 10 % et 15 % selon la cotation et la durée ; franchise abrogée | proportionnel | étape (2004) ; autre lecture : rupture | AR ; NC lue |

Restent en TODO, hors du rendu :
- LF 2007, art. 32 (38-17), annotation ;
- décret-loi n° 2011-100, art. 7-9 (parts de fonds, 2012), annotation.

### 3.5 Fiches : classement

| Fiche | Texte | Portée | Rattachement | État |
|---|---|---|---|---|
| 1 Comptes spéciaux | code, art. 39 § II | mise en place | 1990 | image/OCR |
| 1 | LF 1992, art. 30 | étape | 1992 | image |
| 1 | LF 1992, art. 33 (compte d'épargne-emprunts obligataires) | rupture propre, née de 1992 | 1992 | image |
| 1 | LF 1997, art. 33 | étape (1992) : fin du compte | 1997 | texte |
| 1 | LF 2017, art. 13 | ajustement | revenus 2016 | déjà au précis |
| 1 | LF 2022, art. 24 | ajustement | revenus 2021 | déjà au précis |
| 1 | LF 2022, art. 29 (II *bis*) | rupture propre | — | déjà au précis |
| 1 | LF 2024, art. 34 | ajustement | — | déjà au précis |
| 2 Épargne exonérée | code, art. 38-7 et 38-8 | mise en place | 1990 | OCR |
| 2 | LF 1992, art. 30 | étape (1992) | 1992 | image |
| 2 | LF 1999, art. 43 | ajustement | 1999 | texte |
| 2 | LF 1999, art. 45 | rupture propre | 1999 | texte |
| 3 Assurance-vie | code, art. 39 § I-2 | mise en place | 1990 | texte |
| 3 | LF 1998, art. 52 | ajustement | revenus 1997 (dérivée) | texte |
| 3 | LF 2004, art. 44 (38-16) | ajustement | 2004 | texte décodé |
| 3 | LF 2008, art. 23 ; NC 10/2008 | ajustement | primes de 2007 | texte |
| 3 | LFC 2012, art. 42 | **rupture propre** | — (D6) | texte |
| 3 | LF 2014, art. 24 | étape (2012) | 2014 | image |
| 3 | LF 2018, art. 27 § 3 | ajustement | contrats de 2018 | texte |
| 3 | LF 2021, art. 16 | **rupture propre** | revenus 2020 | déjà au précis |
| 3 | LF 2002, art. 45 ; LF 2020, art. 12 | — | — | non relevés dans N (D7) |
| 4 CEA | loi n° 99-92, art. 4 | rupture (épine 1999) | — (D6) | texte décodé |
| 4 | LF 2002, art. 30-31 | étape (1999) | 2002 | texte décodé |
| 4 | LF 2004, art. 45-46 ; NC 16/2004 | étape (1999) | revenus 2003 | texte ; NC |
| 4 | DL 2011-28, art. 4 | étape (1999) | — (D6) | texte |
| 4 | LF 2021, art. 16 | étape (1999) | revenus 2020 | texte |
| 5 CEI | LF 2003, art. 21-23 (par NC 35/2003) | « — » (création, non portée tant que non lue) | 2003 | NC seule (D5) |
| 5 | LF 2018, art. 27 § 1, 2, 4 ; NC 2/2018 | ajustement | dépôts de 2017 | texte |
| 6 Fonds | LF 1992, art. 31 (52-II-2) | née de 1992 | 1992 | image |
| 6 | LF 1999, art. 43 | ajustement | 1999 | texte |
| 6 | LF 2002, art. 21-28 (par NC 45/2002) | « — » | 2002 | NC seule (D5) |
| 6 | loi n° 2005-59, art. 3 | hors rendu (TODO) | — | annotation |
| 6 | LF 2021, art. 17 ; LF 2022, art. 38 | étapes (2020-2022) | 2021, 2022 | texte |
| 7 Non-résidents | code, art. 52-I-c, 52-II | mise en place | 1990 | image |
| 7 | LF 1992, art. 31 ; LF 1997 | étapes | 1992, 1997 | image ; texte |
| 7 | LF 1995, art. 54 (e 2,5 %) | ajustement | 1995 | texte |
| 7 | LF 2005, art. 69 | ajustement | 2005 | texte |
| 7 | LF 2011, art. 41 (plus-values) | **rupture propre** | 2011 | texte |
| 7 | LF 2011, art. 43 (e 5 %) | ajustement | 2011 | texte |
| 7 | LF 2012, art. 15 (e *bis*) | étape (2011) | 2012 | texte |
| 7 | LFC 2012, art. 12 | ajustement | 2012 | texte |
| 7 | LF 2014, art. 18 § 2 ; LF 2021, art. 14 § 4 ; LF 2025, art. 37 § 7 | ajustements (alignés sur l'IS) | 2014, 2021, 2025 | image ; texte ; extrait texte |
| 7 | LF 2018, art. 47 (e 10 %) | ajustement | 2018 | texte |
| 7 | LF 2014, art. 44 ; LF 2019, art. 35-4 (25 %) | hors rendu (TODO) | — | annotation |

## 4. Tableaux et figures

### 4.1 `#tbl-irpp-epargne-taux` : taux marginal légal par placement aux dates des réformes

**Forme.** Le tableau de N § 6 est transposé :
- les lignes sont les dates ; c'était onze colonnes, trop larges pour une page ;
- les plafonds en dinars sont retirés : ils sont dans les fiches et sur `#fig-irpp-epargne-plafonds` ;
- la ligne « 2023-2026 » de N est coupée en deux, parce que la dernière tranche passe de 35 à 40 % aux revenus de 2025 ;
- les colonnes d'épargne aidée (comptes spéciaux, assurance-vie, CEA) sont retirées, parce qu'elles mêlaient taux et plafonds.

Le tableau est fait main, avec `<!-- TODO (rédacteur) : remplacer par un tableau engendré -->`. La colonne « Texte » de chaque ligne renvoie, par lien `#r-…`, aux lignes des registres.

Chaque cellule de taux donne un taux et un caractère, en toutes lettres : « barème (35 %), retenue de 20 % imputable », « 10 %, libératoire ».

| Date | Dernière tranche du barème | Intérêts (dépôt, obligation, bon du Trésor) | Titre anonyme au porteur | Dividende | Plus-value, action cotée | Plus-value, action non cotée, part sociale |
|---|---|---|---|---|---|---|
| revenus 1990 | 35 % [code, art. 44] | barème ; retenue 15 % imputable (10 % comptes spéciaux) [code, art. 52-I-b, c ; 54] | 35 % libératoire (bons de caisse) [art. 52-I-d, 52-II] | exonéré [art. 38-10] | hors champ | hors champ |
| 2 janvier 1992 | 35 % | barème ; 15 % imputable [LF 1992, art. 31] | 25 % (obligations) ou 35 %, libératoire [LF 1992, art. 31] | exonéré | hors champ | hors champ |
| 1^er^ janvier 1997 | 35 % | barème ; 20 % imputable [LF 1997, art. 30-32] | régime commun : barème, 20 % imputable [idem] | exonéré | hors champ | hors champ |
| 1^er^ janvier 2004 | 35 % | barème ; 20 % imputable [NC 8/2004] | — | exonéré | exonérée [LF 2004, art. 61-63 ; 38-17] | 10 %, au-delà de 10 000 D par an [LF 2004, art. 61-63 ; 44-III-3 ; 38-18] |
| 1^er^ janvier 2011 | 35 % | idem | — | exonéré | acquises avant 2011 : exonérées ; acquises depuis le 1^er^ janvier 2011 : exonérées si cédées après la fin de l'année suivant l'achat, sinon 10 % [LF 2011, art. 41] | 10 %, franchise de 10 000 D |
| 1^er^ janvier 2015 | 35 % | idem | — | 5 %, libératoire [LF 2014, art. 19] | idem 2011 | idem |
| 1^er^ janvier 2018 | 35 % | idem | — | 10 %, libératoire [LF 2018, art. 46] | idem | idem |
| 10 juin 2020 | 35 % | barème ; 20 % imputable ; **35 % définitive** sur les dépôts à terme rémunérés au-delà du TMM moins un point [DL 2020-30, art. 12], avec un TODO (D3) : barème en sus ou non | — | 10 %, libératoire | idem | idem |
| 1^er^ janvier 2021 | 35 % | **20 %, libératoire** [LF 2021, art. 17] | — | 10 %, libératoire | idem | idem |
| 1^er^ janvier 2022 | 35 % | barème ; 20 % imputable [LF 2022, art. 38] | — | 10 %, libératoire | idem | idem |
| 1^er^ janvier 2023 | 35 % | idem | — | 10 %, libératoire | exonérée (détention longue) ; 10 % (courte) [LF 2023, art. 42] | 10 % (longue) ; 15 % (courte) ; sans franchise [LF 2023, art. 42] |
| revenus 2025 | **40 %** [LF 2025, art. 36] | barème ; 20 % imputable | — | 10 %, libératoire | idem 2023 | idem 2023 |

**Garde-fous de cellule.**
- **Bas du barème.** « Barème » signifie « taux de la dernière tranche » pour le contribuable du tableau. La note sous le tableau dit qu'au bas du barème la retenue imputable peut être restituée.
- **Restitution sous 10 000 D.** Le caractère « libératoire » des dividendes est celui de l'art. 52-II-1. La restitution sous 10 000 D est signalée en note sous le tableau, d'après l'article, avec le TODO D4.
- **Date des intérêts de 2020.** La cellule de juin 2020 vaut pour les revenus payés à compter du 10 juin 2020. Le sort des intérêts courus avant cette date n'est pas établi (D3) : TODO.
- **Texte de 2005.** La ligne 2005 n'est pas reprise : pour les résidents, rien ne change en 2005.

### 4.2 Autres tableaux et figures

| Identifiant | Contenu | Données | État |
|---|---|---|---|
| `#tbl-irpp-epargne-etat` | état du droit au 1^er^ janvier 2026 | N § 4, dernières lignes | faisable maintenant ; fait main ; colonne population couverte vide avec TODO |
| `#tbl-epargne` | plafond de la déduction des intérêts (39 § II) | existant, déplacé ; ligne 1992 à corriger | faisable maintenant (D6 pour l'année) |
| `#tbl-irpp-epargne-assurance-vie` | plafonds de la prime déductible | N § 4.5 | faisable maintenant ; fait main ; TODO rédacteur (l'arbre est faux) |
| `#tbl-irpp-epargne-cea` | plafonds du CEA | N § 4.5 | idem |
| tableau du CEI (replié) | dépôts et intérêts | N § 4.5 | idem |
| trois registres et sept registres de fiche | § 3 | N § 4 | faisables maintenant |
| `#fig-irpp-epargne-depenses-fiscales` | coût des déductions 2017-2023, par millésime | cache `depenses-fiscales-detail` | **faisable maintenant** (module `figures/`, lecture par `figtools.series()`) |
| `#fig-irpp-epargne-plafonds` | plafonds en dinars courants et constants | générateur à écrire depuis N § 4.5 + `ipc-longue-periode` | après un travail de données (générateur, tests) |
| `#fig-irpp-epargne-taux` (facultative) | taux et caractère par revenu, 1990-2026, en escalier, avec les périodes libératoires ombrées | même générateur | après un travail de données ; à décider : le tableau 4.1 suffit peut-être |
| encours d'épargne (facultative) | épargne bancaire et postale, dépôts à terme, 2003-2024, part du PIB | `tunisia-data/data/processed/bct/agregats_monnaie_2003_2024.csv` | après un travail de données (catalogue, fiche, cache) |

Les paramètres absents ou faux de l'arbre sont déjà inscrits dans `docs/notes/backlog-modele.md` (ligne du 20/10/2026). Le rédacteur n'y ajoute rien. Le texte rendu ne parle jamais du modèle.

### 4.3 Ancres

- **Sections** : `#sec-irpp-epargne`, `-vue`, `-1990`, `-reformes`, `-1992`, `-1999`, `-2004`, `-2014`, `-2020`, `-registres`, `-etat`, `-dispositifs`, `-comptes-speciaux`, `-exoneree`, `-assurance-vie`, `-cea`, `-cei`, `-fonds`, `-non-residents`, `-longue-periode`, `-economie`.
- **Ajouts d'identifiants** : `#sec-irpp-suppression-1990` sur une sous-section existante ; `#sec-is-bourse` et `#sec-is-2014`, proposés dans `_impot_societes.qmd`.
- **Registres** : ancres `#r-epargne-<élément>-<année>[-<suffixe>]`, par exemple `#r-epargne-interets-1992`, `#r-epargne-av-2012`. Une ligne par texte et par registre : un texte qui sert deux registres, comme la LF 1992, art. 31, a deux ancres.
- **Glossaire, entrées de la passe 1** : `#g-retenue-liberatoire`, `#g-retenue-definitive-non-restituable`, `#g-revenus-capitaux-mobiliers`, `#g-revenus-valeurs-mobilieres`, `#g-benefices-distribues`, `#g-plus-value-cession-titres`, `#g-compte-epargne-actions`, `#g-compte-epargne-investissement`, `#g-comptes-speciaux-epargne`, `#g-opcvm`, `#g-tmm`.
- **Glossaire, entrées existantes** : `#g-retenue-a-la-source`, `#g-irpp`, `#g-taux-marginal`, `#g-bareme-irpp`, `#g-minimum-impot`, `#g-deductions-communes`, `#g-css`, `#g-depense-fiscale`, `#g-plus-value-immobiliere`, `#g-effet-de-verrouillage`, `#g-plus-value-nominale`, `#g-impot-societes`.

## 5. Registre de destination des éléments existants du chapitre

| # | Élément (lignes au 20/10/2026) | Destination |
|---|---|---|
| R1 | Point 7 de `#sec-irpp-calcul` (l. 189), « ces versements s'imputent » | reste ; une proposition et un lien sont ajoutés : « sauf les retenues libératoires, qui font sortir le revenu de $R$ (@sec-irpp-epargne) » |
| R2 | Point 9 (l. 191) et paragraphe qui suit $D = I - V$ (l. 247) | restent ; ajouter `@sec-irpp-epargne` après « libératoire » |
| R3 | TODO l. 258-262 (art. 52 et 53) | reste, réduit : l'art. 52 est lu (N § 4.1) ; l'art. 53 (acomptes) reste à lire |
| R4 | `#sec-irpp-capitaux`, l. 586-590 : définitions (art. 29-35, 31 *bis*), absence d'abattement | **premier plan, inchangé** ; un renvoi en tête vers `@sec-irpp-epargne` est ajouté |
| R5 | l. 592, exonérations de l'art. 38 et retenues libératoires | **réduit** à une phrase et un lien. Les éléments vont dans les fiches 2, 5 et 6 et au registre C (plus-values exonérées). Les comptes courants entre industriels restent ici. Les jeux de pari (LF 2018, art. 56) vont à `#sec-irpp-autres` en une proposition ; la citation `[@lf-2018, art. 56]` les suit |
| R6 | l. 594, fin de l'exonération générale des dividendes | **déplacé** dans `#sec-irpp-epargne-2014` et au registre B ; à sa place, une phrase et un lien. Tous les faits sont gardés : abrogation de 38-10, distributions à partir du 1/1/2015, fonds propres au 31/12/2013. Le jugement « principale extension d'assiette » reste dans `#sec-irpp-capitaux` ou passe dans la réforme de 2014, selon le choix du rédacteur ; il n'est pas répété |
| R7 | `#sec-irpp-deductions`, l. 606, cinq charges de l'art. 39 § I | reste ; les primes d'assurance-vie y sont nommées d'une proposition, avec un lien vers la fiche 3 |
| R8 | l. 608, paragraphe des primes d'assurance-vie | **déplacé**, réécrit dans la fiche 3. La phrase de dépouillement disparaît ; l'information subsiste dans le registre de la fiche |
| R9 | TODO l. 610 et l. 612-617 | **fusionnés** en un seul TODO dans la fiche 3 (LF 2020, art. 12 ; LF 2002, art. 45 ; rattachement de la LFC 2012). La partie sur le CEI passe dans la fiche 5, où N la résout |
| R10 | l. 619-630, `#tbl-epargne` et son paragraphe (intitulés de 2017 et 2022, LF 2024, II *bis*) | **déplacés** dans la fiche 1, identifiant gardé ; ligne 1992 corrigée (D6) ; la phrase « n'est pas établi ici » disparaît |
| R11 | l. 632, autres paragraphes de l'art. 39 | reste pour les § V et X, l'art. 39 *quater*, la loi n° 2017-8 et le code de 1993. Les CEA, CEI et 39 *ter* sont réduits à une proposition et un lien. Le plafond du CEA de 2021 et sa citation `[@lf-2021, art. 16]` passent dans la fiche 4 |
| R12 | `#tbl-irpp-reformes`, lignes LF 2014 art. 19 (l. 1033), LF 2017 art. 13 (1046), LF 2018 art. 56 (1055), LF 2021 art. 16 ×2 (1059-1060), LF 2022 art. 24 et 29 (1062-1063), LF 2024 art. 34 (1067) | **restent**, colonne « Détail » repointée vers `@sec-irpp-epargne-…` (la ligne de 2018 vers `@sec-irpp-autres`). **Aucune ligne nouvelle n'y est ajoutée** : les registres de la section en tiennent lieu. Le chapeau du tableau reçoit une phrase et un lien. Autre choix possible : question H3 |
| R13 | TODO l. 1076-1085 (textes absents du tableau) | reste ; l'art. 30 de la LF 1992 en sort, puisqu'il est désormais au registre de la fiche 1 |
| R14 | TODO l. 649-655 (art. 12 *bis*, origine du 60 %) | reste à `#sec-irpp-deductions`, complété du jalon : les NC 35/2003 et 16/2004 donnent le 60 % en vigueur en 2003 |
| R15 | TODO l. 989-991 (« MANQUE ENCORE… retenue libératoire ») | **supprimé** : son objet est la section nouvelle, qui se place à cet endroit |
| R16 | `#sec-irpp-regimes` (l. 769) | reste ; une phrase est ajoutée : « les revenus de capitaux soumis à une retenue libératoire sortent eux aussi de la chaîne de calcul (@sec-irpp-epargne) » |
| R17 | « La longue période » du chapitre (l. 1087 et suivantes) | inchangée ; la section de l'épargne a sa propre longue période |
| R18 | Annexe des notations | ajouter, au besoin, $R$ et $V$ ; ils y sont déjà, aucune notation neuve n'est prévue. Le tableau 4.1 n'emploie pas de symbole |

Aucun élément n'est supprimé sans dire où l'information subsiste. R15 est un TODO dont l'objet est rempli.

## 6. Clés à citer, par sous-section

Récapitulatif ; le détail est au § 2.

| Sous-section | Clés |
|---|---|
| mise en place | `code-irpp-is-1990`, `loi-irpp-is-1989` |
| 1992 | `lf-1992`, `lf-1997` |
| 1999 | `loi-99-92-relance-marche-financier` |
| 2004 | `lf-2004`, `dgi-nc-8-2004`, `lf-2005`, `dgi-nc-13-2005`, `lf-2011`, `lf-2023`, `dgi-nc-3-2023` |
| 2014 | `lf-2014`, `minfin-cnf-2013-synthese`, `lf-2015`, `lf-2018`, `dgi-nc-14-2018`, `lf-1995`, `lf-2017` |
| 2020-2022 | `decret-loi-2020-30`, `lf-2021`, `lf-2022`, `dgi-nc-1-2022` |
| fiches | `lf-1998`, `lf-1999`, `lf-2002`/`loi2001-123-lf2002`, `dgi-nc-45-2002`, `dgi-nc-35-2003`, `dgi-nc-16-2004`, `loi-2007-70-lf-2008`, `dgi-nc-10-2008`, `decret-loi-2011-28`, `lf-2012`, `lfc-2012`, `lf-2024`, `lf-2025`, `dgi-nc-1-2021`, `dgi-nc-2-2017`, `dgi-nc-2-2018` |
| longue période | `gbo-depenses-fiscales` |

**Non citées tant que non lues** : `decret-loi-2011-100` (clé versée, texte non lu) ; `dgi-nc-3-2015` (clé absente).

## 7. Questions au documentaliste

- **D1.** Antécédent : régime et taux de la taxe sur le revenu des valeurs mobilières (1918) et de l'impôt sur le revenu des créances (1919) dans les années 1980. Ce que le code de 1990 en reprend : retenue par le payeur ? dividendes ? anonymat ? Lois de finances de 1980 à 1989 au corpus.
- **D2.** Contexte des réformes de 1992, 1999 et 2004 : exposé des motifs, rapport de la commission des finances, discours du ministre au vote. Mots des sources de l'époque, pas une interprétation.
- **D3.** Trois rubriques et une date :
  - rubrique de la LF 2023, art. 42 (édition arabe, p. 4068) ;
  - rubrique ou chapitre du décret-loi n° 2020-30 sous lequel est placé l'art. 12 ;
  - sort des intérêts courus avant le 10 juin 2020, d'après une note commune ;
  - **les revenus frappés des 35 % définitifs (52-II-2 *bis*) sortent-ils du revenu global, ou restent-ils au barème, la retenue n'étant simplement pas restituable ?** De la réponse dépend la cellule de juin 2020 du tableau 4.1 : 35 %, ou 35 % plus le barème.
- **D4.** NC 3/2015 et notes postérieures : comment la restitution sous 10 000 D s'articule avec le caractère libératoire de c *bis*, de 2015 à 2026.
- **D5.** Articles connus par une note commune ou par une annotation, à lire au fascicule :
  - LF 2002, art. 21-28 (OPCVM) ;
  - LF 2003, art. 21-23 (CEI) ;
  - LF 2007, art. 32 ;
  - décret-loi n° 2011-100, art. 6-13 ;
  - loi n° 2005-59, art. 3 (39 *ter*) ;
  - LF 2014, art. 44, et LF 2019, art. 35-4 (25 %) ;
  - LF 2000, art. 57, et décret n° 2007-1870.
- **D6.** Années de revenus de rattachement :
  - LF 1992, art. 30 : plafond de 1 500 D, revenus 1991 ou 1992 selon la règle de conversion « cas 2 » ;
  - loi n° 99-92 : CEA, date de dépôt du JORT n° 67 de 1999 ;
  - décret-loi n° 2011-28 : CEA à 50 000 D ;
  - LFC 2012, art. 42 : assurance-vie à 10 000 D.
- **D7.** Assurance-vie : la LF 2002, art. 45, et la LF 2020, art. 12, sont dans le TODO actuel. N § 4.5 ne les traite pas, et le backlog dit la LF 2002 « sans changement de montant ». Confirmer et donner le contenu.
- **D8.** Régime fiscal des SICAV, que la NC 45/2002 dit « en vigueur ».
- **D9.** LF 1995, art. 50-53 : page à confirmer à l'image. Code de 1990, art. 38-10 : relecture à l'image.
- **D10.** LF 2004, art. 61-63 : relecture à l'image demandée par N. La rupture de 2004 repose sur la couche décodée.

**Au bibliographe**
- **B1.** `lf-2002` et `loi2001-123-lf2002` désignent la même loi, avec des pages différentes (4286/4301 contre 4260). Le chapitre cite la seconde (l. 1022). Une seule clé doit rester.
- **B2.** Vérifier que `gbo-depenses-fiscales` couvre les rapports de 2024 et de 2025, que lit la figure de la longue période. Sinon, verser leurs clés.

**Au terminologue (passe 2)**
- **T1.** `retenue-a-la-source` est `valide`, mais sa définition (« imputé sur l'impôt dû par ce dernier ») est **inexacte pour les retenues libératoires et définitives**. À corriger : la retenue s'impute sur l'impôt dû, sauf quand la loi la rend libératoire. Renvoyer à `retenue-liberatoire`.
- **T2.** Les 11 entrées de la passe 1 ont une **définition vide** : un lien `#g-…` y ouvrirait une infobulle vide. La passe 2 doit précéder le rédacteur, ou bien le rédacteur s'abstient de ces liens jusqu'à la passe 2.
- **T3.** `revenus-valeurs-mobilieres`, en arabe : l'entrée porte مداخيل الأوراق المالية, N proposait مداخيل القيم المنقولة. Trancher sur l'édition arabe du code.
- **T4.** `tmm` : l'entrée porte « Taux moyen du marché monétaire », N « Taux du marché monétaire ». Suivre la lettre du décret-loi n° 2020-30 en français, ou, à défaut, celle de la BCT.

## 8. Désaccords de classement possibles, à trancher

1. **1997 : étape ou rupture ?**
   - Je la classe en **étape** de 1992. La rubrique dit « unification », et l'harmonisation de 1992 l'annonçait.
   - Autre lecture : rupture. La loi met fin à deux dispositifs (le libératoire des titres anonymes, celui du compte d'épargne-emprunts obligataires) et fixe un objectif nouveau, le taux unique.
   - Si l'on retient la rupture, 1997 devient un `####` propre, et l'épine compte six réformes.
2. **1999 : grande réforme ou rupture propre au CEA ?**
   - La consigne range en grande réforme une loi qui crée un dispositif sans toucher aux règles de base : je la suis.
   - Autre lecture : la naissance du CEA reste dans sa fiche et l'épine la signale dans l'entre-temps 1997-2004. L'épine compte alors quatre réformes, et le chapitre gagne environ 200 mots visibles.
   - Conséquence du critère retenu : une fois la LF 2003, art. 21 à 23, lue (D5), la naissance du CEI devient une sixième grande réforme, et celle des OPCVM en 2002 peut-être une septième. Il faudra alors regrouper, ou revenir à l'autre lecture.
3. **Le regroupement « 1999-2004 » de N § 3 est refusé.** Ses textes ont des objets différents : relance du marché financier, imposition de la plus-value. Ceux du milieu (LF 2002, LF 2003) ne sont pas lus au fascicule. C'est une commodité de période.
4. **2020-2022 : une réforme ou trois ?**
   - Je retiens **une réforme en trois temps** : trois textes voisins de même objet (art. 52-II), chacun lu.
   - Autre lecture : 2021 est la rupture, 2020 une rupture distincte (un nouveau public, les dépôts à terme bien rémunérés), 2022 une rupture inverse.
5. **2023 : étape de 2004 ou rupture ?**
   - Je la classe en **étape**. La durée de détention, posée en 2011, devient un critère de taux.
   - Autre lecture : rupture, parce que la suppression de la franchise fait entrer un nouveau public, les petites cessions.
   - La rubrique n'est pas relevée (D3) : la réponse peut trancher.
6. **LFC 2012 (assurance-vie) : rupture propre ou ajustement ?** Je la classe en rupture. La déduction cesse d'être familiale, puisque les majorations pour le conjoint et les enfants disparaissent.
7. **Domicile de l'assurance-vie et des comptes spéciaux.**
   - Je les tire de `#sec-irpp-deductions` vers les fiches : ce sont des avantages à l'épargne.
   - Autre choix : les laisser en place, avec un lien en tête. La section de l'épargne gagne alors environ 600 mots en moins, mais l'assurance-vie et le CEA, qui ont la même rubrique en 2021, sont séparés.

**Risques du repli**
- **Le caractère libératoire ou imputable ne doit jamais dépendre d'un bloc replié.** Il est au premier plan dans `#tbl-irpp-epargne-taux` et `#tbl-irpp-epargne-etat`, et défini dans le chapeau. Les registres le répètent.
- **La lettre de l'art. 71 de la LF 2004** ne figure qu'au registre A, ce qui est voulu. Si la revue juge que le lecteur doit savoir que le texte de 2004 disait autre chose que la pratique, une phrase dans la réforme de 2004 suffit, sans récit de recherche.
- **Les naissances des CEI et des OPCVM** ne sont dites que dans leurs fiches, d'après les notes communes. Un lecteur de la seule épine les ignore jusqu'à la lecture des articles (D5).
- **La population couverte reste vide** dans l'état du droit.

## 9. Taille, et options pour ramener le fichier sous le seuil

### 9.1 Budget

| Partie | Visible (mots) | Replié et tableaux (mots) |
|---|---|---|
| chapeau, vue d'ensemble, `#tbl-irpp-epargne-taux` | 400 | 500 (tableau non replié) |
| mise en place | 400 | — |
| cinq réformes et entre-temps | 1 500 | 1 300 (registres A, B, C) |
| état du droit | 200 | 250 (tableau non replié) |
| sept fiches | 1 400 | 2 000 (registres de fiche, tableaux courts) |
| longue période | 350 | 200 |
| économie (quand la fiche existera) | 500 | — |
| **Total ajouté** | **≈ 4 750** | **≈ 4 250** |

**Ce qui est retiré du chapitre.** Environ 1 000 mots : R5, R6, R8, R9, R10, la part de R11 et R15.

**Fichier.** Environ 26 300 − 1 000 + 9 000 ≈ **34 000 mots**. Replier allège le texte visible, pas le compte du fichier, sur lequel porte le critère. Les ordres de grandeur concordent : le chapitre de la TVA a gagné 57 % à sa conversion, et le plan du patrimoine immobilier compte environ 10 500 mots, dont 6 500 visibles.

**Ce qu'il faut garder en tête.** Le chapitre de l'IRPP n'est pas encore converti au format « ruptures au premier plan ». Sa propre conversion le fera grossir encore. Il porte déjà au moins deux épines, le barème et le forfait. L'épargne en ajoute une troisième.

### 9.2 Options, sans décision

Aucun des liens entrants depuis les autres livres ne vise une partie qui changerait de fichier : ils ne visent que `#sec-irpp`, `#sec-irpp-salaires` et `#sec-irpp-famille`, vérifiés par grep le 20 octobre 2026. À l'intérieur du livre, les renvois `@sec-…` et `@tbl-…` se résolvent d'un chapitre à l'autre. Le chapitre ne contient aucun lien brut `](#sec-…)` hors du glossaire. Une scission garde donc toutes les ancres sans casser de lien. Elle impose :
- une entrée au `_quarto.yml` français ;
- l'entrée du `_quarto.yml` arabe, à ajouter à la main une fois la traduction livrée ;
- de recopier la fonction `table()` de tête dans tout fichier qui lit un tableau engendré.

| Option | Ce qui sort de `_impot_revenu.qmd` | Mots sortis | Fichier IRPP après | Remarques |
|---|---|---|---|---|
| **A** | le régime forfaitaire (`#sec-irpp-regimes` et `#sec-irpp-forfait`, l. 767-991), dans un chapitre `_impot_revenu_forfait.qmd` | ≈ 5 400 | ≈ 28 600 | une épine propre (1990, 1993, 2011, 2016, 2026) ; emporte la figure `bic_regimes.py`, les tableaux engendrés `tbl-bic-plafonds` et `tbl-irpp-forfait` et le TODO modéliste. Ne suffit pas seule |
| **B** | `#tbl-irpp-reformes` (texte par texte) et `#sec-irpp-notations`, dans un fichier d'annexe déclaré dans `appendices:` | ≈ 3 500 | ≈ 30 500 | le § 4 des conventions range déjà les textes modificatifs et les notations en annexe. Ne suffit pas seule |
| **A + B** | les deux | ≈ 8 900 | **≈ 25 100** | juste au seuil ; la conversion future du chapitre le fera repasser au-dessus |
| **C** | la section de l'épargne elle-même, dans `_impot_revenu_epargne.qmd`, chapitre placé juste après l'IRPP | ≈ 9 000 | ≈ 25 300 | c'est la recommandation de N § 2, écartée par le propriétaire ; elle remettrait « Ce qu'en dit l'économie » en fin de chapitre, comme le veut la doctrine |
| **D** | aucune ; la section de l'épargne dans un fichier inclus (`{{< include _impot_revenu_epargne.qmd >}}`) | 0 au rendu | ≈ 34 000 rendus | satisfait la lettre (« mots de fichier »), pas l'objet du critère (une épine par chapitre) ; facilite seulement le travail en parallèle. Je ne la recommande pas |

**Mon avis, que l'humain tranche.**
- **A + B** respecte la décision du 20 octobre (l'épargne dans le chapitre de l'IRPP) et ramène le fichier au seuil.
- **C** est la seule option qui donne à l'épargne la forme complète d'un chapitre de dispositif. Le titre du chapitre peut garder l'IRPP, par exemple « L'impôt sur le revenu : les revenus de l'épargne et du capital ». Cela répond peut-être à l'intention de la décision.
- Dans tous les cas, la scission se fait **avant** l'écriture de la section, conformément au § 4 (« il se scinde, avant toute conversion »), et dans une PR à part, sans changement de texte, pour que le diff se relise.

## 10. Ordre d'écriture conseillé

1. **Propriétaire.** Il tranche la scission (§ 9) et les classements du § 8 (1997, 1999, 2020-2022, 2023, domicile de l'assurance-vie) ; ensuite le sort des lignes de `#tbl-irpp-reformes` (R12) et l'ajout des identifiants de l'IS.
2. **Scission éventuelle**, PR mécanique à part, avec des contrôles d'identité : ancres, clés, rendu.
3. **Terminologue, passe 2.** T1 à T4, avant le rédacteur, parce que les infobulles sont vides.
4. **Documentaliste**, en ticket borné : D3, D4, D6 et D10 bloquent des cellules du tableau 4.1 et de l'état du droit. D1, D2, D5, D7, D8 et D9 peuvent suivre. Le rédacteur peut commencer sans eux, avec des TODO.
5. **Rédacteur, dans cet ordre** :
   1. les trois registres A, B et C, puis les registres des fiches ; ce sont les ancres `#r-…` dont dépend la prose ;
   2. `#tbl-irpp-epargne-taux` et `#tbl-irpp-epargne-etat` ;
   3. les cinq réformes ;
   4. la mise en place, puis la vue d'ensemble et le chapeau ;
   5. les sept fiches, en déplaçant R8, R10 et R11 ;
   6. les retouches R1 à R7 et R12 à R18 ;
   7. la longue période avec `#fig-irpp-epargne-depenses-fiscales`.

   Il mesure avant et après : mots, clés, couples clé-localisateur, identifiants, TODO, ancres. Il passe `check_domicile_references.py` et `scripts/verifier.sh fiscalite`. Il met à jour `docs/notes/backlog-precis.md` dans le même changement : retrait du point 9 des manques, lacunes nouvelles, correction du libellé « Intérêts dépôts et épargne ».
6. **Données**, en parallèle : générateur des plafonds (et des taux, si la figure est retenue), puis catalogue BCT dans `tunisia-data`.
7. **Économiste.** `docs/notes/eco-epargne-capital.md`, puis `#sec-irpp-epargne-economie`.

## Fichiers utiles

- Note : `docs/notes/fiscalite-epargne-capital.md`
- Chapitre : `precis/fr/fiscalite/_impot_revenu.qmd` ; IS : `precis/fr/fiscalite/_impot_societes.qmd`
- Série : `precis/_seriescache/depenses-fiscales-detail.csv` (rapports de 2021, 2024, 2025)
- Précédent de générateur : `scripts/generate_forfait_bic_series.py`
- Encours BCT : `~/projets/tunisia-data/data/processed/bct/agregats_monnaie_2003_2024.csv`, hors catalogue
