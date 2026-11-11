# Note documentaire — Transport, chapitre « Institution et tutelle » (ticket T2)

Documentaliste, 10 novembre 2026. Chantier « Livre transport » (worktree
`chantier/transport-livre`). Cette note INSTRUIT ; elle ne rédige pas le précis et ne
touche à aucun `.qmd`, `glossaire.yml` ni `backlog-precis.md`. Les lignes de backlog
proposées sont rassemblées en fin de note sous « Backlog ».

**Règle de domicile appliquée.** Les comptes des opérateurs et de l'ATTT restent aux
entreprises publiques ; le tarif et sa compensation restent à la compensation. On ne
retient ici que ce que l'État **décide et organise** : les textes d'organisation des
ministères, la carte de tutelle des agences/offices (texte de création, mission, ministère
de tutelle — une ligne par organisme, sans comptes), et la structure des programmes
budgétaires GBO des missions « Transport » et « Équipement et Habitat ».

**Sources de la note.** (1) `jort_cache.db`
(`/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db`, 79 790 textes, publication
1956-01-03 → 2026-10-29) pour les décrets d'organisation et les lois de création, par
requêtes LIKE/FTS (titres non accentués dans la base) ; (2) les 47 PDF déjà catalogués dans
`tunisia-data/sources/ministere-transport-equipement-habitat.md` et son CSV, lus par
`pdftotext` pour la structure GBO (aucun re-téléchargement) ; (3) les `references.json`
existants des livres `entreprises_publiques` et `compensation`, pour distinguer les entrées
déjà présentes de celles à créer. La **référence PDF JORT** d'un décret se reconstruit par
le motif `pist.tn`/archive : chemin `pdf_fr` relevé dans `jort_cache` (ex.
`/jort/2014/2014F/Jo0092014.pdf`), à préfixer du domaine du dépôt JORT servi par le CI.

---

## A. Textes d'organisation des ministères (filiation)

### A.1 — Côté « Transport »

Le secteur des transports a longtemps partagé un ministère avec les **communications/PTT**,
avant de s'en détacher. Filiation relevée dans `jort_cache` (décrets d'organisation et
d'attributions, par ordre chronologique) :

