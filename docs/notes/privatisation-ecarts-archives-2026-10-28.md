# Privatisation : écarts du recueil de la DGPV, ce qu'en disent les archives du web

Note de recherche du 27 octobre 2026, pour le chapitre « Céder » du volume « Les entreprises
publiques ». Aucun chapitre modifié. Les pièces brutes sont hors git, sous
`~/projets/tunisia-data/data/raw/entreprises-publiques/archives-web/` (abrégé `AW/` ci-dessous).
Les séries de référence sont celles de `tunisia-data` (branche
`donnees/privatisation-modes-operations`) : `privatisation_recueil_operations_1998_2008.csv`
(le « recueil HTML »), `privatisation_bilan_global_par_mode.csv`,
`privatisation_recueil_recoupement_annuel.csv`, `privatisation_recettes_annuelles_1987_2009.csv`.

## 1. Résultat en bref

| Écart constaté | Expliqué ? | Par quelle pièce |
|---|---|---|
| 1998 : recueil − classeur 2010 = −33,5 MD | oui, au millier de dinars près | recueil arabe de décembre 2009 ; page d'index de janvier 2007 (le recueil part du 01/10/1998) ; fiche CJO (privatisée le 16/10/1998, incluse) |
| 1999 : +19,6 MD | oui, au millier près | recueil arabe 2009 ; classeur de 2005 et feuille « Feuil5 » (doublons Freeshop et ONP) |
| 2008 : −148,6 MD | oui, au dinar près | recueil arabe 2009 ; page « Opérations réalisées en 2008 » |
| 2000-2007 : écarts de 0 à 4,4 MD | oui | recueil arabe 2009 (lignes pluriannuelles, dates différentes, BH) |
| Concessions : 6 noms au recueil, 5 entreprises au bilan | reconstruit | le bilan range chaque entreprise sous un seul mode ; ONP et SOCOMENA mêlent concession et vente d'actifs ; la règle « mode du plus gros montant » retrouve exactement la page « par mode » et place SOCOMENA en concession, ONP en actifs |
| Tourisme et artisanat : total imprimé = somme des lignes + 3 000 mD | non | le recueil arabe 2009 confirme la somme des lignes (222 051 mD), pas le total imprimé ; la version de septembre 2007 avait déjà un total faux, dans l'autre sens |

## 2. Sources trouvées

Toutes les captures sont téléchargées en mode brut (`id_`) depuis `web.archive.org`.

### 2.1 Pièces principales

| Pièce | URL d'origine | Capture | Fichier `AW/` | Contenu |
|---|---|---|---|---|
| **Recueil arabe des opérations 1986-2009** | `http://www.privatisation.gov.tn:80/www/en/download/recueil_op_privatisation_ar.pdf` | 2012-09-07 03:35:23 | `dgpv_recueil_op_privatisation_ar_wb20120907.pdf` (sha256 `57dc4af9…`) | Premier ministère, DGPV, « عمليات التفويت في إطار عمليات تخصيص وإعادة هيكلة المنشآت ذات المساهمات العمومية موزّعة حسب القطاع (1986-2009) », arrêté au 31 décembre 2009, 27 p., PDF créé le 24/12/2009, texte extractible. Une ligne par opération : objet, montant en milliers de dinars, année, mode (بيع أصول, بيع أسهم, عرض عمومي للبيع, إسناد لزمة, الزيادة في رأس المال), acquéreur. 15 secteurs, 219 en-têtes d'entreprise. Total imprimé p. 27 : **5 976 376 mD, 427 opérations**. |
| Classeur « top cession » | `http://www.privatisation.gov.tn:80/www/en/download/top_cession_20003-12-31.xls` | 2008-09-20 21:51:00 | `dgpv_top_cession_2003-12-31_wb20080920.xls` (sha256 `0562a140…`) | Enregistré le 27/09/2005. Feuille 1 : 333 opérations 1986-2002 avec mode ; feuille « Cessions » : liste des entreprises « jusqu'au 31 décembre 2003 », datée du 26 mai 2004. |
| Classeur des recettes annuelles 1987-2008 | `https://privatisation.pm.gov.tn/sites/default/files/2022-04/recettes-annuelles-1987-2008-fr.xls` | 2026-01-18 14:08:58 | `dgpv_recettes_annuelles_1987-2008_fr_wb20260118.xls` (sha256 `4ddb80a3…`) | Enregistré le 10/03/2009. Feuille « Recettes fr » : total **5 963 214,2 mD**, 2008 = 301 542,2. Feuilles « Feuil4 » (1994-1998 par secteur) et « Feuil5 » (1994-2003 par mode, avec une colonne « Total 1999-2004 corrigé »). |

### 2.2 Pages de l'ancien site (`www.privatisation.gov.tn/www/…`, ASP)

