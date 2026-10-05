# Volume VII « Les finances locales », chapitre 3 : note documentaire sur l'histoire des collectivités et de leurs finances

> Note du documentaliste, 4-5 octobre 2026. Elle sert le chapitre 3 du plan
> (`docs/notes/fiscalite-locale-plan.md`), « Histoire des collectivités et de leurs finances »,
> fichier cible `precis/fr/finances_locales/_histoire.qmd` (ancre `sec-fl-histoire`). Rien n'y est
> rédigé pour le précis.
>
> **Sources.** Textes lus au *Journal officiel*, dans les fascicules du corpus local
> (`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`) ou, quand le corpus ne les a pas, téléchargés
> de pist.tn (1957, n° « 122 » de pist.tn, voir § 1.1). Les fascicules antérieurs à 2000 sont des
> images : ils ont été lus à l'image (outil de lecture des PDF) après repérage des pages par
> océrisation (`ocrmypdf -l fra`). L'édition arabe du code de 2018, des décrets-lois de 2023 et du
> décret n° 2023-589 a été lue à l'image ; les citations arabes ci-dessous sont relevées sur l'image.
> Métadonnées : `jort_cache.db`. Guides, jamais sources finales d'un fait de droit : Dafflon et
> Gilbert, AFD 2018 (`dafflon-gilbert-2018`), ch. 2 (p. 31-50) et ch. 7 (p. 263-290) ; pages
> imprimées = page PDF − 2 (vérifié p. 29, 31, 263).
>
> **Pages.** « FR » = édition française, « AR » = édition arabe. Elles coïncident jusqu'aux années
> 1990 dans les fascicules lus ici, sauf en 1957 (p. 296 FR, p. 416 AR pour la loi municipale).
>
> **Dates d'effet** (règle « Dater » d'AGENTS.md). Pour un texte sans clause d'effet : avant 1993,
> un jour franc après la publication ; depuis 1993, dépôt au gouvernorat de Tunis + 5 jours, jour du
> dépôt non compté (`loi93-64`, art. 2). Les dates de dépôt citées ci-dessous sont relevées sur la
> dernière page du fascicule. Pour ce chapitre d'histoire, la plupart des textes sont cités par leur
> date et leur publication ; la date d'effet n'est calculée que là où elle sert.

## 0. Ce que la base contient avant 1956

`jort_cache.db`, compte par `jort_annee` (requête `select jort_annee, count(*) … where jort_annee < 1957
group by jort_annee`, 5 octobre 2026) : 1956 → 1 215 textes ; 1955 → 42 ; 1953 → 9 ; de 1928 à
1954, entre 1 et 2 textes par an (années 1928, 1930-1932, 1934, 1935, 1938, 1940, 1942, 1945, 1949,
1951, 1952, 1954) ; plus des années aberrantes (150, 199, 201, 975, 1070, 1075, 1775, 1870). Le corpus
local des fascicules commence en 1956 (`PDFs/JORT/1956/`, 103 fascicules FR, 104 AR). **Le *Journal
officiel tunisien* d'avant 1956 n'est ni dans la base, ni dans le corpus.**

Conséquence pour la rédaction : les textes beylicaux et du protectorat ne sont connus ici que par
les visas et les abrogations des textes postérieurs (§ 1) et, pour la fiscalité, par la liste
d'abrogations de la loi n° 97-11, déjà exploitée aux chapitres 6 à 8. Formule à employer, sur le
modèle de `_impots_immeubles.qmd` : « ces textes ne sont connus ici que par les visas et les
abrogations des textes postérieurs ». Ni récit de recherche, ni « corpus ».

## 1. Les textes établis

### 1.1 La loi municipale de 1957 (décret beylical du 14 mars 1957)

- **Décret du 14 mars 1957 (12 chaabane 1376), portant loi municipale.**
  - Titre AR (image, p. 416) : « أمر علي مؤرخ في 12 شعبان 1376 (14 مارس 1957) يتعلق بقانون البلديات ».
  - Publication : *Journal officiel tunisien* du **15 mars 1957**, FR p. 296-305 (en-tête « Journal
    officiel tunisien — 15 Mars 1957 » relu p. 296, 303, 304, 305) ; AR p. 416 et suiv.
  - Numéro : `jort_cache` dit n° 22 (recid 107859) ; pist.tn sert ce fascicule sous
    `1957/1957F/Jo12257.pdf` et `1957/1957A/Ja12257.pdf` (200, application/pdf, 4 748 529 et
    4 478 696 octets, 5 octobre 2026). **Piège** : le fichier `PDFs/JORT/1957/fr/Jo02257.pdf` du
    corpus local est un autre fascicule (été 1957, numérotation républicaine) ; le corpus local n'a
    pas le fascicule du 15 mars 1957. Citer avec l'URL `pdf_fr`/`pdf_ar` de la base, qui est bonne.
  - Signé par Mohamed Lamine Pacha Bey, contresigné par Habib Bourguiba, Premier ministre (p. 304).
  - **Visas** (p. 296) : décret du 15 septembre 1945 relatif à l'élection du conseil municipal de
    Tunis, modifié notamment par le décret du 4 mars 1954 ; **décret du 20 décembre 1952 relatif à
    l'organisation et au fonctionnement des municipalités en Tunisie**, modifié notamment par le
    décret du 4 mars 1954 ; décret du 21 juin 1956 portant organisation administrative du Royaume.
  - **Art. 1er** : « Les Communes sont des collectivités de droit public dotées de la personnalité
    civile et de l'autonomie financière et chargées de la gestion des intérêts municipaux. »
  - Art. 2 : corps municipal = conseil municipal, président, un ou plusieurs adjoints. Art. 3 :
    communes constituées, délimitées, modifiées ou supprimées par décret. Art. 4 : nombre de
    conseillers fixé par le tableau annexé ; des conseillers étrangers peuvent être **nommés** par le
    ministre de l'Intérieur en sus. Art. 5 : scrutin de liste majoritaire à un tour, panachage admis.
    **Art. 6 : conseillers élus au suffrage direct universel.** Art. 7 : électeurs, Tunisiens « des
    deux sexes » âgés de 21 ans accomplis (chiffre relu sur l'image, p. 296, colonne droite, en
    partie rogné : **à relire** avant de citer l'âge).
  - Art. 25 : dissolution par décret ; si le conseil ne peut être constitué, une **délégation
    spéciale** en remplit les fonctions (p. 298, repéré par OCR, à relire à l'image si cité).
  - **Budget (titre IV, ch. III, p. 303-304)** : art. 104, budget ordinaire (recettes et dépenses
    annuelles et permanentes ; annuités d'emprunt comprises) et extraordinaire (recettes temporaires
    ou accidentelles ; dépenses de construction et de premier établissement, couvertes par l'excédent
    ordinaire ou des recettes extraordinaires) ; art. 105, neuf dépenses obligatoires ; **art. 106,
    recettes** : « 1° des taxes locales spéciales ; 2° une quote-part de l'actif des divers fonds
    communs institués par la réglementation en vigueur ; 3° les revenus des patrimoines de la
    collectivité et des services publics payants qu'elle assume ; 4° éventuellement des subventions
    pour emprunts imputables aux fonds communs susvisés et des subventions en capital de l'État » ;
    **art. 107 : budget proposé par le président, voté par le conseil, arrêté conjointement par les
    ministres de l'Intérieur et des Finances** ; art. 108 : budget voté en déséquilibre renvoyé pour
    seconde délibération, puis arrêté par les deux ministres ; **art. 109 : déficit d'exécution ≥ 20 %
    des ressources ordinaires** → mesures de redressement, à défaut arrêtées par les ministres, sans
    pouvoir créer d'impositions nouvelles ; art. 111 : l'arrêté conjoint peut rejeter ou réduire les
    dépenses, non les augmenter ; art. 112 : inscription d'office des dépenses obligatoires ; art. 113 :
    budget non arrêté au début de l'exercice → dépenses ordinaires du dernier budget reconduites ;
    art. 114 : le président est seul ordonnateur ; art. 115 : un comptable chargé seul du recouvrement
    et des paiements (séparation ordonnateur-comptable).
  - **Art. 117** (p. 304) : abroge les décrets du 15 septembre 1945, du 20 décembre 1952 et du
    4 mars 1954. **Art. 118** : maintient le décret du 30 juillet 1884 (police des cimetières), les
    textes sur les attributions des communes en matière d'état civil, notamment le décret du
    30 septembre 1929, et les articles 84 à 99 du décret du 31 mars 1955 portant fixation du budget
    ordinaire pour l'exercice 1955-56.
  - **Tableau annexé** (p. 304-305) : **94 communes**, numérotées de 1 (Aïn-Draham) à 94
    (Zéramdine), avec leur nombre de conseillers (de 6 à 30, Tunis) et d'adjoints.
  - Date d'effet : pas de clause d'effet relevée ; règle d'avant 1993 (un jour franc après la
    publication du 15 mars 1957). Le texte d'histoire peut s'en tenir à la date du décret.
  - Clé proposée : `decret-1957-03-14-loi-municipale` ; type `legislation` ; URL FR
    `https://www.pist.tn/jort/1957/1957F/Jo12257.pdf`, AR `https://www.pist.tn/jort/1957/1957A/Ja12257.pdf`.
  - Modificatifs (titres seuls, `jort_cache`) : loi n° 58-96 du 19 septembre 1958 ; loi n° 59-123 du
    28 septembre 1959 ; décret-loi n° 62-15 du 1er août 1962 (ratifié par la loi n° 62-37) ; loi
    n° 66-28 du 3 mai 1966 ; loi n° 69-46 du 26 juillet 1969 (art. 64). Non lus.

### 1.2 Les conseils de gouvernorat (1957, 1963)

- **Loi n° 57-12 du 17 août 1957 (20 moharrem 1377), portant création de conseils de gouvernorat.**
  - JORT n° 9 du **23 août 1957**, FR p. 80-82 (image relue p. 80-81) ; rectificatif JORT n° 21 du
    4 octobre 1957, p. 214 (titre seul). URL FR `https://www.pist.tn/jort/1957/1957F/Jo00957.pdf`,
    AR `…/1957/1957A/Ja00957.pdf` (champs de la base ; fichiers présents au corpus local).
  - **Visas** : décrets du 13 juillet 1922 (18 kaada 1340) et du 20 décembre 1952 (2 rabia II 1372)
    « relatifs aux Conseils de Caïdat » ; **décret du 8 novembre 1945 (3 doul hidja 1364), portant
    organisation des finances locales**.
  - Art. 1er : un conseil de gouvernorat auprès de chaque gouverneur. **Art. 2 : présidé par le
    gouverneur, composé de membres nommés par arrêté du secrétaire d'État à l'Intérieur** sur
    proposition du gouverneur ; art. 3 : nommés pour trois ans. Art. 11 : il examine le budget annuel
    de la région. Art. 15 : discussion politique interdite.
  - **Art. 16 : « Chacune des Régions est dotée de l'autonomie financière et de la personnalité
    civile. Le Gouverneur est ordonnateur du Budget de la Région. »** Art. 17 : comptable désigné par
    le secrétaire d'État aux Finances. Art. 18 : budget préparé par le gouverneur, soumis à l'avis du
    conseil, approuvé par arrêté du secrétaire d'État à l'Intérieur après avis conforme du secrétaire
    d'État aux Finances.
  - **Art. 19 (ressources ordinaires)** : taxes régionales spéciales prévues en matière communale par
    le décret du 8 novembre 1945 ; quote-part des fonds communs ; revenus du patrimoine et des services
    payants ; subventions ou emprunts imputables aux fonds communs et subventions de l'État ; dons et
    legs ; ressources déléguées par les secrétariats d'État techniques. Art. 23 (second du nom, la
    numérotation du fascicule porte deux « Art. 23 ») : recouvrement des taxes régionales confié à
    l'État, **qui retient 5 % de leur produit** pour sa rémunération. Art. 24 : la région rétrocède
    aux communes nouvelles les impôts perçus sur leur territoire. Art. 27 : dépenses obligatoires.
  - Clé proposée : `loi57-12`.
  - Modificatifs (titres, `jort_cache`) : décrets-lois n° 60-15 du 7 avril 1960, n° 60-18 du
    10 septembre 1960, n° 62-14 du 1er août 1962 (ratifié par la loi n° 62-36). Non lus.
