# Épine budgétaire de l'agriculture — note documentaire (chapitre 3 du volume « L'agriculture »)

Rôle : documentaliste. Date : 10 novembre 2026. Objet : constituer la série budgétaire longue
et homogène de la dépense agricole (budgétaire seul, en entonnoir), dire jusqu'où elle tient et
où sont les trous. **Aucun prix agricole** (céréales, lait, huile) n'entre ici : ils vivent à la
compensation. On ne documente que des **flux budgétaires en dinars** (famille budgétaire /
ministère des Finances).

Sources premières : PAP/RAP de la mission Agriculture (portail GBO, acquis dans `tunisia-data`,
fiche `sources/ministere-agriculture-tic-sante-finances.md`) ; tableaux de crédits des lois de
finances (relevés dans `docs/notes/fiscalite-incitations-second-passage-2026-10-13.md`, § 12) ;
rapport sur les transferts et les garanties annexé aux lois de finances (déjà exploité par le
volume « Entreprises publiques »). Lecture de couche texte sauf mention « relu à l'image ».

---

## 1. Série(s) constituée(s) : bornes datées et sources

### 1.1 Série A — budget de la mission, prévision (loi de finances), nomenclature budget-programme

**Périmètre homogène** : budget de la mission « Agriculture, ressources hydrauliques et pêche
maritime », **ressources de l'État, crédits de paiement, hors ressources propres des
établissements publics** (mention portée sur chaque tableau : « sans tenir compte des ressources
propres des établissements »). Unité : millier de dinars (kDT). Source : PAP (projet annuel de
performance) de l'année, tableau « Répartition du budget de la mission … selon les programmes et
la nature des dépenses ». Nomenclature issue de la **loi organique du budget n° 2019-15 du
13 février 2019** (sept sections de nature économique, approche par programmes).

| Année (LF) | Budget mission, CP, ressources État (kDT) | Source (PAP) | Page / repère |
|---|---|---|---|
| 2020 | 1 726 890 | PAP 2020 (fr) | tableau 02, « Total mission d'État » |
| 2021 | 1 780 000 | PAP 2021 (fr) ; recoupé PAP 2022 | tableau « Répartition du budget de la mission pour 2021 », ligne NB |
| 2022 | 1 850 000 | PAP 2022 (fr) | tableau N°1, ligne Mission, 2022 |
| 2023 | 1 965 000 | PAP 2024 (ar) | tableau « ق م 2023 », colonne (1), اعتمادات الدفع |
| 2024 | 2 202 075 | PAP 2024 (ar) **et** PAP 2025 (ar), concordants | « موارد الدولة », اعتمادات الدفع |
| 2025 | 2 279 050 | PAP 2025 (ar) | « ضبطت اعتمادات مهمة الفلاحة … لسنة 2025 في حدود 2 279 050 م د » |

Projections du cadre de dépenses à moyen terme (non exécutoires, à ne pas chaîner comme des LF) :
2026 ≈ 2 331 000 (PAP 2025) / 2 360 190 (PAP 2024) ; 2027 ≈ 2 440 000 (PAP 2025).

**Homogénéité** : même source (PAP), même périmètre (ressources État, CP, hors ressources
propres), même unité, même nomenclature sur 2020-2025 — **six points continus**. C'est l'épine.
Caveat : chiffres 2023-2025 lus sur la couche texte arabe ; 2024 est concordant entre deux PAP,
ce qui le fiabilise ; 2023 et 2025 restent à recouper à l'image.

### 1.2 Série B — budget du ministère, prévision, ancienne nomenclature (Titre I + Titre II)

Les PAP « pilotes » 2015-2018 donnent le budget du ministère dans l'**ancienne nomenclature**
(نفقات التصرف = dépenses de gestion / Titre I ; نفقات التنمية = dépenses de développement /
Titre II, sur budget et sur prêts extérieurs). Unité kDT. **Lu sur couche texte — à recouper à
l'image avant tout usage publié.**

| Année | Total ministère (kDT) | Source | Repère |
|---|---|---|---|
| 2014 | 967 456 | PAP 2015 | المجموع, colonne 2014 |
| 2015 | 1 135 410 | PAP 2015 | المجموع, colonne 2015 |
| 2016 | ~1 243 178 | PAP 2017 | colonne 2016 |
| 2017 | ~1 300 761 (= 541 630 gestion + 759 131 développement) | PAP 2017 | totaux نفقات التصرف + نفقات التنمية |
| 2018 | 1 402 596 | PAP 2018 | المجموع, colonne 2018 |

