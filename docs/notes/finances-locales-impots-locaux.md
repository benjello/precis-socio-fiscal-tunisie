# Volume VII « Les finances locales », chapitres 6 à 8 : note documentaire sur les impôts locaux

> Note du documentaliste, 4 octobre 2026. Elle sert l'étape 1 du plan
> (`docs/notes/fiscalite-locale-plan.md`, version du commit 017dd06) pour trois chapitres :
> ch. 6, impôts sur les immeubles ; ch. 7, impôts sur l'activité ; ch. 8, taxes, redevances et
> autonomie fiscale. Rien n'y est rédigé pour le précis.
>
> **Sources.** Les textes ont été lus dans le *Journal officiel* : fascicules du corpus local
> (`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`), contrôlés sur pist.tn. Les métadonnées
> viennent de `jort_cache.db`, dernière publication indexée le 18 septembre 2026. Deux documents
> ont servi de guides pour repérer les textes, jamais de source finale : le manuscrit Gilbert
> de 2013 (ch. 4, tableaux 4-1 à 4-3) et le livre Dafflon et Gilbert (AFD, 2018), ch. 5. Les
> rapports de 2014 signalés par le coordinateur (Ben Othman Bacha, Belaid) citent les décrets
> 97-432 et 2007-1186, ainsi que l'assiette de 2 % et les taux de 8 à 14 % de la TIB. Le JORT
> confirme les trois points (§ 2 et 3).
>
> **Valeurs.** Toutes les valeurs chiffrées des décrets ont été relues à l'image, dans l'édition
> française puis dans l'édition arabe : 1997 n° 19, 2007 n° 40 et 2017 n° 26. La mention
> « Traduction française pour information » figure en tête des fascicules français de 2007
> n° 64 et de 2013 n° 1, les seuls où elle a été relevée. Le texte arabe fait foi.
>
> **Dates d'effet.** Elles suivent la règle « Dater » d'AGENTS.md. Pour un texte sans clause
> d'effet, la date retenue est le dépôt plus cinq jours (loi n° 93-64, art. 2). La date de dépôt
> est relevée sur la mention de dernière page du fascicule : « Ce numéro du Journal Officiel… a
> été déposé au siège du gouvernorat de Tunis le … ». Le calcul suit le précis, qui compte du
> 30 avril au 5 mai 2019 : la date de dépôt plus cinq jours.
>
> **Pages.** FR désigne l'édition française, AR l'édition arabe. Les deux paginations coïncident en 1997
> (n° 11 et 19) et diffèrent à partir de 2005 : le décret 2007-1185 est p. 1646 en FR et
> p. 1727 en AR. Les années 1998-2004 n'ont pas été vérifiées. Le champ
> `pages` de jort_cache donne tantôt l'une, tantôt l'autre : ici, chaque page a été relue au pied
> de page du fascicule.

## 1. Le texte du code

### 1.1 Promulgation

- **Loi n° 97-11 du 3 février 1997, portant promulgation du code de la fiscalité locale.**
  - Titre arabe : قانون عدد 11 لسنة 1997 مؤرخ في 3 فيفري 1997 يتعلق بإصدار مجلة الجباية المحلية.
  - Publication : JORT n° 11 du **7 février 1997**, pied de page relu. Dépôt au gouvernorat de
    Tunis : 11 février 1997.
  - Pagination : la loi va de la p. 173 à la p. 181. En FR, la loi de promulgation est p. 173 et
    le code p. 173-181. En AR, la pagination est identique ; les p. 173, 174, 176, 177, 178, 179
    et 181 ont été relues à l'image.
  - FR : https://www.pist.tn/jort/1997/1997F/Jo01197.pdf (200, application/pdf, 212 433 octets).
  - AR : https://www.pist.tn/jort/1997/1997A/Ja01197.pdf (200, application/pdf, 266 532 octets).
  - Travaux préparatoires : adoption par la Chambre des députés le 18 décembre 1996, puis
    de nouveau le 28 janvier 1997 (note (1) de la loi).
- **Date d'effet : 1er janvier 1997.** L'art. 3 de la loi l'énonce : « Les dispositions du
  présent code entrent en vigueur à compter du premier janvier 1997 ». L'effet est donc
  rétroactif d'environ cinq semaines.
- **Champ (art. 2 de la loi).** Le code s'applique « aux droits et redevances qui y sont prévus
  ou qui ont été institués ou seront institués par des lois spéciales au profit des collectivités
  locales ».
- **Art. 4 de la loi.** Les collectivités recensent tous les immeubles bâtis et non bâtis dans
  l'année de la promulgation.
- **Art. 5 de la loi.** Il substitue les nouvelles expressions aux anciennes :
  - « taxe d'entretien et d'assainissement » et « taxe sur la valeur locative » deviennent
    « taxe sur les immeubles bâtis » ;
  - dans les textes du Fonds national d'amélioration de l'habitat (FNAH), « valeur locative »
    devient « assiette de la taxe sur les immeubles bâtis ».

### 1.2 Structure du code : huit chapitres, 95 articles

Le code n'est **pas** organisé en « impôts, taxes, redevances ». Il compte huit chapitres, un
par prélèvement, à la nuance près du chapitre VIII, qui regroupe tout le reste. Termes arabes
relevés à l'image dans l'édition arabe ; le chapitre y est un **باب**, la section un **قسم**.

| Ch. | Intitulé FR (JORT) | Intitulé AR (JORT) | Art. |
|---|---|---|---|
| I | Taxe sur les immeubles bâtis | المعلوم على العقارات المبنية | 1-29 |
| II | Taxe sur les terrains non bâtis | المعلوم على الأراضي غير المبنية | 30-34 |
| III | Taxe sur les établissements à caractère industriel, commercial ou professionnel | المعلوم على المؤسسات ذات الصبغة الصناعية أو التجارية أو المهنية | 35-40 |
| IV | Taxe hôtelière | المعلوم على النزل | 41-45 |
| V | Taxe sur les spectacles | المعلوم على العروض | 46-51 |
| VI | Contribution des propriétaires riverains aux dépenses de premier établissement et aux grandes réparations des voies, trottoirs et conduites d'évacuation des matières liquides | مساهمة المالكين الأجوار في نفقات الأشغال الأولية والإصلاحات الكبرى المتعلقة بالطرقات والأرصفة وقنوات تصريف المواد السائلة | 52-60 |
| VII | Droits de licence sur les débits de boissons | معلوم الإجازة الموظف على محلات بيع المشروبات | 61-63 |
| VIII | Taxes et redevances diverses : formalités administratives (64-67), autorisations administratives (68), droits dans les marchés (69-81), domaine (82-90), prestations publiques payantes (91), dispositions communes (92-95) | معاليم مختلفة | 64-95 |

**Une conséquence pour le plan (ch. 6 à 8).** La classification en impôts, taxes et redevances
ne vient pas du code. L'arabe nomme presque tout **معلوم** (pluriel معاليم), là où le français
emploie selon les cas « taxe », « droit », « redevance » ou « contribution ». Le manuscrit de
2013 (§ 4.2, tableau 4-4) dit d'où vient la classification : de la **nomenclature budgétaire**,
c'est-à-dire de l'art. 7 de la loi organique du budget des collectivités locales, modifiée par
la loi organique n° 2007-65 du 18 décembre 2007. Selon le manuscrit, celle-ci « ne correspond
pas » au classement du code. Cet art. 7 n'est pas encore lu (§ 10).

Le **code des collectivités locales de 2018** pose, lui, une distinction juridique (§ 6.4) :
- d'un côté, les impôts et contributions au sens de l'art. 65 de la Constitution de 2014, qui
  relèvent de la loi ;
- de l'autre, les « معاليم ورسوم وحقوق », c'est-à-dire droits, redevances et taxes « quelle
  qu'en soit la dénomination », dont les conseils élus fixent les montants.

C'est la meilleure base pour le ch. 8.

## 2. Taxe sur les immeubles bâtis (TIB)

### 2.1 État initial (code, art. 1-29, JORT 1997 n° 11, p. 173-176)

- **Champ (art. 1).**
  - Sont imposables les immeubles bâtis situés dans les zones relevant des collectivités
    locales. Sont exclus ceux qui sont destinés aux activités soumises à la TCL (art. 35) ou à
    la taxe hôtelière (art. 41).
  - La taxe est due au 1er janvier. Les constructions nouvelles, extensions et surélévations, et
    les changements d'affectation, sont imposables à compter de leur date de réalisation.
- **Redevable (art. 2).** Le propriétaire ou l'usufruitier. À défaut, le possesseur ou l'occupant.
- **Exonérations (art. 3).** Six tirets :
  - les immeubles de l'État, des établissements publics administratifs et des collectivités
    locales, tant qu'ils ne sont pas loués ;
  - les mosquées, lieux de culte et zaouïas ;
  - les immeubles des États étrangers, sous réserve de réciprocité ;
  - les immeubles des organismes internationaux à statut diplomatique ;
  - les immeubles des associations de bienfaisance, de secourisme ou reconnues d'utilité
    publique, s'ils sont affectés à leur activité.
- **Assiette (art. 4).**
  - Formule : **2 % du prix de référence du m² couvert** de la catégorie, multiplié par la
    superficie couverte. Texte arabe : « بنسبة 2 بالمائة من الثمن المرجعي للمتر المربع المبني ».
  - Quatre catégories de superficie couverte : jusqu'à 100 m² ; de 100 à 200 m² ; de 200 à
    400 m² ; plus de 400 m².
  - Est exclue de la superficie couverte la surface des vérandas non couvertes, des garages, des
    caves non aménagées et des patios.
  - La superficie est fixée par la collectivité, sur déclaration. À défaut d'éléments,
    l'immeuble est classé dans la catégorie supérieure (§ III).
  - Les prix de référence (§ IV) sont encadrés par un **décret pris tous les trois ans**, qui
    fixe un minimum et un maximum par catégorie. Dans ces limites, la collectivité fixe le prix
    **par arrêté motivé**, selon les services rendus.
  - Pour les immeubles loués sous le régime du droit au maintien dans les lieux, l'assiette est
    plafonnée au loyer (§ V).
- **Taux (art. 5).**
  - Le taux dépend du nombre de services dont bénéficie l'immeuble : **8 %** pour un ou deux
    services ; **10 %** pour trois ou quatre ; **12 %** pour plus de quatre ; **14 %** pour plus
    de quatre plus des services supplémentaires.
  - Les six services comptés sont le nettoiement, l'éclairage public, les chaussées goudronnées,
    les trottoirs dallés, l'évacuation des eaux usées et celle des eaux pluviales.
  - Les quatre taux ont été vérifiés dans l'édition arabe, p. 174 : le taux de 14 % ouvre la
    colonne de gauche, qui se lit après celle de droite.
