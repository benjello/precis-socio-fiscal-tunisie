# Justesse des administrations publiques et des ménages (25/11/2026)

## Administrations publiques : un effet de mesure, corrigé

Avant correction, la justesse du compte consolidé S13 valait 54 à 65 % de 2015 à 2021, contre 90 à 100 % pour l'État et 82 à 86 % pour la sécurité sociale (2019-2021). Ce n'est pas un effet de consolidation : les transferts entre administrations (D.73) restent imprimés dans le compte consolidé de l'INS (2 231,1 MD en 2020) et leur poste n'en chiffre qu'une part (490,1 MD), comme pour l'État. Deux causes, chiffrées pour 2020 (édition 2020-2024) :

1. **Postes partiels au consolidé.** La consommation finale de S13 (27 380,7 MD) passait pour chiffrée parce que les soins de l'assurance maladie (2 094,3 MD) le sont, alors que la consommation de l'État ne l'est pas. Au niveau de la sécurité sociale, le même poste couvre 99 % de l'opération (2 112,2 MD).
2. **Rattachement des cotisations.** Le poste des cotisations à la CNRPS désigne l'État parmi les payeurs ; la règle « un poste n'est rattaché au secteur qu'une fois » le rangeait en emplois de S13 et non en ressources : 3 430,0 MD de postes en ressources contre 8 675,5 au niveau de la sécurité sociale.

Correction : S13 est désormais la somme des trois sous-secteurs (non consolidée), et un poste versé et reçu dans le même secteur y figure des deux côtés. Justesse 2020 : 94,5 % (au lieu de 64,6 % au consolidé) ; part couverte : 42,6 % (au lieu de 62,2 %). Le compte consolidé reste dans `compte-couverture-annees.csv` (`S13-consolide`).

## Ménages : un effet de composition, et une ventilation de l'IRPP

L'IRPP encaissé par l'État dépasse chaque année les impôts courants (D.5) que l'INS inscrit en emplois des ménages :

| Année | IRPP | dont impôts sur les salaires | dont autres | D.5 des ménages | IRPP / D.5 | D.5 des SNF, SF et RDM − IS | 
|---|--:|--:|--:|--:|--:|--:|
| 2015 | 5 088 | 3 557 | 1 532 | 3 957 | 129 % | 1 331 |
| 2016 | 5 943 | 4 106 | 1 836 | 3 558 | 167 % | 2 412 |
| 2017 | 6 205 | 4 029 | 2 176 | 3 738 | 166 % | 2 548 |
| 2018 | 6 359 | 3 831 | 2 528 | 4 106 | 155 % | 3 119 |
| 2019 | 8 813 | 5 488 | 3 325 | 5 142 | 171 % | 2 502 |
| 2020 | 8 945 | 5 813 | 3 133 | 5 306 | 169 % | 3 197 |
| 2021 | 9 485 | 6 419 | 3 066 | 5 234 | 181 % | 3 650 |
| 2022 | 10 075 | 7 057 | 3 018 | 5 240 | 192 % | 4 059 |
| 2023 | 11 374 | 7 906 | 3 468 | 6 648 | 171 % | 5 460 |

Sources : ministère des Finances, série des recettes fiscales (`recettes_fiscales.xls`, lignes « Impôts sur le Revenu », « Impots sur les Salaires », « Autres », « Impôts sur les Sociétés ») ; INS, comptes des secteurs, édition la plus récente où l'année est définitive. Millions de dinars.

- **Pas de rupture en 2021.** Le rapport IRPP / D.5 est au-dessus de 100 % dès 2015. Le passage de 106 % (2020) à 181 % (2021) est un effet de composition : jusqu'en 2020, la justesse des ménages réunit l'IRPP et les pensions (CNSS et CNRPS, 9 862,9 MD contre 12 393,3) ; dès 2021 les pensions n'ont plus de montant et l'IRPP reste seul.
- **Les impôts sur les salaires** sont proches du D.5 des ménages (90 à 135 % selon l'année). L'IRPP « autres » (revenus non salariaux, retenues à la source) est du même ordre que l'écart entre le D.5 des sociétés et du reste du monde et l'impôt sur les sociétés (de 2015 à 2020 surtout). Ces chiffres sont compatibles avec un rangement par l'INS d'une partie de l'IRPP hors des ménages ; ils ne l'établissent pas : question A15 du cahier de l'expert.
- **Saut de 2019** : les impôts sur les salaires passent de 3 831 à 5 488 MD (+43 %) dans la série du ministère ; le D.5 des ménages croît aussi (+25 %). La série du ministère ne signale pas de rupture : à vérifier (question A15).

Aucune correction de la mesure : le poste IRPP reste rattaché aux ménages, et la justesse le montre.

**25/11/2026, soir.** Depuis 9fcc6c54, le D.1 reçu par les ménages, chiffré par la seule masse salariale de l'État, était entré dans la justesse (38 à 58 %). Règle nouvelle (PR #916) : une opération n'entre dans la justesse que si les postes couvrent tous les secteurs que l'INS inscrit, avec un montant non nul, à l'autre bout de l'opération.
Appliquée strictement, la règle ne laissait aucune opération des ménages dans la justesse : en 2019, le D.5 en sortait pour 110,1 MD d'impôts courants reçus par les collectivités locales, qu'aucun poste ne chiffre.
Ajustement retenu : le secteur n'est jamais sa propre contrepartie, et une opération entre dans la justesse si ses contreparties non couvertes pèsent au plus 5 % de son montant (`SEUIL_CONTREPARTIE`, convention de l'ouvrage, sans source normative). Le D.5 des ménages y entre (1,2 à 2,1 % non couverts de 2015 à 2023 ; justesse de 128,6 % en 2015 à 171,4 % en 2019). Le D.1 n'y entre pas (48 à 54 % non couverts).
