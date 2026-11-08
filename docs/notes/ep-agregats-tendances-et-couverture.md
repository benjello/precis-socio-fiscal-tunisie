# EP — agréger « comme la Présidence », repérer les tendances, et chiffrer ce qui manque

**Note de travail.** Date : 6 novembre 2026. Prolonge `ep-poc-reproduction-productivite-presidence.md`
et `ep-livre-blanc-2018-conclusions.md`. But : reproduire des agrégats du type rapport présidentiel
(revenus / résultat / masse salariale / productivité) **à partir de nos sources sourcées**, repérer
les tendances, et surtout **dire ce qu'on loupe et de combien**.

## Règle appliquée
Tout agrégat est accompagné de sa **couverture** : combien d'EP, quelle part du secteur, quelles EP
manquent. Aucune interpolation ; une valeur non lue reste vide. Un agrégat sur panel changeant est
trompeur, donc on travaille à **panel constant** et on affiche le nombre d'EP contributrices.

## 1. Ce qu'on a (source : `tunisia-data/sources/entreprises-publiques/grandeurs-productivite-ep.csv`)
19 EP, 2000-2025, **945 valeurs sourcées** (fichier + page). Couverture très inégale :
- **Bien couvert, longues séries** : secteur financier coté (BNA, STB, BH, BTE, STAR, Tunis-Re) et
  quelques industriels (Ciments de Bizerte, Sotrapil, Sotumag), + Tunisair (2000-2022), ETAP
  (revenus 2008-2023), STEG (2014-2023).
- **Grandeurs** : `revenus`, `resultat_net`, `masse_salariale` bien peuplées ; **VA** seulement pour
  5 EP (Tunisair, Ciments, Sotrapil, Sotumag, STEG).
- **Trou critique** : les **effectifs** sont quasi absents → **VA/agent (le cœur « productivité »)
  impossible à généraliser** pour l'instant.

## 2. Tendances reproductibles aujourd'hui (panel constant, couverture explicite)
### a. Panel « revenus+résultat+masse salariale » présents 2012 ET 2022
Seules **3 EP** satisfont la triple condition sans trou : **BH-Bank, Ciments de Bizerte, Tunisair**.
C'est un panel **non représentatif** (une banque + un cimentier + la compagnie aérienne) ; à ne lire
que comme illustration de méthode.

| Agrégat (MD) | 2012 | 2022 | Variation |
|---|---|---|---|
| Revenus | 1 503 | 2 626 | **+75 %** |
| Résultat net | −112 | −139 | pertes persistantes |
| Masse salariale | 271 | 402 | **+48 %** |

Ratio **masse salariale / revenus** du panel : ~16 % (2010) → ~20 % (2015-2021) → 15 % (2022).
**Tendance cohérente avec le diagnostic 2018** (masse salariale qui progresse vite, résultat qui
reste négatif), mais **sur 3 EP seulement** : valeur illustrative, pas un agrégat de secteur.

