# L'environnement — fiche de plan de livre

Rôle : architecte. Date : 10 novembre 2026.

Fiche de plan pour un futur volume sectoriel « L'environnement », prévu par la doctrine
(`docs/conventions-redaction.md`, § 4 : partie IV, politiques sectorielles) et placé **en dernier**
des futurs sectoriels par `docs/notes/chantier-decoupage-livres.md` (« le transport ; le logement ;
l'environnement en dernier »). Il n'existe aucune note documentaire pour ce livre : cette fiche
n'affirme aucune rupture, ne date aucun texte au-delà de ce qui est déjà lu dans le dépôt, et cite
les autres textes comme **candidats à lecture**, connus par leur intitulé.

**Décision du propriétaire (10 novembre 2026, soir).** Le périmètre du livre suit **la tutelle
du ministère de l'Environnement** (ANPE, ANGed, APAL, ONAS…), et **l'eau y reste** — décision
plus large que la recommandation R1 ci-dessous (aval seul), qui est donc caduque en tant que
recommandation ; ses arguments restent lisibles. Conséquences : les redevances d'assainissement
suivent l'ONAS dans ce livre (R2, option a, impliquée par le principe de tutelle — à confirmer) ;
la SONEDE et l'eau potable entrent dans le périmètre eau. **Frontière à confirmer** : l'eau
d'irrigation (tarif, périmètres irrigués), que la fiche agriculture du même jour range comme
intrant du producteur (livre agriculture) — proposition : l'irrigation au livre agriculture,
le reste de l'eau ici, chacun une ligne du tableau de voisinage de l'autre.

**Arbitrages tranchés par le propriétaire (11 novembre 2026), après les notes documentaires
Q1/Q3/Q4.** Les textes fondateurs sont désormais *lus* (voir `environnement-q1-textes-fondateurs.md`,
`environnement-q3-budget.md`, `environnement-q4-fonds.md`), ce qui éclaire trois frontières :

- **A1 — Redevances d'assainissement : elles déménagent dans ce livre** (confirme R2, option a). Au
  montage, elles quittent la section ONAS des *Entreprises publiques* pour le chapitre
  « assainissement » d'ici ; la section ONAS garde une phrase et un lien. Déménagement par la
  procédure du chantier (registre de destination, aucune ligne « supprimé »).
- **A2 — Eau potable / SONEDE : en contexte, pas en chapitre.** « L'eau reste », mais la SONEDE
  relève de la **tutelle Agriculture** (ressources hydrauliques), établi par Q1 : elle demeure
  domiciliée aux *Entreprises publiques*. Le livre n'en reçoit qu'une phrase, le lien, et le minimum
  tarifaire nécessaire pour lire la redevance d'assainissement (assise sur la consommation d'eau,
  facturée par la SONEDE). L'épine du livre reste l'aval : assainissement, déchets, dépollution.
- **A3 — Littoral / APAL : HORS de ce livre.** L'APAL est passée sous tutelle de
  l'**Équipement/Habitat** en 2004 (décret n° 2004-106, lu en Q1) ; aucun re-transfert vers
  l'environnement n'est localisé. Le littoral, le domaine public maritime et l'APAL sont donc routés
  vers un **futur livre sectoriel « Habitat / logement »** (non encore ouvert ; planifié avec le
  transport dans `chantier-decoupage-livres.md`). Ce livre-ci ne le **mentionne** qu'en une ligne de
  voisinage, avec renvoi. *Report : les clés `loi95-72-apal` et `loi95-73-dpm`, versées dans
  `environnement/references.json`, sont à re-domicilier vers le livre Habitat/logement à son
  ouverture ; elles restent ici tant qu'il n'existe pas, pour la ligne de mention.*

