# Banque mondiale (2020, 2022) et FMI (2021) : relevés par entreprise et recoupements avec le volume « Les entreprises publiques »

Date : 4 novembre 2026. Branche `chantier/ep-bm-per2020`. Les relevés sont dans
`precis/fr/entreprises_publiques/listes/` :

| Fichier | Lignes de données | Dont sans valeur (TODO) |
|---|---|---|
| `banque-mondiale-per-2020-entreprises.csv` | 139 | 10 |
| `fmi-2021-arrieres-croises.csv` | 15 | 0 (2 de période incertaine) |
| `banque-mondiale-matrice-reformes-2022.csv` | 18 | 0 |

Les pages citées dans les tableaux sont des pages du fichier anglais, sauf mention « imprimée » ; les colonnes `page_pdf` et `page_imprimee` des relevés donnent les deux. Les pages ont été rendues à l'image (150 dpi, 300 dpi pour la figure du FMI) et relues. Aucun
chiffre n'est estimé. Les rapprochements ci-dessous sont des quotients ou des sommes de valeurs
imprimées, jamais des valeurs nouvelles à verser.

## 1. Ce qu'il faut savoir d'abord

- **Le rapport de la Banque mondiale « complet » et la « synthèse » du livre sont le même texte.**
  Le fichier `bm_2020_per_overview.pdf`, que la série du volume cite, a 79 pages comme
  `bm_2020_149126_tunisia_per_en.pdf` ; le texte extrait ne diffère que sur la couverture, et la
  couverture porte « Overview Report ». La clé `wb-tunisia-per-2020` (fonds commun) convient donc
  aux relevés ; aucune clé `-complet` n'a été créée. La fiche de source de tunisia-data parle d'un
  « rapport complet » distinct du résumé : à corriger.
