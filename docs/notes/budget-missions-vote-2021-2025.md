# Transcription — « توزيع الاعتمادات حسب المهمات والمهمات الخاصة », rapports PLF 2021-2025

Note de chantier (documentaliste, 2026-11-10). Accompagne `budget-missions-vote-2021-2025.csv`
(même répertoire). Objet : le tableau unique « répartition des crédits par missions et missions
spéciales » du **Rapport sur le projet de budget de l'État** annexé à chaque PLF, transcrit pour
les cinq éditions en entrepôt (budgets 2021 à 2025). Feuille de route : point 4 de
`docs/notes/annexe-budget-desagregation.md`.

## 1. Sources (entrepôt `tunisia-data`, `data/raw/`)

| Budget | Fichier | Tableau | Page PDF | Page imprimée |
|---|---|---|---|---|
| 2021 | `gbo-recup-2026-11-04/annexes-lf/2020-10_Rapport LF 2021_0.pdf` (143 p.) | § -10, sans numéro de جدول | 52 | 52 |
| 2022 | `banque-mondiale-rapports/minfin_2021-12_rapport_budget_etat_2022_ar.pdf` (124 p.) | § -5, sans numéro | 42 | 41 |
| 2023 | `gbo-recup-2026-11-04/annexes-lf/2023-01_0002_0.pdf` (151 p.) | § -8, sans numéro | 55 | 54 |
| 2024 | `banque-mondiale-rapports/minfin_2023-10_rapport_budget_etat_2024_ar.pdf` (170 p.) | جدول عدد 19 | 71 | 69 |
| 2025 | `banque-mondiale-rapports/minfin_2025_annexe1_rapport_budget_etat_2025_ar.pdf` (174 p.) | جدول 15 | 72 | 71 |

Extraction `pdftotext -layout` : couche texte arabe propre dans les cinq fichiers, chiffres en
chiffres occidentaux, aucun chiffre arabe oriental rencontré dans ces tableaux. Unité imprimée :
« بحساب 1000 دينار » (milliers de dinars) dans les cinq éditions. Chaque tableau tient sur une
page. L'ordre des colonnes (RTL) a été fixé par l'en-tête ET contrôlé par la ligne de total
(le total de chaque colonne retombe sur une grandeur identifiable de la موازنة du même rapport).

## 2. En-têtes relevés (le point que l'inventaire laissait ouvert)

| Édition | Colonnes, de droite à gauche (ordre de lecture arabe) |
|---|---|
| 2021 | المهمات والمهمات الخاصة \| ق م 2020 \| 2020 محين \| تقديرات 2021 |
| 2022 | المهمات والمهمات الخاصة \| قانون المالية 2021 \| ق م 2021 محين \| تقديرات 2022 |
| 2023 | المهمات والمهمات الخاصة \| ق م 2022 \| ق م ت 2022 \| تقديرات 2023 |
| 2024 | المهمات والمهمات الخاصة \| قانون المالية 2023 \| ق م ت 2023 \| تقديرات 2024 |
| 2025 | المهمات والمهمات الخاصة \| قانون المالية 2024 \| تقديرات 2025 |

**Correction à l'inventaire du 2026-11-10** : le tableau ne distingue PAS crédits d'engagement et
crédits de paiement. Chaque exercice n'a qu'UNE colonne de crédits : le rappel de la LF n−1
(« ق م » / « قانون المالية »), une colonne actualisée (« محين » en 2021-2022 — crédits actualisés
en cours d'exercice ; « ق م ت » en 2023-2024 — loi de finances rectificative n−1 ; absente en
2025) et les prévisions du PLF (« تقديرات »). La colonne `credits_engagement_milliers` du CSV est
donc **vide partout** ; les « تقديرات » sont portées en `credits_paiement_milliers`.

**Interprétation « crédits de paiement » — à confirmer** : le tableau ne porte ni تعهد ni دفع.
Arguments : (a) le total général égale, dans les cinq éditions, la ligne « نفقات الميزانية » du
tableau d'équilibre (« موارد الدولة وتكاليفها ») du même rapport, qui est l'agrégat voté en
paiement (p. ex. 59 828 MD pour 2025) ; (b) la LOB distingue crédits d'engagement et de paiement
(loi organique n° 2019-15, art. 22, clé `loi-org-2019-15-lob`) et seule une lecture « paiement »
boucle avec les dépenses du budget. Contre-épreuve possible : le tableau « C » de la LF au JORT
(qui, lui, distingue تعهد/دفع) — lecture image, non faite ici. TODO évaluateur.

