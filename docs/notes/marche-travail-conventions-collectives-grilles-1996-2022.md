# Conventions collectives sectorielles : ce que publient l'UGTT, le ministère et les archives du web — et le trou de 1996-2010

> Note du documentaliste, 8 octobre 2026. Prolonge `docs/notes/marche-travail-conventions-collectives-fond.md`
> (« note de fond »). Aucun dépôt modifié. Fichiers téléchargés : `data/raw/emploi/conventions-collectives-archives/` de `tunisia-data` (hors git) (manifeste
> `manifeste.tsv` : fichier, code HTTP, taille, SHA-256, adresse, date ; version tableau `manifeste.md`).
> Outils de la passe, dans le même dossier : `cdx.sh` (index CDX, avec reprise), `wb.sh` (capture brute
> `id_`), `sig2.py`/`sig3.py` (repérage d'un avenant par les chiffres de ses visas), `verif_wb.txt`
> (horodatage réellement servi par la Wayback Machine pour chaque capture citée).
>
> **Niveaux de preuve** — « image JORT » : chiffre lu sur la page du fascicule arabe du corpus local,
> rendue en image ; « copie » : page du *Journal officiel* reproduite par un tiers (impression PDF des
> pages, pieds de page du journal visibles) ; « tiers » : mise en forme propre au site. Rien n'est de mémoire.

## 0. L'essentiel

1. **Ni l'UGTT ni le ministère des Affaires sociales n'ont publié en ligne les grilles de 1996-2010.**
   Le site de l'UGTT (2000-2011) n'a aucune rubrique de conventions ; depuis 2016 il annonce des avenants
   en brèves, avec parfois la copie de l'arrêté (plastique, 2017). La rubrique `social.gov.tn/conventions`
   signalée par la note de fond est celle des **conventions internationales** (OIT, sécurité sociale
   bilatérale), pas des conventions collectives. Les treize PDF `pdftravail/conventions/NN.pdf` de l'ancien
   site sont des conventions de l'OIT en arabe.
2. **Le trou est pourtant comblé, par une autre voie : le corpus local lui-même.** Les fascicules arabes
   de 1996, 1999, 2002, 2006 et 2009 portent les grilles en image ; on les trouve à peu de frais par la
   signature chiffrée des visas (2006, 2009), par le relevé des pages sans texte (2002) ou par planche
   contact (1996, 1999). **Les neuf avenants manquants sont lus** (textile n° 6 à 10 ; bâtiment n° 6 à 9) :
   § B. Ce sont des lectures du *Journal officiel*, non de l'UGTT.
3. **L'avenant n° 16 du bâtiment (2022) est trouvé** : copie des pages 3709-3714 du JORT n° 132 du
   2 décembre 2022 (édition arabe) sur `paie-tunisie.com` (§ E). La série du bâtiment se prolonge
   jusqu'au 1er janvier 2024.
4. **Concordance** : aucun document de l'UGTT ou du ministère ne porte de grille ; le contrôle n'a donc
   pu porter que sur `paie-tunisie.com`, dont les PDF sont des reproductions du journal — six valeurs
   sur six identiques (§ C). Ses tableaux de références, eux, portent deux erreurs de métadonnées.

## A. Ce qui existe, site par site

### A.1 UGTT — `ugtt.org.tn`

| Période d'archive | Ce qui est publié | Langue, forme | Adresse vérifiée (200 à l'horodatage cité) |
|---|---|---|---|
| 2000-2008, site statique `/html/*.htm` | Histoire, congrès, communiqués ; une page « Octobre 2005 — Augmentations salariales dans la fonction publique » (`/html/accordoct2005fr.htm`, capture `20060505003340`, lue) : accord UGTT-gouvernement du 22 octobre 2005, 3,5 % par an sur 2005-2007, « avec effet rétroactif à partir du 1er mai 2005 pour certains secteurs et à partir du 1er juillet 2005 pour d'autres » ; elle dit en passant que cet accord « survient après les accords conclus entre l'UGTT et le patronat tunisien concernant 43 conventions collectives (sur 51 que compte la Tunisie) » — chiffre de l'UGTT, sans grille. Aucune rubrique de conventions (958 adresses archivées avant 2012, filtre `conv|grille|salair|textile|batiment|…` : 2 lignes, les deux PDF « textile » de 2011) | FR/AR, HTML | index CDX seul |
| 2009-2010, site PHP | Page « Négociations sociales » : **coquille vide** (menu seul, 895 caractères) | FR/AR/EN | `https://web.archive.org/web/20090704162949/http://www.ugtt.org.tn:80/fr/negociations-sociales.php` |
| Février-mars 2011, `/userfiles/file/` | Douze PDF (`textile.pdf`, `textile(1).pdf`, `electr.pdf`, `pt.pdf`, `SNCFT.pdf`, `tr1`…`tr7.pdf`) : **procès-verbaux d'entreprise ou de ministère des 9-14 février 2011**, numérisés (manuscrits pour le textile et l'électronique), insérés dans Word 2007. Vus en première page seulement : `textile` (procès-verbal manuscrit de février 2011 entre une direction et un syndicat d'entreprise, portant sur une hausse de salaire ; lecture du manuscrit incertaine), `textile(1)` (procès-verbal manuscrit d'une société de Sousse avec son syndicat de base), `electr` (papier à en-tête CIPI ACTIA), `pt` (procès-verbal dactylographié du 9 février 2011, Tunisie Télécom), `tr4` (procès-verbal d'accord du ministère du Transport sur le transport terrestre de voyageurs) ; les sept autres non ouverts, même fabrication. Aucune grille, aucun avenant sectoriel | AR, image, sans couche texte | `https://web.archive.org/web/20110304073557/http://www.ugtt.org.tn:80/userfiles/file/textile.pdf` et onze autres (manifeste) |
| 2012, WordPress, catégorie « Conventions collectives » | Brèves : accords ministériels, « signature de l'accord des augmentations des salaires des travailleurs dans les hôtels et les agences de voyages » (30 mars 2012). Pas de texte, pas de grille | FR, HTML | `https://web.archive.org/web/20120423072616/http://www.ugtt.org.tn:80/fr/category/conventions-collectives/` |
| 2016, catégorie « الاتفاقيات المشتركة » (`/category/accords-conjoints/`) | Brèves « صدور الملحق التعديلي عدد N… بالرائد الرسمي » (électricité-électronique n° 7, JORT n° 59 du 19 juillet 2016) | AR, HTML | `https://web.archive.org/web/20160728115151/http://www.ugtt.org.tn:80/category/accords-conjoints/` |
| Site actuel (API WordPress, interrogée le 8 octobre 2026) | La catégorie « accords-conjoints » n'existe plus. Recherche « الملحق التعديلي » : 15 billets, 2016-2025 (électricité 2016, torréfaction 2016, agences de voyages 2016, presse 2016-2017, plastique 2017, « détails de l'accord » du secteur privé du 13 mars 2017, santé privée 2025). Recherche « البناء والأشغال العامة » : 1 billet (15 juin 2016, liste des avenants signés). **Aucun billet sur le textile ou le bâtiment portant une grille.** PDF de la médiathèque : 154, presque tous des numéros du journal *Echaab* (2019-2026) | AR | `https://www.ugtt.org.tn/?rest_route=/wp/v2/posts&search=…` |
| Wayback, PDF du domaine (273 adresses) | 245 numéros d'*Echaab* et documents internes ; deux protocoles de 2012 : `accord-f.pdf` (3 pages, image ; « محضر اتفاق » de décembre 2012, première page vue à basse résolution, sans grille) et `Protocol-daccord-15-08-2012.pdf` (2 pages, image, non lu) | AR/FR | index CDX |

