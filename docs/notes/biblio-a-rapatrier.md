# Inbox bibliographe — références à rapatrier dans Zotero

> Handoff pour l'agent `bibliographe` (Phase 1, issue #17) ou pour traitement manuel.
> Source canonique de la bibliographie = **Zotero groupe 6529669** (`scripts/sync_biblio.py`
> tire Zotero → `references.json`). Toute référence ajoutée à la main dans un
> `references.json` doit être **remontée dans Zotero** pour être pérenne et obtenir une
> clé de citation stable (champ « Extra » : `citation-key: xxx`).

## En attente

### Glossaire — contribution personnelle d'État, quote-part de l'assuré (versement du 23/09/2026)

Branche `feat/glossaire-cpe-cotisation-assure`. Deux textes cités par `precis/glossaire.yml`
(entrées de fiscalité et de cotisations), ajoutés à la main, FR et AR, dans le **fonds commun**
`precis/{fr,ar}/references.json`, **pas encore dans Zotero**. Motif du fonds commun : l'annexe
de glossaire est filtrée par livre (`build_glossary.ancres_utilisees`), et ces notions peuvent
être ancrées par plusieurs livres ; précédent `decret2002-916`. Le `controle-rangement` devra
confirmer, une fois la branche fusionnée, que l'usage réel est bien multi-livres ; s'il n'est
cité que par un livre, il le signalera « à ranger » dans la collection de ce livre.

URL = `pdf_fr` / `pdf_ar` de l'enregistrement `jort_cache.db` du texte lui-même, contrôlées le
23/09/2026 (`curl -k`, HTTP 206, `application/pdf`). Titres des entrées AR : **titres arabes**,
lus au fascicule arabe (à la différence du lot « Retraites » ci-dessous, qui garde les titres
français) ; pagination : celle de l'édition française dans les deux fichiers, pagination arabe
en note.

| Clé | Texte | recid | Remarque |
|---|---|---|---|
| `decret86-1188` | Décret n° 86-1188 du 12 novembre 1986 (barème de la contribution personnelle d'État par tranches de 20 dinars) | 95172 | JORT n° 71 du 5/12/1986, pp. 1426-1431 (éd. fr., lue à l'image) ; titre AR lu au sommaire et à la p. 1426 de l'éd. ar. ; exécutoire le 7/12/1986 (un jour franc) |
| `decret2017-358` | Décret gouvernemental n° 2017-358 du 9 mars 2017 (complète le décret n° 2012-2369 : art. 26 quater à 26 decies, « contrat-dignité ») | 77614 | JORT n° 21 du 14/03/2017, **pp. 996-998** (éd. fr.), pp. 819-820 (éd. ar.) ; art. 26 sexies p. 997 (fr.), pp. 819-820 (ar.) ; `page` vide dans `jort_cache.db` |

- [ ] `decret86-1188` : fin du texte dans l'édition arabe non vérifiée page à page (seuls le
      sommaire et la p. 1426 ont été lus) ; le sommaire place le texte suivant à la p. 1431.
- [ ] `decret2017-358` : date de dépôt du fascicule au siège du gouvernorat de Tunis non établie,
      donc date d'exécution non calculée (loi n° 93-64, art. 2) ; le décret n'a pas de clause d'effet.
- [ ] Rapatriement Zotero **après fusion**, sur feu vert humain : `permissions` → `verifier` →
      `dry-run` → `pousser-un` → `comparer` → `pousser-tout` → `ranger` (collection : aucune,
      c'est-à-dire « Commun », sauf si le contrôle dit autrement) → `controle-rangement`. Ni le
      `dry-run` ni le `controle-rangement` n'ont été lancés lors du versement (consigne : aucun
      workflow).

### Livre « Retraites » — autres régimes de pension de la CNSS (versement du 23/09/2026)

Source : `docs/notes/cnss-autres-regimes.md` (§ 1, 15 ; textes lus au fascicule). Ajoutées à la
main, FR et AR, dans le fonds commun `precis/{fr,ar}/references.json` (convention « textes de la
chaîne d'un régime au fonds commun »), **pas encore dans Zotero**. URL = `pdf_fr` / `pdf_ar` de
l'enregistrement `jort_cache.db` du texte lui-même, toutes contrôlées le 23/09/2026 (`curl -k`,
HTTP 206, `application/pdf`). Titres des entrées AR : titres français (usage des autres entrées de
la chaîne), sauf `decretloi2020-33`, dont l'original est arabe. Pagination : celle de l'édition
française, dans les deux fichiers ; l'éventuelle pagination arabe est dite en note.

| Clé | Texte | recid | Remarque |
|---|---|---|---|
| `decret77-546` | Décret n° 77-546 du 15 juin 1977 (pêcheurs) | 100411 | |
| `decret80-103` | Décret n° 80-103 du 23 janvier 1980 (art. 11 bis) | 98958 | un chiffre illisible (éd. fr.) |
| `loi81-6-rect` | Rectificatif à la loi n° 81-6 (JORT n° 26/1981, p. 844) | 115311 | clé propre (précédent `decret82-1030-rect`) ; `issued` = publication |
| `decret82-1028` | Décret n° 82-1028 du 8 juillet 1982 (art. 3 bis) | 97393 | rectificatif (recid 97255) décrit en note |
| `decret82-1359` | Décret n° 82-1359 du 21 octobre 1982 (indépendants non agricoles) | 97252 | |
| `decret82-1360` | Décret n° 82-1360 du 21 octobre 1982 (indépendants agricoles) | 97253 | |
| `decret89-1611` | Décret n° 89-1611 du 10 octobre 1989 | 93663 | |
| `decret90-548` | Décret n° 90-548 du 27 mars 1990 (pêcheurs indépendants, RSAA) | 93467 | |
| `decret91-604` | Décret n° 91-604 du 30 avril 1991 (prorogation, RTTE) | 92912 | |
| `decret93-357` | Décret n° 93-357 du 8 février 1993 (prorogation, non agricoles) | 92063 | |
| `loi95-102` | Loi n° 95-102 du 27 novembre 1995 (art. 74) | 112524 | |
| `loi96-66` | Loi n° 96-66 du 22 juillet 1996 (art. 60, 61, 63, 69) | 112416 | **pp. 1603-1604**, et non « 1603 » comme dit la note (signature en tête de la p. 1604) |
| `loi97-61` | Loi n° 97-61 du 28 juillet 1997 (art. 41, 64) | 112255 | |
| `arrete-1997-01-27-retraite-complementaire` | Arrêté du 27 janvier 1997 (règlement complémentaire) | 60565 | |
| `decret2019-379` | Décret gouvernemental n° 2019-379 du 22 avril 2019 | — | **sans URL** (voir TODO) |
| `decretloi2020-33` | Décret-loi n° 2020-33 du 10 juin 2020 (auto-entrepreneur) | 144377 | clé renommée (note : `decret-loi2020-33`) selon la convention `decretloiAAAA-N` ; FR sans URL (`pdf_fr` vide) ; AR `Ja0542020` |
| `loi2021-37` | Loi n° 2021-37 du 16 juillet 2021 (travail domestique) | 162301 | |
| `arrete-2020-07-10-prime-pensions` | Arrêté conjoint du 10 juillet 2020 (visas) | 147599 | **pp. 1515-1517** (note : 1515-1516) ; « attribuées » (note : « servies ») |
| `arrete-2026-08-05-allocation-pauvres` | Arrêté conjoint du 5 août 2026 (visas) | — | **sans URL** (postérieur à `jort_cache.db`) ; **pp. 1611-1612** (note : 1610-1611) ; fascicules FR et AR téléchargés de pist.tn le 23/09/2026 |

**Promues au fonds commun** (FR et AR), retirées du fichier de leur livre, comme `loi97-4` :
- `decret2002-916` (de `cotisations_sociales`) : désormais cité par le glossaire du livre
  « Retraites » (`regime-bas-revenus`) et par le chapitre à venir. Intitulé corrigé : « relatif aux
  modalités d'application » (fascicule décodé, `jort_cache.db`, visas de 2019 et 2026), et non
  « fixant » ; note complétée (art. 13-15, 22-25 ; dépôt 2 mai 2002 → exécutoire 7 mai 2002).
- `decret-loi2024-4` (de `prestations_sociales`) : `page` renseigné, **2897-2901** (pieds de page
  du fascicule français `Jo1292024`), à la place de « pagination non établie » ; 5293 est la
  pagination arabe. Note complétée (art. 26-33, dépôt 23 octobre 2024 → 28 octobre 2024).
- `arrete-2025-08-29-allocation-pauvres` (de `prestations_sociales`), entrée inchangée : la note
  documentaire (§ 12) s'appuie sur ses visas, et l'arrêté du 5 août 2026 modifie l'arrêté de 2024
  « tel que modifié par l'arrêté du 29 août 2025 ».