Mise en garde de sigle : dans ce livre, **ANPE désigne l'Agence nationale de protection de
l'environnement** (loi n° 88-91, connue ici par son intitulé) — jamais l'agence de l'emploi
(ANETI). Les deux sigles coexistent dans le dépôt (l'« indemnité ANPE » du livre des retraites
relève de l'emploi) : le rédacteur écrira le nom en toutes lettres à la première occurrence et
posera une entrée de glossaire désambiguïsée.

## 1. Objet et périmètre

**Objet en une phrase.** Ce que l'État tunisien dépense, prélève et tarifie pour l'assainissement
des eaux usées, la gestion des déchets, la dépollution industrielle et la protection du milieu —
les institutions qui portent ces flux, leur dépense sur la longue période, et ce qu'en disent les
rapports et les études.

**L'épine est budgétaire**, conformément au § 4 des conventions : institution, dépense longue
période, dispositifs à flux monétaire, études. La réglementation sans effet budgétaire ni
distributif — études d'impact, normes de rejet, police de l'environnement, autorisations —
**n'entre pas** dans le livre ; elle n'y paraît que lorsqu'un texte qui porte un flux la contient
(exemple déjà rencontré : la loi n° 95-50 sur les canalisations ajoute l'étude d'impact, mais ce
texte vit au livre des entreprises publiques, chapitre énergie).

**Ce qui entre** (dispositifs à flux, sous réserve de la note documentaire) :

- l'**assainissement** : les redevances d'assainissement perçues au profit de l'ONAS (textes déjà
  lus au livre des entreprises publiques : décret n° 75-201, décret n° 2001-2001, arrêté de 2022),
  les transferts du budget à l'Office, la participation des riverains ; le livre sectoriel reçoit
  le **dispositif** (qui paie, combien, pour quel service, depuis quand), l'institution restant
  domiciliée aux entreprises publiques (voir § 2 et le risque R2) ;
- la **gestion des déchets** : la collecte communale (domiciliée aux finances locales), l'ANGed
  (décret n° 2005-2317, connu par son intitulé, à lire), les taxes sur les déchets exportés ou
  détruits déjà lues au chapitre des droits de douane ;
- la **dépollution industrielle** : le fonds de dépollution (FODEP, ouvert par la LF 1993,
  art. 35-37, intitulé seul, à lire), la taxe pour la protection de l'environnement qui l'alimente
  (LF 2003, art. 58-59, lue en couche texte décodée, chiffres à relire à l'image — voir le TODO du
  chapitre des taxes affectées), la prime de dépollution et les avantages « lutte contre la
  pollution » du code d'incitation (déjà documentés au chapitre des régimes d'incitation) ;
- ~~la **protection du littoral** : l'APAL~~ — **retiré du livre (A3, 11/11/2026)** : l'APAL relève
  de la tutelle Équipement/Habitat depuis 2004 et part au futur livre « Habitat / logement » ; ce
  livre-ci n'en garde qu'une ligne de voisinage (§ 2) ;
- la **dépense publique d'environnement** : budget du ministère chargé de l'environnement,
  transferts aux agences, fonds spéciaux du tableau A (fonds de dépollution ; fonds de la
  protection et de l'esthétique de l'environnement, qui figure dans l'inventaire du chapitre des
  taxes affectées sans section ni texte lu).

**Ce qui n'entre pas, ou pas ici** :

- l'**eau potable et l'eau agricole** : la SONEDE vit aux entreprises publiques, l'irrigation
  relève d'un périmètre agricole que le précis n'a pas ouvert ; le livre de l'environnement ne
  prend de l'eau que l'aval (eaux usées). Arbitrage à confirmer (risque R1) ;
- l'**énergie renouvelable et la transition énergétique** : le fonds de transition énergétique est
  inventorié au chapitre des taxes affectées, les entreprises de l'énergie vivent aux entreprises
  publiques, les prix de l'énergie à la compensation. Le livre de l'environnement n'en reçoit
  qu'une phrase et un lien ; il ne construit pas de chapitre « climat-énergie » (risque R1) ;
- la réglementation sans flux : études d'impact, normes, police, aires protégées sans dépense
  identifiée.

## 2. Tableau de domicile et de voisinage

Application de la règle de domicile du § 4 : un dispositif vit dans un seul livre ; l'autre en
reçoit une phrase et un lien, ou un tableau court tiré des mêmes données.

