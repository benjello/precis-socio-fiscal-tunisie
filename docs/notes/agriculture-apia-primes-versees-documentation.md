# Documentation — primes d'investissement agricole **versées (décaissées)** par l'APIA

Rôle : documentaliste. Date : 11 novembre 2026. Livre : « L'agriculture — le soutien au
producteur », chapitre 5 (encouragements à l'investissement). Objet : obtenir une série homogène des
primes d'investissement agricole **effectivement versées / décaissées** par l'APIA — par opposition
aux primes **approuvées (octroyées, engagées)** que portent déjà le portail agridata.tn et le
chapitre `_investissement.qmd` (série approuvée 2010-2016). État antérieur (note
`agriculture-investissement-documentation.md`, §3) : **un seul point de primes versées connu**,
54 MD en 2009 (Banque mondiale 2014).

**Résultat : série des décaissements TROUVÉE** pour 2018-2023, dans les **rapports d'activité annuels
de l'APIA** (تقرير نشاط الوكالة, en arabe), section « suivi de la réalisation des projets et
**صرف المنح** [décaissement des primes] ». Ces rapports distinguent explicitement, dans leurs chiffres,
le **décaissé** (صرف المنح / أذون بالصرف) de l'**approuvé** (المصادق عليها). Documents récupérés et
indexés dans `tunisia-data/data/raw/apia/`.

---

## 1. Série des primes décaissées (APIA) — 2009, puis 2018-2023

Unité : million de dinars (MD). Source APIA = texte arabe du rapport d'activité de l'année
(couche texte lue par `pdftotext -layout`, chiffres en caractères occidentaux dans l'original).

| Année | Primes **décaissées / ordonnancées** (MD) | Nb d'ordres de paiement (أذون بالصرف) | Libellé-source exact | Source |
|---|---:|---:|---|---|
| 2009 | **54** | — | « primes versées par l'APIA » (disbursed) | Banque mondiale 2014 (`banquemondiale2014-revolution-inachevee`, déjà `#tbl-df-bm-cout`) |
| 2018 | **52,823** | 3 543 | « توجيه أذون بصرف المنح … بقيمة جملية تقدر بـ 52,823 م.د » (ordres de paiement de primes émis) | Rapport d'activité APIA 2018, p. 1 (synthèse) et section III-1 |
| 2019 | **112,535** | 4 368 | « 4368 إذن بالصرف لمنح بقيمة 112,535 … في حدود الاعتمادات المتوفرة » (dans la limite des crédits disponibles) | Rapport d'activité APIA 2019, section III-1 |
| 2020 | **~62** (décaissé) / 63 (ordonné, 2351 ordres) | 2 351 | « تم صرف قيمة تقدر بـ 62 م د » ; « 2351 إذن بالصرف … بقيمة في حدود 63 م د » | Rapport d'activité APIA 2020, synthèse p. 2 et §III-1 |
| 2021 | **89** | 2 875 | « صرف منح الاستثمار بقيمة 89 م د لفائدة 2875 باعث » (décaissement des primes d'investissement) | Rapport d'activité APIA 2021, synthèse p. 2 et §III-1 (89,2 MD, 2875 ordres) |
| 2022 | **44,18** | 1 472 | « صرف منح الاستثمار بقيمة 44.18 م د موضوع 1472 إذن بالصرف » | Rapport d'activité APIA 2022, §III-1 (dont ~41,5 MD envoyés à la BNA, reliquat payé début 2023) |
| 2023 | **60,1** | 1 836 | « صرف منح الاستثمار بقيمة 60,1 م د موضوع 1836 إذن بالصرف » | Rapport d'activité APIA 2023, synthèse et §III-1 |

### Contrôle décaissé ≠ approuvé (décisif)
Les **mêmes** rapports, et les **bulletins statistiques annuels** (`ANNEE_YYYY.pdf`), donnent les
primes **approuvées** (المنح المصادق عليها / المنح, en milliers de dinars) — bien plus hautes :
2019 = 187,3 MD ; 2020 = 146,9 MD ; 2021 = 162,5 MD ; 2022 = 168,2 MD ; 2023 = 139,5 MD (ces quatre
dernières recoupent exactement le jeu agridata « indicateurs » national 2021-2026). **Le décaissé
(44-112 MD) est donc nettement inférieur à l'approuvé (139-187 MD) la plupart des années**, ce qui
confirme qu'il s'agit bien du versant **versements**, pas d'un doublon de l'approuvé. (L'approuvé
post-2016, ~150-210 MD, est lui-même en rupture avec l'approuvé pré-2016 d'agridata, ~55-93 MD :
effet de la **loi de l'investissement n° 2016-71** — hors objet de cette note.)

### Homogénéité : série du décaissement, avec une couture de concept à signaler
- **Même famille, même émetteur, même unité** (APIA, rapport d'activité, MD) de 2018 à 2023 : la
  série est homogène de ce côté.
- **Nuance de concept à porter dans le rendu** : pour **2018-2019** le rapport chiffre les
  **ordres de paiement de primes émis** (أذون بصرف المنح, « ordonnancé ») ; pour **2020-2023** il
  chiffre le **décaissement effectif** (صرف المنح) — tout en précisant que les ordres sont émis
  « dans la limite des crédits disponibles ». Les deux notions sont **adjacentes sur le versant
  versements** mais pas strictement identiques : chaque année un **reliquat de demandes prêtes mais
  non payées faute de crédits** subsiste (57 MD fin 2018 ; 53 MD fin 2020 ; 58,9 MD fin 2021). Le
  décaissé-caisse d'une année ≈ ordres exécutés de l'année, à ce décalage près. **À présenter donc
  comme « primes décaissées (ordres de paiement exécutés) »**, avec cette réserve, et non comme un
  décaissé-trésorerie certifié.
- **2019 = 112,5 MD** est un point haut (≈ double des voisins) : vraisemblable rattrapage d'arriéré
  (le rapport insiste « dans la limite des crédits disponibles »). À garder, signalé comme tel.
- **Raccord 2009 ↔ 2018** : le point 2009 (54 MD, Banque mondiale) et la série APIA 2018-2023 sont
  de **sources différentes** ; 2010-2017 reste un **trou** sur le décaissé (voir §4). Ne pas tracer
  une ligne continue 2009→2018 : laisser le trou honnête.

---

## 2. Documents récupérés et indexés (`tunisia-data/data/raw/apia/`)

Catalogue : `tunisia-data/sources/apia-agridata-urls.csv` (URL d'origine, SHA-256, date de collecte
= 2026-11-11). Toutes les URL vérifiées (HTTP 200) le 11/11/2026 sur `www.apia.com.tn`.

**Rapports d'activité annuels (source du décaissé)** — page `apia.com.tn/rapports-apia.html` :
- `apia_rapport_activite_2018.pdf` … `apia_rapport_activite_2023.pdf` (6 fichiers). SHA-256 au
  catalogue. Chemins d'origine : `/medias/files/Rapports-Apia/Rapport-ActivitEs-YYYY[.pdf].pdf`.

**Bulletins statistiques annuels (source de l'approuvé, confirme agridata)** — page
`apia.com.tn/statistiques-annuelles.html` :
- `apia_statistiques_annuelles_2018.pdf` … `_2025.pdf` (8 fichiers ; 2024 = `conjoncture/2024/ANNEE_2024_FIN.pdf`).

**Non encore récupérés** (repérés, à collecter si besoin) : rapports d'activité **2024** et **2025**
(non listés sur la page au 11/11/2026 ; seul le « Rapport statistique année 2024 » et des
présentations de conseil d'administration le sont) ; **antérieurs à 2018** (voir §4). Les
**tableaux de bord « conjoncture »** sont servis via Tableau Public (`public.tableau.com/app/profile/riadh.kouki`),
non téléchargeables en PDF.

---

## 3. Références CSL candidates

Déjà présente (réutiliser) : `banquemondiale2014-revolution-inachevee` (point 2009).

À créer (livre agriculture ; `type: report`, auteur APIA) :

```json
[
  {"id":"apia-rapport-activite-2018","type":"report",
   "title":"Rapport d'activité de l'APIA — année 2018 (تقرير نشاط الوكالة بعنوان سنة 2018)",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2019]]},
   "URL":"https://www.apia.com.tn/medias/files/Rapports-Apia/Rapport-ActivitEs-2018.pdf",
   "note":"Primes décaissées/ordonnancées 2018 : ordres de paiement de primes (أذون بصرف المنح) = 52,823 MD, 3543 ordres (synthèse p. 1 ; §III-1). Primes approuvées assignées 2018 = 211,4 MD. Copie locale : tunisia-data/data/raw/apia/apia_rapport_activite_2018.pdf (SHA-256 1551be3bcffdf1e32cf5aa78cab92c5493950db467a62683dc056618c9827ee2). Consulté le 11/11/2026."},

  {"id":"apia-rapport-activite-2019","type":"report",
   "title":"Rapport d'activité de l'APIA — année 2019",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2020]]},
   "URL":"https://www.apia.com.tn/medias/files/Rapports-Apia/Rapport-ActivitEs-2019.pdf.pdf",
   "note":"Décaissé/ordonnancé 2019 : 4368 ordres de paiement de primes = 112,535 MD (dans la limite des crédits disponibles), §III-1. Copie locale SHA-256 d62fbf9fcfd7778c0477e04ec567e263f1600d95027fb83eab2a713da4f2b09f. Consulté le 11/11/2026."},

  {"id":"apia-rapport-activite-2020","type":"report",
   "title":"Rapport d'activité de l'APIA — année 2020",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2021]]},
   "URL":"https://www.apia.com.tn/medias/files/Rapports-Apia/Rapport-ActivitEs-2020.pdf.pdf",
   "note":"Décaissé 2020 : ~62 MD (صرف منح) ; 2351 ordres ~63 MD ; reliquat >53 MD de demandes prêtes non payées fin 2020. Copie locale SHA-256 e2ddb9d1ec0a45edace5aad3ec7fbd73a2fd96a82b5ef41f77100bc65ff7e385. Consulté le 11/11/2026."},

  {"id":"apia-rapport-activite-2021","type":"report",
   "title":"Rapport d'activité de l'APIA — année 2021",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2022]]},
   "URL":"https://www.apia.com.tn/medias/files/Rapports-Apia/Rapport-ActivitEs-2021.pdf.pdf",
   "note":"Décaissé 2021 : صرف منح الاستثمار = 89 MD à 2875 bénéficiaires (89,2 MD, 2875 ordres, §III-1) ; reliquat 58,9 MD fin 2021. Copie locale SHA-256 7193dd3cf13dcdd77cd8d7493ced854b5e376f91cbf921721bb5d5b1d7eb696b. Consulté le 11/11/2026."},

  {"id":"apia-rapport-activite-2022","type":"report",
   "title":"Rapport d'activité de l'APIA — année 2022",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2023]]},
   "URL":"https://www.apia.com.tn/medias/files/Rapports-Apia/Rapport-ActivitEs-2022.pdf",
   "note":"Décaissé 2022 : صرف منح الاستثمار = 44,18 MD, 1472 ordres (dont ~41,5 MD envoyés à la BNA, reliquat payé début 2023), §III-1. Copie locale SHA-256 4803383c604a7f98c098d1faca9574ccff5eb942ba3da7839a0c3791a18cbf13. Consulté le 11/11/2026."},

  {"id":"apia-rapport-activite-2023","type":"report",
   "title":"Rapport d'activité de l'APIA — année 2023",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2024]]},
   "URL":"https://www.apia.com.tn/medias/files/Rapports-Apia/Rapport-ActivitEs-2023(1).pdf",
   "note":"Décaissé 2023 : صرف منح الاستثمار = 60,1 MD, 1836 ordres, §III-1. Copie locale SHA-256 004ef2bceee87fead20196478cf4b4108db67bc745f54391e55e8de6ad1bcd99. Consulté le 11/11/2026."},

  {"id":"apia-bulletin-statistique-annuel","type":"report",
   "title":"Bulletin statistique annuel de l'investissement agricole privé (APIA)",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2025]]},
   "URL":"https://www.apia.com.tn/statistiques-annuelles.html",
   "note":"Série des primes APPROUVÉES (المنح المصادق عليها, milliers de dinars) : 2019=187,3 ; 2020=146,9 ; 2021=162,5 ; 2022=168,2 ; 2023=139,5 MD. Recoupe le jeu agridata « indicateurs ». Éditions 2018-2025 collectées (tunisia-data/data/raw/apia/apia_statistiques_annuelles_YYYY.pdf). Consulté le 11/11/2026."}
]
```

---

## 4. Lacunes (établies, à ne pas combler par une valeur plausible)

1. **Décaissé 2010-2017** : non trouvé. Les rapports d'activité APIA en ligne ne remontent qu'à
   2018 (`rapports-apia.html`). Les **bulletins statistiques** (2018+) ne portent que l'approuvé.
   Antérieurs à 2018 : à chercher par Wayback (voir §6) ou par demande directe à l'APIA.
2. **Décaissé 2024-2025** : rapports d'activité 2024/2025 non encore publiés sur le site au
   11/11/2026 (seul le « Rapport statistique 2024 » et des présentations de conseil le sont). À
   relancer plus tard.
3. **Concept exact** : pour 2018-2019 la grandeur est « ordres de paiement émis » (ordonnancé) et
   pour 2020-2023 « décaissement » (صرف) ; le décaissé-trésorerie strict, année par année, n'est pas
   isolé des reliquats reportés. Écart borné par les reliquats cités (53-59 MD de demandes prêtes
   non payées en fin d'exercice) : l'ordonnancé d'une année sous-estime la demande solvable mais
   approche le cash réellement sorti, les ordres étant émis « dans la limite des crédits ».
4. **Cour des comptes sur l'APIA** : non recherché faute de temps ; piste pour un décaissé certifié
   (voir backlog).

---

## 5. Notions à glossaire (proposées, non écrites)

- **Prime d'investissement agricole — approuvée (octroyée) vs décaissée (versée)** : l'approuvée
  (المنح المصادق عليها) est l'engagement du comité d'octroi ; la décaissée (صرف المنح) est le
  versement effectif par la BNA sur ordre de paiement (إذن بالصرف) de l'APIA, dans la limite des
  crédits ouverts. Écart structurel entre les deux (reliquats reportés). Source : rapports
  d'activité de l'APIA.
- **Ordre de paiement de prime (إذن بالصرف)** : acte par lequel l'APIA mandate la BNA de payer la
  prime au bénéficiaire ; unité de compte du décaissement dans les rapports d'activité.

---

## 6. Recherche infructueuse → fiche `r-apia-primes-versees` (à enregistrer dans `docs/recherches.yml`)

La fiche était **proposée** dans `agriculture-investissement-documentation.md` §6 ; elle est ici
**partiellement résolue** (décaissé 2018-2023 trouvé) et reste **ouverte sur 2010-2017 et 2024-2025**.

```yaml
- id: r-apia-primes-versees
  objet: série des primes d'investissement agricole EFFECTIVEMENT VERSÉES (décaissées / ordonnancées) par l'APIA, année par année
  ou: [docs/notes/agriculture-apia-primes-versees-documentation.md, docs/notes/agriculture-investissement-documentation.md]
  requetes:
    plein_texte: ['صرف منح الاستثمار', 'أذون بصرف المنح', 'المنح المصروفة فعليا', 'rapport activité APIA décaissement primes']
    depuis: 2005-01-01
  passes:
  - date: 2026-11-11
    role: documentaliste
    sources: [apia.com.tn, web, wayback-cdx]
    couverture: >-
      apia.com.tn/rapports-apia.html : rapports d'activité annuels 2018-2023 récupérés (PDF arabe) ;
      le décaissé/ordonnancé des primes y est chiffré chaque année (2018=52,823 ; 2019=112,535 ;
      2020~62 ; 2021=89 ; 2022=44,18 ; 2023=60,1 MD). apia.com.tn/statistiques-annuelles.html :
      bulletins 2018-2025 = primes APPROUVÉES seulement. Point externe 2009=54 MD (BM 2014).
      NON trouvé : décaissé 2010-2017 (rapports d'activité en ligne remontent à 2018 seulement) ;
      décaissé 2024-2025 (rapports non publiés au 11/11/2026). CDX Wayback apia.com.tn (600 captures)
      et apia.nat.tn (ancien domaine, captures 2009-2022) repérés mais rapports d'activité anciens
      PAS encore sondés sur Wayback. Cour des comptes/APIA non interrogée.
    couvert_jusqu_au: 2026-11-11
    resultat: partiel
  a_faire:
    - sonder la Wayback (CDX + suffixe id_) de apia.com.tn/medias/files/Rapports-Apia/ et de l'ancien apia.nat.tn pour des rapports d'activité < 2018
    - récupérer les rapports d'activité APIA 2024 et 2025 dès parution
    - chercher un rapport de la Cour des comptes sur l'APIA (décaissé certifié)
    - demander à l'APIA la série décaissée 2010-2017 (ordres de paiement exécutés) directement
```

---

## 7. Backlog (à router par l'archiviste selon `docs/backlog-routage.md` — non écrit au backlog ici)

- **Décaissé APIA pré-2018** : Wayback CDX sur `apia.com.tn/medias/files/Rapports-Apia/*` et sur
  l'ancien domaine `apia.nat.tn` (captures 2009-2012, 2022) ; à défaut, demande directe à l'APIA.
- **Décaissé APIA 2024-2025** : relancer la page `rapports-apia.html` à parution.
- **Rupture de régime de l'approuvé** (loi 2016-71) : l'approuvé passe de ~55-93 MD (pré-2016,
  agridata) à ~150-210 MD (2018-2023, bulletins APIA) ; note de concordance à prévoir si le chapitre
  mobilise les deux périodes (différencier approuvé pré/post-2016 ET approuvé vs décaissé).
- **Références CSL** du §3 à verser dans `precis/fr/<livre-agriculture>/references.json`.
- **Fichiers rangés dans `tunisia-data`** : `data/raw/apia/` (14 PDF ajoutés le 11/11/2026) +
  catalogue `sources/apia-agridata-urls.csv` (14 lignes ajoutées).
- **Glossaire** : couple « prime approuvée / prime décaissée » + « ordre de paiement (إذن بالصرف) ».
