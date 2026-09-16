# Droits de consommation — dossier documentaire (champ, redevables, fait générateur, tableau annexé, chronologie, articulation avec la TVA, produits pétroliers)

> Note **documentaire**, préalable à la rédaction de `precis/fr/fiscalite/_droits_consommation.qmd`.
> Elle ne rédige pas de prose de précis et n'a modifié aucun fichier de `precis/`.
>
> **Conventions de datation.** Pour chaque texte, trois dates sont relevées séparément :
> (1) **signature**, (2) **publication au JORT** (numéro de fascicule **et** page), (3) **date d'effet**.
> Comme pour la TVA, la date d'effet n'est jamais présumée : la loi 88-62 ne fixe pas la sienne
> (son article 8 renvoie à un décret, § 1.8) et deux décrets de 1991 sont **rétroactifs** (§ 4.3).
>
> **Degré de certitude.** Quatre mentions, identiques à celles de la note TVA : *établi (JORT, lu à
> l'image)* ; *établi (texte officiel à couche texte)* ; *probable* (cohérent, corroboré
> indirectement, source primaire non lue) ; *non établi* (à ne pas écrire).
> **Provenance des paginations** : sauf mention « pied de page lu », les numéros de page viennent du
> champ `pages` de `jort_cache.db`, qui reprend les notices du JORT — fiable, mais de seconde main.
>
> **Correction d'une donnée du dossier TVA.** Le dossier TVA indiquait que la loi 88-62 partage le
> fascicule n° 39 avec les lois 88-60, 88-61, 88-63 et 88-64 : c'est exact. Il ne donnait pas sa
> pagination. Elle est ici établie : **p. 847-856** (notice `jort_cache` recid 113994, **confirmée
> par les pieds de page lus à l'image** : la loi commence p. 847 et le tableau s'achève p. 856, la
> loi 88-63 suivant sur la même page 856).
>
> **Note d'outillage.** `www.pist.tn` présente un certificat TLS expiré : toutes les URL citées ont
> été testées par `curl -sk … -w "%{http_code} %{content_type} %{size_download}"`. Celles qui sont
> dites « vérifiées » répondent **HTTP 200 en `application/pdf`**. Les URL arabes sont **lues dans le
> champ `pdf_ar`** de la base, jamais dérivées de l'URL française.
> **Trois éditions françaises sont absentes** et il faut le dire dans le précis plutôt que de citer
> une URL morte : **JORT 2015 n° 104** (LF 2016), **JORT 2018 n° 104** (LF 2019) et **JORT 2019
> n° 104** répondent **404** (289 octets de HTML) ; seules leurs éditions arabes existent. Le texte
> français de ces lois a été lu dans les PDF officiels de `PDFs/Lois_de_Finances/`.
>
> **Méthode de recherche.** Toute recherche `LIKE` a été doublée d'une recherche **FTS** et d'une
> recherche **en arabe** (`objet like '%المعلوم على الاستهلاك%'`, 12 occurrences, toutes postérieures
> à 2015). C'est la recherche arabe, et elle seule, qui fait apparaître les articles 44 et 57 de la
> LF 2016 et l'article 45 de la LF 2018 — c'est-à-dire **les deux textes qui ont remplacé le tableau
> annexé en entier**. Une conclusion négative fondée sur le seul français aurait manqué l'essentiel.
>
> **Note sur l'OCR.** L'OCR du fascicule de 1988 entrelace les deux colonnes et transforme
> systématiquement le taux **11** en « il », « nl », « li » ou « 1 ». **Aucun taux de 1988 n'est cité
> ici d'après l'OCR** : les pages **847, 848, 849, 855 et 856 ont été relues à l'image**. Les pages
> **850 à 854 ne l'ont pas été** — voir les lacunes, § 9.
>
> **Statut des notes communes.** Doctrine administrative, jamais source du droit. Trois notes
> communes sont utilisées ici (24/2007, 7/2016, 17/2018) **uniquement en corroboration** de textes
> déjà lus.

---

## Résultat principal

**1. Le droit de consommation n'est pas une annexe de la TVA : c'est une loi autonome, courte, de
huit articles, votée le même jour et publiée dans le même fascicule que le code de la TVA.** La loi
n° 88-62 du 2 juin 1988 tient en **huit articles** (p. 847) suivis d'un **tableau annexé de dix
pages** (p. 847-856). Les huit articles portent, dans l'ordre : le champ, les redevables, le fait
générateur, l'assiette, le droit à imputation, les renvois au code de la TVA, les abrogations, et le
renvoi à un décret pour l'entrée en vigueur. **Tout le reste — quels produits, à quel taux — est dans
le tableau.**

**2. Le champ n'est pas défini par une catégorie économique mais par une liste douanière.** L'article
1er ne décrit aucune classe de produits : il soumet au droit « les produits repris au tableau
figurant en annexe […] qu'ils soient **importés ou fabriqués localement** ». La désignation se fait
par **numéro du tarif douanier** (NT), avec la technique des positions « Ex » pour les extraits de
position. Conséquence de rédaction à ne pas manquer : **modifier le champ, c'est modifier le
tableau** — et c'est ce que font, depuis 1988, une trentaine de textes (§ 4).

**3. Le tableau est mixte dès l'origine : ad valorem et spécifique.** L'article 4 prévoit les deux
assiettes, et le tableau de 1988 les mêle : des taux en pourcentage (11 %, 25 %, 47 %, 60 %, 102 %,
135 %, 160 %, 200 %…) et des tarifs par volume, par poids ou par unité (380 D/hl sur l'alcool
éthylique, 15,228 D/hl sur l'essence super, 6,235 D/tonne sur le propane et le butane). *Écrire que
le droit de consommation est « une taxe ad valorem » serait faux ; écrire qu'il est « une accise
spécifique » le serait aussi.*

**4. L'articulation avec la TVA est une cascade, et elle est asymétrique — c'est le point que le
chapitre TVA laissait ouvert.** Le droit de consommation **s'ajoute** à la TVA et **entre dans son
assiette**, tandis que la TVA n'entre pas dans l'assiette du droit de consommation. Cela ne se déduit
pas : les deux textes le disent. L'article 4 de la loi 88-62 assoit le droit ad valorem sur « le prix
de vente tous frais, droits et taxes compris **à l'exclusion du droit de consommation et de la taxe
sur la valeur ajoutée** » ; l'article 6-I du code de la TVA assoit la TVA sur le prix « tous frais,
droits et taxes inclus, **à l'exclusion de la taxe sur la valeur ajoutée**, des subventions
d'exploitation et des prélèvements conjoncturels et de compensation » — le droit de consommation
n'étant pas au nombre des exclusions, il est dans la base (§ 6).

**5. Le droit de consommation est déductible — ce qui le distingue d'une accise ordinaire.**
L'article 5 autorise l'assujetti à **imputer** sur le droit dû celui qui a grevé ses acquisitions et
importations de matières « qui entrent **intégralement** dans la composition du produit final
soumis », avec report du reliquat sur les mois suivants. La LF 1990 y ajoute une obligation de
**facturation à l'identique** par les commerçants assujettis à la TVA (§ 4.2).

**6. Deux habilitations — les deux seules rencontrées dans le corpus lu — permettent de fixer des
taux par décret ; elles sont d'origine différente et de portée limitée.** (i) Pour les **boissons** (positions 22-03 et 22-05 à
22-09) : **article 86 de la loi n° 88-145 (LF 1989)**, qui renvoie au décret « les règles, les taux
et modalités de perception des impôts droits et taxes » de ces secteurs. (ii) Pour les **produits
pétroliers** (27-09 à 27-11) : **article 35 de la loi n° 89-115 (LF 1990)**, qui ajoute à l'article
1er de la loi 88-62 un second alinéa — « les taux du droit de consommation relatif aux produits
repris au tarif douanier sous les rubriques n° 27-09 à 27-11 **sont fixés par décret** ». *Hors de
ces deux domaines, le tableau ne se modifie que par la loi.* Les deux habilitations ont été **lues à
l'image** (§ 3).

**7. Le tableau annexé de 1988 n'existe plus : il a été abrogé et remplacé en entier, deux fois.**
Une première fois par l'**article 44 de la LF 2016**, une seconde par l'**article 45 de la LF 2018**,
tous deux rédigés en la même forme : « Est abrogé le tableau annexé à la loi n° 88-62 […] et remplacé
par le tableau suivant ». Le tableau en vigueur descend donc du texte de 2018, amendé ensuite par les
LF 2019, 2021 et 2022. *Citer « le tableau annexé à la loi 88-62 » sans millésime est une source
d'erreur : le tableau de 1988 et celui d'aujourd'hui n'ont presque aucun poste en commun.*

**8. Le transfert de 2007 depuis le taux majoré de TVA est établi, et il est étroit.** L'article 14
de la loi n° 2006-80 ajoute au tableau annexé **cinq lignes seulement** — parfums et eaux de toilette
(33-03), produits de beauté et de maquillage (33-04), machines pour le conditionnement de l'air
(84-15), unités de réfrigération de type « split system » (Ex 84-18), machines à laver la vaisselle à
chauffage électrique (Ex 84-22) — toutes au taux de **10 %**, avec effet au **1er janvier 2007**
(art. 19). Les autres produits du tableau « C » ne sont donc pas transférés : ils retombent au taux
normal de 18 % (§ 7).

