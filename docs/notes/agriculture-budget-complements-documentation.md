# Compléments à l'épine budgétaire de l'agriculture — comblement des lacunes GBO

Rôle : documentaliste. Date : 17 novembre 2026. Objet : combler les lacunes des séries
budgétaires de la mission « Agriculture, ressources hydrauliques et pêche maritime »
signalées par `docs/notes/agriculture-budget-documentation.md` (série A, prévision ;
série C, exécution). Complète cette note-mère sans la remplacer : mêmes périmètre
(ressources de l'État, crédits de paiement, hors ressources propres des établissements),
unité (millier de dinars, kDT) et nomenclature budget-programme.

**Résultat.** Trois documents GBO manquants étaient déjà présents dans l'entrepôt
`tunisia-data` (récupération gbo.tn du 4 novembre 2026, rangés sous
`data/raw/gbo-recup-2026-11-04/agriculture/` — hors de la fiche agriculture et non
dépouillés) : **PAP 2019** (prévision 2019), **RAP 2022** et **RAP 2023** (exécution).
Totaux recoupés à l'image. **PAP 2023 et RAP 2021 restent introuvables** (RAP 2021 :
jamais publié sur gbo.tn — preuve ci-dessous).

---

## 1. Nouveaux points de série

### 1.1 Série A — prévision (PAP), CP, ressources de l'État, kDT

| Année (LF) | Budget mission, CP, ressources État (kDT) | Source | Page / repère | Statut |
|---|---|---|---|---|
| **2019** | **1 418 004** | PAP 2019 (ar) | p. 8 imprimée (pdf p. 12), tableau « تطور ميزانية الوزارة 2018-2019 حسب البرامج والبرامج الفرعية », ligne total, colonne 2019 « دفع » (paiement) ; +1,10 % vs 2018 | **NOUVEAU — comble le trou 2019** |

- **Recoupé à l'image** : la ligne de total porte 1 358 489,8 (2017) · 1 402 596 (2018) ·
  2 179 458 (تعهد/engagement 2019) · 1 418 004 (دفع/paiement 2019) · +1,10 %. La colonne
  2018 (1 402 596) **coïncide** avec le total 2018 de la série B (note-mère § 1.2) et avec
  la colonne 2018 du RAP 2019 — le chaînage est donc contrôlé.
- **Portée pour la rupture de nomenclature (note-mère § 2.1)** : ce PAP 2019 est déjà en
  présentation par programmes (دفع/تعهد, LOB 2019-15) **mais sans la section « opérations
  financières » (~84 MDT) qui n'apparaît qu'à partir du PAP 2020**. Le saut réel ne se situe
  donc pas 2018→2019 (1 402 596 → 1 418 004, **+1,10 %**, quasi continu) mais **2019→2020**
  (1 418 004 → 1 726 890, **+21,8 %**), où se cumulent la nouvelle section et la hausse. La
  rupture signalée par la note-mère est ainsi **datée plus finement** : elle est de 2020, pas
  de 2019.

### 1.2 Série C — exécution (RAP), CP réalisés, ressources de l'État, hors ressources propres, kDT

| Année | CP prévus (kDT) | CP réalisés (kDT) | Taux | Source | Statut |
|---|---|---|---|---|---|
| 2019 | 1 418 930 | 1 482 160,6 | 102,4 % | RAP 2019 (ar) | existant (note-mère) |
| 2020 | 1 760 890 | 1 971 409 | 112,0 % | RAP 2020 (fr) | existant (note-mère) |
| **2021** | — | — | — | *RAP jamais publié* | **LACUNE (voir § 5)** |
| **2022** | **1 820 573** | **1 890 273** | **103,83 %** | RAP 2022 (ar) | **NOUVEAU** |
| **2023** | **1 965 000** | **1 900 867** | **97 %** | RAP 2023 (ar) | **NOUVEAU** |

- **RAP 2022, recoupé à l'image** (pdf p. 10 ≈ p. 7 imprimée) : tableau « جدول عدد 1 :
  تنفيذ ميزانية المهمة لسنة 2022 مقارنة بالتقديرات — التوزيع حسب طبيعة النفقة », unité
  « الوحدة : ألف دينار », ligne **المجموع / اعتمادات الدفع** : تقديرات 2022 (ق.م التكميلي)
  = 1 820 573 ; إنجازات 2022 = 1 890 273 ; نسبة الإنجاز 103,83 %. Note de bas de tableau :
  **« دون اعتبار الموارد الذاتية »** (hors ressources propres). ⚠️ le prévu est ici la
  **LF complémentaire** (ق.م التكميلي), non la LF initiale (1 850 000 en PAP 2022,
  note-mère § 1.1) : c'est le réalisé 1 890 273 qui prolonge la série C.