### b. Ce que vaut ce panel face au secteur (le « de combien on loupe »)
En **revenus 2018**, nos EP **non financières** présentes (Tunisair, Ciments, Sotumag, STEG, ETAP)
totalisent **≈ 7 920 MD**. Le dénominateur du ministère des Finances (ressources d'exploitation des
**71 EP non financières**, exercice 2018) est **≈ 23 907 MD** → **couverture ≈ 33 %** (concepts
proches mais non identiques : « revenus » comptables vs « ressources d'exploitation »), et cette
couverture tient presque entièrement à **STEG + ETAP + Tunisair**. Autrement dit : **on loupe environ
les deux tiers** du secteur non financier en valeur, et la quasi-totalité des EP hors « top ».

## 3. Le dénominateur et la clé des trous : le rapport annuel du ministère des Finances
Le MdF publie chaque année, **annexé à la loi de finances** (gbo.tn, millésimes **2012 → 2026**), un
**« Rapport sur les entreprises publiques »** qui donne, pour un échantillon des plus grandes EP, les
CA, effectifs, masse salariale, subventions et résultats — y compris les **grosses non cotées**
absentes de nos comptes (STIR, STEG, CPG, GCT, SNDP, Tunisie Télécom, RNTA, SONEDE, ONAS, offices…).
C'est la source qui donne à la fois **le dénominateur** et **de quoi combler**.

Repères extraits de l'annexe LF2021 (exercice **2018**), archivée dans
`tunisia-data/data/raw/entreprises-publiques/rapports-ep-loi-finances/annexe9_LF2021_entreprises_publiques.pdf` :
- **110 EP** au total ; échantillon analysé = **33 EP** (dont 3 banques, 3 caisses sociales, la Poste,
  la CPSCL, MTK, El Fouladh, Tunisie Télécom, SNCPA, + **21 EP** « les plus importantes »).
- **71 EP non financières** (exercice 2018) : ressources d'exploitation **23 907 MD**, charges
  d'exploitation **24 319 MD**, charges de personnel **2 963 MD**, effectif **89 350 agents**,
  subventions **1 790 MD**, résultats négatifs cumulés **−1 146 MD**, pertes **−2 898 MD**.
- Les **21 plus importantes** représentent **92,8 %** des ressources, **82,3 %** des charges de
  personnel et **78,6 %** des effectifs de ces 71 → **noyau de suivi** : viser ces 21 EP couvre
  l'essentiel du secteur non financier.

## 4. Inventaire des données manquantes à retrouver (backlog de récupération)
Priorité haute (grosses EP, fort poids de secteur, absentes ou lacunaires chez nous) :
1. **Effectifs de toutes les EP** (bloquant pour VA/agent). Source : rapports MdF annuels (narratif
   par EP) + rapports annuels des EP.
2. **STIR** : aucun état financier public (non cotée). Pistes : rapport MdF (CA, subventions
   carburants), Cour des comptes. Non recoupable autrement — lacune déjà consignée.
3. **CPG, GCT, SNDP, Tunisie Télécom, RNTA, SONEDE, ONAS, Office des céréales, TRANSTU, SNCFT,
   El Fouladh, SNCPA, OACA, CTN, Tunisie Autoroutes** : CA / résultat / effectif / subventions via
   les rapports MdF annuels (déjà partiellement lus pour 2018 dans l'annexe LF2021).
4. **Séries longues du rapport MdF** : télécharger les annexes EP **2012 → 2026** (gbo.tn ;
   Wayback Machine pour les millésimes retirés) et en extraire les tableaux d'agrégats (échantillon
   21/71) pour une **série de secteur 2010-2024** — ce que le Livre blanc ne faisait que pour 2010-2014.
5. **Rapport de l'Unité de suivi de la productivité** (source primaire des chiffres de la Présidence,
   exercices 2006 puis 2010-2014) : à localiser (Présidence du gouvernement ; cité par la Banque
   mondiale, rapport 78675-TN, 2014).

Sources déjà repérées (URL) :
- Rapports EP annexés à la LF : `http://www.gbo.tn/fr/Loi-de-Finance-et-rapports-annexes`
  (filtrer « Rapport sur les entreprises publiques », millésimes 2012-2026).
- Livre blanc 2018 (copie en ligne) : leaders.com.tn (déjà dans le corpus).
- Banque mondiale, *Pour une meilleure gouvernance des EP en Tunisie*, mars 2014 (rapport 78675-TN).

## 5. Chantier de récupération — fait le 6 novembre 2026

