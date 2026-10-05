# Volume VII « Les finances locales », chapitre 5 : note documentaire sur les budgets et les comptes

> Note du documentaliste, 5 octobre 2026. Elle sert le chapitre 5 du plan
> (`docs/notes/fiscalite-locale-plan.md`) : nomenclature, procédure, équilibre, endettement,
> tutelle et contrôle des budgets des collectivités locales. Rien n'y est rédigé pour le précis.
>
> **Sources.** Les textes ont été lus dans le *Journal officiel*, fascicules du corpus local
> (`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`). Métadonnées : `jort_cache.db` (dernière
> publication indexée : 18 septembre 2026). Les fascicules français antérieurs à 1994 n'ont pas de
> couche texte : la loi n° 75-35, la loi n° 75-37, les décrets n° 75-485 et 75-782 et la loi
> organique n° 85-44 ont été **lus à l'image** (rendu 200-400 dpi) ; les décrets n° 77-320,
> 86-1036, 89-280 et la loi n° 79-66 (art. 35-41) ont été lus sur une **océrisation**
> (`ocrmypdf`/`tesseract`, au premier plan), chaque montant y étant écrit en lettres et en chiffres
> concordants — à relire à l'image avant publication d'un tableau (voir Lacunes). Les fascicules de
> 1994 et suivants ont une couche texte, lue directement.
>
> **Code des collectivités locales (2018).** Édition arabe seule (JORT n° 39 du 15 mai 2018,
> `Ja0392018.pdf`, 120 p.). Le texte a été lu dans la couche texte du fascicule et dans le miroir
> iort (`data/iort/textes/md/loi_org_2018_29_2018.md`) ; **le miroir saute des articles** (les
> art. 140, 141 et 143 n'y figurent pas) : il ne sert que de repère. La p. 1725 (art. 128-135) a été
> contrôlée à l'image. Les pages données pour les autres articles sont tirées des pieds de page de
> la couche texte (deux colonnes : écart possible d'une page) — à vérifier à l'image. Les
> traductions françaises de passages du code sont les nôtres.
>
> **Dates d'effet.** Règle « Dater » d'AGENTS.md. Depuis 1993 : dépôt au gouvernorat de Tunis
> + 5 jours, jour du dépôt non compté (loi n° 93-64, art. 2), la date de dépôt étant relevée sur la
> mention de dernière page du fascicule. Avant 1993 : un jour franc après la publication ; les dates
> de publication de ces textes sont celles de `jort_cache` sauf mention « en-tête relu », et restent
> à contrôler au fascicule (`outillage-sources.md`, § 3 bis).
>
> **URL.** Les champs `pdf_fr` et `pdf_ar` de `jort_cache` ont été testés le 5 octobre 2026
> (`curl -sk`, 200 `application/pdf`) pour : 1975 n° 34, 52 (FR), 74 (FR) ; 1985 n° 34 ; 2007
> n° 103 ; 2008 n° 28 (FR) ; 2010 n° 101 (FR) ; 2017 n° 49 ; 2018 n° 39 (AR) ; 2025 n° 30. Les
> autres sont lues dans la base et non testées.

## 1. La loi organique du budget de 1975

### 1.1 Texte initial

- **Loi n° 75-35 du 14 mai 1975, portant loi organique du budget des collectivités publiques
  locales.** Titre arabe (2025, art. 8 de la loi organique n° 2025-4) : القانون الأساسي لميزانية
  الجماعات المحلية ; intitulé initial (iort) : القانون الأساسي لميزانية الجماعات العمومية المحلية.
  - JORT n° 34 du **20 mai 1975**, p. 1065-1067 (en-tête relu, édition française, pages 11 à 13 du
    PDF). Adoptée par l'Assemblée nationale le 9 mai 1975 (note (1)).
  - FR : https://www.pist.tn/jort/1975/1975F/Jo03475.pdf — AR : https://www.pist.tn/jort/1975/1975A/Ja03475.pdf
  - jort_cache recid 116141. Clé proposée : `loi75-35`.
  - **Date d'effet : 1er janvier 1976** (art. 28 : « La présente loi prendra effet à compter du
    1er janvier 1976 »).
- **Plan** : chapitre I « Des charges et des ressources des collectivités publiques locales »
  (art. 1-11) ; chapitre II « De la préparation, du vote et de l'approbation du budget »
  (art. 12-20) ; chapitre III « Exécution et règlement du budget » (art. 21-28).
- **Art. 1** : le budget « prévoit et autorise pour chaque année l'ensemble des charges et des
  ressources » ; forme et nomenclature fixées par arrêté conjoint des ministres de l'Intérieur et
  des Finances ; nomenclature simplifiée pour les collectivités dont le budget est approuvé selon
  le § 3 de l'art. 13.
- **Art. 2** : année budgétaire du 1er janvier au 31 décembre, sous réserve de l'art. 3 du code de
  la comptabilité publique.
- **Art. 3** : deux titres, titre I « dépenses et recettes courantes », titre II « dépenses et
  recettes en capital ». **« Chaque titre doit être équilibré en recettes et en dépenses. »**
- **Art. 4** : dépenses courantes en six chapitres — I intérêts de la dette ; II rémunération du
  personnel ; III autres moyens des services ; IV interventions dans les domaines économique, social
  et culturel ; V contribution du titre I aux dépenses du titre II ; VI dépenses diverses et
  imprévues.
- **Art. 5** : recettes courantes en six chapitres — I impôts directs et taxes assimilées ;
  II impôts et taxes indirects ; **III quotes-parts sur le fonds commun** ; IV revenus du domaine ;
  V recettes en atténuation des services rendus ; VI recettes accidentelles et diverses.
- **Art. 6** : dépenses en capital en deux sections, I sur ressources propres (chapitres :
  investissements directs ; opérations financières ; amortissement de la dette), II sur crédits
  délégués.
- **Art. 7** : recettes en capital en deux sections, I ressources propres, II ressources provenant
  des crédits délégués. Les ressources propres proviennent de la contribution du titre I, du
  produit des emprunts, des subventions d'équipement de l'État ou d'organismes publics, du
  prélèvement sur le fonds de réserve, de recettes diverses. *L'emprunt figure donc parmi les
  « ressources propres » du titre II.*
- **Art. 8** : crédits de programme, d'engagement et de paiement ; appliqués progressivement, d'abord
  aux collectivités dont le budget est approuvé selon l'art. 13 § 2.
- **Art. 9** : crédits d'engagement valables sans limitation de durée ; crédits de paiement non
  utilisés annulés.
- **Art. 10, dépenses obligatoires** (7 points) : entretien de l'hôtel de ville ; conservation des
  actes ; rémunération du personnel ; installation et entretien des édifices ; « l'acquittement des
  dettes exigibles et des annuités d'emprunts » ; entretien des voies, aqueducs, égouts, etc. du
  domaine public local ; toute dépense mise à leur charge par la loi ou le règlement.
- **Art. 11** : liste des taxes et droits du budget de fonctionnement (13 points : taxe sur la
  valeur locative — décret du 16 septembre 1902 ; taxes d'entretien et d'assainissement — décret
  du 21 avril 1920 ; taxe de compensation — décret du 4 septembre 1947 (lecture incertaine) ;
  contribution foncière sur les non-bâtis — décret du 15 décembre 1919 ; droit de licence — décrets
  du 14 décembre 1935 et 29 mars 1956 (lecture incertaine) ; taxe sur les véhicules à traction
  animale — décret du 15 janvier 1914 ; taxe sur les spectacles — décret de finances du 1er janvier
  1951 ; droit sur les peaux — décret du 30 décembre 1919 ; taxes pour formalités administratives ;
  taxes d'occupation du domaine public ; redevances pour services rendus ; taxe hôtelière de la loi
  n° 75-34 ; toute autre recette créée par la loi). Plusieurs renvois à l'art. 5 de la « loi n° 58-44
  du 31 mars 1958 ». *Utile au chapitre d'histoire (renvoi) ; dates à relire en meilleure image
  avant de les publier.*
- **Art. 12** : projet proposé par le président, examiné en commission, voté par le conseil ; vote
  par chapitres et par articles ; transmission aux autorités de tutelle **au plus tard le 31 octobre**,
  avec un rapport de présentation et les pièces justificatives.
- **Art. 13, approbation des budgets communaux** : par le **gouverneur**, sauf : § 1 par les
  ministres de l'Intérieur et des Finances si le compte de la dernière gestion close est en déficit
  non apuré ; § 2 par les mêmes ministres si les prévisions de recettes courantes et en capital de
  la gestion précédente atteignent un montant fixé par décret ; § 3 par le **délégué** de la
  circonscription si elles sont inférieures à un montant fixé par décret.
- **Art. 14** : budgets des conseils de gouvernorat approuvés par le ministre de l'Intérieur.
- **Art. 15** : tout projet d'investissement égal ou supérieur à un montant fixé par décret ne peut
  être inscrit qu'après agrément conjoint des ministres de l'Intérieur et des Finances (avis sous
  trois mois, sinon réputé approuvé).
- **Art. 16** : « Les autorisations de dépenses et les prévisions de recettes doivent être
  présentées et votées en **équilibre réel** compte tenu des engagements de la gestion précédente. »
- **Art. 17** : budget non voté en équilibre → renvoi pour seconde délibération sous quinze jours ;
  à défaut, l'autorité de tutelle **arrête d'office** dépenses et recettes.
- **Art. 18** : l'autorité de tutelle peut rejeter ou réduire les dépenses, non les augmenter ni en
  introduire, sauf obligatoires.
- **Art. 19** : inscription d'office des dépenses obligatoires (moyenne des trois dernières années
  pour une dépense annuelle variable) ; à défaut de ressources, création de ressources par
  l'autorité compétente.