**9. Les produits pétroliers ont un régime propre depuis 1990, et le décret 98-952 n'en est ni le
premier ni le dernier chaînon.** La chaîne est : habilitation (LF 1990, art. 35) → décret 94-816 →
décret 98-952, art. 2 → **décret n° 99-894 du 19 avril 1999**, qui fixe le tarif complet et applique
ses dispositions **à compter du 22 avril 1999** (lu à l'image). Depuis les refontes de 2016 et 2018,
les tarifs pétroliers figurent de nouveau **dans le tableau annexé lui-même**, alors même que
l'habilitation de l'article 1er alinéa 2 subsiste — situation à décrire sans la trancher (§ 8).

---

## 1. La loi n° 88-62 du 2 juin 1988 — les huit articles

**Texte** : **loi n° 88-62 du 2 juin 1988, portant refonte de la réglementation relative aux droits
de consommation**.

| | |
|---|---|
| Signature | **2 juin 1988** |
| Publication | **JORT n° 39 du 10 juin 1988**, tome 131, **p. 847-856** (pieds de page lus à l'image) |
| Date d'effet | **non fixée par la loi** : son article 8 renvoie à un décret → **1er juillet 1988** (décret n° 88-1109, art. 2) |

- Copie locale FR : `/home/benjello/projets/PDFs-legislation-tunisie/PDFs/JORT/1988/fr/Jo03988.pdf`
  (**loi 88-62 = pages 27 à 36 du PDF**)
- Copie locale AR : `/home/benjello/projets/PDFs-legislation-tunisie/PDFs/JORT/1988/ar/Ja03988.pdf`
- OCR local : `…/markdown_output/JORT/1988/fr/Jo03988.md`, à partir de la ligne 4006 (**colonnes
  entrelacées, taux inexploitables**)
- URL FR : `https://www.pist.tn/jort/1988/1988F/Jo03988.pdf` — **vérifiée** (HTTP 200)
- URL AR : `https://www.pist.tn/jort/1988/1988A/Ja03988.pdf` — **vérifiée** (HTTP 200)
- Notice `jort_cache.db` : recid **113994**, `pages = '0847-0856'`, `jort_tome = 131`

Mention des travaux préparatoires, en note (1) de la page 847 : « Discussion et adoption par la
chambre des députés dans sa séance du **1er juin 1988** ».

### 1.1 Champ d'application — article 1er — *établi (JORT, lu à l'image, p. 847)*

> « **Art. 1er.** — Sont soumis au droit de consommation, selon les taux prévus à cet effet, les
> produits repris au tableau figurant en annexe de la présente loi **qu'ils soient importés ou
> fabriqués localement**. »

Trois traits à retenir pour la rédaction : (i) **aucune définition matérielle** du champ, seulement
un renvoi au tableau ; (ii) **neutralité entre importation et production locale**, posée dès la
première phrase ; (iii) la désignation des produits se fait par **numéro du tarif douanier**, le
tableau portant en tête de colonne « NT » puis « Désignation des produits » puis « Taux DC en % ».

**Deux alinéas ont été ajoutés depuis, et deux sous-paragraphes supprimés** — état consolidé DGELF :
- alinéa 2 : « Cependant les taux du droit de consommation relatif aux produits repris au tarif
  douanier sous les rubriques n° 27-09 à 27-11 sont fixés par décret » *(ajouté par l'art. 35 de la
  LF 1990 — § 3.2, lu à l'image)* ;
- « les sous-paragraphes 3 et 4 sont abrogés par l'article 45 de la loi de finances pour l'année
  2016 » *(annotation DGELF ; l'article 45 de la LF 2016 a été lu dans le PDF officiel, § 4.7)*.

### 1.2 Redevables — article 2 — *établi (JORT, lu à l'image, p. 847)*

> « **Art. 2.** — Sont assujettis au droit de consommation :
> 1) les **fabricants de bière** ;
> 2) les **embouteilleurs de vin** ;
> 3) les **fabricants de tout autre produit** soumis au droit de consommation ;
> 4) les **entrepositaires et les commerçants de gros** de boissons alcoolisées, de vins et de
> bières. »

Observation utile au précis : **l'importateur n'est pas nommé à l'article 2**, alors que l'article
1er vise les produits importés et que l'article 3 fait du dédouanement un fait générateur. Le
dispositif tient donc par la **liquidation en douane** plutôt que par la qualité d'assujetti.
*Constat de lecture, à formuler prudemment : aucun texte lu ne le commente.*

**Ajout ultérieur** : un **5)** « la société tunisienne de l'électricité et du gaz au titre des
ventes du **gaz naturel destiné à l'utilisation en tant que carburant** pour les véhicules
automobiles », ajouté par l'**article 58 de la loi n° 2007-70 (LF 2008)** *(annotation DGELF ; notice
JORT n° 104 du 28 décembre 2007, p. 4367 ; texte non lu sur pièce)*.

### 1.3 Fait générateur — article 3 — *établi (JORT, lu à l'image, p. 847)*

> « **Art. 3.** — Le fait générateur du droit de consommation est constitué :
> — à l'importation, par le **dédouanement du produit** ;
> — en régime intérieur, par la **livraison du produit**. »

Deux faits générateurs, deux seulement. La rédaction est plus courte que celle de l'article 5 du code
de la TVA (six cas) : ni les livraisons à soi-même, ni les prestations de service, ni les travaux
immobiliers n'ont d'équivalent ici — ce qui est cohérent avec un impôt assis sur des **produits**.

### 1.4 Assiette — article 4 — *établi (JORT, lu à l'image, p. 847)*

> « **Art. 4.** — L'assiette du droit de consommation est constituée :
> a) pour les produits soumis à un **taux ad-valorem** :
> — à l'importation, par la **valeur en douane** ;
> — en régime intérieur, par le **prix de vente tous frais, droits et taxes compris à l'exclusion du
> droit de consommation et de la taxe sur la valeur ajoutée** ;
> b) pour les produits soumis à un **taux spécifique**, par le **volume ou le poids**.
> Toutefois, le droit de consommation applicable aux boissons alcoolisées, aux vins et aux bières
> **n'a pas d'incidence sur le calcul des marges** des entrepositaires et des marchands desdits
> produits. Il est **retransmis à leurs clients pour les mêmes montants qu'ils ont supportés**. »

C'est l'article clef pour le § 6 (articulation avec la TVA) et pour le § 2 (structure du tableau).

**Deux alinéas ajoutés depuis**, tous deux sur les **prix de transfert** :
- **article 43 de la loi n° 2012-27 (LF 2013)** : liquidation sur le prix pratiqué par les
  entrepositaires et commerçants de gros de boissons alcoolisées et de vins, en cas de lien de
  dépendance au sens de l'article 2-II du code de la TVA ;
- **article 57 de la loi n° 2015-53 (LF 2016)** : même règle étendue aux **ventes des fabricants** de
  tout produit soumis au droit ad valorem, en cas de lien de dépendance avec les commerçants
  *(texte lu dans le PDF officiel de la LF 2016, sous l'intitulé « Maîtrise de l'assiette du droit de
  consommation », JORT n° 104 du 29 décembre 2015, **p. 3155**, pied de page lu)*.

### 1.5 Imputation — article 5 — *établi (JORT, lu à l'image, p. 847)*

> « **Art. 5.** — Les assujettis sont autorisés à **imputer** sur le droit de consommation dû […] le
> droit de consommation ayant effectivement grevé leurs acquisitions auprès d'autres assujettis et
> les importations effectuées par eux-mêmes des matières ou produits qui **entrent intégralement dans
> la composition du produit final soumis**.
> Au cas où le droit de consommation dû au titre d'un mois ne permet pas l'imputation totale du droit
> de consommation déductible, le **reliquat est reporté sur les mois qui suivent**.
> Les dispositions prévues à l'**article 9 § I-2 et § IV-4 et 5 du code de la taxe sur la valeur
> ajoutée**, relatif aux déductions, sont applicables en matière de droit de consommation. »

**Alinéa ajouté par l'article 34 de la LF 1990** (§ 3.2, lu à l'image) : les commerçants assujettis à
la TVA qui commercialisent des produits soumis au droit « sont tenus de **facturer à l'identique** à
leurs clients le droit de consommation supporté lors de l'acquisition des mêmes produits », ce droit
étant alors déductible.

### 1.6 Renvois au code de la TVA — article 6 — *établi (JORT, lu à l'image, p. 847)*

> « **Art. 6.** — Les dispositions des **articles 8, 10, 11, 13, 14 et 18 à 21** du code de la taxe
> sur la valeur ajoutée sont applicables en matière de droit de consommation. »

La loi de 1988 n'organise donc **ni le recouvrement, ni le contentieux, ni les obligations
déclaratives** : elle les emprunte au code de la TVA. *C'est un point de structure à écrire
explicitement dans le précis, faute de quoi le lecteur cherchera dans la loi 88-62 des règles qui n'y
sont pas.*

État consolidé (DGELF) : la liste est devenue « articles 8, 10, 11, **13 bis, 13 ter**, 14 et 18 à
21 » — l'article 13 ayant été abrogé par l'article 68 de la loi n° 91-89 du 31 décembre 1991, le
13 ter ajouté par l'article 3 de la loi n° 2017-8, la liste modifiée par l'article 37 de la LF 2022 ;
un second alinéa (art. 52 de la LF 2022) écarte, en matière de droit de consommation, l'exception de
l'article 11 relative aux sociétés de commerce international. **Un article 6 bis** (suspension du
droit pour les véhicules tout terrain importés par les concessionnaires au profit des agences de
voyages) a été ajouté par l'**article 22 de la LF 2018**.

### 1.7 Abrogations — article 7 — *établi (JORT, lu à l'image, p. 847)*

> « **Art. 7.** — Toutes dispositions contraires à la présente loi sont abrogées notamment :
> — les **articles 4 à 11** relatifs à la **taxe sur les bières, vins et autres boissons alcoolisées**
> prévue par la **loi n° 84-2 du 21 mars 1984** portant loi de finances complémentaire pour la
> gestion 1984 ;
> — les **articles 93 à 95** relatifs au **fonds spécial de développement de la culture** prévu par la
> **loi n° 83-113 du 30 décembre 1983** portant loi de finances pour la gestion 1984. »

*C'est l'identité du régime remplacé, et elle est double : une taxe sur les alcools et un fonds
affecté. À citer plutôt qu'une formule vague sur « les anciens droits indirects ».* Noter que la
« **taxe de consommation** » du décret du 29 décembre 1955 n'est pas abrogée ici mais par l'**article
2 de la loi 88-61** (code de la TVA) — les deux lois se partagent l'abrogation de l'ancien régime.

### 1.8 Entrée en vigueur — article 8 et décret n° 88-1109 — *établi (JORT, lu à l'image)*

> « **Art. 8.** — La date de mise en application de la présente loi sera fixée par décret. »

> Décret n° 88-1109, **art. 2** : « Les dispositions de la loi sus-visée n° 88-62 du 2 juin 1988
> portant refonte de la réglementation relative aux droits de consommation sont applicables **à
> compter du 1er juillet 1988** conformément à son article 8. »

| | |
|---|---|
| Signature | **11 juin 1988** |
| Publication | **JORT n° 42 du 21 juin 1988**, tome 131, **p. 923** (pied de page lu) |
| Date d'effet | **1er juillet 1988** |

*Déjà établi dans le dossier TVA ; la référence `decret-88-1109-calendrier-tva` existe dans
`precis/fr/fiscalite/references.json`.* À noter pour la rédaction : **le droit de consommation entre
en vigueur d'un coup**, sans le calendrier échelonné qui a marqué la TVA.

---

## 2. Le tableau annexé de 1988 — structure et contenu

