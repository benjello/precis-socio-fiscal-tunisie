# Compléments documentaires : « Les produits de base » (PR #811)

Documentaliste, 17 novembre 2026. Complète `docs/notes/compensation-produits-base-documentaliste.md`
sans la refaire. Aucun fichier du précis n'est modifié et `docs/recherches.yml` n'est pas touché : les passes sont **proposées** au § 8.

**Mode de lecture**, comme dans la note principale :
- **[IMG]** : lu sur l'image du fascicule local (rendu 90 à 200 dpi) ;
- **[TXT]** : couche texte de l'éditeur. Pour 1999-2005, cette couche est codée par un décalage de police (+29) ; elle a été décodée de façon déterministe ([TXT déc.]) ;
- **[OCR+arith]** : océrisation tesseract. Les chiffres sont contrôlés par l'arithmétique du décret lui-même (prix normal = prix de base + marge + péréquation ; indemnité = prix normal − prix réduit) quand l'image n'a pas été relue ;
- **[OCR-corpus]** : `markdown_output/` (1970-1972), contrôlé de la même façon ;
- **[méta]** : intitulé `jort_cache` seul.

Dates d'effet : selon AGENTS.md, § Dater. Une date énoncée par le texte est reprise telle quelle,
même rétroactive. À défaut, on calcule la date (« un jour franc » avant 1993 ; lendemain de la
publication après le 14 avril 2020). Si le calcul est incertain, on donne la date de publication.

---

## 0. Résumé point par point

| Point | État | Essentiel |
|---|---|---|
| 1. Prix au consommateur après 1991 | **non établi (prix) ; établi (instrument et autorité pour le blé)** | Aucun arrêté de prix au consommateur publié de 1992 à 2026 (texte intégral FR 1994-2026, miroir iort AR, intitulés). Depuis le décret n° 92-1657, les **prix réduits de rétrocession** du blé aux minoteries sont fixés « par décision du ministre » de l'économie nationale, puis du commerce ; ces décisions ne sont pas publiées. Découvertes : arrêtés « pain » du 22 juin 2016 et du 13 novembre 2020 (boulangeries agréées, quotas de farine PS, pain de 400 g et baguette de 220 g), absents des intitulés de `jort_cache` ; arrêté conjoint du 2 avril 2026 sur les taux d'extraction |
| 2. Pain 1975-1991 | **établi, sauf 1980** | 31 mai 1975 : 65 millimes (décret n° 75-352, lu). 10 juillet 1984 : 90 millimes. 15 juillet 1985 : 100 millimes. 30 août 1986 : pain de 600 g. 12 août 1989 : 500 g à 100 millimes. 17 août 1991 : 500 g à 120 millimes. Texte de 1980 non identifié |
| 3. Décrets de campagne 1970-2009 | **établi** | Tableau complet au § 3 (prix de base, prix normaux, prix réduits aux minoteries, qui paie). **Toutes les lacunes sont comblées** par des clauses de reconduction (fiche `r-comp-pb-decrets-campagne-lacunes` : résolue) |
| 4. Textes anciens | **établi** | 67-408, 68-279, 71-277, 74-876, tableau B du décret n° 82-134 et farines de février 1984 lus à l'image. **Correction** : le décret n° 68-279 crée une redevance ; l'indemnité de 115 millimes date du décret n° 71-277 (1971). Décret n° 74-780 en arabe : non fait |
| 5. Lait, papier, fin de subvention, pain 1991 | **en partie** | Prix du lait de 1989 lu ; opérateur non établi. Papier : la loi de finances pour 2026, art. 64, est une exonération fiscale, pas une subvention. Fin de subvention 1992-1999 : non traité. Pain 1991 : effet énoncé au 17 août 1991, publication le 3 septembre 1991 |
| 6. Ciblage 2013-2026 | **rien de juridique** (passe élargie) | Texte intégral FR 2013-2026 et miroir iort AR : aucun texte de ciblage des subventions alimentaires |
| 7. Troisième grande réforme | **oui, mais sur deux points seulement** | **1990-1993 : le prix réduit du blé sort du décret pour une décision ministérielle non publiée (décrets n° 91-943, 92-1657, 93-1721), et l'orge est libérée (décret n° 93-1721).** La Caisse générale apparaît comme payeur dans les décrets à partir de 1989. D'après la BCT (1974, 1975, 1984), elle finançait déjà les céréales : ce point formalise un flux existant et n'est pas une rupture. Voir § 7 |

---

## 1. Prix au consommateur et autorité après 1991 (fiche `r-comp-pb-prix-consommateur-apres-1991`)

### 1.1 Ce qui a été parcouru (passe du 17 novembre 2026)

- **Texte intégral FR, 1992-2026.** Extraction `pdftotext` des 3 857 fascicules FR locaux. Les fascicules 1999-2005 ont été décodés (police décalée de 29). Recherches : `prix … (du pain | de la farine | des farines | de la semoule | du sucre | du lait | huile végétale | pâtes alimentaires)`, `(fixation|fixant) … prix`, `vente du pain`, `farine PS`.
  - Lacunes de couverture : 1992 et 1993 n'ont **aucune couche texte** (88 et 100 fichiers) ; 1995 (1), 1996 (6), 2018 (1), 2022 (2), 2023 (4), 2024 (8) et 2025 (4) ont des fichiers vides ; des pages isolées sont en image dans des fascicules par ailleurs textuels (par exemple n° 87/1995, p. 2045-2048 ; n° 49/2007, p. 2077-2093).
- **Miroir iort (AR)**, 32 130 fiches : `الخبز`, `(سعر|أسعار)…(الخبز|الفارينة|السميد|العجين|الكسكسي|السكر|الزيت النباتي|الحليب)`, `المصادقة على الأسعار`. Seuls résultats : les intitulés des décrets n° 75-352 et 84-153. Pour la période ancienne, les fiches iort se réduisent à l'intitulé, sans texte.
- **`jort_cache` (intitulés)** : `pain`, `farine`, `semoule`, `lait régénéré`, `huile végétale`, `boulang`, `subventionn`, `المدعم`, `المخابز`, depuis le 1er septembre 1991.
- **Résultat** : **aucun arrêté ni décret fixant un prix de vente au public du pain, de la farine, de la semoule, des pâtes, du couscous, du sucre, de l'huile ou du lait n'est publié de 1992 à 2026** dans ce qui a été parcouru. Les derniers sont ceux de 1991 (§ 2).

### 1.2 Défaut de `jort_cache` constaté

Les arrêtés du 22 juin 2016 (JORT n° 53/2016, p. 2090-2091) et du 13 novembre 2020 (JORT n° 113/2020, p. 2603-2606) **ne figurent pas dans les intitulés de `jort_cache`**. Les passes antérieures, faites sur les seuls intitulés, ne prouvent donc rien pour 2016-2020. Ligne à verser au playbook de `tunisia-data` et à `outillage-sources.md` : « `jort_cache` omet des arrêtés du ministère du commerce (2016, 2020) ; doubler toute recherche d'intitulé par le texte intégral des fascicules ».

### 1.3 Textes trouvés : le circuit du pain, non son prix

- **Arrêté du ministre du commerce du 22 juin 2016, relatif à la production, l'exposition et la vente du pain**, JORT n° 53 du 29 juin 2016, p. 2090-2091 [TXT]. URL : https://www.pist.tn/jort/2016/2016F/Jo0532016.pdf
  - Visas : décret du 19 janvier 1956 sur la boulangerie ; loi n° 2015-36, « notamment son article 42 » ; décret n° 91-1996.
  - Art. 1er : « Les boulangeries agréées et bénéficiant de la carte professionnelle sont classées en boulangerie catégorie A et boulangerie catégorie C. L'utilisation de la farine boulangère PS est exclusivement réservée aux boulangeries catégorie A et C ».
  - Art. 2 : « Gros pain : 400 ± 30 g longueur 45 cm ± 3 cm ou diamètre: 23 cm ± 2 cm, Baguette : 220 g ± 10 g longueur = 55 cm ± 5 cm. »
  - Art. 3 : « Le bénéfice de la subvention et des quotas de farine PS » est subordonné à la justification du paiement des salaires et des cotisations à la CNSS.
  - Art. 6 : affichage obligatoire du prix, sans montant fixé.
  - Effet : le texte ne dit rien, et la règle de 1993-2020 suppose la date de dépôt au gouvernorat ; on écrit donc « publié le 29 juin 2016 ».
- **Arrêté du ministre du commerce et du développement des exportations du 13 novembre 2020, relatif à la production, l'exposition et la vente du pain**, JORT n° 113 du 13 novembre 2020, p. 2603-2606 [TXT]. URL : https://www.pist.tn/jort/2020/2020F/Jo1132020.pdf
  - Art. 1er : l'arrêté régit aussi « la détention, l'utilisation et la commercialisation de la farine subventionnée ».
  - Art. 2 : « Farine PS : farine panifiable (destinée à la production du pain subventionné) » ; « Farine PS-7 : farine pâtissière ».
  - Art. 4 : catégorie A, « gros pains subventionné », 400 g ± 30 g ; catégorie C, « baguette », 220 g ± 10 g.
  - Art. 5 : « quota mensuel de farine PS » ; tout dépassement entraîne la « suspension du quota ».
  - Art. 13 : « Les boulangeries agréées doivent respecter les prix et les marges bénéficiaires fixés » ; le gros pain est réservé à la consommation familiale et ne peut être vendu aux hôtels, aux restaurants ni aux acheteurs publics.
  - Art. 16 : abroge l'arrêté du 22 juin 2016.
  - Effet calculé : lendemain de la publication, soit le **14 novembre 2020**.
  - Le texte ne fixe aucun prix : il renvoie à des prix « fixés » sans dire par quel acte.
- **Arrêté conjoint des ministres de l'agriculture et du commerce du 2 avril 2026, fixant les taux d'extraction des farines et de la semoule**, JORT n° 35 du 3 avril 2026, p. 645-647 [TXT]. URL : https://www.pist.tn/jort/2026/2026F/Jo0352026.pdf
  - Art. 2 : semoule extraite à 70 % ; « farine panifiable » extraite à 85 % (cendres de 0,85 à 1,05 %) ; farine « pain fin et confiseries » extraite à 71 %.
  - Art. 5 : abroge l'arrêté du 21 août 1979 sur les taux d'extraction.
  - Effet calculé : **4 avril 2026**.
- **Poids du pain, avant → après** (série datée, à reprendre dans la section « pain ») : 700 g / 300 g (1975-1986) → 600 g / 250 g (30 août 1986) → 500 g / 250 g (12 août 1989) → gros pain 500 g / baguette 250 g (17 août 1991) → gros pain 400 g / baguette 220 g (arrêté du 22 juin 2016, repris le 13 novembre 2020).