Domaines voisins : `ugtt.tn` — aucune capture (CDX, `matchType=domain`). Sites de fédérations (textile,
bâtiment) : aucun repéré dans les liens des pages lues ; non cherchés autrement.

### A.2 Ministère des Affaires sociales — `social.gov.tn`, `social.tn`

| Période | Ce qui est publié | Adresse vérifiée |
|---|---|---|
| Ancien site TYPO3 (captures 2011-2020), `/fileadmin/user1/doc/pdftravail/` | `conventions/29, 81, 87, 98, 100, 105, 111, 122, 135, 138, 142, 159, 182.pdf` : **conventions de l'OIT** portant ces numéros, en arabe, images CCITT sans couche texte (vues : C29, C81, C87, C100, C138, C182). `convar7.pdf` : convention arabe n° 7 de 1977 (sécurité et santé au travail). `codtrav.pdf` : code du travail (non téléchargé). **`evosmig40.pdf`, `evosmig48.pdf`, `evosmag.pdf`** : tableaux d'évolution du SMIG (régimes de 40 et 48 heures) et du SMAG, une page chacun, créés le 27 avril 2011, couche texte à chiffres arabes-indiens mal ordonnés — **utiles au chapitre du SMIG, pas à celui-ci** ; non exploités | `https://web.archive.org/web/20191112203955/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/100.pdf` ; `…/20171025131630/http://www.social.gov.tn:80/fileadmin/user1/doc/pdftravail/evosmig48.pdf` (les 17 au manifeste) |
| Site actuel Drupal (captures 2022-2025), `/conventions`, `/fr/conventions?service=177|181`, `/conventions?service=173` | Liste de **conventions internationales du travail et de sécurité sociale** (« Convention n° 26 : Modalités de fixation des salaires minima », « C182… », conventions bilatérales). Filtre par secteur du ministère. Aucune convention collective | `https://web.archive.org/web/20230331224554/https://www.social.gov.tn/fr/conventions` ; `…/20251010224027/https://www.social.gov.tn/fr/conventions?service=177` ; `…/20250523105501/https://www.social.gov.tn/fr/conventions?service=181` ; `…/20230925204833/https://www.social.gov.tn/conventions?service=173` |
| `social.tn` (2 733 adresses, 2007-2026) | Même rubrique « conventions » ; conventions sectorielles **de l'assurance maladie** (CNAM, 2008) ; concours, appels d'offres | index CDX |

Annuaires statistiques du ministère présents dans l'index (`annuaire_statistiques_sociales__2011_01.pdf`,
`annuairestatsocial2012.pdf`, `annuaire_2014_version_final.pdf`, `Climat_social_2017…pdf`) : **non
ouverts dans cette passe** — piste pour la couverture conventionnelle et les conflits (famille budgétaire/administrative).

### A.3 Dépôt tiers rencontré : `paie-tunisie.com`

