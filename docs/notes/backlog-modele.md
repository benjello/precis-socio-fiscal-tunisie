# Ce que la rédaction du précis a constaté sur openfisca-tunisia

Le précis ne parle jamais du modèle (voir `docs/conventions-redaction.md`, § 1). Ce qu'il
constate en s'appuyant sur ses paramètres atterrit donc ici, et dans une *issue*.

Ce fichier existe pour deux raisons : qu'un constat ne se perde pas entre le moment où on le
fait et celui où quelqu'un le corrige, et qu'on ne le refasse pas deux fois.

## Ouvert

| Constat | Issue | Relevé par |
|---|---|---|
| L'assiette de la retraite complémentaire est bien différentielle dans la formule, mais sa limite de six SMIG est une constante du code, sans date ni référence, alors que le décret n° 74-499 et ses modificatifs la font varier | [#399](https://github.com/openfisca/openfisca-tunisia/issues/399) | dossier cotisations, secteur privé § 1.8 |
| Le paramètre « accident du travail » du RSNA est le point transféré par le décret n° 95-538, non le tarif AT/MP — lequel est patronal, varie de 0,50 % à 5 % sur dix-huit classes, et manque entièrement | [#400](https://github.com/openfisca/openfisca-tunisia/issues/400) | dossier cotisations, secteur privé § 1.4 |
| Les quatre valeurs du régime des bas revenus croisent deux répartitions que les textes énoncent séparément ; et son seuil de 0,66 SMIG est codé en plafond alors que c'est une assiette forfaitaire | [#401](https://github.com/openfisca/openfisca-tunisia/issues/401) | dossier cotisations, secteur privé § 6.2 |
| Les assiettes forfaitaires par classes de revenu — travailleurs non salariés, artistes, Tunisiens à l'étranger — et les coefficients du régime agricole ne sont modélisés pour aucun régime. Le SMAG lui-même manque | [#401](https://github.com/openfisca/openfisca-tunisia/issues/401) | idem |
| Maternité et décès sont intervertis entre les travailleurs non salariés et les artistes, dont l'architecture est identique : l'une des deux répartitions est fausse, aucun texte ne dit laquelle | [#401](https://github.com/openfisca/openfisca-tunisia/issues/401) | idem |
| La variante conventionnelle du régime général — 11 % au lieu de 13 % à la charge de l'employeur, du 1er octobre 1996 au 1er juillet 2007 — est absente | [#410](https://github.com/openfisca/openfisca-tunisia/issues/410) | dossier cotisations, secteur privé § 1.2 |
| Les deux premiers paliers d'assurance maladie du régime des salariés agricoles (1er juillet 2007 et 1er juillet 2008) s'écartent de cinq et de deux centièmes de point des valeurs de l'article 7 du décret n° 2007-1406 ; les trois derniers sont exacts | [#412](https://github.com/openfisca/openfisca-tunisia/issues/412) | dossier cotisations, secteur privé § 2 |
| Les trois parts du taux global du RSNA obtenues par solde — prestations familiales 3,10 %, indemnités maladie-maternité 0,85 %, décès 0,65 % — ne sont fixées par aucun texte lu. À chercher du côté d'une décision du conseil d'administration de la CNSS | [#411](https://github.com/openfisca/openfisca-tunisia/issues/411) | dossier cotisations, secteur privé § 10 A.1 |
| Le salaire de référence retient les *meilleures* années là où les textes disent les *dernières* (RSNA, RSA) ; au CNRPS, la branche « fonction la plus élevée » est appliquée aux deux salaires les plus élevés | [pension#24](https://github.com/openfisca/openfisca-tunisia-pension/issues/24) | dossier retraites § 6.3 |
| La pension minimale de 0,4 SMAG du RSA n'est appuyée par aucun texte : la loi n° 81-6 ne prévoit aucun plancher pour ce régime | [pension#26](https://github.com/openfisca/openfisca-tunisia-pension/issues/26) | dossier retraites § 3.3 |
| L'âge minimum de 50 ans des mères de trois enfants n'a pas de texte et contredit la jouissance immédiate de l'article 41 nouveau (loi n° 88-71) | [pension#27](https://github.com/openfisca/openfisca-tunisia-pension/issues/27) | dossier retraites § 11 |
| Les paramètres de départ des fonctions astreignantes sont datés du décret n° 85-1178 au lieu de l'article 28 de la loi n° 85-12, et bloquent tout calcul CNRPS avant le 24 septembre 1985 | [pension#28](https://github.com/openfisca/openfisca-tunisia-pension/issues/28) | PR pension#25 |
| Les bonifications CNRPS sont calculées en dur ; les paramètres de l'article 32 ne sont lus par aucune formule | [pension#29](https://github.com/openfisca/openfisca-tunisia-pension/issues/29) | dossier retraites § 11 |
| L'indemnité familiale du 4e rang est appliquée à tout enfant au-delà du troisième, sans le test des droits acquis avant 1989 (loi n° 88-39) | [pension#30](https://github.com/openfisca/openfisca-tunisia-pension/issues/30) | lecture de la loi n° 88-39 |
| Sans conjoint, le total des pensions d'orphelins est plafonné à la pension de l'agent ; l'article 46 nouveau (loi n° 2007-43) ne pose pas ce plafond | [pension#31](https://github.com/openfisca/openfisca-tunisia-pension/issues/31) | PR pension#25 |
| `rsa.periode_remplacement_base` n'a aucun texte (la loi n° 81-6 dit 3 ou 5 dernières années) ; documentation de `cadres_actifs` à reprendre | [pension#32](https://github.com/openfisca/openfisca-tunisia-pension/issues/32) | PR pension#25 |
| Le rapport d'audit des sources rattache quatre textes à leur rectificatif ou à un homonyme | [pension#33](https://github.com/openfisca/openfisca-tunisia-pension/issues/33) | PR pension#25 |
| Les indemnités spéciales de 1989-1991 sont comptées comme SMIG et SMAG (123,016 au lieu de 120,016 en 1990) ; SMIG 2026-2028 et SMAG depuis 2020 manquants ; dates de signature du SMAG | [#403](https://github.com/openfisca/openfisca-tunisia/issues/403) | note revalorisation § 11 |
| La revalorisation des pensions est absente, paramètre comme formule, dans les trois régimes : montant forfaitaire indexé sur le SMIG (1981-2000), puis taux de variation du SMIG 48 h (2001) au RSNA ; SMAG au RSA ; péréquation au CNRPS | [pension#38](https://github.com/openfisca/openfisca-tunisia-pension/issues/38) | note revalorisation § 1 et § 5 |
| Le taux global de 9 % du régime complémentaire (6 points employeur, 3 points salarié) n'est pas attesté par l'arrêté du 18 novembre 1978, qui fixe un taux d'appel initial de 4,5 % et confie ses révisions à l'organisme gestionnaire | [#408](https://github.com/openfisca/openfisca-tunisia/issues/408) | note bibliographique `arrete-1978-11-18-retraite-complementaire` |
| Le capital-décès est daté du 1er février 1993 (décret n° 93-308) ; selon la doctrine de la CNRPS, le décret n° 74-572 régit les affiliés décédés avant le 1er juillet 1993 : date de bascule à confronter | [pension#39](https://github.com/openfisca/openfisca-tunisia-pension/issues/39) | note bibliographique `decret74-572` |
| Le titre arabe de la référence à la loi n° 88-16 (retraite des gouverneurs) la date par erreur de 1983 | [#409](https://github.com/openfisca/openfisca-tunisia/issues/409) | note bibliographique `loi88-16` |
| Aucun calcul CNRPS n'aboutit avant le 12 septembre 1985 : les conditions d'ouverture du droit commencent à la loi n° 85-12, et la loi n° 59-18 n'a pas été lue pour la période antérieure ; le barème d'annuités de 1959, sourcé, devient inatteignable | [pension#36](https://github.com/openfisca/openfisca-tunisia-pension/issues/36) | PR pension#25 et #35 |
| Les paramètres « astreignants » portent l'âge de mise à la retraite de l'article 28, non un départ anticipé sur demande ; le même âge existe en double sous `age_legal.civil` | [pension#37](https://github.com/openfisca/openfisca-tunisia-pension/issues/37) | PR pension#35 |
| Les indemnités spéciales de 1989-1992 ne sont lues par aucune formule : une rémunération minimale simulée est inférieure à celle qui était servie | [#406](https://github.com/openfisca/openfisca-tunisia/issues/406) | note revalorisation § 1.5 |
| Neuf valeurs du SMAG (1991-2008), le palier de décembre 2012 et la date d'effet du décret n° 2022-768 ne sont pas lus au fascicule | [#407](https://github.com/openfisca/openfisca-tunisia/issues/407) | note revalorisation § 3.2 |

## Réglé

| Constat | Réglé par |
|---|---|
| Le palier salarié du 1er juin 2019 de la retraite CNRPS n'existe pas : l'article 4 de la loi n° 2019-37 place le point entier au 1er janvier 2020 | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) |
| La deuxième marche patronale de la loi n° 2007-43 tombe en janvier 2008, non en juillet | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) |
| La prévoyance sociale des pensionnés commençait en 1959 sans texte ; elle s'ancre au décret n° 2007-1406 | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) |
| Trente-sept valeurs du secteur privé portaient le 1er janvier 1960, date qu'aucun texte ne soutient | [#398](https://github.com/openfisca/openfisca-tunisia/pull/398) |
| La cotisation des étudiants commençait à 5 dinars, sans son premier palier de 2 dinars | [#398](https://github.com/openfisca/openfisca-tunisia/pull/398) |
| Les références pointaient vers un dépôt GitLab personnel, natlex, ou un site commercial | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) et [#398](https://github.com/openfisca/openfisca-tunisia/pull/398) |
