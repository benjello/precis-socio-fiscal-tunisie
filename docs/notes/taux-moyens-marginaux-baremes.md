# Taux moyens et taux marginaux des barèmes : inventaire et ordre de traitement

Note du 19 octobre 2026. Demande du propriétaire : « pour tous les barèmes, représenter les
taux moyens et marginaux sur un même graphe ».

## 1. Le composant

`scripts/taux_bareme.py`, testé par `tests/test_taux_bareme.py` (bibliothèque standard
seule, comme le job de tests ; le cas qui lit une série pandas est sauté sans pandas).

- **Entrée** : une série de tranches au format de `openfisca_tables.lignes_tranches` — une
  ligne par tranche et par date d'effet, colonnes `<clé>`, `tranche`, `date_effet`, `seuil`,
  `taux` —, lue par `figtools.series()` dans `precis/_seriescache/`. Le générateur l'émet par
  `ot.ecrire_serie_tranches` ; le build ne lit jamais les paramètres vifs.
- **Calcul pur** : `taux_marginal`, `montant_du`, `taux_moyen`, `bareme_a_la_date`, `grille`.
  Tranche i = de `seuil_i` exclu à `seuil_{i+1}` inclus (« 5 000,001 à 10 000 »). Montant dû
  **barème appliqué par tranche**. Taux moyen à assiette nulle : `None`, jamais 0.
- **Figure** : `fig_taux_moyens_marginaux(panneaux, …)` — un cadre par barème, des états
  datés superposés (une couleur par état), marginal en escalier (trait fin), moyen en courbe
  (trait épais) ; un état à taux unique est tracé une fois, et la légende dit que les deux
  taux se confondent ; un état identique au précédent est tireté par-dessus.
- **Données** : `table_taux(panneaux, libellés, assiettes)` — taux marginal et taux moyen
  par état, aux assiettes choisies (les seuils, en pratique). Le montant dû n'y figure que
  sur demande (`avec_montant=True`), et seulement si le tableau en donne aussi la valeur en
  dinars constants.
- **Libellés** FR/AR portés par le composant (« taux marginal (escalier) », « taux moyen
  (courbe) », en-têtes) ; ceux des cadres, des états, des axes et du titre par le module.

**Ancre de contrôle extérieure.** Le code de l'IRPP de 1990 imprime lui-même le taux
d'imposition du revenu global à la limite supérieure de chaque tranche (art. 44 § I). Le
test retrouve, tronqués, 10,50 %, 15,25 %, 20,12 % et 26,05 %.

