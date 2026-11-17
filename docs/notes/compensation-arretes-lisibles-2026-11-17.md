# Compensation : arrêtés et décrets lisibles au corpus local (17 novembre 2026)

Note du documentaliste. Volume « compensation », branche `compensation/produits-de-base-suite-2`.
Elle complète `compensation-produits-base-complements-2026-11-17.md` (§ 11, 12) et
`compensation-avant-1970-et-plans.md` (taxe de 1968). Rien n'est modifié dans le précis.

**Méthode.** Les intitulés viennent de `jort_cache.db`. Les fascicules sont ceux du corpus local
(`PDFs-legislation-tunisie/PDFs/JORT/<année>/fr/`). Ces fascicules de 1968 à 1992 n'ont **aucune
couche texte**. Chaque page utile a été rendue (`pdftoppm`) puis lue **à l'image**.

Niveaux de relecture :
- **[I+]** : chiffres relus sur un agrandissement de 300 à 600 points par pouce ;
- **[I]** : page lue à 120-130 points par pouce, lisible sans agrandissement ;
- **« I (note complémentaire) »** : lignes reprises telles quelles de
  `compensation-produits-base-complements-2026-11-17.md`, **non relues dans cette passe** ;
- **« I (relu) »** : décrets n° 75-352 et 79-413, relus à 120 points par pouce.

- Les pages sont celles de l'édition française.
- Les URL `pdf_fr` et `pdf_ar` sont les champs de `jort_cache`, préfixés par `https://www.pist.tn`.
  Les URL AR **n'ont pas été vérifiées en ligne**.
- **[méta]** : intitulé seul.

**Dates.**
- La date d'effet est celle que le texte énonce, reprise telle quelle (AGENTS.md, « Dater », 1).
- La publication est le numéro et les dates **imprimés sur le fascicule**. Le champ
  `date_publication` de `jort_cache` est antérieur à la signature pour le n° 52/1968 (« 1968-12-06 »
  pour un arrêté du 9) et pour le n° 32/1971 (« 1971-07-23 » pour un arrêté du 26). Ce champ n'est
  donc pas repris.

---

## 1. Taxe au profit de la Caisse et taxe unique de compensation sur les carburants

### 1.1 Arrêté du 9 décembre 1968 [I+]

**Texte.** Arrêté du secrétaire d'État au Plan et à l'Économie nationale du 9 décembre 1968, fixant
les prix des carburants. JORT n° 52 des 6-10 décembre 1968, p. 1291-1292.
- FR : https://www.pist.tn/jort/1968/1968F/Jo05268.pdf
- AR : https://www.pist.tn/jort/1968/1968A/Ja05268.pdf
- Clé **existante** : `arrete-1968-12-09-prix-carburants`, présente dans les `references.json` FR et AR de la compensation.

**Article 1er** (p. 1291) : « Le montant de la taxe prévue par l'article 1er de l'arrêté du
23 septembre 1966 est modifié comme suit :
- *Essence Supérieure* : ancien taux 1.750 millimes par hectolitre ; nouveau taux 2.500 millimes par hectolitre ;
- *Essence normale* : ancien taux 1.650 millimes par hectolitre ; nouveau taux 2.300 millimes par hectolitre.

Cette taxe est applicable pour les produits ci-dessus provenant d'une importation ou sortant d'une
usine exercée. »

**Autres articles.**
- **Art. 10, al. 2** (p. 1292) nomme la taxe : « Les produits des réévaluations dues à l'augmentation
  de la Taxe de Compensation visée à l'article 1 seront versés [...] aux Recettes des Finances [...].
  Les produits des réévaluations seront affectés à la Caisse de Compensation. »
- **Art. 12** (p. 1292) : « Le présent arrêté prend effet à compter du 10 décembre 1968. »

**Lecture.** Les deux anciens taux sont ceux que la figure attribue à l'arrêté du 23 septembre 1966.
La chaîne est donc continue. Correspondance avec les grandeurs de `TAXE_UNIQUE` :
- `t64_essence` = essence supérieure, 1,750 → **2,500 D/hl** ;
- `t64_essence_2` = essence normale, 1,650 → **2,300 D/hl** ;
- pétrole lampant et gas-oil : non visés (taxe supprimée le 25 septembre 1966, inchangée).

### 1.2 Décret n° 76-1123 du 31 décembre 1976 [I+]

**Objet.** Décret n° 76-1123 du 31 décembre 1976, modifiant et complétant le décret n° 70-622 du
31 décembre 1970 portant consolidation et simplification des droits et taxes perçus sur certains
produits pétroliers. JORT n° 83 du 31 décembre 1976, p. 3241.
- FR : https://www.pist.tn/jort/1976/1976F/Jo08376.pdf
- AR : https://www.pist.tn/jort/1976/1976A/Ja08376.pdf

**Ce que dit le texte.**
- **Art. 1er** : « Le montant de la taxe unique de compensation prévue à l'article 5 du décret
  sus-visé N° 70-622 [...] est modifiée comme suit ». Tableau : « Ex. 27-10 | Pétrole | Hl |
  néant » ; « Gaz-Oil | Hl | 0 D, 890 ».
- **Art. 2** : « Il est institué à compter du 1er janvier 1977, au profit de la Caisse Générale de
  Compensation, une taxe unique de compensation sur le fuel-oil léger dont le taux s'élève à
  6D,990 la tonne. »
- **Art. 3** : le décret « prend effet à compter du 1er janvier 1977 ».

**Ce que ce texte change à la figure.** **Ce décret est absent de `TAXE_UNIQUE`.**
- **Pétrole lampant.** La figure prolonge 0,036 D/hl du 1er janvier 1971 jusqu'en 1981. Or la taxe
  est **supprimée au 1er janvier 1977**, et le tracé est faux de 1977 à 1981.
- **Gas-oil.** La figure prolonge 0,235 D/hl jusqu'au 1er janvier 1981 (2,180). Il manque l'étape du
  **1er janvier 1977**, à 0,890 D/hl pour le gas-oil hors agriculture et pêche (voir § 1.3).

### 1.3 Décret n° 77-192 du 17 février 1977 [I]

**Objet.** Décret n° 77-192 du 17 février 1977, modifiant le décret n° 76-1123 du 31 décembre 1976.
JORT n° 13 du 22 février 1977, p. 464.
- FR : https://www.pist.tn/jort/1977/1977F/Jo01377.pdf
- AR : https://www.pist.tn/jort/1977/1977A/Ja01377.pdf

**Ce que dit le texte.**
- **Art. 1er** : « L'article premier du décret sus-visé N° 76-1123 du 31 décembre 1976, est abrogé
  et remplacé par les dispositions suivantes ». « Art. 1 (nouveau) » : la taxe unique de
  compensation est modifiée « conformément au tableau suivant ». Ex 27-10 :
  - « C — Pétrole | HL | Néant » ;
  - « Ex D — Gas-oil destiné aux travaux agricoles et à la pêche | HL | 0 D,235 » ;
  - « Gas-oil pour toutes autres utilisations | HL | 0 D,890 ».
- **Art. 2** : le décret « prend effet à compter du 1er janvier 1977 ». L'effet est **rétroactif** :
  signé le 17 février, publié le 22 février.

**Lecture.**
- Dès 1977, le gas-oil de l'agriculture et de la pêche garde l'ancien taux de 0,235. C'est l'origine
  du taux réduit que le décret n° 80-1641 porte à 1,525 en 1981.
- Ce taux réduit n'est pas tracé aujourd'hui. Pour le 1er janvier 1977, il faut une grandeur
  nouvelle, `tu_gasoil_agri`, ou une note de légende.

### 1.4 Décret n° 82-212 du 4 février 1982 [I+], postérieur à la fin actuelle de la figure

**Objet.** Décret n° 82-212 du 4 février 1982, modifiant et complétant le décret n° 70-622. JORT n° 8
du 9 février 1982, p. 294.
- FR : https://www.pist.tn/jort/1982/1982F/Jo00882.pdf
- AR : https://www.pist.tn/jort/1982/1982A/Ja00882.pdf

**Ce que dit le texte.**
- **Art. 1er** : « La taxe unique de compensation sur le fuel oil léger instituée par le décret
  susvisé n° 76-1123 [...] est fixée à 26D.,990 la tonne à partir du 5 janvier 1982. »
