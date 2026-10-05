# Volume VII « Les finances locales », chapitre 4 : note documentaire sur les compétences et l'organisation

> Note du documentaliste, 4 octobre 2026. Elle sert le chapitre 4 du plan
> (`docs/notes/fiscalite-locale-plan.md`, § 2.2) : « Compétences et organisation ». Rien n'y est
> rédigé pour le précis.
>
> **Sources.** Les textes ont été lus dans les fascicules du corpus local
> (`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`) ; métadonnées de `jort_cache.db` (dernière
> publication indexée : 18 septembre 2026), contrôlées au fascicule. Trois documents de doctrine
> ont servi de guides et de source pour les appréciations, toujours attribuées : Dafflon et Gilbert,
> AFD 2018, ch. 4 ; Hammami, Dafflon et Gilbert, 2021 ; Dafflon et Gilbert, note à la DGCL,
> 2015-2016.
>
> **Lecture.**
> - Code des collectivités locales (loi organique n° 2018-29) : **édition arabe seule** (le JORT
>   n° 39 de 2018 n'a pas d'édition française en ligne, voir l'entrée `loi-org-2018-29-ccl`).
>   Couche texte `pdftotext` de `Ja0392018.pdf` contrôlée contre l'image aux p. 1711 et 1747
>   (Read, pages 7 et 43 du PDF) : fidèle. La page JORT de chaque article a été relevée page par
>   page (`pdftotext -f n -l n`, page PDF n = page JORT 1704 + n).
> - Loi n° 75-33 et loi n° 75-37 (JORT n° 34 de 1975) et loi organique n° 89-11 (JORT n° 10 de
>   1989) : fascicules français **numérisés sans couche texte**, et l'océrisation (`ocrmypdf`,
>   puis `tesseract` à 300 dpi avec seuillage) rend un texte inutilisable (scan pâle). Les pages
>   citées ont été **lues à l'image** (Read) : 1975 p. 1056-1058 et 1068 ; 1989 p. 218-219. Les
>   éditions arabes n'ont pas été lues. Avant 1993, l'édition française est la traduction
>   officielle publiée au JORT ; on la cite comme telle.
> - Loi organique n° 2025-4 et décrets n° 2025-177 et 2025-178 : éditions française
>   (couche texte native) et arabe (contrôle des articles cités) lues.
> - Décret-loi n° 2023-9 : édition arabe seule (JORT n° 24 de 2023 ; l'adresse française rend 404).
>
> **URL vérifiées le 4 octobre 2026** (`curl -sk -L`, après une coupure réseau ; les réponses
> « 000 » d'une première passe sont dues à cette coupure) :
>
> | Fascicule | FR | AR |
> |---|---|---|
> | 1975 n° 34 | `/jort/1975/1975F/Jo03475.pdf` 200 pdf | `/jort/1975/1975A/Ja03475.pdf` 200 pdf 3 119 873 o |
> | 1989 n° 10 | `/jort/1989/1989F/Jo01089.pdf` 200 pdf 2 688 907 o | `/jort/1989/1989A/Ja01089.pdf` 200 pdf 2 374 222 o |
> | 2018 n° 39 | (pas d'édition française en ligne) | `/jort/2018/2018A/Ja0392018.pdf` 200 pdf 3 975 742 o |
> | 2023 n° 24 | `/jort/2023/2023F/Jo0242023.pdf` **404** (289 o) | `/jort/2023/2023A/Ja0242023.pdf` 200 pdf 681 682 o |
> | 2025 n° 30 | `/jort/2025/2025F/Jo0302025.pdf` 200 pdf 639 158 o | `/jort/2025/2025A/Ja0302025.pdf` 200 pdf 447 986 o |
> | 2025 n° 41 | `/jort/2025/2025F/Jo0412025.pdf` 200 pdf 731 689 o | `/jort/2025/2025A/Ja0412025.pdf` 200 pdf 530 536 o |
>
> Préfixe : `https://www.pist.tn`. Les champs `pdf_fr` et `pdf_ar` ont été lus dans `jort_cache`
> (recid 116139, 116143, 113816, 196339, 196570, 171303) ; le décret-loi n° 2023-9 n'a qu'un
> `pdf_ar`.
>
> **Dates d'effet** (règle « Dater » d'AGENTS.md). Sans clause d'effet, dépôt au gouvernorat de
> Tunis + 5 jours (loi n° 93-64, art. 2), date de dépôt lue en dernière page du fascicule. Avant
> 1993 : un jour franc après la publication.

## 1. Le code des collectivités locales de 2018 : catégories de compétences

Référence : loi organique n° 2018-29 du 9 mai 2018 relative au code des collectivités locales
(« قانون أساسي عدد 29 لسنة 2018 مؤرخ في 9 ماي 2018 يتعلّق بمجلة الجماعات المحلية »), JORT n° 39 du
15 mai 2018, AR p. 1710-1760. Clé existante : `loi-org-2018-29-ccl`. Dépôt au gouvernorat de
Tunis : 17 mai 2018 (mention de dernière page). Mais l'entrée en vigueur est réglée par le code
lui-même (§ 6.1 ci-dessous, art. 383) : aucune date d'effet unique.

**Termes français.** Le code n'a pas d'édition française au JORT. Les termes français ci-dessous
sont, sauf mention, **notre traduction**. Hammami, Dafflon et Gilbert (2021, p. 26-27) citent une
traduction française du code (non officielle, source non identifiée) qui rend
« صلاحيات ذاتية » par « attributions propres » ou « compétences propres (exclusives) »,
« صلاحيات مشتركة » par « compétences partagées », « صلاحيات منقولة » par « attributions
transférées » ou « compétences transférées », « التدبير الحر » par « libre administration »,
« مبدأ التفريع » par « principe de subsidiarité ». Ce sont les termes de la doctrine ; on peut
les reprendre en le disant.

### 1.1 Livre I, titre I, section 3 « في صلاحيات الجماعات المحلية » (art. 13-24, p. 1711-1712)

- **Art. 2 (p. 1710).** Les collectivités locales sont des « ذوات عمومية » dotées de la
  personnalité juridique et de l'autonomie administrative et financière ; elles se composent de
  communes (بلديات), de régions (جهات) et de districts (أقاليم), chaque catégorie couvrant tout le
  territoire de la République. **Art. 3** : création et limites par la loi. **Art. 4** : chaque
  collectivité gère les intérêts locaux selon le principe de la libre administration (التدبير
  الحر), conformément à la Constitution et à la loi, dans le respect de l'unité de l'État.
  **Art. 5** : communes, régions et districts sont administrés par des conseils élus.
- **Art. 11 (p. 1711).** La répartition des attributions entre catégories, par la loi, par
  convention ou par délégation, n'emporte aucune tutelle (« أي إشراف مهما كان نوعه ») d'une
  collectivité sur une autre.
- **Art. 12.** Une collectivité peut charger (« تكلّف ») une autre collectivité, ou des
  établissements ou entreprises publics, d'exercer l'une de ses compétences propres, par
  délibération à la majorité absolue, et par convention à durée déterminée selon un modèle fixé
  par décret gouvernemental ; la délibération fixe les conséquences financières ; la compétence
  est exercée au nom de la collectivité d'origine.
- **Art. 13 — les trois catégories.** « تتمتّع الجماعات المحلية بمقتضى القانون بصلاحيات ذاتية
  تنفرد بمباشرتها وبصلاحيّات منقولة من السلطة المركزية. تتمتّع الجماعات المحلية بصلاحيّات مشتركة
  مع السلطة المركزية تباشرها بالتنسيق والتعاون معها … » : des compétences propres, exercées
  seules ; des compétences transférées par l'autorité centrale ; des compétences partagées avec
  elle, exercées en coordination et en coopération « sur la base de la bonne gestion des deniers
  publics et de la meilleure prestation des services ». Les conditions et procédures d'exercice
  des compétences partagées sont fixées **par une loi**, après avis du Conseil supérieur des
  collectivités locales.
- **Art. 14.** Exclusivité des compétences propres, sous réserve des cas prévus par le code ;
  l'autorité centrale peut en exercer une part à la demande de la collectivité ; deux
  collectivités ou plus peuvent en exercer une part en coopération ; le représentant de
  l'autorité centrale peut « exceptionnellement » en exercer une part selon les conditions du
  code.
- **Art. 15 — subsidiarité.** Les compétences partagées et transférées sont réparties entre
  catégories « على أساس مبدأ التفريع » : à chaque catégorie celles qu'elle est « la plus à même »
  d'exercer, par sa proximité des habitants et sa capacité à mieux servir les intérêts locaux.
- **Art. 16 — transfert.** Tout transfert ou extension de compétence est fixé **par la loi**, et
  s'accompagne d'un transfert de crédits et de moyens proportionnés aux charges ; l'autorité
  centrale les transfère dans la limite du budget de l'État et sur avis de la Haute instance des
  finances locales.
- **Art. 17.** Les crédits transférés au titre des compétences sont gérés selon la libre
  administration.
- **Art. 18 — compétence générale de la commune.** « تتمتع البلدية بالاختصاص المبدئي العام
  لممارسة الصلاحيات المتعلّقة بالشؤون المحلية » (compétence de principe générale pour les affaires
  locales), seule, en partage avec l'autorité centrale ou en coopération.
- **Art. 19.** La région exerce les compétences propres « à dimension régionale », les
  compétences partagées et les compétences transférées que la loi lui attribue.
- **Art. 20.** Le district exerce les compétences de développement « à dimension de district »
  (planification, études, exécution, coordination, contrôle) ; la loi fixe ses compétences
  partagées et transférées.
- **Art. 21.** Coordination avec les services extérieurs de l'administration centrale, par
  décret gouvernemental.
- **Art. 22-24 (p. 1712).** Respect de la défense nationale et de la sécurité publique ; les
  conseils statuent sur leurs compétences et peuvent consulter la Haute cour administrative ;
  les conflits de compétence entre collectivités et autorité centrale vont à la cour
  administrative d'appel de Tunis (jugement dans le mois), appel devant la Haute cour
  administrative (deux mois) ; entre collectivités, au tribunal administratif territorialement
  compétent (art. 143).
- **Art. 25-28 (p. 1712) — pouvoir réglementaire (السلطة الترتيبية).** Exercé dans les limites
  du territoire et des compétences ; le conseil a la compétence de principe (art. 26) et peut en
  déléguer une part au président ; publication au Journal officiel des collectivités locales
  (art. 28 ; art. 45-46, p. 1715 : exécutoire cinq jours après la publication en ligne).

### 1.2 La commune (Livre II, titre I, section 3, art. 234-244, p. 1739-1741)

- **Art. 234 (p. 1739).** Compétences propres, partagées avec l'autorité centrale et
  transférées par elle.
- **Compétences propres (الفرع الأول, art. 235-242).**
  - art. 235 : « خدمات وتجهيزات القرب » (services et équipements de proximité) ;
  - art. 236 : le conseil examine et approuve le budget, les emprunts, la gestion et la
    valorisation des biens communaux ;
  - art. 237 : le conseil règle les affaires communales, notamment les engagements financiers ;
    **la fixation des droits, redevances et taxes « مهما كانت تسميتها »**, publicité comprise ;
    les décisions financières (cession, échange, location, participations) ; les baux de plus
    de deux ans ; le classement du domaine public ; la transaction ;
  - art. 238 (p. 1740) : programme d'investissement et d'équipement communal ;
  - art. 239 : plans d'urbanisme (أمثلة التخطيط العمراني), règlements locaux de construction ;
  - art. 240 : création et gestion des services publics communaux, dont voirie et trottoirs,
    jardins, collecte et tri des déchets ménagers et assimilés « au sens de la loi n° 2016-30 »
    jusqu'aux décharges contrôlées, éclairage public, bâtiments communaux, réseaux d'eaux
    pluviales (hors ouvrages de protection contre les inondations), marchés, abattoirs,
    prévention sanitaire, propreté et environnement ;
  - art. 241 : soutien à la vie sociale, culturelle, sportive et environnementale ;
  - art. 242 : avis obligatoire du conseil sur tout projet de l'État, de la région, du district
    ou d'une entreprise publique sur le territoire communal, dans les deux mois ; le défaut d'avis
    ou l'opposition n'empêchent pas la réalisation.
- **Compétences partagées (art. 243, p. 1740-1741).** Développement de l'économie locale et
  emploi ; patrimoine culturel ; zones d'activités ; équipements collectifs sociaux, sportifs,
  culturels, environnementaux et touristiques (maisons de la culture, musées, stades, piscines,
  décharges contrôlées, centres de traitement des déchets) ; parcs naturels ; gestion du
  littoral ; **réseaux d'assainissement** ; oueds et ouvrages contre les inondations ; **transport
  urbain et scolaire** ; **entretien des écoles de base, des dispensaires et des centres de santé
  de base** ; bâtiments menaçant ruine ; domaine public maritime ; entretien des routes de l'État
  traversant les zones urbaines (hors autoroutes) ; programmes pour les migrants et les Tunisiens
  à l'étranger. Exercées selon la loi prévue à l'art. 13, al. 2 ; spécificités des îles.
- **Compétences transférées (art. 244, p. 1741).** Construction et entretien des établissements
  et centres de santé, des établissements éducatifs, des équipements culturels, des équipements
  sportifs. « ويقترن وجوبا كلّ نقل لصلاحية بتحويل الموارد المالية والبشرية الضرورية لممارستها » ;
  réalisation par convention entre l'autorité centrale et la commune.

Tableau de synthèse publié par Hammami, Dafflon et Gilbert (2021, p. 27) : propres art. 235-242
(communes) et 296 (régions) ; transférées 244 et 298 ; partagées 243 et 297. Concorde avec la
lecture ci-dessus.

### 1.3 La région (Livre II, titre II, section 1, art. 293-298, p. 1747-1748)

- **Art. 293 (p. 1747).** La région, collectivité locale à personnalité juridique et autonomie
  administrative et financière, gère les affaires régionales selon la libre administration et
  œuvre au développement global et solidaire, en coordination avec l'autorité centrale et les
  autres collectivités. **Art. 294** : création par la loi ; le code confirme les régions
  existantes (annexe « ب »).
- **Art. 295.** Mêmes trois catégories.
- **Propres (art. 296, p. 1747).** Plans de développement régional par la démocratie
  participative, « مع مراعاة مقتضيات التنمية المستدامة والاقتصاد الأخضر » ; gestion des services et
  équipements publics à dimension régionale (circuits de distribution, environnement, culture,
  sport, jeunesse, affaires sociales, emploi, personnes âgées) et entretien de ses
  installations ; organisation et soutien du transport non urbain à l'intérieur de la région.
  (Texte relu à l'image, p. 1747 : la couche texte entrelace les colonnes à cet article.)
- **Partagées (art. 297, p. 1748).** Plans d'aménagement du territoire régional ; équipements
  publics à dimension régionale ; zones industrielles, artisanales, commerciales et
  touristiques ; accueil des investisseurs ; sites naturels et archéologiques ; activités
  culturelles, sportives et sociales ; formation professionnelle adaptée à la région ; transport
  urbain à dimension régionale ; ouverture des établissements d'enseignement et de recherche ;
  marché du travail ; dialogue social ; migration.
- **Transférées (art. 298, p. 1748).** Entretien et aménagement des infrastructures, bâtiments
  et équipements publics à dimension régionale ; soutien aux activités agricoles, industrielles
  et commerciales et à l'investissement ; même obligation de transfert des moyens.

### 1.4 Le district (Livre II, titre III, art. 356-382, p. 1756-1758)

- **Art. 356 (p. 1756).** Le district (« الإقليم ») est une collectivité locale à personnalité
  juridique et autonomie administrative et financière, chargée de l'intégration et de la
  complémentarité du développement entre les zones qui le composent. **Art. 357** : son conseil
  est élu par les membres des conseils municipaux et régionaux.
- **Art. 358.** Le conseil délibère sur les questions de développement à dimension de district ;
  plans d'aménagement durable ; propositions de projets (transport, communications, eau,
  électricité, assainissement) soumis aux autorités centrales et locales pour financement ;
  politiques de développement ; attractivité ; budget et biens ; environnement ; services publics
  à dimension de district. **Art. 360** : participation obligatoire à l'élaboration des plans
  nationaux de développement.
- **Art. 389 (p. 1760)** : le Conseil supérieur siège sans représentants des districts jusqu'à
  leur création ; **art. 394** : jusqu'à la création des districts, leur part des produits de
  l'art. 148 revient aux communes.

### 1.5 La délégation et la dévolution au sens de la doctrine

- Les mots « délégation » et « dévolution » ne sont pas ceux du code : il dit « propres »,
  « partagées », « transférées ». La correspondance est une **interprétation**, à attribuer.
- Dafflon et Gilbert (note DGCL, 2015-2016, p. 1) distinguent la tâche « entièrement dévolue » à
  la collectivité (conception, décision et mise en œuvre : dévolution) de la tâche dont elle
  n'assure que la mise en œuvre d'un composant décidé par l'autorité supérieure (délégation).
  Ils proposent un processus en cinq étapes (p. 1-2) : préciser la tâche ; identifier ses
  composants (« fonction de production ») ; choisir les critères d'affectation de chaque
  composant à un niveau ; définir les besoins (rattrapage et besoins structurels) ; financer,
  l'art. 132 de la Constitution de 2014 exigeant l'adéquation des ressources aux prérogatives.
- Hammami, Dafflon et Gilbert (2021) :
  - p. 27 : la Constitution de 2014 (art. 134) parle de compétences « déléguées », le code de
    compétences « transférées » ; ils se demandent si la différence est significative ou tient à
    la traduction ;
  - p. 28 : le code « esquisse » la définition des compétences propres et partagées et « reste
    silencieux » sur celle des compétences transférées ;
  - p. 28-29 : une responsabilité « partagée » sans autre précision conduit selon eux à
    l'inaction, à la recentralisation de fait (« tâche déconcentrée ») ou aux doublons ; ils
    proposent de la préciser composant par composant (« par intrant ») ;
  - p. 29 : l'art. 15 reprend le principe de subsidiarité de l'art. 134 de la Constitution ;
    d'autres principes sont dispersés dans le code (tableau 3 : libre administration art. 4 et
    17, subsidiarité art. 15 et 75, égalité art. 25 et 75…) ;
  - p. 6 (avant-propos) : rappel des réformes engagées depuis 2014 (communalisation intégrale
    en 2016, loi électorale locale en 2017, code en 2018, premières élections municipales en
    2018) — appréciation des auteurs, dates non contrôlées au JORT ici.
- Dafflon et Gilbert (AFD 2018, § 4.3, p. 122-130) analysent l'état antérieur au code : la loi
  n° 89-11 pour les régions et la loi organique des communes dans sa rédaction de la loi
  organique n° 2006-48. Selon eux :
  - la région porte une « double casquette » (circonscription déconcentrée et collectivité,
    art. 1 de la loi n° 89-11) ; les compétences de l'art. 2 sont cadrées par le plan national,
    d'où une « mainmise nationale » sur la planification et les projets (p. 122-124) ;
  - ni la Constitution de 1959 ni la « mini-constitution » de 2011 ne donnent de liste de
    compétences communales ; la loi organique des communes ne les énumère pas explicitement, et
    les auteurs les reconstituent par inférence (tableau 13, p. 128-130) (p. 125-126) ;
  - § 4.5 [1] (p. 135) : lister les compétences ne dit rien de la frontière entre délégation et
    dévolution ; il existe une « zone grise ».

## 2. Organisation des collectivités sous le code de 2018

### 2.1 Organes de la commune

- **Conseil municipal (art. 203, p. 1735)** élu selon la loi électorale ; il élit le président
  et les adjoints (art. 7 : sauf impossibilité, le président et le premier adjoint sont de sexes
  différents ; le président ou l'un des premiers adjoints a moins de 35 ans, p. 1710).
- **Dissolution (art. 204, p. 1735).** Sauf cas prévus par la loi, uniquement s'il est
  impossible de recourir à d'autres solutions, par **décret gouvernemental motivé**, après
  consultation du Conseil supérieur et sur avis de la Haute cour administrative, pour violation
  grave de la loi ou blocage manifeste des intérêts des habitants, après audition des membres.
  En urgence, suspension par le ministre chargé des collectivités locales, sur rapport motivé du
  gouverneur (والي), pour deux mois au plus. Recours devant le tribunal administratif de première
  instance ; la suspension ou la dissolution ne prend effet qu'après rejet de la demande de
  sursis ou expiration du délai. Le secrétaire général gère l'administration pendant la
  suspension ; une commission provisoire de gestion (اللجنة المؤقتة للتسيير, art. 208) assure les
  affaires courantes après dissolution.
- **Président (art. 256-257, p. 1742).** Représentant légal ; sous le contrôle du conseil :
  gestion des biens, alignement, direction de l'administration, nominations dans la limite du
  budget, gestion des recettes, préparation du budget et ordonnancement, recensement des
  immeubles et activités assujettis aux impôts locaux, marchés, actions en justice…
- **Bureau municipal (art. 269, p. 1745)** : président, adjoints, présidents de commissions et
  d'arrondissements ; au moins une réunion par mois.
- **Administration municipale (art. 270-275, p. 1745).** Neutralité, égalité, transparence ;
  agents soumis au statut général de la fonction publique (art. 271) ; organigramme approuvé par
  le conseil, sur modèle fixé par décret gouvernemental ; **secrétaire général** sous l'autorité
  du président (art. 272) ; agents payés sur le budget communal, l'autorité centrale pouvant
  mettre à disposition des agents qu'elle continue de rémunérer (art. 273) ; nominations par le
  président dans la limite des effectifs votés (art. 274).
- Pour la région, mêmes organes (art. 299 s., conseil régional ; président, art. 334 « تحت رقابة
  المجلس الجهوي », p. 1753 ; bureau, art. 339 ; administration, art. 340 s.). Non relus en détail.

### 2.2 Instances nationales

- **Conseil supérieur des collectivités locales (المجلس الأعلى للجماعات المحلية), art. 47-60,
  p. 1715-1716.** Compétences (art. 47) : développement et équilibre entre régions, cohérence des
  politiques et programmes locaux et nationaux, coopération entre collectivités, suivi de la
  formation. Composition (art. 48) : un président de commune par région élu par ses pairs ; les
  présidents des quatre communes les plus peuplées et des quatre communes au plus faible indice
  de développement (de régions différentes) ; les présidents de régions et de districts. Avis
  obligatoire sur les projets de loi intéressant les collectivités, notamment planification,
  budget et finances locales (art. 53) ; réunion annuelle en juin sur les finances locales avec
  la Haute instance (art. 54) ; rapports d'évaluation des transferts de compétences (art. 55) ;
  rapport annuel (art. 57). Ressources (art. 52) : contributions des collectivités (0,1 % ou
  0,05 % des transferts du fonds de l'art. 38, selon l'indice de développement), budget de l'État,
  dons ; comptes soumis à la Cour des comptes.
- **Haute instance des finances locales (الهيئة العليا للمالية المحلية), art. 61-65,
  p. 1716-1717.** Placée sous la supervision du Conseil supérieur ; missions (art. 61) :
  propositions au gouvernement, estimation des ressources transférables dans le projet de budget
  de l'État, critères de répartition des transferts, suivi du fonds de l'art. 38, étude préalable
  du coût des transferts de compétences, analyses financières, masse salariale (art. 9),
  endettement, études triennales. Rapport annuel (art. 62). Composition (art. 63) : un magistrat
  financier président, neuf représentants du Conseil supérieur, des représentants des ministères
  (collectivités locales, finances, domaines), de la CPSCL (« صندوق القروض ومساعدة الجماعات
  المحلية »), un expert-comptable, un comptable. Budget de l'État, rattachement au ministère
  chargé des affaires locales (art. 65).
- **Progressivité (التدرج), art. 66-68, p. 1717.** L'État adopte un système décentralisé
  « conformément au chapitre VII de la Constitution » et lui fournit « progressivement » les
  conditions de son efficacité ; une loi d'orientation, votée dans la première année de chaque
  législature, fixe un plan de soutien à la décentralisation ; rapport annuel du gouvernement au
  Parlement avant le 15 février ; évaluation par le Conseil supérieur et, sur demande du
  Parlement, par la Cour des comptes.
- **Formation (art. 43-44, p. 1714).** Droit à la formation des élus et des agents ; crédits de
  formation d'au moins 0,5 % du budget de fonctionnement ; commission nationale de formation des
  élus, réunie au **Centre de formation et d'appui à la décentralisation** (« مركز التكوين ودعم
  اللامركزية »), qui en supporte les frais et en assure le secrétariat.
- **Masse salariale (art. 9, p. 1710-1711).** Les dépenses de rémunération ne doivent pas dépasser
  50 % des ressources ordinaires réalisées ; au-delà, programme de maîtrise soumis à la Haute
  instance et à l'autorité centrale. (Seuil unique, sans série : à citer comme règle, pas comme
  chiffre isolé.)