*Établi (JORT, lu à l'image) pour les pages **847, 848, 849, 855 et 856** ; **non relu à l'image**
pour les pages 850 à 854 (§ 9).*

### 2.1 La forme

Trois colonnes : **« NT »** (numéro du tarif douanier), **« Désignation des produits »**, **« Taux DC
en % »**. Le titre du tableau est « **PRODUITS SOUMIS AU DROIT DE CONSOMMATION** ». Deux conventions
de désignation coexistent :
- la **position entière** (`02-03`, `09-01`, `22-03`, `24-02`) ;
- la **position extraite**, préfixée `Ex` (`Ex 05-07`, `Ex 27-11`, `Ex 33-06`), qui ne retient qu'une
  partie de la position douanière, précisée par le libellé — souvent avec des exclusions (« à
  l'exclusion des amendes », « à l'exclusion de ceux pour aérodynes et à usage agricole »).

L'intitulé de la colonne dit « en % », mais **le tableau contient aussi des tarifs spécifiques** :
la colonne mêle les deux, conformément à l'article 4. C'est une **impropriété du tableau d'origine**,
corrigée dans les tableaux de 2016 et 2018, dont la colonne s'intitule « **DROIT DE CONSOMMATION** ».

### 2.2 Les taux ad valorem de 1988 — relevés à l'image

Échelle observée p. 847-849 et 855-856 : **11 %** (taux le plus fréquent, de loin), **25 %**,
**35 %**, **47 %**, **60 %**, **100 %**, **102 %**, **110 %**, **135 %**, **160 %**, **200 %**.

Exemples littéraux, à l'image (p. 847-848) : foies de volailles 11 % ; ivoire, poudre et déchets
d'ivoire 60 % ; feuillages et parties de plantes pour bouquets 25 % ; ananas, bananes, mangues,
avocats, goyaves, noix de coco, noix du Brésil, noix de cajou 25 % ; pistaches 11 % ; autres fruits à
coques 47 % ; café 11 % ; thé 11 % ; poivre, vanille, cannelle 25 % ; caviar et succédanés 135 % ;
dragées contenant une liqueur alcoolique 110 % ; extraits ou essence de café, y compris le café
soluble, **160 %** ; tabacs bruts 25 % ; tabacs fabriqués **102 %** ; marbres blancs 60 % ; artifices
pour divertissements **200 %**.

### 2.3 Les tarifs spécifiques de 1988 — relevés à l'image (p. 848-849)

| Position | Produit | Tarif 1988 |
|---|---|---|
| 22-08 | alcool éthylique **non dénaturé** de tous titres | **380 D/hl** |
| 22-08 | alcool éthylique **dénaturé** de tous titres | **4,192 D/hl** |
| Ex 22-09 | préparations alcooliques à usage **autre que** la fabrication de boissons alcoolisées | **10,480 D/hl** |
| Ex 22-09 | préparations alcooliques destinées à la **fabrication de boissons alcoolisées** | **380 D/hl** |
| 27-09 | huiles brutes de pétrole ou de minéraux bitumineux | **0,400 D/hl** |
| 27-10 | essence super | **15,228 D/hl** |
| 27-10 | essence normale | **14,630 D/hl** |
| 27-10 | essence avion (kérosène), y compris carburéacteur | **1,990 D/hl** |
| 27-10 | white spirit non dénaturé | **1,690 D/hl** |
| 27-10 | pétrole lampant | **1,125 D/hl** |
| 27-10 | gas-oil | **2,887 D/hl** |
| 27-10 | fuel-oil domestique | **4,972 D/100 kg** |
| 27-10 | fuel-oil léger | **3,900 D/100 kg** |
| 27-10 | fuel-oil lourd | **1,719 D/100 kg** |
| 27-10 | huiles de graissage et lubrifiants | **0,997 D/100 kg** |
| 27-10 | huiles de vaseline et de paraffine | **0,875 D/hl** |
| 27-10 | autres | **1,690 D/hl** |
| Ex 27-11 | propane et butane | **6,235 D/tonne** |
| 36-02 | explosifs préparés | **25,20 N/kg** *(formule, voir renvoi (3) ci-dessous)* |

Les boissons fermentées portent en 1988 des **taux ad valorem très élevés** assortis du renvoi (1) :
bières **268**, champagne **470**, vins de liqueurs et mousseux **190**, autres vins **150**,
vermouths **180**, boukha **612**, whisky et spiritueux importés **580**, whisky et spiritueux de
fabrication locale **350**, pastis, ricard, anisette et thibarine **534**.

### 2.4 Les trois renvois du tableau — *établi (JORT, lu à l'image, p. 856)*

Ils sont à citer, car chacun porte une règle de fond que le corps de la loi ne contient pas :

> **(1)** « Les **hôteliers** sont autorisés à déduire de la taxe sur la valeur ajoutée dûe sur leurs
> opérations **50 % du droit de consommation** relatif aux boissons alcoolisées, vins et bières. »
> **(2)** « Les personnes qui, auparavant, ne supportaient que la **taxe unique de compensation sur
> les carburants** restent soumises à cette même taxe. »
> **(3)** « Le droit de consommation sur les **explosifs** en Tunisie est exigible dès l'achèvement de
> la fabrication. […] Le taux de l'impôt à percevoir sur chaque type de dynamite, cheddite et autres
> explosifs fabriqués ou importés est fixé conformément à la formule suivante : **X = 18 N**, dans
> laquelle le taux X représente le taux en dinars de l'impôt à percevoir et N le coefficient
> d'utilisation pratique de chaque explosif […]. Le taux final de l'impôt ne peut en aucun cas excéder
> **60 millimes par kilo**. »

**Le renvoi (1) a été abrogé** par l'**article 36 de la LF 1990**, sous l'intitulé « Suppression de la
déduction du droit de consommation » (§ 3.2, lu à l'image).

---

## 3. Qui peut modifier le tableau, et par quel véhicule

C'est la question de structure la plus utile au chapitre, et elle a une réponse nette.

### 3.1 Habilitation « boissons » — article 86 de la loi n° 88-145 (LF 1989) — *établi (JORT, lu à l'image)*

> « **Article 86.** — L'organisation des secteurs relatifs à la loterie, aux paris et activités
> similaires et aux produits repris sous les rubriques n° **22-03 et 22-05 à 22-09** est fixée par
> arrêté du ministre concerné.
> Les **règles, les taux et modalités de perception des impôts droits et taxes** relatifs aux secteurs
> visés ci-dessus ainsi que l'affectation des recettes provenant de ces secteurs **sont fixées par
> décret**. »

| | |
|---|---|
| Signature | **31 décembre 1988** (mention « Fait à Tunis, le 31 décembre 1988 », lue p. 1805) |
| Publication | **JORT n° 87 des 30-31 décembre 1988**, tome 131 ; la loi occupe **p. 1793-1805**, l'**article 86 est p. 1801** (pied de page lu) |
| Date d'effet | **1er janvier 1989** — *déduit du régime de droit commun des lois de finances, non lu dans le texte* |

C'est cette habilitation qui fonde les décrets sur les alcools : **91-551**, **93-2090**,
**97-1368**, et ses modificatifs (2002-627, 2007-1977, 2013-929, décret gouvernemental 2015-1768).

### 3.2 Habilitation « produits pétroliers » et trois autres mesures — loi n° 89-115 (LF 1990) — *établi (JORT, lu à l'image, p. 2148-2150)*

Quatre articles de cette loi touchent au droit de consommation ; tous ont été lus à l'image.

> « **Article 29** *(p. 2148-2149, intitulé « Encouragement à la production »)*. — Est supprimé le
> droit de consommation relatif aux produits repris au tableau annexé à la loi n° 88-62 du 2 juin
> 1988 figurant sous les numéros des positions tarifaires suivantes : […] » — suit une liste :
> vanille, cannelle, girofles, noix muscade, **Ex 09-10 thym, laurier et fenugrec**, sucs et extraits
> de réglisse et autres mucilages, 19-05, moutarde préparée, sauces et condiments, **Ex 27-10 white
> spirit dénaturé**, extraits de vanille, tapis « kelim » et similaires, puis *(p. 2149)* Ex 90-25
> appareils photométriques, 91-05 et 91-06 appareils d'horlogerie.

> « **Article 34** *(p. 2150, intitulé « Facturation du droit de consommation »)*. — Il est ajouté un
> nouvel alinéa à l'article 5 de la loi n° 88-62 du 2 juin 1988 ainsi libellé : "Toutefois, les
> commerçants assujettis à la T.V.A. et commercialisant des produits soumis au droit de consommation
> sont tenus de **facturer à l'identique** à leurs clients le droit de consommation supporté lors de
> l'acquisition des mêmes produits. Le droit de consommation ainsi facturé est déductible dans les
> conditions sus-visées." »

> « **Article 35** *(p. 2150)*. — Il est ajouté à l'article 1er de la loi n° 88-62 du 2 juin 1988
> […] un deuxième alinéa ainsi libellé : "Cependant, les taux du droit de consommation relatif aux
> produits repris au tarif douanier sous les rubriques n° **27-09 à 27-11 sont fixés par décret**." »

> « **Article 36** *(p. 2150, intitulé « Suppression de la déduction du droit de consommation »)*. —
> Est abrogé le **renvoi (1)** figurant au tableau annexé à la loi n° 88-62 du 2 juin 1988. »
> *(C'est-à-dire la déduction de 50 % au profit des hôteliers — § 2.4.)*

| | |
|---|---|
| Signature | **30 décembre 1989** |
| Publication | **JORT n° 88 des 29-31 décembre 1989**, tome 132 ; **art. 29 p. 2148-2149**, **art. 34, 35 et 36 p. 2150** (pieds de page lus) |
| Date d'effet | **1er janvier 1990** — *déduit, non lu* |

- URL FR : `https://www.pist.tn/jort/1989/1989F/Jo08889.pdf` — **vérifiée** (HTTP 200)
- URL AR : `https://www.pist.tn/jort/1989/1989A/Ja08889.pdf` (champ `pdf_ar`)
- **Le PDF local n'a pas de couche texte** (`pdftotext` rend 160 octets) : lecture à l'image
  obligatoire. PDF page N = page JORT 2141 + N.

### 3.3 Le cas ordinaire : la loi de finances modifie directement le tableau

Exemple type, lu à l'image : **article 38 de la loi n° 90-111 (LF 1991)**, sous l'intitulé
« Suppression et réduction du droit de consommation dû sur certains produits » :

> « La liste des produits soumis au droit de consommation annexée à la loi n° 88-62 du 2 juin 1988
> […] est modifiée conformément au **tableau "N"** indiqué à la deuxième partie de la présente loi. »

| | |
|---|---|
| Signature | **31 décembre 1990** |
| Publication | **JORT n° 86 des 28-31 décembre 1990**, tome 133, **p. 2052** (pied de page lu) |
| Date d'effet | **1er janvier 1991** — *déduit, non lu* |

*Le contenu du tableau « N » n'a pas été lu : il figure dans la deuxième partie de la loi (tableaux
annexes, p. 2062-2204). À dépouiller si le chapitre a besoin du détail 1991.*

---

## 4. Chronologie des mouvements de périmètre et de taux

### 4.1 Tableau d'ensemble

| Effet | Texte | Ce qu'il fait | Publication | Statut |
|---|---|---|---|---|
| 1er juillet 1988 | **loi 88-62** | institue le droit ; tableau d'origine | n° 39, 10 juin 1988, p. 847-856 | **lu à l'image** |
| 1er janvier 1989 | **loi 88-145 (LF 1989), art. 27** | **supprime** le droit sur une longue liste de positions | n° 87, 30-31 déc. 1988, p. 1795-1796 | **lu à l'image** |
| 1er janvier 1989 | **loi 88-145, art. 86** | habilitation « boissons » (22-03, 22-05 à 22-09) | n° 87, p. 1801 | **lu à l'image** |
| 31 déc. 1988 / 1989 | **décret 88-2002 du 27 déc. 1988** | suppression du droit pour certains produits, réduction ou suspension de TVA | n° 87, p. 1873-1876 | notice seule |
| 1989 | **décrets 89-479 et 89-1348** | modifient le tableau annexé | n° 33, 12 mai 1989, p. 818-819 ; n° 63, 19 sept. 1989, p. 1453 | notice seule |
| 1er janvier 1990 | **loi 89-115 (LF 1990), art. 29, 34, 35, 36** | sorties de produits ; facturation à l'identique ; habilitation pétrole ; abrogation du renvoi (1) | n° 88, 29-31 déc. 1989, p. 2148-2150 | **lu à l'image** |
| 1er janvier 1991 | **loi 90-111 (LF 1991), art. 38** | modifie la liste par le tableau « N » | n° 86, 28-31 déc. 1990, p. 2052 | **lu à l'image** |
| **5 février 1991** | **décret 91-550** | nouveaux tarifs 27-09, Ex 27-10, Ex 27-11 | n° 29, 30 avril 1991, p. 936 | **lu à l'image** |
| **5 février 1991** | **décret 91-551** | nouveaux taux 22-03 à 22-08 | n° 29, 30 avril 1991, p. 936-937 | **lu à l'image** |
| 1992-1994 | **LF 1992 art. 44 ; LF 1993 art. 110 ; LF 1994 art. 50** | modifient la liste | n° 90/1991 ; n° 88/1992 ; n° 100/1993 | liste DGELF |
| 1994 | **décret 94-816** | taux du droit de consommation sur les **hydrocarbures** | n° 30, 19 avril 1994, p. 628-629 | notice seule |
| 1995-1999 | **LF 1995 art. 64 ; LF 1997 art. 51 ; LF 1998 art. 47 ; LF 1999 art. 50** | modifient la liste | — | liste DGELF |
| 24 juillet 1997 | **décret 97-1368** | régime fiscal des produits 22-03 à 22-08 (alcools) | n° 59, 25 juillet 1997, p. 1301-1316 | notice + texte DGELF |
| 6 mai 1998 | **décret 98-952, art. 2** | **transfère les produits pétroliers de la TVA réduite au droit de consommation** et en fixe le tarif | n° 35, 1er mai 1998, p. 923 | établi (dossier TVA) |
| **22 avril 1999** | **décret 99-894** | fixe le **tarif complet** du droit sur les produits pétroliers | n° 33, 23 avril 1999, p. 624-625 | **lu à l'image** |
| 2003-2005 | **LF 2003 art. 65 ; loi 2002-103 ; LF 2004 art. 37 ; LF 2005 art. 35 et 73** | pneumatiques, voitures ≤ 4 CV, artisanat, café soluble | n° 104/2003 p. 3726 et 3731 ; n° 105/2004 p. 3437-3438 et 3444 | notices |
| **1er janvier 2007** | **loi 2006-80, art. 14** | **ajoute cinq lignes** au tableau (transfert depuis le taux majoré de TVA) | n° 101, 19 déc. 2006, **p. 4302** | **lu (couche texte, pied de page lu)** |
| 1er janvier 2007 | **LF 2007 (loi 2006-85), art. 64 et 84** | fiscalité des véhicules de tourisme et à piston rotatif | n° 103, 26 déc. 2006, p. 4390-4391 et 4395 | notices |
| 1er janvier 2008 | **LF 2008 (loi 2007-70), art. 58** | soumet le **gaz naturel carburant** au droit ; ajoute la STEG à l'article 2 | n° 104, 28 déc. 2007, p. 4367 | notice |
| 1er janvier 2013 | **LF 2013 (loi 2012-27), art. 43** | prix de transfert : liquidation sur le prix des entrepositaires | — | annotation DGELF |
| 1er janvier 2014 | **LF 2014 (loi 2013-54), art. 70** | dolomie ; bains et douches équipés de jacuzzi | n° 105, 31 déc. 2013, p. 3689-3690 | notice |
| **1er janvier 2016** | **LF 2016 (loi 2015-53), art. 44** | **abroge et remplace le tableau en entier** | n° 104, 29 déc. 2015, **p. 3150 et s.** | **lu (PDF officiel, pied de page lu)** |
| 1er janvier 2016 | **LF 2016, art. 45** | abroge les sous-paragraphes 3 et 4 de l'art. 1er ; restitution aux grossistes | n° 104, **p. 3152-3153** | **lu** |
| 1er janvier 2016 | **LF 2016, art. 57** | prix de transfert : ventes des fabricants | n° 104, **p. 3155** | **lu** |
| **1er janvier 2018** | **LF 2018 (loi 2017-66), art. 45** | **abroge et remplace le tableau en entier** (2e refonte) | n° 101, 19 déc. 2017, **p. 4281 et s.** | **lu (PDF officiel, pied de page lu)** |
| 1er janvier 2018 | **LF 2018, art. 22** | ajoute l'**article 6 bis** (suspension, véhicules tout terrain) | n° 101 ; **page non établie** | lu (texte), page TODO |
| 1er janvier 2019 | **LF 2019 (loi 2018-56), art. 62, 69, 80** | véhicules 8-9 places pour handicapés ; mélanges odoriférants (Ex 33.02) ; motocycles ≤ 125 cm3 | n° 104, 28 déc. 2018, **p. 4548, 4550, 4553** | **lu (PDF officiel)** |
| 1er janvier 2021 | **LF 2021 (loi 2020-46), art. 20, 21, 22** | révision de taux (bière, vins, tabac chauffé, maassil…) | n° 128, 25 déc. 2020 ; **pages non établies** | liste + annotations DGELF |
| 1er janvier 2022 | **décret-loi 2021-21 (LF 2022), art. 30, 37, 52, 65** | modifie l'art. 6 ; exonère certaines préparations nutritionnelles | n° 119, 28 déc. 2021, p. 3257-3369 (ensemble) ; **pages des articles non établies** | liste + annotations DGELF |

*La colonne « Effet » reprend, quand il est écrit, l'article de date d'effet du texte ; sinon elle
applique le régime de droit commun des lois de finances (1er janvier), ce qui est signalé comme
déduit dans le corps de la note.*

### 4.2 Le premier reflux, dès la première loi de finances — loi 88-145, art. 27 — *établi (JORT, lu à l'image, p. 1795-1796)*

Sous l'intitulé « **Suppression du droit de consommation sur certains produits** » :

> « **Article 27.** — Est supprimé le droit de consommation appliqué aux produits figurant au tableau
> annexé à la loi n° 88-62 du 2 juin 1988 sus-visée et repris sous les numéros des positions
> tarifaires suivantes : […] »

Liste lue à l'image (extraits) : 02-06 viandes et abats salés ou séchés ; Ex 03-02 poissons séchés ou
fumés ; Ex 16-01 saucisses et saucissons ; Ex 16-02 préparations et conserves de viandes ; Ex 16-03
extraits et jus de viande ; 16-05 crustacés et mollusques ; Ex 19-02 poudres pour crèmes et
puddings ; 21-05 préparations pour soupes et potages ; **Ex 25-15 marbre local** ; 34-05 cirages et
encaustiques ; Ex 39-07 ouvrages en matière plastique ; Ex 42-03 vêtements en cuir ; 42-05 autres
ouvrages en cuir ; 43-04 pelleteries factices ; 44-27 ouvrages de tabletterie ; puis *(p. 1796)*
Ex 58-04 velours et peluches ; 58-08 et 58-09 tulles et dentelles ; 66-01 et 66-03 parapluies et
parasols ; Ex 69-14 ouvrages en céramique ; Ex 70-09 miroirs ; Ex 70-13 verrerie de table ; Ex 70-14
verrerie d'éclairage ; Ex 73-36 poêles et cuisinières ; Ex 73-38 articles d'hygiène en fonte ou
acier ; Ex 74-17 et Ex 74-18 ustensiles et articles en cuivre ; Ex 82-09 et Ex 82-14 couverts ;
Ex 83-07 appareils d'éclairage ; **Ex 84-15 réfrigérateurs et congélateurs à usage domestique** ;
Ex 84-17 chauffe-eau non électriques ; Ex 85-20 et Ex 85-21 lampes et tubes ; 90-02 à Ex 90-07
optique et lunetterie.

*Fait intéressant pour le récit : le droit de consommation a donc commencé à refluer **six mois après
son entrée en vigueur**, et ce reflux porte d'abord sur des biens d'équipement ménager et des
produits alimentaires transformés.*

### 4.3 Deux décrets rétroactifs — décrets 91-550 et 91-551 — *établi (JORT, lu à l'image, p. 936-937)*

Les deux décrets, signés le **20 avril 1991** et publiés au **JORT n° 29 du 30 avril 1991**,
appliquent leurs dispositions « **à partir du 5 février 1991** » (art. 2 du 91-550) et « **à compter
du 5 février 1991** » (art. 2 du 91-551). **Leur effet précède donc leur publication de près de trois
mois** : c'est un point à relever, non à taire.

- **Décret 91-550** (p. 936) : nouveaux tarifs pour 27-09, Ex 27-10 et Ex 27-11. Relevés à l'image :
  huiles brutes **0,400 D/hl** ; essence super **18,9456 D/hl** ; essence normale **16,4888 D/hl** ;
  essence avion **1,990 D/hl** ; white spirit non dénaturé **1,690 D/hl** ; pétrole lampant
  **2,9839 D/hl** ; gas-oil **4,7456 D/hl** ; fuel-oil domestique **7,137 D/100 kg** ; fuel-oil léger
  **3,900 D/100 kg** ; fuel-oil lourd **2,1836 D/100 kg** ; huiles de graissage **0,997 D/100 kg** ;
  huiles de vaseline et paraffine **0,875 D/hl** ; autres **1,690 D/hl** ; propane et butane
  **27,386 D/tonne**.
- **Décret 91-551** (p. 936-937) : nouveaux taux pour 22-03 à 22-08, avec apparition d'une
  **tarification à l'unité par contenance de bouteille** pour les vins de consommation courante, les
  AOC et les « premier cru » (de 0,315 D à 1,100 D l'unité selon la contenance) — première apparition,
  dans le corpus lu, d'un tarif par bouteille.

**Anomalie de visa, à signaler et à ne pas trancher.** Le décret 91-550 vise « la **loi n° 88-145 du
31 décembre 1988**, portant loi de finances pour la gestion 1989 et **notamment son article 35** ».
Or l'article 35 de cette loi, **lu à l'image (p. 1797)**, concerne la **contribution au fonds de
promotion des logements pour les salariés** et non le droit de consommation. L'habilitation
réellement pertinente en matière pétrolière est l'**article 35 de la loi n° 89-115 (LF 1990)**
(§ 3.2). Tout indique une **confusion de visa dans le JORT lui-même** ; le précis peut le mentionner
comme tel, sans affirmer laquelle des deux références le rédacteur avait en vue. Le décret 91-551,
lui, vise l'**article 86 de la loi 88-145**, qui est bien l'habilitation « boissons » (§ 3.1) : son
visa est cohérent.

*Second point de vigilance sur ces visas* : les deux décrets visent « la loi n° **91-111** du
31 décembre 1990, portant loi de finances pour la gestion 1991 » ; la loi de finances pour 1991 est
la loi n° **90-111** du 31 décembre 1990 (`jort_cache`, JORT n° 86 de 1990). Lecture à l'image d'un
fac-similé de qualité moyenne : **ne pas citer ce numéro sans revérification**.

---

## 5. L'état actuel du tableau — ce qu'il faut citer, et sous quelle forme

Le tableau en vigueur descend de l'**article 45 de la LF 2018**, lui-même remplaçant celui de
l'article 44 de la LF 2016. Deux sources françaises fiables :
1. le **PDF officiel de la LF 2018** (couche texte fiable), JORT n° 101 du 19 décembre 2017,
   **p. 4281 et suivantes** ;
2. le **code consolidé DGELF 2023**, partie III « **DROIT DE CONSOMMATION** » (p. 84 à 97 de
   l'ouvrage), qui reproduit la loi 88-62 annotée, la liste des textes modificatifs, et le tableau à
   jour.

Physionomie du tableau actuel (DGELF 2023, couche texte) — à comparer avec 1988 :

- **Alimentation et boissons non alcoolisées** : sucreries sans cacao 10 % ; chocolat 10 % ; jus de
  fruits (hors jus de fruits frais) 25 % ; extraits de café et de thé 25 % ; sauces et condiments
  25 % ; glaces de consommation 10 % ; préparations alimentaires non dénommées 40 % ; eaux
  aromatisées et boissons non alcooliques 25 %.
- **Boissons alcoolisées** : bière classée **0,024 D/cl** ; vins en vrac 7,500 D/hl ; vins mousseux
  24,000 D l'unité ; autres vins **2,4 D/litre** ; vermouths 100 % ; alcools éthyliques 16,000 D/hl,
  **570,000 D/hl** pour ceux destinés à la fabrication de boissons alcoolisées ; eaux-de-vie,
  whiskies, pastis **100 %**.
- **Tabac** : tabacs bruts 40 % ; cigares et cigarettes **135 %** ; autres tabacs fabriqués 135 % ;
  **maassil et jirak 10 %** ; **tabac chauffé 50 %** *(ces deux dernières lignes modifiées par
  l'art. 22 de la LF 2021)* ; papier à cigarettes 40 % ; solutions et cartouches pour cigarettes
  électroniques 10 %.
- **Matériaux** : marbres et pierres calcaires en blocs 10 %, en plaques 25 % ; granit et basalte
  10 % / 25 % ; dolomie crue 25 % ; pierres de taille travaillées 50 % ; carreaux de céramique 10 %.
- **Produits pétroliers** : tarifs spécifiques par hectolitre, par 100 kg, par tonne et par m3 (§ 8).
- **Parfumerie** : parfums et eaux de toilette 25 % ; produits de beauté 25 % ; mélanges odoriférants
  pour l'industrie des boissons (330210) 40 %.
- **Véhicules** : barème par cylindrée, distinguant les véhicules importés par les **concessionnaires
  agréés** et par les **autres personnes** — c'est, en volume budgétaire et en visibilité publique, la
  part la plus importante du tableau actuel. La note commune 17/2018 en donne l'économie : taux variant
  « entre 50 % et 200 % selon la cylindrée » pour le n° 87.03 avant 2018.

*Pour un état en vigueur à la date de rédaction, la source à citer est le **code consolidé DGELF**,
non le tableau de 1988 ni même celui de 2018 : quatre lois de finances l'ont amendé depuis.*

---

## 6. Articulation avec la TVA — la réponse à la question laissée ouverte

**Le cumul est établi sur deux textes lus. L'inclusion du droit de consommation dans l'assiette de
la TVA ne résulte pas d'une phrase qui l'énoncerait : elle se déduit *a contrario* du caractère
limitatif des exclusions de l'article 6-I du code de la TVA. Cette déduction est toutefois
expressément confirmée par la doctrine administrative, qui en donne un exemple chiffré (§ 6.1) —
de sorte que le point peut être écrit sans réserve, à condition de citer les deux sources.**

| | Ce qui entre dans l'assiette | Ce qui en est exclu |
|---|---|---|
| **Droit de consommation** (loi 88-62, art. 4, *lu à l'image*) | à l'importation : la valeur en douane — en régime intérieur : le prix de vente **tous frais, droits et taxes compris** | **le droit de consommation lui-même** et **la TVA** |
| **TVA** (code, art. 6-I, *DGELF, couche texte*) | le prix des marchandises, travaux ou services **tous frais, droits et taxes inclus**, et la valeur des objets remis en paiement | **la TVA**, les subventions d'exploitation, les prélèvements conjoncturels et de compensation |

Trois conséquences, à écrire en clair (et corroborées au § 6.1) :
1. **Le droit de consommation se cumule avec la TVA** : rien dans la loi 88-62 ne l'exonère de TVA, et
   l'article 6 du code de la TVA ne l'exclut pas de la base.
2. **Il entre dans l'assiette de la TVA** : la TVA frappe donc un prix qui inclut déjà le droit de
   consommation. C'est une **cascade**, non une juxtaposition.
3. **La réciproque est fausse** : la TVA est expressément exclue de l'assiette du droit de
   consommation.

**Deux tempéraments, tous deux dans les textes** : (i) l'article 5 de la loi 88-62 ouvre une
**imputation** du droit supporté en amont sur les matières entrant intégralement dans la composition
du produit final — mécanisme voisin, mais plus étroit, que la déduction de TVA ; (ii) l'article 4
neutralise l'effet du droit sur les **marges** des entrepositaires et marchands de boissons
alcoolisées, qui le « retransmettent pour les mêmes montants ». Le renvoi (1) du tableau de 1988
autorisait de surcroît les **hôteliers** à déduire de leur TVA 50 % du droit sur les boissons
alcoolisées — **abrogé par l'article 36 de la LF 1990** : ne pas le présenter comme en vigueur.

### 6.1 La cascade, confirmée et chiffrée par la doctrine — note commune n° 29/2007

La **note commune n° 29/2007** est consacrée à cette question précise : « Détermination de l'assiette
de calcul de la TVA, du droit de consommation perçu selon un taux ad-valorem, de la taxe au profit du
Fonds de Développement de la Compétitivité dans le Secteur Industriel, et de la taxe au profit du
Fonds National de la maîtrise de l'énergie ». Elle énonce :

> « La liquidation de la TVA continue à être effectuée sur la base d'une assiette qui **comprend
> lesdites taxes ainsi que le droit de consommation**, conformément aux dispositions de l'article 6 du
> code de la TVA. »

et l'illustre par un exemple : un industriel de produits cosmétiques vend 500 D hors taxes des
produits soumis au droit de consommation de 10 %, à la taxe FODEC de 1 % et à la TVA de 18 % :

> droit de consommation 500 × 10 % = **50 D** ; taxe FODEC 500 × 1 % = **5 D** ; **assiette de la TVA
> = 500 + 50 + 5 = 555 D** ; TVA due 555 × 18 % = **99,900 D** ; prix de vente TTC **654,900 D**.

**Nuance à ne pas omettre**, donnée par la même note : pour éviter une double prise en compte, les
taxes FODEC et FNME « sont liquidées […] sur la base d'une assiette qui **ne comprend pas** le droit
de consommation », et le droit de consommation « est liquidé sur la base d'une assiette qui ne
comprend pas lesdites taxes ». Les deux prélèvements parafiscaux et le droit de consommation sont
donc **parallèles entre eux**, et tous trois **en amont** de la TVA.

*Rappel de statut : une note commune est de la doctrine administrative, jamais une source du droit.
Elle est citée ici parce qu'elle confirme une lecture a contrario, non parce qu'elle la fonde.*

---

## 7. Le transfert de 2007 depuis le taux majoré de TVA

**Vérifié, et plus étroit que ne le suggère une formule générale.**

> **Loi n° 2006-80 du 18 décembre 2006**, chapitre II « En matière de taxe sur la valeur ajoutée et du
> droit de consommation », sous l'intitulé « **Suppression du taux de 29 % de la TVA et imposition de
> certains produits au droit de consommation** » :
> « **ARTICLE 13 :** Est supprimé le numéro 2 du deuxième paragraphe de l'article 7 du code de la TVA.
> **ARTICLE 14 :** Sont ajoutés au **tableau annexé à la loi n° 88-62 du 2 juin 1988** portant refonte
> de la réglementation relative au droit de consommation telle que modifiée et complétée par les
> textes subséquents les produits repris par le tableau suivant : »

| N° du tarif douanier | Désignation | Taux DC |
|---|---|---|
| 33-03 | Parfums et eaux de toilette | **10 %** |
| 33-04 | Produits de beauté ou de maquillage préparés, préparations pour l'entretien ou les soins de la peau (autres que médicaments), y compris préparations anti-solaires et pour bronzer ; préparations pour manucures ou pédicures | **10 %** |
| 84-15 | Machines et appareils pour le conditionnement de l'air comprenant un ventilateur à moteur et des dispositifs propres à modifier la température et l'humidité | **10 %** |
| EX 84-18 | Unités de réfrigération des machines et appareils pour le conditionnement de l'air du type « split system » | **10 %** |
| EX 84-22 | Machines à laver la vaisselle à chauffage électrique | **10 %** |

| | |
|---|---|
| Signature | **18 décembre 2006** |
| Publication | **JORT n° 101 du 19 décembre 2006**, tome 149 ; les **articles 13 et 14 et le tableau sont p. 4302** (pied de page lu dans la couche texte), les articles 15 à 19 p. 4303 |
| Date d'effet | **1er janvier 2007** — écrit : « **ARTICLE 19 :** Sous réserve des dispositions des articles de 5 à 12, les dispositions de la présente loi s'appliquent à compter du 1er janvier 2007. » |

- Local : `PDFs/JORT/2006/fr/Jo1012006.pdf` (couche texte exploitable)
- URL FR : `https://www.pist.tn/jort/2006/2006F/Jo1012006.pdf` — **vérifiée** (dossier TVA)

**Corroboration doctrinale** (note commune n° 24/2007, `markdown_output/Notes_Communes/…13_14_17_et_18_
de_la_loi_n2006-80…`) : « la suppression du taux de la TVA de 29 % et l'imposition des produits
concernés, à ladite taxe **au taux de 18 %** », avec « l'imposition **de certains produits** concernés
par la réduction du taux de la TVA de 29 % à 18 % **au droit de consommation au taux de 10 %** ». La
note confirme donc la lecture : **le transfert est sélectif**, le reste du tableau « C » passant
simplement au taux normal.

*Rectification à porter au chapitre TVA* : la phrase « les produits qui relevaient du taux majoré ont
été transférés au droit de consommation » est **trop large**. Formulation exacte : *le taux majoré est
supprimé et ses produits passent au taux normal de 18 %, cinq catégories d'entre eux étant
simultanément soumises au droit de consommation au taux de 10 %.*

---

## 8. Les produits pétroliers — un régime dans le régime

### 8.1 La chaîne des textes

1. **Loi 88-62, tableau annexé (1988)** : les positions 27-09, 27-10 et Ex 27-11 y figurent d'emblée,
   avec des tarifs spécifiques et le renvoi (2) sur la taxe unique de compensation (§ 2.3-2.4).
2. **Loi 89-115 (LF 1990), art. 35** : ajoute à l'article 1er l'alinéa qui renvoie **au décret** la
   fixation des taux pour 27-09 à 27-11 (§ 3.2, lu à l'image). *C'est l'acte fondateur du régime
   propre.*
3. **Décret 91-550 du 20 avril 1991** : premier exercice de cette habilitation (§ 4.3, lu à l'image).
4. **Décret n° 94-816 du 11 avril 1994**, « fixant les taux du droit de consommation sur les
   hydrocarbures », JORT n° 30 du 19 avril 1994, p. 628-629 — *notice seule, non lu*.
5. **Décret n° 98-952 du 27 avril 1998, art. 2** : fixe le tarif applicable aux produits **27-09,
   27-10 et 27-11** au moment où il **retire** ces produits du taux réduit de TVA. Effet au **6 mai
   1998**. *Établi au dossier TVA ; référence `decret-98-952-fiscalite-petrole-electricite` déjà en
   bibliographie.*
6. **Décret n° 99-894 du 19 avril 1999**, « fixant le tarif du droit de consommation applicable aux
   produits pétroliers » — **lu à l'image** (§ 8.2).
7. **Refontes de 2016 et 2018** : les tarifs pétroliers sont réécrits **dans le tableau annexé**
   lui-même, puis révisés par les articles 45 de la LF 2018 et 20 de la LF 2021.

### 8.2 Décret n° 99-894 — *établi (JORT, lu à l'image, p. 624-625)*

| | |
|---|---|
| Signature | **19 avril 1999** |
| Publication | **JORT n° 33 du 23 avril 1999**, tome 142, **p. 624-625** (pieds de page lus) |
| Date d'effet | **22 avril 1999** — écrit : « Art. 2. — Les dispositions du présent décret s'appliquent **à compter du 22 avril 1999** » |

Visa, lu à l'image — il confirme toute la chaîne : « Vu le code de la taxe sur la valeur ajoutée, Vu
la loi n° 88-62 du 2 juin 1988 […] telle que modifiée et complétée par les textes subséquents et
**notamment l'article 35 de la loi n° 89-115 du 30 décembre 1989 portant loi de finances pour l'année
1990** ».

> « **Article premier.** — Le tarif du droit de consommation applicable aux produits relevant des
> numéros **27-09, 27-10 et 27-11** du tarif des droits de douane est fixé conformément au tableau
> suivant : »

| Position | Produit | Tarif 1999 |
|---|---|---|
| 27-09 | huiles brutes de pétrole ou de minéraux bitumineux | **0,400 D/hl** |
| EX 27-10 | essence super | **23,6325 D/hl** |
| EX 27-10 | essence super **sans plomb** | **19,9615 D/hl** |
| EX 27-10 | essence normale | **21,8013 D/hl** |
| EX 27-10 | essence avion (kérosène, y compris carburéacteur) | **1,990 D/hl** |
| EX 27-10 | white spirit non dénaturé | **1,690 D/hl** |
| EX 27-10 | pétrole lampant | **3,5404 D/hl** |
| EX 27-10 | gaz-oil | **5,8309 D/hl** |
| EX 27-10 | fuel-oil domestique | **8,1904 D/100 kg** |
| EX 27-10 | fuel-oil léger | **3,900 D/100 kg** |
| EX 27-10 | fuel-oil lourd | **2,0749 D/100 kg** |
| EX 27-10 | huiles de graissage et lubrifiants | **0,997 D/100 kg** |
| EX 27-10 | huiles de vaseline et de paraffine | **0,875 D/hl** |
| EX 27-10 | autres, à l'exclusion du white spirit dénaturé | **1,690 D/hl** |
| EX 27-11 | gaz de pétrole, propane et butane, bouteilles ≤ 13 kg | **8,256 D/tonne** |
| EX 27-11 | gaz de pétrole, propane et butane, en vrac ou bouteilles > 13 kg | **44,700 D/tonne** |

- Local : `PDFs/JORT/1999/fr/Jo03399.pdf` (**pages 16-17 du PDF** ; PDF page N = page JORT 608 + N)
- URL FR : `https://www.pist.tn/jort/1999/1999F/Jo03399.pdf` — **vérifiée** (HTTP 200)
- URL AR : `https://www.pist.tn/jort/1999/1999A/Ja03399.pdf` — **vérifiée** (HTTP 200)
- **Attention** : la couche texte de ce fascicule est **illisible** (police décalée, « 75$'8&7,21 » pour
  « TRADUCTION ») ; tout `grep` y échoue sans valeur probante. Lecture à l'image obligatoire.

### 8.3 Deux observations pour la rédaction

1. **L'essentiel du tarif est gelé depuis 1999 ; le mouvement s'est concentré sur deux lignes.**
   Sont **inchangés** entre le décret 99-894 et le code consolidé 2023 : huiles brutes 0,400 D/hl ;
   **essence super 23,632 D/hl** ; **essence normale 21,801 D/hl** ; essence avion 1,990 ; white
   spirit 1,690 ; fuel-oil léger 3,900 D/100 kg ; huiles de graissage 0,997 D/100 kg ; vaseline et
   paraffine 0,875 D/hl ; « autres » 1,690 D/hl ; gaz en bouteilles ≤ 13 kg **8,256 D/tonne** et en
   vrac **44,700 D/tonne**. *Un quart de siècle sans révision nominale : à taux spécifique, cela
   équivaut à une érosion réelle continue — constat à formuler, sans le chiffrer faute de série de
   prix.*
   Ont **augmenté** : l'**essence super sans plomb**, de **19,9615 à 41,382 D/hl** — elle a **plus que
   doublé** et est devenue la ligne la plus lourde du tarif, alors qu'en 1999 elle était **moins
   taxée** que l'essence super ; et le **gaz-oil**, de **5,8309 à 12,116 D/hl**. S'y ajoute une ligne
   qui n'existait pas en 1999, le **gaz-oil à teneur en soufre réduite**, à **29,618 D/hl**, ainsi que
   le **gaz naturel carburant** à 0,113 D/m3 (introduit par l'art. 58 de la LF 2008). Le fuel-oil
   domestique passe de 8,1904 à 8,190 D/100 kg (stabilité) et le fuel-oil lourd de 2,0749 à
   2,074 D/100 kg.
   *Les jalons sûrs, tous lus sur pièce, sont **1988**, **1991**, **1999** et l'**état consolidé
   2023** : c'est la série qui permettra la vue d'évolution qu'exige la convention du précis, plutôt
   qu'un chiffre ponctuel.*
2. **L'habilitation de l'article 1er alinéa 2 n'a pas été abrogée** (elle figure toujours au code
   consolidé DGELF 2023) alors que les tarifs pétroliers sont de nouveau inscrits **dans le tableau
   annexé** par les lois de finances 2016 et 2018. Loi et décret peuvent donc, en l'état, fixer les
   mêmes tarifs. **Non établi** : aucun texte lu n'articule les deux. *À signaler comme une question
   ouverte, pas à trancher.*

---

## 9. Lacunes — ce qui n'est pas établi et ne doit pas être écrit

1. **Pages 850 à 854 du tableau de 1988** : lues en OCR seulement. Les taux qu'elles portent (textiles,
   bonneterie, ouvrages divers) **ne doivent pas être cités**. Lecture à l'image : `Jo03988.pdf`,
   pages 30 à 34 du PDF.
2. **Tableau « N » de la LF 1991** (loi 90-111, deuxième partie, p. 2062-2204) : non lu. Le détail des
   suppressions et réductions de 1991 est donc **inconnu**.
3. **Pages des articles 20, 21 et 22 de la LF 2021** (loi n° 2020-46) : le champ `pages` de
   `jort_cache.db` est **vide** pour ce texte, et les deux PDF locaux `Loi_de_Finances… 2021` et
   `…2022` sont **corrompus** (`Couldn't read xref table` ; `pypdf` : `Stream has ended
   unexpectedly`). Le fascicule **JORT 2020 n° 128 existe en français** sur pist.tn (HTTP 200,
   59,7 Mo) : c'est là qu'il faut aller chercher la pagination. **TODO**.
4. **Pages des articles 30, 37, 52 et 65 du décret-loi 2021-21 (LF 2022)** : même situation ; le
   fascicule **JORT 2021 n° 119 existe en français** (HTTP 200, 45,2 Mo), la loi y occupe
   p. 3257-3369, mais la page de chaque article n'est pas établie. **TODO**.
5. **Page de l'article 22 de la LF 2018** (création de l'article 6 bis) : le texte a été lu dans le PDF
   officiel, mais son pied de page n'a pas été relevé. **TODO** (il est antérieur à la p. 4280).
6. **Décrets 88-2002, 89-479, 89-1348, 94-816, 97-1368, 2002-627, 2007-1977, 2013-929 et décret
   gouvernemental 2015-1768** : connus par la liste du code consolidé DGELF et par les notices de
   `jort_cache.db`, **non lus sur pièce**. Leurs tarifs ne doivent pas être cités d'après ces sources.
7. **Numéro de la loi de finances pour 1991 tel qu'il figure au visa des décrets 91-550 et 91-551**
   (« 91-111 » lu à l'image, contre « 90-111 » dans la base) : **divergence non résolue** (§ 4.3).
8. **Date d'effet des lois de finances** : sauf pour la loi 2006-80 (art. 19, lu), aucune clause de
   date d'effet n'a été lue. Les « 1er janvier » du tableau du § 4.1 sont **déduits**.
9. **Rendement budgétaire du droit de consommation** : aucune série de recettes n'a été recherchée
   dans le cadre de ce dossier. Or la convention du précis interdit le chiffre ponctuel sans vue
   d'évolution : **avant de chiffrer quoi que ce soit, ouvrir un dossier « recettes »** (tableaux « A »
   des lois de finances, ou publications de la DGI / du ministère des finances).
10. **Version arabe de la loi 88-62** : le fascicule arabe `Ja03988.pdf` n'a pas été ouvert. Le terme
    arabe retenu (§ Annexe B) est attesté par les **objets arabes de `jort_cache.db`**, non par le
    texte de 1988 lui-même.

---

## Annexe A — Références candidates (CSL-JSON)

### A.1 Déjà présentes dans `precis/fr/fiscalite/references.json` — à réutiliser telles quelles

`loi-88-61-tva` · `decret-88-1109-calendrier-tva` · `decret-98-952-fiscalite-petrole-electricite` ·
`loi-2006-80-reduction-taux` · `dgelf-code-tva-2023` · `lf-2016` (loi 2015-53) · `lf-2018`
(loi 2017-66).

*Avertissement d'outillage (`docs/notes/outillage-sources.md`, § 7) : `scripts/sync_biblio.py` est en
lecture seule depuis Zotero. Toute clé ajoutée à la main dans `references.json` sera **écrasée** au
prochain sync si elle n'est pas montée dans Zotero. Passer par `docs/notes/biblio-a-rapatrier.md`.*

### A.2 À créer

```json
[
  {
    "id": "loi-88-62-droit-consommation",
    "type": "legislation",
    "title": "Loi n° 88-62 du 2 juin 1988, portant refonte de la réglementation relative aux droits de consommation",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "39",
    "volume": "131",
    "page": "847-856",
    "issued": {"date-parts": [[1988, 6, 2]]},
    "URL": "https://www.pist.tn/jort/1988/1988F/Jo03988.pdf",
    "note": "Publiée le 10 juin 1988 ; applicable à compter du 1er juillet 1988 (décret n° 88-1109, art. 2, conformément à l'art. 8 de la loi). Huit articles p. 847, tableau annexé p. 847-856. Même fascicule que les lois 88-60, 88-61 (code de la TVA), 88-63 et 88-64. Édition arabe : https://www.pist.tn/jort/1988/1988A/Ja03988.pdf. Articles et tableau (p. 847-849, 855-856) lus à l'image ; p. 850-854 non relues."
  },
  {
    "id": "loi-88-145-lf-1989",
    "type": "legislation",
    "title": "Loi n° 88-145 du 31 décembre 1988, portant loi de finances pour la gestion 1989",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "87",
    "volume": "131",
    "page": "1793-1805",
    "issued": {"date-parts": [[1988, 12, 31]]},
    "URL": "https://www.pist.tn/jort/1988/1988F/Jo08788.pdf",
    "note": "Publiée les 30-31 décembre 1988. Art. 27 (p. 1795-1796) : suppression du droit de consommation sur une longue liste de positions tarifaires. Art. 86 (p. 1801) : habilitation à fixer par décret les taux applicables aux produits 22-03 et 22-05 à 22-09. Les deux articles lus à l'image. Édition arabe : https://www.pist.tn/jort/1988/1988A/Ja08788.pdf (vérifiée). URL FR vérifiée (HTTP 200)."
  },
  {
    "id": "loi-89-115-lf-1990",
    "type": "legislation",
    "title": "Loi n° 89-115 du 30 décembre 1989, portant loi de finances pour la gestion 1990",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "88",
    "volume": "132",
    "page": "2144-2155",
    "issued": {"date-parts": [[1989, 12, 30]]},
    "URL": "https://www.pist.tn/jort/1989/1989F/Jo08889.pdf",
    "note": "Publiée les 29-31 décembre 1989. Art. 29 (p. 2148-2149) : suppression du droit sur une liste de positions. Art. 34 (p. 2150) : facturation à l'identique, ajoutée à l'art. 5 de la loi 88-62. Art. 35 (p. 2150) : les taux des produits 27-09 à 27-11 sont fixés par décret — alinéa 2 de l'art. 1er de la loi 88-62. Art. 36 (p. 2150) : abrogation du renvoi (1) du tableau annexé (déduction de 50 % par les hôteliers). Tous lus à l'image ; le PDF local n'a pas de couche texte. Édition arabe : https://www.pist.tn/jort/1989/1989A/Ja08889.pdf. URL FR vérifiée (HTTP 200)."
  },
  {
    "id": "loi-90-111-lf-1991",
    "type": "legislation",
    "title": "Loi n° 90-111 du 31 décembre 1990, portant loi de finances pour la gestion 1991",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "86",
    "volume": "133",
    "page": "2049-2204",
    "issued": {"date-parts": [[1990, 12, 31]]},
    "URL": "https://www.pist.tn/jort/1990/1990F/Jo08690.pdf",
    "note": "Publiée les 28-31 décembre 1990. Art. 38 (p. 2052), « Suppression et réduction du droit de consommation dû sur certains produits » : modifie la liste annexée à la loi 88-62 conformément au tableau « N » de la deuxième partie de la loi (tableaux annexes, p. 2062-2204, non lus). Art. 38 lu à l'image. Édition arabe : https://www.pist.tn/jort/1990/1990A/Ja08690.pdf (champ pdf_ar)."
  },
  {
    "id": "decret-91-550-tarif-petroliers",
    "type": "legislation",
    "title": "Décret n° 91-550 du 20 avril 1991, portant modification du tableau annexé à la loi n° 88-62 du 2 juin 1988, portant refonte de la réglementation relative au droit de consommation",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "29",
    "volume": "134",
    "page": "936",
    "issued": {"date-parts": [[1991, 4, 20]]},
    "URL": "https://www.pist.tn/jort/1991/1991F/Jo02991.pdf",
    "note": "Publié le 30 avril 1991 ; art. 2 : applicable à partir du 5 février 1991 — effet rétroactif de près de trois mois. Fixe les tarifs des produits 27-09, Ex 27-10 et Ex 27-11. Lu à l'image (page 4 du PDF). Anomalie : le visa cite « la loi n° 88-145 … notamment son article 35 », alors que cet article concerne le fonds de promotion des logements ; l'habilitation pertinente est l'art. 35 de la loi 89-115. Édition arabe : https://www.pist.tn/jort/1991/1991A/Ja02991.pdf. URL FR vérifiée (HTTP 200)."
  },
  {
    "id": "decret-91-551-tarif-boissons",
    "type": "legislation",
    "title": "Décret n° 91-551 du 20 avril 1991, portant modification du tableau annexé à la loi n° 88-62 du 2 juin 1988, portant refonte de la réglementation relative au droit de consommation",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "29",
    "volume": "134",
    "page": "936-937",
    "issued": {"date-parts": [[1991, 4, 20]]},
    "URL": "https://www.pist.tn/jort/1991/1991F/Jo02991.pdf",
    "note": "Publié le 30 avril 1991 ; art. 2 : mesures en vigueur à compter du 5 février 1991 — effet rétroactif. Fixe les taux des produits 22-03 à 22-08, avec une tarification à l'unité par contenance de bouteille pour les vins. Visa cohérent : art. 86 de la loi 88-145. Lu à l'image (pages 4-5 du PDF). Édition arabe : https://www.pist.tn/jort/1991/1991A/Ja02991.pdf (champ pdf_ar)."
  },
  {
    "id": "decret-99-894-tarif-petroliers",
    "type": "legislation",
    "title": "Décret n° 99-894 du 19 avril 1999, fixant le tarif du droit de consommation applicable aux produits pétroliers",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "33",
    "volume": "142",
    "page": "624-625",
    "issued": {"date-parts": [[1999, 4, 19]]},
    "URL": "https://www.pist.tn/jort/1999/1999F/Jo03399.pdf",
    "note": "Publié le 23 avril 1999 ; art. 2 : applicable à compter du 22 avril 1999. Visa : art. 35 de la loi n° 89-115 du 30 décembre 1989. Tarif complet des produits 27-09, 27-10 et 27-11 (première apparition d'une ligne « essence super sans plomb »). Lu à l'image (pages 16-17 du PDF) ; la couche texte du fascicule est corrompue et inutilisable. Édition arabe : https://www.pist.tn/jort/1999/1999A/Ja03399.pdf (vérifiée). URL FR vérifiée (HTTP 200)."
  },
  {
    "id": "decret-94-816-hydrocarbures",
    "type": "legislation",
    "title": "Décret n° 94-816 du 11 avril 1994, fixant les taux du droit de consommation sur les hydrocarbures",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "30",
    "volume": "137",
    "page": "628-629",
    "issued": {"date-parts": [[1994, 4, 11]]},
    "URL": "https://www.pist.tn/jort/1994/1994F/Jo03094.pdf",
    "note": "Publié le 19 avril 1994. DATE D'EFFET NON ÉTABLIE (texte non lu sur pièce : la clause d'application n'a pas été vérifiée). NON LU SUR PIÈCE : pagination issue de la notice de jort_cache.db ; cité par le code consolidé DGELF parmi les textes ayant modifié la liste. URL FR vérifiée (HTTP 200). Édition arabe : https://www.pist.tn/jort/1994/1994A/Ja03094.pdf."
  },
  {
    "id": "decret-97-1368-regime-alcools",
    "type": "legislation",
    "title": "Décret n° 97-1368 du 24 juillet 1997, relatif au régime fiscal des produits relevant des numéros 22-03 à 22-08 du tarif des droits de douane",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "59",
    "volume": "140",
    "page": "1301-1316",
    "issued": {"date-parts": [[1997, 7, 24]]},
    "URL": "https://www.pist.tn/jort/1997/1997F/Jo05997.pdf",
    "note": "Publié le 25 juillet 1997. DATE D'EFFET NON ÉTABLIE (clause d'application non vérifiée). Édition arabe : https://www.pist.tn/jort/1997/1997A/Ja05997.pdf (champ pdf_ar). Pris sur le fondement de l'art. 86 de la loi 88-145 (LF 1989). Ses annexes I, II et III ont été abrogées et remplacées par l'art. 2 du décret gouvernemental n° 2015-1768 du 10 novembre 2015. Texte reproduit dans le code consolidé DGELF 2023 ; fascicule NON LU SUR PIÈCE. URL FR vérifiée (HTTP 200)."
  },
  {
    "id": "decret-gouv-2015-1768-annexes-alcools",
    "type": "legislation",
    "title": "Décret gouvernemental n° 2015-1768 du 10 novembre 2015, modifiant le décret n° 97-1368 du 24 juillet 1997, relatif au régime fiscal des produits relevant des numéros 22.03 à 22.08 du tarif des droits de douanes",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "92",
    "issued": {"date-parts": [[2015, 11, 10]]},
    "URL": "https://www.pist.tn/jort/2015/2015F/Jo0922015.pdf",
    "note": "Publié le 17 novembre 2015. DATE D'EFFET NON ÉTABLIE (clause d'application non vérifiée). Abroge et remplace les annexes I, II et III du décret 97-1368 (tarif du droit de consommation sur les vins, bières, alcools et boissons alcoolisées). Pagination non renseignée dans jort_cache.db. URL FR vérifiée (HTTP 200). Édition arabe : https://www.pist.tn/jort/2015/2015A/Ja0922015.pdf."
  },
  {
    "id": "loi-2007-70-lf-2008",
    "type": "legislation",
    "title": "Loi n° 2007-70 du 27 décembre 2007, portant loi de finances pour l'année 2008",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "104",
    "page": "4367",
    "issued": {"date-parts": [[2007, 12, 27]]},
    "URL": "https://www.pist.tn/jort/2007/2007F/Jo1042007.pdf",
    "note": "Publiée le 28 décembre 2007 ; effet au 1er janvier 2008 (déduit du droit commun des lois de finances, clause non lue). Art. 58 : soumission au droit de consommation du gaz naturel destiné à l'utilisation comme carburant, et ajout de la STEG à la liste des assujettis (art. 2-5 de la loi 88-62). Pagination de notice ; texte non lu sur pièce. URL FR vérifiée (HTTP 200). Édition arabe : https://www.pist.tn/jort/2007/2007A/Ja1042007.pdf (champ pdf_ar)."
  },
  {
    "id": "loi-2013-54-lf-2014",
    "type": "legislation",
    "title": "Loi n° 2013-54 du 30 décembre 2013, portant loi de finances pour l'année 2014",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "105",
    "volume": "156",
    "page": "3689-3690",
    "issued": {"date-parts": [[2013, 12, 30]]},
    "URL": "https://www.pist.tn/jort/2013/2013F/Jo1052013.pdf",
    "note": "Publiée le 31 décembre 2013 ; effet au 1er janvier 2014 (déduit, clause non lue). Art. 70 : harmonisation de la fiscalité de la dolomie et des bains et douches équipés de jacuzzi — modifie le tableau annexé à la loi 88-62. Pagination de notice ; texte non lu sur pièce. URL FR vérifiée (HTTP 200). Édition arabe : https://www.pist.tn/jort/2013/2013A/Ja1052013.pdf (champ pdf_ar)."
  },
  {
    "id": "loi-2018-56-lf-2019",
    "type": "legislation",
    "title": "Loi n° 2018-56 du 27 décembre 2018, portant loi de finances pour l'année 2019",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "104",
    "page": "4548-4553",
    "issued": {"date-parts": [[2018, 12, 27]]},
    "URL": "https://www.pist.tn/jort/2018/2018A/Ja1042018.pdf",
    "note": "Publiée le 28 décembre 2018. ATTENTION : l'édition FRANÇAISE du fascicule est ABSENTE de pist.tn (Jo1042018.pdf répond 404, 289 octets) ; seule l'URL arabe existe et répond 200. Texte français lu dans PDFs/Lois_de_Finances/Loi_n_2018-56…pdf : art. 62 p. 4548 (véhicules 8-9 places pour handicapés, tableau annexé à la loi 88-62), art. 69 p. 4550 (champ du droit pour les mélanges odoriférants Ex 33.02 ; suppression pour certains produits alimentaires), art. 80 p. 4553 (motocycles). Pieds de page lus dans la couche texte."
  },
  {
    "id": "loi-2015-53-lf-2016-dc",
    "type": "legislation",
    "title": "Loi n° 2015-53 du 25 décembre 2015, portant loi de finances pour l'année 2016",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "104",
    "page": "3150-3155",
    "issued": {"date-parts": [[2015, 12, 25]]},
    "URL": "https://www.pist.tn/jort/2015/2015A/Ja1042015.pdf",
    "note": "DOUBLON à fusionner avec la clé existante lf-2016. Publiée le 29 décembre 2015. Édition française du fascicule ABSENTE de pist.tn (404) ; URL arabe vérifiée (200). Art. 44 (p. 3150 et s.) : abroge et remplace en entier le tableau annexé à la loi 88-62. Art. 45 (p. 3152-3153) : abroge les sous-paragraphes 3 et 4 de l'art. 1er ; restitution au profit des grossistes de produits homologués. Art. 57 (p. 3155) : liquidation sur le prix des commerçants en cas de lien de dépendance. Texte lu dans PDFs/Lois_de_Finances/Loi_de_Finances_2016.pdf, pieds de page lus."
  },
  {
    "id": "loi-2017-66-lf-2018-dc",
    "type": "legislation",
    "title": "Loi n° 2017-66 du 18 décembre 2017, portant loi de finances pour l'année 2018",
    "container-title": "Journal Officiel de la République Tunisienne",
    "issue": "101",
    "page": "4281-4284",
    "issued": {"date-parts": [[2017, 12, 18]]},
    "URL": "https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf",
    "note": "DOUBLON à fusionner avec lf-2018 et loi-2017-66-lf-2018. Art. 45, « Révision du droit de consommation », à partir de la p. 4281 (pied de page lu) : abroge et remplace en entier le tableau annexé à la loi 88-62 — deuxième refonte intégrale après celle de 2016. Art. 22 : ajoute un article 6 bis à la loi 88-62 (suspension pour les véhicules tout terrain), page non établie. Édition arabe : https://www.pist.tn/jort/2017/2017A/Ja1012017.pdf."
  },
  {
    "id": "dgi-nc-24-2007",
    "type": "report",
    "title": "Note commune n° 24/2007 — Commentaire des dispositions des articles 13, 14, 17 et 18 de la loi n° 2006-80 du 18 décembre 2006 relative à la réduction des taux de l'impôt et à l'allègement de la pression fiscale sur les entreprises, portant aménagement des taux de la taxe sur la valeur ajoutée",
    "author": [{"literal": "Tunisie. Ministère des finances, Direction générale des impôts"}],
    "issued": {"date-parts": [[2007]]},
    "note": "Bulletin officiel des douanes et des impôts, texte n° DGI 2007/35. DOCTRINE ADMINISTRATIVE, jamais source du droit : utilisée ici en seule corroboration du caractère sélectif du transfert de 2007 (cinq lignes au taux de 10 %). Copie locale : markdown_output/Notes_Communes/."
  },
  {
    "id": "dgi-nc-29-2007",
    "type": "report",
    "title": "Note commune n° 29/2007 — Détermination de l'assiette de calcul de la TVA, du droit de consommation perçu selon un taux ad-valorem, de la taxe au profit du Fonds de Développement de la Compétitivité dans le Secteur Industriel, et de la taxe au profit du Fonds National de la maîtrise de l'énergie",
    "author": [{"literal": "Tunisie. Ministère des finances, Direction générale des impôts"}],
    "issued": {"date-parts": [[2007]]},
    "note": "Bulletin officiel des douanes et des impôts, texte n° DGI 2007/64. DOCTRINE ADMINISTRATIVE. Pièce décisive pour l'articulation TVA / droit de consommation : énonce que l'assiette de la TVA comprend le droit de consommation, et donne un exemple chiffré (500 D HT, DC 10 %, FODEC 1 % : assiette TVA = 555 D). Précise aussi que les taxes FODEC et FNME sont liquidées hors droit de consommation, et réciproquement. Copie locale : markdown_output/Notes_Communes/."
  },
  {
    "id": "dgi-nc-7-2016",
    "type": "report",
    "title": "Note commune n° 7/2016 — Commentaire des dispositions des articles 44, 45 et 57 de la loi n° 2015-53 du 25 décembre 2015 portant loi de finances pour l'année 2016",
    "author": [{"literal": "Tunisie. Ministère des finances, Direction générale des impôts"}],
    "issued": {"date-parts": [[2016]]},
    "note": "DOCTRINE ADMINISTRATIVE. Utile pour la ventilation de la refonte de 2016 en trois mouvements (suppressions, réductions, augmentations) et pour ses annexes 1 à 3, qui listent les produits concernés. Copie locale : markdown_output/Notes_Communes/."
  },
  {
    "id": "dgi-nc-17-2018",
    "type": "report",
    "title": "Note commune n° 17/2018 — Commentaire des dispositions de l'article 45 de la loi n° 2017-66 du 18 décembre 2017 portant loi de finances pour l'année 2018 relatives à la révision du droit de consommation",
    "author": [{"literal": "Tunisie. Ministère des finances, Direction générale des impôts"}],
    "issued": {"date-parts": [[2018]]},
    "note": "DOCTRINE ADMINISTRATIVE. Donne l'état du droit au 31 décembre 2017 (taux ad valorem et spécifiques par famille de produits) et quatre annexes, dont deux barèmes de véhicules distinguant concessionnaires agréés et autres importateurs. Copie locale : markdown_output/Notes_Communes/."
  }
]
```

---

## Annexe B — Notions à porter au glossaire (`precis/glossaire.yml`)

**Déjà présente** : `droit-de-consommation` (statut `provisoire`). **Deux corrections à lui apporter :**
1. son terme arabe est `معلوم الاستهلاك` ; les objets arabes du JORT écrivent **`المعلوم على الاستهلاك`**
   (par exemple l'objet de l'article 44 de la LF 2016 : « مراجعة المعلوم على الاستهلاك »). Retenir la
   forme du JORT ;
2. sa définition dit « en sus de la taxe sur la valeur ajoutée » — exact, mais incomplet : préciser
   qu'il **entre dans l'assiette de la TVA** (§ 6) et qu'il frappe des **produits désignés par position
   tarifaire**, importés ou fabriqués localement. Sa référence `source_definition` pourra devenir
   `loi-88-62-droit-consommation`, avec `locator: "art. 1er"`.

| Terme FR | AR (à valider par un arabophone) | Source canonique pressentie |
|---|---|---|
| Droit de consommation *(entrée existante, à corriger)* | المعلوم على الاستهلاك | loi n° 88-62, art. 1er |
| Tableau annexé à la loi n° 88-62 | الجدول الملحق بالقانون عدد 62 لسنة 1988 | loi 88-62, annexe ; refondu par l'art. 44 de la LF 2016 puis l'art. 45 de la LF 2018 |
| Position tarifaire (numéro du tarif douanier, « NT ») | البند التعريفي | tableau annexé, colonne « NT » ; convention « Ex » pour les positions extraites |
| Taux ad valorem | نسبة من القيمة | loi 88-62, art. 4-a |
| Taux spécifique | معلوم قار / نسبة قارة | loi 88-62, art. 4-b (assiette par le volume ou le poids) |
| Fait générateur du droit de consommation | الحدث المنشئ للمعلوم على الاستهلاك | loi 88-62, art. 3 (dédouanement ; livraison) |
| Assiette du droit de consommation | قاعدة المعلوم على الاستهلاك | loi 88-62, art. 4 |
| Imputation du droit de consommation | طرح المعلوم على الاستهلاك | loi 88-62, art. 5 |
| Facturation à l'identique | الفوترة بنفس المبلغ | art. 34 de la loi 89-115 (LF 1990), ajouté à l'art. 5 |
| Entrepositaire | صاحب مستودع | loi 88-62, art. 2-4 |
| Suspension du droit de consommation | توقيف العمل بالمعلوم على الاستهلاك | art. 6 bis de la loi 88-62 (ajouté par l'art. 22 de la LF 2018) ; formule attestée telle quelle dans les objets arabes du JORT |
| Valeur en douane | القيمة الديوانية | loi 88-62, art. 4-a |
| Taxe unique de compensation sur les carburants *(régime antérieur, résiduel)* | — *(non attesté)* | renvoi (2) du tableau annexé de 1988 |
| Taxe sur les bières, vins et boissons alcoolisées *(régime antérieur)* | — *(non attesté)* | art. 4 à 11 de la loi n° 84-2 du 21 mars 1984, abrogés par l'art. 7 de la loi 88-62 |

*Les trois dernières entrées désignent des dispositifs **abrogés ou résiduels** : si le glossaire ne
prévoit pas de statut historique, le signaler dans la définition, comme il a été fait pour le
« tableau B bis » et le « taux majoré » côté TVA.*
