# Note documentaire : l'impôt sur la fortune en Tunisie (2023-2026)

Documentaliste, 4 octobre 2026. Lecture seule : aucun fichier des dépôts n'a été modifié, et `docs/recherches.yml` n'a pas été réécrit (la fiche est proposée au § 13).

## 0. Réponse directe

- **La loi de finances pour 2025 (loi n° 2024-48, JORT n° 149 du 10 décembre 2024) ne contient rien sur ce sujet.** Le plein texte de l'édition arabe ne contient ni « الثروة » ni aucune mention de l'article 23 du décret-loi n° 2022-79, et son texte français (corpus local) ne contient pas « fortune ». La loi de finances pour 2024 (loi n° 2023-13, JORT n° 144/2023) non plus, dans les deux langues.
- **L'impôt « voté récemment » est l'impôt sur la fortune (الضريبة على الثروة)**, institué par l'**article 88 de la loi n° 2025-17 du 12 décembre 2025, loi de finances pour 2026** (JORT n° 148 du 12 décembre 2025, p. 4254 de l'édition arabe). Il s'applique à compter du 1er janvier 2026 (art. 110).
- Il n'est pas né de rien. L'article 88 **abroge et remplace l'article 23 du décret-loi n° 2022-79 du 22 décembre 2022, loi de finances pour 2023**. Cet article avait institué dès le 1er janvier 2023 un **impôt sur la fortune immobilière** (الضريبة على الثروة العقارية) : taux unique de 0,5 %, sur les seuls immeubles, à partir de 3 MD de valeur nette.
- Entre ces deux textes, aucun modificatif n'a été relevé au JORT. La note commune n° 13/2026, § I, confirme par une seconde voie que l'article 23 était encore « la législation en vigueur jusqu'au 31 décembre 2025 ».
- **Antécédent : l'« impôt foncier » (الضريبة العقارية)** de l'article 55 de la loi de finances pour 2014. Il a été supprimé rétroactivement au 1er janvier 2014 par l'article 38 de la loi de finances complémentaire pour 2014.

## 1. Les textes

