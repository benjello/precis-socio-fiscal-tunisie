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
- **`circulaire-42-1996` non créée.** Circulaire n° 42 du 25 octobre 1996 sur la gestion des
  indemnités à caractère familial dans le secteur public (JORT n° 94 du 22 novembre 1996,
  pp. 2349-2364) : repérée et proposée au §12.2 du dossier contributif, mais **non lue** et
  **non citée** par le chapitre. À créer seulement si le texte est établi et cité.
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
