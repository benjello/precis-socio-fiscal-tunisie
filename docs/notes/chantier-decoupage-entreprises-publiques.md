# Le volume des entreprises publiques : une segmentation de premier niveau (27 octobre 2026)

Proposition à relire. Aucun fichier de `precis/` n'est touché. Elle répond à la demande du 27 octobre 2026
d'une segmentation de premier niveau plus fine que « un chapitre et une annexe », à affiner avec ce que
la passe sur les années récentes apporte et avec ce que quelques jours de travail peuvent encore obtenir.
Elle complète la section « V. Les institutions » de `docs/notes/chantier-decoupage-livres.md`.

## 1. Pourquoi scinder, et sur quel critère

- Le chapitre unique `_relation_financiere.qmd` compte 19 000 mots, l'annexe 4 400. Le seuil de 25 000 mots
  du § 4 de `docs/conventions-redaction.md` n'est pas atteint : **la scission ne se justifie pas par la
  taille, mais par les épines.** Le fichier porte au moins six épines chronologiques distinctes : le
  périmètre et la tutelle (1969-2019), le plafond de la garantie (1958-2026), les cessions (1987-2024),
  les recettes de l'État, les transferts, les effectifs. Le critère du § 4 dit : une épine par chapitre.
- La forme « volume ou chapitre », laissée à la revue dans le backlog, est tranchée dans les faits par la
  demande d'un découpage plus fin : c'est un volume. Un volume de sept à treize chapitres est cohérent avec
  la partie V (« institutions »).
- Un chapitre doit tenir seul : son épine, ses chiffres datés, sa longue période. Un sujet qui ne tient pas
  seul (moins de trois ans de série, un seul texte) est rattaché au chapitre voisin et sort quand il a
  de quoi tenir.

## 2. Le plan proposé

Six parties dans le livre, quatorze chapitres, une présentation et trois annexes. Types : cadre, dispositif,
institution, longue période du livre, rapports et études (§ 4 des conventions). Les noms de fichier sont
indicatifs.

| Partie | Chapitre | Type | Épine |
|---|---|---|---|
| (tête) | **Présentation** (`index.qmd`) | cadre | la carte des institutions (texte fondateur, date, où lire), la frise, ce que pèse l'ensemble, le voisinage (fait) |
| I. Le statut | 1. **Ce qu'est une entreprise publique** (`_statut.qmd`) | dispositif | définition et périmètre : 1969, 1985, 1989, 1994-2001, 2006 ; état du droit ; liste des établissements |
| | 2. **Le contrôle et la gouvernance** (`_gouvernance.qmd`) | dispositif | contrôle financier de 1948 et 1969, contrôleurs d'État, fautes de gestion de 1985-1988, rapport annuel de 2019, stratégie de 2015-2018, rémunération des dirigeants de 2014 |
| II. L'État et les entreprises | 3. **Les transferts du budget** (`_transferts.qmd`) | dispositif | subventions d'exploitation, dotations en capital, interventions ; régularisation de 2020 |
| | 4. **Les garanties, les prêts et les arriérés** (`_garanties.qmd`) | dispositif | plafond de la garantie 1958-2026 ; commission de 1993 ; loi organique de 2019 ; prêts du Trésor ; prêts rétrocédés ; encours ; dettes et créances croisées |
| | 5. **Ce que l'État reçoit** (`_recettes.qmd`) | dispositif | dividendes, excédents, profits de la Banque centrale, versements fiscaux ; règles de répartition des bénéfices |
| | 6. **Céder** (`_cessions.qmd`) | dispositif | 1987, 1989, action spécifique de 1994, liquidation de 1999, relevés 1987-2009, recettes budgétaires 2010-2024 |
| | 7. **Restructurer** (`_restructuration.qmd`) | dispositif | contrats-programmes de 1985, fonds de restructuration du capital, commission d'assainissement de 1997, banques publiques 2012-2015, contrats de performance de 2018 |
| III. Les entreprises | 8. **L'énergie** (STEG, STIR, ETAP) | institution | naissance, statut, comptes, dette, emploi, longue période |
| | 9. **Les mines et la chimie** (CPG, Groupe chimique) | institution | idem |
| | 10. **Les offices et les monopoles** (céréales, huile, commerce, tabacs, pharmacie centrale) | institution | idem |
| | 11. **Les transports** (Tunisair, SNCFT, Transtu, sociétés régionales, OACA) | institution | idem |
| | 12. **L'eau et les communications** (SONEDE, ONAS, Tunisie Télécom, Poste) | institution | idem |
| | 13. **Le secteur financier public** (banques, assurances) | institution | idem |
| IV. L'emploi et les comptes | 14. **L'emploi et la masse salariale**, puis **les résultats agrégés** | dispositif et chiffres | effectifs 2016-2023, charges de personnel, résultats par édition |
| V. La longue période | 15. **La relation financière, 1960-2024** | longue période du livre | budgétaire seul : transferts, garanties, recettes, cessions côte à côte par plan de développement |
| VI. Rapports et études | 16. **Le Livre blanc de 2018 et les études extérieures** | rapports et études | chacun avec sa méthode |
| Annexes | liste des entreprises 1997-2021 ; registre des textes ; glossaire | | |