- **Dégrèvements (art. 6).**
  - Partiel, de 25 %, après une année d'inoccupation (§ I).
  - Total, pour les contribuables à faible revenu bénéficiant de l'aide de l'État ou des
    collectivités (§ II).
  - Ils sont accordés par arrêté du président de la collectivité, sur délibération du conseil et
    après avis de la commission de révision. Leurs modalités sont renvoyées à un décret (§ IV).
- **Recensement (art. 7-9).** Recensement **décennal**, annoncé par affichage ou insertion au
  JORT.
- **Recouvrement (art. 10-13).**
  - La taxe est recouvrée par les receveurs des finances, sur un **rôle annuel** rendu
    exécutoire par le président de la collectivité.
  - L'arabe du rôle est d'abord « زمام », puis « جدول تحصيل » à partir de 2006 (§ 2.3).
  - Les indivisaires et les héritiers sont solidaires du paiement.
  - L'autorisation de bâtir est subordonnée à une attestation de paiement (art. 13).
- **Obligations (art. 14-18).**
  - Déclaration lors du recensement, puis déclaration de tout changement dans les trente jours.
  - Solidarité de l'acquéreur, et de l'ancien propriétaire jusqu'à ce qu'il déclare la
    mutation.
  - Les rédacteurs d'actes doivent exiger une attestation de paiement.
- **Sanctions (art. 19-20).**
  - Pénalité de retard de **1,25 % par mois**.
  - Pénalité de **25 D** pour défaut de déclaration ou déclaration inexacte.
- **Contrôle et contentieux (art. 21-26).**
  - Commission de révision : président de la collectivité, deux conseillers, receveur des
    finances, secrétaire général sans voix.
  - Recours devant le **tribunal cantonal**, dans les soixante jours ; le jugement est définitif.
- **Prescription et restitution (art. 27-28).** Trois ans pour l'une comme pour l'autre.

### 2.2 Prix de référence du m² couvert (art. 4 § IV) : trois décrets

Les valeurs ci-dessous ont été relues à l'image, en FR et en AR.

| Catégorie (superficie couverte) | Décret n° 97-431 du 3 mars 1997 | Décret n° 2007-1185 du 14 mai 2007 | Décret gouv. n° 2017-397 du 28 mars 2017 |
|---|---|---|---|
| 1 : ≤ 100 m² | 100 à 150 D | 100 à 162 D | 100 à 178 D |
| 2 : 100-200 m² | 151 à 200 D | 163 à 216 D | 163 à 238 D |
| 3 : 200-400 m² | 201 à 250 D | 217 à 270 D | 217 à 297 D |
| 4 : > 400 m² | 251 à 300 D | 271 à 324 D | 271 à 356 D |
| JORT | n° 19 du 7 mars 1997, FR p. 389, AR p. 389 | n° 40 du 18 mai 2007, FR p. 1646-1647, AR p. 1726-1727 | n° 26 du 31 mars 2017, FR p. 1191-1192, AR p. 1006 |
| Date d'effet | **13 mars 1997** : pas de clause ; dépôt le 8 mars 1997, + 5 jours | **1er janvier 2008** (art. 3) ; il abroge le décret 97-431 (art. 2) | **1er janvier 2017** (art. 3), rétroactif ; il abroge le décret 2007-1185 (art. 2) |

**Observation.** En 2017, les fourchettes se chevauchent : le maximum de la catégorie 1
(178 D) dépasse le minimum de la catégorie 2 (163 D), et il en va de même entre les catégories
suivantes. Les deux éditions concordent sur ce point ; ce n'est pas une erreur de lecture.

Le code prévoit un décret « tous les trois ans ». Or **aucun décret n'est repéré entre 1997 et
2007, ni depuis 2017** (§ 10, fiche r-cfl-prix-reference-tib-apres-2017).

### 2.3 Modificatifs de la TIB et des règles communes (art. 1-29)

| Texte | Art. | Changement (avant → après) | JORT, pages | Date d'effet |
|---|---|---|---|---|
| Loi n° 98-111 du 28/12/1998, LF 1999 (`lf-1999`) | 52 | Hors code. Les bénéficiaires du dégrèvement total de la TIB (art. 6 § II) sont exonérés de la **taxe au profit du FNAH** | n° 104 du 29-31/12/1998, FR p. 2507 | **1er janvier 1997**, clause propre de l'article. L'art. 76 réserve l'art. 52 |
| Loi n° 2001-123 du 28/12/2001, LF 2002 (`loi2001-123-lf2002`) | 87 | Art. 19 § I : pénalité de retard de **1,25 % → 1 %** par mois | n° 104 du 28/12/2001, FR p. 4260 | 1er janvier 2002 (art. 97) |
| Loi n° 2002-76 du 23/07/2002 | 1-2 | Hors code, abandon de créances. Art. 1 : abandon des anciennes taxes locatives et d'assainissement de 1996 et antérieures, dont le principal ne dépasse pas 30 D par article de rôle, et de la contribution au FNAH correspondante. Art. 2 : abandon des pénalités et frais de poursuite sur la TIB de 2001 et antérieures, contre le paiement de 20 % du principal et un calendrier de deux ans et demi ; mesure ouverte jusqu'à fin octobre 2002 | n° 61 du 26/07/2002, FR p. 1715 | **1er août 2002** : dépôt le 27 juillet 2002, + 5 jours |
| Loi n° 2002-101 du 17/12/2002, LF 2003 (`lf-2003`) | 77 | Art. 6 § I abrogé : **suppression du dégrèvement partiel de 25 %** pour inoccupation | n° 102 du 17/12/2002, FR p. 2887 | 1er janvier 2003 (art. 87) |
| idem | 78 | Art. 6 § III : renvoi au seul dégrèvement du § II | idem | idem |
| Loi n° 2004-90 du 31/12/2004, LF 2005 | 13-14 | Hors code. Crée la **contribution au profit du FNAH**, à **4 % de l'assiette de la TIB** (immeubles d'habitation) ; règles de recouvrement et de contentieux de la TIB. Exonérés : immeubles de l'art. 3 du code, bénéficiaires du dégrèvement total. Les art. 11-16 recréent le FNAH comme fonds spécial du Trésor et abrogent le décret beylical du 23 août 1956 | n° 105 du 31/12/2004, FR p. 3433 | 1er janvier 2005 (art. 89) |
| Loi n° 2005-106 du 19/12/2005, LF 2006 | 53 | Art. 13 récrit : attestation de paiement exigée pour le permis de bâtir ou de clôture, le changement d'affectation d'un logement en local commercial ou professionnel, et l'arrêté de lotissement | n° 101 du 20/12/2005, FR p. 3603 ; AR p. 3923 | 1er janvier 2006 (art. 62) |
| idem | 56 | Arabe seulement, art. 10, 21, 56 et 95 : « زمام » (ou « أزمة ») → « **جدول تحصيل** » (rôle). Le FR imprime des guillemets vides | FR p. 3604 ; AR p. 3923 | idem |
| idem | 57 | Art. 10, 56 et 95 : recouvrement « au vu d'un extrait du rôle individuel visé par le receveur des finances » | FR p. 3604 ; AR p. 3923-3924 | idem |
| Loi n° 2006-85 du 25/12/2006, LF 2007 | 54 | Art. 19 § I : **1 % → 0,75 %** par mois, à compter du 1er janvier de l'année suivant celle de l'exigibilité. L'al. 2 (pas de pénalité en cas de paiement dans l'année) est abrogé | n° 103 du 26/12/2006, FR p. 4389 | 1er janvier 2007 (art. 88) |
| Loi n° 2007-53 du 08/08/2007 | 1 | Ajoute l'**art. 17 bis**. § I : le propriétaire, le locataire et l'occupant d'un immeuble bâti, même inachevé, déclarent toute location ou occupation à la collectivité **dans les 8 jours**, sur modèle (adresse, identité des parties, affectation, date et durée) ; les occupations par ascendants ou descendants du propriétaire sont exclues. § II : même obligation pour les gestionnaires pour compte de tiers. § III : constatation par procès-verbal des agents habilités | n° 64 du 10/08/2007, FR p. 2732 | **16 août 2007** : dépôt le 11 août 2007, + 5 jours |
| idem | 2 | Art. 19 § III-V : amende égale à **trois fois le prix de référence maximum du m² de la catégorie supérieure** ; solidarité du locataire ou de l'occupant ; extension aux gestionnaires pour compte de tiers | idem | idem |
| idem | 3 | Hors code, transitoire. Déclaration des locations en cours dans les trois mois, avec la même amende | FR p. 2732-2733 | idem |
| Loi n° 2008-77 du 22/12/2008, LF 2009 | 33 | Art. 13 complété : attestation exigée aussi pour l'inscription au rôle, l'habitation principale, le procès-verbal de récolement et le permis d'occuper | n° 104 du 26/12/2008, FR p. 4279 | 1er janvier 2009 (art. 39) |
| Loi n° 2012-1 du 16/05/2012, LFC 2012 | 17 | Hors code, abandon. TIB et contribution au FNAH de 2007 et antérieures dont le reliquat est ≤ 50 D par an ; 50 % des montants de 2010 et antérieures dont le reliquat est ≤ 100 D ; pénalités et frais au-delà. Conditions : payer 2012, et souscrire un calendrier de trois ans au plus, première tranche avant le 1er septembre 2012 | n° 39 du 18/05/2012, FR p. 924 | **24 mai 2012** : pas de clause générale ; dépôt le 19 mai 2012, + 5 jours |
| Loi n° 2012-27 du 29/12/2012, LF 2013 (`lf-2013`) | 55 | Art. 13 : ajout des « services ». Attestation exigée pour la légalisation de signature des actes de mutation, d'hypothèque, de location ou de jouissance d'immeubles, et pour le permis de démolir | n° 1 du 1er/01/2013, FR p. 16 | 1er janvier 2013 (art. 79) |
| Loi n° 2013-54 du 30/12/2013, LF 2014 (`lf-2014`) | 30 § 1 | Art. 3 : nouveau tiret, exonération des immeubles de l'État, des collectivités et des établissements publics administratifs transférés dans une **émission de sukuk** | n° 105 du 31/12/2013, FR p. 3674 ; AR p. 4350-4351 (art. 25 à 30) | 1er janvier 2014 (art. 95), alors que le dépôt n'a eu lieu que le 3 janvier 2014 |
| idem | 55 | Hors code. **Impôt foncier** égal à 1,5 fois la TIB ou la TNB. Il est déjà au glossaire (`impot-foncier-2014`) et relève du volume « La fiscalité » ; supprimé par l'art. 38 de la LFC 2014 (`lfc-2014`), d'après l'entrée bibliographique existante, non relue ici | FR p. 3683 ; AR p. 4358 | — |
| Loi n° 2018-56 du 27/12/2018, LF 2019 (`loi2018-56-lf2019`) | 72 | Hors code, abandon **total** de la TIB et de la contribution au FNAH de 2016 et antérieures, avec pénalités et frais. Conditions : payer 2019, régler 2017-2018 avant fin décembre 2019 | n° 104 du 28/12/2018, FR absent (404), AR p. 5464 | 1er janvier 2019 (art. 90) |
| Décret-loi n° 2021-21 du 28/12/2021, LF 2022 (`dl2021-21-lf2022`) | 68 § 3 | Art. 19 § I complété : les pénalités de retard **ne peuvent excéder le principal** | n° 119 du 28/12/2021, FR p. 3106, AR p. 3282 | 1er janvier 2022 (art. 73) |
| Décret-loi n° 2022-79 du 22/12/2022, LF 2023 (`lf-2023`) | 59 § 7 | Art. 19 § I : **0,75 % → 1,25 %** par mois. Le § 10 écarte **tout l'article**, donc aussi le § 7, pour trois catégories de sommes : celles des déclarations déposées spontanément avant le 1er avril 2023, celles des résultats de vérification notifiés avant cette date, celles des taxations d'office notifiées avant cette date. Reste à trancher si cette réserve peut concerner la TIB, recouvrée par voie de rôle | n° 141 du 23/12/2022, FR absent (404), AR p. 4075-4076 | 1er janvier 2023 (art. 76), sous la réserve du § 10 |
| Loi n° 2023-13 du 11/12/2023, LF 2024 (`lf-2024`) | 59 | Hors code, abandon pour les personnes physiques de la TIB, de la contribution au FNAH et de la **TNB** de 2021 et antérieures. Conditions : payer 2024, payer 2022-2023 ou souscrire un calendrier de deux ans. Pour les personnes morales, abandon des seules pénalités de 2023 et antérieures | n° 144 du 12/12/2023, FR absent (404), AR p. 6453 | 1er janvier 2024 (art. 70) |
| Loi n° 2024-48 du 09/12/2024, LF 2025 (`lf-2025`) | 76 | Hors code. Nouvel abandon de la TIB, de la contribution au FNAH et de la TNB de 2021 et antérieures, et des pénalités de 2024 et antérieures. Conditions : payer 2025, régler 2022-2024 ou souscrire un calendrier, première tranche avant le 1er janvier 2026 | n° 149 du 10/12/2024, FR absent (404), AR p. 6452 | 1er janvier 2025 (art. 84) |