- **Loi n° 63-54 du 30 décembre 1963 (14 chaabane 1383), relative aux conseils de gouvernorat.**
  - JORT n° 60 du **31 décembre 1963**, FR p. 1873-1875 (image relue). URL FR
    `https://www.pist.tn/jort/1963/1963F/Jo06063.pdf`, AR `…/1963/1963A/Ja06063.pdf`. Adoptée par
    l'Assemblée nationale le 26 décembre 1963. (La base porte une seconde ligne « 63-54 » au JORT n° 6
    du 5 février 1963, p. 167-168 : homonymie à ne pas confondre.)
  - **Art. 1er : « Le Conseil de Gouvernorat est une collectivité publique, dotée de la personnalité
    civile et de l'autonomie financière. Il gère […] dans chaque Gouvernorat, les intérêts
    régionaux. »**
  - **Art. 2 (composition)** : le gouverneur, président ; les membres du comité régional de
    coordination du parti du Néo-Destour ; un représentant de chaque organisation nationale, désigné
    par le secrétaire d'État à l'Intérieur ; les présidents des syndicats de communes. Aucun membre
    élu au conseil comme tel.
  - Art. 9 : examine le projet de budget, les besoins de la région, les projets de développement
    régional. Art. 11 : budget ordinaire et budget supplémentaire ; **exercice du 1er janvier au
    31 décembre**. Art. 12 : le gouverneur établit le budget, qui n'est exécutoire qu'après approbation
    du secrétaire d'État à l'Intérieur. Art. 13 : le gouverneur est ordonnateur.
  - **Art. 15 (recettes ordinaires)** : taxe sur la valeur locative des immeubles ; taxe d'entretien
    et d'assainissement ; taxe sur les débits de boissons ; sur les véhicules ; sur les spectacles ;
    sur les peaux ; taxes sur les formalités administratives ; sur l'occupation du domaine public
    régional ; produits du domaine privé et des services ; quotes-parts des fonds communs des
    collectivités locales ; dons et legs ; taxes exceptionnelles temporaires. Art. 16 : taux, assiette,
    modalités et exonérations fixés par décret. Art. 18 : recouvrement par les recettes du secrétariat
    d'État au Plan et aux Finances. Art. 20 : budget supplémentaire alimenté notamment par les
    subventions de l'État, les emprunts, les crédits délégués.
  - **Titre VI, « La Tutelle », art. 31** : le secrétaire d'État à l'Intérieur exerce l'autorité de
    tutelle ; approbation des virements, des contrats sur le domaine privé, etc.
  - **Art. 39 : abroge la loi n° 57-12.**
  - Clé proposée : `loi63-54`.

### 1.3 La Constitution du 1er juin 1959 et l'article 71

- **Loi n° 59-57 du 1er juin 1959, portant promulgation de la Constitution** : JORT n° 30 du
  **1er juin 1959**. Édition française absente du corpus local et sans `pdf_fr` dans la base ; AR
  `https://www.pist.tn/jort/1959/1959A/Ja03059.pdf` (fichier du corpus). Lu à l'image, AR p. 757 :
  **chapitre VIII « الجماعات المحلية » (« Les collectivités locales »), article 59** dans la numérotation
  de 1959 : « تمارس المجالس البلدية والمجالس الجهوية المصالح المحلية حسبما يضبطه القانون » (les conseils
  municipaux et les conseils régionaux gèrent les affaires locales dans les conditions prévues par la
  loi ; traduction à valider).
  - Le même article devient l'**article 71** après la renumérotation de la Constitution (la loi
    constitutionnelle n° 2002-51 le cite sous ce numéro). Le texte de la renumérotation n'a pas été lu
    (AFD 2018 cite la loi constitutionnelle n° 76-37 du 8 avril 1976 parmi les révisions, p. 34) :
    **à établir** avant d'écrire la date du changement de numéro.
  - Clé proposée : `loi59-57-constitution` (ou `constitution1959`), URL AR seulement ; FR sans URL
    (`biblio-a-rapatrier`).
