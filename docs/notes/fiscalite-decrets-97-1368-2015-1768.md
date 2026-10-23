# Décrets n° 97-1368 et n° 2015-1768 : régime fiscal des bières, vins et alcools

Note documentaliste, 23 octobre 2026. Lecture sur pièce des fascicules du corpus local
(`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`), éditions française et arabe. Volume concerné :
Fiscalité, chapitre `_droits_consommation.qmd` (l. 142-146 et registre `tbl-dc-chronologie`).
Aucun `.qmd` modifié.

## 0. Résumé

- **Décret n° 97-1368 du 24 juillet 1997**, « relatif au régime fiscal des produits relevant des
  numéros 22-03 à 22-08 du tarif des droits de douane ». JORT n° 59 du 25 juillet 1997, édition
  française p. 1301-1316, édition arabe p. 1362-1377. 46 articles et 4 annexes. C'est le code
  complet de la fiscalité des boissons alcoolisées : TVA (art. 1er), redevables (art. 2), tarifs
  du droit de consommation (art. 3-5 et annexes I-III), capsule fiscale sur les vins (art. 6-8,
  annexe IV), obligations des producteurs, embouteilleurs, distillateurs et brasseurs (art. 9-37),
  contrôle et sanctions (art. 38-42), stocks en cas de hausse de tarif (art. 43), mesures
  transitoires (art. 44), abrogation du décret n° 93-2090 (art. 45).
  **Exécutoire le 4 août 1997** : fascicule déposé au siège du gouvernorat de Tunis le 30 juillet
  1997, selon l'édition arabe ; le décret n'a pas de clause d'effet générale.
- **Décret gouvernemental n° 2015-1768 du 10 novembre 2015**. JORT n° 92 du 17 novembre 2015,
  édition française p. 2721-2722, édition arabe p. 3173-3174. Trois articles. Il remplace les
  annexes I, II et III du décret de 1997 par **une annexe unique**. La bière passe d'un tarif par
  récipient à un tarif au centilitre (0,018 D/cl) ; le vin en bouteille, de quatre tranches de
  contenance à 1,8 D/litre ; les spiritueux, le vermouth et les eaux-de-vie passent à un taux
  uniforme de 50 %.
  **Exécutoire le 24 novembre 2015** : déposé le 19 novembre 2015 ; pas de clause d'effet.
- La chaîne complète des textes modificatifs comprend **cinq décrets** : 2002-627, 2007-1977,
  2013-929, 2015-1768 et **2022-545**. Le dernier, qui remplace l'annexe IV (tarif de la capsule
  fiscale), est **absent du volume et de `references.json`**. Les six fascicules ont été lus ; la
  date d'effet de chacun est établie (§ 4).

## 1. Localisation et vérification par une seconde voie

