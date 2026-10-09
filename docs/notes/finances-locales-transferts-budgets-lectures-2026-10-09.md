# Finances locales — transferts et budgets : lectures du 9 octobre 2026 (réponses aux huit questions de l'architecte)

> Note du documentaliste, 9 octobre 2026. Elle répond au § 9 de
> `docs/notes/finances-locales-transferts-budgets-plan-architecte.md`, et à rien d'autre.
>
> **Méthode.** Index `jort_cache.db` (titres français et arabes, FTS et LIKE) ; fascicules du corpus
> local `~/projets/PDFs-legislation-tunisie/PDFs/JORT/` ; `pist.tn` pour un fascicule absent du
> corpus et pour le contrôle des adresses. Chaque passage cité porte son état de lecture :
> **image** (page rendue et lue à l'œil), **texte** (couche texte du PDF, nette), **océrisation**
> (tesseract `fra`, sans relecture à l'image). Le texte arabe extrait a été normalisé (NFKC,
> diacritiques retirés) ; tout chiffre arabe cité a été relu à l'image, sauf mention contraire.
>
> **Adresses.** Les dix-huit adresses pist.tn citées ont répondu `200 application/pdf` avec leur taille
> le 9 octobre 2026 (`curl -sk`, certificat échu). Deux éditions françaises répondent `404` (289
> octets) et sont absentes du corpus : JORT n° 51 de 2018 et n° 39 de 2018.
>
> **Dates d'effet.** Celle que le texte énonce ; à défaut, la date d'exécution avec son calcul
> (avant 1993 : un jour franc après la publication ; depuis 1993 : cinq jours après le dépôt au
> gouvernorat de Tunis, jour du dépôt non compté).
>
> Fichiers de travail, hors dépôt :
> `/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/15adcd5f-c210-406f-907e-f6545e1e97a0/scratchpad/doc-fl-transferts/`
> (`img/` rendus, `ocr/` océrisations, `scan.py` balayage plein texte).

## Ce qui change au plan, en bref

1. **L'article 11 de la loi de finances pour 2018 est lu : la fin du fonds devient une rupture**
   (T4), datée du 1er janvier 2018 par l'article 67 de la même loi. Il supprime le fonds, abroge la
   loi n° 75-36 et renvoie les critères de répartition à un **arrêté conjoint**.
2. **Cet arrêté existe et il est lu** : arrêté du 22 juin 2018, modifié le 29 mars 2019 et le
   29 juin 2021. L'état du droit après 2018, que le plan disait « non établi », peut s'écrire.
   **Second étage, lu aussi** : depuis le 1er janvier 2021, l'article 13 de la loi de finances pour
   2021 crée un fonds d'appui à la décentralisation « destiné à financer les budgets des
   collectivités locales » ;
   en attendant son décret, 90 % vont à la subvention annuelle selon l'arrêté de 2018, 10 % selon
   les règles de l'ancien fonds de coopération, dont le compte est supprimé (Q7, b bis).
3. **Le § 8, point 1, du plan est à renverser** : « au 1er janvier 2018 » (`_longue_periode`,
   l. 28 et 146) est exact ; c'est `_transferts`, l. 93 (« sa date d'effet n'est pas relevée »), qui
   est à corriger.
4. **Les 15 % de 2018-2019 ne sont plus la « réserve » du fonds** : ils correspondent, au million
   près, à la part « dépenses de développement et besoins spécifiques et imprévus » de l'article
   premier de l'arrêté de 2018 (concordance calculée, non définition publiée). La série change de
   nature **et de base** en 2018 (Q7).
5. **T2 a son objet dans les mots de la loi** (rubrique de l'article 92 de la loi de finances pour
   1987). **T3 et B2 n'en ont pas** : ni la loi n° 2000-60 ni la loi organique n° 2007-65 n'impriment
   de rubrique ou d'exposé ; l'objet reste « non dit par la loi ».
6. **R2 est confirmée à l'image** et peut être promue ; les montants du décret n° 92-308 sont
   exacts.
7. **Trouvé en passant, hors des huit questions** : le décret gouvernemental n° 2020-52 du
   23 janvier 2020 approuve le modèle de nomenclature budgétaire des communes — c'est, selon toute
   apparence, le texte que cherche la fiche `r-ccl-2018-nomenclature-art167` (voir en fin de note).

---

## Q1. Loi de finances pour 2018, article 11

**Réponse.** L'article 11 supprime le fonds à compter du 1er janvier 2018, verse son reliquat au
budget de l'État, abroge la loi n° 75-36 et ses modificatifs, et confie à un arrêté conjoint des
deux ministres les critères de répartition des subventions du budget de l'État aux collectivités.

**Texte.** Loi n° 2017-66 du 18 décembre 2017, portant loi de finances pour l'année 2018,
article 11. JORT n° 101 du 19 décembre 2017.
- Édition française : p. 4270 — <https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf> (page 6 du PDF).
- Édition arabe : p. 4270 — <https://www.pist.tn/jort/2017/2017A/Ja1012017.pdf> (page 6 du PDF).
- Les deux éditions portent ici la même pagination.

**Rubrique imprimée.**
- FR : « Suppression du fonds spécial du trésor intitulé « Fonds commun des collectivités publiques
  locales » ».
- AR : « حـــذف الحساب الخاص في الخزينة والمسمّى "حساب المال المشترك للجماعات العموميّة المحليّة" ».

**Citation exacte (FR, lue à l'image).**

> Art. 11 :
> 1) Est supprimé le fonds spécial du trésor intitulé «fonds commun des collectivités publiques
> locales », institué par la loi n° 75-36 du 14 mai 1975, relative au fonds commun des
> collectivités locales. Le solde de ses ressources est transféré au budget de l'Etat.
> 2) Sont abrogées les dispositions de la loi n°75-36 du 14 mai 1975, relative au fonds commun des
> collectivités locales, ensemble les textes qui l'ont modifié ou complété.
> 3) Les critères de répartition des subventions du budget de l'Etat entre les collectivités
> locales, sont fixés par arrêté conjoint du ministre chargé des collectivités locales et du
> ministre chargé des finances.

**Citation exacte (AR, lue à l'image), § 3.** « تضبط مقاييس توزيع مبالغ الدعم المالي من ميزانيّة
الدولة بين الجماعات المحليّة بقرار مشترك بين الوزير المكلّف بالجماعات المحليّة والوزير المكلّف
بالماليّة. » Le § 1 arabe dit « وتحوّل بقايا موارده إلى ميزانيّة الدولة ».

**Date d'effet : 1er janvier 2018.** L'article 11 n'a pas de clause propre ; l'article 67, rubrique
« Date d'application de la loi de finances pour l'année 2018 » (FR p. 4292, lu à l'image), dispose :
« 1) Sous réserve des dispositions contraires prévues par la présente loi, les dispositions de la
présente loi s'appliquent à compter du 1er janvier 2018. » Les § 2 à 4 de l'article 67 ne visent pas
l'article 11. C'est une date énoncée par le texte : aucun calcul d'exécution. (Pour mémoire, le
fascicule français porte : déposé au gouvernorat de Tunis le 20 décembre 2017.)

**État.** Article 11 : lu à l'image, FR et AR. Article 67 : lu à l'image, FR ; AR non relu.

**Avant → après.**
- Avant : un fonds spécial du Trésor régi par la loi n° 75-36, dont la loi fixe elle-même le
  partage (82 % aux collectivités, 18 % de réserve ; critères de l'article 3).
- Après : plus de fonds ni de loi de partage ; des « subventions du budget de l'État » dont les
  critères relèvent d'un arrêté conjoint. **La règle de partage descend de la loi à l'arrêté.**

**Trois précautions pour le rédacteur.**
- « Le solde de ses ressources » (§ 1) est le **reliquat** du compte (« بقايا موارده »), non la
  « réserve » ou « solde » de 25 % puis 18 % (« المدّخر ») de l'article 3 de la loi n° 75-36. Les
  deux mots français coïncident, pas les mots arabes.
- Le français dit « fonds spécial du trésor » là où l'arabe dit « compte spécial » (« الحساب
  الخاص في الخزينة »). Le nom français imprimé en 2017 est « fonds commun des collectivités
  **publiques** locales ». Le chapitre (l. 93) ne cite que le nom arabe : le nom français est
  disponible.
- L'article 11 ne dit rien du montant ni du nom des subventions ; c'est l'arrêté qui parle de
  « subventions annuelles » (Q7).

