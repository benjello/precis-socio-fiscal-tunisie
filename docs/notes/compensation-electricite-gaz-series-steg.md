# Note documentaire : prix d'achat du gaz par la STEG et coût de production de l'électricité, en séries longues

**Ce qu'on peut répondre au propriétaire.** Oui, ces séries existent et elles sont publiques. Elles ne figurent pas dans les rapports annuels de la STEG, qui n'ont pas de notes aux états financiers. Elles sont dans deux ensembles qu'on n'avait pas encore lus :

- **Les états financiers de la STEG, avec leurs notes** (`steg.com.tn/system/files/pdf/etat_financier_<année>.pdf`, exercices 2014 à 2023). Ils donnent pour chaque année le « prix moyen d'achat de la TEP gaz », la facture des combustibles, les achats d'électricité, et pour 2013-2016 le coût de revient du kWh et de la tep.
- **Les rapports annuels de l'ETAP** (2005, 2008-2014, 2016-2024). Ils donnent la valeur FOB et les quantités du gaz algérien acheté pour la STEG jusqu'en 2014, et le prix du gaz tunisien vendu à la STEG.

Avec les sources déjà connues (ONE, rapport du Contrôle général des finances de 2014, BAD, ANER), le prix d'achat du gaz est couvert de 2007 à 2024, avec une rupture de méthode de valorisation en 2006-2007. Le coût de revient du kWh est couvert pour 1996-1998, 2000-2004, 2008-2018 et 2022-2025.

**Rupture principale, établie par le texte.** Note 11 des états financiers 2014, p. 23 : « A partir de 2007, […] la STEG a procédé à la comptabilisation de la subvention d'exploitation accordée par l'Etat sous forme de prix bonifié. En effet, nos achats de gaz auprès de SOTUGAT et ETAP sont comptabilisés à un prix fixe de 90,800 DT qui ne reflète pas la valeur économique du produit […] ».

- La « subvention d'exploitation » des comptes de la STEG est égale, au dixième de million près, au « soutien total » du rapport du Contrôle général des finances de 2014 (p. 72) pour 2007-2013. Exemples : 672,7 ; 1 232,4 ; 2 733,7.
- Elle se décompose ainsi (états financiers 2014, note II-2, p. 35) : subvention indirecte « sur l'achat du gaz algérien » de 1 918,8 MDT en 2013 et 2 270,1 MDT en 2014 ; subvention directe de 850 MDT et 53 MDT.
- L'hypothèse de la note existante (`compensation-tarifs-electricite-gaz.md`, l. 110) est donc vérifiée : dès 2007, la STEG valorise le gaz au prix international dans ses comptes. Le rapport annuel 2007 retraite 2006 (589,7 MDT).
- Avant 2007, la valorisation est le prix administré. C'est le cas du compte 2005 (aucune ligne de subvention), de la BAD 2000-2004 et de l'ANER 1996-1998.

Tous les CSV de travail sont dans `/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/15adcd5f-c210-406f-907e-f6545e1e97a0/scratchpad/steg-series/`, un fichier par série, avec les colonnes année, valeur, unité, source, page, remarque. Il y en a 23, listés en fin de note.

---

## 1. Tableau récapitulatif des séries trouvées

Les familles ne sont pas superposées. Le tableau sert d'inventaire : chaque ligne est une série distincte.

Familles :
- **A** : comptes de la STEG (rapports annuels, états financiers).
- **A'** : ETAP, entreprise publique distincte, classée à part.
- **B** : ministère de l'énergie et Observatoire national de l'énergie (ONE), y compris le rapport de 2014 du Contrôle général des finances (CGF), organe de contrôle de l'État.
- **C** : rapport extérieur (BAD, Banque mondiale, ANER).
- **D** : statistique du commerce extérieur (UN Comtrade).
- **E** : évaluation, c'est-à-dire mon propre calcul.

### Prix d'achat et d'importation du gaz

**1. « Prix moyen (annuel) d'achat de la TEP gaz » de la STEG** (famille A)
- Période 2013-2023 ; DT/tep PCS.
- Source : états financiers 2014 p. 7 (2013 : 804,4 ; 2014 : 821,2) ; 2015 p. 7 (OCR ; 583,6) ; 2016 p. 7 (391,7) ; 2018 p. 8 (2017 : 569,9 ; 2018 : 805,5) ; 2019 p. 5 (933,2) ; 2021 p. 7 (2020 : 622,7 ; 2021 : 719,5) ; 2022 p. 3 (1 471,6) ; 2023 p. 3 (1 423,9).
- Couverture complète sur la période, sans trou.
- Fiabilité forte : texte de l'entreprise, recoupé (voir § 3).
- **Définition** : achats de combustibles ÷ « total des achats gaz » (ktep). Je l'ai vérifiée sur 2019 (5 416,3 / 5 804 = 933,2), 2020 (3 411,1 / 5 478 = 622,7), 2021 (4 147,9 / 5 765 = 719,5), 2022 (8 065,3 / 5 480 = 1 471,8) et 2023 (7 565,6 / 5 315 = 1 423,4). C'est une moyenne sur **toutes** les sources : gaz algérien acheté, redevance, gaz national, condensats. Le numérateur comprend le fuel et le gasoil.

**2. Prix moyen d'achat de la tep de gaz, rapport du CGF** (famille B)
- Période 2007-2013 ; D/tep.
- Source : rapport du 21 juillet 2014, p. 72 (déjà relevé dans `compensation-rapport-2014.md`, l. 266). Valeurs : 339 ; 517,7 ; 383,8 ; 496,4 ; 622,7 ; 799,5 ; 808.
- Couverture complète.
- Fiabilité forte. Les quantités du dénominateur sont celles du CGF : 5 375 ktep en 2012, contre 5 235 dans le rapport annuel 2012.