| # | Texte | Date (sign. / JORT) | Objet | recid |
|---|---|---|---|---|
| 1 | Décret n° 76-719 | 1976-08-19 / JORT 1976 n° 54 | **organisation du ministère des transports et des communications** | 100923 |
| 2 | Décret n° 80-100 | 1980-01-23 | modifie et complète le décret 76-719 | 98956 |
| 3 | Décret n° 80-1084 | 1980-08-22 | transfert d'attributions au min. des transports et communications | 98639 |
| 4 | Décret n° 81-608 | 1981-05-09 / JORT 1981 n° 33 | **organisation du ministère des transports et des communications** (refonte) | 98196 |
| 5 | Décrets n° 82-750, 82-1363, 84-222, 84-583 | 1982-1984 | modifient le décret 81-608 | 97498, 97241, 96568, 96455 |
| 6 | Décret n° 86-863 | 1986-09-15 / JORT 1986 n° 52 | **fixant les attributions du ministère du transport** (le transport apparaît seul) | 95261 |
| 7 | Décret n° 91-86 | 1991-01-14 / JORT 1991 n° 8 | **organisation des services centraux du ministère du transport** | 93033 |
| 8 | Décret n° 94-135 | 1994-01-17 / JORT 1994 n° 8, p. 177-179 | attributions et organisation des **directions régionales** du min. du transport | 91577 |
| 9 | **Décret n° 2014-409** | 2014-01-16 / JORT 2014 n° 9, p. 294-295 | **fixant les attributions du ministère du transport** (texte d'attributions en vigueur) | 79082 |
| 10 | **Décret n° 2014-410** | 2014-01-16 / JORT 2014 n° 9, p. 295-318 | **organisation des services centraux du ministère du transport** (texte d'organigramme en vigueur) | 79083 |
| 11 | Décret gouvernemental n° 2016-97 | 2016-01-11 / JORT 2016 n° 7 | modifie le décret 2014-410 (révision de l'organigramme) | 78243 |

Lecture : l'ossature actuelle du **ministère du Transport** repose sur le couple
**décret 2014-409 (attributions) + décret 2014-410 (organisation des services centraux)**,
le second révisé une fois (2016-97). Avant 2014, les attributions dataient de 1986 (86-863)
et l'organigramme de 1991 (91-86). Aucun décret d'organisation ou d'attributions postérieur
à 2016 n'est trouvé dans `jort_cache` au 29 octobre 2026 pour ce ministère : le libellé
« ministère du Transport et de la Logistique » employé dans les PAP 2021-2024 ne s'appuie
sur aucun nouveau décret d'organisation repéré (à confirmer — fiche R2 ci-dessous).

### A.2 — Côté « Équipement » (et Habitat)

Le ministère de l'Équipement descend du **ministère des travaux publics** (décret
d'attributions 70-46 et d'organisation 70-115, 1970), devenu ministère de l'Équipement
(1974-1975), puis de l'Équipement **et de l'Habitat** (1988), avec un détachement récurrent
de l'**Aménagement du territoire** et de l'**Environnement**.

| # | Texte | Date (sign. / JORT) | Objet | recid |
|---|---|---|---|---|
| 1 | Décret n° 70-46 | 1970-02-14 / JORT 1970 n° 8 | **attributions du ministère des travaux publics** | 103822 |
| 2 | Décret n° 70-115 | 1970-04-06 / JORT 1970 n° 18 | **organisation du ministère des travaux publics** | 103784 |
| 3 | Décret n° 74-93 | 1974-02-15 / JORT 1974 n° 13 | **attributions du ministère de l'équipement** | 102426 |
| 4 | Décret n° 75-397 | 1975-05-30 / JORT 1975 n° 43 | **organisation du ministère de l'équipement** | 101644 |
| 5 | Décrets n° 78-153, 78-1081 | 1978 | modifient/complètent le décret 75-397 | 100009, 99509 |
| 6 | **Décret n° 88-1413** | 1988-07-22 / JORT 1988 n° 52, p. 1112-1122 | **organisation du ministère de l'équipement et de l'habitat** (texte-socle, toujours en vigueur) | 94297 |
| 7 | Décret n° 92-248 | 1992-02-03 / JORT 1992 n° 10 | complète les attributions (décret 74-93) | 92564 |
| 8 | Décret n° 92-249 | 1992-02-03 / JORT 1992 n° 10, p. 203 | complète et modifie l'organisation (décret 88-1413) | 92565 |
| 9 | Décret n° 2008-121 | 2008-01-16 / JORT 2008 n° 7, p. 529-530 | modifie et complète le décret 88-1413 | 82976 |
| 10 | Décret n° 2008-512 | 2008-02-25 / JORT 2008 n° 19, p. 857-860 | attributions et organisation des **directions régionales** du min. de l'équipement, de l'habitat et de l'aménagement du territoire | 82914 |
| 11 | Décret n° 2015-1766 | 2015-11-09 / JORT 2015 n° 91, p. 2712-2713 | modifie le décret 2008-512 (directions régionales) | 78342 |
| 12 | Décret gouvernemental n° 2018-883 | 2018-10-24 / JORT 2018 n° 87 | complète le décret 88-1413 | 76715 |

Lecture : l'organisation du **ministère de l'Équipement et de l'Habitat** reste fondée, en
2026, sur le **décret 88-1413 de 1988**, modifié/complété en 1992, 2008 et 2018 — remarquable
longévité par rapport au transport, refondé en 2014. Les **directions régionales** relèvent
d'un texte distinct (2008-512, modifié 2015-1766). Aucun décret de refonte complète postérieur
à 1988 n'est trouvé ; les intitulés récents « ministère de l'Équipement, de l'Habitat et de
l'Infrastructure » des PAP/budgets 2021-2024 ne correspondent à aucun nouveau décret
d'organisation repéré (fiche R2).

### A.3 — Voisins détachés (pour mémoire, hors domicile transport)

- **Environnement et aménagement du territoire** : décret n° 93-303 (attributions) et
  93-304 (organisation), 1993-02-01 — détachement de l'Environnement. Les missions
  « Environnement » et « Affaires locales et environnement » apparaissent comme missions GBO
  distinctes dans les PAP catalogués (fiche `tunisia-data`), hors périmètre transport.
- **Tourisme et aménagement du territoire** : décret n° 70-225, 1970-06-26 (recid 103707) —
  pour mémoire sur la circulation de l'« aménagement du territoire » entre ministères.

---

## B. Carte des agences et offices du secteur (texte de création, mission, tutelle)

Une ligne par organisme. **Les comptes restent aux entreprises publiques** ; ne figurent ici
que le texte fondateur, la mission et le ministère de tutelle. La colonne « déjà en réf. »
indique si le texte de création est déjà catalogué dans un `references.json` du précis.

### B.1 — Sous tutelle du ministère du Transport

| Organisme | Texte de création | Mission (résumé d'intitulé) | Tutelle | Déjà en réf. ? |
|---|---|---|---|---|
| **ATTT** — Agence technique des transports terrestres | **Loi n° 98-108 du 28 déc. 1998** (relative à l'ATTT) ; décret d'application 98-1375 du 30 juin 1998 | immatriculation, visite technique, titres de transport terrestre (perçoit des droits → institution EP) | Transport | oui (`loi98-108-attt`, `decret98-1375-attt`, EP) |
| **OACA** — Office de l'aviation civile et des aéroports | **Loi n° 98-110 du 28 déc. 1998** ; décret 98-1374 du 30 juin 1998. Antécédent : **Office des ports aériens de Tunisie (OPAT), loi n° 70-30 du 3 juillet 1970** | gestion des aéroports et navigation aérienne civile | Transport | oui (`loi98-110-oaca`, `loi70-30-oaca`, `decret98-1374-oaca`, EP) |
| **OMMP** — Office de la marine marchande et des ports | **Loi n° 98-109 du 28 déc. 1998** ; décret 98-1385 du 30 juin 1998. Antécédent : **Office des ports nationaux, loi n° 65-2 du 12 février 1965** (mod. loi 72-5) | ports de commerce, marine marchande | Transport | oui (`loi98-109-ommp`, `loi65-2-ommp`, `loi72-5-ommp`, EP) |
| **SNCFT** — Société nationale des chemins de fer tunisiens | **Décret du 27 déc. 1956** approuvant les statuts ; loi n° 69-31 du 9 mai 1969 | exploitation du réseau ferré national | Transport | oui (`decret-1956-12-27-sncft`, `loi69-31-sncft`, EP) |
| **RFR** — Société du réseau ferroviaire rapide de Tunis | **Loi n° 2007-42 du 25 juin 2007** (autorisation de souscription au capital ; société créée dans ce cadre) | construction/exploitation du RFR du Grand Tunis | Transport | oui (`loi2007-42-rfr`, EP) |
| **Transtu** — Société des transports de Tunis | **Loi n° 2003-33 du 28 avril 2003** (fusion SNT + Société du métro-léger de Tunis) ; décret d'organisation 2003-2407 du 17 nov. 2003. Antécédents : **Société du métro-léger de Tunis, décret-loi n° 81-21 du 20 oct. 1981** (ratifié loi 82-2) ; **SNT, décret-loi n° 63-8 du 14 mars 1963** | transport public urbain du Grand Tunis (bus, métro léger, TGM) | Transport | oui (`loi2003-33-transtu`, `decret2003-2407-transtu`, `dl63-8-snt`, EP) |
| **SNTRI** — Société nationale de transport rural et interurbain | **Décret-loi n° 81-22 du 20 oct. 1981** (ratifié loi 82-3 ; mod. loi 90-54) | transport interurbain par route | Transport | partiel (texte cité en EP via réquisitions ; **création 81-22 à créer**) |
| **SMLS** — Société du métro léger de Sfax | **Décret n° 2015-957 du 23 juillet 2015** | métro léger de Sfax (projet, non encore exploité) | Transport | **non (à créer)** |
| **CTN** — Compagnie tunisienne de navigation | **Loi n° 59-34 du 16 mars 1959** (approbation des statuts) | transport maritime (passagers/fret) | Transport | partiel (EP cite la CTN ; **statuts 59-34 à créer**) |
| **Tunisair** ; **Tunisair Express** | (statuts/participations — domicile EP) | transport aérien | Transport | — (hors cette note) |
| **Sociétés régionales de transport (SRT)** — Soretras (Sfax), SRT Bizerte, Nabeul, Sahel, Kairouan, Médenine, Kasserine, Béja, Jendouba, Le Kef, Gabès, Gafsa | textes propres par société (ex. Soretras, autorisations d'emprunt des communes 1960-1963) | transport public régional de personnes | Transport | partiel (EP) |

Notes de filiation (aérien/maritime) : l'**OACA** prolonge l'**OPAT** de 1970 ; l'**OMMP**
réunit en 1998 les fonctions de l'**Office des ports nationaux** de 1965 et de la marine
marchande. L'**ATTT** perçoit des droits (visite technique, immatriculation) : conformément
au tableau de domicile, elle reste **institution des entreprises publiques**, citée ici pour
la seule tutelle. Autres établissements « sous tutelle » listés par l'ancien site
`transport.tn` (archive 2016, fiche `tunisia-data` § 1.4) : STT, SOTRAFER, SONOTRAK, STAM,
institut/école de formation maritime (INM) — à rattacher au besoin, hors budget propre.

### B.2 — Sous tutelle du ministère de l'Équipement et de l'Habitat

| Organisme | Texte de création | Mission (résumé) | Tutelle | Déjà en réf. ? |
|---|---|---|---|---|
| **Tunisie Autoroutes** (ex-STA) | Société concessionnaire ; **convention de concession approuvée par décret n° 95-720 du 17 avril 1995** ; capital : lois 99-50, 2002-96, 2006-3, 2010-57, 2019-75 | construction/exploitation du réseau autoroutier à péage | Équipement | oui (`decret95-720-autoroutes` et série autoroutes/péage, EP) |
| **AFH** — Agence foncière d'habitation | **Décret n° 74-33 du 21 janvier 1974** (organisation et fonctionnement) ; statut du personnel décret 75-585 ; missions redéfinies par décret gouvernemental 2021-327 | aménagement foncier pour l'habitat | Équipement | oui (`decret74-33`, `decret-gouv2021-327`, `loi87-28-afh`, EP) |
| **ARRU** — Agence de réhabilitation et de rénovation urbaine | **Loi n° 81-69 du 1er août 1981** | réhabilitation des quartiers, rénovation urbaine | Équipement | **non (à créer)** — l'ARRU figure en EP par ses comptes, mais la loi 81-69 n'y est pas cataloguée |
| **SNIT** — Société nationale immobilière de Tunisie | **Loi n° 57-19 du 10 sept. 1957** (approbation des statuts) ; apport initial loi 58-47 | promotion immobilière publique | Équipement | partiel (EP cite `loi61-29-snit` ; **statuts 57-19 à créer**) |
| **SPROLS** — Société de promotion des logements sociaux | (texte de création à identifier) | logement social | Équipement | **non (à identifier/créer)** — fiche R3 |
| **SOGEMT** (SOMATRA-GET) | (texte de création à identifier) | travaux/géotechnique | Équipement | **non** (hors cœur T2) |

### B.3 — Rattachement de tutelle à vérifier

- **AFH, ARRU, SPROLS, SNIT** : la fiche `tunisia-data` les classe « Équipement et Habitat »
  (PAP/RAP de la mission Équipement). Le glossaire du précis (entrée `caisse-...`, l. 7381)
  note que la caisse immobilière « relève de l'Équipement depuis 2010 » : les rattachements
  habitat ont bougé ; à dater précisément si le chapitre en a besoin.
- **APIP** — Agence des ports et des installations de pêche : **loi n° 92-32 du 7 avril 1992**
  (recid 113247). Tutelle **Agriculture/Pêche**, PAS transport : **exclue** du périmètre, notée
  pour écarter la confusion ports de commerce (OMMP) / ports de pêche (APIP).

---

## C. Programmes budgétaires GBO (missions Transport ; Équipement et Habitat)

Structure relevée à l'image/texte dans les PAP catalogués (`tunisia-data`, pas de
re-téléchargement). La nomenclature GBO tunisienne numérote les programmes opérationnels puis
range le pilotage/appui en dernier (parfois « programme 9 »).

### C.1 — Mission « Transport » (PAP 2021 et 2022, FR)

PAP 2021 (`gbo_2021-04_PAP_2021_Transport_et_logistique_0.pdf`, p. 19 sq.) : la mission
« comprend **quatre programmes, quatre sous-programmes, 15 activités, 14 objectifs
stratégiques et 29 indicateurs**, et 24 opérateurs publics ». Les quatre programmes :

| Programme | Intitulé | Opérateurs/contenu rattachés |
|---|---|---|
| Programme 1 | **Transport terrestre** | SNCFT, RFR, Transtu, SRT, SNTRI, métro de Sfax (ferroviaire + routier de personnes) |
| Programme 2 | **Aviation civile** | OACA, Tunisair, services météo |
| Programme 3 | **Transport maritime et portuaire** | OMMP, CTN, ports |
| Programme 4 | **Pilotage et appui** | administration centrale, encadrement, suivi des contrats-programmes |

Confirmé à l'identique par le PAP 2022 (`gbo_2022-03_version_PAP2022_Transportnv_(2).pdf`,
sommaire : I. transport terrestre ; II. aviation civile ; III. transport maritime et
portuaire ; IV. pilotage et appui). Le tableau budgétaire du PAP 2021 (p. ~37) donne, par
programme et par nature de dépense, les colonnes rémunérations / fonctionnement /
intervention / investissement (total mission 2021 ≈ 829 500 milliers de dinars hors
ressources propres des établissements — chiffre de structure, le détail chiffré reste au
chapitre « dépense »). La **logistique** est un axe transversal rattaché au transport
terrestre (zones logistiques, loi des zones logistiques annoncée dans le PAP 2022), sans
programme propre.

### C.2 — Mission « Équipement et Habitat » (PAP 2022, FR)

PAP 2022 MEH (`gbo_2022-04_PAP_2022__MEH_07_MARS_FR2204.pdf`, sommaire + chap. II) : « trois
programmes opérationnels et un programme de pilotage et d'appui » :

| Programme | Intitulé | Sous-programme(s) relevés |
|---|---|---|
| Programme 1 | **Infrastructure routière** | SP « central » + composantes régionales (route hors autoroute financée au budget) |
| Programme 2 | **Protection des zones urbaines, du littoral et maîtrise d'ouvrage** | SP 1 central « protection des zones… » |
| Programme 3 | **Aménagement, urbanisme et habitat** | AFH, ARRU, SNIT, SPROLS, FOPROLOS, programmes de logement ; coopération ONU-Habitat |
| **Programme 9** | **Pilotage et appui** | SP 1 central ; administration, suivi des EP |

Le numéro « 9 » du programme de pilotage (et non « 4 ») est la convention GBO employée côté
Équipement — à noter pour éviter une fausse incohérence avec la mission Transport (qui numérote
son appui « 4 »). La **route** financée au budget relève du **programme 1 (infrastructure
routière)** ; les **autoroutes à péage** passent par la concession (Tunisie Autoroutes) et non
par un sous-programme budgétaire — articulation à traiter au chapitre routier.

Réserve de cohérence inter-années : les PAP arabes 2015-2018 et 2024 n'ont pas été relus
programme par programme (couche texte partielle, cf. fiche `tunisia-data` § 1) ; la stabilité
de la nomenclature 2021-2022 est établie, son invariance sur 2015-2024 ne l'est pas (fiche R4).

---

## D. Références candidates (CSL-JSON)

### D.1 — À CRÉER (textes d'organisation des ministères — aucun n'est dans un `references.json`)

```json
[
  {
    "id": "decret2014-409-attributions-transport",
    "type": "legislation",
    "title": "Décret n° 2014-409 du 16 janvier 2014, fixant les attributions du ministère du transport",
    "issued": {"date-parts": [[2014, 1, 16]]},
    "authority": "République tunisienne",
    "references": "JORT n° 9 du 31 janvier 2014, p. 294-295",
    "citation-key": "decret2014-409-attributions-transport"
  },
  {
    "id": "decret2014-410-organisation-transport",
    "type": "legislation",
    "title": "Décret n° 2014-410 du 16 janvier 2014, portant organisation des services centraux du ministère du transport",
    "issued": {"date-parts": [[2014, 1, 16]]},
    "authority": "République tunisienne",
    "references": "JORT n° 9 du 31 janvier 2014, p. 295-318",
    "citation-key": "decret2014-410-organisation-transport"
  },
  {
    "id": "decret2016-97-organisation-transport",
    "type": "legislation",
    "title": "Décret gouvernemental n° 2016-97 du 11 janvier 2016, modifiant le décret n° 2014-410 du 16 janvier 2014 portant organisation des services centraux du ministère du transport",
    "issued": {"date-parts": [[2016, 1, 11]]},
    "authority": "République tunisienne",
    "references": "JORT n° 7 du 22 janvier 2016",
    "citation-key": "decret2016-97-organisation-transport"
  },
  {
    "id": "decret88-1413-organisation-equipement",
    "type": "legislation",
    "title": "Décret n° 88-1413 du 22 juillet 1988, portant organisation du ministère de l'équipement et de l'habitat",
    "issued": {"date-parts": [[1988, 7, 22]]},
    "authority": "République tunisienne",
    "references": "JORT n° 52 du 2 août 1988, p. 1112-1122",
    "citation-key": "decret88-1413-organisation-equipement"
  },
  {
    "id": "decret2008-121-organisation-equipement",
    "type": "legislation",
    "title": "Décret n° 2008-121 du 16 janvier 2008, modifiant et complétant le décret n° 88-1413 du 22 juillet 1988 portant organisation du ministère de l'équipement et de l'habitat",
    "issued": {"date-parts": [[2008, 1, 16]]},
    "authority": "République tunisienne",
    "references": "JORT n° 7 du 22 janvier 2008, p. 529-530",
    "citation-key": "decret2008-121-organisation-equipement"
  },
  {
    "id": "decret2018-883-organisation-equipement",
    "type": "legislation",
    "title": "Décret gouvernemental n° 2018-883 du 24 octobre 2018, complétant le décret n° 88-1413 du 22 juillet 1988 portant organisation du ministère de l'équipement et de l'habitat",
    "issued": {"date-parts": [[2018, 10, 24]]},
    "authority": "République tunisienne",
    "references": "JORT n° 87 du 30 octobre 2018",
    "citation-key": "decret2018-883-organisation-equipement"
  },
  {
    "id": "decret2008-512-directions-regionales-equipement",
    "type": "legislation",
    "title": "Décret n° 2008-512 du 25 février 2008, fixant les attributions et l'organisation des directions régionales du ministère de l'équipement, de l'habitat et de l'aménagement du territoire",
    "issued": {"date-parts": [[2008, 2, 25]]},
    "authority": "République tunisienne",
    "references": "JORT n° 19 du 4 mars 2008, p. 857-860",
    "citation-key": "decret2008-512-directions-regionales-equipement"
  }
]
```

Candidats secondaires (filiation, à créer seulement si le chapitre les cite) :
décret 76-719 (recid 100923), décret 81-608 (98196), décret 86-863 (95261), décret 91-86
(93033), décret 94-135 (91577, JORT 1994 n° 8 p. 177-179), décret 70-115 (103784),
décret 75-397 (101644), décret 74-93 (102426), décret 2015-1766 (78342, JORT 2015 n° 91
p. 2712-2713), décret 93-303/93-304 (environnement).

### D.2 — À CRÉER (agences dont le texte de création manque dans les `references.json`)

```json
[
  {
    "id": "loi81-69-arru",
    "type": "legislation",
    "title": "Loi n° 81-69 du 1er août 1981, portant création de l'agence de réhabilitation et de rénovation urbaine",
    "issued": {"date-parts": [[1981, 8, 1]]},
    "authority": "République tunisienne",
    "citation-key": "loi81-69-arru"
  },
  {
    "id": "dl81-22-sntri",
    "type": "legislation",
    "title": "Décret-loi n° 81-22 du 20 octobre 1981, portant création de la société nationale de transport rural et interurbain",
    "issued": {"date-parts": [[1981, 10, 20]]},
    "authority": "République tunisienne",
    "note": "Ratifié par la loi n° 82-3 du 3 février 1982 ; modifié par la loi n° 90-54 du 30 mai 1990.",
    "citation-key": "dl81-22-sntri"
  },
  {
    "id": "dl81-21-metro-tunis",
    "type": "legislation",
    "title": "Décret-loi n° 81-21 du 20 octobre 1981, portant création de la « Société du métro-léger de Tunis »",
    "issued": {"date-parts": [[1981, 10, 20]]},
    "authority": "République tunisienne",
    "note": "Ratifié par la loi n° 82-2 du 3 février 1982 ; antécédent de Transtu (fusion 2003, loi 2003-33).",
    "citation-key": "dl81-21-metro-tunis"
  },
  {
    "id": "decret2015-957-metro-sfax",
    "type": "legislation",
    "title": "Décret n° 2015-957 du 23 juillet 2015, portant création de la société du métro léger de Sfax",
    "issued": {"date-parts": [[2015, 7, 23]]},
    "authority": "République tunisienne",
    "citation-key": "decret2015-957-metro-sfax"
  },
  {
    "id": "loi59-34-ctn",
    "type": "legislation",
    "title": "Loi n° 59-34 du 16 mars 1959, approuvant les statuts de la « Compagnie tunisienne de navigation » et autorisant l'État à souscrire au capital",
    "issued": {"date-parts": [[1959, 3, 16]]},
    "authority": "République tunisienne",
    "citation-key": "loi59-34-ctn"
  },
  {
    "id": "loi57-19-snit",
    "type": "legislation",
    "title": "Loi n° 57-19 du 10 septembre 1957, portant approbation des statuts de la société nationale immobilière de Tunisie (S.N.I.T.)",
    "issued": {"date-parts": [[1957, 9, 10]]},
    "authority": "République tunisienne",
    "citation-key": "loi57-19-snit"
  },
  {
    "id": "loi92-32-apip",
    "type": "legislation",
    "title": "Loi n° 92-32 du 7 avril 1992, portant création de l'agence des ports et des installations de pêche",
    "issued": {"date-parts": [[1992, 4, 7]]},
    "authority": "République tunisienne",
    "note": "Tutelle Agriculture/Pêche — hors périmètre transport ; cité pour distinguer ports de pêche (APIP) et ports de commerce (OMMP).",
    "citation-key": "loi92-32-apip"
  }
]
```

### D.3 — DÉJÀ PRÉSENTES (ne pas recréer ; réutiliser la clé)

Dans `precis/fr/entreprises_publiques/references.json` : `loi98-108-attt`,
`decret98-1375-attt`, `loi98-110-oaca`, `loi70-30-oaca`, `decret98-1374-oaca`,
`loi98-109-ommp`, `loi65-2-ommp`, `loi72-5-ommp`, `decret-1956-12-27-sncft`,
`loi69-31-sncft`, `loi2007-42-rfr`, `loi2003-33-transtu`, `decret2003-2407-transtu`,
`dl63-8-snt`, `decret95-720-autoroutes`, `decret74-33` (AFH), `decret-gouv2021-327` (AFH),
`loi87-28-afh`, `loi61-29-snit`, et les séries autoroutes/péage/garanties.
Dans `precis/fr/compensation/references.json` : `loi85-77` (organisation des transports
terrestres, 1985), `loi2004-33` (organisation des transports terrestres, 2004) — **candidats
à relire sous l'angle « organisation »** comme le demande le plan, § 4.

### D.4 — Note de domicile (rappel pour `/rediger`)

Les clés `…-attt`, `…-oaca`, `…-ommp`, `…-sncft`, `…-transtu`, `…-autoroutes`, etc.
vivent dans le livre **entreprises publiques** : le livre transport les **cite par lien**
(tutelle, mission) sans importer les comptes. Les décrets **D.1** (organisation des
ministères) sont, eux, propres au livre transport — ils n'ont de domicile nulle part ailleurs.

---

## E. Notions à glossaire (vérifier / proposer — ne rien écrire dans `glossaire.yml`)

| Terme FR | AR pressenti | Source canonique pressentie | État |
|---|---|---|---|
| Mission (budgétaire) | مهمة | loi organique du budget n° 2019-15 ; PAP | **absent** du glossaire — à proposer |
| Programme / sous-programme (GBO) | برنامج / برنامج فرعي | loi organique 2019-15 ; PAP | **absent** — à proposer |
| Gestion du budget par objectifs (GBO) | التصرف في الميزانية حسب الأهداف | portail `gbo.tn` ; loi organique 2019-15 | **absent** — à proposer |
| Projet annuel de performance (PAP) / Rapport annuel de performance (RAP) | المشروع السنوي للأداء / التقرير السنوي للأداء | PAP/RAP catalogués | **absent** — à proposer |
| Contrat-programme | عقد برنامج | déjà au glossaire (`contrat-programme`, l. 7197) sous l'angle sécurité sociale | **présent** — étendre la portée au secteur transport (opérateurs) |
| Tutelle | إشراف / سلطة إشراف | décrets d'organisation | notion déjà employée (l. 7197, 7381) — pas d'entrée propre |
| Agence technique des transports terrestres (ATTT) | الوكالة الفنية للنقل البري | loi 98-108 | domicile EP ; entrée pressentie côté EP |
| Réseau ferroviaire rapide (RFR) | الشبكة الحديدية السريعة | loi 2007-42 | domicile EP ; entrée pressentie |

L'économiste et l'architecte trancheront l'opportunité d'entrées GBO génériques (elles
serviraient à tous les livres sectoriels) plutôt que propres au transport.

---

## F. Lacunes (TODO — ne rien inventer)

1. **Intitulé officiel récent des ministères.** Les PAP/budgets 2021-2024 parlent de
   « ministère du Transport et de la Logistique » et de « ministère de l'Équipement, de
   l'Habitat et de l'Infrastructure », mais **aucun décret d'organisation postérieur à 2016
   (transport) / 2018 (équipement)** n'est trouvé dans `jort_cache` (requêtes FR et AR, au
   29 oct. 2026). Soit ces libellés résultent de décrets de **nomination/remaniement**
   (décrets présidentiels de composition de gouvernement, non des décrets d'organisation),
   soit un texte manque à `jort_cache`. → fiche R2.
2. **SPROLS** : texte de création non identifié dans `jort_cache` par les requêtes menées.
   → fiche R3.
3. **Transtu — texte de création exact** : la loi 2003-33 (fusion) et le décret d'organisation
   2003-2407 sont trouvés ; le décret portant *création* de la société (distinct de
   l'organisation) n'a pas été isolé. À vérifier si la fusion vaut création.
4. **Stabilité de la nomenclature GBO 2015-2024** : seuls les PAP FR 2021-2022 ont été relus
   programme par programme ; les PAP arabes 2015-2018 et 2024 (couche texte partielle) ne
   confirment pas que la carte des programmes est restée identique. → fiche R4.
5. **Sous-programmes du transport** : le PAP 2021 annonce « quatre sous-programmes » sans que
   leurs intitulés aient été extraits proprement (tableau en colonnes tronqué par `pdftotext`).
   À relire à l'image si le chapitre détaille l'organisation interne.
6. **Qui décide quoi — chaîne de décision** : le plan (§ 3) demande « tarif : ministre ;
   concession : décret ; contrat-programme : tutelle ». Le tarif est documenté côté
   compensation (arrêtés du ministre du transport) ; la concession par décret est documentée
   (95-720 et suivants, EP) ; **le circuit d'approbation des contrats-programmes** (qui signe,
   qui vise, périodicité) n'est établi que par bribes (PAP 2024 : « dernier contrat-programme »
   par acteur ; métro de Sfax « projet non visé »). Lecture ciblée à faire.
7. **ARRU, SNIT, SPROLS — datation des changements de tutelle habitat** (cf. B.3) non établie.

---

## G. Recherches infructueuses — fiches `docs/recherches.yml` proposées

Fiches **proposées** (ne pas les écrire moi-même ; `/rediger` ou le mainteneur les ajoutera
via `scripts/recherches.py`). Les requêtes listées sont celles réellement lancées le
10 novembre 2026 sur `jort_cache.db`.

```yaml
- id: r-transport-organisation-ministere-apres-2016
  objet: >-
    décret d'organisation ou d'attributions du ministère chargé du transport
    postérieur au décret gouvernemental n° 2016-97 (modif. du décret n° 2014-410),
    qui justifierait le libellé « ministère du Transport et de la Logistique » des
    PAP 2021-2024
  ou: [docs/notes/transport-institution-tutelle-2026-11-10.md]
  requetes:
    titres_like:
      - "%organisation%services centraux%ministere du transport%"
      - "%attributions du ministere du transport%"
    titres_fts:
      - 'transport AND (organisation OR attributions) AND ministere'
    iort_ar:
      - "تنظيم المصالح المركزية لوزارة النقل"
      - "مشمولات وزارة النقل"
      - "وزارة النقل واللوجستيك"
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        jort_cache (intitulés FR et AR), publication jusqu'au 29 octobre 2026.
        Seuls textes d'organisation/attributions trouvés pour le transport :
        décrets 86-863 (1986), 91-86 (1991), 94-135 (1994, régional), 2014-409,
        2014-410 et 2016-97. Rien après janvier 2016. Non exploré : miroir iort au
        plein texte ; décrets présidentiels de composition de gouvernement (qui
        peuvent renommer le ministère sans décret d'organisation).
      couvert_jusqu_au: 2026-10-29
      sources: [titres_like, titres_fts]

- id: r-equipement-organisation-ministere-apres-2018
  objet: >-
    décret d'organisation du ministère chargé de l'équipement/habitat postérieur au
    décret gouvernemental n° 2018-883 (complétant le décret n° 88-1413), qui
    justifierait le libellé « ministère de l'Équipement, de l'Habitat et de
    l'Infrastructure »
  ou: [docs/notes/transport-institution-tutelle-2026-11-10.md]
  requetes:
    titres_like:
      - "%organisation du ministere de l equipement%"
      - "%attributions du ministere de l equipement%"
    titres_fts:
      - 'equipement AND organisation AND ministere'
    iort_ar:
      - "تنظيم وزارة التجهيز والإسكان"
      - "تنظيم وزارة التجهيز والإسكان والبنية التحتية"
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        jort_cache (FR et AR), jusqu'au 29 octobre 2026. Socle inchangé :
        décret 88-1413 (1988), modifié par 92-249 (1992), 2008-121 (2008) et
        2018-883 (2018) ; directions régionales par 2008-512 (2008) modifié
        2015-1766 (2015). Aucune refonte complète après 1988. Non exploré :
        plein texte iort, décrets de composition de gouvernement.
      couvert_jusqu_au: 2026-10-29
      sources: [titres_like, titres_fts]

- id: r-sprols-creation
  objet: texte de création de la Société de promotion des logements sociaux (SPROLS)
  ou: [docs/notes/transport-institution-tutelle-2026-11-10.md]
  requetes:
    titres_like:
      - "%promotion des logements sociaux%"
      - "%logements sociaux%creation%"
    iort_ar:
      - "الشركة الوطنية لترويج المساكن الاجتماعية"
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        jort_cache, intitulés FR ; SPROLS apparaît dans les PAP et le rapport EP
        (capital 5,0 MD, LF 2021) mais son texte fondateur n'a pas été isolé par
        les requêtes FR. Terme arabe non encore joué sur le miroir iort.
      couvert_jusqu_au: 2026-10-29
      sources: [titres_like]

- id: r-transport-gbo-nomenclature-2015-2024
  objet: >-
    confirmation que la carte des programmes/sous-programmes des missions
    « Transport » et « Équipement et Habitat » est restée identique de 2015 à 2024
    (les PAP arabes 2015-2018 et 2024 n'ayant pas été relus programme par programme)
  ou: [docs/notes/transport-institution-tutelle-2026-11-10.md]
  requetes:
    note: >-
      recherche documentaire (PDF catalogués tunisia-data), non jort_cache :
      relire les sommaires des PAP 2015, 2016, 2017 (arabe) et 2024 (arabe)
      transport et équipement.
  passes:
    - date: 2026-11-10
      resultat: partiel
      couverture: >-
        Nomenclature 2021-2022 établie (Transport : 4 programmes ; Équipement :
        P1 infrastructure routière, P2 protection zones urbaines/littoral, P3
        aménagement/urbanisme/habitat, P9 pilotage). PAP arabes 2015-2018 et 2024
        non relus (couche texte partielle, cf. fiche tunisia-data § 1).
      couvert_jusqu_au: 2026-11-10
      sources: [pap-transport-2021, pap-transport-2022, pap-meh-2022]
```

---

## Backlog (reports constatés par cette note — à verser par le mainteneur dans `docs/notes/backlog-precis.md`)

- **Libellé officiel des deux ministères (post-2016/2018)** non sourcé par un décret
  d'organisation : vérifier s'il résulte de décrets présidentiels de composition de
  gouvernement (fiche R2 ci-dessus) ; à trancher avant toute phrase du précis nommant
  « ministère du Transport et de la Logistique » / « …de l'Infrastructure ».
- **Textes de création à cataloguer** (D.2) : ARRU (loi 81-69), SNTRI (décret-loi 81-22),
  métro de Tunis (décret-loi 81-21), métro de Sfax (décret 2015-957), CTN (loi 59-34),
  SNIT (loi 57-19) ; SPROLS à identifier (fiche R3).
- **Chaîne d'approbation des contrats-programmes** des opérateurs (qui signe, vise,
  périodicité) : non établie — lecture ciblée des PAP 2024 et des rapports d'activité MEH.
- **Sous-programmes de la mission Transport** (intitulés des « quatre sous-programmes »)
  non extraits : relecture à l'image du PAP 2021 p. 19-37.
- **Stabilité de la nomenclature GBO 2015-2024** (fiche R4) non confirmée.
- **Datation des changements de tutelle habitat** (AFH, ARRU, SNIT, SPROLS).
- Rappel du plan (§ 4) : relire **loi 85-77** et **loi 2004-33** (organisation des transports
  terrestres) sous l'angle « organisation du secteur » (déjà en réf. compensation).

---

## Complément — collecte ciblée G3 : organisation récente des ministères (10 novembre 2026)

Documentaliste, chantier « Livre transport », ticket G3. Ce complément confirme/clôt trois
points laissés en réserve par la note parente (fiches R2, R3) : décrets d'organisation du
**Transport post-2016**, de l'**Équipement/Habitat post-2018**, et le **texte de création de
la SPROLS**. Source : `jort_cache.db` (publication jusqu'au 2026-10-29), requêtes FR **et
arabes** (iort_ar, période 2011+), URL `pist.tn` vérifiées (HTTP 200, `application/pdf`).

### G3.a — Transport : aucun décret d'organisation/attributions central après 2016-97 (confirmé)

Au 2026-10-29, `jort_cache` ne contient **aucun décret** postérieur au décret gouvernemental
n° 2016-97 (2016-01-11) qui **fixerait à nouveau les attributions** ou **réorganiserait les
services centraux** du ministère chargé du transport. Les décrets 2014-409 (attributions) et
2014-410 (organisation, mod. 2016-97) ne reçoivent **aucune modification** après février 2016
(requêtes FR et AR « 410 لسنة 2014 » / « 409 لسنة 2014 » : nil). L'ossature établie par T2 §A.1
est donc **à jour jusqu'au 2026-10-29**. Textes d'organisation **périphériques** parus depuis :

- **Décret n° 2023-456 du 5 juin 2023**, *fixant les attributions et l'organisation des
  directions régionales du transport* (JORT 2023 n° 62, p. 1633-1638 ; recid 172359) —
  **remplace/actualise** le décret 94-135 de 1994 (directions régionales). C'est le seul texte
  d'« organisation » du ministère du transport postérieur à 2016, mais il ne touche pas
  l'administration centrale.
- **Décret n° 2023-455 du 5 juin 2023**, *portant création d'une unité de gestion par objectifs
  au ministère des transports* (réforme GBO ; JORT 2023 n° 62, p. 1633 ; recid 172358).
- **Décret n° 2023-581 du 7 septembre 2023**, *portant organisation du transport public routier
  non régulier des personnes* (JORT 2023 n° 104, p. 2236 ; recid 182005) — organisation d'une
  activité, non du ministère.

**Libellé « ministère du Transport et de la Logistique »** (fiche R2) : il n'émane d'aucun
décret d'organisation. Il apparaît dans `jort_cache` sous la forme « ministre des transports
et de la logistique » / « وزير النقل واللوجستيك » **seulement** sur des arrêtés publiés **de
août 2020 à juillet 2021** (gouvernements Fakhfakh puis Mechichi) ; avant et après, les textes
disent « ministre des transports » / « وزير النقل ». Le libellé est donc un **intitulé de
portefeuille gouvernemental** (décrets présidentiels de nomination/composition), transitoire,
et non un changement d'organisation. (À ne pas confondre avec le décret 2001-2495, qui renomme
l'École de la marine marchande de Sousse en « Institut supérieur du transport et de la
logistique ».) **Fiche R2 (volet transport) : résolue par la négative** — aucun décret
d'organisation à chercher, le libellé relève de la composition du gouvernement.

### G3.b — Équipement/Habitat : aucun décret d'organisation central après 2018-883 (confirmé)

Au 2026-10-29, le socle organisationnel reste le **décret n° 88-1413 de 1988**, dont la
dernière modification est le décret gouvernemental **n° 2018-883** (2018-10-24 ; publ.
2018-10-30). Requêtes FR et AR « 1413 لسنة 1988 » après octobre 2018 : **nil**. Aucune refonte
complète. Textes périphériques postérieurs à 2018 touchant l'organisation :

- **Décret gouvernemental n° 2021-327 du 5 mai 2021**, *portant fixation des missions de
  l'Agence foncière de l'habitation, de son organisation administrative et financière…* (recid
  155503) — déjà relevé en T2 §B.2 pour l'AFH ; **modifié et complété par le décret n° 2023-584
  du 13 septembre 2023** (JORT 2023 n° 105, p. 2251 ; recid 182038).
- Série de **décrets de création d'unités de gestion par objectifs** (UGO/GBO) au ministère de
  l'équipement en 2023 (n° 2023-95, 2023-97, 2023-98, 2023-177, 2023-753, 2023-764) — réforme
  budgétaire, non réorganisation des services centraux.
- **Directions régionales** : inchangées depuis T2 (décret 2008-512, mod. 2015-1766) ; aucun
  texte nouveau repéré après 2018.

**Libellé « ministère de l'Équipement, de l'Habitat et de l'Infrastructure »** (fiche R2,
volet équipement) : même constat. Il figure dans `jort_cache` (« ministre de l'équipement, de
l'habitat et de l'infrastructure ») **uniquement de décembre 2020 à juin 2021** (gouvernements
Fakhfakh/Mechichi) ; dès 2022, les arrêtés disent de nouveau « ministre de l'équipement et de
l'habitat ». Intitulé de portefeuille gouvernemental, transitoire, sans décret d'organisation.
**Fiche R2 (volet équipement) : résolue par la négative.**

