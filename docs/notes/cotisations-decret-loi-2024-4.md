# Décret-loi n° 2024-4 du 22 octobre 2024 (travailleuses agricoles) : lecture pour le volume « Cotisations sociales »

Note du documentaliste, 23 octobre 2026. Objet : lever le TODO de
`precis/fr/cotisations_sociales/_regimes.qmd` (§ `#sec-cot-travailleuses-agricoles`) : « établir
sur le décret-loi n° 2024-4 le taux et l'assiette de la cotisation du régime des travailleuses
agricoles, et les dater ».

**Réponse courte : le décret-loi ne fixe ni taux ni assiette de cotisation**, pour aucun des deux
régimes qu'il crée (sécurité sociale, CNSS ; risques professionnels, CNAM). Il renvoie à des décrets
les modalités d'affiliation (art. 19 al. 3 et 22) et, pour les risques professionnels seulement,
« la base de calcul et le paiement des cotisations » (art. 41). Aucun de ces décrets n'est identifié
au *Journal officiel* jusqu'au 2 octobre 2026 (fiches de recherche au § 7).

## 1. Le fascicule : localisation, éditions, pages

| | Édition arabe (fait foi) | Édition française (« traduction française pour information ») |
|---|---|---|
| Fichier local | `~/projets/PDFs-legislation-tunisie/PDFs/JORT/2024/ar/Ja1292024.pdf` (6 p. PDF) | `~/projets/PDFs-legislation-tunisie/PDFs/JORT/2024/fr/Jo1292024.pdf` (7 p. PDF) |
| URL pist.tn | https://www.pist.tn/jort/2024/2024A/Ja1292024.pdf | https://www.pist.tn/jort/2024/2024F/Jo1292024.pdf |
| Numéro | JORT n° 129 du mercredi 23 octobre 2024 (20 rabia II 1446), 167e année | idem |
| Pages | 5293-5297 (sommaire p. 5292) | 2897-2902 |
| Couche texte | oui (formes de présentation arabes, à normaliser NFKC) | oui |
| Mention de dépôt | « تم إيداع هذا العدد … بمقر ولاية تونس العاصمة يوم 23 أكتوبر 2024 » | « déposé au siège du gouvernorat de Tunis le 23 octobre 2024 » |
| Signature électronique | Imprimerie officielle, 2024.10.23 15:41:21 +01'00' | PDF créé le 24 octobre 2024 (métadonnées) |

Deux voies de localisation : `jort_cache.db` (recid 188043, `Décret-Loi`, n° 2024-4, signé le
2024-10-22, publié le 2024-10-23, JORT n° 129, `pages` = « 5293-5293 », pagination arabe ; chemins
`/jort/2024/2024F/Jo1292024.pdf` et `/jort/2024/2024A/Ja1292024.pdf`) et `find` sur le corpus (les deux
fichiers ci-dessus, téléchargés le 24 septembre 2026). Le relevé `todo-localisation.md` qui classe le
texte « absent du corpus » est périmé.

**Correspondance articles / pages** (début de chaque page, relevé par `pdftotext -f N -l N` page par page) :

| Page FR | Articles | Page AR | Articles commençant sur la page |
|---|---|---|---|
| 2897 | art. 1er à 5 (début) | 5293 | art. 1er à 6 |
| 2898 | art. 5 (suite) à 12 (al. 1) | 5294 | art. 7 à 16 |
| 2899 | art. 12 (al. 2) à 19 (al. 1-2) | 5295 | art. 17 à 27 |
| 2900 | art. 19 (al. 3) à 32 (a-b) | 5296 | art. 28 à 37 |
| 2901 | art. 32 (c-e) à 38 | 5297 | art. 38 à 52 |
| 2902 | art. 39 à 52 | — | — |

Les dernières pages des deux éditions ne portent pas de folio dans la couche texte : **2902 et 5297
sont déduits de la suite des folios**, pas lus. La note `decret-loi2024-4` de `references.json`
place à tort « art. 45 à 52 » sur la dernière page : la p. 2902 porte les art. 39 à 52 (la p. 2901
s'arrête à l'art. 38). Elle donne aussi « Pp. 2897-2901 » en tête puis 2897-2902 en complément ;
le champ `page` (2897-2902) est juste.

## 2. Date d'effet

Le décret-loi ne contient aucune clause d'effet : l'art. 52 dit seulement « Le présent décret-loi
sera publié au Journal officiel de la République tunisienne » (p. 2902 ; AR p. 5297). Deux calculs :

- **Loi n° 93-64, art. 2** (règle écrite dans `AGENTS.md`, « Dater ») : cinq jours après le dépôt du
  23 octobre 2024, jour du dépôt non compté → **28 octobre 2024**. C'est la date qu'écrit aujourd'hui
  le précis.
