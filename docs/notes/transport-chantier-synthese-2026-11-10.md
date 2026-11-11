# Synthèse du chantier « Livre transport » — instruction documentaire

Point d'arrêt, 10 novembre 2026. Branche `chantier/transport-livre`. Ce chantier **instruit, ne
publie pas** : aucun `.qmd`, aucun commit, ni PR ni issue. Il répond aux questions au
documentaliste du § 4 de la fiche de plan (`docs/notes/transport-plan-livre.md`) et prépare les
arbitrages du § 5, qui restent à trancher par le propriétaire avant tout lancement de volume.

## 1. Notes documentaires versées (cinq tickets)

| Ticket | Note | Objet | État |
|---|---|---|---|
| T1 | `transport-organisation-terrestre-2026-11-10.md` (502 l.) | Lois 85-77 (1985) et de 2004 sous l'angle **organisation** (autorisation, concessions, opérateurs) ; modificatifs ; régime d'opérateur 2025 ; abrogation 2025 du transport régional (→ finances locales) | sourcé ; loi 1985 par **OCR** à contrôler à l'image |
| T2 | `transport-institution-tutelle-2026-11-10.md` (543 l.) | Filiation des ministères Transport / Équipement-Habitat ; carte des agences et offices (tutelle, texte de création) ; programmes GBO | sourcé ; décrets d'organisation récents à compléter |
| T3 | `transport-infrastructure-routiere-2026-11-10.md` (478 l.) | Fonds de développement des autoroutes 1999-2018 ; programme autoroutier d'avant 1995 ; route au budget ; recense l'existant EP (34 ancres `#r-ep-autoroutes-*`) sans le re-sourcer | sourcé ; éclaire l'arbitrage 2 |
| T4 | `transport-depense-longue-periode-2026-11-10.md` (472 l.) | Crédits missions Transport (2012-2024) et Équipement (2014-2024), transferts, investissement, part du PIB | sourcé ; trous = avant-GBO, exécution 2024-2026 |
| T5 | `transport-contrats-programmes-2026-11-10.md` (283 l.) | Dernier contrat-programme **par acteur** (relevé PAP 2024), base juridique, cahier des charges SNCFT (renvoi) | sourcé ; réalisation à collecter |

Garde-fous tenus : aucune modification de `precis/glossaire.yml`, `docs/notes/backlog-precis.md`,
`precis/ar/` ni `recherches.yml` ; frontières de domicile respectées (compensation ; entreprises
publiques → une phrase + un lien, jamais la prose).

## 2. Ce que la matière apporte aux arbitrages du § 5

- **Arbitrage 2 — déménager ou non les registres concessions / péages / garanties.** T3 confirme
  que tout le dispositif juridique (concession, péage, 8 garanties 1999-2012) est **déjà écrit et
  ancré** dans la section Tunisie Autoroutes des EP. Le fonds de développement des autoroutes
  (1999-2018) et le programme d'avant 1995 sont, eux, de la **politique sectorielle** sans domicile
  actuel : ils sont le vrai apport propre du chapitre routier. Variante prudente recommandée par la
  fiche (renvoi par liens tant que le chapitre n'est pas écrit) reste la plus sûre : la règle du
  domicile unique interdit la duplication des ancres existantes.
- **Arbitrage 3 — opportunité d'un chapitre aérien et maritime.** La matière **a grossi** à la
  lecture du PAP 2024 : contrats-programmes signés pour **SONOTRAK** (Kerkennah, oct. 2022) et la
  **Société du port d'Enfidha** (contrat de performance GBO 2022-2025, décret 2018-1006) ; OACA et
  OMMP identifiés (OMMP sans contrat-programme). Un chapitre aérien/maritime devient défendable, à
  condition de relever les budgets 2022-2026 de ces fiches (report T4/T5).
- **Arbitrage 4 — épaisseur du livre.** Entre l'infrastructure (fonds, programme routier,
  investissement Équipement ~85 % de la mission), les contrats-programmes par acteur et la dépense
  longue période 2012-2024, la matière propre existe et dépasse le « livre mince » redouté. L'apport
  reste la **réorganisation** (carte, voisinage, dépense longue période), conforme au chantier.