### G3.c — SPROLS : texte de création identifié (résout la fiche R3)

La fiche R3 de T2 peut être **close, résultat positif**. Le terme arabe employé par T2
(« ترويج المساكن ») était erroné ; la SPROLS se dit **« شركة النهوض بالمساكن الاجتماعية »**. Le
texte fondateur et sa filiation :

- **Loi n° 77-53 du 3 août 1977**, *portant création de la Société de promotion des logements
  sociaux* (JORT 1977 n° 53, p. 2098 ; recid 115766). **Émetteur : loi** (pouvoir législatif).
  → **création de la SPROLS**, tutelle Équipement/Habitat.
- **Décret n° 77-926 du 10 novembre 1977**, *portant organisation de la société de promotion
  des logements sociaux* (JORT 1977 n° 76, p. 3186-3188 ; recid 100198).
- **Loi n° 93-78 du 19 juillet 1993**, *modifiant la loi n° 77-53…* (JORT 1993 n° 54, p. 1027 ;
  recid 112958).
- Textes récents de la filiation : organigramme fixé par décret **99-1105** (1999) puis
  **2015-539** (2015) ; organisation retouchée par décret gouvernemental **2017-840**
  (2017-07-26, recid 77391) ; et, hors période T2, **loi n° 2026-2 du 13 février 2026,
  *complétant la loi n° 77-53…*** (JORT 2026 n° 19, p. 262 ; recid 201858 — texte arabe seul).