### 2.3 Contrôle des actes : la fin de la tutelle a priori

- **Commune, art. 276-280 (p. 1745-1746).** Les arrêtés réglementaires sont exécutoires cinq
  jours après leur publication en ligne au Journal officiel des collectivités locales (art. 276) ;
  le trésorier régional est informé des décisions à incidence financière dans les dix jours.
  Les décisions individuelles sont motivées (art. 277). **Art. 278** : « للوالي بمبادرة منه أو
  بطلب ممن له مصلحة الاعتراض على القرارات التي تتخذها البلدية » — le gouverneur peut contester les
  décisions communales **devant le juge** (copie de la requête au président trois jours avant le
  dépôt) et demander le sursis à exécution ; si la décision porte atteinte à une liberté publique
  ou individuelle, le président du tribunal administratif de première instance ordonne le sursis
  dans les cinq jours ; tout intéressé peut saisir directement le juge. Art. 279 : nullité des
  délibérations auxquelles ont pris part des membres intéressés, prononcée par le tribunal
  administratif à l'initiative du gouverneur ou d'un intéressé.
- **Région, art. 346-349 (p. 1755)** : mêmes règles.
- **Contrôle financier, art. 197-199 (p. 1735).** Recours devant la chambre de la Cour des comptes
  territorialement compétente contre les décisions de préparation, d'exécution et d'équilibre du
  budget (représentant de l'autorité centrale ou contribuables locaux, art. 197) ; contrôle
  **a posteriori** du respect des lois et règlements financiers par les services d'inspection et
  de contrôle de l'autorité centrale (art. 198) ; inspection à la demande du conseil (art. 199).
  (Relève surtout du chapitre 5, budgets.)
- **Transition (art. 386-388, p. 1759-1760)** : en attendant les tribunaux administratifs de
  première instance et d'appel, les chambres du Tribunal administratif ; en attendant la Cour des
  comptes, la Chambre des comptes (loi n° 68-8).
- Hammami, Dafflon et Gilbert (2021, p. 26, encadré 1) : l'art. 138 de la Constitution de 2014
  soumet les collectivités au seul contrôle a posteriori de la légalité de leurs actes. Texte de
  la Constitution à lire au JORT (chapitre 3, autre note).

### 2.4 Modes de gestion des services et organismes locaux

- **Art. 80-83 (p. 1719).** Gestion directe ou indirecte, choisie selon l'efficacité et la qualité
  (art. 80) ; régie directe en principe pour les services administratifs, possible sous forme de
  « وكالة » (régie, art. 81) ; régie dotée d'un budget spécial et d'une comptabilité d'entreprise
  (art. 82) ; concession (« اللزمة », art. 83 s.).
- **Art. 103-104 (p. 1722).** Entreprises publiques locales (« منشآت عمومية محلية » : établissement
  public local ou société anonyme dont les collectivités détiennent plus de la moitié du capital)
  pour les services industriels et commerciaux ; création ou participation par délibération.
- **Coopération intercommunale, art. 281-292** (p. 1746-1747) : établissements de coopération
  (« مؤسسات التعاون بين البلديات »), soumis au contrôle a posteriori et au juge administratif
  (art. 284). Non relus en détail.

### 2.5 Agences et organismes publics nationaux

- **Caisse des prêts et de soutien des collectivités locales (CPSCL).** Loi n° 75-37 du 14 mai
  1975 (JORT n° 34 du 20 mai 1975, FR p. 1068, lue à l'image) : la caisse des prêts aux communes
  « instituée par le décret du 15 décembre 1902 et réorganisée par le décret du 1er mars 1932 » est
  transformée en caisse des prêts et de soutien des collectivités locales (art. 1) ; personnalité
  civile et autonomie financière (art. 2) ; ressources : prélèvement sur le Fonds commun des
  collectivités locales (loi n° 75-36), annuités de remboursement, emprunts, produits financiers
  (art. 3) ; elle consent aux communes, syndicats de communes, conseils de gouvernorat et
  établissements publics locaux des prêts d'investissement, des subventions aux collectivités en
  difficulté et des bonifications d'intérêts (art. 4) ; **effet : 1er janvier 1976** (art. 6,
  clause expresse). Les décrets de 1902 et 1932 ne sont connus ici que par ce visa. **Historique
  seulement** : la CPSCL relève du chapitre 9 (transferts), écrit par un autre agent.
- **Centre de formation et d'appui à la décentralisation.** Cité par le code (art. 44). Seul
  l'intitulé de son décret d'organisation est connu ici : décret n° 2004-1182 du 25 mai 2004
  fixant l'organisation administrative et financière et les modalités de fonctionnement du
  centre (JORT n° 44 du 1er juin 2004, p. 1445-1447 selon jort_cache ; couche texte du fascicule
  à police décalée, non décodée). Son texte de création n'est pas identifié.
- **Agences nationales qui exercent des tâches locales.** Dafflon et Gilbert (AFD 2018, § 4.4,
  p. 130-134) listent l'AFH, l'ARRU (loi n° 81-69), la STEG, l'ANPE (loi n° 88-91), la SONEDE
  (loi n° 68-22), l'ONAS, l'ANGed (décret n° 2005-2317), l'APAL/ANPL (loi n° 95-72), l'APIP
  (loi n° 92-32), l'AFT (loi n° 73-21), l'AFI. Selon eux, une partie de leurs tâches « entre dans
  le champ des compétences qui pourraient être dévolues ou déléguées » aux collectivités, et leur
  externalisation prive celles-ci de ressources potentielles (p. 130). **Ces textes de création
  n'ont pas été lus** : n'en citer que l'appréciation des auteurs, ou les lire avant d'en dater
  un seul.

## 3. L'organisation antérieure

### 3.1 La loi organique des communes de 1975

Loi n° 75-33 du 14 mai 1975, portant promulgation de la loi organique des communes, JORT n° 34
du 20 mai 1975, FR p. 1056-1065 (lue à l'image, p. 1056-1058). Rectificatif : JORT n° 53 du
1er août 1975, p. 1628 (jort_cache, non lu). Clé proposée : `loi75-33`.

- **Loi de promulgation, art. 2 (p. 1056)** : abroge notamment le décret du 14 mars 1957 portant
  loi municipale, la loi n° 59-43 du 5 février 1959 (syndicats de communes), une loi de 1969 sur
  la représentation des communes dans les sociétés (numéro mal lisible à l'image : « 69-? du
  5 février 1969 », **à relire**), la loi n° 73-50 du 2 août 1973 (municipalité de Tunis).
- **Art. 1er (p. 1056)** : « La commune est une collectivité publique locale, dotée de la
  personnalité civile et de l'autonomie financière et chargée de la gestion des intérêts
  municipaux. Elle participe dans le cadre du plan national de développement à la promotion
  économique sociale et culturelle de la localité. » **Art. 2** : création par décret sur
  proposition du ministre de l'Intérieur, après avis des ministres des Finances et de
  l'Équipement. Art. 9 : suppression par décret.
- **Art. 12-13 (p. 1056)** : dissolution du conseil par décret motivé ; en urgence, suspension par
  arrêté motivé du ministre de l'Intérieur, deux mois au plus ; délégation spéciale nommée par
  décret.
- **Art. 36 (p. 1057) — attributions** : « Le Conseil Municipal règle par ses délibérations les
  affaires de la commune » : il examine et approuve le budget ; fixe le programme d'équipement
  dans la limite des ressources ; définit, conformément au plan national, les actions de
  développement ; donne son avis sur les affaires d'intérêt local ; est consulté sur tout projet
  de l'État ou d'une autre collectivité sur son territoire.
- **Art. 38-41 (p. 1058) — nullité et annulation** : nullité de plein droit des délibérations
  étrangères aux attributions ou contraires aux lois, déclarée par **arrêté motivé du gouverneur** ;
  annulation des délibérations des membres intéressés, par arrêté motivé du gouverneur.
- **Art. 42 (p. 1058) — approbation préalable (tutelle a priori)** : ne sont exécutoires qu'après
  approbation de l'autorité supérieure les délibérations portant sur le budget ; les contributions
  extraordinaires et emprunts ; les taxes locales et droits divers dont la perception est
  autorisée ; aliénations et acquisitions ; baux de plus de trois ans ; transactions au-delà d'un
  seuil ; dénomination des rues ; classement et alignement des voies ; foires et marchés ;
  intervention dans des entreprises industrielles ou commerciales ; règlements généraux ; dons et
  legs grevés de charges.
- **Art. 43 (p. 1058)** : approbation par le gouverneur, « sous réserve des dispositions de
  l'article 24 de la loi n° 75-35 du 14 mai 1975 » ; par les ministres de l'Intérieur et des
  Finances pour certains objets (§ 2, 9, 10, 12 de l'art. 42) ; par le ministre de l'Intérieur
  pour d'autres ; par le délégué pour les baux de 3 à 9 ans et taxes et droits divers des communes
  dont le budget est approuvé par lui. **Art. 45** : approbation tacite après quinze jours.
  **Art. 46** : les autres délibérations sont exécutoires quinze jours après leur dépôt.
- **Art. 48 (p. 1058)** : présidents des communes dont le budget relève du « paragraphe 2 de
  l'article 13 de la loi n° 75-35 » exercent à plein temps.
- **Modificatifs** (jort_cache, **non lus**) : lois organiques n° 85-43 du 25 avril 1985 (JORT
  n° 34, p. 642-644), n° 91-24 du 30 avril 1991 (JORT n° 30, p. 947), n° 95-68 du 24 juillet 1995
  (JORT n° 59, p. 1563-1566), **n° 2006-48 du 17 juillet 2006 (JORT n° 59 du 25 juillet 2006,
  p. 1923-1930)** — rédaction analysée par Dafflon et Gilbert —, n° 2008-57 du 4 août 2008 (JORT
  n° 64, p. 2413).
- **Date d'effet de la loi n° 75-33** : pas de clause d'effet lue sur les pages vues ; publication
  le 20 mai 1975, donc exécutoire le 22 mai 1975 (un jour franc). **À confirmer** sur la fin du
  texte (p. 1065, non lue).
- Sort de la loi après 2018 : non établi ici. Le code de 2018 ne l'abroge pas dans les
  articles lus (383-400) ; aucun article d'abrogation générale n'a été relevé dans le Livre III.
  **À vérifier** (Dafflon 2021 ou l'arrêté de mise en œuvre).

### 3.2 Les conseils régionaux (loi organique n° 89-11)

Loi organique n° 89-11 du 4 février 1989 relative aux conseils régionaux, JORT n° 10 du
10 février 1989, FR p. 218-221 (lue à l'image, p. 218-219). Arabe : « القانون الأساسي عدد 11 لسنة
1989 المؤرخ في 4 فيفري 1989 المتعلّق بالمجالس الجهوية » (intitulé tel que cité par le code de 2018,
art. 384). Clé proposée : `loi-org89-11`. Exécutoire le 12 février 1989 (un jour franc après le
10 ; pas de clause d'effet sur les pages lues — art. finaux p. 220-221 non lus).

- **Art. 1er (p. 218)** : « Le gouvernorat est une circonscription territoriale administrative de
  l'État. Il est, en outre, une collectivité publique dotée de la personnalité morale et de
  l'autonomie financière, gérée par un conseil régional et soumise à la tutelle du ministre de
  l'intérieur. »
- **Art. 2 (p. 218-219)** : le conseil examine toutes questions intéressant le gouvernorat ; plan
  régional de développement (dans le cadre du plan national) ; plans d'aménagement hors
  périmètres communaux ; avis sur programmes et projets de l'État ; programmes régionaux ;
  réalisation des projets régionaux arrêtés par les ministères ; coordination ; coopération entre
  communes.
- **Art. 3** : le conseil arrête le budget de fonctionnement et d'équipement, et les impôts et
  taxes recouvrés au profit de la collectivité. **Art. 4** : patrimoine du gouvernorat.
- **Art. 6 (p. 219) — composition** : le **gouverneur, président** ; les députés de la
  circonscription ; les présidents des communes ; les présidents des conseils ruraux (art. 49).
  Le gouverneur préside et ne prend pas part au vote.
- **Art. 9** : dissolution par décret motivé ; suspension par arrêté du ministre de l'Intérieur.
- **Art. 18-21 (p. 219)** : nullité et annulation des délibérations par **arrêté motivé du
  ministre de l'Intérieur**.
- Modificatifs repérés (non lus) : loi organique n° 93-119 du 27 décembre 1993 ; loi organique
  n° 2011-1 du 3 janvier 2011 (composition).
- Le code de 2018 maintient la loi n° 89-11 jusqu'à l'installation des conseils régionaux élus
  (art. 384) ; la part de la région revient d'ici là au gouvernorat collectivité (art. 394) ; les
  biens du gouvernorat passent à la région à la proclamation des premières élections régionales
  (art. 397).
- Dafflon et Gilbert (AFD 2018, p. 122) : la région a une « double casquette ».

## 4. Depuis 2023

- **Décret-loi n° 2023-9 du 8 mars 2023 relatif à la dissolution des conseils municipaux**
  (« مرسوم عدد 9 لسنة 2023 مؤرّخ في 8 مارس 2023 يتعلق بحلّ المجالس البلدية »), JORT n° 24 du
  9 mars 2023, AR p. 694. Art. 1 : dissolution de **tous** les conseils municipaux jusqu'à
  l'élection de nouveaux conseils ; art. 2 : le chargé du secrétariat général de la commune,
  « sous la supervision du gouverneur », gère les affaires courantes et l'administration ;
  art. 3 : abrogation des dispositions contraires. Pas de clause d'effet : dépôt le 9 mars 2023,
  **exécutoire le 14 mars 2023**. Clé proposée : `decretloi2023-9` (AR seulement ; pas d'URL FR).
  Probable recoupement avec la note du chapitre 3 (histoire).
- **Décret-loi n° 2023-10 du 8 mars 2023** (élections des conseils locaux, composition des conseils
  régionaux et de districts), même JORT, AR p. 694 s. — **non lu ici** (chapitre 3).
- **Loi organique n° 2025-4 du 12 mars 2025 relative aux conseils locaux, conseils régionaux et
  conseils de districts** (« قانون أساسي عدد 4 لسنة 2025 مؤرخ في 12 مارس 2025 يتعلق بالمجالس
  المحلية والمجالس الجهوية ومجالس الأقاليم »), JORT n° 30 du 13 mars 2025, FR p. 706, AR
  p. 775-776. Clé proposée : `loi-org2025-4`. Pas de clause d'effet ; dépôt le 13 mars 2025 :
  **exécutoire le 18 mars 2025**.
  - art. 1 : ces conseils « sont considérés comme des collectivités locales » à personnalité
    juridique et autonomie administrative et financière ; ils œuvrent à l'inclusion économique et
    sociale et **délibèrent sur les projets de plans de développement** locaux, régionaux et de
    districts ; leur organisation est fixée **par décret** ;
  - art. 3 : session au moins mensuelle ; art. 4 : indemnité fixée par décret ;
  - art. 5 : régis par la loi organique relative à leur budget et par la loi sur la comptabilité
    publique ; le président est ordonnateur ;
  - art. 7 : siège du conseil local à la délégation (معتمدية), du conseil régional et du conseil de
    district au gouvernorat ;
  - **art. 8 : budget régi par la loi organique n° 75-35 du 14 mai 1975** (budget des collectivités
    locales) en tant qu'elle n'est pas contraire (intéresse le chapitre 5) ;
  - art. 9 : les biens, patrimoine, participations et dotations du conseil régional au sens de la
    loi n° 89-11 sont **transférés à l'État et mis à la disposition du gouverneur** ;
  - **art. 10 : abroge** les dispositions contraires, « notamment » **les dispositions relatives à
    la région et au district du code des collectivités locales**, la loi organique n° 89-11 et la
    loi n° 94-87 du 26 juillet 1994 (conseils locaux de développement).
  - Conséquence à dater : depuis le 18 mars 2025, le Livre II, titres II (région) et III (district)
    du code de 2018, et les dispositions du Livre I qui les visent, ne s'appliquent plus ; les
    dispositions relatives à la commune ne sont pas visées par l'abrogation expresse. Le périmètre
    exact des dispositions « contraires » abrogées n'est pas tranché par le texte.
- **Décret n° 2025-177 du 4 avril 2025** fixant l'organisation des travaux des conseils locaux,
  régionaux et de districts et leur mode de fonctionnement, JORT n° 41 du 5 avril 2025, FR p. 836.
  Dépôt le 5 avril 2025 : **exécutoire le 10 avril 2025**. Art. 1 : le président, représentant
  légal, conduit les séances, conserve archives et documents comptables, **supervise la
  préparation du budget, le soumet au conseil et l'exécute** ; art. 3-4 : secrétariat assuré à
  tour de rôle par les membres élus (préparation du budget) ; art. 5 : les conseils délibèrent
  sur les propositions de plans de développement ; art. 7 : les conseils de districts transmettent
  leurs rapports de synthèse au ministère chargé de la planification. Clé proposée :
  `decret2025-177`.
- **Décret n° 2025-178 du 4 avril 2025** (indemnité de représentation), même JORT, p. 836-837 :
  indemnité **imputée sur le budget du ministère de l'Intérieur** (art. 3). Montant : chiffre
  isolé, à ne pas publier sans série. Clé proposée : `decret2025-178` (facultatif).
- Aucun texte postérieur à mars 2023 n'organise, dans les intitulés de jort_cache, de nouvelles
  élections municipales (fiche proposée § 7).

## 5. Références candidates (ébauches CSL-JSON)

Déjà présentes : `loi-org-2018-29-ccl` (fonds commun), `dafflon-gilbert-2018`
(`finances_locales`), `loi93-64` (fonds commun).

```json
[
 {"id":"loi75-33","type":"legislation",
  "title":"Loi n° 75-33 du 14 mai 1975, portant promulgation de la loi organique des communes",
  "title-short":"Loi n° 75-33 du 14 mai 1975",
  "container-title":"Journal officiel de la République tunisienne","issue":"34","page":"1056-1065",
  "issued":{"date-parts":[[1975,5,14]]},
  "URL":"https://www.pist.tn/jort/1975/1975F/Jo03475.pdf",
  "note":"citation-key: loi75-33\nJORT n° 34 du 20 mai 1975, p. 1056-1065 (jort_cache recid 116139). Fascicule FR numérisé sans couche texte : p. 1056-1058 lues à l'image. Rectificatif : JORT n° 53 du 1er août 1975, p. 1628."},
 {"id":"loi75-37","type":"legislation",
  "title":"Loi n° 75-37 du 14 mai 1975, portant transformation de la caisse des prêts aux communes en une caisse des prêts et de soutien des collectivités locales",
  "title-short":"Loi n° 75-37 du 14 mai 1975",
  "container-title":"Journal officiel de la République tunisienne","issue":"34","page":"1068",
  "issued":{"date-parts":[[1975,5,14]]},
  "URL":"https://www.pist.tn/jort/1975/1975F/Jo03475.pdf",
  "note":"citation-key: loi75-37\nJORT n° 34 du 20 mai 1975, p. 1068 (recid 116143), lue à l'image. Art. 6 : effet au 1er janvier 1976."},
 {"id":"loi-org89-11","type":"legislation",
  "title":"Loi organique n° 89-11 du 4 février 1989, relative aux conseils régionaux",
  "title-short":"Loi organique n° 89-11 du 4 février 1989",
  "container-title":"Journal officiel de la République tunisienne","issue":"10","page":"218-221",
  "issued":{"date-parts":[[1989,2,4]]},
  "URL":"https://www.pist.tn/jort/1989/1989F/Jo01089.pdf",
  "note":"citation-key: loi-org89-11\nJORT n° 10 du 10 février 1989, p. 218-221 (recid 113816). FR lue à l'image, p. 218-219. Abrogée par l'art. 10 de la loi organique n° 2025-4."},
 {"id":"decretloi2023-9","type":"legislation",
  "title":"Décret-loi n° 2023-9 du 8 mars 2023, relatif à la dissolution des conseils municipaux",
  "title-short":"Décret-loi n° 2023-9 du 8 mars 2023",
  "container-title":"Journal officiel de la République tunisienne","issue":"24","page":"694",
  "issued":{"date-parts":[[2023,3,8]]},
  "note":"citation-key: decretloi2023-9\nJORT n° 24 du 9 mars 2023, édition arabe p. 694 (recid 171303, numero NULL dans jort_cache). Intitulé français : notre traduction ; l'édition française (Jo0242023.pdf) rend 404. Dépôt au gouvernorat de Tunis le 9 mars 2023."},
 {"id":"loi-org2025-4","type":"legislation",
  "title":"Loi organique n° 2025-4 du 12 mars 2025, relative aux conseils locaux, conseils régionaux et conseils de districts",
  "title-short":"Loi organique n° 2025-4 du 12 mars 2025",
  "container-title":"Journal officiel de la République tunisienne","issue":"30","page":"706",
  "issued":{"date-parts":[[2025,3,12]]},
  "URL":"https://www.pist.tn/jort/2025/2025F/Jo0302025.pdf",
  "note":"citation-key: loi-org2025-4\nJORT n° 30 du 13 mars 2025, FR p. 706, AR p. 775-776 (recid 196339). Dépôt le 13 mars 2025."},
 {"id":"decret2025-177","type":"legislation",
  "title":"Décret n° 2025-177 du 4 avril 2025, fixant l'organisation des travaux des conseils locaux, des conseils régionaux et des conseils des districts et leur mode de fonctionnement",
  "title-short":"Décret n° 2025-177 du 4 avril 2025",
  "container-title":"Journal officiel de la République tunisienne","issue":"41","page":"836",
  "issued":{"date-parts":[[2025,4,4]]},
  "URL":"https://www.pist.tn/jort/2025/2025F/Jo0412025.pdf",
  "note":"citation-key: decret2025-177\nJORT n° 41 du 5 avril 2025, FR p. 836 (recid 196570). Dépôt le 5 avril 2025."},
 {"id":"hammami-dafflon-gilbert-2021","type":"report",
  "title":"La répartition des compétences entre le niveau central et les collectivités locales : état des lieux et proposition d'une méthodologie opérationnelle",
  "author":[{"family":"Hammami","given":"Mokhtar"},{"family":"Dafflon","given":"Bernard"},{"family":"Gilbert","given":"Guy"}],
  "publisher":"Union européenne","publisher-place":"Tunis",
  "issued":{"date-parts":[[2021,12,1]]},
  "URL":"https://www.unifr.ch/ecopol/en/assets/public/Department/Prof%20em/Dafflon/2021_23.pdf",
  "note":"citation-key: hammami-dafflon-gilbert-2021\nPage de titre : « 1er décembre 2021 » ; « © Union européenne, 2021 » ; version préliminaire restituée à Tunis le 18 novembre 2021. Rapport du programme d'appui (PARD/PAPD-UE selon le manifeste local ; sigle non développé dans le document). Auto-archivage, Université de Fribourg. 103 p. PDF ; pagination imprimée."},
 {"id":"dafflon-gilbert-2016-dgcl","type":"report",
  "title":"Proposition pour un processus pratique de répartition des compétences entre le niveau central et les CTs",
  "author":[{"family":"Dafflon","given":"Bernard"},{"family":"Gilbert","given":"Guy"}],
  "genre":"Note à l'intention de la DGCL",
  "publisher-place":"Tunis et Sfax",
  "issued":{"date-parts":[[2016,5]]},
  "URL":"https://www.unifr.ch/ecopol/en/assets/public/Department/Prof%20em/2016_20_Proposition_pour_un_processus_pratique_de_repartition_des_competences_entre_le_niveau_central_et_les_CTS.pdf",
  "note":"citation-key: dafflon-gilbert-2016-dgcl\nEn-tête : « Note à l'intention de la DGCL selon la demande de la direction, M. M. Hammami » ; « Tunis et Sfax, 25 avril 2015, up-dated mai 2016 ». 12 p. Auto-archivage, Université de Fribourg."}
]
```

Entrées arabes : mêmes champs ; URL AR = `pdf_ar` de jort_cache (tableau d'en-tête) ;
`decretloi2023-9` AR : `https://www.pist.tn/jort/2023/2023A/Ja0242023.pdf`. Titres arabes : ceux
cités ci-dessus (§ 3.2, 4).

## 6. Points de date et de vigueur à reporter

### 6.1 Entrée en vigueur du code de 2018 (art. 383, p. 1759)

« تدخل أحكام هذا القانون الأساسي المتعلقة بكل صنف من أصناف الجماعات المحلية تدريجيا بعد الإعلان
عن النتائج النهائية للانتخابات الخاصة بكل صنف منها » ; les dispositions sur la préparation et
l'approbation du budget n'entrent en vigueur qu'au **1er janvier de l'année suivant la
proclamation des résultats définitifs** des élections de chaque catégorie. Jusqu'à l'entrée en
application du fonds de l'art. 38, l'État alloue à partir de l'exercice suivant les élections un
soutien annuel égal à celui de 2018, majoré d'un taux fixé par la loi de finances. La date de
proclamation des résultats définitifs des élections municipales de 2018 n'est pas établie ici
(fiche proposée § 7) : **c'est elle qui date l'application du code aux communes**. Les élections
régionales prévues par le code n'ont pas eu lieu sous ce régime, à ce que montrent les intitulés
lus ; la loi organique n° 2025-4 abroge ensuite le régime de la région (§ 4).

### 6.2 Chaîne des textes (pour le tableau du chapitre)

| Date d'effet | Texte | Objet |
|---|---|---|
| 22 mai 1975 (à confirmer) | loi n° 75-33 | loi organique des communes |
| 1er janvier 1976 | loi n° 75-37, art. 6 | CPSCL |
| 12 février 1989 (à confirmer) | loi organique n° 89-11 | conseils régionaux |
| 22 mai 2018 (exécutoire) ; application par catégorie, art. 383 | loi organique n° 2018-29 | code des collectivités locales |
| 14 mars 2023 | décret-loi n° 2023-9 | dissolution des conseils municipaux |
| 18 mars 2025 | loi organique n° 2025-4 | conseils locaux, régionaux, de districts ; abrogation du régime de la région et du district du code et de la loi n° 89-11 |
| 10 avril 2025 | décret n° 2025-177 | fonctionnement de ces conseils |

## 7. Lacunes et fiches RECHERCHE proposées

### 7.1 Ce qui n'est pas établi

1. Proclamation des résultats définitifs des élections municipales de 2018 (date d'application
   du code aux communes).
2. Loi prévue par l'art. 13, al. 2, du code (conditions d'exercice des compétences partagées) et
   lois de transfert de l'art. 16 : non identifiées.
3. Éditions arabes des lois n° 75-33 et 89-11 non lues ; fin du texte de 75-33 (p. 1059-1065) et
   de 89-11 (p. 220-221) non lue ; modificatifs de 75-33 (dont 2006-48) non lus.
4. Sort de la loi n° 75-33 après 2018 : abrogation non relevée dans les articles lus.
5. Texte de création du Centre de formation et d'appui à la décentralisation ; décret n° 2004-1182
   (couche texte décalée) non lu.
6. Textes de création des agences listées par Dafflon et Gilbert : non lus.
7. Décret-loi n° 2023-10 : non lu (note du chapitre 3).
8. Élections municipales après la dissolution de 2023 : aucun texte dans les intitulés.

### 7.2 Requêtes réellement lancées (jort_cache, 4 octobre 2026)

- `numero in ('75-33','75-35','75-36','75-37','89-11','2007-65','2006-48','95-68','2008-57','93-119','85-43','91-24','2018-29','2019-15','2025-4'…)`.
- `titre like` `%conseils municipaux%`, `%delegations speciales%`, `%conseils locaux%`,
  `%conseils regionaux%`, `%districts%`, `%المجالس البلدية%`, `%النيابات الخصوصية%`,
  `%المجالس المحلية%`, `%الأقاليم%`, `%collectivites locales%` (2011-2026, hors arrêtés et
  décisions).
- `date_signature >= '2023-03-09'` et `titre like '%municipal%' or '%البلدي%' or '%conseils municipaux%'`
  (hors arrêtés) : seuls deux articles de la loi de finances pour 2026.
- FTS `"conseils municipaux" OR "elections municipales" OR "المجالس البلدية" OR "الانتخابات البلدية"`
  depuis le 9 mars 2023 : aucun résultat.
- FTS `البلدية OR municipales`, signature entre le 1er mai et le 30 septembre 2018 : articles du
  code et décrets gouvernementaux n° 2018-744 et 2018-745 ; aucune décision de l'ISIE.
- FTS `"appui a la decentralisation"` : décret n° 2004-1182 seul texte d'organisation.

### 7.3 Fiches proposées (non versées dans `docs/recherches.yml`)

```yaml
- id: r-fl-elections-municipales-2018-resultats
  objet: décision de l'ISIE proclamant les résultats définitifs des élections municipales de 2018 (date d'application du code des collectivités locales aux communes, art. 383)
  ou: [precis/fr/finances_locales/_competences.qmd#sec-fl-comp-code-2018]
  requetes:
    titres_fts: ['البلدية OR municipales']
    titres_like: []
    iort_ar: [النتائج النهائية للانتخابات البلدية]
    plein_texte: [النتائج النهائية للانتخابات البلدية]
    depuis: 2018-05-06
  passes:
  - date: 2026-10-04
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés de jort_cache, signature du 1er mai au 30 septembre 2018 ; plein texte et iort non parcourus"
    couvert_jusqu_au: 2018-09-30
    resultat: aucun
  a_faire: [plein texte des JORT de mai à juillet 2018, édition arabe]

- id: r-fl-loi-competences-partagees
  objet: loi fixant les conditions et procédures d'exercice des compétences partagées (code des collectivités locales, art. 13, al. 2) ou loi de transfert de compétences (art. 16)
  ou: [precis/fr/finances_locales/_competences.qmd#sec-fl-comp-categories]
  requetes:
    titres_fts: ['"competences partagees"', '"transfert des competences"']
    titres_like: []
    iort_ar: [الصلاحيات المشتركة, نقل الصلاحيات]
    plein_texte: [الصلاحيات المشتركة]
    depuis: 2018-05-15
  passes: []
  a_faire: [lancer toutes les requêtes ; seules les requêtes sur conseils/collectivités du § 7.2 ont été faites]

- id: r-fl-elections-municipales-apres-2023
  objet: texte convoquant ou organisant l'élection de nouveaux conseils municipaux après le décret-loi n° 2023-9
  ou: [precis/fr/finances_locales/_competences.qmd#sec-fl-comp-depuis-2023]
  requetes:
    titres_fts: ['"conseils municipaux" OR "elections municipales" OR "المجالس البلدية" OR "الانتخابات البلدية"']
    titres_like: ['%municipal%', '%البلدي%', '%conseils municipaux%']
    iort_ar: []
    plein_texte: []
    depuis: 2023-03-09
  passes:
  - date: 2026-10-04
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés de jort_cache jusqu'au 18 septembre 2026, hors arrêtés ; plein texte non parcouru"
    couvert_jusqu_au: 2026-09-18
    resultat: aucun
```

La fiche `r-fl-loi-competences-partagees` n'a pas de passe : ses requêtes n'ont pas été lancées.
Ne la verser que si le rédacteur écrit le constat ; sinon, la tenir pour une tâche.

## 8. Plan proposé du chapitre

```
# Compétences et organisation {#sec-fl-competences}
  (rappel des notions : trois volets @sec-fl-trois-volets, libre administration
   @sec-fl-libre-administration, subsidiarité @sec-fl-subsidiarite, tutelle @sec-fl-tutelle)

## Avant le code de 2018 {#sec-fl-comp-avant-2018}
### La commune de la loi organique de 1975 {#sec-fl-comp-communes-1975}
    art. 1, 36 ; dissolution art. 12-13 ; nullité et approbation art. 38-46 (tutelle a priori)
### Le gouvernorat et son conseil régional {#sec-fl-comp-conseils-regionaux}
    loi 89-11 art. 1, 2, 3, 6, 9, 18-21 ; « double casquette » (Dafflon et Gilbert)

## Les compétences dans le code des collectivités locales {#sec-fl-comp-code-2018}
### Trois catégories et un principe {#sec-fl-comp-categories}
    art. 2-5, 11-18 ; propres / partagées / transférées ; subsidiarité art. 15 ;
    transfert par la loi avec les moyens, art. 16-17 ; pouvoir réglementaire art. 25-28 ;
    entrée en vigueur par catégorie, art. 383
### Les compétences de la commune {#sec-fl-comp-commune}
    art. 234-244, tableau à trois colonnes (propres, partagées, transférées)
### Les compétences de la région et du district {#sec-fl-comp-region-district}
    art. 293-298, 356-360
### Délégation ou dévolution ? {#sec-fl-comp-delegation-devolution}
    lecture de la doctrine : Hammami, Dafflon et Gilbert 2021 ; note DGCL 2016 ; AFD 2018 § 4.5

## L'organisation {#sec-fl-comp-organisation}
### Conseils, présidents, administrations {#sec-fl-comp-organes}
    art. 203-208, 256-257, 269-275
### Les instances nationales {#sec-fl-comp-instances}
    Conseil supérieur art. 47-60 ; Haute instance art. 61-65 ; progressivité art. 66-68 ;
    formation art. 43-44
### Le contrôle des actes {#sec-fl-comp-controle}
    art. 276-279, 346-349 (recours du gouverneur devant le juge) ; art. 197-199 en renvoi au
    chapitre des budgets
### Services, entreprises et agences {#sec-fl-comp-agences}
    art. 80-83, 103-104 ; CPSCL (loi 75-37, renvoi en prose au chapitre des transferts) ;
    agences nationales selon AFD 2018 § 4.4

## Depuis 2023 {#sec-fl-comp-depuis-2023}
### La dissolution des conseils municipaux {#sec-fl-comp-dissolution-2023}
    décret-loi 2023-9
### Conseils locaux, régionaux et de districts {#sec-fl-comp-conseils-2025}
    loi organique 2025-4 ; décret 2025-177 ; ce qui reste du code
```

Plan type « origines → institution → réformes → longue période » : la longue période (dépenses
par fonction) relève du chapitre 10 ; Hammami, Dafflon et Gilbert (2021, ch. 6, p. 92-99)
donnent des données de dépenses des communes et des régions 2010-2020 (non exploitées ici).

## 9. Notions mobilisées (ancres existantes)

- `_notions.qmd` : `sec-fl-trois-volets`, `sec-fl-libre-administration`, `sec-fl-subsidiarite`,
  `sec-fl-tutelle`, `sec-fl-budget-decentralise` (tâches dévolues/déléguées et leur financement).
- Glossaire : `g-decentralisation`, `g-deconcentration`, `g-delegation-competences`,
  `g-devolution-competences`, `g-collectivite-locale`, `g-libre-administration`,
  `g-subsidiarite`, `g-tutelle`.

## 10. Notions à glossaire (nouvelles)

| id proposé | FR | AR (attesté, code de 2018 sauf mention) | Source |
|---|---|---|---|
| `competences-propres` | compétences propres | الصلاحيات الذاتية | `loi-org-2018-29-ccl`, art. 13-14 ; FR : Hammami et al. 2021, p. 27 |
| `competences-partagees` | compétences partagées | الصلاحيات المشتركة | art. 13 |
| `competences-transferees` | compétences transférées | الصلاحيات المنقولة | art. 13, 16 |
| `conseil-superieur-collectivites-locales` | Conseil supérieur des collectivités locales | المجلس الأعلى للجماعات المحلية | art. 47-60 |
| `haute-instance-finances-locales` | Haute instance des finances locales | الهيئة العليا للمالية المحلية | art. 61-65 (déjà employée dans `_taxes_redevances.qmd` sans ancre) |
| `pouvoir-reglementaire-local` | pouvoir réglementaire local | السلطة الترتيبية | art. 25-28 |
| `district` | district | الإقليم | art. 2, 356 ; loi organique n° 2025-4 (« مجالس الأقاليم » / « conseils de districts ») |
| `conseil-local` | conseil local | المجلس المحلي | loi organique n° 2025-4, art. 1 (FR et AR) |

Statut : `provisoire` pour les trois catégories de compétences (FR = traduction doctrinale, pas de
texte français officiel) ; les deux dernières ont FR et AR officiels (`loi-org2025-4`). Avant
d'ajouter `district`, vérifier qu'aucune entrée voisine n'existe dans `precis/glossaire.yml`.
