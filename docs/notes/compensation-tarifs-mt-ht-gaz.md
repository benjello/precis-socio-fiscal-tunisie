# Note documentaire — tarifs de l'électricité en moyenne et haute tension, du gaz en moyenne et haute pression ; relecture de la basse tension

Passe du 6 octobre 2026. Famille de toutes les valeurs : **source officielle tunisienne** (Journal officiel ; STEG). Complète `docs/notes/compensation-tarifs-electricite-gaz.md` sans la remplacer. Rien de versionné n'a été modifié.

Pièces de travail : `scratchpad/relu/steg/image_lu.txt` (saisie brute des PDF lus à l'image) ; `relu/steg/ht_hp_html.txt`, `mt_mp_html.txt`, `ind_html.txt` (transcription mécanique des pages archivées de la STEG, une entrée par état distinct de la page) ; `relu/steg/regime_2017.jpg` (régime horaire) ; `relu/jort/j92-17.png`, `j92-18.png`.

## 0. Niveaux de preuve — et une correction de la note précédente

- **I = image lue dans cette passe** : PDF de la STEG rendu à 115 points par pouce et lu (la plupart des PDF déposés n'ont AUCUNE couche texte : ce sont des images) ; ou page du Journal officiel.
- **H = page HTML de la STEG archivée par Internet Archive, portant sa date d'effet** : texte numérique de l'entreprise, transcrit mécaniquement (pas d'OCR, pas de risque de chiffre mal lu), relu ici ligne à ligne.
- **A = Journal officiel lu à l'image par la passe précédente**, non relu ici (sauf 1992).
- **Correction** : les fichiers `steg_tarifs_hp_*.pdf` sont des grilles du **gaz haute pression**, non de l'électricité haute tension. **Il n'existe au dépôt aucun PDF de la haute tension électrique** : toute la haute tension de 2004 à 2022 est de niveau H. De même `steg_tarifs_mt_2018b.pdf` et `mp_2018b.pdf` sont les grilles du **1er mai 2018** (table des tarifs FM-53 du 29 mai 2018), non celles de septembre 2018.
- Les « 31 grilles déposées, non transcrites » : 29 PDF utiles lus à l'image ici (les deux `chang*.pdf` sont des conditions de raccordement sans prix) ; `bt_20180102`, `bp_*` (gaz basse pression, 7 fichiers) et `bt_sys_2025` **n'ont pas été relus** faute de temps.
- **Concordance PDF / HTML** : partout où les deux existent (MT 2010, 2012, 2014, mai 2018, 2019 ; gaz HP 2014, 2017 ; gaz MP 2010, 2014, mai 2018 ; gaz 2022), les valeurs sont **identiques**. Aucun écart.

## 1. Comment se lit un tarif de moyenne ou de haute tension (pour le lecteur non spécialiste)

Un abonné en moyenne tension (usine, hôtel, grande surface, pompage) ou en haute tension (cimenterie, sidérurgie, chimie — 21 à 23 clients seulement, STEG, rapports annuels 2019 et 2021) ne paie pas un prix du kilowattheure par tranche de consommation comme un ménage. Sa facture a deux étages :

1. **une prime fixe, la « redevance de puissance »** : tant de millimes par kilowatt souscrit et par mois, due quelle que soit la consommation. Elle rémunère la capacité que le réseau tient à sa disposition. (Au tarif « uniforme », elle est comptée par kVA.) ;
2. **le prix de l'énergie, qui dépend de l'heure** : la journée est découpée en **postes horaires**, et le kilowattheure coûte plus cher aux heures où le réseau est le plus sollicité (la « pointe ») et moins cher la nuit. C'est un signal : il pousse l'industriel à déplacer sa consommation.

S'y ajoutent, hors grille : la taxe sur la valeur ajoutée (18 % puis 19 % ; taux réduit pour l'irrigation), la surtaxe municipale (1,5 millime par kWh en haute et moyenne tension en 1992 ; 3 puis 5 millimes en 2010 et 2014) et, depuis le 1er janvier 2024, la taxe au profit du Fonds de transition énergétique (5 millimes par kWh).

**Les postes horaires.** Jusqu'en 1992 (Journal officiel) : trois postes — jour, pointe, nuit ; les heures n'en sont pas données par les arrêtés lus. De 2004 à 2013 : quatre postes — jour, pointe, soir, nuit ; **heures non établies ici** (l'image du régime horaire de 2012 n'est pas archivée). À partir du 1er mai 2014 les colonnes changent de sens : **jour, pointe matin été, pointe soir, nuit** — on ne peut donc pas aligner « pointe » et « soir » d'avant 2014 sur les colonnes d'après. Heures du régime à quatre postes **tel que la STEG l'affiche le 21 avril 2017** (image « régime horaire » liée depuis les pages de tarifs, lue à l'image ; le document n'est pas daté : rien n'établit ici que ces heures soient celles du 1er mai 2014 ni qu'elles n'aient pas changé depuis) :

| Période | Nuit | Jour | Pointe matin été | Pointe soir |
|---|---|---|---|---|
| septembre à mai | 21 h – 7 h | 7 h – 18 h | — | 18 h – 21 h |
| juin à août | 22 h – 6 h 30 | 6 h 30 – 8 h 30 et 13 h 30 – 19 h | 8 h 30 – 13 h 30 | 19 h – 22 h |

Le même document donne un « régime à trois postes sur toute l'année » (octobre à mars : jour 6 h 30 – 17 h 30, pointe soir 17 h 30 – 21 h 30, nuit 21 h 30 – 6 h 30 ; avril à septembre : jour 8 h – 19 h, pointe soir 19 h – 23 h, nuit 23 h – 8 h), appliqué à l'irrigation à trois postes en basse tension. Hypothèse, non établie : la pointe d'été en milieu de journée apparaît comme colonne en 2014 ; faute des heures d'avant 2014, on ne sait pas si c'est une nouveauté ou un simple changement de libellé de la « pointe » antérieure.

**Les autres lignes des grilles** : « uniforme » (un prix unique du kWh, pour les abonnés sans comptage horaire) ; « secours » (prime réduite, énergie plus chère — pour qui produit sa propre électricité) ; tarifs agricoles avec « effacement » (l'abonné s'engage à ne pas consommer en pointe). Depuis le 1er juin 2013 un **tarif interruptible** optionnel indemnise le client haute ou moyenne tension qui accepte d'être coupé entre 11 h et 15 h du 1er juin au 30 septembre (« Décision de monsieur le Ministre de l'Industrie du 5 mars 2013 »). Le document de la STEG (`steg_tarifs_interr_2013.pdf`, lu à l'image) le décrit : tarif optionnel pour les abonnés haute et moyenne tension d'au moins 1 MW de puissance souscrite, qui « s'engagent à diminuer leurs puissances appelées suite à la demande de la STEG », 45 heures par an au plus, en juin, juillet, août et septembre, entre 11 h et 15 h ; puissance d'interruption d'au moins 1 MW en haute tension et 100 kW en moyenne tension. Indemnités en moyenne tension : variable, 212 millimes par kWh non consommé en deçà de 400 kW interruptibles et 416 au-delà (465 au tarif uniforme) ; fixe, 1 050 millimes par kW interruptible et par mois (500 par kVA au tarif uniforme). En haute tension (page archivée, capture 20170418214311, niveau H) : variable 204 en deçà de 3 MW et 410 au-delà ; fixe 900.

**Le gaz** se lit de la même façon : redevance d'abonnement (dinars par mois), **redevance de débit** (millimes par thermie-heure souscrite et par mois — l'équivalent de la prime de puissance), et prix de l'énergie en millimes par **thermie** (1 tep = 10 000 thermies). Trois niveaux de pression : basse (ménages, petits commerces : 50 à 8 000 th/h), moyenne (MP1 : 1 000 à 4 000 th/h ; MP2 : 6 000 à 30 000), haute (HP1 : 10 000 à 30 000 ; HP2 : plus de 30 000). Jusqu'en avril 2014 le prix de la haute pression au-delà de 2 000 tep par mois n'est pas un chiffre mais une **formule indexée sur le fuel lourd** : 0,1 F − c, F étant le prix hors taxe de la tonne de fuel lourd n° 2. Depuis le 1er juin 2016 les cimentiers ont un tarif propre, indexé sur le prix d'achat du gaz par la STEG (Pg).