Site privé d'un éditeur de paie. Une page par branche (65 entrées, dont les 54 conventions), en
français : résumé des primes, **tableau « Signature / Arrêté / Agrément / Publication au JORT » de la
convention aux avenants de 2009**, et un lien « Cliquez ici pour charger le document » vers le dernier
avenant — **copie des pages du JORT arabe** (impression PDF, pieds de page du journal, texte en couche
texte, grilles en image). Les liens vers les fascicules de 2006 et 2009 pointent un disque local
(`file://hp-pc/Bibli/CCN/ja0072006.pdf`) : morts. La Wayback Machine a 19 adresses
`paie-tunisie.com/Bibli/CCN/ja*.pdf` (2017), **toutes de faux PDF** (pages d'erreur HTML de 14 ko).
Elle a aussi une cinquantaine de `docs/relatedInfo/arrete2014-…`, `arrete2016-…`, `arrete2017-….pdf`
(captures 2015-2018, non téléchargées) : copies des avenants de 2014 à 2017.

| Branche | Document en ligne (8 octobre 2026, réponse 200) | Contenu |
|---|---|---|
| Bâtiment et travaux publics | `https://paie-tunisie.com/docs/relatedInfo/arrete2022-3802arabe-63.pdf` | avenant n° 16, JORT n° 132/2022 éd. arabe pp. 3709-3714 (§ E) |
| Textile | `https://paie-tunisie.com/docs/relatedInfo/arrete2024-1382arabe-2-59.pdf` | avenant n° 18, JORT n° 49/2024 éd. arabe pp. 3502-3512 |
| Commerce de gros, demi-gros et détail | `…/docs/relatedInfo/arrete2023-714arabe-76.pdf` (non téléchargé) | dernier avenant (2023) |
| Hôtels classés touristiques | `…/docs/relatedInfo/arrete2024-3398arabe-72.pdf` (non téléchargé) | dernier avenant (2024) |
| Mécanique générale et stations de carburant | `…/docs/relatedInfo/arrete2023-1305arabe-58.pdf` (non téléchargé) | dernier avenant (2023) |
| Électricité et électronique | `…/docs/relatedInfo/electricite-electrnonique-29.pdf` (non téléchargé) | non identifié |
| Bonneterie et confection | `…/docs/relatedInfo/arrete2024-1383arabe-35.pdf` (non téléchargé) | dernier avenant (2024) |

Autres dépôts vus dans les résultats de recherche, non instruits : `9anoun.tn` et `diwan.tn` (notices
de l'arrêté du 25 novembre 2022, « 7 pages » selon diwan), `jurisitetunisie.com` (`get_jort.php?fichier=A2022_0001-F2022_132.pdf` :
réponse 200 mais page HTML, pas le PDF), `travailjuripratique.tn/convention/` (349 adresses archivées, non lu),
`chaexpert.com` (récapitulatifs 2022 et 2024).

### A.4 Le corpus local `PDFs-legislation-tunisie/data/conventions_collectives/` et `data/ugtt/`

Le ticket annonce treize branches ; le dossier en contient **six** (constat `ls`, `find`).

| Fichier | D'où il vient | Ce qu'il couvre | Grille datée ? |
|---|---|---|---|
| `index.yaml`, `README.md` (26 mai 2026) | amorce interne ; dit l'extraction IORT bloquée | 6 conventions « référencées », 16 « à découvrir » (dont textile et bâtiment) | non |
| `mecanique_electricite/convention.yaml` | JORT français (`markdown_output/JORT/1993/fr/Jo08993.md`, avenant n° 4) | dates de la convention de 1974 et des avenants n° 1 et 4 | non (« reste à extraire ») |
| `mecanique_electricite/grille_salaires_1974.yaml` | `Jo00275.pdf` pp. 18-19 (JORT n° 2 du 10 janvier 1975), OCR | 16 catégories × 13 échelons, effet 1er juin 1974 | **oui, 1974 ; non relue à l'image** |
| `cafes_bars_restaurants/convention.yaml` | JORT n° 63/1977 (`Jo06377.md`) | 8 catégories, une cinquantaine d'emplois | non |
| `banques/`, `assurances/convention.yaml` | décrets du miroir IORT (`dec_2001_715`…) | références seules | non |
| `transformation_verre_miroiterie/` (2 fichiers) | JORT n° 55/1990 (`Jo05590.md`) | convention de 1985, avenants n° 1 et 2, classifications | non |
| `transformation_plastique/` (convention, chronologie, pages natives, OCR) | **UGTT** : PDF joint au billet n° 3449 du 23 octobre 2017 | chaîne de la convention de 1976 à l'avenant n° 14 (arrêté du 16 octobre 2017, JORT n° 84 du 20 octobre 2017, p. 3591 et suiv.) | texte de l'avenant ; grilles en image (pp. 4-5 du PDF), non extraites |
| `smig_smag.yaml` | miroir IORT (`data/iort/textes/md/`) | décrets du SMIG et du SMAG depuis 2000 | hors sujet |
| `ugtt_accords_salariaux.yaml` | API WordPress de l'UGTT, 128 billets 2017-2026 | 89 « accords » repérés : **pourcentages et années tirés du texte des billets**, surtout d'entreprise | non |
| `ugtt_chronologie.yaml` | idem, 248 billets | 45 billets classés par secteur | non |
| `ugtt_pdfs_index.yaml`, `ugtt_all_pdfs_index.yaml` | idem | 1 PDF téléchargé ; « 130 PDF, 0 lié aux conventions » | — |
| `data/ugtt/pdfs/conventions_collectives/arr_2017_4024_plastique.pdf`, `arrete_2017_4024_plastique.pdf`, `Arrêté2017_4024Arabe-plastique.pdf` | UGTT (`wp-content/uploads`), **trois copies du même fichier** (SHA-256 `13a16bfc6e2902df…`), impression PDF du 23 octobre 2017 | pages du JORT n° 84/2017 (pied « صفحـة 3591 ») | grilles en image |
| `data/ugtt/pdfs/conventions_collectives/arr_2017_4023.pdf` | UGTT | **n'est pas un PDF** : page HTML du site (67 ko) | — |

Conclusion : un seul document du corpus vient réellement de l'UGTT (plastique, 2017), et c'est une
reproduction du journal. Rien sur le textile ni le bâtiment.

## B. Le trou de 1996-2010 : les neuf avenants, lus au *Journal officiel* (édition arabe, corpus local)

Aucun n'est publié par l'UGTT ni par le ministère. Tous sont lus sur les fascicules
`PDFs/JORT/<année>/ar/` du corpus (SHA-256, 16 premiers caractères : `Ja06096.pdf` c1dc3c0dabdd2de8 ;
`Ja04899.pdf` 9fae5db6fdb33b37 ; `Ja0972002.pdf` 40486d02a84c0ec1 ; `Ja0982002.pdf` 87b096cdb7fd7fda ;
`Ja0072006.pdf` 25df9a2949647010 ; `Ja0162009.pdf` 0fa596a093f284ad). Unité : dinars par heure. Les
grilles de 1996 sont imprimées en millimes (« 825 ») ; celles de 1999 et après en dinars.

Chaque grille porte la mention que les salaires comprennent l'indemnité complémentaire provisoire des
décrets n° 81-437 et n° 82-501 : série comparable au SMIG sur toute la période. Régime horaire : non
porté par les grilles horaires (comme dans la note de fond).

### B.1 Textile — catégorie I, échelon 0 (« الترسيم »), agents payés à l'heure

| Avenant | Date d'effet | Bas (I-0) | Haut (IV-2, éch. 0) | Hausse du bas | SMIG 48 h (depuis le) | Bas / SMIG | Source : JORT éd. arabe (page PDF du fascicule) | Lecture |
|---|---|---:|---:|---:|---:|---:|---|---|
| n° 6 | 1er mai 1996 | 0,825 | 1,116 | +4,8 % sur 1995 | 0,770 (1er mai 1996) | 1,07 | n° 60, 26 juill. 1996, p. 1841 (p. 187) | image JORT |
| n° 6 | 1er mai 1997 | 0,863 | 1,179 | +4,6 % | 0,780 (9 sept. 1996) | 1,11 | id., p. 1843 (p. 189) | image JORT |
| n° 6 | 1er mai 1998 | 0,901 | 1,242 | +4,4 % | 0,819 (7 nov. 1997) | 1,10 | id., p. 1845 (p. 191) | image JORT |
| n° 7 | 1er mai 1999 | 0,939 | n. l. | +4,2 % | 0,860 (1er mai 1999) | 1,09 | n° 48, 15 juin 1999, p. 1110 (p. 18) | image JORT |
| n° 7 | 1er mai 2000 | 0,977 | n. l. | +4,0 % | 0,899 (1er mai 2000) | 1,09 | id., p. 1112 (p. 20) | image JORT |
| n° 7 | 1er mai 2001 | 1,015 | n. l. | +3,9 % | 0,899 | 1,13 | id., p. 1114 (p. 22) | image JORT |
| n° 8 | 1er mai 2002 | 1,053 | 1,494 | +3,7 % | 0,940 (1er juill. 2001) | 1,12 | n° 97, 29 nov. 2002, p. 3009 (p. 21) | image JORT |
| n° 8 | 1er mai 2003 | 1,094 | n. l. | +3,9 % | 0,974 (1er juill. 2002) | 1,12 | id., p. 3011 (p. 23) | image JORT |
| n° 8 | 1er mai 2004 | 1,140 | n. l. | +4,2 % | 1,015 (1er juill. 2003) | 1,12 | id., p. 3013 (p. 25) | image JORT |
| n° 9 | **15 juin 2005** | 1,178 | n. l. | +3,3 % | 1,049 (1er juill. 2004) | 1,12 | n° 7, 24 janv. 2006, p. 383 (p. 103) | image JORT |
| n° 9 | 1er mai 2006 | 1,221 | n. l. | +3,7 % | 1,078 (1er sept. 2005) | 1,13 | id., p. 385 (p. 105) | image JORT |
| n° 9 | 1er mai 2007 | 1,264 | n. l. | +3,5 % | 1,112 (1er juill. 2006) | 1,14 | id., p. 387 (p. 107) | image JORT |
| n° 10 | 1er mai 2008 | 1,327 | 1,912 | +5,0 % | 1,153 (1er juill. 2007) | 1,15 | n° 16, 24 févr. 2009, p. 977 (p. 273) | image JORT |
| n° 10 | 1er mai 2009 | 1,390 | 1,998 | +4,7 % | 1,211 (1er juill. 2008) | 1,15 | id., p. 979 (p. 275) | image JORT |
| n° 10 | 1er mai 2010 | 1,460 | 2,093 | +5,0 % | 1,253 (1er août 2009) | 1,17 | id., p. 981 (p. 277) | image JORT |

Raccords : 1995 → 1996, 0,787 → 0,825 ; 2010 → 2011, 1,460 → 1,533 (+5,0 %), lecture de la note de fond.
La progression de 1996 à 2004 est d'un pas presque constant de 38 à 46 millimes par an.
**À contrôler avant citation** : (i) la date du 15 juin 2005 est **confirmée** par un recadrage à 260 points par pouce : « يقع العمل به بداية من 15 جوان 2005 — بصفة استثنائية » (« à titre exceptionnel ») ; la raison de l'exception est à lire dans le texte de l'avenant (pp. 378-382, en image), non lu ; (ii) les numéros de
page de 1996, 1999 et 2002, déduits d'un décalage constant vérifié sur deux pieds de page par fascicule
(1996 : page PDF + 1654 ; 1999 : + 1092 ; n° 97/2002 : + 2988), non lus un à un ; (iii) la sous-catégorie
du « haut » de 1996-1998 : ligne « 2 » de la catégorie IV, lue sur un recadrage où l'en-tête IV n'apparaît
qu'en 1997.

### B.2 Bâtiment et travaux publics — personnel occasionnel (grilles n° 1, 3, 5)

| Avenant | Date d'effet | Manœuvre ordinaire | Chef d'équipe 3e degré | Hausse du bas | SMIG 48 h (depuis le) | Bas / SMIG | Source : JORT éd. arabe (page PDF) | Lecture |
|---|---|---:|---:|---:|---:|---:|---|---|
| n° 6 | 1er mai 1999 | 0,989 | 1,501 | +4,1 % sur 1998 | 0,860 | 1,15 | n° 48, 15 juin 1999, p. 1157 (p. 65) | image JORT |
| n° 6 | 1er mai 2000 | 1,028 | 1,571 | +3,9 % | 0,899 | 1,14 | id., p. 1158 (p. 66) | image JORT |
| n° 6 | 1er mai 2001 | 1,067 | 1,641 | +3,8 % | 0,899 | 1,19 | id., p. 1159 (p. 67) | image JORT |
| n° 7 | 1er mai 2002 | 1,103 | 1,711 | +3,4 % | 0,940 | 1,17 | n° 98, 3 déc. 2002, p. 3091 (p. 39) | image JORT |
| n° 7 | 1er mai 2003 | 1,141 | 1,781 | +3,4 % | 0,974 | 1,17 | id., p. 3092 (p. 40) | image JORT |
| n° 7 | 1er mai 2004 | 1,181 | 1,853 | +3,5 % | 1,015 | 1,16 | id., p. 3093 (p. 41) | image JORT |
| n° 8 | 1er mai 2005 | 1,221 | n. l. | +3,4 % | 1,049 | 1,16 | n° 7, 24 janv. 2006, p. 362 (p. 82) | image JORT |
| n° 8 | 1er mai 2006 | 1,261 | n. l. | +3,3 % | 1,078 | 1,17 | id., p. 363 (p. 83) | image JORT |
| n° 8 | 1er mai 2007 | 1,303 | n. l. | +3,3 % | 1,112 | 1,17 | id., p. 364 (p. 84) | image JORT |
| n° 9 | 1er mai 2008 | 1,371 | 2,221 | +5,2 % | 1,153 | 1,19 | n° 16, 24 févr. 2009, p. 891 (p. 187) | image JORT |
| n° 9 | 1er mai 2009 | 1,439 | 2,365 | +5,0 % | 1,211 | 1,19 | id., p. 892 (p. 188) | image JORT |
| n° 9 | 1er mai 2010 | 1,509 | 2,511 | +4,9 % | 1,253 | 1,20 | id., p. 893 (p. 189) | image JORT |

Raccords : 1998 → 1999, 0,950 → 0,989 ; 2010 → 2011, 1,509 → 1,588 (+5,2 %). Le SMIG et les rapports
sont un calcul de cette note sur `precis/_seriescache/marche-travail-smig-smag.csv` (taux horaire du
régime de 48 heures en vigueur à la date d'effet). De 1999 à 2007 au moins, la grille n° 1 n'a qu'une ligne
« ouvrier hautement qualifié » (six lignes puis trois degrés de chef d'équipe) ; la distinction I/II
est présente dans la grille du 1er mai 2008.

### B.3 Dates d'arrêté qui manquaient à la chaîne du bâtiment (cases « n. r. » de la note de fond)

Lues dans les visas de l'arrêté du 25 novembre 2022 (copie, p. 3709) : avenant n° 6, arrêté du **9 juin
1999** ; n° 7, **25 novembre 2002** ; n° 8, **17 janvier 2006** ; n° 9, **17 février 2009**. Avenant n° 16 :
signé le **27 octobre 2022**.

### B.4 Ce que la période ajoute au constat sur le SMIG

De 1996 à 2010 le rapport du bas de grille au SMIG horaire reste supérieur à 1 et monte lentement :
textile de 1,07 à 1,17, bâtiment de 1,15 à 1,20 ; l'écart entre les deux branches (quatre à six points)
est celui déjà relevé après 2011.

## C. Contrôle de concordance

**UGTT et ministère : sans objet.** Aucun de leurs documents ne porte une grille du textile ou du
bâtiment ; il n'y a rien à comparer.

**`paie-tunisie.com`, textile, avenant n° 18** (copie téléchargée le 8 octobre 2026, impression PDF du
17 avril 2024, 11 pages, pieds de page « الرائد الرسمي… 16 أفريل 2024 — عدد 49 », pp. 3502-3512) contre la
lecture du JORT de la note de fond (§ B.3) :

| Date d'effet | Grandeur | JORT (note de fond) | Copie `paie-tunisie` (page) | Écart |
|---|---|---:|---:|---|
| 1er janv. 2024 | I, éch. 0 | 2,850 | 2,850 (p. 3507) | aucun |
| 1er janv. 2024 | IV-2, éch. 0 | 4,075 | 4,075 | aucun |
| 1er janv. 2025 | I, éch. 0 | 3,035 | 3,035 (p. 3509) | aucun |
| 1er janv. 2025 | IV-2, éch. 0 | 4,340 | 4,340 | aucun |
| 1er janv. 2026 | I, éch. 0 | 3,248 | 3,248 (p. 3511) | aucun |
| 1er janv. 2026 | IV-2, éch. 0 | 4,644 | 4,644 | aucun |

Six sur six. Portée exacte du résultat : la copie **est** la page du journal (même pagination, même
composition), non une ressaisie ; la concordance établit que le site reproduit le journal sans
l'altérer, et confirme au passage les six lectures de la note de fond. La grille mensuelle (595,401 D)
n'a pas été recontrôlée. Sur les dates de 1994-1995, 1996-1998 et 2011-2019, aucun document tiers à
grille n'a été obtenu : pas de comparaison.

**Écarts de métadonnées** dans les tableaux de références de `paie-tunisie.com` (mise en forme du site,
niveau « tiers ») :
- textile, avenant n° 3 : « n° 55 des 28/07 et 03/08/1990 » ; la note de fond a lu le n° 54 des 21-24 août
  1990 à l'image (l'édition arabe cite un n° 55 des 28 et 31 août) ;
- textile, avenant n° 8 : « signature 14/11/2005 » pour un arrêté du 25/11/2002 — coquille (14 novembre 2002) ;
- la sentence arbitrale de 1983 y est appelée « avenant n° 1 ».
Le tableau du bâtiment concorde ligne à ligne avec la chaîne de la note de fond et avec les visas de 2022.

**Contrôle interne des lectures de B** : chaque série se raccorde aux lectures antérieures et
postérieures de la note de fond (1995, 1998, 2011) par des hausses de 3,3 à 5,2 %, sans saut.

## D. Autres branches : ce qui est disponible (sans extraction)

| Branche | UGTT | Ministère | `paie-tunisie.com` | Corpus local (fascicules arabes) |
|---|---|---|---|---|
| Commerce de gros, demi-gros et détail | billet de 2016 (liste) ; rien d'autre | rien | chaîne jusqu'à l'avenant n° 9 (2009) ; copie de l'avenant de 2023 | grille de 1996 repérée au n° 60/1996, p. PDF 204 (p. 1858) ; 1999-2009 à repérer par la même méthode |
| Hôtels classés touristiques | brève du 30 mars 2012 (accord hôtels et agences de voyages) | rien | chaîne jusqu'à l'avenant n° 10 (arrêté du 12 mai 2009, n° 39/2009) ; copie de l'avenant de 2024 | grille de 1996 repérée au n° 60/1996, p. PDF 182 ; avenant de 2009 au n° 39/2009 |
| Mécanique générale et stations de carburant (2000) | rien | rien | chaîne jusqu'à l'avenant n° 3 (arrêté du 21 juillet 2009, n° 60/2009) ; copie de l'avenant de 2023 | `grille_salaires_1974.yaml` (convention d'origine, non relue) ; fascicules à repérer |
| Électricité et électronique (1999) | brèves de 2016 (avenant n° 7, JORT n° 59 du 19 juillet 2016) ; PV d'entreprise de 2011 | rien | chaîne jusqu'à l'avenant n° 3 (arrêté du 1er juin 2009, n° 45/2009) ; un PDF non identifié | fascicules à repérer |

Années couvertes en ligne : la convention et les références de publication de l'origine à 2009 (texte
seul, français, tiers) ; les grilles seulement pour le dernier avenant de chaque branche (copie du
journal), et pour 2014-2017 dans les captures de la Wayback Machine (`docs/relatedInfo/arrete201x-…`).