- **Pages du rapport de la Banque mondiale.** Numéro imprimé = page du fichier moins 15 dans le
  corps ; le résumé exécutif est en chiffres romains (fichier 8 = vii, 11 = x, 12 = xi). La version
  française a les mêmes chiffres (contrôle par le texte, non relu à l'image) ; ses pages de fichier
  sont décalées de 5 à partir de la page 56 du fichier anglais.
- **Le tableau d'arriérés croisés du FMI (DP/2021/019, annexe 4, figure 4.1) n'est pas dans le
  volume.** Aucune citation de `imf-dp-2021-019` ni de la page 103 imprimée. La section « Les
  dettes et créances croisées » de `_garanties.qmd` expose le rapport du ministère des Finances
  (édition LF 2025, fin 2021 à fin 2023, en millions de dinars). La section FMI de `_etudes.qmd` cite la
  consultation article IV (`imf-tunisia-art4-2020`) : 6,2 milliards de dinars d'arriérés des
  entreprises envers l'État et 8,8 milliards de l'État envers elles à fin juin 2020. La fiche de
  tunisia-data dit que les chiffres du DP viennent de l'annexe 9 de la LF 2021 « déjà dans nos
  données » ; la série du volume ne contient que l'édition LF 2025 : à vérifier.

## 2. Écarts et concordances, chiffre par chiffre

### Agrégats déjà dans le volume (série `entreprises-publiques-etudes-rapportees`, clé `wb-tunisia-per-2020`)

Les onze lignes de la série (1,3 milliard et 1,5 % du PIB de pertes des 20 plus grandes ; 26 % pour
la STEG ; 300 millions de dinars pour l'eau ; 564 millions pour les transports ; 190 000 salariés ;
5 % de l'emploi ; 9 à 10 % du PIB ; 5,4 milliards et 6 % du PIB pour la dette garantie de la STEG)
sont **identiques** aux valeurs relevées. Un point de forme : le volume porte « 11 » comme page de
ces lignes avec un TODO caché (`_etudes.qmd`, section Banque mondiale) disant qu'il s'agit de la page
du fichier. Le numéro imprimé est **x** (résumé exécutif). Pour la dette de la STEG, le volume
donne 57 et 42 : conforme (fichier 57, imprimé 42).

### STEG, dette extérieure garantie

| Source | Valeur | Date |
|---|---|---|
| Banque mondiale, fichier 57 (imprimée 42) | 5,4 milliards de dinars, 6 % du PIB, « about 50 percent » des garanties extérieures des entreprises publiques | 2016 |
| Série `garanties-etat` (LF 2022, p. 58) | encours garanti extérieur 9 261,9 MD ; total 11 269,5 MD (11,83 % du PIB) | fin 2016 |
| Livre blanc 2018 (série des études) | dette extérieure garantie des entreprises publiques 12 % du PIB, STEG « plus de 50 % » | 2015 |

5,4 milliards font 58 % de l'encours extérieur de 9 261,9 MD et 48 % de l'encours total. La Banque
mondiale écrit « environ 50 % » ; le quotient avec l'encours extérieur est plus haut de huit
points. Le périmètre de la Banque mondiale (« SOEs ») et celui de l'encours garanti du ministère
(entreprises et établissements) ne sont pas les mêmes. TODO : écart non résolu.
Avec le Livre blanc, 6 % du PIB pour la STEG et 12 % pour l'ensemble sont cohérents, à un an
d'intervalle.

### Transferts aux entreprises de transport

| Source | Valeur | Année |
|---|---|---|
| Banque mondiale, fichier 11 et 57 (imprimées x et 42) | 564 millions de dinars (0,6 % du PIB), « we identify all these transfers in the budget and estimate them » | 2016 |
| Série `transport-transferts-par-entreprise` (LF 2020, réalisations) | ministère du Transport, total 575,611 MD (investissements 110,569 ; interventions 461,587) | 2016 |
| Même série, 2016 | Transtu 147,623 (interventions 126,543) ; SNCFT 110,791 (65,5) ; sociétés régionales 253,955 (241,955) | 2016 |

Écart de 11,6 millions de dinars (2 %) entre 564 et 575,6. La Banque mondiale ne dit pas quelles
lignes elle additionne. Les valeurs par entreprise de la Banque mondiale sont de 2015 et 2010 (SNCFT 55 et 38 millions ;
« state support » de 409 et 220 millions pour les sociétés de transport de voyageurs, périmètre non précisé) : la série du volume
commence en 2016, **aucune comparaison de même année n'est possible**. TODO : rapprocher
quand une édition donnera 2015.

### Entreprises pour lesquelles le volume n'a pas d'homologue de même année

Les fiches du ministère des Finances (`entreprises-publiques-fiches-entreprises`) commencent en
2018, les transferts en 2016 ou 2017 : les chiffres de 2010 à 2016 de la Banque mondiale n'ont donc
pas de pendant. Liste, pour mémoire :

- **STEG** : subventions de l'État 3,2 % du PIB et 82 % de ses recettes (2011-2014 ; définition de
  la Banque mondiale, qui inclut des subventions indirectes) contre la « subvention d'exploitation »
  de 2 323,1 MD en 2014 et 0 en 2016 de `_energie.qmd` (fiche du ministère). Les deux ne se comparent pas.
  Investissements de 650 millions par an ; factures impayées de 1,6 milliard (2016) ; pertes
  techniques ; la dette de 12 900,1 MD fin 2020 du volume est une dette totale, d'une autre date.
- **SONEDE, ONAS, SECADENORD, GDA** : déficits hors subventions de 2015 ; arriérés de clients de
  340 millions de dinars (2015). Le volume donne, pour fin 2023, la créance de la SONEDE sur l'État
  (809,2 MD) et la dette de l'ONAS envers lui (252,0 MD) : autre notion, autre année.
- **Tunisie Autoroutes** : déficit de 38 millions de dinars en 2016 (42 % des recettes), dette de
  1,28 milliard fin 2016, 407 km. Le volume donne les transferts du budget (180,0 MD en 2019) ; pas
  de dette ni de longueur.
- **Transtu, sociétés de Sfax et du Sahel** : voyageurs 2010 à 2015, parc de bus. Le volume n'en a pas.
- **SNCFT** : 2 153 km, recettes d'environ 45 % des coûts d'exploitation. Pas de longueur de réseau
  dans le volume.

### Contrats de performance et gouvernance (matrice des réformes, mars 2022)

| Point | Matrice, p. 111-112 et 126 | Volume (`_statut.qmd`) | Écart |
|---|---|---|---|
| Contrats de performance signés | mars 2022 : STEG, STIR, RNTA, Office des céréales (« performance report ») ; mai 2021 : « 4 sur 5 sauf Tunisair » | Office des céréales, RNTA, STIR ; contrats-programmes avec les trois banques publiques (source : rapport du ministère des Finances annexé à la LF 2021, p. 136-158) | **La matrice ajoute la STEG.** Le volume n'a pas le commentaire de mai 2021. |
| Les cinq plus grandes | STEG, SONEDE, Tunisie Telecom, ONAS, ETAP | absent | La matrice nomme comme signataires STIR, RNTA et Office des céréales, qui ne sont pas dans la liste des cinq : listes différentes, non réconciliées. « Tunisair » du commentaire de mai 2021 n'est pas non plus dans la liste. |
| Article 22 ter de la loi 89-9 | mars 2022 : 11 entreprises, dont 10 avec dérogation aux marchés publics et 1 avec dérogation aux marchés et au recrutement | décret n° 2020-1061 du 30 décembre 2020 : onze entreprises, article 11 bis en plus pour la Compagnie tunisienne de forage | Concordance. Le commentaire de mai 2021 dit « 10 companies » : écart de la matrice avec elle-même. |
| Loi sur la gouvernance des entreprises publiques | déposée à l'ARP en décembre 2019, retirée en 2020, nouvelle loi en préparation | pas relevé dans les chapitres lus | Pas de comparaison. |
| Administrateurs indépendants (au moins 5 sur les 20 de la phase pilote) | décrets 2020-314 et 2020-105 (délai au 31 décembre 2021), aucun texte modificatif publié en mars 2022 | `_statut.qmd` signale la désignation des administrateurs « depuis 2020 » par concours | Numéros de décrets non vérifiés dans le volume. TODO. |
| PPP de l'ONAS | IFC conseil de transaction, deux concessions en cours d'attribution, clôture attendue en 2022 | `_eau_communications.qmd` : pas de mention | Absent du volume. |

La matrice n'imprime aucune date de signature des contrats de performance : seulement la date du
commentaire (mai 2021, mars 2022).

### Arriérés croisés du FMI (2019 et 2020) et séries du volume

| Flux (FMI, % du PIB) | Valeur | Période |
|---|---|---|
| État vers énergie / agriculture / autres EP | 4,9 / 1,4 / 1,2 | juin 2020 |
| Énergie / agriculture / autres EP vers État | 0,5 / 0,5 / 3,4 | juin 2020 |
| État vers fonds de sécurité sociale ; fonds vers État | 0,4 ; 1,2 | non tranchée |

Somme des flèches État vers entreprises : 7,5 % du PIB ; entreprises vers État : 4,4 %. Le rapport
article IV (série du volume) donne 8,8 et 6,2 milliards de dinars, soit un quotient de 1,42 ; le
quotient des sommes du DP est 1,70. Les deux documents sont de la même date (juin 2020) ; ils ne
se recoupent pas sur le quotient. Le DP ne donne aucun PIB de référence : on ne tire pas de
montant en dinars. TODO : lire le texte de l'annexe 4 (autre que la figure) et l'annexe 9 de la LF 2021.
Le volume expose, sans année commune : fin 2021 8 391,8 MD de dettes et 9 864,4 MD de créances ; il
cite aussi « 4 100 MD » de crédits de règlement de la loi de finances complémentaire pour 2020, surtout vers l'Office des
céréales, la STEG, la STIR et la SNDP, dont la nature (énergie et céréales) correspond aux grandes
flèches du FMI. Rien ne permet de rapprocher les montants.

## 3. Incohérences internes de la Banque mondiale

- **Pertes techniques de la STEG** : résumé (p. x) « de 12 à 14 % de l'énergie produite, 2010-2016 » ;
  chapitre 7 (p. 42) « de 12 % de l'énergie injectée en 2010 à environ 15 % ». Dénominateur et valeur
  finale diffèrent.
- **Recettes de la STEG implicites** : les ratios « 43 % des recettes » (factures impayées), « 5,3 % » (200 millions
  d'économie) et « 130 % » (dette garantie) ne reposent pas sur les mêmes recettes, bien que l'année soit la même (2016).
  À ne pas rapprocher entre eux.
- **Figure 7.1** : l'étiquette 13,38 est au-dessus de 2007, 12,03 sous 2011 ; le creux de la courbe est en 2010 et le texte
  donne 12 % en 2010. La ligne 12,03 porte donc l'année « 2010 ou 2011 » ; les deux lignes sont de statut
  `imprime_rattachement_incertain`.
- **Figure 8.4** : étiquettes −72,72 / −74,4 / −31,62 / −123,372 / +2,92 ; le texte donne 73 / 74 /
  32 / 120 (GDA) ; somme des étiquettes −299,192 contre « −299 » imprimé. Concordant à l'arrondi.
- **Figure 9.3** : la barre 2010 n'a que deux segments (Tunis 335,273 ; Sfax 68,563 ; total 403,836
  milliers) alors que le texte dit « plus de 490 millions » de voyageurs en 2010 : le segment Sahel
  manque ou n'est pas imprimé. Pour 2015 la somme (336,1 millions) concorde avec « environ 335 millions ».
  Transtu : 335,273 moins 200,784 donne 134,5, concordant avec les 134 millions du texte.
- **Figure 9.2** : « about 65 percent » du texte pour l'A1 Sud correspond à l'étiquette 2017 ; l'étiquette 2016 est 63 %.
- **Périmètre des 22 % et 409 millions** (p. 57) : le texte parle des « regional public passenger
  transport companies » pour la couverture des coûts et de « the sector » pour les transferts ; la
  fiche de source attribue les deux à « Transtu et sociétés régionales ».

## 4. Illisible, non relevé ou douteux (TODO)

1. Figures sans valeurs imprimées, non lues sur les barres : 7.2 (emprunts de la STEG), 7.1 (hors trois
   étiquettes), 8.4 (coûts et recettes, six entités), 9.4 (parc de bus de la Transtu), barre 2010 de la
   société du Sahel (fig. 9.3).
2. FMI : période des deux flèches État-fonds de sécurité sociale (la chaîne CNSS/CNRPS, CNAM, PCT est lue 2019) ;
   définition de « Other » ; détail par entreprise du bloc énergie (flèche à quatre pointes, 2,5).
3. Matrice : aucune date de signature ; sigle RNTA non développé ; Tunisair du commentaire de mai 2021 ;
   décrets 2020-314 et 2020-105 non vérifiés.
4. Version française de la Banque mondiale : concordance de pages par le texte seulement.
5. Période des « 650 millions par an » d'investissements de la STEG (la phrase ne la donne pas).
6. Figures 7.3 (turbines à gaz), 8.1, 9.1 : non relevées (pas de chiffre par entreprise).