- **Art. 20** : budget non arrêté au 1er janvier → recettes et dépenses obligatoires de
  fonctionnement du dernier budget continuent d'être exécutées.
- **Art. 21-23** : modification en cours d'année si excédent prévisible ; transferts de chapitre à
  chapitre sous approbation de la tutelle ; virements ; dépenses imprévues.
- **Art. 24** : déficit de la dernière gestion close et mesures insuffisantes → invitation à
  délibérer sous quinze jours ; à défaut, les ministres de l'Intérieur et des Finances arrêtent
  d'office le budget, sans pouvoir créer d'impositions nouvelles.
- **Art. 25** : le **compte financier**, établi selon un article du code de la comptabilité publique
  (« 232 » à l'image, lecture incertaine ; Dafflon et Gilbert citent l'art. 282 pour le texte
  reclassé, p. 70), est examiné par le conseil **à sa session de mai** et approuvé par l'autorité de
  tutelle.
- **Art. 26** : l'arrêté de règlement constate encaissements et ordonnancements, annule les crédits
  sans emploi, porte le résultat au **« Fonds de réserve »**, utilisable pour l'équipement ou pour
  résorber un déficit.
- **Art. 27, abrogations** : « les dispositions budgétaires du décret du 23 novembre 1937 » (année
  lue « 1937 » ou « 1977 » — 1937 seul vraisemblable, à confirmer sur l'arabe) ; la loi n° 61-12 du
  27 mai 1961 (le fascicule porte un numéro mal lisible ; `jort_cache` donne **61-12**, « portant
  fixation, pour les budgets des communes et organismes assimilés, de la date d'ouverture de
  l'exercice financier et de sa période complémentaire », JORT n° 21 de 1961, p. 720) ; les art. 11,
  12, 15, 19, 20 et 21 de la **loi n° 63-54 du 30 décembre 1963, relative aux conseils de
  gouvernorat** (JORT n° 60 de 1963, p. 1873-1875).

### 1.2 Modifications avant 2007

| Texte | JORT | Objet | Date d'effet |
|---|---|---|---|
| Loi n° 79-66 du 31 décembre 1979 (LF 1980), art. 38-41 | n° 76 du 28-31 décembre 1979, p. 3546-3547 (OCR) | art. 4 : dépenses courantes en 5 « parties » (indemnités de représentation ; intérêts de la dette ; moyens des services ; interventions publiques ; dépenses diverses et imprévues) ; art. 12 : vote « par parties et par articles » ; art. 22 : transferts de partie à partie ; art. 23 | à établir (clause générale de la LF non lue) |
| Loi organique n° 85-44 du 25 avril 1985 | n° 34 du 30 avril 1985 (cache), p. 644 (image) | art. 13 récrit : approbation par le gouverneur, sauf déficit non apuré ou recettes ≥ montant fixé par décret (ministres) ; **le § 3 (délégué) disparaît** | 2 mai 1985 (jour franc, date de publication du cache) |
| Loi organique n° 94-44 du 9 mai 1994 | n° 38 du 17 mai 1994, p. 800 (texte) | art. 8 récrit : crédits de programme, d'engagement, de paiement, adoptés pour les conseils régionaux et pour les communes de l'art. 13 al. 2 | dépôt non relevé (mention absente de la couche texte) — à établir |
| Loi organique n° 97-1 du 22 janvier 1997 | n° 7 du 24 janvier 1997, p. 114 (texte) | art. 11 récrit : budget de fonctionnement alimenté par « les taxes et redevances instituées par le code de la fiscalité locale » et toute ressource instituée ou affectée par la loi | dépôt 28 janvier 1997 → **2 février 1997** |

Liste confirmée par le visa de la loi organique n° 2007-65 (art. 1er : « telle que modifiée par la
loi n° 79-66 du 31 décembre 1979, la loi organique n° 85-44 du 25 avril 1985, la loi organique
n° 94-44 du 9 mai 1994 et la loi organique n° 97-01 du 22 janvier 1997 »). N. B. : l'encadré 2 de
Dafflon et Gilbert (2018, p. 63) imprime « Loi organique 99-44 du 9 mai 1994 » : coquille pour 94-44.

Clés proposées : `loi79-66-lf1980` (vérifier qu'une clé n'existe pas déjà pour la LF 1980 :
`loi79-66-lf1980` figure dans precis/fr/references.json — **existe déjà**, à réutiliser),
`loi-org85-44`, `loi-org94-44`, `loi-org97-1`.

### 1.3 La refonte de 2007

- **Loi organique n° 2007-65 du 18 décembre 2007, modifiant et complétant la loi n° 75-35 du
  14 mai 1975 relative à la loi organique du budget des collectivités publiques locales.**
  - JORT n° 103 du **25 décembre 2007**, p. 4277-4281 (FR, couche texte). Dépôt : **27 décembre
    2007**. Adoptée par la Chambre des députés le 12 décembre et par la Chambre des conseillers le
    15 décembre 2007.
  - FR : https://www.pist.tn/jort/2007/2007F/Jo1032007.pdf — AR : https://www.pist.tn/jort/2007/2007A/Ja1032007.pdf
  - Avis du Conseil constitutionnel n° 66-2007, même fascicule, p. 4284-4285 (titre seul lu).
  - Clé proposée : `loi-org2007-65`.
  - **Date d'effet** : art. 6 : « Les dispositions de la présente loi s'appliquent au budget des
    collectivités locales de l'année 2008 et aux budgets subséquents. » Exécutoire le 1er janvier
    2008 (dépôt 27 décembre + 5 jours) ; applicable aux budgets à partir de **2008**.
- **Contenu** (articles dans la numérotation de 2007, avant reclassement) :
  - art. 1er : le budget prévoit et autorise charges et ressources « dans le cadre des objectifs du
    plan de développement économique et social » ;
  - art. 3 : titre I = dépenses de gestion et intérêts de la dette ; titre II = développement,
    remboursement du principal, dépenses sur crédits transférés ; **onze parties** de dépenses,
    **douze catégories** de ressources ;
  - art. 4 : titre I, parties 1 rémunération publique, 2 moyens des services, 3 interventions
    publiques, 4 dépenses de gestion imprévues et non ventilées, 5 intérêts de la dette ; sections 1
    (parties 1-4) et 2 (partie 5) ;
  - art. 5 : ressources du titre I, catégories 1 « taxes foncières et taxes sur les activités »,
    2 revenus d'occupation et de concession, 3 redevances pour formalités administratives et droits
    perçus en atténuation de services rendus, 4 autres recettes fiscales ordinaires, 5 revenus
    ordinaires du domaine, 6 revenus financiers ordinaires ; section 1 « recettes fiscales
    ordinaires » = catégories 1 à 4, section 2 « recettes non fiscales ordinaires » = 5 et 6 ;
  - art. 6 : titre II, parties 6 investissements directs, 7 financement public, 8 dépenses de
    développement imprévues, 9 dépenses liées à des ressources extérieures affectées,
    10 remboursement du principal, 11 dépenses sur crédits transférés ; sections 3 (6-9), 4 (10),
    5 (11) ;
  - art. 7 : ressources du titre II, catégories 7 subventions d'équipement, 8 réserves et ressources
    diverses, 9 emprunt intérieur, 10 emprunt extérieur, 11 emprunt extérieur affecté, 12 crédits
    transférés ; sections 3 (ressources propres destinées au développement : 7-8), 4 (emprunt :
    9-11), 5 (crédits transférés : 12) ;
  - art. 7 bis : budget par programmes et missions possible, fixés par décret ;
  - art. 10 : dépenses obligatoires (rémunération, retenues fiscales et sociales comprises ;
    nettoiement et entretien des rues, trottoirs, éclairage, assainissement, espaces verts ;
    annuités d'emprunt en principal et intérêts ; dettes exigibles ; conservation des actes ;
    entretien du siège et des ouvrages ; dépenses imposées par la loi) ;
  - art. 12 : projet préparé par le président **avant fin mai**, voté **à la troisième session** ;
    à défaut, préavis du gouverneur, délibération avant fin août ; transmission à la tutelle
    **avant le 31 octobre** ; à défaut, préavis, puis budget **arrêté d'office** sur la base des
    réalisations, dépenses obligatoires inscrites ;
  - art. 12 bis : dépenses prévues sur la base des recettes prévisibles et des excédents probables
    reportés ; art. 12 ter : vote des dépenses par section, partie, article ; des recettes par
    section et catégorie ;
  - art. 14 bis : discussion du projet avec la tutelle **en novembre** ; actualisation sous quinze
    jours ;
  - art. 20 : budget non arrêté au 1er janvier → douzièmes (« quota mensuel ») sur autorisation du
    ministre de l'Intérieur (conseil régional) ou du gouverneur (commune) ;
  - art. 21 bis : « Le montant total des dépenses ordonnancées doit être limité aux recettes
    effectivement réalisées » ;
  - art. 23 bis : engagements du titre I plafonnés aux recettes effectivement réalisées du titre I ;
    violation = **faute de gestion**, responsabilité civile des ordonnateurs ;
  - art. 23 ter : interdiction des bons de commande manuels là où existe le système informatique ;
  - art. 24 : déficit → délibération sous quinze jours, sinon budget arrêté d'office par les
    ministres de l'Intérieur et des Finances ;
  - art. 26 : arrêté de règlement ; résultat porté au « Fonds de réserve » (titre I, sections 3 et 4)
    et au « Compte de transit » (section 5) ; compte financier transmis à la tutelle.
  - art. 2 : le mot « publiques » disparaît de l'intitulé (« loi organique du budget des
    collectivités locales »).
  - **art. 4 : reclassement** de tous les articles. Correspondances utiles : ancien 13 → **16**
    (approbation des budgets communaux) ; 12 → 13 ; 12 bis → 14 ; 12 ter → 15 ; 14 → 17 ; 15 → 19 ;
    16 → 20 (équilibre réel) ; 19 → 23 ; 21 bis → 26 ; 23 bis → 30 ; 24 → 32 ; 25 → 33 (compte
    financier) ; 26 → 34 ; 27 → 35 ; 10 → 12 (dépenses obligatoires). Les décrets d'application
    de l'ancien art. 13 visent donc, à partir de 2010, « le 2e sous-paragraphe de l'article 16 ».
- **Nomenclature** : arrêté conjoint des ministres de l'Intérieur et du Développement local et des
  Finances du **31 mars 2008**, fixant la forme et la nomenclature des budgets des collectivités
  locales, JORT n° 28 du 4 avril 2008, p. 1141-1142 (dépôt 5 avril 2008 → exécutoire **10 avril
  2008**) : modèle n° 1 (communes approuvées par le gouverneur), n° 2 (communes approuvées par les
  deux ministres), n° 3 (conseils régionaux) ; les modèles sont publiés « en une édition spéciale
  en langue arabe » (non lue) ; abroge l'arrêté du 6 novembre 1975 (JORT n° 74 de 1975, p. 2386,
  titre seul). Arrêté propre aux conseils régionaux : 11 mai 1991, JORT n° 39 de 1991, p. 1080-1081
  (titre seul). Clé proposée : `arrete2008-03-31-nomenclature`.