Remarques sur le plan :

- **Les chapitres 8 à 13 ne s'ouvrent pas tous ensemble.** Tant que les fiches par entreprise du rapport
  annuel (dette, subvention d'exploitation, total des passifs) ne sont pas versées, ils n'ont pas de
  matière. Départ : une seule section « les dix entreprises les plus lourdes » dans le chapitre 14, déjà
  écrite (`#sec-ep-lp-entreprises`) ; un chapitre sectoriel s'ouvre quand trois entreprises du secteur ont
  leur fiche.
- **Le chapitre 2 est provisoire.** Aujourd'hui il tient en la section « Depuis 2011 » (1 200 mots) et en
  celle de 2019. Il reste au chapitre 1 tant qu'il n'a pas lu au moins la loi de 1985 sur les fautes de
  gestion, le décret de 2014 sur la rémunération des dirigeants et les textes de contrôle de 2002-2016.
- **Le chapitre 4 reçoit les dettes et créances croisées.** Elles ne couvrent que 2021-2023 et ne
  tiennent pas seules ; elles sont le bilan croisé des garanties, des prêts et des arriérés. Elles sortent
  si les décrets de compensation de créances et le règlement de 2020 fournissent une épine avant 2021.
- **Les chapitres 5 à 7 se partagent la section de clôture.** Les quatre flux des rapports de la Cour des
  comptes (versements, garanties, prêts, privatisation) vont chacun dans le chapitre de leur dispositif.
  Le chapitre 15 n'en garde qu'une figure et un tableau courts, jamais la prose recopiée (règle de
  domicile du § 4).
- **« Ce qu'en dit l'économie »** : une page au plus, dernière section des chapitres 3 et 4 (contrainte
  budgétaire molle, passifs éventuels), 6 (effets des privatisations), 7 (recapitalisation bancaire), 2
  (gouvernance). Couche tardive, hors du contenu minimal d'un chapitre.

## 3. Table de correspondance avec le chapitre actuel

Mots par section au 27 octobre 2026 (hors blocs de code).

| Section actuelle | Mots | Chapitre cible |
|---|---:|---|
| Vue d'ensemble `#sec-ep-vue-ensemble` | 1 070 | présentation, avec un renvoi par puce vers les chapitres 3 à 6 et 14 |
| Mise en place `#sec-ep-1969`, `#sec-ep-1985` | 340 | 1 |
| `#sec-ep-1987` | 144 | 6 (la définition reste en 1) |
| `#sec-ep-1989` | 269 | 1 pour le périmètre, 6 pour la cession |
| `#sec-ep-1994-2001` | 334 | 1 pour les banques et la liste, 6 pour l'action spécifique |
| `#sec-ep-reformes-cessions` | 63 | 6 |
| `#sec-ep-2019` | 171 | 2 |
| `#sec-ep-apres-2011` | 1 236 | 2, et 7 pour les contrats de performance |
| `#sec-ep-etat-du-droit` | 378 | 1 |
| `#sec-ep-transferts` | 1 044 | 3 |
| `#sec-ep-garanties`, `#sec-ep-garanties-plafond-legal` | 5 113 | 4 |
| `#sec-ep-croisees` | 982 | 4 |
| `#sec-ep-dividendes` et ses deux sous-sections | 1 155 | 5 |
| `#sec-ep-cessions`, `#sec-ep-lp-cessions` | 891 | 6 |
| `#sec-ep-effectifs` | 1 303 | 14 |
| `#sec-ep-lp-editions`, `#sec-ep-lp-resultats` | 829 | 14 |
| `#sec-ep-lp-entreprises` | 547 | 14, puis éclaté dans les chapitres 8 à 13 |
| `#sec-ep-lp-cloture` | 1 330 | éclaté : versements en 5, garanties et prêts en 4, privatisation en 6 ; figure d'ensemble en 15 |
| `#sec-ep-lp-lacunes`, `#sec-ep-longue-periode` | 337 | 15 |
| `#sec-ep-etudes` et ses cinq sous-sections | 987 | 16 |
| Registre des textes `#tbl-ep-registre` | tableau | partagé : chaque ligne suit la section qui la cite |
| Annexe de la liste | 4 410 | annexe, inchangée |

**Liens entrants à préserver** (relevés le 27 octobre 2026) :

- un seul lien externe vers une ancre : `remunerations_publiques/_regime_conventionnel.qmd` ligne 295 vers
  `#sec-ep-transferts` (le chapitre 3 reprend l'ancre) ;
- deux liens vers la page d'accueil du volume, depuis `prestations_sociales/_logement_social.qmd` (lignes 5
  et 509), inchangés ;
- dix ancres de fiches de `docs/recherches.yml` qui nomment le fichier `_relation_financiere.qmd` : à
  réécrire avec le nom du chapitre cible, à la scission ;
- les ancres `sec-ep-*` et `r-ep-*` sont toutes lues par `check_domicile_references.py` : elles survivent
  à la scission si le chapitre qui porte la ligne de registre porte aussi les liens qui y renvoient. Une
  ligne de registre cité depuis deux chapitres se cite par lien relatif entre chapitres ;
- les scripts qui nomment le livre par son dossier (`build.sh`, `build_glossary.py`, `verifier_livres.py`,
  `sync_biblio.py`, `push_biblio.py`) ne dépendent pas du nom des chapitres ;
- le livre n'existe qu'en français : la scission ne touche pas à `precis/ar/` ; chaque chapitre ajouté est
  déclaré dans `_quarto.yml` français, et les parties du livre sont des titres à écrire dans ce fichier.

## 4. Ce que chaque chapitre a, peut avoir, et n'a pas

« En série » : déjà dans le précis après la passe du 27 octobre 2026. « À portée » : source déjà dans
`tunisia-data` ou dans le corpus local, à dépouiller. « À obtenir » : source à chercher.

| Chapitre | En série | À portée | À obtenir |
|---|---|---|---|
| 1. Statut | textes 1969 à 2019, listes 1997-2021 | loi n° 89-9 consolidée, décrets de 2002, 2013 et 2020 sur la tutelle et les entreprises placées en concurrence (dans `jort_cache.db`), loi n° 2004-30 et n° 2007-33 | aucun modificatif de la loi après 2006 identifié ; listes nominatives des rapports 2022-2025 à feuilleter |
| 2. Gouvernance | stratégie de 2015, Livre blanc de 2018, rapport annuel de 2019 | loi n° 85-74 et ses modificatifs de 1987 et 1988, décret n° 2014-12 sur la rémunération des dirigeants, décrets de 2002 et de 2016 sur la tutelle, arrêté de 2022 sur la composition des conseils, décret de 2023 et de 2024 sur les comités d'audit | rapports de la Cour des comptes par entreprise (BNA 2009, SONEDE 2012, flotte de Tunisair 2018, supervision bancaire 2021 sont au catalogue) |
| 3. Transferts | 2016-2024 par secteur et par nature ; plafond de 2016 à 2026 sans objet ici | annexes 8 d'avant 2020, lois de règlement, rapports annuels de la Banque centrale (1959-1986 et 2015-2025 sont rangés), fonds spéciaux des rapports de clôture | transferts par entreprise 2010-2015 ; total « hors compensation, hors caisses » |
| 4. Garanties | plafond de la garantie 1958-2026, plafond des prêts du Trésor 2016-2026, garanties accordées 2016-2024, encours 2016-2024 et selon la Cour 2018-2023, principal remboursé 2010-2024 | plafond des prêts avant 2016 (article voisin de chaque loi, vu), article de la loi de finances de 1997 sur les offices des céréales et de l'huile, loi de finances complémentaires 1969-1991, encours rétrocédé (rapports sur la dette publique, pages repérées) | encours avant 2016 ; garantie de la gestion 1960 et décret de 1957 ; éditions françaises de six fascicules du JORT |
| 5. Recettes | versements 2010-2024, part de l'État dans les bénéfices 2017-2023, échantillon 2017-2022 | rapports de clôture 2005, 2006, 2007 et 2009 (téléchargés), rapports de la Banque centrale | règles de répartition des bénéfices ; rapport de clôture de 2010 et de 2017 ; rapports 1987-2004 |
| 6. Céder | recettes 1987-2024 en deux sources, 15 sorties datées au recueil | seize pages sectorielles du recueil des opérations de la Direction générale de la privatisation, page « bilan global » (114 privatisations totales, 29 partielles, 10 offres publiques, 5 concessions, 41 liquidations), loi n° 99-38, décrets de 1997 et 1998 sur la commission d'assainissement | cessions depuis 2009 ; sociétés confisquées (voir § 5) |
| 7. Restructurer | contrats de performance de 2018, audit des banques publiques 2016-2021 | articles des lois de finances sur le fonds de restructuration du capital (1986, 1990, 2003) et arrêtés de 1989 à 1993 ; articles 14 à 16 des lois de finances de 2014 et de 2015 sur les banques publiques et le fonds de modernisation du secteur bancaire ; tableaux des fonds spéciaux des rapports de clôture | recapitalisations en réalisation ; reprise de dettes (Tunisair, 165 MD autorisés en 2014) |
| 8 à 13. Entreprises | effectifs 2016-2023 pour 50 entités, résultats des dix premières, subvention de la STEG, rapports annuels de l'ETAP 2005-2024, transport (volume de la compensation) | fiches par entreprise des rapports annuels (dette, subvention d'exploitation, passifs), tableaux arabes à rendre à 170 dpi, rapports de la Cour des comptes | rapport de l'Unité de suivi 2010-2014 ; bilans par entreprise avant 2016 |
| 14. Emploi et comptes | effectifs 2018-2022, charges de personnel, résultats 2017-2022 | agrégats par secteur institutionnel (INS), 117 416 employés de 2010 (Banque mondiale) à rapprocher sans chaîner | effectif total de 2021 et d'avant 2018 |
| 15. Longue période | cessions 1987-2024, clôture 2010-2024, annexes 2016-2024 | budget de l'État 1986-2026 et budgets d'équipement 1961-1986 (rangés), plans de développement | réalisation du budget avant 1986 ; PIB de 1959-60 et de 1960 |
| 16. Études | Livre blanc, Banque mondiale 2014 et 2020, FMI 2021, ITCEQ 2010 | OCDE, Cour des comptes (dette publique extérieure, 2018, téléchargée) | |

