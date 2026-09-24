# Le livre « Fiscalité » : ajustements au plan type

Validé par l'humain le 24 septembre 2026. Le livre est déjà découpé par impôt, et la plupart des
chapitres suivent le plan type d'un dispositif (origines → état initial → réformes → longue
période) : pas de refonte, des ajustements ciblés, une PR par chapitre.

| Chapitre | Écart au plan type | Ajustement |
|---|---|---|
| Impôt sur les sociétés | aucun | modèle des autres chapitres ; ne pas toucher |
| IRPP | le calcul précède l'institution de 1989 ; évolution par élément | ordre : origines → institution de 1989-1990 → calcul, avec une **formule** (revenu net → abattements → barème → minimum ; symboles dans la formule, valeurs en égalités datées, annexe de notations) → évolution par élément (barème, assiette, charges de famille, minimum), **gardée** car plus lisible pour un impôt à nombreux paramètres, + **tableau récapitulatif des réformes** (vue réforme par réforme) |
| Droits de consommation | réformes racontées comme « chronologie du périmètre » | section « L'évolution, réforme par réforme » sur le modèle de l'IS ; « Longue période » avant le rendement |
| TVA | chapitre mince, réformes postérieures à 1988 esquissées | recherche documentaire au JORT (lois de finances successives : taux, champ, régimes), puis section de réformes datées et longue période |
| Présentation (`index.qmd`) | trop mince | vue d'ensemble : carte des impôts (direct, indirect), part de chacun dans les recettes (figures existantes), règle de partage avec le livre des Cotisations |

Méthode : contrôle de non-perte (citations, ancres, `table()`, figures, liens `#g-`, ancres
`RECHERCHE`), ancres conservées, `scripts/verifier.sh fiscalite`, une PR par chapitre, fusion
après CI verte.