| Sujet limitrophe | Où il vit | Ce que le livre « Environnement » en reçoit |
|---|---|---|
| Taxe pour la protection de l'environnement, fonds de dépollution, autres taxes affectées (fonds de la protection et de l'esthétique de l'environnement) | fiscalité, chapitre des taxes des fonds spéciaux (`_taxes_fonds_speciaux.qmd`, sections @sec-fst-tpe et inventaire) | une phrase et un lien dans le chapitre « dépollution et fonds » ; le livre documente l'**emploi** du fonds (dépenses, bénéficiaires), le prélèvement restant à la fiscalité |
| Taxes perçues en douane sur les déchets (exportation de ferraille, destruction de friperie au profit du fonds de dépollution) | fiscalité, chapitre des droits de douane | une ligne de renvoi dans le chapitre « déchets » |
| Avantages fiscaux « lutte contre la pollution », prime de dépollution, dépense fiscale « protection de l'environnement » | fiscalité, chapitre des régimes d'incitation (`_regimes_incitation.qmd`) | un tableau court des montants dans le chapitre « dépollution et fonds » |
| ONAS : statut, comptes, dette, garanties, subvention d'exploitation ; SONEDE | entreprises publiques, chapitre eau et communications (`_eau_communications.qmd`, @sec-ep-ge-onas) | une figure ou un tableau court tiré des mêmes données (fiches LF) dans le chapitre « assainissement » ; la prose n'est pas recopiée |
| Redevances d'assainissement (tarif du service : décrets n° 75-201, 2001-2001, barème de 2022) | aujourd'hui décrites dans la section ONAS des entreprises publiques | **à déplacer** dans le livre sectoriel à sa création : c'est un dispositif à flux qui n'existe que pour ce secteur ; la section ONAS garde une phrase et un lien (risque R2) |
| Tarifs administrés en général | compensation | rien : le livre de la compensation ne traite ni l'eau ni l'assainissement (constat du TODO SONEDE : « Le volume "La compensation" ne traite pas l'eau ») ; si la doctrine range un jour la redevance d'assainissement parmi les tarifs administrés, l'arbitrage se fera avec la compensation (risque R2) |
| Propreté communale, déchets ménagers et non ménagers, redevance des déchets non ménagers, compétences partagées (réseaux d'assainissement, littoral) | finances locales (`_competences.qmd`, `_taxes_redevances.qmd`) | une phrase et un lien dans le chapitre « déchets » ; le partage commune / ANGed / ONAS y est exposé comme carte, pas comme droit recopié |
| Part de la réserve du fonds commun des collectivités locales versée à l'ONAS (jusqu'en 2006) | finances locales (`_transferts.qmd`) | une ligne dans la longue période du financement de l'assainissement |
| Transition énergétique, prix de l'énergie | compensation (prix) ; fiscalité (fonds de transition énergétique) ; entreprises publiques (STEG…) | une phrase et un lien ; aucun chapitre propre |
| Eau potable (prix de l'eau, SONEDE) | entreprises publiques (tutelle **Agriculture** / ressources hydrauliques) | une phrase et un lien en tête du chapitre « assainissement » (la redevance est assise sur la consommation d'eau et facturée par la SONEDE : le lecteur doit le savoir d'une phrase). **A2 (11/11/2026) : eau potable en contexte, pas de chapitre** |
| Littoral, domaine public maritime, APAL (loi n° 95-72, loi n° 95-73 DPM) | **futur livre « Habitat / logement »** (tutelle Équipement/Habitat depuis le décret 2004-106) | **A3 (11/11/2026)** : hors de ce livre ; une seule ligne de mention avec renvoi au futur livre, aucune section propre |

## 3. Plan de chapitres proposé

L'ordre suit la présentation type d'un livre (§ 4 des conventions). Pour chaque chapitre : ce
qu'il doit établir ; l'état de la matière dans le dépôt.

1. **Présentation** (type : cadre). L'objet en une phrase ; la carte des dispositifs et
   institutions (texte fondateur, date d'application, où lire) ; une figure de ce que pèse
   l'ensemble (transferts du budget aux agences + fonds spéciaux) ; le plan ; les conventions de
   lecture ; le tableau de voisinage (§ 2 ci-dessus) ; une frise des dates clés sur un seul axe
   (création ONAS 1974, refonte 1993, ANPE 1988, APAL 1995, FODEP 1993, taxe 2003, ANGed 2005 —
   dates reprises des textes lus ou des intitulés, la frise distinguant les deux).
   *Matière* : partielle ; la frise est faisable dès maintenant pour l'ONAS (textes lus), par
   intitulé pour les agences.
2. **Les institutions et la tutelle** (type : institution, ou carte d'institutions). Ce qu'il doit
   établir : qui fait quoi — ministère chargé de l'environnement (dont le périmètre a varié :
   « Environnement et Aménagement du territoire » en 1993, « Affaires locales et Environnement »
   en 2018-2020 d'après les textes lus aux finances locales), ANPE-environnement, ANGed, ONAS
   (l'APAL est **hors du livre**, A3 — mentionnée en voisinage, § 2) — avec, pour chacune,
   naissance, statut, ressources, et ce que le budget lui verse.
   *Textes fondateurs* : loi n° 93-41 (ONAS) **lue** (registre des entreprises publiques) ; loi
   n° 88-91 (ANPE), loi n° 95-72 (APAL), décret n° 2005-2317 (ANGed) **connus par leur intitulé, à
   lire** (ils n'apparaissent dans le dépôt que par la note `finances-locales-competences.md`,
   d'après Dafflon et Gilbert). Aucune rupture ne peut être posée sur ces trois textes avant
   lecture.
3. **La dépense publique d'environnement sur la longue période** (type : longue période du livre,
   budgétaire seul). Ce qu'il doit établir : budget du ministère, transferts aux agences, fonds
   spéciaux, sur la plus longue série constructible ; familles de chiffres séparées, ruptures de
   périmètre ministériel marquées.
   *Matière* : à constituer entièrement (questions Q3-Q4). Les transferts à l'ONAS 2017-2022
   existent déjà (fiches LF, entrepôt).
4. **L'assainissement** (type : dispositif). Ce qu'il doit établir : le service, qui y a droit et
   qui paie ; les redevances d'assainissement comme épine (1975 → 2001 → 2022, trois textes déjà
   lus) ; la participation des riverains ; le financement public (subvention d'exploitation,
   garanties, part FCCL historique) ; ce que couvre la redevance et ce que couvre le budget.
   *Matière* : la plus avancée du livre — textes et chiffres déjà au registre ONAS des entreprises
   publiques ; série du tarif par tranche à construire (les arrêtés de taux entre 2001 et 2022
   ne sont pas lus : candidats à lecture, Q2).
5. **Les déchets** (type : dispositif). Ce qu'il doit établir : le partage commune (collecte,
   décharges contrôlées — code des collectivités locales, lu) / ANGed (texte à lire) ; les flux :
   redevance communale des déchets non ménagers (lue, finances locales), transferts éventuels à
   l'ANGed (à établir), taxes douanières liées aux déchets (lues, renvoi).
   *Matière* : faible hors finances locales ; chapitre impossible à écrire avant la note
   documentaire sur l'ANGed.
6. **La dépollution et les fonds** (type : dispositif). Ce qu'il doit établir : le fonds de
   dépollution — création (LF 1993, art. 35-37, à lire), ressources (taxe de 2003, lue au livre de
   la fiscalité, renvoi), **emplois** (primes, FODEP comme guichet : à documenter) ; les
   avantages du code d'incitation (tableau court, données déjà au chapitre des régimes
   d'incitation) ; le fonds de la protection et de l'esthétique de l'environnement (intitulé seul,
   à lire).
   *Matière* : le prélèvement est documenté, l'emploi ne l'est pas — c'est l'apport propre du
   livre.
7. **Rapports et études** (type : rapports et études, chacun avec sa méthode). Candidats déjà
   catalogués dans `tunisia-data` : rapports de la Cour des comptes (ONAS : rapport 2014, rapport
   sur les eaux usées, 28e rapport ; catalogue `cour-des-comptes-transport-eau-habitat.md`) ;
   Banque mondiale (CCDR Tunisie 2023, diagnostic infrastructure 2019, PER 2020 — à vérifier pour
   leurs chapitres environnement). Le budgétaire ne s'y mêle pas.
8. **Glossaire et annexes**. Entrées attendues : onas (existe déjà), anged, apal,
   anpe-environnement (désambiguïsée), fonds-de-depollution, redevance-assainissement,
   taxe-protection-environnement (existe déjà : `#g-taxe-protection-environnement`).

Chapitres de dispositif (4, 5, 6) : prévoir la section « Ce qu'en dit l'économie » (fiches
`docs/notes/eco-assainissement.md`, `eco-dechets.md`, `eco-depollution.md`, à demander au rôle
économiste le moment venu — tarification de l'assainissement, redevances déchets, taxes sur la
pollution : littérature classique, aucune fiche n'existe).

## 4. Questions au documentaliste

- **Q1 — Textes fondateurs des agences** : loi n° 88-91 (ANPE), loi n° 95-72 (APAL), décret
  n° 2005-2317 (ANGed) — à localiser au JORT, lire les articles de mission et de ressources.
  Même question pour le texte qui organise le ministère chargé de l'environnement (aucun décret
  d'organisation n'est cité dans le dépôt).
- **Q2 — Série du tarif d'assainissement** : les arrêtés fixant les taux des redevances entre le
  décret n° 2001-2001 et l'arrêté de 2022 ne sont pas lus ; existe-t-il, comme pour le prix de
  l'eau SONEDE, une série d'arrêtés dans `jort_cache.db` ?
- **Q3 — Budget du ministère de l'environnement** : les lois de finances donnent-elles une ligne
  continue, malgré les changements de rattachement (environnement seul, affaires locales et
  environnement…) ? Depuis quand le département existe-t-il ?
- **Q4 — Fonds spéciaux au tableau A** : le fonds de dépollution et le fonds de la protection et
  de l'esthétique de l'environnement y figurent-ils avec recettes et dépenses, année par année ?
  (La LF 1993, art. 35-37, et le texte du second fonds sont à lire — reprendre le TODO existant
  du chapitre des taxes affectées : LF 2003 à relire à l'image, extensions 2005-2018 à lire.)
- **Q5 — Emplois du FODEP** : textes d'application (conditions d'octroi des primes de
  dépollution), rapports d'exécution ; le chapitre des régimes d'incitation donne des montants de
  prime — d'où viennent-ils en amont et existe-t-il une série longue ?
- **Q6 — ANGed et communes** : qui paie quoi pour les décharges contrôlées ? (Le code des
  collectivités locales donne la collecte « jusqu'aux décharges contrôlées » aux communes ;
  l'aval n'est documenté nulle part.)
- **Q7 — Dans `tunisia-data`** : déjà catalogués et mobilisables — fiches ONAS des rapports sur
  les entreprises publiques (série `entreprises-publiques-fiches-entreprises`), rapports Cour des
  comptes (ONAS 2014, eaux usées, 28e rapport), BM CCDR 2023 / infrastructure 2019 / PER 2020.
  À chercher : rapports annuels ONAS et ANGed, statistiques déchets (ANGed ou INS), comptes de
  l'APAL. Lire d'abord `sources/` avant toute chasse web.

## 5. Risques et arbitrages

- **R1 — Périmètre eau et énergie.** Le risque principal du livre est l'enflure : « environnement »
  peut aspirer l'eau (SONEDE, irrigation, barrages) et le climat-énergie (FTE, renouvelables).
  Proposition : le livre ne prend que l'aval de l'eau (eaux usées) et ne touche pas à l'énergie ;
  tout le reste est une ligne du tableau de voisinage. À faire trancher par la revue humaine
  avant la première note documentaire.
- **R2 — ONAS : institution ou service.** La matière ONAS vit aux entreprises publiques (statut,
  comptes) et c'est conforme à la règle de domicile. Mais les **redevances d'assainissement** —
  tarif d'un service public, payé par les ménages, avec structure redistributive par tranches —
  sont un dispositif sectoriel : à la création du livre, elles devraient y déménager, la section
  ONAS gardant une phrase et un lien. Variante à écarter : les ranger à la compensation comme
  « tarif administré » — la compensation ne traite pas l'eau et son livre est organisé autour de
  la Caisse générale de compensation, qui n'intervient pas ici. **Tranché (A1, 11/11/2026) : les
  redevances d'assainissement déménagent dans ce livre** ; le déménagement suivra la procédure du
  chantier (registre de destination, aucune ligne « supprimé »).
- **R3 — Le rang « en dernier » est justifié par les dépendances.** Le livre reçoit presque toute
  sa matière de livres déjà écrits : fiscalité (taxes affectées, incitations, douane), entreprises
  publiques (ONAS), finances locales (communes). Ces chapitres existent et sont stables ; ce qui
  manque est ce qui n'existe nulle part (agences, emplois des fonds, budget du ministère) — un
  travail documentaire entier. Écrire ce livre avant le transport et le logement n'apporterait
  rien qu'un recopiage ; l'écrire en dernier permet de ne produire que l'apport propre. Le rang
  arrêté par le chantier est donc confirmé.
- **R4 — Risque de livre-catalogue.** Si les emplois des fonds et les budgets des agences restent
  introuvables, le livre se réduirait à des renvois vers les trois livres de flux. Critère de
  lancement proposé : ne pas ouvrir le chantier avant que les questions Q1, Q3 et Q4 aient reçu
  une réponse au moins partielle — sinon le livre n'a pas d'épine budgétaire propre.
- **R5 — Sigle ANPE.** Voir la mise en garde de tête ; une entrée de glossaire et une convention
  d'écriture s'imposent dès le premier chapitre.

## Reports et lacunes signalés par cette fiche

- Aucun texte fondateur d'agence (ANPE, ANGed, APAL) n'est lu dans le dépôt ; tout est « intitulé
  seul ». — à verser au backlog lors de l'ouverture du chantier, pas avant (livre non ouvert).
- Le TODO existant du chapitre des taxes affectées (LF 2003 à relire à l'image, LF 1993 art. 35-37
  à lire, extensions 2005-2018) conditionne aussi ce livre ; il est déjà au backlog de la
  fiscalité, ne pas le dupliquer.
- Les fiches économiste (assainissement, déchets, dépollution) n'existent pas.