**Cette série ne se chaîne PAS avec la série A** (voir § 2). Elle est du même émetteur (ministère
des Finances / budget), mais d'un autre périmètre de nomenclature.

### 1.3 Série C — exécution (RAP), crédits de paiement réalisés

Famille distincte des PAP (réalisation ≠ prévision) : **ne pas mêler aux séries A/B**.

| Année | CP prévus (kDT) | CP réalisés (kDT) | Taux | Source |
|---|---|---|---|---|
| 2019 | 1 418 930 | 1 482 160,6 | 102,4 % | RAP 2019 (ar), « المجموع العام للبرامج » |
| 2020 | 1 760 890 | 1 971 409 | 112,0 % | RAP 2020 (fr), exécution du budget de la mission |

Deux points seulement (RAP 2019 et 2020 acquis) ; RAP 2021 et suivants non acquis (lacune).

### 1.4 Transferts aux offices — localisation (ne pas recopier)

La dépense de transfert de l'État aux offices vit **au volume « Entreprises publiques »**,
`precis/fr/entreprises_publiques/_transferts.qmd` : figure `fig-ep-transferts` et tables
`tbl-ep-transferts-reste`, `tbl-ep-transferts-compensation`. Source : **rapport sur les
transferts et les garanties** annexé aux lois de finances. Y figurent l'Office des céréales (de
1,7 à 3,2 Md DT, 2021-2022) et l'Office national de l'huile, **comptés au titre du ministère du
Commerce** (≈ 3,5 Md DT en 2023) — c'est-à-dire pour l'essentiel de la **compensation de prix**,
hors du périmètre de ce chapitre. Le chapitre 3 renvoie à cette figure ; il ne la refait pas. À
l'inverse, les subventions d'exploitation et d'investissement à l'OTD, à l'APIP (pêche) et aux
régies (matériel de terrassement, sondages hydrauliques) sont **à l'intérieur** du budget de la
mission (dépenses de rémunération et d'intervention des programmes), donc déjà dans les séries
A/B — à ne pas additionner une seconde fois.

---

## 2. Trous et ruptures de périmètre

1. **Rupture de nomenclature à 2019** (entre série B et série A). L'ancienne nomenclature
   (Titre I gestion / Titre II développement) laisse place, avec la LOB n° 2019-15, à sept
   sections de nature économique, dont une **section « opérations financières » (~84-85 MDT)**
   absente de l'ancienne présentation. Le saut 1 402 596 (2018, ancienne) → 1 726 890 (2020,
   nouvelle) mêle donc effet de périmètre et évolution réelle : **les séries A et B ne se chaînent
   pas en silence**. Il faut deux segments, la rupture signalée.
2. **Trou 2019 en prévision** : pas de PAP 2019 acquis (lacune connue) ; seul le RAP 2019
   (exécution, 1 482 160,6 kDT) couvre l'année, dans la nomenclature programme. La prévision
   LF 2019 n'est pas relevée.
3. **Trou en exécution** : RAP 2022 et suivants non acquis ; l'exécution ne tient que pour 2019
   et 2020. Prévision (PAP) et exécution (RAP) ne se recouvrent que ces deux années.
4. **Avant 2014 : trou complet.** Aucune série du budget du ministère de l'Agriculture avant
   2014 n'est constituée. À chercher dans les **lois de finances (dépenses par département /
   budget par ministère)** et les **lois de règlement** — non dépouillées (fiche de recherche
   `r-agri-budget-ministere-avant-2014`, § 5). Les lois de règlement lues pour d'autres besoins
   (gestions 1984, 1990-1995, 2007) règlent le budget par titre et section, les fonds spéciaux en
   une seule ligne : le budget du seul ministère de l'Agriculture n'en ressort pas directement.
5. **Prévision vs révision** : pour une même année passée, les PAP successifs donnent des
   montants différents (ex. 2023 : 1 965 000 en PAP 2024 contre 1 897 322 en PAP 2025 ;
   2022 : 1 850 000 en PAP 2022 contre 1 936 693 en PAP 2024), selon qu'il s'agit de la LF
   initiale, d'une LF complémentaire ou d'une réalisation. **Règle retenue pour l'homogénéité** :
   prendre, pour chaque année, le montant de la LF initiale lu dans le PAP de cette année-là.