### 1.4 La tutelle d'approbation : seuils fixés par décret (série datée)

L'art. 13 (16 après 2007) renvoie à un décret le montant de recettes à partir duquel le budget
communal est approuvé conjointement par les ministres de l'Intérieur et des Finances, et non par
le gouverneur. Série complète, chaque décret abrogeant le précédent :

| Décret | JORT | Approbation par les ministres si recettes ≥ | Gouverneur | Délégué | Assiette | Exécutoire |
|---|---|---|---|---|---|---|
| n° 75-485 du 26 juillet 1975 | n° 52 du 29 juillet 1975 (en-tête relu), p. 1593 — image | 500 000 D | 75 000 à 500 000 D | < 75 000 D | prévisions de recettes courantes et en capital de la gestion précédente | 31 juillet 1975 (jour franc) ; la loi prend effet le 1er janvier 1976 |
| n° 77-320 du 1er avril 1977 | n° 23 du 5 avril 1977, p. 834 — OCR | 1 000 000 D | 75 000 à 1 000 000 D | < 75 000 D (art. 3, chiffre non lu en entier) | idem | 7 avril 1977 |
| (loi organique n° 85-44) | n° 34 de 1985, p. 644 | — | tous les autres budgets | supprimé | — | 2 mai 1985 |
| n° 86-1036 du 30 octobre 1986 | n° 64 du 7 novembre 1986, p. 1252 — OCR | 1 000 000 D | — | — | **recettes courantes réalisées** de la gestion précédente | 9 novembre 1986 |
| n° 89-280 du 10 février 1989 (cache : 19 février) | n° 13 du 21 février 1989, p. 285 — OCR | 2 000 000 D | — | — | prévisions de recettes courantes | **1er janvier 1989** (art. 3, clause d'effet expresse, relu à l'image le 5 octobre 2026) |
| n° 97-1837 du 15 septembre 1997 | n° 77 du 26 septembre 1997, p. 1808 (dépôt 27 sept.) | 4 000 000 D | — | — | prévisions de recettes courantes | 2 octobre 1997 |
| n° 2010-3179 du 13 décembre 2010 | n° 101 du 17 décembre 2010, p. 3415 (dépôt 18 déc.) | 6 000 000 D | — | — | idem | 23 décembre 2010 |
| n° 2012-2475 du 16 octobre 2012 | n° 84 du 23 octobre 2012, p. 2590-2591 (dépôt 24 oct.) | 8 000 000 D | — | — | idem | 29 octobre 2012 |
| n° 2013-3235 du 2 août 2013 | n° 67 du 20 août 2013, p. 2447-2448 (dépôt 22 août) | 10 000 000 D | — | — | idem | 27 août 2013 |
| n° 2014-2232 du 16 juin 2014 | n° 50 du 24 juin 2014, p. 1623-1624 (dépôt 26 juin) | 12 000 000 D | — | — | idem | 1er juillet 2014 |
| gouv. n° 2015-1739 du 10 novembre 2015 | n° 91 du 13 novembre 2015, p. 2704-2705 (dépôt 14 nov.) | 14 000 000 D | — | — | idem | 19 novembre 2015 |
| gouv. n° 2017-758 du 13 juin 2017 | n° 49 du 20 juin 2017, p. 2207 (dépôt 21 juin) | 18 000 000 D | — | — | idem | 26 juin 2017 |