## 4 bis. Le détail des sections de chaque chapitre

Ordre de chaque chapitre : vue d'ensemble, mise en place, grandes réformes, état du droit, sections
secondaires, longue période, « Ce qu'en dit l'économie ». Entre parenthèses : l'ancre actuelle, ou
« nouveau » pour une section à écrire.

**Présentation (`index.qmd`)**

- La carte des institutions : texte fondateur, date, chapitre où lire (nouveau, à partir de `sec-ep-vue-ensemble`).
- La frise de 1948 à 2020 (§ 7).
- Ce que pèse l'ensemble : effectifs, transferts, garanties.
- Le voisinage avec les autres livres (`tbl-ep-voisinage`, fait).
- Les définitions des termes : entreprise publique, établissement public, participation.

**1. Ce qu'est une entreprise publique**

- Vue d'ensemble : trois périmètres successifs (1969, 1985, 1989), puis la liste (nouveau, 150 mots).
- Avant 1969 : offices et régies du Protectorat, nationalisations de 1956-1964 (nouveau, couche du passé).
- 1969 : la tutelle étendue aux filiales (`sec-ep-1969`).
- 1985 : le seuil de 34 % et les contrats-programmes (`sec-ep-1985`).
- 1989 : le seuil de 50 % (`sec-ep-1989`, partie périmètre).
- 1994-2001 : banques, assurances, établissements sur liste (`sec-ep-1994-2001`).
- 2006 : l'ouverture à la concurrence, loi n° 2007-33 (nouveau ; textes dans `jort_cache.db`).
- Les listes d'établissements 1997-2021 (annexe).
- L'état du droit au 1ᵉʳ janvier 2026 (`sec-ep-etat-du-droit`).

