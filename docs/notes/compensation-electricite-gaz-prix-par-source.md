# Note documentaire : prix des sources de gaz de la STEG (figure `fig-compensation-eg-gaz-sources`)

## Réponse au propriétaire

**Les prix sont disponibles en partie, et jamais pour les quatre sources la même année.**

| Bloc de la figure | Ce qui est publié | Ce qui ne l'est pas |
|---|---|---|
| Gaz algérien | Un prix moyen FOB des achats contractuels et additionnels réunis : 2005, 2006, 2008-2014, 1er semestre 2015 (ETAP), 2008-2013 (Contrôle général des finances), 2013-2025 (ONE) | Le prix de chaque part. Il existe pourtant : SONATRACH envoie chaque mois deux factures, l'une pour la quantité contractuelle, l'autre pour l'additionnelle, « chacune avec son prix unitaire » (rapport du Contrôle général des finances (CGF) de 2014, p. 42, § 64). Aucune source lue ne publie ces prix unitaires. |
| Miskar | Un prix seulement depuis le 8 juin 2022, quand la concession passe à l'ETAP (ETAP RA 2022 p. 60 ; RA 2023 p. 53 ; RA 2024 p. 60) | Tout 1996-2022 : le gaz était vendu par BG/Shell, et l'on n'a que l'historique de la formule (point 2) |
| Redevance | 90,8 DT/tep administré jusqu'en 2014 | Aucun prix après 2014 : un mode de valorisation (« prix international ») et un dû budgétaire pour 2015 |
| Autres champs nationaux | Prix par champ 2016-2019 et 2021-2024 (ETAP) | — |

**Ce que mesurent les tableaux par champ de l'ETAP.** Quantités et montants sont **la part de l'ETAP**, non la production du champ.
- Le rapport ETAP / prélèvements STEG vaut 0,500 pour Hasdrubal (2016, 2019), 0,50 pour Oued Zar et Adam, 0,51 pour Maâmoura et Baraka, 0,497 pour Nawara (2021) et environ 0,55 pour Chergui (détail dans `comparaison_etap_steg_par_champ.csv`).
- Le prix moyen de l'ETAP n'est donc pas le prix du bloc « gaz national » de la figure.
- Deux points sont des **inférences**, non des faits lus :
  - le prix par champ vaudrait pour tout le champ, parce que les co-titulaires signent ensemble comme vendeurs (ETAP RA 2018 p. 68-69) ;
  - les tep de l'ETAP seraient sur la même base que celles de la STEG (PCS), puisque le rapport tombe à exactement 0,500.

## 1. Gaz tunisien champ par champ (famille A', rapports de l'ETAP)

`etap_gaz_tunisien_steg_par_champ.csv` donne 117 lignes : année, champ, quantité, $/tep, montant en $ et, de 2016 à 2019, montant en DT. Pages imprimées :

| Année | Page | Prix moyen ($/tep) | Fourchette par champ ($/tep) |
|---|---|---|---|
| 2016 | 68 | 159,847 | 145-172 |
| 2017 | 60 | 224,900 | — |
| 2018 | 75 | 291,273 | — |
| 2019 | 75 | 288,113 | — |
| 2021 | 58 (ktep et M$ dans la source) | 280,330 | — |
| 2022 | 60 | 424,505 | Miskar 466,041 sur 248 ktep, du 8 juin au 31 décembre |
| 2023 | 53 | 377,612 | Miskar 383,526 sur 409,5 ktep |
| 2024 | 60 | 376,072 | Miskar 386,643 sur 352,8 ktep |

Les quantités et les montants en $ s'additionnent jusqu'au total imprimé. Trois incohérences sont **dans la source** et sont notées dans le CSV :
- **2018, Hasdrubal** : 291 393 tep × 321,197 = 93,6 M$, alors que le montant imprimé est 82,6 M$.
- **2018, Maâmoura/Baraka** : le montant en DT reprend celui de 2017.
- **2019** : les lignes en DT font 506,9 MDT, le total imprimé 566,7 MDT.

