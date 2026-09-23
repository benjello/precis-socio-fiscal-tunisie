# Les autres régimes de pension de la CNSS : origines, état initial, réformes du cœur du régime

> Note **documentaire**, rédigée le 23 septembre 2026 sur la branche
> `feat/retraites-cnss-autres-regimes`. Elle n'écrit pas de prose de précis. Elle n'a modifié aucun
> `.qmd`, aucun `references.json` ni aucun paramètre.
>
> Objet : préparer la réorganisation, sur le modèle de la partie RSNA, des sections de
> `precis/fr/retraites/_secteur_prive.qmd` consacrées aux autres régimes de pension de la CNSS :
> salariés agricoles (RSA, RSAA), régime complémentaire, non-salariés (RTNS), Tunisiens à l'étranger
> (RTTE), artistes (RACI), travailleurs à faibles revenus (RTFR), et les régimes que le chapitre omet.
> Elle reprend la forme de `rsna-histoire-reformes.md`.
>
> **Elle relève dix erreurs ou états périmés dans le chapitre actuel (§ 13), et trois régimes de
> pension de la CNSS qu'il omet (§ 2).**

## Conventions

**Trois niveaux d'attestation** : **[T]** texte lu au fascicule (à l'image, ou couche texte relue ;
« OCR » signale une lecture par océrisation dont seuls les chiffres cités ont été relus à l'image) ;
**[M]** métadonnées `jort_cache.db` seules ; **[D]** dérivé d'un rapprochement ou d'une convention.

**Dates d'entrée en vigueur** (AGENTS.md). Date d'effet énoncée par le texte : reprise telle quelle.
Sans clause d'effet :
- avant 1993, **un jour franc après la publication** (décret du 27 janvier 1883, art. 3 nouveau,
  rédaction du décret du 13 septembre 1956) ;
- depuis 1993, **cinq jours après le dépôt** du JORT au siège du gouvernorat de Tunis, jour du dépôt
  non compté (loi n° 93-64, art. 2). Le décompte suit celui des paramètres déjà sourcés (dépôt J →
  exécutoire J + 5 : 14 avril 2009 → 19 avril 2009). **Chaque date de dépôt citée ici est lue dans la
  mention imprimée en dernière page du fascicule** (« Ce numéro … a été déposé au siège du
  gouvernorat de Tunis le … »).

**URL** : `https://www.pist.tn/jort/<aaaa>/<aaaa>{F|A}/{Jo|Ja}<nnn><aa|aaaa>.pdf`. Toutes les URL de
cette note ont été contrôlées le 23 septembre 2026 avec `curl -k` (`200 application/pdf`, taille
plausible), sauf mention contraire.

**Lecture.** Les fascicules 1977-1993 n'ont pas de couche texte : rendus à 200 dpi, océrisés
(`tesseract -l fra`) pour le repérage, chiffres relus à l'image sur des découpes. Les fascicules
2002-2003 (n° 22, 35, 106/2002 ; n° 34/2003) ont la police décalée de 29, décodée selon
outillage-sources § 5. Images de travail : `scratchpad/autres/`, hors dépôt. Aucun processus d'OCR
ne tourne à la fin de la tâche.

---

## 0. Résumé

