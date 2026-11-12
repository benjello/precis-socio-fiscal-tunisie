# Agriculture — chapitre 2 « l'institution, la tutelle et l'encadrement » : note documentaire

Rôle : documentaliste. Date : 10 novembre 2026. Volume candidat : « L'agriculture — le soutien au
producteur » (option c, arbitrée le 10/11/2026). Chapitre de **cadre/institution**
(`docs/conventions-redaction.md`, § 4 : naissance, statut, ce qu'elle sert, comptes, longue période).

**Périmètre tenu** : tutelle et encadrement porteurs d'un flux budgétaire ou distributif. **Hors
périmètre** (frontière du ticket) : statut et comptes des EP (Office des céréales, ONH, OTD, BNA,
SONEDE) — déjà au livre des entreprises publiques.

**Méthode de lecture.** Les notices (type, numéro, date de signature, fascicule JORT, tome, pages)
viennent de `jort_cache.db` (requêtes SQL le 10/11/2026) et sont **établies**. Le **texte intégral**
des fascicules a été vérifié : les fascicules JORT antérieurs à ~1996 du corpus local
(`~/projets/PDFs-legislation-tunisie/PDFs/JORT/<année>/fr/`) sont des **images scannées sans couche
texte** (≤ 64 caractères extraits) ; leurs articles exigent une **OCR** avant d'être cités au mot.
Un seul texte de cadre a une couche texte exploitable et a été **lu au mot** : la loi n° 96-4 (centres
techniques agricoles). Partout ailleurs, intitulé + localisation établis, **contenu des articles non
lu** : signalé comme tel.

Aucun PDF n'a été versé à `tunisia-data/data/raw/` : tous les textes cités sont des fascicules JORT,
déjà dans le corpus de législation dédié ; aucune étude ni rapport externe n'est cité dans cette note.

---

## 1. Ce qui est établi et lu

### 1.1 Le ministère de l'Agriculture — organisation et attributions (série de décrets)

Épine des décrets portant **organisation** et **attributions** du ministère, tous notices établies,
fascicules présents au corpus (scannés, articles non lus sauf mention) :

| Objet | Texte | Date | JORT |
|---|---|---|---|
| Organisation | Décret n° 70-104 | 28 mars 1970 | — |
| Attributions | Décret n° 77-647 | 5 août 1977 | n° 56/1977 |
| Organisation | Décret n° 77-648 | 5 août 1977 | n° 56/1977 (modifié par 80-1230, 81-1015, 82-267, 83-1244/1245, 84-311) |
| Attributions | Décret n° 86-1233 | 4 déc. 1986 | (modifié 87-85) |
| Organisation | Décret n° 87-779 | 21 mai 1987 | (modifié 90-558, 90-670, 93-2357, 99-2825) |
| Attributions | Décret n° 2001-419 | 13 févr. 2001 | n° 15/2001, pp. 310-311 |
| Organisation | Décret n° 2001-420 | 13 févr. 2001 | n° 15/2001, pp. 312-332 |
| Modif. organisation | Décret n° 2010-625 | 5 avril 2010 | — |
| Modif. organisation | Décret n° 2011-1560 | 5 sept. 2011 | — |

Observations : (a) le **couple attributions / organisation** se refait à chaque grande recomposition
(1977, 1986-87, 2001) ; le décret de 2001 (20 pages d'organisation) est le socle encore modifié en
2010-2011. (b) Le fascicule n° 15/2001 (`Jo0152001.pdf`) est présent **avec** couche texte, mais une
recherche plein-texte n'y fait pas surgir « agriculture » ni les n° 419/420 : couche probablement
pivotée/partielle — **articles à confirmer par relecture image**. (c) Après 2011 le ministère devient
« ministère de l'Agriculture, des Ressources hydrauliques et de la Pêche (maritime) » ; une
**réorganisation d'ensemble post-2014** n'a pas été isolée (titres arabes probables — voir § 6,
fiche proposée).

### 1.2 Les CRDA — commissariats régionaux au développement agricole

- **Texte fondateur : Décret n° 74-847 du 4 septembre 1974**, *portant création de commissariats
  régionaux au développement agricole* (JORT n° 56/1974, p. 1972 ; notice établie, **articles non lus
  — scanné**).
- **Décret n° 79-123 du 30 janvier 1979**, fixant les emplois fonctionnels des CRDA (modifié 80-612,
  84-1313).
- **Décret n° 81-215 du 18 février 1981**, *fixant les attributions et l'organisation des CRDA* (JORT
  n° 12/1981, pp. 365-367 ; **articles non lus — scanné**). C'est le texte de référence du rôle (CRDA
  comme services déconcentrés du ministère au niveau du gouvernorat).
