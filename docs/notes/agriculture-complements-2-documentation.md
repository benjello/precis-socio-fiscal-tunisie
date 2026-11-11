# Compléments documentaires 2 — PAP 2023 (budget) & ventilation des indemnités du fonds de calamités

Rôle : documentaliste. Date : 18 novembre 2026. Chantier « livre agriculture ».
Deux cibles indépendantes : (1) retrouver le **PAP 2023** de la mission Agriculture (chapitre 3) ;
(2) constituer la **ventilation datée des indemnités/déclarations du fonds de calamités par aléa**
(chapitre 7), à partir des sections d'activité CTAMA des *Rapports sur l'activité des Fonds Spéciaux*
déjà dans `tunisia-data`. Invariants respectés : `uv run` pour tout Python ; aucune donnée brute dans
git ; aucun PDF neuf téléchargé (toutes les sources étaient déjà dans l'entrepôt — rien dans /tmp
sauf du scratch CDX non-PDF) ; aucun fichier du précis touché.

---

## CIBLE 1 — PAP 2023 de la mission Agriculture, ressources hydrauliques et pêche

### Verdict : **NON TROUVÉ** — jamais mis en ligne sur gbo.tn / finances.gov.tn (preuve ci-dessous).
La prévision 2023 de la mission reste néanmoins **triangulée sur trois sources primaires** déjà
détenues (voir § 1.3), donc le chiffre que porterait le PAP 2023 est **sourcé sans lui**.

### 1.1 Ce qui a été cherché (couverture datée, URL vérifiées le 2026-11-18)

- **Entrepôt `tunisia-data` d'abord.** Le dossier agriculture de la récupération gbo.tn du 4 nov. 2026
  (`sources/gbo-recuperation-2026-11-04.csv`) couvre les PAP agriculture **2016, 2017, 2019, 2020,
  2021, 2022, 2024** et le budget-de-mission LF2020/2021/2022/2024/2025 — **pas de PAP 2023, pas de
  budget-de-mission LF2023**. La récup du 10 nov. ne contient aucune ligne agriculture.
