# Fiche de plan de livre — « Le transport » (partie IV, politique sectorielle)

Architecte, 10 novembre 2026. Fiche de plan de **livre**, préalable à toute note documentaire :
aucune rupture n'y est affirmée ; tout texte cité sans lecture l'est « connu par son intitulé,
à lire ». Référentiel : `docs/conventions-redaction.md` § 4 ; ordre arrêté dans
`docs/notes/chantier-decoupage-livres.md` (« le transport » d'abord parmi les trois futurs
sectoriels, et il « réorganise plus qu'il n'ajoute »).

## 1. Objet et périmètre

**Objet en une phrase.** Ce que l'État paie pour que les personnes et les marchandises
circulent — l'infrastructure qu'il finance (routes, autoroutes concédées, rail, ports,
aéroports), les contrats et subventions qu'il passe avec les opérateurs publics, et les tarifs
sociaux qu'il rembourse — avec la dépense publique de transport sur la longue période.

**Ce qui entre** (épine budgétaire, conforme à la règle des livres sectoriels) :

- l'institution : le ministère du Transport, le ministère de l'Équipement pour la route, les
  agences et offices du secteur (tutelle, missions, programmes budgétaires — les missions
  « Transport » et « Équipement et Habitat » des PAP/RAP sont déjà cataloguées dans
  `tunisia-data/sources/ministere-transport-equipement-habitat.md`) ;
- la dépense publique de transport sur la longue période (crédits des deux missions,
  transferts aux entreprises du secteur — la série `transport-transferts-par-entreprise`
  2016-2024 existe dans `tunisia-data`) ;
- les dispositifs à flux monétaire propres au secteur : l'investissement en infrastructure et
  son financement (dont le fonds de développement des autoroutes, 1999-2018, déjà relevé au
  chapitre « Les transports » des entreprises publiques) ; les concessions autoroutières et le
  péage ; les contrats-programmes des opérateurs (état relevé dans les PAP : métro de Sfax
  « non achevé ni visé », SNIT 2021-2025 — à documenter pour le secteur) ; les subventions
  d'exploitation et d'équilibre, en articulation avec la compensation (voir § 5) ;
- les rapports et études : Cour des comptes (trois rapports transport déjà rangés dans
  `tunisia-data`), Banque mondiale (*Livre blanc* transports et logistique, 2016, rangé et
  partiellement versé).

**Ce qui n'entre pas** :

- le code de la route et la réglementation sans effet budgétaire ni distributif (permis,
  immatriculation, signalisation) — hors livre par la règle du § 4 ; l'ATTT, qui perçoit des
  droits, reste une institution des entreprises publiques ;
