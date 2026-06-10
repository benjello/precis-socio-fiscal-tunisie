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
