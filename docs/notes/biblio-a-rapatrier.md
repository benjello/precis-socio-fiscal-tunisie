# Inbox bibliographe — références à rapatrier dans Zotero

> Handoff pour l'agent `bibliographe` (Phase 1, issue #17) ou pour traitement manuel.
> Source canonique de la bibliographie = **Zotero groupe 6529669** (`scripts/sync_biblio.py`
> tire Zotero → `references.json`). Toute référence ajoutée à la main dans un
> `references.json` doit être **remontée dans Zotero** pour être pérenne et obtenir une
> clé de citation stable (champ « Extra » : `citation-key: xxx`).

## En attente

### Sources de données (catalog.yml de tunisia-data) — type CSL `dataset`
Clés référencées par les séries de données (`tunisia_data.meta()`), à créer dans Zotero
pour que les figures du précis soient citées et tracées :

| Clé | Source | Type |
|---|---|---|
| `minfin-remunerations` | Min. Finances — Série répartition économique des dépenses (masse salariale) | dataset |
| `minfin-indicateurs-fp` | Min. Finances — Indicateurs des finances publiques (déficit, dette, pression fiscale) | dataset |
| `ins-cnat-2015` | INS — Comptes de la Nation, base 2015 | dataset |
| `ins-fonction-publique-2021` | INS — Caractéristiques des agents de la fonction publique et leurs salaires 2010-2021 | dataset |
| `bct-bsf` | BCT — Bulletin des Statistiques Financières (et archives) | dataset |

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