## 2. Électricité, moyenne tension — tarif à postes horaires et tarif uniforme (millimes par kWh, hors taxes)

### 1975-1992 (Journal officiel ; trois postes)

| Date d'effet | Jour | Pointe | Nuit | Prime de puissance | Uniforme | Texte | Preuve |
|---|---:|---:|---:|---|---:|---|---|
| 20/04/1975 | 11,3 | 18,4 | 4,1 | 1 500 mill/kW-mois | à tranches 20,4 / 15,3 | arrêté du 15 avril 1975, JORT n° 26, p. 758 | A |
| 30/11/1978 | 18 | 30 | 9 | 1 500 | à tranches 30 / 26 | arrêté conjoint du 27 nov. 1978, JORT n° 80, p. 3416 | A |
| 31/08/1981 | 31 | 47 | 22 | 1 500 | à tranches 41 | arrêté du 1er sept. 1981, JORT n° 55, p. 2051 | A (partiel) |
| 29/09/1982 | 35 | 56 | 26 | 2 000 | 46 | arrêté du 30 sept. 1982, JORT n° 63, p. 2072-2073 | A |
| 31/05/1984 | 39 | 68 | 29 | 2 000 | 51 | arrêté du 4 juin 1984, JORT n° 38, p. 1378-1379 | A |
| 16/06/1987 | 42 | 77 | 30 | 2 000 | 54 | arrêté du 8 juin 1987, JORT n° 42, p. 757-759 | A |
| 01/01/1991 | 40 | 80 | 29 | 2 000 | 52 | arrêté du 19 déc. 1990, JORT n° 86, p. 2252-2253 | A |
| 01/08/1992 | 40 | 84 | 29 | 2 500 (« 2,500 dinars par KW et par mois ») | 56 (300 mill/kVA-mois) | décision du 11 août 1992, JORT n° 56, p. 1101 | **I** |

