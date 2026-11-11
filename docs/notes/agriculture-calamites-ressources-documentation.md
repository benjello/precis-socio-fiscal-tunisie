# Note documentaire — chapitre 7 : les RESSOURCES / DOTATIONS du fonds de calamités agricoles

Rôle : documentaliste. Date : 10 novembre 2026. Objet : constituer la **série datée des ressources
et de la dotation d'État** du *fonds d'indemnisation des dommages agricoles dus aux calamités
naturelles* (ex-« fonds de mutualité », loi 86-106 / LF 1987 ; refonte loi 2017-66 / LF 2018), sur
**source primaire**. Complète `docs/notes/agriculture-calamites-documentation.md` (§ 2, « ressources
du fonds : partiellement sourcé, série primaire non encore constituée »).

**Verdict : série TROUVÉE et homogène, 2018-2023, sur document budgétaire primaire.** La « subvention
d'État de ~30 MD/an » jusqu'ici connue par la seule presse est **confirmée** : la dotation annuelle de
l'État rétrocédée au fonds vaut **30 000 mille dinars (30 MD) chaque année de 2019 à 2023**.

---

## 1. La série des ressources — TROUVÉE (primaire, homogène)

### 1.1 Source et famille

Source primaire : **ministère des Finances / GBO, *Rapport sur l'activité des Fonds Spéciaux***, annexe
au projet de loi de finances (annexe n° 10). Chaque édition annuelle donne, pour **chaque** fonds
spécial du Trésor, un **« état du compte »** (ar. كشف الحساب) sur les **trois dernières années de
réalisation** : total des ressources, dotation annuelle de l'État, cotisation des déclarants, taxe de
solidarité, produits des placements, reliquats, interventions (indemnités + expertises), souscriptions.
La **source citée dans le rapport** est la **Trésorerie Générale de la République tunisienne (TGRT)**
et, pour les données d'activité, la **CTAMA** (مؤسسة «كتاما»). **Famille : budgétaire / ministère des
Finances** (réalisations d'exécution des comptes spéciaux du Trésor).

Éditions dépouillées (toutes rangées dans `tunisia-data`) :

| Édition (PLF) | Langue | Années de réalisation | Fichier dans `tunisia-data` (data/raw, hors git) |
|---|---|---|---|
| LF 2020 | **FR** | 2018 (+ prév. 2019) | `gbo/Annexe_10_LF2020-Fonds_Speciaux.pdf` (déjà catalogué) |
| LF 2022 | AR | 2018-2020 | `gbo-recup-2026-11-04/annexes-lf/2022-02_ANNEXE_10_0.pdf` |
| LF 2023 | AR | 2019-2021 | `gbo-recup-2026-11-04/annexes-lf/2023-01_8.pdf` |
| LF 2024 | AR | 2020-2022 | `gbo-recup-2026-11-04/annexes-lf/التقرير حول نشاط الصناديق الخاصة ملحق عدد _10.pdf` |
| LF 2025 | AR | 2021-2023 | `gbo/FST_LF2025_Annexe10_ar.pdf` (**récupéré ce jour**, catalogué) |

Les éditions se **recouvrent** (chaque millésime reprend les 3 années précédentes) : les valeurs d'une
même année sont **cross-confirmées** par 2 à 3 éditions, sans aucune épissure de périmètre. Série
homogène de bout en bout (même source TGRT, même unité « mille dinars », même concept de fonds).

### 1.2 La série (unité : **mille dinars** — « أد » = ألف دينار)

| Année (réalisation) | **Total ressources** | **Dotation annuelle État** | Cotisation déclarants | Taxe solidarité (via Office des céréales) | Produits placements | Reliquats années ant. | **Total interventions** | dont indemnités versées | dont expertises | Souscriptions (fin de campagne) |
|---|---|---|---|---|---|---|---|---|---|---|
| **2018** | 518 ¹ (523 ²) | **0** ³ | 0 | 518 / 523 | 0 | 0 | 0 | 0 | 0 | 0 |
| **2019** | 43 923 | **30 000** | 33 | 13 367 | 0 | 523 | 0 | 0 | 0 | 46 |
| **2020** | 88 241 | **30 000** | 1 326 | 12 880 | 112 | 43 923 | 20 433 | 20 325 | 108 | 1 415 |
| **2021** | 113 399 | **30 000** | 1 271 | 14 210 | 110 | 67 808 | 20 105 | 19 992 ⁴ | 113 | 1 840 |
| **2022** | 140 056 | **30 000** | 2 363 | 14 056 | 343 | 93 294 | 28 569 | 28 400 | 169 | 2 750 |
| **2023** | 156 883 | **30 000** | 2 925 | 12 471 | 0 | 111 487 | 59 477 | 59 253 | 224 | 2 348 |

¹ LF 2020 (FR), p. 66 : « ressources … 518 mille dinars en 2018, mais ce fonds n'a pas encore démarré ».
² LF 2022 et LF 2023 (AR) : total ressources 2018 = **523** mille D (légère révision ; les 523/518 sont
intégralement la part « taxe de solidarité » collectée par l'Office des céréales, le fonds n'ayant alors
ni dotation ni cotisation). Écart 5 mille D, négligeable, à signaler.
³ Dotation d'État **nulle en 2018** : le fonds n'a démarré son activité que le **28 octobre 2019**
(premier contrat d'assurance le 13 novembre 2019 ; LF 2022, p. 59).
⁴ 2021 : 19 992 mille D « dont 67 mille D au titre de 4 contrats de la campagne 2019-2020 et 19 925 mille
D pour 1 673 contrats de la campagne 2020-2021 » (note (*) des éditions LF 2023/2024/2025).

**Lecture d'ensemble.** La **dotation budgétaire de l'État** est **stable à 30 MD/an** de 2019 à 2023
(les rapports le disent explicitement : « إستقرار املبالغ املحالة إلى الصندوق من ميزانية الدولة », stabilité
des montants transférés du budget de l'État). La croissance du **total des ressources** (de 44 à 157 MD
en 4 ans) ne vient donc **pas** d'une hausse de la dotation mais de l'**accumulation des reliquats
non dépensés** (le fonds encaisse plus qu'il n'indemnise) et de la **taxe de solidarité** (~12-14 MD/an,
collectée par l'OC sur pêche, fruits, légumes, olives, céréales). Les **indemnités versées** restent
modestes jusqu'en 2022 (~20-28 MD) puis bondissent en **2023 à 59 MD** (sécheresse grandes cultures,
calamité reconnue par le décret 2023-527 du 17 juillet 2023).

### 1.3 Prévisions des lois de finances (famille : prévision, à ne pas mêler aux réalisations)

- LF 2019 actualisée : ressources prévues **42 518** mille D (LF 2020, p. 67).
- LF 2023 (prévision pour 2023) : ressources **144 294** mille D dont dotation **30 000** ; crédits
  nouveaux **35 000** (LF 2023, lignes 155 et 3669/3942).
- Ces chiffres sont des **prévisions**, à garder distincts de la colonne « réalisations » ci-dessus.

### 1.4 Barème de la contribution (décret 2018-822, lu via le rapport FR LF 2020, p. 42)

- **Cotisation des déclarants = 2,5 %** de la valeur du produit ou des coûts de production.
- **Taxe de solidarité = 1 %** sur les produits de pêche, légumes, fruits, olives et céréales
  collectés par l'**Office des céréales**.
- Dotations annuelles inscrites à la **LF au budget du ministère de l'agriculture et de la pêche**.
- Indemnité plafonnée à **60 %** de la valeur du produit / des dépenses de production ; seuil de
  dommage **≥ 25 %** ; valeur du produit = moyenne de production des 3 dernières années de la délégation.

## 2. Nature budgétaire exacte du fonds — ÉTABLIE

- **C'est un *fonds spécial du Trésor*** (صندوق خاص de la Trésorerie), figurant dans le *Rapport sur
  l'activité des Fonds Spéciaux* aux côtés du Fonds national de garantie, du Fonds de garantie des
  assurés, etc. Les flux (ressources et dépenses) **transitent par la Trésorerie Générale de la
  République tunisienne**, qui en est la source statistique.
- **Gestion opérationnelle déléguée par convention à la CTAMA** (مؤسسة «كتاما»), par un **accord
  Ministre des Finances ↔ CTAMA du 29 octobre 2019** (LF 2024, p. 45 ; LF 2020, p. 42 : « sa gestion
  est confiée à une compagnie d'assurance en vertu d'un accord conclu entre le Ministre des Finances
  et cette société »). La CTAMA encaisse les cotisations, place la trésorerie (placements rémunérés à
  6,8-11,8 % en 2019-2020, déposés à la TGRT) et verse les indemnités.
- **Ordonnateur : le ministre de l'agriculture, des ressources hydrauliques et de la pêche** (اآلمر
  بالصرف ; LF 2024, p. 45).
- **Nuance importante vs le chapitre rédigé.** Le `_calamites.qmd` (§ mise en place) écrit, d'après le
  texte de 1986, « une subvention de l'État égale à **30 %** du total des contributions ». Ce régime
  est celui du **fonds de mutualité d'origine (1986-2017)**. Après la **refonte LF 2018**, la part
  étatique n'est plus un pourcentage des contributions mais une **dotation annuelle fixe votée en loi
  de finances** (de fait 30 MD/an depuis 2019). À distinguer nettement dans le texte : « 30 % des
  contributions » (1986) ≠ « 30 MD de dotation » (post-2018) — la coïncidence du nombre 30 est fortuite.

## 3. Références candidates (CSL-JSON, à verser par le bibliographe)

`tn-minfin-fonds-speciaux-2020` existe déjà dans `precis/fr/agriculture/references.json` (édition
LF 2020). À **créer** pour les éditions mobilisées ici :

```json
[
  {"id":"tn-minfin-fonds-speciaux-2022","type":"report","title":"Rapport sur l'activité des fonds spéciaux — annexe 10 au projet de loi de finances 2022 (ar.)","author":[{"literal":"Ministère des Finances"}],"publisher":"République tunisienne, gestion du budget par objectifs","issued":{"date-parts":[[2021]]},"URL":"https://www.finances.gov.tn/sites/default/files/2022-02/ANNEXE_10_0.pdf","note":"Réalisations 2018-2020. Fonds de calamités agricoles : état du compte (كشف الحساب) pp. 59-60 ; dotation d'État 0 (2018) puis 30 000 mille D (2019, 2020) ; démarrage du fonds le 28 oct. 2019. Source citée : Trésorerie Générale de la République tunisienne et CTAMA. Copie tunisia-data data/raw/gbo-recup-2026-11-04/annexes-lf/2022-02_ANNEXE_10_0.pdf (SHA-256 b8005bc5cfb74c2feb8598976022bfe4f1ba27896117d3c46cd1d0d3849a10d5). Consulté le 10 novembre 2026."},
  {"id":"tn-minfin-fonds-speciaux-2023","type":"report","title":"Rapport sur l'activité des fonds spéciaux — annexe 10 au projet de loi de finances 2023 (ar.)","author":[{"literal":"Ministère des Finances"}],"publisher":"République tunisienne, gestion du budget par objectifs","issued":{"date-parts":[[2022]]},"URL":"https://www.finances.gov.tn/","note":"Réalisations 2019-2021. État du compte du fonds de calamités agricoles pp. 61-62 ; dotation d'État 30 000 mille D/an. Copie tunisia-data data/raw/gbo-recup-2026-11-04/annexes-lf/2023-01_8.pdf. Consulté le 10 novembre 2026."},
  {"id":"tn-minfin-fonds-speciaux-2024","type":"report","title":"Rapport sur l'activité des fonds spéciaux — annexe 10 au projet de loi de finances 2024 (ar.)","author":[{"literal":"Ministère des Finances"}],"publisher":"République tunisienne, gestion du budget par objectifs","issued":{"date-parts":[[2023]]},"URL":"https://www.finances.gov.tn/sites/default/files/2024-01/%D8%A7%D9%84%D8%AA%D9%82%D8%B1%D9%8A%D8%B1%20%D8%AD%D9%88%D9%84%20%D9%86%D8%B4%D8%A7%D8%B7%20%D8%A7%D9%84%D8%B5%D9%86%D8%A7%D8%AF%D9%8A%D9%82%20%D8%A7%D9%84%D8%AE%D8%A7%D8%B5%D8%A9%20%D9%85%D9%84%D8%AD%D9%82%20%D8%B9%D8%AF%D8%AF%20_10.pdf","note":"Réalisations 2020-2022. État du compte du fonds pp. 45-47 ; cadre juridique (loi 2017-66 art. 17, décrets 2018-821 et 2018-822, convention MdF/CTAMA du 29 oct. 2019). Copie tunisia-data data/raw/gbo-recup-2026-11-04/annexes-lf/. Consulté le 10 novembre 2026."},
  {"id":"tn-minfin-fonds-speciaux-2025","type":"report","title":"Rapport sur l'activité des fonds spéciaux — annexe 10 au projet de loi de finances 2025 (ar.)","author":[{"literal":"Ministère des Finances"}],"publisher":"République tunisienne, gestion du budget par objectifs","issued":{"date-parts":[[2024]]},"URL":"http://www.gbo.tn/sites/default/files/2025-03/%D9%85%D9%84%D8%AD%D9%82%2010%20%D8%A7%D9%84%D8%B5%D9%86%D8%A7%D8%AF%D9%8A%D9%82%20%D8%A7%D9%84%D8%AE%D8%A7%D8%B5%D8%A9.pdf","note":"Réalisations 2021-2023. État du compte du fonds pp. 43-44 ; dotation d'État 30 000 mille D/an ; indemnités versées 59 253 mille D en 2023 (sécheresse grandes cultures, décret 2023-527). Copie tunisia-data data/raw/gbo/FST_LF2025_Annexe10_ar.pdf (SHA-256 9c5192ee3dd4a1a1ca328d1f92e88f7f574e754b78fdd8c19e8b00e8c94616ab). Consulté le 10 novembre 2026."}
]
```

Note bibliographe : la table du précis citera de préférence **l'édition la plus récente couvrant
chaque année** (LF 2025 pour 2021-2023, LF 2022 pour 2018-2019), toutes convergentes.

## 4. Recherches infructueuses (consignées)

- **Réalisations 2024 du fonds** (dotation, ressources, indemnités) — attendues dans le *Rapport sur
  l'activité des Fonds Spéciaux* annexé au **PLF 2026**. Sources interrogées le 2026-11-10 :
  page `gbo.tn/fr/Loi-de-Finance-et-rapports-annexes` (ne liste que jusqu'à l'édition LF 2025, dossier
  `2025-03/`) ; `finances.gov.tn` taxonomy « قانون المالية » (term/80) et page `document/qanwn-almalyt-lsnt-2026`
  (aucun lien PDF vers l'annexe 10) ; essai d'URL par analogie `gbo.tn/sites/default/files/{2025-12,2026-01}/ملحق 10 الصناديق الخاصة.pdf` → **404** ; Wayback CDX API **temporairement hors ligne** ce jour.
  **Résultat : édition FST du PLF 2026 non trouvée** (probablement pas encore mise en ligne au format annexe
  séparée ; le fichier `2026-01_115725_LF2026.pdf` déjà détenu est le *projet de loi*, pas le rapport FST).
  Couverture : série des réalisations **arrêtée à 2023**. À relancer quand le PLF 2026 publie son annexe 10.
- **Édition FR des rapports FST postérieurs à LF 2020** : de LF 2022 à LF 2025, le rapport **n'existe
  qu'en arabe** sur gbo.tn / finances.gov.tn (version FR non trouvée). Non bloquant : les chiffres sont
  en caractères latins, lisibles ; mais le libellé des rubriques devra être traduit (fait dans cette note).
- **Indemnités versées par calamité / décret de reconnaissance** : le rapport FST donne le **total annuel**
  d'indemnités (colonne « indemnités versées »), non une ventilation par calamité. La ventilation
  (par aléa, par gouvernorat) existe en partie dans les sections d'activité CTAMA des mêmes rapports
  (ex. LF 2024, pp. 47-49 : 2 039 déclarations pour la campagne 2021-2022, dont 2 015 sécheresse et 24
  gel) — exploitable mais non consolidé en série. Lacune partielle, gisement identifié.

> Fiche `docs/recherches.yml` : à ouvrir (registre `agriculture-recherches-*.yml` non encore créé pour
> ce chantier). Fiche proposée **r-fst-calamites-2024** : objet « réalisations 2024 du fonds de
> calamités agricoles » ; `ou` : gbo.tn annexe 10 PLF 2026, finances.gov.tn term/80, Wayback CDX
> `finances.gov.tn/sites/default/files/2025-12/*` et `2026-*/*` ; passe 2026-11-10, résultat aucun,
> couvert-jusqu-au 2025-03 (dernière édition en ligne = LF 2025).

## 5. Backlog (à verser au backlog durable par le propriétaire)

- **Prolonger la série à 2024** dès parution de l'annexe 10 du PLF 2026 (puis PLF 2027 pour 2025).
- **Corriger / préciser le `_calamites.qmd`** : distinguer « subvention = 30 % des contributions »
  (régime 1986) de la **dotation annuelle fixe de 30 MD** (post-refonte LF 2018), et ajouter la série
  des ressources 2018-2023 (table ci-dessus) au § `sec-agri-calamites-donnees` (le TODO documentaliste
  y est aujourd'hui ouvert). La dotation 30 MD/an est désormais **sourcée sur document budgétaire**,
  plus seulement sur la presse.
- **Série des indemnités versées par calamité** : consolider à partir des sections d'activité CTAMA des
  rapports FST (déclarations/indemnités par aléa et par gouvernorat, 2019-2023) + décrets de reconnaissance.
- **Décret 2018-821** (activités concernées / tri des aléas) : cité dans le visa (art. 2) à côté du
  2018-822 ; à récupérer et dépouiller (non encore fait ici).
- **LF 2026, dispositions fiscales** : le PLF 2026 (déjà détenu) modifie « المعلوم لفائدة صندوق تعويض
  الأضرار الفلاحية » (taxe affectée au fonds) — vérifier si le taux de 1 % évolue.

---

### Trace technique (reproductibilité)

Récupéré ce jour : `data/raw/gbo/FST_LF2025_Annexe10_ar.pdf` (gbo.tn, 2025-03, 132 p., SHA-256
`9c5192ee…616ab`), catalogué dans `tunisia-data/sources/gbo-fonds-speciaux-rapport-urls.csv`.
Playbook `tunisia-data/sources/chercher-des-donnees-tunisie.md` : ajout d'une ligne « Comptes/fonds
spéciaux du Trésor » (le *Rapport sur l'activité des Fonds Spéciaux* comme source d'un état de compte
annuel par fonds, source TGRT, éditions recouvrantes). Éditions LF 2022/2023/2024 déjà présentes dans
`data/raw/gbo-recup-2026-11-04/annexes-lf/`. Lecture : `pdftotext -layout` (chiffres en caractères
latins malgré le texte arabe RTL).