- Créations/compléments par gouvernorat ensuite (ex. décret 80-1113, CRDA de …).
- **Antécédent à relever** : les **associations de développement agricole** (décret-loi n° 64-11 du
  26 mars 1964, ratifié par loi n° 64-12 ; **abrogé** par la **loi n° 71-25 du 14 juin 1971**) ; les
  CRDA (1974) sont postérieurs à cet abandon. Filiation exacte (ce que 74-847 reprend) : OCR requise.

### 1.3 Les offices de mise en valeur des périmètres irrigués

Famille nombreuse, construite par vagues :
- **Décret-loi n° 60-3 du 9 février 1960** : office de mise en valeur de Sidi-Bou-Zid (premier ;
  dissous par loi n° 68-18 de 1968). **Loi n° 61-1 du 2 janvier 1961** : office des Souassi (dissous
  loi n° 71-26).
- **Loi n° 63-18 du 27 mai 1963, *portant réforme agraire dans les périmètres publics irrigués*** —
  texte-pivot du régime des périmètres publics irrigués (modifiée par loi n° 71-9) ; **scanné,
  articles non lus**.
- Vague de 1973 : **loi n° 73-27** (office de Lakhmes), **loi n° 73-28** (office de Nebhana) ; décrets
  d'organisation 73-391/392. Offices de la vallée de la Medjerda et des périmètres irrigués (décret-loi
  70-10). La liste du régime conventionnel (cf. § 1.9) énumère les offices « de mise en valeur des
  périmètres irrigués » de Jendouba, Nabeul, Gabès-Médenine, Kairouan, Gafsa-Djérid, Sidi Bouzid, etc.
- **Conditions de mise en valeur des terres domaniales agricoles par les offices** : décret n° 83-226
  du 4 mars 1983.

### 1.4 L'Agence de la réforme agraire des périmètres publics irrigués → Agence foncière agricole

- **Texte fondateur : Loi n° 77-17 du 16 mars 1977, *portant création de l'Agence de la réforme
  agraire des périmètres publics irrigués*** (deux localisations en notice : JORT n° 18/1977, pp.
  651-652 — intitulé ; et n° 30/1977, pp. 1125-1132 — texte complet ; **scanné, articles non lus**).
- **Décret n° 77-627 du 1er août 1977**, organisation et fonctionnement (JORT n° 56/1977, pp.
  2225-2227 ; modifié 92-1376).
- **Décret n° 79-958 du 29 novembre 1979** : transfert de biens au profit de l'agence.
- **Changement de dénomination : Décret n° 99-1877 du 14 septembre 1999** — l'agence devient
  **« Agence foncière agricole » (AFA)** ; **Loi n° 2000-29 du 6 mars 2000** modifiant et complétant
  la loi n° 77-17 ; organigramme par décret n° 2001-656 du 8 mars 2001. C'est l'entité qui **figure**
  dans la liste du régime conventionnel des rémunérations publiques (sous son nom de 1977).

### 1.5 L'APIA — Agence de promotion des investissements agricoles

- **Cadre fondateur : Loi n° 82-67 du 6 août 1982, *portant encouragement aux investissements dans les
  secteurs de l'agriculture et de la pêche*** (JORT n° 54/1982, tome 125, pp. 1691-1696 ;
  **référence déjà dans `precis/fr/fiscalite/references.json`, id `loi-82-67` ; texte NON lu —
  scanné**). C'est le texte sous lequel l'APIA est mise en place comme guichet des avantages agricoles
  (article créateur **à confirmer par OCR**).