- **Art. 2** : il est institué, à compter du 5 janvier 1982 et au profit de la Caisse générale de
  compensation, « une taxe unique de compensation sur le fuel oil domestique dont le taux s'élève
  à 20D. 000 ». **L'unité n'est pas imprimée.**
- **Art. 3** : effet au 5 janvier 1982. L'effet est **rétroactif** : signé le 4 février, publié le
  9 février.
- **Visa** : le décret n° 76-1123, « notamment son article 2 ».

### 1.5 Décret n° 84-210 du 29 février 1984 [I+], second accès, postérieur à la figure

**Objet.** Décret n° 84-210 du 29 février 1984, modifiant le décret n° 70-622. JORT n° 15 des 2-6 mars
1984, p. 535.
- FR : https://www.pist.tn/jort/1984/1984F/Jo01584.pdf
- AR : https://www.pist.tn/jort/1984/1984A/Ja01584.pdf

**Ce que dit le texte.**
- **Art. 1er** : « Le montant de la taxe unique de compensation pour le Gaz-oil destiné aux travaux
  agricoles et à la pêche prévu par l'article 5 du décret n° 70-622 [sic : « 70-662 »] [...] est
  modifié comme suit : Gaz-oil destiné aux travaux agricoles et à la pêche | HL | 0,D025 ».
- **Art. 2** : effet « à compter du 22 février 1984 à zéro heure ». L'effet est **rétroactif**.
- **Visa** : le décret n° 70-622 « tel qu'il a été modifié ou complété par le décret n° 77-192 du
  17 février 1977, le décret n° 78-316 du 23 mars 1978 et le décret n° 80-1641 du 29 décembre
  1980 ».

**Lecture.** Le taux agricole tombe de 1,525 à **0,025 D/hl**.

### 1.6 Les modificatifs du décret n° 70-622, de 1971 à 1984

La série est désormais complète **selon les intitulés** :
- 74-576 ;
- 76-1123 ;
- 77-192 ;
- 78-316 ;
- 80-1641 ;
- 82-212 ;
- 84-210.

Ce relevé s'appuie sur deux accès :
1. une recherche sur l'intitulé et l'objet, `titre LIKE '%70-622%' OR objet LIKE '%70-622%'`, de
   1971 à 1992 ;
2. une recherche plein texte (FTS) `"taxe unique" AND compensation`, de 1964 à 1992.

Les « taxe unique de compensation » des lois de finances de 1984 à 1993 portent sur les
**transports routiers**. C'est un autre impôt.

La liste des modificatifs dans le visa de 84-210 n'est pas exhaustive : elle omet 74-576, qui
modifiait pourtant l'art. 5 pour l'essence, ainsi que 76-1123 et 82-212. Elle ne corrobore donc
rien.

### 1.7 Tuples prêts à transcrire (ne pas éditer ici ; `figures/transcriptions.py`, `TAXE_UNIQUE`)

```
("t64_essence",   "1968-12-10", 2.500, "arrêté du 9 décembre 1968", "arrete-1968-12-09-prix-carburants", "art. 1, p. 1291"),
("t64_essence_2", "1968-12-10", 2.300, "arrêté du 9 décembre 1968", "arrete-1968-12-09-prix-carburants", "art. 1, p. 1291"),
("tu_lampant",    "1977-01-01", None,  "décret n° 76-1123", "decret76-1123", "art. 1 et 3"),
("tu_gasoil",     "1977-01-01", 0.890, "décret n° 77-192",  "decret77-192",  "art. 1 (nouveau), p. 464"),
# taux réduit, grandeur nouvelle si on la trace :
("tu_gasoil_agri", "1977-01-01", 0.235, "décret n° 77-192",  "decret77-192",  "art. 1 (nouveau)"),
("tu_gasoil_agri", "1981-01-01", 1.525, "décret n° 80-1641", "decret80-1641", ""),
("tu_gasoil_agri", "1984-02-22", 0.025, "décret n° 84-210",  "decret84-210",  "art. 1 et 2, p. 535"),
```

**Points à arbitrer.**
- **`tu_gasoil` au 1er janvier 1977.** Le décret n° 76-1123 donne 0,890 sans distinction. Le décret
  n° 77-192 le remplace rétroactivement à la même date. Seul le second se cite donc pour la valeur.
- **Fuel-oil léger et fuel-oil domestique.** Leurs taux sont en D/t et ne se tracent pas sur l'axe
  en D/hl :
  - fuel-oil léger : 6,990 D/t au 1er janvier 1977, puis 26,990 D/t au 5 janvier 1982 ;
  - fuel-oil domestique : 20,000 au 5 janvier 1982, unité non imprimée.

  À citer en légende comme le fuel-oil lourd de 1980.
- **`TAXE_UNIQUE_FIN = 1981`.** Prolonger après 1981 demande de relire les tarifs essence et gas-oil
  après le décret n° 80-1641. Les décrets n° 82-212 et 84-210 ne touchent ni l'essence ni le gas-oil
  ordinaire. Aucun intitulé de 1981 à 1992 ne signale d'autre modificatif de l'art. 5 pour ces
  produits. Ce constat repose sur les seuls intitulés : ne pas en déduire que le tarif de 1981
  reste en vigueur après 1981.

**TODO de `_carburants.qmd` (l. 243).** La lecture est faite : l'arrêté du 9 décembre 1968 est lu
à l'image, et ses taux et son effet sont ci-dessus. **Reste le versement dans `TAXE_UNIQUE`.**

### 1.8 Textes rencontrés sur les mêmes pages (hors commande, utiles au volume)

- **Décret n° 76-1120 du 28 décembre 1976** (JORT n° 83/1976, p. 3241) [I]. Il porte institution
  d'une taxe compensatrice sur les exportations d'huile d'olive.
  - Art. 1er : « une taxe compensatrice fixée à 30 millimes par kilogramme d'huile d'olive exportée
    [...] retenue par l'Office National de l'huile ».
  - Art. 2 : elle est versée « au compte de la Caisse Générale de Compensation pour être affectée à
    la stabilisation du prix de vente en Tunisie de l'huile d'olive conditionnée pour la
    consommation ».
  - Art. 3 : abrogation du décret n° 74-876.
  - Art. 4 : effet au 1er janvier 1977.
  - **Changement d'objet et de taux** : en 1974, 80 m/kg, pour « les huiles de graine » ; en 1977,
    30 m/kg, pour « l'huile d'olive conditionnée ».
- **Décret n° 76-1124 du 31 décembre 1976** (même page) [I]. Il fixe le taux de la taxe de
  compensation due sur le ciment ensaché.
  - Art. 1er : « deux (2) dinars la tonne », « perçue au profit de la Caisse Générale de
    Compensation ».
  - Art. 2 : effet « à compter du 1er janvier **1976** », tel qu'imprimé, soit un an de rétroactivité
    et peut-être une coquille.
  - Visa : loi n° 75-83 (loi de finances pour 1976), art. 67.

---

## 2. Produits de base : tableaux par produit

**Lecture des colonnes.**
- **« Prix »** : le prix au public (détail), sauf mention.
- **Les autres stades** (producteur ou usine, gros, détaillant) figurent dans « Autres stades ».
- **Unités** : celles du texte, recopiées. Une conversion est marquée « calculé ».

### 2.1 Sucre (prix du kilogramme)

| Effet (énoncé) | Poudre : détail | Morceaux : détail | Autres stades (poudre ; morceaux) | Texte | JORT, page | Lecture |
|---|---|---|---|---|---|---|
| 31.5.1975 | 200 M | 300 M | 186 / 190 ; 286 / 290 | arrêté du 3.6.1975 | n° 38/1975, p. 1191 | I (note complémentaire) |
| **23.1.1980 à zéro heure** | **0,240 D/kg** | **0,340 D/kg** | grossistes 0,221 / détaillants 0,226 ; 0,326 / 0,330 | arrêté du ministre du commerce du 20.2.1980, portant fixation des prix de vente du sucre et du café | n° 12 du 26.2.1980, p. 558 | I+ |
| **25.11.1986** | **270 Mil.** | **370 Mil** | producteur 246 / gros 252 ; 346 / 352 | arrêté du ministre de l'industrie et du commerce du 22.11.1986, portant fixation du prix de vente maximum du sucre | n° 68 du 25.11.1986, p. 1337 | I+ |
| **1.7.1988** | **300 mil** | **400 mil** | 276 / 282 ; 357 / 364 | arrêté du ministre de l'industrie et du commerce du 8.9.1988, portant fixation du prix de vente du sucre | n° 61 du 16.9.1988, p. 1274 | I+ |
| **12.8.1989** | **350** | **500** | 326 / 332 ; 433 / 450 | arrêté du ministre de l'économie nationale du 11.11.1989, portant fixation du prix de vente du sucre | n° 77 des 17-21.11.1989, p. 1822 | I+ |
| **13.7.1990** | **400 mil** (« sucre blanc en poudre ») | **560 mil** | 376 / 382 ; 490 / 510 | arrêté du ministre de l'économie et des finances du 18.7.1990, portant fixation des prix de vente du sucre | n° 49 du 24.7.1990, p. 982 | I+ |
| **17.6.1991** | **430 mil.** | **620 mil.** | 395 / 405 ; 538 / 560. **Sucre brun** (nouveau) : 265 / 275 / **300 mil.** | arrêté du ministre de l'économie nationale du 25.6.1991, portant fixation des prix de vente du sucre | n° 48 du 5.7.1991, p. 1251 | I+ |

