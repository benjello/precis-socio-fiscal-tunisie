# Prestations contributives non-retraite — dossier documentaire

> Note **documentaire** répondant à l'étape 1 de `docs/notes/prestations-sociales-plan.md` §5,
> pour la partie 1.2 du livre « Prestations sociales » (prestations servies par la CNSS, la CNRPS
> et la CNAM **hors branche vieillesse**). Elle ne rédige pas de prose de précis et n'a modifié
> aucun fichier de `precis/`.
>
> **Trois niveaux d'attestation**, portés sur chaque ligne :
> - **[T]** *attesté — texte lu* : article lu dans le JORT, à l'image ou sur le miroir iort.tn ;
> - **[M]** *attesté — métadonnées `jort_cache.db`* : numéro, dates, fascicule, page seulement ;
> - **[D]** *dérivé* : déduit d'un autre texte ou d'un renvoi, non lu dans le texte lui-même.
>
> **Trois dates par texte** : signature / publication au JORT (n° + page) / **effet tel que
> l'énonce l'article**. Quand aucun article d'entrée en vigueur n'a été lu, la date d'effet est
> portée **« non établie »** — jamais dérivée de la date de publication.
>
> **Outillage.** `www.pist.tn` présente un certificat TLS expiré ; toutes les URL ci-dessous ont
> été vérifiées par `curl -sk -o /dev/null -w "%{http_code} %{content_type} %{size_download}"`,
> réponse **HTTP 200**, `application/pdf`, taille non nulle (un 404 rend 289 octets de HTML).
> Convention de nommage confirmée : `https://www.pist.tn/jort/<année>/<année>F/Jo<n° sur 3
> chiffres><année sur 2 chiffres jusqu'en 1999, 4 à partir de 2000>.pdf`.
> Les textes antérieurs à 2000 ont été océrisés (`ocrmypdf -l fra --force-ocr` puis `pdftotext`)
> **et relus à l'image** pour tout montant, taux ou tableau.

---

## 0. Résultats principaux

**R1 — Les taux et le plafond des allocations familiales ont quatre âges, et aucun n'est 1960.**
La série de l'article 61 alinéa 2 de la loi n° 60-30, **établie texte par texte, lue à l'image** :

| Depuis | Texte | Taux par rang | Plafond trimestriel |
|---|---|---|---|
| origine (1960) | loi n° 60-30, art. 61 | **15 %** pour chaque enfant | bande **52 D – 500 D** |
| **1er janvier 1976** | **loi n° 75-82** du 30 déc. 1975, art. 2 | **18 / 16 / 14 / 12 %** (1er au 4e enfant) | **72,000 D** |
| **1er mai 1986** | **loi n° 86-75** du 28 juill. 1986, art. 2 | **18 / 16 / 14 / 12 %**, inchangés | **122,000 D** |
| **1er janvier 1989** | **loi n° 88-38** du 6 mai 1988, art. 5 | **18 / 16 / 14 %** — le 4e rang est supprimé | **122,000 D**, inchangé |

Trois conséquences. Les **taux** 18/16/14 datent de **1976**, non de 1988 ; le **plafond de 122 D**
date de **1986**, non de 1988 ; ce que la loi n° 88-38 apporte, c'est la **suppression du quatrième
rang** et la limitation corrélative aux trois premiers enfants (art. 52 al. 2-4 nouveaux). Les
paramètres openfisca sont **justes en valeur et faux en date de trois manières différentes** : ils
datent de `1960-01-01` des taux de 1976 et un plafond de 1986, et ils ignorent le rang 4 à 12 %
ouvert de 1976 à 1988.

Cela résout aussi l'anomalie apparente entre le **plafond de 500 D** de 1960 et celui de **122 D**
de 1989, qui aurait pu se lire comme une coupe brutale : le passage se fait **par le bas**, la
bande 52-500 D à 15 % ayant été remplacée en 1976 par un plafond unique de **72 D** à des taux plus
élevés, relevé à 122 D en 1986. La rupture est celle de **1976**, pas celle de 1988.

**R2 — La chaîne modificative de la loi n° 60-30 a été dépouillée intégralement, sur les seize
lois de 1961 à 2007** que `jort_cache.db` recense, chacune ouverte et lue :

| Loi | Ce qu'elle modifie | Touche l'art. 61 ? |
|---|---|---|
| n° 61-9 (29 avr. 1961) | non identifié précisément (OCR) | non |
| n° 63-26 (15 juill. 1963) | délibérations du conseil d'administration ; art. 35 | non |
| n° 64-31 (2 juill. 1964) | art. 69 (article unique) | non |
| n° 70-34 (9 juill. 1970) | art. 6, 34, 36, 37, 38, **58**, 70, 71, 78 | non |
| n° 74-101 (25 déc. 1974, LF 1975) | dispositions diverses | non |
| **n° 75-82 (30 déc. 1975)** | **art. 61 al. 2** | **OUI** |
| **n° 80-36 (28 mai 1980)** | **ajoute la section I bis et l'art. 65 bis** | non (mais crée la MSU) |
| n° 81-5 (12 févr. 1981) | art. 24 bis, art. 91 4° | non |
| n° 82-71 (15 août 1982) | prestations familiales des licenciés | non |
| **n° 86-75 (28 juill. 1986)** | **art. 61 al. 2** | **OUI** |
| **n° 88-38 (6 mai 1988)** | **art. 52 al. 2-4, art. 61 al. 2, art. 110, art. 111 bis** | **OUI** |
| n° 95-101 (27 nov. 1995) | art. 111 (prescription, capital décès) | non |
| n° 96-65 (22 juill. 1996) | art. 53 dernier al., 54, 55 al. 3 (âges) | non |
| n° 97-4 (3 févr. 1997) | art. 41 (cotisations) | non |
| n° 97-58 (28 juill. 1997) | art. 91 al. 3 (soins) | non |
| n° 98-91 (2 nov. 1998) | art. 88 (assiette des indemnités en espèces) | non |
| n° 2007-51 (23 juill. 2007) | art. 105, art. 45 (pénalités, périodicité) | non |

**L'article 61 n'a plus été touché depuis 1988** : résultat négatif désormais établi sur la chaîne
complète, et non sur les seuls textes postérieurs.

**R3 — Le champ d'application personnel est le fait le plus discriminant du système.** Les
prestations familiales ne sont ouvertes qu'à **deux** régimes CNSS sur sept (RSNA et RSAA) ; le
secteur public a un dispositif **distinct, servi par l'employeur**, pas par la CNRPS. Voir la
matrice au §9.