| Page | Capture | Fichier `AW/` | Ce qu'elle donne |
|---|---|---|---|
| Bilan global (`fr/doc.asp?mcat=1&mrub=49&msrub=8&dev=true`) | 2007-01-08 19:17:59 | `dgpv_old_bilan_global_2006-10-31_wb20070108.html` | au 31/10/2006 : 203 entreprises, 5 557 MD ; totale 100, partielle 40, OPV 12, **concession 5**, liquidation 40, autres 6 |
| Index du recueil (`fr/doc.asp?mcat=1&mrub=49&msrub=7&dev=true`) | 2007-01-08 19:17:47 | `dgpv_old_recueil_index_wb20070108.html` | « Statistiques générales **(Depuis le 01/10/1998 au 31/10/2006)** » |
| Statistiques agrégées (`…msrub=20&dev=true`) | 2007-01-06 13:37:37 | `dgpv_old_stats_agregees_wb20070106.html` | « Données actualisées au 31 octobre 2006 » |
| Par période (`fr/doc.asp?docid=270…`) | 2007-09-15 21:09:15 | `dgpv_old_par_periode_wb20070915.html` | IXe Plan : 1 189 MD, 174 opérations ; total 5 571 MD, 205 entreprises, 409 opérations ; note : une entreprise est datée de sa première opération |
| Par mode (`docid=271`) | 2007-09-15 21:11:29 | `dgpv_old_par_mode_wb20070915.html` | 205 entreprises ; **concession 5, 756 MD** ; actifs 104, 405 MD ; actions 96, 4 410 MD |
| Par secteur (`docid=272`), part des IDE (`docid=273`) | 2007-09-15 | `dgpv_old_par_secteur_wb20070915.html`, `dgpv_old_part_ide_wb20070915.html` | non exploitées ici |
| Recueil, statistiques générales (`fr/directdoc.asp?docid=249`) | 2007-09-15 21:09:59 | `dgpv_old_recueil_stats_generales_wb20070915.html` | 120 entreprises, 5 105 514,46 mD ; tourisme 30 entreprises, 158 499 mD |
| Recueil, pages FR par secteur (`directdoc.asp?docid=296` à `303`) | 2007-09-15 | `dgpv_old_recueil_<secteur>_wb20070915.html` (8 fichiers) | agriculture à cuir et textiles ; les pages FR tourisme, commerce, transport, services ne sont pas capturées |
| Recueil, pages AR tourisme, commerce, pêche (`ar/directdoc.asp?docid=282`, `283`, `273`) | 2007-09-15 | `dgpv_old_recueil_ar_tourisme_artisanat_wb20070915.html`, `…_ar_commerce_…`, `…_ar_peche_…` | version arabe des pages du recueil, encodage cp1256 |
| FAQ (`fr/doc.asp?mcat=1&mrub=61`) | 2009-06-25 09:48:41 | `dgpv_old_faq_wb20090625.html` | Question n° 2 : moment où une opération entre dans les statistiques |

### 2.3 Pages du site actuel (`privatisation.pm.gov.tn`)

