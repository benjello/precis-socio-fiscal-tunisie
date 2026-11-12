# Élucidation — les « fonds spéciaux » du soutien à l'investissement agricole (FOSDA / FOSDAP / FSPA)

Rôle : documentaliste. Date : 10 novembre 2026. Livre : « L'agriculture — le soutien au producteur ».
Objet : trancher par les textes la divergence posée entre la note *investissement*
(`agriculture-investissement-documentation.md`, §2 et §6) et la note *budget*
(`agriculture-budget-documentation.md`, §7), reprise en lacune transversale par
`agriculture-synthese-documentaire.md` §4.2 et §7, sur ce que désigne le sigle **FOSDAP** et quel
texte crée le fonds qui porte les primes d'investissement de l'APIA.

Sources dépouillées : `PDFs-legislation-tunisie/jort_cache.db` (79 790 notices, dernière publication
indexée ≈ avril 2026) — requêtes LIKE sur titres FR **et** AR ; corpus local des fascicules
(texte extrait par `pdftotext -layout`) ; **décret gouvernemental n° 2017-389** (fascicule JORT
n° 25/2017, couche texte lue) ; **PAP 2022** de la mission Agriculture (tunisia-data) ; et —
pièce décisive trouvée en cours de fouille — le **Rapport sur l'activité des Fonds Spéciaux**
du ministère des Finances, **annexe 10 au projet de loi de finances 2020** (gbo.tn), qui décrit
chaque fonds spécial du Trésor, son objet et **son texte créateur**. Ce rapport est rangé dans
`tunisia-data/data/raw/gbo/Annexe_10_LF2020-Fonds_Speciaux.pdf`
(SHA-256 `2bb81c13b2a554b5e997364abab6a6883b02c2b026cb3a81a0cd7ddd2f1d967a`, 130 p., collecté le
10/11/2026 ; catalogue `sources/gbo-fonds-speciaux-rapport-urls.csv`).

---

## 0. Le texte qui ferme le débat (preuve littérale)

**a) Décret gouvernemental n° 2017-389 du 9 mars 2017** (incitations financières de la loi de
l'investissement), JORT n° 25 du 2017, pp. 1098-1125 — **art. 27** (dispositions transitoires,
couche texte lue au fascicule) :

> « Jusqu'à l'exercice du fonds tunisien de l'investissement de ses missions, les primes, les
> participations et les prêts fonciers agricoles sont imputés sur : — **les ressources du fonds
> spécial pour le développement de l'agriculture** pour les investissements réalisés dans le secteur
> **de l'agriculture, de la pêche et de l'aquaculture** et pour les prêts fonciers agricoles, — les
> ressources du fonds de promotion et de décentralisation industrielle pour […], — les dotations du
> titre II […]. »

→ Le décret nomme **un seul** fonds pour l'ensemble agriculture + pêche + aquaculture, sous le
libellé « fonds spécial pour le développement de l'agriculture ». Il ne cite **aucun** texte
fondateur (les visas, grepés sur tout le fascicule, ne mentionnent ni ce fonds ni un FSPA).

**b) Rapport Fonds Spéciaux 2020 du ministère des Finances** (annexe 10 LF 2020) — distingue
explicitement **deux** fonds agricoles voisins et donne leur texte créateur :

> **§3, pp. 21-22 — « Fonds Spécial de Développement Agricole et de la Pêche »** : « a été créé en
> vertu de la **loi n° 17 du 27 mai 1963** portant encouragement de l'État à l'investissement privé
> dans les secteurs de l'agriculture et de la pêche […]. La gestion du Fonds est confiée à la
> **Banque Nationale Agricole et à la Banque Tunisienne de Solidarité**. […] continuera à accorder
> les prêts d'investissement […] **en plus des primes accordées en vertu de la nouvelle loi de
> l'investissement promulguée en septembre 2016** » — pour les petits investissements (agricole
> ≤ 60 mille D, pêche ≤ 90 mille D, aquaculture ≤ 100 mille D, coopératives/GDA).