**Ce que disent les articles.**
- **1980**, art. 1er : « A compter du mercredi 23 janvier 1980 à zéro heure, les prix de vente du
  sucre et du café sont fixés comme suit ».
  - Café torréfié : 2,840 / 2,890 / 3,000 D/kg.
  - Art. 3 : redevances différentielles à la Caisse générale de compensation de 0,040 D/kg, poudre
    et morceaux, à chaque stade.
  - L'effet (23 janvier) est **antérieur à la signature** (20 février) et à la publication
    (26 février).
- **1986**, art. 1er : « A compter du 25 novembre 1986 les prix de vente d'un kilogramme de sucre
  sont fixés ». L'effet coïncide avec la publication.
- **1988**, art. 1er : « A compter du 1er juillet 1988 les prix de vente du kilogramme de sucre ».
  Art. 2 : déclaration des stocks « à compter du 30 juin 1988 à zéro heure ». L'effet est
  **rétroactif** de deux mois et demi.
- **1989**, art. 1er : « A compter du 12 août 1989 ». Le tableau n'imprime pas d'unité ; l'article
  dit « du kilogramme ». L'effet est **rétroactif** : publication le 17 novembre.
- **1990**, art. 1er : « A compter du 13 juillet 1990 ». L'effet est **antérieur à la signature**
  (18 juillet).
- **1991**, art. 1er : « A compter du 17 juin 1991 ». L'art. 2 imprime « A compter du 17 juin
  **1990** à zéro heure » pour la déclaration de stock, coquille probable du texte officiel. **Son
  visa cite l'arrêté du 11 novembre 1989, non celui du 18 juillet 1990.**

**Chaîne des visas** : 1975 → 1980 → 1986 → 1988 → 1989 → (1990) → 1991.
- Elle corrobore qu'aucun arrêté du sucre ne manque de 1975 à 1991, sans le prouver.
- Le chaînon de 1990 est sauté par le visa de 1991.

**Produit défini.**
- Jusqu'en 1989 : « sucre en poudre » et « sucre en morceaux ».
- Depuis 1990 : « sucre blanc en poudre », « sucre blanc en morceaux ».
- En 1991 : « sucre brun » en plus.
- Aucun conditionnement n'est précisé.

**Sources (champs `pdf_fr` / `pdf_ar` de `jort_cache` ; AR non vérifiées en ligne)** :
- 1975, n° 38 : FR https://www.pist.tn/jort/1975/1975F/Jo03875.pdf ; AR https://www.pist.tn/jort/1975/1975A/Ja03875.pdf
- 1980, n° 12 : FR https://www.pist.tn/jort/1980/1980F/Jo01280.pdf ; AR https://www.pist.tn/jort/1980/1980A/Ja01280.pdf
- 1986, n° 68 : FR https://www.pist.tn/jort/1986/1986F/Jo06886.pdf ; AR https://www.pist.tn/jort/1986/1986A/Ja06886.pdf
- 1988, n° 61 : FR https://www.pist.tn/jort/1988/1988F/Jo06188.pdf ; AR https://www.pist.tn/jort/1988/1988A/Ja06188.pdf
- 1989, n° 77 : FR https://www.pist.tn/jort/1989/1989F/Jo07789.pdf ; AR https://www.pist.tn/jort/1989/1989A/Ja07789.pdf
- 1990, n° 49 : FR https://www.pist.tn/jort/1990/1990F/Jo04990.pdf ; AR https://www.pist.tn/jort/1990/1990A/Ja04990.pdf
- 1991, n° 48 : FR https://www.pist.tn/jort/1991/1991F/Jo04891.pdf ; AR https://www.pist.tn/jort/1991/1991A/Ja04891.pdf

### 2.2 Huile de mélange, puis huile de graines (vrac)

| Effet (énoncé) | Détail | Autres stades | Texte | JORT, page | Lecture |
|---|---|---|---|---|---|
| 31.5.1975 | 200 m/litre | 200 m/kg (grossistes, rendu chef-lieu de délégation) ; 204 m/kg (détaillants) | arrêté du 3.6.1975 | n° 38/1975, p. 1189-1190 | I (note complémentaire) |
| **3.5.1979** | **250 M/Litre** | 250 M/KG rendue chef-lieu de délégation ; 255,5 M/KG des grossistes aux détaillants | arrêté du ministre du commerce du 7.5.1979, portant fixation du prix de l'huile mélangée | n° 32 du 11.5.1979, p. 1383 | I+ |
| **23.1.1980 à zéro heure** | **0d,300/litre** | 0d,300 le kg rendu chef-lieu de délégation ; 0d,307/kg | arrêté du ministre du commerce du 21.1.1980, portant fixation du prix de l'huile mélangée | n° 21 du 4.4.1980, p. 1021 | I+ |
| **7.12.1986** | **320 mil/litre** | producteur 319 mil/kg ; gros 329 mil/kg | arrêté du ministre de l'industrie et du commerce du 29.12.1986, portant fixation du prix de vente maximum de l'huile de mélange vrac | n° 1 des 2-6.1.1987, p. 14 | I+ |
| 12.8.1989 | 340 mil/litre | 338 / 348 | arrêté du 11.11.1989 | n° 77/1989, p. 1823 | I (note complémentaire) |
| **17.8.1991** | **370 millimes/litre** (« huile de graine en vrac ») | producteur 369 millimes/kg ; gros 380 millimes/kg | arrêté du ministre de l'économie nationale du 15.8.1991, portant fixation des prix de vente de l'huile de graines en vrac | n° 61 des 3-6.9.1991, p. 1546-1547 | I+ |

**Ce que disent les articles.**
- **1979** : art. 1er, « A compter du 3 mai 1979 ». Art. 3 : redevances à la Caisse générale de
  compensation, 51,5 M/KG pour les grossistes et 50 M/Litre pour les détaillants. Visa : arrêté du
  3 juin 1975.
- **1980** : art. 1er, « A compter du 23 janvier 1980 à zéro heure ».
  - Art. 3 : redevances de « 0d,0?0/kg » et « 0d,0?0/litre ». L'impression hésite entre 050 et 060
    même à 600 points par pouce ; « 050 » est la lecture probable (50 M en 1979).
  - Visa : arrêté du 7 mai 1979.
  - Publication le 4 avril 1980, plus de deux mois après l'effet.
- **1986** : art. 1er, « A compter du 7 décembre 1986 ». Mais l'art. 2 impose la déclaration des
  stocks « à compter du 10 décembre 1986 à zéro heure ». Les deux dates diffèrent dans le texte
  même : retenir le 7 décembre (art. 1er) et signaler l'écart. Visa : arrêté du 21 janvier 1980.
- **1991** : art. 1er, « A compter du 17 août 1991 ». Le produit change de nom : « huile de graines
  en vrac », non plus « huile de mélange ».

**Chaîne des visas** : 1975 → 1979 → 1980 → 1986 (→ 1989 → 1991).