| Page | Capture ou consultation | Fichier `AW/` |
|---|---|---|
| Opérations réalisées en 2005, 2006, 2007, 2008 | captures 2026-07-13 (12:13:31, 11:57:03, 11:50:33, 13:15:48) | `dgpv_operations_realisees_<année>_wb<horodatage>.html` |
| Opérations réalisées en 2008 | consultation directe, 2026-10-27 | `dgpv_operations_realisees_2008_2026-10-27.html` |
| Répartition par mode ; par secteur ; part des IDE | consultation directe, 2026-10-27 (les captures du 2026-04-11 sont des pages captcha, supprimées) | `dgpv_repartition_par_mode_2026-10-27.html`, `dgpv_repartition_par_secteur_2026-10-27.html`, `dgpv_part_ide_2026-10-27.html` |
| Série temporelle des recettes (fiche du classeur) | 2026-04-11 03:58:26 | `dgpv_serie_temporelle_recettes_wb20260411.html` (« Date d'insertion : 28 février 2009 ») |
| Bilan global ; statistiques ; statistiques agrégées ; données ; index du recueil ; synthèse | captures 2025-05-19/20 | `dgpv_bilan_global_wb20250520.html`, etc. Le bilan donne les mêmes chiffres que la copie du 11/10/2026 (fichiers non identiques octet à octet). |
| Enquête nationale sur les entreprises privatisées (PDF arabe, 16 p., août 2008) | 2024-06-27 17:56:57 | `dgpv_enquete_entreprises_privatisees_wb20240627.pdf` et sa fiche `dgpv_article_enquete_wb20250425.html` — 138 entreprises privatisées 1986-2004, 93 répondantes ; sans rapport avec les écarts |

La page « par mode » actuelle donne, au 31/01/2009 : vente d'actions 99 entreprises, 4 698 MD
(bloc 86 / 4 588 ; bloc + OPV 3 / 27 ; OPV 10 / 83) ; augmentation de capital 1 / 132 ;
vente d'éléments d'actif 112 / 427 ; **concession 5 / 706** ; total 217 / 5 963.

### 2.4 Manifeste complet

Copie de `AW/MANIFEST.tsv` (hors git).

| Fichier | Capture | URL d'origine | URL de capture | Octets | sha256 |
|---|---|---|---|---:|---|
| `dgpv_recueil_op_privatisation_ar_wb20120907.pdf` | 20120907033523 | `http://www.privatisation.gov.tn:80/www/en/download/recueil_op_privatisation_ar.pdf` | `https://web.archive.org/web/20120907033523id_/http://www.privatisation.gov.tn:80/www/en/download/recueil_op_privatisation_ar.pdf` | 321729 | `57dc4af9b0a60eb622da30ac7016b1ccb5835426301da476b4c6c39012f35b29` |
| `dgpv_top_cession_2003-12-31_wb20080920.xls` | 20080920215100 | `http://www.privatisation.gov.tn:80/www/en/download/top_cession_20003-12-31.xls` | `https://web.archive.org/web/20080920215100id_/http://www.privatisation.gov.tn:80/www/en/download/top_cession_20003-12-31.xls` | 189440 | `0562a14089aca4c078ab1c1a279835378e4ef0457bcf98a65126eeab90d6eb9f` |
| `dgpv_recettes_annuelles_1987-2008_fr_wb20260118.xls` | 20260118140858 | `https://privatisation.pm.gov.tn/sites/default/files/2022-04/recettes-annuelles-1987-2008-fr.xls` | `https://web.archive.org/web/20260118140858id_/https://privatisation.pm.gov.tn/sites/default/files/2022-04/recettes-annuelles-1987-2008-fr.xls` | 26624 | `4ddb80a38546053ce589679e446fcf96f91c45953a240cf80b3df087d0b022cf` |
| `dgpv_enquete_entreprises_privatisees_wb20240627.pdf` | 20240627175657 | `http://privatisation.pm.gov.tn/sites/default/files/2022-04/Enqu%C3%AAte%20VF%20internet.pdf` | `https://web.archive.org/web/20240627175657id_/http://privatisation.pm.gov.tn/sites/default/files/2022-04/Enqu%C3%AAte%20VF%20internet.pdf` | 533900 | `366f7bbcba19874835123abe59e2d977dfeaa6c72e8932c25df9a87b98b73c03` |
| `dgpv_old_bilan_global_2006-10-31_wb20070108.html` | 20070108191759 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=49&msrub=8&dev=true` | `https://web.archive.org/web/20070108191759id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=49&msrub=8&dev=true` | 22319 | `b13d143b0c82705f20c9deeb302055ffcdfc9da441eac59b6efa411b97f8cc1d` |
| `dgpv_old_recueil_index_wb20070108.html` | 20070108191747 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=49&msrub=7&dev=true` | `https://web.archive.org/web/20070108191747id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=49&msrub=7&dev=true` | 22991 | `b0fc4212fe4e1d915756ae0e03f436f51f370d79f11cf2f932b73c2aa1d7b1ef` |
| `dgpv_old_stats_agregees_wb20070106.html` | 20070106133737 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=49&msrub=20&dev=true` | `https://web.archive.org/web/20070106133737id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=49&msrub=20&dev=true` | 20881 | `fc12147817f808fbd39ff3c3bb1574ef5fb6d11a85cc3862268236d8b1528020` |
| `dgpv_old_par_periode_wb20070915.html` | 20070915210915 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=270&mcat=1&mrub=49&msrub=20` | `https://web.archive.org/web/20070915210915id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=270&mcat=1&mrub=49&msrub=20` | 27152 | `6b8026873075b15522923db0217f043367b58698192e44c9f22157198fd48b7e` |
| `dgpv_old_par_mode_wb20070915.html` | 20070915211129 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=271&mcat=1&mrub=49&msrub=20` | `https://web.archive.org/web/20070915211129id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=271&mcat=1&mrub=49&msrub=20` | 26617 | `24f66270cfc797d1cd830ed5762c885618a28242d6ab857ac147397961a0de7f` |
| `dgpv_old_par_secteur_wb20070915.html` | 20070915184345 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=272&mcat=1&mrub=49&msrub=20` | `https://web.archive.org/web/20070915184345id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=272&mcat=1&mrub=49&msrub=20` | 30965 | `198371697511136c96b83c439274ad9de2485afe16aa262f85619ac7694f022e` |
| `dgpv_old_part_ide_wb20070915.html` | 20070915184150 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=273&mcat=1&mrub=49&msrub=20` | `https://web.archive.org/web/20070915184150id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?docid=273&mcat=1&mrub=49&msrub=20` | 27745 | `2d88ae4581d1894e4f142255980f580f284e27214a8799c826366b0e3aa0344d` |
| `dgpv_old_recueil_stats_generales_wb20070915.html` | 20070915210959 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=249` | `https://web.archive.org/web/20070915210959id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=249` | 31803 | `e72e024943701b0afce0af71ab08c68c7d54d3a0d1edfcdbfd1d6d11cf46f76c` |
| `dgpv_old_faq_wb20090625.html` | 20090625094841 | `http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=61` | `https://web.archive.org/web/20090625094841id_/http://www.privatisation.gov.tn:80/www/fr/doc.asp?mcat=1&mrub=61` | 22159 | `7e9de95e380b4a1dadcea528dc84abecc6d82353e03b8993134ab40814d23378` |
| `dgpv_old_recueil_agriculture_wb20070915.html` | 20070915210937 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=296` | `https://web.archive.org/web/20070915210937id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=296` | 36794 | `1408b297d472db6e63dcafa5d6be750794f25d863bb69dda402874ffd4bda06f` |
| `dgpv_old_recueil_peche_wb20070915.html` | 20070915184408 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=297` | `https://web.archive.org/web/20070915184408id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=297` | 27837 | `80675f47f45ffce5f9f6e98e82d315e75398247d04539c8a02439859c1f34847` |
| `dgpv_old_recueil_services_agricoles_wb20070915.html` | 20070915184418 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=298` | `https://web.archive.org/web/20070915184418id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=298` | 26648 | `2d583b4efcc28468df6ef15b97cc815f1e2925c2cd80d29faff010b7de2c3165` |
| `dgpv_old_recueil_agroalimentaire_wb20070915.html` | 20070915184423 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=299` | `https://web.archive.org/web/20070915184423id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=299` | 30113 | `e3aaf1182df8d2217c01c32469b98afbf9b8205fc9d1839f2126c663a7e19dc2` |
| `dgpv_old_recueil_imccv_wb20070915.html` | 20070915184245 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=300` | `https://web.archive.org/web/20070915184245id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=300` | 35979 | `00bd044ec07694f5141e8cbce1c6fc2abf11cb932beda24582dffa03d3e0b1e9` |
| `dgpv_old_recueil_ime_wb20070915.html` | 20070915184350 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=301` | `https://web.archive.org/web/20070915184350id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=301` | 35930 | `7bb0fd11396594ae491eacb61401d121038f191301a1497905ce347b5d7005e1` |
| `dgpv_old_recueil_chimie_wb20070915.html` | 20070915184227 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=302` | `https://web.archive.org/web/20070915184227id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=302` | 26751 | `b589f2d8192d560f83d1ba103c561e73bab3b7d8a5f5fe3d103acc2b579243b6` |
| `dgpv_old_recueil_cuir_textiles_wb20070915.html` | 20070915184304 | `http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=303` | `https://web.archive.org/web/20070915184304id_/http://www.privatisation.gov.tn:80/www/fr/directdoc.asp?docid=303` | 28607 | `804163a444f694290702b0c15943f788091152ccf2fabf70195ba8cdb9d0bc5b` |
| `dgpv_old_recueil_ar_tourisme_artisanat_wb20070915.html` | 20070915184259 | `http://www.privatisation.gov.tn:80/www/ar/directdoc.asp?docid=282` | `https://web.archive.org/web/20070915184259id_/http://www.privatisation.gov.tn:80/www/ar/directdoc.asp?docid=282` | 35383 | `b5e03c6a55d194f3e440d0c0f9e2a5854b3963cb592e1b76481ad31318f9d24c` |
| `dgpv_old_recueil_ar_commerce_wb20070915.html` | 20070915210926 | `http://www.privatisation.gov.tn:80/www/ar/directdoc.asp?docid=283` | `https://web.archive.org/web/20070915210926id_/http://www.privatisation.gov.tn:80/www/ar/directdoc.asp?docid=283` | 26876 | `202b99677c3a849d3be864b3707b5f4ce76b3a7ce00e9ec12126a9cd6e415451` |
| `dgpv_old_recueil_ar_peche_wb20070915.html` | 20070915211124 | `http://www.privatisation.gov.tn:80/www/ar/directdoc.asp?docid=273` | `https://web.archive.org/web/20070915211124id_/http://www.privatisation.gov.tn:80/www/ar/directdoc.asp?docid=273` | 25235 | `94a2e9169572c9dc141cde17ab2ed7a5ee57ec1af3cbba4c47792e83cdb1177a` |
| `dgpv_operations_realisees_2005_wb20260713121331.html` | 20260713121331 | `https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2005` | `https://web.archive.org/web/20260713121331id_/https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2005` | 69815 | `6ea4af222504a08eded6750167d856811bd7e647149f5a49d7adc96d8583ce1b` |
| `dgpv_operations_realisees_2006_wb20260713115703.html` | 20260713115703 | `https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2006` | `https://web.archive.org/web/20260713115703id_/https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2006` | 69424 | `c43dac394df57591b3ac8794783c65eb56de30d34109541dccbfdb6505ce2462` |
| `dgpv_operations_realisees_2007_wb20260713115033.html` | 20260713115033 | `https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2007` | `https://web.archive.org/web/20260713115033id_/https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2007` | 69660 | `1710272ab716aa6a53c3822a34dc85267bb95540b40c4890376eb8c9bc5000c5` |
| `dgpv_operations_realisees_2008_wb20260713131548.html` | 20260713131548 | `https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2008` | `https://web.archive.org/web/20260713131548id_/https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2008` | 69627 | `7133e5bcb316f2aab41dcac151d29789948d3afcf200c7a418fdb8217f0190d3` |
| `dgpv_serie_temporelle_recettes_wb20260411.html` | 20260411035826 | `https://privatisation.pm.gov.tn/fr/article/serie-temporelle-des-recettes-des-privatisation-et-des-restructurations` | `https://web.archive.org/web/20260411035826id_/https://privatisation.pm.gov.tn/fr/article/serie-temporelle-des-recettes-des-privatisation-et-des-restructurations` | 74441 | `7ae7f4d4b5fc9348e347f1a1fcf4351b37baa9ecddef3b0e126d2ca635ccd63b` |
| `dgpv_statistiques_agregees_wb20250520.html` | 20250520002236 | `https://privatisation.pm.gov.tn/fr/statistiques-agregees` | `https://web.archive.org/web/20250520002236id_/https://privatisation.pm.gov.tn/fr/statistiques-agregees` | 63869 | `c0f8f672cfc5d830bd958343b6b94556192a0cc3b6f5763aee6ffc59674dbab8` |
| `dgpv_donnees_wb20250519.html` | 20250519232653 | `https://privatisation.pm.gov.tn/fr/donnees` | `https://web.archive.org/web/20250519232653id_/https://privatisation.pm.gov.tn/fr/donnees` | 63159 | `7bdf955c7256057be6a9257eddc7d78e1e183df185de168284abb7d1384129a8` |
| `dgpv_statistiques_wb20250519.html` | 20250519233915 | `https://privatisation.pm.gov.tn/fr/statistiques` | `https://web.archive.org/web/20250519233915id_/https://privatisation.pm.gov.tn/fr/statistiques` | 64055 | `e4cbe659e0a3edb92251a31b54485a3cf9aae10cc3f6e00e38f7284f397c167b` |
| `dgpv_bilan_global_wb20250520.html` | 20250520011519 | `https://privatisation.pm.gov.tn/fr/bilan-global-des-privatisations` | `https://web.archive.org/web/20250520011519id_/https://privatisation.pm.gov.tn/fr/bilan-global-des-privatisations` | 63442 | `17d8e9495695a00ead810d1b343ba430a42a1d24e644e0a0fabdd1e5c2f1b18e` |
| `dgpv_recueil_index_wb20250520.html` | 20250520004545 | `https://privatisation.pm.gov.tn/fr/recueil-des-operations-depuis-1998` | `https://web.archive.org/web/20250520004545id_/https://privatisation.pm.gov.tn/fr/recueil-des-operations-depuis-1998` | 64342 | `f1dd5a743213f768bb92d6f8ab759572650dafa1e9e8aa7e1ac73004179f6d17` |
| `dgpv_synthese_processus_wb20250519.html` | 20250519235718 | `https://privatisation.pm.gov.tn/fr/synthese-du-processus-de-privatisation` | `https://web.archive.org/web/20250519235718id_/https://privatisation.pm.gov.tn/fr/synthese-du-processus-de-privatisation` | 62291 | `6b523c02de113ecdb9ab74439c3f4aa8e178ce69ff4c6d1fe64b209b6e05f3de` |
| `dgpv_article_enquete_wb20250425.html` | 20250425214549 | `https://privatisation.pm.gov.tn/fr/article/resultats-de-lenquete-nationale-relative-aux-entreprises-et-unites-privatisees` | `https://web.archive.org/web/20250425214549id_/https://privatisation.pm.gov.tn/fr/article/resultats-de-lenquete-nationale-relative-aux-entreprises-et-unites-privatisees` | 68838 | `8ec259179bd9245612e4af87002f7f775d5119afdbfaaa1f911ea1474ebc34a4` |
| `dgpv_operations_realisees_2008_2026-10-27.html` | 2026-10-27 | `https://privatisation.pm.gov.tn/fr/operations-de-privatisation-realisees-en-2008` | (consultation directe 2026-10-27) | 69627 | `2629ac0d7c0a3c23b0c7e14b3edca5b6944f5f4fac93e8d94d195751f9031503` |
| `dgpv_repartition_par_mode_2026-10-27.html` | 2026-10-27 | `https://privatisation.pm.gov.tn/fr/repartition-du-produit-recettes-des-privatisations-et-restructurations-par-mode` | (consultation directe 2026-10-27) | 73035 | `4136860135550ab54bd56180204b61b981a43207e57af1243b0702e1c6028ea4` |
| `dgpv_repartition_par_secteur_2026-10-27.html` | 2026-10-27 | `https://privatisation.pm.gov.tn/fr/repartition-des-recettes-des-privatisations-et-restructurations-par-secteur-dactivite` | (consultation directe 2026-10-27) | 76191 | `ab1a22e8a45c5f5503e7df21bfc546a6445f8b35997ce6fcca5b20a1c06f4ff6` |
| `dgpv_part_ide_2026-10-27.html` | 2026-10-27 | `https://privatisation.pm.gov.tn/fr/part-des-investissements-etrangers-dans-les-recettes-de-privatisations-et-restructurations-repartis` | (consultation directe 2026-10-27) | 72848 | `d7688e40f9117057f0ffd3a98767c79781975ebdd00df4b587bb41866cff4c73` |
| `dgpv_ar_operations_reussies_cjo_wb20100508.pdf` | 20100508062315 | `http://www.privatisation.gov.tn:80/www/ar/download/operations_reussies/cjo.pdf` | `https://web.archive.org/web/20100508062315id_/http://www.privatisation.gov.tn:80/www/ar/download/operations_reussies/cjo.pdf` | 796722 | `cde9b0a2cdd56a90115b532f4d3447bb484312c296fe3f365edac3566b0563f7` |

### 2.5 Fichiers de travail

`AW/travail/parse_ar.py` (lecture du PDF arabe après `pdftotext -layout` et normalisation NFKC),
`AW/travail/ops_ar.csv` (427 lignes : entreprise, acquéreur, mode, année, montant, objet),
`AW/travail/cmp.py` (comparaison par entreprise et par année avec le recueil HTML). Contrôles :
somme des 427 lignes = 5 976 381 mD (imprimé 5 976 376 ; trois en-têtes diffèrent de 1 mD de la
somme de leurs lignes) ; chaque en-tête d'entreprise et chaque total de secteur retrouve la somme
de ses lignes.

## 3. Le recueil arabe de 2009 est le détail du classeur annuel

Sommes par année des 427 opérations du PDF arabe, comparées au classeur de 2010
(`privatisation_recettes_annuelles_1987_2009.csv`) :

| Année | PDF arabe (mD) | Classeur 2010 (MD) |
|---|---:|---:|
| 1998 | 456 650 | 456,650 |
| 1999 | 43 496 | 43,495 |
| 2003 | 35 469 | 35,469 |
| 2006 | 3 110 481 | 3 110,480 |
| 2007 | 135 571 | 135,569 |
| 2008 | 302 562 | 302,562 |
| 2009 | 12 142 (STIA seule) | 12,142 |

Les années 1986-1997 concordent aussi (le PDF date de 1986 les 6 772 mD que le classeur range en 1987).
Opérations par Plan dans le PDF : 68, 83, 170, 85 pour les VIIe à Xe Plans, soit exactement les
nombres de la page « par période » actuelle. Le PDF arabe est donc la liste d'opérations dont
le classeur annuel et la page « par période » sont les agrégats.

Le bilan global (31/01/2009 : 217 entreprises, 5 963 MD) correspond au classeur de mars 2009
(5 963 214,2 mD), pas à celui de 2010. Les deux diffèrent de 13 162 mD = STIA 2009 (12 142) +
EDIM 2008 (1 020, absente du classeur de mars 2009 : 2008 = 301 542,2 contre 302 562,2). Les
219 en-têtes d'entreprise du PDF, moins STIA et EDIM, donnent 217 ; par secteur, les effectifs
de la page « par secteur » se retrouvent (industries mécaniques et électriques 20 − STIA = 19 ;
autres services 3 + 13 − EDIM = 15 ; tourisme 51 ; pêche 3, dont « LAC NORD »).

## 4. Écarts annuels du recueil HTML, expliqués opération par opération

Comparaison par entreprise et par année entre le PDF arabe et les lignes à une seule année du
recueil HTML (`cmp.py`). Valeurs en milliers de dinars.

### 1998 : −33 530

Le recueil HTML se déclarait, en janvier 2007, « depuis le 01/10/1998 »
(`dgpv_old_recueil_index_wb20070108.html`). Quinze entreprises ont des opérations datées de 1998
dans le PDF arabe et aucune ligne 1998 dans le recueil HTML : SOTETEL 7 304, SIAME 6 700,
SAROST 5 000, CTN 3 000, ONP 2 995, ETHIMAR 2 036, SOPART 1 860 (2 030 au PDF contre 170 au
recueil), Palais arabe 1 500, STM 1 157, GRAFOUPAST 800, SOTACER 588, Bâtiment 300, IRSIT 250,
SHTT 30, SOCOMENA 10. Somme : 33 530, l'écart exact. Le PDF ne donne pas le mois : que ces
opérations soient toutes antérieures au 1er octobre 1998 est cohérent avec la borne déclarée,
mais n'est pas vérifié opération par opération. Vérification partielle dans l'autre sens : la
fiche « opérations réussies » de la Société Ciment Jebel Ouest
(`dgpv_ar_operations_reussies_cjo_wb20100508.pdf`, p. 1) date sa privatisation du
**16 octobre 1998**, et la CJO (241 330 mD) figure bien parmi les lignes 1998 du recueil HTML.

### 1999 : +19 588

| Poste | mD |
|---|---:|
| Freeshop, concession : 1999 au recueil HTML, 1997 au PDF | +24 744 |
| ONP, concessions de Bibane (410) et d'Ichkel (210) : 1999 au recueil, 1998 au PDF | +620 |
| SONAM : 1999 au PDF, ligne pluriannuelle « 1999-2000-2001 » au recueil | −3 176 |
| Bâtiment : idem, ligne « 1999 ; 2000 ; 2004 » | −1 772 |
| El Anabib : idem, ligne « 1999-2000 » | −827 |
| arrondi SORETRAP | −1 |
| **Total** | **+19 588** |

Les dates du recueil HTML pour Freeshop et pour Bibane et Ichkel reprennent des **doublons** des
anciennes éditions : le classeur « top cession » (2005) porte Freeshop trois fois (1997, 1998,
1999, 24 744 chaque fois) et Bibane et Ichkel deux fois (1998 et 1999) ; sa somme 1998
(481 394) et 1999 (68 859,2) est celle du classeur 1987-2005 de 2006. La feuille « Feuil5 » du
classeur de mars 2009 range en concession 24 744 (1997), 25 364 (1998), 25 483 (1999), soit
756 293 mD au total, et la page « par mode » de septembre 2007 imprime 756 MD de concessions.
Les doublons ont été retirés entre septembre 2007 et mars 2009 : la feuille « Recettes fr » du
classeur enregistré le 10/03/2009 porte déjà 1998 = 456 650 et 1999 = 43 495,2 (1998 :
481 394 − 456 650 = 24 744 ; 1999 : 68 859 − 43 495 ≈ 25 364), alors que la page « par mode »
du 15/09/2007 imprime encore 756 MD ; la page actuelle imprime 706 MD. La feuille « Feuil5 » du
même classeur de mars 2009 est un reste non mis à jour. C'est la révision de 1998 et 1999
entre les classeurs 2006 et 2010 déjà signalée dans le catalogue. Le recueil HTML garde une
seule occurrence, datée de 1999.

### 2008 : −148 639

Cinq opérations de 2008 du PDF arabe manquent au recueil HTML : STAR, augmentation de capital
de 35 % au profit de Groupama, 132 000 ; Sousse Center (hôtel Boujaafar), bloc de 99,93 %,
12 597 ; CST, usine de betterave à sucre, 2 200 ; EDIM, 99,874 % du capital, 1 020 ; Mateur
Jalta (MAJAL), ferme 3, 822. Somme : 148 639, l'écart exact. La page « Opérations de
privatisation réalisées en 2008 » du même site cite STAR, Sousse Center, Mateur Jalta 3 et CST
(sans montants) ; elle ne cite pas EDIM.

### 2000-2007

| Année | Écart | Composition |
|---|---:|---|
| 2000 | −2 332 | Bâtiment 1 360, SONAM 942, El Anabib 30 dans des lignes pluriannuelles |
| 2001 | −321 | SONAM 614 (pluriannuelle) ; TOFCO : 422 en 2001 au recueil, 129 en 2001 et 293 en 2002 au PDF (+293) |
| 2002 | −1 518 | ONH 1 225 (ligne « 2002-2003-2004 ») ; TOFCO 293 |
| 2003 | −3 123 | ONH (pluriannuelle) |
| 2004 | +68 | SMVDA Sidi Mansour : troisième ligne de 129 au recueil, absente du PDF (+129) ; ONH 55 et Bâtiment 6 (pluriannuelles) |
| 2005 | 0 | — |
| 2006 | −4 427 | BH, 4 027 : 2006 au PDF, 2007 au recueil ; Tunisie Télécom 3 052 400 au PDF contre 3 052 000 au recueil (−400) |
| 2007 | +3 224 | BH +4 027 ; SODASS, ferme Sidi Saâd 1, 799, absente du recueil ; arrondis −4 |

## 5. Concessions : 6 noms contre 5 entreprises

Le PDF arabe compte, comme le recueil HTML, neuf opérations de concession sous six en-têtes :
LAC NORD (101, 2003, cédant « الدولة », l'État), ONP (4 lots, 739, 1998-1999), SOCOMENA (100,
2004), PARK LA SOUKRA (60, 2003, cédant « الدولة »), FREE SHOP (24 744, 1997), GSM (680 000,
2002). Somme : 705 744 mD, soit les 706 MD de la page « par mode ».

La page « par mode » range chaque entreprise sous **un seul** mode (99 + 1 + 112 + 5 = 217),
alors que ses montants sont des sommes par opération : les sommes du PDF par mode d'opération
retrouvent la page (actifs 427 106 → 427 MD ; concession 705 744 → 706 ; augmentation de capital
132 000 ; actions et OPV 4 698 369 → 4 698). Dans le PDF, quatre en-têtes n'ont que des
concessions (LAC NORD, PARK LA SOUKRA, FREE SHOP, GSM) et deux mêlent concession et vente
d'actifs : ONP (17 ventes d'actifs, 8 793 mD ; 4 concessions, 739) et SOCOMENA (1 vente
d'actifs, 10 ; 1 concession, 100). Cinq = quatre concessions pures + l'une de ces deux
entreprises. **Laquelle n'est dit nulle part** dans les pages trouvées. Le compte de 5 est
stable depuis le bilan au 31/10/2006, où les six concessions étaient déjà réalisées.

Deux règles de rangement ont été essayées sur les 217 en-têtes (219 moins STIA et EDIM,
opérations jusqu'en 2008, regroupées par en-tête et non par nom), en rangeant OPV et blocs sous
« vente d'actions » :

| Règle | Actifs | Actions | Augmentation de capital | Concession | Page « par mode » |
|---|---:|---:|---:|---:|---|
| Mode de la **première opération** (convention de la page « par période ») | 111 | 102 | 0 | 4 | ne retrouve pas |
| Mode qui porte le **plus gros montant** | 112 | 99 | 1 | 5 | retrouve exactement (112, 99, 1, 5) |

Avec la seconde règle, ONP (8 793 mD d'actifs contre 739 de concessions) va aux ventes
d'actifs et SOCOMENA (100 de concession contre 10 d'actifs) aux concessions ; STAR va à
l'augmentation de capital (132 000 contre 3 000 d'OPV). Les cinq concessions du bilan seraient
donc LAC NORD, PARK LA SOUKRA, FREE SHOP, GSM et SOCOMENA. C'est une **reconstruction
cohérente avec les totaux de la page**, non une règle énoncée par la DGPV.

Le bilan par mode a aussi été reclassé entre le 31/10/2006 et le 31/01/2009 (partielle 40 → 29,
autres 6 → 18) sans note de méthode trouvée.

## 6. Tourisme et artisanat : 3 000 mD non expliqués

- Version actuelle (13/10/2026) : 39 lignes, 222 050,85 ; total imprimé 225 050,85.
- PDF arabe 2009, secteur 10, opérations 1998-2008 : 236 538 ; moins les trois opérations absentes
  du recueil HTML (SHTT 30, SOPART 1 860, Sousse Center 12 597) : 222 051. Le PDF confirme la
  **somme des lignes**, pas le total imprimé.
- Version arabe de la page au 15/09/2007 (`dgpv_old_recueil_ar_tourisme_artisanat_wb20070915.html`) :
  35 lignes, somme 168 917 ; total imprimé « المجموع 30 158499 », soit 10 418 de **moins** que
  les lignes. Les quatre lignes ajoutées ensuite (STC 50 127, SGT 1 529,85, STIL 610, STAD 867 :
  53 133,85) font passer la somme des lignes de 168 917 à 222 050,85 ; le total imprimé, lui, est
  passé de 158 499 à 225 050,85 (+66 551,85). Le total imprimé n'a donc jamais été la somme des
  lignes de la page, ni en 2007 ni aujourd'hui.
- Aucune opération de 3 000 mD ne manque au recueil HTML pour 1998-2008 dans ce secteur. Deux
  opérations du secteur valent 3 000 dans le PDF : Hôtel Kahena (2004, présente dans les lignes) et
  Société Taoufik (1992, hors période). Rien ne permet d'en rattacher une à l'écart.

## 7. Valeurs candidates, avec leur place

| Grandeur | Valeur | Pièce, page |
|---|---|---|
| Opérations 1986-2009, total | 5 976 376 mD, 427 opérations | PDF arabe, p. 27 |
| Arrêté du PDF | 31 décembre 2009 | PDF arabe, pied de chaque page |
| Recettes 1987-2008 | 5 963 214,2 mD ; 2008 = 301 542,2 | classeur 1987-2008, feuille « Recettes fr », ligne 9 |
| Période du recueil HTML (édition 2006) | 01/10/1998 – 31/10/2006 | index du recueil, capture du 08/01/2007 |
| Bilan au 31/10/2006 | 203 entreprises, 5 557 MD, concession 5 | bilan global, capture du 08/01/2007 |
| Par mode au 31/01/2009 | concession 5 entreprises, 706 MD (11,8 %) ; actifs 112, 427 MD ; augmentation de capital 1, 132 MD | page « par mode », consultée le 27/10/2026 |
| Par mode, édition 2007 | concession 5, 756 MD (avec doublons) | page « par mode », capture du 15/09/2007 |
| Concessions par année, feuille non mise à jour (doublons) | 1997 : 24 744 ; 1998 : 25 364 ; 1999 : 25 483 ; 2002 : 680 000 ; 2003 : 702 | classeur 1987-2008, feuille « Feuil5 », lignes 4-8. Le 702 de 2003 n'est pas une concession : il égale la SMVDA Zama Bouzid (439 + 263, vente d'actifs avec location de terres domaniales) ; les concessions de 2003 font 161 (LAC NORD 101, PARK LA SOUKRA 60) et celle de SOCOMENA (2004) manque. La feuille suit son propre classement. |
| Règle d'entrée dans les statistiques | contrat de cession signé (actifs) ; contrat de concession signé ; enregistrement à la BVMT (actions) | FAQ, question n° 2, capture du 25/06/2009 |
| Datation des entreprises par période | date de la première opération | page « par période », note (*), capture du 15/09/2007 |
| Opérations 2008 absentes du recueil HTML | STAR 132 000 ; Sousse Center 12 597 ; CST 2 200 ; EDIM 1 020 ; MAJAL 822 (mD) | PDF arabe, p. 1 (MAJAL), p. 5 (CST), p. 18 (Sousse Center), p. 25 (STAR), p. 26 (EDIM) — pages comptées par sauts de page de `pdftotext`, à vérifier à l'image avant citation |

