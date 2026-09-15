# TVA — dossier documentaire (champ, assujettis, fait générateur, taux, exonérations, calendrier)

> Note **documentaire**, préalable à la rédaction de la section TVA du livre « Fiscalité ».
> Elle ne rédige pas de prose de précis et n'a modifié aucun fichier de `precis/`.
>
> **Conventions de datation.** Pour chaque texte, trois dates sont relevées séparément :
> (1) **signature**, (2) **publication au JORT** (numéro de fascicule et page), (3) **date d'effet**.
> Pour la TVA, la date d'effet n'est jamais implicite : le code de 1988 n'est pas entré en vigueur le
> jour de sa publication (§ 2) et les décrets de taux réduit portent tous une clause d'application
> bornée à l'année civile (§ 4).
>
> **Degré de certitude.** Quatre mentions sont employées : *établi (JORT, lu à l'image)* — la page du
> Journal officiel a été lue en image, pas seulement en OCR ; *établi (texte officiel à couche
> texte)* — extraction directe d'un PDF officiel à couche texte fiable ; *probable* — cohérent et
> corroboré indirectement, mais la source primaire n'a pas été lue ; *non établi* — ce qui n'a pas pu
> être vérifié, et qui ne doit pas être écrit.
> **Provenance des paginations** : sauf mention « pied de page lu », les numéros de page proviennent
> du champ `pages` de `jort_cache.db`, qui reprend les notices du JORT — fiable, mais de seconde
> main. Le cas du décret 89-1222 (§ 2.2) montre qu'une notice peut se tromper.
>
> **Note d'outillage.** `www.pist.tn` présente un **certificat TLS expiré** : les URL ont été testées
> par `curl -skIL` et toutes celles citées répondent **HTTP 200**, sauf mention contraire explicite.
> Convention de nommage confirmée :
> `https://www.pist.tn/jort/<année>/<année>{F|A}/{Jo|Ja}<n° sur 3 chiffres><année>.pdf`, avec l'année
> sur **2 chiffres jusqu'en 1999** (`Jo03988.pdf`) et **4 chiffres à partir de 2000**
> (`Jo0022007.pdf`). Les URL arabes ont été **lues dans le champ `pdf_ar`** de la base, jamais
> dérivées de l'URL française par transformation de chaîne.
>
> **Avertissement de méthode — deux pièges, dont un a produit un faux négatif dans cette note même.**
> 1. Toute recherche `LIKE` doit être doublée d'une recherche **FTS** : la série des décrets de taux
>    réduit est invisible à `objet LIKE '%taux de 12%'`, les objets disant « réduction **à** 12 % du
>    taux ».
> 2. **Plus grave, et non signalé jusqu'ici : le champ `objet` de `jort_cache.db` est en arabe pour
>    une part considérable des textes récents.** Une requête en français — `LIKE` *comme* FTS — y est
>    structurellement aveugle. Part des `objet` contenant de l'arabe, par année de signature :
>
> | Année | 2008-2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | % d'objets en arabe | 0 % | 36 % | 6 % | 0,2 % | 9 % | 43 % | 71 % | 52 % | **82 %** | 73 % | 14 % |
>
> C'est ce piège qui m'a d'abord fait conclure — à tort — que l'année 2013 n'était couverte par aucun
> décret : les deux décrets qui la couvrent sont bien dans la base, avec un objet **en arabe**
> (§ 4.4). **Toute conclusion négative portant sur la période 2011-2020 doit être vérifiée par une
> requête en arabe** (par exemple `objet LIKE '%الأداء على القيمة المضافة%'`) **et** par la lecture
> des fascicules JORT locaux.
>
> **Note sur l'OCR.** Les valeurs chiffrées et les tableaux du JORT de 1988 ont été **relus à
> l'image** ; l'OCR du corpus local les abîme systématiquement (colonnes entrelacées, « 1890 » pour
> « 1990 »).
>
> **Statut des notes communes.** Doctrine administrative : aucune règle de cette note n'est établie
> sur une note commune.

---

## Résultat principal

**1. La TVA naît avec trois taux, et le taux réduit d'origine est de 6 %.** L'article 7 du code de
1988 pose un taux général de **17 %**, un taux réduit de **6 %** (tableau B) et un **taux majoré de
29 %** (tableau C). Le taux majoré a vécu dix-huit ans : supprimé par l'**article 13 de la loi
n° 2006-80 du 18 décembre 2006**, avec effet au 1er janvier 2007.

**2. La TVA n'est pas entrée en vigueur d'un coup.** Le code s'applique **à compter du 1er juillet
1988** (décret n° 88-1109), **à l'exception** du commerce de gros « des autres secteurs » et des
régimes forfaitaires ; le commerce de gros n'entre qu'au **1er octobre 1989** (décret n° 89-1222), et
encore **à l'exception des grossistes en alimentation générale** ; le **commerce de détail** n'est
assujetti qu'au **1er juillet 1996** (loi n° 95-109, art. 43 et 46). La construction du champ s'étale
sur **huit ans**.

**3. Correction majeure au plan initial — le taux réduit sur l'électricité et les carburants n'est
pas une faveur nouvelle, c'est la restauration annuelle d'un avantage supprimé.** En 1988,
l'électricité, le gaz et les huiles de pétrole figurent **dans le code**, au tableau B, au taux de
**6 %**. L'**article 40 de la loi n° 95-109 du 25 décembre 1995** les en **retire**. Retombés au taux
normal, ces produits sont ensuite ramenés à un taux réduit **par décret**, sur le fondement de
l'**article 8 du code**, lequel dispose que de telles mesures « **ne sont valables que pour l'année
civile au cours de laquelle elles sont prises** ». *C'est cette clause, et elle seule, qui explique
la répétition annuelle des décrets de 1998 à 2014.*

**4. Les deux séries n'ont pas la même histoire, et l'une d'elles est interrompue six ans.** Le
**décret n° 98-952 du 27 avril 1998** abroge le décret 98-384 et **transfère les produits pétroliers
du taux réduit de TVA vers le droit de consommation** (tarif par hectolitre et par tonne), ne
laissant subsister qu'un taux réduit de TVA sur l'**électricité**. La série « produits pétroliers »
s'interrompt donc de mai 1998 à juillet 2004 et ne reprend qu'avec le **décret n° 2004-1773 du 2 août
2004**. *Écrire que les deux séries courent en parallèle de 1998 à 2014 serait faux.* Cette
interruption est **établie et non inférée** : le **tableau « L »** de la LF 2002, qui fixe le contenu
du tableau B bis (taux de 10 % inscrit dans le code), a été lu intégralement et **ne comporte ni
produits pétroliers, ni électricité** (§ 3.3).

**5. Le taux réduit de ces séries est de 10 % de 1998 à 2006, de 12 % de 2007 à 2017, de 13 % depuis
2018** — et le passage de 10 % à 12 % **n'est pas l'œuvre des décrets 2007-1 et 2007-2**, malgré leur
intitulé : il résulte de l'**article 17 de la loi n° 2006-80**, que ces décrets se bornent à
appliquer (ils le citent en visa).

**6. Aucune année n'est laissée sans texte entre 1998 et 2014.** Les « trous » de 2006 et de 2011
signalés par le plan sont des **artefacts de datation** : la base indexe `jort_annee` sur l'année de
**signature**, or les décrets couvrant 2006 et 2011 ont été signés fin décembre de l'année
précédente. L'année 2013, que j'ai d'abord crue vide, est couverte par les **décrets n° 2012-3413 et
2012-3414 du 31 décembre 2012** (JORT 2013 n° 1, p. 201-202), invisibles à toute requête française
parce que leur objet est enregistré **en arabe**.

**7. Le changement de véhicule en 2014 s'explique par la nature de la mesure.** L'**article 36 de la
loi n° 2014-59 (LF 2015)** inscrit l'électricité domestique, l'électricité d'irrigation et les
produits pétroliers au **tableau B bis annexé au code** : la mesure cesse d'être conjoncturelle
(article 8, annuelle) pour devenir structurelle, ce qui met fin à la reconduction par décret. La
LF 2017 supprime ensuite le tableau B bis et réinscrit ces produits **directement à l'article 7**.

**8. Le taux réduit existe toujours.** La grille en vigueur est **7 % / 13 % / 19 %**, issue de
l'**article 43 de la loi n° 2017-66 (LF 2018)**, qui a relevé les trois taux d'un point au 1er janvier
2018.

---

## 1. Le code de 1988 : champ, assujettis, fait générateur, taux

**Texte** : **loi n° 88-61 du 2 juin 1988, portant promulgation du code de la taxe sur la valeur
ajoutée**.

| | |
|---|---|
| Signature | **2 juin 1988** |
| Publication | **JORT n° 39 du 10 juin 1988**, tome 131, **p. 827-846** |
| Date d'effet | **non fixée par la loi** : son article 6 renvoie à un décret (§ 2) |

- Copie locale FR : `/home/benjello/projets/PDFs-legislation-tunisie/PDFs/JORT/1988/fr/Jo03988.pdf`
- Copie locale AR : `/home/benjello/projets/PDFs-legislation-tunisie/PDFs/JORT/1988/ar/Ja03988.pdf`
- OCR local : `…/markdown_output/JORT/1988/fr/Jo03988.md` (utile pour se repérer ; **tableaux et
  chiffres inexploitables**)
- URL FR : `https://www.pist.tn/jort/1988/1988F/Jo03988.pdf` — **vérifiée** (HTTP 200, 4 137 193 o)
- URL AR : `https://www.pist.tn/jort/1988/1988A/Ja03988.pdf` — **vérifiée** (HTTP 200, 2 957 617 o)

Le **même fascicule n° 39** porte la loi 88-60 (LF complémentaire 1988), la **loi 88-62** (refonte des
droits de consommation), 88-63 (enregistrement) et 88-64.

### 1.1 Ce que fait la loi de promulgation (p. 827) — *établi (JORT, lu à l'image)*

- **Art. 1er** : les textes annexés « relatifs à l'imposition du chiffre d'affaires sont réunis en un
  seul corps sous le titre "Code de la taxe sur la valeur ajoutée" ».
- **Art. 2** : abroge, à compter de la mise en vigueur du code, « le **décret du 29 décembre 1955**
  portant institution d'une **taxe à la production**, d'une **taxe de consommation** et d'une **taxe
  sur les prestations de service** ». *C'est l'identité du régime remplacé : à citer, plutôt qu'une
  formule vague sur « les taxes sur le chiffre d'affaires ».*
- **Art. 4** : les travaux immobiliers relevant de marchés définitivement conclus **avant le
  1er juillet 1988** demeurent soumis au taux de **13,63 % hors TVA** au titre de la taxe à la
  production ; les travaux omis de la liste nominative à déposer avant le 30 septembre 1988 sont
  soumis au taux de **17 %**.
- **Art. 5** : dans tous les textes en vigueur, « taxe à la production », « taxe de consommation » et
  « taxe sur les prestations de service » sont remplacées par « taxe sur la valeur ajoutée ».
- **Art. 6** : « Le code […] est mis en application selon un **calendrier fixé par décret**. »

### 1.2 Champ d'application — article 1er du code (p. 827) — *établi (JORT, lu à l'image)*

**§ I — principe.** Sont soumises à la TVA, « quels qu'en soient les buts ou les résultats, les
affaires faites en Tunisie au sens de l'article 3 ci-dessous et revêtant le **caractère industriel,
artisanal ou relevant d'une profession libérale**, ainsi que les **opérations commerciales autres que
les ventes** ». La taxe s'applique quels que soient (a) le **statut juridique** des personnes et leur
situation au regard de tous autres impôts, (b) la **forme ou la nature** de leur intervention et le
caractère **habituel ou occasionnel** de celle-ci.

*Conséquence de rédaction, à ne pas manquer : le commerce — les ventes — n'est dans le champ que par
les cas énumérés au § II. Le commerce de détail n'y est pas.*

**§ II — opérations imposables par détermination de la loi**, dix numéros : 1) importations ;
2) a) reventes en l'état par les **concessionnaires de biens d'équipements industriels et de biens
d'équipements de travaux publics**, b) reventes en l'état par les **commerçants grossistes en
matériaux de construction** ; 3) reventes en l'état par les **commerçants grossistes exerçant dans
d'autres secteurs et qui approvisionnent d'autres commerçants revendeurs** ; 4) présentation
commerciale des produits **autres qu'agricoles ou de la pêche** ; 5) **vente de lots** par les
lotisseurs immobiliers ; 6) **travaux immobiliers** ; 7) vente d'**immeubles ou de fonds de
commerce** par ceux qui, habituellement, achètent ces biens en vue de leur revente ; 8) affaires
portant sur la **consommation sur place** ; 9) **livraisons à soi-même d'immobilisations** ;
10) livraisons à soi-même de biens **autres qu'immobilisations** pour les besoins propres de
l'exploitation, dans la mesure où ces biens ne concourent pas à des opérations passibles de la TVA ou
ouvrant droit à déduction.