**R4 — La « majoration pour salaire unique » du secteur privé a un texte, et ce n'est aucun de ceux
que le dépouillement par titres suggérait.** Elle est créée par la **loi n° 80-36 du 28 mai 1980**
(JORT n° 32 des 27-30 mai 1980, p. 1478), dont l'article premier ajoute au chapitre premier du
titre II de la loi n° 60-30 une **« SECTION I bis — Majoration pour Salaire Unique »** et un
**article 65 bis** ; l'article 2 en fixe l'effet au **1er mai 1980**. Le titre de cette loi ne
porte que « *complétant la loi n° 60-30* » : aucune recherche par intitulé ne pouvait la trouver.
La **loi n° 96-101, art. 7** (lue à l'image) confirme qu'elle est toujours en vigueur en 1996.
Symétriquement, le **décret n° 74-463** — seul titre du corpus à porter l'expression — ne la
contient **pas dans son dispositif** : son article premier accorde aux militaires « *les
indemnités à caractère familial dans les mêmes conditions que les fonctionnaires de l'État* ». Le
vocable du titre de 1974 est donc un **surnom de sommaire**, et le dispositif réel est celui de
1980, dans le secteur privé.

**R5 — « L'indemnité pour perte d'emploi » n'existe toujours pas.** L'article 17 de la loi de
finances pour 2025 crée un **fonds**, pas une prestation, et renvoie à un décret qui n'était pas
paru au 8 septembre 2026 (§7). Le seul dispositif effectif antérieur est la loi n° 96-101, qui ne
verse **aucun revenu de remplacement** : elle fait avancer par la CNSS les indemnités de
licenciement impayées et **proroge de quatre trimestres** les droits familiaux et les soins.

---

## 1. Textes fondateurs — identification, dates, URL

Toutes les URL ci-dessous ont été vérifiées (HTTP 200, `application/pdf`).

| Texte | Signature | Publication JORT | Pages | Effet énoncé | Niv. |
|---|---|---|---|---|---|
| Loi n° 60-30, organisation des régimes de sécurité sociale | 1960-12-14 | n° 57, 13-16 déc. 1960 | 1602-1613 | **non établi** (article final non lu) | [T] arts 50-91 |
| Loi n° 60-33, pensions secteur non agricole | 1960-12-14 | n° 57 de 1960 | 1616 | non établi | [M] |
| Loi n° 72-2, réforme du régime de prévoyance sociale des fonctionnaires | 1972-02-15 | n° 7, 11 févr. 1972 | 189 | non établi | [M] |
| Loi n° 74-41, attribution du service du capital-décès à la Caisse nationale des retraites | 1974-05-22 | n° 36, 24 mai 1974 | 1101 | non établi | [M] |
| Décret n° 74-572, capital-décès | 1974-05-22 | n° 36 de 1974 | 1108-1109 | abrogé par le décret n° 93-308 art. 14 | [M] + [T] via 93-308 |
| Décret n° 74-499, pensions RSNA | 1974-04-27 | n° 30, 30 avril 1974 | 915-919 | non établi | [M] |
| **Loi n° 75-82**, modifiant la loi n° 60-30 (art. 61 al. 2) | 1975-12-30 | n° 87, 30-31 déc. 1975 | 2852 | **1er janvier 1976** (art. 2) | [T] |
| **Loi n° 80-36**, complétant la loi n° 60-30 (section I bis, art. 65 bis — majoration pour salaire unique) | 1980-05-28 | n° 32, 27-30 mai 1980 | 1478 | **1er mai 1980** (art. 2) | [T] |
| Loi n° 81-6, régimes de sécurité sociale du secteur agricole | 1981-02-12 | n° 9, 13 févr. 1981 | 265-273 | non établi | [T] art. 1-4 |
| **Loi n° 86-75**, modifiant la loi n° 60-30 (art. 61 al. 2) | 1986-07-28 | n° 43, 1er-5 août 1986 | 843 | **1er mai 1986** (art. 2) | [T] |
| Loi n° 86-86, réforme des structures de la sécurité sociale (CNSS / CNRPS) | 1986-09-01 | n° 49, 9 sept. 1986 | 977-980 | non établi | [M] |
| Loi n° 88-38, modifiant la loi n° 60-30 (allocations familiales) | 1988-05-06 | n° 33, 13-17 mai 1988 | 735 | **1er janvier 1989** (art. 5) | [T] |
| Loi n° 88-39, indemnités familiales dans le secteur public | 1988-05-06 | n° 33 de 1988 | 735 | **non établi** ; « ne s'applique pas aux droits acquis antérieurement au 1er janvier 1989 » | [T] |
| Décret n° 89-107, extension aux travailleurs tunisiens à l'étranger | 1989-01-10 | n° 4, 17 janv. 1989 | 98-99 | non établi | [T] arts 1-10 |
| Loi n° 89-73, complétant la loi n° 81-6 (titre III — régime agricole amélioré) | 1989-09-02 | n° 60, 5-8 sept. 1989 | 1338-1339 | **1er octobre 1989** (art. 4) | [T] |
| Décret n° 93-308, régime du capital-décès (secteur public) | 1993-02-01 | n° 13, 16 févr. 1993 | 246-247 | **1er juillet 1993** (art. 15) | [T] |
| Loi n° 94-28, réparation des accidents du travail et maladies professionnelles | 1994-02-21 | n° 15, 22 févr. 1994 | 308-318 | **1er janvier 1995** (art. 107), abroge la loi n° 57-73 | [T] |
| **Loi n° 94-88**, contribution aux frais de prise en charge des enfants dans les crèches | 1994-07-26 | n° 60, 2 août 1994 | 1255 | non établi | [T] |
| **Décret n° 95-114**, montant de la contribution aux frais de crèche | 1995-01-16 | n° 8, 27 janv. 1995 | 264 | **1er octobre 1994** (art. 4) | [T] |
| Loi n° 95-56, régime particulier AT/MP dans le secteur public | 1995-06-28 | n° 53, 4 juill. 1995 | 1419-1424 | **1er janvier 1996** (art. 58) | [T] |
| Décret n° 95-1166, sécurité sociale des travailleurs non salariés | 1995-07-03 | n° 55, 11 juill. 1995 | 1486-1489 | non établi | [T] arts 1-33 |
| Loi n° 96-65, modifiant la loi n° 60-30 (âges des enfants) | 1996-07-22 | n° 60, 26 juill. 1996 | 1603 | non établi | [T] |
| Loi n° 96-101, protection sociale des travailleurs | 1996-11-18 | n° 94, 22 nov. 1996 | 2319-2320 | non établi | [T] |
| Décret n° 96-1906, taux des indemnités à caractère familial | 1996-10-16 | n° 85, 22 oct. 1996 | 2097 | **1er novembre 1996** (art. 5) | [T] |
| Loi n° 97-58, modifiant la loi n° 60-30 (art. 91 al. 3, soins) | 1997-07-28 | n° 61, 1er août 1997 | 1359 | **1er mai 1997** (art. 2) | [T] |
| Loi n° 98-91, modifiant la loi n° 60-30 (art. 88, assiette) | 1998-11-02 | n° 89, 6 nov. 1998 | 2184 | **1er mai 1998** (art. 2) | [T] |
| Loi n° 2002-32, régime de certaines catégories de travailleurs | 2002-03-12 | n° 22, 15 mars 2002 | 603-606 | non établi | [T] miroir |
| Loi n° 2002-104, artistes, créateurs et intellectuels | 2002-12-30 | n° 106, 31 déc. 2002 | 3187-3190 | non établi | [T] miroir |
| Loi n° 2004-71, institution d'un régime d'assurance maladie | 2004-08-02 | n° 63, 6 août 2004 | 2228-2230 | **aucune date propre** : art. 3 renvoie à un décret | [T] miroir |
| Décret n° 2007-1366, étapes d'application de la loi n° 2004-71 | 2007-06-11 | n° 47, 2007 | 1982-1983 | **1er juillet 2007** (art. 1er) | [T] miroir |
| Loi n° 2017-47, modifiant la loi n° 2004-71 (art. 16 et 16 bis) | **conflit, voir §11** | n° 50 de 2017 | 2244 | non établi | [T] miroir |
| Loi n° 2024-44, congés de maternité et de paternité | 2024-08-12 | n° 99, 12 août 2024 | 2215 | **aucun article d'entrée en vigueur** ; art. 11 abroge les dispositions contraires | [T] miroir |
| Décret-loi n° 2024-4, protection sociale des travailleuses agricoles | 2024-10-22 | n° 129, 23 oct. 2024 | voir §11 | non établi | [T] miroir |
| Loi n° 2024-48, loi de finances 2025, **art. 17** | 2024-12-09 | n° 149, 10 déc. 2024 | 6420-6421 (**éd. arabe**) | non établi ; gestion renvoyée à un décret | [T] éd. arabe |

**URL pist.tn vérifiées** (édition française sauf mention) :

```
loi 60-30, 60-33          https://www.pist.tn/jort/1960/1960F/Jo05760.pdf
loi 74-41, décret 74-572  https://www.pist.tn/jort/1974/1974F/Jo03674.pdf
décret 74-463             https://www.pist.tn/jort/1974/1974F/Jo02674.pdf
décret 74-499             https://www.pist.tn/jort/1974/1974F/Jo03074.pdf
loi 70-34                 https://www.pist.tn/jort/1970/1970F/Jo03470.pdf
loi 75-82                 https://www.pist.tn/jort/1975/1975F/Jo08775.pdf
loi 80-36                 https://www.pist.tn/jort/1980/1980F/Jo03280.pdf
loi 81-5, loi 81-6        https://www.pist.tn/jort/1981/1981F/Jo00981.pdf
loi 86-75                 https://www.pist.tn/jort/1986/1986F/Jo04386.pdf
loi 86-86                 https://www.pist.tn/jort/1986/1986F/Jo04986.pdf
lois 88-38, 88-39         https://www.pist.tn/jort/1988/1988F/Jo03388.pdf
décret 89-107             https://www.pist.tn/jort/1989/1989F/Jo00489.pdf
loi 89-73                 https://www.pist.tn/jort/1989/1989F/Jo06089.pdf
décret 93-308             https://www.pist.tn/jort/1993/1993F/Jo01393.pdf
loi 94-28                 https://www.pist.tn/jort/1994/1994F/Jo01594.pdf
loi 94-88                 https://www.pist.tn/jort/1994/1994F/Jo06094.pdf
décret 95-114             https://www.pist.tn/jort/1995/1995F/Jo00895.pdf
arrêté 21 déc. 1994       https://www.pist.tn/jort/1995/1995F/Jo00195.pdf
loi 95-56                 https://www.pist.tn/jort/1995/1995F/Jo05395.pdf
décret 95-1166            https://www.pist.tn/jort/1995/1995F/Jo05595.pdf
loi 96-65                 https://www.pist.tn/jort/1996/1996F/Jo06096.pdf
décret 96-1906            https://www.pist.tn/jort/1996/1996F/Jo08596.pdf
loi 96-101 + circ. n° 42  https://www.pist.tn/jort/1996/1996F/Jo09496.pdf
loi 97-58                 https://www.pist.tn/jort/1997/1997F/Jo06197.pdf
loi 98-91                 https://www.pist.tn/jort/1998/1998F/Jo08998.pdf
loi 2002-32               https://www.pist.tn/jort/2002/2002F/Jo0222002.pdf
loi 2002-24               https://www.pist.tn/jort/2002/2002F/Jo0182002.pdf
loi 2002-104              https://www.pist.tn/jort/2002/2002F/Jo1062002.pdf
loi 57-73                 https://www.pist.tn/jort/1957/1957F/Jo04357.pdf
loi 72-2                  https://www.pist.tn/jort/1972/1972F/Jo00772.pdf
loi 2004-71               https://www.pist.tn/jort/2004/2004F/Jo0632004.pdf
décrets 2007-1366/1367    https://www.pist.tn/jort/2007/2007F/Jo0472007.pdf
décret 2007-1406          https://www.pist.tn/jort/2007/2007F/Jo0492007.pdf
loi 2024-44               https://www.pist.tn/jort/2024/2024F/Jo0992024.pdf
décret-loi 2024-4         https://www.pist.tn/jort/2024/2024F/Jo1292024.pdf
LF 2025 (art. 17)         https://www.pist.tn/jort/2024/2024A/Ja1492024.pdf  (édition ARABE)
```

---

## 2. Les prestations familiales

### 2.1 Le secteur privé — loi n° 60-30, titre II, chapitre premier

**[T]** *Article 51* (JORT n° 57 de 1960, p. 1606, lu à l'image) : « *Les prestations familiales
prévues par la présente loi comprennent : 1° les allocations familiales ; 2° les allocations pour
congés de naissance ; 3° les allocations pour congés de jeunes travailleurs.* »

C'est la définition légale du terme. Elle est **plus large que les seules allocations familiales**,
et deux de ses trois composantes sont des **remboursements à l'employeur** :

- **[T]** *art. 66* : la Caisse nationale rembourse à l'employeur l'avance faite en exécution du
  **décret du 27 mai 1948 (19 redjeb 1367)**, qui accorde au chef de famille salarié un congé
  supplémentaire à l'occasion de chaque naissance ;
- **[T]** *art. 67* : même mécanisme pour les indemnités de congé supplémentaire des jeunes
  travailleurs du commerce, de l'industrie et des professions libérales, prévues par le **décret
  du 20 janvier 1949 (20 rabia I 1368)**.

#### Qui y a droit — allocations familiales

**[T]** *art. 52* (version 1960) : dues aux **travailleurs salariés des établissements ou
professions énumérés à l'article 34**, **à partir du premier enfant à charge**, **résidant en
Tunisie**, et **seulement pour les quatre premiers enfants**. « *Le cinquième enfant et suivants,
dans l'ordre de primogéniture ou d'adoption, n'ouvrent, en aucun cas, droit aux allocations
familiales.* » Dérogation : le droit est maintenu au travailleur salarié **tunisien** pour ses
enfants résidant à l'étranger ; il est reconnu au travailleur salarié **étranger** dont les enfants
résident à l'étranger **à condition** qu'il soit ressortissant d'un État lié à la Tunisie par une
convention de réciprocité en matière d'allocations familiales.

**[T]** *art. 52 al. 2, 3 et 4 nouveaux* (loi n° 88-38, art. 1er, effet **1989-01-01**) : le
plafond passe de quatre à **trois** enfants ; hors décès dans le groupe des trois premiers, le
quatrième enfant et les suivants ne viennent jamais en rang utile ; en cas de décès, l'enfant
substituant vient en rang utile immédiatement après le dernier bénéficiaire, sans porter le nombre
au-delà de trois.

**[T]** *art. 53* : l'allocataire est 1° le père ou la mère du chef de leurs enfants ou de ceux
nés d'un premier lit ; 2° l'adoptant ou le conjoint de l'adoptant ; 3° le tuteur officieux salarié ;
4° la personne ayant la garde de l'enfant au sens de l'article 57 du Code du statut personnel, à
condition qu'elle assure effectivement logement, nourriture et habillement.
**[T]** *art. 53 dernier alinéa nouveau* (loi n° 96-65) : à défaut d'activité propre assujettie,
la personne ayant la garde peut être attributaire si le droit est ouvert du fait de l'activité du
père ou de la mère et si l'enfant vient en rang utile auprès de ces derniers.

**Limites d'âge — [T]** *art. 54*, deux états successifs :

| | 1960 (art. 54 d'origine) | depuis la loi n° 96-65 (art. 54 nouveau) |
|---|---|---|
| Sans condition | < 14 ans | **< 16 ans** |
| Apprentissage (rémunération ≤ 75 % du SMIG, régime 48 h) | jusqu'à 18 ans | jusqu'à **18 ans** |
| Scolarité second degré / supérieur / technique / professionnel | jusqu'à 20 ans | jusqu'à **21 ans** |
| Fille remplaçant la mère décédée, impotente, divorcée ou veuve | jusqu'à 20 ans | jusqu'à **21 ans** |
| Infirmité ou maladie incurable | au-delà de 20 ans | au-delà de **21 ans**, et **titulaires d'une carte d'handicapé** non pris en charge intégralement |
| Rang | — | **les enfants handicapés ou infirmes sont servis quel que soit leur rang** |

Le maintien pendant les vacances scolaires, y compris celles qui suivent la fin de l'année, figure
dans les deux versions. La date d'effet de la loi n° 96-65 n'a **pas** été lue : **non établie**.

**Maintien du droit en cas de rupture ou de risque — [T]** :
- *art. 56* : maintenues en cas de décès du salarié dû à un accident du travail ou à une maladie
  professionnelle, tant que les enfants y ont droit ; étendu aux enfants nés dans les **300 jours**
  suivant le décès ;
- *art. 57* : maintenues pendant l'incapacité temporaire et, si l'incapacité permanente est
  **≥ 40 %**, pendant celle-ci ;
- *art. 58* : conservées au salarié couvert par le régime des assurances sociales pendant une
  interruption de travail pour maladie, dans la limite de **365 jours** ; et pendant la période
  légale de couches pour la salariée, prorogeable **jusqu'à un an** si elle a interrompu son
  activité pour élever son enfant ;
- *art. 59* : en cas de mort du salarié pour une autre cause, le droit passe à la personne qui
  recueille les enfants, sous condition d'un stage d'activité (six mois dans l'année précédant la
  cessation, ou huit mois en moyenne sur les dix années antérieures) ;
- **[T]** loi n° 82-71 du 15 août 1982 (JORT n° 55 de 1982, p. 1737) : ajoute à la loi n° 60-30 une
  disposition sur le maintien des prestations familiales des travailleurs dont la situation est
  constatée par la **commission de contrôle des licenciements** — précurseur direct de l'article 7
  de la loi n° 96-101. *Dispositif lu partiellement (OCR), à relire à l'image.*

#### Montant

**[T]** *art. 61 al. 2, version 1960* : « *le taux de l'allocation afférente à chaque enfant est
fixé à 15 % de cette rémunération* » ; « *les parties des salaires […] égales ou inférieures à
52 D, ou supérieures à 500 D par trimestre, n'entrent pas en compte pour le calcul des allocations
familiales afférentes au trimestre considéré* ». **[T]** *art. 63* : le montant des allocations
servies aux orphelins (art. 62) ne peut être inférieur à **50 %** du maximum de l'allocation de
l'art. 61 lorsque les bénéficiaires sont les enfants de travailleurs décédés ou victimes
d'accidents du travail ou de maladies professionnelles atteints d'une incapacité permanente **≥
40 %**.

**[T]** *art. 61 al. 2 nouveau*, **loi n° 75-82 du 30 décembre 1975** (JORT n° 87 des 30-31
décembre 1975, p. 2852), lu à l'image :

> « *Le montant trimestriel de l'allocation est calculé en pourcentage de la rémunération globale
> trimestrielle du travailleur **plafonnée à 72 D, 000** soit : **18 %** pour le premier enfant ;
> **16 %** pour le deuxième enfant ; **14 %** pour le troisième enfant ; **12 %** pour le quatrième
> enfant.* » — *Art. 2* : « *La présente loi prendra effet à compter du **1er janvier 1976**.* »

**[T]** *art. 61 al. 2 nouveau*, **loi n° 86-75 du 28 juillet 1986** (JORT n° 43 des 1er-5 août
1986, p. 843), lu à l'image : rédaction **identique**, à ceci près que le plafond passe à
**122,000 dinars** ; les quatre taux 18 / 16 / 14 / 12 % sont inchangés. *Art. 2* : « *La présente
loi prend effet à partir du **1er mai 1986**.* »

**[T]** *art. 61 al. 2 nouveau*, **loi n° 88-38 du 6 mai 1988** (effet **1er janvier 1989**), lu à
l'image :

> « Le montant trimestriel de l'allocation est calculé en pourcentage de la rémunération globale
> trimestrielle du travailleur **plafonnée à 122,000** soit : — **18 %** pour le premier enfant ;
> — **16 %** pour le deuxième enfant ; — **14 %** pour le troisième enfant. »

Le **quatrième rang à 12 %**, ouvert du 1er janvier 1976 au 31 décembre 1988, **disparaît** — c'est
le seul apport de la loi n° 88-38 sur les montants, cohérent avec la limitation aux trois premiers
enfants qu'elle opère au même article premier.

**[T]** *art. 65* : les allocations sont versées par la Caisse nationale **au moins une fois par
trimestre**, dans les 45 jours suivant le terme de la période.

**Correction à porter à openfisca-tunisia.** `prestations/contributives/prestations_familiales/af/`
porte 0,18 / 0,16 / 0,14 et un plafond trimestriel de 122 D **datés `1960-01-01`**, tout en citant
la loi n° 88-38 en `reference`. **Aucune de ces trois choses n'est correcte.** La série complète,
entièrement attestée à l'image :

```yaml
# af/taux/enf1.yaml, enf2.yaml, enf3.yaml
1960-01-01: 0.15   # loi n° 60-30, art. 61 — taux unique pour tout enfant en rang utile
1976-01-01: 0.18 / 0.16 / 0.14   # loi n° 75-82, art. 2
# af/taux/enf4.yaml — paramètre à CRÉER
1976-01-01: 0.12   # loi n° 75-82
1989-01-01: 0      # loi n° 88-38 : le 4e rang cesse d'ouvrir droit
# af/plaf_trim.yaml
1960-01-01: 500    # loi n° 60-30, art. 61 — plafond de la bande
1976-01-01: 72     # loi n° 75-82, art. 2
1986-05-01: 122    # loi n° 86-75, art. 2
# af/plancher_trim.yaml — paramètre à CRÉER
1960-01-01: 52     # loi n° 60-30, art. 61
1976-01-01: 0      # supprimé par la loi n° 75-82 (plafond unique)
# af/nb_enfants_max — paramètre à CRÉER
1960-01-01: 4      # loi n° 60-30, art. 52
1989-01-01: 3      # loi n° 88-38, art. 1er
```

Rappel : les clés `href` des paramètres pointent sur un dépôt GitLab tiers ; les citations
canoniques sont les URL pist.tn listées au §1.

#### Majoration pour salaire unique — loi n° 80-36, article 65 bis

**[T]**, lu à l'image (JORT n° 32 des 27-30 mai 1980, p. 1478). *Article premier* : « *Il est
ajouté au chapitre 1er du titre II de la loi n° 60-30 […] une **section I bis** dont la teneur
suit : **SECTION I bis — Majoration pour Salaire Unique**.* »

> « **Art. 65 bis.** — Il est attribué à l'assuré ayant des **enfants à charge au sens de
> l'article 53** précédent, **ouvrant droit au bénéfice des allocations familiales** et **dont le
> conjoint n'exerce aucune activité professionnelle**, une indemnité dite « majoration pour salaire
> unique » dont le montant trimestriel est de :
> — **9 d,375** si le foyer comporte un enfant à charge ;
> — **18 d,750** si le foyer comporte 2 enfants à charge ;
> — **23 d,475** si le foyer comporte 3 enfants ou plus à charge. »

Trois conditions cumulatives, donc : enfants à charge au sens de l'article 53, **droit ouvert aux
allocations familiales**, et **conjoint sans activité professionnelle** — c'est cette dernière qui
donne son nom au dispositif.

La majoration est « *liquidée dans les mêmes conditions et dans les mêmes délais que l'allocation
familiale* » et « *versée à la personne qui a la garde des enfants* ». La CNSS « *se substitue aux
employeurs affiliés qui assurent à leurs salariés, à la date de la promulgation de la présente loi,
le service d'une indemnité de même nature dans la limite des taux susmentionnés* » ; « *seule reste
à la charge de l'employeur la différence éventuelle entre le taux de la majoration légale et celui
de la majoration contractuelle* » — le dispositif **légalise et plafonne une pratique
conventionnelle préexistante**, trait à relever. *Art. 2* : « *La présente loi prend effet à
compter du **1er mai 1980**.* »

**Correction à porter à openfisca-tunisia.** `prestations_familiales/salaire_unique/` porte
**9,375 / 18,75 / 23,475 D** datés `1960-01-01` et **sans aucune `reference`**. Les valeurs sont
**exactement celles de l'article 65 bis** : elles doivent être datées **`1980-05-01`** et référencées
sur la loi n° 80-36. **Aucun texte postérieur revalorisant ces montants n'a été trouvé** ; ils
seraient donc nominalement inchangés depuis 1980, ce qui est un fait à vérifier avant publication
plutôt qu'à énoncer (voir §10, L2).

#### Contribution aux frais de crèche — loi n° 94-88 et décret n° 95-114

Ce dispositif **n'est pas dans la loi n° 60-30** : c'est un texte autonome de 1994.

**[T]** **Loi n° 94-88 du 26 juillet 1994** (JORT n° 60 du 2 août 1994, p. 1255), lue à l'image.
*Art. 1er* : contribution aux frais de prise en charge des enfants dans les **crèches autorisées
par le ministère de tutelle**, conformément à un cahier des charges adopté par décret ; montant,
modalités et conditions de recouvrement fixés par décret. *Art. 2* : servie au titre des enfants
**des assurées sociales et des affiliées aux caisses de sécurité sociale** dont le salaire mensuel,
indemnités comprises, ne dépasse pas un montant fixé par décret ; « *les dispositions de l'alinéa
précédent ne s'appliquent qu'au titre des enfants admis au régime des allocations familiales* ».
*Art. 3* : à la charge des caisses de sécurité sociale. *Art. 4* : servie **directement à la
crèche**, pour les enfants dont l'âge est compris **entre deux et trente-six mois**, et pour une
période de **onze mois par année** ; **non servie pendant le congé de maternité**.

**[T]** **Décret n° 95-114 du 16 janvier 1995** (JORT n° 8 du 27 janvier 1995, p. 264), lu à
l'image. *Art. 1er* : montant fixé à **quinze dinars par enfant et par mois**, durant onze mois par
an ; servie au titre des enfants des **assurées sociales actives** dont le revenu mensuel, y compris
les indemnités, **ne dépasse pas deux fois et demie le salaire minimum garanti** ; attribuée par la
caisse **sur demande présentée par la mère bénéficiaire**. *Art. 2* : attestation de présence
déposée par la crèche tous les trois mois, visée par le commissaire régional à la jeunesse et à
l'enfance. *Art. 3* : servie **trimestriellement et directement à la crèche**, dans un délai d'un
mois à compter du dépôt de l'attestation. *Art. 4* : « *Le montant de la contribution visé à
l'article premier du présent décret est servi **à compter du 1er octobre 1994**.* »

**Le dispositif est donc réservé aux mères** : la loi vise « les assurées sociales » et « les
affiliées », le décret « la mère bénéficiaire ». C'est le seul dispositif du bloc contributif dont
le champ est explicitement genré, et cela mérite d'être relevé.

**Correction à porter à openfisca-tunisia.** `prestations_familiales/creche/` porte `montant: 15`,
`plaf: 2.5`, `duree: 11`, `age_min: 2`, `age_max: 36`, **tous datés `1960-01-01` et sans aucune
`reference`**. Les cinq valeurs correspondent **exactement** au décret n° 95-114 et à l'article 4
de la loi n° 94-88 — `plaf` étant un multiple du SMIG et `age_min`/`age_max`/`duree` des **mois**.
Elles doivent être datées **`1994-10-01`** et référencées sur ces deux textes.

### 2.2 Le secteur public — les indemnités à caractère familial

Dispositif **entièrement distinct**, à ne pas confondre avec les allocations familiales.

**[T]** **Loi n° 88-39 du 6 mai 1988** (JORT n° 33 de 1988, p. 735), *article unique*, lu à
l'image :

> « L'indemnité familiale est servie aux agents de l'État, des collectivités publiques locales, des
> établissements publics, des offices et des sociétés nationales **autres que ceux soumis au régime
> de sécurité sociale institué par la loi n° 60-30**, dans les conditions et selon les modalités
> prévues par le **décret du 22 novembre 1918** tel qu'amendé ou modifié par les textes subséquents,
> et **dans la limite des trois premiers enfants**. Le montant des indemnités est fixé par décret.
> Les dispositions de la présente loi ne s'appliquent pas aux droits acquis antérieurement au
> 1er janvier 1989. »

Trois traits à retenir : le **critère d'exclusion réciproque** avec la loi n° 60-30 (on relève
de l'un **ou** de l'autre) ; le renvoi à un texte **de 1918**, toujours opérant en 1988 ; le
montant fixé **par décret**, donc en dinars, et non en pourcentage d'un salaire.

**Payeur : l'employeur public, pas la CNRPS.** « *L'indemnité familiale est **servie aux agents*** »
et le décret n° 96-1906 vise « *les indemnités familiales **dues aux fonctionnaires et agents**
de l'État, des collectivités publiques locales et des établissements publics à caractère
administratif* ». Aucune mention de la CNRPS dans l'un ni dans l'autre. C'est une **indemnité de
rémunération**, budgétairement portée par l'employeur, non une prestation de sécurité sociale —
d'où le renvoi, dans la matrice du §9, à un statut de nature différente et non à une simple coche.
*Confirmation attendue : la circulaire n° 42 du 25 octobre 1996 « ayant pour objet la gestion des
indemnités à caractère familial dans le secteur public », JORT n° 94 de 1996, pp. 2349-2364,
16 pages — repérée [M], non encore lue.*

**Chaîne des taux** (tous [M] sauf mention) :

| Texte | Signature | JORT | Page |
|---|---|---|---|
| Décret n° 75-952, fixation du taux des indemnités à caractère familial | 1975-12-30 | n° 87 de 1975 | 2884 |
| Décret n° 86-611, fixation des taux | 1986-06-03 | n° 34 de 1986 | 674 |
| Décret n° 88-1136, fixation des taux | 1988-06-11 | n° 43 de 1988 | 941 |
| **Décret n° 96-1906, fixation des taux** | 1996-10-16 | n° 85 de 1996 | 2097 **[T]** |
| Circulaire n° 42, gestion des indemnités dans le secteur public | 1996-10-25 | n° 94 de 1996 | 2349-2364 |

**[T]** **Décret n° 96-1906**, lu à l'image (JORT n° 85 de 1996, p. 2097). *Article premier* — taux
**mensuel par enfant à charge** :

| Rang | Montant mensuel |
|---|---|
| premier enfant | **7,320 D** |
| deuxième enfant | **6,507 D** |
| troisième enfant | **5,693 D** |
| *art. 2* — quatrième enfant ayant acquis le droit antérieurement au 1er janvier 1989 (loi n° 88-39) | **4,880 D** |
| *art. 3* — enfant handicapé venant après le 3e rang parmi ses frères et sœurs | **4,880 D** |

*Art. 4* : abroge les décrets n° 86-611 et n° 88-1136. *Art. 5* : **prend effet à compter du
1er novembre 1996**.

**[T]** **Décret n° 74-463 du 11 avril 1974** (JORT n° 26 de 1974, p. 757), lu à l'image. Titre :
« *portant octroi de l'indemnité dite majoration pour salaire unique à certaines catégories des
personnels militaires* ». *Article premier* : les officiers, sous-officiers d'active et hommes de
troupe servant sous contrat après la durée légale « *bénéficient, en plus de la solde, des
**indemnités à caractère familial** dans les mêmes conditions que les fonctionnaires de l'État et
sous réserve qu'ils aient obtenu l'autorisation ou la reconnaissance de mariages réglementaires* ».
*Art. 3* : **prend effet à compter du 1er janvier 1974**. Le dispositif ne contient donc pas
l'expression du titre.

---

## 3. Les indemnités de maladie et de maternité

### 3.1 Le socle : loi n° 60-30, titre II, chapitre II « Les assurances sociales »

**[T]** *art. 68* : les assurances sociales comprennent **1°** des indemnités en espèces en cas de
**maladie, de maternité ou de décès**, servies par la Caisse nationale ; **2°** l'octroi des soins
en cas de consultations ou d'hospitalisation dans les établissements relevant du secrétariat d'État
à la Santé publique.

**[T]** *art. 69* : « *Bénéficient de ces régimes les travailleurs salariés visés à l'article 34
ci-dessus, ainsi que leur famille, dans les conditions définies au présent chapitre, et **sous
réserve de résider en Tunisie***. »

#### Indemnité de maladie

**[T]** *art. 71* — quatre conditions cumulatives : 1° incapacité dûment constatée par le contrôle
technique ; 2° **immatriculation au titre des assurances sociales depuis au moins six mois** ;
3° **au moins 90 jours de travail** pendant les deux trimestres civils précédant celui du début de
l'incapacité ; 4° maladie, blessure ou accident non provoqués intentionnellement.

**[T]** *art. 72* : l'indemnité est due pour chaque jour, ouvrable ou non, compris dans la période
**débutant le 21e jour d'incapacité** et **se terminant le 180e**, sans que le nombre de jours
indemnisés puisse dépasser **300 au cours de 24 mois consécutifs**. Le délai de carence est
**ramené à 3 jours** pour les maladies de longue durée dont la liste est fixée par arrêté. Non
cumulable avec l'indemnité AT/MP ni avec le maintien d'une rémunération légale, conventionnelle ou
réglementaire, sauf différence servie par la Caisse. Aucun stage n'est exigé en cas d'incapacité
due à une blessure ou à un accident, si la victime était assujettie à la date du fait.

**[T]** *art. 77* : indemnité journalière = **50 % du salaire journalier moyen** (art. 88 à 90),
due à terme échu, payable **deux fois par mois**.

#### Indemnité de couches

**[T]** *art. 78* : la **femme salariée** suspendant son travail à cause de son état de grossesse
ou de son accouchement, sous deux conditions : 1° **immatriculée depuis au moins un an** à la date
de l'accouchement ; 2° **au moins 150 jours de travail** pendant les quatre trimestres civils
précédant le trimestre de l'accouchement.
**[T]** *art. 79* : durée = la **période légale de couches** telle que déterminée par le **décret du
6 avril 1950 (18 djoumada II 1369)**.
**[T]** *art. 82* : **50 % du salaire journalier moyen**, à terme échu, **payable mensuellement**.

#### Assiette commune

**[T]** *art. 88* : salaire journalier calculé sur les salaires du **trimestre au cours duquel s'est
produite l'incapacité ou le décès** (maladie, décès), ou du **trimestre précédant le début du congé
de couches** ; plafonnés dans les mêmes conditions que l'article 27 de la loi n° 57-73.
**[T]** *art. 89* : salaire journalier moyen = **1/92e** du total des salaires de l'article 88.
**[T]** *art. 90* : si l'assuré a bénéficié d'une indemnité pendant le trimestre de référence, son
montant est ajouté au total des salaires.

**[T]** *art. 88 nouveau* (**loi n° 98-91**, effet **1er mai 1998**, lu à l'image) : le salaire
journalier moyen est déterminé sur le **trimestre choisi parmi les quatre trimestres précédant**
l'incapacité, la maternité ou le décès, **au cours duquel l'assuré a perçu les salaires les plus
élevés** ; ces salaires ne sont pris en considération, pour un trimestre déterminé, que **dans la
limite de deux fois le SMIG régime 48 heures rapporté à une durée d'occupation de 600 heures**. Le
plafond est révisable par décret.

### 3.2 Les congés de maternité et de paternité — loi n° 2024-44

**[T]** (miroir iort.tn, texte français intégral). *Article premier* : la loi s'applique à **tous
les agents de la fonction publique et du secteur public affiliés à la CNRPS** et aux **salariés
**et non-salariés** du secteur privé affiliés et déclarés à la CNSS**. C'est le premier texte du
corpus à couvrir en un seul mouvement les deux caisses et les non-salariés.

| Congé | Durée | Public / secteur public | Secteur privé |
|---|---|---|---|
| Prénatal (art. 3) | max. **15 jours** au cours du dernier mois | plein traitement | indemnité |
| Postnatal (art. 4) | **3 mois** ; **4 mois** si naissances gémellaires ou multiples, handicap, prématurité, malformations ; **1 mois** si enfant mort-né | plein traitement | indemnité |
| Paternité (art. 5) | **7 jours** ; **10 jours** dans les mêmes cas aggravés ; **3 jours** si enfant mort-né ; à prendre dans les **30 jours** | plein traitement | plein traitement |
| Accouchement (art. 6) | **1 à 4 mois** sur demande, après accord | **demi-traitement** | indemnité |
| Repos d'allaitement (art. 8) | 1 h par séance ≥ 4 h ; 2 × 1 h si travail en deux séances ≥ 7 h/jour | — | — |
| Congé d'allaitement (art. 8) | **9 mois** à compter de la reprise, ou jusqu'à l'échéance d'un an depuis l'accouchement si congé d'accouchement pris | — | — |

*Art. 7* : pendant les congés, l'agent est réputé **en activité** et conserve ses droits à
l'avancement, à la promotion et à la retraite. *Art. 9* : les indemnités du secteur privé sont
calculées « **conformément à la législation en vigueur** » — c'est-à-dire l'article 82 de la loi
n° 60-30 (50 % du salaire journalier moyen), la loi **ne fixe aucun taux propre**. *Art. 10* :
interdiction de sanction ou de licenciement pour un motif lié à la grossesse, l'accouchement ou
l'allaitement.

**Point d'attention.** La loi n° 2024-44 **ne renvoie à aucun décret d'application** et ne comporte
**aucun article d'entrée en vigueur** : elle est donc immédiatement opérante par sa publication,
mais l'articulation entre les nouvelles **durées** (art. 4 : trois mois) et le **stage** de
l'article 78 de la loi n° 60-30 (un an d'immatriculation, 150 jours de travail) n'est réglée par
aucun des deux textes. **Question non tranchée** — lacune L3.

---

## 4. Le capital décès et les droits des survivants

Deux dispositifs de **noms proches et de natures différentes**, à ne surtout pas fusionner.

### 4.1 Secteur privé — l'« indemnité de décès » de la loi n° 60-30

**[T]** *art. 83* : accordée **à l'assuré**, en cas de décès **de son conjoint ou de ses enfants
non assurés à sa charge**. Conditions : 1° immatriculation au titre des assurances sociales depuis
**au moins six mois** au moment du décès ; 2° **au moins 90 jours de travail** pendant les deux
trimestres civils précédant, **ou** bénéfice de l'indemnité de maladie ou de couches au moment du
décès. Les ayants droit de l'assuré prédécédé en bénéficient aux mêmes conditions.
**[T]** *art. 85* : **non due si le décès est provoqué par un accident du travail ou une maladie
professionnelle** — la réparation relève alors de la loi n° 94-28.
**[T]** *art. 86* : montant = **indemnité journalière de maladie multipliée par** :

| Défunt | Multiplicateur |
|---|---|
| le travailleur | **120** |
| le conjoint, ou un enfant de plus de 16 ans | **60** |
| un enfant de plus de 6 ans et n'ayant pas dépassé 16 ans | **30** |
| un enfant de plus de 2 ans et n'ayant pas dépassé 6 ans | **20** |
| un enfant n'ayant pas dépassé 2 ans, ou enfant mort-né | **10** |

**[T]** *art. 87* : payée dans les 15 jours suivant la production des attestations ; ordre de
priorité des ayants droit — 1° si le décès frappe le travailleur ou le conjoint non assuré : le
conjoint survivant, puis les enfants ; 2° si le décès frappe un enfant : le travailleur, son
conjoint, les autres enfants.

**[T]** loi n° 95-101 du 27 novembre 1995 (JORT n° 96 de 1995, pp. 2223-2224) : ajoute un
deuxième alinéa à l'article 111 de la loi n° 60-30 — pour l'**indemnité dite « capital décès »** et
les pensions, le délai de prescription est porté à **cinq ans**. *Lecture partielle (OCR) ; à
relire à l'image pour la date d'effet.*

### 4.2 Secteur public — le capital-décès, décret n° 93-308

Lignée : arrêté du 17 juillet 1951 (modifié 1956, 1963, 1964) → décret n° 73-90 du 8 mars 1973
(extension aux personnels militaires du régime du décret du 12 avril 1951) → **loi n° 74-41 du
22 mai 1974** (attribution du service à la Caisse nationale des retraites) et **décret n° 74-572 du
22 mai 1974** → **décret n° 93-308 du 1er février 1993**, qui abroge le décret n° 74-572 (art. 14).
Comme les indemnités familiales du §2.2, le dispositif descend d'un **texte colonial** encore
opérant jusqu'à sa réécriture des années 1990.

**[T]** décret n° 93-308, lu à l'image (JORT n° 13 de 1993, pp. 246-247).

*Champ (art. 1er)* — quatre catégories : 1° agents de l'État, des collectivités publiques locales
et des établissements publics à caractère administratif ; 2° membres du gouvernement, députés et
gouverneurs, pendant l'exercice de leurs fonctions et jusqu'à la cessation du paiement de leurs
émoluments ; 3° agents des **EPIC et sociétés nationales** dont la liste est fixée par le décret
n° 85-1025 du 29 août 1985 ; 4° **personnels retraités** titulaires d'une pension servie par la
CNRPS, **à l'exclusion** des titulaires d'une pension au titre d'un régime subventionné.

*Cotisation (art. 2)* : **1 %** de la rémunération globale soumise à retenue pour pension (actifs) ;
**0,50 %** du produit brut de la pension (retraités).

*Ayants droit (art. 3)* : 1° le **conjoint non divorcé** de l'affilié décédé ; 2° les **enfants à
charge** au moment du décès — tous les enfants auxquels l'affilié assurait de manière permanente et
effective logement, nourriture et habillement, **jusqu'à 16 ans**, âge reculé jusqu'à la majorité
pour ceux qui fréquentent un établissement d'enseignement public ou privé reconnu sans occuper
d'emploi rémunéré, **sans limite d'âge** en cas d'infirmité ou de maladie incurable ; 3° les
**ascendants à charge**, âgés d'au moins **55 ans**, non couverts par un régime de sécurité sociale,
sans revenu permanent ou avec un revenu non imposable, la condition d'âge tombant pour les
ascendants infirmes ou gravement malades.

*Positions ouvrant droit (art. 4)* : activité ou maintien en activité au-delà de l'âge légal,
détachement, disponibilité **hors** disponibilité pour convenances personnelles, sous les drapeaux
(sauf décès en service comportant concession d'une pension militaire), suspension par mesure
disciplinaire, congé sans solde.

*Montant (art. 5)* : **rémunération annuelle servant de base à la liquidation de la pension de
retraite**, **majorée de 1/12 par année de service effectif** dans la limite de **18 mois de
salaires** (une période de service > 6 mois compte pour un an, < 6 mois n'est pas prise en compte),
puis **majorée de 10 % par enfant à charge**, et **doublée** si le décès est survenu
accidentellement à l'occasion de l'exercice des fonctions ou dans un accident de la circulation.

*Retraités (art. 6)* : **50 %** de la rémunération annuelle ayant servi de base à la liquidation de
la pension, majorée selon l'article 5, taux **réduit à 40 % après 70 ans, 30 % après 75, 20 % après
80, 10 % après 85** ; **jamais inférieur au SMIG annuel**.

*Répartition (art. 7)* : **un tiers** au conjoint non divorcé, **deux tiers** aux enfants par parts
égales ; à défaut d'enfants, la totalité au conjoint ; à défaut de conjoint, la totalité aux
enfants ; à défaut des deux, par parts égales au père et à la mère à leur charge. *Art. 8* :
pluralité de conjoints non divorcés — partage par parts égales de la fraction leur revenant.
*Art. 9* : décès de deux conjoints affiliés — un capital-décès **au titre de chacun**. *Art. 10* :
exclu celui ou celle qui a été condamné pour avoir donné ou tenté de donner la mort au défunt.
*Art. 11* : subrogation de la CNRPS contre le tiers responsable.

*Effet* : **1er juillet 1993** (art. 15).

---

## 5. Les accidents du travail et les maladies professionnelles

### 5.1 Secteur privé — loi n° 94-28

**[T]**, lue à l'image (JORT n° 15 de 1994, pp. 308-318). Elle **abroge la loi n° 57-73 du
11 décembre 1957** à compter du **1er janvier 1995** (art. 107).

*Art. 2* : gestion confiée à la **CNSS**. *Effet ultérieur* : **[T]** l'article 8 de la loi
n° 2004-71 transfère à la **CNAM** « *la gestion des régimes légaux de réparation des dommages
résultant des accidents du travail et des maladies professionnelles dans les secteurs public et
privé* ». La compétence gestionnaire change donc en 2007, sans que la loi n° 94-28 soit modifiée.

*Art. 3 — définitions* : accident survenu **par le fait ou à l'occasion du travail**, quelle qu'en
soit la cause ou le lieu ; **accident de trajet** entre lieu de travail et lieu de résidence, pourvu
que le parcours n'ait pas été interrompu ou détourné pour un motif personnel ; **maladie
professionnelle** = toute manifestation morbide, infection microbienne ou affection **imputable par
présomption** à l'activité professionnelle, la liste et les travaux susceptibles d'en être à
l'origine étant fixés par arrêté conjoint Santé publique / Affaires sociales, **révisé au moins
tous les trois ans**, et fixant le **délai de prise en charge** après cessation de l'exposition.

*Art. 4 — champ d'application personnel*, le plus large du corpus. « *La présente loi est
applicable à **tous les travailleurs ou assimilés employés par des personnes physiques ou morales
sous quelque forme que ce soit et quelle que soit la nature de l'activité, le statut du travailleur
ou son mode de rémunération***. » Sont **nommément** ajoutés : **stagiaires**, **apprentis**,
**élèves des établissements d'enseignement technique ou professionnel** si l'accident est
directement rattaché aux programmes, **détenus** pour les travaux exécutés dans le cadre d'une
utilisation régulière de la main-d'œuvre pénitentiaire, **travailleurs des chantiers nationaux ou
régionaux de développement**, **gens de maison**. Étendue aux personnes envoyées **en mission ou en
stage à l'étranger**, sauf motif étranger à la mission et sauf couverture au moins aussi favorable
dans le pays d'accueil.
**Exclusions** : « *La présente loi n'est pas applicable **aux agents de l'État, des collectivités
locales et des établissements publics couverts par un régime particulier**, ni **aux entreprises
familiales n'employant que leurs propriétaires et des membres de leurs familles**, sauf si elles
optent pour le bénéfice de ses dispositions.* »

*Art. 5* : le régime est **exclusif** de toute autre action contre l'employeur, sauf faute pénale ;
il ne fait pas obstacle à des indemnités statutaires ou conventionnelles plus élevées, ni à une
réparation complémentaire contre le **tiers responsable** ; subrogation de la Caisse.

*Prestations* :
- **soins** — art. 33-34, servis dès l'information de la Caisse ;
- **incapacité temporaire** — art. 35 : indemnité journalière égale aux **deux tiers de la
  rémunération quotidienne habituelle**, quelle que soit la durée, sans distinction de jours
  ouvrables, de repos ou fériés ; la **journée de l'accident est intégralement à la charge de
  l'employeur** ; **carence de 3 jours**, sauf hospitalisation ou caractère sérieux prouvé ; les
  absences pour soins sans interruption du travail sont indemnisées aux deux tiers ; assiette =
  **trimestre choisi parmi les quatre précédant l'accident au cours duquel les salaires ont été les
  plus élevés**, toutes indemnités comprises hors remboursements de frais ; recalculée en cas
  d'avancement ou de relèvement de la catégorie ; plancher de l'art. 53. Art. 36 : payable **par
  quinzaine** ;
- **incapacité permanente** — art. 39 et s. : **rente** ; conversion en capital sous 15 %
  d'incapacité ; majoration en cas de recours à une tierce personne ;
- **décès** — art. 44 : **indemnité de frais funéraires** égale à un mois de salaire, jamais
  inférieure au **SMIG correspondant à 200 heures**. Art. 45 : bénéficient de la **rente de décès**
  le conjoint et les enfants et, à défaut, les ascendants et descendants. Art. 46 : partage par
  parts égales entre plusieurs veuves épousées conformément au Code du statut personnel ; conjoint
  divorcé titulaire d'une pension alimentaire, dans la limite de celle-ci. Art. 47 : condition de
  mariage au moment du décès et absence de condamnation pour abandon de famille ; suspension en cas
  de remariage, rétablissement en cas de décès du nouveau conjoint ou de dissolution. Art. 48 :
  rentes d'orphelins pour les enfants au sens de l'article 53 de la loi n° 60-30 — **16 ans** sans
  condition, **21 ans** si études secondaires/techniques/professionnelles, **25 ans** si études
  supérieures, **la fille** tant qu'elle ne dispose pas de ressources et n'est pas à la charge de
  son mari, **sans limite d'âge** en cas d'affection incurable ou d'infirmité. Art. 49 : rente du
  conjoint = **50 %** du salaire annuel du défunt sans enfants rentiers, **40 %** avec enfants.

*Dispositions transitoires* : art. 103 met fin, au 1er janvier 1995, à **tous les contrats
d'assurance** contre les risques AT/MP ; les sinistres antérieurs restent à la charge des
compagnies selon la loi n° 57-73 ; art. 104 : la CNSS **se substitue au « Fonds des accidents du
travail »** et en liquide l'actif et le passif ; art. 106 : les accidents survenus et les maladies
constatées avant l'entrée en vigueur relèvent de la législation en vigueur au moment du fait.

*Ressource complémentaire repérée, non lue* : **[M]** arrêté du ministre des Affaires sociales du
21 décembre 1994 « *réglementant le contenu du résumé de la loi n° 94-28* », JORT n° 1 de 1995,
pp. 7-11 — résumé officiel affichable en entreprise. Équivalent 1960 pour la loi n° 57-73 :
arrêté du 15 novembre 1960, JORT n° 53 de 1960, p. 1469.

### 5.2 Secteur public — loi n° 95-56

**[T]**, lue à l'image (JORT n° 53 de 1995, pp. 1419-1424). Effet **1er janvier 1996** (art. 58).

*Art. 2 — champ* : agents de l'État, des collectivités locales et des établissements publics à
caractère administratif **affiliés à la CNRPS**, **à l'exclusion** des **militaires** (loi n° 72-70
du 11 novembre 1972 ratifiant le décret-loi n° 72-3, pensions militaires d'invalidité) et des
**forces de sécurité intérieure** (loi n° 82-70 du 6 août 1982). Extension possible **par décret**
aux agents d'entreprises publiques soumis au statut général de la fonction publique. Couvre les
missions et stages à l'étranger aux mêmes conditions que la loi n° 94-28.

*Art. 3* : définitions de l'accident du travail, de l'accident de trajet et de la maladie
professionnelle, **rédigées dans les mêmes termes** que l'article 3 de la loi n° 94-28.

*Art. 5 — gestion partagée, trait propre au régime public* :
> « La gestion du régime de réparation prévu par la présente loi est confiée à : — **l'employeur**,
> en ce qui concerne le **maintien du salaire** et la prestation des **secours et des soins** ; — la
> **caisse nationale de retraite et de prévoyance sociale**, en ce qui concerne le paiement des
> **indemnités compensatrices pour incapacité permanente** au profit des victimes ou de leurs
> ayants droit en cas de décès. Les charges découlant de ce régime sont supportées par
> l'employeur, lequel restitue les indemnités compensatrices déboursées par la [CNRPS]. »

Il n'y a donc **pas d'indemnité journalière** dans le régime public : le salaire est maintenu.
Art. 43-47 : contentieux devant le **juge cantonal**. Art. 48-49 : **carte de priorité** aux
victimes. Art. 57 : l'employeur peut confier les secours et soins à la Caisse par convention.

*Décrets d'application repérés (chaîne non vérifiée texte par texte, note de `loi95-56` dans
`precis/fr/remunerations_publiques/references.json`)* : décret n° 95-2487, modifié par les décrets
n° 2000-908, 2001-1446, 2006-2777 et 2012-2586 — liste des entreprises publiques concernées. **[D]**

---

## 6. L'assurance maladie — loi n° 2004-71 (CNAM)

**[T]** (miroir iort.tn, texte français intégral, 29 articles).

*Art. 1-2* : régime d'assurance maladie au profit des assurés sociaux **et de leurs ayants droit**,
comportant un **régime de base obligatoire** et des **régimes complémentaires facultatifs**.

*Art. 3* : « *Les dispositions de la présente loi sont applicables aux assurés sociaux mentionnés
dans **les différents régimes légaux de sécurité sociale**. Les **étapes d'application** […] pour
les différentes catégories d'assurés sont fixées par décret.* » — la loi n'a donc **aucune date
d'effet propre**.

*Art. 4 — les bénéficiaires*, à citer intégralement dans le précis :
- **l'assuré social** ;
- le **conjoint non divorcé** et ne bénéficiant pas, au titre de son activité, d'une couverture
  légale obligatoire contre la maladie ;
- les **descendants à charge** : enfants **mineurs** non couverts par ailleurs ; **la fille quel que
  soit son âge** tant que son obligation alimentaire n'incombe pas à son époux ou tant qu'elle ne
  dispose pas de source de revenu ; les **enfants handicapés** incapables d'exercer une activité
  rémunérée et non couverts ;
- les **bénéficiaires d'une pension de survivants** au titre d'un régime légal, sans couverture
  propre ;
- les **ascendants à charge**, à condition de ne pas être soumis à titre principal à une couverture
  légale obligatoire.

*Art. 5* : prise en charge des soins **dans les secteurs public et privé**, **à l'exception des
frais consécutifs à un accident du travail ou à une maladie professionnelle**, qui restent régis
par la législation en vigueur. Conditionnée à l'affiliation et à la déclaration à l'un des régimes
de l'article 3.

*Art. 7* : création de la **CNAM**, établissement public à caractère non administratif.
*Art. 8* : outre le régime d'assurance maladie, la CNAM gère **les régimes AT/MP des secteurs
public et privé**, **les autres régimes légaux d'assurance maladie**, et sert **les indemnités de
maladie et de couches** prévues par les régimes de sécurité sociale à la date d'entrée en vigueur.
C'est l'article qui déplace vers la CNAM une partie du dispositif décrit aux §3 et §5 sans en
modifier le contenu.
*Art. 11-13* : convention cadre et **conventions sectorielles** avec les fournisseurs de soins,
approuvées par arrêté et publiées au JORT.
*Art. 15* : cotisation de base **6,75 %** du salaire ou du revenu — **4 %** employeur / **2,75 %**
salarié ; **totalité** à la charge de l'assuré travaillant pour son propre compte ; **4 %** pour les
pensionnés.
*Art. 16* (remplacé par la loi n° 2017-47) et *16 bis* : recouvrement par la CNRPS et la CNSS, et
transfert à la CNAM.

### Le calendrier d'ouverture — décret n° 2007-1366

**[T]** (miroir iort.tn). *Article premier* : « *À compter du **1er juillet 2007**, les dispositions
de la loi n° 2004-71 […] s'appliquent aux assurés sociaux ci-après mentionnés :*
- *les **affiliés à la CNRPS**,*
- *les affiliés à la CNSS assujettis aux régimes suivants : le régime des **travailleurs salariés
  du secteur non agricole** (loi n° 60-30) ; le régime de sécurité sociale **dans le secteur
  agricole** (loi n° 81-6, telle que modifiée par la loi n° 89-73) ; le régime des **artistes,
  créateurs et intellectuels** (loi n° 2002-104) ; le régime des **travailleurs tunisiens à
  l'étranger** (décret n° 89-107) ; le régime des **travailleurs non salariés** des secteurs
  agricole et non agricole (décret n° 95-1166).* »

*Art. 2* : extension possible « *dans une étape ultérieure* » à d'autres catégories.

**Constat.** Le régime de la **loi n° 2002-32** (employés de maison, agents publics non couverts,
petits pêcheurs, petits agriculteurs, artisans à la pièce) **n'est pas dans la liste**, et aucune
extension postérieure n'a été trouvée : sur les quatre textes que `jort_cache` rattache à la loi
n° 2004-71 (décrets n° 2005-3031 et 2007-1366, loi n° 2017-47), aucun n'ajoute de régime. Les
assurés de ce régime relèvent donc des **prestations de soins servies par la CNSS** au titre des
articles 10 et 11 de la loi n° 2002-32, non de la CNAM. **Résultat à confirmer** — lacune L4.

*Textes d'application repérés* **[M]** : décret n° 2005-321 (organisation de la CNAM, JORT n° 15 de
2005, pp. 459-463) ; décret n° 2005-3031 (contrôle médical, n° 94 de 2005, pp. 3331-3334) ; décret
n° 2005-3154 (conventions, n° 99 de 2005, pp. 3507-3509) ; décret n° 2007-1367 (modalités,
procédures et taux de prise en charge, n° 47 de 2007, pp. 1983-1988), modifié par le décret
n° 2008-756 ; décret n° 2007-1406 (assiette des cotisations, n° 49 de 2007, pp. 2154-2163) ; arrêté
du 3 juin 2008 (plafond annuel, n° 45 de 2008, pp. 1717-1719) ; décret n° 2008-3707 (organigramme).

---

## 7. La protection contre la perte d'emploi

### 7.1 Loi n° 96-101 du 18 novembre 1996 — le seul dispositif effectif

**[T]**, lue à l'image (JORT n° 94 de 1996, pp. 2319-2320). *Article premier* : « *La présente loi
a pour objet de déterminer les mesures de la protection sociale en faveur des travailleurs ayant
cessé leur travail pour des raisons **économiques ou technologiques**.* »

**Chapitre I — prise en charge des indemnités de licenciement.** *Art. 2* : la CNSS est habilitée à
prendre en charge les indemnités dues aux travailleurs licenciés pour raisons économiques ou
technologiques **ainsi que leurs droits légaux**, « *au cas où il est établi qu'ils ne peuvent
recouvrer les sommes qui leur sont dues **en raison de cessation de paiement par l'entreprise*** ».
*Art. 3* : subrogation de la CNSS. *Art. 4* : privilège des salaires ; recouvrement par états de
liquidation rendus exécutoires par le ministre des Affaires sociales, **nonobstant opposition**.
*Art. 5* : financement par les montants recouvrés et par une **cotisation complémentaire de 0,4 %
des salaires, prélevée sur le taux global** de cotisation de la loi n° 60-30 — donc **sans
prélèvement additionnel**. *Art. 6* : conditions et modalités fixées par décret.

**Chapitre II — maintien des droits.** *Art. 7* : « *Nonobstant les dispositions de la loi
n° 60-30 […], le bénéfice **des allocations familiales et de la majoration pour salaire unique** est
maintenu au profit des travailleurs régis par la loi susvisée et licenciés pour des raisons
économiques ou technologiques, **au titre des quatre trimestres suivant celui au cours duquel ils
ont cessé leur activité**. Le montant de ces prestations correspond **au taux plafond** prévu par la
loi précitée.* » Pour l'ouverture du droit aux **soins**, ces périodes sont **assimilées à des
périodes d'activité**. *Art. 8* : le caractère économique ou technologique doit être constaté par
**l'inspection du travail**, la **commission de contrôle des licenciements** ou **les tribunaux** ;
le travailleur ne doit pas avoir exercé, pendant la période, une activité assujettie ouvrant droit
aux mêmes prestations.

**Chapitre III — interventions sociales.** *Art. 9* : une **enveloppe annuelle** est prélevée sur
les **réserves de la CNSS** et affectée au financement des interventions et actions sociales au
profit des travailleurs. *Art. 10* : conditions, modalités et mode de fixation de l'enveloppe fixés
par décret.

**Modificateur** **[M]** : loi n° 2002-24 du 27 février 2002, JORT n° 18 de 2002, p. 515. *Contenu
non lu.*

**Conclusion à porter au précis.** La loi n° 96-101 **n'institue aucun revenu de remplacement**.
Elle fait de la CNSS un **garant de créances salariales** et **proroge des droits déjà ouverts**.
Employer le mot « indemnité pour perte d'emploi » à son propos serait un faux sens.

### 7.2 Article 17 de la loi de finances pour 2025

**[T]** — lu sur l'édition **arabe** du JORT n° 149 du 10 décembre 2024, pp. 6420-6421 (loi
n° 2024-48 du 9 décembre 2024). Traduction de travail :

> **Article 17 — Création d'un fonds spécial « fonds d'assurance contre la perte de postes de
> travail pour raisons économiques »**
> 1) Il est créé un fonds spécial dénommé « fonds d'assurance contre la perte de postes de travail
> pour raisons économiques », ayant pour objet de financer un **régime d'assurance contre la perte
> collective de postes de travail pour des raisons non imputables aux deux parties de la relation
> de travail**, et d'instaurer un **régime d'encadrement social des travailleurs licenciés pour
> raisons économiques** et de leur protection. Le ministre chargé des affaires sociales est
> ordonnateur des dépenses du fonds. **Les conditions et procédures de gestion du fonds sont fixées
> par décret.**
> 2) Le fonds est financé par : une dotation du budget de l'État **dans la limite de 5 millions de
> dinars** ; une **cotisation de 0,5 % à la charge de l'employeur et du salarié**, assise sur la
> masse salariale déclarée à la CNSS ; **14 % du produit de la majoration spécifique sur le tabac
> et les allumettes** ; une taxe de **30 %** sur les jeux auxquels on participe par téléphone, SMS
> ou serveur vocal, à la charge du participant ; les dons et toutes ressources affectées au fonds.
> 3) Le fonds est géré selon une convention conclue entre les ministres chargés des affaires
> sociales, de l'emploi et des finances.
> 4) Sont **abrogés les articles 2 à 4 de la loi n° 2009-40 du 8 juillet 2009** (loi de finances
> complémentaire pour 2009) relatifs à la création du compte de financement des mesures
> exceptionnelles de mise à la retraite, dont le reliquat des ressources est **transféré au fonds**.