- **Loi constitutionnelle n° 2002-51 du 1er juin 2002, portant modification de certaines dispositions
  de la Constitution** : JORT n° 45 du **3 juin 2002**, FR p. 1298-1309. Lu à l'image, FR **p. 1306** :
  « Article 71 (nouveau) : Les conseils municipaux, les conseils régionaux et les structures auxquelles
  la loi confère la qualité de collectivité locale gèrent les affaires locales dans les conditions
  prévues par la loi. » La même loi fait élire une partie de la nouvelle Chambre des conseillers « par
  les membres élus des collectivités locales » (art. 19 nouveau, FR p. 1300 environ, repéré par le
  texte décodé, **à relire à l'image** avant citation). Fascicule à **police décalée** (+29) :
  `pdftotext` illisible tel quel. URL FR `https://www.pist.tn/jort/2002/2002F/Jo0452002.pdf`, AR
  `…/2002/2002A/Ja0452002.pdf` (base). Clé proposée : `loiconst2002-51`.

### 1.4 La loi organique des communes de 1975 et ses lois sœurs

- **Loi n° 75-33 du 14 mai 1975, portant promulgation de la loi organique des communes.**
  - JORT n° 34 du **20 mai 1975**, FR p. 1056-1065 (en-tête relu p. 1056) ; rectificatif JORT n° 53
    du 1er août 1975, p. 1628 (titre seul). URL FR `https://www.pist.tn/jort/1975/1975F/Jo03475.pdf`,
    AR `…/1975/1975A/Ja03475.pdf` (identiques aux fichiers du corpus, `cmp`). Titre AR (d'après les
    visas de textes de 2018, relus) : « القانون عدد 33 لسنة 1975 المؤرخ في 14 ماي 1975 المتعلق بإصدار
    القانون الأساسي للبلديات ». Travaux : adoption par l'Assemblée nationale le 7 mai 1975 (note de bas
    de page, chiffre peu lisible : **à relire**).
  - **Art. 2 de la loi de promulgation** (p. 1056, image agrandie) : abroge « toutes dispositions
    contraires […] et notamment » le décret du 14 mars 1957 portant loi municipale ; la loi n° 59-13
    du 5 février 1959 relative aux syndicats de communes ; la loi n° 59-20 du 5 février 1959 fixant le
    statut des représentants de la commune auprès des sociétés et groupements dans lesquels elle
    détient une participation en capital ; la loi n° 73-50 du 2 août 1973 relative au régime
    administratif de la municipalité de Tunis. (Numéros 59-13 et 59-20 lus sur une image dégradée,
    confirmés par les titres de `jort_cache`.)
  - **Art. 1er de la loi organique** : « La commune est une collectivité publique locale, dotée de la
    personnalité civile et de l'autonomie financière et chargée de la gestion des intérêts municipaux.
    Elle participe dans le cadre du plan national de développement à la promotion économique, sociale
    et culturelle de la localité. » Art. 2 : création par décret sur proposition du ministre de
    l'Intérieur après avis des ministres des Finances et de l'Équipement. Art. 12 : dissolution par
    décret motivé. **Art. 13 : délégation spéciale** en cas de dissolution, de démission de tous les
    membres ou de création d'une commune, nommée par décret, au moins six membres.
  - Clé proposée : `loi75-33`.
- Le même fascicule porte, p. 1065-1069 (titres et pages lus dans la base et sur le sommaire ; corps
  non relu par ce documentaliste, relevant du chapitre 5 et du chapitre 9) : **loi n° 75-34** (taxe
  hôtelière au profit des communes et des conseils de gouvernorat), **loi n° 75-35** (loi organique du
  budget des collectivités publiques locales, p. 1065-1067), **loi n° 75-36** (fonds commun des
  collectivités locales, p. 1067-1068), **loi n° 75-37** (transformation de la caisse des prêts aux
  communes en caisse des prêts et de soutien des collectivités locales, p. 1068), **loi n° 75-38**
  (allègement de la dette des communes et des conseils de gouvernorat), **loi n° 75-39** (taxe sur
  les établissements). Clés proposées (convention) : `loi75-35`, `loi75-36`, `loi75-37`.
  **Le 14 mai 1975 est donc la date d'un paquet de six lois** qui fonde ensemble l'organisation, le
  budget, la péréquation (fonds commun), le crédit (caisse) et deux impôts des collectivités.
- Modificatifs de la loi organique des communes (titres et pages de la base ; dates confirmées par
  l'énumération de l'art. 1er de la loi organique n° 2008-57, FR p. 2413, lue) :
  - loi organique n° 85-43 du 25 avril 1985, JORT n° 34 du 30 avril 1985, p. 642-644 ;
  - loi organique n° **91-24 du 30 avril 1991**, JORT n° 30 du 3 mai 1991, p. 947 — AFD 2018 (p. 34)
    écrit « 20 avril 1991 » : **erreur de la source-guide**, le JORT et la loi de 2008 disent 30 avril ;
  - loi organique n° 95-68 du 24 juillet 1995, JORT n° 59 du 25 juillet 1995, p. 1563-1566 ;
  - loi organique n° 2006-48 du 17 juillet 2006, JORT n° 59 du 25 juillet 2006, p. 1923-1930 ;
    selon AFD 2018 (p. 35), la refonte la plus importante, qui renumérote de nombreux articles (non
    vérifié au texte) ;
  - loi organique n° 2008-57 du 4 août 2008, JORT n° 64 du 8 août 2008, FR p. 2413 (lue) : récrit
    l'art. 56, § 3 — présidents de commune **à plein temps** au chef-lieu de gouvernorat ou au-delà de
    seuils de recettes ordinaires ou d'habitants fixés par décret au début de chaque mandat.
  - Le contenu de 85-43, 91-24, 95-68 et 2006-48 n'a pas été lu. Pour le chapitre, on peut les
    énumérer comme modificatifs (avec leurs références) ou les réserver ; rien n'est à dire de leur
    contenu sans lecture.

### 1.5 Les conseils régionaux (1989-2025)

- **Loi organique n° 89-11 du 4 février 1989, relative aux conseils régionaux.**
  - JORT n° 10 du **10 février 1989**, FR p. 218-221 (image relue p. 218, 219, 221). URL FR
    `https://www.pist.tn/jort/1989/1989F/Jo01089.pdf`, AR `…/1989/1989A/Ja01089.pdf`. Titre AR
    (iort) : « قانون أساسي عدد 11 لسنة 1989 مؤرخ في 4 فيفري 1989 يتعلق بالمجالس الجهوية ». Adoptée
    par la Chambre des députés le 31 janvier 1989.
  - **Art. 1er : « Le gouvernorat est une circonscription territoriale administrative de l'État. Il
    est, en outre, une collectivité publique dotée de la personnalité morale et de l'autonomie
    financière, gérée par un conseil régional et soumise à la tutelle du ministre de l'intérieur. »**
  - Art. 2 : attributions (plan régional de développement, aménagement hors périmètres communaux,
    avis, programmes régionaux…). **Art. 3 : le conseil arrête le budget de fonctionnement et
    d'équipement, et les impôts et taxes dont le recouvrement est assuré au profit de la collectivité
    publique, dans le cadre de la législation en vigueur.**
  - **Art. 6 (composition)** : le gouverneur, président ; les députés élus dans le gouvernorat ; les
    présidents des communes ; les présidents des conseils ruraux (art. 49). Pas d'élection propre.
    Art. 9 : dissolution par décret motivé ; art. 10 : délégation spéciale présidée par le gouverneur.
    Art. 18-21 : nullité et annulation des délibérations par le ministre de l'Intérieur.
  - Art. 49 : conseils ruraux consultatifs dans les zones non érigées en communes.
  - **Art. 57** : patrimoine du conseil de gouvernorat transféré au gouvernorat en tant que
    collectivité publique. **Art. 59 : abroge la loi n° 63-54**. Art. 60 : application au plus tard le
    31 décembre 1989.
  - Clé proposée : `loi-org89-11`.
- Loi organique n° 93-119 du 27 décembre 1993 (complète 89-11), JORT n° 99 du 28 décembre 1993,
  p. 2173-2174 : titre seul.
- Loi n° 94-87 du 26 juillet 1994, création de conseils locaux du développement : titre seul
  (citée dans l'abrogation de 2025, ci-dessous).
- **Loi organique n° 2011-1 du 3 janvier 2011, relative à la composition des conseils régionaux**,
  JORT n° 2 du 7 janvier 2011, FR p. 45 (lue) : ajoute aux conseils régionaux où les députés élus sur
  la base de la répartition nationale des sièges n'excèdent pas 25 % des membres, des membres nommés
  par décret dans cette limite. Clé proposée : `loi-org2011-1`. (Intérêt secondaire.)

### 1.6 2011 : dissolutions et délégations spéciales

- **Décret n° 2011-383 du 8 avril 2011, portant dissolution de certains conseils municipaux du
  territoire tunisien**, JORT n° 26 du **15 avril 2011**, FR p. 468 (lu). Visas : décret-loi
  n° 2011-14 du 23 mars 2011 portant organisation provisoire des pouvoirs publics (art. 16) ; loi
  organique des communes, notamment la loi organique n° 2008-57 « en ses articles 11 et 12 » ; rapport
  du ministre de l'Intérieur du 22 mars 2011 « portant exposé de la situation actuelle des communes ».
  Art. 1er : dissout les conseils de vingt-trois municipalités énumérées (Tunis, Bardo, Carthage, Sidi
  Bou Saïd, La Goulette, La Marsa, Kram ; Kalaat-El-Andalous ; Borj El Amri, Jedeida, El Battan ;
  Nabeul ; Siliana ; Kébili ; Kasserine ; Tataouine ; Jendouba ; Kairouan ; Kef ; Gabès ; Tozeur ;
  Sfax — **recompter** sur le fascicule avant de donner un nombre).
- **Décret n° 2011-384 du 8 avril 2011, portant nomination de délégations spéciales dans certaines
  communes**, même JORT, p. 469 : délégations spéciales « pour remplir les fonctions des conseils
  communaux pendant une durée maximale d'une année » (art. 1er ; visa de l'art. 12 de la loi organique
  des communes). Les noms des membres ne sont pas à reprendre.