6. **Ressources propres exclues** : les séries A/B donnent les seuls moyens de l'État ; le total
   « toutes ressources » (avec ressources propres des établissements : 67 179 kDT en 2023,
   66 472 en 2024…) existe dans les mêmes tableaux mais n'est pas la série retenue. À ne pas
   mélanger avec la série « ressources État ».

### Les « trois séries » des encouragements à l'agriculture (lois de finances)

Le TODO de `precis/fr/fiscalite/_regimes_incitation.qmd` (l. 754) et la note
`fiscalite-incitations-second-passage-2026-10-13.md` (§ 12) signalent « trois séries qui ne
s'enchaînent pas ». Elles sont relevées dans les **tableaux de crédits de programmes des lois de
finances** (« D » en français, « ث » en arabe), en dinars :

- **Série 1 (2010-2013)** — ligne unique « Encouragement de l'État au secteur de l'agriculture
  et de la pêche » : 119 300 000 ; 120 350 000 ; 138 500 000 ; 142 900 000 (LF 2010 p. 3955 ;
  2011 p. 3524 ; 2012 p. 35 ; 2013 p. 52).
- **Série 2 (2014-2016)** — « … sur l'investissement dans le secteur agricole et de la pêche » :
  70 000 000 ; 70 000 000 ; 79 000 000 (LF 2014 p. 3731 ; 2015 p. 3505 ; 2016 éd. ar
  pp. 3656-3657).
- **Série 3 (2017-2019)** — la même ligne tombe à 2 000 000 et **trois lignes nouvelles**
  apparaissent : production agricole 48 000 000 → 75 500 000 ; pêche et aquaculture 7 000 000 →
  10 400 000 ; hydraulique 24 000 000 → 27 100 000 (LF 2017 p. 3887 ; 2018 pp. 4330-4331 ;
  2019 éd. ar p. 5509).

**Pourquoi elles ne s'enchaînent pas** — trois ruptures de périmètre, non des évolutions réelles :
1. **2013 → 2014** : l'intitulé passe de « secteur » (large — périmètre non établi, vraisem­bla­ble­ment
   avec soutien au lait et aux hydrocarbures agricoles) à « investissement » (restreint). Le
   niveau chute de 142,9 à 70 MDT : c'est une redéfinition de l'assiette, pas une coupe.
2. **2016 → 2017** : la ligne unique éclate en quatre (résidu 2 MDT + trois lignes thématiques :
   production, pêche, hydraulique). On ne peut additionner une ligne unique d'avant à un faisceau
   de lignes d'après sans double compte ni omission.
3. **Aucune des trois ne nomme un fonds (FOSDA/FOSDAP) ni une « prime »** : le lien entre la ligne
   budgétaire et l'instrument d'incitation à l'investissement agricole n'est pas établi par le
   libellé ; le périmètre réel de la dépense reste indéterminé. Ces lignes sont donc du budget de
   soutien sectoriel, pas une série de « primes versées ».

Les montants 2010-2019 relevés sont en **dinars courants** ; aucune année de référence pour des
dinars constants. Après 2019, la nomenclature par missions/programmes supprime ces lignes nommées
(LF 2020 : plus de ligne nommée, décret de répartition non ouvert) — les encouragements sont
désormais fondus dans le budget de la mission (série A, activités des programmes 1, 2 et 3).

---

## 3. Où vit le script d'extraction

`~/projets/tunisia-data/scripts/extract_pap_budget_agriculture.py`
(`uv run python scripts/extract_pap_budget_agriculture.py`). Il lance `pdftotext -layout` sur
chaque PAP/RAP de `data/raw/ministeres-tutelle/agriculture/` et isole les lignes de total de
mission (fr et ar). Catalogué : fiche `sources/ministere-agriculture-tic-sante-finances.md`, § 4
(ajout du 2026-11-10). Il sert à rejouer le relevé quand un PAP/RAP manquant est acquis. Les PDF
sont déjà catalogués (inventaire `inventaire-agriculture-tic-sante-finances.tsv`, avec sha256 et
URL) ; aucun PDF nouveau n'a été téléchargé pour cette note.

---

## 4. Références CSL candidates

