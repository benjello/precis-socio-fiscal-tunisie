# Les aides aux élèves du primaire et du secondaire : note documentaire

Note du documentaliste, 17 octobre 2026, pour le chapitre 5 du livre de l'éducation
(`docs/notes/education-plan-2026-10-17.md`, sections 2, 5, 6 et 7) et pour la section 3 du
chapitre 2 (frais à la charge des familles). Aucun `.qmd` n'est écrit. Les fiches de recherche
proposées sont dans `docs/notes/education-recherches-B.yml`. Ce fichier est à fusionner dans
`docs/recherches.yml`. Les ancres `ou:` des fiches visent un `_aides.qmd` qui n'existe pas encore :
elles sont proposées, à ajuster par l'architecte.

**États employés.** « lu » : lu au fascicule, à l'image ou dans la couche de texte, aux articles
indiqués. « lu (OCR) » : lu dans une océrisation faite ici, sans relecture à l'image de la valeur
citée. « index » : seule la notice de `jort_cache.db` est connue. « à lire » : rien n'est établi.

**Corpus et outils.** Fascicules de `~/projets/PDFs-legislation-tunisie/PDFs/JORT/` ; notices de
`jort_cache.db` (dernière publication indexée le 2 octobre 2026) ; miroir iort
(`data/iort/textes/md/`). Les fascicules de 1966, 1971, 1972, 1974, 1976, 1991 et 1992 n'ont pas
de couche de texte : ils ont été océrisés (tesseract `fra`, 300 dpi) dans `/tmp/education-ocr-B/`,
et chaque valeur chiffrée citée ci-dessous comme « lu » a été relue à l'image. Le fascicule n° 86
de 2004 est en police décalée (décodé, voir outillage-sources.md, § 5).

---

## 0. Trois corrections au plan

1. **La loi sur la restauration des élèves est la loi n° 2009-32, pas la loi n° 2009-39.**
   L'édition française (JORT n° 51 du 26 juin 2009, p. 1660) et l'édition arabe (même numéro,
   p. 2180, « قانون عدد 32 لسنة 2009 مؤرخ في 23 جوان 2009 ») portent toutes deux le n° 32. La notice
   109742 de `jort_cache` la numérote à tort 2009-39 ; la loi n° 2009-39 est celle du 8 juillet 2009
   portant mise à la retraite avant l'âge légal (clé existante `loi2009-39` dans
   `precis/fr/references.json`). La fiscalité cite déjà le bon texte, sous la clé
   `loi-2009-32-restauration-formation` (`precis/fr/fiscalite/references.json` ;
   `_tva_tableaux.qmd`, ligne du n° 30 bis). → Corriger le plan (§ 3, chapitre 5, section 5, et
   annexe 8.2).
2. **La loi de finances pour 1977 ne porte pas une mesure de bourse : elle porte une sanction.**
   L'article 15 de la loi n° 76-115 oblige le contribuable non salarié qui demande une attestation
   fiscale pour la bourse de son enfant à s'engager à restituer les sommes indûment perçues,
   majorées d'une pénalité de 10 % par an (§ 1.5). Ce n'est ni un montant ni une condition
   d'attribution.
3. **La suite des bourses scolaires après 1974 tient en partie à un texte de 2016.** Le décret
   gouvernemental n° 2016-664 confie à l'office qu'il crée l'attribution des bourses scolaires
   « selon les critères qui seront fixés par décision du ministre de l'éducation » (art. 2), et le
   budget de 2017 transfère à cet office les crédits des bourses scolaires (§ 5.1). Le dispositif
   existe donc encore en 2016-2017. Aucun texte publié qui en fixe les critères ou les montants après
   l'arrêté du 12 août 1974 n'est identifié.

---

## 1. Les bourses scolaires

### 1.1 Arrêté du secrétaire d'État à l'Éducation nationale du 3 octobre 1966 — lu

*Relatif au règlement des bourses scolaires pour les enseignements du second et du premier degré.*
JORT n° 43, fascicule daté des 4-7 octobre 1966, p. 1449-1451 (FR ; fascicule
`1966/fr/Jo04366.pdf`, pages 5 à 7 du fichier). Recid 71970. Visa : loi n° 58-118 du 4 novembre
1958. Lu à l'image : art. 1 à 22.

- **Objet de la bourse (art. 3)** : elle « est destinée à couvrir en partie ou en totalité les
  frais de demi-pension ou de pension. Elle ne porte en aucun cas sur les frais de fournitures
  scolaires ou de trousseau. »
- **Bénéficiaires (art. 2)** : élèves de nationalité tunisienne « appartenant à une famille
  nécessiteuse ». **Établissements publics seulement (art. 4).**
- **Bourse entière (art. 5)** : seulement en cas d'indigence, ou pour un orphelin ou un enfant de
  parents séparés. **Bourse de pension (art. 6)** : en principe aux élèves dont la famille habite
  loin de tout établissement du cycle demandé.
- **Conditions scolaires** : internat primaire, moyenne annuelle d'au moins 12/20 (art. 8) ; entrée
  en 1re année du secondaire ou du moyen, au moins 11/20 à l'examen d'entrée (art. 9) ; élèves du
  secondaire ou du moyen, âge de la classe et moyenne générale de 10/20 (2e cycle) ou 11/20
  (1er cycle) (art. 10).
- **Plafond de revenu** : non chiffré par l'arrêté. Sont écartés les dossiers « comportant un
  revenu familial dépassant un chiffre fixé chaque année par la Commission des Bourses Scolaires »
  (art. 14 b). Le dossier comprend la déclaration de revenus de l'année précédente (art. 11).
- **Commission des bourses** (art. 12-16), réunie une fois par an ; diminution ou suppression pour
  amélioration de la situation de la famille, travail insuffisant ou indiscipline, et suppression
  automatique en cas de redoublement sauf motif valable (art. 18-19).
- **Date de validité** : les bourses « ne sont valables qu'à partir du 1er octobre qui suit la
  décision » de la commission (art. 21).
- **Date d'effet** : pas de clause. Règle d'avant 1993 : un jour franc après la publication ; le
  fascicule couvre les 4-7 octobre 1966 (l'index donne le 4 octobre) : jour exact à établir.
- Abrogé par le décret n° 71-356 (art. 13).

### 1.2 Décret n° 71-356 du 28 septembre 1971 — lu

*Fixant l'organisation et les conditions d'attribution des bourses scolaires pour les élèves de
l'enseignement secondaire.* JORT n° 43, fascicule des 5-8 octobre 1971, p. 1307-1320 (FR ;
`1971/fr/Jo04371.pdf`, pages 13 à 26 du fichier ; p. 1311-1320 : modèles de formulaires).
Recid 103336. Visas : loi n° 58-118, notamment son article 3 ; arrêté du 3 octobre 1966.

- **Objet (art. 3)** : même rédaction qu'en 1966 (frais de demi-pension ou de pension, jamais
  fournitures ni trousseau). **Public seulement (art. 4).** Les élèves étrangers peuvent être
  autorisés à demander (art. 2).
