# Réserve — le barème AT/MP rapproché des accidents observés par activité

**État : en réserve, non publié.** Retiré du chapitre « Les accidents du travail et les maladies
professionnelles » (`precis/fr/cotisations_sociales/_accidents_travail.qmd`) le 6 octobre 2026,
au lendemain de son ajout, parce que l'exercice n'est pas assez solide pour être publié. Il est
conservé ici, avec les critiques qui l'ont fait retirer, pour être repris si elles peuvent un
jour être levées.

## L'exercice

Rapprocher, activité par activité, le taux de cotisation du barème de 1999 (décret n° 99-1010) et
la sinistralité publiée par la CNAM pour 2021-2023 : fréquence des accidents avec arrêt pour
1 000 travailleurs assujettis, et accidents mortels pour 1 000 accidents déclarés. Dix activités
seulement sont retenues, celles dont le libellé CNAM rejoint un point du barème à taux unique.

L'idée de fond reste pertinente : une tarification par activité est censée suivre le niveau de
risque, et la comparer à la sinistralité observée est la manière naturelle d'en apprécier la
cohérence.

## Ce qui est conservé

| Élément | Emplacement |
|---|---|
| Module de la figure (deux nuages de points, tableau) | `precis/fr/cotisations_sociales/figures/atmp_secteurs.py` |
| Données de la figure, telles qu'engendrées le 5 octobre 2026 | `precis/fr/cotisations_sociales/figdata/fig_atmp_secteurs.csv` et `.csv.yml` |
| Texte de la section et appel de la figure | ci-dessous, à l'identique |
| Séries de la CNAM | dépôt `tunisia-data` |

Le module n'est plus appelé par aucun chapitre : il n'est donc plus exercé par le rendu, et peut
cesser de fonctionner sans que rien le signale. Le rejouer avant de s'y fier.

## Les critiques

### Celle d'une relectrice qui a travaillé à l'évaluation du régime (6 octobre 2026)

Avis : ne pas retenir le graphique dans sa forme actuelle, et ne pas le présenter comme un moyen
de comparer directement les taux et la sinistralité par activité.

- **La classification des employeurs par activité n'est pas fiable.** La CNSS classe les
  employeurs selon la nomenclature NAT61. Un employeur peut y être rattaché à une activité qui
  n'est pas son activité réelle. Les statistiques de sinistralité par activité en sont affectées,
  et le rapprochement risque de donner une image qui ne reflète pas le niveau réel de risque.
- **Un chantier de fiabilisation est en cours** : rapprochement avec les données de l'INS, en
  s'appuyant sur la NAT2009 et sur le tableau de correspondance NAT61–NAT2009.
- **L'analyse gagnerait à être refaite après ce chantier**, sur une classification fiabilisée.

Ces constats viennent d'un échange privé. Ils ne sont appuyés ici sur aucun document publié :
ils ne peuvent pas être cités dans le précis en l'état.

### Celles que le texte retiré reconnaissait déjà

- Le barème et les statistiques ne mesurent pas la même chose : un taux en pourcentage des
  salaires d'un côté, des accidents rapportés aux travailleurs ou aux accidents déclarés de l'autre.
- Le barème de 1999 n'est pas le taux effectivement payé de 2021 à 2023 ; la majoration et la
  réduction individuelles ne sont pas observées.
- Le rapprochement des intitulés avec le décret est une lecture éditoriale, non un tableau de
  passage officiel ; quinze rubriques sur vingt-cinq sont écartées.
- Dix points par année : les droites d'ajustement et les corrélations n'ont guère de portée.
- Le champ de la CNAM inclut des travailleurs occasionnels des chantiers publics, hors du barème
  montré ; la fréquence de 2023 utilise les assujettis de 2022 ; les décès comprennent le trajet.

## Ce qu'il faudrait pour le republier

1. Une source **publiée** sur la qualité de la classification des employeurs par activité, ou des
   statistiques de sinistralité établies sur une classification fiabilisée (NAT2009).
2. Un tableau de passage, officiel ou documenté, entre les rubriques de la CNAM et les points du
   barème — par les codes d'activité, non par les libellés.
