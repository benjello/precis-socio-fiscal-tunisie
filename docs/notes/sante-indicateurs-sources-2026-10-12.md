# Santé — résultats, protection financière et sources récurrentes

## Indicateurs OMS relevés le 12 octobre 2026

**Couverture des services essentiels**, indicateur `UHC_INDEX_REPORTED` (ODD
3.8.1), Tunisie 2000-2023. URL :
<https://ghoapi.azureedge.net/api/UHC_INDEX_REPORTED?$filter=SpatialDim%20eq%20'TUN'&$select=TimeDim,Value&$orderby=TimeDim>.
La [fiche de méthode OMS](https://www.who.int/data/gho/data/themes/topics/service-coverage)
définit un **indice de 0 à 100**, moyenne géométrique pondérée de **14 traceurs**
des services essentiels : santé reproductive et materno-infantile, maladies
infectieuses, maladies non transmissibles, capacité de service et accès. Les
traceurs ne sont pas une liste exhaustive de soins et l'indice n'est ni un taux
de population couverte par la CNAM ni une mesure directe de qualité clinique.

| Année | Indice | Année | Indice | Année | Indice |
|---|---:|---|---:|---|---:|
| 2000 | 61 | 2008 | 67 | 2016 | 73 |
| 2001 | 61 | 2009 | 68 | 2017 | 74 |
| 2002 | 62 | 2010 | 69 | 2018 | 75 |
| 2003 | 63 | 2011 | 69 | 2019 | 75 |
| 2004 | 66 | 2012 | 70 | 2020 | 76 |
| 2005 | 66 | 2013 | 70 | 2021 | 75 |
| 2006 | 67 | 2014 | 72 | 2022 | 76 |
| 2007 | 67 | 2015 | 73 | 2023 | 76 |

Sous-indices 2000 → 2023 relevés séparément dans l'API : santé reproductive,
materno-infantile 59 → 81 (`UHC_SCI_RMNCH`), infectieux 78 → 98
(`UHC_SCI_INFECT`), maladies non transmissibles 45 → 57 (`UHC_SCI_NCD`),
capacité et accès 65 → 73 (`UHC_SCI_CAPACITY`). Ils donnent le contexte de
l'indice, pas une attribution causale aux réformes tunisiennes.

**Difficulté financière liée aux soins**, indicateur
`FINANCIALHARDSHIP_PROPORTIONOFPOP`, Tunisie, observation nationale
`Dim1=RESIDENCEAREATYPE_TOTL` :
<https://ghoapi.azureedge.net/api/FINANCIALHARDSHIP_PROPORTIONOFPOP?$filter=SpatialDim%20eq%20'TUN'%20and%20Dim1%20eq%20'RESIDENCEAREATYPE_TOTL'&$select=TimeDim,Value,Dim1&$orderby=TimeDim>.
La [fiche OMS](https://www.who.int/data/gho/data/themes/topics/financial-protection)
explicite la **définition révisée en 2025 de l'ODD 3.8.2** : part de la
population vivant dans un ménage dont la dépense de santé directe, positive,
excède **40 % du budget discrétionnaire**. Les données sont fondées sur des
enquêtes, disponibles seulement aux six dates suivantes ; le seuil porte sur
le budget du ménage **après besoins essentiels**, non sur sa dépense totale.

| Année d'enquête | Population concernée (%) | Source de données indiquée par l'API |
|---|---:|---|
| 1995 | 25,04 | DATASOURCE_FPTUN1995 |
| 2000 | 25,08 | DATASOURCE_FPTUN2000 |
| 2005 | 26,95 | DATASOURCE_FPTUN2005 |
| 2010 | 24,46 | DATASOURCE_FPTUN2010 |
| 2015 | 21,16 | DATASOURCE_FPTUN2015 |
| 2021 | 31,18 | DATASOURCE_FPTUN2021 |

L'ancienne série `FINPROTECTION_CATA_TOT_10_POP` mesure un autre seuil,
10 % de la dépense totale ; elle est archivée et **ne se raccorde pas** à la
définition de 2025. Aucun chiffre annuel ne se déduit entre les enquêtes. Une
révision de méthode sur les données anciennes reste possible : dater la
consultation à chaque reprise de la série.

## Documents récurrents pour le livre

| Famille et producteur | Séries utilisables | Période du corpus consulté | Portée et vigilance |
|---|---|---|---|
| *Annuaire statistique de la Tunisie*, INS (source ministère des Finances pour le budget, ministère de la Santé pour l'offre) | tableaux budgétaires, structures de soins, médecins par gouvernorat, autres statistiques sanitaires | éditions cataloguées 1995-2001 à 2019-2023 | les tableaux d'offre de la dernière édition donnent **2023**, ceux du budget 2021-2023 ; les éditions glissantes permettent une histoire, en vérifiant les définitions |
| *Indicateurs globaux d'activité*, *Prestations sanitaires* et états financiers, CNAM | affiliés par filière, praticiens conventionnés, facturation hospitalière et deux postes des cliniques privées, charges et flux de trésorerie | filières 2008-2021 ; médecins et prestations sanitaires 2007-2021 ; états financiers 2016-2021 lisibles en texte (2011-2015 océrisés, non validés) | statistiques d'activité distinctes des comptes ; changement de définition des affiliés en 2019 et des factures en 2017 ; postes de soins non exhaustifs |
| Rapports et documents de la mission Santé, ministère des Finances | crédits par programme, fonctionnement et investissement, PAP/RAP | budgets ministériels récupérés de 2013 à 2018 ; annexes PLF sur les caisses jusqu'aux éditions suivantes | distinguer prévision, montant constaté et exécution ; aucune somme du ministère n'est à additionner sans contrôle aux charges CNAM |
| Rapports de clôture et contrôles particuliers, Cour des comptes | exécution budgétaire et constats sur CNAM, hôpitaux, équipements, prévention et cliniques | clôtures 2018-2024 ; rapports particuliers 2006-2021 présents dans le catalogue | constats de contrôle datés, **pas** série statistique nationale ; réponses de l'organisme contrôlé à distinguer |
| *Global Health Expenditure Database* et observatoire mondial, OMS | dépense courante, financeurs, paiements directs et indices de couverture/protection financière | comptes de santé 2000-2023 ; couverture 2000-2023 ; enquêtes de difficulté financière 1995-2021 | périmètre des administrations plus large que le budget ministériel ; dépense courante hors capital ; indicateurs et méthodes propres à chaque série |
| Enquêtes quinquennales de consommation des ménages, INS | dépenses médicales détaillées, niveau de vie et répartition | 2015 et 2021 lus en couche texte pour les rubriques de santé | traitement des remboursements à établir avant de les qualifier de reste à charge net |

Inventaires détaillés dans `tunisia-data/sources/ins-annuaires-statistiques.md`,
`cnam-statistiques.md`, `minfinances-portail-ancien.md`,
`cour-des-comptes.md` et la présente note ; chacun donne le fichier local,
le lieu de publication et les limites de lecture. **Échelle historique** :
le droit est suivi depuis la prévoyance de 1951, les assurances sociales de
1960, l'organisation sanitaire de 1991 et l'assurance maladie de 2004-2007 ;
les séries de résultat ci-dessus commencent en 1995 ou en 2000 et ne mesurent
pas rétrospectivement ces premiers régimes.