Bases fiscales : taxes comprises jusqu'en 1987, hors TVA à partir de 1991. La prime de 1975 à 1987 est donnée par la note précédente en millimes par kW et par mois ; l'unité des arrêtés de 1975 à 1984 est à contrôler à la page avant publication (la haute tension de la même époque est tarifée par kW et **par an**).

### 2004-2022 (STEG ; quatre postes)

| Date d'effet | Jour | Pointe | Soir | Nuit | Prime (mill/kW-mois) | Uniforme (prime en mill/kVA-mois) | Source | Preuve |
|---|---:|---:|---:|---:|---:|---|---|---|
| 01/05/2004 | 58 | 102 | 80 | 40 | 3 000 | 73 (300) | fr/clients_ind/tarifs.html, capt. 20040912124736 | H |
| 01/01/2006 | 66 | 112 | 95 | 48 | 3 500 | 84 (500) | id., capt. 20060511033855 | H |
| 01/09/2008 | 96 | 153 | 122 | 76 | 3 500 | 115 (500) | id., capt. 20090106032036 | H |
| 01/06/2010 | 110 | 168 | 133 | 85 | 3 500 | 125 (500) | steg_tarifs_mt_20100601.pdf ; page capt. 20120503044359 | **I** + H |
| 01/09/2012 | 123 | 185 | 147 | 94 | 4 000 | 137 (700) | steg_tarifs_mt_20120901.pdf ; page capt. 20121103154608 | **I** + H |
| 01/03/2013 | 132 | 197 | 154 | 100 | 5 000 | 143 (1 200) | fr/clients_ind/tarifs_mt.html, capt. 20130512122123 | H |

| Date d'effet | Jour | Pointe matin été | Pointe soir | Nuit | Prime (mill/kW-mois) | Uniforme (prime en mill/kVA-mois) | Source | Preuve |
|---|---:|---:|---:|---:|---:|---|---|---|
| 01/05/2014 | 152 | 238 | 218 | 115 | 8 000 | 167 (2 600) | steg_tarifs_mt_20140501.pdf ; page capt. 20170420111255 | **I** + H |
| 01/01/2017 | 161 | 250 | 227 | 124 | 8 000 | 176 (2 600) | page capt. 20180112083138 | H |
| 01/05/2018 | 173 | 294 | 252 | 133 | 8 000 | 189 (2 600) | steg_tarifs_mt_2018b.pdf ; page capt. 20180706181801 | **I** + H |
| 01/09/2018 | 215 | 323 | 291 | 167 | 11 000 | 212 (5 000) | page capt. 20181011193337 | H |
| 01/06/2019 | 240 | 366 | 329 | 188 | 11 000 | 251 (5 000) | steg_tarifs_mt_2019.pdf ; page capt. 20190818160727 | **I** + H |
| 01/10/2022 | 290 | 417 | 377 | 222 | 11 000 | 291 (5 000) | page capt. 20230330151526 et 20240519131811 | H |

Autres lignes lues à l'image (détail dans `image_lu.txt`) : secours — 128 / 180 / 150 / 90, prime 2 000 (2010) ; 143 / 198 / 164 / 101, 2 250 (2012) ; 170 / 295 / 258 / 123, 3 700 (2014) ; 188 / 322 / 284 / 140, 3 700 (mai 2018) ; 264 / 407 / 365 / 200, 6 000 (2019). Irrigation agricole (effacement en pointe) : jour 104, soir 120, nuit 80 (2012) ; 114 / 132 / 88 (2014) ; 126 / 144 / 96 (mai 2018) ; 189 / 195 / 138 (2019). Taux de TVA portés par les grilles : 18 % et 12 % (irrigation, usages domestiques) jusqu'en 2017 ; 19 % et 13 % en 2018 ; 19 % et 7 % (irrigation) en 2019.

**Lecture** (constat) : entre le 1er mai 2004 et le 1er octobre 2022 le kWh de jour est multiplié par 5,0 (58 → 290), celui de nuit par 5,6 (40 → 222), la prime de puissance par 3,7 (3 000 → 11 000) ; la hausse la plus forte en une fois est celle du 1er septembre 2018 (jour : 173 → 215, +24 % ; prime : 8 000 → 11 000).