**2. Le contrôle et la gouvernance** (provisoire : fondu dans le 1 tant que la matière manque)

- Le contrôle financier de 1948 et de 1969, les contrôleurs d'État (nouveau).
- Les fautes de gestion, 1985-1988 (nouveau ; loi n° 85-74 à lire).
- Depuis 2011 : la stratégie de réforme de 2015-2018 (`sec-ep-apres-2011`).
- La rémunération des dirigeants, décret n° 2014-12 (nouveau).
- Le rapport annuel de 2019 (`sec-ep-2019`).
- Les comités d'audit de 2023-2024 et la composition des conseils de 2022 (nouveau).
- Ce qu'en dit l'économie : gouvernance (fiche à écrire).

**3. Les transferts du budget**

- Ce que recouvrent les transferts : subventions d'exploitation, dotations en capital, interventions (`sec-ep-transferts`).
- 2016-2024 par secteur et par nature (`sec-ep-transferts`, figure).
- La régularisation de 2020 (même section).
- 2010-2015 et avant : annexes 8, lois de règlement, rapports de la Banque centrale (nouveau).
- Ce qu'en dit l'économie : contrainte budgétaire molle.

**4. Les garanties, les prêts et les arriérés**

- Vue d'ensemble : l'encours garanti et son plafond (nouveau, court).
- Le plafond de la garantie fixé par la loi de finances, 1958-2026 (`sec-ep-garanties-plafond-legal`).
- La commission de garantie de 1993 et la loi organique de 2019 (nouveau, extrait de `sec-ep-garanties`).
- Les garanties accordées et l'encours, 2016-2024 (`sec-ep-garanties`).
- Les prêts du Trésor : plafond 2016-2026, registre (`sec-ep-garanties`).
- Les prêts rétrocédés (nouveau ; rapports sur la dette publique).
- Les dettes et créances croisées, 2021-2023 (`sec-ep-croisees`).
- Les garanties de la clôture 2010-2024 (extraites de `sec-ep-lp-cloture`).
- Ce qu'en dit l'économie : passifs éventuels.