Décret d'application de l'art. 6 : **décret n° 98-1254 du 8 juin 1998**, relatif à la fixation des
conditions et modalités d'application du dégrèvement de la taxe sur les immeubles bâtis.
- JORT n° 48 du 16 juin 1998, FR p. 1307-1308 ; dépôt le 19 juin 1998, donc exécutoire le
  **24 juin 1998**.
- Dégrèvement partiel (art. 2-8) :
  - immeuble inoccupé pendant une année entière, immeubles loués exclus ;
  - déclarations trimestrielles et attestation de paiement ;
  - procès-verbal de deux agents, avis de la commission de révision, puis dégrèvement de 25 %
    imputé sur la taxe de l'année suivante.
- Dégrèvement total (art. 9-12) : il exige une aide **permanente** de l'État ou d'une
  collectivité, et la demande suspend le recouvrement.
- Le chapitre du dégrèvement partiel est privé d'objet depuis la LF 2003 (art. 77).
- AR : pages non relevées.

## 3. Taxe sur les terrains non bâtis (TNB)

### 3.1 État initial (code, art. 30-34, JORT 1997 n° 11, p. 176)

- **Champ et redevable (art. 30-31).**
  - Sont imposables les terrains non bâtis des zones relevant des collectivités locales. La taxe
    est due au 1er janvier, ou à la date d'entrée dans le champ.
  - Redevable : le propriétaire ou l'usufruitier, à défaut le possesseur ou l'occupant.
- **Exonérations (art. 32), sept tirets :**
  - les jardins enclos attenant aux immeubles ;
  - les terrains agricoles ;
  - les terrains enclos exploités dans une activité industrielle, commerciale ou professionnelle ;
  - les terrains de l'État, des établissements publics administratifs et des collectivités ;
  - les terrains en zone d'interdiction de bâtir ;
  - les lotissements industriels, d'habitat, touristiques ou artisanaux, tant qu'ils ne sont pas
    cédés par le lotisseur ;
  - les réserves foncières et les périmètres d'intervention foncière.
- **Assiette et taux (art. 33).**
  - Taux de **0,3 % de la valeur vénale réelle**. En arabe, « 0,3 بالمائة من القيمة التجارية
    الحقيقية للأراضي ».
  - À défaut de valeur vénale : **tarif au m² progressif selon la densité urbaine** des zones du
    plan d'aménagement urbain, « fixé pour chaque zone par décret tous les trois ans ».
- **Procédure (art. 34).** Les art. 7 à 29 (TIB) s'appliquent.

### 3.2 Tarif au m² (art. 33, al. 2) : trois décrets

Les valeurs ont été relues à l'image, en FR et en AR.