Notes :
- Le décret n° 97-1837 vise le décret n° 89-280 « du 10 février 1989 », comme le titre océrisé du
  décret lui-même ; `jort_cache` donne le 19 février. Retenir le 10 février, sous réserve de la
  relecture à l'image.
- Le décret n° 77-320 vise un décret « n° 75-485 du 28 juillet 1965 » : coquille du fascicule.
- Tous les décrets reprennent aussi le cas du déficit non apuré (jusqu'en 1997), puis seulement le
  seuil (à partir de 2010, le cas du déficit étant dans la loi).
- Signataires : ministres de l'Intérieur et des Finances, puis (2017) ministre des Affaires locales
  et de l'Environnement et ministre des Finances.
- Aucun décret postérieur au décret gouvernemental n° 2017-758 n'est identifié (requêtes au § 6).
- Clés proposées : `decret75-485`, `decret77-320`, `decret86-1036`, `decret89-280`,
  `decret97-1837`, `decret2010-3179`, `decret2012-2475`, `decret2013-3235`, `decret2014-2232`,
  `decret2015-1739`, `decret2017-758` (URL : champs `pdf_fr`/`pdf_ar` de chaque recid, § 7).
- **Ce tableau est une série de seuils, non une série de valeurs à indexer** : il se présente tel
  quel, en tableau daté (règle « aucun chiffre isolé »). Il ne relève pas d'un générateur tant
  qu'aucune base de paramètres ne le porte : `<!-- TODO (rédacteur) : remplacer par un tableau
  engendré -->`.

Agrément préalable des investissements (art. 15, devenu 19) : **décret n° 75-782 du 6 novembre
1975**, JORT n° 74 du 11 novembre 1975 (en-tête relu), p. 2384 (image) : agrément conjoint des
ministres pour tout projet ≥ **100 000 D** dans les communes dont le budget est approuvé par les
ministres, ≥ **50 000 D** pour les autres communes et les conseils de gouvernorat. Exécutoire le
13 novembre 1975. Aucun décret postérieur fixant ce montant n'est identifié (FTS « 75-35 » : seul
75-782 vise l'art. 15). Clé proposée : `decret75-782`.

## 2. L'emprunt avant 2018

- **Loi n° 75-37 du 14 mai 1975, portant transformation de la caisse des prêts aux communes en une
  caisse des prêts et de soutien des collectivités locales**, JORT n° 34 du 20 mai 1975, p. 1068
  (image, partielle : art. 3 à 6). Art. 3 : ressources de la caisse = prélèvement sur les
  ressources annuelles du fonds commun (loi n° 75-36), annuités de remboursement, emprunts de la
  caisse, produits financiers, autres recettes. Art. 4 : prêts aux communes, syndicats de communes,
  conseils de gouvernorat et établissements publics locaux pour les investissements d'intérêt
  public ; subventions aux collectivités à sujétions spéciales ou en situation financière
  difficile, dans la limite de la moitié du prélèvement sur le fonds commun ; bonifications
  d'intérêts. Art. 5 : modalités par décret. Art. 6 : effet au **1er janvier 1976**. Clé proposée :
  `loi75-37` (historique seulement : la CPSCL relève du chapitre 9).
- **Loi n° 75-38** du même jour (allègement de la dette des communes et conseils de gouvernorat
  auprès de la caisse des prêts) : titre seul (cache), p. 1068-1069.
- LF 1980 (loi n° 79-66), art. 37 : exonération de timbre et d'enregistrement des conventions de
  prêts « autorisés par décrets » conclues avec la CPSCL (OCR) — indique que les prêts étaient
  autorisés par décret.
- Décret n° 2014-3505 du 30 septembre 2014, conditions d'attribution des prêts et subventions par
  la CPSCL, JORT n° 79 de 2014, p. 2576-2578 : titre seul (relève du chapitre 9).
- **Ni la loi n° 75-35 ni sa refonte de 2007 ne fixent de plafond d'endettement** ; la règle est
  l'inscription des annuités parmi les dépenses obligatoires (art. 10 / 12) et l'équilibre par
  titre (1975) puis l'encadrement des engagements (2007). Dafflon et Gilbert (2018, p. 84-88)
  relèvent que l'« équilibre réel » n'est pas défini par la loi, et que l'emprunt est compté parmi
  les recettes du titre II.

## 3. Exécution, comptabilité et contrôle avant 2018

- Code de la comptabilité publique, loi n° 73-81 du 31 décembre 1973 : visé par tous les décrets
  de 2010-2017 ; **non lu** ici. L'art. 2 de la loi n° 75-35 renvoie à son art. 3 (exercice),
  l'art. 25 à un article sur le compte financier. Clé : à vérifier dans `precis/fr/references.json`
  (non relevée).
- Ordonnateur : le président de la collectivité (art. 8 et 23 bis de 2007 : « ordonnateurs des
  budgets des collectivités locales ») ; comptable : receveur des finances (non lu dans un texte de
  ce dossier ; voir code de la comptabilité publique).
- Cour des comptes : d'après Dafflon et Gilbert (2018, p. 77), la loi n° 68-8 du 8 mars 1968,
  modifiée par la loi organique n° 2008-3 du 29 janvier 2008, lui donne compétence pour examiner les
  comptes et apprécier la gestion des collectivités locales ; non lu au JORT. Le code de 2018
  (art. 388) vise « القانون عدد 8 لسنة 1968 المؤرخ في 8 مارس 1968 المتعلق بتنظيم دائرة المحاسبات ».
- Tutelle : gouverneur pour les communes, ministre de l'Intérieur pour les conseils régionaux,
  ministres de l'Intérieur et des Finances au-delà du seuil (§ 1.4). Dafflon et Gilbert analysent
  cette tutelle comme une tutelle de légalité sur la procédure, puis une tutelle de contenu portant
  surtout sur l'équilibre (p. 77).

## 4. Le code des collectivités locales de 2018 : régime financier

- **Loi organique n° 2018-29 du 9 mai 2018, relative au code des collectivités locales**
  (« مجلة الجماعات المحلية »), JORT n° 39 du **15 mai 2018**, édition arabe ; dépôt au gouvernorat de
  Tunis le **17 mai 2018** (« تم إيداع هذا العدد ... يوم 17 ماي 2018 ») → exécutoire le **22 mai
  2018**. Clé existante : `loi-org-2018-29-ccl` (FR sans URL, AR : Ja0392018).
- **Entrée en vigueur des dispositions budgétaires** (art. 383, p. 1759) : les dispositions
  relatives à chaque catégorie de collectivités entrent en vigueur progressivement après la
  proclamation des résultats définitifs de leurs élections ; « ولا تدخل الأحكام المتعلّقة بإعداد
  الميزانية والمصادقة عليها حيّز النفاذ إلا بداية من غرّة جانفي للسنة الموالية للإعلان عن النتائج النهائية
  للانتخابات الخاصة بكلّ صنف من الجماعات المحلية » (les dispositions sur la préparation et
  l'approbation du budget n'entrent en vigueur qu'au 1er janvier de l'année qui suit la proclamation
  des résultats définitifs des élections de chaque catégorie). Les élections municipales de 2018
  donneraient le **1er janvier 2019** pour les communes, **sous réserve de la date de proclamation
  des résultats définitifs, non établie ici** (fiche proposée `r-ccl-2018-resultats-municipales`,
  § 6). Pour les régions, aucune élection régionale n'a eu lieu sous le code (à établir au chapitre
  d'histoire) : ses dispositions budgétaires régionales ne sont donc jamais entrées en vigueur, et
  la loi organique n° 2025-4 les abroge (§ 5).
- **Le code n'abroge pas la loi n° 75-35** : aucune disposition d'abrogation dans les art. 383-400
  (lus), et la loi organique n° 2025-4 renvoie encore à la loi n° 75-35 (§ 5).
- **Principes** :
  - art. 126 (p. 1724) : libre disposition des ressources ; « مبدأ الشرعية المالية وقاعدة التوازن
    الحقيقي للميزانية » (principe de légalité financière et règle de l'équilibre réel du budget) ;
  - art. 128 : pas de charges de l'État imposées aux collectivités, sauf cas exceptionnels prévus
    par la loi, avec remboursement ;
  - art. 129 : le comptable de la collectivité est un **comptable public de l'État**, comptable
    principal, nommé par arrêté du ministre des Finances ;
  - art. 130 : budget annuel transparent et participatif, « وثيقة شاملة وموحّدة وواضحة », sur des
    prévisions « واقعية وصادقة ونزيهة » ;
  - art. 131 : l'État fait progressivement des ressources propres la part la plus importante des
    ressources de chaque collectivité ;
  - art. 132 : définition des **ressources propres** (موارد ذاتية) — neuf rubriques, dont les
    impôts locaux fixés par la loi (art. 65 de la Constitution), les parts d'impôts partagés, les
    droits et redevances fixés par les conseils, et les parts de péréquation (« منابات ... بعنوان
    التسوية والتعديل والتضامن ») ;
  - **art. 133 (p. 1725, image)** : budget en équilibre effectif ; « تعتبر ميزانية الجماعة المحلية
    متوازنة عندما تتمّ المصادقة على نفقات التصرف ونفقات التنمية على أساس التوازن مع الأخذ بعين الاعتبار
    كلّ التعهدات السابقة بما في ذلك خدمة الدين » ;
  - **art. 134 (image)** : « تخصص موارد الاقتراض وجوبا لتمويل استثمارات الجماعات المحلية ولا يجوز
    الاقتراض لتمويل ميزانية التصرف » — **règle d'or** : l'emprunt finance exclusivement
    l'investissement ;
  - **art. 135 (image)**, huit règles de prévision : sincérité (صدقية) ; recettes du titre I ≥
    dépenses du titre I ; inscription des dépenses obligatoires de l'art. 160 ; **service de la
    dette (principal et intérêts) couvert par les ressources propres** ; dépenses sur ressources
    extérieures affectées ≥ emprunt extérieur affecté ; équilibre de la partie 5 ; **rémunérations
    ≤ 50 % du titre I de l'année écoulée** ; **remboursement annuel du principal ≤ 50 % du budget de
    fonctionnement de l'année précédant la préparation**, emprunts à mobiliser compris.
- **Ressources** : art. 137 (p. 1726), huit sources de financement ; art. 139, les conseils fixent
  les droits et redevances (déjà exploité aux chapitres 6-8) ; art. 142 : autorisation annuelle de
  perception par la délibération budgétaire, recours du gouverneur devant le juge administratif.
- **Nomenclature** : art. 155 (p. 1728), ressources du titre I en six catégories — 1 recettes
  fiscales sur les immeubles et les activités ; 2 autres recettes fiscales ; 3 droits, redevances
  et prix des services ; 4 occupation du domaine ; 5 revenus du domaine, participations et divers ;
  **6 transferts de l'État au titre du fonctionnement** (« تحويلات الدولة بعنوان التسيير ») ;
  partie 1 (fiscal) = 1-2, partie 2 (non fiscal) = 3-6. Titre II : catégories 7 à 13, la 13e
  nouvelle (« موارد حسابات أموال المشاركة », fonds de concours) ; parties 3 à 6. Art. 159
  (p. 1729) : dépenses en douze sections (القسم), la 12e nouvelle (fonds de concours). Art. 156 :
  budget par missions et programmes, nomenclature par décret gouvernemental ; évaluation par des
  auditeurs au moins tous les trois ans. Art. 157-158 : crédits d'engagement et de paiement. Art.
  167 : nomenclature détaillée par décret gouvernemental sur approbation du Haut Conseil des
  collectivités locales. Dafflon (2021) : la déclinaison des art. 155 et 159 est « pratiquement
  identique » à celle de 2007, à deux changements près (catégories 3 et 4 passées du fiscal au non
  fiscal ; ajout d'une sixième partie pour les fonds de concours) ; aucune classification
  fonctionnelle. *À noter aussi : la 6e catégorie change d'objet — revenus financiers en 2007,
  transferts de fonctionnement de l'État en 2018 (lecture directe des deux textes).*
- **Dépenses obligatoires** : art. 160 (p. 1730), même liste qu'en 2007, archives comprises.
- **Préparation et vote** (art. 166-176, p. 1731-1732) : cadre triennal (art. 166) ; prévisions
  de transferts communiquées par l'État avant le 30 juin, définitives avant le 10 septembre
  (art. 168) ; propositions des conseillers avant le 30 juin, projet en commission des finances
  avant le 1er septembre, au bureau avant le 20 septembre (art. 169) ; transmission au trésorier
  régional (أمين المال الجهوي) avant le 15 octobre, avis sous un mois ; documents aux conseillers
  quinze jours avant la séance (art. 170) ; documents publiés (art. 171) ; vote **avant le
  1er décembre** (art. 172), à défaut convocation par un tiers des membres, puis mise en demeure du
  gouverneur jusqu'au 15 décembre ; vote des recettes par parties et catégories, des dépenses par
  sections et articles ; quorum de deux cinquièmes (art. 173) ; **transmission au gouverneur et au
  trésorier régional sous cinq jours ; le gouverneur peut, sous dix jours, saisir la chambre
  territoriale de la Cour des comptes** (« هيئة محكمة المحاسبات المختصة ترابيا ») pour déséquilibre
  ou défaut d'inscription d'une dépense obligatoire ; ses décisions s'imposent (art. 174) ; budget
  non adopté au 31 décembre → douzièmes des dépenses obligatoires ; **non adopté fin mars → le
  conseil est dissous de plein droit** (art. 175) ; publication en ligne (art. 176).
  *Le régime passe ainsi d'une approbation a priori par l'autorité de tutelle (1975-2007) à un
  contrôle a posteriori par recours juridictionnel.*
- **Exécution** (art. 177-183, p. 1732-1733) : dépenses ordonnancées ≤ encaissements effectifs ;
  modification en cours d'année ; virements votés par le conseil, recours du gouverneur devant la
  chambre de la Cour des comptes (art. 179) ; plafonnement des engagements (art. 181, reprise de
  l'art. 23 bis de 2007) ; **déficit d'exécution > 5 %** → le Haut Conseil des collectivités, à la
  demande du ministre des Finances, invite la collectivité à le résorber ; sinon mesures ordonnées
  par la chambre de la Cour des comptes (art. 182) ; violation de l'art. 181 = faute de gestion
  (art. 183).
- **Comptable et comptes** (art. 184-197, p. 1733-1735) : attributions du comptable ; contrôle de
  légalité, non d'opportunité (art. 186) ; réquisition par l'ordonnateur et transmission à la
  chambre de la Cour des comptes (art. 186) ; comptabilité en partie double et en droits constatés,
  système comptable préparé par le Conseil national des normes des comptes publics et pris par
  décret gouvernemental (art. 191), à adopter **dans les quatre ans** de l'entrée en vigueur des
  dispositions budgétaires (art. 390, p. 1760) ; états financiers avant le 5 avril, compte arrêté
  par le conseil avant fin mai (art. 194) ; refus → chambre de la Cour des comptes (art. 195) ;
  copie du compte financier à la chambre avant le 31 juillet (art. 196) ; recours des contribuables
  locaux devant la chambre contre les décisions budgétaires (art. 197) ; inspection a posteriori
  (art. 198-199).
- **Haute instance des finances locales** (art. 61-65, p. 1716-1717) : placée auprès du Haut
  Conseil des collectivités locales ; propose les transferts et leurs critères, **suit
  l'endettement**, analyse les états financiers, évalue le coût des transferts de compétences ;
  rapport annuel ; composée d'un magistrat financier président, de neuf représentants du Haut
  Conseil, de représentants des ministères et de la CPSCL (« صندوق القروض ومساعدة الجماعات المحلية »),
  d'un expert-comptable et d'un comptable. Art. 399 : nomination transitoire par décret
  gouvernemental. Le décret de nomination n'est pas identifié ici (non cherché en détail ; voir
  § 6).
- **Démocratie participative et budget** : art. 130 et 171 (publication), 165 (droit de demande
  d'explication des habitants, recours au tribunal administratif). Dafflon (2021) traite des
  « trois piliers de la démocratie participative » du code ; les articles du code sur les
  mécanismes participatifs (Livre I, section 5, art. 29 et suiv.) relèvent du chapitre
  compétences/organisation (non lus ici).
- **Pouvoirs du conseil municipal** : art. 236 (p. 1739) : le conseil municipal étudie et approuve
  le budget et les opérations d'emprunt.

## 5. Après 2018 : la loi organique n° 2025-4

- **Loi organique n° 2025-4 du 12 mars 2025, relative aux conseils locaux, conseils régionaux et
  conseils de districts**, JORT n° 30 du **13 mars 2025**, FR p. 706 (« Traduction française pour
  information »), AR p. 775 (art. 8-10) ; dépôt le **13 mars 2025** → exécutoire le **18 mars 2025**.
  Adoptée par l'ARP le 27 février 2025.
  - FR : https://www.pist.tn/jort/2025/2025F/Jo0302025.pdf — AR : https://www.pist.tn/jort/2025/2025A/Ja0302025.pdf
  - Clé proposée : `loi-org2025-4`.
  - art. 1er : conseils locaux, régionaux et de districts = collectivités locales dotées de la
    personnalité juridique et de l'autonomie administrative et financière ;
  - art. 5 : régis par « la loi organique relative au budget desdits conseils » et par la loi sur
    la comptabilité publique ; le président du conseil est ordonnateur ;
  - **art. 8** (AR fait foi) : « تخضع قواعد وصيغ إعداد ميزانية المجلس المحلي والمجلس الجهوي ومجلس
    الإقليم والمصادقة عليها لأحكام القانون الأساسي عدد 35 لسنة 1975 المؤرخ في 14 ماي 1975 المتعلق
    بالقانون الأساسي لميزانية الجماعات المحلية ما لم تتعارض مع أحكام هذا القانون » — **la loi
    n° 75-35 régit le budget des nouveaux conseils** ;
  - art. 9 : biens et dotations des conseils régionaux de la loi n° 89-11 transférés à l'État, à
    la disposition du gouverneur ;
  - art. 10 : abroge les dispositions contraires, « notamment les dispositions relatives à la
    région et au district » du code de 2018, la loi organique n° 89-11 et la loi n° 94-87.
- **Conséquence** : pour les communes, le régime budgétaire du code (livre I, titre IV) reste en
  vigueur ; pour les nouveaux conseils, c'est la loi n° 75-35. *Ce que devient en pratique le budget
  des communes dont les conseils ont été dissous en 2023 relève du chapitre d'histoire (décret-loi
  n° 2023-9, hors de ce dossier).*
- Décrets n° 2025-177 et 2025-178 du 4 avril 2025 (fonctionnement des conseils ; indemnités) :
  titres seuls (cache), JORT n° 41 de 2025, p. 836-837.

## 6. Recherches infructueuses : fiches proposées

```yaml
- id: r-lob-cl-seuil-approbation-apres-2017
  objet: décret fixant le seuil de recettes au-delà duquel le budget communal est approuvé par les ministres (art. 16, 2e sous-paragraphe, loi n° 75-35), postérieur au décret gouvernemental n° 2017-758
  ou: [precis/fr/finances_locales/_budgets.qmd]
  requetes:
    titres_fts: ['"75-35" OR "75 35"', 'ميزانية AND الجماعات AND المحلية']
    titres_like: ['%budget des collectivites%', '%budgets des communes%', '%budgets communaux%', '%ميزانية الجماعات%', '%ميزانيات الجماعات%', '%35 لسنة 1975%', '%المصادقة على ميزانيات%']
    depuis: 2017-06-21
  passes:
  - date: 2026-10-05
    role: documentaliste
    sources: [jort_cache]
    couverture: "titres jort_cache jusqu'au 18 septembre 2026 ; plein texte non parcouru ; fascicules inconnus de la base (outillage-sources § 1 f) non examinés"
    couvert_jusqu_au: 2026-09-18
    resultat: aucun
  a_faire: [plein texte des fascicules 2017-2026 sur « 75-35 » et « 35 لسنة 1975 »]

- id: r-ccl-2018-nomenclature-art167
  objet: décret gouvernemental fixant la nomenclature des budgets (art. 167), les missions et programmes (art. 156) ou le système comptable (art. 191) du code des collectivités locales
  ou: [precis/fr/finances_locales/_budgets.qmd]
  requetes:
    titres_fts: ['تبويب', 'المحاسبي AND الجماعات', 'nomenclature AND collectivites', 'comptable AND collectivites AND locales', 'مهمات AND برامج AND الجماعات']
    depuis: 2018-05-15
  passes:
  - date: 2026-10-05
    role: documentaliste
    sources: [jort_cache]
    couverture: "titres jort_cache 2018 – 18 septembre 2026 ; seuls des textes relatifs au budget de l'État sont sortis ; plein texte non parcouru"
    couvert_jusqu_au: 2026-09-18
    resultat: aucun

- id: r-ccl-2018-resultats-municipales
  objet: décision de l'ISIE proclamant les résultats définitifs des élections municipales de 2018 (point de départ de l'art. 383 du code des collectivités locales)
  ou: [precis/fr/finances_locales/_budgets.qmd]
  requetes:
    titres_fts: ['النتائج النهائية']
    titres_like: ['%انتخابات البلدية%', '%elections municipales%', '%élections municipales%', '%النتائج النهائية للانتخابات البلدية%']
    depuis: 2018-05-06
  passes:
  - date: 2026-10-05
    role: documentaliste
    sources: [jort_cache]
    couverture: "titres jort_cache 2018 ; plein texte non parcouru ; les décisions de l'ISIE ont souvent un titre arabe seul"
    couvert_jusqu_au: 2018-12-31
    resultat: aucun
  a_faire: [plein texte JORT mai-août 2018, « النتائج النهائية للانتخابات البلدية »]