- **Décision (art. 5)** : ministre de l'Éducation nationale, sur propositions des commissions
  régionales arrêtées « conformément aux critères figurant à l'annexe ». Le ministre fixe « le taux
  de la bourse ».
- **Commission nationale** (art. 6-8, avis sur les options, la réglementation, les crédits) et
  **commission régionale par gouvernorat** (art. 9-11). La décision « est fonction des crédits
  consacrés aux bourses » (art. 9, 2°).
- **Validité au 1er octobre** qui suit la décision (art. 12).
- **Abrogations (art. 13)** : le décret n° 60-260 du 19 juillet 1960 « relatif aux remises de
  principe dans les établissements d'enseignement public » et l'arrêté du 3 octobre 1966.
- **Date d'effet** : pas de clause ; un jour franc après publication (fascicule des 5-8 octobre
  1971 ; index : 5 octobre) ; jour exact à établir.

**L'annexe : un barème à points** (lu à l'image, p. 1308-1311). Les revenus sont les « revenus
annuels de la famille », en dinars.

| Partie | Critère | Points |
|---|---|---|
| 1re — boursiers de 1970-1971 (renouvellement) | conduite et assiduité | 0 à 5 (conseil des professeurs) |
| | parents : orphelin des deux / d'un parent / divorcés | 5 / 3 / 2 |
| | habitation : dans la commune / hors commune avec transport / sans transport | 0 / 2 / 5 |
| | revenu : ≤ 100 D / 101-200 / 201-300 / 301-400 / 401-500 / > 500 D | 35 / 28 / 21 / 14 / 7 / 0 |
| | **fraction** : 45-50 / 40-44 / 31-39 / 21-30 points | bourse complète / 3/4 / 1/2 / 1/4 |
| 2e — bourse nouvelle | moyenne : 9-10 / 10-11 / 11-12 / 12-13 / 13-14 / > 14 sur 20 | 0 / 4 / 8 / 12 / 16 / 20 |
| | conduite ; parents ; habitation | comme ci-dessus |
| | frères et sœurs (hors actifs et boursiers) : 4 / 5 / 6 / 7 / plus de 8 | 1 / 2 / 3 / 4 / 5 |
| | revenu : ≤ 100 D / 100-200 / 201-300 / 301-400 / 401-500 / > 500 D | 10 / 8 / 6 / 4 / 2 / 0 |
| | **fraction** : 41-50 / 36-40 / 31-35 / 25-30 | complète / 3/4 / 1/2 / 1/4 |
| 3e — augmentation de fraction | mêmes critères et barème que la 2e partie | |
| 4e — admis au concours d'entrée en 1re année | moyenne au concours : 10-11 / 11-12 / 12-13 / 13-14 / > 14 | 4 / 8 / 12 / 16 / 20 |
| | parents ; frères et sœurs ; habitation | comme la 2e partie |
| | revenu : < 100 D / 101-200 / 201-300 / 301-400 / 401-500 / > 500 D | 15 / 13 / 11 / 9 / 7 / 0 |
| | **fraction** : 50-41 / 40-36 / 35-31 / 30-25 | complète / 3/4 / 1/2 / 1/4 |

Le redoublement supprime la bourse, sauf maladie et avis favorable du conseil des professeurs
(remarques des 1re et 2e parties).

### 1.3 Décret n° 72-229 du 5 juillet 1972 — lu (l'annexe en partie)

*Modifiant le décret n° 71-356.* JORT n° 28, fascicule des 7-11 juillet 1972, p. 966-969 (FR ;
`1972/fr/Jo02872.pdf`, pages 14 à 17 du fichier). Recid 103119.

- **Art. 1** : nouveaux art. 6, 7 et 10. La commission nationale ne choisit plus les imprimés.
  Nouvelle composition des commissions ; la commission régionale reçoit les inspecteurs régionaux de
  l'enseignement primaire.
- **Art. 2** : l'annexe de 1971 est abrogée et remplacée.
- **Nouvelle annexe, 1re partie (bourse nouvelle)**, lue à l'image (p. 967-968) :
  - moyenne, en points « 1er cycle et enseignement professionnel / 2e cycle » : 9 à 9,99 → 0 / 2 en
    cas de passage, 0 en cas de redoublement ; 10-10,99 → 4 / 6 ; 11-11,99 → 8 / 10 ; 12-12,99 →
    12 / 14 ; 13-13,99 → 16 / 18 ; 14-14,99 → 18 / 20 ; plus de 15 → 20 / 20 ;
  - conduite et assiduité : 0 à 5 ;
  - **condition familiale : 0 à 5, à l'appréciation de la commission régionale** (décès, divorce,
    incapacité de travail des parents ou tout autre facteur). Le barème fixe de 1971 disparaît ;
  - frères et sœurs de moins de 20 ans, hors actifs et boursiers : 4 → 3 ; 5 → 4 ; 6 et plus → 5 ;
  - **orientation d'office** : 5 points pour l'élève orienté hors de la délégation de résidence ;
    5 points si la famille réside hors de la commune de l'établissement sans transport public
    régulier ;
  - revenus « après déduction » : ≤ 100 D → 15 ; 101-200 → 10 ; 201-300 → 7 ; 301-400 → 5 ;
    401-500 → 3 ; > 500 D → 0 ;
  - **fraction : 45-55 → complète ; 40-44 → 3/4 ; 30-39 → 1/2. Le quart de bourse disparaît.**
