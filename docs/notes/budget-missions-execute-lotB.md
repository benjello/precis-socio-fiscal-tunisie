# Exécuté budgétaire par mission — lot B (RAP, missions de tutelle EP + MAS)

Collecte : extraction du 2026-11-04 (`tunisia-data`, `data/raw/gbo-recup-2026-11-04/` +
`data/raw/ministeres-tutelle/` pour les doublons indexés + `data/raw/caisses/mas/`).
Livrable jumeau : `budget-missions-execute-lotB.csv` (75 lignes, une par (mission, année de gestion)).
Le lot A n'est pas touché.

## Méthode

- Index de départ : `sources/gbo-recuperation-2026-11-04.csv` filtré `type=RAP` sur les 11 missions
  du lot (100 lignes, dont 21 « doublon_local » pointant vers `data/raw/ministeres-tutelle/…`,
  suivis et utilisés quand ils comblent un trou ou offrent l'édition la plus récente). Ajout des
  RAP MAS 2018/2022/2023 (`caisses/mas/`). 104 PDF convertis par `pdftotext -layout` (un seul
  introuvable : la copie `_tous/2021-03_RAP_2017_energies_mines.pdf`, identique au fichier du
  dossier mission).
- **L'année de gestion et la mission réelles sont prises à la page de titre**, jamais au nom de
  fichier : plusieurs fichiers sont mal classés ou mal datés (voir « anomalies »).
- Repérage de la section « تنفيذ ميزانية المهمة » / « Exécution du budget de la mission » par
  balayage normalisé (NFKC, suppression des diacritiques/tatweel), puis lecture de la page ;
  chaque total retenu a été re-localisé par recherche du nombre dans la page citée (`page_pdf` =
  page physique du PDF, pas la page imprimée).
- Totaux retenus : ligne **المجموع (العام)** du tableau mission (tableau 1 « par nature », sinon
  tableau 2 « par programmes »), اعتمادات التعهد (engagé) et اعتمادات الدفع (payé), convertis en
  **milliers de dinars** quand le tableau est en dinars (commerce 2017-2019, environnement 2023,
  transport 2023, MAS 2018).

## Structures rencontrées

1. **2016-2019 (ancienne nomenclature)** : exécution en crédits de paiement seuls (تصرف/تنمية/
   صناديق الخزينة) ; `engage_milliers` vide pour ces années.
2. **2020-2023 (GBO/LOLF 2019)** : tableau par nature puis par programmes, التعهد et الدفع,
   « دون اعتبار الموارد الذاتية للمؤسسات » — sauf santé 2017-2018 (totaux **y compris**
   ressources propres, signalés en note).
3. Traductions FR « Expertise France » : utilisées quand l'original AR est illisible à
   l'extraction (polices non-Unicode) ; la version arabe fait foi, noté dans le CSV.

## Contrôles

- **Taux imprimé vs réalisé/prévu** : vérifié par recalcul sur les totaux ; divergences internes
  signalées en note (commerce 2022 : 89.4 imprimé pour 98,4 ; finances 2016 : 81 % vs 83,8 %
  selon le tableau ; agriculture 2020 : tableau 1 imprime un engagé = prévu à 100 %, tableau 2
  donne 94,7 % — retenu le tableau 2, confirmé par la version FR ; équipement 2018 : tableau
  programmes 1 429 055 vs tableau nature 1 440 779 ; santé 2023 et aff. religieuses 2022 :
  micro-écarts entre tableaux 1 et 2).
- **Ordre de grandeur vs `precis/_seriescache/budget-missions-vote.csv` (LF votée, 2021-2023)** :
  cohérent (±20 %) pour l'essentiel. Écarts >25 % , tous expliqués par les LF rectificatives ou
  le périmètre :
  - commerce 2023 : payé 3 934 MD vs LF 2 689 MD (+46 %) — crédits complémentaires de
    compensation ; le RAP compare à un ق.م تعديلي de 3 971 MD (taux 99 %) ;
  - industrie-énergie 2021 : payé 3 464 MD vs LF initiale 679 MD — la compensation hydrocarbures
    est entrée par LFR (prévu LFR 3 606 MD) ; 2022 : payé 7 249 MD vs LF 3 180 MD, prévu
    rectifié 8 128 MD ;
  - environnement 2023 : payé 302 MD vs LF 415 MD (-27 %) — le total du RAP exclut les comptes
    du Trésor (93 MD exécutés à part) et l'exécution est faible (81 %) ;
  - affaires sociales 2023 : payé 2 530 MD vs LF votée 3 302 MD, alors que le RAP affiche un
    prévu rectifié de 2 605 MD — écart LF/RAP à élucider (transferts re-périmétrés ?), à creuser
    côté rédaction.
- Plausibilité interannuelle : sauts expliqués par les changements de périmètre ministériel
  (environnement : avec affaires locales 2017-2020, mission البيئة seule ensuite ; industrie :
  scission 2017-2019 puis fusion avec énergie-mines dès 2020 — la compensation énergie fait
  passer la mission de ~0,2 à ~7 Md DT).

## Anomalies de classement (index `gbo-recuperation-2026-11-04.csv`)

- `agriculture/…RAP 2020 MAR.pdf`, `RAP 2020 MAR` (FR), `RAP 21 MAR.pdf`, `RAP 2022 MAR.pdf` :
  **Affaires religieuses** (MAR = ministère des Affaires religieuses), pas agriculture. Extraits
  quand même (3 années), marqués « hors périmètre ».
- `finances/2021-03_RAP_2017_MFFES.pdf` et `2021-03_RAP MFFES 2018.pdf` : RAP de la **Femme,
  Famille, Enfance et Seniors**, pas finances. Non extraits (hors périmètre ; signalés pour un
  éventuel lot ultérieur).
- `environnement/2023-06_RAP MIME actualisé216.pdf` (= RAP **2021 industrie-mines-énergie**),
  `RAP MIME 2022-VF0106.pdf` et `2024-06_RAP FR-2022-MIME- 141123.pdf` (= industrie 2022) :
  classés environnement à tort.
- Années d'index erronées : `RAP 23 DOMAINE` (LF2024 → gestion 2023), `rap 23 industrie`
  (LF2024 → 2023), `RAPtransport 20092021` (2021 → gestion 2020), `070` santé
  (`…الصحة1012 12021.pdf`, nommé 2021 → gestion 2020).

## Reports / lacunes

- **RAP introuvables dans le lot** (aucune ligne au CSV) : agriculture **2019** et **2021** ;
  commerce : rien à signaler ; domaines de l'État : complet 2017-2023 ; économie-planification
  **2022 et 2023** (mission créée en 2021, un seul RAP dans le lot) ; équipement **2017** ;
  énergie-mines **2018 et 2019** (la scission 2017-2019 fait que le lot n'a que le volet
  industrie) ; industrie-énergie : engagé **2018** non fiabilisé (colonnes RTL, note au CSV) ;
  transport **2017** ; TIC : complet ; santé : complet ; finances : complet (2016 en bonus).
  → à chercher sur gbo.tn/archives Wayback lors d'une prochaine collecte ; pas de fiche
  `docs/recherches.yml` créée (il s'agit de documents administratifs hors JORT, le registre des
  recherches vise les textes juridiques ; si l'équipe préfère une fiche par RAP manquant, le dire
  et je les rédige).
- Originaux AR illisibles à l'extraction texte (polices non-Unicode), totaux pris sur la
  traduction FR : environnement 2019 et 2020, santé 2019, équipement 2019, transport 2019,
  finances 2020, domaines 2020, TIC 2019-2021 ; un OCR (tesseract ara) permettrait de vérifier
  sur l'arabe qui fait foi.
- MAS 2022 : les **prévisions** du tableau sont corrompues à l'extraction (mapping de glyphes) ;
  réalisés fiabilisés par somme des natures ; à confirmer visuellement sur le PDF.
- MAS 2019-2021 présents dans `caisses/mas/` mais laissés au lot A (consigne du ticket).
- Santé 2017-2018 : totaux y compris ressources propres des établissements — non directement
  comparables aux années suivantes (hors RP) ; le détail « hors RP » n'est pas imprimé dans ces
  RAP, ne pas le reconstruire sans décision de méthode.