```

Requêtes réellement lancées pour la fiche `r-lob-cl-seuil-approbation-apres-2017` : FTS
`"75-35" OR "75 35"` (toutes années, liste complète au § 1.4) ; LIKE sur les titres listés ;
FTS `ميزانية AND الجماعات AND المحلية` depuis 2017 (deux arrêtés de 2018-2019 sur la répartition du
soutien de l'État, sans rapport). Pour l'agrément des investissements (art. 15/19), la même FTS ne
rend que le décret n° 75-782 : pas de fiche proposée tant que le rédacteur ne présente pas ce
seuil comme en vigueur.

## 7. Références candidates

Déjà présentes : `loi-org-2018-29-ccl`, `loi93-64`, `dafflon-gilbert-2018`, `loi79-66-lf1980`
(precis/fr/references.json — à vérifier qu'il s'agit bien de la LF 1980, JORT n° 76 de 1979).

À créer (type `legislation`, `container-title` « Journal officiel de la République tunisienne »,
URL = champ `pdf_fr` / `pdf_ar` du recid) :

| Clé | Titre | JORT | recid |
|---|---|---|---|
| `loi75-35` | Loi n° 75-35 du 14 mai 1975, portant loi organique du budget des collectivités publiques locales | n° 34, 20 mai 1975, p. 1065-1067 | 116141 |
| `loi75-37` | Loi n° 75-37 du 14 mai 1975, portant transformation de la caisse des prêts aux communes en une caisse des prêts et de soutien des collectivités locales | n° 34, p. 1068 | 116143 |
| `loi-org85-44` | Loi organique n° 85-44 du 25 avril 1985, portant modification de l'article 13 de la loi n° 75-35… | n° 34, 30 avril 1985, p. 644 | 114585 |
| `loi-org94-44` | Loi organique n° 94-44 du 9 mai 1994, modifiant la loi n° 75-35… | n° 38, 17 mai 1994, p. 800 | 112807 |
| `loi-org97-1` | Loi organique n° 97-1 du 22 janvier 1997, portant modification de l'article 11 de la loi n° 75-35… | n° 7, 24 janvier 1997, p. 114 | 112334 |
| `loi-org2007-65` | Loi organique n° 2007-65 du 18 décembre 2007, modifiant et complétant la loi n° 75-35… | n° 103, 25 décembre 2007, p. 4277-4281 | 110125 |
| `arrete2008-03-31-nomenclature` | Arrêté du ministre de l'intérieur et du développement local et du ministre des finances du 31 mars 2008, fixant la forme et la nomenclature des budgets des collectivités locales | n° 28, 4 avril 2008, p. 1141-1142 | 54490 |
| `decret75-485` | Décret n° 75-485 du 26 juillet 1975… article 13 de la loi n° 75-35… | n° 52, 29 juillet 1975, p. 1593 | 101581 |
| `decret75-782` | Décret n° 75-782 du 6 novembre 1975… article 15… | n° 74, 11 novembre 1975, p. 2384 | 101415 |
| `decret77-320` | Décret n° 77-320 du 1er avril 1977… article 13… | n° 23, 1977, p. 834 | 100546 |
| `decret86-1036` | Décret n° 86-1036 du 30 octobre 1986… article 13… | n° 64, 1986, p. 1252 | 95191 |
| `decret89-280` | Décret n° 89-280 du 10 février 1989… article 13… (date : fascicule ; cache : 19 février) | n° 13, 1989, p. 285 | 94017 |
| `decret97-1837` | Décret n° 97-1837 du 15 septembre 1997… article 13… | n° 77, 26 septembre 1997, p. 1808 | 89808 |
| `decret2010-3179` | Décret n° 2010-3179 du 13 décembre 2010… 2e sous-paragraphe de l'article 16… | n° 101, 17 décembre 2010, p. 3415-3416 | 80817 |
| `decret2012-2475` | Décret n° 2012-2475 du 16 octobre 2012… | n° 84, 23 octobre 2012, p. 2590-2591 | 79810 |
| `decret2013-3235` | Décret n° 2013-3235 du 2 août 2013… | n° 67, 20 août 2013, p. 2447-2448 | 79340 |
| `decret2014-2232` | Décret n° 2014-2232 du 16 juin 2014… | n° 50, 24 juin 2014, p. 1623-1624 | 78951 |
| `decret2015-1739` | Décret gouvernemental n° 2015-1739 du 10 novembre 2015… | n° 91, 13 novembre 2015, p. 2704-2705 | 78337 |
| `decret2017-758` | Décret gouvernemental n° 2017-758 du 13 juin 2017… | n° 49, 20 juin 2017, p. 2207 | 77426 |
| `loi-org2025-4` | Loi organique n° 2025-4 du 12 mars 2025, relative aux conseils locaux, conseils régionaux et conseils de districts | n° 30, 13 mars 2025, FR p. 706, AR p. 775 | 196339 |

Doctrine :
- `dafflon-gilbert-2018` : ch. 3 « Budgets et comptes décentralisés », p. 61-97 ; § 3.1 (textes,
  encadré 2, p. 62-63), § 3.3 (nomenclature, p. 69-74), § 3.4 (procédure, schéma 14, tutelle,
  p. 74-81), § 3.5 (discipline, équilibre, endettement, p. 81-91 ; « équilibre réel » non défini,
  p. 84 ; sous-équilibres de l'art. 30, p. 85-87 ; reddition des comptes, schémas 15-16,
  p. 88-90) ; § 3.6 questions ouvertes (p. 91-97).
- **À créer** : `dafflon-2021-budget-local` — Dafflon, Bernard, « Le budget local : la
  transparence financière au service de la démocratie participative », in *Transparence et droit :
  ouvrage collectif en l'honneur du doyen Néji Baccouche*, Sfax, Centre d'études fiscales de la
  Faculté de droit de Sfax, 2021, p. 391-425 (type `chapter` ; métadonnées :
  `docs/notes/biblio-fiscalite-locale.md`, texte 4 ; copie d'auteur
  https://www.unifr.ch/ecopol/en/assets/public/Department/Prof%20em/2021_123_le_budget_local.pdf).
  **Ne jamais citer de page** (manuscrit) : citer sans locator ou par section (« § 3 »).
- Dafflon, RTF n° 20 (2013), p. 105-154 : hors accès libre, non lu ; ne pas citer.

## 8. Notions à glossaire

Termes attestés au JORT (FR = édition française ; AR = édition arabe, lue) :

| id proposé | FR | AR | Source |
|---|---|---|---|
| `equilibre-reel` | équilibre réel (du budget) | التوازن الحقيقي (للميزانية) | loi 75-35 art. 16 (FR) ; CCL art. 126, 135 (AR) |
| `depenses-obligatoires` | dépenses obligatoires | النفقات الإجبارية / النفقات الوجوبية | loi 75-35 art. 10 ; CCL art. 160 (« إجبارية »), 174 (« وجوبية ») |
| `titre-budget-local` | titre I (gestion), titre II (développement) | العنوان الأول / العنوان الثاني | loi 2007-65 art. 3 ; CCL art. 135, 155 |
| `compte-financier` | compte financier | الحساب المالي | loi 75-35 art. 25 ; CCL art. 195-196 |
| `fonds-de-reserve` | fonds de réserve | (AR à relever dans Ja1032007) | loi 2007-65 art. 26 |
| `ordonnateur` | ordonnateur | آمر الصرف | loi 2007-65 art. 8, 23 bis ; CCL art. 163, 186 |
| `comptable-public` | comptable public (de la collectivité) | محاسب الجماعة المحلية / المحاسب العمومي | CCL art. 129, 184 |
| `tresorier-regional` | trésorier régional (FR non attesté : traduction) | أمين المال الجهوي | CCL art. 170, 174 — **provisoire** |
| `credits-engagement-paiement` | crédits d'engagement, crédits de paiement | اعتمادات التعهد / اعتمادات الدفع | loi 2007-65 art. 8 ; CCL art. 157 |
| `haute-instance-finances-locales` | Haute instance des finances locales (FR non attesté) | الهيئة العليا للمالية المحلية | CCL art. 61 — déjà cité au chapitre 8 ; vérifier si une entrée existe |
| `faute-de-gestion` | faute de gestion | خطأ تصرّف | loi 2007-65 art. 23 bis ; CCL art. 183 |

Notions déjà au glossaire (chapitre 2), à mobiliser : `g-regle-d-or`, `g-emprunt`,
`g-capacite-emprunt`, `g-tutelle`, `g-discipline-budgetaire`, `g-epargne-nette`,
`g-ressources-propres`, `g-taux-de-recouvrement` (art. 152-154 : objectifs de recouvrement,
avance de l'État de la moitié des créances fiscales non recouvrées après un an, art. 154).

## 9. Lacunes

> Relecture du 5 octobre 2026 (rédaction) : les décrets n° 77-320 (p. 834 : 1 000 000 D et 75 000 D), 86-1036 (p. 1252 : 1 000 000 D) et 89-280 (p. 285 : 2 000 000 D, signé le 10 février 1989, effet au 1er janvier 1989) ont été relus à l'image ; le point 1 ne vaut plus que pour la LF 1980. Résultats définitifs des municipales de 2018 : décisions de l'ISIE n° 2018-12 à 2018-361, du 17 mai au 12 juin 2018, JORT n° 46 à 50 de 2018 (point 5 levé).

1. **Relire à l'image** les décrets n° 77-320 (art. 3 : seuil du délégué), 86-1036 et 89-280
   (seuils et date de signature), et la LF 1980 (art. 38-41), lus sur OCR ; confirmer les dates de
   publication des textes antérieurs à 1993 au pied des fascicules.
2. Art. 11 et 27 de la loi n° 75-35 : dates des décrets beylicaux cités (1937 ? 1947 ? 1956 ?),
   mal lisibles sur le scan français : lire l'édition arabe (Ja03475, p. 1065-1067).
3. Article du code de la comptabilité publique visé par l'art. 25 (232 ou 282) : lire le texte.
4. Code de la comptabilité publique (loi n° 73-81) et loi sur la Cour des comptes (loi n° 68-8 ;
   loi organique n° 2019-41 du 30 avril 2019, à identifier) : non lus.
5. Date de proclamation des résultats définitifs des municipales de 2018 (fiche
   `r-ccl-2018-resultats-municipales`), donc date exacte d'entrée en vigueur du régime budgétaire
   du code pour les communes.
6. Décrets gouvernementaux d'application des art. 156, 167 et 191 du code (fiche
   `r-ccl-2018-nomenclature-art167`) ; décret de nomination transitoire de la Haute instance
   (art. 399) — non cherché.
7. Pages du code (art. 136 et suiv.) à confirmer à l'image (deux colonnes).
8. Plafonds de l'art. 135 (rémunérations ≤ 50 % ; principal ≤ 50 %) : valeurs uniques, en vigueur
   depuis l'entrée en vigueur des dispositions budgétaires ; ce sont des règles, non des séries,
   mais le rédacteur doit les présenter avec la date d'effet et la mention qu'aucune modification
   n'est identifiée.
9. Données (soldes, endettement, recouvrement) : renvoi en prose au chapitre de la longue période
   (chapitre 10), aucune valeur ici.

## 10. Plan proposé du chapitre

```
# Budgets et comptes {#sec-fl-budgets-comptes}
(rappel des notions : budget décentralisé @sec-fl-budget-decentralise, règle d'or @sec-fl-regle-or,
 tutelle @sec-fl-tutelle, autonomie @sec-fl-autonomie, recouvrement @sec-fl-recouvrement)