| Zone (plan d'aménagement urbain) | Décret n° 97-432 du 3 mars 1997 | Décret n° 2007-1186 du 14 mai 2007 | Décret gouv. n° 2017-396 du 28 mars 2017 |
|---|---|---|---|
| Haute densité urbaine (ذات كثافة عمرانية مرتفعة) | 0,300 D | 0,318 D | 0,385 D |
| Moyenne densité (متوسطة) | 0,090 D | 0,095 D | 0,115 D |
| Basse densité (منخفضة) | 0,030 D | 0,032 D | 0,040 D |
| JORT | n° 19, FR p. 389, AR p. 389 | n° 40, FR p. 1647, AR p. 1727-1728 | n° 26, FR p. 1190-1191, AR p. 1005-1006 |
| Date d'effet | **13 mars 1997** (dépôt le 8 mars, + 5 jours) | **1er janvier 2008** (art. 3) ; abroge 97-432 | **1er janvier 2017** (art. 3) ; abroge 2007-1186 |

### 3.3 Modificatifs propres à la TNB

| Texte | Art. | Changement | JORT, pages | Date d'effet |
|---|---|---|---|---|
| LF 2002 (`loi2001-123-lf2002`) | 43 | Art. 32 : 8e tiret, terrains non bâtis aménagés acquis par les **promoteurs immobiliers**, pendant deux ans à compter de l'acquisition | n° 104/2001, FR p. 4256 | 1er janvier 2002 (art. 97) |
| LF 2005 | 82 | Art. 32, 1er tiret remplacé par trois tirets : jardins enclos attenant aux immeubles **individuels, dans la limite de 1 000 m²** ; jardins attenant aux immeubles collectifs ; terrains enclos et **boisés** attenant aux immeubles | n° 105/2004, FR p. 3445 | 1er janvier 2005 (art. 89) |
| LF 2014 (`lf-2014`) | 30 § 2 | Art. 32 : nouveau tiret après le 10e, exonération des terrains publics transférés dans une émission de **sukuk** | n° 105/2013, FR p. 3674 | 1er janvier 2014 (art. 95) |
| LF 2009, LF 2024, LF 2025 | 33, 59, 76 | L'art. 33 de la LF 2009 est titré « Amélioration du recouvrement de la TIB et de la TNB ». La TNB entre aussi dans les abandons de 2024 et 2025 (§ 2.3) | — | — |

Le décompte des tirets de l'art. 32 se tient : 7 en 1997, 8 après 2002, 10 après 2005, d'où le
« après le 10e tiret » de 2014.

## 4. Taxe sur les établissements à caractère industriel, commercial ou professionnel (TCL)

### 4.1 Antécédent

Loi n° 75-39 du 14 mai 1975, portant institution d'une taxe sur les établissements à caractère
industriel, professionnel ou commercial au profit des collectivités locales : JORT n° 34 du
20 mai 1975, p. 1069 d'après jort_cache. Elle est abrogée par l'art. 3 de la loi 97-11. Son
texte n'a **pas été lu** ici. jort_cache signale aussi :
- le décret n° 76-2 du 5 janvier 1976 (plafond) ;
- la LF 1976 (minimum de perception) ;
- la LF 1980 ;
- la LF 1992 (« taxe … applicable aux … »).

Tous ces textes sont des pistes pour le chapitre historique.

### 4.2 État initial (code, art. 35-40, JORT 1997 n° 11, p. 176-177)

- **Redevables (art. 35).** La taxe est due même en cas d'exonération d'IR ou d'IS :
  - les personnes physiques soumises à l'IR au titre des BIC et des BNC ;
  - les personnes morales soumises à l'IS ;
  - les sociétés de personnes et les associations en participation.
- **Exonérations (art. 36).**
  - Les personnes des art. 3 § 6 et 45 § 2 du code de l'IRPP et de l'IS.
  - Les établissements touristiques soumis à la taxe hôtelière.
  - Les régimes spéciaux légaux ou conventionnels sont maintenus.
- **Assiette (art. 37).**
  - **Chiffre d'affaires brut local**.
  - Pour trois cas, la taxe est assise sur l'IR ou l'IS : les forfaitaires de l'art. 44 § IV du
    code de l'IRPP et de l'IS ; les établissements dont la marge brute réglementée est ≤ 4 % ;
    les établissements déficitaires justifiant d'une comptabilité régulière.
- **Taux (art. 38).**
  - **0,2 %** du chiffre d'affaires (§ I). Pour les cas de l'art. 37 al. 2, le taux est de
    **25 %** de l'IR ou de l'IS.
  - **Minimum (§ II).** Il est égal à la TIB des locaux exploités, calculée sur la base de **5 %
    du prix de référence** du m², multipliée par la superficie couverte. Il s'applique aussi aux
    établissements sans chiffre d'affaires.
  - Le minimum distingue quatre catégories d'immeubles :
    - usage administratif ou activité commerciale ou non commerciale ;
    - construction légère industrielle ;
    - béton industriel ;
    - industriel de plus de 5 000 m².
  - La « taxe par m² de référence » du minimum est fixée **par décret tous les trois ans** (§ II).
  - **Maximum** fixé par décret (§ III). Si le minimum dépasse le maximum, c'est le minimum qui
    est recouvré.
  - Établissements agricoles et de pêche soumis à l'IS : taxe égale à la TIB de chaque local
    (§ IV).
  - Activité sur plusieurs collectivités : répartition selon la **superficie couverte** de chaque
    centre ou agence (§ V).
- **Déclaration et paiement (art. 39).**
  - Déclaration à la recette des finances. Elle mentionne le siège, le matricule, les filiales
    et leurs superficies, le chiffre d'affaires brut local et la catégorie d'immeuble.
  - Délais : les quinze premiers jours du mois suivant pour les personnes physiques, les
    vingt-huit premiers jours pour les personnes morales (§ II).
  - Les redevables de l'art. 37 al. 2 paient la taxe avec l'IR ou l'IS (§ IV).
- **Contrôle et contentieux (art. 40).**
  - Règles du code de l'IRPP et de l'IS (§ I).
  - Pour le minimum, les règles des art. 10 à 29 (§ II).
  - À défaut de déclaration des filiales, la collectivité impose la filiale à la TIB, sans
    restitution (§ III).

### 4.3 Minimum : taxe par m² de référence (art. 38 § II)

Montants en dinars par m², selon le taux de la TIB applicable au local. Valeurs relues à
l'image, FR et AR.

| Catégorie | 97-433 : 8 % / 10 % / 12 % / 14 % | 2007-1187 : 8 % / 10 % / 12 % / 14 % | 2017-395 : 8 % / 10 % / 12 % / 14 % |
|---|---|---|---|
| 1 : administratif, commercial ou non commercial | 0,760 / 0,950 / 1,140 / 1,330 | 0,815 / 1,020 / 1,220 / 1,425 | 0,900 / 1,125 / 1,345 / 1,570 |
| 2 : structure légère industrielle | 0,520 / 0,650 / 0,780 / 0,910 | 0,560 / 0,700 / 0,835 / 0,975 | 0,620 / 0,770 / 0,920 / 1,075 |
| 3 : béton industriel | 0,640 / 0,800 / 0,960 / 1,120 | 0,685 / 0,860 / 1,030 / 1,200 | 0,755 / 0,950 / 1,135 / 1,320 |
| 4 : industriel > 5 000 m² | 0,840 / 1,050 / 1,260 / 1,470 | 0,900 / 1,125 / 1,350 / 1,575 | 0,990 / 1,240 / 1,485 / 1,735 |
| JORT | n° 19/1997, FR p. 389-390, AR p. 389-390 | n° 40/2007, FR p. 1648, AR p. 1728 | n° 26/2017, FR p. 1189-1190, AR p. 1004-1005 |
| Date d'effet | **13 mars 1997** | **1er janvier 2008** (art. 3) ; abroge 97-433 | **1er janvier 2017** (art. 3) ; abroge 2007-1187 |

Contrôle arithmétique de 1997 : les valeurs à 8 % valent 5 % × 8 % × un prix de référence
implicite de 190 D (catégorie 1), 130 D (cat. 2), 160 D (cat. 3) et 210 D (cat. 4). Les colonnes
à 10, 12 et 14 % en sont proportionnelles, ce qui conforte la lecture. Ce calcul est fait pour
vérifier la transcription ; il ne doit pas entrer dans le précis sans être présenté comme tel.

### 4.4 Maximum (art. 38 § III), jusqu'à sa suppression

| Texte | Maximum annuel | JORT | Date d'effet |
|---|---|---|---|
| Décret n° 97-435 du 3 mars 1997 | 50 000 D | n° 19 du 7/03/1997, FR p. 390, AR p. 390 | 13 mars 1997 (dépôt le 8 mars, + 5 jours) |
| Décret n° 2003-1345 du 16 juin 2003 ; abroge 97-435 | 60 000 D | n° 49 du 20/06/2003, FR p. 1992 | **26 juin 2003** (pas de clause ; dépôt le 21 juin 2003, + 5 jours) |
| Décret n° 2006-3360 du 25 décembre 2006 ; abroge 2003-1345 | 100 000 D | n° 2 du 5/01/2007, FR p. 29 | **1er janvier 2007** (art. 2) |
| LFC 2012 (loi n° 2012-1), art. 50 | **maximum supprimé** : art. 38 § III abrogé | n° 39 du 18/05/2012, FR p. 930 | **1er janvier 2012**, clause propre de l'article |

### 4.5 Autres modificatifs de la TCL

| Texte | Art. | Changement | JORT, pages | Date d'effet |
|---|---|---|---|---|
| LF 2002 | 65 | Art. 35, 3e tiret : ajout des **groupements d'intérêt économique** | n° 104/2001, FR p. 4258 | 1er janvier 2002 |
| LF 2003 | 80 | Art. 40 § II : pour le minimum, renvoi aux art. 10 à 26, 28 et 29 ; l'art. 27, sur la prescription, n'est plus visé | n° 102/2002, FR p. 2887 | 1er janvier 2003 |
| LF 2005 | 80 | Art. 36, 1er tiret remplacé : exonération des personnes **non établies et non domiciliées** en Tunisie | n° 105/2004, FR p. 3445 | 1er janvier 2005 |
| LF 2005 | 81 | Art. 38 § V complété : à défaut de répartition par superficie, **critères fixés par décret** | idem | idem |
| Décret n° 2006-49 du 9 janvier 2006 | — | Critères de répartition : carrière, 50 % à la collectivité qui l'abrite ; immeubles non bâtis ou non couverts, 30 % à parts égales entre leurs collectivités ; à défaut d'immeubles, répartition au chiffre d'affaires | n° 5 du 17/01/2006, FR p. 181-182 | **23 janvier 2006** (dépôt le 18 janvier, + 5 jours) |
| LF 2011 (loi n° 2010-58) | 32, 40 | Hors code. Nouveau régime forfaitaire de l'IR : l'art. 44 quater du code de l'IRPP et de l'IS dispose que l'impôt forfaitaire « comprend la taxe sur les établissements ». L'art. 40 est transitoire pour 2010. Renvoi au volume « La fiscalité » | n° 102 du 21/12/2010, FR p. 3470-3471 et 3474 | 1er janvier 2011 (art. 50, sous réserve des art. 18, 40 et 41) |
| LF 2013 (`lf-2013`) | 14 | Hors code. Le Fonds de coopération entre les collectivités locales est financé par le produit de la TCL **au-delà de 100 000 D** par établissement et par an. Renvoi au ch. 9 | n° 1/2013, FR p. 5 | 1er janvier 2013 |
| idem | 23 | Art. 37 al. 2 récrit : assiette IR ou IS pour les forfaitaires de l'**art. 44 bis** et les établissements en perte. Le cas de la marge ≤ 4 % disparaît | FR p. 8 | idem |
| idem | 24 | Art. 38 § I : **taux réduit de 0,1 %** pour les établissements qui commercialisent exclusivement des produits à prix homologués dont la marge brute est ≤ 6 %, ou au moins 80 % de tels produits. Option pour 25 % de l'IR ou de l'IS, exercée en janvier | idem | idem |
| LF 2014 (`lf-2014`) | 49 | Art. 37 et 39 § I : le mot « **local** » est supprimé. Art. 38 § I : 0,1 % appliqué au chiffre d'affaires d'**exportation**, à celui des établissements de santé travaillant exclusivement pour des non-résidents, et à celui des prestataires de services financiers aux non-résidents | n° 105/2013, FR p. 3680, AR p. 4356 | 1er janvier 2014 |
| idem | 50 | Hors code. La TCL est retirée des exonérations du code d'incitation aux investissements, de la loi 2001-94 (établissements de santé) et de la loi 92-81 (parcs d'activités) | FR p. 3680-3681 | idem |
| LF 2016 (`lf-2016`) | 37 | Art. 39 § I : nouveau tiret, déclaration des superficies et adresses des lots non couverts ou non bâtis. Art. 40 § III : **amende de 1 000 D** par lot non déclaré | n° 104 du 29/12/2015, FR absent (404), AR p. 3608 | 1er janvier 2016 (art. 92) |
| LF 2019 (`loi2018-56-lf2019`) | 42 | Hors code. Contribution unique des petits exploitants à revenu irrégulier qui se déclarent spontanément à partir de 2019 : 200 D ou 100 D d'IR selon la zone, plus les cotisations. Elle « comprend » la TCL | AR p. 5453 | 1er janvier 2019 |
| LF 2021 (`lf-2021`) | 13 | Hors code. Le Fonds d'appui à la décentralisation est alimenté notamment par la TCL au-delà de 100 000 D par établissement. Renvoi au ch. 9 | n° 128 du 25/12/2020, FR p. 3125, AR p. 3376 | 1er janvier 2021 (art. 42) |
| idem | 37 | Art. 38 § V remplacé : répartition à la superficie bâtie ou couverte « nonobstant l'usage destiné ». À défaut, les critères du décret 2006-49 passent dans la loi (carrière 50 %, non bâti 30 %, chiffre d'affaires) | FR p. 3136, AR p. 3386-3387 | idem |
| LF 2023 (`lf-2023`) | 52 § 3 | Hors code. Auto-entrepreneur (décret-loi 2020-33, art. 7 nouveau) : la contribution unique comprend la TCL « à raison de 20 % » de l'IR, sans minimum | n° 141/2022, AR p. 4071-4072 | 1er janvier 2023 |
| idem | 57 § 7 | Art. 39 § II : après « pour les personnes physiques », ajoute un délai trimestriel, les quinze premiers jours du mois suivant chaque trimestre civil, pour les personnes visées à l'**art. 62 § III ter** du code de l'IRPP et de l'IS | AR p. 4074 | idem |
| LF 2024 (`lf-2024`) | 67 | Art. 40 § III : l'amende suit les règles de la TNB | n° 144/2023, AR p. 6456 | 1er janvier 2024 (art. 70) |
| idem | 69 § 4 | Art. 39 § II : délai ramené aux **vingt premiers jours** pour les personnes morales qui télédéclarent | AR p. 6458 | idem |

**Amnisties.** Plusieurs lois de finances étendent leurs mesures d'amnistie à la TCL, à la taxe
hôtelière et au droit de licence :
- LFC 2012, art. 15 (FR p. 924) ;
- LF 2019, art. 73 ;
- LF 2024, art. 58 (AR p. 6452-6453) ;
- LF 2025, art. 74 (AR p. 6450) ;
- LF 2026, article non numéroté ici (AR p. 4249, JORT 2025 n° 148) ;
- en 2006, la loi n° 2006-25 du 15 mai 2006 portant amnistie fiscale (art. 4-5) et le
  décret-loi n° 2006-1 du 31 juillet 2006 (art. 3), repérés au plein texte dans les JORT 2006
  n° 39 et n° 62, sans relevé de page.

Ce ne sont pas des modifications du code. On les signale sans les détailler.

## 5. Taxe hôtelière

- **Antécédent.** Loi n° 75-34 du 14 mai 1975, portant institution d'une taxe hôtelière au profit
  des communes et des conseils de gouvernorat : JORT n° 34 du 20 mai 1975, p. 1065 d'après
  jort_cache. Abrogée par l'art. 3 de la loi 97-11, elle n'a pas été lue ici.