| Régime | Texte fondateur | Effet | Cœur du régime modifié depuis ? | Dernier modificatif (seconde voie : visas) |
|---|---|---|---|---|
| RSA (salariés agricoles) | loi n° 81-6 | 1er janv. 1981 (art. 88) | **non** (âge, stage, taux, SMAG × 300 j × coefficient inchangés) ; droits dérivés modifiés 1996, 1997, 2007 | loi n° 2007-43 (visas de 2020 et du 5 août 2026, éd. ar.) |
| RSAA (agricole amélioré) | loi n° 89-73 (titre III de la loi n° 81-6) | 1er oct. 1989 (art. 4) | **non** | idem |
| Régime complémentaire | arrêté du 18 nov. 1978 | 1er janv. 1974 (art. 2) | **non** sur la formule ; survivants modifiés en 1997 | arrêté du 27 janv. 1997 (seul modificatif au JORT) |
| Non-salariés | **décrets n° 82-1359 et 82-1360** | **1er juillet 1982** | **oui** : 1989 (non agricole : classes en multiples du SMIG ; revalorisation par arrêté) ; 1995 (fusion ; non agricole : minimum 1/2 → 30 % SMIG ; **agricole : taux 40 → 30 %, minimum créé, départ dès 60 ans avec décote, classes**) ; 2002 (revalorisation automatique) | décret n° 2008-172 (visas 2020, 2025, 2026) |
| RTTE | décret n° 89-107 | 19 janv. 1989 [D] | **non** | décret n° 91-604 (visas 2020) |
| RACI | loi n° 2002-104 ; décret n° 2003-894 | 5 janv. 2003 [D] | **non** (seul l'orphelin, 2007) | loi n° 2007-43 |
| RTFR | loi n° 2002-32 ; **décret n° 2002-916** | 21 mars 2002 [D] | **non** sur la formule ; champ étendu en **2019** (décret gouvernemental n° 2019-379) | loi n° 2007-43 ; décret n° 2019-379 (visas 2020, 2025, 2026) |
| **Pêcheurs** | **décret n° 77-546** | 23 juin 1977 [D] | extension du régime de 1974, assiette forfaitaire | décret n° 82-1028 (visas 2020) |
| **Travailleuses agricoles** | **décret-loi n° 2024-4** | 28 oct. 2024 [D] | textes d'application non publiés (pas de taux) | — |

Aucun texte modifiant l'âge, le stage ou le taux de l'un de ces régimes n'a été trouvé au JORT
jusqu'au n° 93 du 18 septembre 2026 (§ 12).

---

## 1. Les textes lus

| Texte | Objet | JORT (éd. fr.) | Pages | Dépôt / publication | Effet | Niv. |
|---|---|---|---|---|---|---|
| Décret n° 77-546 du 15 juin 1977 | sécurité sociale des pêcheurs | n° 43, 21 juin 1977 | 1655-1657 | publ. 21 juin 1977 | sans clause : **23 juin 1977** [D] | **[T]** (art. 1-12 à l'image) |
| Décret n° 80-103 du 23 janv. 1980 | ajoute l'art. 11 bis au décret n° 77-546 | n° 6/1980 | 252 | publ. 29 janv. 1980 [M] | sans clause | **[T]** OCR ; un chiffre illisible (§ 11) |
| Loi n° 81-6 du 12 févr. 1981 | régimes de sécurité sociale du secteur agricole | n° 9, 13 févr. 1981 | 265-273 (art. 45-88 : 270-273) | — | **art. 88 : 1er janv. 1981** | **[T]** art. 45-88 OCR, chiffres relus à l'image ; art. 53 al. 2 confirmé sur l'éd. ar. (80 %) |
| Rectificatif à la loi n° 81-6 | — | n° 26, 17 avril 1981 | **844** | — | — | **[T]** intégral à l'image |
| Décret n° 82-1028 du 8 juil. 1982 | art. 3 bis du décret n° 77-546 | n° 50, 13-16 juil. 1982 ; rectificatif n° 66/1982, p. 2197 | 1579 | — | transitoire 2 ans (rectificatif) | **[T]** OCR |
| **Décret n° 82-1359 du 21 oct. 1982** | extension aux travailleurs indépendants non agricoles | n° 66, 19-22 oct. 1982 | 2192-2195 | — | **art. 26 : 1er juillet 1982** | **[T]** art. 1-26 ; art. 7, 8, 18-24 à l'image |
| **Décret n° 82-1360 du 21 oct. 1982** | exploitants et travailleurs indépendants agricoles | même fascicule | 2195-2197 | — | **art. 18 : 1er juillet 1982** | **[T]** art. 1-18 ; art. 5, 8 à l'image |
| Loi n° 89-73 du 2 sept. 1989 | titre III de la loi n° 81-6 (RSAA) | n° 60, 5-8 sept. 1989 | 1338-1339 | — | **art. 4 : 1er oct. 1989** | **[T]** OCR, art. 93-97 relus à l'image |
| Décret n° 89-107 du 10 janv. 1989 | RTTE | n° 4, 17 janv. 1989 | 98-99 | publ. 17 janv. 1989 | sans clause : **19 janv. 1989** [D] | **[T]** OCR intégral |
| **Décret n° 89-1611 du 10 oct. 1989** | modifie le décret n° 82-1359 | n° 70, 20 oct. 1989 | 1653-1654 | publ. 20 oct. 1989 | sans clause : **22 oct. 1989** [D], corroboré par le décret n° 93-357 | **[T]** ; barème des classes à l'image |
| Décret n° 90-548 du 27 mars 1990 | assiette des pêcheurs indépendants (RSAA) | n° 24, 6 avril 1990 | 490-491 | — | — | **[T]** OCR |
| Décret n° 91-604 du 30 avril 1991 | proroge l'art. 24 du décret n° 89-107 | n° 32/1991 | 1008 | — | — | **[T]** OCR |
| Décret n° 93-357 du 8 févr. 1993 | proroge l'art. 24 du décret n° 82-1359 | n° 14, 19 févr. 1993 | 273 | — | prorogation « à compter du 22 octobre 1992 » | **[T]** OCR |
| Décret n° 95-1166 du 3 juil. 1995 | RTNS | n° 55, 11 juil. 1995 | 1486-1489 | **dépôt 14 juil. 1995** | **19 juil. 1995** [D] | **[T]** couche texte |
| Loi n° 95-102 du 27 nov. 1995 | art. 74 al. 1 de la loi n° 81-6 | n° 96, 1er déc. 1995 | 2224 | **dépôt 5 déc. 1995** | **10 déc. 1995** [D] | **[T]** |
| Loi n° 96-66 du 22 juil. 1996 | art. 60, 61, 63, 69 de la loi n° 81-6 | n° 60, 26 juil. 1996 | 1603 | **dépôt 30 juil. 1996** | **4 août 1996** [D] | **[T]** |
| Arrêté du 27 janv. 1997 | art. 21, 22, 24, 30 du règlement complémentaire | n° 11, 7 févr. 1997 | 183-184 | **dépôt 11 févr. 1997** | **16 févr. 1997** [D] | **[T]** |
| Loi n° 97-61 du 28 juil. 1997 | art. 41 al. 3 et 64 de la loi n° 81-6 | n° 61, 1er août 1997 | 1360 | — | **art. 2 : 1er mai 1997** | **[T]** |
| Arrêté du 29 juil. 1998 | revalorisation des pensions RTNS | n° 63, 7 août 1998 | 1719-1720 | dépôt 10 août 1998 | **art. 3 : 1er mai 1998** | **[T]** couche texte |
| Loi n° 2002-32 du 12 mars 2002 | RTFR | n° 22, 15 mars 2002 | 603-606 | **dépôt 16 mars 2002** | **21 mars 2002** [D] | **[T]** décodé |
| **Décret n° 2002-916 du 22 avril 2002** | application de la loi n° 2002-32 | n° 35, 30 avril 2002 | 1058-1061 | **dépôt 2 mai 2002** | **7 mai 2002** [D] | **[T]** décodé |
| Loi n° 2002-104 du 30 déc. 2002 | RACI | n° 106, 31 déc. 2002 | 3187-3190 | **dépôt 31 déc. 2002** | **5 janv. 2003** [D] | **[T]** décodé ; art. 20 lu sur l'éd. ar. à l'image |
| Décret n° 2003-894 du 21 avril 2003 | application de la loi n° 2002-104 | n° 34, 29 avril 2003 | 1291-1294 | **dépôt 30 avril 2003** | **5 mai 2003** [D] | **[T]** décodé |
| Loi n° 2007-43 du 25 juin 2007 | titre II : art. 64 (81-6), 25 (2002-32), 22 (2002-104) | n° 51, 26 juin 2007 | 2198-2199 | **dépôt 27 juin 2007** | **2 juillet 2007** [D] | **[T]** couche texte |
| **Décret gouvernemental n° 2019-379 du 22 avril 2019** | étend la loi n° 2002-32 | n° 34, 26 avril 2019 | 1277-1278 | **dépôt 29 avril 2019** | **4 mai 2019** [D] | **[T]** couche texte |
| Arrêté du 19 juin 2019 | pièces d'affiliation des récoltantes de coquillages et saisonniers ruraux | n° 52/2019 (éd. ar. seule) | 2109-2110 | — | — | **[M]** |
| Décret-loi n° 2020-33 du 10 juin 2020 | auto-entrepreneur (المبادر الذاتي) | n° 54/2020 (éd. ar. seule) | 1417-1420 | dépôt 10 juin 2020 | — | **[T]** art. 7 (éd. ar.) |
| Arrêté conjoint du 10 juil. 2020 | prime aux pensionnés CNSS et CNRPS | n° 67, 14 juil. 2020 | 1515-1516 | — | — | **[T]** visas (seconde voie) |
| Loi n° 2021-37 du 16 juil. 2021 | travail domestique | n° 68, 30 juil. 2021 | 2006-2010 | dépôt 30 juil. 2021 | **art. 29 : six mois après la publication** | **[T]** art. 4, 29 |
| **Décret-loi n° 2024-4 du 22 oct. 2024** | protection sociale des travailleuses agricoles | n° 129, 23 oct. 2024 | 2897-2901 | **dépôt 23 oct. 2024** | **28 oct. 2024** [D] | **[T]** intégral (couche texte) |
| Arrêté conjoint du 5 août 2026 | allocation monétaire des catégories pauvres | n° 80, 7 août 2026 | 1610-1611 | — | — | **[T]** visas (seconde voie), éd. fr. et ar. |
| Règlement annexé à l'arrêté du 18 nov. 1978 | régime complémentaire | n° 79, 24 nov. 1978 | 3374-3379 | — | art. 2 : 1er janv. 1974 | **[T]** OCR (numérotation et taux des art. 6, 10, 21-31) |

URL (préfixe `https://www.pist.tn/jort/`), toutes vérifiées :

| Texte | Français | Arabe |
|---|---|---|
| Décret n° 77-546 | `1977/1977F/Jo04377.pdf` | `1977/1977A/Ja04377.pdf` |
| Décret n° 80-103 | `1980/1980F/Jo00680.pdf` | `1980/1980A/Ja00680.pdf` |
| Rectificatif à la loi n° 81-6 | `1981/1981F/Jo02681.pdf` | `1981/1981A/Ja02681.pdf` |
| Décret n° 82-1028 | `1982/1982F/Jo05082.pdf` | `1982/1982A/Ja05082.pdf` |
| Décrets n° 82-1359 et 82-1360 | `1982/1982F/Jo06682.pdf` | `1982/1982A/Ja06682.pdf` |
| Décret n° 89-1611 | `1989/1989F/Jo07089.pdf` | `1989/1989A/Ja07089.pdf` |
| Décret n° 90-548 | `1990/1990F/Jo02490.pdf` | `1990/1990A/Ja02490.pdf` |
| Décret n° 91-604 | `1991/1991F/Jo03291.pdf` | `1991/1991A/Ja03291.pdf` |
| Décret n° 93-357 | `1993/1993F/Jo01493.pdf` | `1993/1993A/Ja01493.pdf` |
| Loi n° 95-102 | `1995/1995F/Jo09695.pdf` | `1995/1995A/Ja09695.pdf` |
| Loi n° 96-66 | `1996/1996F/Jo06096.pdf` | `1996/1996A/Ja06096.pdf` |
| Arrêté du 27 janv. 1997 | `1997/1997F/Jo01197.pdf` | `1997/1997A/Ja01197.pdf` |
| Loi n° 97-61 | `1997/1997F/Jo06197.pdf` | `1997/1997A/Ja06197.pdf` |
| Décret n° 2002-916 | `2002/2002F/Jo0352002.pdf` | `2002/2002A/Ja0352002.pdf` |
| Décret gouvernemental n° 2019-379 | `2019/2019F/Jo0342019.pdf` | `2019/2019A/Ja0342019.pdf` |
| Arrêté du 19 juin 2019 | **absente** (404 ; `pdf_fr` vide dans `jort_cache`) | `2019/2019A/Ja0522019.pdf` |
| Décret-loi n° 2020-33 | **absente** (404 ; `pdf_fr` vide dans `jort_cache`) | `2020/2020A/Ja0542020.pdf` |
| Arrêté conjoint du 10 juil. 2020 | `2020/2020F/Jo0672020.pdf` | `2020/2020A/Ja0672020.pdf` |
| Loi n° 2021-37 | `2021/2021F/Jo0682021.pdf` | `2021/2021A/Ja0682021.pdf` |
| Décret-loi n° 2024-4 | `2024/2024F/Jo1292024.pdf` | `2024/2024A/Ja1292024.pdf` |

Les URL des textes déjà en bibliographie (81-6, 89-73, 89-107, 95-1166, 2002-32, 2002-104,
2003-894, 2007-43, arrêté de 1978, arrêté de 1998) sont celles des entrées existantes.

---

## 2. Les régimes que le chapitre omet

### 2.1 Les régimes des travailleurs indépendants de 1982 — le RTNS n'est pas né en 1995

Le chapitre écrit que le RTNS « est institué par le décret n° 95-1166 ». Les non-salariés sont
couverts depuis le **1er juillet 1982** par deux décrets du 21 octobre 1982, que le décret de 1995
**fusionne et abroge** (art. 34, 35, 39) en transférant leurs réserves et en conservant leurs
affiliés. Le décret n° 94-1477 (art. 3) les nomme parmi les régimes gérés par la CNSS. Détail au § 6.

### 2.2 Les pêcheurs : décret n° 77-546

**Art. 1 [T]** : « L'ensemble des régimes de Sécurité Sociale découlant des lois […] N° 60-30 et
60-33 du 14 décembre 1960, et du décret […] N° 74-499 du 27 avril 1974, est étendu aux pêcheurs, aux
patrons pêcheurs même propriétaires de leur barque ainsi qu'aux armateurs travaillant sur un bateau
de pêche dont ils assurent l'équipement […]. Sont pareillement couverts les petits armateurs visés à
l'article 65 du même code. » C'est une **extension du régime de 1974**, sans règle de pension propre
(ni âge, ni taux, ni minimum distincts). Sa particularité est l'assiette (§ 11). Le texte est encore
visé en 2020 parmi les régimes de pension de la CNSS (§ 12) ; depuis 1989, une partie de son champ
est passée au RSAA (loi n° 89-73, art. 3), et depuis 2002 une autre au RTFR (loi n° 2002-32, art. 1 c).

### 2.3 Les travailleuses agricoles : décret-loi n° 2024-4

**Un régime de pension de la CNSS institué en 2024**, que le chapitre ne mentionne pas. Détail au § 10.

### 2.4 Rattachements et extensions, non des régimes nouveaux

- **Récoltantes de coquillages et ouvriers saisonniers et mobiles ruraux** : entrés dans le RTFR en
  2019 par le décret gouvernemental n° 2019-379 (§ 9.4).
- **Auto-entrepreneur** (décret-loi n° 2020-33, art. 7, éd. ar. **[T]**) : la « contribution unique »
  comprend 7,5 % calculés sur les deux tiers du SMAG ou du SMIG, et « تنطبق أحكام العنوان الثاني من
  القانون عدد 32 لسنة 2002 […] على نظام المبادر الذاتي » (les dispositions du titre II de la loi
  n° 2002-32 — les prestations — s'appliquent). L'auto-entrepreneur peut en outre adhérer au régime
  des non-salariés (11 % du SMAG ou du SMIG, 4 % pour les retraités), une classe supérieure restant
  possible. **Il n'y a donc pas de régime de pension de l'auto-entrepreneur : ses droits sont ceux du
  RTFR, et optionnellement du RTNS.**
- **Employés de maison** : la loi n° 2021-37, art. 4 **[T]**, confirme qu'ils « demeurent régis par
  les dispositions de la loi n° 2002-32 ».

### 2.5 Une ligne statistique sans texte identifié : les « travailleurs de chantiers »

Les séries de la CNSS publient une ligne « travailleurs de chantiers (convention) » : 10,6 millions
de dinars de pensions en 2016, 9,8 en 2020 (tunisia-data, `cnss_pensions_par_regime.csv`) ;
l'annuaire 2013 en donne l'évolution **dans la partie du RTFR** (p. 266 imprimée : « Evolution de
l'effectif des pensionnés et des montants des pensions servies par nature (travailleurs de
chantiers) », sigle RTC). **Aucun texte du JORT n'a été rattaché à cette ligne** (FTS
`chantiers AND (securite OR pension …)` : seuls les décrets de 1954-1960 sur les chômeurs des
chantiers). Hypothèses non vérifiées : régime conventionnel géré par la CNSS au titre du décret
n° 94-1477, art. 4, ou catégorie b) de la loi n° 2002-32. **TODO** (§ 17).

---

## 3. Le régime des salariés agricoles (RSA)

### 3.1 Origine

