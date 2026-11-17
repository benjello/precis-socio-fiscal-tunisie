# Note documentaire : « Les produits de base » (volume compensation)

Documentaliste, 17 novembre 2026. Branche `compensation/produits-de-base`. Répond aux questions
D1 à D16 de `docs/notes/plan-compensation-produits-de-base.md` (§ 9). Aucun fichier du précis
modifié, `docs/recherches.yml` non touché : les passes et fiches sont **proposées** au § 9.

**Mode de lecture**, pour chaque fait :
- **[TXT]** : couche texte du fascicule (seuls le décret n° 95-1142 et le JORT n° 121/2020) ou du miroir iort, relue ;
- **[OCR-corpus]** : océrisation déjà faite par le corpus (`markdown_output/`), relue mais non contrôlée à l'image ;
- **[OCR]** : océrisation tesseract (fra) faite pour cette note sur l'image du fascicule local,
  page ciblée ; les chiffres décisifs ont été relus à l'image quand c'est dit (**[IMG]**) ;
- **[OCR-2col]** : OCR d'une page à deux colonnes, recadrée par colonne, à relire à l'image avant
  d'en recopier une liste ;
- **[méta]** : intitulé seul (`jort_cache.db`) ;
- **[BCT]**, **[MF]**, **[RAP]** : rapport annuel de la BCT, document du ministère des Finances,
  rapport annuel de performance ; les pages BCT sont des **positions dans le fichier**
  (`pdftotext`), la pagination imprimée n'apparaissant pas dans la couche texte : à relever à
  l'image avant citation.

Les dates de signature et de publication viennent **du fascicule**, pas de `jort_cache`, qui se
trompe sur trois textes utilisés ici (voir § 8).

---

## 0. Résumé par question

| Q. | État | Ce qui est établi |
|---|---|---|
| D1 | **établi** | Décret n° 70-543, art. 1 et tableau A : liste des produits « soumis à taxation », dont pain, farine et semoule, couscous et pâtes, viandes, lait et dérivés, huiles alimentaires, sucre, thé, café, riz, poivre, engrais. Abrogé par le décret n° 82-134 (art. 8), qui reprend la taxation (art. 4, tableau B) |
| D2 | **en partie** | Série des décrets de campagne 1970-2009 identifiée (métadonnées, pages, fascicules) ; lus : 83-1274 (art. 14, 15, 22, 25), 84-150 ; prix de rétrocession de décembre 1983 relevés. Campagnes 1993-1994, 1994-1995, 1997-1998 à 1999-2000, 2001-2002 à 2004-2005, 2006-2007 absentes des intitulés |
| D3 | **en partie** | Mots de la BCT 1974 et 1975 relevés ; indemnité compensatrice aux minotiers et semouliers (décret n° 68-279, 115 millimes/q, connu par visa ; décret n° 74-780, + 185 millimes/q au 1er juillet 1974, lu) ; réajustement des prix du 1er juin 1975 (décret n° 75-352, BCT 1975). Aucun texte unique « premier prix inférieur au coût » : le mécanisme existe avant 1974 au budget de l'Office. Art. 83 de la LF 1975 : non relu ici (#810) |
| D4 | **en partie** | 68-279 et 67-408 connus par les visas de 74-780 |
| D5 | **établi (textes)** | Hausse au 28 décembre 1983 / 1er janvier 1984 (pain de 700 g : 170 millimes ; le prix antérieur de 80 millimes vient de la BCT 1983, le texte de 1980 n'est pas identifié) par décret n° 83-1274 et quatre arrêtés ; retour par décret n° 84-150 et arrêtés du 17 février 1984 (pain : 80 millimes), publiés le 28 février 1984. Contexte BCT 1984 relevé |
| D6 | **établi** | Tableau A de 1991 (rectificatif de 1992), de 1993 (décret n° 93-59) et de 1995 (décret n° 95-1142) relevés en entier. Aucun remplacement postérieur identifié (fiche relancée) |
| D7 | **non traité** | Sorties du maïs, du soja, des engrais, du sucre local : aucun texte cherché faute de temps ; piste : listes du commerce extérieur (décret n° 94-1742 et suites) |
| D8 | **en partie** | Lait régénéré subventionné au tableau A dès 1991 ; prix de 1991 relevés ; primes de 2001 aux centrales laitières financées hors Caisse ; opérateur du lait subventionné non établi ; sortie 2008 / retour 2011 : aucun texte |
| D9 | **rien de juridique** | Aucun texte de ciblage ou de transfert de substitution. Trouvé : objectif 2.1 du RAP 2023 Commerce, régime des quotas, cahier des charges de 2020 (contrôle du circuit, pas ciblage) |
| D10 | **en partie** | Derniers prix au consommateur publiés au JORT : 1991 (pain du 17 août 1991). Autorité : ministre de l'économie nationale jusqu'en 1991 (arrêtés). Aucun prix publié ensuite ; prix en vigueur non établis |
| D11 | **établi** | Décrets n° 2002-2145 (art. 1-2) et 2005-2934 (art. 1-2) lus |
| D12 | **en partie** | Décomposition 2018-2023 : la ligne « Commerce » de l'annexe des transferts contient aussi l'Office du commerce et la SNCPA ; un résidu de 181 à 303 MD par an (2018-2023) reste sans attribution |
| D13 | **non établi** | Aucune série budgétaire par produit après 2011 dans les rapports BCT 2015-2019 lus ; quantités 2021-2023 au RAP |
| D14 | **la question change** | Pâtes et couscous sont taxés depuis 1970 et « subventionnés » au tableau A depuis 1993 ; papier scolaire « subventionné » au tableau A depuis 1993 ; concentré de tomate au tableau C (marges) |
| D15 | **en partie** | Papier scolaire au tableau A (1993, 1995) ; SNCPA dans les transferts de la mission Commerce ; LF 2026 art. 64 vise le « papier subventionné » (intitulé) |
| D16 | **établi (unités)** | RAP 2023 Commerce, p. 11-12 : farine pour le pain en millions de quintaux, huile végétale en milliers de tonnes. Décret n° 74-876 et concession : non lus |

**Seuil de trois grandes réformes : non atteint.** Les deux réformes du plan (1984 ; 1991-1992)
sont maintenant sourcées par leurs prix et leur liste ; la mise en place les précède. Ni 1975
(réajustement de prix), ni 1993 (liste ramenée aux produits « subventionnés »), ni 2002-2005
(unité de compensation), ni 2020 (cahier des charges du commerce de gros) ne changent le
dispositif : ce sont des étapes. Aucun texte de ciblage (D9).

---

## 1. La liste des produits soustraits à la liberté des prix (D1, D6, D14) — section « 1991-1992 » et « État du droit »

### 1.1 1970 : la « taxation » (décret n° 70-543) [OCR-corpus]

**Décret n° 70-543 du 24 octobre 1970, relatif aux régimes de fixation des prix des produits,
marchandises et services**, JORT n° 49 des 27-30 octobre 1970, p. 1418-1419
(`markdown_output/JORT/1970/fr/Jo04970.md`, l. 461-620).
- Visa : loi n° 70-26, « notamment son article 2 ».
- Art. 1er : « Sont soumis à taxation les prix à tous les stades des marchandises et produits
  sensibles et de grande consommation et des services d'intérêt général énumérés dans le tableau
  « A » annexé au présent décret. »
- Art. 2 : homologation préalable (production : produits fabriqués ou transformés localement ;
  distribution : marchandises sans marge fixée). Art. 4 : auto-homologation (tableaux B et C).
  Art. 5 : « liberté contrôlée ». Art. 7 : « liberté totale », notamment « au stade de la
  production, les prix des produits agricoles et de la pêche ».
- **Tableau A**, « Liste des produits, marchandises et services soumis au régime de la taxation
  des prix » : Pain ; Farine et semoule ; Couscous et pâtes alimentaires ; Viandes ; Lait et
  dérivés (beurre, fromage, yoghourt) ; Huiles alimentaires ; Sucre ; Thé ; Café (lu « £até » dans l'OCR du corpus, à vérifier à l'image) ; Riz ; Poivre ;
  Radios et transistors ; Téléviseurs ; Chaux, ciments, briques, carreaux et autres matériaux de
  construction ; Engrais ; Électricité, eau, gaz ; Transports ; Articles scolaires ; Journaux ;
  Spectacles ; Carburants, lubrifiants et combustibles ; Consultations et actes médicaux ;
  Produits pharmaceutiques et articles de pansement (production seulement) ; Eaux minérales
  (production seulement).
- Modifié par les décrets n° 73-138 du 30 mars 1973 (JORT n° 13/1973, p. 543) et n° 76-34 du
  10 janvier 1976 (JORT n° 3/1976, p. 74) [méta ; non lus].
- URL : https://www.pist.tn/jort/1970/1970F/Jo04970.pdf

### 1.2 1982 : la taxation reprise (décret n° 82-134) [OCR-2col]

**Décret n° 82-134 du 27 janvier 1982, relatif aux régimes de fixation des prix des produits,
marchandises et services**, JORT n° 6 du 29 janvier 1982, p. 229-231.
- Visa du décret n° 70-543 « modifié par les décrets n° 73-138 du 30 mars 1973 et n° 76-34 du
  10 janvier 1976 ».
- Art. 4 : « Sont soumis au régime de la taxation des prix, les marchandises et les produits
  sensibles ou de grande consommation et les services d'intérêt général énumérés dans le tableau B ».
- Art. 8 : « Les dispositions du décret susvisé n° 70-543 du 24 octobre 1970 sont abrogées. »
- Tableau B, 1°) « À tous les stades » (p. 230), lecture provisoire par colonne : pain ; farine et
  semoule ; couscous et pâtes alimentaires ; huiles alimentaires ; sucre ; thé ; café ; chaux,
  ciment, briques et aciers de construction ; carburants ; électricité, eau, gaz ; engrais ;
  transport ; livres et cahiers scolaires ; poivre ; médicaments et actes médicaux ; **lait
  régénéré** ; cafés et boissons servis dans les hôtels. 2°) « Au stade de la distribution » : « les
  produits agricoles de grande consommation ou faisant l'objet d'organisation de campagne dont les
  prix viennent à subir des variations de nature à affecter les intérêts des producteurs ou
  consommateurs » ; « poulets et viande bovine ». **À relire à l'image** avant de recopier la liste
  (deux colonnes).