**Le décret prévu au § 1 n'a pas été trouvé.** Interrogation de `jort_cache.db` sur les années 2025
et 2026, sur les titres contenant « perte », « licenci » et la racine arabe « فقدان » : aucun
résultat. **À la date du 8 septembre 2026, le régime d'assurance contre la perte de poste de
travail n'est donc pas opérant** — le texte crée le véhicule financier, pas le droit. Résultat
négatif, à réinterroger avant publication.

---

## 8. Les régimes — champ d'application personnel, régime par régime

### RSNA — salariés non agricoles, loi n° 60-30
**[T]** art. 34 (renvoi de l'art. 52 et de l'art. 69). *Note : l'article 34 lui-même n'a pas été
lu ; il énumère les établissements et professions assujettis.* Ouvre **prestations familiales**
(arts 51-67) **et assurances sociales** (arts 68-98). C'est le seul régime doté des deux blocs
depuis l'origine.

### RSA — salariés agricoles, loi n° 81-6, titres I et II
**[T]** *Article premier*, lu à l'image : « *Il est institué un régime de sécurité sociale au profit
des **travailleurs salariés et des coopérateurs de l'agriculture**. Ce régime assure […] le service
des prestations en matière **d'assurances sociales : maladie, maternité, décès**, et de pensions de
vieillesse, d'invalidité et de survivants. Des **décrets pourront attribuer aux salariés agricoles
le bénéfice d'autres prestations de sécurité sociale** et en fixer les modalités.* »
→ **Pas de branche prestations familiales** dans le régime agricole de base.
*Art. 2* : travailleurs salariés et coopérateurs exerçant des activités agricoles au sens de
l'article 3 du Code du travail, **à l'exception** de ceux employés par des entreprises affiliées à
un régime légal couvrant les mêmes risques ; l'affiliation à l'un ou l'autre doit couvrir
**l'ensemble du personnel**. *Art. 3* : gestion par la CNSS ; administration des pensions déléguée
à la CAVIS (décret n° 76-981 du 19 novembre 1976).