| Texte | Notice `jort_cache` (recid) | Fichier local FR | Fichier local AR | Couche texte |
|---|---|---|---|---|
| décret n° 97-1368 | 89883 | `1997/fr/Jo05997.pdf` | `1997/ar/Ja05997.pdf` | FR : p. 1301 seulement ; p. 1302-1316 **en image** (OCR + lecture à l'image). AR : p. 1362 seulement ; p. 1363-1377 en image |
| décret n° 2002-627 | 86950 | `2002/fr/Jo0272002.pdf` | `2002/ar/Ja0272002.pdf` | police décalée de 29, décodée (outillage-sources § 5) |
| décret n° 2007-1977 | 83320 | `2007/fr/Jo0632007.pdf` | `2007/ar/Ja0632007.pdf` | oui |
| décret n° 2013-929 | 79586 | `2013/fr/Jo0142013.pdf` | `2013/ar/Ja0142013.pdf` | oui |
| décret gouv. n° 2015-1768 | 78328 (intitulé arabe, champ `pages` vide) | `2015/fr/Jo0922015.pdf` | `2015/ar/Ja0922015.pdf` | oui |
| décret prés. n° 2022-545 | 168695 | `2022/fr/Jo0712022.pdf` | `2022/ar/Ja0712022.pdf` | oui |
| décret n° 93-2090 (antécédent) | 91746 | `1993/fr/Jo08093.pdf` | — | non (OCR + lecture à l'image) |

La copie locale du fascicule français de 1997 est identique à celle de pist.tn : même empreinte
SHA-256, `5387eca39e257b1946d7fb7856cfc38082ed54e6806d5be6c4cb95fc92566db0`.

La liste des modificatifs a été obtenue par deux voies :
1. notices `jort_cache` : `numero`, `titre LIKE '%97-1368%'`, `'%1368%1997%'`,
   `'%1368 لسنة 1997%'`, `objet LIKE '%1368%1997%'`, `'%22-03 a 22-08%'`, `'%22.03 a 22.08%'`,
   `'%22.3 a 22.8%'` ;
2. plein texte de **tous** les fascicules locaux de 2016 à 2026, FR et AR (`pdftotext` ;
   motifs `97-1368`, `97 - 1368`, `1368 لسنة 1997`, `1368.*1997`). Seul résultat : le
   JORT n° 71 de 2022 (FR et AR), c'est-à-dire le décret n° 2022-545. Ce balayage ne lit que les
   fascicules qui ont une couche texte ; les fascicules scannés de cette période échappent au
   motif.

## 2. Décret n° 97-1368 du 24 juillet 1997 : contenu article par article

**Fondement et visas** (FR p. 1301) : décret du 10 octobre 1919 (répression des fraudes) ;
**décret du 20 novembre 1927 réglementant le régime des alcools** ; **décret du 21 mai 1931 relatif
à l'impôt sur la vigne**, « et notamment l'article 17 de la loi n° 86-106 du 31 décembre 1986 »
(LF 1987) ; code de la TVA ; loi n° 88-62 ; loi n° 88-145 (LF 1989), « notamment son article 86 » ;
loi n° 92-117 (protection du consommateur) ; décret n° 93-2090 du 11 octobre 1993 ; avis des
ministres de l'agriculture, de l'industrie et du commerce, et du tribunal administratif.

**Lecture de la p. 1302 (art. 1er à 5 et début de l'art. 6).** Dans le fascicule français
(local et pist.tn), cette page est presque effacée. Elle est restée illisible à 400 dpi, même
avec un contraste renforcé. **Les articles 1er à 5 ont donc été lus dans l'édition arabe,
p. 1363**, et l'article 6 à la p. 1364. Aucune citation française n'en est donnée ci-dessous ; les
formulations sont des traductions de travail.

- **Art. 1er** (AR p. 1363). TVA à **17 %** pour les bières, vins, boissons alcoolisées et alcools
  des positions 22-03, 22-04, 22-05, 22-06 et 22-07, ainsi que pour les préparations alcooliques de
  la position 22-08. TVA à **29 %** pour les boissons alcoolisées de la position 22-08. Texte
  arabe : « تخضع للأداء على القيمة المضافة بنسبة 17 % الجعة والخمور والمشروبات الكحولية والكحول
  المدرجة تباعا بالأعداد 03-22 و04-22 و05-22 و06-22 و07-22 … وكذلك المستحضرات الكحولية المدرجة
  بالعدد 08-22 » ; « وتخضع للأداء على القيمة المضافة بنسبة 29 % المشروبات الكحولية المدرجة
  بالعدد 08-22 ».
- **Art. 2.** Redevables du droit de consommation sur les bières, vins, boissons alcoolisées et
  alcools : fabricants et conditionneurs de bière, en bouteilles ou en autres récipients ;
  vendeurs de vin en vrac aux embouteilleurs, et embouteilleurs de vin ; fabricants d'alcool ;
  fabricants et embouteilleurs de boissons alcoolisées ; grossistes en bières, vins, alcools et
  boissons alcoolisées.
- **Art. 3.** Les tarifs du droit de consommation applicables aux bières classées, aux vins
  classés, aux boissons alcoolisées et aux alcools sont fixés aux annexes I, II et III. Les vins,
  les bières et les boissons alcoolisées sont classés par arrêté du ministre chargé du secteur.
- **Art. 4.** Bière en récipients de plus d'un litre et vin en bouteilles de plus d'un litre : le
  droit se liquide, par 10 centilitres ou fraction de 10 centilitres, au dixième du tarif
  applicable au litre. Texte arabe : « يحتسب المعلوم على الاستهلاك على أساس عشر التعريفة المطبقة
  على اللتر الواحد لهذه المنتوجات لكل عشرة سنتلتر أو جزء منها ».
- **Art. 5.** Les tarifs des articles 3 et 4 sont **doublés** pour les bières et les vins **non
  classés** au sens de la législation en vigueur.
- **Art. 6** (AR p. 1364 ; FR p. 1303 pour la fin). Une **capsule fiscale** est instituée sur les
  vins en bouteilles, « pour garantir le recouvrement des impôts et droits dus sur les vins »
  (traduction de « لضمان استخلاص الأداءات والمعاليم المستوجبة على الخمور »). Elle compte six
  catégories, selon la nature du vin et la contenance de la bouteille, et son tarif est celui de
  l'annexe IV.
- **Art. 7** (FR p. 1303). Mention « Capsule Fiscale » et catégorie. Couleur verte pour les vins
  premier cru d'appellation d'origine contrôlée, bleue pour les vins d'appellation d'origine
  contrôlée, noire pour les vins de consommation courante.
- **Art. 8** (FR p. 1303). Le ministère des finances émet la capsule ; des personnes autorisées
  par le ministre la distribuent. En cas de contrefaçon, de distribution, de transport ou d'usage
  de capsules falsifiées : amende de « 200% des droits et taxes dus sur les vins représentés par
  les capsules falsifiées », confiscation, et sanctions des articles 180 et 181 du code pénal
  (montant vérifié à l'image).
- **Art. 9 à 12** (p. 1303-1305). Producteurs de vin : déclaration d'existence de l'unité de
  vinification (adresse, plan, matériel, cuves) ; toute modification déclarée dans les dix jours ;
  dates de vinification annoncées au moins dix jours à l'avance ; déclaration de récolte et de
  stocks au plus tard le **31 octobre** (art. 11) ; registre de comptabilité matière (art. 12).
- **Art. 13 à 17** (p. 1305-1306). Embouteilleurs de vin : déclaration d'existence ; **caution**
  égale au droit afférent aux quantités mises en bouteille, calculée sur la moyenne mensuelle des
  achats de vin en vrac de l'année précédente (art. 14) ; registres des vins et des capsules
  (art. 15-16) ; capsule apposée « immédiatement après le remplissage de la bouteille » (art. 17).
  Vin vendu, acheté, transporté ou détenu sans capsule ou avec une capsule non conforme : amende
  de « 5 dinars par bouteille de vin avec un minimum de 50 dinars » (vérifié à l'image).
- **Art. 18** (p. 1307). Manquants de vin admis jusqu'à « 1,25% des quantités vendues », au titre
  de l'outillage, du coulage, du soutirage, de la purification et des autres déchets (vérifié).
- **Art. 19 à 29** (p. 1307-1310). Alcools : autorisation préalable d'ouverture d'un entrepôt
  d'alcool (art. 19) ; déclaration d'existence des fabricants (art. 20) ; caution égale au droit dû
  sur le stock mensuel moyen (art. 21) ; distillation annoncée dix jours à l'avance, rendement
  minimum déclaré (art. 22) ; matériel scellé ou présence continue des agents (art. 23) ;
  autorisation des alambics (art. 24) ; registres de fermentation, de production et de
  comptabilité matière (art. 25-28) ; manquants admis jusqu'à 1,25 % (art. 29, vérifié).
- **Art. 30** (p. 1310). Dénaturation obligatoire des alcools destinés à la parfumerie, aux
  cosmétiques, aux produits pharmaceutiques et au vinaigre, ainsi qu'à l'usage industriel et
  ménager, en présence de deux agents.
- **Art. 31-32** (p. 1310-1312). Circulation sous **congé** si le droit a été acquitté au plein
  tarif, sous **acquit-à-caution** dans les autres cas. Amende : « 10 dinars par litre d'alcool ou
  de boissons alcoolisées et à 50 dinars par hectolitre ou fraction d'hectolitre de vin ou de lies
  et à 10 dinars par tonne ou fraction de tonne de marcs et à 0,100 dinar par capsule fiscale »
  (vérifié). L'art. 32 énumère les mentions obligatoires des titres de circulation.
- **Art. 33** (p. 1312). Les unités de mise en bouteille sont indépendantes des unités de
  production.
- **Art. 34-36** (p. 1312-1313). Brasseurs et conditionneurs de bière : déclaration d'existence et
  registres.
- **Art. 37.** Registres et documents conservés dix ans.
- **Art. 38** (p. 1313). Contrôle et inventaires par les agents. Manquants ou excédents chez les
  producteurs et conditionneurs : amende de « 50 dinars par hectolitre ou fraction d'hectolitre »
  et paiement des droits. Capsules manquantes ou excédentaires chez les embouteilleurs : « 0,100
  dinar par capsule fiscale avec un minimum de 50 dinars » (vérifié).
- **Art. 39-40** (p. 1314). Infractions constatées par les agents fiscaux, les douanes et les
  agents habilités en matière de circulation ; à défaut de sanction particulière, renvoi au code
  de la TVA.
- **Art. 41-42** (p. 1314). Contrôle intermittent ou permanent, aux frais des fabricants. En
  surveillance permanente, l'entreprise fournit un bureau et rembourse les émoluments. Hors heures
  légales, l'entreprise paie, par heure ou fraction d'heure, « 1.5 dinars » entre 6 h et 21 h et
  « 3 dinars » entre 21 h et 6 h (vérifié).
- **Art. 43** (p. 1315). À toute modification des tarifs, les grossistes inventorient leurs stocks
  dans les 48 heures et paient, dans les dix jours, le supplément de droit sur ces stocks.
- **Art. 44** (p. 1315). **Dates d'application propres** :
  - les dispositions sur la capsule s'appliquent dans un délai de dix jours au plus à compter du
    jour où l'administration a avisé les embouteilleurs de l'émission de la capsule. Cette date
    ne se lit pas au JORT ;
  - les producteurs et embouteilleurs déclarent leurs stocks de vin en vrac dans les dix jours de
    la publication du décret.
- **Art. 45.** « Sont abrogées les dispositions antérieures contraires au présent décret et
  notamment le décret n° 93-2090 du 11 octobre 1993. »
- **Art. 46.** Exécution. Signé « Tunis, le 24 juillet 1997. Zine El Abidine Ben Ali ».

### Annexes (FR p. 1316, lues à l'image)

**Annexe I. Bières (22-03).** Bière classée, en récipients :

| Récipient et contenance | Droit |
|---|---|
| boîte < 0,250 l | 0,160 D l'unité |
| boîte de 0,250 à 0,320 l | 0,430 D l'unité |
| bouteille ≤ 0,320 l | 0,430 D l'unité |
| bouteille ou boîte de 0,321 à 0,400 l | 0,510 D l'unité |
| bouteille ou boîte de 0,401 à 0,500 l | 0,600 D l'unité |
| bouteille ou boîte de 0,501 à 0,660 l | 0,670 D l'unité |
| bouteille ou boîte de 0,661 à 1 l | 1,200 D l'unité |

S'y ajoutent la bière à pression classée, 0,780 D/litre, et la bière en vrac classée,
0,610 D/litre.

**Annexe II. Vins (Ex 22-04).**

| Produit | Droit |
|---|---|
| vins en vrac classés livrés aux embouteilleurs | 5,000 D l'hectolitre |
| vins mousseux classés, bouteille ≤ 1 l | 16,000 D l'unité |
| vins de liqueur, mistelles, moûts à l'alcool, classés, bouteille ≤ 1 l | 2,500 D l'unité |
| autres vins classés, bouteille ≤ 0,375 l | 0,450 D l'unité |
| autres vins classés, bouteille de 0,376 à 0,500 l | 0,600 D l'unité |
| autres vins classés, bouteille de 0,501 à 0,750 l | 0,900 D l'unité |
| autres vins classés, bouteille de 0,751 à 1 l | 1,200 D l'unité |

**Annexe III. Alcools et boissons alcoolisées.**

| Position | Produit | Droit |
|---|---|---|
| 22-05 | vermouths et autres vins aromatisés | 200 % |
| 22-06 | autres boissons fermentées (cidre, poiré, hydromel) | 25 % |
| 22-07 | alcools bruts, alcools éthyliques mauvais goût et dénaturés à usage ménager | 4,200 D/hl |
| 22-07 | alcools éthyliques bon goût dénaturés à usage pharmaceutique, de parfumerie et industriel | 10,500 D/hl |
| 22-07 | alcools éthyliques bon goût non dénaturés destinés aux boissons alcoolisées (hors vinaigres) | 380,000 D/hl |
| Ex 22-08 | préparations alcooliques composées pour boissons alcoolisées | 24,000 D/hl |
| Ex 22-08 | autres préparations alcooliques | 12,000 D/hl |
| Ex 22-08 | eaux-de-vie obtenues par distillation | 683 % |
| Ex 22-08 | whiskies, cognac, vodka, gin et autres spiritueux non classés | 648 % |
| Ex 22-08 | whiskies, cognac, vodka, gin et autres spiritueux classés | 395 % |
| Ex 22-08 | pastis, ricard, anisette et thibarine | 597 % |

Le décret n'indique pas l'assiette des taux en pourcentage ; c'est celle de la loi n° 88-62.

**Annexe IV. Capsule fiscale sur les vins.**

| Vins | Contenance | Catégorie | Tarif |
|---|---|---|---|
| vins de raisins frais | 0,001 à 0,375 l | « 1 » | 30 millimes |
| vins de raisins frais | 0,376 à 0,500 l | « 2 » | 40 millimes |
| vins de raisins frais | 0,501 à 0,750 l | « 3 » | 50 millimes |
| vins de raisins frais | 0,751 à 1 l | « 4 » | 60 millimes |
| vins de liqueur, mistelles, moûts à l'alcool | toute contenance | « 5 » | 70 millimes |
| vins mousseux | toute contenance | « 6 » | 80 millimes |

L'annexe IV arabe (p. 1377, « ملحق عدد IV ») donne les mêmes valeurs.

### Date d'effet du décret de 1997

- Pas de clause d'effet générale. Règle applicable depuis 1993 : exécutoire cinq jours après le
  dépôt au siège du gouvernorat de Tunis, jour du dépôt non compté (loi n° 93-64, art. 2).
- Les deux éditions se contredisent sur la date de dépôt :
  - **édition arabe**, JORT n° 59, dernière page : « تم إيداع هذا العدد من الرائد الرسمي للجمهورية
    التونسية بمقر ولاية تونس العاصمة يوم 30 جويلية 1997 » ;
  - **édition française**, p. 31 du fichier : « déposé au siège du gouvernorat de Tunis le
    24 juillet 1997 ».
- La date française est impossible : elle précède d'un jour la date du fascicule (25 juillet) et
  coïncide avec la date de signature. L'arabe est l'édition originale ; le français est une
  « traduction française pour information ». La date retenue est donc le **30 juillet 1997**, d'où
  un décret **exécutoire le 4 août 1997**. La note de la référence doit mentionner l'écart entre
  les deux éditions.
- Pour la capsule, l'application dépend de l'avis aux embouteilleurs (art. 44), dont la date
  n'est pas établie.

## 3. Décret gouvernemental n° 2015-1768 du 10 novembre 2015

FR p. 2721 (corps) et p. 2722 (annexe), couche texte native ; valeur de la ligne 22-07 « mauvais
goût » contrôlée à l'image. AR p. 3173-3174.

- **Visas** : Constitution ; loi n° 87-2 (système harmonisé) ; code de la TVA, notamment la loi
  n° 2012-1 (LFC 2012) ; loi n° 88-62, notamment la loi n° 2011-7 (LF 2012) ; loi n° 88-145,
  art. 86 ; tarif des droits de douane (loi n° 89-113) ; décret n° 97-1368, « notamment par le
  décret n° 2013-929 du 4 février 2013 » ; décret présidentiel n° 2015-35 ; avis du tribunal
  administratif.
- **Art. 1er.** Dans l'art. 3 du décret n° 97-1368, l'expression « aux annexes I, II et III du
  présent décret » est remplacée par « à l'annexe du présent décret gouvernemental ».
- **Art. 2.** « Sont abrogées les annexes I, II et III du décret n° 97-1368 … et remplacées par
  l'annexe suivante ».
- **Art. 3.** Exécution (finances, industrie, commerce, agriculture). Signé le 10 novembre 2015
  par Habib Essid.

**Annexe (Nouveau)**, « Tarif du droit de consommation applicable aux vins, bières, alcools et
boissons alcoolisées » :

| Position | Produit | Droit |
|---|---|---|
| Ex 21-06 | préparations alcooliques composées (hors substances odoriférantes) pour boissons alcoolisées | 48,000 D/hl |
| Ex 21-06 | les mêmes, pour d'autres usages | 24,000 D/hl |
| 22-03 | bière classée | **0,018 D/centilitre** |
| Ex 22-04 | vins en vrac classés livrés aux embouteilleurs | 7,500 D/hl |
| Ex 22-04 | vins mousseux classés, bouteille ≤ 1 l | 24,000 D l'unité |
| Ex 22-04 | vins de liqueur, mistelles, moûts à l'alcool, bouteille ≤ 1 l | 3,750 D l'unité |
| Ex 22-04 | autres vins classés en bouteilles | **1,8 D/litre** |
| 22-05 | vermouths et autres vins aromatisés | **50 %** |
| 22-06 | autres boissons fermentées | 25 % |
| 22-07 | alcools bruts non dénaturés ≥ 80 % vol, mauvais goût, pour le compte de l'État | 16,000 D/hl |
| 22-07 | alcools bruts dénaturés, mauvais goût, destinés aux ménages | 16,000 D/hl |
| 22-07 | alcools éthyliques non dénaturés ≥ 80 % vol, bon goût, usages pharmaceutiques, de parfumerie et industriels, pour le compte de l'État | 16,000 D/hl |
| 22-07 | alcools éthyliques dénaturés, bon goût, mêmes usages | 16,000 D/hl |
| 22-07 | alcools éthyliques non dénaturés, bon goût, destinés aux boissons alcoolisées | 570,000 D/hl |
| Ex 22-08 | eaux-de-vie obtenues par distillation | **50 %** |
| Ex 22-08 | whiskies, cognac, vodka, gin et autres spiritueux | **50 %** |
| Ex 22-08 | pastis, ricard, anisette et thibarine | **50 %** |
| Ex 33-02 | préparations alcooliques composées pour boissons alcoolisées | 48,000 D/hl |
| Ex 33-02 | autres préparations alcooliques composées | 24,000 D/hl |

La distinction entre spiritueux classés et non classés disparaît.

**Date d'effet.** Pas de clause d'effet. Fascicule déposé le **19 novembre 2015** (même date dans
les colophons FR et AR), d'où un décret **exécutoire le 24 novembre 2015**.

## 4. Chaîne complète : ce que fait chaque modificatif (lu sur pièce)

| Texte | JORT (FR ; AR) | Dépôt (FR = AR) | Exécutoire | Contenu |
|---|---|---|---|---|
| décret n° 93-2090 du 11 octobre 1993 (antécédent, abrogé par l'art. 45 de 97-1368) | n° 80 du 22 octobre 1993, p. 1818-1819 (FR) | non lu | non établi | un tableau unique de droit de consommation **et** de TVA pour 22-03 à 22-08. Valeurs (lues à l'image, libellés des lignes par OCR) : bières 370 %, TVA 17 % ; vin en vrac aux embouteilleurs 5 D/hl ; vin en bouteilles 0,435 / 0,650 / 0,870 / 1,300 D l'unité ; vins importés 200 % ; 22-05 200 % ; 22-06 25 % ; alcools 10,480 / 4,192 / 380 / 4,192 D/hl ; préparations 24 et 12 D/hl ; spiritueux 683 / 648 / 395 / 597 %, TVA 29 % |
| **décret n° 97-1368** | n° 59 du 25 juillet 1997, p. 1301-1316 ; AR p. 1362-1377 | 30 juillet 1997 (AR) ; « 24 juillet » (FR, erroné) | **4 août 1997** | voir § 2 |
| décret n° 2002-627 du 26 mars 2002 | n° 27 du 2 avril 2002, p. 833-834 | 4 avril 2002 | **9 avril 2002** | art. 1er : TVA de l'art. 1er portée de 17 % à **18 %** ; art. 2 : redevables, « les producteurs du vin en vrac et les embouteilleurs de vins » ; art. 3 : nouvel art. 43 *bis*, **affectation** de 1 400 000 D par an, prélevés sur le droit de consommation 22-03 à 22-08, au fonds de développement de la compétitivité dans le secteur de l'agriculture et de la pêche, et nouvel art. 43 *ter*, **50 %** des recettes de la capsule au fonds de concours « prêts sur gage » ; art. 4 : déclaration des producteurs au 31 décembre ; art. 5 : annexe III, 22-07, cinq lignes (4,200 / 4,200 / 10,500 / 10,500 / 380,000 D/hl), 22-05, 22-06 et 22-08 « sans changement ». Vise le décret n° 2001-1183 portant dissolution de l'office national de la vigne |
| décret n° 2007-1977 du 30 juillet 2007 | n° 63 du 7 août 2007, p. 2712-2713 | 8 août 2007 | **13 août 2007** | art. 1er : nouvel art. 24, alambics soumis à un cahier des charges ; art. 2 : **annexe IV**, capsule portée à 60 / 80 / 100 / 120 / 140 / 160 millimes ; art. 3 : art. 43 *ter*, affectation portée à **75 %** des recettes de la capsule |
| décret n° 2013-929 du 4 février 2013 | n° 14 du 15 février 2013, p. 673-675 | 16 février 2013 | **21 février 2013** | art. 1er : annexes I-III. **Bières** : 0,270 / 0,730 / 0,730 / 0,870 / 1,020 / 1,140 / 2,040 D l'unité ; pression 1,330 D/l ; vrac 1,040 D/l. **Vins** : vrac 7,500 D/hl ; mousseux 24,000 D ; liqueur 3,750 D ; bouteilles 0,675 / 0,900 / 1,350 / 1,800 D l'unité. **Alcools** : Ex 21-06 et Ex 33-02, 48 et 24 D/hl ; 22-07, 6,000 / 6,000 / 16,000 / 16,000 / 570,000 D/hl ; 22-05, 22-06 et Ex 22-08 « (Sans modification) ». Art. 2 : « eaux-de-vie » ajouté à l'art. 1er et **suppression du deuxième paragraphe de l'art. 1er** (TVA à 29 %) |
| **décret gouv. n° 2015-1768** | n° 92 du 17 novembre 2015, p. 2721-2722 ; AR p. 3173-3174 | 19 novembre 2015 | **24 novembre 2015** | voir § 3 |
| **décret prés. n° 2022-545 du 17 juin 2022** | n° 71 du 24 juin 2022, p. 1995-1996 ; AR p. 2109-2110 | 24 juin 2022 | **29 juin 2022** | art. 1er : **annexe IV** remplacée, capsule à 120 / 160 / 200 / 240 / 280 / 320 millimes ; art. 2 : publication. Vise le décret présidentiel n° 2021-117 (mesures exceptionnelles) et le décret-loi n° 2021-21 (LF 2022) |

Séries qui en découlent, de décret en décret :

| Paramètre | 1997 | 2002 | 2007 | 2013 | 2015 | 2022 |
|---|---|---|---|---|---|---|
| bière 0,661-1 l | 1,200 D l'unité | — | — | 2,040 D l'unité | 0,018 D/cl, soit 1,8 D/l | — |
| vin, bouteille de 0,751-1 l | 1,200 D l'unité | — | — | 1,800 D l'unité | 1,8 D/l | — |
| vin en vrac | 5 D/hl | — | — | 7,5 D/hl | 7,5 D/hl | — |
| alcool bon goût pour boissons | 380 D/hl | 380 D/hl | — | 570 D/hl | 570 D/hl | — |
| capsule, catégorie 3 | 50 millimes | — | 100 millimes | — | — | 200 millimes |

## 5. Ce que le volume dit déjà, et ce qui manque

**Ce qu'il dit** (`_droits_consommation.qmd`, l. 142-146, registre l. 288-300) : les références
des décrets n° 97-1368, 2002-627, 2007-1977, 2013-929 et 2015-1768 et leurs pages (sauf pour
2015-1768) ; la chaîne d'habilitation (LF 1989, art. 86) ; une date d'effet « non établie » sur
chaque ligne du registre.

**Ce qui manque ou est à corriger**
1. Les tarifs : annexes I-IV de 1997, valeurs de 2002, 2007, 2013, 2015 et 2022 (§ 2-4). Le
   registre peut désormais porter une colonne « avant → après ».
2. Les dates d'effet des six décrets (§ 4).
3. Le **décret présidentiel n° 2022-545** : absent du chapitre et de `references.json`.
4. Le contenu non tarifaire du décret de 1997 :
   - TVA propre aux boissons (17 % / 29 %, puis 18 % en 2002, et le 29 % supprimé en 2013) ;
   - capsule fiscale ;
   - régime d'entrepôt et de circulation (congé, acquit-à-caution) ;
   - comptabilité matière ;
   - contrôle permanent aux frais des fabricants ;
   - affectations de recettes (art. 43 *bis* et *ter*, 2002 et 2007).
5. L'**antécédent** : décret n° 93-2090 (1993) et, en amont, décret n° 91-551 (déjà au
   registre) ; décrets beylicaux du 20 novembre 1927 (régime des alcools) et du 21 mai 1931
   (impôt sur la vigne), visés en 1997.
6. **La rupture de 1997 pour la bière** : on passe d'un droit *ad valorem* de 370 % (1993) à un
   tarif spécifique par récipient. Celle de 2015 : passage à un tarif au volume (centilitre,
   litre).
7. Formulation à reprendre, l. 142 : « Seules leurs références sont connues ici : leurs tarifs et
   leurs dates d'effet ne sont pas établis ». AGENTS.md proscrit cette tournure, et le contenu est
   désormais établi. Même chose l. 146 (« aucun tarif n'est établi ») et pour les mentions « non
   établie » du registre (l. 288-300). Le TODO de la l. 144 peut être levé.
8. Point à signaler au rédacteur sans le trancher : l'habilitation de l'art. 86 de la LF 1989 vise
   « 22-03 et 22-05 à 22-09 » (citation du volume), sans le 22-04 (vins). Les décrets de 1993 et
   de 1997 fixent pourtant des tarifs pour Ex 22-04.

## 6. Références candidates (CSL-JSON)

### Existantes, à mettre à jour (`precis/fr/fiscalite/references.json`, et l'équivalent arabe)

```json
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
  "note": "Publié le 25 juillet 1997. Édition arabe p. 1362-1377 : https://www.pist.tn/jort/1997/1997A/Ja05997.pdf. Lu sur pièce le 23 octobre 2026 : p. 1301 en couche texte ; p. 1303-1316 par OCR, montants contrôlés à l'image ; p. 1302 (art. 1er-5) illisible dans l'édition française (local et pist.tn, même SHA-256), lue dans l'édition arabe p. 1363-1364. Pas de clause d'effet générale. Dépôt au gouvernorat de Tunis : 30 juillet 1997 selon le colophon arabe ; le colophon français porte « 24 juillet 1997 », date antérieure à la publication. Exécutoire le 4 août 1997 (loi n° 93-64, art. 2). Art. 44 : capsule applicable dix jours après l'avis aux embouteilleurs. Pris sur le fondement de l'art. 86 de la loi n° 88-145 ; abroge le décret n° 93-2090 (art. 45). Annexes I-III remplacées par le décret gouvernemental n° 2015-1768 ; annexe IV remplacée par les décrets n° 2007-1977 et 2022-545.",
  "title-short": "Décret n° 97-1368 du 24 juillet 1997"
}
```

```json
{
  "id": "decret-gouv-2015-1768-annexes-alcools",
  "type": "legislation",
  "title": "Décret gouvernemental n° 2015-1768 du 10 novembre 2015, modifiant le décret n° 97-1368 du 24 juillet 1997, relatif au régime fiscal des produits relevant des numéros 22.03 à 22.08 du tarif des droits de douanes",
  "container-title": "Journal Officiel de la République Tunisienne",
  "issue": "92",
  "page": "2721-2722",
  "issued": {"date-parts": [[2015, 11, 10]]},
  "URL": "https://www.pist.tn/jort/2015/2015F/Jo0922015.pdf",
  "note": "Publié le 17 novembre 2015. Édition arabe p. 3173-3174 : https://www.pist.tn/jort/2015/2015A/Ja0922015.pdf. Lu sur pièce (couche texte) le 23 octobre 2026. Art. 1er : renvoi de l'art. 3 du décret n° 97-1368 à « l'annexe du présent décret gouvernemental » ; art. 2 : annexes I, II et III abrogées et remplacées par une annexe unique. Pas de clause d'effet ; fascicule déposé le 19 novembre 2015 (FR et AR) ; exécutoire le 24 novembre 2015 (loi n° 93-64, art. 2).",
  "title-short": "Décret gouvernemental n° 2015-1768 du 10 novembre 2015"
}
```

Mises à jour analogues pour `decret-2002-627-alcools` (dépôt le 4 avril 2002, exécutoire le
9 avril 2002), `decret-2007-1977-alcools` (dépôt le 8 août 2007, exécutoire le 13 août 2007) et
`decret-2013-929-alcools` (dépôt le 16 février 2013, exécutoire le 21 février 2013). La mention
« valeurs non établies » est à retirer de chacune.

### À créer

```json
{
  "id": "decret-pres-2022-545-capsule-vins",
  "type": "legislation",
  "title": "Décret Présidentiel n° 2022-545 du 17 juin 2022, portant modification du décret n° 97-1368 du 24 juillet 1997, relatif au régime fiscal des produits relevant des numéros 22-03 à 22-08 du tarif des droits de douane",
  "container-title": "Journal Officiel de la République Tunisienne",
  "issue": "71",
  "page": "1995-1996",
  "issued": {"date-parts": [[2022, 6, 17]]},
  "URL": "https://www.pist.tn/jort/2022/2022F/Jo0712022.pdf",
  "note": "Publié le 24 juin 2022. Édition arabe : p. 2109-2110 : https://www.pist.tn/jort/2022/2022A/Ja0712022.pdf (HTTP 200, 23 octobre 2026). Lu sur pièce (couche texte) le 23 octobre 2026. Art. 1er : annexe IV du décret n° 97-1368 abrogée et remplacée ; tarif de la capsule fiscale sur les vins de 120, 160, 200, 240, 280 et 320 millimes (catégories 1 à 6). Pas de clause d'effet ; fascicule déposé le 24 juin 2022 (FR et AR) ; exécutoire le 29 juin 2022 (loi n° 93-64, art. 2). Notice jort_cache recid 168695.",
  "title-short": "Décret Présidentiel n° 2022-545 du 17 juin 2022"
}
```

```json
{
  "id": "decret-93-2090-alcools",
  "type": "legislation",
  "title": "Décret n° 93-2090 du 11 octobre 1993, portant fixation des taux du droit de consommation et de la taxe sur la valeur ajoutée sur les alcools, boissons alcoolisées, vins et bières",
  "container-title": "Journal Officiel de la République Tunisienne",
  "issue": "80",
  "page": "1818-1819",
  "issued": {"date-parts": [[1993, 10, 11]]},
  "URL": "https://www.pist.tn/jort/1993/1993F/Jo08093.pdf",
  "note": "Publié le 22 octobre 1993. Fascicule sans couche texte ; lu par OCR le 23 octobre 2026, colonne des taux contrôlée à l'image (p. 1818), libellés des lignes par OCR. Date de dépôt non lue. Abrogé par l'art. 45 du décret n° 97-1368. Notice jort_cache recid 91746. URL pist.tn vérifiée (HTTP 200, 23 octobre 2026).",
  "title-short": "Décret n° 93-2090 du 11 octobre 1993"
}
```

## 7. Notions à glossaire (`precis/glossaire.yml`)

Aucune n'existe aujourd'hui ; `droit-de-consommation` et `taxe-bieres-vins-boissons-alcoolisees`
existent.

| id proposé | FR | AR (lu dans l'édition arabe de 1997) | Source canonique |
|---|---|---|---|
| `capsule-fiscale-vins` | capsule fiscale sur les vins | العلامة الجبائية على الخمور | décret n° 97-1368, art. 6-8 et annexe IV |
| `acquit-a-caution` | acquit-à-caution | à relever (AR art. 31, p. 1371 environ, en image) | décret n° 97-1368, art. 31 |
| `conge-circulation` | congé (titre de mouvement, droit acquitté) | à relever (même article) | décret n° 97-1368, art. 31 |
| `comptabilite-matiere` | registre de comptabilité matière | à relever | décret n° 97-1368, art. 12, 15 et 27 |
| `entrepositaire-alcools` | entrepositaire d'alcools | à relever | décret n° 97-1368, art. 19 et 21 |
| `biere-vin-classe` | bière, vin « classés » (opposés aux produits non classés, tarif doublé) | الجعة والخمور المصنفة / غير المصنفة (AR art. 3 et 5, p. 1363) | décret n° 97-1368, art. 3 et 5 |

## 8. Lacunes

- **Coexistence des décrets et des lois de finances.** La LF 2016 (loi n° 2015-53, art. 44-45)
  et la LF 2018 (loi n° 2017-66, art. 45) « abroge[nt] et remplace[nt] le tableau en entier » de
  la loi n° 88-62. La LF 2021 (loi n° 2020-46, art. 20-22) révise les taux de la bière et des vins
  (registre du volume). Il reste à établir si ces lois reprennent les tarifs des positions 22-03 à
  22-08, et donc si l'annexe de 2015 est encore le tarif en vigueur au 1er janvier 2026. Textes
  dans le corpus (couche texte). C'est le point principal avant d'écrire un « état du droit ».
- **Taux *ad valorem* entre 1997 et 2015.** Le décret n° 2013-929 laisse 22-05, 22-06 et Ex 22-08
  « sans modification ». Ces textes ne disent pas si une loi a modifié ces taux entre 1997 et 2015
  ; la loi n° 2006-80 a pour intitulé « imposition de certains produits au droit de consommation ».
  Le passage de 200 % à 50 % (vermouths) ou de 683 % à 50 % (eaux-de-vie) n'est donc établi
  qu'**entre annexes de décrets**, pas comme l'état de la veille de 2015.
- **TVA des boissons après 2007.** L'art. 1er, § 2 (29 %) est devenu sans objet avec la loi
  n° 2006-80 (suppression du taux majoré) et n'est formellement supprimé qu'en 2013. Le taux de
  l'art. 1er, 18 % depuis 2002, n'a pas été suivi dans les réformes de taux de la TVA (19 % depuis
  2018). À rapprocher du chapitre TVA.
- **Antécédent de 1993** : date de dépôt du JORT n° 80 de 1993 non lue ; libellés des lignes du
  tableau lus par OCR (colonne gauche du tableau non contrôlée à l'image).
- **Contexte de 1997** : le décret n'a pas d'exposé des motifs. Le contexte est à chercher dans
  les débats ou rapports de l'époque (budget 1997, IXe plan), non consultés.
- **Date d'application de la capsule de 1997** : elle dépend de l'avis de l'administration
  (art. 44) ; aucune source.
- Termes arabes *acquit-à-caution*, *congé*, *comptabilité matière*, *entrepositaire* : à relever
  aux pages en image de l'édition arabe de 1997 (p. 1369-1373 environ).

## 9. Recherches infructueuses

Aucun texte attendu n'est resté introuvable. Une fiche est proposée pour rendre rejouable la
vérification « pas d'autre modificatif que les cinq décrets » ; elle ne contient que ce qui a été
fait.

```yaml
- id: r-modificatifs-decret-97-1368
  objet: Textes modifiant le décret n° 97-1368 du 24 juillet 1997 (régime fiscal des produits 22-03 à 22-08)
  ou: JORT 1997-2026, éditions FR et AR
  requetes:
    titres_like: ["%97-1368%", "%1368%1997%", "%22-03 a 22-08%", "%22.03 a 22.08%", "%22.3 a 22.8%"]
    iort_ar: ["%1368 لسنة 1997%"]
    plein_texte: ["97-1368", "97 - 1368", "1368 لسنة 1997", "1368.*1997"]
  passes:
    - date: 2026-10-23
      resultat: decret-pres-2022-545-capsule-vins
      couverture: >
        Notices jort_cache (titre et objet) 1956-2026 ; plein texte des fascicules locaux 2016-2026,
        FR et AR, couche texte seulement (fascicules scannés non parcourus). Trouvés : 2002-627,
        2007-1977, 2013-929, 2015-1768, 2022-545. Rien après le JORT n° 71 de 2022.
      couvert_jusqu_au: 2026-10-02
      sources: [jort_cache, corpus_local]
```

La date `couvert_jusqu_au` reprend celle de la dernière publication indexée relevée dans
outillage-sources § 1 g ; à recaler sur le dernier fascicule du corpus local avant
d'enregistrer la fiche par `scripts/recherches.py`.
