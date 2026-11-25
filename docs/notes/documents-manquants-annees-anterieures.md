# Documents manquants pour les années antérieures des comptes par secteur (25/11/2026)

Objet : les documents qui manquent pour chiffrer les comptes des secteurs avant les années déjà
couvertes, en remontant aussi loin que va l'ouvrage, protectorat compris.

## Méthode

Un document n'est dit **manquant** que s'il ne figure dans aucun de ces lieux, cherché par deux voies
(nom de fichier ; titre ou années dans les manifestes et fiches) :

- le dossier brut de l'entrepôt de données (`data/raw/`, 4 699 fichiers listés par `find` le
  25/11/2026, lecture seule) ;
- les manifestes et fiches `sources/*.csv` et `sources/*.md` de la copie à jour de `main`
  (dont `*-urls.csv`, `ins-portal-manifest.csv`, `cour-des-comptes-catalog.csv`,
  `bct-archives-catalog.csv`) et `catalog.yml` ;
- le dossier des téléchargements de l'utilisateur ;
- pour les lois, les métadonnées du *Journal officiel* (`jort_cache.db`).

Trois statuts :

- **présent** : fichier dans le dossier brut ou les téléchargements (chemin donné) ;
- **listé, non téléchargé** : adresse au manifeste, fichier absent : il n'est pas manquant ;
- **manquant** : absent partout.

Aucun document n'a été téléchargé. Les adresses ne sont données que si elles figurent dans
l'entrepôt.

Gain de couverture : `precis/fr/compte-couverture-annees.csv` ne couvre que 2015-2023. Pour toute
année antérieure, le gain est **non calculable**. L'étendue des postes est lue dans
`precis/fr/postes-etendue.csv` de la branche `comptes/couverture-longue-periode` (non fusionnée) :
les postes budgétaires partent de 1986, les cotisations et pensions de la CNSS de 2000, les
dépenses des communes de 2008, celles de la CNAM de 2011, celles de la CNRPS de 2019.

## Six lignes de la liste du 25/11 sont déjà présentes

La note `a-collecter-2026-11-25.md` déclare « à collecter » des documents qui sont dans le dossier
brut. Ce sont des lectures à faire, non des collectes :

| Ligne | Document | Emplacement |
|--:|---|---|
| 1 | INS, ENBCNV 2021, annexe 3 (dépense annuelle moyenne par personne selon le produit) | `ins-publications/ebncv-2021/Annexe3_2021_Depense_annuelle_moyenne_par_personne_selon_le_produit.xlsx` ; aussi dans les téléchargements |
| 4 | CNAM, états financiers 2020-2021 | `caisses/cnam/BILAN_2020-2021.pdf` |
| 9 | Cour des comptes, analyses financières des communes 2020 | `finances_locales/dgct_portail/analfinancom2020.pdf` ; aussi dans les téléchargements |
| 10 | Cour des comptes, note de synthèse du contrôle financier des communes, gestion 2020 | `finances_locales/dgct_portail/مذكرة-تأليفية-نهائية-الرقابة-المالية-على-البلديات-بعنوان-تصرّف-2020-1.pdf` |
| 11 | HIFL, rapport annuel 2020, son résumé et sa première partie en français | `finances_locales/dgct/2020_hifl_rapport_annuel.pdf`, `…/2020_hifl_rapport_annuel_fr_premiere_partie.pdf`, `finances_locales/dgct_portail/HIFL_Rapportannuel_2020_Resume.pdf` |
| 12 | DGCT, *L'impact du COVID-19 sur les finances locales en Tunisie* | `finances_locales/dgct/2020_dgct_impact_covid19_finances_locales.pdf` |

## Grille de présence résumée

Chemins relatifs au dossier brut.