**Extension ultérieure majeure — le commerce de détail.** L'**article 43 de la loi n° 95-109 du
25 décembre 1995 (LF 1996)** ajoute au § II un **alinéa 11** : « la vente des produits en l'état par
les **commerçants détaillants** qui réalisent un **chiffre d'affaires annuel global égal ou supérieur
à 100 000 dinars** ». Son **article 46** en fixe l'effet au **1er juillet 1996**. Le seuil s'apprécie
sur le chiffre d'affaires de 1995 pour les commerçants déjà en activité ; les produits alimentaires
notamment restent exonérés à la revente au détail.
*Établi (texte officiel à couche texte, JORT n° 104 des 29-31 décembre 1995, p. 2371-2372 ;
`PDFs/JORT/1995/fr/Jo10495.pdf` ; URL `https://www.pist.tn/jort/1995/1995F/Jo10495.pdf` vérifiée.)*

### 1.3 Assujettis — article 2 du code (p. 827-828) — *établi (JORT, lu à l'image)*

**§ I.** Sont assujettis les personnes physiques ou morales qui : 1) réalisent les opérations des § I
et II-2 à 8 de l'article 1er ; 2) **mentionnent la TVA sur leurs factures**, « et ce, du seul fait de
sa facturation » — ces personnes n'étant redevables que de la taxe ayant fait l'objet d'une mention ;
3) **optent** pour la qualité d'assujetti, pour tout ou partie de leurs activités.

**Régime de l'option**, entièrement dans le texte de 1988 : déclaration souscrite auprès du centre ou
bureau de contrôle des impôts ; **effet au premier jour du mois suivant** celui de l'acceptation ;
**période irrévocable expirant le 31 décembre de la quatrième année** qui suit celle de la prise
d'effet ; **reconduction tacite par périodes de quatre ans**, sauf dénonciation **trois mois** avant
l'expiration ; l'**abandon** de la qualité d'assujetti est subordonné au paiement de la taxe sur les
stocks et au reversement de la taxe sur les biens d'équipement et bâtiments.

**§ II.** Les **entreprises dépendantes** d'entreprises assujetties, quelle que soit leur forme
juridique — avec une définition de la dépendance (pouvoir de décision exercé en fait, part
prépondérante dans le capital ou majorité absolue des suffrages, personnes interposées énumérées, cas
du siège situé hors de Tunisie).

**§ III.** Les **entrepositaires et marchands en gros de boissons alcoolisées, de vins et de bières**.

### 1.4 Fait générateur — article 5 du code (p. 828) — *établi (JORT, lu à l'image)*

| Opération | Fait générateur |
|---|---|
| Importations | le **dédouanement** de la marchandise |
| Ventes | la **livraison** ; pour les **immeubles** (art. 1er II-7) et les **échanges**, l'**acte** qui constate l'opération ou, à défaut, le **transfert de propriété** |
| Prestations de service | la **réalisation du service** ou l'**encaissement** du prix ou des acomptes s'il intervient antérieurement |
| Biens que les redevables se livrent à eux-mêmes | la **première utilisation** des biens |
| Travaux immobiliers | l'**exécution partielle ou totale**, avec deux règles : le fait générateur ne peut être postérieur à la facturation totale, et l'établissement de décomptes provisoires, mémoires ou factures partiels rend la taxe exigible ; les entreprises de travaux publics et de bâtiment travaillant pour l'**État, les collectivités publiques locales et les établissements publics à caractère administratif** acquittent la taxe **sur leurs encaissements**, le fait générateur de droit commun continuant de déterminer le **taux** applicable |

### 1.5 Taux d'origine — articles 7 et 8 du code (p. 829) — *établi (JORT, lu à l'image)*

> « **Art. 7.** — Sont soumis à la taxe sur la valeur ajoutée au taux de **17 %**, les opérations
> portant sur les biens et les services non soumis à un autre taux.
> Toutefois sont soumis à la taxe sur la valeur ajoutée :
> 1) au taux de **6 %**, les opérations portant sur les biens et les services repris au tableau « B »
> figurant en annexe.
> 2) au taux de **29 %**, les opérations portant sur les biens repris au tableau « C » figurant en
> annexe. »

> « **Art. 8.** — Dans le cadre de l'action du gouvernement pour le développement et la promotion de
> l'économie nationale ainsi que dans les cas conjoncturels, des **suspensions ou des réductions** de
> la taxe sur la valeur ajoutée pourront être prévues **par décret** pris après avis du ministre des
> finances et des ministres concernés. **Ces mesures ne sont valables que pour l'année civile au
> cours de laquelle elles sont prises.** »

**L'article 8 est la clef du § 4** : il rend les réductions de taux par décret **annuelles par
construction**, donc nécessairement répétées. Il est **inchangé, mot pour mot, depuis 1988**.

### 1.6 Contenu des tableaux B et C en 1988 (p. 836-837) — *établi (JORT, lu à l'image)*

**Tableau B (6 %).**
- **§ I — professions** : architectes et ingénieurs-conseils ; dessinateurs, géomètres et
  topographes ; avocats, huissiers-notaires, notaires et interprètes ; conseils juridiques et
  conseils fiscaux ; entrepreneurs de tenue de comptabilité ; exploitants de laboratoire d'analyse ;
  infirmiers et masseurs ; médecins, médecins spécialistes, dentistes, sages-femmes et vétérinaires ;
  experts quelle que soit leur spécialisation.
- **§ II — importation, production et vente** : 1) engrais ; **2) électricité et gaz** ; 3) aliments
  composés pour bétail, tourteaux de soja, farines de poisson ; 4) produits destinés à l'industrie
  pharmaceutique et produits pharmaceutiques finis ; 5) machines pour le traitement de l'information,
  pièces, parties et supports magnétiques ; 6) appareils récepteurs de télévision non combinés,
  parties et pièces détachées, transformateurs et régulateurs de courant ; 7) conserves de tomate, de
  harissa et de sardines ; 8) savon ordinaire.
- **§ III — activités et produits** : 1) hôtellerie, y compris hébergement, restauration, ventes à
  consommer sur place et animation ; 2) produits de l'artisanat local ; 3) transport de personnes ou
  de marchandises ; **4) vente des huiles de pétrole ou de minéraux bitumineux (essence de pétrole,
  pétrole lampant, gaz-oil, fuel-oil) par les entreprises de distribution** ; 5) hébergement,
  restauration et services des cliniques et polycliniques médicales ; 6) intérêts débiteurs ;
  7) services réalisés en matière informatique.

*Les numéros II-2 (électricité et gaz) et III-4 (huiles de pétrole) sont exactement ceux que
l'article 40 de la loi n° 95-109 fera disparaître : § 4.1.*

**Tableau C (29 %)** : liste douanière de produits de consommation « de luxe » et de denrées
largement importées — foies de volailles, viandes et abats, poissons séchés ou fumés, beurre, plumes
de parure, ivoire, fleurs coupées, champignons et truffes, fruits exotiques (ananas, bananes,
mangues, avocats, goyaves, noix de coco, noix de cajou), raisins secs, fruits à coques, pommes et
poires fraîches, café, thé, poivre, vanille, cannelle, girofles, muscade, thym et safran, malt,
gommes et résines, saucissons et conserves de viande, conserves de poissons hors thon/sardines/
anchois, crustacés, sucreries sans cacao, cacao sous toutes ses formes.

### 1.7 Exonérations — article 4 et tableau A (p. 833-836) — *établi (JORT, lu à l'image)*

L'**article 4** se borne à renvoyer : « Sont exonérées de la taxe sur la valeur ajoutée les opérations
reprises au tableau "A" figurant en annexe. » Le tableau A d'origine compte **46 numéros** (p. 833 à
836). Principaux postes, dans l'ordre du texte :