- **Index Wayback (CDX) de gbo.tn, requête `urlkey:.*pap.*` sur `sites/default/files` (333 captures,
  interrogé le 2026-11-18 avant la panne temporaire d'Internet Archive).** Les PAP agriculture indexés
  sont **2015, 2017, 2018, 2019, 2020, 2021, 2022, 2024, 2025** — **2023 absent**. Or les PAP **2023
  d'une quinzaine d'autres missions** sont bien là (dossier `2023-01/` : affaires religieuses,
  enseignement supérieur, justice, santé, domaines de l'État, MFFES, MCDE… ; `2023-05/` tourisme,
  transport ; etc.). L'absence est donc **spécifique à l'agriculture**, pas un trou d'archivage général.
- **Miroir finances.gov.tn (CDX)** : une seule occurrence « PAP MAR … » = **PAP 2024** ; aucun PAP 2023.
- **Sondage direct gbo.tn (9 motifs d'URL plausibles, 2026-11-18)** : `2023-01/PAP 2023 Agriculture.pdf`,
  `…/PAP2023 agriculture.pdf`, `…/PAP 2023 MARHP.pdf`, `…/PAP 2023 MAR.pdf`, `2022-12/PAP 2023
  Agriculture.pdf`, `…/PAP 2023 agriculture version finale.pdf`, `2023-01/13 مهمة الفلاحة… .pdf`,
  `2022-12/13 مهمة الفلاحة.pdf`, `2023-01/مهمة الفلاحة… .pdf` → **tous HTTP 404**.

**Lecture.** Le PAP 2023 agriculture n'a, selon toute apparence, **jamais été publié** sur les portails
GBO/Finances (ni archivé par Wayback). À distinguer d'un simple échec de collecte : le même index liste
les PAP 2023 des autres missions et les PAP agriculture des années voisines. Cause probable : fascicule
non mis en ligne cette année-là (comme le RAP 2021 agriculture, autre manquant déjà constaté).

### 1.2 Confirmation de la valeur cible par sources primaires détenues (triangulation)

Le total **crédits de paiement, ressources de l'État, hors ressources propres** de la mission pour
l'exercice **2023** vaut **1 965 000 mille dinars (1 965 MDT)** — recoupé par **trois** documents
primaires déjà dans l'entrepôt, tous concordants :

| Source primaire (déjà détenue) | Repère exact | Valeur 2023 |
|---|---|---|
| **Rapport sur le budget de l'État 2023** (annexe PLF 2023) | `gbo-recup-2026-11-04/annexes-lf/2023-01_0002_0.pdf` ; tableau des budgets de mission, mission 13 « الفلاحة والموارد المائية والصيد البحري », ligne LF votée (déjà saisie dans `docs/notes/budget-missions-vote-2021-2025.csv`, ligne `2023,13`) | **1 965 000** (voté) |
| **RAP 2023** (ar), déjà dépouillé (note budget-compléments § 1.2) | pdf p. 7, « المجموع العام / اعتمادات الدفع », تقديرات 2023 (ق.م), « دون اعتبار الموارد الذاتية » | **1 965 000** (prévu) |
| **PAP 2024** (ar), déjà dépouillé (note-mère budget) | colonne 2023 de rappel | **1 965 000** |

Le chiffre du PAP 2023 absent est donc **connu et fiable** ; seul le **fascicule lui-même** (avec ses
objectifs/indicateurs de performance et sa ventilation par programme/sous-programme 2023) manque.

### 1.3 Références candidates (CIBLE 1)

Aucune nouvelle entrée CSL n'est requise : les trois sources de recoupement sont déjà cataloguées.
Si le rédacteur cite la valeur 2023, la **source première à mobiliser** est le *Rapport sur le budget
de l'État 2023* (ou le RAP 2023), **jamais** un « PAP 2023 » qui n'existe pas en ligne.

---

## CIBLE 2 — Ventilation des indemnités / déclarations du fonds de calamités, par aléa et par an

### Verdict : **TROUVÉ et constitué** (campagnes 2019-2020 à 2022-2023), sur source budgétaire primaire.
Les sections d'activité CTAMA des *Rapports sur l'activité des Fonds Spéciaux* (annexe 10 aux PLF)
donnent une ventilation **par campagne agricole**, avec le **nombre de déclarations éclaté par aléa**
(sécheresse / gelée) et une ventilation **par gouvernorat** des déclarations et des souscriptions. Les
**montants d'indemnités versées**, eux, sont donnés **par campagne** (non éclatés par aléa dans la
source) — mais les déclarations de gelée étant marginales, les indemnités sont **quasi intégralement
imputables à la sécheresse** (voir note de lecture).

### 2.1 Sources (toutes déjà dans `tunisia-data`, hors git ; famille budgétaire / ministère des Finances)

| Édition (PLF) | Fichier `data/raw/` | Campagnes couvertes | Pages du fonds (PDF) |
|---|---|---|---|
| LF 2022 (AR) | `gbo-recup-2026-11-04/annexes-lf/2022-02_ANNEXE_10_0.pdf` | 2019-2020 | 59-61 |
| LF 2023 (AR) | `gbo-recup-2026-11-04/annexes-lf/2023-01_8.pdf` | 2019-2020, 2020-2021 | 62-66 |
| LF 2024 (AR) | `gbo-recup-2026-11-04/annexes-lf/2024-01_التقرير حول نشاط الصناديق الخاصة ملحق عدد _10.pdf` | 2019-2020 → 2021-2022 | 45-51 |
| LF 2025 (AR) | `gbo/FST_LF2025_Annexe10_ar.pdf` | 2020-2021 → 2022-2023 | 43-47 |

Source citée dans les rapports : **Trésorerie Générale de la République tunisienne** (comptes) et
**CTAMA / مؤسسة «كتاما»** (activité). Lecture : `pdftotext -layout` (chiffres en caractères latins).
Les éditions **se recouvrent** : chaque campagne est confirmée par 2 à 3 rapports.

### 2.2 Déclarations de dommages, par campagne et **par aléa** (nombre de déclarations)

| Campagne agricole | **Total décl.** | **Sécheresse** (جائحة الجفاف) | **Gelée** (جائحة الجليدة) | Note | Source (p.) |
|---|---|---|---|---|---|
| **2019-2020** | **1 027** | 1 027 | 0 | *première campagne du fonds* ; 100 % sécheresse | LF2022 p.60-61 ; LF2024 p.50 |
| **2020-2021** | **1 679** | **1 648** | **31** | +6 décl. rejetées ; gelée = 467 kDT de dommages estimés | LF2023 p.65 |
| **2021-2022** | **2 039** | **2 015** | **24** | | LF2024 p.49-50 |
| **2022-2023** | **1 644** | 1 644 (grandes cultures) | 0 | +5 décl. sécheresse **arbres fruitiers** (grenadiers, Testour/Béja) laissées **en attente** (hors décret 2023-527) | LF2025 p.46 |

- **2020-2021, détail gelée (31 décl., 467 kDT)** : 7 en grandes cultures (Siliana, Béja, Manouba),
  8 en légumineuses (Siliana, Béja, Manouba), 16 en arbres fruitiers (Kef, Kasserine, Siliana,
  Kairouan) — LF2023 p.65.
- **Périmètre des aléas éligibles** (loi 2017-66, décret 2018-821) : inondations, tempêtes, vents,
  **sécheresse**, neige, **gelée**. Sur 2019-2023, **seules la sécheresse et la gelée** ont effectivement
  produit des déclarations ; aucune inondation/tempête/neige indemnisée sur la période.

### 2.3 Indemnités versées et dossiers, **par campagne** (unité : mille dinars = kDT)

Valeurs de l'édition la plus récente couvrant chaque campagne (LF2025 pour 2020-21→2022-23 ; LF2022/24
pour 2019-20). Le montant total annuel de l'« état du compte » (déjà dans la note calamités-ressources
§ 1.2) est **par année civile** du fonds ; le tableau ci-dessous est **par campagne** (les deux quasi
coïncident, chaque campagne étant indemnisée l'année civile suivante).

| Campagne | Décl. | Exploit. déclarées | Valeur dommages estimée/expertise (kDT) ⚠ | Dossiers indemnisés | Exploit. indemnisées | **Indemnités versées (kDT)** | Expertises (kDT) |
|---|---|---|---|---|---|---|---|
| 2019-2020 | 1 027 | 3 572 | 34 012,4 | 1 023 | 3 566 | **20 392** | 108 (an. 2020) |
| 2020-2021 | 1 679 | 4 539 | 19 950 / 33 250 ⚠ | 1 679 | 4 539 | **19 950** (≈ 19 992 an. 2021) | 113 |
| 2021-2022 | 2 039 | 6 267 | 47 561,7 | 1 998 | 6 078 | **28 400** | 169 |
| 2022-2023 | 1 644 | 6 919 | 101 395 | 1 557 | 6 424 | **59 246** (≈ 59 253 an. 2023) | 224 |

⚠ **Piège de concordance à signaler au rédacteur.** La colonne « valeur des dommages estimée » change de
*définition* selon l'édition : pour 2020-2021, LF2023/LF2024 portent **19 950** (valeur réelle calculée
sur rapports d'expertise, note **), tandis que LF2025 porte **33 250** (dommage maximal potentiel = 60 %
du capital assuré). **Ne pas chaîner cette colonne en série** : elle mêle deux concepts. La série
**homogène et sûre** est celle des **indemnités effectivement versées** (dernière colonne), stable de
définition d'un bout à l'autre.