**Années sans tableau par champ** (`etap_gaz_tunisien_steg_totaux.csv`) :

| Année | Ce qu'on a | Source |
|---|---|---|
| 2015 | Total seulement : 870 ktep pour 230 M$, soit 264,4 $/tep (mon calcul) | RA 2015, sans couche texte, lu à l'image, p. 58 |
| 2006 | 275 ktep, quantité seule | RA 2006, lu à l'image, PDF p. 55 |
| 2007 | 279 ktep, quantité seule | RA 2007, PDF p. 39 |
| 2009-2014 | Quantités et liste des champs seulement ; aucun prix, formule ni montant | RA 2009 p. 25, 2011 p. 53, 2012 p. 63, 2013 p. 61, 2014 p. 79 |
| 2014 et 2020 | Valeurs déduites (famille E), à ne pas mettre en série sans avertissement | voir ci-dessous |

- **2014** : 418 M$, déduit de « baisse de 188 millions US$ » (RA 2015 p. 58).
- **2020** : environ 654 ktep et 143 M$, déduits des écarts donnés par le RA 2021 p. 57. Le rapport 2020 reste introuvable.

## 2. Formule du prix du gaz national : le désaccord 80 % / 85 % s'explique par les textes

Détail dans `formule_prix_gaz_national.csv` (21 lignes).

**Deux régimes de prix coexistent.**
- **Décret-loi n° 85-9 du 14 septembre 1985, art. 33** (JORT n° 65, p. 1181, lu à l'image) : « un prix équivalent à 85 % du prix international d'exportation FOB dans les ports méditerranéens relatif au fuel oil à haute teneur en soufre », à pouvoir calorifique égal, pour un gaz rendu au point d'entrée du réseau principal.
- **Code des hydrocarbures, loi n° 99-93, art. 73.1** (JORT n° 67 de 1999, p. 1479) : le prix « sera fixé par décret ». C'est le **décret n° 2000-1027**, qui retient 80 % du fuel à 1 % de soufre FOB Med Italy (Platt's), en moyenne sur les neuf mois précédents.
- Selon les art. 3 et 5 de la loi de promulgation (p. 1465), les concessions développées avant le code restent sous leur ancien régime, sauf si leur titulaire opte pour le code.

**L'ANER décrit l'état d'avant mai 2000.** Son étude date d'avril 2000 ; elle donne 0,85 × fuel HTS pour Miskar, ce qui est le régime de 1985.

**Le passage de Miskar au code, selon le CGF (2014).**
- Un avenant au contrat Miskar signé le 13 mai 2000, et une lettre de la Direction générale de l'énergie du 6 mai 2000, appliquent le prix du code à Miskar avec effet rétroactif à mars 2000 (p. 108, § 170-171).
- Le CGF juge ce passage irrégulier : le titulaire n'a pas exercé l'option. Il le chiffre à environ 105,1 MD de surcoût pour la STEG sur 2000-2013.
- Le même jour sont signés les deux avenants approuvés par les lois n° 2000-80 et 2000-81 (JORT n° 64 de 2000, p. 1874). Leur texte n'est pas publié.
- L'**arrêté du 12 décembre 2000** (JORT n° 101, p. 3143-3144, lu) liste les titres admis au code. Ni Amilcar ni Miskar n'y figurent.

**Divergences à exposer, sans les trancher.**
- **Franig et Baguel** : 0,80 × HTS selon l'ANER ; 84 % HTS « ajusté » selon le CGF (p. 107) ; 85 % selon le décret-loi.
- **Coût du passage au code** : le CGF donne 93,7 MD pour l'ensemble des titres en 2000-2013 (p. 99) et 105,1 MD pour Miskar seul (p. 108). Les deux renvoient à l'annexe 38, qui n'est pas dans le PDF.

