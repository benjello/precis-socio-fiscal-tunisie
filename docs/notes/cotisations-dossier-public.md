# Dossier documentaire — Cotisations sociales : secteur public et recouvrement

> Matière documentaire pour le chapitre « Cotisations sociales ». Périmètre : régimes du
> secteur public (CNRPS salariés, CNRPS pensionnés, régimes spéciaux) et recouvrement.
> Les régimes du secteur privé sont traités ailleurs.
>
> **Niveaux d'attestation** utilisés partout ci-dessous :
> `texte lu` — l'article a été lu à l'image ou dans la couche texte du fascicule JORT ;
> `métadonnées` — établi sur `jort_cache.db` ou sur les métadonnées d'`openfisca-tunisia`,
> sans lecture du texte ;
> `dérivé` — déduit d'une règle générale (année de gestion, délai d'entrée en vigueur), non
> énoncé comme tel par le texte.
>
> Travail effectué le 9 septembre 2026. Chaque page citée en `texte lu` a été **ouverte et lue
> en édition française** dans le fascicule. Toutes les URL pist.tn citées dans ce dossier ont
> par ailleurs été testées le 9 septembre 2026 avec `curl -k` (le certificat du site est expiré
> depuis le 25 août 2026) et répondent `200 application/pdf` ; pour les entrées `métadonnées`,
> ce test établit que la ressource existe, **non** que le fascicule servi est bien l'édition
> française ni que le texte s'y trouve à la page annoncée.

---

## Partie 1 — Les régimes du secteur public : création et évolution

### 1.1 Les salariés affiliés à la CNRPS

#### a) L'origine : deux caisses de 1959

**Loi n° 59-18 du 5 février 1959, fixant le régime des pensions civiles et militaires de
retraite.**
JORT n° 8, fascicule daté **3-6 février 1959**, pp. 93-100 (édition française).
URL : <https://www.pist.tn/jort/1959/1959F/Jo00859.pdf>