Loi n° 81-6 du 12 février 1981, JORT n° 9 du 13 février 1981, p. 265-273. **Art. 88 [T]** : « La
présente loi entrera en vigueur le 1er janvier 1981. » (art. 104 depuis la loi n° 89-73, art. 2).
**Art. 87 [T]** : elle abroge « les dispositions du titre I bis de la loi n° 60-30 », c'est-à-dire le
cadre agricole antérieur logé dans la loi de 1960 (sa teneur n'a pas été lue ici ; rien n'indique
qu'il comportait des pensions : **TODO**). **Art. 85 [T]** : coordination avec le régime de 1974 —
les conditions d'âge et de stage « sont supposées remplies si elles le sont dans l'ensemble des deux
régimes », chaque régime payant au prorata des périodes qu'il retient, sur une pension théorique
calculée selon ses propres règles.

### 3.2 Le régime à son entrée en vigueur, d'un seul tenant (art. 45-84) [T]

| Élément | Règle de 1981 | Article |
|---|---|---|
| Périodes assimilées | incapacité temporaire AT ; rente AT ≥ 66,66 % ; indemnités de maladie, longue maladie, maternité ; invalidité (sous réserve de l'art. 52, rectificatif) — accomplies depuis l'entrée en vigueur de la loi | 45 |
| Âge et stage | **60 ans** ; **40 trimestres** effectifs ou assimilés ; pas d'activité assujettie | 48 |
| Rupture du contrat | le droit « oblige à mettre fin aux relations de travail », sauf accord homologué | 47 |
| Taux | **40 %** à 40 trimestres + **0,5 % par trimestre**, plafond **80 %** | 49 |
| Salaire de référence | « salaire minimum agricole garanti rapporté à une durée de travail de 300 jours par an affecté du **coefficient multiplicateur moyen** ayant servi de base au calcul des cotisations au cours des trois ou cinq dernières années précédent l'âge d'ouverture du droit », la plus avantageuse | 50 |
| Invalidité | 2/3 ; stage de **20 trimestres dont 2 au cours des 12 mois** précédents ; **40 %** + 0,5 %/trimestre au-delà de 40 trimestres, plafond **80 %** (chiffre confirmé sur l'éd. ar., « حدا اقصاه 80 بالمائة ») ; tierce personne + 20 % | 51-54 |
| Contrôle, cumul AT | contrôle annuel, pas de révision après 55 ans ; réduction de moitié de la rente | 56, 59 |
| Réversion | « **la veuve** » d'un pensionné ou d'un assuré remplissant le stage, et « le veuf invalide » ; mariage « antérieurement à l'ouverture de droit à pension » ; **50 %**, partagé entre veuves ; **suppression au remariage** | 60-63 |
| Orphelins | orphelin **mineur** : 16 ans ; 21 ans en études ; sans limite si infirme ; **20 %**, **30 %** de père et de mère ; collectives | 64-68 |
| Plafond | « pension de référence du mari » | 69 |
| Carrière courte | **allocation en capital** dès **20 trimestres** : une mensualité de la pension théorique par période de deux trimestres ; prescription d'un an | 70-73 |
| Liquidation | demande dans **un an** ; jouissance au mois qui suit la cessation d'activité ; résidence | 74-77 |
| Cumul invalidité / survivant | **interdit** | 79 |
| **Revalorisation** | « révisées lors de chaque paiement proportionnellement à la variation du SMAG par rapport à celui qui a servi au calcul du salaire de référence » | 80 |
| Transitoire | **art. 81** : validation forfaitaire d'un trimestre par année entre 40 ans et l'âge de départ, dans la limite de 18 trimestres ; **pendant la période transitoire, si le total ne dépasse pas 40 trimestres, pension au prorata** ; **art. 82** : allocation dès 10 trimestres pour une moyenne de 1 à 2 trimestres par an | 81-82 |

Aucun âge anticipé, aucune pension minimale : exact (§ 13).

### 3.3 Le rectificatif (JORT n° 26 du 17 avril 1981, p. 844) — lu en entier à l'image

Il porte sur neuf points : art. 1er al. 3 (« l'octroi de prestations de sécurité sociale à d'autres
catégories ») ; art. 11 dernier al. ; art. 39-4 (allocation au décès d'un enfant de 2 à 6 ans : 40 → 30) ; art. 43 (dernier alinéa rétabli, carnet de soins) ; **art. 45 d)** (renvoi à l'art. **52**
au lieu de 51) ; art. 57 (renvoi à l'art. 25 au lieu de 2) ; **art. 74 al. 1 et 2, 75 al. 1, 76
al. 1** (les mots « ou d'allocation » / « et allocations » sont supprimés). **Il ne touche ni
l'art. 48, ni 49, ni 50, ni 53, ni 60-73, ni 80-82, ni 88.** Le callout « Un rectificatif reste à
confronter » peut être levé : les chiffres et la date d'effet que le chapitre tire de la loi sont
inchangés.

### 3.4 Réformes : recensement exhaustif

Modificatifs de la loi n° 81-6 (FTS sur `titre`/`objet` + LIKE ; seconde voie : visas, § 12) :

| Texte | Effet | Article | Avant → après | Cœur ? |
|---|---|---|---|---|
| Rectificatif | 1er janv. 1981 | 45 d), 74-76… | § 3.3 | non |
| Loi n° 89-73 | 1er oct. 1989 | ajoute le titre III (art. 86-101), renumérote 86-88 en 102-104 | § 4 | nouveau régime |
| Loi n° 95-102 | 10 déc. 1995 [D] | 74 al. 1 | délai de demande **1 an → 5 ans** | non (procédure) |
| **Loi n° 96-66** | **4 août 1996** [D] | **60, 61, 63, 69** | **veuve / veuf invalide → « conjoint survivant »** ; mariage antérieur à l'ouverture du droit → « liens de mariage existant au moment du décès » ; **suppression au remariage → suspension seulement si remariage avant 55 ans, rétablissement revalorisé au décès du nouveau conjoint ou à la dissolution, cumul de pensions de conjoint interdit (la plus élevée)** ; plafond « pension de référence du mari » → « pension dont bénéficiait ou aurait pu bénéficier le défunt » | non (droits dérivés) |
| **Loi n° 97-61** | **1er mai 1997** (art. 2) | 41 al. 3 (soins) ; **64** | orphelin : 16 / 21 / sans limite → **16 ans ; 21 ans en secondaire, technique ou professionnel ; 25 ans en supérieur sans bourse ; « d) à la fille tant qu'elle ne dispose pas des ressources ou que l'obligation alimentaire n'incombe pas à son époux » ; e) sans limite si infirme** | non |
| Loi n° 2007-43 | 2 juil. 2007 [D] | 64 d) ; 64 al. 1 | d) remplacé : fille sans limite d'âge, conditions appréciées au décès, paiement **définitivement suspendu** si une condition fait défaut ; suppression de « mineur » ; art. 5 : pas de reprise des pensions interrompues | non |

**Aucune réforme du cœur du régime** : âge 60, stage 40 trimestres, 40 % + 0,5 %, plafond 80 %,
SMAG × 300 j × coefficient moyen sur 3 ou 5 ans, revalorisation proportionnelle au SMAG, absence de
minimum et d'anticipé. La **revalorisation** a été réaffirmée par le décret n° 2026-66, art. 5
(clé `decret2026-66`, déjà versée).

---

## 4. Le régime agricole amélioré (RSAA)

Loi n° 89-73, JORT n° 60 des 5-8 septembre 1989, p. 1338-1339. **Art. 4 [T]** : entrée en vigueur au
**1er octobre 1989**. Les affirmations du tableau `tbl-rsa-rsaa` sont **confirmées** à l'image :
art. 86 (champ ; extension possible par décret), 93 (trimestres avec un salaire déclaré d'au moins
**50 fois le SMAG**), 95 (salaires des **3 ou 5 années** précédant l'année d'ouverture ; limite de
**6 × SMAG × 300 jours**), 96 (minimum **1/2 SMAG × 300 jours**), 97 (majoration égale à la hausse du
SMAG journalier × 25 jours, affectée du taux de la pension ; alinéa 4 pour veuves et orphelins),
98 (non-cumul avec l'art. 96), 99 (validation depuis le 1er janvier 1981), 101 (renvoi aux titres I
et II).

Deux compléments au chapitre :
- **Art. 3 de la loi n° 89-73 [T]** : abroge le décret n° 77-546 pour les pêcheurs visés à
  l'art. 86 al. 3 (bateaux de moins de 30 tonneaux, pêcheurs indépendants, petits armateurs), qui
  passent au RSAA.
- **Décret n° 90-548 [T]** (OCR) : pour les pêcheurs indépendants et petits armateurs, l'assiette de
  l'art. 89 est le **SMAG × 75 jours par trimestre** ; le taux de 15 % se répartit en **7,5 %**
  pensions, 4,5 % allocations familiales, 3 % assurances sociales. Leur pension repose donc sur un
  salaire forfaitaire. (Relève aussi du livre « Cotisations sociales », qui cherchait ce décret de
  répartition : **il existe**, au moins pour ces catégories.)

**Réformes** : aucun modificatif du titre III n'a été trouvé ; les visas de 2020 et 2026 citent la loi
n° 81-6 « modifiée en dernier lieu par la loi n° 2007-43 ». La loi n° 96-66 et la loi n° 97-61
réécrivent les art. 60-69, applicables au RSAA par le renvoi de l'art. 101. **Pas de réforme du
cœur.**

---

## 5. Le régime complémentaire

Arrêté du 18 novembre 1978, JORT n° 79 du 24 novembre 1978, p. 3374-3379 (clé existante).
Numérotation du règlement contrôlée à l'OCR : art. 6 (taux d'appel **4,5 %** du salaire
différentiel), 10 (points ; cotisation contractuelle de **18 %**), 11 (salaire de référence), 14
(cotisation minimum), 15-17, 18 (« valeur du point de retraite »), 20, **21 « Pension des veuves et
des veufs », 22 « Condition d'attribution », 23 « Taux » (50 %), 24 « Suppression de la pension » (le
remariage de la veuve entraîne suppression)**, 25-27 (orphelins 20 / 30 %), 30 (cumul), 31
(versement unique), 34 (suspension, 80 %). Les renvois du chapitre sont exacts pour 1978.

**Seul modificatif trouvé : arrêté du 27 janvier 1997** (JORT n° 11 du 7 février 1997, p. 183-184)
**[T]**. « Article unique. — Les articles 21, 22, 24 et 30 de l'arrêté du 18 novembre 1978 susvisé
sont abrogés et remplacés » :
- art. 21 : « Le conjoint survivant » d'un pensionné ou d'un participant remplissant le stage ;
- art. 22 : pension due « lorsque les liens de mariage existent au moment du décès » ;
- art. 24 : **suspension si remariage avant 55 ans**, rétablissement revalorisé, cumul de pensions de
  conjoint interdit (la plus élevée) ;
- art. 30 : plafond = pension dont bénéficiait ou aurait pu bénéficier le défunt.

Effet : sans clause ; dépôt le 11 février 1997, exécutoire le **16 février 1997** [D]. C'est
l'alignement sur le RSNA (décret n° 90-1455, art. 32 ; décret n° 97-291) et sur le RSA (loi
n° 96-66). **Aucune réforme de la formule (points, valeur du point) n'est au JORT** ; ces décisions
relèvent du directeur général de la CAVIS puis de la CNSS (règlement, art. 11 et 18), non publiées.

---

## 6. Les travailleurs non salariés : de 1982 à 1995

### 6.1 Les deux régimes de 1982 [T]

**Décret n° 82-1359** (non agricole), JORT n° 66 des 19-22 octobre 1982, p. 2192-2195 :