**Autres éléments du CGF.**
- Coefficients ajustés au point de livraison (p. 107) : Adam et Maâmoura-Baraka 83 % HTS, Djebel Grouz 82 % HTS, El Borma 78 % BTS, Chaouech Essaida 65 % BTS.
- Adam passe de 83 % à 82,25 % le 30 novembre 2012 (p. 102).
- Rabais de qualité sur Miskar par l'avenant n° 2 du 14 septembre 2012 (p. 102).
- Pénalités en cas de livraison manquante : 20 % pour les fournisseurs contre 100 % pour la STEG (p. 103).

**Après 2012.**
- L'avenant n° 4 Baguel et Franig du 17 août 2018 change « le prix contractuel », sans en donner la valeur (STEG RA 2018 p. 14 ; ETAP RA 2018 p. 69).
- Le décret-loi n° 2022-44 (JORT n° 70 de 2022, p. 1962) approuve la convention Miskar avec l'ETAP. Comme pour les accords de 1993 et 2000, le texte de la convention n'est pas reproduit au JORT.
- Les modificatifs du code (lois n° 2002-23, 2004-61, 2008-15, 2017-41) ne touchent pas l'art. 73. Aucun modificatif du décret 2000-1027 n'est identifié.

## 3. Gaz algérien : contractuel et additionnel

Détail dans `gaz_algerien_contractuel_additionnel.csv` et `cgf2014_gaz_algerien_prix_moyen.csv`.

**Aucun prix publié distinct** pour l'une ou l'autre part, dans aucune des sources lues :
- rapports de l'ETAP 2005-2015 : « contractuels et additionnels », une seule valeur ;
- CGF p. 44-45 : un prix moyen unique de 458,064 ; 275,253 ; 362,646 ; 482,708 ; 546,3 ; 522,074 $/tep pour 2008-2013, la dernière année étant provisoire ;
- rapports annuels et états financiers de la STEG ;
- ONE.

**Ce que les sources disent du contrat.**
- Le prix SONATRACH est indexé sur le gasoil (القازوال) Platt's. La référence à 1 % de soufre est employée depuis décembre 2009, Platt's ne publiant plus le 2 % ; l'avenant n° 2 du 26 septembre 2013 l'officialise (CGF p. 43).
- La STEG achète directement depuis le 1er juillet 2015. L'avenant n° 4 au « contrat-cadre » porte le contractuel à 2,5 milliards de m³ en 2016 (STEG RA 2016 p. 52).
- L'**avenant n° 7** relève le prix de « +2 $US/MMBTU » sur les livraisons depuis octobre 2021, avec 156 MDT de rattrapage (états financiers STEG 2022 p. 29). La note ne dit pas s'il vise le contractuel ou l'additionnel.

**Rupture de définition en 2015.** « Contractuel » change de sens : 389 ktep en 2014, 2 246 ktep en 2015 (STEG RA 2014 p. 13, RA 2015 p. 11).

**Valeur FOB nouvelle** (`gaz_algerien_fob_complements.csv`) :

| Période | Quantité | Valeur FOB | Prix | Source |
|---|---|---|---|---|
| 2006 | 502 ktep | 146 M$ | 290,8 $/tep (mon calcul) | ETAP RA 2006, OCR et image, p. 52 |
| 1er semestre 2015 | 1 096 ktep | 417,62 M$ | « 381,109 US$/TEP » (imprimé) | ETAP RA 2015 p. 57 |
| 2007 | 874 ktep | non donnée | — | RA 2007, PDF complet lu |

## 4. Redevance après 2014

Détail dans `redevance_apres_2014.csv`. **Aucun prix n'est publié.**