- le tarif administré du transport public et sa compensation : domicile à la compensation
  (`precis/fr/compensation/_transport.qmd`, chapitre complet, huit textes 1948-2017, état du
  droit d'octobre 2026) ;
- le statut et les comptes des opérateurs : domicile aux entreprises publiques
  (`precis/fr/entreprises_publiques/_transports.qmd`, douze sections : Tunisie Autoroutes,
  Transtu, SNCFT, RFR, métro de Sfax, Tunisair, ATTT, OACA, OMMP, CTN, SNTRI, sociétés
  régionales) ;
- la taxe de circulation (« vignette ») et les taxes sur les véhicules : fiscalité (recette du
  budget général, relevée dans `_taxes_fonds_speciaux.qmd` ; le décret du 31 mars 1955,
  art. 19 à 21, est hors corpus — backlog de la fiscalité).

## 2. Tableau de domicile et de voisinage

C'est le cœur du livre : il **réorganise plus qu'il n'ajoute**. Chaque ligne dit où le sujet
vit et ce que le livre transport en reçoit.

| Sujet limitrophe | Vit dans | Le livre transport reçoit |
|---|---|---|
| Tarifs administrés du transport public, abonnement scolaire et universitaire, gratuités et leur remboursement, compensation du transport | Compensation (`_transport.qmd`) | une phrase et un lien ; au chapitre « transport urbain et interurbain », une figure courte de la subvention par société (mêmes données que `fig-compensation-transport-soutien`), jamais la prose |
| Statut, comptes, dette, effectifs des opérateurs (Transtu, SNCFT, Tunisair, OACA, OMMP, CTN, SNTRI, SRT, RFR, métro de Sfax, ATTT, Tunisie Autoroutes) | Entreprises publiques (`_transports.qmd`) | une phrase et un lien par opérateur ; le livre transport garde ce que l'État **décide et paie** (concession, contrat-programme, subvention, garantie d'un projet), pas les comptes |
| Concessions autoroutières, péages, fonds de développement des autoroutes | Aujourd'hui dans la section Tunisie Autoroutes des entreprises publiques | **à déménager** (candidat) : la concession et le péage sont une politique du secteur, pas un compte d'entreprise — arbitrage au § 5 |
| Taxe de circulation, taxes sur les véhicules, taxe par siège des véhicules de transport touristique | Fiscalité (`_taxes_fonds_speciaux.qmd` ; chapitre timbre à compléter, TODO existant) | rien, ou une phrase si un chapitre du livre en a besoin |
| Fonds de prévention des accidents de la circulation (Intérieur), fonds de garantie des victimes des accidents de la circulation (Domaines de l'État) | Fiscalité (liste des fonds spéciaux) | rien tant que leurs emplois ne sont pas documentés |
| Transport urbain et scolaire comme compétence partagée des communes ; transport non urbain de la région (abrogé en 2025) ; permis de circulation des taxis, stationnement | Finances locales (`_competences.qmd`, `_taxes_redevances.qmd`) | une phrase et un lien au chapitre « transport urbain et interurbain » |
| Transport des élèves pauvres (budgets communaux), abonnement scolaire comme aide à la scolarité | Éducation (`_aides.qmd`, `_depense.qmd`) — qui renvoie déjà à la compensation | une phrase et un lien |
| Subventions au bac de Kerkennah, à Tunisair Express, au port d'Enfidha (relevées dans le poste transport de la compensation et les PAP) | Compensation (poste) ; entreprises publiques (opérateurs) | le chapitre « aérien et maritime » les réunit par une figure ou un tableau court tiré des mêmes données, si le chapitre existe (§ 5) |

## 3. Plan de chapitres proposé (plan type sectoriel)

| Chapitre | Ce qu'il doit établir | État de la matière |
|---|---|---|
| Présentation | objet en une phrase ; carte des dispositifs (texte fondateur, date d'application, où lire) ; figure du poids de l'ensemble ; frise des dates clés ; conventions de lecture ; tableau de voisinage (§ 2) | matière éparse à réunir ; la frise peut reprendre les dates déjà établies (compensation 1948-2017, concessions 1995-2019) |
| Institution et tutelle | le ministère du Transport et le ministère de l'Équipement, leurs programmes budgétaires (missions GBO), les agences ; qui décide quoi (tarif : ministre, relevé dans la compensation ; concession : décret ; contrat-programme : tutelle) | filiation des deux ministères **sourcée** (T2) : ossature actuelle du Transport = décrets 2014-409 (attributions) + 2014-410 (organisation), révisé par 2016-97 ; Équipement descendu des travaux publics (1970) ; carte des agences/offices de tutelle relevée ; PAP/RAP catalogués ; **restent à confirmer** les décrets d'organisation postérieurs à 2016 (Transport) et 2018 (Équipement), création SPROLS |
| La dépense publique de transport, longue période | crédits des missions Transport et Équipement sur la longue période ; transferts aux entreprises du secteur ; part de l'investissement ; rapport au cadre des finances publiques | **sourcée** (T4) : mission Transport **2012-2024** et mission Équipement **2014-2024** (investissement routier ~85 % de la mission), exécution RAP 2018-2023 et transferts 2016-2024 versés ; rupture de nomenclature (LOB 2019) signalée dans la série ; **trous** = avant-GBO (Transport < 2012, Équipement < 2014), exécution 2024-2026 (RAP non collectés), cohérence des nomenclatures |
| Infrastructure routière et autoroutes | la route financée au budget (Équipement) et l'investissement (mission Équipement) ; le fonds de développement des autoroutes (1999-2018) ; le programme autoroutier d'avant 1995 ; **renvoie par liens** aux concessions, péages et garanties, **ne les déménage pas** (arbitrage 2 tranché, variante prudente) | registres concessions/péages/garanties déjà écrits et ancrés dans la section Tunisie Autoroutes des entreprises publiques (34 ancres `#r-ep-autoroutes-*`, concessions 1995-2025, péages 1996-2022, huit garanties 1999-2012) : **à relier, pas à re-sourcer** ; apport propre **sourcé** (T3) = fonds autoroutier 1999-2018 et route au budget ; **programme d'avant 1995** et ressources/emplois du fonds à détailler (recherche à ce jour bredouille) |
| Le ferroviaire | ce que l'État confie et paie à la SNCFT et au RFR : concession/cahier des charges (le cahier des charges de 2001 et son droit à compensation sont au chapitre compensation), contrats-programmes, projets (RFR), garanties | cahier des charges SNCFT = décret n° 2001-2621 du 9 nov. 2001 **relevé** (T5) ; dernier contrat-programme SNCFT daté (2002-2006), RFR sans contrat-programme signé ; **réalisation à collecter** ; comptes restent aux entreprises publiques |
| Le transport urbain et interurbain | l'organisation du transport public de personnes (la loi de 1985 et la loi de 2004, déjà lues pour la compensation, sont candidates à relire ici sous l'angle de l'organisation) ; les contrats-programmes des sociétés ; renvois : tarifs → compensation ; compétences locales → finances locales | lois 85-77 (1985, 23 art.) et 2004-33 (2004, 64 art.) **relues au fascicule** sous l'angle organisation (T1 ; loi 1985 par OCR, à contrôler à l'image avant citation littérale) ; dernier contrat-programme Transtu daté (18 mars 2003) ; abrogation 2025 du transport régional → **finances locales** ; renvois posés |
| L'aérien et le maritime | ce que le budget paie hors les comptes des opérateurs : subventions à des liaisons (bac de Kerkennah, Tunisair Express relevées), ports et aéroports ; les contrats-programmes et contrats de performance des acteurs | **chapitre ferme** (arbitrage 3 tranché le 10 nov. 2026) ; contrats-programmes relevés par acteur (T5) : SONOTRAK (Kerkennah, oct. 2022), Société du port d'Enfidha (contrat de performance 2022-2025, décret 2018-1006), OACA (mai 2017), OMMP (aucun) ; **budgets 2022-2026 à relever** (SONOTRAK p. 185, Enfidha, OACA, OMMP — PAP 2024) |
| Rapports et études | Cour des comptes (tutelle du transport terrestre 2008, ministère du Transport 2016, SNTRI 2017 — rangés, le troisième non exploité) ; Banque mondiale, *Livre blanc* 2016 ; chacun avec sa méthode | PDF rangés dans `tunisia-data` ; lecture **à faire** (sauf extraits versés) |
| Glossaire | entrées du secteur | à constituer ; des entrées existent déjà (compensation du transport, Tunisie Autoroutes) |

Chaque chapitre de dispositif se clôt sur « Ce qu'en dit l'économie » (fiche
`docs/notes/eco-<dispositif>.md` à demander à l'économiste — aucune n'existe ; la note du 11
octobre 2026 constate qu'aucune évaluation de l'incidence du poste transport n'a été trouvée).

## 4. Questions au documentaliste

**Textes fondateurs candidats, connus par intitulé seulement (à lire) :**

- la loi d'organisation des transports terrestres de 1985 et celle de 2004 : lues pour la
  compensation sous l'angle du tarif ; à relire sous l'angle de l'organisation du secteur
  (qui peut transporter, concessions et autorisations) ;
- les textes d'organisation du ministère du Transport et du ministère de l'Équipement
  (intitulés à identifier dans `jort_cache.db`) ;
- les textes des contrats-programmes des opérateurs (les PAP 2024 datent le « dernier
  contrat-programme » par acteur : fiches à relever une à une) ;
- les arrêtés de 1948 et de 1957 sur les taxes de compensation des transports automobiles
  (intitulés seuls, déjà au backlog de la compensation) ;
- le ou les textes du programme autoroutier antérieurs à la concession de 1995, s'ils existent.

**Séries budgétaires à chercher :**

- budgets du ministère du Transport 2018-2026 et antérieurs à 2013 (TODO documentaliste déjà
  posé dans `precis/fr/compensation/_transport.qmd`) ; budgets du ministère de l'Équipement sur
  la même fenêtre ;
- dépense d'investissement routier et ferroviaire sur la longue période (lois de finances,
  lois de règlement, rapports de la Cour des comptes sur la clôture du budget) ;
- réalisation des contrats-programmes (RAP, rapports d'activité des ministères).

**Déjà dans `tunisia-data` (ne pas rechasser) :** fiches `compensation-transport.md`,
`minfin-budget-transport.md` (2012-2017), `minfin-transferts-transport.md` (2016-2024),
`jort-transport-tarifs.md` (1987-2000), `ins-bms-prix-transport.md` (2007-2026),
`transport-trafic-comptes.md` (Banque mondiale et ministère des Finances),
`ministere-transport-equipement-habitat.md` (47 PDF : PAP, RAP, budgets, rapports d'activité),
`cour-des-comptes-transport-eau-habitat.md` (observations, sources citées, comptes) ; non
versés : annuaires INS SNCFT/métro 1995-2023 (colonnes à vérifier à l'image), tarifs
antérieurs à 1987.

## 5. Risques et arbitrages à trancher par l'humain

1. **Frontière avec la compensation.** Le tarif administré et sa compensation restent à la
   compensation : le chapitre y est complet et récent. Le livre transport ne reçoit qu'un lien
   et une figure courte. Risque si on déroge : prose recopiée et deux chapitres qui divergent.
2. **Frontière avec les entreprises publiques — que reste-t-il ?** Les comptes des opérateurs
   restent là-bas. Le livre transport garde la **décision et la dépense de l'État** :
   l'infrastructure, les concessions et le péage, les contrats-programmes, les subventions et
   garanties par projet, la dépense longue période. Arbitrage le plus lourd : **déménager ou
   non les registres concessions/péage** de la section Tunisie Autoroutes (aujourd'hui aux
   entreprises publiques) vers le chapitre routier. Pour : c'est une politique sectorielle,
   pas un compte. Contre : la section vient d'être écrite, les ancres `#r-ep-autoroutes-*`
   sont citées, et la règle du domicile unique interdit la duplication. Variante prudente :
   le livre transport renvoie par liens tant que le chapitre routier n'est pas écrit.
   **TRANCHÉ le 10 novembre 2026 — variante prudente retenue :** on **ne déménage pas** les
   registres hors de la section Tunisie Autoroutes des entreprises publiques ; le chapitre
   routier **renvoie par liens** vers les ancres `#r-ep-autoroutes-*`. Son apport propre = le
   fonds de développement des autoroutes (1999-2018), le programme d'avant 1995, la route au
   budget et l'investissement (mission Équipement).
3. **Opportunité d'un chapitre aérien et maritime.** Les flux budgétaires propres identifiés
   sont minces (Kerkennah, Tunisair Express, Enfidha). S'ils ne grossissent pas à la lecture
   des PAP et de la Cour des comptes, une section du chapitre de la dépense suffit — ne pas
   créer un chapitre pour le remplir ensuite.
   **TRANCHÉ le 10 novembre 2026 — OUI à un chapitre dédié :** la matière a grossi à la lecture
   du PAP 2024 (contrats-programmes SONOTRAK et port d'Enfidha 2022, OACA, OMMP). « L'aérien et
   le maritime » devient un chapitre à part entière, non une simple section de la dépense.
   Report associé : relever les budgets 2022-2026 de ces acteurs.
4. **Opportunité du livre lui-même.** Si, après les arbitrages 1 à 3, la matière propre se
   réduit à l'infrastructure et aux contrats-programmes, un livre mince est possible mais
   assumé : son apport est la **réorganisation** (carte, voisinage, dépense longue période),
   conformément au chantier. L'alternative — des chapitres « infrastructure » ailleurs — n'a
   pas de domicile naturel (ni la compensation ni les entreprises publiques).
   **TRANCHÉ le 10 novembre 2026 — l'épaisseur n'est pas un obstacle :** le volume se fait ;
   son apport assumé est la **réorganisation** (carte, voisinage, dépense longue période).
5. **Ordre des travaux.** *(Reste ouvert au 10 novembre 2026.)* Le chantier prévoit le cadre
   des finances publiques avant toute politique sectorielle nouvelle, et l'éducation avant le
   transport : ce livre ne se lance pas avant ces préalables ; la présente fiche sert à cadrer
   la collecte documentaire. La rédaction `.qmd` n'est pas ouverte.

## Backlog (reports constatés par cette fiche)

- Fiches « Ce qu'en dit l'économie » du secteur : aucune n'existe (`docs/notes/eco-*.md`).
- Rapport Cour des comptes SNTRI (2017) rangé mais non exploité ; rapports 2008 et 2016 à lire.
- Textes d'organisation des ministères du Transport et de l'Équipement : intitulés à
  identifier, rien de relevé.
- Budgets Transport 2018-2026 et avant 2013, budgets Équipement : TODO documentaliste existant,
  étendu ici à l'Équipement.