- Ce qui change pour l'alimentaire, sous réserve de la relecture : le lait n'est plus « lait et
  dérivés » mais « lait régénéré » ; les viandes passent au stade de la distribution ; le riz n'est
  plus taxé.
- URL : https://www.pist.tn/jort/1982/1982F/Jo00682.pdf
- Les arrêtés de prix de 1983-1991 visent tous le décret n° 82-134 (§ 2 et 4) : c'est le texte de
  régime de la période 1982-1991.

### 1.3 1991 : l'homologation à tous les stades (décret n° 91-1996) [OCR, relu]

**Décret n° 91-1996 du 23 décembre 1991, relatif aux produits et services exclus du régime de la
liberté des prix et aux modalités de leur encadrement**, JORT n° 88 du 24 décembre 1991,
p. 2052-2055 (`jort_cache` : 2052-2056). Clé existante : `decret91-1996`.
- Visas : loi n° 91-64, art. 3 ; décrets n° 70-544, 70-545, 82-134, 82-135.
- Art. 1er (p. 2052-2053) : il fixe « la liste des produits et services exclus du bénéfice du
  régime de la liberté des prix ainsi que les modalités de leur encadrement ».
- Art. 2 (p. 2053) : deux régimes. « 1) Le régime de l'homologation, c'est la fixation préalable
  par l'administration du niveau des prix ou de leurs variations » ; « 2) Le régime de
  l'autohomologation ».
- Art. 3 (p. 2053) : « Sont soumis au régime de l'homologation des prix : aux stades de la
  production et de la distribution : les prix des produits et services repris dans le tableau A ».
- Art. 5 : délai de 30 jours (remplacé par 25 jours par le décret n° 2015-307).
- **Tableau A**, publication d'origine p. 2054 [OCR], identique au **rectificatif** « rétablissant
  les annexes A et C … publié au J.O.R.T n° 88 du 24 décembre 1991 (les pages 2054 et 2055) »,
  **JORT n° 30 du 15 mai 1992, p. 581** [OCR, relu] (clé existante
  `rectificatif1992-decret91-1996-annexes-a-c`) : « Liste des produits et services soumis au
  régime de l'homologation des prix à tous les stades » :
  1 Pain subventionné ; 2 Farine et semoule ; 3 Couscous et pâtes alimentaires ; 4 Huiles
  alimentaires autres que l'huile d'olive ; 5 Sucre ; 6 Thé ; 7 Carburants [y compris GPL dans
  l'original] ; 8 Électricité, eau et gaz ; 9 Tarifs de transport des voyageurs ; 10 Médicaments
  et actes médicaux ; **11 Lait régénéré subventionné** ; 12 Tarifs de prestations postales et
  téléphoniques ; 13 Tabac, allumettes, alcool et autres produits de monopole ; 14 Tarifs des
  prestations portuaires ; 15 Tarifs des établissements d'enseignement et de formation
  professionnelle ; 16 Tarifs d'internat et des cantines scolaires et universitaires ; 17 Péages
  sur autoroutes ; 18 Construction et location d'immeubles à usage d'habitation ; 19 Tarifs
  d'entrée aux stades ; 20 Tarifs des boissons non alcoolisées servies dans les établissements
  cafetiers.
- Tableau B d'origine (p. 2054) : au stade de la production, on y trouve notamment « Lait
  concentré et en poudre », « Viande de volaille y compris abats », « Papiers, manuels et cahiers
  scolaires » [OCR]. (Le tableau B a été lui aussi rétabli : JORT n° 11/1992, p. 215 [méta].)
- URL : https://www.pist.tn/jort/1991/1991F/Jo08891.pdf ; rectificatif :
  https://www.pist.tn/jort/1992/1992F/Jo03092.pdf

### 1.4 1993 : la liste ramenée aux produits « subventionnés » (décret n° 93-59) [OCR]

**Décret n° 93-59 du 11 janvier 1993, portant modification du décret n° 91-1996**, JORT n° 6 du
22 janvier 1993, p. 129-130. Clé existante : `decret93-59`.
- Visas : loi n° 91-64, art. 3 ; « avis de la commission de la concurrence ».
- Article unique : « Les tableaux A, B et C annexés au décret sus-visé n° 91-1996 … sont annulés
  et remplacés par les tableaux A, B, et C annexés au présent décret. »
- **Tableau A** (p. 129) : 1) Pain subventionné ; 2) Farine et semoule subventionnées ;
  3) Couscous et pâtes alimentaires subventionné[e]s ; 4) Huiles alimentaires subventionnées ;
  5) Sucre subventionné ; **6) Papiers, manuels et cahiers scolaires subventionnés** ; 7) Thé ;
  8) Carburants y compris GPL ; 9) Électricité, eau et gaz ; 10) Tarifs de transport des
  voyageurs ; 11) Médicaments et actes médicaux ; **12) Lait régénéré subventionné** ; 13) Tarifs
  des prestations postales et téléphoniques ; 14) Tabacs, allumettes et alcool ; 15) Tarifs des
  prestations portuaires ; 16) Boissons chaudes (café et thé) servies dans les établissements
  cafetiers.
- **Avant → après** (alimentaire) : la farine, la semoule, les pâtes et couscous, les huiles
  alimentaires et le sucre ne sont plus homologués comme produits, mais **dans leur variété
  subventionnée** ; le papier scolaire subventionné entre au tableau A (il était au tableau B,
  production) ; la liste passe de 20 à 16 rubriques (sortent enseignement, internats et cantines,
  péages, construction et location, stades).
- Tableau C (p. 130) : riz, café, concentré de tomates, conserve d'harissa, beurre, sons et
  issues… soumis à l'« encadrement des marges de distribution ».
- URL : https://www.pist.tn/jort/1993/1993F/Jo00693.pdf

### 1.5 1995 : tableau A inchangé pour l'alimentaire (décret n° 95-1142) [TXT]

**Décret n° 95-1142 du 28 juin 1995**, JORT n° 54 du 7 juillet 1995, p. 1476. Clé existante :
`decret95-1142`.
- Article unique : tableaux A, B, C « annulés et remplacés ».
- Tableau A : mêmes seize rubriques qu'en 1993 (1 Pain subventionné ; 2 Farine et semoule
  subventionnées ; 3 Couscous et pâtes alimentaires subventionnés ; 4 Huiles alimentaires
  subventionnés [sic] ; 5 Sucre subventionnée [sic] ; 6 Papiers, manuels et cahiers scolaires
  subventionnés ; 7 Thé ; … 12 Lait regénéré subventionné ; …).
- Tableau C, « Liste des produits soumis à encadrement des marges de distribution » : riz,
  concentré de tomates (NAP 1511), sucre en morceaux (1613), beurre, papier scolaire (6212),
  cahiers scolaires (6231), farines lactées pour enfants…
- URL : https://www.pist.tn/jort/1995/1995F/Jo05495.pdf

### 1.6 Après 1995

- **Décret n° 2015-307** : ne touche pas au tableau A (déjà établi, NEG § 2.2).
- **Loi n° 2015-36, art. 78** : les textes d'application de la loi n° 91-64 « restent en vigueur
  tant qu'un nouveau texte n'est pas promulgué » (NEG). Le décret n° 91-1996 est encore visé
  « tel que modifié et complété » par l'arrêté du 1er décembre 2020 (§ 5.2).