- Suite (titres, `jort_cache`, non lus) : une vingtaine de décrets de dissolution d'avril à novembre
  2011 (2011-394, 659, 661, 777, 779, 830, 860, 1091, 1137, 1183, 1207, 2407, 2409, 2907, 3292, 3388,
  4253) et de 2012 (385, 387) ; prorogations des délégations spéciales (décrets n° 2012-578 du 8 juin
  2012, n° 2012-910 du 2 août 2012) ; **décret n° 2012-1122 du 10 août 2012, portant nomination des
  délégations spéciales de l'ensemble des conseils régionaux** (JORT n° 64 du 14 août 2012,
  p. 1900-1901, titre seul). Le texte peut dire que des délégations spéciales nommées remplacent les
  conseils élus à partir d'avril 2011, avec ces références ; **le compte des communes concernées
  n'est pas établi** (fiche `r-fl-dissolutions-2011` proposée, § 4).
- Encore en mai 2018, les arrêtés publiés au JORT n° 39 visent « رئيس النيابة الخصوصية لبلدية … »
  (président de la délégation spéciale) : constat incident, AR p. 1773 environ.

### 1.7 La Constitution de 2014

- **Adoption et publication.** Décision du président de l'Assemblée nationale constituante du
  30 rabia I 1435 - 31 janvier 2014, ordonnant la publication de la Constitution : JORT n° 10 du
  **4 février 2014**, AR p. 316 (lue à l'image), FR p. 331 (sommaire et texte lus : « Les textes sont
  publiés uniquement en langue arabe », note (1)). Contenu de la décision (AR) : la Constitution a été
  **adoptée en séance plénière le 26 janvier 2014**, **scellée le 27 janvier 2014** par le président
  de la République, le président de l'ANC et le chef du gouvernement ; art. 1er : elle « est publiée
  dans un numéro spécial du JORT le lundi 10 février 2014 ». URL FR
  `https://www.pist.tn/jort/2014/2014F/Jo0102014.pdf`, AR `…/2014/2014A/Ja0102014.pdf` (200,
  application/pdf, 5 octobre 2026). Clé proposée pour la décision : `decision-anc-2014-01-31`.
- **Le numéro spécial du 10 février 2014 n'est pas identifié** sur pist.tn ni au corpus (essais
  `Ja0002014`, `Jo0002014`, `Jas2014`, `Constitution2014` : 404 ; `jort_cache` n'a aucune ligne
  datée du 10 février 2014 qui s'y rapporte — la seule, « n° 3 du 10 février 2014 », est un arrêté mal
  rattaché). AFD 2018 (p. 264) cite une traduction française parue dans un « Numéro spécial du JORT du
  20 avril 2015 », non identifié non plus (la base a les n° 31 du 17 avril et 32 du 21 avril 2015).
  Fiche `r-fl-constitution-2014-numero-special` proposée (§ 4).
- **Chapitre VII « Le pouvoir local », art. 131 à 142** — texte connu ici par la traduction que
  reproduisent Dafflon et Gilbert (AFD 2018, p. 267-286, colonne « Constitution du 27 janvier 2014 »),
  qui l'attribuent à ce numéro spécial de 2015 :
  - art. 131 : le pouvoir local est fondé sur la décentralisation ; collectivités locales = communes,
    régions et districts, chacune des catégories couvrant tout le territoire ; catégories particulières
    créées par la loi (p. 267-268) ;
  - art. 132 : personnalité juridique, autonomie administrative et financière ; gestion des intérêts
    locaux selon le **principe de la libre administration** (p. 270) ;
  - art. 133 : conseils élus ; conseils municipaux et régionaux élus au suffrage universel, libre,
    direct, secret ; conseils de district élus par les membres des conseils municipaux et régionaux
    (p. 271) ;
  - art. 134 : **compétences propres, partagées avec l'autorité centrale, déléguées** par elle ;
    partagées et déléguées réparties selon le **principe de subsidiarité** ; pouvoir réglementaire ;
    Journal officiel des collectivités locales (p. 273) ;
  - art. 135 : **ressources propres et ressources déléguées** par l'autorité centrale, adaptées aux
    attributions ; tout transfert de compétence accompagné de ressources ; régime financier fixé par
    la loi (p. 276) ;
  - art. 136 : ressources supplémentaires de l'autorité centrale selon la **solidarité, l'égalisation
    et la péréquation** ; équilibre entre revenus et charges locales ; part des revenus des ressources
    naturelles pour le développement régional (p. 278) ;
  - art. 137 : gestion libre des ressources dans le cadre du budget adopté, sous le contrôle de la
    justice financière (p. 281) ;
  - art. 138 : **contrôle a posteriori de légalité** (p. 282) ;
  - art. 139 : démocratie participative et gouvernance ouverte (p. 283) ;
  - art. 140 : coopération et partenariats, coopération décentralisée (p. 285) ;
  - art. 141 : **Haut Conseil des collectivités locales**, siège hors de la capitale (p. 286) ;
  - art. 142 : la justice administrative statue sur les conflits de compétence (p. 286, AFD).
  - Pour le précis : citer les articles avec la clé de la Constitution **et** la mention qu'on suit
    la traduction reproduite par `dafflon-gilbert-2018` ; ou citer `dafflon-gilbert-2018, p. …`
    seul. Le texte arabe n'est pas lu ici. Clé proposée : `constitution2014` (legislation, sans URL
    tant que le numéro spécial n'est pas identifié ; la note renvoie à la décision du 31 janvier 2014).
  - Le visa du décret présidentiel n° 2017-254 (ci-dessous) confirme l'existence d'un art. 126 de cette
    Constitution (ISIE) : sans intérêt direct.
- Organisation provisoire 2011-2014 : décret-loi n° 2011-14 du 23 mars 2011 (visé en 2011, § 1.6) ;
  loi constituante n° 2011-6 du 16 décembre 2011 (visée par la décision du 31 janvier 2014). Selon
  AFD 2018 (p. 32 et 35), la loi constituante suspend la Constitution de 1959 sans abroger les lois
  qui ne la contredisent pas, de sorte que la loi organique des communes reste en vigueur, et elle
  comporte un article 21 sur les collectivités. Non lu : **piste**, à ne pas écrire comme fait de droit
  sans lecture.

### 1.8 Les communes nouvelles (2015-2017) et les élections de 2018

- Selon AFD 2018 (p. 34-37, encadré 1 et tableau 3, sources JORT citées) : décrets n° 2015-1262 à
  2015-1278 (17 communes), 2015-2131 et 2015-2132, 2016-205, **2016-600 (8 communes) et 2016-601
  (58 communes)** du 26 mai 2016, modifiés en 2017 ; **264 communes en 2014, 350 à la fin de 2017,
  dont 86 nouvelles** ; 24 gouvernorats. Non vérifié au JORT par ce documentaliste (décrets
  gouvernementaux de 2016, n° 600 et 601 : à lire si le chiffre est publié).
- **Le code de 2018 « reconnaît » les communes et régions existantes** (art. 201 et 294, iort, à
  relire) et les liste en annexe : **annexe A « قائمة البلديات », AR p. 1761-1765, et annexe B
  « قائمة الجهات », AR p. 1766-1767** (pages relues à l'image). L'annexe B compte **24 régions**
  (relu). L'annexe A compte **350 communes** d'après la transcription iort
  (`loi_org_2018_29_2018.md`, 350 tirets) ; la mise en page (quatre pages à deux colonnes d'environ
  44 noms) est cohérente ; **recompte au fascicule recommandé** avant d'écrire le chiffre.
- Série possible du nombre de communes, avec sources : 94 (tableau annexé au décret du 14 mars 1957,
  relu) ; 264 (2014) et 350 (fin 2017) d'après AFD 2018 ; 350 (annexe A du code, 15 mai 2018). Elle
  peut faire un petit tableau daté, conforme à la règle « aucun chiffre isolé » ; les états
  intermédiaires (1975, 1985, 2000…) ne sont pas établis (fiche `r-fl-nombre-communes` proposée).
- **Décret présidentiel n° 2017-254 du 19 décembre 2017, portant convocation des électeurs pour les
  élections municipales 2018**, JORT n° 101 du 19 décembre 2017, FR p. 4453 (lu) : électeurs
  convoqués « le dimanche 6 mai 2018 » (militaires et forces de sécurité intérieure : le 29 avril
  2018). Visas : loi organique n° 2014-16 du 26 mai 2014 relative aux élections et référendums,
  modifiée par la **loi organique n° 2017-7 du 14 février 2017** (JORT n° 14 du 17 février 2017,
  p. 731-740, titre seul). Clé proposée : `decret-pres2017-254`.

### 1.9 Le code des collectivités locales (loi organique n° 2018-29)

Clé existante : `loi-org-2018-29-ccl` (commune, FR sans URL ; AR `Ja0392018.pdf`). Édition française
absente (404, déjà consigné). Lu à l'image, AR :

- **Titre** : « قانون أساسي عدد 29 لسنة 2018 مؤرخ في 9 ماي 2018 يتعلّق بمجلة الجماعات المحلية ».
  JORT n° 39 du **15 mai 2018**, AR p. 1710-1767. Adoption par l'ARP le 26 avril 2018 (note (1),
  p. 1710).