| Texte | JORT | Pages (édition) | Contenu | Effet |
|---|---|---|---|---|
| Loi n° 2013-54 du 30 déc. 2013 (LF 2014), art. 55 | n° 105 du 31 déc. 2013 | FR p. 3683 ; AR p. 4358 (pied de page, page par page) | Institue un « impôt foncier » (الضريبة العقارية) sur les immeubles des personnes physiques, égal à une fois et demie la TIB ou la TNB | - |
| Loi n° 2014-54 du 19 août 2014 (LFC 2014), art. 38 | n° 68 du 22 août 2014 | FR p. 2106 (page AR non relevée) | « Sont supprimées à partir du 1er janvier 2014, les dispositions de l'article 55 de la loi de finances pour l'année 2014 » | rétroactif au 1er janv. 2014 |
| Décret-loi n° 2022-79 du 22 déc. 2022 (LF 2023), art. 23 | n° 141 du 23 déc. 2022 | AR pp. 4063-4064 ; FR pp. 3559-3560 | Institue l'impôt sur la fortune immobilière, au taux de 0,5 % | 1er janv. 2023 (art. 76 : AR p. 4082, FR p. 3576) |
| Loi n° 2025-17 du 12 déc. 2025 (LF 2026), art. 88 | n° 148 du 12 déc. 2025 | AR p. 4254 (pas d'édition FR) | Abroge et remplace l'art. 23 : impôt sur la fortune, meubles et immeubles, 0,5 % / 1 % | 1er janv. 2026 (art. 110, AR p. 4258) |

Vérifications faites :
- **Pagination.** Les numéros de page ont été relevés au pied de chaque page, page par page (`pdftotext -f/-l`). Le pied de page est en bas de page dans les quatre fascicules.
- **URL pist.tn**, vérifiées par `curl -k` le 4 octobre 2026 :
  - `https://www.pist.tn/jort/2022/2022A/Ja1412022.pdf` : 200, application/pdf, 40 580 246 o ;
  - `https://www.pist.tn/jort/2022/2022F/Jo1412022.pdf` : **404** (289 o, HTML) ;
  - `https://www.pist.tn/jort/2025/2025A/Ja1482025.pdf` : 200, 8 775 232 o ;
  - `https://www.pist.tn/jort/2025/2025F/Jo1482025.pdf` : 200, mais il sert **le fascicule arabe** (même taille, 8 775 232 o ; piège déjà consigné dans `lf-2026`).
  - Il n'existe donc **aucune URL FR pist.tn** pour ces deux lois.
- **Édition française du JORT n° 141/2022 : elle existe.** Le portail de la DGI en diffuse un fac-similé : `https://jibaya.tn/wp-content/uploads/2024/02/Decret-loi2022_79_compressed.pdf`, 108 pages, créé le 23 février 2023. Ses pieds de page portent « N° 141 Journal Officiel de la République Tunisienne — 23 décembre 2022 Page 3559 ». Le décret-loi commence p. 3556, l'art. 23 occupe les pp. 3559-3560 (§ 1 p. 3559, §§ 2-6 p. 3560), l'art. 76 est p. 3576. **Cela lève le TODO « pagination française non établie » de l'entrée `lf-2023`** (voir § 9).
- **LF 2026 en français.** Il n'existe qu'une traduction diffusée sur www.iort.gov.tn (miroir local `PDFs-legislation-tunisie/data/iort/textes/md/loi_2025_17_2025.md`, l. 578-598). Ce n'est pas un fascicule du JORT. **Le texte arabe fait foi.**
- **Adoption de la LF 2026.** La note (1) de la loi n° 2025-17 (AR p. 4231) porte : « مداولة مجلس نواب الشعب ومصادقته في الجلسة العامة المشتركة بتاريخ 4 ديسمبر 2025 » (délibération et adoption en séance plénière commune le 4 décembre 2025).

## 2. Impôt sur la fortune immobilière (1er janvier 2023 - 31 décembre 2025) : texte de l'art. 23 du DL 2022-79

### Texte arabe (fait foi), JORT n° 141/2022, pp. 4063-4064, couche texte relue

> إحداث ضريبة على الثروة العقارية
> الفصل 23 ـ (1 توظّف في غرة جانفي من كل سنة على مكاسب كل شخص طبيعي من العقارات التي تساوي أو تفوق قيمتها التجارية الحقيقية 3 مليون دينار بما في ذلك العقارات الراجعة بالملك لأبنائه القصر الذين هم في كفالته، ضريبة تسمّى "الضريبة على الثروة العقارية".
> (2 مع مراعاة اتفاقيات تفادي الازدواج الضريبي المبرمة مع البلدان الأخرى عند الاقتضاء، تطبّق الضريبة على الثروة العقارية على: - العقارات الكائنة بالبلاد التونسية بصرف النظر عن مكان إقامة المطالب بالضريبة. - العقارات سواء كانت كائنة بالبلاد التونسية أو بالخارج إذا كان المطالب بالضريبة مقيما بالبلاد التونسية طبقا للتشريع الجبائي الجاري به العمل.
> (3 لا تخضع للضريبة على الثروة العقارية الأملاك الآتي ذكرها: - المسكن الرئيسي للمطالب بالضريبة، - العقارات المخصصة للاستعمال المهني باستثناء العقارات المسوغة لفائدة الغير.
> (4 يضبط مبلغ 3 مليون دينار على أساس قيمة كل العقارات الخاضعة للضريبة المذكورة بما في ذلك الحقوق الاجتماعية في الشركات المدنية العقارية بعد طرح الديون المحمّلة على العقارات المنصوص عليها بأحكام مجلة الحقوق العينية باستثناء الضمانات العينية لفائدة الشركات. تحدّد نسبة الضريبة على الثروة العقارية بـ 0,5 %.
> (5 توظّف الضريبة على الثروة العقارية ويتمّ التصريح بها بقباضة المالية الراجع لها بالنظر مكان مقرّ الإقامة الرئيسي للمطالب بالضريبة بالبلاد التونسية وفي غياب ذلك مكان المنشأة الرئيسية للمطالب بالضريبة أو مكان العقار الأرفع قيمة إذا كان المطالب بالضريبة غير مقيم بالبلاد التونسية، ويتم ذلك في أجل أقصاه موفّى شهر جوان من كل سنة على أساس تصريح تعدّه الإدارة. ويمكن التصريح بهذه الضريبة ودفع المبالغ المستوجبة بعنوانها بالطرق الالكترونية الموثوق بها.
> (6 تطبق على الضريبة على الثروة العقارية بالنسبة إلى الاستخلاص والمراقبة ومعاينة المخالفات والعقوبات والنزاعات والتقادم والاسترجاع نفس القواعد المنصوص عليها بمجلة الحقوق والإجراءات الجبائية.

### Texte français : JORT n° 141/2022, édition française, pp. 3559-3560 (fac-similé DGI, couche texte)

> **Institution d'un impôt sur la fortune immobilière**
> Art. 23 -
> 1) Est exigible au 1er janvier de chaque année sur les biens immobiliers de chaque personne physique dont la valeur vénale est égale ou supérieure à 3 millions de dinars, y compris les immeubles de ses enfants mineurs sous sa tutelle, un impôt intitulé « impôt sur la fortune immobilière ».
> 2) Sous réserve des conventions de non double imposition conclues avec les autres pays le cas échéant, l'impôt sur la fortune immobilière s'applique aux :
> - immeubles situés en Tunisie quel que soit le lieu de résidence du redevable.
> - immeubles situés en Tunisie ou à l'étranger dans le cas où le redevable est résident en Tunisie au sens de la législation fiscale en vigueur.
> 3) Ne sont pas soumis à l'impôt sur la fortune immobilière les biens mentionnés ci-après :
> - L'habitation principale du redevable,
> - Les immeubles destinés à l'exploitation professionnelle à l'exception des immeubles loués au profit d'autrui.
> 4) Le montant de 3 millions de dinars est déterminé sur la base de la valeur de tous les immeubles soumis audit impôt y compris les parts sociales dans les sociétés civiles immobilières après déduction des dettes supportées par les immeubles et prévues par le code des droits réels à l'exception des garanties réelles au profit des sociétés.
> Le taux de l'impôt sur la fortune immobilière est fixé à 0,5%.
> 5) L'impôt sur la fortune immobilière est établi et déclaré à la recette des finances dans la circonscription de laquelle se trouve le lieu du domicile principal du redevable en Tunisie. A défaut du domicile principal, l'impôt doit être établi et déclaré au lieu de l'établissement principal du redevable ou au lieu de l'immeuble ayant la valeur la plus élevée dans le cas où le redevable n'est pas résident en Tunisie, et ce, sur la base d'une déclaration établie par l'administration dans un délai maximum ne dépassant pas la fin du mois de juin de chaque année. Ledit impôt peut être déclaré et payé par les moyens électroniques fiables.
> 6) Sont appliquées à l'impôt sur la fortune immobilière les mêmes modalités prévues au code des droits et procédures fiscaux, relatives aux recouvrement, contrôle, constatation des infractions, sanctions, prescription et restitution.

Date d'effet : art. 76 (FR p. 3576) : « Sous réserve des dispositions contraires prévues par le présent décret-loi, les dispositions du présent décret-loi s'appliquent à compter du 1er janvier 2023. » Le fait générateur est le 1er janvier de chaque année, et l'article 23 ne déroge pas à l'article 76. **Première exigibilité : 1er janvier 2023**, déclaration avant fin juin 2023. La date est énoncée par le texte, donc reprise telle quelle (règle « Dater »).

## 3. Impôt sur la fortune (depuis le 1er janvier 2026) : texte de l'art. 88 de la loi n° 2025-17

### Texte arabe (fait foi), JORT n° 148/2025, p. 4254, couche texte relue

> مزيد تدعيم العدالة الجبائية بين الأفراد
> الفصل 88 ـ تلغى أحكام الفصل 23 من المرسوم عدد 79 لسنة 2022 المؤرخ في 22 ديسمبر 2022 المتعلق بقانون المالية لسنة 2023 وتعوّض بما يلي:
> (1 تستوجب في 1 جانفي من كل سنة ضريبة على مكاسب الأشخاص الطبيعيين بما في ذلك المكاسب الراجعة بالملك لأبنائهم القصر الذين في كفالتهم من العقارات ومن المنقولات تسمى "الضريبة على الثروة" تحتسب بنسبة: - 0,5% بالنسبة إلى المكاسب التي تتراوح قيمتها بين 3 مليون دينار و5 مليون دينار. - 1% بالنسبة إلى المكاسب التي تفوق قيمتها 5 مليون دينار.
> (2 مع مراعاة اتفاقيات تفادي الازدواج الضريبي المبرمة مع البلدان الأخرى عند الاقتضاء، تطبق الضريبة على الثروة على: - العقارات والمنقولات الكائنة بالبلاد التونسية بصرف النظر عن مكان إقامة المطالب بالضريبة. - العقارات والمنقولات سواء كانت كائنة بالبلاد التونسية أو بالخارج إذا كان المطالب بالضريبة مقيما بالبلاد التونسية طبقا للتشريع الجبائي الجاري به العمل.
> (3 توظف الضريبة على الثروة على قيمة العقارات والأصول التجارية والمنقولات المكتسبة بجميع أصنافها، باستثناء المكاسب الآتي ذكرها: - المسكن الرئيسي للمطالب بالضريبة وكذلك الأثاث المستغل به، - العقارات والمنقولات المخصصة للاستعمال المهني والأصول التجارية المستغلة فعليا، - العربات غير النفعية التي تساوي أو تقل قوتها الجبائية عن اثني عشرة خيلا، - الأموال المودعة بالبنوك وبالمؤسسات المالية أو بالبريد التونسي.
> (4 تضبط قيمة المكاسب الخاضعة للضريبة على أساس قيمتها بعد طرح الديون المحملة المنصوص عليها بأحكام مجلة الحقوق العينية باستثناء الضمانات العينية لفائدة الشركات.
> (5 يتمّ التصريح بالضريبة على الثروة في أجل أقصاه موفى شهر جوان من كل سنة وفق أنموذج تعدّه الإدارة، ويمكن التصريح بهذه الضريبة ودفع المبالغ المستوجبة بعنوانها بالطرق الإلكترونية الموثوق بها. وتخضع الضريبة على الثروة بالنسبة إلى التصريح والمراقبة والنزاعات والتقادم والاسترجاع والمخالفات والعقوبات لأحكام مجلة الحقوق والإجراءات الجبائية.
> (6 يتم التصريح بالضريبة على الثروة وتوظيفها: - بمكان مقر الإقامة الرئيسي المصرح به ضمن آخر تصريح بالضريبة على الثروة وفي غياب ذلك بالمقر المضمن ببطاقة التعريف الوطنية بالنسبة إلى الأشخاص الطبيعيين الذين لا يمارسون نشاطا ولا يحققون دخلا على معنى أحكام العددين 1 و2 من الفقرة الأولى من الفصل 3 من مجلة الحقوق والإجراءات الجبائية. - بمكان العقار أو المنقول بالنسبة إلى الأشخاص الطبيعيين الذين لا يمارسون نشاطا ولا يحققون دخلا [...] والذين ليس لهم مقر إقامة رئيسي بالبلاد التونسية أو بمكان العقار أو المنقول الأرفع قيمة [...]. وتبقى المصلحة الجبائية الراجع لها بالنظر المقر الرئيسي للمطالب بالأداء هي المختصة [...] حتى وإن تبيّن من خلال أعمال المراجعة أنّ المقر المصرح بإعفائه من الضريبة على الثروة ليس هو المقر الرئيسي الفعلي للمطالب بالأداء.

### Traduction française diffusée par l'IORT (www.iort.gov.tn ; ce n'est pas le JORT), extraits

> Renforcement de l'équité fiscale entre particuliers
> Art. 88 - Sont abrogées les dispositions de l'article 23 du décret-loi n° 2022-79 du 22 décembre 2022, portant loi de finances pour l'année 2023 et remplacées par ce qui suit:
> 1) Est exigible au 1er janvier de chaque année sur la fortune des personnes physiques y compris la fortune revenant à leurs enfants mineurs sous leur tutelle provenant de biens immeubles et meubles, un impôt intitulé "impôt sur la fortune" liquidé au taux de :
> - 0,5% de la fortune dont la valeur varie de 3 millions de dinars à 5 millions de dinars.
> - 1% de la fortune dont la valeur est supérieure à 5 millions de dinars.
> [...]
> 3) L'impôt sur la fortune est dû sur la valeur des immeubles, des fonds de commerce, et des meubles acquis quel que soit leur nature, à l'exception des biens suivants:
> - L'habitation principale du redevable et les meubles meublants y afférant,
> - Les immeubles et meubles destinés à l'exploitation professionnelle et les fonds de commerce effectivement exploités,
> - Les véhicules non utilitaires dont la puissance fiscale est égale ou inférieure à douze (12) chevaux,
> - Les biens déposés auprès des banques et établissements financiers ou auprès de la Poste tunisienne.
> 4) La valeur de la fortune soumise à l'impôt est déterminée sur la base de sa valeur après déduction des dettes supportées prévues par le code des droits réels excepté les garanties réelles au profit des sociétés.
> 5) L'impôt sur la fortune est déclaré dans un délai maximum ne dépassant pas la fin du mois du juin de chaque année selon un modèle établi par l'administration [...]

Écarts de la traduction IORT par rapport à l'arabe, à signaler si on la cite :
- « الأموال المودعة » = « les fonds déposés » (IORT : « les biens déposés ») ;
- « الأثاث المستغل به » = « le mobilier qui y est utilisé » (IORT : « meubles meublants y afférant ») ;
- « الأصول التجارية » = « fonds de commerce » (correct) ;
- « المكتسبة بجميع أصنافها » = « acquis, de toutes catégories ».
- Le précis traduira donc lui-même, en signalant que l'édition française du JORT n'est pas parue.

Date d'effet : art. 110 § 1 (AR p. 4258) : « تطبق أحكام هذا القانون بداية من غرة جانفي 2026 وذلك باستثناء الأحكام الواردة بالفصول 56 و60 و61 و62 من هذا القانون » (les dispositions de la présente loi s'appliquent à compter du 1er janvier 2026, à l'exception des articles 56, 60, 61 et 62). L'art. 88 n'est pas parmi les exceptions. **Première exigibilité de l'impôt sur la fortune : 1er janvier 2026**, déclaration avant fin juin 2026.

## 4. Ce qui change entre 2023 et 2026, selon les seuls textes de loi

| Élément | DL 2022-79, art. 23 (1/1/2023 - 31/12/2025) | Loi 2025-17, art. 88 (depuis le 1/1/2026) |
|---|---|---|
| Nom | الضريبة على الثروة العقارية / impôt sur la fortune immobilière | الضريبة على الثروة / impôt sur la fortune |
| Redevables | personnes physiques, biens des enfants mineurs à charge compris | idem |
| Fait générateur | 1er janvier de chaque année | idem |
| Biens imposables | immeubles, parts de sociétés civiles immobilières comprises (§ 4) | immeubles, fonds de commerce, meubles « de toutes catégories » (§ 3) ; les SCI ne sont plus citées par le texte |
| Territorialité | immeubles en Tunisie (tout redevable) ; en Tunisie et à l'étranger (résident) | idem, étendue aux meubles |
| Exonérations | habitation principale ; immeubles professionnels **sauf ceux loués à autrui** | habitation principale et son mobilier ; immeubles et meubles professionnels, fonds de commerce effectivement exploités ; véhicules non utilitaires ≤ 12 CV ; fonds déposés en banque, établissement financier ou à la Poste ; plus de mention des immeubles loués |
| Valeur | « valeur vénale » / القيمة التجارية الحقيقية ; dettes du code des droits réels déduites, garanties réelles au profit de sociétés exclues | valeur nette des mêmes dettes ; le texte ne dit plus « valeur vénale » |
| Seuil | ≥ 3 MD (valeur nette) | 3 MD : « entre 3 et 5 MD » |
| Taux | 0,5 % | 0,5 % (3 à 5 MD) ; 1 % (au-delà de 5 MD) |
| Déclaration | avant fin juin, recette des finances du domicile principal ; à défaut, établissement principal ou immeuble de plus grande valeur (non-résident) | avant fin juin, selon un modèle de l'administration ; lieu fixé au § 6 par renvoi à l'art. 3 du CDPF |
| Contrôle, sanctions, contentieux | renvoi au CDPF | renvoi au CDPF |

Le texte de 2026 ne dit pas si chaque taux s'applique à toute la valeur ou à la seule tranche (« تحتسب بنسبة 0,5% بالنسبة إلى المكاسب التي تتراوح قيمتها بين … »). La lecture de l'administration est donnée au § 5.

## 5. Doctrine administrative (notes communes de la DGELF), à tenir distincte de la loi

### NC n° 15/2023, 29 mai 2023 (cachet de couverture lu à l'image), sur l'art. 23 du DL 2022-79

- **Source.** PDF de 13 pages sans couche texte, créé le 20 juin 2023 : `https://jibaya.tn/wp-content/uploads/2024/07/مذكرة-عامة-عدد-15.pdf` (fiche : `https://jibaya.tn/docs/note-commune-n15-impot-sur-la-fortune-immobiliere-disponible-en-arabe/`, mise en ligne le 1er juillet 2024). Arabe seulement. Océrisé (tesseract `ara`) ; couverture et pp. 4, 5, 8 et 9 relues à l'image, et tout ce qui est cité ci-dessous en provient. Signée « المدير العام للدراسات والتشريع الجبائي — يحيى الشملالي ».
- **Annexes.** Annexe 1 : exemples d'application. Annexe 2 : **modèle de déclaration** « التصريح بالضريبة على الثروة العقارية ».
- **Taux appliqué à toute la base, non au dépassement.** § IV.1 (p. 5, à l'image) : « تحتسب الضريبة على الثروة بنسبة 0.5 % على أساس القيمة الجمليّة لكلّ العقارات الخاضعة للضريبة ». Exemple 1 (p. 9, relu à l'image) : base 3,570 MD − dette 170 000 D = 3,4 MD ; « 3,4 م د X 0,5% = 17.000 د ». Exemple 2 : base nette 2,9 MD, pas d'impôt, « باعتبار أنّ قيمة العقارات المستوجبة لدفع الضريبة ... لا تساوي أو تفوق 3 مليون دينار ».
- **Immeubles loués** (p. 5, à l'image) : « وتجدر الإشارة إلى أنّ العقارات المسوّغة لفائدة الغير سواء كانت فلاحيّة أو غير فلاحية تدخل ضمن عناصر قاعدة احتساب الضريبة وتخضع للضريبة على الثروة العقارية » (les immeubles loués à autrui, agricoles ou non, entrent dans la base et sont imposables).
- **Terres agricoles.** Les terres exploitées directement ne sont exonérées que si des revenus agricoles sont déclarés. Les terres de grandes cultures exploitées directement sont exonérées.
- **Biens des mineurs.** Les enfants mineurs à charge s'entendent au sens de l'art. 154 du CSP. Les biens des enfants majeurs sont déclarés séparément.
- **Meubles** (p. 4, à l'image) : « فإنّ المنقولات بجميع أنواعها كالأموال وسندات القيم المنقولة تكون خارج ميدان التطبيق » (les meubles de toute nature, dont les fonds et les valeurs mobilières, sont hors du champ).
- **Valeur et dettes.** La valeur retenue est la valeur vénale réelle au 1er janvier. L'hypothèque se déduit pour le capital restant dû au 1er janvier.
- **Effet.** § 8 du résumé : « يجري العمل بهذا الإجراء ابتداء من غرة جانفي 2023 ».

### NC n° 13/2026, 11 juin 2026 (cachet « 11 جوان 2026 » lu à l'image), sur l'art. 88 de la loi n° 2025-17

- **Source.** PDF de 10 pages, créé le 12 juin 2026 (auteur : MINISTERE DES FINANCES) : `https://jibaya.tn/wp-content/uploads/2026/06/مذكرة-عامة-عدد-13-لسنة-2026.pdf` (fiche : `https://jibaya.tn/docs/note-commune-n13-commentaire-des-dispositions-de-larticle-88-de-la-loi-n2025-17-du-12-decembre-2025-portant-loi-de-finances-pour-lannee-2026-relatives-a-linsta/`, mise en ligne le 12 juin 2026). Arabe seulement.
- **Lecture.** La couche texte utilise une police à substitution (illisible telle quelle). **Les passages cités ont été relus à l'image** : pp. 1, 4, 5, 6, 7, 8 et 10.
- **Objet** (p. 1) : « شرح أحكام الفصل 88 من القانون عدد 17 لسنة 2025 المؤرخ في 12 ديسمبر 2025 المتعلق بقانون المالية لسنة 2026 المتعلقة بإحداث ضريبة على الثروة ».
- **§ I (p. 4), « التشريع الجاري به العمل إلى غاية 31 ديسمبر 2025 ».** Il résume l'art. 23 : 0,5 % sur les immeubles dont la valeur globale est ≥ 3 MD. **C'est la seconde voie qui établit l'absence de modificatif entre 2023 et 2025.**
- **§ II.1.1, taux (p. 4)** : « 0,5% من القيمة الجمليّة للمكاسب التي تتراوح بين 3 مليون دينار و5 مليون دينار » ; « 1% من القيمة الجمليّة للمكاسب التي تفوق 5 مليون دينار ».
  - **Pour l'administration, le taux s'applique à la valeur globale, non à la tranche.**
  - Conséquence arithmétique, calculée par le documentaliste et non écrite dans la note : 25 000 D d'impôt à 5 MD, 50 000 D dès que la valeur dépasse 5 MD.
  - La seule source de cette lecture est la NC. À présenter comme lecture administrative.
- **§ II.1.2 (p. 5, à l'image) :** « تطبّق الضريبة على الثروة على الأشخاص الطبيعيين الذين تساوي أو تفوق القيمة الجملية للأصول الصافية الراجعة لهم بالملكية في تاريخ 1 جانفي من سنة التوظيف 3 مليون دينار ». Est redevable toute personne physique dont la valeur globale des actifs nets au 1er janvier est ≥ 3 MD. Les biens des enfants majeurs sont déclarés séparément. En indivision, chaque redevable déclare sa quote-part.
- **§ II.1.3 (pp. 5-6, à l'image), biens imposables.** « على جملة المكاسب ... سواء تعلّق الأمر بالعقارات أو الحقوق العينية العقارية أو المنقولات بجميع أنواعها ... أو حقوق اجتماعيّة في شركات مدنيّة عقاريّة » : immeubles et droits réels immobiliers, **parts sociales de sociétés civiles immobilières** (alors que l'art. 88 ne les nomme plus), meubles corporels et incorporels au sens des art. 14 et 15 du code des droits réels (actions, parts, créances).
- **§ II.2 (p. 6), valeur.**
  - Immeubles : la valeur déclarée, rectifiable par l'administration par comparaison ou expertise.
  - Titres cotés : cours au 31 décembre de l'année précédente.
  - Titres non cotés : valeur de liquidation ou valeur comptable, notamment.
- **§ II.3, exonérations, avec des conditions que la loi n'écrit pas** :
  - **Habitation principale** (p. 6) : quelle qu'en soit la valeur ou la surface, dépendances comprises ; le mobilier « مهما كانت قيمته » (quelle qu'en soit la valeur) ; la preuve se fait par une attestation des services compétents.
  - **Usage professionnel** (pp. 6-7) : le bien doit figurer à l'actif du bilan ou avoir fait l'objet d'une déclaration de revenus professionnels. Les terres agricoles exploitées directement ne sont exonérées que si des revenus agricoles sont déclarés, même déficitaires.
  - **Immeubles loués** (p. 7) : « فإنّ إعفاء العقارات المسوّغة لفائدة الغير من الضريبة على الثروة يتوقّف على التصريح بمداخيل عقارية بعنوانها » (l'exonération des immeubles loués à autrui est subordonnée à la déclaration des revenus fonciers correspondants). **Cette condition est dans la NC, non dans l'art. 88.**
  - **Actions et parts** (p. 7) : actions et parts de SARL réputées professionnelles si le redevable et ses enfants mineurs détiennent au moins 50 % du capital. Parts de sociétés en nom collectif, de fait, en commandite simple, en participation, de sociétés communautaires, de GIE et de sociétés civiles professionnelles : exonérées.
  - **Fonds déposés** (p. 8) : la NC en dresse **une liste limitative** :
    - les comptes spéciaux d'épargne (logement, études, autres) ;
    - les comptes épargne en actions de la loi n° 99-92 ;
    - les comptes épargne pour l'investissement ;
    - les primes et cotisations d'assurance-vie et de capitalisation, takaful compris.
    - **Les comptes courants et les dépôts à terme n'y figurent pas.**
  - **Véhicules** (p. 8) : les véhicules non utilitaires de plus de 12 CV sont imposables, sauf ceux inscrits au bilan professionnel.
- **§ II.4 (pp. 8-10).** Calcul sur la valeur globale nette de dettes. Hypothèque déduite pour le capital restant dû au 1er janvier.
- **§ III (p. 10, à l'image) :** « عملا بأحكام الفصل 110 من قانون المالية لسنة 2026 تطبّق أحكام الفصل 88 منه ابتداء من غرّة جانفي 2026 ». L'art. 88 s'applique à compter du 1er janvier 2026 en vertu de l'art. 110, donc aux biens détenus à cette date.
- **Signature** (p. 10, à l'image) : « يحيى الشملالي », directeur général des études et de la législation fiscales.

## 6. Textes d'application

- Ni l'art. 23 ni l'art. 88 ne renvoient à un décret ou à un arrêté. Le modèle de déclaration est « établi par l'administration ».
- Aucun décret ni arrêté relatif à cet impôt n'a été trouvé dans jort_cache ni dans le corpus (§ 13).
- Le modèle de déclaration 2023 est l'annexe 2 de la NC 15/2023.
- Le modèle de déclaration 2026 n'a pas été trouvé : la NC 13/2026 n'a pas d'annexe. La presse (La Presse, 29 juin 2026) évoque un changement de formulaire, sans pièce primaire.

## 6 bis. Codification : l'impôt reste hors code

- **L'impôt n'est codifié dans aucun code. Il vit dans une disposition autonome de loi de finances.**
  - En 2023, c'est l'art. 23 du DL 2022-79.
  - En 2026, l'art. 88 de la loi n° 2025-17 « abroge et remplace les dispositions de l'article 23 du décret-loi n° 2022-79 » : il modifie ce décret-loi, non un code.
  - Les deux textes ne renvoient au code des droits et procédures fiscaux (CDPF) que pour la procédure : déclaration, contrôle, contentieux, prescription, restitution, infractions et sanctions (art. 23 § 6 ; art. 88 § 5). L'art. 88 § 6 renvoie aussi à l'art. 3 du CDPF pour le lieu de déclaration.
- **Codes consolidés de l'IRPP et de l'IS** (`markdown_output/Code_de_lIRPP_et_IS_{2019,2020,2021,2022,2023,2025}.md`, PDF en regard dans `PDFs/Code_de_lIRPP_et_IS/`, pas d'édition 2024 ni 2026 au corpus) :
  - « fortune » et « patrimoine » n'y renvoient qu'à la note de l'art. 43 : l'évaluation forfaitaire d'après « l'accroissement de sa fortune » ou « l'accroissement du patrimoine », sans rapport avec cet impôt ;
  - l'édition 2025, postérieure au DL 2022-79, n'intègre pas l'impôt sur la fortune immobilière.
- **Aucun article de LF n'a été trouvé qui modifie le CDPF pour y nommer l'impôt.** Un tel article contiendrait « الثروة ». Or le plein texte normalisé des 555 fascicules arabes de 2023 au n° 93 de 2026 n'a « الثروة » que dans l'art. 23 et dans l'art. 88 (les autres occurrences sont des homonymes). Le CDPF consolidé lui-même n'est pas au corpus local et n'a pas été lu ; la lacune se limite à ce contrôle direct.
- **Lois de finances au corpus** (`PDFs/Lois_de_Finances/`) :
  - LF 2024 (122 p.) et LF 2025 (117 p.), éditions françaises : aucune occurrence de « fortune ». Cela confirme, dans l'autre langue, l'absence de modificatif ;
  - `Loi_des_Finances_2026_disponible_en_langue_arabe_uniquement.pdf` (101 p., arabe) : 8 occurrences de « الثروة », toutes dans l'art. 88 comme au fascicule. Ce n'est pas le même fichier que `Ja1482025.pdf` (md5 différents) ; seul le JORT est cité.
- **Notes communes locales** (`PDFs/Notes_Communes/`, 1 223 fichiers) :
  - la NC 15/2023 y est (`Note_commune_n15__Impôt_sur_la_fortune_immobilière_Disponible_en_arabe.pdf`), identique octet pour octet à la pièce de jibaya.tn (md5 805518e5…) ;
  - **la NC 13/2026 n'y est pas** (seule la NC 2/2026 sur l'art. 53 de la LF 2026 y figure). Elle a été prise sur jibaya.tn ;
  - aucune note commune ne commente une disposition « fortune » de la LF 2025, qui n'en contient pas.

## 7. Antécédent : l'impôt foncier de 2014 (lu au fascicule)

- **Institution.** LF 2014, art. 55, JORT n° 105 du 31 décembre 2013, FR p. 3683, AR p. 4358. Intitulé AR : « توظيف ضريبة على العقارات » ; FR : « Institution d'un impôt sur les immeubles ». Texte FR :
  > Est institué un impôt sur les immeubles y compris les droits s'y rattachant qui sont détenus par les personnes physiques dénommé « impôt foncier ». […] Le montant de l'impôt exigible est égal à une fois et demie, la taxe sur les immeubles bâtis ou la taxe sur les immeubles non bâtis, selon le cas. L'impôt foncier est payé au plus tard à la fin du mois de mars de chaque année […]

  AR : « توظف ضريبة على العقارات التي يمتلكها الأشخاص الطبيعيون بما في ذلك الحقوق المتعلقة بها تسمّى الضريبة العقارية ».
- **Exonérations de 2014** :
  - habitation principale ;
  - immeubles bâtis exploités pour une activité industrielle, commerciale ou professionnelle ;
  - immeubles affectés à une émission de sukuk ;
  - terres agricoles en zone agricole ;
  - terrains non bâtis lotis en zones industrielle, d'habitation, touristique ou artisanale ;
  - terrains non bâtis exploités pour une activité ;
  - immeubles destinés à la location, si l'on joint la déclaration de revenus fonciers.
- **Suppression.** LFC 2014, art. 38, JORT n° 68 du 22 août 2014, FR p. 2106 : « Sont supprimées à partir du 1er janvier 2014, les dispositions de l'article 55 de la loi de finances pour l'année 2014. » AR : « تلغى ابتداء من غرة جانفي 2014 أحكام الفصل 55 من قانون المالية لسنة 2014 », sous l'intitulé « إلغاء أحكام قانون المالية لسنة 2014 المتعلقة بإحداث ضريبة عقارية وبجباية وسائل النقل ».
- **Nature.** Ce n'était pas un impôt sur la fortune (pas de seuil de patrimoine) : c'était une surtaxe des taxes locales sur les immeubles. **Il n'a jamais été appliqué**, faute d'avoir survécu à son année.
- Aucun autre impôt national sur le patrimoine n'a été identifié entre 1956 et 2022. La recherche n'a pas été poussée au-delà des intitulés jort_cache, et l'époque beylicale et coloniale n'a pas été explorée : c'est une lacune.

## 8. Rendement et genèse parlementaire

- **Aucune série officielle de rendement n'a été trouvée.**
  - Le tableau A de la LF 2026 n'a pas de ligne propre : le plein texte du fascicule n° 148/2025 ne contient « الثروة » que dans l'art. 88.
  - Pas de donnée dans les sources consultées du ministère des Finances.
  - La série `minfin-recettes-fiscales` du précis n'a pas été dépouillée pour cette ligne : TODO.
- **Chiffres de presse, à ne pas reprendre comme valeurs** : objectif de « 35 MD minimum » et « plus de 2 700 fortunes immobilières » ciblées en 2023 (presse, sans pièce de la DGI) ; estimation du ministère de « 11 MD » pour l'art. 50 du projet de LF 2026, citée par un député (La Presse, 24 novembre 2025).
- **Genèse de l'art. 88 (presse seulement)** :
  - l'art. 50 du projet de LF 2026 est rejeté en commission conjointe, par 10 voix contre 3 (La Presse, 24 novembre 2025) ;
  - il est supprimé en plénière le 1er décembre 2025 (La Presse, 1er décembre 2025) ;
  - il est réintroduit sous forme modifiée par le gouvernement, puis adopté, et devient l'art. 88 (La Presse, 5 décembre 2025).
  - La seule pièce primaire est la note (1) de la loi : adoption en plénière commune le 4 décembre 2025. Le reste n'entre pas au corps du précis sans pièce de l'ARP ou du CNRD.

## 9. Références candidates

### Entrées existantes à compléter (bibliographe)

- **`lf-2023` (FR et AR)** :
  - ajouter à `note` : art. 23, AR pp. 4063-4064, FR pp. 3559-3560 ; art. 76, AR p. 4082, FR p. 3576.
  - **Lever le TODO « pagination française non établie »** : le décret-loi commence FR p. 3556, d'après le fac-similé de l'édition française du JORT n° 141 diffusé par la DGI (`https://jibaya.tn/wp-content/uploads/2024/02/Decret-loi2022_79_compressed.pdf`, 108 p., pieds de page « N° 141 … Page 3559 », lus le 4 octobre 2026).
  - L'entrée FR reste **sans URL** (pist.tn 2022F : 404), la copie DGI étant consignée dans `note` ; l'entrée AR garde `https://www.pist.tn/jort/2022/2022A/Ja1412022.pdf`.
- **`lf-2026` (FR et AR)** : ajouter à `note` : art. 88 (impôt sur la fortune), AR p. 4254 ; art. 110 (date d'application), AR p. 4258 ; note (1), adoption en plénière commune le 4 décembre 2025. Traduction française non officielle sur www.iort.gov.tn.
- **`lf-2014` (fiscalite FR et AR)** : ajouter art. 55 (impôt foncier), FR p. 3683, AR p. 4358.
- **`lfc-2014` (fiscalite FR et AR)** :
  - ajouter art. 38, FR p. 2106 ;
  - **vérifier le champ `page: "2183-2232"`**. Dans le fascicule français local `Jo0682014.pdf` (88 p.), la loi commence p. 2094-2095 et l'art. 38 est p. 2106. Le texte arabe montre une page « 2182 » en tête de la loi. **La plage 2183-2232 semble être la pagination arabe**, même confusion que celle déjà notée pour `lf-2025`. À confirmer à l'image avant correction.

### Entrées nouvelles (FR, `precis/fr/fiscalite/references.json`)

```json
{
  "id": "dgi-nc-15-2023",
  "type": "report",
  "title": "Note commune n° 15/2023 — Commentaire des dispositions de l'article 23 du décret-loi n° 2022-79 du 22 décembre 2022 portant loi de finances pour l'année 2023 relatives à l'institution d'un impôt sur la fortune immobilière",
  "title-short": "Note commune n° 15/2023",
  "author": [{"literal": "Tunisie. Ministère des finances, Direction générale des études et de la législation fiscales"}],
  "publisher": "Ministère des finances",
  "publisher-place": "Tunis",
  "issued": {"date-parts": [[2023, 5, 29]]},
  "URL": "https://jibaya.tn/docs/note-commune-n15-impot-sur-la-fortune-immobiliere-disponible-en-arabe/",
  "note": "citation-key: dgi-nc-15-2023\nNote en arabe seulement (مذكرة عامة عدد 15 لسنة 2023). Titre français : traduction du documentaliste d'après l'objet arabe. PDF de 13 p. SANS couche texte : https://jibaya.tn/wp-content/uploads/2024/07/مذكرة-عامة-عدد-15.pdf (créé le 20/06/2023, mis en ligne le 01/07/2024). Cachet de couverture « 29 ماي 2023 », lu à l'image le 4/10/2026. Annexe 1 : exemples (ex. 1 : 3,4 MD × 0,5 % = 17 000 D, taux appliqué à toute la base). Annexe 2 : modèle de déclaration."
}
```

```json
{
  "id": "dgi-nc-13-2026",
  "type": "report",
  "title": "Note commune n° 13/2026 — Commentaire des dispositions de l'article 88 de la loi n° 2025-17 du 12 décembre 2025 portant loi de finances pour l'année 2026 relatives à l'instauration de l'impôt sur la fortune",
  "title-short": "Note commune n° 13/2026",
  "author": [{"literal": "Tunisie. Ministère des finances, Direction générale des études et de la législation fiscales"}],
  "publisher": "Ministère des finances",
  "publisher-place": "Tunis",
  "issued": {"date-parts": [[2026, 6, 11]]},
  "URL": "https://jibaya.tn/docs/note-commune-n13-commentaire-des-dispositions-de-larticle-88-de-la-loi-n2025-17-du-12-decembre-2025-portant-loi-de-finances-pour-lannee-2026-relatives-a-linsta/",
  "note": "citation-key: dgi-nc-13-2026\nNote en arabe seulement (مذكرة عامة عدد 13 لسنة 2026) ; titre français repris de la fiche jibaya.tn. PDF de 10 p. : https://jibaya.tn/wp-content/uploads/2026/06/مذكرة-عامة-عدد-13-لسنة-2026.pdf (créé le 12/06/2026). La couche texte, à police substituée, est inutilisable : citer d'après l'image. Cachet « 11 جوان 2026 » lu à l'image le 4/10/2026. § I : régime de l'art. 23 du DL 2022-79 en vigueur jusqu'au 31/12/2025. § II.1.1 : taux appliqué à la valeur globale. § II.3.3 : liste limitative des fonds déposés exonérés. § III : effet au 1er janvier 2026 (art. 110)."
}
```

### Entrées nouvelles (AR, `precis/ar/fiscalite/references.json`)

L'usage actuel (`dgi-nc-1-2022` AR) garde le titre français. Ébauches à titre arabe, si le bibliographe le préfère pour des notes parues en arabe seulement :

```json
{
  "id": "dgi-nc-15-2023",
  "type": "report",
  "title": "مذكرة عامة عدد 15 لسنة 2023 — شرح أحكام الفصل 23 من المرسوم عدد 79 لسنة 2022 المؤرخ في 22 ديسمبر 2022 المتعلق بقانون المالية لسنة 2023 المتعلقة بإحداث ضريبة على الثروة العقارية",
  "title-short": "مذكرة عامة عدد 15 لسنة 2023",
  "author": [{"literal": "الجمهورية التونسية. وزارة المالية، الإدارة العامة للدراسات والتشريع الجبائي"}],
  "publisher": "وزارة المالية",
  "publisher-place": "تونس",
  "issued": {"date-parts": [[2023, 5, 29]]},
  "URL": "https://jibaya.tn/docs/note-commune-n15-impot-sur-la-fortune-immobiliere-disponible-en-arabe/",
  "note": "citation-key: dgi-nc-15-2023\n(même note de provenance que l'entrée FR)"
}
```

```json
{
  "id": "dgi-nc-13-2026",
  "type": "report",
  "title": "مذكرة عامة عدد 13 لسنة 2026 — شرح أحكام الفصل 88 من القانون عدد 17 لسنة 2025 المؤرخ في 12 ديسمبر 2025 المتعلق بقانون المالية لسنة 2026 المتعلقة بإحداث ضريبة على الثروة",
  "title-short": "مذكرة عامة عدد 13 لسنة 2026",
  "author": [{"literal": "الجمهورية التونسية. وزارة المالية، الإدارة العامة للدراسات والتشريع الجبائي"}],
  "publisher": "وزارة المالية",
  "publisher-place": "تونس",
  "issued": {"date-parts": [[2026, 6, 11]]},
  "URL": "https://jibaya.tn/docs/note-commune-n13-commentaire-des-dispositions-de-larticle-88-de-la-loi-n2025-17-du-12-decembre-2025-portant-loi-de-finances-pour-lannee-2026-relatives-a-linsta/",
  "note": "citation-key: dgi-nc-13-2026\n(même note de provenance que l'entrée FR)"
}
```

Presse, à ne créer que si le rédacteur cite la genèse parlementaire hors du corps (secondaire) :
- `lapresse-2025-11-24-ifi-rejet` : https://www.lapresse.tn/2025/11/24/impot-sur-la-fortune-voici-pourquoi-le-parlement-a-dit-non/
- `lapresse-2025-12-01-art50` : https://www.lapresse.tn/2025/12/01/parlement-larticle-50-sur-limpot-sur-la-fortune-supprime/
- `lapresse-2025-12-05-adoption` : https://www.lapresse.tn/2025/12/05/limpot-sur-la-fortune-officiellement-adopte/

## 10. Notions à glossaire (`precis/glossaire.yml` : aucune entrée « fortune » ni « ثروة » à ce jour)

| id proposé | FR | AR (terme du JORT) | Source (définition et traduction) |
|---|---|---|---|
| `impot-fortune` | impôt sur la fortune | الضريبة على الثروة | `lf-2026`, art. 88 (AR p. 4254) ; traduction FR de l'IORT, non officielle |
| `impot-fortune-immobiliere` | impôt sur la fortune immobilière | الضريبة على الثروة العقارية | `lf-2023`, art. 23 (AR p. 4063, FR p. 3559) : les deux éditions du JORT |
| `impot-foncier-2014` | impôt foncier (2014) | الضريبة العقارية | `lf-2014`, art. 55 (FR p. 3683, AR p. 4358) : les deux éditions |
| `habitation-principale` | habitation principale | المسكن الرئيسي | `lf-2023`, art. 23 § 3 (FR « habitation principale » ; AR « المسكن الرئيسي للمطالب بالضريبة ») |
| `fonds-de-commerce` | fonds de commerce | الأصول التجارية | `lf-2026`, art. 88 § 3 (seule la traduction IORT donne le FR) ; à confirmer dans un texte bilingue du JORT avant `valide` |

Règle « impôt » de `docs/agents/terminologue.md` : un impôt nommé garde le nom que lui donne le texte. On écrit donc **الضريبة على الثروة**, et non الأداء على الثروة. Redevable : « المطالب بالضريبة » (art. 23 et art. 88 §§ 2 et 3) ; l'art. 88 § 6 et les NC disent aussi « المطالب بالأداء ».

## 11. Où le placer dans « La fiscalité »

- **Nature.** C'est un impôt direct : une matière stable, imposée chaque année au 1er janvier, au sens de Zakraoui cité dans `index.qmd`. Il ne relève d'aucun des quatre chapitres existants : il frappe un stock, pas un revenu, un bénéfice ou une opération.
- **Option A, un chapitre propre** (`_impot_fortune.qmd`, après l'IS, dans l'imposition directe). C'est la seule option qui suive le plan type (historique, description, évolution réforme par réforme, données). Conséquences :
  - dans `index.qmd`, réécrire « Les quatre impôts de ce livre », compléter `tbl-fisc-carte` d'une ligne, et nuancer « Ces quatre impôts ont en commun d'avoir été refondus à la fin des années 1980 » ;
  - ajouter le chapitre au `_quarto.yml` FR, puis **à la main** au `_quarto.yml` AR une fois la traduction livrée ;
  - la section finale « ce qu'il rapporte » serait vide : pas de série officielle de rendement (§ 8). Le chapitre devrait s'achever sur une case vide honnête.
- **Option B, une section du chapitre IRPP** (même redevables, personnes physiques). Plus légère, mais elle range un impôt sur le stock dans un chapitre sur le revenu. Le seul lien textuel est l'art. 43 du code (accroissement du patrimoine, déjà cité au chapitre IRPP), et il est indirect.
- **À arbitrer par l'humain.**

## 12. Lacunes (TODO, rien n'a été inventé)

1. Rendement de l'impôt sur la fortune immobilière (2023-2025) et de l'impôt sur la fortune (2026) : aucune source officielle. La série `minfin-recettes-fiscales` n'a pas été dépouillée pour cette ligne.
2. Modèle de déclaration 2026 : non trouvé.
3. Édition française officielle de la LF 2026 : non parue (pist.tn sert l'arabe à l'adresse 2025F). Les citations FR de l'art. 88 sont des traductions.
4. Page arabe de l'art. 38 de la LFC 2014 : non relevée (texte lu dans la couche texte normalisée). Celle de l'art. 55 de la LF 2014 (p. 4358) est confirmée.
5. Champ `page` de `lfc-2014` : vraisemblablement la pagination arabe, à confirmer à l'image.
6. Antécédents avant 1956 et entre 1956 et 2013 : non explorés au-delà des intitulés jort_cache.
7. Genèse parlementaire de l'art. 88 : presse seulement. Aucune pièce de l'ARP ni du CNRD lue.
8. Corpus postérieur au JORT n° 93 du 18 septembre 2026 : non parcouru. Le n° 58 de 2026 est absent du corpus (lacune déjà connue).

## 13. Recherche infructueuse : fiche proposée (non versée, travail en lecture seule)

Aucune fiche existante ne porte sur cet objet : `recherches.py lister` donne 36 fiches, aucune sur la fortune ou le patrimoine.

```yaml
- id: r-impot-fortune-modificatifs
  objet: texte modifiant l'article 23 du décret-loi n° 2022-79 (impôt sur la fortune immobilière) ou l'article 88 de la loi n° 2025-17 (impôt sur la fortune), ou pris pour leur application (décret, arrêté)
  ou: [precis/fr/fiscalite/<chapitre à créer>.qmd#<ancre>]   # À REMPLIR par le rédacteur : tel quel, `recherches.py verifier` échoue
  requetes:
    titres_fts: ['fortune OR patrimoine immobilier', 'fortune OR الثروة']
    titres_like: ['%loi de finances%']
    plein_texte: [الثروة, الثروة العقارية, الضريبة على الثروة, "79 لسنة 2022", fortune, "impôt sur la fortune"]
    depuis: 2022-12-23
  passes:
  - date: 2026-10-04
    role: documentaliste
    sources: [jort_cache, corpus_local, iort, presse]
    couverture: 'jort_cache : FTS match « fortune OR patrimoine immobilier » (soit fortune OU (patrimoine ET immobilier), sans guillemets de phrase) et match « fortune OR الثروة » (un seul résultat pertinent, la notice du DL 2022-79 art. 23), LIKE « loi de finances » 2019-2026. Plein texte (pdftotext -layout) de tous les fascicules AR (555, normalisés NFKC pour les formes de présentation arabes) et FR du corpus local de 2023 au n° 93 de 2026, et des n° 140-143 de 2022 : « الثروة » ne renvoie, hors homonymes (ثروة حيوانية, معدنية, مصدر الثروة), qu à Ja1412022 (art. 23) et Ja1482025 (art. 88) ; « fortune » ne renvoie à aucun fascicule FR. Les « 79 لسنة 2022 » des LF 2024 (Ja1442023) et LF 2025 (Ja1492024) visent d autres articles (15, 26, 28, 29, 59, 64). Seconde voie : la NC 13/2026, § I, donne l art. 23 comme législation en vigueur jusqu au 31/12/2025. Lacunes : n° 58 de 2026 absent du corpus ; rien après le n° 93 de 2026 ; fascicules inconnus de jort_cache (outillage-sources § 1 f) parcourus seulement s ils sont au corpus local ; Ja0672025, Ja0702025, Ja0842024, Ja1202024, Ja1252024 sont de petits fascicules à couche texte (2 à 7 p.), non des scans.'
    couvert_jusqu_au: 2026-09-18
    resultat: aucun
  a_faire:
  - 'lire les numéros du JORT postérieurs au n° 93 de 2026, et le n° 58 de 2026'
```

## 14. Pièces téléchargées (scratchpad, hors dépôts)

Dans `/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/212eebb3-5a49-4181-98e4-bbe6590342a7/scratchpad/` :
- `nc15_2023.pdf` et `nc15_2023_ocr.txt` (OCR `ara`) ;
- `nc13_2026.pdf` et `nc13img/p-*.png` (images relues) ;
- `lf2023jib.pdf` (fac-similé de l'édition française du JORT n° 141/2022) et `lf2023jib.txt` ;
- `Jo1052013.txt`, `Jo0682014.txt`, `Ja1052013.txt.nfkc`, `Ja0682014.txt.nfkc`.

Aucun processus OCR ne reste en cours.

Sources web consultées :
- https://jibaya.tn/docs-category/notes-communes/
- https://jibaya.tn/docs/loi-de-finances-2023/
- https://www.lapresse.tn/2025/11/24/impot-sur-la-fortune-voici-pourquoi-le-parlement-a-dit-non/
- https://www.lapresse.tn/2025/12/01/parlement-larticle-50-sur-limpot-sur-la-fortune-supprime/ (titre seul, via recherche)
- https://www.lapresse.tn/2025/12/05/limpot-sur-la-fortune-officiellement-adopte/ (titre seul, via recherche)
- https://www.ey.com/en_tn/insights/publication/impot-sur-la-fortune-immobiliere (presse et cabinets, secondaire, non utilisés pour les faits)