## 3. Lacunes et reports (à router — non écrits dans `backlog-precis.md`)

Chaque note porte sa section « Backlog » et « Lacunes ». Principaux reports :

- **OCR / lecture à l'image** : loi 85-77 relue par OCR (T1) à contrôler ; annuaires INS
  SNCFT/métro 1995-2023 (colonnes à vérifier à l'image, déjà noté dans `tunisia-data`).
- **Séries budgétaires** : avant-GBO (Transport < 2012, Équipement < 2014) ; exécution 2024-2026
  (RAP non collectés) ; cohérence des nomenclatures (loi organique 2019, renommage « Transport et
  logistique ») — T4.
- **Textes d'organisation récents** des ministères Transport (après 2016) et Équipement (après
  2018) ; création SPROLS — T2.
- **Contrats-programmes** : texte instituant le régime à confirmer ; réalisation (RAP, rapports
  d'activité) ; budgets 2022-2026 de SONOTRAK, Enfidha, OACA, OMMP — T5.
- **Infrastructure** : ressources/emplois du fonds autoroutier à détailler ; investissement routier
  longue période ; programme autoroutier d'avant 1995 (recherche à ce jour bredouille) — T3.

## 4. Fiches `docs/recherches.yml` proposées (à verser après relecture)

Les fiches rejouables sont rédigées complètes dans les notes (requêtes réellement lancées, passe
datée, couverture) mais **non écrites dans `recherches.yml`** pour éviter les conflits entre
chantiers parallèles. À intégrer en une passe, à la relecture :

- T1 : `r-transport-decrets-application-organisation` ; fiche d'organisation du transport terrestre.
- T2 : `r-transport-organisation-ministere-apres-2016`, `r-equipement-organisation-ministere-apres-2018`,
  `r-sprols-creation`, `r-transport-gbo-nomenclature-2015-2024`.
- T3 : `r-autoroutes-programme-avant-1995`, `r-fonds-autoroutes-ressources-emplois`,
  `r-investissement-routier-longue-periode`.
- T4 : `r-transport-decret-manque-a-gagner` ; relier l'existante `r-transport-ligne-budgetaire-1995-2002`.
- T5 : `r-transport-contrat-programme-base`, `r-transport-execution-rap-2024-2026`.

## 4 bis. Décisions du propriétaire (10 novembre 2026)

Arbitrages du § 5 tranchés :

- **Arbitrage 2 — registres concessions / péages / garanties : OK (variante prudente).** On **ne déménage pas** les registres hors de la section Tunisie Autoroutes des entreprises publiques ; le livre transport **renvoie par liens** vers les ancres `#r-ep-autoroutes-*`. L'apport propre du chapitre routier reste le **fonds de développement des autoroutes** (1999-2018), le **programme d'avant 1995**, la **route au budget** et l'**investissement** (mission Équipement).
- **Arbitrage 3 — aérien et maritime : OK pour un chapitre dédié.** La matière (contrats-programmes SONOTRAK et port d'Enfidha 2022, OACA, OMMP) justifie un chapitre « L'aérien et le maritime », non une simple section de la dépense. Report associé : relever les budgets 2022-2026 de SONOTRAK (p. 185), Enfidha, OACA, OMMP (PAP 2024).
- **Arbitrage 4 — épaisseur du livre : pas un obstacle.** Le volume se fait ; son apport assumé est la réorganisation.

Non tranché restant : l'**ordre des travaux** (§ 5-5 — cadre des finances publiques et éducation avant le transport) ; la rédaction `.qmd` n'est pas ouverte.

## 4 ter. Collecte ciblée réalisée (G1-G4, 10 novembre 2026)

Quatre compléments versés, chacun en fin de sa note parente (fichiers distincts) :

- **G1 — budgets longue période** (→ note T4). Trouvaille : les **budgets du ministère pré-GBO** déjà dans l'entrepôt rouvrent **2011-2013** (crédits totaux par titre, Transport et Équipement). **Famille distincte** des missions GBO : à ne PAS chaîner (périmètre ministère ≠ mission, écart ~4 % utilisé comme contrôle, pas comme raccord) ; rupture dès 2014 (fusions ministérielles). Trou avant 2011 laissé honnête (portail ancien ne descend qu'à l'édition 2013).
- **G2 — budgets aérien/maritime 2022-2026** (→ note T5). Relevé par acteur (SONOTRAK, OMMP…) du PAP 2024, unités et pages notées ; incohérence de la source signalée (SONOTRAK 2026 : total imprimé ≠ somme, écart +20).
- **G3 — organisation récente des ministères** (→ note T2). **Confirmé** : aucun décret d'organisation *central* du Transport après 2016-97 ni de l'Équipement après 2018-883 ; seuls des textes périphériques récents. La « lacune » supposée est levée.
- **G4 — contrôle à l'image de la loi 85-77** (→ note T1). OCR de T1 **fidèle** (23 articles, 6 titres, autorisation centralisée art. 11), vérifié **FR et AR** ; le fascicule a bien une couche texte et la loi est **bilingue** au JORT 1985 — la réserve « citation à contrôler » tombe.

Aucun fichier interdit touché ; rien re-téléchargé ni commité.

## 4 quater. Chapitre « Rapports et études » instruit (R1-R2, 10 novembre 2026)

La dernière tranche de collecte est bouclée ; famille « rapport extérieur », tenue séparée du
budgétaire ; chaque source avec sa méthode.

- **R1 — Cour des comptes** (`transport-rapports-cour-des-comptes-2026-11-10.md`) : trois rapports
  exploités — contrôle de l'État sur le transport terrestre (2008, 23ᵉ rapport annuel), ministère
  du Transport (2016), **SNTRI (2017, jusqu'ici non exploité, désormais lu)** ; observations
  sectorielles seulement (les comptes d'opérateur restent aux EP).
- **R2 — Banque mondiale** (`transport-rapports-bm-livre-blanc-2026-11-10.md`) : *Livre blanc
  transports et logistique* (2016, n° ACS18045), PDF localisé dans l'entrepôt ; méthode relevée,
  constats distingués des recommandations ; voisin *Infrastructure Diagnostic* (2019) tenu séparé.

**Le dossier documentaire du volume est complet** : les neuf chapitres du plan § 3 ont leur matière
sourcée. Il ne reste, avant rédaction, que la lecture d'« économie » (fiches `eco-*.md` par
l'économiste — aucune n'existe ; aucune évaluation d'incidence du poste transport trouvée) et
l'intégration éditoriale, qui se fait **au moment** d'ouvrir le livre.

## 5. Ce qui attend le propriétaire

1. **Arbitrages tranchés** (§ 4 bis) ; reste ouvert l'**ordre des travaux** (§ 5-5 : cadre des
   finances publiques et éducation **avant** le transport). Ce chantier n'a préparé que la collecte,
   pas la rédaction — la décision d'ouvrir le livre t'appartient.
2. Au lancement du livre, autoriser l'intégration : fiches `recherches.yml` (avec leurs ancres
   `.qmd`), lignes de backlog (via `archiviste-backlog`, sous un titre « Backlog » en corps de PR),
   références CSL candidates (via `bibliographe`), passes du glossaire (via `terminologue`).
3. Commander à l'**économiste** les fiches `eco-<dispositif>.md` du secteur (aucune n'existe).

Rien n'est commité ; aucune PR ni issue ouverte.