## E. Bâtiment après 2019 : l'avenant n° 16 est trouvé

**Document lu** : `https://paie-tunisie.com/docs/relatedInfo/arrete2022-3802arabe-63.pdf` (réponse 200 le
8 octobre 2026 ; SHA-256 `fc6fe463685bf688b133285f1096266d2730a9ab2f90d5dc5cdf81dbf11bc7a7` ; 6 pages ;
impression PDF du 5 décembre 2022). Il **reproduit les pages 3709 à 3714 du JORT n° 132 du 2 décembre
2022, édition arabe** (pieds de page du journal sur chaque page) : arrêté (p. 3709), avenant
(pp. 3710-3711), grilles (pp. 3712-3714). Ce n'est pas une mise en forme du site. Niveau « copie » : le
fascicule lui-même reste absent du corpus et de pist.tn.

| Date d'effet | Manœuvre ordinaire | Chef d'équipe 3e degré | Hausse du bas | SMIG 48 h (depuis le) | Bas / SMIG | Page du JORT |
|---|---:|---:|---:|---:|---:|---|
| 1er déc. 2021 (au titre de 2022) | 2,567 | 4,340 | +6,5 % sur le 1er mai 2019 | 2,064 (1er oct. 2020) | 1,24 | p. 3712 (grille n° 1) |
| 1er janv. 2023 | 2,740 | 4,633 | +6,75 % | 2,208 (1er oct. 2022) | 1,24 | p. 3713 (grille n° 3) |
| 1er janv. 2024 | 2,925 | 4,946 | +6,75 % | 2,208 | 1,32 | p. 3714 (grille n° 5) |