**5. Ce que l'État reçoit**

- Première phrase : la Banque centrale n'est pas une entreprise publique et pèse 58 % des versements en 2024.
- La part de l'État dans les bénéfices (`sec-ep-dividendes-part`).
- Les versements et les transferts reçus, sur un échantillon (`sec-ep-flux`).
- Les versements 2010-2024 d'après la clôture (extraits de `sec-ep-lp-cloture`).
- Les règles de répartition des bénéfices (nouveau ; source à obtenir).

**6. Céder**

- Vue d'ensemble : 114 privatisations totales, 29 partielles, 10 offres publiques, 5 concessions, 41 liquidations (recueil de la Direction générale de la privatisation).
- 1987 : la cession autorisée (`sec-ep-1987`).
- 1989 : l'organisation de la cession (`sec-ep-1989`).
- 1994 : l'action spécifique (`sec-ep-1994-2001`).
- 1999 : la liquidation, loi n° 99-38 (nouveau).
- Les recettes de cession 1987-2009 (`sec-ep-lp-cessions`).
- Les recettes budgétaires 2010-2024 (`sec-ep-cessions`, `sec-ep-lp-cloture`).
- Une section par secteur du recueil (nouveau ; seize pages à dépouiller).
- Les sociétés confisquées depuis 2011 : une ligne tant que la question de domicile (§ 5) n'est pas tranchée.
- Ce qu'en dit l'économie : effets des privatisations.

**7. Restructurer**

- Les contrats-programmes de 1985 (`sec-ep-1985`, partie contrats).
- Le fonds de restructuration du capital, 1986-2003 (nouveau ; lois de finances).
- La commission d'assainissement de 1997 (nouveau).
- Les banques publiques, 2012-2015 : articles 14 à 16 des lois de finances de 2014 et 2015 (nouveau).
- Les contrats de performance de 2018 (`sec-ep-apres-2011`).
- La reprise de dettes : Tunisair, 165 MD autorisés en 2014 (nouveau).
- Ce qu'en dit l'économie : recapitalisation bancaire.

**8 à 13. Les entreprises** (aucun écrit ; plan commun)

- Naissance et statut de l'entreprise.
- Les comptes : résultats, total des passifs.
- La dette et les garanties dont elle bénéficie.
- La subvention d'exploitation et les transferts reçus.
- L'emploi.
- La longue période.

