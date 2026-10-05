# Réforme fiscale tunisienne 2013-2014 : archivage et inventaire des documents du ministère

*4 octobre 2026. Archivage dans `~/projets/tunisia-data` ; rien n'a été committé ni poussé.*

## 1. Ce qui a été trouvé et archivé

**43 PDF** sont rangés dans `~/projets/tunisia-data/data/raw/minfinances/reforme_fiscale_2013_2014/`.
Le répertoire est ignoré par git : une entrée a été ajoutée au `.gitignore`, et `git check-ignore`
le confirme.

- **Fiche de source**, versionnable mais non committée :
  `~/projets/tunisia-data/sources/minfinances-reforme-fiscale-2013-2014.md`.
- **Manifeste**, versionnable : `~/projets/tunisia-data/sources/minfinances-reforme-fiscale-2013-2014-urls.csv`.
  Colonnes : fichier, titre, url_origine (adresse sur `www.finances.gov.tn`), url_recuperee (adresse du miroir, si le fichier vient de là), url_wayback, date_capture, mode, octets, sha256, pages.

Le processus a laissé ses documents à six étapes, auxquelles s'ajoutent des documents budgétaires.

| étape | fichiers |
|---|---|
| Lancement de la réforme, CNF élargi de juin 2013 | `2013-06_*` (6) |
| CNF du 29 août 2013 : synthèses des six groupes en arabe | `2013-08_cnf_*` (8, dont le programme) |
| CNF des 28-29 novembre 2013 | `2013-11_cnf_*` (10). Six synthèses finales, le **rapport de synthèse français (153 p.)**, le compte rendu arabe (135 p.) et l'allocution du ministre. La présentation générale du programme date aussi du 28/11/2013 |
| Consultation régionale du Kef, 17 juin 2014 | 1 |
| Journée de réflexion du 1er octobre 2014 | `2014-10_jr_*` (8). Exposés du MEF, du FMI (M. Mansour), de la Banque mondiale (J. Loeprick), de la GIZ (M. Steinich), de l'USAID/Pragma (J. Wooster) et de l'OECT |
| Assises nationales de la fiscalité, 12-13 novembre 2014 | `2014-11_anf_*` (4). **Projet de réforme du système fiscal tunisien** en français (123 p., deux exportations au texte identique) et en arabe (110 p.), plus le discours du ministre |
| Documents budgétaires et de simplification 2013-2014 | Rapport sur le projet de budget 2014 (ar), LFC 2014, LF 2015, trois dossiers de simplification MEF-IFC |

Provenance des fichiers :

- **29 viennent de la Wayback Machine**, par le préfixe `id_`. 27 viennent de `finances.gov.tn/images/`, capturés pour la plupart en juin 2017. Les 2 autres sont des captures du miroir faites en 2024-2025.
- **14 viennent du miroir encore en ligne `http://dev.finances.gov.tn/old/version2/`**, une copie de l'ancien portail. Il sert toujours les fichiers statiques, alors que ses `index.php` répondent 404.
- Sur ces 14, **13 ont été archivés dans la Wayback Machine** le 04/10/2026 avec *Save Page Now*. Leur horodatage est dans le manifeste. Les captures de deux d'entre eux ont été relues : leur SHA-256 est identique à celui des fichiers archivés.

Aucun fichier n'est un scan : tous ont une couche texte, donc **aucun OCR à prévoir**. En revanche, les diaporamas arabes exportés de PowerPoint donnent un texte extrait inversé ou mal encodé. Leurs chiffres ont été relevés **à l'image**.

Ajustements faits en cours de route :

- Deux fichiers ont été écartés après lecture. Les « conférences de presse » de 2012-2013 portaient sur les biens confisqués, pas sur la fiscalité.
- Un fichier a été renommé parce que son nom le datait mal : `2013-11_cnf_programme_reforme_fiscale_presentation_generale.pdf`.

## 2. Ce qui manque

- **`assises_fiscalite/pdf/3-Tunisia_Tax_incentives_Sept2014_final_(short).pdf`** (Banque mondiale) a été récupéré sur le miroir. *Save Page Now* l'a refusé deux fois, sans doute à cause des parenthèses dans l'URL : il n'a donc **pas d'URL Wayback**.
- Les autres fichiers liés depuis les pages de la réforme (portail id 77, 294, 425, 462, 617, 619 et `assises_fiscalite/documentation.html`) sont tous récupérés.
- **Pas trouvé :**
  - les deux études FMI de 2012 qui ont servi de diagnostic, l'une sur le système fiscal et l'autre sur l'administration. La page arabe id 294 les cite, sans lien ;
  - un « livre blanc » sous ce titre ;
  - les supports des autres consultations régionales, puisque seul celui du Kef est lié ;
  - les annexes de `rf_2` (1-3) et de la fiscalité locale de novembre 2013 (1-2), annoncées mais absentes des PDF.
- **Non pris parce que hors sujet :** catégories jdownloads (budgets, dette), audio `mosaique_-reforme.mp3`, LF 2014 et budget citoyen 2014.

## 3. Chiffres utiles au précis, par priorité

Ce sont d'abord des diagnostics de 2013. Un chiffre ne se cite qu'avec son document et sa page, et plusieurs n'ont pas d'année explicite.

### 3.1 Régime forfaitaire

Le document clé est **`2013-08_cnf_presentation_revision_regime_forfaitaire.pdf`**, CNF d'août 2013, 34 p., en arabe. Pagination PDF :

| | 2009 | 2010 | 2011 |
|---|---|---|---|
| Inscrits au fichier (p. 5) | 348 581 | 363 390 | 377 045 |
| En règle (déclarants) | 232 504 (67 %) | 216 526 (60 %) | 181 337 (48 %) |
| Défaillants | 116 077 | 146 864 | 195 708 |
| Contribution (MD) | 25,181 | 22,616 | 14,969 |
| Contribution moyenne (D) | 108,3 | 104,5 | 82,5 |

Autres pages du même document :

- **p. 4** :
  - 300 000 inscrits en 2004, 394 000 à fin juin 2013 (+31,3 %) ;
  - 60 % du fichier et 80 % des personnes physiques BIC ;
  - dépôt des déclarations : 40 % dans les délais, 50 % en fin d'année ;
  - contribution de 14 MD en 2004, puis 23 MD en 2012 (+64 %), soit **0,2 % des recettes du régime intérieur** ;
  - contrôle : 45 000 interventions par an, pour environ 12 MD ;
  - le texte avance « 30 MD en 2010 », ce qui contredit les 22,616 du graphique.
- **p. 7** : **nombre de déclarations par tranche de chiffre d'affaires** (11 tranches, de [0-3 000] à [30 000-100 000] D), 2009-2011. Par exemple en 2010 : 131 143 ; 47 352 ; 19 220 ; 8 572 ; 3 370 ; 1 688 ; 837 ; 350 ; 195 ; 199 ; 3 600.
- **p. 8** : **contribution par tranche**, en milliers de dinars. La tranche [30 000-100 000] porte 24 % de la contribution en 2009-2010 et 10 % en 2011. Deux valeurs sont masquées sur la diapositive.
- **p. 11** : en 2010, 61 % des déclarations sont sous 3 000 D de chiffre d'affaires et 82 % sous 6 000 D.
- **p. 6 et p. 33** : répartition par secteur en 2010.
  - Effectifs : services 52 %, commerce de détail 43 %, transformation 4 %, artisanat 1 %.
  - Contribution, en milliers de dinars : services 12 565,1 (56 %), commerce de détail 8 141,1 (36 %), industrie 1 683,5 (7 %), artisanat 226,4 (1 %).
  - Les sous-activités de la p. 33 (cafés 19 %, taxis 14 %, alimentation générale 49 %…) sont à vérifier sur le PDF.
