# TVA — les réformes de 1988 à 2026 (dossier documentaire)

> Note **documentaire** pour le chapitre `precis/fr/fiscalite/_tva.qmd`. Elle ne rédige pas de
> prose de précis et ne modifie aucun fichier de `precis/`. Elle **part de**
> `docs/notes/fiscalite-tva-documentation.md` (code de 1988, calendrier, décrets de l'article 8
> sur l'électricité et les carburants) et n'en reprend que ce qu'il faut pour la chronologie. Elle
> y ajoute tout ce qui s'est passé **après le code**, loi de finances par loi de finances.
>
> **Établie le 24 septembre 2026.** Sources : `jort_cache.db` (métadonnées à jour au 18/09/2026),
> corpus local des fascicules (`PDFs-legislation-tunisie/PDFs/JORT/`, `PDFs/Lois_de_Finances/`),
> code consolidé de la DGELF (millésime 2023, français) et fascicules arabes pour 2022-2025.

## Mode d'emploi

**Degré de lecture**, indiqué pour chaque ligne :

- **[image]** : la page du JORT a été lue en image (outil de lecture PDF) ;
- **[texte]** : lu dans la couche texte du fascicule, par extraction page à page (y compris
  après décodage du décalage de 29 des fascicules 1999-2004, `outillage-sources.md` § 5) ;
- **[OCR]** : lu dans une océrisation `tesseract fra` faite pour cette note (fascicules
  1988-1993, sans couche texte) : le libellé est sûr, les chiffres et numéros tarifaires sont
  à relire à l'image avant d'être publiés ;
- **[AR]** : lu dans l'édition arabe seulement ;
- **[notice]** : **seul l'intitulé est connu** (notice de `jort_cache`), le texte n'a pas été lu.

**Pagination.** Sauf mention, « p. » est la pagination de l'**édition française** relevée page
à page dans le fascicule (pied de page). L'édition arabe a sa propre pagination depuis au moins
2014 ; elle est donnée « AR p. » quand elle a été mesurée. Les notices de `jort_cache` donnent,
pour 2019-2025, la pagination **arabe**.

- Éditions françaises **absentes de pist.tn** : JORT n° 104/2015 (LF 2016), n° 104/2019
  (LF 2020), n° 141/2022 (LF 2023), n° 144/2023 (LF 2024), n° 149/2024 (LF 2025)
  (`outillage-sources.md` § 3). Pour LF 2016, 2019, 2020, 2024 et 2025, la pagination
  française vient des PDF de `PDFs/Lois_de_Finances/`, qui portent l'en-tête et le pied de page
  du JORT français ; pour LF 2023 et LF 2026 (JORT n° 148/2025, dont le fichier « F » est
  l'arabe), il n'existe **que** la pagination arabe.
- Les PDF locaux des LF 2021, 2022 et 2023 dans `PDFs/Lois_de_Finances/` sont **corrompus**
  (`pdftotext` : « Couldn't read xref table ») ; LF 2021 et 2022 ont été lues dans les fascicules
  du corpus (`PDFs/JORT/2020/fr/Jo1282020.pdf`, `PDFs/JORT/2021/fr/Jo1192021.pdf`).

**Dates d'effet** (AGENTS.md, « Dater »). Les LF 1989 à 1993 ne portent **aucune clause spéciale
d'application** : leur dernière page, lue à l'image, passe directement du dernier article à la
formule de publication et d'exécution. Aucune date d'effet n'en est déduite ici. À partir de la
LF 1994, les lois examinées portent un article final « Les dispositions de la présente loi sont
applicables à compter du 1^er^ janvier N », sous réserve de dates propres à certains articles.
Clause **lue jusqu'à la date** pour les LF 1994 (art. 77), 1995 (art. 100), 1996 (art. 68), 1997,
1998 (art. 90), 1999, 2000 (art. 73),
2001 (art. 68), 2002 (art. 97), 2003 (art. 87), 2004 (art. 105), 2005 (art. 89), 2006 (art. 62), 2007
(loi 2006-80, art. 19), 2008 (art. 64), 2009 (art. 39), 2010 (art. 56), 2013 (art. 79),
2014 (art. 95), 2015 (art. 46), 2016 (art. 92), 2017 (art. 79), 2018 (art. 67), 2019 (art. 90),
2020 (art. 58), 2021 (article final, § 1), 2022 (décret-loi n° 2021-21, art. 73), 2023, 2024,
2025 et 2026 (ces quatre dernières en arabe : « تطبق أحكام هذا القانون بداية من غرة جانفي »).
Une date propre à l'article prime toujours (ex. LF 1996, art. 38, 39, 42, 46).

---

## Résultat principal — ce que la chronologie change au chapitre

1. **Le premier taux de 10 % inscrit dans la loi date du 1^er^ janvier 1995, pas de 1998.**
   (Des décrets de l'article 8 ont pu réduire des taux auparavant : les 144 intitulés de 1988-1997
   n'ont pas été triés, voir point 9.) L'article 56 de la LF 1995
   (loi n° 94-127) soumet au taux de 10 % l'informatique, les téléviseurs et le transport de
   marchandises, retirés du tableau B (6 %) par l'article 57 [texte]. Le tableau
   `tbl-tva-taux` du chapitre (« 1^er^ juillet 1988 → 31 déc. 1997 : 17 % / 6 % / 29 % »)
   omet donc un taux pendant trois ans. La LF 1996 l'étend, au 1^er^ avril puis au
   1^er^ septembre 1996, aux professions libérales, à l'hôtellerie et à la restauration.
2. **Le tableau C (29 %) est retouché presque chaque année bien avant sa suppression de 2007**,
   surtout pour en retirer des produits : LF 1991 (art. 35, retraits ; mais art. 36, **ajout** du
   verre opalin), 1992 (art. 37-38), 1993 (art. 83-84, 94, 109), 1994 (art. 50-51), 1995
   (art. 86), 1998 (art. 27). Pour la LF 1993 (art. 119) et la LF 2005 (art. 71-72,
   climatiseurs), **seul l'intitulé est connu** : le sens du mouvement n'est pas établi.
3. **Aucun texte identifié n'a mis en application les régimes forfaitaires du code dans leur
   rédaction de 1988.** Différés par le décret n° 88-1109 (art. 16, 17 I et 17 II-1), les
   articles 16 et 17 I sont **remplacés** par la LF 1990
   (loi n° 89-115, art. 24 à 26) : taxe forfaitaire annuelle de TVA pour les petites entreprises
   individuelles, droit forfaitaire simplifié pour les cafetiers et les coiffeurs [image]. Ils
   sont **abrogés** par la LF 1993 (loi n° 92-122, art. 105), qui rend l'impôt forfaitaire sur le
   revenu « libératoire de la taxe sur la valeur ajoutée » (art. 103) [image]. Reste le forfait
   des transporteurs (art. 17 II) : aucun texte identifié ne le met en application entre 1988 et
   1997 ; la LF 1998 (art. 29) le réécrit et le rend imputable sur la TVA du régime réel [image].
   La LF 1990 ne porte pas de clause spéciale d'application et sa date d'effet n'est pas établie
   ici (« Non établi », 1). La fiche
   `r-tva-mise-en-application-post-1989` avance donc, sans être résolue (§ 9.1).
4. **Les télécommunications, exonérées en 1995, sont taxées au taux normal depuis le
   1^er^ janvier 2003** (LF 1995 art. 85 ; LF 2002 art. 66 à 70 ; décret n° 2002-3356).
5. **Professions libérales : 6 % → 10 % (1^er^ avril 1996) → 12 % (2007) → 13 % (2018) →
   taux normal, soit 19 % (1^er^ janvier 2023).** Le dernier passage est une **déduction** :
   l'article 44 du décret-loi n° 2022-79 (LF 2023) [AR] supprime le tiret qui les plaçait à 13 %,
   et le taux de 19 % découle de l'article 7, alinéa 1^er^ ; aucun texte ne l'écrit pour elles. La LF 2017 les transfère du tableau B bis à l'article 7 **à taux inchangé**
   (12 %) [texte] : l'entrée CSL proposée dans l'ancienne note (« passage des professions
   libérales de 6 % à 12 % ») est **fausse** sur ce point.
6. **Logements vendus par les promoteurs : exonérés (2001) → 13 % (2018) → 7 % ou taux normal
   (2025).** La hausse à 19 % votée en 2017 pour 2020 a été **reportée trois fois** (2021, 2024,
   2025) puis abandonnée pour un barème à deux branches, selon un seuil de 400 000 dinars hors
   taxe (LF 2025 art. 64).
7. **Le champ s'élargit massivement en 2016-2017** : la LF 2016 (art. 30-31) fait passer à 6 %
   une série d'opérations jusque-là exonérées (dont l'enseignement privé), refond les tableaux A,
   B et B bis ; la LF 2017 (art. 16 à 28) poursuit et supprime le tableau B bis.
8. **Le commerce de détail est retouché trois fois après 1996** : les médicaments sortent de
   l'exonération au détail (LF 2016 art. 31-4, effet différé à 2017 puis 2020) puis y rentrent,
   gros et détail, avec abandon des rappels (LF 2021 art. 25) ; les détaillants en boissons
   alcoolisées deviennent assujettis (LF 2022 art. 33).
9. **L'article 8 du code sert dès 1988, pas seulement à partir de 1998.** `jort_cache` compte
   **144 décrets** signés de 1988 à 1997 dont l'intitulé mentionne la TVA — pour l'essentiel des
   suspensions ou réductions, les deux décrets de calendrier compris (ex. décret n° 88-2002 du
   27 décembre 1988 ; décrets n° 95-1256 et 96-771, cahiers scolaires à 10 %) [notice]. La série électricité-carburants de 1998-2014 n'en est qu'un cas particulier.

---

## 1. Chronologie des taux

### 1.1 Vue d'ensemble corrigée (dates d'effet)

| Période | Normal | Réduit(s) | Majoré | Textes |
|---|---|---|---|---|
| 1^er^ juil. 1988 → 31 déc. 1994 | 17 % | 6 % (tableau B) | 29 % (tableau C) | code, art. 7 |
| 1^er^ janv. 1995 → 31 déc. 1997 | 17 % | 6 % ; **10 % hors code** | 29 % | LF 1995, art. 56-58 |
| 1^er^ janv. 1998 → 31 déc. 2001 | 18 % | 6 % ; 10 % hors code | 29 % | LF 1998, art. 25 |
| 1^er^ janv. 2002 → 31 déc. 2006 | 18 % | 6 % ; 10 % (tableau B bis) | 29 % | LF 2002, art. 82-84 |
| 1^er^ janv. 2007 → 31 déc. 2017 | 18 % | 6 % ; 12 % | supprimé | loi 2006-80, art. 13 et 17 |
| 1^er^ janv. 2018 → aujourd'hui | 19 % | 7 % ; 13 % | — | LF 2018, art. 43 |

À partir de 2017, le taux intermédiaire n'a plus de tableau : il est écrit dans l'article 7,
n° 3 (LF 2017, art. 27). Sa liste s'est depuis **réduite** : irrigation (2019), professions
libérales (2023), logements (2025) en sont sortis ; il ne porte plus, en 2026, que les produits
pétroliers et l'électricité domestique au-delà de 300 kWh par mois.

### 1.2 Les textes, un par un

| Date d'effet | Texte | Art. | Avant → après | Lecture |
|---|---|---|---|---|
| 1^er^ janv. 1995 | Loi n° 94-127 du 26/12/1994 (LF 1995), JORT n° 103 des 30-31/12/1994, p. 2047 | 56 | création hors code d'un taux de **10 %** : machines de traitement de l'information (84-71, 84-73) et services informatiques ; téléviseurs (85-29, 85-40, 85-04) ; transport de marchandises sauf produits agricoles et de pêche | [texte] |
| 1^er^ janv. 1995 | idem, p. 2047 | 57-58 | tableau B (6 %) : suppression des n° II-5, II-6 et III-7 ; III-3 réécrit (transport de personnes et de produits agricoles et de pêche seulement) | [texte] |
| 1^er^ janv. 1995 | idem, p. 2050 | 86 | produits du tableau « M bis » retirés du tableau C : 29 % → 17 % (« intégration industrielle ») | [texte] ; liste non lue |
| 1^er^ janv. 1995 | idem, p. 2051 | 100 | « Les dispositions de la présente loi sont applicables à compter du 1^er^ janvier 1995 » | [texte] |
| **1^er^ avril 1996** | Loi n° 95-109 du 25/12/1995 (LF 1996), JORT n° 104 des 29-31/12/1995, p. 2371-2372 | 37 § 6, 38 | architectes, ingénieurs-conseils, avocats, notaires, huissiers-notaires, interprètes, conseils juridiques et fiscaux, comptables, experts : 6 % → **10 %** ; contrats enregistrés au plus tard le 31/03/1996 maintenus à 6 % jusqu'au 31/12/1996 ; tableau B § I réduit aux professions de santé et aux géomètres de l'immatriculation agricole | [texte] |
| **1^er^ sept. 1996** | idem, p. 2371-2372 | 37 § 1-5, 39 | hôtellerie, excursions et hébergement des touristes non résidents par les agences, plongée et promenades en mer, restauration : 6 % → **10 %** ; suppression des n° 1, 8, 10, 12 et 13 du § III du tableau B | [texte] |
| 1^er^ janv. 1996 | idem, p. 2371 | 36 | équipements du tableau « P » soumis à 10 %, « sans préjudice du code d'incitations aux investissements » | [texte] ; clause générale : art. 68, p. 2375 [image] |
| date fixée par décret | idem, p. 2372 | 40 | électricité et gaz (B II-2), huiles de pétrole (B III-4) retirés du tableau B (6 %) — voir l'ancienne note, § 4 | [texte] |
| 1^er^ janv. 1997 | Loi n° 96-113 du 30/12/1996 (LF 1997), JORT n° 105 du 31/12/1996, p. 2580 | 19 | équipements de l'article 18 de la même loi soumis à 10 %, sauf équipements agricoles et de pêche | [texte] |
| 1^er^ janv. 1998 | Loi n° 97-88 du 29/12/1997 (LF 1998), JORT n° 104 des 30-31/12/1997, p. 2437 | 25 | taux normal 17 % → **18 %** | [image] |
| 1^er^ janv. 1998 | idem, p. 2437 | 26 | suppression du § 2 de l'art. 56 de la LF 1995 : téléviseurs 10 % → 18 % | [image] |
| 1^er^ janv. 1998 | idem, p. 2437 | 27 | produits du tableau « L » retirés du tableau C (29 %) | [image] ; liste non lue |
| 1^er^ janv. 1998 | idem, p. 2437 | 28 | équipements fabriqués localement (code d'incitations, art. 9, 50 § 2 et 56) acquis après l'entrée en activité : 10 % | [image] |
| 1^er^ janv. 1998 | idem | 90 | clause finale : « applicables à compter du 1^er^ janvier 1998 » (l'ancienne note écrivait « droit commun de la loi de finances ») | [texte] |
| 1^er^ janv. 2000 | Loi n° 99-101 du 31/12/1999 (LF 2000), JORT n° 105 du 31/12/1999, p. 2741 | 19 | services de formation : 18 % → 10 % | [texte] |
| 1^er^ janv. 2001 | Loi n° 2000-98 du 25/12/2000 (LF 2001), JORT n° 104 du 29/12/2000, p. 3178 | 40 | services Internet : 18 % → 10 % | [texte] |
| 1^er^ janv. 2002 | Loi n° 2001-123 du 28/12/2001 (LF 2002), JORT n° 104 du 28/12/2001, p. 4255 | 41 | collecte des déchets de plastique : 18 % → 10 % | [notice] |
| 1^er^ janv. 2002 | idem, p. 4260 | 82-84 | taux de 10 % incorporé à l'art. 7 (n° 3), tableau B bis ; abrogation des textes épars | [image] (ancienne note) |
| 1^er^ janv. 2004 | Loi n° 2003-80 du 29/12/2003 (LF 2004), JORT n° 104 du 30/12/2003, p. 3726 | 36 | hébergement hôtelier vendu par les agences aux résidents : 10 % | [notice] |
| 1^er^ janv. 2006 | Loi n° 2005-106 du 19/12/2005 (LF 2006), JORT n° 101 du 20/12/2005, p. 3601 | 41 | services de certification électronique : 10 % (B bis, n° 12 bis) | [notice] |
| **1^er^ janv. 2007** | Loi n° 2006-80 du 18/12/2006, JORT n° 101 du 19/12/2006, p. 4302 | 13 | suppression du n° 2 de l'art. 7 : fin du taux de **29 %** | [texte] |
| 1^er^ janv. 2007 | idem, p. 4302 | 14 | parfums, produits de beauté, etc. ajoutés au tableau du droit de consommation | [texte] |
| 1^er^ janv. 2007 | idem, p. 4303 | 17 | **10 % → 12 %**, dans le code et « partout où il est prévu » | [texte] |
| 1^er^ janv. 2007 | idem, p. 4303 | 19 | clause finale : « à compter du 1^er^ janvier 2007 » | [texte] |
| 1^er^ janv. 2014 | Loi n° 2013-54 du 30/12/2013 (LF 2014), JORT n° 105 du 31/12/2013, p. 3674 | 33 | papier pour l'impression des revues : 18 % → 6 % | [notice] |
| 1^er^ janv. 2015 | Loi n° 2014-59 du 26/12/2014 (LF 2015), JORT n° 105 du 30/12/2014, p. 3469 | 36 | électricité domestique et d'irrigation, produits pétroliers inscrits au tableau B bis (12 %) : fin des décrets annuels | [image] (ancienne note) ; AR : art. 37 lu p. 3822, art. 36 non localisé |
| 1^er^ janv. 2016 | Loi n° 2015-53 du 25/12/2015 (LF 2016), JORT n° 104 du 29/12/2015, p. 3147 | 31 § 2-3 | produits de l'annexe 5 ajoutés à 6 % (tableau B) ou 12 % (B bis) ; tableaux A, B et B bis remplacés par des tableaux « nouveaux » | [texte] (PDF local) |
| 1^er^ janv. 2017 | Loi n° 2016-78 du 17/12/2016 (LF 2017), JORT n° 105 du 27/12/2016, p. 3834-3836 | 24-26 | tableau B nouveau : suppression du n° 8 du § I ; ajouts à 6 % (intrants agricoles et de pêche, informatique 84-71, cahiers scolaires, collecte des déchets plastiques…) ; taux de 12 % de l'art. 19 de la LF 2012 ramené à 6 % | [texte] ; AR p. 4131-4133 |
| 1^er^ janv. 2017 | idem, p. 3835-3836 | 27 | art. 7 n° 3 réécrit « au taux de 12 % » : produits pétroliers 27-10 et 27-11, électricité domestique et d'irrigation, **professions libérales** (liste de 1996, « conseils juridiques » en moins) ; restaurants et cafés de 1^re^ catégorie et enseignement privé reformulés au tableau B ; **tableau B bis abrogé** | [texte] ; AR p. 4133 |
| **1^er^ janv. 2018** | Loi n° 2017-66 du 18/12/2017 (LF 2018), JORT n° 101 du 19/12/2017, p. 4281 | 43 | **18 → 19 %, 6 → 7 %, 12 → 13 %** « là où il est prévu » | [texte] ; AR p. 4279 |
| exceptions | idem | 67 § 2-3 | l'art. 43 ne s'applique ni aux marchandises expédiées avant l'entrée en vigueur et mises directement à la consommation, ni aux montants payés jusqu'au 31/12/2018 sur des marchés publics conclus avant le 1^er^ janvier 2018 | [texte] |
| 1^er^ janv. 2019 | Loi n° 2018-56 du 27/12/2018 (LF 2019), JORT n° 104 du 28/12/2018, p. 4549 | 64 | téléphonie et internet fixes (ADSL) des particuliers : 19 % → 7 % (tableau B, § II n° 29) | [texte] (PDF local) ; AR p. 5461 |
| 1^er^ janv. 2019 | idem, p. 4549 | 65 | électricité d'irrigation agricole : 13 % → 7 % (tableau B, § I n° 29) | [texte] (PDF local) ; AR p. 5461 |
| 1^er^ janv. 2019 | idem, p. 4547 | 60 | panneaux solaires (EX 85-41) : 7 % (tableau B, n° 18 quater) | [texte] |
| 1^er^ janv. 2021 | Loi n° 2020-46 du 23/12/2020 (LF 2021), JORT n° 128 du 25/12/2020, p. 3132 | 26 | 7 % étendu aux mêmes services facturés par les opérateurs aux fournisseurs d'accès | [texte] |
| **1^er^ janv. 2023** | Décret-loi n° 2022-79 du 22/12/2022 (LF 2023), JORT n° 141 du 23/12/2022, AR p. 4069 | 44 | suppression du 3^e^ tiret de l'art. 7 n° 3 : **professions libérales 13 % → taux normal (19 %, par l'art. 7 al. 1^er^ — déduction)** ; chirurgie esthétique non thérapeutique exclue du 7 % des services médicaux (tableau B, § II n° 1) | [AR] |
| 1^er^ janv. 2023 | idem, AR p. 4064 | 24 | bornes de recharge des véhicules électriques : 7 % (jusqu'au 31/12/2023 d'après l'intitulé) | [AR] partiel |
| 1^er^ janv. 2024 | Loi n° 2023-13 du 11/12/2023 (LF 2024), JORT n° 144 du 12/12/2023, p. 3481 (AR p. 6449 mesurée ; notice : 6444) | 50 | véhicules, bicyclettes et motocycles électriques : 7 % (tableau B, n° 18 quinquies) | [texte] (PDF local) |
| 1^er^ janv. 2025 | Loi n° 2024-48 du 09/12/2024 (LF 2025), JORT n° 149 du 10/12/2024, p. 3428 ; AR p. 6426 | 31 | électricité basse tension domestique : 13 % au-delà de 300 kWh/mois ; 7 % en deçà (tableau B, n° 30) | [texte] (PDF local) |
| 1^er^ janv. 2025 | idem, p. 3449 ; AR p. 6446 | 59 | olives conservées provisoirement (07112010) : 7 % (tableau B, n° 21 bis) | [texte] |
| 1^er^ janv. 2026 | Loi n° 2025-17 du 12/12/2025 (LF 2026), JORT n° 148 du 12/12/2025, AR p. 4241 | 46 | intrants non fabriqués localement pour les batteries au lithium : 7 % | [AR] |
| 1^er^ janv. 2026 | idem, AR p. 4241 | 47 | véhicules hybrides rechargeables ajoutés au n° 18 quinquies (7 %) | [AR] |

---

## 2. Chronologie du champ d'application

| Date d'effet | Texte | Art. | Avant → après | Lecture |
|---|---|---|---|---|
| 1^er^ juil. 1988 | décret n° 88-1109 | 1 | code applicable, sauf grossistes (art. 1^er^ II-3) et forfaits (art. 16-17) | [image] (ancienne note) |
| 1^er^ oct. 1989 | décret n° 89-1222 | 1 | commerce de gros, sauf alimentation générale | [image] (ancienne note) |
| 1^er^ juil. 1996 | LF 1996, p. 2372-2373 | 43, 46 | commerce de détail au-delà de 100 000 D de chiffre d'affaires ; exonération à la revente des produits alimentaires, des médicaments et des produits homologués | [texte] |
| 1^er^ juil. 1996 | idem, p. 2372 | 44 | art. 6 I, al. 10 : ventes des assujettis à des non-assujettis taxées sur une base **majorée de 25 %** (sauf alimentation, médicaments, produits homologués, ventes à l'État et ventes des détaillants) ; al. 11 : assiette des détaillants par taux | [texte] |
| 1^er^ juil. 1996 | idem, p. 2372 | 45 | obligations de facturation et de tenue du livre des détaillants | [texte] |
| 1^er^ janv. 2003 | LF 2003 (loi n° 2002-101), JORT n° 102 du 17/12/2002, p. 2882 | 52 | majoration de 25 % étendue à une liste de produits de consommation | [notice] |
| 1^er^ janv. 2003 | LF 2002, p. 4258 ; décret n° 2002-3356 du 30/12/2002, JORT n° 106 du 31/12/2002, p. 3194 | 66-70 | n° 48 du tableau A réduit à la radio-télédiffusion : **télécommunications taxées** (18 %) ; redevance de 5 % (art. 68) exclue de l'assiette (art. 69) ; date fixée au 1^er^ janv. 2003 par le décret, art. 1^er^ | [texte] |
| 1^er^ janv. 2016 | LF 2016, p. 3146-3147 | 30 | passent au tableau B (6 %) : papiers de l'agence TAP, publications touristiques, aéronefs, absorbeurs solaires, matériels de nettoiement des collectivités, peaux brutes, matériel ferroviaire, chauffe-eau solaires, restaurants touristiques classés, restauration des étudiants, **enseignement primaire à supérieur, auto-écoles, garderies, formation informatique**, séjours vendus par les agences aux non-résidents, radio-télédiffusion, messages de presse, affrètement international | [texte] (PDF local) |
| 1^er^ janv. 2016 | idem, p. 3147 | 31 § 1 | abrogés du tableau A : n° 3, 9, 10, 20 b-c, 21, 22, 25 a-b, 27, 28 g-i, 30 bis, 47, 48 | [texte] |
| 1^er^ sept. 2016 | idem, p. 3147 | 31 § 5 | entrée en vigueur du n° 6 du § II du tableau B nouveau (enseignement) | [texte] |
| 1^er^ janv. 2016 | idem, p. 3147 | 33 | art. 6 I-9 : TVA sur la marge pour les achats des commerçants auprès de **tout non-assujetti** (et non plus des seuls forfaitaires) | [texte] |
| 1^er^ janv. 2017 | LF 2017, p. 3832 ; AR p. 4130 | 16 | abrogés du tableau A nouveau : § I n° 6, 8, 28, 30, 38, 48, 49, 50, 54 ; § II n° 9 | [texte] ; contenu des numéros non rapproché |
| 1^er^ janv. 2017 | idem, p. 3833 ; AR p. 4131 | 20 | art. 1^er^ II-5 bis : **ventes de lots de terrain par les promoteurs immobiliers** | [texte] |
| 1^er^ janv. 2017 | idem, p. 3833 | 21 | livraisons à soi-même : immobilisations « corporelles **et incorporelles** » | [texte] |
| 1^er^ janv. 2022 | Décret-loi n° 2021-21 du 28/12/2021 (LF 2022), JORT n° 119 du 28/12/2021, p. 3088 ; AR p. 3264 | 33 | **boissons alcoolisées, vins et bières** exclus de l'exonération au détail ; leurs détaillants assujettis (art. 2 III) ; déduction de la TVA sur stocks au 31/12/2021 | [texte] |

**Médicaments au stade de la revente** — même tableau, à part parce que la date a bougé trois fois :

| Date | Texte | Art. | Contenu | Lecture |
|---|---|---|---|---|
| — | LF 2016, p. 3147 | 31 § 4 | supprime « les médicaments, les produits pharmaceutiques » de l'exonération au détail (art. 1^er^ II-11) | [texte] |
| 1^er^ janv. 2017 | Loi n° 2017-1 du 03/01/2017 (LFC 2016), JORT n° 2 du 06/01/2017, p. 60 | 3 | « nonobstant l'article 92 » de la LF 2016, l'art. 31 § 4 s'applique « à compter du 1^er^ janvier 2017 » | [texte] |
| 1^er^ janv. 2020 | Loi n° 2019-78 du 23/12/2019 (LF 2020), JORT n° 104 du 27/12/2019, p. 4432 ; AR p. 4705 | 30 | même disposition, applicable « à compter du 1^er^ janvier 2020 » | [texte] (PDF local) |
| 1^er^ janv. 2021 | LF 2021, p. 3132 ; AR p. 3382 | 25 | vente des médicaments et produits pharmaceutiques exclue du champ au gros (art. 1^er^ II-3) et exonérée au détail (II-11) ; **abandon définitif** de la TVA due antérieurement, sans restitution | [texte] |

---

## 3. Les régimes forfaitaires

| Date d'effet | Texte | Art. | Contenu | Lecture |
|---|---|---|---|---|
| différé | décret n° 88-1109 | 1 | art. 16 et 17 I et II-1 du code non mis en application ; aucun décret ultérieur identifié | [image] (ancienne note) |
| date d'effet non établie (aucune clause spéciale dans la LF 1990) | Loi n° 89-115 du 30/12/1989 (LF 1990), JORT n° 88 des 29-31/12/1989, p. 2146 | 24 | art. 16 I-II nouveaux : **taxe forfaitaire annuelle** pour les entreprises individuelles à établissement unique, non importatrices ni exportatrices, dont le chiffre d'affaires ne dépasse pas 15 000 D (services), 20 000 D (consommation sur place), 30 000 D (autres) ; barème en dinars par tranche (taux de 17 % et 29 %) | [image] |
| idem | idem, p. 2147 | 25 | art. 16 IV-VI : déclaration en mars, paiement en 1 à 4 échéances, option pour le réel | [image] |
| idem | idem, p. 2147-2148 | 26 | art. 17 I nouveau : **droit forfaitaire simplifié** des petits professionnels et artisans, par nombre d'employés et zone ; barèmes des cafetiers de 1^re^ catégorie et des coiffeurs pour hommes | [image] |
| idem | Loi n° 90-111 (LF 1991), JORT n° 86 des 28-31/12/1990, p. 2052 | 34 | art. 6 I-9 : TVA sur la marge pour les ventes de produits achetés aux forfaitaires | [OCR] |
| date d'effet non établie (aucune clause spéciale dans la LF 1993) | Loi n° 92-122 du 29/12/1992 (LF 1993), JORT n° 88 du 31/12/1992, p. 1676-1677 | 100-103 | « unification et simplification du régime forfaitaire » dans le code de l'IRPP ; art. 103 : « L'impôt forfaitaire est libératoire de la taxe sur la valeur ajoutée » | [image] |
| idem | idem, p. 1677 | 104 | option (art. 2 I-3) ouverte aux forfaitaires de l'IRPP ; exclue pour les opérations exonérées sauf à l'exportation | [image] |
| idem | idem, p. 1677 | 105 | **abrogation de l'art. 16 et de l'art. 17 § I** | [image] |
| 1^er^ janv. 1998 | LF 1998, p. 2437 | 29 | art. 17 II : taxe forfaitaire mensuelle des transports terrestres (1 D/tonne, 1 D/place), sauf louage et taxi ; « assujettissement de toutes les catégories de transport terrestre au régime normal » | [image] |
| 1^er^ janv. 1998 | idem | 30 | art. 10 : pas de déduction pour les achats auprès des forfaitaires de l'IRPP | [texte] |
| 1^er^ janv. 2002 | LF 2002, p. 4261 | 89-90 | renvois de l'art. 6 aux art. 16 et 17 remplacés par l'art. 44 IV du code de l'IRPP | [texte] |

---

## 4. Régimes particuliers (sélection)

| Date d'effet | Texte | Art. | Contenu | Lecture |
|---|---|---|---|---|
| — | LF 1992, JORT n° 90 du 31/12/1991, p. 2090 | 68 | art. 13 (régime suspensif des alcools) abrogé | [OCR] |
| non relevée (LF 1993) | LF 1993, p. 1678 | 114 | mention obligatoire, sur facture, de la TVA suspendue ; relevé trimestriel | [OCR] |
| 1^er^ sept. 1996 | LF 1996, p. 2372 | 41-42 | restitution du crédit relevée à 40 % pour le crédit lié aux investissements | [texte] |
| 1^er^ janv. 1998 | LF 1998, p. 2438 | 36-38 | **retenue à la source** de 50 % de la TVA par l'État, les collectivités et les entreprises publiques (art. 19 bis) ; fait générateur à l'encaissement pour ces marchés (art. 5-6) | [texte] |
| 1^er^ janv. 1999 | LF 1999, JORT n° 104 du 29/12/1998, p. 2507 | 57 | option ouverte hors champ et aux forfaitaires ; exclue pour les exonérés, sauf exportation et fourniture d'assujettis | [texte] |
| 1^er^ janv. 2016 | LF 2016, p. 3148 | 34 | retenue à la source TVA : 50 % → 25 % | intitulé lu, texte non lu |
| 1^er^ janv. 2022 | LF 2022, p. 3097 | 52 | fin de la suspension pour les sociétés de commerce international et les entreprises de services non totalement exportatrices | [texte] |

Crédit de TVA, régime suspensif (art. 11, 13 bis-sexies), finance islamique et retenue à la
source (LF 2003 art. 55-56, LF 2004 art. 72-74, LF 2013 art. 42, etc.) : **seul l'intitulé est
connu ici** (voir les notices de `jort_cache`, requête de la § 7).

---

## 5. Exonérations majeures et logement

### 5.1 Le logement vendu par les promoteurs

| Date d'effet | Texte | Art. | Avant → après | Lecture |
|---|---|---|---|---|
| 1^er^ janv. 2001 | LF 2001, p. 3181 | 63 | tableau A, n° 50 : vente des immeubles bâtis à usage exclusif d'habitation par les promoteurs immobiliers, et dépendances : **exonérée** | [texte] |
| 1^er^ janv. 2016 | LF 2016, annexe 1 | 31 § 3 | l'exonération devient le n° 53 du § I du tableau A nouveau | [texte] |
| **1^er^ janv. 2018** | LF 2018, p. 4281 ; AR p. 4279 | 44 | n° 53 réduit aux logements sociaux financés par le FOPROLOS ; les autres ventes passent au taux de **13 %** (4^e^ tiret ajouté à l'art. 7 n° 3) ; 19 % prévu au **1^er^ janv. 2020** (§ 3) ; contrats et promesses conclus avant le 1^er^ janv. 2018 restent exonérés (§ 4) | [texte] |
| — | LF 2019, p. 4553 ; AR p. 5466 | 79 | 19 % reporté au **1^er^ janv. 2021** ; déduction de la TVA sur stocks au 31/12/2017 (inventaire avant le 31/03/2019) | [texte] (PDF local) |
| — | LF 2020, p. 4432 ; AR p. 4706 | 31 | 19 % reporté au **1^er^ janv. 2024** | [texte] (PDF local) |
| — | LF 2024, p. 3477 ; AR p. 6445 | 39 | 19 % reporté au **1^er^ janv. 2025** | [texte] (PDF local) |
| **1^er^ janv. 2025** | LF 2025, p. 3449 ; AR p. 6447 | 64 | 4^e^ tiret de l'art. 7 n° 3 abrogé (fin du 13 %) ; tableau B, n° 31 : **7 %** si le prix ne dépasse pas **400 000 D hors taxe** ; au-delà, faute d'autre taux, le taux normal de 19 % (art. 7 al. 1^er^) — **déduction, non écrite par l'article** | [texte] (PDF local) |

### 5.2 Autres exonérations et reclassements notables

| Date d'effet | Texte | Art. | Contenu | Lecture |
|---|---|---|---|---|
| LF 1989 | Loi n° 88-145 du 31/12/1988 (LF 1989), JORT n° 87 des 30-31/12/1988, p. 1794-1795 | 23-25 | ajouts au tableau A (dont raffinage et conditionnement des huiles, forage d'eau) ; ajouts au tableau B (restauration, distribution et projection de films, séjours des agences de voyages, fruits et légumes transformés) ; lessives retirées du tableau C | [OCR] **médiocre**, à relire à l'image |
| LF 1991 | LF 1991, p. 2052 | 33 | vente d'eau destinée à l'agriculture exonérée (tableau A n° 14) | [OCR] |
| LF 1991 | idem, p. 2055 | 60 | papier journal exonéré (n° 19 a), sous caution | [OCR] |
| LF 1992 | LF 1992, p. 2085-2086 | 35-42 | tableau B : huiles acides pour savon, attractions foraines, maïs, plongée ; bicyclettes taxées (n° 25 supprimé) ; raffinage des huiles végétales et services aériens exonérés | [OCR] |
| LF 1993 | LF 1993, p. 1674-1675 | 79-92 | artisanat (A n° 46, B n° 12), équipements municipaux (A n° 47), transport mixte rural et bus pour handicapés exonérés (A n° 28 d-f) | [OCR] |
| 1^er^ janv. 1994 | Loi n° 93-125 (LF 1994), JORT n° 100 du 31/12/1993, p. 2199-2200 | 52-54, 60-61 | location d'immeubles par les collectivités et les non-assujettis ; location de navires et aéronefs du transport international ; insecticides agricoles ; ordures municipales ; prêts de la CPSCL | [OCR] |
| 1^er^ janv. 1995 | LF 1995, p. 2049-2050 | 76, 81-85, 88 | logements étudiants, pièces agricoles, engrais, services portuaires, **télécommunications** (n° 48), équipements de maîtrise de l'énergie | [texte] / [notice] |
| 1^er^ janv. 2014 | LF 2014, p. 3674, 3686 | 31-32, 64-65 | secteur culturel exonéré ; fin de l'exonération des soins aux non-résidents | [notice] |
| 1^er^ janv. 2021 | LF 2021, p. 3132 | 27 | dons aux associations des personnes handicapées | [texte] |

---

## 6. Références candidates (pour le bibliographe)

**Déjà présentes, à réutiliser** (vérifiées dans `precis/fr/fiscalite/references.json` ou
`precis/fr/references.json`) : `loi-88-61-tva`, `decret-88-1109-calendrier-tva`,
`decret-89-1222-calendrier-tva-gros`, `decret-88-2002-suppressions`, `loi-88-145-lf-1989`,
`loi-89-115-lf-1990`, `lf-1991`, `lf-1992`, `lf-1993`, `lf-1994`, `lf-1995`, `lf-1996`,
`lf-1997`, `lf-1998`, `lf-1999`, `loi2001-123-lf2002` (partagée), `lf-2003`, `lf-2004`,
`lf-2005`, `lf-2006`, `loi-2006-80-reduction-taux`, `lf-2007`, `loi-2007-70-lf-2008`, `lf-2010`,
`lf-2011`, `lf-2013`, `lf-2014`, `lfc-2014`, `lf-2015`, `lf-2016`, `lf-2017`, `lf-2018`
(partagée), `loi2018-56-lf2019` (partagée), `lf-2020`, `lf-2021`, `lf-2022` (partagée),
`lf-2023` (partagée), `lf-2024`, `lf-2025` (partagée), `lf-2026` (partagée),
`dgelf-code-tva-2023`.

**Pages précises pour les citations de `_tva.qmd`** (le champ `page` des entrées peut viser
d'autres articles, et n'est pas à modifier pour autant) :

- `lf-2018` (partagée, `page: 4289-4290`) : articles 43 et 44 **p. 4281**. La p. 4280 du
  fascicule se termine sur l'article 42 (extraction de la seule p. 16 du PDF) ; le chapitre
  et l'ancienne note écrivent « p. 4280-4281 ».
- `lf-1996` (`page: 2371-2372`) : articles 36-37 p. 2371, 43-45 p. 2372, 46 p. 2373.
- La note de l'entrée proposée `loi-2016-78-lf-2017` de l'ancienne note (« passage des
  professions libérales de 6 % à 12 % ») est fausse : à taux inchangé, voir résultat 5.

**Créées dans `precis/{fr,ar}/fiscalite/references.json` le 24 septembre 2026** :

| Clé | JORT français | Pages vérifiées | Contrôle |
|---|---|---|---|
| `lf-2000` | n° 105 du 31/12/1999, tome 142 | loi p. 2739 ; art. 19 p. 2741 ; art. 73 p. 2751 | couche texte décodée ; URL FR et AR testées |
| `lf-2001` | n° 104 du 29/12/2000, tome 143 | loi p. 3171 ; art. 40 p. 3178 ; art. 63 p. 3181 ; art. 68 p. 3182 | couche texte décodée ; URL FR et AR testées |
| `decret-2002-3356-tva-telecom` | n° 106 du 31/12/2002, tome 145 | p. 3194 | couche texte décodée ; URL FR et AR testées |
| `lfc-2016` | n° 2 du 06/01/2017 | art. 3 p. 60 | couche texte saine |

Les trois paires d'URL de 1999, 2000 et 2002 sont celles des champs `pdf_fr` et `pdf_ar` de
`jort_cache.db` ; elles répondent en PDF. L'URL arabe de 2000 porte bien le nom exceptionnel
`Ja10400.pdf` (et non `Ja1042000.pdf`).

---

## 7. Notions pour le glossaire (`precis/glossaire.yml`)

Déjà présentes : `tva`, `assujetti`, `fait-generateur-tva`, `territorialite-tva`,
`exoneration-tva`, `tableau-a-tva`, `tableau-b-tva`, `tableau-b-bis-tva`, `tableau-c-tva`,
`taux-normal-tva`, `taux-reduit-tva`, `taux-majore-tva`, `livraison-a-soi-meme`,
`commercant-grossiste`, `chiffre-affaires-imposable`, `calendrier-application-tva`,
`droit-de-consommation`, `regime-forfaitaire`, `retenue-a-la-source`.

À vérifier ou ajouter :

| Terme FR | AR (à valider) | Source canonique |
|---|---|---|
| Taux intermédiaire (10 %, 12 %, 13 %) | النسبة الوسطى | LF 1995 art. 56 ; code, art. 7 n° 3 — le code ne le nomme pas : terme descriptif, à trancher |
| Taxe forfaitaire annuelle de TVA *(1990-1992)* | الأداء الجزافي السنوي | art. 16 nouveau (LF 1990 art. 24), abrogé par LF 1993 art. 105 |
| Droit forfaitaire simplifié *(1990-1992)* | المعلوم الجزافي المبسط | art. 17 I nouveau (LF 1990 art. 26) |
| Taxe forfaitaire mensuelle des transports | الأداء الجزافي الشهري على النقل | code, art. 17 II (LF 1998 art. 29) |
| Commerçant détaillant assujetti | تاجر التفصيل الخاضع | code, art. 1^er^ II-11 (LF 1996 art. 43) |
| Majoration de 25 % de l'assiette | الترفيع بـ 25 % في قاعدة الأداء | code, art. 6 I-10 (LF 1996 art. 44) |
| TVA sur la marge | الأداء على هامش الربح | code, art. 6 I-9 (LF 1991 art. 34 ; LF 2016 art. 33) |
| Régime suspensif | نظام توقيف العمل بالأداء | code, art. 11 |
| Crédit de TVA | فائض الأداء على القيمة المضافة | code, art. 15 |
| Promoteur immobilier | الباعث العقاري | code, art. 1^er^ II-5 bis ; art. 7 n° 3 (2018-2024) ; tableau B n° 31 |

Le terme arabe de la dernière colonne se vérifie sur le code consolidé arabe de 2025
(`PDFs/TVA/Code_de_la_Taxe_sur_la_Valeur_Ajoutée_2025.pdf`), non consulté ici.

---

## 8. Non établi

1. **Date d'effet des LF 1989 à 1993** : les dernières pages ont été lues à l'image. Les cinq lois
   sont muettes sur une date spéciale d'application et se terminent seulement par « La présente
   loi sera publiée au Journal officiel de la République tunisienne et exécutée comme loi de
   l'État ». Établir leur date d'effet exige donc la base factuelle nécessaire à l'application de
   la règle générale alors en vigueur ; aucune date n'est calculée ici.
2. **Grossistes en alimentation générale** : aucun texte ne les fait entrer dans le champ.
   Le code consolidé actuel ne mentionne plus leur exclusion (art. 1^er^ II-3, qui n'exclut que
   les médicaments depuis 2021) : l'exclusion ne vivait que dans le décret n° 89-1222.
3. **Décret n° 97-1339 du 14 juillet 1997** (date d'effet de l'art. 40 de la LF 1996) : toujours
   hors de `jort_cache` (ancienne note, § 5).
4. **Contenu des listes** : tableaux « L » (LF 1998), « M » (LF 1994), « M bis » (LF 1995),
   « P » (LF 1996), annexe 5 (LF 2016) non lus ; numéros abrogés du tableau A par la LF 2017
   (art. 16) non rapprochés de leur contenu.
5. **Retouches du taux de 13 % sans rapport avec les professions libérales** : l'art. 44 de la
   LF 2023 supprime le « 3^e^ tiret » ; le rapprochement tiret par tiret avec l'art. 7 de 2022
   a été fait sur la version DGELF 2023 (« supprimé par l'article 44 de la LF 2023 »), non sur la
   rédaction arabe en vigueur au 31/12/2022.
6. **LF 1989 (loi 88-145), art. 23 à 26** : OCR en colonnes entrelacées, contenu à relire à
   l'image avant toute publication.
7. **Pages arabes avant 2014** : non mesurées.
8. **Forfait des transporteurs (art. 17 II-1), 1988-1997** : différé par le décret n° 88-1109,
   il n'a de mise en application identifiée qu'avec sa réécriture par la LF 1998 (art. 29).
   Qu'il ait été perçu entre-temps n'est ni établi ni exclu.
9. **Décrets de l'article 8, 1988-1997** : 144 intitulés non triés ; certains réduisent le taux
    (ex. décret n° 89-224, voitures montées localement, taux non lu).

---

## 9. Recherches et contrôles

### 9.1 `r-tva-mise-en-application-post-1989` — fiche mise à jour

La fiche a été précisée sans être scindée. Son objet exclut désormais les articles 16 et 17, I,
dont le sort est établi : remplacement par la loi n° 89-115, art. 24 à 26, puis abrogation par la
loi n° 92-122, art. 105. Restent recherchés l'entrée dans le champ des grossistes en alimentation
générale et la mise en application du forfait des transporteurs de l'article 17, II-1, dans sa
rédaction de 1988.

`recherches.py` a été relancé depuis le 12 septembre 1989, puis élargi au plein texte par le terme
« alimentation générale ». La FTS de `jort_cache` ne donne comme candidat pertinent que le décret
n° 89-1222, point de départ de la recherche. Le plein texte donne trois homonymes sans rapport
(JORT n° 46/2014, 25/2017 et 113/2020). La couche texte est inexploitable pour l'essentiel des
fascicules scannés de 1989 à 1993 : la conclusion repose donc aussi sur la lecture ciblée des lois
de finances, non sur le silence du balayage. Une passe `aucun`, couverte jusqu'au 18 septembre
2026, est consignée dans `docs/recherches.yml`. Lacune maintenue : le corps des décrets relatifs à
la TVA publiés de 1989 à 1996 n'a pas été dépouillé systématiquement.

### 9.2 LF 1989 à 1993 — absence de clause spéciale vérifiée

La proposition de fiche `r-lf-1989-1993-clause-effet` n'est pas créée : les sources primaires ont
été retrouvées et lues, de sorte qu'il ne subsiste pas de texte attendu à rechercher. Les cinq
lois passent directement du dernier article à la formule de publication et d'exécution :

| Loi | Dernier article | Page FR | Formule finale |
|---|---:|---:|---|
| n° 88-145, LF 1989 | 125 | 1805 | publication au JORT et exécution comme loi de l'État |
| n° 89-115, LF 1990 | 73 | 2155 | idem |
| n° 90-111, LF 1991 | 97 | 2061 | idem |
| n° 91-98, LF 1992 | 102 | 2093 | idem |
| n° 92-122, LF 1993 | 123 | 1679 | idem |

Cette lecture établit l'absence de clause spéciale ; elle n'établit pas, à elle seule, la date
d'effet résultant de la règle générale alors applicable.

### 9.3 LF 1996 — article 68 retrouvé

La proposition de fiche `r-lf-1996-clause-effet` n'est pas créée : le fascicule français local
`PDFs/JORT/1995/fr/Jo10495.pdf` est complet. À la page 2375, sous le titre « Fixation de la date
d'application de la loi de finances pour la gestion 1996 », l'article 68 dispose : « Sans préjudice
des dispositions spéciales prévues par les articles précédents, les dispositions de la présente
loi sont applicables à compter du 1^er^ janvier 1996. » La page a été lue à l'image ; l'édition
arabe n'est pas nécessaire pour combler cette lacune.

La loi n° 2000-98 (LF 2001) reste hors de cette recherche : son article 68, lu page 3182 du
fascicule français décodé `Jo1042000.pdf`, fixe l'application au 1^er^ janvier 2001.

---

## Annexe — Requêtes et fichiers de travail

- Inventaire : `jort_cache.textes` filtré sur `type like 'Loi%' or type = 'Decret-Loi'` et
  « valeur ajoutee » / « القيمة المضافة » dans `titre||objet` (205 notices, 1988-2025), complété
  par un balayage plein texte des LF (« valeur ajout », « T.V.A ») article par article, et par les
  chaînes d'annotation du code consolidé DGELF 2023 (art. 1, 2, 7, 16-17).
- Décrets avant 1998 : même filtre sur `type like 'Dec%'`, signatures 1988-1997 (144 notices,
  intitulés non triés un à un).
- LF 2026 (loi n° 2025-17) : numéro établi par la notice `jort_cache` (`numero` souvent NULL
  pour cette loi) et l'en-tête du fascicule arabe.
