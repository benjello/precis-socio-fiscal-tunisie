# Note documentaire — Livre « L'environnement », Q3 : série budgétaire longue de la dépense publique d'environnement

Rôle : documentaliste. Date : 11 novembre 2026. Branche `chantier/environnement-livre`.
Budget du ministère chargé de l'environnement sur la plus longue période constructible, malgré les
changements de rattachement ; transferts du budget de l'État aux établissements sous tutelle (ONAS
d'abord). Familles de chiffres gardées séparées ; aucun ratio PIB calculé.

L'essentiel vient du **local** `tunisia-data` (PDF GBO et annexes de lois de finances, récupérations
des 4 et 10 novembre 2026).

---

## 0. Pièges levés d'emblée

- **ANPE = Agence nationale de protection de l'environnement** (loi n° 88-91). Jamais l'agence de
  l'emploi.
- Dans les fichiers GBO, **« MIME » = ministère de l'Industrie, des Mines et de l'Énergie**, PAS
  l'environnement. Le fichier `2024-06_RAP FR-2022-MIME- 141123.pdf` rangé dans le dossier
  `environnement/` est en réalité le RAP **industrie-énergie** 2022. À ne pas confondre avec le vrai
  RAP environnement 2022 (`2023-06_RAP ENVIRONNEMENT 202202.pdf`). *Report à `tunisia-data`.*

---

## 1. Depuis quand le département existe-t-il ? Histoire du périmètre

Source primaire institutionnelle : **ministère de l'Environnement, « Cadre juridique et
institutionnel »**, http://admin.environnement.gov.tn/ministere/cadre-juridique-et-institutionnel
(consulté le 11/11/2026 ; MAJ page 22/05/2026).

| Date / texte | Fait |
|---|---|
| Loi n° **88-91** du 2 août 1988 | Création de l'**ANPE** ; introduit les principes du droit de l'environnement. |
| **1991** | Premier **ministre chargé de l'environnement** → naissance du département. |
| Décrets n° **93-303** et **93-304** du 1er fév. 1993 | Attributions et organisation du **MEAT**. CNDD créée la même année. |
| MEAT **1991-2002** | Environnement **+ aménagement du territoire**. |
| **2002-2004** | Environnement rattaché au **MAERH** (agriculture) — pas de ministère autonome. |
| MEDD **2004-2011** | **Ministère de l'environnement et du développement durable**. |
| Décret du 10 mars 2011 ; décret n° 2011-4796 du 29 déc. 2011 | Fusion brève avec l'agriculture (mai 2011), puis ministère **autonome**. |
| Décret n° **2013-1372** du 15 mars 2013 | Environnement **confié au ministre de l'Équipement** + secrétariat d'État. |
| Décret n° **2014-413** du 3 fév. 2014 | **MEATDD**. |
| **Février 2015** | **MEDD** réapparaît ; autonome jusqu'en juillet 2016. |
| Décret n° **2016-107** du 27 août 2016 | **Ministère des affaires locales et de l'environnement** ; environnement **annexé aux affaires locales**. |
| Décret n° **2020-19** du 27 fév. 2020 | Département **autonome** (brièvement). |
| Décret n° **2020-313** du 15 mai 2020 | « MEDD » **renommé « ministère de l'environnement »**. |
| Décret n° **2020-84** du 2 sept. 2020 | De nouveau **affaires locales et environnement**. |
| **11 octobre 2021** (gouvernement Bouden) | **Ministère de l'environnement** autonome. Depuis, autonome. |
| Attributions en vigueur | Décret n° **2005-2933** (abroge le 93-303). Organisation : décret n° **2006-898**, mod. 2020-313 et 2022-488. Services extérieurs : décret n° **94-1636** (six directions régionales). |

**Six organismes sous tutelle** (ordre de création) : **ONAS** (1974, réorg. 1993 loi 93-41) ;
**ANPE** (1988) ; **APAL** (loi 95-72) ; **CITET** ; **BNG** (Banque nationale des gènes, 2003) ;
**ANGed** (2005).