### RSAA — régime agricole amélioré, loi n° 81-6 titre III, ajouté par la loi n° 89-73
**[T]**, lu à l'image (JORT n° 60 de 1989, pp. 1338-1339). Intitulé exact du titre ajouté :
« **Dispositions particulières applicables aux salariés employés par certaines entreprises
agricoles** ».
*Art. 86 — champ, obligatoire pour* : les **coopérateurs salariés** employés par les entreprises
agricoles ayant la forme de société, les sociétés de mise en valeur, les coopératives agricoles et
toutes personnes morales agricoles non assujetties à un régime couvrant les mêmes risques ; **tous
les salariés des autres exploitants agricoles employant 30 salariés permanents au moins** ; les
**pêcheurs** employés sur des bateaux dont la jauge brute est inférieure à 30 tonneaux, pêcheurs
indépendants et petits armateurs au sens du code du pêcheur (loi n° 75-17 du 31 mars 1975).
Extension possible par décret. *Art. 87* : l'adhésion doit couvrir **l'ensemble des salariés de
l'entreprise** ; les travailleurs déjà immatriculés à un régime plus favorable y restent affiliés.
*Art. 90* : cotisation **15 %** — 10 % employeur, 5 % salarié ; **totalité** pour les non-salariés.
*Art. 91* : « *Les assurés soumis au régime prévu par le présent titre bénéficient des prestations
prévues par la présente loi **ainsi que des allocations familiales**.* »
*Art. 92* : « *Les allocations familiales sont servies du chef de l'assuré pour les **trois premiers
enfants** selon les **mêmes conditions et aux mêmes taux** que ceux prévus par les **articles 52 à
65 de la loi n° 60-30***. » Maintenues au profit des titulaires de pensions.
*Art. 93* : stage — sont pris en considération les trimestres ayant donné lieu à déclaration d'un
salaire **au moins égal à 50 fois le SMAG**.
*Art. 94* : prestations en espèces d'assurances sociales calculées sur les salaires déclarés au
titre d'un **trimestre choisi parmi les quatre précédant** la maladie, la maternité ou le décès, au
cours duquel les salaires ont été les plus élevés ; **plafonnés dans les mêmes conditions que
l'article 88 al. 2 de la loi n° 60-30**.
*Art. 4 de la loi n° 89-73* : **entre en vigueur le 1er octobre 1989**.
→ **Le RSAA est, avec le RSNA, le seul régime CNSS ouvrant les allocations familiales.**

