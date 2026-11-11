# Documentation — chapitre 5 « Les encouragements à l'investissement agricole » (versant versements)

Rôle : documentaliste. Date : 10 novembre 2026. Livre : « L'agriculture — le soutien au
producteur » (option c retenue le 10/11/2026). Périmètre : ce que la fiscalité ne documente pas —
textes antérieurs à 1993, articulation des fonds, primes **effectivement versées** par l'APIA, APIA
comme guichet. Le versant fiscal (code de 1993, loi de 2016, barème des primes du régime) est déjà
écrit dans le livre de la fiscalité (`precis/fr/fiscalite/_regimes_incitation.qmd`) : non repris ici.

Sources : d'abord `jort_cache.db` (corpus `PDFs-legislation-tunisie`, 78 953 textes, dernière
publication indexée ≈ avril 2026) ; catalogue `tunisia-data/sources/` ; portail open data
`agridata.tn` (APIA) ; vérifications web (AfDB, guide entrepreneur). Les fascicules JORT cités sont
dans le corpus local **en image, sans couche texte** : les dates et la structure viennent des
notices de `jort_cache` ; la transcription des articles demande un OCR (signalé à chaque fois).

---

## 1. Établi et lu (textes datés)

La chaîne du soutien à l'investissement agricole remonte bien avant 1993. Six jalons sont **datés
et situés** par leurs notices de `jort_cache` ; leur **contenu d'articles** reste à transcrire par
OCR (fascicules en image).

| Texte | Objet (intitulé de la notice) | JORT | Statut de lecture |
|---|---|---|---|
| **Loi n° 63-17 du 27 mai 1963** | « portant encouragement de l'État au développement de l'agriculture » | n° 26 du 24 mai 1963, tome 106, pp. 745-746 | notice seule ; **antécédent fondateur** du régime d'« encouragement de l'État » (subventions + prêts bonifiés) |
| **Loi n° 72-87 du 27 déc. 1972** (LF 1973), art. 28-30 | création du **fonds spécial de promotion agricole** (FSPA), fonds spécial du Trésor, ministère de l'Agriculture | n° 52 du 26 déc. 1972, tome 115, p. 1855 | notice seule (modifiée par loi n° 73-82, LF 1974, art. 69-70, JORT n° 51/1973, p. 2287) |
| **Décret n° 80-1161 du 15 sept. 1980** | octroi de l'aide du FSPA aux attributaires de lots domaniaux à vocation agricole (modif. 86-296, 88-343) | — | notice seule |
| **Loi n° 82-67 du 6 août 1982** | « portant encouragement aux investissements dans les secteurs de l'agriculture et de la pêche » | n° 54 du 10 août 1982, tome 125, **pp. 1691-1696** | notice seule ; **fascicule en image → OCR à faire** (aucune notice d'article dans le cache) |
| **Loi n° 88-18 du 2 avril 1988** | « portant promulgation du code des investissements agricoles et de pêche » | n° 23 du 8 avril 1988, tome 131, **pp. 522-526** | **structure connue article par article** (notices de cache) ; **texte en image → OCR à faire** |
| **Décret n° 86-367 du 14 mars 1986** | « refonte des taux d'intérêts applicables aux prêts accordés dans le cadre de l'encouragement de l'État au développement de l'agriculture » | n° 20 du 28 mars 1986, tome 129, pp. 434-435 | notice seule ; **contexte ajustement structurel de 1986** |
| **Décret n° 90-822 du 12 mai 1990** | « réglementant l'encouragement de l'État au développement de l'agriculture » (rectificatif 90-922) | n° 36 du 29 mai 1990, tome 133, **pp. 684-695 (12 pages de barèmes)** | notice seule ; **c'est le barème des aides (versements) du régime → OCR prioritaire** |

**Structure de la loi n° 88-18 (code des investissements agricoles et de pêche de 1988)**, établie
par les notices d'articles du cache (recids 114078-114088) — utile pour cadrer l'OCR :
- Titre I, dispositions générales : principes (art. 1-12), classement de l'investissement (art. 13-15) ;
- Titre II, **encouragements communs** : octroi (art. 16-19), **avantages fiscaux (art. 20)**,
  **avantages financiers (art. 21-26)** ← c'est ici que vivent les primes (versements) ;
