# Compensation, « Les produits de base » depuis 1992 : prix au public, ciblage, série par produit et bénéficiaires de l'écart

Note documentaire du 18 novembre 2026 (rôle documentaliste). Objet : trois lacunes du chapitre
`precis/fr/compensation/_produits_base.qmd` :

- (a) les prix au public des produits subventionnés depuis 1992 ;
- (b) le ciblage des subventions et les transferts de substitution, 2013-2026 ;
- (c) la série budgétaire par produit après 2011, et les bénéficiaires de l'écart entre le poste
  « produits de base » et les transferts à l'Office des céréales et à l'ONH.

Les sources lues sont presque toutes déjà dans `~/projets/tunisia-data` ; aucun PDF nouveau n'a été
téléchargé. Les pages sont des **pages imprimées**. Vues à l'image : Cour des comptes 2016,
pp. 2, 9, 10, 11, 26, 27, 29 ; rapports de clôture (pages des tableaux) ; PAP 2018, 2019, 2022 ;
budgets de mission (pages des tableaux) ; rapports sur le budget 2022 (p. 49), 2023 (pp. 61-62),
2024 (p. 78), 2025 (pp. 22, 80). Les autres pages sont lues en couche texte et calées sur le numéro
imprimé voisin : elles sont marquées « couche texte ». Dans les PDF arabes, la couche texte altère les chiffres (exemple : PAP 2018, « 61 » dans le texte pour
36 à l'image). Les chiffres retenus ont été relus à l'image ou contrôlés par l'addition des tableaux.

## Ce qui change pour le chapitre, en bref

1. **(c) est résolu.** Les rapports de la Cour des comptes sur la clôture du budget donnent la
   dépense **payée** de compensation des produits de base, **par produit**, chaque année de 2011 à
   2024. La ligne « céréales » est égale, au millier de dinars près, au transfert versé à l'Office des
   céréales, et la ligne « huile végétale » à celui versé à l'ONH. L'écart de 2018 à 2023 est donc,
   à 0,1 MD près, la somme des autres lignes :
   - le lait demi-écrémé (versé aux centrales laitières, selon la Cour des comptes pour 2011-2014) ;
   - les pâtes et le couscous ;
   - le papier scolaire ;
   - le sucre (Office du commerce) ;
   - la viande (Société des viandes, 2018, 2019 et 2021).

   Seule exception, 2019 : 7,0 MD restent sans attribution, parce que la colonne « 2019 » de la BCT
   donne 1 800 MD (crédit de la loi de finances) et non le payé, 1 792,554 MD. L'écart va de
   191,3 MD (2022) à 307,0 MD (2019) ; le « 181 » de la TODO du chapitre est une coquille, et
   `_transferts.qmd` dit bien 191.
2. **(a) : on connaît l'acte qui fixe les prix depuis 1992, pas une série de prix.** C'est une
   **décision du ministre chargé du commerce** (مقرر), non publiée au JORT. La Cour des comptes en
   cite plusieurs, de 2011 à 2014 ; la baisse des prix au public du 14 janvier 2011 est, elle, un
   « قرار » sans auteur ni numéro, absent du JORT. Pour 2010, une étude reprend les prix de vente que lui a donnés le
   ministère du Commerce (dix produits). En janvier 2011, une décision baisse les prix au public de
   plusieurs produits.
3. **(b) : il y a des documents budgétaires, mais toujours pas de texte d'organisation.**
   - Le rapport sur le budget de l'État pour 2022 présente les crédits comme pris « في انتظار إرساء
     منظومة الدعم المباشر لفائدة الفئات الاجتماعية المستحقة » (dans l'attente de la mise en place du
     système de subvention directe aux catégories sociales qui y ont droit).
   - Le rapport pour 2023 annonce un « برنامج إصلاحي شامل لمنظومة الدعم » (programme de réforme
     globale du système de subvention) et une plateforme électronique d'inscription des ménages. Il
     inscrit 697 MD de transferts directs et 585 MD de « transferts aux familles au titre de la
     subvention » en dépenses imprévues.
   - La dépense payée en 2023 pour les produits de base reste de 3 809,5 MD, contre 2 523 MD inscrits
     en loi de finances.

---

## (a) Les prix au public après 1991

### Faits établis

**L'instrument : une décision du ministre chargé du commerce.** Famille : contrôle (Cour des
comptes). Source : Cour des comptes, « منظومة دعم المواد الأساسية » (le système de subvention des
produits de base), 56 p., contrôle de la période 2009-2014, mis en ligne le 15 juin 2016 selon le
catalogue du site.