- Pas de visas : « باسم الشعب، وبعد مصادقة مجلس نواب الشعب » (p. 1710).
- Art. 1er (p. 1710) : objet — règles d'organisation des structures du **pouvoir local**
  (« هياكل السلطة المحلية »), de leurs compétences et de leur fonctionnement selon la démocratie
  participative, « بما يحقّق اللامركزية والتنمية الشاملة والعادلة والمستدامة في إطار وحدة الدولة ».
- **Art. 2** : « الجماعات المحلية ذوات عمومية تتمتّع بالشخصية القانونية والاستقلالية الإدارية والمالية
  وتتكوّن من بلديات وجهات وأقاليم يغطّي كل صنف منها كامل تراب الجمهورية ». Art. 3 : création et
  limites par la loi. **Art. 4 : libre administration, « مبدأ التدبير الحر »**. Art. 5 : conseils
  élus. Art. 9 : charges de personnel plafonnées à **50 % des ressources ordinaires réelles**
  (« خمسين بالمائة من الموارد الاعتيادية المحققة ») — relève du chapitre 5.
- **Dispositions transitoires, livre III, art. 383-400** (AR p. 1759-1760, relues) :
  - **art. 383** : entrée en vigueur **progressive**, catégorie par catégorie, après la proclamation
    des résultats définitifs de leurs élections ; **les dispositions relatives à l'élaboration et à
    l'adoption du budget n'entrent en vigueur qu'au 1er janvier de l'année qui suit** cette
    proclamation ; jusqu'à l'entrée en vigueur du fonds de soutien à la décentralisation, appui annuel
    égal à celui de 2018 augmenté d'un taux fixé par la loi de finances ;
  - art. 384 : jusqu'à l'installation des conseils régionaux élus, la région agit par les conseils
    régionaux de la loi organique n° 89-11 ;
  - art. 390 : comptabilité en partie double dans les quatre ans ; art. 391 : fin progressive des
    art. 46 à 95 du code de la fiscalité locale (déjà au chapitre 8) ; art. 392 : fin des art. 13 à 15
    de la LF 2013 (fonds de coopération) à la création du fonds de soutien ; art. 394 : part des
    districts aux communes et part de la région au gouvernorat jusqu'aux élections ; art. 397 :
    biens du gouvernorat-collectivité transférés à la région ; art. 399 : Haute instance des finances
    locales nommée par décret gouvernemental jusqu'au Haut Conseil.
  - **Aucun article des dispositions transitoires n'abroge expressément la loi organique des
    communes (75-33) ni la loi n° 75-35** (lecture des art. 383-400 et recherche de « تلغى/يلغى » dans
    la transcription iort : seules occurrences sans rapport). Le chapitre ne doit donc pas écrire que
    le code « abroge » la loi de 1975 ; il peut écrire qu'il la remplace pour les communes élues, selon
    l'art. 383, et que la loi n° 2025-4 se réfère encore à la loi n° 75-35 (§ 1.11).