- *Article premier* — « **Institution de la Caisse Nationale de Retraites.** — La Société de
  Prévoyance des Fonctionnaires et Employés Tunisiens prend l'appellation de Caisse Nationale
  de Retraites. » (p. 93) — **texte lu** (lecture à l'image, PDF p. 11).
- *Art. 5-I* — « Les personnels civils et les militaires régulièrement affiliés à la Caisse
  Nationale de Retraites subissent, au profit de cette Caisse, un prélèvement de **7 %** sur
  la partie de la rémunération qui constitue le traitement de base soumis à retenue pour
  pension. » (p. 93) — **texte lu**.
- *Art. 8* — subvention mensuelle de l'État, des établissements publics, offices et
  municipalités : « Cette subvention est fixée au taux uniforme de **dix pour cent** par an
  des dits traitements et émoluments. » (p. 93) — **texte lu**. C'est la part employeur de
  1959.
- *Art. 52* — « Les dispositions de la présente loi sont applicables aux fonctionnaires et
  militaires ainsi qu'à leurs ayants-droit dont les droits à pension s'ouvriront à compter du
  **1er avril 1959**. » (p. 100) — **texte lu**.
- *Art. 56* — clause de publication ordinaire, sans date d'effet propre pour la retenue de
  l'article 5. Signature : Tunis, 5 février 1959.

> **Point de vigilance.** La loi **ne comporte aucune clause fixant l'effet au 1er février
> 1959**. La seule date qu'elle énonce est le **1er avril 1959** (art. 52), et elle porte sur
> l'ouverture des droits à pension, non sur la retenue. La date `1959-02-01` portée par
> `openfisca-tunisia` est donc **sans appui textuel** ; voir Partie 2.

**Loi n° 59-19 du 5 février 1959, relative à la Caisse Nationale des Retraites.**
JORT n° 8 (même fascicule), pp. 100-101. Même URL.
*Article premier* — « La Caisse Nationale des Retraites constitue un **établissement public**
doté de la personnalité civile et de l'autonomie financière, rattaché au Secrétariat d'État
aux Finances et au Commerce […]. Elle a pour objet d'assurer le service des pensions civiles
et militaires prévues par la loi susvisée n° 59-18 du 5 février 1959. » — **texte lu**
(lecture à l'image, PDF p. 18).

> Les deux lois se répartissent donc les rôles : **59-18 crée l'appellation et le régime**,
> **59-19 donne à la caisse sa personnalité d'établissement public**. C'est cette seconde que
> la loi de finances de 1976 désignera comme le texte instituant la CNR (voir *infra*).

**Loi n° 59-45 du 15 avril 1959, relative à la Caisse de prévoyance sociale.**
JORT n° 22 du 17 avril 1959, p. 368 — **métadonnées** (`jort_cache.db`, recid 118145).
URL : <https://www.pist.tn/jort/1959/1959F/Jo02259.pdf> (non ouverte).

#### b) La création de la CNRPS par voie budgétaire (1975)

**Loi n° 75-83 du 30 décembre 1975, portant loi de finances pour la gestion 1976, art. 28.**
JORT n° 87, fascicule daté **30-31 décembre 1975**, la loi commence p. 2852 ; **l'article 28
est à la page 2854** (édition française).
URL : <https://www.pist.tn/jort/1975/1975F/Jo08775.pdf>

Texte exact, sous la rubrique « *Entreprises Publiques — Transformation du statut juridique
de la Caisse Nationale des Retraites et de la Caisse de Prévoyance Sociale* » :

> « **Art. 28.** — La Caisse Nationale des Retraites et la Caisse de Prévoyance Sociale,
> établissements publics institués respectivement par les lois n° 59-19 du 5 février 1959 et
> n° 59-45 du 15 avril 1959 sont **transformées en un établissement public à caractère
> financier** doté de la personnalité civile et de l'autonomie financière dénommé **Caisse
> Nationale de Retraite et de Prévoyance Sociale (C.N.R.P.S.)**. La Caisse Nationale de
> Retraite et de Prévoyance Sociale est rattachée au Ministère des Finances. Son siège est à
> Tunis. »

**texte lu** (lecture à l'image, PDF p. 4). Les articles 29 à 34 complètent : attributions
(art. 29), organisation fixée par décret (art. 30), transfert des patrimoines des deux caisses
(art. 31), privilège général du Trésor pour le recouvrement des créances (art. 32),
exonérations fiscales (art. 33), dévolution à l'État en cas de dissolution (art. 34).

Trois précisions utiles au rédacteur :

1. La caisse est **créée par une loi de finances**, ce que le titre confirme : la loi 75-83
   est bien la loi de finances **pour la gestion 1976**. Fait établi sur le texte.
2. Le verbe employé est **« transformées en »**, non « instituée » : la CNRPS naît de la
   fusion de deux établissements préexistants, elle n'est pas une création *ex nihilo*.
3. La date de signature est le **30 décembre 1975**. Les fichiers d'`openfisca-tunisia`
   (`salarie_cnrps/index.yaml` et `pensionne_cnrps/index.yaml`) écrivent « 31 décembre 1975 » :
   **correction à porter au modèle**. Ils attribuent par ailleurs la création de la CNR à la
   loi 59-19 — ce que l'article 28 confirme —, mais l'article premier de la loi 59-18 est
   également fondateur : la formulation du précis gagnera à mentionner les deux.

#### c) La refonte du régime (1985) et son évolution

**Loi n° 85-12 du 5 mars 1985, portant régime des pensions civiles et militaires de retraite
et des survivants dans le secteur public.**
JORT n° 20 du **12 mars 1985**, pp. 359-365 (édition française).
URL : <https://www.pist.tn/jort/1985/1985F/Jo02085.pdf>

- *Art. premier* — champ d'application : État, collectivités publiques locales, établissements
  publics à caractère administratif ; établissements publics à caractère industriel et
  commercial et sociétés nationales dont la liste est fixée par décret (p. 359) — **texte lu**.
- *Art. 4* — gestion du régime confiée à la CNRPS (p. 359) — **texte lu**.
- *Art. 8* — le régime est financé par une contribution **à la charge de l'agent et de
  l'organisme employeur** (p. 359) — **texte lu**.
- *Art. 9* — « Le taux de la contribution payée par l'agent à la Caisse Nationale de Retraite
  et de Prévoyance Sociale est fixé à **5 %** de la rémunération prévue par les articles 10, 11
  et 12 de la présente loi. L'employeur est chargé de **prélever mensuellement** cette
  contribution sur la rémunération de l'agent et de la **verser sans délai** à la Caisse
  précitée. Il est interdit à l'employeur de conserver les montants de ces contributions ou de
  les utiliser à une autre fin. » (p. 359) — **texte lu**.
- *Art. 10* — assiette : « les différents éléments **permanents** de la rémunération de
  l'agent qu'ils soient en espèces ou en nature » (p. 359) — **texte lu**.
- *Art. 13* — « Le taux de la contribution payée par l'employeur […] est fixé à **sept pour
  cent (7 %)** de la même rémunération sur la base de laquelle a été retenue la contribution de
  l'agent. » (p. 360) — **texte lu**.
- *Art. 75* — « La présente loi entre en vigueur à l'expiration d'un délai de **six (6) mois**
  à compter de la date de sa publication au Journal Officiel de la République Tunisienne. »
  (p. 365) — **texte lu**.
- *Art. 76* — « Sont abrogées toutes dispositions antérieures, contraires à la présente loi et
  notamment la loi n° 59-18 du 5 février 1959, et tous les textes qui l'ont modifiée ou
  complétée **à l'exception des dispositions relatives à l'invalidité**. » (p. 365) —
  **texte lu**.

> **Conséquence de datation.** Publication le 12 mars 1985 + six mois ⇒ entrée en vigueur le
> **12 septembre 1985** (`dérivé`). Le modèle porte `1985-10-01`, valeur qui n'est énoncée par
> aucun article de la loi. Le palier est de toute façon **neutre sur le taux** : 5 % avant,
> 5 % après. Il s'agit d'une re-consécration du taux dans un texte nouveau, non d'un
> relèvement — le chapitre gagnera à le dire.
>
> La formulation de l'article 76 est « dispositions relatives à l'invalidité », sans référence
> à une « section II ». La rédaction du précis doit reprendre les termes du texte.

**Que sont devenues les dispositions survivantes ?** Elles sont toujours en vigueur et toujours
appliquées vingt-deux ans plus tard : l'article 47 (nouveau) de la loi 85-12, tel qu'il résulte
de l'article 2 de la **loi 2007-43** (p. 2199, **texte lu**), dispose que la maladie incurable ou
l'invalidité permanente d'un orphelin « sont appréciées par **la commission de réforme visée à
l'article 29 de la loi n° 59-18 du 5 février 1959** ». C'est une preuve d'application, non une
modification.

**En revanche, aucun texte postérieur à 1985 modifiant la loi 59-18 n'a été trouvé.** Recherche
menée dans `jort_cache.db` sur 1985-2026, `titre` et `objet`, chaîne non accentuée « 59-18 » →
**zéro résultat** ; doublée par une recherche FTS → mêmes résultats, tous antérieurs à 1985. Les
seuls textes modificatifs identifiés sont **antérieurs** à l'abrogation : décret-loi n° 70-1 du
14 septembre 1970 (JORT n° 43 de 1970, pp. 1186-1187) et loi n° 73-71 du 19 novembre 1973
(voir Partie 2.2), plus le décret n° 77-629 du 3 août 1977 qui **étend** le bénéfice du régime à
certaines catégories (JORT n° 53 de 1977, p. 2114) — les trois en **métadonnées**.
L'affirmation selon laquelle les dispositions survivantes auraient été « modifiées depuis »
**n'est donc pas établie** ; voir « Ce qui n'a pas pu être établi », point 11.

Les modifications ultérieures de la loi 85-12 pertinentes pour les taux sont regroupées en
Partie 2 (paliers 1994, 2002-2006, 2007-2009, 2019-2020) et Partie 3 (art. 9 bis, pénalités).

---

### 1.2 Les pensionnés de la CNRPS : cotiser sur sa pension

Deux prélèvements distincts pèsent sur la pension : la **prévoyance sociale / assurance
maladie** et le **capital décès**. Seul le premier est établi ici sur texte, et seul le texte
de 2007 l'établit sans ambiguïté.

#### a) Le texte qui l'établit sans ambiguïté : le décret de 2007

**Décret n° 2007-1406 du 18 juin 2007, fixant l'assiette de calcul des taux de cotisations dues
au titre du régime de base d'assurance maladie et ses étapes d'application.**
JORT n° 49 du **19 juin 2007**, pp. 2154-2162 (édition française).
URL : <https://www.pist.tn/jort/2007/2007F/Jo0492007.pdf>

- *Art. 2* — « L'assiette des cotisations visée à l'article 1er du présent décret est assise,
  pour les **bénéficiaires de pension**, sur le **montant brut de la pension** fixé
  conformément à la législation en vigueur. » (p. 2156) — **texte lu**.
- *Titre III « Les cotisations des titulaires de pensions », art. 12* — taux cible de **4 %**
  sur l'assiette de l'article 2, appliqué progressivement (p. 2162) — **texte lu**.
- *Art. 13* (chapitre 1er, titulaires de pensions **affiliés à la CNRPS**, au titre du régime
  **obligatoire** de prévoyance sociale) — **texte lu**, p. 2162 :

  | À compter du | Taux |
  |---|---|
  | 1er juillet 2007 | 1 % |
  | 1er juillet 2008 | 2 % |
  | 1er juillet 2009 | 3 % |
  | 1er juillet 2010 | 4 % |

C'est le seul texte lu qui nomme expressément les titulaires de pensions affiliés à la CNRPS,
au titre du régime obligatoire, avec un taux et une date. Il constitue donc **l'ancrage de la
section**.

> **Correction au modèle.** `pensionne_cnrps/prevoyance_sociale.yaml` fait démarrer le 1 % au
> `1959-02-01`. Le décret 2007-1406 le donne comme le taux **à compter du 1er juillet 2007**.
> La date `1959-02-01` est **sans appui textuel**.

#### b) L'antériorité : un texte de 1973 dont la portée n'est pas raccordable

**Décret n° 73-91 du 12 mars 1973, portant organisation des régimes de prévoyance sociale.**
JORT n° 10, fascicule daté **9-13-16 mars 1973**, pp. 355-356 (édition française).
URL : <https://www.pist.tn/jort/1973/1973F/Jo01073.pdf>

- *Art. 14* (chapitre III « Cotisation ») — « La cotisation due par l'assuré ayant opté pour
  les prestations en nature, soit pour le régime de Prévoyance Sociale institué par le décret
  susvisé du 12 avril 1951 est fixée à **1 %** et assise sur les éléments de la rémunération
  soumise à retenues pour pensions. » (p. 356) — **texte lu** (lecture à l'image, PDF p. 6).
- *Art. 15* — cotisation supplémentaire du régime facultatif d'assurance-maladie fixée à 3 % ;
  puis, dans le même article : « **La cotisation due par le retraité et la veuve de retraité
  titulaire d'une pension directe ou de réversion est fixée à 2 % de leur pension en
  principal.** » (p. 356) — **texte lu**.
- *Art. 16* — « La contribution de l'État aux régimes obligatoires des prestations en nature
  et de Prévoyance Sociale est fixée à **1 %** et est assise sur les éléments de la
  rémunération soumise à retenue pour pension. » (p. 356) — **texte lu**. C'est la part
  employeur du 1 % de prévoyance sociale.
- *Art. 17* — abroge notamment l'arrêté du 23 juillet 1952 fixant le taux des contributions au
  régime de prévoyance — **texte lu**.
- *Art. 18* — « […] le présent décret **qui prend effet à compter du 1er avril 1973** » (p. 356)
  — **texte lu**. Signature : Tunis, 12 mars 1973, Hedi Nouira.

> **Ce décret est le seul texte antérieur retrouvé qui fasse cotiser un pensionné sur sa
> pension, et sa portée est incertaine.** Deux réserves, qui vont dans le même sens :
>
> 1. Le paragraphe sur le retraité est **logé dans l'article 15**, entièrement consacré par
>    ailleurs à la cotisation *supplémentaire* du régime **facultatif** d'assurance-maladie.
>    La lecture littérale ne permet pas de trancher seule s'il vaut pour tous les pensionnés
>    ou pour les seuls adhérents au régime facultatif.
> 2. **Le taux ne se raccorde pas à la série.** Le décret de 1973 donne **2 %** au 1er avril
>    1973 ; le décret 2007-1406 donne **1 %** au 1er juillet 2007 pour le régime obligatoire.
>    Un taux qui *baisserait* de 2 % à 1 % en trente-quatre ans n'est pas une lecture plausible
>    d'une même série obligatoire. C'est un argument positif de plus pour rattacher le 2 % de
>    1973 à la branche facultative.
>
> **Conclusion à retenir pour la rédaction :** l'ancrage textuel du prélèvement sur la pension
> est le décret 2007-1406 ; **avant 2007, la case reste vide**. À trancher, le cas échéant, sur
> l'arrêté d'application du même jour (JORT n° 10, pp. 357-358) et sur le décret n° 88-186 du
> 6 février 1988 qui amende le décret 73-91 (JORT n° 14 du 23 février 1988, pp. 284-285 —
> **métadonnées**).

**Capital décès des pensionnés — non établi sur texte.**
Le modèle porte 0,5 % depuis le 1er juin 1974, référencé au décret n° 74-572 du 22 mai 1974
relatif au capital-décès (JORT n° 36 du 24 mai 1974, pp. 1108-1109) et au décret n° 93-308 du
1er février 1993 relatif au régime du capital décès (JORT n° 13 du 16 février 1993,
pp. 246-247) — **métadonnées** (`jort_cache.db`, recids 102263 et 92069). Les articles n'ont pas
été lus. URL : <https://www.pist.tn/jort/1974/1974F/Jo03674.pdf> et
<https://www.pist.tn/jort/1993/1993F/Jo01393.pdf>. Voir « Ce qui n'a pas pu être établi ».

---

### 1.3 Le régime spécial des membres du gouvernement, des députés et des gouverneurs

Ce n'est pas **un** régime mais **trois régimes parallèles**, portés par trois lois de
structure identique — même article 5, mêmes taux, même caisse.

| Régime | Texte | JORT | Page (éd. fr.) | Attestation |
|---|---|---|---|---|
| Membres du gouvernement | Loi n° **83-31** du 17 mars 1983 | n° 23 du 25 mars 1983 | 808-809 | art. 5 **texte lu** |
| Députés | Loi n° **85-16** du 8 mars 1985 | n° 21 du 15 mars 1985 | 375-377 | art. 5 **texte lu** |
| Gouverneurs | Loi n° **88-16** du 17 mars 1988 | n° 20 du 22 mars 1988 | 427 | art. 5 **texte lu** |

URL : <https://www.pist.tn/jort/1983/1983F/Jo02383.pdf> ;
<https://www.pist.tn/jort/1985/1985F/Jo02185.pdf> ;
<https://www.pist.tn/jort/1988/1988F/Jo02088.pdf>

**Loi 83-31, art. 5** (texte lu) : « La rémunération du Membre du Gouvernement est soumise à
retenue pour pension, égale à **10 %**, au profit de la Caisse Nationale de Retraite et de
Prévoyance Sociale qui bénéficie en outre d'une **contribution de l'État égale à 15 %** de la
rémunération d'activité prélevée sur le budget du département ministériel concerné. Ces
montants sont payés jusqu'à la cessation du bénéfice de la rémunération de Membre du
Gouvernement. »

**Loi 88-16, art. 5** (texte lu) : « Les éléments permanents de la rémunération des gouverneurs
sont soumis à une retenue pour pension de retraite égale à **10 %** au profit de la caisse
nationale de retraite et de prévoyance sociale qui bénéficie en outre d'une contribution de
l'État égale à **15 %** de ces mêmes éléments. »

**Loi 85-16, art. 5** (texte lu) : les indemnités parlementaires permanentes sont soumises à une
retenue « égale à **10 %** au profit de la Caisse Nationale de Retraite et de Prévoyance
Sociale » ; la contribution de l'État est mentionnée à l'article 5 également, le libellé exact
restant à relire à l'image (l'OCR est partiel sur ce point).

**Structure à retenir pour la rédaction.** Ces trois articles 5 sont ensuite **modifiés en bloc,
et par les mêmes textes que le régime général du secteur public** : la loi 94-71 (art. unique),
l'article 85 de la loi de finances 2002 et l'article premier de la loi 2007-43 énumèrent tous
trois, dans leur clause « en conséquence, sont modifiés les taux des contributions prévus par
les lois ci-après », l'article 5 de la loi 83-31, les articles 9 et 13 de la loi 85-12,
l'article 5 de la loi 85-16 et l'article 5 de la loi 88-16 (**texte lu** dans les trois cas ;
voir Partie 2). C'est pourquoi les taux des régimes spéciaux suivent la même trajectoire que
ceux de la CNRPS, avec un point de départ plus élevé (10 % / 15 % au lieu de 5 % / 7 %).

Deux corrections au modèle :

- `regimes_speciaux/.../index.yaml` ne cite que la loi 83-31 ; **les lois 85-16 et 88-16
  manquent** dans la documentation.
- Le titre arabe de la loi 88-16 dans `cotisations_salarie/retraite` la date de **1983**
  (« المؤرخ في 17 مارس 1983 ») alors qu'elle est du **17 mars 1988**.
- La loi n° **2005-54 du 18 juillet 2005**, étendant les régimes spéciaux applicables aux
  membres de la chambre des députés aux membres de la chambre des conseillers (JORT n° 57 du
  19 juillet 2005, p. 1749 — **métadonnées**), n'apparaît nulle part dans le modèle. Elle
  explique que la loi 2007-43 vise « la chambre des conseillers ».
  URL : <https://www.pist.tn/jort/2005/2005F/Jo0572005.pdf>

---

## Partie 2 — La série des taux de retraite CNRPS, 1959-2020 : les références JORT

### 2.1 Réponse à la question posée : l'échéancier est bien pluriannuel

**Tranché sur pièce, et par la lecture des deux articles.** Les quatre paliers réputés
« manquants » — 2003, 2004, 2008, 2009 — **ne correspondent à aucun texte distinct**. Ils sont
programmés à l'avance, dans un article unique, par les deux lois déjà identifiées :

- **Loi n° 2001-123 du 28 décembre 2001, LF 2002, art. 85** (p. 4260, **texte lu**) :

  > « Les taux de la contribution au régime des pensions civiles et militaires de retraite et
  > des survivants dans le secteur public et des régimes de retraite des membres du
  > gouvernement, des députés et des gouverneurs sont relevés comme suit :
  > — de **1 %** de la base de calcul de la contribution **à la charge de l'assuré social** et
  > ce comme suit : 0,50 % à partir du 1er juillet 2002 ; 0,25 % à partir du 1er juillet 2003 ;
  > 0,25 % à partir du 1er juillet 2004 ;
  > — de **1,5 %** de la base de calcul de la contribution **à la charge de l'employeur** et ce
  > comme suit : 0,50 % à partir du 1er juillet 2002 ; 0,25 % à partir du 1er juillet 2003 ;
  > 0,25 % à partir du 1er juillet 2004 ; 0,25 % à partir du 1er juillet 2005 ; 0,25 % à partir
  > du 1er juillet 2006.
  > En conséquence, sont modifiés les taux des contributions prévus par les lois ci-après :
  > l'article 5 de la loi n° 83-31 du 17 mars 1983 […] ; les articles 9 et 13 de la loi n° 85-12
  > du 5 mars 1985 […] ; l'article 5 de la loi n° 85-16 du 8 mars 1985 […] ; l'article 5 de la
  > loi n° 88-16 du 17 mars 1988 […] ; l'article unique de la loi n° 94-71 du 27 juin 1994 […]. »

- **Loi n° 2007-43 du 25 juin 2007, article premier** (p. 2198, **texte lu**) : relèvement de
  **1,8 %** à la charge de l'employeur (0,60 % au 1er **janvier** 2007, 2008 et 2009) et de
  **1,2 %** à la charge de l'assuré social (0,40 % au 1er **juillet** 2007, 2008 et 2009), avec
  la même clause « en conséquence » visant les quatre articles 5 / 9 et 13.

Les deux échéanciers reconstituent exactement la série publiée. Le taux salarié est de
**6 %** depuis le 1er juillet 1994 (loi 94-71) ; l'échéancier de 2001 le porte à
**6,5 %** (1/7/2002), **6,75 %** (1/7/2003) puis **7 %** (1/7/2004), et celui de 2007 à
**7,4 %** (1/7/2007), **7,8 %** (1/7/2008) puis **8,2 %** (1/7/2009).

**Il n'y a donc rien à trouver de plus : il y a un article à citer.** La formule du chapitre
(« le texte qui fixe chaque palier n'a pas été établi ») peut être remplacée par la citation de
l'article 85 de la LF 2002 et de l'article premier de la loi 2007-43.

### 2.2 Table de référence, palier par palier (part salarié)

| Effet | Taux | Texte | Signature | Publication JORT | Page (éd. fr.) | URL pist.tn | Attestation |
|---|---|---|---|---|---|---|---|
| voir note ¹ | 7 % | Loi n° 59-18, **art. 5-I** | 5 févr. 1959 | n° 8, fasc. 3-6 févr. 1959 | 93 | `/jort/1959/1959F/Jo00859.pdf` | **texte lu** |
| gestion 1975 ² | 5 % | Loi n° 74-101 (LF 1975), **art. 38** | 25 déc. 1974 | n° 80 du 31 déc. 1974 | 2917 | `/jort/1974/1974F/Jo08074.pdf` | **texte lu** |
| 12 sept. 1985 ³ | 5 % | Loi n° 85-12, **art. 9** (effet : art. 75) | 5 mars 1985 | n° 20 du 12 mars 1985 | 359 (art. 75 : 365) | `/jort/1985/1985F/Jo02085.pdf` | **texte lu** |
| 1er juill. 1994 | 6 % | Loi n° 94-71, **art. unique** | 27 juin 1994 | n° 50 du 28 juin 1994 | 1086 | `/jort/1994/1994F/Jo05094.pdf` | **texte lu** |
| 1er juill. 2002 | 6,5 % | Loi n° 2001-123 (LF 2002), **art. 85** | 28 déc. 2001 | n° 104 du 28 déc. 2001 | 4260 | `/jort/2001/2001F/Jo1042001.pdf` | **texte lu** |
| 1er juill. 2003 | 6,75 % | *idem*, art. 85 (échéancier) | " | " | 4260 | *idem* | **texte lu** |
| 1er juill. 2004 | 7 % | *idem*, art. 85 (échéancier) | " | " | 4260 | *idem* | **texte lu** |
| 1er juill. 2007 | 7,4 % | Loi n° 2007-43, **art. premier** | 25 juin 2007 | n° 51 du 26 juin 2007 | 2198 | `/jort/2007/2007F/Jo0512007.pdf` | **texte lu** |
| 1er juill. 2008 | 7,8 % | *idem*, art. premier (échéancier) | " | " | 2198 | *idem* | **texte lu** |
| 1er juill. 2009 | 8,2 % | *idem*, art. premier (échéancier) | " | " | 2198 | *idem* | **texte lu** |
| ~~1er juin 2019~~ ⁴ | ~~8,7 %~~ | **Aucun appui textuel pour la part salarié.** La loi n° 2019-37, art. 4, place la totalité du +1 point au 1er janvier 2020 ; la date du 1er juin 2019 porte le **+2 points employeur** | 30 avr. 2019 | n° 35 du 30 avr. 2019 | 1314 | `/jort/2019/2019F/Jo0352019.pdf` | **contredit par le texte** |
| 1er janv. 2020 ⁴ | 9,2 % | Loi n° 2019-37, **art. 4** | 30 avr. 2019 | n° 35 du 30 avr. 2019 | 1314 | `/jort/2019/2019F/Jo0352019.pdf` | **texte lu** |

Toutes les URL sont à préfixer par `https://www.pist.tn`. Les douze lignes correspondent
exactement aux douze millésimes publiés par le chapitre, la onzième étant conservée pour la
correspondance ligne à ligne bien qu'elle soit à supprimer.

**Un mouvement absent de la série, et qui n'est pas un palier de taux :** la loi n° 73-71 du
19 novembre 1973 remplace l'article 5 de la loi 59-18 **en maintenant le taux à 7 %** et en
élargissant l'assiette (voir note ² ci-dessous). Le chapitre gagnera à le mentionner en une
phrase : la série des taux est plate de 1959 à 1974, l'assiette ne l'est pas.

**¹ La date d'effet du 7 % n'est pas établie.** Voir 1.1 a) : la loi 59-18 ne comporte aucune
clause d'effet pour l'article 5. La seule date énoncée, 1er avril 1959 (art. 52), porte sur
l'ouverture des droits à pension. Le « 1er février 1959 » du modèle et du chapitre est
**invérifié**. Case honnêtement vide : *effet non énoncé par le texte ; publication au JORT du
3-6 février 1959*.

**² La date du 1er janvier 1975 est `dérivé`.** L'article 38 de la LF 1975 est ainsi rédigé
(p. 2917, **texte lu**) :

> « **Art. 38.** — L'article 5 de la loi n° 59-18 du 5 février 1959 fixant le régime des
> pensions civiles et militaires de retraite tel qu'il a été modifié par l'article 1er de la loi
> n° 73-71 du 19 novembre 1973, est abrogé et remplacé par les dispositions suivantes :
> ***Article 5 (nouveau)*** — I. Les personnels civils et militaires affiliés à la Caisse
> Nationale des Retraites subissent au profit de cette Caisse un prélèvement de **5 %** sur les
> émoluments globaux indiciaires ainsi que sur les indemnités et primes entrant en compte dans
> le calcul de la pension […]. Cependant, pour les traitements, indemnités et compléments de
> cherté de vie compris, ne dépassant pas ceux afférents à l'indice 250, le montant de ce
> prélèvement ne doit en aucun cas être supérieur à celui pratiqué, à indice égal, conformément
> aux dispositions antérieures. »

L'article ne porte **aucune date d'effet** ; le 1er janvier 1975 se déduit du rattachement à la
gestion 1975. Deux enseignements pour le chapitre : (a) la baisse s'accompagne d'un
**élargissement de l'assiette** (émoluments globaux indiciaires + primes, au lieu du seul
traitement de base), ce qui interdit de lire « 7 % → 5 % » comme une baisse nette du
prélèvement ; (b) un texte intermédiaire s'intercale entre 1959 et 1975 — la **loi
n° 73-71 du 19 novembre 1973**, citée par l'article 38 lui-même, et **lue** (voir ci-dessous).

**Le maillon de 1973, lu et refermé.** **Loi n° 73-71 du 19 novembre 1973, portant modification
de la loi n° 59-18 du 5 février 1959, fixant le régime des pensions civiles et militaires de
retraite**, JORT n° 43, fascicule daté **16-20-23-27 novembre 1973**, pp. 1852-1853 (édition
française), URL <https://www.pist.tn/jort/1973/1973F/Jo04373.pdf>. Son *article premier* abroge
et remplace l'article 5 de la loi 59-18 (p. 1852, **texte lu**, lecture à l'image) :

> « ***Article 5 (nouveau).*** — I. — Les personnels civils et militaires affiliés à la Caisse
> Nationale des Retraites subissent au profit de cette caisse un prélèvement de **7 %** sur la
> partie de la rémunération qui constitue le traitement de base ainsi que sur les indemnités et
> primes entrant en compte dans le calcul de la pension et prévues à l'article 22 de la présente
> loi. »

**Le taux reste donc à 7 % ; c'est l'assiette qui s'élargit** (traitement de base *plus*
indemnités et primes). Il n'y a **aucun palier de taux manquant entre 1959 et 1974** : la série
est continue à 7 % sur quinze ans, et les deux mouvements de 1973 et 1975 portent l'un sur
l'assiette seule, l'autre sur le taux et l'assiette ensemble. La loi 73-71 ne comporte pas de
clause d'effet (elle se clôt sur la formule ordinaire de publication) ; sa signature est datée
du **19 novembre 1973** dans le fascicule, là où `jort_cache.db` porte le 16 novembre — le
fascicule fait foi. Un rectificatif a été publié au JORT n° 47 de 1973, p. 2127
(**métadonnées**). Elle modifie également les articles 9, 11, 20, 21, 22 et 25 de la loi 59-18.