- **Décret n° 82-1484 du 29 novembre 1982, *portant organisation et fonctionnement de l'Agence de
  promotion des investissements agricoles*** (JORT n° 77/1982, pp. 2606-2609 ; modifié 84-344).
- Organisations administratives et financières successives : décrets n° 90-569 (2 avril 1990),
  99-370 (15 févr. 1999), 2001-866 (organigramme, 18 avril 2001), 2010-345 (organigramme, 22 févr.
  2010) ; statut du personnel 2010-2014, modifié par décret gouvernemental 2018-13.
- **Rôle de guichet** établi par ailleurs dans la fiscalité (`_regimes_incitation.qmd`) : l'APIA
  instruit et verse les **primes** à l'investissement agricole ; une seule valeur connue à ce jour,
  **54 MD de primes versées en 2009** (tableau du coût des avantages, `_regimes_incitation.qmd`,
  l. 1076). L'APIA relève de la fiscalité pour le régime d'incitation ; le chapitre « institution »
  ne porte que son statut de guichet et son rattachement.

### 1.6 Les groupements interprofessionnels (par filière)

- **Phase sectorielle (1971-1984)**, chaque filière par sa loi : **loi n° 71-30 du 2 juillet 1971**
  (agrumes et fruits ; statut décret 71-394), **décret-loi n° 73-1 du 10 août 1973** (légumes ;
  ratifié loi 73-56 ; statut 74-202), **loi n° 74-45 du 22 mai 1974** (dattes ; statut 74-854),
  **loi n° 84-39 du 23 juin 1984** (produits avicoles ; organisation 84-1396).
- **Cadre général : Loi n° 93-84 du 26 juillet 1993, *relative aux groupements interprofessionnels
  dans le secteur agricole et agro-alimentaire*** (JORT n° 56/1993, pp. 1076-1078 ; **scanné, articles
  non lus**). Statuts-type par **décret n° 94-1165 du 23 mai 1994** ; loi modifiée par **loi n° 2005-16
  du 16 février 2005** ; statuts-type révisés décret 2005-2872.
- Les groupements perçoivent des **cotisations interprofessionnelles** (prélèvements par filière) —
  flux distributif à documenter, lien avec le fonds de compétitivité agricole (FODECAP, déjà en
  fiscalité). Montants/affectations : **non relevés** (lacune, § 3).

### 1.7 Vulgarisation, recherche, encadrement (institutions porteuses de flux)

- **Vulgarisation — AVFA : Loi n° 90-73 du 30 juillet 1990, *portant création de l'agence de la
  vulgarisation et de la formation agricoles*** (JORT n° 51/1990, pp. 1007-1008 ; **scanné**) ;
  organisation **décret n° 91-66 du 7 janvier 1991**. Cellules territoriales de vulgarisation agricole
  (CTV) créées par arrêtés 1991-1996.
- **Recherche / enseignement — IRESA : Loi n° 90-72 du 30 juillet 1990, *portant création de
  l'institution de la recherche et de l'enseignement supérieur agricoles*** (JORT n° 51/1990, p. 1007 ;
  **scanné**) ; organisation **décret n° 91-104 du 21 janvier 1991** (modifié 95-1000, 98-1144,
  2003-1678, 2009-350, 2010-1318, 2015-151) ; **pôles régionaux de recherche-développement** décret
  n° 95-999 du 5 juin 1995.
- **Centres techniques agricoles — Loi n° 96-4 du 19 janvier 1996, *relative aux centres techniques
  dans le secteur agricole*** (JORT n° 7/1996, pp. 203-204) — **SEUL texte de cadre LU AU MOT** :
  - *Art. 1er* : les centres techniques sont des **personnes morales d'intérêt économique public**,
    dotées de la personnalité civile et de l'autonomie financière ;
  - *Art. 2* : créés **par arrêté du ministre de l'agriculture**, à l'initiative des organismes et
    organisations professionnels, pour une composante ou la totalité d'un secteur ;
  - *Art. 3* : créés **sans capital social**, activité **non génératrice de distribution de bénéfices** ;
  - *Art. 7* : missions — adaptation des résultats de la recherche aux exploitations, **vulgarisation**
    (transfert du progrès technique), appui à la productivité/qualité/coûts, études et documentation ;
  - *Art. 12* : **ressources** = ressources fiscales créées à leur profit, produits de leurs activités
    et de leur patrimoine, dons et legs, **ressources de l'État** et toute autre ressource affectée —
    c'est le **flux budgétaire/distributif** qui justifie leur présence au chapitre.
  - Statuts approuvés par arrêté : CT de la pomme de terre (1997), **CT des céréales** (1997), CT de
    l'agriculture biologique (1999), etc. (statuts-type arrêté 2007).

