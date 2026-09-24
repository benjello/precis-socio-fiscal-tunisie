# Le livre « Cotisations sociales » : plan de réorganisation

Validé par l'humain le 24 septembre 2026. Le livre, aujourd'hui découpé **par régime**, est
réorganisé **par branche** (pensions, maladie, famille, accidents du travail, emploi,
complémentaire), selon le plan type de tout dispositif du précis : origines → état initial →
réformes → longue période. Les régimes ne reviennent qu'en partie 5, secteur privé puis secteur
public, dans des fiches courtes qui ne gardent que leurs singularités.

## Pourquoi

- **Éviter les redites.** Le découpage par régime répète la même histoire (retraite, maladie,
  famille) à chaque régime, et la répète encore dans le livre « Retraites ».
- **Le plan type s'applique aux branches**, qui ont chacune une histoire : quote-part de la loi
  n° 60-30 et cotisation propre de 1974 pour les pensions, assurances sociales de 1960 puis CNAM
  pour la maladie, loi n° 94-28 pour les accidents du travail, fonds récents pour l'emploi.
- **Les régimes diffèrent par peu de choses** — qui paie, sur quelle assiette, à quel taux — que
  les tableaux engendrés `branches_<régime>` et `coin_par_regime` montrent mieux qu'un récit.

## Règle de partage avec les autres livres

| Livre | Ce qu'il porte |
|---|---|
| Cotisations sociales | ce qui est **prélevé** : taux et assiette de chaque branche, leur histoire |
| Retraites, Prestations sociales | ce qui est **servi** (formule, conditions) et l'équilibre (τ*) |

Les Retraites ne gardent que le symbole κ (taux légal) et renvoient aux tableaux des
Cotisations, sans raconter l'histoire des taux. Les renvois entre livres sont vérifiés un à un.

## Sommaire

Ancres entre accolades ; « (existant) » : repris du texte actuel.

### 1. Présentation générale `{#sec-cot-presentation}` (existant, réordonné)
- 1.1 Cotisation et impôt
- 1.2 La carte des régimes — privé (CNSS), public (CNRPS) ; renvoi à la partie 5
- 1.3 Une architecture en deux étages
- 1.4 La datation des taux — règle de date d'effet ; tableaux engendrés, onglet « Base législative »
- 1.5 Ce que ce livre traite et ne traite pas — la règle de partage

### 2. L'assiette `{#sec-cot-assiette}`
- 2.1 Le salaire réel et ses éléments — privé (loi n° 60-30) ; public (éléments permanents de la
  rémunération, renvoi aux Retraites et aux Rémunérations publiques)
- 2.2 Plafonds et limites (six SMIG du régime complémentaire, etc.)
- 2.3 Les assiettes forfaitaires, regroupées :
  - 2.3.1 classes de revenu — non-salariés, artistes, Tunisiens à l'étranger ;
  - 2.3.2 salaire minimum agricole — SMAG × 45 jours par trimestre (loi n° 81-6), période de
    référence 180 / 260 / 300 jours ;
  - 2.3.3 assiettes réduites — faibles revenus, étudiants
- 2.4 L'assiette des pensionnés
- 2.5 Tableau de synthèse des assiettes par régime

### 3. Le taux global et le coin social `{#sec-cot-taux-global}`
- 3.1 Le taux unique de 1960 et la répartition en vingtièmes (loi n° 60-30)
- 3.2 Du taux global aux taux par branche — textes qui fixent la ventilation, et ceux qui la
  laissent sans source
- 3.3 Le coin social par régime (tableau engendré `coin_par_regime`)
- 3.4 Part patronale, part salariale, cotisation de l'assuré

### 4. Les branches, une à une
Dans chacune : origines → état initial → réformes, **privé** puis **public** → longue période ;
taux en tableaux engendrés, jamais en chiffres isolés.