**Sources (champs `pdf_fr` / `pdf_ar` de `jort_cache` ; AR non vérifiées en ligne)** :
- 1975, n° 38 : FR https://www.pist.tn/jort/1975/1975F/Jo03875.pdf ; AR https://www.pist.tn/jort/1975/1975A/Ja03875.pdf
- 1979, n° 32 : FR https://www.pist.tn/jort/1979/1979F/Jo03279.pdf ; AR https://www.pist.tn/jort/1979/1979A/Ja03279.pdf
- 1980, n° 21 : FR https://www.pist.tn/jort/1980/1980F/Jo02180.pdf ; AR https://www.pist.tn/jort/1980/1980A/Ja02180.pdf
- 1987, n° 1 : FR https://www.pist.tn/jort/1987/1987F/Jo00187.pdf ; AR https://www.pist.tn/jort/1987/1987A/Ja00187.pdf
- 1989, n° 77 : FR https://www.pist.tn/jort/1989/1989F/Jo07789.pdf ; AR https://www.pist.tn/jort/1989/1989A/Ja07789.pdf
- 1991, n° 61 : FR https://www.pist.tn/jort/1991/1991F/Jo06191.pdf ; AR https://www.pist.tn/jort/1991/1991A/Ja06191.pdf

### 2.3 Farines (D/q sauf mention)

| Effet (énoncé) | Produit | Valeur | Stade | Texte | JORT, page | Lecture |
|---|---|---|---|---|---|---|
| **1.8.1971** | Farine panifiable de blé tendre extraite à PS + 10 | **6d,100** | non dit. L'arrêté modifie l'art. 1er de l'arrêté du 10.8.1967, non lu ; unité non imprimée | arrêté **des ministres de l'économie nationale et de l'agriculture** du 26.7.1971, modifiant l'arrêté du 10 août 1967 fixant le prix des farines et semoules | n° 32 des 23-27.7.1971, p. 1002 | I+ |
| 1.8.1971 | Farine panifiable de blé tendre extraite à PS − 2 | **6d,540** | idem | idem | idem | I+ |
| 31.5.1975 | PS-2 ; PS + 10 | 7D,350 ; 6D,795 | « au quintal net, nu, rendu au chef lieu de la délégation » | décret n° 75-352, art. 1er | n° 38/1975, p. 1192 | I (relu) |
| 3.5.1979 | PS-2 | 8,650D | « au quintal net, nu, rendu au chef lieu de la délégation » | décret n° 79-413, art. 1er | n° 32 du 11.5.1979, p. 1381 | I (relu ; était [M]) |
| **12.8.1989** | Farine de blé tendre extraite à PS-7, vrac par kg | **245 mil** (détail) | chef-lieu de délégation 220 ; gros 225 | arrêté du ministre de l'économie nationale du 11.11.1989, portant fixation du prix de vente de la farine extraite à PS-7 | n° 77/1989, p. 1821 | I+ |
| 12.8.1989 | PS-7, paquet 1 kg | **290 mil** | 258 ; 264 | idem | idem | I+ |

**Réserves.**
- **L'unité de 1971 n'est pas imprimée** (« 6d,100 »). Elle se déduit seulement par la continuité
  avec 1975, où le texte dit « au quintal ». Le visa du décret n° 75-352 cite « l'arrêté du 10 août
  1967, modifié par l'arrêté du 26 juillet 1971, fixant le prix des farines et semoules ».
- **Ministère.** `jort_cache` attribue l'arrêté de 1971 au seul ministère de l'Agriculture. Le texte
  est conjoint ; ses signataires sont Tijani Chelli et Abdallah Farhat.
- **Correction de la note complémentaire, § 12.3.** Ce tableau donne les farines et semoules de 1975
  et 1979 comme « prix de détail ». Les décrets n° 75-352 et 79-413 disent « rendu au chef lieu de
  la délégation » pour les farines et « rendu fabrique ou magasin » pour les semoules de 1975. **Ce
  ne sont pas des prix au public.** Ne pas les chaîner avec les prix de détail de 1984 et 1989.
- **PS-7 de 1989.** Visa : arrêté du 17 février 1984 fixant le prix des farines. Il n'y a donc pas
  d'arrêté des farines entre février 1984 et août 1989, sous la même réserve de méthode.

**Sources (champs `pdf_fr` / `pdf_ar` de `jort_cache` ; AR non vérifiées en ligne)** :
- 1971, n° 32 : FR https://www.pist.tn/jort/1971/1971F/Jo03271.pdf ; AR https://www.pist.tn/jort/1971/1971A/Ja03271.pdf
- 1975, n° 38 : FR https://www.pist.tn/jort/1975/1975F/Jo03875.pdf ; AR https://www.pist.tn/jort/1975/1975A/Ja03875.pdf
- 1979, n° 32 : FR https://www.pist.tn/jort/1979/1979F/Jo03279.pdf ; AR https://www.pist.tn/jort/1979/1979A/Ja03279.pdf
- 1989, n° 77 : FR https://www.pist.tn/jort/1989/1989F/Jo07789.pdf ; AR https://www.pist.tn/jort/1989/1989A/Ja07789.pdf

### 2.4 Semoule de blé dur PS-10

| Effet (énoncé) | Détail | Autres stades | Unité imprimée | Texte | JORT, page | Lecture |
|---|---|---|---|---|---|---|
| **10.7.1984** | **15D,500 le quintal** | rendu chef-lieu de délégation 13D,440 ; gros 13D,800 | D/q | arrêté du ministre de l'économie nationale du 10.7.1984, fixant les prix des semoules (« semoules de blé dur extraites à P.S. 10 ») | n° 43 des 17-20.7.1984, p. 1595 | I+ |
| 12.8.1989 | 17,500 | 15,440 / 15,800 | D/q | arrêté du 11.11.1989 | n° 77/1989, p. 1824-1825 | I (note complémentaire) |
| **17.8.1991** | **205 mil** (vrac 1 kg) | producteur rendu chef-lieu 180 mil ; gros 185 mil | **mil par kg** (soit 20,500 D/q, calculé) | arrêté du ministre de l'économie nationale du 15.8.1991, portant fixation des prix de vente de la semoule PS-10 | n° 61 des 3-6.9.1991, p. 1546 | I+ |

**Ce que disent les articles.**
- **1984**, art. 1er : « A compter du 10 juillet 1984 ».
  - Art. 3 : redevances différentielles à la Caisse générale de compensation, à verser le 25 juillet.
  - Visas : décret n° 84-153 du 17 février 1984, qui abroge le décret n° 79-413 ; décret n° 84-150 ;
    arrêté du 17 février 1984 fixant les prix des semoules.
  - Publication : 17 juillet 1984.
- **1991**, art. 1er : « A compter du 17 août 1991 ». **L'unité change** : le quintal jusqu'en 1989,
  le kilogramme vrac en 1991.

**Sources (champs `pdf_fr` / `pdf_ar` de `jort_cache` ; AR non vérifiées en ligne)** :
- 1984, n° 43 : FR https://www.pist.tn/jort/1984/1984F/Jo04384.pdf ; AR https://www.pist.tn/jort/1984/1984A/Ja04384.pdf
- 1989, n° 77 : FR https://www.pist.tn/jort/1989/1989F/Jo07789.pdf ; AR https://www.pist.tn/jort/1989/1989A/Ja07789.pdf
- 1991, n° 61 : FR https://www.pist.tn/jort/1991/1991F/Jo06191.pdf ; AR https://www.pist.tn/jort/1991/1991A/Ja06191.pdf

### 2.5 Pâtes alimentaires et couscous (prix de détail ; millimes, unité non imprimée dans les tableaux de 1984 et 1989)

| Effet | Pâtes PS-10 vrac 1 kg | Couscous PS-10 vrac 1 kg | Autres conditionnements (détail) | Texte | JORT, page | Lecture |
|---|---|---|---|---|---|---|
| 31.5.1975 | 113 (gros 105) | 120 (gros 112) | — ; « au kg, en vrac », semoule PS, « dans le périmètre communal de Tunis » | décret n° 75-352 | n° 38/1975, p. 1192 | I (relu) |
| 3.5.1979 | 0,125 D (gros 0,115) | 0,135 D (gros 0,123) | « au kg, en vrac », semoule PS, « rendu au chef lieu de la délégation » | décret n° 79-413, art. 1er | n° 32/1979, p. 1381 | I (relu ; était [M]) |
| **10.7.1984** | **200** (usine 175 ; gros 180) | **208** (183 ; 188) | Pâtes : papier 1 kg 225 ; cellophane 1 kg 270, ½ kg 140, ¼ kg 73 ; cheveux d'ange 330 (la ligne « cannuloni, lasagne, marguerite » n'a pas de prix). Couscous : paquet 1 kg 230, ½ kg 120 | arrêté du ministre de l'économie nationale du 10.7.1984, fixant les prix de vente des pâtes et couscous rapide | n° 43/1984, p. 1595-1596 | I+ |
| 30.8.1986 | 240 | 250 | — | arrêté du 29.8.1986 | n° 50/1986, p. 1019-1020 | I (note complémentaire) |
| **12.8.1989** | **260** (producteur rendu chef-lieu 235 ; gros 240) | **300** (273 ; 278) | Pâtes : papier 1 kg 315 ; cellophane 1 kg 360, ½ kg 185, ¼ kg 100 ; cheveu d'ange, cannoli, lasagne, marguerite en cellophane 420. Couscous : papier 1 kg 320, ½ kg 165 ; cellophane 1 kg 340 | arrêté du ministre de l'économie nationale du 11.11.1989, portant fixation du prix de vente des pâtes alimentaires et couscous rapide | n° 77/1989, p. 1822-1823 | I+ |
| 17.8.1991 | 300 | 340 | — | arrêté du 15.8.1991 | n° 61/1991, p. 1545-1546 | I (note complémentaire) |