**3. Coût d'acquisition du gaz par tep distribuée, CGF** (famille B)
- Période 2008-2012 ; D/tep.
- Source : CGF 2014, p. 95-97. Valeurs : 514,5 ; 399 ; 506,8 ; 633,5 ; 796,3.
- Couverture complète. Fiabilité forte.

**4. Gaz algérien acheté pour la STEG, valeur FOB** (famille A')
- Période 2005, 2008-2014 ; $/tep (calculé sauf 2011-2012, que l'ETAP écrit).
- Source : ETAP RA 2005 (124 M$ pour « 568 Mille Tonnes ») ; RA 2009 (2008 : 553 M$ pour 1 207 ktep) ; RA 2010 p. 58 (2009 : 307 / 1 117 ; 2010 : 382 / 1 053) ; RA 2012 p. 63 (« 482,708 $/tep » en 2011 ; « 546,300 $/tep » en 2012, 1 413 MDT) ; RA 2014 p. 78 (2013 : 1 060,20 M$ / 2 044,181 ktep ; 2014 : 1 342,92 M$ / 2 633,152 ktep).
- Trous : 2006 et 2007. Le rapport 2006 n'a pas de couche texte, le PDF 2007 est endommagé.
- Fiabilité forte. Ce sont les achats contractuels et additionnels ; la redevance est exclue.

**5. « Prix d'importation du gaz algérien »** (famille B, ONE)
- Période 2013-2025 ; DT/tep PCS.
- Source : Mémento 2014 p. 35 (2013 : 853,1 ; 2014 : 874,5) ; Conjoncture déc. 2016 p. 30 et Mémento AR 2016 p. 38 (2015 : 640,3 ; 2016 : 424,8) ; Chiffres clés 2018-2025.
- Couverture complète.
- Fiabilité forte, mais l'ONE et la STEG partagent la même origine (voir § 3).

**6. Prix de cession du gaz à la STEG** (familles B, A et C)
- Valeur 90,8 DT/tep sur 1993-2014.
- Sources : CGF p. 7, 22 et 178 (décision du 8 octobre 1993) ; ANER 2000 p. 29 (1999) ; états financiers STEG 2014 note 11 p. 23 ; ONE Mémento 2014 p. 35 (2013-2014).
- Couverture : un prix fixe, constant sur toute la période.
- Fiabilité forte. L'acte de 1993 n'est pas identifié.

**7. Gaz tunisien vendu par l'ETAP à la STEG** (famille A')
- 2016-2019 et 2021-2024 : $/tep, M$ et MDT.
- Sources : ETAP RA 2016 p. 69 (763,1 ktep ; 159,847 $/tep ; 263,4 MDT) ; RA 2017 p. 61 (704,4 ; 224,900 ; 383,9) ; RA 2018 p. 76 (712,7 ; 291,273 ; 552,1) ; RA 2019 p. 76 (597,3 ; 288,113 ; 566,7) ; RA 2021 p. 59 (831,7 ; 280,330 ; 233,16 M$) ; RA 2022 p. 61 (1 026,8 ; 424,505 ; 435,9 M$) ; RA 2023 p. 54 (1 150,3 ; 377,612) ; RA 2024 p. 61 (877,9 ; 376,072).
- Couverture : la même série avec les quantités seules sur 2009-2014 (529 ; 826 ; 802 ; 882 ; 960,2 ; 928,0). 2015 et 2020 manquent : le rapport 2015 n'a pas de couche texte, le rapport 2020 est introuvable (404).
- Fiabilité forte. Le prix est donné champ par champ.

**8. Importations de la Tunisie en provenance d'Algérie, position SH 271129** (famille D)
- Période 1995-2024 ; M$, et $/tep si l'on divise par les ktep achetés selon la STEG.
- Source : UN Comtrade, API « preview », consultée le 17/10/2026.
- Couverture : valeur complète ; prix implicite calculé pour 2005 et 2007-2021.
- Fiabilité faible. La Tunisie déclare ce gaz en **271129**, pas en 271121. Les poids nets sont inutilisables à partir de 2016, et avant 1999. La valeur de 2004 est aberrante (20,5 M$).

**9. Prix implicite d'achat du gaz** (famille E, sur des termes de famille A)
- 2005 : 180,3 ; 2007 : 374,5 ; 2008 : 545,2 ; 2019 : 933,2 (DT/tep).
- Termes : facture des combustibles (RA 2005 p. 57 ; RA 2008 p. 4 et p. 56 ; RA 2019 p. 10) ÷ prélèvements de gaz (RA 2005 p. 26 ; RA 2007 p. 29 ; RA 2008 p. 33 ; RA 2020 p. 37).
- Couverture ponctuelle. Fiabilité moyenne : le numérateur inclut le fuel, et 2005 est antérieur à la valorisation au prix international.

**10. Redevance du gazoduc valorisée** (famille E sur des termes de famille B)
- Un seul point : 2015, 429 DT/tep. Les 115 MDT dus « sur les quantités livrées à la STEG » (rapport semestriel du ministère des Finances, fin décembre 2015, p. 18) sont divisés par 268 ktep (RA STEG 2015 p. 36).
- Fiabilité faible : il s'agit du dû, et les dates d'encaissement sont décalées.

### Quantités

**11. Prélèvements de gaz par la STEG, par source** (famille A)
- Période 2001-2024 ; ktep PCS.
- Sources : RA 2005 p. 26 et 48 ; RA 2007 p. 9 et 29 ; RA 2008-2021 (bilan national du gaz et tableaux « prélèvements ») ; RA 2023 p. 32-33 et RA 2024 p. 32-33, lus à l'image.
- Couverture : 2022 n'a pas de rapport annuel ; ses valeurs sont tirées de la colonne 2022 du RA 2023.
- Fiabilité forte.
- Détail disponible : achats contractuels et additionnels, redevance totale et consommée, Miskar, total national. Le « total des achats gaz » (dénominateur de la série 1) est publié pour 2019-2024.

### Coût de revient du kWh

**12. Coût de revient du kWh, comptes de la STEG** (famille A)
- Période 2013-2016 ; millimes/kWh distribué.
- Sources : états financiers 2014 p. 7 (2013 : 266 ; 2014 : 273,8) ; 2015 p. 8, OCR (222,7) ; 2016 p. 7 (résultat +4,7, soit 177,4 calculé ; l'exercice 2015 y est révisé à −33, soit 218,4).
- Couverture complète sur 2013-2016.
- Fiabilité forte. Ces chiffres ne sont plus imprimés après 2016.

**13. Coût de revient du kWh, ONE** (famille B)
- 2015-2018 et 2022-2025 ; millimes/kWh.
- Sources : Mémento AR 2016 p. 38, lu à l'image (2015 : 218,4 ; 2016 : 175,7) ; Chiffres clés 2018 p. 41, lu à l'image (2017 : 235,5 ; 2018 : 285,9) ; Chiffres clés 2023-2025 (471,9 ; 472,2 ; 480,9 ; 456,3).
- Trou : 2019-2021 ne sont pas publiés.
- Fiabilité forte. Ce sont des données « provisoires avant audit » à partir de 2022.

**14. Coût unitaire du kWh par composante, CGF** (famille B)
- Période 2008-2012 ; millimes/kWh.
- Source : CGF 2014, p. 73-76. Combustibles 138,1 → 204,6 ; coût total 179 → 259,6.
- Couverture complète.
- Fiabilité forte. Le débat national de 2013 (p. 32) reprend 180, 211 et 259 pour 2010-2012 ; c'est la même origine, la STEG.

**15. Coût de revient du kWh, BAD** (famille C)
- Période 2000-2004 ; millimes/kWh. Valeurs : 72,5 ; 73,8 ; 72,6 ; 79,0 ; 78,4.
- Source : BAD, rapport d'achèvement Électricité VI, tableau 4.4.1 (déjà noté dans `compensation-tarifs-1993-2004.md`, l. 132).
- Fiabilité moyenne. Le gaz y est au prix administré.

**16. Prix de revient moyen du kWh, ANER** (famille C)
- 1996 : environ 66,5 ; 1997 : environ 63,5 ; 1998 : environ 61,5 (millimes/kWh).
- Source : ANER, avril 2000, p. 36 du document (PDF p. 37). **Lu sur graphique, à ±1 millime près.** Le graphique donne aussi le détail HT, MT et BT.
- Fiabilité faible : lecture sur graphique.

**17. Coût marginal de long terme, Banque mondiale** (famille C)
- Un seul point : 1997, 78 millimes/kWh.
- Source : rapport d'achèvement (ICR) n° 17374, tableau 1.9, p. 11.
- Ce n'est pas un coût comptable.

### Coût de revient de la tep de gaz distribuée

**18. Coût de revient de la tep de gaz** (familles A et B)
- 2008-2018 et 2022-2025 ; DT/tep.
- Sources : CGF p. 95 (2008-2012 : 542,5 ; 428,4 ; 539,3 ; 667,1 ; 827,2) ; états financiers 2014 p. 7 (2013 : 856,1 ; 2014 : 858,7), 2015 p. 8 (662,6), 2016 p. 7 (461,9) ; ONE (2017 : 638,1 ; 2018 : 864,3 ; 2022-2025 : 1 545,9 ; 1 777,9 ; 1 622,8 ; 1 497,7).
- Trou : 2019-2021.
- Fiabilité forte.

### Prix de vente moyen hors taxes

**19. Prix de vente moyen HT, électricité et gaz**
- Électricité, 1994-2025 sans 2013 manquant : ESMAP 1994-1999 ; BAD 1999-2004 ; BAD rapport d'achèvement Électricité VII, annexe 3 p. 1, 2005-2010 (84,0 ; 92,1 ; 95,7 ; 113,4 ; 121,0 ; 125,0) ; CGF 2008-2012 ; ONE 2013-2025 (147,0 ; 179,1 ; 185,4 ; 182,1 ; 189,6 ; 206,3 ; 244,0…).
- Gaz : CGF 2008-2012 ; ONE 2013-2025 (341,7 ; 421,2 ; 439,5 ; 434,8 ; 460,4 ; 508,0…).
- Familles A, B et C selon le segment ; fiabilité forte.
- Le Mémento AR 2016, p. 38, imprime pour le gaz en 2016 des prix moyenne pression 586,4 et basse pression 630,4, supérieurs à la moyenne de 434,8. C'est vérifié à l'image : ces chiffres sont incohérents dans la source même.

### Achats d'électricité et cession de gaz entre activités

**20. Achats d'électricité** (famille A)
- 2017-2023 ; MDT. Valeurs : 459,2 ; 492,6 ; 544,6 ; 576,6 ; 821,1 ; 827,8 ; 791,2.
- Source : états financiers, note II-3 (2018 p. 43 ; 2019 p. 35 ; 2021 p. 37 ; 2022 et 2023 p. 35).
- Fiabilité forte. La ligne mêle les producteurs indépendants (CPC) et les importations de SONELGAZ et de GECOL : le RA 2024 p. 35 parle d'« achats auprès de SONELGAZ et GECOL ». **Ne pas la diviser par les GWh de la CPC.**

**21. « Cession fournie » du gaz aux centrales** (famille A)
- 2016-2023 ; MDT, au « prix coûtant ». Valeurs : 1 261,3 ; 1 887,6 ; 2 717,2 ; 3 379,3 ; 2 136,2 ; 2 599,2 ; 5 584,4 ; 5 362,0.
- Source : états de résultat par activité des états financiers (2017 p. 43 ; 2018 p. 50 ; 2019 p. 40 ; 2021 p. 44 ; 2022 et 2023 p. 42).
- Fiabilité forte. C'est la base d'un coût du combustible par kWh, à construire (§ 3).

### Facture des combustibles et poste « Achats »

**22. Facture des combustibles** (famille A)
- 2005, 2007, 2008, 2013-2023 ; MDT.
- Valeurs : 652 ; 1 441 ; 2 315,4 ; puis 4 426,3 ; 4 600,8 ; 3 255,4 ; 2 093 ; 3 160,7 ; 4 567,8 ; 5 416,3 ; 3 411,1 ; 4 147,9 ; 8 065,3 ; 7 565,6.
- Trous : 2006 et 2009-2012.
- Fiabilité forte.

**23. Poste « Achats » du coût des ventes** (famille A)
- 2004-2016 ; MDT. Source : rapports annuels, tableaux du « coût des ventes ».
- Fiabilité forte. **Ne pas diviser par des ktep** : le poste comprend l'électricité achetée et les matières.

### Coût du combustible au kWh et ordres de grandeur d'études

**24. Coût du combustible au kWh** : seule la série CGF 2008-2012 existe (série 14, ligne « combustibles »). Aucune série par filière ou par technologie n'a été trouvée.

**25. Prix « non subventionné » de l'électricité** (famille C, évaluation)
- Un seul point : mai 2014, 0,268 TND/kWh.
- Source : Banque mondiale, WPS 7312 (2015), tableau 3, p. 10-11. Méthode de l'écart de prix : prix international de référence fourni par la Direction générale de l'énergie, plus taxes et coûts de distribution.

---

## 2. Les trous, et pourquoi

### Prix d'achat du gaz
- **Avant 1993** : rien n'a été trouvé.
- **1993-2006** : un prix administré unique, 90,8 DT/tep, pour le gaz algérien et la redevance. Pour le gaz national, une formule indexée sur le fuel :
  - décret n° 2000-1027 du 15 mai 2000 (JORT n° 40, p. 1107, lu à l'image) : P = (80 % × FBTS) × TM/Kcal, où FBTS est le fuel à 1 % de soufre FOB Med Italy (Platts), en moyenne sur les neuf mois précédents ;
  - l'ANER (p. 29) donne une version différente : 0,85 × fuel HTS pour Miskar, 0,80 × fuel HTS pour Franig et Baguel. Ce désaccord est à signaler, non à trancher. Le coefficient de Miskar vient sans doute de sa convention propre ;
  - aucun modificatif n'est identifié, mais la recherche est insuffisante depuis 2011 (fiche proposée au § 4).
- **Coût moyen d'acquisition avant 2007** : seulement 2005 (calcul, 180 DT/tep) et la valeur FOB de l'ETAP pour 2005 (218 $/tep).
- **2006-2007** : rapport ETAP 2006 sans couche texte, rapport ETAP 2007 endommagé (xref). Le rapport annuel STEG 2006 est **en arabe**, et le seul modèle arabe de Tesseract est dans `~/projets/PDFs-legislation-tunisie/tessdata` ; je ne l'ai pas utilisé. Comtrade permet un ordre de grandeur pour 2007 (283 $/tep).
- **2024-2025** : les états financiers 2024 sont introuvables (404 sur `etat_financier_2024.pdf` et quatre variantes). Le RA 2024 donne les quantités (total des achats 5 123 ktep) mais pas la facture.
- **2009-2012, facture des combustibles** : les rapports annuels ne la donnent pas, et les états financiers d'avant 2014 sont absents du site (404 pour 2012 et 2013). Le prix est connu par le CGF.

### Coût de revient du kWh
- **Avant 1996** : rien.
- **1999** : rien.
- **2005-2007** : ni la BAD (rapport Électricité VII : « we did not undertake financial calculations »), ni le CGF, ni les états financiers.
- **2019-2021** : l'ONE ne les publie pas et les états financiers ne les impriment plus. On peut les reconstituer à partir des comptes par activité (§ 3, raccord 6), mais ce serait une évaluation.
- **Par filière** (vapeur, cycle combiné, turbines à combustion, éolien, hydraulique, producteurs indépendants) : aucune série publiée n'a été trouvée.
  - Seuls éléments : la consommation de gaz des centrales par type d'équipement (RA 2024 p. 35 : turbines à combustion 719, cycles combinés 2 687, turbines à vapeur 113 ktep en 2024), la consommation spécifique (EF 2014 et 2015 : 240,3 puis 228,9 tep/GWh) et la production par équipement (EF 2015 p. 7).
  - Pas de coût moyen actualisé tunisien publié et vérifié dans cette passe : la BAD 2021 (diagnostic) ne donne de coûts actualisés que pour le photovoltaïque en autoproduction ; IRENA 2021 et GIZ n'ont pas été ouverts.

### Coût de revient du gaz
- Trous : 2019-2021, et tout ce qui précède 2008.

### Rapports de la STEG 2006, 2022, 2023, 2024
- **2006** : en arabe, seulement des images.
- **2022** : le rapport annuel est absent de tunisia-data. Je ne l'ai pas cherché en ligne.
- **2023 et 2024** : seulement des images. J'ai lu à l'image les pages du gaz (p. 32-35). L'OCR complet a été arrêté : la machine était trop chargée pour qu'il aboutisse.

---

## 3. Raccordements

### Raccordables sans réserve
1. **Prix de vente moyen HT de l'électricité, 1994-2025.** Tous les segments sont hors taxes, en moyenne toutes tensions, et la source primaire est toujours la STEG :
   - ESMAP 1994-1999 ;
   - BAD 1999-2004 ;
   - BAD Électricité VII 2005-2010 ;
   - CGF 2008-2012 ;
   - ONE 2013-2025.

   Les chevauchements concordent au dixième près : 2008 donne 113,4 dans la BAD et le CGF, 2009 donne 121,0 dans les deux.
2. **Prélèvements de gaz par source, 2001-2024** : même tableau STEG d'année en année.
3. **Coût de revient du kWh, 2013-2018 puis 2022-2025.** Les états financiers de la STEG (2013-2016) et l'ONE (2015-2018, 2022-2025) ont la même origine : 2015 vaut 218,4 dans l'ONE comme dans les états financiers 2016. **Il faut les présenter comme une seule source, la STEG, reprise par l'ONE, et non comme deux sources qui se confirment.** Attention aux millésimes : les états financiers 2015 donnent 222,7 pour 2015, ceux de 2016 donnent 218,4.

### Raccordables avec réserve
4. **Prix d'importation du gaz algérien, 2005-2025.** On raccorde l'ETAP en $/tep (2005, 2008-2014) à l'ONE en DT/tep PCS (2013-2025).
   - Même définition : achats contractuels et additionnels, FOB, redevance exclue.
   - Même base : les quantités de l'ETAP et de la STEG concordent à l'unité (1 644,209 et 1 644 ; 2 633,152 et 2 633), et l'ONE précise « PCS ».
   - Contrôle sur 2013 : 518,6 $/tep × 1,6254 (taux du CGF, p. 72) = 842,9, contre 853,1 à l'ONE, soit −1,2 %.
   - Contrôle sur 2014 : 510,0 × 1,70 (« Moyenne 2014 », ONE Conjoncture septembre 2015, p. 29) = 867, contre 874,5, soit −0,9 %.
   - L'ETAP donne aussi des montants en DT : 800,6 MDT / 1 164 = 687,8 DT/tep en 2011, et 1 413 / 1 644,2 = 859,4 DT/tep en 2012.
   - **Conditions** : convertir chaque année avec un taux de change sourcé (BCT), sans aucune conversion non citée ; 2006-2007 restent vides, ou Comtrade en famille séparée.
5. **Prix moyen d'achat de la tep, toutes sources confondues.** On raccorde le CGF (2007-2013) aux états financiers de la STEG (2013-2023). En 2013, les deux valent 808 et 804,4, soit 0,4 % d'écart. Réserve : les dénominateurs diffèrent un peu (CGF 5 375 ktep en 2012, rapport annuel 5 235).
6. **Coût du combustible au kWh, 2008-2023 : à construire, en évaluation.** La série du CGF (combustibles 138,1 → 204,6 millimes/kWh, 2008-2012) se prolonge peut-être par « cession fournie » ÷ production des centrales STEG. Condition : vérifier d'abord que la méthode reproduit 2008-2012. Je ne l'ai pas fait faute de temps ; les GWh sont dans les rapports annuels.

### Non raccordables : ruptures à marquer
7. **Coût de revient du kWh avant et après 2007.** Les séries ANER 1996-1998 (environ 61-66) et BAD 2000-2004 (72-79) valorisent le gaz au prix administré de 90,8. Le CGF à partir de 2008 (179) et l'ONE le valorisent au prix international. **Aucun chaînage n'est possible.** Il faut des segments séparés, avec la rupture expliquée par la note 11 des états financiers 2014.
   - Avant 2007, l'écart ne va pas toujours dans le même sens. Selon l'ANER, en 1999 le prix de 90,8 est **supérieur** au prix d'acquisition algérien, de 28 DT/tep. En 2005, le prix FOB d'environ 218 $/tep lui est très supérieur.
   - On ne peut donc pas parler de « subvention » pour toute la période d'avant 2007.
8. **Prix moyen d'achat de la STEG et prix d'importation de l'ONE.** **Ne pas les superposer comme une même grandeur.**
   - De 2018 à 2020 ils sont proches : 805,5 contre 863,5 ; 933,2 contre 977 ; 622,7 contre 626.
   - À partir de 2021 le prix de la STEG passe **au-dessus** : 719,5 contre 697 ; 1 471,6 contre 1 335 ; 1 423,9 contre 1 321.
   - Les définitions diffèrent : le prix STEG porte sur tous les combustibles et toutes les sources (dont la redevance, le gaz national et les condensats), le prix ONE sur l'importation seule.
   - Les notes des états financiers n'expliquent pas l'inversion. Je ne l'explique pas.
9. **Comtrade et ETAP.** Ils concordent en 2012 (+3 %), 2013 (−3 %) et 2014 (environ 0 %), mais s'écartent de −16 % en 2011 et de −18 % en 2005. Comtrade sert seulement d'ordre de grandeur pour combler 2006-2007, dans un tableau à part. Ce n'est jamais une série de prix : le poids est incohérent, et le prix implicite n'existe qu'en le divisant par les ktep de la STEG.
10. **Subvention d'exploitation de la STEG et subvention budgétaire.** Jusqu'en 2014, la première comprend la subvention indirecte (le gaz). En 2015 elle est égale au budget (858). C'est la rupture de 2015 déjà documentée (`compensation-rupture-2015.md`), désormais **fondée sur la note II-2 des états financiers 2014**.
11. **Redevance du gazoduc, montant budgétaire ÷ ktep.** Ce n'est pas un prix. Seul 2015 est calculable (429 DT/tep sur le dû propre à la STEG). Avant 2015, la part de la STEG est cédée à 90,8 DT/tep et la recette mêle la part exportée et des encaissements décalés.

---

## 4. Passes et fiches à verser au registre (`docs/recherches.yml`)

Je n'ai rien écrit dans le dépôt. Le registre ne contient ni `r-steg-cout-de-revient-avant-2017` ni `r-arrete-1993-10-08-prix-gaz-steg` (vérifié avec `scripts/recherches.py lister`) : elles ne vivent que dans les notes. Les fiches ci-dessous sont à **créer**.

### a) `r-steg-cout-de-revient-avant-2017` (à créer, reprise de la note)
- **Objet** : coût de revient du kWh et de la tep de gaz de la STEG avant 2017 et pour 2019-2021.
- **Où** : états financiers de la STEG ; rapports annuels de la STEG ; ONE ; rapports de la BAD et de la Banque mondiale ; CGF.
- **Requêtes lancées le 17/10/2026** :
  - Python `re` sur les couches texte des RA STEG 2005-2021 : « coût de revient », « prix moyen d'achat », « facture », « achats de combustible », « Achats » ;
  - téléchargement de `steg.com.tn/system/files/pdf/etat_financier_{2012…2025}.pdf` : présents 2014 à 2023 ; 404 pour 2012, 2013, 2024 et 2025, et pour quatre variantes de nom en 2024 ;
  - motifs `co[uû]t de revient|prix de vente moyen|résultat (bénéficiaire|déficitaire)` sur les pages de faits marquants des états financiers ;
  - OCR en français des p. 4 à 9 des états financiers 2015 ;
  - recherche web « STEG coût de revient kWh 2005 2006 2007 BAD » et « African Development Bank STEG cost price kWh » ;
  - rapport d'achèvement BAD Électricité VII par Wayback, capture 20230817001921 (afdb.org renvoie 403).
- **Résultat** : trouvé 2013-2016 (états financiers), 2015-2018 (ONE), 1996-1998 (ANER, graphique). Restent 2005-2007, 2019-2021 et tout ce qui précède 1996.
- **Couverture** : états financiers 2014-2023 lus en couche texte, sauf 2015 (OCR) et 2020 (sans couche texte, non lu). Rapports d'achèvement BAD d'Électricité VI et VII seulement.
- **Couvert jusqu'au** : 2026-10-17.
- **iort_ar** : سعر التكلفة ; كلفة الإنتاج ; كلفة الكيلوات ساعة ; الغاز الجزائري ; سعر الإحالة. Ces termes sont à contrôler au glossaire.

### b) `r-arrete-1993-10-08-prix-gaz-steg` (à créer, reprise de la note)
- **Objet** : décision du ministre de l'économie nationale du 8 octobre 1993 fixant à 90,8 D/tep le prix de cession du gaz à la STEG.
- **Requêtes** : celles qui sont déjà décrites dans `compensation-rupture-2015.md`, l. 149.
- **Passe nouvelle** : aucune. Il faut ajouter comme sources indirectes l'ANER 2000 (p. 29) et les états financiers STEG 2014 (note 11, p. 23). Elles confirment la valeur, mais ni la date ni l'acte.

### c) `r-prix-gaz-commercial-concessions-apres-2000` (nouvelle)
- **Objet** : texte modifiant ou remplaçant le décret n° 2000-1027 du 15 mai 2000, qui fixe le prix du gaz commercial des concessions, et conventions particulières de prix, dont Miskar à 0,85 × fuel HTS selon l'ANER.
- **Où** : jort_cache, fascicules du JORT, rapports de l'ETAP.
- **Requêtes lancées le 17/10/2026** :
  - titres_fts `"gaz commercial" OR (prix AND gaz AND concessions) OR (gaz AND algerienne AND (redevance OR prelevement OR transport))`, toutes années. Résultat : seul le décret 2000-1027, plus les textes de transit (loi n° 2005-102, décrets 2006-458, 2006-1823/1824, 2006-3265, 2007-2194, 2007-2378/2379) ;
  - titres LIKE en arabe : `%غاز%` et (`%سعر%`, `%أسعار%`, `%أتاوة%`, `%إتاوة%`). Résultat : loi n° 2019-71 et décret gouvernemental n° 2019-824 (redevance de transit), aucun texte de prix.
- **Couverture** : intitulés seulement ; le plein texte n'a pas été parcouru. Il faut ajouter en `iort_ar` : « سعر الغاز التجاري », « لزمات استغلال المحروقات », « المنتج انطلاقا من لزمات ».
- **Couvert jusqu'au** : 2026-10-02 (dernière publication dans jort_cache).
- **Résultat** : aucun.

### d) `r-etap-achats-gaz-algerien-2006-2007` (nouvelle)
- **Objet** : valeur FOB et prix du gaz algérien acheté pour la STEG en 2006 et 2007.
- **Requêtes** : téléchargement de `etap.com.tn/storage/downloads/annual reports/{2005…2009}/RA-<année>-fr.pdf`. 2006 : 66 pages sans couche texte. 2007 : PDF endommagé (pdftotext échoue ; `mutool` répare la table xref mais je n'ai pas extrait le texte).
- **Lacune** : OCR du rapport 2006 et réparation du 2007 à faire.
- **Résultat** : aucun. **Couvert jusqu'au** : 2026-10-17.

### e) `r-steg-etats-financiers-2024` (nouvelle)
- **Objet** : états financiers 2024 de la STEG (prix moyen d'achat, facture du gaz).
- **Requêtes** : cinq variantes d'adresse, toutes en 404 le 17/10/2026.
- **Résultat** : aucun.

---

## 5. Références candidates (CSL minimal)

### Déjà présentes dans `precis/fr/compensation/references.json`
`steg-ra-2007` à `steg-ra-2021`, `one-chiffres-cles-energie`, `one-conjoncture-energetique`, `bad-2006-rap-electricite-vi`, `bm-1998-icr-17374`, `esmap-2005-307-electrification-rurale`, `bm-2015-wps7312`, `bm-2013-82712`.

### À créer

```json
{"id":"steg-ef-2014","type":"report","title":"États financiers de l'exercice 2014","author":[{"literal":"Société tunisienne de l'électricité et du gaz"}],"issued":{"date-parts":[[2015]]},"URL":"https://www.steg.com.tn/system/files/pdf/etat_financier_2014.pdf","note":"Note 11 p. 23 (prix fixe de 90,800 DT, subvention indirecte comptabilisée depuis 2007) ; note II-2 p. 35 ; faits marquants p. 7"}
```

Pour 2015 à 2023, même modèle : `steg-ef-2015` … `steg-ef-2023`, URL `etat_financier_<année>.pdf`. Pages utiles :
- 2015 : p. 7-8 (OCR) ;
- 2016 : p. 7 et 35 ;
- 2017 : p. 7, 38 et 43 ;
- 2018 : p. 8, 43 et 50 ;
- 2019 : p. 5, 35 et 40 ;
- 2021 : p. 7, 37 et 44 ;
- 2022 : p. 3, 35 et 42 ;
- 2023 : p. 3, 35 et 42.

Rapports annuels STEG à créer sur le même modèle que `steg-ra-*` :
- `steg-ra-2005` : `https://www.steg.com.tn/system/files/pdf/Rap_STEG_2005.pdf` ;
- `steg-ra-2023` et `steg-ra-2024` : leurs adresses ne sont pas relevées dans cette passe. Les fichiers sont dans tunisia-data sans ligne de catalogue (voir plus bas) ; l'adresse d'origine est à reprendre de la note de collecte.

Autres références :

```json
{"id":"etap-ra-<année>","type":"report","title":"Rapport annuel <année>","author":[{"literal":"Entreprise tunisienne d'activités pétrolières"}],"URL":"https://www.etap.com.tn/storage/downloads/annual%20reports/<année>/RA-<année>-fr.pdf"}
```
Années utiles : 2005, 2009, 2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024.

```json
{"id":"cgf-2014-subvention-carburants","type":"report","title":"Rapport sur le système de subvention des carburants (STEG, STIR, ETAP)","author":[{"literal":"Tunisie. Contrôle général des finances (هيئة الرقابة العامة للمالية)"}],"issued":{"date-parts":[[2014,7,21]]},"language":"ar","note":"mission n° 42 du ministre des Finances du 16 septembre 2013 ; pp. 7, 22, 72-76, 95-97, 178"}
```
Cette clé est à aligner sur celle que la note de lecture `compensation-rapport-2014.md` n'a pas encore fixée.

```json
{"id":"bad-2012-pcr-electricite-vii","type":"report","title":"Republic of Tunisia. Electricity Distribution Network Rehabilitation Project (Electricity VII). Completion Report","author":[{"literal":"Banque africaine de développement"}],"issued":{"date-parts":[[2012,3]]},"URL":"https://web.archive.org/web/20230817001921/https://www.afdb.org/fileadmin/uploads/afdb/Documents/Project-and-Operations/Tunisia-(P-TN-FAC-002)-PCR_-_Electricity_Distribution_Network_Rehabilitation_Project__(Electricity_VII.pdf","note":"annexe 3 p. 1, tableau II (prix moyens HT 2005-2010)"}
```

```json
{"id":"aner-2000-impact-prix-energie","type":"report","title":"Étude de l'impact des prix de l'énergie sur la demande","author":[{"literal":"Agence nationale des énergies renouvelables"}],"issued":{"date-parts":[[2000,4]]},"note":"p. 29 (prix du gaz à la STEG : 90,8 DT/tep, formules Miskar et Franig-Baguel) ; p. 36 (graphique prix de revient et prix de vente 1996-1998)"}
```
Le titre exact est à relire sur la couverture, et l'adresse d'origine est à compléter.

```json
{"id":"decret-2000-1027","type":"legislation","title":"Décret n° 2000-1027 du 15 mai 2000, fixant le prix du gaz commercial écoulé sur le marché local par les titulaires de concessions d'exploitation d'hydrocarbures","number":"2000-1027","issued":{"date-parts":[[2000,5,15]]},"container-title":"Journal officiel de la République tunisienne","issue":"40","page":"1107"}
```
L'adresse pist.tn de l'édition française est à relever.

```json
{"id":"one-memento-2014","type":"report","title":"Mémento de l'énergie 2014","author":[{"literal":"Observatoire national de l'énergie"}],"note":"p. 35 (prix de cession à la STEG 90,8 ; prix d'importation 2013-2014)"}
```
Même modèle pour `one-memento-2016-ar` (p. 38).

```json
{"id":"minindustrie-2013-debat-national-energie","type":"speech","title":"Débat national sur l'énergie (présentation)","author":[{"literal":"Ministère de l'Industrie"}],"issued":{"date-parts":[[2013,6,27]]},"note":"p. 32 (coût de revient et prix de vente 2010-2012)"}
```

```json
{"id":"uncomtrade-tun-dza-2711","type":"dataset","title":"UN Comtrade, importations de la Tunisie en provenance d'Algérie, SH 2711 (6 chiffres)","author":[{"literal":"Nations unies, division de statistique"}],"URL":"https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=788&partnerCode=12&flowCode=M&cmdCode=AG6","accessed":{"date-parts":[[2026,10,17]]}}
```

### Rangé dans tunisia-data (non commité, à relire)
- `data/raw/minenergie/steg/etats-financiers/steg_ef_2014.pdf` … `steg_ef_2023.pdf` (sans 2024) ; catalogue **nouveau, non suivi** : `/home/benjello/projets/tunisia-data/sources/minenergie-steg-urls.csv` (10 lignes, SHA-256).
- `data/raw/entreprises-publiques/etap/etap_ra_{2005-2019,2021-2024}.pdf` ; **19 lignes ajoutées** à `/home/benjello/projets/tunisia-data/sources/entreprises-publiques-urls.csv` (SHA-256, état de chaque PDF).
- `data/raw/banque-mondiale-rapports/afdb_2012_electricity_vii_pcr_en.pdf` ; **1 ligne ajoutée** à `/home/benjello/projets/tunisia-data/sources/banque-mondiale-rapports-urls.csv`. Ce catalogue n'a pas de colonne sha256 : l'empreinte est dans le champ titre.
- **Fichiers présents mais sans ligne de catalogue, à rattraper** : les rapports annuels STEG 2005-2024 (`data/raw/minenergie/steg/rapports-annuels/`), `afdb_2006_electricity_vi_pcr_en.pdf`, `afdb_2006_electricite_vi_rap_fr.pdf`, `aner_2000_*`, `one_*`.

---

## 6. À demander en priorité à la STEG, à l'ONE et à l'ETAP

### STEG (direction centrale des finances, comptabilité analytique)
1. **États financiers avec notes de 2005 à 2013 et de 2024.**
   - *Publié* : 2014-2023 en ligne ; rapports annuels sans notes de 2005 à 2021, puis 2023 et 2024.
   - *Non publié* : notes d'avant 2014, et l'exercice 2024.
2. **Prix moyen d'achat de la tep, ventilé par source** (gaz algérien contractuel, additionnel, redevance, gaz national, condensats), en quantité et en valeur, de 2000 à 2025.
   - *Publié* : la moyenne seule, de 2013 à 2023.
3. **Coût de revient du kWh distribué et de la tep distribuée**, de 1990 à 2025, avec la décomposition du CGF (combustible, personnel, charges financières, amortissements, divers).
   - *Publié* : 2013-2016 dans les états financiers ; 2008-2012 par le CGF.
   - *Non publié* : 2005-2007, 2019-2021, et la décomposition hors 2008-2012.
4. **Coût du kWh par filière** (vapeur, cycle combiné, turbines à combustion, éolien, hydraulique) et **coût d'achat par fournisseur** (CPC, autres producteurs indépendants, SONELGAZ, GECOL), en MDT et en GWh.
   - *Non publié* : la ligne « achats d'électricité » est agrégée.
5. **Série retraitée cohérente avant et après 2007** : coût de revient valorisé aux deux prix, administré et international, pour 2000-2014.

### ONE (ministère de l'industrie, des mines et de l'énergie)
6. **Éditions des « Chiffres clés » antérieures à 2018 et Mémentos 2015-2017.** Je ne les ai cherchés ni sur le site ni dans les archives. *Publié en local* : le Mémento 2014 et le Mémento arabe 2016.
7. **Coût de revient 2019-2021**, absent des éditions 2019-2021.
8. **Prix d'importation du gaz algérien en $/tep et en DT/tep, mensuel**, depuis 2005. *Publié* : un graphique mensuel depuis janvier 2014 dans les Chiffres clés 2018 (p. 42) et le Mémento 2014 (p. 36), sans tableau.

### ETAP
9. **Rapports 2006, 2007, 2015 et 2020 lisibles** (2006 et 2015 sans couche texte, 2007 endommagé, 2020 introuvable). Également la **valeur des ventes de gaz tunisien à la STEG pour 2009-2014**, où seules les quantités sont publiées.
10. **Valorisation de la redevance de transit cédée à la STEG**, en quantité et en valeur, de 2000 à 2025.

---

### Notions à glossaire (à vérifier dans `precis/glossaire.yml`)
- « prix de cession » (du gaz à la STEG) : سعر الإحالة ;
- « subvention indirecte » : الدعم غير المباشر ;
- « redevance de transit » ou « forfait fiscal » (gazoduc transméditerranéen) : الأتاوة, prélèvement fiscal ;
- « coût de revient » : سعر التكلفة, la forme du Mémento ONE 2016 ;
- « prix moyen d'achat de la tep » ;
- « gaz commercial » ;
- « tep PCS ».

Source canonique pressentie : la note 11 et la note II-2 des états financiers STEG 2014 ; le CGF 2014.

### Les 23 CSV de travail
Dans `/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/15adcd5f-c210-406f-907e-f6545e1e97a0/scratchpad/steg-series/` :

- `steg_ef_prix_moyen_achat_tep_gaz.csv`
- `steg_ef_achats_combustible_electricite.csv`
- `steg_ef_cout_de_revient.csv`
- `steg_ef_cession_gaz_centrales.csv`
- `steg_ef_subvention_directe_indirecte.csv`
- `steg_prelevements_gaz_ktep.csv`
- `steg_facture_combustible_et_gaz.csv`
- `steg_prix_implicite_achat_gaz.csv`
- `steg_achats_cout_des_ventes.csv`
- `steg_subvention_vs_cgf2014_soutien_total.csv`
- `cgf2014_cout_kwh_composantes.csv`
- `cgf2014_gaz_cout_tep.csv`
- `etap_achats_gaz_algerien_fob.csv`
- `etap_ventes_gaz_tunisien_steg.csv`
- `one_prix_import_gaz_algerien.csv`
- `one_prix_vente_moyen_ht.csv`
- `one_cout_de_revient.csv`
- `prix_cession_gaz_steg.csv`
- `ext_cout_revient_kwh_avant_2005.csv`
- `ext_bad_prix_vente_moyen_2005_2010.csv`
- `comtrade_import_gaz_algerie.csv`
- `redevance_gazoduc_budget_vs_ktep.csv`
- `catalogue_lines.csv` (lignes de catalogue copiées dans tunisia-data)

Les textes extraits (pdftotext) sont dans `txt/` et `dl/`, et les réponses Comtrade brutes dans `comtrade/`. Aucun OCR ne tourne plus : j'ai arrêté mes propres processus et vérifié qu'il n'en restait aucun.

### Sources web consultées
- [STEG, états financiers 2023](https://www.steg.com.tn/system/files/pdf/etat_financier_2023.pdf)
- [STEG, états financiers 2022](https://www.steg.com.tn/system/files/pdf/etat_financier_2022.pdf)
- [ETAP, rapport annuel 2022](https://www.etap.com.tn/storage/downloads/annual%20reports/2022/RA-2022-fr.pdf)
- [ETAP, rapport annuel 2011](https://www.etap.tn/storage/downloads/annual%20reports/2011/RA-2011-fr.pdf)
- [BAD, rapport d'achèvement Électricité VII](https://www.afdb.org/fileadmin/uploads/afdb/Documents/Project-and-Operations/Tunisia-(P-TN-FAC-002)-PCR_-_Electricity_Distribution_Network_Rehabilitation_Project__(Electricity_VII.pdf), lu par la capture Wayback
- [BAD, Country Priority Plan and Diagnostic of the Electricity Sector, Tunisie](https://www.afdb.org/sites/default/files/2021/11/22/tunisia.pdf)
- [STEG, rapport annuel 2005](https://www.steg.com.tn/system/files/pdf/Rap_STEG_2005.pdf)
- [UN Comtrade, API](https://comtradeapi.un.org/public/v1/preview/C/A/HS)