**Note de lecture (aléa × montant).** La source n'éclate **pas** les indemnités versées par aléa. Mais
les déclarations de gelée sont nulles ou marginales (0 ; 31 ; 24 ; 0) et leurs dommages estimés très
faibles (ex. 467 kDT en 2020-2021, à comparer à ~19 500 kDT de sécheresse la même campagne) : les
indemnités versées 2019-2023 sont donc **imputables à plus de ~97 % à la sécheresse**. Le pic 2022-2023
(**59 MDT**) correspond à la sécheresse des grandes cultures reconnue **calamité par le décret 2023-527
du 17 juillet 2023** (LF2025 p.44). Cette approximation « ~97 % sécheresse » est **informative et bornée**
(l'écart maximal, si toutes les gelées avaient été indemnisées à plein, resterait < 2-3 % du total) ;
elle serait rendue caduque par une éventuelle table CTAMA éclatant les versements par aléa — non publiée à
ce jour (à demander à la CTAMA ; cf. backlog).

### 2.4 Ventilation **par gouvernorat** (gisement complémentaire, non consolidé)

- **Déclarations sécheresse 2019-2020** (1 027) : Siliana 407, Kef 242, Kasserine 242, Béja 97,
  Zaghouan 28, Jendouba 11 (LF2022 p.61).
- **Déclarations 2020-2021** réparties sur Kef, Siliana, Kasserine, Zaghouan, Béja, Manouba (sécheresse)
  (LF2023 p.65) ; **2022-2023** sur Kef, Siliana, Kasserine, Zaghouan, Béja, Jendouba, Manouba, Ben Arous,
  Nabeul, Kairouan (LF2025 p.46).
- **Souscriptions/contrats et surfaces assurées par gouvernorat** (chaque campagne) : tableaux
  dédiés — LF2023 p.64 (2019-20, 2020-21), LF2024 p.48 (2020-21, 2021-22), LF2025 p.45 (2021-22,
  2022-23). Concentration des surfaces assurées : Kasserine, Siliana, Kef (trio dominant).
  Ces tables sont une ventilation géographique **de l'exposition** (souscriptions), pas des indemnités.

### 2.5 Références candidates (CIBLE 2)

Les quatre éditions mobilisées ont **déjà** des entrées CSL candidates proposées dans
`docs/notes/agriculture-calamites-ressources-documentation.md` § 3 (`tn-minfin-fonds-speciaux-2022`,
`-2023`, `-2024`, `-2025`) et `tn-minfin-fonds-speciaux-2020` existe déjà. **Aucune entrée nouvelle** :
le dépouillement de ventilation réutilise exactement ces quatre rapports. Enrichissement de `note`
suggéré pour `-2024` et `-2025` : « sections d'activité CTAMA : déclarations par aléa (sécheresse/gelée)
et par gouvernorat, indemnités versées par campagne ».

### 2.6 Notions à glossaire (pressenties ; vérification par le bibliographe)

- **Fonds d'indemnisation des dommages agricoles dus aux calamités naturelles** (صندوق تعويض الأضرار
  الفلاحية الناجمة عن الجوائح الطبيعية) — source canon. : loi 2017-66 art. 17 ; décrets 2018-821 et
  2018-822. *(déjà pressenti par les notes calamités antérieures ; signalé pour cohérence, pas à créer si
  présent.)*
