# Contribution sociale de solidarité (CSS) — vérification sur le *Journal officiel*

Note documentaliste, 4 octobre 2026. Lecture seule : aucun fichier des dépôts n'a été modifié.

Sources lues : le corpus JORT local (`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`), les extraits
de lois de finances (`PDFs/Lois_de_Finances/`), les notes communes de la DGELF
(`PDFs/Notes_Communes/`), plus `jort_cache.db` pour les métadonnées. J'ai vérifié sur pist.tn
quelles éditions françaises existent.

**Pagination.** Au JORT, le numéro de page est imprimé **en pied de page**. Avec `pdftotext`, la
ligne « Page N » vient donc *après* le contenu de la page N. Chaque page citée ci-dessous a été
contrôlée page par page (`pdftotext -f p -l p`), et les pages clés ont été rendues en image.

**Citations arabes.** Celles de la LF 2023 (art. 22) et de la LF 2026 (art. 87) ont été relues sur
l'image de la page. Les autres sont des extractions dont j'ai corrigé à la main l'ordre des chiffres
et de la ponctuation.

---

## 1. Chronologie datée et sourcée (2018 → 4 octobre 2026)

### 1.1 Personnes physiques

| # | Texte | Disposition | Effet (règle « Dater ») |
|---|---|---|---|
| 1 | **LF 2018** : loi n° 2017-66 du 18 déc. 2017, art. 53. JORT n° 101 du 19 déc. 2017. FR p. 4289, AR p. 4287. [FR](https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf), [AR](https://www.pist.tn/jort/2017/2017A/Ja1012017.pdf) | Création de la CSS au profit des caisses sociales. Pour les personnes physiques, elle est égale à l'impôt calculé sur le barème de l'art. 44 **majoré d'un point sur chaque taux de tranche**, moins l'impôt calculé sur le barème non majoré. Aucun minimum. | Date énoncée par le texte (§ 4) : « revenus et bénéfices réalisés à partir du 1er janvier 2018 » → **2018-01-01** |
| 2 | **LF 2020** : loi n° 2019-78 du 23 déc. 2019, art. 39 § 1 et § 4. JORT n° 104 du 27 déc. 2019. AR p. 4708 ([AR](https://www.pist.tn/jort/2019/2019A/Ja1042019.pdf)). L'édition FR de ce numéro répond 404 sur pist.tn ; l'extrait FR local `Loi_n_2019-78_….pdf` place l'article p. 4435 | **Dispense permanente.** La CSS ne s'applique pas aux personnes qui réalisent *exclusivement* des revenus de l'art. 25 du code (traitements, salaires, pensions, rentes viagères) et dont le revenu annuel net ne dépasse pas **5 000 D** après les **seules** déductions de l'art. 40 (situation et charges de famille). | L'art. 39 § 1 n'a pas de clause d'effet. Le § 4 interdit toute restitution des sommes payées « avant le 1er janvier 2020 », et la NC 28/2019 l'applique aux salaires et pensions « payés à partir du 1er janvier 2020 ». La date exécutoire n'est pas établie ici : la règle de la loi 93-64 la fixe à cinq jours après le dépôt du JORT n° 104 au gouvernorat de Tunis, et la date de ce dépôt est inconnue. → **2020-01-01** (voir les questions ouvertes) |
| 3 | **LF 2023** : décret-loi n° 2022-79 du 22 déc. 2022, art. 22 § 2. JORT n° 141 du 23 déc. 2022, AR pp. 4062-4063 (§ 2 p. 4063). [AR](https://www.pist.tn/jort/2022/2022A/Ja1412022.pdf). Pas d'édition FR : 404 sur pist.tn, et l'extrait local `Loi_de_Finances_2023.pdf` est tronqué et illisible | Ajoute un **§ 7** à l'art. 53 : la majoration passe à **un demi-point** de chaque taux de tranche. Le § 7 reprend la dispense de 5 000 D en termes identiques, parce qu'il s'applique « nonobstant » le premier tiret du § 2. | « revenus … dont le délai de déclaration intervient au cours des années 2023, 2024 et 2025 » (voir 1.3) |
| 4 | LF 2024 : loi n° 2023-13 du 11 déc. 2023. JORT n° 144 du 12 déc. 2023 (AR à partir de la p. 6437) | **Ne touche pas la CSS.** Aucune occurrence dans le fascicule AR ni dans l'extrait FR local. | — |
| 5 | **LF 2025** : loi n° 2024-48 du 9 déc. 2024. JORT n° 149 du 10 déc. 2024. AR p. 6428 (art. 36) et p. 6430 (art. 37). L'édition FR répond 404 sur pist.tn ; l'extrait FR local donne p. 3432 pour l'art. 37 | **Ne touche pas le § 7.** L'art. 36 remplace le barème de l'art. 44 pour les revenus réalisés à partir du 1er janvier 2025 (0 % jusqu'à 5 000 D, puis 15, 25, 30, 33, 36, 38 et 40 %) : la CSS change donc *mécaniquement*, puisqu'elle s'adosse au barème. L'art. 37 § 10-11 ne concerne que les sociétés (voir 1.2). **Aucune disposition de « maintien à 0,5 % »** dans ce texte. | — |
| 6 | **LF 2026** : loi n° 2025-17 du 12 déc. 2025, art. 87 § 2. JORT n° 148 du 12 déc. 2025. Art. 87 et § 1 p. 4253, § 2 p. 4254 ([AR](https://www.pist.tn/jort/2025/2025A/Ja1482025.pdf)). L'URL FR `2025F/Jo1482025.pdf` sert le fascicule **arabe** : la copie locale `fr/Jo1482025.pdf` est identique octet pour octet (`cmp`) à `ar/Ja1482025.pdf`. Il n'y a pas d'édition FR | **Prorogation d'un an.** Le délai d'application du § 7 devient « de 2023 à 2026 ». | Revenus dont la déclaration échoit de 2023 à 2026 |

Autres occurrences, hors de la majoration :

- **Décret-loi n° 2020-30** du 10 juin 2020, art. 1er § 3, al. 2. JORT n° 54 du 10 juin 2020, AR
  p. 1408. Le complément différentiel qui porte à 180 D les petites pensions CNSS/CNRPS n'est
  soumis ni à la retenue d'assurance maladie ni à la CSS.
- **Décret-loi n° 2021-21** (LF 2022), art. 12 : ouverture du « compte de diversification des
  sources de sécurité sociale », alimenté par la CSS. JORT n° 119 du 28 déc. 2021, FR p. 3082. Ce
  texte ne modifie pas le calcul.

### 1.2 Sociétés (pour mémoire : c'est le second sujet du modèle)

- **LF 2018, art. 53 § 2.** Majoration d'un point du taux de l'IS, avec un minimum de 300 D (taux
  de 35 %), 200 D (25, 20 ou 15 %) ou 100 D (10 %). Montant fixe de 200 D pour les sociétés
  totalement exonérées.
- **LF 2019, art. 87-88.** Contribution exceptionnelle de 1 % sur le chiffre d'affaires des
  banques, assurances, télécoms et pétroliers, au profit des caisses. Ce n'est **pas la CSS**.
  L'art. 88 la reporte au 1er janvier 2020, puis l'art. 39 § 5 de la LF 2020 l'abroge.
- **LF 2020, art. 39 § 2.** Nouveau § 5 de l'art. 53 : **+3 points** (minimum 300 D) pour les
  banques, établissements financiers et assurances, **+2 points** (minimum 300 D) pour les autres
  sociétés à 35 %. S'applique aux bénéfices dont la déclaration échoit en 2020, 2021 et 2022.
- **LF 2020, art. 39 § 3.** Ajoute « ou 13,5 % » au palier de 100 D.
- **LF 2021** (loi n° 2020-46), art. 14 § 21-22, JORT n° 128 du 25 déc. 2020, FR p. 3128.
  Suppression de « 25 %, » au palier de 200 D et de « ou 13.5% » au palier de 100 D. S'applique
  aux bénéfices réalisés à partir du 1er janvier 2021 (§ 28).
- **LF 2023, art. 22.**
  - § 1 (nouveau § 6) : **+4 points** (minimum 500 D) pour les sociétés à 35 % visées à
    l'art. 49 ; **+3 points** pour celles imposées à 20, 15 ou 10 % (minimum 400 D à 20 ou 15 %,
    200 D à 10 %). Déclarations 2023-2025.
  - § 3 et § 4 : relèvement **permanent** des minima, de 300/200/100 D à 500/400/200 D, et du
    montant fixe des sociétés exonérées de 200 à 400 D. Bénéfices déclarés « à partir de 2023 »
    (§ 5).
- **LF 2025, art. 37 § 10-11.** Le taux de 40 % entre dans le premier palier du minimum (300 D en 2018, 500 D depuis la LF 2023) et dans le § 6
  (+4 points, minimum 500 D). Bénéfices réalisés à partir du 1er janvier 2024 (§ 16).
- **LF 2026, art. 87 § 1.** Le § 6 est prorogé aux déclarations « de 2023 à 2026 ».

### 1.3 Ce que les textes disent exactement, et la lecture de l'administration

**LF 2023, art. 22 § 2** (AR p. 4063, relu sur l'image) :

> 2) تضاف إلى الفصل 53 من القانون عدد 66 لسنة 2017 المؤرخ في 18 ديسمبر 2017 المتعلق بقانون المالية لسنة 2018 كما تم تنقيحه وإتمامه بالنصوص اللاحقة، فقرة 7 فيما يلي نصها:
> 7) بالنسبة إلى الأشخاص الطبيعيين، تساوي المساهمة الاجتماعية التضامنية الفارق بين الضريبة على الدخل المحتسبة على أساس جدول الضريبة على الدخل المنصوص عليه بالفصل 44 من مجلة الضريبة على دخل الأشخاص الطبيعيين والضريبة على الشركات بإضافة نصف نقطة لنسب الضريبة المعتمدة على مستوى شرائح الدخل الواردة بالجدول المذكور والضريبة على الدخل المحتسبة على أساس جدول الضريبة المذكور دون إضافة نصف نقطة إلى نسب الضريبة.
> ولا تطبق المساهمة الاجتماعية التضامنية على الأشخاص الطبيعيين الذين يحققون المداخيل المنصوص عليها بالفصل 25 من مجلة الضريبة على دخل الأشخاص الطبيعيين والضريبة على الشركات دون سواها والذين لا يتجاوز دخلهم السنوي الصافي 5000 دينار بعد طرح التخفيضات بعنوان الحالة والأعباء العائلية المنصوص عليها بالفصل 40 من المجلة المذكورة فحسب.
> تطبق أحكام هذه الفقرة على المداخيل المعتمدة لاحتساب الضريبة على الدخل التي يحلّ أجل التصريح بها خلال السنوات 2023 و2024 و2025 وذلك بصرف النظر عن أحكام المطة الأولى من الفقرة 2 من هذا الفصل.

Il n'existe pas d'édition française officielle. Voici la formulation de l'administration
(**NC 1/2023**, DGELF), qui n'est pas une traduction officielle : « *ladite contribution est égale
à la différence entre l'impôt sur le revenu déterminé sur la base du barème […] en majorant d'un
demi-point les taux d'imposition applicables aux tranches de revenu prévus par ce barème et l'impôt
sur le revenu déterminé sur la base dudit barème d'impôt sans la majoration d'un demi-point* ».

Sur la dispense, la même note est explicite : « *aucune modification n'a été apportée à
l'exonération de la contribution sociale de solidarité pour les personnes physiques qui réalisent
exclusivement des revenus dans la catégorie traitements, salaires, pensions et rentes viagères et
dont le revenu annuel net ne dépasse pas 5.000 dinars* ».

**LF 2020, art. 39 § 1** (FR, extrait local p. 4435 ; AR p. 4708) : « *Est ajouté aux dispositions
du premier tiret du paragraphe 2 de l'article 53 […] ce qui suit : La contribution sociale de
solidarité ne s'applique pas aux personnes physiques qui réalisent exclusivement les revenus prévus
à l'article 25 du code […] et dont le revenu annuel net ne dépasse pas 5000 dinars après déduction
des abattements au titre de la situation et charges de famille prévus à l'article 40 dudit code
uniquement.* » Le § 4 ajoute : « *L'application des dispositions du paragraphe 1 du présent article
ne peut pas entraîner la restitution des montants payés au titre de la contribution sociale de
solidarité avant le 1er janvier 2020.* »

**LF 2026, art. 87 § 2** (AR p. 4254, relu sur l'image) :

> 2) تنقّح أحكام الفقرة الثالثة من الفقرة 7 من الفصل 53 من القانون عدد 66 لسنة 2017 المؤرخ في 18 ديسمبر 2017 المتعلق بقانون المالية لسنة 2018 كما يلي:
> تطبق أحكام هذه الفقرة على المداخيل المعتمدة لاحتساب الضريبة على الدخل التي يحلّ أجل التصريح بها خلال السنوات من 2023 إلى 2026 وذلك بصرف النظر عن أحكام المطة الأولى من الفقرة 2 من هذا الفصل.

Le titre de l'article est « مواصلة تطبيق الأحكام الاستثنائية للمساهمة الاجتماعية التضامنية » (p. 4253).

**Deux lectures du déclencheur temporel.** Le texte rattache le demi-point à l'*année où échoit la
déclaration*. Les notes communes le rattachent, pour les salariés et pensionnés, à la *date de
paiement* du salaire :

- **NC 1/2023** : « *pour les salariés et les pensionnés : aux salaires et pensions payés à partir
  du 1er janvier 2023 jusqu'à la fin de l'année 2025* » ; pour les autres personnes physiques, aux
  revenus dont la déclaration échoit en 2023, 2024 et 2025.
- **NC 1/2026**, publiée en arabe seulement (fichier daté du 5 janvier 2026) : pour les salariés et
  pensionnés, « على الأجور والجرايات المدفوعة ابتداء من غرة جانفي 2026 إلى موفّى ديسمبر 2026 » ;
  pour les autres, aux revenus dont la déclaration échoit en 2026.

| Année de revenu | Lettre de la loi (déclaration l'année suivante) | Notes communes (salaires et pensions retenus à la source) |
|---|---|---|
| 2018 – 2021 | 1 point | 1 point |
| 2022 | **½ point** (déclaré en 2023) | 1 point (payé en 2022) |
| 2023 – 2025 | ½ point | ½ point |
| 2026 | **1 point** (déclaré en 2027, hors du délai prorogé) | **½ point** (payé en 2026) |
| 2027 – | 1 point, sauf nouvelle prorogation | 1 point, sauf nouvelle prorogation |

Je ne tranche pas entre les deux lectures. Pour les salariés, c'est celle des notes communes qui
s'applique en pratique à la retenue à la source.

---

## 2. Verdict sur l'énoncé du volume « Les caisses de sécurité sociale »

Fichier : `precis/fr/caisses/_etat_caisses.qmd`, l. 31.

| Fragment | Verdict |
|---|---|
| Création, redevables, revenus réalisés à partir du 1er janvier 2018, définition en points [@lf-2018, art. 53] | **Exact.** |
| « La loi de finances pour 2023 ramène cette majoration à un demi-point pour les revenus dont la déclaration échoit en 2023, 2024 et 2025 » | **Exact** à la lettre (art. 22 § 2, AR p. 4063). |
| « … et en dispense, pour ces mêmes années, les personnes qui ne perçoivent que des revenus de l'article 25 … n'excède pas 5 000 dinars » [@lf-2023, art. 22] | **À corriger.** La dispense date de la **LF 2020, art. 39 § 1**. Elle est permanente depuis les salaires payés en 2020, et la LF 2023 ne fait que la reprendre dans son régime temporaire. Écrite ainsi, la phrase laisse croire que la dispense est née en 2023 et cesse avec le régime. |
| « le même article modifie aussi, pour certaines sociétés, le calcul de la contribution, et relève ses minima » | **Exact** (§ 1, § 3 et § 4). |
| « ce qui vaut au-delà n'est pas établi ici » | **Dépassé.** La LF 2026, art. 87 § 2, proroge le demi-point aux déclarations échéant en 2026. |

Le TODO des l. 33-36 est lui aussi à refaire. La LF 2025 ne « maintient » rien : elle ne touche pas
le § 7. C'est la LF 2026 qui proroge.

**Texte proposé**, en remplacement de la phrase « La loi de finances pour 2023 ramène … n'est pas
établi ici. » :

> Depuis la loi de finances pour 2020, la contribution ne s'applique pas aux personnes qui ne perçoivent que des revenus de l'article 25 du code de l'impôt sur le revenu — traitements, salaires, pensions et rentes viagères — et dont le revenu annuel net, après les seules déductions pour situation et charges de famille, n'excède pas 5 000 dinars [@lf-2020, art. 39]. La loi de finances pour 2023 ramène la majoration à un demi-point pour les revenus dont la déclaration échoit en 2023, 2024 et 2025, en reprenant la même dispense ; le même article modifie aussi, pour certaines sociétés, le calcul de la contribution, et relève ses minima [@lf-2023, art. 22]. La loi de finances pour 2026 étend le demi-point aux revenus dont la déclaration échoit en 2026 [@lf-2026, art. 87]. La majoration est donc d'un point sur les revenus réalisés à partir de 2018, puis d'un demi-point sur ceux dont la déclaration échoit de 2023 à 2026 ; à défaut d'une nouvelle prorogation, le point entier vaut de nouveau pour les revenus déclarés à partir de 2027.

Note pour le rédacteur : cette formulation garde volontairement les termes de la loi (année d'échéance de la déclaration) sans les convertir en années de revenu. Le texte et `tbl-css-salarie`, qui affiche 1 % jusqu'au 1er janvier 2023, ne s'accorderont qu'une fois tranchée la question de date (voir 1.3 et 3).

Pour les salariés, on peut ajouter une phrase sur la lecture administrative : retenue à la source
au demi-point sur les salaires et pensions payés du 1er janvier 2023 au 31 décembre 2026 (notes
communes 1/2023 et 1/2026). Il faudrait alors verser ces notes en références.

Deux autres endroits portent la même erreur :

- **`precis/fr/remunerations_publiques/_regime_indiciaire.qmd`, l. 200** : « en dispense les seuls
  salariés et pensionnés … [@lf-2023, art. 22] ». Même correction : la dispense vient de
  [@lf-2020, art. 39], et la LF 2026 prolonge le demi-point. Le TODO de la l. 202 (« ne vaut que
  pour les revenus déclarés en 2023-2025 ») est dépassé : c'est « 2023-2026 ».
- **`docs/notes/backlog-modele.md`, l. 23** attribue la dispense à la LF 2023 ; **la l. 22**
  cherche dans la loi n° 2024-48 un article qui n'existe pas. **Q10** de
  `docs/notes/fiscalite-irpp-besoins-documentation.md` suppose de même un « maintien par la
  LF 2025 ». Ces trois points sont à mettre à jour.

---

## 3. Verdict sur `tbl-css-salarie` et les paramètres d'openfisca-tunisia

Le tableau engendré (`precis/fr/remunerations_publiques/tables/css_salarie.md`) dit :
1 % au 1er janvier 2018 [@lf-2018, art. 53], puis 0,5 % au 1er janvier 2023 [@lf-2023, art. 22].
La ligne 2025 est écartée par l'option `sans_maintien`.

Il lit `openfisca_tunisia/parameters/prelevements_sociaux/contribution_sociale_solidarite/salarie.yaml`.
Ce fichier est un barème à une tranche (seuil 0) qui vaut 0,01 en 2018, 0,005 en 2023 et 0,005 en
2025 ; il est ajouté au barème de l'IR. J'ai lu le dépôt local, à jour de `origin/master` (e8548797).

**Ce qui est juste**

- **Les valeurs 1 et ½.** Elles sont justes **comme majorations en points de chaque taux de
  tranche**, y compris la tranche à 0 %. C'est bien ce que fait l'addition du barème. La NC 1/2026
  le dit d'ailleurs : « إلى 0.5% من المداخيل ».
- **Pas de taux minimal pour les personnes physiques.** Ni le texte de 2018 ni ses modifications
  n'en prévoient. Les minima ne visent que les sociétés.
- **La date 2018-01-01.**

**Ce qui est faux ou incomplet**

1. **Le libellé.** « Taux applicable aux salariés » est inexact. La CSS des personnes physiques
   vise tous les revenus soumis au barème de l'art. 44, pas les seuls salariés. Et ce n'est pas un
   taux sur une assiette : c'est **une majoration en points de chaque taux du barème de l'IRPP**.
   Proposition : « Contribution sociale de solidarité des personnes physiques : majoration (en
   points) de chaque taux du barème de l'impôt sur le revenu ».
2. **La date du demi-point (2023-01-01).** Elle ne correspond qu'à la lecture des notes communes,
   c'est-à-dire aux salaires payés à partir de janvier 2023. À la lettre de la loi, le demi-point
   vaut pour les **revenus de 2022**, déclarés en 2023 (voir 1.3). La référence « article 22 – tiret
   7 » est imprécise : c'est l'art. 22 § 2, qui crée le § 7 de l'art. 53.
3. **La ligne 2025-01-01, sourcée « LF 2025 (maintien) » sur finances.gov.tn.** La source est
   fausse : la loi n° 2024-48 n'a pas de disposition sur la CSS des personnes physiques. La valeur
   0,005 reste juste pour les revenus de 2025 (déclarés en 2026), mais en vertu de la **LF 2026,
   art. 87 § 2**. Sous la lecture « date de paiement », cette ligne est simplement redondante.
4. **La fin du régime manque.** Rien ne marque le retour au point entier. Selon la lecture, ce
   retour vaut pour les revenus de 2026 (lettre de la loi : 2026-01-01 → 0,01) ou pour les
   salaires payés à partir du 1er janvier 2027 (notes communes : 2027-01-01 → 0,01). Le paramètre
   prolonge aujourd'hui 0,005 indéfiniment, ce qu'aucun texte ne dit.
5. **Le seuil de dispense n'est pas un paramètre.** La formule le dérive du barème : c'est le
   premier seuil à taux non nul. Or la loi le fixe **en toutes lettres à 5 000 D**, sans renvoi au
   barème. Le docstring dit le contraire du droit. Les deux valeurs coïncident aujourd'hui, mais un
   déplacement de la tranche à 0 % les séparerait.
6. **Les conditions de la dispense.**
   - Le texte exige des revenus de l'art. 25 « exclusivement », ce que la formule annuelle
     (foyer) ne vérifie pas.
   - Il mesure le revenu net « après les seules » déductions de l'art. 40, alors que la formule
     annuelle compare le revenu net imposable, après toutes les déductions.
   - La formule de la retenue est plus proche du texte.
7. **Les références.** Le fichier pointe vers GitLab (`tunisia-legislative-references`) et vers
   jibaya.tn pour des notes communes, et vers legislation.tn dans `index.yaml` et les barèmes des
   sociétés. Il faut les remplacer par pist.tn. Les éditions FR de 2019/104, 2022/141, 2023/144 et
   2024/149 manquent sur pist.tn, et 2025/148 sert l'arabe : il faut donc l'URL arabe.

**Côté sociétés**, à traiter dans une issue séparée (« une PR, un sujet ») :

- `taux_is_35_pc` porte 0,02 en 2019 sans autre source que la LF 2018 : la vraie source est la
  LF 2020, art. 39 § 2. Les +3 points des banques et assurances (2019-2021) manquent.
- Aucun barème ne marque la fin du relèvement, pour les bénéfices déclarés après 2026.
- Les minima de 2023 sont datés 2023-01-01 alors que les barèmes du même article sont datés
  2022-01-01 : le § 5 vise les bénéfices déclarés à partir de 2023, donc les bénéfices de 2022.
- Le montant fixe des sociétés exonérées (200 puis 400 D) manque, comme le palier « 13,5 % »
  (2020) et la suppression de « 25 % » (2021).
- Le taux de 40 % (LF 2025, art. 37) manque.

**Valeurs proposées pour les personnes physiques** (à trancher par la revue ; aucune ne mentionne
de variable ni de formule) :

```yaml
# majoration en points de chaque taux du barème de l'art. 44 (lecture « année de déclaration »)
2018-01-01: 0.01    # LF 2018 art. 53 §2 et §4 — JORT n°101 du 19/12/2017, FR p.4289 / AR p.4287
2022-01-01: 0.005   # LF 2023 (décret-loi 2022-79) art. 22 §2 — JORT n°141 du 23/12/2022, AR p.4063
                    #   + prorogation LF 2026 (loi 2025-17) art. 87 §2 — JORT n°148 du 12/12/2025, AR p.4254
2026-01-01: 0.01    # fin du §7 : revenus déclarés en 2027 — art. 53 §2, premier tiret (LF 2018)
# variante « date de paiement » (NC 1/2023 et 1/2026) : 2023-01-01 → 0.005 ; 2027-01-01 → 0.01

# seuil de dispense, nouveau paramètre
2020-01-01: 5000    # LF 2020 (loi 2019-78) art. 39 §1 et §4 — JORT n°104 du 27/12/2019, AR p.4708
```

### Brouillon d'issue (openfisca-tunisia). NE PAS OUVRIR sans revue humaine

**Titre** : CSS des personnes physiques : demi-point prorogé par la LF 2026, ligne 2025 mal sourcée, seuil de dispense de 5 000 D en dur

**Corps** :

> Paramètre concerné : `prelevements_sociaux/contribution_sociale_solidarite/salarie.yaml`, avec la dispense des petits salaires et pensions.
>
> **Ce que disent les textes** (tous lus sur le JORT)
>
> | Texte | Disposition | JORT |
> |---|---|---|
> | Loi n° 2017-66 (LF 2018), art. 53 § 2 et § 4 | Majoration de **1 point** de chaque taux du barème de l'art. 44 ; revenus réalisés à partir du 1/1/2018 | n° 101 du 19/12/2017, FR p. 4289 (https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf), AR p. 4287 |
> | Loi n° 2019-78 (LF 2020), art. 39 § 1 et § 4 | Dispense **permanente** des personnes qui n'ont que des revenus de l'art. 25 et dont le revenu annuel net après les seules déductions de l'art. 40 est ≤ **5 000 D** ; aucune restitution avant le 1/1/2020 | n° 104 du 27/12/2019, AR p. 4708 (https://www.pist.tn/jort/2019/2019A/Ja1042019.pdf) ; FR absente de pist.tn |
> | Décret-loi n° 2022-79 (LF 2023), art. 22 § 2 (nouveau § 7 de l'art. 53) | Majoration ramenée à **½ point**, dispense de 5 000 D reprise ; revenus dont la déclaration échoit en 2023, 2024 et 2025 | n° 141 du 23/12/2022, AR pp. 4062-4063 (https://www.pist.tn/jort/2022/2022A/Ja1412022.pdf) ; pas d'édition FR |
> | Loi n° 2024-48 (LF 2025) | **Aucune disposition** sur la CSS des personnes physiques. L'art. 36 change le barème de l'IR à partir des revenus de 2025 | n° 149 du 10/12/2024 (https://www.pist.tn/jort/2024/2024A/Ja1492024.pdf) |
> | Loi n° 2025-17 (LF 2026), art. 87 § 2 | Le § 7 vaut pour les revenus dont la déclaration échoit « de 2023 à 2026 » | n° 148 du 12/12/2025, AR pp. 4253-4254 (https://www.pist.tn/jort/2025/2025A/Ja1482025.pdf) ; pas d'édition FR (l'URL `2025F` sert l'arabe) |
>
> **Écarts constatés**
>
> 1. La valeur au 2025-01-01 est sourcée « LF 2025, maintien à 0,5 % » (finances.gov.tn). Ce texte ne contient pas une telle disposition. La source de la valeur pour les revenus de 2025 est la LF 2026, art. 87 § 2.
> 2. Aucune valeur ne marque la fin du régime temporaire : 0,005 se prolonge indéfiniment.
> 3. Le demi-point est daté au 2023-01-01. Cela suit la lecture des notes communes 1/2023 et 1/2026 (salaires et pensions **payés** du 1/1/2023 au 31/12/2026). À la lettre de la loi, le déclencheur est l'année d'échéance de la déclaration : revenus 2022 à 2025.
> 4. Le seuil de 5 000 D n'est pas un paramètre : il est déduit du barème, alors que la loi le fixe en dinars.
> 5. Les références pointent vers GitLab, jibaya.tn et legislation.tn, au lieu du JORT sur pist.tn.
>
> **Correction proposée**
>
> - Re-libeller le paramètre comme une majoration en points de chaque taux du barème de l'IRPP.
> - Remplacer la source de 2025, ou supprimer la ligne si la lecture « date de paiement » est retenue.
> - Ajouter la valeur de retour à 0,01 : 2026-01-01 à la lettre de la loi, 2027-01-01 selon les notes communes.
> - Créer un paramètre « seuil de dispense » de 5 000 D au 2020-01-01, avec dans sa `note` le calcul de la date (aucune clause d'effet à l'art. 39 § 1 ; § 4 ; NC 28/2019 : salaires payés à partir du 1/1/2020).
> - Créer au besoin une variable d'entrée « revenus exclusivement de l'art. 25 », vraie par défaut pour les cas salariés.
> - Mesurer le revenu de la dispense après les seules déductions de l'art. 40.
> - Tests YAML : bornes 5 000 / 5 000,001 D, revenus 2022, 2025 et 2026.
>
> **Questions ouvertes**
>
> - Lecture « année de déclaration » (lettre du § 7) ou « date de paiement » (notes communes) pour la retenue à la source ? Faut-il deux paramètres, un pour l'impôt annuel et un pour la retenue ?
> - Date d'effet de la dispense : 2020-01-01 (§ 4 et NC 28/2019) ou la date exécutoire de la loi 2019-78 (cinq jours après le dépôt du JORT n° 104, dépôt non daté ici) ?
> - Le volet des sociétés (relèvements 2019-2026, minima, 40 %) fait l'objet d'une issue distincte.
>
> Dépendance : le précis lit ce paramètre par son chemin (`tbl-css-salarie`). Un renommage doit suivre l'ordre d'AGENTS.md : version publiée, puis borne relevée, puis chemins corrigés.

---

## 4. Ce qui reste non trouvé, et les requêtes faites

**Non trouvé ou non disponible**

- **Texte français officiel des LF 2020, 2023, 2024, 2025 et 2026.** pist.tn répond 404 pour
  `2019F/Jo1042019`, `2022F/Jo1412022`, `2023F/Jo1442023` et `2024F/Jo1492024`, et
  `2025F/Jo1482025` sert l'arabe. Les extraits FR locaux des LF 2020, 2024 et 2025 sont mis en page
  comme le JORT, mais leur provenance n'est pas établie ; celui de la LF 2023 est tronqué et
  illisible (pdftotext, mutool et gs échouent). Les citations FR de la LF 2023 viennent donc de la
  NC 1/2023, présentée comme telle.
- **La date exacte de dépôt** du JORT n° 104/2019 au gouvernorat de Tunis, qui servirait au calcul
  de la date exécutoire de l'art. 39 de la LF 2020.
- **La LF 2027** n'est pas publiée au 4 octobre 2026. L'état du droit au-delà des déclarations de
  2026 n'est donc connu que par l'art. 53 lui-même, c'est-à-dire le point entier.
- **Les arrêtés de répartition** du compte de diversification restent couverts par la fiche
  existante `r-css-arretes-repartition`, que je n'ai pas relancée.

**Requêtes**

- `jort_cache.db` :
  - lois et décrets-lois de finances par `numero`, de 2017-66 à 2025-17 : la base ne connaît ni
    2022-79, ni 2023-13, ni 2024-48 sous ces numéros (le n° 141/2022 y figure sans numéro) ;
  - titres `like '%تضامني%'` ou `'%solidarit%sociale%'` ;
  - lois de finances complémentaires ou rectificatives 2018-2026 (`like '%complementaire%'`,
    `'%التعديلي%'`, doublées d'un FTS `complementaire AND finances`) : on trouve la LFC 2019
    (2019-77, n° 100/2019) et la LFR 2020 (2020-45, n° 123/2020).
- **Balayage plein texte** de tous les fascicules locaux FR et AR de 2018 à 2026 (2 117 PDF, jusqu'au
  n° 93/2026), après normalisation NFKC et retrait des marques bidirectionnelles. Motifs :
  « contribution sociale de solidarit », « المساهمة الاجتماعية التضامنية », « 53 من القانون عدد 66 »,
  « article 53 de la loi n° 2017-66 ».
  - Seuls touchés : 2019/104 (LF 2020), 2020/54 (décret-loi 2020-30), 2020/128 (LF 2021), 2021/119
    (LF 2022), 2022/141 (LF 2023), 2024/149 (LF 2025) et 2025/148 (LF 2026).
  - Rien dans la LFC 2019, la LFR 2020 ni la LF 2024 (n° 144/2023).
  - Lacunes : trois fascicules sans couche texte (2018 FR n° 29, 2018 AR n° 26, 2022 AR n° 92), et
    les fascicules absents du corpus local, que ce balayage ne voit pas. Le texte de 2017 n'a pas
    été balayé au-delà du n° 101.
- **Notes communes** lues : 28/2019 (scannée, lue en image), 1/2023 (FR) et 1/2026 (AR seule).

**Fiche de recherche.** Aucune nouvelle fiche n'est proposée : la question « au-delà de 2025 » est
résolue par la LF 2026, art. 87. Je n'ai lancé aucune sous-commande de `scripts/recherches.py`, qui
réécrirait `docs/recherches.yml`.

**Pour le bibliographe**

- `lf-2020` existe dans `fiscalite/references.json` mais **pas dans `caisses/references.json`**
  (FR et AR) : à verser avant d'appliquer le texte proposé.
- `lf-2023` n'a ni `URL` ni pages. À ajouter : https://www.pist.tn/jort/2022/2022A/Ja1412022.pdf,
  art. 22 aux pp. 4062-4063, JORT n° 141 du 23/12/2022.
- `lf-2018` (pp. 4289-4290) et `lf-2020` (p. 4435) sont cohérents avec la pagination FR vérifiée.
- `lf-2026` porte « 4231-4331 » : le texte de la loi s'achève p. 4258, et les tableaux budgétaires
  suivent. Pagination à revoir.
- Les notes communes 28/2019, 1/2023 et 1/2026 sont à verser si le précis cite la lecture
  administrative.

**Ébauches CSL-JSON** (clés suggérées, à valider par le bibliographe)

```json
[
  {"id": "lf-2023", "type": "legislation", "title": "Décret-loi n° 2022-79 du 22 décembre 2022, portant loi de finances pour l'année 2023",
   "container-title": "Journal officiel de la République tunisienne", "number": "141", "issued": {"date-parts": [[2022, 12, 22]]},
   "page": "4062-4063", "URL": "https://www.pist.tn/jort/2022/2022A/Ja1412022.pdf", "note": "Pages de l'art. 22 ; édition arabe seule."},
  {"id": "nc-2019-28", "type": "report", "title": "Note commune n° 28/2019 : commentaire des dispositions de l'article 39 de la loi n° 2019-78 du 23 décembre 2019, portant loi de finances pour l'année 2020, relatives à la révision de la contribution sociale de solidarité",
   "publisher": "Ministère des finances, Direction générale des études et de la législation fiscales", "issued": {"date-parts": [[2019, 12, 31]]}},
  {"id": "nc-2023-1", "type": "report", "title": "Note commune n° 1/2023 : commentaire des dispositions de l'article 22 du décret-loi n° 2022-79 du 22 décembre 2022, portant loi de finances pour l'année 2023",
   "publisher": "Ministère des finances, Direction générale des études et de la législation fiscales", "issued": {"date-parts": [[2023]]}},
  {"id": "nc-2026-1", "type": "report", "title": "مذكرة عامة عدد 1 لسنة 2026 : تحليل أحكام الفصل 87 من القانون عدد 17 لسنة 2025 المؤرخ في 12 ديسمبر 2025 المتعلق بقانون المالية لسنة 2026",
   "publisher": "وزارة المالية، الإدارة العامة للدراسات والتشريع الجبائي", "issued": {"date-parts": [[2026]]}, "language": "ar"}
]
```

URL publiques des notes communes non vérifiées : les fichiers lus sont les copies locales de
`PDFs/Notes_Communes/`. La date exacte de la NC 1/2023 n'a pas été relevée sur le document (le
paramètre d'openfisca dit « 26/01/2023 », non vérifié).