- **Mode de valorisation** : états financiers 2015, note 11, p. 26 : « A partir de 2015, les achats de gaz sont désormais comptabilisés et réglés au prix international ». Le rapport du projet de loi de finances complémentaire (LFC) 2015 (§ 20) dit de même.
- **Montant dû, recette de l'État** : 115 MDT dus en 2015 sur la part livrée à la STEG (rapport semestriel du ministère des Finances, p. 18). Le ratio de 429 DT/tep est une évaluation, pas un prix.
- **Ce n'est pas un prix** : l'ONE compte la redevance comme une « importation à valeur nulle », qui est une convention statistique.
- **Pas de ligne propre** :
  - les états financiers de la STEG 2015 (p. 39), 2016-2019 et 2021-2023 ne ventilent pas les achats de combustibles par source ;
  - les notes 2020 n'ont pas été lues (pas de couche texte) ;
  - les rapports de l'ETAP ne valorisent pas la redevance de transit.
- **Taux de la redevance** (en quantité, pour le contexte) : loi n° 2005-102, art. 2 (5,25 %, 6 % et 6,75 %), puis loi n° 2019-71 (5,25 % depuis le 1er octobre 2019, JORT n° 63 de 2019, p. 2435).

## 5. Rapports de l'ETAP 2006 et 2007

- **2006** : 66 pages océrisées en français sur les pages 1 à 46 ; les pages 52 à 55 sont lues à l'image.
- **2007** : le PDF n'est pas endommagé, il est **tronqué**.
  - Copie de tunisia-data et sa ligne de catalogue : 137 920 512 octets, sha256 603c2a04…
  - Fichier complet retéléchargé : 316 542 767 octets, sha256 `84e932ce9d1d267f55bbdff7af3126f3e5d27891f87c666cf3087e9211997a13`, rangé dans `steg-series-2/r2007/etap_ra_2007.pdf`.
  - **À remplacer dans tunisia-data, ce que je n'ai pas fait.**
- Toutes les océrisations sont arrêtées : seuls mes propres processus ont été tués, par leur PID. Aucun processus ne tourne.

## Raccordements

**Possibles :**
- Le prix moyen du gaz algérien du CGF 2008-2013 égale celui de l'ETAP au millième pour 2011 et 2012.
- Les tableaux par champ de l'ETAP se raccordent d'une année à l'autre (même tableau).

**Impossibles :**
- Prix ETAP « gaz tunisien » et bloc national de la STEG : ce sont des parts différentes, et Miskar est absent jusqu'en 2022.
- Quantités contractuelles d'avant et d'après 2015.
- Redevance : prix de 90,8 DT/tep, puis montant dû.
- CGF 2013 et ETAP 2013 : 1 966,5 contre 2 044,2 ktep.

## Fiches proposées pour `docs/recherches.yml`

Le registre n'a ni la fiche de 1993 ni celle de 2006-2007 (vérifié avec `lister`).

**a) `r-arrete-1993-10-08-prix-gaz-steg`** (à créer)
- Nouvelle piste : l'« art. 8 », avec deux formules selon le seuil de 27,3 $ le baril (CGF p. 42, § 65), contre le « prix fixe 90,800 » ailleurs.
- Requêtes jort_cache lancées : `titre LIKE '%gaz%' AND (prix|tarif|cession)`, toutes années. Résultat : rien en 1993.
- `iort_ar` : سعر إحالة الغاز ; قرار وزير الاقتصاد الوطني 8 أكتوبر 1993.

**b) `r-prix-gaz-commercial-concessions-apres-2000`** (à créer)
- Objet : modificatif du décret 2000-1027 et textes des conventions et avenants Miskar, Amilcar, Franig et Baguel.
- Requêtes françaises lancées : `titre LIKE '%Miskar%'|'%prix du gaz%'|'%gaz commercial%'|'%Amilcar%'` ; liste des modificatifs du code.
- Requêtes arabes lancées sur les titres de jort_cache : ميسكار, مسكار, سعر الغاز, الغاز التجاري. Résultat vide, mais **ce vide n'est pas probant** : les notices de 1993 à 2000 ont des titres français.
- Sur le miroir iort, la recherche Python trouve `loi_93_102`, `loi_2000_81` et `dec_loi_2022_44`. Une première recherche, faite avec `grep`, ne trouvait rien : elle ne compte pas comme résultat.
- Couverture : titres jusqu'au 2026-10-02. Fascicules lus : 1985 n° 65, 1993 n° 83, 1999 n° 67, 2000 n° 101.
- Résultat : aucun modificatif. Les conventions et avenants ne sont pas publiés.