## 3. Totaux de contrôle

### 3.1 Sommes des lignes vs totaux imprimés (الجملة العامة) — exacts, 5/5

| Édition | Colonne | Total imprimé (milliers D) | Somme des lignes | Écart |
|---|---|---|---|---|
| 2021 | ق م 2020 | 39 191 000 | 39 191 000 | 0 |
| 2021 | 2020 محين | 43 700 000 | 43 700 000 | 0 |
| 2021 | تقديرات 2021 | 41 016 000 | 41 016 000 | 0 |
| 2022 | قانون المالية 2021 | 40 203 000 | 40 203 000 | 0 |
| 2022 | ق م 2021 محين | 44 241 000 | 44 241 000 | 0 |
| 2022 | تقديرات 2022 | 47 166 000 | 47 166 000 | 0 |
| 2023 | ق م 2022 | 47 166 000 | 47 166 000 | 0 |
| 2023 | ق م ت 2022 | 50 914 000 | 50 914 000 | 0 |
| 2023 | تقديرات 2023 | 53 921 000 | 53 921 000 | 0 |
| 2024 | قانون المالية 2023 | 53 921 000 | 53 921 000 | 0 |
| 2024 | ق م ت 2023 | 56 071 000 | 56 071 000 | 0 |
| 2024 | تقديرات 2024 | 59 805 000 | 59 805 000 | 0 |
| 2025 | قانون المالية 2024 | 59 805 000 | 59 805 000 | 0 |
| 2025 | تقديرات 2025 | 59 828 000 | 59 828 000 | 0 |

### 3.2 Cohérence interne au rapport

Dans chaque édition, le total « تقديرات n » égale la ligne « نفقات الميزانية » du tableau
d'équilibre du même rapport : 41 016 (2021), 47 166 (2022), 53 921 (2023), 59 805 (2024),
59 828 (2025) MD. Périmètre : dépenses du budget au sens de la LOB (y compris نفقات التمويل et
العمليات المالية), hors remboursement du principal de la dette (تكاليف الخزينة).

### 3.3 Rappels croisés entre éditions : PLF ≠ LF votée pour 2021

Rappel « ق م n−1 » (édition n) vs « تقديرات n−1 » (édition n−1) : écart nul pour 2022→2023,
2023→2024, 2024→2025. **Exception : 2021.** Le PLF 2021 (41 016 000) dépasse de 813 000 milliers
le rappel « قانون المالية 2021 » de l'édition 2022 (40 203 000) ; différences par mission :
Commerce −200 000, Transport −100 000, Dépenses de financement −245 000, Dépenses imprévues
−268 000 (le vote de la loi n° 2020-46 a réduit ces quatre missions). Conséquence de méthode :
**la colonne « تقديرات » est une proposition du PLF, pas nécessairement le voté** ; pour 2022 à
2025, PLF = LF votée au niveau mission (totaux identiques), mais pour tout usage « voté », le
rappel de l'édition n+1 (ou le tableau C de la LF) fait foi.

### 3.4 Contrôle externe vs cache du précis

La série `jort-lf-budget-etat` citée au ticket **n'existe pas** dans `precis/_seriescache/`
(vérifié le 2026-11-10) ; contrôle fait contre `precis/_seriescache/budget-vote-realise.csv`
(lignes `etat=LF`, `total_hors_dette_MDT`, hors نفقات التمويل) :

| Budget | Total missions − نفقات التمويل (MD) | Cache LF `total_hors_dette_MDT` | Écart | % |
|---|---|---|---|---|
| 2021 | 41 016 − 4 275 = 36 741 | 36 313 | +428 | +1,18 % |
| 2022 | 47 166 − 4 326 = 42 840 | 42 806 | +34 | +0,08 % |
| 2023 | 53 921 − 5 307 = 48 614 | 48 814 | −200 | −0,41 % |
| 2024 | 59 805 − 6 838 = 52 967 | 53 167 | −200 | −0,38 % |
| 2025 | 59 828 − 6 487 = 53 341 | 53 541 | −200 | −0,37 % |