| Famille | Présent | Listé, non téléchargé | Manquant |
|---|---|---|---|
| INS, comptes de la nation (TEE, TOF, comptes des secteurs) | éditions 2001-2005 à 2013-2017 (base 1983 puis 1997), 2015-2020, 2017-2021 à 2021-2025 (base 2015) : `ins-publications/comptes-de-la-nation/`, `ins-comptes-nationaux-publications/` ; années couvertes 2001-2025 | — | éditions antérieures à 2001-2005 (années 1983-2000 et avant) ; pages 2015-2020 (non « base 2015 ») et « en 2018 » sans PDF |
| INS, comptes de patrimoine | aucun tableau dans les 18 éditions inventoriées (`inventaire-tableaux.csv`) | — | existence incertaine |
| UNdata (relais) | tableaux 101 et 102, 1960-2024 ; tableau 4.1 « Total Economy (S.1) », 1990-2024 : `undata/` | — | aucun tableau par secteur |
| INS, annuaire statistique | 22 éditions, 1995-2001 à 2019-2023 : `ins-publications/annuaire-statistique/` | — | 1996-2000, 1997-2001, 2009-2013 (absentes du portail) ; éditions antérieures à 1995-2001 |
| BCT, rapport annuel | 1959-2025 : `bct-archives/109/` | — | — |
| BCT, balance des paiements | 1987-2024 : `bct-archives/106/` | — | avant 1987 (contenue dans les rapports annuels) |
| BCT, bulletin des statistiques financières | 1972-2026 (226 fichiers pour 229 numéros) : `bct-archives/108/` | — | — |
| BCT, supervision bancaire | 2011-2022 : `bct-archives/198/` | 2023, 2024 | — |
| Lois de finances | 1959-60 à 2026, articles d'équilibre (fiches `jort-lf-budget-ordinaire.md`, `jort-lf-budget-etat.md`, corpus du *Journal officiel*) ; textes 2003-2019 : `minfinances/portail_ancien/lois_finances/` | — | — |
| Lois de règlement | gestions 1954-55 à 2020 dans les métadonnées du *Journal officiel* (`jort_cache.db`) | — | gestions 2021 et suivantes (non trouvées) |
| Cour des comptes, rapports sur la clôture du budget | gestions 2005-2007, 2009, 2011-2016, 2018-2024 : `cour-des-comptes/18/` | — | 2017 (au catalogue sans fichier), 2008, 2010 ; avant 2005 |
| Cour des comptes, rapports annuels généraux | n° 1-4, 9, 10, 13-18, 20-32 : `cour-des-comptes/84/` | — | n° 5-8, 11, 12, 19 (au catalogue sans fichier) |
| Rapport sur le budget de l'État (Finances) | 2012 actualisé, 2013, 2014 (projet) : `minfinances/portail_ancien/lois_finances/` ; LF 2018, 2021, 2022, 2024 : `gbo-recup-2026-11-04/annexes-lf/`, `banque-mondiale-rapports/` | — | avant 2012 ; autres années à établir (fichiers 2023 non identifiés) |
| Communes : Cour des comptes, HIFL, DGCT | voir la grille détaillée ci-dessous | contrôles financiers de 46 communes (rubrique 88) | analyses 2021-2023 ; HIFL 2021 et suivants ; DGCT avant 2008 |
| CNSS | annuaires 2006 (rétrospectif 1970-2006), 2010, 2013, 2016, 2017, 2018 ; planches « La CNSS en chiffres » 2020 ; états financiers 2018, 2020 ; rétrospective financière 1990-2004 : `caisses/cnss/` | — | rapports ou états financiers 2021-2023 ; annuaires 2019, 2007-2009, 2011-2012, 2014-2015 |
| CNRPS | rapports d'activité 2014-2020 ; états financiers 2015, 2016, 2018 (2017 et 2019 tronqués, illisibles) ; recueils statistiques 2000-2019 : `caisses/cnrps/` | — | rapports d'activité avant 2014 et après 2020 ; états financiers 2017 et 2019 lisibles |
| CNAM | états financiers 2010, 2011-2015, 2016-2021 ; rapports annuels 2018-2021 : `caisses/cnam/` | — | états financiers 2005-2009 et 2022-2023 |
| INS, enquêtes budget-consommation | 2021 : annexes 2 et 3, communiqué : `ins-publications/ebncv-2021/` | 2021 : annexe 1, « Accès aux services collectifs » (`ins-portal-manifest.csv`) | toutes les autres éditions (grille détaillée ci-dessous) |
| INS, enquêtes emploi | rapports annuels 2005, 2007-2012 ; notes trimestrielles 2012-2026 ; enquêtes emploi et salaires 2012, 2014, 2022 : `ins-enquete-emploi/` | — | rapports annuels 2006, 2013-2016 ; enquêtes antérieures à 2005 |
| DGI, statistiques fiscales | recettes fiscales par rubrique 1986-2025 : `minfinances/recettes_fiscales.xls` | — | statistiques par secteur ou par catégorie de contribuable (existence incertaine) |
| Entreprises publiques | rapport annexé aux LF 2020-2025 : `entreprises-publiques/rapports-ep-loi-finances/`, `caisses/minfin/` ; Cour des comptes, clôture du budget 2005-2009 (transferts aux EP 2003-2009) | — | rapport agrégé avant la LF 2020 (existence incertaine) |
| Plans et budgets économiques | plan triennal 1962-1964, perspectives décennales 1962-1971 : `plans-developpement/` | — | budgets économiques annuels ; plans suivants |
| Avant 1956 | *Bulletin économique et social de la Tunisie* : sept numéros de 1949-1953 (`caisses/best/`, `foncier-histoire/`) ; lois de règlement des exercices 1954-55 et 1955-56 (métadonnées du *Journal officiel*) | — | budgets et comptes du Protectorat ; annuaire statistique du Protectorat ; autres numéros du *BEST* |