- **Conséquence datée pour les communes** : proclamation des résultats des municipales du 6 mai 2018
  au cours de 2018 → dispositions budgétaires du code applicables aux communes **à partir du
  1er janvier 2019**. La date de proclamation des résultats définitifs n'est pas relevée ici
  (décisions de l'ISIE de 2018 : à chercher), mais toute date de 2018 donne le même 1er janvier 2019.
  Les conseils régionaux n'ayant jamais été élus sous ce code, ses dispositions sur la région ne sont
  pas entrées en vigueur selon l'art. 383 (à formuler prudemment : constat sur les textes lus).
  **Ceci résout le TODO du chapitre 8** (`_taxes_redevances.qmd`, § « La transition », premier des
  trois points) : à signaler à l'orchestrateur, sans modifier ce chapitre.

### 1.10 La Constitution de 2022

- **Décret présidentiel n° 2022-691 du 17 août 2022, portant promulgation de la Constitution de la
  République tunisienne**, JORT n° 91 du **18 août 2022**, FR et AR p. 2473 (FR lu : « Traduction
  française pour information »). Article unique : promulgation et publication « dans un numéro spécial
  du Journal officiel ». Dépôt au gouvernorat de Tunis le 18 août 2022 (dernière page FR). Visas :
  décret présidentiel n° 2022-506 du 25 mai 2022 (convocation au référendum du 25 juillet 2022) ;
  décision ISIE n° 2022-22 du 16 août 2022 (résultats définitifs). URL FR
  `https://www.pist.tn/jort/2022/2022F/Jo0912022.pdf`, AR `…/2022/2022A/Ja0912022.pdf` (200). Clé
  proposée : `decret-pres2022-691`.
- **Numéro spécial du 18 août 2022 (AR seulement)** : pist.tn le sert sous
  `https://www.pist.tn/jort/2022/2022A/Ja0922022.pdf` (200, application/pdf, 10 966 991 octets ; fichier
  au corpus local) ; la couverture porte « عدد خاص », « الخميس 20 محرم 1444 – 18 أوت 2022 », sans
  numéro ; l'adresse française `Jo0922022.pdf` rend 404. Texte calligraphié, pagination propre au
  numéro (1 à 50 environ). Lu à l'image :
  - **art. 75** (p. 23 du numéro) : la loi ordinaire fixe notamment « ضبط قاعدة الأداءات والمساهمات
    ونسبها وإجراءات استخلاصها » (assiette, taux et recouvrement des impôts et contributions) ;
  - **art. 81** (p. 26) : section II « المجلس الوطني للجهات والأقاليم » (**Conseil national des régions
    et des districts**) : élus des régions et des districts ; chaque conseil régional élit trois de
    ses membres ; les élus des conseils régionaux de chaque district élisent un député par district ;
  - **art. 84** (p. 27) : les projets relatifs au budget de l'État et aux plans de développement
    régionaux, de district et nationaux sont soumis obligatoirement au Conseil national des régions et
    des districts ; loi de finances et plans adoptés à la majorité des présents de chacune des deux
    chambres, au moins le tiers de leurs membres ; **art. 85** : contrôle de l'exécution du budget et
    des plans ;
  - **chapitre VII « الجماعات المحلية والجهوية » (« Les collectivités locales et régionales »),
    art. 133, article unique** (p. 44) : « تمارس المجالس البلدية والمجالس الجهوية ومجالس الأقاليم
    والهياكل التي يمنحها القانون صفة الجماعة المحلية، المصالح المحلية والجهوية حسبما يضبطه القانون ».
    Traduction à valider : les conseils municipaux, les conseils régionaux, les conseils de district et
    les structures auxquelles la loi confère la qualité de collectivité locale gèrent les intérêts
    locaux et régionaux dans les conditions fixées par la loi. **Rédaction proche, mot pour mot sur sa
    trame, de l'art. 59 de 1959 et de l'art. 71 (nouveau) de 2002** : à dire comme constat de texte,
    sans commentaire.
  - Traduction française officielle : non identifiée (pas d'édition FR du numéro spécial).
  - Clé proposée : `constitution2022` (legislation, AR seulement ; FR sans URL).

### 1.11 Après 2022 : dissolution, conseils locaux, districts, loi de 2025

- **Décret-loi n° 2023-9 du 8 mars 2023, relatif à la dissolution des conseils municipaux.**
  - Titre AR : « مرسوم عدد 9 لسنة 2023 مؤرّخ في 8 مارس 2023 يتعلق بحلّ المجالس البلدية ». JORT n° 24 du
    **9 mars 2023**, AR p. 694 (lu à l'image). Le JORT n° 24 n'a **pas d'édition française** (pist.tn
    404 ; base : `pdf_fr` vide, `numero` vide — recid 171303, pages données « 0691-0694 », alors que
    le décret-loi tient sur la p. 694). URL AR `https://www.pist.tn/jort/2023/2023A/Ja0242023.pdf`.
  - Art. 1er : « يتمّ حلّ جميع المجالس البلدية إلى حين انتخاب مجالس بلدية جديدة ». **Art. 2 : la
    gestion des affaires courantes de la commune est confiée à « المكلف بالكتابة العامة للبلدية »
    (le chargé du secrétariat général de la commune), « تحت إشراف والي الجهة » (sous la supervision du
    gouverneur)**. Art. 3 : abrogation des dispositions contraires.
  - Dépôt au siège du gouvernorat de Tunis le **9 mars 2023** (dernière page du fascicule) ; pas de
    clause d'effet → **exécutoire le 14 mars 2023** (9 mars + 5 jours, jour du dépôt non compté).
  - Clé proposée : `decretloi2023-9`.
- **Décret-loi n° 2023-8 du 8 mars 2023** (même JORT, p. 691-694) : modifie la loi organique
  n° 2014-16 (élections) — notamment les élections municipales (scrutin uninominal par circonscription,
  art. 117 bis et suiv. nouveaux) ; **art. 6 : abroge les dispositions contraires, notamment celles du
  code des collectivités locales**. Clé proposée : `decretloi2023-8` (intérêt secondaire).
- **Décret-loi n° 2023-10 du 8 mars 2023, relatif à l'organisation des élections des conseils locaux
  et à la composition des conseils régionaux et des conseils de districts.**
  - Titre AR : « مرسوم عدد 10 لسنة 2023 مؤرّخ في 8 مارس 2023 يتعلّق بتنظيم انتخابات المجالس المحلّية
    وتركيبة المجالس الجهويّة ومجالس الأقاليم ». JORT n° 24 du 9 mars 2023, AR p. 694-698 (lu p. 694,
    695, 698).
  - **Art. 1er, al. 2 : « تعتبر المجالس المحلية والجهوية ومجالس الأقاليم جماعات محلية وجهوية طبقا للباب
    السابع من الدستور »** (conseils locaux, régionaux et de districts sont des collectivités locales et
    régionales au sens du chapitre VII de la Constitution).
  - Art. 3 : membres des conseils locaux, régionaux, de districts et du Conseil national élus pour
    **cinq ans**. Art. 6 : électeurs du conseil local = inscrits des **imadas** (« العمادات ») du conseil.
    **Art. 7 : électeurs du conseil régional = les membres des conseils locaux élus de la région ; le
    territoire du conseil régional coïncide avec celui du gouvernorat (« الولاية »).** Art. 8 : électeurs
    du conseil de district = membres des conseils régionaux élus du district ; territoire et
    gouvernorats de chaque district fixés par décret. Art. 9 : électeurs du Conseil national = membres
    des conseils régionaux et de districts. Art. 28 : chaque imada = circonscription d'élection du
    conseil local (p. 696, titre relevé par texte, à relire si cité).
  - **Art. 43 : abroge les dispositions contraires, notamment celles du code des collectivités
    locales.**
  - Même dépôt (9 mars 2023) → exécutoire le 14 mars 2023.
  - Clé proposée : `decretloi2023-10`.
- **Décret n° 2023-588 du 21 septembre 2023** (convocation des électeurs pour l'élection des membres
  des conseils locaux, **le dimanche 24 décembre 2023**) et **décret n° 2023-589 du 21 septembre 2023,
  relatif à la délimitation du territoire des districts de la République tunisienne et des gouvernorats
  qui relèvent de chacun d'eux** : JORT n° 108 du **22 septembre 2023**, AR p. 5097-5098 (lus à
  l'image ; pas d'édition FR : `pdf_fr` vide ; la base porte à tort `numero = 2023-108`). Titre AR
  du second : « أمر عدد 589 لسنة 2023 مؤرخ في 21 سبتمبر 2023 يتعلق بتحديد تراب أقاليم الجمهورية التونسية
  والولايات الراجعة بالنظر لكل إقليم ». Visas : Constitution, notamment son art. 133 ; loi organique
  n° 2018-29 ; décret-loi n° 2023-10, notamment son art. 8.
  - **Art. 1er : cinq districts** : I — Bizerte, Béja, Jendouba, Le Kef ; II — Tunis, Ariana, Ben
    Arous, Zaghouan, Manouba, Nabeul ; III — Siliana, Sousse, Kasserine, Kairouan, Monastir, Mahdia ;
    IV — Tozeur, Sidi Bouzid, Sfax, Gafsa ; V — Tataouine, Gabès, Kébili, Médenine. (Noms
    translittérés par nous ; vérifier l'ordre et l'orthographe à la relecture.) Art. 2 : le conseil
    se réunit au siège d'un gouvernorat du district, siège tournant tous les six mois. Art. 3 : les
    gouvernorats mettent à disposition les moyens humains et matériels.
  - Clés proposées : `decret2023-588`, `decret2023-589`. URL AR
    `https://www.pist.tn/jort/2023/2023A/Ja1082023.pdf` (200).
- Installations suivantes (titres seuls, `jort_cache`, éditions FR existantes) : décision ISIE
  n° 2024-538 du 18 mars 2024 (résultats définitifs des élections des conseils de districts),
  n° 2024-539 du 3 avril 2024 (Conseil national des régions et des districts) ; décret n° 2024-196 du
  16 avril 2024 (convocation de sa séance inaugurale), JORT n° 49 du 16 avril 2024. Non lus.
- **Loi organique n° 2025-4 du 12 mars 2025, relative aux conseils locaux, conseils régionaux et
  conseils de districts.**
  - Titre AR : « قانون أساسي عدد 4 لسنة 2025 مؤرخ في 12 مارس 2025 يتعلق بالمجالس المحلية والمجالس الجهوية
    ومجالس الأقاليم ». JORT n° 30 du **13 mars 2025**, FR p. 706-707 (« Traduction française pour
    information », lu intégralement), AR p. 706. URL FR `https://www.pist.tn/jort/2025/2025F/Jo0302025.pdf`,
    AR `…/2025/2025A/Ja0302025.pdf` (200). Adoptée par l'ARP le 27 février 2025. Dépôt au gouvernorat
    de Tunis le 13 mars 2025 (FR et AR) → **exécutoire le 18 mars 2025**.
  - **Art. 1er** : ces conseils « sont considérés comme des collectivités locales jouissant de la
    personnalité juridique et de l'autonomie administrative et financière » ; ils délibèrent sur les
    projets de plans de développement locaux, régionaux et de districts, « dans le cadre de l'unité de
    l'État » ; organisation et fonctionnement fixés **par décret**. Art. 3 : session au moins mensuelle.
    Art. 4 : indemnité mensuelle des élus fixée par décret. **Art. 5 : régis par la loi organique
    relative au budget desdits conseils et par la loi relative à la comptabilité publique ; le
    président du conseil est ordonnateur.** Art. 7 : siège du conseil local = siège de la délégation ;
    du conseil régional et du conseil de district = siège du gouvernorat. **Art. 8 : élaboration et
    adoption du budget régies par la loi organique n° 75-35 du 14 mai 1975, « dans la mesure où elles
    ne sont pas contraires »** (la loi de 1975 est donc tenue pour en vigueur en 2025). **Art. 9 : les
    biens, le patrimoine, les participations et les dotations du conseil régional au sens de la loi
    n° 89-11 sont transférés à l'État et mis à la disposition du gouverneur.** **Art. 10 : abroge les
    dispositions contraires, « notamment les dispositions relatives à la région et au district prévues
    à la loi organique n° 2018-29 », la loi organique n° 89-11 et la loi n° 94-87.**
  - Ce que la loi **laisse** du code de 2018 : elle n'abroge nommément que ses dispositions sur la
    région et le district ; les dispositions communes et celles sur la commune ne sont pas visées
    (sauf contrariété). Les conseils municipaux restent dissous (décret-loi n° 2023-9). À dire ainsi,
    sans conclure sur l'état d'ensemble du code.
  - Clé proposée : `loi-org2025-4`.
- Textes d'application de 2025 (titres seuls) : décret n° 2025-177 du 4 avril 2025 (organisation des
  travaux et fonctionnement des conseils), décret n° 2025-178 du 4 avril 2025 (indemnité de
  représentation des membres), JORT n° 41 du 5 avril 2025, p. 836-837. Non lus.