Explications probables, à trancher par l'évaluateur de données : (a) 2021, seul écart > 1 % — le
tableau est le PLF et la LF votée a retranché 813 000 milliers (§ 3.3), dont 568 000 hors
financement ; (b) l'écart récurrent de −200 MD (2023-2025) égale exactement la colonne
`prets_MDT` du cache (200 MD de prêts du Trésor) : différence de périmètre probable entre le
total du cache et نفقات الميزانية (les prêts et avances du Trésor sont des charges de trésorerie
dans la LOB, art. 17). Non tranché ici.

## 4. Référentiel mission_ar ↔ mission_fr et classement ordinaire/spéciale

Classement `speciale` d'après l'art. 19 de la loi organique n° 2019-15 (clé
`loi-org-2019-15-lob` ; liste lue dans l'édition arabe Ja0152019.pdf, couche texte, et dans
l'édition française Jo0152019.pdf, p. 397) : ARP, Conseil supérieur de la magistrature, Cour
constitutionnelle, structures juridictionnelles judiciaires, administratives et financières dont
la loi organique prévoit l'autonomie administrative et financière (d'où la **Cour des comptes**),
instances constitutionnelles indépendantes (d'où l'**ISIE**), dépenses de financement, dépenses
imprévues et non réparties. Le **Conseil national des régions et des districts** (2023+) est
classé `speciale` par analogie avec l'ARP — classement non lu dans un texte, à vérifier
(l'art. 19 est antérieur à la constitution de 2022).

Traductions courtes stables (détail complet dans le CSV) : Assemblée des représentants du
peuple ; Conseil national des régions et des districts ; Présidence de la République ; Présidence
du gouvernement ; Intérieur ; Justice ; Affaires étrangères, migration et Tunisiens à l'étranger ;
Défense nationale ; Affaires religieuses ; Finances ; Économie et planification ; Domaines de
l'État et affaires foncières ; Agriculture, ressources hydrauliques et pêche ; Industrie, mines et
énergie ; Commerce et développement des exportations ; Technologies de la communication ;
Tourisme ; Équipement et habitat ; Environnement ; Transport ; Affaires culturelles ; Jeunesse et
sport ; Famille, femme, enfance et seniors ; Santé ; Affaires sociales ; Éducation ; Enseignement
supérieur et recherche scientifique ; Emploi et formation professionnelle ; Conseil supérieur
(provisoire) de la magistrature ; Cour constitutionnelle ; Cour des comptes ; ISIE ; Dépenses de
financement ; Dépenses imprévues et non réparties.

Ruptures de périmètre à retenir pour toute série longue :

- **Affaires locales** : 2021, mission « الشؤون المحلية والبيئة » (Affaires locales et
  environnement, 1 230 000) ; 2022, note (*) du tableau : les crédits des services des affaires
  locales passent à la mission **Intérieur**, le reste devient mission **Environnement**
  (350 000 proposés en 2022, rappel 2021 affiché 1 230 000 sous « البيئة »). L'Intérieur passe de
  3 927 000 (LF 2021) à 5 417 357 (2022) pour l'essentiel par cet apport.
- **2021, intitulés différents** : mission 10 « الاقتصاد والمالية ودعم الاستثمار » éclatée en
  deux lignes sans sous-total (1.10 Finances ; 2.10 Développement, investissement et coopération
  internationale) ; mission 20 « الشباب والرياضة والادماج المهني » idem (1.20 Jeunesse et sport ;
  2.20 Formation professionnelle et emploi). Transcrites en deux lignes chacune, même rang.
  À partir de 2022 : missions séparées Finances / Économie et planification, et Jeunesse et
  sport / Emploi et formation professionnelle.
- **Équipement** : « التجهيز والإسكان والبنية التحتية » (2021) devient « التجهيز والإسكان »
  (2022+) ; « النقل واللوجستيك » (2021) devient « النقل » (2022+) ; « المرأة والأسرة وكبار
  السن » (2021) devient « الأسرة والمرأة والطفولة وكبار السن » (2022+).
- **CSM** : « المجلس الأعلى للقضاء » (2021-2022) devient « المجلس الأعلى المؤقت للقضاء »
  (provisoire) à partir de l'édition 2023.

Nombre de lignes : 31 (2021, dont 2 missions éclatées → 33 lignes CSV), 33 (2022), 34 (2023,
2024, 2025). Soit, en 2023-2025 : 26 missions ordinaires + 8 missions spéciales — et non
« ~34 + 7 » comme l'écrivait l'inventaire : les ~34 lignes INCLUENT les missions spéciales.

## 5. Anomalies et cellules vides (aucune valeur inventée)

- **المجلس الوطني للجهات والأقاليم** : ligne présente mais entièrement vide en 2023 et 2024 ;
  première dotation en 2025 (15 610).
- **المحكمة الدستورية** : rappel 1 624 / rectifié 0 / proposé 0 en 2023 ; ligne entièrement vide
  en 2024 et 2025 (institution non mise en place).
- **ISIE** : à-coups électoraux — 27 778 (LF 2022) → 74 000 (2023, référendum + législatives
  déjà passés, rectifié 19 463) → 192 469 (2024, présidentielle 2024 ?) → 23 000 (2025).
- 2021 : les trois dernières valeurs de la colonne محين (قضاء 8 800, دستورية 6 140, محاسبات
  20 225) sont identiques au rappel ق م 2020 — vraisemblable (pas d'actualisation), lu tel quel.
- Aucune cellule illisible : toutes les cellules vides du CSV correspondent à des cases vides du
  tableau imprimé.

## 6. Famille de chiffres et méthode (conventions § 3)

Famille **budgétaire — ministère des Finances** : crédits proposés au PLF (تقديرات), rappels de
LF et de LF rectificative, en milliers de dinars courants, périmètre نفقات الميزانية (LOB,
art. 15 : rémunérations, gestion, interventions, investissement, opérations financières,
financement, imprévues ; hors remboursement du principal). Document : rapport annexé au PLF
(art. 46 de la LOB), établi par le ministère des Finances à l'automne n−1. Ce sont des crédits
**votés/proposés**, pas des réalisations.

## 7. Reports et lacunes

1. **Rapports 2020 et 2026 absents de l'entrepôt** → collecte à faire (agent data, dépôt
   `tunisia-data`) ; la vue « voté par mission » commence en 2020 (première année en missions).
2. **Clés CSL à créer** : `minfin-rapport-budget-2021` et `minfin-rapport-budget-2023`
   (entrées candidates dans la note documentaire du chantier ; URLs d'origine et SHA-256 au
   catalogue `tunisia-data/sources/gbo-recuperation-2026-11-04.csv`, lignes 274 et 312).
   Existent déjà : `minfin-rapport-budget-2022`, `-2024`, `-2025` (sans URL, à compléter par le
   bibliographe avec les adresses finances.gov.tn si retrouvables).
3. **Sens « paiement » des تقديرات à contre-éprouver** sur le tableau C d'une LF au JORT
   (lecture image) — § 2 ci-dessus.
4. **Série `jort-lf-budget-etat` introuvable** dans `_seriescache/` : le contrôle externe a été
   fait contre `budget-vote-realise.csv` ; écarts résiduels (−200 MD récurrents, +428 en 2021) à
   trancher par l'évaluateur de données (§ 3.4).
5. **Classement du Conseil national des régions et des districts en mission spéciale** : par
   analogie, non sourcé (§ 4) — vérifier si un texte (LOB modifiée ? LF 2025 ?) le classe.
6. **Glossaire** (terminologue) : mission (مهمة), mission spéciale (مهمة خاصة), programme
   (برنامج), crédits d'engagement (اعتمادات التعهد), crédits de paiement (اعتمادات الدفع) —
   source canonique pressentie : loi organique n° 2019-15, art. 18, 19 et 22
   (`loi-org-2019-15-lob`).
7. Aucune fiche `docs/recherches.yml` ouverte : aucun texte attendu au JORT n'a été cherché en
   vain dans ce chantier (les manques sont des collectes de rapports, routées au point 1).