- **p. 9 : la baisse de janvier 2011.** L'acte est appelé « قرار », sans auteur ni numéro. Aucun
  texte signé du 13 au 15 janvier 2011 sur les prix ne figure dans `jort_cache` (requête par date de
  signature, langue indifférente : quatre textes ces jours-là, aucun sur les prix ; aucun texte de
  prix publié de janvier à mars 2011 hormis le décret de campagne n° 2011-325). « وصدر في 14 جانفي 2011 قرار يقضي بتخفيض أسعار البيع للعموم
  لمشتقات الحبوب والحليب المعقّم نصف الدسم والسكر ومعجون الطماطم وتحميل ميزانية الدولة الانعكاسات
  المالية الناتجة عن هذا القرار » (une décision est intervenue le 14 janvier 2011 pour baisser les
  prix de vente au public des dérivés des céréales, du lait stérilisé demi-écrémé, du sucre et du
  concentré de tomate, le budget de l'État prenant en charge le coût).
  - **Les primes forfaitaires qui en découlent** : 50 millimes/kg pour le sucre ; 20 millimes/kg pour
    les pâtes et le couscous ; 50 à 60 millimes/litre pour le lait ; 70 à 100 millimes par boîte de
    concentré de tomate.
  - **Le concentré de tomate** : son prix est fixé par la « décision du ministre chargé du commerce
    n° 3 de 2011 », qui le soumet à l'homologation administrative. La Cour des comptes juge cette
    décision contraire au décret n° 1996 de 1991, qui soumet ce produit à l'autohomologation. Elle
    juge aussi contraire à la loi n° 91-64, art. 4 (note 4), l'application de cette décision
    exceptionnelle au-delà de six mois. Subvention indue du 1er août 2011 au 31 décembre 2013, « تاريخ
    إعادة ضبط هوامش ربحها وإخراجها من الدّعم » (date de la refixation de ses marges et de sa sortie de
    la subvention) : 28,273 MD. Cette sortie concorde avec le « – » de 2014 au tableau de (c).
  - **Note 3 de la même page** : les marges de distribution sont fixées « بمقرر من الوزير المكلّف
    بالتجارة » (par décision du ministre chargé du commerce).
- **p. 26 : les pâtes.** La « décision n° 05 du ministre chargé du commerce du 14 janvier 2011 »
  fixe des prix par type de pâtes. Des pâtes hors de sa liste sont subventionnées et vendues
  0,430 D les 500 g au lieu de 0,410 D, sur la seule foi d'une lettre de l'administration à la chambre
  syndicale des fabricants du 20 janvier 2011. Surcoût pour une usine en 2013 : 67,459 milliers de
  dinars (p. 27).
- **p. 27 : le lait.** À la suite de la baisse du prix de vente au public des laits à partir de
  2011, la prime versée aux centrales laitières est de 60 millimes/litre pour les briques d'un litre
  et les bouteilles trois couches, et de 50 millimes/litre pour les bouteilles d'un litre. Elle est
  payée sur le budget du ministère du Commerce, selon les ventes de lait stérilisé demi-écrémé, à
  compter du 14 janvier 2011.
  - Note 1 de la même page : « à partir du 25 octobre 2012 », 110 millimes/litre pour les bouteilles
    d'un litre et 120 millimes/litre pour les briques d'un litre et les bouteilles trois couches.
- **pp. 10-11 : la farine.**
  - Prix de vente de la farine panifiable : 6,089 D le quintal aux boulangeries de catégorie A et
    22,668 D le quintal à celles de catégorie C. Farine de luxe (« الرفيعة ») : 51,200 D le quintal.
  - L'écart entre farine de luxe et farine panifiable « est monté le 5 mars 2013 à 45,111 D »
    (51,200 − 6,089 : un écart, pas un prix).
  - La farine destinée au petit pain est entrée dans la subvention « إثر مراجعة هيكلة أسعار الفرينة
    والسميد بتاريخ 05 مارس 2013 » (à la suite de la révision de la structure des prix de la farine
    et de la semoule du 5 mars 2013).
  - Note 1 de la p. 10 : le barème d'agréage des blés est fixé par « الأمر » (décret) du 18 juin
    2007, modifié par « الأمر عدد 621 لسنة 2012 ». Identifié dans `jort_cache` : décret n° 2012-621 du
    13 juin 2012, modifiant le décret n° 2007-1401 du 18 juin 2007 relatif à la détermination du
    barème d'agréage du blé dur et du blé tendre (JORT n° 47 du 15 juin 2012). URL pist.tn à relever.
- **p. 11 : l'usage industriel.** Le sucre vendu aux industriels jusqu'au 1er juillet 2014 et la farine
  de luxe ne couvrent pas leur coût réel. Avantage dont les industriels ont bénéficié en 2013 :
  environ 134 MD pour la farine de luxe et 11 MD pour le sucre.

**Les prix de vente de 2010.** Famille : évaluation économique ; les prix sont relayés depuis le
ministère du Commerce. Source : INS, CRES et BAD, *Analyse de l'impact des subventions alimentaires
et des programmes d'assistance sociale sur la population pauvre et vulnérable*, 2013, tableau 2,
p. 12, « Source : Ministère du Commerce ». Unités : millimes l'unité de vente.

| Produit | Prix de vente | Prix de revient | Subvention | Part du prix de revient |
|---|---:|---:|---:|---:|
| Gros pain (400 g) | 230 | 430 | 200 | 46,5 % |
| Baguette (220 g) | 190 | 272 | 82 | 30,1 % |
| Semoule (kg) | 450 | 1 030 | 580 | 56,3 % |
| Farine (kg) | 630 | 1 190 | 560 | 47,1 % |
| Tomate industrielle (800 g) | 1 600 | 1 670 | 70 | 4,2 % |
| Lait demi-écrémé (litre) | 970 | 1 020 | 50 | 4,9 % |
| Couscous (kg) | 795 | 1 415 | 620 | 43,8 % |
| Pâtes alimentaires (kg) | 805 | 1 425 | 620 | 43,5 % |
| Huile de graines (litre) | 900 | 1 800 | 900 | 50,0 % |
| Sucre (kg) | 970 | 1 420 | 450 | 31,7 % |

- **Unités.** Elles sont données par la version provisoire BAD-CRES du 30 mars 2013, tableau 2.1
  (kg, litre, 800 g) ; les valeurs sont identiques.
- **Le poids du pain.** Le tableau donne déjà 400 g et 220 g en 2010, alors que le dernier texte
  publié de poids est de 1991 (500 g et 250 g) et que l'arrêté du 22 juin 2016 fixe 400 g et 220 g.
  Le changement de poids entre 1991 et 2010 n'est pas daté par un texte : voir les lacunes.
- **Méthode** de l'étude, déjà relevée dans `compensation-etudes-incidence-calculs.md`, § D :
  enquête budget-consommation de 2010 ; subvention unitaire = prix de revient − prix de vente.
- **Même p. 12, l'exclusion de 1996.** « En 1996, et dans le cadre de l'assainissement de la
  situation financière de la caisse générale de compensation, et afin de mieux cibler la
  compensation vers les catégories des ménages à revenu faible, des produits alimentaires profitant
  le moins à ces catégories ont été exclus du champ d'intervention direct du système de compensation
  (sucre en morceaux, aliment de bétail, huile acide, viande, engrais). » La phrase est reconstituée
  à partir d'une mise en page à deux colonnes : à relire à l'image avant citation. Elle sert la TODO
  de la l. 125 du chapitre (sorties du champ de 1992-1999).

**Le prix réduit du blé aux minoteries, 2009-2020.** Famille : données de l'opérateur (Office des
céréales, portail de données ouvertes du ministère de l'Agriculture). Prix « de vente subventionné »,
en dinars le quintal, mensuels :

- **blé dur** : 28,350 (début 2009) → 28,102 → 27,917 → 29,782 (août 2010) → 27,711 (février 2011) →
  27,603 (2012) → **27,014 depuis mars 2013**, inchangé jusqu'en décembre 2020 ;
- **blé tendre** : 27,123 (2009) → 24,754 → 22,522 → 26,815 (août 2010) → 22,515 (février 2011) →
  20,413 → **20,049 depuis juin 2012**, inchangé jusqu'en décembre 2020.

Fichiers : `data/raw/ministeres-tutelle/agriculture/agridata/OC/evolution-du-prix-de-vente-subventionne-du-ble-dur-en-dinar-__fb2d08e9.xlsx`
(sha256 `2a059bacc8e7145afeb232fee8377da617226e212648fa009fb9e828f5c63481`) et
`…ble-tendre-en-din__489f7de3.xlsx` (sha256
`e784de7f680826d2854128d4ff35ac596d532be779f14953630e83e5e4d923c2`). Adresses dans
`agriculture/agridata_telechargements.tsv` (collecte du 4 novembre 2026).

- **La fiche `r-oc-prix-reduits-retrocession` est concernée.** Les valeurs sont celles de l'Office ;
  les décisions du ministre qui les fixent restent non identifiées. On peut s'en servir comme
  **approximation sourcée** (voir les lacunes).
- **Concordance avec la Cour des comptes**, p. 10 : la farine de petit pain entre dans la
  subvention le 5 mars 2013 ; le blé dur passe à 27,014 D en mars 2013.

**L'huile.** La Cour des comptes, p. 12 (couche texte), mentionne que l'ONH revend l'huile raffinée aux
conditionneurs « بسعر إحالة يضبط بمقرر من الوزير المكلّف بالتجارة » (à un prix de cession fixé par
décision du ministre chargé du commerce). Le prix au public n'est pas donné.

### Ce que cela établit pour la fiche `r-comp-pb-prix-consommateur-apres-1991`

- **L'acte.** Depuis 1992, les prix homologués du tableau A du décret n° 91-1996 et les marges
  sont fixés par **décision (مقرر) du ministre chargé du commerce**. Ces décisions ne paraissent pas
  dans la partie « décrets et arrêtés » du JORT. Décisions nommées par la Cour des comptes : n° 05
  du 14 janvier 2011 (pâtes), n° 3 de 2011 (concentré de tomate), décision du 19 novembre 2014
  (huile, ratio de raffinage ; p. 22, couche texte). À part : l'acte (« قرار ») du 14 janvier 2011
  qui baisse les prix au public, sans auteur ni numéro, absent de `jort_cache`.
- **Le résultat pour le JORT reste « aucun ».** La suite de la recherche relève de la base
  législative (texte non publié, archivé avec l'émetteur) ou d'une demande au ministère du Commerce,
  plus de nouvelles requêtes au JORT.

---

## (b) Ciblage et transferts de substitution, 2013-2026

### Faits établis, famille budgétaire (ministère des Finances)

- **Rapport sur le budget de l'État pour 2022** (décembre 2021), clé existante
  `minfin-rapport-budget-2022`.
  - p. 21 (couche texte), § 8, « إصلاح منظومة الدعم » (réforme du système de subvention) : réécrire les politiques
    de subvention et les mécanismes de compensation « لمساندة الأسر والحفاظ على المقدرة الشرائيّة
    والسّلم الاجتماعي » (pour soutenir les familles et préserver le pouvoir d'achat et la paix
    sociale). Les mesures citées portent sur l'énergie : ajustement automatique des carburants et de
    l'électricité.
  - p. 49 : crédits de 3 771 MD pour les produits de base en 2022, contre 2 200 MD en 2021 (le détail
    par produit est au tableau de (c)). Le montant « يأخذ بعين الاعتبار اقتصادا بحوالي 429م د في إطار
    اتخاذ تدابير جديدة قصد مزيد ترشيد دعم المواد الأساسية والتحكم فيه وتشديد المراقبة على مسالك
    التوزيع للحد من ظاهرة التهريب، وذلك في انتظار إرساء منظومة الدعم المباشر لفائدة الفئات
    الاجتماعية المستحقة » (tient compte d'une économie d'environ 429 MD, par de nouvelles mesures de
    rationalisation et de maîtrise de la subvention des produits de base et un contrôle renforcé des
    circuits de distribution contre la contrebande, dans l'attente de la mise en place du système de
    subvention directe aux catégories sociales qui y ont droit).
  - Le titre courant de l'édition est « تقرير حول ميزانية الدولة لسنة 2022 », sans « مشروع » (projet).
- **Rapport sur le budget de l'État pour 2023** (décembre 2022, mis en ligne en janvier 2023), clé
  existante `minfin-rapport-budget-2023`. Copie locale :
  `data/raw/gbo-recup-2026-11-04/annexes-lf/2023-01_0002_0.pdf`, sha256
  `cbde5d110335b73c32185b3894dc8f1149c4426efd04ec14b89eab7783875d82`.
  - **p. 38** (couche texte) : 8 832 MD pour les subventions, contre 11 999 MD attendus en 2022 (− 3 167 MD). La
    baisse vient « أساسا الانطلاق في برنامج إصلاحي شامل لمنظومة الدعم يهدف إلى الحفاظ على مكسب الدعم
    كخيار ثابت … وتحقيق العدالة الاجتماعية من خلال توجيه الدعم إلى مستحقيه ومقاومة الفقر في إطار
    حماية خاصة للفئات المعوزة ومحدودة الدخل » (essentiellement du lancement d'un programme de réforme
    globale du système de subvention qui vise à garder la subvention comme choix permanent … et la
    justice sociale en orientant la subvention vers ceux qui y ont droit et en luttant contre la
    pauvreté, avec une protection particulière des catégories démunies et à revenu limité).
  - **p. 39** (couche texte) : « les autres dépenses d'intervention » augmentent de 1 682 MD, « جزء منها يعود بالأساس
    إلى التحويلات الاجتماعية التي سيقع تفعيلها ضمن برنامج إصلاح منظومة الدعم » (dont une partie tient
    aux transferts sociaux qui seront activés dans le programme de réforme du système de subvention).
  - **p. 52** (couche texte), « إصلاح منظومة الدعم » : la stratégie passe « خاصة عبر تركيز منصة الكترونية للانطلاق في
    تسجيل الأسر للانتفاع بالدعم » (notamment par la mise en place d'une plateforme électronique pour
    lancer l'inscription des ménages à la subvention).
  - **p. 61** : produits de base, 2 523 MD en 2023 contre 3 771 MD en 2022 ; « بالإضافة لهذا المبلغ تم
    ترسيم مبلغ 697م د بعنوان التحويلات المباشرة و 585م د ضمن النفقات الطارئة » (s'y ajoutent 697 MD
    de transferts directs et 585 MD en dépenses imprévues).
  - **p. 142** (couche texte) : les 585 MD de dépenses imprévues sont « التحويلات للعائلات بعنوان الدعم » (les
    transferts aux familles au titre de la subvention).
- **Rapport sur le budget de l'État pour 2024** (octobre 2023), clé `minfin-rapport-budget-2024`.
  - p. 35 (couche texte) : le projet de loi vise « إيجاد آليات بديلة لتمويل منظومة الدعم » (trouver d'autres moyens
    de financer le système de subvention).
  - p. 51 (couche texte) : contrôle des circuits, « وخاصة مشتقات الحبوب المدعمة » (surtout des dérivés subventionnés
    des céréales). Les produits de base font 31,7 % des subventions et 2 % du PIB en 2024, contre
    33,2 % et 2,4 % (actualisé 2023).
  - Aucune mention de transferts directs de substitution.
- **Rapport sur le budget de l'État pour 2025** (octobre 2024), clé `minfin-rapport-budget-2025`,
  p. 52 (couche texte) : « تحسين نجاعة منظومة الدعم من خلال ترشيد الاستهلاك وتعزيز مراقبة مسالك التوزيع » (améliorer
  l'efficacité du système par la rationalisation de la consommation et le contrôle des circuits). Ni
  ciblage par ménage, ni transfert.

### Faits établis, famille contrôle (Cour des comptes)

- **Rapport sur la clôture du budget de 2023**, p. 69 :
  - « شملت نفقات التدخلات الاعتيادية في سنة 2023 التحويلات الشهرية المباشرة لفائدة الأسر بعنوان
    الدعم، ضمن برنامج "الأمن الاجتماعي" بمبلغ 697م.د » (les dépenses d'intervention ordinaires de
    2023 comprennent les transferts mensuels directs aux familles au titre de la subvention, dans le
    programme « Sécurité sociale », pour 697 MD) ;
  - le passage renvoie au rapport sur le projet de budget 2023 : il s'agit du **crédit initial** ;
  - la couche texte de ce rapport est lacunaire (lettres manquantes) : citation à reprendre à
    l'image ;
  - **l'exécution de ces 697 MD n'est pas établie** dans cette passe.
  - Pour les produits de base, la même série donne 3 809,5 MD payés en 2023 contre 2 523 MD
    initiaux (rapport de clôture 2024, p. 73 ; (c) ci-dessous).
- **Rapport « منظومة دعم المواد الأساسية »** (2016), p. 11 : les plans de développement ont insisté
  sur l'orientation de la subvention vers ceux qui y ont droit, mais « تحديد الفئة المستهدفة بهذا الدعم
  اتّسم بعدم الوضوح في ظل النظام الحالي لتعويض المواد الأساسية، حيث يتمّ توجيه الدعم لفائدة كل الفئات
  الاجتماعية عوض حصره لفائدة الفئات المستحقة » (la cible n'est pas définie dans le système actuel : la
  subvention va à toutes les catégories sociales au lieu d'être réservée à celles qui y ont droit).
  - Note 3 de la même page : au Maroc, la subvention passe par une aide financière directe et
    conditionnée aux catégories pauvres.
  - Le budget économique de 2010 insistait déjà sur la limitation de la subvention à la consommation
    des ménages.
  - p. 10 : les orientations adoptées sur la base de l'enquête sur les boulangeries de 2008
    prévoyaient de réserver la subvention au gros pain, de rapprocher le prix de la farine panifiable
    de celui de la farine de luxe et de verser la compensation aux boulangeries. Fin octobre 2014,
    ces orientations n'étaient pas appliquées.

### Faits établis, famille rapports extérieurs (FMI)

- **FMI, demande d'accord de confirmation**, IMF Country Report n° 13/161, juin 2013, p. 25 (couche
  texte, numéro imprimé du pied de page) : « As
  for food subsidy reform, given the importance of food subsidies for poorer households and despite
  existing leakages (e.g., to hotels or industry), the government will assess at a later stage how
  to reform these, and may be able to use lessons from the energy subsidy reform to design
  compensatory measures. »
  - Copie locale : `data/raw/banque-mondiale-rapports/imf_2013_161_sba_request_tunisia.pdf`, sha256
    `331281f5925dcd6cac7382ee853260bc8297a56db7d86819ec2c9256f4989a23`, identique au fichier de
    `https://www.imf.org/external/pubs/ft/scr/2013/cr13161.pdf` (vérifié le 18 novembre 2026). Pas de
    clé ; pas de ligne au catalogue `sources/`.
- **FMI, communiqué n° 22/353 du 15 octobre 2022** (accord au niveau des services, mécanisme élargi
  de crédit d'environ 1,9 milliard de dollars) : les autorités ont « started to gradually phase out
  generalized wasteful price subsidies through regular price adjustments that link domestic prices
  to international prices, while providing adequate targeted protection to vulnerable segments
  (including through social transfers) ».
  - Le texte porte sur les subventions **généralisées**, sans distinguer l'alimentaire.
  - Lu en ligne le 18 novembre 2026. Copie non archivée : le téléchargement a été refusé par
    l'environnement d'exécution ; à archiver.
- **Ne pas citer pour l'alimentaire** : FMI 2016 (CR 16/138, p. 17) et FMI 2021 (CR 21/44, p. 18),
  qui parlent de transferts monétaires en contrepartie des subventions à l'**énergie**.

### Texte d'organisation

Aucun décret, arrêté ou article de loi de finances qui organise le ciblage des subventions aux
produits de base, la plateforme d'inscription ou les transferts mensuels de 2023 n'a été repéré dans
les documents lus. Le crédit de 697 MD relève de la loi de finances pour 2023 (décret-loi de
décembre 2022) ; l'article ou le tableau qui l'inscrit reste à lire. La fiche reste « aucun » pour
les textes (passe ci-dessous).

---

## (c) Série par produit après 2011 et bénéficiaires de l'écart

### 1. La dépense payée par produit, 2011-2024

Famille : budgétaire (exécution du budget, relevée par la Cour des comptes). Ces chiffres égalent
le poste budgétaire du chapitre en 2011-2014 et 2017-2024 et peuvent figurer à côté de lui. « الاعتمادات المأمور بصرفها » :
crédits ordonnancés, puis « نفقات … التي تمّ صرفها » : dépenses payées par le ministère du Commerce.
Millions de dinars courants. Chaque tableau a été relu à l'image, et les additions tombent juste à
0,001 MD près. Les rapports 2011-2014 disent « ordonnancé », le rapport 2018 « payé » ; ils donnent les
mêmes valeurs pour 2014.

| Produit | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Céréales | 833,673 | 908,947 | 1 117,936 | 1 123,778 | 1 253,119 | 1 236,919 | 1 104,329 | 1 305,754 | 1 284,436 | 1 848,475 | 1 674,154 | 3 220,944 | 3 344,168 | 2 993,300 |
| Huile végétale | 214,383 | 264,381 | 232,163 | 206,488 | 167,899 | 199,934 | 247,882 | 249,151 | 208,096 | 268,951 | 301,383 | 358,795 | 165,355 | 92,306 |
| Lait | 23,066 | 31,928 | 57,107 | 61,737 | 63,911 | 63,478 | 87,969 | 134,177 | 189,617 | 209,071 | 161,843 | 138,076 | 156,847 | 350,700 |
| Pâtes et couscous | 4,185 | 4,804 | 16,359 | 12,506 | 31,825 | 47,195 | 39,824 | 44,726 | 88,640 | 73,505 | 44,309 | 35,097 | 110,298 | 122,707 |
| Sucre | 10,840 | 10,435 | 9,685 | 9,342 | 8,946 | 10,131 | 9,854 | 8,867 | 9,088 | 9,876 | 9,353 | 9,357 | 5,870 | 5,379 |
| Papier scolaire | 4,300 | 4,344 | 4,321 | 2,821 | 4,300 | 3,884 | 3,897 | 2,703 | 10,320 | 6,122 | 8,704 | 8,732 | 26,962 | 37,108 |
| Tomate | 9,553 | 10,794 | 12,429 | – | | | | | | | | | | |
| Viande | | | | | – | – | – | 4,622 | 2,356 | – | 0,254 | – | – | – |
| **Total** | 1 100,000 | 1 235,633 | 1 450,000 | 1 416,672 | 1 530,000 | 1 561,541 | 1 493,755 | 1 750,000 | 1 792,554 | 2 416,000 | 2 200,000 | 3 771,000 | 3 809,500 | 3 601,500 |

**Sources** (Cour des comptes, « تقرير عن غلق ميزانية الدولة », toutes déjà en clé `cdc-cloture-*`
dans `precis/fr/entreprises_publiques/references.json`) :

| Années du tableau | Rapport | Page | Clé | sha256 |
|---|---|---|---|---|
| 2011-2013 | clôture 2013 | p. 76 | `cdc-cloture-2013` | `9fc00e9f…a168b` |
| 2012-2014 | clôture 2014 | p. 80 | `cdc-cloture-2014` | `52f41e23…a5d3` |
| 2014-2018 | clôture 2018 | p. 90 | `cdc-cloture-2018` | `0dfeeed1…6eb3` |
| 2017-2020 | clôture 2020 | p. 78 | `cdc-cloture-2020` | `8769b805…0146` |
| 2020-2024 | clôture 2024 | p. 73 | `cdc-cloture-2024` | sha256 au catalogue `cour-des-comptes-telechargements.csv` |

Les années qui se chevauchent concordent d'un rapport à l'autre.

**Écarts avec la série du chapitre** (`fig_compensation_par_poste.csv`) :

| Année | Chapitre | Cour des comptes | Écart | Source du chapitre |
|---|---:|---:|---:|---|
| 2015 | 1 549,0 | 1 530,000 | − 19,0 | note du ministère des Finances, fin 2018, « نتائج » |
| 2016 | 1 580,7 | 1 561,541 | − 19,2 | même note |
| 2019 | 1 800 | 1 792,554 | − 7,4 | BCT, colonne non qualifiée ; 1 800 est le crédit de la loi de finances |

- **2011-2014 et 2017-2024 : égalité.** La colonne « non qualifiée » de la BCT pour 2020-2023 est
  donc un payé.
- **Indice pour 2015** : 1 530,000 est aussi le crédit de la LFC 2015 (`fig_compensation_prevu_realise.csv`).
  C'est un indice, pas une conclusion.
- **Rupture de 2011 avec la série BCT 1985-2011** (`fig_compensation_par_produit.csv`, rapport BCT
  2011, p. 45) : huile, lait, sucre, papier, pâtes et tomate égaux à 0,1 MD près ; **céréales
  883,2 (BCT) contre 833,673 (Cour des comptes)** ; total 1 149,6 contre 1 100,0. La BCT exclut
  « un montant budgétisé de 96,7 MDT reporté à l'année 2012 au profit de l'Office des céréales ».
  Les deux séries ne se raccordent pas en silence : la jonction de 2011 est une rupture à dire.
- **Il faut trancher entre les deux familles budgétaires pour 2015 et 2016.** La Cour des comptes
  fait le payé du ministère du Commerce ; le ministère des Finances fait les résultats d'exécution,
  peut-être tous ministères confondus. À trancher par le rédacteur, et à noter en concordance.
- **Les autres lectures de la Cour des comptes**, en commentaire du tableau :
  - **2021** : la baisse des céréales s'explique « خاصة بانخفاض حجم الكميات المدعمة لمادة الفارينة »
    (surtout par la baisse des quantités subventionnées de farine) — clôture 2021, ligne de commentaire
    lue en couche texte, à paginer ;
  - **2024** : baisse des céréales (− 350,868 MD) et de l'huile (− 73,049 MD), hausse du lait
    (+ 193,853 MD) ; blé dur importé à 391 dollars la tonne en moyenne en 2024, contre 457 en 2023
    et 624 en 2022 (clôture 2024, p. 73) ;
  - **2024** : le secteur laitier reçoit en outre 96 MD sur la mission Agriculture (aide à la collecte
    du lait). C'est une aide à la production, hors compensation (même page).

### 2. Les crédits de loi de finances par produit, 2018-2025

Famille : budgétaire. Ces chiffres sont des **crédits**, jamais des payés.

| Produit | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Céréales | 1 200 | 1 325 | 1 309 | 1 804 | 3 025 | 1 736 | 2 446 | 2 674 |
| Huile végétale | 250 | 240 | 217 | 290 | 480 | 400 | 380 | 375 |
| Lait | 70 | 180 | 189 | 205 | 160 | 232 | 524 | 524 |
| Pâtes et couscous | 36 | 40 | 70 | 86 | 86 | 110 | 190 | 190 |
| Sucre | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| Papier scolaire | 4 | 5 | 5 | 5 | 10 | 35 | 41 | 28 |
| **Total** | 1 570 | 1 800 | 1 800 | 2 400 | 3 771 | 2 523 | 3 591 | 3 801 |
| État | projet (PAP) | projet (PAP) | projet | projet | loi de finances | loi de finances | projet = LF | projet |

**Où chaque colonne a été lue.** PAP = projet annuel de performance de la mission Commerce ;
« budget de mission » = document du ministère des Finances « ميزانية الدولة لسنة … — مهمة التجارة »,
tableau par article et paragraphe (« 302-01 دعم المواد الأساسية », paragraphes 001 à 005, et
« 302-02 دعم منتوجات أخرى », 001 papier).

| Année | Lecture principale | Concordances et remarques |
|---|---|---|
| 2018 | PAP 2018, pp. 5-6 | 1 570 MD contre 1 600 MD en loi de finances 2017 ; lu à l'image |
| 2019 | PAP 2019, p. 6 | 1 800 contre 1 570 en LF 2018 ; lu à l'image |
| 2020 | budget de mission 2020 (octobre 2019), p. 184 | PAP 2020 (version française), p. 8, mêmes valeurs ; le PAP imprime « 2,77 % » pour 72,7 % |
| 2021 | budget de mission 2021 (octobre 2020), p. 182 | PAP 2021 français, p. 10. La loi de finances 2021 vote 2 200 MD (PAP 2022 français, p. 10 ; rapport budget 2022, p. 49). La loi de finances 2021 du rapport sur les transferts donne l'OC à 1 604 et l'ONH à 290 : la coupe de 200 MD porte sur les céréales |
| 2022 | budget de mission 2022 (décembre 2021), p. 181 | rapport budget 2022, p. 49 ; PAP 2022, p. 10 |
| 2023 | budget de mission 2023 (décembre 2022), p. 181 | rapport budget 2023, p. 62 |
| 2024 | budget de mission 2024 (octobre 2023), p. 183 | rapport budget 2024, p. 78 ; la Cour des comptes confirme 3 591 MD initiaux et 10,5 MD complémentaires (clôture 2024, p. 73) |
| 2025 | rapport budget 2025, p. 80 | le budget de mission 2025 (octobre 2024, p. 185) met les 3 801 MD sur la seule ligne 001 « دعم الحبوب », vu à l'image |

**Incohérences internes à signaler**, sans les corriger dans le texte :

- **Le narratif des budgets de mission recopie la ventilation de 2019** (1 325 / 240 / 180 / 40 /
  10 / 5 = 1 800) : à la p. 13 du budget 2020, pour les « mêmes crédits que 2019 », ce qui est juste ;
  à la p. 32 du budget 2021, pour 2 400 MD, ce qui est faux, la somme faisant 1 800. Les tableaux
  par article font foi.
- **La loi de finances 2021** : 2 400 MD au budget de mission (projet) contre 2 200 MD votés.

### 3. Qui reçoit quoi : les bénéficiaires de l'écart

- **Céréales → Office des céréales.** Égalité du payé de la Cour des comptes et du transfert à l'OC
  du rapport sur les transferts (annexe 8) : 2018 1 305,754 ; 2020 1 848,475 ; 2021 1 674,154 ;
  2022 3 220,944 ; 2023 3 344,167 MD. En 2019 : 1 284,436 contre 1 285,000. En loi de finances,
  l'annexe 8 donne pour l'OC exactement le crédit « céréales » : 3 025 (2022), 1 736 (2023),
  2 446 (2024). Transcription `tunisia-data/sources/transcriptions/minfin-transferts-par-etablissement.csv`.
  - Le PAP 2024, p. 31, précise que les estimations de subvention tiennent compte « مستحقات المطاحن
    والمخابز بعنوان الزيادة في تكاليف الإنتاج » (des sommes dues aux minoteries et aux boulangeries
    au titre de la hausse des coûts de production). Ces sommes passent donc par la ligne céréales.
- **Huile végétale → ONH.** Égalité : 249,151 (2018) ; 268,951 (2020) ; 301,383 (2021) ;
  358,795/358,794 (2022) ; 165,355/165,300 (2023). Crédits : 480 (2022), 400 (2023), 380 (2024).
- **Lait → centrales laitières.** Prime « لفائدة مركزيات الحليب حسب مبيعاتها من الحليب الطازج
  المعقّم نصف الدسم » (aux centrales laitières selon leurs ventes de lait frais stérilisé demi-écrémé),
  sur le budget du ministère du Commerce (Cour des comptes 2016, p. 27). Elles sont absentes de
  l'annexe 8. Le rapport couvre 2009-2014 : aucune source lue ne nomme le bénéficiaire après 2014.
- **Pâtes et couscous → fabricants.** Prime forfaitaire de 20 millimes/kg depuis le 14 janvier 2011
  (Cour des comptes 2016, p. 9 ; « أحد المصانع », p. 27). Absents de l'annexe 8. Même réserve : aucune
  source lue ne les nomme après 2014.
- **Sucre → Office du commerce de la Tunisie (OCT).**
  - L'OCT supporte « الفارق بين الكلفة الحقيقية لشراء السكر وسعر بيعه » (l'écart entre le coût
    réel d'achat du sucre et son prix de vente) : 28 MD de charges supplémentaires en 2013 (Cour des
    comptes 2016, p. 29).
  - Ce qu'il reçoit du budget est égal à la ligne sucre en 2021 (9,353), 2022 (9,356 contre 9,357)
    et 2023 (5,900 contre 5,870). Il reçoit plus en 2018 (11,199 contre 8,867) et en 2020 (14,328
    contre 9,876).
- **Viande → Société des viandes** : 4,623 (2018), 2,356 (2019), 0,254 (2021) ; égalité.
- **Papier scolaire → SNCPA, en partie.** SNCPA = 2,703 en 2018, égal à la ligne papier. Ensuite,
  3,555 contre 10,320 (2019), 0,061 contre 6,122 (2020), 0,142 contre 8,704 (2021), rien contre
  8,7 à 37,1 (2022-2023). **Le bénéficiaire du reste du papier scolaire n'est pas établi.**

**Rapprochement de l'écart** (MD ; poste = `fig_compensation_par_poste.csv` ; OC + ONH =
`minfin-transferts-par-etablissement`) :

| Année | Poste | OC + ONH | Écart | Lait + pâtes + sucre + papier + viande (Cour des comptes) | Reste |
|---|---:|---:|---:|---:|---:|
| 2018 | 1 750,0 | 1 554,9 | 195,1 | 195,095 | 0,0 |
| 2019 | 1 800,0 | 1 493,0 | 307,0 | 300,021 | 7,0 = + 7,4 (poste : crédit 1 800 au lieu du payé 1 792,554) − 0,6 (OC : 1 285,000 en annexe 8 contre 1 284,436) + 0,1 (ONH : 208,000 contre 208,096) |
| 2020 | 2 416,0 | 2 117,4 | 298,6 | 298,574 | 0,0 |
| 2021 | 2 200,0 | 1 975,5 | 224,5 | 224,463 | 0,0 |
| 2022 | 3 771,0 | 3 579,7 | 191,3 | 191,262 | 0,0 |
| 2023 | 3 809,5 | 3 509,5 | 300,0 | 299,977 | 0,0 |

### 4. Paiements hors du poste budgétaire : le compte « ن مكرر »

Rapport sur le budget de l'État pour 2025, p. 22 (exécution à fin août 2024) : « صرف مبلغ 561م د
بعنوان دعم المواد الأساسية … وذلك علاوة على مبلغ 825م د تم صرفه على حساب "ن مكرر" لديوان الحبوب
ومبلغ 117م د تم صرفه على حساب "ن مكرر" لديوان الزيت » (561 MD payés au titre de la subvention des
produits de base, en plus de 825 MD payés sur le compte « ن مكرر » à l'Office des céréales et de
117 MD à l'ONH).

- Les rapports de clôture nomment ce compte « أموال المؤسسات شبه الدولية (دفتر ن مكرر) » (fonds des
  établissements para-étatiques, carnet « ن مكرر ») : clôture 2021 et 2022, section des dépôts au
  Trésor, couche texte, page à relever.
- Le lien entre ces paiements et la dépense annuelle de compensation n'est pas établi ici : à
  documenter avant tout usage rédigé.

### 5. Données de l'opérateur : compensation des céréales par type, 2007-2025

Famille : données de l'opérateur (Office des céréales), à tenir séparées du budgétaire.

- **Fichier annuel 2007-2019**, `evolution-de-la-valeur-de-la-compensation-des-cereales-en-10__9fcd5f9e.xlsx`
  (sha256 `b3da23f1b7c823170c6b1a21faea8180645da99f1948f09bb30ee44854134af0`). Milliers de dinars, blé
  dur, blé tendre et orge, local et importé confondus ; puis janvier-juin 2020 et janvier-septembre
  2021, cette dernière colonne étant en dinars.
- **Fichier mensuel 2018-2025**, `valeur-mensuelle-de-la-compensation-des-cereales-par-type-en__49d1bd4e.xlsx`
  (sha256 `5f07e179bec097ba58e0b1ae520a8903418ef1872ed27417fa61fcca6c90bbd9`). Six colonnes : blé dur,
  blé tendre et orge, chacun local ou importé.
  - Unités : milliers de dinars pour 2018-2020, **dinars à partir de 2021**, sans le dire.
  - Mois manquants : juillet-décembre 2020, décembre 2023, novembre-décembre 2024.
- **Totaux annuels calculés ici** : 2018 1 353,7 ; 2019 1 759,8 ; 2022 3 686,5 ; 2025 2 178,0 MD.
- **Écart avec la ligne céréales payée** par la Cour des comptes (2018 : 1 305,8 ; 2019 : 1 284,4 ;
  2022 : 3 220,9). Le fichier de l'Office comprend l'orge. L'écart (2019 : 475 MD) n'est pas expliqué
  ici. À ne pas superposer sans le dire.
- **Seule série par produit après 2024 (opérateur).** C'est aussi la seule source qui distingue
  local et importé ainsi que l'orge.

---

## Références candidates

### Déjà présentes

À copier dans `precis/fr/compensation/references.json` en alignant la notice sur celle d'origine :

- `cdc-cloture-2013`, `cdc-cloture-2014`, `cdc-cloture-2018`, `cdc-cloture-2020`,
  `cdc-cloture-2024` : dans `precis/fr/entreprises_publiques/references.json`.
- `minfin-rapport-budget-2022`, `-2023`, `-2024`, `-2025` : dans `precis/fr/references.json`. Le
  titre de la notice 2022 et celui de la notice 2023 disent « مشروع » ; le titre courant des
  documents est « تقرير حول ميزانية الدولة لسنة … », versions votées de décembre. À vérifier par le
  bibliographe.
- `ins-cres-bad-2013-subventions` : dans `compensation/references.json`.
- `rap-2023-commerce` : dans `compensation/references.json`.
- `fmi-2016-cr16138` : dans `precis/fr/references.json`. `imf-tunisia-eff-2016`, dans
  `remunerations_publiques`, est le même rapport : doublon à signaler au bibliographe.
- `imf-tunisia-art4-2020` = CR 21/44.

### À créer

Absence vérifiée le 18 novembre 2026 dans `precis/*/references.json` et `precis/*/*/references.json`.

```json
[
  {"id": "cour-comptes-2016-subvention-produits-base", "type": "report",
   "title": "منظومة دعم المواد الأساسية (Le système de subvention des produits de base)",
   "author": [{"literal": "Tunisie. Cour des comptes"}], "publisher": "Cour des comptes",
   "publisher-place": "Tunis", "issued": {"date-parts": [[2016, 6, 15]]},
   "URL": "https://www.courdescomptes.nat.tn/wp-content/uploads/pdf_rapport/Rapport_82_2018-08-16-10-46-17.pdf",
   "note": "citation-key: cour-comptes-2016-subvention-produits-base\nRubrique 82, 56 p., contrôle 2009-2014 ; date = mise en ligne selon le catalogue du site. Copie locale tunisia-data/data/raw/cour-des-comptes/82/Rapport_82_2018-08-16-10-46-17.pdf, SHA-256 e281ab8b60781d5cbc5bfbb850fb92cec9d4f7f4269ffe6742eb7275f257cc95. Pages imprimées = page du fichier + 1."},
  {"id": "minfin-budget-mission-commerce-2020", "type": "report",
   "title": "ميزانية الدولة لسنة 2020 : مهمة التجارة (Budget de l'État pour 2020 : mission Commerce)",
   "author": [{"literal": "Tunisie. Ministère des finances"}], "issued": {"date-parts": [[2019, 10]]},
   "URL": "http://www.gbo.tn/sites/default/files/2021-03/%D9%85%D9%87%D9%85%D8%A9%20%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D8%A9_0.pdf",
   "note": "citation-key: minfin-budget-mission-commerce-2020\n216 p. ; SHA-256 421a67f57e2c5fa0c1989cb1ac0f54024c8828ac063f7c0378239445a28f807b ; catalogué à tort « LF2021 » dans gbo-recuperation-2026-11-04.csv."},
  {"id": "minfin-budget-mission-commerce-2021", "type": "report",
   "title": "ميزانية الدولة لسنة 2021 : مهمة التجارة وتنمية الصادرات",
   "author": [{"literal": "Tunisie. Ministère de l'économie, des finances et de l'appui à l'investissement"}],
   "issued": {"date-parts": [[2020, 10]]},
   "URL": "http://www.gbo.tn/sites/default/files/2022-09/%D9%85%D9%87%D9%85%D8%A9%20%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D8%A9%20%D9%88%D8%AA%D9%86%D9%85%D9%8A%D8%A9%20%D8%A7%D9%84%D8%B5%D8%A7%D8%AF%D8%B1%D8%A7%D8%AA2021.pdf",
   "note": "citation-key: minfin-budget-mission-commerce-2021\nSHA-256 b54256696bd795e9b3a3553c4a7a3b1adf1568366101384e61731ae1adc62a2f."},
  {"id": "minfin-budget-mission-commerce-2022", "type": "report",
   "title": "ميزانية الدولة لسنة 2022 : مهمة التجارة وتنمية الصادرات",
   "author": [{"literal": "Tunisie. Ministère des finances"}], "issued": {"date-parts": [[2021, 12]]},
   "URL": "http://www.gbo.tn/sites/default/files/2022-09/%D9%85%D9%87%D9%85%D8%A9%20%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D8%A9%20%D9%88%D8%AA%D9%86%D9%85%D9%8A%D8%A9%20%D8%A7%D9%84%D8%B5%D8%A7%D8%AF%D8%B1%D8%A7%D8%AA%202022.pdf",
   "note": "citation-key: minfin-budget-mission-commerce-2022\nSHA-256 6b4aa2a27c894f9f7a7e1572ecc7e270784616c796cd04a53976ef9767dc64a9."},
  {"id": "minfin-budget-mission-commerce-2023", "type": "report",
   "title": "ميزانية الدولة لسنة 2023 : مهمة التجارة وتنمية الصادرات",
   "author": [{"literal": "Tunisie. Ministère des finances"}], "issued": {"date-parts": [[2022, 12]]},
   "URL": "http://www.gbo.tn/sites/default/files/2023-01/2023%D9%85%D9%87%D9%85%D8%A9%20%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D8%A9%20%D9%88%D8%AA%D9%86%D9%85%D9%8A%D8%A9%20%D8%A7%D9%84%D8%B5%D9%80%D8%A7%D8%AF%D8%B1%D8%A7%D8%AA%20%2812023.pdf",
   "note": "citation-key: minfin-budget-mission-commerce-2023\nSHA-256 1014873db09aa4f2cc3286c89591e4d662facc75fec523b2456f47c46fe1d128."},
  {"id": "minfin-budget-mission-commerce-2024", "type": "report",
   "title": "ميزانية الدولة لسنة 2024 : مهمة التجارة وتنمية الصادرات",
   "author": [{"literal": "Tunisie. Ministère des finances"}], "issued": {"date-parts": [[2023, 10]]},
   "URL": "http://www.gbo.tn/sites/default/files/2024-01/15-%D9%85%D9%87%D9%85%D8%A9%20%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D8%A9%20%D9%88%20%D8%AA%D9%86%D9%85%D9%8A%D8%A9%20%D8%A7%D9%84%D8%B5%D8%A7%D8%AF%D8%B1%D8%A7%D8%AA.pdf",
   "note": "citation-key: minfin-budget-mission-commerce-2024\nSHA-256 524ca3eb8c7311f252842e2cff9b264e9e9f1191bb39fa970c0f65bc4ece393b."},
  {"id": "minfin-budget-mission-commerce-2025", "type": "report",
   "title": "ميزانية الدولة لسنة 2025 : مهمة التجارة وتنمية الصادرات",
   "author": [{"literal": "Tunisie. Ministère des finances"}], "issued": {"date-parts": [[2024, 10]]},
   "URL": "http://www.gbo.tn/sites/default/files/2025-03/15%20%D9%85%D9%87%D9%85%D8%A9%20%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D8%A9%20%D9%88%20%D8%AA%D9%86%D9%85%D9%8A%D8%A9%20%D8%A7%D9%84%D8%B5%D8%A7%D8%AF%D8%B1%D8%A7%D8%AA.pdf",
   "note": "citation-key: minfin-budget-mission-commerce-2025\nSHA-256 72db3ff1c7b9f7caa38124bd99ac971dfd6dba44c3bc4a85bedf101fcf9f3bd0."},
  {"id": "pap-2018-commerce", "type": "report", "title": "المشروع السنوي للقدرة على الأداء لمهمة التجارة لسنة 2018",
   "author": [{"literal": "Tunisie. Ministère du commerce"}], "issued": {"date-parts": [[2017]]},
   "URL": "http://www.gbo.tn/sites/default/files/2021-03/PAP%202018%20Commerce.pdf",
   "note": "citation-key: pap-2018-commerce\nSHA-256 52ab587004241c3b3c9de715e6db9e0a2917297b58acb3c4e3dd8a0bbf7a85ab."},
  {"id": "pap-2019-commerce", "type": "report", "title": "المشروع السنوي للأداء لمهمة التجارة لسنة 2019",
   "author": [{"literal": "Tunisie. Ministère du commerce"}], "issued": {"date-parts": [[2018]]},
   "URL": "http://www.gbo.tn/sites/default/files/2021-03/PAP%202019%20Commerce.pdf",
   "note": "citation-key: pap-2019-commerce\nSHA-256 91b6c0d6e4c84e0fa3af603759820abe495e3e8767ce6202487fe258e18675d8."},
  {"id": "pap-2022-commerce", "type": "report", "title": "Projet annuel de performance de la mission Commerce et développement des exportations, 2022",
   "author": [{"literal": "Tunisie. Ministère du commerce et du développement des exportations"}], "issued": {"date-parts": [[2021]]},
   "URL": "http://www.gbo.tn/sites/default/files/2022-03/PAPcommerce%202022%281%29.pdf",
   "note": "citation-key: pap-2022-commerce\nVersion française ; SHA-256 b75e4b01e626e2c037b84d39b98f8c82dd46ba0f9a3cf9ee837c343e96251b3d."},
  {"id": "pap-2024-commerce", "type": "report", "title": "المشروع السنوي للأداء لسنة 2024 : مهمة التجارة وتنمية الصادرات",
   "author": [{"literal": "Tunisie. Ministère du commerce et du développement des exportations"}], "issued": {"date-parts": [[2023, 10]]},
   "URL": "http://www.gbo.tn/sites/default/files/2024-01/PAP2024comernv.pdf",
   "note": "citation-key: pap-2024-commerce\nSHA-256 d174e04b0bfec185c94082144ea08cb4a5f1bcad4cda6f30f814663d069b91cf."},
  {"id": "oc-agridata-compensation-cereales", "type": "dataset",
   "title": "Valeur mensuelle de la compensation des céréales par type en 1000 dinars",
   "author": [{"literal": "Office des céréales"}], "publisher": "Ministère de l'Agriculture, portail agridata",
   "URL": "https://catalog.agridata.tn/dataset/cd33729f-b6a1-45fb-970f-48dc327acb6f",
   "accessed": {"date-parts": [[2026, 11, 4]]},
   "note": "citation-key: oc-agridata-compensation-cereales\nRessource 49d1bd4e ; SHA-256 5f07e179bec097ba58e0b1ae520a8903418ef1872ed27417fa61fcca6c90bbd9 ; unités mélangées (milliers de dinars 2018-2020, dinars depuis 2021)."},
  {"id": "oc-agridata-prix-vente-subventionne", "type": "dataset",
   "title": "Évolution du prix de vente subventionné du blé dur et du blé tendre en dinar le quintal",
   "author": [{"literal": "Office des céréales"}], "publisher": "Ministère de l'Agriculture, portail agridata",
   "URL": "https://catalog.agridata.tn/dataset/b1086522-7f57-4dcd-8923-fe2f5379b9f2",
   "accessed": {"date-parts": [[2026, 11, 4]]},
   "note": "citation-key: oc-agridata-prix-vente-subventionne\nBlé dur : ressource fb2d08e9 (SHA-256 2a059bac…3481) ; blé tendre : jeu 471c0362, ressource 489f7de3 (SHA-256 e784de7f…23c2). 2009-2020, mensuel."},
  {"id": "fmi-2013-cr13161", "type": "report",
   "title": "Tunisia: Request for a Stand-By Arrangement — Staff Report; Press Release on the Executive Board Discussion; and Statement by the Executive Director for Tunisia",
   "author": [{"literal": "Fonds monétaire international"}], "number": "IMF Country Report No. 13/161", "issued": {"date-parts": [[2013, 6]]},
   "URL": "https://www.imf.org/external/pubs/ft/scr/2013/cr13161.pdf",
   "note": "citation-key: fmi-2013-cr13161\nURL vérifiée le 18/11/2026 (fichier identique à la copie locale). Copie locale banque-mondiale-rapports/imf_2013_161_sba_request_tunisia.pdf, SHA-256 331281f5925dcd6cac7382ee853260bc8297a56db7d86819ec2c9256f4989a23 ; p. 25 (imprimée)."},
  {"id": "fmi-pr-22-353", "type": "webpage",
   "title": "IMF Staff Reaches Staff-Level Agreement on an Extended Fund Facility with Tunisia (Press Release No. 22/353)",
   "author": [{"literal": "Fonds monétaire international"}], "issued": {"date-parts": [[2022, 10, 15]]},
   "URL": "https://www.imf.org/en/News/Articles/2022/10/15/pr22353-tunisia-imf-staff-reaches-staff-level-agreement-on-an-extended-fund-facility-with-Tunisia",
   "accessed": {"date-parts": [[2026, 11, 18]]},
   "note": "citation-key: fmi-pr-22-353\nCopie non archivée (téléchargement refusé par l'environnement le 18/11/2026) : à archiver."}
]
```

`pap-2020-commerce` et `pap-2021-commerce` ne sont à créer que si le rédacteur cite le PAP plutôt
que le budget de mission. Adresses : `PAP_2020_Commerce.pdf` (sha256 `239f523d…6d0c`) et
`PAP 2021 Commerce et développement des exportations.pdf` (sha256 `fae3b199…159d`), dans
`gbo-recuperation-2026-11-04.csv`.

## Notions à glossaire

À vérifier dans `precis/glossaire.yml` :

- **décision du ministre** (مقرر) : acte non publié au JORT qui fixe les prix homologués et les
  marges. Source : Cour des comptes 2016, p. 9 (note 3), p. 26.
- **prime forfaitaire de compensation** (منحة جزافية) : sucre, pâtes, lait et tomate depuis 2011.
  Source : Cour des comptes 2016, p. 9.
- **centrale laitière** (مركزية الحليب) : bénéficiaire de la prime du lait. Source : Cour des comptes
  2016, p. 27.
- **farine panifiable / farine de luxe** (الفرينة المعدّة لصنع الخبز / الفرينة الرفيعة). Source :
  Cour des comptes 2016, pp. 10-11.
- **transferts directs au titre de la subvention** (التحويلات المباشرة بعنوان الدعم). Sources :
  rapport budget 2023, p. 60 ; clôture 2023, p. 69.
- **compte « ن مكرر »** (dépôts des établissements para-étatiques au Trésor) : à définir avant tout
  emploi.

## Lacunes (TODO, rien n'est inventé)

- **(a) La série des prix au public après 1991 n'existe pas dans le corpus.** Seul point établi :
  2010 (dix produits, prix du ministère du Commerce relayés par une étude). Les décisions du
  ministre de 1992 à 2026 ne sont pas lues : décision n° 05 de 2011, décision n° 3 de 2011, révision
  du 5 mars 2013, décision du 19 novembre 2014 ; de même l'acte (« قرار ») du 14 janvier 2011, absent
  du JORT. Destination :
  base législative `tunisia-legislative-references` (texte non publié, émetteur : ministère du
  Commerce) ou demande au ministère.
  - **Approximation possible, à n'utiliser que nommée comme telle.** Pour les dérivés des céréales,
    le prix réduit du blé (série de l'Office 2009-2020, constant depuis 2012-2013) signale les
    changements de structure de prix, mais pas le prix au public. On ne peut pas en tirer un prix au
    public ; à ne pas faire.
- **Poids du pain** : 400 g et 220 g sont déjà donnés pour 2010 (INS-CRES-BAD), alors que le dernier
  texte publié est de 1991 (500 g et 250 g). L'acte qui a changé le poids entre 1991 et 2010 n'est
  pas identifié.
- **Décret n° 2012-621** (JORT n° 47 du 15 juin 2012) : identifié ; URL pist.tn et clé à créer si
  le rédacteur le cite.
- **LF 2026** : ni le rapport sur le budget 2026, ni le PAP 2026, ni le budget de mission 2026 ne sont
  dans l'entrepôt ; non lus. `data/raw/minfinances/repartition_depenses_LF2026.xls` n'a pas été ouvert.
- **(b) L'exécution des 697 MD de transferts mensuels de 2023** n'est pas établie, ni l'emploi des
  585 MD de dépenses imprévues. Le texte qui organise la plateforme d'inscription et les transferts
  n'est pas identifié (passe ci-dessous).
- **(c) Papier scolaire** : le bénéficiaire du reste de la ligne, au-delà de la SNCPA, n'est pas
  établi (2019-2024). L'OCT reçoit plus que la ligne sucre en 2018 et en 2020 : objet de la
  différence non établi.
- **(c) 2015-2016** : écart de 19 MD entre le payé du ministère du Commerce (Cour des comptes) et
  les « résultats » du ministère des Finances, à expliquer dans une note de concordance.
- **Pages à revoir à l'image** : clôture 2023, p. 69 (couche texte lacunaire) ; budget de mission
  2021, narratif p. 32 ; commentaire de la clôture 2021 sur la farine (« الكميات المدعمة لمادة
  الفارينة »), à paginer.
- **Copie du communiqué FMI 22/353** à archiver dans `tunisia-data`.

## Recherches : passes à consigner (non appliquées : la note seule est écrite)

```yaml
# r-comp-pb-prix-consommateur-apres-1991 : ajouter
- date: 2026-11-18
  role: documentaliste
  sources: [web, jort_cache]
  couverture: 'Hors JORT : Cour des comptes, « منظومة دعم المواد الأساسية » (2016, contrôle 2009-2014), pp. 9-11, 26-27 et 29 ; budgets de mission et PAP du Commerce 2018-2025 ; rapports de clôture 2013-2024 ; INS-CRES-BAD 2013, tableau 2. Résultat : les prix au public sont fixés depuis 1992 par décision (مقرر) du ministre chargé du commerce, non publiée au JORT ; décisions nommées : 14 janvier 2011 (baisse des prix au public des dérivés des céréales, du lait demi-écrémé, du sucre et du concentré de tomate), n° 05 du 14 janvier 2011 (pâtes : 0,410 D les 500 g), n° 3 de 2011 (concentré de tomate), 19 novembre 2014 (huile) ; l''acte (قرار) du 14 janvier 2011 baissant les prix au public n''est pas dans jort_cache (textes signés du 13 au 15 janvier 2011 : quatre, aucun sur les prix) ; restructuration des prix de la farine et de la semoule le 5 mars 2013 ; prix de vente de 2010 du ministère du Commerce (dix produits). Aucun texte de ces décisions n''est lu. Lacunes : textes des décisions (ministère du Commerce, base législative) ; prix 1992-2009 et 2011-2026 ; documents de la LF 2026 non lus.'
  couvert_jusqu_au: 2026-06-30
  resultat: aucun
# a_faire, à remplacer par :
# a_faire: ['décisions du ministre du commerce (مقرر) : base législative ou demande au ministère', 'miroir iort : termes iort_ar de la fiche']

# r-comp-pb-ciblage-2013-2026 : ajouter
- date: 2026-11-18
  role: documentaliste
  sources: [web]
  couverture: 'Hors JORT : rapports sur le budget de l''État 2022 (p. 20 et 48), 2023 (p. 37, 38, 51, 60 et 141), 2024 (p. 35 et 51), 2025 (p. 52) ; Cour des comptes, clôture 2023 (p. 69) et rapport de 2016 (p. 10-11) ; FMI CR 13/161 (p. 25) et communiqué 22/353. Résultat : intention budgétaire (2022 : « dans l''attente de la mise en place du système de subvention directe » ; 2023 : programme de réforme, plateforme d''inscription des ménages, 697 MD de transferts mensuels directs au programme « Sécurité sociale » et 585 MD de transferts aux familles en dépenses imprévues) ; aucun texte d''organisation (décret, arrêté, article de loi de finances) n''est cité par ces documents. Lacunes : article ou tableau de la loi de finances 2023 qui inscrit les 697 MD ; exécution 2023 ; rapport sur le budget 2026 et PAP 2026 non lus ; miroir iort et plein texte arabe des fascicules 2022-2023 non relancés.'
  couvert_jusqu_au: 2026-06-30
  resultat: aucun
# termes à ajouter (elargir, iort_ar) : منصة تسجيل الأسر ; التحويلات المباشرة بعنوان الدعم ; التحويلات الشهرية المباشرة لفائدة الأسر
```

## Corrections à porter ailleurs (pour l'archiviste)

- **tunisia-data, `sources/gbo-recuperation-2026-11-04.csv`** : `2021-03_مهمة التجارة_0.pdf` est le
  budget de la mission pour **2020** (octobre 2019), catalogué « LF2021 ».
- **tunisia-data, playbook `chercher-des-donnees-tunisie.md`**, à ajouter :
  - pour la dépense **payée par produit** (compensation, transferts), les rapports de la Cour des
    comptes sur la clôture du budget (rubrique 18), tableau de la mission Commerce, aux pages
    données en (c) ;
  - pour le **crédit par paragraphe**, les documents « ميزانية الدولة — مهمة » de gbo.tn (tableau par
    article, vers la p. 180).
- **tunisia-data, catalogue** : `imf_2013_161_sba_request_tunisia.pdf` n'a pas de ligne au
  catalogue `sources/` (adresse vérifiée :
  `https://www.imf.org/external/pubs/ft/scr/2013/cr13161.pdf`).
- **tunisia-data, nouvelle série possible** : `compensation-produits-base-par-produit` (2011-2024,
  Cour des comptes), avec sa fiche de provenance.
- **Chapitre, TODO de la l. 207** : l'écart est de 191 à 307 MD, pas de 181 à 307 MD. Les
  bénéficiaires sont établis en (c) 3 ; le rédacteur peut remplacer la phrase « la part du poste qui
  va à d'autres bénéficiaires n'est pas attribuée par les sources budgétaires ».
- **Chapitre, TODO de la l. 125** (sorties du champ) : la phrase de l'INS-CRES-BAD sur 1996, citée
  en (a), est à relire à l'image.
- **Chapitre, TODO de la l. 403** (opérateur du lait régénéré) : la prime du lait demi-écrémé va aux
  centrales laitières depuis 2011 (Cour des comptes 2016, p. 27). Le « lait régénéré » d'avant 2011
  reste à établir.