**Ce que cela change au plan.** § 2.2 : le « terme » devient la rupture **T4**, colonne « ce que
la loi cherche » = la rubrique ci-dessus ; date d'effet 1er janvier 2018. § 2.4, section « Depuis
2018 » : elle s'écrit avec l'arrêté (Q7). § 8, point 1 : à renverser (voir « en bref », 3). A5 est
levé. Hors précis : `tunisia-data/sources/finances-locales.md` et `…-communes.md` datent la
suppression « selon Dafflon et Gilbert 2022 » ; la source primaire est désormais lue.

**Références.** Clé existante `lf-2018` (`precis/fr/references.json`, que le `_quarto.yml` du
volume charge avec `references.json` : rien à verser). Sa `note` ne connaît que l'article 53 et
sa `page` vaut « 4289-4290 » : ajouter « art. 11, FR et AR p. 4270 ; art. 67, FR p. 4292 ».

---

## Q2. Rubriques ou exposés : loi de finances pour 1987, art. 92 ; loi n° 2000-60

### a) Loi de finances pour 1987, article 92

**Réponse.** L'article a une rubrique, qui dit l'objet : intégrer au budget de l'État les recettes
fiscales et parafiscales qui revenaient à des fonds spéciaux du Trésor.

**Texte.** Loi n° 86-106 du 31 décembre 1986, portant loi de finances pour la gestion 1987,
article 92. JORT n° 78 des 30-31 décembre 1986, FR p. 1623 —
<https://www.pist.tn/jort/1986/1986F/Jo07886.pdf> (page 15 du PDF). Édition arabe non lue.

**Ce qui est imprimé, dans l'ordre (lu à l'image, 170 dpi).**
- Intitulé de la partie : « DEUXIEME PARTIE — FONDS SPECIAUX DU TRESOR ».
- Rubrique de l'article 91 : « SUPPRESSION DE CERTAINS FONDS SPECIAUX DU TRESOR ».
- **Rubrique de l'article 92 : « INTEGRATION AU BUDGET DE L'ETAT DES RECETTES FISCALES ET
  PARA-FISCALES REVENANT AUX FONDS SPECIAUX DU TRESOR ».**
- Article 92 : « Les impôts, droits, taxes redevances et contributions à caractère fiscale ou
  para-fiscal affectés en totalité ou en partie, en vertu de la législation ou de la
  règlementation en vigueur aux fonds spéciaux de trésor désignés ci-dessous, reviennent au profit
  du budget [général] de l'Etat. » (Le fascicule porte des coquilles — « fiscale », et une faute
  sur « général » : ne pas les reproduire.)
- Suit la liste : douze fonds sous huit ministères, le premier étant, sous « Ministère de
  l'intérieur », « — Fonds commun des collectivités locales ». Les autres : fonds de la garantie
  automobile, fonds de promotion du logement pour les salariés ; compte du comité national de
  solidarité sociale, fonds des accidents de travail ; fonds national d'amélioration de l'habitat ;
  fonds de stabilisation des prix des produits avicoles ; caisse générale de compensation, fonds de
  promotion des exportations, fonds de stabilisation des prix des légumes et fruits ; caisse de
  compensation et de soutien des transports routiers ; fonds national pour la promotion du sport et
  de la jeunesse.
- Deux alinéas finals : « Les modalités d'application de l'alinéa précédent sont fixées par le
  ministre du plan et des finances. » ; « Toutes les dispositions antérieures contraires au présent
  article sont abrogées. »
- Rubrique de l'article 94 (même page) : « PRELEVEMENT SUR LES RESSOURCES DU FONDS COMMUN DES
  COLLECTIVITES LOCALES AU PROFIT DE LA CAISSE DES PRETS ET DE SOUTIEN AUX COLLECTIVITES LOCALES ».

**Date d'effet.** L'article 92 n'en énonce pas. La loi n'a pas de clause générale : son dernier
article est l'article 102 (FR p. 1624, lu à l'image), qui fixe « pour la gestion 1987 » les
recettes et dépenses des fonds spéciaux, suivi de la formule de promulgation, « le 31 décembre
1986 ». Date d'exécution par calcul : un jour franc après une publication au 31 décembre 1986,
soit le **2 janvier 1987**. Le fascicule est daté « 30-31 décembre » : le jour de parution est
supposé être le 31. « Gestion 1987 », que retient le plan, reste la formulation sûre.

**État.** Lu à l'image (rubriques, article 92, article 102).

**Ce que cela change au plan.** T2, colonne « ce que la loi cherche » : la rubrique de
l'article 92. Fait utile pour le texte : le fonds commun n'est pas visé seul, mais avec onze
autres fonds — la mesure est une réforme des fonds spéciaux, pas des finances locales. À ne pas
confondre : l'article 91 **supprime** d'autres fonds (dont le « Fonds de développement
municipal ») ; l'article 92 ne supprime pas le fonds commun, il lui retire ses impôts.

**Références.** Clé existante `loi86-106-lf1987` (compléter la `note` : rubrique de l'art. 92 ;
art. 102, p. 1624).

### b) Loi n° 2000-60 du 13 juin 2000

**Réponse.** La loi ne dit pas ce qu'elle cherche : ni rubrique, ni exposé, ni titre de section.
Elle tient en deux articles sous son seul intitulé.

**Texte.** Loi n° 2000-60 du 13 juin 2000, modifiant la loi n° 75-36 du 14 mai 1975, relative au
fonds commun des collectivités locales. JORT n° 48 du 16 juin 2000, FR p. 1461 —
<https://www.pist.tn/jort/2000/2000F/Jo0482000.pdf> (page 9 du PDF). AR p. 1489 (note du
4 octobre, non relue ici).

**Ce qui est imprimé (lu à l'image).**
- Intitulé : « Loi n° 2000-60 du 13 juin 2000, modifiant la loi n° 75-36 du 14 mai 1975, relative
  au fonds commun des collectivités locales (1). »
- Note (1) : « Travaux préparatoires : Discussion et adoption par la chambre des députés dans sa
  séance du 8 juin 2000. »
- Le seul passage qui désigne le public nouveau, quatrième tiret de l'alinéa 3 nouveau : « - 4%
  réparti au prorata de la population entre les communes ayant une moyenne des trois dernières
  années au titre des montants constatés inscrits au rôle de la taxe sur les immeubles bâtis, des
  recettes réalisées au titre de la taxe sur les établissements à caractère industriel, commercial
  ou professionnel, de la taxe hôtelière et des produits des marchés affermés, inférieure à la
  moyenne des recettes réalisées par toutes les communes au titre des taxes et produits précités
  au cours des trois dernières années. »
- Article 2 : « La présente loi entre en vigueur le 1er janvier 2001. »

**État.** Lu à l'image. L'objet de la loi : **non identifié dans le texte** ; il relève des débats
de la séance du 8 juin 2000, hors corpus (fiche proposée, § « Recherches »).

**Ce que cela change au plan.** T3 garde « objet non dit par la loi ». La colonne peut porter
l'intitulé et la désignation du public par le quatrième tiret, sans prêter d'objectif au
législateur. Les mots « péréquation », « communes à faibles recettes » ou « faible potentiel » ne
sont pas dans la loi : ce sont des mots de commentaire.

**Références.** Clé existante `loi2000-60`. **Erreur à corriger par le bibliographe** : son `title`
porte « loi n° 75-36 du **13** mai 1975 » ; le fascicule imprime « du **14** mai 1975 ».

---

## Q3. Loi organique n° 2007-65 : exposé des motifs ou rubriques

**Réponse.** Aucun : la loi n'imprime ni exposé ni rubrique ; six articles sous un intitulé qui dit
seulement « modifiant et complétant ».

**Texte.** Loi organique n° 2007-65 du 18 décembre 2007, modifiant et complétant la loi n° 75-35
du 14 mai 1975 relative à la loi organique du budget des collectivités publiques locales. JORT
n° 103 du 25 décembre 2007, FR p. 4277-4281 — <https://www.pist.tn/jort/2007/2007F/Jo1032007.pdf>
(pages 5 à 9 du PDF).

**Ce qui est imprimé (couche texte, nette).**
- Note (1), p. 4277 : « Travaux préparatoires : Discussion et adoption par la chambre des députés
  dans sa séance du 12 décembre 2007. Discussion et adoption par la chambre des conseillers dans sa
  séance du 15 décembre 2007. »
- Les seuls passages où la loi dit une fin ou une règle dans ses propres mots :
  - article premier (nouveau), p. 4277 : « Le budget des collectivités locales prévoit et autorise
    pour chaque année l'ensemble des charges et des ressources desdites collectivités, et ce, dans
    le cadre des objectifs du plan de développement économique et social. » ;
  - article 7 bis, p. 4280 : « Il peut être autorisé dans le budget des collectivités locales
    l'affectation des crédits selon des programmes et des missions. » ; les programmes visent « des
    objectifs déterminés et des résultas pouvant être évalués » (coquille du fascicule) ;
  - article 21 bis, p. 4280 : « Le montant total des dépenses ordonnancées doit être limité aux
    recettes effectivement réalisées. » ;
  - article 23 bis, p. 4280-4281 : « le montant total des dépenses du titre I engagées en cours
    d'année ne doit pas dépasser le montant des recettes effectivement réalisées au niveau de ce
    même titre » ; « La violation des dispositions prévues à l'alinéa premier du présent article
    constitue une faute de gestion ».
- Article 6, p. 4281 : « Les dispositions de la présente loi s'appliquent au budget des
  collectivités locales de l'année 2008 et aux budgets subséquents. »
- Article 2 : le mot « publique » est supprimé de l'intitulé de la loi de 1975 (« budget des
  collectivités locales »).

