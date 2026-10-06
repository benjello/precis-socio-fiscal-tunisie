# Note documentaire — la structure des prix des carburants, relue à l'image (2014-2026)

Passe du 6 octobre 2026. Famille de TOUTES les valeurs de cette note : **source officielle tunisienne** (ministère chargé de l'énergie, Observatoire national de l'énergie [et des mines], *Conjoncture énergétique* mensuelle). Niveau de preuve : **image lue** (page du tableau rendue à 140 points par pouce, recadrée, lue ligne à ligne), sauf mention. Rien de versionné n'a été modifié.

Fichiers (hors dépôt) :
- `scratchpad/one_structure_prix_2015_2026_relu.csv` — 468 lignes, 78 numéros × 6 produits, colonnes `relu_image` (oui partout), `ecart_somme_public`, `ecart_somme_nominal`, `ecart_import_moins_cession_CALCUL`, `correction` ;
- `scratchpad/relu/one/image_lu.txt` — la saisie brute de la lecture, numéro par numéro ; `relu/one/compare.py` — la confrontation au relevé automatique ; `relu/one/st_grp_*.png`, `st_grq_*.png` — les 26 planches lues (trois tableaux par planche) ;
- `scratchpad/one_conjoncture_2020_2025_manifeste.tsv` — 29 numéros nouveaux récupérés aujourd'hui (adresse, origine, SHA-256), fichiers dans `scratchpad/relu/one/dl/` — **à verser** dans `tunisia-data/data/raw/` avec leur ligne de catalogue (non fait : le catalogue `sources/*.csv` est versionné).

## 1. Ce que le tableau contient et comment il se lit

Tableau « PRODUITS PETROLIERS », rubrique « Produits pétroliers » (puis « Prix des produits pétroliers ») de l'annexe « prix » de chaque numéro. Six lignes, toujours les mêmes :