- **p. 10** : ancienneté, en part des inscrits et part de la contribution, de « moins de 8 ans » (32 % / 24 %) à « plus de 33 ans ».
- **p. 16** : **comparaison avec le régime réel**. Pour 36 activités exercées par 80 % des forfaitaires, la contribution moyenne est de **98 D, contre 522 D** pour les contribuables au réel à l'IR.
- **p. 19 et p. 34** : le transport, c'est 21 % des forfaitaires et 20 % de la contribution. Contribution moyenne : marchandises 58 D, taxi 99 D, louage 125 D, transport rural 72 D. 66 % des anciens forfaitaires optionnels réduisent leur chiffre d'affaires, mais le sens de ce chiffre est ambigu.
- **p. 31** : amendes de 100 D (pas de livre de recettes) et de 25 D (pas de déclaration d'existence).
- `2013-08_cnf_rf_4_ar.pdf` est le **même diaporama**, avec les pages 15 à 19 permutées.

**`2013-06_ar_waqi.pdf`** (« L'administration fiscale : état des lieux et perspectives », juin 2013) :

- **p. 10**, vérifié à l'image : 644 248 contribuables, dont 1 600 personnes morales à la DGE. Personnes morales 16,96 %, personnes physiques 83,04 %. Ces dernières se répartissent en forfaitaires 61,31 %, réel 15,16 % et BNC 6,57 % (en part du total).
- **p. 11** : **394 976 forfaitaires**, dont 52 % dans les services (transport 40 %) et 43 % dans le commerce de détail (alimentaire 55 %).
- **p. 12**, vérifié à l'image : le forfait rapporte **23,4 MD, soit 0,21 %** (« 0,2 % » dans le texte) des recettes fiscales du régime intérieur (10,9 Md D). La même page donne la structure de ces recettes : personnes morales 26,80 %, salariés 24,01 %, réel 4,78 %, impôts indirects 44,19 %. Année non dite.

**`2013-06_presentation_systeme_fiscal.pdf`** :

- **p. 14-15** : barème du forfait en mai 2013. Vérifié à l'image.
  - Plafonds de chiffre d'affaires : 100 000 D (achat pour la revente, transformation, consommation sur place), 50 000 D (services).
  - Taux : 2 % (achat pour la revente, transformation) ou 2,5 % (autres activités) du chiffre d'affaires.
  - Minimum : 50 D hors zones communales, 100 D ailleurs.
- **p. 35** : « environ 395 000 » forfaitaires pour 23,5 MD, « soit 0,2 % de l'ensemble des ressources fiscales ». Vérifié à l'image.

**`2013-11_cnf_presentation_regime_forfaitaire.pdf`** (synthèse finale, novembre 2013) :

- **p. 4** : environ 400 000 forfaitaires, soit 60 % du fichier et 80 % des personnes physiques BIC ; environ 70 % ont au moins 8 ans d'ancienneté.
- **p. 5** : 31 % des déclarations portent un chiffre d'affaires inférieur à 3 000 D et paient l'impôt minimum.
- **p. 10** : 45 000 contrôles pour 12 MD.
- **p. 11** : 21 % des forfaitaires sont dans le transport.
- Les mesures proposées ne sont pas chiffrées : leur « incidence sur les recettes » est marquée « non mesurée ».

**Rapport de synthèse français (CNF, novembre 2013) et projet des Assises (novembre 2014)** :

- 60 % des inscrits pour 0,2 % des recettes, 45 000 contrôles pour 12 MD : rapport de synthèse p. 10, projet des Assises p. 10.
- Forfait d'assiette des BNC : 3 % de l'IRPP, choisi par 60 % des BNC ; bénéfice fixé à 70 % des recettes. Projet des Assises p. 8 et p. 24.
- La version arabe des Assises donne 2,6 % de l'IRPP en 2013 et 4,1 % en 2014.
- Projet des Assises :
  - 68 activités exclues par la LF 2014 (p. 65) ;
  - minimum des forfaitaires relevé de 50 % (p. 66) ;
  - majoration de 50 % en cas de retard (p. 67) ;
  - LFC 2014 : minimum de 1 000 ou 2 000 D, ou 15 % des dépôts bancaires (p. 68) ;
  - abattement des BNC ramené de 30 % à 20 %, pour **+6,7 MD** (p. 52-53 ; aussi CNF impôts directs p. 7-8).
- **LF 2015 (présentation)** :
  - décret n° 2939 du 1er août 2014 (numéro et date tels que les donne la présentation), qui exclut certaines activités du forfait à partir de 2015 ;
  - comptabilité simplifiée pour les BNC jusqu'à 150 000 D de chiffre d'affaires ;
  - LFC 2014 : déduction dégressive de 75, 50 puis 25 % du bénéfice pour qui passe au réel.

### 3.2 IRPP

- **`rf_1` (août 2013)** :
  - 83 % des redevables sont des personnes physiques et 17 % des personnes morales (p. 3) ;
  - les impôts directs font 43 % des recettes fiscales, partagés en IR 52 % et IS 48 % (p. 4) ;
  - l'IR vient des salariés pour 81 %, des BNC pour 3 %, des revenus fonciers pour 1 % et d'autres revenus pour 15 % (p. 5).
- **`presentation_systeme_fiscal` p. 13**, vérifié à l'image : barème de 2013. 0 % jusqu'à 1 500 D, 15 % jusqu'à 5 000 D, 20 % jusqu'à 10 000 D, 25 % jusqu'à 20 000 D, 30 % jusqu'à 50 000 D, 35 % au-delà. Pour les BIC et les BNC, l'impôt est d'au moins 0,1 % du chiffre d'affaires brut, avec un minimum de 200 D. La p. 35 ajoute : salariés 80 % de l'IR, BNC 3 %.
- **Impact chiffré des variantes**, en MD (rapport de synthèse p. 50-63, CNF impôts directs p. 17, Assises p. 52) :
  - charges de famille : −20,1 / −27 ;
  - frais professionnels à 12 % : −73,3 ; dégressif : −66 ; avec plafond de 4 000 D : −56,7 ;
  - première tranche portée à 2 000 D : −113,2 ;
  - déduction de 1 000 D jusqu'à 5 000 D de revenu : −35,1 ; variante : −19,2 ;
  - tranche exonérée indexée sur le SMIG : −410.

### 3.3 IS

- **`presentation_louati`** : 54 731 sociétés, 34 185 sociétés payantes, 5,8 Md D d'assiette brute, 3,5 Md D d'exonérations. Année non dite.
- **`rf_1` p. 5** : 80 % de l'IS est payé par les sociétés à 35 %, qui sont 5 % des sociétés.
- **`rf_3` p. 4-5** : les grandes entreprises font 70 % des recettes fiscales ; 450 vérifications pour 9 610 entreprises de plus de 1 MDT de chiffre d'affaires.
- **Impacts**, en MD :
  - taux de 25 % avec dividendes taxés : −116,3 ; taux de 20 % : −221,6 ;
  - avec un minimum de 0,2 % du chiffre d'affaires : −101,4 / −206,5 ;
  - exonérés à 10 % : +85,4 ; export à 10 % : +137 ; extension du taux de 35 % : +3.
- **Banque mondiale** (Journée d'octobre 2014) : coût fiscal net des incitations de 1 115, 1 304 et 1 158 MD en 2009-2011 (2,2 % du PIB en 2009) ; 90 % concentrés sur environ 2 500 entreprises sur 24 000.

### 3.4 TVA

- **`rf_2` p. 10** : rendement par taux, en MD.

  | Taux | 2009 | 2010 |
  |---|---|---|
  | 6 % | 58 | 56,9 |
  | 12 % | 622,5 | 609,4 |
  | 18 % | 2 686,3 | 3 086 |
  | Total | 3 373,5 | 3 749,8 |

- **`rf_2`, autres chiffres** :
  - majoration de 25 % : 26,8 / 28,2 / 28,5 MD en 2009-2011 ;
  - crédit de TVA : 1 415 / 1 502 / 1 694 MD en 2010-2012 ;
  - remboursements demandés, puis accordés : 375,8 puis 320,8 en 2010 ; 359,2 puis 301,2 en 2011 ; 203,3 puis 179,2 en 2012 ;
  - retenue à la source de 50 % : 387,2 / 352,1 / 305,5 MD en 2010-2012.
- **Impôts indirects (CNF novembre) p. 12 et Assises p. 77** : retenue à la source de 298,9 MD en 2012. Simulations à 30, 25 et 20 % : 179,3 / 149 / 119,5. La valeur de 149 semble incohérente.
- Proposition : un taux réduit unique de 8 à 10 % à la place de 6 % et 12 %.

### 3.5 Recettes, administration, fiscalité locale

- **LF 2015, présentation p. 99-106** :
  - recettes par impôt de 2010 à 2015 (IRPP, IS pétrolier et non pétrolier, douane, TVA, droit de consommation), plus les parts des impôts directs et de la douane de 1990 à 2015 ;
  - pression fiscale de 22,2 % en 2015 ;
  - recettes 2014 actualisées à 18 733 MD.
- **Rapport sur le budget 2014 p. 12-16** : mêmes rubriques pour 2012-2014, avec le droit de consommation par produit ; pression fiscale de 21 %.
- **Taux de dépôt des déclarations annuelles** (CNF novembre « transparence » p. 7, `rf_6` p. 11) : dans les délais, 51,2 / 40,5 / 36,6 % en 2009-2011. Le détail par catégorie (personnes morales, BNC) est donné aussi.
- **Fiscalité locale (`rf_5`)** : rendements 2010-2012 en MD.
  - Taxe sur les immeubles bâtis : 40 / 21 / 30.
  - Taxe sur les entreprises (TCL) : 111 / 93 / 137.
  - Marchés : 62 / 36 / 44.
  - Les exposés MEF et OECT d'octobre 2014 donnent aussi les ressources locales de 2007 à 2013.

## 4. Inventaire détaillé par document

Ci-dessous, les inventaires de lecture, page par page. Le fichier de la section C appelé `2013-06_programme_reforme_fiscale_presentation_generale.pdf` s'appelle désormais `2013-11_cnf_programme_…`. Les deux fichiers « conférence de presse » de la section H ont été supprimés de la collection.


---

### Inventaire C — lancement de la réforme fiscale, 2013-06 (7 fichiers)

Lecture : les diaporamas arabes `ar_waqi` ont été lus visuellement (pages 4-26) ; pour `presentation_systeme_fiscal`, `ar_manhajiyat`, `programme_reforme…` le texte extrait a été normalisé en Unicode NFKC (les formes de présentation arabes deviennent lisibles, ordre logique correct) et relu ; ces trois diaporamas ne contiennent ni tableau ni graphique chiffré (texte seul). `presentation_louati` lue visuellement. Aucun fichier n'est un scan sans texte : tous ont une couche texte (pour les fichiers arabes, couche texte en formes de présentation, exploitable après NFKC). Aucun OCR nécessaire.

#### 2013-06_ar_waqi.pdf

- Titre (p. 1) : « إدارة الجباية : الواقع والآفاق » — L'administration fiscale : état des lieux et perspectives. En-tête : الجمهورية التونسية، وزارة المالية. Date : 2013-05-13 (inscrite p. 1 ; PDF créé le 13 mai 2013).
- Auteur : ministère des Finances (aucune direction nommée). 26 pages, arabe, diaporama PowerPoint. Plan : Partie 1 « diagnostic de la performance et de l'organisation des services fiscaux » (axe 1 organisation et moyens, axe 2 performance) ; Partie 2 « perspectives et voies de modernisation » (axe 1 « début de la réforme », axe 2 « vision des réformes futures »). p. 26 : « merci ».
- Les chiffres du régime forfaitaire sont aux pp. 11 et 12.

### Chiffres, par page

- p. 4 : organigramme (ministre ; Direction générale des impôts au centre ; DG des études et de la législation fiscales ; DG des avantages fiscaux et financiers ; DG de la comptabilité publique et du recouvrement ; DG des douanes ; École nationale des finances ; Centre informatique du ministère ; Direction des affaires administratives et financières). Aucun chiffre.
- p. 5 : effectif des cadres et agents du contrôle : 3 400 (hors ouvriers) ; 48 % affectés aux opérations de contrôle, 52 % à d'autres tâches ; 366 000 attestations délivrées (« administration de services »).
- p. 6 : effectif des cadres et agents du recouvrement : 4 500 (hors ouvriers) ; 69 % affectés aux opérations de recouvrement, 31 % à d'autres tâches ; répartis sur 25 trésoreries régionales (أمانة مال جهوية) et 241 recettes des finances. Les sommes versées par 633 000 contribuables représentent environ 17 % des sommes recouvrées via le système « Rafik ».
- p. 7 : moyens matériels : une voiture pour 16 agents ; un ordinateur pour 3 agents. Crédits (millions de dinars) :

| nature | 2010 | 2011 | 2012 |
|---|---|---|---|
| crédits de rémunération (التأجير) | 43,1 | 54,8 | 69,7 |
| crédits de fonctionnement (التسيير) | 5,1 | 6,3 | 6,2 |
| crédits de développement (التنمية) | 2,5 | 1,4 | 3,0 |

  Mention : dans les pays européens, la rémunération représente environ 50 % du total des crédits.
- p. 8 : schéma des applications informatiques (Rafik, Sadek, gestion électronique des documents, correction des erreurs sur contrats et écrits enregistrés aux recettes des finances, aide à la décision, Sanad, déclaration à distance, base documentaire, correspondance électronique, aide à l'élaboration du programme de vérification). Aucun chiffre.
- p. 10 : « le nombre de contribuables (المطالبون بالأداء) s'est élevé à 644 248 » (annotation : dont 1 600 personnes morales inscrites à la DGE). Répartition (histogramme, % de 644 248) :
  - personnes morales 16,96 % ; personnes physiques 83,04 % ;
  - parmi les personnes physiques : commerçants, industriels, prestataires de services et artisans au régime réel 15,16 % ; au régime forfaitaire (نظام تقديري) 61,31 % ; professions non commerciales 6,57 %. (15,16 + 61,31 + 6,57 = 83,04.)
  - Annotation : « mieux maîtriser l'assiette et fournir l'information fiscale ».
  - Le chiffre de 61,31 % est entouré d'un cercle rouge. 61,31 % x 644 248 = environ 395 000 (recoupe p. 11).
- **p. 11 : « répartition des assujettis sous le régime forfaitaire » (توزيع المنضوين تحت النظام التقديري) : total 394 976.** Sous-répartition (pourcentages du total) : prestataires de services 52 % ; commerce de détail 43 % (les 5 % restants ne sont pas détaillés sur la page).
  - Services (52 %) : transport de personnes et de marchandises 40 % ; autres services 60 %, dont, « principalement » : coiffure 10 %, restauration légère et cafés 20 %, mécanique générale 10 %.
  - Commerce de détail (43 %) : produits alimentaires 55 % ; autres produits 45 %.
- **p. 12 : « contribution aux recettes fiscales (régime interne) » (graphique en secteurs) : les recettes fiscales du régime interne sont estimées à 10,9 milliers de millions de dinars (« 10,9 ألف م د », soit 10,9 milliards de dinars). Répartition : personnes morales 26,80 % ; salariés (أجراء) 24,01 % ; régime réel 4,78 % ; régime forfaitaire 0,21 % ; contributions au titre des impôts indirects 44,19 %** (total 100,00 %). Annotation : la contribution des forfaitaires s'est élevée à **23,4 millions de dinars, soit 0,2 % du total des recettes fiscales du régime interne** (année non indiquée sur la page ; le diaporama est de mai 2013).
- p. 13 : remboursement des excédents d'impôt : 400 millions de dinars remboursés chaque année, dont 70 % au titre de la TVA ; 30 % des vérifications fiscales portent sur des dossiers programmés à la suite d'une demande de remboursement d'excédent ; difficulté : « manque de maîtrise de l'élaboration du programme de vérification ».
- p. 14 : interventions du contrôle : 5 500 vérifications fiscales ; 70 000 mises en demeure de régulariser les omissions (تنبيه لتسوية الإغفالات) ; « elles ont le même rendement » (annotation).
- p. 15 : taux de dépôt des déclarations annuelles : dans les délais légaux 40 % ; à fin d'année (après intervention des services de contrôle) 57 %. Pour les principaux contribuables, taux de dépôt annuel supérieur à 90 % (40 000 contribuables, soit environ 96 % de la contribution totale des assujettis au régime réel ; environ 700 000 déclarations déposées par eux). Total des déclarations déposées : 2 millions. Note : hausse du nombre de déclarations « négatives » (environ 30 000 par mois) au titre de la TVA, dont la cause serait : gonflement des archives, étroitesse des bureaux de contrôle, hausse du coût de l'impôt.
- p. 18 : centre de conseil fiscal à distance : instauré par l'ordonnance (أمر) n° 2856 du 7 octobre 2011, opérationnel depuis mars 2012 ; 81 100 400 (numéro d'appel affiché) ; réalisations jusqu'à fin décembre 2012 : 1 528 appels traités ; base documentaire de 250 fiches portant sur 165 sujets fiscaux.
- p. 19 : déclaration et paiement à distance : institués par l'article 57 de la loi de finances 2001 ; adhésion obligatoire par l'article 70 de la loi de finances 2005 pour les entreprises dépassant un chiffre d'affaires annuel brut fixé par arrêté du ministre des Finances (seuil : 2005 : 15 M.D ; 2006 : 10 M.D ; 2007 : 5 M.D ; 2008 : 2 M.D ; 2012 : 1 M.D) ; adhésion facultative pour les entreprises non soumises et pour les personnes physiques sans identifiant fiscal. Inscrits : de 1 075 (2007) à 11 953 (2012). Déclarants : de 616 (2007) à 6 485 (2012) (72 %). Sommes recouvrées : environ 83 % du total des sommes recouvrées via le système Rafik, contre 55 % en 2007.
- p. 20 : autres moyens de recouvrement : paiement à distance, avec versement des sommes dues à n'importe quelle recette des finances : environ 15 000 déclarations liquidées ; recettes des finances toutes informatisées ; sur 241 recettes, 47 équipées de terminaux de paiement (TPE), utilisés dans 2 326 opérations de recouvrement en 2012.
- p. 21 : dépôt de la déclaration de l'employeur sur support magnétique : même condition de seuil de chiffre d'affaires (2005 : 15 M.D, 2006 : 10 M.D, 2007 : 5 M.D, 2008 : 2 M.D, 2012 : 1 M.D) ; déclarants : 7 500 sur 11 000 assujettis (66 %) ; ce service a permis d'enrichir la banque d'informations de 1,5 million de bénéficiaires (salaires, honoraires, commissions, revenus de capitaux mobiliers, plus-values).
- pp. 23-25 : perspectives (texte, sans chiffre) : sensibilisation et culture fiscale ; classer les contribuables selon des critères objectifs (taille, risques fiscaux) ; accueil ; services en ligne ; simplification ; encadrement et rationalisation du contrôle ; mécanismes de prévention du contentieux fiscal ; valorisation du recouvrement ; enrichissement de la banque de données ; lutte contre la fraude (opérations entre résidents, avec non-résidents) ; formation des agents.

#### 2013-06_presentation_systeme_fiscal.pdf

- Titre (p. 1) : « النظام الجبائي التونسي: النقائص وأهداف الإصلاح » — Le système fiscal tunisien : lacunes et objectifs de la réforme. Date : mai 2013 (pied de page 13/05/2013). Auteur : ministère des Finances (non nommé). 42 pages (la p. 42 est vide, la numérotation affichée va jusqu'à 42), arabe, diaporama, texte seul, sans graphique.

### Barèmes et taux décrits (état du droit présenté, mai 2013)

- p. 3 : codes : TVA (1988) ; IRPP et IS (1990) ; droits d'enregistrement et de timbre (1993) ; encouragement des investissements (1993) ; fiscalité locale (1997) ; droits et procédures fiscaux (2000).
- p. 4 : en 2007, réduction de l'IS de 35 % à 30 % ; suppression du taux élevé de TVA (29 %).
- p. 11 : détermination du revenu : pour les bénéfices d'entreprise, bénéfice net d'après la comptabilité retraitée ; pour les autres catégories, revenu net sur une base forfaitaire de **90 % pour les salariés** et **70 % pour les professions libérales et revenus fonciers** (déductions de 10 % et 30 %).
- p. 13 : barème de l'IRPP (dinars, revenu imposable) :

| tranche | taux |
|---|---|
| 0 – 1 500 | 0 % |
| 1 500,001 – 5 000 | 15 % |
| 5 000,001 – 10 000 | 20 % |
| 10 000,001 – 20 000 | 25 % |
| 20 000,001 – 50 000 | 30 % |
| au-delà de 50 000 | 35 % |

  Minimum d'impôt pour bénéfices commerciaux et professions non commerciales : 0,1 % du chiffre d'affaires brut (ou des revenus bruts) hors exportation, avec un minimum de 200 dinars.
- **p. 14 : régime forfaitaire (النظام التقديري)** : entreprises individuelles aux bénéfices industriels et commerciaux, « selon des conditions déterminées », dont le chiffre d'affaires annuel ne dépasse pas : **100 000 D** pour les activités d'achat pour la revente, de transformation et de consommation sur place ; **50 000 D** pour les activités de services.
- **p. 15 : impôt forfaitaire = pourcentage du chiffre d'affaires annuel : 2 % pour l'achat-revente et la transformation ; 2,5 % pour les autres activités ; impôt minimal : 50 D pour les entreprises établies hors des zones communales, 100 D pour celles établies dans les autres zones.**
- p. 19 : taux de l'IS : général 30 % ; réduit 10 % (artisanat, agriculture et pêche) ; spécial 35 % (secteur financier, télécommunications, assurance, hydrocarbures en production-raffinage-transport-distribution en gros…).
- p. 20 : minimum d'IS : 0,1 % du chiffre d'affaires hors exportation, sans pouvoir être inférieur à 200 D pour les personnes morales à 10 % et à 350 D pour celles à 35 % ou 30 %.
- p. 21 : modes de paiement : retenue à la source (honoraires, commissions, loyers, revenus de capitaux mobiliers, redevances, salaires, jetons de présence) à 15 % - 20 % ; 3 acomptes provisionnels de 30 % chacun de l'impôt de l'année précédente (sociétés, commerçants, industriels, professions non commerciales) ; avance de 10 % à l'importation sur une liste de produits de consommation ; avance de 25 % sur les bénéfices des sociétés de personnes ; régularisation annuelle.
- p. 23 : champ de la TVA : importation ; production industrielle, artisanale et services ; professions libérales ; commerce de gros hors produits alimentaires ; commerce de détail pour les commerçants dont le chiffre d'affaires annuel total est égal ou supérieur à 100 000 D ; option possible.
- p. 24 : base : majoration de 25 % si le fournisseur n'est pas assujetti (sauf État, collectivités, établissements publics administratifs) ou si le produit figure sur la liste du décret n° 477 de 2003 du 3 mars 2003 (produits de consommation, hors équipements, matières premières et intrants).
- p. 25 : taux de TVA : général 18 % ; 6 % (médecins, laboratoires, infirmiers, professions paramédicales, transport de personnes, transport de produits de l'artisanat local, de produits agricoles ou de la pêche par des tiers…) ; 12 % (hôtellerie, restauration, avocats, huissiers-notaires, comptables et experts-comptables, transport de marchandises hors produits agricoles et de la pêche).
- pp. 26-27 : déductions de TVA et exceptions (voitures de tourisme non exploitées, achats auprès de non-assujettis) ; report de TVA pour les exportateurs.
- p. 28 : droit de consommation : voitures de tourisme, carburants, tabac, alcools et bière ; taux en pourcentage entre 10 % et 683 % ; tarifs spécifiques (carburants, alcools).
- p. 29 : autres prélèvements sur le chiffre d'affaires : fonds de compétitivité industrie-services-artisanat 1 % du chiffre d'affaires et de la valeur en douane ; fonds de compétitivité agriculture-pêche 2 % (fruits et légumes, produits de la pêche, à l'importation et sur la production locale) ; fonds de repos biologique (pêche) 1 % du chiffre d'affaires et 2 % de la valeur en douane à l'exportation ; fonds de compétitivité du tourisme 1 % du chiffre d'affaires et 2 D par siège pour les transports touristiques d'agences de voyages de catégorie A ; fonds de lutte contre la pollution 5 % du chiffre d'affaires et de la valeur en douane à l'importation.
- p. 30 : enregistrement : vente d'immeubles 5 % ; actes de sociétés 150 D par acte ; marchés 0,5 % de la valeur du marché.
- p. 31 : taxe de formation professionnelle 1 % (industries manufacturières) ou 2 % (autres secteurs) du salaire brut ; contribution au fonds de promotion du logement pour les salariés (FOPROLOS) 1 % du salaire brut ; taxe sur les contrats d'assurance 5 % (risques maritimes et aériens) et 10 % (autres risques).
- p. 32 : fiscalité locale : taxe sur les établissements à caractère industriel, commercial ou professionnel 0,2 % du chiffre d'affaires local brut (0,1 % pour les produits à prix homologués) ; taxe hôtelière 2 % du chiffre d'affaires brut ; taxe sur les immeubles bâtis : base = 2 % du prix de référence du m² x surface, taux entre 8 % et 14 % ; taxe sur les terrains non bâtis 0,3 % de la valeur vénale.

### Lacunes citées (pp. 34-38) — chiffres

- **p. 35 : « l'existence d'un régime forfaitaire réservé aux petits exploitants, dont ont profité de nombreux contribuables sans y avoir droit (environ 395 mille assujettis, qui contribuent pour 23,5 millions de dinars, soit 0,2 % du total des ressources fiscales) »** (à rapprocher de `ar_waqi` p. 12 : 23,4 M.D, 0,21 %).
- p. 35 : professions non commerciales : « rendement faible par rapport à leur nombre et au volume de leurs revenus » : 3 % du rendement de l'impôt sur le revenu ; salariés : « contribution élevée » : 80 % du rendement de l'impôt sur le revenu (aucun montant en dinars ni année).
- pp. 34, 36-38 : multiplicité des textes ; régime différencié des entreprises exportatrices ; exonérations (dividendes, plus-values) ; tranche exonérée et barème non adaptés à l'inflation ; champ de la TVA limité ; multiplicité des prélèvements sur le chiffre d'affaires ; faible rendement de la fiscalité locale. Aucun autre chiffre.
- pp. 40-41 : objectifs de la réforme (simplification, code unique, réduction du nombre de taux de TVA, rapprochement des régimes offshore / onshore, réduction des prélèvements sur le chiffre d'affaires, redistribution des tranches de l'IR, nouvelles compétences des collectivités locales). Aucun chiffre.

#### 2013-06_ar_manhajiyat_islah_nidham_jibai.pdf

- Titre (p. 1) : « منهجية إصلاح المنظومة الجبائية التونسية » — Méthodologie de la réforme du système fiscal tunisien. Date : 13 mai 2013. Auteur : République tunisienne, ministère des Finances. 15 pages (affichées 15 ; p. 16 vide à l'extraction), arabe, diaporama, texte seul.
- Pas de chiffre fiscal. Contenu :
  - p. 4 : objectifs (révision d'ensemble pour simplifier, plus d'efficacité et d'équité ; moderniser l'administration) et contraintes (cohérence avec les objectifs de croissance, compétitivité, équilibres budgétaires, moyens limités).
  - p. 5 : six domaines d'intervention : 1 impôts directs ; 2 impôts indirects ; 3 fiscalité locale ; 4 transparence, concurrence loyale, lutte contre l'évasion, garanties des contribuables ; 5 modernisation de l'administration fiscale ; 6 « révision du régime forfaitaire et intégration de l'économie parallèle dans le circuit économique organisé » (le régime forfaitaire est à réserver « exclusivement à ses ayants droit »).
  - pp. 6-7 : gouvernance : équipes de travail (superviseur, coordinateur, représentant du bureau d'études ; ministère des Finances, experts-comptables, conseillers fiscaux, comptables, universitaires), bureau d'études sélectionné sur appel d'offres, comité de pilotage, cellule consultative (Conseil national de la fiscalité).
  - pp. 9-13 : calendrier : phase préparatoire achevée (diagnostic initial avec l'administration, FMI, Banque mondiale, OCDE, USAID) ; 1re phase : lancement 13 mai, fin mai 2013 ; 2e phase : 1er juin - 31 août (travaux des équipes, débat au CNF) ; 1er - 15 septembre (présentation des grandes lignes à un conseil ministériel, options actualisées au CNF) ; 15 octobre (consultation nationale « Assises de la fiscalité ») ; fin octobre - 15 novembre (projet final à un conseil ministériel).

#### 2013-06_programme_reforme_fiscale_presentation_generale.pdf

- Titre (p. 1) : « مشروع إصلاح النظام الجبائي التونسي — لمحة عامة » — Projet de réforme du système fiscal tunisien : aperçu général. Présenté au Conseil national de la fiscalité (المجلس الوطني للجباية), **28 novembre 2013** (PDF créé le 29 novembre 2013, donc postérieur au CNF de juin ; le nom de fichier « 2013-06 » est trompeur pour ce document). « Avec la coopération de » MS Louzir, membre de Deloitte Touche Tohmatsu Limited (© 2013). 22 pages, arabe, diaporama, texte seul, aucun chiffre.
- Sommaire (p. 3) : 1 cadre général de la réforme ; 2 méthodologie du projet ; 3 synthèse du diagnostic et des recommandations (organismes nationaux et internationaux).
- p. 10 : six équipes de travail, deux séances par semaine chacune pendant 6 mois, soit « plus de 280 ateliers » ; chaque équipe comprend « plus de 120 personnes » ; comité de projet hebdomadaire, comité de pilotage mensuel.
- pp. 7-15 : méthodologie en phases 0 (cadrage, gouvernance) à III (mise en œuvre) ; consultation nationale ; stratégie d'exécution.
- pp. 17-22 : tableau « situation actuelle / position des parties prenantes » sur : équité (abattements pour salaires et pensions favorisant les hauts revenus ; exonérations de TVA contraires à la loyauté de la concurrence ; redistribution de la charge entre salariés et non-salariés) ; simplification (trois taux de TVA contre l'objectif de deux taux ; code unique) ; neutralité (base d'IS érodée) ; fiscalité locale ; administration ; transparence et lutte contre la fraude : p. 22 « le taux de respect de l'obligation fiscale baisse continûment », « de nombreux contribuables sont dans le régime forfaitaire sans droit », recommandation « intensifier le contrôle des forfaitaires ; réformer le régime forfaitaire et revoir ses modalités de gestion ». Aucun chiffre sur le forfait.

#### 2013-06_presentation_louati.pdf

- Titre (p. 1) : « Composition des entreprises » (le texte arabe « تركيبة المؤسسات » est la désignation donnée à la consigne ; les pages sont en français). Date : non indiquée (PDF créé le 13 mai 2013). Auteur : non indiqué (nom du fichier : Louati ; métadonnée de titre erronée « CEZ a.s. »). Mention « DRAFT » sur chaque page. 3 pages, français, graphiques en secteurs (IS, entreprises ; année des données non précisée).
- p. 1 « Composition des entreprises – par chiffre d'affaires » : 54 731 entreprises (317 « entreprises spéciales » exclues, ex. pétrole et gaz). Graphique 1 (nombre d'entreprises) : chiffre d'affaires nul 31 % ; locales 44 % ; totalement exportatrices 15 % ; partiellement exportatrices 10 %. Graphique 2 (chiffre d'affaires de 76,4 milliards DT) : local 64 % ; export 36 %.
- p. 2 : « par revenu » (54 731 entreprises) : déficitaires 38 % (- 4,6 milliards DT) ; rentables 43 % (5,8 milliards DT) ; revenu nul 19 %. « Assiette de l'impôt » (5,8 milliards DT) : exonérations 60 %, base imposable nette 40 %. « Par type d'incitation » (8 895 entreprises, exonérations 3,5 milliards DT) : export 82 % (- 2,9 milliards DT) ; non-export 10 % (- 200 millions DT) ; abattement pour réinvestissement 8 % (- 338 millions DT). Encadré : assiette brute 5,8 milliards - érosion 3,5 milliards = base imposable nette 2,3 milliards, soit 60 % d'érosion.
- p. 3 « Par paiement de l'impôt » : 34 185 entreprises ; moins de 350 DT : 44 % des entreprises, 0,3 million DT d'impôt ; plus de 350 DT : 56 % des entreprises, 644,8 millions DT d'impôt (attribution des montants aux deux tranches lue d'après les étiquettes du graphique ; à confirmer si utilisé).

#### 2013-06_liens.pdf

- Titre (p. 1) : « رسم توضيحي لمشروع الإصلاح » — Schéma illustratif du projet de réforme. Date : non indiquée (PDF créé le 13 mai 2013). Auteur : non indiqué. 2 pages, arabe, tableaux modèles (fiche d'équipe et matrice de priorisation) sur l'exemple des impôts directs. Aucun chiffre fiscal.
- p. 1 : fiche par domaine (exemple : impôts directs IS, IRPP, avantages fiscaux) : objectifs stratégiques (simplifier, équité, efficacité), contraintes ; orientations d'intervention : revoir le taux de l'IS ; rapprocher l'assiette de la base comptable ; adapter les modalités de recouvrement à la baisse des taux (retenue à la source, avance à l'importation) ; régime fiscal spécifique PME (taux et obligations) ; revoir le barème IR et exonérer les petits revenus ; revoir les déductions communes.
- p. 2 : matrice d'évaluation des propositions selon objectifs (simplification, équité, efficacité, croissance, compétitivité) et contrainte (recettes fiscales) avec un degré de priorité (1 : baisse du taux de l'IS ; 1 : règles de détermination de l'assiette ; 3 : adaptation des modes de recouvrement ; 2 : déductions communes) ; cases de la matrice vides.

#### 2013-06_axes_du_programme.pdf

- Titre (p. 1) : « Axes du programme de la réforme du système fiscal tunisien » (en-tête : République tunisienne, ministère des Finances, Direction générale des études et de la législation fiscales). Date : non portée sur le texte ; PDF créé le 6 juin 2013 ; renvoie à un rapport à remettre « au plus tard le 31 mai 2013 ». 3 pages, français, texte seul.
- Axes : I imposition directe (IS : réduction du taux de 30 % ; rapprochement de l'assiette de l'assiette comptable ; régime fiscal spécifique pour les PME ; IR : barème réaménagé avec défiscalisation des faibles revenus « ne dépassant pas 5 000 D » ; révision des déductions communes) ; II TVA (élargir le champ, réduire les cas particuliers d'assiette, réduire le nombre de taux) ; III avantages fiscaux (rapprochement on shore / off shore) ; IV transparence, lutte contre la fraude, économie informelle : « Révision du régime forfaitaire », levée du secret bancaire, sanctions, « catégorisation des contribuables comme c'est le cas pour le Maroc » ; V climat des affaires et garanties (rescrit fiscal, médiateur fiscal…) ; VI modernisation (système d'information, microsimulation « étude d'impact »).
- Coordinateurs : imposition directe Mme Sihem Nemsia ; TVA M. Imed Zaïr ; avantages fiscaux M. Khalil Chtourou ; transparence/fraude/informel Mme Najet Choura ; climat des affaires Mme Emna Gharbi ; modernisation M. Sami Mekki. Équipes : ministère des Finances, autres ministères, Ordre des experts-comptables, Chambre syndicale des conseillers fiscaux, Compagnie des comptables, un universitaire ; coordination générale par le directeur général des impôts et le DG des études et de la législation fiscales. Aucun chiffre.

---

### Inventaire D1 : Conseil national de la fiscalité, séance du 29 août 2013

Lecture visuelle intégrale des trois fichiers (rendu des pages en image). Les titres des métadonnées PDF sont faux (rf_1 : « Diapositive 1 » ; rf_2 : titre d'un autre groupe de travail) et sont ignorés. Répertoire : `/home/benjello/projets/tunisia-data/data/raw/minfinances/reforme_fiscale_2013_2014/`. Aucune page n'est une image sans texte à océriser : les trois fichiers ont une couche texte, mais en arabe inversé / en formes de présentation (illisible en extraction directe), d'où la lecture visuelle. Les « annexes » (ملحق 1, 2, 3) citées dans rf_2 ne sont pas dans le fichier. Les chiffres sont recopiés tels que lus sur les diapositives ; les astérisques (*) bleus des diapositives de rf_1 renvoient à des liens/notes non repris dans le PDF.

#### 2013-08_cnf_programme_ar.pdf

- Titre (p. 1) : « اجتماع المجلس الوطني للجباية — البرنامج » (Réunion du Conseil national de la fiscalité — Programme). Date de séance : 29 août 2013 (selon la consigne ; la page ne porte pas de date en clair). 1 page, arabe, programme de la séance. Pied de page : les interventions sont consultables sur finances.gov.tn ; pause café au choix des participants.
- Horaire : 08h30 accueil ; 09h00 ouverture par le ministre des Finances ; 09h30 intervention 1, Mme Sihem Nemsia : bilan du groupe de travail sur la réforme du système fiscal en matière d'impôts directs et avantages fiscaux ; 09h50 intervention 2, Mme Najet Choura : groupe chargé de la révision du régime d'évaluation (النظام التقديري : régime forfaitaire / d'assiette estimative) et de l'intégration de l'économie parallèle ; 10h10 intervention 3, M. Imed Zaiem : impôts indirects ; 10h30 débat ; 11h30 intervention 4, M. Rached Touzi : fiscalité locale ; 11h50 intervention 5, Mme Amna Gharbi : lutte contre la fraude fiscale, règles de transparence, garanties de recouvrement ; 12h10 intervention 6, M. Noureddine Ferii'a (lecture : Farî'a) : modernisation de l'administration fiscale ; 12h30 débat et clôture.
- Aucun chiffre.

#### 2013-08_cnf_rf_1_ar.pdf

- Titre (p. 1) : « مشروع إصلاح المنظومة الجبائية — حوصلة لأشغال فريق العمل المكلف بإصلاح المنظومة الجبائية في مادة الضرائب المباشرة والامتيازات الجبائية المتعلقة بها — أوت 2013 » (Projet de réforme du système fiscal — Synthèse des travaux du groupe de travail chargé de la réforme du système fiscal en matière d'impôts directs et d'avantages fiscaux — août 2013). Logo du ministère des Finances. Groupe de travail de la 1re intervention (Mme Sihem Nemsia d'après le programme). 33 diapositives (= 33 pages PDF), arabe, diaporama. Structure : 4 axes (p. 2) : (1) révision de l'assiette (entreprise / individus / autres propositions) ; (2) révision des taux (entreprise / individus) ; (3) révision des modes de recouvrement ; (4) révision des avantages fiscaux. Chaque diapositive d'axe oppose « Défauts (النقائص) » et « Propositions (المقترحات) ». « م د » = millions de dinars ; « مردود » = rendement.

### Chiffres globaux (p. 3 à 5, camemberts)
- p. 3, structure des redevables des impôts directs : personnes physiques 83 % ; personnes morales 17 %.
- p. 4, structure des recettes des impôts directs : impôts directs 43 % contre 57 % pour les autres recettes fiscales (droits de timbre/« المعاليم الديوانية » inclus : « باعتبار المعاليم الديوانية » = y compris les droits de douane) ; au sein des impôts directs, impôt sur les sociétés 48 %, impôt sur le revenu 52 %. Année non indiquée.
- p. 5, structure de l'impôt sur le revenu : salariés 81 % ; bénéfices des professions non commerciales (BNC) 3 % ; revenus fonciers 1 % ; autres catégories de revenus 15 %. Structure de l'impôt sur les sociétés : sociétés au taux de 35 % essentiellement 80 % (elles représentent 5 % de l'ensemble des sociétés) ; autres sociétés 20 %. Année non indiquée.

### Axe 1, assiette, volet entreprise (p. 7 à 11)
- p. 7 : étendre la liste des actifs amortissables (terrains exploités en lots, actifs incorporels type fonds de commerce) ; élargir les provisions déductibles (dépréciation des actions, subventions sociales dans le capital des sociétés soumises à commissaire aux comptes ; risques et charges dans certaines limites, risques de change, grosses réparations) ; relever par étapes le taux de déduction des provisions. Défaut : inadaptation de la législation fiscale à la législation comptable sur la détermination du résultat fiscal.
- p. 8 : report illimité des pertes dans le temps, avec imputation de la fraction sur les pertes réelles au titre de l'année de leur enregistrement lors d'un contrôle fiscal.
- p. 9 : codifier les conditions générales de déduction des charges ; élargir les charges nécessaires à l'exploitation et revoir les conditions spéciales (cadeaux aux ouvriers, présents, frais de réception) ; déduire les jetons de présence dans la limite d'un pourcentage du chiffre d'affaires, plutôt que les considérer comme remboursement de frais, ou dans la limite des jetons versés par les entreprises publiques.
- p. 10 : exonération de la plus-value de cession d'éléments d'actif (hors immeubles et fonds de commerce) après une durée de détention, sous condition de remploi du prix de cession dans un réinvestissement.
- p. 11 : aligner le taux d'intérêt des comptes courants d'associés sur le taux du marché financier et supprimer ce taux sur les prêts entre entreprises.

### Axe 1, assiette, volet individus (p. 12 à 19)
- p. 12 : relèvement des abattements pour situation et charges de famille, révisés périodiquement. Hypothèse 1 : chef de famille de 150 D à 250 D ; enfants à charge 100 D pour les quatre premiers. Hypothèse 2 : chef de famille de 150 D à 300 D ; enfants à charge 100 D par enfant sans limitation aux quatre premiers. Parents à charge : de 150 D à 300 D, avec durcissement des conditions de déduction. Défaut : inadéquation des abattements au coût de la vie et à l'évolution des prix.
- p. 13 : relèvement de la déduction pour frais professionnels, actuellement de 10 % (salariés). Hypothèse 1 : taux unique de 12 % pour toutes les tranches de revenu. Hypothèse 2 : taux dégressif selon des tranches de revenu croissantes (taux d'abattement plus élevé pour les revenus plus faibles). Défaut : déduction des frais professionnels inadaptée pour les salariés par rapport à leur contribution aux ressources fiscales.
- p. 14, régime d'assiette estimative (النظام التقديري) pour les BNC. Défauts : manque d'efficacité des régimes estimatifs ; BNC : faible contribution aux recettes fiscales (3 % de l'impôt sur le revenu) ; absence de critères objectifs de bénéfice du régime estimatif (60 % des intéressés déclarent selon la base estimative). Propositions : mécanismes pour relever leur contribution en revoyant le mécanisme d'imposition selon la base estimative et en durcissant les conditions d'accès : baisser l'abattement forfaitaire (الطرح التقديري) de 30 % à 20 %, rendement attendu +6,7 M D ; plafonner le chiffre d'affaires donnant accès à la base estimative ; fixer une durée maximale du bénéfice du régime (3 ou 5 ans) ; fixer des critères objectifs selon la nature de l'activité et les régions pour déterminer la base imposable.
- p. 15, revenus fonciers sous base estimative. Défauts : faible contribution (1 % de l'impôt sur le revenu) ; faible taux de déclaration de cette catégorie. Propositions : abattement estimatif de 30 % à 20 % ; obligations supplémentaires de déclaration des revenus fonciers (liste périodique des immeubles loués que les communes remettent à l'administration fiscale, sur le modèle des déclarations des propriétaires et locataires).
- p. 16 à 17, plus-values mobilières et immobilières. Défaut : revenus du capital favorisés par un régime différentiel par rapport aux revenus du travail (plus-value immobilière, plus-value de cession de titres). Hypothèse 1 : plus-values de cession de titres et d'immeubles soumises au barème de l'impôt sur le revenu comme les autres catégories. Hypothèse 2 : régime selon la durée de détention : plus-value à court terme intégrée au revenu global imposable ; plus-value à long terme à taux spécial après une durée de détention. Hypothèse 3 (p. 17) : étendre l'impôt sur la plus-value immobilière à tous les terrains sauf terres agricoles situées en zones agricoles, et à tous les terrains cédés aux promoteurs immobiliers y compris agricoles ; relever les taux sur la plus-value de cession de titres et supprimer l'abattement de 10 000 D, avec une exonération limitée aux petits épargnants.
- p. 18 : révision du barème d'évaluation des éléments du train de vie (article 42 du code de l'impôt sur le revenu des personnes physiques et de l'impôt sur les sociétés) pour actualiser le revenu estimatif tenant compte des besoins actuels.
- p. 19 : déclaration d'existence obligatoire pour toutes les personnes physiques sauf salariés et titulaires de revenus de capitaux mobiliers et de valeurs mobilières ; obligation de communiquer aux services fiscaux le système informatique, la base de données et les fichiers utilisés (achats, ventes, facturation).

### Axe 1, autres propositions (p. 20 à 21)
- p. 20 : étendre le champ de l'impôt aux associations et groupements de développement agricole et de pêche, réexaminer l'exonération des mutuelles et sociétés coopératives de services agricoles ; inclure dans une catégorie spéciale les revenus et bénéfices hors champ (plus-values de cession de biens meubles, gains de jeux de hasard et loteries).
- p. 21 : inciter les entreprises à éviter les paiements en espèces ; accès de l'administration aux relevés de comptes bancaires et postaux ; non-admission en déduction des services payés à des résidents de paradis fiscaux ; incitations pour ceux qui s'acquittent spontanément de leurs obligations, notamment les entreprises transparentes. Défaut : aggravation de la fraude fiscale.

### Axe 2, taux (p. 23 à 27)
- p. 23, impôt sur les sociétés, taux de 30 % (défaut : taux d'IS élevés et exonération des bénéfices distribués). Hypothèse 1 : taux de 30 % à 25 % et soumission des bénéfices distribués à l'impôt (5 %, 10 % ou 15 %), sans égard à la qualité du bénéficiaire (résident ou non, personne physique ou morale), en maintenant l'exonération des bénéfices distribués aux personnes morales résidentes.
- p. 24 : Hypothèse 2 : de 30 % à 20 % et distribution soumise à 5 %, 10 % ou 15 %, sans égard à la qualité du bénéficiaire. Hypothèse 3 : taux à 25 % ou 20 % en supprimant tous les avantages sauf ceux accordés à l'épargne (prise en compte du projet de révision du code d'incitation à l'investissement). Hypothèse 4 : taux à 25 % ou 20 % avec instauration d'un impôt minimum de 0,5 % du chiffre d'affaires brut (y compris l'exportation) applicable à toutes les entreprises ; cet impôt minimum donne droit à un crédit d'impôt limité dans le temps pour les entreprises déficitaires.
- p. 25 : étendre l'application du taux de 35 % aux grandes surfaces, fournisseurs d'accès internet et secteurs à forte marge ; soumettre les entreprises exonérées d'impôt sur les sociétés au taux réduit de 10 % (rendement +85,4 M D). Défaut : inadéquation du taux d'IS à la nature de l'activité.
- p. 26, IRPP, barème : relever la première tranche du barème de 1 500 D à 2 500 D ou 3 000 D avec redistribution du barème. Relever la tranche exonérée de base en supprimant la déduction supplémentaire de la base de 1 000 D pour les titulaires du salaire minimum garanti (SMIG) et en l'appliquant à toute personne physique dont le revenu net annuel n'excède pas 5 000 D. Relever la déduction supplémentaire de 1 000 D pour les titulaires du SMIG, les salariés, pensionnés et rentiers viagers dont le revenu net annuel n'excède pas 5 000 D, avec déduction supplémentaire de 500 D. Défaut : inadéquation des taux d'IR à l'évolution des prix et aux revenus limités.
- p. 27 : exonérer les personnes physiques dont le revenu net annuel n'excède pas le SMIG ou fixer la tranche exonérée au niveau du SMIG (indexation au SMIG), avec relèvement des taux des tranches supérieures dans certains cas.

### Axe 3, recouvrement (p. 29 à 31)
- p. 29 : aligner les taux de retenue à la source avec la révision des taux de l'IS et du barème de l'IR (défaut : taux élevés et multiples).
- p. 30 : relever à 15 % le taux de la retenue à la source sur les sommes versées à des résidents ou établis dans des paradis fiscaux ; permettre à la Tunisie d'appliquer les taux des conventions de non double imposition : retenue sur intérêts de prêts versés à des établissements bancaires non résidents de 5 % à 10 % (rendement attendu +1,8 M D) ; fin de l'exonération des redevances versées par les établissements totalement exportateurs à des non-résidents ; généraliser la non-déductibilité de la retenue à la source supportée par les entreprises au titre de redevances pour non-résidents.
- p. 31 : réduire le taux de l'acompte provisoire sur les importations de biens de consommation, actuellement de 10 %, et revoir la liste des produits de consommation soumis à cet acompte (défaut : taux élevé affectant la trésorerie des entreprises).

### Axe 4, avantages fiscaux (p. 33)
- Soumettre les bénéfices d'exportation à l'impôt sur les sociétés au taux de 10 % à compter de 2014, rendement attendu +137 M D ; unifier la notion d'exportation entre le code de l'IR/IS et le code d'incitation à l'investissement ; réviser les avantages du code de l'IR/IS vers une harmonisation avec le projet de nouveau code d'investissement, en maintenant les avantages liés à l'épargne ; remplacer les avantages par un crédit d'impôt à la réalisation effective des opérations ouvrant droit ; regroupement des avantages fiscaux dans un cadre juridique unique. Défauts : éparpillement du système d'avantages fiscaux ; inadéquation de certains avantages à ceux de la législation de l'investissement ; multiplicité des exonérations partielles et totales et des déductions de la base.
- Les p. 2, 6, 22, 28, 32 sont des diapositives de plan / titres d'axe.

### Régime forfaitaire
Ce fichier ne donne ni nombre de forfaitaires, ni recettes du forfait. Les seules données sur le régime estimatif (النظام التقديري) sont : BNC = 3 % de l'IR ; revenus fonciers = 1 % de l'IR ; 60 % des BNC déclarent sous régime estimatif ; abattement estimatif de 30 % ramené à 20 % (BNC et fonciers), rendement attendu +6,7 M D (p. 14) ; plafonnement du CA, durée limitée (3 ou 5 ans) et critères objectifs envisagés.

#### 2013-08_cnf_rf_2_ar.pdf

- Titre (p. 1) : « مشروع إصلاح المنظومة الجبائية بوزارة المالية — حوصلة لأشغال فريق العمل المكلف بالضرائب غير المباشرة » (Projet de réforme du système fiscal du ministère des Finances — Synthèse des travaux du groupe de travail chargé des impôts indirects). La métadonnée PDF (titre sur la modernisation de l'administration fiscale) est fausse. Groupe de la 3e intervention (M. Imed Zaiem d'après le programme). Août 2013 (non daté sur la page). 25 diapositives, arabe, diaporama ; rendu des pages avec mutool (pdftoppm échoue sur ce fichier). Axes (p. 3) : champ de la TVA, taux, assiette, conditions de déduction, excédent de TVA et remboursement, retenue à la source de 50 % en TVA, obligations et sanctions en matière de droits indirects.
- p. 2 : objectifs : consacrer l'équité fiscale ; simplifier les règles fiscales ; garantir la neutralité de l'impôt à l'égard des opérateurs économiques.
- p. 5, défauts du champ d'application : secteurs hors champ : agriculture et pêche ; grossistes de la restauration générale ; détaillants dont le chiffre d'affaires annuel est inférieur à 100 000 D (écrit « 100 000 ألف دينار » dans le texte) ; personnes sous régime estimatif ; multiplicité des exonérations et rupture de la chaîne de déduction (accumulation de résidus fiscaux) ; multiplicité des textes d'exonérations spéciales ou d'annexes ; multiplicité des droits assis sur le chiffre d'affaires, comme ceux au profit des caisses spéciales du Trésor : 18 droits, rendement d'environ 320 millions de dinars en 2012 (annexe 1, non jointe).
- p. 6 : proposition : généraliser la TVA par étapes ; supprimer les exonérations accordées à certaines entreprises publiques par leurs lois (annexe 2) ; exigences de l'étude : exonération au titre du chiffre d'affaires et des acquisitions (équipements et services) ; étudier les ratios d'équilibre ; étudier l'impact financier sur le budget des entreprises concernées.
- p. 7 : réviser les exonérations du tableau « A » annexé au code de la TVA ; suppression graduelle des exonérations ; liste limitée d'exonérations (annexe 3) ; listes de produits à étudier pour l'effet sur les prix (denrées de base) ou l'impact économique (secteur financier).
- p. 9, taux de TVA : hypothèses : deux taux ; ou deux taux avec un taux super réduit (taux super réduit) ; ou maintien de 3 taux avec révision (par modification des taux ou des listes de produits et activités) ; dans tous les cas, liste limitée de produits soumis à un taux autre que le taux de droit commun. Objectifs : équité fiscale (secteurs actuellement à des taux différents) ; simplification (cas de deux taux) ; limiter l'accumulation d'excédent de TVA (secteurs à taux réduit enregistrant un excédent).
- p. 10, rendement de la TVA par taux (en millions de dinars) : taux 6 % : 2009 = 58 ; 2010 = 56,9. Taux 12 % : 2009 = 622,5 ; 2010 = 609,4. Taux 18 % : 2009 = 2 686,3 ; 2010 = 3 086. Total : 2009 = 3 373,5 ; 2010 = 3 749,8. (Les taux de droit commun à 18 %, réduits 6 % et 12 % ressortent du tableau ; le taux de 25 % apparaît p. 12-13 ; pas d'autre année dans le tableau.)
- p. 12, défaut sur la base : le relèvement de 25 % (majoration de la base) a contribué à la montée de la fraude, notamment sur les chiffres d'affaires déclarés et la facturation ; charges administratives supplémentaires de contrôle et contentieux.
- p. 13 : la TVA est calculée selon une règle générale et des règles spéciales pour certaines opérations, notamment la majoration de 25 % sur les ventes des assujettis à des non-assujettis. Proposition : suppression de la majoration de 25 % dans l'assiette de la TVA. Étude de l'impact financier : rendement de la majoration de 25 % : 2009 = 26,8 M D ; 2010 = 28,2 M D ; 2011 = 28,5 M D.
- p. 15, défauts sur les conditions de déduction : manque de clarté sur les conditions (obligations comptables : registre de la TVA) ; exceptions limitant le droit à déduction ; multiplicité des exonérations rompant la chaîne de déduction, notamment pour les assujettis totalement à la TVA fournissant des personnes ou institutions exonérées (texte de bas de page, suite coupée à l'écran mais lisible dans la couche texte).
- p. 16 : propositions : simplifier les procédures et conditions de déduction ; système fondé sur la déduction de la TVA sur la base des factures ou équivalent ; principe de non-limitation du droit à déduction en cas d'irrégularités comptables, avec application des seules pénalités ; supprimer les exceptions au droit à déduction.
- p. 18, excédent de TVA (crédit de TVA) : accumulation d'excédent chez les entreprises assujetties, effet négatif sur la trésorerie, charges administratives de contrôle des dossiers et de remboursement. Volume d'excédent de TVA enregistré : 2010 = 1 415 M D ; 2011 = 1 502 M D ; 2012 = 1 694 M D. Absence de clarté des dispositions de remboursement ; complexité des dispositions de remboursement.
- p. 19 : propositions : supprimer les causes d'apparition de l'excédent ; compensation entre excédent de TVA et autres droits exigibles ; unifier le taux de l'acompte provisoire ; supprimer la mesure de non-transfert de l'excédent ; améliorer les délais de remboursement. Montants d'excédent demandés et remboursés : demandés 2010 = 375,8 M D ; 2011 = 359,2 M D ; 2012 = 203,3 M D. Remboursés 2010 = 320,8 M D ; 2011 = 301,2 M D ; 2012 = 179,2 M D.
- p. 21, retenue à la source de 50 % en TVA : effet négatif sur la trésorerie des entreprises soumises à la retenue ; contribution mécanique à gonfler les montants d'excédent (coût administratif de contrôle des dossiers de remboursement) ; assujettissement des entreprises organisées qui déclarent et paient la TVA. Rendement de la retenue à la source de 50 % : 2010 = 387,2 M D ; 2011 = 352,1 M D ; 2012 = 305,5 M D.
- p. 22 : proposition : baisser le taux de la retenue de 50 % progressivement en vue de la supprimer ; étude de l'impact financier pour fixer le taux proposé.
- p. 24 : défaut : dispersion des dispositions sur les obligations et sanctions (code de la TVA, loi sur le droit de consommation, code de l'IR/IS, code des droits et procédures fiscaux) ; multiplicité et complexité des obligations (attestations, registres) ; sanctions inadaptées à la nature des infractions.
- p. 25 : propositions : regrouper toutes les sanctions dans un seul texte (code de la TVA) ; simplifier les obligations fiscales ; fixer les sanctions selon la nature des infractions.
- Les p. 1, 3, 4, 8, 11, 14, 17, 20, 23 sont des diapositives de titre ou de plan.
- Ce fichier ne traite ni du régime forfaitaire (hors mention « personnes sous régime estimatif » hors champ de la TVA, p. 5), ni du droit de consommation (cité seulement p. 24), ni de recettes globales.

---

### Inventaire A : deux diaporamas du Conseil national de la fiscalité, août 2013 (régime forfaitaire)

Lecture visuelle de toutes les pages des deux fichiers (rendu 80 dpi, plus un zoom sur la p. 33). Les deux PDF sont de 34 pages, en arabe, sans image-scan : la couche texte existe (mais l'ordre bidi est inversé, d'où la lecture visuelle). Aucun OCR à prévoir.

#### Relation entre les deux documents (à lire d'abord)

**Ce sont deux exports du même diaporama** « حوصلة لأشغال فريق العمل المكلف بمراجعة النظام التقديري وإدماج الإقتصاد الموازي », même contenu, mêmes chiffres, mêmes graphiques. Seule la police change : dans `rf_4_ar`, une police de substitution plus large fait déborder le texte des cases (propositions et diagnostics tronqués en bas de case aux p. 4, 10, 11, 12-15, 17-19, 21, 24-25, 32, 34 ; p. 4 : la dernière puce est coupée) ; le fichier `presentation_revision_regime_forfaitaire` est donc le plus lisible. Le titre du fichier `rf_4_ar` (métadonnées PDF) est « حوصلة لأشغال فريق العمل المكلف بدراسة مجال "تعصير إدارة الجباية… », titre du groupe voisin, probablement hérité d'un modèle : le contenu, lui, est bien celui du forfait.
- **Diapositives strictement identiques (texte extrait identique)** : 1, 2, 23, 28, 32 ; la p. 33 est identique à 95 %, elle aussi (graphique de répartition par secteur, mêmes valeurs).
- **Mêmes diapositives, mise en page différente** (valeurs numériques identiques, vérifiées visuellement p. 3-14, 20, 21, 24, 25, 32-34 et par comparaison des nombres extraits pour les autres) : toutes les autres, avec un **ordre différent** pour les p. 15-19 :
  - A p. 15 (II. révision de la méthode de fixation de l'impôt) = B p. 19 ;
  - A p. 16 (III. généralisation de la TVA ; écart 98 D / 522 D) = B p. 15 ;
  - A p. 17 (intercalaire « Axe 1 – 3. maîtrise de l'assiette ») = B p. 16 ;
  - A p. 18 (maîtrise de l'assiette : 60 %, 0,2 %, 45 000) = B p. 17 ;
  - A p. 19 (maîtrise de l'assiette, suite : 66 %, transport 21 %/20 %) = B p. 18.
  - Les p. 22, 26, 27, 29-31 de B n'ont pas été relues image par image ; leurs nombres extraits sont identiques à ceux de A.
- Les chiffres ci-dessous sont donnés avec la pagination du fichier A (`presentation_revision_regime_forfaitaire`) ; ceux de B se déduisent par la correspondance ci-dessus.

#### 2013-08_cnf_presentation_revision_regime_forfaitaire.pdf

- **Titre (p. 1)** : « مشروع إصلاح المنظومة الجبائية – وزارة المالية » puis « حوصلة لأشغال فريق العمل المكلف بمراجعة النظام التقديري وإدماج الإقتصاد الموازي » (Projet de réforme du système fiscal, ministère des Finances ; synthèse des travaux du groupe de travail chargé de la révision du régime d'estimation [= forfaitaire] et de l'intégration de l'économie parallèle). Titre du fichier : « Révision du système forfaitaire ».
- **Date** : aucune sur le document ; présenté au Conseil national de la fiscalité du 29 août 2013 (selon la consigne). Seule date interne : séance de travail Gouvernement–UTICA du 24 mai 2013 (p. 25) ; chiffres jusqu'à fin juin 2013 pour la p. 4.
- **Auteur** : groupe de travail « régime d'estimation et économie parallèle », projet de réforme fiscale du ministère des Finances. **Nature** : diaporama, 34 p., arabe (étiquettes de graphiques en français). Structure : Axe 1 révision du régime forfaitaire (1 données statistiques p. 4-9 ; 2 révision du système de fixation de l'impôt p. 10-16 ; 3 maîtrise de l'assiette p. 17-19 ; 4 amélioration du recouvrement p. 20-22) ; Axe 2 intégration de l'économie parallèle (p. 23-27) ; Axe 3 mesures communes (p. 28-31) ; « merci » (p. 32) ; deux annexes (p. 33-34).
- Remarque sur les unités : « م د » = millions de dinars ; « د » = dinars ; « أ د » = mille dinars (les tranches de « رقم المعاملات », chiffre d'affaires déclaré, sont en dinars : [0-3000] etc.).

### Chiffres du régime forfaitaire (priorité a)

**p. 4 – données statistiques (texte)**
- Inscrits au fichier : de 300 000 en 2004 à 394 000 à fin juin 2013 (+31,3 %).
- Part dans le fichier : 60 % de l'ensemble du fichier et 80 % des « PP-BIC ».
- Dépôt des déclarations annuelles : 40 % dans les délais légaux, 50 % à la fin de l'année.
- Contribution : de 14 M D en 2004 à 23 M D en 2012 (+64 %) ; la diapositive précise qu'en 2010 la contribution des forfaitaires a atteint 30 M D (valeur différente des 22,616 M D du graphique p. 5 pour 2010 : écart non expliqué dans le document).
- Part dans les recettes fiscales du régime interne : 0,2 %.
- Interventions des services de contrôle auprès de ces personnes : en moyenne 45 000 interventions par an, pour un rendement d'environ 12 M D.

**p. 5 – inscrits au fichier, taux de dépôt, contribution (graphique + tableau)**
| | 2009 | 2010 | 2011 |
|---|---|---|---|
| Total inscrits | 348 581 | 363 390 | 377 045 |
| En règle (déposants) | 232 504 (67 %) | 216 526 (60 %) | 181 337 (48 %) |
| Défaillants | 116 077 | 146 864 | 195 708 |
| Contribution totale (M D) | 25,181 | 22,616 | 14,969 |
| Contribution moyenne (dinars) | 108,3 | 104,5 | 82,5 |
(Les pourcentages figurent sur la partie « en règle » du graphique ; 232 504 + 116 077 = 348 581, etc. : cohérent.)

**p. 6 – répartition par secteur (deux camemberts, 2010)**
- Répartition des forfaitaires actifs (nombre) : services 52 %, commerce de détail 43 %, transformation (« عمليات التحويل ») 4 %, entreprises artisanales (« مؤسسات حرفية ») 1 %.
- Répartition de la contribution 2010 : services 56 %, commerce de détail 36 %, transformation 7 %, artisanat 1 %.
(Attribution des camemberts : le titre de droite porte « contribution 2010 », celui de gauche « répartition des forfaitaires actifs par secteur » ; confirmée par les montants de la p. 33.)

**p. 7 – nombre de déclarations par tranche de chiffre d'affaires (« رقم المعاملات », dinars), 2009 / 2010 / 2011**
Tranches : [0-3000], [3000-6000], [6000-9000], [9000-12000], [12000-15000], [15000-18000], [18000-21000], [21000-24000], [24000-27000], [27000-30000], [30000-100000]. Effectifs puis cumul en %.
- 2009 : 129 568 ; 55 718 ; 24 423 ; 10 934 ; 4 206 ; 1 982 ; 959 ; 385 ; 184 ; 124 ; 4 021 (somme 232 504). Cumul : 56, 80, 90, 95, 97, 98, 98, 98, 98, 98, 100 %.
- 2010 : 131 143 ; 47 352 ; 19 220 ; 8 572 ; 3 370 ; 1 688 ; 837 ; 350 ; 195 ; 199 ; 3 600 (somme 216 526). Cumul : 61, 82, 91, 95, 97, 98, 98, 98, 98, 98, 100 %.
- 2011 : 108 827 ; 45 205 ; 12 231 ; 6 061 ; 2 784 ; 1 523 ; 1 071 ; 528 ; 458 ; 479 ; 2 170 (somme 181 337). Cumul : 60, 85, 92, 95, 97, 97, 98, 98, 99, 99, 100 %.
(Les sommes recalculées retombent sur les « en règle » de la p. 5.)

**p. 8 – contribution par tranche de chiffre d'affaires (mêmes tranches ; valeurs en milliers de dinars d'après la cohérence avec les totaux de la p. 5)**
- 2009 : 5 765 ; 4 501 ; [3e valeur masquée par une étiquette, non lisible ; ≈ 3 200 d'après la hauteur de la barre et le total 25 181] ; 2 273 ; 1 297 ; 874 ; 562 ; 290 ; 155 ; 119 ; dernière tranche 6 123. Cumul : 23, 41, 54, 63, 68, 71, 73, 75, 75, 76, 100 % ; la dernière tranche [30 000-100 000] pèse 24 %.
- 2010 : 5 901 ; 3 939 ; 2 626 ; 1 824 ; 1 059 ; 745 ; 489 ; 255 ; 166 ; 185 ; dernière tranche non lisible (étiquette recouverte ; ≈ 5 400 par différence avec 22 616). Cumul : 26, 44, 55, 63, 68, 71, 73, 74, 75, 76, 100 % ; dernière tranche 24 %.
- 2011 : 6 091 ; 3 243 ; 1 402 ; 937 ; 547 ; 363 ; 300 ; 172 ; 168 ; 203 ; 1 544 (somme 14 970 ≈ 14 969). Cumul : 41, 62, 72, 78, 82, 84, 86, 87, 88, 90, 100 % ; dernière tranche 10 %.

**p. 10 – ancienneté d'activité (diagnostic) : part des inscrits / part de la contribution**
| Ancienneté | % des inscrits | % de la contribution |
|---|---|---|
| moins de 8 ans | 32 % | 24 % |
| 8 à 13 ans | 21 % | 20 % |
| 13 à 23 ans | 30 % | 33 % |
| 23 à 33 ans | 13 % | 17 % |
| plus de 33 ans | 4 % | 6 % |
Texte p. 10 (diagnostic) : des bénéficiaires du régime sans droit ni conditions légales suffisantes liées aux éléments d'exercice ; déclarations ne contenant pas les informations sur l'exercice ; pas d'indicateur de durée. Proposition court terme : (1) exclure certaines activités du régime ; (2) en restreindre davantage le bénéfice **dans le temps** : régime accordé pour 3 ou 4 ans à compter du début d'activité (chevauchement possible), renouvelable une seconde période sur présentation d'un justificatif d'éligibilité ; l'administration conserve son droit de contrôle.

**p. 11 – tranches de chiffre d'affaires déclaré, 2010 (en milliers de dinars)**
| Tranche | % des déclarations 2010 | % cumulé |
|---|---|---|
| moins de 3 | 61 % | 61 % |
| 3 à 6 | 21 % | 82 % |
| 6 à 9 | 9 % | 91 % |
| 9 à 12 | 4 % | 95 % |
| plus de 12 | 5 % | 100 % |
Proposition 3 (p. 11) : exempter du forfait les contribuables dont le revenu est limité (« revenu de survie ») des obligations fiscales liées à l'activité, sauf la déclaration d'existence, contre un mécanisme permettant aux collectivités locales de les suivre et d'établir une contribution rédactionnelle (« مساهمة تحريرية ») au profit de ces collectivités. (Le chiffre de seuil du « revenu de survie » n'est pas donné.)

**p. 12-13 – propositions moyen terme (pas de chiffre)** : régime d'estimation contractuel (négocié) pour une durée donnée, appliqué dans les zones municipales, fondé sur des indicateurs (superficie du local, nombre d'employés, marge bénéficiaire) ; ou instauration d'un droit annuel fixe (« Droit de patente ») fixé en concertation avec les représentants des secteurs, payé durant les 6 premiers mois de l'année, l'impôt définitif sur le revenu étant calculé sur un taux appliqué à l'écart entre recettes et dépenses, l'impôt dû ne pouvant être inférieur au droit fixe. Diagnostic : pas d'indicateurs de « timing » ni de « catégorisation » lors de l'octroi du régime.

**p. 14 – montant de l'impôt minimum** : diagnostic : faiblesse du montant de l'impôt minimum et des taux de l'impôt appliqués au chiffre d'affaires, d'où faible contribution aux recettes fiscales (contribution moyenne par personne **82 dinars en 2011**). Proposition : relever l'impôt minimum exigible et l'aligner sur celui des contribuables du régime réel, avec rattachement possible au minimum dû au titre du droit de « superficie » des établissements. Aucun montant proposé.

**p. 15 – méthode de fixation** : diagnostic : le système manque d'équité car il ne tient pas compte de la différence de marge bénéficiaire entre activités et régions. Propositions : (a) adapter les taux appliqués au chiffre d'affaires selon la nature de l'activité et la marge bénéficiaire ; ou (b) remplacer par un système de fixation du bénéfice ou du revenu sur une marge différenciée par secteur/activité, avec revenu global soumis au barème (déclaration unique). Aucun taux chiffré.

**p. 16 – généralisation de la TVA (facturation) et écart forfait/réel**
- Diagnostic : « Pour 36 activités exercées par 80 % des forfaitaires, la contribution individuelle moyenne est de **98 dinars**, contre **522 dinars** de contribution individuelle moyenne des contribuables du régime réel au titre de l'impôt sur le revenu. »
- Propositions : court terme, limiter l'assujettissement à la TVA aux prestataires de services (seuls les prestataires de services y seraient soumis, les autres non) ; moyen terme, soumettre à la TVA le reste des forfaitaires, sauf quelques activités relevant du régime de l'homologation administrative des prix.

**p. 18-19 – maîtrise de l'assiette**
- p. 18 : 60 % des inscrits au fichier ne contribuent que pour 0,2 % des recettes du régime interne ; 45 000 interventions par an pour un rendement de 12 M D. Propositions : développer l'information fiscale et le système d'information ; soumettre les forfaitaires à l'obligation de facturation pour les opérations dépassant un montant donné (non chiffré).
- p. 19 : nombre de forfaitaires ayant antérieurement opté pour le régime facultatif, qui réduisent leur chiffre d'affaires pour limiter leur contribution : **66 %** (formulation : « de ceux qui ont opté pour le régime d'estimation facultatif … en réduisant leur chiffre d'affaires pour limiter leur contribution, à hauteur de 66 % » ; sens exact de ce 66 % ambigu à la lecture). **Transport : 21 % des forfaitaires exercent dans le transport et contribuent pour 20 % de la contribution globale.** Propositions : caisses enregistreuses ou carnet de tickets pour certaines activités ; carnet de bord et d'entretien du véhicule pour le transport.

**p. 21-22 – recouvrement** : diagnostic : faiblesse de la contribution en raison de la suppression des acomptes provisionnels et du refus de payer en deux fois, d'où un taux d'omission élevé (taux de dépôt légal 40 %, 50 % à fin d'année). Propositions : rendre obligatoire le paiement en deux tranches ; recours automatique (« آلي لخطية ») à un montant égal à l'impôt minimum pour les défaillants ; lier le paiement des sommes dues par l'État et les établissements publics au règlement de la situation fiscale ; lier le certificat de contrôle technique des véhicules à la production de la dernière quittance ; lier les services administratifs rendus à la régularisation fiscale.

**p. 31 – sanctions (diagnostic)** : « pénalité de **100 dinars** pour défaut de tenue du livre des recettes et dépenses et **25 dinars** pour défaut de déclaration d'existence » ; proposition : relever les montants des pénalités. (Ces montants sont les seuls chiffres de pénalité de la présentation.)

**p. 34 – transport (annexe)**
- Contribution individuelle moyenne par activité (dinars) : transport de marchandises 58 ; taxi 99 ; louage 125 ; transport rural 72.
- Répartition de la contribution des transporteurs par tranche de CA (2010) : [0-3000] 29 % ; [3000-6000] 34 % ; [6000-9000] 22 % ; [9000-12000] 10 % ; [12000-100000] 5 %.

**p. 33 – répartition des forfaitaires par secteur d'activité (contribution, 2010), annexe**
- Camembert (milliers de dinars, part) : services 12 565,1 (56 %) ; commerce de détail 8 141,1 (36 %) ; activités industrielles 1 683,5 (7 %) ; activités artisanales 226,4 (1 %). Total ≈ 22 616 = contribution 2010 de la p. 5.
- Quatre barres empilées de la part de chaque sous-activité dans la contribution du secteur (attribution étiquette-valeur déduite de l'ordre d'empilement, de bas en haut ; les sommes ne font pas 100 % : valeurs intermédiaires non affichées ou masquées) :
  - Services : 446 café-buvette 19 % ; 490 autres prestations 16 % ; 422 taxi 14 % ; 421 transport terrestre de marchandises 11 % ; 480 mécanique générale 8 % ; 444 restauration 8 % ; 461 coiffure 6 % ; 423 louage 6 %. (Total lu : 88 %.)
  - Commerce de détail : 215 alimentation générale 49,1 % ; 290 autres commerces de détail 18,3 % ; 220 textiles, bonneterie et mercerie 7,9 % ; 217 débit de tabac 5,6 % ; 256 quincaillerie et articles sanitaires 3,1 % ; 265 pièces détachées et pneumatiques 2,4 %. (Total lu : 86,4 %.)
  - Industrie : 575 bois et ameublement 48,7 % ; 565 sidérurgie et métallurgie 20,2 % ; 521 boulangerie et pâtisserie 10,5 % ; 586 cuir et chaussures 5,8 % ; 580 textile 4,9 % ; 590 autres 2,4 %. (Total lu : 92,5 %.)
  - Artisanat : 180 poterie 23 % ; 190 autres artisanats 22 % ; 130 tissage et habillement 20 % ; 121 argent 12 % ; 160 bois et fibres végétales 9 % ; 150 cuir et chaussure 9 % ; 120 or 4 %. (Total lu : 99 %.)
  - Réserve : l'appariement exact étiquette/pourcentage n'est pas certain (légende et barres sont séparées) ; à vérifier sur le PDF avant citation.

### Autres chiffres (priorité b à e)

- **p. 24 – économie non structurée (part du PIB)** : Tunisie 30 % ; Turquie 32 % ; pays en développement 41 %.
- **p. 25 – causes** : rigidité du marché du travail et de la réglementation (part en %) : Tunisie 15 % ; Liban et Égypte 37 % ; Maroc et Syrie 29 % ; Jordanie 20 %. Niveau des impôts : Tunisie 37 % ; Liban et Égypte 12 % ; Maroc 37 % ; Jordanie 29 % ; Syrie 18 %. (Les intitulés exacts des indicateurs, sans unité ni année ni source, ne sont pas précisés dans la diapositive.) Propositions : comités mixtes, séance Gouvernement–UTICA du 24 mai 2013, étude d'une « police fiscale ».
- Autres pages (26-31) : propositions qualitatives (zones franches commerciales frontalières, espaces dédiés, contrôle conjoint, relèvement des pénalités, révision à la baisse des taux de l'impôt pour attirer vers le secteur organisé, politique de communication, service fiscal pour les PME (« SIME »), prolongation des délais de prescription, interdiction des factures préfabriquées, réduction du coût de conformité) ; aucun chiffre.
- Pas de chiffre sur l'IRPP (barème), l'IS, la TVA (taux) ni sur les recettes fiscales globales, hors la mention de 0,2 % (p. 4, 18).

#### 2013-08_cnf_rf_4_ar.pdf

- **Titre (p. 1)** : identique à celui de A (« حوصلة لأشغال فريق العمل المكلف بمراجعة النظام التقديري وإدماج الإقتصاد الموازي ») ; métadonnées PDF au titre du groupe voisin (voir plus haut). 34 p., arabe, diaporama, texte extractible, mêmes auteur et date que A.
- **Contenu** : identique à A ; seule la mise en page diffère (police élargie, débordement de texte, quelques graphiques avec séparateurs de milliers en espace au lieu de point : « 25,181 / 22,616 / 14,969 » au lieu de « 25.181 / 22.616 / 14.969 » ; « 116 077 » au lieu de « 116,077 »). Valeurs vérifiées visuellement identiques aux p. 5-8, 10-11, 24-25, 33-34. Correspondance de pagination des p. 15-19 : voir plus haut.
- Texte p. 4 tronqué ; ce fichier n'apporte aucun chiffre supplémentaire : inutile de l'exploiter si A est disponible.

---

### Inventaire D2 : Conseil national de la fiscalité, août 2013 (rapports de groupes de travail n° 3, 5, 6)

Répertoire : /home/benjello/projets/tunisia-data/data/raw/minfinances/reforme_fiscale_2013_2014/
Lecture : visuelle des 77 diapositives (rendu PDF), complétée par la couche texte pour les chiffres. Pour les trois fichiers, le titre des métadonnées PDF est le même copier-coller (« حوصلة لأشغال فريق العمل المكلف بدراسة مجال "تعصير إدارة الجباية » ), faux pour les nos 5 et 6. Les trois sont des diaporamas PowerPoint 2007 (4:3, 720 x 540 pt), créés les 27-28 août 2013 (métadonnées). Aucune page n'est un scan : la couche texte existe partout (arabe extrait en ordre inversé / illisible, chiffres fiables), pas d'OCR à prévoir. Aucun des trois ne contient de donnée sur le régime forfaitaire, l'IRPP, l'IS ni la TVA (priorités a à d : néant). Contenu relevant de la priorité e : contrôle fiscal, fiscalité locale, recouvrement.

Structure commune des diapositives : trois colonnes « العنصر » (élément) / « التشخيص » (diagnostic) / « المقترحات » (propositions). Plusieurs diapositives débordent du cadre : le texte du bas est coupé à l'écran (signalé « coupée » ci-dessous), la couche texte n'ajoute en général rien de plus.

---

#### 2013-08_cnf_rf_3_ar.pdf

- **Titre exact (p. 1)** : « مشروع إصلاح المنظومة الجبائية بوزارة المالية » (Projet de réforme du système fiscal au ministère des Finances), la ligne du haut est coupée à l'écran ; sous-titre : « حوصلة لأشغال فريق العمل المكلف بدراسة مجال تعصير إدارة الجباية » (Synthèse des travaux du groupe de travail chargé d'étudier le domaine de la modernisation de l'administration fiscale).
- **Date** : « 18 جويلية 2013 » (18 juillet 2013) sur la première diapositive ; fichier PDF créé le 28 août 2013.
- **Auteur** : groupe de travail « modernisation de l'administration fiscale » du projet de réforme du système fiscal, ministère des Finances (logo). Pas de nom de personne.
- **Pages** : 28. **Langue** : arabe. **Nature** : diaporama de synthèse (5 axes). Pas de scan.
- **Plan** : axe 1 restructuration du cadre organisationnel de l'administration fiscale (p. 3-7) ; axe 2 renforcement des services à distance (p. 8-12) ; axe 3 développement des services fiscaux (p. 13-16) ; axe 4 communication et relation avec les contribuables (p. 17-20) ; axe 5 moyens de travail et leur gestion (p. 21-28).
- **Tableaux / graphiques** : aucun. Uniquement des chiffres dans le texte.

### Chiffres (numéro de page PDF)
- p. 4 : proposition d'élargir à court terme le périmètre de la direction des grandes entreprises à la vérification approfondie de **1 600 entreprises** ; affecter une recette des finances au recouvrement des impôts dus par les grandes entreprises, qui représentent **70 % des ressources fiscales** (année et assiette non précisées).
- p. 5 : diagnostic : « 450 vérifications approfondies pour **9 610** entreprises dont le chiffre d'affaires dépasse **1 million de dinars** » (année non précisée).
- p. 6 (entreprises moyennes, cas du gouvernorat de Tunis) : **1 584** entreprises de services et d'activités non commerciales de chiffre d'affaires **entre 500 000 DT et 10 MDT**, et **421** entreprises industrielles et commerciales de CA **entre 3 et 10 MDT**, contribuant pour **322 MDT** aux ressources fiscales (le texte rattache 322 MDT à l'ensemble ; période non précisée). Proposition : service des impôts pour entreprises moyennes (SIME) à Tunis, puis généralisation.
- p. 10 : télédéclaration : **9 058** adhérents, **6 485** déclarants, montants recouvrés par ce canal = **83 %** du total des montants recouvrés (année non précisée ; l'expression « de l'ensemble des montants recouvrés » est lue ainsi sur la diapositive).
- p. 14 : **192** procédures formelles fiscales inventoriées.
- p. 15 : échec de l'expérience des bureaux d'accueil et d'orientation fiscale (**16** bureaux) et des centres de gestion intégrés (**5** centres).
- p. 16 : norme ISO 9001:2008 : **10** bureaux de contrôle fiscal ; label « Marhaba » (accueil) : **17** bureaux, application des conditions techniques à **15** recettes des finances.
- p. 22 : **1 600** agents chargés du contrôle fiscal, dont **450** chargés de la vérification approfondie (ces 450 coïncident avec le chiffre de la p. 5).
- p. 23 : un véhicule pour **16** agents.
- p. 24 : un micro-ordinateur pour **7** agents ; un poste réservé à l'accès au système d'information pour **3** agents.
- p. 27 : loyers des locaux : **1,5 MDT** par an (« 1.5 م د معلوم كراء مقرات »).
- p. 28 : propositions d'archivage électronique « sur le modèle du programme Jad ».

Pages sans chiffre : 2 (axes), 3, 8, 13, 17, 21 (titres d'axes), 7, 9, 11, 12, 18-20, 25, 26 (diagnostic/propositions qualitatifs : vérification, guichet virtuel, système documentaire, déclaration à distance, médiateur fiscal, comités de contribuables).

---

#### 2013-08_cnf_rf_5_ar.pdf

- **Titre exact (p. 1)** : « مشروع إصلاح المنظومة الجبائية بوزارة المالية » ; sous-titre : « حوصلة لأشغال فريق العمل المكلف المحلية باصلاح الجباية » (Synthèse des travaux du groupe de travail chargé de la fiscalité locale ; la préposition « المحلية » est mal placée dans le texte source). Ce n'est donc pas le titre des métadonnées PDF.
- **Date** : aucune sur le diaporama ; PDF créé le 27 août 2013.
- **Auteur** : groupe de travail « fiscalité locale » (« لجنة الجباية المحلية »), qui déclare (p. 3) avoir tenu **17 séances de travail** ; ministère des Finances (logo).
- **Pages** : 21. **Langue** : arabe. **Nature** : diaporama de synthèse. Pas de scan.
- **Plan** : I présentation générale (p. 3) ; II réformes liées aux textes, par taxe (p. 4-15) ; III réformes liées aux moyens et à caractère général (p. 16-17) ; IV mécanisme de transfert de recettes fiscales aux collectivités locales (p. 18-19) ; V travaux à venir de la commission (p. 20, coupée) ; p. 21 « merci ».
- Les sept éléments traités : taxe sur les immeubles bâtis, taxe sur les terrains non bâtis, taxe sur les entreprises, taxe sur les hôtels (« النزل »), taxe sur les licences des débits de boissons (« الاجازة »), taxe sur les spectacles, droits des marchés.
- **Tableaux** : aucun. Chiffres dans le texte. Les rendements sont en MDT (millions de dinars).

### Chiffres (numéro de page PDF)
- p. 3 : 17 séances de travail ; références comparées : France, Allemagne, Turquie, Portugal, Maroc, Mali, Bénin, Sénégal, Burkina Faso (p. 20).
- **Taxe sur les immeubles bâtis (p. 4-7)** :
  - rendement : **40 MDT en 2010**, **21 MDT en 2011**, **30 MDT en 2012** ;
  - taux de recouvrement : **22 %, 11 % et 14 %** du total des créances (inscrites aux rôles annuels + arriérés des années précédentes), respectivement 2010, 2011, 2012 ;
  - base actuelle (p. 5, rappel) : surface couverte x prix de référence du m² x **2 %** ; taux « selon le nombre de services fournis par la collectivité » entre **8 % et 14 %** (lecture partielle, texte superposé) ;
  - proposition (p. 6) : fusion avec la taxe nationale d'amélioration de l'habitat en une « taxe sur l'habitat » ; taux unifié abaissé d'un point : **11 %** au lieu de 12 % (**8 % TIB + 4 % FNAH**) et **13 %** au lieu de 14 % (**10 % TIB + 4 % FNAH**) ; (lecture : 8 % + 4 % = 12 %, 10 % + 4 % = 14 %) ;
  - p. 7 : remise de **10 %** sur les sommes dues pour paiement avant fin février ; pénalités de retard de **0,75 %** portées à **2 %** par mois restant de l'année ; utilisation des données STEG (électricité et gaz) ; la partie basse de la diapositive est coupée.
- **Taxe sur les terrains non bâtis (p. 8)** : rendement **15 MDT en 2010**, **12 MDT en 2011**, **14 MDT en 2012** ; taux de recouvrement annuels d'environ **18 %, 14 % et 14 %**, pour un total de créances d'environ **85 MDT, 89 MDT et 100 MDT**. Rappel de la règle : valeur vénale réelle x **0,3 %** (lecture partielle, « % 0,3 ») ; à défaut, taxe progressive au m² selon la densité des zones urbaines : **32, 95 ou 318 millimes** par m².
- **Taxe sur les entreprises (p. 9-10)** : rendement **111 MDT en 2010**, **93 MDT en 2011**, **137 MDT en 2012** (« de 111 MDT à 93 puis 137 », lecture de la couche texte et de l'image) ; propositions : exonérer le chiffre d'affaires à l'export de l'assiette ou le soumettre à la taxe, régime forfaitaire (montants fixés par arrêté, par tranches selon la nature de l'activité) pour les contribuables en régime d'évaluation « estimatif » (« النظام التقديري ») ; aucune valeur chiffrée de ce forfait.
- **Taxe sur les hôtels (p. 11)** : rendement **22 MDT en 2010**, **12 MDT en 2011**, **15 MDT en 2012**. Proposition : abroger le paragraphe III de l'article 40 du Code de la fiscalité locale (restitution de la taxe sur les immeubles bâtis en cas d'impossibilité d'obtenir la taxe hôtelière).
- **Taxe sur les débits de boissons (licence) (p. 12)** : rendement inférieur à **1 MDT par an**. Deux hypothèses : taxe inscrite dans le cadre des droits de licence ou suppression et intégration à la taxe sur les entreprises.
- **Taxe sur les spectacles (p. 13)** : faible rendement (inférieur à 1 MDT par an) selon la même mention ; proposition : intégrer à la fiscalité locale et fixer un plafond.
- **Droits des marchés (p. 14-15)** : rendement **62 MDT en 2010**, **36 MDT en 2011**, **44 MDT en 2012** (surtout droits de stationnement des véhicules et droit de criée) ; propositions : cadre juridique de la fiscalité des marchés, réforme des droits ; séparation du droit de stationnement.
- **Moyens (p. 16)** : proposition d'étendre le système d'information « Rafik » aux ressources de l'État ; plan comptable : taux de couverture en comptables spécialisés dans les finances locales **de 20 % à 80 %** environ (ancien taux de **20 %**) ; allongement du délai de prescription des créances locales de **4 à 10 ans**.
- **Garantie de l'État (p. 17)** : proposition de garantie de l'État couvrant **60 %** du rôle annuel de la taxe sur les immeubles bâtis, avec régularisation en cours d'année ; avis divergents des membres de la commission (certains jugent qu'elle contredit l'autonomie financière).
- **Transferts de recettes (p. 18-19)** : transfert de recettes fiscales aux collectivités locales (retenues à la source sur les salaires des agents des collectivités, part de la taxe sur la valeur ajoutée, droits d'immatriculation et de plus-value foncière, etc.) ; **aucun taux ni montant**. Constat conforme à la consigne : pas de TVA chiffrée.
- p. 20 (coupée) : travaux à venir : étude comparative (France, Allemagne, Turquie, Portugal, Maroc, Mali, Bénin, Sénégal, Burkina Faso) sur la fiscalité, avec examen des taxes sur l'expropriation et la propriété publique. Le bas de la diapositive est invisible.

---

#### 2013-08_cnf_rf_6_ar.pdf

- **Titre exact (p. 1)** : « مشروع إصلاح المنظومة الجبائية بوزارة المالية » ; sous-titre : « حوصلة لأشغال فريق العمل المكلف بدعم الشفافية الجبائية وقواعد المنافسة النزيهة ودعم ضمانات المطالبين بالأداء والتصدي لأعمال التهرب الجبائي » (Synthèse des travaux du groupe de travail chargé du soutien à la transparence fiscale et aux règles de concurrence loyale, du soutien aux garanties des contribuables et de la lutte contre les actes d'évasion fiscale).
- **Date** : aucune sur le diaporama ; PDF créé le 28 août 2013.
- **Auteur** : groupe de travail sur la transparence fiscale, la concurrence loyale, les garanties des contribuables et la lutte contre l'évasion, ministère des Finances (logo).
- **Pages** : 28. **Langue** : arabe. **Nature** : diaporama de synthèse (3 axes). Pas de scan.
- **Plan** : axe 1 soutien à la transparence et à la concurrence loyale (niveau politique p. 4, administration p. 5-6, contribuables p. 7-8, justice p. 9) ; axe 2 lutte contre l'évasion fiscale (p. 10-18) ; axe 3 garanties des contribuables (p. 19-28 : cadre législatif, phase de contrôle, phase de contentieux).

### Tableau chiffré (p. 11, « معطيات إحصائية », données statistiques)
Taux de dépôt des déclarations annuelles (la diapositive déborde en bas, la ligne 2011 du second tableau est invisible).

Tableau A : taux de dépôt des déclarations annuelles pour l'ensemble des contribuables enregistrés

| Année | Dans les délais | À fin 2012 |
|---|---|---|
| 2009 | 51,2 % | 75,7 % |
| 2010 | 40,5 % | 65,7 % |
| 2011 | 36,6 % | 50,8 % |

Tableau B : par catégorie (personnes morales ; professions non commerciales). Colonnes lues d'après les positions horizontales (ambiguïté de mise en page : l'attribution de chaque valeur à sa colonne est probable mais pas certaine) :

| Année | Personnes morales : dans les délais | Personnes morales : à fin 2012 | Professions non commerciales : dans les délais | Professions non commerciales : à fin 2012 |
|---|---|---|---|---|
| 2009 | 50 % | 80,7 % | 66,6 % | 88,3 % |
| 2010 | 44,7 % | 72,4 % | 57,7 % | valeur partiellement coupée (fragment visible « 81, ? ») |
| 2011 | ligne coupée, invisible | | | |

Le périmètre exact (ensemble des déclarants de l'IR, de l'IS ?) n'est pas précisé ; l'unité est le pourcentage de dépôt, pas un montant.

### Autres chiffres (numéro de page PDF)
- p. 6 : sanction pour défaut de désignation d'un commissaire aux comptes par les entreprises soumises à cette obligation : « non dissuasive », comprise **entre 2 000 DT et 20 000 DT**.
- p. 8 (paiements en espèces, comparaison) : en Tunisie, paiements en espèces sans limite ; proposition de plafonner les transactions en espèces à **30 000 DT**, puis de réduire progressivement à **20 000 DT** puis **10 000 DT**, avec sanction. Pays cités : France : interdiction de payer en espèces au-delà de **6 000 DT** (**2 000 DT** à partir de 2014) ; Belgique : **10 000 DT** (**6 000 DT** à partir de 2014) ; Maroc : **2 000 DT** ; Algérie : **1 000 DT** (valeurs en dinars tunisiens, sans date sauf mention 2014 ; l'indication « DT » est lue telle quelle).
- p. 7 : les pays cités pour l'accès aux comptes bancaires : France, Algérie, Maroc, Belgique.
- p. 9 : référence au Canada (juge fiscal).
- p. 12-14 : échange d'information et coopération internationale, sans chiffre ; télédéclaration par le bailleur d'immeubles (« المؤجر »), déclaration à distance rattachée au seul chiffre d'affaires (coupée).
- p. 15-18 : police fiscale ; sanctions pénales (moins de poursuites pénales, transfert d'une partie aux sanctions administratives) ; prix de transfert (p. 17 : limites du droit actuel contre le transfert de bénéfices par les prix) ; code de déontologie pour les agents du contrôle (p. 18). Propositions coupées en bas de plusieurs diapositives.
- p. 20-21 : unification des codes fiscaux ; visite sur place : autorisation du parquet, accompagnement d'un officier de police judiciaire.
- p. 22-24 : restitution d'excédents (priorité à l'excédent antérieur) ; vérification approfondie ouverte automatiquement dès la demande de restitution ; durée de la vérification approfondie ramenée à **3 mois** si elle porte sur une seule année ou un seul impôt ; l'administration doit répondre à l'opposition du contribuable en **6 mois au plus** ; délai de réponse du contribuable aux demandes d'éclaircissement : de **10 jours à 30 jours** (p. 24) ; délai de **2 mois** pour l'administration pour répondre.
- p. 25 : base de taxation d'office quand aucune déclaration n'est déposée (dernière déclaration déposée sans prise en compte des excédents, pertes et amortissements différés) ; litiges sur les droits d'enregistrement et la plus-value immobilière ; réévaluation des immeubles et actifs commerciaux.
- p. 26 : le médiateur fiscal et comités de conciliation ; **20 000** décisions de taxation (« قرارات التوظيف ») par an (« بلغت سنويا 20 ألف قرار » ; ligne partiellement coupée).
- p. 27-28 : contentieux fiscal local intégré au Code des droits et procédures fiscaux ; double degré de juridiction supprimé au profit du tribunal administratif ; représentation du contribuable ; droit d'être entendu devant la commission de l'article **74** du Code des droits et procédures fiscaux (p. 28 : saisine de cette commission pour les infractions passibles de peines corporelles).

Aucun chiffre sur le forfait, l'IRPP, l'IS, la TVA ; pas de graphique.

---

### Inventaire E — Conseil national de la fiscalité, novembre 2013 (six documents)

Répertoire : `/home/benjello/projets/tunisia-data/data/raw/minfinances/reforme_fiscale_2013_2014/`.
Lecture visuelle complète des diaporamas arabes (le texte extrait est désordonné). Aucune page n'est un scan sans texte : tous les PDF ont une couche texte (désordonnée pour l'arabe).

#### 2013-11_cnf_presentation_impots_directs.pdf

- Titre (p. 1) : « حوصلة لأشغال فريق العمل المكلف بإصلاح الضرائب المباشرة » = « Synthèse des travaux du groupe de travail chargé de la réforme des impôts directs » ; sous-titre « المجلس الوطني للجباية » (Conseil national de la fiscalité), « نوفمبر 2013 » ; logos Ministère des Finances / République tunisienne. Pages de contenu intitulées « خلاصة عمل اللجنة المكلفة بالإصلاح في مادة الضرائب المباشرة ».
- 25 pages, arabe, diaporama (p. 25 = « شكرا »). Date : novembre 2013. Auteur : groupe de travail « impôts directs » du CNF. Pas de scan.
- Structure : tableau à 4 colonnes par diapositive : Objectifs / Propositions / Principes généraux (équité, simplification, neutralité, transparence, modernisation, décentralisation ; coché = conforme, croix = non conforme, O = conformité discutable) / Incidence sur les recettes fiscales (« غ.م » = non mesuré / sans objet chiffré). Aucun tableau de séries, aucun graphique, aucune donnée sur le forfait.
- Axes : 1. révision de l'assiette (entreprise p. 2-4 ; personnes physiques p. 5-12 ; autres propositions p. 12-13) ; 2. révision des taux (entreprise p. 14-16 ; personnes p. 17) ; 3. modes de recouvrement (p. 18-19) ; 4. incitations fiscales liées aux impôts directs (p. 20-24).

### Chiffres (incidence annoncée sur les recettes, en MD = millions de dinars ; « نقص » = baisse, « مردود إيجابي » = gain)
IRPP (personnes physiques) :
- p. 5, déductions pour situation et charges de famille, révision périodique. Hypothèse 1 : chef de famille de 150 D à 250 D ; enfants à charge 100 D pour les quatre premiers ; parents à charge de 150 D à 250 D (avec renforcement des conditions de déduction) — incidence : baisse de 20,1 MD. Hypothèse 2 : chef de famille de 150 D à 300 D ; enfants 100 D par enfant sans limite aux quatre premiers ; parents de 150 D à 300 D — baisse de 27 MD. Maintien dans les deux cas de la déduction pour enfants poursuivant études supérieures et enfants handicapés.
- p. 6, déduction pour frais professionnels des salariés (aujourd'hui 10 %) : hypothèse 1, taux de 12 % pour toutes les tranches — baisse de 73,3 MD ; hypothèse 2, taux dégressif selon tranches de revenu (taux plus élevé pour les revenus faibles) — sans plafond : baisse de 66 MD ; avec plafond de 4 000 D : baisse de 56,7 MD.
- p. 7, BNC (professions non commerciales) au régime de l'assiette forfaitaire (« القاعدة التقديرية ») : abattement forfaitaire de 30 % ramené à 20 % — gain de 6,7 MD ; durée de bénéfice du régime fixée à 5 ans, + 3 ans supplémentaires sur justificatifs ; exclusion de certaines professions (avocats, experts-comptables, comptables, médecins, intermédiaires d'assurance, exploitants d'établissements d'enseignement privés) ; recoupements (levée du secret bancaire...). Les autres lignes : « غ.م ».
- p. 8, revenus fonciers : abattement forfaitaire de 30 % ramené à 20 % du montant des loyers encaissés (incidence non mesurée) ; obligation faite aux communes de communiquer périodiquement aux services fiscaux la liste des immeubles loués et de leurs propriétaires ; retenue à la source généralisée sur tout débiteur principalement de personnes physiques à l'assiette forfaitaire (BIC) avec déclaration simplifiée, sur le modèle de la retenue sur salaires.
- p. 9-10, plus-values de cession de titres et d'immeubles : hyp. 1, imposition au barème de l'IRPP comme les autres catégories ; hyp. 2, extension de l'IRPP à la plus-value immobilière (tous terrains sauf agricoles en zone agricole, terrains cédés aux promoteurs immobiliers) et régime des plus-values de titres selon la durée de détention : court terme (3 ans) intégrée au revenu global ; moyen/long terme taux de 10 % après un délai (3 ans) ; suppression de la plus-value sur titres jusqu'à 10 000 D (petits épargnants). Incidence non mesurée.
- p. 11, obligations déclaratives : obligation de présenter aux services fiscaux le système informatique et la base de données des achats/ventes/facturation ; suppression de l'obligation de déclaration d'existence pour toutes personnes physiques sauf salariés et titulaires de revenus de capitaux mobiliers et valeurs mobilières ; « caisse enregistreuse » obligatoire pour certaines catégories.
- p. 12-13, autres : imposition des associations et groupements de développement du secteur agricole et de la pêche avec exemption dans la limite de leur objet social ; catégorie spéciale pour revenus hors champ (plus-values mobilières, gains de jeux et loteries...) ; réexamen de l'exonération des coopératives de services agricoles (taux préférentiel). P. 13 : refus de déduction des charges non déclarées dans la déclaration de l'employeur (bailleur) ; refus de déduction des services rendus par des résidents de paradis fiscaux ; retenue à la source de 15 % sur sommes versées aux résidents de paradis fiscaux ; régime incitatif pour entreprises transparentes (restitution de l'excédent d'impôt sans contrôle préalable).
IS (sociétés) :
- p. 14, baisse du taux de l'IS de 30 % — hypothèse 1, en deux phases : de 30 % à 25 % avec imposition des bénéfices distribués à 5, 10 ou 15 % (soit sans égard à la qualité du bénéficiaire, soit en maintenant l'exonération des personnes morales résidentes), baisse de 116,3 MD ; puis 25 % à 20 %, incidence non mesurée.
- p. 15 : hypothèse 2, taux de 30 % à 20 % avec bénéfices distribués imposés à 5, 10 ou 15 % sans égard au bénéficiaire — baisse de 221,6 MD ; hypothèse 3, taux de 25 % ou 20 % avec impôt minimum de 0,2 % du chiffre d'affaires brut (y compris exportation), applicable à toutes les entreprises et donnant crédit d'impôt limité dans le temps pour les entreprises déficitaires — taux 25 % : baisse de 101,4 MD ; taux 20 % : baisse de 206,5 MD.
- p. 16 : extension du taux de 35 % (actuel) aux exploitants de grandes surfaces commerciales, fournisseurs d'accès Internet, concessionnaires automobiles, courtiers d'assurance et autres secteurs à marge élevée — hausse d'environ 3 MD ; assujettissement des entreprises exonérées au taux réduit de 10 % — gain de 85,4 MD.
- p. 17, barème IRPP : hyp. 1, première tranche du barème élargie de 1 500 D à 2 000 D avec redistribution du barème — baisse de 113,2 MD ; hyp. 2, tranche exonérée via déduction supplémentaire de 1 000 D de l'assiette pour les titulaires du SMIG dont le revenu net annuel ne dépasse pas 5 000 D — baisse de 35,1 MD ; ou déduction supplémentaire de 1 000 D pour titulaires du SMIG, salariés, retraités et rentiers dont le revenu net annuel ne dépasse pas 5 000 D plus déduction supplémentaire de 500 D — baisse de 19,2 MD ; indexation de la tranche exonérée sur le SMIG — baisse de 410 MD.
- p. 18 : retenue à la source sur intérêts de prêts payés aux établissements bancaires non résidents de 5 % à 10 % — gain de 1,8 MD ; fin de l'exonération des jetons de présence versés par sociétés totalement exportatrices à des non-résidents ; non-déductibilité des jetons de présence à la charge des sociétés versés à des non-résidents. P. 19 : exemption des pénalités de retard sur l'excédent d'impôt (écart acomptes) ; acomptes provisionnels étendus aux agriculteurs et titulaires de revenus fonciers ; taux de l'acompte sur importations de biens de consommation (« التسبقة ») ramené à 10 % ; révision de la liste des biens de consommation soumis ; assujettissement à l'acompte de certains intrants pour fabrication de produits finis.
- p. 20-24 (incitations) : révision des avantages du code de l'IRPP et IS ; suppression des avantages à l'exploitation/au réinvestissement pour entreprises installées hors de Tunisie, services d'hébergement d'étudiants et restauration, commercialisation de programmes immobiliers, bureaux d'étude et conseil fiscal, moins-values dues à l'abandon de l'option de souscription au capital (p. 20) ; maintien des avantages d'épargne : déduction de l'excédent des comptes d'épargne portée à 2 000 D par an (comptes spéciaux d'épargne et bons du Trésor) ; plafond déductible des dépôts en comptes d'épargne-investissement porté de 20 000 D à 50 000 D, comme les comptes d'épargne en actions (p. 21) ; revue du régime des sociétés d'investissement à capital de développement et fonds communs de placement à risque (p. 22) ; avantages pour plus-values de cession de titres, hors Bourse de Tunis, sous condition de bilan de l'investissement ; bénéfices d'exportation imposés au taux de 10 % dès 2014 avec définition unifiée de l'exportation — gain de 137 MD (p. 23) ; revenus de l'intermédiation internationale imposés à 10 % comme l'export ; compensation des avantages par crédit d'impôt (p. 24).
- Aucun chiffre du forfait, de recettes IRPP/IS globales, de nombre de contribuables.

#### 2013-11_cnf_presentation_impots_indirects.pdf

- Titre (p. 1) : « حوصلة لأشغال فريق العمل المكلف بإصلاح الضرائب غير المباشرة » = « Synthèse des travaux du groupe de travail chargé de la réforme des impôts indirects » ; CNF, novembre 2013. Pages de contenu : « خلاصة عمل اللجنة المكلفة بالإصلاح في مادة الضرائب غير المباشرة ».
- 15 pages, arabe, diaporama (p. 15 = « شكرا »), même tableau à 4 colonnes. Pas de scan. Un seul tableau chiffré (p. 12).
- Axes : 1. généraliser le champ de la TVA (p. 2-7) ; 2. taux de TVA (p. 8-10) ; 3. autres dispositions (p. 11-14).

### Contenu chiffré
- p. 2 : suppression des exonérations pour les acquisitions des établissements publics soumis à la TVA ; révision de l'exonération au niveau du chiffre d'affaires (rapport de proportionnalité) ; TVA généralisée à la vente en gros dans le secteur de l'alimentation générale, grossistes de médicaments et produits pharmaceutiques assujettis ; suppression du seuil minimum de chiffre d'affaires annuel pour l'assujettissement des détaillants (100 000 D).
- p. 3 : assujettis au régime forfaitaire (النظام التقديري) : deux options — ne pas assujettir les forfaitaires à la TVA (petits exploitants) ; ou assujettir une tranche déterminée selon un système simplifié et non d'après la marge bénéficiaire. Aucun chiffre.
- p. 4-7, production agricole et pêche : hyp. 1, maintien hors champ de la TVA ; hyp. 2, suppression des droits et taxes sur le chiffre d'affaires de ventes de produits agricoles et de la pêche, remplacés par la TVA à taux réduit, avec retenue à la source au niveau des marchés de gros / industriels (transformateurs de légumes et céréales), agriculteurs pouvant opter pour la TVA ; suppression de l'exonération du tableau « A » (n° 11) ; maintien d'une liste limitée d'exonérations liées aux prix (régime de fixation des prix, subvention) ; médicaments et produits pharmaceutiques au détail soumis à la TVA à taux réduit ; denrées alimentaires, boissons alcoolisées et produits sous homologation administrative des prix : fin des exonérations propres au détail.
- p. 8, taux : deux taux de TVA (taux normal et taux « réduit ») plus un taux « super réduit » : taux normal inchangé (le texte ne le chiffre pas) ; suppression des taux de 6 % et 12 % et application d'un taux réduit (entre 8 % et 10 %) à une liste limitée d'activités ; service soumis au taux normal : professions libérales, formation, services liés à l'informatique et à Internet.
- p. 9 : maintien du taux réduit proposé pour les opérations aujourd'hui à 6 %, sauf médicaments et produits pharmaceutiques et leurs intrants ; équipements soumis au taux normal à l'exploitation avec suspension de TVA à l'investissement ; taux « super réduit » pour une liste limitée (médicaments, produits pharmaceutiques et intrants, produits actuellement exonérés dont l'assujettissement est prévu).
- p. 10 : suppression totale de la majoration de l'assiette de TVA à 25 % (importations par non-assujettis sauf État, collectivités locales et établissements publics administratifs ; produits importés de la liste du décret n° 477 du 3 mars 2003 ; acquisitions des non-assujettis industriels, grossistes et artisans).
- p. 11 : déduction de la TVA sur factures conformes ; sanctions proportionnées ; suppression des causes de crédit de TVA (compensation avec autres droits, unification de la retenue, délais de restitution).
- p. 12, retenue à la source de la TVA (« الخصم من المورد ») : réduction par étapes de 50 % jusqu'à suppression, avec taux de 30 %, 25 % ou 20 %. Tableau « incidence de la baisse du taux de retenue » (montants en millions de dinars ; montant de retenue 2012 : 298,9 MD) :

| taux de retenue | montant de la retenue | incidence sur le montant de TVA payé | incidence sur le montant d'excédent |
|---|---|---|---|
| 30 % | 179,321 | 45,11 | -74,4 |
| 25 % | 149 | 57,9 | -91,4 |
| 20 % | 119,5 | 71,6 | -107,7 |

- p. 13 : dispositif d'incitation à la déclaration à distance ; sanctions proportionnées, aggravées pour fraude fiscale et infractions de facturation ; assujettissement des secteurs non assujettis à la TVA en remplacement des autres droits adossés au chiffre d'affaires ; transfert éventuel de la TVA sur les secteurs directement vers le financement de la caisse.
- p. 14 : droit de consommation (« المعلوم على الاستهلاك ») : suppression des dispositions fixant les taux pour boissons alcoolisées et vin (« الخمور والجعة ») ; révision de la liste des produits soumis ; non-soumission de certains produits parallèlement à la généralisation de la TVA ; révision des taux appliqués à certains produits. Aucun taux chiffré.

#### 2013-11_cnf_presentation_modernisation_administration.pdf

- Titre (p. 1) : « حوصلة لأشغال فريق العمل المكلف بتعصير إدارة الجباية » = « Synthèse des travaux du groupe de travail chargé de la modernisation de l'administration fiscale » ; CNF, novembre 2013. Pages de contenu : « خلاصة عمل اللجنة المكلفة بتعصير إدارة الجباية ».
- 21 pages, arabe, diaporama (p. 21 = « شكرا »). Tableau à 4 colonnes (ici « nature du changement » : organisation et opérations, système d'information, infrastructure et communication, gouvernance et indicateurs de performance). Pas de scan. Très peu de chiffres, aucun tableau de séries.
- Axes : 1. modernisation du cadre organisationnel (p. 2-5) ; 2. services à distance (p. 6-9) ; 3. développement des services fiscaux (p. 10-12) ; 4. communication entre l'administration et les contribuables (p. 13-14) ; 5. moyens de travail (p. 15-20).

### Chiffres et éléments utiles
- p. 2 : création d'une « Direction générale des impôts » (هيئة عامة للأداءات) regroupant progressivement les missions fiscales, dotée plus tard d'autonomie administrative et financière ; structures de gestion des risques, de coopération internationale et d'échange d'informations, d'enquêtes et de recoupements ; unification des fonctions législation / contrôle / recouvrement ; guichet unique.
- p. 3, grandes entreprises : extension de la direction des grandes entreprises pour couvrir les vérifications approfondies de « 1 600 entreprises » ; création d'une recette des finances affectée au recouvrement des impôts dus par les grandes entreprises, qui représentent « 70 % des ressources fiscales » ; doublement des brigades de vérification ; cellule de programmation et de suivi ; cellule de suivi du recouvrement des dettes fiscales lourdes ; confier les enquêtes fiscales à une structure spécialisée de la DG des impôts.
- p. 4, moyennes entreprises : création de services d'impôts pour les moyennes entreprises (SIME) ; direction des moyennes entreprises centralisée à l'échelle du gouvernorat de Tunis, sur le modèle de celle des grandes entreprises, puis généralisation après évaluation. Objectif : améliorer la contribution des petites et moyennes entreprises aux recettes fiscales.
- p. 5 : restructuration des centres régionaux et bureaux de contrôle des impôts ; recettes des finances spécialisées dans le recouvrement rattachées aux centres régionaux.
- p. 6-8, espace virtuel : compte fiscal en ligne, dépôt de demandes de restitution d'excédent, dématérialisation des attestations, dépôt à distance des déclarations (déclaration de l'employeur) ; « liasse fiscale » unique en forme d'états financiers unifiés adossés au système comptable (p. 7), en deux phases ; extension de l'obligation de télédéclaration et télépaiement à d'autres catégories (dont forfaitaires, salariés) (p. 8) ; étude de l'accès du ministère des Finances aux marchés publics électroniques.
- p. 9 : refonte de la base documentaire. p. 10 : poursuite de l'inventaire des procédures formelles fiscales : « 192 procédures » recensées ; accélération des décisions du Conseil des ministres relatives au projet « simplification des procédures fiscales et domaniales ». p. 11 : revue du dispositif d'assistance ; échec des bureaux d'accueil et d'orientation fiscale et des centres de gestion intégrés. p. 12 : stratégie qualité. p. 13-14 : communication ; sondages d'opinion périodiques, boîtes à suggestions, « comités des usagers », rôle du « médiateur fiscal » (الموفق الجبائي). p. 15-20 : statut particulier des agents des impôts ; formation ; équipement informatique et mobile pour les brigades de vérification ; véhicules ; système d'information (interconnexion avec ministère de l'Intérieur, Poste, registre foncier, domaines de l'État) ; archivage électronique (programme « Jad ») ; séparation des fonctions de contrôle et d'établissement du dossier de contrôle ; modèle électronique unifié de rapports de contrôle.
- Aucun chiffre sur le forfait, IRPP, IS, TVA.

#### 2013-11_cnf_presentation_fiscalite_locale.pdf

- Titre (p. 1) : « حوصلة لأشغال فريق العمل المكلف بإصلاح الجباية المحلية » = « Synthèse des travaux du groupe de travail chargé de la réforme de la fiscalité locale » ; CNF, novembre 2013. En haut de la p. 1, deux annexes annoncées (liens) : « ملحق عدد 1 : أعضاء لجنة الجباية المحلية » (annexe 1 : membres de la commission de la fiscalité locale) et « ملحق عدد 2 : المعاليم المحلية الجاري بها العمل » (annexe 2 : taxes locales en vigueur) — ces annexes ne font pas partie du PDF.
- 24 pages, arabe, diaporama (p. 24 = « شكرا »). P. 2-3 : schémas (cadre du plan de renforcement de la décentralisation ; programme de réforme de la fiscalité locale en trois volets : voies de développement des ressources, domaines de réforme les plus à même de donner de l'autonomie aux collectivités, analyse du système des transferts de l'État). P. 4-23 : tableau à 4 colonnes. Pas de scan.
- Axes : 1. codification de la matière fiscale locale (p. 4) ; 2. réformes liées aux moyens et à la nature générale (p. 5-7) ; 3. réformes de nature textuelle (p. 8-20) ; 4. transfert de prélèvements fiscaux au profit des collectivités (p. 21-23).

### Chiffres
- p. 4 : trois hypothèses de codification : (1) intégrer la fiscalité locale dans un code de la fiscalité locale (loi), (2) restructurer la fiscalité locale au sein du code des droits et procédures / code général de l'impôt (« المجلة العامة للأداءات ») ; (3) conserver le code de la fiscalité locale en ne gardant que la matière fiscale locale. Aucun chiffre.
- p. 5, renforcer les recettes des finances (« قباضات ») chargées de la gestion financière locale : hypothèse 1, relèvement progressif, par périodes de cinq ans, de la couverture en comptables spécialisés dans la gestion des finances locales de « 20 % à 80 % » ; incidence indiquée : « − 600 000 D par an » avec la mention « 15 000 D × 200 receveurs sur 5 ans » (lecture : 200 receveurs, 15 000 D chacun sur 5 ans, soit 600 000 D par an ; c'est une lecture, l'extraction est désordonnée) ; hypothèse 2 : intégrer le receveur dans l'organigramme de chaque collectivité (incidence non mesurée).
- p. 6 : généraliser le système « Rafik » aux ressources de l'État incluant les ressources reversées aux collectivités ; répartition des compétences par concertations sectorielles (éducation, santé).
- p. 7 : marge de manœuvre sur l'assiette de certaines taxes ; accès des communes aux informations sur les contribuables ; allongement de la prescription du recouvrement des dettes locales de 4 ans à 10 ans (conformité « discutable »).
- p. 8-10, taxe sur les immeubles bâtis (TIB) : barème progressif des prix de référence au m² bâti par tranche de surface couverte, à l'instar du barème de l'impôt sur le revenu (p. 8) ; lier les services rendus par les collectivités à l'obtention du quitus de paiement de la TIB et de la taxe sur les terrains non bâtis (p. 9) ; réduction de 10 % des montants dus pour ceux qui payent avant fin février, et relèvement de l'intérêt de retard de 0,75 % à 2 % par mois restant dans l'année (p. 9) ; utiliser la base de données de la STEG pour déterminer les assujettis (p. 10).
- p. 11, fusion de la TIB et de la contribution au Fonds national d'amélioration de l'habitat (FNAH) en une taxe unique dite « taxe sur l'habitation » ; le taux unifié est abaissé d'un point : 11 % au lieu de 12 % (TIB 8 % + FNAH 4 %) ; 13 % au lieu de 14 % (TIB 10 % + FNAH 4 %) ; 15 % au lieu de 16 % (TIB 12 % + FNAH 4 %) ; 17 % au lieu de 18 % (TIB 14 % + FNAH 4 %).
- p. 12 : taxe sur les terrains non bâtis (TTNB) : calcul sur la valeur vénale réelle, abandon du système de la densité d'habitat, en conservant le taux actuel ; taxe sur les établissements (TCL) : régime spécial pour le régime forfaitaire (montants forfaitaires fixés par décret selon tranches par nature d'activité), maintien du minimum pour les contribuables du régime réel sur base de la surface couverte. P. 13 : intégrer le chiffre d'affaires à l'export dans l'assiette de la taxe sur les établissements ; « taxe sur la résidence » (TH, « المعلوم على النزل ») : retrait de l'alinéa III de l'article 40 du code de la fiscalité locale (restitution en cas de non-obtention de la taxe sur l'hébergement). P. 14 : redevances de marchés ; regrouper les droits dans « المعلوم العام للوقوف والخدمات » ; séparer la taxe de stationnement. P. 15 : taxe de licence des débits de boissons (DL) : hypothèse 1, l'intégrer aux taxes locales sur la base du recensement des locaux ; hypothèse 2, la supprimer et l'intégrer à la taxe sur les établissements. P. 16 : taxe sur les spectacles. P. 17 : taxe d'occupation temporaire de la voie publique. P. 18 : taxe de publicité (contrats de concession : libre choix du mode de licence). P. 19 : taxe d'abattage et de contrôle sanitaire. P. 20 : taxe d'occupation du domaine public maritime (modification de l'article 23 de la loi n° 73 de 1995) ; taxe d'octroi de terrain dans les cimetières. Aucun chiffre sur les recettes.
- p. 21, objectif 2015-2019 : amener les ressources des collectivités locales à environ « 8 % » des ressources du budget de l'État, ou « 4 % » du PIB en 2019.
- p. 22 : proposition de transferts fiscaux au profit des collectivités (proportions non remplies — le texte porte des pointillés) : retenues à la source de l'impôt sur les agents des collectivités ; part annuelle de l'impôt sur le revenu des personnes résidant dans le ressort territorial (« …… % du revenu de l'année précédente ») ; part annuelle de la TVA (« …… % en 2015 et 2016 à …… % en 2017 et 2018 pour atteindre …… % à partir de 2019 ») ; part des recettes des péages ; « …… % » des droits d'enregistrement ; part de l'impôt sur la plus-value immobilière. Les pourcentages sont laissés en blanc dans le diaporama.
- p. 23 : fonds de coopération entre collectivités ; mécanisme de répartition des crédits entre collectivités via un « fonds régional et local de développement » ; critères de répartition.

#### 2013-11_cnf_presentation_26-11-2013.pdf

- Titre (p. 1) : « حوصلة لأشغال فريق العمل المكلف بدعم الشفافية الجبائية وقواعد المنافسة النزيهة والتصدي لأعمال التهرب الجبائي ودعم ضمانات المطالبين بالأداء » = « Synthèse des travaux du groupe de travail chargé du renforcement de la transparence fiscale et des règles de concurrence loyale, de la lutte contre l'évasion fiscale et du renforcement des garanties des contribuables » ; CNF, novembre 2013 (nom de fichier : 26-11-2013).
- 20 pages, arabe, diaporama (p. 20 = « شكرا »). Tableau à 4 colonnes. Pas de scan. Un seul écran de statistiques (p. 7).
- Axes : transparence fiscale et concurrence loyale (niveaux politique, administration, contribuables : p. 2-7) ; lutte contre l'évasion fiscale (p. 8-12) ; garanties des contribuables (en cours de contrôle, de vérification, de taxation d'office, en contentieux : p. 13-19).

### Chiffres
- p. 6, plafond des transactions en espèces : fixer un plafond de 30 000 D et le réduire progressivement à 20 000 D puis 10 000 D, avec sanction. Comparaisons internationales (en dinars, convertis dans le diaporama) : France : paiement en espèces interdit au-delà de 6 000 D (2 000 D à partir de 2014) ; Belgique : 10 000 D (6 000 D à partir de 2014) ; Maroc : 2 000 D ; Algérie : 1 000 D.
- p. 7, « Données statistiques » : taux de dépôt des déclarations annuelles. Pour tous les inscrits (dans les délais / à fin 2012) : 2009 : 51,2 % / 75,7 % ; 2010 : 40,5 % / 65,7 % ; 2011 : 36,6 % / 50,8 %. Pour les personnes morales (dans les délais / à fin 2012) : 2009 : 50 % / 80,7 % ; 2010 : 44,7 % / 72,4 % ; 2011 : 40,3 % / 62,2 %. Pour les professions non commerciales (dans les délais / à fin 2012) : 2009 : 66,6 % / 88,3 % ; 2010 : 57,7 % / 81,3 % ; 2011 : 55,4 % / 71,5 %. (Colonnes lues sur l'image ; le périmètre « inscrits » n'est pas précisé davantage.)
- p. 2 : déclaration de patrimoine des responsables politiques et hauts cadres ; preuve du respect des obligations fiscales pour se porter candidat à des mandats et aux hautes fonctions ; publication des états financiers des collectivités locales. P. 3 : unification des procédures, formation, code unique des droits et obligations fiscales (« مجلة موحدة تنظم جميع الأداءات »), simplification et limitation des régimes dérogatoires, sanctions de la corruption. P. 4 : sanction du défaut de désignation d'un commissaire aux comptes ; rôle d'un comité de contrôle de la qualité des travaux des commissaires aux comptes. P. 5 : droit de communication étendu aux comptes ouverts auprès des intermédiaires en Bourse (droit d'accès direct aux établissements financiers en cas de refus du contribuable de produire ses relevés). P. 8-12 : collecte d'informations et coopération interne, déclaration à distance, création d'une police fiscale, dépénalisation partielle et transfert de contraventions pénales vers le domaine administratif, coopération internationale (échange d'informations, prix de transfert). P. 13-19 : garanties de la vérification sur place (autorisation du parquet, accompagnement d'un officier de police judiciaire) ; durée de vérification approfondie limitée à 3 mois quand elle porte sur un an ou un seul impôt (p. 15) ; obligation pour l'administration de répondre à l'opposition du contribuable dans un délai maximal de 6 mois (p. 15) ; allongement du délai de réponse du contribuable aux demandes d'éclaircissements de 10 jours à 30 jours (p. 15) ; délai de deux mois pour que l'administration se prononce sur la réponse (p. 16) ; en taxation d'office : limitation du pourcentage de suspension de l'exécution à 10 % ou 15 % du paiement comptant (hypothèse 2, p. 18) ; représentation du contribuable par un conseil fiscal ou un avocat si la taxation d'office dépasse 100 000 D (p. 19).
- Aucun chiffre sur le forfait, l'IRPP, l'IS, la TVA (hors cas ci-dessus).

#### 2013-11_cnf_ar_discours_ministre.pdf

- Titre (p. 1) : « كلمة السيّد وزير المالية في افتتاح اجتماع المجلس الوطني للجباية » = « Allocution du Ministre des Finances à l'ouverture de la réunion du Conseil national de la fiscalité » ; République tunisienne, Ministère des Finances ; 28-29 novembre 2013, hôtel Ramada Plaza, Gammarth (« قمرت »).
- 7 pages, arabe, discours (texte dactylographié). Pas de scan ; mais la couche texte extraite est corrompue (glyphes mal encodés : « الجمهىريت التىنسيت », mots déformés), à ne pas utiliser — la lecture visuelle est nécessaire (et a été faite). Le nom du ministre ne figure pas dans le document : l'attribution à Elyès Fakhfakh mentionnée dans la demande n'est pas vérifiable dans ce PDF (le discours salue le chef du gouvernement « علي العريض », et la date est novembre 2013 : à vérifier par ailleurs, Elyès Fakhfakh ayant quitté le ministère des Finances en 2012 d'après mes connaissances, hors du document).
- Contenu : adresse au chef du gouvernement (Ali Laarayedh), aux membres de l'Assemblée nationale constituante, du gouvernement, aux représentants d'organisations nationales et internationales et aux membres du CNF (p. 2) ; la réforme fiscale comme projet national dans le cadre d'une politique économique et sociale (p. 3, citation du projet de constitution : « l'acquittement de l'impôt et la prise en charge des charges publiques est un devoir selon un système juste et équitable ») ; rôle central de la fiscalité (p. 5) : (1) financement du budget de l'État, où les ressources fiscales (hors avantages fiscaux) représentent « environ 80 % » des ressources propres et permettent de couvrir « les deux tiers (2/3) » des interventions de l'État hors dette publique (fonctionnement et développement) ; (2) investissement et implantation dans les régions intérieures et à l'export ; (3) justice sociale, répartition équitable des richesses, lutte contre la fraude, équilibre entre régions. P. 5-6 : méthode participative, « au moins 200 séances de travail » pendant 6 mois avec organisations nationales, experts, universitaires et société civile ; consultation nationale et régionale prévue après ce rendez-vous (p. 6) ; appel à ne pas laisser la réforme « de l'encre sur du papier » (p. 6) ; remerciements (p. 7).
- Aucun chiffre sur le forfait, l'IRPP, l'IS, la TVA, le nombre de contribuables.

---

#### 2013-11_cnf_rapport_synthese_groupes_travail.pdf

**Identification**
- Titre (p. 1) : « République Tunisienne — Projet de réforme du système fiscal tunisien — Rapport de synthèse des travaux des groupes de travail », mention « DRAFT », « En collaboration avec » (logo MS Louzir, membre de Deloitte Touche Tohmatsu ; pied de page « © 2013 MS Louzir membre de Deloitte Touche Tohmatsu »), « Novembre 2013 ».
- Métadonnées PDF : créé avec PowerPoint 2010 le 3 mars 2014 ; 153 pages ; français ; diaporama de synthèse (type rapport projeté) sous la direction du ministère des Finances, validé par le Conseil national de la fiscalité (CNF) d'après p. 19.
- Auteur : ministère des Finances avec le cabinet MS Louzir/Deloitte. Six groupes de travail (p. 19) : impôts directs, impôts indirects, fiscalité locale, transparence-compétitivité-lutte contre l'évasion, régime forfaitaire, modernisation de l'administration (« plus de 200 ateliers »).
- Couche texte correcte sur toutes les pages : aucun scan à océriser. Tableaux lus visuellement (pp. 50-63, 65-91).
- Structure : 1 Introduction (p. 3-4) ; 2 Executive Summary (p. 5-17) ; 3 Méthodologie (p. 18-21) ; 4 Diagnostic FMI/BM/USAID/SFI et recommandations (p. 22-47) ; 5 Synthèse des travaux et recommandations avec colonne « Impact / Recettes fiscales » (p. 48-128) ; Annexes : plans de mise en oeuvre (p. 129-153).

### A. Régime forfaitaire (priorité a)

Chiffres du diagnostic :
- p. 10 (Executive Summary, « Révision du régime forfaitaire et intégration de l'économie informelle ») : « leur contribution aux recettes fiscales reste faible (60 % des inscrits au fichier contribuent à concurrence de 0,2 % des recettes fiscales, 45 000 interventions des services de contrôle avec un rendement annuel de 12 millions de dinars) ». Année et périmètre non précisés dans le texte.
- p. 10 : pas de conditions légales d'éligibilité rattachées à l'exercice, certains contribuables bénéficient indéfiniment du régime ; difficulté d'obtenir des informations fiscales ; obligations des forfaitaires ne permettant pas de déterminer le CA avec précision.
- p. 25 (diagnostic) : « L'assiette des BIC se trouve fortement érodée par le recours massif au système simplifié et libératoire du Régime Forfaitaire » ; « La répartition des forfaitaires en termes de CA et entre les secteurs d'activités montre un potentiel de recettes non négligeable ... permettant l'identification des faux forfaitaires ». Aucune répartition chiffrée n'est donnée dans ce document.
- p. 24 : BNC des professions libérales, option de fiscalisation sur la base d'un bénéfice forfaitaire « égal à 70 % des recettes brutes réalisées » (soit déduction forfaitaire de 30 %).
- p. 8 (Executive Summary, IRPP) : BNC au forfait d'assiette « faible contribution dans la recette fiscale (3 % de l'IRPP) » ; « 60 % optent pour le forfait d'assiette » ; revenus fonciers (forfait de 30 %) « faible contribution dans la recette fiscale (1 % de l'IRPP) ».
- p. 26 : le régime forfaitaire est cité parmi les activités exonérées de prélèvements à la source (avec l'exportation) ; p. 28 diagnostic TVA.
- p. 38 (mesure proposée par les organismes internationaux) : « Renforcer le contrôle du système du forfait » ; p. 38-39 : utiliser les informations de l'assurance sociale pour l'assiette des professions non commerciales ; « Réviser la possibilité de détermination forfaitaire ».
- p. 42 : étendre le seuil d'assujettissement à la TVA prévu pour les commerçants (100 000 DT) à l'ensemble des activités et entreprises.

Mesures sur le forfait d'assiette BNC et revenus fonciers (tableau Impôts directs, colonne « Impact / Recettes fiscales »), pp. 53 et 131-132 :
- p. 53, mesure 5 « Amélioration du rendement des BNC au régime de forfait d'assiette » : baisse de la déduction forfaitaire de 30 % à 20 % ; limitation de la période de bénéfice à 5 ans avec extension possible de 3 ans sous conditions (faiblesse des revenus, difficulté de tenir une comptabilité) ; exclusion des avocats, experts comptables, comptables, médecins, courtiers en assurance, exploitants d'établissements d'enseignement privé ; amélioration des moyens de recoupement (levée du secret bancaire...). **Impact : « Rendement positif de 6,7M dt »** (lu sur l'image p. 53, rattaché à la première ligne, la baisse de 30 % à 20 %). Les autres lignes : NA.
- p. 53-54, mesure 6 « Améliorer le rendement des revenus fonciers » : baisse de la déduction forfaitaire de 30 % à 20 % du montant des recettes ; obligations supplémentaires (liste des immeubles loués fournie par les municipalités) ; extension de la retenue à la source sur les loyers à tous les redevables, y compris BIC au régime forfaitaire. Impact : NA.

Tableau « Régime forfaitaire » (pp. 64-75, colonne Impact : NA partout, aucun chiffre) :
- p. 65 mesure 1 (court terme) : exclure certaines activités du forfait (quincaillerie, matériaux de construction et sanitaire..., importance des capitaux, des moyens d'exploitation, lieu d'implantation : chefs-lieux de gouvernorat, centres commerciaux) ; liste fixée par décret en accord avec les structures professionnelles.
- p. 65-66 mesure 2 : dispenser du formalisme fiscal les personnes à « revenus de survie » (critères : liste d'activités fixée avec les représentants des professionnels ; revenu ne dépassant pas le SMIG) ; prise en charge par les collectivités locales avec contribution libératoire.
- p. 66 mesure 3 : augmentation du minimum d'impôt et harmonisation avec l'impôt minimum du régime réel (aucun montant donné).
- p. 66-67 mesure 4 (moyen terme) : hypothèse 1, régime forfaitaire contractuel participatif de durée déterminée (indicateurs : superficie du local, nombre d'employés, marge bénéficiaire) ; hypothèse 2, impôt annuel fixe « droit de patente » payable durant les 6 premiers mois de chaque année, impôt sur le revenu définitif calculé par pourcentage sur recettes moins dépenses, impôt exigible non inférieur au droit de patente ; commission administration-UTICA.
- p. 67 mesure 5 : généraliser la TVA aux petits exploitants hors « revenus de survie » ; court terme : prestataires de services seulement ; moyen terme : le reste des forfaitaires, hors activités à homologation administrative des prix.
- p. 68 mesure 6 : réviser les taux d'imposition calculés sur le CA selon activités/marges (hypothèse 1) ou, à moyen terme, remplacer par un régime fondé sur le revenu selon marges bénéficiaires et imposition à l'IR selon le barème (hypothèse 2).
- p. 68-69 mesures 7-8 : facturation obligatoire au-delà d'un montant à déterminer ; matricule fiscal comme identifiant unique ; base de données unique DGI-CNSS ; caisses enregistreuses ; carnet de bord pour les transporteurs.
- p. 69 mesure 9 (recouvrement) : paiement obligatoire en deux tranches ; doublement du montant de l'impôt, minimum d'impôt compris, pour déclaration hors délai ; paiement des forfaitaires traitant avec l'État subordonné à la régularisation ; certificat de visite technique des véhicules subordonné au dépôt des déclarations annuelles.
- pp. 70-72 mesures 10-12 : intégration de l'économie informelle (dispense de régularisation du passé, prise en charge d'une partie des cotisations sociales, commission technique, police fiscale, zones franches frontalières, art. 71 du Code des douanes, art. 26 loi n° 95-46 du 15/05/1995).
- pp. 73-75 mesures 13-19 : suppression de l'interlocuteur unique à la recette des finances ; services fiscaux des moyennes entreprises (SIME) « surtout pour les forfaitaires » ; prescription allongée en cas de fraude ; interdiction des factures préétablies vendues en librairie ; régime réel simplifié ; centres de gestion intégrés et « certification fiscale » ; sanctions plus dissuasives.
- p. 77 (TVA) : suppression du seuil d'imposition de 100 000 dt de chiffre d'affaires annuel des détaillants ; forfaitaires : non-soumission des petits exploitants, soumission d'une catégorie à un régime d'assujettissement simplifié sans TVA sur la marge.
- p. 91 mesure 11 (fiscalité locale) : TCL appliquée aux forfaitaires par montants prédéterminés selon la nature d'activité ; p. 12 et 143 : transfert progressif de la gestion du régime forfaitaire aux collectivités locales.
- p. 137 et suivantes (annexe plan de mise en oeuvre) : reprend les mêmes mesures du forfait avec mécanisme (décret, code IRPP/IS art. 44...) et délais, sans chiffre de recettes.
- Non trouvé dans ce document : nombre de forfaitaires, recettes de l'impôt forfaitaire, ventilation par activité ou tranche de CA, minimum d'impôt en dinars, montants de l'impôt (hors les trois chiffres ci-dessus : 60 % / 0,2 % / 45 000 / 12 MD).

### B. IRPP (priorité b)

Colonne « Impact / Recettes fiscales », tableau Impôts directs (pp. 50-62), valeurs exactes recopiées de l'image (notations d'origine « M dt », « Mdt ») :
- p. 51-52, mesure 3 « Harmonisation des déductions (situation et charges de famille) » :
  - 1re hypothèse : chef de famille 150 dt -> 250 dt ; enfants à charge 100 dt pour les quatre premiers ; parents à charge 150 dt -> 250 dt avec amélioration des conditions de déduction. Impact : **baisse de 20.1 M dt** (p. 51).
  - 2e hypothèse : chef de famille 150 dt -> 300 dt ; enfants 100 dt par enfant sans limiter aux quatre premiers ; parents à charge 150 dt -> 300 dt. Impact : **baisse de 27 M dt** (p. 52). Les déductions pour enfants poursuivant des études supérieures et enfants handicapés inchangées dans les deux hypothèses.
- p. 52, mesure 4 « Déduction des frais professionnels » :
  - 1re hypothèse : taux de 12 % pour toutes les tranches. Impact : **baisse de 73,3 M dt**.
  - 2e hypothèse : taux dégressif selon la tranche de revenu. Impact : « Si la déduction n'est pas plafonnée : baisse de 66M dt ; si la déduction est plafonnée à 4000 dt : baisse de 56,7M dt ».
- p. 59, mesure 13 « Harmonisation des taux de l'impôt sur le revenu » :
  - 1re hypothèse : première tranche du barème de 1500 dt -> 2000 dt avec harmonisation des autres tranches. Impact : **baisse de 113.2 M dt**.
  - 2e hypothèse, première variante : élargissement de la tranche inférieure exonérée par extension de la déduction supplémentaire de 1000 dt prévue pour les smigards à toutes les personnes physiques dont le revenu annuel net ne dépasse pas 5000 dt. Impact : **baisse de 35,1M dt**.
  - 2e hypothèse, seconde variante : déduction supplémentaire de 1000 dt pour les smigards + déduction supplémentaire de 500 dt aux salariés et pensionnaires dont le revenu annuel net ne dépasse pas 5000 dt. Impact : **baisse de 19,2M dt**.
  - Fixation de la tranche exonérée dans la limite du SMIG (indexation au SMIG). Impact : **baisse de 410 M dt**.
  - (Attribution des quatre impacts aux quatre sous-lignes lue sur l'image p. 59 ; les lignes sont dans l'ordre 113.2 / 35,1 / 19,2 / 410.)
- p. 8 : diagnostic « Inadéquation des taux d'IRPP avec l'augmentation des prix et les faibles revenus » ; p. 23 : barème non révisé depuis plus de 20 ans, « le SMIG dépasse le seuil de la première tranche d'imposition ».
- p. 24 : revenus d'intérêt : prélèvement à la source de 20 % ; dividendes totalement défiscalisés.
- p. 53-55, mesure 7 (plus-values, aucun impact chiffré) : hypothèse 1, imposition au barème ; hypothèse 2 : élargissement de l'impôt sur la plus-value immobilière à tous les terrains sauf agricoles en zone agricole et aux terrains vendus aux promoteurs ; plus-value sur titres : à court terme (3 ans) intégrée au revenu global, à moyen/long terme taux de 10 % après plus de 3 ans de détention ; suppression de l'abattement de 10 000 dt sur la plus-value de cession de titres.
- p. 61 mesure 21 : plafond de déduction des intérêts des comptes spéciaux d'épargne et bons du Trésor porté à 2000 dt ; déduction des comptes d'épargne investissement de 20 000 dt à 50 000 dt.
- p. 60 : retenue à la source sur intérêts d'emprunts aux établissements bancaires non-résidents de 5 % à 10% (impact ci-dessous, rubrique IS).
- Pas de série de recettes IRPP (hors 3 % et 1 % de l'IRPP ci-dessus), pas de répartition salariés / non-salariés chiffrée.

### C. IS (priorité c)

Colonne Impact :
- p. 57, mesure 11 « Baisse du taux de l'IS avec imposition des dividendes » (taux actuel indiqué 30 %) :
  - 1re hypothèse, 1re phase : 30 % -> 25 % et dividendes imposés à 5 %, 10 % ou 15 % (indépendamment du bénéficiaire, ou en maintenant l'exonération des personnes morales résidentes). Impact : **baisse de 116,3M dt**.
  - 1re hypothèse, 2e phase : 25 % -> 20 %. Impact : NA.
  - 2e hypothèse : 30 % -> 20 % et dividendes à 5 %, 10 % ou 15 % indépendamment du statut du bénéficiaire. Impact : **baisse de 221,6M dt**.
- p. 58, 3e hypothèse : taux de 25 % ou 20 % avec minimum d'impôt de 0,2 % du chiffre d'affaires global (y compris exportation) applicable à toutes les sociétés, crédit d'IS limité dans le temps pour les sociétés déficitaires. Impact : « Pour un taux d'IS de 25 % : baisse de 101,4Mdt ; pour un taux d'IS de 20 % : baisse de 206,5Mdt ».
- p. 58, mesure 12 : élargissement du taux de 35 % aux exploitants de grandes surfaces, fournisseurs de services internet, concessionnaires automobiles, courtiers en assurance et autres activités à marge élevée. Impact : **augmentation de 3Mdt**. Soumission des entreprises exonérées à l'IS à un taux réduit de 10 %. Impact : **rendement positif de 85,4Mdt**.
- p. 63, mesure 21 : soumission à l'IS à 10 % des bénéfices provenant de l'exportation à partir de 2014 et unification de la notion d'exportation. Impact : **augmentation de 137M dt**. Courtage international à 10 % : NA.
- p. 60, mesure 15 : retenue sur intérêts d'emprunts versés aux banques non-résidentes de 5 % à 10 % ; impact : **rendement positif de 1,8 M dt** ; fin de l'exonération des redevances payées par les entreprises totalement exportatrices à des non-résidents non établis : NA. Mesure 19 : baisse de l'avance à l'importation (taux actuel 10 %) : NA.
- p. 56 (mesure 10) : relèvement de la retenue à la source sur les sommes versées à des résidents de paradis fiscaux (taux actuel 15 %) : NA.
- p. 25 (diagnostic) : « multitude de taux d'imposition statutaires », « triples planchers » (minima d'imposition) ; p. 26 : acomptes provisionnels de 30 % de l'impôt dû de l'année précédente ; p. 38 : recommandation d'un taux de 10 % pour toutes les activités totalement exonérées, y compris l'exportation.
- p. 8 : IS baisse de 30 % à 20 % ; taux de 35 % étendu.
- Aucun nombre de sociétés, aucune recette d'IS, aucune concentration chiffrée dans le document.

### D. TVA, droit de consommation (priorité d)

- p. 82, mesure 8 « Baisse du taux de la retenue à la source sur TVA » (50 % actuel -> 30 %, 25 % ou 20 %) ; tableau d'impact en bas de page, recopié tel qu'imprimé (en M dt ; lu sur l'image, en-tête « le taux 30 % / 25 % / 20 % ») :
  - Le montant de la retenue : 179,321 | 149 | 119,5 (valeur « 149 » pour 25 % : incohérence apparente avec la suite 179,321 -> 119,5, à confirmer sur l'original ; lecture de l'image nette).
  - L'impact de la baisse sur l'impôt payé : 45,11 | 57,9 | 71,6.
  - L'impact de la baisse sur le crédit de TVA : -74,4 | -91,4 | -107,7.
  - Note : « Le montant de la retenue à la source en 2012 est de 298,9M dt ».
- p. 79-80 : deux taux plus un taux super réduit ; suppression des taux de 6 % et 12 % ; taux réduit entre 8 % et 10 % ; maintien de 6 % sauf médicaments et produits pharmaceutiques ; équipements au taux général en exploitation avec suspension en investissement ; taux super réduit pour médicaments, produits pharmaceutiques et leurs intrants et produits exonérés non soumissibles. Impact : NA.
- p. 80 : suppression de la majoration de 25 % (importations par non-assujettis hors État/collectivités/EPA, produits listés par le décret n° 2003-477 du 03/03/2003, achats de non-assujettis auprès d'assujettis). Impact : NA. Diagnostic p. 28 : cette majoration « apporte des recettes faibles ».
- pp. 77-78 : suppression de l'exonération des achats des entreprises publiques ; généralisation aux grossistes en alimentation générale et en médicaments ; suppression du seuil de 100 000 dt ; agriculture et pêche : hors champ (hyp. 1) ou TVA à taux super réduit (hyp. 2), retenue à la source au marché de gros ; exonérations du tableau A (§11, intrants agricoles) supprimées. Impact : NA, une ligne « Nul » (p. 77).
- p. 81 : limitation des crédits de TVA (compensation avec autres taxes, unification du taux de restitution, délais). NA.
- p. 83 : droit de consommation : suppression des dispositions fixant par décret les droits sur boissons alcooliques, vins et bière ; révision de la liste des produits. NA.
- p. 27 : « stagnation des recettes de fiscalité indirecte interne à un peu plus de 10 % du PIB » (pas de série) ; TVA tunisienne « nettement moins efficace que la moyenne des pays du Moyen-Orient ».
- Pas de taux de recettes de TVA, nombre d'assujettis ou de série chronologique.

### E. Recettes globales, pression fiscale, contrôle, fiscalité locale (priorité e)

- p. 31 : taux de recouvrement sur constatations de contrôle : **12 %** (année non précisée).
- p. 103 (« La lutte contre l'évasion fiscale », données statistiques) : pourcentage de déclarations annuelles déposées :
  - Tous contribuables : dans les délais / fin 2012 : 2009 : 51,2 % / 75,7 % ; 2011 : 40,5 % / 65,7 % ; 2012 : 36,6 % / 50,8 %.
  - Personnes morales : dans les délais / fin 2012 : 2009 : 50 % / 80,7 % ; 2011 : 44,7 % / 72,4 % ; 2012 : 40,3 % / 62,2 %.
  - BNC : dans les délais / fin 2012 : 2009 : 66,6 % / 88,3 % ; 2011 : 57,7 % / 81,3 % ; 2012 : 55,4 % / 71,5 %.
  - (Le deuxième tableau comporte quatre colonnes : PM dans les délais, PM fin 2012, BNC dans les délais, BNC fin 2012. L'intitulé de la colonne « fin 2012 » est ambigu : taux de dépôt au 31/12/2012 pour chacune des années d'imposition 2009, 2011, 2012, selon la lecture la plus plausible ; 2010 absent.)
- p. 115 : DGE : 1600 entreprises, « 70 % des recettes fiscales » (périmètre non précisé).
- p. 102 : plafond de paiements en espèces proposé 30 000 TND, puis 20 000, puis 10 000 ; comparaisons citées : France 6 000 TND (2 000 TND en 2014), Belgique 10 000 TND (6 000 en 2014), Maroc 2 000 TND, Algérie 1 000 TND (valeurs en TND telles quelles).
- p. 15-16 (Executive Summary) : plafond transactions en espèces 30 000 -> 20 000 -> 10 000 TND ; litiges ne dépassant pas 100 000 TND (p. 16, 112, 151) ; p. 109 : période de vérification approfondie ramenée à 3 mois ; demande d'éclaircissements de 10 à 30 jours.
- p. 111, 151 : taxation d'office à 10 % ou 15 % (paiements en espèces).
- Fiscalité locale : p. 87 (mesure 2) « Une charge supplémentaire de 600kdt / an (200 receveurs x15kdt/an sur 5 ans) » ; hausse de la couverture des comptables publics spécialisés de 20 % à 80 % (pp. 13, 87, 143) ; p. 90 mesure 9 : fusion TIB (taxe sur les immeubles bâtis) et contribution au FNAH en « Taxe sur l'habitation » : 11 % au lieu de 12 % (8 % TIB + 4 % FNAH ; la lecture « 8 % + 4 % = 12 % » est celle du texte), 13 % au lieu de 14 % (10 % + 4 %), 15 % au lieu de 16 % (12 % + 4 %), 17 % au lieu de 18 % (14 % + 4 %) ; p. 89 : abattement de 10 % pour paiement de la TIB avant fin février, pénalité de retard de 0,75 % à 2 % par mois ; p. 88 : prescription du recouvrement des dettes locales de 4 à 10 ans ; p. 96 mesure 22 : doubler les ressources des collectivités locales sur 2015-2019 pour atteindre 8 % du budget de l'État ou 4 % du PIB ; p. 97 : quotes-parts à transférer (IRPP, TVA, taxe de circulation, enregistrement, plus-value mobilière) laissées en blanc (« …% »).
- Pas de pression fiscale globale, pas de dépenses fiscales chiffrées dans ce document.

### F. Autres éléments
- p. 4 : principes : simplicité, équité, neutralité, transparence, modernisation, décentralisation (grille de cases à cocher du tableau, pp. 50-98) ; p. 5-6 : TVA à deux taux, code unique (« CGI »).
- pp. 129-153 : plan de mise en oeuvre (délais court terme / moyen terme 2 à 5 ans, budget qualitatif - / + / ++), sans chiffres.

---

#### 2013-11_cnf_compte_rendu_travaux.pdf

**Identification**
- Titre (p. 1) : « الجمهورية التونسية — خلاصة أعمال المجلس الوطني للجباية — المجلس الوطني للجباية 28 و 29 نوفمبر 2013 — بالتعاون مع » (La République tunisienne — Synthèse des travaux du Conseil national de la fiscalité — Conseil national de la fiscalité, 28 et 29 novembre 2013 — en collaboration avec [MS Louzir / Deloitte, pied de page « © 2013 MS Louzir membre de Deloitte Touche Tohmatsu »]).
- Métadonnée PDF : « Compte rendu des travaux de la CNF », créé le 9 décembre 2013, 135 pages ; **langue : arabe** ; ministère des Finances (logo) ; diaporama (PowerPoint) de format « tableau à deux colonnes » : à droite « المقترحات المقدمة في التقرير » (propositions du rapport), à gauche « ملاحظات المجلس الوطني للجباية » (observations du CNF), plus des pages « مقترحات جديدة للمجلس الوطني للجباية » (nouvelles propositions du CNF) à la fin de chaque partie.
- Couche texte présente et lisible (certaines lignes tronquées en bord de page) ; pas de page-image à océriser. Pages vérifiées visuellement : 9, 17, 45-53. Dans plus de la moitié des diapositives, la colonne d'observations est vide.
- **Aucun tableau chiffré d'impact financier (pas de « M dt », pas de recettes)** : seulement des taux, seuils et montants de propositions, déjà présents dans le rapport de synthèse, et les observations du CNF. Une observation du CNF (p. 27) demande d'ailleurs de clarifier les méthodes de détermination de l'incidence financière (« طلب توضيح طرق تحديد الانعكاس المالي ») et relève que la difficulté de calculer l'incidence de certaines propositions affectera l'évaluation de leur effet sur les équilibres financiers.
- Structure : impôts directs pp. 3-28 (promotion de l'assiette, taux, recouvrement, avantages fiscaux, nouvelles propositions) ; impôts indirects pp. 29-43 ; régime forfaitaire / économie parallèle pp. 44-63 ; fiscalité locale pp. 64-86 ; synthèse des observations du CNF sur le politique, l'administration, le commissaire aux comptes, les contribuables, la justice, le contrôle, la révision, la taxation, le contentieux (pp. 87-112) ; modernisation de l'administration fiscale pp. 113-134 ; p. 135 : renvoi au site www.finances.gov.tn.

### A. Régime forfaitaire (pp. 44-63) : propositions du rapport et observations du CNF

- Convention de lecture : les chiffres ci-dessous sont des propositions ou observations, pas des données.
- p. 45 : exclusion de certaines activités (capital et moyens d'exploitation importants, certaines zones) ; durée limitée du régime de **3 ou 4 ans** renouvelable une fois (dans ce compte rendu ; le rapport de synthèse, p. 53, parle de 5 ans + 3 ans). Observations CNF : vide.
- p. 46 : exonération des obligations pour les « revenus limités » (activités fixées avec les représentants des secteurs ou niveau du salaire minimum garanti) ; augmentation du minimum d'impôt et alignement sur le régime réel. Observations : vide.
- p. 47 : régime contractuel participatif ; observation du CNF : « cette procédure est ramifiée et complexe, surtout pour l'administration ».
- p. 48 : droit de patente annuel fixe, payable dans les 6 premiers mois ; impôt non inférieur à ce droit ; commission administration-UTICA. Observations : vide.
- p. 49 : généralisation de la TVA aux petits exploitants sauf revenus minimaux, court terme services seulement, moyen terme reste hors prix homologués ; recommandation d'étudier l'effet sur le niveau général des prix. Observation du CNF : « cette mesure peut accroître l'évasion fiscale ».
- p. 50 : révision de la méthode d'imposition (taux sur CA adaptés aux marges, ou remplacement à moyen terme par revenu selon marges et barème IRPP, déclaration unique). Observations : vide.
- pp. 51-53 : maîtrise de l'assiette (facturation, identifiant fiscal unique, base DGI-CNSS « exploitée d'ici deux ans », caisses enregistreuses, carnet de bord pour les transporteurs), amélioration du recouvrement (paiement en deux tranches obligatoire, doublement de l'impôt et du minimum en cas de retard, certificat de visite technique, services administratifs). Observations : vide.
- pp. 54-57 : intégration de l'économie parallèle. Observation du CNF à propos des avantages à l'intégration spontanée : « cette proposition ne sert pas l'équité fiscale et encourage les fraudeurs ; il faut utiliser les mécanismes disponibles pour régulariser la situation de ces personnes ». Police fiscale : le CNF propose d'abandonner la création de cette structure et d'étendre à la place le champ d'intervention de la garde douanière (p. 57). Zones franches commerciales frontalières (p. 57).
- pp. 58-62 : mesures communes (suppression de l'interlocuteur unique, culture fiscale, SIME, prescription, factures préétablies, régime réel simplifié, centres de gestion intégrés / certification fiscale, sanctions plus dissuasives). Observations CNF : vide.
- p. 63 « Nouvelles propositions du CNF » (forfait / économie informelle) : rétablir le régime forfaitaire **facultatif** (« إعادة العمل بالنظام التقديري الاختياري ») ; limiter l'économie non organisée ; criminaliser la contrebande et le monopole ; obligation de s'approvisionner auprès de contribuables au régime réel au-delà d'un certain montant d'achats ; lever le secret bancaire pour les contribuables au régime forfaitaire ; subordonner la licence d'exploitation à la régularisation fiscale et la rendre annuelle ; relancer le recensement géographique (« المسح الجغرافي »).
- p. 27 (impôts directs, nouvelles propositions) : observations du CNF « proposition de supprimer le régime forfaitaire » (« اقتراح حذف النظام التقديري ») et « proposition de supprimer l'impôt minimum, assimilé à la jizya » (« اقتراح حذف الضريبة الدنيا التي تعتبر بمثابة الجزية »). Les deux formulations sont citées telles que lues ; qui les porte exactement parmi les membres du CNF n'est pas précisé.
- p. 9 (BNC, à vérifier sur l'image) : observations du CNF sur la baisse de la déduction forfaitaire : importance de renforcer les éléments d'investigation en plus de baisser la déduction ; possibilité de lever le secret bancaire pour la vérification approfondie sur autorisation sur requête ; l'exclusion de certaines professions « n'est pas la meilleure décision » (certaines réalisent des bénéfices limités) avec proposition d'étendre à toutes les professions les conditions d'accès au forfait ; suppression progressive du régime forfaitaire d'assiette ; levée nécessaire du secret bancaire ; généralisation de la déclaration des factures ; opposition à une levée du secret bancaire pour certaines personnes seulement ; « inclure certaines professions libérales au régime réel seulement est une mesure injuste ».
- p. 8 : IRPP : plafond de déduction des frais professionnels « fixé à 10 % » (observation CNF : choisir l'hypothèse 2 avec plafond de 10 %) et rappel des hypothèses : taux de 12 % pour toutes les tranches (hyp. 1) ou taux dégressif (hyp. 2).
- p. 10 (revenus fonciers) : baisse de la déduction de 30 % à 20 % des recettes ; retenue à la source sur les loyers étendue aux forfaitaires BIC.

### B. IRPP (pp. 7-15, 19)
- p. 7 : déductions pour charges de famille (hypothèse 1 : 150 -> 250 dt ; enfants 100 dt pour les 4 premiers ; hypothèse 2 : 150 -> 300 dt). Observation CNF : choisir l'hypothèse 2 ; d'autres méthodes de déduction des charges.
- p. 19 : barème : 1re tranche de 1500 à 2000 dt avec redistribution (hyp. 1) ; relèvement de la tranche exonérée par déduction supplémentaire de 1000 dt aux smigards, extension aux revenus nets annuels ≤ 5000 dt, déduction supplémentaire de 500 dt ; indexation sur le SMIG (hyp. 2). Observations CNF : réviser les tranches du barème avec possibilité de plus de cinq tranches ; « rejet de la proposition de déduction supplémentaire de l'assiette ».
- pp. 11-12 : plus-values sur titres et immeubles ; taux de 10 % après 3 ans ; suppression de l'abattement de 10 000 dt. Observations : vide dans le texte extrait.
- p. 13 : obligation de déclaration d'existence, caisse enregistreuse.
- p. 14 : observation CNF : revoir la proposition d'imposer les associations, mutuelles, coopératives de services agricoles « pour éviter de les surcharger d'impôts ».
- pp. 27-28 (nouvelles propositions CNF, impôts directs) : réconciliation administration-contribuable ; impôt sur la fortune ; absence de simplification ; prise en compte du modèle de développement ; étude de l'impact social ; taux d'IS unique pour sociétés résidentes et non résidentes ; réduire l'écart entre salariés et professions non commerciales dans la contribution aux recettes ; régime non pénalisant pour sportifs et artistes ; faciliter la restitution de l'excédent d'impôt ; réforme administrative préalable ; préciser les critères de choix du plafond de déduction. Aucun chiffre financier.

### C. IS (pp. 4-6, 16-18, 22-26)
- p. 16 : baisse du taux d'IS de 30 % à 25 % puis 20 % avec dividendes à 5 %, 10 % ou 15 % (hyp. 1) ; observation CNF : imposer les dividendes par étapes (une observation oppose : ne pas imposer les dividendes en raison de la fragilité du marché financier).
- p. 17 : hyp. 2 : 30 % -> 20 % et dividendes imposés ; hyp. 3 : 25 % ou 20 % avec impôt minimum de 0,2 % du CA global (exportation incluse) et crédit d'impôt limité dans le temps. Observations CNF : simplifier avec un ou deux taux ; prévoir des mesures transitoires ; taux différentiel pour les sociétés industrielles.
- p. 18 : taux de 35 % étendu (grandes surfaces, fournisseurs d'accès internet, concessionnaires automobiles, courtiers d'assurance, autres à marge élevée) ; entreprises exonérées à 10 %.
- p. 20 : retenue sur intérêts de prêts aux banques non résidentes de 5 % à 10 % ; p. 21 : avance à l'importation (10 %).
- p. 25 : exportation à l'IS à 10 % dès 2014, observation CNF : soumettre l'exportation à l'IS à moyen terme « compte tenu de la conjoncture actuelle », progressivité, maintenir l'exonération des exportateurs.
- p. 22-26 : avantages fiscaux (comptes d'épargne : déduction des intérêts à 2000 dinars/an ; comptes d'épargne investissement de 20 000 à 50 000 dinars ; transmission d'entreprises ; plus-values de titres hors BVMT ; crédit d'impôt).

### D. TVA (pp. 29-43)
- p. 30 : suppression de l'exonération des achats des entreprises publiques ; généralisation aux grossistes en alimentation générale et en médicaments ; suppression du seuil de 100 000 dinars des détaillants. Observation CNF : maintenir l'exonération de l'agriculture, de l'alimentation générale et des médicaments.
- pp. 36-37 : deux taux (général et réduit 8 % à 10 %, suppression de 6 % et 12 %) plus taux super réduit ; observations CNF : revoir la répartition des activités selon les taux proposés ; adopter un taux unique.
- p. 38 : suppression de la majoration de 25 % (décret n° 2003-477 du 3 mars 2003). Observation CNF (p. 43) : appliquer deux taux en abandonnant la majoration de 25 %.
- p. 39 : crédit de TVA : suppression des causes, compensation, taux de restitution unifié ; observation CNF : faciliter la restitution pour les entreprises transparentes ; crédit unifié.
- p. 40 : retenue à la source sur TVA de 50 % -> 30 %, 25 % ou 20 %. Observation CNF : supprimer le mécanisme de la retenue de 50 %.
- p. 41-42 : sanctions ; droit de consommation (suppression de la fixation des taux par décret, révision de la liste).
- p. 43 (nouvelles propositions CNF) : TVA sociale pour renforcer les caisses sociales ; revoir la base de calcul de la TVA ; déduction de la TVA sur voitures de tourisme, pièces de rechange et entretien pour certaines professions libérales ; précisions sur les contrats et les services utilisés à l'étranger ; remboursement de l'excédent sans limitation de durée ; fait générateur au encaissement plutôt qu'à la facturation ; compétitivité du secteur touristique.
- Aucun chiffre de recettes ou d'impact.

### E. Fiscalité locale (pp. 64-86)
- p. 66 : proportion de comptables publics spécialisés dans les finances locales de « environ 20 % à 80 % » par paliers quinquennaux.
- p. 68 : prescription des dettes locales de 4 à 10 ans ; p. 70 : abattement de 10 % pour paiement de la TIB avant fin février, pénalité de 0,75 % à 2 % par mois ; p. 72 : taxe sur l'habitation 11 % / 13 % / 15 % / 17 % au lieu de 12 % / 14 % / 16 % / 18 % (TIB 8, 10, 12, 14 % + FNAH 4 %) ; p. 83 : quotes-parts (IRPP, TVA 2015-2016 puis 2017-2018 puis 2019, taxe de circulation, enregistrement, plus-value immobilière) laissées en pointillés (pourcentages non fixés) ; p. 85 : observations CNF : agence nationale pour unifier les bases de données locales, éviter les prélèvements, fiscalité propre des collectivités, etc. ; p. 86 : réforme de fond préférable après l'adoption de la Constitution et de la loi sur la décentralisation. Aucun chiffre de recettes.

### F. Contrôle, contentieux, modernisation (pp. 87-134)
- p. 92 : plafond de paiements en espèces 30 000 -> 20 000 -> 10 000 dinars avec sanctions ; p. 100 : proposition de limiter le contrôle (« 4 ans » pour la période, restriction à une année ... texte partiellement tronqué à l'extraction) ; p. 102 : réponse du contribuable à la demande d'éclaircissements ; vérification approfondie ramenée à 3 mois, délai de réponse 6 mois de l'administration ramené à 3 mois (« إقتراح الحط من أجل 6 أشهر ... إلى 3 أشهر »), réclamation à traiter dans un maximum de 6 mois ; p. 103 : délai de demande d'éclaircissements de 10 à 30 jours ; p. 107 : suppression de l'acompte de 20 % pour suspendre l'exécution de la taxation d'office ; taux de taxation d'office pour paiements en espèces 10 % ou 15 % ; p. 108 : seuil des litiges 100 000 dinars, proposition de 50 000 ; p. 115 : DGE 1600 entreprises, « 70 % des recettes fiscales » ; p. 122 : « 192 formalités fiscales inventoriées » (texte tronqué ; chiffre lu : 192).
- Aucune statistique de déclarations déposées (le tableau de la p. 103 du rapport de synthèse n'est pas repris ici).

---

#### Synthèse

- Les deux documents ne contiennent presque aucun chiffre de population forfaitaire : le seul bloc chiffré sur le forfait est à la p. 10 du rapport de synthèse (« 60 % des inscrits au fichier contribuent à concurrence de 0,2 % des recettes fiscales ; 45 000 interventions de contrôle ; rendement annuel de 12 millions de dinars », sans année). Forfait d'assiette BNC : 3 % de l'IRPP, 60 % des BNC l'optent (p. 8) ; revenus fonciers : 1 % de l'IRPP ; déduction forfaitaire 30 % (BNC : bénéfice forfaitaire à 70 % des recettes).
- Tableau d'impact (rapport de synthèse, pp. 50-63) : forfait BNC : rendement positif de 6,7M dt (baisse de la déduction de 30 % à 20 %) ; charges de famille : baisse de 20,1 M dt (hyp. 1) et 27 M dt (hyp. 2) ; frais professionnels : 73,3 M dt (12 %), 66 M dt non plafonné / 56,7 M dt plafonné à 4000 dt (taux dégressif) ; barème : 113,2 / 35,1 / 19,2 / 410 M dt de baisse ; IS : 116,3 M dt (25 % + dividendes), 221,6 M dt (20 %), 101,4 / 206,5 M dt avec minimum 0,2 % du CA ; taux de 35 % étendu : +3 Mdt ; entreprises exonérées à 10 % : +85,4 Mdt ; exportation à 10 % : +137 M dt ; retenue sur intérêts non-résidents : +1,8 M dt.
- TVA : retenue à la source sur TVA (298,9 M dt en 2012) ; impact d'une baisse à 30 / 25 / 20 % : impôt payé +45,11 / +57,9 / +71,6 M dt, crédit de TVA -74,4 / -91,4 / -107,7 (p. 82 ; valeur « 149 » pour 25 % douteuse).
- Autres chiffres : taux de recouvrement sur constatations 12 % ; taux de dépôt des déclarations dans les délais 2009 / 2011 / 2012 : 51,2 % / 40,5 % / 36,6 % (tous contribuables), 50 / 44,7 / 40,3 % (personnes morales), 66,6 / 57,7 / 55,4 % (BNC) (p. 103).
- Le compte rendu du CNF (arabe, 28-29 nov. 2013, 135 p.) n'a aucun tableau chiffré : il ne contient que les positions du CNF, parmi lesquelles, pour le forfait : rétablir un régime forfaitaire facultatif, supprimer le forfait ou l'impôt minimum selon certains membres, TVA aux forfaitaires jugée facteur de fraude.
- Aucun scan : les deux PDF ont une couche texte exploitable ; aucun OCR requis.

---

### Inventaire B : régime forfaitaire (CNF nov. 2013) et consultation régionale du Kef (juin 2014)

#### 2013-11_cnf_presentation_regime_forfaitaire.pdf

**Titre (p. 1)** : « حوصلة لأشغال فريق العمل المكلف بمراجعة النظام التقديري وإدماج الاقتصاد الموازي » — « Synthèse des travaux du groupe de travail chargé de la révision du régime forfaitaire (النظام التقديري) et de l'intégration de l'économie parallèle ». Sous le titre : « المجلس الوطني للجباية — نوفمبر 2013 » (Conseil national de la fiscalité, novembre 2013). En-tête : République tunisienne, ministère des Finances.
- Date : novembre 2013 (PDF créé le 29/11/2013 ; séances du CNF les 28-29 novembre 2013 selon la consigne). Aucune autre date interne.
- Auteur : groupe de travail (représentants du ministère des Finances, autres ministères, professionnels, universitaires, organisations et associations nationales) ; « près de 30 séances de travail » (p. 2).
- 22 pages, arabe, diaporama PowerPoint. Couche texte présente (l'extraction est inversée mais lisible) ; aucune page en scan : pas d'OCR à prévoir. Pages 4-21 : tableaux à 4 colonnes (objectifs / propositions / principes généraux cochés : justice, simplification, neutralité, transparence, modernisation, décentralisation / incidence sur les recettes fiscales, partout « غ.م » = non mesurée). P. 22 : « Merci ».
- Plan : axe 1 révision du régime forfaitaire (3 sous-volets : assiette-imposition p. 4-9, maîtrise de l'assiette p. 10-11, recouvrement p. 12) ; axe 2 intégration de l'économie parallèle (p. 13-16) ; axe 3 mesures communes (p. 17-21).

### a) Chiffres du régime forfaitaire (tous en encadrés jaunes, colonne « objectifs »)
| Page | Valeur exacte | Contexte |
|---|---|---|
| 4 | environ **400 000** assujettis au régime forfaitaire, soit **60 %** des inscrits au fichier (« الجذاذية »), soit **80 %** des personnes physiques commerçants et industriels (« أ.ط. تجار وصناعيون ») | Objectif : limiter le forfait aux petits exploitants. Année de référence non indiquée. |
| 4 | environ **70 %** d'entre eux ont une ancienneté dans l'activité **égale ou supérieure à 8 ans** | idem |
| 5 | **31 %** des déclarations déposées comportent un chiffre d'affaires (« رقم معاملات ») **inférieur à 3 000 dinars** et paient donc l'impôt **minimum** (« الضريبة الدنيا ») | Objectif : alléger la charge des revenus limités ; ajuster l'impôt minimum au coût du recouvrement. Année non indiquée. |
| 10 | environ **45 000** vérifications (« تدخلات ») par an des services de contrôle auprès des forfaitaires, pour un rendement annuel d'environ **12 millions de dinars** | Objectif : mieux maîtriser l'assiette. Année non indiquée. |
| 11 | **66 %** : « beaucoup d'anciens forfaitaires optionnels ont délibérément abaissé leur chiffre d'affaires déclaré, ce qui a réduit leur contribution de 66 % » (formulation du diaporama : « للحط من مساهمتهم بنسبة 66% ») | Objectif : renforcer les mécanismes de contrôle. Lecture littérale ; périmètre/année non précisés. |
| 11 | **21 %** des forfaitaires exercent dans le secteur du transport | idem |

Aucun tableau ni graphique numérique : pas de recettes globales de l'impôt forfaitaire, pas de répartition par activité ou tranche de CA, pas de série annuelle dans ce document.

### Mesures proposées (sans chiffres, hormis ce qui est noté)
- P. 4, court terme : exclure du forfait certaines activités exigeant un capital et des moyens importants (surface, main-d'œuvre) et exercées dans certaines zones (chefs-lieux, zones à forte activité commerciale) ; liste fixée par arrêté après consultation des structures professionnelles ; octroi du régime pour une durée déterminée (**3 ou 4 ans**) renouvelable sur justification.
- P. 5 : exonérer des obligations fiscales liées à l'activité les forfaitaires à revenus limités (définis soit par secteurs, soit par référence au revenu des titulaires du SMIG, base de données des Affaires sociales), avec une contribution libératoire au profit des collectivités locales ; relever l'impôt minimum et l'aligner sur celui du régime réel.
- P. 6, moyen terme, hypothèse 1 : forfait « contractuel/consultatif » pour une durée donnée, fondé sur des indicateurs (surface du local, nombre de salariés, marge) ; hypothèse 2 (p. 7) : « droit de patente » annuel fixe, montant fixé avec les secteurs, payable dans les 6 premiers mois, l'impôt définitif calculé par un taux appliqué à l'écart recettes-dépenses, plancher = droit fixe ; commissions avec l'UTICA pour fixer les barèmes.
- P. 8 : généraliser la TVA aux petits exploitants sauf ceux aux revenus de subsistance (dépôt de déclarations trimestrielles ou semestrielles) ; court terme : limiter aux seuls prestataires de services ; moyen terme : y soumettre le reste des forfaitaires sauf les activités à homologation administrative des prix.
- P. 9 : réviser le mode de calcul (adapter les taux sur chiffre d'affaires à la nature de l'activité et à la marge, ou imposer le revenu global au barème de l'IRPP en une seule déclaration) ; réunions avec les représentants des secteurs.
- P. 10 : obligation de facturation au-delà d'un seuil de transaction ; identifiant fiscal unique chez les Affaires sociales ; base de données commune DGI-CNSS (la CNSS a recensé tous les affiliés, exploitation sous deux ans).
- P. 11 : caisses enregistreuses/terminaux de paiement ; carnet de conduite obligatoire dans le transport.
- P. 12, recouvrement : paiement obligatoire en 2 tranches (au lieu de l'option) ; doublement de l'impôt dû (y compris minimum) en cas de paiement hors délai ; lier les remboursements des contractants de l'État et des établissements publics à la régularité fiscale ; lier le contrôle technique des véhicules de transport au dépôt de la déclaration annuelle ; lier les services administratifs à la régularité fiscale.
- P. 13-16 (économie parallèle) : traitement progressif sectoriel ; incitations à l'intégration spontanée (pas de régularisation du passé, exonération partielle de la contribution de sécurité sociale limitée dans le temps, facilités de financement) ; comité technique national ; lutte contre la contrebande, coordination avec les pays voisins, espaces dédiés aux acteurs informels ; comité permanent (douane, administration des prestations, organisations professionnelles, défense du consommateur, gouvernance) ; application de l'article 26 de la loi n° 46 du 15/05/1995 (statut général des agents de la douane) selon les principes de la convention d'Arusha ; étude d'une « police fiscale » ; zones franches frontalières.
- P. 17-21 (mesures communes) : supprimer la procédure de l'interlocuteur unique à la recette des finances pour déposer la déclaration d'existence auprès des bureaux de contrôle des impôts ; politique de communication et éducation fiscale ; création d'un service fiscal des moyennes entreprises (SIME) ; prolonger les délais de prescription pour la fraude ; interdire l'usage de factures pré-imprimées ; réduire le nombre de déclarations, simplifier le contenu, réduire le nombre de passages à la recette ; revoir le référentiel comptable du réel simplifié ; « certification fiscale » via centres de gestion agréés ; relever les montants des sanctions pour les rendre dissuasives (p. 21).

### b) à e) IRPP, IS, TVA, recettes
Rien de chiffré en dehors du régime forfaitaire (hors les références de la TVA et du statut des douanes ci-dessus).

---

#### 2014-06_consultation_regionale_kef_expose_six_commissions_ar.pdf

**Titre (p. 1)** : « وزارة الاقتصاد والمالية — استشارة جهوية حول إصلاح المنظومة الجبائية — ولايات الكاف – جندوبة – باجة – سليانة – بنزرت — الكاف، 17 جوان 2014 » (ministère de l'Économie et des Finances ; consultation régionale sur la réforme du système fiscal ; gouvernorats du Kef, Jendouba, Béja, Siliana, Bizerte ; Le Kef, 17 juin 2014).
- Date : 17 juin 2014 (PDF créé le 24/06/2014, convertisseur « Conv2pdf.com »). 47 pages, arabe, diaporama. Couche texte correcte (extraction lisible) ; aucun scan, aucun graphique : pas d'OCR à prévoir.
- Nature : exposé de synthèse des travaux des commissions de la réforme (plan : objectifs p. 2-3 ; sommaire p. 4 ; impôts directs p. 5-12 ; impôts indirects p. 13-23 ; régime forfaitaire p. 24-27 ; économie parallèle p. 28-31 ; administration fiscale p. 32-38 ; lutte contre la fraude p. 39-46 ; « Merci » p. 47). La numérotation interne des diapositives est décalée de 1 par rapport aux pages PDF (j'utilise les pages PDF). Les mentions « أنجز ضمن قانون المالية لسنة 2014 » identifient les mesures déjà réalisées.
- **Document sans tableau ni graphique ; il ne contient presque aucune donnée chiffrée** (aucun effectif, aucune recette, aucun barème). Les seuls nombres sont des taux ou plafonds proposés.

### a) Régime forfaitaire (p. 25-27, 31)
- P. 25, court terme : exclure certaines activités du forfait (**réalisé par la loi de finances 2014**) ; durée **3 ou 4 ans** renouvelable ; exonération des obligations fiscales pour les forfaitaires à revenus limités avec contribution libératoire au profit des collectivités locales ; **relèvement de l'impôt minimum** et alignement sur celui du régime réel (**réalisé par la LF 2014**).
- P. 26, moyen terme : hypothèse 1 forfait contractuel à durée déterminée ; hypothèse 2 « droit de patente » annuel fixe négocié avec les secteurs ; obligation de facturation au-delà d'un seuil (**réalisé LF 2014** ; seuil non indiqué) ; information fiscale/système d'information ; caisses enregistreuses ; carnet de conduite pour le transport.
- P. 27 : doublement de l'impôt forfaitaire, impôt minimum compris, en cas de paiement hors délai (**LF 2014**) ; paiement des sommes dues par l'État/établissements publics conditionné à la régularité fiscale (**LF 2014**) ; contrôle technique et services administratifs liés à la régularité fiscale (non réalisé à cette date).
- P. 7 : (impôts directs, personnes physiques) « réviser les conditions d'accès aux régimes forfaitaires ».
- P. 31 : orienter les bureaux de contrôle vers la maîtrise du fichier des forfaitaires ; rendre les sanctions dissuasives, notamment en matière de facturation.
- Aucun nombre de forfaitaires ni recette dans ce document.

### b) IRPP (p. 7, 10, 11)
- P. 7 : relever les déductions pour situation et charges de famille avec révision périodique ; revoir la déduction pour frais professionnels ; régime fiscal des plus-values sur titres et immeubles. P. 10 : « revoir le barème de l'impôt sur le revenu » (sans taux). P. 8 : étendre l'impôt à d'autres personnes et revenus (associations hors objet social, jeux de hasard, loterie).
- P. 11 : aligner les taux de retenue à la source sur les taux de l'IS et le barème de l'IR ; **réduire le taux de l'acompte sur importations fixé à 10 %** (sans nouveau taux) ; revoir la liste des biens de consommation soumis à cet acompte.

### c) IS (p. 6, 9, 12)
- P. 9 : « réduire le taux de l'IS fixé à **30 %** avec soumission des bénéfices distribués à l'impôt » (**réalisé par la LF 2014**) ; soumettre les entreprises exonérées d'IS au taux réduit fixé à **10 %** (proposition).
- P. 6 : provisions déductibles : étendre aux provisions pour dépréciation des actions et parts sociales (sociétés auditées par un commissaire aux comptes) et pour risques et charges (risque de change, grosses réparations) ; relever le taux de déduction des provisions par étapes : **75 % puis 100 %** (valeur de référence non précisée dans le document).
- P. 12 : réviser les avantages fiscaux de l'IR/IS en cohérence avec le projet de code de l'investissement, maintenir ceux liés à l'épargne ; remplacer les avantages retenus par un crédit d'impôt (crédit d'impôt à la réalisation effective) ; regrouper les avantages dans un cadre légal unique.

### d) TVA et droits de consommation (p. 14-23)
- P. 14 : supprimer les exonérations sur les acquisitions des entreprises publiques auprès d'assujettis ; généraliser la TVA au commerce de gros alimentaire et y soumettre le commerce de gros de médicaments et produits pharmaceutiques.
- P. 15-16 : production agricole et pêche : hypothèse 1 les laisser hors champ ; hypothèse 2 supprimer droits et taxes sur chiffre d'affaires et les remplacer par la TVA à taux réduit. P. 17 : soumettre les médicaments au détail (en parallèle du gros, taux réduit) ; supprimer les exonérations du détail sauf celles prévues par la loi ; supprimer les exonérations des intrants agricoles/pêche (n° 11 du tableau « A ») ; maintenir une liste limitée (prix administrés/subvention).
- P. 18 : deux taux (général et réduit) plus un taux super-réduit ; **supprimer les taux de 6 % et 12 %**, appliquer un taux réduit **entre 8 % et 10 %** à une liste limitée d'opérations ; taux général pour professions libérales, formation, informatique/Internet ; maintien du taux réduit pour les opérations actuellement à 6 % sauf médicaments et intrants ; équipements au taux général en phase d'exploitation avec suspension en phase d'investissement.
- P. 19 : taux super-réduit pour une liste (médicaments, intrants, produits aujourd'hui exonérés à soumettre) ; **suppression totale** de la mesure de relèvement de la base de TVA de **25 %** (formulation exacte : « الحذف الكلّي لإجراء الترفيع في قاعدة الأداء على القيمة المضافة بنسبة 25% »).
- P. 20 : déductibilité sur la base de factures conformes ; sanctions proportionnées sans limiter le droit à déduction ; réduire les excédents de TVA (unifier le taux de l'acompte, améliorer les délais de remboursement).
- P. 21 : retenue à la source : réduire le taux dans un premier temps, supprimer ensuite ; réduction de **50 %** par étapes vers la suppression, par application d'un taux de **30 %, 25 % ou 20 %** (valeur de départ non précisée sur la page).
- P. 22 : limiter la multiplicité des droits et taxes sur chiffre d'affaires en étendant la TVA ; examiner l'affectation d'une fraction de la TVA aux caisses. P. 23 : droit de consommation : revoir la liste (exclure certains produits avec l'extension de la TVA) et les taux.

### e) Recettes, contrôle, fraude, administration (p. 29-46)
- Aucun chiffre de recettes, pression fiscale ou dépenses fiscales.
- P. 44 : plafond des transactions en espèces : **20 000 dinars**, ramené progressivement à **10 000 dinars** puis **5 000 dinars**, avec sanction (marqué **réalisé par la LF 2014** ; la page ne dit pas à quelles dates les paliers s'appliquent).
- P. 42 : sanction pénale de l'émission de factures à montants gonflés (**LF 2014**) ; P. 40-46 : collecte d'informations, déclarations de l'employeur sur support magnétique sans seuil de chiffre d'affaires, structure de recherche et lutte contre la fraude, activité occulte (peine spécifique et prescription allongée), domiciliation, prix de transfert (accord préalable), accès aux comptes bancaires et portefeuilles-titres, garanties du contribuable (autorisation du parquet pour visites domiciliaires, réduction de la durée de vérification approfondie, délais de réponse de l'administration, expertise immobilière à la demande du contribuable).
- P. 33-34 : création d'une structure de gestion des risques, d'une structure de coopération internationale, d'une structure de recherche et lutte contre la fraude, d'une structure de modernisation ; élargir la DGE au recouvrement ; à moyen terme une autorité générale des impôts autonome et un service pour moyennes entreprises du Grand Tunis.
- Fiscalité locale : citée au sommaire (p. 4) mais aucune diapositive dédiée dans cet exposé.

---

### Inventaire G : Assises nationales de la fiscalité (12-13 nov. 2014) et Journée de réflexion (1er oct. 2014)

Convention : « p. N » = numéro de page du PDF (pour le document FR des Assises, le numéro imprimé sur la diapositive est p. PDF − 1). Les valeurs sont recopiées telles quelles ; « NA » = impact non chiffré dans le document. Aucune page n'est un scan sans texte : tous les PDF ont une couche texte (les images repérées sont des logos, fonds ou graphiques ; les graphiques sans couche texte ont été lus visuellement).

#### 2014-11_anf_projet_reforme_fiscale_FR.pdf

- **Titre** : « Projet de réforme du système fiscal tunisien », Ministère de l'Économie et des Finances, « Les Assises Nationales de la Fiscalité », 12 et 13 novembre 2014, Hôtel Le Palace Gammarth (p. 1).
- **Auteur** : ministère de l'Économie et des Finances (MEF) ; le document reprend les travaux des six commissions du projet de réforme (mai 2013-nov. 2013), validés par le Conseil national de la fiscalité (CNF, nov. 2013), puis la consultation régionale et nationale de 2014. Les diagnostics du chapitre « organismes internationaux » citent « Fonds monétaire international » comme source (p. 37) ; la p. 19 mentionne des diagnostics « FMI, MCC ». Aucun auteur nominatif.
- **Nature** : diaporama (rapport en format diapositives), 123 p., français. Texte intégral présent. Pages avec images : 1, 2, 20 (organigramme de gouvernance), 22, 80 (schéma).
- **Plan** : Introduction (p. 4) ; Executive Summary (p. 6-17) ; Méthodologie et organisation (p. 19-20) ; Diagnostic et mesures proposées (p. 23-47) ; Synthèse des travaux : impôts directs (p. 50-63), régime forfaitaire (p. 65-70), impôts indirects (p. 72-78), fiscalité locale (p. 80-93 env.), transparence/concurrence loyale (p. 94-98), évasion, garanties du contribuable (p. 100-107), administration fiscale (p. 109-120), annexe TVA (p. 123).
- **Le fichier `2014-11_anf_document_FR_PG.pdf` est identique** : 123 p., fichier texte extrait identique octet à octet (`cmp`). Il n'est pas inventorié séparément.
- Ce document ne contient **aucun tableau statistique** (nombre de forfaitaires, recettes, ventilation par activité ou tranche de CA, série annuelle) : il contient des estimations d'impact budgétaire par mesure et quelques chiffres de diagnostic.

### a) Régime forfaitaire

- p. 10 (Executive Summary, « Révision du régime forfaitaire et intégration de l'économie informelle », lu visuellement) : « En dépit de l'importance du nombre de contribuables soumis au régime forfaitaire, leur contribution aux recettes fiscales reste faible (60 % des inscrits au fichier contribuent à concurrence de 0,2 % des recettes fiscales, 45 000 interventions des services de contrôle avec un rendement annuel de 12 millions de dinars) ». Aucune année, aucune définition précise de « inscrits au fichier » ; l'arabe (p. 11) dit « 0,2 % des recettes fiscales dans le régime intérieur » et « 45.000 interventions annuelles, rendement de 12 MD ».
- p. 10 : « En l'absence de conditions légales d'éligibilité … certains contribuables bénéficient indéfiniment de ce régime » ; « les obligations fiscales à la charge des forfaitaires ne permettent pas de déterminer avec précision le niveau du CA ».
- p. 8 (IRPP, régimes d'assiette forfaitaire) : BNC au forfait d'assiette : « Faible contribution dans la recette fiscale (3 % de l'IRPP) » ; « 60 % optent pour le forfait d'assiette » ; revenus fonciers : « Faible contribution (1 % de l'IRPP) ».
- p. 24 : option de fiscalisation des BNC « sur la base d'un bénéfice forfaitaire égal à 70 % des recettes brutes ».
- p. 25 : « La répartition des forfaitaires en termes de CA et entre les secteurs d'activités montre un potentiel de recettes non négligeable en cas d'une meilleure maîtrise de l'assiette imposable permettant l'identification des faux forfaitaires » (aucune répartition chiffrée dans le document).
- p. 32 : « Plus de la moitié des entreprises inscrites au fichier (forfaitaires et entreprises au réel) ne remplissent pas leurs obligations fiscales. »
- p. 31 : taux de recouvrement sur constatations de contrôle : 12 % (tous contribuables).
- p. 52 (Impôts directs n° 5, BNC au forfait d'assiette) : réduction de la déduction forfaitaire de 30 % à 20 % (LF 2014) : rendement positif de 6,7 MD ; limitation du forfait d'assiette à 5 ans, extensible de 3 ans ; exclusion des avocats, experts comptables, comptables, médecins, courtiers en assurance, établissements d'enseignement privé.
- p. 52-53 (n° 6, revenus fonciers) : déduction forfaitaire de 30 % à 20 % du montant des recettes (NA) ; possibilité de déduire 1 % par an du montant des loyers sur présentation du contrat enregistré (p. 53).
- p. 65 (Régime forfaitaire n° 1) : « LF2014 – 68 activités ont été exclues » du régime forfaitaire ; limiter le régime à 3 à 4 ans, renouvelable. N° 2 : réviser les taux calculés sur le CA, ou remplacer par un régime contractuel participatif (indicateurs : superficie, nombre d'employés, marge), ou un « droit de patente » fixe. Aucun taux ni barème recopié dans le document.
- p. 66 (n° 4) : « Augmentation de 50 % du montant du minimum d'impôt dû par les forfaitaires (LF 2014) » ; n° 3 : dispense du formalisme pour les « revenus de survie », avec contribution libératoire collectée par les collectivités locales.
- p. 67 (n° 5-6) : factures obligatoires au-dessus d'un montant (LF 2014) ; caisses enregistreuses ; majoration de 50 % de l'impôt forfaitaire dû en cas de dépôt tardif (plus de 30 jours après l'échéance) (LF 2014).
- p. 68 (n° 7, LFC 2014, intégration de l'économie informelle) : impôt minimum par déclaration de **1000 ou 2000 dinars** (deux tranches selon l'activité) ; dispense d'impôt sur les montants déposés en banque/poste/bourse/contrats de capitalisation moyennant **15 %** de leur valeur avant le 31 déc. 2015 ; transactions en espèces limitées, saisie des espèces non justifiées (10.000 dinars) ; prescription portée à 15 ans pour les condamnés pour contrebande.
- p. 69-70 : commission technique nationale (douanes, enquêtes économiques, DGI), zones franches frontalières, SIME (services des moyennes entreprises) pour mieux maîtriser « les micro-entreprises et surtout les forfaitaires » (p. 70, n° 12), système de transition « similaire au forfait optionnel qui a été supprimé » (p. 70, n° 13).
- p. 72 (TVA n° 2) : « La non soumission des petits exploitants imposables selon le régime forfaitaire à la TVA » ; soumission d'une catégorie des forfaitaires à un assujettissement simplifié.
- p. 86 (fiscalité locale n° 11) : TCL : régime dédié aux forfaitaires par montants prédéterminés par nature d'activité (NA) ; p. 12 : transfert progressif de la gestion du régime forfaitaire aux collectivités locales.
- p. 38-40 (diagnostic, mesures « proposées » citant l'FMI) : « renforcer le contrôle du système du forfait » ; mettre en œuvre le régime réel simplifié comme régime de transition ; seuil unique d'assujettissement à la TVA (p. 40) ; p. 42 : étendre le seuil de **100 000 DT** (commerçants) à toutes les activités.

### b) IRPP

- p. 23 : barème non révisé « depuis plus de 20 ans » ; « le SMIG dépasse le seuil de la première tranche d'imposition » (sans chiffre).
- p. 24 : prélèvement à la source de 20 % sur revenus d'intérêt ; dividendes totalement exonérés ; BNC : forfait 70 % des recettes brutes.
- p. 51 (n° 3, déductions pour situation et charges de famille) : hypothèse 1 : chef de famille 150 → 250 D ; enfants 100 D pour les quatre premiers ; parents 150 → 250 D : baisse de recettes de **20,1 MD** ; hypothèse 2 (p. 52) : chef de famille 150 → 300 D ; enfants 100 D sans limite aux quatre premiers ; parents 150 → 300 D : baisse de **27 MD**.
- p. 52 (n° 4, frais professionnels des salariés) : hypothèse 1 : taux unique 12 % : baisse de **73,3 MD** ; hypothèse 2 : taux dégressif : baisse de **66 MD** si non plafonnée, **56,7 MD** si plafonnée à 4000 D.
- p. 59 (n° 13, barème) : première tranche exonérée de 1500 dt à 2000 dt (autres tranches harmonisées), ou indexée sur le SMIG (baisse 40 M dt), ou 1500 dt à 5000 dt avec hausse des taux des tranches supérieures, avec ou sans maintien des déductions communes ; impacts listés dans la colonne : « Baisse de 113.2 MD », « Baisse de 35,1 MD », « Baisse de 19,2 MD », « Baisse de 410 MD » (l'appariement de chaque impact avec sa variante n'est pas explicite dans la mise en page). Hypothèse 2 : maintien du barème, déduction supplémentaire de 1000 dt des SMIGARS étendue aux personnes dont le revenu annuel net ne dépasse pas 5000 dt (baisse de 35,1 M dt), ou 1000 dt SMIGARS + 500 dt pour salariés/pensionnés ≤ 5000 dt.
- p. 54-55 (n° 7, revenus des capitaux) : plus-values de cession de titres : intégrées au revenu global à court terme (3 ans), imposées à **10 %** au-delà de 3 ans de détention ; suppression de l'abattement de **10 000 dt** sur la plus-value de cession d'actions et parts sociales (p. 55). Impôt sur la fortune : « possibilité d'instauration » (p. 55).
- p. 61 (n° 21) : plafond de déduction des intérêts des comptes d'épargne porté à **2000 D** ; déduction « compte épargne investissement » de **20 000 D à 50 000 D** (aligné sur les comptes épargne en actions).
- p. 60 (n° 15) : retenue à la source sur les intérêts d'emprunts payés aux banques non résidentes de 5 % à 10 % : rendement positif 1,8 MD. N° 19 : avance sur importation de produits de consommation fixée à 10 %.
- Aucun barème chiffré (tranches, taux) n'est recopié dans ce document ; aucune recette globale de l'IRPP ; aucune répartition salariés/non-salariés.

### c) IS

- p. 8 : baisse du taux de l'IS de 30 % à 25 %, puis 20 % ; dividendes imposés à 5 %, 10 % ou 15 % ; extension du taux de 35 % (« fait partiellement dans le cadre de LF 2014 »).
- p. 57 (n° 11 et suiv.) : première phase (30 % → 25 %, LF2014) + dividendes à 5/10/15 % : baisse de **116,3 MD** ; deuxième phase (25 % → 20 %) : baisse de **221,6 MD**.
- p. 58 (n° 11, 2e hypothèse, lu visuellement) : taux de 25 % ou 20 % avec minimum d'impôt de **0,2 %** du CA global (y compris exportation) applicable à toutes les sociétés (LF 2014) : taux 25 % : baisse de **101,4 MD** ; taux 20 % : baisse de **206,5 MD**. N° 12 : extension du taux de 35 % (grandes surfaces, fournisseurs d'accès internet, concessionnaires automobiles, courtiers en assurance…) : **+3 MD** ; entreprises exonérées soumises à un taux réduit de 10 % + PME à taux préférentiel après la période d'exonération : rendement positif de **85,4 MD**.
- p. 63 (n° 21) : bénéfices d'exportation soumis à l'IS à **10 %** dès 2014 (LF 2014) : augmentation de **137 MD** ; courtage international à 10 %.
- p. 25 : IS multiples taux statutaires, « triples planchers » (minima d'imposition) ; p. 26 : avances trimestrielles de **30 %** de l'impôt dû de l'année précédente ; p. 38 : taux de 10 % proposé pour toutes les activités totalement exonérées.
- p. 28 : retenue à la source TVA : moitié du montant de TVA facturée (voir d).
- Aucun nombre de sociétés, aucune concentration, aucune recette globale de l'IS ; aucune estimation du coût des avantages fiscaux (dépenses fiscales) dans ce document.

### d) TVA et droits de consommation

- p. 26 : « TVA à trois taux » (6 %, 12 %, 18 %) à seuils d'assujettissement multiples ; p. 27 : « stagnation des recettes de fiscalité indirecte interne à un peu plus de 10 % du PIB » ; p. 28 : majoration de 25 % sur ventes à non-assujettis.
- p. 72 (n° 2) : généralisation de la TVA aux grossistes en alimentation générale et aux grossistes en médicaments, suppression du seuil annuel de 100 000 dt pour les détaillants : **14,4 MD** (taux 6 % et 18 %). (L'arabe, p. 69, donne **158,9 MD** pour la même ligne : voir la section AR.)
- p. 73 (n° 3) : médicaments et produits pharmaceutiques à TVA : **41,28 MD** (6 % à tous les stades) ou **−1,78 MD** (4 % en gros et détail).
- p. 74 (n° 4, taux) : deux taux (droit commun et réduit entre 8 % et 10 %, supprimant les 6 % et 12 %) : **25,9 MD** (application de 2 taux 10 % et 18 %) ; services de professions libérales, formations, internet/informatique au taux commun : **45,35 MD**.
- p. 75 (n° 5) : suppression de la majoration de 25 % : **17,9 MD**. (Arabe p. 72 : **34,5 MD**.)
- p. 77 (n° 8, retenue à la source TVA) : retenue actuelle 50 %, baisse à 30 %, 25 % ou 20 %. Tableau (en M dt ; montant de la retenue en 2012 : **298,9 M dt**) :

| Taux de retenue | 30 % | 25 % | 20 % |
|---|---|---|---|
| Montant de la retenue | 179,321 | 149 | 119,5 |
| Impact de la baisse sur l'impôt payé | 45,11 | 57,9 | 71,6 |
| Impact de la baisse sur le crédit de TVA | −74,4 | −91,4 | −107,7 |

- p. 78 (n° 10-11) : droits de consommation sur boissons alcooliques, vins et bière à fixer par la loi (et non décret) ; révision de la liste des produits.
- p. 123 (annexe, lu visuellement) : « Impact de la suppression des exonérations de quelques biens et services du Tableau « A » », revenus 2012 par numéro de ligne du tableau A, en dinars (présentation en anglais « 2012 Revenue Impact (6 %) / (10 %) / (18 %) ») : n° 7 soluté de dialyse, hémodialyses, véhicules pour invalides : 83 744 393 (6 %) ; n° 9 enseignement primaire … supérieur, professionnel : 1,16 (10 %, unité douteuse) ; n° 10 hammam : 19 058 277 (18 %) ; n° 12 bateaux autres que de plaisance : cellule vide ; n° 13 plants et semences : 12 449 (6 %) ; n° 15 eau agricole : 15 246 000 (6 %) ; n° 22 agences de voyages : 1 719 372 (10 %) ; n° 26 matériel de forage et sondage : 3 640 044 (6 %) ; n° 27 aéronefs : 185 424 668 (18 %) ; n° 40 énergies renouvelables : vide ; n° 41 exploration/production d'hydrocarbures : 616 920 000 (18 %) ; n° 42 aérodynes militaires : vide ; n° 43 sulfate de baryum naturel : 2 244 465 (18 %) ; n° 47 matériels de nettoiement des villes : 1 793 239 (10 %) ; n° 48 radio-télédiffusion réseaux publics : vide ; n° 49 envois postaux : 932 953 (18 %). Les colonnes d'appartenance aux taux sont lues sur l'image ; une ligne (n° 9, « 1.16 ») est suspecte.

### e) Recettes globales, pression fiscale, dépenses fiscales, contrôle, fiscalité locale

- p. 27 : fiscalité indirecte interne « un peu plus de 10 % du PIB ».
- p. 29 : 27 FST (fonds spéciaux du Trésor) perçoivent des taxes affectées.
- p. 109 : DGE : « 1600 entreprises » en contrôle approfondi ; grandes entreprises = « 70 % des recettes fiscales ».
- p. 97 : plafond des transactions en espèces : 20 000 D, puis 10 000 D, puis 5 000 D (LF complémentaire 2014) ; comparaison internationale : France 2 000 TND, Belgique 6 000 TND, Maroc 2 000 TND, Algérie 1 000 TND.
- p. 16 (Executive Summary, p. 16) : représentation par avocats/conseillers fiscaux pour litiges > 100 000 TND. P. 105 : suspension d'exécution de l'arrêté de taxation d'office ramenée à 10 % (15 % si espèces).
- Fiscalité locale : p. 13 : receveurs, comptables publics de 20 % à 80 % en 5 ans ; p. 82 : coût supplémentaire de **600 kdt/an** (200 receveurs × 15 kdt/an sur 5 ans) ; p. 83 : prescription des dettes locales de 4 à 10 ans ; p. 84 : abattement de 10 % pour paiement de la TIB avant fin février, pénalité de retard de 0,75 % à 2 % par mois ; p. 85 : taxes sur l'habitation (TIB + FNAH) : 11 % au lieu de 12 % (8 % TIB + 4 % FNAH), 13 % au lieu de 14 % (10 + 4), 15 % au lieu de 16 % (12 + 4), 17 % au lieu de 18 % (14 + 4) ; p. 91 : ressources globales des collectivités locales pour 2015-2019 pour atteindre **8 % du budget de l'État ou 4 % du PIB** ; p. 92 : parts de TVA et de taxe de circulation à fixer (« …% » laissés en blanc dans le texte).
- Aucune série historique de recettes fiscales ni de pression fiscale n'est présente.

#### 2014-11_anf_projet_reforme_fiscale_AR.pdf

- **Titre** : « مشروع إصلاح المنظومة الجبائية — الاستشارة الوطنية حول إصلاح المنظومة الجبائية » (Projet de réforme du système fiscal ; Consultation nationale sur la réforme du système fiscal), Ministère de l'Économie et des Finances, 12 et 13 novembre 2014, Hôtel Le Palace, Gammarth (p. 1).
- **Auteur** : MEF ; **nature** : diaporama (110 p., arabe), traduction de la version française (sommaire identique ; 110 p. contre 123 : mise en page différente, plusieurs diapositives regroupées). Texte extractible (bidi inversé mais les chiffres sont lisibles).
- **Chiffres absents ou différents du français** (comparaison automatique des nombres puis lecture) :
  - p. 9 (diagnostic IRPP) : forfait d'assiette BNC : « contribution faible aux ressources fiscales (**2,6 % en 2013 et 4,1 % en 2014** de l'impôt sur le revenu) » (le FR dit 3 %) ; revenus fonciers : « **0,6 %** de l'impôt sur le revenu » (le FR dit 1 %).
  - p. 69 : TVA grossistes en alimentation générale/pharmacie, suppression du seuil de 100 000 dinars : **158,9 MD** (FR p. 72 : 14,4 MD).
  - p. 72 : suppression de la majoration de 25 %, achats de non-assujettis auprès d'industriels, grossistes, artisans : **34,5 MD** (FR p. 75 : 17,9 MD).
  - p. 104 : « 192 procédures » fiscales inventoriées (simplification des formalités ; absent du FR).
  - p. 11 : forfaitaires : 60 % des inscrits au fichier, 0,2 % des recettes, 45.000 interventions, 12 MD (identique au FR).
- Les autres nombres divergents sont des différences de notation décimale (point/virgule, séparateurs de milliers). Les estimations d'impact IS, IRPP, TVA recopiées plus haut figurent dans les deux versions.

#### 2014-11_anf_discours_ministre.pdf

- **Titre** : « كلمة السيد وزير الاقتصاد والمالية بمناسبة الاستشارة الوطنية حول إصلاح المنظومة الجبائية يومي 12 و13 نوفمبر 2014 » (Allocution du ministre de l'Économie et des Finances à l'occasion de la consultation nationale sur la réforme du système fiscal, 12-13 nov. 2014) ; République tunisienne, MEF, 12 novembre 2014.
- **Auteur** : ministre de l'Économie et des Finances (nom non indiqué sur le document) ; destinataires cités : chef du gouvernement, gouverneur de la BCT, UTICA, représentants de la Banque mondiale, de la BAD et d'autres institutions internationales. **Nature** : discours, 7 p., arabe, texte extractible (accents arabes dégradés par l'extraction, lisible).
- **Chiffres** : aucun tableau ni donnée statistique. Dates et jalons : réforme lancée début 2013 ; diagnostic en 2012-2013 ; validation par le Conseil national de la fiscalité en novembre 2013 ; six domaines (impôts directs, indirects, fiscalité locale, concurrence loyale et lutte contre l'évasion, modernisation de l'administration, révision du régime forfaitaire pour le réserver à ses ayants droit et intégrer l'économie parallèle) ; lois de finances et de finances complémentaire 2014 citées pour le régime forfaitaire ; projet de loi de finances 2015 déposé fin octobre, avec la « Majalla » unifiée des impôts (code unique) ; entrée en vigueur annoncée au 1er janvier 2015.

#### 2014-10_jr_reforme_fiscale_decentralisation_fiscalite_locale.pdf

- **Titre** : pas de titre propre sur la première page (« Présenté par MAZIGH MOHAMED LAZHAR, Directeur des finances locales, Ministère de l'Économie et des Finances, octobre 2014 ») ; contenu : « Caractéristiques de la fiscalité locale tunisienne » et « Axes de réforme des finances locales ».
- **Auteur** : Mohamed Lazhar Mazigh, directeur des finances locales, MEF. **Nature** : diaporama, 11 p., français, texte extractible ; les graphiques p. 3-4 n'ont pas de valeurs dans la couche texte pour p. 4 (lu visuellement).
- **Chiffres** :
  - p. 2 : finances locales « près de **4 %** de la finance publique » et « ne dépassent guère **2 % du PIB** ».
  - p. 3, « Structure des ressources ordinaires des CL », en MD :

| | 2010 | 2011 | 2012 | 2013 |
|---|---|---|---|---|
| Ressources propres fiscales | 336 | 231 | 312 | 359 |
| Ressources propres non fiscales | 68 | 39 | 59 | 61 |
| Fonds commun des CL | 132 | 145 | 176 | 197 |
| Dotation exceptionnelle de l'État | 0 | 147 | 95 | 76 |

  - p. 4, « Structure des ressources fiscales des CL » (secteurs, année non indiquée) : TCL 40 %, produit des marchés 15 %, TIB 10 %, surtaxe 9 %, taxe hôtelière 5 %, TTNB 5 %, autres 16 %.
  - p. 5-10 : six axes de réforme (assainissement, rendement, dotations/FCCL, partage des ressources, autonomie, Fonds de développement régional et local) ; décret n° 97-1428 cité (p. 6) ; aucun autre chiffre.

#### 2014-10_jr_mansour_investissement_et_croissance.pdf

- **Titre** : « Journée de réflexion sur la réforme fiscale – investissement et croissance », Mario Mansour, Département des finances publiques, **FMI**, Tunis, 1er octobre 2014.
- **Nature** : diaporama, 4 p., français, texte extractible. **Chiffres** : aucun. Contenu : questions fondamentales (neutralité ou distorsions), limites des exonérations temporaires, coût du travail et contributions sociales, taux élevé de la fiscalité des bénéfices (« réforme récente importante, est-elle crédible ? »), TVA agissant en partie comme impôt sur la production ; tendances internationales (neutralité, taux faibles, subventions directes ciblées).

#### 2014-10_jr_mansour_justice_et_equite.pdf

- **Titre** : « Journée de réflexion sur la réforme fiscale – justice et équité », Mario Mansour, Département des finances publiques, **FMI**, Tunis, 1er octobre 2014.
- **Nature** : diaporama, 5 p., français, texte extractible. **Chiffres** : seulement « taux de TVA à 6 % » (p. 3) et « CI de 1993 » (code d'incitations, p. 4). Contenu : manque d'indicateurs d'équité, fiscalité affectée comme handicap, tableau p. 5 « À chaque impôt son rôle » (rôle principal / rôle actuel pour impôts sur les bénéfices, impôt sur le revenu « principalement sur les salaires », taxes sur la consommation, taxes foncières « localités largement financées par des taxes affectées basées sur le CA »).

#### 2014-10_jr_mef_fiscalite_juste_citoyenne.pdf

- **Titre** : « Réforme fiscale en Tunisie : pour une fiscalité juste, citoyenne et au service de l'investissement », Panel 3 : Décentralisation et fiscalité locale, Dr. Markus Steinich ; logos de la coopération allemande (Deutsche Zusammenarbeit) et de **GIZ** (« Mis en œuvre par la : GIZ »). La date en pied de page est **22.10.2014** (et non le 1er octobre : date de la diapositive, probablement du fichier source).
- **Nature** : diaporama, 11 p., français, texte extractible. **Chiffres** : aucun. Contenu : articles 132, 134, 135, 136, 137 et 139 de la Constitution de janvier 2014 (autonomie financière des collectivités locales, transfert de ressources accompagnant les compétences, solidarité, péréquation) ; schémas compétences/ressources (propres, conjointes, transférées) ; coopération GIZ (groupes de travail sur la décentralisation fiscale et le développement régional, budget participatif).

#### 2014-10_jr_reforme_fiscalite_locale_elements_discussion.pdf

- **Titre** : « Réforme de la fiscalité locale en Tunisie : éléments de discussion » (la première page porte la coquille « Réfome de la fiscale locale »), Christian Valenduc, Service d'études du ministère des Finances (Belgique), professeur à l'UCLouvain et à l'Université de Namur. Date non indiquée sur le document (Journée du 1er octobre 2014 selon le nom du fichier).
- **Nature** : diaporama, 9 p., français, texte extractible. **Chiffres** : aucun. Contenu : avantages/inconvénients de la décentralisation, financement selon les besoins ou selon les ressources, « voie médiane » (autonomie fiscale à la marge) ; pour la Tunisie : sortir de la « fausse autonomie » des recettes affectées, éventuels additionnels à l'impôt sur le revenu (impossible avec un impôt cédulaire), impôts locaux restreints (foncier, taxes de séjour, voitures).

#### 2014-10_jr_tunisia_tax_incentives_sept2014.pdf

- **Titre** : « Incitations fiscales – coûts/bénéfices et l'expérience mondiale », Jan Loeprick, PSD Specialist, Groupe de la **Banque mondiale** (logo World Bank Group sur les pages ; adresse du bureau de Tunis p. 18), pour le ministère de l'Économie et des Finances, septembre 2014.
- **Nature** : diaporama, 18 p., français (tableaux et graphiques partiellement en anglais), texte extractible ; p. 7, 10-13, 16 sont des graphiques.
- **Chiffres** :
  - p. 3 : prévalence des incitations par région (exonérations/congés fiscaux, taux réduits, etc.), source James (Banque mondiale) : 7 colonnes de pourcentages par région (ex. Moyen-Orient et Afrique du Nord, 15 pays : 80 %, 40 %, 13 %, 0 %, 0 %, 80 %, 27 %).
  - p. 5 : enquêtes sur l'effet des incitations ; ligne **Tunisie (2012) : 58 %** des investisseurs disent que les incitations ont influencé le niveau d'investissement, avec un ratio de redondance de **25 %** (les autres : Malaisie 81/33, Guinée 92/6, Jordanie 70/28, Kenya 61/11, etc.).
  - p. 15 : enquête Tunisie : « Votre entreprise aurait-elle investi sans les incitations ? » : ensemble Oui **61,2 %** / Non **38,8 %** ; offshore : Oui **56,5 %** / Non **43,5 %** ; onshore : Oui **65,7 %** / Non **34,3 %** (attribution contrôlée à l'image de la p. 15 le 6 octobre 2026 : le grand graphique, titré « Votre entreprise aurait-elle investi s'il n'y avait pas les incitations à l'investissement ? », porte 61,2 / 38,8 ; les deux petits, titrés « (Off-Shore) » et « (On-Shore) », portent 56,5 / 43,5 et 65,7 / 34,3 ; erratum signalé dans `fiscalite-depenses-fiscales.md`, § 3.2).
  - p. 16 (graphique lu visuellement), « Coût net des avantages fiscaux par année », millions de dinars, source Impôts, Douanes, CNSS, API, APIA :

| | 2009 | 2010 | 2011 |
|---|---|---|---|
| Déductions impôts redondantes | 839 | 948 | 907 |
| Déductions douanes redondantes | 405 | 504 | 394 |
| Impôts additionnels | −22 | −23 | −23 |
| Droits de porte additionnels | −107 | −125 | −120 |
| Coût fiscal net | 1115 | 1304 | 1158 |

  - p. 17 (conclusions de l'analyse coûts/bénéfices) : 90 % des incitations concentrées sur environ **2 500 entreprises** sur un total d'environ **24 000** bénéficiaires ; coût des incitations fiscales et financières estimé à **1,2 milliard de dinars en 2009, soit 2,2 % du PIB** ; coût total des incitations fiscales et douanières **6 362 dinars annuels par emploi**, environ **30 000 dinars annuels par emploi** rapporté aux emplois additionnels estimés.
  - p. 7 : graphique « dépenses fiscales en % du PIB » (échelle 0-10 %) sans valeurs lisibles par pays ; p. 13 : cas de l'Inde (exportations, IDE, ratio impôt/PIB 1995-2012), séries non recopiables.

#### 2014-10_jr_tax_reform_roundtable3_modelisation.pdf

- **Titre** : « La réforme fiscale en Tunisie : vers un régime fiscal plus simple et plus équitable » (bandeau : « Développements récents dans l'analyse et la modélisation de l'impôt »), James H. Wooster, **USAID / Pragma**, atelier « Réforme fiscale en Tunisie : pour une fiscalité juste, citoyenne et au service de l'investissement », 1er octobre 2014 (table ronde 3).
- **Nature** : diaporama, 8 p., français, texte extractible. **Chiffres** : aucun. Contenu : modèles de micro-simulation de l'IRPP, de la TVA et de l'IS aux mains de la DGELF/DGI (« MOF DGELF / DGI ont maintenant des outils développés ») ; méthode : déclarations de contribuables, calcul sous la loi actuelle, recalcul sous la loi proposée, comparaison ; limites : timing, conformité, comportements.

#### 2014-10_jr_decentralisation_fiscalite_locale_mf.pdf

- **Titre** : « Réforme fiscale en Tunisie : Décentralisation et fiscalité locale en Tunisie — Document benchmarké (Tunisie, France, Maroc, Slovaquie, Tahiti, Rwanda) », par **Nabil Abdellatif, président de l'Ordre des experts comptables de Tunisie** ; daté du 01/10/2014 (pied de page).
- **Nature** : diaporama, 28 p., français, texte extractible sauf p. 7-9 (tableaux en image, lus visuellement).
- **Chiffres** :
  - p. 10 : recettes fiscales de l'ensemble des communes ≈ **2,4 %** des recettes fiscales de l'État ; comparaisons : Maroc 4,8 %, France 15,2 %, Angleterre 12 %, Allemagne 48 %, États-Unis 43 % ; fiscalité du conseil régional en 2013 : **16,3 MD** sur **1560,7 MD** de recettes des conseils régionaux, et sur **375,1 MD** de recettes fiscales locales.
  - p. 9 (tableau en image, MD ; rubriques communes / conseils de gouvernorats / total) :

| Rubrique | 2007 (comm. / gouv. / total) | 2008 | 2012 | 2013 |
|---|---|---|---|---|
| 1. Ressources ordinaires | 427,3 / 40,1 / 467,4 | 456,0 / 42,4 / 498,4 | 643,1 / 74,4 / 717,5 | 692,4 / 63,0 / 785,4 |
| Ressources fiscales | 243,8 / 12,2 / 256,0 | 252,1 / 13,2 / 265,3 | 311,9 / 12,7 / 324,6 | 358,8 / 16,3 / 375,1 |
| Ressources non fiscales | 78,5 / 9,6 / 88,1 | 91,7 / 9,7 / 101,4 | 54,5 / 6,4 / 60,9 | 61,3 / 8,4 / 69,7 |
| Quote-part sur FCCL | 105,0 / 18,3 / 123,3 | 112,2 / 19,5 / 131,7 | 176,1 / 30,2 / 206,3 | 196,2 / 34,6 / 230,8 |
| 2. Ressources de développement | 132,8 / 550,4 / 683,2 | 147,6 / 584,5 / 732,1 | 100,6 / 25,1 / 125,7 | 76,1 / 3,7 / 79,8 |
| Ressources propres | 36,0 / 80,3 / 116,3 | 117,5 / 113,8 / 231,3 | 170,5 / 537,4 / 707,9 | 238,3 / 687,7 / 926,0 |
| Crédits délégués | 96,8 / 470,1 / 566,9 | 30,1 / 470,7 / 500,8 | 34,3 / 644,0 / 678,3 | 56,0 / 808,5 / 864,5 |
| 3. Ressources d'emprunts | 26,1 / 2,6 / 28,7 | 24,6 / 1,9 / 26,5 | 24,2 / 1,8 / 26,0 | 33,5 / 1,5 / 35,0 |
| TOTAL | 586,2 / 593,1 / 1179,3 | 628,2 / 628,8 / 1257,0 | 872,1 / 1257,6 / 2129,7 | 1020,2 / 1560,7 / 2580,9 |

    Le tableau est une image de basse résolution (certains totaux 2007 : « 467;4 », valeurs lues avec incertitude ; les lignes « ressources de développement » 2012-2013 sont incohérentes avec leurs sous-lignes dans l'image : à vérifier sur l'original avant tout usage).
  - p. 7-8 : tableau (image) des attributions communes/gouvernorats (état civil, ordre public, foncier-urbanisme, eau-assainissement, déchets ménagers, énergie, transports urbains), sans chiffre.
  - p. 2-6, 11-27 : cadre constitutionnel (art. 14, 131 à 142), principes de la décentralisation fiscale, fiscalité communale, difficultés (art. 34 al. 7 de la Constitution de 1959, art. 11 de la loi organique du budget des collectivités locales du 22/01/1997), diversification des ressources ; aucun autre chiffre.

---

### Inventaire H : autres présentations du ministère, 2013-2014

Remarques générales. (1) Aucun de ces huit documents ne donne de chiffre sur le nombre de forfaitaires ni sur les recettes de l'impôt forfaitaire ; les seules mentions du régime forfaitaire (« système d'estimation », النظام التقديري, nidham taqdiri) sont des mesures, listées ci-dessous (LFC 2014 p. 5 ; LF 2015 pp. 53, 69, 70, 78 ; séminaire pp. 23, 32). (2) Les deux « conférences de presse du ministre » ne sont PAS des présentations fiscales du ministre Ben Hammouda : ce sont des présentations de la Commission nationale de gestion des avoirs et fonds objets de confiscation (2012-2013). Aucun lien avec la fiscalité hors les recettes de confiscation. (3) Les diaporamas arabes LFC 2014 et le rapport 2014 (arabe) ont une couche texte inversée ou illisible ; la LF 2015 a une couche texte avec chiffres inversés (« 5102 » pour 2015) : tous les chiffres ci-dessous ont été relus visuellement sur les pages. Aucune page n'est un scan sans texte.

#### 2014-03_conference_presse_ministre_fr.pdf

- Titre : « Commission Nationale de Gestion d'Avoirs et des Fonds objets de Confiscation ou de Récupération en faveur de l'Etat — Présentation des principaux axes de gestion des biens confisqués » ; sous-titre p. 2 « La gestion des participations ». Pas de nom du ministre.
- Date : non portée sur la page ; métadonnées PDF créées le 19/03/2013 (PowerPoint 2007) ; contenu : bilan de l'année 2012, opérations de novembre-décembre 2012, reprise prévue en 2013. Le nom de fichier « 2014-03 » est donc trompeur.
- Auteur : la Commission (pas de signature individuelle). 24 pages, français (quelques mots arabes), diaporama. Pas de page-image sans texte hors logos/schémas (pp. 6, 16 : schémas à pourcentages ou logos ; p. 24 : tableau lisible visuellement).
- Contenu fiscal : aucun. Seul tableau chiffré : p. 24 « Les recettes nettes de l'année 2012 » (MTND ; recette / remboursement des crédits) : 60 % d'Ennakl SA (dont 4 % revenant à Zitouna Banque) 212 / 67 ; 66 % de City Cars (KIA) 114 ; 13 % de la Banque de Tunisie 217 / 5 ; revenus de l'opération Tunisiana 713 / 546 ; liquidation des titres SICAV 121 ; recettes liquides (fonds de Sidi Dhrif) 41 ; liquidation des comptes bancaires 44 ; sociétés vendues à la CDC Développement 200 ; autres 7 ; total 1 669 recettes / 618 remboursements ; total net 1 051 MTND.
- Autres chiffres : Ennakl 231 MTND (action 12,85 TND, p. 6) ; City Cars 114 MTND (p. 7) ; Banque de Tunisie 217,6 MDT, action 14,88 TND (pp. 9-10) ; offres Tunisiana 790 / 616 puis 834 MTND (p. 14), put QTEL 15 % à 360 MUSD (p. 15).

#### 2014-03_conference_presse_ministre_2.pdf

- Titre (arabe) : « اللجنة الوطنية للتصرف في الأموال والممتلكات المعنية بالمصادرة أو الاسترجاع لفائدة الدولة — الندوة الصحفية عدد 1 : الإعلان عن انطلاق عمليات التفويت في المساهمات المصادرة » (Commission nationale de gestion des biens objets de confiscation ou de récupération au profit de l'État — conférence de presse n° 1 : annonce du lancement des cessions de participations confisquées).
- Date : 26 juillet 2012 (indiquée p. 1) ; PDF converti le 25/04/2013. 10 pages, arabe, diaporama, texte extrait lisible.
- Contenu fiscal : aucun. Chiffres p. 2 des avoirs confisqués : 114 personnes physiques ; 223 sociétés ; 300 (sociétés ?) ; 550 immeubles ; 48 navires et yachts ; 83 chevaux ; 40 portefeuilles ; 367 comptes bancaires et liquidités (attribution des chiffres aux libellés incertaine, schéma). P. 5 : répartition sectorielle des participations en pourcentages (graphique non transcrit). Calendrier de cession de 25 % de Tunisiana (offres le 2 novembre) et de la société de transport automobile (offres fin novembre).

#### 2014-07_lfc2014_presentation_synthese.pdf

- Titre : « على طريق الإنتعاش الإقتصادي — مشروع قانون المالية التكميلي لسنة 2014 » (Sur la voie de la reprise économique — projet de loi de finances complémentaire pour 2014), Ministère de l'Économie et des Finances, 4 juillet 2014. 22 pages, arabe, diaporama ; couche texte illisible, tout lu visuellement. Source citée sur chaque diapositive : ministère de l'Économie et des Finances. Numéro de diapositive = page PDF moins 1.
- Régime forfaitaire (p. 5, diapositive 4, rubrique « Consolider le devoir fiscal ») : ouverture exceptionnelle, avant la fin de l'année, d'un délai de régularisation pour les contribuables du régime forfaitaire (النظام التقديري) en défaut de dépôt de déclaration (déclarations tardives ou rectificatives) ; incitation à passer au régime réel : toute personne en régime forfaitaire ou en base forfaitaire qui passe au réel bénéficie d'une déduction d'une partie du bénéfice sur les trois premières années (75 %, 50 %, 25 %) à partir de l'entrée dans le réel ; possibilité pour les personnes exerçant une activité non déclarée (informel) de régulariser avec exonération des impôts, droits, pénalités et amendes ; renforcement de l'acquittement du minimum d'impôt des professions non commerciales (fixé par référence à l'impôt dû par des personnes exerçant la même activité dans la fonction publique, ou au taux de l'impôt de la profession concernée pour les activités non commerciales ; à partir de la 4e année d'activité). Aucun chiffre de contribuables ni de recettes.
- P. 6 (diap. 5) : liaison de l'enregistrement des actes de mutation immobilière et fonds de commerce avec la régularisation fiscale ; accès du fisc aux relevés de comptes bancaires à partir de 2015 ; contribuables en défaut qui régularisent des dépôts effectués avant le 1er janvier 2014 : déclaration au plus tard le 31 décembre 2014 et paiement de 15 % de la valeur.
- P. 7 (diap. 6) : lutte contre le commerce parallèle : délai de prescription 15 ans pour contrebande ; baisse de la fiscalité sur certains produits (climatiseurs, bananes, fruits secs, certains appareils électriques/électroniques) ; aggravation des sanctions.
- P. 8 (diap. 7) : TVA ramenée à 6 % sur les équipements importés sans équivalent fabriqué localement (taux antérieur 12 %, voir p. 17 : « de 12 à 6 % », coût 50 MD) ; programme d'aide aux PME ; relèvement des taux d'amortissement/ crédit d'impôt pour investissements en zones de développement régional (relèvement de la quote-part des salaires nouveaux et des fonds propres) ; prorogation jusqu'au 31/12/2019 du délai d'introduction en bourse donnant droit au taux réduit d'IS.
- P. 9 (diap. 8) : subventions (ciment, brique, électricité et gaz, hausse en mai plutôt qu'en juin 2014).
- P. 10 (diap. 9) : mesures sociales : relèvement du SMIG et SMAG ; allocation aux familles nécessiteuses de 110 à 120 dinars et bénéficiaires de 235 000 à 250 000 ; suspension de la TVA sur acquisitions financées par dons en coopération internationale.
- P. 11 (diap. 10) : mobilisation de ressources : environ 950 MD au 2e semestre 2014 (régularisation voitures FCR des Tunisiens à l'étranger, droit de 30 D à la sortie des non-résidents, droit de passeport/ carte de séjour étrangers de 15 à 100 D, droit de timbre sur factures de téléphone, contribution exceptionnelle conjoncturelle de 2014 de toutes sociétés et personnes physiques : environ 320 MD de rendement, accélération du règlement des dossiers en cours de vérification).
- P. 12 (diap. 11) : rationalisation : économie totale 1 580 MD ; économie nette 500 MD compte tenu des nouvelles pressions.
- P. 14 (diap. 13) : pressions sur le budget 2014, MD : manque de ressources 1 924 ; nouveaux besoins de dépenses 1 411 ; arriérés 2013 1 195 ; total 4 530. Croissance 2013 à prix constants ramenée de 3,6 % à 2,3 % ; 2014 de 4 % à 2,8 %.
- P. 15 (diap. 14) : détail du manque de ressources, MD : suppression des taxes (الأتاوات) -120 ; révision des hypothèses de croissance 2013 et 2014 -280 ; ressources alourdies (supplémentaires) -400 ; contrepartie : prélèvements exceptionnels +631 (fiscalité pétrolière exceptionnelle 250 MD, excédent de redevance 150 MD, 231 MD d'amélioration des recouvrements) ; net recettes fiscales -169 ; recettes non fiscales -900 (dividendes -200, programme de confiscation -700) ; emprunts -855 (sukuk -635, UE -220) ; total -1 924.
- P. 16 (diap. 15) : nouveaux besoins 1 411 MD : établissements publics 623 (CNRPS 406, Tunisair 217) ; salaires 238 ; organes constitutionnels 130 ; développement et financement public 250 ; divers 170.
- P. 17 (diap. 16) : arriérés 2013 : 2 565 MD ramenés à 1 195 (FMI 812, Turquie 320, solde tranche 184, don UE 54) ; 26 MD fin mai 2014.
- P. 18 (diap. 17) : mesures de ressources propres 6 mois 2014, MD : recettes fiscales 864 dont droit de sortie 75, actualisation droits vignette taxis 7, fiscalité véhicules à double usage 15, régularisation véhicules FCR 100, facilitation de la conciliation 3, droit à l'occasion de la publication des affaires aux tribunaux 50, relèvement taxes factures de téléphone 16, droit de timbre sur contrats de mariage 1, carte de séjour 1, assujettissement des coupons Promosport au droit de 100 millimes 4, accélération des dossiers en vérification 160, recouvrement des dettes alourdies 50, relèvement du prix du tabac 50, lutte contre fraude et contrebande 100, contribution exceptionnelle 30, baisse de la TVA sur équipements de 12 à 6 % : -50, baisse du taux de change : -38 ; non fiscales 249 (don Algérie 84, apurement OACA 165) ; total 1 113 MD (la p. 20 retient 1 133 MD de ressources, écart non expliqué).
- P. 19 (diap. 18) : mesures de dépenses : -1 608 (économie sur subventions -147, fonctionnement -495, développement -941) ; échéancier de certains établissements -178 (CNRPS -156, Tunisair -22) ; total -1 761 MD.
- P. 20 (diap. 19) : bilan : pressions 4 530 ; mesures 2 874 (ressources 1 133, dépenses -1 761 ; décompte tel que lu) ; réduction des pressions nette 1 656. Budget initial 2014 : 28 125 MD, déficit 5 852 MD (6,9 % du PIB) ; sans mesures 29 358, déficit 7 632 (9,2 %) ; effet des mesures sur le déficit 2 790 MD (3,4 %) ; LFC 2014 : 27 775 MD, déficit 4 842 (5,8 %).
- P. 21 (diap. 20) : tableau « Budget complémentaire 2014 : les équilibres » (MD ; LF initiale / LF sans mesures / mesures nettes / LFC) : ressources propres 20 287 / 19 218 / +44 / 20 331 ; recettes fiscales 17 897 / 17 728 / +695 / 18 592 ; recettes non fiscales 2 390 / 1 490 / -651 / 1 739 ; emprunts 7 838 / – / – / 7 444 ; total ressources 28 125 / – / – / 27 775 ; dépenses de gestion 17 750 / 18 172 / -220 / 17 530 (salaires 10 555 / 10 793 / -50 / 10 505) ; développement 5 600 / 6 261 / -280 / 5 320 ; prêts 100 / 250 / +150 / 250 ; service de la dette 4 675 ; total 28 125 / 29 358 / -350 / 27 775 ; déficit -5 852 (-6,9 %) / -7 632 (-9,2 %) / +1 010 / -4 842 (-5,8 %). Aucune ventilation IRPP / IS / TVA dans ce document.
- Pas de graphique d'impôts. P. 22 : remerciements.

#### 2014-10_lf2015_presentation.pdf

- Titre : « مشروع قانون المالية لسنة 2015 — مواصلة دعم الإنتعاش الإقتصادي » (Projet de loi de finances pour 2015 — Poursuivre le soutien à la reprise économique), République tunisienne, Ministère de l'Économie et des Finances, octobre 2014 ; en pied : « نسخة 24 أكتوبر 2014 ». Document Word 2007, 173 pages, arabe, rapport (4 chapitres : conjoncture 2014 p. 3 ; cadre macro p. 28 ; rapport sur le budget p. 83 ; loi de finances 2015 – dispositions annoncée p. 174 dans le sommaire, absente du fichier de 173 pages). Pages = pages PDF = numéros imprimés. Couche texte à chiffres inversés (2015 lu « 5102 ») : chiffres vérifiés visuellement ; la dépense par ministère (pp. 109-173) non inventoriée.
- Régime forfaitaire : 
  - P. 52-53 : projet de réforme fiscale entamé en 2012, six chantiers dont le n° 6 : « révision du régime forfaitaire dans le sens de sa réservation à ses seuls ayants droit et de l'intégration de l'économie parallèle dans le circuit économique organisé » ; phase finale en 2014, consultation nationale élargie prévue en novembre 2014, études d'impact en cours.
  - P. 69 : réviser le régime forfaitaire et conciliation avec les contribuables forfaitaires pour les inciter à passer au réel ; comptabilité simplifiée pour les professions non commerciales dont le chiffre d'affaires annuel ne dépasse pas 150 000 dinars ; délai de régularisation pour l'informel ; minimum d'impôt des professions non commerciales aligné dès 2015 sur l'impôt dû par des personnes exerçant la même activité dans la fonction publique.
  - P. 70 : décret n° 2939 de 2014 du 1er août 2014 (liste des activités exercées par des entreprises dans les zones communales exclues du régime forfaitaire à partir de 2015) ; rappel des mesures LF 2014 : durcissement du régime forfaitaire (BIC) par relèvement de l'impôt minimum, obligation de facturation, exclusion de certaines activités ; pour les BNC, réduction de la part des charges déductibles de 30 % à 20 % ; généralisation de la retenue à la source.
  - P. 76 (mesure 7) : suppression de la possibilité d'imputer sur l'impôt annuel l'impôt minimum de 0,2 % du chiffre d'affaires (l'impôt minimum fixé à 0,1 % étant définitif et non imputable) ; p. 78 (mesure 20) : distributeurs du secteur des communications : retenue à la source de 1,5 % de la commission au lieu de 15 % (« en raison de la multiplicité des distributeurs et de la faiblesse de leur marge, avec ouverture au régime forfaitaire »).
  - Aucun chiffre sur le nombre de forfaitaires ni sur les recettes de l'impôt forfaitaire.
- Mesures de la LF 2015 (pp. 74-82, 41 mesures, « aucune nouvelle disposition fiscale à incidence financière supplémentaire pour les secteurs organisés » p. 74) : 1) retenue à l'exportation abaissée de 5 % à 2,5 % et de 1,5 % à 0,5 % ; 2) entreprises exportatrices autorisées à vendre localement 50 % (au lieu de 30 %) du chiffre d'affaires 2014 ; 3) restitution du crédit de TVA/IS sous 7 jours pour les grandes entreprises ; 7) voir ci-dessus ; 9) retenue à la source généralisée sur les établissements stables d'entreprises étrangères (5 %) ; 10) jus de fruits : droit de consommation de 25 % ; 20) voir ci-dessus ; 27) exonération de la retenue à la source de 1,5 % pour les personnes physiques agricoles et pêche ; 28) TVA de 18 % à 12 % sur électricité basse et moyenne tension ménagère et irrigation ; 29) produits d'aide à l'arrêt du tabac : 12 % de TVA, exonération de droits de douane et de droit de consommation ; 39) plafond minimal du compte d'épargne postale relevé de 2 à 10 dinars ; 40) droit au profit du Trésor de 1 % sur tout paiement en espèces supérieur à 5 000 D auprès des comptables publics ; 41) droit de timbre sur déclarations d'importation de devises de 3 à 10 D. Coût ou rendement par mesure : non donnés.
- Recettes fiscales (MD) :
  - P. 99, tableau 1 « Répartition des ressources du budget de l'État et leur évolution (2010-2015) », colonnes 2010 / 2011 / 2012 / 2013 / 2014 LFC / 2014 actualisé / 2015 estimations : ressources propres 14 823 / 16 753 / 18 504 / 19 960 / 20 331 / 20 390 / 21 595 ; recettes fiscales 12 699 / 13 630 / 14 864 / 16 334 / 18 592 / 18 733 / 19 820 ; non fiscales 2 124 / 3 123 / 3 640 / 3 626 / 1 739 / 1 657 / 1 775 ; emprunts et trésorerie 3 061 / 3 997 / 4 755 / 6 455 / 7 444 / 6 941 / 7 405 ; total 17 884 / 20 750 / 23 259 / 26 415 / 27 775 / 27 331 / 29 000.
  - P. 101, tableau 2 « Évolution des recettes fiscales », 2010 / 2011 / 2012 / 2013 / 2014 LFC / 2014 actualisé / 2015 : impôts directs 5 033 / 5 914 / 6 089 / 7 118 / 8 229 / 8 456 / 8 672 ; impôt sur le revenu 2 600 / 2 873 / 3 188 / 3 710 / 4 116 / 4 136 / 4 430 ; IS pétrolier 813 / 999 / 1 285 / 1 710 / 1 867 / 1 768 / 1 590 ; IS non pétrolier 1 620 / 2 042 / 1 616 / 1 698 / 2 246 / 2 552 / 2 652 ; impôts indirects 7 666 / 7 716 / 8 776 / 9 216 / 10 363 / 10 277 / 11 148 ; droits de douane 564 / 561 / 715 / 729 / 880 / 860 / 844 ; TVA 3 750 / 3 849 / 4 376 / 4 449 / 4 822 / 4 885 / 5 338 ; droit de consommation 1 563 / 1 469 / 1 598 / 1 547 / 1 734 / 1 676 / 1 841 ; autres droits et taxes 1 789 / 1 837 / 2 087 / 2 490 / 2 927 / 2 856 / 3 125 ; total 12 699 / 13 630 / 14 865 (14 864 dans le tableau 1) / 16 334 / 18 592 / 18 733 / 19 820. Pression fiscale 2015 : 22,2 % (20,4 % hors fiscalité pétrolière). Directs 44 % et indirects 56 % du total 2015.
  - P. 102, graphique 3 : part des impôts directs dans les recettes fiscales : 1990 18,6 % ; 1995 23,2 % ; 2000 28,1 % ; 2005 36,5 % ; 2010 39,6 % ; 2011 43,4 % ; 2012 41,0 % ; 2013 44,7 % ; 2014 43,3 % ; 2015 44,0 %.
  - P. 103, tableau 3 « Impôts directs » (2013 résultats / 2014 LF / LFC / actualisé / 2015 LF) : impôt sur le revenu 3 710 / 4 221 / 4 116 / 4 136 / 4 430 ; salaires 3 068 / 3 517 / 3 378 / 3 300 / 3 629 ; autres ressources 643 / 704 / 738 / 836 / 801 ; IS 3 407 / 3 522 / 4 113 / 4 320 / 4 242 ; IS pétrolier 1 710 / 1 552 / 1 867 / 1 768 / 1 590 ; IS non pétrolier 1 698 / 1 970 / 2 246 / 2 552 / 2 652 ; total 7 118 / 7 743 / 8 229 / 8 456 / 8 672. (Le tableau 2 donne 7 118 et l'IS 2013 = 1 710 + 1 698 = 3 408, valeurs imprimées telles quelles.) La part des salariés (retenue à la source sur traitements et salaires) est 3 629 sur 4 430 d'IR en 2015 : 82 %.
  - P. 102 : IS non pétrolier 2015 +3,9 % ; effet des mesures LF 2014 : taux d'IS ramené de 30 % à 25 % et relevé à 10 % pour l'exportation ; IS pétrolier -10,1 % (recouvrements exceptionnels 250 MD en 2014).
  - P. 103-105 : TVA +9,3 % en 2015, dont 11,2 % du régime intérieur et 3,7 % à l'importation ; effet de la baisse de 12 % à 6 % sur les équipements : environ 100 MD ; part de la TVA à l'importation 51 %, intérieure 49 %. Droit de consommation 1 841 MD 2015 : tabac 746 (pourcentages tels qu'imprimés : tabac 746 MD, « 13 % », voitures 287 (11,7 %), produits pétroliers 281 (4,5 %), boissons alcoolisées 327 (7,9 %), autres produits 200 (7 %)) ; une partie des pourcentages imprimés est manifestement erronée (tabac), à ne pas citer sans contrôle. Droits de douane -1,9 % (régularisation des véhicules). Autres droits +9,4 % (droit de sortie 190 MD, timbre factures et cartes téléphoniques 32 MD, véhicules à double usage 20 MD).
  - P. 104, graphique 4 : part des droits de douane dans les recettes fiscales : 1990 22,8 % ; 1995 22,1 % ; 2000 11,3 % ; 2005 6,4 % ; 2010 4,4 % ; 2011 4,1 % ; 2012 4,8 % ; 2013 4,5 % ; 2014 4,6 % ; 2015 4,3 %.
  - P. 105, tableau 4 : impôts indirects (2013 / 2014 LF / LFC / actualisé / 2015) : droits de douane 729 / 780 / 880 / 860 / 844 ; TVA 4 449 / 4 715 / 4 822 / 4 885 / 5 338 ; droit de consommation 1 547 / 1 704 / 1 734 / 1 676 / 1 841 ; autres 2 490 / 2 955 / 2 927 / 2 856 / 3 125 ; total 9 216 / 10 154 / 10 363 / 10 277 / 11 148. TVA = 47 % des indirects et 27 % du total.
  - P. 106, tableau 5 : recettes non fiscales (2013 / 2014 LF / LFC / actualisé / 2015) : dividendes 1 071 / 500 / 465 / 465 / 550 ; redevance gazoduc 110 / 130 / 130 / 130 / 249 ; dons extérieurs 222 / 214 / 298 / 298 / 211 ; privatisations 1 070 / 0 / 0 / 0 / 0 ; confiscations 524 / 1 000 / 300 / 100 / 200 ; autres 662 / 546 / 446 / 664 / 565 ; total 3 626 / 2 390 / 1 739 / 1 657 / 1 775.
  - P. 90-92 : résultats actualisés 2014 : recettes propres +59 MD sur la LFC ; recettes fiscales +141 MD, à 18 733 MD (+14,7 % sur 2013, +2 400 MD) ; impôts directs +227 MD vs LFC (+1 338 vs 2013), dont IS non pétrolier +306 (+854) ; impôts indirects -86 (+1 061) ; non fiscales -82 ; dépenses -444 MD ; budget 27 331 MD ; déficit 4 139 MD (5 % du PIB) contre 4 842 en LFC ; dette publique 51,5 % du PIB fin 2014 (45,8 % fin 2013). Croissance 2014 actualisée à moins de 2,5 % ; baril 110 $ → moins de 90 $ en septembre-octobre.
  - P. 107-108 : emprunt 2015 7 405 MD (intérieur 3 000, extérieur 4 405), dette publique 47 306 MD, 52,9 % du PIB fin 2015 ; graphique 5 de la dette/PIB 2002-2015 (2002 55,9 % ; 2005 52,4 % ; 2010 40,5 % ; 2013 45,7 %, 2014 51,5 %, 2015 52,9 %).
- Rien dans le document sur dépenses fiscales ni sur fiscalité locale, hors l'annonce du chantier « fiscalité locale » p. 52. Chapitre IV (dispositions de la loi de finances) annoncé p. 174, hors fichier.

#### 2013-10_rapport_projet_budget_etat_2014_ar.pdf

- Titre : « الجمهورية التونسية — وزارة المالية — تقرير حول مشروع ميزانية الدولة لسنة 2014 » (République tunisienne, ministère des Finances, rapport sur le projet de budget de l'État pour 2014), novembre 2013 (sur la couverture ; nom du fichier 2013-10). 97 pages, arabe, rapport ; polices non intégrées, texte extrait lisible après normalisation ; tableaux fiscaux relus visuellement (pp. 18-22). Pas de scan.
- Les abréviations des tableaux : ق م = loi de finances initiale 2013 ; ق م ت = loi de finances complémentaire 2013.
- Hypothèses et mesures (pp. 7-9) : budget 28 125 MD (+2,3 %, +644 MD) ; croissance 4 % en prix constants, 9,6 % en prix courants ; baril 110 $, dollar à 1,670 dinar ; effet des mesures du projet de loi de finances 830 MD, dont 430 MD de mesures fiscales nouvelles et 400 MD de mobilisation de montants alourdis en contentieux et de meilleur recouvrement ; confiscation 1 000 MD ; sukuk 825 MD ; recettes fiscales 17 897 MD contre 16 600 MD, +7,8 % ; pression fiscale 21 % (19 % hors pétrole) ; déficit 5,7 % du PIB contre 6,8 % ; dette publique 41 754 MD (49,1 % du PIB) contre 36 616 MD (47,2 %).
- P. 12 (tableau 2) « Les ressources fiscales » (MD ; 2012 résultats / 2013 LF / 9 mois 2013 / 2013 LFC / 2014 LF) : impôts directs 6 089 / 6 857 / 5 126 / 7 427 / 7 743 (variations 3,0 % / 12,6 % / 16,1 % / 22,0 % / 4,3 %) ; impôts indirects 8 775 / 9 793 / 6 787 / 9 173 / 10 154 (13,7 % / 11,6 % / 3,1 % / 4,5 % / 10,7 %) ; total 14 864 / 16 650 / 11 913 / 16 600 / 17 897 (9,1 % / 12,0 % / 8,3 % / 11,7 % / 7,8 %) ; pression fiscale avec pétrole 21,0 % / 21,3 % / – / 21,4 % / 21,0 % ; hors pétrole 19,1 % / 19,7 % / – / 19,1 % / 19,2 %.
- P. 13 (graphique 2) : part des impôts directs dans les recettes fiscales : 1990 18,6 % ; 1995 23,2 % ; 2000 28,1 % ; 2005 36,5 % ; 2010 39,6 % ; 2011 43,4 % ; 2012 41,0 % ; 2013 44,7 % ; 2014 43,3 % (le texte dit 43 % direct, 57 % indirect ; le graphique donne 43,3 % pour 2014, 44,7 % pour 2013). Croissance 2014 des directs : impôt sur le revenu +12,1 % lié aux mesures du projet de loi ; IS pétrolier -13,8 % ; IS non pétrolier +5,8 %.
- P. 14 (tableau 3) « Impôts directs » (2012 / 2013 LF / 9 mois / LFC / 2014) : impôt sur le revenu 3 188 / 3 835 / 2 782 / 3 765 / 4 221 (11,0 % / 20,3 % / 16,7 % / 18,1 % / 12,1 %) ; traitements et salaires 2 640 / 3 173 / 2 300 / 3 125 / 3 517 (13,5 % / 20,2 % / 16,4 % / 18,4 % / 12,5 %) ; autres ressources 548 / 662 / 482 / 640 / 704 ; IS 2 901 / 3 022 / 2 344 / 3 662 / 3 522 (-4,6 % / 4,2 % / 15,4 % / 26,2 % / -3,8 %) ; IS pétrolier 1 285 / 1 200 / 993 / 1 800 / 1 552 ; IS non pétrolier 1 616 / 1 822 / 1 351 / 1 862 / 1 970 ; total 6 089 / 6 857 / 5 126 / 7 427 / 7 743.
- P. 15-16 : TVA +7,2 % en 2014 (54 % à l'importation, 46 % sur le marché intérieur) ; droit de consommation 1 704 MD : tabac 720 MD (42 %), automobiles 267 (16 %), produits pétroliers 259 (15 %), boissons alcoolisées 246 (15 %), autres 212 (12 %). Graphique 3 : part des droits de douane dans les recettes fiscales : 1990 22,8 % ; 1995 22,1 % ; 2000 11,3 % ; 2005 6,4 % ; 2010 4,4 % ; 2011 4,1 % ; 2012 4,8 % ; 2013 4,4 % ; 2014 4,4 %.
- P. 16 (tableau 4) « Impôts indirects » (2012 / 2013 LF / 9 mois / LFC / 2014) : droits de douane 715 / 750 / 552 / 730 / 780 ; TVA 4 376 / 4 800 / 3 242 / 4 400 / 4 715 ; droit de consommation 1 598 / 2 005 / 1 131 / 1 600 / 1 704 ; autres 2 086 / 2 238 / 1 862 / 2 443 / 2 955 ; total 8 775 / 9 793 / 6 787 / 9 173 / 10 154. TVA = 46 % des indirects, 26 % des recettes fiscales. Part de la retenue à la source dans le recouvrement : 19 % en 2000, 26 % en 2012, 27 % (prévision 2013), 28 % (2014).
- P. 17-18 : recettes non fiscales 2 390 MD (contre 3 945 en LFC 2013) ; tableau 5 (2012 / 2013 LF / LFC / 2014) : dividendes 773 / 1 157 / 1 072 / 500 ; redevance gazoduc 211 / 121 / 119 / 130 ; dons 633 / 400 / 264 / 214 ; privatisations 205 / 300 / 70 / – ; Tunisie Telecom 900 / – / 1 000 / – ; recouvrement des prêts 209 / 148 / 144 / 120 ; confiscations 235 / 900 / 868 / 1 000 ; autres 473 / 299 / 408 / 426 ; total 3 640 / 3 325 / 3 945 / 2 390.
- P. 9 (tableau d'équilibre p. 9 du rapport, p. 12 PDF) : séries 2010-2014 du budget : recettes fiscales 12 699 (2010) / 13 630 / 14 864 / 16 650 / 16 600 (LFC 2013) / 17 897 ; aussi prix du baril et taux du dollar, dépenses (salaires 6 785 → 10 555 ; subventions 1 500 → 4 292), déficit (651 MD en 2010 → 4 852 MD en 2014 hors confiscation 5 852).
- Pas de mention du régime forfaitaire dans le rapport ; le reste (pp. 21 sq.) porte sur les dépenses de l'État, par ministère et la dette (non inventorié).

#### 2014_projet_de_simplification.pdf

- Titre : « Projet de simplification des formalités fiscales et douanières : résultats globaux du projet », Adnène Gallas, membre du groupe de travail, ministère des Finances ; IACE, 29 avril 2014. 12 pages, français, diaporama, texte lisible. Pas de scan.
- P. 2-3 : projet pilote lancé par le ministère des Finances en 2011 ; arrêté du ministre des Finances du 22 novembre 2011 instaurant un processus participatif. Formalités recensées : DGI 159, DGD 254, DGCPR 33 (total 446).
- P. 4 : bilan par administration, % (nombre) : à conserver DGI 26 (42), DGCPR 33 (11), DGD 7 (17), total 16 (70) ; à supprimer 8 (12), 3 (1), 7 (17), total 7 (30) ; à simplifier 66 (105), 64 (21), 86 (220), total 77 (346) ; total 100 (159), (33), (254), (446).
- Pp. 5-6 : formalités fiscales : 126 simplifications ; axes (nombre / %) : réduction de délai 71 / 56 ; réduction de pièces 84 / 67 ; prorogation de la validité 11 / 9 ; décentralisation 4 / 3 ; fusion 6 / 5 ; dématérialisation 30 / 23 ; scission 1 / 1. Formalités douanières : 220 simplifications : réduction de délai 85 / 39 ; pièces 109 / 49 ; prorogation 39 / 18 ; décentralisation 60 / 27 ; dématérialisation 126 / 57 ; cahier des charges 21 / 9 ; fusion 12 / 5 ; scission 2 / 1.
- Pp. 7-10 : approche (suppression des pièces, délais, cahiers des charges, validité, décentralisation (plus de 60 % des formalités douanières, soit 153, délivrées au niveau de la direction générale), dématérialisation, formulaires : 204 modèles pour 446 formalités dont 15 informatisés). Pas de forfaitaire, IRPP, IS ni TVA chiffrés.

#### 2014_registre_electronique.pdf

- Titre : « Projet de simplification des formalités fiscales et douanières » (suite : registre électronique), Tunis, 29 avril 2014. 10 pages, français, diaporama, texte lisible. Pas de scan. Auteur non indiqué.
- Contenu : rapport validé par un conseil interministériel le 17 juin 2013 (calendrier, publication de la liste, recours) ; registre électronique central des formalités mis en ligne, en vigueur par décision du ministre des Finances du 21 octobre 2013 (5 articles) : publication sur les sites du ministère, de la DGI et de la douane (art. 2) ; centre informatique chargé de la gestion en ligne (art. 3) ; opposabilité du registre, recours examiné et tranché sous 24 heures (art. 4) ; rapports et statistiques au comité de pilotage (art. 5). Aucun chiffre fiscal.

#### 2014_seminaire_mef_ifc_point_situation.pdf

- Titre : « Projet de simplification des formalités fiscales et douanières — Point de la situation », Tunis, 29 avril 2014 (pieds de page datés 12/05/2014) ; séminaire MEF / IFC d'après le nom du fichier (l'IFC n'est pas nommé dans le texte extrait). 54 pages, français, diaporama de tableaux, texte lisible. Pas de scan.
- Structure : formalités douanières simplifiées (pp. 3-16) ; cellule de veille et d'écoute (p. 17) ; principes de simplification (pp. 18-22) ; formalités fiscales simplifiées DGI (pp. 22-36, tableaux avec identifiant F/xxx, simplification, concrétisation) ; calendrier de réalisation DGI (pp. 37-44) ; formalités DGCPR simplifiées (p. 45) ; calendrier DGCPR (pp. 52-53). Aucun chiffre de recettes ou de contribuables.
- Mentions fiscales utiles :
  - P. 23 : suppression du certificat d'imposition selon le régime réel (F/AVF/007) par l'article 88 de la loi de finances 2014 (retenue à la source ramenée de 15 % à 5 % ; mention « soumis au régime réel » portée sur la carte d'identification fiscale 2014) ; suppression de la tenue du registre des prestations aux étrangers non résidents des cliniques (art. 89 LF 2014) ; suppression du livre spécial achats-ventes des détaillants soumis à la TVA, qui tiennent un registre simplifié s'ils ne sont pas tenus à une comptabilité conforme au système comptable des entreprises (art. 89 LF 2014) ; suppression de la déclaration de l'avance sur la taxe de formation professionnelle (TFP).
  - P. 32 : suppression de pièces dans la déclaration de l'impôt forfaitaire (F/DEC/002, certificats de retenue à la source ; note de service n° 9031 du 18/12/2013) ; déclaration IS (F/DEC/006), acompte provisionnel (F/DEC/008), IRPP (F/DEC/009), avance des sociétés de personnes (F/DEC/013, LF 2014).
  - P. 33 : livre spécial des personnes assujetties à la TVA ne tenant pas de comptabilité (F/RLC/007) ; attestation de non-imposition à l'IR et à l'IS (F/SIT/003).
  - P. 38-40 (calendrier DGI) : suppression des déclarations semestrielle et trimestrielle des impôts (F/DEC/003, 004) dans le cadre de la réforme fiscale ; suppression de six pièces annexées à la déclaration d'IS (LF 2015) ; révision de l'article 57 du code de l'IRPP et de l'IS (déduction de 20 % des revenus et bénéfices, attestation du centre de gestion intégré), LF 2015 ; déclaration de l'impôt forfaitaire dû par les salariés étrangers (F/DEC/010, projet de dématérialisation).
  - Pp. 42-43 : restitution du crédit de TVA (F/RES/001 à 005) : réduction des délais, décentralisation, suppression du contrôle fiscal préalable.
  - Rien sur le minimum d'impôt, le nombre de forfaitaires ou le contrôle chiffré.