- **4.1 Pensions** `{#sec-cot-pensions}`
  - 4.1.1 Origines
  - 4.1.2 Privé — quote-part du taux global (1,25/20^e^ en 1974 → 4,25, 6,25, 7,25) ; cotisation
    propre (décret n° 74-499) ; réformes de 1988, 1994, 1997, 2002-2003 ; loi n° 2007-43 ; 2019
  - 4.1.3 Public — taux de 1959, fusion de 1975, lois de finances ; loi n° 2007-43 ; loi
    n° 2019-37 ; contribution de 2011
  - 4.1.4 Longue période — κ par régime ; renvoi aux Retraites (prestations, équilibre)
- **4.2 Assurance maladie** `{#sec-cot-maladie}`
  - 4.2.1 Origines — les « assurances sociales » de 1960 (maladie, maternité, décès)
  - 4.2.2 Privé — taux et ventilation, parts non fixées par un texte
  - 4.2.3 Public — agents et pensionnés
  - 4.2.4 La réforme de 2004 — CNAM, taux unifié
  - 4.2.5 Longue période
- **4.3 Prestations familiales** `{#sec-cot-famille}` (privé)
  - 4.3.1 Part du taux global de 1960 ; 4.3.2 évolution ; 4.3.3 renvoi aux Prestations
- **4.4 Accidents du travail et maladies professionnelles** `{#sec-cot-at}`
  - 4.4.1 Avant 1994 ; 4.4.2 loi n° 94-28 (taux selon le risque) ; 4.4.3 longue période
- **4.5 Perte d'emploi, protection sociale des travailleurs, fonds de l'État** `{#sec-cot-emploi}`
  - 4.5.1 Fonds spécial de l'État ; 4.5.2 protection sociale des travailleurs ; 4.5.3 perte
    d'emploi (loi n° 96-101, fonds récents ; renvoi aux Prestations)
- **4.6 Retraite complémentaire facultative** `{#sec-cot-complementaire}` (privé)
  - 4.6.1 Règlement de 1978, assiette différentielle ; 4.6.2 taux, adhésion ; 4.6.3 renvoi aux
    Retraites

### 5. Ce qui distingue les régimes `{#sec-cot-regimes}`
Fiche courte par régime : qui paie, sur quelle assiette, ce qui déroge, tableau engendré
`branches_<régime>` ; renvois aux parties 2 et 4, pas de taux répétés.

- **5.1 Secteur privé (CNSS)** — 5.1.1 salariés non agricoles (régime de référence) ; 5.1.2
  salariés agricoles ; 5.1.3 régime agricole amélioré ; 5.1.4 travailleurs non salariés
  (l'assuré paie seul) ; 5.1.5 artistes, créateurs et intellectuels ; 5.1.6 travailleurs à
  faibles revenus ; 5.1.7 Tunisiens à l'étranger ; 5.1.8 étudiants ; 5.1.9 travailleuses
  agricoles (décret-loi n° 2024-4, prise en charge par l'État)
- **5.2 Secteur public (CNRPS)** — 5.2.1 agents civils et militaires (régime de référence) ;
  5.2.2 part patronale (État, collectivités, établissements publics) ; 5.2.3 régimes spéciaux
  (membres du gouvernement, députés, gouverneurs) ; 5.2.4 pensionnés

### 6. Recouvrement, rendement, vue d'ensemble (existant)
- 6.1 Recouvrement ; 6.2 ce que les cotisations rapportent ; 6.3 vue d'ensemble (matrice
  régime × branche)

### Annexes
- Notations du livre (κ, etc.) ; textes modificatifs par branche

## Méthode

- Contrôle de non-perte avant/après : citations (clé + locator), ancres `{#…}`, appels
  `table()`, liens `#g-`, ancres `RECHERCHE`, figures.
- Ancres de compatibilité : les anciennes ancres des sections par régime restent sur les fiches
  de la partie 5 ; tous les renvois des autres livres (`@sec-…`, `@tbl-…`) sont vérifiés.
- Renvois des Retraites (18 passages vers ce livre) vérifiés ; redites sur les taux retirées des
  Retraites au profit d'un renvoi.
- Trois PR : parties 1-3 ; partie 4 ; parties 5-6 et annexes. Contrôle : `scripts/verifier.sh`.