Grille mensuelle n° 2 au 1er décembre 2021 : catégorie 1, échelon 1, 523,665 D (p. 3712, lue à
résolution réduite, à contrôler).

Texte (couche texte, p. 3711) : l'avenant, signé le 27 octobre 2022 entre l'UTICA et la Fédération
nationale des entrepreneurs de bâtiment et de travaux publics d'une part, l'UGTT et la Fédération
générale du bâtiment et du bois d'autre part, s'appuie sur le procès-verbal d'accord UGTT-UTICA du
1er janvier 2022 (hausses de 2022, 2023 et 2024). Il fixe aussi — ce qui **lève la réserve de la note
de fond sur la nature des deux indemnités du bâtiment** :
- article 51 nouveau, **indemnité de présence** (منحة الحضور), par mois : 6,894 D au 1er décembre 2021,
  7,359 D au 1er janvier 2023, 7,856 D au 1er janvier 2024 ; elle inclut l'« indemnité de demi-journée »
  du décret du 8 janvier 1948 ;
- article 52 nouveau, **indemnité globale de transport** (المنحة الجملية للنقل), ouvriers permanents,
  occasionnels et temporaires : 79,399 D ; 84,758 D ; 90,479 D aux mêmes dates.
Ces deux séries prolongent, au pas de 6,5 % puis 6,75 %, les couples relevés par la note de fond
(74,553 et 6,473 D au 1er mai 2019) : la plus élevée est bien le transport, l'autre la présence.

Conséquences : la série du bâtiment va désormais de 1996 à 2024 sans trou ; la « dernière grille » au
sens du décret n° 2026-68 est celle du 1er janvier 2024 (2,925 D). Nombre de pages : la notice de diwan.tn annonce sept pages, la copie en a six, consécutives (3709-3714) ; l'écart n'est pas expliqué, mais l'article 2 de l'avenant annonce six grilles (n° 1 à 6) et les trois pages 3712-3714 en portent deux chacune : rien n'indique une page de grille manquante. Second exemplaire indépendant non
obtenu (jurisitetunisie rend une page HTML ; 9anoun et diwan non ouverts). Un avenant n° 17 reste non
repéré (constat de la note de fond, non relancé).

## F. Ce qui n'est pas trouvé, et les requêtes

| Objet | Requête exacte | Couverture | Résultat |
|---|---|---|---|
| Grilles 1996-2010 sur le site de l'UGTT | `web.archive.org/cdx/search/cdx?url=ugtt.org.tn&matchType=domain&filter=mimetype:application/pdf&collapse=urlkey&limit=20000` (273 lignes) ; `…&filter=original:.*(onvention|avenant|grille|salaire|ittifak|accord).*` (16) ; `…&to=20111231` (958) ; `url=ugtt.org.tn/userfiles*` (26). La première forme, `url=ugtt.org.tn*`, a échoué six fois (page « Temporarily Offline ») et a été remplacée par `matchType=domain` | captures de 2000 au 8 octobre 2026 ; PDF de 2012 non lus (2) ; billets non parcourus un à un | aucun |
| Idem, site actuel | `?rest_route=/wp/v2/posts&search=الملحق التعديلي` (15), `…البناء والأشغال العامة` (1), `…الاتفاقية المشتركة القطاعية` (13) ; `/wp/v2/media?mime_type=application/pdf` (154) ; catégories (51) | 8 octobre 2026 ; numéros d'*Echaab* non dépouillés | aucun |
| Grilles sur le site du ministère | `cdx?url=social.gov.tn*&filter=original:.*(onvention|ittifak|grille|salaire|avenant).*` (36) ; `…&filter=mimetype:application/pdf` (880) ; `url=social.gov.tn&matchType=domain&to=20200630&filter=statuscode:200` (1 451) ; `url=social.tn*` (2 733) | 2007-2026 ; annuaires statistiques non ouverts ; pages `index.php?id=` de l'ancien site non lues | aucun (conventions internationales seules) |
| Fascicules de 2006 et 2009 chez un tiers | `cdx?url=paie-tunisie.com&matchType=domain&filter=original:.*\.pdf.*` (271) | 2013-2026 | 19 adresses `Bibli/CCN`, toutes des pages d'erreur |
| Second exemplaire de l'avenant n° 16 du bâtiment | `jurisitetunisie.com/get_jort.php?fichier=A2022_0001-F2022_132.pdf` | 8 octobre 2026, un essai | HTML, pas de PDF |
| Sites de fédérations (textile, bâtiment) | aucune requête propre ; `cdx?url=ugtt.tn&matchType=domain` : 0 | — | non cherché au-delà |
| Haut de grille du textile 1999-2001, 2003-2007 ; du bâtiment 2005-2007 | — | recadrages de cette passe | non lus (les pages sont identifiées : une lecture chacune) |

