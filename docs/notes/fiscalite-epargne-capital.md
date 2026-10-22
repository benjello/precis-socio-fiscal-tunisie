# La fiscalité de l'épargne et du capital — note documentaire

Rôle : documentaliste. Ouverte le 20 octobre 2026 (n° 9 des « Manques du précis »,
`docs/notes/backlog-precis.md`). Rendue le 20 octobre 2026.

## 1. Carte du déjà-traité dans le volume « La fiscalité »

| Sujet | Où, dans le volume | Ce qui est dit | Ce qui manque |
|---|---|---|---|
| Définition des revenus de valeurs mobilières (art. 29-33) et de capitaux mobiliers (art. 34-35) | `_impot_revenu.qmd`, #sec-irpp-capitaux | définitions, absence d'abattement, art. 31 *bis* (plus-value sur actions, 2004) | aucun taux de retenue, aucun taux d'imposition de la plus-value |
| Fin de l'exonération générale des dividendes | `_impot_revenu.qmd`, #sec-irpp-capitaux ; registre l. 1033 | abrogation de l'art. 38-10 par LF 2014 art. 19, distributions à partir du 1/1/2015 | la retenue de 5 % puis 10 % (c *bis*), son caractère libératoire, la restitution sous 10 000 D |
| Exonérations de l'art. 38 (épargne logement, devises, comptes études, CEI, plus-values boursières, jeux) | `_impot_revenu.qmd`, #sec-irpp-capitaux, une phrase | énumération | plafonds, dates, chaîne des plus-values exonérées |
| Déduction des primes d'assurance-vie (art. 39 § I-2) | `_impot_revenu.qmd`, #sec-irpp-deductions | bornes 200 D (1990) et 100 000 D (revenus 2020) | série intermédiaire (TODO existant) |
| Plafond de déduction des intérêts d'épargne (art. 39 § II) | `_impot_revenu.qmd`, #tbl-epargne | série 1990-2021 complète, II *bis* obligations vertes | — (bascule 1991/1992 non établie) |
| CEA (39 § VIII), CEI (39 *bis*), FCPR (39 *ter*) | `_impot_revenu.qmd`, #sec-irpp-deductions, une phrase | CEA 50 000 → 100 000 D (LF 2021) | séries, conditions, dates |
| Minimum d'impôt au titre des avantages (art. 12 *bis* loi 89-114) | `_impot_revenu.qmd`, #tbl-plafonnement (tableau engendré) | 60 % puis 45 % | — |
| Régime boursier (loi 2010-29) : IS à 20 % cinq ans | `_impot_societes.qmd`, « Un régime hors du code : l'admission en bourse » | conditions, fenêtre 2010-2014 | — (reste au chapitre IS) |
| Option de la plus-value à 15 % puis 10 % (IS) ; retenues réalignées LF 2021/2025 | `_impot_societes.qmd`, « 2021 — aplatir », « 2024 — remonter » | mention des §§ | les taux de retenue eux-mêmes |
| Plus-value immobilière | `_patrimoine_immobilier.qmd` | complet | renvoi seulement |
| Coût des déductions CEA et CEI, que le rapport range sous « Intérêts dépôts et épargne » (26,6 / 30,2 / 2,7 MD, 2017-2019) | rapport des dépenses fiscales annexé au PLF 2021 (`docs/notes/fiscalite-depenses-fiscales.md` l. 808 le prenait pour des intérêts exonérés : c'est CEA + CEI) ; détail par mesure dans la série `depenses-fiscales-detail` du cache du précis | — | à reprendre par mesure (§ 7) |
| Antécédent : taxe sur le revenu des valeurs mobilières (décret organique du 23/12/1918), impôt sur le revenu des créances (décret du 20/12/1919) | `_impot_revenu.qmd`, « La suppression de 1990 » | nommés, sans taux | taux et régime avant 1990 |

TODO déjà posé dans le volume : `_impot_revenu.qmd` l. 989-991, « le régime de la retenue à la
source libératoire (revenus de capitaux mobiliers notamment), articles du code et série des
taux » — c'est le cœur de la présente note.

## 2. Recommandation à l'architecte : un chapitre neuf

**Recommandation : un chapitre `_epargne_capital.qmd`**, entre `_impot_fortune.qmd` et
`_patrimoine_immobilier.qmd` (ou juste après `_impot_societes.qmd`), et non une extension de
#sec-irpp-capitaux. Trois motifs :

1. **Le critère de scission** (`docs/conventions-redaction.md`, § 4) : `_impot_revenu.qmd`
   compte déjà 26 285 mots (wc, 20/10/2026), au-delà du seuil d'environ 25 000. L'extension est
   exclue.
2. **Une épine propre.** Les retenues sur les revenus de capitaux suivent leur propre suite de
   ruptures, qui ne coïncide pas avec celle du barème : 1990 (code), 1992 (« harmonisation du
   régime fiscal applicable aux différentes formes d'épargne »), 1997 (« unification des taux »),
   2004 (plus-values sur actions), 2015 (dividendes), 2020-2022 (retenue de 35 %, puis
   libératoire générale, puis retour à l'imputation), 2023 (plus-values à deux taux). Elle croise
   l'IRPP (catégorie VI, déductions), l'IS (retenues, régime boursier) et les non-résidents.
3. **La vue économique** : le lecteur veut le taux effectif par placement à dates repères. Ce
   tableau n'a sa place ni dans le chapitre de l'IRPP ni dans celui de l'IS.

**Règle de domicile proposée** :
- #sec-irpp-capitaux garde ses définitions (art. 29-35), l'absence d'abattement, une phrase et
  un lien en tête vers le nouveau chapitre. Le paragraphe « fin de l'exonération générale des
  dividendes » déménage, ou se réduit à une phrase et un lien.
- #tbl-epargne (plafond de déduction des intérêts d'épargne), les primes d'assurance-vie, le CEA,
  le CEI et l'art. 39 *ter* : à déménager dans le nouveau chapitre. Ce sont des avantages à
  l'épargne, pas des charges du revenu. À défaut, ils restent en place avec un lien en tête.
  À trancher par l'architecte.
- Le régime boursier de la loi n° 2010-29 (IS à 20 %) reste à `_impot_societes.qmd`. Le nouveau
  chapitre y renvoie. C'est un avantage à l'émetteur, pas au placement.
- La plus-value immobilière reste à `_patrimoine_immobilier.qmd` (renvoi).
- Le coût budgétaire des déductions à l'épargne (CEA, CEI, assurance-vie) se renvoie à
  `_depenses_fiscales.qmd` ; les montants par mesure sont dans la série `depenses-fiscales-detail` (voir § 7).

## 3. Plan proposé (ruptures au premier plan)

1. **Vue d'ensemble** : trois régimes coexistent — retenue imputable sur l'impôt du barème,
   retenue libératoire ou définitive, exonération ou déduction. Ce qui distingue les placements,
   c'est la combinaison des trois. Figure ou tableau court : le taux marginal légal par
   placement aux dates de rupture (§ 6).
2. **Mise en place (1990)** : l'antécédent cédulaire (taxe sur le revenu des valeurs mobilières,
   décret organique du 23 décembre 1918 ; impôt sur le revenu des créances, décret organique du
   20 décembre 1919, abrogés par la loi n° 89-114, art. 2). Puis le code de 1990 : retenues de
   10 % (comptes spéciaux d'épargne), 15 % (revenus de capitaux mobiliers), 35 % libératoire
   (bons de caisse anonymes). Dividendes exonérés (art. 38-10). Épargne logement, livrets de
   la CENT et dépôts en devises exonérés (art. 38-7 et 38-8). Déduction des intérêts des comptes
   spéciaux (1 000 D) et des primes d'assurance-vie (200 D et majorations).
3. **Grandes réformes, dans l'ordre des dates** :
   - **1992 — harmoniser les formes d'épargne** (LF 1992, titre III) : 15 % sur tous les dépôts
     et obligations ; 25 % et 35 % libératoires sur les titres au porteur anonymes ; 20 %
     définitive pour les personnes morales exonérées ; plafond de déduction à 1 500 D ; comptes
     d'épargne-emprunts obligataires (15 % libératoire sous blocage de cinq ans).
   - **1997 — unifier à 20 %** (LF 1997, art. 30-33) : un seul taux de 20 % sur les revenus de
     capitaux mobiliers ; fin des taux libératoires sur les titres anonymes et du compte
     d'épargne-emprunts obligataires. Cela vient après l'imposition des jetons de présence
     (LF 1995).
   - **1999-2004 — orienter l'épargne vers la Bourse** : comptes épargne en actions (loi
     n° 99-92), régime des OPCVM (LF 2002), comptes épargne pour l'investissement (LF 2003),
     plus-value sur actions et parts sociales imposée à 10 %, avec exonération des actions cotées
     et franchise de 10 000 D (LF 2004).
   - **2011 — conditionner l'exonération boursière à la durée de détention** (LF 2011, art. 41 ;
     décret-loi n° 2011-100) ; imposition des plus-values des non-résidents (retenue « e *bis* »,
     LF 2012).
   - **2014-2018 — imposer les dividendes** (LF 2014, art. 19 : 5 % libératoire sur les
     distributions à partir du 1^er^ janvier 2015 ; LF 2018, art. 46 : 10 %), en contrepartie de
     la baisse de l'IS de 30 % à 25 % (même loi, art. 18).
   - **2020-2022 — trois régimes en trois ans pour les intérêts** : retenue définitive de 35 %
     sur les dépôts mieux rémunérés que le TMM moins un point (décret-loi n° 2020-30, art. 12) ;
     retenue libératoire générale de 20 % (LF 2021, art. 17) ; « réinstauration de la retenue à
     la source déductible » (LF 2022, art. 38).
   - **2023 — plus-values à deux taux** (10 % et 15 % ; suppression de la franchise de 10 000 D ;
     LF 2023, art. 42).
4. **Bilan et état du droit au 1^er^ janvier 2026** : un tableau par nature de revenu — taux,
   caractère libératoire, exonérations et plafonds.
5. **Sections secondaires** (une par dispositif, avec leur chronologie repliée) : comptes spéciaux
   d'épargne et obligations (#tbl-epargne) ; assurance-vie ; CEA ; CEI ; comptes épargne études ;
   OPCVM et fonds (FCP, SICAV, fonds d'amorçage, FCPR) ; jetons de présence et rémunérations des
   administrateurs ; non-résidents (retenues b, c, c *bis*, e, e *bis*, paradis fiscaux à 25 %).
6. **Longue période économique** (budgétaire seul) : encours de l'épargne bancaire et postale ;
   coût des exonérations selon le rapport des dépenses fiscales ; recettes des retenues (lacune,
   § 8).
7. **« Ce qu'en dit l'économie »** (fiche `docs/notes/eco-…` à commander à l'économiste) :
   imposition duale des revenus du capital, effet du taux sur les dividendes sur les
   distributions, verrouillage des plus-values.

## 4. Paramètres datés

Conventions de cette section :
- **Lu image** : chiffre relu sur l'image du fascicule.
- **Lu texte** : couche texte du fascicule, ou couche décodée (+29) pour les fascicules à police
  décalée.
- **Lu AR** : édition arabe seule, l'édition française n'étant ni au corpus ni sur pist.tn.
- Pages : pagination imprimée de l'édition française, sauf mention AR. Elles sont établies au
  pied de page de la page du fichier qui porte le texte : le numéro de page du JORT est en
  **pied** de page, et un en-tête qui précède le texte dans une extraction appartient à la page
  précédente.
- **Dates d'effet** : celles qu'énonce le texte ou une note commune, sinon « dérivée », avec le
  calcul. Quand le calcul exige la date de dépôt au gouvernorat (règle de la loi n° 93-64), la
  date est dite « à établir ».

### 4.1 Retenue sur les revenus de capitaux mobiliers (intérêts) — art. 52 § I et § II

| Date d'effet | Avant → après | Texte, article, page | État |
|---|---|---|---|
| revenus 1990 | **10 %** intérêts des comptes spéciaux d'épargne ouverts auprès des banques (52-I-b) ; **15 %** revenus de capitaux mobiliers et sommes servies aux non-résidents au titre de l'art. 3-6° (52-I-c) ; **35 %** revenus des bons de caisse au porteur dont l'identité n'est pas révélée (52-I-d). Libératoire (52-II) **seulement** pour les bons de caisse au porteur et pour les revenus servis aux non-résidents. Pour les autres, retenue imputable (art. 54) | Code IRPP-IS, art. 52, JORT n° 1 des 2-5 janvier 1990, p. 11 [@code-irpp-is-1990] | lu image (p. 11) ; OCR `markdown_output/Code_de_lIRPP_et_IS_1990.md` concordant |
| 2 janvier 1992 (dérivée : JORT du 31/12/1991 + un jour franc ; la LF 1992 n'a pas de clause générale d'effet, vérifié sur l'OCR de la fin de la loi) | 52-I et II abrogés et remplacés : **15 %** sur les intérêts des dépôts à la CENT ou en comptes spéciaux d'épargne (10 % → 15 %), sur les revenus des obligations et autres capitaux mobiliers, et sur les sommes servies aux non-résidents ; **25 %** sur les obligations au porteur anonymes ; **35 %** sur les autres revenus de capitaux mobiliers au porteur anonymes. Libératoire pour les revenus au porteur anonymes et pour les non-résidents. Nouveau 52-II-2 : **20 % définitive et non restituable** pour les revenus de capitaux mobiliers des personnes morales non soumises à l'IS ou totalement exonérées | LF 1992 (loi n° 91-98), art. 31, titre III « Dispositions portant harmonisation du régime fiscal applicable aux différentes formes d'épargne », JORT n° 90 du 31 décembre 1991, p. 2084-2085 [@lf-1992, art. 31] | lu image (p. 2084-2085) |
| idem | **Comptes d'épargne-emprunts obligataires** : intérêts soumis à une retenue **libératoire de 15 %** si aucun retrait pendant 5 ans ; retenue complémentaire de 10 % en cas de retrait | LF 1992, art. 33, p. 2085 [@lf-1992, art. 33] | lu image |
| 1^er^ janvier 1997 (LF 1997, art. 54 : « applicables à compter du 1er janvier 1997 », p. 2583) | « **Unification** des taux de la retenue à la source sur les revenus de capitaux mobiliers » : abrogation des 1^er^ et 2^e^ tirets de 52-I-b (15 % épargne et obligations) et de 52-I-d (35 %) ; 52-I-c devient « **20 %** au titre des revenus de capitaux mobiliers » ; suppression du 1^er^ tiret de 52-II-1 (fin du libératoire pour les titres anonymes). Art. 33 : abrogation des 2^e^ et 3^e^ paragraphes de l'art. 33 de la LF 1992 (fin du libératoire de 15 % du compte d'épargne-emprunts obligataires) | LF 1997 (loi n° 96-113), art. 30-33, JORT n° 105 du 31 décembre 1996, p. 2581 [@lf-1997, art. 30 à 33] | lu texte |
| 1^er^ janvier 1999 (LF 1999, art. 76) | 52-I-c : ajout de « à l'exception des intérêts des dépôts et des titres en devises et en dinars convertibles » (déjà exonérés par 38-8 ; la retenue n'est plus opérée). 52-II-2 : retrait d'une mention relative aux banques offshore (loi n° 85-108) | LF 1999 (loi n° 98-111), art. 43, JORT n° 104 du 29-31 décembre 1998, p. 2505 [@lf-1999, art. 43] | lu texte |
| 1^er^ janvier 2002 (LF 2002, art. 97 : « applicables à compter du 1er janvier 2002 ») | FCP en valeurs mobilières : leurs revenus de capitaux mobiliers sont soumis à une retenue « définitive et libératoire » de 20 % (52-II-2 étendu). Les revenus des parts de FCP sont des revenus distribués (29-II *bis*), donc exonérés jusqu'en 2014. Fonds communs de créances : 20 % sur leurs revenus, imputable sur la retenue due aux copropriétaires | LF 2002 (loi n° 2001-123), art. 21 à 28 [@lf-2002] ; note commune n° 45/2002 (résumé), `markdown_output/Notes_Communes/` | lu NC ; articles non relus au fascicule |
| 1^er^ janvier 2004 (clause générale de la LF 2004, couche décodée) | 52-II-1 récrit : « La retenue à la source est libératoire de l'impôt sur le revenu ou de l'impôt sur les sociétés au titre des sommes prévues par les alinéas b, c et e du paragraphe I du présent article et par l'alinéa 3 du présent paragraphe ». **À la lettre, le texte ne réserve pas le caractère libératoire aux non-résidents.** L'administration ne l'a pas lu ainsi : la note commune n° 8/2004 (art. 66 de la même loi, cautionnements) écrit que la retenue de 20 % frappe les revenus de capitaux mobiliers « à l'instar de tous les revenus de capitaux mobiliers » et qu'elle « est imputable sur l'impôt annuel exigible ultérieurement ou sur les acomptes provisionnels », le bénéficiaire restant « tenu de déclarer lesdits revenus parmi son revenu global ». En 2004, la retenue reste donc imputable pour les résidents ; la LF 2005 met le texte en accord | LF 2004 (loi n° 2003-80), art. 71, JORT n° 104 du 30 décembre 2003, p. 3732 [@lf-2004, art. 71] ; note commune n° 8/2004 | **lu image** (p. 3732) ; NC lue |
| 1^er^ janvier 2005 (note commune n° 13/2005 pour l'art. 69 : montants « payés ou mis à la disposition » à partir du 1/1/2005) | 52-II-1 récrit : libératoire « au titre des sommes prévues par les alinéas b et c du paragraphe I du présent article **et servies aux non résidents et non établis** en Tunisie et par l'alinéa e […] et par le paragraphe 3 ». 52-I-c : ajout des **jetons de présence** (15 % → 20 %) | LF 2005 (loi n° 2004-90), art. 69 § 3 et § 5, JORT n° 105 du 31 décembre 2004, p. 3442 [@lf-2005, art. 69] ; NC 13/2005 | lu texte (décodé) ; NC lue |
| **10 juin 2020** : art. 17 du décret-loi, « entre en vigueur à la date de sa publication », JORT AR n° 54 du 10 juin 2020, p. 1414 ; fascicule déposé au gouvernorat de Tunis le 10 juin 2020. Aucune clause propre à l'art. 12 : la retenue vaut pour les revenus payés à compter de cette date ; le sort des intérêts courus avant reste à confirmer par une note commune | Nouveau 52-II-2 *bis* : revenus de capitaux mobiliers des **dépôts à terme** et produits financiers similaires dont le taux de rémunération au 1^er^ janvier de l'année dépasse **le TMM moins un point** : retenue **définitive et non restituable de 35 %**, quel que soit le régime fiscal du bénéficiaire ; hors devises et dinars convertibles | Décret-loi du Chef du gouvernement n° 2020-30 du 10 juin 2020, art. 12, JORT AR n° 54 de 2020, p. 1410 (l'édition française est absente du corpus et répond 404 sur pist.tn le 20/10/2026) | **lu AR** (couche texte NFKC), art. 12 et 17 ; rubrique de l'art. 12 : « retenue à la source **libératoire** de 35 % » (§ 14, D3) |
| 1^er^ janvier 2021 (LF 2021, art. 42 § 1, p. 3138 ; NC 1/2022 : « revenus de capitaux mobiliers payés à partir du 1er janvier 2021 ») | « Révision du régime fiscal des revenus de capitaux mobiliers » : abrogation de 52-II-2 et 2 *bis* (fin des 35 %) ; 52-II-1 complété : la retenue de l'alinéa c « est **définitive et non restituable** […] nonobstant le régime fiscal du bénéficiaire ». La NC 1/2022 la qualifie de « retenue à la source **libératoire** au taux de 20 % » : les revenus ne sont plus pris en compte dans le revenu soumis au barème. Les exonérations et déductions (art. 38, 39 § II) sont maintenues | LF 2021 (loi n° 2020-46), art. 17, JORT n° 128 du 25 décembre 2020, p. 3130 [@lf-2021, art. 17] ; [@dgi-nc-1-2022] | lu texte ; NC lue |
| 1^er^ janvier 2022 (NC 1/2022 : revenus « payés à partir du 1er janvier 2022 », sans restitution des montants antérieurs) | « **Réinstauration** de la retenue à la source déductible » : suppression de la phrase de 2021 ; 52-II-2 rétabli (20 % définitive pour les personnes morales exonérées et les FCP, étendue aux fonds d'amorçage et aux FCPR, hors devises) ; la retenue de 20 % redevient imputable sur l'IR ou l'IS | LF 2022 (décret-loi n° 2021-21), art. 38, JORT n° 119 du 28 décembre 2021, p. 3090 [@lf-2022, art. 38] ; [@dgi-nc-1-2022] | lu texte ; NC lue |

**Bons du Trésor.** Leurs intérêts sont des revenus de capitaux mobiliers (art. 34-1 : « effets
publics ») et suivent la retenue de l'alinéa c. Les bons du Trésor assimilables entrent dans la
déduction de 39 § II par la LF 2024, art. 34 (déjà au précis).
<!-- (documentaliste) Le décret n° 2007-1870 du 17 juillet 2007 fixe les modalités de la retenue sur les titres d'emprunt négociables (LF 2000, art. 57) : non lu. -->

### 4.2 Dividendes et revenus distribués — art. 38-10, art. 52-I-c *bis*

| Date d'effet | Avant → après | Texte, article, page | État |
|---|---|---|---|
| revenus 1990 | Revenus de valeurs mobilières des art. 29, 30 et 31 **exonérés** (38-10) ; aucune retenue | Code, art. 38-10, JORT n° 1 de 1990, p. 8 [@code-irpp-is-1990, art. 38] | lu (OCR, page 8) — relecture à l'image à faire |
| 1^er^ janvier 1995 (LF 1995, article final : « applicables à compter du 1er janvier 1995 ») | **Jetons de présence** exclus de l'exonération (38-10 récrit) et soumis à une retenue de **15 %** (ajout d'un tiret à 52-I-b) ; déductibles de l'IS (48-VI) | LF 1995 (loi n° 94-127), art. 50 à 53, JORT n° 103 du 30-31 décembre 1994, p. 2046 (page à confirmer à l'image : numéro lu dans une liste ambiguë) [@lf-1995, art. 50 à 53] | lu texte |
| 1^er^ janvier 2005 | Jetons de présence : 15 % → **20 %** (déplacés à 52-I-c) | LF 2005, art. 69 § 3-4, p. 3442 ; NC 13/2005 | lu |
| montants payés à partir du 1^er^ janvier 2017 (LF 2017, art. 79 : la loi « s'applique à compter du 1er janvier 2017 » ; art. 30 sans clause propre) | « jetons de présence » remplacés par « rémunérations et primes attribuées […] aux membres des conseils, des directoires et des comités » des SA et SCA (art. 30-3, 52-I-c, 48-VI) | LF 2017 (loi n° 2016-78), art. 30, JORT n° 105 du 20 décembre 2016, p. 3837 [@lf-2017, art. 30] | lu texte |
| distributions à partir du **1^er^ janvier 2015** (art. 19 § 3) | Abrogation de 38-10 et du 2^e^ tiret du 3^e^ paragraphe de l'art. 3. Nouvel alinéa 52-I-c *bis* : **5 %** sur les revenus distribués (29-II-a et 29-II *bis*, donc parts de FCP comprises). **Libératoire** (52-II-1 étendu à c *bis*). Personnes physiques dont les revenus distribués ne dépassent pas **10 000 D par an** : retenue déductible de l'IR annuel ou restituable (§ 6). Distributions prélevées sur les fonds propres au bilan du 31/12/2013 et mentionnées dans les notes aux états financiers de 2013 : exclues (§ 7) | LF 2014 (loi n° 2013-54), art. 19, JORT n° 105 du 31 décembre 2013, p. 3670-3671 [@lf-2014, art. 19] | **lu image** (p. 3670) |
| idem (même loi) | Contrepartie : IS de droit commun **30 % → 25 %** (bénéfices de 2014), et retenue de 30 % → 25 % là où elle figure à l'art. 52 (cessions à partir du 1/1/2014) | LF 2014, art. 18, p. 3670 | lu image |
| 1^er^ janvier 2015 (LF 2015, art. 46, clause générale ; art. 25 sans clause propre) | c *bis* étendu à l'alinéa c du 29-II (bénéfices des établissements stables présumés distribués aux associés non résidents) ; paiement par déclaration de l'établissement stable | LF 2015 (loi n° 2014-59), art. 25, JORT n° 105 du 30 décembre 2014, p. 3466 [@lf-2015, art. 25] ; NC 3/2015 (non lue en détail) | lu texte |
| distributions à partir du **1^er^ janvier 2018** (NC 14/2018), même si les bénéfices sont antérieurs ; bénéfices 2017 des établissements stables | c *bis* : **5 % → 10 %**. Restent hors retenue : bénéfices distribués aux personnes morales résidentes, fonds propres au 31/12/2013, exonérations conventionnelles | LF 2018 (loi n° 2017-66), art. 46, JORT n° 101 du 19 décembre 2017, p. 4286 [@lf-2018, art. 46] ; NC 14/2018 | lu texte ; NC lue |

État au 1^er^ janvier 2026 : 52-I-c *bis* à 10 %, libératoire. La phrase de restitution sous
10 000 D figure toujours au code consolidé de 2025 (art. 52-II-1). Son articulation avec le
caractère libératoire est à confirmer par la NC 3/2015 ou par une note postérieure.
Taux de **25 %** pour les bénéficiaires établis dans un État à régime fiscal privilégié (dernier
alinéa de l'art. 52, ajouté par la LF 2014, art. 44, et modifié par la LF 2019, art. 35-4 —
annotations du code consolidé, **non lues au fascicule**).

### 4.3 Plus-values de cession de titres (personnes physiques résidentes) — art. 31 *bis*, 33, 38-17 et 18, 44-III-3

| Date d'effet | Avant → après | Texte, article, page | État |
|---|---|---|---|
| avant 2004 | La plus-value de cession d'actions et de parts sociales par une personne physique, hors activité professionnelle, n'est rattachée à aucune catégorie | (constat : l'art. 31 *bis* est créé en 2004) | — |
| cessions à partir du **1^er^ janvier 2004** (art. 31 *bis*) | Plus-value de cession d'actions et de parts sociales rangée dans la catégorie des revenus de valeurs mobilières (31 *bis*) ; égale au prix de cession moins la valeur d'acquisition, après imputation des moins-values de l'année (33, 2^e^ al.). Taux : **10 %** de son montant (44-III-3). Exonérations (38-17) : actions cotées à la BVMT et cessions dans le cadre d'une introduction en bourse ; actions de SICAV ; cessions réalisées pour le compte de personnes physiques par les SICAR. Franchise de **10 000 D par an** (38-18) | LF 2004 (loi n° 2003-80), art. 61 à 63, JORT n° 104 du 30 décembre 2003, p. 3730 [@lf-2004, art. 61 à 63] | lu texte (décodé) ; à relire à l'image |
| à établir (LF 2007, art. 88 : loi applicable au 1/1/2007 ; article non lu) | 38-17 modifié (ajouts) | LF 2007 (loi n° 2006-85), art. 32 [@lf-2007, art. 32] | annotation seule, **non lu** |
| cessions à partir du **1^er^ janvier 2011** (art. 41 § 5) | 38-17, 1^er^ tiret : l'exonération des actions cotées est réservée à celles **acquises ou souscrites avant le 1/1/2011** et aux introductions en bourse. Nouveau tiret : actions cotées acquises à partir du 1/1/2011 exonérées **si la cession a lieu après l'expiration de l'année suivant celle de l'acquisition**, sinon imposées à 10 %. Plus-value des non-résidents imposée (art. 3, 2^e^ paragraphe ; art. 45-III). Retenue sur le prix de cession pour les non-résidents (52-I-e) : 5 % pour les personnes morales, 2,5 % pour les personnes physiques, avec option pour l'imposition de la plus-value réelle | LF 2011 (loi n° 2010-58), art. 41 § 1-14, JORT n° 102 du 21 décembre 2010, p. 3474-3476 [@lf-2011, art. 41] ; NC 16/2011 (non lue) | lu texte |
| cessions de parts de fonds à partir du **1^er^ janvier 2012** | 31 *bis* étendu aux parts de fonds ; 38-17 récrit (actions cotées acquises depuis 2011 détenues au-delà de l'année suivante ; SICAV et FCPVM ; fonds d'amorçage ; SICAR et FCPR sous conditions) ; 38-18 *bis* abrogé | Décret-loi n° 2011-100 du 21 octobre 2011, art. 7 à 9 (JORT n° 81 de 2011, notice à intitulé arabe dans `jort_cache`) | annotations du code consolidé ; **non lu au fascicule** |
| cessions à partir du **1^er^ janvier 2023** (art. 42 § 3) | 44-III-3 : **10 %** pour les actions cotées cédées avant l'expiration de l'année suivant l'acquisition, et pour les autres actions, parts sociales et parts de fonds cédées après cette échéance ; **15 %** pour les actions non cotées, parts sociales et parts de fonds cédées avant. **Franchise de 10 000 D (38-18) abrogée** | LF 2023 (décret-loi n° 2022-79), art. 42, JORT AR n° 141 du 23 décembre 2022, p. 4068 [@lf-2023, art. 42] (édition française absente) ; NC 3/2023 | **lu AR** ; NC lue |

L'exonération des actions cotées détenues au-delà de l'année suivant l'acquisition (38-17)
demeure au 1^er^ janvier 2026 (code consolidé 2025).

### 4.4 Plus-values des non-résidents non établis (retenue « e *bis* ») — pour mémoire

| Date d'effet | Avant → après | Texte, page | État |
|---|---|---|---|
| 1^er^ janvier 2012 (LF 2012, art. 49) | Retenue sur le prix (52-I-e, 2011) remplacée par 52-I-e *bis* : **30 %** de la plus-value (personnes morales), **10 %** (personnes physiques) | LF 2012 (loi n° 2011-7), art. 15, JORT n° 1 du 3 janvier 2012, p. 5 [@lf-2012, art. 15] | lu texte |
| 2012 | Plafonds : 5 % du prix (personnes morales), 2,5 % (personnes physiques) | LFC 2012 (loi n° 2012-1), art. 12, JORT n° 39 de 2012, p. 923 [@lfc-2012, art. 12] | lu texte |
| cessions à partir du 1/1/2014 | 30 % → **25 %** | LF 2014, art. 18 § 2, p. 3670 | lu image |
| plus-values réalisées à partir du 1/1/2021 (art. 14 § 28) | 25 % → **15 %** | LF 2021, art. 14 § 4, p. 3127 | lu texte |
| plus-values réalisées à partir du 1/1/2025 (art. 37 § 16) | 15 % → **20 %** | LF 2025 (loi n° 2024-48), art. 37 § 7, JORT n° 149 du 10 décembre 2024, p. 3431 (extrait français local ; pist.tn ne sert pas l'édition française) [@lf-2025, art. 37] | lu texte (extrait) |

Intérêts des prêts payés aux banques non établies (52-I-e) : **2,5 %** (LF 1995, art. 54,
p. 2046), **5 %** (LF 2011, art. 43, p. 3476), **10 %** (LF 2018, art. 47, p. 4286) — lus.

### 4.5 Épargne exonérée ou aidée

| Dispositif | Date d'effet | Avant → après | Texte, page | État |
|---|---|---|---|---|
| Livrets CENT et épargne logement (38-7) | revenus 1990 | intérêts des livrets de la CENT et des contrats d'épargne logement exonérés | Code, art. 38-7, p. 8 | lu (OCR) |
| idem | 1992 | 38-7 réduit à l'**épargne logement** (les livrets de la CENT passent dans la déduction plafonnée de 39 § II) | LF 1992, art. 30, p. 2084 | lu image |
| Dépôts et titres en devises ou dinars convertibles (38-8) | revenus 1990 | exonérés ; hors retenue depuis 1999 | Code, art. 38-8 ; LF 1999, art. 43 | lu |
| Comptes spéciaux d'épargne et obligations (39 § II) | — | série complète déjà au précis (#tbl-epargne) | — | — |
| Comptes d'épargne pour les études (38-12) | 1^er^ janvier 1999 (LF 1999, art. 76) | intérêts exonérés ; décret n° 99-1923 | LF 1999, art. 45, p. 2506 [@lf-1999, art. 45] | lu texte |
| **Assurance-vie** (39 § I-2) — déduction des primes | revenus 1990 | 200 D + 100 D (conjoint) + 50 D par enfant (4 premiers) | Code, art. 39, p. 8 | lu |
| idem | revenus 1997 [dér.] : LF 1998, art. 90 (« applicables à compter du 1er janvier 1998 »), art. 52 sans clause propre, règle de conversion « cas 2 » de `docs/notes/fiscalite-irpp-assiette-abattements.md` | **800 D** + 400 D (conjoint) + 200 D par enfant à charge (sans limite de rang) | LF 1998 (loi n° 97-88), art. 52, JORT n° 104 de 1997, p. 2439 [@lf-1998, art. 52] | lu texte |
| idem | **primes payées à partir du 1^er^ janvier 2007** (NC 10/2008) | **1 200 D** + 600 D (conjoint) + 300 D par enfant ; rachat sans pénalités après 5 ans d'épargne (rachats à partir du 1/1/2008) | LF 2008 (loi n° 2007-70), art. 23, JORT n° 104 de 2007, p. 4360 [@loi-2007-70-lf-2008, art. 23] ; NC 10/2008 | lu texte ; NC lue |
| idem | **déclarations dont l'échéance tombe à partir du 25 mai 2012, soit les revenus de 2011** pour les BNC, artisans, agriculteurs, salariés et pensionnés ; retenue sur salaires à partir du 25 mai 2012 (NC 25/2012) | **10 000 D** par an, majorations supprimées ; descendants ajoutés | LFC 2012 (loi n° 2012-1), art. 42, p. 929 [@lfc-2012, art. 42] ; NC 25/2012 | lu texte ; NC lue |
| idem | 2014 | 10 000 D maintenus ; durée minimale 10 ans ; contrats collectifs | LF 2014, art. 24, p. 3671 | lu image |
| idem | contrats conclus à partir du 1^er^ janvier 2018 (NC 2/2018) | durée 10 → 8 ans | LF 2018, art. 27 § 3, p. 4275 ; NC 2/2018 | lu texte ; NC lue |
| idem | revenus 2020 | 10 000 → **100 000 D** ; soumis au minimum d'impôt | LF 2021, art. 16 [@dgi-nc-1-2021] | déjà au précis |
| Rentes viagères des contrats d'assurance-vie (38-16) | 2004 | exonérées | LF 2004, art. 44 | lu texte (décodé) |
| **CEA** (39 § VIII) | exécutoire le 26 août 1999 (JORT n° 67 déposé au gouvernorat le 21 août 1999) ; année de revenus non établie | création : déduction de **50 %** des dépôts, plafond **5 000 D** ; blocage 5 ans ; actions cotées et BTA | Loi n° 99-92 du 17 août 1999 « relative à la relance du marché financier », art. 4, JORT n° 67, p. 1463-1464 ; décret n° 99-2773 | lu texte (décodé) |
| idem | 2002 | champ élargi aux OPCVM investis en actions cotées et BTA ; 5 000 D maintenus | LF 2002, art. 30-31, p. 4253-4254 du fascicule n° 104 de 2001 (à recouper avec la pagination de la notice `lf-2002`) | lu texte (décodé) |
| idem | **revenus 2003** (NC 16/2004 ; art. 105 de la LF 2004) | 50 % et 5 000 D → **20 000 D**, plus de quote-part ; condition de comptabilité supprimée | LF 2004, art. 45-46, JORT n° 104 de 2003 ; NC 16/2004 | lu texte et NC |
| idem | date à établir (décret-loi publié au JORT n° 27 du 19 avril 2011) | 20 000 → **50 000 D** (le JORT imprime « 50.0000 ») | Décret-loi n° 2011-28 du 18 avril 2011, art. 4, JORT n° 27, p. 488 | lu texte |
| idem | revenus 2020 | 50 000 → **100 000 D** | LF 2021, art. 16 [@dgi-nc-1-2021] | déjà au précis ; lu |
| **CEI** (39 *bis*, 38-15) | 2003 (NC 35/2003) | création : déduction des dépôts plafonnée à **20 000 D** par an ; intérêts exonérés dans la limite de **2 000 D** ; emploi sous 5 ans | LF 2003 (loi n° 2002-101), art. 21-23 ; NC 35/2003 ; arrêté du 24 avril 2003 | lu NC ; articles non relus au fascicule |
| idem | **montants déposés et intérêts réalisés à partir du 1^er^ janvier 2017** (revenus 2017, NC 2/2018) | dépôts 20 000 → **50 000 D** ; intérêts 2 000 → **4 000 D** ; « ou bénéfices » ajoutés | LF 2018, art. 27 § 1, 2 et 4, p. 4275 [@lf-2018, art. 27] ; NC 2/2018 | lu texte ; NC lue |
| Fonds d'amorçage et FCPR (39 *ter*) | 2005 | déduction des revenus réinvestis en parts, hors minimum d'impôt | Loi n° 2005-59 du 18 juillet 2005, art. 3 | annotation ; non lu |

**Minimum d'impôt de l'art. 12 *bis* de la loi n° 89-114 : un jalon pour le TODO voisin.** Les
NC 35/2003 et 16/2004 écrivent que ce minimum est « fixé à 60 % de l'impôt dû sur le revenu
global ». Le taux de 60 % est donc en vigueur en 2003. Cela borne la recherche de son texte
d'origine (TODO de `_impot_revenu.qmd`, l. 649-655).

## 5. Antécédents et contexte

- **Avant 1990 — régime cédulaire.** La « taxe sur le revenu des valeurs mobilières et sur les
  intérêts des créances hypothécaires ou privilégiées » (décret organique du 23 décembre 1918) et
  l'« impôt sur le revenu des créances » (décret organique du 20 décembre 1919) sont abrogés par
  la loi n° 89-114, art. 2, pour les revenus de 1990 [@loi-irpp-is-1989, art. 2] (déjà au
  chapitre IRPP). **Leurs taux n'ont pas été cherchés.** Sources pressenties : *Journal officiel
  tunisien* 1918-1919 (scans, OCR) et lois de finances 1956-1989 (corpus local) ; la note
  `docs/notes/fiscalite-irpp-besoins-documentation.md` n'en traite pas. Le code de 1990 reprend
  le principe de la retenue par le payeur, l'exonération des dividendes (aucune taxe distincte
  sur les distributions ne lui succède) et un taux libératoire pour l'anonymat (bons de caisse,
  35 %).
- **1992 — mots de la loi.** Titre III de la LF 1992 : « Dispositions portant harmonisation du
  régime fiscal applicable aux différentes formes d'épargne » ; rubriques « Déduction des
  intérêts de l'épargne » et « Dispositions relatives à la retenue à la source » (JORT n° 90 de
  1991, p. 2084).
- **1997 — mots de la loi.** « Unification des taux de la retenue à la source sur les revenus de
  capitaux mobiliers » (LF 1997, p. 2581).
- **1999-2004 — relance du marché financier.** Loi n° 99-92 « relative à la relance du marché
  financier » : IS à 20 % pendant cinq ans pour les sociétés admettant au moins 30 % de leur
  capital à la cote (art. 1-3), et CEA (art. 4). Rubrique de la LF 2004 : « Soumission de la
  plus-value provenant de la cession des actions et des parts sociales à l'impôt sur le revenu »
  et « Exonération de la plus-value réalisée dans le cadre d'une opération d'introduction en
  bourse ».
- **2011 — rubrique** : « Rationalisation de l'exonération de la plus value provenant de la
  cession des titres » (LF 2011, art. 41).
- **2013-2014 — contexte de l'imposition des dividendes** (sources de l'époque, toutes dans
  `~/projets/tunisia-data/data/raw/minfinances/reforme_fiscale_2013_2014/`, inventaire
  `docs/notes/reforme-fiscale-2013-2014-inventaire.md`) :
  - rapport de synthèse des groupes de travail de la réforme fiscale, ministère des Finances avec
    MS Louzir (Deloitte), novembre 2013, p. 24, partie « Diagnostic du système fiscal », relue le
    20/10/2026 : « La combinaison du prélèvement à la source de 20 % et du respect d'un secret
    bancaire fait que de nombreux contribuables préfèrent ne pas déclarer les revenus
    mobiliers » ; « les dividendes se trouvent totalement défiscalisés peu importe que les
    bénéfices générés au niveau de la société distributrice aient fait l'objet d'une imposition
    ou pas ». La partie 4 du rapport (p. 22-47) synthétise les diagnostics du FMI, de la Banque
    mondiale, de l'USAID et de la SFI : citer comme le rapport du ministère, en le disant ;
  - Conseil national de la fiscalité, août 2013, groupe de travail n° 1 (`2013-08_cnf_rf_1_ar.pdf`,
    p. 23-24 selon l'inventaire, non relu ici) : hypothèses « IS de 30 % à 25 % (ou 20 %) et
    soumission des bénéfices distribués à 5, 10 ou 15 % » ;
  - présentation « impôts directs » du CNF, novembre 2013, p. 14-15 selon l'inventaire, non
    relu : incidence annoncée de −116,3 MD (25 % avec dividendes imposés) et de −221,6 MD
    (20 %). C'est une estimation ministérielle ex ante, de famille budgétaire, méthode non
    décrite ;
  - rubrique de la LF 2014, art. 18-19 : « Réduction du taux de l'impôt sur les sociétés et
    imposition des bénéfices distribués ».
- **2017 — rubrique de l'art. 46 de la LF 2018** : « Relèvement du taux d'imposition des
  bénéfices distribués ».
- **2020-2022.** Décret-loi n° 2020-30 « portant des mesures pour la consolidation des assises de
  la solidarité nationale et le soutien des personnes et des entreprises suite aux répercussions
  de la propagation du Coronavirus » (intitulé du code consolidé). LF 2021 : « Révision du
  régime fiscal des revenus de capitaux mobiliers ». LF 2022 : « Réinstauration de la retenue à
  la source déductible due sur les revenus de capitaux mobiliers » ; la NC 1/2022 en donne
  l'objet : « encourager les personnes physiques à adhérer aux différents mécanismes d'épargne,
  […] renforcer la justice fiscale ».
- **2022 — rubrique** de l'art. 42 de la LF 2023 (édition arabe) à relever.

## 6. Vue d'ensemble : taux marginal légal par placement, à dates repères

**Méthode, à écrire avec le tableau.** Contribuable type : une personne physique résidente, au
taux marginal supérieur du barème τ̄ (35 % de 1990 à 2024, 40 % depuis les revenus de 2025 —
#sec-irpp-bareme). La contribution sociale de solidarité (+1 point depuis 2018, +0,5 point pour
les revenus déclarés en 2023-2025) n'est pas comptée ; à signaler en note. Le tableau donne le
**taux marginal légal** d'un dinar supplémentaire de revenu, au-delà des plafonds d'exonération
ou de déduction. En deçà du plafond, le taux est nul (exonération) ou négatif (déduction de la
mise : assurance-vie, CEA, CEI). On ne mesure ni l'inflation (taux sur le rendement nominal), ni
l'IS déjà payé en amont par la société, ni la fraude — que le rapport de 2013 décrit, p. 24.
Toutes les cellules sont tirées des tableaux du § 4. Les dates repères sont des ruptures, pas un
pas régulier.

| Placement | 1990 | 1992 | 1997 | 2004 | 2005-2014 | 2015 | 2018 | 10 juin-31 déc. 2020 | 2021 | 2022 | 2023-2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dépôt à terme, obligation, bon du Trésor | τ̄ (retenue 15 % imputable) | τ̄ (15 %) | τ̄ (20 %) | τ̄ (20 % imputable, NC 8/2004) | τ̄ (20 %) | τ̄ | τ̄ | τ̄ ; **35 % libératoire** (rubrique de l'art. 12) sur les dépôts à terme rémunérés au-delà du TMM moins un point | **20 % libératoire** | τ̄ (20 % imputable) | τ̄ |
| Compte spécial d'épargne (sous plafond) | 0 (déduction 1 000 D) | 0 (1 000 D sur 1 500 D) | 0 | 0 | 0 | 0 | 0 (3 000 D sur 5 000 D, revenus 2016-2020) | 0 | 0 | 0 (6 000 D sur 10 000 D) | 0 |
| Titre anonyme au porteur | 35 % libératoire (bons de caisse) | 25 % (obligations) ou 35 % libératoire | régime commun | — | — | — | — | — | — | — | — |
| Épargne logement ; dépôts en devises | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Dividende d'action | 0 | 0 | 0 | 0 | 0 | **5 %** libératoire | **10 %** libératoire | 10 % | 10 % | 10 % | 10 % |
| Plus-value, action cotée | hors champ | hors champ | hors champ | 0 (exonérée) | 0 ; depuis 2011 : 10 % si cession avant la fin de l'année suivant l'achat | idem | idem | idem | idem | idem | 0 (détention longue) ; 10 % (courte) |
| Plus-value, action non cotée, part sociale | hors champ | hors champ | hors champ | 10 % (franchise de 10 000 D) | 10 % | 10 % | 10 % | 10 % | 10 % | 10 % | 10 % (longue) ; 15 % (courte), sans franchise |
| Assurance-vie (plafond de la prime déductible) | 200 D (+ majorations) | idem | 800 D (+ majorations) depuis les revenus de 1997 [dér.] | 800 D | 1 200 D (primes de 2007), 10 000 D (revenus 2011, NC 25/2012) | 10 000 D | 10 000 D | 10 000 D | 100 000 D (revenus 2020) | idem | idem |
| CEA (plafond du dépôt déductible) | — | — | — | 20 000 D (revenus 2003) | 50 000 D (2011, rattachement à établir) | 50 000 D | 50 000 D | 50 000 D | 100 000 D (revenus 2020) | idem | idem |

Pour un rédacteur : le tableau ne porte que des paramètres sourcés au § 4. Les cellules « τ̄ »
renvoient au barème. Il vaut pour un contribuable au taux marginal supérieur ; au bas du barème,
la retenue imputable de 20 % peut excéder l'impôt dû et devient restituable (art. 54),
sauf en 2021.
<!-- Les déductions (assurance-vie, CEA, CEI) sont plafonnées par le minimum d'impôt de l'art. 12 bis de la loi n° 89-114 (60 % puis 45 % de l'impôt dû) : leur avantage effectif est borné. -->

## 7. Séries chiffrées

Familles distinguées, budgétaire d'abord.

**Budgétaire**
- **Coût des avantages à l'épargne, par mesure** (rapports des dépenses fiscales annexés aux
  projets de LF 2021, 2024 et 2025 ; série `depenses-fiscales-detail` du cache du précis,
  `precis/_seriescache/depenses-fiscales-detail.csv`, déjà lue par les figures du chapitre « Les
  dépenses fiscales »). En MD :

  | Mesure (code) | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
  |---|---|---|---|---|---|---|---|
  | Dépôts en CEA (111103909) | 24,631 | 28,257 | 2,578 | 27,989 | 33,335 | 13,710 (LF 2024) / 36,432 (LF 2025) | 28,184 |
  | Dépôts en CEI (111103912) | 2,007 | 1,970 | 0,122 | 2,373 | 1,899 | 0,583 (LF 2024) / 1,676 (LF 2025) | 1,042 |
  | Primes d'assurance-vie (111103901) | non valorisé | non valorisé | non valorisé | 12,101 | 29,453 | 15,961 (LF 2024) / 44,304 (LF 2025) | 43,771 |
  | Plus-value sur actions et parts sociales (111103809) | 0,159 | 0,121 | 0,006 | 0,048 | 0,148 | 0,184 (LF 2024) | — |
  | Intérêts des comptes spéciaux d'épargne (111103904), épargne logement, devises, comptes études | non valorisé dans les trois rapports | | | | | | |

  Années 2017-2019 : rapport LF 2021 ; 2020-2022 : rapport LF 2024 ; 2021-2023 : rapport LF 2025.
  **Les millésimes divergent pour 2022** (CEA 13,7 MD dans le rapport LF 2024 contre 36,4 MD dans
  le rapport LF 2025 ; assurance-vie 16,0 contre 44,3 ; CEI 0,6 contre 1,7) : le rapport LF 2024
  porte vraisemblablement une estimation provisoire, ce que le rapport ne dit pas ; présenter les
  deux, sans chaîner en silence. 2021 concorde entre les deux rapports. Le libellé « 02 Intérêts
  dépôts et épargne » du tableau par domaine du rapport LF 2021 (p. 32 : 26,64 / 30,23 / 2,70 MD)
  est **exactement CEA + CEI** (24,631 + 2,007 = 26,638 ; 28,257 + 1,970 = 30,227 ; 2,578 + 0,122
  = 2,700) : ce ne sont pas des intérêts exonérés, qui sont, eux, non valorisés. Méthode du
  rapport : `docs/notes/fiscalite-depenses-fiscales.md` (perte de recettes à comportement
  inchangé). La chute de 2019 n'est pas expliquée par le rapport.
- **Recettes des retenues sur les revenus de capitaux et sur les dividendes : non trouvées.**
  `tunisia-data/data/raw/minfinances/recettes_fiscales.xls` ne ventile pas l'IRPP. Sources à
  examiner : rapports annuels de la DGI 2013-2014 (dans `tunisia-data`, arabe, à lire à
  l'image), lois de règlement, rapport sur le budget de l'État (`2013-10_rapport_projet_budget_etat_2014_ar.pdf`).
  Ne rien estimer.
- **Estimations ex ante du ministère (2013)** : −116,3 MD et −221,6 MD (§ 5), pour l'ensemble
  « baisse de l'IS et imposition des dividendes ». Chiffres de l'inventaire, à relire avant
  usage.

**Encours (BCT, statistique monétaire)**
- **Épargne bancaire et postale**, fin d'année, 2003-2024, en milliers de dinars : de 5 582 991
  (2003) à 44 828 004 (2024) ; également **dépôts à terme** (même table, colonne v4). Source : BCT,
  *Bulletin des statistiques financières*, table IV-2-a « Situation rétrospective des agrégats de
  monnaie », transcrite par `tunisia-data/scripts/map_bsf_agregats_monnaie.py` →
  `data/processed/bct/agregats_monnaie_2003_2024.csv`. Mensuel CENT 2012-2026 :
  `data/processed/bct/epargne_cep.csv` (provenance à documenter dans `sources/` : aucune fiche
  ne le cite). À rapporter au PIB courant : dire la base (annexe PIB).
- **Capitalisation boursière, actifs des OPCVM, primes d'assurance-vie : non collectés.** Sources
  pressenties : CMF (rapports annuels), BVMT, FTUSA ou CGA (assurance) ; Banque mondiale WDI
  (rapport extérieur, à tenir à part).

**Rapports extérieurs et évaluations** : aucun récupéré ni cité. Candidats à chercher pour la
section des études et pour l'économiste : FMI, rapports au titre de l'article IV et *selected
issues* sur la réforme fiscale de 2013-2014 ; Banque mondiale, *The Unfinished Revolution*
(2014), chapitre fiscal ; OCDE, *Statistiques des recettes publiques en Afrique* (ventilation
de l'IRPP par source si elle existe).

## 8. Lacunes (rien n'est inventé ; chaque point est à lire ou à obtenir)

1. **Portée de l'art. 71 de la LF 2004 : réglée.** La lettre du texte (p. 3732, lue à l'image)
   rend libératoire la retenue de l'alinéa c pour tous. La note commune n° 8/2004, rédigée en
   2004, la dit imputable pour les résidents. La LF 2005 aligne le texte. Pas de fiche de
   recherche.
2. **Restitution sous 10 000 D et caractère libératoire de c *bis*.** Les deux phrases sont dans
   l'art. 52 depuis 2014. Lire la note commune n° 3/2015 (au corpus local, non lue en détail),
   puis toute note postérieure, pour l'état depuis 2018.
3. **Dates de rattachement non établies** : CEA à 50 000 D (décret-loi n° 2011-28, art. 4,
   publié au JORT du 19 avril 2011 ; aucune note commune trouvée au corpus) ; loi n° 99-92 (CEA, création : exécutoire
   le 26 août 1999, année de revenus à établir) ; LF 1992, art. 30. (Assurance-vie à 10 000 D :
   établi par la NC 25/2012, § 14.)
4. **Textes connus par les seules annotations du code consolidé, non lus au fascicule** :
   LF 2007, art. 32 (38-17) ; décret-loi n° 2011-100, art. 6 à 13 (JORT n° 81 de 2011, notice
   à intitulé arabe) ; loi n° 2005-59 (fonds d'amorçage) ; LF 2014, art. 44, et LF 2019,
   art. 35 (taux de 25 % pour les paradis fiscaux) ; LF 2003, art. 21-23 (CEI : lus par la
   NC 35/2003 seulement) ; LF 2002, art. 21-28 (OPCVM : lus par la NC 45/2002 seulement).
5. **SICAV.** Leur régime (IS ? distributions soumises à c *bis* ?) n'est pas établi : la
   NC 45/2002 renvoie à un « régime fiscal des SICAV en vigueur » antérieur, non identifié.
6. **Antécédent cédulaire** : taux de la taxe sur le revenu des valeurs mobilières (1918) et de
   l'impôt sur le revenu des créances (1919) aux dernières années (1980-1989) ; non cherchés.
   Lois de finances 1980-1989 au corpus local (scans, OCR ciblé).
7. **Recettes des retenues** (capitaux mobiliers, dividendes, plus-values) : aucune série
   budgétaire ventilée trouvée (§ 7).
8. **Rapports des dépenses fiscales : lacune levée.** La série `depenses-fiscales-detail` du
   cache du précis porte les rapports annexés aux PLF 2021, 2024 et 2025 (§ 7). Restent : le
   rapport PLF 2022 et 2023 (années 2018-2021) s'il diffère, et la divergence des millésimes pour
   2022.
9. **Capitalisation boursière, encours OPCVM, primes d'assurance-vie** : non collectés.
10. **Arrêté du 24 avril 2003 (CEI), décrets n° 99-2773 (CEA), 99-1923 (comptes études),
    2007-1870 (retenue sur les titres d'emprunt négociables)** : non lus.
11. **LF 2023, art. 42 : l'intitulé de la rubrique** est à relever dans l'édition arabe
    (p. 4068).

## 9. Notions à glossaire

| Terme FR | AR pressenti | Source canonique | État |
|---|---|---|---|
| Retenue à la source libératoire | خصم من المورد تحرري (DL 2020-30, art. 12, édition AR : « لخصم من المورد تحرري ») | Code, art. 52-II-1 | **à créer** ; l'entrée `retenue-a-la-source` existe : la compléter (son « imputé sur l'impôt dû » est faux pour les retenues libératoires) |
| Retenue définitive et non restituable | خصم من المورد نهائي وغير قابل للإرجاع (DL 2020-30, art. 12, AR) | art. 52-II-2 | à créer ou à fondre dans la précédente |
| Revenus de capitaux mobiliers | مداخيل رؤوس الأموال المنقولة (DL 2020-30, AR) | Code, art. 34 | à créer |
| Revenus de valeurs mobilières | مداخيل القيم المنقولة (à confirmer sur l'édition AR du code) | Code, art. 29-33 | à créer |
| Bénéfices (revenus) distribués | الأرباح الموزعة / المداخيل الموزعة (LF 2014, éd. AR : les deux formes) | Code, art. 29 | à créer ; choix du terme AR au terminologue |
| Plus-value de cession de titres | القيمة الزائدة (LF 2023, art. 42, AR) | Code, art. 31 *bis* et 33 | à créer (voir aussi `plus-value-immobiliere`) |
| Compte épargne en actions (CEA) | حساب الادخار في الأسهم (à confirmer) | Code, art. 39-VIII ; loi n° 99-92 | à créer |
| Compte épargne pour l'investissement (CEI) | حساب الادخار من أجل الاستثمار (à confirmer) | Code, art. 39 *bis* | à créer |
| Comptes spéciaux d'épargne | الحسابات الخاصة للادخار (à confirmer) | Code, art. 39-II | à vérifier (cité dans `deductions-communes`) |
| Organisme de placement collectif en valeurs mobilières (OPCVM : SICAV, FCP) | مؤسسات التوظيف الجماعي في الأوراق المالية (à confirmer) | Loi n° 2001-83 | à créer |
| Taux du marché monétaire (TMM) | معدل نسبة الفائدة في السوق النقدية (DL 2020-30, AR) | — | à vérifier |

## 10. Références candidates

**Déjà présentes** (à citer avec article et page) : `code-irpp-is-1990`, `loi-irpp-is-1989`,
`lf-1992`, `lf-1995`, `lf-1997`, `lf-1998`, `lf-1999`, `lf-2002`, `lf-2004`, `lf-2005`,
`lf-2007`, `loi-2007-70-lf-2008`, `lf-2011`, `lf-2012`, `lfc-2012`, `lf-2014`, `lf-2015`,
`lf-2017`, `lf-2018`, `lf-2021`, `lf-2022`, `lf-2023`, `lf-2024`, `lf-2025`, `dgi-nc-1-2021`,
`dgi-nc-1-2022`, `dgi-nc-2-2017`, `loi-2010-29`, `loi-avantages-fiscaux-2017`,
`minfin-cnf-2013-synthese` (rapport de synthèse de novembre 2013), `gbo-depenses-fiscales`.
**Doublon à signaler au bibliographe (non corrigé ici)** : `lf-2002` et `loi2001-123-lf2002`
désignent la même loi n° 2001-123 ; la première porte les pages 4286 et 4301, la seconde la
page 4260 ; les art. 30-31 se lisent p. 4253-4254 du fascicule n° 104 de 2001 (couche décodée,
page à confirmer à l'image).

**À créer** (type `legislation` pour les textes, `report` pour les notes communes ; URL pist.tn
pour le JORT, édition de la langue du fichier) :

```json
[
 {"id": "loi-99-92-relance-marche-financier", "type": "legislation",
  "title": "Loi n° 99-92 du 17 août 1999, relative à la relance du marché financier",
  "container-title": "Journal officiel de la République tunisienne", "issue": "67",
  "page": "1463-1464", "issued": {"date-parts": [[1999, 8, 20]]},
  "URL": "https://www.pist.tn/jort/1999/1999F/Jo06799.pdf"},
 {"id": "decret-loi-2011-28", "type": "legislation",
  "title": "Décret-loi n° 2011-28 du 18 avril 2011, portant des mesures fiscales et financières pour la relance de l'économie nationale",
  "container-title": "Journal officiel de la République tunisienne", "issue": "27",
  "page": "487-489", "issued": {"date-parts": [[2011, 4, 19]]},
  "URL": "https://www.pist.tn/jort/2011/2011F/Jo0272011.pdf"},
 {"id": "decret-loi-2020-30", "type": "legislation",
  "title": "Décret-loi du Chef du gouvernement n° 2020-30 du 10 juin 2020, portant des mesures pour la consolidation des assises de la solidarité nationale et le soutien des personnes et des entreprises suite aux répercussions de la propagation du Coronavirus « Covid-19 »",
  "container-title": "Journal officiel de la République tunisienne (édition arabe)", "issue": "54",
  "page": "1407-1413", "issued": {"date-parts": [[2020, 6, 10]]},
  "URL": "https://www.pist.tn/jort/2020/2020A/Ja0542020.pdf",
  "note": "Édition française absente : 2020F/Jo0542020.pdf répond 404 (20/10/2026). Intitulé français repris du code consolidé, à vérifier."},
 {"id": "decret-loi-2011-100", "type": "legislation",
  "title": "Décret-loi n° 2011-100 du 21 octobre 2011, portant adaptation des avantages fiscaux relatifs au réinvestissement dans le capital risque avec le champ d'intervention des SICAR et des FCPR",
  "container-title": "Journal officiel de la République tunisienne", "issue": "81",
  "issued": {"date-parts": [[2011, 10, 25]]},
  "note": "Pagination à relever ; notice jort_cache à intitulé arabe. Non lu."},
 {"id": "dgi-nc-13-2005", "type": "report", "title": "Note commune n° 13/2005 — Commentaire des dispositions de l'article 69 de la loi n° 2004-90 du 31 décembre 2004 portant loi de finances pour l'année 2005, relatives au relèvement du taux de la retenue à la source au titre de certains revenus", "publisher": "Direction générale des études et de la législation fiscales", "issued": {"date-parts": [[2005]]}},
 {"id": "dgi-nc-14-2018", "type": "report", "title": "Note commune n° 14/2018 — Commentaire des dispositions de l'article 46 de la loi n° 2017-66 du 18 décembre 2017 portant loi de finances pour l'année 2018 (relèvement du taux d'imposition des bénéfices distribués)", "issued": {"date-parts": [[2018]]}, "note": "Numéro tiré du nom de fichier du corpus local ; à vérifier sur l'en-tête."},
 {"id": "dgi-nc-2-2018", "type": "report", "title": "Note commune n° 2/2018 — Commentaire des dispositions de l'article 27 de la loi n° 2017-66 du 18 décembre 2017 portant loi de finances pour l'année 2018", "issued": {"date-parts": [[2018]]}, "note": "En-tête « NOTE COMMUNE N° 02/2018 » ; le fichier du corpus est nommé « numéro 20 »."},
 {"id": "dgi-nc-16-2004", "type": "report", "title": "Note commune n° 16/2004 — Relèvement du montant déductible au titre des dépôts dans les comptes épargne en actions et assouplissement des conditions de déduction", "issued": {"date-parts": [[2004]]}},
 {"id": "dgi-nc-35-2003", "type": "report", "title": "Note commune n° 35/2003 — Commentaire des dispositions des articles 21, 22 et 23 de la loi n° 2002-101 du 17 décembre 2002 portant loi de finances pour l'année 2003 relatives aux comptes épargne pour l'investissement", "issued": {"date-parts": [[2003]]}},
 {"id": "dgi-nc-45-2002", "type": "report", "title": "Note commune n° 45/2002 — Commentaire des dispositions des articles 21 à 28 de la loi n° 2001-123 du 28 décembre 2001 portant loi de finances pour l'année 2002 (régime fiscal des organismes de placement collectif)", "issued": {"date-parts": [[2002]]}},
 {"id": "dgi-nc-10-2008", "type": "report", "title": "Note commune n° 10/2008 — Commentaire des dispositions de l'article 23 de la loi n° 2007-70 du 27 décembre 2007 portant loi de finances pour l'année 2008", "issued": {"date-parts": [[2008]]}},
 {"id": "dgi-nc-3-2023", "type": "report", "title": "Note commune n° 3/2023 — Commentaire des dispositions de l'article 42 du décret-loi n° 2022-79 du 22 décembre 2022 portant loi de finances pour l'année 2023", "issued": {"date-parts": [[2023]]}}
]
```

Les URL des notes communes sont à prendre sur jibaya.tn, comme pour `dgi-nc-1-2021` ; les
fichiers sont dans `~/projets/PDFs-legislation-tunisie/markdown_output/Notes_Communes/` (et
`PDFs/Notes_Communes/`). À ranger dans `tunisia-data/data/raw/minfinances/notes_communes/`
(répertoire existant), avec une ligne de catalogue, si le bibliographe les cite.

## 11. Ce que porte le modèle (pour `docs/notes/backlog-modele.md`, jamais pour le rendu)

Lu le 20/10/2026 dans `openfisca-tunisia/openfisca_tunisia/parameters/impot_revenu/` et
`impot_societes/`.
- **Absents** : tout taux de retenue sur les revenus de capitaux mobiliers (art. 52-I-c), sur
  les dividendes (c *bis*), sur les intérêts payés aux banques non établies (e), sur les
  plus-values des non-résidents (e *bis*) ; le taux de 35 % de 2020 ; le caractère libératoire
  ou imputable ; le taux de la plus-value mobilière des personnes physiques (44-III-3 : 10 %
  depuis 2004, 10 % et 15 % depuis 2023) et la franchise de 10 000 D (2004-2022).
  Série à fenêtre : tout est lisible depuis 1990 (§ 4).
- **`deductions/cea_cei/cea`** : 0 en 1990, 50 000 au 1/1/2001, 100 000 au 1/1/2021, avec
  pour seule référence « Loi n° 2020-46 … (Article 24) ». Les textes donnent : 5 000 D et 50 %
  des dépôts (loi n° 99-92, art. 4, 1999), 20 000 D (revenus 2003, LF 2004, art. 45, NC 16/2004),
  50 000 D (décret-loi n° 2011-28, art. 4, 2011, rattachement à établir), 100 000 D (revenus
  2020). L'article de la LF 2021 est l'**art. 16**, non l'art. 24 (lu p. 3129 ; le précis cite
  déjà l'art. 16).
- **`deductions/cea_cei/cei`** : 50 000 au 1/1/2003, sans référence. Les textes donnent 20 000 D
  (LF 2003, art. 21 ; NC 35/2003), puis 50 000 D pour les dépôts à partir du 1/1/2017 (LF 2018,
  art. 27 § 1 ; NC 2/2018).
- **`deductions/interets_comptes_epargne_investissement/plaf`** : 2 000 depuis 1990, sans
  référence. L'exonération est créée en 2003 (LF 2003, art. 22 ; 38-15) à 2 000 D et portée à
  4 000 D pour les intérêts réalisés à partir du 1/1/2017 (LF 2018, art. 27 § 2 ; NC 2/2018).
- **`deductions/assurance_vie/plaf`** : le palier de 10 000 D est daté du 1/1/2013 et sourcé à
  la LF 2014, art. 24 § 1. Or le plafond de 10 000 D (majorations supprimées) vient de la
  **LFC 2012 (loi n° 2012-1), art. 42 § 1** (JORT n° 39 de 2012, p. 929) ; la LF 2014 le
  reprend. La NC 25/2012 le rattache aux revenus de 2011 (déclarations échues à partir du
  25 mai 2012) : date du paramètre 2011, non 2013. Le palier de 1 200 D (2007) est
  confirmé par la NC 10/2008 (primes payées à partir du 1/1/2007).
- **`deductions/interets_comptes_speciaux_epargne_cent/plaf`** : 1 000 depuis 1990, sans
  référence ni description utile. En 1990, la déduction ne vise que les comptes des banques ;
  les livrets de la CENT sont alors exonérés (38-7). La CENT entre dans la déduction en 1992
  (LF 1992, art. 30). Paramètre à revoir ou à supprimer.

- **État après la 0.141 (22/10/2026).** Les feuilles ci-dessus sont versées (#496, #499, #500).
  Le précis en engendre, outre les cinq tableaux de plafonds et d'actions cotées, cinq tableaux
  de retenues : `irpp_epargne_fonds` (retenue définitive, 1992, 2021, 2022),
  `irpp_epargne_ceo` (comptes d'épargne-emprunts obligataires, 1992, 1997),
  `irpp_epargne_nr_interets` (non-résidents : revenus de capitaux mobiliers, intérêts des
  prêts des banques non établies, bénéficiaires de pays à régime fiscal privilégié),
  `irpp_epargne_nr_plus_values` (retenue sur le prix puis sur la plus-value, plafond en part du
  prix) et `irpp_epargne_jetons`. La date vient de la feuille ; le libellé du texte et l'ancre
  du registre sont écrits dans `scripts/generate_bareme_tables.py`. Restent à la main : la
  liste des États à régime fiscal privilégié, l'extension de 2002 aux fonds communs de
  placement (LF 2002, art. 21 à 28 non relus), les lignes de registre sans changement de valeur
  (1999 pour les fonds, 2005 pour les non-résidents), `regimes_speciaux/retenue_liberatoire/taux`
  (0,20 en 1990 contre 15 % au code, p. 11) et le détail des textes de chaque registre.
- **Correction du registre des intérêts (1990).** Au code de 1990 (JORT n° 1 des 2-5 janvier
  1990, p. 11), l'alinéa 52-I-c a deux tirets : les revenus de capitaux mobiliers (15 %) et les
  sommes servies aux non-résidents au titre de l'article 3, point 6 (15 %, redevances). La ligne
  `r-epargne-interets-1990` écrivait « 15 % sur les autres revenus de capitaux mobiliers et les
  sommes servies aux non-résidents » : le second tiret ne vise pas des revenus de placement ; la
  ligne le dit. Le caractère libératoire pour les non-résidents (52-II) est inchangé. La LF 2019
  (art. 35, édition arabe, pp. 5449-5450) est ajoutée au registre des non-résidents
  (`r-epargne-nr-2019`).
- **Écart de pages à noter** : la feuille des jetons de présence cite les art. 50 et 52 de la
  LF 1995 ; le registre cite les art. 50 à 53 ; le tableau engendré reprend le registre.

## 12. Recherches infructueuses

`uv run python scripts/recherches.py lister` (20/10/2026) : 170 fiches, aucune sur ce sujet.
**Aucune fiche créée, aucune écriture dans `docs/recherches.yml`** (le reformatage de la fiche
LF 1987 signalé par le coordinateur n'a donc pas eu lieu). La seule recherche qui aurait pu en
appeler une, la portée de l'art. 71 de la LF 2004, est résolue par la note commune n° 8/2004.
Les lacunes du § 8 sont des textes **identifiés et non lus** (au corpus ou en ligne), ou des
séries non collectées, non des recherches infructueuses.

## 13. Sources lues et état de l'OCR

- OCR lancées au premier plan, terminées, sans processus restant : JORT n° 1 de 1990 (doublon
  de l'OCR du coordinateur, `markdown_output/Code_de_lIRPP_et_IS_1990.md`, utilisée ensuite),
  JORT n° 90 de 1991 (LF 1992) et n° 88 de 1992 (LF 1993, non exploitée). Les fichiers sont dans
  le répertoire temporaire de la session, non versés. **Chiffres relus à l'image** : code de
  1990, p. 11 ; LF 1992, p. 2084-2085 ; LF 2004, art. 71, p. 3732 ; LF 2014, art. 18-19, p. 3670.
- Fascicules à police décalée décodés (+29, `outillage-sources.md` § 5) : JORT n° 67 de 1999,
  n° 104 de 2001, n° 104 de 2003, n° 105 de 2004.
- Pages vérifiées par le pied de page de la page du fichier. LF 1999, art. 45 : p. 2506 (et non 2505).
- Édition arabe seule : DL 2020-30 (JORT AR n° 54/2020), LF 2023 (JORT AR n° 141/2022).
- Extraits français corrompus du dossier `PDFs/Lois_de_Finances/` (LF 2021, LF 2022, LF 2023 :
  « Couldn't read xref table ») : les fascicules du corpus JORT ont été lus à leur place.

## 14. Réponses aux questions de l'architecte (20 octobre 2026)

Questions de `docs/notes/fiscalite-epargne-capital-plan-architecte.md`, § 7. Pages : pied de
page de la page du fichier qui porte le texte.

**D3 — décret-loi n° 2020-30 et LF 2023.**
- **Les revenus frappés des 35 % sortent du revenu global.** L'art. 12 est placé sous le titre III
  « إجراءات لتمويل الاستثمار وإعادة تنشيط الاقتصاد » (mesures pour le financement de
  l'investissement et la relance de l'économie), et sa rubrique propre est : « إخضاع مداخيل
  الإيداعات بأجل التي تفوق نسبة تأجيرها معدل نسبة الفائدة في السوق النقدية ناقص نقطة مائوية
  لخصم من المورد **تحرري** بنسبة 35% » — soumission des revenus des dépôts à terme dont la
  rémunération dépasse le taux du marché monétaire moins un point à une retenue à la source
  **libératoire** de 35 %. Le corps de l'article dit « نهائي وغير قابل للإرجاع » (définitive et non
  restituable) « بصرف النظر عن النظام الجبائي للمنتفع ». JORT AR n° 54 du 10 juin 2020, p. 1410 ;
  lu AR (couche texte NFKC), rubrique et article. Cohérent avec la lecture de la même formule en
  2021 par la NC 1/2022 (« libératoire et définitive », revenus non pris en compte au barème).
  Aucune note commune propre au décret-loi trouvée (corpus des notes communes : aucune ne cite
  « 2020-30 » ; la presse de l'époque annonçait une note commune sur les intérêts précomptés des
  titres de créances négociables, non retrouvée). **Cellule : 35 %, sans barème.**
- Sort des intérêts courus avant le 10 juin 2020 : **non établi** (pas de note commune ; le
  décret-loi entre en vigueur à sa publication, art. 17, p. 1414).
- **LF 2023, art. 42 : rubrique** « مراجعة النظام الجبائي للقيمة الزائدة المتأتية من التفويت في
  السندات », JORT AR n° 141 du 23 décembre 2022, p. 4068 (lu AR). La NC 3/2023 la traduit
  « Révision du régime fiscal de la plus-value provenant de la cession des titres non rattachés à
  un bilan » et parle de « taux de l'impôt sur le revenu libératoire ». C'est une **révision**, pas
  une institution : argument pour l'étape (§ 8.5 du plan).

**D4 — restitution sous 10 000 D et caractère libératoire des dividendes.** La NC 3/2015 (relue
au corpus) ne fait que juxtaposer les deux règles : les revenus distribués à partir du 1/1/2015
« sont soumis à une retenue à la source libératoire », et « pour les personnes physiques
résidentes et non résidentes, la retenue à la source susvisée est déductible de l'impôt sur le
revenu annuel ou est restituable, et ce, si leurs revenus distribués ne dépassent pas 10.000
dinars annuellement ». Lecture du texte : libératoire par défaut, avec une faculté, sous
10 000 D, d'intégrer les dividendes au revenu global et d'imputer ou de se faire restituer la
retenue. **Les modalités (option, déclaration, seuil apprécié par bénéficiaire et par an) ne
sont pas décrites** par la NC 3/2015 ; la NC 14/2018 (passage à 10 %) n'en parle pas. Aucune autre
note du corpus ne croise « 10.000 dinars » et revenus distribués. La phrase est au code
consolidé de 2025 : la faculté demeure, au même seuil nominal, depuis 2015. Non établi au-delà.

**D6 — années de rattachement.**
- **LF 1992, art. 30 (1 500 D)** : non établi. La loi n'a pas d'article final de date
  d'application (vérifié) ; elle est exécutoire le 2 janvier 1992 (un jour franc après le JORT du
  31/12/1991) ; la règle « cas 2 » ne s'applique pas faute d'article final. Le rapport annuel de
  la BCT pour 1992 décrit la mesure sans date de rattachement (fichier p. 135). Aucune note commune
  de 1992 au corpus ; une recherche web sans résultat.
- **Loi n° 99-92 (CEA)** : le JORT n° 67 de 1999 « a été déposé au siège du gouvernorat de Tunis
  le 21 août 1999 » (mention du fascicule, couche décodée) ; **exécutoire le 26 août 1999**
  (loi n° 93-64, art. 2, jour du dépôt non compté). Les conditions d'ouverture des comptes sont
  fixées par le décret n° 99-2773 du 13 décembre 1999. Année de revenus : non établie (revenus 1999
  vraisemblables, non attestés).
- **Décret-loi n° 2011-28, art. 4 (CEA à 50 000 D)** : non établi. Aucune note commune au corpus
  ne commente l'art. 4 ; recherche web sans résultat.
- **LFC 2012, art. 42 (assurance-vie à 10 000 D)** : **établi par la NC 25/2012** (« entrent en
  vigueur à partir du 25 mai 2012 ») : la déduction de 10 000 D s'applique « aux déclarations de
  l'impôt sur le revenu des personnes physiques dont le délai de dépôt intervient à partir du
  25 mai 2012 », soit, pour les bénéfices non commerciaux, artisanaux, agricoles et les salaires
  et pensions, **les revenus de 2011** déclarés en 2012, et à la retenue sur salaires exigible à
  partir du 25 mai 2012. La NC précise aussi l'état antérieur : 1 200 D + 600 D + 300 D par enfant
  « dans la limite des quatre premiers enfants », soit 3 000 D au plus. Clé à créer :
  `dgi-nc-25-2012`.

**D7 — assurance-vie, LF 2002 et LF 2020.** LF 2002, art. 45 : étend la déduction aux contrats
« individuels ou collectifs », sans changer le montant (fascicule n° 104 de 2001, couche décodée).
LF 2020 (loi n° 2019-78), art. 12 : étend la déduction aux cotisations de l'adhérent et aux contrats
d'assurance takaful, sans changer le montant (JORT n° 104 du 27 décembre 2019, p. 4427, lu texte).
Les sept textes du TODO de `_impot_revenu.qmd` sont donc lus : seuls la LF 1998 (800 D), la LF 2008
(1 200 D) et la LFC 2012 (10 000 D) changent le montant.

**D5 — articles lus au fascicule (partiel).**
- LF 2014, art. 44 : « Relèvement du taux de la retenue à la source sur les montants payés à des
  résidents dans des paradis fiscaux » : le taux du 3^e^ tiret de b et des alinéas c, c *bis* et e
  « est relevé à 25 % » pour les résidents de paradis fiscaux, liste fixée par décret ; JORT n° 105
  du 31 décembre 2013, p. 3677 (lu texte, extrait). LF 2019, art. 35-4 : non lu.
- LF 2007, art. 32 : ajoute au point 17 de l'art. 38 l'exonération de la plus-value d'apport
  d'actions et de parts sociales au capital d'une société mère ou holding qui s'engage à
  introduire ses actions en bourse avant la fin de l'année suivante (prorogeable d'un an) ; JORT
  n° 103 de 2006, p. 4387 (lu texte, extrait ; page à confirmer : le texte suit le pied de page
  4386).
- Non lus : LF 2002, art. 21-28, et LF 2003, art. 21-23 au fascicule ; décret-loi n° 2011-100 ;
  loi n° 2005-59 ; LF 2000, art. 57 ; décret n° 2007-1870 (la NC 1/2008 qui le commente est au
  corpus).

**D9 — relectures à l'image** : LF 1995, art. 50-54, **p. 2046 confirmée** (« Imposition des
jetons de présence », 15 % par ajout d'un tiret à 52-I-b ; 2,5 % sur les intérêts des prêts
payés aux banques non établies). Code de 1990, art. 38-10 et 39, **p. 8 confirmée** à l'image.

**D10 — LF 2004, art. 61-63 : p. 3730 confirmée à l'image** (31 *bis* pour les cessions à partir
du 1/1/2004 ; 10 % ; exonérations du point 17 ; franchise de 10 000 D du point 18).

**D8 — SICAV** : non traité (pas de recherche).

**D1 — avant 1990.**
- **1968** : la LF 1968 (loi n° 67-57), art. 13, récrit l'article premier du décret organique du
  23 décembre 1918 : « taxe annuelle et obligatoire de 16,90 % (taux global général) ou de
  14,50 % (taux global réduit) » sur les revenus de valeurs mobilières et de créances « quelle
  qu'en soit la dénomination (dividendes, coupons, arrérages, intérêts, etc.) » ; « le taux global
  de l'impôt sur les revenus des créances, dépôts, cautionnements et comptes-courants est fixé à
  10 % à partir du 1er janvier 1968 » ; les obligations émises depuis le 1er juillet 1956 pour cinq
  ans au moins gardent 12,10 % et 9,10 %. Art. 14 : intérêts des bons de caisse soumis à l'impôt
  sur les revenus des créances ; si l'émetteur ne déclare pas les bénéficiaires, taxe
  additionnelle de 24 %, qui « remplace forfaitairement la part de la Contribution Personnelle
  d'État ». JORT n° 55 des 29-30 décembre 1967, p. 1649, **lu à l'image**. C'est l'ancêtre du taux
  libératoire sur les bons anonymes (35 % en 1990).
- **1988-1989 : un taux unique de 20 %, imputable.** LF 1988 (loi n° 87-83), art. 29, rubrique
  « Unification des taux de l'impôt sur les revenus des valeurs mobilières et de l'impôt sur les
  revenus de capitaux mobiliers » : « Sont soumis au taux de 20 % les revenus des valeurs
  mobilières non prévus par la loi n° 87-48 du 2 août 1987, ainsi que les jetons de présence et
  les revenus des capitaux mobiliers. Il est institué un crédit d'impôt au taux de 20 % des
  revenus indiqués au paragraphe 1er ci-dessus, à valoir sur la contribution personnelle d'État
  due par les personnes physiques. » Art. 30 : suppression de la contribution de solidarité sur
  ces revenus. Art. 23 : exonération de l'impôt sur les revenus des valeurs mobilières des
  bénéfices distribués par les sociétés exportatrices de la loi n° 84-20. JORT n° 91 des
  29-31 décembre 1987, p. 1630, **lu à l'image** (clé existante `loi-87-83-lf-1988`).
- Ce que le code de 1990 en reprend et en écarte : il garde la retenue par le payeur et son
  imputation (le crédit d'impôt de 1988 devient l'imputation de l'art. 54), et le taux pénalisant
  de l'anonymat (24 % en 1968, 35 % en 1990) ; il **écarte l'imposition des dividendes**, taxés à
  20 % en 1988-1989, exonérés en 1990 (art. 38-10), et **baisse le taux sur les intérêts** de 20 %
  à 15 %. Le taux de 20 % de 1997 retrouve celui de 1988.
- Entre 1968 et 1987 : non lu (lois de finances 1969-1987 ; la LF 1983, art. 24, « revenus des
  valeurs mobilières », et la LF 1984, art. 24, exonération des dépôts en devises, sont repérées
  dans l'index, non lues). Loi n° 87-48 (titres de participation, JORT n° 56 de 1987, p. 960) non
  lue.
- OCR : JORT n° 55 de 1967 et n° 91 de 1987, au premier plan, terminées ; chiffres relus à l'image.

**D2 — contexte, dans les sources de l'époque.** Pas d'exposé des motifs ni de rapport de
commission trouvés ; les rapports annuels de la BCT, contemporains, relaient les lois :
- **1992** — BCT, rapport annuel 1992 (`tunisia-data/data/raw/bct-archives/109/RA_fr_1992.pdf`,
  fichier p. 135 et 137, page imprimée à relever ; clé `bct-ra-1992`) : « Dans le cadre de la
  suppression des distorsions fiscales qui existent entre les diverses formes de placements, la
  loi de finances n° 91-98 pour la gestion 1992 a aligné les taux d'imposition qui grèvent les
  intérêts de l'épargne bancaire d'un côté et de l'épargne postale de l'autre » ; les comptes
  d'épargne-emprunts obligataires et les FCP sont créés « dans le cadre de l'encouragement des
  autorités monétaires à la mobilisation de l'épargne et afin de contribuer à la réalisation de la
  privatisation de certaines entreprises publiques ».
- **1997** — BCT, rapport annuel 1996 (fichier p. 177, couche texte décalée d'un cran, décodée ;
  page imprimée à relever) : sous « Renforcement des structures de fonctionnement du marché
  financier » (création du CMF, cotation électronique à la BVMT), « Sur le plan fiscal, le taux de
  la retenue à la source en matière d'impôts sur les revenus générés par les capitaux mobiliers a
  été unifié à 20 % » contre 15 %, 25 % et 35 %.
- **1999** — BCT, rapport annuel 2000 (fichier p. 231, couche décalée de trois crans, décodée) :
  « aucune nouvelle admission à la cote de la Bourse n'a été enregistrée, au cours de l'année
  2000, et ce, en dépit des incitations fiscales additionnelles décidées par la loi n° 99-92 du
  17 août 1999 pour encourager de nouvelles sociétés à s'introduire en Bourse ».
- **2003-2004** — BCT, rapport annuel 2003 (téléchargé le 20/10/2026 depuis
  https://www.bct.gov.tn/bct/siteprod/documents/rapport2003.pdf, rangé
  `tunisia-data/data/raw/bct-archives/109/RA_fr_2003.pdf`, SHA-256
  531f090d1f07bbe4b4a250141a243f271b3b946c7117ced17a4fa57fffd63aab ; l'adresse figure déjà dans
  `sources/bct-archives-urls.csv`, dont le format n'a pas de colonne de date ni d'empreinte) :
  p. 107, mesures adoptées pour « concrétiser […] les objectifs du Xème Plan », dont « la
  promotion de l'épargne longue destinée directement au financement des investissements par
  l'adoption de régimes fiscaux de faveur pour les titulaires de comptes épargne en actions et
  épargne pour l'investissement » ; p. 192, « en vue de lever les distorsions grevant les
  différents comptes d'épargne, il a été procédé à l'harmonisation de la fiscalité relative aux
  comptes d'épargne en actions et aux comptes d'épargne pour l'investissement » (relèvement de
  5 000 à 20 000 D). Le contexte de la plus-value de 2004 n'y est pas trouvé ; rapport 2004 non
  récupéré (adresse au catalogue).
- Ces rapports sont de famille budgétaire au sens large (relais de la loi) ; les citer comme
  rapports de la BCT, en les distinguant de « ce que la loi cherche » (rubriques).

**Corrections de la note faites ce jour** : § 1 et § 7 (« Intérêts dépôts et épargne » = CEA + CEI,
série par mesure 2017-2023, divergence des millésimes pour 2022) ; lacune 8 levée ; doublon
`lf-2002` / `loi2001-123-lf2002` signalé au § 10 ; cellule de juin 2020 du § 6 (35 % libératoire).
`docs/recherches.yml` et `docs/notes/backlog-precis.md` non modifiés.
