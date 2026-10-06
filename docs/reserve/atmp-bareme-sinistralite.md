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

### La classification des employeurs par activité (retour de lecture du 6 octobre 2026)

Avis d'une relectrice qui a travaillé à l'évaluation du régime : ne pas retenir le graphique dans
sa forme actuelle, et ne pas le présenter comme un moyen de comparer directement les taux et la
sinistralité par activité. L'argument a une **source publiée**, citable : La Lettre du CRES n° 8,
janvier 2023, « Régime de réparation des accidents du travail et des maladies professionnelles :
quel bilan et quelles perspectives ? » (clé `belloussaief2023-atmp`, p. 6).

- **Qui classe.** C'est la CNSS qui classe l'entreprise à son affiliation : elle lui attribue un
  code d'activité économique, auquel correspond un « code ATMP » qui détermine son taux. La CNAM,
  qui gère le régime et publie les statistiques d'accidents, ne fait pas ce classement.
- **Selon quelle nomenclature.** Une nomenclature de 1961 (NAT 1961), qui « ne tient pas compte des
  évolutions du tissu économique tunisien ». La Lettre recommande de réviser les codes pour
  s'aligner sur la nomenclature de 2009 (NAT 2009).
- **Des erreurs de classement dans les deux sens.** Des entreprises sont classées dans une activité
  au taux inférieur à celui de leur activité réelle, d'autres dans une activité au taux supérieur.
- **Aucun contrôle systématique.** Les systèmes de gestion des deux caisses ne communiquent pas : la
  CNAM n'est pas informée des affiliations nouvelles ni des changements de taux. L'écart entre le
  taux appliqué et l'activité réelle n'apparaît qu'à l'occasion d'une enquête après un sinistre ou
  d'une visite. Un accord d'échange de données entre les deux caisses date de 2011 ; la Lettre
  écrit que la CNAM n'a reçu aucune liste depuis sa signature.

Conséquence pour l'exercice : l'activité sous laquelle un accident est compté, et celle dont
l'employeur paie le taux, peuvent ne correspondre ni l'une ni l'autre à l'activité réelle. Les deux
axes du graphique sont donc affectés, et pas de la même façon : un nuage de points par activité ne
mesure pas la cohérence du barème avec le risque.

Ce que le retour de lecture ajoute à la publication, et qui n'a pas de source publiée ici : un
chantier de fiabilisation est en cours, par rapprochement avec les données de l'INS et le tableau
de correspondance NAT61–NAT2009. L'analyse gagnerait à être refaite après ce chantier.

### Les limites des statistiques elles-mêmes

La même Lettre (p. 5) relève que les statistiques d'accidents fournies par la CNAM « souffrent de
beaucoup de limites telles que la sous déclaration, la sous reconnaissance des maladies
professionnelles et la couverture limitée de certains secteurs excluant notamment la fonction
publique et les indépendants ». La sous-déclaration n'a aucune raison d'être égale d'une activité à
l'autre : elle biaise la comparaison entre activités, pas seulement les niveaux.

### Ce que la Lettre publie par activité, sans le rapprocher du barème

Elle donne l'indice de fréquence des accidents avec arrêt, de 2012 à 2020, pour les cinq secteurs
les plus exposés (fonderie et sidérurgie, matériaux de construction, caoutchouc, construction et
réparation navale, bois et liège ; tableau 2, p. 4), rapporté à la moyenne de tous les secteurs.
Elle ne confronte pas ces fréquences aux taux de cotisation. C'est la forme la plus prudente de
l'exercice, et le point de départ d'une reprise : une série de neuf ans, établie par l'institution
qui a accès aux données.

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

1. Des statistiques de sinistralité établies sur une classification **fiabilisée** des employeurs
   (NAT 2009), ou à défaut une mesure publiée de l'ampleur des erreurs de classement.
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