- **État initial (art. 41-45, p. 177-178).**
  - Redevables : les exploitants des établissements touristiques au sens de la législation en
    vigueur.
  - Assiette : le **chiffre d'affaires brut global**.
  - Taux : **2 %**.
  - Recouvrement : celui de la TCL (art. 38 § V, art. 39 § I-III, art. 40).
  - Les établissements soumis à la taxe hôtelière sont exonérés de TCL (art. 36) et de TIB
    (art. 1).
- **Modificatifs.** Aucune modification des art. 41-45 n'a été repérée de 1997 à 2026. Contrôles
  faits :
  - plein texte FR des lois de finances 1997-2021 ;
  - plein texte AR des lois de finances 2016, 2019, 2020, 2023-2026 ;
  - plein texte AR de « مجلة الجباية المحلية » sur tout le corpus 1997-2026.

  Deux textes hors code touchent la taxe hôtelière :
  - **LF 1997 (loi n° 96-113, `lf-1997`), art. 53.** Il fait passer à « cinquante pour cent du
    produit de la taxe hôtelière » la part affectée au fonds spécial du Trésor pour la
    protection des zones touristiques, en modifiant l'art. 39 de la loi n° 92-122 (LF 1993). JORT
    n° 105 du 31/12/1996, FR p. 2583. Effet au 1er janvier 1997 (art. 54).
  - Les décrets fixant les **zones municipales touristiques**, notamment le décret 94-822 et ses
    compléments de 1996 à 2019, n'ont pas été lus (§ 10).

## 6. Autres taxes et redevances du code

### 6.1 Taxe sur les spectacles (art. 46-51)

- Redevables : les organisateurs de spectacles **occasionnels**.
- Assiette : **50 % des recettes prévisionnelles**.
- Taux : **6 %**.
- Paiement avant l'autorisation ; pénalité égale au double du droit.
- Exonérations : galas de bienfaisance subventionnés, troupes amateurs agréées, foires gratuites,
  spectacles dont le prix d'entrée n'excède pas un montant fixé par décret.
- **Décret n° 97-530 du 22 mars 1997 : prix maximum de 5 D.** JORT n° 26 du 1er/04/1997, FR
  p. 531 ; dépôt le 2 avril 1997, exécutoire le **7 avril 1997**.
- Le décret n° 2003-457 du 24 février 2003, « taxe due sur le prix des billets d'entrée aux
  spectacles artistiques », n'appartient **pas** à la fiscalité locale. Il est pris en
  application de l'art. 39 de la LF 2003 et finance la couverture sociale des artistes (JORT
  n° 18/2003, p. 476).

### 6.2 Contribution des propriétaires riverains (art. 52-60)

- Contribution aux travaux de premier établissement et de grosses réparations des voies,
  trottoirs et égouts, après un décret déclarant les travaux d'utilité publique.
- La collectivité peut réduire la contribution de 50 % pour les cas sociaux.
- Avance de 10 à 30 %, puis cinq annuités ; pénalité de 10 %.
- **Loi n° 2002-76, art. 3.** Elle récrit l'art. 53 § 3 : dégrèvement **total** pour les
  contribuables à faible revenu, selon les règles de la TIB. JORT n° 61, p. 1715 ; exécutoire le
  1er août 2002.

### 6.3 Droit de licence sur les débits de boissons (art. 61-63)

- Assis sur la catégorie de l'établissement.
- Prélèvement de 10 % au profit du budget de l'État.
- Déclaration en janvier.
- **Décret n° 97-434 du 3 mars 1997** : tarif annuel de 25, 150 et 300 D selon la catégorie
  1, 2 ou 3. JORT n° 19, FR p. 390, AR p. 390 ; exécutoire le 13 mars 1997.

### 6.4 Chapitre VIII (art. 64-95) et le code des collectivités locales de 2018

- **Contenu.**
  - Redevances de légalisation de signature, de certification conforme et de délivrance d'actes.
  - Taxe sur les **autorisations administratives**, permis de bâtir compris (art. 68).
  - Droits de marché, de stationnement, de pesage et de criée.
  - Taxe d'abattage, occupation de la voie publique et du domaine public maritime, concessions
    funéraires.
  - **Contribution à la réalisation de parkings collectifs** (art. 89-90), sur des listes de
    communes fixées par arrêtés du 4 mars 1997 et du 30 mai 2003.
  - Redevances pour **prestations publiques** (art. 91), dont la contribution aux travaux
    d'**électrification et d'éclairage public**, perçue sur les factures d'électricité et de gaz.
- **Tarifs.** L'art. 92 renvoie leur fixation à un décret, sauf pour la contribution de parking.
  L'art. 93 laisse à la collectivité les déchets non ménagers.
- **Modificatifs repérés.**
  - **LF 2003, art. 79.** Il récrit l'art. 90 (parkings) : barème selon le taux de places
    manquantes (≤ 25 %, 25-75 %, plus de 75 %) et selon la population (≤ 50 000 habitants,
    50 000-100 000, au-delà). Le montant va de 250 à 2 250 D par place et double en cas de
    réaffectation. JORT n° 102/2002, FR p. 2887.
  - **LF 2002, art. 88.** Art. 74 : pénalité de **1,25 % → 0,75 %**. JORT n° 104/2001, FR
    p. 4260.
  - **LF 2013, art. 74.** Exonère les **groupements hydrauliques** de la contribution de l'art.
    91. JORT n° 1/2013, FR p. 28.
- **Décrets de tarifs, cités sans transcription des grilles.**
  - Décret n° 98-1428 du 13 juillet 1998, relatif à la fixation du tarif des taxes que les
    collectivités locales sont autorisées à percevoir : JORT n° 59, p. 1621-1626.
  - Modifié par les décrets :
    - n° 2000-232 (n° 12/2000, p. 389) ;
    - n° 2000-1692 (n° 59/2000, p. 1775, rectificatif au n° 72, p. 2100) ;
    - n° 2003-1346 (n° 49/2003, p. 1992-1993) ;
    - n° 2004-80 (n° 7/2004, p. 172-173) ;
    - n° 2012-1958 (n° 76/2012, p. 2222) ;
    - n° 2013-3236 (n° 67/2013, p. 2448-2449).
  - **Abrogé** par l'art. 2 du **décret gouvernemental n° 2016-805 du 13 juin 2016**, relatif
    à la fixation du tarif des droits que les collectivités locales sont autorisées à percevoir
    (« يتعلق بضبط تعريفة المعاليم المرخص للجماعات المحلية في استخلاصها »). JORT n° 53 (29 juin 2016
    selon jort_cache, pied de page non relu), AR p. 2379, relue au plein texte. L'art. 2 dispose : « تلغى الأحكام السابقة
    المخالفة لأحكام هذا الأمر الحكومي وخاصة الأمر عدد 1428 لسنة 1998 ». L'édition FR
    existe dans le corpus mais n'a pas été lue ; la date d'effet n'est pas établie.
  - **Complément du rédacteur, 4 octobre 2026.** Édition FR lue dans le corpus local
    (`Jo0532016.pdf`, « Traduction française pour information ») : intitulé « Décret
    gouvernemental n° 2016-805 du 13 juin 2016, relatif à la fixation du tarif des taxes que les
    collectivités locales sont autorisées à percevoir », JORT n° 53 du 29 juin 2016, p. 2067 ;
    annexe p. 2067-2070. Art. 1er : tarif des taxes des sections 1 à 5 du chapitre VIII fixé par
    le tableau annexé. Art. 2 : l'édition FR imprime « décret n° 98-1998 du 13 juillet 1998 »
    (l'AR porte 1428). Pas de clause d'effet ; dépôt au gouvernorat de Tunis le 30 juin 2016
    (mention de dernière page), donc exécutoire le **5 juillet 2016**. L'annexe fixe tantôt un
    montant, tantôt un tarif « fixé par arrêté de la collectivité locale concernée » entre deux
    bornes ou au-dessus d'un minimum (voie publique, marchés, publicité, domaine public maritime,
    fourrière, déchets). Grille non transcrite.
  - Les pages des décrets de 1998 à 2013 viennent de jort_cache. Leurs grilles n'ont pas été
    lues (§ 10).
- **Code des collectivités locales**, loi organique n° 2018-29 du 9 mai 2018
  (`loi-org-2018-29-ccl`). JORT n° 39 du 15/05/2018, **AR seulement** (FR : 404).
  - **Art. 137 (AR p. 1726).** Il énumère les ressources du budget local et distingue deux
    catégories :
    - « الأداءات والمعاليم المحلية التي يقرها القانون » ;
    - « مختلف المعاليم والرسوم والحقوق … التي لا تكتسي صبغة الأداء والمساهمة على معنى الفصل 65
      من الدستور والتي تقر مبالغها أو نسبها الجماعات المحلية بواسطة مجالسها المنتخبة ».
  - **Art. 139 (AR p. 1726).** Les conseils élus fixent le montant ou le tarif de ces droits et
    redevances, et les cas d'**exonération ou de réduction**.
  - **Art. 140.** Il énumère les droits des **communes**. On y trouve la taxe sur les spectacles,
    la contribution des riverains, le droit de licence, les redevances de légalisation, les
    autorisations administratives, les droits de marché, l'abattage, l'occupation du domaine,
    la publicité, les parkings, etc. La TIB, la TNB, la TCL et la taxe hôtelière n'y figurent pas.
  - **Art. 141 (AR p. 1727).** Les droits des **régions**.
  - **Art. 391 (AR p. 1760).** Les **art. 46 à 95 du code** cessent de s'appliquer « تباعا »,
    collectivité par collectivité, à mesure qu'entrent en vigueur ses propres délibérations
    tarifaires. Pendant cinq ans au plus après l'entrée en vigueur des dispositions budgétaires,
    des décrets gouvernementaux pris sur avis de la Haute instance des finances locales fixent
    toutefois le droit de licence, la légalisation de signature, la certification conforme et la
    délivrance d'actes.
  - **Art. 392.** Il met fin aux art. 13 à 15 de la LF 2013 (Fonds de coopération) dès la
    création par la loi du fonds de 2021. Renvoi au ch. 9.
  - Les dates d'effet de ces articles ne sont pas établies, faute d'avoir lu les dispositions
    finales du code (§ 10).