1) fabrication et vente des **farines, semoules, pain, couscous et pâtes alimentaires de qualité
ordinaire** ; 2) **lait** frais, farines lactées, laits conservés pour nourrissons et malades ;
3) importation des **peaux brutes** ; 4) **huile d'olive**, grignons et sous-produits de la
trituration, fèves et huile de soja, huiles végétales importées par l'Office national de l'huile pour
mélange ; 5) **sucre** non additionné d'aromatisants ni de colorants ; 6) affaires des **œuvres
reconnues d'intérêt humanitaire et social** agréées par le ministre des finances ; 7) appareils pour
**handicapés physiques** et appareils et filtres d'**hémodialyse** (soluté de dialyse, filtres,
fauteuils roulants, reins artificiels, appareils d'orthopédie) ; 8) **enlèvement des ordures
ménagères** ; 9) **établissements d'enseignement** primaire, secondaire, supérieur, technique et
professionnel et **établissements de garderie** ; 10) exploitation des **douches** ;
11) polyéthylène agricole (serres, paillage), éléments des **stations d'irrigation par goutte à
goutte**, acide gibberellique, vernis et fongicides pour agrumes, **engrais minéraux ou chimiques
potassiques**, animaux reproducteurs de race pure, naissains d'huîtres, talc agricole, **biens
d'équipement agricoles** (serres, tracteurs, machines de récolte, machines à traire, pressoirs,
avions agricoles) ; 12) **plants et semences** ; 13) **travaux agricoles** effectués par des tiers,
location de matériel, transport de produits agricoles, location d'étalages dans les marchés publics ;
14) vente d'**eau** par abonnement ou autrement ; 15) biens et prestations livrés à titre de **don
dans le cadre de la coopération internationale** ; 16) **timbres** postaux et fiscaux ; 17) fonds,
billets de banque, monnaies, actions et obligations ; 18) **livres, brochures, journaux et
publications périodiques** ; … 42) exploration et production des **hydrocarbures** ; 43) rotochutes
et aérodynes de formation ou de lutte contre l'incendie ; 44) sulfate de baryum naturel destiné aux
sociétés pétrolières ; 45) **articles de sport** ; 46) importations de l'État : matériel d'armement
et équipements militaires, véhicules de lutte contre l'incendie, véhicules des services de la sûreté.

*Ce tableau a été entièrement refondu depuis : la LF 2016 (loi n° 2015-53, art. 31) abroge une
quinzaine de numéros et remplace le tableau A par un « **tableau A nouveau** » annexé à la loi ; la
LF 2017 (loi n° 2016-78, art. 16 à 23) poursuit la réduction du champ des exonérations. Pour l'état
actuel, la source à citer est le **code consolidé de la DGELF**, non le tableau de 1988.*

---

## 2. Calendrier d'entrée en vigueur — *établi (JORT, lu à l'image)*

L'article 6 de la loi 88-61 renvoie à un décret. Il y en a eu **deux**, et **deux seulement** : le code
consolidé de la DGELF, dans sa partie liminaire « **TEXTES DE MISE EN APPLICATION DU CODE DE LA TAXE
SUR LA VALEUR AJOUTÉE** », n'en reproduit pas d'autre (`PDFs/TVA/Code_de_la_taxe_sur_la_valeur_
ajoutée_2023.pdf`, sommaire p. 12-14 : « CALENDRIER D'APPLICATION DU CODE DE LA TVA ET DU DROIT DE
CONSOMMATION », puis « **CALENDRIER DE MISE EN APPLICATION DE LA TVA AU SECTEUR DU GROS** »).

### 2.1 Décret n° 88-1109 du 11 juin 1988 — le gros du code au 1er juillet 1988

| | |
|---|---|
| Signature | **11 juin 1988** |
| Publication | **JORT n° 42 du 21 juin 1988**, tome 131, **p. 923** (pied de page lu) |
| Date d'effet | **1er juillet 1988** |

> « **Article 1er.** — Conformément aux dispositions de l'article 6 de la loi sus-visée n° 88-61 du
> 2 juin 1988 portant promulgation du code de la taxe sur la valeur ajoutée sont applicables **à
> compter du 1er juillet 1988**, les dispositions du code de la taxe sur la valeur ajoutée, **à
> l'exception de celles prévues à l'article premier II-3, et celles prévues aux articles 16 et 17 I
> et II-1** dudit code.
> **Art. 2.** — Les dispositions de la loi sus-visée n° 88-62 du 2 juin 1988 portant refonte de la
> réglementation relative aux droits de consommation sont applicables **à compter du 1er juillet
> 1988** conformément à son article 8. »

Sont donc **différés** : l'article 1er **II-3** (grossistes des autres secteurs approvisionnant des
revendeurs) et les **articles 16 et 17 I et II-1** (régimes forfaitaires).

- Local : `PDFs/JORT/1988/fr/Jo04288.pdf` (**page 7 du PDF**)
- URL FR : `https://www.pist.tn/jort/1988/1988F/Jo04288.pdf` — **vérifiée** (HTTP 200)
- URL AR : `https://www.pist.tn/jort/1988/1988A/Ja04288.pdf` — **vérifiée** (HTTP 200)

### 2.2 Décret n° 89-1222 du 25 août 1989 — le commerce de gros au 1er octobre 1989

| | |
|---|---|
| Signature | **25 août 1989** |
| Publication | **JORT n° 61 du 12 septembre 1989**, tome 132, **p. 1395** (pied de page lu) |
| Date d'effet | **1er octobre 1989** |

> « **Article premier.** — Les dispositions du code de la taxe sur la valeur ajoutée sont applicables
> aux opérations prévues à l'**article 1er — II — 3** dudit code **à compter du 1er octobre 1989**, **à
> l'exception de celles relatives aux commerçants grossistes en alimentation générale**. »

**Piège de pagination à signaler.** Le **sommaire** du fascicule annonce ce décret **p. 1396** ; le
texte est en réalité **p. 1395** (pied de page lu à l'image ; la p. 1396 porte des arrêtés du
ministère de l'agriculture). La valeur de `jort_cache.db` (`pages = '1395'`) est la bonne, le sommaire
du JORT se trompe. **Citer p. 1395.**

- Local : `PDFs/JORT/1989/fr/Jo06189.pdf` (**page 13 du PDF**)
- URL FR : `https://www.pist.tn/jort/1989/1989F/Jo06189.pdf` — **vérifiée** (HTTP 200)
- URL AR : `https://www.pist.tn/jort/1989/1989A/Ja06189.pdf` — **vérifiée** (HTTP 200)

### 2.3 Chronologie de l'entrée dans le champ — synthèse

| Date d'effet | Ce qui entre dans le champ | Texte |
|---|---|---|
| **1er juillet 1988** | le code, sauf art. 1er II-3, 16 et 17 I et II-1 | décret 88-1109, art. 1er |
| **1er juillet 1988** | droits de consommation (loi 88-62) | décret 88-1109, art. 2 |
| **1er octobre 1989** | commerce de **gros** des autres secteurs, **sauf alimentation générale** | décret 89-1222, art. 1er |
| **1er juillet 1996** | commerce de **détail** à partir de 100 000 D de CA annuel | loi 95-109, art. 43 et 46 |

**Non établi**, à ne pas combler par conjecture : (i) la date d'entrée dans le champ des **grossistes
en alimentation générale** — aucun texte de mise en application ultérieur trouvé (FTS `"valeur
ajoutee" AND (calendrier OR "mise en application")` : les deux décrets ci-dessus ; FTS `"alimentation
generale"` : aucun résultat) ; (ii) la date d'entrée en vigueur des **articles 16 et 17** (forfaits).
Pour établir (i) et (ii), dépouiller les lois de finances 1990-1996 sur la TVA, la piste la plus
probable étant la même loi n° 95-109 qui a étendu la taxe au détail.

---

## 3. Chronologie des taux, de 1988 à aujourd'hui

### 3.1 Tableau d'ensemble

| Période (dates d'effet) | Taux normal | Taux réduits | Taux majoré | Texte |
|---|---|---|---|---|
| 1er juillet 1988 → 31 déc. 1997 | **17 %** | **6 %** (tableau B) | **29 %** (tableau C) | art. 7 du code (loi 88-61) |
| 1er janv. 1998 → 31 déc. 2001 | **18 %** | 6 % ; **10 %** épars, hors code | 29 % | art. 25 de la loi 97-88 |
| 1er janv. 2002 → 31 déc. 2006 | 18 % | 6 % ; **10 %** (tableau B bis, **dans le code**) | 29 % | art. 82-84 de la loi 2001-123 |
| 1er janv. 2007 → 31 déc. 2017 | 18 % | 6 % ; **12 %** | **supprimé** | art. 13 et 17 de la loi 2006-80 |
| **1er janv. 2018 → aujourd'hui** | **19 %** | **7 %** ; **13 %** | — | art. 43 de la loi 2017-66 |

### 3.2 Le passage de 17 % à 18 % — *établi (JORT, lu à l'image)*

**Loi n° 97-88 du 29 décembre 1997, portant loi de finances pour la gestion 1998**, sous l'intitulé
officiel « **Révision des taux de la taxe sur la valeur ajoutée** » :

> « **Article 25 :** Le paragraphe premier de l'article 7 du code de la TVA est modifié comme suit :
> "Sont soumis à la taxe sur la valeur ajoutée au taux de **18 %** les opérations portant sur les
> biens et les services non soumis à un autre taux".
> **Article 26 :** Le paragraphe 2 de l'article 56 de la loi n° 94-127 du 26 décembre 1994 portant loi
> de finances pour la gestion 1995 est supprimé.
> **Article 27 :** Sont supprimés du tableau "C" annexé au code de la taxe sur la valeur ajoutée les
> produits figurant au tableau "L" annexé à la présente loi. »

| | |
|---|---|
| Signature | **29 décembre 1997** |
| Publication | **JORT n° 104 des 30-31 décembre 1997**, tome 140 ; la loi commence p. 2435, les **articles 25 à 27 sont p. 2437** (pied de page lu) |
| Date d'effet | **1er janvier 1998** (application de droit commun de la loi de finances) |

- Local : `PDFs/JORT/1997/fr/Jo10497.pdf` (**page 5 du PDF**)
- URL FR : `https://www.pist.tn/jort/1997/1997F/Jo10497.pdf` — **vérifiée** (HTTP 200)
- URL AR : `https://www.pist.tn/jort/1997/1997A/Ja10497.pdf` — **vérifiée** (HTTP 200)

### 3.3 L'incorporation du taux de 10 % au code — *établi (JORT, lu à l'image)*

Avant 2002, le taux de 10 % existe, mais **éparpillé dans les lois de finances** et non dans le code
(loi 94-127 art. 56-58 ; loi 95-109 art. 36-38 ; loi 96-113 art. 19 ; loi 97-88 art. 28 ; loi 99-101
art. 19 et 32 ; loi 2000-98 art. 40). La **loi n° 2001-123 du 28 décembre 2001 (LF 2002)** y met bon
ordre, sous l'intitulé « **Incorporation du taux de 10 % au code de la taxe sur la valeur ajoutée** » :

> « **ARTICLE 82 :** Est ajouté à l'article 7 du code de la taxe sur la valeur ajoutée un alinéa 3
> ainsi libellé : "3) au taux de **10 %**, les opérations portant sur les produits, activités et
> services repris au tableau « **B bis** » figurant en annexe".
> **ARTICLE 83 :** La liste des produits et activités repris au tableau « B bis » […] est fixée
> conformément au tableau « L » annexé à la présente loi.
> **ARTICLE 84 :** Sont abrogées les dispositions prévues par les articles suivants : […] »

| | |
|---|---|
| Signature | **28 décembre 2001** |
| Publication | **JORT n° 104 du 28 décembre 2001**, tome 144 ; la loi commence p. 4251, les **articles 82 à 84 sont p. 4260** (pied de page lu) |
| Date d'effet | **1er janvier 2002** (art. 97 de la même loi) |

**Contenu du tableau « L » — c'est-à-dire du tableau B bis, liste des opérations au taux de 10 %**
(JORT n° 104, **p. 4359**, dernière page de la loi ; *établi — lu à l'image*) :

> **I. LES PRODUITS** — 1) machines pour le traitement de l'information (positions 84-71, 84-73,
> 85-42) ; 2) véhicules de transport de personnes d'une puissance n'excédant pas 4 chevaux fiscaux,
> d'une cylindrée n'excédant pas 1 200 cm3 et de moins de trois ans d'âge (position 87-03), à
> l'exclusion des véhicules tous terrains ; 3) équipements n'ayant pas de similaires fabriqués
> localement, et équipements fabriqués localement, prévus par le code d'incitation aux
> investissements.
> **II. LES ACTIVITÉS ET SERVICES** — 1) transport de marchandises ; 2) entreprises hôtelières
> (hébergement, restauration, ventes à consommer sur place, animation) ; 3) excursions et circuits
> pour touristes non résidents ; 4) hébergement des touristes non résidents par les agences de
> voyage ; 5) plongée sous-marine et promenades en mer ; 6) parcs animaliers ; 7) terrains de golf ;
> 8) jeux des parcs d'attraction ; 9) thalassothérapie et thermalisme ; 10) restauration ;
> 11) services des **architectes, ingénieurs-conseils, dessinateurs, géomètres, topographes, avocats,
> notaires, huissiers-notaires, interprètes, conseils juridiques et fiscaux, entrepreneurs de tenue de
> comptabilité et experts** ; 12) services informatiques ; 13) services de formation ; 14) services
> Internet ; 15) collecte des déchets de plastique.