## 3. Électricité, haute tension (millimes par kWh, hors taxes)

### 1978-1992 (Journal officiel ; trois postes)

| Date d'effet | Jour | Pointe | Nuit | Prime de puissance | Texte | Preuve |
|---|---:|---:|---:|---|---|---|
| 30/11/1978 | 15 | 22 | 8 | 5 D/kW-an | JORT 1978 n° 80 | A |
| 31/08/1981 | 26 | 37 | 20 | 6 D/kW-an | JORT 1981 n° 55 | A (partiel) |
| 29/09/1982 | 31 | 46 | 24 | 12 D/kW-an | JORT 1982 n° 63 | A |
| 31/05/1984 | 33 | 58 | 25 | 15 D/kW-an | JORT 1984 n° 38 | A |
| 16/06/1987 | 34 | 68 | 26 | 15 D/kW-an | JORT 1987 n° 42 | A |
| 01/01/1991 | 33 | 68 | 25 | 1,250 D/kW-mois | JORT 1990 n° 86 | A |
| 01/08/1992 | 34 | 74 | 26 | 2,000 D/kW-mois | décision du 11 août 1992, JORT n° 56, p. 1101, annexe 1 « Tarifs haute tension 225 kV – 150 kV – 90 kV » | **I** |

Aussi lu en 1992 (I) : haute tension secours 0,500 D/kW-mois, 49 / 84 / 29 ; moyenne tension secours 1,500 D, 54 / 90 / 31 ; usages agricoles avec effacement, jour 40, nuit 29 ; surtaxe municipale 2 millimes (BT) et 1,5 (HT-MT) ; TVA 6 % sur l'énergie, 17 % sur les redevances.

### 2004-2022 (STEG, pages archivées — aucun PDF)

| Date d'effet | Jour | Pointe [matin été à partir de 2014] | Soir [pointe soir à partir de 2014] | Nuit | Prime (mill/kW-mois) | Capture | Preuve |
|---|---:|---:|---:|---:|---:|---|---|
| 01/05/2004 | 48 | 89 | 69 | 38 | 2 500 | tarifs_hp.html, 20040912124756 | H |
| 01/01/2006 | 59 | 103 | 79 | 45 | 3 000 | 20060511223807 | H |
| 01/09/2008 | 94 | 147 | 119 | 75 | 3 000 | 20090106024743 | H |
| 01/06/2010 | 106 | 164 | 129 | 81 | 3 000 | 20110929172540 ; tarifs_ht.html 20120503041404 | H |
| 01/09/2012 | non capturée | | | | | — | — |
| 01/03/2013 | 126 | 192 | 142 | 96 | 4 500 | tarifs_ht.html, 20130531031738 | H |
| 01/05/2014 | 148 | 233 | 212 | 111 | 7 500 | 20170418214311 | H |
| 01/01/2017 | 156 | 249 | 221 | 120 | 7 500 | 20180115190725 | H |
| 01/05/2018 | 168 | 279 | 243 | 129 | 7 500 | 20180706212555 | H |
| 01/09/2018 | 207 | 309 | 279 | 160 | 10 000 | 20181011222848 | H |
| « 01/06/2019 » | 207 | 309 | 279 | 160 | 10 000 | 20211027082142 | H |
| 01/05/2022 | 238 | 364 | 332 | 179 | 10 000 | 20230330140759 | H |

Lignes annexes (H) : « trois postes horaires » jusqu'en 2010 (54 / 87 / 38 en 2004 ; 68 / 99 / 45 en 2006 ; 109 / 139 / 75 en 2008 ; 122 / 150 / 81 en 2010 ; prime identique) — ligne disparue en 2013 ; secours : 59 / 102 / 76 / 40, prime 1 000 (2004) ; 70 / 115 / 89 / 46, 1 250 (2006) ; 110 / 160 / 134 / 77 (2008) ; 124 / 176 / 146 / 86 (2010) ; 147 / 206 / 159 / 104, 1 700 (2013) ; 168 / 290 / 255 / 120, 3 000 (2014) ; 173 / 295 / 260 / 125 (2017) ; 185 / 315 / 279 / 135 (mai 2018) ; 225 / 350 / 315 / 168, 5 200 (sept. 2018) ; 260 / 395 / 358 / 187 (2022).