**Cadrage (important).** Ces rapports ne sont **pas** à reproduire : leurs tableaux de synthèse
ministériels ne sont **pas** notre produit. Ils sont une **source de données par EP** (CA, effectif,
masse salariale, résultat — y compris les grosses non cotées STIR, CPG, GCT, SNDP, Tunisie Télécom,
STEG…) qu'on extrait pour **remplir `grandeurs-productivite-ep.csv` et recalculer NOS agrégats**,
avec notre couverture. Les totaux ministériels ne servent que de **dénominateur** (dire ce qu'on loupe).

Rapports MdF « Entreprises publiques » (annexe 9 à la LF) retrouvés (gbo.tn + finances.gov.tn + Wayback)
et archivés dans `tunisia-data/data/raw/entreprises-publiques/rapports-ep-loi-finances/` :
- **LF2020** (`annexe9_LF2020_entreprises_publiques_fr.pdf`, 159 p., **français**, « Octobre 2019 »,
  exercices ~2016-2018) ;
- **LF2021** (`annexe9_LF2021_entreprises_publiques.pdf`, 179 p., **français** — exploité, exercice 2018) ;
- **LF2022** (`annexe9_LF2022_entreprises_publiques.pdf`, 128 p., **arabe** — échantillon de 50 EP, 2018-2019) ;
- **LF2024** (`annexe9_LF2024_entreprises_publiques_ar.pdf`, **arabe**) ;
- **LF2025** (`annexe9_LF2025_entreprises_publiques_ar.pdf`, **arabe**) ;
- **État des lieux des états financiers 2017-2018-2019** (`etat_des_lieux_...pdf`, 4 p.).

**Millésimes toujours absents** (hors ligne sur gbo.tn / finances.gov.tn / Wayback au 6 nov. 2026) :
**LF2012-2019, LF2023, LF2026**, et les **rapports primaires de l'Unité de suivi de la productivité**
(exercices 2006, 2010-2014 — source des chiffres du Livre blanc). Avant 2020 les rapports annuels
semblent sporadiques (un rapport en 2007, puis 2014) : le relais reste le **Livre blanc (2010-2014)**.
Les deux versions **françaises** (LF2020, LF2021) sont les plus exploitables ; les millésimes arabes
(2022, 2024, 2025) demandent une lecture bilingue.

**Prochaine étape = USAGE, pas transcription** : extraire des rapports français (LF2020, LF2021) les
valeurs **par EP** absentes de notre CSV — en priorité les **effectifs** (débloque VA/agent) et les
**grosses non cotées** (STIR, CPG, GCT, SNDP, Tunisie Télécom, STEG) — chaque valeur avec fichier +
page, puis recalculer nos agrégats et tendances sur un panel enfin proche du noyau des 21 EP.

Première série de secteur sourcée construite :
`tunisia-data/sources/entreprises-publiques/agregats-secteur-ep.csv` — une ligne par (exercice,
périmètre, indicateur), chaque valeur avec fichier + page. Contenu actuel, **confidentiel au sourçage** :
- **2010-2014** : ratios au PIB, subventions, dette, parts (Livre blanc 2018, source primaire Unité de suivi) ;
- **2018** : agrégats des 71 EP non financières et des 21 plus importantes (LF2021, Tableau 9, p. 31).

Reste à faire (consigné ici, à verser au backlog durable) :
1. **Lecture bilingue de LF2020 et LF2022** (arabe) pour en tirer les agrégats 2017-2019 (indicateurs
   globaux, top 10, échantillon de 50) — tables RTL, extraction `pdftotext` ambiguë : à relire à la
   source avant d'inscrire la moindre valeur. **Rien n'en a été versé** pour éviter une mauvaise
   affectation de colonne.
2. **Millésimes manquants** : LF2012-2019 et LF2023-2026 non encore localisés (le dépôt gbo.tn n'en
   archive que 2021-2022 ; finances.gov.tn en sert quelques-uns par pages-nœuds). Explorer la Wayback
   plus finement et le site vivant du MdF.
3. **Effectifs par EP** (bloquant VA/agent) : les rapports MdF les donnent en narratif par entreprise —
   à extraire EP par EP.

## 6. Option (b) — chasse aux états financiers des EP non cotées (6 nov. 2026)
But : amener des chiffres **absents des rapports**, en calculant la VA depuis les comptes primaires
des grandes EP non cotées. Résultat de la recherche (CMF, sites d'entreprise, Wayback) :

**Exploitable — nouveau** :
- **Tunisie Télécom** : document de référence CMF 2010
  (`data/raw/entreprises-publiques/etats-financiers-non-cotees/tunisie_telecom_doc_reference_2010.pdf`,
  555 p.). Les **Soldes Intermédiaires de Gestion** (p. 173) **posent la VA brute** :
  **771,9 (2007) → 785,0 (2008) → 820,7 (2009) MD** ; masse salariale 135,7 → 171,1 MD.
  **Part des salaires dans la VA ≈ 18-21 %**, EBITDA 50 % du CA → profil **très profitable**,
  à l'opposé de Tunisair/STEG. Valeurs sourcées dans `grandeurs-ep-non-cotees.csv`.
  Réserve : la VA est **individuelle** (société mère) ; l'effectif publié est **Groupe**
  (9 049/9 538/9 706) → VA/agent possible mais avec un écart mère/groupe à lever.
- **STEG** (déjà primaire-complet par ailleurs) et **Tunisair** : EF aussi disponibles au CMF / site propre.

**Phosphates (les deux plus gros déficitaires)** :
- **GCT** : rapport annuel 2013 PART2 (`gct.com.tn/…/GCT-ANNUAL-REPORT-2013-PART2.pdf`, archivé sous
  `etats-financiers-non-cotees/gct_rapport_annuel_2013_part2.pdf`) a une **couche texte** (44 000 car.,
  anglais) → **exploitable sans OCR**, à dépouiller. Le 2016 PART2 a renvoyé 404.
- **CPG** : `cpg.com.tn/documentation/448656.pdf` (archivé) — **scan pur** (38 car.) → **OCR requis**.
- Les « doc de référence CMF » CPG/GCT 2010 évoqués par la recherche **n'existent pas** (404) ; seul
  celui de **Tunisie Télécom** est réel.
- **Attention périmètre** (voir §7) : GCT/CPG sont **productifs** (phosphate vendu) → VA pertinente ;
  ne pas les confondre avec les offices de compensation.

**Mur OCR restant** : CPG (scan), et les millésimes GCT scannés. OCR à lancer au premier plan.

**Lacune de disponibilité (comptes audités mais non publiés)** : ODC, SONEDE, ONAS publient des
données physiques (`oc.com.tn`, open data) mais **pas leurs états financiers** ; ceux-ci existent
(audités en conseil d'administration) → source à tenter : **Cour des comptes** (monographies d'EP) ou
demande directe. Mais pour l'**ODC** (compensation), la VA serait de toute façon sans objet (§7).

**Aucun EF public exploitable** (lacune structurelle, à consigner) : **SONEDE** (seule la filiale
« SONEDE International » publie), **SNDP/AGIL**, **STIR**, **SNCFT**, **TRANSTU**, **RNTA**,
**Office des Céréales**. Pour ces EP, la productivité restera hors de portée sans obtention directe
des comptes — même mur que la STIR dans le POC.

**Diagnostic longue durée — part des salaires dans la VA, EP à VA primaire** (neuf, vérifié) :
Tunisair (2003-2022, rupture post-2011 jusqu'à >100 %), STEG (VA/agent 2014-2019 : 68k→37k DT/agent,
−57 % 2016-2018), Ciments de Bizerte, Sotrapil (~35-40 %, sain), Sotumag, et désormais
**Tunisie Télécom (2007-2009, ~18-21 %, sain)**. Deux profils nets : utilities/transport en
détérioration vs télécom/distribution profitables.

## 7. Principe de périmètre — ne pas empiler trois natures d'EP (la faille du Livre blanc)
Le Livre blanc 2018 range dans **un seul classement « revenus 2014 »** (graphique p.8) des entités de
natures incompatibles, sans le signaler :
- **STIR 4 495,7** (n°1) et **Office des Céréales 829,6** — des **offices de compensation** dont le
  « revenu » est **gonflé par le circuit de subvention** (achat/revente à prix administrés, créances
  de compensation sur l'État) ;
- **CNRPS 2 540, CNAM 2 182, CNSS 2 159** — des **caisses sociales** dont le « revenu » est en fait
  des **cotisations**, pas de la production ;
- STEG, ETAP, Tunisair, GCT, Tunisie Télécom… — des **EP productives**.
C'est pourquoi la STIR (n°1) était irrécupérable dans le POC (3 478 vs 4 495,7) : artefact de compensation.

**Règle de périmètre du diagnostic de productivité** (notre apport, non une resucée) :
1. **EP productives** (biens/services vendus sur un marché) → VA, VA/agent, part des salaires dans la VA
   ont un sens. C'est le périmètre du diagnostic.
2. **Offices de compensation** (STIR carburants, ODC céréales, et la Caisse Générale de Compensation)
   → « revenus » et « VA » **économiquement faux** : on mesurerait le circuit de subvention. À **exclure**
   du diagnostic de productivité et à traiter dans le **volet compensation**.
3. **Caisses sociales** (CNRPS, CNAM, CNSS) → ni production ni VA : relais des volets **cotisations /
   prestations / retraites**, pas de ce diagnostic.
Tout agrégat de « revenus du secteur EP » qui mélange ces trois natures (comme le Livre blanc) est
trompeur ; nos agrégats annoncent leur périmètre et s'en tiennent au type 1.

## 8. Résultats consolidés du diagnostic de productivité (EP de type 1, 6 nov. 2026)
Chiffres **calculés par nous**, depuis les comptes primaires, **absents des rapports**, périmètre
« EP productives » (§7). Sources : `grandeurs-productivite-ep.csv` (BVMT/STEG) + `grandeurs-ep-non-cotees.csv`
(Tunisie Télécom doc réf. CMF 2010 ; GCT rapport annuel 2013 ; CPG rapport annuel 2010, **OCR**).

**a) Part des salaires dans la VA (%)** — deux profils nets :
- *En détérioration* : **Tunisair** (2003-2022) ~50 % avant 2011 → 89-110 % (2011-2013) → 332 % (2020) →
  135 % (2022) ; **STEG** franchit 100 % en 2018 ; **Ciments de Bizerte** très volatil (jusqu'à 263 % en 2024).
- *Sains* : **Sotrapil** ~35-40 % (2007-2017) ; **Tunisie Télécom** ~18-21 % (2007-2009) ; **CPG 2010** ~22 %.

**b) VA par agent (DT/agent)** — niveau et trajectoire :
- **STEG** : 68k (2014) → 86k (2016) → 37k (2018) — **−57 % en deux ans** (effectif primaire).
- **GCT** : ~28,8k (2012) → 30,1k (2013) — très bas (phosphate en crise, perte −105 MD).
- **CPG** : 36k (2006) → **226k (2008, pic phosphate)** → 91k (2009) → 124k (2010) — boom-bust spectaculaire.
- **ETAP** (revenus/agent, faute de VA) : ~1,5–2,0 MDT/agent (2017-2019) — pétrole, très capitalistique.

**c) Le boom-bust du phosphate (CPG, 2006-2010)**, inexistant dans tout rapport de synthèse : VA
210→268→**1242**→460→605 MD ; résultat net 54→99→**951**→269→375 MD. Le pic 2008 domine toute la
décennie — une lecture longue durée qui disparaît dans un instantané annuel.

**Couverture** : 8 EP productives au diagnostic (Tunisair, STEG, Ciments, Sotrapil, Sotumag, Tunisie
Télécom, GCT, CPG) + ETAP en revenus/agent. **Vérification** : revenus 2014 reproduits à l'identique
contre le Livre blanc (Tunisair 1 149,6 ; STEG 3 736) ; CPG 2010 et GCT 2013 confirmés par leur propre
narratif. **Réserves** : CPG en **OCR** (valeurs marquées « à vérifier », 2008/2010 recoupées au narratif) ;
Tunisie Télécom VA individuelle vs effectif groupe ; GCT masse salariale non lue (VA/agent seul).

**Carte de disponibilité (ratissage systématique multi-canaux, 6 nov. 2026 ; Wayback hors ligne ce jour)** :
- **VA calculable, à jour** : STEG (site propre, EF → 2023), Tunisair (BVMT, 2023), Ciments/Sotrapil/Sotumag (BVMT).
- **VA calculable mais plafonnée par la publication** : GCT (rapports publics **s'arrêtent à 2014**),
  CPG (**2010**), Tunisie Télécom (**2009**). Seule voie pour du récent : **prospectus d'emprunts
  obligataires au CMF** (EF individuels+consolidés) — canal **non encore épuisé**.
- **Piste chaude** : **ETAP** publie des « Rapports financiers » sur `etap.com.tn` (site hors ligne au test) ;
  s'il porte l'état de résultat → VA d'ETAP (on n'a que ses revenus). À re-tester.
- **VA NON calculable publiquement — mais comptes existants** (à ne pas dire « sans comptes ») :
  **SONEDE, ONAS, SNCFT, TRANSTU, CTN, STIR, SNDP/AGIL, RNTA**. Leurs comptes sont **audités** et des
  **indicateurs partiels sont publics** (CA, résultat, effectif via l'**Annexe 9 LF** et les monographies
  de la **Cour des comptes**), mais le **détail achats consommés / charges externes** nécessaire à la VA
  **n'est pas en ligne**. Les filiales (SONEDE International, STEG International Services) ne sont PAS les
  comptes des mères.
- **ODC** : exclu **par nature** (compensation, §7), pas par indisponibilité.

**Canaux restant à épuiser avant toute conclusion définitive** : CMF **bulletins officiels** (émissions
obligataires des EP mères → prospectus avec EF) ; **Cour des comptes** dépouillée page à page ;
**gbo Annexe 9 LF2024/2025** (arabe) ; Wayback (hors ligne ce jour) ; re-test ETAP.

## 9. Ratissage CMF — constat définitif + extension STEG (6 nov. 2026)
**Le CMF ne débloque pas le récent des EP mères.** Les grandes EP opératrices (STEG, SONEDE, ONAS,
GCT, CPG, ETAP, SNDP, SNCFT, TRANSTU, STIR, RNTA, ODC) **ne font pas d'appel public à l'épargne** :
leurs emprunts obligataires sont **garantis par l'État et placés sans APE**, donc **sans visa ni dépôt
au CMF**. Elles n'y figurent que comme **sponsors de fonds d'essaimage (FCPR)** — scans inexploitables —
ou via des **filiales** (STEG International Services, SONEDE International) qui **ne sont pas** les mères.
Conclusion : pour GCT/CPG/TT/SONEDE/ONAS/ETAP… le détail VA récent **n'est pas accessible par le CMF**.

**Seule exception productive : STEG publie ses EF sur son site** (`steg.com.tn/fr/publications`,
2013→2024). Rapport annuel **2024** archivé (`minenergie/steg/etats-financiers/steg_rapport_annuel_2024.pdf`).
Extractible pour 2024 : **revenus 6 068,7 MD ; résultat net −229,8 MD ; effectif en activité 13 223**
(inscrit 14 146). **VA 2024 non extractible** : le rapport donne l'état de résultat **par fonction**
(coût des ventes), pas l'ESG par nature → attendre l'EF 2024 détaillé (`etat_financier_2024.pdf`, pas
encore publié).

**À lever (recoupement)** : le rapport 2024 donne **résultat net STEG 2023 = −489,6 MD**, alors que
notre série porte **−320,4 MD** — divergence (retraitement ? source provisoire ?) à trancher avant usage,
sans écraser en silence.

**Bilan « jusqu'à aujourd'hui »** : atteignable (VA) pour STEG (sauf 2024 en attente), Tunisair,
Ciments/Sotrapil/Sotumag (BVMT) ; **plafonné** pour GCT (2014), CPG (2010), TT (2009) ; **impossible
publiquement** (VA) pour les utilities — seulement CA/résultat/effectif via Annexe 9 LF et Cour des comptes.
SOTRAPIL récent (2018-2024) reste récupérable au CMF (nommage irrégulier) — canal non épuisé.

## 10. SOTRAPIL — la série ne s'arrêtait pas faute de données (6 nov. 2026)
Notre VA SOTRAPIL s'arrêtait à 2017, mais le corpus contient ses EF **jusqu'à 2024/2025**
(`bvmt-etats-financiers/sotrapil/`). Raison du blocage : les EF récents sont en **arabe** (2018-2022,
couche texte OK) et en **scan** (2024-2025, ~1 000 car.) — le parseur `extraire_grandeurs_ep.py`,
orienté français, ne les lit pas. **Données présentes, parseur à étendre** (pas une lacune de source).

Lecture manuelle vérifiée de l'EF arabe 2018 (colonne gauche = 2017, droite = 2018) — **test d'or
interne réussi** : le 2017 redérive revenus 15,10 / masse salariale 4,98 / résultat net 6,22 MD
(exacts vs CSV) et VA 14,67 MD (à 0,6 % du CSV 14,76). **SOTRAPIL 2018** : revenus 17,48 MD,
VA ≈ 15,5 MD, masse salariale 4,93 MD, **part salaires/VA 32 %**, résultat net 7,10 MD — profil sain
confirmé. (Non injecté dans le CSV généré : à intégrer via le parseur pour garder une seule définition
de VA.)

**Prototype de lecteur arabe (dérisqué le 6 nov. 2026)** — acquis à réutiliser :
- Le texte est en **formes de présentation** → **normaliser `unicodedata.normalize("NFKC", ligne)`**
  avant toute recherche (sinon les libellés ne matchent pas).
- Les deux années sont côte à côte : colonne **gauche = N-1, droite = N** ; la valeur de l'exercice
  est le **dernier montant comptable (≥ 1000) avant le libellé**. Validé sur `revenus` SOTRAPIL :
  2017 redérive 15,1014 MD (exact vs CSV), 2018 = 17,48 MD.
- **Difficultés restantes à traiter pour une version fiable** : certains libellés **passent à la
  ligne** (مشتريات التموينات / المستهلكة) ou se placent **entre les deux colonnes**
  (« 6 218 419 [النتيجة الصافية] 7 103 434 ») → **s'ancrer sur les codes de note stables** (1-5, 3-5,
  4-5, 10-5…) plutôt que sur le libellé ; les codes donnent un repère fixe de colonne.