**État.** Lu par la couche texte (pages vérifiées une à une) ; l'objet de la loi : **non identifié
dans le texte**, à chercher dans les débats des 12 et 15 décembre 2007, hors corpus.

**Ce que cela change au plan.** B2 garde « objet non dit par la loi ». Le titre de rupture peut
s'appuyer sur l'article 21 bis, cité tel quel : c'est la formule du plan (« la dépense limitée aux
recettes réalisées »), et elle est de la loi. La lecture concurrente du § 3.2 (étape de B1) n'est
ni confortée ni écartée par le texte.

**Références.** Clé existante `loi-org2007-65` (note : art. 21 bis et 23 bis p. 4280 ; art. 6
p. 4281 ; travaux préparatoires p. 4277).

---

## Q4. Loi de finances pour 1992, article 80 ; décret n° 92-308

**Réponse.** La lecture par océrisation est confirmée à l'image, mot pour mot et chiffre pour
chiffre : la réserve de 25 % est « attribué[e] par décret » à six bénéficiaires, et le décret de
1992 répartit 24 millions de dinars.

### a) Article 80

**Texte.** Loi n° 91-98 du 31 décembre 1991, portant loi de finances pour la gestion 1992,
article 80. JORT n° 90 du 31 décembre 1991, FR p. 2091 —
<https://www.pist.tn/jort/1991/1991F/Jo09091.pdf> (page 11 du PDF). Édition arabe non lue.

**Rubrique imprimée.** « DISTRIBUTION DU SOLDE DU FONDS COMMUN ».