### RTNS — travailleurs non salariés, décret n° 95-1166
**[T]**, lu à l'image (JORT n° 55 de 1995, pp. 1486-1489).
*Article premier* : « *Les dispositions des **articles 68 à 98, 100 à 107, 109 à 120** de la loi
n° 60-30 […] et celles des articles 20 à 38, 46 à 52, 54 et 57 du décret n° 74-499 […] sont
étendues […] aux travailleurs non salariés des secteurs agricole et non agricole, **qui ne sont
pas affiliés au titre de leur activité non salariée à un régime légal couvrant les mêmes
risques***. » L'énumération **commence à l'article 68** : les articles 51 à 67 — les prestations
familiales — sont **exclus**.
*Art. 2* : travailleur non salarié = « *toute personne exerçant à titre principal une activité
professionnelle, quelle que soit sa nature, pour son propre compte ou en qualité de mandataire* » ;
étendu aux **artisans titulaires d'une carte professionnelle** et aux **métayers**.
*Art. 4* : affiliation obligatoire dans le mois suivant l'assujettissement ; **impossible au-delà de
55 ans révolus**, sauf si l'intéressé totalise déjà **40 trimestres validés** ; exemption pour les
titulaires de pensions de retraite et d'invalidité.
*Art. 7* : cotisations assises sur un **revenu forfaitaire** = classe de revenu × coefficient
multiplicateur du SMIG (secteur non agricole, 2 400 h/an) ou du SMAG (secteur agricole, 300 j/an) ;
**10 classes**, coefficients 1 / 1,5 / 2 / 3 / 4 / 6 / 9 / 12 / 15 / 18. *Art. 9* : taux **11 %**,
dont **7 %** pensions et **4 %** assurances sociales.
*Art. 16* : bénéfice des prestations du **régime des assurances sociales** du titre II chapitre II
de la loi n° 60-30. *Art. 17 — stage* : indemnités en espèces de **maladie ou de décès**,
**deux trimestres de cotisations effectives** pendant les quatre trimestres précédant celui de
l'événement ; **indemnité de couche**, **quatre trimestres** de cotisations effectives précédant le
trimestre de l'accouchement. *Art. 18* : assiette = moyenne pondérée des coefficients des classes
d'adhésion sur les quatre trimestres précédents ; le **capital décès** obéit à la même règle.
*Art. 21* : droit à l'**hospitalisation** subordonné à **deux trimestres de cotisations effectives**
pendant les quatre trimestres précédant le début de l'hospitalisation.

### RTTE — travailleurs tunisiens à l'étranger, décret n° 89-107
**[T]**, lu à l'image (JORT n° 4 de 1989, pp. 98-99).
*Article premier* : extension des **articles 68 à 96, 100 à 120** de la loi n° 60-30 et des articles
20, 38, 46 à 52, 54 et 57 du décret n° 74-499 « *aux travailleurs tunisiens à l'étranger **qu'ils
soient salariés ou non salariés**, qui ne sont pas couverts par une **convention bilatérale de
sécurité sociale** ou par une réglementation spéciale régissant leur affiliation* ». Là encore,
l'énumération **commence à 68** : pas de prestations familiales.
*Art. 3* : « *L'adhésion au régime prévu par le présent décret est **volontaire**. Elle couvre
**obligatoirement la branche des assurances sociales** et celles des pensions de vieillesse,
d'invalidité et de survivants.* » — les deux branches sont indissociables.
*Art. 6-7* : revenu forfaitaire = SMIG 48 h (2 400 h/an) × coefficient ; **4 classes**, coefficients
2 / 4 / 6 / 9, l'assuré choisissant librement sa classe. Taux **10,65 %** — **5,40 %** assurances
sociales, **5,25 %** pensions. *Art. 8* : cotisations à la charge du travailleur, éventuellement
prises en charge par son employeur.

### Bas revenus — loi n° 2002-32
**[T]** (miroir iort.tn, texte français intégral).
*Article premier* : « *Il est institué un régime spécifique de sécurité sociale comprenant l'octroi
des **prestations de soins**, des **pensions de vieillesse, d'invalidité et de survivants**.* » —
**aucune indemnité en espèces**, aucune prestation familiale. Catégories :
**a)** employés de maison ; **b)** personnes employées par l'État, les collectivités locales et les
EPA **qui ne sont pas couvertes par un autre régime légal** ; **c)** pêcheurs sur bateaux ≤ 5
tonneaux, pêcheurs indépendants et petits armateurs ; **d)** agriculteurs travaillant pour leur
propre compte exploitant **≤ 5 ha en sec ou 1 ha en irrigué** ; **e)** artisans travaillant à la
pièce. Extension possible par décret.
*Art. 2* : les catégories **c, d et e** peuvent **opter** pour le régime spécifique à leur
catégorie.
*Art. 7* : cotisation **7,5 %**, assise sur **2/3 du SMAG** (c, d, e) ou **2/3 du SMIG** (a, e) ;
2/3 employeur / 1/3 salarié pour ceux qui exercent sous l'autorité d'un employeur, totalité pour
les indépendants.
*Art. 10 — bénéficiaires des soins* : l'assuré, « *à condition que ces prestations **ne rentrent
pas dans le cadre du régime des accidents du travail et des maladies professionnelles*** » ; le
conjoint ; les enfants mineurs à charge et non assurés ; les enfants au-delà de 20 ans en
impossibilité permanente et absolue de travailler ; la fille au-delà de 20 ans tant qu'elle ne
dispose pas de ressources ou que l'obligation alimentaire n'incombe pas à son époux ; les
**ascendants à charge** — définis comme ne bénéficiant d'aucune couverture, sans revenu permanent
ou avec un revenu non imposable, **âgés d'au moins 55 ans**, la condition d'âge tombant en cas
d'infirmité ou de maladie incurable.
*Art. 36* : hormis les employés de maison et les personnes employées par l'État, les collectivités
locales et les EPA, sont applicables les chapitres 1 et 2 du titre III de la loi n° 60-30, sauf les
articles 99, 108, 121, 122 et 123 pour les petits agriculteurs et les artisans à la pièce.
*Note de nomenclature* : le livre Retraites intitule cette section « **Le régime des travailleurs à
bas revenu** » (`precis/fr/retraites/_secteur_prive.qmd`, l. 15). La correspondance avec la loi
n° 2002-32 est **fortement probable mais non attestée** dans le livre, qui ne cite aucun texte —
lacune L5.

### Artistes, créateurs et intellectuels — loi n° 2002-104
**[T]** (miroir iort.tn).
*Article premier* : régime spécial comportant « *les **assurances sociales**, les pensions de
vieillesse, d'invalidité et de survivants et les **actions sanitaires et sociales*** ». Pas de
prestations familiales.
*Art. 2 — conditions cumulatives* : **A)** appartenance au secteur culturel ou exercice permanent
d'une activité artistique ou culturelle, attestée par une pièce délivrée par le ministère chargé de
la Culture ; **B)** **n'être assujetti à aucun autre régime légal** de sécurité sociale ; **C)** ne
bénéficier d'**aucune indemnité permanente attribuée par l'État** ni d'un revenu lié à une autre
activité.
*Art. 6* : affiliation obligatoire dans le mois suivant l'assujettissement ; **exemption** pour les
titulaires de pensions de retraite et d'invalidité.
*Art. 7* : cotisation **11 %** du revenu de la classe, **jamais inférieur à deux fois le SMIG**
régime 48 h (2 400 h/an) ; **7 %** pensions, **4 %** assurances sociales.
*Art. 9* : bénéfice des prestations du **titre II chapitre II de la loi n° 60-30**.
*Art. 10 — stage*, identique au RTNS : indemnités en espèces de **maladie ou de décès**, **deux
trimestres** de cotisations effectives dans les quatre trimestres précédant ; **indemnité de
couche**, **quatre trimestres** précédant le trimestre de l'accouchement.
*Art. 37-38* : droit d'option des artistes précédemment affiliés au RTNS, exerçable par demande
écrite dans l'année suivant la promulgation ; renonciation à l'option **une seule fois** dans la
carrière.