**Ce que disent les articles.**
- **1984** : art. 1er, « A compter du 10 juillet 1984 », avec la mention « rendu chef lieu de
  délégation ». Visas : arrêté du 17 février 1984 fixant les prix de vente maximum des pâtes et
  couscous rapide.
- **1989** : art. 1er, « A compter du 12 août 1989 ». Visa : arrêté du 29 août 1986. Il n'y a donc
  pas d'arrêté des pâtes entre 1986 et 1989, sous la même réserve.

**Sources (champs `pdf_fr` / `pdf_ar` de `jort_cache` ; AR non vérifiées en ligne)** :
- 1975, n° 38 : FR https://www.pist.tn/jort/1975/1975F/Jo03875.pdf ; AR https://www.pist.tn/jort/1975/1975A/Ja03875.pdf
- 1979, n° 32 : FR https://www.pist.tn/jort/1979/1979F/Jo03279.pdf ; AR https://www.pist.tn/jort/1979/1979A/Ja03279.pdf
- 1984, n° 43 : FR https://www.pist.tn/jort/1984/1984F/Jo04384.pdf ; AR https://www.pist.tn/jort/1984/1984A/Ja04384.pdf
- 1986, n° 50 : FR https://www.pist.tn/jort/1986/1986F/Jo05086.pdf ; AR https://www.pist.tn/jort/1986/1986A/Ja05086.pdf
- 1989, n° 77 : FR https://www.pist.tn/jort/1989/1989F/Jo07789.pdf ; AR https://www.pist.tn/jort/1989/1989A/Ja07789.pdf
- 1991, n° 61 : FR https://www.pist.tn/jort/1991/1991F/Jo06191.pdf ; AR https://www.pist.tn/jort/1991/1991A/Ja06191.pdf

### 2.6 Rectificatif du décret n° 75-352 [I+]

**Texte.** Rectificatif au décret n° 75-352 du 3 juin 1975. JORT n° 57 des 26-29 août 1975, p. 1814.
- FR : https://www.pist.tn/jort/1975/1975F/Jo05775.pdf
- AR : https://www.pist.tn/jort/1975/1975A/Ja05775.pdf

**Citation.** « RECTIFICATIF au J.O.R.T. N° 38 des 3 et 6 juin 1975 page 1192, 2e colonne. Article
Premier. — Pâtes alimentaires et couscous rapide.
- Au lieu de : Les prix de vente [...] pourront être librement fixés à tous les stades de la
  production et de la distribution.
- Lire : Les prix de vente [...] sont fixés à tous les stades de la production et de la distribution
  par le Ministre de l'Economie Nationale conformément à la loi N° 70-26 du 19 mai 1970 et au décret
  N° 70-543 du 24 octobre 1970. »

**Phrase visée** (p. 1192, 2e colonne, lue) : « Les prix de vente des pâtes alimentaires et du
couscous rapide, fabriqués avec des semoules de qualité extraite à PS-18, pourront être librement
fixés à tous les stades de la production et de la distribution. »

**Portée.** Les pâtes et couscous de semoule PS-18, produit de qualité en paquets, passent de la
liberté des prix à la fixation par le ministre. Cela se fait par rectificatif, près de trois mois
après le décret. Le décret n° 79-413 reprend cette règle : « seront fixés par arrêté aux stades de
la production et de la distribution ».

### 2.7 Lait régénéré (prix de vente public)

| Effet (énoncé) | Produit défini | Public | Autres stades | Texte | JORT, page | Lecture |
|---|---|---|---|---|---|---|
| **22.11.1982** | « Lait à 3mg [sic] de matière grasse » | 200 M. le litre | — | arrêté du ministre de l'économie nationale du 21.11.1982, fixant le prix de vente public du lait régénéré | n° 76 du 30.11.1982, p. 2581 | I+ |
| 22.11.1982 | Lait pasteurisé en tétra-brik d'un litre | **240 M.** le litre | — | idem | idem | I+ |
| 22.11.1982 | Lait pasteurisé en tétra-brik d'un demi-litre | **130 M.** (imprimé « le litre » ; prix du demi-litre) | — | idem | idem | I+ |
| 22.11.1982 | Lait stérilisé en bouteille d'un litre | 240 M. le litre | — | idem | idem | I+ |
| 22.11.1982 | Lait U.H.T. en tétra-brik d'un litre | **260 M.** le litre | — | idem | idem | I+ |
| 12.8.1989 | demi-écrémé : UHT tétrabrik 1 l ; pasteurisé tétrabrik 1 l | 380 ; 310 | — | arrêté du 11.11.1989 | n° 77/1989, p. 1824 | I (note complémentaire) |
| **22.7.1991** | demi-écrémé : pasteurisé 1 l | **350 mil** | usine rendu TTC 323 ; détaillants 330 | arrêté du ministre de l'économie nationale du 30.7.1991, fixant les prix de vente du lait régénéré demi-écrémé | n° 57 du 16.8.1991, p. 1451 | I+ |
| 22.7.1991 | pasteurisé ½ l | 175 mil | 161,5 ; 165 | idem | idem | I+ |
| 22.7.1991 | stérilisé en bouteille 1 l | 380 mil | 353 ; 360 | idem | idem | I+ |
| 22.7.1991 | U.H.T. en tétra-brik 1 l | **440 mil** | 413 ; 420 | idem | idem | I+ |

**Ce que disent les articles.**
- **1982**, art. 1er : « A partir du 22 novembre 1982, le prix de vente public du lait régénéré est
  fixé ». L'effet est **rétroactif** : publication le 30 novembre.
  - Visas : loi n° 70-26 ; décret n° 82-134 ; avis du Comité national des prix. Aucun arrêté
    antérieur sur le lait n'est visé.
  - Le texte dit « lait régénéré », **sans « demi-écrémé »**. La comparabilité avec 1989 et 1991 est
    à signaler.
- **1991**, art. 1er : « A compter du 22 juillet 1991 ». Mais l'art. 3 dit : « cet arrêté est
  d'application immédiate ». Retenir le 22 juillet (énoncé) et signaler la contradiction interne.
  Signature : 30 juillet ; publication : 16 août.
  - La date d'effet « à relire » de la note complémentaire est donc le **22 juillet 1991**.

**Sources (champs `pdf_fr` / `pdf_ar` de `jort_cache` ; AR non vérifiées en ligne)** :
- 1982, n° 76 : FR https://www.pist.tn/jort/1982/1982F/Jo07682.pdf ; AR https://www.pist.tn/jort/1982/1982A/Ja07682.pdf
- 1989, n° 77 : FR https://www.pist.tn/jort/1989/1989F/Jo07789.pdf ; AR https://www.pist.tn/jort/1989/1989A/Ja07789.pdf
- 1991, n° 57 : FR https://www.pist.tn/jort/1991/1991F/Jo05791.pdf ; AR https://www.pist.tn/jort/1991/1991A/Ja05791.pdf

---

## 3. Prix réduits de rétrocession de la récolte 1990 (décret n° 91-943, art. 8)

Fiche existante : `r-comp-pb-arrete-reduit-1991`. Le registre n'a pas été modifié (`recherches.py` non lancé), pour ne toucher qu'à cette note.

**Conclusion.** Aucun arrêté fixant les prix réduits de rétrocession de la récolte 1990 n'apparaît,
de juillet 1991 à décembre 1992, dans aucune des quatre sources parcourues. **C'est un constat sur
les sources parcourues, non une preuve d'inexistence.**