- **La VA est absente des EF arabes** (0 occurrence de القيمة المضافة) → à **recalculer** avec une
  formule documentée (production − achats − charges externes) ; vérifier qu'elle **reproduit à < 1 %**
  la VA française sur l'année de recouvrement (2017) avant d'accepter la série, pour éviter une
  **rupture de définition** FR/AR.

**Backlog (rôle modéliste, PR à relire)** : (1) ajouter au générateur une **famille `G_PAR_NATURE_AR`**
(NFKC + ancrage sur codes de note + lecture « dernier nombre avant ancre ») et une détection
« EF arabe » ; (2) recompute VA documentée + test d'or de recouvrement 2017 ; (3) **OCR** des EF
SOTRAPIL **2024-2025** (scans). Une fois fait : SOTRAPIL couvert **2000→2024/2025**, et la même
famille débloque les années arabes des autres cotées. **Coût/valeur** : chantier modéré pour un gain
sur de petites EP — à arbitrer.

## Garde-fous
- Les agrégats ci-dessus sont **illustratifs** tant que le panel n'atteint pas le noyau des 21 EP du
  MdF ; chaque chiffre porte sa couverture.
- Les repères de secteur (23 907 MD, 89 350 agents, etc.) sont **attribués au rapport MdF annexé à la
  LF 2021** (exercice 2018) ; ce sont les affirmations du rapport, non un état vérifié par recoupement.
- Prochaine étape utile : parser les annexes MdF 2012-2026 en une petite série `agregats-secteur-ep.csv`
  (année, périmètre, ressources, charges personnel, effectif, subventions, résultat), une ligne par
  exercice, chaque valeur sourcée (fichier + page).