3. Si possible, les cotisations effectivement appelées par activité, plutôt que le taux légal.
4. Renoncer aux droites de tendance et aux corrélations tant que le nombre d'activités comparables
   reste aussi faible.

## Le texte retiré

Reproduit tel qu'il figurait dans le chapitre. Les clés de citation et les ancres sont celles du
volume des cotisations sociales.

~~~~markdown
## Le barème et les accidents observés par activité {#sec-cot-at-sinistralite}

Le barème de cotisation du décret n° 99-1010 et les statistiques d'accidents ne mesurent pas la même chose. Le premier fixe des taux **en pourcentage des salaires**, par activité de l'employeur affilié à la CNSS **après transfert du point** [@decret99-1010, art. 1^er^, art. 2 nouveau du décret n° 95-538] ; les secondes comptent les accidents déclarés à la CNAM et rapportent les **accidents avec arrêt** au nombre de travailleurs assujettis, pour 1 000 travailleurs [@cnam-statistiques-atmp-2023, pp. PDF 4, 13 et 15]. Les décès déclarés comprennent ceux survenus au travail et ceux sur le trajet [@cnam-statistiques-atmp-2023, pp. PDF 24 et 26].

La figure rapproche **dix activités** dont le libellé CNAM correspond à un point précis du barème de 1999, ou à des sous-activités qui portent **toutes le même taux** — c'est le cas des dix branches alimentaires. Elle ne fabrique pas de taux moyen pour la chimie, les transports, les services ou les autres rubriques qui regroupent plusieurs points à taux différents. Deux nuages de points placent le taux du **barème de 1999 en abscisse** : la fréquence des accidents avec arrêt en ordonnée dans le premier, puis le nombre d'accidents mortels **rapporté à 1 000 accidents déclarés** dans le second. Les trois couleurs donnent l'évolution **2021–2023**, avec une droite de tendance et une corrélation calculées séparément pour chaque année ; les nombres d'accidents et de décès restent consultables dans l'onglet « Données ». Ce rapprochement descriptif n'établit ni le taux effectivement payé par chaque employeur ces années-là, ni un effet de la cotisation sur le risque.

```{python}
#| label: fig-atmp-secteurs
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")
from figures import atmp_secteurs as atsec
import figtools
figtools.figure_tabs(
    [("Accidents avec arrêt", atsec.fig_accidents()),
     ("Accidents mortels", atsec.fig_mortalite())], atsec.table(),
    "atmp-echelles-1995-1999", "cnam-atmp-2023-ventilations-brutes",
    "cnam-atmp-2023-activites-frequence-mortels-bruts",
    slug="fig_atmp_secteurs",
    caption="Taux légal AT/MP du barème de 1999 et sinistralité observée par activité, 2021-2023",
    note_lecture=(
        "**Chaque point est une activité ; son abscisse est le taux du barème légal de 1999 "
        "après transfert du point du régime général, en % des salaires.** La première vue "
        "porte en ordonnée la fréquence des accidents **avec arrêt**, pour 1 000 travailleurs "
        "assujettis ; la seconde, les accidents **mortels pour 1 000 accidents déclarés**, "
        "et non pour 1 000 travailleurs. Les lettres renvoient aux activités listées sous "
        "les graphiques. Gris : 2021 ; orange : 2022 ; bleu : 2023. Les droites pointillées "
        "sont des ajustements linéaires sur **dix activités seulement** ; « r de Pearson » "
        "mesure l'association brute, pas un effet causal. Les décès comprennent ceux du "
        "trajet et peuvent être révisés pendant cinq ans. Le champ de la CNAM inclut "
        "des travailleurs occasionnels des chantiers publics, alors que le barème légal "
        "montré vise les employeurs affiliés à la CNSS. La fréquence 2023 utilise la "
        "ventilation des travailleurs assujettis **de 2022**. Le tableau des accidents "
        "par secteur totalise un cas de plus que le total national en 2022 ; les valeurs "
        "sont conservées. Le rapprochement des intitulés avec le décret n'est pas un tableau "
        "de passage officiel. Quinze autres rubriques sont écartées faute de taux unique, "
        "de correspondance ou de ligne de décès ; aucune cotisation moyenne n'est inventée."),
)
```
~~~~