> **§4, pp. 23-24 — « Fonds Spécial de Développement Agricole (Compte Central de Développement
> Agricole) »** : « a été créé en vertu de la **loi n° 17 du 27 mai 1963** relative à l'encouragement
> de l'État au développement agricole […] à travers le financement : — des avantages accordés en
> vertu du **Code d'Incitation des Investissements** ; — des primes accordées en vertu d'autres
> textes […]. Sa gestion a été confiée à la **Banque Nationale Agricole**. »

→ « loi n° 17 du 27 mai 1963 » = **loi n° 63-17 du 27 mai 1963** (recid 117574, JORT n° 26/1963,
pp. 745-746). **Attention** : le ministère la cite sous un intitulé **paraphrasé** (« encouragement
de l'État à l'investissement privé dans les secteurs de l'agriculture et de la pêche ») qui **ne
correspond pas** au titre JORT exact (« portant encouragement de l'État au développement de
l'agriculture »). L'attribution est donc **administrative et secondaire**, pas le texte lui-même.

**c) PAP 2022, mission Agriculture** — origine de la lecture « pêche » de la note budget :
- Programme 1 (Production agricole), activité 2 : « Encouragement de l'État pour l'investissement
  dans le secteur agricole » (76 600 → 78 100 mD) — **sans sigle**.
- Programme 2 (Pêche et aquaculture), activité 3 : « Encouragement de l'État pour l'investissement
  dans le secteur Pêche et Aquaculture **(FOSDAP)** et l'indemnisation des dommages agricoles causés
  par les calamités naturelles » (10 400 → 11 900 mD).
- Activité 6 : « Transfert au profit de l'opérateur APIA au titre de l'activité : Encouragement des
  Investissements Agricoles » (11 860 → 12 900 mD).

→ Le PAP accole le sigle « (FOSDAP) » à **la ligne pêche d'un programme**, non à un fonds distinct :
c'est un **artefact de nomenclature budgétaire**, pas une définition du fonds.

---

## 1. Tableau des fonds distincts

Intitulés **exacts** tels qu'ils figurent dans la source citée (FR) ; l'arabe n'est donné que
lorsqu'il est attesté dans un titre JORT (sinon « non attesté au JORT »).

| # | Intitulé exact (FR) | Arabe | Sigle | Texte fondateur (daté) | Objet / bénéficiaire |
|---|---|---|---|---|---|
| **D** | **« Fonds Spécial de Développement Agricole et de la Pêche »** (rapport Fonds Spéciaux 2020) ; « fonds spécial pour le développement de l'agriculture » (décret 2017-389, art. 27) | non attesté au JORT | **FOSDAP** | **Non établi au JORT.** Rattaché par le ministère des Finances (rapport Fonds Spéciaux 2020, p. 21) à la **loi n° 63-17 du 27 mai 1963** (titre JORT paraphrasé) ; **aucune notice JORT** ne porte ce fonds en titre ; le décret 2017-389 le nomme sans citer sa création | **Primes d'investissement de la loi 2016 + prêts d'investissement + prêts fonciers agricoles**, petits projets agriculture/pêche/aquaculture. Guichet : **APIA** ; gestion **BNA + BTS** |
| **E** | **« Fonds Spécial de Développement Agricole (Compte Central de Développement Agricole) »** (rapport Fonds Spéciaux 2020, p. 23) | non attesté au JORT | **FOSDA / CCDA** | **Non établi au JORT.** Même rattachement à la **loi n° 63-17 du 27 mai 1963** par le ministère des Finances | Avantages du **Code d'incitation aux investissements** + primes d'autres textes ; projets plus importants. Gestion **BNA** |
| **A** | « Fonds spécial de promotion agricole » (FSPA) | non attesté (titre JORT FR) | **FSPA** | **Loi n° 72-87 du 27 déc. 1972** (LF 1973), fonds spéciaux du Trésor, art. 28-30 — JORT n° 52 du 26 déc. 1972, p. 1855 ; modif. loi n° 73-82 (LF 1974), art. 69-70 ; décret 80-1161 | **Ancêtre budgétaire** du soutien à l'investissement agricole (aide aux attributaires de lots domaniaux). Candidat au support du régime de la loi 63-17 |
| **B** | « Fonds de soutien de la pêche » | non attesté (titre JORT FR) | — | Institué par **décret du ministre des Finances du 21 juin 1956** (JORT n° 50/1956, p. 835) ; **supprimé** par loi n° 59-124 (JORT n° 51/1959, p. 1096) ; **rétabli** en fonds spécial du Trésor par **LFC 1982, loi n° 82-27, art. 13-15** (JORT n° 20/1982, p. 724) ; organisé par décret n° 82-1351 | Soutien sectoriel à la pêche. **Distinct** de D/E |
| **C** | « Fonds de développement de la compétitivité dans les secteurs de l'agriculture, de la pêche et des industries agro-alimentaires » (→ « …de l'agriculture et de la pêche ») | صندوق تنمية القدرة التنافسية في قطاع الفلاحة والصيد البحري | FODECAP / FST | **Loi n° 94-127 du 26 déc. 1994** (LF 1995), art. 45-49 (JORT n° 103/1994, p. 2046) ; décret n° 95-1420 ; refonte décret n° 96-1563 | Fonds **financé par taxes** sur produits ; compétitivité / mise à niveau. **Déjà traité au volume Fiscalité** (`#sec-fst-agriculture`). **Distinct** de D/E |
| F | « Fonds de financement du repos biologique dans le secteur de la pêche » | صندوق تمويل الراحة البيولوجية في قطاع الصيد البحري | — | **Loi n° 2009-71 (LF 2010), art. 11-12** (JORT n° 102/2009, p. 3913) ; décret n° 2010-1766 | Pêche (repos biologique). Pour mémoire |
| G | « Fonds d'indemnisation des dommages agricoles causés par les calamités naturelles » | صندوق تعويض الأضرار الفلاحية الناجمة عن الجوائح الطبيعية | — | **Loi n° 2017-66 (LF 2018), art. 17** (JORT n° 101/2017) ; décrets gouv. 2018-729/821/822 | Calamités (chapitre 7). Budgété **avec** l'activité FOSDAP au PAP 2022 — d'où le mélange |