### Secteur public — CNRPS
Textes de base **[M]** : loi n° 72-2 du 15 février 1972 portant **réforme du régime de prévoyance
sociale des fonctionnaires** (JORT n° 7 de 1972, p. 189), modifiée notamment par la **loi
n° 97-60 du 28 juillet 1997** dont l'article 2 alinéa c nouveau définit les **enfants à charge**
pour les soins **[T]**, lu à l'image dans le même fascicule que la loi n° 97-58 ; loi n° 86-86 du
1er septembre 1986 (structures) ; décret n° 76-3 (CNRPS).
Prestations non-retraite : **indemnités à caractère familial** (§2.2, servies par l'employeur),
**capital-décès** (§4.2, décret n° 93-308, servi par la CNRPS), **AT/MP** (§5.2, loi n° 95-56,
salaire maintenu par l'employeur + rente CNRPS), **assurance maladie CNAM** depuis le 1er juillet
2007, **congés de maternité et de paternité à plein traitement** (loi n° 2024-44). Il n'y a **pas
d'indemnité journalière de maladie** : le régime statutaire maintient le traitement.
**Non lu** : le texte qui organise les congés de maladie des agents publics (loi n° 83-112, statut
général) — hors périmètre de cette note.

### Travailleuses agricoles — décret-loi n° 2024-4
**[T]** (miroir iort.tn, texte français intégral, 340 lignes).
*Article premier* : régime spécifique de protection sociale des travailleuses agricoles garantissant
« *les prestations d'**assurance maladie**, les **pensions** de vieillesse, d'invalidité et des
survivants, la **couverture contre les risques professionnels** et les prestations du programme
« **Amen Social** »* ». Il croise donc contributif et assistance dans un même texte.
*Art. 17* : institution du régime spécifique de sécurité sociale (assurance maladie + pensions).
*Art. 18* : gestion **CNSS**. *Art. 19* : affiliation obligatoire de la travailleuse agricole non
salariée dans le mois suivant l'assujettissement. *Art. 20 et 23* : **l'État prend en charge les
cotisations à la charge des travailleuses agricoles pendant les trois premières années** d'activité.
*Art. 24 — ayants droit assurance maladie* : la travailleuse agricole et son **conjoint non
divorcé** ne bénéficiant pas d'une couverture obligatoire au titre de son activité.
*Art. 25* : « *La travailleuse agricole bénéficie des **indemnités et des congés de maternité**
conformément aux dispositions de la législation en vigueur.* » — renvoi, sans règle propre.
*Art. 35* : les prestations « Amen Social » **ne sont pas cumulables** avec les prestations de la
couverture sociale.
*Art. 38-39 — AT/MP* : définitions calquées sur la loi n° 94-28, étendues à la travailleuse agricole
**salariée ou non salariée** ; « *la gestion du régime de réparation […] est confiée à la **Caisse
nationale d'assurance maladie*** » — cohérent avec l'article 8 de la loi n° 2004-71. *Art. 40* :
affiliation obligatoire de la non-salariée **et** de tout employeur d'une salariée agricole.
*Art. 42* : l'État prend en charge les cotisations AT/MP pendant les trois premières années.
*Art. 43-48* : soins, appareillage, **indemnité journalière** en cas d'incapacité temporaire,
**rente** en cas d'incapacité permanente, **indemnité de décès équivalente à un mois de salaire**
au conjoint et aux enfants à charge, **rente de décès** au conjoint et aux enfants à charge.
→ Premier texte tunisien à ouvrir l'AT/MP à des **non-salariées**.
*Aucune prestation familiale.*

---

## 9. La matrice régime × prestation

**Convention de lecture.** ● = prestation ouverte, avec le texte qui l'ouvre. ○ = **fermée**,
c'est-à-dire attestée comme non comprise dans le régime. ? = **non tranché**, aucune case n'est
laissée vide. Les prestations familiales sont prises au sens de l'article 51 de la loi n° 60-30
(allocations familiales + congés de naissance + congés de jeunes travailleurs).

| Régime | Prestations familiales | Indemnités maladie / couches | Soins | Capital / indemnité décès | AT-MP | Perte d'emploi | Assurance maladie CNAM |
|---|---|---|---|---|---|---|---|
| **RSNA** (loi n° 60-30) | ● arts 51-67 ; taux 18/16/14 % depuis la loi n° 75-82 (1976), plafond 122 D depuis la loi n° 86-75 (1986), trois enfants depuis la loi n° 88-38 (1989) ; **majoration pour salaire unique** art. 65 bis, loi n° 80-36 (1980) ; **frais de crèche** loi n° 94-88 (1994) | ● arts 71-82 | ● art. 91 (jusqu'en 2007) | ● arts 83-87 (indemnité de décès) | ● loi n° 94-28 art. 4 | ● loi n° 96-101 (maintien de droits, pas de revenu) | ● décret n° 2007-1366, **1er juillet 2007** |
| **RSA** (loi n° 81-6, titres I-II) | ○ art. 1er : maladie, maternité, décès et pensions seulement | ● art. 1er | ● art. 1er | ● art. 1er (« décès ») | ● loi n° 94-28 art. 4 | ? renvoi de la loi n° 96-101 limité aux « travailleurs régis par la loi [n° 60-30] » | ● décret n° 2007-1366, **1er juillet 2007** |
| **RSAA** (loi n° 81-6 titre III, loi n° 89-73) | ● **art. 91-92** — 3 premiers enfants, mêmes conditions et taux que les arts 52 à 65 de la loi n° 60-30 | ● art. 94 | ● art. 94 | ● art. 94 (« décès ») | ● loi n° 94-28 art. 4 | ? *idem RSA* | ● décret n° 2007-1366 (visé sous « loi n° 81-6 modifiée par la loi n° 89-73 ») |
| **RTNS** (décret n° 95-1166) | ○ art. 1er : extension à partir de l'**art. 68** | ● art. 16-17 (stage 2 trim. ; couche 4 trim.) | ● art. 21 (hospitalisation, stage 2 trim.) | ● art. 18 (capital décès) | ○ loi n° 94-28 art. 4 vise les travailleurs **employés** ; entreprises familiales sur option | ○ loi n° 96-101 vise les travailleurs licenciés | ● décret n° 2007-1366, **1er juillet 2007** |
| **RTTE** (décret n° 89-107) | ○ art. 1er : extension à partir de l'**art. 68** | ● arts 1 et 3 | ● arts 1 et 3 | ● arts 1 et 3 | ? le décret n'évoque pas les risques professionnels | ○ | ● décret n° 2007-1366, **1er juillet 2007** |
| **Bas revenus** (loi n° 2002-32) | ○ art. 1er : soins et pensions seulement | ○ art. 1er | ● arts 10-11, **servis par la CNSS** | ○ art. 1er | ● loi n° 94-28 art. 4 (gens de maison nommément cités) ; loi n° 2002-32 art. 10.1 écarte du régime de soins ce qui relève de l'AT/MP | ○ | ? **absent** de la liste du décret n° 2007-1366 ; aucune extension trouvée — lacune L4 |
| **Artistes** (loi n° 2002-104) | ○ art. 1er : assurances sociales, pensions, actions sanitaires et sociales | ● arts 9-10 (stage 2 trim. ; couche 4 trim.) | ● art. 9 | ● arts 9-10 | ? non traité par la loi ; les artistes salariés relèvent de la loi n° 94-28 art. 4 | ○ | ● décret n° 2007-1366, **1er juillet 2007** |
| **Secteur public** (CNRPS) | ● **indemnités à caractère familial**, loi n° 88-39 + décret n° 96-1906 — **servies par l'employeur**, pas par la caisse ; nature d'indemnité de rémunération | ○ pas d'indemnité journalière : **traitement maintenu** (statut) ; congés de maternité et paternité **à plein traitement**, loi n° 2024-44 arts 3-6 | ● loi n° 72-2 (prévoyance sociale des fonctionnaires), puis CNAM | ● **capital-décès**, décret n° 93-308, servi par la **CNRPS** | ● loi n° 95-56 — **hors militaires et forces de sécurité intérieure** ; salaire maintenu par l'employeur, rente par la CNRPS | ? sans objet dans le statut ; **non tranché** pour les agents contractuels | ● décret n° 2007-1366, **1er juillet 2007** |
| **Travailleuses agricoles** (décret-loi n° 2024-4) | ○ art. 1er et art. 17 : assurance maladie, pensions, risques professionnels, Amen Social | ● art. 25 (maternité, par renvoi) ; ? indemnité de maladie non mentionnée | ● art. 24 | ● art. 47 (indemnité d'un mois de salaire) et art. 48 (rente de décès), au titre de l'**AT/MP** ; ? capital décès hors AT/MP | ● arts 38-48, **y compris non salariées** — gestion **CNAM** | ○ | ● art. 24, législation en vigueur |

**Deux croisements que la matrice met au jour.**

1. **Un même travailleur peut relever de deux régimes selon la prestation.** L'employé de maison
   est couvert pour les **soins et les pensions** par la loi n° 2002-32, et pour les **AT/MP** par
   la loi n° 94-28, qui le cite nommément à l'article 4. L'article 10.1 de la loi n° 2002-32 écarte
   d'ailleurs explicitement du régime de soins ce qui relève de l'AT/MP. La segmentation n'est donc
   pas par personne mais **par risque**.
2. **Les non-salariés étaient exclus de l'AT/MP jusqu'en 2024.** La loi n° 94-28 s'applique aux
   travailleurs « **employés** » et exclut les entreprises familiales sauf option. Le décret-loi
   n° 2024-4 est le premier texte à ouvrir la couverture des risques professionnels à des
   **non-salariées**, et il en confie la gestion à la CNAM, cohérent avec l'article 8 de la loi
   n° 2004-71. C'est un changement de doctrine qui mérite d'être relevé.

---

## 10. Lacunes — ce qui n'a pas pu être sourcé

| # | Objet | État | Piste |
|---|---|---|---|
| **L1** | ~~Texte fondateur de la majoration pour salaire unique~~ | **RÉSOLU** : loi n° 80-36 du 28 mai 1980, art. 65 bis, effet 1er mai 1980. Voir R4 et §2.1. | — |
| **L2** | **Revalorisation** des montants de la majoration pour salaire unique et de la contribution aux frais de crèche | **Non établie.** Les montants de 1980 (9,375 / 18,750 / 23,475 D) et de 1994 (15 D) n'ont aucun texte modificatif repéré dans `jort_cache`. Ils seraient donc nominalement gelés depuis, ce qui est plausible mais non vérifié. | Interroger les rapports annuels de la CNSS et le ministère des Affaires sociales ; vérifier les décrets pris sur le fondement de l'art. 65 bis et de la loi n° 94-88. |
| **L2 bis** | ~~Base légale de la contribution aux frais de crèche~~ | **RÉSOLU** : loi n° 94-88 du 26 juillet 1994 et décret n° 95-114 du 16 janvier 1995, effet 1er octobre 1994. Voir §2.1. | — |
| **L3** | **Articulation de la loi n° 2024-44 avec le stage de l'article 78 de la loi n° 60-30** | **Non tranché.** La loi de 2024 fixe des durées mais renvoie l'indemnisation privée à « la législation en vigueur » sans toucher aux conditions d'ouverture. | Vérifier l'existence d'une circulaire CNAM/CNSS 2024-2025 ; interroger `jort_cache` sur 2025-2026. |
| **L4** | **Le régime de la loi n° 2002-32 est-il entré dans la CNAM ?** | **Non tranché.** Absent du décret n° 2007-1366 ; aucune extension trouvée parmi les textes citant la loi n° 2004-71. | Dépouiller les décrets « assurance maladie » 2008-2015 ; vérifier si la loi n° 2002-32 a été modifiée. |
| **L5** | **Correspondance « régime des travailleurs à bas revenu » ↔ loi n° 2002-32** | **Fortement probable, non attestée.** Le livre Retraites nomme la section sans citer de texte. | À trancher avec l'auteur du livre Retraites ; la nomenclature CNSS publique peut confirmer. |
| **L6** | **Date d'effet** de : loi n° 60-30, loi n° 81-6, loi n° 96-65, loi n° 96-101, décret n° 95-1166, décret n° 89-107, loi n° 2002-32, loi n° 2002-104, décret-loi n° 2024-4 | **Non établie.** Les articles finaux n'ont pas été lus. | Relire la dernière page de chaque texte ; peu coûteux, à faire avant rédaction. |
| **L7** | **Contenu des lois n° 61-9 (1961), n° 82-71 (1982), n° 95-101 (1995) et n° 2002-24 (2002)** | Repéré, **lu partiellement ou pas du tout**. Pour la n° 61-9, seul le fait qu'elle **ne touche pas l'article 61** est établi ; l'article modifié n'a pas été identifié (OCR de 1961 dégradé). La n° 82-71 touche aux prestations familiales des licenciés, la n° 95-101 à la prescription du capital décès, la n° 2002-24 modifie la loi n° 96-101. | Relire à l'image ; fascicules déjà localisés et océrisés. |
| **L8** | **Décret d'application de l'article 17 de la LF 2025** | **Introuvable au 8 septembre 2026.** Le régime d'assurance contre la perte de poste n'est donc pas opérant. | Réinterroger `jort_cache` avant publication ; c'est un résultat négatif à publier, pas un trou. |
| **L9** | **Article 34 de la loi n° 60-30** (liste des établissements et professions assujettis) | **Non lu.** C'est le pivot du champ d'application du RSNA, visé par les articles 52 et 69. | JORT n° 57 de 1960, page de folio ~1604 ; une lecture à l'image suffit. |
| **L10** | **Circulaire n° 42 du 25 octobre 1996**, gestion des indemnités à caractère familial dans le secteur public, 16 pages | Repérée **[M]**, non lue. C'est la source la plus détaillée sur le dispositif public. | JORT n° 94 de 1996, pp. 2349-2364 — même fascicule que la loi n° 96-101, déjà océrisé. |
| **L11** | **Chaîne des décrets d'application de la loi n° 95-56** (n° 95-2487, 2000-908, 2001-1446, 2006-2777, 2012-2586) | **[D]** depuis une note de `references.json`, non vérifiée texte par texte. | Requête `jort_cache` par numéro. |

---

## 11. Deux conflits de source, à porter tels quels

**C1 — Loi n° 2017-47, date de signature.** Le miroir iort.tn (`loi_2017_47_2017.md`) porte
**deux fois** « **15 juin 2017** » : dans l'intitulé et dans la formule finale « Tunis, le 15 juin
2017 ». `jort_cache.db` donne `date_signature = 2017-05-15` avec un titre « du 15 Mai 2017 », et
un `date_publication` **égal** à la date de signature — signature d'un enregistrement dégradé. Le
JORT n° 50 de 2017 est cohérent avec une publication de juin. **Retenir la date du texte
(15 juin 2017) et signaler la métadonnée** ; à confirmer sur le fascicule.

**C2 — Pagination des textes de 2024 et postérieurs.** Comme le documente déjà la note de
`lf-2025` dans `precis/fr/fiscalite/references.json`, **deux paginations coexistent** et les deux
sont exactes : l'édition française et l'édition arabe du même fascicule ne portent pas les mêmes
folios. Deux conséquences pour cette note :
- l'article 17 de la LF 2025 est cité **pp. 6420-6421 de l'édition arabe** ; le folio de l'édition
  française n'a pas été établi ;
- `jort_cache` donne pour le décret-loi n° 2024-4 la page `5293-5293`, valeur incompatible avec un
  texte de 48 articles : elle décrit vraisemblablement **l'édition arabe** et un renvoi de sommaire.
  **Le folio français est non établi** ; toute citation doit préciser l'édition.

---

## 12. Références candidates (CSL-JSON)

### 12.1 Déjà présentes — à réutiliser, ne pas dupliquer

| Clé | Fichier | Remarque |
|---|---|---|
| `loi60-30` | `precis/fr/remunerations_publiques/references.json` | URL pist.tn correcte. **Compléter la note** : pages 1602-1613, et préciser que le texte porte les articles 51-67 (prestations familiales) et 68-98 (assurances sociales). |
| `loi2004-71` | *idem* | La note dit « contenu non lu » : **à corriger**, le texte français intégral est disponible sur le miroir iort.tn et a été dépouillé ici. |
| `loi95-56` | *idem* | La note dit « contenu non lu » : **à corriger** de même. Ajouter la date d'effet **1er janvier 1996** (art. 58). |
| `lf-2025` | `precis/fr/fiscalite/references.json` | **À réutiliser pour l'article 17** — ne pas créer d'entrée nouvelle. Compléter la note : « art. 17, pp. 6420-6421 de l'édition arabe, création du fonds d'assurance contre la perte de postes de travail ». |
| `unicef2020` | `precis/fr/prestations_sociales/references.json` | Existe, jamais citée. Hors périmètre contributif. |
| `23975222/EZEBV8GK` | *idem* | Pièce jointe Zotero résiduelle, **à retirer** (plan §5). |

### 12.2 À créer

```json
{
  "items": [
    {
      "id": "loi88-38",
      "type": "legislation",
      "title": "Loi n° 88-38 du 6 mai 1988, complétant et modifiant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "33",
      "page": "735",
      "issued": {"date-parts": [[1988, 5, 6]]},
      "URL": "https://www.pist.tn/jort/1988/1988F/Jo03388.pdf",
      "note": "citation-key: loi88-38\nJORT n° 33 des 13-17 mai 1988, p. 735. Article 1er : art. 52 al. 2-4 nouveaux (limitation aux trois premiers enfants) et art. 61 al. 2 nouveau (18 %, 16 %, 14 % d'une rémunération globale trimestrielle plafonnée à 122,000 D). Article 5 : entrée en vigueur le 1er janvier 1989, droits acquis maintenus. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi88-39",
      "type": "legislation",
      "title": "Loi n° 88-39 du 6 mai 1988, relative à l'octroi des indemnités familiales dans le secteur public",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "33",
      "page": "735",
      "issued": {"date-parts": [[1988, 5, 6]]},
      "URL": "https://www.pist.tn/jort/1988/1988F/Jo03388.pdf",
      "note": "citation-key: loi88-39\nJORT n° 33 des 13-17 mai 1988, p. 735, même page que la loi n° 88-38. Article unique : indemnité familiale servie aux agents publics NON soumis au régime de la loi n° 60-30, dans les conditions du décret du 22 novembre 1918, limitée aux trois premiers enfants ; montant fixé par décret. Aucun article d'entrée en vigueur ; la loi ne s'applique pas aux droits acquis antérieurement au 1er janvier 1989. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret96-1906",
      "type": "legislation",
      "title": "Décret n° 96-1906 du 16 octobre 1996, portant fixation des taux des indemnités à caractère familial",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "85",
      "page": "2097",
      "issued": {"date-parts": [[1996, 10, 16]]},
      "URL": "https://www.pist.tn/jort/1996/1996F/Jo08596.pdf",
      "note": "citation-key: decret96-1906\nJORT n° 85 du 22 octobre 1996, p. 2097. Taux mensuels par enfant : 7,320 D / 6,507 D / 5,693 D ; 4,880 D pour le quatrième enfant ayant acquis le droit avant le 1er janvier 1989 et pour l'enfant handicapé au-delà du 3e rang. Abroge les décrets n° 86-611 et n° 88-1136. Effet 1er novembre 1996 (art. 5). Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi75-82",
      "type": "legislation",
      "title": "Loi n° 75-82 du 30 décembre 1975, modifiant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "87",
      "page": "2852",
      "issued": {"date-parts": [[1975, 12, 30]]},
      "URL": "https://www.pist.tn/jort/1975/1975F/Jo08775.pdf",
      "note": "citation-key: loi75-82\nJORT n° 87 des 30-31 décembre 1975, p. 2852. Article premier : art. 61 alinéa 2 nouveau — le montant trimestriel de l'allocation familiale devient 18 % pour le premier enfant, 16 % pour le deuxième, 14 % pour le troisième, 12 % pour le quatrième, d'une rémunération globale trimestrielle plafonnée à 72,000 D. Remplace le taux unique de 15 % et la bande 52-500 D de la loi n° 60-30. Art. 2 : prend effet à compter du 1er janvier 1976. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi80-36",
      "type": "legislation",
      "title": "Loi n° 80-36 du 28 mai 1980, complétant la loi n° 60-30 du 14 décembre 1960 organisant les régimes de sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "32",
      "page": "1478",
      "issued": {"date-parts": [[1980, 5, 28]]},
      "URL": "https://www.pist.tn/jort/1980/1980F/Jo03280.pdf",
      "note": "citation-key: loi80-36\nJORT n° 32 des 27-30 mai 1980, p. 1478. TEXTE FONDATEUR DE LA MAJORATION POUR SALAIRE UNIQUE dans le secteur privé : ajoute au chapitre 1er du titre II de la loi n° 60-30 une section I bis et un article 65 bis. Conditions cumulatives : enfants à charge au sens de l'art. 53, droit ouvert aux allocations familiales, conjoint sans activité professionnelle. Montants trimestriels 9,375 D / 18,750 D / 23,475 D pour un, deux, trois enfants ou plus. La CNSS se substitue aux employeurs servant déjà une indemnité de même nature, dans la limite de ces taux. Art. 2 : prend effet à compter du 1er mai 1980. Aucune recherche par titre ne pouvait trouver ce texte : son intitulé ne porte pas l'expression. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi86-75",
      "type": "legislation",
      "title": "Loi n° 86-75 du 28 juillet 1986, modifiant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "43",
      "page": "843",
      "issued": {"date-parts": [[1986, 7, 28]]},
      "URL": "https://www.pist.tn/jort/1986/1986F/Jo04386.pdf",
      "note": "citation-key: loi86-75\nJORT n° 43 des 1er-5 août 1986, p. 843. Article premier : art. 61 alinéa 2 nouveau — plafond de la rémunération globale trimestrielle porté de 72,000 à 122,000 dinars, taux 18/16/14/12 % inchangés. C'est CE TEXTE, et non la loi n° 88-38, qui fixe le plafond de 122 D. Art. 2 : prend effet à partir du 1er mai 1986. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi94-88",
      "type": "legislation",
      "title": "Loi n° 94-88 du 26 juillet 1994, relative à la contribution aux frais de prise en charge des enfants dans les crèches",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "60",
      "page": "1255",
      "issued": {"date-parts": [[1994, 7, 26]]},
      "URL": "https://www.pist.tn/jort/1994/1994F/Jo06094.pdf",
      "note": "citation-key: loi94-88\nJORT n° 60 du 2 août 1994, p. 1255. Base légale de la contribution aux frais de crèche, dispositif autonome hors de la loi n° 60-30. Art. 2 : servie au titre des enfants des assurées sociales et affiliées, sous plafond de salaire, et seulement pour les enfants admis au régime des allocations familiales. Art. 3 : à la charge des caisses de sécurité sociale. Art. 4 : servie directement à la crèche, enfants de 2 à 36 mois, onze mois par année, non servie pendant le congé de maternité. Lu à l'image ; date d'effet non établie (celle du décret n° 95-114 est le 1er octobre 1994). URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret95-114",
      "type": "legislation",
      "title": "Décret n° 95-114 du 16 janvier 1995, fixant le montant de la contribution aux frais de prise en charge des enfants dans les crèches, ainsi que les modalités et les conditions de son recouvrement",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "8",
      "page": "264",
      "issued": {"date-parts": [[1995, 1, 16]]},
      "URL": "https://www.pist.tn/jort/1995/1995F/Jo00895.pdf",
      "note": "citation-key: decret95-114\nJORT n° 8 du 27 janvier 1995, p. 264. Art. 1 : quinze dinars par enfant et par mois, onze mois par an, pour les enfants des assurées sociales actives dont le revenu mensuel indemnités comprises ne dépasse pas deux fois et demie le salaire minimum garanti ; demande présentée par la mère bénéficiaire. Art. 3 : versée trimestriellement et directement à la crèche. Art. 4 : servie à compter du 1er octobre 1994. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi89-73",
      "type": "legislation",
      "title": "Loi n° 89-73 du 2 septembre 1989, modifiant et complétant la loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "60",
      "page": "1338-1339",
      "issued": {"date-parts": [[1989, 9, 2]]},
      "URL": "https://www.pist.tn/jort/1989/1989F/Jo06089.pdf",
      "note": "citation-key: loi89-73\nJORT n° 60 des 5-8 septembre 1989, pp. 1338-1339. Ajoute à la loi n° 81-6 un titre III « Dispositions particulières applicables aux salariés employés par certaines entreprises agricoles », articles 86 à 101 : c'est le régime agricole amélioré (RSAA). Art. 86 champ (≥ 30 salariés permanents, coopérateurs, pêcheurs) ; art. 90 cotisation 15 % ; art. 91-92 allocations familiales pour les trois premiers enfants aux taux des articles 52 à 65 de la loi n° 60-30 ; art. 4 entrée en vigueur le 1er octobre 1989. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi81-6",
      "type": "legislation",
      "title": "Loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "9",
      "page": "265-273",
      "issued": {"date-parts": [[1981, 2, 12]]},
      "URL": "https://www.pist.tn/jort/1981/1981F/Jo00981.pdf",
      "note": "citation-key: loi81-6\nJORT n° 9 du 13 février 1981, pp. 265-273 ; rectificatif au JORT n° 26 du 17 avril 1981, p. 844. Article premier : le régime couvre les assurances sociales (maladie, maternité, décès) et les pensions — PAS les prestations familiales, qui ne sont ouvertes qu'au titre III ajouté par la loi n° 89-73. Article premier lu à l'image ; date d'effet non établie. URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret95-1166",
      "type": "legislation",
      "title": "Décret n° 95-1166 du 3 juillet 1995, relatif à la sécurité sociale des travailleurs non salariés dans les secteurs agricole et non agricole",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "55",
      "page": "1486-1489",
      "issued": {"date-parts": [[1995, 7, 3]]},
      "URL": "https://www.pist.tn/jort/1995/1995F/Jo05595.pdf",
      "note": "citation-key: decret95-1166\nJORT n° 55 du 11 juillet 1995, pp. 1486-1489. Article premier : étend les articles 68 à 98, 100 à 107 et 109 à 120 de la loi n° 60-30 — l'énumération commence à 68, donc SANS les prestations familiales (art. 51-67). Art. 9 cotisation 11 % (7 % pensions, 4 % assurances sociales) ; art. 17 stage de deux trimestres (quatre pour l'indemnité de couche). Modifié par le décret n° 2004-167 du 20 janvier 2004. Lu à l'image ; date d'effet non établie. URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret89-107",
      "type": "legislation",
      "title": "Décret n° 89-107 du 10 janvier 1989, étendant le régime de sécurité sociale aux travailleurs tunisiens à l'étranger",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "4",
      "page": "98-99",
      "issued": {"date-parts": [[1989, 1, 10]]},
      "URL": "https://www.pist.tn/jort/1989/1989F/Jo00489.pdf",
      "note": "citation-key: decret89-107\nJORT n° 4 du 17 janvier 1989, pp. 98-99. Article premier : étend les articles 68 à 96 et 100 à 120 de la loi n° 60-30 — sans les prestations familiales. Art. 3 : adhésion VOLONTAIRE, couvrant obligatoirement assurances sociales et pensions. Art. 6-7 : quatre classes, coefficients 2/4/6/9 du SMIG ; taux 10,65 %. Lu à l'image ; date d'effet non établie. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi2002-32",
      "type": "legislation",
      "title": "Loi n° 2002-32 du 12 mars 2002, relative au régime de sécurité sociale pour certaines catégories de travailleurs dans les secteurs agricole et non agricole",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "22",
      "page": "603-606",
      "issued": {"date-parts": [[2002, 3, 12]]},
      "URL": "https://www.pist.tn/jort/2002/2002F/Jo0222002.pdf",
      "note": "citation-key: loi2002-32\nJORT n° 22 du 15 mars 2002, pp. 603-606. Article premier : régime limité aux prestations de SOINS et aux pensions — ni indemnités en espèces ni prestations familiales. Cinq catégories : employés de maison, agents publics non couverts, pêcheurs ≤ 5 tonneaux, agriculteurs ≤ 5 ha en sec ou 1 ha en irrigué, artisans à la pièce. Art. 7 cotisation 7,5 % sur 2/3 du SMAG ou du SMIG. Texte français intégral sur le miroir iort.tn. Correspond probablement au « régime des travailleurs à bas revenu » du livre Retraites — correspondance non attestée. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi2002-104",
      "type": "legislation",
      "title": "Loi n° 2002-104 du 30 décembre 2002, relative au régime de sécurité sociale des artistes, des créateurs et des intellectuels",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "106",
      "page": "3187-3190",
      "issued": {"date-parts": [[2002, 12, 30]]},
      "URL": "https://www.pist.tn/jort/2002/2002F/Jo1062002.pdf",
      "note": "citation-key: loi2002-104\nJORT n° 106 du 31 décembre 2002, pp. 3187-3190. Article premier : assurances sociales, pensions et actions sanitaires et sociales — pas de prestations familiales. Art. 2 : trois conditions cumulatives, dont l'absence de tout autre régime légal et d'indemnité permanente de l'État. Art. 7 cotisation 11 % sur un revenu au moins égal à deux fois le SMIG. Art. 10 : stage de deux trimestres (quatre pour l'indemnité de couche). Texte français intégral sur le miroir iort.tn. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi94-28",
      "type": "legislation",
      "title": "Loi n° 94-28 du 21 février 1994, portant régime de réparation des préjudices résultant des accidents du travail et des maladies professionnelles",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "15",
      "page": "308-318",
      "issued": {"date-parts": [[1994, 2, 21]]},
      "URL": "https://www.pist.tn/jort/1994/1994F/Jo01594.pdf",
      "note": "citation-key: loi94-28\nJORT n° 15 du 22 février 1994, pp. 308-318. Art. 4 : champ le plus large du corpus (tous travailleurs employés, stagiaires, apprentis, élèves, détenus, chantiers de développement, gens de maison), EXCLUANT les agents publics couverts par un régime particulier et les entreprises familiales sauf option. Art. 35 : indemnité journalière = deux tiers de la rémunération quotidienne, carence de trois jours. Art. 107 : entrée en vigueur le 1er janvier 1995, abrogation de la loi n° 57-73 du 11 décembre 1957. Gestion CNSS (art. 2), transférée à la CNAM par l'art. 8 de la loi n° 2004-71. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi57-73",
      "type": "legislation",
      "title": "Loi n° 57-73 du 11 décembre 1957, relative au régime de réparation des accidents du travail et des maladies professionnelles",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "43",
      "page": "585-605",
      "issued": {"date-parts": [[1957, 12, 11]]},
      "URL": "https://www.pist.tn/jort/1957/1957F/Jo04357.pdf",
      "note": "citation-key: loi57-73\nJORT n° 43 du 20 décembre 1957, pp. 585-605 ; rectificatif au JORT n° 3 du 10 janvier 1958, pp. 24-25. Abrogée au 1er janvier 1995 par l'art. 107 de la loi n° 94-28. Résumé officiel : arrêté du 15 novembre 1960, JORT n° 53 de 1960, p. 1469. CONTENU NON LU ; métadonnées jort_cache uniquement. URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret93-308",
      "type": "legislation",
      "title": "Décret n° 93-308 du 1er février 1993, relatif au régime du capital-décès",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "13",
      "page": "246-247",
      "issued": {"date-parts": [[1993, 2, 1]]},
      "URL": "https://www.pist.tn/jort/1993/1993F/Jo01393.pdf",
      "note": "citation-key: decret93-308\nJORT n° 13 du 16 février 1993, pp. 246-247. Capital-décès du secteur public. Art. 1 : agents publics, membres du gouvernement, députés, gouverneurs, agents des EPIC et sociétés nationales (liste du décret n° 85-1025), retraités CNRPS. Art. 2 : cotisation 1 % (actifs) et 0,50 % (pensions). Art. 5 : rémunération annuelle de liquidation majorée de 1/12 par année de service dans la limite de 18 mois, +10 % par enfant à charge, doublée en cas de décès accidentel en service. Art. 7 : un tiers au conjoint, deux tiers aux enfants. Art. 14 : abroge le décret n° 74-572 du 22 mai 1974. Art. 15 : entrée en vigueur le 1er juillet 1993. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi96-101",
      "type": "legislation",
      "title": "Loi n° 96-101 du 18 novembre 1996, relative à la protection sociale des travailleurs",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "94",
      "page": "2319-2320",
      "issued": {"date-parts": [[1996, 11, 18]]},
      "URL": "https://www.pist.tn/jort/1996/1996F/Jo09496.pdf",
      "note": "citation-key: loi96-101\nJORT n° 94 du 22 novembre 1996, pp. 2319-2320 ; rectificatif au JORT n° 7 du 24 janvier 1997, p. 114. N'institue AUCUN revenu de remplacement. Chap. I : la CNSS prend en charge les indemnités de licenciement économique impayées pour cessation de paiement, financée par une cotisation complémentaire de 0,4 % prélevée sur le taux global de la loi n° 60-30. Chap. II art. 7 : maintien des allocations familiales et de la majoration pour salaire unique pendant quatre trimestres, au taux plafond, et assimilation de la période à de l'activité pour les soins. Chap. III art. 9 : enveloppe annuelle sur les réserves de la CNSS. Modifiée par la loi n° 2002-24 du 27 février 2002 (JORT n° 18 de 2002, p. 515). Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi98-91",
      "type": "legislation",
      "title": "Loi n° 98-91 du 2 novembre 1998, modifiant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "89",
      "page": "2184",
      "issued": {"date-parts": [[1998, 11, 2]]},
      "URL": "https://www.pist.tn/jort/1998/1998F/Jo08998.pdf",
      "note": "citation-key: loi98-91\nJORT n° 89 du 6 novembre 1998, p. 2184. Article 88 nouveau : le salaire journalier moyen servant au calcul des indemnités en espèces est déterminé sur le trimestre le plus favorable parmi les quatre précédents, ces salaires n'étant retenus que dans la limite de deux fois le SMIG régime 48 heures rapporté à 600 heures ; plafond révisable par décret. Art. 2 : applicable à compter du 1er mai 1998. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi96-65",
      "type": "legislation",
      "title": "Loi n° 96-65 du 22 juillet 1996, amendant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "60",
      "page": "1603",
      "issued": {"date-parts": [[1996, 7, 22]]},
      "URL": "https://www.pist.tn/jort/1996/1996F/Jo06096.pdf",
      "note": "citation-key: loi96-65\nJORT n° 60 du 26 juillet 1996, p. 1603. Article unique : articles 53 dernier alinéa, 54 et 55 alinéa 3 nouveaux. Relève les limites d'âge des enfants ouvrant droit aux allocations familiales — 16 ans sans condition, 18 ans en apprentissage, 21 ans pour la scolarité, au-delà de 21 ans en cas d'infirmité ou de carte d'handicapé ; les enfants handicapés sont servis quel que soit leur rang. Ne touche PAS l'article 61 (taux). Lu à l'image ; date d'effet non établie. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi97-58",
      "type": "legislation",
      "title": "Loi n° 97-58 du 28 juillet 1997, amendant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "61",
      "page": "1359",
      "issued": {"date-parts": [[1997, 7, 28]]},
      "URL": "https://www.pist.tn/jort/1997/1997F/Jo06197.pdf",
      "note": "citation-key: loi97-58\nJORT n° 61 du 1er août 1997, p. 1359. Article 91 alinéa 3 nouveau : bénéfice des soins pour les enfants mineurs à charge et non assurés, ouvert au-delà de 20 ans pour les enfants infirmes ou atteints de maladie incurable et pour la fille tant que l'obligation alimentaire n'incombe pas à son époux. Art. 2 : prend effet à compter du 1er mai 1997. Le même fascicule porte la loi n° 97-60 du 28 juillet 1997 amendant la loi n° 72-2 sur le régime de prévoyance sociale des fonctionnaires. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret2007-1366",
      "type": "legislation",
      "title": "Décret n° 2007-1366 du 11 juin 2007, portant détermination des étapes d'application de la loi n° 2004-71 du 2 août 2004 portant institution d'un régime d'assurance maladie aux différentes catégories d'assurés sociaux",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "47",
      "page": "1982-1983",
      "issued": {"date-parts": [[2007, 6, 11]]},
      "URL": "https://www.pist.tn/jort/2007/2007F/Jo0472007.pdf",
      "note": "citation-key: decret2007-1366\nJORT n° 47 de 2007, pp. 1982-1983. Article premier : à compter du 1er JUILLET 2007, la loi n° 2004-71 s'applique aux affiliés de la CNRPS et, à la CNSS, aux régimes des lois n° 60-30 et n° 81-6 (modifiée par la loi n° 89-73), n° 2002-104, et des décrets n° 89-107 et n° 95-1166. Le régime de la loi n° 2002-32 n'y figure pas. Art. 2 : extension ultérieure possible par décret. C'est ce décret, et non la loi, qui porte la date d'effet de l'assurance maladie. Texte français intégral sur le miroir iort.tn. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi2024-44",
      "type": "legislation",
      "title": "Loi n° 2024-44 du 12 août 2024, relative à l'organisation des congés de maternité et de paternité dans la fonction publique et les secteurs public et privé",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "99",
      "page": "2215",
      "issued": {"date-parts": [[2024, 8, 12]]},
      "URL": "https://www.pist.tn/jort/2024/2024F/Jo0992024.pdf",
      "note": "citation-key: loi2024-44\nJORT n° 99 du 12 août 2024, p. 2215 (pagination à confirmer, deux éditions coexistent). Art. 1 : agents CNRPS et salariés ET non-salariés du privé affiliés à la CNSS. Congé prénatal 15 jours, postnatal 3 mois (4 en cas de naissances multiples, handicap, prématurité ; 1 mois si enfant mort-né), paternité 7 jours (10 dans les cas aggravés, 3 si mort-né), congé d'accouchement 1 à 4 mois à demi-traitement, repos et congé d'allaitement. Plein traitement dans le public, indemnité dans le privé calculée « conformément à la législation en vigueur » (art. 9), c'est-à-dire l'art. 82 de la loi n° 60-30. Aucun article d'entrée en vigueur, aucun décret d'application prévu. Texte français intégral sur le miroir iort.tn. URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret-loi2024-4",
      "type": "legislation",
      "title": "Décret-loi n° 2024-4 du 22 octobre 2024, relatif au régime de protection sociale des travailleuses agricoles",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "129",
      "issued": {"date-parts": [[2024, 10, 22]]},
      "URL": "https://www.pist.tn/jort/2024/2024F/Jo1292024.pdf",
      "note": "citation-key: decret-loi2024-4\nJORT n° 129 du 23 octobre 2024. PAGINATION NON ÉTABLIE : jort_cache donne 5293-5293, valeur incompatible avec un texte de 48 articles et décrivant vraisemblablement l'édition arabe. Art. 1 et 17 : régime couvrant l'assurance maladie, les pensions, les risques professionnels et les prestations Amen Social ; gestion CNSS pour le régime de sécurité sociale (art. 18) et CNAM pour l'AT/MP (art. 39). Arts 20 et 23 et 42 : l'État prend en charge les cotisations pendant les trois premières années. Premier texte ouvrant la couverture AT/MP à des NON-SALARIÉES (arts 38-48). Art. 35 : non-cumul Amen Social / couverture sociale. Aucune prestation familiale. Texte français intégral sur le miroir iort.tn. URL vérifiée (HTTP 200)."
    },
    {
      "id": "decret74-463",
      "type": "legislation",
      "title": "Décret n° 74-463 du 11 avril 1974, portant octroi de l'indemnité dite majoration pour salaire unique à certaines catégories des personnels militaires",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "26",
      "page": "757",
      "issued": {"date-parts": [[1974, 4, 11]]},
      "URL": "https://www.pist.tn/jort/1974/1974F/Jo02674.pdf",
      "note": "citation-key: decret74-463\nJORT n° 26 des 12-16 avril 1974, p. 757. SEUL texte du corpus dont le TITRE porte l'expression « majoration pour salaire unique » — mais son dispositif ne la contient pas : l'article premier accorde aux militaires « les indemnités à caractère familial dans les mêmes conditions que les fonctionnaires de l'État », sous réserve de mariage réglementaire. Art. 3 : prend effet à compter du 1er janvier 1974. Lu à l'image. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi74-41",
      "type": "legislation",
      "title": "Loi n° 74-41 du 22 mai 1974, portant attribution du service du capital-décès à la Caisse nationale des retraites",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "36",
      "page": "1101",
      "issued": {"date-parts": [[1974, 5, 22]]},
      "URL": "https://www.pist.tn/jort/1974/1974F/Jo03674.pdf",
      "note": "citation-key: loi74-41\nJORT n° 36 du 24 mai 1974, p. 1101. Le même fascicule porte le décret n° 74-572 du 22 mai 1974 relatif au capital-décès, pp. 1108-1109, abrogé par l'art. 14 du décret n° 93-308. CONTENU NON LU ; métadonnées jort_cache. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi72-2",
      "type": "legislation",
      "title": "Loi n° 72-2 du 15 février 1972, portant réforme du régime de prévoyance sociale des fonctionnaires",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "7",
      "page": "189",
      "issued": {"date-parts": [[1972, 2, 15]]},
      "URL": "https://www.pist.tn/jort/1972/1972F/Jo00772.pdf",
      "note": "citation-key: loi72-2\nJORT n° 7 du 11 février 1972, p. 189. Texte de base du régime de prévoyance sociale des fonctionnaires (CNRPS), pendant public du chapitre « assurances sociales » de la loi n° 60-30. Modifiée notamment par la loi n° 97-60 du 28 juillet 1997 (art. 2 alinéa c nouveau, définition des enfants à charge). CONTENU NON LU ; métadonnées jort_cache. URL vérifiée (HTTP 200)."
    },
    {
      "id": "loi86-86",
      "type": "legislation",
      "title": "Loi n° 86-86 du 1er septembre 1986, portant réforme des structures de la sécurité sociale",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "49",
      "page": "977-980",
      "issued": {"date-parts": [[1986, 9, 1]]},
      "URL": "https://www.pist.tn/jort/1986/1986F/Jo04986.pdf",
      "note": "citation-key: loi86-86\nJORT n° 49 du 9 septembre 1986, pp. 977-980. Texte de création de la CNSS et de la CNRPS. CONTENU NON LU ; métadonnées jort_cache. URL vérifiée (HTTP 200)."
    },
    {
      "id": "circulaire-42-1996",
      "type": "regulation",
      "title": "Circulaire n° 42 du 25 octobre 1996, ayant pour objet la gestion des indemnités à caractère familial dans le secteur public",
      "container-title": "Journal officiel de la République tunisienne",
      "issue": "94",
      "page": "2349-2364",
      "issued": {"date-parts": [[1996, 10, 25]]},
      "URL": "https://www.pist.tn/jort/1996/1996F/Jo09496.pdf",
      "note": "citation-key: circulaire-42-1996\nJORT n° 94 du 22 novembre 1996, pp. 2349-2364 (16 pages). Source la plus détaillée sur la gestion des indemnités à caractère familial dans le secteur public. REPÉRÉE, NON LUE. URL vérifiée (HTTP 200)."
    }
  ]
}
```

---

## 13. Notions à porter au glossaire `precis/glossaire.yml`

Le fichier n'a **aucune** des notions ci-dessous ; il faut par ailleurs ajouter le livre
`prestations_sociales` à `BOOKS` dans `scripts/build_glossary.py` et lui poser une annexe dans les
**deux** `_quarto.yml` (plan §5, étape 4). Existent déjà : `cnss`, `cnrps`, `cnam`,
`cotisations-sociales`, `fonds-de-securite-sociale`, `smig`.

| `id` proposé | Terme FR | Terme AR (à valider) | Source canonique |
|---|---|---|---|
| `prestations-familiales` | Prestation familiale | المنح العائلية | **loi n° 60-30, art. 51** — les trois composantes |
| `allocation-familiale` | Allocation familiale | المنحة العائلية | loi n° 60-30, arts 52-65 ; loi n° 88-38 pour les taux |
| `indemnite-caractere-familial` | Indemnité à caractère familial | المنح ذات الصبغة العائلية | **loi n° 88-39** + décret n° 96-1906 |
| `majoration-salaire-unique` | Majoration pour salaire unique | منحة الأجر الوحيد | **loi n° 80-36, art. 65 bis** (section I bis de la loi n° 60-30) — statut `valide` |
| `contribution-frais-creche` | Contribution aux frais de crèche | المساهمة في مصاريف رياض الأطفال | **loi n° 94-88** et décret n° 95-114 |
| `indemnite-journaliere` | Indemnité journalière | التعويض اليومي | loi n° 60-30 art. 77 (maladie) ; loi n° 94-28 art. 35 (AT/MP) |
| `indemnite-de-couches` | Indemnité de couches | منحة الولادة | loi n° 60-30, arts 78-82 |
| `capital-deces` | Capital-décès | منحة الوفاة / رأس مال الوفاة | **décret n° 93-308** (public) ; loi n° 60-30 arts 83-87 pour l'indemnité de décès (privé) — **deux entrées distinctes recommandées** |
| `indemnite-de-deces` | Indemnité de décès | منحة الوفاة | loi n° 60-30, arts 83-87 |
| `assurances-sociales` | Assurances sociales | التأمينات الاجتماعية | loi n° 60-30, art. 68 — c'est la branche, pas l'assurance maladie |
| `accident-du-travail` | Accident du travail | حادث شغل | **loi n° 94-28, art. 3** |
| `maladie-professionnelle` | Maladie professionnelle | مرض مهني | loi n° 94-28, art. 3 |
| `rente-accident-travail` | Rente d'accident du travail | إيراد حادث الشغل | loi n° 94-28, arts 39-49 |
| `stage` (ou `stage-cotisation`) | Stage de cotisation | مدة الانخراط الدنيا | loi n° 60-30 arts 71 et 78 ; décret n° 95-1166 art. 17 |
| `ayant-droit` | Ayant droit | ذوو الحق | **loi n° 2004-71, art. 4** |
| `assure-social` | Assuré social | المضمون الاجتماعي | loi n° 2004-71, art. 4 |
| `rsna` | Régime des salariés non agricoles | نظام الأجراء غير الفلاحيين | loi n° 60-30 |
| `rsa` | Régime des salariés agricoles | نظام الأجراء الفلاحيين | loi n° 81-6, titres I-II |
| `rsaa` | Régime des salariés agricoles amélioré | النظام الفلاحي المحسّن | **loi n° 89-73**, titre III de la loi n° 81-6 |
| `rtns` | Régime des travailleurs non salariés | نظام العملة غير الأجراء | décret n° 95-1166 |
| `rtte` | Régime des travailleurs tunisiens à l'étranger | نظام العملة التونسيين بالخارج | décret n° 89-107 |
| `regime-bas-revenus` | Régime des travailleurs à bas revenu | نظام ذوي الدخل الضعيف | loi n° 2002-32 — statut `provisoire`, correspondance non attestée (L5) |
| `regime-artistes` | Régime des artistes, créateurs et intellectuels | نظام الفنانين والمبدعين والمثقفين | loi n° 2002-104 |
| `carence` | Délai de carence | فترة الانتظار | loi n° 60-30 art. 72 (20 jours, 3 pour longue durée) ; loi n° 94-28 art. 35 (3 jours) |
| `salaire-journalier-moyen` | Salaire journalier moyen | الأجر اليومي المتوسط | loi n° 60-30 arts 88-90 ; art. 88 nouveau, loi n° 98-91 |

---

## 14. Ce qu'il faut faire avant de rédiger

1. **Combler L6** — lire la dernière page de neuf textes pour établir les dates d'effet. Une heure.
2. **Combler L9** — lire l'article 34 de la loi n° 60-30 : c'est le pivot du champ RSNA, et il est
   visé par deux articles clés (52 et 69).
3. **Lire la circulaire n° 42 de 1996** (L10) : elle referme le §2.2 et confirmera le payeur.
4. **Trancher L2** — les montants de la majoration pour salaire unique (1980) et de la contribution
   aux frais de crèche (1994) sont-ils inchangés en 2026 ? — ou publier le résultat négatif en
   indiquant précisément la recherche effectuée, comme le précis l'a fait pour le PNAFN.
5. **Ne pas générer les tableaux openfisca avant d'avoir corrigé les dates.** Les treize valeurs de
   `prestations_familiales/` sont toutes datées `1960-01-01` alors qu'aucune ne date de 1960 : les
   taux sont de **1976**, le plafond de **1986**, la majoration pour salaire unique de **1980**, la
   contribution crèche de **1994**. Générer maintenant reproduirait quatre erreurs de date dans le
   livre. Les corrections chiffrées sont données au §2.1 sous forme de séries prêtes à encoder ; la
   PR de paramètres devrait aussi **créer** trois paramètres manquants (`af/taux/enf4`,
   `af/plancher_trim`, `af/nb_enfants_max`) sans lesquels la période 1976-1988 est inreprésentable.