## Recherches infructueuses — fiches

- **`r-btp-avenant-16-grilles`** (proposée par la note de fond, non versée) : à verser **résolue** pour
  l'avenant n° 16 — `--resultat avenant16-btp-2022` (clé ci-dessous), sources `[jort_cache, corpus_local, pist, web]`,
  couverture : « texte et grilles lus sur la copie de paie-tunisie.com des pp. 3709-3714 du JORT n° 132/2022
  éd. arabe ; fascicule toujours absent du corpus et de pist.tn ; avenant n° 17 non repéré, sommaires
  arabes de 2023-2026 non lus ». Si l'on veut garder ouverte la question de l'avenant n° 17, la scinder.
- **Nouvelle fiche proposée** (seulement ce qui a été fait) :

```yaml
- id: r-conventions-grilles-ugtt-ministere
  objet: publication en ligne, par l'UGTT ou le ministère des Affaires sociales, du texte et des grilles de salaires des conventions collectives sectorielles (1996-2010 en particulier)
  ou: [docs/notes/marche-travail-conventions-collectives-fond.md]
  requetes:
    cdx: ['ugtt.org.tn (matchType=domain, mimetype application/pdf)', 'ugtt.org.tn (matchType=domain, original ~ onvention|avenant|grille|salaire|ittifak|accord)', 'ugtt.org.tn/userfiles*', 'social.gov.tn* (original ~ onvention|ittifak|grille|salaire|avenant)', 'social.gov.tn* (mimetype application/pdf)', 'social.tn*', 'ugtt.tn (matchType=domain)']
    api_wordpress_ugtt: ['search=الملحق التعديلي', 'search=البناء والأشغال العامة', 'search=الاتفاقية المشتركة القطاعية', 'media mime_type=application/pdf']
    depuis: 1996-07-24
  passes:
  - date: 2026-10-08
    role: documentaliste
    sources: [wayback_cdx, ugtt_api, web]
    couverture: 'index CDX des deux domaines jusqu''au 8 octobre 2026 ; pages lues : negociations-sociales.php (2009), catégories de 2012 et 2016, rubrique conventions du ministère (2023-2025), 12 PDF userfiles de 2011, 14 PDF pdftravail ; non lus : numéros du journal Echaab, annuaires statistiques du ministère, pages index.php?id= de l''ancien site du ministère, sites de fédérations'
    couvert_jusqu_au: 2026-10-08
    resultat: aucun
```

## Références candidates

Aucune n'est vérifiée dans `precis/fr/marche_travail/references.json` (à contrôler par le bibliographe).
Adresses pist.tn de l'édition arabe **non vérifiées dans cette passe** (motif `https://www.pist.tn/jort/<année>/<année>A/Ja…pdf`) :
à contrôler avant insertion ; l'intitulé français des arrêtés de 1999-2009 est à reconstituer d'après
les visas, l'édition française ne publiant qu'un avis collectif.

```json
[
 {"id":"avenant6-textile-1996","type":"legislation","title":"Arrêté du ministre des affaires sociales du 24 juillet 1996, portant agrément de l'avenant n° 6 à la convention collective nationale du textile","issued":{"date-parts":[[1996,7,24]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"60","page":"1841-1846","note":"Avenant signé le 23 juillet 1996. Grilles horaires pp. 1841, 1843, 1845 (pages déduites, à contrôler). Pages de l'arrêté non relevées."},
 {"id":"avenant7-textile-1999","type":"legislation","title":"Arrêté du ministre des affaires sociales du 9 juin 1999, portant agrément de l'avenant n° 7 à la convention collective nationale du textile","issued":{"date-parts":[[1999,6,9]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"48","page":"1110-1115","note":"Grilles horaires pp. 1110, 1112, 1114."},
 {"id":"avenant6-btp-1999","type":"legislation","title":"Arrêté du ministre des affaires sociales du 9 juin 1999, portant agrément de l'avenant n° 6 à la convention collective nationale du bâtiment et des travaux publics","issued":{"date-parts":[[1999,6,9]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"48","page":"1157-1159","note":"Avenant signé le 28 mai 1999. Grilles pp. 1157-1159."},
 {"id":"avenant8-textile-2002","type":"legislation","title":"Arrêté du ministre des affaires sociales et de la solidarité du 25 novembre 2002, portant agrément de l'avenant n° 8 à la convention collective nationale du textile","issued":{"date-parts":[[2002,11,25]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"97","page":"3009-3014","note":"Arrêté à la page PDF 15 du fascicule ; grilles horaires pp. 3009, 3011, 3013."},
 {"id":"avenant7-btp-2002","type":"legislation","title":"Arrêté du ministre des affaires sociales et de la solidarité du 25 novembre 2002, portant agrément de l'avenant n° 7 à la convention collective nationale du bâtiment et des travaux publics","issued":{"date-parts":[[2002,11,25]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"98","page":"3091-3093","note":"JORT du 3 décembre 2002. Avenant signé le 14 novembre 2002."},
 {"id":"avenant9-textile-2006","type":"legislation","title":"Arrêté du 17 janvier 2006, portant agrément de l'avenant n° 9 à la convention collective sectorielle du textile","issued":{"date-parts":[[2006,1,17]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"7","page":"377-388","note":"JORT du 24 janvier 2006. Grilles horaires pp. 383, 385, 387."},
 {"id":"avenant8-btp-2006","type":"legislation","title":"Arrêté du 17 janvier 2006, portant agrément de l'avenant n° 8 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2006,1,17]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"7","page":"358-364","note":"Avenant signé le 29 décembre 2005. Grilles pp. 362-364."},
 {"id":"avenant10-textile-2009","type":"legislation","title":"Arrêté du 17 février 2009, portant agrément de l'avenant n° 10 à la convention collective sectorielle du textile","issued":{"date-parts":[[2009,2,17]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"16","page":"973-982","note":"JORT du 24 février 2009. Grilles horaires pp. 977, 979, 981."},
 {"id":"avenant9-btp-2009","type":"legislation","title":"Arrêté du 17 février 2009, portant agrément de l'avenant n° 9 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2009,2,17]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"16","page":"886-893","note":"Avenant signé le 28 janvier 2009. Grilles pp. 891-893."},
 {"id":"avenant16-btp-2022","type":"legislation","title":"Arrêté du ministre des affaires sociales du 25 novembre 2022, portant agrément de l'avenant n° 16 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2022,11,25]]},"container-title":"Journal officiel de la République tunisienne (édition arabe)","issue":"132","page":"3709-3714","note":"JORT du 2 décembre 2022 ; édition française p. 3387 (notice). Avenant signé le 27 octobre 2022. Lu sur la copie https://paie-tunisie.com/docs/relatedInfo/arrete2022-3802arabe-63.pdf (SHA-256 fc6fe463…bc7a7), l'adresse pist.tn répondant 404 : ne pas mettre l'adresse du tiers comme URL principale ; laisser l'URL vide tant que pist.tn ne sert pas le fascicule."}
]
```
`avenant18-textile-2024` : déjà proposé par la note de fond.

## Notions à glossaire (compléments)