### 1.4 L'autorité établie : le ministre, par « décision » non publiée, pour le blé

Les décrets de campagne fixent dans leur propre texte le prix réduit de rétrocession du blé aux minoteries de 1974 à 1989. Ensuite :
- **Décret n° 91-943** (récolte 1990), art. 8 [IMG] : le blé destiné aux semoules et farines est rétrocédé « à des prix réduits fixés par arrêté du ministre de l'économie nationale » ; aucun arrêté de ce type n'apparaît dans les intitulés ;
- **décret n° 92-1657** (récolte 1991), art. 8 [IMG] : « à des prix réduits fixés par décision du ministre de l'économie nationale » ;
- **décret n° 96-2549**, art. 7 et 12 [TXT], puis tous les décrets jusqu'en 2025 (2025-344, art. 15 : « décision du ministre chargé du commerce ») : la « prime de compensation prise en charge par la caisse générale de compensation » est la différence entre les prix normaux et « les prix réduits de rétrocession tels que fixés par décision du ministre du commerce ».

**Conclusion pour la fiche** : depuis 1992, l'acte qui fixe le prix réduit du blé est une **décision ministérielle**. Les décrets n'en publient pas le montant et le JORT ne la publie pas. Pour le prix au consommateur des dérivés, aucun acte n'est identifié. L'hypothèse d'une décision du même type n'est **pas établie** et ne doit pas s'écrire.
<!-- à conserver comme réserve : RECHERCHE r-comp-pb-prix-consommateur-apres-1991 -->

---

## 2. Prix du pain 1975-1991, décret n° 75-352 et arrêtés du 3 juin 1975

### 2.1 Décret n° 75-352 du 3 juin 1975, fixant le prix des farines et semoules, du pain, des pâtes alimentaires et du couscous rapide [IMG]

JORT n° 38 des 3-6 juin 1975, p. 1192 ; URL : https://www.pist.tn/jort/1975/1975F/Jo03875.pdf

- Art. 1er : « A compter du 31 mai 1975 », les prix sont les suivants.
  - Farines : farine de blé tendre extraite à PS-2, 7,350 D/q ; extraite à PS + 10, 6,795 D/q.
  - Semoules : semoule de blé dur extraite à PS, 8,100 D/q ; semoule « couscous » et « G », 8,800 D/q.
  - Pain : 700 g, toutes catégories, **65 millimes** ; 300 g, 38 millimes.
  - Pâtes alimentaires : 0,105 D le kg en gros, 0,113 D au détail. Couscous rapide : 0,112 D et 0,120 D.