### Communes, année par année

| Exercice | Cour des comptes, analyses financières | HIFL, rapport annuel | DGCT |
|---|---|---|---|
| avant 2008 | n'existe pas (voir ci-dessous) | n'existe pas | **manquant** ; séries Banque mondiale 1985-1991, 1990-1996, 2002-2012 présentes (`finances_locales/banque-mondiale/`) |
| 2008-2014 | n'existe pas (voir ci-dessous) | n'existe pas | agrégats présents (`dgct_portail/Données-Financières-Globales.xls` et classeurs voisins) |
| 2015-2017 | existence incertaine | n'existe pas | agrégats présents |
| 2018 | présent : `dgct_portail/التحاليل_المالية_على_البلديات_بعنوان_سنة_2018.pdf` (arabe, couche texte illisible, 126 communes) | n'existe pas | agrégats et fichiers par commune présents |
| 2019 | présent : `dgct_portail/RAPPORT-ANALYSE-CF.2019.pdf` | présent : `dgct/2019_hifl_rapport_annuel_ar.pdf` (« premier rapport annuel ») | agrégats et fichiers par commune présents |
| 2020 | présent : `dgct_portail/analfinancom2020.pdf` (227 communes) ; note de synthèse du contrôle financier, gestion 2020 | présent (arabe, résumé, première partie française) | fichiers par commune ; étude COVID-19 |
| 2021 | **manquant** | **manquant** | situation au 25/12/2021 seulement (`Depenses_Decembre2021.xlsx`) ; exercice clos **manquant** |
| 2022 | **manquant** | **manquant** | présent (`Budget2022_*.xlsx`) |
| 2023 | **manquant** | **manquant** | présent (`Data_*_2023_10-01-2024.xlsx`) |

