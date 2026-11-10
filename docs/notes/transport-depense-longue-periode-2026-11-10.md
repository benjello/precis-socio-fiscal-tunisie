# Note documentaire — La dépense publique de transport, longue période (ticket T4)

Documentaliste, 10 novembre 2026. Chantier « Livre transport » (branche `chantier/transport-livre`).
Cette note **instruit** le chapitre « La dépense publique de transport, longue période »
(`docs/notes/transport-plan-livre.md`, § 3 et § 4). Elle ne rédige ni ne publie : aucun `.qmd`,
aucun commit. Les séries citées vivent dans l'entrepôt `tunisia-data` (fiches `minfin-budget-transport.md`,
`minfin-transferts-transport.md`, `ministere-transport-equipement-habitat.md`,
`transport-trafic-comptes.md`) et dans le cache de séries du précis (`precis/_seriescache/`).

**Règle de domicile appliquée.** Trois familles tenues séparées :
- **budgétaire / ministère des Finances** : crédits votés (lois de finances, PAP), réalisations
  (RAP), transferts aux entreprises, répartition par programme et par nature ;
- **rapport extérieur** : Banque mondiale (*Livre blanc* 2016), FMI — non mobilisés ici pour la
  dépense, renvoyés au chapitre « Rapports et études » ;
- **évaluation économique** : aucune évaluation d'incidence du poste transport n'existe (constat
  de la note du 11 octobre 2026) ; rien à verser.

Le **poste « transport » de la compensation** (111,0 MD en 2003 → 660,0 MD en 2024) a son domicile
au livre compensation (`precis/fr/compensation/_transport.qmd`, @sec-compensation-par-poste) : je
**relie**, je ne recopie pas. Les **comptes des opérateurs** (résultats, dette, effectifs) ont leur
domicile aux entreprises publiques : hors champ de cette note (sauf mention de contexte).

---

## 0. Résultat en une ligne

La dépense budgétaire de transport se lit, à l'ère du budget par objectifs (GBO), sur **deux
missions** du budget de l'État : la **mission Transport** (opérateurs de transport : subventions
d'exploitation et d'équilibre, dominées par la ligne « interventions ») et la **mission Équipement
et Habitat** (où vit l'**investissement routier**, ~85 % de la mission). La matière existe **déjà
dans l'entrepôt et dans le cache du précis** et couvre, pour la mission Transport, **2012-2024**, et
pour la mission Équipement, **2014-2024** — bien au-delà de ce que le TODO du chapitre compensation
laissait croire manquant. Les vrais trous sont : **l'avant-GBO** (Transport avant 2012, Équipement
avant 2014), **l'exécution 2024-2026** (RAP non encore collectés), et **la cohérence entre éditions
et nomenclatures** (loi organique du budget 2019, renommage « Transport et logistique »).

---

## 1. Faits et séries sourcés — famille **budgétaire**

### 1.1 Mission Transport — crédits (loi de finances) et réalisations

**Famille** : budgétaire (ministère des Finances, documents GBO). **Unité** : millions de dinars
courants (MD), convertis depuis les milliers de dinars des sources. **Concept** : « budget de
l'État » = **hors ressources propres des établissements publics**, crédits de paiement (CP).

**a) Série d'exécution (réalisations, RAP) — la plus homogène disponible.**
Déjà construite dans le précis : `precis/_seriescache/budget-missions-execute.csv`
(série `budget-missions-execute`, source `gbo-rap-missions`, générée le 2026-11-10), ligne `transport` :

| Année | Mission Transport, payé (MD) | Régime | Source |
|---|---:|---|---|
| 2018 | 640,0 | paiements seuls, ancienne nomenclature | RAP 2018 |
| 2019 | 616,3 | paiements seuls, ancienne nomenclature | RAP 2019 |
| 2020 | 808,0 | LOB 2019, hors ressources propres | RAP 2020 |
| 2021 | 705,6 | LOB 2019, hors ressources propres | RAP 2021 |
| 2022 | 878,2 | LOB 2019, hors ressources propres | RAP 2022 |
| 2023 | 935,5 | LOB 2019, hors ressources propres | RAP 2023 |

**Rupture de nomenclature signalée dans la série elle-même** : la loi organique du budget de 2019
(généralisée à partir de la gestion 2020) fait passer de « paiements seuls / ancienne nomenclature »
à « hors ressources propres ». 2018-2019 et 2020-2023 ne sont pas strictement homogènes ; le raccord
ne doit pas être muet (voir § 5).

**b) Crédits de paiement votés / prévus — cadre de dépenses à moyen terme (CDMT) des PAP.**
Reconstitués à partir des tableaux CDMT des PAP de l'entrepôt (lus sur couche texte `pdftotext -layout`,
à confirmer à l'image avant citation littérale). Chaque année figure dans plusieurs éditions, avec un
état différent (**réalisation**, **loi de finances**, **prévision**) :

| Année | État | Total mission (MD) | Édition source |
|---|---|---:|---|
| 2012 | réalisation | 543,3 | PAP 2015 (CDMT par programme) |
| 2013 | réalisation | 385,3 | PAP 2015 |
| 2014 | loi de finances | 854,5 | PAP 2015 |
| 2015 | loi de finances | 688,2 | PAP 2015 |
| 2016 | prévision | 707,6 | PAP 2015 |
| 2017 | réalisation | 943,0 | PAP 2021 |
| 2017 | prévision | 769,3 | PAP 2015 |
| 2018 | réalisation | 640,0 | PAP 2021 |
| 2019 | réalisation | 609,2 | PAP 2021 |
| 2020 | loi de finances | 728,65 | PAP 2021 |
| 2020 | réalisation | 808,9 | PAP 2022 |
| 2021 | loi de finances | 829,5 | PAP 2021 (« Transport et logistique ») |
| 2021 | loi de finances | 729,5 | PAP 2022 (« Transport ») |
| 2022 | réalisation | 876,3 | PAP 2024 |
| 2022 | prévision (PLF) | 953,9 | PAP 2022 ; `budget-missions-vote.csv` |
| 2023 | loi de finances | 1 011,5 | PAP 2024 ; `budget-missions-vote.csv` |
| 2024 | loi de finances | 1 051,0 | PAP 2024 ; `budget-missions-vote.csv` |
| 2025 | loi de finances | 1 076,5 | `budget-missions-vote.csv` |

> **Alerte homogénéité (perimètre).** Pour 2021, l'édition PAP 2021 (intitulée *Transport et
> logistique*, crédits fixés « dans la limite de 829 500 mille dinars » par la loi de finances n° 2020-46)
> et l'édition PAP 2022 (*Transport*, LF 2021 = 729 500) **diffèrent de 100 MD**. Le renommage de la
> mission (retrait ou reclassement du volet « logistique ») est la cause probable. **Ne pas chaîner
> ces deux éditions en silence.** Prendre la série d'exécution (§ 1.1 a) comme colonne vertébrale et
> traiter les CP votés comme une seconde série, édition par édition.

