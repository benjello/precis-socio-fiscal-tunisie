# Note documentaire — « Tunisia Infrastructure Diagnostic » (Banque mondiale, 2019) : relevé et recoupements

Note du documentaliste, arrêtée au 4 novembre 2026. Elle ne rédige rien dans le volume ; aucun `.qmd` n'est modifié.

Relevé : `precis/fr/entreprises_publiques/listes/banque-mondiale-diagnostic-infrastructure-2019.csv` (260 lignes, dont 19 cases « NA » sans valeur) et son manifeste `.csv.yml`. Clé de la source : `wb-infra-diagnostic-2019`. Pages données en page du PDF et en page imprimée (décalage de 6).

Le rapport reprend les rapports annuels des entreprises (source du tableau 1.3 : « Elaboration of SOE annual reports », information « approximate »). Un écart avec le précis n'est donc pas une erreur du précis ni du rapport : il dit seulement que les deux ne disent pas la même chose. Aucun écart n'est tranché ici.

## 1. Contrôles internes au rapport

| Contrôle | Résultat |
|---|---|
| Tableau 1.2 : 1+1+1+2+1+1+2+1+1+12+1+1 | 25, égal au total imprimé |
| Subventions d'exploitation du tableau 1.3, 2017 : 593+1+128+48+126+0+0+0 | 896, égal au chiffre du résumé (p. 1) |
| Dette du tableau 1.3 : somme des neuf valeurs (6 438+606+795+791+587+7+1 280+1 062+1 217) | 12 783 M TND, égal aux « 12,8 Md » du texte (p. 2 et 14) ; mélange 2017 (STEG, SONEDE, ONAS, SNCFT, OMMP, STA) et 2016 (TRANSTU, TUNISAIR, Tunisie Télécom), comme le texte le dit |
| Investissement de la STEG, figure 2.5 : 115+203+137+86+12 (2017) ; 565+108+138+47+13 (2013) | 553, égal au tableau 1.3 ; 871, égal au texte p. 33 |
| Investissement de la STEG, figure 2.5, 2015 : 188+61+109+44+16 | 418 ; le texte p. 33 dit 541 pour 2015. Écart non expliqué |
| Résultat brut d'exploitation = produits − charges (tableau 1.3) | vrai pour STEG, SNCFT, OMMP, STA, TUNISAIR, OACA ; faux pour SONEDE (−26 calculé, −51 imprimé), ONAS (+32 calculé, −96 imprimé), TRANSTU (−128 calculé, −254 imprimé) ; pour ONAS et TRANSTU, produits − charges − subventions d'exploitation redonne la valeur imprimée ; pour SONEDE (−27) non |
| Résultat net agrégé 2017 des neuf entreprises : −1 420 M TND (p. 1, hors TRANSTU) | non reproduit : somme du tableau 1.3 (STEG, SONEDE, ONAS, SNCFT, OMMP, TUNISAIR, OACA) = −1 485 ; avec TUNISAIR et OACA de la figure 1.3 (−140 ; +25) = −1 382. Les deux sommes mélangent des exercices (2016, 2015, 2017) |
| Résultat net 2017 : tableau 1.3 contre figure 1.3 | TUNISAIR −196 contre −140 ; OACA −22 contre +25 ; les autres valeurs sont identiques (STEG −1 194, SONEDE −39, ONAS 3, SNCFT −81, TRANSTU −132, OMMP 44) ; la figure est titrée 2017, la colonne TRANSTU et TUNISAIR du tableau est de 2016 |
| Tableau 1.4 : somme 12 616+766+740+374+7 208 | 21 704, proche des « 22 Md » du résumé (p. 1) ; avec 208 au lieu de 7 208, 14 704 |
| STEG, subventions d'exploitation 2009-2017 | 12 616 M TND (tableau 1.4) ; « 45 % of its revenues » (texte p. 10) ; 51 % (tableau 1.4 et texte p. 12, où la période est 2009-2016) |
| STEG, subventions d'exploitation 2016 | 0 selon le texte p. 34 ; « Annually except in 2016 » au tableau 1.4 ; cohérent |
| STEG, dette 2017 : long terme 5,4 Md + court terme 1,1 Md (texte p. 34) | 6,5 Md ; tableau 1.3 : 6 438 M TND ; l'écart tient à l'arrondi des deux chiffres du texte |
| STEG, perte 2017 : −1,2 Md « excluding state subsidies » (p. 33) | le tableau 1.3 donne −1 194 « net income » ; la figure 1.3 est titrée « after operating subsidies » ; les deux textes disent le contraire l'un de l'autre sur la prise en compte des 593 M TND |
| TUNISAIR, dette 1 062 M TND « (USD 90.8 million) » (p. 30) | le taux de 2,34 donné p. 14 donne environ 454 M USD ; la conversion imprimée est incohérente |
| Inflation cumulée 2009-2017 | 43 % (p. 12), 40 % (p. 1, 13) |

## 2. Recoupements avec le précis, exercice 2017