- **Relance de la fiche `r-decret-91-1996-liste-apres-2015`** (17 novembre 2026, depuis le
  30 septembre 2015) : `jort_cache` ne rend que des arrêtés d'exemption de l'art. 5 de la loi
  n° 2015-36, le décret n° 2016-1204 (procédure d'exemption) et les décrets-lois de 2020 sur la
  répression ; le miroir iort rend un seul candidat, le décret n° 2024-5 (redevances
  d'aéroport), qui vise le décret n° 91-1996 sans le modifier ; plein texte : aucun terme dans la
  fiche. **Aucun remplacement du tableau A identifié** : la version de 1995 est la dernière
  relevée. Passe proposée au § 9.

**Conséquence pour D14.** Pâtes et couscous sont dans la liste depuis 1970 (taxation) et, comme
produits « subventionnés », depuis 1993 ; le papier scolaire subventionné, depuis 1993 ; le lait
régénéré subventionné, depuis 1991. Les mouvements de 2008 (lait) et de 2011 (pâtes, couscous,
concentré de tomate) sont des **lignes budgétaires** (BCT, MF), pas des entrées ou sorties
juridiques. Le concentré de tomate n'est jamais au tableau A : il est au tableau C (marges).

---

## 2. 1984 : hausse du 28 décembre 1983 et retour du 17 février 1984 (D5, D2) — section `sec-compensation-pb-1984`

Tous lus à l'image par OCR ; prix de rétrocession et de farine **relus à l'image** [IMG].

### 2.1 Les textes du 28 décembre 1983 (JORT n° 1 du 3 janvier 1984)

URL : https://www.pist.tn/jort/1984/1984F/Jo00184.pdf

| Texte | Page | Contenu (avant → après quand il est lu) | Effet |
|---|---|---|---|
| Décret n° 83-1274 du 28 décembre 1983, portant modification du décret n° 83-1075 du 17 novembre 1983 (campagne 1983-1984) | 5-6 | Art. 1er : remplace les art. 14, 15, 22, 23 et 25 du décret n° 83-1075. Art. 14 nouveau : rétrocession **blé dur 15,600 D/q**, **blé tendre 13,000 D/q** ; art. 15 nouveau : 15,975 et 13,375 D/q livrés aux centres, « y compris une péréquation de transport de 0,375 par quintal » [IMG]. Art. 22 nouveau : redevance compensatrice de 0,930 D/q de blé dur versée au compte « Soutien du Marché des Céréales » et indemnité de 0,536 D/q de blé tendre. Art. 2 : redevances sur les stocks des minotiers et semouliers | « à compter du 28 décembre 1983 » |
| Décret n° 83-1275 du 28 décembre 1983, abrogeant le décret n° 74-966 du 8 novembre 1974 (indemnités compensatrices applicables aux farines utilisées par les boulangers) | 6 | Art. 1er : abrogation | — |
| Décret n° 83-1276 du 28 décembre 1983, abrogeant le décret n° 74-780 du 5 août 1974 (indemnité compensatrice, marge de mouture) | 6 | Art. 1er : abrogation | — |
| Arrêté du ministre de l'économie nationale du 28 décembre 1983, fixant les prix des semoules | 6-7 | Semoule PS-10 : rendu chef-lieu 23,32[5] D/q ; gros 24,100 D/q ; public 27,000 D/q [OCR, 1er chiffre à relire]. Art. 3 : « redevances différentielles » sur les stocks au profit de la Caisse générale de compensation | « À compter du 28 décembre 1983 » |
| Arrêté du même jour, fixant les prix de vente maxima des pâtes et couscous rapide | 7-8 | Tableau usine / gros / détail ; pâtes PS-10 vrac 1 kg : 311 / 320 / 350 millimes ; couscous vrac : 322 / 330 / 360 millimes [OCR] | « À compter du 28 décembre 1983 » |
| Arrêté du même jour, fixant les prix des farines | 8 | Farine PS : 17,950 / 18,300 / **19,500 D/q** (public) ; PS-7 : 21,600 / 22,300 / 25,000 D/q [IMG] | « À compter du 28 décembre 1983 » |
| Arrêté du même jour, relatif au prix maxima de la vente du pain | 9 | Art. 1er : « À compter du 1er janvier 1984 », pain de **700 g : 170 millimes** ; pain de 300 g : 90 millimes ; prix plafonds | 1er janvier 1984 (clause du texte) |

Visas communs des arrêtés : loi n° 70-26 ; décret du 28 juin 1945 (Caisse de compensation) ;
décret n° 82-134 ; décret n° 83-1274. L'autorité de prix est donc **le ministre de l'économie
nationale, par arrêté, sous le régime de taxation du décret n° 82-134**.

### 2.2 Les textes du 17 février 1984 (JORT n° 14 du 28 février 1984)

URL : https://www.pist.tn/jort/1984/1984F/Jo01484.pdf

| Texte | Page | Contenu |
|---|---|---|
| Décret n° 84-150 du 17 février 1984, abrogeant le décret n° 83-1274 | 451 | Art. 1er : abrogation ; art. 2 : « Sont remises en vigueur les dispositions des articles 14, 15, 22, 23 et 25 du décret susvisé n° 83-1075 du 17 novembre 1983 » |
| Décret n° 84-151, abrogeant le décret n° 83-1275 | 451 | Art. 2 : « Sont remises en vigueur les dispositions du décret … n° 74-966 du 8 novembre 1974 » (indemnités aux farines des boulangers) |
| Décret n° 84-152, abrogeant le décret n° 83-1276 | 451-452 | Art. 2 : remise en vigueur du décret n° 74-780 (indemnité de mouture) |
| Décret n° 84-153, abrogeant le décret n° 79-413 du 7 mai 1979 (prix des farines et semoules, du pain, des pâtes et du couscous) | 452 | Art. 1er : abrogation. Les prix des dérivés relèvent désormais des seuls arrêtés |
| Arrêté du 17 février 1984, fixant les prix des semoules | 452 | Semoule PS-10 vrac 1 kg : 125,4 / 129 / **145 millimes** ; paquet 1 kg : 164 / 168 / 185 ; abroge l'arrêté du 28 décembre 1983 |
| Arrêté du 17 février 1984, prix des pâtes et couscous rapide | 453 | Pâtes PS-10 vrac 1 kg : 165 / 170 / **190 millimes** ; couscous vrac : 173 / 178 / 198 [OCR] |
| Arrêté du 17 février 1984, prix maxima de la vente du pain | 453 | Art. 1er : pain de **700 g : 80 millimes** ; 300 g : 50 millimes ; abroge l'arrêté du 28 décembre 1983 |
| Arrêté du 17 février 1984, prix des farines | 454 | Farine PS vrac 1 kg : 105 / 107 / **115 millimes** ; PS-7 vrac : 140 / 143 / 160 [OCR, colonnes à relire] |

**Dates.** Les textes du 17 février 1984 n'énoncent pas de date d'effet. Règle d'avant 1993 (« un
jour franc après la publication au Journal Officiel ») : publication le mardi 28 février 1984 ;
1984 est bissextile ; jour franc : 29 février ; effet calculé : **1er mars 1984**. Si le rédacteur
préfère ne pas calculer : « publiés le 28 février 1984 ». **Le plan parle d'un retour « en janvier
1984 » : les textes publiés sont de février.**

### 2.3 Le prix d'avant la hausse

- **Décret n° 79-413 du 7 mai 1979**, JORT n° 32 du 11 mai 1979, p. 1381-1382 [OCR] : « À compter
  du 3 mai 1979 », pain de 700 g « toutes catégories » : **70 millimes** ; 300 g : 45 millimes ;
  farine PS-2 : 8,650 D/q ; semoule PS : 9,150 D/q ; pâtes 0,125 D/kg et couscous rapide
  0,135 D/kg au détail. Visas : décret n° 68-279 tel que modifié par le décret n° 71-277 ; décret
  n° 74-780 ; décret n° 75-352. URL : https://www.pist.tn/jort/1979/1979F/Jo03279.pdf
- **BCT, rapport annuel 1983**, tableau « Évolution des prix de certains produits soumis au
  régime de la taxation » (position 73 dans le fichier) [BCT] : pain « 670 g » [sic] 70 millimes
  en 1979, **80 millimes en 1980**, sans changement jusqu'en 1983. Le texte de 1980 n'est pas
  identifié dans les intitulés de `jort_cache` (fiche proposée `r-comp-pb-prix-pain-1980`).
- D'où : pain de 700 g **80 millimes (1980) → 170 millimes (1er janvier 1984) → 80 millimes
  (février 1984)** ; le retour est un retour au prix de 1980.

### 2.4 Contexte selon la BCT (rapport 1984) [BCT]

- Position 131 : « Les finances publiques ont été marquées en 1984 par une conjoncture
  internationale difficile qui a entraîné, par le biais d'une appréciation continue du cours de
  certaines devises étrangères, un accroissement du service de la dette publique extérieure ainsi
  qu'une augmentation des charges de la Caisse générale de compensation. »
- Position 140 : la décélération des dépenses de fonctionnement « est due au programme
  volontariste visant à contenir le déficit budgétaire, à consolider les moyens d'intervention au
  profit de la Caisse générale de compensation et à dégager le volume d'épargne publique requis ».
- Position 151 (p. 153 imprimée selon la notice `bct-ra-1984`, lue à l'image) : « L'augmentation, d'une part, du volume des besoins et, d'autre part, des prix à
  l'importation des céréales, de l'huile de soja et du sucre, explique, dans une large mesure, la
  forte progression des dépenses de la Caisse générale de compensation. Ces dépenses sont passées
  de 149,3 millions de dinars en 1983 à 245,8 millions en 1984 » ; subventions de 106 MD à la
  Caisse, « dont 98 millions à la charge du Budget ordinaire et 8 millions par prélèvement sur les
  disponibilités du Fonds de la contribution exceptionnelle de solidarité ».
- La BCT ne dit rien, dans les passages lus, de la hausse de décembre ni de son retrait. Les
  mouvements de janvier 1984 restent sans source primaire.

---

## 3. Mise en place et passage à la subvention, 1968-1975 (D2, D3, D4)

### 3.1 L'indemnité compensatrice des minotiers et semouliers

**Décret n° 74-780 du 5 août 1974, fixant le montant de l'indemnité compensatrice, au titre de
la revalorisation de la marge de mouture applicable aux blés durs et tendres**, JORT n° 52 des
9-13 août 1974, p. 1819-1820 [OCR].
- Visas : décret-loi n° 62-10 modifié par le décret-loi n° 70-7 ; loi n° 70-26 ; décret
  n° 67-408 du 24 novembre 1967 (redevances compensatrices sur les stocks de farines et semoules
  détenus le 14 juin 1967) ; **décret n° 68-279 du 7 septembre 1968** (« redevances et indemnités
  compensatrices applicables aux blés tendres et durs mis en œuvre »), modifié par le décret
  n° 71-277 du 26 juillet 1971 ; décret n° 74-649 (campagne 1974-1975) ; arrêté du 10 août 1967
  fixant le prix des farines et semoules.
- Art. 1er : « Indépendamment de l'indemnité compensatrice de 115 millimes, prévue à l'article 1er
  du décret sus-visé du 7 septembre 1968, les minotiers recevront, à compter du 1er juillet 1974,
  une indemnité compensatrice supplémentaire de 185 millimes par quintal de blé tendre mis en
  œuvre pour la fabrication de farine panifiable. » Même indemnité de 185 millimes/q aux
  semouliers pour le blé dur.
- Art. 2 : « Le montant de ces indemnités compensatrices sera comptabilisé à la rubrique du budget
  de l'Office des Céréales intitulée « Soutien du Marché des Céréales ». »
- **À noter pour le circuit** : cette compensation est une charge du budget de l'Office des
  céréales, pas de la Caisse générale. Le mécanisme de l'indemnité existe dès 1968 (décret
  n° 68-279, connu par visa).
- URL : https://www.pist.tn/jort/1974/1974F/Jo05274.pdf

**Décret n° 74-966 du 8 novembre 1974**, indemnités compensatrices applicables aux farines utilisées
par les boulangers, JORT n° 67 du 12 novembre 1974, p. 2416 [méta] : le scan local (Jo06774.pdf)
ne s'océrise pas (texte illisible à 250 dpi). **À obtenir** : autre exemplaire (édition arabe,
pist.tn) ou OCR à plus haute résolution. URL : https://www.pist.tn/jort/1974/1974F/Jo06774.pdf