**Deux singularités à écrire, non à lisser.**
1. La page de la haute tension datée « à compter du 01/06/2019 » porte les prix du 1er septembre 2018 : **la haute tension n'a pas été relevée en juin 2019**, alors que la moyenne tension l'a été (+12 % sur le jour). La date de 2019 est celle de la page, non d'un changement de prix.
2. **La haute tension est relevée le 1er mai 2022, la moyenne tension le 1er octobre 2022** : les deux pages, capturées le même jour (30 mars 2023), portent ces deux dates différentes ; la capture de mai 2024 confirme le 1er octobre pour la moyenne tension. Aucune grille de moyenne tension datée du 1er mai 2022 n'a été vue : entre mai et octobre 2022 la moyenne tension restait, selon ces pièces, à la grille de 2019. À publier comme deux dates distinctes, avec cette réserve.

## 4. Gaz naturel, moyenne pression (millimes par thermie, hors taxes)

| Date d'effet | MP (unique) / MP1 | MP2 | Redevance d'abonnement ; de débit (MP1 / MP2) | Source | Preuve |
|---|---:|---:|---|---|---|
| 16/06/1987 | 11,3 (taxe à la production comprise) | — | — | JORT 1987 n° 42 | A |
| 01/01/1991 | 11,1 | — | — | JORT 1990 n° 86 | A |
| 01/08/1992 | 12,3 | — | 20 D/ab-mois ; 0,100 D par th/h et par mois (débit de 1 000 à 20 000 th/h, pression maximale 20 bars) | JORT 1992 n° 56, p. 1102, annexe 4 | **I** |
| 01/08/2004 | 15,76 | 15,19 | 20 D ; — / 200 mill/th-h-mois | fr/clients_ind/tarifs.html, capt. 20040912124736 (15,76 retrouvé dans la page) | H |
| 01/01/2006 | 16,57 | 16,00 | 20 D ; — / 200 | capt. 20060511033855 (16,57 retrouvé dans la page) | H |
| 01/09/2008 | 23,60 | 23,00 | 20 D ; 100 / 200 | capt. 20090106032036 | H |
| 01/06/2010 | 25,30 | 24,90 | 20 D ; 100 / 200 | steg_tarifs_mp_20100601.pdf ; tarifs_mp.html capt. 20120504033902 | **I** + H |
| 01/09/2012 ; 01/03/2013 | non capturées | | | — | — |
| 01/05/2014 | 37,6 | 37,1 | 20 D ; 200 / 325 | steg_tarifs_mp_20140501.pdf ; capt. 20170421210723 | **I** + H |
| 01/01/2017 | 40,3 | 39,8 | 20 D ; 200 / 325 | tarifs_mp.html, capt. 20180115231552 | H |
| 01/05/2018 | 44,5 | 43,9 | 20 D ; 200 / 325 | steg_tarifs_mp_2018b.pdf ; capt. 20180606040318 | **I** + H |
| 01/09/2018 | 54,5 | 53,8 | 20 D ; 300 / 450 | capt. 20181018014622 | H |
| 01/05/2022 | 71,1 | 70,5 | 20 D ; 300 / 450 | steg_tarifs_gaz_2024.pdf (table du 02-01-2024) ; capt. 20230330150817 | **I** + H |

**Nouveau par rapport à la note précédente** : les grilles du 1er mai 2014, du 1er janvier 2017, du 1er mai 2018 et du 1er septembre 2018 (la page `tarifs_mp.html` existait dans le balayage, contrairement à ce que disait la note). Tarif cimentier en moyenne pression (I) : 1,032 × Pg, soit 60,2261 mill/th à compter du 1er juin 2016 (Pg = 58,3586, « prix moyen d'achat du gaz naturel pour l'année 2015 ») et 40,4232 à compter du 1er juin 2017 (Pg = 39,1698, prix moyen de 2016) ; « tarifs révisables pendant le mois de juin de chaque année sur la base des données comptables de la STEG de l'année qui précède ».

**Lecture** : de juin 2010 à mai 2022 le prix de l'énergie en MP1 est multiplié par 2,8 (25,30 → 71,1) ; le saut le plus fort est celui de mai 2014 (+49 % par rapport à 2010, deux grilles intermédiaires manquant).

## 5. Gaz naturel, haute pression (millimes par thermie, hors taxes)

