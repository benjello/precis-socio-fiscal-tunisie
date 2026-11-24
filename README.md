# L'économie publique de la Tunisie

Population, production, revenus et action de l'État

Un ouvrage de référence en accès libre, en français et en arabe : histoire des politiques publiques, textes
de mise en œuvre, chiffres et analyse économique. Il retrace règle par règle l'évolution des
politiques publiques tunisiennes, sociales et fiscales d'abord, depuis l'indépendance, chaque valeur
datée et renvoyée au *Journal officiel*.

**À lire en ligne : <https://benjello.github.io/precis-socio-fiscal-tunisie/>** — chaque volume se
télécharge aussi en PDF.

## Les volumes

Seize volumes, rangés en neuf parties qui suivent la séquence des comptes nationaux (voir
`precis/fr/principes-structure.qmd`). Les parties 0 (le cadre), V (l'utilisation du revenu), VII
(le reste du monde) et VIII (la synthèse) n'ont pas encore de volume.

| Partie | Volume | Objet |
|---|---|---|
| I. La production | L'agriculture | crédit bonifié, encouragements à l'investissement, eau d'irrigation, calamités et assurance, intrants, dépense du ministère de l'Agriculture |
| | Le transport | infrastructure financée par l'État, contrats-programmes et subventions aux opérateurs publics, dépense des missions « Transport » et « Équipement » |
| | L'environnement | assainissement des eaux usées, gestion des déchets, dépollution industrielle : institutions, dépense publique, rapports |
| II. La formation des revenus | Marché du travail | salaire minimum, conventions collectives et négociations salariales du secteur privé |
| | Rémunérations publiques | statuts, grilles, indemnités des agents publics |
| | L'informel : définitions et mesures | secteur informel, emploi informel, économie informelle : définitions internationales, manières de les mesurer, estimations pour la Tunisie |
| | Compensation | la Caisse générale de compensation et les subventions aux prix : produits de base, carburants, transport |
| III. La distribution secondaire du revenu | Fiscalité | l'impôt sur le revenu et les autres impôts |
| | Finances locales | fiscalité locale, transferts de l'État et budgets des collectivités locales |
| | Cotisations sociales | taux, assiettes et plafonds des prélèvements sur les revenus du travail |
| | Caisses de sécurité sociale | la CNSS, la CNRPS et la CNAM : leur lignée, leur statut, leurs comptes par régime et leurs relations avec l'État |
| | Retraites | les régimes de retraite des secteurs public et privé |
| | Prestations sociales | aide et assistance sociales, soutien à l'emploi, prestations familiales |
| IV. La redistribution en nature | Santé | couverture des soins, hôpital public, médecine de ville, rémunération des soignants et transferts non monétaires |
| | L'éducation et la formation | histoire des lois du système éducatif, aides aux élèves et aux étudiants, dépense publique d'éducation |
| VI. L'accumulation | Entreprises publiques | transferts, garanties, dettes croisées, dividendes et cessions |

Chaque dispositif y est présenté dans son histoire, réforme par réforme, avec des tableaux datés
et des liens vers les textes. C'est un travail en cours : certains chapitres sont complets,
d'autres encore à l'état d'ébauche.

## Contribuer

L'ouvrage a besoin de lecteurs qui connaissent le terrain : pour signaler une erreur, pour indiquer
un document introuvable — rapport d'activité, annuaire statistique, circulaire, thèse —, pour dire
ce qui manque. Aucune compétence technique n'est requise. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Organisation du dépôt

- `precis/fr/<volume>/` — les volumes en français, source de vérité ; `precis/ar/<volume>/` — leur
  version arabe, produite par traduction automatique et jamais modifiée à la main ;
- `precis/glossaire.yml` — le glossaire bilingue ; `precis/*/references.json` — la bibliographie ;
- `scripts/` — génération des tableaux et des figures, contrôles, traduction ;
- `docs/` — conventions de rédaction, notes de travail, registre des recherches en cours.

Les tableaux de paramètres sont engendrés depuis
[OpenFisca-Tunisia](https://github.com/openfisca/openfisca-tunisia), le modèle de microsimulation
du système socio-fiscal tunisien, dont l'arbre de paramètres sert de base de données de la
législation.

## Construire le site

Il faut [uv](https://docs.astral.sh/uv/) et [Quarto](https://quarto.org/).

```
./build.sh              # tous les volumes, en français et en arabe, dans local_site/
./build.sh --no-pdf     # sans les PDF, plus rapide
scripts/verifier.sh     # contrôles, tests et rendu des volumes modifiés
```

Les conventions de rédaction sont dans [`docs/conventions-redaction.md`](docs/conventions-redaction.md),
celles qui s'adressent aux agents dans [`AGENTS.md`](AGENTS.md).

## Licence

L'ouvrage est sous licence CC BY-SA 4.0, les programmes sous AGPL-3.0-or-later. Voir
[`LICENSE.md`](LICENSE.md) ; pour citer l'ouvrage, [`CITATION.cff`](CITATION.cff).