### 3.2 Le sucre en 1974 [OCR]

JORT n° 36 du 24 mai 1974 :
- Décret n° 74-573 du 24 mai 1974 (p. 1109) : « La taxe à la production perçue à l'importation des
  sucres relevant du n° 17.01B/b du tarif des douanes est suspendue à compter du 24 mai 1974. »
- Arrêté du ministre de l'économie nationale du 24 mai 1974, portant fixation des prix du sucre
  (p. 1112) : à compter du 24 mai 1974, sucre en poudre 161,5 / 165 / **170 millimes** le kg
  (cession aux grossistes / aux détaillants / vente au public) ; sucre en morceaux 231,5 / 235 /
  240 millimes ; « redevances différentielles » sur les stocks au profit de la Caisse générale de
  compensation. Visas : loi n° 70-26, décret n° 70-543, décret du 28 juin 1945.
- URL : https://www.pist.tn/jort/1974/1974F/Jo03674.pdf

### 3.3 Les mots de la BCT [BCT]

- **RA 1974** (position 57, rubrique des prix) : « La quasi-stabilité des prix des denrées
  alimentaires de grande consommation est réalisée grâce à l'intervention massive des pouvoirs
  publics qui ont non seulement procédé à des importations de quantités de produits alimentaires
  pour desserrer la pression sur la demande mais également pris en charge la différence entre les
  prix de revient à l'importation et les prix de vente sur le marché national. C'est ainsi qu'en
  1974, les différents organismes chargés de la compensation ont dû débourser, au titre de la
  stabilisation des prix, 15 millions de dinars pour le sucre, 10 millions pour les céréales,
  6 millions pour l'huile de soja et 0,5 million de dinars pour la viande. Notons que la
  subvention a également intéressé certains produits liés à la production agricole tels que les
  engrais azotés (10 millions de dinars). » Clé existante : `bct-ra-1974`.
- **RA 1974** (position 103, fonds spéciaux) : « Le niveau élevé des opérations de compensation
  s'explique par l'intervention de plus en plus accrue de l'État pour stabiliser les cours des
  produits de première nécessité importés et limiter ainsi la hausse des prix à l'intérieur du
  pays. » Dépenses de la Caisse : 9,4 MD (1973) → 27,3 MD (1974).
- **RA 1975** (position 70) : hausse des prix alimentaires « imputable principalement à
  l'augmentation des prix, décidée le premier juin 1975, de certaines denrées, notamment le sucre
  et les produits à base de céréales » ; tableau : huile mélangée 0,180 → 0,200 D/l ; sucre en
  poudre 0,170 → 0,200 D/kg ; en morceaux 0,240 → 0,300 ; farine PS+10 6,100 → 6,795 D/q ; semoule
  PS 6,900 → 8,100 D/q ; **pain de 700 g 0,055 → 0,065 D** ; pâtes 0,100 → 0,113 D/kg. « Ce
  réajustement devait soulager la trésorerie de la caisse générale de compensation lourdement
  grevée par l'élargissement de l'écart entre le prix de vente à la consommation de certains
  produits et leur coût réel. Pour les produits importés, notamment le sucre, l'augmentation n'a
  répercuté sur les prix intérieurs qu'une partie de la hausse enregistrée sur le marché
  international au cours des deux dernières années. » Clé existante (livre général) :
  `bct-ra-1975`.
- **RA 1975** (positions 116-117) : fonds spéciaux prévus à 104,5 MD « dont 83 millions de dinars
  alloués à la Caisse Générale de Compensation » ; « compte tenu d'une baisse sensible des cours
  mondiaux de certains produits compensés, notamment le sucre, les crédits prévus pour la
  compensation ont été ramenés à 65,1 millions de dinars » ; opérations de la Caisse : 52,5 MD en
  recettes et 49,2 MD en dépenses en 1975, contre 18,4 et 27,3 MD en 1974.
- Textes de 1975 correspondants [méta] : décret n° 75-352 du 3 juin 1975 « fixant le prix des
  farines et semoules, du pain, des pâtes alimentaires et du couscous rapide » (JORT n° 38 du
  3 juin 1975, p. 1192 ; rectificatif ou republication JORT n° 57/1975, p. 1814) ; arrêtés du
  3 juin 1975 fixant le prix de l'huile mélangée (p. 1189-1190) et du sucre (p. 1191). Non lus.
  URL : https://www.pist.tn/jort/1975/1975F/Jo03875.pdf
- Décret du 9 janvier 1975 « portant augmentation des prévisions de recettes et de dépenses du
  fonds spécial du trésor intitulé « caisse générale de compensation » au titre de la gestion
  1974 », JORT n° 2/1975, p. 59 [méta].

**Pour D3.** Aucun texte ne fixe « pour la première fois » un prix inférieur au coût : l'écart
entre coût et prix de vente est payé avant 1974 par l'Office des céréales (indemnités de 1968) et
il devient, en 1974, une charge de la Caisse que la BCT décrit avec les mots ci-dessus. La phrase
de contexte peut reprendre la BCT 1974 (« stabiliser les cours des produits de première nécessité
importés ») et 1975 (« soulager la trésorerie de la caisse »).

### 3.4 Les décrets de campagne des céréales 1970-2009 (D2) [méta sauf mention]

Tous intitulés « fixant le prix et les modalités de paiement, de stockage et de rétrocession des
céréales pour la campagne … ». Lignes charnières :

| Campagne | Décret | JORT (n°/année, pages) |
|---|---|---|
| 1970-1971 | n° 70-261 du 30 juillet 1970 ; modifié par n° 70-606 du 9 décembre 1970 | 37/1970, p. 985-992 ; rectificatif 43/1970, p. 1202 ; 55/1970, p. 1648-1649 |
| 1971-1972 | n° 71-253 du 8 juillet 1971 | 30/1971, p. 909-915 |
| 1972-1973 | n° 72-244 du 7 août 1972 | 32/1972, p. 1097-1103 |
| 1973-1974 | n° 73-346 du 14 juillet 1973 | 28/1973, p. 1139-1145 |
| 1974-1975 | n° 74-649 du 22 juin 1974 | 44/1974, p. 1439-1445 ; rectificatif 50/1974, p. 1711 |
| 1975-1976 | n° 75-542 du 4 août 1975 | 54/1975, p. 1674-1680 |
| 1983-1984 | n° 83-1075 du 17 novembre 1983 ; modifié par 83-1274 [lu], abrogé par 84-150 [lu] ; modifié par 84-785 du 10 juillet 1984 | 75/1983, p. 2977-2984 ; 1/1984, p. 5-6 ; 14/1984, p. 451 ; 43/1984, p. 1594 |
| 1984-1985 | n° 84-1520 du 25 décembre 1984 | 1/1985, p. 11-17 |
| 1990-1991 | n° 91-943 du 17 juin 1991 | 47/1991, p. 1236-1242 |
| 1991-1992 | n° 92-1657 du 14 septembre 1992 | 66/1992, p. 1310-1312 |
| 1992-1993 | n° 93-1721 du 16 août 1993 | 65/1993, p. 1393-1399 |
| 2007-2008 | n° 2007-1402 du 18 juin 2007 | 49/2007, p. 2087-2093 |
| 2008-2009 | n° 2008-2081 du 2 juin 2008 | 47/2008, p. 1814-1819 |
| 2009-2010 | n° 2009-1853 du 9 juin 2009 | 47/2009, p. 1556-1559 |

Autres décrets de la série [méta] : 76-812 (et 77-339), 77-981, 79-289, 80-140, 80-1257, 81-1069
(et 82-173), 82-1286, 85-1242, 87-129, 88-707, 89-1171, 90-671, 95-2021, 96-2549, 2001-864,
2005-1983. **Absents des intitulés** : campagnes 1993-1994, 1994-1995, 1997-1998 à 1999-2000,
2001-2002 à 2004-2005, 2006-2007 (fiche proposée `r-comp-pb-decrets-campagne-lacunes`). La
plupart des fascicules sont au corpus local en image (non océrisés). Prix de base et prime de
compensation : non relevés hors 1983.

---

## 4. Prix au consommateur et autorité qui les fixe (D10)

