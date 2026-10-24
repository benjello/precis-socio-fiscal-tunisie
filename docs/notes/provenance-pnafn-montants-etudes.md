# Provenance de la série `pnafn-montants-etudes`

Série de la figure `fig-pnafn-allocation` (chapitre de l'assistance sociale, section de
l'allocation du programme national d'aide aux familles nécessiteuses). Fichier versionné :
`precis/_seriescache/pnafn-montants-etudes.csv` ; module de la figure :
`precis/fr/prestations_sociales/figures/assistance.py` ; contrôle : `scripts/verifier_pnafn_montants_etudes.py`
(valeur contre citation, citation contre la couche texte du PDF) et `tests/test_pnafn_montants_etudes.py`.
Lecture et contrôle du 24 octobre 2026.

Quatre familles, jamais raccordées entre elles ni à la série du chapitre. Aucune ne cite le texte
qui fixe le montant.

| Famille | Document (clé) | Page | Valeurs | Méthode du document |
|---|---|---|---|---|
| `ciblage-2021` | Banque mondiale pour le ministère des Affaires sociales, rapport technique de ciblage, 2021 (`mas-bm-ciblage-2021`) | 50 (encadré 2) | 7,7 (1987) ; 36,3 (2000) ; 56,7 (2010) ; 115 (2014) ; 150 (2014) ; 180 (février 2018) | modèle d'approximation des moyens pour classer les ménages ; l'encadré relate l'évolution du transfert, sans source ni calcul |
| `bad-cres-2013` | BAD et CRES, version provisoire du 30 mars 2013 (`bad-2013-subventions-aides-directes`) | 12 | 100 (2012) | simulation de la réaffectation du budget des subventions vers le programme sur l'enquête de l'INS de 2010 ; la page décrit le programme tel qu'il est (100 D par mois, 10 D par enfant scolarisé, 183 000 familles à l'aide médicale gratuite en 2012) |
| `unicef-2019` | ministère des Affaires sociales et UNICEF, décembre 2019 (`unicef-2019-garantie-allocation-enfants`) | 18, note 4 | 180 (janvier 2018) | étude de faisabilité d'une allocation pour enfants, par la simulation de plusieurs scénarios ; la note rapporte la décision du gouvernement |
| `presse-2018` | L'Économiste maghrébin, 15 janvier 2018 (`economiste-maghrebin-2018-01-15`) | — | 70 (« jusqu'à 2010 ») ; 150 (« en 2017 ») ; 180 (ordre du chef du gouvernement) | article de presse rapportant les propos du ministre ; aucune méthode |

Hors figure, grandeurs distinctes : les 10 D par enfant scolarisé de 2012 (BAD et CRES, p. 12) ;
le plafond de 585 D de revenu annuel moyen ajusté de la circulaire conjointe des ministères de
l'Intérieur (n° 12) et des Affaires sociales (n° 3) du 27 mai 2011, citée par la BAD et le CRES
(annexe VII, p. 76-77) ; la circulaire elle-même n'est pas obtenue (fiche
`r-pnafn-montants-historiques`).

Placement : une valeur annuelle au milieu de son année, une valeur mensuelle au milieu de son
mois, l'article de presse à son jour. Le pouvoir d'achat emploie l'indice annuel moyen des prix
à la consommation de l'année de la date citée (`ipc-longue-periode`, `bct-ipc-base2015`), en
dinars de 2025, comme la figure précédente ; aucun PIB.

Divergences de date repérées sur la figure : 150 D en 2014 (rapport de ciblage) contre le 1er janvier
2015 (série du chapitre) ; 180 D en février 2018 (rapport de ciblage) contre le 1er avril 2018
(série).