Autres FST agricoles historiques relevés dans la rubrique « fonds spéciaux du Trésor : ministère de
l'agriculture » des LF (pour l'index, non centraux ici) : fonds de reconversion du vignoble (LF 1976,
loi 75-83, art. 69-72) ; fonds de sauvegarde de la faune cynégétique (LF 1977, loi 76-115) ; fonds
de stabilisation des prix des produits avicoles (LF 1984, loi 83-113, art. 96-98) ; fonds de
promotion du secteur oléicole (arrêté du 14/02/1990 ; cité au rapport Fonds Spéciaux 2020).

---

## 2. Réponse nette : que désigne « FOSDAP » ?

**FOSDAP = « Fonds Spécial de Développement Agricole *et de la Pêche* » — un fonds qui couvre
*ensemble* l'agriculture, la pêche et l'aquaculture, et non la pêche seule.** Le « P » du sigle est
« Pêche », mais il s'ajoute à « Agricole » : ce n'est pas un fonds pêche distinct d'un fonds
agriculture.

- **La note *investissement* a raison** : FOSDAP est le fonds qui porte les primes d'investissement
  servies via l'APIA, pour l'agriculture **et** la pêche/aquaculture (décret 2017-389 art. 27 ;
  rapport Fonds Spéciaux 2020 p. 21). Le développé « Fonds spécial de développement de l'agriculture
  et de la pêche » attesté hors JORT (AfDB ADB-BD-IF-2006-162 ; UN-FFD Srarfi 2006, « géré par la
  BNA » ; guide Mashrou3i) est **confirmé** par une source officielle du ministère des Finances.
- **La note *budget* se trompe sur un point** : elle lit FOSDAP = « fonds de développement de la
  **pêche et de l'aquaculture** », distinct d'un « FOSDA = agriculture ». Cette lecture vient du
  **seul** PAP 2022, qui accole « (FOSDAP) » à la ligne pêche du programme 2 — artefact de
  nomenclature. Aucun texte ne crée un fonds FOSDAP « pêche seule ».