| Élément | Règle | Art. |
|---|---|---|
| Champ | artisans, commerçants, industriels, médecins et pharmaciens non affiliés, et toute catégorie qui demande une adhésion collective ; extension des art. 68-96, 100-120 de la loi n° 60-30 et **20-38, 46-52, 54 et 57 du décret n° 74-499** | 1-2 |
| Gestion | CNSS ; pensions déléguées à la CAVIS | 3 |
| Assiette | **six classes de revenu forfaitaire en dinars** : 660, 2 000, 4 000, 6 000, 8 500, 15 000 D ; « révisé en cas de hausse sensible du niveau de vie » | 7 |
| Cotisation | **10,65 %**, dont **5,25 %** pensions et 5,40 % assurances sociales | 8 |
| Âge | **65 ans** ; dès **60 ans**, pension « réduite de 0,5 % par trimestre restant à courir » jusqu'à 65 ans | 18 |
| Revenu de référence | « moyenne pondérée des revenus forfaitaires auxquels l'assuré a cotisé au cours de l'ensemble de sa carrière » | 19 |
| Taux | **30 %** à **120 mois** (stage de l'art. 15 b du décret de 1974) + **0,5 % par période de 3 mois**, plafond **80 %** | 20 |
| Invalidité | 30 % à 60 mois ; même majoration au-delà de 120 mois ; 80 % | 21 |
| **Minimum** | **1/2 du SMIG × 2 400 heures** | 22 |
| Revalorisation | « révisé en cas de hausse sensible du niveau de vie », par décret | 23 |
| Transitoire | validation forfaitaire d'un trimestre par an entre 45 ans et l'âge (max. 18) ; pension au prorata si total ≤ 40 trimestres, sans minimum | 24 |
| Conventionnels | transférés à la CAVIS | 25 |
| **Effet** | « prend effet à compter du 1er juillet 1982 » (rétroactif) | 26 |

**Décret n° 82-1360** (agricole), même fascicule, p. 2195-2197 : extension de la loi n° 81-6 « aux
travailleurs indépendants, métayers et tous exploitants » (art. 1) ; cotisation trimestrielle de
**6,45 %** d'un forfait SMAG × **45 jours par trimestre**, coefficient 1, 1,5 ou 2 au choix, dont
**5,25 %** pensions (art. 5) ; **âge 65 ans** ; salaire de référence SMAG × 300 jours × **moyenne des
coefficients de toute la carrière** (art. 8) ; réserve initiale de 35 millions de dinars (art. 12) ;
transitoire identique (art. 16) ; allocation de vieillesse dès 10 trimestres (art. 17) ; **effet au
1er juillet 1982** (art. 18). Les autres règles (taux 40 % + 0,5 %, plafond 80 %, pas de minimum,
revalorisation sur le SMAG) sont celles de la loi n° 81-6 par l'art. 7 **[D]**.

### 6.2 Les modificatifs de 1989 et 1993 [T]

**Décret n° 89-1611** (JORT n° 70 du 20 octobre 1989, p. 1653-1654), qui réécrit les art. 1, 4
al. 4, 7, 17 al. 2, 19, 23 et 24 du décret n° 82-1359 :
- art. 1 : champ élargi aux « membres des professions libérales » et à « toute autre catégorie de
  travailleurs indépendants » non affiliés ;
- **art. 7 : neuf classes en multiples du SMIG 48 h × 2 400 h** : 2/3, 1, 1,5, 2, 4, 6, 9, 12, 15
  (lu à l'image) ;
- **art. 19 : revenu de référence = moyenne pondérée des coefficients, « rapportée à la valeur du SMIG
  […] en vigueur au moment de la liquidation »** — la pension devient indexée sur le SMIG jusqu'à la
  liquidation ;
- **art. 23 : « révisé en cas de majoration du SMIG », date et modalités « fixées par arrêté du
  ministre des affaires sociales »** ;
- art. 24 : validation des services antérieurs, dans les trois ans, au barème de 13 % à 20 % selon
  l'âge ;
- art. 3 : conversion des cotisations 1982-1988 en coefficients du SMIG (ex. classe 1 de 1982 :
  0,672).

Sans clause d'effet : exécutoire le **22 octobre 1989** [D]. Le **décret n° 93-357** (JORT n° 14 du
19 février 1993, p. 273) proroge l'art. 24 « pour une période d'une année à compter du 22 octobre
1992 » — soit trois ans après le 22 octobre 1989, ce qui corrobore cette date.

### 6.3 Le décret n° 95-1166 : fusion, et ce qui change [T]

Art. 23-30 confirmés tels que le chapitre les cite. Art. 34-39 : les affiliés de 1982 conservent leur
affiliation ; les réserves des deux régimes sont transférées ; les droits transitoires (art. 24 et 16
de 1982) sont préservés ; les cotisations antérieures à 1990 (non agricole) sont converties en
coefficients du SMIG (tableau 1982-1989, art. 37) ; les catégories agricoles 1 / 2 / 3 sont converties
(1,333 / 2 / 2,666 pour les dix premières années, 1 / 1,5 / 2 au-delà, art. 38) ; art. 39 : abrogation
des décrets n° 82-1359 et 82-1360. Dépôt le 14 juillet 1995 : exécutoire le **19 juillet 1995** [D].

### 6.4 Le cœur du régime, réforme par réforme

| Élément | 1982 (82-1359 / 82-1360) | 1989 (89-1611, non agricole) | 1995 (95-1166) | 2002 (2002-3018) |
|---|---|---|---|---|
| Âge | 65 ans ; dès 60 avec −0,5 %/trimestre (NA) ; 65 ans (A) | inchangé | **65 ; dès 60 avec −0,5 %/trimestre, pour tous** (art. 24) | inchangé |
| Stage | 120 mois (NA) ; 40 trimestres (A) | inchangé | **40 trimestres effectifs** (art. 23) | inchangé |
| Taux | 30 % + 0,5 %/3 mois, plafond 80 % (NA) ; 40 % + 0,5 %/trimestre, 80 % (A, par renvoi) | inchangé | **30 % + 0,5 %/trimestre, 80 %, pour tous** (art. 26) | inchangé |
| Assiette / référence | 6 classes en dinars ; moyenne des forfaits de carrière (NA) ; SMAG × 300 j × coefficient moyen 1-2 (A) | **9 classes × SMIG ; SMIG à la liquidation** | 10 classes 1 à 18 × SMIG ou SMAG ; SMIG/SMAG à l'ouverture du droit (art. 7, 25) | inchangé |
| Minimum | **1/2 SMIG × 2 400 h** (NA) ; aucun (A) | inchangé | **30 % du SMIG × 2 400 h ou du SMAG × 300 j** (art. 29) | inchangé |
| Carrière courte | pension au prorata en période transitoire ; allocation dès 10 trimestres (A) | — | **versement unique = cotisations** (art. 28) | inchangé |
| Revalorisation | révision par décret en cas de hausse sensible du niveau de vie | **par arrêté, en cas de majoration du SMIG** | par arrêté, en cas de majoration du SMIG ou du SMAG (art. 30) | **automatique, taux de variation du SMIG/SMAG** |

Revalorisations propres effectivement publiées : **arrêté du 29 juillet 1998** (effet 1er mai 1998),
seul trouvé. Chiffres du chapitre **confirmés** au fascicule : non agricole 2,33600 (1984) … 1,07551
(1996), 1,03684 (1997), 1,00000 (1998) ; agricole 1,07551 jusqu'en 1996. Les coefficients commencent
en **1984** : ce sont des pensions ouvertes sous les décrets de 1982. La note de la clé
`arrete-1998-07-29-revalorisation-rtns` (« texte non lu ») est à mettre à jour.

---

## 7. Les Tunisiens à l'étranger (RTTE)

Décret n° 89-107, JORT n° 4 du 17 janvier 1989, p. 98-99 **[T]** (OCR intégral) : les affirmations du
chapitre sont **confirmées** (art. 1-3, 6-8, 17-24 ; 4 classes 2 / 4 / 6 / 9 ; 10,65 % dont 5,25 % ;
65 / 60 ans ; 30 % à 120 mois + 0,5 %/3 mois, 80 % ; invalidité 30 % à 60 mois ; **minimum 1/2 SMIG** ;
révision par décret « en cas de hausse sensible du niveau de vie » ; validation dans les deux ans).
Sa formule (âge, taux, minimum, révision) est celle du décret n° 82-1359 (art. 18, 20-23), non une
préfiguration de 1995 comme le dit le chapitre (§ 13, point 7) ; son assiette, en revanche (classes en
multiples du SMIG, SMIG à la liquidation), annonce celle que le décret n° 89-1611 donnera aux
non-salariés neuf mois plus tard.

**Décret n° 91-604** (JORT n° 32/1991, p. 1008) **[T]** : « Les dispositions de l'article 24 du décret
sus-visé n° 89-107 […] sont prorogées pour une période d'une année, à compter du 10 janvier 1991. »
Ferme le TODO du chapitre. Observation [D] : l'administration fait courir les deux ans de l'art. 24
depuis le 10 janvier 1989, date de signature, et non depuis le 19.

**Réformes** : aucune. Aucun décret de révision pris en application de l'art. 23 n'a été trouvé
(requêtes « travailleurs tunisiens a l'etranger », FTS `"89-107"` sur titre et objet). Seconde voie :
les visas de l'arrêté conjoint du 10 juillet 2020 citent le décret n° 89-107 « tel que modifié et
complété par le décret n° 91-604 ». **Le régime n'a donc ni revalorisation automatique ni texte de
revalorisation publié au JORT** ; comment la CNSS revalorise ces pensions n'est pas établi (**TODO**).

---

## 8. Les artistes, créateurs et intellectuels (RACI)

Loi n° 2002-104 et décret n° 2003-894 **[T]** (fascicules décodés) : affirmations du chapitre
**confirmées** (loi, art. 1, 12-15, 20-23, 31 ; décret, art. 5 : 2 / 2,5 / 3 / 4 / 5 / 7 / 10 / 13 /
16 / 18 ; art. 16-17 : 30 % à 40 trimestres + 0,5 %, 80 %, minimum 200 D par mois).

**L'article 20, tranché sur l'édition arabe** (JORT ar. n° 106/2002, lu à l'image) : « يحدد مبلغ
جراية الباقين بعد الوفاة بنسبة 50% من جراية الشيخوخة أو العجز التي انتفع بها الهالك أو كان قد
استحقها يوم وفاته **ويرفع في مقدار هذه النسبة إلى حد 75%** من جراية الشيخوخة أو العجز في صورة وجود
أبناء منتفعين بجراية. » Traduction de travail : « le montant de la pension de survivants est fixé à
50 % […] ; **ce taux est relevé jusqu'à 75 %** de la pension de vieillesse ou d'invalidité en cas
d'existence d'enfants bénéficiaires d'une pension. » Le « majoré de 75 % » du français est donc un
« porté à 75 % » (« إلى حد »). Reste une question que le texte ne tranche pas : « جراية الباقين »
(pension de survivants) désigne-t-elle la pension du conjoint seul ou l'ensemble conjoint +
orphelins ? L'art. 25 plafonne de toute façon le cumul à la pension du défunt. À signaler en ces
termes, sans choisir.

Compléments :
- loi, **art. 33-38** : dispositions transitoires — pension d'au moins 200 D sans cotisation pour les
  plus de 55 ans titulaires d'une indemnité permanente de l'État (art. 33), ou sans revenu permanent
  (art. 34) ; option RTNS / RACI dans l'année (art. 37-38) ;
- décret, art. 9 et 14 : les majorations du SMIG ne comptent pour les cotisations et les indemnités
  qu'au 1er janvier suivant ;
- dates exécutoires : loi **5 janvier 2003**, décret **5 mai 2003** [D].

**Réformes** : seule la loi n° 2007-43 (art. 3 et 5, tiret 5 de l'art. 22) touche le régime. Aucun
texte ne relève le minimum de 200 D (FTS `"2002-104" OR "2003-894"` sur titre et objet ; rien dans
les fascicules 2024-2026 du corpus local ni dans les n° 57-93 de 2026). **Seconde voie
incomplète** : les visas de 2020 et de 2026 ne citent pas la loi n° 2002-104 (**TODO**).

---

## 9. Les travailleurs à faibles revenus (RTFR)

### 9.1 La loi n° 2002-32 [T]

Affirmations du chapitre **confirmées** : art. 1 (cinq catégories ; pêcheurs sur bateaux ≤ 5
tonneaux ; extension « par décret à d'autres catégories »), 7 (7,5 % sur les 2/3 du SMAG ou du SMIG),
13 (65 ans, 120 mois), 14, 16-18, 21-28, 32. Compléments : art. 2 (option pour les catégories c, d,
e), **art. 37** (maintien en activité au-delà de l'âge pour achever le stage ; au décès avant le
stage, versement unique des retenues pour pension), art. 38 (option dans l'année).

**Date exécutoire : le chapitre écrit « publiée le 15 mars 2002, elle devient exécutoire le 17 »,
selon la règle antérieure à 1993.** Le fascicule porte : « déposé au siège du gouvernorat de Tunis le
16 mars 2002 » → exécutoire le **21 mars 2002** [D] (§ 13, point 8).

### 9.2 Le décret n° 2002-916, que le chapitre ne cite pas [T]

- art. 13 : assiette mensuelle = 2/3 du SMIG × 200 heures (employés de maison, artisans) ou 2/3 du
  SMAG × 25 jours (autres) ; une majoration du salaire minimum ne compte qu'au 1er janvier suivant ;
- art. 14-15 : 7,5 %, dont **5 % pensions** et 2,5 % soins ; 5 % employeur / 2,5 % salarié, ou tout à
  la charge des indépendants ;
- **art. 22 : la pension est calculée sur le SMIG × 200 h ou le SMAG × 25 j « en vigueur à la date
  d'ouverture du droit à pension », mais « n'est pris en compte qu'à concurrence des deux tiers lors
  de la fixation de la fraction de la pension résultant des périodes de cotisations qui dépassent les
  120 mois »** — c'est la règle que le chapitre déduit de la loi (« deux bases distinctes ») ;
- art. 23-24 : 30 % ; majoration 0,5 %/trimestre ; 80 % ;
- **art. 25 : revalorisation selon l'évolution du SMIG ou du SMAG, mais une majoration n'est prise en
  compte « qu'à partir du premier jour de l'année civile qui suit »** ;
- art. 26 : maintien en activité ; art. 27-30 : option.

Exécutoire le **7 mai 2002** [D].

### 9.3 Formule, telle que les textes la donnent [D]

Avec $S_m$ le salaire minimum mensuel du secteur à l'ouverture du droit (SMIG × 200 h ou SMAG × 25 j)
et $q$ le nombre de trimestres au-delà de 120 mois :
$P_{mensuelle} = 30\,\% \cdot S_m + 0{,}5\,\% \cdot q \cdot \tfrac{2}{3} S_m$, dans la limite de
$80\,\% \cdot \tfrac{2}{3} S_m$ (loi, art. 14 ; décret, art. 22-23). Chaque trimestre
supplémentaire ajoute $0{,}5\,\% \times 2/3 = 0{,}333\,\%$ de $S_m$ ; le plafond, 53,33 % de $S_m$,
est donc atteint à $q = (53{,}33 - 30)/0{,}333 = 70$ trimestres au-delà du stage, soit **330 mois** de
cotisations. Dérivation à faire relire : la loi dit « le montant total de la pension » ≤ 80 %
« dudit salaire ».

### 9.4 Extensions et rattachements

| Texte | Effet | Contenu |
|---|---|---|
| Loi n° 2007-43, art. 3-5 | 2 juil. 2007 [D] | art. 25, tiret 5 (fille) ; suppression de « mineur » |
| **Décret gouvernemental n° 2019-379** | **4 mai 2019** [D] | ajoute à l'art. 2 du décret n° 2002-916 un **paragraphe f)** : « Les femmes récoltant les huîtres et les ouvriers saisonniers et mobiles appartenant au milieu rural et travaillant dans le secteur agricole y compris la femme employée dans ce secteur » (saisonniers : moins de 45 jours par trimestre chez un employeur, ou plusieurs employeurs) ; assiette et pension sur le SMAG (art. 13 b et 22 b nouveaux) ; cotisations à leur charge ; paiement possible par d'autres organismes (art. 19) |
| Arrêté du 19 juin 2019 [M] | — | pièces d'affiliation de ces catégories |
| Décret-loi n° 2020-33, art. 7 | — | l'auto-entrepreneur relève du titre II de la loi n° 2002-32 (§ 2.4) |
| Loi n° 2021-37, art. 4 | 6 mois après la publication | les employés de maison restent régis par la loi n° 2002-32 |

« Huîtres » est la traduction du JORT français ; l'arabe dit « المحار » (coquillages). **Aucune
réforme du cœur** : le phrasé du chapitre (« Seul son article 25 a été modifié ») est exact pour la
loi, mais incomplet pour le régime.

---

## 10. Le régime des travailleuses agricoles (décret-loi n° 2024-4)

JORT n° 129 du 23 octobre 2024, p. 2897-2901 **[T]**. Pas de clause d'effet (art. 52) ; « déposé au
siège du gouvernorat de Tunis le 23 octobre 2024 » → exécutoire le **28 octobre 2024** [D].

- **Art. 1 et 17** : « un régime spécifique de sécurité sociale des travailleuses agricoles comportant
  l'octroi des prestations de l'assurance maladie et les pensions de vieillesse, d'invalidité et des
  survivants » ; champ : la travailleuse non salariée à titre principal pour son propre compte, et la
  salariée « pour une période de travail égale ou supérieure à 15 jours de travail par mois et avec une
  moyenne au moins égale à 45 jours par trimestre ou 180 jours par an », sauf si son employeur est
  affilié à un régime légal couvrant les mêmes risques pour tous ses employés.
- **Art. 18** : gestion par la CNSS. **Art. 20 et 23** : l'État prend en charge les cotisations de la
  travailleuse pendant les trois premières années d'activité.
- **Art. 26** : **65 ans**, **120 mois** de cotisations effectives et validées, pas d'activité
  assujettie. **Art. 27** : pension possible **dès 60 ans** avec 120 mois (sans décote énoncée).
  **Art. 28** : allocation de vieillesse en deçà de 60 mois.
- **Art. 29-30** : invalidité réduisant d'**au moins la moitié** la capacité (et non des deux tiers),
  stage de 60 mois.
- **Contrôle sur l'édition arabe** (Ja1292024, p. 5295, couche texte) : art. 26 « خمس وستين سنة » et
  « 120 شهرا » ; art. 27 « بداية من سن الستين سنة » après 120 mois ; art. 28 « إذا لم تتجاوز مدة
  الاشتراكات الفعلية والمعتبرة 60 شهرا » (allocation si la durée **ne dépasse pas** 60 mois) ; art. 29
  « يخفّض إلى النصف على الأقل ». Les deux éditions concordent. **Entre 61 et 119 mois, le décret-loi ne
  prévoit rien** : ni pension, ni allocation.
- **Art. 31-32** : conjoint survivant (lien conjugal au décès) ; orphelins 16 / 21 / 25 ans, fille sans
  ressources, infirmes.
- **Art. 33** : « Les taux, les modalités et les procédures de bénéfice de la pension de vieillesse,
  de l'allocation de vieillesse, de la pension d'invalidité et des pensions octroyées au conjoint et
  aux orphelins sont fixés par décret. »

**Ce décret n'a pas été trouvé** : ni dans `jort_cache` (jusqu'au 10 avril 2026), ni dans les
fascicules 2024-2026 du corpus local (scan FR et AR des références « 2024-4 », « العاملات
الفلاحيات », « 4 لسنة 2024 »), ni dans les n° 57-93 de 2026. Une enquête de presse du 27 août 2026
l'affirme aussi (Nawaat, S. Zghidi : « ولم يتم إنفاذه بإصدار الأوامر والقرارات والاتفاقيات اللازمة »),
source secondaire. **Le régime a donc, à ce jour, un âge et un stage, mais ni taux ni formule.** La loi
n° 2024-48 (LF 2025) crée le « صندوق الحماية الاجتماعية للعاملات الفلاحيات » ([M], JORT n° 149/2024,
p. 6420), qui relève du financement.

---

## 11. Les pêcheurs (décret n° 77-546) [T]

- art. 1 : extension du régime de 1974 (§ 2.2) ;
- **art. 3** : pour les pêcheurs à la part sur des bateaux de moins de 30 tonneaux, les pêcheurs
  indépendants et les petits armateurs, **revenu forfaitaire = SMIG mensuel × coefficient** : patron
  de pêche 3, second du patron 2, mécanicien 2, second mécanicien 1,5, ramandeur 2, pêcheur
  spécialisé 1,5, pêcheur 1, petit armateur 1 ; ajusté avec le SMIG ; cotisation minimale d'une
  quinzaine ;
- art. 4 : salaire réel sur les bateaux de 30 tonneaux et plus ;
- art. 5 : taux = ceux de l'art. 41 de la loi n° 60-30 et de l'art. 9 du décret n° 74-499 ;
- art. 9 : mutuelles de pêcheurs collectrices ; art. 12 : exécution, sans clause d'effet.
- **Décret n° 80-103** : art. 11 bis — validation forfaitaire de **8 mois** par année entre 45 ans et
  l'âge à la publication, dans la limite de **102 mois**, pour les assurés d'au moins 45 ans comptant
  18 mois de cotisations « au cours des [chiffre illisible] premières années » (**TODO** : éd. ar.).
- **Décret n° 82-1028** et rectificatif : art. 3 bis, à titre transitoire pendant deux ans « à compter
  du 1er jour du trimestre suivant la promulgation », assiette uniforme de **2/3 du SMIG mensuel** ;
  pour les pensions, les cotisations se comptent par périodes de 15 jours.

Ce régime n'a pas de formule de pension propre : il relève d'une section « autres éléments » (assiette,
validation), non d'un régime à part entière.

---

## 12. Recensement : méthode et seconde voie

**Première voie** — `jort_cache.db` (78 953 textes, dernière publication indexée le 10 avril 2026) :
- FTS5 sur `titre` **et** `objet` : `"81-6"`, `(agricole OR agricoles) AND (pension OR vieillesse OR
  retraite OR securite OR sociale OR cotisations)`, `(independants OR "non salaries" OR artistes OR
  complementaire OR "certaines categories" OR "89-107" OR "2002-104" OR "2003-894" OR "2002-32" OR
  "95-1166" OR entrepreneur OR domestique OR "travailleuses agricoles") AND (…)`,
  `chantiers AND (…)`, `pecheur`;
- LIKE sans accents et LIKE sur les intitulés arabes après 2008 (« الضمان الاجتماعي », « جرايات »,
  « غير الأجراء », « الفنانين », « المبادر الذاتي », « 32 لسنة 2002 », « 1166 لسنة 1995 », « المحار »,
  « العاملات الفلاحيات ») ;
- LIKE `%18 novembre 1978%` et `%regime complementaire%` : un seul modificatif (1997).

**Au-delà du 10 avril 2026** : scan en texte des fascicules FR et AR 2024-2026 du corpus local
(n° 1-56 de 2026), puis des n° 57-93 de 2026 déjà téléchargés depuis pist.tn (scratchpad
`pist/`, extraction arabe normalisée : suppression des marques bidirectionnelles, sans quoi « 6 لسنة
1981 » n'est pas trouvé). Aucun texte ne modifie l'un des régimes. Le n° 58 de 2026 reste non consulté
(voir la note RSNA).

**Seconde voie — les visas** :

| Texte (visas) | Loi n° 81-6 | Décret n° 95-1166 | Loi n° 2002-32 | Décret n° 2002-916 | Décret n° 89-107 | Décret n° 77-546 |
|---|---|---|---|---|---|---|
| Arrêté conjoint du 10 juil. 2020 (JORT n° 67, p. 1515-1516) | dernier : loi n° 2007-43 | dernier : décret n° 2008-172 | modifiée par la loi n° 2007-43 | cité | modifié par le n° 91-604 | dernier : décret n° 82-1028 |
| Décret n° 2019-379 (JORT n° 34/2019, p. 1277) | notamment loi n° 2007-43 | notamment n° 2008-172 | modifiée par la loi n° 2007-43 | — | — | — |
| Arrêté conjoint du 29 août 2025 (JORT n° 107 du 29 août 2025) | dernier : loi n° 2007-43 | dernier : n° 2008-172 | cité | « modifié et complété » | — | — |
| Arrêté conjoint du 5 août 2026 (JORT n° 80) | **éd. ar.** : « وآخرها القانون عدد 43 لسنة 2007 » (absent des visas de l'éd. fr.) | dernier : n° 2008-172 | modifiée par la loi n° 2007-43 | modifié par le **décret gouvernemental n° 2019-379** | — | — |

L'arrêté de 2020 recense, dans ses visas, les textes des « différents régimes de sécurité sociale »
dont la CNSS sert des pensions : 74-499, **77-546**, 81-6, 89-107, 95-1166, 2002-32 / 2002-916. **La
loi n° 2002-104 n'y figure pas**, ni dans ceux de 2026.

---

## 13. Écarts avec le chapitre actuel, à corriger par le rédacteur

1. **RTNS « institué par le décret n° 95-1166 »** (l. 780) : faux. Les non-salariés sont couverts
   depuis le **1er juillet 1982** (décrets n° 82-1359 et 82-1360), que le décret de 1995 fusionne et
   abroge (art. 34-39). Preuve interne : le chapitre cite lui-même les coefficients de l'arrêté de
   1998 pour des pensions ouvertes **depuis 1984**. Même correction à apporter à la définition du
   glossaire `rtns`.
2. **« Les paramètres de la pension de vieillesse sont donc ceux de 1995, inchangés depuis trente
   ans »** (l. 790) : faux dans les deux sens, selon le secteur.
   - **Non agricole** : l'âge (65 / 60 ans avec −0,5 %/trimestre), le taux (30 % + 0,5 %) et le
     plafond (80 %) datent de **1982** (décret n° 82-1359) ; le minimum est passé de **1/2 SMIG (1982)
     à 30 % (1995)** ; la référence au SMIG à la liquidation date de **1989**.
   - **Agricole** : 1995 est une **réforme du cœur** du régime de 1982 (décret n° 82-1360, qui
     renvoyait à la loi n° 81-6) : taux de **40 % → 30 %** ; **création** d'un minimum (30 % du SMAG),
     là où il n'y en avait pas ; départ **dès 60 ans avec décote**, là où l'âge était de 65 ans
     seulement ; référence SMAG × 300 j × coefficient moyen de carrière (1 / 1,5 / 2) → classes 1 à
     18. Rapprochement [D], non énoncé par le texte : les coefficients de conversion de l'art. 38 pour
     les dix premières années (1,333 / 2 / 2,666) valent exactement 4/3 × (1 / 1,5 / 2), et 4/3 =
     40 % / 30 % ; appliqués aux seules dix premières années — la durée du stage —, ils semblent
     compenser la baisse du taux sur les périodes passées. Et « Ce plancher est la seule indexation qu'ait connue le
   régime avant 2002 » (l. 786) est inexact : depuis 1989, la pension est révisée par arrêté en cas de
   majoration du SMIG (89-1611, art. 23 ; 95-1166, art. 30), et le revenu de référence suit le SMIG
   jusqu'à la liquidation.
3. **RSA, droits dérivés** (l. 730) : le chapitre expose l'état de 1981 comme s'il était l'état
   actuel. La **loi n° 96-66** (4 août 1996 [D]) a remplacé la veuve par le « conjoint survivant »,
   l'antériorité du mariage par le lien de mariage au décès, la **suppression au remariage** par une
   **suspension limitée au remariage avant 55 ans**, et le plafond « pension de référence du mari »
   par la pension du défunt. En 1981, le droit n'est pas ouvert au « conjoint » mais à « la veuve » et
   au « veuf invalide » (art. 60).
4. **RSA, orphelins** : le chapitre attribue la règle de la fille à la loi n° 2007-43. Elle vient de
   la **loi n° 97-61** (effet **1er mai 1997**), qui porte aussi la limite à **25 ans** en études
   supérieures sans bourse ; la loi n° 2007-43 réécrit ce paragraphe d) (appréciation au décès,
   suspension définitive) et supprime « mineur ». Le tableau `tbl-comparaison-secteurs` (ligne
   « Orphelin », colonne agricole) est à compléter : 16 / 21 / 25 ans depuis 1997.
5. **RSA, carrières courtes** (l. 721) : l'affirmation est exacte pour les art. 70-73, mais omet
   l'**art. 81** (pension **au prorata** des trimestres en période transitoire quand le total est
   inférieur à 40) ; le rectificatif retire par ailleurs la mention « allocation » des art. 74-76.
6. **Callout « Un rectificatif reste à confronter »** (l. 704-708) : à lever. Le rectificatif (lu en
   entier, § 3.3) ne touche aucun chiffre ni la date d'effet cités.
7. **RTTE** (l. 798) : « ce sont celles que le régime des non-salariés reprendra six ans plus tard ».
   L'inverse : la formule du RTTE (1989) reprend celle du décret n° 82-1359 (art. 18, 20-23) :
   65 / 60 ans, 30 %, 0,5 % par 3 mois, 80 %, minimum 1/2 SMIG, révision par décret ; seule son
   assiette (classes × SMIG) précède la réforme de 1989 des non-salariés.
8. **RTFR, date exécutoire** (l. 828) : « publiée le 15 mars 2002, elle devient exécutoire le 17 »
   applique la règle d'avant 1993. Dépôt le 16 mars 2002 → **21 mars 2002**.
9. **Régime complémentaire, survivants** (l. 769) : « supprimée en cas de remariage » est l'état de
   1978. Depuis l'**arrêté du 27 janvier 1997** : conjoint survivant, lien de mariage au décès,
   **suspension si remariage avant 55 ans**, plafond égal à la pension du défunt.

10. **RSA, citation de l'art. 50** (l. 719) : le chapitre cite entre guillemets « affecté du
    coefficient multiplicateur ayant servi de base au calcul des cotisations ». Le texte, lu à l'image
    (JORT n° 9/1981, p. 270), dit « affecté du **coefficient multiplicateur moyen** ayant servi de
    base… ». Citation à rétablir.

Points confirmés sans changement : RSAA (tableau `tbl-rsa-rsaa`), RTTE (sauf le point 7), RACI (art.
12-17, 21-23, 31), RTFR (art. 13-18, 23-28, 32), arrêté de 1998 (coefficients). RACI, art. 20 :
l'ambiguïté signalée par le chapitre est levée sur l'édition arabe (§ 8).

TODO du chapitre fermés par cette note : rectificatif de la loi n° 81-6 (l. 708) ; décret n° 91-604
(l. 806) ; départ anticipé et pension minimale du RSA (l. 716, l. 727 : aucun texte, confirmé par
les visas de 2020 et 2026 qui donnent la loi n° 2007-43 pour dernier modificatif).

---

## 14. Données disponibles par régime

**Dans tunisia-data (`data/processed/caisses/`)** :
- `cnss_pensions_par_regime.csv` : dépenses de pensions par régime pour **2016, 2017, 2019, 2020**
  (10 lignes : RSNA, complémentaire, RSA, RSAA, RTNS NA, RTNS A, RTTE, RACI, « travailleurs de
  chantiers (convention) », faibles revenus) ; actifs et pensionnés par régime pour **2019**.
- `cnss_effectifs_par_regime.csv` : actifs et pensionnés par régime, **2000 et 2020**.
- `bit2002_couverture_1989_1999.csv` : assujettis et affiliés par grand régime, 1989-1999 (Chaabane,
  BIT 2002 ; clé `chaabane-2002-ess4`).
- `cnss_rsna_annuaires.csv` : RSNA seul.

**Dans les annuaires** (`data/raw/caisses/cnss/annuaires/`, clé `cnss-annuaires-statistiques`) — les
sommaires lus montrent **une partie par régime**, avec pour chacun un tableau « Evolution de
l'effectif des pensionnés et des montants des pensions servies par nature » :

| Régime | Annuaire 2013 (fr., séries 2000-2013), page imprimée | Annuaire 2017 (ar., 2000-2017) | Assiette publiée |
|---|---|---|---|
| RC | 4e partie, p. 49 et suiv. | الباب الرابع | effectifs actifs / pensionnés |
| RSA | 6e partie, p. 78 (employeurs, assurés), 81 (catégories professionnelles), 86 (pensions) | الباب السادس | forfait : effectifs par catégorie (coefficients 1 / 1,5 / 2) |
| RSAA | 7e partie, **p. 101 (employeurs, salariés, masse salariale, salaire moyen)**, 112 (pensions) | الباب السابع | **salaires réels** |
| RTNS NA | 8e partie, p. 127 (actifs), **131 (classes de revenu 2002-2013)**, 147 (pensions : ex. 2013, 61 956 pensionnés, 90,3 MD, pension moyenne de vieillesse de décembre 169,094 D) | الباب الثامن | classes |
| RTNS A | 9e partie, p. 162, **166 (classes)**, 182 (pensions) | الباب التاسع | classes |
| RTNS (ensemble) | 10e partie, p. 197, **201**, 217 | الباب العاشر | classes |
| RTTE | 11e partie, p. 232, **235 (classes)**, 240 (pensions) | الباب الحادي عشر | classes |
| RTFR | 12e partie, p. 255-256 (immatriculés par activité), **266 (pensions, travailleurs de chantiers)** | الباب الثاني عشر | forfait 2/3 SMIG / SMAG |
| RACI | 13e partie, p. 280, **282 (classes)**, 287 (pensions) | الباب الثالث عشر | classes |

Décalage entre page imprimée et page du fichier PDF de l'édition 2013 : environ +29 à +30 (p. 147
imprimée = p. 177 du PDF). Ces tableaux **ne sont pas encore extraits** dans tunisia-data.

**Faisabilité d'un taux d'équilibre par régime** (pensions servies / assiette cotisée) :
- **RSAA** : oui directement (masse salariale déclarée et pensions, 2000-2017).
- **RTNS NA / A, RTTE, RACI** : oui par reconstruction de l'assiette forfaitaire = Σ effectifs par
  classe × coefficient × SMIG (ou SMAG) annuel de l'année ; les SMIG/SMAG sont déjà sourcés dans le
  précis. Arbitrage à documenter : classe moyenne annuelle ou fin d'année.
- **RSA** : assiette = effectifs par catégorie × coefficient × SMAG × 300 j — mais la cotisation est
  due sur des jours travaillés (catégorie), non sur 300 j : à vérifier sur la loi n° 81-6, art. 18
  (non relu ici).
- **RTFR** : effectifs × 2/3 SMIG/SMAG × 12 ; mélange de catégories (employés de maison, agricoles).
- **Régime complémentaire** : l'assiette (salaire différentiel) n'est pas publiée.
Aucun annuaire postérieur à 2017 (voir la note RSNA).

---

## 15. Références

### 15.1 Clés existantes (à citer telles quelles)

`loi81-6`, `loi89-73`, `loi2007-43`, `decret89-107`, `decret95-1166`, `decret-96-1797`,
`decret-96-2145`, `decret-2002-3018`, `decret-2004-167`, `decret-2008-172`,
`arrete-1998-07-29-revalorisation-rtns`, `loi2002-104`, `decret2003-894`, `loi2002-32`,
`arrete-1978-11-18-retraite-complementaire`, `decret2026-66`, `decret94-1477`, `decret74-499`,
`loi2003-8`, `decret2003-1128`, `cnss-annuaires-statistiques`, `chaabane-2002-ess4`.

Notes à corriger :
- `loi81-6` : « rectificatif […] non lu » → lu (§ 3.3), il ne touche ni l'art. 88 ni les articles
  cités ; ajouter la loi n° 95-102, la loi n° 96-66 et la loi n° 97-61 comme modificatifs.
- `arrete-1998-07-29-revalorisation-rtns` : « Métadonnées seules ; texte non lu » → texte lu (art. 1-3,
  effet 1er mai 1998, dépôt 10 août 1998).
- `loi2007-43` : « Aucune clause d'entrée en vigueur ; date de dépôt non attestée » → **dépôt le
  27 juin 2007** (mention imprimée du fascicule n° 51), exécutoire le 2 juillet 2007.
- `loi2002-32` : la note dit « correspondance non attestée » avec le régime des bas revenus : elle
  l'est par les annuaires (12e partie « REGIME DES TRAVAILLEURS A FAIBLE REVENU ») ; dépôt le 16 mars
  2002.
- `decret95-1166` : « date d'effet non établie » → dépôt le 14 juillet 1995 (sans clause : 19 juillet).
- `decret89-107` : « date d'effet non établie » → sans clause, 19 janvier 1989 (un jour franc).

### 15.2 Entrées à créer (CSL-JSON, sur le gabarit de `precis/fr/references.json`)

Pour chacune, une entrée miroir dans `precis/ar/references.json` (URL `…A/Ja…`, sauf mention), et un
signalement dans `docs/notes/biblio-a-rapatrier.md`.

```json
[
 {"id": "decret77-546", "type": "legislation",
  "title": "Décret n° 77-546 du 15 juin 1977, organisant la sécurité sociale des pêcheurs",
  "container-title": "Journal officiel de la République tunisienne", "issue": "43", "page": "1655-1657",
  "issued": {"date-parts": [[1977, 6, 15]]},
  "URL": "https://www.pist.tn/jort/1977/1977F/Jo04377.pdf",
  "note": "citation-key: decret77-546\nJORT n° 43 du 21 juin 1977. Art. 1 : étend les régimes des lois n° 60-30 et 60-33 et du décret n° 74-499 aux pêcheurs, patrons pêcheurs, armateurs et petits armateurs. Art. 3 : revenu forfaitaire = SMIG mensuel × coefficient (patron 3 … pêcheur 1). Sans clause d'effet : exécutoire le 23 juin 1977. Lu à l'image."},
 {"id": "decret80-103", "type": "legislation",
  "title": "Décret n° 80-103 du 23 janvier 1980, complétant le décret n° 77-546 du 15 juin 1977, organisant la sécurité sociale des pêcheurs",
  "container-title": "Journal officiel de la République tunisienne", "issue": "6", "page": "252",
  "issued": {"date-parts": [[1980, 1, 23]]},
  "URL": "https://www.pist.tn/jort/1980/1980F/Jo00680.pdf",
  "note": "citation-key: decret80-103\nArt. 11 bis : validation forfaitaire de 8 mois par année entre 45 ans et l'âge atteint, dans la limite de 102 mois. Un chiffre illisible dans l'édition française. Lu (OCR, chiffres relus à l'image)."},
 {"id": "loi81-6-rect", "type": "legislation",
  "title": "Rectificatif à la loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole",
  "container-title": "Journal officiel de la République tunisienne", "issue": "26", "page": "844",
  "issued": {"date-parts": [[1981, 4, 17]]},
  "URL": "https://www.pist.tn/jort/1981/1981F/Jo02681.pdf",
  "note": "citation-key: loi81-6-rect\nJORT n° 26 du 17 avril 1981, p. 844. Corrige les art. 1 al. 3, 11, 39-4, 43, 45 d), 57, 74 al. 1-2, 75 al. 1, 76 al. 1 ; ne touche ni les art. 48-50, 53, 60-73, 80-82 ni l'art. 88. Lu à l'image."},
 {"id": "decret82-1028", "type": "legislation",
  "title": "Décret n° 82-1028 du 8 juillet 1982, modifiant le décret n° 77-546 du 15 juin 1977, organisant la sécurité sociale des pêcheurs",
  "container-title": "Journal officiel de la République tunisienne", "issue": "50", "page": "1579",
  "issued": {"date-parts": [[1982, 7, 8]]},
  "URL": "https://www.pist.tn/jort/1982/1982F/Jo05082.pdf",
  "note": "citation-key: decret82-1028\nJORT n° 50 des 13-16 juillet 1982 ; rectificatif au JORT n° 66/1982, p. 2197. Art. 3 bis : à titre transitoire pendant deux ans, assiette uniforme de 2/3 du SMIG mensuel ; cotisations comptées par quinzaines pour les pensions. Lu (OCR)."},
 {"id": "decret82-1359", "type": "legislation",
  "title": "Décret n° 82-1359 du 21 octobre 1982, étendant le régime de sécurité sociale aux travailleurs indépendants dans le secteur non agricole",
  "container-title": "Journal officiel de la République tunisienne", "issue": "66", "page": "2192-2195",
  "issued": {"date-parts": [[1982, 10, 21]]},
  "URL": "https://www.pist.tn/jort/1982/1982F/Jo06682.pdf",
  "note": "citation-key: decret82-1359\nJORT n° 66 des 19-22 octobre 1982. Art. 7 : six classes forfaitaires (660 à 15 000 D) ; art. 8 : 10,65 % dont 5,25 % pensions ; art. 18 : 65 ans, dès 60 ans avec réduction de 0,5 % par trimestre ; art. 20 : 30 % à 120 mois + 0,5 % par 3 mois, 80 % ; art. 22 : minimum 1/2 SMIG × 2 400 h ; art. 23 : révision par décret ; art. 26 : effet au 1er juillet 1982. Abrogé par le décret n° 95-1166, art. 39. Lu à l'image."},
 {"id": "decret82-1360", "type": "legislation",
  "title": "Décret n° 82-1360 du 21 octobre 1982, relatif à la sécurité sociale des exploitants et travailleurs indépendants dans l'agriculture",
  "container-title": "Journal officiel de la République tunisienne", "issue": "66", "page": "2195-2197",
  "issued": {"date-parts": [[1982, 10, 21]]},
  "URL": "https://www.pist.tn/jort/1982/1982F/Jo06682.pdf",
  "note": "citation-key: decret82-1360\nArt. 1 : extension de la loi n° 81-6 aux travailleurs indépendants, métayers et exploitants ; art. 5 : 6,45 % d'un forfait SMAG × 45 jours par trimestre, coefficient 1, 1,5 ou 2, dont 5,25 % pensions ; art. 8 : 65 ans, SMAG × 300 jours × moyenne des coefficients de carrière ; art. 18 : effet au 1er juillet 1982. Abrogé par le décret n° 95-1166, art. 39. Lu à l'image."},
 {"id": "decret89-1611", "type": "legislation",
  "title": "Décret n° 89-1611 du 10 octobre 1989, modifiant et complétant le décret du 21 octobre 1982, étendant le régime de sécurité sociale aux travailleurs indépendants dans le secteur non agricole",
  "container-title": "Journal officiel de la République tunisienne", "issue": "70", "page": "1653-1654",
  "issued": {"date-parts": [[1989, 10, 10]]},
  "URL": "https://www.pist.tn/jort/1989/1989F/Jo07089.pdf",
  "note": "citation-key: decret89-1611\nJORT n° 70 du 20 octobre 1989. Art. 7 nouveau : neuf classes, coefficients 2/3, 1, 1,5, 2, 4, 6, 9, 12, 15 du SMIG × 2 400 h ; art. 19 : SMIG à la liquidation ; art. 23 : révision par arrêté en cas de majoration du SMIG ; art. 24 : validation (13 à 20 %). Sans clause : exécutoire le 22 octobre 1989. Lu (OCR, barème à l'image)."},
 {"id": "decret90-548", "type": "legislation",
  "title": "Décret n° 90-548 du 27 mars 1990, fixant les modalités de calcul des cotisations des pêcheurs indépendants et des petits armateurs et la répartition du taux de cotisation entre les régimes de sécurité sociale",
  "container-title": "Journal officiel de la République tunisienne", "issue": "24", "page": "490-491",
  "issued": {"date-parts": [[1990, 3, 27]]},
  "URL": "https://www.pist.tn/jort/1990/1990F/Jo02490.pdf",
  "note": "citation-key: decret90-548\nArt. 1 : assiette SMAG × 75 jours par trimestre ; art. 2 : 7,5 % pensions, 4,5 % allocations familiales, 3 % assurances sociales. Lu (OCR)."},
 {"id": "decret91-604", "type": "legislation",
  "title": "Décret n° 91-604 du 30 avril 1991, portant prorogation du délai de validation des services, prévu par le décret n° 89-107 du 10 janvier 1989, étendant le régime de sécurité sociale aux travailleurs tunisiens à l'étranger",
  "container-title": "Journal officiel de la République tunisienne", "issue": "32", "page": "1008",
  "issued": {"date-parts": [[1991, 4, 30]]},
  "URL": "https://www.pist.tn/jort/1991/1991F/Jo03291.pdf",
  "note": "citation-key: decret91-604\nArt. 1 : art. 24 du décret n° 89-107 prorogé d'un an à compter du 10 janvier 1991. Lu (OCR)."},
 {"id": "decret93-357", "type": "legislation",
  "title": "Décret n° 93-357 du 8 février 1993, prorogeant le délai de validation des services dans le cadre du régime de sécurité sociale des travailleurs indépendants du secteur non agricole prévu par le décret n° 82-1359 du 21 octobre 1982",
  "container-title": "Journal officiel de la République tunisienne", "issue": "14", "page": "273",
  "issued": {"date-parts": [[1993, 2, 8]]},
  "URL": "https://www.pist.tn/jort/1993/1993F/Jo01493.pdf",
  "note": "citation-key: decret93-357\nArt. 1 : art. 24 du décret n° 82-1359 prorogé d'un an à compter du 22 octobre 1992. Lu (OCR)."},
 {"id": "loi95-102", "type": "legislation",
  "title": "Loi n° 95-102 du 27 novembre 1995, portant révision de la loi n° 81-6 du 12 février 1981 organisant les régimes de sécurité sociale dans le secteur agricole",
  "container-title": "Journal officiel de la République tunisienne", "issue": "96", "page": "2224",
  "issued": {"date-parts": [[1995, 11, 27]]},
  "URL": "https://www.pist.tn/jort/1995/1995F/Jo09695.pdf",
  "note": "citation-key: loi95-102\nArticle unique : art. 74 al. 1, délai de demande de pension porté à cinq ans. Dépôt le 5 décembre 1995 : exécutoire le 10 décembre 1995. Couche texte."},
 {"id": "loi96-66", "type": "legislation",
  "title": "Loi n° 96-66 du 22 juillet 1996, modifiant la loi n° 81-6 du 12 février 1981 relative à l'organisation des régimes de sécurité sociale dans le secteur agricole",
  "container-title": "Journal officiel de la République tunisienne", "issue": "60", "page": "1603",
  "issued": {"date-parts": [[1996, 7, 22]]},
  "URL": "https://www.pist.tn/jort/1996/1996F/Jo06096.pdf",
  "note": "citation-key: loi96-66\nArticle unique : art. 60, 61, 63 et 69 nouveaux — conjoint survivant ; lien de mariage au décès ; suspension si remariage avant 55 ans et rétablissement ; plafond égal à la pension du défunt. Dépôt le 30 juillet 1996 : exécutoire le 4 août 1996. Couche texte."},
 {"id": "loi97-61", "type": "legislation",
  "title": "Loi n° 97-61 du 28 juillet 1997, amendant la loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole",
  "container-title": "Journal officiel de la République tunisienne", "issue": "61", "page": "1360",
  "issued": {"date-parts": [[1997, 7, 28]]},
  "URL": "https://www.pist.tn/jort/1997/1997F/Jo06197.pdf",
  "note": "citation-key: loi97-61\nArt. 1 : art. 41 al. 3 et 64 nouveaux — orphelin : 16 ans ; 21 ans (secondaire, technique, professionnel) ; 25 ans (supérieur, sans bourse) ; fille sans ressources ; infirme sans limite. Art. 2 : effet au 1er mai 1997. Couche texte."},
 {"id": "arrete-1997-01-27-retraite-complementaire", "type": "legislation",
  "title": "Arrêté du ministre des affaires sociales du 27 janvier 1997, modifiant l'arrêté du 18 novembre 1978, relatif au régime complémentaire de pensions de vieillesse, d'invalidité et de survivants",
  "container-title": "Journal officiel de la République tunisienne", "issue": "11", "page": "183-184",
  "issued": {"date-parts": [[1997, 1, 27]]},
  "URL": "https://www.pist.tn/jort/1997/1997F/Jo01197.pdf",
  "note": "citation-key: arrete-1997-01-27-retraite-complementaire\nArticle unique : art. 21, 22, 24 et 30 du règlement remplacés — conjoint survivant, lien de mariage au décès, suspension si remariage avant 55 ans, plafond égal à la pension du défunt. Dépôt le 11 février 1997 : exécutoire le 16 février 1997. Couche texte."},
 {"id": "decret2002-916", "type": "legislation",
  "title": "Décret n° 2002-916 du 22 avril 2002, relatif aux modalités d'application de la loi n° 2002-32 du 12 mars 2002, relative au régime de sécurité sociale pour certaines catégories de travailleurs dans les secteurs agricole et non agricole",
  "container-title": "Journal officiel de la République tunisienne", "issue": "35", "page": "1058-1061",
  "issued": {"date-parts": [[2002, 4, 22]]},
  "URL": "https://www.pist.tn/jort/2002/2002F/Jo0352002.pdf",
  "note": "citation-key: decret2002-916\nJORT n° 35 du 30 avril 2002. Art. 13 : assiette 2/3 du SMIG × 200 h ou du SMAG × 25 j ; art. 14 : 7,5 % dont 5 % pensions ; art. 22 : pension sur le SMIG × 200 h ou le SMAG × 25 j à l'ouverture du droit, 2/3 pour la fraction au-delà de 120 mois ; art. 25 : revalorisation au 1er janvier suivant la majoration. Dépôt le 2 mai 2002 : exécutoire le 7 mai 2002. Modifié par le décret gouvernemental n° 2019-379. Couche texte décalée (décodée)."},
 {"id": "decret2019-379", "type": "legislation",
  "title": "Décret gouvernemental n° 2019-379 du 22 avril 2019, modifiant et complétant le décret n° 2002-916 du 22 avril 2002, relatif aux modalités d'application de la loi n° 2002-32 du 12 mars 2002",
  "container-title": "Journal officiel de la République tunisienne", "issue": "34", "page": "1277-1278",
  "issued": {"date-parts": [[2019, 4, 22]]},
  "URL": "https://www.pist.tn/jort/2019/2019F/Jo0342019.pdf",
  "note": "citation-key: decret2019-379\nJORT n° 34 du 26 avril 2019. Art. 2 : ajoute un paragraphe f) à l'art. 2 du décret n° 2002-916 — femmes récoltant les coquillages (« huîtres » dans l'éd. fr.) et ouvriers saisonniers et mobiles ruraux du secteur agricole ; art. 1 : assiette et pension sur le SMAG. Dépôt le 29 avril 2019 : exécutoire le 4 mai 2019. Couche texte."},
 {"id": "decret-loi2020-33", "type": "legislation",
  "title": "مرسوم من رئيس الحكومة عدد 33 لسنة 2020 مؤرخ في 10 جوان 2020 يتعلق بنظام المبادر الذاتي",
  "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "54", "page": "1417-1420",
  "issued": {"date-parts": [[2020, 6, 10]]},
  "URL": "https://www.pist.tn/jort/2020/2020A/Ja0542020.pdf",
  "note": "citation-key: decret-loi2020-33\nÉdition française absente (pist.tn 404 ; pdf_fr vide dans jort_cache). Art. 7 : contribution unique, dont 7,5 % sur 2/3 du SMAG ou du SMIG ; le titre II de la loi n° 2002-32 s'applique ; adhésion possible au RTNS (11 %, 4 % pour les retraités). Dépôt le 10 juin 2020. Lu (couche texte arabe)."},
 {"id": "loi2021-37", "type": "legislation",
  "title": "Loi n° 2021-37 du 16 juillet 2021, relative à la réglementation du travail domestique",
  "container-title": "Journal officiel de la République tunisienne", "issue": "68", "page": "2006-2010",
  "issued": {"date-parts": [[2021, 7, 16]]},
  "URL": "https://www.pist.tn/jort/2021/2021F/Jo0682021.pdf",
  "note": "citation-key: loi2021-37\nArt. 4 : les travailleurs domestiques demeurent régis par la loi n° 2002-32 ; art. 29 : entrée en vigueur six mois après la publication. Couche texte."},
 {"id": "decret-loi2024-4", "type": "legislation",
  "title": "Décret-loi n° 2024-4 du 22 octobre 2024, relatif au régime de protection sociale des travailleuses agricoles",
  "container-title": "Journal officiel de la République tunisienne", "issue": "129", "page": "2897-2901",
  "issued": {"date-parts": [[2024, 10, 22]]},
  "URL": "https://www.pist.tn/jort/2024/2024F/Jo1292024.pdf",
  "note": "citation-key: decret-loi2024-4\nJORT n° 129 du 23 octobre 2024. Art. 17-18 : régime spécifique géré par la CNSS ; art. 26-28 : 65 ans, 120 mois, dès 60 ans, allocation en deçà de 60 mois ; art. 29-30 : invalidité de la moitié, 60 mois ; art. 33 : taux et modalités renvoyés à un décret (non publié au 18 septembre 2026). Dépôt le 23 octobre 2024 : exécutoire le 28 octobre 2024. Couche texte."},
 {"id": "arrete-2020-07-10-prime-pensions", "type": "legislation",
  "title": "Arrêté du ministre des affaires sociales et du ministre des finances du 10 juillet 2020, portant attribution d'une prime complémentaire, exceptionnelle et temporaire au profit des personnes dont le montant mensuel net des pensions qui leurs sont servies par la caisse nationale de sécurité sociale et la caisse nationale de retraite et de prévoyance sociale est inférieur ou égal à cent quatre-vingt dinars",
  "container-title": "Journal officiel de la République tunisienne", "issue": "67", "page": "1515-1516",
  "issued": {"date-parts": [[2020, 7, 10]]},
  "URL": "https://www.pist.tn/jort/2020/2020F/Jo0672020.pdf",
  "note": "citation-key: arrete-2020-07-10-prime-pensions\nUtile par ses visas, qui énumèrent les textes des régimes de pension de la CNSS et leur dernier modificatif. Couche texte."}
]
```

Facultatives (seulement si le texte les cite) : `arrete-2019-06-19-affiliation-ruraux` (éd. ar. seule,
JORT n° 52/2019, p. 2109-2110, [M]) ; `loi89-73` est déjà versée.

## 16. Notions à porter au glossaire

| Terme FR | Arabe | Source | État |
|---|---|---|---|
| Régime des salariés agricoles | l'entrée porte « نظام الأجراء الفلاحيين » ; l'annuaire 2017 dit « نظام الأجراء في القطاع الفلاحي » | loi n° 81-6 ; annuaire 2017, الباب السادس | existe (`rsa`) : préciser que le droit de 1981 va à la veuve et au veuf invalide ; mentionner 1996-1997 |
| Régime agricole amélioré | entrée : « النظام الفلاحي المحسَّن » ; annuaire : « نظام الأجراء في القطاع الفلاحي المحسن » | loi n° 89-73 ; annuaire 2017, الباب السابع | existe (`rsaa`, provisoire) : la forme de l'annuaire peut servir de validation |
| Régime des travailleurs non salariés | « نظام العملة غير الأجراء » (annuaire 2017, الباب العاشر) | décrets n° 82-1359, 82-1360, 95-1166 | existe (`rtns`) : **définition à corriger** (né en 1982, fusionné en 1995) |
| Régime des travailleurs à faibles revenus | entrée : « نظام العملة ذوي الدخل الضعيف » ; **annuaire 2017 : « نظام العملة ذوي الدخل المحدود »** | loi n° 2002-32 ; annuaire 2017, الباب الثاني عشر | existe (`regime-bas-revenus`) : remplacer le terme arabe par celui de l'annuaire, et étendre la définition au décret n° 2019-379 |
| Régime des Tunisiens à l'étranger | annuaire : « نظام العملة التونسيين بالخارج » | décret n° 89-107 | existe (`rtte`) : ajouter la forme de l'annuaire en synonyme |
| Régime des artistes, créateurs et intellectuels | annuaire : « نظام الفنانين والمبدعين والمثقفين » | loi n° 2002-104 | existe ; déjà synonyme |
| **Régime complémentaire** (de pension) | « النظام التكميلي للجرايات » (annuaire 2017, الباب الرابع) | arrêté du 18 nov. 1978 | **à créer** (`regime-complementaire`) : le chapitre pose une ancre `#sec-regime-complementaire` mais aucune entrée n'existe |
| **Classe de revenu** / revenu forfaitaire | « شريحة الدخل » (décret-loi n° 2020-33, art. 7 : « الانخراط بشريحة دخل ») | décrets n° 82-1359, 89-1611, 95-1166 (art. 7), 2003-894 (art. 5) | **à créer** : notion commune à quatre régimes |
| **Valeur du point** (de retraite) | non lue | règlement de 1978, art. 18 | à envisager (`valeur-du-point`) |
| **Régime des travailleuses agricoles** | « نظام الحماية الاجتماعية للعاملات الفلاحيات » (intitulé du décret-loi) | décret-loi n° 2024-4 | **à créer** |
| Auto-entrepreneur | « المبادر الذاتي » | décret-loi n° 2020-33 | à envisager (ou renvoi dans `regime-bas-revenus`) |

## 17. Lacunes (TODO, rien n'a été inventé)

- **« Travailleurs de chantiers (convention) »** : ligne de pensions publiée par la CNSS (≈ 10 MD par
  an, 2016-2020) et partie RTC de l'annuaire 2013, sans texte fondateur identifié au JORT.
- **Décret d'application de l'art. 33 du décret-loi n° 2024-4** : non trouvé jusqu'au n° 93 de 2026
  (n° 58 de 2026 non consulté ; couverture 2025 du corpus local partielle : 117 fascicules FR).
  Contrôler pist.tn fascicule par fascicule pour 2025 avant d'écrire qu'il n'existe pas.
- **RTTE : revalorisation** — aucun décret de l'art. 23 trouvé ; mode de revalorisation effectif non
  établi.
- **RACI** : seconde voie par les visas incomplète (loi n° 2002-104 absente des visas de 2020 et 2026) ;
  sens de « جراية الباقين » à l'art. 20 (conjoint seul ou ensemble).
- **Titre I bis de la loi n° 60-30**, abrogé par la loi n° 81-6 (art. 87) : ni son texte ni sa date
  n'ont été lus ; rien n'établit qu'il comportait des pensions agricoles avant 1981.
- **Décret n° 80-103** : chiffre illisible (« au cours des … premières années ») ; lire l'éd. ar.
- **Arrêté du 19 juin 2019** : visas et contenu non lus (métadonnées).
- **Loi n° 81-6, art. 18** (coefficients de qualification 1 / 1,5 / 2) : cité par le chapitre, non
  relu ici.
- **Règlement de 1978** : articles relus à l'OCR seulement (numérotation et taux) ; l'annexe I n'est
  pas lue.
- **Pagination arabe** : relevée seulement pour la loi n° 81-6 (art. 53, p. 295 de l'éd. ar.).
- Les dates de publication de `jort_cache` n'ont pas été confrontées au pied de page pour le
  décret n° 80-103.
