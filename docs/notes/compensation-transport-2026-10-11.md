# Note documentaire — la compensation du transport public (11 octobre 2026)

Matière pour un chapitre nouveau `precis/fr/compensation/_transport.qmd`. Le poste budgétaire
« transport » lui-même (111,0 MD en 2003, 660,0 MD en 2024) est acquis dans `_depense.qmd` et
`docs/notes/compensation.md` (§ 2.1 et § 10) : il n'est pas refait ici. Cette note dit **ce que le
poste paie, à qui, à quels tarifs, pour quels voyageurs**.

**Niveaux de preuve** employés ci-dessous, en clair : « lu à l'image » (page rendue et lue) ;
« couche texte » (extraction `pdftotext`, non relue à l'image) ; « couche texte décodée » (éditions
du JORT de 1999 à 2005 dont la couche texte est décalée de 29 : accents perdus) ; « OCR »
(tesseract, non relu à l'image) ; « intitulé seul » (notice de `jort_cache.db`). Les tableaux en
arabe (budgets, rapports du ministère des Finances) sont lus en couche texte après normalisation
NFKC ; l'ordre des colonnes a été vérifié à l'image **une fois par édition citée comme telle**.
Pages : « p. PDF » = rang de la page dans le fichier ; « p. imprimée » = numéro porté par la page ;
pour le Rapport sur les entreprises publiques (LF 2020, LF 2021), les pages citées sans précision
sont des numéros imprimés. Pour le *Journal officiel*, toujours la pagination imprimée de
l'édition française.

**Trois familles de chiffres, jamais sur le même plan** : (A) budgétaire et ministère des
Finances ; (B) contrôle public (Cour des comptes) ; (C) rapport extérieur (Banque mondiale). Aucune
évaluation économique de l'incidence du poste n'a été trouvée (§ 1.6).

---

## 1. Ce qui est établi, série par série

### 1.1 Ce que la subvention paie, et à qui

**Constat central.** Le poste « transport » de la dépense de compensation n'est pas un fonds : c'est
la somme de **subventions par société** inscrites aux dépenses d'intervention du ministère du
Transport, sous le libellé « دعم النقل العمومي » (soutien du transport public), articles 170 à 178
du budget. La somme des lignes par société égale, au dixième de million, le poste « transport » de
`_depense.qmd` pour chacune des six années lues (277,5 ; 330 ; 385 ; 416 ; 433 ; 450).

**Ce que la ligne rémunère, dans les mots du ministère des Finances.** Rapport sur les finances
publiques 2010 (`2010_rapport_finances_publiques.pdf`, arabe, p. PDF 34, couche texte, § « ت - دعم النقل ») :
le soutien du transport public augmente d'environ 20 MD « نظرا لتطور عدد المنتفعين بعنوان النقل
المدرسي و الجامعي و النقل بتعريفات منخفضة و كذلك النقل المجاني لبعض الفئات الخصوصية » — en raison
du nombre de bénéficiaires du transport scolaire et universitaire, du transport à tarifs réduits et
du transport gratuit de certaines catégories. Budget 2013 du ministère du Transport (p. PDF 6,
couche texte) : crédit de 330 MD « مقابل 277,5 م.د في سنة 2012 », la hausse de 52,5 MD étant
affectée « خاصة بالنقل المدرسي والجامعي ». La société de transport de Tunis l'inscrit dans ses
comptes sous le nom de « compensation scolaire » (tableau 1.1 c).

#### a) Tableau A1 — crédits de la loi de finances par société, 2012-2017 (famille A, budgétaire)

Source : ministère des Finances, « ميزانية وزارة النقل » (budget du ministère du Transport),
éditions 2013 à 2017, tableau « أبرز مؤشرات نشاط الوزارة » (principaux indicateurs), ligne « دعم
النقل العمومي (بحساب 1000 د) » ; chaque édition donne l'année N-1 (« ق.م », loi de finances) et
l'année N (« تقديرات », prévisions). Fichiers : `tunisia-data/data/raw/minfinances/portail_ancien/
budgets_ministeres/` — `2013_budget_ministre_transport_jd59.pdf` (p. PDF 10),
`2014_budget_transport_jd635.pdf` (p. 19), `2015_budget_transport_ar_jd814.pdf` (p. 18, imprimée 14),
`2016_budget_transport_ar_jd1018.pdf` (p. 18), `2017_budget_transport_ar_jd1192.pdf` (p. 17,
imprimée 14). **Lu à l'image : éditions 2015 et 2017 ; couche texte : 2013, 2014, 2016.**
Montants en millions de dinars courants. **Ce sont des crédits votés ou proposés, pas des dépenses
constatées.**

| Société | 2012 (LF) | 2013 (prév.) | 2014 (LF) | 2014 (LFC) | 2015 (prév.) | 2016 (prév.) | 2017 (prév.) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sociétés régionales de transport | 155,0 | 190,0 | 220,130 | 217,130 | 228,795 | 244,0 | 255,0 |
| Société des transports de Tunis — autobus | 63,0 | 70,0 | 83,018 | 83,018 | 90,0 | 94,0 | 96,0 |
| Société des transports de Tunis — métro | 23,0 | 25,0 | 29,157 | 29,157 | 30,0 | 32,0 | 34,0 |
| SNCFT | 32,0 | 38,0 | 43,795 | 41,795 | 49,705 | 50,5 | 50,0 |
| Société nouvelle de transport de Kerkennah (bac) | 4,0 | 6,5 | 8,0 | 8,0 | 9,0 | 9,5 | 10,0 |
| Tunisair Express (aérien) | — | — | — | 5,0 | 5,0 | 2,0 | 3,0 |
| SNTRI (interurbain) | — | — | — | — | 2,0 | — | 1,0 |
| Transport scolaire rural | 0,5 | 0,5 | 0,9 | 0,9 | 1,5 | 1,0 | 1,0 |
| **Total « دعم النقل العمومي »** | **277,5** | **330,0** | **385,0** | **385,0** | **416,0** | **433,0** | **450,0** |
| Poste « transport » de `_depense.qmd` | 277,5 | 330,0 | 384,0 | — | 415,9 | 433,0 | 448,2 |

Lecture : (i) les sociétés régionales reçoivent 55 à 58 % du poste (55,0 % en 2015, 57,6 % en
2013), la société de Tunis 29 à 31 %, la SNCFT 11 à 12 % (calcul du précis sur le tableau). (ii) **Le périmètre déborde le transport
terrestre** : bac de Kerkennah depuis 2012 au moins, Tunisair Express à partir de la loi de
finances complémentaire pour 2014. (iii) **Deux lectures de 2014** : l'édition 2014 donne 43,795
(SNCFT) et 220,130 (régionales) ; l'édition 2015, dont la colonne est intitulée « ق م تكميلي
2014 » (LFC 2014, lu à l'image), donne 41,795 et 217,130 : les 5 MD d'écart sont la ligne Tunisair
Express, créée par redéploiement. Les deux sont à garder, étiquetées. (iv) La dernière ligne du
tableau rappelle l'exécuté déjà publié : elle n'est pas de la même nature que les autres.

#### b) Tableau A2 — transferts « interventions » par société, 2016-2024 (famille A, ministère des Finances)

Source : ministère des Finances, « Rapport sur les transferts et les garanties au profit des
entreprises publiques et des établissements publics non administratifs » (annexe n° 8 du projet de
loi de finances), éditions LF 2020 (français), LF 2022, LF 2024 et LF 2025 (arabe). Fichiers :
`tunisia-data/data/raw/caisses/minfin/annexe8_transferts_LF20{20,22,24,25}.pdf`. Chaque édition
porte, par année, un tableau « التحويلات بعنوان سنة N » à cinq colonnes — total, investissements,
**interventions** (« التدخلات »), fonctionnement, rémunérations. Seule la colonne « interventions »
est reprise ici. **Lu à l'image : édition LF 2025, tableau de 2023 (p. 97 imprimée et PDF) ;
couche texte pour le reste.** État : « إنجازات » (réalisations) sauf mention. Millions de dinars.

| Société | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 (LF) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Sociétés régionales de transport | 241,955 | 258,755 | 255,0 | 255,0 | 325,0 | 288,5 | 361,0 | 393,0 | 400,0 |
| Société des transports de Tunis | 126,543 | 276,007 ? | 162,007 | 131,407 | 155,2 | 135,0 | 140,0 | 141,0 | 153,0 |
| SNCFT | 65,5 | 219,624 | 91,0 | 72,065 | 110,958 | 71,926 | 86,639 | 82,494 | 83,0 |
| Société nouvelle de transport de Kerkennah | 9,5 | 10,0 | 10,0 | 10,0 | 12,5 | 14,0 | 16,0 | 17,0 | 18,0 |
| Tunisair Express | 2,0 | 3,0 | 3,0 | 3,0 | 10,0 | 10,0 | 10,0 | 10,0 | 10,0 |
| SNTRI | 3,0 | 32,7 | 1,0 | 1,0 | 7,5 | 2,5 | 5,0 | 3,0 | 3,0 |
| Société du réseau ferroviaire rapide de Tunis | 12,0 | 20,0 | 27,762 (colonne indéterminée) | 29,0 | 37,9 | 38,875 | 42,757 | 49,913 | 60,0 |
| **Interventions du ministère du Transport** | 461,587 | 820,422 | 550,395 | 501,472 | 659,058 | 560,801 | 661,396 | 696,407 | 727,0 |
| *Poste « transport » de `_depense.qmd`, pour mémoire* | 433,0 | 448,2 | 450,0 | 450 | 600 | 504,0 | 600,0 | 640,0 | 660,0 |
| Édition lue | LF 2020 | LF 2020 | LF 2022 | LF 2022 | LF 2024 | LF 2025 | LF 2025 | LF 2025 | LF 2025 |

Réserves, à porter au rédacteur :

0. **Rapprochement établi pour 2016, à 0,5 MD près.** Interventions du ministère, 461,587 ; moins
   la société du réseau ferroviaire rapide (12,0), l'Institut national de la météorologie (1,089,
   même tableau) et la subvention d'entretien du réseau ferré de la SNCFT (« autour de 15 MD »,
   Rapport sur les entreprises publiques) : 433,5, pour un poste « transport » de 433,0. Par
   société : SNCFT 65,5 = 50,5 (budget) + 15 ; société de Tunis 126,543 pour 94 + 32 = 126 ; bac
   de Kerkennah 9,5 = 9,5 ; Tunisair Express 2,0 = 2,0 ; régionales 241,955 pour 244,0 au budget ;
   SNTRI 3,0 pour une ligne vide au budget. **Le même calcul n'est pas fait pour 2018-2024**, faute
   de connaître la subvention d'entretien de ces années : ôter la seule société du réseau rapide
   laisse un résidu d'environ 21 MD en 2020 et 6,5 MD en 2023. Pour 2018, la ligne de cette société
   ne porte que deux nombres identiques (27 762) : on ne peut dire, sur la couche texte, si c'est
   une intervention ou un investissement.
1. **« Interventions » n'est pas « compensation ».** La colonne dépasse le poste « transport » de
   28 à 372 MD selon l'année. Ce qui est établi : en 2016, la SNCFT reçoit 65,5 MD d'interventions
   quand le budget ne lui affecte que 50,5 MD au titre du soutien du transport ; le rapport sur les
   entreprises publiques (LF 2020, p. imprimée 75) nomme l'autre versement — une subvention de
   l'État pour l'entretien du réseau ferré, « autour de 15 MD ». La colonne compte aussi la société
   du réseau ferroviaire rapide de Tunis (12 à 60 MD), absente de la ligne « دعم النقل العمومي »
   des budgets 2013-2017. **Le reste de l'écart n'est pas rapproché ici** (2020 : 659,1 contre 600 ;
   2023 : 696,4 contre 640,0).
2. **2017 n'est pas une année de compensation ordinaire.** Les interventions passent de 461,6 à
   820,4 MD : le rapport sur les entreprises publiques (LF 2020, p. 72-73) explique que l'État a
   pris en charge les dettes de la société de Tunis envers la Société nationale de distribution des
   pétroles (145,3 MD au 30 juin 2017) ; le rapport sur les transferts (LF 2020, p. PDF 30) cite la SNCFT
   (284,9 MD de transferts contre 110,8) et la SNTRI (32,7 contre 3,0). C'est un apurement, hors du
   poste « transport » (448,2 MD) : voir § 7.
3. **L'édition française LF 2020 a des chiffres inversés dans sa couche texte** (« 955 253 » pour
   253 955 ; « 007 276 » pour la société de Tunis en 2017, lu ici 276,007 sous toute réserve — le
   total de ligne imprimé est 287 764 et les investissements 11 757, ce qui confirme 276,007). **Les
   colonnes 2016 et 2017 sont à relire à l'image avant citation.**
4. La colonne 2023 de l'édition LF 2024 est « ق م 2023 » (SNCFT 83,0 ; Tunis 141,0 ; régionales
   393,0) ; celle de l'édition LF 2025 est « إنجازات 2023 » : les régionales et Tunis y sont au
   millier près les montants votés.
5. 2021 dans l'édition LF 2022 est la loi de finances (régionales 288,5 ; SNCFT 69,0 ; Tunis 135,0 ;
   réseau rapide 37,0 ; total 556,0), non reprise au tableau.

#### c) Tableau A3 — la subvention vue des comptes des sociétés (familles A et C, à ne pas fondre)

| Société, année | Grandeur | Montant | Source |
|---|---|---:|---|
| Tunis, 2013 | « Compensation scolaire » (produit d'exploitation) | 95,000 MD | Banque mondiale, *Livre blanc*, 2016, annexe, p. PDF 73 (et p. PDF 32), citant le rapport annuel 2014 de la société (famille C) |
| Tunis, 2014 | idem | 112,175 MD | idem |
| Tunis, 2016 | subventions d'exploitation de l'État | 126 MD | Rapport sur les entreprises publiques, LF 2020, p. 72 (famille A) |
| Tunis, 2017 | idem | 140,6 MD, dont 130 de subvention d'exploitation et 10,6 de dette envers AGIL prise en charge | idem |
| Tunis, 2018 (prév.) | idem | 130 MD | idem |
| SNCFT, 2016 | « indemnité de transport attribuée par l'État » | 44,6 MD | idem, p. imprimée 75 |
| SNCFT, 2017 | idem | 42,5 MD | idem |
| SNCFT, 2016-2017 | subvention d'entretien du réseau | « autour de 15 MD » | idem |

**Recoupement établi** : 95,000 = 70,0 + 25,0 (budget 2013, autobus + métro) ; 112,175 = 83,018 +
29,157 (budget 2014) ; 130 = 96 + 34 (budget 2017) ; 126 = 94 + 32 (budget 2016). La ligne
budgétaire de la société de Tunis et sa « compensation scolaire » sont donc la même grandeur.
**Recoupement qui échoue** : SNCFT 2016, 44,6 MD dans le rapport contre 50,5 au budget ; 2017, 42,5
contre 50,0. Écart à signaler, non à expliquer.

#### d) Tableau B1 — ce que la compensation ne couvre pas (famille B, Cour des comptes)

- **2006** — Cour des comptes, rapport « إشراف الدولة على قطاع النقل البري » (contrôle de l'État
  sur le transport terrestre ; vingt-troisième rapport annuel selon le renvoi du rapport de 2016 ;
  mis en ligne le 15 juin 2008 ; `Rapport_81_2018-08-15-12-51-01.pdf`, **p. imprimée 99, lue à
  l'image**) : « الدولة تقوم فقط بتعويض جزئي للنقص في مداخيل المنشآت العمومية للنقل البري » —
  l'État ne compense que partiellement le manque à gagner ; pour 2006, « قدّر العجز المالي بدون
  اعتبار الشركة الوطنية للنقل بين المدن بحوالي 228,4 م.د مقابل منح تعويض بلغت 145 م.د » — déficit
  financier estimé à environ **228,4 MD**, hors SNTRI, **en regard de 145 MD de subventions de
  compensation** (le poste « transport » de 2006 est de 146 MD). **Le rapport ne dit pas si ces
  228,4 MD s'entendent avant ou après subvention** : ne pas en tirer un taux. Causes citées : le
  transport gratuit et le transport scolaire, les réductions aux élèves et étudiants atteignant
  **90 % du tarif normal** (note : procès-verbal de la séance de travail ministérielle du 28 juillet
  2006). Même page : sauf pour la SNCFT, les montants de la compensation « لا يستند إلى معايير
  واضحة » (ne reposent pas sur des critères clairs) et aucune règle ne les fixe.
  **Réponse du ministère du Transport, imprimée en italique dans le même rapport (p. imprimée 113,
  lue à l'image)** — à citer comme telle, non comme un constat de la Cour : la compensation du
  transport scolaire et universitaire est calculée « اعتمادا على معدل تعريفة الاشتراك السنوي »
  (sur la base du tarif moyen de l'abonnement annuel) ; celle du transport gratuit est fixée
  « بطريقة جزافية » (au forfait) ; les compensations accordées ne suffisent pas à couvrir le manque
  à gagner ; un projet de décret sur la méthode de calcul a été transmis aux parties concernées.
- **2012-2013** — Cour des comptes, rapport « وزارة النقل » (mis en ligne le 15 juin 2016 ;
  `Rapport_81_2018-08-16-10-44-17.pdf`, p. imprimées 281-282, **lu à l'image**) : le ministère évalue
  à **près de 400 MD par an** le manque à gagner des entreprises de transport terrestre dû aux
  tarifs réduits des élèves et étudiants, les subventions versées à ce titre étant de **273 MD en
  2012 et 323 MD en 2013** ; résultats négatifs cumulés de 1 200 MD sur 2010-2013 ; prise en charge
  en 2011 par le budget de dettes de la société de Tunis envers la Société nationale de distribution
  des pétroles et la CNRPS pour 244 MD.

Le rapport de 2016 donne la seule mesure trouvée d'un **taux de compensation** : 273 / 400 = 68 %
et 323 / 400 = 81 % du manque à gagner scolaire en 2012 et 2013 (calcul du précis sur une
estimation du ministère, « près de 400 MD », donnée sans année).

#### e) Avant 2012

- 2003-2011 : seul le total du poste est lu (rapports sur les finances publiques, déjà au
  chapitre). Le rapport 2010 porte une ligne « وزارة النقل (التعويض) » par exercice (164,4 ; 182,2 ;
  200,0 ; 220,0 — couche texte) qui redonne le poste, sans détail par société.
- **À partir de 1984** : la subvention passe par un fonds spécial du Trésor, la caisse de
  compensation et de soutien des transports routiers (§ 2). Lu : son crédit de 1984 (5 600 000 D,
  tableau F de la loi de finances, déjà au chapitre). **La date à laquelle ce fonds cesse de porter
  la subvention n'est pas établie** : les tableaux des lois de finances de 1985 à 2002 ne sont pas
  dépouillés ; ce qui est lu, c'est qu'en 2007 la dépense figure au budget du ministère sous la
  ligne « وزارة النقل (التعويض) » (rapport sur les finances publiques 2010).
- Aucune décomposition par nature (scolaire, tarifs réduits, gratuités) n'est publiée : la source
  dit seulement que le scolaire domine, et que les gratuités sont compensées au forfait ou pas du tout.

### 1.2 Les tarifs dans le temps

**Constat.** De 1967 à 2000, les tarifs sont fixés par arrêté publié au *Journal officiel* ; le
dernier barème général qui y figure est celui du **6 mai 1998** (arrêté du 27 avril 1998), retouché
le 17 février 2000 pour la seule société de Sfax. Les relèvements suivants n'y sont pas : ils sont
connus par le relevé de prix de l'INS (un relèvement en août 2010, un en juin 2021) et par la
presse. Les sources publiques datent de **2010** le début du gel (Rapport sur les entreprises
publiques, LF 2020, p. 72 : « le gel des tarifs depuis l'année 2010 » ; Cour des comptes 2016,
p. 281, lu à l'image : tarifs non actualisés « منذ سنة 2010 »).

#### a) Tableau T1 — tarifs repères au *Journal officiel*, 1987-2000

Réseaux des sociétés de transport routier et du métro léger de Tunis (hors sociétés de Sfax et du
Sahel, qui ont leur colonne). Ticket en millimes ; abonnements en dinars ; interurbain en millimes
par place-kilomètre, tranche de plus de 10 km jusqu'à 150 km.

| Date d'effet | Texte | JORT (éd. française) | Ticket 1 section | Ticket 2 sections | Abonnement annuel ordinaire, 1 section | Abonnement scolaire, une ligne urbaine (1 ou 2 sections) | Interurbain, place-km | Preuve |
|---|---|---|---:|---:|---:|---:|---:|---|
| 16 févr. 1987 (art. 5) | arrêté du 14 févr. 1987 | n° 13 du 20 févr. 1987, p. 261 | 140 | 210 | 102,000 | non lu | 20 | image |
| 31 août 1989 (calcul) | deux arrêtés du 10 août 1989 | n° 58 du 29 août 1989, p. 1282-1286 | 150 | 240 | 112,500 | 14,800 | 22 | image |
| 12 août 1990 (calcul) | deux arrêtés du 30 juill. 1990 | n° 52 du 10 août 1990, p. 1045-1048 | 170 | 260 | 112 | 14,800 | 24,5 | image |
| 14 juill. 1991 (calcul) | deux arrêtés du 2 juill. 1991 | n° 50 du 12 juill. 1991, p. 1294-1298 | 190 | 290 | 126 | 16,300 | 27,5 | image |
| 3 sept. 1992 (calcul) | deux arrêtés du 24 août 1992 | n° 57 du 1er sept. 1992, p. 1128-1134 | 210 | 320 | non lu | 16,300 | 30,2 | image |
| non calculée | deux arrêtés du 26 août 1993 | n° 67 du 7 sept. 1993, p. 1430-1436 | 230 | 350 | non lu | 17,200 | 33,2 | image |
| 6 mai 1998 (art. 21) | arrêté du 27 avr. 1998 | n° 37 du 8 mai 1998, p. 997-1001 | 260 | 390 | 167 | — | — | image (abonnements, p. 999-1001) ; tickets : couche texte p. 998, recoupée par l'annexe de 2000 lue à l'image |
| 1er août 1998 (art. 13) | arrêté du 29 juill. 1998 (abonnements scolaires) | n° 63 du 7 août 1998, p. 1723-1725 | — | — | — | 19,400 | — | image |
| 8 févr. 1999 (art. 2) | arrêté du 6 févr. 1999 | n° 12 du 9 févr. 1999, p. 229 | — | — | — | — | 37,5 | couche texte |
| 25 févr. 2000 + 5 j. (non calculée) | arrêté du 17 févr. 2000 | n° 16 du 25 févr. 2000, p. 535-536 | 260 | 390 | — | — | — | image |

Dates d'effet : celle de l'article cité quand le texte l'énonce. Sinon, pour les textes antérieurs à
la loi n° 93-64, un jour franc après la publication (publication le 29 août 1989 → 31 août ; le
10 août 1990 → 12 août ; le 12 juillet 1991 → 14 juillet ; le 1er septembre 1992 → 3 septembre).
**L'absence de clause d'effet est vérifiée à l'image pour 1989 (art. 20), pour 1990 (deux
arrêtés, p. 1045 et 1048), pour l'interurbain de 1991 (art. 11) et pour l'interurbain de 1992
(p. 1134) ; pour les arrêtés urbains de 1991 et de 1992, elle n'est constatée qu'en OCR** : à
relire. Un arrêté du 30 septembre 1989 (JORT n° 67, p. 1584-1586, intitulé seul) a modifié
l'arrêté urbain du 10 août 1989 un mois après sa publication ; l'arrêté de 1990 dit remplacer les
annexes de ce texte-là : **le barème de l'automne 1989 n'est pas lu**, et la ligne « 1989 » du
tableau est celle d'août. Pour les arrêtés du
26 août 1993 et du 17 février 2000, postérieurs à la loi n° 93-64, la date est « cinq jours après
le dépôt du fascicule au siège du gouvernorat de Tunis » : la date de dépôt n'est pas connue ici,
la date n'est donc pas calculée.

Autres valeurs lues à l'image dans les mêmes textes, utiles au chapitre :

- **L'écart scolaire, mesuré dans le barème.** En 1998, abonnement annuel ordinaire d'une ligne à
  une section : **167 D** (deux sections : 205 D) ; abonnement scolaire d'une ligne urbaine d'une ou
  deux sections : **19,400 D**. L'élève paie 9 à 12 % du prix ordinaire (calcul du précis) — ce qui
  recoupe les « 90 % » de la Cour des comptes. En 1991 : 126 D (155 D) contre 16,300 D.
- **L'abonnement annuel ordinaire d'une section** : 102 D en 1987, 112,500 D en 1989, 112 D en
  1990, 126 D en 1991, 167 D en 1998 (image).
- **L'abonnement scolaire suit moins vite que le ticket.** 14,800 D en 1989 et 1990, 16,300 D en 1991
  et 1992, 17,200 D en 1993, 19,400 D en 1998 : + 31 % en neuf ans, quand le ticket d'une section
  passe de 150 à 260 millimes (+ 73 %).
- 1998, autres abonnements scolaires (réseau de la société nationale des transports) : zone urbaine
  28,900 D ; ligne suburbaine de 3 sections et plus 41,700 D ; réseau général 53,200 D ; métro, une
  ligne 19,400 D, réseau 37,860 D ; TGM 2e classe 48,100 D.
- 1998, tarif réduit du ticket : 210 millimes (1-2 sections), 320 (3-5 sections) ; carte
  hebdomadaire d'une section 2,350 D ; abonnement mensuel d'une section 16,700 D.
- Arrêté du 17 février 2000 : remplace la seule annexe 1 ; les tarifs de Tunis sont inchangés ; la
  société de Sfax reçoit une 5e section à 790 millimes et une 6e à 1 000.
- Interurbain : chaque arrêté fixe un prix de 0 à 10 km égal à dix fois le prix kilométrique (220,
  245, 275, 302, 332, 375 millimes), un prix au-delà de 150 km (18 ; 20 ; 22,5 ; 25 ; 27,5 ;
  30,9) et un minimum pour la SNTRI. En 1987 : 200 millimes de 0 à 10 km, 20 par place-kilomètre
jusqu'à 150 km, 16 au-delà (image).

**Avant 1987** : arrêtés du 1er août 1977, du 15 août et du 24 novembre 1981, du 10 décembre 1982,
du 20 août 1983, du 10 février et du 28 mars 1986 (intitulés à l'index). OCR partiel et bruité,
non retenu : interurbain 9,5 millimes par place-km en août 1981, 13 en décembre 1982, 16,5 en août
1983 ; ticket d'une section 120 millimes en août 1983 (une lecture « 1120 » à corriger). **À relire
à l'image avant tout usage.**

#### b) Tableau T2 — après le *Journal officiel* : le relevé de prix de l'INS, 2007-2026 (famille A, statistique officielle)

Source : INS, *Bulletin mensuel de la statistique*, tableau « Prix moyen de détail à Tunis »,
rubrique « Transport(s) », 213 numéros de novembre 2008 à juillet 2026
(`tunisia-data/data/raw/ins-bms/bms-AAAA-MM.pdf`) ; chaque numéro donne treize mois et une moyenne
annuelle. **Couche texte, non relu à l'image.** Millimes, sauf l'abonnement en dinars.

| Ligne de l'INS | nov. 2007 – juill. 2010 | août 2010 – mai 2021 | juin 2021 – juill. 2026 |
|---|---:|---:|---:|
| « Parcours autobus », puis « Autobus / métro » (billet) | 450 | 470 | 500 |
| « Billet de train 2ème classe » (ligne présente à partir de la fin de 2010 ; premier mois lisible dans ses colonnes rétrospectives : décembre 2009) | 7 700 de déc. 2009 à juill. 2010 ; rien avant | 8 000 | 8 000 |
| « Abon scolaire (bus) » (ligne présente jusqu'à l'automne 2010 ; dinars) | 23,7 | 24,9 en août et sept. 2010, puis ligne supprimée | absente |

L'INS ne dit ni la durée ni le réseau de son « abonnement scolaire » (l'appel de note qui
l'accompagne marque les lignes exprimées en dinars ; son libellé n'a pas été lu) : **23,7 D ne se
rapproche d'aucune ligne du barème de 1998 et ne doit pas être mis en série avec lui.**
L'INS ne dit pas davantage à quel trajet correspond son billet d'autobus ; **il coïncide avec le ticket de
deux sections** donné par la presse pour la veille du relèvement de 2021 (470 millimes), et s'y
rattache par le *Journal officiel* (390 millimes en 1998-2000). C'est un rapprochement, non une
définition publiée. Les moyennes annuelles imprimées (458 pour 2010, 488 pour 2021) placent bien
les relèvements en août 2010 et en juin 2021.

**Le relèvement du 1er juin 2021** (presse citant l'agence TAP : Webmanagercenter, 30 mai 2021) :
tickets d'autobus de la société de Tunis de 320, 470 et 650 millimes (sections 1 à 3) portés à un
tarif unique de 500 ; de 800, 970 et 1 170 (sections 4 à 6) à 1 dinar ; de 1 350, 1 850 et 2 150
(sections 7 à 10) à 1,5 dinar ; « dernière augmentation en 2010 ». **Famille presse : à
n'employer que pour dater et décrire, non comme barème.** Le ticket d'une section **passe de 320 à
500 millimes (+ 56 %)** quand celui de trois sections **baisse** de 650 à 500 : c'est une
restructuration en trois paliers autant qu'une hausse.

**Abonnements scolaires de la société de Tunis, tels que la presse les rapporte en mars 2018**
(Tuniscope, 6 mars 2018 ; année scolaire non dite) : zone urbaine autobus 36,500 D ; réseau général
autobus 66,250 D ; réseau général métro 47,450 D ; TGM 2e classe 60,050 D. Contre 28,900 ; 53,200 ;
37,860 et 48,100 D au barème de 1998 : + 25 à + 26 % en vingt ans.

#### c) Tableau T3 — en dinars constants (calcul du précis)

Déflateur : indice des prix à la consommation, série longue de l'entrepôt
(`tunisia-data/data/processed/ins-publications/ipc_longue_periode.csv`, **indice base 1970
raccordé**, moyennes annuelles ; dernière année portée : 2023). Valeurs en millimes de 2023.

| Année | Ticket 1 section | Ticket 2 sections | Abonnement scolaire urbain (D de 2023) | Interurbain, place-km |
|---|---:|---:|---:|---:|
| 1987 | 785 | 1 178 | — | 112,2 |
| 1989 | 728 | 1 165 | 71,9 | 106,8 |
| 1990 | 774 | 1 184 | 67,4 | 111,6 |
| 1991 | 803 | 1 226 | 68,9 | 116,2 |
| 1992 | 841 | 1 281 | 65,3 | 120,9 |
| 1993 | 884 | 1 345 | 66,1 | 127,6 |
| 1998 | 812 | 1 217 | 60,6 | 114,0 (1999) |
| 2010 | 680 | 998 | — | — |
| 2021 | 592 | 592 | — | — |
| 2023 | 500 | 500 | — | — |

Le ticket de deux sections vaut en 2023, en pouvoir d'achat, 37 % de ce qu'il valait en 1993 ;
celui d'une section, 57 %. Les valeurs de 2010 emploient 320 et 470 millimes (presse et INS) : à
présenter comme telles.

### 1.3 Qui a droit à quoi

| Catégorie | Règle | Texte | L'État rembourse-t-il le transporteur ? |
|---|---|---|---|
| Élèves, stagiaires de premier niveau et apprentis de 25 ans au plus ; étudiants du 1er cycle (30 ans), du 2e (33 ans), du 3e (35 ans) ; établissements privés agréés (20 h par semaine, 6 mois) | abonnement scolaire, valable l'année scolaire hors dimanches, fériés et vacances ; majoré de 50 % pour ces jours ; abonnement d'été à 50 % ; exclu si activité rémunérée | arrêté du 29 juill. 1998, art. 1er à 5 (lu : couche texte et image) ; mêmes principes dans l'arrêté du 10 août 1989, art. 8 (OCR : élèves de moins de 23 ans) | oui : c'est l'objet principal du poste (§ 1.1) |
| Enfants de moins de 3 ans accompagnés | gratuité | arrêté du 27 avr. 1998, art. 10 (couche texte) | le texte ne le dit pas |
| Titulaire de la carte de handicapé, et l'accompagnant du titulaire de la carte « handicapé prioritaire avec accompagnant » | gratuité | idem, art. 10 ; conditions d'accès : arrêtés des ministres du transport et des affaires sociales du 23 avr. 1982, du 12 juill. 1989 et du 6 mai 1993 (intitulés seuls) | non lu |
| Agents de contrôle du ministère du Transport | gratuité | arrêté du 27 avr. 1998, art. 10 | **non** : la Cour des comptes relève que le ministère n'a pas compensé depuis 1991 la gratuité de ses agents (512 en 2013), contre l'article 12 de la loi n° 2004-33 (rapport de 2016, p. 282, image) |
| Enfants de 3 à 7 ans ; militaires en uniforme, et officiers, sous-officiers et élèves en civil sur carte ; journalistes sur carte professionnelle ; invalides porteurs de la carte de la loi n° 62-34 et du décret-loi n° 72-3 | tarif réduit du ticket | arrêté du 27 avr. 1998, art. 11 ; déjà dans l'arrêté du 10 août 1989, art. 11 (image) | le texte ne le dit pas |
| « Certaines catégories d'usagers », au choix de la société | réduction « pouvant aller jusqu'à 90 % » | arrêté du 27 avr. 1998, art. 12 ; arrêté du 2 juill. 1991 (interurbain, image) | — |
| Agents des douanes en uniforme | gratuité sur les lignes intérieures des sociétés nationales et régionales (zones énumérées) | arrêté des ministres du transport et des finances du 25 juin 1998, art. 1er et 2 (couche texte, lecture partielle) | suite de l'arrêté non lue |
| Agents des forces de sûreté intérieure relevant du ministère de l'intérieur, en exercice effectif | gratuité sur les lignes de la société de Tunis, de la SNCFT (banlieues et grandes lignes), des sociétés régionales et de la SNTRI, sur carte professionnelle | arrêté conjoint du 24 juin 2011, art. 1er à 3 (couche texte) ; remplace un arrêté du 2 janv. 1999 (visé) | **oui, en droit** : art. 4, « sont imputées sur le budget de l'État […] les compensations dues en raison des services rendus par les sociétés de transport » |
| Agents et cadres des corps actifs des ministères de l'intérieur, de la justice, de la défense, des douanes et de la protection civile | gratuité urbaine, régionale et interurbaine sur les lignes intérieures des sociétés nationales et régionales | décret gouvernemental n° 2017-987 du 17 août 2017, art. 1er (**lu à l'image, édition arabe**) | **oui, au forfait** : coût annuel fixé forfaitairement par décisions conjointes du ministre des finances, du ministre du transport et des ministres concernés, réparti par société (art. 2) ; conventions, paiement en quatre tranches égales au début de chaque trimestre (art. 3) ; à la charge du budget du ministère concerné (art. 4) |
| Blessés de la révolution et familles des martyrs | gratuité | loi n° 2012-26 du 24 déc. 2012 (intitulé ; la règle est rapportée par la Cour des comptes) | **non** en 2013 : manque à gagner d'environ 3,3 MD, sans désignation de l'autorité payeuse (Cour des comptes 2016, p. 282, image) |

**La règle générale de remboursement.** Loi n° 2004-33 du 19 avril 2004, article 12 (couche texte
décodée, à relire à l'image pour citer) : l'État et l'autorité régionale organisatrice peuvent
obliger un transporteur public de personnes à accorder la gratuité ou à appliquer des tarifs
réduits en faveur de certaines catégories d'usagers ; « dans ce cas, le manque-à-gagner qui en
résulte pour le transporteur est compensé par l'autorité qui a pris cette mesure. La méthode de
calcul de ce manque-à-gagner est fixée par décret ». Article 11 : les services de transport
collectif public sont financés par les usagers et, le cas échéant, par l'État, les autorités
régionales et les « bénéficiaires » de ces services, ceux-ci étant soumis à un droit sur le
transport collectif public dont l'assiette est fixée par décret.

**Ce décret général n'est pas identifié ici.** La Cour des comptes constate son absence en octobre
2007 (rapport de 2008, p. imprimée 99, image) puis de nouveau « plus de dix ans » après la loi
(rapport de 2016, p. 281, image). Le décret n° 2017-987 ne règle que le cas des corps actifs, et au
forfait. → fiche `r-transport-decret-manque-a-gagner` (§ 5).

Pour la SNCFT, la règle est écrite depuis 2001 : décret n° 2001-2621 du 9 novembre 2001, cahier des
charges (couche texte décodée) — art. 20, l'État peut imposer des tarifs inférieurs aux tarifs
commerciaux, ce qui « ouvre droit à une compensation financière » ; art. 27, l'État verse une
contribution « pour compenser le déficit du transport voyageur urbain », définie par contrat pour
les banlieues, et « les tarifs réduits et gratuits imposés par l'État […] pour les transports
interurbains […] donnent lieu à une compensation calculée sur la base du tarif moyen pondéré » ;
art. 10, les tarifs interurbains sont approuvés par le ministre « dans la limite de trois pour
cent par an », et au-delà une compensation est allouée sur justification.

### 1.4 Volumes

#### a) Société des transports de Tunis — trafic par catégorie, 2007-2014 (famille C)

Source : Banque mondiale, *Livre blanc relatif au secteur des transports et de la logistique*,
rapport n° ACS18045, 18 mai 2016, annexe, p. PDF 72, tableau « Trafic STT (Bus, métro et TGM) »,
source déclarée « TRANSTU 2015 ». **Couche texte, non relu à l'image.** Millions de voyageurs.

| | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Payant non scolaire | 207,0 | 201,6 | 188,1 | 167,9 | 117,6 | 115,7 | 113,1 | 120,3 |
| Scolaire | 191,9 | 184,5 | 174,0 | 156,7 | 127,8 | 114,2 | 95,6 | 89,8 |
| Gratuit | 45,6 | 46,2 | 46,9 | 52,0 | 50,1 | 48,6 | 49,2 | 49,8 |
| Total | 444,5 | 432,3 | 409,0 | 376,6 | 295,5 | 278,5 | 257,9 | 259,9 |
| Part du scolaire | 43 % | 43 % | 43 % | 42 % | 43 % | 41 % | 37 % | 35 % |

En 2014, **54 % des voyageurs de la société de Tunis ne paient pas le tarif ordinaire** (scolaire
35 %, gratuit 19 % ; calcul du précis). Suite, par le Rapport sur les entreprises publiques
(famille A) : 232,5 millions en 2017 (− 4 % ; élèves et étudiants − 9,7 %), 229,4 en 2018 (− 1,3 % ;
élèves et étudiants − 6,1 %), 223 prévus en 2019 dont 122 payants, 59 élèves et étudiants et 42 « au
titre du transport collectif » (LF 2020, p. imprimées 70-71 ; LF 2021, p. imprimées 69-70). **Les deux séries ne se
raccordent pas sans vérifier la définition** (le « gratuit » de l'une, le « transport collectif »
de l'autre).

Page suivante (p. PDF 73) : produits et charges d'exploitation de la société de Tunis, milliers de dinars —
2013 : revenus 64 538, autres revenus 11 038, compensation scolaire 95 000, total des produits
170 576 ; charges 282 141 dont personnel 174 466. 2014 : 66 319 ; 5 738 ; 112 175 ; 184 232 ;
charges 283 661 dont personnel 186 073. **Les « revenus » (recettes du trafic) couvrent 23 % des charges
d'exploitation en 2013 comme en 2014 ; revenus et compensation scolaire ensemble, 57 % et 63 % ;
le total des produits d'exploitation, autres revenus compris, 60 % et 65 %** (calculs du précis).
Rapport sur les entreprises publiques : charges d'exploitation 353,7 MD en 2017 et 367,2 MD en
2018, produits 214,6 et 203,9 MD, subventions comprises.

#### b) SNCFT — voyageurs, 2007-2014 (famille C) et 1995-2012 (famille A)

*Livre blanc*, p. PDF 78 (source déclarée « SYSTRA 2012 & SNCFT 2015 », couche texte), milliers de
voyageurs :

| | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Grandes lignes | 6 139 | 5 999 | 5 880 | 5 867 | 3 990 | 3 900 | 4 490 | 4 363 |
| Banlieues | 32 668 | 33 227 | 32 695 | 34 284 | 28 751 | 31 318 | 31 774 | 33 262 |
| Total | 38 807 | 39 226 | 38 575 | 40 151 | 32 741 | 35 218 | 36 264 | 37 625 |
| dont scolaire | 11 886 | 11 892 | 11 688 | 12 555 | 11 087 | — | 11 116 | 11 467 |
| Part du scolaire | 31 % | 30 % | 30 % | 31 % | 34 % | — | 31 % | 30 % |

INS, *Annuaire statistique de la Tunisie*, chapitre « Transport », tableau du transport ferroviaire
(couche texte) : 27 660 milliers de voyageurs en 1995, 36 819 en 2001 (édition 1995-2001), 39 226
en 2008 (édition 2004-2008 ; même valeur que le *Livre blanc*), 32 741 en 2011. Rapport sur les
entreprises publiques : 40,95 millions en 2016, 40,99 en 2017, 39,98 en 2018 ; recettes voyageurs
51 MD en 2016, 49,2 MD en 2017, baisse imputée au « nombre élevé des groupes voyageant
gratuitement » (LF 2020, p. imprimées 74-75).

#### c) Métro léger et TGM — recettes, dépenses, voyageurs, 1995-2001 (famille A)

INS, *Annuaire statistique* 2001, tableau 11.9 (suite et fin), p. 171, source déclarée : société du
métro léger de Tunis ; **couche texte, édition à colonnes de gauche à droite**. Ensemble métro + TGM.

| | 1995 | 1996 | 1997 | 1998 | 1999 | 2000 | 2001 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Recettes, impôts compris (milliers de D) | 21 474 | 22 576 | 22 566 | 22 811 | 23 035 | 22 530 | 22 834 |
| Dépenses (milliers de D) | 32 084 | 37 255 | 38 068 | 38 257 | 36 451 | 36 105 | 36 275 |
| Voyageurs (millions) | 107,3 | 112,6 | 114,4 | 113 | 115,7 | 119,7 | 121,4 |
| Recettes / dépenses (calcul du précis) | 67 % | 61 % | 59 % | 60 % | 63 % | 62 % | 63 % |

Le même tableau existe dans les vingt-deux éditions (jusqu'à 2019-2023) : **série de 1995 à 2023 à
transcrire** (§ 6). Si les « recettes » comprennent ou non la compensation, le tableau ne le dit pas.

#### d) Abonnements scolaires — nombre, 2012-2017 (famille A) : deux segments, une rupture

Budgets du ministère du Transport, même tableau qu'en 1.1 a), ligne « تطور الإشتراكات المدرسية »
(évolution des abonnements scolaires). Unité non dite par la source (nombre d'abonnements).

| | 2012 (LF) | 2013 (prév.) | 2014 (prév.) | 2014 (LFC) | 2015 (prév.) | 2016 (prév., éd. 2016) | **2016 (LF, éd. 2017)** | **2017 (prév.)** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Sociétés régionales | 290 565 | 366 665 | 348 744 | 348 744 | 338 288 | 342 912 | 326 428 | 333 501 |
| Société des transports de Tunis | 148 947 | 151 921 | 156 702 | 193 700 | 205 276 | 209 347 | **94 865** | **96 200** |
| SNCFT | 14 000 | 16 000 | 23 500 | 13 000 | 13 000 | 13 390 | 11 739 | 11 978 |
| Total | 453 512 | 534 586 | 528 946 | 555 444 | 556 564 | 565 649 | **433 032** | **441 679** |

**L'année 2016 a deux valeurs, 565 649 et 433 032**, selon l'édition ; la société de Tunis tombe de
209 347 à 94 865. C'est un changement de mesure (prévision remplacée par un constat, ou autre
définition) que la source n'explique pas : **deux segments, jamais chaînés**. La colonne 2014 a de
même deux lectures. Lu à l'image : éditions 2015 et 2017.

#### e) Sociétés régionales

Aucune série de voyageurs ni de recettes n'est établie ici pour les sociétés régionales, **qui
reçoivent pourtant plus de la moitié du poste**. Les *Annuaires statistiques* de l'INS (couche
texte de dix éditions sondées) ne portent, pour la route, que les immatriculations d'autocars :
pas de trafic par société. Pistes : § 5.

### 1.5 Mise en place et ruptures institutionnelles — voir § 2

### 1.6 Incidence

**Aucune étude d'incidence propre à la subvention du transport n'a été trouvée.**

- Jouini, Lustig, Moummi et Shimeles (CEQ, document de travail n° 38, 2017 ; déjà cité au chapitre
  `_incidence.qmd`) : les subventions y sont **un seul agrégat** — produits de base, énergie et
  transport. Méthode pour les subventions (p. PDF 17, couche texte) : « calculated based on
  information reported on food and non-food consumption », montant « adjusted downward to match
  their ratio to disposable income in administrative accounts and the household survey » ; enquête
  sur le budget des ménages de 2010. Seul chiffre propre au transport : 0,3 % du PIB en 2010 sur
  2,4 % (p. PDF 12 ; base du PIB non dite par la source). Aucune répartition du transport par décile.
- Banque mondiale, *Livre blanc* (2016) : diagnostic sectoriel et financier, **sans incidence par
  niveau de vie** ; recommande « la compensation intégrale, pour les opérateurs, du manque-à-gagner
  induit par la gratuité ou certaines réductions » et envisage « un régime de subvention bien
  ciblé » (p. PDF 19, 29 et 44 pour la première formule ; p. PDF 45 pour la seconde ; couche texte).
- Les trois autres études du chapitre `_incidence.qmd`, vérifiées sur leur couche texte :
  Banque mondiale 2013 (`bm-2013-82712`, énergie) ne traite le transport que comme usage du
  gasoil et, dans une note de tableau, comme composante d'un total « subventions énergétiques
  (explicites), produits de base, et transport » ; Banque mondiale 2015 (`bm-2015-wps7312`) le
  nomme une fois, parmi les subventions universelles ; INS-CRES-BAD 2013
  (`ins-cres-bad-2013-subventions`) porte sur l'alimentaire. **Aucune ne répartit la subvention du
  transport par niveau de vie.** Banque mondiale 1993 et rapports du FMI rangés : non dépouillés
  sur ce point.

Ce que le chapitre peut dire sans étude : **la subvention suit les élèves et les étudiants
abonnés, non le niveau de vie** ; son ciblage est celui de la scolarisation et de la géographie des
réseaux. Toute phrase sur la progressivité serait une inférence, à ne pas écrire.

---

## 2. Ruptures proposées, dans l'ordre des dates

| Date | Texte | Ce que le texte change pour qui paie et qui reçoit | Dans ses mots | Portée | Preuve |
|---|---|---|---|---|---|
| 23 févr. 1948 ; refonte le 28 févr. 1957 ; modifié jusqu'au décret n° 65-303 du 15 juin 1965 | arrêtés « portant refonte des taxes de compensation sur les transports automobiles » | taxes sur les transporteurs routiers | — | mise en place | intitulés seuls (déjà dans `compensation-avant-1970-et-plans.md`) |
| 1er janv. 1963 | loi n° 63-13 du 27 mai 1963, JORT n° 26, p. 740-741 | **les transporteurs paient pour les transporteurs** : caisse alimentée par la surtaxe de 1950, la taxe sur les taxis de 1957 et une redevance par tonne autorisée ; elle secourt d'anciens titulaires de licences et subventionne des sociétés | « Caisse Spéciale de Compensation des Transports Routiers » | mise en place — fonds de restructuration, pas un mécanisme de prix | OCR (note antérieure) |
| 1er janv. 1978 | loi n° 77-81 du 31 déc. 1977 (LF 1978), art. 37 et 38, JORT n° 86, p. 3603 | la caisse finance aussi les centres de visite technique et reçoit le droit de visite | « couvrir totalement ou partiellement les dépenses nécessaires à la création et au fonctionnement des centres de visites techniques » | ajustement | OCR |
| 1er janv. 1982 | loi n° 81-100 du 31 déc. 1981 (LF 1982), art. 110, JORT n° 84, p. 3048 | disposition sur la « caisse spéciale des transports routiers » | — | — | intitulé seul |
| **1er janv. 1984** | loi n° 83-113 du 30 déc. 1983 (LF 1984), art. 99 à 103, JORT n° 86, p. 3385-3386 ; art. 38 à 47 (taxe), p. 3378-3379 | **rupture : un fonds paie le tarif préférentiel, et ce sont les véhicules de transport qui l'alimentent.** Fonds spécial du Trésor, ordonnateur le ministre des transports ; il subventionne l'exploitation des entreprises de transport public routier de personnes à participation publique supérieure à 40 % ; **ressources (art. 101) : le droit de visite technique, « 40 % du produit de la taxe unique de compensation de transports routiers instituée par l'article 38 de la présente loi », les remboursements des prêts de la caisse, les autres recettes que les textes lui attribuent** ; la caisse de 1963 est supprimée et son solde versé au fonds (art. 103). La taxe (art. 38 et 39) frappe chaque mois les véhicules de transport en commun de plus de neuf places (4 D par place assise offerte, réduit de 60 % pour le transport touristique et urbain), les louages (1, 5 ou 10 D par place selon la zone), les taxis (5 D dans les gouvernorats de Tunis, de l'Ariana et de Ben Arous, 3 D ailleurs ; 20 et 50 D pour le « grand tourisme ») et le transport de marchandises (6 D par tonne de charge utile pour compte d'autrui, 9 D pour compte propre) | art. 100 : « accorder des subventions d'exploitation aux entreprises de transport public routier de personnes […]. Ces subventions sont destinées à couvrir les moins-values de recettes résultant de l'application d'un tarif préférentiel accordé par voie législative ou réglementaire à certains usagers » ; art. 99 : « consolider et […] promouvoir le secteur des transports routiers » | **rupture** — et non une prise en charge par le budget général : en 1984 la subvention est financée par une taxe affectée | **image** (p. 3378 et 3386) ; OCR pour l'art. 99 (p. 3385). **Ceci répond au TODO de `_reformes.qmd`, l. 48** (taux, assiette, affectation) ; les articles 40 à 47 (réductions, paiement, sanctions) sont lus sur la même image, non repris |
| 21 mars 1984 ; LF 1985, art. 26 ; LF 1988 à 1995 | loi n° 84-2 (réduction du taux de la taxe unique) et modificatifs | taux et modalités de paiement de la taxe | — | ajustements | intitulés seuls — relève du volume « Fiscalité » |
| 4 août 1985 | loi n° 85-77, JORT n° 58 du 9 août 1985, p. 1000-1001 | principe tarifaire : le tarif doit rémunérer le coût ; la politique tarifaire appartient au ministre | art. 7 : les tarifs « peuvent permettre une juste rémunération du transporteur assurant la couverture des coûts réels du service rendu » ; art. 10 : « la politique tarifaire est définie par le ministre » de manière à obtenir « l'utilisation optimale, sur le plan économique et social, du système de transports terrestres » | étape | OCR |
| 16 févr. 1987 → 6 mai 1998 | arrêtés tarifaires (§ 1.2) | relèvements presque annuels de 1989 à 1993, puis un seul en 1998 | — | étapes | image |
| 9 nov. 2001 | décret n° 2001-2621, JORT n° 92 du 16 nov. 2001, p. 3951-3954 | la SNCFT a un **droit écrit à compensation** : contribution pour obligation de service public, compensation du déficit des banlieues par contrat, des tarifs réduits et gratuits des grandes lignes « sur la base du tarif moyen pondéré » | art. 19 : la contribution est telle que recettes et contribution couvrent « la totalité des charges qui seraient imputables au service concerné dans le contexte d'une gestion efficace » | étape | couche texte décodée |
| 28 avr. 2003 | loi n° 2003-33, JORT n° 34, p. 1290 | fusion de la société nationale des transports et de la société du métro léger de Tunis | — | étape institutionnelle | intitulé seul |
| **19 avr. 2004** | loi n° 2004-33, JORT n° 32 du 20 avr. 2004, p. 996-1003 ; modifiée par la loi n° 2006-55 | **rupture de principe : qui décide la gratuité la paie** (art. 12) ; l'État fixe les tarifs et les règles de financement (art. 6) ; financement par les usagers, l'État, les régions et les bénéficiaires indirects (art. 11) | art. 12, cité au § 1.3 | **rupture — restée sans décret d'application général** | couche texte décodée |
| août 2010 | relèvement des tarifs, hors *Journal officiel* | ticket (INS) de 450 à 470 millimes ; train de 7 700 à 8 000 | — | dernier relèvement avant onze ans de gel | INS, couche texte |
| 24 juin 2011 | arrêté conjoint (forces de sûreté intérieure), JORT n° 47 du 28 juin 2011, p. 1100-1101 | gratuité étendue à tous les réseaux publics ; compensation à la charge du budget | art. 4, cité au § 1.3 | ajustement | couche texte |
| 17 août 2017 | décret gouvernemental n° 2017-987, JORT (éd. arabe) n° 70-71 des 1er-5 sept. 2017, p. 2970-2971 | premier texte d'application de l'article 12 : coût de la gratuité des corps actifs fixé **au forfait**, payé par le budget de chaque ministère en quatre tranches | « تضبط الكلفة السنوية لمجانية النقل جزافيا » | étape | image (arabe) |
| 1er juin 2021 | relèvement et tarif en trois paliers, hors *Journal officiel* | ticket d'une section de 320 à 500 millimes ; fin du gel de 2010 | — | étape | presse (TAP) ; INS |

---

## 3. Références candidates

Clés vérifiées le 11 octobre 2026 dans `precis/fr/compensation/references.json` : **existent**
`lf-1984`, `minfin-finances-publiques-2005`, `-2008`, `-2010`, `-2011`, `bm-2013-82712`,
`bm-2015-wps7312`, `ins-cres-bad-2013-subventions`, `jouini-lustig-moummi-shimeles-2017-ceq38`,
`ins-annuaire-statistique-prix-detail` ; `ins-bms` existe dans `precis/fr/references.json` et
`ins-annuaire` dans les livres « Fiscalité » et « Prestations sociales ». **Toutes les autres
entrées ci-dessous sont à créer.** URL vérifiées le
11 octobre 2026 (code 200, `application/pdf`, certificat de pist.tn ignoré) ; **le contenu français
de chaque fichier servi n'a été ouvert que pour les fascicules lus ici depuis le corpus local**.
**Pages de l'édition arabe : non relevées, sauf pour le décret n° 2017-987 — le ticket les
demande, ce point reste ouvert.**

**Journal officiel** (`https://www.pist.tn/jort/<année>/<année>F/<fichier>`)

| Clé suggérée | Texte | JORT, pages (FR) | Fichier |
|---|---|---|---|
| `loi-63-13` | loi n° 63-13 du 27 mai 1963 instituant la caisse spéciale de compensation des transports routiers | n° 26 de 1963, p. 740-741 | `1963/1963F/Jo02663.pdf` |
| `lf-1978` | loi n° 77-81 du 31 déc. 1977, art. 37-38 | n° 86 du 30 déc. 1977, p. 3603 | `1977/1977F/Jo08677.pdf` |
| `lf-1982` | loi n° 81-100 du 31 déc. 1981, art. 110 (intitulé seul) | n° 84 de 1981, p. 3048 | URL non vérifiée |
| `lf-1984` (existe) | loi n° 83-113 du 30 déc. 1983, art. 38-47 et 99-103 | n° 86 du 30 déc. 1983, p. 3378-3379 et 3385-3386 | `1983/1983F/Jo08683.pdf` |
| `loi-85-77` | loi n° 85-77 du 4 août 1985 portant organisation des transports terrestres | n° 58 du 9 août 1985, p. 1000-1001 | `1985/1985F/Jo05885.pdf` |
| `arrete-1987-02-14-tarifs-voyageurs` | arrêté du ministre du transport du 14 févr. 1987 | n° 13 du 20 févr. 1987, p. 261 | `1987/1987F/Jo01387.pdf` |
| `arrete-1989-08-10-tarifs-urbains`, `…-interurbains` | arrêtés du 10 août 1989 | n° 58 du 29 août 1989, p. 1282-1284 et 1285-1286 | `1989/1989F/Jo05889.pdf` |
| `arrete-1990-07-30-tarifs-urbains`, `…-interurbains` | arrêtés du 30 juill. 1990 | n° 52 du 10 août 1990, p. 1045-1048 et 1048 | `1990/1990F/Jo05290.pdf` |
| `arrete-1991-07-02-tarifs-urbains`, `…-interurbains` | arrêtés du 2 juill. 1991 | n° 50 du 12 juill. 1991, p. 1294-1297 et 1297-1298 | `1991/1991F/Jo05091.pdf` |
| `arrete-1992-08-24-tarifs-urbains`, `…-interurbains` | arrêtés du 24 août 1992 | n° 57 du 1er sept. 1992, p. 1128-1133 et 1134 | `1992/1992F/Jo05792.pdf` |
| `arrete-1993-08-26-tarifs-urbains`, `…-interurbains` | arrêtés du 26 août 1993 | n° 67 du 7 sept. 1993, p. 1430-1435 et 1436 | `1993/1993F/Jo06793.pdf` |
| `arrete-1993-05-06-handicapes-transport` | arrêté du 6 mai 1993 (accès des personnes handicapées) | n° 37 du 18 mai 1993, p. 677 | `1993/1993F/Jo03793.pdf` |
| `arrete-1998-04-27-tarifs-urbains` | arrêté du 27 avr. 1998 | n° 37 du 8 mai 1998, p. 997-1001 | `1998/1998F/Jo03798.pdf` |
| `arrete-1998-06-25-gratuite-douanes` | arrêté du 25 juin 1998 | n° 53 du 3 juill. 1998, p. 1422 | `1998/1998F/Jo05398.pdf` |
| `arrete-1998-07-29-abonnements-scolaires` | arrêté du 29 juill. 1998 | n° 63 du 7 août 1998, p. 1723-1725 | `1998/1998F/Jo06398.pdf` |
| `arrete-1999-02-06-tarifs-interurbains` | arrêté du 6 févr. 1999 | n° 12 du 9 févr. 1999, p. 229 | `1999/1999F/Jo01299.pdf` |
| `arrete-2000-02-17-tarifs-urbains` | arrêté du 17 févr. 2000 | n° 16 du 25 févr. 2000, p. 535-536 | `2000/2000F/Jo0162000.pdf` |
| `decret-2001-2621` | décret n° 2001-2621 du 9 nov. 2001 (cahier des charges de la SNCFT) | n° 92 du 16 nov. 2001, p. 3951-3954 | `2001/2001F/Jo0922001.pdf` |
| `loi-2003-33` | loi n° 2003-33 du 28 avr. 2003 (fusion) | n° 34 du 29 avr. 2003, p. 1290 | `2003/2003F/Jo0342003.pdf` |
| `loi-2004-33` | loi n° 2004-33 du 19 avr. 2004 | n° 32 du 20 avr. 2004, p. 996-1003 | `2004/2004F/Jo0322004.pdf` |
| `arrete-2011-06-24-gratuite-surete` | arrêté conjoint du 24 juin 2011 | n° 47 du 28 juin 2011, p. 1100-1101 | `2011/2011F/Jo0472011.pdf` |
| `loi-2012-26` | loi n° 2012-26 du 24 déc. 2012 | n° 103 du 28 déc. 2012, p. 3366-3368 | `2012/2012F/Jo1032012.pdf` |
| `decret-gouv-2017-987` | décret gouvernemental n° 2017-987 du 17 août 2017 | **édition arabe** n° 70-71 des 1er-5 sept. 2017, p. 2970-2971 : `https://www.pist.tn/jort/2017/2017A/Ja0712017.pdf` (200, PDF). **Édition française : `2017F/Jo0702017.pdf` et `Jo0712017.pdf` répondent 404 ; fascicule absent du corpus local** — pagination française inconnue | — |

**Rapports et études** (PDF rangés dans `~/projets/tunisia-data/data/raw/`, hors git)

| Clé suggérée | Document | Fichier | Famille |
|---|---|---|---|
| `minfin-budget-transport-2013` … `-2017` | Ministère des Finances, « ميزانية وزارة النقل لسنة N », cinq éditions | `minfinances/portail_ancien/budgets_ministeres/201{3..7}_budget*transport*.pdf` (déjà rangés ; fiche `minfinances-portail-ancien.md`) | A |
| `minfin-transferts-garanties-lf2020`, `-lf2022`, `-lf2024`, `-lf2025` | Ministère des Finances, « Rapport sur les transferts et les garanties au profit des entreprises publiques et des établissements publics non administratifs » | `caisses/minfin/annexe8_transferts_LF20{20,22,24,25}.pdf` (déjà rangés ; URL d'origine à reprendre de la fiche qui les a collectés — non retrouvée sous ce nom dans `sources/`) | A |
| `minfin-entreprises-publiques-lf2020`, `-lf2021` | Ministère des Finances, « Rapport sur les entreprises publiques » | `caisses/minfin/Annexe_9_LF2020-…pdf`, `Annexe_9_LF2021_…pdf` (fiche `minfin-entreprises-publiques-caisses.md`) | A |
| `minfin-finances-publiques-2010` (existe) | rapport sur les finances publiques 2010 | `…/rapports_finances_publiques/2010_rapport_finances_publiques.pdf` | A |
| `ins-bms` (existe, bibliographie commune) | INS, *Bulletin mensuel de la statistique*, tableau des prix moyens de détail à Tunis | `ins-bms/bms-AAAA-MM.pdf` | A |
| `ins-annuaire-statistique-2001` et suivantes | INS, *Annuaire statistique de la Tunisie*, chapitre « Transport » | `ins-publications/annuaire-statistique/*.pdf` | A |
| `cour-comptes-2008-transport-terrestre` | Cour des comptes, « إشراف الدولة على قطاع النقل البري », 26 p., mis en ligne le 15 juin 2008 | **rangé ce jour** : `cour-des-comptes/81/Rapport_81_2018-08-15-12-51-01.pdf` ; `https://www.courdescomptes.nat.tn/wp-content/uploads/pdf_rapport/Rapport_81_2018-08-15-12-51-01.pdf` ; SHA-256 `7fac23ac7184f1fb3284e46d90b61e8e34e2a113c2e6de73d0162e0f00d6f005` | B |
| `cour-comptes-2016-ministere-transport` | Cour des comptes, « وزارة النقل », 43 p., mis en ligne le 15 juin 2016 | **rangé ce jour** : `…/81/Rapport_81_2018-08-16-10-44-17.pdf` ; même racine d'URL ; SHA-256 `981e39d91b6a2bf1b59d69cc4843ba4841fff5a93dbf856075bce6c7592de132` | B |
| (non exploité) | Cour des comptes, « الشركة الوطنية للنقل بين المدن », 29 p., mis en ligne le 15 juin 2017 | **rangé ce jour** : `…/81/Rapport_81_2018-08-16-11-02-16.pdf` ; SHA-256 `26731d60d29931c6b06d9519946ea581d2d672b1d36615ad1ac2e5f8b9913848` | B |
| `banque-mondiale-2016-livre-blanc-transports` | Banque mondiale, *République tunisienne. Livre blanc relatif au secteur des transports et de la logistique*, rapport n° ACS18045, 18 mai 2016, 92 p. | **rangé ce jour** : `banque-mondiale-rapports/bm_2016_livre_blanc_transports_logistique_ACS18045.pdf` ; `https://documents1.worldbank.org/curated/en/339961488471609720/pdf/ACS18045-REVISED-PUBLIC.pdf` ; SHA-256 `9a683dd933cbcfd85d3503b1b417e9a63e1b9b6da45c863020981f1f19092771` | C |
| `jouini-lustig-moummi-shimeles-2017-ceq38` (existe) | CEQ, document de travail n° 38 | déjà rangé | évaluation |

**Presse** (à ne citer que pour dater) : Webmanagercenter avec TAP, « Réajustement des tarifs des
transports publics », 30 mai 2021,
`https://www.webmanagercenter.com/2021/05/30/468470/reajustement-des-tarifs-des-transports-publics/` ;
Tuniscope, « TRANSTU : Tarifs des abonnements scolaires et universitaires », 6 mars 2018,
`https://www.tuniscope.com/article/15729/business/services/universitaires-155214`. Les deux pages ont été
relues sur leur texte brut le 11 octobre 2026 : « le prix du ticket de 320 et 470 millimes a augmenté
pour atteindre 500 millimes, contre une baisse du tarif du ticket de 650 millimes » (première) ;
« Abonnement Réseau Général BUS (Annuel), Prix : 66,250 D », « Abonnement zone urbaine BUS
(annuel), Prix : 36,500 DT », « TGM 2ème classe (annuel), Prix : 60,050 DT » (seconde). Le tarif
du métro (47,450 D) n'a été lu que par l'outil de résumé.

---

## 4. Notions à glossaire

| Terme (FR) | Terme (AR) | Source canonique pressentie | État |
|---|---|---|---|
| Compensation du transport | دعم النقل | existe (`compensation-transport`) : **définition à enrichir** — subventions par société inscrites au budget du ministère du Transport sous « دعم النقل العمومي », pour l'essentiel au titre du transport scolaire et universitaire | à réviser |
| Soutien du transport public (libellé budgétaire) | دعم النقل العمومي | budgets du ministère du Transport 2013-2017 | AR attesté ; à mettre en synonyme |
| Abonnement scolaire | الاشتراك المدرسي (pluriel الاشتراكات المدرسية) | arrêté du 29 juill. 1998 (FR) ; budgets (AR) | FR et AR attestés |
| Transport scolaire et universitaire | النقل المدرسي والجامعي | rapport sur les finances publiques 2010 | AR attesté |
| Manque à gagner (du transporteur) | النقص الحاصل في المداخيل | loi n° 2004-33, art. 12 (FR décodé) ; Cour des comptes et décret n° 2017-987 (AR) | attestés ; FR à relire à l'image |
| Gratuité du transport | مجانية النقل / النقل المجاني | arrêtés de 1998 et 2011 ; décret n° 2017-987 | attestés |
| Tarif réduit | تعريفة منخفضة | arrêté du 27 avr. 1998, art. 11 ; Cour des comptes | attestés |
| Section (tarifaire) | — | arrêtés tarifaires (« nombre de sections ») | FR attesté ; AR à relever dans l'édition arabe d'un arrêté |
| Obligation de service public ; contribution pour obligation de service public | — | décret n° 2001-2621, art. 19 à 21 | FR décodé, à relire ; AR à relever |
| Caisse de compensation et de soutien des transports routiers | — | LF 1984, art. 99 | FR (OCR) ; AR à relever |
| Caisse spéciale de compensation des transports routiers | — | loi n° 63-13 | FR ; AR au miroir iort (intitulé) |
| Sociétés régionales de transport | الشركات الجهوية للنقل | budgets | attestés |
| Société des transports de Tunis | شركة النقل بتونس | budgets ; loi n° 2003-33 | attestés ; « Transtu » est le sigle d'usage, non le nom légal |
| Corps actifs | الأسلاك النشيطة | décret n° 2017-987 | AR attesté ; FR à vérifier dans un texte français |
| Autorité régionale organisatrice des transports terrestres | السلطة الجهوية المنظمة للنقل البري | loi n° 2004-33, art. 3 et 9 | attestés |

---

## 5. Ce qui n'est pas établi, et les fiches de recherche

### Lacunes (TODO, ne rien inventer)

1. **Décomposition par société avant 2012 et après 2017 au sens strict du poste.** 2012-2017 :
   établie (crédits). 2018-2024 : seule la colonne « interventions » est lue, plus large que le
   poste. Les budgets du ministère du Transport de 2018 à 2026 (qui portent la ligne « دعم النقل
   العمومي » par société) ne sont pas dans l'entrepôt : **à collecter sur `finances.gov.tn` et
   `gbo.tn`, puis aux archives du web**, avant toute demande à l'administration. 2003-2011 : budgets
   du ministère antérieurs à 2013, à chercher aux archives du web de `portail.finances.gov.tn`.
2. **Décomposition par nature** (scolaire, tarifs réduits, gratuités) : aucune source ne la publie.
3. **Crédits et recettes du fonds spécial de 1984 à sa disparition**, la date de cette disparition,
   et celle à laquelle le budget général prend le relais de la taxe affectée : tableaux des lois de
   finances annuelles et rapports annuels de la BCT de 1985 à 2002, **non dépouillés**. Le poste est
   dans les rapports budgétaires à partir de 2003 ; ce qui se passe entre les deux n'est pas lu.
   C'est la principale question ouverte pour la longue période.
4. **Tarifs entre mars 2000 et novembre 2007** : le ticket de deux sections passe de 390 à
   450 millimes à des dates inconnues. → fiche ci-dessous.
5. **Barèmes de 2010 et de 2021** : connus par l'INS (un prix) et la presse, pas par un acte.
6. **Tarifs de la SNCFT** : seuls les intitulés des arrêtés d'approbation sont relevés (les barèmes
   n'y sont pas, ils sont « approuvés ») ; le billet de train de l'INS est le seul repère.
7. **Sociétés régionales** : ni voyageurs, ni recettes, ni taux de couverture. Pistes : rapports de
   la Cour des comptes sur les sociétés de Béja (2014), Gafsa (2012), Jendouba (2010), Kairouan et
   Sfax (2009), du Sahel (2006), au catalogue `cour-des-comptes-catalog.csv`, rubrique 81, **non
   téléchargés** ; éditions arabes du Rapport sur les entreprises publiques (LF 2022 à LF 2025),
   **non dépouillées pour le transport**.
8. **Taxe unique de compensation de transports routiers, produit annuel** : une ligne « المعلوم
   التعويضي على النقل » existe dans les annexes des rapports sur les finances publiques de 2008 et
   de 2010 (ordre de grandeur : 84 à 105 MD par an, colonnes alternant loi de finances et
   résultats) ; **années et valeurs à relire à l'image, rien n'est transcrit ici**. Elle relève du volume « Fiscalité » ; rien
   n'indique qu'elle soit affectée au poste « transport » après 1984 : ne pas l'écrire.
9. **Articles 11 et 12 de la loi n° 2004-33, articles du décret n° 2001-2621** : lus sur une couche
   texte décodée, sans accents ; à relire à l'image avant citation littérale.
10. **Statut du relèvement d'août 2010** : la SNCFT (billet de train) et l'autobus bougent le même
    mois ; l'acte n'est pas identifié.

### Fiches proposées pour `docs/recherches.yml` (aucune fiche existante ne porte sur le transport : `recherches.py lister` du 11 octobre 2026)

```yaml
- id: r-transport-tarifs-apres-2000
  objet: acte fixant ou modifiant les tarifs du transport public collectif de personnes (réseaux urbains et suburbains, métro léger et TGM, interurbain par route, abonnements scolaires) après les arrêtés du ministre du transport du 6 février 1999 (interurbain) et du 17 février 2000 (urbain) — relèvements constatés par l'INS entre mars 2000 et novembre 2007, en août 2010 et en juin 2021
  ou: [precis/fr/compensation/_transport.qmd]
  requetes:
    titres_fts:
    - tarifs AND transport
    titres_like:
    - '%transport scolaire%'
    - '%abonnement%scolaire%'
    - '%transport public collectif%'
    - '%metro leger%'
    iort_ar: [تعريفات النقل, تعريفة النقل, الاشتراكات المدرسية, معاليم النقل, النقل العمومي]
    depuis: 2000-02-25
  passes:
  - date: 2026-10-11
    role: documentaliste
    sources: [jort_cache]
    couverture: 'Titres de jort_cache seulement, dernière publication indexée le 2 octobre 2026. Requêtes jouées en plus de celles du champ requetes, en SQL : titre like ''%tarif%'' avec ''%transport%'', ''%voyageurs%'', ''%metro%'', ''%chemins de fer%'', ''%louage%'' ou ''%taxi%'' depuis le 1er janvier 2000 ; titre like ''%abonnement%'' avec ''%scolaire%'' ou ''%transport%'' ; ''%eleves%'' ou ''%etudiants%'' avec ''%transport%'' ; ''%تعريف%'' avec ''%النقل%'' ou ''%نقل%'' ; ''%اشتراكات%'' ; arrêtés portant « transport » ou « النقل » au titre ou au ministère dans trois fenêtres de signature (mars 2000-novembre 2007 : 115 arrêtés ; juin-septembre 2010 : aucun ; avril-juin 2021 : 3), filtrés sur prix, tarif, سعر, أسعار, تعريف, voyageurs, personnes. Après le 17 février 2000, aucune réponse ne porte sur un tarif de transport collectif de personnes (ports, manutention, marchandises, amendes transactionnelles, autorisations). NON FAIT : plein texte des fascicules ; miroir iort ; fascicules inconnus de la base ; lecture des 115 arrêtés de 2000-2007 au-delà de leur intitulé. Voie latérale ouverte, hors Journal officiel : INS, Bulletin mensuel de la statistique, prix du billet d''autobus à Tunis (450 jusqu''en juillet 2010, 470 d''août 2010 à mai 2021, 500 depuis juin 2021).'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - jouer le plein texte (« tarifs de transport », « abonnements scolaires ») sur les fascicules de 2000 à 2010 et de 2021
  - chercher les communiqués de la société des transports de Tunis et de la SNCFT aux archives du web (2003, 2005, 2008, 2010, 2021)
  - relever dans le Bulletin mensuel de la statistique antérieur à novembre 2008, s'il est obtenu, le mois de chaque relèvement entre 2000 et 2007

- id: r-transport-decret-manque-a-gagner
  objet: décret fixant la méthode de calcul du manque à gagner des transporteurs publics de personnes en cas de gratuité ou de tarifs réduits (loi n° 2004-33 du 19 avril 2004, art. 12), et décret fixant l'assiette et le recouvrement du droit sur le transport collectif public dû par les bénéficiaires (même loi, art. 11) — autres que le décret gouvernemental n° 2017-987 du 17 août 2017, limité aux corps actifs
  ou: [precis/fr/compensation/_transport.qmd]
  requetes:
    titres_fts:
    - manque gagner OR (gratuite AND transport) OR (tarifs AND reduits AND transport)
    iort_ar: [النقل العمومي, 33 لسنة 2004]
    depuis: 2004-04-20
  passes:
  - date: 2026-10-11
    role: documentaliste
    sources: [jort_cache]
    couverture: 'Titres de jort_cache seulement, dernière publication indexée le 2 octobre 2026. Requêtes jouées en plus, en SQL : titre like ''%gratuit%'', ''%reduction%'' ou ''%tarif reduit%'' avec ''%transport%'' ; ''%handicap%'' avec ''%transport%'' ou ''%gratuit%'' ; ''%compensation%'' avec ''%transport%''. « النقل العمومي » depuis 2000 rend quatre notices, dont le décret gouvernemental n° 2017-987 (intitulé arabe seul à l''index ; lu à l''image dans l''édition arabe, JORT n° 70-71 de 2017, p. 2970-2971). « 33 لسنة 2004 » rend deux notices sans rapport (décret gouvernemental n° 2016-1101 ; arrêté du 10 octobre 2019 sur les amendes transactionnelles). Trouvés par ailleurs : arrêtés du 25 juin 1998 (douanes) et du 24 juin 2011 (sûreté intérieure). Constat extérieur concordant, qui ne vaut pas preuve d''inexistence : la Cour des comptes relève l''absence des deux décrets en octobre 2007 (rapport mis en ligne en 2008, p. 99) puis dans son rapport mis en ligne en juin 2016 (p. 281). NON FAIT : plein texte, miroir iort.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - jouer le plein texte (« manque à gagner », « droit sur le transport collectif ») sur les fascicules de 2004 à 2026
  - lire l'arrêté du 15 août 2011 sur la gratuité des agents des forces de sûreté intérieure relevant du ministère de la justice, visé par le décret n° 2017-987
```

Les deux fiches reprennent la structure de `r-tarifs-electricite-gaz-apres-1992` (clés `ou`,
`requetes`, `passes`, `a_faire`). Le champ `requetes` ne porte que des termes joués tels quels ;
les conjonctions SQL, que le registre ne sait pas exprimer, sont dites dans `couverture`. **Elles
ne sont pas enregistrées** : `scripts/recherches.py verifier` n'a pas été lancé dessus, et l'ancre
`ou` vise un chapitre qui n'existe pas encore.

---

## 6. Séries à verser dans `tunisia-data`

| Série | Source, page | Étendue | État | Priorité |
|---|---|---|---|---|
| Soutien du transport public par société, crédits | budgets du ministère du Transport 2013-2017, tableau des indicateurs (p. PDF 10, 19, 18, 18, 17) et tableau des articles 170 à 178 | 2012-2017 | tableau A1 prêt ; 2013, 2014, 2016 à relire à l'image | 1 |
| Interventions par société | rapport sur les transferts et les garanties, tableaux annuels « التحويلات بعنوان سنة N » | 2016-2024 | tableau A2 prêt ; 2016-2017 à relire à l'image (chiffres inversés) ; extraction par la géométrie recommandée, comme `extract_caisses_minfin.py` | 1 |
| Nombre d'abonnements scolaires par société | budgets, même tableau | 2012-2017, deux segments | prêt (§ 1.4 d) | 2 |
| Prix du billet d'autobus, du billet de train et de l'abonnement scolaire | INS, BMS, tableau des prix de détail à Tunis | nov. 2007 – juill. 2026, mensuel | à extraire des 213 numéros (le moteur de la note `compensation-prix-carburants-1993-2018.md` lit déjà ce tableau pour le gasoil) | 1 |
| Tarifs repères du *Journal officiel* | arrêtés de 1987 à 2000 (§ 1.2) | 1987-2000, par date d'effet | tableau T1 prêt, lu à l'image ; 1977-1986 à lire à l'image | 2 |
| Métro léger et TGM : recettes, dépenses, voyageurs, parcours | INS, *Annuaire statistique*, chapitre « Transport », tableau du transport ferroviaire (suite et fin) | 1995-2023 par chevauchement de 22 éditions | 1995-2001 transcrit ; le reste à extraire, **sens des colonnes à vérifier par édition** (éditions bilingues : années décroissantes) | 2 |
| SNCFT : voyageurs (grandes lignes, banlieues), voyageurs-km | idem | 1995-2023 | repéré, non transcrit | 3 |
| Société de Tunis : trafic par catégorie ; SNCFT : trafic scolaire | Banque mondiale, *Livre blanc*, annexe, p. 70-77 | 2007-2014 | transcrit (§ 1.4), **famille C, fichier séparé** | 2 |

Rangé ce jour dans l'entrepôt, sans commit : trois rapports de la Cour des comptes
(`data/raw/cour-des-comptes/81/`, lignes ajoutées à `sources/cour-des-comptes-telechargements.csv`) ;
le *Livre blanc* de la Banque mondiale (`data/raw/banque-mondiale-rapports/`, ligne ajoutée à
`sources/banque-mondiale-rapports-urls.csv`) ; fiche `sources/compensation-transport.md`.

---

## 7. Frontière avec un futur texte sur les entreprises publiques

À signaler, non à traiter dans le chapitre :

- **Apurements de dettes par le budget**, qui ne sont pas de la compensation mais passent par la
  même colonne « interventions » : 2011, dettes de la société de Tunis envers la Société nationale
  de distribution des pétroles et la CNRPS, 244 MD (Cour des comptes 2016, p. 281) ; 2017, 145,3 MD
  envers la même société pétrolière (Rapport sur les entreprises publiques, LF 2020, p. imprimée 73) ; loi
  n° 2005-73 du 4 août 2005 « relative à l'assainissement de la situation financière » des deux
  sociétés fusionnées (JORT n° 62 de 2005 ; intitulé seul) ; SNCFT, équilibre rétabli en 2006 pour
  106 MD selon le *Livre blanc* (p. PDF 78).
- **Comptes** : société de Tunis, résultat net − 125,5 MD en 2013, − 187,5 MD en 2018, capitaux
  propres − 571,5 MD et pertes cumulées 1 059,5 MD à la fin de 2017 ; SNCFT, résultat net − 81,3 MD
  en 2017, − 91,1 MD en 2018 (Rapports sur les entreprises publiques LF 2020 et LF 2021).
- **Dettes et garanties** : endettement de la société de Tunis 1 112,5 MD en 2017, dont 198,8 MD
  envers les caisses sociales ; garanties de l'État (rapport sur les transferts et les garanties,
  seconde partie) ; créances des sociétés sur les ministères au titre des gratuités non payées
  (défense : 8 MD envers la société de Bizerte, Cour des comptes 2016 ; intérieur : presse).
- **Investissement** : colonne « investissements » du même rapport (autobus, réseau ferroviaire
  rapide), et avantages fiscaux à l'acquisition des véhicules de transport public (décrets annuels
  de 2003 à 2014 à l'index) — volume « Fiscalité ».
- **Le lien à écrire dans le chapitre, en une phrase** : la compensation ne couvre qu'une partie du
  manque à gagner (§ 1.1 d) ; le reste se retrouve dans les pertes, puis dans les apurements — c'est
  ce second étage qui appartient au texte sur les entreprises publiques.