Les numéros de page du PDF arabe sont comptés par les sauts de page de la sortie
`pdftotext -layout` ; à contrôler sur l'image avant tout versement.

## 8. Ce qui reste ouvert

- Le rangement de SOCOMENA en concession (§ 5) est reconstruit, pas énoncé par la DGPV.
- L'origine des 3 000 mD du total imprimé « tourisme et artisanat ».
- Le mois des opérations de 1998 exclues du recueil HTML (seule la CJO, incluse, est datée : 16/10/1998).
- Pourquoi le recueil HTML n'a pas été mis à jour des cinq opérations de 2008 (le site cite
  quatre d'entre elles sur une autre page).
- La page du recueil « Statistiques générales » actuelle n'affiche plus sa période ; la borne
  haute de l'édition prolongée (après le 31/10/2006) n'est pas connue.

Avant toute demande à l'administration, deux pistes restent à épuiser : une version française
ou anglaise du recueil PDF (absente de la liste CDX de `privatisation.gov.tn`, mais la requête
ciblée sur ces noms n'a pas abouti, l'Internet Archive étant hors service le 27/10/2026 au
soir) ; les pages arabes de 2007 des secteurs transport, services financiers et autres
services, non téléchargées.

## 9. Recherches sans résultat ou incomplètes

| Requête | Date | Résultat |
|---|---|---|
| CDX `privatisation.gov.tn*` (collapse urlkey, limite 2000) | 27/10/2026 | 620 URL ; seuls fichiers téléchargeables : `recueil_op_privatisation_ar.pdf`, `top_cession_20003-12-31.xls`, les deux classeurs déjà catalogués, `operations_reussies/cjo.pdf`, deux avis d'appel d'offres. Pas de version FR/EN du recueil PDF. |
| CDX `privatisation.gov.tn/www/*/download/*` et `…/fr/download*` | 27/10/2026 | réponse vide puis 502 ; non rejoué |
| CDX filtré sur `recueil_op_privatisation_fr.pdf`, `…_en.pdf` | 27/10/2026, 20 h | Internet Archive hors service ; à rejouer |
| CDX `privatisation.pm.gov.tn*` | 27/10/2026 | 442 lignes ; **aucune page du recueil par secteur** capturée (agriculture, tourisme, etc.) ; seuls fichiers : classeur 1987-2008, enquête, guide d'accès à l'information |
| CDX des pages « par mode », « par secteur », « part des IDE », « privatisation de la STIA » | 27/10/2026 | une seule capture chacune (2026-04-11), page captcha |
| Pages FR du recueil 2007, `directdoc.asp?docid=304` à `309` (tourisme, commerce, transport, services) | 27/10/2026 | non capturées |
| CDX `pm.gov.tn/*privatis*`, `privatisation.tn*`, `*.privatisation.gov.tn*` | 27/10/2026 | vide |
| Recherche web « recettes de privatisation » Tunisie 1998 1999 BCT rapport annuel Free shop concession | 27/10/2026 | rien sur les écarts ; un communiqué FMI de juin 1999 (cimenteries 1998, 418 MD) — hors sujet ici |
| Recherche web Cour des comptes, rapport annuel, « Direction générale de la privatisation » recettes | 27/10/2026 | rien |
| `tunisia-data/sources/` : catalogues Cour des comptes, BCT, archives BCT, grep « privat » | 27/10/2026 | 0 entrée |