> **Conséquence pour la série budgétaire** : trois régimes de périmètre se succèdent — (a)
> environnement + aménagement/développement durable (≤ 2016) ; (b) **affaires locales + environnement**
> (2016-2020, dominé par les transferts aux collectivités, 3-6× l'environnement) ; (c) **environnement
> autonome** (2021→). **Aucune de ces trois phases ne se chaîne muettement aux autres.**

---

## 2. Série A — budget « classique par titre » (JORT), avant GBO (votés, MD)

Fascicules « budget du ministère », couche texte. Fichiers
`data/raw/minfinances/portail_ancien/budgets_ministeres/` (catalogués
`sources/minfinances-portail-ancien-urls.csv`). Unité : millions de dinars (total = gestion +
développement + comptes spéciaux).

| Exercice | Intitulé | Gestion | Dév. | CST | **Total** | Fichier |
|---|---|---:|---:|---:|---:|---|
| 2013 | Environnement | 40,1 | 157,1 | 49,0 | **246,3** | `2013_budget_environnement_jd36.pdf` |
| 2014 | **Équipement + Environnement** (fusionnés) | 169,7 | 1 057,4 | 71,0 | **1 298,0** (combiné) | `2014_budget_equipement_environnement_jd642.pdf` |
| 2016 | Environnement et dév. durable | 43,2 | 119,2 | 20,0 | **182,4** | `2016_budget_environnement_developpement_durable_ar_jd1010.pdf` |
| 2017 | (titre) Env. et dév. durable ; (contenu) déjà « affaires locales » | 476,8 | 239,8 | 124,0 | **840,6** | `2017_budget_environnement_developpement_durable_ar_jd1175.pdf` |

Pièges : **2014** non isolable (équipement + environnement réunis) → trou honnête 2014-2015 en
périmètre environnement seul. **2017** : 182 → 840 vient de l'annexion des affaires locales, non
d'une croissance de l'environnement. Le **programme « Environnement et qualité de vie »** isolé vaut
~150,4 MD (2016) et ~160,6 MD (2017) — voir Série C.

---

## 3. Série B — budget de la **mission** GBO (crédits de paiement), 2017-2025

RAP et budgets de mission, `gbo.tn`/`finances.gov.tn` (récupérations 4 et 10/11/2026). MD, hors
ressources propres des établissements.

| Exercice | Périmètre | LF voté (MD) | Réalisé (MD) | Source |
|---|---|---:|---:|---|
| 2017 | Affaires locales et environnement | 716,6 | 700,6 | RAP 2017 |
| 2018 | Affaires locales et environnement | 887,4 | 978,1 | RAP 2018 |
| 2019 | Affaires locales et environnement | 1 006,3 | 1 101,7 | RAP 2019 |
| 2020 | Affaires locales et environnement | 1 156,9 (init.) ; 844,3 (LFC) | 916,8 | RAP 2020 ; budget-mission |
| 2021 | **Rupture** : voté aff. loc.+env ; scindé → **environnement seul** | 1 230,0 (voté) ; ~308,6 (env. seul) | 383,0 (env. seul) | budget-mission ; RAP 2021 |
| 2022 | Environnement seul | 350,0 | 350,9 | RAP 2022 |
| 2023 | Environnement seul | 414,6 | ~398,6 | budgets-mission LF2024/LF2025 |
| 2024 | Environnement seul | 459,4 | n.d. (RAP 2024 non publié) | budget-mission |
| 2025 | Environnement seul | 466,0 | — | budget-mission LF2025 |

**Ruptures de périmètre (trait vertical sur la figure)** : (1) ≤2016→2017 entrée des affaires
locales (×4-5) ; (2) **2020→2021 scission des affaires locales** en cours d'exécution — la LF 2021
votée à 1 230 MD, le RAP 2021 ne rend compte que de l'environnement seul (383 MD) : **ne jamais
tracer 2020→2021 comme une chute** ; (3) depuis 2022, mission ≈ environnement proprement dit
(350 → 466 MD, homogène). **Caveat 2020** : LF init. 1 156,9 / LFC 844,3 / réalisé 916,8 — à relire
à l'image.

---

## 4. Série C — programme « Environnement et développement durable » (colonne vertébrale la plus homogène)

Le programme n° 1 de la mission traverse les changements de rattachement : c'est l'environnement
« pur ».

| Exercice | Programme 1 — voté (MD) | Réalisé (MD) | Source |
|---|---:|---:|---|
| 2016 | ~150,4 | n.d. | budget ministère 2016 |
| 2017 | 160,6 | 160,9 | RAP 2017 |
| 2018 | 201,9 | 256,5 | RAP 2018 (prog. 1 + prog. 2) |
| 2019 | 237,7 | 253,3 | RAP 2019 |
| 2020 | 340,8 | 417,9 | RAP 2020 |
| 2021 | 238,6 | 321,9 | RAP 2021 |
| 2022 | 338,7 | 340,1 | RAP 2022 |

**Caveat d'homogénéité (à porter dans la prose)** : à partir de **2020**, l'exécution gonfle
(340,8 voté / 417,9 réalisé) parce que le programme **absorbe l'exécution de deux fonds spéciaux du
Trésor** — fonds de protection de l'environnement et de l'esthétique urbaine, et fonds de lutte
contre la pollution (RAP 2020). **La bosse 2020 est partiellement un artefact de périmètre de fonds**,
pas une hausse de la dépense récurrente. → recoupe directement Q4.

---

## 5. Transferts du budget de l'État aux établissements sous tutelle

### 5.1 Annexe 8 (transferts par établissement) — série reconstruite, triangulée et auto-validée

Source : min. Finances, **« Rapport sur les transferts et les garanties au profit des entreprises et
établissements publics » (annexe n° 8 du PLF)**, bloc **وزارة البيئة**. Fichiers
`data/raw/caisses/minfin/annexe8_transferts_LF{2023,2024,2025}.pdf` (catalogués
`sources/minfin-transferts-par-etablissement.md`). Unité d'origine : mille dinars ; donné en MD.
Datation des colonnes **triangulée** (recoupement des réalisations stables) et **validée par somme**
(ONAS+ANPE+ANGed+CITET+APAL = total وزارة البيئة imprimé : exact pour 2022, 2023, 2025). Mapping :
LF2023 = 2020-2023 ; LF2024 = 2021-2024 ; LF2025 = 2022-2025.

| Établissement | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 (LF) |
|---|---:|---:|---:|---:|---:|---:|
| **ONAS** | 173,8 | 263,3 | 205,2 | 199,2 | 218,6 | **334,5** |
| **ANPE** | 17,1 | 18,0 | 18,4 | 18,3 | 18,5 | 20,1 |
| **ANGed** | 86,2 | 99,9 | **3,1** | 92,3 | 116,4 | 47,0 |
| **CITET** | 3,7 | 4,9 | 3,7 | 5,4 | 5,2 | 6,1 |
| **APAL** | 22,1 | 13,4 | 11,3 | 13,9 | 12,0 | 23,3 |
| **TOTAL ministère** | **302,8** | **399,6** | **241,7** | **329,0** | **370,8** | **431,0** |

*(2020-2024 = réalisations ; 2025 = LF. Statuts منجز/وقتي/تقديري à relever colonne par colonne.)*

À relever pour la prose : **ONAS écrase tout** (57-76 % des transferts chaque année — poste central) ;
**ANGed chute à 3,1 MD en 2022** (anomalie, probable reclassement/décalage — à élucider) ; APAL,
CITET petits et stables ; ANPE stable ~18-20 MD. Le total des transferts **n'est pas le budget de la
mission** (Série B) : ne pas additionner.

### 5.2 Annexe 9 (rapport sur les entreprises publiques) — ONAS, série déjà vérifiée (garder séparée)

Transcription figée `sources/transcriptions/entreprises-publiques-transferts-par-entreprise.csv`.
**Périmètre d'échantillon différent de l'annexe 8 → ne pas épisser.**

| Année | ONAS (MD) | Statut | Édition |
|---|---:|---|---|
| 2017 | 58,0 | réalisé | LF2021 (concept plus étroit) |
| 2018 | 59,4 → **155,9** | réalisé | LF2021 vs LF2022 |
| 2019 | 97,7 → **210,7** | réalisé | LF2021 vs LF2022/LF2023 |
| 2020 | 201,3 | réalisé | LF2023/LF2024 |
| 2021 | 222,5 | réalisé | LF2024 |
| 2022 | 185,5 | provisoire | LF2024 |

Raccord muet à proscrire pour 2018-2019 : LF2021 (59,4/97,7) vs LF2022+ (155,9/210,7) = deux
concepts. **Retenir la série LF2022+** et ignorer LF2021 pour le chaînage. Croisement annexe 8 ↔
annexe 9 (ONAS) : écarts 15-40 MD, périmètres distincts — **les deux séries coexistent, ne
fusionnent jamais**. Préférer l'annexe 8 (se somme au total ministériel, couvre toutes les agences).

### 5.3 SONEDE (eau potable — dans le périmètre « l'eau reste », mais tutelle Agriculture)

Annexe 8, bloc ministère de l'Agriculture, ligne الشركة الوطنية لاستغلال وتوزيع المياه :

| | 2020 | 2022 | 2023 | 2024 | 2025 (LF) |
|---|---:|---:|---:|---:|---:|
| **SONEDE** (MD) | 80,8 | 171,1 | 224,1 | 50,0* | 217,955 |

*(2024 = 50,0 à vérifier — paraît bas/prévisionnel.)* SONEDE **sous tutelle Agriculture**, pas
environnement : réserve de domicile à signaler dans le chapitre « eau ».

### 5.4 Fonds spéciaux et garanties (familles distinctes)

- Fonds de protection de l'environnement et de l'esthétique urbaine, et fonds de lutte contre la
  pollution : exécutés via le programme 1 (RAP 2020). Recettes/dépenses au tableau A : voir Q4.
- Garanties de l'État au secteur eau-assainissement (annexe 8 LF2025) : prêts garantis à l'ONAS —
  AFD 50 M€ (24/09/2019, 4e tranche assainissement rural) ; 113,6 M€ (02/06/2023). **Famille
  « garanties » — ne jamais additionner aux transferts.**

---

## 6. Raisonnement de série

- Série homogène unique **impossible** (trois périmètres) → trois séries parallèles étiquetées, non
  chaînées (A/B/C).
- La plus exploitable pour « ce que pèse l'environnement » : **programme 1 (Série C)**, complété par
  la mission entière à partir de 2022 (B). Trous assumés : 2014-2015 (non isolable), 2023-2025 du
  programme 1 (≈ mission).
- **Transferts** : la série **annexe 8 (§5.1) est la plus solide** (triangulée, auto-validée par
  somme, cinq agences 2020-2025). **Aucune approximation nécessaire** ; incertitudes résiduelles :
  statuts des colonnes à figer, anomalie ANGed 2022, extension avant 2020 (annexes 8 LF2020-LF2022
  non lues).
- Écart ONAS annexe 8 vs annexe 9 : 15-40 MD, borné, documenté, ne renverse aucune lecture. **Note
  de concordance ONAS** recommandée (annexe 8 / annexe 9 / subvention d'exploitation).
- Subvention d'exploitation ONAS (compte de résultat, `grandeurs-onas.csv`) : 12,5 (2017), 13,8
  (2018), 135,2 (2020) MD — encore un autre concept, à tenir à part.

---

## 7. Références candidates (CSL-JSON)

> À vérifier dans les `references.json` avant ajout. Plusieurs annexes LF existent déjà
> (entreprises publiques / fiscalité).

```json
[
  {"id":"me-cadre-juridique-institutionnel","type":"webpage","title":"Cadre juridique et institutionnel","container-title":"Ministère de l'Environnement (Tunisie)","URL":"http://admin.environnement.gov.tn/ministere/cadre-juridique-et-institutionnel","accessed":{"date-parts":[[2026,11,11]]},"issued":{"date-parts":[[2026,5,22]]}},
  {"id":"minfin-annexe8-transferts-garanties","type":"report","title":"Rapport sur les transferts et les garanties au profit des entreprises et établissements publics (annexe n° 8 au projet de loi de finances)","author":[{"literal":"Tunisie. Ministère des Finances"}],"publisher":"Ministère des Finances","URL":"https://www.finances.gov.tn/fr/les-indicateurs/loi-de-finances","note":"Éditions LF2020 à LF2025 ; bloc « وزارة البيئة » lu pour ONAS, ANPE, ANGed, CITET, APAL.","accessed":{"date-parts":[[2026,11,4]]}},
  {"id":"minfin-annexe9-entreprises-publiques","type":"report","title":"Rapport sur les entreprises publiques (annexe n° 9 au projet de loi de finances)","author":[{"literal":"Tunisie. Ministère des Finances"}],"publisher":"Ministère des Finances","note":"Transferts par entreprise (tableaux 31/38/40/45) ; transcription tunisia-data."},
  {"id":"gbo-rap-environnement","type":"report","title":"Rapport annuel de performance — mission Environnement (et Affaires locales, selon l'exercice)","author":[{"literal":"Tunisie. Ministère chargé de l'Environnement"}],"publisher":"Portail du budget par objectifs (gbo.tn)","URL":"http://www.gbo.tn/","note":"RAP 2017 à 2023 ; PAP et budgets de mission 2015-2025."}
]
```

(Les décrets d'organisation 2005-2933 / 2006-898 / 88-91 sont déjà proposés en Q1 — ne pas
dupliquer.)

---

## 8. Notions à glossaire (propositions — ne pas modifier `glossaire.yml`)

- **ANPE** (désambiguïsée, loi 88-91), **ANGed** (2005-2317), **APAL** (95-72), **CITET**,
  **MEAT/MEDD** (noms successifs du ministère).
- **Fonds de protection de l'environnement et de l'esthétique urbaine** ; **fonds de lutte contre
  la pollution** (fonds spéciaux exécutés via le programme environnement ; voir Q4).
- (`onas`, `taxe-protection-environnement` existent déjà.)

---

## 9. Lacunes et trous de série assumés

1. 2014-2015 (environnement seul) non isolable → case vide sourcée.
2. Statuts des colonnes de l'annexe 8 (réalisé/provisoire/estimé) non relevés — à figer.
3. ANGed 2022 = 3,1 MD : anomalie non expliquée.
4. Transferts aux agences avant 2020 : annexes 8 LF2020-LF2022 (bloc affaires locales + env.) non
   lues → série commence à 2020.
5. Caveat mission 2020 (1 156,9 / 844,3 / 916,8) non tranché.
6. RAP 2024 non publié → réalisé 2024 manquant ; PAP 2026 manquant.
7. Fonds spéciaux (Q4) : recettes/dépenses au tableau A non extraites.
8. Subvention d'exploitation ONAS : 2017, 2018, 2020 lues ; 2019, 2021-2023 à prolonger.

---

## 10. Reports (destination durable — à router selon `docs/backlog-routage.md`)

**Vers `tunisia-data`** : proposer une transcription figée
`transcriptions/minfin-transferts-environnement.csv` (bloc وزارة البيئة, 2020-2025, mapping d'années
documenté) + ligne SONEDE ; ajouter l'index des tableaux à `minfin-transferts-par-etablissement.md` ;
note de concordance ONAS (annexe 8 / annexe 9 / subvention d'exploitation) ; signaler le mauvais
classement de `2024-06_RAP FR-2022-MIME- 141123.pdf` (= industrie-énergie).

**Backlog (propositions, ne pas écrire dans `backlog-precis.md`) :**
- [env] Lire les annexes 8 LF2020-LF2022 (bloc affaires locales + environnement) pour prolonger les
  transferts avant 2020.
- [env] Extraire les fonds spéciaux « protection de l'environnement et esthétique urbaine » et
  « lutte contre la pollution » au tableau A (Q4).
- [env] Élucider l'anomalie ANGed 2022 (3,1 MD) et le caveat mission 2020.
- [env] Prolonger la subvention d'exploitation ONAS 2019, 2021-2023 (annexes 9 arabes).
- [env] Q1 : lecture au JORT des textes fondateurs (voir note Q1).

**Chiffres-clés pour le rédacteur** : département de l'environnement depuis **1991** (organisé 1993) ;
budget propre (programme environnement) **~150 MD (2016) → ~466 MD (LF 2025)** ; **ONAS = 57-76 % des
transferts du ministère** (173,8 → 334,5 MD de 2020 à 2025) ; trois régimes de périmètre interdisant
toute série mission chaînée muette entre 2016 et 2021.