- **RAP 2023, recoupé à l'image** (pdf p. 7 ≈ p. 4 imprimée) : même tableau pour 2023, ligne
  **المجموع العام / اعتمادات الدفع** : تقديرات 2023 (ق.م) = 1 965 000 ; إنجازات 2023 =
  1 900 867 ; نسبة 97 %. Note : « دون اعتبار الموارد الذاتية ». Le prévu 1 965 000
  **coïncide** avec la prévision 2023 de la série A (note-mère : 1 965 000, lu au PAP 2024) —
  double recoupement du point 2023.

---

## 2. Documents récupérés et indexés dans `tunisia-data`

Déjà présents sous `data/raw/gbo-recup-2026-11-04/agriculture/` (téléchargés direct gbo.tn le
2026-11-04, empreintes au manifeste `data/manifeste/gbo-recup-2026-11-04.csv`). **Copiés** ce
jour dans `data/raw/ministeres-tutelle/agriculture/` (dossier de la fiche agriculture, où tourne
le script) et **ajoutés à l'inventaire** `data/raw/ministeres-tutelle/inventaire-agriculture-tic-sante-finances.tsv` :

| Fichier (ministeres-tutelle/agriculture) | Pages | sha256 | URL d'origine |
|---|---|---|---|
| `2021-04_الفلاحة_PAP_2019_PDF-VF.pdf` | 310 | e4b90c9b4d87119ad37e59e7703de93fbe47a457bcaf63880841f73c7c66b256 | gbo.tn/sites/default/files/2021-04/الفلاحة PAP_2019_PDF-VF.pdf |
| `2023-04_RAP_2022_Agriculture.pdf` | 88 | 4b8c0f99fbdc55b9680f9abf71dee2c69328be5a91f24fe19aa6e3ad80ddde0f | gbo.tn/sites/default/files/2023-04/RAP_2022_Agriculture.pdf |
| `2024-07_RAP2023_agriculture.pdf` | 77 | 80883e0bf6300b6d7324bb8ca603e34d21ab45e50f899018968415ed1a3380c3 | gbo.tn/sites/default/files/2024-07/RAP2023 agriculture.pdf |

> **Attention nommage « MAR ».** Dans le dossier de récupération, les fichiers « RAP 2020 MAR »,
> « RAP 21 MAR », « RAP 2022 MAR », « PAP 2020 MAR » sont le **ministère des Affaires
> Religieuses** (vérifié : première page « Ministère des Affaires Religieuses / وزارة الشؤون
> الدينية »), **pas** l'agriculture. « RAP 21 MAR » n'est donc PAS le RAP 2021 agriculture.
> Les documents agricoles portent « agriculture / MARHP / الفلاحة ». Ne pas confondre.

Aucun téléchargement web nouveau n'a été nécessaire (documents déjà dans l'entrepôt).

---

## 3. Où vit le script d'extraction

`~/projets/tunisia-data/scripts/extract_pap_budget_agriculture.py`
(`uv run python scripts/extract_pap_budget_agriculture.py`). Inchangé : il lance
`pdftotext -layout` sur chaque PAP/RAP de `data/raw/ministeres-tutelle/agriculture/` et isole
les lignes de total de mission (fr/ar). Comme les trois fichiers ci-dessus y ont été copiés, le
script les **couvre désormais** et rejoue le relevé (totaux arabes à recouper à l'image — fait
ici pour 2019, 2022, 2023). Catalogué : fiche `sources/ministere-agriculture-tic-sante-finances.md`,
§ 4.

---

## 4. Références CSL candidates (à créer dans le references.json du volume « agriculture »)