- **Décret-loi n° 2020-1 du 14 avril 2020, art. 2** (`dl2020-1`, `precis/fr/marche_travail/references.json`,
  JORT n° 32 du 14 avril 2020, p. 767) : exécutoire « le lendemain de leur publication dans l'édition
  électronique » et de leur dépôt électronique → **24 octobre 2024**. La signature électronique de
  l'édition arabe (23 octobre 2024, 15 h 41) date la publication électronique du 23 octobre.

**Le propriétaire a tranché le 20 octobre 2026 pour le décret-loi n° 2020-1** pour tout texte publié
depuis le 14 avril 2020 (`docs/notes/backlog-precis.md`, § marché du travail : « depuis le 14 avril
2020, le lendemain de la publication électronique ; avant, la loi n° 93-64. Reste à l'écrire dans
`AGENTS.md` (« Dater ») et à reporter aux dates calculées depuis 2020 des autres volumes »). La règle
est déjà appliquée par la PR « Dates d'effet depuis le décret-loi n° 2020-1 : loi 2025-9, loi 2024-44,
arrêté de 2025 ; art. 117 du code du travail » (#482, fusionnée). **Conséquence : le décret-loi
n° 2024-4 est exécutoire le 24 octobre 2024**, et non le 28.

Endroits qui écrivent encore le 28 octobre 2024 (à corriger par le rédacteur, après confirmation) :

- `precis/fr/references.json`, note de `decret-loi2024-4` (« exécutoire le 28 octobre 2024 (loi n° 93-64, art. 2) ») ;
- `precis/glossaire.yml`, l. 4885 (définition de `regime-travailleuses-agricoles`), d'où `retraites/_glossaire.qmd` (engendré) ;
- `precis/fr/retraites/_secteur_prive.qmd`, l. 1582 ;
- `precis/fr/retraites/index.qmd`, l. 198 ;
- `precis/fr/prestations_sociales/_autres_risques.qmd`, l. 60 (`#r-ar-2024-4`) ;
- `precis/fr/prestations_sociales/_matrice.qmd`, l. 78 (liste des dates d'exécution) ;
- `docs/notes/backlog-precis.md`, l. 819 (« décret-loi n° 2024-4 (28 octobre 2024) ») et l. 1157.

Le volume « Cotisations sociales » n'écrit aucune date d'effet pour ce texte.

## 3. Contenu, article par article (édition française, contrôlée sur l'arabe aux points cités)

Titre et visas (p. 2897) : « Le Président de la République, Après délibération du Conseil des
ministres, Et après information de la commission de la santé, de la femme et de la famille, des
affaires sociales et des personnes handicapées à l'Assemblée des représentants du peuple ».
Cinquante-deux articles, quatre titres. Signé « Tunis, le 22 octobre 2024. Le Président de la
République Kaïs Saïed ». Aucun article n'abroge ni ne modifie un texte antérieur.

### Titre premier — Dispositions générales (p. 2897-2898)

- **Art. 1er** : crée « un régime spécifique de protection sociale des travailleuses agricoles »,
  visant l'inclusion économique et garantissant « les prestations d'assurance maladie, les pensions
  de vieillesse, d'invalidité et des survivants, de couverture contre les risques professionnels et
  les prestations du programme « Amen Social » ».
- **Art. 2** : définitions. *Travailleuse agricole* : « la femme travaillant dans le secteur agricole
  au sens de l'article 3 du code de travail, non-salariée exerçant, à titre principal, une activité
  professionnelle agricole pour son propre compte et la travailleuse agricole salariée travaillant
  chez un ou plusieurs employeurs » ; *inclusion économique* (AR الإدماج الاقتصادي) ; *exploitations
  agricoles familiales* (« qui n'emploient que leurs propriétaires et les membres de leurs familles ») ;
  *transport des travailleuses agricoles* (transport public routier non régulier de personnes, dans
  un ou plusieurs gouvernorats).
- **Art. 3** : les dépenses des programmes sont imputées sur le « Fonds de protection sociale des
  travailleuses agricoles ». **Al. 2 : « La travailleuse agricole est exemptée du paiement des
  cotisations pour le financement du dit Fonds dans les limites fixées par les dispositions du présent
  décret-loi »** (AR : « وتعفى العاملة الفلاحية من تحمل المساهمات في تمويل هذا الصندوق في الحدود
  المضبوطة بأحكام هذا المرسوم »). Le Fonds est nommé ici sans être créé : il l'est par la loi de
  finances pour 2025, art. 15 (§ 4).

### Titre II — L'inclusion économique (art. 4 à 16, p. 2897-2899)

Hors du champ des cotisations ; utile au volume « Marché du travail » (politiques de l'emploi).

- Art. 4 : accès aux mécanismes d'inclusion économique (travail salarié ou indépendant).
- Art. 5 : l'Agence nationale pour l'emploi et le travail indépendant organise études de faisabilité,
  accompagnement, formation ; le **Fonds national de l'emploi** prend en charge les dépenses de
  qualification, de formation et d'accompagnement.
- Art. 6 : indemnité mensuelle pendant la qualification, la formation ou le stage, sur le Fonds
  national de l'emploi ; **montant et modalités fixés par décret** ; non cumulable avec les transferts
  monétaires permanents de l'Amen social.
- Art. 7 : procédures préférentielles dans la formation professionnelle et l'emploi ; priorité aux
  programmes agricoles du développement régional.
- Art. 8 : financement de petites entreprises agricoles (exploitations familiales ou initiatives
  individuelles) sur le Fonds de protection sociale ; bénéficiaires : propriétaire ou détentrice
  légale de la terre, ou non-salariée agricole ; non-cumul avec des avantages similaires ; **décret**.
- Art. 9 : accès aux avantages et incitations à l'investissement agricole ; **décret**.
- Art. 10 : financement des projets par la **Banque tunisienne de solidarité**, convention avec les
  ministres des affaires sociales et des finances.
- Art. 11 : convention entre les ministres des affaires sociales, de l'emploi, des finances et de
  l'agriculture.
- Art. 12 : commission technique présidée par le ministre des affaires sociales ; missions et
  composition par **arrêté** ; rapport périodique au Chef du Gouvernement.
- Art. 13 : commission régionale de protection sociale des travailleuses agricoles dans chaque
  direction régionale des affaires sociales ; **arrêté**.
- Art. 14 : **registre national des travailleuses agricoles** auprès du ministère des affaires
  sociales (données démographiques, sanitaires, éducatives, sociales, économiques ; prestations Amen
  social et prestations des caisses) ; tenue fixée par **arrêté**.
- Art. 15 : système de paiement électronique géré par l'Office national des postes (convention).
- Art. 16 : plateforme de projets du ministère de l'agriculture.

### Titre III — La protection sociale (art. 17 à 35, p. 2899-2901)

**Chapitre premier, le régime de sécurité sociale des travailleuses agricoles** (intitulé AR : نظام
الضمان الاجتماعي للعاملات الفلاحيات).

- **Art. 17** (p. 2899 ; AR p. 5295) : régime spécifique « comportant l'octroi des prestations de
  l'assurance maladie et les pensions de vieillesse, d'invalidité et des survivants », pour :
  - « La travailleuse agricole non salariée exerçant à titre principal une activité professionnelle
    agricole pour son propre compte » ;
  - « La travailleuse agricole salariée, exerçant de manière régulière ou intermittente, chez un ou
    plusieurs employeurs pour une période de travail égale ou supérieure à 15 jours de travail par mois
    et avec une moyenne au moins égale à 45 jours par trimestre ou 180 jours par an, qu'elle soit
    employée de façon permanente ou saisonnière ou occasionnelle », sauf si elle est employée par une
    entreprise affiliée à un régime légal couvrant les mêmes risques pour tous ses employés.
- **Art. 18** : gestion confiée à la **CNSS**.
- **Art. 19** (non-salariées) : affiliation obligatoire à la CNSS « dans le mois qui suit la date de
  son assujettissement » ; exemptée : la bénéficiaire d'une pension de retraite d'un régime de
  sécurité sociale « et d'une pension d'invalidité » prévue par un régime légal ; **al. 3 (p. 2900) :
  « Les modalités, les conditions et les procédures d'affiliation sont fixées par décret »**.
- **Art. 20** (p. 2900) : « L'Etat prend en charge les cotisations à la charge des travailleuses
  agricoles au titre du régime de sécurité sociale des travailleuses agricoles non salariées durant les
  trois premières années à partir de la date du début de l'activité » (AR : « تتكفل الدولة بمعاليم
  الاشتراكات المحمولة على العاملات الفلاحيات … لمدة الثلاث سنوات الأولى من بداية النشاط »).
- **Art. 21** (salariées) : tout employeur, « dès le moment où elle engage une travailleuse agricole »,
  s'affilie à la CNSS dans le mois et la fait immatriculer.
- **Art. 22** : « Le montant de la cotisation est versé à la Caisse nationale de sécurité sociale. Les
  modalités, les conditions et les procédures d'affiliation au régime de sécurité sociale des
  travailleuses agricoles sont fixées par décret. » AR : « يدفع معلوم الاشتراك للصندوق الوطني للضمان
  الاجتماعي وتضبط بمقتضى أمر صيغ وشروط وإجراءات الانخراط بنظام الضمان الاجتماعي للعاملات الفلاحيات
  الأجيرات ». **Ni l'une ni l'autre édition ne renvoie le taux ou l'assiette au décret** : le texte
  arabe ne vise que les modalités d'affiliation des *salariées* (الأجيرات).
- **Art. 23** : « L'Etat prend en charge **la quote-part des cotisations à la charge des travailleuses
  agricoles** au titre du régime de sécurité sociale mentionné dans le présent décret-loi, durant les
  trois premières années à compter de la date du début de l'activité professionnelle. » AR : « معاليم
  الاشتراكات المحمولة على العاملات الفلاحيات ». Pour la salariée, **seule la part salariale** est prise
  en charge ; le texte ne dit rien de la part patronale, qui reste donc due.
- **Art. 24** : assurance maladie pour la travailleuse, le conjoint non divorcé sans couverture
  obligatoire propre, les enfants à charge.
- **Art. 25** : **indemnités et congés de maternité** « conformément aux dispositions de la
  législation en vigueur ».
- **Art. 26** : pension de vieillesse à **65 ans**, **120 mois** de cotisations effectives et validées,
  sans activité assujettie. **Art. 27** : dès **60 ans** avec 120 mois. **Art. 28** : allocation de
  vieillesse — **divergence d'éditions** : FR « inférieure à 60 mois », AR « إذا لم تتجاوز … 60
  شهرا » (n'excède pas 60 mois). L'arabe fait foi ; le précis suit déjà l'arabe (« ne dépasse pas »).
  La note `decret-loi2024-4` et `cnss-autres-regimes.md` § 10 disent « les deux éditions concordent »
  sur ce point : c'est inexact pour l'art. 28 (le seuil de 60 mois appartient à l'allocation en arabe,
  pas en français).
- **Art. 29-30** : invalidité non professionnelle réduisant d'au moins la moitié la capacité de
  travail ou de gain ; avant l'âge de la vieillesse ; 60 mois de cotisations effectives.
- **Art. 31-32** : conjoint survivant ; orphelins jusqu'à 16 ans, 21 ans (études secondaires ou
  techniques), 25 ans (études supérieures, sans bourse), sans limite pour la fille sans ressources et
  l'infirme.
- **Art. 33** : « Les taux, les modalités et les procédures de bénéfice » des pensions et de
  l'allocation sont **fixés par décret** (fiche `r-dl2024-4-art33`).

**Chapitre 2, prestations du programme « Amen Social »** (p. 2901).

- Art. 34 : transferts monétaires mensuels pour les travailleuses des catégories pauvres ; aide
  occasionnelle pour les catégories pauvres et à revenu limité.
- Art. 35 : soins dans les structures publiques ; **al. 2 : « Les prestations au titre du programme
  « Amen Social » ne peuvent être cumulées avec les prestations au titre de la couverture sociale. »**

### Titre IV — Transport et risques professionnels (art. 36 à 51, p. 2901-2902)

- Art. 36 : transport réservé aux travailleuses inscrites au registre, munies d'une carte délivrée par
  le commissariat régional au développement agricole.
- Art. 37 : le Fonds de protection sociale prend en charge un pourcentage des frais de transport
  « selon les besoins fixés par les gouverneurs » ; modalités, spécifications des véhicules et taux de
  prise en charge par **décret**.
- Art. 38 : définitions de l'accident du travail (y compris de trajet) et de la maladie
  professionnelle, pour la salariée **et la non-salariée** ; liste des maladies par arrêté conjoint
  santé / affaires sociales.
- **Art. 39** (p. 2902) : gestion du régime de réparation confiée à la **CNAM**.
- **Art. 40** : affiliation obligatoire de la non-salariée, et de tout employeur d'une salariée, qui
  doit la faire immatriculer.
- **Art. 41** : « Les conditions et les procédures d'affiliation et d'immatriculation ainsi que **la
  base de calcul et le paiement des cotisations** au titre du régime de réparation … sont fixés par
  décret. » AR : « شروط وإجراءات الانخراط والتسجيل ودفع الاشتراكات وقاعدتها ». Le taux n'est pas
  nommé.
- **Art. 42** : « L'Etat prend en charge les cotisations dues au titre du régime de réparation …
  durant les trois premières années à partir de la date du début de l'activité. Lesdites cotisations
  sont imputées sur le fonds de la protection sociale des travailleuses agricoles. » AR : « تتكفل
  الدولة … **بكامل** معاليم الاشتراكات المستوجبة … وتحمل على صندوق الحماية الاجتماعية للعاملات
  الفلاحيات ». L'arabe précise **la totalité** des cotisations (le français omet « entière »), et
  l'imputation est sur le Fonds, non sur le budget général.
- Art. 43-50 : soins, appareillage, indemnité journalière (jours ouvrables, repos et fériés
  confondus), rente d'incapacité permanente (taux et base par **décret**, art. 46), indemnité de décès
  égale à « un salaire d'un mois » (art. 47), rente de décès au conjoint (suspendue au remariage) et
  aux orphelins.
- Art. 51 : taux d'incapacité et indemnisation par **décret**. Art. 52 : publication.

### Récapitulatif pour le volume « Cotisations sociales »

| Élément | Régime de sécurité sociale (CNSS) | Risques professionnels (CNAM) |
|---|---|---|
| Affiliation obligatoire | art. 19 (non-salariée), art. 21 (employeur) | art. 40 |
| Taux | non fixé, non renvoyé expressément | non fixé, non nommé |
| Assiette | non fixée | « base de calcul » renvoyée à un décret (art. 41) |
| Décret d'affiliation | art. 19 al. 3, art. 22 | art. 41 |
| Prise en charge, 3 premières années depuis le début de l'activité | non-salariée : cotisations à sa charge (art. 20) ; salariée : sa quote-part seulement (art. 23) ; payeur : l'État | totalité des cotisations (art. 42, AR « بكامل »), imputée sur le Fonds |
| Branches financées | maladie, maternité (art. 24-25), vieillesse, invalidité, survivants (art. 17) | accidents du travail, maladies professionnelles |
| Prestations familiales | aucune | — |

## 4. Le Fonds de protection sociale des travailleuses agricoles (loi de finances pour 2025)

Loi n° 2024-48 du 9 décembre 2024 (`lf-2025`), JORT n° 149 du 10 décembre 2024, **art. 15, édition
arabe p. 6420**, lu en couche texte de `PDFs/JORT/2024/ar/Ja1492024.pdf` (l'édition française n'est
pas au corpus ; le précis cite p. 3421-3422 en français). Intitulé de rubrique : « إحداث صندوق الحماية
الاجتماعية للعاملات الفلاحيات وإقرار امتيازات جبائية لفائدتهن ». Le fonds assure la couverture sociale
et l'inclusion économique dans le cadre du décret-loi ; fonctionnement et interventions par décret ;
gestion CNSS (convention), programmes d'inclusion par la BTS. Ressources : subvention budgétaire
« في حدود 5 مليون دينار » ; taxe de 1 % des primes ou cotisations d'assurance de toutes branches
(versée mensuellement par les assureurs, non répercutable, déductible de l'assiette de l'IS) ; 5 dinars
par certificat de visite technique ; 10 % des amendes routières encaissées ; recettes de services des
organismes sous tutelle des affaires sociales (arrêté) ; dons. Art. 16 (p. 6420-6421) : exonération
d'impôt (art. 38, point 26, du code de l'IRPP et de l'IS) des revenus des bénéficiaires pendant 10 ans.

Le volume « Retraites » expose déjà tout cela (`_secteur_prive.qmd`, l. 1591-1603). Pour le volume
« Cotisations sociales », le point utile est l'articulation : **les cotisations de risques
professionnels prises en charge sont imputées sur ce Fonds (art. 42), celles du régime CNSS sont
mises à la charge de « l'État » (art. 20, 23)** sans que le décret-loi désigne le fonds. Le Fonds est
alimenté par des taxes affectées qui ne sont pas des cotisations sociales (famille « recettes
affectées », à ne pas mêler aux cotisations dans un tableau).

## 5. Ce que le volume « Cotisations sociales » dit déjà, et ce qui manque

Ce qu'il dit (`_regimes.qmd`, l. 238-244 ; `_bilan.qmd`, l. 209 ; `index.qmd`, l. 53) :

- l'institution du régime, sa gestion par la CNSS et son champ (art. 1, 17, 18) — exact ;
- « la prise en charge de ses cotisations par l'État pendant les trois premières années d'activité
  [@decret-loi2024-4, art. 20 et 23] » — **trop large** : pour la salariée, seule la quote-part de la
  travailleuse (art. 23) ; le point de départ est le début de l'activité (art. 20, 23, 42), non
  l'affiliation ni l'entrée en vigueur ;
- la création du Fonds par la LF 2025, art. 15 — exact ;
- « Le taux et l'assiette de la cotisation ne sont pas exposés ici » — à remplacer par le constat :
  le décret-loi ne les fixe pas, et le décret d'affiliation n'est pas identifié (ancre de recherche) ;
- matrice `tbl-matrice-branches` : « Travailleuses agricoles | oui | maladie | non | non ».
  À revoir : (a) la maternité est ouverte (art. 25), la case « Assurances sociales et maladie » peut
  dire « maladie et maternité » ; (b) le titre du tableau parle de « branches financées par le
  prélèvement », or aucun prélèvement n'est chiffré pour ce régime : les branches sont *couvertes*,
  leur financement par cotisation n'est pas établi.

Ce qui manque :

1. **La couverture des risques professionnels** et sa cotisation : rien dans `_accidents_travail.qmd`
   (`#sec-cot-at`) sur les art. 39-42 — affiliation obligatoire, y compris des non-salariées (premier
   texte qui le fait, selon `references.json`), assiette renvoyée à un décret, prise en charge totale
   pendant trois ans sur le Fonds. La matrice dit que la cotisation AT « ne suit pas le découpage des
   régimes » : ce régime fait exception (gestion CNAM, régime propre).
2. **L'exemption de l'art. 3 al. 2** (pas de contribution de la travailleuse au Fonds).
3. **La date d'effet** (§ 2), absente du volume.
4. **L'antécédent côté cotisations** (§ 6) : la travailleuse agricole relève depuis 2019 du régime
   des travailleurs à faibles revenus, cotisations à sa charge ; le volume l'expose (`_regimes.qmd`,
   l. 167, `@decret2019-379`) sans le relier au régime de 2024.
5. **Le non-cumul Amen social / couverture sociale** (art. 35 al. 2) relève du volume
   « Prestations sociales », qui le porte déjà (`_matrice.qmd`).

## 6. Antécédents et contexte

- **Décret gouvernemental n° 2019-379 du 22 avril 2019** (`decret2019-379`, JORT n° 34 du 26 avril
  2019, p. 1277-1278 ; exécutoire le 4 mai 2019 selon `cnss-autres-regimes.md` § 9.4) : ajoute à
  l'art. 2 du décret n° 2002-916 un paragraphe f) — « Les femmes récoltant les huîtres et les ouvriers
  saisonniers et mobiles appartenant au milieu rural et travaillant dans le secteur agricole y compris
  la femme employée dans ce secteur » (saisonniers : moins de 45 jours par trimestre chez un employeur)
  —, assiette et pension sur le SMAG, cotisations à leur charge (citation reprise de
  `cnss-autres-regimes.md` § 9.4, texte lu par un autre passage, non relu ici). Le seuil de 45 jours par
  trimestre de l'art. 17 du décret-loi est le même nombre, pris dans l'autre sens (« au moins égale
  à 45 jours par trimestre »). **Le décret-loi n'abroge ni ne modifie le décret n° 2019-379** et ne
  dit pas comment les deux régimes s'articulent (lacune, § 8).
- **Salariées agricoles relevant de la loi n° 81-6** (`loi81-6`) : l'art. 17 exclut seulement la
  travailleuse d'une entreprise affiliée à un régime couvrant les mêmes risques pour tous ses employés.
  Le rapport avec le régime des salariés agricoles n'est pas énoncé (lacune).
- **Transport (titre IV, chap. 1)** : loi n° 2019-51 du 11 juin 2019, « portant création d'une
  catégorie de « transport de travailleurs agricoles » » (JORT n° 48 du 14 juin 2019, p. 1707-1708, lu
  au corpus) : ajoute un art. 21 bis à la loi n° 2004-33 sur les transports terrestres (« service de
  transport public non régulier de personnes réservé aux travailleurs agricoles titulaires, saisonniers
  ou provisoires », tarif à la place selon la distance) ; décret d'application dans les trois mois
  (art. 4) : décret gouvernemental n° 2020-724 du 31 août 2020 (JORT n° 90 du 4 septembre 2020,
  p. 1920-1924, selon `jort_cache` ; non lu). La définition de l'art. 2 du décret-loi reprend celle de
  2019 en la réservant aux travailleuses.
- **Forme et procédure** : décret-loi du Président de la République, « après délibération du Conseil
  des ministres » et « après information » de la commission parlementaire compétente (visas, p. 2897).
  Pas d'exposé des motifs publié au JORT. Les motifs se lisent dans l'art. 1er : inclusion économique,
  conditions de vie des familles, « consacrer leur rôle entant qu'acteur économique ».
- **Mise en œuvre (presse, source secondaire)** : Mosaïque FM, 5 décembre 2025 (Sidi Bouzid) : un
  responsable de l'Association tunisienne du mouvement culturel déclare que l'exécution « تأخر لسنة
  كاملة في ظل غياب الأوامر التطبيقية والإجراءات التنفيذية المرتبطة به » (l'article écrit « عدد 4 لسنة
  2025 », coquille) ; Kapitalis, 15 février 2026 : décret-loi « دون تفعيل فعلي » plus d'un an après sa
  publication ; Nawaat, 27 août 2026 (cité dans `cnss-autres-regimes.md` § 10, non relu ici). À ne
  citer, le cas échéant, que comme presse ; le constat juridique repose sur la recherche au JORT (§ 7).

## 7. Recherches au *Journal officiel*

- **`r-dl2024-4-art33`** (décret de l'art. 33, pensions) : relancée le 23 octobre 2026 ; passe consignée
  dans `docs/recherches.yml` (résultat : aucun ; couvert jusqu'au 2 octobre 2026 ; jort_cache, miroir
  iort, plein texte FR/AR des n° 94-97 de 2026 ; lacune : n° 58 de 2026, absent du corpus).
- **Fiche nouvelle proposée : `r-dl2024-4-cotisations`** (non écrite au registre ; à créer avec l'ancre
  dans `_regimes.qmd` quand le rédacteur pose la réserve). Les termes de recherche sont ceux de la fiche
  de l'art. 33, qui ne dépendent pas de l'article : un décret d'application, quel que soit son objet,
  vise le décret-loi ou nomme les travailleuses agricoles.

```yaml
- id: r-dl2024-4-cotisations
  objet: décret fixant les modalités, conditions et procédures d'affiliation aux régimes du décret-loi n° 2024-4 (art. 19 et 22, CNSS) et la base de calcul et le paiement des cotisations de risques professionnels (art. 41, CNAM), ou tout texte fixant le taux ou l'assiette de leurs cotisations
  ou: [precis/fr/cotisations_sociales/_regimes.qmd#sec-cot-travailleuses-agricoles]
  requetes:
    titres_fts: ['"travailleuses agricoles"', 'travailleuses OR ouvrieres']
    titres_like: ['%travailleuses agricoles%', '%femmes rurales%']
    iort_ar: [العاملات الفلاحيات, عاملات الفلاحيات, الحماية الاجتماعية للعاملات]
    plein_texte: [2024-4, العاملات الفلاحيات, 4 لسنة 2024, عاملات الفلاحيات]
    depuis: 2024-10-23
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache, iort, corpus_local]
    couverture: 'jort_cache (dernière publication indexée le 2 octobre 2026) : FTS « travailleuses OR ouvrieres » depuis le 1er janvier 2024 et LIKE sur titres et objets (« travailleuses agricoles », « femmes rurales », « الفلاحيات », « الحماية الاجتماعية للعاملات ») depuis le 1er octobre 2024 : seuls le décret-loi n° 2024-4 et la loi n° 2024-48 (art. 15-16) ; miroir iort et plein texte des n° 94-97 de 2026 par la relance de r-dl2024-4-art33 (0 candidat). Pour la période antérieure au 19 septembre 2026, le plein texte FR/AR des fascicules de 2024 au n° 93 de 2026 a été parcouru avec les mêmes termes par les passes de r-dl2024-4-art33 des 23 et 24 septembre 2026 (autre passage). Lacune : n° 58 de 2026, absent du corpus et 404 sur pist.tn au 24 septembre 2026.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - 'lire le JORT n° 58 de 2026'
  - 'relancer après mise à jour de jort_cache au-delà du 2 octobre 2026'
```

- La fiche existante **`r-lf2025-art15-decret`** (décret de fonctionnement du Fonds) couvre le décret
  de la LF 2025, art. 15 ; non relancée ici.

## 8. Lacunes

- **Taux et assiette de cotisation** des deux régimes : non fixés par le décret-loi ; décrets
  d'application (art. 19, 22, 41) non identifiés au 2 octobre 2026. Rien à verser au modèle.
- **Date d'effet** : 24 octobre 2024 selon la règle tranchée le 20 octobre 2026, à reporter dans six
  fichiers (§ 2) ; `AGENTS.md` (« Dater ») ne porte pas encore la règle.
- **Articulation avec le décret n° 2019-379** (RTFR, femmes employées dans l'agriculture) et avec la
  loi n° 81-6 : aucun article ne la règle.
- **Travailleuses déjà actives avant 2024** : le point de départ des trois ans est « la date du début de
  l'activité » (art. 20, 23, 42) ; le texte ne dit pas comment il s'applique à une activité commencée
  avant l'entrée en vigueur. À ne pas trancher sans décret.
- **Divergence FR/AR de l'art. 28** (seuil de l'allocation de vieillesse) : corriger la phrase « les
  deux éditions concordent » dans la note de `decret-loi2024-4` et dans `cnss-autres-regimes.md` § 10.
- **Folios des dernières pages** (2902, 5297) déduits, non lus à l'image.
- **Décret gouvernemental n° 2020-724** (transport des travailleurs agricoles) : non lu.
- **Exposé des motifs** : aucun publié ; pas de rapport officiel préparatoire identifié.
- **Données** : effectifs affiliés, dépenses du Fonds (budget du ministère des affaires sociales,
  comptes spéciaux du Trésor) non recherchés ici.
- Aucun PDF d'étude n'est cité : rien à ranger dans `tunisia-data`. Les articles de presse ne sont pas
  archivés.

## 9. Références candidates (CSL-JSON)

Déjà présentes : `decret-loi2024-4` (`precis/fr/references.json`, l. 4986 ; absente de
`precis/fr/cotisations_sociales/references.json`), `lf-2025`, `decret2019-379`, `loi2002-32`,
`loi81-6` (`precis/fr/references.json`), `dl2020-1` (`precis/fr/marche_travail/references.json`).

Corrections proposées à la note de `decret-loi2024-4` : « exécutoire le 24 octobre 2024 (décret-loi
n° 2020-1, art. 2 ; dépôt et publication électronique le 23 octobre 2024) » ; « art. 39 à 52 sur la
dernière page (p. 2902, non foliotée) » ; « art. 28 : FR “inférieure à 60 mois”, AR “n'excède pas
60 mois” » ; « art. 23 : quote-part de la travailleuse seulement » ; « art. 42 : totalité des
cotisations AT/MP, imputées sur le Fonds » ; « art. 41 : base de calcul des cotisations AT/MP renvoyée
à un décret ; aucun article ne fixe de taux ». Pagination arabe : 5293-5297.

À créer (si le rédacteur cite les antécédents du transport) :

```json
{
  "id": "loi2019-51",
  "type": "legislation",
  "title": "Loi n° 2019-51 du 11 juin 2019, portant création d'une catégorie de « transport de travailleurs agricoles »",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "48",
  "page": "1707-1708",
  "issued": {"date-parts": [[2019, 6, 11]]},
  "URL": "https://www.pist.tn/jort/2019/2019F/Jo0482019.pdf",
  "note": "citation-key: loi2019-51\nJORT n° 48 du 14 juin 2019. Art. 1er : art. 21 bis ajouté à la loi n° 2004-33 (transport public non régulier réservé aux travailleurs agricoles). Art. 4 : décret gouvernemental dans les trois mois. Lu au corpus (Jo0482019.pdf). URL pist.tn à vérifier (HTTP)."
}
```

```json
{
  "id": "decret2020-724",
  "type": "legislation",
  "title": "Décret gouvernemental n° 2020-724 du 31 août 2020, fixant les conditions de l'exercice de l'activité de transport des travailleurs agricoles et les conditions du bénéfice de ce service",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "90",
  "page": "1920-1924",
  "issued": {"date-parts": [[2020, 8, 31]]},
  "URL": "https://www.pist.tn/jort/2020/2020F/Jo0902020.pdf",
  "note": "citation-key: decret2020-724\nJORT n° 90 du 4 septembre 2020 (métadonnées jort_cache ; jort_cache donne le numéro « 2000-724 »). Non lu. URL à vérifier (HTTP)."
}
```

## 10. Notions à glossaire

Présentes : `regime-travailleuses-agricoles` (définition à corriger pour la date), `amen-social`,
`cnss`, `cnam`, `regime-bas-revenus`, « Allocation de vieillesse » (l. 3255).

À créer (source canonique : décret-loi n° 2024-4, éd. arabe qui fait foi) :

| FR | AR | Source |
|---|---|---|
| Travailleuse agricole | العاملة الفلاحية | art. 2 (définition) |
| Fonds de protection sociale des travailleuses agricoles | صندوق الحماية الاجتماعية للعاملات الفلاحيات | décret-loi, art. 3 ; LF 2025, art. 15 (création, ressources) |
| Régime de protection sociale des travailleuses agricoles (intitulé du décret-loi, plus large que le régime de sécurité sociale) | نظام الحماية الاجتماعية للعاملات الفلاحيات | titre et art. 1er |
| Inclusion économique (traduction officielle ; l'arabe dit « intégration ») | الإدماج الاقتصادي | art. 2 |

« Registre national des travailleuses agricoles » et « transport des travailleuses agricoles » : utiles
au volume « Marché du travail » plutôt qu'à celui-ci ; non proposés.