**c) `r-etap-achats-gaz-algerien-2006-2007`**
- Passe : résultat partiel. 2006 trouvé, 2007 sans valeur (rapport complet lu).
- La fiche reste ouverte pour 2007 (Comtrade seulement).

**d) `r-etap-rapport-annuel-2020`**
- Objet : le rapport annuel 2020 de l'ETAP, avec le tableau par champ de 2020.
- Le 404 vient de la passe précédente.

## Lacunes et demandes

**Lacunes :**
- Prix de Miskar 1996-2022 (vendeur BG/Shell).
- Prix SONATRACH contractuel et additionnel, 2005-2025.
- Second semestre 2015 du gaz algérien.
- Redevance après 2014.
- Notes des états financiers 2020.
- Couverture partielle :
  - OCR des rapports STEG 2023 et 2024 : partielle (74 et 50 pages traitées) ;
  - année de mise en production de Miskar lue « 1998 » au CGF p. 106, à revérifier.

**À demander à l'ETAP :**
- le rapport annuel 2020 ;
- les factures SONATRACH de 2005 à juin 2015, avec les deux prix unitaires ;
- les contrats de vente de gaz et leurs avenants, Miskar compris.

**À demander à la STEG :**
- les prix contractuel et additionnel depuis juillet 2015, et l'avenant n° 7 ;
- le prix d'achat de Miskar à BG/Shell, 1996-2022 ;
- la valorisation de la redevance depuis 2015 ;
- les états financiers 2024.

**À demander au CGF ou au ministère** : les annexes 11, 19, 20, 38, 39, 45 et 46 du rapport de 2014. Elles sont citées, mais absentes du PDF de 192 pages.

## Références candidates (à créer, en CSL-JSON)

| Clé suggérée | Type | Notice | Origine et note |
|---|---|---|---|
| `jort-decret-loi-1985-9` | legislation | décret-loi n° 85-9 du 14 sept. 1985, JORT n° 65, p. 1176-1182 | pist.tn `/jort/1985/1985F/Jo06585.pdf` |
| `jort-arrete-2000-12-12-code-hydrocarbures` | legislation | arrêté du 12 déc. 2000, JORT n° 101, p. 3143-3144 | — |
| `jort-dl-2022-44-miskar` | legislation | décret-loi n° 2022-44, JORT n° 70 de 2022, p. 1962 | — |
| `etap-ra-2006` | report | ETAP, *Rapport annuel 2006* | — |
| `etap-ra-2015` | report | ETAP, *Rapport annuel 2015* | — |
| `etap-ra-2007` | report | ETAP, *Rapport annuel 2007* | à rattacher au fichier complet |
| `steg-ef-2015` | report | STEG, états financiers 2015 | à vérifier dans references.json |
| `steg-ef-2022` | report | STEG, états financiers 2022 | à vérifier dans references.json |

## Fichiers

Tous dans `/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/15adcd5f-c210-406f-907e-f6545e1e97a0/scratchpad/steg-series-2/` :
- `etap_gaz_tunisien_steg_par_champ.csv`
- `etap_gaz_tunisien_steg_totaux.csv`
- `comparaison_etap_steg_par_champ.csv`
- `formule_prix_gaz_national.csv`
- `gaz_algerien_contractuel_additionnel.csv`
- `gaz_algerien_fob_complements.csv`
- `cgf2014_gaz_algerien_prix_moyen.csv`
- `redevance_apres_2014.csv`
- `r2007/etap_ra_2007.pdf`, le rapport 2007 complet
- `cgf/`, les pages du rapport du CGF lues à l'image