Sources du précis consultées : `precis/fr/entreprises_publiques/figdata/*.csv` (séries tirées des états financiers de la STEG, des rapports du ministère des Finances sur les entreprises publiques, éditions LF 2020 et LF 2021), `listes/*.csv`, texte des `.qmd` du volume. Les fiches du ministère (`*_fiches.csv`) ne commencent qu'en 2018 : elles ne donnent rien pour 2017. Pour les colonnes en 2016 ou 2015 du rapport (TRANSTU, TUNISAIR, Tunisie Télécom, OACA), les valeurs du précis sont de 2017 ou de 2016 selon le cas, notées.

### STEG (comptes 2017 : `figdata/fig_ep_steg_comptes.csv`, états financiers de 2017, p. 13 et 15 du fichier)

| Grandeur | Rapport (M TND, tableau 1.3) | Précis | Écart |
|---|---|---|---|
| Produits d'exploitation | 4 068 | « Revenus » 4 067,791 | aucun à l'arrondi |
| Subventions d'exploitation | 593 | 593,166 | aucun |
| Résultat net | −1 194 | −1 193,681 (états financiers) ; −1 193,7 (classement du ministère, LF 2021) | aucun |
| Fonds propres | −276 | −276,093 | aucun |
| Dette (emprunts à terme et crédits bancaires à court terme) | 6 438 | concours bancaires 1 065,913 + emprunts non courants 5 371,939 = 6 437,852 | aucun, mais la somme est calculée pour cette note ; le précis ne la donne pas |
| Actif total | 8 978 | « Total des passifs, hors capitaux propres » 9 254,431, moins 276,093 de fonds propres = 8 978,338 | aucun, calcul de cette note |
| Effectifs | 12 388 | 12 388 (LF 2020) | aucun |
| Charges d'exploitation | 4 872 | non donnée (le précis a le résultat d'exploitation −151,076) | non comparable : le rapport donne produits − charges = −804, le précis un résultat d'exploitation de −151 ; le rapport ne dit pas quel poste il appelle « charges d'exploitation » |
| Subventions d'investissement | 125 | non relevée dans le précis | — |
| Investissement | 553 | non relevé dans le précis | — |
| Transferts du budget (ministère, LF 2021) | subventions d'exploitation 593 + d'investissement 125 = 718 | 914,6 | 196,6 ; le périmètre des « transferts du budget » du ministère n'est pas celui des deux subventions du rapport (le précis rapproche STEG et STIR du poste carburants, `_energie.qmd`) |

### Autres entreprises

| Entreprise, grandeur | Rapport | Précis | Écart |
|---|---|---|---|
| SONEDE, effectifs 2017 | 6 318 | 6 312 (LF 2020) | 6 agents |
| SONEDE, transferts du budget 2017 | subventions d'exploitation 1 + d'investissement 23 | 180,7 MD (LF 2021, `_eau_communications.qmd`) | non comparable : le rapport ne compte que deux subventions |
| ONAS, effectifs 2017 | 3 592 | 3 592 (LF 2020 et LF 2021) | aucun |
| ONAS, transferts du budget 2017 | subventions d'exploitation 128 + d'investissement 52 | 58,0 MD | non comparable ; le précis est inférieur à la seule subvention d'exploitation du rapport |
| SNCFT, effectifs 2017 | 4 518 | 4 518 (LF 2020) | aucun |
| SNCFT, résultat net 2017 | −81 | −82,2 (classement LF 2021) | 1,2 |
| SNCFT, transferts du budget 2017 | 48 + 37 | 104,56 | non comparable |
| TRANSTU, effectifs | 7 813 (2016) | 7 529 (2017, LF 2020) | exercices différents |
| TRANSTU, résultat net | −132 (2016) | −167,3 (2017, classement LF 2021) | exercices différents |
| TRANSTU, transferts du budget | subventions d'exploitation 126 (2016) | 154,4 (2017) | exercices différents |
| TUNISAIR, effectifs | 8 000 (2016) | 3 594 (2016, LF 2020) ; 3 765 (2017, LF 2020) ; 3 565 (2017, LF 2021) | écart de plus du double, même exercice 2016 ; le rapport dit « 2016-17, 8 000 agents » dans sa fiche de source ; périmètre (groupe ou société) non établi |
| TUNISAIR, résultat net | −196 (2016) ; −140 (figure 1.3) | −206,6 (2017, classement LF 2021) | exercices différents |
| TUNISAIR, subventions | 0 | transferts du budget 0 (2017) | aucun |
| OACA, effectifs | 4 070 (2015) | 4 033 (2016, LF 2020) ; 3 971 (2017, LF 2020 et LF 2021) | exercices différents |
| Tunisie Télécom, effectifs | NA | 6 244 (2017, LF 2021) | rien à comparer |
| STA (Tunisie Autoroutes), subventions d'exploitation 2017 | 0 | transferts du budget 0 (2017, LF 2021) | aucun |
| OMMP, ces grandeurs | produits 142, charges 101, résultat net 44, effectifs 1 050 | aucune valeur 2017 dans le précis | — |
| Tunisie Autoroutes, STA : autres grandeurs | produits 82, résultat net −38, dette 1 280, effectifs 1 000 | aucune valeur 2017 dans le précis | — |

