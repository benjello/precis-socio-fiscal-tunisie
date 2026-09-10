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
| La variante conventionnelle du régime général — 11 % au lieu de 13 % à la charge de l'employeur, du 1er octobre 1996 au 1er juillet 2007 — est absente | à ouvrir | dossier cotisations, secteur privé § 1.2 |
| Les deux premiers paliers d'assurance maladie du régime des salariés agricoles (1er juillet 2007 et 1er juillet 2008) s'écartent de cinq et de deux centièmes de point des valeurs de l'article 7 du décret n° 2007-1406 ; les trois derniers sont exacts | à ouvrir | dossier cotisations, secteur privé § 2 |
| Les trois parts du taux global du RSNA obtenues par solde — prestations familiales 3,10 %, indemnités maladie-maternité 0,85 %, décès 0,65 % — ne sont fixées par aucun texte lu. À chercher du côté d'une décision du conseil d'administration de la CNSS | à ouvrir | dossier cotisations, secteur privé § 10 A.1 |

## Réglé

| Constat | Réglé par |
|---|---|
| Le palier salarié du 1er juin 2019 de la retraite CNRPS n'existe pas : l'article 4 de la loi n° 2019-37 place le point entier au 1er janvier 2020 | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) |
| La deuxième marche patronale de la loi n° 2007-43 tombe en janvier 2008, non en juillet | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) |
| La prévoyance sociale des pensionnés commençait en 1959 sans texte ; elle s'ancre au décret n° 2007-1406 | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) |
| Trente-sept valeurs du secteur privé portaient le 1er janvier 1960, date qu'aucun texte ne soutient | [#398](https://github.com/openfisca/openfisca-tunisia/pull/398) |
| La cotisation des étudiants commençait à 5 dinars, sans son premier palier de 2 dinars | [#398](https://github.com/openfisca/openfisca-tunisia/pull/398) |
| Les références pointaient vers un dépôt GitLab personnel, natlex, ou un site commercial | [#397](https://github.com/openfisca/openfisca-tunisia/pull/397) et [#398](https://github.com/openfisca/openfisca-tunisia/pull/398) |