**Ce qui a été parcouru.**
1. **`jort_cache`, intitulés** (date de publication du 1er juin 1991 au 31 mars 1993) :
   - mots « céréal », « blé », « minot », « semoul », « farine », « rétrocession »,
     « compensation » ;
   - puis la liste complète des arrêtés des ministres de l'économie nationale, du commerce et de
     l'agriculture du 1er juillet 1991 au 31 décembre 1992.

   Seuls résultats pertinents :
   - les décrets n° 91-943 et 92-1657 ;
   - les décrets n° 92-99 et 92-801 : suspension des droits de douane et de la TVA à l'importation
     du blé et de l'orge ;
   - l'arrêté du 7 juillet 1992 relevant les prévisions du fonds spécial « Caisse générale de
     compensation » (clé existante `arrete-1992-07-07-cgc`) ;
   - les arrêtés de prix des 25 juin, 30 juillet et 15 août 1991 (§ 2).
2. **Sommaires des fascicules FR, océrisés** (tesseract, fra, 200 points par pouce) :
   - pages 1 à 3 des n° 47 à 90 de 1991 (44 fascicules) et des n° 1 à 88 de 1992 (88 fascicules) ;
   - ces fascicules n'ont pas de couche texte.

   Le contrôle de couverture compare la plus haute page citée par le sommaire océrisé à la dernière
   page connue de `jort_cache` pour le numéro. Deux écarts seulement :
   - n° 47/1991 : numéros de page détachés des lignes par l'OCR, mais les intitulés sont présents ;
   - n° 29/1992 : arrêtés de la santé publique, p. 564-567.

   Recherche : `blé`, `céréale`, `rétrocession`, `minot`, `semoul`, `farine`, `prix réduit`, `prix`,
   et lecture des rubriques « Ministère de l'Economie Nationale » et « Ministère de l'agriculture ».
   Aucun arrêté de prix réduits.
3. **Miroir iort (AR)**, fichiers `*_1991.md` et `*_1992.md` (991 fiches), intitulé arabe filtré sur
   قمح, الحبوب, التعويض, إحالة, المطاحن. Seuls résultats : `dec_91_943_1991`, `dec_92_1657_1992`,
   `dec_92_801_1992`, `dec_92_99_1992`. Le miroir ne compte que 232 arrêtés, toutes années
   confondues : il couvre mal la catégorie cherchée.
4. **Seconde voie : les visas du décret n° 92-1657** (JORT n° 66 du 2 octobre 1992, p. 1310) [I].
   - Ils citent : le décret du 28 juin 1945 [imprimé « 1954 »] ; la loi n° 86-106, art. 17 ; la loi
     n° 91-64 du 29 juillet 1991 relative à la concurrence et aux prix ; le décret n° 1083 du
     26 juin 1990 ; le décret n° 91-943.
   - **Aucun arrêté de prix réduits n'y figure.** C'est une corroboration, non une preuve.

**Passe à consigner** sur `r-comp-pb-arrete-reduit-1991` (commande à lancer par le rôle qui tient
le registre) :

```
uv run python scripts/recherches.py passe r-comp-pb-arrete-reduit-1991 --resultat aucun \
  --couvert-jusqu-au 1992-12-31 --sources jort_cache corpus_local iort visas \
  --couverture "Intitulés jort_cache (1.6.1991-31.3.1993 ; mots blé, céréal, minot, semoul, farine, rétrocession, compensation ; liste complète des arrêtés économie nationale, commerce, agriculture 1.7.1991-31.12.1992). OCR (fra, 200 dpi) des pages 1-3 des sommaires FR n° 47-90/1991 et 1-88/1992 ; couverture contrôlée par la dernière page citée (écarts : n° 47/1991, mise en page OCR ; n° 29/1992, santé). Miroir iort *_1991/*_1992 (991 fiches ; 232 arrêtés seulement dans tout le miroir). Visas du décret 92-1657 (p. 1310, image) : aucun arrêté de prix réduits. Lacunes : corps des fascicules non océrisé ; éditions AR des fascicules non lues."
```

**Termes à ajouter à `iort_ar`** (avec `elargir`) : `الحبوب` et `أسعار الإحالة`.

**La lecture la plus probable.** Le prix réduit de la récolte 1990 a été fixé par une décision non
publiée. Ce serait déjà la pratique que le décret n° 92-1657 rend explicite pour 1991 (« décision du
Ministre », note complémentaire § 1.4). **Inférence à ne pas écrire comme établie.**

---

## 4. Références CSL-JSON candidates

**Les 24 clés nouvelles ont été vérifiées absentes**, une à une, de tous les `precis/*/references.json`
et `precis/*/*/references.json`, de `biblio-a-rapatrier.md` et des notes `compensation-*.md`.

**Clés déjà présentes, à ne pas recréer** :
- `arrete-1968-12-09-prix-carburants` ;
- `decret70-622` ;
- `decret80-1641` ;
- `decret75-352` ;
- `arrete-1975-06-03-prix-sucre` ;
- `arrete-1975-06-03-prix-huile` ;
- `arrete-1989-11-11-prix-lait` ;
- `arrete-1989-11-11-prix-pain` ;
- `arrete-1991-07-30-prix-lait`. Pour cette dernière, compléter la `note` : effet énoncé au
  22 juillet 1991, art. 3 « d'application immédiate », image lue.

Modèle des notices : celui de `decret80-1641` dans `precis/fr/compensation/references.json`.