**Ce que le composant ne sait pas faire.** Un barème dont le taux de la tranche atteinte
frappe toute l'assiette (« liquidé sur la valeur globale ») : le taux moyen y est le taux de
la tranche, et le droit fait un saut à chaque seuil. Il faudrait un mode
`tranche_atteinte` — taux moyen en escalier, pas de « taux marginal » au sens d'une
fonction en escalier (le saut du droit au seuil se lit mieux en montant qu'en taux). À
ajouter avant de traiter les barèmes marqués « valeur globale » ci-dessous.

## 2. Inventaire des barèmes à tranches

Colonnes : où (livre, chapitre) ; présentation actuelle ; série dans le snapshot
(`precis/_seriescache/`) ; mode d'application ; effort.

| Barème | Où | Présentation actuelle | Série au snapshot | Mode | Effort |
|---|---|---|---|---|---|
| Droit sur les successions, 1984, 1993, 1998 | Fiscalité, `_patrimoine_immobilier.qmd`, `fig-pi-tarif-successions` | figure + tableau | `successions-tarif` | 1984 : mode de liquidation non établi, taux de la tranche seul (fiche `r-liquidation-successions-1929`) ; taux unique depuis 1993 | **fait le 19/10/2026** |
| Droit sur les successions, 1969 et 1975 | même chapitre, `tbl-pi-baremes-successoraux` | tableau engendré depuis la série `successions-tarif` (fait le 19/10/2026, paramètres 0.136.1, PR openfisca-tunisia #495) | oui | à établir, comme 1984 | fait pour le tableau ; la figure garde les états de 1984, 1993 et 1998 (demande du propriétaire : pas de changement de figure) |
| Impôt sur le revenu (IRPP), 1990, 2017, 2025 | Fiscalité, `_impot_revenu.qmd`, tableaux `bareme_1990/2017/2025`, `bareme_generations` | tableaux engendrés, pas de figure | non | par tranche (art. 44 § I ; le texte de 1990 imprime le taux moyen aux limites) | **faible** : `lignes_tranches` passe sur `impot_revenu/bareme.yaml` sans erreur (18 lignes, dates 1990, 2017, 2025 ; essai sur la copie locale du modèle à 0.118, à refaire sur la version publiée) ; ajouter `ot.ecrire_serie_tranches("irpp-bareme", …)` à `generate_bareme_tables.py`, laisser la CI régénérer, puis une figure à un cadre et trois états |
| Contribution personnelle d'État, 1962-1986 | même chapitre, tableaux `bareme_cpe_*` (onglets) | tableaux engendrés | non | par tranche (tableaux à taux effectif imprimé) | **faible** : `lignes_tranches` passe sur `contribution_personnelle_etat/bareme.yaml` (116 lignes, 1962, 1965, 1980, 1983, 1986) ; même démarche ; figure à un cadre, cinq états, ou deux cadres (CPE, IRPP) pour la rupture de 1990 |
| Contribution sociale de solidarité des personnes physiques, depuis 2018 | Fiscalité, `_impot_revenu.qmd` (section CSS) ; Caisses, `_etat_caisses.qmd` | texte | non | différence entre l'impôt au barème majoré (1 point, ½ point de 2023 à 2025) et l'impôt au barème : barème dérivé de l'IRPP | moyen : dépend de la série IRPP ; références du paramètre à remplacer par des URL pist.tn (TODO existant) |
| Électricité, tarif des ménages en basse tension, 1984-2022 | Compensation, `_electricite_gaz.qmd`, `tbl-compensation-eg-grilles-*` | tableaux faits main | non (le paramètre `energie/electricite/tarifs_par_tranche.yaml` ne porte que 2024, sans source pist.tn) | par tranche jusqu'en 2022 ; **prix de la tranche atteinte** sur toute la consommation depuis 2022 ; prix en millimes par kWh, non des taux | élevé : verser les grilles datées en amont ; adapter le composant au prix (marginal et moyen par kWh) et au mode `tranche_atteinte` |
| Gaz naturel, basse pression | Compensation, `_electricite_gaz.qmd`, `tbl-compensation-eg-gaz` | tableau fait main | non | prix par tranche de consommation | élevé, même démarche que l'électricité |
| Droit complémentaire sur les ventes d'immeubles, depuis 2017 | Fiscalité, `_patrimoine_immobilier.qmd` | texte et tableaux | non | **valeur globale** (code, art. 20 *bis*) : taux de la tranche atteinte sur toute la valeur | moyen : mode `tranche_atteinte` à ajouter ; série à émettre |
| Impôt sur la fortune (immobilière), 2023-2026 | Fiscalité, `_impot_fortune.qmd`, `tbl-fortune-evolution` | tableaux | non | la loi ne dit pas si le taux frappe toute la valeur ou la fraction ; l'administration lit « valeur globale » | moyen, après le mode `tranche_atteinte` ; lecture à trancher par le texte |
| Régime forfaitaire des BIC, annexe II, 1990-2010 | Fiscalité, `_impot_revenu.qmd`, `tbl-forfait-annexe-2` | tableau | non | **montant** fixe par tranche de chiffre d'affaires, non un taux | hors composant tel quel : un « taux moyen » (montant / chiffre d'affaires) se calcule, pas un taux marginal ; à discuter |
| Contribution au budget de l'État, 2014 | Fiscalité (IRPP) | — | non | jours de salaire par tranche de revenu (montant) | hors composant ; pas prioritaire |
| Pension CNRPS, barème d'annuités de 1985 | Retraites, `_secteur_public.qmd` | tableau et formule | `retraites-taux-liquidation` (par durée) | tranches de **durée**, non d'assiette en dinars ; plafond de 90 % | hors objet : le « taux moyen par annuité » n'éclaire pas ; la série par durée nourrit déjà `fig-taux-liquidation` (`_secteur_prive.qmd`) |
| Compléments de pension 1981-1983 | Retraites, `_secteur_public.qmd` | liste | non | montants ou pourcentages par tranche de pension | faible intérêt ; pas prioritaire |
| Bourses scolaires, 1971-1974 | Éducation, `_aides.qmd` | tableau | non | points par tranche de revenu, non un taux | hors objet |
| Cotisations sociales (RSNA, RTFR…) | Cotisations sociales | tableaux par branche | non (tableaux engendrés) | taux uniques pour la plupart ; deux tranches pour certaines cotisations du RTFR | à examiner branche par branche : un taux unique ne fait pas diverger moyen et marginal ; pas pour ce chantier |
| Taxe sur les terrains non bâtis, taxe sur les immeubles bâtis | Finances locales | figures en escalier dans le temps | `fl-tnb-tarif`, `fl-tib-prix-reference` | tarifs par zone ou catégorie, non par tranche d'assiette | hors objet |
| Accidents du travail (classes, 1995, 1999) | Cotisations sociales | tableaux | `atmp-echelles-1995-1999` | taux par classe de risque, non par tranche d'assiette | hors objet |

## 3. Application faite le 19 octobre 2026

Une seule série de tranches est au snapshot : `successions-tarif`. Le composant y est
appliqué : `fig-pi-tarif-successions` trace, pour quatre parentés, le taux marginal et le
taux moyen aux états du 1er janvier 1984, du 17 mai 1993 et du 17 août 1998 ; l'onglet
« Données » donne taux marginal et taux moyen aux seuils de 1984 et à 120 000 D.

Le mode de liquidation du barème de 1984 n'est établi par aucun texte de 1962 à 1984
(`docs/notes/successions-liquidation-1969-1984.md`) : la figure ne trace pour 1984 que le
taux de la tranche, sans courbe de taux moyen (`SANS_MOYEN` dans
`figures/patrimoine_immobilier.py`, option `sans_moyen` du composant). Un TODO documentaliste
et la fiche `r-liquidation-successions-1929` disent quoi refaire une fois le décret du
28 décembre 1929 lu : rétablir la courbe si la liquidation est par tranches, ou ajouter le
mode « tranche atteinte ».

## 4. Ordre de traitement proposé

1. **IRPP** (1990, 2017, 2025) — *fait le 19 octobre 2026, `fig-irpp-taux-bareme`* : effort faible, intérêt le plus fort (le chapitre a déjà ses
   tableaux et le taux moyen imprimé en 1990 sert de contrôle). Émettre la série dans
   `generate_bareme_tables.py`, laisser la CI régénérer le snapshot, puis une figure dans
   `_impot_revenu.qmd` près de `bareme_generations`.
2. **Contribution personnelle d'État** (1962-1986) — *fait le 19 octobre 2026, `fig-cpe-taux`, deux cadres d'échelles différentes ; le barème de 1990 est sur la figure de l'IRPP, non sur celle-ci* : même générateur, même démarche ; une
   figure qui place les cinq barèmes de la CPE et celui de 1990 permet de voir la rupture de
   1990 en taux moyen (68 % de taux marginal supérieur → 35 %).
3. **Mode `tranche_atteinte`** dans le composant, puis le **droit complémentaire de 2017** et
   l'**impôt sur la fortune** (après lecture du texte sur le mode).
4. **Successions de 1969 et 1975** : barèmes versés en amont (0.136.1) et tableau du chapitre engendré le 19 octobre 2026 ; la figure ne change pas.
5. **CSS des personnes physiques** : courbe dérivée du barème de l'IRPP, après 1.
6. **Électricité et gaz** : composant à adapter aux prix ; grilles datées à verser en amont.
   Chantier le plus lourd.
7. Hors objet ou à discuter : forfait BIC, contribution au budget de l'État, barèmes de
   durée (retraites), points (bourses), plafonds de cotisations.