### 1.8 Les offices de développement régional (encadrement territorial)

Porteurs de budgets d'intervention, à la frontière tutelle/EP — à **clarifier avec le livre EP** :
- **Office de développement sylvo-pastoral du Nord-Ouest (ODESYPANO) : loi n° 81-17 du 9 mars 1981**
  (org. décret 81-975) ; refondé **Office de développement du Nord-Ouest, loi n° 94-85 du 18 juillet
  1994** (org. 94-2046).
- **Office de développement du Sud (ODS) : décret n° 85-447 du 19 mars 1985**, refondé **loi n° 94-83
  du 18 juillet 1994** (org. 94-2045). Office de développement de la Tunisie centrale (cf. liste § 1.9).

### 1.9 Point d'ancrage déjà dans le précis

La liste nominative du **régime conventionnel des rémunérations publiques**
(`precis/fr/remunerations_publiques/_regime_conventionnel.qmd`, l. 260) énumère déjà, comme
établissements rattachés à la CNRPS : l'« Agence de la réforme agraire des périmètres publics
irrigués », l'« Agence de promotion des investissements agricoles », le « Centre national d'études
agricoles », et toute la série des « Office de mise en valeur des périmètres irrigués de … » et offices
de développement (Sud, Sylvo-pastoral du Nord-Ouest, Tunisie centrale). **Point de raccord** pour le
chapitre : ces entités ont un personnel public (CNRPS) — leur masse salariale est un flux.

---

## 2. Séries et flux budgétaires localisés

1. **PAP/RAP de la mission « Agriculture, ressources hydrauliques et pêche » (2015-2025)** — déjà
   **acquis et catalogués** dans `tunisia-data` (`sources/ministere-agriculture-tic-sante-finances.md`,
   § 1.1). Contiennent : budgets par programme, **fiches opérateurs** (OTD, OC, ONH ; SONEDE), crédits
   de transfert. Les **CRDA** (services déconcentrés) et les programmes de vulgarisation/recherche y
   apparaissent comme programmes budgétaires. Lacunes du lot : PAP 2019 et 2023, RAP 2022+. C'est
   l'**épine budgétaire** du chapitre 3 du livre ; pour le chapitre 2, elle fournit l'ossature
   institution ↔ programme.
2. **Primes APIA** : une seule valeur sourcée (54 MD en 2009, `_regimes_incitation.qmd`). Série à
   construire (rapports d'activité APIA, archives web non ouvertes). Relève surtout de la fiscalité.
3. **Ressources des centres techniques et cotisations interprofessionnelles** : adossées au **fonds
   de développement de la compétitivité dans le secteur de l'agriculture et de la pêche** (FODECAP,
   né en 1995), déjà traité en fiscalité (`#sec-fst-agriculture`). Montants par organisme : **non
   relevés**.
4. **Budget du ministère avant 2015** (lois de finances / lois de règlement) : **non dépouillé** —
   voir backlog.

---

## 3. Textes candidats non lisibles au mot + où les obtenir

Tous localisés en notice ; **articles non lus car fascicules scannés sans couche texte** → **OCR
ciblée** (pages connues) ou lecture image :