**Pour le ch. 8.** Après 2018, l'autonomie se partage en deux.
- **Impôts fixés par la loi** (TIB, TNB, TCL, taxe hôtelière). Les collectivités n'y modulent
  que ce que le code leur laisse :
  - le prix de référence de la TIB, dans la fourchette du décret, par arrêté motivé (art. 4
    § IV) ;
  - la réduction de 50 % de la contribution des riverains (art. 53) ;
  - le taux de l'avance de cette contribution, entre 10 et 30 % (art. 59) ;
  - les tarifs des déchets non ménagers (art. 93) ;
  - les dégrèvements, sur délibération (art. 6).
- **Droits et redevances fixés par délibération**, une fois la transition de l'art. 391
  achevée.

## 7. Antécédents abrogés par le code (art. 3 de la loi 97-11)

L'art. 3 abroge « tous les textes contraires et notamment » les textes suivants. La liste est
celle du JORT 1997 n° 11, p. 173, vérifiée en FR et en AR. **Aucun de ces textes n'a été lu
ici.**

| Texte abrogé | Objet | Repris dans le code par |
|---|---|---|
| Décret du 31 janvier 1887 | contribution des propriétaires riverains | ch. VI |
| Décret du 16 septembre 1902 | taxe sur la valeur locative des immeubles | TIB (art. 5 de la loi) |
| Décret du 15 janvier 1914, art. 1, 2, 6 et 9 | taxe d'abattage | art. 82-83 |
| Décret du 15 janvier 1914, art. 2 et 6 | occupation temporaire de la voie publique | art. 85 |
| Décret du 15 janvier 1914 | taxe sur les véhicules | — |
| Décret du **24 février** 1914 | droits de voirie | — |
| Décret du 15 décembre 1919 | contribution foncière sur les terrains non bâtis | TNB |
| Décret du 21 avril 1920, et décret du 28 octobre 1948 | taxe d'entretien et d'assainissement | TIB (art. 5 de la loi) |
| Décret du 4 septembre 1947 | taxe de compensation | — |
| Décret du **1er juin** 1951 | taxe sur les spectacles | ch. V |
| Décret du 22 mars 1956 | droit de licence | ch. VII |
| Loi n° 71-41 du 28 juillet 1971, art. 1, 5, 8, 9, 10 et 11 | pesage et mesurage publics | art. 76-78 |
| Loi n° 75-39 du 14 mai 1975 | TCL | ch. III |
| Loi n° 75-34 du 14 mai 1975 | taxe hôtelière | ch. IV |

**Discordances du manuscrit de 2013 (tableau 4-1) avec le JORT.**
- Le manuscrit écrit « décret du 24 janvier [1914] » ; le JORT FR et AR porte **24 février
  1914**.
- Le manuscrit écrit « 1951, décret du 4 septembre » ; le JORT porte le **1er juin 1951**.
- Le manuscrit mentionne un décret « 97-1989 du 6 octobre 1989 » (tableau 4-2), qui ne peut
  exister sous ce numéro.
- Le tableau 4-2 omet les décrets 97-431, 97-432, 97-433 et 97-435 ; il ne cite, de cette série du
  3 mars 1997, que le décret 97-434.

L'abandon de 2002 (loi 2002-76, art. 1) vise encore, pour 1996 et les années antérieures, la
taxe sur la valeur locative, les taxes d'entretien et d'assainissement et la taxe de
compensation.

## 8. Termes arabes (édition arabe du JORT)

Ce relevé est destiné au terminologue. La règle « impôt » de `docs/agents/terminologue.md`
s'applique : l'impôt garde le nom que lui donne son texte. Le code écrit partout **المعلوم على**
(« la taxe sur ») ; jamais ضريبة ni أداء pour ces quatre impôts.

| FR (JORT) | AR (JORT) | Où relevé |
|---|---|---|
| Code de la fiscalité locale | مجلة الجباية المحلية | loi 97-11, p. 173 |
| Taxe sur les immeubles bâtis | المعلوم على العقارات المبنية | code, ch. I, p. 173 |
| Taxe sur les terrains non bâtis | المعلوم على الأراضي غير المبنية | code, ch. II, p. 176 |
| Taxe sur les établissements à caractère industriel, commercial ou professionnel | المعلوم على المؤسسات ذات الصبغة الصناعية أو التجارية أو المهنية | code, ch. III, p. 176 |
| Taxe hôtelière | المعلوم على النزل | code, ch. IV, p. 177 |
| Taxe sur les spectacles | المعلوم على العروض | code, ch. V, p. 178 |
| Contribution des propriétaires riverains | مساهمة المالكين الأجوار | code, ch. VI, p. 178 |
| Droit de licence sur les débits de boissons | معلوم الإجازة الموظف على محلات بيع المشروبات | code, ch. VII, p. 179 ; décret 97-434 |
| Taxes et redevances diverses | معاليم مختلفة | code, ch. VIII, p. 179 |
| Redevance pour légalisation de signature | معلوم التعريف بالإمضاء | art. 64, p. 179 |
| Taxe sur les autorisations administratives | معاليم الرخص الإدارية | art. 68, p. 179 |
| Prix de référence du mètre carré couvert (bâti) | الثمن المرجعي للمتر المربع المبني | art. 4 ; décrets 97-431 et 2017-397 |
| Superficie couverte | المساحة المغطاة | art. 4 |
| Taxe par mètre carré de référence (minimum de la TCL) | المعلوم بالمتر المربع المرجعي | décrets 97-433 et 2017-395 |
| Valeur vénale réelle | القيمة التجارية الحقيقية | art. 33 |
| Zone à haute, moyenne ou basse densité urbaine | منطقة ذات كثافة عمرانية مرتفعة / متوسطة / منخفضة | décrets 97-432 et 2017-396 |
| Chiffre d'affaires brut local | رقم المعاملات المحلي الخام | art. 37 et 39, p. 177 |
| Commission de révision | لجنة المراجعة | art. 24 |
| Recensement | الإحصاء | art. 7 |
| Dégrèvement | الحط (من المعلوم) | art. 6 ; titre du décret 98-1254 |
| Rôle (de recouvrement) | زمام, puis **جدول تحصيل** à partir de 2006 | art. 10 ; LF 2006, art. 56 |
| Contribution au profit du FNAH | المساهمة لفائدة الصندوق الوطني لتحسين السكن | LF 2019, art. 72 ; LF 2024, art. 59 |
| Droits, redevances et taxes (CCL) | المعاليم والرسوم والحقوق | CCL, art. 137-141 et 391 |
| Haute instance des finances locales | الهيئة العليا للمالية المحلية | CCL, art. 391 |

Le glossaire contient déjà `impot-foncier-2014`, dont la définition cite la TIB et la TNB. Il
faudra des entrées pour la TIB, la TNB, la TCL, la taxe hôtelière, le prix de référence et le
code lui-même.

## 9. Références candidates (ébauches CSL-JSON)

Les clés déjà présentes dans `precis/fr/*/references.json` sont à réutiliser :
- `lf-1997`, `lf-1999`, `loi2001-123-lf2002`, `lf-2003` à `lf-2007`, `lf-2010`, `lf-2011` ;
- `lf-2013`, `lf-2014`, `lfc-2014`, `lf-2016`, `loi2018-56-lf2019`, `lf-2021`, `lf-2022` (ou
  `dl2021-21-lf2022` : doublon apparent, à trancher par le bibliographe) ;
- `lf-2023`, `lf-2024`, `lf-2025`, `lf-2026`, `loi-org-2018-29-ccl`, `loi93-64`.

À créer : les textes ci-dessous. Les clés sont indicatives. Les champs `_verifier` sont des notes
de travail, à retirer avant versement.