**c) Répartition par nature (PAP 2021, CP, MD) — l'investissement est marginal dans la mission.**

| Nature | 2017 | 2018 | 2019 | 2020 (LF) | 2021 |
|---|---:|---:|---:|---:|---:|
| Rémunération | 14,2 | 15,2 | 16,9 | 21,0 | 21,6 |
| Fonctionnement | 2,9 | 3,0 | 3,4 | 3,7 | 4,0 |
| **Interventions** | **925,6** | **621,3** | **587,9** | **698,0** | **798,2** |
| Investissement | 0,3 | 0,5 | 1,0 | 6,0 | 5,7 |
| Total | 943,0 | 640,0 | 609,2 | 728,65 | 829,5 |

PAP 2024 (CDMT 2024-2026, ar) prolonge : interventions 850,8 (2022 réal) → 967,7 (2023 LF) →
1 007,2 (2024 LF) → 1 034,3 (2025) → 1 071,3 (2026) ; investissement 1,5 → 15,3 → 14,2 → 14,6 → 15,1.

**Fait structurant** : la mission Transport est **à 90-97 % des « interventions »** (subventions aux
opérateurs) ; sa ligne d'**investissement propre est quasi nulle** (0,3 à 15 MD). L'investissement du
secteur ne transite donc **pas** par la ligne d'investissement de la mission Transport (voir § 1.3).

**d) Répartition par programme (PAP 2015, CP, MD).** Programme « Transport terrestre » dominant :
524,5 (2012) / 363,6 (2013) / 629,8 (2014) / 616,9 (2015) / 670,2 (2016) / 728,3 (2017) ; aviation
civile et maritime/ports, chacun < 30 MD ; pilotage 7-14 MD. Le programme terrestre porte la
compensation du transport public (relié au livre compensation).

### 1.2 Mission Équipement et Habitat — crédits et réalisations

**Famille** : budgétaire. **Unité** : MD courants. **Concept** : hors ressources propres, CP.
**Réserve de périmètre capitale** : la mission « Équipement et Habitat » **n'est pas une mission de
transport**. Elle réunit l'**infrastructure routière** (Programme 1), la **protection des zones
urbaines et du littoral** (Programme 2) et l'**aménagement du territoire, urbanisme et habitat**
(Programme 3). Seul le **Programme 1 — Infrastructure routière** est la part transport ; le reste
(logement social, urbanisme) relève d'autres politiques. **Ne jamais compter la mission entière
comme « dépense de transport ».**

**a) Exécution (RAP, payé, MD)** — `budget-missions-execute.csv`, ligne `equipement` :

| Année | Mission Équipement, payé (MD) | Engagé (MD) | Régime |
|---|---:|---:|---|
| 2018 | 1 440,8 | — | paiements seuls, ancienne nomenclature |
| 2019 | 1 262,5 | — | paiements seuls, ancienne nomenclature |
| 2020 | 1 609,7 | 3 793,7 | LOB 2019, hors ressources propres |
| 2021 | 1 446,9 | 1 994,6 | LOB 2019, hors ressources propres |
| 2022 | 1 423,5 | 2 747,8 | LOB 2019, hors ressources propres |
| 2023 | 1 603,1 | 2 189,7 | LOB 2019, hors ressources propres |

**b) Mission entière et Programme 1 (routes), PAP, CP, MD.** Les éditions divergent fortement entre
**prévision** et **réalisation** (l'investissement est massivement sous-réalisé : le RAP 2020 note un
taux d'engagement de **42,8 %**) :

- PAP 2018 (total ministère, projections/LF) : 812,5 (2014) / 989,4 (2015) / 1 278,3 (2016) /
  1 686,97 (2017 LF) / 1 585,8 (2018) / 2 385,8 (2019 prév) / 2 687,0 (2020 prév).
- PAP 2022 (réal/LF/prév) : **total mission** 1 609,7 (2020 réal) / 1 735,0 (2021 LF) / 1 802,5
  (2022) / 1 916,2 (2023) / 1 999,9 (2024). **Programme 1 Infrastructure routière** : 1 239,1 (2020
  réal) / 1 347,8 (2021 LF) / 1 359,6 (2022) / 1 441,1 (2023) / 1 530,1 (2024).
- PAP 2024 (ar) : crédits d'investissement du Programme 1 860,2 (2022 réal) → 1 075,0 (2023 LF) →
  1 100,0 (2024) → 1 179,2 (2025) → 1 270,7 (2026) ; dont ~450,0 sur ressources extérieures affectées.

**Répartition par nature (PAP 2022, mission entière, CP, MD)** : l'investissement **domine** —
rémunération 104,5 (2020) → 114,9 (2021 LF) ; fonctionnement 55,9 → 57,0 ; interventions 3,4 → 3,1 ;
**investissement 1 364,3 → 1 387,8** (≈ 85 % de la mission). L'infrastructure routière est de
l'**investissement public**, à la différence de la mission Transport, faite de subventions.

**c) Détail d'activité (PAP 2022, crédits d'engagement, Programme 1, MD)** : autoroute Tunis-Jelma
(232,0 prévu 2022), voiries structurantes (126,0), réhabilitation des routes classées (124,8),
entretien des routes classées (202,2), ouvrages d'art (37,1), entretien des pistes rurales (84,6),
sécurité routière et dégâts d'inondation (24,5). Matière prête pour une figure « où va le crédit
routier ».

### 1.3 Transferts et subventions aux entreprises du secteur

**Famille** : budgétaire. **Série** : `transport-transferts-par-entreprise` (entrepôt, 2016-2024,
607 valeurs ; fiche `minfin-transferts-transport.md`). Source : « Rapport sur les transferts et les
garanties au profit des entreprises publiques… », annexe n° 8 du PLF (clé `minfin-transferts-garanties`).
Cinq natures par entité (`total`, `investissements`, `interventions`, `fonctionnement`,
`remunerations`), 11-12 entités + ligne ministère. **C'est ici que vivent (a) les subventions
d'exploitation/équilibre et (b) l'investissement financé par transfert aux opérateurs** (ex. réseau
ferroviaire rapide : 27 762 en 2018 ; métro de Sfax ; SNCFT).

**Articulation avec la compensation (reliée, non recopiée)** : la colonne « interventions » **n'est
pas** la compensation du transport ; elle dépasse chaque année le poste « transport » de la dépense
de compensation (périmètre plus large : entretien du réseau ferré, apurements de dettes). Le
rapprochement n'est établi que pour 2016 (à 0,5 MD près, par la note du précis). **Ne pas chaîner**
avec `transport-soutien-par-societe` (2012-2017, ligne « دعم النقل العمومي » du budget du ministère
du Transport ; fiche `minfin-budget-transport.md`) : deux périmètres, deux fichiers.