Non fait : dépouillement des rapports annuels de la BCT 1998-2009 (recettes de privatisation du
Trésor) et des lois de règlement ; ils mesurent un autre périmètre (encaissements du Trésor) et
ne dateraient pas les opérations de la DGPV.

### Fiche proposée pour `docs/recherches.yml` (non versée)

Conforme au schéma de `docs/recherches.yml` : validée par `recherches.erreurs_fiche()` (aucune
erreur). Le schéma exige au moins une requête de corpus JORT ; `plein_texte` y est inscrit pour
une passe future et **n'a pas été joué**. L'ancre `<!-- RECHERCHE … -->` est à poser dans
`_cessions.qmd`, section `#sec-ep-cessions-operations`, si le chapitre garde l'un des deux
constats ouverts.

```yaml
- id: r-ep-privatisation-ecarts-recueil
  objet: pièce de la Direction générale de la privatisation qui donne le total des opérations du tourisme et de l'artisanat (225 050,85 mD au recueil des opérations depuis 1998, 3 000 mD de plus que ses lignes) et le mode retenu au bilan global pour les entreprises mêlant concession et vente d'actifs (ONP, SOCOMENA)
  ou: [precis/fr/entreprises_publiques/_cessions.qmd#sec-ep-cessions-operations]
  requetes:
    plein_texte: [الإدارة العامة للتخصيص, Direction générale de la privatisation]
    depuis: 1998-10-01
  passes:
  - date: 2026-10-27
    role: documentaliste
    sources: [web]
    couverture: >-
      web.archive.org, index CDX de privatisation.gov.tn* (620 URL, collapse urlkey) et de
      privatisation.pm.gov.tn* (442 URL) ; téléchargés : recueil arabe 1986-2009 (capture
      2012-09-07), classeur top cession 2003 (2008-09-20), classeur 1987-2008 (2026-01-18),
      pages statistiques et recueil 2006-2007 de l'ancien site, pages actuelles par mode, par
      secteur et IDE (consultées le 2026-10-27). Lacunes : pages FR du recueil 2007 pour
      tourisme, commerce, transport et services non capturées ; pages AR 2007 transport, services
      financiers et autres services non téléchargées ; requête CDX ciblée sur
      recueil_op_privatisation_fr.pdf et _en.pdf non aboutie (Internet Archive hors service) ;
      rapports annuels BCT et lois de règlement non dépouillés ; plein_texte non joué sur le
      corpus JORT.
    couvert_jusqu_au: 2026-10-27
    resultat: aucun
  a_faire: [rejouer le CDX sur recueil_op_privatisation_fr.pdf et _en.pdf, télécharger ar/directdoc.asp docid 284 à 288 (captures 2007-09-15), jouer plein_texte sur le corpus JORT]
```

## 10. Suites possibles dans `tunisia-data`

- Cataloguer les pièces de `AW/` dans `sources/entreprises-publiques-urls.csv` (URL d'origine,
  URL de capture, taille, sha256) ; corriger la mention « aucune capture aux archives du web »
  du catalogue pour l'index du recueil (capture du 20/05/2025) et pour l'édition 2007 des pages.
- Verser le recueil arabe 2009 comme série par opération (`privatisation-operations-1986-2009`),
  avec contrôles par entreprise, par secteur et au total, et la lecture à l'image des pages
  citées.
- Remplacer, dans `privatisation_recueil_recoupement_annuel.csv`, l'écart brut par sa
  décomposition (§ 4).