```json
{"id":"decret76-1123","type":"legislation","title":"Décret n° 76-1123 du 31 décembre 1976 modifiant et complétant le décret n° 70-622 du 31 décembre 1970 portant consolidation et simplification des droits et taxes perçus sur certains produits pétroliers","container-title":"Journal officiel de la République tunisienne","issue":"83","page":"3241","issued":{"date-parts":[[1976,12,31]]},"title-short":"Décret n° 76-1123 du 31 décembre 1976","URL":"https://www.pist.tn/jort/1976/1976F/Jo08376.pdf","note":"citation-key: decret76-1123\nJORT n° 83 du 31 décembre 1976, p. 3241. Taxe unique de compensation : pétrole « néant », gas-oil 0,890 D/hl (art. 1er) ; fuel-oil léger 6,990 D/t (art. 2) ; effet au 1er janvier 1977 (art. 3). Art. 1er remplacé par le décret n° 77-192. Preuve : image lue (p. 3241)."}
{"id":"decret77-192","type":"legislation","title":"Décret n° 77-192 du 17 février 1977 modifiant le décret n° 76-1123 du 31 décembre 1976 portant consolidation et simplification des droits et taxes perçus sur certains produits pétroliers","container-title":"Journal officiel de la République tunisienne","issue":"13","page":"464","issued":{"date-parts":[[1977,2,17]]},"title-short":"Décret n° 77-192 du 17 février 1977","URL":"https://www.pist.tn/jort/1977/1977F/Jo01377.pdf","note":"citation-key: decret77-192\nJORT n° 13 du 22 février 1977, p. 464. Art. 1er (nouveau) du décret n° 76-1123 : pétrole néant ; gas-oil agriculture et pêche 0,235 D/hl ; autres gas-oils 0,890 D/hl ; effet au 1er janvier 1977 (art. 2). Preuve : image lue."}
{"id":"decret82-212","type":"legislation","title":"Décret n° 82-212 du 4 février 1982 modifiant et complétant le décret n° 70-622 du 31 décembre 1970 portant consolidation et simplification des droits et taxes perçus sur certains produits pétroliers","container-title":"Journal officiel de la République tunisienne","issue":"8","page":"294","issued":{"date-parts":[[1982,2,4]]},"title-short":"Décret n° 82-212 du 4 février 1982","URL":"https://www.pist.tn/jort/1982/1982F/Jo00882.pdf","note":"citation-key: decret82-212\nJORT n° 8 du 9 février 1982, p. 294. Fuel-oil léger 26,990 D/t ; fuel-oil domestique 20,000 (unité non imprimée) ; effet au 5 janvier 1982 (art. 3). Preuve : image lue."}
{"id":"decret84-210","type":"legislation","title":"Décret n° 84-210 du 29 février 1984 modifiant le décret n° 70-622 du 31 décembre 1970 relatif à la consolidation et la simplification des droits et taxes perçus sur certains produits pétroliers","container-title":"Journal officiel de la République tunisienne","issue":"15","page":"535","issued":{"date-parts":[[1984,2,29]]},"title-short":"Décret n° 84-210 du 29 février 1984","URL":"https://www.pist.tn/jort/1984/1984F/Jo01584.pdf","note":"citation-key: decret84-210\nJORT n° 15 des 2-6 mars 1984, p. 535. Taxe unique de compensation sur le gas-oil des travaux agricoles et de la pêche : 0,025 D/hl, à compter du 22 février 1984 à zéro heure. Preuve : image lue."}
{"id":"decret76-1120","type":"legislation","title":"Décret n° 76-1120 du 28 décembre 1976 portant institution d'une taxe compensatrice sur les exportations d'huile d'olive","container-title":"Journal officiel de la République tunisienne","issue":"83","page":"3241","issued":{"date-parts":[[1976,12,28]]},"title-short":"Décret n° 76-1120 du 28 décembre 1976","URL":"https://www.pist.tn/jort/1976/1976F/Jo08376.pdf","note":"citation-key: decret76-1120\nJORT n° 83 du 31 décembre 1976, p. 3241. 30 millimes/kg d'huile d'olive exportée, versés au compte de la Caisse générale de compensation pour la stabilisation du prix de l'huile d'olive conditionnée ; abroge le décret n° 74-876 ; effet au 1er janvier 1977. Preuve : image lue."}
{"id":"decret76-1124","type":"legislation","title":"Décret n° 76-1124 du 31 décembre 1976 portant fixation du taux de la taxe de compensation due sur le ciment ensaché","container-title":"Journal officiel de la République tunisienne","issue":"83","page":"3241","issued":{"date-parts":[[1976,12,31]]},"title-short":"Décret n° 76-1124 du 31 décembre 1976","URL":"https://www.pist.tn/jort/1976/1976F/Jo08376.pdf","note":"citation-key: decret76-1124\nJORT n° 83 du 31 décembre 1976, p. 3241. 2 dinars la tonne au profit de la Caisse générale de compensation ; effet imprimé « 1er janvier 1976 » (art. 2). Preuve : image lue."}
{"id":"arrete-1971-07-26-prix-farines","type":"legislation","title":"Arrêté des ministres de l'économie nationale et de l'agriculture du 26 juillet 1971 modifiant l'arrêté du 10 août 1967 fixant le prix des farines et semoules","container-title":"Journal officiel de la République tunisienne","issue":"32","page":"1002","issued":{"date-parts":[[1971,7,26]]},"URL":"https://www.pist.tn/jort/1971/1971F/Jo03271.pdf","note":"citation-key: arrete-1971-07-26-prix-farines\nJORT n° 32 des 23-27 juillet 1971, p. 1002. Farine panifiable PS + 10 : 6d,100 ; PS − 2 : 6d,540 (unité non imprimée) ; effet au 1er août 1971. Preuve : image lue."}
{"id":"decret75-352-rectificatif","type":"legislation","title":"Rectificatif au décret n° 75-352 du 3 juin 1975 fixant le prix des farines et semoules, du pain, des pâtes alimentaires et du couscous rapide","container-title":"Journal officiel de la République tunisienne","issue":"57","page":"1814","issued":{"date-parts":[[1975,8,26]]},"URL":"https://www.pist.tn/jort/1975/1975F/Jo05775.pdf","note":"citation-key: decret75-352-rectificatif\nJORT n° 57 des 26-29 août 1975, p. 1814 (date : premier jour du fascicule). Pâtes et couscous de semoule PS-18 : « sont fixés [...] par le Ministre de l'Economie Nationale » au lieu de « pourront être librement fixés ». Preuve : image lue."}
{"id":"arrete-1979-05-07-prix-huile","type":"legislation","title":"Arrêté du ministre du commerce du 7 mai 1979 portant fixation du prix de l'huile mélangée","container-title":"Journal officiel de la République tunisienne","issue":"32","page":"1383-1384","issued":{"date-parts":[[1979,5,7]]},"URL":"https://www.pist.tn/jort/1979/1979F/Jo03279.pdf","note":"citation-key: arrete-1979-05-07-prix-huile\nJORT n° 32 du 11 mai 1979, p. 1383. 250 M/litre au public, effet au 3 mai 1979. Preuve : image lue."}
{"id":"arrete-1980-01-21-prix-huile","type":"legislation","title":"Arrêté du ministre du commerce du 21 janvier 1980 portant fixation du prix de l'huile mélangée","container-title":"Journal officiel de la République tunisienne","issue":"21","page":"1021-1022","issued":{"date-parts":[[1980,1,21]]},"URL":"https://www.pist.tn/jort/1980/1980F/Jo02180.pdf","note":"citation-key: arrete-1980-01-21-prix-huile\nJORT n° 21 du 4 avril 1980, p. 1021. 0d,300/litre au public, effet au 23 janvier 1980 à zéro heure. Preuve : image lue."}
{"id":"arrete-1980-02-20-prix-sucre","type":"legislation","title":"Arrêté du ministre du commerce du 20 février 1980 portant fixation des prix de vente du sucre et du café","container-title":"Journal officiel de la République tunisienne","issue":"12","page":"558-559","issued":{"date-parts":[[1980,2,20]]},"URL":"https://www.pist.tn/jort/1980/1980F/Jo01280.pdf","note":"citation-key: arrete-1980-02-20-prix-sucre\nJORT n° 12 du 26 février 1980, p. 558. Sucre en poudre 0,240 D/kg, en morceaux 0,340 D/kg au public ; effet au 23 janvier 1980 à zéro heure. Preuve : image lue."}
{"id":"arrete-1982-11-21-prix-lait","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 21 novembre 1982 fixant le prix de vente public du lait régénéré","container-title":"Journal officiel de la République tunisienne","issue":"76","page":"2581","issued":{"date-parts":[[1982,11,21]]},"URL":"https://www.pist.tn/jort/1982/1982F/Jo07682.pdf","note":"citation-key: arrete-1982-11-21-prix-lait\nJORT n° 76 du 30 novembre 1982, p. 2581. UHT tétra-brik 1 l : 260 M. ; pasteurisé tétra-brik 1 l : 240 M. ; effet au 22 novembre 1982. Preuve : image lue."}
{"id":"arrete-1984-07-10-prix-semoules","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 10 juillet 1984 fixant les prix des semoules","container-title":"Journal officiel de la République tunisienne","issue":"43","page":"1595","issued":{"date-parts":[[1984,7,10]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo04384.pdf","note":"citation-key: arrete-1984-07-10-prix-semoules\nJORT n° 43 des 17-20 juillet 1984, p. 1595. Semoule PS 10 : 15D,500 le quintal au public ; effet au 10 juillet 1984. Preuve : image lue."}
{"id":"arrete-1984-07-10-prix-pates","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 10 juillet 1984 fixant les prix de vente des pâtes et couscous rapide","container-title":"Journal officiel de la République tunisienne","issue":"43","page":"1595-1596","issued":{"date-parts":[[1984,7,10]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo04384.pdf","note":"citation-key: arrete-1984-07-10-prix-pates\nJORT n° 43 des 17-20 juillet 1984, p. 1595-1596. Pâtes PS 10 vrac 1 kg : 200 ; couscous vrac 1 kg : 208 (détail) ; effet au 10 juillet 1984. Preuve : image lue."}
{"id":"arrete-1986-11-22-prix-sucre","type":"legislation","title":"Arrêté du ministre de l'industrie et du commerce du 22 novembre 1986 portant fixation du prix de vente maximum du sucre","container-title":"Journal officiel de la République tunisienne","issue":"68","page":"1337","issued":{"date-parts":[[1986,11,22]]},"URL":"https://www.pist.tn/jort/1986/1986F/Jo06886.pdf","note":"citation-key: arrete-1986-11-22-prix-sucre\nJORT n° 68 du 25 novembre 1986, p. 1337. Poudre 270, morceaux 370 millimes/kg au détail ; effet au 25 novembre 1986. Preuve : image lue."}
{"id":"arrete-1986-12-29-prix-huile","type":"legislation","title":"Arrêté du ministre de l'industrie et du commerce du 29 décembre 1986 portant fixation du prix de vente maximum de l'huile de mélange vrac","container-title":"Journal officiel de la République tunisienne","issue":"1","page":"14","issued":{"date-parts":[[1986,12,29]]},"URL":"https://www.pist.tn/jort/1987/1987F/Jo00187.pdf","note":"citation-key: arrete-1986-12-29-prix-huile\nJORT n° 1 des 2-6 janvier 1987, p. 14. 320 mil/litre au détail ; effet au 7 décembre 1986 (art. 1er) ; déclaration des stocks au 10 décembre (art. 2). Preuve : image lue."}
{"id":"arrete-1988-09-08-prix-sucre","type":"legislation","title":"Arrêté du ministre de l'industrie et du commerce du 8 septembre 1988 portant fixation du prix de vente du sucre","container-title":"Journal officiel de la République tunisienne","issue":"61","page":"1274","issued":{"date-parts":[[1988,9,8]]},"URL":"https://www.pist.tn/jort/1988/1988F/Jo06188.pdf","note":"citation-key: arrete-1988-09-08-prix-sucre\nJORT n° 61 du 16 septembre 1988, p. 1274. Poudre 300, morceaux 400 mil/kg ; effet au 1er juillet 1988. Preuve : image lue."}
{"id":"arrete-1989-11-11-prix-sucre","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 11 novembre 1989 portant fixation du prix de vente du sucre","container-title":"Journal officiel de la République tunisienne","issue":"77","page":"1822","issued":{"date-parts":[[1989,11,11]]},"URL":"https://www.pist.tn/jort/1989/1989F/Jo07789.pdf","note":"citation-key: arrete-1989-11-11-prix-sucre\nJORT n° 77 des 17-21 novembre 1989, p. 1822. Poudre 350, morceaux 500 (du kilogramme) ; effet au 12 août 1989. Preuve : image lue."}
{"id":"arrete-1989-11-11-prix-farines","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 11 novembre 1989 portant fixation du prix de vente de la farine extraite à PS-7","container-title":"Journal officiel de la République tunisienne","issue":"77","page":"1821-1822","issued":{"date-parts":[[1989,11,11]]},"URL":"https://www.pist.tn/jort/1989/1989F/Jo07789.pdf","note":"citation-key: arrete-1989-11-11-prix-farines\nJORT n° 77 des 17-21 novembre 1989, p. 1821. PS-7 vrac 245 mil/kg, paquet 1 kg 290 mil au détail ; effet au 12 août 1989. Preuve : image lue."}
{"id":"arrete-1989-11-11-prix-pates","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 11 novembre 1989 portant fixation du prix de vente des pâtes alimentaires et couscous rapide","container-title":"Journal officiel de la République tunisienne","issue":"77","page":"1822-1823","issued":{"date-parts":[[1989,11,11]]},"URL":"https://www.pist.tn/jort/1989/1989F/Jo07789.pdf","note":"citation-key: arrete-1989-11-11-prix-pates\nJORT n° 77 des 17-21 novembre 1989, p. 1822-1823. Pâtes PS-10 vrac 1 kg 260 ; couscous vrac 1 kg 300 (détail) ; effet au 12 août 1989. Preuve : image lue."}
{"id":"arrete-1990-07-18-prix-sucre","type":"legislation","title":"Arrêté du ministre de l'économie et des finances du 18 juillet 1990 portant fixation des prix de vente du sucre","container-title":"Journal officiel de la République tunisienne","issue":"49","page":"982-983","issued":{"date-parts":[[1990,7,18]]},"URL":"https://www.pist.tn/jort/1990/1990F/Jo04990.pdf","note":"citation-key: arrete-1990-07-18-prix-sucre\nJORT n° 49 du 24 juillet 1990, p. 982. Sucre blanc en poudre 400, en morceaux 560 mil/kg ; effet au 13 juillet 1990. Preuve : image lue."}
{"id":"arrete-1991-06-25-prix-sucre","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 25 juin 1991 portant fixation des prix de vente du sucre","container-title":"Journal officiel de la République tunisienne","issue":"48","page":"1251","issued":{"date-parts":[[1991,6,25]]},"URL":"https://www.pist.tn/jort/1991/1991F/Jo04891.pdf","note":"citation-key: arrete-1991-06-25-prix-sucre\nJORT n° 48 du 5 juillet 1991, p. 1251. Sucre blanc en poudre 430, en morceaux 620, sucre brun 300 mil/kg ; effet au 17 juin 1991 (art. 2 imprime « 1990 »). Preuve : image lue."}
{"id":"arrete-1991-08-15-prix-semoules","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 15 août 1991 portant fixation des prix de vente de la semoule PS-10","container-title":"Journal officiel de la République tunisienne","issue":"61","page":"1546","issued":{"date-parts":[[1991,8,15]]},"URL":"https://www.pist.tn/jort/1991/1991F/Jo06191.pdf","note":"citation-key: arrete-1991-08-15-prix-semoules\nJORT n° 61 des 3-6 septembre 1991, p. 1546. Vrac 1 kg : 205 mil au détail ; effet au 17 août 1991. Preuve : image lue."}
{"id":"arrete-1991-08-15-prix-huile","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 15 août 1991 portant fixation des prix de vente de l'huile de graines en vrac","container-title":"Journal officiel de la République tunisienne","issue":"61","page":"1546-1547","issued":{"date-parts":[[1991,8,15]]},"URL":"https://www.pist.tn/jort/1991/1991F/Jo06191.pdf","note":"citation-key: arrete-1991-08-15-prix-huile\nJORT n° 61 des 3-6 septembre 1991, p. 1547. 370 millimes/litre au détail ; effet au 17 août 1991. Preuve : image lue."}
```