### Garanties, rétrocessions et prêts du Trésor

| Grandeur | Rapport | Précis | Écart |
|---|---|---|---|
| Garanties, rétrocessions et prêts du Trésor aux entreprises publiques, 2016 | 14 % du PIB (p. 8, renvoi 5), non daté dans la phrase, daté par le renvoi ; p. 3 : « guarantees … 14 percent of GDP in 2016 » | encours de la dette garantie fin 2016 : 11 269,5 MD, soit 11,8 % du PIB (base 2015) ; fin 2017 : 13 671,8 MD, 13,4 % ; fin 2018 : 14,8 % (`figdata/fig_ep_encours.csv`, `_garanties.qmd`) | 2,2 points en 2016 ; le rapport additionne trois flux ou stocks (garanties, rétrocessions, prêts du Trésor), le précis ne donne ici que l'encours garanti ; le PIB de référence du rapport n'est pas précisé |
| Dette des neuf entreprises, 2017 | 12,8 Md TND, 13 % du PIB (12,7 % p. 14) | encours de la dette garantie 13 671,8 MD, 13,4 % du PIB | non comparables : l'un est la dette des entreprises, l'autre les prêts garantis par l'État, tous prêteurs, toutes entreprises |
| Résultat net agrégé 2017 | −1 420 (neuf entreprises, hors TRANSTU) | −2 723,1 MD pour 78 entreprises (`fig_ep_resultats.csv`) | périmètres différents |

## 3. TODO pour le documentaliste

- TODO : tableau 1.4, SONEDE : l'image porte « ¹⁵7208 ». Le renvoi 15 est collé à un nombre qui peut être 7 208 (somme des cinq lignes = 21 704, proche de « 22 Md » du résumé) ou 208 (somme = 14 704 ; plus plausible pour une entreprise dont le rang est le cinquième et qui reçoit « relatively modest » de subventions, 9 % des produits). Le relevé garde 7208, imprimé. À trancher par le rapport source de la Banque (rapports annuels de la SONEDE 2011, 2015, 2016) ; ne pas citer ce chiffre avant.
- TODO : figures 1.4 (croissance des produits en termes réels), 1.5 (produits par employé) et 1.6 (évolution de la dette 2009-2017 en indice, rapport dette/actif) : graphiques sans valeurs imprimées, non lus, aucune ligne dans le relevé. La figure 1.6 est en pourcentage d'évolution (axe 0 à 250 %) pour la dette, en pourcentage pour le rapport dette/actif ; aucun chiffre sur les barres ni les courbes.
- TODO : tableau 1.3, ligne « Debt » du second tableau : l'étiquette porte l'appel b (valeurs de 2015), la définition de la dette (renvoi c) est celle de la ligne du premier tableau. La dette de Tunis Air (1 062) est datée de 2016 par le texte p. 30 ; celles d'OMMP, STA et Tunisie Télécom n'ont pas de date certaine (2017 pour OMMP et STA par la colonne, 2016 pour Tunisie Télécom).
- TODO : tableau 1.3, SONEDE : résultat brut d'exploitation −51 contre −26 (produits − charges) ; ONAS et TRANSTU : le résultat brut d'exploitation imprimé est net des subventions d'exploitation, pas STEG ni SNCFT. À signaler avant de reprendre une ligne « résultat brut » du rapport.
- TODO : le texte (p. 1) donne −1 420 M TND de résultat net agrégé 2017 pour les neuf entreprises hors TRANSTU, que le tableau 1.3 ne permet pas de reconstituer (−1 485 ou −1 382 selon la source de TUNISAIR et d'OACA). Ne pas reprendre ce total comme somme du tableau.
- TODO : OMMP, texte p. 27 : « 83 percent increase in OMMP's annual revenue from 2016 (TND 44 million) » ; 44 est le résultat net 2017 du tableau 1.3, les produits sont 142. La phrase est ambiguë ; relevée comme `produits_exploitation_texte` 2016 = 44 avec la réserve en note.
- TODO : Tunisair, effectifs 8 000 (rapport) contre 3 594 à 3 765 (ministère) : établir si le rapport compte le groupe.
- TODO : STEG, investissement 2015 : 541 (texte p. 33) contre 418 (somme de la figure 2.5) ; le texte écrit aussi « 92 percent decrease » pour 871 → 541.
- TODO : transferts du budget du ministère (STEG 914,6, SONEDE 180,7, ONAS 58,0, SNCFT 104,56 en 2017) contre les subventions d'exploitation et d'investissement du rapport : rapprocher les définitions dans les états financiers de chaque entreprise avant d'écrire qu'une série contredit l'autre.
- TODO : stock de prêts rétrocédés et de prêts du Trésor fin 2016 : non trouvé dans `listes/` ni `figdata/` ; le précis n'a que l'encours garanti et les flux de l'année (`fig_ep_flux.csv` : prêts du Trésor rétrocédés 567,5 MD en 2017, échantillon de 33 entreprises). Rien d'autre cherché ; à chercher dans le rapport du ministère sur les transferts et les garanties (`minfin-transferts-2020`) avant de rapprocher les 14 %.