- **Élections municipales après la dissolution de 2023** : aucun texte de convocation n'est identifié
  dans la base (`jort_cache`, couverte jusqu'au 18 septembre 2026). Fiche `r-fl-municipales-apres-2023`
  proposée (§ 4).

## 2. Termes arabes relevés dans les textes (pour le terminologue)

| FR | AR | Texte où relevé |
|---|---|---|
| loi municipale | قانون البلديات | décret du 14 mars 1957, AR p. 416 |
| loi organique des communes | القانون الأساسي للبلديات | visas de 2011-2018 (ex. AR JORT n° 39/2018, p. 1767 env.) |
| conseil municipal / conseils municipaux | المجلس البلدي / المجالس البلدية | Constitution 1959 (p. 757), DL 2023-9 |
| conseil régional / conseils régionaux | المجلس الجهوي / المجالس الجهوية | loi org. 89-11 (iort), Constitution 1959, DL 2023-10 |
| collectivités locales (1959) | الجماعات المحلية | intitulé du ch. VIII, Constitution 1959 |
| collectivités locales | الجماعات المحلية | code 2018, art. 2 |
| collectivités locales et régionales (2022) | الجماعات المحلية والجهوية | intitulé du ch. VII, Constitution 2022 |
| structures du pouvoir local | هياكل السلطة المحلية | code 2018, art. 1er |
| libre administration | التدبير الحر | code 2018, art. 4 (titre de section) |
| commune / région / district | بلدية / جهة / إقليم (pl. أقاليم) | code 2018, art. 2 ; décret 2023-589 |
| conseil local / conseils locaux | المجلس المحلي / المجالس المحلية | DL 2023-10 ; loi org. 2025-4 |
| conseil de district | مجلس الإقليم (pl. مجالس الأقاليم) | DL 2023-10 ; loi org. 2025-4 |
| Conseil national des régions et des districts | المجلس الوطني للجهات والأقاليم | Constitution 2022, art. 81 |
| délégation spéciale | النيابة الخصوصية | arrêtés du JORT n° 39/2018 (« رئيس النيابة الخصوصية ») |
| gouvernorat / gouverneur | الولاية / الوالي | DL 2023-9, DL 2023-10 |
| délégation (circonscription) | المعتمدية | DL 2023-10 |
| imada (secteur) | العمادة | DL 2023-10 |
| Haute instance des finances locales | الهيئة العليا للمالية المحلية | code 2018, art. 399 |
| conseil de gouvernorat | مجلس الولاية — **non relevé** dans les textes lus (l'arabe de la loi 57-12 n'a pas été lu) | à relever dans Ja00957 / Ja06063 |

## 3. Références candidates

Toutes de type `legislation`, `container-title` « Journal officiel de la République tunisienne »
(« Journal officiel tunisien » pour mars 1957), avec `title-short`, `issue`, `page` et URL pist.tn de
l'édition de la langue du fichier. **Existantes** : `loi-org-2018-29-ccl`, `loi93-64`,
`loi97-11`, `dafflon-gilbert-2018`.

| Clé proposée | Texte | JORT | Pages | URL FR | URL AR |
|---|---|---|---|---|---|
| `decret-1957-03-14-loi-municipale` | Décret du 14 mars 1957 portant loi municipale | 15 mars 1957 (n° 22 selon la base) | FR 296-305 ; AR 416 et s. | 1957F/Jo12257.pdf | 1957A/Ja12257.pdf |
| `loi57-12` | Loi n° 57-12 du 17 août 1957, création de conseils de gouvernorat | n° 9, 23 août 1957 | 80-82 | 1957F/Jo00957.pdf | 1957A/Ja00957.pdf |
| `loi59-57-constitution` | Loi n° 59-57 du 1er juin 1959, promulgation de la Constitution | n° 30, 1er juin 1959 | AR 757 (ch. VIII) | — (404 / absent) | 1959A/Ja03059.pdf |
| `loi63-54` | Loi n° 63-54 du 30 décembre 1963, conseils de gouvernorat | n° 60, 31 déc. 1963 | 1873-1875 | 1963F/Jo06063.pdf | 1963A/Ja06063.pdf |
| `loi75-33` | Loi n° 75-33 du 14 mai 1975, loi organique des communes | n° 34, 20 mai 1975 | 1056-1065 | 1975F/Jo03475.pdf | 1975A/Ja03475.pdf |
| `loi75-35`, `loi75-36`, `loi75-37` | lois du 14 mai 1975 (budget ; fonds commun ; caisse des prêts) | n° 34, 20 mai 1975 | 1065-1067 ; 1067-1068 ; 1068 | idem | idem |
| `loi-org89-11` | Loi organique n° 89-11 du 4 février 1989, conseils régionaux | n° 10, 10 févr. 1989 | 218-221 | 1989F/Jo01089.pdf | 1989A/Ja01089.pdf |
| `loiconst2002-51` | Loi constitutionnelle n° 2002-51 du 1er juin 2002 | n° 45, 3 juin 2002 | 1298-1309 (art. 71 : FR 1306) | 2002F/Jo0452002.pdf | 2002A/Ja0452002.pdf |
| `loi-org2008-57` | Loi organique n° 2008-57 du 4 août 2008 (modifie la loi org. des communes) | n° 64, 8 août 2008 | 2413 | 2008F/Jo0642008.pdf | 2008A/Ja0642008.pdf |
| `loi-org2011-1` | Loi organique n° 2011-1 du 3 janvier 2011, composition des conseils régionaux | n° 2, 7 janv. 2011 | 45 | 2011F/Jo0022011.pdf | 2011A/Ja0022011.pdf |
| `decret2011-383` / `decret2011-384` | Décrets du 8 avril 2011 (dissolution ; délégations spéciales) | n° 26, 15 avril 2011 | 468 ; 469 | 2011F/Jo0262011.pdf | 2011A/Ja0262011.pdf |
| `decision-anc-2014-01-31` | Décision du président de l'ANC du 31 janvier 2014 ordonnant la publication de la Constitution | n° 10, 4 févr. 2014 | FR 331 ; AR 316 | 2014F/Jo0102014.pdf | 2014A/Ja0102014.pdf |
| `constitution2014` | Constitution de la République tunisienne du 27 janvier 2014 | numéro spécial du 10 févr. 2014 (non identifié) | — | — | — |
| `decret-pres2017-254` | Décret présidentiel n° 2017-254 du 19 déc. 2017, convocation des électeurs (municipales 2018) | n° 101, 19 déc. 2017 | 4453 | 2017F/Jo1012017.pdf | 2017A/Ja1012017.pdf |
| `decret-pres2022-691` | Décret présidentiel n° 2022-691 du 17 août 2022, promulgation de la Constitution | n° 91, 18 août 2022 | 2473 | 2022F/Jo0912022.pdf | 2022A/Ja0912022.pdf |
| `constitution2022` | Constitution de la République tunisienne (référendum du 25 juillet 2022) | numéro spécial du 18 août 2022 | AR numéro spécial, p. 23-27, 44 | — (404) | 2022A/Ja0922022.pdf |
| `decretloi2023-9` | Décret-loi n° 2023-9 du 8 mars 2023, dissolution des conseils municipaux | n° 24, 9 mars 2023 | AR 694 | — (404) | 2023A/Ja0242023.pdf |
| `decretloi2023-10` | Décret-loi n° 2023-10 du 8 mars 2023, élections des conseils locaux… | n° 24, 9 mars 2023 | AR 694-698 | — (404) | 2023A/Ja0242023.pdf |
| `decret2023-589` | Décret n° 2023-589 du 21 sept. 2023, territoire des districts | n° 108, 22 sept. 2023 | AR 5097-5098 | — (absent) | 2023A/Ja1082023.pdf |
| `loi-org2025-4` | Loi organique n° 2025-4 du 12 mars 2025, conseils locaux, régionaux et de districts | n° 30, 13 mars 2025 | 706-707 | 2025F/Jo0302025.pdf | 2025A/Ja0302025.pdf |

URL contrôlées le 5 octobre 2026 (`curl -sk`, 200 application/pdf) : 2025 n° 30 FR et AR, 2022 n° 91
FR et AR, 2022 numéro spécial AR (`Ja0922022`), 2023 n° 24 AR et n° 108 AR, 2018 n° 39 AR, 2014 n° 10
FR et AR, 1957 `Jo12257`/`Ja12257`, 1957 n° 9 FR et AR, 1963 n° 60 FR et AR, 1989 n° 10 FR et AR,
1975 n° 34 FR, 1959 n° 30 AR, 2002 n° 45 FR et AR, 2011 n° 26 FR et AR, 2017 n° 101 FR. 404 : 2022
`Jo0922022`, 2023 `Jo0242023`, 1959 `Jo03059`. Non contrôlées : 1975 n° 34 AR (fichier identique au
corpus, `cmp`), 2017 n° 101 AR, 2008 n° 64, 2011 n° 2, 2023 n° 24 FR (404 relevé plus haut) — à
contrôler par le bibliographe au versement. Les fichiers français antérieurs à 2000 sont des images
sans couche texte (ceux de 2000-2006 peuvent avoir une police décalée : cas du n° 45 de 2002).

Doctrine : `dafflon-gilbert-2018` (existante) pour ch. 2 et 7. Ben Jelloul, *Le foncier urbain en
Tunisie* (CPU, 2017), et son compte rendu (Jadaliyya, 2018, fichier local) : rien sur l'histoire
municipale dans le compte rendu (680 mots, lu) ; l'ouvrage n'est pas en accès libre. Rapports
« Stratégie de l'habitat » 2014 (Ben Othman Bacha, partie I, p. 6-25) : histoire foncière, piste non
exploitée pour ce chapitre.

## 4. Fiches RECHERCHE proposées

```yaml
- id: r-fl-constitution-2014-numero-special
  objet: numéro spécial du JORT publiant la Constitution du 27 janvier 2014 (10 février 2014), et sa traduction française (numéro spécial du 20 avril 2015 selon AFD 2018)
  ou: [precis/fr/finances_locales/_histoire.qmd#sec-fl-hist-2014]
  requetes:
    titres_like: ['%constitution de la republique%']
    plein_texte: []
    depuis: 2014-01-27
  passes:
  - date: 2026-10-05
    role: documentaliste
    sources: [jort_cache, corpus_local, pist]
    couverture: "jort_cache : seule la décision du 31 janvier 2014 (JORT n° 10) ; aucune ligne du 10 février 2014 ni du 20 avril 2015 qui s'y rapporte ; corpus local 2014 sans fichier hors numérotation ; pist.tn : Ja0002014, Jo0002014, Jas2014, Constitution2014 en 404"
    couvert_jusqu_au: 2015-04-21
    resultat: aucun
  a_faire: [demander à l'IORT la cote du numéro spécial ; essayer d'autres noms de fichiers sur pist.tn]
- id: r-fl-municipales-apres-2023
  objet: texte convoquant des élections municipales après la dissolution des conseils par le décret-loi n° 2023-9
  ou: [precis/fr/finances_locales/_histoire.qmd#sec-fl-hist-apres-2022]
  requetes:
    titres_like: ['%conseils municipaux%', '%elections municipales%']
    iort_ar: [المجالس البلدية, الانتخابات البلدية]
    depuis: 2023-03-09
  passes:
  - date: 2026-10-05
    role: documentaliste
    sources: [jort_cache]
    couverture: "titres jort_cache 2023-2026 (LIKE FR et AR) ; plein texte non parcouru"
    couvert_jusqu_au: 2026-09-18
    resultat: aucun
- id: r-fl-dissolutions-2011
  objet: liste et nombre des conseils municipaux dissous et des délégations spéciales nommées en 2011-2012
  ou: [precis/fr/finances_locales/_histoire.qmd#sec-fl-hist-2011]
  requetes:
    titres_like: ['%dissolution de certains conseils municipaux%', '%delegations speciales%']
    depuis: 2011-01-14
  passes:
  - date: 2026-10-05
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: "titres jort_cache 2011-2014 relevés (une vingtaine de décrets de dissolution) ; seul le décret n° 2011-383 lu"
    couvert_jusqu_au: 2014-12-31
    resultat: aucun
  a_faire: [lire chaque décret de dissolution et compter les communes]
- id: r-fl-nombre-communes
  objet: nombre de communes à des dates intermédiaires entre 1957 et 2014
  ou: [precis/fr/finances_locales/_histoire.qmd#sec-fl-hist-carte]
  requetes:
    titres_fts: ['"creation d''une commune"']
    depuis: 1957-03-15
  passes:
  - date: 2026-10-05
    role: documentaliste
    sources: [corpus_local]
    couverture: "seuls le tableau annexé au décret du 14 mars 1957 (94 communes) et l'annexe A du code de 2018 ont été lus"
    couvert_jusqu_au: 2018-05-15
    resultat: aucun
```

Les requêtes ci-dessus sont celles réellement lancées (LIKE sur `titre`, FTS non lancé pour les deux
dernières : à `elargir` au versement si l'on veut les rejouer). Le format exact est à valider par
`recherches.py` (l'orchestrateur les verse ; ce documentaliste n'écrit pas dans `recherches.yml`).

## 5. Lacunes

- Pré-1956 : aucun texte lu ; seulement visas (1945, 1952, 1954, 1956 ; 1922, 1952 pour les conseils
  de caïdat ; 1945 pour les finances locales) et abrogations. La « municipalité de Tunis » de 1858 et
  les commissions municipales du protectorat, parfois citées, ne sont établies par aucune source lue :
  **ne rien écrire**.
- Renumérotation de l'art. 59 → 71 de la Constitution de 1959 (loi constitutionnelle de 1976 ?).
- Contenu des lois organiques 85-43, 91-24, 95-68, 2006-48.
- Texte arabe de la Constitution de 2014 et son numéro spécial.
- Résultats définitifs des municipales de 2018 (décision ISIE) : date exacte non relevée.
- Arabe de « conseil de gouvernorat » (loi 57-12, 63-54).
- Nombre exact des communes de l'annexe A de 2018 au fascicule (350 d'après iort).
- Âge électoral de 1957 (art. 7) à relire.

## 6. Plan proposé du chapitre

`# Histoire des collectivités et de leurs finances {#sec-fl-histoire}` — rappel des notions
(décentralisation, déconcentration, collectivité locale, libre administration, tutelle), annonce du plan,
avertissement sur les sources d'avant 1956 (formule neutre).

- `## Avant l'indépendance {#sec-fl-hist-avant-1956}` (court, sans subdivision) : ce que disent les
  visas de 1957 (décrets de 1945, 1952, 1954 sur les municipalités ; 1922 et 1952 sur les conseils de
  caïdat ; 8 novembre 1945 sur les finances locales) et les abrogations de 1997 (taxes de 1887 à 1956,
  renvoi au chapitre 6).
- `## Les institutions de l'indépendance, 1957-1975 {#sec-fl-hist-1957}`
  - `### La loi municipale de 1957 {#sec-fl-hist-loi-municipale}` — collectivité de droit public,
    conseil élu au suffrage universel direct, 94 communes ; budget arrêté par deux ministres, recettes
    de l'art. 106, seuil de déficit de 20 %.
  - `### Les conseils de gouvernorat {#sec-fl-hist-conseils-gouvernorat}` — 1957 (conseil nommé, région
    personne civile, recouvrement par l'État contre 5 %), 1963 (collectivité publique, composition
    partisane et représentative, tutelle du secrétaire d'État à l'Intérieur).
  - `### La Constitution de 1959 {#sec-fl-hist-1959}` — art. 59 (puis 71).
- `## Les lois de 1975 et leurs réformes {#sec-fl-hist-1975}`
  - `### Le paquet du 14 mai 1975 {#sec-fl-hist-paquet-1975}` — six lois ; loi organique des communes
    (art. 1er, délégation spéciale) ; renvois en prose aux chapitres des budgets (§ 75-35), des
    transferts (75-36, 75-37) et des impôts (75-34, 75-39).
  - `### Les conseils régionaux de 1989 {#sec-fl-hist-1989}` — gouvernorat double, tutelle du
    ministre de l'Intérieur, composition non élue, abrogation de 1963.
  - `### Les modifications jusqu'en 2011 {#sec-fl-hist-modifications}` — 85-43 à 2008-57 (liste
    datée), art. 71 nouveau de 2002, loi 2011-1.
- `## La décentralisation constitutionnelle, 2011-2022 {#sec-fl-hist-2011-2022}`
  - `### 2011 : dissolutions et délégations spéciales {#sec-fl-hist-2011}`
  - `### La Constitution de 2014 {#sec-fl-hist-2014}` — chapitre VII (art. 131-142), d'après la
    traduction reproduite par Dafflon et Gilbert ; ancre RECHERCHE du numéro spécial.
  - `### La carte communale et les élections de 2018 {#sec-fl-hist-carte}` — 264 → 350 communes,
    tableau daté (1957, 2014, 2017, 2018) ; municipales du 6 mai 2018.
  - `### Le code des collectivités locales {#sec-fl-hist-code-2018}` — art. 1-5, entrée en vigueur
    progressive (art. 383), budget au 1er janvier 2019 pour les communes, régions non élues.
- `## Depuis 2022 {#sec-fl-hist-apres-2022}`
  - `### La Constitution de 2022 {#sec-fl-hist-2022}` — art. 133 (rédaction de 1959 élargie),
    Conseil national des régions et des districts (art. 81, 84, 85).
  - `### Dissolution des conseils municipaux et nouveaux conseils {#sec-fl-hist-2023-2025}` —
    DL 2023-9 et 2023-10, cinq districts, élections du 24 décembre 2023, loi organique 2025-4
    (art. 1er, 5, 8, 9, 10) ; ancre RECHERCHE des municipales.
- `## La longue période {#sec-fl-hist-longue-periode}` — tableau chronologique des textes fondateurs
  (date, texte, ce qui change : statut, mode de désignation des conseils, tutelle) et tableau du nombre
  de communes ; renvoi en prose au chapitre de la longue période.

Toutes les sections subdivisées ont au moins deux sous-sections (règle 5 de `check_numerotation`).
Ancres à ne pas réutiliser : `sec-fl-budget`, `sec-fl-tutelle`, `sec-fl-transferts`,
`sec-fl-perequation` (existent dans `_notions.qmd`).

## 7. Notions mobilisées (rappel en tête de chapitre)

- Ancres de `_notions.qmd` : `@sec-fl-trois-volets` (déconcentration, délégation, dévolution),
  `@sec-fl-libre-administration`, `@sec-fl-subsidiarite`, `@sec-fl-tutelle`, `@sec-fl-regle-or`
  (pour le seuil de déficit de 1957), `@sec-fl-autonomie` (autonomie financière des textes),
  `@sec-fl-perequation` (art. 136 de 2014).
- Glossaire existant : `#g-decentralisation`, `#g-deconcentration`, `#g-delegation-competences`,
  `#g-devolution-competences`, `#g-collectivite-locale`, `#g-libre-administration`,
  `#g-subsidiarite`, `#g-tutelle`, `#g-autonomie-financiere`, `#g-perequation-financiere`.
- Notions nouvelles candidates au glossaire (terme du texte) : délégation spéciale
  (النيابة الخصوصية), conseil régional (المجلس الجهوي), conseil local (المجلس المحلي), district
  (إقليم), Conseil national des régions et des districts (المجلس الوطني للجهات والأقاليم), loi
  organique des communes (القانون الأساسي للبلديات).
- Point de vocabulaire à signaler dans le texte : la « libre administration » de Dafflon et Gilbert
  et l'« التدبير الحر » du code de 2018 ; la Constitution de 2022 n'emploie plus ni « pouvoir local »
  ni « libre administration » dans son art. 133 (constat sur le texte lu, à formuler sans jugement).