**Deux constats décisifs, et qui ne vont pas de soi :**
1. **Ni les produits pétroliers (27-10, 27-11), ni l'électricité ne figurent au tableau B bis.** Leur
   taux réduit ne repose donc à aucun moment sur le code entre 2002 et 2014 : il reste suspendu aux
   décrets annuels de l'article 8 (§ 4).
2. **Les professions libérales sont au taux de 10 % dès 2002** — elles avaient déjà quitté le taux de
   6 % le **1er avril 1996** (voir ci-dessous).

**Le déclassement des professions libérales, de 6 % à 10 %, date de 1996, non de 2017.** L'**article 37
§ 6 de la loi n° 95-109 (LF 1996)** soumet au taux de 10 % « les services rendus par : les architectes
et les ingénieurs-conseils ; les avocats, les notaires, les huissiers-notaires et les interprètes ;
les conseils juridiques et les conseils fiscaux ; les entrepreneurs de tenue de comptabilité ; les
experts quelle que soit leur spécialisation » ; l'**article 39** en fixe l'effet au **1er septembre
1996** pour les § 1 à 5 et l'**article 38** au **1er avril 1996** pour le § 6, en supprimant à cette
date la liste des professions du § I du tableau B, **remplacée** par une liste réduite : « les
exploitants de laboratoire d'analyses ; les infirmiers et les masseurs ; les médecins, médecins
spécialistes, dentistes, sages-femmes et vétérinaires ; les dessinateurs, géomètres et topographes au
titre des services relatifs à l'immatriculation foncière des terres agricoles ». *Seules les
professions de santé restent donc au taux réduit de 6 %.* Les contrats enregistrés au plus tard le
31 mars 1996 demeurent à 6 % jusqu'au 31 décembre 1996.
*Établi (texte officiel à couche texte, JORT n° 104 des 29-31 décembre 1995, p. 2371-2372).*

- Local : `PDFs/JORT/2001/fr/Jo1042001.pdf` (**page 12 du PDF** pour les art. 82-84 ; **page 111** pour
  le tableau « L ») — *pas de couche texte exploitable
  pour ces pages : lecture à l'image obligatoire*
- URL FR : `https://www.pist.tn/jort/2001/2001F/Jo1042001.pdf` — **vérifiée** (HTTP 200)

### 3.4 1er janvier 2007 : 10 % → 12 %, et suppression du taux de 29 % — *établi (texte officiel à couche texte ; pagination de notice)*

**Loi n° 2006-80 du 18 décembre 2006, relative à la réduction des taux de l'impôt et à l'allègement de
la pression fiscale sur les entreprises**, chapitre II « En matière de taxe sur la valeur ajoutée et
du droit de consommation » :

> « **Suppression du taux de 29 % de la TVA et imposition de certains produits au droit de
> consommation** — **ARTICLE 13 :** Est supprimé le numéro 2 du deuxième paragraphe de l'article 7 du
> code de la TVA. »

> « **ARTICLE 17 :** 1) Est remplacé par le taux de **12 %**, le taux de **10 %** prévu par le numéro 3
> du deuxième paragraphe de l'article 7 du code de la taxe sur la valeur ajoutée.
> 2) Est remplacé par le taux de 12 % le taux de la taxe sur la valeur ajoutée de 10 % **partout où il
> est prévu par les textes législatifs et réglementaires en vigueur**. »

| | |
|---|---|
| Signature | **18 décembre 2006** |
| Publication | **JORT n° 101 du 19 décembre 2006**, tome 149, **p. 4302-4303** *(pagination issue de la notice de la base, non d'un pied de page lu)* |
| Date d'effet | **1er janvier 2007** |

- Local : `PDFs/JORT/2006/fr/Jo1012006.pdf` (couche texte exploitable)
- URL FR : `https://www.pist.tn/jort/2006/2006F/Jo1012006.pdf` — **vérifiée** (HTTP 200)

**Corroboration indépendante** : le code consolidé DGELF porte, sous l'article 7, « 2) *(abrogé par
l'art. 13 loi n° 2006-80 du 18/12/2006…)* » et, en note, « **Il s'agit des produits soumis jusqu'au
31/12/2006 à la TVA au taux de 29 %** ».

*Le taux majoré aura donc existé du **1er juillet 1988 au 31 décembre 2006**. Les produits concernés
n'ont pas été détaxés : ils ont été **transférés au droit de consommation** (art. 14 de la même loi,
qui les ajoute au tableau annexé à la loi 88-62).*

### 3.5 1er janvier 2018 : le relèvement d'un point des trois taux — *établi (texte officiel à couche texte)*

**Article 43 de la loi n° 2017-66 du 18 décembre 2017 (LF 2018)**, « Révision des taux de la taxe sur
la valeur ajoutée » :

> « 1) Est remplacé le taux de **18 %** prévu au premier paragraphe de l'article 7 du code de la taxe
> sur la valeur ajoutée par le taux de **19 %**.
> 2) Est remplacé le taux de **6 %** de la taxe sur la valeur ajoutée par le taux de **7 %**, là où il
> est prévu aux textes législatifs et règlementaires en vigueur.
> 3) Est remplacé le taux de **12 %** de la taxe sur la valeur ajoutée par le taux de **13 %**, là où
> il est prévu aux textes législatifs et règlementaires en vigueur. »

| | |
|---|---|
| Signature | **18 décembre 2017** |
| Publication | **JORT n° 101 du 19 décembre 2017** ; l'**article 43 est p. 4280-4281** (pied de page lu dans le PDF officiel de la loi) |
| Date d'effet | **1er janvier 2018** |

- Local : `PDFs/Lois_de_Finances/Loi_n_2017-66_du_18_décembre_2017_portant_loi_de_finances_pour_lannée_2018.pdf`
- URL FR : `https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf` — **vérifiée** (HTTP 200)
- URL AR : `https://www.pist.tn/jort/2017/2017A/Ja1012017.pdf` — **vérifiée** (HTTP 200)

### 3.6 État actuel de l'article 7 — *établi (code consolidé DGELF, mis à jour au 1er janvier 2023)*