Déjà dans `tunisia-data` (pas de nouvelle collecte). Entrées à créer dans le references.json du
volume « agriculture » quand il naîtra :

```json
[
  {
    "id": "tn-pap-agriculture-2020",
    "type": "report",
    "title": "Projet annuel de performance de la mission Agriculture, ressources hydrauliques et pêche maritime — année 2020",
    "author": [{"literal": "Ministère de l'Agriculture, des Ressources hydrauliques et de la Pêche"}],
    "publisher": "République tunisienne, gestion du budget par objectifs",
    "issued": {"date-parts": [[2019]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-11/PAP%202020%20AgricultureF.pdf",
    "note": "sha256 ceaa263cefc7f4c0513f976eb6270768b0326b132f29805d87da0686dce4eba8 ; tunisia-data data/raw/ministeres-tutelle/agriculture/"
  },
  {
    "id": "tn-pap-agriculture-2021",
    "type": "report",
    "title": "Projet annuel de performance de la mission Agriculture, ressources hydrauliques et pêche maritime — année 2021",
    "author": [{"literal": "Ministère de l'Agriculture, des Ressources hydrauliques et de la Pêche"}],
    "issued": {"date-parts": [[2020]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-04/PAP-2021%20Agriculture%2Cressources%20hydrauliques%20et%20p%C3%A8che%20maritime.pdf",
    "note": "sha256 d06fef6df6c90ef588a7299f104009bb626ea827bcbf01b47f4a78b641ed4003"
  },
  {
    "id": "tn-pap-agriculture-2022",
    "type": "report",
    "title": "Projet annuel de performance de la mission Agriculture, ressources hydrauliques et pêche maritime — année 2022",
    "author": [{"literal": "Ministère de l'Agriculture, des Ressources hydrauliques et de la Pêche"}],
    "issued": {"date-parts": [[2021]]},
    "URL": "http://www.gbo.tn/sites/default/files/2022-01/PAP%202022%20Agriculture.pdf",
    "note": "sha256 0a1feba0612e5c1d2a98f98669e52134a8df1ef41caf33e842377cea659bf131"
  },
  {
    "id": "tn-pap-agriculture-2024",
    "type": "report",
    "title": "المشروع السنوي للأداء لمهمة الفلاحة والموارد المائية والصيد البحري — سنة 2024",
    "author": [{"literal": "وزارة الفلاحة والموارد المائية والصيد البحري"}],
    "issued": {"date-parts": [[2023]]},
    "URL": "http://www.gbo.tn/sites/default/files/2024-01/AGRICULTURE.pdf",
    "note": "sha256 ca516ed4b12be65cfa414efb584daa6b51168a821748b6759b3470249f87c6d3 ; totaux lus couche texte, à recouper à l'image"
  },
  {
    "id": "tn-pap-agriculture-2025",
    "type": "report",
    "title": "المشروع السنوي للأداء لمهمة الفلاحة والموارد المائية والصيد البحري — سنة 2025",
    "author": [{"literal": "وزارة الفلاحة والموارد المائية والصيد البحري"}],
    "issued": {"date-parts": [[2024]]},
    "URL": "http://www.gbo.tn/sites/default/files/2025-03/PAP%202025agriculture%20version%20nv.pdf",
    "note": "sha256 e59e7ecd77e661381cb8f29ae798f0ae9c7e9446ab8879e04bae25242828d3c0 ; totaux lus couche texte, à recouper à l'image"
  },
  {
    "id": "tn-pap-agriculture-2015",
    "type": "report",
    "title": "Projet annuel de performance — ministère de l'Agriculture, année 2015 (nomenclature Titre I / Titre II)",
    "author": [{"literal": "Ministère de l'Agriculture"}],
    "issued": {"date-parts": [[2014]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-04/PAP%202015%20agriculture.pdf",
    "note": "sha256 d7372a0884eca44ba4f333b744e7b8c1c9ce8c5a5e419f6472c8e87928d0157f ; totaux couche texte à recouper"
  },
  {
    "id": "tn-pap-agriculture-2017",
    "type": "report",
    "title": "Projet annuel de performance — ministère de l'Agriculture, année 2017 (nomenclature Titre I / Titre II)",
    "author": [{"literal": "Ministère de l'Agriculture"}],
    "issued": {"date-parts": [[2016]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-03/PAP%202017%20Agriculture.pdf",
    "note": "sha256 c4341e1f007e9f7c0ee51afcb6148fb22f3da08ac076b104d6bdf116aa7be8f5"
  },
  {
    "id": "tn-pap-agriculture-2018",
    "type": "report",
    "title": "Projet annuel de performance — ministère de l'Agriculture, année 2018 (nomenclature Titre I / Titre II)",
    "author": [{"literal": "Ministère de l'Agriculture"}],
    "issued": {"date-parts": [[2017]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-03/PAP%202018%20Agriculture.pdf",
    "note": "sha256 372656e9eb7322ed7e6cd13c9e549ea6c5745cf165c7574a07d4836d81b41ae7"
  },
  {
    "id": "tn-rap-agriculture-2019",
    "type": "report",
    "title": "Rapport annuel de performance de la mission Agriculture, ressources hydrauliques et pêche maritime — année 2019",
    "author": [{"literal": "Ministère de l'Agriculture, des Ressources hydrauliques et de la Pêche"}],
    "issued": {"date-parts": [[2020]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-03/RAP_2019%20Agriculture.pdf",
    "note": "sha256 98e59939199fa60ae7ab7679a8c72c76e35e81b76762b2a0b6f0b18802634b43 ; exécution 1 482 160,6 kDT (ar, à recouper à l'image)"
  },
  {
    "id": "tn-rap-agriculture-2020",
    "type": "report",
    "title": "Rapport annuel de performance de la mission Agriculture, ressources hydrauliques et pêche maritime — année 2020",
    "author": [{"literal": "Ministère de l'Agriculture, des Ressources hydrauliques et de la Pêche"}],
    "issued": {"date-parts": [[2021]]},
    "URL": "http://www.gbo.tn/sites/default/files/2021-12/RAP2020%20MARHP.pdf",
    "note": "sha256 552b6c5b407355792395996987cbde564a1ebf94761ba13d74dca975d08f3225 ; exécution CP 1 971 409 kDT"
  }
]
```