```json
[
  {"id": "loi97-11", "type": "legislation", "language": "fr",
   "title": "Loi n° 97-11 du 3 février 1997, portant promulgation du code de la fiscalité locale",
   "container-title": "Journal officiel de la République tunisienne", "issue": "11",
   "issued": {"date-parts": [[1997, 2, 7]]}, "page": "173-181",
   "URL": "https://www.pist.tn/jort/1997/1997F/Jo01197.pdf",
   "note": "Code annexé p. 173-181. Entrée en vigueur au 1er janvier 1997 (art. 3). Dépôt au gouvernorat de Tunis le 11 février 1997."},
  {"id": "loi97-11", "type": "legislation", "language": "ar",
   "title": "قانون عدد 11 لسنة 1997 مؤرخ في 3 فيفري 1997 يتعلق بإصدار مجلة الجباية المحلية",
   "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "11",
   "issued": {"date-parts": [[1997, 2, 7]]}, "page": "173-181",
   "URL": "https://www.pist.tn/jort/1997/1997A/Ja01197.pdf"},
  {"id": "decret97-431", "type": "legislation", "language": "fr",
   "title": "Décret n° 97-431 du 3 mars 1997, relatif à la détermination du minimum et du maximum du prix de référence du mètre carré couvert pour chacune des catégories d'immeubles assujettis à la taxe sur les immeubles bâtis",
   "container-title": "Journal officiel de la République tunisienne", "issue": "19",
   "issued": {"date-parts": [[1997, 3, 7]]}, "page": "389",
   "URL": "https://www.pist.tn/jort/1997/1997F/Jo01997.pdf",
   "_verifier": "titre AR relevé à l'image p. 389 : أمر عدد 431 لسنة 1997 مؤرخ في 3 مارس 1997 يتعلق بضبط الحد الأدنى والحد الأقصى للثمن المرجعي للمتر المربع المبني لكل صنف من أصناف العقارات الخاضعة للمعلوم على العقارات المبنية"},
  {"id": "decret97-432", "type": "legislation", "language": "fr",
   "title": "Décret n° 97-432 du 3 mars 1997, relatif à la détermination du montant de la taxe par mètre carré des terrains non bâtis",
   "container-title": "Journal officiel de la République tunisienne", "issue": "19",
   "issued": {"date-parts": [[1997, 3, 7]]}, "page": "389",
   "URL": "https://www.pist.tn/jort/1997/1997F/Jo01997.pdf",
   "_verifier": "titre AR (image p. 389) : أمر عدد 432 لسنة 1997 مؤرخ في 3 مارس 1997 يتعلق بضبط المعلوم بالمتر المربع بالنسبة للأراضي غير المبنية"},
  {"id": "decret97-433", "type": "legislation", "language": "fr",
   "title": "Décret n° 97-433 du 3 mars 1997, relatif à la détermination du montant de la taxe par mètre carré de référence pour chacune des catégories des immeubles à usage industriel, commercial ou professionnel",
   "container-title": "Journal officiel de la République tunisienne", "issue": "19",
   "issued": {"date-parts": [[1997, 3, 7]]}, "page": "389-390",
   "URL": "https://www.pist.tn/jort/1997/1997F/Jo01997.pdf",
   "_verifier": "titre AR (miroir iort) : يتعلق بضبط مبلغ المعلوم بالمتر المربع المرجعي لكل صنف من أصناف العقارات المعدة لتعاطي نشاط صناعي أو تجاري أو مهني"},
  {"id": "decret97-434", "type": "legislation", "language": "fr",
   "title": "Décret n° 97-434 du 3 mars 1997, relatif à la fixation du tarif du droit de licence sur les débits de boissons",
   "container-title": "Journal officiel de la République tunisienne", "issue": "19",
   "issued": {"date-parts": [[1997, 3, 7]]}, "page": "390",
   "URL": "https://www.pist.tn/jort/1997/1997F/Jo01997.pdf"},
  {"id": "decret97-435", "type": "legislation", "language": "fr",
   "title": "Décret n° 97-435 du 3 mars 1997, relatif à la détermination du montant maximum de la taxe sur les établissements à caractère industriel, commercial ou professionnel",
   "container-title": "Journal officiel de la République tunisienne", "issue": "19",
   "issued": {"date-parts": [[1997, 3, 7]]}, "page": "390",
   "URL": "https://www.pist.tn/jort/1997/1997F/Jo01997.pdf"},
  {"id": "decret97-530", "type": "legislation", "language": "fr",
   "title": "Décret n° 97-530 du 22 mars 1997, relatif à la fixation du prix maximum pour l'exonération de la taxe sur les spectacles",
   "container-title": "Journal officiel de la République tunisienne", "issue": "26",
   "issued": {"date-parts": [[1997, 4, 1]]}, "page": "531",
   "URL": "https://www.pist.tn/jort/1997/1997F/Jo02697.pdf"},
  {"id": "decret98-1254", "type": "legislation", "language": "fr",
   "title": "Décret n° 98-1254 du 8 juin 1998, relatif à la fixation des conditions et modalités d'application du dégrèvement de la taxe sur les immeubles bâtis",
   "container-title": "Journal officiel de la République tunisienne", "issue": "48",
   "issued": {"date-parts": [[1998, 6, 16]]}, "page": "1307-1308",
   "URL": "https://www.pist.tn/jort/1998/1998F/Jo04898.pdf"},
  {"id": "loi2002-76", "type": "legislation", "language": "fr",
   "title": "Loi n° 2002-76 du 23 juillet 2002, relative à l'institution de mesures d'allégement de la charge fiscale et d'amélioration des ressources des collectivités locales",
   "container-title": "Journal officiel de la République tunisienne", "issue": "61",
   "issued": {"date-parts": [[2002, 7, 26]]}, "page": "1715",
   "URL": "https://www.pist.tn/jort/2002/2002F/Jo0612002.pdf",
   "_verifier": "titre AR et page AR à relever"},
  {"id": "decret2003-1345", "type": "legislation", "language": "fr",
   "title": "Décret n° 2003-1345 du 16 juin 2003, relatif à la détermination du montant maximum annuel de la taxe sur les établissements à caractère industriel, commercial ou professionnel",
   "container-title": "Journal officiel de la République tunisienne", "issue": "49",
   "issued": {"date-parts": [[2003, 6, 20]]}, "page": "1992",
   "URL": "https://www.pist.tn/jort/2003/2003F/Jo0492003.pdf"},
  {"id": "decret2006-49", "type": "legislation", "language": "fr",
   "title": "Décret n° 2006-49 du 9 janvier 2006, portant fixation des critères de répartition de la taxe sur les établissements à caractère industriel, commercial ou professionnel",
   "container-title": "Journal officiel de la République tunisienne", "issue": "5",
   "issued": {"date-parts": [[2006, 1, 17]]}, "page": "181-182",
   "URL": "https://www.pist.tn/jort/2006/2006F/Jo0052006.pdf"},
  {"id": "decret2006-3360", "type": "legislation", "language": "fr",
   "title": "Décret n° 2006-3360 du 25 décembre 2006, relatif à la détermination du montant maximum annuel de la taxe sur les établissements à caractère industriel, commercial ou professionnel",
   "container-title": "Journal officiel de la République tunisienne", "issue": "2",
   "issued": {"date-parts": [[2007, 1, 5]]}, "page": "29",
   "URL": "https://www.pist.tn/jort/2007/2007F/Jo0022007.pdf"},
  {"id": "decret2007-1185", "type": "legislation", "language": "fr",
   "title": "Décret n° 2007-1185 du 14 mai 2007, relatif à la détermination du minimum et du maximum du prix de référence du mètre carré couvert pour chacune des catégories d'immeubles assujettis à la taxe sur les immeubles bâtis",
   "container-title": "Journal officiel de la République tunisienne", "issue": "40",
   "issued": {"date-parts": [[2007, 5, 18]]}, "page": "1646-1647",
   "URL": "https://www.pist.tn/jort/2007/2007F/Jo0402007.pdf",
   "_verifier": "AR p. 1726-1727 : https://www.pist.tn/jort/2007/2007A/Ja0402007.pdf"},
  {"id": "decret2007-1186", "type": "legislation", "language": "fr",
   "title": "Décret n° 2007-1186 du 14 mai 2007, relatif à la détermination du montant de la taxe par mètre carré des terrains non bâtis",
   "container-title": "Journal officiel de la République tunisienne", "issue": "40",
   "issued": {"date-parts": [[2007, 5, 18]]}, "page": "1647",
   "URL": "https://www.pist.tn/jort/2007/2007F/Jo0402007.pdf",
   "_verifier": "AR p. 1727-1728 ; titre AR (image) : أمر عدد 1186 لسنة 2007 مؤرخ في 14 ماي 2007 يتعلق بضبط المعلوم بالمتر المربع بالنسبة للأراضي غير المبنية"},
  {"id": "decret2007-1187", "type": "legislation", "language": "fr",
   "title": "Décret n° 2007-1187 du 14 mai 2007, relatif à la détermination du montant de la taxe par mètre carré de référence pour chacune des catégories des immeubles à usage industriel, commercial ou professionnel",
   "container-title": "Journal officiel de la République tunisienne", "issue": "40",
   "issued": {"date-parts": [[2007, 5, 18]]}, "page": "1648",
   "URL": "https://www.pist.tn/jort/2007/2007F/Jo0402007.pdf",
   "_verifier": "AR p. 1728"},
  {"id": "loi2007-53", "type": "legislation", "language": "fr",
   "title": "Loi n° 2007-53 du 8 août 2007, complétant les dispositions du code de la fiscalité locale pour l'amélioration des modalités de perception des taxes revenant aux collectivités locales",
   "container-title": "Journal officiel de la République tunisienne", "issue": "64",
   "issued": {"date-parts": [[2007, 8, 10]]}, "page": "2732-2733",
   "URL": "https://www.pist.tn/jort/2007/2007F/Jo0642007.pdf",
   "_verifier": "titre AR et pages AR à relever (couche texte arabe illisible)"},
  {"id": "lf-2009", "type": "legislation", "language": "fr",
   "title": "Loi n° 2008-77 du 22 décembre 2008, portant loi de finances pour l'année 2009",
   "container-title": "Journal officiel de la République tunisienne", "issue": "104",
   "issued": {"date-parts": [[2008, 12, 26]]},
   "URL": "https://www.pist.tn/jort/2008/2008F/Jo1042008.pdf",
   "_verifier": "étendue des pages ; art. 33 p. 4279 ; art. 39 (date d'application) p. 4280"},
  {"id": "lfc-2012", "type": "legislation", "language": "fr",
   "title": "Loi n° 2012-1 du 16 mai 2012, portant loi de finances complémentaire pour l'année 2012",
   "container-title": "Journal officiel de la République tunisienne", "issue": "39",
   "issued": {"date-parts": [[2012, 5, 18]]},
   "URL": "https://www.pist.tn/jort/2012/2012F/Jo0392012.pdf",
   "_verifier": "étendue des pages (début p. 919 selon jort_cache) ; art. 14 p. 923, art. 15-17 p. 924, art. 50 p. 930"},
  {"id": "decret2017-395", "type": "legislation", "language": "fr",
   "title": "Décret gouvernemental n° 2017-395 du 28 mars 2017, relatif à la détermination du montant de la taxe par mètre carré de référence pour chacune des catégories des immeubles à usages industriel, commercial ou professionnel",
   "container-title": "Journal officiel de la République tunisienne", "issue": "26",
   "issued": {"date-parts": [[2017, 3, 31]]}, "page": "1189-1190",
   "URL": "https://www.pist.tn/jort/2017/2017F/Jo0262017.pdf"},
  {"id": "decret2017-395", "type": "legislation", "language": "ar",
   "title": "أمر حكومي عدد 395 لسنة 2017 مؤرخ في 28 مارس 2017 يتعلق بضبط مبلغ المعلوم بالمتر المربع المرجعي لكل صنف من أصناف العقارات المعدة لتعاطي نشاط صناعي أو تجاري أو مهني",
   "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "26",
   "issued": {"date-parts": [[2017, 3, 31]]}, "page": "1004-1005",
   "URL": "https://www.pist.tn/jort/2017/2017A/Ja0262017.pdf"},
  {"id": "decret2017-396", "type": "legislation", "language": "fr",
   "title": "Décret gouvernemental n° 2017-396 du 28 mars 2017, relatif à la détermination du montant de la taxe par mètre carré des terrains non bâtis",
   "container-title": "Journal officiel de la République tunisienne", "issue": "26",
   "issued": {"date-parts": [[2017, 3, 31]]}, "page": "1190-1191",
   "URL": "https://www.pist.tn/jort/2017/2017F/Jo0262017.pdf"},
  {"id": "decret2017-396", "type": "legislation", "language": "ar",
   "title": "أمر حكومي عدد 396 لسنة 2017 مؤرخ في 28 مارس 2017 يتعلق بضبط المعلوم بالمتر المربع بالنسبة للأراضي غير المبنية",
   "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "26",
   "issued": {"date-parts": [[2017, 3, 31]]}, "page": "1005-1006",
   "URL": "https://www.pist.tn/jort/2017/2017A/Ja0262017.pdf"},
  {"id": "decret2017-397", "type": "legislation", "language": "fr",
   "title": "Décret gouvernemental n° 2017-397 du 28 mars 2017, relatif à la détermination du minimum et du maximum du prix de référence du mètre carré couvert pour chacune des catégories d'immeubles assujettis à la taxe sur les immeubles bâtis",
   "container-title": "Journal officiel de la République tunisienne", "issue": "26",
   "issued": {"date-parts": [[2017, 3, 31]]}, "page": "1191-1192",
   "URL": "https://www.pist.tn/jort/2017/2017F/Jo0262017.pdf"},
  {"id": "decret2017-397", "type": "legislation", "language": "ar",
   "title": "أمر حكومي عدد 397 لسنة 2017 مؤرخ في 28 مارس 2017 يتعلق بضبط الحد الأدنى والحد الأقصى للثمن المرجعي للمتر المربع المبني لكل صنف من أصناف العقارات الخاضعة للمعلوم على العقارات المبنية",
   "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "26",
   "issued": {"date-parts": [[2017, 3, 31]]}, "page": "1006",
   "URL": "https://www.pist.tn/jort/2017/2017A/Ja0262017.pdf",
   "_verifier": "fin du décret en p. 1006 ou 1007"}
]
```