URL vérifiées (HTTP 200, PDF) : `https://www.pist.tn/jort/1977/1977F/Jo05377.pdf` (loi 77-53,
éd. FR) ; `https://www.pist.tn/jort/2023/2023F/Jo0622023.pdf` (décret 2023-456, éd. FR).

### G3.d — Références CSL-JSON candidates (à créer)

```json
[
  {
    "id": "loi77-53-sprols",
    "citation-key": "loi77-53-sprols",
    "type": "legislation",
    "title": "Loi n° 77-53 du 3 août 1977, portant création de la Société de promotion des logements sociaux (SPROLS)",
    "issued": {"date-parts": [[1977, 8, 3]]},
    "authority": "République tunisienne",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "53",
    "page": "2098",
    "URL": "https://www.pist.tn/jort/1977/1977F/Jo05377.pdf"
  },
  {
    "id": "decret77-926-sprols",
    "citation-key": "decret77-926-sprols",
    "type": "legislation",
    "title": "Décret n° 77-926 du 10 novembre 1977, portant organisation de la Société de promotion des logements sociaux",
    "issued": {"date-parts": [[1977, 11, 10]]},
    "authority": "République tunisienne",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "76",
    "page": "3186-3188",
    "URL": "https://www.pist.tn/jort/1977/1977F/Jo07677.pdf"
  },
  {
    "id": "decret2023-456-transport-dr",
    "citation-key": "decret2023-456-transport-dr",
    "type": "legislation",
    "title": "Décret n° 2023-456 du 5 juin 2023, fixant les attributions et l'organisation des directions régionales du transport",
    "issued": {"date-parts": [[2023, 6, 5]]},
    "authority": "République tunisienne",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "62",
    "page": "1633-1638",
    "URL": "https://www.pist.tn/jort/2023/2023F/Jo0622023.pdf"
  },
  {
    "id": "decret2023-584-afh",
    "citation-key": "decret2023-584-afh",
    "type": "legislation",
    "title": "Décret n° 2023-584 du 13 septembre 2023, modifiant et complétant le décret gouvernemental n° 2021-327 du 5 mai 2021, portant fixation des missions de l'Agence foncière de l'habitation",
    "issued": {"date-parts": [[2023, 9, 13]]},
    "authority": "République tunisienne",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "105",
    "page": "2251",
    "URL": "https://www.pist.tn/jort/2023/2023F/Jo1052023.pdf"
  }
]
```

