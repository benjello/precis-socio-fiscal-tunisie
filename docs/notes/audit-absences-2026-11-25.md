# Audit des affirmations d'absence sur les comptes nationaux (25/11/2026)

Cet audit fait suite à l'affirmation erronée sur D.63. Toutes les éditions ont désormais un inventaire de leurs tableaux : `sources/ins-comptes-nationaux/inventaire-tableaux.csv` dans le dépôt de données. Il recense 2 473 pages, dont 740 extraites, 1 167 non extraites et 566 de texte. Les affirmations d'absence de l'ouvrage et des notes portant sur les comptes nationaux y ont été cherchées par script (motifs « ne publie pas », « n'imprime pas », « ne ventile pas », « aucune ligne », « ne figure pas », « n'apparaît pas », « pas de compte »), puis relues une à une, dans les pages rendues et dans les cahiers.

| Affirmation | Où | Verdict | Ce qui a été fait |
|---|---|---|---|
| Les comptes publiés n'impriment pas de compte de redistribution en nature (D.63) | prestations_sociales/_soins, cahier de l'expert D6 | **infirmée** : tableau « Transferts sociaux en nature », 15 éditions (éd. 2021-2025, p. 114), et tableau économique d'ensemble, compte II.3 | texte corrigé avec les valeurs de 2023 ; D6 retirée et reformulée ; série `cnat-d63` extraite |
| La base 2015 n'est pas publiée par branche avant 2020 | energie/index, industrie/index | **infirmée pour les comptes de la nation** : « Répartition sectorielle de la valeur ajoutée nominale », éd. 2015-2020, p. 50-51, de 2015 à 2020 (non extrait). L'affirmation reste vraie pour la banque de données de l'INS | phrase corrigée ; extraction proposée au backlog |
| Le recalcul de la base 2015 jusqu'en 2010 ne figure dans aucune édition | annexe-pib | **confirmée** : aucune édition en base 2015 ne commence avant 2015 (inventaire) ; le recalcul vient du fichier de l'INS du 15/08/2021 | aucune modification |
| Le reste du monde ne ventile pas sa rémunération des salariés en salaires et cotisations | annexe-comptes-nation | **confirmée** : les pages « Opérations avec l'extérieur » (extraites) n'ont que D.1 | aucune modification |
| Pas de comptes de patrimoine | annexe-comptes-nation | **confirmée** : citation de l'INS, et aucun tableau d'encours non financiers dans l'inventaire | aucune modification |

**Bilan** : 5 affirmations relues ; 2 infirmées et corrigées ; 3 confirmées.

Les autres occurrences des motifs (73 en tout) ne portent pas sur les comptes nationaux. Ce sont des rapports d'entreprises publiques, des textes juridiques, des classeurs du ministère des Finances, ILOSTAT : elles sont hors du champ de cet audit et restent à relire avec leur propre inventaire de sources.

Tableaux non extraits qui lèveraient le plus de manques, par ordre de priorité :
- le tableau économique d'ensemble, 47 pages ;
- les opérations agrégées, 30 pages ;
- le revenu disponible brut des secteurs, 18 pages ;
- les revenus primaires, 15 pages ;
- la valeur ajoutée et la production par branche ;
- le tableau des entrées-sorties (TES) en base 1997, 30 pages.