| Date d'effet | Texte (JORT) | Produit et prix | Lecture |
|---|---|---|---|
| 24 mai 1974 | arrêté du 24 mai 1974 (36/1974, p. 1112) | sucre en poudre 170 millimes/kg au public | [OCR] |
| 1er juin 1975 | décret n° 75-352 (38/1975, p. 1192) ; BCT 1975 | pain de 700 g 55 → 65 millimes | [BCT ; texte méta] |
| 3 mai 1979 | décret n° 79-413 (32/1979, p. 1381-1382) | pain de 700 g 70 millimes | [OCR] |
| 1980 | texte non identifié ; BCT 1983 | pain 80 millimes | [BCT] |
| 1er janvier 1984 | arrêté du 28 décembre 1983 (1/1984, p. 9) | pain de 700 g 170 millimes | [OCR] |
| publié le 28 février 1984 | arrêté du 17 février 1984 (14/1984, p. 453) | pain de 700 g 80 millimes | [OCR] |
| — | arrêtés du 17 juillet 1984 (43/1984, p. 1594-1596), du 19 juillet 1985 (55/1985, p. 946), 1986, 1988, 1989 (77/1989, p. 1821-1825, dont « poids et prix de vente du pain »), 1990 | pain, semoules, pâtes, sucre, farine PS-7 | [méta] |
| 17 août 1991 | arrêté du ministre de l'économie nationale du 15 août 1991 (61/1991, p. 1545) | « gros pain : 500 grammes : 120 millimes » ; « baguette : 250 grammes : 100 millimes » ; tolérance 30 g et 10 g | [OCR] |
| — | arrêté du 30 juillet 1991, lait régénéré demi-écrémé (57/1991, p. 1451) | public : pasteurisé 1 l 350 millimes ; stérilisé bouteille 1 l 380 ; UHT tétra-brik 1 l **440 millimes** | [OCR-corpus] |
| — | arrêtés de juillet 1991 (sucre, 48/1991, p. 1251) et du 15 août 1991 (pâtes, semoule PS-10 : 61/1991, p. 1545-1546) | — | [méta] |

URL du pain de 1991 : https://www.pist.tn/jort/1991/1991F/Jo06191.pdf ; du lait :
https://www.pist.tn/jort/1991/1991F/Jo05791.pdf

**Constat.** Après les arrêtés de 1991, les intitulés de `jort_cache` (français et arabes, 1991-2026)
ne portent plus aucun texte fixant le prix de vente du pain, de la farine, de la semoule, des pâtes,
du sucre, de l'huile ou du lait. Le seul texte postérieur relevé qui en parle est le cahier des
charges du 1er décembre 2020 (§ 5.2), qui oblige les grossistes à « appliquer les prix fixés
conformément à la réglementation en vigueur » (art. 5). **Prix en vigueur et autorité actuelle : non
établis**, et rien n'est conclu ici sur leur publication (fiche proposée
`r-comp-pb-prix-consommateur-apres-1991`).

**Autorité, établie pour 1974-1991** : le ministre de l'économie nationale, par arrêté, visa de la
loi n° 70-26 et des décrets n° 70-543 puis 82-134 ; jusqu'en 1984 un décret fixe aussi, à côté,
les prix de l'ensemble des dérivés (75-352, 79-413, abrogé par 84-153). Depuis 1992 : régime de
l'homologation du décret n° 91-1996 (art. 2-3) ; l'acte d'homologation n'est pas identifié pour
ces produits.

---

## 5. Circuit, opérateurs, unité de compensation (D11, D12) — section `sec-compensation-pb-circuit`

### 5.1 L'unité de compensation des produits de base [TXT, miroir iort]

- **Décret n° 2002-2145 du 30 septembre 2002, portant création d'une unité de compensation des
  produits de base**, JORT n° 81 du 4 octobre 2002, p. 2338-2339. Visas : LF 1971, art. 48 ; loi
  n° 91-64. Art. 1er : « Il est créé au ministère des finances une unité de compensation des
  produits de base, soumise à l'autorité du ministre des finances. » Art. 2 : elle est chargée
  notamment de « la fixation des besoins annuels de compensation des produits de base et les
  modalités de leur financement » et de « la participation à l'évaluation de l'efficacité des
  programmes, des mécanismes, des modalités et des procédures de compensation des produits de
  base ». URL : https://www.pist.tn/jort/2002/2002F/Jo0812002.pdf
- **Décret n° 2005-2934 du 1er novembre 2005, portant rattachement de l'unité de compensation des
  produits de base au ministère du commerce et de l'artisanat**, JORT n° 90 du 11 novembre 2005,
  p. 2988. Art. 1er : « Est rattachée au ministère du commerce et de l'artisanat, l'unité … Elle
  est placée sous l'autorité du ministre du commerce et de l'artisanat. » Art. 2 : les art. 2 à 4
  du décret de 2002 lui sont étendus. URL : https://www.pist.tn/jort/2005/2005F/Jo0902005.pdf
- Classement : ajustement (organisation administrative, « qui décide »).

### 5.2 Le commerce de gros des produits subventionnés (2020) [TXT]

**Arrêté du ministre du commerce et du développement des exportations du 1er décembre 2020,
portant approbation du cahier des charges relatif à l'organisation de l'exercice du commerce des
produits de base subventionnés par les grossistes des produits alimentaires**, JORT n° 121 du
8 décembre 2020 : édition française p. 2863-2864 (l'arrêté seul ; art. 1er : le cahier est
« annexé à la version arabe du présent arrêté ») ; **cahier des charges dans l'édition arabe,
p. 3106-3108**.
- Visas (FR) : loi n° 2009-69 ; loi n° 2015-36 ; décret-loi n° 2020-10 ; « décret n° 91-1996 …
  tel que modifié et complété » ; décret n° 99-2552.