**Notes corrigées** (FR et AR) : `loi81-6` (rectificatif lu, modificatifs listés, « coefficient
multiplicateur moyen ») ; `loi2007-43` (dépôt le **27 juin 2007** → exécutoire le 2 juillet 2007 ;
`page` 2197-2199 → **2198-2199**, vérifié au sommaire) ; `arrete-1998-07-29-revalorisation-rtns`
(« texte non lu » → art. 1-3 lus, effet 1er mai 1998) ; `loi2002-32` (correspondance avec le RTFR
attestée par l'annuaire 2013 ; dépôt 16 mars 2002 → 21 mars 2002) ; `decret95-1166` (fusion des
régimes de 1982 ; dépôt 14 juillet 1995 → 19 juillet 1995) ; `decret89-107` (exécutoire le
19 janvier 1989 ; prorogation par le décret n° 91-604) ; compléments sans contradiction :
`loi2002-104` (art. 20 lu sur l'éd. ar. ; exécutoire le 5 janvier 2003), `decret2003-894`
(exécutoire le 5 mai 2003), `arrete-1978-11-18-retraite-complementaire` (modificatif de 1997),
`loi89-73` (art. 3, 93-97). Dates de dépôt relues le 23/09/2026 dans la mention imprimée des
fascicules (couche texte ou décodée) : n° 55 et 96/1995, 60/1996, 11/1997, 63/1998, 22, 35 et
106/2002, 34/2003, 51/2007, 34/2019, 54/2020 (éd. ar.), 68/2021, 129/2024, 80/2026. Aucune date de
dépôt n'est citée pour la loi n° 97-61 (effet fixé par son art. 2).

**Écartées** :
- `arrete-2019-06-19-affiliation-ruraux` : métadonnées seules ([M]), texte non lu.

Clôture, seconde passe (23/09/2026, après la réorganisation de `_secteur_prive.qmd` et le
tableau `tbl-carte-regimes` de `index.qmd`, qui cite désormais `decret77-546`, `decret82-1359`,
`decret82-1360` et `decret-loi2024-4`) — **état de la worktree, glossaire en cours de révision** :
- les 257 clés citées par `precis/fr/retraites/*.qmd` résolvent, FR et AR (fichier du livre +
  fonds commun + `references.bib`) ; ids identiques FR/AR dans les quatre fichiers touchés
  (retraites 57, commun 267, cotisations 9, prestations 48).
- URL des 19 nouvelles clés, des quatre clés du tableau et des trois promues comparées champ à
  champ à `pdf_fr` / `pdf_ar` de leur recid dans `jort_cache.db` : toutes conformes ; sans URL,
  comme prévu, `decret2019-379`, `arrete-2026-08-05-allocation-pauvres` (FR et AR) et
  `decretloi2020-33` (FR seul).
- rendus FR et AR de « Retraites », « Cotisations sociales » et « Prestations sociales » :
  0 `[?]`, 0 `?@`, aucun `figdata` modifié.
- `push_biblio.py --verifier` : 514 entrées, 0 perte. `--dry-run` (sans clé) : conversion des
  514 entrées sans erreur.
- `--controle-rangement` (lecture seule, API publique) : 495 références dans Zotero,
  531 citations ; 430 bien rangées ; **3 à déclasser** : `decret2002-916` (retirer
  `cotisations_sociales`), `decret-loi2024-4` et `arrete-2025-08-29-allocation-pauvres` (retirer
  `prestations_sociales`) — toutes trois citées désormais par « Retraites » et par leur livre
  d'origine ; 0 à ranger ; 62 sans citation ; **19 absentes de Zotero**, liste identique, clé à
  clé, aux 19 du tableau ci-dessus. Rien poussé. **À relancer sur `master` après la fusion** (le
  glossaire, lu par `cles_citees`, bouge encore).

Reste à faire — **dans cet ordre**, feu vert humain requis pour toute écriture Zotero :

**Aucune descente `sync_biblio` avant les étapes 2 et 3.** Zotero range encore
`decret-loi2024-4` et `arrete-2025-08-29-allocation-pauvres` dans `prestations_sociales`, et
`decret2002-916` dans `cotisations_sociales` : une descente les renverrait dans le fichier de ces
livres, hors de portée de « Retraites » (rendu `[?]`), et écraserait les 12 corrections.

- [ ] 1. `--permissions` → `--verifier` → `--dry-run`, avec la clé d'écriture.
- [x] 2. **Fait le 23/09/2026** : `--corriger` sur les 12 clés — 12 corrigées, 0 échec.
      Pour mémoire, **`--corriger`** (Zotero ignore ces corrections ; `--pousser` ne crée que les absentes
      et `--comparer` ne compare pas la note) :
      `loi81-6,loi2007-43,arrete-1998-07-29-revalorisation-rtns,loi2002-32,decret95-1166,decret89-107,decret2002-916,decret-loi2024-4,loi2002-104,decret2003-894,arrete-1978-11-18-retraite-complementaire,loi89-73`.
      `--corriger` abandonne tout le lot à la première clé absente de Zotero : n'y ajouter
      **aucune** des 19 nouvelles avant leur création. Si la chaîne de la section RSNA
      (`decret2003-1212,decret74-499,loi60-33,decret82-1030`) est toujours en attente, la joindre
      à celle-ci en un seul appel.
- [x] 3. **Fait le 23/09/2026** : `--appliquer-rangement` — 3 déclassements, `decret2002-916`
      hors `cotisations_sociales`, `decret-loi2024-4` et `arrete-2025-08-29-allocation-pauvres`
      hors `prestations_sociales` ; contrôle à blanc suivant : 0 à reclasser.
      Pour mémoire, **déclassement** : `--appliquer-rangement` à blanc, vérifier qu'il ne touche que
      `decret2002-916` (− `cotisations_sociales`), `decret-loi2024-4` et
      `arrete-2025-08-29-allocation-pauvres` (− `prestations_sociales`) — plus ce qui reste
      pendant de la section RSNA —, puis `--appliquer-rangement --pousser`. À faire **avant**
      l'étape 4 : ensuite, `--appliquer-rangement` rangerait aussi les 19 dans `retraites`.
- [x] 4. **Fait le 23/09/2026** : `pousser-un` puis `pousser-tout` — 19 créées, 0 échec ;
      restées sans collection, donc au fonds commun (décision humaine : on les classera plus
      tard). `--comparer` signale un **faux écart `shortTitle`** : Zotero rend `shortTitle`, que
      la descente renomme en `title-short` (`RENOMMAGES` de `sync_biblio.py`), mais `--comparer`
      n'applique pas ce renommage. À corriger plus tard dans `push_biblio.py` (non corrigé).
      Pour mémoire, pousser les 19 clés : `pousser-un` → `comparer` → `pousser-tout` :
      `arrete-1997-01-27-retraite-complementaire`, `arrete-2020-07-10-prime-pensions`,
      `arrete-2026-08-05-allocation-pauvres`, `decret2019-379`, `decret77-546`, `decret80-103`,
      `decret82-1028`, `decret82-1359`, `decret82-1360`, `decret89-1611`, `decret90-548`,
      `decret91-604`, `decret93-357`, `decretloi2020-33`, `loi2021-37`, `loi81-6-rect`,
      `loi95-102`, `loi96-66`, `loi97-61`.
- [ ] 5. **Non lancé** (23/09/2026). `--ranger` : sans effet attendu sur les 19 (leur fichier est le fonds commun, sans
      livre) ; elles restent sans collection et redescendent dans le fonds commun, conformément
      à la convention « chaîne d'un régime au fonds commun ».
- [ ] 6. **Décision humaine du 23/09/2026 : on classera plus tard** ; d'ici là, les 19 restent
      sans collection. **Conflit de convention à trancher** (même question que la section RSNA ci-dessous) :
      citées par le seul livre « Retraites », les 19 apparaîtront au contrôle comme « à ranger :
      retraites », et tout `--appliquer-rangement` ultérieur les rangerait dans `retraites`, donc
      dans `precis/{fr,ar}/retraites/references.json`. Ne pas lancer `--appliquer-rangement`
      sans exclure ces clés tant que la règle n'est pas fixée.

Vérifications de métadonnées en attente (sans écriture Zotero) :
- [ ] `decret2019-379` : **absent de `jort_cache.db`** (le fascicule n° 34/2019 n'y porte que deux
      notices, recid 169836 et 169837). Candidats vérifiés le 23/09/2026 (HTTP 206, décret lu
      pp. 1277-1278 dans `Jo0342019`) : `https://www.pist.tn/jort/2019/2019F/Jo0342019.pdf` et
      `https://www.pist.tn/jort/2019/2019A/Ja0342019.pdf`. À poser une fois la notice présente
      dans `jort_cache.db`. Défaut connexe : le recid 169837 (arrêté du 22 avril 2019, espadon)
      porte `date_signature` 2022-10-12 et `pdf_ar` `Ja1132019`, incohérents avec son fascicule.
- [ ] `decretloi2020-33`, entrée FR : pas d'édition française (`pdf_fr` vide, 404) ; l'intitulé
      français vient de la note commune n° 3 de la DGI (art. 36 de la loi n° 2024-48).
- [ ] `arrete-2026-08-05-allocation-pauvres` : URL à poser quand `jort_cache.db` couvrira août 2026
      (candidats `Jo0802026` / `Ja0802026`, HTTP 200 le 23/09/2026).
- [ ] `decret80-103` : chiffre illisible (« au cours des … premières années ») à lire sur l'éd. ar.

Annuaire statistique 2010 de la CNSS (passe du 23/09/2026, TODO du bibliographe de
`_secteur_prive.qmd`, § non-salariés et § Tunisiens à l'étranger) :
- [x] **Clé distincte `cnss-annuaire-2010`** versée dans `precis/{fr,ar}/retraites/references.json`,
      et non une troisième édition dans la note de `cnss-annuaires-statistiques` : les pages
      citées n'appartiennent qu'au fichier 2010, et un locateur sur l'entrée composite ne dirait
      pas de quelle édition il s'agit. « الدليل الإحصائي 2010 » (couverture lue à l'image ; page
      de titre : إدارة الدراسات و مراقبة التصرف، مصلحة الإحصائيات), éd. arabe, 292 pages
      (en note, pas de `number-of-pages`), séries 2000-2010 ; `issued` laissé vide (2010 est
      l'année des données ; le PDF est créé en avril 2012, métadonnée de fichier). Pages lues
      (page du fichier ; p. 170 imprimée « 143 ») : RTNS ensemble, classes, p. 141 ; RTTE,
      assurés p. 170, classes p. 173. L'édition 2013 ne publie les classes qu'à partir de 2005
      (p. 233 et 268 lues). **Hors convention « archives du web »** : `cnss.tn` sert toujours le
      fichier, identique octet pour octet (7 462 383 octets, SHA-1 `0df636ea…`, téléchargé le
      23/09/2026) ; URL = adresse de l'éditeur ; capture du 16/07/2019 en note (horodatage lu au
      CDX, empreinte CDX décodée = SHA-1 du fichier) ; captures 2022 et 2024 d'une autre empreinte.
      Citée l. 1144 (`p. 141`) et l. 1246 (`p. 170 et 173`) ; les deux TODO sont retirés.
- [x] Note de `cnss-annuaires-statistiques` (FR et AR) complétée des pages lues des parties
      consacrées aux autres régimes, 2017 / 2013 (d'après `tunisia-data/sources/cnss-annuaires.md` ;
      pages 2013 recoupées sur le fichier le 23/09/2026), et d'un renvoi à `cnss-annuaire-2010`.
- [ ] Zotero (feu vert humain) : **pousser `cnss-annuaire-2010`**, puis la ranger dans
      `retraites` (citée par ce seul livre, comme `cnss-annuaires-statistiques`) ; **`--corriger
      cnss-annuaires-statistiques`** si elle est déjà dans Zotero, sans quoi la prochaine descente
      effacera les pages ajoutées à sa note. `push_biblio.py --verifier` (hors ligne) : 515 entrées,
      0 perte. Rendus FR et AR de « Retraites » : 0 `[?]`, 0 `?@`. `dry-run` et `controle-rangement` non lancés dans
      cette passe (workflows interdits par la consigne) : à lancer à la clôture.
- [ ] Hors du dépôt, à signaler : `tunisia-data/sources/cnss-urls.csv` dit l'annuaire 2010
      « non exploité », quand `cnss-annuaires.md` l'exploite pour les classes du RTNS et du RTTE.

### Livre « Retraites » — RSNA avant 1974 et réformes du cœur du régime (versement du 23/09/2026)

Source : `docs/notes/rsna-histoire-reformes.md` (§ 1, 2, 5 et 7.2 ; textes lus au fascicule).
Ajoutées à la main, FR et AR, **pas encore dans Zotero**. Depuis la réorganisation du § RSNA
de `_secteur_prive.qmd` (passe de clôture du 23/09/2026, ci-dessous), les huit sont citées par
le seul livre « Retraites ».

Textes juridiques, dans le fonds commun `precis/{fr,ar}/references.json` (convention du
versement CNRPS du 22/09/2026 : textes de la chaîne d'un décret de régime au fonds commun, comme
`decret74-499`, `decret82-1030`, `decret2007-2148`). URL = `pdf_fr` / `pdf_ar` du même
enregistrement `jort_cache.db`, toutes contrôlées le 23/09/2026 (`curl -k`, HTTP 206,
`application/pdf`). Les titres arabes restent les titres français, comme pour les autres entrées
AR de la chaîne (aucune traduction machine).

| Clé | Texte | recid |
|---|---|---|
| `decret71-452` | Décret n° 71-452 du 17 décembre 1971 (prestations *minima* transitoires) | 103269 |
| `decret76-981` | Décret n° 76-981 du 19 novembre 1976 (CAVIS) | 100779 |
| `decret82-1030-rect` | Rectificatif au décret n° 82-1030 (art. 17 al. 3, « l'âge normal ») | 97254 |
| `decret94-1477` | Décret n° 94-1477 du 4 juillet 1994 (abroge le décret n° 76-981) | 91308 |
| `arrete-1975-07-04-age-mineurs` | Arrêté du 4 juillet 1975 (55 ans, mineurs) | 69285 |
| `arrete-2015-09-11-age-mineurs` | Arrêté du 11 septembre 2015 (55 ans, agents mineurs) | 50206 |
| `arrete-2023-05-22-age-assainissement` | Arrêté du 22 mai 2023 (55 ans, assainissement et déchets) | 172137 |

- Rectificatif du décret n° 82-1030 en **clé propre** : la décote « jusqu'à l'âge normal » en
  procède (note, § 6, écart 4), la prose le citera comme source distincte. La note de
  `decret82-1030` y renvoie. `issued` = date de publication (19/10/1982, `jort_cache.db`).
- `decret94-1477` : pages **1193-1194** (`jort_cache.db` et fascicule : art. 6 et signature
  p. 1194), et non « 1193 » comme l'écrit la note documentaire.
- Corrigées (FR et AR) : `decret74-499` — « 71-432 » → « 71-452 » ; rectificatif du JORT n° 39
  du 7 juin 1974, p. 1252, **lu à l'image** le 23/09/2026 (art. 39 : article 16 → 15 ; art. 62
  al. b : article 62 → 61), URL `Jo03974` / `Ja03974` (`pdf_ar` du recid 102251, HTTP 206) ;
  `loi60-33` — « Métadonnées seules ; texte non lu » remplacé par le contenu des art. 1 à 5 (1-4
  lus à l'image, 5 par OCR) ; `decret82-1030` — renvoi à la clé du rectificatif.
- Non versées : `decret78-962`, `decret89-268` (modificatifs de la CAVIS, intitulés seuls
  connus) ; rectificatif du décret n° 74-499 (décrit dans la note de l'entrée principale, la
  prose ne le cite pas à part).

Source statistique, dans le livre `precis/{fr,ar}/retraites/references.json` (cité par ce seul
livre, comme `cnrps-etats-financiers`) :

| Clé | Référence | Remarque |
|---|---|---|
| `cnss-annuaires-statistiques` | CNSS, « الدليل الإحصائي 2017 » (éd. arabe, URL principale, titre en tête) et « Annuaire statistique 2013 » (éd. française, en note) | **hors convention « archives du web »** : `cnss.tn` sert toujours les deux fichiers, identiques octet pour octet aux copies exploitées (taille, SHA-1 et nombre de pages vérifiés le 23/09/2026). URL = adresse de l'éditeur ; captures en note comme copies de vérification (20220304034917 et 20190716124119, horodatages et empreintes lus au CDX le 23/09/2026) |

Hors du dépôt, à signaler : `tunisia-data/sources/cnss-annuaires.md` et `cnss-urls.csv` disent
l'empreinte de la capture de l'annuaire 2017 « non recoupée » ; elle l'est désormais (CDX :
`2LOQYUHOYRWL2YVEIHC45VI73X2TSUMN`, identique au fichier).

Clôture (23/09/2026) : rendus FR et AR du livre « Retraites » sans `?@` ; les 8 clés résolues
par un document de test (citeproc, bibliographies des deux `_quarto.yml`) ;
`push_biblio.py --verifier` : 492 entrées, 0 perte ; `--dry-run` : conversion des 492 entrées
sans erreur (sans clé d'API, il ne retranche pas l'existant : « 492 à créer » n'est pas un
décompte réel) ; `--controle-rangement` : 420 bien rangées, 0 à déclasser, 0 à ranger, 64 sans
citation, 0 absente de Zotero (les 8 nouvelles clés, non citées, n'entrent pas dans le décompte).

Seconde clôture (23/09/2026, après la réorganisation du § RSNA par le rédacteur) :

- Résolution : toutes les clés citées par `_secteur_prive.qmd` et `index.qmd` (108 clés de
  bibliographie, renvois `@sec-`/`@tbl-`/`@fig-` exclus) résolvent en
  FR et en AR par `quarto pandoc --citeproc` sur un document de test, avec les bibliographies des
  deux `_quarto.yml` ; de même les 42 clés du livre « Cotisations sociales » (FR et AR), touché
  par le déplacement de `loi97-4`. Aucun rendu relancé (le rendu servi était en relecture).
  Aucun identifiant en double entre fonds commun et fichiers de livre.
- [x] `loi97-4` **promue au fonds commun** (FR et AR), retirée de
      `precis/{fr,ar}/cotisations_sociales/references.json` : elle est désormais citée par deux
      livres. URL AR = `pdf_ar` du recid 112333 (`Ja01097.pdf`, HTTP 200 le 23/09/2026 ; l'entrée
      AR la portait déjà). Citation posée dans `_secteur_prive.qmd` (« … ramené ce taux global à
      18 % [@loi97-4] »), TODO du bibliographe supprimé. **Provisoire** tant que Zotero la
      range dans la collection `cotisations_sociales` : la prochaine descente la remettrait dans
      le fichier du livre « Cotisations sociales », hors de portée du livre « Retraites ».
- [x] `decret2003-1212` (FR et AR) : la note disait « porte de 1,25/20e à 7,25/20e » ; corrigé en
      « de 6,25/20e (rédaction du décret n° 94-1429, en vigueur depuis le 1er janvier 1994) à
      7,25/20e » (note documentaire § 4.1 ; `tunisia-data/sources/cnss-annuaires.md` ; note de
      `decret94-1429`, art. 5 b) nouveau, effet art. 2). La note de `decret88-1137` décrit encore
      la série du dossier des cotisations comme « 1,25/20e en 1974 → 7,25/20e en 2003 » : c'est
      une remarque sur ce dossier, laissée telle quelle.
- `loi60-33` : la note ne dit plus « non lu » (FR et AR). Le TODO de `index.qmd` (l. 32, « la
  loi n° 60-33 n'a pas été lue (métadonnées seules) ») est devenu inexact : au rédacteur.
- Locateurs contrôlés contre la note documentaire et les notes d'entrée ; conformes, sauf :
  - `decret97-291` : art. 1 (l. 479 et 517 : « ne touche à l'article 53 que pour remplacer
    “veuves” par “conjoint survivant” ») et art. 2 (l. 509 : abrogation de l'art. 52). La note
    de l'entrée dit l'art. 53 nouveau « pas relu », la note documentaire dit le décret « pas
    rouvert ». Affirmation et locateurs sans lecture attestée : au documentaliste ;
  - `decret74-499`, art. 10, 11 (l. 90 : réserve technique, transfert de 15 millions de dinars)
    et art. 35-36 (l. 498) : hors de la liste « lu à l'image » de la note d'entrée ; couverts
    seulement par le « [T] (art. 1-64) » global de la note documentaire, qui n'en parle pas. Le
    chiffre de 15 MD n'apparaît dans aucune des deux notes ;
  - `decret81-188`, art. 2 (l. 479, réversion à 75 %) : partage entre art. 1 et 2 déduit de
    l'intitulé ; l'art. 31 al. 2 n'a été lu que par OCR ;
  - `loi60-30`, art. 2, 5, 68, 119-120 (l. 40) : lus par OCR, non confirmés à l'image.
- `push_biblio.py --verifier` : 495 entrées, 0 perte. `--dry-run` : conversion des 495 entrées
  sans erreur (sans clé d'API, « 495 à créer » n'est pas un décompte réel).
  `--controle-rangement` : 484 références dans Zotero, 504 citations ; 417 bien rangées ;
  **3 à déclasser** (`decret2003-1212`, `decret97-555`, `loi97-4` — retirer
  `cotisations_sociales` : désormais citées aussi par « Retraites ») ; **1 à ranger**
  (`decret88-1137` — ajouter `retraites`) ; 63 sans citation ; **11 absentes de Zotero** : les
  8 clés RSNA ci-dessus et `minfin-ep-2023`, `minfin-ep-2024`, `minfin-ep-2025` (section CNRPS
  ci-dessous), toutes citées par « Retraites » seul. Rien poussé.

Reste à faire (feu vert humain requis pour toute écriture Zotero) :
- [ ] Pousser les 8 clés, puis `ranger`. Selon le contrat du contrôle, citées par le seul livre
      « Retraites », elles voudraient la collection `retraites` et descendraient dans
      `precis/{fr,ar}/retraites/references.json` — à l'encontre de la convention « chaîne d'un
      décret de régime au fonds commun » rappelée plus haut. Conflit à trancher avec celui de la
      section h) du 11/09/2026, avant toute montée.
- [ ] **Corrections locales que Zotero ignore encore** (lu le 23/09/2026 dans l'Extra des items
      du groupe, API publique) : `decret2003-1212` porte toujours « de 1,25/20e à 7,25/20e » ;
      `decret74-499` porte toujours « 71-432 » ; `loi60-33` porte toujours « non lu » ;
      `decret82-1030` ne renvoie pas au rectificatif. `--pousser` ne crée que les absentes et
      `--comparer` ne compare pas la note : sans `--corriger
      decret2003-1212,decret74-499,loi60-33,decret82-1030`, la prochaine descente écrasera ces
      quatre corrections, FR et AR.
- [ ] Déclasser `decret2003-1212`, `decret97-555` et `loi97-4` (retirer `cotisations_sociales`)
      et ranger `decret88-1137` dans `retraites` : `--appliquer-rangement`, à blanc puis
      `--pousser`. Sans ce déclassement, la prochaine descente renverrait ces trois clés dans le
      livre « Cotisations sociales » et le livre « Retraites » ne les résoudrait plus.
- [ ] `decret76-981` : confirmer à l'image les art. 1-3, 23-24 et 26-27 (lus par OCR).
- [ ] Dates exécutoires de `decret94-1477` et des arrêtés de 2015 et 2023 : date de dépôt au
      gouvernorat de Tunis inconnue.

### Livre « Retraites » — taux de cotisation d'équilibre de la CNRPS

Ajoutées à la main dans `precis/{fr,ar}/retraites/references.json`, **pas encore dans
Zotero** ; documents tirés des archives du web (convention du bibliographe : `archive`,
`archive_location`, `accessed`) :

| Clé | Référence | Remarque |
|---|---|---|
| `cnrps-guides-rapports` | CNRPS, guides statistiques 2000-2010 et 2010-2014, rapports d'activité 2016-2020 | entrée reprise d'une autre branche, où elle existe aussi : doublon d'`id` à fusionner |
| `cnrps-etats-financiers` | CNRPS, états financiers 2015, 2016 et 2018 (provisoires) | captures du 01/03/2021, 25/02/2021, 01/03/2021 (CDX lu le 22/09/2026) |
| `minfin-remunerations` | copie à l'identique de l'entrée du livre « Rémunérations publiques » | désormais citée dans deux livres : à ranger en « Commun » |

**Bloquant pour le rapatriement (clôture du 23/09/2026)** : `push_biblio.py --verifier` rend
rc=1, **7 pertes de champ** sur trois entrées — `archive`, `archive_location` et `accessed` de
`cnrps-etats-financiers` et `cnrps-guides-rapports`, `accessed` de `cnss-chiffres`. La
conversion CSL → Zotero ne porte pas ces champs, alors que Zotero les a (`archive`,
`archiveLocation`, `accessDate`). Défaut du convertisseur, préexistant (entrées committées en
40510bd), non corrigé dans cette passe. **Ne pas pousser ces deux clés avant la correction** :
l'emplacement d'archive, qui est toute la source, se perdrait.

### Livre « Retraites » — CNRPS avant 1985, chaîne de la loi n° 59-18 (versement du 22/09/2026)

Ajoutées à la main dans `precis/{fr,ar}/references.json` (fonds commun, comme `loi59-18` et
`loi81-70`), **pas encore dans Zotero**. Collection Zotero cible : **`retraites`** (seul livre
qui les cite ; à poser par `ranger` d'après l'usage réel, une fois la section 1 du chapitre CNRPS
rédigée). Le fichier commun suit l'usage local : `loi81-70` et `decret81-939`, cités par le seul
livre « Retraites », y sont déjà ; le rendu résout dans les deux cas. Source :
`docs/notes/cnrps-avant-1985.md`, § 1 (textes lus au fascicule) ; métadonnées recoupées dans
`jort_cache.db` ; URL = `pdf_fr` / `pdf_ar` du même enregistrement, toutes vérifiées
(HTTP 206, `application/pdf`, `curl -k` : le certificat de pist.tn est expiré au 22/09/2026).

| Clé | Texte | recid |
|---|---|---|
| `decret59-78` | Décret n° 59-78 du 17 mars 1959 (limites d'âge, 60 ans) | 107383 |
| `decret59-80` | Décret n° 59-80 du 19 mars 1959 (65 ans pour des magistrats listés) | 107381 |
| `loi59-37` | Loi n° 59-37 du 28 mars 1959 (ouvriers, SNCFT) | 118149 |
| `loi59-100` | Loi n° 59-100 du 20 août 1959 (art. 52 nouveau) | 118092 |
| `decretloi61-4` | Décret-loi n° 61-4 du 30 janvier 1961 (art. 11) | 106630 |
| `loi64-45` | Loi n° 64-45 du 3 novembre 1964 (art. 45) | 117478 |
| `loi68-2` | Loi n° 68-2 du 8 mars 1968 (art. 26 § V) ; rectificatif dans la note | 117109 (+ 117107) |
| `decretloi70-1` | Décret-loi n° 70-1 du 14 septembre 1970 ; rectificatif dans la note | 103656 (+ 103490) |
| `decretloi70-3` | Décret-loi n° 70-3 du 14 septembre 1970 (loi 59-37) | 103658 |
| `decretloi74-9` | Décret-loi n° 74-9 du 2 octobre 1974 (militaires) | 116312 |
| `loi76-61` | Loi n° 76-61 du 12 juillet 1976 (art. 4) | 115961 |
| `loi77-36` | Loi n° 77-36 du 25 mai 1977 (art. 52 bis) | 115808 |
| `loi79-66-lf1980` | Loi n° 79-66 du 31 décembre 1979, LF 1980, art. 43-45 | 115521 |
| `loi80-24` | Loi n° 80-24 du 23 mai 1980 | 115454 |

Clés de la note renommées selon la convention du dépôt (`decretloiAAAA-N`, cf.
`decretloi2011-48`) : `dl61-4` → `decretloi61-4`, `dl70-1` → `decretloi70-1`, `dl70-3` →
`decretloi70-3`, `dl74-9` → `decretloi74-9`. Pas de clé `-rect` (`loi68-2-rect`,
`dl70-1-rect`, `loi73-71-rect`) : les rectificatifs sont décrits dans la note de l'entrée
principale, comme l'était déjà celui de `loi73-71` (note complétée : contenu et URL du rectificatif). À scinder si la prose en cite un comme
source distincte.

**Déplacées** du fichier du livre « Cotisations sociales » vers le fonds commun (FR et AR,
entrées inchangées) : `loi73-71`, `loi74-101-lf1975` — elles seront citées aussi par le livre
« Retraites », qui ne lit pas le fichier de « Cotisations sociales ». **Dans Zotero**, si elles y
portent la collection `cotisations_sociales`, il faudra la leur retirer (déclassement vers
Commun) une fois la section 1 du chapitre CNRPS rédigée — sans quoi `sync_biblio.py` les
redescendrait dans le seul livre « Cotisations sociales » et le livre « Retraites » rendrait
`?@`. Action sortante : feu vert humain requis.

Défauts de `jort_cache.db` relevés (consignés dans les notes des entrées) :
- recid 103490 (rectificatif du DL 70-1) : `jort_annee` = 1970, alors que le fascicule est le
  n° 19 de **1971** ; les champs `pdf_fr` / `pdf_ar` pointent bien 1971.
- recid 116312 (DL 74-9) : typé « Loi » et loi modifiée datée du « 2 février 1959 » ; le
  fascicule (OCR de la p. 2158 relu) porte « Décret-loi » et « 5 février 1959 ».
- recid 115961 (loi 76-61) : fascicule daté du 9 juillet 1976, avant la signature du 12 juillet
  — écart relevé, non résolu.

Reste à faire :
- [ ] Rapatrier les 14 entrées dans Zotero (collection `retraites`), puis `ranger` — feu vert humain.
- [x] Relancer `--controle-rangement` après rédaction : fait le 23/09/2026 (voir la clôture
      ci-dessous).
- [ ] Titres : repris de `jort_cache.db`, accents et ponctuation rétablis (« retraites » →
      « retraite » pour `loi76-61`, « Regime des Pensions » → minuscules pour `loi80-24`) ; seul
      celui du DL 74-9 a été confronté au fascicule.
- [ ] Titres arabes des 14 entrées AR : titre français conservé, comme pour `loi59-18`,
      `loi81-70`, `loi73-71` ; à remplacer par le titre du JORT arabe lorsqu'il aura été lu
      (aucune traduction machine).
- [ ] `loi59-100` : numérotation de l'article additionnel (« 15 bis » ou « 52 bis ») à relire à
      l'image.

#### Clôture du 23/09/2026 — chapitre CNRPS réorganisé (section 1 rédigée)

Fait :
- [x] Résolution : les 195 clés de `_secteur_public.qmd` et `index.qmd` résolvent contre les
      bibliographies déclarées des deux `_quarto.yml` (FR et AR) ; livres « Retraites » FR et AR
      rendus, aucun `?@` ni `[?]`.
- [x] `loi59-19`, art. premier relu à l'image (JORT n° 8 de 1959, p. 100, page 18 du PDF) :
      « La Caisse Nationale des Retraites constitue un Établissement public doté de la
      personnalité civile et de l'autonomie financière, rattaché au Secrétariat d'État aux
      Finances et au Commerce » ; même date que la loi n° 59-18 (5 février 1959). Les phrases
      qui la citent (`_secteur_public.qmd`, section 1 ; `index.qmd`, « Deux caisses ») sont
      exactes.
- [x] Locators précisés d'après `cnrps-avant-1985.md` (§ 1, 4.3, 4.5, 6) :
      `[@decretloi70-1, art. 1-2]` → `art. 1 (art. 21 et 22) et art. 2` (refontes, et sources du
      tableau 1959-1985), `art. 1 (art. 22 § II) et art. 2` (plafond),
      `art. 1 (art. 26 § II) et art. 2` (rente d'invalidité) ; `[@loi68-2, art. 1-2]` →
      `art. 1 (art. 26 § V) et art. 2`.

Usage réel et Zotero (lecture seule, 23/09/2026) :

| Clé | Citée par | Dans Zotero |
|---|---|---|
| `decret59-78`, `decret59-80`, `loi59-100`, `loi68-2`, `decretloi70-1`, `decretloi74-9`, `loi79-66-lf1980`, `loi80-24` | Retraites | non |
| `loi59-37`, `decretloi61-4`, `loi64-45`, `decretloi70-3`, `loi76-61`, `loi77-36` | aucun livre | non |
| `loi73-71` | Retraites et Cotisations sociales | oui, collection `cotisations_sociales` |
| `loi59-19` | Retraites et Cotisations sociales | oui |
| `loi74-101-lf1975` | Cotisations sociales seul (pas le livre « Retraites ») | oui |

Reste à faire (feu vert humain requis pour toute écriture Zotero) :
- [ ] Pousser les **8 clés citées** (1re ligne du tableau), puis `ranger` : collection `retraites`.
- [ ] Les **6 clés non citées** : les pousser aussi, pour qu'elles ne se perdent pas au prochain
      `sync_biblio.py`. Sans citation, `ranger` ne leur donne aucune collection, et elles
      descendent alors en « Commun » : c'est attendu, et c'est là qu'elles sont déjà.
- [ ] Déclasser `loi73-71` (retirer `cotisations_sociales`) : `--controle-rangement` la signale.
- [ ] `loi74-101-lf1975` : citée par le seul livre « Cotisations sociales », elle y redescendra
      au prochain sync, alors qu'elle se trouve aujourd'hui dans le fonds commun. C'est sans
      effet tant que le livre « Retraites » ne la cite pas. S'il vient à la citer, il faudra la
      déclasser.

### Sources de données (catalog.yml de tunisia-data) — type CSL `dataset`
Clés référencées par les séries de données (`tunisia_data.meta()`), à créer dans Zotero
pour que les figures du précis soient citées et tracées :

| Clé | Source | Type |
|---|---|---|
| `minfin-remunerations` | Min. Finances — Série répartition économique des dépenses (masse salariale) | dataset |
| `minfin-indicateurs-fp` | Min. Finances — Indicateurs des finances publiques (déficit, dette, pression fiscale) | dataset |
| `ins-cnat-2015` | INS — Comptes de la Nation, base 2015 | dataset |
| `ins-fonction-publique-2021` | INS — Caractéristiques des agents de la fonction publique et leurs salaires 2010-2021 | dataset |
| `ins-fonction-publique-2025` | INS — Évolution des effectifs et des rémunérations des agents de la fonction publique tunisienne 2018-2025 (août 2026). Versée à la main dans `precis/{fr,ar}/remunerations_publiques/references.json`, comme la clé 2021. PDF : <https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/La%20fonction%20publique%20-%202018-2025.pdf> | dataset |
| `bct-bsf` | BCT — Bulletin des Statistiques Financières (et archives) | dataset |
| `bct-ra` | BCT — **Rapport Annuel** (annuel depuis 1959 ; source de la série `bct-emploi-occupe`, population active occupée 2007-2024) | dataset |

Fiches de provenance correspondantes : `tunisia-data/sources/*.md`.

### Ticket #6 — section A.2 (rémunérations publiques)

Ajoutées à la main dans `precis/fr/remunerations_publiques/references.json` (résolues au
rendu), **pas encore dans Zotero** :

| Clé de citation | Référence | Collection Zotero cible |
|---|---|---|
| `imf-tunisia-art4-2020` | FMI, *Tunisia: 2020 Article IV Consultation* (publié fév. 2021) | Commun (→ `precis/{lang}/references.json` partagé) |
| `wb-tunisia-per-2020` | Banque mondiale, *Tunisia Public Expenditure Review* (2020) | Commun |

**Attention** : le livre `remunerations_publiques` n'est pas encore mappé dans
`COLLECTION_TO_BOOK` (`scripts/sync_biblio.py`). À ajouter si une collection Zotero dédiée
est créée ; sinon ranger ces deux rapports en « Commun » (bibliographie partagée).

#### TODO de vérification métadonnées (avant publication)
- `imf-tunisia-art4-2020` : confirmer le **numéro exact du rapport** (probable *IMF Country
  Report No. 21/44* — ne pas confondre avec CR 20/103) et l'URL du PDF.
- `wb-tunisia-per-2020` : confirmer titre complet / report number et l'URL pérenne du
  document Banque mondiale.
- Vérifier les **chiffres** cités dans A.2 sur les PDF primaires (17,6 % ; 14,7 % ; >60 % ;
  effectifs) — cf. `docs/notes/perimetre-masse-salariale.md` §III.
- À terme, ces estimations FMI/BM seront **corroborées/remplacées par des sources
  officielles tunisiennes** fournies par l'auteur (Finances / Présidence du gouvernement /
  INS) — cf. `perimetre-masse-salariale.md` §III.5.

### URL corrigées (à reporter dans Zotero — sync_biblio écrase references.json)
- `ins-cnat-2015` : URL → `https://www.ins.tn/statistiques/153` (l'ancienne `/publications` renvoyait 404).
- `minfin-remunerations` / `minfin-indicateurs-fp` : `http://www.finances.gov.tn` (landing ; affiner vers la page série si dispo).
- Entrées dataset **dupliquées dans `precis/ar/remunerations_publiques/references.json`** (titres en langue d'origine, non traduits) en attendant le rapatriement Zotero + mapping `COLLECTION_TO_BOOK`.
- `loi83-112` : URL jurisitetunisie (404) -> PDF JORT officiel `https://www.pist.tn/jort/1983/1983F/Jo08283.pdf`.
- `loi89-9` : URL pm.gov.tn (404) -> PDF JORT officiel `https://www.pist.tn/jort/1989/1989F/Jo00989.pdf`.

### Section A.5 — statuts spéciaux & caisses sociales (rémunérations publiques)

Ajoutées à la main dans `precis/{fr,ar}/remunerations_publiques/references.json`
(type CSL `legislation`, titres en français = langue d'origine, **dupliquées en AR non
traduites**). Résolues au rendu (`quarto render`, aucun `[?]`). **Pas encore dans Zotero.**
Même réserve `COLLECTION_TO_BOOK` que ci-dessus (livre `remunerations_publiques` non mappé →
collection dédiée ou « Commun »).

| Clé de citation | Référence | URL JORT | État |
|---|---|---|---|
| `loi67-29` | Loi n°67-29 du 14 juillet 1967, organisation judiciaire / CSM / statut de la magistrature | `https://www.pist.tn/jort/1967/1967F/Jo03067.pdf` (JORT n°30) | OK |
| `loi67-20` | Loi n°67-20 du 31 mai 1967, statut général des militaires | `https://www.pist.tn/jort/1967/1967F/Jo02467.pdf` (JORT n°24/1967) | **RÉSOLU** |
| `loi82-70` | Loi n°82-70 du 6 août 1982, statut général des forces de sécurité intérieure | `https://www.pist.tn/jort/1982/1982F/Jo05482.pdf` (JORT n°54/1982) | **RÉSOLU** |
| `decret-statut-caisses-2022` | Décret présidentiel n°2022-76 du 22 février 2022, statut particulier du personnel des organismes de sécurité sociale (CNSS, CNRPS, CNAM) | `https://www.pist.tn/jort/2022/2022F/Jo0202022.pdf` (JORT n°20/2022) | **RÉSOLU** |

#### Résolution métadonnées (A.5) — base JORT `jort_cache.db` (PDFs-legislation-tunisie)
Méthode de confirmation : recherche par **numéro de texte** dans la base JORT locale (78 953
textes, champs `numero`/`type`/`date_signature`/`jort_numero`/`pdf_fr` issus de l'API JORT),
reproduisant exactement les 3 URLs déjà validées (`loi83-112`, `loi89-9`, `loi67-29`). L'URL
pist.tn est dérivée du `jort_numero` confirmé, puis vérifiée HTTP 200 + type PDF.
- `loi67-20` : **JORT n°24 de 1967** (Loi n°67-20 du 31 mai 1967, titre concordant dans la base). RÉSOLU.
- `loi82-70` : **JORT n°54 de 1982** (Loi n°82-70 du 6 août 1982, titre concordant). RÉSOLU.
- `decret-statut-caisses-2022` : numéro désormais **confirmé** = **Décret présidentiel n°2022-76
  du 22 février 2022**, publié au **JORT n°20 de 2022** (publication 23/02/2022), titre base :
  « relatif à l'approbation du statut particulier du personnel des organismes [de sécurité
  sociale] ». Entrée corrigée (titre + numéro + date de signature 22/02/2022). RÉSOLU.

### loi85-78 — URL JORT — RÉSOLU
- `loi85-78` (5 août 1985) : **JORT n°58 de 1985** confirmé via base JORT locale (Loi n°85-78
  du 5 août 1985, titre concordant). URL = `https://www.pist.tn/jort/1985/1985F/Jo05885.pdf`. RÉSOLU.

### Section B.1 — le régime indiciaire (rémunérations publiques)

Ajoutées à la main dans `precis/{fr,ar}/remunerations_publiques/references.json`
(type CSL `legislation`, titres en français = langue d'origine, **dupliquées en AR non
traduites**). Résolues au rendu (`quarto render _regime_indiciaire.qmd`, aucun `[?]`,
les 6 clés sortent en `data-cites`). **Pas encore dans Zotero.** Même réserve
`COLLECTION_TO_BOOK` (livre `remunerations_publiques` non mappé → collection dédiée ou « Commun »).

| Clé de citation | Référence | URL | État |
|---|---|---|---|
| `decret-97-1832` | Décret n°97-1832 du 16 sept. 1997, traitement de base des personnels de l'État/CPL/EPA | `https://www.pist.tn/jort/1997/1997F/Jo07697.pdf` (JORT n°76/1997) | **RÉSOLU** |
| `decret-2007-267` | Décret n°2007-267 du 12 fév. 2007, transfert d'indemnités spécifiques vers le traitement de base | `https://www.pist.tn/jort/2007/2007F/Jo0142007.pdf` (JORT n°14/2007) | **RÉSOLU** |
| `decret-2007-268` | Décret n°2007-268 du 12 fév. 2007, modifiant le décret 97-1832 | `https://www.pist.tn/jort/2007/2007F/Jo0142007.pdf` (JORT n°14/2007, même JORT que 2007-267) | **RÉSOLU** |
| `decret-99-12` | Décret n°99-12 du 4 janv. 1999, catégories des grades (État/CL/EPA) | `https://www.pist.tn/jort/1999/1999F/Jo00499.pdf` (JORT n°4/1999) | **RÉSOLU** |
| `loi85-12` | Loi n°85-12 du 5 mars 1985, régime des pensions civiles et militaires de retraite et des survivants (secteur public) | `https://www.pist.tn/jort/1985/1985F/Jo02085.pdf` (JORT n°20/1985 — **remplace** legislation-securite.tn) | **RÉSOLU** |
| `loi2017-66-lf2018` | Loi n°2017-66 du 18 déc. 2017, loi de finances pour 2018 (art. 53 — contribution sociale de solidarité) | `https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf` (JORT n°101/2017) | **RÉSOLU** |

#### Résolution métadonnées (B.1) — base JORT `jort_cache.db`
- **URLs JORT pist.tn** des 4 décrets, de `loi85-12` et de la loi de finances 2018 :
  **toutes RÉSOLUES** via la base JORT locale (numéro de JORT confirmé par le champ `jort_numero`
  du texte correspondant, titre/date concordants ; URL dérivée puis vérifiée HTTP 200 + PDF).
- **Annexes chiffrées** : les grilles de traitement de base (`decret-97-1832`) et la nouvelle
  grille des salaires (`decret-2007-268`) sont incluses dans les JORT correspondants (n°76/1997
  et n°14/2007). Vérification des valeurs chiffrées hors périmètre biblio.
- `loi85-12` : titre promulgué « **portant** régime… » confirmé (legislation-securite.tn, NATLEX) ;
  les *vu*-clauses des décrets 2007 le paraphrasent en « fixant le régime… » — wording promulgué retenu.

#### Anti-duplication — réutilisation inter-livres
- `loi85-12` (loi pensions → livre `retraites`) et `loi2017-66-lf2018` (loi de finances → livre
  `fiscalite`) : **absentes** de `precis/fr/{retraites,fiscalite}/references.json` et du partagé
  `precis/fr/references.json` au moment de l'ajout (aucun conflit de clé/contenu). Créées ici dans
  le livre `remunerations_publiques`. Toute citation future dans `retraites`/`fiscalite` doit
  **réutiliser ces mêmes clés** ; envisager de les **promouvoir dans le partagé**
  `precis/fr/references.json` (« Commun ») plutôt que de les dupliquer. À arbitrer au rapatriement Zotero.

### Section B.2 — le régime statutaire autonome (rémunérations publiques)

Ajoutées à la main dans `precis/{fr,ar}/remunerations_publiques/references.json` (12 entrées
`legislation` citées + `loi91-62` créée mais citée en prose seulement + `sipri-milex` type
`dataset`). Render FR OK, **0 `[?]`**, les 12 clés citées sortent en `data-cites`. **Pas encore
dans Zotero.** Même réserve `COLLECTION_TO_BOOK` (livre `remunerations_publiques` non mappé →
collection dédiée ou « Commun »).

URL JORT pist.tn résolues depuis `jort_cache.db` (FR = `pdf_fr`, AR = `pdf_ar` du **même**
enregistrement, identifié numéro+type+date_signature ; jamais dérivé `Jo→Ja`). **Tous les
`pdf_ar` présents → aucune entrée AR laissée sans URL.**

| Clé | Texte | URL FR | URL AR | JORT |
|---|---|---|---|---|
| `loi-org-2016-34` | Loi org. n°2016-34 du 28/04/2016 (CSM) | `Jo0352016.pdf` | `Ja0352016.pdf` | n°35/2016 |
| `loi72-40` | Loi n°72-40 du 01/06/1972 (Tribunal administratif) | `Jo02372.pdf` | `Ja02372.pdf` | n°23/1972 |
| `loi68-8` | Loi n°68-8 du 08/03/1968 (org. Cour des comptes) | `Jo01168.pdf` | `Ja01168.pdf` | n°11/1968 |
| `decret-loi-70-6` | Décret-loi n°70-6 du 26/09/1970 (statut membres Cour des comptes) | `Jo04570.pdf` | `Ja04570.pdf` | n°45/1970 |
| `decret-72-380` | Décret n°72-380 du 06/12/1972 (statut part. militaires) | `Jo04972.pdf` | `Ja04972.pdf` | n°49/1972 |
| `decret-79-96` | Décret n°79-96 du 11/01/1979 (solde militaires) | `Jo00579.pdf` | `Ja00579.pdf` | n°5/1979 |
| `decret-67-158` | Décret n°67-158 du 31/05/1967 (indemnités armée de terre) | `Jo02467.pdf` | `Ja02467.pdf` | n°24/1967 |
| `loi95-46` | Loi n°95-46 du 15/05/1995 (statut agents des douanes) | `Jo03995.pdf` | `Ja03995.pdf` | n°39/1995 |
| `decret-96-2311` | Décret n°96-2311 du 03/12/1996 (statut part. douaniers) | `Jo09996.pdf` | `Ja09996.pdf` | n°99/1996 |
| `loi2019-37` | Loi n°2019-37 du 30/04/2019 (mod. loi 85-12) | `Jo0352019.pdf` | `Ja0352019.pdf` | n°35/2019 |
| `loi68-12` | Loi n°68-12 du 03/06/1968 (statut général antérieur) | `Jo02468.pdf` | `Ja02468.pdf` | n°24/1968 |
| `loi91-62` | Loi n°91-62 du 22/07/1991 (mod. art. 2 loi 83-112) | `Jo05391.pdf` | `Ja05391.pdf` | n°53/1991 |
| `sipri-milex` | SIPRI Military Expenditure Database — Tunisia (`dataset`) | https://www.sipri.org/databases/milex | — | — |

Notes de résolution :
- `loi72-40` : deux enregistrements même date (JORT n°23 = texte original ; n°26 = rectificatif).
  Retenu le **texte original n°23**.
- `loi91-62` : **créée comme demandé** mais le chapitre la cite en prose (« modifiée par la loi
  n°91-62 ») sous `[@loi83-112, art. 2]`, **pas** via `@loi91-62`. Entrée non `data-cites`
  (n'affecte pas le compte `[?]`). À conserver pour Zotero ; à arbitrer si une citation propre
  `@loi91-62` est souhaitée dans la prose.

#### TODO objets arabes (B.2) — ne pas machine-traduire
Titres AR posés en dénomination nue (`«type» عدد «num» المؤرخ في «date»`, mois tunisiens, types :
قانون أساسي / قانون / أمر / مرسوم). **Objet arabe à compléter sur titre officiel JORT AR** pour :
`loi72-40`, `loi68-8`, `decret-loi-70-6`, `decret-72-380`, `decret-79-96`, `decret-67-158`,
`loi95-46`, `decret-96-2311`, `loi2019-37`, `loi68-12`, `loi91-62`.
- Exception : `loi-org-2016-34` porte l'objet AR **publié** (champ `titre` de la base JORT :
  « يتعلق بالمجلس الأعلى للقضاء ») → pas de TODO objet.

#### À pousser dans Zotero (B.2) — NE PAS pousser sans feu vert
Clés : `loi-org-2016-34`, `loi72-40`, `loi68-8`, `decret-loi-70-6`, `decret-72-380`,
`decret-79-96`, `decret-67-158`, `loi95-46`, `decret-96-2311`, `loi2019-37`, `loi68-12`,
`loi91-62`, `sipri-milex` (collection `remunerations_publiques` **toujours absente** de
`COLLECTION_TO_BOOK` → collection Zotero dédiée à créer + mapping, ou ranger en « Commun »).

### Bibliographie partagée (`precis/{fr,ar}/references.json`) — URLs non-pist remplacées
URL canonique d'un texte juridique = JORT pist.tn (consigne durable). Remplacement des URLs
9anoun.tn par le PDF JORT pist.tn, confirmées via la base JORT locale `jort_cache.db`.
- `loi-amen-social-2019` (loi organique n°2019-10 du 30 janvier 2019) :
  **JORT n°11 de 2019** confirmé (texte « Loi organique n°2019-10 », base JORT). URL =
  `https://www.pist.tn/jort/2019/2019F/Jo0112019.pdf` (PDF absent du champ `pdf_fr` de la base
  mais n° de JORT confirmé ; URL dérivée selon le motif 2019 et vérifiée HTTP 200 + PDF 1,3 Mo).
  Remplace `9anoun.tn`. RÉSOLU.
- `loi-irpp-is-1989` (loi n°89-114 du 30 décembre 1989, **texte promulgateur** du Code IRPP/IS) :
  visé = la loi de promulgation, et non le code consolidé. Base JORT : deux textes n°89-114 du
  30/12/1989 — celui « **portant promulgation** du code… » est au **JORT n°88 de 1989**. URL =
  `https://www.pist.tn/jort/1989/1989F/Jo08889.pdf` (vérifiée HTTP 200 + PDF 9,6 Mo). Remplace
  `9anoun.tn`. RÉSOLU. (NB : le code consolidé n'a pas de PDF JORT unique ; on cite le texte
  promulgateur, conformément à la consigne.)

### Méthode de résolution JORT (toutes entrées ci-dessus)
Les outils MCP `mcp__jort__*` n'étaient pas exposés à la session ; résolution faite via la
**base JORT locale** `PDFs-legislation-tunisie/jort_cache.db` (78 953 textes, champs issus de
l'API JORT : `numero`, `type`, `date_signature`, `jort_annee`, `jort_numero`, `pdf_fr`). La base
reproduit **à l'identique** les 3 URLs déjà validées (`loi83-112` → Jo08283, `loi89-9` → Jo00989,
`loi67-29` → Jo03067), ce qui la qualifie comme source de confirmation. Pour chaque entrée :
recherche par numéro de texte → confirmation type/date/titre concordants → URL = `pist.tn` +
`pdf_fr` (ou dérivée du `jort_numero` confirmé quand `pdf_fr` est nul) → contrôle HTTP 200 + PDF.
Aucune URL non-pist conservée ; aucun numéro deviné.

### À pousser dans Zotero (rappel — NE PAS pousser sans feu vert)
Toutes les entrées `legislation` ci-dessus ont leur URL pist.tn corrigée dans les `references.json`
FR + miroirs AR. Au rapatriement Zotero, reporter le champ `URL` (PDF pist.tn) dans l'item
correspondant (`citation-key` en « Extra »). Items concernés : decret-97-1832, decret-2007-267,
decret-2007-268, decret-99-12, loi2017-66-lf2018, loi85-78, loi67-20, loi82-70,
decret-statut-caisses-2022 (n°2022-76), loi85-12 (livre `remunerations_publiques`) ;
loi-irpp-is-1989, loi-amen-social-2019 (partagé « Commun »).

### Règle URL JORT par langue — FR = `pdf_fr`, AR = `pdf_ar`
Pour toute entrée CSL `legislation` :
- `references.json` **FR** → URL = `https://www.pist.tn` + `pdf_fr` (dossier `…F`, préfixe `Jo`).
- `references.json` **AR** → URL = `https://www.pist.tn` + `pdf_ar` **du même enregistrement**
  de `PDFs-legislation-tunisie/jort_cache.db` (dossier `…A`, préfixe `Ja`). L'URL AR est **lue
  dans le champ `pdf_ar`**, jamais dérivée par substitution `Jo→Ja`/`F→A`.

#### Correction AR (10/06/2026) — entrées AR repointées du JORT FR vers le JORT AR
Méthode : enregistrement retrouvé dans `jort_cache.db` par `pdf_fr` (= URL FR actuelle, sans
`https://www.pist.tn`), puis lecture du champ `pdf_ar`. Toutes les valeurs `pdf_ar` étaient
non nulles.

`precis/ar/references.json` :
- `loi-irpp-is-1989` → `https://www.pist.tn/jort/1989/1989A/Ja08889.pdf`
- `loi-amen-social-2019` → `https://www.pist.tn/jort/2019/2019A/Ja0112019.pdf`
  (record `pdf_fr` NULL : retrouvé par numéro+type+date = Loi organique n°2019-10 du 30/01/2019,
  JORT n°11/2019 ; `pdf_ar` présent. **NB** : l'URL **FR** de cette entrée reste *dérivée du motif*
  et **à confirmer** — le record n'a pas de `pdf_fr` dans la base.)

`precis/ar/remunerations_publiques/references.json` (13 entrées) :
- `decret-97-1832` → `.../1997/1997A/Ja07697.pdf`
- `decret-2007-267` → `.../2007/2007A/Ja0142007.pdf`
- `decret-2007-268` → `.../2007/2007A/Ja0142007.pdf`
- `decret-99-12` → `.../1999/1999A/Ja00499.pdf`
- `loi85-12` → `.../1985/1985A/Ja02085.pdf`
- `loi2017-66-lf2018` → `.../2017/2017A/Ja1012017.pdf`
- `loi83-112` → `.../1983/1983A/Ja08283.pdf`
- `loi85-78` → `.../1985/1985A/Ja05885.pdf`
- `loi89-9` → `.../1989/1989A/Ja00989.pdf`
- `loi67-29` → `.../1967/1967A/Ja03067.pdf`
- `loi67-20` → `.../1967/1967A/Ja02467.pdf`
- `loi82-70` → `.../1982/1982A/Ja05482.pdf`
- `decret-statut-caisses-2022` → `.../2022/2022A/Ja0202022.pdf`

Aucune entrée AR laissée sans URL (tous les `pdf_ar` présents). JSON AR valides ; rendu FR du
livre `remunerations_publiques` OK (0 `[?]`). Au rapatriement Zotero, les URL **AR** devront être
portées dans le champ language-specific approprié (à arbitrer selon le modèle Zotero retenu).

### Titres arabes des références juridiques (`legislation`) — posés 10/06/2026
Les entrées `legislation` des `references.json` **AR** portaient un `title` français ; remplacé
par la dénomination arabe (forme canonique `«type» عدد «numéro» المؤرخ في «date» [المتعلق بـ«objet»]`).
Dénomination = forme déjà publiée dans la prose AR (sortie CI), nettoyée ; **aucun objet
machine-traduit**. Seul le champ `title` a changé (id/type/issued/URL `Ja…`/note intacts).
Les deux JSON AR restent valides.

Objet présent en prose AR → attaché (verbatim) :
- `loi83-112` → `القانون عدد 83-112 المؤرخ في 12 ديسمبر 1983 المتعلق بضبط النظام الأساسي العام لأعوان الدولة والجماعات المحلية والمؤسسات العمومية ذات الصبغة الإدارية`
- `decret-99-12` → `الأمر عدد 99-12 المؤرخ في 4 جانفي 1999 المتعلق بضبط أصناف الرتب في الوظيفة العمومية`
- `loi2017-66-lf2018` → `القانون عدد 2017-66 المؤرخ في 18 ديسمبر 2017 المتعلق بقانون المالية لسنة 2018`

Dénomination nue (type+numéro+date, faits) → **TODO objet arabe à compléter sur titre officiel JORT**
(ne pas machine-traduire l'objet français ; à reprendre du JORT AR ou d'une prose AR future) :
- `decret-97-1832`, `decret-2007-267`, `decret-2007-268`, `loi85-12`, `loi85-78`, `loi89-9`,
  `loi67-29`, `loi67-20`, `loi82-70`, `loi-irpp-is-1989` (objet « إصدار مجلة الضريبة على دخل
  الأشخاص الطبيعيين والضريبة على الشركات » absent de la prose AR), `decret-statut-caisses-2022`
  (objet : statut particulier du personnel des organismes de sécurité sociale),
  `loi-amen-social-2019` (objet : programme AMEN SOCIAL).

### Chapitre B.3 « Régime conventionnel public » — passe bibliographe 11/06/2026

URL JORT pist.tn résolues depuis la base locale `jort_cache.db` (champs `pdf_fr`/`pdf_ar`
du **même enregistrement**, jamais dérivées par transformation de chaîne) :

- `loi60-30` (Loi n°60-30 du 14 décembre 1960, sécurité sociale, JORT n°57/1960) — **RÉSOLU**.
  Entrée FR créée à la main par le rédacteur avec URL vide → complétée.
  - FR : `https://www.pist.tn/jort/1960/1960F/Jo05760.pdf`
  - AR : `https://www.pist.tn/jort/1960/1960A/Ja05760.pdf` (entrée AR **créée**, titre =
    dénomination factuelle `القانون عدد 60-30 المؤرخ في 14 ديسمبر 1960` → **TODO objet arabe**).
  - Note FR nettoyée (clause « URL pist.tn à compléter (TODO bibliographe) » retirée).
- `loi85-78` — **déjà résolu** (FR `Jo05885` / AR `Ja05885`), vérifié conforme au cache. Sans changement.
- `loi89-9` — **titre FR corrigé** : intitulé d'origine 1989 « relative aux participations et
  entreprises publiques » (verbatim cache JORT n°9/1989). La mention « et établissements publics »
  provenait de la version amendée (loi 2006-36). AR = dénomination nue (type+numéro+date), aucune
  incohérence d'objet → inchangée.
- **Code IRPP/IS** (TODO du rédacteur, ligne 34 du `.qmd`) : clé **déjà existante** dans le
  partagé `precis/{fr,ar}/references.json` = **`loi-irpp-is-1989`** (loi n°89-114 du 30 déc. 1989,
  JORT n°88/1989, FR `Jo08889` / AR `Ja08889`). **Aucune entrée à créer.** Pour sourcer la retenue
  à la source IRPP, le rédacteur doit citer `@loi-irpp-is-1989` (non encore cité dans le chapitre ;
  n'apparaît donc pas au contrôle `[?]`).

À rapatrier dans Zotero (provisoires, livre `remunerations_publiques` **toujours absent** de
`COLLECTION_TO_BOOK` → collection dédiée à créer ou ranger en « Commun ») :
`loi60-30` (FR + AR, nouvelles/complétées), `loi89-9` (titre FR corrigé).

Contrôle : rendu FR `remunerations_publiques` OK, **0 `[?]`**. JSON FR et AR valides (36 items chacun).

#### Décrets/loi CNRPS (chaîne 85-1025 / CREGT) — 3 clés ajoutées (B.3, §5.5) — 11/06/2026
3 nouvelles clés `legislation` citées dans `_regime_conventionnel.qmd`, créées en FR + AR.
URL résolues depuis `jort_cache.db` (FR = `pdf_fr`, AR = `pdf_ar` du **même** enregistrement,
identifié par numéro+type+date ; jamais dérivées par substitution de chaîne). **Tous les
`pdf_ar` présents → aucune entrée AR sans URL.**

| Clé | Texte | URL FR | URL AR | JORT |
|---|---|---|---|---|
| `decret85-1025` | Décret n°85-1025 du 29/08/1985 (liste EPIC/soc. nat. affiliés CNRPS) | `Jo06285.pdf` | `Ja06285.pdf` | n°62/1985 |
| `loi98-37` | Loi n°98-37 du 25/05/1998 (transfert CREGT électricité/gaz/transports → CNRPS) | `Jo04398.pdf` | `Ja04398.pdf` | n°43/1998 |
| `decret98-1981` | Décret n°98-1981 du 12/10/1998 (transfert agents CREGT en activité → CNRPS) | `Jo08398.pdf` | `Ja08398.pdf` | n°83/1998 |

- TODO objets arabes (ne pas machine-traduire) : `decret85-1025`, `loi98-37`, `decret98-1981`
  posés en dénomination nue (`«type» عدد «num» المؤرخ في «date»`). Objet AR à compléter sur
  titre officiel JORT AR.
- À rapatrier dans Zotero (provisoires) : `decret85-1025`, `loi98-37`, `decret98-1981` (FR + AR).
  Livre `remunerations_publiques` **toujours absent** de `COLLECTION_TO_BOOK` → collection
  Zotero dédiée à créer ou ranger en « Commun ».
- Contrôle : rendu FR `_regime_conventionnel.qmd` OK, **0 `[?]`** ; les 3 clés sortent en
  `data-cites`. JSON FR et AR valides (39 items chacun).

### Chapitre B.4 « Le régime de marché contrôlé » — passe bibliographe 12/06/2026

4 nouvelles clés `legislation` citées dans `_regime_marche_controle.qmd`, créées en FR + AR.
URL résolues depuis `jort_cache.db` (FR = `pdf_fr`, AR = `pdf_ar` du **même** enregistrement,
identifié par numéro+type+date_signature ; jamais dérivées par substitution de chaîne).
**Tous les `pdf_ar` présents → aucune entrée AR sans URL.** URL repères de la note B.4
(`Jo0582016`, `Jo1012015`, `Jo07590`, `Jo0232014`) **confirmées** contre `pdf_fr`.

| Clé | Texte | URL FR | URL AR | JORT |
|---|---|---|---|---|
| `loi2016-48` | Loi n°2016-48 du 11/07/2016 (banques et établissements financiers) | `Jo0582016.pdf` | `Ja0582016.pdf` | n°58/2016 |
| `cc-banques-2014` | Arrêté du 17/02/2014 (agrément convention coll. sectorielle banques/étab. financiers, révisée) | `Jo0232014.pdf` | `Ja0232014.pdf` | n°23/2014 |
| `decret2015-2217` | Décret n°2015-2217 du 11/12/2015 (taux rémunération chefs d'étab./entreprises publiques et soc. à majorité publique) | `Jo1012015.pdf` | `Ja1012015.pdf` | n°101/2015 |
| `decret90-1855` | Décret n°90-1855 du 10/11/1990 (régime rémunération chefs d'entreprises à majorité publique) | `Jo07590.pdf` | `Ja07590.pdf` | n°75/1990 |

- `cc-banques-2014` : l'enregistrement de l'**arrêté du 17 février 2014** EST présent dans le
  cache (recid 50874, type `Arrete`, JORT 23/2014, `pdf_fr` + `pdf_ar` présents) → URL FR **et**
  AR résolues depuis le champ, pas seulement l'URL repère. Pas de TODO URL.
- Objets arabes : `loi2016-48` et `decret2015-2217` portent l'**objet AR publié** repris du champ
  `objet` du cache (« يتعلق بالبنوك والمؤسسات المالية » ; « يتعلق بضبط نظام تأجير رؤساء المؤسسات
  والمنشآت العمومية والشركات ذات الأغلبية العمومية ») → pas de TODO objet. **TODO objet arabe**
  (ne pas machine-traduire ; confirmer sur titre officiel JORT AR) pour : `cc-banques-2014`,
  `decret90-1855`.
- À rapatrier dans Zotero (provisoires) : `loi2016-48`, `cc-banques-2014`, `decret2015-2217`,
  `decret90-1855` (FR + AR). Livre `remunerations_publiques` **toujours absent** de
  `COLLECTION_TO_BOOK` → collection Zotero dédiée à créer ou ranger en « Commun ».
- Contrôle : rendu FR `_regime_marche_controle.qmd` OK, **0 `[?]`** ; les 4 clés résolues
  (`ref-…` présents dans le HTML). JSON FR et AR valides (43 items chacun).

#### Consolidation `minfin-ep` + loi 2018-56 (B.3/B.4) — passe bibliographe 12/06/2026

`minfin-ep` (FR + AR) : entrée faible (URL `finances.gov.tn/` page d'accueil) **remplacée** par
l'édition précise **Rapport sur les entreprises publiques, annexe 9 au PLF 2021** (Ministère de
l'économie, des finances et de l'appui à l'investissement ; données 2017-2019). `type: report`,
`issued: 2020`, URL stable gbo.tn
(`http://www.gbo.tn/sites/default/files/2021-04/Annexe%209%20LF2021%20Entreprises%20Publiques.pdf`),
landing de repli `https://www.finances.gov.tn/fr/document/le-rapport-sur-les-entreprises-publiques-ar`.
PDF archivé tracé dans `note` : `biblio_pdfs/minfin_rapport_entreprises_publiques_lf2021.pdf`.
- **Titre AR officiel confirmé** = `التقرير حول المنشآت العمومية` (intitulé repris de la page
  document officielle finances.gov.tn, chemin AR `/ar/document/altqryr-hwl-almnshyat-almwmyt` ;
  forme **منشآت** retenue, pas une machine-traduction). Pas de TODO objet AR.

`minfin-ep-2020` (FR + AR) : **créé** pour la vue d'évolution — édition annexe 9 au PLF 2020
(données 2016-2018), `issued: 2019`, URL gbo
`http://www.gbo.tn/sites/default/files/2021-02/Annexe_9_LF2020-Entreprises_publiques.pdf`,
PDF archivé `biblio_pdfs/minfin_rapport_entreprises_publiques_lf2020.pdf`. Entrée orpheline
(non citée en prose à ce stade) — n'affecte pas le compte `[?]`.

`loi2018-56-lf2019` (Loi n°2018-56 du 27 décembre 2018, loi de finances 2019, art. 28 augm.
capital BNA) : clé **absente** de tous les `references.json` (FR/AR/partagé). **Créée** en FR + AR.
- Résolution `jort_cache.db` : Loi 2018-56, 27/12/2018, **JORT n°104/2018**. `pdf_fr` **VIDE**
  (NULL), `pdf_ar` présent = `/jort/2018/2018A/Ja1042018.pdf`.
  - **FR : pas d'URL** + **TODO URL FR** (pdf_fr absent du cache ; ne pas dériver `Ja→Jo`).
  - AR : `https://www.pist.tn/jort/2018/2018A/Ja1042018.pdf` (lu dans `pdf_ar`).
- La prose B.4 cite l'art. 28 sans `[@clé]` (fait couvert par l'encadré `[@minfin-ep]`). La clé
  `loi2018-56-lf2019` est donc **disponible mais non citée** (entrée orpheline, pas de `[?]`).
  → Si l'auteur veut une citation propre, ajouter `[@loi2018-56-lf2019]` à la prose (action
  rédacteur ; non faite ici).

À rapatrier dans Zotero (provisoires, NE PAS pousser sans feu vert) : `minfin-ep` (consolidée),
`minfin-ep-2020`, `loi2018-56-lf2019` (FR + AR). Livre `remunerations_publiques` **toujours absent**
de `COLLECTION_TO_BOOK` (`scripts/sync_biblio.py`) → créer une collection Zotero dédiée + mapping,
ou ranger en « Commun ».
- Contrôle : rendu FR `remunerations_publiques` OK, **0 `[?]`**. JSON FR et AR valides (45 items chacun).

#### Suppression loi91-62 + création decret-2022-797 & loi-org-2018-29-ccl (B.1) — passe bibliographe 12/06/2026

`loi91-62` (Loi n°91-62 du 22 juillet 1991) : **SUPPRIMÉE** (FR + AR). Créée sur prémisse fausse
(« modifie l'art. 2 de la loi 83-112 / clause d'exclusion ») ; l'exclusion des corps à statut
spécial est en réalité à l'**art. 1er** de la loi 83-112 (texte 1983), sans modification de 1991.
Plus aucune prose `.qmd` (FR/AR) ne cite `@loi91-62` (seule occurrence résiduelle : le fichier
généré `_glossaire.qmd`, régénéré au build depuis `precis/glossaire.yml` qui pointe désormais
`loi83-112` art. 1er — pas d'édition manuelle d'un fichier généré).

`decret-2022-797` (Décret n°2022-797 du 8 novembre 2022, programme/montants de l'augmentation
générale des salaires, années 2023-2024-2025) : **créé** FR + AR. Cité en B.1 (`_regime_indiciaire`).
Résolution `jort_cache.db` (recid 170029) : JORT n°120/2022.
- FR : `pdf_fr` = `https://www.pist.tn/jort/2022/2022F/Jo1202022.pdf`.
- AR : `pdf_ar` = `https://www.pist.tn/jort/2022/2022A/Ja1202022.pdf` (lu dans le champ, pas dérivé).
- **TODO objet AR** : l'objet du cache est en français ; titre AR = dénomination factuelle, à
  confirmer sur titre officiel JORT AR.

`loi-org-2018-29-ccl` (Loi organique n°2018-29 du 9 mai 2018, Code des collectivités locales) :
**créée** FR + AR. Citée en B.1 (`_regime_indiciaire`). Résolution `jort_cache.db` (recid 108664) :
JORT n°39/2018.
- **FR : pas d'URL** + **TODO URL FR** (`pdf_fr` VIDE/NULL dans le cache ; ne pas dériver `Ja→Jo`).
- AR : `pdf_ar` = `https://www.pist.tn/jort/2018/2018A/Ja0392018.pdf`. Objet AR officiel repris du
  cache (`يتعلق بمجلة الجماعات المحلية`) — pas de TODO objet AR.

`ugtt-pv-augmentation-2022` (PV d'accord UGTT–gouvernement sur l'augmentation des salaires
de la fonction publique et du secteur public, séance du 14 sept. 2022, publié le 16 sept. 2022) :
**créé** FR + AR. Cité en B.1 (`_regime_indiciaire`) comme source de **contexte** (dialogue
social), jamais opposable (opposabilité = `decret-2022-797`).
- URL page : `https://www.ugtt.org.tn/?p=7841`. Scans sources : `uploads/2022/09/01-1.jpg`,
  `02-1.jpg`, `03-1.jpg` (TLS UGTT non vérifiable → `curl -sk`).
- **PDF local** : `biblio_pdfs/ugtt_pv_augmentation_2022.pdf` (3 pages, assemblage des 3 scans ;
  dossier gitignoré). À joindre comme pièce jointe Zotero au rapatriement.
- Titre AR repris du titre du PV publié par l'UGTT (pas de rédaction AR à la main).
- Scans connexes **archivés mais NON cités** (pas d'entrée CSL créée — non opposables,
  pas de décret JORT) : `biblio_pdfs/ugtt_table_fp_2017_2018.pdf` (cycle FP 2017-2018,
  table désormais lisible — cf. note b1 §effort OCR) et
  `biblio_pdfs/ugtt_pv_secteur_public_2018.pdf` (PV secteur public 2017-2019, périmètre
  B.3). À ne créer en référence que si un décret JORT de mise en œuvre est identifié.

À rapatrier dans Zotero (provisoires, NE PAS pousser sans feu vert) : `decret-2022-797`,
`loi-org-2018-29-ccl` (FR + AR), `ugtt-pv-augmentation-2022` (FR + AR, + PDF joint). Livre
`remunerations_publiques` **toujours absent** de `COLLECTION_TO_BOOK` → collection Zotero dédiée
+ mapping, ou « Commun ».

### Apports « précis ajouts.docx » — passe du 26/08/2026 (B.1 et B.2)

15 entrées **créées à la main** FR + AR dans
`precis/{fr,ar}/remunerations_publiques/references.json`, toutes résolues au rendu
(`quarto render` FR et AR OK). **Aucune n'est encore dans Zotero.**

URLs JORT dérivées de `jort_cache.db` selon la règle par langue déjà posée plus haut
(FR = `Jo…` sous `<annee>F/`, AR = `Ja…` sous `<annee>A/`) ; le motif
`Jo<NNN><aa>.pdf` (avant 2000) / `Jo<NNN><aaaa>.pdf` (à partir de 2000) a été vérifié sur
quatre échantillons (1959, 1960, 1973, 2004).

#### Ancien régime indiciaire (nouvelle sous-section B.1)

| Clé | Référence | JORT |
|---|---|---|
| `decret-60-328` | Décret n°60-328 du 17 sept. 1960, classement hiérarchique et échelonnements indiciaires (cadres du secrétariat d'État à la santé publique) | n°44/1960, p. 1218-1221 |
| `decret-73-316` | Décret n°73-316 du 27 juin 1973, classement hiérarchique et échelonnement indiciaire des **agents temporaires** | n°25/1973, p. 1026-1027 |
| `decret-73-384` | Décret n°73-384 du 10 août 1973, statut du **personnel ouvrier** de l'État | n°31/1973 |
| `decret-75-353` | Décret n°75-353 du 3 juin 1975, fixant le **traitement global annuel** | n°38/1975 |
| `decret-79-93` | Décret n°79-93 du 11 janv. 1979, fixant le traitement global annuel | n°5/1979 |
| `decret-79-94` | Décret n°79-94 du 11 janv. 1979, modifiant le décret n°73-384 (ouvriers) | n°5/1979 |

Série « traitement global annuel » **incomplète** : les décrets n°77-122 (16 fév. 1977),
n°78-53 (25 janv. 1978), n°78-923 (23 oct. 1978) et n°80-128 (12 fév. 1980) sont identifiés
au JORT et cités dans le texte **sans clé CSL** (mention en toutes lettres). À créer si l'on
veut une chronologie citée pièce par pièce.

#### Bascule de 1997-1998 et statut général

| Clé | Référence | JORT |
|---|---|---|
| `decret-97-2127` | Décret n°97-2127 du 10 nov. 1997, **indemnités compensatrices** instituées par le décret n°97-1832 | n°93/1997, p. 2081 |
| `loi97-83` | Loi n°97-83 du 20 déc. 1997, modifiant la loi n°83-112 (art. 28 bis, 33, 37, 38) | n°103/1997 |
| `loi59-12` | Loi n°59-12 du 5 fév. 1959, **fixant le statut des fonctionnaires de l'État** | n°8/1959, p. 84-90 |

⚠ **Intitulé** : `loi59-12` s'intitule au JORT « *fixant le statut des fonctionnaires de
l'État* », et non « portant statut général des fonctionnaires » comme on le lit souvent.

#### Fondements transversaux

| Clé | Référence | JORT |
|---|---|---|
| `loi73-81` | Loi n°73-81 du 31 déc. 1973, promulguant le **Code de la comptabilité publique** | n°51/1973 |
| `loi2004-71` | Loi n°2004-71 du 2 août 2004, instituant le régime d'**assurance maladie** (CNAM) | n°63/2004, p. 2228-2230 |
| `loi95-56` | Loi n°95-56 du 28 juin 1995, régime particulier de réparation des **AT/MP dans le secteur public** | n°53/1995 |

`loi73-81` : le code est publié en entier dans le JORT n°51/1973 mais **éclaté en 26 notices**
dans le cache (une par titre/chapitre) ; l'URL retenue est celle du fascicule. Les articles 41
et 42 ont été **vérifiés sur la version consolidée du ministère des Finances**
(`https://www.finances.gov.tn/sites/default/files/2018-11/code_compta_fr.pdf`), mentionnée
dans le champ `note`.

#### Statuts autonomes (B.2)

| Clé | Référence | JORT |
|---|---|---|
| `decret-71-222` | Décret n°71-222 du 29 mai 1971, rémunération du personnel de la **Cour des comptes** | n°25/1971 |
| `decret-73-58` | Décret n°73-58 du 14 fév. 1973, indemnités servies au personnel du **Tribunal administratif** | n°7/1973 |

Chaînes de modification **citées en toutes lettres, sans clés CSL** (à créer si le chapitre
passe des structures aux montants) : solde militaire (n°87-878, 88-263, 88-909, 2002-1973,
2004-2127, 2005-3382, 2007-2408, 2010-2935) et **indemnité de magistrature** (n°2001-2125,
2001-2775, 2001-2776 ; 2009-2791, 2009-2792, 2009-2826 ; 2010-1749, 2010-1751, 2010-2521 ;
2012-3552, 2012-3553, 2012-3554 ; 2017-1361, 2017-1362, 2017-1364 ; 2018-73) — chacun à
vérifier sur `jort_cache.db` avant création.

#### Doctrine — entrée INCOMPLÈTE

`cherif-kammoun-tajir` : Salah Eddine Chérif & Maher Kammoun,
*سلسلة قانون الوظيفة العمومية في تونس، الجزء الرابع: نظام التأجير بالوظيفة العمومية*.
**Éditeur, année et ISBN manquants** — la couverture du scan fourni est illisible.
À compléter avant publication.

Rôle éditorial strict : cette référence sert uniquement à **attribuer** deux affirmations non
vérifiées sur source primaire — (a) l'ordre du 23 mai 1949 et ses articles 103 à 105
(indices 100-800, catégories A/B/C/D), (b) la date d'effet au 1^er^ janvier 1998 du décret
n°97-1832 et la publication des grilles en trois tableaux. Elle ne vaut jamais source
opposable.

⚠ **Erreur de la source à ne pas propager** : l'ouvrage date le décret n°97-1832 du
**10 novembre 1997**. La date exacte est le **16 septembre 1997** (JORT n°76, publié le
23 sept. 1997) — `decret-97-1832` est correct et ne doit pas être « corrigé ». L'erreur vient
probablement du lot d'application du 10 novembre 1997 (décrets n°97-2127 à 97-2134).

#### Contenu non lu — limite commune à ces entrées

**pist.tn est injoignable depuis l'environnement de rédaction** (`ECONNREFUSED` sur
164.160.2.73:443, comme gbo.tn). Sauf `loi73-81` et `loi97-83` (vérifiés sur versions
consolidées hors JORT), ces entrées reposent sur les **métadonnées** de `jort_cache.db`
— numéro, date, intitulé, fascicule, pagination — et **non** sur la lecture du texte.
Les intitulés sont donc fiables, les contenus ne le sont pas : aucun montant ni aucune
disposition n'est cité d'après elles.

À rapatrier dans Zotero (provisoires, NE PAS pousser sans feu vert) : les 15 clés ci-dessus.

#### Correctif 27/08/2026 — lecture sur corpus local, trois entrées ne sont plus « contenu non lu »

pist.tn est toujours injoignable, mais le dépôt **`~/projets/PDFs-legislation-tunisie`**
contient un corpus JORT converti en Markdown (`markdown_output/JORT/<année>/<langue>/`).
Trois fascicules y ont été lus intégralement — `1997/fr/Jo07697.md`, `1997/fr/Jo09397.md`,
`2007/fr/Jo0142007.md` —, ce qui met à jour les `note` CSL de **`decret-97-1832`**,
**`decret-97-2127`** et **`decret-2007-268`** : elles portent désormais le détail des
articles lus, et non plus la mention « contenu non lu ».

**Réflexe à retenir** : avant de conclure qu'un texte JORT est inaccessible, chercher dans
`markdown_output/JORT/` du dépôt de législation. La façade `uv run legislation search …` /
`uv run jort search …` (voir son `AGENTS.md`) indexe ce corpus et celui de l'IORT.

**Entrée créée** — `decret-1949-budget` : *Décret du 23 mai 1949, portant fixation du budget
de l'exercice 1949-1950*. **Sans URL ni numéro JORT** (le corpus ne remonte pas à 1949).
Le texte est identifié par le **visa du décret n°97-1832**, ce qui établit sur source
primaire son intitulé, sa nature budgétaire et son maintien en vigueur jusqu'en 1997 ; son
contenu (art. 103-105) reste attribué à `cherif-kammoun-tajir`.

**Portée de `cherif-kammoun-tajir` réduite** : la date d'effet au 1^er^ janvier 1998, la
structure en trois grilles et la nature budgétaire du texte de 1949 sont désormais primaires.
L'ouvrage ne sert plus qu'à attribuer le contenu des articles 103 à 105. Sa `note` a été
mise à jour en conséquence, avertissement sur l'erreur de date compris.

**À vérifier au prochain passage** : les fascicules portant les chaînes « indemnité de
magistrature » et « solde militaire » sont peut-être eux aussi dans le corpus local — cela
lèverait le blocage sur les chronologies chiffrées de B.2.

---

### Livre « Fiscalité », section IRPP — passe bibliographe 07/09/2026

Dix clés créées à la main dans **`precis/fr/fiscalite/references.json`** (aucune n'est
partagée : seul `precis/fr/fiscalite/index.qmd` les cite). Le livre `fiscalite` figure déjà
dans `COLLECTION_TO_BOOK` (collection Zotero « fiscalité ») : **à pousser dans cette
collection**, champ « Extra » = `citation-key: <clé>`. Tant que ce n'est pas fait, un
`sync_biblio.py` les écrase.

| Clé | Type CSL | Texte | JORT | URL |
|---|---|---|---|---|
| `lf-1986` | legislation | Loi n° 85-109 du 31/12/1985, LF 1986 (barème C.P.E., art. 8 p. 1731) | n° 91 du 31/12/1985, t. 128, la loi commence p. 1730 | `…/1985/1985F/Jo09185.pdf` |
| `code-irpp-is-1990` | legislation | Code IRPP-IS, texte annexé à la loi n° 89-114 (art. 44 p. 9) | n° 1 des 2-5/01/1990, t. 133, p. 3-21 | `…/1990/1990F/Jo00190.pdf` |
| `lf-1991` | legislation | Loi n° 90-111 du 31/12/1990, LF 1991 | n° 86 des 28-31/12/1990, t. 133, la loi commence p. 2049 | `…/1990/1990F/Jo08690.pdf` |
| `lf-1993` | legislation | Loi n° 92-122 du 29/12/1992, LF 1993 (art. 101, forfait) | n° 88 du 31/12/1992, t. 135, la loi commence p. 1668 | `…/1992/1992F/Jo08892.pdf` |
| `loi-98-73` | legislation | Loi n° 98-73 du 04/08/1998, simplification et réduction des taux | n° 64 du 11/08/1998, t. 141, p. 1736-1737 | `…/1998/1998F/Jo06498.pdf` |
| `lf-2014` | legislation | Loi n° 2013-54 du 30/12/2013, LF 2014 (art. 73 p. 3691) | n° 105 du 31/12/2013, t. 156, p. 3666-3832 | `…/2013/2013F/Jo1052013.pdf` |
| `lf-2017` | legislation | Loi n° 2016-78 du 17/12/2016, LF 2017 (art. 14 p. 3831) | n° 105 du 27/12/2016, p. 3829 | `…/2016/2016F/Jo1052016.pdf` |
| `lf-2025` | legislation | Loi n° 2024-48 du 09/12/2024, LF 2025 (art. 36 p. 6429) | n° 149 du 10/12/2024, t. 167, la loi commence p. 6418 | `…/2024/2024A/Ja1492024.pdf` |
| `lf-2026` | legislation | Loi n° 2025-17 du 12/12/2025, LF 2026 (art. 56 p. 4243 ; art. 91 p. 4254-4255) | n° 148 du 12/12/2025, t. 168, p. 4231-4331 | `…/2025/2025A/Ja1482025.pdf` |
| `dgi-nc-3-2017` | report | Note commune n° 3/2017 (commentaire de l'art. 14 de la LF 2017) | — | *pas d'URL à cette date — **périmé**, URL jibaya.tn trouvée le 07/09/2026, voir la passe « sous-section assiette et abattements » plus bas* |

Métadonnées vérifiées sur `jort_cache.db` (`~/projets/PDFs-legislation-tunisie`) : numéro,
type, date de signature, fascicule, tome, pagination, `pdf_fr`/`pdf_ar`. Les dix URL ont
été retestées en HTTP 200 le 07/09/2026 (`curl -skIL` — `www.pist.tn` a un **certificat TLS
expiré**, les clients stricts échouent à tort).

**Deux URL pointent volontairement sur l'édition arabe, ne pas « corriger » :**
- `lf-2025` : le champ `pdf_fr` de `jort_cache.db` est **vide** pour le JORT 149/2024 —
  l'édition française n'est pas référencée.
- `lf-2026` : `jort_cache.db` porte pourtant `pdf_fr = /jort/2025/2025F/Jo1482025.pdf`.
  Ce fichier a été téléchargé et ouvert le 07/09/2026 : **il sert le fascicule arabe**
  (l'édition française n'est pas parue). La justification est consignée dans le champ
  `note` de l'entrée.

**`code-irpp-is-1990` ≠ `loi-irpp-is-1989`** : `jort_cache.db` porte deux enregistrements
distincts pour la loi n° 89-114 — la promulgation (JORT n° 88 du 31/12/1989, t. 132,
p. 2142-2144, `Jo08889.pdf`, déjà en base sous `loi-irpp-is-1989`, dans le
`references.json` **partagé** car `remunerations_publiques` la cite) et le **code annexé**
(JORT n° 1 du 02/01/1990, `Jo00190.pdf`). Les deux clés doivent coexister dans Zotero.

#### Hygiène — fait

- Supprimé : entrée parasite de pièce jointe Zotero `23975222/K2B3EV4C`
  (`bastier_1997_fiscalite_coloniale.pdf`) dans `precis/fr/fiscalite/references.json` —
  la référence réelle `bastier1997` était bien présente.
- Supprimé : entrée parasite `23975222/DKA289MH` (`loi_2019_10_amen_social.pdf`) dans
  `precis/fr/references.json` — la référence réelle `loi-amen-social-2019` était bien présente.
- Ces deux pièces jointes doivent aussi cesser d'être exportées côté Zotero (elles
  reviendront au prochain `sync_biblio.py` si l'export inclut les attachments).

#### Reste à faire

- **`precis/ar/fiscalite/references.json` n'a pas été mis à jour** (hors périmètre de cette
  passe) : les dix clés y manquent. URL arabes à utiliser, lues dans le champ `pdf_ar` des
  mêmes enregistrements : `Ja09185`, `Ja00190`, `Ja08690`, `Ja08892`, `Ja06498`,
  `Ja1052013`, `Ja1052016`, `Ja1492024`, `Ja1482025` (chemins `…/<année>/<année>A/…`).
  Pour `dgi-nc-3-2017` : pas d'URL à cette date — **périmé**, voir la passe « sous-section
  assiette et abattements » plus bas (URL jibaya.tn trouvée le 07/09/2026).
- **`yaich`** : le millésime de l'édition citée manque (« Les impôts en Tunisie », ouvrage
  réédité annuellement). Non inventé — à relever sur l'exemplaire utilisé par le rédacteur,
  puis renseigner `issued` dans Zotero.
- **`dgi-nc-3-2017`** (**PÉRIMÉ — résolu plus bas, passe « sous-section assiette et
  abattements » : URL jibaya.tn trouvée et vérifiée le 07/09/2026**) : aucune URL pérenne
  identifiée sur le portail du ministère des
  finances ; l'entrée renvoie à la copie locale
  `PDFs-legislation-tunisie/PDFs/Notes_Communes/Note_Commune_numéro 3  …_2017_re.pdf`.
  À chercher côté `impots.finances.gov.tn` avant rapatriement.
- **`dgi-nc-14-2014`** (note commune n° 14/2014, modalités de détermination du seuil de
  5 000 D) : citée par la NC 3/2017, **document non consulté**, pas encore citée dans le
  précis — entrée non créée. À documenter si le rédacteur la cite.
- **`eset2016`** et **`lapresse2025`** ne sont plus cités dans le corps de la section IRPP.
  Conservées (`lapresse2025` est rattachée à un TODO « incidence » en cours).

---

### Livre « Fiscalité », sous-section « L'évolution de l'assiette et des abattements » — passe bibliographe 07/09/2026

**Vingt clés créées à la main dans `precis/fr/fiscalite/references.json`** (le livre rend
désormais sans aucune citation non résolue : 20 avertissements `Citeproc: citation … not
found` avant la passe, **0 après**). Elles sont **provisoires** tant qu'elles ne sont pas
dans Zotero (groupe 6529669, collection « fiscalité », mappée dans `COLLECTION_TO_BOOK`).

#### Textes législatifs — type CSL `legislation`

| Clé | Texte | JORT | Édition de l'URL | Page (édition française) |
|---|---|---|---|---|
| `lf-2005` | Loi n° 2004-90 du 31/12/2004, LF 2005 (art. 49 et 50) | n° 105 du 31/12/2004, t. 147 | **FR** `…/2004/2004F/Jo1052004.pdf` | 3440 |
| `lf-2007` | Loi n° 2006-85 du 25/12/2006, LF 2007 (art. 35) | n° 103 du 26/12/2006, t. 149 | **FR** `…/2006/2006F/Jo1032006.pdf` | **4387** |
| `lf-2010` | Loi n° 2009-71 du 21/12/2009, LF 2010 (art. 39 et 40) | n° 102 du 22/12/2009, t. 152 | **FR** `…/2009/2009F/Jo1022009.pdf` | 3919 |
| `lf-2016` | Loi n° 2015-53 du 25/12/2015, LF 2016 (art. 21) | n° 104 du 29/12/2015, t. 158 | **AR** `…/2015/2015A/Ja1042015.pdf` | **3143** |
| `lf-2018` | Loi n° 2017-66 du 18/12/2017, LF 2018 (art. 53, 54, 55) | n° 101 du 19/12/2017, t. 160 | **FR** `…/2017/2017F/Jo1012017.pdf` | **4289-4290** |
| `lf-2020` | Loi n° 2019-78 du 23/12/2019, LF 2020 (art. 41) | n° 104 du 27/12/2019, t. 162 | **AR** `…/2019/2019A/Ja1042019.pdf` | 4435 |
| `lf-2021` | Loi n° 2020-46 du 23/12/2020, LF 2021 (art. 16) | n° 128 du 25/12/2020, t. 163 | **FR** `…/2020/2020F/Jo1282020.pdf` | **3129** |
| `lf-2022` | Décret-loi n° 2021-21 du 28/12/2021, LF 2022 (art. 24) | n° 119 du 28/12/2021, t. 164 | **FR** `…/2021/2021F/Jo1192021.pdf` | 3086 |
| `lf-2023` | Décret-loi n° 2022-79 du 22/12/2022, LF 2023 (art. 43) | n° 141 du 23/12/2022, t. 165 | **AR** `…/2022/2022A/Ja1412022.pdf` | *non établie — voir ci-dessous* |
| `lf-2024` | Loi n° 2023-13 du 11/12/2023, LF 2024 (art. 34) | n° 144 du 12/12/2023, t. 166 | **AR** `…/2023/2023A/Ja1442023.pdf` | **3476** |
| `loi-avantages-fiscaux-2017` | Loi n° 2017-8 du 14/02/2017, refonte des avantages fiscaux (art. 2 § 6) | n° 15 du 21/02/2017, t. 160 | **FR** `…/2017/2017F/Jo0152017.pdf` | **778** |

#### Doctrine administrative (notes communes DGI) — type CSL `report`

Les neuf notes ont une **URL pérenne sur `jibaya.tn`** (portail de la DGI) : page
`https://jibaya.tn/docs/<slug>/`, renvoyant au PDF sous `wp-content/uploads/2024/02/`.
Les neuf PDF ont été téléchargés et leur **en-tête et objet contrôlés sur pièce** ; les
neuf **copies locales** correspondantes existent dans
`PDFs-legislation-tunisie/PDFs/Notes_Communes/` (nom de fichier exact consigné dans le
champ `note` de chaque entrée).

| Clé | Note commune | Texte commenté | Couche texte du PDF |
|---|---|---|---|
| `dgi-nc-33-2005` | n° 33/2005 | art. 50 LF 2005 (enfant infirme, 500 → 750 D) | oui |
| `dgi-nc-18-2007` | n° 18/2007 | art. 35 et 36 LF 2007 (pensions étrangères, 80 %) | oui |
| `dgi-nc-14-2010` | n° 14/2010 | art. 39 LF 2010 (intérêts de prêt logement social) | oui |
| `dgi-nc-16-2016` | n° 16/2016 | art. 21, 23 et 27 LF 2016 (revenus fonciers, 30 → 20 %) | oui |
| `dgi-nc-2-2017` | n° 2/2017 | art. 13 LF 2017 (intérêts de l'épargne) | **non** (lue à l'image) |
| `dgi-nc-7-2018` | n° 7/2018 | art. 54 et 55 LF 2018 (charges de famille, enfants infirmes) | oui |
| `dgi-nc-3-2020` | n° 3/2020 | art. 40 et 41 LF 2020 (parent à charge, 150 → 450 D) | **non** (lue à l'image) |
| `dgi-nc-1-2021` | n° 1/2021 | art. 16 LF 2021 (CEA, assurance-vie ; minimum d'impôt à 45 %) | **non** (lue à l'image) |
| `dgi-nc-1-2022` | n° 1/2022 | art. 24, 29 et 38 LF 2022 (intérêts de l'épargne) | oui |

#### Méthode de vérification appliquée (07/09/2026)

`www.pist.tn` a un **certificat TLS expiré** (`curl -k`). Un code 200 ne prouve rien : les
onze fascicules ont été **téléchargés et ouverts**, et pour chacun l'édition (mention
« TRADUCTION FRANÇAISE POUR INFORMATION » ou couverture arabe), le numéro, l'année (tome)
et la date de publication ont été relevés sur la page de couverture, puis la page de
l'article citée lue sur le pied de page de la page physique correspondante.

- Signature d'un 404 sur ce serveur : `404 text/html; charset=iso-8859-1 289` (289 octets
  de HTML, pas un PDF). **Le champ `pdf_fr` de `jort_cache.db` ne prouve pas l'existence
  du fichier** : `…/2022/2022F/Jo1412022.pdf` y figure pour d'autres textes du fascicule
  n° 141/2022 et renvoie pourtant un 404.
- Le fascicule `Jo1052004.pdf` a une couche texte à encodage de police décalé qui
  **n'expose pas les chiffres** : la pagination y a été lue à l'image (rendu du pied de
  page, « Page 3440 — Journal Officiel de la République Tunisienne — 31 décembre 2004 —
  N° 105 »).
- Pour les fascicules français absents en ligne, la **pagination française** a été relevée
  sur les extraits du JORT français conservés dans
  `PDFs-legislation-tunisie/PDFs/Lois_de_Finances/` (pieds de page français intacts).

#### Cinq corrections de pagination au § 11.2 de `docs/notes/fiscalite-irpp-assiette-abattements.md`

Établies sur pièce, consignées dans le champ `note` des entrées concernées. La note
documentaire n'a pas été modifiée (hors périmètre) : à corriger là-bas si elle doit
continuer à servir de source.

| Clé | § 11.2 | Valeur établie |
|---|---|---|
| `lf-2007` | ~4386 | **4387** |
| `loi-avantages-fiscaux-2017` | 777 | **778** |
| `lf-2024` | 3475 | **3476** |
| `lf-2016` | 3142-3143 | **3143** (l'article 21 tient sur une page) |
| `lf-2021` | 3128-3129 | **3129** (l'article 16 tient sur une page) |
| `lf-2018` | art. 54 et 55 tous deux p. 4289 | art. 53 et 54 p. **4289**, art. 55 p. **4290** |

#### Cinq éditions françaises confirmées absentes de pist.tn — URL arabe assumée

`Jo1042015`, `Jo1042019`, `Jo1442023`, `Jo1492024` et `Jo1412022` renvoient tous un
**404** (signature `text/html`, 289 octets). Les entrées `lf-2016`, `lf-2020`, `lf-2023`,
`lf-2024` (et, déjà en base, `lf-2025`) pointent donc sur l'**édition arabe**, tandis que
le champ `page` porte la **pagination française**. Les deux paginations coexistent et sont
l'une et l'autre exactes ; chaque `note` le dit explicitement. **Ne pas « corriger » ces
URL vers une adresse en `…F/Jo…`, ni la pagination vers la pagination arabe.** Pages de
début en pagination arabe, pour mémoire : 3597 (`lf-2016`), 4699 (`lf-2020`), 4059
(`lf-2023`), 6437 (`lf-2024`).

#### Reste à faire

- **`lf-2023` — pagination française non établie.** Le numéro et la date du fascicule sont
  désormais **acquis** (JORT n° 141 du 23/12/2022, t. 165, sommaire arabe vérifié + notice
  `jort_cache.db`), ce qui lève la réserve principale du § 11.2. Mais le fascicule français
  est absent en ligne et la copie locale
  `PDFs-legislation-tunisie/PDFs/Lois_de_Finances/Loi_de_Finances_2023.pdf` est
  **illisible** (« Couldn't read xref table »). L'entrée est donc **sans champ `page`**, et
  sa `note` le dit. À reprendre si une source française du fascicule apparaît.
- **`precis/ar/fiscalite/references.json` n'a pas été mis à jour** (hors périmètre de la
  commande) : les vingt clés y manquent. URL arabes à utiliser, lues dans le champ `pdf_ar`
  des mêmes enregistrements de `jort_cache.db` (ne jamais déduire l'URL AR en transformant
  la chaîne FR) : `Ja1052004`, `Ja1032006`, `Ja1022009`, `Ja1042015`, `Ja1012017`,
  `Ja1042019`, `Ja1282020`, `Ja1192021`, `Ja1412022`, `Ja1442023`, `Ja0152017`
  (chemins `…/<année>/<année>A/…`). Pour les neuf notes communes, l'URL `jibaya.tn` est la
  même dans les deux langues (jibaya.tn a un miroir arabe `/ar/`, non vérifié).
- **`dgi-nc-3-2017` — URL pérenne trouvée et RENSEIGNÉE (TODO levé).** Le PDF
  `https://jibaya.tn/wp-content/uploads/2024/02/Note-Commune-n%C2%B003-5.pdf` a été
  téléchargé et lu à l'image : en-tête « NOTE COMMUNE N° 3/2017 », objet conforme
  (article 14 de la LF 2017), cachet du 24 janvier 2017. L'entrée existante a été complétée
  par l'URL de la page jibaya.tn correspondante ; **à reporter dans Zotero**. Quirk à
  connaître : le slug de cette page mentionne à tort « larticle-13 » (collision avec la
  note commune n° 2/2017), mais le titre de la page et le PDF servi sont bien ceux de la
  note commune n° 3/2017.
- **Huit lois de finances citées en prose sans clé** dans `precis/fr/fiscalite/index.qmd`
  (liste conservée dans le commentaire de fin de fichier), hors périmètre de cette passe :
  loi n° 91-98 (LF 1992), n° 97-88 (LF 1998), n° 98-111 (LF 1999), n° 2001-123 (LF 2002),
  n° 2002-101 (LF 2003), n° 2003-80 (LF 2004), n° 2007-70 (LF 2008), n° 2010-58 (LF 2011).
  À créer si le précis doit les citer formellement.

#### À pousser dans Zotero — NE PAS pousser sans feu vert

Les vingt clés ci-dessus, collection « fiscalité » (mappée `fiscalite` dans
`COLLECTION_TO_BOOK`), champ « Extra » : `citation-key: <clé>`. Aucune écriture Zotero
n'a été effectuée.

---

### Livre « Prestations sociales » — 63 clés (8 septembre 2026)

Ajoutées ou déplacées à la main pour que le chapitre « Prestations sociales » rende sans
citation non résolue (une clé non résolue s'affiche **en gras dans le corps du texte**, pas
en `[?]` : le contrôle utile est l'absence d'avertissement `Citeproc: citation … not found`
au rendu, et la présence d'une ancre `#ref-<clé>` pour chaque clé citée). **Aucune écriture
Zotero n'a été effectuée.**

Métadonnées reprises du §12.2 de `docs/notes/prestations-contributif.md` et du §8.2 de
`docs/notes/prestations-assistance.md`. Toutes les URL sont des fascicules JORT pist.tn
**vérifiés par téléchargement** (`curl -k`, certificat expiré). Les 59 entrées pointent
**52 fascicules distincts** (sept fascicules portent deux textes ou plus : JORT 33/1988,
14/1988, 84/2012, 45/2020 — quatre textes —, 38/2022). Tous répondent 200 en `application/pdf`,
aucun n'est le corps HTML de 289 octets du 404, et **l'édition française est confirmée sur le
contenu** : couche texte en caractères latins pour 30 fascicules, océrisation de la première
page (`pdftoppm` + `tesseract -l fra`) pour les 22 autres (scannés d'avant 1994, plus les JORT
2002 et 2005 dont la couche texte est défectueuse, cf. §5 de
`docs/notes/outillage-sources.md`).

#### a) 59 clés créées dans `precis/fr/prestations_sociales/references.json`

Collection Zotero cible : **à créer** pour `prestations_sociales` (voir réserve ci-dessous),
sinon « Commun ». Champ « Extra » : `citation-key: <clé>`.

*Bloc contributif (28)* : `loi57-73`, `loi72-2`, `loi74-41`, `decret74-463`, `loi75-82`,
`loi80-36`, `loi81-6`, `loi86-75`, `loi86-86`, `loi88-38`, `loi88-39`, `loi89-73`,
`decret89-107`, `decret93-308`, `loi94-28`, `loi94-88`, `decret95-114`, `decret95-1166`,
`loi96-65`, `loi96-101`, `decret96-1906`, `loi97-58`, `loi98-91`, `loi2002-32`, `loi2002-104`,
`decret2007-1366`, `loi2024-44`, `decret-loi2024-4`.

*Bloc assistance (31)* : `loi-86-83-lfr-1986`, `arrete-1987-01-06-financement-pnafn`,
`loi-87-29-amg`, `loi-87-83-lf-1988`, `decret-88-175-livrets-amg`,
`arrete-1988-02-17-droit-affiliation-amg`, `loi-90-111-lf-1991`,
`arrete-1997-09-30-personnes-agees`, `decret-98-409-amg2`, `decret-98-1812-amg1`,
`decret-2005-2886-amg2-ascendants`, `decret-2012-2521-amg1-pnafn`,
`decret-2012-2522-amg2-commissions`, `decret-2014-1526-banque-donnees`,
`decret-gouv-2020-317-amen`, `arrete-2020-05-19-scoring`, `arrete-2020-05-19-transferts`,
`arrete-2020-05-19-appui-occasionnel`, `arrete-2021-08-20-aides-covid`,
`decret-loi-2022-8-allocation-familiale`, `arrete-2022-04-01-transferts`,
`arrete-2022-04-01-allocation-familiale`, `decret-2022-715-autonomisation`,
`decret-2022-919-soins-amen`, `arrete-2022-12-08-appui-occasionnel`,
`arrete-2023-04-03-transferts`, `arrete-2024-02-28-transferts`,
`arrete-2024-07-10-allocation-pauvres`, `arrete-2025-01-29-transferts`,
`arrete-2025-07-30-gluten`, `arrete-2025-08-29-allocation-pauvres`.

#### b) 4 clés promues dans la bibliographie partagée `precis/fr/references.json`

`loi60-30`, `loi2004-71`, `loi95-56` (retirées de
`precis/fr/remunerations_publiques/references.json`) et `lf-2025` (retirée de
`precis/fr/fiscalite/references.json`). Ces quatre textes fondateurs servent plusieurs livres ;
**ne pas les dupliquer**. Collection Zotero cible : **Commun**. Les quatre livres chargent
`../references.json` et rendent sans citation non résolue après l'opération (vérifié).

Corrections portées au passage, à répercuter dans Zotero : `loi60-30` — pp. 1602-1613, articles
51-67 (prestations familiales) et 68-98 (assurances sociales) ; `loi2004-71` et `loi95-56` —
mention « contenu non lu » retirée (textes dépouillés depuis) et date d'effet du 1er janvier
1996 (art. 58) ajoutée à `loi95-56` ; `lf-2025` — renvoi à l'article 17 (pp. 6420-6421 de
l'**édition arabe**), l'avertissement sur les deux paginations restant intact.

#### c) Entrée existante complétée, sans doublon

`loi-amen-social-2019` (`precis/fr/references.json`) reçoit les métadonnées de l'entrée
candidate `loi-org-2019-10-amen` du dossier assistance : JORT n° 11 du 5 février 2019,
pp. 277-279, `event-date` = 30 janvier 2019. La clé `loi-org-2019-10-amen` **n'a pas été
créée** : le chapitre cite `loi-amen-social-2019`.

#### Reste à faire

- **Collection Zotero manquante.** `prestations_sociales` n'est pas dans `COLLECTION_TO_BOOK`
  de `scripts/sync_biblio.py` — même réserve que `remunerations_publiques` ci-dessus. Créer une
  collection Zotero dédiée et l'ajouter au mapping, ou ranger les 59 items en « Commun ».
  Tant que rien n'est monté dans Zotero, **le prochain sync écrasera ces 63 clés**.
- **`precis/ar/prestations_sociales/references.json` n'a pas été alimenté** (hors périmètre de
  la commande) : les 63 entrées y manquent. URL arabes à lire dans le champ `pdf_ar` des
  **mêmes** enregistrements de `jort_cache.db` — ne jamais déduire l'URL AR en transformant la
  chaîne FR. Cas particulier : `lf-2025` pointe déjà l'édition arabe (`Ja1492024`), l'édition
  française du JORT n° 149/2024 étant absente en ligne.
- ~~**`circulaire-42-1996` non créée.**~~ **Créée le 11 septembre 2026** dans la bibliographie
  partagée, sur l'entrée CSL du § 9 du dossier retraites (voir « Livre « Retraites » — passe
  bibliographe du 11 septembre 2026 »). Elle reste **non lue** et **non citée** : métadonnées
  seules (JORT n° 94 du 22 novembre 1996, pp. 2349-2364, recid 46979).
- **`loi2017-66-lf2018` non résolue dans le livre « fiscalité »** — anomalie **préexistante**,
  sans rapport avec la promotion des quatre clés : la clé est citée par
  `precis/fr/fiscalite/_glossaire.qmd` (fichier **généré**, non modifiable à la main) et
  n'existe dans aucune bibliographie. À corriger côté `precis/glossaire.yml` ou en créant
  l'entrée (loi n° 2017-66 du 18 décembre 2017, loi de finances pour 2018).
- **`unicef2020`** est désormais citée pour la première fois ; la pièce jointe Zotero
  résiduelle `23975222/EZEBV8GK` a été **retirée** de
  `precis/fr/prestations_sociales/references.json`.

#### Deux divergences de convention entre les deux blocs — à NE PAS « harmoniser » à l'aveugle

- **Nature de la date.** Le bloc contributif porte `issued` = **date de signature** du texte et
  pas d'`event-date` ; le bloc assistance porte `issued` = **date de publication relevée sur le
  pied de page du fascicule** et `event-date` = date de signature. Les deux blocs sont
  internement cohérents et aucune année ne bascule, mais des entrées voisines de la
  bibliographie afficheront des dates de nature différente. Trancher avant la montée dans
  Zotero.
- **Sens du champ `page`.** Le §8.2 du dossier assistance définit `page` comme « page du
  fascicule ». Pour les lois de finances, la page portée est celle de la **disposition citée**
  et non celle du début de la loi : `loi-90-111-lf-1991` porte 2056 (articles 65-66) alors que
  le sommaire du fascicule annonce la loi p. 2040 ; même configuration probable pour
  `loi-86-83-lfr-1986` (art. 13, p. 928) et `loi-87-83-lf-1988` (art. 62 à 67, pp. 1633-1634).
  Ce n'est pas une erreur, mais la convention doit être explicitée dans Zotero.

#### À pousser dans Zotero — NE PAS pousser sans feu vert

Les 63 clés ci-dessus (59 en collection « prestations sociales » à créer, 4 en « Commun »),
champ « Extra » : `citation-key: <clé>`. Aucune écriture Zotero n'a été effectuée.

## Livre « Cotisations sociales » — collection Zotero à créer

Le cinquième livre a été ouvert sans collection Zotero. En conséquence,
`scripts/sync_biblio.py` ne lui écrit rien, et les deux entrées que cite son annexe
glossaire ont été **copiées à la main** dans `precis/{fr,ar}/cotisations_sociales/references.json`
depuis les livres qui les portaient déjà :

- `decret-2017-668-smig` — venait de la collection « Fiscalité » ;
- `loi85-12` — venait de la collection « Rémunérations publiques ».

Ces deux textes sont désormais cités par trois livres. **À faire dans Zotero** : créer la
collection « Cotisations sociales » et y ajouter ces deux items — un item peut appartenir à
plusieurs collections, il n'y a donc rien à déplacer. Le mapping
`COLLECTION_TO_BOOK["cotisations sociales"]` est déjà en place côté script : la collection
créée, la synchronisation reprendra la main sur ce fichier et la copie manuelle disparaîtra.

Les références qu'ont rapportées les dossiers documentaires des régimes (privé et public)
s'ajoutent à cette même collection : elles sont listées à la sous-section suivante.

### Versement des dossiers documentaires (privé et public) — fait localement, à rapatrier

Les deux dossiers `docs/notes/cotisations-dossier-prive.md` (§ 12) et
`docs/notes/cotisations-dossier-public.md` (§ « Références candidates ») ont été versés dans
`precis/{fr,ar}/cotisations_sociales/references.json`, qui compte désormais **41 entrées**.
Toutes sont provisoires au sens du § *Rappel de procédure* : sans collection Zotero
« Cotisations sociales », `scripts/sync_biblio.py` ne les gouverne pas.

**30 clés créées** (aucune n'existait ailleurs dans le dépôt) :

`arrete-1978-11-18-retraite-complementaire`, `decret2002-916`, `decret2003-894`,
`decret2003-1212`, `decret2003-1544`, `decret2007-1406`, `decret2014-2919`, `decret73-91`,
`decret74-499`, `decret81-224`, `decret92-631`, `decret94-1429`, `decret95-538`,
`decret97-555`, `decret97-1645`, `decretloi2011-48`, `loi59-18`, `loi59-19`, `loi59-45`,
`loi73-71`, `loi74-101-lf1975`, `loi83-31`, `loi85-16`, `loi88-16`, `loi94-71`, `loi97-4`,
`loi2001-123-lf2002`, `loi2005-54`, `loi2007-43`, `loi2007-51`.
(23/09/2026 : `loi97-4` a depuis été promue au fonds commun, citée aussi par « Retraites ».)

**8 clés recopiées** depuis un autre livre, parce que sa bibliographie ne figure pas dans le
`_quarto.yml` de celui-ci — l'item Zotero existe déjà, il suffira de l'ajouter à la collection
« Cotisations sociales » : `loi75-83`, `loi81-6`, `loi89-73`, `loi96-101`, `loi2002-32`,
`loi2002-104`, `decret89-107`, `decret95-1166` (collection « Prestations sociales ») et
`loi2019-37` (collection « Rémunérations publiques »).

**2 clés déjà présentes** : `decret-2017-668-smig` et `loi85-12` (voir ci-dessus). `loi85-12` a
été **complétée** — `container-title`, `issue: 20`, `page: 359-365`, note enrichie (art. 9, 13
et 76) : la correction est à reporter sur l'item Zotero, qui vient de « Rémunérations
publiques ».

**Non recopiées, et à laisser telles quelles** : `loi60-30`, `loi2004-71` et `lf-2025` vivent
dans `precis/{fr,ar}/references.json` (« Commun »), qui **est** sur le chemin de bibliographie
du livre. Les dupliquer localement créerait un `id` en double dans la bibliographie fusionnée.

Points de forme pour la montée dans Zotero :

- type d'item Zotero **Statute** (→ CSL `legislation`) ;
- champ **Extra** : `citation-key: <clé>` **et** `issue: <n° de fascicule>` — le type Statute
  n'a pas de champ Issue, et `apply_extra_variables()` le réinjecte à la descente ;
- l'URL déposée dans Zotero est celle de l'**édition française** ; la descente dérive l'arabe.
  Les 40 dérivations FR→AR de ce livre ont été contrôlées **par comparaison de taille** contre
  pist.tn : toutes servent bien deux fichiers distincts.

#### Deux corrections faites en marge, hors collection « Cotisations sociales »

- `precis/urls-jort.json` : ajout de `https://www.pist.tn/jort/2017/2017F/Jo0452017.pdf`. Les
  deux chemins de ce fascicule servent le **même** fichier de 1 217 842 octets (mesuré) ; sans
  cette exception, la descente fabriquerait pour l'arabe un lien qui répond 200 en servant le
  français. C'est le fascicule de `decret-2017-668-smig`, cité par trois livres.
- `precis/{fr,ar}/references.json`, `loi60-30` (« Commun ») : la note portait « JORT n° 57 des
  16-20 décembre 1960 ». Le fascicule porte en en-tête « 13-16 décembre 1960 » et
  `jort_cache.db` donne `date_publication = 1960-12-13`. Corrigé en « fascicule daté 13-16
  décembre 1960 ». **À reporter sur l'item Zotero de la collection « Commun ».**

#### Restent à vérifier avant d'être cités dans le texte

- `decretloi2011-48` — métadonnées `jort_cache.db` (recid 80629), **contenu non lu** ; porte le
  palier employeur de juillet 2011 dans openfisca-tunisia.
- `loi59-45` (recid 118145) et `loi2005-54` (recid 110642) — métadonnées seules, contenu non lu.
- ~~`loi85-16` — le libellé de la contribution de l'État reste à relire à l'image.~~ **Levé le
  11 septembre 2026** : art. 5 relu à 400 dpi, contribution de l'État de 15 % lisible (voir la
  section « Retraites » ci-dessous).
- `loi73-71` — `issued` retenu au **19 novembre 1973** (fascicule, lu à l'image) contre le
  16 novembre de `jort_cache.db` ; divergence consignée dans la note de l'entrée.

### Trois des cinq entrées « à vérifier avant citation » sont désormais citées

Le versement des références du livre « Cotisations sociales » signalait cinq entrées dont le
contenu n'avait pas été lu : `decretloi2011-48`, `loi59-45`, `loi2005-54`, `loi85-16` et
`loi73-71`. La rédaction de la section du secteur public en cite trois. État exact :

- `loi73-71` — **lue** au fascicule (JORT n° 43 de 1973, p. 1852, lecture à l'image) : l'article
  premier remplace l'article 5 de la loi 59-18 en maintenant le taux à 7 %. Rien à vérifier.
- `loi59-45` — **non ouverte**, mais le fait qu'elle porte (la création de la Caisse de prévoyance
  sociale) est attesté par un texte lu : l'article 28 de la loi n° 75-83 la nomme expressément.
  L'attestation est donc indirecte et suffisante pour ce que le chapitre en dit.
- `loi85-16` — article 5 **partiellement lu** : la retenue de 10 % est établie, la mention de la
  contribution de l'État de 15 % est illisible sur le fascicule océrisé. Le chapitre le dit
  désormais explicitement plutôt que d'étendre aux trois lois ce qui n'est établi que pour deux.
  **Mise à jour du 11 septembre 2026** : la mention est lisible à 400 dpi — « une contribution de
  l'Etat égale à 15 % de ces mêmes indemnités prélevée sur le budget de la Chambre des Députés ».
  La phrase de `precis/fr/cotisations_sociales/index.qmd` (l. 433) qui la dit illisible est donc
  **dépassée** : à reprendre par le rédacteur (pas par le bibliographe).

`decretloi2011-48` et `loi2005-54` ne sont pas citées ; elles restent à vérifier avant de l'être.

### ✅ Fait le 9 septembre 2026 — la montée est effectuée

Les 41 références du livre « Cotisations sociales » sont dans Zotero, et la collection du
même nom a été créée par `push_biblio.py --ranger`. Déroulé, par le workflow
`biblio-zotero` :

1. `verifier` — aller-retour de conversion hors ligne : 198 entrées, aucune perte de champ.
2. `dry-run` — 198 références locales, 30 à créer.
3. `pousser-un` puis `comparer` — une seule référence montée
   (`arrete-1978-11-18-retraite-complementaire`, article `XNATUX5Z`), relue dans Zotero :
   **0 écart après aller-retour réel**, champ Extra compris. C'est ce test à l'unité qui
   avait révélé, à la montée précédente, que l'export CSL de l'API laisse tomber les
   variables du champ Extra.
4. `pousser-tout` — 29 créées, 0 en échec.
5. `ranger` — collection « Cotisations sociales » créée, 41 articles classés, 0 en échec.
6. `descendre` — et c'est là qu'un écart est apparu : **`loi85-12` perdait
   `container-title`, `issue` et `page`**. L'entrée existait déjà dans Zotero au titre du
   livre « Rémunérations publiques », et l'enrichissement fait en local n'était donc jamais
   monté : la descente l'aurait écrasé. Réparé par `corriger loi85-12`.
7. `descendre` à nouveau — **198 clés en local, 198 après descente, aucun champ perdu,
   aucune valeur changée.**

**La leçon, pour la prochaine fois.** `pousser` ne crée que les clés absentes : une entrée
déjà présente dans Zotero mais **enrichie en local** passe entre les mailles, et seule la
descente le révèle. Après toute montée, dérouler `descendre` et comparer clé par clé et
champ par champ — un diff de lignes ne suffit pas, celui-ci comptait 1 062 suppressions
pour 1 056 ajouts alors que six lignes seulement étaient en cause.

Le diff que produit la descente est par ailleurs du réordonnancement : les fichiers locaux
sont identiques en contenu et n'ont pas été récrits.

## Livre « Retraites » — passe bibliographe du 11 septembre 2026

Source : `docs/notes/retraites-dossier.md` (10 septembre 2026), entrées CSL-JSON des § 9 et
§ 10.4, plus les textes que le corps du dossier cite sans leur donner d'entrée. Tout est versé
dans la bibliographie **partagée** `precis/{fr,ar}/references.json` (80 entrées par langue,
contre 14), sur instruction : ces textes servent le livre « Retraites » et, pour beaucoup, les
livres « Cotisations sociales », « Prestations sociales » et « Rémunérations publiques ».
**Aucune écriture Zotero n'a été effectuée.**

URL : FR = `pdf_fr`, AR = `pdf_ar`, lus sur le **même** enregistrement de `jort_cache.db`
(recid ci-dessous) par un script unique qui écrit les deux langues. Tous les enregistrements
portent les deux champs. Les 47 URL `legislation` du dossier concordent avec `pdf_fr`, et ses
n° de fascicule et dates de signature avec la notice.

### a) 42 clés créées (partagé FR + AR)

Clés du dossier renommées à la convention du dépôt (`tn-decret-1979-536` → `decret79-536`,
`tn-loi-2009-20` → `loi2009-20`…). **Les identifiants `tn-…` du dossier ne sont pas des clés :
ne pas les citer.**

| Clé | recid | Niveau (dossier) |
|---|---|---|
| `decret79-536` | 99253 | [T] |
| `decret79-510` | 99274 | [M] |
| `decret81-187` | 98356 | [T] |
| `decret81-188` | 98357 | [T] |
| `loi81-70` | 115268 | [T] art. 4-5 |
| `decret82-1030` | 97385 | [T] |
| `decret85-1177` | 95684 | [T] |
| `decret85-1178` | 95685 | [T] |
| `decret86-611` | 95353 | [T] |
| `decret88-1136` | 94346 | [T] |
| `decret88-1137` | 94347 | [T] |
| `decret90-1455` | 93242 | [T] |
| `decret96-326` | 90575 | [T] (dossier cotisations) — hors § 9, créée ici |
| `decret97-291` | 90103 | [T] (dossier cotisations) — hors § 9, créée ici |
| `decret97-1927` | 89803 | [T] art. 33 nouveau |
| `decret2001-779` | 87591 | [T] |
| `decret2007-2148` | 83291 | [T] |
| `decret81-939` | 98073 | [M] |
| `decret82-971` | 97403 | [M] |
| `decret83-737` | 96876 | [M] |
| `decret75-952` | 101344 | [M] |
| `arrete-1998-07-29-revalorisation-rtns` | 59879 | [M] |
| `circulaire-42-1996` | 46979 | [M] (clé déjà proposée § « Prestations sociales ») |
| `loi2009-20` | 109760 | [T] |
| `loi60-33` | 117856 | [M] — hors § 9, créée ici (voir d) |
| `loi88-71` | 113976 | [M] |
| `loi90-6` | 113646 | [M] |
| `loi96-67` | 112417 | [M] (homonyme du 29 juillet 1996 : ne pas confondre) |
| `loi97-74` | 112234 | [M] |
| `loi2002-61` | 111264 | [M] |
| `loi87-7` | 114257 | [M] |
| `loi87-8` | 114258 | [M] |
| `loi2009-39` | 109727 | [M] |
| `loi88-84` | 113960 | [M] |
| `loi2003-8` | 111156 | [M] |
| `decret2003-1128` | 86249 | [M] |
| `loi95-105` | 112519 | [M] |
| `loi88-101` | 113942 | [M] |
| `decret85-980` | 95742 | [M] |
| `decret85-1176` | 95683 | [M] |
| `decret74-572` | 102263 | [M] |
| `cnrps-manuel-liquidation-2013` | — | document interne non normatif, type `report` |

### b) 24 clés promues d'un livre vers le partagé (retirées du fichier de livre, FR et AR)

Copies FR et AR vérifiées identiques entre livres avant fusion ; contenu inchangé.

- depuis `cotisations_sociales` : `loi81-6`, `loi89-73`, `loi2002-32`, `decret89-107`,
  `decret95-1166`, `loi2002-104` (ces six aussi depuis `prestations_sociales`), `loi83-31`,
  `loi85-16`, `loi88-16`, `decret81-224`, `decret94-1429`, `decret97-555`, `decret2003-1212`,
  `decret2003-894`, `arrete-1978-11-18-retraite-complementaire`, `loi94-71`, `loi2005-54` ;
- depuis `prestations_sociales` : `decret93-308`, `decret96-1906`, `loi88-39`, `loi94-28` ;
- depuis `remunerations_publiques` : `decret85-1025`, `loi98-37`, `decret98-1981` (titres
  arabes conservés côté AR).

Entrées du dossier absorbées par une clé existante (pas de doublon) : `tn-loi-1981-6`,
`tn-loi-1989-73`, `tn-loi-2002-32`, `tn-decret-1981-224`, `tn-decret-1996-1906`,
`tn-loi-1988-39`, `tn-loi-2005-54`, `tn-decret-1985-1025`, `tn-loi-1998-37`.

Non promues, faute d'usage par le dossier : `loi2001-123-lf2002` (ligne § 10.2 sans données
JORT) et `loi96-101`.

### c) Entrées existantes corrigées — À REPORTER DANS ZOTERO (la montée ne crée que les absentes)

- `decret74-499` : la note affirmait « sans article d'entrée en vigueur » — **faux** : l'art. 64
  (lu à l'image) le fait prendre effet au **1er janvier 1974**. Fascicule corrigé en « n° 30,
  30 avril - 3-4 mai 1974 » (publication 1974-04-30 selon `jort_cache.db`, et non « 3 mai ») ;
  articles lus et rectificatif (JORT n° 39 du 7 juin 1974, p. 1252, recid 102251, non lu) ajoutés.
- `loi2019-37` : entrée nue complétée — `container-title`, `issue: 35`, `page: 1312-1315`, note
  (art. 1, 3, 5, 7 ; aucune clause d'entrée en vigueur).
- `loi85-12` : note complétée de l'art. 75 (effet au 12 septembre 1985).
- `precis/{fr,ar}/references.bib` : définition `@book{sdiri2014}` **supprimée** ; la clé reste
  définie une seule fois, dans `precis/{fr,ar}/retraites/references.json` (collection
  « Retraites »). Reste dans les deux `.bib` l'entrée `loi2016` (loi française « République
  numérique », gabarit), citée par aucun `.qmd` : à supprimer sur décision.

### d) Écarts entre le dossier, `jort_cache.db` et les fascicules

- `loi60-33` : créée parce que le dossier la documente (§ 2.0 : n° 57, p. 1616, objet) et que la
  notice le confirme. Métadonnées seules. La note précise qu'elle **ne porte pas** le barème du
  RSNA (décret n° 74-499, art. 17).
- `loi81-70` : `page` = étendue de la loi (1789-1798, notices article par article) ; les art. 4-5
  lus sont aux pp. 1789-1790 (§ 1.0), ce que dit la note. Convention retenue : étendue du texte
  en `page`, articles en note.
- `decret90-1455` : la notice JORT (« relatif au régime de vieillesse… ») omet la mention
  « amendant le décret n° 74-499 ». Tranché sur le fascicule (OCR `tesseract -l fra`) : l'intitulé
  du texte, p. 1358, porte « **amendant** le décret N° 74-499 » (intitulé du § 9 du dossier,
  retenu) ; le sommaire porte « modifiant ». C'est la notice qui est fautive.
- `loi85-16` : note corrigée — l'art. 5 a été relu à 400 dpi, la contribution de l'État de 15 %
  est lisible ; la réserve « à relire à l'image » est levée (conforme au § 4.2 du dossier).
- `loi60-33` : note alignée sur `loi60-30` (« fascicule daté 13-16 décembre 1960 »). Les visas du
  décret n° 90-1455 la citent avec « régime d'allocations » (pluriel), la notice avec
  « allocation » : intitulé de la notice conservé.
- `loi83-31` : dossier pp. 807-809, notice et entrée 808-809. Non modifié ; dernière page non lue.
- `loi2007-43` : entrée 2197-2199 ; notice et dossier 2198-2199 ; sommaire du fascicule 2198.
  Le pied de page du fascicule local (`2007/fr/Jo0512007.pdf`) montre que l'intitulé commence
  **en bas de la p. 2197** : l'entrée est juste, la notice et le sommaire donnent la page de
  l'article premier.
- `loi75-83` : entrée 2852-2854, notices 2852-2853. Non modifié.
- `circulaire-42-1996` : date de publication (22 novembre 1996) ajoutée depuis la notice.

### e) Sans URL

- `cnrps-manuel-liquidation-2013` : document interne de la CNRPS, aucune URL publique connue ;
  exemplaire local seulement. **TODO** : chercher une diffusion publique (cnrps.nat.tn) avant de
  lui en donner une.

Toutes les autres entrées créées ou promues ont une URL pist.tn en FR et en AR.

### f) Textes nommés par le dossier, volontairement sans clé

Rectificatifs du décret n° 74-499, du décret n° 82-1030 (JORT n° 66/1982, p. 2197) et de la loi
n° 81-6 (JORT n° 26/1981, p. 844) : portés en note de l'entrée principale. Décret n° 71-432
(abrogé, sans données JORT), décrets du 2 février et du 8 juin 1944 (hors `jort_cache.db`), loi
n° 81-46, décrets n° 87-337, 91-604, 96-1015 (clé créée depuis, voir la passe « chaîne 85-12 » ci-dessous), 2003-1656, 2009-2085, loi n° 88-145, décret-loi
n° 74-22, loi n° 77-57, décrets de classement des cadres actifs (67-282, 69-167, 81-1600, 84-748,
84-750, 84-753, 84-755, 88-2131) : simplement mentionnés, sans lecture. À créer si le texte du
livre les cite.

### g) TODO arabe

Les 42 nouvelles entrées AR, et les 21 promues depuis `cotisations_sociales` et
`prestations_sociales`, portent un `title` **français**. Dénomination arabe à reprendre du JORT
arabe (fascicule `pdf_ar`), jamais traduite à la machine.

### h) Zotero — conflit de rangement à trancher AVANT toute montée

`scripts/sync_biblio.py` écrit dans un livre tout article rangé dans une collection mappée, et
dans le partagé **seulement** les articles rangés dans **aucune** collection mappée (« Commun »
= hors collection, pas une collection nommée Commun). Conséquences :

1. Les 42 clés créées doivent être montées **hors collection** pour rester dans le partagé ; les
   ranger dans la collection « Retraites » les ferait descendre dans
   `precis/{fr,ar}/retraites/references.json`, en doublon du partagé.
2. Les 24 clés promues sont déjà dans Zotero **dans** leurs collections de livre (« Cotisations
   sociales », « Prestations sociales », « Rémunérations publiques ») : la prochaine descente
   les recréera dans les fichiers de livre, en doublon du partagé. Même défaut latent pour les
   huit clés promues le 10 septembre (commit 0e819f4).
3. Deux sorties : retirer ces articles de leurs collections de livre dans Zotero, ou modifier
   `sync_biblio.py` pour qu'un article présent dans plusieurs collections, ou marqué commun,
   descende dans le partagé.

#### À pousser dans Zotero — NE PAS pousser sans feu vert

- créer : les 42 clés du a) (Extra : `citation-key: <clé>` et `issue: <n°>`), hors collection
  sauf décision contraire au point h ;
- corriger : `decret74-499`, `loi2019-37`, `loi85-12` (point c) et `loi85-16` (point d) ;
- vérifier : `sdiri2014` doit exister dans Zotero, collection « Retraites », Extra
  `citation-key: sdiri2014` — depuis la suppression de sa copie `.bib`, la seule définition du
  dépôt est dans `precis/{fr,ar}/retraites/references.json`, fichier que la descente récrit ;
- déranger (sortir de leurs collections de livre) : les 24 clés du b), si la première sortie
  du point h est retenue.

### Passe « chaîne modificative de la loi n° 85-12 » — 11 septembre 2026

Source : `docs/notes/retraites-dossier.md`, § 11 à 11.6 et § 11 bis. **Aucune écriture Zotero.**
Contrôle d'unicité refait sur les `references.json` (partagé et livres) et les deux `.bib` : aucune
des quatre clés, ni aucun des quatre textes, n'existait sous une autre clé (le décret n° 96-1015
n'était cité qu'en note de `loi95-105`).

#### a) 4 clés créées (partagé FR + AR)

URL lues sur le **même** enregistrement de `jort_cache.db` : FR = `pdf_fr`, AR = `pdf_ar`. Les
quatre enregistrements portent les deux champs.

| Clé | Texte | recid | Niveau |
|---|---|---|---|
| `loi97-59` | Loi n° 97-59 du 28 juillet 1997 (art. 47 al. 3 ; effet 1er mai 1997) | 112253 | [T] |
| `decret96-1015` | Décret n° 96-1015 du 27 mai 1996 (validation des services) | 90472 | [T] |
| `decretloi2022-49` | Décret-loi n° 2022-49 du 16 août 2022 (dérogation à l'art. 37 al. 4) | 169123 | [T] |
| `decret2023-741` | Décret n° 2023-741 du 1er décembre 2023 (augmentation optionnelle de l'âge) | 183576 | [T] |

Écarts par rapport au JSON proposé au § 11.6 du dossier :
- `decret96-1015` : « Art. 8 : délais » **retiré** — le § 11.1 attribue les délais (art. 8-9) à la
  **loi n° 95-105**, non au décret ; « Art. 5 : périodes validables » réduit à l'art. 5-1 cité.
- `decretloi2022-49` : l'objet est reformulé sur le corps du § 11.2 (différentiel complémentaire,
  retenue suspendue de février 2022 à l'entrée en vigueur) ; les écarts de notice (signature
  5 août, publication 8 août, p. 2793) restent en note.
- `decret2023-741` : notice fautive (`numero` = « 2023-138 », n° du fascicule) — enregistrement
  identifié par le titre et la date.

**Pagination arabe non établie** : les entrées AR reprennent la pagination de l'édition française
(convention du dépôt : FR et AR ne diffèrent que par l'URL). Pour `decretloi2022-49`, la notice
donne p. 2793 (probablement l'édition arabe) ; pour `decret2023-741`, 3240 seule. TODO : relever
la pagination sur les fascicules `pdf_ar` si l'édition arabe doit être paginée.

#### b) Notes mises à jour (champ `note` seul, FR et AR)

Articles de la loi n° 85-12 touchés et date d'effet établie, d'après le § 11 ; « Métadonnées
seules » levé :
- partagé : `loi87-8` (art. 72 abrogé ; effet non énoncé), `loi88-71` (art. 5, 6, 16, 24, 25-26,
  33, 41, 61 ; effet 1er janvier 1989 [D] ; réserve « selon la référence du modèle ; à vérifier »
  **supprimée**), `loi90-6` (art. 6 dernier alinéa ; non énoncé), `loi96-67` (art. 48 ; non
  énoncé), `loi97-74` (art. 42 al. 3 ; non énoncé), `loi2002-61` (art. 5 2° d, 6 § 2, 33 § 3,
  41 1° c ; non énoncé), `decret96-326` (**décret n° 74-499**, art. 46 al. 1er ; non énoncé ;
  la question de la neutralité sur l'art. 18 est **tranchée**), `decret97-1927` (**décret
  n° 74-499**, art. 33 ; « Date d'effet non lue » → **1er mai 1997**, art. 2) ;
- `cotisations_sociales` : `loi2001-123-lf2002` (art. 85 → art. 9 et 13 ; **art. 86** → art. 37 ;
  **art. 97**, effet 1er janvier 2002), `decretloi2011-48` (art. 13 ; effet 1er juillet 2011 ;
  « contenu NON LU » **levé**) ;
- promue : `lf-2023` (**art. 12, édition arabe seulement**, p. 4060 de la pagination arabe →
  art. 71 bis ; effet 1er janvier 2023, art. 76).

#### c) 2 clés promues de `fiscalite` vers le partagé (retirées du fichier de livre, FR et AR)

`lf-2022` et `lf-2023`, pour la rédaction du livre « Retraites ». `lf-2022` promue **à
l'identique** ; `lf-2023` avec le seul ajout de note du point b). Champs de `lf-2023` conservés
tels quels : URL arabe dans le fichier FR (édition française absente de pist.tn) et pas de `page`.

#### d) Reste à faire

- `lf-2022` : son `page` (3086) vise l'art. 24 ; l'**art. 14** (départ anticipé dès 57 ans,
  2022-2024, « contrairement aux dispositions de la loi n° 85-12 ») est **p. 3082**. Note non
  modifiée dans cette passe : à compléter si le livre cite l'art. 14.
- Notes que le § 11 éclaire aussi, **non modifiées** (hors liste de la passe) : `loi95-105`
  (abrogation implicite des art. 14-21, barème 23-32 %, 36 mensualités ; « Métadonnées seules »
  à lever), `loi94-71` (art. 9 et 13, effets 1er juillet 1994 et 1995), `loi2007-43` (art. 1er,
  taux ; art. 9 et 13), `loi2019-37` (art. 2, art. 32 § 2 et 3).
- `lf-2025` (loi n° 2024-48, art. 14, prolongation) : [M] au dossier, pagination arabe seule.
- Textes du § 11 sans clé, à créer si le livre les cite : loi n° 88-8, décret n° 2003-1656 (non
  lu), arrêtés du Chef du Gouvernement sur les délais du programme de départ anticipé.
- **TODO arabe** : les quatre nouvelles entrées AR portent un `title` français (même réserve que
  le g) ci-dessus) ; `lf-2022` et `lf-2023` aussi.

#### e) Zotero — même conflit de rangement que le h)

- Les 4 clés créées : à monter **hors collection** (sinon descente dans le fichier du livre
  « Retraites », en doublon du partagé).
- `lf-2022` et `lf-2023` sont très probablement rangées dans la collection « Fiscalité » : la
  prochaine descente les recréera dans `precis/{fr,ar}/fiscalite/references.json`, en doublon du
  partagé. Sortie identique au h) (déranger, ou adapter `sync_biblio.py`).

#### À pousser dans Zotero — NE PAS pousser sans feu vert

- créer (hors collection) : `loi97-59`, `decret96-1015`, `decretloi2022-49`, `decret2023-741`
  (Extra : `citation-key: <clé>`) ;
- corriger la note : `loi87-8`, `loi88-71`, `loi90-6`, `loi96-67`, `loi97-74`, `loi2002-61`,
  `decret96-326`, `decret97-1927`, `loi2001-123-lf2002`, `decretloi2011-48`, `lf-2023` ;
- déranger (sortir de « Fiscalité ») : `lf-2022`, `lf-2023`, si la première sortie du h) est
  retenue.

### Passe « séries de revalorisation des pensions » — 11 septembre 2026

Source : `docs/notes/retraites-revalorisation.md` (§ 9, § 10, tableaux § 12.1 et § 12.2).
**Aucune écriture Zotero.** Script unique écrivant FR et AR ; URL : FR = `pdf_fr`, AR = `pdf_ar`,
lus sur le **même** enregistrement de `jort_cache.db` (recid contrôlé : n° de fascicule et date de
signature assertés contre la notice). Partagé : 90 → 161 entrées par langue.

#### a) Clés : le § 9.2 de la note n'emploie PAS les clés retenues

Les clés vont dans le partagé, donc au format `decretNN-NNN` / `decretAAAA-NNN`. Les clés
`decret-2015-462`, `decret-2016-1`, `decret-2019-209`, `decret-2019-1133`, `decret-2020-767`,
`decret-2026-63` proposées au § 9.2 **n'existent pas** : citer `decret2015-462`, `decret2016-1`,
`decret2019-209`, `decret2019-1133`, `decret2020-767`, `decret2026-63`. Clés existantes
conservées telles quelles : `decret-2017-668-smig`, `decret-2022-797`, `lf-2026`,
`loi2001-123-lf2002`.

#### b) 68 clés créées (partagé FR + AR)

- **SMIG et indemnités assimilées (§ 12.1)**, recid entre parenthèses : `decret80-75` (98968),
  `decret80-609` (98803), `decret81-437` (98252), `decret82-501` (97577), `decret83-509` (96960),
  `decret86-689` (95334), `decret87-1277` (94685), `decret88-889` (94420), `decret89-1551`
  (93676), `decret90-246` (93499), `decret91-1316` (92750), `decret92-1299` (92354),
  `decret92-1630` (92265), `decret93-1256` (91936), `decret93-1838` (91810), `decret94-1804`
  (91240), `decret95-900` (90925), `decret96-1013` (90470), `decret96-1547` (90337),
  `decret97-1521` (89854), `decret97-2148` (89746), `decret98-1674` (89295), `decret99-994`
  (88956), `decret99-1866` (88726), `decret2000-949` (88208), `decret2001-1746` (87333),
  `decret2002-1790` (86750), `decret2003-1691` (86068), `decret2004-1803` (85440),
  `decret2005-2320` (84800), `decret2006-2098` (84093), `decret2007-2079` (83303),
  `decret2008-2072` (82740), `decret2009-2257` (81794), `decret2010-1746` (81088),
  `decret2011-679` (80623), `decret2012-1981` (79866), `decret2014-2907` (78875),
  `decret2015-1762` (78338), `decret2018-672` (76805), `decret2019-454` (118538),
  `decret2020-1069` (148614), `decret2022-769` (—), `decret2024-419` (186713), `decret2026-67` (—).
- **Secteur public (§ 12.2, § 5.1)** : `decret82-972` (97404), `decret88-1888` (94141),
  `decret96-1907` (90242), `decret2015-462` (78509), `decret2016-1` (78276), `decret2019-209`
  (76498), `decret2019-1133` (129070), `decret2020-767` (148111), `decret2026-63` (—).
- **Treize décrets de tranches de l'IGE 1999-2012** (la note donne leur notice, § 6.2 ; créés au
  niveau [M], titre de la notice accents restitués, « montants et date d'effet non lus » en note) :
  `decret99-2015` (88704), `decret2000-1199` (88093), `decret2001-1557` (87377),
  `decret2002-2672` (86641), `decret2003-1568` (86136), `decret2004-1538` (85490),
  `decret2005-3137` (84663), `decret2006-2182` (84048), `decret2007-1671` (83390),
  `decret2008-4047` (82262, [T]), `decret2009-2145` (81826), `decret2010-1973` (81029),
  `decret2012-2959` (79693).
- **§ 10.2** : `arrete-1997-03-29-bareme-actualisation` (60518) — [T°].

Niveau de lecture de chaque entrée porté dans son `note` (lu à l'image / couche texte / OCR /
métadonnées seules) ; les montants [V] de la note (repris d'un inventaire, non lus) n'ont **pas**
été reportés dans les notes.

#### c) 3 clés promues d'un livre vers le partagé (retirées du fichier de livre, FR et AR)

- `decret-2022-797` (depuis `remunerations_publiques`) — **complétée** : titre FR tronqué complété
  sur le fascicule local (« … au titre des années 2023-2024-2025 ») ; ajout `container-title`,
  `issue: 120`, `page: 2959-2966` et note de contenu. Titre arabe de l'entrée AR conservé.
- `lf-2026` (depuis `fiscalite`) — note complétée de l'art. 15 (édition arabe, p. 4233).
- `loi2001-123-lf2002` (depuis `cotisations_sociales`) — à l'identique.

#### d) Entrées existantes du partagé modifiées — À REPORTER DANS ZOTERO

- `decret79-510`, `decret81-939`, `decret82-971`, `decret83-737` : « Métadonnées seules ; texte non
  lu » remplacé par le contenu lu à l'image (§ 1.2, § 5.1), date d'effet comprise.
- `decret94-1429` : note complétée des art. 18 et 19 (nouveaux) (§ 10.1).
- `decret-2017-668-smig` : note complétée (effet 1er août 2016, montants, lecture sur l'édition
  arabe) ; **URL de l'entrée AR corrigée** : elle portait l'URL française `2017F/Jo0452017.pdf`,
  elle porte désormais `pdf_ar` = `2017A/Ja0452017.pdf` (recid 77455).

#### e) URL pist.tn qui servent l'édition arabe (§ Conventions de la note)

- `2017F/Jo0452017.pdf` : URL de l'entrée **FR** `decret-2017-668-smig` (c'est le `pdf_fr` de la
  notice). Laissée en place, faute d'autre URL française ; la note le dit. Aucune édition française
  vue.
- `2019F/Jo0202019.pdf` : **aucune entrée ne la porte**. `decret2019-209` : `pdf_fr` vide dans la
  notice → URL arabe `2019A/Ja0202019.pdf` dans les deux langues (précédent des « cinq éditions
  françaises absentes »), sans `page` (pagination française non établie ; p. 727 de l'édition arabe).
- `2025F/Jo1482025.pdf` : **aucune entrée ne la porte**. L'entrée FR `lf-2026` pointe déjà, à
  dessein, sur `2025A/Ja1482025.pdf` : ne pas la « corriger ».

#### f) Écarts de notice (§ 10.7) et de pagination — signalés, non tranchés

- `decret86-689` : notice signée le 20 juillet 1986, « publiée » le 18 juillet. Entrée créée avec la
  date de signature de la notice ; incohérence en note. Fascicule (image non océrisée) à ouvrir.
- `decret88-889` : notice signée le 5 juin 1988 (titre compris), publiée le 6 mai 1988 ; le visa du
  décret n° 90-246, lu à l'image, porte **5 mai 1988**. Entrée créée au **5 juin** (notice), doute en
  note. **TODO** : lire l'intitulé au fascicule `1988F/Jo03188.pdf`, p. 715, puis corriger `issued`
  et `title` si le 5 mai se confirme.
- `decret2020-767` : notice pp. 1072-1078 ; entrée à **2072-2079** (pagination française lue).
- **Pagination de notice = pagination arabe** (défaut documenté, `outillage-sources.md` § 4 ;
  vérifié ici encore) : `decret2019-454`, notice
  pp. 1681-1682 (numéro vide, intitulé arabe) ; le sommaire du fascicule français local
  (`PDFs/JORT/2019/fr/Jo0432019.pdf`) donne **p. 1585**, retenue. La note de revalorisation (§ 2.2)
  donne à tort 1681-1682 comme pages françaises. Les pages [M] de cette passe (86-689, 88-889,
  99-994, 99-1866, 2002-1790 à 2005-2320, les douze tranches non lues) sont donc **provisoires** ;
  chaque note le dit.
- `decret2018-672` : notice sans pages, intitulé arabe ; p. 2684 et intitulé (« code **de**
  travail ») relevés sur le sommaire et le texte du fascicule français local.
- `decret2019-1133` : l'intitulé du § 9.2 omet « et la fixation de ses montants » ; intitulé complet
  relevé sur le fascicule.
- `decret2015-462` : intitulé FR « au titre de l'année 2014 » (fascicule), notice arabe « 2015 ».
- `decret92-1299` : deux notices (n° 49, pp. 935-936, retenue ; n° 55, p. 1067, « rectificatif »,
  recid 92316, non lu, porté en note).
- `decret2000-949` (`Ja03800.pdf`) et `decret2000-1199` (`Ja04700.pdf`) : `pdf_ar` hors convention
  de nommage. Écrits tels quels ; tous deux répondent `200 application/pdf` (10,3 Mo et 0,65 Mo),
  contenu non ouvert.
- Doublons **de texte** antérieurs, non introduits ici, relevés en contrôle : `loi2017-66-lf2018` et
  `lf-2018` (même loi, `remunerations_publiques`) ; `lf-1991` (`fiscalite`) et
  `loi-90-111-lf-1991` (`prestations_sociales`).

#### g) Sans URL — TODO

Texte sans enregistrement dans `jort_cache.db` → pas d'URL. Fascicule vérifié en local, URL
candidate (curl 200 selon la note, 11 septembre 2026) à valider par un humain ou par une mise à jour
de la base :
- `decret2026-63` et `decret2026-67` : base arrêtée au 10 avril 2026 ; fascicule
  `PDFs/JORT/2026/fr/Jo0442026.pdf` (candidate `2026/2026F/Jo0442026.pdf`, AR `Ja0442026.pdf`
  présent en local).
- `decret2022-769` : aucune notice (seul le décret SMAG n° 2022-768 du même fascicule en a une) ;
  fascicule `PDFs/JORT/2022/fr/Jo1142022.pdf` (candidate `2022/2022F/Jo1142022.pdf`).
- `decret2019-454` : **a** une URL (arabe, `pdf_ar`), `pdf_fr` vide ; une édition française existe
  en local (`Jo0432019.pdf`) : URL française candidate à vérifier (ouvrir le fichier servi, cf.
  `outillage-sources.md` § 3).

#### h) Restent sans clé

- Cités par la note hors du périmètre de la passe (§ 12 et § 10) : décrets n° 2026-64, 2026-65
  (magistrats), 2026-66 (SMAG), arrêté du 10 juillet 2020 (prime exceptionnelle aux pensions),
  *Lettre CRES* n° 3 (2014). JSON prêt au § 9.2 ; à créer si le livre les cite (2026-* : sans URL,
  même motif qu'au g).
- Série SMAG (§ 3.2), décrets IGE non lus de 1990-1998 (90-1001, 91-803, 93-2062, 97-1174,
  98-1292), décrets n° 81-444, 82-504, 82-505, 84-424, 85-980 (déjà clé `decret85-980`) : pas de clé
  nouvelle.
- Les autres arrêtés annuels de barème d'actualisation (1994-2024) : seul celui du 29 mars 1997 a
  une clé.

#### i) TODO arabe

Les 68 entrées AR créées portent un `title` français (même réserve qu'au g) de la passe du
11 septembre). Plusieurs notices portent un intitulé arabe (2015-462, 2016-1, 2018-672, 2019-209,
2019-454) : à reprendre du fascicule `pdf_ar`, non de la notice (troncatures connues).

#### j) Ce que la descente `sync_biblio.py` fera de ces URL — à trancher avant la montée

La descente **dérive** l'URL d'une langue depuis l'autre (`url_jort` : `F/Jo` ↔ `A/Ja`), sauf pour
les URL listées dans `precis/urls-jort.json` (`sans_homologue`). Contrôle `curl -k` du
11 septembre 2026 :
- `decret-2017-668-smig` : `2017F/Jo0452017.pdf` figure dans `sans_homologue` ; la descente
  remettra l'entrée AR sur l'URL « F ». Sans conséquence pour le lecteur : `Jo0452017.pdf` et
  `Ja0452017.pdf` sont **identiques à l'octet** (md5 `523cfa73…`).
- `decret2000-949` et `decret2000-1199` : l'URL AR dérivée (`2000A/Ja0382000.pdf`,
  `2000A/Ja0472000.pdf`) répond **404** ; les URL AR de la notice (`Ja03800.pdf`, `Ja04700.pdf`)
  répondent 200. La descente produirait deux liens AR morts : ajouter ces deux URL à un mécanisme
  d'exception, ou corriger le motif de dérivation.
- `decret2019-454` : l'entrée FR porte l'URL arabe (`pdf_fr` vide). La descente la dériverait vers
  `2019F/Jo0432019.pdf`, qui répond 200 et sert bien l'**édition française** (« Traduction
  française pour information », md5 identique au fichier du corpus local). URL française
  candidate **vérifiée** : peut remplacer l'URL arabe de l'entrée FR sur décision.
- `decret2019-209` : la descente dériverait l'entrée FR vers `2019F/Jo0202019.pdf`, qui sert
  l'**édition arabe** (note, § Conventions) : l'ajouter à `sans_homologue`, ou accepter le lien.
- `lf-2026` : `2025A/Ja1482025.pdf` déjà dans `sans_homologue`, rien à faire.

`urls-jort.json` n'a pas été modifié (fichier régénéré par `scripts/verifier_urls_jort.py`).

#### k) Zotero

Même conflit de rangement qu'au h) de la passe « Retraites » : les 68 clés à monter **hors
collection** ; `decret-2022-797` (collection « Rémunérations publiques »), `lf-2026`
(« Fiscalité ») et `loi2001-123-lf2002` (« Cotisations sociales ») redescendront dans leurs
fichiers de livre, en doublon du partagé, tant que le point h) n'est pas tranché.

#### À pousser dans Zotero — NE PAS pousser sans feu vert

- créer (hors collection) : les 68 clés du b) (Extra : `citation-key: <clé>` **et** `issue: <n°>` —
  le type `legislation` de Zotero n'a pas de champ pour le n° du JORT ; sans cette ligne, la
  descente effacerait `issue` des 68 entrées) ;
- corriger : `decret-2022-797` (titre, issue, page, note), `lf-2026` (note), `decret79-510`,
  `decret81-939`, `decret82-971`, `decret83-737`, `decret94-1429`, `decret-2017-668-smig` (notes ;
  pour ce dernier, l'URL arabe n'est pas un champ Zotero partagé : vérifier comment
  `sync_biblio.py` produit l'URL AR avant la montée) ;
- déranger (sortir de leurs collections de livre) : `decret-2022-797`, `lf-2026`,
  `loi2001-123-lf2002`, si la première sortie du h) est retenue.

### Passe « Retraites — fenêtre du salaire de référence » (11 septembre 2026) — À REPORTER DANS ZOTERO

- `decret90-1455` et `decret94-1429` : champ `note` réécrit (FR et AR) — articles modifiés, art. 19
  non touché en 1990, remplacement de l'art. 18 par le décret de 1994, dates d'effet (exécutoire le
  23 septembre 1990 ; paliers énoncés 1er juillet 1994/1995/1996). Source : `retraites-dossier.md` § 12.
- [x] ~~À créer : `arrete-1994-11-17-bareme-actualisation`~~ — créée le 11 septembre 2026 (passe
  suivante).

### Passe « Retraites — avant retouche du livre » (11 septembre 2026)

**Aucune écriture Zotero.** Partagé : 161 → 165 entrées par langue ; `cotisations_sociales` :
14 → 13. Aucun `.qmd` modifié.

#### a) 3 clés créées (partagé FR + AR)

- [x] `arrete-1994-11-17-bareme-actualisation` — recid **61474** (arrêté, signé le 17 novembre 1994,
  JORT n° 93 du 25 novembre 1994, p. 1898 ; notice concordante). URL FR = `pdf_fr`
  `1994F/Jo09394.pdf`, AR = `pdf_ar` `1994A/Ja09394.pdf`, lues sur la notice. Page contrôlée sur le
  fascicule local : l'arrêté tient entièrement sur la p. 1898 (page 10 du fichier). Intitulé,
  coefficients 1961 (6,48469) et 1993 (1,00000), art. 2 (droits ouverts à compter du
  1er juillet 1994) recontrôlés sur la couche texte ; lecture à l'image : dossier § 12.
- [x] `decret2026-65` — **sans URL** (JORT n° 44 du 30 avril 2026, postérieur à l'état de
  `jort_cache.db`, arrêtée au 10 avril 2026 ; aucune notice). Intitulé et page (**835**) relevés sur
  `PDFs/JORT/2026/fr/Jo0442026.pdf` (couche texte). **Magistrats** (ordre judiciaire, Tribunal
  administratif, Cour des comptes) : 120 D aux 1er janvier 2026, 2027 et 2028 sur l'indemnité de
  magistrature ; **art. 2** : applicable aux pensions des retraités. La demande de passe le désignait
  comme « augmentation dans le secteur public » : c'est bien ce texte (clause pensions à l'art. 2 ;
  2026-63 et 2026-64 la portent à l'art. 4), l'intitulé retenu est celui du fascicule.
- [x] `decret2026-66` — **sans URL**, même motif. SMAG, p. **837** ; art. 1er (21,336 / 22,400 /
  23,520 D par jour aux 1er janvier 2026/2027/2028), art. 2 (prime de technicité), **art. 5** :
  « s'applique aux pensions de retraite ». Clé de la note § 9.2 `decret2026-66` conservée ; URL
  proposée par la note (`2026F/Jo0442026.pdf`) **non reprise** (pas d'enregistrement dans la base).

La clé `decret-2026-65` proposée au § 9.2 de `retraites-revalorisation.md` n'est pas retenue :
citer `decret2026-65`.

#### b) 1 clé promue (retirée du fichier de livre, FR et AR)

- [x] `decretloi2011-48` — de `precis/{fr,ar}/cotisations_sociales/references.json` vers
  `precis/{fr,ar}/references.json`, objet copié à l'identique ; URL déjà conformes à la notice
  recid 80629 (FR `2011F/Jo0412011.pdf`, AR `2011A/Ja0412011.pdf`). Aucun `.qmd` ne la cite encore :
  le TODO bibliographe de `precis/fr/retraites/_secteur_public.qmd` (l. 59) est levé côté
  bibliographie, la citation reste à poser par le rédacteur.

#### c) Notes vérifiées, non modifiées

- `loi2001-123-lf2002` : la note porte déjà l'art. 86 (art. 37 réécrit, péréquation) et l'art. 97
  (effet au 1er janvier 2002), FR et AR.
- `decret97-1927` : la note porte déjà l'art. 2 (effet au 1er mai 1997), FR et AR.

#### d) Sans URL — TODO

- `decret2026-65`, `decret2026-66` : s'ajoutent à `decret2026-63` et `decret2026-67` (passe
  « séries de revalorisation », g). URL candidates `2026/2026F/Jo0442026.pdf` et
  `2026/2026A/Ja0442026.pdf` (fascicules présents en local) à reprendre de `pdf_fr` / `pdf_ar` quand
  `jort_cache.db` couvrira le 30 avril 2026.

#### e) TODO arabe

Les 3 entrées AR créées portent un `title` français (même réserve que les passes précédentes) ;
intitulés arabes à relever sur `Ja09394.pdf` et `Ja0442026.pdf`, non sur une notice.

#### f) Contrôles

JSON valides (4 fichiers) ; aucun identifiant en double dans un fichier ni entre le partagé et un
fichier de livre ; doublons connus inchangés (`loi96-101` et `lf-2018`, en double entre deux
fichiers de livre ; `loi2016`, présent dans `references.bib`, non touché : le contrôle par
identifiant ne le fait pas apparaître en double). Rendu HTML de `precis/fr/retraites` et `precis/fr/cotisations_sociales` sans
citation non résolue ; aucun `figdata` modifié par le rendu.

#### À pousser dans Zotero — NE PAS pousser sans feu vert

- créer (hors collection, cf. conflit de rangement h) : `arrete-1994-11-17-bareme-actualisation`,
  `decret2026-65`, `decret2026-66` (Extra : `citation-key: <clé>` **et** `issue: <n°>`) ;
- déranger : `decretloi2011-48`, s'il est rangé dans la collection « Cotisations sociales » (sinon il
  redescendra dans le fichier de livre, en doublon du partagé) ;
- corriger (notes, passe précédente) : `decret90-1455`, `decret94-1429`.

### Passe « Retraites — entrée en vigueur des textes » (11 septembre 2026)

**Aucune écriture Zotero.** Partagé : 165 → 167 entrées par langue. Fichiers modifiés par cette
passe, et eux seuls : `precis/fr/references.json`, `precis/ar/references.json` et la présente note.
Les modifications de `precis/glossaire.yml`, `precis/{fr,ar}/retraites/_glossaire.qmd` et
`precis/fr/retraites/_secteur_prive.qmd` présentes dans l'arbre sont antérieures ou concurrentes,
et ne viennent pas de cette passe.

#### a) 2 clés créées (partagé FR + AR), règles générales de computation des dates d'effet

Contrôle d'unicité préalable (partagé, fichiers de livre, deux `.bib`) : aucun des deux textes
n'avait de clé. URL : FR = `pdf_fr`, AR = `pdf_ar`, lues sur le **même** enregistrement ; notice
assertée (date de signature, n° de fascicule, pages) avant écriture.

- [x] `decret-1956-09-13-publication` — recid **108190**. Décret du 13 septembre 1956 (7 safar 1376)
  modifiant le décret du 27 janvier 1883 relatif à la publication des décrets et arrêtés ; JORT
  n° 74 du 14 septembre 1956, p. 1247 ; FR `1956F/Jo07456.pdf`, AR `1956A/Ja07456.pdf`. Article
  unique (art. 3 nouveau, un jour franc) **lu** par OCR `tesseract -l fra` du fascicule local
  (couche texte absente), al. 1 et al. 2 (exécution immédiate par disposition expresse) cités
  séparément. **Écart de notice** : la notice titre « Decret du Chef du gouvernement du
  13 Septembre 1956 » ; l'intitulé du fascicule (décret beylical, rubrique « Présidence du
  Conseil ») ne nomme aucune autorité. Intitulé du fascicule retenu, écart porté en note.
  `container-title` : « Journal officiel tunisien » (titre du fascicule en 1956) ; première entrée
  `legislation` antérieure à 1957 à en porter un, convention à confirmer.
- [x] `loi93-64` — recid **112971**. Loi n° 93-64 du 5 juillet 1993 ; JORT n° 50 du 6 juillet 1993,
  p. 931 (notice « 0931 ») ; FR `1993F/Jo05093.pdf`, AR `1993A/Ja05093.pdf`. Art. 1er, art. 2
  (cinq jours après le dépôt au siège du gouvernorat de Tunis, jour du dépôt exclu) et art. 3
  (abroge le décret du 27 janvier 1883 et ses modificatifs, dont ceux du 8 septembre 1955 et du
  13 septembre 1956) **lus** par OCR du fascicule local, p. 931.

Aucun `.qmd` ne cite encore ces deux clés : résolution contrôlée hors livre (`quarto pandoc
--citeproc` sur les deux fichiers, FR et AR).

Les deux paires d'URL suivent exactement le motif `F/Jo` ↔ `A/Ja` : la descente `sync_biblio.py`
les régénère à l'identique, aucune exception `sans_homologue` n'est nécessaire.

#### b) Notes nettoyées de toute mention du modèle (FR et AR, champ `note` seul)

Le précis ne parle pas du modèle. Faits de droit conservés ; remarques retirées, **à reporter dans
`docs/notes/backlog-modele.md`** si elles doivent survivre (non fait dans cette passe) :
- [x] `decretloi2011-48` : retiré « Porte le palier employeur de juillet 2011 dans le modèle
  openfisca-tunisia. » (art. 13 de la loi n° 85-12, effet 1er juillet 2011, régimes concernés
  conservés) ;
- [x] `arrete-1978-11-18-retraite-complementaire` : retiré « le taux global de 9 % (6 points
  employeur / 3 points salarié) que porte le modèle n'est pas attesté par ce texte » ;
- [x] `decret74-572` : retiré « à confronter à la date 1993-02-01 portée par les paramètres du
  modèle » ;
- [x] `loi88-16` : retiré « Attention : le modèle openfisca-tunisia la date par erreur de 1983 dans
  son titre arabe. » ;
- [x] `cnrps-manuel-liquidation-2013` : retiré « Exemplaire local : openfisca-tunisia-pension/tmp/
  manuel pensions.pdf. » (chemin de dépôt ; l'exemplaire reste à cet emplacement, cf. e) de la
  passe « Livre Retraites »).

Plus aucune occurrence de « openfisca » ni de « modèle » dans les deux `references.json` partagés.

#### c) TODO

- **TODO arabe** : les 2 entrées AR portent un `title` français ; intitulés arabes à relever sur
  `Ja07456.pdf` et `Ja05093.pdf`, non traduits.
- **Hors périmètre (partagé seulement), à décider** : notes de livre qui nomment encore le modèle,
  FR et AR — `cotisations_sociales` : `decret2003-1544` (« la date du 2 juillet 2003 retenue par le
  modèle openfisca-tunisia est celle de la signature… ») et `decret97-1645` (« Le modèle
  openfisca-tunisia ne porte aucun paramètre pour cette variante. »). Le « modèle de scoring » du
  titre de `arrete-2020-05-19-scoring` (`prestations_sociales`) est le mot du texte : rien à faire.
- Ne pas calculer dans les notes la date d'effet propre de la loi n° 93-64 : articles consignés tels
  que lus, computation laissée au rédacteur.

#### d) Contrôles

JSON valides ; aucun identifiant en double introduit (doublons connus `loi96-101` et `lf-2018`
inchangés) ; rendu HTML de `precis/fr/retraites` sans citation non résolue ; aucun `figdata`
modifié par le rendu.

#### À pousser dans Zotero — NE PAS pousser sans feu vert

- créer (hors collection, cf. conflit de rangement h) : `decret-1956-09-13-publication`,
  `loi93-64` (Extra : `citation-key: <clé>` **et** `issue: <n°>`) ;
- corriger la note : `decretloi2011-48`, `arrete-1978-11-18-retraite-complementaire`,
  `decret74-572`, `loi88-16`, `cnrps-manuel-liquidation-2013`.

### Livre « Fiscalité », section « Les droits de consommation » — passe bibliographe 16/09/2026

Source : `docs/notes/fiscalite-droits-consommation-documentation.md`, annexe A. **15 clés créées** et
**4 clés existantes complétées**, dans `precis/fr/fiscalite/references.json` ET
`precis/ar/fiscalite/references.json` (URL FR = `pdf_fr`, URL AR = `pdf_ar`, lues sur
l'enregistrement de `jort_cache.db`, jamais dérivées l'une de l'autre).

#### Créées — type CSL `legislation` (11)

- [ ] `loi-88-62-droit-consommation` — JORT n° 39 de 1988, t. 131, p. 847-856 ; FR `Jo03988`, AR `Ja03988`.
- [ ] `loi-88-145-lf-1989` — n° 87, t. 131, p. 1793-1805 ; FR `Jo08788`, AR `Ja08788`.
- [ ] `loi-89-115-lf-1990` — n° 88, t. 132, p. 2144-2155 ; FR `Jo08889`, AR `Ja08889`.
- [ ] `decret-91-550-tarif-petroliers` — n° 29 de 1991, t. 134, p. 936 ; FR `Jo02991`, AR `Ja02991`.
- [ ] `decret-91-551-tarif-boissons` — même fascicule, p. 936-937.
- [ ] `decret-94-816-hydrocarbures` — n° 30, t. 137, p. 628-629 ; FR `Jo03094`, AR `Ja03094`.
- [ ] `decret-97-1368-regime-alcools` — n° 59, t. 140, p. 1301-1316 ; FR `Jo05997`, AR `Ja05997`.
- [ ] `decret-99-894-tarif-petroliers` — n° 33, t. 142, p. 624-625 ; FR `Jo03399`, AR `Ja03399`.
- [ ] `decret-gouv-2015-1768-annexes-alcools` — n° 92 de 2015 ; FR `Jo0922015`, AR `Ja0922015`.
      Pagination et tome **vides** dans la notice : champs omis, pas devinés.
- [ ] `loi-2007-70-lf-2008` — n° 104, t. 150, p. 4367 ; FR `Jo1042007`, AR `Ja1042007`.
- [ ] `loi-2018-56-lf-2019` — n° 104 de 2018, p. 4548-4553 ; **entrée FR SANS URL** (voir ci-dessous),
      AR `Ja1042018`.

Les 21 champs URL versés portent 19 adresses distinctes (10 FR + 11 AR ; le fascicule 1991 n° 29 sert les décrets 91-550 et 91-551), toutes re-vérifiées le 16/09/2026 (HTTP 200).

#### Créées — doctrine administrative, type CSL `report` (4)

`dgi-nc-24-2007`, `dgi-nc-29-2007`, `dgi-nc-7-2016`, `dgi-nc-17-2018`. En-têtes et objets **lus sur
les copies locales** (`PDFs-legislation-tunisie/markdown_output/Notes_Communes/`) : les bulletins
« Texte n° DGI 2007/35 » et « n° DGI 2007/64 » sont confirmés, ainsi que l'exemple chiffré de la
NC 29/2007 (500 D HT, DC 50 D, FODEC 5 D, assiette TVA **555 D**).

#### Doublons ÉVITÉS — 4 entrées existantes complétées, aucune clé nouvelle

L'annexe A en signalait deux ; il y en avait **quatre**. Dans les quatre cas, seul le champ `note` a
reçu un paragraphe « DROIT DE CONSOMMATION » ; **le champ `page` n'a pas été touché**, car il porte
la pagination des articles IRPP déjà cités par le chapitre correspondant.

- [ ] `lf-1991` = loi n° 90-111 → l'annexe A proposait `loi-90-111-lf-1991` (art. 38, tableau « N »).
- [ ] `lf-2014` = loi n° 2013-54 → l'annexe A proposait `loi-2013-54-lf-2014` (art. 70).
- [ ] `lf-2016` = loi n° 2015-53 → l'annexe A proposait `loi-2015-53-lf-2016-dc` (art. 44, 45, 57).
- [ ] `lf-2018` = loi n° 2017-66 → l'annexe A proposait `loi-2017-66-lf-2018-dc` (art. 45 et 22).

#### Fascicules français non servis par pist.tn — TODO

**Méthode, car elle a été mise en doute et elle est reproductible.** Vérification par requête HTTP
réellement aboutie : `curl -ksI <url>`. **Le `-k` n'est pas optionnel** — le certificat TLS de
pist.tn est expiré (convention déjà consignée dans ce dépôt). Sans lui, `curl` sort en **code 60**
et Python lève `SSL: CERTIFICATE_VERIFY_FAILED` : on croit alors le site injoignable, alors qu'il
répond. Les réponses reçues portent des en-têtes serveur complets (`Server: Apache`, `ETag`,
`Last-Modified`, `Content-Length`) : ce sont des requêtes abouties, non des déductions. L'absence de
`pdf_fr` dans `jort_cache.db` n'a servi que de **seconde** voie concordante.

Les deux éditions **françaises** ci-dessous rendent **404** ; seule l'édition arabe répond 200 :

- **JORT 2015 n° 104** (`Jo1042015.pdf`) — entrée `lf-2016` ;
- **JORT 2018 n° 104** (`Jo1042018.pdf`) — entrée `loi-2018-56-lf-2019`.

Conformément à la convention, **l'entrée FR reste sans URL** plutôt que de porter celle de l'édition
arabe. **`lf-2016` portait justement l'URL arabe dans le fichier FR : elle a été RETIRÉE.** À
surveiller : si une descente `sync_biblio.py` la réintroduit, c'est Zotero qu'il faut corriger.

- [ ] **TODO** : retrouver une édition française de ces deux fascicules (autre source que pist.tn),
      ou acter durablement l'absence d'URL.
- [ ] **TODO — hors périmètre de cette passe, à trancher** : `lf-2020` et `lf-2024`
      (`precis/fr/fiscalite/references.json`) portent **le même défaut** — une URL arabe dans le
      fichier français. La convention est donc enfreinte à deux autres endroits, non corrigés ici.

#### TODO de vérification restants

- [ ] `dgi-nc-24-2007`, `dgi-nc-29-2007`, `dgi-nc-7-2016`, `dgi-nc-17-2018` : **aucune URL pérenne**
      identifiée (non recherchées sur jibaya.tn). Entrées sans URL, à compléter.
- [ ] `dgi-nc-7-2016` : le numéro « 7/2016 » n'est attesté que par le **nom de fichier** de la copie
      locale — ni en-tête de bulletin ni numéro dans le corps du document. À confirmer sur l'original.
- [ ] `decret-94-816-hydrocarbures`, `decret-97-1368-regime-alcools`,
      `decret-gouv-2015-1768-annexes-alcools`, `loi-2007-70-lf-2008` : **non lus sur pièce**
      (métadonnées de notice). Date d'effet **non établie** pour les trois décrets. Leurs tarifs ne
      doivent pas être cités d'après ces entrées.
- [ ] `loi-2007-70-lf-2008`, `lf-2014` : date d'effet au 1er janvier **déduite**, clause non lue.
- [ ] `decret-91-550-tarif-petroliers` : anomalie de visa (art. 35 de la loi 88-145 au lieu de la loi
      89-115) et divergence « 91-111 » / « 90-111 » — consignées en note, **non résolues**.
- [ ] **TODO arabe** : les 15 entrées AR portent un `title` et une `note` en français — c'est le
      motif établi du fichier, mais les intitulés arabes restent à relever sur les fascicules `Ja…`.

#### Contrôles

JSON valides, 67 entrées par fichier, FR et AR strictement alignés sur les `id`. Résolution des
24 clés (15 créées, 4 complétées, 5 réutilisées) contrôlée **hors livre** par
`quarto pandoc --citeproc` sur les deux bibliographies : **zéro `[?]`** — la section
`_droits_consommation.qmd` ne comptant que 3 lignes et ne citant encore aucune clé, le rendu du
livre seul n'aurait rien éprouvé. Conversion Zotero éprouvée hors ligne sur l'arbre de travail
(`push_biblio.py --verifier`) : **348 entrées, 0 perte de champ** (333 avant la passe).

#### À pousser dans Zotero — NE PAS pousser sans feu vert

- créer : les **15 clés** ci-dessus (Extra : `citation-key: <clé>` **et** `issue: <n°>`) ;
- corriger la note : `lf-1991`, `lf-2014`, `lf-2018` ;
- corriger la note **et retirer l'URL** : `lf-2016`.

Collection Zotero visée : « Fiscalité » (présente dans `COLLECTION_TO_BOOK`). Rappel : un article
créé par l'API arrive **sans collection** — l'action `ranger` est indispensable après un envoi.

### Correctif de la même passe (16/09/2026) — doublon inter-livres et URL arabes en fichier français

#### a) Doublon inter-livres créé par cette passe — RÉSOLU

`loi-2018-56-lf-2019`, que j'avais créée dans le livre Fiscalité, faisait double emploi avec
**`loi2018-56-lf2019`**, déjà sur `master` dans « Rémunérations publiques » (même loi, même date).

- [x] **Ma clé a été supprimée** des deux fichiers du livre Fiscalité. C'est elle qui devait céder :
      elle n'était citée nulle part, tandis que `loi2018-56-lf2019` est citée par
      `_regime_marche_controle.qmd` (FR **et** AR). Renommer l'ancienne aurait cassé de la prose.
- [x] La clé survivante a été **enrichie** (issue 104, p. 4548-4553, articles 62, 69 et 80) puis
      **remontée au fonds commun** (`precis/{fr,ar}/references.json`) et retirée du livre
      « Rémunérations publiques » : elle est désormais citée par **deux** livres.
- [x] **`lf-2018`** : même situation, ancienne et non de mon fait — citée par Fiscalité **et**
      Rémunérations publiques, et présente **en double** dans les deux fichiers de livre. Remontée au
      fonds commun, retirée des deux. C'est aussi ce que réclamait `controle-rangement`
      (« lf-2018 — retirer : fiscalite, remunerations_publiques »).

#### b) Neuf URL arabes dans des fichiers français — traitées une par une

Le contrôle inverse est propre : **aucune** URL française dans un fichier arabe. Après traitement,
l'invariant est vérifié par assertion sur les **six** fichiers : toute URL `/jort/` d'un fichier FR
est en `F/Jo`, toute URL d'un fichier AR est en `A/Ja`.

**Le piège à connaître : un `200` sur un chemin en `F/Jo` ne prouve PAS qu'une édition française
existe.** pist.tn sert parfois le fascicule **arabe** sous une adresse en `…F/Jo…`. Vérifié deux fois
plutôt qu'une, en ouvrant les fichiers :

- `lf-2026` — `2025F/Jo1482025.pdf` répond 200 ; téléchargé en entier (8 775 232 o), sa page 1 est
  **arabe** (« السنـة 168 — عـدد 148 »). URL retirée. *L'ancienne note disait déjà vrai.*
- `decret2019-209` — `2019F/Jo0202019.pdf` répond 200 ; l'exemplaire local de même taille
  (1 921 747 o) s'ouvre sur un **sommaire arabe**. URL retirée. *Il avait été signalé comme
  corrigeable : il ne l'est pas.*

**Une seule correction était démontrable**, et elle a été faite :

- [x] `decret2019-454` → `https://www.pist.tn/jort/2019/2019F/Jo0432019.pdf` : 200,
      `Content-Length` 1 399 936 = taille exacte de l'exemplaire local, dont la page 1 porte
      « TRADUCTION FRANÇAISE POUR INFORMATION — … 28 mai 2019 — N° 43 ». Le `pdf_fr` vide de
      `jort_cache.db` était une **lacune de la base**, pas une absence de fascicule.

**URL arabes retirées des entrées françaises** (candidat FR testé et 404, ou servant l'arabe) —
l'adresse arabe est conservée **dans la note**, et l'entrée arabe homologue la garde en `URL` :

- [x] `lf-2020`, `lf-2024` (`precis/fr/fiscalite/`) ;
- [x] `lf-2023`, `lf-2025`, `lf-2026`, `decret2019-209` (`precis/fr/references.json`, fonds commun) ;
- [x] `loi-org-2018-29-ccl`, `loi2018-56-lf2019` (`precis/fr/remunerations_publiques/`).

Soit **8 retraits + 1 correction**. Ces entrées viennent de Zotero : la correction doit y remonter,
sans quoi la prochaine descente réinstallera les URL arabes. **C'est la cause mécanique** du fait que
l'entorse soit à sens unique.

- [ ] **TODO** : si une édition française de ces fascicules existe hors pist.tn, la référencer ;
      sinon, acter durablement l'absence d'URL.

### Clôture de la section « Droits de consommation » (16/09/2026) — 14 clés versées

Le chapitre `_droits_consommation.qmd` portait un `<!-- TODO (bibliographe) -->` réclamant
18 textes. **Quatre existaient déjà** et n'ont pas été recréés : `lf-1993` (loi 92-122),
`lf-1998` (loi 97-88), `lf-2005` (loi 2004-90), `lf-2007` (loi 2006-85). Leur note a été
**complétée** d'un paragraphe « DROIT DE CONSOMMATION » ; le TODO du chapitre sur-comptait donc
de quatre. Restaient **14 créations**, faites dans `precis/{fr,ar}/fiscalite/references.json`.

Méthode : URL FR lue dans `pdf_fr`, URL AR dans `pdf_ar` du **même enregistrement** de
`jort_cache.db` (jamais dérivée par transformation de chaîne). **Édition française établie sur
pièce** pour les 14 : taille distante (`curl -ksI`, `content-length` — le certificat TLS de
pist.tn est expiré, `-k` est obligatoire) **égale à l'octet près** au fascicule du corpus local
`PDFs-legislation-tunisie`, dont la première page porte « traduction française » (couche texte
ou page 1 relue à l'image). Un `200` sur un chemin `…F/Jo…` ne prouve rien par lui-même.

| Clé | Texte | Degré établi |
|---|---|---|
| `lf-1995` | Loi n° 94-127 (LF 1995), **art. 64** | **lu sur pièce** (couche texte) |
| `lf-1997` | Loi n° 96-113 (LF 1997), **art. 51** | **lu sur pièce** |
| `lf-1999` | Loi n° 98-111 (LF 1999), **art. 50** | **lu sur pièce** |
| `lf-2013` | Loi n° 2012-27 (LF 2013), **art. 43** | **lu sur pièce, en entier** |
| `decret-89-479-tableau` | Décret n° 89-479, modif. du tableau annexé | titre + pagination **lus à l'image** (sommaire FR) |
| `decret-89-1348-tableau` | Décret n° 89-1348, modif. du tableau annexé | titre + pagination **lus à l'image** (sommaire FR) |
| `decret-2007-1977-alcools` | Décret n° 2007-1977, modif. du décret 97-1368 | **visas lus sur pièce** |
| `decret-2013-929-alcools` | Décret n° 2013-929, modif. du décret 97-1368 | **visas et intitulés de tableaux lus sur pièce** |
| `decret-2002-627-alcools` | Décret n° 2002-627, modif. du décret 97-1368 | substance lue (encodage décalé), **chiffres perdus** |
| `lf-1994` | Loi n° 93-125 (LF 1994), art. 50 | notice ; **numéro corroboré** par l'art. 64 de la LF 1995, lu sur pièce |
| `lf-1992` | Loi n° 91-98 (LF 1992) | notice seule (titre 4, p. 2085-2086) |
| `lf-2003` | Loi n° 2002-101 (LF 2003) | substance lue, **n° d'article non établi** |
| `lf-2004` | Loi n° 2003-80 (LF 2004) | substance lue, **n° d'article non établi** |
| `decret-88-2002-suppressions` | Décret n° 88-2002 | **notice seule** |

#### Ce qui reste NON ÉTABLI — à ne pas écrire dans le précis

- [ ] **Numéros d'article de `lf-2003` et `lf-2004`** (art. 65 et 37 selon la liste DGELF). La
      couche texte de ces deux fascicules porte un encodage de police décalé : déchiffrée, elle
      rend les **lettres** mais **efface les chiffres**. Les intitulés et le corps des articles
      ont été lus, les numéros non. À relire à l'image avant toute citation « art. n ».
- [ ] **`lf-1992` art. 44** : fascicule sans couche texte, seule la page 1 relue à l'image.
      Contenu inconnu.
- [ ] **Contenu** (positions, taux) des décrets **88-2002, 89-479, 89-1348** : jamais ouverts
      au-delà du sommaire. Comme pour `94-816`, `97-1368`, `2015-1768` et `loi-2007-70-lf-2008`,
      **aucun tarif ne doit être tiré de ces entrées** ; leur note le dit explicitement.
- [ ] **Dates d'effet** : déduites (1er janvier) pour les huit lois de finances, clause non lue ;
      **non établies** pour les six décrets.
- [ ] **Pages imprimées** des articles lus sur pièce (`lf-1995`, `lf-1997`, `lf-1999`, `lf-2013`) :
      non relevées ; le champ `page` porte le début de la loi.
- [ ] **TODO arabe — le compte passe de 15 à 29.** Les 14 entrées AR de cette passe portent, comme
      les 15 précédentes, un `title` et une `note` **en français** : c'est le motif établi du
      fichier, mais les intitulés arabes restent à relever sur les fascicules `Ja…`.

**Un titre à ne pas « corriger »** : `decret-2013-929-alcools` est intitulé **verbatim** comme le
JORT l'imprime — « numéros **22.3 à 22.8** du tarif des droits de **douanes** » — alors que les
autres textes de la série (décrets 97-1368, 2002-627, 2007-1977) écrivent « 22-03 à 22-08 ». La
divergence est celle du Journal officiel ; elle est consignée en note et n'est pas normalisée.

#### Handoff rédacteur

Les 14 clés sont **disponibles mais citées par personne** : le chapitre n'a pas été modifié
(interdit par la commande de clôture). Publier la chronologie complète du § 4.1 à la place des
« principales étapes » suppose une **passe rédacteur** qui insère les `@clé` et retire le
`<!-- TODO (bibliographe) -->` des lignes 197-202 de `_droits_consommation.qmd`.

#### Contrôles de clôture (16/09/2026)

- **Résolution hors livre** — c'est le seul test qui éprouve des clés non encore citées :
  `quarto pandoc --citeproc` sur les deux bibliographies de chaque langue, document `nocite`
  de **248 clés** FR et 248 AR → **zéro `[?]`, zéro `?@`**.
- **Rendu du livre** (`precis/fr/fiscalite`, `quarto render --to html`) : sortie créée,
  **0 `[?]`**. L'unique `?@` de `public/` est dans `site_libs/quarto-html/anchor.min.js`
  (bibliothèque de Quarto, pas une citation) — à savoir pour ne pas s'en alarmer.
- **`--verifier`** (hors ligne) : **361 entrées éprouvées, 0 perte de champ**.
- **`dry-run` local** (`env -u ZOTERO_API_KEY … --dry-run`) : **361 références, 361 à créer**,
  aucune `ValueError` de `csl_vers_zotero`. Il tourne **sans clé** : la récupération Zotero est
  gardée par `if args.pousser or api_key`. *Le lancer en local, et non par le workflow, est ici
  le seul choix utile : le workflow tourne sur `master` et ne verrait aucune des 14 clés.*
- **`controle-rangement` local** : il tourne lui aussi **sans clé** (le groupe 6529669 se lit en
  anonyme). Résultat : **333 références dans Zotero, 430 citations relevées** ; bien rangées 174 ;
  en défaut 147 clés distinctes ; **à déclasser 41**, **à ranger 108**, sans citation 12,
  **absentes de Zotero 38**. Rappel du défaut d'affichage **non commité** : `174+41+108+12`
  ne s'additionne pas à 333 parce que « à déclasser » et « à ranger » **se chevauchent**
  (2 clés rangées dans le mauvais livre y figurent deux fois) — ce n'est pas un défaut de
  classement.
- **Où tombent mes 14 clés : nulle part, et c'est normal.** Le contrôle ne voit que les clés
  **citées** ; les miennes ne le sont par personne (le chapitre n'a pas été modifié). Elles ne
  sont donc ni dans « sans citation » — ce panier ne parle que d'articles **présents dans
  Zotero** — ni dans « absentes de Zotero », qui ne parle que de clés **citées**. Elles
  n'apparaîtront qu'après la passe rédacteur.
- **Le panier « absentes de Zotero : 38 » décomposé** (recalculé clé par clé, pas déduit) :
  **14** sont les clés de la passe précédente, citées, avec entrée locale, en attente de
  rapatriement ; les **24 autres ne sont pas des références** mais des **étiquettes de renvoi
  Quarto** — `sec-rsna`, `tbl-bareme-irpp-2025`, `fig-effectifs-fp`… `cles_citees()` ramasse
  tout `@clé` sans distinguer un renvoi interne d'une citation bibliographique, ce qui **gonfle
  ce panier de 24**. Aucune de ces 24 n'est une citation morte : le rendu est à 0 `[?]`.
  *Piste de correction du script : écarter les préfixes `sec-`, `tbl-`, `fig-`, `eq-`.*
  Le diff local/Zotero, lui, donne **28 clés locales absentes de Zotero** = mes 14 + les 14
  d'hier (les 15 moins `loi-2018-56-lf-2019`, supprimée comme doublon). Les deux nombres
  comptent des univers différents ; aucun des deux ne signale de manque.

#### À pousser dans Zotero — NE PAS pousser sans feu vert (liste consolidée)

Toute clé ajoutée à la main est **provisoire** : la prochaine descente de `sync_biblio.py`
l'écrasera tant qu'elle n'est pas dans Zotero. **28 clés** sont dans ce cas :

- les **14 de cette passe** (tableau ci-dessus) ;
- les **14 de la passe précédente** : `loi-88-62-droit-consommation`, `loi-88-145-lf-1989`,
  `loi-89-115-lf-1990`, `loi-2007-70-lf-2008`, `decret-91-550-tarif-petroliers`,
  `decret-91-551-tarif-boissons`, `decret-94-816-hydrocarbures`, `decret-97-1368-regime-alcools`,
  `decret-99-894-tarif-petroliers`, `decret-gouv-2015-1768-annexes-alcools`, `dgi-nc-24-2007`,
  `dgi-nc-29-2007`, `dgi-nc-7-2016`, `dgi-nc-17-2018` ;
- **plus** les corrections de note/URL déjà listées plus haut (`lf-1991`, `lf-2014`, `lf-2016`,
  `lf-2018`, les 8 retraits d'URL arabes, `decret2019-454`).

Collection visée : « Fiscalité ». **`ranger` reste indispensable après tout envoi** : un article
créé par l'API arrive **sans collection**, et serait donc vu comme « commun » à la descente
suivante — c'est le mécanisme qui avait fait tomber le fonds commun à sept clés.

#### Observation à verser au dossier (défaut préexistant, cosmétique)

Le `dry-run` montre **96 entrées** dont l'`extra` porte **deux fois** la ligne `issue: <n>` : une
fois ajoutée par `csl_vers_zotero` (le type Zotero `statute` n'a pas de champ « issue », la
variable passe donc en Extra), une fois parce que la **note descendue de Zotero commence déjà**
par `citation-key: …` / `issue: …`. `csl_vers_zotero` déduplique `citation-key:` mais **pas**
`issue:`. **90 de ces 96 sont préexistantes** ; les entrées créées à la main reprennent le même
motif par cohérence.

**Ce n'est pas purement cosmétique : la duplication croît d'un cran à chaque cycle.** La descente
lit Zotero en `format=csljson`, export qui verse le champ **Extra dans le champ `note`** de
l'entrée CSL ; la note locale porte donc l'Extra complet, `issue:` compris. À la remontée
suivante, `csl_vers_zotero` retire les lignes `citation-key:` de la note mais **pas** les lignes
`issue:`, et en rajoute une. Chaque aller-retour pousse → descend → pousse ajoute donc une ligne
`issue:` de plus, sur 96 entrées. *Établi par lecture du code (`apply_extra_variables`,
`csl_vers_zotero`), non par un aller-retour réel — aucune écriture Zotero n'a été faite.*
Correctif suggéré : dédupliquer `issue:` comme `citation-key:` l'est déjà.

### Documents tirés des archives du web — convention et audit (22/09/2026)

Convention : `.claude/agents/bibliographe.md`, section « Documents tirés des archives du web ».
Champs `archive`, `archive_location`, `accessed` ; `push_biblio.py --verifier` : 403 entrées, 0 perte
(la perte `cnss-chiffres/accessed` est corrigée du même coup).

- [x] `eset2016` (fiscalité, FR et AR) : convention appliquée ; capture 20170109185021 vérifiée au CDX
  et consultée le 22/09/2026 ; domaine `eset.com.tn` inexistant. **Non cité** dans le livre.
- [ ] **Après fusion de `feat/retraites-pension-salaire`** (entrées absentes de `master`) :
  `cnrps-guides-rapports`, `ins-portail-2006-salaires-prive`, `ins-portail-2009-salaires-prive`
  (fichier `retraites`, FR et AR). Pour chacune : `URL` passe en `https://web.archive.org/web/…` ;
  `archive` = libellé de la langue du fichier ; `archive_location` = ce qui suit l'horodatage dans
  l'URL ; `accessed` = la date de consultation déjà portée par la note (21/09/2026 pour la CNRPS,
  22/09/2026 pour l'INS) ; une phrase de motif ajoutée à la note. Captures vérifiées au CDX le
  22/09/2026 : 20150106002250 (guide 2000-2010), 20190214182033 (guide 2010-2014),
  20220709151214, 20220709102723, 20220709000059, 20220709005355 (rapports 2016, 2017, 2018, 2020),
  20061129142926 et 20061129142343 (INS, FR), 20090713025533 (INS, AR).
- [ ] `fmi-1996-red`, `fmi-1997-selected-issues` : **hors convention** (page de l'éditeur servie aux
  lecteurs, 403 aux seuls robots) ; URL de l'éditeur conservée, capture citée en note.
- [ ] `cnrps-manuel-liquidation-2013` : **provenance non établie**. Aucune capture sur `cnrps.nat.tn`
  (CDX du domaine, avec et sans filtre de type) ; copie locale seulement. Pas d'URL tant que la
  source n'est pas retrouvée.
- [ ] À pousser dans Zotero, **sur feu vert** et une fois les scripts sur `master` : `corriger
  eset2016` (déjà dans Zotero : absent des 40 « à créer » du dry-run du 22/09/2026) et `corriger
  cnss-chiffres` (son `accessed` n'avait jamais atteint Zotero), puis les trois entrées retraites
  une fois fusionnées. Vérifier par `comparer` que l'API accepte `accessDate` au format
  `AAAA-MM-JJ` et que l'export csljson rend `archive_location` et `accessed`.
- [x] Le défaut « une ligne `issue:` de plus à chaque cycle » décrit plus haut (passe du 16/09/2026)
  est corrigé dans `csl_vers_zotero` : les lignes de la note déjà émises en Extra sont retirées
  (95 entrées dédoublonnées au prochain `corriger`/`pousser`).
- [ ] Limite connue : la phrase arabe ajoutée à la `note` des fichiers AR sera **écrasée** par la
  prochaine descente (`note` n'est pas dans `CHAMPS_TRADUITS`, et Zotero porte la note française).
  Le libellé visible `archive`, lui, est préservé (ajouté à `CHAMPS_TRADUITS`).
- [ ] Signalé à tunisia-data (non modifié) : `sources/cnrps-urls.csv` note `20220708232111` pour
  `ra_2016`, `ra_2017`, `ra_2019`, `ra_2020` ; ce n'est pas une capture mais l'horodatage demandé,
  que la Wayback redirige vers 20220709151214, 20220709102723, 20220709061458 et 20220709005355.
### Passe « Retraites — pension moyenne et salaire moyen des cotisants de la CNRPS » (21/09/2026) — À REPORTER DANS ZOTERO

Deux clés citées par le catalogue de `tunisia-data` (branche `feat/cnrps-pensions`, séries
`cnrps-pensions` et `bm1993-caisses`) et par `precis/fr/retraites/index.qmd`, **versées à la
main, identiques, dans `precis/fr/retraites/references.json` et `precis/ar/retraites/references.json`**.
Pas encore dans Zotero.

| Clé | Référence | Type | Collection Zotero cible |
|---|---|---|---|
| `cnrps-guides-rapports` | CNRPS, guides statistiques 2000-2010 et 2010-2014, rapports d'activité 2016, 2017, 2018, 2020 (en arabe) | report | Retraites |
| `bm-1993-social-protection` | Banque mondiale, *Republic of Tunisia. The Social Protection System*, rapport n° 11376-TUN, avril 1993 | report | Retraites — **candidate au fonds commun** : l'annexe couvre aussi la CNSS/CAVIS, les cotisations ou les prestations la citeront vraisemblablement |

Vérifié :

- [x] `bm-1993-social-protection` : titre, numéro, « April 1993 » et division lus sur la couverture
  du PDF ; recoupés par l'API du catalogue de la Banque mondiale (`search.worldbank.org/api/v2/wds`,
  guid 558471468337768900 : repnb 11376, docdt 1993-04-30, « Pre-2003 Economic or Sector Report »).
  URL du PDF : HTTP 200 le 21/09/2026. `issued` = 1993-04 (date imprimée), pas le jour du catalogue.
- [x] `cnrps-guides-rapports` : intitulés arabes lus sur les couvertures (« الدليل الإحصائي »,
  « تقرير النشاط » ; en-tête courant du rapport 2020 « التقرير السنوي للنشاط ») ; nom de la caisse
  en arabe et en français lu sur les couvertures ; six URL d'archive testées (HTTP 200, taille égale
  aux copies locales).

Reste :

- [ ] `cnrps-guides-rapports` n'a **pas d'`issued`** : ensemble de documents publiés de 2011
  (guide 2000-2010, « أكتوبر 2011 ») à une date non imprimée (rapport 2020). Le convertisseur ne
  porte que la première partie d'une plage de dates ; la période couverte est dans le titre.
- [ ] Le rapport 2016 archivé n'a pas de couverture ; le guide 2010-2014 et le rapport 2020 n'ont
  pas de date imprimée en couverture.
- [ ] `bm-1993-social-protection` porte le numéro de rapport en `genre` (passe en Extra) : même
  risque de duplication à chaque aller-retour que la ligne `issue:` décrite plus haut.
- [ ] Rapatriement Zotero (feu vert humain) puis `ranger` vers « Retraites ».

### Passe « Retraites — barème d'actualisation, prix et revenus » (21/09/2026) — À REPORTER DANS ZOTERO

Huit clés citées par l'entrée `croissances-revenus-prix` du catalogue de `tunisia-data` (branche
`main`), que `figtools.source_line()` rendra en `[@clé]` sous la figure du livre « Retraites » qui
compare le barème d'actualisation des salaires aux croissances des prix et des revenus. **Versées à
la main, identiques, dans `precis/fr/retraites/references.json` et `precis/ar/retraites/references.json`**
(aucune n'est un texte juridique : pas d'édition du JORT à distinguer).

| Clé | Référence | Type | Origine | Collection Zotero cible |
|---|---|---|---|---|
| `bct-ra` | BCT, *Rapport annuel* | dataset | copiée à l'identique du livre « Rémunérations publiques » | Retraites + Rémunérations publiques → **fonds commun** |
| `ins-fonction-publique-2021` | INS, *Caractéristiques des agents de la fonction publique et leurs salaires 2010-2021* | dataset | idem | idem |
| `minfin-remunerations` | Ministère des finances, répartition économique des dépenses (rémunérations publiques) | dataset | idem | idem |
| `ins-annuaire` | INS, *Annuaire statistique de la Tunisie*, éditions 1995-2001, 1998-2002, 1999-2003, 2019-2023 | report | nouvelle | Retraites |
| `ins-cnat-editions` | INS, *Les comptes de la nation*, 19 éditions 2001-2005 à 2021-2025 | report | nouvelle | Retraites |
| `undata-sna` | UNSD, *National Accounts Official Country Data*, tableau 4.1, Tunisie | dataset | nouvelle | Retraites |
| `ins-enpe` | INS, *Enquête nationale sur la population et l'emploi*, rapports 2005, 2010, 2012 | report | nouvelle | Retraites |
| `wb-wdi` | Banque mondiale, *World Development Indicators* | dataset | nouvelle | Retraites |

Vérifié (21/09/2026) :

- [x] Titres des publications de l'INS lus en couverture sur les PDF locaux de `tunisia-data`
  (`data/raw/…`) : annuaire 1995-2001 (« 2001, N° 44 », ISSN 0066-3689) et 2019-2023
  (« نشرية 65 », « Edition 2024 ») ; comptes de la nation 2001-2005 et 2021-2025 (« Base 2015,
  Edition 2026 ») ; enquête population-emploi 2005 (« أكتوبر 2006 »), 2010 (« جوان 2011 »), 2012
  (bilingue, « Décembre 2013 »). Éditions, tableaux et années d'emploi repris de
  `docs/croissances-revenus-prix.md` et de la colonne `source` du CSV traité.
- [x] URL : pages INS des éditions 2019-2023 (annuaire), 2021-2025 (comptes), 2012 (enquête) en
  HTTP 200 — ainsi que 1995-2001, 1998-2002, 1999-2003, 2001-2005, enquêtes 2005 et 2010, citées
  dans les notes ; page UNdata filtrée (année 1995) en 200 ; fiche du catalogue de données de la
  Banque mondiale en 200 (une fiche inexistante y rend 404 : ce n'est pas un 200 de complaisance).
- [x] UNdata : éditeur (« Statistics Division (UNSD) ») et « Last update in UNdata: 2025/10/14 »
  lus sur les pages conservées ; l'adresse de la base sans filtre répond 404.
- [x] WDI : libellés des indicateurs et « lastupdated »: « 2026-07-13 » lus dans les réponses de
  l'API conservées (`data/raw/banque-mondiale/`) ; téléchargement du 21/09/2026.
- [x] Résolution des huit clés contre `retraites/references.json` + `../references.json`, FR et AR,
  par `quarto pandoc --citeproc` : aucun avertissement (le même test signale bien une clé absente).
- [x] `push_biblio.py --verifier` : 410 entrées éprouvées (405 avant), 1 perte, **inchangée**
  (`cnss-chiffres`, `accessed`). Aucun `accessed` ni `number-of-pages` dans les nouvelles entrées :
  dates de consultation en `note`.

Reste :

- [ ] **Fonds commun.** `bct-ra`, `ins-fonction-publique-2021` et `minfin-remunerations` sont
  désormais dans deux fichiers de livre (Retraites, Rémunérations publiques). À la prochaine descente,
  `repartit_references` les promouvra au fonds commun (`precis/{fr,ar}/references.json`) et les
  retirera des deux livres, **à condition** que Zotero les porte dans les deux collections ; sinon la
  descente les laissera au seul livre « Rémunérations publiques » et la figure des retraites perdra
  ses sources. Laissées dans les fichiers de livre plutôt que déplacées à la main : les mettre au
  commun sans les retirer des « Rémunérations publiques » dupliquerait la clé sur le chemin de ce
  livre. Décision humaine : déplacement local maintenant, ou attente du rapatriement + `ranger`.
  Deux précédents de la même situation : `loi96-101`, `minfin-indicateurs-fp`.
- [ ] **Doublon possible** `ins-cnat-editions` / `ins-cnat-2015` (« Les Comptes de la Nation (base
  2015) », livre « Rémunérations publiques », URL `ins.tn/statistiques/153`). Même famille de
  publications, périmètres différents (dix-neuf éditions successives contre la seule base 2015) ; la
  note de `ins-cnat-editions` le dit. Fusion à trancher avant rapatriement.
- [ ] Pas d'`issued` sur les huit nouvelles (trois ensembles INS pluriannuels, deux bases mises à
  jour en continu) : les dates connues — parution de chaque édition, mise à jour des bases — sont
  en `note`. Même arbitrage que `cnrps-guides-rapports`.
- [ ] L'URL de `undata-sna` est une page filtrée sur une seule année (1995) : la base n'a plus
  d'adresse stable sans filtre.
- [ ] `wb-wdi` couvre aussi `SL.EMP.WORK.ZS`, que la colonne `source` du CSV cite mais qui n'est pas
  une des deux séries du PIB : dit dans la note.
- [ ] `dry-run` et `controle-rangement` non lancés localement (pas de `ZOTERO_API_KEY` dans cet
  environnement) ; à déclencher dans le workflow `biblio-zotero` une fois la branche poussée — sur
  `master`, ils ne verraient pas ces entrées.
- [ ] Rapatriement Zotero (feu vert humain) puis `ranger` : cinq nouvelles vers « Retraites », les
  trois partagées à ajouter à « Retraites » (elles restent dans « Rémunérations publiques »).

## Fusion `ins-cnat-editions` → `ins-cnat-2015` (21/09/2026)

Les deux clés désignaient les éditions successives des *Comptes de la nation* de l'INS. La clé
conservée est `ins-cnat-2015`, déjà citée dans le texte du livre « Rémunérations publiques », en
français et en arabe ; elle prend le contenu, plus complet, de l'ancienne `ins-cnat-editions`
(dix-neuf éditions, 2001-2005 à 2021-2025, toutes bases). Citée par deux livres, elle est
versée au fonds commun (`precis/{fr,ar}/references.json`) et retirée des fichiers de livre. Le
catalogue de tunisia-data a suivi (PR #8). À rapatrier dans Zotero : une seule entrée, dans les
collections « Rémunérations publiques » et « Retraites » ; supprimer `ins-cnat-editions` si elle
y a été créée.

## Passe « Retraites — salaires du secteur privé (INS, CNSS) » (22/09/2026) — À REPORTER DANS ZOTERO

Trois clés nouvelles de la série `croissances-revenus-prix` de tunisia-data, rendues en `[@clé]`
par `figtools.source_line()` dans une figure du livre « Retraites ». Versées dans
`precis/{fr,ar}/retraites/references.json`, identiques en FR et en AR (aucune n'est un texte
juridique) :

- [x] `ins-bms` — INS, *Bulletin mensuel de la statistique*, collection des 213 numéros en ligne
  (novembre 2008 à juillet 2026), tableau 2.2, renvoi « Salaire dans le secteur privé non
  agricole ». Type `report`, **sans `issued`** (collection ; même arbitrage que `ins-annuaire`,
  `ins-enpe`). URL : page du numéro de juillet 2026 ; page du portail `ins.tn/statistiques/99`,
  liste des captures d'archive et `sources/ins-bms-urls.csv` en `note`. Pages des numéros de
  novembre 2008 et juillet 2026, leurs PDF, `ins.tn/publication`, `ins.tn/statistiques/99` et la
  capture du 18/06/2025 : HTTP 200 le 22/09/2026.
- [x] `ins-guide-salaires-prive-2026` — titre lu en tête du document, sur trois lignes (« Taux
  d'évolution trimestriel des salaires » / « Guide méthodologique pour le calcul du taux
  d'évolution trimestriel des salaires » / « Secteur privé non agricole »), 4 pages. `issued`
  2026-08-10.
- [x] `wb-2004-employment-strategy-annexes` — sur le modèle de `bm-1993-social-protection` :
  `genre` « Report No. 25456-TUN », `issued` 2004-05-28 (couverture « May 28, 2004 », confirmée
  par le catalogue de la Banque mondiale : « Tunisia - Employment strategy (Vol. 2 of 2) :
  Annexes », rapport 25456). Tableau 8.1 relu à l'image, page 39 du PDF (90 p.).

Reste :

- [ ] **Date du guide non imprimée.** `2026-08-10` vient des métadonnées du PDF (création le
  10/08/2026), concordantes avec le répertoire `2026-08` de l'URL et la mise à jour du 10/08/2026
  affichée sur `ins.tn/statistiques/99` ; dit dans la `note`. À ramener à `2026-08` si l'on
  n'admet que les dates imprimées.
- [ ] Le tableau 8.1 de la Banque mondiale s'intitule « 1994-2001 » mais s'arrête à 2000 ; la couche
  texte du scan est fautive (750 363 lu 150 363) : dit dans la `note`.
- [ ] **Clés invisibles au `controle-rangement`.** `push_biblio.cles_citees` ne lit que les `.qmd` et
  `tables/*.md` ; les clés rendues par `figtools.source_line()` n'y figurent pas. Les trois clés de
  cette passe, et `bct-ra`, `ins-annuaire`, `undata-sna`, `ins-enpe`, `wb-wdi`, sont donc classées
  « sans citation » ou « absentes de Zotero », jamais « à ranger ». Le contrôle ne dira pas si leur
  rangement dérive. Correction de l'outil à décider (lire les `sources` du catalogue des séries
  citées par les figures du livre).
- [ ] Rapatriement Zotero (feu vert humain) puis `ranger` : les trois clés vers « Retraites ».

Contrôles (22/09/2026) : `push_biblio.py --verifier` : 412 entrées, 1 perte, la même qu'avant
(`cnss-chiffres`, `accessed`) : aucune perte nouvelle. `quarto pandoc --citeproc` contre
livre + fonds commun, FR et AR : les trois clés résolvent. `--dry-run` (sans clé : ne compare
pas à Zotero, annonce 412 à créer) : conversion des 412 sans erreur, les trois en `report`.
`--controle-rangement` : 363 références dans Zotero, 347 bien rangées, 2 à déclasser
(`loi96-101` : retirer cotisations_sociales, prestations_sociales ; `minfin-indicateurs-fp` :
retirer fiscalite), 0 à ranger, 14 sans citation, 16 absentes de Zotero.

## Passe « Retraites — premier portail de l'INS, salaires du privé 2001-2009 » (22/09/2026) — À REPORTER DANS ZOTERO

Deux clés citées par la série `croissances-revenus-prix` de tunisia-data (fiche
`sources/ins-bms-salaires-prive.md`), rendues en `[@clé]` par `figtools` dans les figures
`fig-bareme-taux` et `fig-bareme-recent` du livre « retraites ». Versées dans
`precis/{fr,ar}/retraites/references.json`, après `ins-guide-salaires-prive-2026` (livre seul
utilisateur : pas de fonds commun).

- [x] `ins-portail-2006-salaires-prive` — page française du premier portail (www.ins.nat.tn),
  « Données Conjoncturelles » > « Données sur les Salaires », indicateur 0402040, intitulé lu sur la
  page brute (windows-1256) : « Taux d’évolution trimestriel du salaire moyen dans le secteur privé
  non agricole ». Type `webpage` ; `container-title` « Institut National de la Statistique -
  Tunisie (www.ins.nat.tn) » ; `issued` 2006-10-06 (« Date de mise à jour : 06-10-2006 ») ; URL :
  capture du 29/11/2006. Identique en FR et en AR.
- [x] `ins-portail-2009-salaires-prive` — page arabe, même indicateur, « تاريخ آخر تحيين:
  30-06-2009 » → `issued` 2009-06-30 ; URL : capture du 13/07/2009.
  **Arbitrage de présentation** (page qui n'existe qu'en arabe) : on suit les précédents du livre
  (`ins-enpe`, `cnrps-guides-rapports`) et `cherif-kammoun-tajir` (suffixe « [en arabe] ») :
  - fichier **FR** : `title` = traduction littérale, « Taux d'évolution trimestriel des salaires
    dans le secteur privé non agricole [en arabe] » ; la `note` cite l'intitulé original
    « نسبة التطور الثلاثي للأجور في القطاع الخاص الغير الفلاحي », dit que le titre français en est
    la traduction, et rappelle l'intitulé officiel français du même indicateur en 2006 ;
  - fichier **AR** : `title` = l'intitulé original arabe, `container-title` « المعهد الوطني
    للإحصاء - تونس (www.ins.nat.tn) » ; le reste (auteur, `title-short`, note, URL, date) est le
    miroir du FR. Ces deux champs sont dans `CHAMPS_TRADUITS` de `sync_biblio.py` : contenant de
    l'arabe, ils survivent à la descente depuis Zotero, qui recevra le titre français (la montée ne
    lit que le FR).
- Pas d'`accessed` : consultation (22/09/2026) et vérification HTTP dans la `note`.

Contrôles (22/09/2026) : les deux URL d'archive répondent HTTP 200 sans redirection (19 990 et
21 494 octets) ; la liste CDX
(`http://web.archive.org/cdx/search/cdx?url=ins.nat.tn&matchType=domain&filter=original:.*0402040.*`)
ne compte que ces deux captures. `push_biblio.py --verifier` : 414 entrées, 1 perte, la même
qu'avant (`cnss-chiffres`, `accessed`) : aucune perte nouvelle. `quarto pandoc --citeproc` contre
livre + fonds commun, FR (`precis.csl`) et AR : les deux clés résolvent. `--dry-run` (sans clé :
annonce 414 à créer) : conversion sans erreur, les deux en `webpage` (`websiteTitle`, `date`).
`--controle-rangement` : inchangé — 363 dans Zotero, 347 bien rangées, 2 à déclasser (`loi96-101`,
`minfin-indicateurs-fp`), 0 à ranger, 14 sans citation, 16 absentes de Zotero ; les deux clés
neuves n'y apparaissent pas (clés de figure invisibles à `cles_citees`, voir la passe précédente).

Reste :

- [ ] Rapatriement Zotero (feu vert humain) puis `ranger` : les deux clés vers « Retraites ».
- [ ] Traduction du titre de 2009 faite ici, non publiée par l'INS : à revoir par le terminologue si
  l'on préfère reprendre l'intitulé français de 2006 (« du salaire moyen »), qui n'est pas celui
  de la page arabe (« للأجور », des salaires).

## Passe « Retraites — salaires par secteur 1981-1996 et couverture 1989-1999 » (22/09/2026) — À REPORTER DANS ZOTERO

Trois clés de tunisia-data (`main` à 5036761). Les deux premières sont citées par la série
`croissances-revenus-prix`, rendue en `[@clé]` par `figtools` dans une figure du livre
« retraites » ; la troisième (`bit2002_couverture_1989_1999`) n'est lue par aucune figure du livre
à ce jour : **versée par avance**, pour une figure à venir — ce n'est pas une entrée orpheline.
Versées dans `precis/{fr,ar}/retraites/references.json`, après
`wb-2004-employment-strategy-annexes` (livre seul utilisateur : pas de fonds commun). Entrées
identiques en FR et en AR (aucun texte du JORT, aucune source en arabe). Champs calqués sur
`bm-1993-social-protection` : ni `DOI`, ni ISBN, ni `number-of-pages`, ni `accessed` — ces
données sont dans la `note`.

- [x] `bm-1995-pauvrete-annexes` — Banque mondiale, rapport n° 13993-TUN, vol. II : Annexes,
  août 1995 (mois seul : la couverture ne donne pas de jour, et le catalogue en donne deux, le 1er et le 31).
  Titre relu sur la couverture à 300 dpi : **« Allégement »**, et non « Allègement » (la fiche
  `sources/bm-1995-pauvrete-annexes.md` de tunisia-data et la commande disaient « Allègement »).
  Tableaux 39-41, p. 117-119 du PDF. URL : HTTP 200, 11 961 326 octets, identique au PDF local.
- [x] `fmi-1997-selected-issues` — `citation_title` « Tunisia: Selected Issues »,
  `citation_publication_date` 1997/07/25, `citation_author` « International Monetary Fund »,
  DOI 10.5089/9781451837742.002.A001 (relus dans le HTML local). **Réserve** : la chaîne « 97/57 »
  n'apparaît ni sur la page ni dans la capture d'archive, et Crossref ne donne ni volume ni numéro ;
  la page de titre du PDF, `cr9757.pdf` de l'ancien site du FMI et l'aperçu `previewpdf` rendent
  HTTP 403 : non lus. Le `genre` reprend donc la forme lue, « IMF Staff Country Reports, vol. 1997,
  n° 057 », et « No. 97/57 » ne figure que dans la `note`, comme forme usuelle de citation. La page d'origine
  rend 403 elle aussi, y compris par le DOI. **Capture d'archive vérifiée** (contrairement à ce
  que dit la fiche de tunisia-data, « Internet Archive hors ligne ») : HTTP 200 sans redirection,
  3 404 920 octets, mêmes `citation_title` et DOI, tableau 5 présent. Elle est citée dans la `note` ;
  l'`URL` reste la page d'origine.
- [x] `chaabane-2002-ess4` — BIT, Mohamed Chaabane, page de titre « ESS Paper No 4 » (notice
  catalographique : « Working Paper No.4 », ISBN 92-2-113067-3, ISSN 1020-9581), Genève,
  « First published 2002 ». Annexe III p. 32 du PDF (p. 28 imprimée). URL : HTTP 200,
  247 085 octets, identique au PDF local.

Contrôles (22/09/2026) : `push_biblio.py --verifier` : 417 entrées, 1 perte, la même qu'avant
(`cnss-chiffres`, `accessed`) : aucune perte nouvelle. `quarto pandoc --citeproc` contre
livre + fonds commun, FR (`precis.csl`) et AR : les trois clés résolvent. `--dry-run` (sans clé :
annonce 417 à créer) : conversion des 417 sans erreur, les trois en `report`.
`--controle-rangement` : inchangé — 363 dans Zotero, 347 bien rangées, 2 à déclasser (`loi96-101`,
`minfin-indicateurs-fp`), 0 à ranger, 14 sans citation, 16 absentes de Zotero. **Ces chiffres ne
couvrent pas les trois clés neuves** : des clés portées par les figures, `cles_citees` ne voit rien
(voir plus haut). « 0 à ranger » ne dit donc rien de leur rangement.

Reste :

- [ ] Rapatriement Zotero (feu vert humain) puis `ranger` : les trois clés vers « Retraites ».
- [ ] `fmi-1997-selected-issues` : lire la page de titre du PDF (navigateur) ; si elle porte
  « IMF Staff Country Report No. 97/57 », passer le `genre` à cette forme (FR et AR) ; corriger la fiche de tunisia-data (capture d'archive
  vérifiée le 22/09/2026) — hors du périmètre de cette passe.
- [ ] `bm-1995-pauvrete-annexes` : aligner la fiche de tunisia-data sur « Allégement ».

## Passe « Retraites — pension et salaire : sources anciennes » (22/09/2026) — À REPORTER DANS ZOTERO

Six clés pour la figure `precis/fr/retraites/figures/pension_salaire.py` et la note
`docs/notes/series-pensions-salaires-bilan.md`. **Aucune n'est encore citée** (ni prose, ni
tableau, ni catalogue de tunisia-data) : versées par avance, pour des séries à venir — ce ne sont
pas des entrées orphelines. Aucune n'existait sous une autre clé (recherche par id, titre, auteur
et éditeur dans tous les `references.json` ; la seule entrée du BIT est `chaabane-2002-ess4`,
autre ouvrage). Versées dans `precis/{fr,ar}/retraites/references.json`, après
`chaabane-2002-ess4`, identiques en FR et en AR (aucun texte du JORT, aucune source en arabe).
Champs calqués sur `bm-1993-social-protection` et `fmi-1997-selected-issues` : ni ISBN, ni
ISSN, ni édition, ni `number-of-pages`, ni `accessed` — `csl_vers_zotero` ne porte que les
champs de `CHAMPS` et laisserait tomber les autres sans rien dire ; ces données sont dans la `note`.

| Clé | Référence | Type | Collection Zotero cible |
|---|---|---|---|
| `bm-1990-cem-8044-vol1` | Banque mondiale, *Country Economic Memorandum: The Road to an Outward-Oriented Economy*, rapport n° 8044-TUN, vol. I : Main Report, mars 1990 | report | Retraites |
| `bm-1990-cem-8044-vol5` | idem, vol. V : Annex 4, Statistical Annexes, mars 1990 | report | Retraites |
| `fmi-1996-red` | FMI, *Tunisia: Recent Economic Developments*, IMF Staff Country Reports, vol. 1996, n° 027, 7 mai 1996 | report | Retraites |
| `vittas-1993-wps1154` | Dimitri Vittas, *Options for Pension Reform in Tunisia*, Policy Research Working Paper WPS 1154, juillet 1993 | report | Retraites — **candidate au fonds commun** si les cotisations le citent |
| `bit-yearbook-1985` | BIT, *Year Book of Labour Statistics / Annuaire des statistiques du travail*, 45e édition, 1985 | book | Retraites |
| `bit-yearbook-1999` | BIT, *Yearbook of Labour Statistics / Annuaire des statistiques du travail*, 58e édition, 1999 | book | Retraites |

**Une clé par volume, et non `bm-1990-cem-8044` pour l'ensemble** (écart avec la commande) : la
Banque mondiale catalogue chaque volume sous un identifiant, un rang (« Vol. 1 of 5 », « Vol. 5 of
5 ») et un PDF propres ; une entrée CSL ne porte qu'une `URL`, et une clé unique aurait renvoyé
l'un des deux volumes en note. Même forme que `bm-1995-pauvrete-annexes`, clé du seul volume II.

Vérifié (22/09/2026) :

- [x] `bm-1990-cem-8044-vol5` : titre, « Report No. 8044-TUN », « March 1990 », « Country
  Operations Division, Country Department II, Europe, Middle East and North Africa Region » lus à
  l'image sur la couverture (la commande disait « EMENA » : forme développée de la couverture
  retenue). Catalogue (API `search.worldbank.org/api/v3/wds`, guid 919691468337762945) : rapport
  8044, vol. 5 de 5, daté du 31/03/1990 ; `issued` = 1990-03. Tableaux 2.4 (p. 25 du PDF) et 10.2
  (p. 91). PDF : HTTP 200, 3 289 753 octets, sha1 identique à `wb_1990_8044_cem_c.pdf`.
- [x] `bm-1990-cem-8044-vol1` : **le PDF du volume I s'ouvre sur la couverture du volume III**
  (vu à l'image). Identification par le catalogue (guid 162381468313479177, « Vol. 1 of 5 : Main
  report ») et par le contenu (paragraphe de mission, « author of the main report » ; tableaux 1 à
  19). Tableau 6 « Wages and Prices: 1980-84 » lu à l'image (p. 7 imprimée, p. 26 du PDF ; l'OCR
  de la table des tableaux écrit « 1985-1984 »). PDF : HTTP 200, 6 409 044 octets, sha1 identique
  à `wb_1990_8044_cem_a.pdf` — que le nom de fichier de tunisia-data ne rattache à aucun volume ; la
  couverture trompeuse est dite dans la `note`, pour que personne ne « corrige » le titre.
- [x] `fmi-1996-red` : `citation_title`, `citation_publication_date` 1996/05/07,
  `citation_author`, DOI 10.5089/9781451837735.002.A001, eISBN 9781451837735, relus dans le HTML
  local de tunisia-data (copie de la page, sans marque d'archive) **et** dans la capture d'archive
  du 15/06/2025 (HTTP 200, 2 264 273 octets, mêmes métadonnées, tableau 21 « Wage and Employment
  Indicators, 1990–95 » présent). Page d'origine : HTTP 403 aux accès automatisés. **DOI en champ**
  (le type Zotero `report` a un champ `DOI`, vérifié sur le schéma ; l'aller-retour ne le perd pas),
  alors que `fmi-1997-selected-issues` ne le porte qu'en `note`. « No. 96/27 » seulement en `note`.
- [x] `vittas-1993-wps1154` : titre, auteur, collection, « Financial Sector Development
  Department », « July 1993 », « WPS 1154 » lus à l'image sur la couverture. Catalogue (guid
  297941468781762735) : WPS1154, 31/07/1993 ; `issued` = 1993-07. PDF : HTTP 200, 2 343 945 octets,
  sha1 identique à la copie locale.
- [x] `bit-yearbook-1985` / `-1999` : couvertures et versos lus à l'image. 1985 : « 45th issue »,
  « Year Book » en deux mots, ISBN 92-2-005297-0 (relié) et 92-2-005298-9 (broché), ISSN
  0084-3857, « Printed in Switzerland ». 1999 : « 58th issue », « Yearbook » en un mot, « The set of
  2 volumes », ISBN 92-2-007358-7, « Printed in France ». Tableaux : 1985, tableau 22 partie A
  « Labour cost in manufacturing — All industries », p. 737 ; 1999, tableau 6A « Labour cost in
  manufacturing », p. 1003 — la même série, renumérotée. URL : HTTP 200, tailles égales aux PDF
  locaux (75 970 741 et 71 280 029 octets).

Contrôles (22/09/2026) : `push_biblio.py --verifier` : 423 entrées, 1 perte, la même qu'avant
(`cnss-chiffres`, `accessed`). `quarto pandoc --citeproc` contre livre + fonds commun, FR
(`precis.csl`) et AR : les six clés résolvent (une clé témoin inexistante est bien signalée).
`--dry-run` (sans clé : annonce 423 à créer) : conversion des 423 sans erreur, quatre `report` et
deux `book`, DOI porté sur `fmi-1996-red`. `--controle-rangement` : inchangé — 363 dans Zotero,
347 bien rangées, 2 à déclasser (`loi96-101`, `minfin-indicateurs-fp`), 0 à ranger, 14 sans
citation, 16 absentes de Zotero. Ces chiffres ne disent rien des six clés : aucune n'est citée.

Reste :

- [ ] Rapatriement Zotero (feu vert humain) puis `ranger` : les six clés vers « Retraites ».
- [ ] ISSN de l'édition de 1999 imprimé « 0084-5857 », clé de contrôle fausse (celle de 1985,
  0084-3857, est juste) : non repris ; à confirmer au catalogue du BIT si l'on veut l'ajouter.
- [ ] `fmi-1996-red` : lire la page de titre du PDF (navigateur) ; si elle porte « IMF Staff Country
  Report No. 96/27 », passer le `genre` à cette forme (FR et AR), comme pour
  `fmi-1997-selected-issues`. Aligner les deux entrées du FMI sur le DOI : en champ ici, en `note`
  seulement pour 1997 — à trancher.
- [ ] Usage à préciser dans les `note` quand les séries seront écrites : la commande ne dit pas
  quels tableaux de `fmi-1996-red` et `vittas-1993-wps1154` seront lus (le tableau 21 du FMI est
  signalé comme pertinent, sans plus).
- [ ] tunisia-data : les fichiers `wb_1990_8044_cem_{a..e}.pdf` ne disent pas quel volume ils
  portent (a = vol. I sous couverture du vol. III, c = vol. V, e = vol. III ; b = vol. IV,
  d = vol. II d'après leurs couvertures) — à consigner dans la fiche source.
## Livre « Retraites » — éléments permanents soumis à retenue (passe bibliographe du 22 septembre 2026)

Source : `docs/notes/retraites-elements-permanents.md` (§ 2.2, § 3). Ajoutées à la main dans
**`precis/fr/references.json` et `precis/ar/references.json`** (fichier commun, comme les
décrets de base `decret85-980`, `decret85-1176` et les autres décrets de retraite
`decret74-499`, `decret89-107`… ; la note proposait le fichier du livre, qui ne porte que cinq
clés à tiret). **Pas encore dans Zotero.** Aucune n'est encore citée par un `.qmd`.

Chaque URL vient de l'enregistrement `jort_cache.db` du texte (identifié par numéro exact et date
de signature ; pour 2024-2, par date et intitulé) : `pdf_fr` pour le fichier FR, `pdf_ar` pour le
fichier AR, confrontée au tableau § 3.1 de la note — concordance totale, sauf 2019-482 (ci-dessous).
Les 76 URL distinctes répondent `200 application/pdf` (HEAD, 22/09/2026).

- [x] **41 clés créées (FR et AR)** : `decret86-784`, `decret87-771`, `decret88-1102`,
  `decret88-1443`, `decret89-1082`, `decret90-1250`, `decret90-1985`, `decret90-2007`,
  `decret91-812`, `decret91-1028`, `decret91-1333`, `decret92-2`, `decret92-1629`,
  `decret93-929`, `decret93-1126`, `decret93-1929`, `decret93-2170`, `decret93-2444`,
  `decret94-1392`, `decret94-2409`, `decret94-2581`, `decret95-2432`, `decret96-1`,
  `decret96-1654`, `decret97-1207`, `decret98-1301`, `decret2002-2084`, `decret2002-3015`,
  `decret2006-1801`, `decret2007-2590`, `decret2008-3471`, `decret2011-1015`,
  `decret2014-1386`, `decret2015-2723`, `decret2017-428`, `decret2017-458`, `decret2017-459`,
  `decret2017-1368`, `decret2017-1374`, `decret2019-482`, `decret2024-2`.
- [x] **Notes mises à jour** (FR et AR) : `decret85-980`, `decret85-1176` — « Métadonnées
  seules » remplacé par le contenu lu à l'image (§ 3.3 de la note) ; pour `decret85-980`, la
  mention « Assiette de liquidation de la pension (art. 10 et 36 de la loi 85-12) » est conservée.

### TODO de vérification

- [ ] **`decret2019-482`, URL française** : `jort_cache.db` n'a **aucun `pdf_fr`** pour le
  JORT n° 45-46 de 2019 (seul `pdf_ar` = `/jort/2019/2019A/Ja0462019.pdf`). *Mise à jour : l'URL
  ci-dessous a depuis été portée dans l'entrée FR, sur vérification du fichier servi ; reste à
  compléter la notice `jort_cache` ou à entériner l'exception.* Or `https://www.pist.tn/jort/2019/2019F/Jo0462019.pdf` répond (200, PDF) et a la
  taille exacte du fascicule français local lu par la documentaliste (916 541 octets ; revérifié le 22/09/2026). À lever par
  l'humain : soit compléter la notice `jort_cache`, soit accepter l'URL vérifiée hors base.
- [ ] **`decret2017-1368`, intitulé français** : l'édition française du JORT n° 103 de 2017
  n'existe pas (404 ; `pdf_fr` vide en base). L'entrée FR est **sans URL** ; l'intitulé français
  est une construction de la documentaliste sur le modèle des autres modificatifs (la note de
  l'entrée le dit : « Intitulé français non publié : à valider »). Intitulé officiel arabe
  (notice `jort_cache`) : « يتعلق بإتمام الأمر عدد 1176 لسنة 1985 … ». Pagination (p. 4553) de
  l'édition arabe.
- [ ] **Pagination arabe** : les entrées AR reprennent la pagination française (usage du fichier).
  Elle coïncide avec les pages de la notice `jort_cache` pour 37 des 41 textes ; la notice n'a pas
  de pages pour 2017-1368 et 2017-1374, donne pour 2019-482 une pagination arabe distincte, et
  porte `0208-0208` pour 2024-2 là où le fascicule lu donne pp. 208-209 (lecture du fascicule
  retenue).
  Pagination arabe **relevée** seulement pour 2019-482 (`1737-1738`, notice `jort_cache` ; p. 1737
  lue au sommaire) et 2017-1368 (4553). Non vérifiée ailleurs, en particulier pour 2002-2024.

### Rapatriement Zotero (feu vert humain requis)

Les 41 clés + les deux notes corrigées, par la séquence `permissions` → `verifier` → `dry-run` →
`pousser-un` → `comparer` → `pousser-tout` → **`ranger`**. Rangement : aucune n'est citée à ce
jour, donc `controle-rangement` ne prend pas position (« sans citation »). Dès que la
sous-section « Les éléments soumis à retenue » les citera, `ranger` les rattachera à la
collection du ou des livres citants — si le seul livre citant est « Retraites », elles
descendront au prochain `sync` dans `precis/{lang}/retraites/references.json` et non plus dans
le fichier commun. À garder en tête pour ne pas créer de doublon d'`id` entre les deux fichiers.

### Passe « clôture » (22 septembre 2026) — textes nommés sans clé

Contrôle d'unicité préalable (numéros cherchés dans tous les `references.json` et `.bib`) : aucune
entrée préexistante. URL : `pdf_fr` / `pdf_ar` lus sur le même enregistrement `jort_cache.db`,
servis par pist.tn (`curl -k`, `200 application/pdf`) avec la taille exacte des fascicules locaux.
Intitulés arabes relevés **à l'image** des fascicules arabes (OCR `ara` pour localiser, lecture de
l'image pour transcrire, orthographe du fascicule conservée).

- [x] **4 clés créées (partagé FR + AR)** :
  - `decret88-1442` — recid 94274 ; JORT n° 54/1988, FR p. 1140, AR pp. 1126-1127 ; art. 3 lu.
  - `decret2000-241` — recid 88341 ; JORT n° 12/2000, FR p. 397, AR pp. 399-400 ; art. 2 lu.
    **URL AR `2000A/Ja01200.pdf`** (valeur du champ `pdf_ar`, conforme à l'anomalie de nommage de
    l'an 2000, `outillage-sources.md` § 3) : la dérivation `url_jort` de `sync_biblio.py`
    produirait `Ja0122000.pdf`, qui répond **404**, et `sans_homologue` ne couvre pas ce cas.
    **TODO outillage** : à la prochaine descente Zotero, l'URL AR de cette entrée sera fausse.
  - `decret2007-2009` — recid 83316 ; JORT n° 65/2007, FR pp. 2764-2766, AR pp. 2932-2934 ;
    **édition française lue** (couche texte) : art. 2, 4, 5 et **8** (voir ci-dessous).
  - `decret2021-476` — recid 162129 ; JORT n° 55/2021, FR pp. 1667-1669, AR pp. 1742-1744 (la
    notice donne « 1667-1667 ») ; art. 4 lu en français.
- [x] **`decret81-437` (AR)** : intitulé arabe relevé (p. 882), pagination arabe 882-884.
- [x] **`decret88-1443` (AR)** : pagination arabe p. 1127 (au lieu de la française). **Divergence de
  date** : l'édition arabe date le décret du **14 juillet 1988** (intitulé et formule finale), la
  française et `jort_cache` du 28 juillet. `issued` non modifié ; **à trancher par l'humain**.
- [ ] **Non créés, faute de lecture** : décrets n° 82-504 et 82-515 (recid 97550, 97560 ; JORT
  n° 20/1982, pp. 691 et 697) ; n° 81-444 (recid 98243), qui n'est d'ailleurs pas nommé dans la prose.
- [ ] **TODO arabe restants** : `decret82-501`, `loi93-64`, `decret88-1443` et les 41 modificatifs
  portent un intitulé français dans le fichier AR ; pagination arabe non relevée pour la plupart
  (le cas 88-1443 montre qu'elle diffère).
- **Pour le rédacteur/documentaliste** : l'art. 8 du décret n° 2007-2009 (édition française)
  exclut aussi les **indemnités de représentation** des présidents de communes, premiers
  adjoints, adjoints et vice-présidents de la retenue « au titre de la cotisation aux régimes de
  la sécurité sociale » — troisième exclusion expresse, que la prose (« La seule exclusion expresse
  identifiée… », « D'après son texte arabe ») ne mentionne pas.

Rapatriement Zotero : ajouter ces 4 clés à la liste des 41 (même séquence, feu vert requis).

Contrôles de clôture (local, sans clé Zotero, rien poussé) : `--dry-run` 448 entrées converties
sans `ValueError` (sans clé, le groupe n'est pas lu : « à créer » n'est pas un décompte) ;
`--controle-rangement` 363 références dans Zotero, 472 citations, 347 bien rangées, à déclasser 2
(`loi96-101`, `minfin-indicateurs-fp`), à ranger 1 (`loi93-64` → retraites), sans citation 13,
absentes de Zotero 55.

- [ ] **`--verifier` : 1 perte de champ**, antérieure à cette passe — `cnss-chiffres`, champ
  `accessed` envoyé (`2026-09-18`) mais non relu. N'interrompt pas la conversion ; à corriger avant
  `pousser-tout`.
- [ ] **Rangement et descente** : une fois `loi93-64` rangée dans « retraites » (et les 41 + 4 clés
  poussées et citées par ce seul livre), la descente les écrira dans
  `precis/{lang}/retraites/references.json` ; les retirer alors du fichier commun, sans quoi l'`id`
  sera en double.

## Pagination arabe (23/09/2026)

- [x] `loi59-18` (AR) : 93-100 → 132-143 (édition arabe, JORT n° 8/1959, lue à l'image par le terminologue).
- [x] `decretloi70-1` (AR) : 1186-1187 → 1300-1301 (édition arabe, JORT n° 43/1970).
- [ ] `loi81-70` (AR) : porte encore la pagination française (1789-1798) sur l'URL du fascicule arabe. Seules les pp. 1889-1890 de l'édition arabe (art. 4) ont été lues : établir l'étendue complète de la loi dans l'édition arabe avant de corriger.
- [ ] Même défaut probable pour d'autres entrées AR du fonds commun dont la pagination vient de `jort_cache` (qui donne la pagination française).