- **Mais la note budget a raison sur l'existence d'un second fonds presque homonyme** : il y a bien
  **deux** fonds distincts, que le rapport Fonds Spéciaux 2020 sépare clairement — **FOSDAP** (« …
  Agricole et de la Pêche », primes de la loi 2016, petits projets, BNA+BTS) et **FOSDA / Compte
  Central de Développement Agricole** (avantages du Code d'incitation, projets plus grands, BNA).
  Le sigle **FOSDA** désigne donc le **Compte Central de Développement Agricole**, *pas* « le fonds
  agriculture par opposition à un fonds pêche ».

**Développés corrects (tranchés) :**
- **FOSDAP** = **Fonds Spécial de Développement Agricole et de la Pêche** (agriculture + pêche +
  aquaculture) ;
- **FOSDA** = **Fonds Spécial de Développement Agricole**, dit **Compte Central de Développement
  Agricole (CCDA)** ;
- **FSPA** = **Fonds Spécial de Promotion Agricole** (créé LF 1973, loi 72-87) — ancêtre budgétaire,
  à ne pas confondre avec les précédents.

**Conséquence pour le précis.** Le sigle FOSDAP peut désormais être employé **avec son développé
sourcé** (« Fonds spécial de développement agricole et de la pêche », rapport Fonds Spéciaux 2020 du
ministère des Finances), à condition de signaler que **son texte créateur exact au JORT n'est pas
établi** (voir §3). Le rédacteur distinguera soigneusement FOSDAP (petits projets, primes 2016),
FOSDA/CCDA (Code d'incitation), FSPA (1972, historique) et le fonds de compétitivité C (fiscalité).

---

## 3. Le fonds des primes APIA : texte de création **partiellement établi, à sourcer « par le
ministère des Finances », non par le JORT**

- **Établi (attribution administrative)** : le ministère des Finances rattache FOSDAP **et**
  FOSDA/CCDA à la **loi n° 63-17 du 27 mai 1963** (rapport Fonds Spéciaux 2020, pp. 21 et 23). Cela
  **confirme la filiation** proposée par la note investissement (régime « encouragement de l'État au
  développement de l'agriculture », 1963). C'est une base citable — mais **secondaire** : le rapport
  paraphrase le titre de la loi et n'indique **pas l'article** qui érige le compte spécial du Trésor.
- **Non établi (texte JORT)** : **aucune notice de `jort_cache` ne porte en titre** « fonds spécial
  de développement agricole et de la pêche » / « …de l'agriculture » (ni en FR ni en AR —
  صندوق خاص لتنمية الفلاحة, صندوق التنمية الفلاحية, تنمية الفلاحة والصيد البحري : zéro résultat de
  texte créateur). Le titre JORT de la loi 63-17 est « encouragement de l'État au développement de
  l'agriculture » (sans « et de la pêche », sans « investissement privé »), et une **loi
  d'encouragement n'érige pas elle-même un fonds spécial du Trésor** — ce véhicule budgétaire naît en
  pratique d'un **article de loi de finances** (modèle attesté : FSPA, loi 72-87 ; fonds de soutien
  de la pêche, LFC 82-27). L'article exact qui crée/renomme le compte spécial sous l'intitulé actuel
  **n'est pas localisé** ; candidat le plus probable : le **FSPA (loi 72-87, 1973)**, renommé au fil
  des LF — continuité **non prouvée par le texte**. Le décret 2017-389, qui nomme le fonds, **ne cite
  pas** sa création.

**Verdict** : la **politique** fondatrice est établie (loi 63-17, 1963, par le ministère des
Finances) ; le **texte budgétaire créant le fonds spécial du Trésor sous son nom actuel reste non
établi** au JORT. À dépouiller : les articles « fonds spéciaux du Trésor : ministère de
l'agriculture » des LF 1973-2018 (en image → OCR), pour saisir le moment où le FSPA/CCDA devient
« …agricole et de la pêche ».

---

## 4. Références CSL candidates

**Déjà présentes** (réutiliser les clés) : `loi-63-17-encouragement-agriculture`,
`loi-72-87-lf-1973-fonds-promotion-agricole`, `loi-94-127-lf-1995-fonds`,
`decret-95-1420-fonds-competitivite-agricole`, `afdb-2006-pcr-cap-bon`,
`decret-gouv-2017-389-incitations-financieres` (→ **enrichir la note** : art. 27 nomme le « fonds
spécial pour le développement de l'agriculture » pour agriculture + pêche + aquaculture).

**À créer** (CSL-JSON) :

```json
[
  {"id":"tn-minfin-fonds-speciaux-2020","type":"report",
   "title":"Rapport sur l'activité des Fonds Spéciaux — annexe 10 au projet de loi de finances 2020",
   "author":[{"literal":"Ministère des Finances (République tunisienne), gestion du budget par objectifs"}],
   "issued":{"date-parts":[[2019]]},
   "URL":"http://www.gbo.tn/sites/default/files/2021-02/Annexe_10_LF2020-Fonds_Sp%C3%A9ciaux.pdf",
   "note":"130 p. Décrit chaque fonds spécial du Trésor et son texte créateur. §3 pp. 21-22 : « Fonds Spécial de Développement Agricole et de la Pêche » (FOSDAP), créé en vertu de la loi n° 63-17 du 27 mai 1963, géré par BNA et BTS, primes de la loi d'investissement 2016. §4 pp. 23-24 : « Fonds Spécial de Développement Agricole (Compte Central de Développement Agricole) », même rattachement, avantages du Code d'incitation. Copie locale : tunisia-data/data/raw/gbo/Annexe_10_LF2020-Fonds_Speciaux.pdf (SHA-256 2bb81c13b2a554b5e997364abab6a6883b02c2b026cb3a81a0cd7ddd2f1d967a). Consulté le 10 novembre 2026. Famille : budgétaire / ministère des Finances."},

  {"id":"loi-82-27-lfc-1982-fonds-soutien-peche","type":"legislation",
   "title":"Loi n° 82-27 du 23 mars 1982, portant loi de finances complémentaire pour la gestion 1982 — fonds spéciaux du Trésor : ministère de l'agriculture : fonds de soutien de la pêche, art. 13 à 15",
   "title-short":"Loi n° 82-27 du 23 mars 1982 (LFC 1982)",
   "issued":{"date-parts":[[1982,3,23]]},
   "note":"JORT n° 20 du 1982, p. 724 (notice jort_cache recid 115132). Rétablit le fonds de soutien de la pêche en fonds spécial du Trésor. Fonds initial : décret du ministre des Finances du 21 juin 1956 (JORT n° 50/1956, p. 835), supprimé par loi n° 59-124 (JORT n° 51/1959, p. 1096). Image : OCR à faire."},

  {"id":"decret-82-1351-fonds-soutien-peche","type":"legislation",
   "title":"Décret n° 82-1351 du 12 octobre 1982, fixant les conditions et les modalités d'intervention du fonds de soutien de la pêche",
   "title-short":"Décret n° 82-1351 du 12 octobre 1982",
   "issued":{"date-parts":[[1982,10,12]]},
   "note":"JORT n° 66 du 1982, p. 2189 (notice jort_cache recid 97250). Modifié par décrets 87-877, 91-1499, 95-2271, 2000-2083, 2001-1638, 2004-1795."},

  {"id":"loi-2009-71-lf-2010-repos-biologique-peche","type":"legislation",
   "title":"Loi n° 2009-71 du 21 décembre 2009, portant loi de finances pour l'année 2010 — création du fonds de financement du repos biologique dans le secteur de la pêche, art. 11 à 13",
   "title-short":"Loi n° 2009-71 du 21 décembre 2009 (LF 2010)",
   "issued":{"date-parts":[[2009,12,21]]},
   "note":"JORT n° 102 du 2009, p. 3913 (notice jort_cache recid 109604/109608). Décret d'application n° 2010-1766 du 19 juillet 2010. Fonds pêche, pour mémoire (distinct du FOSDAP)."},

  {"id":"srarfi-2006-financement-investissement-agricole","type":"paper-conference",
   "title":"Le financement de l'investissement privé dans le secteur agricole en Tunisie",
   "author":[{"literal":"Srarfi (M.)"}],
   "issued":{"date-parts":[[2006]]},
   "URL":"https://www.un.org/esa/ffd/wp-content/uploads/2006/11/20061122_NDBs-MSC-SA-Srarfi.doc",
   "note":"Nations Unies, Financing for Development. Atteste : le financement se fait « à travers le fonds spécial de développement de l'agriculture et de la pêche (FOSDAP), qui est géré par la BNA ». Famille : source externe (secondaire) ; corrobore le rapport Fonds Spéciaux 2020. PDF/DOC à récupérer dans tunisia-data si cité."}
]
```

---

## 5. Recherches infructueuses (fiches `docs/recherches.yml` — mises à jour / proposées)

Le fichier `docs/recherches.yml` et `scripts/recherches.py` **n'existent pas** dans ce dépôt
(worktree agriculture) ; les deux fiches proposées par les notes antérieures ne sont donc pas encore
dans un registre. Je les **fusionne et corrige** ici (elles portaient sur le même objet) : la fiche
reste **partiellement résolue** — le rattachement politique est trouvé (loi 63-17, par le ministère
des Finances), le texte budgétaire créateur reste à trouver au JORT.

```yaml
- id: r-fosdap-fonds-developpement-agricole-peche
  objet: >
    texte créateur AU JORT du « Fonds spécial de développement agricole et de la pêche » (FOSDAP) et
    du « Fonds spécial de développement agricole / Compte central de développement agricole » (FOSDA/CCDA),
    supports budgétaires des primes et prêts d'investissement servis via l'APIA. Rattachés par le
    ministère des Finances (rapport Fonds Spéciaux 2020) à la loi n° 63-17 du 27 mai 1963 ; l'article
    de loi de finances érigeant le compte spécial du Trésor sous l'intitulé actuel reste à localiser.
  remplace: [r-fosdap-creation, r-agri-fosda-fonds-special-developpement]
  ou: [docs/notes/agriculture-fonds-elucidation.md, docs/notes/agriculture-investissement-documentation.md, docs/notes/agriculture-budget-documentation.md]
  requetes:
    titres_like:
      - "%fonds special de developpement%agricult%"
      - "%developpement agricole et de la peche%"
      - "%fonds special de promotion agricole%"
      - "%compte central%developpement agricole%"
    titres_fts:
      - "fonds AND special AND developpement AND agricole"
      - "fonds AND promotion AND agricole"
    iort_ar:
      - "صندوق خاص لتنمية الفلاحة"
      - "صندوق التنمية الفلاحية"
      - "تنمية الفلاحة والصيد البحري"
      - "الصندوق الخاص للتنمية الفلاحية والصيد البحري"
    plein_texte: [FOSDAP, FOSDA, "fonds special pour le developpement de l'agriculture"]
    depuis: 1963-01-01
  passes:
  - date: 2026-11-10
    role: documentaliste
    sources: [jort_cache, corpus_local, gbo.tn, web]
    couverture: >
      jort_cache (≈ avril 2026), LIKE/FTS titres FR + AR 1957-2026 : AUCUNE notice ne porte en titre
      « fonds spécial de développement agricole et de la pêche » / « …de l'agriculture » ni leur forme
      arabe. Seuls trouvés : FSPA (loi 72-87, 1973) ; fonds de soutien de la pêche (décret 1956,
      LFC 82-27) ; fonds de compétitivité (loi 94-127, 1995) ; repos biologique (LF 2010) ; calamités
      (LF 2018). TROUVÉ hors JORT : rapport Fonds Spéciaux 2020 du ministère des Finances (annexe 10
      LF 2020), qui NOMME les deux fonds (FOSDAP pp. 21-22 ; FOSDA/CCDA pp. 23-24) et les rattache à
      la loi n° 63-17 du 27 mai 1963 (titre paraphrasé, article non précisé) ; décret gouv. 2017-389
      art. 27 nomme « le fonds spécial pour le développement de l'agriculture » (agriculture + pêche
      + aquaculture) sans citer sa création ; AfDB ADB-BD-IF-2006-162 et UN-FFD Srarfi 2006 (« géré
      par la BNA ») confirment le développé. Non couvert : articles « fonds spéciaux du Trésor :
      ministère de l'agriculture » des LF 1973-2018 lus au corps (fascicules en image, OCR à faire) ;
      miroir iort arabe non chargé.
    couvert_jusqu_au: 2026-04-10
    resultat: partiel
  a_faire:
    - OCR des articles « fonds spéciaux du Trésor / ministère de l'agriculture » des LF 1973-2018 pour
      saisir la création et les renommages (FSPA → …agricole et de la pêche → CCDA)
    - récupérer l'édition arabe du rapport Fonds Spéciaux (annexe au PLF) pour l'intitulé arabe officiel
    - récupérer les éditions antérieures/postérieures du rapport Fonds Spéciaux (séries annuelles gbo.tn)
```

---

## 6. Ce qui reste à OCR / à acquérir

- **LF, articles « fonds spéciaux du Trésor : ministère de l'agriculture », 1973-2018** (fascicules
  en image) : pour établir le **texte budgétaire** qui érige puis renomme le fonds (FSPA 1972 → « …
  agricole et de la pêche » → Compte Central). Cibles prioritaires : loi 72-87 (art. 28-30), loi
  82-27 (art. 13-15), et toute LF portant « changement d'appellation d'un fonds spécial » côté
  agriculture.
- **Loi n° 63-17 du 27 mai 1963** (JORT n° 26/1963, pp. 745-746, image) : transcrire pour vérifier
  si son dispositif crée déjà un fonds ou renvoie à la loi de finances.
- **Intitulé arabe officiel** de FOSDAP et FOSDA/CCDA : non attesté au JORT ; à prendre dans
  l'édition **arabe** du rapport Fonds Spéciaux (à récupérer) plutôt que reconstruit.
- **Rapport Fonds Spéciaux, autres millésimes** (gbo.tn / finances.gov.tn) : pour une série et pour
  confirmer la stabilité des intitulés et du rattachement.

---

## 7. Backlog (notions + pistes — à router par l'archiviste ; NON écrit au glossaire ni au backlog-precis)

**Notions à glossaire** (développés tranchés) :
- **FOSDAP — Fonds spécial de développement agricole et de la pêche** : fonds spécial du Trésor
  (gestion BNA + BTS) portant primes et prêts d'investissement des petits projets agricoles, de
  pêche et d'aquaculture servis via l'APIA ; rattaché par le ministère des Finances à la loi
  n° 63-17 (1963) ; texte budgétaire créateur au JORT non établi. Source canonique : rapport Fonds
  Spéciaux 2020 (ministère des Finances), pp. 21-22.
- **FOSDA — Fonds spécial de développement agricole (Compte Central de Développement Agricole,
  CCDA)** : fonds spécial du Trésor (gestion BNA) finançant les avantages du Code d'incitation aux
  investissements ; même rattachement. Source : rapport Fonds Spéciaux 2020, pp. 23-24.
- **FSPA — Fonds spécial de promotion agricole** : fonds du Trésor créé par la LF 1973 (loi 72-87,
  art. 28-30) ; ancêtre budgétaire, à ne pas confondre avec FOSDAP/FOSDA.
- Ne pas confondre avec **C** (fonds de développement de la compétitivité, taxes, fiscalité) ni avec
  **G** (fonds d'indemnisation des calamités agricoles, LF 2018), budgété avec l'activité FOSDAP au
  PAP 2022.

**Pistes / données** :
- OCR des articles LF « fonds spéciaux du Trésor / agriculture » 1973-2018 (ci-dessus).
- Récupérer l'édition arabe + autres millésimes du rapport Fonds Spéciaux (séries annuelles).
- Fichiers rangés dans `tunisia-data` (feu vert AGENTS.md) : `data/raw/gbo/Annexe_10_LF2020-Fonds_Speciaux.pdf`
  + catalogue `sources/gbo-fonds-speciaux-rapport-urls.csv` (URL, date, SHA-256).