Déjà présente / à compléter : `loi93-78-sprols` (loi 77-53 modifiée) peut s'ajouter si le
chapitre évoque la réforme de 1993. La **loi 2026-2** (texte arabe seul dans `jort_cache`,
`pdf_fr` nul) est notée mais hors période utile au récit institutionnel 2014-2024 ; à cataloguer
depuis l'édition arabe seulement si le chapitre couvre 2026.

### G3.e — Notions à glossaire (pour mémoire, non modifiées)

- **SPROLS** (Société de promotion des logements sociaux / شركة النهوض بالمساكن الاجتماعية) —
  source canonique : loi 77-53 du 3 août 1977. Distincte de la **SNIT** (promotion immobilière
  générale) et du **FOPROLOS** (fonds). À verser au glossaire par le rôle compétent si besoin.

### G3.f — Lacunes résiduelles

- **Loi 2026-2 (SPROLS)** : contenu non lu (édition arabe seule ; hors période du récit
  2014-2024). Objet exact « complétant la loi 77-53 » non détaillé ici.
- **Datation fine du rattachement de tutelle habitat** (AFH/ARRU/SNIT/SPROLS entre
  Équipement et autres ministères) : toujours non établie (déjà au backlog T2, §F/Backlog).
- Les **intitulés transitoires** de portefeuille (2020-2021) ne sont pas reliés à leurs décrets
  présidentiels de composition de gouvernement précis — non nécessaire au récit d'organisation,
  signalé pour écarter toute tentation de les présenter comme des réorganisations.