| Ligne (libellé de la source) | Unité |
|---|---|
| Essence SSP (sans plomb) | millimes par litre |
| Gasoil ordinaire (« ordianiare » jusqu'en 2017) | millimes par litre |
| Gasoil 50PPM, puis « Gasoil S.S. » (sans soufre) à partir du numéro de septembre 2017 | millimes par litre |
| Fuel oil lourd (N° 2) HTS | dinars par tonne |
| GPL, puis « GPL domestique » | millimes par kilogramme |
| GPL (Bouteille 13 kg) | dinars par bouteille |

Colonnes, selon la période :

| Numéros | Colonnes |
|---|---|
| septembre 2015 à janvier 2020 | Prix import (1) · Pcession (2) · Prix de vente (3) |
| février 2020, [mars], mai, juin, juillet 2020 | Prix import · Droits et taxes · Divers et marges · Prix de vente nominal · Prix de vente — **sans** prix de cession |
| avril et août 2020 | les six : Prix import · Pcession · Droits et taxes · Divers et marges · Prix de vente nominal · Prix de vente |
| septembre 2020 à juillet 2026 (sauf octobre 2020, sans cession) | Prix import · Pcession · Droits et taxes · Divers et marges · Prix de vente — le « nominal » disparaît |

Notes de bas de tableau, citées telles quelles (image) :
- (1) « Prix moyen pondéré » ;
- (2) [2015-2019] « Prix à la sortie de raffinerie Bizerte par voie terrestre en vigueur de JJ/MM/AAAA » — la **date de la structure** ;
- (3) [2015-2019] « Prix de vente en vigueur aux publics du JJ/MM/AAAA » ; à partir de 2020 : « Prix de vente en vigueur au[x] public[s] à partir du JJ/MM/AAAA » ;
- « Droits et Taxes : droits de consommation (DC) + RPD (3 % du DC) + TVA (13-19 % du prix de vente par les sociétés HTVA) » ;
- « Divers et Marges : frais de mise en place + marge sociétés + forfait de transport uniforme + stockage de sécurité + marge des revendeurs » ;
- « prix de vente nominale : Prix de vente simulé hors subvention » (février 2020), puis « simulé sur la base du prix d'importation » (avril à août 2020).

**Ce que mesure le prix d'importation.** Ce n'est PAS le prix du mois : c'est la moyenne, pondérée par les quantités, depuis le début de l'année. L'Observatoire l'écrit deux fois : « Les prix d'importation des produits pétroliers du tableaux 4 sont des moyennes pondérées par la quantité sur la période des 9 mois » (numéro de septembre 2022, encadré « Éclaircissements concernant les coûts à l'importation… », p. 15 du fichier, couche texte) ; « Les prix d'exportation et d'importation de pétrole brut et des produits pétroliers des tableaux 3 et 4 sont des moyennes pondérées par la quantité sur la période de l'exercice. Les quantités importées/exportées étant variables d'un mois à un autre selon les besoins du marché national ce qui peut impacter la moyenne » (juillet 2026, p. 16, couche texte). L'en-tête le confirme : « A fin <mois> », et « 2017 », « Année 2021 », « Année 2022 » pour les numéros de décembre. Conséquences : (i) le numéro de décembre donne la moyenne annuelle ; (ii) la série saute chaque mois de janvier (essence : 768 à fin décembre 2016, 1 001 en janvier 2017) ; (iii) un tiret remplace le prix d'importation du fuel lourd dans les numéros de janvier à mars 2019 et de janvier 2020, **sans explication de la source** (la note « Pas d'importation courant… » qui figure au-dessus du tableau appartient au tableau du pétrole brut, non à celui-ci).

**Niveau de preuve de cette lecture.** L'Observatoire n'écrit en toutes lettres que le prix est une moyenne cumulée que dans les numéros de septembre à décembre 2022 et dans celui de juillet 2026. Pour 2015-2021, c'est une **inférence** de la note documentaire, fondée sur trois indices lus : la mention « (1) Prix moyen pondéré », l'en-tête « A fin <mois> » ou « Année », et les sauts de janvier. À écrire comme tel si la série 2015-2021 est publiée.

**Les identités comptables** (vérifiées sur le numéro d'avril 2020, le seul avec août 2020 à porter les six colonnes) :
- prix de vente au public = prix de cession + droits et taxes + divers et marges — essence : 1 101 + 738 + 196 = 2 035 ;
- prix de vente nominal = prix d'importation + droits et taxes + divers et marges — essence : 994 + 738 + 196 = 1 928 ;
- donc nominal − public = importation − cession, **par construction** : ce n'est pas un contrôle indépendant.

**L'écart « importation − cession »** (colonne `ecart_import_moins_cession_CALCUL`, CALCUL de la note, non lu) : positif, le produit importé coûte plus que le prix auquel il est cédé aux distributeurs — c'est une perte unitaire avant taxes pour l'importateur (STIR) ; négatif, un gain. L'Observatoire trace lui-même cette grandeur dans le graphique « Prix de ventes et résultats unitaires (*) », avec la réserve : « (*) calcul à titre indicatif basé sur le différentiel entre le prix moyen pondéré d'importation et le prix de cession » (avril 2020, p. 15, image). Trois réserves à écrire avec toute publication : c'est un écart sur une moyenne cumulée depuis janvier, non sur le mois ; il ignore la production de la raffinerie ; l'Observatoire le dit « indicatif » — et, pour le gaz et l'électricité, précise que le résultat unitaire « n'est pas forcément identique à la subvention budgétaire » (juillet 2026, p. 16).

## 2. Ce qui a été relu, et le taux d'erreur du relevé automatique

- **78 numéros lus à l'image, 468 lignes** : les 48 du relevé automatique (septembre 2015 à décembre 2021), le numéro de juillet 2026, et 29 numéros nouveaux (mars, juin à novembre 2020 ; mars, mai, novembre 2021 ; janvier à décembre 2022 ; avril, août, décembre 2023 ; juin, novembre 2024 ; juillet, décembre 2025). C'est une relecture intégrale du relevé, non un échantillon.
- **Relevé automatique : 1 ligne fausse sur 288** (fuel lourd, février 2020 : décalage d'une colonne — « cession 111, droits 35, marges 1 017 » au lieu de « cession absente, droits 111, marges 35, nominal 1 017 »), soit **4 valeurs sur 1 023 comparées (0,4 %)**. Toutes les autres valeurs, et toutes les dates, sont identiques à l'image. S'y ajoutent 6 lignes en double (décembre 2018 : deux fichiers, « finale » et non, mêmes valeurs) : 288 lignes distinctes, non 294. La réserve de la note n° 3 sur la bouteille de septembre-décembre 2017 est levée : les valeurs sont justes.
- **Sept numéros « non lus »** (mars, avril, mai, novembre, décembre 2015 ; janvier, mars 2016) : **le tableau n'y figure pas.** Deux voies : (a) aucune page ne contient « SSP », « Millimes », « cession » ni « Pcession » (couche texte, page par page) ; (b) planches-contact des pages (novembre 2015 en entier ; six dernières pages de mai et décembre 2015, janvier et mars 2016) : le numéro s'achève sur « Les échanges commerciaux » puis « Abréviations », sans annexe de prix. Pour mars et avril 2015, seule la voie (a) et l'identité de maquette avec mai 2015. Le tableau apparaît dans le numéro de septembre 2015 et, de façon continue, à partir d'avril 2016.
- **Lacunes du corpus** (numéros ni au dépôt ni récupérés) : juin à août 2015, octobre 2015, février, mai, juin, juillet 2016, juin à août 2017, janvier à juin 2018 ; 2023 à 2026 n'ont été lus que par sondage (8 numéros), ce qui suffit puisque la structure du 24 novembre 2022 n'a pas changé.

## 3. Cohérence interne (somme des composantes)

`ecart_somme_public` = prix public − (cession + droits et taxes + divers et marges) ; `ecart_somme_nominal` = nominal − (importation + droits et taxes + divers et marges). Calculables sur les numéros de 2020 à 2026 seulement.

- Écart nul ou d'un millime (arrondi) partout — l'essence porte un écart constant de +1 millime du 20 avril 2021 au 24 novembre 2022 (1 149 + 747 + 198 = 2 094 pour 2 095 ; 1 498 + 815 + 211 = 2 524 pour 2 525), le GPL de −1 (214 + 75 + 304 = 593 pour 592) — **sauf quatre cas, qui sont dans la source** :
  1. **février 2021** : essence +11, gasoil +7, gasoil sans soufre +8 — le prix public (1 955 / 1 500 / 1 685, au 6 février 2021) et le prix de cession (1 033 / 1 050 / 1 032) ont été mis à jour, mais les colonnes « droits et taxes » et « divers et marges » sont restées celles de la structure précédente (719 / 192, etc.). **Ne pas publier les droits et marges de la structure du 6 février 2021** ;
  2. **février 2020, fuel lourd** : nominal 1 017 pour 804 + 111 + 35 = 950 (écart 67) ;
  3. **juin 2020, essence** : nominal 1 856 pour 961 + 729 + 192 = 1 882 (écart −26) ;
  4. **bouteille de 13 kg, mai à août 2020** : nominal arrondi au dinar (« 20 »).
- Le numéro de **mars 2020** (fichier « Conjoncture_énergétique_Mars_2020.pdf ») porte un tableau intitulé « A fin avril 2020 », identique à celui d'avril sans la colonne cession, au-dessus d'un graphique « Structure des prix à fin mars 2020 » : fichier remanié ; la ligne est marquée, à ne pas employer.
- **Deux dates divergentes pour la même structure** : « 10/11/2020 » (numéros de novembre et décembre 2020) et « 09/11/2020 » (janvier 2021), mêmes prix (1 915 / 1 470 / 1 650).
- Le numéro de septembre 2020 date le prix public du « 08/09/2020 » avec des prix identiques à ceux du 8 juillet (1 915 / 1 470 / 1 700) : ajustement de septembre sans changement, ou date erronée — non tranché.
- Le numéro de décembre 2017 date la structure du « 31/12/2017 » (1 800 / 1 280 / 1 560 ; fuel 560 ; bouteille 7,7) : c'est l'ajustement dit du 1er janvier 2018 ailleurs dans le volume.
- Le numéro de mars 2019 (« Fin mars-19 ») porte encore la structure du 2 septembre 2018 ; celle du 31 mars 2019 apparaît au numéro d'avril.

## 4. Tableau de synthèse publiable — les structures datées, 2014-2022

Prix fixés par l'administration à chaque date de structure (ils ne bougent pas entre deux dates ; seul le prix d'importation change d'un numéro à l'autre). **Le tableau n'est exhaustif qu'à partir de février 2020.** Avant, il ne porte que les structures présentes dans les numéros lus, et quatre fenêtres sans numéro peuvent cacher une structure intermédiaire : octobre 2015 – mars 2016 (une seule connue : 6 janvier 2016), mai – juillet 2016, juin – août 2017, **janvier – juin 2018**. Confrontation au tableau des ajustements datés du volume (`_carburants.qmd`, tableau 2002-2018) : toutes ses dates de juillet 2014 à septembre 2018 se retrouvent ici, **sauf le 1er avril 2018** (1 850 / 1 330, source de presse dans le volume), qui tombe dans la quatrième fenêtre — ligne ajoutée ci-dessous, sans prix de cession. Les numéros de janvier à juin 2018 ne sont pas archivés (index d'Internet Archive interrogé le 6 octobre 2026 sur `data.industrie.gov.tn/wp-content/uploads/` et `energiemines.gov.tn/fileadmin/`, filtre « onjoncture…2018 » : huit adresses, de juillet à décembre 2018, plus « janvier-2018 » en erreur 403). Millimes par litre ; fuel lourd en dinars par tonne ; bouteille de 13 kg en dinars. Lecture d'une cellule : cession / droits et taxes / divers et marges → prix public. « — » : la source ne le donne pas.

| Date d'effet (source) | Essence sans plomb | Gasoil ordinaire | Gasoil 50 ppm / sans soufre | Fuel lourd n° 2 | Bouteille 13 kg | Premier numéro qui la porte |
|---|---|---|---|---|---|---|
| 01/07/2014 | 1 065 → 1 670 | 942 → 1 250 | 1 164 → 1 500 | 403 → 510 | 3,222 → 7,400 | sept. 2015 |
| 06/01/2016 | 822 → 1 650 | 828 → 1 200 | 870 → 1 450 | 401 → 510 | 3,032 → 7,4 | avril 2016 |
| 16/07/2016 | 822 → 1 650 | 774 → 1 140 | 843 → 1 420 | 401 → 510 | 3,032 → 7,4 | août 2016 |
| 25/11/2016 | 817 → 1 650 | 769 → 1 140 | 838 → 1 420 | 400 → 510 | 2,913 → 7,4 | déc. 2016 |
| 02/07/2017 | 855 → 1 750 | 805 → 1 230 | 870 → 1 510 | 400 → 510 | 2,913 → 7,4 | sept. 2017 |
| 31/12/2017 | 934 → 1 800 | 884 → 1 280 | 953 → 1 560 | 444 → 560 | 3,060 → 7,7 | déc. 2017 |
| [01/04/2018 — absente des numéros lus ; prix publics d'après le volume, source de presse] | — → 1 850 | — → 1 330 | — | — | — | aucun numéro de janvier à juin 2018 |
| 23/06/2018 | 1 027 → 1 925 | 984 → 1 405 | 1 051 → 1 685 | 520 → 650 | 3,001 → 7,7 | juil. 2018 |
| 02/09/2018 | 1 077 → 1 985 | 1 051 → 1 480 | 1 104 → 1 745 | 573 → 710 | 3,001 → 7,7 | sept. 2018 |
| 31/03/2019 | 1 138 → 2 065 | 1 124 → 1 570 | 1 169 → 1 825 | 634 → 780 | 2,882 → 7,7 | avril 2019 |
| 31/03/2019 (décomposée en fév. 2020) | — / 744 / 183 → 2 065 | — / 298 / 148 → 1 570 | — / 508 / 149 → 1 825 | — / 111 / 35 → 780 | — / 0,977 / 3,842 → 7,7 | fév. 2020 |
| 07/04/2020 | 1 101 / 738 / 196 → 2 035 | 1 095 / 295 / 160 → 1 550 | 1 135 / 504 / 161 → 1 800 | 634 / 111 / 35 → 780 | 2,782 / 0,970 / 3,948 → 7,7 | avril 2020 |
| 08/05/2020 | — / 733 / 192 → 2 005 | — / 293 / 157 → 1 530 | — / 501 / 158 → 1 775 | — / 111 / 35 → 780 | inchangée | mai 2020 |
| 09/06/2020 | — / 729 / 192 → 1 975 | — / 291 / 157 → 1 510 | — / 498 / 158 → 1 750 | inchangé | inchangée | juin 2020 |
| 08/07/2020 | 1 004 / 719 / 192 → 1 915 (colonnes de juillet : — / 724 / 192 → 1 945) | 1 027 / 286 / 157 → 1 470 (juillet : — / 288 / 157 → 1 490) | 1 049 / 493 / 158 → 1 700 (juillet : — / 495 / 158 → 1 725) | 637 / 111 / 32 → 780 | inchangée | juil. et août 2020 — **voir réserve** |
| 09/10/2020 | inchangée | inchangé | — / 490 / 158 → 1 675 | inchangé | inchangée | oct. 2020 |
| 10/11/2020 (09/11 selon janv. 2021) | 1 004 / 719 / 192 → 1 915 | 1 027 / 286 / 157 → 1 470 | 1 005 / 487 / 158 → 1 650 | 637 / 111 / 32 → 780 | 2,782 / 0,970 / 3,948 → 7,7 | nov. 2020 |
| 06/02/2021 | 1 033 / [n.p.] → 1 955 | 1 050 / [n.p.] → 1 500 | 1 032 / [n.p.] → 1 685 | inchangé | inchangée | fév. 2021 |
| 11/03/2021 | 1 067 / 731 / 197 → 1 995 | 1 076 / 293 / 162 → 1 530 | 1 063 / 495 / 162 → 1 720 | inchangé | inchangée | mars 2021 |
| 20/04/2021 | 1 149 / 747 / 198 → 2 095 | 1 141 / 301 / 163 → 1 605 | 1 137 / 504 / 164 → 1 805 | inchangé | inchangée | avril 2021 |
| 01/02/2022 | 1 198 / 757 / 200 → 2 155 | 1 183 / 307 / 165 → 1 655 | 1 184 / 511 / 165 → 1 860 | inchangé | inchangée | fév. 2022 |
| 01/03/2022 | 1 251 / 767 / 201 → 2 220 | 1 226 / 313 / 166 → 1 705 | 1 231 / 517 / 167 → 1 915 | inchangé | inchangée | mars 2022 |
| 14/04/2022 | 1 343 / 785 / 202 → 2 330 | 1 300 / 323 / 167 → 1 790 | 1 314 / 528 / 168 → 2 010 | 846 / 140 / 44 → 1 030 | inchangée | avril 2022 |
| 18/09/2022 | 1 398 / 796 / 206 → 2 400 | 1 358 / 330 / 171 → 1 860 | 1 372 / 536 / 172 → 2 080 | inchangé | 3,43 / 1,11 / 4,27 → 8,80 | sept. 2022 |
| 24/11/2022 (en vigueur à fin juillet 2026) | 1 498 / 815 / 211 → 2 525 | 1 464 / 345 / 176 → 1 985 | 1 478 / 550 / 177 → 2 205 | 846 / 140 / 44 → 1 030 | 3,43 / 1,11 / 4,27 → 8,80 | nov. 2022 ; juil. 2026 |

[n.p.] = non publiable (colonnes non mises à jour, § 3). GPL en vrac (millimes/kg) : cession 247,811 → 569,23 (2014) ; 233 → 569 (2016) ; 224 → 569 (25/11/2016) ; 235 → 592 (31/12/2017) ; 231 → 592 (2018) ; 222 → 592 (31/03/2019) ; 214 / 75 / 304 → 592 (07/04/2020 au 14/04/2022) ; 264 / 85 / 328 → 677 (depuis le 18/09/2022).

**Réserve sur juillet 2020.** Le numéro de juillet 2020 date du « 08/07/2020 » les prix 1 945 / 1 490 / 1 725 ; celui d'août 2020 date du même « 08/07/2020 » les prix 1 915 / 1 470 / 1 700. L'un des deux numéros porte une date périmée : la baisse suivante (août 2020) n'est pas datée par la source. À écrire comme tel — « deux structures successives, toutes deux datées du 8 juillet 2020 par la source » — ou à recouper avec les communiqués du ministère.

**Lecture économique que la série autorise** (constats, sans plus) : de 2014 à 2019 les ajustements sont espacés (dix structures connues en cinq ans : les neuf lues ici et celle du 1er avril 2018 ; nombre plancher, vu les fenêtres sans numéro) ; d'avril à novembre 2020 l'ajustement mensuel joue à la baisse (essence : 2 065 → 1 915) ; il rejoue à la hausse en février, mars et avril 2021, s'arrête, reprend cinq fois en 2022 ; depuis le 24 novembre 2022 rien ne bouge. Part des droits et taxes dans le prix public au 24 novembre 2022 : essence 815 / 2 525 = 32 % ; gasoil 345 / 1 985 = 17 % ; gasoil sans soufre 550 / 2 205 = 25 % (ces trois pourcentages sont imprimés par l'Observatoire dans son graphique « Décomposition du prix des carburants », juillet 2026, couche texte).

## 5. Le prix d'importation et l'écart avec le prix de cession — moyennes annuelles (numéros de décembre)

Moyenne pondérée de l'année (numéro de décembre ; image). Écart = importation − cession en vigueur en fin d'année : CALCUL de la note.

| Année | Essence : import / cession / écart | Gasoil ordinaire | Gasoil sans soufre | Bouteille 13 kg (D) |
|---|---|---|---|---|
| 2016 | 768 / 817 / −49 | 716 / 769 / −53 | 763 / 838 / −75 | 11,559 / 2,913 / +8,646 |
| 2017 | 1 048 / 934 / +114 | 1 023 / 884 / +139 | 1 045 / 953 / +92 | 15,899 / 3,060 / +12,839 |
| 2018 | 1 381 / 1 077 / +304 | 1 414 / 1 051 / +363 | 1 464 / 1 104 / +360 | 18,027 / 3,001 / +15,026 |
| 2019 | 1 416 / 1 138 / +278 | 1 484 / 1 124 / +360 | 1 522 / 1 169 / +353 | 17,871 / 2,882 / +14,989 |
| 2020 | 916 / 1 004 / −88 | 963 / 1 027 / −64 | 939 / 1 005 / −66 | 15,46 / 2,782 / +12,68 |
| 2021 | 1 510 / 1 149 / +361 | 1 366 / 1 141 / +225 | 1 457 / 1 137 / +320 | 24,58 / 2,782 / +21,80 |
| 2022 | 2 570 / 1 498 / +1 072 | 2 912 / 1 464 / +1 448 | 2 855 / 1 478 / +1 377 | 33,40 / 3,43 / +29,97 |
| 2023 | 2 131 / 1 498 / +633 | 2 082 / 1 464 / +618 | 2 146 / 1 478 / +668 | 26,20 / 3,43 / +22,77 |
| 2024 (à fin novembre) | 2 039 / 1 498 / +541 | 1 990 / 1 464 / +526 | 2 049 / 1 478 / +571 | 23,98 / 3,43 / +20,55 |
| 2025 | 1 711 / 1 498 / +213 | 1 765 / 1 464 / +301 | 1 771 / 1 478 / +293 | 24,52 / 3,43 / +21,09 |

Réserve : le prix de cession retenu est celui de la fin d'année, alors que le prix d'importation est la moyenne de l'année ; quand la cession a changé en cours d'année (2017, 2018, 2020, 2021, 2022), l'écart surestime ou sous-estime l'écart moyen. Pour 2015, seul le numéro de septembre existe (essence 910 / 1 065 ; gasoil 858 / 942 ; bouteille 12,662 / 3,222). Le numéro de décembre 2024 n'a pas été récupéré (capture en redirection).

## 6. Références

Déjà proposée : `one-conjoncture-energetique` / `one-conjoncture-energetique-2015-2021-archives`. À étendre :
```json
{"id": "one-conjoncture-energetique", "type": "report", "title": "Conjoncture énergétique", "author": [{"literal": "Observatoire national de l'énergie et des mines"}], "issued": {"literal": "mensuel ; numéros de septembre 2015 à juillet 2026"}, "publisher": "Ministère chargé de l'énergie", "publisher-place": "Tunis", "URL": "https://www.energiemines.gov.tn/fr/tc/publications/", "note": "Tableau « Produits pétroliers » de l'annexe des prix ; 78 numéros lus à l'image le 6 octobre 2026 ; adresses et empreintes des numéros de 2020 à 2025 dans one_conjoncture_2020_2025_manifeste.tsv ; numéros de 2015 à 2021 : captures de data.industrie.gov.tn (manifest.tsv de la note n° 3)."}
```

## 7. Notions à glossaire

- **prix de cession** (سعر التفويت — à vérifier par le terminologue) : prix « à la sortie de raffinerie Bizerte par voie terrestre », auquel le produit est cédé aux sociétés de distribution ; source canonique : note (2) du tableau de l'Observatoire.
- **prix de vente nominal** : prix public simulé si le produit était cédé à son prix d'importation (colonne publiée de février à août 2020 seulement).
- **forfait de transport uniforme**, **stockage de sécurité**, **RPD** (redevance de prestations douanières, 3 % du droit de consommation) : composantes nommées par la source, non chiffrées séparément.
- **résultat unitaire** : différentiel entre prix moyen pondéré d'importation et prix de cession, « à titre indicatif ».

## 8. Lacunes

- Aucune composante séparée (droit de consommation, TVA, chaque marge) : la source ne publie que deux agrégats. Les droits et la TVA se reconstituent depuis le Journal officiel — non fait ici.
- Droits, taxes et marges de 2014 à janvier 2020 : absents de la source.
- Structure du 6 février 2021 : composantes non mises à jour par la source. Date de la baisse d'août 2020 : non donnée.
- Numéros manquants listés au § 2 ; numéros de 2023-2026 lus par sondage.
- Aucune recherche infructueuse nouvelle au sens de `docs/recherches.yml` (aucun texte juridique cherché dans cette passe).