La **loi organique du budget n° 2019-15 du 13 février 2019** (fondement de la rupture de
nomenclature) est à référencer depuis le JORT ; non récupérée ici (texte de loi, pas un rapport).

---

## 5. Recherches infructueuses (fiches `docs/recherches.yml` proposées)

Aucune fiche agriculture-budget préexistante (`lister` du 2026-11-10, 1467 fiches, aucune sur
budget/FOSDA/office agricole). Deux fiches **à créer** :

```yaml
- id: r-agri-budget-ministere-avant-2014
  objet: budget du ministère de l'Agriculture avant 2014 (dépenses par département des lois de finances ; lois de règlement)
  ou: [docs/notes/agriculture-budget-documentation.md]
  requetes:
    titres_fts: ['"budget" "agriculture"', '"loi de règlement"']
    titres_like: []
    iort_ar: [ميزانية الفلاحة, وزارة الفلاحة, قانون غلق الميزانية]
    plein_texte: []
    depuis: 1956-01-01
  passes:
  - date: 2026-11-10
    role: documentaliste
    sources: [corpus_local]
    couverture: "lois de règlement lues pour d'autres besoins (gestions 1984, 1990-1995, 2007) : budget réglé par titre et section, fonds spéciaux en une ligne ; le budget du seul ministère de l'Agriculture n'en ressort pas. Tableaux 'dépenses par département' des lois de finances annuelles non dépouillés."
    couvert_jusqu_au: 2013-12-31
    resultat: aucun
  a_faire: [dépouiller les tableaux 'dépenses par département/ministère' des lois de finances annuelles 1956-2013 ; récupérer les lois de règlement de gestions non lues]

- id: r-agri-fosda-fonds-special-developpement
  objet: texte fondateur du fonds spécial de développement de l'agriculture (FOSDA) et son rapport au « fonds de développement agricole » supprimé par la LF 1995
  ou: [docs/notes/agriculture-budget-documentation.md]
  requetes:
    titres_fts: ['"développement agricole"', '"fonds spécial"']
    titres_like: []
    iort_ar: [الصندوق الخاص بالتنمية الفلاحية, صندوق التنمية الفلاحية]
    plein_texte: []
    depuis: 1956-01-01
  passes:
  - date: 2026-11-10
    role: documentaliste
    sources: [corpus_local]
    couverture: "le FOSDAP (pêche et aquaculture) est nommé dans le PAP 2022 (programme 2, activité 3) ; le FOSDA (agriculture) n'est pas nommé dans les lignes de crédits 2010-2019 relevées. Texte fondateur non identifié ; lien avec le 'fonds de développement agricole' supprimé en 1995 non établi."
    couvert_jusqu_au: 2026-11-10
    resultat: aucun
  a_faire: [identifier le décret/loi créant le FOSDA ; lire la LF 1995 art. supprimant le « fonds de développement agricole »]
```