### G3.g — Fiches `docs/recherches.yml` proposées (mises à jour — ne pas écrire moi-même)

Ajouter une **passe datée 2026-11-10** aux fiches R2 et R3 de T2 (ne pas créer de doublon) :

```yaml
# Mise à jour fiche existante r-transport-organisation-ministere-apres-2016 :
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        jort_cache (FR + AR), publication jusqu'au 2026-10-29. Aucun décret
        d'organisation/attributions CENTRAL du min. du transport après 2016-97 ;
        2014-409 et 2014-410 non modifiés après fév. 2016 (requêtes « 410/409 لسنة
        2014 » : nil). Nouveaux textes d'organisation PÉRIPHÉRIQUES : décret 2023-456
        (directions régionales), 2023-455 (UGO/GBO), 2023-581 (transport public non
        régulier). Libellé « …et de la logistique » : intitulé de portefeuille
        gouvernemental (arrêtés 2020-08 → 2021-07, gouv. Fakhfakh/Mechichi), non un
        décret d'organisation. Volet transport considéré RÉSOLU par la négative.
      couvert_jusqu_au: 2026-10-29
      sources: [titres_like, titres_fts, iort_ar]

# Mise à jour fiche existante r-equipement-organisation-ministere-apres-2018 :
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        jort_cache (FR + AR), jusqu'au 2026-10-29. Socle inchangé : décret 88-1413,
        dernière modif = 2018-883 (aucune après oct. 2018 ; « 1413 لسنة 1988 » : nil).
        Textes périphériques : AFH redéfinie 2021-327 mod. 2023-584 ; UGO/GBO 2023 ;
        directions régionales toujours 2008-512 mod. 2015-1766. Libellé « …et de
        l'infrastructure » : intitulé de portefeuille (arrêtés 2020-12 → 2021-06),
        non un décret d'organisation. Volet équipement RÉSOLU par la négative.
      couvert_jusqu_au: 2026-10-29
      sources: [titres_like, titres_fts, iort_ar]

# Fiche r-sprols-creation : RÉSOLUE — passer resultat = clé CSL loi77-53-sprols
  passes:
    - date: 2026-11-10
      resultat: loi77-53-sprols
      couverture: >-
        Texte trouvé : loi n° 77-53 du 3 août 1977 portant création de la SPROLS
        (recid 115766, JORT 1977 n° 53 p. 2098). Organisation : décret 77-926 (1977).
        Le terme arabe correct est « شركة النهوض بالمساكن الاجتماعية » (et non
        « ترويج »), ce qui explique l'échec de la passe FR/AR du 2026-11-10 initial.
      couvert_jusqu_au: 2026-10-29
      sources: [titres_like]
    # ajouter aux requêtes.iort_ar le terme correct :
    #   - "النهوض بالمساكن الاجتماعية"
```