**Citation exacte (lue à l'image, 200 dpi).**

> ARTICLE 80 :
> Les dispositions du paragraphe 4 de l'article 3 de la loi 75-36 du 14 Mai 1975 relatif au fonds
> commun des collectivités locales telle qu'elle a été modifiée ou complétée par les textes
> subséquents sont modifiées ainsi qu'il suit :
> Article 3 paragraphe 4 (nouveau) :
> Le solde de 25% des ressources du fonds commun est attribué par décret à la commune de Tunis, au
> Conseil Régional de Tunis, aux communes siége de gouvernorats, au district de Tunis, à la caisse
> des prêts et de soutien des collectivités locales et à l'Office National de l'Assainissement.
> Ce décret peut réserver dans ces dispositions une partie de ce solde en l'ajoutant à la part
> revenant aux communes visées au paragraphe 1er du présent article. La répartition sera effectuée
> sur la base des critères fixées au paragraphe 3 précédent.

**Date d'effet.** Ni l'article ni la loi n'en énoncent : le dernier article est l'article 102
(FR p. 2093, lu à l'image), suivi de « Tunis, le 31 décembre 1991 ». Calcul : publication au
31 décembre 1991, un jour franc, exécutoire le **2 janvier 1992**. Le décret d'application parle
de « la gestion 1992 ».

### b) Décret n° 92-308

**Texte.** Décret n° 92-308 du 10 février 1992 relatif à la répartition de la réserve du fonds
commun. JORT n° 12 du 25 février 1992, FR p. 227-228 —
<https://www.pist.tn/jort/1992/1992F/Jo01292.pdf> (pages 3 et 4 du PDF). Rubrique : « FONDS
COMMUN », sous « Ministère de l'intérieur ». Édition arabe non lue.

**Citation exacte (lue à l'image).** Visa : « Vu la loi n° 91-98 du 31 décembre 1991 portant loi de
finances pour la gestion 1992 et notamment son article 80. » Article premier : « La réserve du
fonds commun des collectivités locales fixée à 24 millions de dinars (24 000 000 d) pour la
gestion 1992 est répartie comme suit : »

| Bénéficiaire (ordre du décret) | Montant imprimé (D) | Part de la réserve (calcul) |
|---|---:|---:|
| La commune de Tunis | 4 600 000 | 19,2 % |
| Le district de Tunis | 920 000 | 3,8 % |
| Caisse des prêts et de soutien aux collectivités locales | 7 620 000 | 31,8 % |
| Les communes sièges des gouvernorats | 2 600 000 | 10,8 % |
| Office national de l'assainissement | 7 680 000 | 32,0 % |
| Conseil régional de Tunis | 580 000 | 2,4 % |
| Total (calcul : la somme rend bien 24 000 000) | 24 000 000 | 100 % |

Les parts sont un calcul de cette note, non un chiffre du JORT. Date d'exécution : publication le
25 février 1992, un jour franc, soit le **27 février 1992**.

**État.** Article 80 et décret : lus à l'image. La mention [OCR] de la note du 4 octobre tombe
pour ces deux textes.

**Ce que cela change au plan.** R2 peut être promue en rupture propre à la réserve (§ 2.2).
Vocabulaire : la loi dit « solde », le décret dit « réserve » — même objet. Point de § 8, 3
inchangé (la colonne « 1995 » du tableau porte une règle de 1992). Aucun décret antérieur à 1992
n'est à chercher : avant l'article 80, les parts sont dans la loi.

**Références.** Clés existantes `loi91-98-lf1992` (note : rubrique ; art. 102 p. 2093) et
`decret92-308`.

---

## Q5. Rubriques du code de 2018 (régime financier)

**Réponse.** Le régime financier est la quatrième division (« الباب الرابع ») du livre premier,
intitulée « في النظام المالي للجماعات المحلية » ; elle ouvre par quatre articles sans subdivision
(126 à 129), puis compte sept subdivisions (« قسم »).

**Texte.** Loi organique n° 2018-29 du 9 mai 2018, relative au code des collectivités locales.
JORT n° 39 du 15 mai 2018, **édition arabe** —
<https://www.pist.tn/jort/2018/2018A/Ja0392018.pdf>. L'édition française de ce numéro répond 404
sur pist.tn (`…/2018F/Jo0392018.pdf`) et manque au corpus.

**Le nom français des niveaux n'est pas attesté ici pour ce code.** Aucun texte français lu ne
cite ses divisions (loi organique n° 2025-4, loi de finances pour 2021, arrêtés de 2019 et 2021 :
tous renvoient à des articles). Un repère d'usage, pris dans un texte lu dans les deux langues :
la loi de finances pour 2018, article 66, rend « يضاف إلى العنوان الرابع […] باب رابع » par « Est
ajouté au titre IV […] un chapitre IV » (FR p. 4292, image ; AR, couche texte). Selon cet usage,
« باب » se dit **chapitre** et « عنوان » titre ; « قسم » serait alors **section**. La question de
l'architecte (« intitulés du titre et des chapitres ») ne se corrige donc pas sur cette base : le
plus probable est « livre premier, chapitre IV, sections 1 à 7 ». **Les traductions des intitulés
ci-dessous sont les nôtres.**

| Niveau (arabe) | Intitulé imprimé | Traduction de travail | Articles | Page AR |
|---|---|---|---|---|
| الكتاب الأول | الأحكام المشتركة | Dispositions communes | 1-199 | — |
| الباب الرابع | في النظام المالي للجماعات المحلية | Du régime financier des collectivités locales | 126-199 (126-129 sans subdivision) | 1724 (image) |
| القسم الأول | في القواعد العامة للميزانية ومواردها | Des règles générales du budget et de ses ressources | 130-145 | 1725 (texte) |
| القسم الثاني | في الاعتمادات المحالة من قبل الدولة | Des crédits transférés par l'État | 146-151 | 1727 (image) |
| القسم الثالث | في استخلاص المبالغ والمستحقات الراجعة للجماعات المحلية | Du recouvrement des sommes et créances revenant aux collectivités locales | 152-154 | 1729 (texte) |
| القسم الرابع | في تبويب الموارد | De la nomenclature des ressources | 155 | 1729 (texte) |
| القسم الخامس | في اعتمادات الجماعات المحلية ونفقاتها | Des crédits et des dépenses des collectivités locales | 156-165 | 1729 (texte) |
| القسم السادس | في إعداد الميزانية والمصادقة عليها | De la préparation du budget et de son adoption | 166-176 | 1731 (texte) |
| القسم السابع | في تنفيذ الميزانية وختمها | De l'exécution du budget et de sa clôture | 177-199 | 1732 (texte) |

Les intervalles d'articles sont ceux des notices de `jort_cache` ; les intitulés de la quatrième
division et de sa deuxième subdivision sont lus à l'image, les autres dans la couche texte arabe
normalisée (pages déduites du pied de page suivant, méthode vérifiée sur les deux pages vues à
l'image). À ne pas confondre avec la nomenclature du budget lui-même, où « العنوان الأول / الثاني »
sont les titres I et II et où « قسم » désigne une partie de dépenses.

**Dans les mots du code, pour B3.** Article 126, deuxième alinéa (lu à l'image, p. 1724) :
« تتمتع الجماعات المحلية بحرية التصرف في مواردها وتتقيّد بمبدأ الشرعية المالية وقاعدة التوازن
الحقيقي للميزانية » (les collectivités disposent librement de leurs ressources et sont tenues par
le principe de légalité financière et la règle de l'équilibre réel du budget — traduction de
travail). Dans l'intitulé de la sixième subdivision, « المصادقة » est l'adoption par le conseil,
non une approbation de tutelle (couche texte : « مصادقة مجلس الجماعة المحلية عليها ») : à ne pas
traduire par « approbation ».

**Lu en passant, deuxième subdivision (p. 1727-1728, texte et image) — utile à la section « Depuis
2018 » des transferts.** Article 146 : l'État transfère des crédits « بعنوان التسوية والتعديل » ;
article 148 : ressources du « صندوق دعم اللامركزية والتعديل والتضامن بين الجماعات المحلية », réparti
70 % aux communes, 20 % aux régions, 10 % aux districts (chiffres lus à l'image) ; article 150 :
critères (population, taux de chômage, potentiel fiscal, indice de développement, capacité
d'endettement), dont l'application relève d'un décret gouvernemental ; article 151 : crédit annuel
du budget de l'État pour les besoins spécifiques et imprévus et pour la caisse des prêts. Le code
nomme le fonds ; c'est l'article 13 de la loi de finances pour 2021 qui le crée (Q7, b bis). Les
arrêtés de 2018 et 2019 ne visent du code que son article 168 (arrêté de 2019), et se fondent sur
l'article 11 de la loi de finances pour 2018.

**État.** Lu en arabe, à l'image pour deux intitulés, en couche texte pour les autres. Édition
française : non identifiée ici ; noms français des niveaux : non attestés.

**Ce que cela change au plan.** § 3.2, B3 : la colonne peut porter l'intitulé de la quatrième
division et celui de sa sixième subdivision, en traduction signalée comme telle. Le plan garde
« chapitre » pour « باب ».

**Références.** Clé existante `loi-org-2018-29-ccl` (`precis/fr/references.json`).

---

## Q6. Clauses générales d'effet (1982, 1986, 1992) ; date d'effet de la loi organique n° 94-44

**Réponse.** Aucune des trois lois de finances n'a de clause générale d'effet : elles finissent sur
l'article des fonds spéciaux et la formule de promulgation. La loi organique n° 94-44 n'a pas de
clause non plus ; déposée le 18 mai 1994, elle est exécutoire le 23 mai 1994.

| Texte | Dernier article, page (FR), état | Ce qu'il dit | Signature ; JORT | Date d'exécution (calcul) |
|---|---|---|---|---|
| Loi n° 81-100, loi de finances pour la gestion 1982 | art. 111, p. 3048, image | « Est, et demeure, autorisée pour la gestion 1982 la perception au profit des fonds spéciaux du trésor… » ; puis « La présente loi sera publiée… » | « Fait au Palais de Carthage, le 31 décembre 1981 » ; n° 84 des 29-31 décembre 1981 | publication au 31 décembre 1981 + un jour franc = **2 janvier 1982** |
| Loi n° 85-109, loi de finances pour l'année 1986 | art. 87, p. 1741, image | même formule, « pour la gestion 1986 », tableau « F » | « le 31 décembre 1985 » ; n° 91 du 31 décembre 1985 | **2 janvier 1986** |
| Loi n° 91-98, loi de finances pour la gestion 1992 | art. 102, p. 2093, image | création d'un établissement ; puis formule de promulgation | « Tunis, le 31 décembre 1991 » ; n° 90 du 31 décembre 1991 | **2 janvier 1992** |
| Loi organique n° 94-44 du 9 mai 1994 | article unique, p. 800, texte | récrit l'article 8 de la loi n° 75-35 ; aucune clause d'effet | « Tunis, le 9 mai 1994 » ; n° 38 du 17 mai 1994 | dépôt le 18 mai 1994 + cinq jours = **23 mai 1994** |

- Adresses : <https://www.pist.tn/jort/1981/1981F/Jo08481.pdf> (page 20 du PDF) ;
  <https://www.pist.tn/jort/1985/1985F/Jo09185.pdf> (page 13) ;
  <https://www.pist.tn/jort/1991/1991F/Jo09091.pdf> (page 13) ;
  <https://www.pist.tn/jort/1994/1994F/Jo03894.pdf> (loi : page 4 du PDF ; dépôt : page 31).
- Loi n° 94-44, mention du dépôt, lue à l'image (FR, 200 dpi) : « Ce numéro du Journal Officiel de
  la République Tunisienne a été déposé au siège du gouvernorat de Tunis le 18 Mai1994 ». L'édition
  arabe porte la même date (« يوم 18 ماي 1994 », vue à petite échelle). Note (1) de la loi :
  « Discussion et adoption par la chambre des députés dans sa séance du 3 mai 1994. »
- Pour 1982, le fascicule est daté « 29 - 31 décembre » : la parution est supposée au 31, jour de la
  signature. Les trois dates du 2 janvier sont **dérivées** ; « gestion 1982 / 1986 / 1992 » reste
  la formulation attestée par les lois elles-mêmes.

**État.** Derniers articles lus à l'image (1982, 1986, 1992) ; loi n° 94-44 en couche texte, son
dépôt à l'image.

**Ce que cela change au plan.** Les réserves « à contrôler sur le dernier article » de la note du
4 octobre (§ 2) sont levées : pas de clause, le calcul tient. `_budgets` : la loi n° 94-44 reçoit
sa date (23 mai 1994), que la note des budgets laissait « à établir ».

**Références.** Clés existantes `loi81-100-lf1982`, `loi85-109-lf1986`, `loi91-98-lf1992`,
`loi-org94-44` (ajouter aux `note` la page du dernier article et, pour 94-44, le dépôt).

---

## Q7. Fondement des 15 % de 2018-2019 ; nature de la « dotation annuelle » de 2022-2023

**Réponse.** Les 15 % correspondent, au million près, à la part « dépenses de développement et
besoins spécifiques et imprévus » que fixe l'article premier de l'arrêté conjoint du 22 juin 2018,
pris en application de l'article 11 de la loi de finances pour 2018 ; la « dotation annuelle » des
budgets de 2022 et 2023 porte le nom arabe de cette subvention annuelle, que l'article 13 de la loi
de finances pour 2021 maintient — pour 90 % des sommes — selon l'arrêté de 2018, modifié en 2019
puis le 29 juin 2021.

### a) Les trois arrêtés

| Texte | JORT | Pages | Adresse | État | Dépôt → exécutoire |
|---|---|---|---|---|---|
| Arrêté du ministre des finances et du ministre des affaires locales et de l'environnement du 22 juin 2018, fixant les critères de répartition des subventions annuelles du budget de l'État entre les collectivités locales | n° 51 du 26 juin 2018 | AR p. 3098 ; FR : édition absente (404) | <https://www.pist.tn/jort/2018/2018A/Ja0512018.pdf> (page 50 du PDF) | AR lu à l'image, en entier | 2 juillet 2018 (mention AR, lue à l'image, page 71 du PDF) → **7 juillet 2018** |
| Arrêté des mêmes ministres du 29 mars 2019, modifiant l'arrêté du 22 juin 2018 | n° 28 du 5 avril 2019 | FR p. 918-919 ; AR p. 1021 | <https://www.pist.tn/jort/2019/2019F/Jo0282019.pdf> (pages 30-31) | FR : dispositif lu à l'image (p. 919), visas en couche texte ; AR en couche texte | 6 avril 2019 (FR et AR) → **11 avril 2019** |
| Arrêté du ministre de l'économie, des finances et de l'appui à l'investissement et du ministre des affaires locales et de l'environnement du 29 juin 2021, portant modification de l'arrêté du 22 juin 2018 | n° 58 du 9 juillet 2021 | FR p. 1841-1842 ; AR p. 1926 (début) | <https://www.pist.tn/jort/2021/2021F/Jo0582021.pdf> (pages 39-40) | FR : dispositif lu à l'image (p. 1842) ; AR en couche texte | 9 juillet 2021 → **14 juillet 2021** |

Aucun des trois n'énonce de date d'effet. L'intitulé français de l'arrêté de 2018 est celui que lui
donnent les éditions françaises de 2019 et 2021 ; l'arabe dit « يتعلق بضبط مقاييس توزيع مبالغ الدعم
المالي السنوي من ميزانية الدولة بين الجماعات المحلية ». Tous trois visent « la loi n° 2017-66 […] et
notamment son article 11 » ; celui de 2021 vise en outre l'article 13 de la loi de finances pour
2021.

### b) La règle de partage, état par état

Pourcentages lus à l'image : arabe pour 2018, français pour 2021. Les libellés français de la
colonne 2018 reprennent ceux des éditions françaises de 2019 et 2021.

| Article de l'arrêté | Objet | 22 juin 2018 | 29 juin 2021 |
|---|---|---:|---:|
| 1er | part allouée aux dépenses de gestion | 85 % | 86,5 % |
| 1er | part allouée aux dépenses d'investissement (2018, AR : « نفقات التنمية ») et aux besoins spécifiques et imprévus | 15 % | 13,5 % |
| 2 | de la part de gestion : communes | 89 % | 90 % |
| 2 | de la part de gestion : conseils régionaux | 11 % | 10 % |
| 3 | des communes : à égalité entre toutes les communes | 10 % | 10 % |
| 3 | au prorata de la population | 40 % | 38 % |
| 3 | au prorata de la moyenne triennale des recettes de la taxe sur les immeubles bâtis | 31 % | 31 % |
| 3 | au prorata de la population, entre les communes dont la moyenne triennale (rôle de la taxe sur les immeubles bâtis, taxe sur les établissements, taxe hôtelière, marchés affermés) est inférieure à la moyenne nationale | 9 % | 9 % |
| 3 | « subvention d'équilibre » (« منحة توازن ») aux communes en difficulté financière, par décision conjointe | 10 % | 12 % |
| 4 | conseils régionaux : selon les besoins de gestion de chacun | décision conjointe des deux ministres | décision du seul ministre des affaires locales |
| 5 | de la part d'investissement : commune de Tunis | 25 % | 25 % (inchangé) |
| 5 | communes chefs-lieux des gouvernorats | 30 % | 29 % |
| 5 | caisse des prêts et de soutien des collectivités locales | 29 % | 27 % |
| 5 | « exigences de l'autorité centrale », besoins spécifiques et imprévus des collectivités et des établissements sous tutelle | 16 % | 19 % |

- Contrôle : chaque bloc somme à 100 dans les deux colonnes.
- Article 5, dernier tiret (2018 et 2021) : une partie de cette subvention peut être ajoutée au
  financement des dépenses de gestion des communes, par décision conjointe.
- **2021, article 2** — ajoute un paragraphe 2 à l'article 5 : « La commune de Tunis et les
  communes chefs-lieux des gouvernorats peuvent attribuer un montant de la subvention annuelle
  allouée au financement de l'investissement pour financer les dépenses de gestion par décision du
  ministre des affaires locales et de l'environnement. »
- **2019** — ne change aucun pourcentage : récrit les tirets 3 et 4 de l'article 3 pour déplacer
  les années de référence. 2018 (AR) : « خلال الثلاث سنوات الأخيرة » (les trois dernières années).
  2019 (AR) : « الثلاث سنوات ما قبل السنة الأخيرة » (les trois années qui précèdent la dernière) ;
  2019 (FR) : « au cours des trois précédentes années à l'année en cours ». **Les deux éditions de
  2019 ne disent pas la même chose** ; l'édition française est une traduction pour information.

### b bis) Depuis 2021 : le fonds de la loi de finances pour 2021, article 13

**Texte.** Loi n° 2020-46 du 23 décembre 2020, portant loi de finances pour l'année 2021,
article 13. JORT n° 128 du 25 décembre 2020 : FR p. 3125-3127 —
<https://www.pist.tn/jort/2020/2020F/Jo1282020.pdf> (pages 5 à 7 du PDF ; le fichier local a la
taille de celui de pist.tn, et c'est bien du français) ; AR p. 3376-3377. La note du 4 octobre
croyait l'édition française absente : elle existe. **Rubrique** : « Institution d'un fonds d'appui
à la décentralisation, de péréquation, de régularisation et de solidarité entre les collectivités
locales » (« إحداث صندوق دعم اللامركزية والتسوية والتعديل والتضامن بين الجماعات المحلية »).

**Ce qu'il dispose (FR lu à l'image, p. 3125-3127 ; AR p. 3376 à l'image).**
- § 1 : « Est créé un fonds spécial dénommé "Fonds d'appui à la décentralisation, de péréquation,
  de régularisation et de solidarité entre les collectivités locales " destiné à financer les
  budgets des collectivités locales. » Ordonnateur : le ministre chargé des collectivités locales ;
  compte spécial dans les écritures du trésorier général.
- § 2, ressources : « une subvention du budget de l'Etat fixée annuellement par la loi de
  finances » ; une proportion du produit des impôts de l'État ; « le produit de la taxe sur les
  établissements à caractère industriel, commercial ou professionnel qui dépasse au cours de
  l'année 100.000 dinars pour chaque établissement » ; le produit de la contribution aux travaux
  d'électrification et d'éclairage public ; le cas échéant une part des revenus des richesses
  naturelles ; toute autre ressource affectée.
- § 3, cinq sortes de crédits : forfaitaires, de régularisation, de péréquation, de bonification
  pour les communes comportant des zones rurales, exceptionnels et affectés.
- § 4 : critères (habitants, chômage, potentiel fiscal, indice de développement, capacité
  d'endettement), dont l'application est renvoyée à « un décret gouvernemental, conformément aux
  dispositions des articles 39, 61 et 150 du code des collectivités locales » ; répartition entre
  catégories : 70 % communes, 20 % régions, 10 % districts.
- **§ 5, le régime transitoire** : « Jusqu'à la promulgation du décret gouvernemental prévu par le
  paragraphe 4 du présent article, les textes réglementaires fixant les montants des subventions
  revenant aux collectivités locales et les critères et procédures de leur répartition restent en
  vigueur comme suit : - Une proportion de 90% au profit des collectivités locales au titre de la
  subvention financière annuelle, conformément à l'arrêté […] du 22 juin 2018 […] tel que modifié
  par l'arrêté du 29 mars 2019. - Une proportion de 10% au profit des collectivités locales au
  titre des ressources du fonds de coopération des collectivités locales, conformément au décret
  n° 2013- 2797 du 8 juillet 2013 ».
- § 6 : « Est supprimé le compte spécial de trésor intitulé "Fonds de coopération des collectivités
  locales" institué en vertu de l'article 13 de la loi n° 2012-27 du 29 décembre 2012 […]. Le solde
  de ses ressources est transféré au profit du fonds d'appui ».

**Date d'effet : 1er janvier 2021** — article 42, § 1 (FR p. 3138, couche texte) : « Sous réserve
des dispositions contraires prévues par la présente loi, les dispositions de la présente loi
s'appliquent à compter du 1er janvier 2021. »

**Trois conséquences.**
- Depuis 2021, la subvention annuelle n'est plus tout ce que l'État répartit par critères : elle
  est la part de 90 % d'un ensemble dont 10 % suivent les règles de l'ancien fonds de coopération.
  Le texte ne dit pas de quoi 90 et 10 sont les proportions ; la lecture naturelle est : des
  crédits du fonds. **À ne pas écrire plus précisément que la loi.**
- La taxe sur les établissements au-delà de 100 000 dinars par établissement alimente le fonds :
  ce point touche le chapitre des impôts sur l'activité (hors de ce ticket, à signaler à son
  rédacteur).
- L'arrêté du 29 juin 2021 est pris sous ce régime : il vise l'article 13 et modifie l'arrêté que
  le § 5 désigne.

**Le décret gouvernemental du § 4 : non identifié ici** (fiche proposée). **Et la suite, déjà au
backlog du précis** : le décret-loi n° 2026-4 du 30 septembre 2026 relatif aux conseils municipaux
(JORT n° 96 du 30 septembre 2026, édition arabe, article 134 lu à l'image ; p. 2074 d'après le pied de page en couche texte) maintient le fonds et le
renomme : « يتواصل العمل بصندوق دعم اللامركزية والتسوية والتعديل والتضامن بين الجماعات المحلية المحدث
بمقتضى الفصل 13 من القانون عدد 46 لسنة 2020 […] ويعوض اسمه بـ "صندوق التحويلات المالية للدولة
لفائدة الجماعات المحلية". يتم ضبط صيغ ومعايير وشروط توزيع موارد الصندوق بمقتضى قرار مشترك من
وزيري الداخلية والمالية. » Son article 136 diffère l'entrée en vigueur du décret-loi à la
proclamation des résultats des premières élections municipales qui suivront ; son article 139
abroge le code de 2018. Rien de cela n'est en vigueur au 9 octobre 2026 ; le chapitre le signale
au plus en une phrase, et `docs/notes/backlog-precis.md` porte déjà la tâche.

**Références.** Clé existante `lf-2021` (`precis/fr/references.json` ; ajouter à la `note` :
art. 13, FR p. 3125-3127, AR p. 3376-3377 ; art. 42, FR p. 3138). Décret-loi n° 2026-4 : notice à
créer par le chantier que suit le backlog, non ici.

### c) Les 15 % des données de la Direction générale

- Le classeur `fccl.xls` du portail s'intitule « Les subventions annuelles du budget de l'Etat
  entre les collectivités locales » : ce sont les mots de l'intitulé français de l'arrêté, mais le
  titre coiffe toute la série 2008-2019, années du fonds comprises ; il ne prouve rien pour 2018 à
  lui seul. La preuve est le calcul ci-dessous.
- Contrôle par le calcul, sur les valeurs publiées (MD) :

| Année | Crédit global | « Réserve » | Communes | Conseils régionaux | Réserve / global | Communes / global | Régions / global |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2018 | 440 | 66 | 333 | 41 | 15,0 % | 75,7 % | 9,3 % |
| 2019 | 480 | 72 | 363 | 45 | 15,0 % | 75,6 % | 9,4 % |
| Arrêté de 2018 | — | — | — | — | 15 % | 85 % × 89 % = 75,65 % | 85 % × 11 % = 9,35 % |

  Les trois parts de 2018 et 2019 sont, à l'arrondi du million près, celles de l'arrêté. Le
  rattachement de la colonne « la Reserve » aux 15 % de l'article premier est une **concordance
  calculée**, non une définition publiée : la Direction générale garde l'ancien libellé.
- Famille de sources : budgétaire (administration). Source : `tunisia-data`,
  `data/raw/finances_locales/dgct_portail/fccl.xls`, clé `dgct-donnees-ouvertes`.

### d) La « dotation annuelle » de 2022-2023

- Dans les budgets par commune de 2022 (`Budget2022_Recettes-1.xlsx`), l'article 6101 est libellé
  « المناب من الدعم السنوي » (« … بعنوان التسيير »), sous « تحويلات من ميزانية الدولة بعنوان
  التسيير » ; l'article 8002, « المناب من الدعم المالي السنوي بعنوان الاستثمار ». C'est le terme de
  l'arrêté et de l'article 13, § 5 : « الدعم المالي السنوي ».
- Le français du JORT est « **subvention annuelle** » (arrêtés de 2019 et 2021) ou « subvention
  financière annuelle » (loi de finances pour 2021) ; « dotation annuelle » est une traduction de
  l'entrepôt de données, non un terme du JORT.
- En droit, les budgets de 2022 et 2023 relèvent de l'article 13, § 5, de la loi de finances pour
  2021 et de l'arrêté de 2018 dans sa rédaction du 29 juin 2021 (86,5 / 13,5) — tant que le décret
  gouvernemental du § 4 n'a pas paru (fiche `r-fl-decret-fonds-appui-decentralisation`) et que
  l'arrêté n'a pas été modifié de nouveau (fiche `r-fl-criteres-subventions-apres-2021`).
- **Ce qui n'est pas établi** : que les articles 6101 et 8002 portent toute la subvention annuelle
  et rien qu'elle ; la part de 10 % répartie selon le décret n° 2013-2797 a pu être inscrite
  ailleurs, ou avec elle. Les 591 MD de 2022 et 611 MD de 2023 ne se comparent pas sans réserve aux
  440 et 480 MD de 2018-2019.

### e) Le changement de base en 2018

La part réservée aux communes dont les recettes sont inférieures à la moyenne ne se suit pas en un
seul pourcentage à travers 2018 :

| Période | Taux imprimé | Base du taux | En part du fonds, puis de la subvention annuelle (calcul) |
|---|---:|---|---:|
| 2001-2006 | 4 % | part des communes = 86 % de 75 % du fonds | 2,6 % |
| 2007-2013 | 4 % | part des communes = 86 % de 82 % du fonds | 2,8 % |
| 2014-2017 | 8 % | idem | 5,6 % |
| 2018-juillet 2021 | 9 % | part de gestion des communes = 89 % de 85 % des subventions | 6,8 % |
| depuis juillet 2021 | 9 % | 90 % de 86,5 % | 7,0 % |

La dernière colonne est un calcul de cette note. Depuis 2021, la subvention annuelle est elle-même
la part de 90 % visée à l'article 13, § 5 : toute part « du total » doit dire de quel total. S'y
ajoute en 2018 un instrument sans précédent dans la loi n° 75-36 : la subvention d'équilibre (10 %,
puis 12 %), répartie par décision.

**État.** Arrêtés lus (voir tableau a) ; article 13 de la loi de finances pour 2021 lu à l'image.
Concordance avec les données de 2018-2019 : calculée. Modificatif de l'arrêté postérieur au
29 juin 2021, et décret gouvernemental de l'article 13, § 4 : **non identifiés ici** (fiches
proposées).

**Ce que cela change au plan.**
- § 2.2 et § 2.4 : la section « Depuis 2018 » a sa règle et son tableau d'évolution ; l'état du
  droit s'écrit au 14 juillet 2021, par sa date.
- § 2.1 : ce qui succède au fonds en 2018, ce sont les subventions annuelles de l'arrêté ; le
  fonds que le code nomme (art. 148-150) n'est créé qu'au 1er janvier 2021, et il **entre dans le
  plan** : il est lu, il a sa date, et il encadre la subvention annuelle (b bis). La section
  « Depuis 2018 » a donc deux temps, 2018 puis 2021. Reste hors du plan le seul fonds de
  coopération de 2013, connu par son intitulé, par le décret n° 2013-2797 (non lu) et désormais
  par sa suppression au 1er janvier 2021.
- Section de la réserve : elle s'arrête au 31 décembre 2017. Après, trois des cinq lignes de 2014
  reparaissent à l'article 5 de l'arrêté — commune de Tunis, communes chefs-lieux, caisse des
  prêts — avec la ligne de la tutelle (25 / 30 / 29 / 16, à rapprocher des plafonds 24 / 30 / 27 /
  16 de 2014), mais sur une part de 15 % ; le conseil régional de Tunis (3 % en 2014) n'y figure
  plus.
- `_longue_periode` l. 146 et `fig-fl-lp-fccl` : les « points creux » de 2018-2019 se justifient
  par le changement de nature et de base, sourcé ; le libellé « réserve » ne vaut plus après 2017.
- Tableau fait main à prévoir pour la règle de 2018-2021, avec son `TODO (rédacteur)` ; le constat
  va à `docs/notes/backlog-modele.md`.

**Références à créer** (type `legislation`, `container-title` « Journal officiel de la République
tunisienne ») :

```json
[
  {"id": "arrete2018-criteres-subventions", "type": "legislation",
   "title": "Arrêté du ministre des finances et du ministre des affaires locales et de l'environnement du 22 juin 2018, fixant les critères de répartition des subventions annuelles du budget de l'État entre les collectivités locales",
   "container-title": "Journal officiel de la République tunisienne", "issue": "51", "page": "3098",
   "issued": {"date-parts": [[2018, 6, 22]]},
   "URL": "https://www.pist.tn/jort/2018/2018A/Ja0512018.pdf",
   "note": "citation-key: arrete2018-criteres-subventions\nJORT n° 51 du 26 juin 2018, ÉDITION ARABE, p. 3098 (page 50 du PDF). L'édition française de ce numéro n'est pas en ligne sur pist.tn (404 le 9 octobre 2026) ; intitulé français repris des arrêtés modificatifs de 2019 et 2021. Déposé le 2 juillet 2018, exécutoire le 7 juillet 2018."},
  {"id": "arrete2019-criteres-subventions", "type": "legislation",
   "title": "Arrêté du ministre des finances et du ministre des affaires locales et de l'environnement du 29 mars 2019, modifiant l'arrêté du ministre des finances et le ministre des affaires locales et de l'environnement du 22 juin 2018, fixant les critères de répartition des subventions annuelles du budget de l'Etat entre les collectivités locales",
   "container-title": "Journal officiel de la République tunisienne", "issue": "28", "page": "918-919",
   "issued": {"date-parts": [[2019, 3, 29]]},
   "URL": "https://www.pist.tn/jort/2019/2019F/Jo0282019.pdf",
   "note": "citation-key: arrete2019-criteres-subventions\nJORT n° 28 du 5 avril 2019, édition française p. 918-919, édition arabe p. 1021. Déposé le 6 avril 2019, exécutoire le 11 avril 2019."},
  {"id": "arrete2021-criteres-subventions", "type": "legislation",
   "title": "Arrêté du ministre de l'économie, des finances et de l'appui à l'investissement et du ministre des affaires locales et de l'environnement du 29 juin 2021, portant modification de l'arrêté du ministre des finances et du ministre des affaires locales et de l'environnement du 22 juin 2018, portant fixation des critères de répartition des subventions annuelles du budget de l'Etat entre les collectivités locales",
   "container-title": "Journal officiel de la République tunisienne", "issue": "58", "page": "1841-1842",
   "issued": {"date-parts": [[2021, 6, 29]]},
   "URL": "https://www.pist.tn/jort/2021/2021F/Jo0582021.pdf",
   "note": "citation-key: arrete2021-criteres-subventions\nJORT n° 58 du 9 juillet 2021, édition française p. 1841-1842, édition arabe p. 1926. Déposé le 9 juillet 2021, exécutoire le 14 juillet 2021."}
]
```

Les intitulés reprennent le fascicule (capitale de « Etat » comprise pour 2019 et 2021). Entrées
arabes : mêmes clés, adresses `2019A/Ja0282019.pdf` et `2021A/Ja0582021.pdf` (vérifiées).

---

## Q8. Définitions des ratios publiés par la Direction générale

**Réponse.** Non identifiées : la Direction générale publie les séries sous leur seul libellé, sans
formule ni note de méthode.

**Ce qui est publié.** Classeur `Ratios-financiers.xls`, feuille `ratios`, titre « Ratios
financiers », 2008-2019 ; colonnes, telles quelles : « Autonomie financiére », « Dotation de l'etat
et de subvention », « Rémunération », « % de réalisation des ressources propres », « % de
recouvrement de la taxe sur les immeubles bâtis ». Les classeurs jumeaux d'août 2020
(`Autonomie-Dotation.xlsx`, `Remunération.xlsx`, `taux-de-recouvrement-de-la-taxe-sur-les-immeubles-batis.xlsx`)
et la page « Indicateurs des finances locales » du portail redonnent les mêmes valeurs, sans
définition.

**Ce qui se constate, sans valoir définition** (`tunisia-data`, `sources/finances-locales-communes.md`) :
- « Autonomie financière » + « Dotation de l'État et de subvention » = 1, chaque année ;
- le ratio « Rémunération » se reconstitue par rémunérations / recettes du titre 1, à l'arrondi
  près (écart inférieur à 0,006) ;
- le ratio d'autonomie ne se reconstitue exactement par aucune des formules essayées (écart de
  0,06 en 2011).

**Repères voisins, à ne pas prendre pour la définition de ces séries.**
- Code de 2018, article 135 : plafond des rémunérations à la moitié des recettes du titre I — même
  rapport que le ratio reconstitué (déjà au chapitre).
- Rapport Essoussi (2020), p. 35 : pour 126 communes en 2018, la taxe sur les immeubles bâtis
  « n'a été recouverte qu'à hauteur de 13,21% des droits constatés » — un rapport recouvrements /
  droits constatés, proche des 12 % publiés pour 2018, sans que le rapport dise que c'est le même
  calcul. Famille : rapport commandé par l'administration, non budgétaire.

**État.** Non identifié. Adresses essayées le 9 octobre 2026 :
`http://www.collectiviteslocales.gov.tn/fr/مؤشرات-المالية-المحلية/` (200, lue : aucune définition) ;
`http://www.collectiviteslocales.gov.tn/fr/ratios-financiers/` (connexion refusée) ; une recherche
web. Pistes non ouvertes : l'étude « Les transferts financiers entre l'État et les collectivités
locales » de la bibliothèque du portail
(`bibliotheque.collectiviteslocales.gov.tn/pdf/Etude sur transferts financiers_Fr.pdf`) ; l'arrêté
du 29 décembre fixant les critères de l'évaluation annuelle des performances
(`…/wp-content/uploads/2015/06/criteres_valuation_annuelle_independante_performances_fr.pdf`), qui
définit un taux de recouvrement des ressources propres « par rapport aux montants budgétisés ».

**Ce que cela change au plan.** Rien : le chapitre continue de dire que la définition n'est pas
publiée, et s'en tient aux ratios qu'il calcule lui-même. Le libellé exact de la colonne est
disponible pour les légendes.

**Références.** Clé existante `dgct-donnees-ouvertes`.

---

## Recherches infructueuses : fiches proposées pour `docs/recherches.yml`

Je n'ai pas édité le registre. Les requêtes sont celles qui ont été lancées, rien de plus.

```yaml
- id: r-fl-criteres-subventions-apres-2021
  objet: arrêté modifiant ou remplaçant, après celui du 29 juin 2021, l'arrêté conjoint du 22 juin 2018 fixant les critères de répartition des subventions annuelles du budget de l'État entre les collectivités locales (loi de finances pour 2018, art. 11, § 3 ; loi de finances pour 2021, art. 13, § 5)
  ou: [precis/fr/finances_locales/_transferts.qmd#sec-fl-fccl-2018]
  requetes:
    titres_fts: [subventions AND annuelles AND budget AND collectivites]
    titres_like: ['%subventions annuelles du budget%', '%criteres de repartition%', '%مقاييس توزيع%', '%الدعم المالي السنوي%', '%مبالغ الدعم%']
    plein_texte: [subventions annuelles du budget, الدعم المالي السنوي]
    depuis: 2021-07-10
  passes:
  - date: 2026-10-09
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: 'titres FR et AR de jort_cache (FTS et LIKE) jusqu''à la dernière publication indexée, 2 octobre 2026 : seuls les arrêtés de 2019 et 2021. Plein texte par un script de circonstance (pdftotext, texte arabe normalisé, motifs fixes ; non par recherches.py) sur les fascicules FR et AR du corpus local, 2021 à 2026 jusqu''au n° 97 du 2 octobre 2026, 1 578 fichiers : les deux termes de la fiche, plus deux conditions composées (« 22 juin 2018 » et « critères de répartition » dans le même fascicule ; leur équivalent arabe). Seul le n° 58 de 2021 répond, dans les deux langues : le détecteur retrouve le positif connu. Lacunes : fascicules sans couche texte dans aucune édition présente, non lus — 2022 n° 35, 91, 92 ; 2024 n° 120, 125 ; 2025 n° 67, 70. Numéros absents du corpus, existence non vérifiée sur pist.tn — 2022 n° 132 ; 2023 n° 122 ; 2026 n° 58. Quatorze fichiers « fr » sont en fait l''édition arabe : pour eux seule l''édition arabe vaut. pist.tn non sondé. Une première tentative de balayage, au motif mal formé, n''a rien testé et n''est pas comptée. Note : docs/notes/finances-locales-transferts-budgets-lectures-2026-10-09.md, Q7.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire: [océriser 2022 n° 35 91 92 puis 2024 n° 120 125 puis 2025 n° 67 70, relancer --sonder-pist pour 2022 n° 132 et 2023 n° 122 et 2026 n° 58]

- id: r-fl-decret-fonds-appui-decentralisation
  objet: décret gouvernemental fixant les conditions d'application de la répartition des crédits du fonds d'appui à la décentralisation, de péréquation, de régularisation et de solidarité entre les collectivités locales (loi de finances pour 2021, art. 13, § 4 ; code des collectivités locales, art. 150)
  ou: [precis/fr/finances_locales/_transferts.qmd#sec-fl-fccl-2018]
  requetes:
    titres_fts: [decentralisation AND fonds]
    titres_like: ['%appui a la decentralisation%', '%perequation%', '%دعم اللامركزية%']
    plein_texte: ['appui à la décentralisation, de péréquation', صندوق دعم اللامركزية]
    depuis: 2020-12-25
  passes:
  - date: 2026-10-09
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: 'titres FR et AR de jort_cache jusqu''au 2 octobre 2026 : seule la notice de l''article 13 de la loi n° 2020-46 répond. Plein texte par le même script de circonstance sur les fascicules FR et AR de 2020 à 2026, jusqu''au n° 97 du 2 octobre 2026 : répondent le n° 128 de 2020 (la loi de finances pour 2021, FR et AR — positif connu retrouvé), le n° 9 de 2020 (décret gouvernemental n° 2020-52, nomenclature budgétaire des communes, qui nomme le fonds) et le n° 96 de 2026 (décret-loi n° 2026-4, art. 134, qui maintient et renomme le fonds et renvoie ses critères à un arrêté conjoint). Aucun décret d''application. Lacunes : les mêmes fascicules sans couche texte et numéros absents que la fiche r-fl-criteres-subventions-apres-2021 ; les tableaux des lois de finances de 2022 à 2026 ne répondent pas au nom du fonds, ce qui laisse penser qu''ils sont en image — non vérifié.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire: [océriser les fascicules sans couche texte, lire les tableaux des comptes et fonds spéciaux des lois de finances de 2021 à 2026 à l'image pour le montant du fonds]

- id: r-fl-debats-lois-2000-60-et-2007-65
  objet: exposé des motifs ou débats parlementaires de la loi n° 2000-60 du 13 juin 2000 (séance de la chambre des députés du 8 juin 2000) et de la loi organique n° 2007-65 du 18 décembre 2007 (séances des 12 et 15 décembre 2007), pour dire ce que ces lois cherchent
  ou: [precis/fr/finances_locales/_transferts.qmd#sec-fl-fccl-2001-2007, precis/fr/finances_locales/_budgets.qmd#sec-fl-budg-2007]
  requetes:
    depuis: 2000-06-08
  passes:
  - date: 2026-10-09
    role: documentaliste
    sources: [corpus_local, web]
    couverture: 'les deux lois lues au JORT (n° 48 de 2000, FR p. 1461, à l''image ; n° 103 de 2007, FR p. 4277-4281, couche texte) : ni exposé ni rubrique, seule la note des travaux préparatoires. Deux recherches web (l''une sur la loi organique n° 2007-65 et « recettes effectivement réalisées », l''autre sur la loi n° 2000-60 et le fonds commun) : aucun compte rendu de débats ni exposé des motifs. Lacunes : le journal des débats de la chambre des députés et de la chambre des conseillers n''est pas dans le corpus et n''a été cherché sur aucun site d''archives ; presse de juin 2000 et de décembre 2007 non consultée ; édition arabe des deux lois non relue.'
    couvert_jusqu_au: 2007-12-25
    resultat: aucun
  a_faire: [chercher les débats parlementaires (مداولات مجلس النواب) des séances du 8 juin 2000 et des 12 et 15 décembre 2007 dans les archives en ligne, presse des mêmes dates]

- id: r-fl-dgct-definitions-ratios
  objet: définition ou note de méthode des ratios publiés par la Direction générale des collectivités locales (autonomie financière, dotation de l'État et subvention, rémunération, réalisation des ressources propres, recouvrement de la taxe sur les immeubles bâtis), 2008-2019
  ou: [precis/fr/finances_locales/_budgets.qmd#sec-fl-lp-autonomie]
  requetes:
    depuis: 2008-01-01
  passes:
  - date: 2026-10-09
    role: documentaliste
    sources: [web]
    couverture: 'classeurs du portail déjà rangés dans tunisia-data (Ratios-financiers.xls, Autonomie-Dotation.xlsx, Remunération.xlsx, taux-de-recouvrement…xlsx) : libellés seuls. Page « Indicateurs des finances locales » du portail, lue le 9 octobre 2026 : aucune définition. Page /fr/ratios-financiers/ : connexion refusée. Une recherche web. PDF de tunisia-data cherchés sur « autonomie financière » et « taux de recouvrement » (étude DGCT 2018, rapports de la Haute instance 2020, étude de recouvrement 2023, rapport Essoussi) : aucune définition de ces séries. Lacunes : étude « transferts financiers » de la bibliothèque du portail et arrêté sur l''évaluation annuelle des performances non ouverts ; archives du web non consultées.'
    couvert_jusqu_au: 2026-10-09
    resultat: aucun
  a_faire: [ouvrir l'étude sur les transferts financiers de la bibliothèque du portail, archives du web de la page des indicateurs]
```

Les ancres du champ `ou` sont celles que le plan de l'architecte prévoit ; à ajuster aux
identifiants réels des sections après conversion. Les deux dernières fiches n'ont pas de requête
rejouable sur le JORT : leur objet n'y paraît pas. À l'architecte ou au propriétaire de dire si
elles ont leur place au registre ou si un `TODO (documentaliste)` suffit.

La fiche existante `r-fccl-repartition-reserve-2014-2017` n'a pas été rejouée (hors ticket).

## Trouvé en passant : la nomenclature budgétaire des communes (hors des huit questions)

Le balayage plein texte sur le nom du fonds a fait sortir un texte que la fiche existante
`r-ccl-2018-nomenclature-art167` cherche (« décret gouvernemental fixant la nomenclature des
budgets (art. 167) ») et que sa requête sur les titres a manqué — l'intitulé dit « nomenclature
budgétaire des communes », non « collectivités ».

- **Décret gouvernemental n° 2020-52 du 23 janvier 2020, portant approbation du modèle de la
  nomenclature budgétaire des communes.** JORT n° 9 du 31 janvier 2020, FR p. 367-368 —
  <https://www.pist.tn/jort/2020/2020F/Jo0092020.pdf> (200, même taille que le fichier local).
- Lu en couche texte, FR : « Article premier - Est approuvé le modèle annexé au présent décret
  gouvernemental relatif à la nomenclature budgétaire des communes(1). » ; note (1) : « Le modèle
  relatif à la nomenclature budgétaire des communes est publié uniquement en langue arabe. »
  L'édition arabe vise les articles 155, 159, 167 et 383 du code (couche texte).
- Sans clause d'effet ; fascicule déposé le 1er février 2020 (mention française, couche texte) :
  exécutoire le **6 février 2020**.
- **Non lu** : le modèle lui-même (édition arabe, autour de la p. 374). C'est lui qui porte les
  articles 6101 et 8002 des budgets de 2022-2023 et les lignes « المبالغ المتأتية من صندوق دعم
  اللامركزية… » ; il peut trancher la lacune 4.
- Je n'ai ni rejoué ni modifié la fiche. Proposition : `passe r-ccl-2018-nomenclature-art167`
  avec ce texte pour la nomenclature (art. 167), l'objet restant ouvert pour les missions et
  programmes (art. 156) et le système comptable (art. 191) ; clé suggérée `decret-gouv2020-52`.
  `_budgets.qmd` (section de la nomenclature) est concerné.

## Notions à glossaire

- **Subvention annuelle du budget de l'État (aux collectivités locales)** : الدعم المالي السنوي من
  ميزانية الدولة (arrêté du 22 juin 2018, AR ; FR : arrêtés de 2019 et 2021). Succède au fonds
  commun le 1er janvier 2018. Remplace « dotation annuelle » dans le texte.
- **Subvention d'équilibre** : منحة توازن (arrêté de 2018, art. 3 ; FR : arrêté de 2021).
- **Fonds d'appui à la décentralisation, de péréquation, de régularisation et de solidarité entre
  les collectivités locales** : صندوق دعم اللامركزية والتسوية والتعديل والتضامن بين الجماعات المحلية
  (loi de finances pour 2021, art. 13, FR et AR). Le nom français, que la note du 4 octobre donnait
  « à vérifier », est attesté ; l'ordre des termes diffère entre les deux langues. Le code de 2018
  écrit le nom sans « والتسوية » à l'article 148 (image), avec ce mot ailleurs (couche texte).
- **Fonds de coopération des collectivités locales** : forme française du JORT (loi de finances
  pour 2021, art. 13, § 5 et 6), à préférer à « fonds de coopération entre les collectivités ».
- **Fonds commun des collectivités publiques locales** : variante du nom en 2017 (loi de finances
  pour 2018, art. 11, FR) ; AR حساب المال المشترك للجماعات العموميّة المحليّة.
- **Communes chefs-lieux des gouvernorats** (FR 2021) = « communes sièges des gouvernorats » (FR
  1992) : البلديات مراكز الولايات. Un seul terme à retenir.
- **Reliquat (du fonds)** : بقايا موارده — à distinguer de la **réserve**, المدّخر.

## Lacunes

1. Éditions arabes non lues : loi de finances pour 1987 (art. 92), loi de finances pour 1992
   (art. 80), décret n° 92-308 ; loi n° 2000-60 et loi organique n° 2007-65 non relues en arabe.
2. Édition française du JORT n° 51 de 2018 et du n° 39 de 2018 : absentes de pist.tn et du corpus.
3. Jour exact de parution des fascicules datés sur plusieurs jours (1981, 1986) : supposé le 31.
4. Décret n° 2013-2797 (fonds de coopération), que l'article 13, § 5, de la loi de finances pour
   2021 maintient pour 10 % : non lu. Base exacte des proportions de 90 % et 10 % : non dite par la
   loi. Contenu des articles 6101 et 8002 des budgets de 2022-2023 au regard de ces deux parts :
   non établi.
5. Montant annuel des subventions dans les lois de finances de 2018 et suivantes : non relevé (les
   440 et 480 MD viennent de la Direction générale).