| Texte | Fascicule / pages | Où / comment |
|---|---|---|
| Décret 74-847 (création CRDA) | JORT 56/1974, p. 1972 | OCR `PDFs/JORT/1974/fr/Jo05674.pdf` |
| Décret 81-215 (attributions CRDA) | JORT 12/1981, pp. 365-367 | OCR `.../1981/fr/Jo01281.pdf` |
| Loi 63-18 (réforme agraire PPI) | JORT 1963 | corpus local / pist.tn |
| Loi 77-17 (Agence réforme agraire) | JORT 30/1977, pp. 1125-1132 | OCR `.../1977/fr/Jo03077.pdf` |
| Décret 77-627 (org. agence) | JORT 56/1977, pp. 2225-2227 | OCR `.../1977/fr/Jo05677.pdf` |
| Loi 82-67 (encouragement agric./pêche — cadre APIA) | JORT 54/1982, pp. 1691-1696 | OCR `.../1982/fr/Jo05482.pdf` (ref `loi-82-67` existe) |
| Décret 82-1484 (org. APIA) | JORT 77/1982, pp. 2606-2609 | OCR `.../1982/fr/Jo07782.pdf` |
| Loi 93-84 (groupements interprof.) | JORT 56/1993, pp. 1076-1078 | OCR `.../1993/fr/Jo05693.pdf` |
| Loi 90-73 (AVFA) | JORT 51/1990, pp. 1007-1008 | OCR `.../1990/fr/Jo05190.pdf` |
| Loi 90-72 (IRESA) | JORT 51/1990, p. 1007 | OCR `.../1990/fr/Jo05190.pdf` |
| Décret 2001-420 (org. ministère) | JORT 15/2001, pp. 312-332 | `.../2001/fr/Jo0152001.pdf` (couche texte à vérifier / image) |
| Loi 81-17 (ODESYPANO) | JORT 17/1981, pp. 523-524 | OCR `.../1981/fr/Jo01781.pdf` |

Texte **lu au mot et exploitable** : **Loi n° 96-4** (JORT 7/1996, `Jo00796.pdf`, couche texte OK).

---

## 4. Notions à glossaire (à vérifier/ajouter — proposées, non écrites)

- **CRDA** — commissariat régional au développement agricole (مندوبية جهوية للتنمية الفلاحية) ;
  source canonique : décret n° 74-847 ; attributions décret n° 81-215.
- **APIA** — Agence de promotion des investissements agricoles (وكالة النهوض بالاستثمارات الفلاحية) ;
  source : loi n° 82-67 ; décret n° 82-1484.
- **Agence foncière agricole (AFA)** — ex-Agence de la réforme agraire des périmètres publics irrigués
  (الوكالة العقارية الفلاحية) ; source : loi n° 77-17, renommée décret n° 99-1877 / loi n° 2000-29.
- **Périmètre public irrigué (PPI)** — source : loi n° 63-18.
- **Groupement interprofessionnel** (secteur agricole) (المجمع المهني المشترك) ; source : loi n° 93-84.
- **AVFA** — Agence de la vulgarisation et de la formation agricoles ; source : loi n° 90-73.
- **IRESA** — Institution de la recherche et de l'enseignement supérieur agricoles ; source : loi n° 90-72.
- **Centre technique agricole** — personne morale d'intérêt économique public (art. 1er loi n° 96-4).
- **Office de mise en valeur (des périmètres irrigués)** ; **ODESYPANO**, **ODS** (offices de
  développement régional).
(Formes arabes à confirmer au glossaire / sur intitulés arabes du miroir iort avant emploi.)

---

## 5. Références CSL candidates