- **Aléa / jaïha طبيعية (jawāʾiḥ ṭabīʿiyya)** : distinction sécheresse (جفاف) / gelée (جليدة) /
  inondation (فيضان) — utile pour lire la ventilation.
- **CTAMA (مؤسسة «كتاما»)** : gestionnaire délégué du fonds (convention MdF/CTAMA du 29 oct. 2019).

---

## Lacunes (à ne pas inventer)

1. **PAP 2023 agriculture** : fascicule introuvable en ligne (gbo.tn, finances.gov.tn, Wayback). La
   valeur 2023 de la mission est connue par ailleurs (§ 1.2) ; les **indicateurs de performance 2023**
   et la **ventilation programme/sous-programme 2023** propres au PAP, eux, restent non sourcés.
2. **Indemnités versées éclatées par aléa** : non publiées ; seules les *déclarations* le sont. Proxy
   « ~97 % sécheresse » établi et borné (§ 2.3), à remplacer par la donnée CTAMA si elle est obtenue.
3. **Campagne 2023-2024 et au-delà** : hors des rapports détenus (le FST du PLF 2026, qui porterait les
   réalisations 2024, n'est pas encore en ligne — cf. fiche r-fst-calamites-2024 déjà ouverte dans la
   note calamités-ressources § 4).