## Les origines {#sec-fl-budg-origines}
  ### Avant 1975 : les textes que la loi organique abroge {#sec-fl-budg-avant-1975}
  ### La loi organique du budget de 1975 {#sec-fl-budg-1975}

## Le budget sous la loi organique de 1975 {#sec-fl-budg-lob}
  ### La nomenclature, de 1975 à 2007 {#sec-fl-budg-nomenclature}      (tableau 1975 / 1980 / 2007 / 2018)
  ### Préparation, vote et approbation {#sec-fl-budg-procedure}
  ### La tutelle d'approbation et ses seuils {#sec-fl-budg-seuils}      (tableau daté § 1.4)
  ### Équilibre, dépenses obligatoires et déficit {#sec-fl-budg-equilibre}
  ### Emprunt et caisse des prêts {#sec-fl-budg-emprunt}

## Le code des collectivités locales de 2018 {#sec-fl-budg-ccl}
  ### Principes et ressources propres {#sec-fl-budg-ccl-principes}
  ### Équilibre, règle d'or et plafonds {#sec-fl-budg-ccl-regle-or}
  ### Du contrôle a priori au recours devant la Cour des comptes {#sec-fl-budg-ccl-controle}
  ### Comptable public et reddition des comptes {#sec-fl-budg-ccl-comptes}
  ### Entrée en vigueur {#sec-fl-budg-ccl-vigueur}