**Déjà présentes** (à réutiliser telles quelles) :
- `loi-82-67` (fiscalité) — Loi n° 82-67 du 6 août 1982, encouragement investissements agriculture/pêche.
- `loi-88-18-code-investissements-agricoles` (fiscalité) — Code des investissements agricoles et de pêche
  (abrogé par loi 93-120 ; hors cadre institution, mentionné pour antécédent du régime d'incitation).

**À créer** (type `legislation`, `container-title` = « Journal officiel de la République tunisienne ») :

```json
{ "items": [
  { "id": "decret-74-847-crda", "type": "legislation",
    "title": "Décret n° 74-847 du 4 septembre 1974, portant création de commissariats régionaux au développement agricole",
    "title-short": "Décret n° 74-847 du 4 septembre 1974",
    "container-title": "Journal officiel de la République tunisienne", "issue": "56", "page": "1972",
    "issued": {"date-parts": [[1974,9,4]]},
    "note": "citation-key: decret-74-847-crda\nJORT n° 56/1974, p. 1972 (notice jort_cache.db). Fascicule scanné sans couche texte : articles non lus, OCR requise avant de citer un article." },
  { "id": "decret-81-215-crda-attributions", "type": "legislation",
    "title": "Décret n° 81-215 du 18 février 1981, fixant les attributions et l'organisation des commissariats régionaux au développement agricole",
    "title-short": "Décret n° 81-215 du 18 février 1981",
    "container-title": "Journal officiel de la République tunisienne", "issue": "12", "page": "365-367",
    "issued": {"date-parts": [[1981,2,18]]},
    "note": "citation-key: decret-81-215-crda-attributions\nJORT n° 12/1981, pp. 365-367. Scanné : articles non lus." },
  { "id": "loi-63-18-reforme-agraire-ppi", "type": "legislation",
    "title": "Loi n° 63-18 du 27 mai 1963, portant réforme agraire dans les périmètres publics irrigués",
    "title-short": "Loi n° 63-18 du 27 mai 1963",
    "container-title": "Journal officiel de la République tunisienne",
    "issued": {"date-parts": [[1963,5,27]]},
    "note": "citation-key: loi-63-18-reforme-agraire-ppi\nModifiée par loi n° 71-9. Scanné : articles non lus." },
  { "id": "loi-77-17-agence-reforme-agraire", "type": "legislation",
    "title": "Loi n° 77-17 du 16 mars 1977, portant création de l'Agence de la réforme agraire des périmètres publics irrigués",
    "title-short": "Loi n° 77-17 du 16 mars 1977",
    "container-title": "Journal officiel de la République tunisienne", "issue": "30", "page": "1125-1132",
    "issued": {"date-parts": [[1977,3,16]]},
    "note": "citation-key: loi-77-17-agence-reforme-agraire\nTexte complet JORT n° 30/1977, pp. 1125-1132 ; intitulé aussi n° 18/1977, pp. 651-652. Renommée « Agence foncière agricole » par décret n° 99-1877 et loi n° 2000-29. Scanné : articles non lus." },
  { "id": "decret-82-1484-apia", "type": "legislation",
    "title": "Décret n° 82-1484 du 29 novembre 1982, portant organisation et fonctionnement de l'Agence de promotion des investissements agricoles",
    "title-short": "Décret n° 82-1484 du 29 novembre 1982",
    "container-title": "Journal officiel de la République tunisienne", "issue": "77", "page": "2606-2609",
    "issued": {"date-parts": [[1982,11,29]]},
    "note": "citation-key: decret-82-1484-apia\nJORT n° 77/1982, pp. 2606-2609 ; modifié par décret n° 84-344. Scanné : articles non lus." },
  { "id": "loi-93-84-groupements-interprofessionnels", "type": "legislation",
    "title": "Loi n° 93-84 du 26 juillet 1993, relative aux groupements interprofessionnels dans le secteur agricole et agro-alimentaire",
    "title-short": "Loi n° 93-84 du 26 juillet 1993",
    "container-title": "Journal officiel de la République tunisienne", "issue": "56", "page": "1076-1078",
    "issued": {"date-parts": [[1993,7,26]]},
    "note": "citation-key: loi-93-84-groupements-interprofessionnels\nStatuts-type décret n° 94-1165 ; modifiée par loi n° 2005-16. Scanné : articles non lus." },
  { "id": "loi-90-73-avfa", "type": "legislation",
    "title": "Loi n° 90-73 du 30 juillet 1990, portant création de l'agence de la vulgarisation et de la formation agricoles",
    "title-short": "Loi n° 90-73 du 30 juillet 1990",
    "container-title": "Journal officiel de la République tunisienne", "issue": "51", "page": "1007-1008",
    "issued": {"date-parts": [[1990,7,30]]},
    "note": "citation-key: loi-90-73-avfa\nOrganisation décret n° 91-66. Scanné : articles non lus." },
  { "id": "loi-90-72-iresa", "type": "legislation",
    "title": "Loi n° 90-72 du 30 juillet 1990, portant création de l'institution de la recherche et de l'enseignement supérieur agricoles",
    "title-short": "Loi n° 90-72 du 30 juillet 1990",
    "container-title": "Journal officiel de la République tunisienne", "issue": "51", "page": "1007",
    "issued": {"date-parts": [[1990,7,30]]},
    "note": "citation-key: loi-90-72-iresa\nOrganisation décret n° 91-104. Scanné : articles non lus." },
  { "id": "loi-96-4-centres-techniques-agricoles", "type": "legislation",
    "title": "Loi n° 96-4 du 19 janvier 1996, relative aux centres techniques dans le secteur agricole",
    "title-short": "Loi n° 96-4 du 19 janvier 1996",
    "container-title": "Journal officiel de la République tunisienne", "issue": "7", "page": "203-204",
    "issued": {"date-parts": [[1996,1,19]]},
    "note": "citation-key: loi-96-4-centres-techniques-agricoles\nLUE AU MOT (couche texte OK). Art. 1er (personne morale d'intérêt économique public, autonomie financière), 2 (création par arrêté du ministre), 3 (sans capital, pas de distribution de bénéfices), 7 (missions : adaptation recherche, vulgarisation, productivité/qualité/coûts), 12 (ressources : fiscales affectées, produits, dons, ressources de l'État)." },
  { "id": "decret-2001-420-organisation-ministere-agriculture", "type": "legislation",
    "title": "Décret n° 2001-420 du 13 février 2001, portant organisation du ministère de l'agriculture",
    "title-short": "Décret n° 2001-420 du 13 février 2001",
    "container-title": "Journal officiel de la République tunisienne", "issue": "15", "page": "312-332",
    "issued": {"date-parts": [[2001,2,13]]},
    "note": "citation-key: decret-2001-420-organisation-ministere-agriculture\nAttributions : décret n° 2001-419 (même fascicule, pp. 310-311). Modifié par décrets n° 2010-625 et 2011-1560. Couche texte du fascicule à vérifier (relecture image)." },
  { "id": "loi-81-17-odesypano", "type": "legislation",
    "title": "Loi n° 81-17 du 9 mars 1981, portant création de l'Office de développement sylvo-pastoral du Nord-Ouest",
    "title-short": "Loi n° 81-17 du 9 mars 1981",
    "container-title": "Journal officiel de la République tunisienne", "issue": "17", "page": "523-524",
    "issued": {"date-parts": [[1981,3,9]]},
    "note": "citation-key: loi-81-17-odesypano\nRefondé « Office de développement du Nord-Ouest » par loi n° 94-85. Scanné : articles non lus." }
] }
```
(Dépôt cible : nouveau `precis/fr/<livre-agriculture>/references.json` à la création du livre ; d'ici
là, `loi-82-67` et `loi-88-18-…` restent au dossier fiscalité.)

---

## 6. Recherches infructueuses / à consigner

Aucune fiche `docs/recherches.yml` existante ne couvre ces institutions (vérifié le 10/11/2026 :
`recherches.py lister` ne renvoie que des objets retraites / temps de travail). **Fiches proposées**
(à créer par le rôle habilité ; je n'ai pas modifié le registre) :

- **`r-agri-org-ministere-post2014`** — objet : décret portant **organisation/attributions du
  ministère de l'Agriculture, des Ressources hydrauliques et de la Pêche** postérieur au décret
  n° 2011-1560 (refonte d'ensemble). `ou` : jort_cache (titres FR + **iort_ar**), corpus local, pist.tn.
  Requêtes lancées le 10/11/2026 : `titre like '%organisation du ministere de l%agriculture%'` et
  `'%attributions du ministere de l%agriculture%'` avec `jort_annee>=2012` → **seul** le décret
  présidentiel n° 2022-200 (modifiant le décret n° 95-99…) ressort, pas une organisation d'ensemble.
  **Couverture : jusqu'au 2026-11-10 pour les seuls titres français** ; une réorganisation à **titre
  arabe seul** (part élevée 2015-2019) n'est pas exclue → **terme arabe requis** : « تنظيم وزارة
  الفلاحة », « مشمولات وزارة الفلاحة ». Résultat : **aucun** (titres FR).
- **`r-agri-cotisations-groupements-interprof`** — objet : textes fixant les **cotisations
  interprofessionnelles** (taux, assiette, affectation) perçues par les groupements de la loi n° 93-84.
  Non cherché en fascicule à ce stade (au-delà de l'intitulé du cadre) → **à instruire**.

---

## 7. VERDICT

**Le chapitre « institution, tutelle et encadrement » TIENT**, et c'est le chapitre le plus solide du
livre candidat. Argument :

1. **Tous les textes fondateurs sont identifiés, datés et localisés** au fascicule et à la page (CRDA
   1974/1981 ; offices de mise en valeur 1960-1973 et réforme agraire PPI 1963 ; Agence de la réforme
   agraire 1977 → AFA 1999-2000 ; APIA 1982 ; groupements interprofessionnels, cadre 1993 après la
   vague sectorielle 1971-1984 ; AVFA 1990 ; IRESA 1990 ; centres techniques 1996 — ce dernier **lu au
   mot**). L'épine chronologique d'un chapitre de cadre (3-6 jalons) est largement couverte.
2. **Le flux budgétaire existe et est localisé** : PAP/RAP de la mission Agriculture (2015-2025, déjà
   dans `tunisia-data`) donnent institutions ↔ programmes et transferts ; les centres techniques et
   groupements portent des **ressources affectées** (art. 12 loi 96-4 ; FODECAP) ; la masse salariale
   des opérateurs passe par la CNRPS (liste du régime conventionnel, déjà au précis). Le chapitre n'est
   pas une coquille réglementaire : il a une matière distributive.
3. **Réserve** : le **contenu des articles** (missions exactes, attributions, ressources) de la quasi-
   totalité des textes de cadre n'est **pas encore lu** (fascicules scannés) — sauf la loi 96-4. Le
   chapitre *tient sur l'ossature* ; sa **rédaction fine exige une passe OCR** sur les ~12 fascicules du
   § 3 (pages connues : OCR ciblée, peu coûteuse). Tant que l'OCR n'est pas faite, les missions se
   disent par l'intitulé du texte, pas au mot.
4. **Frontière EP** : les offices de développement régional (ODESYPANO, ODS) et les offices de mise en
   valeur sont à la lisière tutelle/EP ; à cadrer avec le livre des entreprises publiques (ils y ont
   peut-être un statut d'opérateur) — n'empêche pas le chapitre de tenir.

Conclusion : **ouvrir le chapitre 2** ; prérequis de rédaction = **OCR ciblée** des fascicules du § 3.

---

## 8. Backlog (propositions — non reportées dans `docs/notes/backlog-precis.md`)

- **OCR ciblée** des 12 fascicules JORT du § 3 (pages connues) pour établir au mot missions,
  attributions et ressources des institutions agricoles ; prioriser CRDA (74-847, 81-215), APIA
  (82-67, 82-1484), groupements (93-84), AVFA/IRESA (90-73, 90-72), Agence réforme agraire (77-17).
- **Créer `docs/recherches.yml`** : fiches `r-agri-org-ministere-post2014` (avec termes arabes) et
  `r-agri-cotisations-groupements-interprof`.
- **Séries à dépouiller** : budget du ministère avant 2015 (lois de finances / lois de règlement) ;
  cotisations interprofessionnelles par groupement ; ressources affectées aux centres techniques
  (FODECAP) par organisme ; primes APIA (série au-delà de la valeur 2009 — rapports d'activité APIA,
  archives web non ouvertes).
- **Frontière à trancher avec le livre EP** : statut des offices de développement régional
  (ODESYPANO, ODS) et des offices de mise en valeur — opérateur (EP) vs encadrement (tutelle).
- **Ajouter au catalogue `tunisia-data/sources/`** : le cas échéant, rapports d'activité APIA et
  rapports de la Cour des comptes sur APIA/AFA/offices (non récupérés ici — aucune étude citée).
- **Références** : verser le bloc CSL du § 5 au `references.json` du futur livre agriculture ;
  réutiliser `loi-82-67` et `loi-88-18-code-investissements-agricoles`.
