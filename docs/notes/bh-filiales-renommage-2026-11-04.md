# BH : renommage des filiales (« Rebranding » de 2019)

Note du 4 novembre 2026. Établit les correspondances entre les noms des entités consolidées par la
Banque de l'Habitat avant le changement de dénomination (rapports annuels 2016 et 2017, qui portent
les anciens noms) et après (rapports annuels 2021, 2022 et 2023, qui portent les nouveaux noms « BH … »).
Ces correspondances alimentent `ALIAS_ENTITES` dans `precis/fr/entreprises_publiques/figures/cotees.py`,
pour que la carte d'évolution du périmètre (`ct.figure_evolution("BH", …)`) suive chaque entité d'un
exercice à l'autre au lieu de la dédoubler.

Le rapport d'activité 2019 décrit l'opération : « À travers l'action de Rebranding, la banque a donné un
coup de frais à sa marque : une nouvelle dénomination, un nouveau logo, une nouvelle signature »
(`20240507_Rapport_BH_2019_FR_VF.pdf`, rubrique communication). Dès 2019, la « Liste des entreprises
filiales » du rapport ne porte plus que les noms « BH … » ; les anciens noms ne subsistent que dans des
adresses (« Immeuble Assurances SALIM ») et une note de portefeuille (« sa filiale la SIM SICAR »). En
2020, le périmètre de consolidation ne nomme plus que « BH LEASING, BH INVEST, BH SICAF et BH IMMO »,
« BH EQUITY », « BH Recouvrement » (`20240507_Etats_Financiers_Cons31-12-2020.pdf`, note sur le périmètre).

PDF sous `tunisia-data/data/raw/entreprises-publiques/bvmt-rapports-archives/bh/` (hors git).

## Correspondances

| Clé (ancien) | Ancien nom imprimé (2016-2017) | Clé (nouveau) | Nouveau nom (2021-2023) | Preuve |
|---|---|---|---|---|
| SICAVBHPLACEMENT | SICAV BH-Placement | SICAVBHCAPITALISATION | SICAV BH-Capitalisation | **Explicite** : « SICAV BH CAPITALISATION » ex « SICAV BH PLACEMENT » (rapports de conventions 2021, 2022 et 2023, PART-3). |
| SICAVBHOBLIGATOIRE | SICAV BH-Obligatoire | SICAVBHOBLIGATAIRE | SICAV BH-Obligataire | Variante d'orthographe du même fonds (seule la terminaison change). |
| SICAFBHEPARGNEINVESTISSEMENT | SICAF BH Epargne Investissement | BHSICAF | BH SICAF | Même SICAF du groupe ; pourcentage d'intérêt continu (53,17 % en 2017, 53,18 % en 2021-2023). Rebranding 2019. |
| ASSURANCESALIM | Assurance SALIM | BHASSURANCES | BH ASSURANCES | L'assureur du groupe ; le siège de « BH Assurances » est l'« Immeuble Assurances SALIM » (liste des filiales 2019). |
| MODERNLEASING | Modern Leasing | BHLEASING | BH LEASING | Société de crédit-bail du groupe ; « Modern Leasing » disparaît du périmètre, « BH LEASING » apparaît (rebranding 2019). |
| SIMSICAR | Société SIM SICAR | BHEQUITY | BH EQUITY | SIM SICAR hors du périmètre consolidé dès 2020 ; « BH EQUITY » (capital-investissement) y figure ; intérêt 52,84 % (2017) → 53,08 % (2021-2023). |
| SOPIVEL | Société SOPIVEL | BHIMMO | BH IMMO | Promotion immobilière du groupe (site sopivelimmobilier.com) ; « BH IMMO » remplace SOPIVEL dans le périmètre de 2019-2020. |
| GENERALRECOUVREMENT | Société Général(e) Recouvrement | BHRECOUVREMENT | BH RECOUVREMENT | La « Société Générale de Recouvrement des créances » du groupe, devenue « BH Recouvrement ». |

Rapprochements laissés à la clé automatique (`_cle_entite`), sans alias : « Société BH Invest » ↔
« BH INVEST » ; « Société STIMEC » ↔ « STIMEC (BH PRINT) » ↔ « STIMEC » ; « TFB » (inchangé).

## Réserves

Deux correspondances reposent sur la continuité du périmètre et de l'activité, non sur une mention « ex »
dans les textes : **SIM SICAR → BH EQUITY** et **Modern Leasing → BH LEASING**. Elles sont cohérentes
avec le rebranding de 2019, la sortie de l'ancien nom du périmètre et un pourcentage d'intérêt continu,
mais un acte de changement de dénomination au *Journal officiel* ou au Registre national des entreprises
les confirmerait. À vérifier si le détail importe.