**Appuis budgétaires 2020 (RAP 2020, milliers de dinars, LF / LFC / réalisé)** — utile pour relier
les transferts aux opérateurs : sociétés régionales 300 000 / 335 000 / 335 000 ; SNCFT 143 200 /
183 200 / 171 808 ; réseau ferroviaire rapide 62 000 / 62 000 / 60 200 ; Transtu 153 000 / 173 000 /
169 696 ; SNTRI 2 500 / 7 500 / 7 500 ; métro de Sfax 5 357 / 5 357 / 5 259.

### 1.4 Part de l'investissement (routier et ferroviaire)

Synthèse des trois sources ci-dessus, **par famille, sans les mélanger** :

- **Investissement routier** : mission Équipement, Programme 1 — ~1,0 à 1,5 milliard de dinars de CP
  par an (réalisés 2020-2022), dont une part sur ressources extérieures affectées (≈ 450 MD/an).
  C'est **l'essentiel de l'investissement public de transport**.
- **Investissement ferroviaire et des opérateurs** : par **transfert** (série
  `transport-transferts-par-entreprise`, colonne `investissements`) — réseau ferroviaire rapide,
  SNCFT, métro de Sfax ; ordres de grandeur dans les PAP (métro de Sfax : 40 → 3 165 → 45 600 →
  73 400 → 61 220 milliers de dinars, 2022-2026, PAP 2024).
- **Investissement propre de la mission Transport** : **marginal** (0,3-15 MD/an), § 1.1 c.

> **Mise en garde de lecture.** L'investissement est **voté large et réalisé étroit** : taux
> d'engagement de la mission Équipement de 42,8 % (2020) à 186,7 % (2022, crédits reportés). Toute
> série d'investissement doit préciser **voté vs engagé vs payé** et privilégier le **payé** (RAP)
> pour l'homogénéité.

### 1.5 Rapport au cadre des finances publiques (part du PIB)

**Famille** : budgétaire (numérateur) rapportée au **PIB base 2015** (dénominateur, INS, millions de
dinars courants — `precis/_seriescache/cnat-pib-nominal.csv`, éditions *Comptes de la nation*). Les
deux termes sont en **dinars courants, base 2015** sur toute la fenêtre 2018-2024 : **pas de chaînage
muet de bases** (voir `precis/fr/annexe-pib.qmd`). Pour toute année ≤ 2015, le PIB change de base
(base 1997/2010) : ne pas prolonger le ratio avant 2016 sans signaler la rupture de base.

Ratios calculés sur l'**exécution** (RAP, § 1.1 a et § 1.2 a) / PIB base 2015 (édition la plus
récente par année) :

| Année | Transport (payé/PIB) | Équipement (payé/PIB) | PIB base 2015 (MD) |
|---|---:|---:|---:|
| 2018 | 0,57 % | 1,28 % | 112 985,5 |
| 2019 | 0,50 % | 1,03 % | 122 578,4 |
| 2020 | 0,68 % | 1,35 % | 119 526,4 |
| 2021 | 0,54 % | 1,10 % | 131 544,6 |
| 2022 | 0,63 % | 1,02 % | 139 444,5 |
| 2023 | 0,62 % | 1,07 % | 149 733,8 |

Lecture : la mission Transport pèse **~0,5-0,7 % du PIB**, la mission Équipement **~1,0-1,35 %** ;
ensemble ~1,6-2,0 %. **Caveat de périmètre** : la mission Équipement inclut logement et urbanisme ;
la part proprement *transport* (Transport + Programme 1 routes) vaut plutôt **~1,5 % du PIB**
(Transport ~0,6 % + routes ~0,9 %). À présenter comme tel, jamais « 2 % du PIB pour le transport ».

---

## 2. Références candidates (CSL-JSON)

**Déjà présentes dans la bibliographie** (réutiliser la clé) :
- `gbo-rap-missions` — *Rapports annuels de performance des missions du budget de l'État
  (gestions 2016-2023)*, clé collective des RAP (`precis/fr/references.json`). Couvre les
  réalisations Transport et Équipement de § 1.1 a et § 1.2 a.
- `minfin-transferts-garanties` — *Rapport sur les transferts et les garanties au profit des
  entreprises publiques et des établissements publics non administratifs* (annexe n° 8 du PLF),
  clé collective (éditions `minfin-transferts-2020` à `-2025`). Couvre § 1.3.
- `minfin-budget-transport-2013` … `-2017` — budgets du ministère du Transport
  (`precis/fr/compensation/references.json`). Couvrent § 1.1 d (2012-2017) et la ligne soutien.
- `minfin-finances-publiques-2010` — pour le contexte du poste (déjà cité au livre compensation).

**À créer** — les PAP de mission mobilisés ici pour les CDMT (CSL-JSON prêt à verser ; copies locales
hors git catalogues dans `tunisia-data/sources/ministere-transport-equipement-habitat-urls.csv` avec
SHA-256 ; dates de collecte 2026-11-04). Une **clé collective par mission** suffirait, sur le modèle
de `gbo-rap-missions` ; à défaut, clés par édition :

```json
[
  {
    "id": "gbo-pap-transport",
    "type": "report",
    "title": "Projets annuels de performance de la mission Transport (gestions 2015-2024)",
    "title-short": "PAP Transport",
    "author": [{"literal": "Tunisie, ministère des Finances"}],
    "publisher": "Ministère des Finances (budget par objectifs)",
    "URL": "https://www.finances.gov.tn/fr/pap_rap",
    "note": "Clé collective des PAP de la mission Transport. Éditions utilisées : PAP 2015 (CDMT par programme 2012-2017, gbo.tn/2021-03), PAP 2021 'Transport et logistique' (CDMT par nature 2017-2023, gbo.tn/2021-04), PAP 2022 (budget d'État hors ressources propres 2020-2024, gbo.tn/2022-03), PAP 2024 (CDMT 2024-2026, ar, finances.gov.tn/2024-01). Copies locales et SHA-256 : tunisia-data/sources/ministere-transport-equipement-habitat-urls.csv.",
    "language": "ar-fr"
  },
  {
    "id": "gbo-pap-equipement-habitat",
    "type": "report",
    "title": "Projets annuels de performance de la mission Équipement et Habitat (gestions 2015-2024)",
    "title-short": "PAP Équipement et Habitat",
    "author": [{"literal": "Tunisie, ministère des Finances"}],
    "publisher": "Ministère des Finances (budget par objectifs)",
    "URL": "https://www.finances.gov.tn/fr/pap_rap",
    "note": "Clé collective des PAP de la mission Équipement et Habitat. Éditions utilisées : PAP 2018 (total ministère et Programme 1 routes, 2014-2020, gbo.tn/2021-03), PAP 2022 (CDMT mission par nature et par programme, 2020-2024, gbo.tn/2022-04), PAP 2024 (CDMT 2024-2026, ar/fr, finances.gov.tn/2024-01). Programme 1 = Infrastructure routière. Copies locales et SHA-256 : tunisia-data/sources/ministere-transport-equipement-habitat-urls.csv.",
    "language": "ar-fr"
  }
]
```