L'article suivant de la LF 1975, **art. 39** (p. 2918, **texte lu**), traite la part employeur : « Le deuxième
alinéa de l'article 8 de la loi visée n° 59-18 du 5 février 1959 […] est abrogé et remplacé par
la disposition suivante : *Cette subvention est fixée au taux uniforme de **7 %** par an sur les
éléments de rémunération sur lesquels l'affilié supporte la dite retenue.* » — c'est le passage
de 10 % à 7 % côté employeur.

**³ Le palier de 1985 est neutre et mal daté dans le modèle.** Voir 1.1 c) : entrée en vigueur
au 12 septembre 1985 (`dérivé` de l'art. 75), non au 1er octobre ; et 5 % avant comme après.

**⁴ Le palier « 1er juin 2019 → 8,7 % » n'existe pas pour la part salarié.** L'article 4 de la
loi 2019-37 est sans ambiguïté (p. 1314, **texte lu**) :

> « **Art. 4** — Les taux des contributions dues au titre de la retraite définis aux articles 9
> et 13 de la loi 85-12 du 5 mars 1985 susmentionnée, sont majorés de **3 %** comme suit :
> **Au titre de l'employeur** : — **2 %** à partir du premier jour du mois qui suit la date
> d'entrée en vigueur de la présente loi.
> **Au titre de l'agent** : — **1 %** à partir du **premier janvier 2020**. »

La majoration de la part salarié est donc de **un point en une seule fois au 1er janvier 2020**
(8,2 % → 9,2 %), et non de deux demi-points en juin 2019 puis janvier 2020. Le fractionnement
0,5 / 0,5 que porte `salarie_cnrps/cotisations_salarie/retraite.yaml` (`2019-06-01: 0.087`)
est **contredit par le texte**. La date de juin 2019 vaut pour la **part employeur** (12,5 % → 14,5 %),
et elle-même n'est pas énoncée : la loi ne comporte **aucune clause d'entrée en vigueur**, elle
se clôt sur la formule ordinaire « sera publiée au Journal Officiel […] et exécutée comme loi de
l'État ». Le « 1er juin 2019 » suppose donc une entrée en vigueur intervenue **avant le
1er juin**, ce qui est compatible avec le droit commun de la publication mais **n'a pas été
vérifié sur texte** : la règle de droit commun applicable (délai courant à compter de la
publication au JORT) n'a pas été identifiée ni citée dans ce dossier. À traiter comme `dérivé`,
et à ne pas présenter comme une date énoncée par la loi.

C'est la correction la plus lourde de conséquence du dossier : elle touche à la fois le tableau
publié (`tbl-cnrps-retraite`), le paramètre du modèle et le récit du chapitre.

### 2.3 Part employeur — pour mémoire, et deux anomalies

| Effet | Taux | Texte | Attestation |
|---|---|---|---|
| 1959 | 10 % | Loi 59-18, art. 8 | **texte lu** (p. 93) |
| gestion 1975 | 7 % | Loi 74-101 (LF 1975), art. 39 | **texte lu** (p. 2918) |
| 12 sept. 1985 | 7 % | Loi 85-12, art. 13 | **texte lu** (p. 360) |
| 1er juill. 1995 | 8,2 % | Loi 94-71, art. unique (« de 1,2 % […] à la charge de l'employeur et ce à partir du premier juillet **1995** ») | **texte lu** (p. 1086) |
| 1/7/2002 → 1/7/2006 | 8,7 → 9,7 % | LF 2002, art. 85 (cinq marches de 0,50 / 0,25 / 0,25 / 0,25 / 0,25) | **texte lu** |
| 1/1/2007, 1/1/2008, 1/1/2009 | +0,60 chacun | Loi 2007-43, art. premier | **texte lu** |
| 1er juill. 2011 | 12,5 % | Décret-loi n° 2011-48 du 4 juin 2011, JORT n° 41 du 7 juin 2011, p. 844 | **métadonnées** |
| 1er juin 2019 | 14,5 % | Loi 2019-37, art. 4 | **texte lu** (date `dérivé`) |

Deux anomalies du modèle à signaler :

1. `cotisations_employeur/retraite.yaml` place le palier de 2008 au **1er juillet** 2008, alors
   que la note qu'il cite lui-même et le texte de la loi 2007-43 disent **1er janvier** 2008.
   Le décalage vaut aussi pour 2007 et 2009, correctement datés en janvier, ce qui rend
   l'incohérence interne.
2. Le décret-loi 2011-48 est cité sans que son contenu ait été lu ; le palier employeur de
   juillet 2011 (11,5 % → 12,5 %) reste `métadonnées`.
   URL : <https://www.pist.tn/jort/2011/2011F/Jo0412011.pdf>

---

## Partie 3 — Le recouvrement

Le recouvrement n'obéit pas au même instrument dans les deux secteurs, et la dissymétrie mérite
d'être écrite plutôt qu'aplanie : **au privé, une déclaration trimestrielle avec versement à
échéance ; au public, un précompte mensuel opéré par l'employeur public lui-même.**

### 3.1 CNSS — périodicité, déclaration, pénalités

Tout part de la **loi n° 60-30 du 14 décembre 1960, relative à l'organisation des régimes de
sécurité sociale**, JORT n° 57, fascicule daté **13-16 décembre 1960**, pp. 1602-1613 (édition
française). URL : <https://www.pist.tn/jort/1960/1960F/Jo05760.pdf>

- **Périodicité — art. 45** (p. 1606, **texte lu**) : « Le montant des cotisations des
  travailleurs et des employeurs est dû par ceux-ci, **à la fin de chaque trimestre**. Les
  cotisations dues pour le trimestre écoulé doivent être versées, par l'employeur, **au plus
  tard le quinzième jour du mois suivant** ce trimestre. »
- **Déclaration — art. 46** (p. 1606, **texte lu**) : « En même temps qu'il verse les
  cotisations et, au plus tard, le quinzième jour du mois suivant le trimestre échu,
  l'employeur doit faire parvenir à la Caisse Nationale, une **déclaration trimestrielle de
  salaires justificative des cotisations dues**. » L'article précise que la déclaration doit
  couvrir toutes les sommes versées au personnel énumérées à l'article 42, « que ces sommes
  soient effectivement versées ou soient le résultat d'une évaluation », « à toutes personnes
  effectuant un travail à titre habituel ou occasionnel, à forfait, au temps, ou à la tâche,
  dans les locaux de l'entreprise, ou à domicile ». Sont réputées **nulles** les déclarations
  qui ne comprennent pas l'intégralité des salaires payés, ou qui font mention de salaires
  inférieurs aux salaires minimums réglementaires.
- **Justification — art. 47** (p. 1606, **texte lu**) : l'employeur doit prouver, chaque fois
  qu'il en est requis, la conformité de ses déclarations de salaires aux feuilles de paie et à
  tous documents et registres comptables.
- **Taxation d'office — art. 104** (p. 1611, **texte lu**) : quatre cas, dont l'employeur qui a
  fourni ses déclarations sans y joindre ses cotisations, et celui qui a omis de déclarer
  l'intégralité des salaires.
- **Pénalités, version d'origine — art. 105** (p. 1611, **texte lu**) : l'employeur qui, « au
  terme de la première quinzaine suivant l'expiration du trimestre », n'a pas fait parvenir sa
  déclaration ni joint ses cotisations, est mis en demeure par lettre recommandée avec accusé
  de réception ; faute de régularisation dans les **quinze jours**, la Caisse procède à une
  taxation d'office sur les bases de l'article 104, « majoré, à titre de pénalité, de **trois
  pour mille par jour de retard**, à partir de la date de l'échéance trimestrielle, à
  concurrence de **90 jours de retard au maximum** ». Le montant est mis en recouvrement par
  **état de liquidation** décerné par le président-directeur général de la Caisse.
- **Remise gracieuse — art. 107** (p. 1611, **texte lu**) : la remise des pénalités des articles
  105 et 106 ne peut être accordée que par décision du ministre chargé des affaires sociales,
  après avis des contrôleurs technique et financier, et **pour motifs d'intérêt général**.
- **Prescription — art. 110** (p. 1611, **texte lu**) : les actions de la Caisse contre les
  affiliés pour non-paiement de cotisations se prescrivent **par un an**, la prescription
  courant « du premier jour du trimestre suivant celui auquel les cotisations se rapportent ».
- **Privilège — art. 116** (p. 1611, **texte lu**) : les créances de la Caisse à l'égard des
  employeurs bénéficient du **privilège général du Trésor**.

**Loi n° 2007-51 du 23 juillet 2007, modifiant et complétant la loi n° 60-30.**
JORT n° 60 du **27 juillet 2007**, p. 2581 (édition française) — **texte lu**.
URL : <https://www.pist.tn/jort/2007/2007F/Jo0602007.pdf>

C'est le texte qui donne au recouvrement CNSS sa physionomie actuelle. Il tient en deux
articles :

- *Art. premier* — remplace le premier paragraphe de l'article 105 :
  > « Toute cotisation ou fraction de cotisation, non payée à sa date d'exigibilité par un
  > employeur affilié, est majorée d'une **pénalité de retard pour non-paiement des cotisations
  > exigibles égale à 1 % pour chaque mois de retard ou fraction de mois** si l'employeur a
  > volontairement déclaré la totalité des salaires payés. En cas de **non-déclaration de la
  > totalité des salaires** payés à sa date d'exigibilité, s'applique **en sus** des pénalités
  > de retard pour non-paiement une **pénalité de retard pour non-déclaration des salaires égale
  > à 0,5 % du montant des cotisations exigibles pour chaque mois de retard ou fraction de
  > mois**. »
- *Art. 2* — ajoute un troisième paragraphe à l'article 45 :
  > « Les montants des cotisations prévues par le présent article **peuvent être versées
  > mensuellement par les employeurs**. »

> **C'est l'argument textuel exact du « réputé trimestriel » du chapitre.** La périodicité de
> principe reste celle de l'article 45 alinéa 1 — trimestrielle, exigible à la fin du trimestre,
> payable au plus tard le 15 du mois suivant — et le versement mensuel n'est, depuis 2007,
> qu'une **faculté** ouverte à l'employeur. Le régime de pénalités passe pour sa part d'une
> logique journalière plafonnée (3 ‰ / jour, 90 jours maximum) à une logique mensuelle non
> plafonnée (1 % / mois), avec une pénalité **additionnelle** de 0,5 % qui sanctionne
> spécifiquement la sous-déclaration : c'est la déclaration, autant que le paiement, qui est
> sanctionnée.

**Les remises de pénalités sont une pratique périodique**, ce que le chapitre peut mentionner en
une phrase sans s'y étendre : arrêté du 27 avril 1985 (JORT n° 37, p. 702), arrêté du
30 août 1988 (JORT n° 59, p. 1234), décret n° 2007-1507 du 25 juin 2007 (JORT n° 52,
pp. 2254-2255), décret n° 2008-87 du 8 janvier 2008 (JORT n° 5, pp. 385-386), décret-loi
n° 2011-67 du 14 juillet 2011 (JORT n° 52, pp. 1244-1245), décret n° 2014-2919 du 15 août 2014
(JORT n° 67, pp. 2073-2074), décret gouvernemental n° 2016-567 du 2 mai 2016 (JORT n° 39,
pp. 1551-1553), décret-loi n° 2022-6 du 26 janvier 2022 (JORT n° 11, pp. 279-280), décret
n° 2024-503 du 24 octobre 2024 (JORT n° 130, p. 5310), décret n° 2025-259 du 22 mai 2025
(JORT n° 60, p. 1289) — **métadonnées** pour tous, sauf le **décret 2014-2919, texte lu**, qui
confirme la maille trimestrielle : la remise porte sur les pénalités dues « **au titre des
trimestres écoulés et dans la limite du deuxième trimestre de l'année 2014** », et vise
expressément les « pénalités de retard exigées pour **non-déclaration de la totalité des
salaires** ».

### 3.2 CNRPS — précompte mensuel et pénalités de 2019

Le mécanisme est différent : l'employeur public **retient sur le traitement** et **reverse**,
sans déclaration trimestrielle intermédiaire.

- **Loi n° 85-12, art. 9** (p. 359, **texte lu**) : « L'employeur est chargé de **prélever
  mensuellement** cette contribution sur la rémunération de l'agent et de la **verser sans
  délai** à la Caisse précitée. Il est interdit à l'employeur de conserver les montants de ces
  contributions ou de les utiliser à une autre fin. » La rédaction de 1985 ne fixe **ni délai
  chiffré, ni sanction**.
- **Loi n° 2019-37, art. 3, insérant un article 9 bis à la loi 85-12** (p. 1313, **texte lu**) —
  c'est le texte qui comble ce vide :
  > « **Article 9 bis** : Des pénalités de retard sont encourues par l'État, les collectivités
  > locales, les établissements publics à caractère administratif, les établissements publics à
  > caractère non administratif, les entreprises nationales, les instances constitutionnelles
  > indépendantes et les instances publiques mentionnés à l'article premier de la présente loi,
  > **au cas où l'employeur ne procède pas mensuellement à la retenue de la cotisation sur le
  > salaire mensuel de l'agent et à son transfert à la Caisse nationale de retraite et de
  > prévoyance sociale dans un délai n'excédant pas le cinquième jour du mois suivant**.
  > Les pénalités de retards sont égales au taux de **1,5 % pour chaque mois de retard ou pour
  > chaque fraction de mois**, et sont calculées sur la base du montant des cotisations dues ou
  > sur la base d'une fraction de ce montant.
  > Le recouvrement des montants dus au titre de ces pénalités intervient conformément à la
  > législation et à la réglementation en vigueur. »

  Deux traits notables : le **débiteur de la pénalité est l'État lui-même** (et les autres
  personnes publiques employeuses), et le **taux de 1,5 % par mois est supérieur de moitié au
  taux de 1 % du secteur privé** issu de la loi 2007-51.

- **Déclaration employeur — loi 2019-37, art. 3, articles 71 quinquies et 71 sexies**
  (p. 1314, **texte lu**) : la CNRPS « doit disposer d'un système d'informations propre au suivi
  de la vie professionnelle des affiliés et à la tenue de leurs comptes individuels, basé sur
  **l'échange automatique et instantané des données entre la Caisse et l'employeur lors de la
  déclaration des cotisations et des retenues dues à la Caisse** » ; l'échange « doit avoir lieu
  **mensuellement** et d'une manière régulière **lors du paiement des salaires et des
  traitements**, par le biais de registres informatisés ». L'article 71 sexies impose à
  l'employeur, avant transfert, de s'assurer de « la stricte concordance entre les montants
  globaux des cotisations et des retenues inclus dans les décomptes extensifs et le total des
  montants inclus dans ces registres ». Les modalités d'application sont renvoyées à un décret
  gouvernemental — **non identifié à ce jour** (voir *infra*).

> **Formule d'articulation pour le chapitre.** Au privé, la déclaration trimestrielle de
> salaires est le titre du recouvrement : elle précède et justifie le versement, et sa carence
> ouvre la taxation d'office. Au public, il n'y a pas de titre déclaratif équivalent avant 2019 :
> la retenue est opérée sur le traitement et reversée, l'employeur étant lui-même une personne
> publique. La loi de 2019 rapproche les deux logiques en instaurant une déclaration mensuelle
> dématérialisée et en assortissant le retard d'une pénalité — jusque-là, l'obligation de
> l'article 9 était dépourvue de sanction chiffrée.

---

## Références candidates (CSL-JSON)

### Déjà présentes

| `citation-key` | Où | Remarque |
|---|---|---|
| `loi85-12` | `precis/fr/cotisations_sociales/references.json`, `precis/fr/remunerations_publiques/references.json` | **À compléter** : pas de `container-title`, ni `issue`, ni `page`. Ajouter JORT n° 20 du 12 mars 1985, pp. 359-365. |
| `loi60-30` | `precis/fr/references.json` | **À corriger** : la note porte « JORT n° 57 des **16-20** décembre 1960 ». Le fascicule lu porte en en-tête de page « **13-16 Décembre 1960** », et `jort_cache.db` donne `date_publication = 1960-12-13`. |
| `loi75-83` | `precis/fr/prestations_sociales/references.json` | **À enrichir** : la note dit « le contenu de l'article instituant la caisse n'a pas été lu ». Il l'est désormais : art. 28, p. 2854. |
| `loi2019-37` | `precis/fr/remunerations_publiques/references.json` | À réutiliser tel quel dans le livre Cotisations. |
| `loi2004-71` | `precis/fr/references.json` | Utile en renvoi (assurance maladie). |

### À créer

```json
{
  "id": "loi59-18",
  "type": "legislation",
  "title": "Loi n° 59-18 du 5 février 1959, fixant le régime des pensions civiles et militaires de retraite",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "8",
  "page": "93-100",
  "issued": {"date-parts": [[1959, 2, 5]]},
  "URL": "https://www.pist.tn/jort/1959/1959F/Jo00859.pdf",
  "note": "citation-key: loi59-18\nJORT n° 8, fascicule daté 3-6 février 1959, pp. 93-100 (édition française). Art. premier : la Société de Prévoyance des Fonctionnaires et Employés Tunisiens prend l'appellation de Caisse Nationale de Retraites. Art. 5-I : prélèvement de 7 %. Art. 8 : subvention de l'État au taux uniforme de 10 %. Art. 52 : application aux droits à pension s'ouvrant à compter du 1er avril 1959 ; aucune clause d'effet pour l'art. 5. Abrogée par la loi 85-12, art. 76, à l'exception des dispositions relatives à l'invalidité. Texte lu à l'image."
}
```

```json
{
  "id": "loi59-19",
  "type": "legislation",
  "title": "Loi n° 59-19 du 5 février 1959, relative à la Caisse nationale des retraites",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "8",
  "page": "100-101",
  "issued": {"date-parts": [[1959, 2, 5]]},
  "URL": "https://www.pist.tn/jort/1959/1959F/Jo00859.pdf",
  "note": "citation-key: loi59-19\nMême fascicule que la loi 59-18. Article premier : la CNR constitue un établissement public doté de la personnalité civile et de l'autonomie financière, rattaché au Secrétariat d'État aux Finances et au Commerce. Texte lu à l'image."
}
```

```json
{
  "id": "loi59-45",
  "type": "legislation",
  "title": "Loi n° 59-45 du 15 avril 1959, relative à la Caisse de prévoyance sociale",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "22",
  "page": "368",
  "issued": {"date-parts": [[1959, 4, 15]]},
  "URL": "https://www.pist.tn/jort/1959/1959F/Jo02259.pdf",
  "note": "citation-key: loi59-45\nJORT n° 22 du 17 avril 1959, p. 368. Seconde des deux caisses fusionnées en 1975 pour former la CNRPS. Métadonnées jort_cache.db (recid 118145) ; contenu non lu."
}
```

```json
{
  "id": "loi74-101-lf1975",
  "type": "legislation",
  "title": "Loi n° 74-101 du 25 décembre 1974, portant loi de finances pour la gestion 1975",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "80",
  "page": "2913-2934",
  "issued": {"date-parts": [[1974, 12, 25]]},
  "URL": "https://www.pist.tn/jort/1974/1974F/Jo08074.pdf",
  "note": "citation-key: loi74-101-lf1975\nJORT n° 80 du 31 décembre 1974. Art. 38, p. 2917 : remplace l'art. 5 de la loi 59-18 ; prélèvement ramené à 5 % mais assiette élargie aux émoluments globaux indiciaires, primes et indemnités. Art. 39, p. 2918 : subvention de l'employeur ramenée de 10 % à 7 %. Aucune date d'effet énoncée ; le 1er janvier 1975 est dérivé du rattachement à la gestion. Articles 38 et 39 lus à l'image."
}
```

```json
{
  "id": "loi73-71",
  "type": "legislation",
  "title": "Loi n° 73-71 du 19 novembre 1973, portant modification de la loi n° 59-18 du 5 février 1959, fixant le régime des pensions civiles et militaires de retraite",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "43",
  "page": "1852-1853",
  "issued": {"date-parts": [[1973, 11, 19]]},
  "URL": "https://www.pist.tn/jort/1973/1973F/Jo04373.pdf",
  "note": "citation-key: loi73-71\nJORT n° 43, fascicule daté 16-20-23-27 novembre 1973, pp. 1852-1853 (édition française). Article premier : remplace l'art. 5 de la loi 59-18 — le prélèvement reste à 7 % mais l'assiette s'élargit du seul traitement de base aux indemnités et primes entrant dans le calcul de la pension. Modifie aussi les art. 9, 11, 20, 21, 22 et 25. Aucune clause d'effet. Rectificatif au JORT n° 47 de 1973, p. 2127 (métadonnées). Attention : jort_cache.db donne le 16 novembre 1973 comme date de signature ; le fascicule porte le 19 novembre. Articles premier et 2 à 8 lus à l'image."
}
```

```json
{
  "id": "loi94-71",
  "type": "legislation",
  "title": "Loi n° 94-71 du 27 juin 1994, relative à la révision des taux de la contribution aux régimes de retraite dans le secteur public",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "50",
  "page": "1086",
  "issued": {"date-parts": [[1994, 6, 27]]},
  "URL": "https://www.pist.tn/jort/1994/1994F/Jo05094.pdf",
  "note": "citation-key: loi94-71\nJORT n° 50 du 28 juin 1994, p. 1086. Article unique : +1 point à la charge de l'assuré social à partir du 1er juillet 1994, +1,2 point à la charge de l'employeur à partir du 1er juillet 1995 ; modifie en conséquence l'art. 5 de la loi 83-31, les art. 9 et 13 de la loi 85-12, l'art. 5 de la loi 85-16 et l'art. 5 de la loi 88-16. Texte lu."
}
```

```json
{
  "id": "loi2001-123-lf2002",
  "type": "legislation",
  "title": "Loi n° 2001-123 du 28 décembre 2001, portant loi de finances pour l'année 2002",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "104",
  "page": "4260",
  "issued": {"date-parts": [[2001, 12, 28]]},
  "URL": "https://www.pist.tn/jort/2001/2001F/Jo1042001.pdf",
  "note": "citation-key: loi2001-123-lf2002\nJORT n° 104 du 28 décembre 2001. Art. 85, p. 4260 (édition française) : échéancier pluriannuel — assuré social +1 point (0,50 au 1/7/2002, 0,25 au 1/7/2003, 0,25 au 1/7/2004) ; employeur +1,5 point en cinq marches de 2002 à 2006. C'est l'article qui porte les paliers 2003 et 2004 de la série CNRPS. Texte lu (couche texte à encodage décalé de -29 ; décodage vérifié contre la pagination du fascicule)."
}
```

```json
{
  "id": "loi2007-43",
  "type": "legislation",
  "title": "Loi n° 2007-43 du 25 juin 2007, modifiant et complétant les lois régissant les pensions servies au titre des régimes de retraite, d'invalidité et de survivants dans les secteurs public et privé et des régimes spéciaux",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "51",
  "page": "2197-2199",
  "issued": {"date-parts": [[2007, 6, 25]]},
  "URL": "https://www.pist.tn/jort/2007/2007F/Jo0512007.pdf",
  "note": "citation-key: loi2007-43\nJORT n° 51 du 26 juin 2007. Article premier, p. 2198 : employeur +1,8 point (0,60 au 1er janvier 2007, 2008 et 2009) ; assuré social +1,2 point (0,40 au 1er juillet 2007, 2008 et 2009). C'est l'article qui porte les paliers 2008 et 2009 de la série CNRPS. Texte lu."
}
```

```json
{
  "id": "loi83-31",
  "type": "legislation",
  "title": "Loi n° 83-31 du 17 mars 1983, fixant le régime de retraite des membres du gouvernement",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "23",
  "page": "808-809",
  "issued": {"date-parts": [[1983, 3, 17]]},
  "URL": "https://www.pist.tn/jort/1983/1983F/Jo02383.pdf",
  "note": "citation-key: loi83-31\nJORT n° 23 du 25 mars 1983. Art. 5 : retenue pour pension de 10 % sur la rémunération, contribution de l'État de 15 %, au profit de la CNRPS. Texte lu (OCR relu)."
}
```

```json
{
  "id": "loi85-16",
  "type": "legislation",
  "title": "Loi n° 85-16 du 8 mars 1985, fixant le régime de retraite des députés",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "21",
  "page": "375-377",
  "issued": {"date-parts": [[1985, 3, 8]]},
  "URL": "https://www.pist.tn/jort/1985/1985F/Jo02185.pdf",
  "note": "citation-key: loi85-16\nJORT n° 21 du 15 mars 1985. Art. 5 : les indemnités parlementaires permanentes sont soumises à une retenue de 10 % au profit de la CNRPS. Texte lu (OCR) ; le libellé de la contribution de l'État reste à relire à l'image."
}
```

```json
{
  "id": "loi88-16",
  "type": "legislation",
  "title": "Loi n° 88-16 du 17 mars 1988, fixant le régime de retraite des gouverneurs",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "20",
  "page": "427",
  "issued": {"date-parts": [[1988, 3, 17]]},
  "URL": "https://www.pist.tn/jort/1988/1988F/Jo02088.pdf",
  "note": "citation-key: loi88-16\nJORT n° 20 du 22 mars 1988, p. 427. Art. 5 : retenue de 10 % sur les éléments permanents de la rémunération des gouverneurs, contribution de l'État de 15 %, au profit de la CNRPS. Texte lu (OCR relu). Attention : le modèle openfisca la date par erreur de 1983 dans son titre arabe."
}
```

```json
{
  "id": "decret73-91",
  "type": "legislation",
  "title": "Décret n° 73-91 du 12 mars 1973, portant organisation des régimes de prévoyance sociale",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "10",
  "page": "355-356",
  "issued": {"date-parts": [[1973, 3, 12]]},
  "URL": "https://www.pist.tn/jort/1973/1973F/Jo01073.pdf",
  "note": "citation-key: decret73-91\nJORT n° 10, fascicule daté 9-13-16 mars 1973. Art. 14 : cotisation de l'assuré 1 % sur les éléments soumis à retenue pour pension. Art. 15 : cotisation supplémentaire du régime facultatif 3 % ; « la cotisation due par le retraité et la veuve de retraité titulaire d'une pension directe ou de réversion est fixée à 2 % de leur pension en principal ». Art. 16 : contribution de l'État 1 %. Art. 18 : prend effet à compter du 1er avril 1973. Texte lu à l'image (p. 356)."
}
```

```json
{
  "id": "decret2007-1406",
  "type": "legislation",
  "title": "Décret n° 2007-1406 du 18 juin 2007, fixant l'assiette de calcul des taux de cotisations dues au titre du régime de base d'assurance maladie et ses étapes d'application",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "49",
  "page": "2154-2162",
  "issued": {"date-parts": [[2007, 6, 18]]},
  "URL": "https://www.pist.tn/jort/2007/2007F/Jo0492007.pdf",
  "note": "citation-key: decret2007-1406\nJORT n° 49 du 19 juin 2007. Art. 2, p. 2156 : assiette des titulaires de pension = montant brut de la pension. Art. 4, p. 2157 : montée en charge CNRPS actifs (3 % au 1/7/2007, 4,88 % au 1/7/2008, 6,75 % au 1/7/2009) avec la répartition employeur/employé. Art. 12 et 13, p. 2162 : titulaires de pensions affiliés à la CNRPS — 1 % au 1/7/2007, 2 % au 1/7/2008, 3 % au 1/7/2009, 4 % au 1/7/2010. Texte lu à l'image."
}
```

```json
{
  "id": "loi2007-51",
  "type": "legislation",
  "title": "Loi n° 2007-51 du 23 juillet 2007, modifiant et complétant la loi n° 60-30 du 14 décembre 1960, relative à l'organisation des régimes de sécurité sociale",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "60",
  "page": "2581",
  "issued": {"date-parts": [[2007, 7, 23]]},
  "URL": "https://www.pist.tn/jort/2007/2007F/Jo0602007.pdf",
  "note": "citation-key: loi2007-51\nJORT n° 60 du 27 juillet 2007, p. 2581. Art. premier : nouveau premier paragraphe de l'art. 105 de la loi 60-30 — pénalité de retard de 1 % par mois ou fraction de mois pour non-paiement, majorée de 0,5 % par mois en cas de non-déclaration de la totalité des salaires. Art. 2 : nouveau paragraphe à l'art. 45 — les cotisations peuvent être versées mensuellement. Texte lu."
}
```

```json
{
  "id": "decret2014-2919",
  "type": "legislation",
  "title": "Décret n° 2014-2919 du 15 août 2014, portant remise totale et automatique des pénalités de retard exigées au titre des régimes de sécurité sociale et du régime de réparation des préjudices résultant des accidents du travail et des maladies professionnelles",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "67",
  "page": "2073-2074",
  "issued": {"date-parts": [[2014, 8, 15]]},
  "URL": "https://www.pist.tn/jort/2014/2014F/Jo0672014.pdf",
  "note": "citation-key: decret2014-2919\nJORT n° 67 du 19 août 2014. Exemple canonique des remises périodiques de pénalités. Article premier : remise « au titre des trimestres écoulés et dans la limite du deuxième trimestre de l'année 2014 », visant aussi les pénalités pour non-déclaration de la totalité des salaires — confirme la maille trimestrielle du recouvrement CNSS. Texte lu."
}
```

```json
{
  "id": "decretloi2011-48",
  "type": "legislation",
  "title": "Décret-loi n° 2011-48 du 4 juin 2011, modifiant les lois régissant les pensions civiles et militaires de retraite et des survivants dans le secteur public, le régime de retraite des membres du gouvernement et le régime de retraite des gouverneurs",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "41",
  "page": "844",
  "issued": {"date-parts": [[2011, 6, 4]]},
  "URL": "https://www.pist.tn/jort/2011/2011F/Jo0412011.pdf",
  "note": "citation-key: decretloi2011-48\nJORT n° 41 du 7 juin 2011, p. 844. Porte le palier employeur de juillet 2011 dans le modèle openfisca. Métadonnées jort_cache.db (recid 80629) ; contenu NON LU — à vérifier avant citation."
}
```

```json
{
  "id": "loi2005-54",
  "type": "legislation",
  "title": "Loi n° 2005-54 du 18 juillet 2005, étendant les régimes spéciaux applicables aux membres de la chambre des députés aux membres de la chambre des conseillers",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "57",
  "page": "1749",
  "issued": {"date-parts": [[2005, 7, 18]]},
  "URL": "https://www.pist.tn/jort/2005/2005F/Jo0572005.pdf",
  "note": "citation-key: loi2005-54\nJORT n° 57 du 19 juillet 2005, p. 1749. Explique la mention de la chambre des conseillers dans la loi 2007-43. Métadonnées jort_cache.db (recid 110642) ; contenu non lu."
}
```

> **Rappel de procédure** (`docs/notes/outillage-sources.md`, § 7) : `scripts/sync_biblio.py` est
> en lecture seule depuis Zotero. Toute clé ajoutée à la main dans `references.json` sera
> écrasée au prochain sync tant qu'elle n'est pas montée dans Zotero. Ces entrées sont donc à
> verser d'abord dans `docs/notes/biblio-a-rapatrier.md`.

---

## Notions à porter au glossaire

Le glossaire porte déjà `cnss`, `cnrps`, `cnam`, `cotisations-sociales`, `assure-social`,
`stage-cotisation`, `pensions-civiles-militaires`. Manquent, pour ce chapitre :

| `id` proposé | Terme FR | Terme AR | Source canonique pressentie |
|---|---|---|---|
| `retenue-pour-pension` | Retenue pour pension | الحجز بعنوان الجراية | Loi 59-18, art. 5-I ; loi 85-12, art. 9 (`texte lu`) |
| `contribution-employeur-retraite` | Contribution de l'employeur au régime de retraite | مساهمة المؤجر | Loi 85-12, art. 13 (`texte lu`) |
| `elements-permanents-remuneration` | Éléments permanents de la rémunération | العناصر القارة للأجر | Loi 85-12, art. 10 : « les différents éléments permanents de la rémunération de l'agent qu'ils soient en espèces ou en nature » — c'est la définition de l'assiette CNRPS (`texte lu`) |
| `prevoyance-sociale` | Prévoyance sociale | الحيطة الاجتماعية | Décret 73-91, intitulé et chapitre III (`texte lu`) |
| `declaration-trimestrielle-salaires` | Déclaration trimestrielle de salaires | التصريح الثلاثي بالأجور | Loi 60-30, art. 46 (`texte lu`) |
| `penalites-de-retard` | Pénalités de retard | خطايا التأخير | Loi 60-30, art. 105 tel que modifié par la loi 2007-51, art. premier ; loi 85-12, art. 9 bis (`texte lu`) |
| `taxation-office-cotisations` | Taxation d'office (cotisations sociales) | التوظيف الإجباري | Loi 60-30, art. 104 et 105 (`texte lu`) |
| `remise-gracieuse-penalites` | Remise gracieuse des pénalités | الإعفاء من خطايا التأخير | Loi 60-30, art. 107 ; décret 2014-2919 (`texte lu`) |
| `regimes-speciaux-retraite` | Régimes spéciaux de retraite | الأنظمة الخصوصية للتقاعد | Lois 83-31, 85-16 et 88-16, art. 5 (`texte lu`) |
| `capital-deces` | Capital décès | رأس المال عند الوفاة | Décret 74-572 puis décret 93-308 — **non lus**, à ne poser qu'après vérification |

Vérifier aussi que `cnrps` porte bien, dans sa définition, la double filiation
CNR + CPS (loi 75-83, art. 28) ; sa fiche actuelle ne cite que la loi 85-12 comme
`source_definition`, ce qui est exact pour le régime mais non pour la caisse.

---

## Deux points de forme relevés dans le chapitre (`precis/fr/cotisations_sociales/index.qmd`)

Sans rapport avec les sources, mais utiles au rédacteur :

- **Ligne 120** : « Trois millésimes — 2003, 2004, 2008 et 2009 — ne portent pas de texte en
  regard. » Quatre millésimes sont énumérés ; le compte est à corriger — et le constat
  lui-même tombe, puisque les quatre relèvent des échéanciers lus en Partie 2.1.
- **Lignes 122-124** : le `callout-warning` « Les références de cette série sont à reprendre »
  peut être **supprimé**. Toutes les références de la série ont désormais une URL pist.tn et un
  niveau d'attestation ; la seule réserve résiduelle, mais elle est d'une autre nature, porte
  sur l'exactitude d'une **valeur** (le palier 2019) et non sur la qualité des liens.

---

## Ce qui n'a pas pu être établi

1. **La date d'effet du taux de 7 % de 1959.** La loi 59-18 ne l'énonce pas. Le « 1er février
   1959 » du chapitre et du modèle n'a aucun appui textuel. Ce qui est certain : signature le
   5 février 1959, publication au JORT n° 8 daté 3-6 février 1959, et effet au 1er avril 1959
   pour l'ouverture des droits à pension (art. 52). **TODO** : chercher si un décret
   d'application ou la loi 59-19 fixe une date pour la retenue.
2. **Les dates d'entrée en vigueur de la loi 73-71 (1973), de l'article 38 de la LF 1975 et de
   la loi 2019-37.** Aucun de ces trois textes ne comporte de clause d'effet ; les dates
   retenues par la série (1975, 2019) sont `dérivé`, et la règle de droit commun sur l'entrée
   en vigueur des textes publiés au JORT n'a pas été identifiée ni citée dans ce dossier. À
   établir avant toute affirmation de date.
3. **Le contenu du décret-loi n° 2011-48 du 4 juin 2011** (palier employeur de juillet 2011,
   11,5 % → 12,5 %). Métadonnées seules.
4. **Le capital décès** : ni le décret 74-572 (taux de 0,5 % pour le pensionné, 1 % pour
   l'actif), ni le décret 93-308, ni la circulaire du Premier ministre n° 12 du 15 février 1993
   invoquée par le modèle n'ont été lus. La circulaire n'a d'ailleurs **pas été retrouvée dans
   `jort_cache.db`** — les circulaires du Premier ministre ne sont pas systématiquement publiées
   au JORT. À ne pas citer en l'état.
5. **Le prélèvement sur la pension avant le 1er juillet 2007.** Le seul texte antérieur
   retrouvé est l'article 15 du décret 73-91 (2 % au 1er avril 1973), dont la portée est
   incertaine et dont le taux ne se raccorde pas à la série obligatoire (voir 1.2 b). **La case
   « pensionnés CNRPS, avant 2007 » doit rester vide dans le chapitre.** À trancher sur
   l'arrêté d'application du 12 mars 1973 (JORT n° 10, pp. 357-358) et sur le décret n° 88-186
   du 6 février 1988.
6. **Le décret gouvernemental d'application des articles 71 quinquies et 71 sexies** de la loi
   85-12 (échange mensuel de données CNRPS / employeur). Renvoi exprès du texte de 2019 ; le
   décret n'a pas été identifié. **TODO** : recherche FTS ciblée sur 2019-2022.
7. **Le libellé exact de la contribution de l'État dans la loi 85-16** (députés) : l'OCR ne
   restitue pas la phrase complète. Le taux de 15 % est présumé par analogie avec les lois 83-31
   et 88-16, mais **n'est pas attesté** ; à relire à l'image (JORT n° 21/1985, p. 375).
8. **Les dates d'effet des trois lois de régimes spéciaux.** Le modèle fait démarrer la série au
   `1985-04-01` pour un texte de 1983 ; la clause d'entrée en vigueur de chacune des trois lois
   n'a pas été relevée.
9. **L'assiette CNSS** (quelles primes, quels avantages en nature) n'est traitée ici que du côté
   public (loi 85-12, art. 10). Le TODO correspondant du chapitre relève du périmètre « secteur
   privé ».
10. **La modification postérieure à 1985 des dispositions survivantes de la loi 59-18 sur
    l'invalidité.** Le brief la tenait pour acquise ; la recherche décrite en 1.1 c) n'a rien
    trouvé dans `jort_cache.db` sur 1985-2026. Trois hypothèses non départagées : le texte
    modificatif existe mais son intitulé ne cite pas le numéro « 59-18 » (la base indexe les
    titres, non le corps des textes) ; la modification est passée par le décret-loi n° 72-3 du
    11 octobre 1972 sur les pensions militaires d'invalidité, plusieurs fois modifié depuis
    (lois 85-7, 90-81, 92-104, 2000-44 — **métadonnées**), qui est un régime distinct ; ou
    l'affirmation est inexacte. **Ne rien écrire sur ce point tant qu'il n'est pas tranché.**
11. **Aucune donnée chiffrée de rendement du recouvrement** (taux de recouvrement, stock de
    créances CNSS/CNRPS) n'a été recherchée. Si le chapitre veut accompagner la section d'une
    vue d'évolution, la source pressentie est le rapport annuel de la CNSS ou l'annexe
    « organismes de sécurité sociale » au projet de loi de finances — non consultée.