```json
[
  {
    "id": "tn-pap-agriculture-2019",
    "type": "report",
    "title": "المشروع السنوي للأداء — وزارة الفلاحة والموارد المائية والصيد البحري — سنة 2019",
    "author": [{"literal": "وزارة الفلاحة والموارد المائية والصيد البحري"}],
    "publisher": "République tunisienne, gestion du budget par objectifs",
    "issued": {"date-parts": [[2018]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-04/%D8%A7%D9%84%D9%81%D9%84%D8%A7%D8%AD%D8%A9%20PAP_2019_PDF-VF.pdf",
    "note": "sha256 e4b90c9b4d87119ad37e59e7703de93fbe47a457bcaf63880841f73c7c66b256 ; tunisia-data data/raw/ministeres-tutelle/agriculture/ ; total mission CP ressources État 2019 = 1 418 004 kDT (p. 8, recoupé à l'image)"
  },
  {
    "id": "tn-rap-agriculture-2022",
    "type": "report",
    "title": "التقرير السنوي للأداء لمهمة الفلاحة والموارد المائية والصيد البحري — سنة 2022",
    "author": [{"literal": "وزارة الفلاحة والموارد المائية والصيد البحري"}],
    "issued": {"date-parts": [[2023]]},
    "URL": "http://www.gbo.tn/sites/default/files/2023-04/RAP_2022_Agriculture.pdf",
    "note": "sha256 4b8c0f99fbdc55b9680f9abf71dee2c69328be5a91f24fe19aa6e3ad80ddde0f ; exécution CP 1 890 273 kDT (103,83 %), hors ressources propres, p. 7 recoupée à l'image"
  },
  {
    "id": "tn-rap-agriculture-2023",
    "type": "report",
    "title": "التقرير السنوي للأداء لمهمة الفلاحة والموارد المائية والصيد البحري — سنة 2023",
    "author": [{"literal": "وزارة الفلاحة والموارد المائية والصيد البحري"}],
    "issued": {"date-parts": [[2024]]},
    "URL": "http://www.gbo.tn/sites/default/files/2024-07/RAP2023%20agriculture.pdf",
    "note": "sha256 80883e0bf6300b6d7324bb8ca603e34d21ab45e50f899018968415ed1a3380c3 ; exécution CP 1 900 867 kDT (97 %), hors ressources propres, p. 4 recoupée à l'image"
  }
]
```

---

## 5. Recherches infructueuses

1. **RAP 2021 de la mission Agriculture — introuvable, apparemment jamais publié.**
   - *Preuve* : l'index CDX de l'Internet Archive sur `gbo.tn/sites/default/files/*`
     (interrogé le 2026-11-17, URL canonique `web.archive.org/cdx/search/cdx`) liste des RAP
     agricoles pour **2017, 2018, 2019, 2020, 2022, 2023** — **aucun pour 2021**. Un RAP 2021
     existe pour d'autres missions (Éducation, Finances, Justice, Transport/MEH, MTC, Domaines,
     Commerce, Emploi, Enseignement sup., Présidence du gouvernement), ce qui confirme qu'il
     s'agit bien d'une absence propre à l'agriculture, non d'un trou d'archivage général.
   - *Fausse piste écartée* : `2022-09_RAP 21 MAR.pdf` (dossier agriculture de la récupération)
     est le **RAP 2021 des Affaires Religieuses** (« MAR »), pas l'agriculture.
   - *Pistes restantes* : demande directe à l'Unité GBO (`gbo.tn`) ou à la DGRE du ministère de
     l'Agriculture ; surveiller une mise en ligne tardive (le RAP 2023 n'a paru qu'en juillet
     2024). Le réalisé 2021 reste donc **un trou honnête** dans la série C, entre 2020
     (1 971 409) et 2022 (1 890 273).
2. **PAP 2023 de la mission Agriculture — document non acquis**, mais sa grandeur utile est
   **triangulée** : prévision mission 2023 = **1 965 000 kDT**, lue au PAP 2024 (série A,
   note-mère) **et** confirmée comme « تقديرات 2023 (ق.م) » dans le RAP 2023 (§ 1.2). Le point
   de prévision 2023 est donc couvert ; seul le PDF du PAP 2023 manque. Au CDX, les PAP 2023
   d'autres missions existent (justice, finances, santé, etc.) mais aucun fichier nommé
   « PAP 2023 agriculture » n'y figure.

---

## 6. Backlog (à verser aux destinations durables par l'archiviste)

- **Série A (prévision)** : point 2019 acquis (1 418 004) → le tableau du chapitre peut passer de
  2020-2025 à **2019-2025** (7 points), sous réserve de l'avertissement de périmètre § 1.1
  (section « opérations financières » absente en 2019 : rupture reportée à 2020).
- **Série C (exécution)** : points 2022 (1 890 273) et 2023 (1 900 867) acquis → la série
  d'exécution passe de deux points (2019-2020) à **2019, 2020, [2021 trou], 2022, 2023**.
- **Lacune ferme — RAP 2021 agriculture** : jamais publié (preuve CDX). À tenter par demande à
  l'émetteur ; sinon trou assumé dans la série C.
- **Lacune douce — PDF du PAP 2023** : non acquis, mais grandeur triangulée (1 965 000). Récupérer
  le document si mis en ligne, pour vérifier la ventilation par programme.
- **Recoupement à l'image** déjà fait pour PAP 2019, RAP 2022, RAP 2023 (ce travail) ; restent à
  recouper les totaux arabes PAP 2024/2025 et RAP 2019 (hérité de la note-mère § 7).