Secteurs : énergie (STEG, STIR, ETAP) ; mines et chimie (CPG, Groupe chimique) ; offices et monopoles ;
transports ; eau et communications ; secteur financier public. Matériau existant : `sec-ep-lp-entreprises`
et la subvention de la STEG. La subvention et son partage entre les ménages restent dans « La compensation ».

**14. L'emploi et la masse salariale**

- Les effectifs 2016-2023 pour 50 entités et les charges de personnel (`sec-ep-effectifs`).
- Les six éditions du rapport et leurs échantillons (`sec-ep-lp-editions`).
- Les résultats agrégés par édition, 2017-2022 (`sec-ep-lp-resultats`).
- La dizaine d'entreprises les plus lourdes (`sec-ep-lp-entreprises`), jusqu'à l'ouverture des chapitres 8 à 13.
- Les agrégats de l'INS et les 117 416 employés de 2010 (Banque mondiale), rapprochés sans chaînage.

**15. La relation financière, 1960-2024**

- Transferts, garanties, recettes et cessions côte à côte, par plan de développement (nouveau ; figure d'ensemble).
- Le tableau des ruptures de série : 2020, la privatisation absente 2017-2024, les sources non chaînées.
- Les années sans série budgétaire (`sec-ep-lp-lacunes`).
- Le PIB : base 2015, jamais chaînée, avec renvoi à l'annexe PIB.

**16. Le Livre blanc et les études extérieures** (écrit ; déplacé tel quel)

- Le Livre blanc de 2018 (`sec-ep-livre-blanc`).
- Banque mondiale 2014 et 2020 (`sec-ep-banque-mondiale-2014`, `sec-ep-banque-mondiale`).
- FMI 2021 (`sec-ep-fmi`).
- ITCEQ 2010 (`sec-ep-itceq`).

**Annexes** : la liste des entreprises 1997-2021 (inchangée) ; le registre des textes, réparti par chapitre ; le glossaire.

## 5. Les pièges de domicile, à trancher avant la scission

- **Ce qui reste dans la compensation.** Le statut, les comptes, la dette, l'emploi d'une entreprise qui
  porte la compensation (STEG, STIR, Office des céréales, Office de l'huile, sociétés de transport) sont
  ici. La subvention, ses taux et sa répartition entre les ménages restent dans « La compensation » :
  les chapitres 8, 10 et 11 ne donnent que la phrase et le lien.
- **La Banque centrale n'est pas une entreprise publique.** Ses profits dominent les versements au budget
  (58 % en 2024). Le chapitre 5 le dit dès sa première phrase.
- **Les caisses de sécurité sociale** sont des entreprises publiques au sens de la loi mais leurs comptes
  sont dans « Les caisses » : chaque chapitre dit si elles sont dans ses totaux.
- **Les sociétés confisquées depuis 2011.** Le décret-loi n° 2011-13 organise la confiscation d'avoirs et de
  biens, le décret-loi n° 2011-68 crée la commission nationale de gestion des avoirs, et des arrêtés de 2011 et
  de 2012 créent la recette des produits de biens confisqués. Le rapport de clôture de 2022 range une cession
  de 45 MD de société pharmaceutique parmi les recettes de confiscation. **Question ouverte :** ces sociétés,
  dont l'État détient la majorité du capital, sont-elles des entreprises publiques au sens de la loi n° 89-9 ?
  À lire dans les textes avant de leur donner un domicile ici ; en attendant, une ligne dans le chapitre 6.
- **Concessions et partenariats public-privé** (décret de 2010, unité de suivi de 2013, décret
  gouvernemental de 2020) : hors périmètre du volume, aucune entreprise publique ni flux budgétaire. Une
  ligne dans le tableau de voisinage et une phrase dans le chapitre 6, qui compte cinq concessions parmi les
  opérations de la Direction générale de la privatisation.
- **Les rémunérations.** Les statuts, les grilles et les augmentations sont aux « Rémunérations publiques » ;
  le chapitre 2 ne traite que de la rémunération des dirigeants (décret de 2014), le chapitre 14 que de la
  masse salariale.
- **Le Livre blanc de 2018**, « à extraire » selon le chantier : c'est le chapitre 16, déjà écrit, à
  déplacer tel quel.

## 6. L'ordre de remplissage et de scission

La consigne : une ossature de longue période, remplie d'abord par les années récentes, puis par couches vers
le passé.

1. **Passe en cours** (27 octobre 2026) : clôture 2010-2024, plafonds 2016-2026. Elle touche les futurs
   chapitres 4, 5, 6 et 15. Aucune scission pendant cette passe : une PR, un sujet.
2. **Scission mécanique**, une fois cette passe relue et fusionnée : créer les fichiers du § 3, déplacer les
   sections sans changer le texte, déclarer les chapitres dans `_quarto.yml`, corriger le lien externe et les
   dix fiches, rendre le livre. Aucun contenu nouveau. Niveau de modèle : mécanique.
3. **Années récentes, chapitre par chapitre**, dans l'ordre où les sources sont ouvertes :
   chapitre 5 (rapports de clôture 2005-2009, rapports de la Banque centrale récents), chapitre 3 (annexes 8
   d'avant 2020, lois de règlement), chapitre 7 (articles des lois de finances de 2014, 2015, fonds spéciaux),
   chapitre 6 (recueil sectoriel de la privatisation), chapitre 2 (loi n° 85-74, décret n° 2014-12,
   décrets de contrôle).
4. **Passé, par couches** : rapports annuels de la Banque centrale de 1987 à 2015 (transferts, revenus de
   participations), lois de finances complémentaires de 1969 à 1991, antécédents du Protectorat (offices,
   régies) pour la mise en place du chapitre 1.
5. **Versement des fiches par entreprise** des rapports annuels : c'est ce qui débloque les chapitres 8 à 13.
   Marche à part, à planifier tôt, car elle demande de la lecture à l'image (tableaux arabes tournés).
6. **« Ce qu'en dit l'économie »** : fiches de l'économiste pour les chapitres 3, 4, 6 et 7, en dernier.

## 7. La frise de la présentation

La présentation du livre doit porter une frise des dates clés de tous les dispositifs sur un seul axe. Dates
déjà sourcées dans le volume : 1948 (contrôle financier), 1958 (plafond de la garantie), 1969 (tutelle des
filiales), 1985 (seuil de 34 %, contrats-programmes), 1987 (cession autorisée), 1989 (seuil de 50 %),
1993 (commission de garantie), 1994 (action spécifique), 1996 (liste des établissements), 1999 (liquidation),
2006 (concurrence), 2011 (confiscation), 2014-2015 (banques publiques), 2018 (Livre blanc), 2019 (rapport
annuel), 2020 (règlement des arriérés). À compléter par les dates des créations d'entreprises (Protectorat,
nationalisations de 1956-1964) quand les chapitres 8 à 13 s'ouvriront.

## 8. Ce qu'il faut que l'humain tranche

1. Le nombre de chapitres de la partie III : six chapitres sectoriels, ou un chapitre « Les grandes
   entreprises » avec une section par entreprise, au moins tant que les fiches ne sont pas versées.
2. Les sociétés confisquées : domicile dans ce volume ou non (question du § 5).
3. Le chapitre 2 : séparé dès maintenant, ou fondu dans le chapitre 1 jusqu'à ce qu'il ait sa matière.
4. L'ordre des chapitres dans le livre : par dispositif (partie II d'abord), comme ci-dessus, ou par
   institution (partie III d'abord), plus proche du lecteur qui cherche « sa » entreprise.

## 9. Décisions de l'humain (27 octobre 2026)

1. Seize chapitres, regroupés en six grandes sections (les six parties du § 2).
2. Chapitre 2 (gouvernance) fondu dans le chapitre 1 jusqu'à ce qu'il ait sa matière.
3. Partie III : **un seul chapitre « Les grandes entreprises »**, une section par entreprise ; scission par secteur
   quand trois entreprises du secteur ont leur fiche. Les chapitres 8 à 13 du § 2 sont donc des cibles, non des
   chapitres ouverts.
4. Les dispositifs d'abord (partie II avant la partie III) ; les notions sont précisées dès la présentation
   (entreprise publique, établissement public, participation, garantie, prêt rétrocédé, cession, privatisation).
5. Sociétés confisquées : une ligne dans le chapitre 6, sans domicile propre.
6. Moment de la scission : non tranché.
7. Les sections mixtes (1989, 1994-2001, clôture 2010-2024) sont éclatées entre les chapitres.
8. Le registre des textes est réparti par chapitre.
9. Ancres `sec-ep-*` et `r-ep-*` conservées.
10. Français seulement ; `precis/ar/` non touché.