## Depuis 2025 : deux régimes budgétaires {#sec-fl-budg-2025}

## La longue période {#sec-fl-budg-longue-periode}   (renvoi en prose au chapitre 10)

## Notations, si formules (sans doute aucune) — sinon pas de section
```

Chaque section subdivisée a au moins deux sous-sections ; `## Depuis 2025` et `## La longue
période` restent non subdivisées.

## 11. Notions mobilisées

- Ancres de `_notions.qmd` : `sec-fl-budget-decentralise` (budget de référence, emprunt hors des
  ressources), `sec-fl-regle-or` (fonctionnement/investissement, règle d'or revisitée, capacité
  d'emprunt), `sec-fl-tutelle` (légalité/opportunité, a priori/a posteriori — le passage de 1975 à
  2018 en est l'illustration directe), `sec-fl-autonomie` (art. 131-132 du code),
  `sec-fl-recouvrement` (art. 152-154), `sec-fl-taux-autonomie` (définition légale des ressources
  propres, art. 132, à confronter à la mise en garde de Dafflon et Gilbert, p. 150).
- Glossaire : `g-regle-d-or`, `g-emprunt`, `g-capacite-emprunt`, `g-tutelle`,
  `g-discipline-budgetaire`, `g-epargne-nette`, `g-ressources-propres`, `g-taux-de-recouvrement`.
- Notions nouvelles : § 8.