Le rapport de 2018 dit s'inscrire dans le programme de développement urbain et de gouvernance
locale (prêt BIRD 8413-TN) et dans la note technique de 2018 (p. 2, lu à l'image) ; il ne cite
aucune édition antérieure. Une analyse antérieure à 2018 n'est donc pas attestée. La HIFL, instituée
par le code de 2018, publie son premier rapport sur 2019.

### Enquêtes budget-consommation de l'INS, édition par édition

Le communiqué de 2021 (`ins-publications/ebncv-2021/EBCNV2021_Communique_Fr.pdf`, p. 1) présente
l'enquête de 2021 comme « la douzième enquête quinquennale » depuis 1968. La thèse de M. Chebli
(2016, téléchargements, p. 80) en énumère dix : 1968, 1975, 1980, 1985, 1990, 1995, 2000, 2005,
2010 et 2014. Avec 2021, cela fait onze dates pour douze enquêtes : l'écart n'est pas résolu.

| Édition | Statut | Preuve d'existence |
|---|---|---|
| 1968 | manquant | communiqué 2021, p. 1 ; Chebli, p. 80 |
| 1975 | manquant | Chebli, p. 80 (seule source) |
| 1980 | manquant | Chebli, p. 80 ; même thèse : seuil de pauvreté établi « pour la première fois en 1980 » |
| 1985 | manquant | Banque mondiale 1995, rapport 13993-TUN, vol. I et II (`banque-mondiale-rapports/wb_1995_13993_*`) ; circulaire n° 18 du 4 juin 1986 (chapitre des prestations non contributives) |
| 1990 | manquant | Banque mondiale 1995, vol. II : 7 734 ménages interrogés de juin 1990 à juin 1991 |
| 1995 | manquant | Chebli, p. 80 ; la Banque mondiale (1995) ne l'annonce qu'à venir (« Enquête sur le niveau de vie des ménages ») |
| 2000 | manquant | Chebli, p. 80 (seule source) |
| 2005 | manquant | communiqué 2021 (taux de pauvreté 2005) ; études d'incidence de la compensation |
| 2010 | manquant | communiqué 2021 ; études d'incidence (11 281 ménages) |
| 2015 | manquant | communiqué 2021 (coefficients 2015) ; thèse de N. Ben Cheikh, p. 140 (mai 2015-mai 2016, 27 108 ménages) |
| 2021 | présent (annexes 2 et 3, communiqué) ; annexe 1 et « Accès aux services collectifs » listées, non téléchargées | — |

Aucun classeur ni rapport d'une édition antérieure à 2021 ne figure dans le dossier brut, les
manifestes ou les téléchargements (les fichiers `Annexe2010_0.xlsx` et `Annexe2020.xlsx` des
téléchargements sont des annexes de l'enquête sur la fonction publique).

## Présents mais non exploités

Ces documents reculeraient des postes sans rien collecter :

- lois de règlement 1954-55 à 1985 (corpus du *Journal officiel*) : postes budgétaires avant 1986 ;
- rapports d'activité de la CNRPS 2014-2018 et recueils 2000-2019 : cotisations et pensions de la
  CNRPS avant 2019 ;
- balance des paiements de la BCT 1987-2018 : postes du reste du monde avant 2019 ;
- agrégats de la DGCT 2008-2019 : rémunérations et moyens des services des communes ;
- annuaire CNSS 2006 (masse salariale 1970-1999, pensions 1980-2006) et rapports annuels de la BCT
  1960-1975 (salaires déclarés à la CNSS) : CNSS avant 2000.

## Liste des documents manquants, par priorité

### Priorité forte

1. **Cour des comptes, analyses financières des communes, exercice 2021.** Titre des éditions
   présentes : « التحاليل المالية على البلديات لسنة … ». Organisme : Cour des comptes, 2021. Chiffre :
   D.1 et P.2 des collectivités locales (S1313). Gain : S1313 passe de 8,3 % du montant couvert en
   2021 vers 22 % à 26 %, niveau des années où les deux postes sont chiffrés. Adresse non vérifiée :
   portail des collectivités locales (rubrique où figurent 2018-2020), site de la Cour, archives du
   web. Existence : probable (éditions 2018, 2019, 2020 présentes, liées au programme financé par la
   BIRD) ; non attestée par un document.
2. **CNSS, rapports d'activité ou états financiers 2021-2023.** Organisme : CNSS. Chiffre : D.61
   (ressources) et D.62 (emplois) de S1314. Gain : D.62 pèse 36,3 à 37,8 points de S1314 en
   2021-2023 ; la part CNSS de D.62 était de 38,9 % en 2020 (`a-collecter-2026-11-25.md`, ligne 16).
   Adresse non vérifiée : site de la caisse, archives du web (les éditions 2018 et 2020 en viennent,
   `sources/cnss-urls.csv`). Existence : probable (états financiers 2018 et 2020 publiés) ; non
   attestée pour 2021-2023.
3. **CNRPS, rapports d'activité 2021-2023.** Organisme : CNRPS. Chiffre : D.61 et D.62 de S1314.
   Gain : part CNRPS de D.62 de 56,6 % en 2020 ; S1314 aujourd'hui à 48,4 %, 42,3 % et 42,3 % du
   montant. Adresse non vérifiée : site de la caisse (bloqué), archives du web, rubrique
   `upload/acces_docs/Rapports/` (`sources/cnrps-urls.csv`). Existence incertaine : « aucun rapport
   d'activité postérieur à celui de 2020 n'a été trouvé » (`sources/cnrps-publications.md`). Les
   fichiers `rapport_ada_2019` à `2025` du dossier CNRPS ne sont pas des rapports d'activité (12 pages,
   renvoi à la loi organique n° 2016-22 sur l'accès à l'information, page de titre à confirmer à
   l'image).
4. **INS, comptes de la nation, éditions antérieures à 2001-2005.** Description : publication
   « Les comptes de la nation » portant les comptes des secteurs, TEE et TOF des années 1983-2000.
   Chiffre : cible INS de tous les secteurs pour ces années. Gain : non calculable. Adresse non
   vérifiée : bibliothèque de l'INS, BCT, archives nationales. Existence : probable — les éditions
   2001-2005 à 2004-2008 sont en base 1983 (`sources/ins-comptes-nationaux-publications.md`, l. 76-79)
   et « aucune édition en ligne ne porte 2001 et une année antérieure » (`catalog.yml`, l. 387) ; titre
   et années des éditions non établis.
5. **INS, enquête budget-consommation 2015 : annexes et rapport.** Description : tableaux de la
   dépense par produit, du type des annexes 2 et 3 de 2021. Chiffre : P.3 de S14, 2015-2019. Gain :
   non calculé pour 2015 ; en 2020, P.3 vaut 30,5 points du compte de S14 (borne haute,
   `sources-societes-menages.md`). Adresse non vérifiée : portail de l'INS, rubrique des enquêtes ;
   archives du web. Existence : sûre (communiqué 2021, p. 1 ; Ben Cheikh, p. 140) ; publication des
   annexes non établie.

### Priorité moyenne

6. **HIFL, rapports annuels 2021, 2022, 2023.** Chiffre : D.1, P.2 et transferts de S1313. Gain : celui
   de la ligne 1 si les montants y sont. Adresse non vérifiée : site de la HIFL, portail des
   collectivités locales. Existence incertaine (deux rapports connus, 2019 et 2020).
7. **Cour des comptes, analyses financières des communes, exercices 2022 et 2023.** Chiffre : contrôle
   de D.1 et P.2 de S1313. Gain : faible, S1313 est déjà à 25,6 % et 25,2 % grâce aux fichiers de la
   DGCT. Adresse non vérifiée : comme la ligne 1. Existence incertaine.
8. **DGCT, dépenses par commune de l'exercice 2021 clos.** Chiffre : D.1, P.2 de S1313. Gain : celui de
   la ligne 1. Adresse non vérifiée : portail des collectivités locales. Existence incertaine.
9. **CNAM, états financiers 2022-2023 et 2005-2009.** Chiffre : D.61, D.63 de S1314 ; série partant
   aujourd'hui de 2011. Gain : non calculé. Adresse non vérifiée : `http://www.cnam.nat.tn/doc/upload/`
   pour les éditions présentes (`sources/cnam-statistiques.md`). Existence incertaine.
10. **INS, enquêtes budget-consommation 2005 et 2010 : rapports et tableaux.** Chiffre : P.3 de S14
    pour les années couvertes par les éditions base 1983-1997 des comptes. Gain : non calculable.
    Adresse non vérifiée : bibliothèque de l'INS, portail de l'INS. Existence : sûre (communiqué
    2021 ; études d'incidence).
11. **CNRPS, rapports d'activité antérieurs à 2014.** Chiffre : D.61 et D.62 de S1314, 2001-2013. Gain :
    non calculable. Adresse non vérifiée : archives du web, bibliothèque de la caisse. Existence
    incertaine. Les recueils statistiques 2000-2019, présents, donnent déjà effectifs et masses.
12. **CNRPS, états financiers 2017 et 2019 lisibles.** Les copies présentes sont tronquées à 1 Mio
    (`sources/cnrps-etats-financiers.md`). Chiffre : recettes et charges des régimes. Adresse :
    `sources/cnrps-urls.csv` (seule capture tronquée) ; autre copie à chercher auprès de la caisse.
    Existence : sûre.
13. **Statistiques fiscales de la DGI par secteur ou par catégorie de contribuable.** Chiffre : D.5 de
    S11 et de S14. Gain : en 2020, 2,46 points de S11 (borne haute) ; non calculable avant 2015.
    Adresse non vérifiée : site du ministère des Finances. Existence incertaine.
14. **Budgets économiques annuels (ministère du Plan).** Description : « الميزان الاقتصادي », budget
    économique de l'année. Chiffre : agrégats de l'investissement et des revenus avant 2001, pour
    contrôle des comptes. Gain : non calculable. Adresse non vérifiée : bibliothèque de l'INS,
    archives nationales. Existence : sûre pour 1992 (cité par la Cour des comptes,
    `sources/cour-des-comptes-sources-citees-energie-industrie.csv`, l. 30) ; autres années non
    établies.
15. **Cour des comptes, rapports sur la clôture du budget, gestions 2008, 2010 et 2017.** Chiffre :
    contrôle des postes budgétaires. Gain : faible, les lois de règlement de ces gestions figurent
    au *Journal officiel*. Adresse : 2017 au catalogue sans fichier (`cour-des-comptes-catalog.csv`) ;
    2008 et 2010 non vérifiées, site de la Cour. Existence : sûre pour 2017 ; incertaine pour 2008 et
    2010.
16. **INS, annuaires statistiques 1996-2000, 1997-2001, 2009-2013 et antérieurs à 1995-2001.**
    Chiffre : FCCL, finances locales, emploi, années 1956-1994. Gain : non calculable. Adresse non
    vérifiée : bibliothèque de l'INS ; version anglaise du portail pour 2009-2013. Existence : les trois
    éditions récentes « jamais mises en ligne » (`sources/ins-annuaires-statistiques.md`) ; éditions
    antérieures non établies.

### Priorité faible

17. **INS, enquêtes budget-consommation 1968, 1975, 1980, 1985, 1990, 1995, 2000.** Chiffre : P.3 de
    S14 sur longue période, sans cible INS par secteur avant 2001. Adresse non vérifiée : bibliothèque
    de l'INS, archives nationales ; pour 1985 et 1990, données unitaires citées par la Banque mondiale.
    Existence : sûre pour 1968, 1985 et 1990 ; incertaine pour 1975, 1980, 1995 et 2000 (une seule
    source, Chebli).
18. **Cour des comptes, analyses financières des communes 2015-2017.** Existence incertaine (aucune
    édition antérieure à 2018 citée). Gain nul pour D.1 et P.2 : les agrégats de la DGCT 2008-2019
    sont présents.
19. **Comptes des communes avant 2008 (ministère de l'Intérieur).** Description : exécution agrégée des
    budgets communaux. Chiffre : S1313 avant 2008. Gain : non calculable. Adresse non vérifiée :
    bibliothèque de la DGCT, archives nationales. Existence incertaine ; les séries de la Banque
    mondiale 1985-2012, présentes, en tiennent lieu en partie.
20. **CNSS, annuaires 2019, 2007-2009, 2011-2012, 2014-2015.** Chiffre : masse salariale par activité
    (D.1 de S11 et S14) ; 2019 seul compte pour la couverture actuelle. Adresse non vérifiée : site de
    la caisse, archives du web. Existence incertaine ; les planches 2020 présentes ne portent pas la
    masse salariale.
21. **Rapport sur le budget de l'État (Finances) avant 2012 et années non identifiées depuis.** Chiffre :
    contrôle des postes budgétaires. Gain : faible (séries du ministère 1986-2025 présentes). Adresse
    non vérifiée : ancien portail du ministère, archives du web. Existence incertaine avant 2012.
22. **Rapport sur les entreprises publiques annexé aux lois de finances antérieures à 2020.** Chiffre :
    P.1, D.1 des entreprises publiques (S11). Adresse non vérifiée : site du ministère des Finances.
    Existence incertaine.
23. **INS, enquête emploi : rapports annuels 2006, 2013-2016 et enquêtes antérieures à 2005.** Chiffre :
    effectifs, clés de partage de D.1 entre S11 et S14. Adresse non vérifiée : portail de l'INS.
    Existence incertaine (années à établir).
24. **Cour des comptes, rapports annuels généraux n° 5-8, 11, 12, 19.** Au catalogue sans fichier.
    Chiffre : observations sur les comptes des organismes. Adresse non vérifiée : bibliothèque de la
    Cour. Existence : sûre (catalogue de la Cour).
25. **Avant 1956 : budgets et comptes de la Régence.** Description : budget général et comptes de
    l'État tunisien sous le Protectorat. Chiffre : recettes et dépenses de l'administration centrale
    avant 1956. Adresse non vérifiée : Gallica (*Journal officiel tunisien*), archives nationales. Existence :
    sûre pour les exercices 1954-55 et 1955-56 (lois de règlement publiées en 1966) ; à établir pour
    les années antérieures.
26. **Avant 1956 : annuaire statistique du Protectorat.** Description : recueil statistique annuel de
    l'administration du Protectorat. Adresse non vérifiée : Gallica, BnF, archives nationales.
    Existence incertaine : aucun document de l'entrepôt ne le cite.
27. **Avant 1956 : autres numéros du *Bulletin économique et social de la Tunisie*.** Sept numéros
    présents (1949-1953). Chiffre : salaires, prix, prévoyance. Adresse non vérifiée : Gallica,
    bibliothèque nationale de Tunisie. Existence : sûre (numéros présents).
28. **Avant 1958 : rapports de la Banque de l'Algérie et de la Tunisie.** Chiffre : monnaie et crédit
    avant les rapports de la BCT (1959). Adresse non vérifiée : Gallica, archives de la Banque de
    France. Existence incertaine : aucun document de l'entrepôt ne le cite.

## Limites

- Les années des lois de règlement viennent des métadonnées du *Journal officiel* ; la présence de
  chaque fascicule au corpus local n'a pas été vérifiée une à une.
- Le dénombrement « douzième enquête » du communiqué de 2021 et les dix dates de la thèse Chebli ne
  concordent pas ; aucune autre source de l'entrepôt ne date 1975, 1980, 1995 et 2000.
- Gains non calculables avant 2015 : la table de couverture ne remonte pas plus haut.