Éditions individuelles mobilisées (si clés par édition préférées) et leurs adresses d'origine :
- `gbo-pap-transport-2015` — http://www.gbo.tn/sites/default/files/2021-03/PAP%202015%20TRANSPORT%20%281%29.pdf (SHA-256 718e68b5…, 165 p., CDMT p. 14-15)
- `gbo-pap-transport-2021` — http://www.gbo.tn/sites/default/files/2021-04/PAP%202021%20Transport%20et%20logistique_0.pdf (103b9691…, 159 p., CDMT p. 11-13)
- `gbo-pap-transport-2022` — http://www.gbo.tn/sites/default/files/2022-03/version%20PAP2022%20Transportnv%20%282%29.pdf (656d675e…, 79 p.)
- `gbo-pap-transport-2024` — https://www.finances.gov.tn/sites/default/files/2024-01/PAP%20transport%202024%20vf2710.pdf (153a9463…, 238 p., CDMT p. 5 et suiv.)
- `gbo-pap-equipement-2018` — http://www.gbo.tn/sites/default/files/2021-03/PAP%202018%20Equipement.pdf (6ba3a63d…, 145 p.)
- `gbo-pap-equipement-2022` — http://www.gbo.tn/sites/default/files/2022-04/PAP%202022%20%20MEH%2007%20MARS%20FR2204.pdf (40a749cc…, 162 p., CDMT p. 15)
- `gbo-pap-equipement-2024` — https://www.finances.gov.tn/sites/default/files/2024-01/PAP%202024%20MEH%20version%2027%20oct%202023%20%281%29vf.pdf (1ead7e3c…, 276 p.)

---

## 3. Notions à verser au glossaire (propositions — ne pas éditer `glossaire.yml` ici)

- **mission-budgetaire** (existe déjà) — vérifier qu'elle nomme bien les missions « Transport » et
  « Équipement et Habitat » comme unités de vote du budget de l'État.