| Date d'effet | HP1 | HP2 jusqu'à 2 000 tep/mois | HP2 au-delà | Redevance d'abonnement ; de débit | Source | Preuve |
|---|---|---|---|---|---|---|
| 16/06/1987 ; 01/01/1991 | formule unique : 0,1 F − 0,67 | | | — | JORT 1987 n° 42 ; 1990 n° 86 | A |
| 01/08/1992 | 0,1 F − 0,67 (débit ≥ 20 000 th/h, 76 bars) | | | 300 D/ab-mois ; 0,400 D par th/h et par mois | JORT 1992 n° 56, p. 1102 | **I** |
| 01/05/2004 | 0,1 F − 1,2475 (débit ≥ 10 000 th/h) | | | 300 D ; 400 mill | tarifs_hp.html, capt. 20040912124756 | H |
| 01/01/2006 | 0,1 F − 7,8932 | | | 300 ; 400 | capt. 20060511223807 | H |
| 01/09/2008 | 24,00 | 24,00 | 0,1 F − 4,3571 | 300 ; 400 | capt. 20090106024743 | H |
| 01/06/2010 | 25,30 | 26,80 | 0,1 F − 1,590 | 300 ; 400 | capt. 20110929172540 | H |
| 01/09/2012 | 27,10 | 29,50 | 0,1 F − 1,590 | 300 ; 400 | capt. 20121127144428 | H |
| 01/03/2013 | 29,20 | 32,30 | 0,1 F − 1,590 | 300 ; 400 | capt. 20130512102554 | H |
| 01/05/2014 | 35,8 | 39,1 | **52,5** (prix fixe : la formule disparaît) | 300 ; 500 | steg_tarifs_hp_20140501.pdf ; capt. 20170516131050 | **I** + H |
| 01/01/2017 | 38,4 | 42,6 | 56,0 | 300 ; 500 | steg_tarifs_hp_20180102.pdf ; capt. 20170331002613 | **I** + H |
| 01/05/2018 | 42,5 | 47,2 | 59,4 | 300 ; 500 | capt. 20180706201817 | H |
| 01/09/2018 | 52,2 | 58,0 | 70,0 | 300 ; 700 | capt. 20181011230139 | H |
| « 01/06/2019 » | 52,2 | 58,0 | 70,0 (inchangés) | 300 ; 700 | capt. 20210819160850 | H |
| 01/05/2022 | 60,4 | 67,1 | 81,3 | 300 ; 700 | steg_tarifs_gaz_2024.pdf ; capt. 20230205070803 | **I** + H |

F : « le prix en dinars hors taxe sur la valeur ajoutée de la tonne [de] fuel oil lourd n° 2 livrée en vrac à tout utilisateur dont la consommation afférente à une même usine est égale ou supérieure à 10 000 tonnes métriques par an » (JORT 1992, p. 1102, image). Les valeurs en millimes que la note précédente donne pour la formule (31,3572 en 2008 ; 34,1243 en 2010 ; 38,5886 en 2012 ; 41,2671 en 2013) sont des applications de la formule au prix du fuel du moment. Contrôle fait : 31,3572 (capture 20090106024743), 38,5886 (20121127144428) et 41,2671 (20130512102554) **figurent dans les pages** (niveau H), avec le prix du fuel F = 357,143, 401,786 et 428,571 D la tonne ; 34,1243 (2010) n'a pas été retrouvé dans la capture lue et reste un CALCUL (0,1 × 357,143 − 1,590). Tarif cimentier en haute pression (I) : 1 × Pg = 58,3586 mill/th à compter du 1er juin 2016. Taxe du Fonds de transition énergétique : 0,25 millime par thermie (page capturée le 5 février 2023), puis 1,25 à compter du 1er janvier 2024 (I et H), sauf pour les abonnés basse pression jusqu'à 300 thermies par mois.

Gaz basse pression au 1er mai 2022 (I, même document) : conforme au tableau du volume (24,3 / 38,7 / 58,5 / 86,7 pour les ménages) ; les sept PDF basse pression de 2008 à 2019 n'ont pas été relus.

## 6. Le prix moyen du kWh d'un « profil type » : aucune source n'en donne

Ni la STEG (grilles, pages, rapports annuels ouverts) ni l'Observatoire ne publient de facture type ou de profil de charge pour un abonné moyenne ou haute tension. **Ne pas en inventer.** Deux substituts honnêtes :

**(a) La recette moyenne par kWh et par niveau de tension — CALCUL de la note** à partir de deux tableaux de la STEG (ventes en GWh ; ventes hors taxes en millions de dinars, « redevances de puissance comprises »). Rapport annuel 2019 (p. 37 et 74 du fichier), rapport annuel 2021 (p. 32 et 66 du fichier), couche texte.

| Année | Haute tension : MD / GWh = mill/kWh | Moyenne tension | Basse tension |
|---|---|---|---|
| 2018 | 259 / 1 302 = 199 | 1 457 / 6 856 = 213 | 1 526 / 7 390 = 206 |
| 2019 | 351 / 1 262 = 278 | 1 867 / 6 956 = 268 | 1 851 / 8 169 = 227 |
| 2020 | 468 / 1 178 = 397 (**anomalie**) | 1 754 / 6 359 = 276 | 1 767 / 7 835 = 226 |
| 2021 | 312 / 1 358 = 230 | 1 850 / 6 780 = 273 | 1 882 / 8 304 = 227 |