**Clés à aligner.**
- `decret79-413` existe déjà (FR et AR). Compléter sa `note` : image lue au n° 32 du 11 mai 1979, p. 1381 ; effet au 3 mai 1979 ; prix des farines et semoules « au quintal net, nu, rendu au chef lieu de la délégation », non au détail.
- `arrete-1991-08-15-prix-pates` : absente ; à créer sur le même modèle si le rédacteur la cite.

Les éditions AR (`Ja…`) se citeraient sous des clés `-ar` distinctes. Leur pagination n'est pas
relevée ici.

---

## 5. Lacunes et suites

**Taxe unique et lait.**
- **Fuel-oil domestique, 1982.** L'unité du taux de 20,000 n'est pas imprimée à l'art. 2 du décret
  n° 82-212. La tonne est probable par analogie avec l'art. 1er, **non établie**.
- **Taxe unique après le décret n° 84-210.** Les tarifs de l'essence et du gas-oil ordinaire après
  1984 ne sont pas lus. Les intitulés de 1984 à 1992 ne signalent pas d'autre modificatif de
  l'art. 5 du décret n° 70-622 ; à vérifier par une seconde voie avant de prolonger la figure.
- **Arrêté du 10 août 1967** (farines et semoules, base de l'arrêté de 1971). Non lu ; il fixerait
  l'unité et le stade des prix de 1971.
- **Lait avant 1982.** L'arrêté du 31 mars 1973 « portant fixation des prix des produits laitiers »
  (n° 13/1973, p. 544) [méta] est le seul antécédent repéré. L'arrêté de 1982 ne le vise pas.

**Ce que le texte lui-même rend incertain.**
- **Redevances de l'huile en 1980.** La lecture « 0d,050 » contre « 0d,060 » reste ambiguë à
  l'image.
- **Effets contradictoires.**
  - Huile 1986 : 7 décembre selon l'art. 1er, 10 décembre selon l'art. 2.
  - Lait 1991 : 22 juillet selon l'art. 1er, « application immédiate » selon l'art. 3.
  - Sucre 1991 : coquille de l'art. 2, qui imprime 1990.
  - Ciment 1976 : effet imprimé au 1er janvier 1976.

  À signaler en note, sans corriger le texte.

**Lignes de backlog proposées** (à verser par `archiviste-backlog`).
- `backlog-precis.md`, chapitre carburants :
  - verser 1968, 1977 et 1984 dans `TAXE_UNIQUE` (§ 1.7) ;
  - TODO de la ligne 243 : la lecture est faite, reste le versement ;
  - corriger le tracé du pétrole lampant à partir de 1977.
- `backlog-precis.md`, chapitre produits de base :
  - séries sucre, huile, semoule, pâtes et lait 1979-1991, désormais lues à l'image (§ 2) ;
  - corriger les « prix de détail » des farines de 1975 et 1979 (§ 2.3) ;
  - rectificatif PS-18 de 1975 (§ 2.6).
- `biblio-a-rapatrier.md` : les 24 clés nouvelles du § 4.

Aucun PDF n'a été téléchargé : tout vient du corpus local. Aucun fichier du précis n'a été modifié.