| FR | AR | Source | État |
|---|---|---|---|
| indemnité de présence (bâtiment) | منحة الحضور | avenant n° 16, art. 51 nouveau (JORT n° 132/2022, p. 3711) | confirme l'entrée proposée pour le textile |
| indemnité globale de transport | المنحة الجملية للنقل | id., art. 52 nouveau | à ajouter comme variante d'« indemnité de transport » |
| manœuvre ordinaire ; manœuvre spécialisé ; aide-ouvrier | عامل عادي ; عامل مختص ; نصف عامل | grille n° 1 du bâtiment (1999-2022) | à ajouter |
| chef d'équipe | رئيس فريق | id. | à ajouter |
| procès-verbal de séance (accord d'entreprise) | محضر جلسة | PV de février 2011 archivés du site de l'UGTT | utile seulement si le chapitre parle des accords d'entreprise |

## Lacunes et suites

- Verser les séries B.1, B.2 et E dans `tunisia-data` (branche, date d'effet, catégorie, valeur, unité,
  fascicule, page, niveau de lecture) ; ranger les deux copies de `paie-tunisie.com` sous
  `data/raw/conventions/` avec leur ligne de catalogue (adresse, 8 octobre 2026, SHA-256 du manifeste).
- Contrôles à l'image restants : les points (i) à (iii) de B.1 ; les « n. l. » ; la grille mensuelle de 2021.
- La note de fond est à corriger sur trois points : « 1996-2009 : pages entièrement en image, couche
  texte inexploitable » (les chiffres des visas et des pieds de page sortent en clair en 2006 et 2009, ce
  qui suffit à trouver l'avenant) ; le coût « moyen à élevé » du trou (il a tenu en une passe) ; la
  rubrique `social.gov.tn/conventions` (conventions internationales).
- Méthode réutilisable pour les autres branches : `sig2.py <fascicule> <pages> <années des visas>` rend la
  page de l'arrêté en 2006 et 2009 ; les grilles sont les pages sans texte qui suivent. Pour 1996 et
  1999 (scans), une planche contact suffit à repérer les blocs, un recadrage des titres à les nommer.

## Annexe — fichiers téléchargés (`data/raw/emploi/conventions-collectives-archives/` de `tunisia-data` (hors git), à ranger)

Le dossier `data/raw/emploi/conventions-collectives-archives/` de `tunisia-data` (hors git) ne contient plus que ces fichiers et leur manifeste (`manifeste.tsv`, `manifeste.md`) ; le matériel de travail (index CDX, pages de paie-tunisie, réponses de l'API de l'UGTT, images de lecture, scripts, `verif_wb.txt`) est dans `scratchpad/ugtt-travail/`. Collecte : 8 octobre 2026. Chaque adresse de la Wayback Machine a répondu 200 **à l'horodatage cité** (contrôle `verif_wb.txt` : horodatage servi = horodatage demandé, 36 sur 36 ; les trois fichiers ajoutés ensuite — `ugtt_2006_accordoct2005fr.html`, `ugtt_2012_*.pdf` — ont répondu 200 sans ce second contrôle). Les pages HTML sont la capture brute (`id_`).

| Fichier | HTTP | Octets | SHA-256 | Adresse |
|---|---|---:|---|---|
| `ugtt_2011_textile.pdf` | 200 | 863205 | `d7d40b1312652297b2859f8dcbbf79828addbcc26a07b64f6b5eda16922defb9` | https://web.archive.org/web/20110304073557/http://www.ugtt.org.tn:80/userfiles/file/textile.pdf |
| `ugtt_2011_textile_1.pdf` | 200 | 839763 | `cfa06bd981b32409a44e22a1f1ebb6367be1916291025152e1d592c14c78ffbf` | https://web.archive.org/web/20110302022020/http://www.ugtt.org.tn:80/userfiles/file/textile(1).pdf |
| `ugtt_2011_electr.pdf` | 200 | 617112 | `96cf6d339c9888d2297221a78fc55e04f13fa449c3c6d9dbebeb155b1ca4db1c` | https://web.archive.org/web/20110304073457/http://www.ugtt.org.tn:80/userfiles/file/electr.pdf |
| `ugtt_2011_pt.pdf` | 200 | 831836 | `a6286b3f9247908a2085271792282c51d3cf5ad7a15ef906282bf5ffa03750e5` | https://web.archive.org/web/20110302021328/http://www.ugtt.org.tn:80/userfiles/file/pt.pdf |
| `ugtt_2011_SNCFT.pdf` | 200 | 234930 | `9cfcb35825d65504a6d0334547a9d66c331217da16819bdbc410134d82ee9c60` | https://web.archive.org/web/20110304014917/http://www.ugtt.org.tn:80/userfiles/file/SNCFT.pdf |
| `ugtt_2011_tr1.pdf` | 200 | 303843 | `b31112ea8ec48d7b67cb951d838e4ffef5e847f0daf4704e61f55efbe0942a9e` | https://web.archive.org/web/20110302022026/http://www.ugtt.org.tn:80/userfiles/file/tr1.pdf |
| `ugtt_2011_tr2.pdf` | 200 | 869338 | `90baf91a72aec94b916849ba2afa49bb604ed00a204483b87ccf00bf1abc377a` | https://web.archive.org/web/20110302022029/http://www.ugtt.org.tn:80/userfiles/file/tr2.pdf |
| `ugtt_2011_tr3.pdf` | 200 | 281496 | `9bdafa278bf1791315344073c8a88e1b2c28bf4b588cf7494e7bd6f1394f504b` | https://web.archive.org/web/20110302021335/http://www.ugtt.org.tn:80/userfiles/file/tr3.pdf |
| `ugtt_2011_tr4.pdf` | 200 | 987814 | `664a6a14744aa07338e0c18508e1f9f374c55b3c5eca1a336c4cc83604229597` | https://web.archive.org/web/20110302022037/http://www.ugtt.org.tn:80/userfiles/file/tr4.pdf |
| `ugtt_2011_tr5.pdf` | 200 | 721064 | `559784b20a365be1693a158369c3a94c616e0a7fc4a8602d7886c776c7e96bd2` | https://web.archive.org/web/20110302021338/http://www.ugtt.org.tn:80/userfiles/file/tr5.pdf |
| `ugtt_2011_tr6.pdf` | 200 | 673157 | `85c66936180c28f4b97fa0e11a8a68d116d320ba981e2b4f23820721b19ab1f8` | https://web.archive.org/web/20110302021447/http://www.ugtt.org.tn:80/userfiles/file/tr6.pdf |
| `ugtt_2011_tr7.pdf` | 200 | 894518 | `b6d231abfacf3625e9305797f9294ff36ada18afcf881060ecc18310aebd6bee` | https://web.archive.org/web/20110302022051/http://www.ugtt.org.tn:80/userfiles/file/tr7.pdf |
| `mas_convar7.pdf` | 200 | 980772 | `7e0e4613a7176c83d05199e5bf68a8426cbddf7248131ad6411efe293ff75128` | https://web.archive.org/web/20180417040204/http://www.social.gov.tn:80/fileadmin/user1/doc/pdftravail/convar7.pdf |
| `mas_100.pdf` | 200 | 97124 | `23ed9f164a68ed5844775f8f07bf5dca7df08ad4754c8bf9ddc68ae7325d77de` | https://web.archive.org/web/20191112203955/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/100.pdf |
| `mas_105.pdf` | 200 | 69458 | `7172ead9ccd741d8277acf1f6c132f6486cbb48cb01dabf1df54725495b59bdf` | https://web.archive.org/web/20191112210943/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/105.pdf |
| `mas_111.pdf` | 200 | 90788 | `2a0fa69f9dd179f178287b210d841a2f83abc15b57b8ebb0b64c4e2787b0d71e` | https://web.archive.org/web/20191112204040/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/111.pdf |
| `mas_122.pdf` | 200 | 87729 | `5fcb06f9d09d75e5d3af4f3efe50b53646cabca5e5f38d16009b14e6a61c7c83` | https://web.archive.org/web/20191112204217/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/122.pdf |
| `mas_135.pdf` | 200 | 76054 | `e5b3e7d91b956bf5640e64971788df1873dea60fc0f4b34b8c305355289f4c77` | https://web.archive.org/web/20180417035030/http://www.social.gov.tn:80/fileadmin/user1/doc/pdftravail/conventions/135.pdf |
| `mas_138.pdf` | 200 | 208552 | `c8898175269c4e9a059edc3355222a08d587d27721d2215b02f8d8e35e556e01` | https://web.archive.org/web/20191112215400/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/138.pdf |
| `mas_142.pdf` | 200 | 84656 | `8efd2def2dd71b44cb237323067320ce601a98ad1d7cb1abc895cb4ab8cadbd1` | https://web.archive.org/web/20191112214031/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/142.pdf |
| `mas_159.pdf` | 200 | 100964 | `5d69ebf90a03b50af535edb0bdc8021c76514b41d18c8777256da1011e35520a` | https://web.archive.org/web/20191112204029/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/159.pdf |
| `mas_182.pdf` | 200 | 114625 | `09a69b5988c89c19a06b5d766d55f385300540c4d7daa2dcabb43db890720e5b` | https://web.archive.org/web/20171215141428/http://www.social.gov.tn:80/fileadmin/user1/doc/pdftravail/conventions/182.pdf |
| `mas_29.pdf` | 200 | 275252 | `ade6c56a73d1ddf1e1731cc2be293ca3854269235434d63da4b607f7056fbe6a` | https://web.archive.org/web/20191112203943/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/29.pdf |
| `mas_81.pdf` | 200 | 234751 | `a4f507b2148737f41fc832b63712a2049f570501b16f698c71c0b87973d0d94b` | https://web.archive.org/web/20191112220720/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/81.pdf |
| `mas_87.pdf` | 200 | 127455 | `7139898baeb2ed16ed60242a1ce118dca7e341b844d36c278456bdbf8a8c1bf2` | https://web.archive.org/web/20171025131136/http://www.social.gov.tn:80/fileadmin/user1/doc/pdftravail/conventions/87.pdf |
| `mas_98.pdf` | 200 | 97187 | `d6c2eaf2cdcc9a903136b3d7dbc382b53006d2d5626b5bfb987179378d410cf7` | https://web.archive.org/web/20191112205930/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/conventions/98.pdf |
| `mas_evosmag.pdf` | 200 | 130293 | `b352ff8140756813ee31b044d861472ba969c5564e324251954654f6772106e2` | https://web.archive.org/web/20191112214655/http://www.social.gov.tn/fileadmin/user1/doc/pdftravail/evosmag.pdf |
| `mas_evosmig40.pdf` | 200 | 160698 | `1cd36ee470f976b99562e137643ed628c9e012159fb8c4d2d22624e599ffa453` | https://web.archive.org/web/20171025131625/http://www.social.gov.tn:80/fileadmin/user1/doc/pdftravail/evosmig40.pdf |
| `mas_evosmig48.pdf` | 200 | 157739 | `7b027e395432cb79d8bf452ede56bd92b4b3514673c21a5c70fb6dd0b53e4acc` | https://web.archive.org/web/20171025131630/http://www.social.gov.tn:80/fileadmin/user1/doc/pdftravail/evosmig48.pdf |
| `mas_new_fr_conventions.html` | 200 | 69221 | `8592e4069f7ce66e17bf1da3b4bea7ced55039c588a271cd2e9a33a205df8396` | https://web.archive.org/web/20230331224554/https://www.social.gov.tn/fr/conventions |
| `mas_new_fr_conv177.html` | 200 | 71913 | `635ce6de95e0749290883eca6fb26e25190a4e21fdd513b858f708724de5ac22` | https://web.archive.org/web/20251010224027/https://www.social.gov.tn/fr/conventions?service=177 |
| `mas_new_fr_conv181.html` | 200 | 71723 | `6d70a05cd140179629effaa8cb31a259dfe5717bb007f65a4c64046be51787a4` | https://web.archive.org/web/20250523105501/https://www.social.gov.tn/fr/conventions?service=181 |
| `mas_new_conv173.html` | 200 | 66733 | `df9bf73a7f2bf3c5a41793c4d2856a7616fdad63cfc17afdd905b0e5e5bc01b8` | https://web.archive.org/web/20230925204833/https://www.social.gov.tn/conventions?service=173 |
| `ugtt_2009_fr_negociations.html` | 200 | 45015 | `ce7ee3d69d632e0ad64a204c1d69413f5e06f2109f6a6e4ef6984f5e801c52f2` | https://web.archive.org/web/20090704162949/http://www.ugtt.org.tn:80/fr/negociations-sociales.php |
| `ugtt_2012_fr_cat_conventions.html` | 200 | 46754 | `5a67923fe57bc99dbd5184cac094df7285d2323e3fb8e4f87a9651de57662831` | https://web.archive.org/web/20120423072616/http://www.ugtt.org.tn:80/fr/category/conventions-collectives/ |
| `ugtt_2016_cat_accords.html` | 200 | 85954 | `5cb1bfd7eb658958f621a30e2738e8491b5d56fc2a8e107f99d4a3f522e346c8` | https://web.archive.org/web/20160728115151/http://www.ugtt.org.tn:80/category/accords-conjoints/ |
| `pt_btp_avenant16_2022_ar.pdf` | 200 | 3141690 | `fc6fe463685bf688b133285f1096266d2730a9ab2f90d5dc5cdf81dbf11bc7a7` | https://paie-tunisie.com/docs/relatedInfo/arrete2022-3802arabe-63.pdf |
| `pt_textile_avenant18_2024_ar.pdf` | 200 | 6791082 | `b5669a3551019a6e4e0f531c57bca3f093d8f36b1c49ed37b20b2b46929fb5f9` | https://paie-tunisie.com/docs/relatedInfo/arrete2024-1382arabe-2-59.pdf |
| `ugtt_2006_accordoct2005fr.html` | 200 | 12767 | `d17231b8c792b92663a29380073466fc563a32980c1f0dec0956718f816ce55c` | https://web.archive.org/web/20060505003340/http://www.ugtt.org.tn:80/html/accordoct2005fr.htm |
| `ugtt_2012_protocole_15-08.pdf` | 200 | 187779 | `d64cd6c67fd31bd28163eecbc2b705ba67a2901488a8be0218152c19208a6f4a` | https://web.archive.org/web/20120906234313/http://www.ugtt.org.tn:80/wp-content/uploads/2012/08/Protocol-daccord-15-08-2012.pdf |
| `ugtt_2012_accord-f.pdf` | 200 | 745201 | `53390d54d6635b3578a23e3c693a2251094b59353684d5fa4b97083199218e88` | https://web.archive.org/web/20121224114622/http://www.ugtt.org.tn:80/wp-content/uploads/2012/12/accord-f.pdf |