Les URL de toutes les éditions citées ont été vérifiées le 4 octobre 2026 avec `curl -sk` (code,
type, taille) :
- 200 `application/pdf` pour tous les fascicules cités ;
- **404** pour les éditions FR de 2015 n° 104, 2018 n° 39, 2018 n° 104, 2022 n° 141, 2023
  n° 144 et 2024 n° 149 ;
- l'URL FR du 2025 n° 148 sert le fichier **arabe** (même taille, 8 775 232 octets) : la LF
  2026 n'a donc pas été lue en français.

## 10. Lacunes, requêtes faites et fiches RECHERCHE proposées

### 10.1 Requêtes faites (4 octobre 2026)

- **jort_cache, FTS** sur titre et objet :
  - « fiscalite locale », « immeubles batis », « terrains non batis », « etablissements a
    caractere », « taxe hoteliere » ;
  - « collectivites locales » AND (taxe OR redevance OR droits) ;
  - termes arabes : الجباية المحلية, العقارات المبنية, الأراضي غير المبنية, المؤسسات ذات الصبغة,
    المبنية, المربع, المرجعي.
- **jort_cache, LIKE**, sans accents, sur les mêmes notions et sur les titres de décrets, pour
  les années 1997-2026.
- **Plein texte FR** de tous les fascicules 1997-2026 du corpus local : « code de la fiscalite
  locale », « fiscalite locale ».
  - Les fascicules à police décalée ont été décodés (années 2000-2006, cf.
    `outillage-sources.md` § 5). La détection du décalage a été corrigée en cours de travail,
    et 1997-2007 rebalayé : les seuls fascicules nouveaux traitent des amnisties de 2006.
  - Recensement de contrôle, 1997-2007 : deux fascicules FR restent illisibles, en clair comme
    décodés (1998 n° 1 et n° 30). Les constats négatifs de cette note n'en tiennent pas compte.
  - Résultat : 846 occurrences, dans environ 190 fascicules.
- **Plein texte AR** de tous les fascicules 1997-2026 : « مجلة الجباية المحلية ».
  - La couche texte arabe est illisible avant 2005 et dans plusieurs fascicules de 2006-2013
    (encodage de police propriétaire).
- **Extraction article par article** des lois de finances :
  - FR, de 1996 n° 105 à 2025 n° 148 ;
  - AR, de 2014 à 2025.
  - Puis inventaire, loi par loi, des articles du code qu'elles citent.
- **Pages et dates.** Pieds de page relus ; mention de dépôt de dernière page relevée pour 23
  fascicules. Tableaux de décrets lus à l'image, en FR et en AR.

### 10.2 Ce qui reste à faire

1. **Pages AR** des articles de 1998 à 2013 dont la couche texte arabe est illisible : LF 1999,
   2002, 2003, 2005, 2007, 2009, 2011, 2013, LFC 2012, lois 2002-76 et 2007-53, décrets 98-1254,
   2003-1345, 2006-49 et 2006-3360. À relever à l'image. Les chiffres des pieds de page
   survivent dans l'extraction : AR = numéro de page PDF + décalage constant.
2. **Portée du § 10 de l'art. 59 du décret-loi 2022-79** sur le taux de 1,25 % de la TIB : le
   texte est lu (§ 2.3), l'interprétation reste à trancher.
3. **Grilles tarifaires du ch. VIII** : décret 98-1428 et ses six modificatifs, décret
   gouvernemental 2016-805 et sa date d'effet. Seules les références sont données. À lire et transcrire à l'image
   si le ch. 8 les retient.
4. **Classification budgétaire** : art. 7 de la loi organique du budget des collectivités
   locales, modifiée par la loi organique n° 2007-65 du 18 décembre 2007 (JORT n° 103 du
   25/12/2007, p. 4277-4281 selon jort_cache). C'est la source de la typologie impôts, taxes et
   redevances (§ 1.2). Non lu.
5. **Code des collectivités locales** (édition arabe seule) :
   - date d'entrée en vigueur des dispositions budgétaires (art. 391 et dispositions finales) ;
   - décrets transitoires pris en vertu de l'art. 391 ;
   - délibérations tarifaires des communes. Ces dernières sont publiées au Journal officiel des
     collectivités locales, hors JORT, donc hors corpus.
6. **Antécédents** : lois 75-34 et 75-39, et les décrets de 1887 à 1956, non lus. Leurs
   modificatifs signalés par jort_cache (décret 76-2, LF 1976, 1980, 1992) relèvent du
   chapitre historique.
7. **Zones municipales touristiques** (taxe hôtelière, fonds de protection des zones
   touristiques) : décret 94-822 et compléments 96-1474, 97-1989 (?), 99-659, 99-2810,
   2001-2510, 2003-186, 2010-479, 2016-895, 2017-969, 2019-1026. Les numéros viennent du
   manuscrit et de jort_cache. Non lus.
8. **Décret-loi n° 2020-33** (auto-entrepreneur), art. 7 dans sa rédaction initiale : non lu.
   On ne sait donc pas si la TCL y était déjà incluse avant 2023.
9. **Arrêtés des collectivités** fixant les prix de référence de la TIB dans les fourchettes :
   hors JORT, à chercher au Journal officiel des collectivités locales ou auprès des communes.
10. **Rapport Essoussi** (DGCT, 2020), signalé dans `biblio-fiscalite-locale.md`, et rapports de
    2014 du ministère de l'Équipement : pistes seulement, non exploitées ici.

### 10.3 Fiches RECHERCHE proposées (non versées dans `docs/recherches.yml`)

`recherches.py lister` ne contient aucune fiche sur la fiscalité locale à ce jour.

```yaml
- id: r-cfl-prix-reference-tib-apres-2017
  objet: décret fixant, après le décret gouvernemental n° 2017-397, le minimum et le maximum du prix de référence du mètre carré couvert de la taxe sur les immeubles bâtis (code de la fiscalité locale, art. 4 § IV, « tous les trois ans »)
  ou: []
  requetes:
    titres_fts: ['"prix de reference"', 'المرجعي', 'المربع', 'المبنية']
    titres_like: ['%prix de reference%', '%immeubles batis%']
    plein_texte: [الثمن المرجعي للمتر المربع, مجلة الجباية المحلية, prix de reference du metre carre]
    depuis: 2017-03-31
  passes:
  - date: 2026-10-04
    role: documentaliste
    sources: [jort_cache, corpus_local, pist]
    couverture: "jort_cache : titres FTS et LIKE, jusqu'au 18/09/2026, seuls les décrets de 2017 répondent. Plein texte AR et FR de tous les fascicules du corpus local 2017-2026, y compris ceux que jort_cache ignore : seul le JORT 2017 n° 26 répond. Lacune : fascicules existant sur pist.tn mais absents du corpus (relancer --sonder-pist non lancé) ; éditions FR absentes après 2018, l'AR seul fait foi."
    couvert_jusqu_au: 2026-09-18
    resultat: aucun
- id: r-cfl-tarif-tnb-apres-2017
  objet: décret fixant, après le décret gouvernemental n° 2017-396, le montant de la taxe par mètre carré des terrains non bâtis (code de la fiscalité locale, art. 33, al. 2, « tous les trois ans »)
  ou: []
  requetes:
    titres_fts: ['"terrains non batis"', 'المبنية', 'المربع']
    titres_like: ['%terrains non batis%']
    plein_texte: [بالمتر المربع بالنسبة للأراضي غير المبنية, مجلة الجباية المحلية, taxe par metre carre]
    depuis: 2017-03-31
  passes:
  - date: 2026-10-04
    role: documentaliste
    sources: [jort_cache, corpus_local, pist]
    couverture: "mêmes sources, même couverture et mêmes lacunes que r-cfl-prix-reference-tib-apres-2017 ; seul le JORT 2017 n° 26 répond"
    couvert_jusqu_au: 2026-09-18
    resultat: aucun
- id: r-cfl-minimum-tcl-apres-2017
  objet: décret fixant, après le décret gouvernemental n° 2017-395, la taxe par mètre carré de référence servant au minimum de la TCL (code de la fiscalité locale, art. 38 § II, « tous les trois ans »)
  ou: []
  requetes:
    titres_fts: ['المرجعي', 'المربع']
    plein_texte: [المتر المربع المرجعي, مجلة الجباية المحلية, taxe par metre carre]
    depuis: 2017-03-31
  passes:
  - date: 2026-10-04
    role: documentaliste
    sources: [jort_cache, corpus_local, pist]
    couverture: "mêmes sources, même couverture et mêmes lacunes que r-cfl-prix-reference-tib-apres-2017 ; seul le JORT 2017 n° 26 répond"
    couvert_jusqu_au: 2026-09-18
    resultat: aucun
- id: r-cfl-prix-reference-1998-2006
  objet: décret fixant le prix de référence de la TIB, le tarif de la TNB ou le minimum de la TCL entre les décrets du 3 mars 1997 et ceux du 14 mai 2007 (« tous les trois ans »)
  ou: []
  requetes:
    titres_fts: ['"prix de reference"', '"terrains non batis"']
    titres_like: ['%prix de reference%', '%terrains non batis%']
    plein_texte: [prix de reference du metre carre, taxe par metre carre, code de la fiscalite locale]
    depuis: 1997-03-07
  periode:
    jusqu_au: 2007-05-18
    motif: "les décrets 2007-1185, 2007-1186 et 2007-1187 n'abrogent que les décrets 97-431, 97-432 et 97-433, ce qui suggère qu'aucun texte intermédiaire n'existe"
  passes:
  - date: 2026-10-04
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: "jort_cache (titres FTS et LIKE 1997-2007) et plein texte FR de tous les fascicules 1997-2007 du corpus local, décodés quand la police est décalée : seuls les JORT 1997 n° 11, 1997 n° 19 et 2007 n° 40 répondent. Lacunes : fascicules FR 1998 n° 1 et n° 30, illisibles en clair comme décodés ; plein texte AR inopérant avant 2005 (encodage de police)."
    couvert_jusqu_au: 2007-05-18
    resultat: aucun
```

Le champ `ou` reste vide : aucune ancre n'existe encore. Le rédacteur le remplira au moment de
poser les ancres `<!-- RECHERCHE r-… -->` dans les chapitres 6 et 7.