4. **Divergence de la colonne « valeur des dommages estimée » 2020-2021** (19 950 vs 33 250 selon
   l'édition) : non une erreur mais deux concepts ; documentée, à ne pas chaîner.

## Recherches infructueuses (fiches `docs/recherches.yml` proposées)

Aucun fichier `agriculture-recherches-*.yml` n'existe encore pour ce chantier (comme déjà noté). Fiches
proposées (à créer par le propriétaire ; ne transforme pas le silence de Wayback en « n'existe pas ») :

```yaml
- id: r-pap-2023-agriculture
  objet: "PAP (projet annuel de performance) 2023 de la mission Agriculture, ressources hydrauliques et pêche"
  ou:
    - "tunisia-data sources/gbo-recuperation-2026-11-04.csv (dossier agriculture) — absent"
    - "Wayback CDX gbo.tn/sites/default/files urlkey:.*pap.* — PAP agri 2015..2025 présents SAUF 2023"
    - "Wayback CDX finances.gov.tn — seul PAP MAR 2024"
    - "sondage direct gbo.tn 2023-01/ & 2022-12/ (9 motifs d'URL) — HTTP 404"
  requetes:
    - "CDX url=gbo.tn/sites/default/files&matchType=prefix&filter=urlkey:.*pap.*"
    - "CDX url=finances.gov.tn/sites/default/files filter pap|فلاحة 2023"
    - "GET gbo.tn/sites/default/files/{2023-01,2022-12}/PAP*2023*agric*|MAR*|MARHP*"
  passe:
    - date: 2026-11-18
      resultat: aucun
      couverture: "gbo.tn + finances.gov.tn + Wayback (index complet PAP) ; PAP agri 2023 jamais mis en ligne"
      couvert-jusqu-au: 2026-11-18
      sources: [gbo.tn, finances.gov.tn, wayback-cdx]
  note: "Valeur mission 2023 = 1 965 000 kDT connue par Rapport budget État 2023, RAP 2023, PAP 2024. À relancer si gbo.tn republie ses fascicules."

- id: r-fst-calamites-indemnites-par-alea
  objet: "Ventilation des indemnités VERSÉES par aléa (sécheresse vs gelée) du fonds de calamités agricoles"
  ou:
    - "Rapports FST (annexe 10) LF2022..LF2025 — donnent déclarations par aléa, PAS indemnités par aléa"
    - "CTAMA (gestionnaire délégué) — demande directe à envisager"
  requetes:
    - "lecture sections activité CTAMA, FST LF2022/2023/2024/2025"
  passe:
    - date: 2026-11-18
      resultat: aucun
      couverture: "4 éditions FST dépouillées ; indemnités données par campagne, non par aléa"
      couvert-jusqu-au: 2026-11-18
      sources: [tunisia-data/gbo]
  note: "Proxy ~97 % sécheresse établi et borné (<2-3 % d'écart). Cible de remplacement : table CTAMA des versements par aléa, si obtenue."
```

## Backlog (à verser aux destinations durables par le propriétaire — `docs/backlog-routage.md`)

- **Chapitre 7 (`_calamites.qmd`)** : intégrer la **ventilation datée par aléa des déclarations**
  (table § 2.2) et la **série des indemnités versées par campagne** (table § 2.3), en nommant
  l'approximation « ~97 % sécheresse » comme telle et en renvoyant au décret 2023-527 pour le pic 2023.
- **Note de concordance** : consigner le double sens de la colonne « valeur des dommages estimée »
  (réelle vs maximale potentielle) pour 2020-2021 — ne pas la chaîner.
- **Prolonger la ventilation à 2023-2024** dès parution du FST du PLF 2026 (lié à r-fst-calamites-2024).
- **Chapitre 3 (budget)** : acter que le **PAP 2023 agriculture n'existe pas en ligne** ; citer la
  valeur 2023 (1 965 MDT) depuis le *Rapport budget de l'État 2023* / RAP 2023, pas depuis un PAP 2023.
- **tunisia-data** : les sources mobilisées sont déjà cataloguées (`sources/gbo-fonds-speciaux-rapport-urls.csv`,
  `sources/gbo-recuperation-2026-11-04.csv`) ; aucun PDF neuf à indexer (rien téléchargé).

### Trace technique (reproductibilité)
CDX Wayback interrogé le 2026-11-18 (`http://web.archive.org/cdx/search/cdx?url=gbo.tn/sites/default/files&matchType=prefix&filter=urlkey:.*pap.*&collapse=urlkey`) — Internet Archive est passé « Temporarily Offline » en fin de session (requêtes ultérieures renvoyant la page d'erreur HTML) ; les résultats PAP exploités ont été capturés avant la panne. Sondages gbo.tn via `curl` (HTTP 404). Dépouillement FST via `uv run python` + `pdftotext -layout`. Aucun fichier du précis modifié ; aucun fichier écrit hors cette note.