- Titre III, **avantages spécifiques** : activités prioritaires (art. 27-32), **avantages aux jeunes
  agriculteurs et pêcheurs et aux techniciens (art. 33-35)**, activités de service (art. 36-37),
  régions à conditions climatiques difficiles et gouvernorats côtiers (art. 38) ;
- Titre IV, dispositions diverses (art. 39-48).
- **Abrogée par la loi n° 93-120** (code d'incitations aux investissements) **sauf** l'art. 2 § 1,
  les art. 10, 11, 12 (hors son § 2) et l'art. 48.

**Antécédent et filiation (dans les mots des notices).** Le régime fondateur est l'« encouragement
de l'État au développement de l'agriculture » (loi n° 63-17, 1963), servi par subventions et prêts
bonifiés et porté budgétairement par le **fonds spécial de promotion agricole** (1972). La loi
n° 82-67 (1982) puis le **code de 1988** (loi n° 88-18) rangent ces aides sous un régime
d'« encouragement aux investissements » couvrant ensemble l'agriculture et la pêche, avec avantages
fiscaux **et** financiers (primes). Le code de 1988 est absorbé par le code d'incitations aux
investissements de 1993 (déjà écrit dans la fiscalité). Les taux d'intérêt des prêts sont
« refondus » par le décret n° 86-367 **de mars 1986**, dans la foulée de l'ajustement structurel ;
le barème des aides est entièrement réécrit par le décret n° 90-822 (1990). La vérification du mot
exact des « exposés des motifs » et des contextes reste subordonnée à l'OCR des fascicules.

---

## 2. Articulation des fonds — un, deux ou trois ? Réponse : **au moins quatre fonds distincts**

Le grep du précis mélangeait trois noms ; le dépouillement de `jort_cache` en sépare **quatre**,
qui ne sont pas le même fonds.

| # | Fonds | Texte repère | Rôle | Rapport aux autres |
|---|---|---|---|---|
| A | **Fonds spécial de promotion agricole (FSPA)** | créé par LF 1973 (loi n° 72-87, art. 28-30) ; modif. LF 1974 (loi n° 73-82) ; décret 80-1161 | aides aux attributaires de lots domaniaux, promotion agricole | **ancêtre budgétaire** du soutien à l'investissement ; candidat au prédécesseur du FOSDAP (à confirmer) |
| B | **Fonds de développement agricole (FDA)** | **supprimé** par la LF 1995 (loi n° 94-127 du 26 déc. 1994), ressources versées au budget général (`_taxes_fonds_speciaux.qmd`) | — (dissous) | **texte créateur non identifié** ; **n'est pas** le fonds qui vit en 2017 (il est supprimé en 1995) |
| C | **Fonds de développement de la compétitivité dans les secteurs de l'agriculture, de la pêche et des industries agro-alimentaires** | **créé** par la même LF 1995 (loi n° 94-127, art. 45-49) ; organisé par décret n° 95-1420 (31 juil. 1995) puis renommé/refondu « …secteur de l'agriculture et de la pêche » par décret n° 96-1563 (9 sept. 1996) | **financé par des taxes** sur produits ; compétitivité, mise à niveau | = le **FST agricole déjà écrit** dans la fiscalité (`#sec-fst-agriculture`). **Distinct** du soutien à l'investissement |
| D | **« Fonds spécial de développement de l'agriculture [et de la pêche] »** | nommé par le **décret gouvernemental n° 2017-389** (art. de rattachement budgétaire des primes APIA) comme support des primes « jusqu'à ce que le Fonds tunisien de l'investissement exerce ses missions » | **porte les primes d'investissement agricole versées par l'APIA** | **texte fondateur NON identifié** dans `jort_cache` (voir § 6). C'est le fonds du chapitre 5 |

**Conclusion.** La LF 1995 fait **deux** choses à ne pas confondre : elle **supprime** le « fonds de
développement agricole » (B) **et** elle **crée** le fonds de compétitivité agricole (C). Aucun des
deux n'est le fonds (D) qui, en 2017, porte encore les primes de l'APIA. Le précis gagnera à
distinguer nettement : C (taxes → compétitivité, fiscalité) et D (budget → primes d'investissement,
ce chapitre). Le fonds D descend vraisemblablement du régime « encouragement de l'État au
développement de l'agriculture » (loi 63-17 → FSPA 1972 → codes 1982/1988 → décret 90-822), mais la
**continuité juridique du support budgétaire reste à prouver par le texte** (fiche r-fosdap-creation).

### Statut de FOSDAP : **non établi** (par un texte fondateur)

- Le **développé** « Fonds spécial de développement de l'agriculture et de la pêche » et le **sigle
  FOSDAP** sont **attestés par des sources externes** : rapport d'achèvement de la BAD
  (ADB-BD-IF-2006-162, Tunisie, projet Cap Bon, liste des sigles : « FOSDAP : Fonds spécial de
  développement de l'agriculture et de la pêche ») et un guide de l'entrepreneur tunisien (cabinet
  NFM/Mashrou3i), qui décrit « le Fonds Spécial de Développement de l'Agriculture et de la Pêche »
  et ses primes.
- Mais **le texte qui crée ce fonds et en fixe l'intitulé officiel n'est pas identifié** dans
  `jort_cache` (aucune notice de loi ou décret au titre « fonds spécial de développement de
  l'agriculture [et de la pêche] » ; la création est probablement enfouie dans un article de loi de
  finances, dont l'intitulé ne porte pas le nom du fonds).
- **En conséquence et conformément au ticket : ne pas employer le sigle FOSDAP dans le précis tant
  que le texte fondateur n'est pas trouvé.** Le décret n° 2017-389 l'appelle « fonds spécial de
  développement de l'agriculture » (sans « et de la pêche ») : l'écart de dénomination entre le
  décret et les sources externes est lui-même à lever par le texte fondateur.

---

## 3. Série des primes APIA — localisée, mais **pas de série homogène de primes *versées***

### Ce qui existe
- **Un seul point de primes *versées* (disbursed)** : **54 MD en 2009**, « primes versées par
  l'APIA », cité par la Banque mondiale (2014), famille *rapport extérieur* — déjà dans la fiscalité
  (`#tbl-df-bm-cout`). Ce n'est **pas** une série.
- **Des séries de primes *approuvées* (subventions sur investissements approuvés)** sur le portail
  **agridata.tn** (producteur APIA, 37 jeux). Fichiers récupérés et catalogués dans `tunisia-data`
  (`data/raw/apia/`, `sources/apia-agridata-urls.csv`). Agrégats annuels calculés :

| Année | Primes approuvées (MD) — jeu « par gouvernorat/délégation 2010-2016 » | Primes approuvées (MD) — jeu « par projet 2010-2017/2019 » | Primes approuvées (MD) — « indicateurs » nationaux (cumul déc.) |
|---|---:|---:|---:|
| 2010 | 55,5 | 42,0 | — |
| 2011 | 60,2 | 42,8 | — |
| 2012 | 57,5 | 40,0 | — |
| 2013 | 61,9 | 43,5 | — |
| 2014 | 74,6 | 52,6 | — |
| 2015 | 74,2 | 54,3 | — |
| 2016 | 93,1 | 73,1 | — |
| 2017 | — | 50,0 | — |
| 2018 | — | 167,7 (?) | — |
| 2021 | — | — | 162,5 |
| 2022 | — | — | 168,2 |
| 2023 | — | — | 139,5 |
| 2024 | — | — | 129,4 |
| 2025 | — | — | 120,1 |
| 2026 (sept.) | — | — | 83,0 |

### Le problème d'homogénéité (décisif)
- **Deux jeux agridata donnent des totaux de primes approuvées divergents pour les mêmes années**
  (2010 : 55,5 vs 42,0 MD ; 2016 : 93,1 vs 73,1 MD — écart ~30 %). Les périmètres (secteurs inclus,
  année de décision vs d'approbation, primes engagées vs décaissées) **ne sont pas documentés** par
  le portail. Épisser ces jeux fabriquerait une fausse continuité : **à proscrire.**
- Le jeu 2017-2019 s'arrête en fait à 2018 et son total 2018 (167,7 MD) est hors d'échelle vs 2016 :
  suspicion de double compte ou de changement de définition — **non utilisable tel quel.**
- Le jeu national « indicateurs » (2021-2026) est propre (cumul mensuel, déc. = total annuel) mais
  **ne recouvre pas** les années antérieures : pas de pont vérifiable avec 2010-2016.
- **Trou 2017-2020** non comblé de façon fiable.
- **Primes approuvées ≠ primes versées.** Le propos « versements » du chapitre porte sur le
  **décaissé**, que seule la valeur BM 2009 touche. (Coïncidence notable, non une preuve : 2009
  versées = 54 MD ≈ 2010 approuvées par délégation = 55,5 MD.)

### Verdict de série
- **Primes *versées* : pas de série** — un point (2009). Lacune établie, **à ne pas combler par une
  valeur plausible.**
- **Primes *approuvées* : séries existantes mais hétérogènes et contradictoires** entre jeux
  agridata ; une série longue homogène **n'est pas constituable** par simple assemblage. La
  **source-cible** qui la rendrait homogène est la publication propre de l'APIA — **Bulletin
  statistique / rapport d'activité annuel** (`apia.com.tn/conjoncture-agricole.html` ; bulletins
  mensuels/annuels), à récupérer en PDF et, au besoin, les éditions anciennes par Wayback (voir
  fiche r-apia-primes-versees). Tant qu'elle n'est pas obtenue, la série ne se publie qu'avec la
  mention « primes *approuvées* » et la rupture de source 2016/2021 signalée.

---

## 4. Notions à glossaire (à verser par le terminologue — proposées ici, non écrites au glossaire)

- **APIA — Agence de promotion des investissements agricoles** : établissement public sous tutelle du
  ministère de l'Agriculture, guichet des avantages (primes, prêts fonciers) de l'investissement
  agricole. Source canonique pressentie : texte de création de l'APIA (à identifier — non fait ici)
  et `apia.com.tn`.
- **Encouragement de l'État au développement de l'agriculture** : régime d'aides (subventions + prêts
  bonifiés) institué par la loi n° 63-17 du 27 mai 1963 ; barème réglé par le décret n° 90-822.
- **Fonds spécial de promotion agricole (FSPA)** : fonds spécial du Trésor créé par la LF 1973 (loi
  n° 72-87, art. 28-30).
- **Prime d'investissement agricole** (avantage financier) : part du coût d'investissement versée par
  le budget via l'APIA ; à distinguer de l'avantage fiscal (déjà au glossaire fiscalité) et de la
  subvention *approuvée* (engagée) vs *versée* (décaissée).
- **Prêt foncier** : prêt bonifié à l'acquisition de terres agricoles, suivi par l'APIA (colonne
  dédiée du jeu « indicateurs »). Source : agridata.tn / APIA.
- **FOSDAP** : **à NE PAS inscrire** tant que le texte fondateur n'est pas trouvé (sigle non établi).

---

## 5. Références CSL candidates

**Déjà présentes dans `precis/fr/fiscalite/references.json`** (réutiliser les clés) :
- `loi-82-67` (loi n° 82-67 du 6 août 1982, agriculture et pêche) — intitulé seul, à enrichir après OCR.
- `loi-88-18-code-investissements-agricoles` (loi n° 88-18 du 2 avril 1988) — intitulé seul ;
  **compléter la note** avec la structure des titres/articles établie au § 1 ci-dessus.
- `decret-gouv-2017-389-incitations-financieres`, `banquemondiale2014-revolution-inachevee`,
  `loeprick2014-incitations-fiscales` (primes APIA 2009).

**À créer** (CSL-JSON) :

```json
[
  {"id":"loi-63-17-encouragement-agriculture","type":"legislation",
   "title":"Loi n° 63-17 du 27 mai 1963, portant encouragement de l'État au développement de l'agriculture",
   "title-short":"Loi n° 63-17 du 27 mai 1963",
   "issued":{"date-parts":[[1963,5,27]]},
   "note":"JORT n° 26 du 24 mai 1963, tome 106, pp. 745-746 (notice jort_cache, recid 117574). Fascicule en image : OCR à faire. Antécédent du régime d'encouragement à l'investissement agricole."},

  {"id":"loi-72-87-lf-1973-fonds-promotion-agricole","type":"legislation",
   "title":"Loi n° 72-87 du 27 décembre 1972, portant loi de finances pour la gestion 1973 — fonds spécial de promotion agricole, art. 28 à 30",
   "title-short":"Loi n° 72-87 du 27 décembre 1972 (LF 1973)",
   "issued":{"date-parts":[[1972,12,27]]},
   "note":"JORT n° 52 du 26 décembre 1972, tome 115, p. 1855 (notice jort_cache, recid 116579). Création du fonds spécial de promotion agricole (FSPA). Modifiée par la loi n° 73-82 (LF 1974), art. 69-70, JORT n° 51/1973, p. 2287. Image : OCR à faire."},

  {"id":"decret-86-367-taux-interet-encouragement-agriculture","type":"legislation",
   "title":"Décret n° 86-367 du 14 mars 1986, portant refonte des taux d'intérêts applicables aux prêts accordés dans le cadre de l'encouragement de l'État au développement de l'agriculture",
   "title-short":"Décret n° 86-367 du 14 mars 1986",
   "issued":{"date-parts":[[1986,3,14]]},
   "note":"JORT n° 20 du 28 mars 1986, tome 129, pp. 434-435 (notice jort_cache, recid 95417). Contexte : ajustement structurel de 1986. Image : OCR à faire."},

  {"id":"decret-90-822-encouragement-agriculture","type":"legislation",
   "title":"Décret n° 90-822 du 12 mai 1990, réglementant l'encouragement de l'État au développement de l'agriculture",
   "title-short":"Décret n° 90-822 du 12 mai 1990",
   "issued":{"date-parts":[[1990,5,12]]},
   "note":"JORT n° 36 du 29 mai 1990, tome 133, pp. 684-695 (12 pages de barèmes ; notice jort_cache, recid 93415). Rectificatif : décret n° 90-922. Barème des aides (versements) du régime. Image : OCR prioritaire."},

  {"id":"loi-94-127-lf-1995-fonds","type":"legislation",
   "title":"Loi n° 94-127 du 26 décembre 1994, portant loi de finances pour la gestion 1995 — suppression du fonds de développement agricole ; fonds de développement de la compétitivité dans les secteurs de l'agriculture, de la pêche et des industries agro-alimentaires, art. 45 à 49",
   "title-short":"Loi n° 94-127 du 26 décembre 1994 (LF 1995)",
   "issued":{"date-parts":[[1994,12,26]]},
   "note":"JORT n° 103 du 30 décembre 1994, tome 137, p. 2046 (notice jort_cache, recid 112662). Supprime le fonds de développement agricole ET crée le fonds de compétitivité agricole (déjà cité dans la fiscalité). Image : OCR à faire."},

  {"id":"decret-95-1420-fonds-competitivite-agricole","type":"legislation",
   "title":"Décret n° 95-1420 du 31 juillet 1995, fixant les règles d'organisation, de fonctionnement et les modes d'intervention du fonds de développement de la compétitivité dans les secteurs de l'agriculture, de la pêche et des industries agro-alimentaires",
   "title-short":"Décret n° 95-1420 du 31 juillet 1995",
   "issued":{"date-parts":[[1995,7,31]]},
   "note":"JORT n° 64 du 11 août 1995, tome 138, pp. 1667-1668 (notice jort_cache, recid 90838). Renommé/refondu par décret n° 96-1563 du 9 septembre 1996. Fonds C (compétitivité, taxes) — distinct du fonds des primes d'investissement."},

  {"id":"apia-indicateurs-investissement-prive","type":"dataset",
   "title":"Les indicateurs de l'investissement agricole privé (national, mensuel cumulé, 2021-2026)",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2026]]},
   "URL":"https://catalog.agridata.tn/dataset/d92956e3-9ff1-407e-ba80-df5677e01eae",
   "note":"agridata.tn. Colonne valeur_des_subventions_d'investissement_en_million_dinars (primes APPROUVÉES, cumul annuel = décembre). Copie locale : tunisia-data/data/raw/apia/apia_indicateurs_investissement_prive_2021-2026.xlsx (SHA-256 f07559039d7786d0db83daab7ea179a6b293f7233812fab2fdf9fd74e42324cf). Consulté le 10 novembre 2026."},

  {"id":"apia-subventions-gouv-delegation-2010-2016","type":"dataset",
   "title":"Répartition des investissements et des subventions par gouvernorat et délégation, 2010-2016",
   "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
   "issued":{"date-parts":[[2016]]},
   "URL":"https://catalog.agridata.tn/dataset/eb70ed58-6984-4112-aef3-0141d59c87c2",
   "note":"agridata.tn. Colonnes INV, PRIMES (dinars) — primes APPROUVÉES. Totaux divergents d'avec le jeu « par projet 2010-2017 » (~30 %) : périmètres non documentés, ne pas épisser. Copie locale : tunisia-data/data/raw/apia/apia_investissements_subventions_par_gouv_delegation_2010-2016.csv (SHA-256 b4c99084548e39297fd2b1ef5d4431fedfccf4e1c7e6fc26069df13404e148cb). Consulté le 10 novembre 2026."},

  {"id":"afdb-2006-pcr-cap-bon","type":"report",
   "title":"Tunisie — Projet de valorisation des grands périmètres irrigués (Cap Bon), rapport d'achèvement",
   "author":[{"literal":"Banque africaine de développement"}],
   "issued":{"date-parts":[[2006]]},
   "URL":"https://www.afdb.org/fileadmin/uploads/afdb/Documents/Project-and-Operations/ADB-BD-IF-2006-162-FR-TUNISIE-CAP-BON-PCR-VGTID2_.PDF",
   "note":"Atteste le développé du sigle : « FOSDAP : Fonds spécial de développement de l'agriculture et de la pêche ». Famille : rapport extérieur. PDF à récupérer dans tunisia-data si cité."}
]
```

---

## 6. Recherches infructueuses (fiches proposées pour `docs/recherches.yml`)

Aucune fiche existante ne couvre ces objets (vérifié dans `docs/recherches.yml` le 10/11/2026).

```yaml
- id: r-fosdap-creation
  objet: texte créant le « fonds spécial de développement de l'agriculture [et de la pêche] » (FOSDAP), support budgétaire des primes d'investissement agricole versées par l'APIA, nommé « fonds spécial de développement de l'agriculture » par le décret gouvernemental n° 2017-389
  ou: [docs/notes/agriculture-investissement-documentation.md, precis/fr/fiscalite/_regimes_incitation.qmd]
  requetes:
    titres_fts: ['fonds AND developpement AND agriculture AND peche', 'fonds AND special AND developpement AND agriculture']
    titres_like: ['%fonds special de developpement de l''agriculture%', '%developpement de l''agriculture et de la peche%', '%promotion agricole%']
    iort_ar: ['صندوق خاص لتنمية الفلاحة', 'صندوق خاص للتنمية الفلاحية', 'تنمية الفلاحة والصيد البحري']
    plein_texte: [FOSDAP, 'fonds special de developpement']
    depuis: 1970-01-01
  passes:
  - date: 2026-11-10
    role: documentaliste
    sources: [jort_cache]
    couverture: "jort_cache (≈ avril 2026) : LIKE et FTS sur titres, 1957-2026 — aucun texte au titre « fonds spécial de développement de l'agriculture [et de la pêche] » ; trouvés seulement le fonds spécial de promotion agricole (loi 72-87, 1972) et le fonds de compétitivité agricole (loi 94-127, 1995). Développé/sigle attestés hors JORT (AfDB ADB-BD-IF-2006-162 ; guide entrepreneur). Lacune : création probablement dans un article de loi de finances (titre sans le nom du fonds) ; nomenclature des fonds spéciaux du Trésor des LF non dépouillée texte par texte ; intitulés arabes non rejoués faute de miroir iort chargé."
    couvert_jusqu_au: 2026-04-10
    resultat: aucun
  a_faire: [dépouiller la rubrique « fonds spéciaux du Trésor / ministère de l'Agriculture » des lois de finances 1973-1995, OCR; chercher le texte de création/rattachement cité par les visas du décret n° 2017-389 et par le décret n° 90-822]

- id: r-apia-primes-versees
  objet: série des primes d'investissement agricole EFFECTIVEMENT VERSÉES (décaissées) par l'APIA, année par année (une seule valeur connue : 54 MD en 2009, Banque mondiale 2014)
  ou: [docs/notes/agriculture-investissement-documentation.md]
  requetes:
    plein_texte: ['primes versées APIA', 'subventions décaissées investissement agricole', 'rapport d''activité APIA']
    depuis: 2005-01-01
  passes:
  - date: 2026-11-10
    role: documentaliste
    sources: [agridata, apia.com.tn, web]
    couverture: "agridata.tn (37 jeux APIA) : seules des primes APPROUVÉES, et deux jeux divergent de ~30 % pour 2010-2016 ; jeu national « indicateurs » propre pour 2021-2026 ; trou 2017-2020 ; aucune colonne de primes décaissées. apia.com.tn : bulletin statistique mensuel/annuel repéré (conjoncture-agricole.html) mais non récupéré en PDF ; rapports d'activité annuels non ouverts ; Wayback de apia.com.tn non sondé. Un seul point de primes versées (BM 2014, 2009 = 54 MD)."
    couvert_jusqu_au: 2026-11-10
    resultat: aucun
  a_faire: [récupérer les bulletins statistiques et rapports d'activité annuels de l'APIA (PDF) et leurs éditions anciennes par Wayback; demander à l'APIA la série engagées vs décaissées; vérifier si les rapports annuels de performance de la mission Agriculture portent le décaissé]
```

---

## 7. VERDICT : le chapitre **tient**, comme chapitre d'institution + dispositif, **pas** comme série de versements

- **La colonne vertébrale textuelle pré-1993 tient** : six textes datés et situés (1963 → fonds 1972
  → 1982 → code 1988 → ajustement 1986 → barème 1990), la structure de la loi n° 88-18 est connue
  article par article, et la filiation vers le code de 1993 (déjà écrit) est claire. Reste un **OCR**
  (fascicules en image) pour transcrire articles et barèmes — travail borné, non bloquant pour la
  décision d'ouverture.
- **L'articulation des fonds tient** : quatre fonds distincts identifiés et démêlés ; la LF 1995
  supprime B et crée C ; D (celui des primes APIA) a son **texte fondateur à trouver** (fiche
  r-fosdap-creation). Le sigle **FOSDAP reste non établi** et ne doit pas être employé.
- **La série des primes NE tient PAS comme « versements »** : un seul point de primes *versées*
  (2009) ; les primes *approuvées* d'agridata existent mais sont hétérogènes et contradictoires —
  série homogène non constituable sans la publication propre de l'APIA (cible identifiée). C'est une
  **lacune établie**, pas à combler par une valeur plausible.
- **Portée pour l'arbitrage (préalable du plan, § 5-3)** : le chapitre 5 apporte une matière réelle
  (institution APIA + guichet + dispositif historique daté), mais son versant « versements effectifs »
  est mince tant que l'APIA n'a pas livré sa série décaissée. Il tient donc **mieux comme chapitre de
  dispositif historico-institutionnel** que comme chapitre à épine budgétaire de versements. À
  recouper avec les chapitres 4 (crédit) et 7 (calamités) pour juger si deux des trois « tiennent ».

---

## 8. Backlog (à router par l'archiviste selon `docs/backlog-routage.md` — non écrit ici au backlog)

- **OCR prioritaire** (corpus `PDFs-legislation-tunisie`, fascicules en image) :
  loi n° 82-67 (JORT 54/1982, pp. 1691-1696) ; loi n° 88-18 (JORT 23/1988, pp. 522-526, surtout
  art. 20-26 et 33-35) ; **décret n° 90-822 (JORT 36/1990, pp. 684-695, barème des aides)** ;
  décret n° 86-367 ; loi n° 63-17. (Tesseract du poste est très lent : ~minutes/page ; prévoir un
  traitement par lot hors session.)
- **Texte fondateur du FOSDAP (fonds D)** : dépouiller la rubrique « fonds spéciaux du Trésor /
  ministère de l'Agriculture » des LF 1973-1995 et les visas du décret n° 2017-389 (fiche
  r-fosdap-creation). Tant qu'il manque, sigle FOSDAP interdit dans le précis.
- **Texte de création de l'APIA** : non identifié ici ; à chercher (guichet du chapitre).
- **Série APIA des primes versées (décaissées)** : récupérer en PDF les bulletins statistiques et
  rapports d'activité annuels de l'APIA (apia.com.tn) + éditions anciennes par Wayback ; demander à
  l'APIA engagées vs décaissées ; ranger dans `tunisia-data/data/raw/apia/` (fiche r-apia-primes-versees).
- **Réconciliation des jeux agridata** : expliquer l'écart ~30 % entre les deux jeux 2010-2016
  (périmètre sectoriel ? engagé vs approuvé ?) avant tout usage en série.
- **Note de concordance** à prévoir si le chapitre mobilise plusieurs jeux : primes *approuvées* vs
  *versées*, mille dinars vs million de dinars, par gouvernorat vs national, année de décision vs
  d'exécution.
- **Références CSL** du § 5 à verser dans `precis/fr/<livre-agriculture>/references.json` lorsque le
  livre sera créé ; enrichir `loi-88-18-...` (structure) et `loi-82-67` (après OCR).
- **Fichiers rangés dans `tunisia-data`** (feu vert AGENTS.md) : `data/raw/apia/` (7 fichiers) +
  catalogue `sources/apia-agridata-urls.csv` (URL, date, SHA-256) + ligne ajoutée au playbook
  `sources/chercher-des-donnees-tunisie.md` (portail agridata.tn).