---

## 6. VERDICT

**L'épine budgétaire tient — sur une période courte et homogène, avec des trous honnêtes avant.**

- **Série homogène solide 2020-2025** (6 points) : budget de la mission Agriculture, ressources
  de l'État, crédits de paiement, hors ressources propres, nomenclature budget-programme — même
  source, même périmètre, même unité. C'est un socle publiable (sous réserve de recoupement à
  l'image des totaux arabes 2023-2025).
- **Segment antérieur 2014-2018** disponible (PAP pilotes) mais en **ancienne nomenclature** :
  second segment, à ne pas chaîner, rupture 2019 signalée (annexe PIB non concernée ; c'est une
  rupture de nomenclature de dépense, pas de base de PIB — aucun ratio au PIB n'est calculé ici).
- **Avant 2014 : trou assumé**, à combler par dépouillement des lois de finances / règlement
  (fiche `r-agri-budget-ministere-avant-2014`). Une lacune établie, pas une valeur plausible.
- **Les « trois séries » d'encouragements** sont identifiées et leur non-raccordement est
  **expliqué** (redéfinition d'assiette 2014, éclatement en 4 lignes 2017, absence de lien à un
  fonds nommé) : elles illustrent le chapitre comme cas d'école de fausse continuité, sans
  fournir une série chaînable.
- **Transferts aux offices** : localisés au volume EP, pour l'essentiel compensation de prix
  (hors périmètre) ; renvoi, pas de recopie.

Le chapitre 3 tient donc comme **épine budgétaire courte et honnête** : une série continue de six
ans, deux segments antérieurs documentés mais non chaînés, un trou daté avant 2014. Pas de
place-holder, pas d'approximation : aucune n'a été nécessaire ni tentée (les niveaux manquants
avant 2014 ne sont pas « approximés » faute de borne d'erreur contrôlable).

---

## 7. Backlog (notions, données, pistes — à verser aux destinations durables par l'archiviste)

**Notions à glossaire** (ne pas confondre — trois fonds voisins) :
- **FOSDA** — fonds spécial de développement de l'agriculture (texte fondateur à identifier ;
  fiche `r-agri-fosda-fonds-special-developpement`).
- **FOSDAP** — fonds spécial de développement de la pêche et de l'aquaculture (nommé au PAP 2022,
  programme 2, activité 3, budgété avec l'indemnisation des calamités agricoles).
- **FODECAP / fonds de développement de la compétitivité (agriculture et pêche)** — déjà traité
  au volume Fiscalité (`#sec-fst-agriculture`, né en 1995) : renvoi, ne pas redoubler.
- **« Crédits de paiement » / « crédits d'engagement »** et **nomenclature budget-programme** vs
  **Titre I / Titre II** : définir sur la LOB n° 2019-15, pour expliquer la rupture 2019.
- **Ressources propres des établissements** (exclues du périmètre « ressources de l'État »).

**Données / pistes** :
- Acquérir **PAP 2019 et 2023** et **RAP 2021 et suivants** (lacunes GBO connues) — étendrait les
  séries A et C.
- **Recouper à l'image** les totaux arabes PAP 2024/2025 et RAP 2019 (couche texte peu fiable).
- **Dépouiller les tableaux « dépenses par département » des lois de finances 1956-2013** pour le
  budget du ministère avant 2014 (fiche dédiée).
- Établir l'articulation **FOSDA / « fonds de développement agricole » supprimé en 1995** (report
  déjà noté dans `agriculture-plan-livre.md`).
- **Indemnisation des calamités agricoles** : budgétée avec le FOSDAP au PAP 2022 — piste pour le
  chapitre 7 (calamités), à relever dans les activités du programme 2.
- Trancher l'**année de référence pour dinars constants** si une série en volume est voulue (les
  relevés sont en dinars courants).