(2017, en MD seulement : 228 / 1 236 / 1 478.) Le chiffre de la haute tension en 2020 n'est pas un prix : les ventes en valeur y montent de 33 % quand les volumes baissent de 7 %, puis retombent de 33 % en 2021 ; le rapport de 2021 ne l'explique pas dans les lignes lues (régularisation, ventes à l'étranger ?) — à écarter ou à éclaircir avant toute publication. Les montants en MD de ces tableaux n'ont pas été relus à l'image. Ce calcul recoupe l'ordre de grandeur de l'Observatoire (prix de vente global hors taxe : 244,0 mill/kWh en 2019, 248,6 en 2020, 244,8 en 2021).

**(b) Une facture type à hypothèses écrites**, si le rédacteur en veut une. Il faudrait poser, et afficher sous le tableau : la puissance souscrite (par exemple 100 kW en moyenne tension) ; le facteur de charge (par exemple 40 %, soit 29 200 kWh par mois) ; la répartition de l'énergie entre postes — soit uniforme sur les heures de l'année (ce qui donne, avec les heures du § 1, 42 % de jour, 12,5 % de pointe soir, 5 % de pointe matin d'été et 40 % de nuit : CALCUL de la note sur 8 760 heures — 273 jours à 11 h de jour, 3 h de pointe soir et 10 h de nuit ; 92 jours à 7,5 h, 5 h de pointe matin, 3 h de pointe soir et 8,5 h de nuit), soit celle d'une usine à un poste de jour ; l'absence de dépassement de puissance et d'énergie réactive. Avant 2014 les heures des postes ne sont pas établies : la facture type ne peut pas remonter au-delà sans elles.

## 7. Relecture des grilles basse tension publiées au volume (`tbl-compensation-eg-grilles-steg`)

| Grille | Pièce relue à l'image | Résultat |
|---|---|---|
| 1er mai 2004 ; 1er janvier 2006 | aucune : ces deux grilles n'existent qu'en page HTML archivée (niveau H) — pas de PDF de la STEG | non relisible à l'image ; à dire dans la légende |
| 1er septembre 2008 | steg_tarifs_bt_20080901.pdf | conforme (74 ; 90 / 131 ; 131 / 174 ; redevance 200) |
| 1er juin 2010 | steg_tarifs_bt_20100601.pdf | conforme (75 ; 92 / 133 ; 133 / 186) |
| 1er septembre 2012 | steg_tarifs_bt_20120901.pdf | conforme (75 ; 92 / 135 ; 135 / 200 ; redevance 300) |
| 1er mai 2014 | steg_tarifs_bt_20140501.pdf (image pure) | conforme (75 ; 108 ; 140 ; 151 / 184 / 280 / 350 ; redevance 500) |
| 1er janvier 2017 | steg_tarifs_bt_20170104.pdf | conforme (75 ; 108 ; 162 ; 167 / 198 / 285 / 350) |
| 1er septembre 2018 | steg_tarifs_bt_2018b.pdf (image pure) | conforme (75 ; 108 ; 176 / 218 / 295 / 355 ; redevance 700) |
| 1er juin 2019 | steg_tarifs_bt_2019.pdf | conforme (62 ; 96 ; 176 / 218 / 341 / 414) |
| 1er mai 2022 | steg_tarifs_bt_2024.pdf (table du 02-01-2024, p. 3/3) | prix conformes (62 ; 96 ; 176 ; 218 ; 341 ; 414) |

**Aucun écart de prix sur les huit grilles relues.** Trois précisions à porter au volume :
1. **La taxe du Fonds de transition énergétique.** La légende écrit qu'elle passe « de 1 à 5 millimes par kWh » en 2024. Le document relu dit seulement : « la taxe au profit du Fonds de Transition Energétique (FTE) (à compter du 1er janvier 2024) : 5 mill/kWh, **sauf pour les clients de la tranche économique en Basse Tension dont la consommation ne dépasse pas 100 kWh/mois** ». Le « 1 millime » antérieur n'y figure pas (il vient d'une autre pièce, à citer) et **l'exonération des petites consommations manque au volume**.
2. La surtaxe municipale est de 3 millimes par kWh en 2008 et 2010, de 5 à partir du 1er septembre 2012 ; le document de 2024 l'appelle « contribution au profit des collectivités locales ».
3. La redevance « passe de 150 […] à 700 depuis 2018 » : confirmé pour 2008 (200), 2012 (300), 2014 et 2017 (500), 2018, 2019 et 2022 (700) ; le 150 de 2004 et le 200 de 2006 sont de niveau H.
- La mention « à confronter aux documents » peut être levée pour 2008-2022 et remplacée par : « grilles de 2008 à 2022 relues sur les documents de la STEG ; grilles de 2004 et de 2006 d'après les pages du site de la STEG conservées aux archives du web ».
- Colonne des abonnés non résidentiels (301-500 kWh : 250 en 2014, 260 en 2017 ; 290 en 2018 ; 333 en 2019 et 2022 ; 501 et plus : 295, 295, 345, 391, 391) et tarifs spéciaux (éclairage public : 149, 170, 177, 218, 224, 234, 234, 261) : conformes à la note précédente.

## 8. Références candidates

Déjà créées par la passe précédente : `arrete-1975-04-15-…` à `decision-1992-08-11-tarifs-electricite-gaz` ; `steg-grille-2004-05-01` à `steg-grille-2022-05-01` ; `steg-ra-2019`, `steg-ra-2021`. À créer :
```json
[
 {"id": "steg-grille-2013-03-01", "type": "webpage", "title": "Les tarifs de l'électricité (à compter du 01/03/2013) (hors taxes) — moyenne tension, haute tension ; tarifs du gaz haute pression", "author": [{"literal": "Société tunisienne de l'électricité et du gaz"}], "issued": {"date-parts": [[2013, 3, 1]]}, "URL": "http://web.archive.org/web/20130512122123/http://www.steg.com.tn/fr/clients_ind/tarifs_mt.html", "note": "citation-key: steg-grille-2013-03-01 ; HT : capture 20130531031738 (tarifs_ht.html) ; gaz HP : 20130512102554 (tarifs_hp.html)."},
 {"id": "steg-grille-2018-05-01", "type": "report", "title": "Table des tarifs — tarifs de l'électricité moyenne tension et du gaz naturel à compter du 1er mai 2018 (hors taxes), réf. FM-53 / IE 02", "author": [{"literal": "Société tunisienne de l'électricité et du gaz, direction des études et de la planification"}], "issued": {"date-parts": [[2018, 5, 29]]}, "URL": "http://web.archive.org/web/20180614020128/http://www.steg.com.tn:80/dwl/tarifs/2018/tarifsmt_fr.pdf", "note": "citation-key: steg-grille-2018-05-01 ; gaz MP : capture 20180613124840 (tarifsmp_fr.pdf). Fichiers steg_tarifs_mt_2018b.pdf et steg_tarifs_mp_2018b.pdf."},
 {"id": "steg-grille-2022-10-01-mt", "type": "webpage", "title": "Les tarifs de l'électricité (à compter du 01/10/2022) (hors taxes) — niveau tension : MT", "author": [{"literal": "Société tunisienne de l'électricité et du gaz"}], "issued": {"date-parts": [[2022, 10, 1]]}, "URL": "http://web.archive.org/web/20230330151526/http://www.steg.com.tn/fr/clients_ind/tarifs_mt.html", "note": "citation-key: steg-grille-2022-10-01-mt"},
 {"id": "steg-regime-horaire-2017", "type": "webpage", "title": "Régime horaire (régime à trois postes horaires sur toute l'année ; régime à quatre postes horaires en été)", "author": [{"literal": "Société tunisienne de l'électricité et du gaz"}], "issued": {"literal": "s. d. ; capture du 21 avril 2017"}, "URL": "http://web.archive.org/web/20170421225223/http://www.steg.com.tn:80/fr/clients_ind/regime_horaire.html", "note": "citation-key: steg-regime-horaire-2017 ; image HtMt_L.jpg, lue."}
]
```

## 9. Notions à glossaire

- **redevance de puissance / prime fixe** (معلوم القدرة — à vérifier) ; **poste horaire** (jour, pointe, soir, nuit ; pointe matin été) ; **effacement** ; **tarif interruptible** ; **tarif uniforme** ; **tarif de secours** ; **thermie** et **redevance de débit** ; **haute, moyenne, basse pression** ; **Pg** (prix d'achat du gaz naturel par la STEG). Source canonique : grilles de la STEG et décision du 11 août 1992.

## 10. Lacunes

- Haute tension du 1er septembre 2012 ; gaz moyenne pression de septembre 2012 et mars 2013 ; moyenne tension entre mai et octobre 2022 (aucune grille datée de mai) : non capturées.
- Heures des postes avant 2014 : non établies. L'image `regime_horaire.jpg` de 2012 n'est pas archivée (la capture renvoie une page d'erreur).
- 1993-avril 2004 : toujours aucune grille (fiche `r-tarifs-electricite-grilles-1993-2003`, inchangée — aucune requête nouvelle dans cette passe).
- Journal officiel 1975-1990 (moyenne et haute tension, gaz) : valeurs de la passe précédente, non relues ici ; seule la décision de 1992 l'a été, en entier, et elle est conforme. Arrêtés de 1976, 1977, 1980, janvier 1981 : toujours non lus.
- Sept PDF du gaz basse pression (2008-2019), `bt_20180102`, `bt_sys_2025` : non relus à l'image.
- Profil type : aucune source (§ 6).
- Recherches infructueuses : aucune fiche nouvelle ; aucune passe à consigner (rien n'a été cherché au Journal officiel).