- Art. 3 : une rubrique « Péréquation du transport de la farine » est créée au compte « Soutien du Marché » à compter du 31 mai 1975, alimentée par 0,250 D par quintal de farine livrée.
- Art. 4 : prix de rétrocession réduits du blé aux minoteries « à compter du 31 mai 1975 » : blé dur 5,970 D/q, blé tendre 4,930 D/q (modifie l'art. 13 du décret n° 74-649).
- Art. 5 : les indemnités du décret n° 74-966 (farines des boulangers) sont supprimées à compter du 31 mai 1975.
- Art. 6 : l'indemnité de 115 millimes du décret n° 68-279 est « ramenée à cent millimes » ; celle de 185 millimes du décret n° 74-780 est supprimée.
- Art. 7 : abroge les décrets n° 74-780 et 74-966 et les arrêtés des 14 juin 1967 (prix du pain) et 10 août 1967 (farines et semoules).
- **Remarque** : en 1983, les décrets n° 83-1275 et 83-1276 abrogent les décrets n° 74-966 et 74-780, déjà abrogés en 1975 ; en 1984, les décrets n° 84-151 et 84-152 les « remettent en vigueur ». Les textes de 1983-1984 ne tiennent pas compte de l'abrogation de 1975. **Le rédacteur ne doit pas présenter 74-780 et 74-966 comme en vigueur de 1975 à 1983.**
- Rectificatif ou republication au JORT n° 57/1975, p. 1814 [méta] : non lu.
- Les prix du pain (55 → 65 millimes) et des farines concordent avec ceux de la BCT pour 1975 ; « 55 » est le prix d'avant, selon la BCT seule.

### 2.2 Arrêtés du ministre de l'économie nationale du 3 juin 1975 [IMG]

Même fascicule, avec effet énoncé au **31 mai 1975**.
- **Huile mélangée** (p. 1189-1190) : 200 m/kg en cession aux grossistes, rendu chef-lieu de délégation ; 204 m/kg aux détaillants ; **200 m/litre au public**. Les stocks paient une redevance à la Caisse générale de compensation : 19 m/kg pour les grossistes, 20 m/litre pour les détaillants.
- **Sucre** (p. 1191) : poudre, 186 / 190 / **200 M** ; morceaux, 286 / 290 / **300 M**. Redevances différentielles : 25 et 30 M/kg pour la poudre, 55 et 60 M/kg pour les morceaux. L'arrêté abroge celui du 24 mai 1974.

### 2.3 Prix du pain 1984-1991 [IMG sauf mention]

| Effet | Texte (JORT) | Contenu |
|---|---|---|
| 10 juillet 1984 (énoncé) | arrêté du ministre de l'économie nationale du 10 juillet 1984, portant fixation des prix de vente du pain (n° 43 des 17-20 juillet 1984, p. 1594-1595) | 700 g : **90 millimes** ; 300 g : 60 millimes (pain de farine PS) |
| 15 juillet 1985 (énoncé) | arrêté du 15 juillet 1985, portant fixation des prix de vente du pain (n° 55 des 19-23 juillet 1985, p. 946) | 700 g : **100 millimes** ; 300 g : 70 millimes. Ses visas ne citent que les arrêtés du 17 février et du 10 juillet 1984 : rien entre les deux |
| 30 août 1986 (énoncé) | arrêté du ministre de l'industrie et du commerce du 29 août 1986, portant fixation du poids du pain (n° 50 du 16 septembre 1986, p. 1020) | « Gros pain : 600 grammes » ; « Petit pain : 250 grammes » ; tolérances de 35 g et 10 g. Le prix ne change pas : 100 et 70 millimes depuis l'arrêté de 1985, que visent les arrêtés de 1986 et de 1989 |
| 12 août 1989 (énoncé ; rétroactif, publié le 17 novembre 1989) | arrêté du ministre de l'économie nationale du 11 novembre 1989, portant fixation du poids et du prix de vente du pain (n° 77 des 17-21 novembre 1989, p. 1823) | 500 g : **100 millimes** ; 250 g : 80 millimes |
| 17 août 1991 (énoncé ; publié le 3 septembre 1991) | arrêté du 15 août 1991, portant fixation des prix du pain (n° 61 des 3-6 septembre 1991, p. 1545) | gros pain de 500 g : **120 millimes** ; baguette de 250 g : 100 millimes |

- URL : 1984 : https://www.pist.tn/jort/1984/1984F/Jo04384.pdf ; 1985 : https://www.pist.tn/jort/1985/1985F/Jo05585.pdf ; 1986 : https://www.pist.tn/jort/1986/1986F/Jo05086.pdf ; 1989 : https://www.pist.tn/jort/1989/1989F/Jo07789.pdf ; 1991 : https://www.pist.tn/jort/1991/1991F/Jo06191.pdf
- Le même jour paraissent d'autres arrêtés.
  - 10 juillet 1984 : semoules (p. 1595) ; pâtes et couscous rapide (p. 1595-1596) [méta].
  - 29 août 1986 : pâtes et couscous, effet au 30 août 1986 [IMG] ; pâtes PS/10 vrac, 215 / 220 / **240** millimes le kg ; couscous P.S.-10 vrac, 223 / 228 / **250**.
  - 11 novembre 1989, effet au 12 août 1989 [IMG] : huile de mélange vrac, 338 / 348 / **340 mil/litre** au détail ; semoule PS-10, 15,440 / 15,800 / **17,500 D/q** ; lait (§ 5) ; farine PS-7 (p. 1821-1822), sucre (p. 1822) et pâtes (p. 1822-1823) [méta].
  - 15 août 1991 [IMG] : pâtes PS-10 vrac, 268 / 275 / **300 mil** ; couscous PS-10 vrac, 307 / 314 / **340 mil**.
- **« 1986, 1988, 1990 »** : dans la note principale, cette mention groupait des arrêtés autres que ceux du pain : pâtes en 1986 ; sucre le 22 novembre 1986, le 8 septembre 1988 et le 18 juillet 1990 ; huile le 29 décembre 1986. **Il n'y a pas d'arrêté de prix du pain en 1986 (seul le poids change), en 1988 ni en 1990.**

### 2.4 Pain de 1980 (fiche `r-comp-pb-prix-pain-1980`)

Non établi.
- Décret n° 80-140 (11 février 1980) : il reconduit pour 1979-1980 le décret n° 79-289 « tel qu'[il a] été modifié par les articles 4 et 5 » du décret n° 79-413 ; il ne fixe pas de prix du pain.
- Décret n° 80-1257 (JORT n° 57 du 7 octobre 1980) : il relève le prix réduit du blé aux minoteries de 6,393 à **8,000 D/q** (blé dur) et de 5,712 à 7,250 (blé tendre). Ce relèvement est cohérent avec le pain à 80 millimes de la BCT, mais ne le prouve pas.
- Intitulés de 1980-1981 (`jort_cache`) : aucun texte « pain », « farine », « semoule » ou « dérivés ». On relève en revanche un arrêté sur le sucre et le café du 20 février 1980 (n° 12/1980, p. 558-559) et un sur l'huile mélangée du 21 janvier 1980 (n° 21/1980, p. 1021-1022) [méta].
- Prochaine étape : sommaires des n° 55 à 60 de 1980 (OCR) ; le décret n° 80-1257 n'a pas de couche texte.

---
## 3. Décrets de campagne des céréales 1970-2009 : tableau pour la série et les paramètres

### 3.1 Lacunes comblées (fiche `r-comp-pb-decrets-campagne-lacunes` : **résolue**)

| Campagnes absentes des intitulés | Régime appliqué | Texte qui le dit |
|---|---|---|
| 1993-1994, 1994-1995 | décret n° 93-1721 | décret n° 96-2549, art. 14 : « Sont applicables aux campagnes 1993-1994 et 1994-1995, les dispositions du décret n° 93-1721 du 16 octobre 1993 susvisé » (le visa dit « 16 août 1993 » ; le titre du corps imprime « Décret n° 97-2549 »). JORT n° 4 du 14 janvier 1997, p. 59 [TXT] |
| 1997/98, 1998/99, 1999/2000 | décret n° 96-2549 | décret n° 2001-864, art. 14, JORT n° 33 du 24 avril 2001, p. 924 [TXT déc.] |
| 2001-2002 à 2004-2005 | décret n° 2001-864 | décret n° 2005-1983, art. 4 : « Sont appliquées pour les campagnes 2001-2002, 2002-2003 et 2003-2004 et 2004-2005, les dispositions du décret n° 2001-864 ». JORT n° 57 du 19 juillet 2005, p. 1798 [TXT déc.] |
| 2006/2007 | décret n° 2005-1983 | décret n° 2007-1402, art. 15 : « Sont applicables à la campagne 2006/2007, les dispositions du décret n° 2005-1983 ». JORT n° 49 du 19 juin 2007, p. 2091 [OCR, visa relu] |

La récolte 1979 est couverte par le décret n° 80-140, art. 1er, qui reconduit le décret n° 79-289 tel que modifié par les art. 4 et 5 du décret n° 79-413 [OCR]. **Toutes les récoltes de 1970 à 2009 ont donc un texte.**

### 3.2 Tableau (D/q ; « réduit » = prix de rétrocession du blé destiné à la fabrication industrielle des semoules et farines)

Effet : chaque décret vaut pour « la récolte de l'année X ». Il paraît souvent après la récolte, parfois l'année suivante. **Ne pas inventer une date d'effet au 1er juin** : prendre la récolte comme période et donner la publication (question ouverte au modéliste).

| Récolte | Décret (date) | JORT n°, date, pages | Base BD / BT / orge | Normal BD / BT / orge | Réduit BD / BT | Qui paie l'écart | Lecture |
|---|---|---|---|---|---|---|---|
| 1970 | 70-261 (30.7.1970), mod. 70-606 | 37 du 31.7 au 4.8.1970, p. 985-992 (prix : p. 990) | 4,800 / 4,300 / 2,800 | 5,271 / 4,726 / 3,196 | — (pas de prix réduit pour le blé ; orge pour le bétail 2,300) | indemnité orge 0,978, compte « Soutien du Marché des Céréales » (art. 31-32) | IMG (p. 990) |
| 1971 | 71-253 (8.7.1971) | 30 du 9.7.1971, p. 909-915 | idem | idem | — | idem | OCR-corpus+arith |
| 1972 | 72-244 (7.8.1972) | 32/1972, p. 1097-1103 (`jort_cache` : publié le 4.8.1972, avant la signature : à vérifier) | idem | idem | — | idem | OCR-corpus |
| 1973 | 73-346 (14.7.1973) | 28 des 20-27.7.1973, p. 1139-1145 | 4,800 / 4,300 / 2,800 (orge : + prime de difficulté exceptionnelle de 0,200, art. 10) | 5,271 / 4,726 / 3,196 | — | idem | IMG (p. 1143) |
| 1974 | 74-649 (22.6.1974) | 44 des 25-27.6.1974, p. 1439-1445 | 6,100 / 5,500 / 4,000 | 6,790 / 6,130 / 4,595 | **5,271 / 4,726** (art. 13) | indemnité compensatrice 1,519 / 1,404 (art. 22), compte de l'Office « Soutien du Marché des Céréales » (art. 25) | IMG (p. 1443-1444) ; indemnités OCR+arith |
| (31.5.1975) | 75-352, art. 4 | 38 des 3-6.6.1975, p. 1192 | — | — | 5,970 / 4,930 | — | IMG |
| 1975 | 75-542 (4.8.1975) | 54 du 8.8.1975, p. 1674-1680 | 6,600 / 6,000 / 4,500 | 7,290 / 6,630 / 5,095 | 5,970 / 4,930 | 1,320 / 1,700 ; Office | IMG (p. 1678) ; indemnités OCR+arith |
| 1976 | 76-812 (13.9.1976), mod. 77-339 (1.4.1977, n° 24/1977, p. 898-899) | 56 du 17.9.1976, p. 2220-2225 | 6,600 / 6,000 / 4,500 | 7,460 / 6,750 / 5,214 | 5,970 / 4,930 du 1.6 au 31.10.1976, puis 5,670 / 4,880 dès le 1.11.1976 | 1,490 / 1,820, puis 1,790 / 1,870 ; Office | IMG (p. 2224) ; 77-339 et indemnités OCR+arith |
| 1977 | 77-981 (22.11.1977) | 81 des 9-13.12.1977, p. 3384-3390 | 7,135 / 6,535 / 5,035 | 8,135 / 7,415 / 5,855 | 5,670 / 4,880 | Office | IMG |
| 1978 | 79-289 (2.4.1979) | 25 du 6.4.1979, p. 984-990 | 7,600 / 7,000 / 5,500 | 8,630 / 7,910 / 6,350 | 5,670 / 4,880 ; dès le 3.5.1979, **6,393 / 5,712** (79-413, art. 4 ; indemnités 2,237 / 2,198, art. 5) | Office | IMG |
| 1979 | 80-140 (11.2.1980), reconduction | 10 du 19.2.1980, p. 455-456 | (79-289) | (79-289) | 6,393 / 5,712 | Office | OCR |
| 1980 | 80-1257 (30.9.1980) | 57 du 7.10.1980, p. 2534-2540 | 8,600 / 7,700 / 5,900 | 9,735 / 8,762 / 6,908 | **8,000 / 7,250** | Office | IMG |
| 1981 | 81-1069 (15.8.1981) ; mod. 82-173 (29.1.1982, n° 7/1982, p. 266 : prix de consommation en grains et semences) | 53 des 18-21.8.1981, p. 1935-1941 | 9,600 / 8,700 / 6,900 | 10,840 / 9,867 / 8,013 | 8,000 / 7,250 | Office | IMG |
| 1982 | 82-1286 (18.9.1982) | 61 des 24-28.9.1982, p. 1998-2004 | 11,000 / 10,000 / 8,000 | 12,616 / 11,585 / 9,524 | 8,000 / 7,250 | Office | IMG |
| 1983 | 83-1075 (17.11.1983) | 75 du 22.11.1983, p. 2977-2984 | 12,800 / 11,700 / 9,500 | 14,670 / 13,536 / 11,269 | 8,000 / 7,250 ; **15,600 / 13,000 dès le 28.12.1983** (83-1274) ; retour par 84-150 ; **8,800 / 7,250** par 84-785 du 10.7.1984, sans clause d'effet, publié au JORT n° 43 des 17-20.7.1984, p. 1594 (indemnités 5,870 / 6,286) | Office (84-785 : « compte soutien du marché ») | IMG |
| 1984 | 84-1520 (25.12.1984) | 1 des 1er-4.1.1985, p. 11-17 | 14,000 / 14,000 / 10,000 | 15,996 / 15,996 / 11,874 | 8,800 / 7,250 | 7,196 / 8,746 ; Office | IMG |
| 1985 | 85-1242 (7.10.1985) | 72 du 15.10.1985, p. 1387-1393 | 15,000 / 14,500 / 10,500 | 17,118 / 16,606 / 12,486 | 8,800 / 7,250 | Office | IMG |
| 1986 | 87-129 (11.2.1987) | 13 du 20.2.1987, p. 252-258 | 16,000 / 16,000 / 11,000 | 18,193 / 18,193 / 13,043 | 8,800 / 7,250 | Office | IMG |
| 1987 | 88-707 (25.3.1988) | 23 du 8.4.1988, p. 533-538 | 18,500 / 17,000 / 12,000 | 21,219 / 19,673 / 14,521 | 8,800 / 7,250 | Office | IMG |
| 1988 | 89-1171 (14.8.1989) | 59 du 1.9.1989, p. 1323-1329 | 21,000 / 19,000 / 14,000 | 23,908 / 21,837 / 16,659 | 8,800 / 7,250 | **Office, « dont le solde sera pris en charge par la caisse générale de compensation »** (art. 27) | IMG (p. 1327-1328 ; indemnités 15,108 / 14,587 confirment le prix réduit) |
| 1989 | 90-671 (25.4.1990) | 31 des 8-11.5.1990, p. 573-579 | 21,000 / 19,000 / 14,000 | 23,908 / 21,837 / 16,659 | 8,800 / 7,250 | idem (art. 26 ; semences à la charge du titre II du budget) | IMG |
| 1990 | 91-943 (17.6.1991) | 47 du 2.7.1991, p. 1236-1242 | 24,500 / 20,900 / 15,000 (IMG, p. 1236) | 28,256 / 24,440 / 18,192 | « par arrêté du ministre de l'économie nationale » (art. 8) | « prime de compensation » (art. 14) ; « Le solde sera pris en charge par la caisse générale de compensation » (art. 16) | IMG |
| 1991 | 92-1657 (14.9.1992) | 66 du 2.10.1992, p. 1310-1312 | 24,500 / 20,900 / 15,000 (IMG, p. 1310) | 28,496 / 24,650 / 18,342 | « par décision du ministre de l'économie nationale » (art. 8) | idem (art. 14, 16) | IMG |
| 1992 (et 1993, 1994) | 93-1721 (16.8.1993) | 65 du 31.8.1993, p. 1393-1399 | 26,000 / 22,500 / **orge : commercialisation libre, prix d'intervention 15,000** | 30,218 / 26,472 / 18,450 | décision du ministre de l'économie nationale (art. 7) | **« prime de compensation pris en charge par la Caisse Générale de Compensation »** (art. 13) | IMG |
| 1995 | 95-2021 (16.10.1995) | 87 du 31.10.1995, p. 2043-2048 | 27,500 / 24,000 / orge, intervention 15,000 (+ 5,000 de prompte livraison du 1.6 au 31.7.1995) | 31,876 / 28,178 / 23,950 | décision du ministre du commerce | CGC (art. 13) | TXT |
| 1996 (et 1997 à 1999) | 96-2549 (30.12.1996) | 4 du 14.1.1997, p. 57-62 | 28,500 / 25,000 / orge, intervention 17,000 | 33,031 / 29,333 / 20,877 | décision du ministre du commerce (art. 7) | CGC (art. 12) | TXT |
| 2000 (et 2001 à 2004) | 2001-864 (18.4.2001) | 33 du 24.4.2001, p. 922-928 | 29,500 / 26,000 / 17,000 (orge, intervention 17,000 + 8,000 de prompte livraison) | 34,165 / 30,497 / 21,077 | décision du ministre du commerce (art. 7) | CGC | TXT déc. ; art. 1 IMG |
| 2005 (et 2006) | 2005-1983 (11.7.2005) | 57 du 19.7.2005, p. 1797-1798 | 30,500 / 27,000 / orge, intervention 18,000 | 35,165 / 31,497 / 22,077 (art. 2) | par renvoi au décret n° 2001-864 (art. 3) | CGC | TXT déc. |
| 2007 | 2007-1402 (18.6.2007) | 49 du 19.6.2007, p. 2087-2093 | 32,782 / 28,732 / orge, intervention 20,000 | 38,230 / 34,012 / 24,908 | décision du ministre du commerce (art. 8) | CGC | IMG |
| 2008 | 2008-2081 (2.6.2008) | 47 du 10.6.2008, p. 1814-1819 | 40,000 / 35,000 / orge, intervention 30,000 ; **prime exceptionnelle de prompte livraison : blé dur 15, blé tendre 10, **triticale** 10** (art. 2 ; l'orge n'y figure pas) | 61,675 / 51,242 / 46,020 (**prime comprise**, art. 8 c) | décision du ministre du commerce et de l'artisanat (art. 9) | CGC | TXT |
| 2009 | 2009-1853 (9.6.2009) | 47 du 12.6.2009, p. 1556-1559 | 43,000 / 35,000 / orge, intervention 30,000 ; prime : blé dur 15, blé tendre 10, orge et triticale 10, pour les livraisons avant le 31.8.2009 | 64,675 / 51,242 / 46,020 (prime comprise) | décision (art. 9) | CGC (art. 14) | TXT |

URL pist.tn (FR), dans l'ordre :
- 1970 : https://www.pist.tn/jort/1970/1970F/Jo03770.pdf
- 1971 : https://www.pist.tn/jort/1971/1971F/Jo03071.pdf
- 1972 : https://www.pist.tn/jort/1972/1972F/Jo03272.pdf
- 1973 : https://www.pist.tn/jort/1973/1973F/Jo02873.pdf
- 1974 : https://www.pist.tn/jort/1974/1974F/Jo04474.pdf
- 1975 : https://www.pist.tn/jort/1975/1975F/Jo05475.pdf
- 1976 : https://www.pist.tn/jort/1976/1976F/Jo05676.pdf (77-339 : https://www.pist.tn/jort/1977/1977F/Jo02477.pdf)
- 1977 : https://www.pist.tn/jort/1977/1977F/Jo08177.pdf
- 1978 : https://www.pist.tn/jort/1979/1979F/Jo02579.pdf
- 1979 : https://www.pist.tn/jort/1980/1980F/Jo01080.pdf
- 1980 : https://www.pist.tn/jort/1980/1980F/Jo05780.pdf
- 1981 : https://www.pist.tn/jort/1981/1981F/Jo05381.pdf
- 1982 : https://www.pist.tn/jort/1982/1982F/Jo06182.pdf
- 1983 : https://www.pist.tn/jort/1983/1983F/Jo07583.pdf (84-785 : https://www.pist.tn/jort/1984/1984F/Jo04384.pdf)
- 1984 : https://www.pist.tn/jort/1985/1985F/Jo00185.pdf
- 1985 : https://www.pist.tn/jort/1985/1985F/Jo07285.pdf
- 1986 : https://www.pist.tn/jort/1987/1987F/Jo01387.pdf
- 1987 : https://www.pist.tn/jort/1988/1988F/Jo02388.pdf
- 1988 : https://www.pist.tn/jort/1989/1989F/Jo05989.pdf
- 1989 : https://www.pist.tn/jort/1990/1990F/Jo03190.pdf
- 1990 : https://www.pist.tn/jort/1991/1991F/Jo04791.pdf
- 1991 : https://www.pist.tn/jort/1992/1992F/Jo06692.pdf
- 1992 : https://www.pist.tn/jort/1993/1993F/Jo06593.pdf
- 1995 : https://www.pist.tn/jort/1995/1995F/Jo08795.pdf
- 1996 : https://www.pist.tn/jort/1997/1997F/Jo00497.pdf
- 2000 : https://www.pist.tn/jort/2001/2001F/Jo0332001.pdf
- 2005 : https://www.pist.tn/jort/2005/2005F/Jo0572005.pdf
- 2007 : https://www.pist.tn/jort/2007/2007F/Jo0492007.pdf
- 2008 : https://www.pist.tn/jort/2008/2008F/Jo0472008.pdf
- 2009 : https://www.pist.tn/jort/2009/2009F/Jo0472009.pdf

Éditions arabes : même chemin, en remplaçant `F/Jo` par `A/Ja`.

### 3.3 Ruptures de la série, à porter en métadonnées (pour le modéliste)

1. **Orge** : de 1970 à 1991, c'est un prix de base. Depuis la récolte 1992 (décret n° 93-1721, art. 1er), c'est un **prix d'intervention**, la commercialisation étant libre. Il faut deux paramètres distincts ou une note de rupture.
2. **Prix normal de rétrocession** : sa composition change.
   - Jusqu'en 1991 : base + marge brute + péréquation de transport.
   - Depuis 1992 : base + prime forfaitaire (marge nette et péréquation) + 0,100 D au fonds d'équipement + somme des primes de magasinage.
   - En 2008 et 2009 : il comprend en plus la **prime exceptionnelle de prompte livraison** (art. 8 c). C'est ce qui explique le saut de 38,230 (2007) à 61,675 (2008) pour le blé dur.
3. **Prix réduit aux minoteries** :
   - absent pour le blé de 1970 à 1973 ;
   - fixé par le décret de 1974 à 1989 ;
   - fixé par arrêté pour la récolte 1990 (aucun arrêté de ce type n'est identifié) ;
   - fixé par **décision non publiée** depuis la récolte 1991.

   La série publiée des prix réduits s'arrête donc à 8,800 / 7,250 (récolte 1989).
4. **Qui paie** :
   - le compte de l'Office « Soutien du Marché des Céréales », de 1968 à 1987 ;
   - le même compte, avec un solde à la charge de la Caisse générale de compensation, pour les récoltes 1988 à 1991 ;
   - la Caisse générale directement (« prime de compensation »), depuis la récolte 1992.
5. **Titre trompeur** : le décret n° 81-1069 est intitulé « campagne 1980-1981 » au fascicule, mais son corps porte sur la « récolte 1981 » (art. 11, 14). Il s'applique à la récolte 1981 ; le décret n° 80-1257 couvre la récolte 1980.
6. **Instrument** : la campagne 2026-2027 est fixée par **arrêté conjoint** du 24 juillet 2026 (JORT n° 75/2026) et non plus par décret. Ce constat relève du registre des campagnes 2010-2026 ; il est à vérifier par qui tient ce registre.

### 3.4 Prix de vente des dérivés, série officielle (complément au § 2)

Farine PS-2 (puis PS), au détail, en D/q :
- 7,350 au 31 mai 1975 ;
- 8,650 au 3 mai 1979 (décret n° 79-413) ;
- 19,500 au 28 décembre 1983 ;
- 11,500 en février 1984 : 115 millimes le kg vrac [IMG ; le prix PS-7 vrac est de 160 millimes].

Semoule PS, au détail :
- 8,100 (31 mai 1975) ;
- 9,150 (3 mai 1979) ;
- 27,000 (28 décembre 1983) ;
- 14,500 (février 1984 : 145 millimes le kg) ;
- 17,500 pour la semoule PS-10 (12 août 1989).

Les autres années (1980-1983, 1984-1989) ne sont pas établies.

---

## 4. Textes anciens (point 4)

- **Décret n° 67-408 du 24 novembre 1967, fixant le taux des redevances compensatrices sur les stocks de farines et de semoules détenus le 14 juin 1967**, JORT n° 50 du 28 novembre au 1er décembre 1967, p. 1469 [IMG]. URL : https://www.pist.tn/jort/1967/1967F/Jo05067.pdf
  - Art. 1er : les détenteurs de plus de 100 kg de farines et semoules versent « à l'Office des Céréales une redevance compensatrice ». Taux : farine PS + 10, 0,951 D/q ; PS-2, 1,015 D/q ; semoule PS et semoule couscous et G, 0,900 D/q.
  - Art. 2 : versée au compte « Soutien du Marché des Céréales ».
  - Il s'agit d'une **ponction sur les stocks** lors de la hausse des prix de juin 1967, non d'une subvention.
- **Décret n° 68-279 du 7 septembre 1968, fixant le montant des redevances compensatrices applicables aux blés tendres mis en œuvre**, JORT n° 37 des 6-10 septembre 1968, p. 993-994 [IMG]. URL : https://www.pist.tn/jort/1968/1968F/Jo03768.pdf
  - Art. 1er : « A compter du 15 juin 1967 », les minotiers **versent** une redevance de 75 millimes par quintal de blé tendre (farine PS + 10), 60 millimes (PS-2) et 500 millimes (PS-7).
  - Art. 3 : la redevance va au compte « Soutien du Marché des Céréales ».
  - Art. 5 : abroge l'arrêté du 16 janvier 1960 sur les redevances et indemnités.
  - **Correction de la note principale** : en 1968, le décret n° 68-279 impose une redevance et **non une indemnité de 115 millimes**.
- **Décret n° 71-277 du 26 juillet 1971, modifiant et complétant le décret n° 68-279**, JORT n° 32 des 23-27 juillet 1971, p. 1000 [IMG]. URL : https://www.pist.tn/jort/1971/1971F/Jo03271.pdf
  - Art. 1er nouveau : « A compter du 1er août 1971 », la redevance est de 75 millimes (PS + 10) et de **715 millimes** (PS-7). « À compter de la même date, les minotiers recevront une indemnité compensatrice de 115 millimes pour chaque quintal de blé tendre mis en œuvre pour la fabrication de farine panifiable extraite à PS — 2 ».
  - Du 1er mai au 31 juillet 1971, les boulangers reçoivent une indemnité de 240 millimes par quintal de farine PS-2.
  - Art. 3 nouveau : redevances et indemnités au compte « Soutien du Marché des Céréales ».
  - **C'est le premier texte lu où la farine à pain est payée en dessous de son coût**, par péréquation entre qualités de farine, au sein du budget de l'Office. Il complète le point D3 de la note principale : l'indemnité de 115 millimes date de 1971, non de 1968.
  - Même fascicule : arrêté du 26 juillet 1971 modifiant l'arrêté du 10 août 1967 sur le prix des farines et semoules [méta, non lu].
- **Décret n° 74-876 du 24 septembre 1974, portant institution d'une taxe compensatrice sur les exportations d'huile d'olive**, JORT n° 58 des 20-24-27 septembre 1974, p. 2090 [IMG]. URL : https://www.pist.tn/jort/1974/1974F/Jo05874.pdf
  - Visa : loi de finances pour 1971, art. 48.
  - Art. 1er : « une taxe compensatrice de 80 millimes par kilogramme d'huile d'olive exporté », « retenue par l'Office National de l'Huile ».
  - Art. 2 : versée « au compte de la Caisse Générale de Compensation pour être affectée à la stabilisation du prix de vente en Tunisie des huiles de graine ».
  - Art. 3 : « prend effet à compter du 1er janvier 1974 » (effet énoncé, rétroactif).
  - L'incohérence de `jort_cache` est expliquée : le n° 58 est un fascicule triple, daté des 20, 24 et 27 septembre ; la date de publication de l'index est la première.
- **Tableau B du décret n° 82-134**, p. 230, relu à l'image [IMG] :
  - liste « à tous les stades » **confirmée telle que dans la note principale** : pain ; farine et semoule ; couscous et pâtes alimentaires ; huiles alimentaires ; sucre ; thé ; café ; chaux, ciment, briques et aciers de construction (rond à béton) ; carburants ; électricité, eau, gaz ; engrais ; transport ; livres et cahiers scolaires ; poivre ; médicaments et actes médicaux ; **lait régénéré** ; cafés et boissons servis dans les hôtels ;
  - 2°) au stade de la distribution : produits agricoles de grande consommation ou faisant l'objet d'une campagne ; « Poulets et viande bovine » ;
  - tableau C (homologation) : boissons alcoolisées, sel, margarine, levure de panification…
- **Farines de février 1984** (arrêté du 17 février 1984, JORT n° 14, p. 454) [IMG], en millimes : usine / gros / détail.
  - Farine extraite à PS, vrac 1 kg : 105 / 107 / **115**.
  - PS-7, vrac 1 kg : 140 / 143 / 160 ; paquet 1 kg : 178 / 182 / 205 ; paquet 1/2 kg : 91,5 / 94,5 / 108.
  - L'arrêté n'a pas d'art. 3 : il passe de l'art. 2 à l'art. 4.
  - Le blé tendre y est exprimé « en millimes ».
- **Décret n° 74-780, édition arabe** : non fait (Ja05274.pdf au corpus, image). Reste à faire si le terminologue en a besoin.
- **Décret n° 74-966** : toujours non lu (scan illisible). Son sort juridique est établi : supprimé le 31 mai 1975 (décret n° 75-352, art. 5 et 7).
- **Loi n° 86-106 (loi de finances pour 1987), art. 17**, visé par tous les décrets de campagne depuis 1995 : son intitulé dans `jort_cache` est « suppression des impôts agricoles » (JORT n° 78/1986, p. 1611) [méta]. Les visas des décrets n° 91-943, 92-1657 et 93-1721 [IMG] le qualifient d'« article 17 supprimant les impôts sur les céréales » : il touche à la fiscalité et non au circuit de compensation.

---

## 5. Lait, papier, fin de subvention, pain de 1991 (point 5)

- **Lait régénéré demi-écrémé**, arrêté du 11 novembre 1989, effet au 12 août 1989 (JORT n° 77, p. 1824) [IMG].
  - Prix au détail : pasteurisé tétrabrik 1 l, **310 millimes** ; 1/2 l, 155 ; stérilisé bouteille 1 l, 330 ; stérilisé UHT tétrabrik 1 l, **380**.
  - Visa : arrêté du 21 novembre 1982 « fixant le prix de vente public du lait régénéré » (JORT n° 76 du 30 novembre 1982, p. 2581) [méta, non lu].
  - Série officielle : 21 novembre 1982 (à lire) → 12 août 1989 (UHT 380) → arrêté du 30 juillet 1991 (UHT 440, note principale).
- **Opérateur du lait subventionné** : non établi. Les arrêtés imposent aux « producteurs » de lait une redevance différentielle à la Caisse générale sur leurs stocks (art. 2-3 de l'arrêté de 1989), sans nommer de concessionnaire.
- **Papier scolaire.** Loi n° 2025-17 portant loi de finances pour 2026, art. 64 (JORT AR n° 148 du 12 décembre 2025, p. 4247), intitulé « تخفيف جباية المدخلات الضرورية للشركة الوطنية لعجين الحلفاء وإعفاء الورق المدعم » [TXT AR].
  - Al. 1 : suspension de la TVA sur les équipements, matières, pâtes et services « الضرورية لإنتاج الورق ».
  - Al. 2 : ajout au tableau A du code de la TVA du n° 46 ter, « الورق المعدّ لصناعة الكتاب والكراس المدرسي ».
  - C'est une **mesure fiscale** ; elle n'établit ni l'opérateur ni le circuit de la subvention du papier. Le rôle de la SNCPA reste une hypothèse.
- **Fin de subvention 1992-1999** (maïs, tourteaux de soja, engrais, sucre local ; piste du décret n° 94-1742) : **non traité** dans cette passe.
- **Pain du 15 août 1991** [IMG] : art. 1er, « A compter du 17 août 1991 » ; fascicule n° 61 du 3-6 septembre 1991, p. 1545.
  - Effet énoncé : **17 août 1991** (antérieur à la publication). Publication : **3 septembre 1991**.
  - Les deux dates de la note principale et de l'index sont donc exactes, chacune pour ce qu'elle dit. Le TODO de la ligne 262 du chapitre est levé.

---

## 6. Ciblage 2013-2026 (fiche `r-comp-pb-ciblage-2013-2026`)

Passe élargie (17 novembre 2026) :
- **texte intégral FR**, fascicules de 2013 à 2026 : `ciblage`, `cibler`, `rationalisation de la compensation`, `subvention des produits de base`, `compensation des produits de base`, `transfert monétaire`, `revenu minimum`, `bénéficiaires de la compensation`, et les articles des lois de finances qui citent la Caisse générale de compensation ou les produits de base ;
- **miroir iort AR** : `منظومة الدعم`, `ترشيد الدعم`, `توجيه الدعم`, `المواد الأساسية المدعمة`, `الخبز المدعم`, `استهداف`.

Résultats, dont **aucun n'est un texte de ciblage des subventions alimentaires** :
- décret n° 2014-1526 (organisation du ministère des affaires sociales) : il prévoit « un nouveau concept de ciblage des bénéficiaires des aides par la mise en place d'un système de scoring ». Cela concerne l'aide sociale (renvoi aux prestations sociales) ;
- loi n° 2016-71 (article non relevé) : « ترشيد الدعم » parmi les critères d'octroi des autorisations. Ce n'est pas la compensation ;
- loi de finances pour 2018, art. 25 (JORT n° 101 du 19 décembre 2017) : « Est instituée au profit de la caisse générale de compensation une taxe à l'exportation des huiles alimentaires usagées ». C'est une **ressource** (domicile `_institution`) ;
- nominations de chefs de l'« unité de compensation des produits de base » au ministère du commerce (JORT n° 38/2014, 12/2017, 25/2018) : l'unité de 2002-2005 existe toujours ;
- décret gouvernemental n° 2018-417, procédure de la carte de boulangerie : « قطاع المخابز مرتبط بمنظومة الدعم » ;
- arrêtés « pain » de 2016 et 2020 (§ 1.3) : quotas et contrôle du circuit.

Lacunes de cette passe :
- texte intégral AR des fascicules non interrogé : la couche texte arabe est en formes de présentation, à normaliser ;
- fichiers FR vides (§ 1.1).

---

## 7. Une troisième grande réforme ? Oui, sur l'instrument et sur l'orge (1990-1993) ; non sur le payeur

**Ce que disent les décrets** (tous lus, [IMG]) :
- **Récoltes 1974 à 1987** (décrets n° 74-649 à 88-707) : le décret de campagne fixe dans son texte le prix réduit de rétrocession du blé aux minoteries (par exemple 8,800 / 7,250 D/q). L'écart avec le prix normal est versé en « indemnité compensatrice », imputée au compte de l'Office « Soutien du Marché des Céréales » (84-1520, art. 27 ; 88-707, art. 27).
- **Récoltes 1988 et 1989** (décret n° 89-1171, JORT n° 59 du 1er septembre 1989, p. 1328, art. 27 ; décret n° 90-671, art. 26) : même imputation, « dont le solde sera pris en charge par la caisse générale de compensation » ; la compensation des grains pour semences va au titre II du budget de l'État.
- **Récolte 1990** (décret n° 91-943, JORT n° 47 du 2 juillet 1991, p. 1237) : le prix réduit sort du décret ; il est « fixé par arrêté du ministre de l'économie nationale » (art. 8). L'écart devient une « prime de compensation » (art. 14), et « Le solde sera pris en charge par la caisse générale de compensation » (art. 16).
- **Récolte 1991** (décret n° 92-1657, art. 8) : le prix réduit est fixé « par décision du ministre de l'économie nationale ».
- **Récolte 1992** (décret n° 93-1721, JORT n° 65 du 31 août 1993, p. 1393-1394) :
  - art. 1er : « La commercialisation de l'orge est libre » ; il ne reste qu'un prix d'intervention ;
  - art. 7 : prix réduits « fixés par décision du Ministre de l'Economie Nationale » ;
  - art. 13 : « Le montant de la prime de compensation pris en charge par la Caisse Générale de Compensation est déterminé pour tout produit comme étant la différence entre les prix normaux de rétrocession [...] et les prix réduits de rétrocession tels que fixés par décision du Ministre ».

  Cette rédaction est reprise jusqu'au décret n° 2025-344 et à l'arrêté de 2026.

**Ce qui est une rupture du dispositif, d'après les textes :**
1. **L'instrument et la publicité du prix** : de 1974 à 1989, le prix du blé cédé aux minoteries est fixé et publié dans un décret. Depuis la récolte 1991, une décision ministérielle le fixe et le JORT ne la publie pas (§ 1.4). Le prix au cœur de la subvention sort ainsi de la norme publiée.
2. **L'orge** sort de la fixation administrative du prix à la production (récolte 1992).

**Ce qui n'est pas une rupture : le payeur.** Le passage de l'imputation de l'Office (« soutien du marché ») à la Caisse générale (« solde », puis « prime de compensation ») est réel dans le texte des décrets. Mais la BCT rattache déjà les céréales à la compensation bien avant 1989 :
- rapport pour 1974 : 10 MD « pour les céréales » versés par « les différents organismes chargés de la compensation » ;
- rapport pour 1975 : réajustement destiné à « soulager la trésorerie de la caisse générale de compensation », notamment pour les « produits à base de céréales » ;
- rapport pour 1984 : hausse des dépenses de la Caisse due aux « prix à l'importation des céréales » (note principale, § 2.4 et 3.3).

Le circuit financier entre la Caisse et le compte de l'Office avant 1989 n'est pas documenté ici. **La mention de la Caisse dans les décrets de 1989-1993 s'analyse donc comme la formalisation d'un financement existant**, sauf preuve contraire. Elle se présente comme une étape et ne fonde pas la réforme.

**Verdict.** Une troisième grande réforme fondée sur des textes lus existe : « 1990-1993 : le prix du blé subventionné sort du Journal officiel ; l'orge est libérée ». Elle est mince : deux changements, sans exposé des motifs ni rubrique qui en donne les mots ; le contexte (ajustement structurel, loi n° 91-64, VIIIe Plan, rapports de la BCT pour 1989-1993) reste à sourcer. Deux rattachements sont possibles :
- (a) en faire une réforme distincte ;
- (b) en faire le second volet de la réforme 1991-1992, centrée sur le décret n° 91-1996.

La coïncidence de dates et la loi n° 91-64, visée par les décrets n° 92-1657 et 93-1721, plaident pour (b). Dans ce cas, le chapitre garde deux grandes réformes, et le seuil de trois n'est pas atteint par un texte de nature différente.

Candidats écartés comme étapes :
- 1971 (premier soutien de la farine à pain, décret n° 71-277) et 1974 (premier prix réduit du blé, décret n° 74-649) : ils relèvent de la **mise en place** et enrichissent la section 1962-1974 ;
- 2016 et 2020 (quotas, boulangeries agréées) : contrôle du circuit ;
- 2026 (arrêté conjoint au lieu d'un décret pour la campagne) : forme de l'acte.

---

## 8. Passes proposées pour `docs/recherches.yml` (à verser par l'appelant ou l'archiviste)

**`r-comp-pb-decrets-campagne-lacunes`** : passe du 2026-11-17 (documentaliste) ; sources : `plein_texte` et `corpus` (fascicules locaux, couche texte et OCR).
- Couverture : décrets n° 96-2549 (art. 14), 2001-864 (art. 14), 2005-1983 (art. 4) et 2007-1402 (art. 15), lus au fascicule. Les campagnes 1993-1994, 1994-1995, 1997-1998 à 1999-2000, 2001-2002 à 2004-2005 et 2006-2007 sont régies par reconduction des décrets n° 93-1721, 96-2549, 2001-864 et 2005-1983.
- `couvert_jusqu_au` : 2009-12-31.
- **resultat** : `decret96-2549` (clé à créer), avec mention des trois autres textes dans la couverture. Si la fiche ne peut porter qu'une clé, prendre la plus ancienne et lister les autres en couverture.

**`r-comp-pb-prix-consommateur-apres-1991`** : passe du 2026-11-17 ; sources : `plein_texte`, `iort`, `jort_cache`.
- Couverture : texte intégral des fascicules FR de 1994 à 2026 (1999-2005 décodés), miroir iort AR, intitulés depuis 1991 ; aucun acte de prix au public.
- Trouvés : arrêtés « pain » du 22 juin 2016 et du 13 novembre 2020 (circuit, poids et quotas, sans prix), absents des intitulés de `jort_cache` ; arrêté conjoint du 2 avril 2026 (taux d'extraction). Les décrets de campagne renvoient, depuis 1992, à une « décision du ministre » pour le prix réduit du blé.
- Lacunes : 1992-1993 sans couche texte ; fichiers vides en 1995-1996 et 2018-2025 ; pages en image ; texte intégral AR non interrogé.
- `couvert_jusqu_au` : 2026-10-29 ; resultat : aucun.
- `iort_ar` à ajouter : `قرار … يتعلق بضبط أسعار`, `الفارينة المدعمة`.
- `plein_texte` à ajouter : `décision du ministre`, `prix réduits de rétrocession`.

**`r-comp-pb-prix-pain-1980`** : passe du 2026-11-17 ; sources : `jort_cache`, `corpus`.
- Couverture : intitulés de 1980-1981 (prix, farine, semoule, dérivés, boulangerie, mouture, 79-413) ; décrets n° 80-140 et 80-1257 lus (reconduction ; prix réduit du blé à 8,000 / 7,250 pour la récolte 1980).
- Lacunes : sommaires des n° 55 à 60 de 1980 non océrisés.
- `couvert_jusqu_au` : 1984-02-27 ; resultat : aucun.

**`r-comp-pb-ciblage-2013-2026`** : passe du 2026-11-17 ; sources : `plein_texte`, `iort`.
- Couverture : texte intégral FR 2013-2026 et miroir iort, termes du § 6 ; aucun texte de ciblage. Voisins : décret n° 2014-1526 (ciblage de l'aide sociale), loi de finances pour 2018, art. 25 (ressource), décret gouvernemental n° 2018-417, arrêtés « pain » de 2016 et 2020.
- Lacunes : texte intégral AR des fascicules ; fichiers FR vides.
- `couvert_jusqu_au` : 2026-10-29 ; resultat : aucun.

**Fiche nouvelle proposée `r-comp-pb-arrete-reduit-1991`**
- Objet : arrêté du ministre de l'économie nationale fixant les prix réduits de rétrocession du blé de la récolte 1990 (décret n° 91-943, art. 8).
- Requête lancée : `jort_cache`, intitulés de juillet 1991 à décembre 1992, `prix` ET (`blé` OR `rétrocession` OR `céréales`) ; aucun résultat.
- iort_ar : `أسعار إحالة القمح`.
- Lacune : 1992 sans couche texte.

---

## 9. Références candidates (CSL-JSON)

Vérifier chaque clé dans tous les `references.json` avant de l'ajouter. Ces clés n'ont pas été cherchées une à une : le bibliographe doit lancer `grep -l '"id": "<clé>"'`. Chaque ligne porte `type` et `container-title`.

```json
{"id":"decret68-279","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 68-279 du 7 septembre 1968, fixant le montant des redevances compensatrices applicables aux blés tendres mis en œuvre","issue":"37","page":"993-994","issued":{"date-parts":[[1968,9,7]]},"URL":"https://www.pist.tn/jort/1968/1968F/Jo03768.pdf"}
{"id":"decret71-277","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 71-277 du 26 juillet 1971, modifiant et complétant le décret n° 68-279 du 7 septembre 1968, fixant le montant des redevances compensatrices applicables aux blés tendres mis en œuvre","issue":"32","page":"1000","issued":{"date-parts":[[1971,7,26]]},"URL":"https://www.pist.tn/jort/1971/1971F/Jo03271.pdf"}
{"id":"decret67-408","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 67-408 du 24 novembre 1967, fixant le taux des redevances compensatrices sur les stocks de farines et de semoules détenus le 14 juin 1967","issue":"50","page":"1469","issued":{"date-parts":[[1967,11,24]]},"URL":"https://www.pist.tn/jort/1967/1967F/Jo05067.pdf"}
{"id":"decret74-649","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 74-649 du 22 juin 1974, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1974-1975","issue":"44","page":"1439-1445","issued":{"date-parts":[[1974,6,22]]},"URL":"https://www.pist.tn/jort/1974/1974F/Jo04474.pdf"}
{"id":"decret74-876","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 74-876 du 24 septembre 1974, portant institution d'une taxe compensatrice sur les exportations d'huile d'olive","issue":"58","page":"2090","issued":{"date-parts":[[1974,9,24]]},"URL":"https://www.pist.tn/jort/1974/1974F/Jo05874.pdf"}
{"id":"decret75-352","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 75-352 du 3 juin 1975, fixant le prix des farines et semoules, du pain, des pâtes alimentaires et du couscous rapide","issue":"38","page":"1192","issued":{"date-parts":[[1975,6,3]]},"URL":"https://www.pist.tn/jort/1975/1975F/Jo03875.pdf"}
{"id":"arrete-1975-06-03-prix-sucre","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre de l'économie nationale du 3 juin 1975, portant fixation des prix du sucre","issue":"38","page":"1191","issued":{"date-parts":[[1975,6,3]]},"URL":"https://www.pist.tn/jort/1975/1975F/Jo03875.pdf"}
{"id":"arrete-1975-06-03-prix-huile","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre de l'économie nationale du 3 juin 1975, portant fixation du prix de l'huile mélangée","issue":"38","page":"1189-1190","issued":{"date-parts":[[1975,6,3]]},"URL":"https://www.pist.tn/jort/1975/1975F/Jo03875.pdf"}
{"id":"decret84-785","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 84-785 du 10 juillet 1984, portant modification du décret n° 83-1075 du 17 novembre 1983 fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1983-1984","issue":"43","page":"1594","issued":{"date-parts":[[1984,7,10]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo04384.pdf"}
{"id":"arrete-1984-07-10-prix-pain","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre de l'économie nationale du 10 juillet 1984, portant fixation des prix de vente du pain","issue":"43","page":"1594-1595","issued":{"date-parts":[[1984,7,10]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo04384.pdf"}
{"id":"arrete-1985-07-15-prix-pain","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre de l'économie nationale du 15 juillet 1985, portant fixation des prix de vente du pain","issue":"55","page":"946","issued":{"date-parts":[[1985,7,15]]},"URL":"https://www.pist.tn/jort/1985/1985F/Jo05585.pdf"}
{"id":"arrete-1986-08-29-poids-pain","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre de l'industrie et du commerce du 29 août 1986, portant fixation du poids du pain","issue":"50","page":"1020","issued":{"date-parts":[[1986,8,29]]},"URL":"https://www.pist.tn/jort/1986/1986F/Jo05086.pdf"}
{"id":"arrete-1989-11-11-prix-pain","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre de l'économie nationale du 11 novembre 1989, portant fixation du poids et du prix de vente du pain","issue":"77","page":"1823","issued":{"date-parts":[[1989,11,11]]},"URL":"https://www.pist.tn/jort/1989/1989F/Jo07789.pdf"}
{"id":"arrete-1989-11-11-prix-lait","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre de l'économie nationale du 11 novembre 1989, portant fixation du prix de vente du lait régénéré demi-écrémé","issue":"77","page":"1824","issued":{"date-parts":[[1989,11,11]]},"URL":"https://www.pist.tn/jort/1989/1989F/Jo07789.pdf"}
{"id":"decret89-1171","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 89-1171 du 14 août 1989, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1988-1989","issue":"59","page":"1323-1329","issued":{"date-parts":[[1989,8,14]]},"URL":"https://www.pist.tn/jort/1989/1989F/Jo05989.pdf"}
{"id":"decret91-943","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 91-943 du 17 juin 1991, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne de 1990-1991","issue":"47","page":"1236-1242","issued":{"date-parts":[[1991,6,17]]},"URL":"https://www.pist.tn/jort/1991/1991F/Jo04791.pdf"}
{"id":"decret92-1657","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 92-1657 du 14 septembre 1992, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1991-1992","issue":"66","page":"1310-1312","issued":{"date-parts":[[1992,9,14]]},"URL":"https://www.pist.tn/jort/1992/1992F/Jo06692.pdf"}
{"id":"decret93-1721","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 93-1721 du 16 août 1993, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1992-1993","issue":"65","page":"1393-1399","issued":{"date-parts":[[1993,8,16]]},"URL":"https://www.pist.tn/jort/1993/1993F/Jo06593.pdf"}
{"id":"decret96-2549","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 96-2549 du 30 décembre 1996, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1996-1997","issue":"4","page":"57-62","issued":{"date-parts":[[1996,12,30]]},"URL":"https://www.pist.tn/jort/1997/1997F/Jo00497.pdf"}
{"id":"decret2001-864","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 2001-864 du 18 avril 2001, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 2000-2001","issue":"33","page":"922-928","issued":{"date-parts":[[2001,4,18]]},"URL":"https://www.pist.tn/jort/2001/2001F/Jo0332001.pdf"}
{"id":"decret2005-1983","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 2005-1983 du 11 juillet 2005, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 2005-2006","issue":"57","page":"1797-1798","issued":{"date-parts":[[2005,7,11]]},"URL":"https://www.pist.tn/jort/2005/2005F/Jo0572005.pdf"}
{"id":"decret2007-1402","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Décret n° 2007-1402 du 18 juin 2007, fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 2007-2008","issue":"49","page":"2087-2093","issued":{"date-parts":[[2007,6,18]]},"URL":"https://www.pist.tn/jort/2007/2007F/Jo0492007.pdf"}
{"id":"arrete-2016-06-22-pain","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre du commerce du 22 juin 2016, relatif à la production, l'exposition et la vente du pain","issue":"53","page":"2090-2091","issued":{"date-parts":[[2016,6,22]]},"URL":"https://www.pist.tn/jort/2016/2016F/Jo0532016.pdf"}
{"id":"arrete-2020-11-13-pain","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté du ministre du commerce et du développement des exportations du 13 novembre 2020, relatif à la production, l'exposition et la vente du pain","issue":"113","page":"2603-2606","issued":{"date-parts":[[2020,11,13]]},"URL":"https://www.pist.tn/jort/2020/2020F/Jo1132020.pdf"}
{"id":"arrete-2026-04-02-taux-extraction","type":"legislation","container-title":"Journal officiel de la République tunisienne","title":"Arrêté conjoint du ministre de l'agriculture, des ressources hydrauliques et de la pêche maritime et du ministre du commerce et du développement des exportations du 2 avril 2026, fixant les taux d'extraction des farines et de la semoule","issue":"35","page":"645-647","issued":{"date-parts":[[2026,4,2]]},"URL":"https://www.pist.tn/jort/2026/2026F/Jo0352026.pdf"}
```

Les autres décrets de campagne du tableau du § 3.2 suivent le même gabarit. Leurs pages et URL sont au § 3.2.

---

## 10. Notions à glossaire

| Terme FR | Source canonique | Remarque |
|---|---|---|
| Prix normal de rétrocession | décret n° 93-1721, art. 6 ; décret n° 74-649, art. 12 | base + marge (+ péréquation) ; distinct du prix réduit |
| Prix réduit de rétrocession | décret n° 74-649, art. 13 ; décret n° 93-1721, art. 7 et 13 | l'entrée `prix-reduit-retrocession` existe : l'ancrer dans le § 3 |
| Prime de compensation (céréales) | décret n° 91-943, art. 14 ; décret n° 93-1721, art. 13 | prix normal − prix réduit, à la charge de la Caisse générale |
| Indemnité compensatrice / redevance compensatrice | décrets n° 68-279, 71-277 et 74-649 (art. 22) | régime antérieur, au compte de l'Office |
| Prix d'intervention (orge) | décret n° 93-1721, art. 1er | orge libre depuis la récolte 1992 |
| Farine PS, PS-7 ; boulangerie agréée (catégories A et C) ; quota de farine PS | arrêté du 13 novembre 2020, art. 2, 4 et 5 | définit enfin « PS » : « farine panifiable (destinée à la production du pain subventionné) » |
| Taux d'extraction | arrêté conjoint du 2 avril 2026, art. 2 | farine panifiable à 85 % |

---

## 11. Lacunes et lignes de backlog

| Lacune | État |
|---|---|
| Prix au consommateur après 1991 ; acte qui les fixe | **à obtenir** (décisions non publiées) ; fiche |
| Arrêté de 1991 fixant le prix réduit de la récolte 1990 | **à chercher** (fiche nouvelle) ; 1992 sans couche texte : OCR |
| Pain à 80 millimes en 1980 | sommaires des n° 55 à 60 de 1980 : **OCR** |
| Prix réduits des récoltes 1990 à 2026 | **à obtenir** (décisions ministérielles ; peut-être rapports de l'Office des céréales ou du ministère du commerce) |
| Décret n° 74-780 en arabe ; décret n° 74-966 | **OCR** (arabe) ; **à obtenir** (74-966) |
| Arrêté du 21 novembre 1982 (lait), arrêté du 26 juillet 1971 (farines), rectificatif de 75-352 (n° 57/1975) | **lisibles**, OCR |
| Fin des subventions 1992-1999 (décret n° 94-1742) | **non traité** |
| Loi n° 86-106, art. 17 | les visas des décrets n° 91-943, 92-1657 et 93-1721 [IMG] le disent « supprimant les impôts sur les céréales » ; texte même **lisible** (n° 78/1986, p. 1611) |
| Contexte de la réforme 1989-1993 (BCT 1989-1993, VIIIe Plan) | **à chercher** dans `tunisia-data` (rapports de la BCT) |
| Date de publication du décret n° 72-244 (index : avant la signature) | **lisible** au fascicule |

Lignes à verser ailleurs :
- **`tunisia-data/sources/chercher-des-donnees-tunisie.md`** :
  - les couches texte FR de 1999-2005 sont codées par un décalage de +29 (« 6RPPDLUH » = « Sommaire ») et se décodent par `chr(ord(c)+29)`, hors espaces et sauts de ligne, avec une table pour les accents ;
  - 1992-1993 n'ont pas de couche texte ;
  - `jort_cache` omet des arrêtés du commerce de 2016 et de 2020 ;
  - pour un décret de campagne, l'article des prix normaux donne aussi, par soustraction, le prix de base ; l'article des indemnités permet de vérifier le prix réduit.
- **`backlog-modele.md`** : série « cereales-prix-campagne » 1970-2009 (§ 3.2) à verser, avec quatre ruptures à déclarer : orge (1992), composition du prix normal (1992, 2008), prix réduit non publié (1990), payeur (1988-1992). Question ouverte : la date d'effet d'une récolte.
- **`backlog-precis.md`** :
  - chapitre « Les produits de base » : réforme 1989-1993 à arbitrer (§ 7) ;
  - mise en place enrichie : 1971 (décret n° 71-277), 1974 (décret n° 74-649), 1975 (décret n° 75-352) ;
  - correction : le décret n° 68-279 crée une redevance, pas une indemnité ;
  - 74-780 et 74-966 sont abrogés dès 1975 ;
  - série du poids et du prix du pain (§ 2.3) ;
  - TODO de la ligne 262 levé (17 août / 3 septembre 1991).

Aucun PDF nouveau n'a été téléchargé : toutes les sources viennent du corpus local. Aucun processus n'est resté actif ; tous les OCR ont été lancés au premier plan.

---

## 12. Séries de prix prêtes à tracer (dinars courants)

Consigne : graphes en dinars courants et en dinars de l'année la plus récente. Chaque ligne a une date d'effet, une valeur nominale et son texte. **Aucune série n'est créée ici.** Les tableaux sont la matière à verser par le modéliste ou le collecteur. Pour les dates en cours d'année, `figtools.moyenne_annuelle_escalier` donne la moyenne annuelle d'un montant en escalier (§ 13).

Légende de la colonne « Lecture » : I = image ; T = couche texte ; B = rapport de la BCT, sans texte juridique ; M = note principale (`compensation-produits-base-documentaliste.md`).

### 12.1 Pain : grand format (le « gros pain »)

| Date d'effet | Poids | Prix (millimes) | Prix au kg (millimes, calculé) | Texte (JORT) | Lecture |
|---|---|---|---|---|---|
| avant le 31.5.1975 | 700 g | 55 | 78,6 | rapport BCT pour 1975 (prix d'avant) | B |
| 31.5.1975 | 700 g | 65 | 92,9 | décret n° 75-352 (n° 38/1975, p. 1192) | I |
| 3.5.1979 | 700 g | 70 | 100,0 | décret n° 79-413 (n° 32/1979, p. 1381) | M |
| 1980 (date non établie) | 700 g | 80 | 114,3 | rapport BCT pour 1983 ; **texte non identifié** | B |
| 1.1.1984 | 700 g | 170 | 242,9 | arrêté du 28.12.1983 (n° 1/1984, p. 9) | M |
| 1.3.1984 (calculé ; publié le 28.2.1984) | 700 g | 80 | 114,3 | arrêté du 17.2.1984 (n° 14/1984, p. 453) | M |
| 10.7.1984 | 700 g | 90 | 128,6 | arrêté du 10.7.1984 (n° 43/1984, p. 1594-1595) | I |
| 15.7.1985 | 700 g | 100 | 142,9 | arrêté du 15.7.1985 (n° 55/1985, p. 946) | I |
| 30.8.1986 | **600 g** | 100 (prix inchangé) | 166,7 | arrêté du 29.8.1986 sur le poids (n° 50/1986, p. 1020) | I |
| 12.8.1989 | **500 g** | 100 | 200,0 | arrêté du 11.11.1989 (n° 77/1989, p. 1823) | I |
| 17.8.1991 | 500 g | 120 | 240,0 | arrêté du 15.8.1991 (n° 61/1991, p. 1545) | I |
| publié le 29.6.2016 | **400 g** | non publié | — | arrêté du 22.6.2016 (n° 53/2016, p. 2090) | T |

### 12.2 Pain : petit format

| Date d'effet | Poids | Prix (millimes) | Texte | Lecture |
|---|---|---|---|---|
| 31.5.1975 | 300 g | 38 | décret n° 75-352 | I |
| 3.5.1979 | 300 g | 45 | décret n° 79-413 | M |
| 1.1.1984 | 300 g | 90 | arrêté du 28.12.1983 | M |
| 1.3.1984 (calculé) | 300 g | 50 | arrêté du 17.2.1984 | M |
| 10.7.1984 | 300 g | 60 | arrêté du 10.7.1984 | I |
| 15.7.1985 | 300 g | 70 | arrêté du 15.7.1985 | I |
| 30.8.1986 | **250 g** | 70 (prix inchangé) | arrêté du 29.8.1986 | I |
| 12.8.1989 | 250 g | 80 | arrêté du 11.11.1989 | I |
| 17.8.1991 | baguette de 250 g | 100 | arrêté du 15.8.1991 | I |
| publié le 29.6.2016 | baguette de **220 g** | non publié | arrêté du 22.6.2016 | T |

Le pain de 1980 et les années 1992-2026 sont des trous. **Ne pas interpoler.**

### 12.3 Farines et semoules, prix de détail (D/q)

| Date d'effet | Farine panifiable (PS-2, puis PS) | Semoule PS (puis PS-10) | Texte | Lecture |
|---|---|---|---|---|
| 31.5.1975 | 7,350 (PS + 10 : 6,795) | 8,100 | décret n° 75-352 | I |
| 3.5.1979 | 8,650 | 9,150 | décret n° 79-413 | M |
| 28.12.1983 | 19,500 | 27,000 (PS-10) | arrêtés du 28.12.1983 (n° 1/1984, p. 6-8) | M (I pour la farine) |
| 1.3.1984 (calculé) | 11,500 (115 millimes le kg vrac) | 14,500 (145 millimes le kg vrac) | arrêtés du 17.2.1984 (n° 14/1984, p. 452 et 454) | I (farine) ; M (semoule) |
| 10.7.1984 | — | non lu | arrêté du 10.7.1984 sur les semoules (n° 43/1984, p. 1595) | — |
| 12.8.1989 | — | 17,500 (PS-10) | arrêté du 11.11.1989 (n° 77/1989, p. 1824-1825) | I |
| 17.8.1991 | — | non lu | arrêté du 15.8.1991 sur la semoule PS-10 (n° 61/1991, p. 1546) | — |

Farine PS-7 : 25,000 D/q (28.12.1983) ; 160 millimes le kg vrac (1.3.1984) [I] ; arrêté du 11.11.1989 (p. 1821-1822), non lu.

### 12.4 Pâtes et couscous, vrac 1 kg, prix de détail (millimes)

| Date d'effet | Pâtes | Couscous rapide | Texte | Lecture |
|---|---|---|---|---|
| 31.5.1975 | 113 | 120 | décret n° 75-352 | I |
| 3.5.1979 | 125 | 135 | décret n° 79-413 | M |
| 28.12.1983 | 350 (PS-10) | 360 | arrêté du 28.12.1983 | M (OCR) |
| 1.3.1984 (calculé) | 190 | 198 | arrêté du 17.2.1984 | M (OCR) |
| 10.7.1984 | non lu | non lu | arrêté du 10.7.1984 (p. 1595-1596) | — |
| 30.8.1986 | 240 (PS/10) | 250 (P.S.-10) | arrêté du 29.8.1986 (n° 50/1986, p. 1019-1020) | I |
| 12.8.1989 | non lu | non lu | arrêté du 11.11.1989 (p. 1822-1823) | — |
| 17.8.1991 | 300 (PS-10) | 340 (PS-10) | arrêté du 15.8.1991 (p. 1545-1546) | I |

### 12.5 Sucre en poudre, prix au public (millimes le kg)

| Date d'effet | Prix | Texte | Lecture |
|---|---|---|---|
| 24.5.1974 | 170 | arrêté du 24.5.1974 (n° 36/1974, p. 1112) | M |
| 31.5.1975 | 200 (morceaux : 300) | arrêté du 3.6.1975 (n° 38/1975, p. 1191) | I |

Arrêtés suivants identifiés mais non lus : 20.2.1980 (n° 12/1980, p. 558-559) ; 22.11.1986 (n° 68/1986, p. 1337) ; 8.9.1988 (n° 61/1988, p. 1274) ; 11.11.1989 (n° 77/1989, p. 1822) ; 18.7.1990 (n° 49/1990, p. 982-983) ; 25.6.1991 (n° 48/1991, p. 1251). Prochaine étape : les lire à l'image. Ils sont tous au corpus local.

### 12.6 Huile de mélange (graines), prix au public

| Date d'effet | Prix | Texte | Lecture |
|---|---|---|---|
| avant le 1.6.1975 | 180 millimes le litre | rapport BCT pour 1975 | B |
| 31.5.1975 | 200 millimes le litre | arrêté du 3.6.1975 (n° 38/1975, p. 1189-1190) | I |
| 12.8.1989 | 340 millimes le litre (vrac) | arrêté du 11.11.1989 (n° 77/1989, p. 1823) | I |

Non lus : 21.1.1980 (n° 21/1980, p. 1021-1022) ; 29.12.1986 (n° 1/1987, p. 14) ; 15.8.1991, huile de graines en vrac (n° 61/1991, p. 1546-1547).

### 12.7 Lait régénéré demi-écrémé, prix de détail (millimes le litre)

| Date d'effet | UHT tétrabrik 1 l | Pasteurisé tétrabrik 1 l | Texte | Lecture |
|---|---|---|---|---|
| 21.11.1982 ? | non lu | non lu | arrêté du 21.11.1982 (n° 76/1982, p. 2581) | — |
| 12.8.1989 | 380 | 310 | arrêté du 11.11.1989 (n° 77/1989, p. 1824) | I |
| 1991 (arrêté du 30.7.1991 ; effet à relire) | 440 | 350 | n° 57/1991, p. 1451 | M (OCR du corpus) |

### 12.8 Prix de campagne des céréales

Le tableau du § 3.2 est prêt à tracer : une ligne par récolte. Il distingue base, prix normal et prix réduit, avec les ruptures du § 3.3. Pour l'axe des temps, prendre **l'année de récolte**, et non la date de publication.

### 12.9 Taxes et prélèvements unitaires

| Date d'effet | Objet | Montant | Texte | Lecture |
|---|---|---|---|---|
| 15.6.1967 | redevance sur le blé tendre mis en œuvre : PS + 10 / PS-2 / PS-7 | 75 / 60 / 500 millimes le quintal | décret n° 68-279 | I |
| 1.8.1971 | redevance PS + 10 / PS-7 ; **indemnité** PS-2 | 75 / 715 millimes ; −115 millimes le quintal | décret n° 71-277 | I |
| 1.7.1974 | indemnité de mouture, supplément | 185 millimes le quintal | décret n° 74-780 (M) | M |
| 1.1.1974 | taxe compensatrice sur l'huile d'olive exportée, versée à la Caisse | 80 millimes le kg | décret n° 74-876 | I |
| 31.5.1975 | indemnité PS-2 ramenée ; supplément de 1974 supprimé | 100 millimes ; 0 | décret n° 75-352, art. 6 | I |
| 3.5.1979 | indemnité de mouture de 100 millimes supprimée | 0 | décret n° 79-413, art. 6 | M (OCR) |

---

## 13. Déflateurs disponibles (rien n'est créé)

Lus dans `precis/_seriescache/` (snapshot de `figtools.series()`), `catalog.snapshot.yml`, `scripts/dinars_constants.py` et `tunisia-data/data/processed/`.

| Série (id) | Où | Couverture | Base | Ruptures et réserves |
|---|---|---|---|---|
| `ipc-longue-periode` | snapshot du précis ; tunisia-data `data/processed/ins-publications/ipc_longue_periode.csv` | **1962-2023** (le titre du catalogue dit « 1962-2003 » ; le snapshot va jusqu'en 2023) | 100 en 1970, moyenne annuelle | **Deux indices raccordés en 1970** : coût de la vie (BCT, base 1962, 131,6 en 1970), puis prix à la consommation familiale (INS, depuis 1976). Les valeurs 1962-1975 sont relevées à la main dans les rapports de la BCT. La colonne `segment` marque le raccord (« base 1962 raccordée », puis « base 1970 »). Coquille de l'annuaire 1995-2001 pour 1985 écartée. Le catalogue conseille `bct-ipc-base2015` « au-delà de 2003 », alors que le snapshot porte 2004-2023 depuis l'annuaire 2019-2023 : incohérence de fiche à signaler à `tunisia-data` |
| `bct-ipc-base2015` | snapshot du précis ; `data/processed/bct-archives/ipc_base2015.csv` | 2015-2025 | 100 en 2015, posée par définition (non lue) | Reconstituée à partir de huit rapports de la BCT. 2025 ne repose que sur un rapport. Écart entre 186,3 / 176,8 et le taux de 5,3 % imprimé, signalé. S'arrête en 2025 |
| `ins-annuaire-ipc` | snapshot | 1976-2023 | 100 en 1970 | Lectures brutes par annuaire, source de la partie 1976-2023 de `ipc-longue-periode` (colonne `retenu`) |
| `croissances-revenus-prix` (indicateur « prix à la consommation ») | snapshot | 1963-2023 | taux annuels (%) | Dérivé des précédents ; ce n'est pas un indice |
| `bct/ipc_base2005.csv`, `bct/ipc_base2010.csv` | tunisia-data seulement (hors snapshot) | 2010-2014 ; 2021-2025 et janvier 2024-2026 | 100 en 2005 ; libellé « 100 en 2010 » | Par poste COICOP, dont **« Alimentation & boissons »** : seul sous-indice alimentaire repéré. Deux fenêtres disjointes. Selon la fiche de `bct-ipc-base2015`, le libellé « base 100 en 2010 » du BSF est **périmé** (valeurs en base 2015) : ne pas employer sans vérifier |

**Pratique en place dans le précis** : `scripts/dinars_constants.py`.
- Indice : `ipc-longue-periode` (base 1970), prolongé au-delà de sa dernière année par la variation de `bct-ipc-base2015`.
- `ANNEE_BASE = 2025`.
- Montant fixé par un texte : moyenne des montants en vigueur au premier de chaque mois (`figtools.moyenne_annuelle_escalier`).
- Le chapitre `_produits_base.qmd` cite déjà ce module.

Pour les prix de 1967-2025, l'indice couvre donc toute la période, avec un **raccord en 1970** et un **prolongement en 2024-2025**. Les années 1962-1975 reposent sur l'indice du coût de la vie, dont le périmètre est différent ; à dire en légende. **Aucun déflateur du PIB** n'est au snapshot ; les tables `ins-comptes-nationaux` (PIB courant et volumes par base) le permettraient, mais avec les ruptures de base de l'annexe PIB. Recommandation : l'IPC, déjà employé.

Limites pour ces séries :
- un prix fixé en cours d'année et déflaté par l'indice annuel moyen est une approximation ; le catalogue le dit ;
- un **indice alimentaire long** n'existe pas dans l'entrepôt ; à verser au backlog de `tunisia-data` s'il est souhaité. Ce n'est pas une demande de cette note.