- 2e partie (augmentation) et 3e partie (redoublement : maintien ou suppression par le conseil des
  professeurs, pas d'augmentation pour le redoublant) : lues en OCR.
- 4e partie (concours d'entrée) : lue en OCR seulement. Barème de la moyenne de 10/20 à 16 et plus,
  revenus de 15 à 0 points. Seules les deux premières lignes du tableau des fractions sont lisibles :
  41-50 → complète, 35-40 → 3/4. Le reste est à lire (p. 969).
- **Date d'effet** : pas de clause ; un jour franc après publication (index : 7 juillet 1972).

### 1.4 Décret n° 74-783 du 5 août 1974 et arrêté du 12 août 1974 — lus

JORT n° 52, fascicule des 9-13 août 1974, p. 1822-1824 (FR ; `1974/fr/Jo05274.pdf`, pages 24 à 26
du fichier). Recids 102157 (décret) et 69697 (arrêté).

**Décret n° 74-783.**
- Nouvel art. 5 : les bourses sont accordées par le ministre « en fonction des crédits consacrés à
  cet effet et sur proposition des commissions régionales des bourses conformément aux critères
  d'attribution **fixés par arrêté** du Ministre de l'Education Nationale après avis de la
  commission nationale ». Les critères quittent le décret pour l'arrêté.
- Nouvel art. 8 : la commission nationale se réunit en décembre ou janvier.
- Nouvel art. 9 : la commission régionale informe les candidats « au moins un mois avant le début
  de l'année scolaire ».
- Art. 2 : abroge l'art. 2 du décret n° 72-229, c'est-à-dire l'annexe de 1972.

**Arrêté du ministre de l'Éducation nationale du 12 août 1974** fixant les critères d'attribution
des bourses aux élèves de l'enseignement secondaire. **Effet au 1er juillet 1974 (art. 2).**
Annexe, 1re partie (bourse nouvelle), lue à l'image (p. 1822-1823) :
- moyenne : jusqu'à 10,99 → 10 points, à condition de passer dans la classe supérieure ; 11 à
  12,99 → 14 ; 13 à 13,99 → 16 ; 14 et plus → 20 ;
- conduite et assiduité : 0 à 5 ; condition familiale : 0 à 5 (commission régionale) ;
- frères et sœurs de moins de 20 ans et sans profession : 1 → 1 ; 2 → 2 ; 3 → 3 ; 4 → 4 ; 5 et
  plus → 5 ;
- orientation d'office : comme en 1972 ;
- **revenu annuel de la famille, après déductions : jusqu'à 200 D → 15 ; 201-300 → 10 ;
  301-400 → 7 ; 401-500 → 5 ; 501-600 → 3 ; plus de 600 D → 0** ;
- **fraction : 45-55 → 1 ; 40-44 → 3/4 ; 30-39 → 1/2.**

2e et 3e parties (augmentation, redoublement) : lues en OCR, même économie qu'en 1972 ; la décision
du conseil des professeurs sur le redoublant est « définitive ». 4e partie (concours d'entrée) : le
barème de la moyenne (10 / 14 / 16 / 20) est lu en OCR ; les critères 3 (frères et sœurs) et 4
(affectation) ne sont que des fragments d'OCR, à lire à l'image (p. 1823-1824).

### 1.5 Loi n° 76-115 du 31 décembre 1976, loi de finances pour 1977, art. 15 — lu

JORT n° 83 du 31 décembre 1976, p. 3164 (FR ; `1976/fr/Jo08376.pdf`, page 4 du fichier).
Recid 115846. Chapitre deuxième, « mesures spéciales destinées à améliorer le recouvrement et le
contrôle fiscal ». Rubrique : « Obligation de restituer des bourses scolaires et universitaires
indûment perçues majorées d'une pénalité ». Lu à l'image :

> Art. 15. — Les contribuables autres que ceux disposant exclusivement de revenu sous forme de
> salaires ou pensions qui demandent une attestation fiscale pour l'octroi à leurs enfants d'une
> bourse scolaire ou universitaire doivent souscrire un engagement avec leur signature légalisée,
> entraînant pour eux en cas de redressement les situant au-dessus des seuils d'éligibilité à la
> bourse, la restitution des sommes indûment perçues par leurs enfants majorées d'une pénalité de
> 10 % par an.

Portée : la condition de ressources des bourses se prouve par une attestation fiscale ; un
redressement qui fait passer la famille au-dessus des « seuils d'éligibilité » oblige à restituer
les sommes, majorées de 10 % par an. Date d'effet : l'article n'en énonce pas. La clause générale
de la loi est à lire.

### 1.6 La loi de 1991 : le fondement de l'aide — lu (OCR)

Loi n° 91-65 du 29 juillet 1991 relative au système éducatif, JORT n° 55 de 1991, p. 1398-1400
(FR ; `1991/fr/Jo05591.pdf`, pages 10 à 12 du fichier ; pages imprimées lues dans l'en-tête de
l'OCR). Recid 113404.
- **Art. 4, 2e alinéa** (p. 1399) : « L'Etat apporte, autant que possible, son aide aux élèves
  issus de familles économiquement modestes et qui excellent dans leurs études grâce aux efforts
  qu'ils fournissent ou aux aptitudes et potentialités dont ils font preuve. » C'est ce que la loi
  dit chercher : une aide sous double condition, de ressources et de mérite. Le 1er alinéa garantit
  « gratuitement » le droit à la formation scolaire.
- Art. 24 : voir § 4.1.
- Texte de l'OCR non relu à l'image ; aucune valeur chiffrée n'y est reprise.

### 1.7 Après 1974

- **Aucun texte publié ne fixe, après l'arrêté du 12 août 1974, de nouveaux critères ni de
  montant des bourses scolaires du secondaire** (fiche `r-bourses-scolaires-apres-1974`).
- **Décret gouvernemental n° 2016-664 du 25 mai 2016, art. 2** (§ 2.1) : l'office est chargé
  d'« étudier les dossiers des bourses scolaires et les attribuer aux bénéficiaires selon les
  critères qui seront fixés par décision du ministre de l'éducation ». La sous-direction des
  activités culturelles, sportives et sociales comprend un « service des actions sociales et des
  bourses scolaires » (art. 9). Cette décision n'est pas identifiée et n'est peut-être pas publiée
  au *Journal officiel* (fiche `r-bourses-scolaires-decision-ministre`).
- **Budgets du ministère** (§ 5.1) : ligne « transferts (bourses scolaires et bourses de
  formation) » de 7,394 MD reconduite de 2013 à 2016 ; transfert des crédits des bourses scolaires
  à l'office en 2017.
- **Montant de la bourse.** Aucun texte de 1966 à 1974 ne fixe de montant en dinars : la bourse est
  une fraction (1/4 jusqu'en 1972, puis 1/2, 3/4, complète) des frais de pension ou de
  demi-pension. Le montant dépend donc des tarifs de pension. Les textes de tarif identifiés à
  l'index ne sont pas lus (§ 7).

---

## 2. La restauration scolaire : cantines et internats

### 2.1 Décret gouvernemental n° 2016-664 du 25 mai 2016 — lu

*Portant création de l'office des œuvres scolaires et fixant son organisation administrative et
financière et les modalités de son fonctionnement.* JORT n° 47 du 10 juin 2016, FR p. 1836-1841
(`2016/fr/Jo0472016.pdf`, couche de texte). Recid 78008 (intitulé arabe à l'index : « يتعلق بإحداث
ديوان الخدمات المدرسية وبضبط تنظيمه الإداري والمالي وطرق تسييره »). Pagination arabe à relever
(fascicule `Ja0472016.pdf`, page 12 du fichier).

**Le nom de l'office.** L'édition française dit « office des œuvres scolaires », l'arabe
« ديوان الخدمات المدرسية » (office des services scolaires). L'arrêté du 10 février 2022 (FR, index)
écrit « office des services scolaires ». C'est l'arabe qui fait foi (loi n° 93-64, art. 1er) : le
nom à retenir est **office des services scolaires**.

- **Art. 1** : établissement public à caractère administratif sous tutelle du ministère de
  l'Éducation, budget rattaché pour ordre au budget de l'État.
- **Art. 2 (mission)** : « veiller au fonctionnement des cantines et des foyers scolaires, de les
  soutenir ainsi que d'améliorer les conditions d'hébergement aux foyers ». « Relèvent de l'office
  **dès le 31 décembre 2016**, tous les foyers et les cantines scolaires relevant actuellement des
  établissements éducatifs publics. » L'office soutient aussi le transport scolaire et la vie
  scolaire. Il est chargé notamment d'étudier l'extension du réseau des écoles primaires
  bénéficiant des cantines, d'assurer la restauration et l'hébergement des internats scolaires, et
  d'attribuer les bourses scolaires (§ 1.7).
- **Art. 8, ce que le texte dit chercher** : la direction de l'hébergement et des cantines
  scolaires doit « renforcer et conserver le réseau des cantines scolaires principalement dans les
  écoles primaires dont les résultats enregistrés sont inférieurs à la moyenne nationale, et ce
  afin, d'y améliorer les conditions d'étude, d'aider les élèves à y poursuivre leurs études et
  d'éviter l'abandon scolaire, en leur fournissant un repas scolaire équilibré et sain ».
- Art. 3, 11-13 : une « unité des œuvres scolaires » par délégation comprenant un ou plusieurs
  foyers ; chefs de bureau payés d'une indemnité mensuelle de 80 dinars (art. 13).
- **Art. 18 (ressources)** : subventions de l'État au budget du ministère, « recettes provenant des
  contributions des élèves en contrepartie des services rendus par l'office », autres subventions.
  Le texte qui fixe ces contributions n'est pas identifié (fiche `r-oss-contributions-eleves`).
- **Art. 21** : les agents des foyers et cantines sont mutés à l'office le 31 décembre 2016.
- **Date d'effet** : pas de clause générale ; date de dépôt non relevée. Le transfert des foyers,
  des cantines et des agents est daté par le texte : 31 décembre 2016.

### 2.2 Avant 2016 : ce qui est connu

- **Aucun texte d'organisation des cantines des écoles primaires n'est identifié avant 2016**
  (fiche `r-cantines-scolaires-avant-2016`). Les cantines relevaient « des établissements éducatifs
  publics » (décret n° 2016-664, art. 2).
- **Internats.** Les collèges, lycées et internats sont des établissements publics : ils sont créés
  et supprimés par les lois de finances. L'index en donne des exemples : loi n° 73-82, LF 1974,
  création de collèges (recid 116458) ; décret n° 83-1253, changement d'appellation des « collèges,
  lycées et internats » (recid 96654) ; loi n° 86-106, LF 1987, art. 84-85, suppression de
  l'internat primaire de Hajeb Layoun (recid 114321) ; loi n° 89-115, LF 1990, art. 63-65,
  suppression de l'internat primaire de l'Ariana (recid 113698). Tous sont à l'index seulement.
  Deux internats primaires (Menaqaa à Zaghouan, Mateur) figurent encore, comme établissements
  publics du ministère de l'Éducation, à l'annexe des lois de finances de 2017 à 2020 (lu, § 5.2).
- **Tarifs de pension.** Ils fondent le montant de la bourse (§ 1.7). Textes à l'index, non lus :
  arrêté du ministre de l'Éducation nationale du 15 janvier 1957 « relatif aux rétributions
  scolaires et au prix de pension des commensaux dans les établissements d'enseignement public »
  (JORT 1957/7, p. 87-88, recid 75676) ; loi n° 58-45 du 31 mars 1958, budget 1958-59, art. 38 à 40,
  « tarifs des pensions dans les établissements d'enseignement à personnalité civile » (JORT 1958/25,
  recid 118331) ; décret n° 60-260 du 19 juillet 1960 sur les remises de principe (JORT 1960/35,
  p. 993, recid 106888), abrogé en 1971. Aucun texte postérieur sur le prix de pension dans les
  établissements du ministère de l'Éducation n'est identifié.
- **Coopération.** Loi organique n° 2020-9 du 25 février 2020 et décret présidentiel n° 2020-18 du
  même jour : approbation et ratification d'un protocole d'accord du 30 mars 2019 avec l'Italie
  « concernant le programme d'amélioration des infrastructures et des services scolaires dans le
  cycle primaire » (JORT n° 19 de 2020, p. 643 et 645). Lu : article unique de la loi organique. Le
  protocole n'est pas reproduit au fascicule.
- **Arrêté conjoint du 10 février 2022** (ministres de l'Éducation et des Finances), fixant les
  montants d'exploitation des complexes sportifs, culturels et de loisirs scolaires relevant de
  l'office (JORT 2022/17, p. 508, recid 164751) : index ; hors restauration, à lire seulement si le
  chapitre traite de l'office en entier.

### 2.3 Loi n° 2009-32 du 23 juin 2009 — lu (par renvoi à la fiscalité)

*Relative à l'octroi d'avantages fiscaux aux prestations de restauration au profit des élèves et
des apprenants dans les centres de formation professionnelle de base.* JORT n° 51 du 26 juin 2009,
FR p. 1660, AR p. 2180. Clé existante : `loi-2009-32-restauration-formation`. Travaux
préparatoires : Chambre des députés, 9 juin 2009 ; Chambre des conseillers, 18 juin 2009.
- **Art. 1** : étend aux revenus des prestations de restauration des élèves et des apprenants des
  centres de formation professionnelle de base, « selon les mêmes conditions », les § III, III bis et
  III ter de l'art. 39 du code de l'IRPP et de l'IS : déduction des revenus et des revenus réinvestis
  dans ces projets.
- **Art. 2** : même extension, pour l'IS, aux § VII bis et VII octies de l'art. 48.
- **Art. 3** : nouveau n° 30 bis du tableau A du code de la TVA : « Les prestations de restauration
  rendues au profit des étudiants, des élèves et des apprenants dans les centres de formation
  professionnelle de base, et ce, conformément à un cahier des charges établi par le ministère
  chargé de la tutelle du secteur ». Le cahier des charges n'est pas identifié (fiche
  `r-cahier-charges-restauration-eleves`).
- Le chapitre 5 en dit une ligne et renvoie à la fiscalité (`_tva_tableaux.qmd`, n° 30 bis, créé
  pour les étudiants par l'art. 58 de la LF 1998).
- Date d'effet : pas de clause propre ; date de dépôt non relevée.

---

## 3. L'aide de rentrée avant l'Amen social

**Ce que le précis dit déjà.** `prestations_sociales/_non_contributives.qmd`, `@sec-nc-aides` et
`@tbl-nc-rentree-scolaire`, couvre l'aide de rentrée de l'Amen social depuis l'arrêté conjoint du
19 mai 2020 : 50 D par enfant, puis 100 D à compter du 1er septembre 2024 ; abonnements de
transport scolaire depuis l'arrêté du 8 décembre 2022 ; crédits de 2021 à 2023. Il ne dit rien
d'une aide antérieure à 2020, ni dans ce chapitre ni dans `docs/notes/prestations-assistance.md`.
Rien n'est à dupliquer.

**Ce qui est trouvé ici :**
- **Aucun texte publié instituant une aide de rentrée scolaire avant le 19 mai 2020 n'est
  identifié** (fiche `r-aide-rentree-avant-2020`). Aucun intitulé de l'index ne contient
  « rentrée scolaire » ni « العودة المدرسية » ; les seuls fichiers du miroir iort qui contiennent
  « العودة المدرسية » sont des textes d'organisation (décrets n° 2008-3171 et 2013-3749).
- **Une ligne budgétaire « aides scolaires » existe au budget du ministère de l'Éducation**
  (budgétaire, projets de budget ; § 5.1) : « إعانات مدرسية » 1,020 MD en 2013, 2014 et 2015 ;
  « إعانات مدرسية وتدخلات اجتماعية أخرى » 2,002 MD en 2016 et 2,252 MD en 2017. Rien ne dit qu'il
  s'agit d'une aide de rentrée : le libellé dit seulement « aides scolaires ».
- La question Q3 du plan reste ouverte. Une réponse viendra des documents du programme national
  d'aide aux familles nécessiteuses ou du ministère, hors *Journal officiel*.

---

## 4. Les frais à la charge des familles dans le public

### 4.1 Le fondement : loi n° 91-65, art. 24 — lu (OCR)

JORT n° 55 de 1991, p. 1400. Les ressources des écoles préparatoires, lycées et lycées pilotes
comprennent, entre autres, « des recettes provenant des droits d'inscription pouvant être mis à la
charge des élèves dont les revenus des parents les rendent à même de les payer, ainsi que des
droits d'assurance et de bibliothèque. Les modalités d'application du présent article sont fixées
par décret. » La gratuité de l'art. 4 et les droits de l'art. 24 coexistent. La loi d'orientation
n° 2002-80, qui garantit « le droit à l'enseignement gratuit dans les établissements scolaires
publics », est visée par le décret de 2010 ; son article sur les droits reste à lire.

### 4.2 La chaîne des décrets

| Date d'effet | Texte | JORT | Primaire | Collèges (écoles préparatoires), lycées, lycées pilotes | État |
|---|---|---|---|---|---|
| septembre 1992 (art. 3) | décret n° 92-1185 du 22 juin 1992, art. 1-3 | n° 41 du 26 juin 1992, p. 816 (FR) | — | droits d'inscription, d'assurance et de bibliothèque : **2,500 D** ; exonération si les revenus cumulés du père et de la mère ne dépassent pas le SMIG (art. 2) | lu à l'image |
| septembre 1997 (art. 2) | décret n° 97-1355 du 21 juillet 1997, art. 1 | n° 60 du 29 juillet 1997, p. 1345 (FR) | — | **5 D** (art. 1 nouveau du décret de 1992) | lu (couche de texte) |
| exécutoire cinq jours après le dépôt (loi n° 93-64, art. 2) ; publication le 13 août 2010 ; date de dépôt non relevée | décret n° 2010-1928 du 6 août 2010, art. 1-5 | n° 65 du 13 août 2010, p. 2247 (FR) | droits d'inscription : **2 D** | **5 D** ; payables à l'inscription (art. 2) ; exonération sous le SMIG des revenus cumulés des deux parents (art. 3) ; droits du primaire versés au commissariat régional (art. 4) ; abroge le décret de 1992 (art. 5) | lu (couche de texte) |
| année scolaire 2019-2020 (art. 2) | décret gouvernemental n° 2019-898 du 16 octobre 2019, art. 1-2 | n° 85 du 22 octobre 2019, AR p. 3620-3621 | **4 D** | **8,600 D** (collèges « de tous types », lycées, lycées pilotes) ; la répartition des droits d'inscription, d'assurance et de bibliothèque est fixée par arrêté conjoint Éducation-Finances | lu à l'image (AR) |

- Le décret de 2019 ne remplace que l'art. 1 du décret de 2010 : l'**exonération sous le SMIG
  (art. 3 de 2010) demeure**. Le texte dit « salaire minimum industriel garanti » ; entrée
  existante du glossaire : `smig`.
- Le décret de 2019 prend effet pour l'année scolaire 2019-2020, alors qu'il est publié le
  22 octobre 2019. L'édition française du JORT n° 85 de 2019 n'est pas dans le corpus local.
- Le décret de 1992 se fonde sur l'art. 24 de la loi n° 91-65 (visa) ; celui de 2010 sur la loi
  d'orientation n° 2002-80 modifiée en 2008 et sur la loi n° 2010-14 relative aux commissariats
  régionaux.
- Le droit d'assurance n'est pas isolé dans ces décrets : c'est une part d'un droit unique. Le
  régime de l'assurance scolaire (garanties, assureur) n'est pas identifié (fiche
  `r-assurance-scolaire-regime`), ni l'arrêté conjoint de répartition de 2019 (fiche
  `r-droits-inscription-repartition`).
- Aucun texte postérieur à 2019 n'est identifié à l'index (titres FR et AR) au 2 octobre 2026.

### 4.3 Textes voisins (pour mémoire)

- Décret n° 92-1186 du 22 juin 1992 (même fascicule, p. 816, lu à l'image) : il exonère de l'amende
  de l'art. 32 de la loi n° 91-65 le tuteur qui n'inscrit pas son enfant si l'établissement le plus
  proche est à plus de 2 km (école primaire), 3 km (école préparatoire sans internat) ou 20 km
  (école pourvue d'internat). L'art. 32 de la loi n° 91-65 fixe l'amende de 10 à 100 dinars,
  200 dinars en récidive (OCR, à relire à l'image).
- Droits de l'École internationale de Tunis : décret n° 99-2025 du 13 septembre 1999 (JORT 1999/77)
  et décret gouvernemental n° 2018-787 du 21 septembre 2018, « frais d'inscription, de scolarité et
  de demi-pension » (JORT 2018/77, p. 3208-3209) : index. Régime particulier, hors du droit commun.
- Indemnité « des coûts des fournitures scolaires » (décrets n° 2007-2308, 2007-2309 et suivants,
  jusqu'en 2025) : c'est une indemnité **des enseignants**, pas une aide aux familles. Elle va aux
  rémunérations publiques.

---

## 5. Séries

### 5.1 Budgétaire : crédits d'intervention du ministère de l'Éducation (projets de budget)

Source : budgets du ministère de l'Éducation présentés par le ministère des Finances, rangés dans
`tunisia-data` (`data/raw/minfinances/portail_ancien/budgets_ministeres/`). Famille : budgétaire,
**prévisions du projet de budget, non exécution**. MD = millions de dinars. Pages imprimées.

| Année | Transferts (bourses scolaires et bourses de formation) | Cantines scolaires des écoles primaires | Aides scolaires (puis « et autres interventions sociales ») | Total des interventions | Source, page |
|---|---:|---:|---:|---:|---|
| 2013 | 7,394 (dont établissements 7,220) | 14,560 | 1,020 | 35,285 | `2013_budget_education_jd40.pdf`, p. 29 |
| 2014 | 7,394 | 24,000 | 1,020 | 44,725 | `2014_budget_leducation_jd646.pdf`, p. 32 |
| 2015 | 7,394 | 24,000 | 1,020 | 44,725 | `2015_budget_leducation_ar_jd795.pdf`, p. 31 |
| 2016 | 7,394 | 24,000 | 2,002 | 44,725 | `2016_budget_leducation_ar_jd1042.pdf`, p. 30 |
| 2017 | 0,872 ; subvention à l'office : 0,550 | 24,000 | 2,252 | 38,753 | `2017_budget_leducation_ar_jd1172.pdf`, p. 30 et 39 |

- Les montants identiques d'une année à l'autre sont des **crédits reconduits** ; ils ne mesurent
  pas une dépense constatée.
- 2014 : la hausse de 9,440 MD (+26,8 %) des interventions est affectée aux cantines des écoles
  primaires (p. 32) ; celle du programme « primaire », +9,923 MD (+58,4 %), « au soutien des
  dépenses d'alimentation des cantines scolaires » (p. 43).
- 2017 : la baisse de 5,972 MD des interventions vient « essentiellement du transfert des crédits
  des bourses scolaires inscrits aux budgets des commissariats régionaux de l'éducation à l'office
  des services scolaires » (p. 30) ; programme 2 (préparatoire et secondaire) : −7,216 MD,
  −95,8 %, même motif (p. 39).
- Les effectifs donnés aux mêmes pages (4 562 écoles primaires et environ 1 076 000 élèves en
  2014-2015 ; 4 585 écoles et environ 1 093 600 élèves en 2016-2017) sont les **effectifs totaux**
  du primaire, **pas des bénéficiaires de cantines**.
- Le programme annuel de performance de 2014 (`2014_budget_leducation_programme_annuelle_performance_jd647.pdf`,
  p. 43) définit l'indicateur « part des écoles primaires dotées de cantines aménagées », rapportée
  aux écoles qui servent des repas. Seule la fiche de définition est lue ; les valeurs sont à
  chercher.
- <!-- TODO (documentaliste) : pages du fichier = p. imprimée + 6 pour 2013 (29 → 35), + 5 pour
  2014 (32 → 37, 43 → 48), 2015 (31 → 36), 2016 (30 → 35) et 2017 (30 → 35, 39 → 44). -->

### 5.2 Budgétaire : budget prévisionnel de l'office des services scolaires (annexe des lois de finances)

Tableau des budgets des établissements publics du ministère de l'Éducation, en dinars, colonnes
« subvention de l'État », « ressources propres », « total des ressources », « dépenses ». Lu à
l'image dans l'édition arabe.

| Loi de finances | JORT, page (AR) | Subvention de l'État | Ressources propres | Total = dépenses |
|---|---|---:|---:|---:|
| 2017 (loi n° 2016-78) | n° 105 du 27 décembre 2016, p. 4283 | 36 550 000 | 5 616 000 | 42 166 000 |
| 2018 (loi n° 2017-66) | n° 101 du 19 décembre 2017, p. 4412 | non établi | non établi | non établi |
| 2019 (loi n° 2018-56) | n° 104 du 28 décembre 2018, p. 5616 | 71 973 000 | 5 600 000 | 77 573 000 |
| 2020 (loi n° 2019-78) | n° 104 du 27 décembre 2019, p. 4783 | 69 981 000 | 5 600 000 | 75 581 000 |

- **2018 : lignes décalées dans le tableau officiel.** Sur la ligne de l'office on lit
  22 000 / 1 000 / 23 000 D, et les montants de l'ordre de ceux de l'office (36 791 000 / 5 600 000 /
  42 391 000) sont sur la ligne de l'internat primaire de Menaqaa (Zaghouan). La valeur de l'office
  pour 2018 n'est pas établie ici. Le miroir iort reproduit le même décalage.
- Les « ressources propres » sont, d'après l'art. 18 du décret n° 2016-664, alimentées notamment par
  les contributions des élèves : rien, dans le tableau, ne les détaille.
- **2021 à 2026 : à lire.** La recherche de « الخدمات المدرسية » dans le texte extrait des
  fascicules arabes des lois de finances pour 2021 à 2026 (JORT 2020/128, 2021/119, 2022/141,
  2023/144, 2024/149, 2025/148) ne trouve rien ; l'annexe a pu changer de forme, ou l'extraction
  échouer. Cela ne prouve pas que la ligne soit absente.

### 5.3 Bénéficiaires

- Boursiers du secondaire, élèves demi-pensionnaires et internes, bénéficiaires des cantines du
  primaire : **aucune série publiée lue ici**. À chercher dans les statistiques scolaires du
  ministère de l'Éducation (titres à vérifier) et dans les rapports d'activité de l'office (non
  identifiés).
- Rapports extérieurs (PAM), **titres et chiffres non vérifiés** (pages non ouvertes) : une
  recherche web renvoie à des notes de pays et à des rapports annuels du Programme alimentaire
  mondial sur le « National School Feeding Programme » (par exemple *Annual Country Report 2019:
  Tunisia. Country Strategic Plan 2018-2022*, notice https://wfp.tind.io/record/127999, qui a
  répondu 403). Un extrait de recherche prête au programme 260 000 enfants dans 2 500 écoles
  primaires, à une date non précisée. **Ce chiffre n'est pas utilisable en l'état** : il reste à
  récupérer le PDF, à relever page et méthode, et à le classer comme rapport extérieur.

---

## 6. Références candidates (CSL-JSON)

Déjà présentes : `loi-2009-32-restauration-formation` (fiscalité) ; `smig` est une entrée du
glossaire, pas une référence. Présentes dans un autre livre, à vérifier avant création :
`loi93-64`.

À créer (URL pist.tn dérivées de la convention, à vérifier par `verifier_urls_jort.py` ; le
certificat de pist.tn est échu) :

```json
[
  {"id": "arrete-1966-10-03-bourses-scolaires", "type": "legislation",
   "title": "Arrêté du secrétaire d'État à l'Éducation nationale du 3 octobre 1966, relatif au règlement des bourses scolaires pour les enseignements du second et du premier degré",
   "container-title": "Journal officiel de la République tunisienne", "issue": "43", "page": "1449-1451",
   "issued": {"date-parts": [[1966, 10, 3]]}, "URL": "https://www.pist.tn/jort/1966/1966F/Jo04366.pdf"},
  {"id": "decret-71-356-bourses-scolaires", "type": "legislation",
   "title": "Décret n° 71-356 du 28 septembre 1971, fixant l'organisation et les conditions d'attribution des bourses scolaires pour les élèves de l'enseignement secondaire",
   "container-title": "Journal officiel de la République tunisienne", "issue": "43", "page": "1307-1320",
   "issued": {"date-parts": [[1971, 9, 28]]}, "URL": "https://www.pist.tn/jort/1971/1971F/Jo04371.pdf"},
  {"id": "decret-72-229-bourses-scolaires", "type": "legislation",
   "title": "Décret n° 72-229 du 5 juillet 1972, modifiant le décret n° 71-356 du 28 septembre 1971",
   "container-title": "Journal officiel de la République tunisienne", "issue": "28", "page": "966-969",
   "issued": {"date-parts": [[1972, 7, 5]]}, "URL": "https://www.pist.tn/jort/1972/1972F/Jo02872.pdf"},
  {"id": "decret-74-783-bourses-scolaires", "type": "legislation",
   "title": "Décret n° 74-783 du 5 août 1974, portant modification du décret n° 71-356 du 28 septembre 1971",
   "container-title": "Journal officiel de la République tunisienne", "issue": "52", "page": "1822",
   "issued": {"date-parts": [[1974, 8, 5]]}, "URL": "https://www.pist.tn/jort/1974/1974F/Jo05274.pdf"},
  {"id": "arrete-1974-08-12-criteres-bourses", "type": "legislation",
   "title": "Arrêté du ministre de l'Éducation nationale du 12 août 1974, fixant les critères d'attribution des bourses aux élèves de l'enseignement secondaire",
   "container-title": "Journal officiel de la République tunisienne", "issue": "52", "page": "1822-1824",
   "issued": {"date-parts": [[1974, 8, 12]]}, "URL": "https://www.pist.tn/jort/1974/1974F/Jo05274.pdf"},
  {"id": "loi-76-115-lf-1977", "type": "legislation",
   "title": "Loi n° 76-115 du 31 décembre 1976, portant loi de finances pour la gestion 1977",
   "container-title": "Journal officiel de la République tunisienne", "issue": "83", "page": "3164",
   "issued": {"date-parts": [[1976, 12, 31]]}, "URL": "https://www.pist.tn/jort/1976/1976F/Jo08376.pdf"},
  {"id": "loi-91-65-systeme-educatif", "type": "legislation",
   "title": "Loi n° 91-65 du 29 juillet 1991, relative au système éducatif",
   "container-title": "Journal officiel de la République tunisienne", "issue": "55", "page": "1398-1400",
   "issued": {"date-parts": [[1991, 7, 29]]}, "URL": "https://www.pist.tn/jort/1991/1991F/Jo05591.pdf"},
  {"id": "decret-92-1185-droits-inscription", "type": "legislation",
   "title": "Décret n° 92-1185 du 22 juin 1992, relatif à la fixation des droits d'inscription, d'assurance et de bibliothèque concernant les élèves des écoles préparatoires, des lycées secondaires et des lycées pilotes",
   "container-title": "Journal officiel de la République tunisienne", "issue": "41", "page": "816",
   "issued": {"date-parts": [[1992, 6, 22]]}, "URL": "https://www.pist.tn/jort/1992/1992F/Jo04192.pdf"},
  {"id": "decret-97-1355-droits-inscription", "type": "legislation",
   "title": "Décret n° 97-1355 du 21 juillet 1997, portant modification du décret n° 92-1185 du 22 juin 1992",
   "container-title": "Journal officiel de la République tunisienne", "issue": "60", "page": "1345",
   "issued": {"date-parts": [[1997, 7, 21]]}, "URL": "https://www.pist.tn/jort/1997/1997F/Jo06097.pdf"},
  {"id": "decret-2010-1928-droits-inscription", "type": "legislation",
   "title": "Décret n° 2010-1928 du 6 août 2010, relatif à la fixation des droits d'inscription aux écoles primaires et des droits d'inscription, d'assurance et de bibliothèque aux écoles préparatoires, aux lycées et aux lycées pilotes",
   "container-title": "Journal officiel de la République tunisienne", "issue": "65", "page": "2247",
   "issued": {"date-parts": [[2010, 8, 6]]}, "URL": "https://www.pist.tn/jort/2010/2010F/Jo0652010.pdf"},
  {"id": "decret-gouv-2019-898-droits-inscription", "type": "legislation",
   "title": "Décret gouvernemental n° 2019-898 du 16 octobre 2019, portant modification du décret n° 2010-1928 du 6 août 2010",
   "container-title": "Journal officiel de la République tunisienne", "issue": "85", "page": "3620-3621",
   "issued": {"date-parts": [[2019, 10, 16]]}, "URL": "https://www.pist.tn/jort/2019/2019A/Ja0852019.pdf",
   "note": "Pagination et URL de l'édition arabe ; édition française absente du corpus local, URL FR à vérifier."},
  {"id": "decret-gouv-2016-664-office-services-scolaires", "type": "legislation",
   "title": "Décret gouvernemental n° 2016-664 du 25 mai 2016, portant création de l'office des services scolaires et fixant son organisation administrative et financière et les modalités de son fonctionnement",
   "container-title": "Journal officiel de la République tunisienne", "issue": "47", "page": "1836-1841",
   "issued": {"date-parts": [[2016, 5, 25]]}, "URL": "https://www.pist.tn/jort/2016/2016F/Jo0472016.pdf",
   "note": "L'édition française écrit « office des œuvres scolaires » ; l'arabe, qui fait foi, « ديوان الخدمات المدرسية »."}
]
```

Les lois de finances pour 2017 à 2020 ont sans doute déjà leurs clés dans la fiscalité : le
bibliographe le vérifie avant toute création. Les budgets du ministère de l'Éducation (2013-2017) ne
sont pas encore dans `references.json` : à créer par le bibliographe (type `report`, auteur
ministère des Finances / ministère de l'Éducation, titre arabe exact à relever en couverture).

---

## 7. Lacunes, classées

**Lisible dans le corpus (texte ou image, non lu ici)**
- Loi n° 76-115 : article final ou clause d'effet de la loi (JORT 1976/83).
- Décret n° 72-229, 4e partie, tableau des fractions (p. 969) ; arrêté du 12 août 1974, 4e partie,
  critères 3 et 4 (p. 1823-1824) : à relire à l'image.
- Loi n° 91-65 : art. 4, 24 et 32 à relire à l'image (amende de l'art. 32 notamment).
- Loi d'orientation n° 2002-80 : article sur les droits d'inscription, s'il y en a un (fascicule
  2002/062, police décalée).
- Décret n° 2016-664 : pagination arabe (`Ja0472016.pdf`).
- Arrêté conjoint du 10 février 2022 (JORT 2022/17, p. 508).
- Lois de finances pour 2021 à 2026 : annexe des établissements publics (ligne de l'office), à lire
  à l'image.
- Programme annuel de performance 2014 : valeurs de l'indicateur des cantines aménagées.

**OCR nécessaire (fascicule sans couche de texte)**
- Arrêté du 15 janvier 1957 (JORT 1957/7) et loi n° 58-45, art. 38 à 40 (JORT 1958/25) : prix de
  pension.
- Décret n° 60-260 du 19 juillet 1960, remises de principe (JORT 1960/35, p. 993).
- Textes des lois de finances qui créent et suppriment les internats (LF 1974, 1987, 1990), si le
  chapitre retrace le réseau.

**À obtenir (hors JORT ou non identifié)**
- Décision du ministre fixant les critères des bourses scolaires (décret n° 2016-664, art. 2).
- Texte fixant les contributions des élèves aux services de l'office (art. 18).
- Arrêté conjoint de répartition des droits de 2019 (décret n° 2019-898, art. 1, 2e al.).
- Cahier des charges de la restauration des élèves (loi n° 2009-32, art. 3).
- Régime de l'assurance scolaire.
- Aide de rentrée avant 2020 (PNAFN, ministère).
- Séries : boursiers, internes et demi-pensionnaires, bénéficiaires des cantines (statistiques du
  ministère, rapports de l'office) ; exécution budgétaire (lois de règlement).
- Rapports du PAM sur le programme national d'alimentation scolaire : PDF à récupérer, à ranger
  dans `tunisia-data`, méthode à relever.

---

## 8. Notions à glossaire

Aucune de ces notions n'est dans `precis/glossaire.yml` (contrôlé le 17 octobre 2026), sauf
`smig`, qui existe.

| Terme FR | Terme AR pressenti | Source canonique pressentie |
|---|---|---|
| Bourse scolaire | منحة مدرسية (« المنح المدرسية » au décret n° 2016-664, AR) | arrêté du 3 octobre 1966, art. 3 ; décret n° 71-356, art. 3 |
| Fraction de bourse (quart, demi, trois quarts, bourse complète) | — (à relever dans l'édition arabe de 1971 ou 1974) | décret n° 71-356, annexe ; arrêté du 12 août 1974 |
| Pension, demi-pension (frais de) | نصف الإقامة (à vérifier) | arrêté de 1966, art. 3 |
| Cantine scolaire | المطعم المدرسي / المطاعم المدرسية | décret n° 2016-664, art. 2 et 8 |
| Foyer scolaire, internat | المبيت (المبيتات المدرسية) | décret n° 2016-664, art. 2 |
| Office des services scolaires | ديوان الخدمات المدرسية | décret n° 2016-664, art. 1 (titre arabe) |
| Droits d'inscription, d'assurance et de bibliothèque | رسوم التسجيل والتأمين والمكتبة | décret n° 92-1185, art. 1 ; décret n° 2019-898 |
| Orientation d'office (critère de bourse) | — | décret n° 72-229, annexe |
| Commission régionale des bourses scolaires | — | décret n° 71-356, art. 9 |

---

## 9. Recherches infructueuses

Fiches proposées dans `docs/notes/education-recherches-B.yml`, à fusionner dans
`docs/recherches.yml` :

- `r-bourses-scolaires-apres-1974` — critères ou montants des bourses scolaires après le
  12 août 1974 ;
- `r-bourses-scolaires-decision-ministre` — décision ministérielle prévue par le décret
  n° 2016-664, art. 2 ;
- `r-cantines-scolaires-avant-2016` — organisation des cantines et des internats, et contribution
  des familles, avant 2016 ;
- `r-oss-contributions-eleves` — contributions des élèves aux services de l'office (art. 18) ;
- `r-aide-rentree-avant-2020` — aide de rentrée scolaire antérieure à l'Amen social ;
- `r-assurance-scolaire-regime` — régime de l'assurance scolaire ;
- `r-droits-inscription-repartition` — arrêté conjoint de répartition des droits (décret
  n° 2019-898, art. 1) ;
- `r-cahier-charges-restauration-eleves` — cahier des charges du n° 30 bis du tableau A de la TVA
  (loi n° 2009-32, art. 3).

Chaque passe consigne ce qui a été fait : requêtes SQL (FTS et LIKE) et LIKE arabes sur les
titres et objets de `jort_cache`, `grep` sur le miroir iort. **Le plein texte des fascicules n'a pas
été parcouru** : `scripts/recherches.py relancer`, lancé sur une copie de travail, n'a pas abouti
dans le temps imparti. Ce parcours est inscrit dans le champ `a_faire` de chaque fiche.

## Tarifs de pension et de demi-pension, 1966-2022 : lectures du 18 octobre 2026

Huit arrêtés lus à l'image (sauf 2022 : texte) : 24 juillet 1967 (effet 1er octobre 1966), 8 mars 1973, 12 janvier 1977, 14 février 1979, 27 décembre 1982 (effet 1er janvier 1983), 2 septembre 1987
(effet 14 septembre 1987), 28 mars 1988 (effet 14 septembre 1988), 10 février 2022. Le tableau du chapitre donne la demi-pension et la pension du 2e cycle et des internats primaires, au premier
trimestre. Valeurs non reprises au chapitre : tarifs des deuxième et quatrième trimestres (de 1977 à 1988), du 1er cycle, des classes primaires annexées et des collèges (1966-1983), des lycées pilotes (1988),
tarifs des commensaux par catégorie (surveillants, personnel ouvrier, élèves-maîtres) et tarifs d'hébergement du personnel de passage et des élèves (art. 6). Pages de l'index `jort_cache.db` exactes pour ces huit textes.
Dates : l'arrêté de 1982 est signé le 27 décembre 1982 et prend effet le 1er janvier 1983 ; celui de 1967 prend effet le 1er octobre 1966, soit près d'un an avant sa signature.

**Arrêté du 15 janvier 1957 — lecture du 18 octobre 2026.** Fascicule JORT n° 7 du 22 janvier 1957 absent du corpus local (le fichier `Jo10757.pdf` de l'index n'existe pas) :
récupéré sur pist.tn (`https://www.pist.tn/jort/1957/1957F/Jo10757.pdf`, 3,1 Mo) et lu à l'image, p. 87-88. Montants en francs. Les nombres du 2e cycle (13 050 ; 25 380) et des commensaux
(7 260 ; 4 020 ; 160 ; blanchissage 840) sont les mêmes que dans l'arrêté du 24 juillet 1967 en dinars (13,050 ; 25,380 ; 7,260 ; 4,020 ; 0,160 ; 0,840). Les internats primaires
passent de 7 560 / 16 380 à 8,280 / 18,000. Effet : 1er octobre 1956 (art. 9). L'arrêté abroge celui du 20 décembre 1952, modifié le 2 septembre 1953 et complété le 24 janvier 1956.

**Arrêté du 24 janvier 1956 — lecture du 18 octobre 2026.** JORT n° 8 du 27 janvier 1956, p. 116 (`Jo00856.pdf`, texte à l'image). Il complète l'arrêté du 20 décembre 1952, modifié le 2 septembre 1953, par un article 1 bis : les élèves nourris dans les mêmes conditions que les internes mais non logés faute de place sont inscrits comme internes, avec une remise de plein droit de 20 % sur le tarif d'internat (catégorie des « internes-externés ») ; effet au 1er octobre 1955. Les arrêtés du 20 décembre 1952 et du 2 septembre 1953 ne sont pas dans le corpus local ; l'index ne les contient pas.