> « **ARTICLE 7.-** Sont soumis à la taxe sur la valeur ajoutée au taux de **19 %**, les opérations
> portant sur les biens et les services non soumis à un autre taux. *(Modifié art 25 LF 97-88 du
> 29/12/1997 et par l'article 43 de la LF 2018)*
> Toutefois sont soumises à la taxe sur la valeur ajoutée :
> 1) au taux de **7 %**, les opérations portant sur les biens et les services repris au tableau "B"
> figurant en annexe ; *(Modifié par l'article 43 de la LF 2018)*
> 2) *(abrogé par l'art. 13 loi n° 2006-80 du 18/12/2006)*
> 3) au taux de **13 %** les opérations suivantes : *(Modifié par l'article 27 de la LF 2017 et par
> l'article 43 de la LF 2018)* — l'importation et la vente des **produits pétroliers** relevant des
> numéros 27-10 et 27-11 du tarif des droits de douane […] ; la vente de l'**électricité basse tension
> destinée à la consommation domestique** *(Modifié par l'article 65 de la loi de finances 2019)* ;
> *(un tiret supprimé par l'article 44 de la LF 2023)* ; la **vente des immeubles bâtis à usage
> exclusif d'habitation** réalisés par les promoteurs immobiliers […]. »

- Source : `PDFs/TVA/Code_de_la_taxe_sur_la_valeur_ajoutée_2023.pdf` (**français**, couche texte
  fiable). Le millésime **2025** du même code est **en arabe seulement** : pour citer en français,
  utiliser le millésime 2023, ou l'arabe 2025 avec relecture arabophone.

**Ajustements postérieurs à 2018, de périmètre et non de taux** (à ne pas confondre avec des
changements de taux) : **LF 2019** (loi 2018-56) art. 64 et 65 — la téléphonie fixe et l'internet fixe
ADSL domestique, ainsi que l'**électricité moyenne et basse tension d'irrigation agricole**, quittent
le 13 % pour le **tableau B (7 %)** ; **LF 2023** art. 44 — suppression d'un tiret du n° 3 ;
**LF 2025** (loi n° 2024-48 du 9 décembre 2024) **art. 31** — l'électricité basse tension domestique
reste à 13 % **au-delà de 300 kWh par mois** et passe au tableau B (7 %) **en deçà** ; **art. 59** —
ajout des olives conservées provisoirement au tableau B.

---

## 4. Les deux séries de décrets annuels — correction du plan initial

### 4.1 Le mécanisme, établi sur texte

**Étape 1 — la sortie du taux réduit.** **Article 40 de la loi n° 95-109 du 25 décembre 1995
(LF 1996)** :

> « **Article 40 :** Sont supprimées **à compter d'une date qui sera fixée par décret** les
> dispositions figurant au **n° 2 du paragraphe II** et au **n° 4 du paragraphe III** du tableau "B"
> annexé au code de la taxe sur la valeur ajoutée. »

C'est-à-dire (§ 1.6) : l'**électricité et le gaz** (II-2) et les **huiles de pétrole vendues par les
entreprises de distribution** (III-4) **sortent du taux réduit de 6 %** et retombent au taux normal.
*Établi (texte officiel à couche texte, JORT n° 104 des 29-31 décembre 1995, p. 2371-2372).*

**Étape 2 — le décret qui fixe la date.** Les décrets de la série citent en visa le « **décret
n° 97-1339 du 14 juillet 1997, relatif à la fixation de la date de mise en application des
dispositions de l'article 40 de la loi n° 95-109** ». **Non établi** : ce décret **n'est pas dans
`jort_cache.db`** — les textes signés le 14 juillet 1997 qu'elle contient portent les numéros 97-1349
à 97-1372 ; le 97-1339 en est absent. Son existence est certaine (deux décrets le visent nommément),
mais **sa référence de publication n'a pas été établie**. À chercher dans les fascicules JORT de
juillet-août 1997 (`PDFs/JORT/1997/fr/`, n° 57 à 61).

**Étape 3 — la restauration annuelle.** Chaque année, un ou deux décrets pris **sur le fondement de
l'article 8 du code** (visé en tête de tous) réduisent le taux applicable. L'article 8 limitant
l'effet de telles mesures à l'**année civile**, chaque décret porte une clause de durée explicite :

> décret 98-384, **art. 3** : « … s'appliquent **du 1er janvier 1998 au 31 décembre 1998**. »
> décret 99-211, **art. 2** : « … s'appliquent **à partir du 1er janvier 1999 jusqu'au 31 décembre 1999**. »
> décret 2005-3384, **art. 2** : « … s'appliquent **du 1er janvier 2006 au 31 décembre 2006**. »
> décret 2005-3383, **art. 2** : « … s'appliquent **aux quantités d'énergie électrique consommées du
> 1er janvier 2006 au 31 décembre 2006**. »
> décret 2007-1, **art. 2** : « … **du 1er janvier 2007 au 31 décembre 2007**. »
> décret 2010-3587, **art. 2** : « … **du 1er janvier 2011 au 31 décembre 2011**. »
> décret 2012-3413, **art. 2** : « … **à partir du 1er janvier 2013 au 31 décembre 2013**. »

### 4.2 Une bifurcation décisive en 1998 : les carburants quittent la TVA réduite

**Décret n° 98-952 du 27 avril 1998, relatif à la fiscalité des produits pétroliers, de l'électricité
et du gaz** — *établi (texte officiel à couche texte)*. Ce texte, visé par **tous** les décrets
ultérieurs de la série, est le pivot que le plan initial ignorait :

> « **Article premier.** - Est réduit à **10 %** le taux de la taxe sur la valeur ajoutée applicable à
> l'**électricité basse tension destinée à la consommation domestique** et ce **jusqu'au 31 décembre
> 1998**.
> **Art. 2.** - Le **tarif du droit de consommation** applicable aux produits relevant des numéros
> **27-09, 27-10 et 27-11** du tarif des droits de douane est fixé conformément au tableau suivant
> […] *(essence super 22,4469 D/hl ; essence super sans plomb 18,7758 D/hl ; gaz de pétrole en
> bouteilles ≤ 13 kg 8,256 D/tonne ; en vrac ou > 13 kg 42,077 D/tonne, etc.)*
> **Art. 3.** - Les dispositions du présent décret s'appliquent **à compter du 6 mai 1998**.
> **Art. 4.** - Sont abrogées toutes dispositions antérieures contraires au présent décret et
> notamment les dispositions du **décret n° 98-384 du 10 février 1998** susvisé. »

| | |
|---|---|
| Signature | **27 avril 1998** |
| Publication | **JORT n° 35 du 1er mai 1998**, **p. 923** (pied de page, **couche texte** — non relu à l'image) |
| Date d'effet | **6 mai 1998** |

**Conséquence, à écrire sans ambiguïté** : à partir du 6 mai 1998, les **produits pétroliers ne sont
plus l'objet d'un taux réduit de TVA** — ils relèvent d'un **droit de consommation** à tarif
spécifique — tandis que l'**électricité** conserve un taux réduit de TVA reconduit chaque année. La
série « produits pétroliers » est donc **interrompue de mai 1998 à juillet 2004** et ne reprend
qu'avec le **décret n° 2004-1773 du 2 août 2004** (§ 4.3). *Cela invalide l'idée de deux séries
parallèles continues, et explique l'absence — longtemps inexpliquée — de décret « pétrole » entre 1999
et 2003.*

**Objection examinée et écartée.** On pouvait craindre que l'incorporation du taux de 10 % au code par
la LF 2002 (§ 3.3) ait rétabli discrètement un taux réduit pour les carburants, ce qui aurait réduit
l'interruption aux seules années 1998-2001. **Ce n'est pas le cas** : le **tableau « L »** annexé à la
loi n° 2001-123, qui constitue le contenu du tableau B bis, a été lu à l'image (JORT n° 104 du
28 décembre 2001, **p. 4359**) et **ne mentionne ni les positions 27-10 et 27-11, ni l'électricité**.
L'interruption court donc bien de **mai 1998 à juillet 2004**. *Corollaire : l'électricité non plus ne
figure pas au tableau B bis — son taux réduit a continué de reposer sur les décrets annuels pris au
titre de l'article 8, jusqu'à la LF 2015.*

- Local : `PDFs/JORT/1998/fr/Jo03598.pdf`
- URL FR : `https://www.pist.tn/jort/1998/1998F/Jo03598.pdf` — **vérifiée** (HTTP 200, 1 561 199 o)
- URL AR : `https://www.pist.tn/jort/1998/1998A/Ja03598.pdf` — **vérifiée** (HTTP 200)

### 4.3 Les taux de la série, et qui les fixe réellement

- **1998** : régime **asymétrique et scindé en deux périodes**. Du 1er janvier au 5 mai : décret
  98-384, **10 %** sur « l'essence super, l'essence normale, le gasoil, le fuel-oil domestique et le
  gaz de pétrole, propane et butane » (art. 1er) et **6 %** sur « l'électricité basse tension destinée
  à la consommation domestique » (art. 2). À partir du 6 mai : décret 98-952, **10 %** sur
  l'électricité, **droit de consommation** sur les produits pétroliers.
- **1999 → 2006** : **10 %**, sur la **seule électricité**.
- **2007 → 2017** : **12 %**. **Ce n'est pas le décret qui décide.** Les décrets 2007-1 et 2007-2
  visent expressément « l'**article 17 de la loi n° 2006-80 du 18 décembre 2006** » : c'est cette loi
  qui a substitué 12 % à 10 % « partout où il est prévu par les textes législatifs et réglementaires
  en vigueur » (§ 3.4). Les décrets annuels ne font qu'en tirer les conséquences.
- **2018 → aujourd'hui** : **13 %**, par l'article 43 de la LF 2018 (§ 3.5).

**Couverture année par année.** La base indexe `jort_annee` sur l'année de **signature** : un décret
signé fin décembre et publié en janvier apparaît sous l'année précédente. Le tableau ci-dessous est
construit sur l'**année d'application** telle qu'elle est écrite dans l'article de durée de chaque
décret.

| Année d'application | Électricité | Produits pétroliers | Publication | Vérifié |
|---|---|---|---|---|
| 1998 | 98-384 art. 2 (**6 %**), puis 98-952 art. 1er (**10 %**) dès le 6 mai | 98-384 art. 1er (10 %) **jusqu'au 5 mai**, puis **droit de consommation** | JORT 1998 n° 15, 20 févr. 1998, p. 376 ; n° 35, 1er mai 1998, p. 923 | **lu** |
| 1999 | 99-211 (10 %) | **aucun — droit de consommation** | JORT 1999 n° 11, 5 févr. 1999, p. 198 | **lu** |
| 2000 | 2000-329 | *idem* | JORT 2000 n° 14, 18 févr. 2000, p. 497 | probable |
| 2001 | 2001-401 | *idem* | JORT 2001 n° 13, 13 févr. 2001, p. 292 | probable |
| 2002 | 2002-209 | *idem* | JORT 2002 n° 12, 8 févr. 2002, p. 330 | probable |
| 2003 | 2003-133 | *idem* | JORT 2003 n° 6, 21 janv. 2003, p. 166 | probable |
| 2004 | 2004-9 | **2004-1773** — reprise de la série, **à compter du 1er août 2004**, sans terme énoncé | JORT 2004 n° 3, p. 83 ; **n° 63, 6 août 2004, p. 2239-2240** | pétrole **lu** ; électricité non lu |
| 2005 | 2004-2728 | 2004-2727 | JORT **2005** n° 1, 4 janv. 2005, p. 5-6 | probable |
| **2006** | **2005-3383** | **2005-3384** | JORT **2006** n° 1, 3 janv. 2006, p. 8-9 | **lu** |
| 2007 | 2007-2 | 2007-1 | JORT 2007 n° 2, 5 janv. 2007, p. 30-31 | **lu** |
| 2008 | 2008-2 | 2008-1 | JORT 2008 n° 2, 4 janv. 2008, p. 57-58 | **lu** (électricité) |
| 2009 | 2008-3967 | 2008-4113 | JORT **2009** n° 1, p. 33 ; n° 4, p. 154 | **lu** (électricité) |
| 2010 | 2009-3762 | 2009-3761 | JORT 2009 n° 103, 25 déc. 2009, p. 4171-4172 | **lu** (pétrole) |
| **2011** | **2010-3586** | **2010-3587** | JORT **2011** n° 1, 4 janv. 2011, p. 31-32 | **lu** |
| 2012 | 2012-9 | 2012-6 | JORT 2012 n° 2, 6 janv. 2012, p. 230 et 235 | **lu** (pétrole) |
| **2013** | **2012-3414** | **2012-3413** | JORT **2013 n° 1, 1er janvier 2013, p. 201-202** | **lu** |
| 2014 | 2013-5197 | 2013-5198 | JORT 2013 n° 105, 31 déc. 2013, p. 3866-3867 | **lu** |
| 2015 → | *fin de la série* — loi 2014-59, art. 36 | idem | JORT 2014 n° 105, 30 déc. 2014, p. 3468-3469 | **lu** |

*« lu » = clause de durée lue dans le texte officiel ; « probable » = objet de la notice, clause de
durée non lue.*

**Le décret n° 2004-1773 mérite une mention particulière** (*établi — JORT, lu à l'image*) : il rétablit
le taux de 10 % sur les produits 27-10 et 27-11 après six ans d'interruption, et son **article 2 ne
porte pas de terme** — « Les dispositions du présent décret s'appliquent **à compter du 1er août
2004** » — alors que tous les autres décrets de la série bornent leur effet au 31 décembre. L'article 8
du code limitant de toute façon la mesure à l'année civile, la portée pratique est la même, mais la
rédaction est singulière et vaut d'être signalée. Publication : **JORT n° 63 du 6 août 2004, p. 2239-
2240** (sommaire et pied de page lus) ; local `PDFs/JORT/2004/fr/Jo0632004.pdf` (**pages 15-16 du
PDF** ; couche texte inutilisable, lecture à l'image obligatoire).

### 4.4 Les trois anomalies du plan : toutes résolues

**(a) 2006 et 2011 — artefact de datation.** Les deux années sont couvertes, par des décrets signés en
décembre de l'année précédente et publiés au JORT n° 1 de l'année concernée (voir le tableau).

**(a bis) 2013 — faux négatif de ma propre recherche, corrigé.** J'ai d'abord conclu qu'aucun texte ne
couvrait l'année d'application 2013 : recherches `LIKE` **et** FTS sur toutes les signatures du
1er novembre 2012 au 31 décembre 2013, lecture du texte français intégral de la **LF 2013** (loi
n° 2012-27, 8 740 lignes) et des **trois lois de finances complémentaires** de la période — rien.
**Cette conclusion était fausse.** Le balayage des fascicules JORT locaux de janvier-février 2013 fait
apparaître, dès le **JORT n° 1 du 1er janvier 2013** :

> **Décret n° 2012-3413 du 31 décembre 2012**, portant réduction à 12 % du taux de la TVA sur certains
> produits pétroliers (**p. 201**) — art. 1er : 12 % sur les produits 27-10 et 27-11 ; **art. 2 : « Les
> dispositions du présent décret s'appliquent à partir du 1er janvier 2013 au 31 décembre 2013. »**
> **Décret n° 2012-3414 du 31 décembre 2012**, portant réduction à 12 % du taux de la TVA applicable à
> l'électricité basse tension à usage domestique et à l'électricité moyenne et basse tension d'irrigation
> (**p. 202**) — **art. 2 : « … s'appliquent aux quantités d'énergie électrique consommées à partir du
> 1er janvier 2013 au 31 décembre 2013. »**
> *Signés par le Chef du gouvernement Hamadi Jebali ; visent l'article 8 du code et la LF 2013.*

**Cause du faux négatif** : les deux décrets **sont bien dans la base** (recids 79653 et 79654), mais
leur `objet` y est enregistré **en arabe** (« يتعلق بالتخفيض إلى 12% في نسبة الأداء على القيمة
المضافة… »). Aucune requête française, `LIKE` ou FTS, ne pouvait les atteindre. Un balayage en arabe
(`objet LIKE '%الأداء على القيمة المضافة%'` combiné à `%البترولية%` ou `%الكهرباء%`) les fait
apparaître immédiatement, et confirme qu'**aucun autre décret de la série n'est dissimulé de la sorte**.
*Leçon générale, reportée en tête de note : sur la période 2011-2020, toute conclusion négative tirée
d'une requête française est sans valeur.*

**(b) Le passage du décret à la loi en 2014 — résolu.** **Article 36 de la loi n° 2014-59 du
26 décembre 2014 (LF 2015)** :

> « 1- Sont ajoutés au paragraphe I du tableau « **B bis** » annexé au code de la TVA les numéros **5**
> et **6** ainsi libellés : **5)** — l'électricité basse tension destinée à la consommation domestique ;
> — l'électricité moyenne et basse tension utilisée pour le fonctionnement des équipements de pompage
> de l'eau destinée à l'irrigation agricole. **6)** Les produits pétroliers relevant des numéros 27-10
> et 27-11 du tarif des droits de douane […] »

**Le changement de véhicule est un changement de nature juridique** : tant que la réduction reposait
sur l'article 8 du code, elle était par définition **conjoncturelle et annuelle** ; inscrite à une
**annexe du code**, elle devient **permanente**, et la reconduction par décret perd son objet.
Publication : **JORT n° 105 du 30 décembre 2014**, tome 157 ; article 36 **p. 3468-3469** (pied de page
lu). Local : `PDFs/Lois_de_Finances/Loi_de_Finances_2015.pdf` ; URL
`https://www.pist.tn/jort/2014/2014F/Jo1052014.pdf` — **vérifiée** (HTTP 200).
*Piège d'homonymie : le § 3 de l'**article 37** ajoute au même tableau B bis un **numéro 4** (produits
d'aide au sevrage tabagique). Ne pas le confondre avec les numéros 5 et 6 de l'article 36.*

**(c) Ce que devient le taux réduit après 2014 — résolu.** Trois étapes :
1. **LF 2016** (loi n° 2015-53 du 25 décembre 2015), art. 30-31 : refonte d'ensemble ; les tableaux A,
   B et B bis sont remplacés par des tableaux « **nouveaux** » annexés à la loi.
2. **LF 2017** (loi n° 2016-78 du 17 décembre 2016), art. 27 : le **tableau B bis est abrogé** (§ 5) et
   son contenu réécrit **directement dans l'article 7**, au n° 3 du deuxième paragraphe, « au taux de
   **12 %** » : produits pétroliers 27-10 et 27-11, électricité basse tension domestique et
   électricité moyenne et basse tension d'irrigation, **plus les services des professions libérales**
   (architectes, ingénieurs-conseils, dessinateurs, géomètres, topographes, avocats, notaires,
   huissiers-notaires, interprètes, conseils fiscaux, entrepreneurs de tenue de comptabilité,
   experts). **Attention à un contresens tentant** : ces professions ne quittent pas le taux de 6 % à
   cette occasion — elles l'avaient quitté **le 1er avril 1996** (art. 37 à 39 de la loi n° 95-109,
   § 3.3) et figuraient au tableau B bis à 10 % depuis 2002, puis à 12 % depuis 2007. La LF 2017 ne
   fait que les transférer du tableau B bis, qu'elle abroge, vers le corps de l'article 7, **à taux
   inchangé**.
3. **LF 2018**, art. 43 : 12 % → **13 %**.

**Ce qui autorise à affirmer que la série des décrets s'arrête bien en 2014.** L'argument ne repose
pas seulement sur l'absence de résultat en français. Le balayage **en arabe** de la base
(`objet LIKE '%الأداء على القيمة المضافة%'` croisé avec `%البترولية%` ou `%الكهرباء%`) ne renvoie que
**quatre** enregistrements, toutes années confondues : les décrets 2012-3413 et 2012-3414, la
loi 2018-56 (LF 2019) et la loi de finances 2025. Or la part d'objets en arabe **culmine précisément
en 2015-2019** (43 % à 82 %), c'est-à-dire là où se cacherait un décret postérieur à la LF 2015 s'il
existait. L'absence est donc testée dans la langue où le risque de faux négatif est maximal.

**Le taux réduit existe donc toujours, à 13 %, et couvre toujours les carburants et l'électricité
domestique** — cette dernière dans la limite fixée par la LF 2025 (au-delà de 300 kWh/mois ; en deçà,
7 %).

---

## 5. Lacunes — ce qui n'a pas pu être établi

1. **Décret n° 97-1339 du 14 juillet 1997** (date de mise en application de l'article 40 de la loi
   95-109) : **absent de `jort_cache.db`** — les textes signés ce jour-là qu'elle contient portent les
   numéros 97-1349 à 97-1372. Référence de publication non établie. C'est le pivot du § 4.1 : à
   chercher dans `PDFs/JORT/1997/fr/`, fascicules n° 57 à 61 (juillet-août 1997).
2. **Clauses de durée non lues** pour les décrets marqués « probable » au tableau du § 4.3 (2000-329,
   2001-401, 2002-209, 2003-133, 2004-9, 2004-2727, 2004-2728). Rien n'indique qu'elles s'écartent du
   modèle, mais elles n'ont pas été lues. Le fascicule JORT 2004 n° 3 (`Jo0032004.pdf`) n'a pas de
   couche texte exploitable : lecture à l'image nécessaire.
3. **Entrée dans le champ des grossistes en alimentation générale** et **des forfaitaires**
   (articles 16 et 17 du code) : dates non établies, voir § 2.3.
4. **Tableau B bis : lu et clos.** Son contenu d'origine (tableau « L » de la LF 2002, p. 4359) a été
   lu à l'image (§ 3.3). Ses remaniements intermédiaires (LF 2016, art. 31, qui lui substitue un
   « tableau B bis nouveau ») n'ont pas été dépouillés poste par poste, mais la question qui importait
   — carburants et électricité y figurent-ils ? — est tranchée pour 2002, et la LF 2015 (art. 36) dit
   explicitement qu'elle **y ajoute** ces produits en 2015, ce qui confirme qu'ils n'y étaient pas.
5. **Tableau A actuel** : la présente note établit le tableau A **de 1988**. L'état en vigueur
   (« tableau A nouveau », refondu par la LF 2016 et amputé par la LF 2017) n'a pas été dépouillé
   poste par poste ; il figure dans le code consolidé DGELF 2023, partie annexes.
6. **Édition française du code consolidé 2025** : le millésime 2025 disponible localement est **en
   arabe uniquement**. Toute citation française de l'état du droit au 1er janvier 2025 doit passer par
   le millésime **2023** (français) complété des LF 2024 et 2025, ou par une relecture arabophone.
7. **Édition française de la LF 2016** : introuvable sur pist.tn
   (`https://www.pist.tn/jort/2015/2015F/Jo1042015.pdf` répond **404** ; le champ `pdf_fr` de la base
   est `NULL`). Seule l'édition arabe est en ligne (`…/2015A/Ja1042015.pdf`, HTTP 200). Le texte
   français a été lu dans `PDFs/Lois_de_Finances/Loi_de_Finances_2016.pdf`, dont l'appartenance au
   fascicule n'a pas été vérifiée par un pied de page.

**Deux points signalés comme lacunes dans une version antérieure de cette note, et désormais résolus,
consignés ici pour mémoire :**
- *L'absence de décret « pétrole » de 1999 à 2003* n'est pas une lacune documentaire : c'est un fait
  juridique, expliqué par le décret 98-952 (§ 4.2).
- *La divergence de référence sur la LF 2025* est levée. L'enregistrement « JORT 2024 n° 156 » que
  j'avais relevé sous le numéro « 2024-48 » est un **arrêté** n° 2024-48 du 25 décembre 2024, sans
  rapport avec la loi de finances. La **loi n° 2024-48 du 9 décembre 2024** figure bien dans la base,
  sous un `numero` mal analysé (**« 2024-149 », qui reprend le numéro du fascicule**), avec 71 notices :
  **JORT n° 149 du 10 décembre 2024, tome 167, p. 6418 à 6453** ; l'**article 31** (électricité) est
  **p. 6426** et l'**article 59** (produits agricoles) **p. 6446**. Cette pagination est cohérente avec
  celle de la note IRPP du dépôt (p. 6429 pour l'article 36). La pagination « p. 3420 et suivantes »
  lue en pied de page du PDF `Loi_de_Finances_2025.pdf` relève donc d'un **tirage à pagination
  distincte** : **citer la pagination du JORT (6418-6453), pas celle du PDF**. À noter : l'URL
  française `…/2024F/Jo1492024.pdf` répond **404**, l'arabe `…/2024A/Ja1492024.pdf` répond 200.

---

## Annexe A — Références candidates (CSL-JSON)

**Aucune de ces entrées n'existe dans `precis/fr/fiscalite/references.json`** (clés existantes :
`ayadi1996`, `baccouche2008`, `bastier1997`, `code-irpp-is-1990`, `dgi-nc-*`, `eset2016`,
`gbo-depenses-fiscales`, `lapresse2025`, `lf-1986`, `lf-1991`, `lf-1993`, `lf-1998`, `lf-2005`,
`lf-2007`, `lf-2010`, `lf-2014`, `lf-2016`, `lf-2017`, `lf-2018`, `lf-2020`, `lf-2021`, `lf-2024`,
`loi-98-73`, `loi-avantages-fiscaux-2017`, `mesple-somps2022`, `minfin-*`, `touaiti2026`, `yaich`)
**ni dans `precis/fr/references.json`**.

*Avertissement de nommage* : les clés `lf-1998`, `lf-2017` et `lf-2018` **existent déjà** ; leur
contenu n'a pas été vérifié ici. Si elles désignent bien les lois n° 97-88, n° 2016-78 et n° 2017-66,
**les réutiliser** plutôt que de créer `loi-97-88-lf-1998`, `loi-2016-78-lf-2017` et
`loi-2017-66-lf-2018`. Idem pour `loi2001-123-lf2002`, déjà présente dans `precis/fr/references.json`.

```json
[
  {
    "id": "loi-88-61-tva",
    "type": "legislation",
    "title": "Loi n° 88-61 du 2 juin 1988, portant promulgation du code de la taxe sur la valeur ajoutée",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "39",
    "volume": "131",
    "page": "827-846",
    "issued": {"date-parts": [[1988, 6, 2]]},
    "URL": "https://www.pist.tn/jort/1988/1988F/Jo03988.pdf",
    "note": "Publié le 10 juin 1988. Code annexé : art. 1 (champ) p. 827, art. 2 (assujettis) p. 827-828, art. 5 (fait générateur) p. 828, art. 7 et 8 (taux) p. 829, tableau A p. 833-836, tableaux B et C p. 836-837. Édition arabe : https://www.pist.tn/jort/1988/1988A/Ja03988.pdf. URL vérifiées (HTTP 200)."
  },
  {
    "id": "decret-88-1109-calendrier-tva",
    "type": "legislation",
    "title": "Décret n° 88-1109 du 11 juin 1988, fixant le calendrier d'application de la taxe sur la valeur ajoutée et du droit de consommation",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "42",
    "volume": "131",
    "page": "923",
    "issued": {"date-parts": [[1988, 6, 11]]},
    "URL": "https://www.pist.tn/jort/1988/1988F/Jo04288.pdf",
    "note": "Publié le 21 juin 1988. Applique le code au 1er juillet 1988, sauf art. 1er II-3 et art. 16 et 17 I et II-1. Édition arabe : https://www.pist.tn/jort/1988/1988A/Ja04288.pdf."
  },
  {
    "id": "decret-89-1222-calendrier-tva-gros",
    "type": "legislation",
    "title": "Décret n° 89-1222 du 25 août 1989, fixant le calendrier de mise en application de la taxe sur la valeur ajoutée",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "61",
    "volume": "132",
    "page": "1395",
    "issued": {"date-parts": [[1989, 8, 25]]},
    "URL": "https://www.pist.tn/jort/1989/1989F/Jo06189.pdf",
    "note": "Publié le 12 septembre 1989. Applique l'art. 1er II-3 (commerce de gros) au 1er octobre 1989, sauf grossistes en alimentation générale. ATTENTION : le sommaire du fascicule annonce p. 1396 ; le texte est p. 1395. Édition arabe : https://www.pist.tn/jort/1989/1989A/Ja06189.pdf."
  },
  {
    "id": "lf-1996",
    "type": "legislation",
    "title": "Loi n° 95-109 du 25 décembre 1995, portant loi de finances pour la gestion 1996",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "104",
    "volume": "138",
    "page": "2371-2372",
    "issued": {"date-parts": [[1995, 12, 25]]},
    "URL": "https://www.pist.tn/jort/1995/1995F/Jo10495.pdf",
    "note": "Publié les 29-31 décembre 1995. Art. 40 : sortie de l'électricité, du gaz et des huiles de pétrole du tableau B (6 %). Art. 43 et 46 : assujettissement du commerce de détail au-delà de 100 000 D, au 1er juillet 1996."
  },
  {
    "id": "loi-97-88-lf-1998",
    "type": "legislation",
    "title": "Loi n° 97-88 du 29 décembre 1997, portant loi de finances pour la gestion 1998",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "104",
    "volume": "140",
    "page": "2435-2560",
    "issued": {"date-parts": [[1997, 12, 29]]},
    "URL": "https://www.pist.tn/jort/1997/1997F/Jo10497.pdf",
    "note": "Publié les 30-31 décembre 1997. Art. 25 (taux normal 17 % -> 18 %), art. 26 et 27, p. 2437. Doublon possible avec la clé existante lf-1998."
  },
  {
    "id": "decret-98-384-tva-reduite",
    "type": "legislation",
    "title": "Décret n° 98-384 du 10 février 1998, portant réduction à 10 % du taux de la taxe sur la valeur ajoutée sur certains produits pétroliers et à 6 % du taux de la taxe sur la valeur ajoutée sur l'électricité basse tension destinée à la consommation domestique",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "15",
    "volume": "141",
    "page": "376",
    "issued": {"date-parts": [[1998, 2, 10]]},
    "URL": "https://www.pist.tn/jort/1998/1998F/Jo01598.pdf",
    "note": "Publié le 20 février 1998. Premier décret de la série. Art. 3 : application du 1er janvier au 31 décembre 1998. ABROGÉ dès le 6 mai 1998 par le décret 98-952. Édition arabe : https://www.pist.tn/jort/1998/1998A/Ja01598.pdf."
  },
  {
    "id": "decret-98-952-fiscalite-petrole-electricite",
    "type": "legislation",
    "title": "Décret n° 98-952 du 27 avril 1998, relatif à la fiscalité des produits pétroliers, de l'électricité et du gaz",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "35",
    "page": "923",
    "issued": {"date-parts": [[1998, 4, 27]]},
    "URL": "https://www.pist.tn/jort/1998/1998F/Jo03598.pdf",
    "note": "Publié le 1er mai 1998, effet au 6 mai 1998. Abroge le décret 98-384 ; maintient un taux de TVA de 10 % sur la seule électricité basse tension domestique et transfère les produits pétroliers (27-09, 27-10, 27-11) au droit de consommation. Texte pivot : visé par tous les décrets ultérieurs de la série. URL vérifiée (HTTP 200)."
  },
  {
    "id": "decret-2004-1773-tva-petroliers",
    "type": "legislation",
    "title": "Décret n° 2004-1773 du 2 août 2004, portant réduction à 10 % du taux de la taxe sur la valeur ajoutée sur certains produits pétroliers",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "63",
    "volume": "147",
    "page": "2239-2240",
    "issued": {"date-parts": [[2004, 8, 2]]},
    "URL": "https://www.pist.tn/jort/2004/2004F/Jo0632004.pdf",
    "note": "Publié le 6 août 2004. Rétablit le taux réduit de TVA sur les produits 27-10 et 27-11 après six ans d'interruption. Art. 2 : « s'appliquent à compter du 1er août 2004 », sans terme énoncé — rédaction singulière dans la série. URL vérifiée (HTTP 200)."
  },
  {
    "id": "loi-2001-123-lf-2002",
    "type": "legislation",
    "title": "Loi n° 2001-123 du 28 décembre 2001, portant loi de finances pour l'année 2002",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "104",
    "volume": "144",
    "page": "4251-4359",
    "issued": {"date-parts": [[2001, 12, 28]]},
    "URL": "https://www.pist.tn/jort/2001/2001F/Jo1042001.pdf",
    "note": "Art. 82 à 84 (incorporation du taux de 10 % à l'article 7 du code, tableau B bis) p. 4260 ; le tableau « L », qui constitue le tableau B bis, est p. 4359 (dernière page de la loi) et ne comporte ni produits pétroliers ni électricité. Effet au 1er janvier 2002 (art. 97). Doublon probable avec loi2001-123-lf2002 (precis/fr/references.json)."
  },
  {
    "id": "loi-2006-80-reduction-taux",
    "type": "legislation",
    "title": "Loi n° 2006-80 du 18 décembre 2006, relative à la réduction des taux de l'impôt et à l'allègement de la pression fiscale sur les entreprises",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "101",
    "volume": "149",
    "page": "4302-4303",
    "issued": {"date-parts": [[2006, 12, 18]]},
    "URL": "https://www.pist.tn/jort/2006/2006F/Jo1012006.pdf",
    "note": "Publié le 19 décembre 2006. Art. 13 : suppression du taux de 29 %. Art. 17 : remplacement du taux de 10 % par 12 %, dans le code et partout ailleurs. Effet au 1er janvier 2007."
  },
  {
    "id": "decret-2007-1-tva-petroliers",
    "type": "legislation",
    "title": "Décret n° 2007-1 du 3 janvier 2007, portant réduction à 12 % du taux de la taxe sur la valeur ajoutée sur certains produits pétroliers",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "2",
    "page": "30-31",
    "issued": {"date-parts": [[2007, 1, 3]]},
    "URL": "https://www.pist.tn/jort/2007/2007F/Jo0022007.pdf",
    "note": "Publié le 5 janvier 2007. Art. 2 : application du 1er janvier au 31 décembre 2007. Vise l'art. 8 du code et l'art. 17 de la loi 2006-80."
  },
  {
    "id": "decret-2007-2-tva-electricite",
    "type": "legislation",
    "title": "Décret n° 2007-2 du 3 janvier 2007, fixant à 12 % le taux de la taxe sur la valeur ajoutée applicable à l'électricité basse tension à usage domestique et à l'électricité moyenne et basse tension utilisée pour le fonctionnement des équipements de pompage de l'eau destinée à l'irrigation agricole",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "2",
    "page": "31",
    "issued": {"date-parts": [[2007, 1, 3]]},
    "URL": "https://www.pist.tn/jort/2007/2007F/Jo0022007.pdf",
    "note": "Publié le 5 janvier 2007. Art. 2 : s'applique aux quantités d'énergie électrique consommées du 1er janvier au 31 décembre 2007."
  },
  {
    "id": "decret-2012-3413-tva-petroliers",
    "type": "legislation",
    "title": "Décret n° 2012-3413 du 31 décembre 2012, portant réduction à 12 % du taux de la taxe sur la valeur ajoutée sur certains produits pétroliers",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "1",
    "page": "201",
    "issued": {"date-parts": [[2012, 12, 31]]},
    "URL": "https://www.pist.tn/jort/2013/2013F/Jo0012013.pdf",
    "note": "Publié le 1er janvier 2013 (JORT 2013 n° 1). Art. 2 : application du 1er janvier au 31 décembre 2013. Objet enregistré en arabe dans jort_cache.db (recid 79653) : invisible à toute requête française."
  },
  {
    "id": "decret-2012-3414-tva-electricite",
    "type": "legislation",
    "title": "Décret n° 2012-3414 du 31 décembre 2012, portant réduction à 12 % du taux de la taxe sur la valeur ajoutée applicable à l'électricité basse tension à usage domestique et à l'électricité moyenne et basse tension utilisée pour le fonctionnement des équipements de pompage de l'eau destinée à l'irrigation agricole",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "1",
    "page": "202",
    "issued": {"date-parts": [[2012, 12, 31]]},
    "URL": "https://www.pist.tn/jort/2013/2013F/Jo0012013.pdf",
    "note": "Publié le 1er janvier 2013 (JORT 2013 n° 1). Art. 2 : s'applique aux quantités consommées du 1er janvier au 31 décembre 2013. Objet enregistré en arabe (recid 79654)."
  },
  {
    "id": "lf-2015",
    "type": "legislation",
    "title": "Loi n° 2014-59 du 26 décembre 2014, portant loi de finances pour l'année 2015",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "105",
    "volume": "157",
    "page": "3468-3469",
    "issued": {"date-parts": [[2014, 12, 26]]},
    "URL": "https://www.pist.tn/jort/2014/2014F/Jo1052014.pdf",
    "note": "Publié le 30 décembre 2014. Art. 36 : inscription de l'électricité domestique, de l'électricité d'irrigation et des produits pétroliers au tableau B bis (12 %) — fin de la série des décrets annuels."
  },
  {
    "id": "lf-2016-loi-2015-53",
    "type": "legislation",
    "title": "Loi n° 2015-53 du 25 décembre 2015, portant loi de finances pour l'année 2016",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "104",
    "issued": {"date-parts": [[2015, 12, 25]]},
    "URL": "https://www.pist.tn/jort/2015/2015A/Ja1042015.pdf",
    "note": "Publié le 29 décembre 2015. Art. 30 et 31 : élargissement du champ, refonte des tableaux A, B et B bis en tableaux « nouveaux ». ATTENTION : l'édition FRANÇAISE est introuvable sur pist.tn (404 ; pdf_fr NULL dans la base). URL arabe vérifiée (HTTP 200). Texte français consulté via PDFs/Lois_de_Finances/Loi_de_Finances_2016.pdf. Doublon possible avec lf-2016."
  },
  {
    "id": "loi-2016-78-lf-2017",
    "type": "legislation",
    "title": "Loi n° 2016-78 du 17 décembre 2016, portant loi de finances pour l'année 2017",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "105",
    "page": "3829-3900",
    "issued": {"date-parts": [[2016, 12, 17]]},
    "URL": "https://www.pist.tn/jort/2016/2016F/Jo1052016.pdf",
    "note": "Publié le 27 décembre 2016. Art. 24 à 28 « Révision des taux de la TVA », p. 3834-3835 : abrogation du tableau B bis, réécriture du n° 3 du 2e § de l'article 7 (12 %), passage des professions libérales de 6 % à 12 %. Doublon avec lf-2017."
  },
  {
    "id": "loi-2017-66-lf-2018",
    "type": "legislation",
    "title": "Loi n° 2017-66 du 18 décembre 2017, portant loi de finances pour l'année 2018",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "101",
    "page": "4280-4281",
    "issued": {"date-parts": [[2017, 12, 18]]},
    "URL": "https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf",
    "note": "Publié le 19 décembre 2017. Art. 43 : 18 -> 19 %, 6 -> 7 %, 12 -> 13 %, au 1er janvier 2018. Édition arabe : https://www.pist.tn/jort/2017/2017A/Ja1012017.pdf. Doublon avec lf-2018."
  },
  {
    "id": "dgelf-code-tva-2023",
    "type": "book",
    "title": "Code de la taxe sur la valeur ajoutée, loi relative au droit de consommation, leurs textes d'application et textes connexes — mis à jour au 1er janvier 2023",
    "author": [{"literal": "Tunisie. Ministère des finances, Direction générale des études et de la législation fiscales"}],
    "issued": {"date-parts": [[2023]]},
    "note": "Version consolidée officielle, en français, avec chaîne d'annotation des modifications. Copie locale : PDFs-legislation-tunisie/PDFs/TVA/Code_de_la_taxe_sur_la_valeur_ajoutée_2023.pdf. Le millésime 2025 n'existe localement qu'en arabe."
  }
]
```

---

## Annexe B — Notions à porter au glossaire (`precis/glossaire.yml`)

Aucune de ces entrées n'existe dans le glossaire actuel ; seules `assiette-fiscale`, `taux-marginal`,
`taux-effectif-limite-superieure` et `taux-de-liquidation` y figurent, et aucune ne concerne la TVA.

| Terme FR | AR (à valider par un arabophone) | Source canonique |
|---|---|---|
| Taxe sur la valeur ajoutée (TVA) | الأداء على القيمة المضافة | loi n° 88-61 du 2 juin 1988 ; code de la TVA |
| Assujetti | الخاضع للأداء | art. 2 du code de la TVA |
| Option pour la qualité d'assujetti | الاختيار للخضوع للأداء | art. 2 § I-3 du code |
| Fait générateur | الحدث المنشئ للأداء | art. 5 du code |
| Territorialité (« affaire faite en Tunisie ») | مبدأ الإقليمية | art. 3 du code |
| Exonération | الإعفاء | art. 4 et tableau A du code |
| Tableau A (exonérations) | الجدول « أ » | annexe du code |
| Tableau B (taux réduit) | الجدول « ب » | annexe du code ; art. 7 § 1 |
| Tableau B bis | الجدول « ب مكرر » | créé par la LF 2002 (art. 82-84), **abrogé** par la LF 2017 (art. 27-5) — à rédiger au passé |
| Tableau C (taux majoré) | الجدول « ج » | annexe du code ; **supprimé** au 1er janvier 2007 (loi 2006-80, art. 13) |
| Taux normal | النسبة العادية | art. 7 § 1 du code |
| Taux réduit | النسبة المخفضة | art. 7 § 2 du code |
| Taux majoré | النسبة المرتفعة | art. 7 (rédaction 1988-2006) |
| Livraison à soi-même | التسليم للنفس | art. 1er § II-9 et 10 ; art. 5 § 4 du code |
| Commerçant grossiste / détaillant | تاجر جملة / تاجر تفصيل | art. 1er § II-3 du code ; art. 43 de la loi 95-109 |
| Chiffre d'affaires imposable | رقم المعاملات الخاضع | art. 6 du code |
| Droit de consommation | المعلوم على الاستهلاك | loi n° 88-62 du 2 juin 1988 (section propre) ; décret 98-952 pour les produits pétroliers |
| Taxe à la production *(régime antérieur)* | الأداء على الإنتاج | décret du 29 décembre 1955, abrogé par l'art. 2 de la loi 88-61 |
| Taxe sur les prestations de service *(régime antérieur)* | الأداء على الخدمات | décret du 29 décembre 1955, abrogé par l'art. 2 de la loi 88-61 |

*Les entrées « tableau B bis » et « taux majoré » désignent des dispositifs **abrogés** : si le
glossaire ne prévoit pas de statut historique, le signaler dans la définition.*