- Art. 1er du cahier (AR, p. 3106) : objet : « ضمان التزويد المنتظم لمختلف جهات البلاد بهذه المواد
  والتحكم في مسالك توزيعها والتصدي للتلاعب بها واستعمالها في غير أغراضها أو تهريبها » (assurer
  l'approvisionnement régulier des régions, maîtriser les circuits de distribution, lutter contre
  la manipulation, le détournement d'usage et la contrebande ; traduction de travail).
- Art. 2 : produits visés : « مشتقات الحبوب : سميد وفرينة رفيعة وعجين غذائي وكسكسي ؛ زيت نباتي مدعم ؛
  سكر » (dérivés des céréales : semoule, farine fine, pâtes, couscous ; huile végétale
  subventionnée ; sucre).
- Art. 5 : appliquer « الأسعار المحددة طبقا للتراتيب الجاري بها العمل » et ne consentir aucune remise.
- Art. 6 : vente exclusive aux détaillants munis d'un identifiant fiscal, en quantités
  « raisonnables » ; interdiction de vendre « لأغراض صناعية » ; sucre blanc en vrac « المعد
  للاستعمال الحرفي » au prix réglementé, réservé aux artisans et aux apiculteurs.
- Art. 7 : saisie des achats et ventes dans les applications informatiques du ministère.
- URL : https://www.pist.tn/jort/2020/2020A/Ja1212020.pdf (édition arabe, qui porte le cahier) ;
  édition française : https://www.pist.tn/jort/2020/2020F/Jo1212020.pdf
- Classement : étape (contrôle du circuit), pas ciblage.

### 5.3 Quotas et arriérés selon le RAP 2023 Commerce [RAP]

`tunisia-data/data/raw/ministeres-tutelle/energie-industrie-commerce/gbo/2024-07_RAP2023 COMMERCE_compressed.pdf`,
p. 11-12 imprimées (arabe) :
- Objectif stratégique 2.1 : « حسن التصرف في نفقات الدعم وتوجيهه نحو مستحقيه » (bonne gestion des
  dépenses de subvention et orientation vers ceux qui y ont droit), « من خلال تنظيم ومراقبة مسالك
  توزيع المواد المدعمة ».
- Indicateur 1.2.1, « نسبة تطور الكميات المدعمة » : farine destinée au pain, **millions de quintaux** :
  6,248 (2021), 6,302 (2022), 6,488 (2023, contre 6,5 prévus, 99,82 %) ; huile végétale
  subventionnée, **milliers de tonnes** : 105,242 (2021), 67,904 (2022), 37,566 (2023, contre 174
  prévus, 21,59 %). La virgule arabe est le séparateur décimal ; le taux de 99,82 % le confirme.
- Explication de l'écart sur l'huile : stocks d'huile brute insuffisants, l'ONH n'ayant pas pu
  prendre livraison des quantités contractées faute de payer ses fournisseurs, « نتيجة التأخر في
  صرف مستحقات الدعم الراجعة لفائدة الديوان » (retard de paiement de la subvention due à l'Office).
- Mécanisme : « اعتماد نظام الحصص في توزيع مادة الفرينة على المخابز والزيت النباتي على المعلبين »
  (quotas de farine aux boulangeries, d'huile aux conditionneurs) ; application informatique de
  suivi des ventes de farine.
- Ces faits relèvent de la famille « budgétaire (performance) » ; aucun n'est un texte.
- Le PDF est déjà dans `tunisia-data` ; vérifier sa ligne de catalogue (`sources/ministere-energie-industrie-commerce.md`, l. 61, qui donne encore l'unité de la farine « à vérifier » : à corriger par le collecteur).

### 5.4 D12 : décomposition de l'écart

Sources : poste « produits de base » (`precis/_seriescache/compensation-parts.csv`, famille
budgétaire, MF ou BCT selon l'année) ; transferts par établissement de l'annexe des transferts
des lois de finances (`tunisia-data/data/processed/entreprises-publiques/transferts_budget_par_etablissement_2017_2024.csv`,
colonne « réalisations », en MD).

| Année | Poste PB | Ligne « Commerce » | OC | ONH | Office du commerce | SNCPA | PB − (OC + ONH) | PB − (OC + ONH + OCT + SNCPA) |
|---|---|---|---|---|---|---|---|---|
| 2018 | 1 750 | 1 590,5 | 1 305,8 | 249,2 | 11,2 | 2,7 | 195,1 | 181,2 |
| 2019 | 1 800 | 1 523,0 | 1 285,0 | 208,0 | — | 3,6 | 307,0 | 303,4 |
| 2020 | 2 416 | 2 152,2 | 1 848,5 | 269,0 | 14,3 | 0,1 | 298,6 | 284,2 |
| 2021 | 2 200 | 2 007,0 | 1 674,2 | 301,4 | 9,4 | 0,1 | 224,4 | 214,9 |
| 2022 | 3 771 | 3 608,5 | 3 220,9 | 358,8 | 9,4 | — | 191,3 | 181,9 |
| 2023 | 3 809,5 | 3 536,7 | 3 344,2 | 165,3 | 5,9 | — | 300,0 | 294,1 |

- La ligne « Commerce » de l'annexe dépasse OC + ONH + OCT + SNCPA (2018 : 1 590,5 contre
  1 568,8) : elle contient d'autres organismes, non ventilés ici.
- **Le résidu (181 à 303 MD par an) n'est attribué par aucune source lue.** Hypothèses
  à vérifier, non à écrire : centrales laitières (lait), conditionneurs, papier.
- SNCPA (Société nationale de cellulose et de papier alfa) : sa présence dans la mission Commerce
  et l'intitulé de la LF 2026, art. 64 (« إعفاء الورق المدعم », JORT n° 148/2025, p. 4247) font du
  papier scolaire une **hypothèse** pour D15, pas un constat.
- États : les transferts sont des colonnes « réalisations » ; le poste n'est « réalisé » qu'en 2018 (note d'exécution du MF) ; de 2019 à 2023 il vient d'une colonne « non qualifiée » des rapports de la BCT (`compensation-parts.csv`). L'écart de 2019-2023 mêle donc peut-être deux états d'exécution.
- PB − (OC + ONH) donne 191 à 307 MD : c'est l'écart cité par le plan.

### 5.5 Liste des produits exclus de la liberté du commerce extérieur (piste pour D7, D12)

Décret n° 94-1742 du 29 août 1994 « fixant les listes des produits exclus du régime de la liberté
de commerce extérieur », JORT n° 69/1994, p. 1395-1444, modifié en 1995, 1996, 1997, 1998, 2000,
2001 [méta]. C'est là que se lit, en principe, le monopole d'importation des offices (céréales,
huiles, sucre…). Non lu.

---

## 6. Le lait (D8)

- **Liste** : « Lait et dérivés » taxés en 1970 ; « lait régénéré » taxé en 1982 [OCR-2col] ;
  « Lait régénéré subventionné » au tableau A depuis 1991 (n° 11), puis n° 12 en 1993 et 1995
  [OCR/TXT]. Au tableau B de 1991 : « Lait concentré et en poudre » (production).
- **Prix** : arrêté du 30 juillet 1991 (lait régénéré demi-écrémé, § 4) ; arrêté de 1989 « portant
  fixation du prix de vente du lait régénéré demi-écrémé » (JORT n° 77 du 17 novembre 1989,
  p. 1824) [méta]. Les arrêtés visent le décret du 28 juin 1945 (Caisse de compensation) et le
  décret n° 82-134.
- **Opérateur** : non établi. Le décret n° 2001-2708 nomme les centrales laitières comme bénéficiaires d'une prime sur la poudre de lait, financée hors Caisse ; il ne dit pas qui vend le lait régénéré subventionné pour le compte de la Caisse.
- **Soutiens aux centrales, hors Caisse** [TXT, iort] : décret n° 2001-2708 du 13 novembre 2001
  (JORT n° 93 du 20 novembre 2001, p. 3975) : art. 2 : prime « au titre du soutien du prix de
  vente de la poudre de lait fabriquée à partir du lait frais produit localement », « servie au
  profit des centrales laitières par kilogramme de poudre de lait vendu », 750 millimes/kg pour
  2001 ; art. 5 : payée par le fonds de développement de la compétitivité industrielle (75 %) et
  le fonds de développement de la compétitivité dans l'agriculture et la pêche (25 %), via le
  groupement interprofessionnel du lait. **Ne pas la compter dans les charges de la Caisse.**
  Suites : stock de régulation de lait frais stérilisé (décret n° 99-658, JORT n° 28/1999,
  p. 529-530, et arrêtés annuels jusqu'en 2026) ; prime aux frais de stockage (décret
  n° 2007-244) ; prime aux frais de séchage (décret n° 2012-793, JORT n° 56/2012, p. 1673-1675,
  modifié en 2014 et 2017) [méta]. Ces textes relèvent plutôt du livre « L'agriculture » (soutien
  au producteur).
- **Sortie de 2008 et retour de 2011** : aucun texte ; connus par la BCT et le MF seulement.

---

## 7. Ciblage et transferts de substitution (D9)

**Aucun texte juridique de ciblage des subventions alimentaires ni de transfert de substitution
n'a été identifié.** Requêtes réellement lancées (17 novembre 2026, `jort_cache`, intitulés, depuis
2011) : LIKE sur `compensation`, `ciblage`, `produits de base`, `subventionn`, `transfert%monetaire`,
`identifiant unique`, et en arabe `الدعم`, `المواد الأساسية`, `التعويض`, `ترشيد`, `منظومة الدعم`,
`المدعم`, `التحويلات المالية`, `المعرف الوحيد`. Résultats pertinents, aucun n'étant un texte de
ciblage :
- arrêté conjoint du 19 mai 2020 « fixant le mode de calcul et le montant des transferts
  monétaires directs au profit des catégories pauvres bénéficiant du programme « AMEN SOCIAL » »
  (JORT n° 45/2020, p. 1097), modifié le 8 avril 2022 (JORT n° 38/2022, p. 972-973) : prestations
  sociales, renvoi ;
- loi n° 2020-17 relative à l'identifiant unique du citoyen et décret n° 2020-312 : outil, sans
  lien établi aux subventions ;
- cahier des charges du 1er décembre 2020 (§ 5.2) et RAP 2023 (§ 5.3) : contrôle du circuit ;
- LF 2024 (loi n° 2023-13), art. 19, intitulé « تكريس الدور الاجتماعي للدولة وتأمين تزويد السوق
  بالمواد الأساسية … » : il ouvre une ligne de financement sur le Fonds national de l'emploi gérée
  par la BTS (intitulé seul) ; ce n'est pas un texte de compensation.
- LF 2014, art. 76-78 (« renforcement des ressources de la caisse générale de compensation ») :
  ressources, domicile `_institution`.

Le seul énoncé officiel de ciblage relevé est l'objectif 2.1 du RAP (« توجيهه نحو مستحقيه »), qui est
un objectif de performance. La section « Le ciblage » se réduit donc aux deux phrases de renvoi
prévues par le plan. Fiche proposée : `r-comp-pb-ciblage-2013-2026`.

---

## 8. Corrections au plan et aux métadonnées

- **Plan, § 3 (1984)** : « leur retour en janvier 1984 » → les textes du retour sont du 17 février
  1984, publiés le 28 février.
- **Plan, D14** : la question suppose des entrées dans le champ vers 2011 ; juridiquement, pâtes,
  couscous et papier scolaire sont au tableau A depuis 1993 (§ 1.6).
- **`jort_cache`** :
  - décret n° 83-1274 : date de signature « 1983-12-23 » ; le fascicule dit « Fait au Palais de
    Carthage le 28 décembre 1983 », et les visas des arrêtés « du 28 décembre 1983 » ;
    `jort_annee` 1983 alors qu'il paraît au JORT n° 1 de 1984 ;
  - rétablissements du décret n° 91-1996 rangés en `jort_annee` 1991 : ils sont aux JORT n° 11 et
    n° 30 **de 1992** (le n° 30 est daté du 15 mai 1992) ;
  - décret n° 74-876 : signature 24 septembre, publication 20 septembre 1974 (incohérent, à
    vérifier au fascicule).
- **Clé `decret91-1996`** : la notice porte le n° 88 ; ajouter les pages 2052-2055 si elles
  manquent.

---

## 9. Recherches infructueuses : passes et fiches proposées (à verser par l'appelant)

**Passe proposée pour `r-decret-91-1996-liste-apres-2015`** (rôle documentaliste, 17 novembre 2026,
sources `jort_cache`, `iort`) : couverture : « relance depuis le 2015-09-30 : jort_cache (FTS et
LIKE arabes de la fiche) ne rend que des arrêtés d'exemption de l'art. 5 de la loi n° 2015-36, le
décret n° 2016-1204 et les décrets-lois de 2020 ; miroir iort (4 350 fichiers datés de 2015 et
après) : un candidat, le décret n° 2024-5 (redevances d'aéroport), qui vise le décret n° 91-1996
sans modifier le tableau A ; l'arrêté du 1er décembre 2020 (cahier des charges, JORT n° 121) vise le
décret n° 91-1996 « tel que modifié et complété » sans le modifier. Lacune : plein texte vide
(aucun terme dans la fiche) » ; `couvert_jusqu_au` : 2026-10-29 ; résultat : aucun. Ajouter un
terme plein texte, par exemple « 91-1996 ».

**Fiche nouvelle `r-comp-pb-ciblage-2013-2026`**
- objet : texte (article de loi de finances, décret, arrêté) organisant le ciblage des subventions
  aux produits de base ou leur remplacement par des transferts monétaires, 2013-2026 ;
- ou : `precis/fr/compensation/_produits_base.qmd#sec-compensation-pb-ciblage` (à créer) ;
- requêtes lancées : titres_like `%compensation%` (hors `%indemnit%`), `%ciblage%`, `%produits de
  base%`, `%subventionn%`, `%transfert%monetaire%`, `%identifiant unique%`, `%الدعم%`,
  `%المواد الأساسية%`, `%التعويض%`, `%ترشيد%`, `%منظومة الدعم%`, `%المدعم%`, `%التحويلات المالية%`,
  `%المعرف الوحيد%`, depuis 2011-01-01 ;
- iort_ar à ajouter : ترشيد الدعم ; منظومة الدعم ; توجيه الدعم لمستحقيه ; المواد الأساسية المدعمة ;
- plein texte à ajouter : « compensation des produits de base » ;
- passe : 17 novembre 2026, `jort_cache` (intitulés), résultat aucun ; lacunes : miroir iort et
  plein texte non interrogés ; couvert jusqu'au 2026-10-29.

**Fiche nouvelle `r-comp-pb-prix-consommateur-apres-1991`**
- objet : acte fixant ou homologuant, après les arrêtés du 15 août 1991, les prix de vente au
  public du pain, de la farine, de la semoule, des pâtes et du couscous, de l'huile végétale, du
  sucre et du lait subventionnés (décret n° 91-1996, tableau A, et art. 2-3) ;
- requêtes lancées : titres_like (prix ET pain|farine|semoule|sucre|huile|pates|couscous|lait),
  depuis 1984-03-01 ; LIKE arabes (`%أسعار%`|`%سعر%` ET `%الخبز%`|`%السكر%`|`%الفارينة%`|`%السميد%`|
  `%الزيت%`|`%العجين%`|`%الحليب%`), depuis 1991-10-01 ; dernier résultat : arrêtés de 1991 ;
- iort_ar à ajouter : ضبط أسعار البيع ; المصادقة على الأسعار ; الخبز ; الفارينة ; السميد ;
- passe : 17 novembre 2026, `jort_cache`, résultat aucun ; lacunes : décisions (مقرر) non publiées
  dans la partie « décrets et arrêtés », plein texte, avis et communications ; couvert jusqu'au
  2026-10-29.

**Fiche nouvelle `r-comp-pb-prix-pain-1980`**
- objet : texte fixant à 80 millimes le pain de 700 g en 1980 (BCT 1983, tableau des prix taxés),
  entre le décret n° 79-413 et l'arrêté du 28 décembre 1983 ;
- requête lancée : titres_like prix ET pain|farine|semoule|pates|79-413, du 1979-05-12 au
  1984-02-27 : seuls les arrêtés du 28 décembre 1983 ressortent ;
- à faire : sommaires des JORT de 1980 (corpus local, image) ; LF 1980-1981 ;
- passe : 17 novembre 2026, `jort_cache`, résultat aucun ; couvert jusqu'au 1984-02-27.

**Fiche nouvelle `r-comp-pb-decrets-campagne-lacunes`**
- objet : décrets fixant le prix et les modalités de paiement, de stockage et de rétrocession des
  céréales pour les campagnes 1993-1994, 1994-1995, 1997-1998 à 1999-2000, 2001-2002 à 2004-2005,
  2006-2007 ;
- requête lancée : titres_like `%cereales%` ET (`%prix%`|`%campagne%`|`%recolte%`), 1970-2009 ;
- iort_ar à ajouter : أسعار الحبوب ; إحالة الحبوب ; الصابة ;
- passe : 17 novembre 2026, `jort_cache`, résultat aucun pour ces campagnes ; lacune : intitulés
  différents possibles (« récolte »), plein texte non interrogé.

---

## 10. Références candidates (CSL-JSON)

Vérifié le 17 novembre 2026 dans tous les `precis/*/references.json` et `precis/*/*/references.json` : aucune des clés « à créer » n'existe.

**Déjà présentes** (`precis/fr/compensation/references.json`) : `decret91-1996`,
`rectificatif1992-decret91-1996-annexes-a-c`, `rectificatif1992-decret91-1996-annexe-b`,
`decret93-59`, `decret95-1142`, `loi91-64`, `loi2015-36`, `bct-ra-1974`, `bct-ra-1984`, `lfc-1984`.
**Dans `precis/fr/references.json`, à reprendre dans le livre** : `loi70-26`, `bct-ra-1975`.

**À créer** (URL pist.tn dans l'édition française, sauf mention) :

```json
{"id":"decret70-543","type":"legislation","title":"Décret n° 70-543 du 24 octobre 1970, relatif aux régimes de fixation des prix des produits, marchandises et services","container-title":"Journal officiel de la République tunisienne","issue":"49","page":"1418-1419","issued":{"date-parts":[[1970,10,24]]},"URL":"https://www.pist.tn/jort/1970/1970F/Jo04970.pdf"}
{"id":"decret82-134","type":"legislation","title":"Décret n° 82-134 du 27 janvier 1982, relatif aux régimes de fixation des prix des produits, marchandises et services","container-title":"Journal officiel de la République tunisienne","issue":"6","page":"229-231","issued":{"date-parts":[[1982,1,27]]},"URL":"https://www.pist.tn/jort/1982/1982F/Jo00682.pdf"}
{"id":"decret74-780","type":"legislation","title":"Décret n° 74-780 du 5 août 1974, fixant le montant de l'indemnité compensatrice, au titre de la revalorisation de la marge de mouture applicable aux blés durs et tendres","container-title":"Journal officiel de la République tunisienne","issue":"52","page":"1819-1820","issued":{"date-parts":[[1974,8,5]]},"URL":"https://www.pist.tn/jort/1974/1974F/Jo05274.pdf"}
{"id":"arrete-1974-05-24-prix-sucre","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 24 mai 1974, portant fixation des prix du sucre","container-title":"Journal officiel de la République tunisienne","issue":"36","page":"1112","issued":{"date-parts":[[1974,5,24]]},"URL":"https://www.pist.tn/jort/1974/1974F/Jo03674.pdf"}
{"id":"decret79-413","type":"legislation","title":"Décret n° 79-413 du 7 mai 1979, fixant le prix des farines et semoules, du pain, des pâtes alimentaires et du couscous","container-title":"Journal officiel de la République tunisienne","issue":"32","page":"1381-1382","issued":{"date-parts":[[1979,5,7]]},"URL":"https://www.pist.tn/jort/1979/1979F/Jo03279.pdf"}
{"id":"decret83-1274","type":"legislation","title":"Décret n° 83-1274 du 28 décembre 1983, portant modification du décret n° 83-1075 du 17 novembre 1983 fixant le prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1983-1984","container-title":"Journal officiel de la République tunisienne","issue":"1","page":"5-6","issued":{"date-parts":[[1983,12,28]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo00184.pdf"}
{"id":"arrete-1983-12-28-prix-pain","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 28 décembre 1983, relatif au prix maxima de la vente du pain","container-title":"Journal officiel de la République tunisienne","issue":"1","page":"9","issued":{"date-parts":[[1983,12,28]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo00184.pdf"}
{"id":"arrete-1983-12-28-prix-farines","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 28 décembre 1983, fixant les prix des farines","container-title":"Journal officiel de la République tunisienne","issue":"1","page":"8","issued":{"date-parts":[[1983,12,28]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo00184.pdf"}
{"id":"decret84-150","type":"legislation","title":"Décret n° 84-150 du 17 février 1984, abrogeant le décret n° 83-1274 du 28 décembre 1983 portant modification du décret n° 83-1075 du 17 novembre 1983 fixant les prix et les modalités de paiement, de stockage et de rétrocession des céréales pour la campagne 1983-1984","container-title":"Journal officiel de la République tunisienne","issue":"14","page":"451","issued":{"date-parts":[[1984,2,17]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo01484.pdf"}
{"id":"decret84-153","type":"legislation","title":"Décret n° 84-153 du 17 février 1984, abrogeant le décret n° 79-413 du 7 mai 1979, fixant le prix des farines et semoules, du pain, des pâtes alimentaires et du couscous","container-title":"Journal officiel de la République tunisienne","issue":"14","page":"452","issued":{"date-parts":[[1984,2,17]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo01484.pdf"}
{"id":"arrete-1984-02-17-prix-pain","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 17 février 1984, relatif aux prix maxima de la vente du pain","container-title":"Journal officiel de la République tunisienne","issue":"14","page":"453","issued":{"date-parts":[[1984,2,17]]},"URL":"https://www.pist.tn/jort/1984/1984F/Jo01484.pdf"}
{"id":"arrete-1991-08-15-prix-pain","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 15 août 1991, portant fixation des prix du pain","container-title":"Journal officiel de la République tunisienne","issue":"61","page":"1545","issued":{"date-parts":[[1991,8,15]]},"URL":"https://www.pist.tn/jort/1991/1991F/Jo06191.pdf"}
{"id":"arrete-1991-07-30-prix-lait","type":"legislation","title":"Arrêté du ministre de l'économie nationale du 30 juillet 1991, fixant les prix de vente du lait régénéré demi-écrémé","container-title":"Journal officiel de la République tunisienne","issue":"57","page":"1451","issued":{"date-parts":[[1991,7,30]]},"URL":"https://www.pist.tn/jort/1991/1991F/Jo05791.pdf"}
{"id":"decret2001-2708","type":"legislation","title":"Décret n° 2001-2708 du 13 novembre 2001, portant institution d'une prime au titre du soutien du prix de vente de la poudre de lait produite localement et fixant les modalités de son octroi","container-title":"Journal officiel de la République tunisienne","issue":"93","page":"3975","issued":{"date-parts":[[2001,11,13]]},"URL":"https://www.pist.tn/jort/2001/2001F/Jo0932001.pdf"}
{"id":"decret2002-2145","type":"legislation","title":"Décret n° 2002-2145 du 30 septembre 2002, portant création d'une unité de compensation des produits de base","container-title":"Journal officiel de la République tunisienne","issue":"81","page":"2338-2339","issued":{"date-parts":[[2002,9,30]]},"URL":"https://www.pist.tn/jort/2002/2002F/Jo0812002.pdf"}
{"id":"decret2005-2934","type":"legislation","title":"Décret n° 2005-2934 du 1er novembre 2005, portant rattachement de l'unité de compensation des produits de base au ministère du commerce et de l'artisanat","container-title":"Journal officiel de la République tunisienne","issue":"90","page":"2988","issued":{"date-parts":[[2005,11,1]]},"URL":"https://www.pist.tn/jort/2005/2005F/Jo0902005.pdf"}
{"id":"arrete-2020-12-01-cahier-produits-subventionnes","type":"legislation","title":"Arrêté du ministre du commerce et du développement des exportations du 1er décembre 2020, portant approbation du cahier des charges relatif à l'organisation de l'exercice du commerce des produits de base subventionnés par les grossistes des produits alimentaires","container-title":"Journal officiel de la République tunisienne","issue":"121","page":"2863-2864","issued":{"date-parts":[[2020,12,1]]},"URL":"https://www.pist.tn/jort/2020/2020F/Jo1212020.pdf","note":"Le cahier des charges est annexé à la seule édition arabe (n° 121, p. 3106-3108) : clé distincte « …-ar » si on le cite."}
{"id":"bct-ra-1983","type":"report","title":"25ème Rapport d'activité. Exercice 1983","author":[{"literal":"Banque centrale de Tunisie"}],"publisher":"Banque centrale de Tunisie","publisher-place":"Tunis","URL":"https://www.bct.gov.tn/bct/siteprod/documents/RA_fr_1983.pdf","note":"Titre déduit de la numérotation (17ème en 1975, 26ème en 1984) : à vérifier sur la couverture. Couverture sans date de parution probable (cf. bct-ra-1984). PDF local tunisia-data/data/raw/bct-archives/109/RA_fr_1983.pdf."}
{"id":"rap-2023-commerce","type":"report","title":"Rapport annuel de performance 2023 — mission Commerce","author":[{"literal":"Ministère du Commerce et du Développement des exportations"}],"issued":{"date-parts":[[2024,7]]},"language":"ar","note":"Titre arabe exact et URL gbo.tn à reprendre du catalogue tunisia-data (fichier 2024-07_RAP2023 COMMERCE_compressed.pdf)."}
```

Pour les décrets de campagne 1983-1984 (83-1075, 84-785), 84-151, 84-152, les arrêtés du 17 février
1984 (semoules, pâtes, farines) et ceux du 28 décembre 1983 (semoules, pâtes) : même gabarit,
pages au § 2.

---

## 11. Notions à glossaire (à vérifier par le terminologue)

| Terme FR | Source canonique pressentie | AR (si lu) | Remarque |
|---|---|---|---|
| Taxation (des prix) | décret n° 70-543, art. 1er ; décret n° 82-134, art. 4 | à relever (édition arabe 1970/1982) | régime de 1970-1991 ; à distinguer de « taxe » |
| Homologation des prix à tous les stades | décret n° 91-1996, art. 2-3, tableau A | « المصادقة الادارية للاسعار في كل المراحل » (glossaire existant) | entrée `homologation-des-prix` existante : ajouter le tableau A de 1993/1995 |
| Liberté contrôlée ; liberté totale | décret n° 70-543, art. 5 et 7 | à relever | historique |
| Indemnité compensatrice | décret n° 74-780, art. 1er | à relever | payée aux minotiers et semouliers |
| Redevance compensatrice ; redevance différentielle | décret n° 83-1274, art. 22 ; arrêtés du 28 décembre 1983, art. 3 | à relever | sur les stocks, au profit de l'Office ou de la Caisse |
| Prix de rétrocession (des blés) | décret n° 83-1274, art. 14 | à relever | le plan dit « prix normal de rétrocession » (décrets récents) |
| Soutien du marché des céréales (compte) | décret n° 74-780, art. 2 ; décret n° 83-1274, art. 25 | à relever | compte du budget de l'Office |
| Produits de base subventionnés | arrêté du 1er décembre 2020 | « المواد الأساسية المدعمة » (JORT ar n° 121/2020, p. 3106) | compléter l'entrée `produits-de-base` |
| Unité de compensation des produits de base | décret n° 2002-2145, art. 1er | à relever | |
| Lait régénéré (subventionné) | décret n° 91-1996, tableau A | à relever | |
| Farine extraite à PS, PS-7 ; semoule PS-10 | arrêtés de 1983-1984 ; arrêté du 16 janvier 1960 (taux d'extraction) | à relever | sigle « PS » non défini dans les textes lus |
| Quota (de farine, d'huile) | RAP 2023 Commerce, p. 12 | « نظام الحصص » | performance, pas droit |

---

## 12. Lacunes (état : lisible / OCR / à obtenir)

| Lacune | État |
|---|---|
| Tableau B du décret n° 82-134 (p. 230) : liste à confirmer | **OCR fait, à relire à l'image** (Jo00682.pdf, image locale) |
| Décret n° 74-966 (farines des boulangers) | **à obtenir** : scan local inexploitable ; édition arabe ou autre copie |
| Décret n° 68-279 (indemnité de 115 millimes) et 67-408 | lisibles au corpus (fascicules 1967-1968 à vérifier), **OCR** |
| Décrets de campagne 1970-2009 : prix de base, prime, rétrocession | corpus local en image, **OCR** page par page ; 1970-1972 en markdown |
| Campagnes absentes des intitulés (§ 3.4) | **à chercher** (fiche) |
| Décret n° 75-352 et arrêtés du 3 juin 1975 | corpus local (Jo03875.pdf), **OCR** |
| Texte du pain à 80 millimes en 1980 | **à chercher** (fiche) |
| Art. 83 de la LF 1975 | domicile #810, non relu ici |
| D7 : sorties du maïs (1992), des tourteaux de soja (1993), des engrais et du sucre local (1999) | **non cherché** ; piste : décret n° 94-1742 et suites, LF |
| Prix au consommateur après 1991 et acte d'homologation | **à chercher** (fiche) |
| Lait : sortie 2008, retour 2011 | aucun texte ; sources budgétaires seulement |
| D12 : bénéficiaire du résidu de 181-303 MD | **à obtenir** : PAP/RAP de la mission Commerce (programme « produits de base »), lois de règlement |
| D13 : série budgétaire par produit après 2011 | **à obtenir** : PAP/RAP Commerce, budgets citoyens, lois de règlement ; BCT 2015-2019 sans ventilation (passages lus) |
| D15 : papier scolaire, prise en charge par le CNP en 1995 | non traité ; LF 2026 art. 64 à lire (JORT n° 148/2025, p. 4247) |
| D16 : décret n° 74-876 (taxe compensatrice sur l'huile d'olive exportée, JORT n° 58/1974, p. 2090) ; concession d'approvisionnement en huile végétale | corpus local, **OCR** ; concession : à chercher |
| Pagination imprimée des rapports BCT 1974, 1975, 1983, 1984 | **lisible** à l'image (positions données) |

**Études et rapports à signaler** : aucun PDF nouveau à télécharger pour cette note ; le RAP 2023
Commerce et les rapports BCT sont déjà dans `tunisia-data`. La ligne du catalogue
`sources/ministere-energie-industrie-commerce.md` (l. 61) est à corriger (unités du RAP 2023).

---

## 13. Lignes à verser (destination ; non écrites ici, consigne de l'appelant)

- **`tunisia-data/sources/bct-archives.md`, « Index des tableaux »** :
  - RA 1974 : dépenses de stabilisation des prix par produit (sucre, céréales, huile de soja,
    viande, engrais), rubrique des prix (position 57) ; Caisse générale, recettes et dépenses
    1973-1974, fonds spéciaux (position 103) ;
  - RA 1975 : tableau « Évolution des prix à la consommation de certaines denrées alimentaires »
    au 1er juin 1975 (position 70) ; prévision et exécution de la Caisse (positions 116-117) ;
  - RA 1983 : tableau « Évolution des prix de certains produits soumis au régime de la taxation »,
    1979-1983 (position 73) ;
  - RA 1984 : fonds spéciaux et Caisse générale, 1983-1984 (positions 140 et 151 ; p. 153 imprimée
    pour la seconde).
- **`tunisia-data/sources/chercher-des-donnees-tunisie.md` (playbook)** :
  - les dates et l'année de `jort_cache` peuvent être fausses (décret n° 83-1274 ; rétablissements
    de 1992 rangés en 1991) : prendre la date au fascicule ;
  - pour un tableau ou une page à deux colonnes d'un JORT scanné : rendu à 400 dpi, recadrage par
    colonne, `tesseract --psm 6` ; dans les JORT des années 1980, « d » (dinar) est souvent lu « 4 »
    (« 15d,600 » → « 154,600 ») : relire les montants à l'image ;
  - les scans de certains fascicules de 1974 (n° 67) ne s'océrisent pas à 250 dpi.
- **`tunisia-data/sources/ministere-energie-industrie-commerce.md`, l. 61** : unités du RAP 2023
  Commerce : farine en millions de quintaux, huile végétale en milliers de tonnes (p. 11-12
  imprimées) ; la mention « à vérifier » peut être levée.
- **`docs/notes/backlog-precis.md`** (par l'archiviste) : les lacunes du § 12, avec leur état
  « lisible / OCR / à obtenir », sous le chapitre « Les produits de base ».
- **`docs/recherches.yml`** (par l'appelant ou l'archiviste, via `scripts/recherches.py`) : la passe
  et les quatre fiches du § 9.