- **Crédits de paiement / crédits d'engagement** (FR ; AR اعتمادات الدفع / اعتمادات التعهد) — notion
  clé pour lire tout tableau GBO ; source canonique : loi organique n° 2019-15 du 13 février 2019
  (budget de l'État). **À vérifier/ajouter.**
- **Loi organique du budget 2019 (LOB) / budget par objectifs (GBO)** — explique la rupture de
  nomenclature 2020 (ancienne nomenclature par titre → missions/programmes hors ressources propres).
  Source : loi organique n° 2019-15. **À ajouter.**
- **Programme d'infrastructure routière** (Programme 1 de la mission Équipement et Habitat) — où vit
  l'investissement routier public ; source : PAP Équipement. Utile pour distinguer de l'habitat.
- **Transferts et garanties aux entreprises publiques** (annexe n° 8 du PLF ; AR التحويلات
  والضمانات) — support des subventions d'exploitation, d'équilibre et d'investissement aux opérateurs.
- **compensation-transport** (existe) — garder au livre compensation ; le livre transport n'y renvoie.

---

## 4. Lacunes, année par année

### Mission Transport
- **Avant 2012** : aucune donnée GBO (le GBO ne rétropole pas au-delà de 2012). L'avant-GBO est
  dans les budgets du ministère par titre/partie (portail ancien `portail.finances.gov.tn`) et dans
  les lois de finances/règlement — **non rangés pour le transport**. Pour la subvention d'exploitation
  1995-2002, fiche de recherche `r-transport-ligne-budgetaire-1995-2002` déjà ouverte (livre
  compensation) : non résolue. **TROU honnête : laisser vide avant 2012.**
- **2012-2017** : couvert (PAP 2015 pour les CP ; `transport-soutien-par-societe` pour la ligne
  soutien par société). 2017 a deux valeurs (réal 943,0 / prév 769,3) — garder les deux, états
  distincts.
- **2018-2023** : couvert, exécution (RAP, `budget-missions-execute.csv`). 2021 : divergence
  d'éditions sur les CP votés (829,5 vs 729,5, cause périmètre « et logistique ») — § 5.
- **2024** : CP votés 1 051,0 (LF, PAP 2024) ; **exécution non disponible** (RAP 2024 non publié/non
  collecté).
- **2025-2026** : CP votés 1 076,5 (2025, `budget-missions-vote.csv`) ; prévisions CDMT seulement pour
  2025-2026 (PAP 2024) ; **loi de finances 2026 et exécution : non collectées**.

### Mission Équipement et Habitat
- **Avant 2014** : aucune donnée GBO. **TROU honnête.**
- **2014-2017** : couvert par projections/LF (PAP 2018) ; **réalisations manquantes** avant 2018.
- **2018-2023** : couvert, exécution (RAP). Attention : 2018-2019 « ancienne nomenclature ».
- **2024** : CP votés ~2 000 (prév PAP 2022) / investissement Pr1 1 100 (PAP 2024 ar) ; **exécution
  non disponible**.
- **2025-2026** : prévisions CDMT seulement ; **série votée (PLF/LF) de la mission Équipement NON
  construite** dans le précis (`budget-missions-vote.csv` ne contient que la mission Transport).

### Transferts / subventions
- `transport-transferts-par-entreprise` couvre **2016-2024**. Éditions LF 2021 et LF 2023 non
  transcrites (dans/absentes de l'entrepôt) ; **2025+ non couvert**. Rapprochement
  interventions ↔ poste compensation établi pour **2016 seulement** ; **2018-2024 non refait**.

### Investissement
- Pas de **série longue homogène d'investissement routier réalisé** : seule l'exécution de la mission
  Équipement (2018-2023) l'approche, mais mêlée à l'habitat. Le Programme 1 réalisé n'existe
  proprement que pour 2020-2022 (PAP 2022/2024). **Investissement ferroviaire réalisé** : seulement
  par bribes dans les transferts et les PAP ; pas de série.

### PIB / ratios
- Ratios calculables 2018-2024 (base 2015). **Avant 2016** : rupture de base PIB — ne pas prolonger
  le ratio sans note de concordance (`annexe-pib.qmd`).

---

## 5. Série homogène vs approximation — raisonnement

**Série visée** : dépense de la mission Transport (et de la mission Équipement) sur la plus longue
fenêtre homogène — même périmètre (hors ressources propres), même concept (CP payés), même source
(RAP), même unité (MD courants).

**Ce qui est atteignable sans approximer** :
1. **Transport, exécution 2018-2023** et **Équipement, exécution 2018-2023** : homogènes **à une
   réserve** — la bascule « ancienne nomenclature » (2018-2019, paiements seuls) → « LOB 2019, hors
   ressources propres » (2020-2023). L'écart de concept est réel (les ressources propres des
   établissements sont exclues depuis 2020) mais **documenté dans la colonne `regime` de la série** :
   le raccord n'est pas muet. Je **laisse le marqueur de régime visible** plutôt que de lisser.
2. **Transport, CP votés 2022-2025** : homogène (même source `budget-missions-vote`), à condition
   d'exclure 2021 (périmètre « et logistique »).

**Ce qui n'est PAS homogène et ne doit pas être chaîné en silence** :
- **2021 Transport, 829,5 vs 729,5** : deux périmètres (« Transport et logistique » / « Transport »).
  Un chaînage muet fabriquerait une fausse baisse de 100 MD. **Trou/double-valeur assumé.**
- **Prévisions PAP 2018 vs réalisations Équipement** : écart jusqu'à 2,69 Md (prév 2020) contre
  1,61 Md (réal) — l'investissement est voté large, réalisé étroit. **Ne jamais présenter une
  prévision CDMT comme une dépense.**
- **Avant-GBO** : les budgets par titre ne se raccordent pas aux missions GBO. **Trou laissé.**

**Aucune approximation proposée dans cette note.** La grandeur manquante (avant-GBO, exécution
2024-2026) est importante, mais **l'erreur n'est pas bornable** sans les documents sources (budgets
anciens par titre ; RAP non publiés) : l'exigence « informative, pas trompeuse » n'est pas remplie.
Conformément à la règle, **le trou se laisse honnête**. La cible qui le comblerait est nommée au
backlog (§ 6) et aux fiches de recherche (§ 7), pour qu'il soit un provisoire réparable.

---

## 6. Backlog (lignes proposées pour `docs/notes/backlog-precis.md` — NE PAS éditer ici)

- **Construire la série votée (PLF/LF) de la mission Équipement et Habitat** (comme
  `budget-missions-vote` l'a fait pour Transport) : lois de finances 2021-2026, annexe « Dépenses par
  mission ». Documents en partie dans l'entrepôt (PAP) ; compléter par les lois de finances.
- **Isoler le Programme 1 (Infrastructure routière) réalisé** en série propre, pour une dépense
  routière distincte de l'habitat ; sources RAP (répartition par programme) 2018-2023 à extraire.
- **Transcrire les éditions de transferts manquantes** (LF 2021, LF 2023) et **refaire le
  rapprochement interventions ↔ poste compensation pour 2018-2024** (une seule année faite, 2016).
- **Collecter l'exécution 2024-2026** (RAP Transport et Équipement) dès publication sur gbo.tn /
  finances.gov.tn ; la page PAP/RAP est protégée par CAPTCHA (code 421) → voir § 7.
- **Avant-GBO (Transport < 2012, Équipement < 2014)** : budgets des ministères par titre sur le
  portail ancien `portail.finances.gov.tn` + lois de règlement ; reconstitution à instruire
  séparément, sans chaînage aux missions GBO.
- **Note de concordance « dépense de transport »** : carte des périmètres (mission Transport vs
  mission Équipement Pr1 vs poste compensation vs transferts), invariants et écarts chiffrés — utile
  avant toute figure « poids de l'ensemble ».
- Fiches « Ce qu'en dit l'économie » du secteur : aucune n'existe (report de la fiche de plan).

## 6 bis. À verser à l'index des tableaux / au playbook de l'entrepôt `tunisia-data`

- **`bct-archives.md` n'est pas le bon index** ici : proposer, dans
  `ministere-transport-equipement-habitat.md`, un **« Index des CDMT de mission »** (quel PAP donne
  quelles années, par nature et par programme) — tableau de § 1.1 b/c/d et § 1.2 b ci-dessus.
- **Playbook `chercher-des-donnees-tunisie.md`** : ajouter la technique « les **CDMT des PAP**
  donnent des **séries rétrospectives de 5-6 ans** par mission (réal N-3..N-1, LF N, prév N+1..N+2) —
  un seul PAP récent reconstitue une demi-décennie ; recouper les éditions pour détecter les
  changements de périmètre (ex. mission renommée) avant de chaîner ».

---

## 7. Recherches infructueuses / fiches proposées

**Attention : Internet Archive (Wayback) était hors ligne au moment de cette note** (2026-11-10,
« Internet Archive services are temporarily offline ») : les recettes CDX ci-dessous sont à rejouer
quand le service revient. Ne pas conclure « n'existe pas » sur ce silence.

Fiche proposée (nouvelle), à créer dans `docs/recherches.yml` via `scripts/recherches.py` :

```
- id: r-transport-execution-rap-2024-2026
  objet: >
    Rapports annuels de performance (RAP) des missions « Transport » et « Équipement et Habitat »
    pour les gestions 2024, 2025 et 2026, afin d'étendre la série d'exécution
    budget-missions-execute au-delà de 2023.
  ou: [gbo.tn, finances.gov.tn, web.archive.org]
  requetes:
    motifs_url:
      - "gbo.tn/sites/default/files/AAAA-MM/RAP*TRANSPORT*.pdf"
      - "gbo.tn/sites/default/files/AAAA-MM/RAP*MEH*.pdf"
      - "finances.gov.tn/sites/default/files/AAAA-MM/RAP*.pdf"
    cdx:
      - 'curl "http://web.archive.org/cdx/search/cdx?url=gbo.tn*&matchType=domain&filter=original:.*RAP.*(ransport|MEH|quipement).*&output=text&fl=timestamp,original,statuscode&collapse=digest"'
  passe:
    date: 2026-11-10
    resultat: aucun
    couverture: >
      Entrepôt : RAP Transport 2018-2023 et RAP Équipement 2018-2023 présents
      (precis/_seriescache/budget-missions-execute.csv ; data/raw/gbo-recup-2026-11-04 et -11-10).
      Tentative directe gbo.tn / finances.gov.tn : page PAP/RAP protégée par validation image
      (CAPTCHA, code 421), non contournée (déjà constaté le 2026-11-04,
      ministere-transport-equipement-habitat.md § 4). Wayback : service hors ligne ce jour
      (impossible de lancer le CDX). RAP 2024-2026 non trouvés.
    couvert_jusqu_au: 2023-12-31
    sources: [gbo.tn, finances.gov.tn]
```

Fiche existante à **relier** (ne pas dupliquer) : `r-transport-ligne-budgetaire-1995-2002`
(subvention d'exploitation des sociétés publiques de transport routier 1995-2002, livre
compensation) — couvre une partie de l'avant-GBO ; non résolue.

Autres tentatives, consignées (déjà dans `ministere-transport-equipement-habitat.md § 4`, reprises
ici pour mémoire) : PAP 2025 des trois missions et RAP 2021 Transport/Environnement — page de
validation par image, non contournée ; sites du ministère du Transport (`transport.gov.tn`,
`mt.gov.tn`, etc.) ne répondent pas ; ancien `transport.tn` archivé (statistiques prises, aucun RAP).

---

## 8. Pointeurs de l'entrepôt (ce qui a servi, pour ne pas rechasser)

- `tunisia-data/sources/minfin-budget-transport.md` — soutien par société 2012-2017, abonnements
  scolaires (budgétaire, crédits).
- `tunisia-data/sources/minfin-transferts-transport.md` — transferts par entreprise 2016-2024
  (budgétaire), 5 natures dont investissements.
- `tunisia-data/sources/ministere-transport-equipement-habitat.md` + `-urls.csv` — 47 PDF (PAP, RAP,
  budgets de mission) avec pages, SHA-256 ; **source des CDMT de mission de cette note**.
- `tunisia-data/sources/transport-trafic-comptes.md` — Banque mondiale 2016 (rapport extérieur) et
  comptes des opérateurs (hors champ dépense).
- `precis/_seriescache/budget-missions-execute.csv`, `budget-missions-vote.csv` — séries de mission
  déjà construites dans le précis (exécution 2018-2023 ; vote Transport 2021-2025).
- `precis/_seriescache/cnat-pib-nominal.csv` — PIB par base/édition pour les ratios (base 2015).
- `precis/fr/annexe-pib.qmd` — règle de lecture des bases ; `precis/fr/compensation/_transport.qmd` —
  domicile du poste compensation (relié).

---

## Complément — collecte ciblée G1 (10 novembre 2026)

Documentaliste, chantier « Livre transport ». Ce complément **instruit** le ticket G1 (combler les
trous avant-GBO et l'exécution 2024-2026 de la dépense budgétaire de transport). Il **ne réécrit
pas** la note parente : il ajoute les séries nouvelles trouvées dans l'entrepôt `tunisia-data` et
dit, année par année, ce qui reste trou. **Aucun fichier du précis modifié ; rien re-téléchargé**
(les PDF cités sont déjà dans l'entrepôt, catalogués avec SHA-256).

### G1.1 Avant-GBO : les **budgets du ministère** rouvrent 2011-2013 (famille nouvelle, distincte des missions GBO)

**Trouvaille principale.** Les budgets de l'État par ministère déjà rangés dans l'entrepôt
(`data/raw/minfinances/portail_ancien/budgets_ministeres/`, fiche `minfinances-portail-ancien.md`,
catalogue `minfinances-portail-ancien-urls.csv`) contiennent, **avant le premier PAP de mission**,
un tableau « نفقات التصرف و التنمية » (dépenses de fonctionnement et de développement) des crédits
**totaux du ministère**, par titre, sur **trois années** (réalisation N-2, LF N-1, prévision N). Le
budget 2013 remonte ainsi à **2011**. Cette matière n'était **pas** exploitée par la note parente
(qui n'en avait tiré que la ligne « soutien du transport public par société », série
`transport-soutien-par-societe`).

**Famille** : budgétaire (ministère des Finances). **Unité** : millions de dinars courants (MD ;
« م د »), sous-total par titre en milliers de dinars. **Concept** : crédits **du ministère** par
titre (Titre I = fonctionnement/التصرف ; Titre II = développement/التنمية ; + fonds du Trésor pour
l'Équipement). **États** : réalisation (إنجازات), loi de finances (ق.م), prévision (تقديرات).

**a) Ministère du Transport — crédits totaux (budget 2013, `2013_budget_ministre_transport_jd59.pdf`, p. 1-3, lu sur couche texte `pdftotext -layout`, à confirmer à l'image avant citation littérale) :**

| Année | État | Titre I fonctionnement (MD) | Titre II développement (MD) | **Total ministère (MD)** |
|---|---|---:|---:|---:|
| 2011 | réalisation | 245,849 | 380,505 | **626,354** |
| 2012 | loi de finances | 291,183 | 274,160 | **565,343** |
| 2013 | prévision | 346,010 | 74,240 | **420,250** |

Détail du développement 2013 : investissements directs 0,920 ; financement public sur ressources
générales 58,820 ; sur ressources extérieures affectées 14,500.

**b) Ministère de l'Équipement — crédits totaux (budget 2013, `2013_budget_equipement_jd38.pdf`, p. 1-2) :**

| Année | État | Titre I (MD) | Titre II développement (MD) | Fonds du Trésor (MD) | **Total ministère (MD)** |
|---|---|---:|---:|---:|---:|
| 2011 | réalisation | 108,139 | 802,448 | 19,529 | **930,116** |
| 2012 | loi de finances | 116,255 | 1 058,200 | 104,500 | **1 278,955** |
| 2013 | prévision | 125,487 | 1 144,554 | 96,000 | **1 366,041** |

Développement 2013 : investissements directs sur ressources générales 865,304 ; sur ressources
extérieures affectées 270,800 ; financement public 8,450. Fonds du Trésor : FNAH (تحسين السكن)
76,000 ; FOPROLOS (النهوض بالسكن للأجراء) 20,000 ; fonds des autoroutes 3,637 (2011). L'investissement
routier et l'habitat social sont ici **dans un même budget** : périmètre large.

**Ce que cela comble, honnêtement.** Les crédits **du ministère** (et non des missions GBO) sont
désormais sourcés pour **2011, 2012, 2013** pour les deux ministères. C'est **une famille à part**,
**à ne pas chaîner** aux séries de mission de la note parente (§ 1.1-1.2) :
- le périmètre « ministère » ≠ « mission » : la mission GBO Transport exclut les ressources propres
  des EPNA et réorganise en programmes ; le ministère pré-GBO additionne fonctionnement + développement
  par titre, **ressources extérieures affectées comprises** (14,5 MD en 2013 pour le Transport) ;
- recoupement d'ordre de grandeur, non d'identité : mission Transport 2012 = 543,3 MD en réalisation
  (PAP 2015, note parente) vs ministère Transport 2012 = 565,3 MD en LF (ici) — **deux états, deux
  périmètres**, écart ~4 % ; utile comme contrôle, **pas** comme raccord.

**Rupture de périmètre dès 2014 — ne pas prolonger la série « ministère » sans la casser.** À partir
de la gestion 2014 les intitulés ministériels **fusionnent et se recomposent** : « ministère de
l'Équipement **et de l'Environnement** » (budget 2014, `2014_budget_equipement_environnement_jd548.pdf`,
dont le tableau extrait porte sur « جزء البيئة », la **part Environnement** : 246,251 MD en 2013 →
228,525 MD en 2014), puis « Équipement, Aménagement du territoire et Développement durable » (2015),
puis « Équipement, Habitat et Aménagement du territoire » (2016-2017). Le ministère du Transport est
plus stable (budget 2014 total ≈ 420,250 MD ; budget 2015 : LF 2014 initiale 583,466 → 854,466 MD
après modifications, p. 1). **Conclusion de concordance** : la fenêtre homogène « budget du ministère »
propre et simple est **2011-2013** (Transport et Équipement séparés) ; dès 2014 tout chaînage exige
une note de périmètre explicite (fusion Environnement, puis Habitat/Aménagement). Le **trou avant
2011 reste honnête** : les éditions antérieures des budgets par ministère (2012, 2011, 2010…) **ne
sont pas dans l'entrepôt** (le portail ancien ne descend qu'à l'édition 2013), et les lois de finances
2003-2012 présentes (`lois_finances/`) ne contiennent que **les articles** (totaux par titre/partie
de l'État), **sans ventilation par ministère** — vérifié sur la LF 2011 (`2011_loi_finances_jd774.pdf`).

### G1.2 Exécution 2024-2026 : RAP toujours non publiés (trou confirmé, pas comblé)

Vérifié le 10 novembre 2026 (Wayback Machine **de nouveau en ligne** ce jour, contrairement au
2026-11-10 de la note parente § 7 où le service était tombé) :
- `https://www.finances.gov.tn/fr/pap_rap` répond **200** et ne liste que des **PAP 2024** (prévisions,
  déjà collectés) — **aucun RAP 2024/2025**, ni Transport, ni Équipement/MEH ;
- `http://www.gbo.tn/fr/pap_rap` répond **404** (page déplacée) ;
- Wayback CDX sur `finances.gov.tn/sites/default/files*` et `gbo.tn/sites/default/files*`, filtre
  `RAP.*(transport|MEH|quipement)` : **aucune capture**.

**L'exécution 2024-2026 des deux missions reste un trou honnête** : les RAP ne sont pas publiés
(seuls existent les PAP = crédits prévus). La série d'exécution `budget-missions-execute` s'arrête à
**2023**. Aucune approximation : l'écart prévu→réalisé est trop large (note parente § 1.2 b : taux
d'engagement 42,8 % à 186,7 %) pour borner une estimation — l'exigence « informative, pas trompeuse »
n'est pas remplie.

### G1.3 Couverture année par année après G1

**Crédits du ministère / mission Transport** (famille budgétaire) :
- **≤ 2010** : trou (éditions de budget par ministère absentes de l'entrepôt ; LF sans ventilation) ;
- **2011-2013** : **comblé** — crédits totaux du **ministère** par titre (budget 2013, G1.1 a) ;
- **2012-2024** : crédits/exécution de **mission** (note parente § 1.1, familles PAP/RAP — périmètre
  distinct du ministère) ;
- **2024** : crédits votés 1 051,0 MD (LF) ; **exécution manquante** (RAP non publié) ;
- **2025-2026** : votés/prévisions CDMT ; **exécution manquante**.

**Crédits du ministère / mission Équipement** :
- **≤ 2010** : trou ;
- **2011-2013** : **comblé** — crédits totaux du **ministère de l'Équipement** par titre (budget 2013,
  G1.1 b), périmètre large (routes + hydraulique + fonds logement) ;
- **2014-2017** : budgets du ministère présents mais **périmètre recomposé** (Équipement+Environnement,
  puis +Habitat/Aménagement) — **non homogène**, à traiter avec note de concordance ;
- **2014-2023** : exécution/votés de **mission** « Équipement et Habitat » (note parente § 1.2) ;
- **2024-2026** : votés/prévisions ; **exécution manquante** (RAP non publié).

### G1.4 Références candidates (CSL-JSON)

**Déjà présentes** (réutiliser) : `minfin-budget-transport-2013`…`-2017` (budgets du ministère du
Transport, `precis/fr/compensation/references.json`) — **couvrent aussi le tableau de crédits totaux
du ministère de G1.1 a**, pas seulement la ligne soutien. Vérifier que la clé `-2013` pointe bien
`2013_budget_ministre_transport_jd59.pdf`.

**À créer** — budgets du ministère de l'Équipement (source des crédits totaux de G1.1 b). Copies
locales et SHA-256 au catalogue `tunisia-data/sources/minfinances-portail-ancien-urls.csv` :

```json
[
  {
    "id": "minfin-budget-equipement-2013",
    "type": "report",
    "title": "Budget de l'État pour 2013 — ministère de l'Équipement (ميزانية وزارة التجهيز)",
    "title-short": "Budget ministère Équipement 2013",
    "author": [{"literal": "Tunisie, ministère des Finances"}],
    "issued": {"date-parts": [[2012, 11]]},
    "publisher": "Ministère des Finances",
    "URL": "http://v2.portail.finances.gov.tn/index.php?option=com_jdownloads&Itemid=613&view=finish&cid=38&catid=1&lang=fr",
    "note": "Crédits totaux du ministère par titre, p. 1-2 : 2011 réalisation 930,116 MD, 2012 LF 1 278,955, 2013 prévision 1 366,041. Copie locale 2013_budget_equipement_jd38.pdf, SHA-256 ebd87f539b398fac1b8ef602ea6bd49d2ed9fae3787a57c56f8fbae11d948a11. Entrepôt tunisia-data, minfinances-portail-ancien-urls.csv.",
    "language": "ar"
  },
  {
    "id": "minfin-budget-equipement-2014",
    "type": "report",
    "title": "Budget de l'État pour 2014 — ministère de l'Équipement et de l'Environnement",
    "title-short": "Budget ministère Équipement et Environnement 2014",
    "author": [{"literal": "Tunisie, ministère des Finances"}],
    "issued": {"date-parts": [[2013, 12]]},
    "publisher": "Ministère des Finances",
    "URL": "http://finances.gov.tn/index.php?option=com_jdownloads&Itemid=712&view=finish&cid=548&catid=1&lang=fr",
    "note": "ATTENTION périmètre : ministère fusionné Équipement + Environnement (rupture de 2013). Copie locale 2014_budget_equipement_environnement_jd548.pdf, SHA-256 2cbc658079b073538d49978193c1ef6e43b728d2ed91745eb5ebfafc32509b55. Entrepôt tunisia-data.",
    "language": "ar"
  }
]
```

(Les budgets du ministère du Transport 2014/2015 — `2014_budget_transport_jd635.pdf` SHA-256
d96459af…, `2015_budget_transport_ar_jd814.pdf` SHA-256 af550434… — sont déjà au catalogue et
peuvent recevoir les clés `minfin-budget-transport-2014`, `-2015` sur le même modèle.)

### G1.5 Lacunes résiduelles

- **Avant 2011** (Transport et Équipement) : crédits par ministère **non atteignables** dans l'état
  de l'entrepôt — éditions de budget par ministère antérieures à 2013 absentes ; lois de finances
  2003-2012 présentes mais **sans ventilation par ministère**. Cible : éditions 2008-2012 des budgets
  par ministère (jdownloads du portail Joomla) ou **tableaux annexes « جدول أ » / répartition des
  crédits par département** des lois de finances — à chercher sur Wayback (cid jdownloads) et sur le
  miroir `dev.finances.gov.tn/old/`. Fiche proposée ci-dessous.
- **Exécution pré-GBO** (dépense réalisée par ministère avant 2012/2014) : **non atteignable** —
  pas de loi de règlement dans l'entrepôt, les bulletins d'exécution (`budget_execution/`) sont par
  titre/classification économique, **pas par ministère**. Les lois de règlement tunisiennes sont
  rares et tardives : fiche proposée ci-dessous.
- **Homogénéité 2014-2017 du ministère de l'Équipement** : périmètre recomposé (Environnement, puis
  Habitat/Aménagement) — extraction des totaux à faire **à l'image** (couche texte en formes
  arabes présentées, fragile), avec note de concordance, avant toute citation littérale.
- **Exécution 2024-2026** des deux missions : RAP non publiés (G1.2). Relancer dès parution.

### G1.6 Recherches infructueuses — fiches proposées (à créer via `scripts/recherches.py`, NE PAS éditer `docs/recherches.yml` ici)

**Passe à ajouter à la fiche existante** `r-transport-execution-rap-2024-2026` (note parente § 7) :

```
  passe:
    date: 2026-11-10
    resultat: aucun
    couverture: >
      Wayback Machine de nouveau en ligne ce jour. finances.gov.tn/fr/pap_rap : 200,
      ne liste que les PAP 2024 (prévisions), aucun RAP 2024/2025 Transport ni MEH.
      gbo.tn/fr/pap_rap : 404 (page déplacée). CDX finances.gov.tn et gbo.tn
      (sites/default/files, filtre RAP.*(transport|MEH|quipement)) : aucune capture.
      RAP 2024-2026 non publiés.
    couvert_jusqu_au: 2026-11-10
    sources: [finances.gov.tn, gbo.tn, web.archive.org]
```

**Fiche nouvelle proposée** (avant-GBO, crédits par ministère < 2011) :

```
- id: r-transport-equipement-budgets-ministere-avant-2011
  objet: >
    Crédits des ministères du Transport et de l'Équipement avant 2011 (budgets de l'État par
    ministère, éditions 2008-2012 ; ou tableaux « جدول أ » / répartition par département des lois
    de finances 2003-2012), pour prolonger avant 2011 la série des crédits totaux du ministère
    (fonctionnement + développement par titre) ouverte par les budgets 2013-2017.
  ou: [dev.finances.gov.tn/old, web.archive.org, finances.gov.tn]
  requetes:
    motifs_url:
      - "v2.portail.finances.gov.tn/index.php?option=com_jdownloads&cid=NNN (budgets ministères 2008-2012)"
      - "dev.finances.gov.tn/old/portail/publications/*budget*transport*"
      - "dev.finances.gov.tn/old/version2/images/*budget*equipement*"
    cdx:
      - 'curl "http://web.archive.org/cdx/search/cdx?url=finances.gov.tn*&matchType=domain&filter=original:.*(budget).*(transport|equipement|tajhiz|naql).*&output=text&fl=original,timestamp&collapse=urlkey&limit=200"'
    plein_texte:
      - "LF 2003-2012 : chercher le tableau annexe de répartition des crédits de paiement par département (جدول أ)"
  passe:
    date: 2026-11-10
    resultat: aucun
    couverture: >
      Entrepôt : budgets par ministère du portail ancien ne descendent qu'à l'édition 2013
      (rubrique budgets_ministeres, minfinances-portail-ancien-urls.csv). Lois de finances
      2003-2012 présentes mais sans ventilation par ministère (vérifié sur 2011_loi_finances_jd774.pdf :
      articles et totaux par titre/partie de l'État seulement). Éditions de budget par ministère
      antérieures à 2013 et tableaux annexes des LF : non recherchés en profondeur ce jour.
    couvert_jusqu_au: 2013-12-31
    sources: [minfinances-portail-ancien]
```

**Fiche nouvelle proposée** (exécution pré-GBO par ministère) :

```
- id: r-transport-equipement-execution-ministere-avant-2012
  objet: >
    Dépense RÉALISÉE (exécution) des ministères du Transport et de l'Équipement avant 2012/2014,
    par ministère — via lois de règlement (قانون غلق الميزانية / تصفية) ou rapports de la Cour des
    comptes sur l'exécution du budget de l'État.
  ou: [iort.gov.tn, finances.gov.tn, courdescomptes.nat.tn, web.archive.org]
  requetes:
    motifs_url:
      - "finances.gov.tn + 'loi de règlement' / 'قانون غلق ميزانية الدولة' pour l'année N"
    plein_texte:
      - "JORT : loi de règlement du budget (loi de clôture), année 2008-2013, tableau d'exécution par département"
  passe:
    date: 2026-11-10
    resultat: aucun
    couverture: >
      Entrepôt : aucune loi de règlement ; les bulletins d'exécution (budget_execution/) sont par
      titre et classification économique, pas par ministère. Non recherché en profondeur ce jour.
    couvert_jusqu_au: 2013-12-31
    sources: [minfinances-portail-ancien]
```

### G1.7 À verser à l'entrepôt `tunisia-data` (index/playbook — propositions, pas d'édition ici)

- **Index des CDMT de mission** (`ministere-transport-equipement-habitat.md`, proposé par la note
  parente § 6 bis) : **ajouter une seconde sous-table « Crédits totaux du ministère, budgets
  pré/para-GBO »** indiquant que les budgets 2013 (jd59 Transport, jd38 Équipement) portent les
  crédits totaux du ministère par titre pour **2011-2013** (réal/LF/prév), et que les éditions 2014+
  changent de périmètre ministériel.
- **Playbook `chercher-des-donnees-tunisie.md`** : ajouter « les **budgets de l'État par ministère**
  (rubrique `budgets_ministeres` du portail ancien) donnent, en tête de fascicule, un tableau des
  **crédits totaux du ministère par titre sur 3 ans** (réal N-2, LF N-1, prév N) — un seul budget
  reconstitue 3 années ; **le périmètre ministériel change d'une édition à l'autre** (fusions
  Équipement+Environnement+Habitat), recouper les intitulés avant de chaîner ».
