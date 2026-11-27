# Collecte de sources manquantes — 25 novembre 2026

> ⚠️ **Confronter au catalogue avant de croire une « lacune ».** Mise à jour 26/11 : plusieurs
> « introuvables » ci-dessous étaient en fait **déjà catalogués et dans `tunisia-data/data/raw/`**
> (rapports Cour des comptes sous-cat 76 et RAPAM, rapports CNRPS `bilan*`/`ra_*`). Toute ligne de
> cette note doit être vérifiée contre `tunisia-data` (`sources/*-catalog.csv`, `data/raw/`) + 
> `jort_cache.db` avant d'engager une nouvelle collecte — cf. `docs/conventions/sources-et-datation.md`.

Récupération de sept lots de sources demandés par l'humain. Fichiers déposés hors dépôt dans
`~/Downloads/` (le dépôt est public : aucune donnée brute n'y est versée). Récupération via les
sites officiels vivants et, à défaut, la Wayback Machine (snapshot le plus proche `…/2id_/<URL>`).

⚠️ Captures Wayback tronquées : plusieurs fichiers n'existent qu'en version coupée à 1 048 576 o
(1 Mo) au moment du crawl — écartés car incomplets (voir CNRPS ci-dessous).

## Obtenu

| Lot | Emplacement `~/Downloads/` | Contenu | Couverture |
|---|---|---|---|
| **1. EBCNV INS** | `EBCNV2021_*.pdf/.xlsx` | Note de synthèse (15 p.), communiqués FR/AR, données Excel | 2021 |
| **2. Masse salariale CNSS** | `CNSS_publication_2020/` (18 tableaux FR + sommaire) | Dont `08-Fr-evolution_cotisations_cnss_2000-2020` ; effectifs, pensions, prestations | séries 2000‑2020 |
| **3. Stats fiscales DGI** | `DGI_stats_fiscales/` (5 fichiers) | Série recettes par **type d'impôt** 1986‑2025 ; contrôle fiscal 2016 (créations par secteur) ; IACE 2025 (chiffres DGI par secteur, **secondaire**) ; rapports d'activité DGI 2014‑2015 | variable |
| **4. Cotisations CNAM** | `CNAM_cotisations/` (9 PDF) | Rapports branche **AT/MP** (ANNUEL 2018‑2021, statistiques 2018‑2022) ; 2 fichiers de faible valeur (AO, accès info) | 2018‑2022 |
| **5. Transferts aux ménages** | `transferts_menages/` (14 PDF) | AMEN Social (rapports activité 2022, 2023 ; éval. impact 2021), CRES, Banque mondiale, UNICEF | 2017‑2023 |
| **6. CNRPS retraites** | `CNRPS_rapports/` | Rapports annuels `ra_2019`, `ra_2020` ; `rapport_ada_2019…2022` | 2019‑2022 |
| **7. Comptes communaux** | `comptes_communaux/` (9 fichiers) | 2020 réalisé par commune (CSV+XLSX) ; 2021 budgets détaillés + réalisé décembre | 2020‑2021 |

Déjà en main avant cette collecte (non repris) : annuaires CNSS 2016 et 2018, rétrospective CNSS
1990‑2004, BILAN CNAM 2010/2016‑2018/2018‑2019/2020‑2021.

## Lacunes confirmées (à verser au backlog durable)

- **Rapports annuels / publications statistiques CNSS et CNRPS 2021, 2022, 2023 : INTROUVABLES**
  publiquement (sites vivants + Wayback). Dernières éditions : **CNSS 2020** (série 2000‑2020),
  **CNRPS `ra_2020`** et recueil `gstat_2010-2019`. ⇒ les **pensions 2021‑2023 restent vides** tant
  que ces données ne sont pas obtenues directement auprès des caisses.
  - *Mise à jour 26/11 (session msika) :* confirmé qu'aucun rapport annuel CNSS ni CNRPS 2022/2023
    n'est publié en ligne. Bilan des pistes creusées depuis msika :
    - **Accès réseau** : depuis msika les sites CNRPS/CNSS sont joignables, mais leur chaîne TLS est
      incomplète (certificat intermédiaire manquant) — il faut `curl -k`/désactiver la vérif du cert ;
      `curl`/`web_fetch` standard échouent (`000`). INS et (par intermittence) la Wayback passent.
    - **« Guide / recueil statistique CNRPS »** : INTROUVABLE en URL statique. Le PDF « 2022, 2,02 Mo,
      04-01-2023 » repéré en recherche = en fait le **rapport annuel 2022 du chargé d'accès à
      l'information** (déjà en main, `rapport_ada_2022`), pas un recueil de données. Les vraies
      pages de données (`/acces-aux-docs/donnees-statistiques/pensions`) sont rendues en JS, non
      scrapables au `curl` ; les anciennes URL `upload/documents/gstat_*.pdf` renvoient 500 (arbo
      disparue au passage à Drupal). ⇒ restes possibles : **Wayback** (hors ligne au 26/11, à
      reprendre), **navigateur sans tête**, ou **demande formelle d'accès à l'information**.
    - **Moisson Wayback (26/11)** : l'ancienne arbo `cnrps.nat.tn/upload/acces_docs/Rapports/` est
      archivée. Récupérés **complets** dans `~/Downloads/CNRPS_rapports/wayback_2021/` : `bilan2015`
      (56 p.), `bilan2018` (75 p.), `ra_2017` (74 p.), `ra_2018` (85 p.). **Tronqués à 1 Mio,
      irrécupérables** (snapshot unique, capé au crawl) : **`gstat_2010-2019` (le recueil
      statistique !)**, `budget_2015/2017/2018/2019`, `bilan2017`, `bilan2019`, `ra_2014`, `ra_2015` ;
      `bilan2016` incomplet (sans trailer). ⇒ le **recueil statistique `gstat` n'existe nulle part en
      version complète** (ni site vivant, ni Wayback) : seule voie = **demande d'accès à
      l'information** auprès de la CNRPS.
    - **Cour des comptes** (`courdescomptes.nat.tn`) : **DÉJÀ OUTILLÉ ET CATALOGUÉ dans
      `tunisia-data`** (ne pas refaire). Le projet a déjà `scripts/scrape_cour_des_comptes.py`
      (`--catalog` → `sources/cour-des-comptes-catalog.csv`, 361 l. ; `--download <rubrique>` →
      `data/raw/cour-des-comptes/<rubrique>/` avec contrôle de troncature + SHA-256 dans
      `sources/cour-des-comptes-telechargements.csv`). Les 35 rapports de la sous-cat **76 « Santé et
      affaires sociales »** (dont audits **CNRPS** 2018, **CNSS** 2014, **CNAM** 2016, cliniques CNSS
      2017) et le **RAPAM 32** (cat 2 / sous-cat 84) sont catalogués ; 34/35 des PDF de la sous-cat 76
      sont dans `data/raw/` (le 35ᵉ, `Rapport_76_2018-08-16-09-08-22.pdf`, est **cassé à la source**
      et légitimement refusé). *(Un doublon exploratoire Playwright `~/outils/cour-des-comptes/cdc.mjs`
      a été écrit pendant cette session avant de retrouver l'existant : superflu, le script Python fait
      foi.)*
      **Sourçage vérifié** (rapport CNRPS p. 351) : la Cour **cite les textes** (loi n° 47-2017 du
      15/06/2017 modifiant la loi n° 71-2004) et **définit ses indicateurs** en note (autonomie
      financière = réserves techniques/passif ; couverture liquidité = actifs liquides/charges
      mensuelles) ; chiffres = agrégats d'audit tirés des comptes de la caisse (déficit 846,849 MD
      fin 2016 ; dette envers la CNAM 261,127 → 1 583,292 MD 2011-2016).
      Les PDF **bruts vont dans `tunisia-data/data/raw/`** (hors git, sauvegardé par restic),
      catalogués dans `sources/` — **jamais dans le précis public ni dans la base législative**
      (routage : textes juridiques → `tunisia-legislative-references`/`PDFs-legislation-tunisie` ;
      données et rapports d'analyse → `tunisia-data` ; précis = seulement `.qmd` + biblio + glossaire).
      **Limite** : RAPAM téléchargeable **s'arrête au 32ᵉ (2021, données ≤ ~2019)** ; les 33ᵉ/34ᵉ
      (cités dans l'actualité) ne sont pas publiés en PDF (404 aux URL prévisibles). Les
      **chiffres caisses 2021-2022 ne sont donc pas encore dans un rapport téléchargeable** ; seules
      les **lois de règlement 2020/2021/2022/2023** (sous-cat 18) sont en ligne (budget de l'État,
      transferts sociaux — pas les comptes détaillés des caisses).
    - **Observatoire tunisien de l'économie** : **FAUSSE PISTE, écartée** (vérifiée sur Wayback le
      26/11). Ses « rapports du commissaire aux comptes 2022 » (`rapport_cac_ote_2022.pdf`) sont
      l'audit des comptes **de l'association OTE elle-même** (total bilan 1 045 703 DT), **pas** les
      états financiers des caisses — confusion initiale levée. Rien à en tirer pour la CNSS/CNRPS.
    - **Chiffres officiels 2021-2022 déjà attestés par la presse** (ministère des Affaires sociales /
      Cour des comptes, relayé janv. 2024) — utilisables comme points sourcés en attendant les
      rapports : **CNSS résultat net −1 274 MDT (2021) → −961,5 MDT (2022)** ; **CNRPS déficit
      ≈578 MDT (2022), résultat net en recul de 420,6 MDT /2021**. (À re-sourcer sur le texte primaire
      avant usage dans le précis.)
  - ✅ *Rapatriement CNSS — vérifié contre `tunisia-data` le 26/11 : RIEN à faire, faux positif.*
    Tout le matériel CNSS de `~/Downloads/` est **déjà dans `tunisia-data/data/raw/caisses/`,
    catalogué et sauvegardé** : annuaire 2016 = doublon md5 de `annuaires/annuaire_statistique_2016_ar.pdf` ;
    lot 2020 déjà présent **en plus complet** (`cnss/2020/`, 24 fichiers dont états financiers, vs 18
    en local) ; `CNSS_Budget_2022.pdf` = md5 identique à `cnss/2020/03_Budget.pdf` ; `rapport_ada_2025`
    (CNRPS) déjà dans `caisses/cnrps/`. L'alerte « seulement en local » était erronée — cas d'école
    du réflexe « catalogue d'abord » (`sources/cnss-urls.csv`, `md5sum`).
- **Recettes fiscales DGI ventilées par secteur** (IS/IRPP par branche, nombre de contribuables par
  secteur) : **aucune série officielle**. La ventilation sectorielle n'existe qu'en partiel (contrôle
  fiscal 2016) ou en source secondaire (IACE 2025, qui reprend des chiffres DGI). data.gov.tn muet.
- **Cotisations d'assurance maladie CNAM détaillées** (produits par régime, taux) : absentes de tout
  document public ; ne figurent que dans les BILAN CNAM déjà récupérés. Pas d'ANNUEL/statistiques
  CNAM 2023 en ligne.
- **CNRPS `bilan2019`, `budget_2019`, `gstat_2010-2019`** : seules des captures Wayback **tronquées à
  1 Mo** existent — à récupérer entières auprès de la CNRPS si besoin.
- Pistes non explorées : CGSS / ministère des Affaires sociales et Conseil du marché financier pour
  les comptes CNAM ; CPSCL pour des comptes communaux antérieurs à 2020.

## Liste consolidée des documents à récupérer — état au 26/11/2026 au soir

Après la session msika (Wayback exploité, Cour des comptes cataloguée, CNSS réconciliée avec
l'entrepôt, produits CNAM extraits). Vérifiée contre `tunisia-data` (`sources/`, `data/raw/`) le
26/11. Trois canaux :

### A. À demander (Nejla / CRES, sources papier possibles à scanner ; ou accès à l'information)

**Liste épurée le 26/11 au soir, après audit complet de l'entrepôt** (ne rien demander de ce qu'on a) :

| Document | Organisme | État chez nous |
|---|---|---|
| **Recueil statistique `gstat` 2010-2019** (+ édition plus récente si elle existe) | CNRPS | seul exemplaire tronqué à 1 Mio ; les `gstat` 2000-2010 → 2010-2014 sont complets |
| **Rapports d'activité 2021, 2022, 2023** | CNRPS | rien après `ra_2020` (les `ra_2014→2020` sont complets en entrepôt) |
| **Bilans 2017 et 2019 ; budgets 2015→2019** | CNRPS | présents mais **tronqués à 1 Mio** dans l'entrepôt même (coupe Wayback) ; bilans 2015/2016/2018 complets |
| **Annuaire / publication statistique 2021-2023** (effectifs, pensions par régime et nature) | CNSS | dernière édition : série 2000-2020. ⚠️ **Ne pas demander les soldes** : résultats nets et endettement 2021-2023 déjà sourcés (rapports EP du ministère des Finances, séries `cnss-resultat-exercice` : −1 274,3 / −961,5 / −911,1p ; `cnrps-minfin-entreprises-publiques` : −578,7p en 2022) — la ligne « attestés que par la presse » était fausse |
| **États financiers 2022-2023 AVEC notes annexes** ; si possible la **ventilation des produits techniques par origine** (actifs vs retraités via CNSS/CNRPS), même pour 2016-2021 | CNAM | BILAN s'arrête à 2020-2021 ; la ventilation trancherait le sur-compte D.61 (+4 %) de la fiche-pont |

⚠️ *À relever aussi (hors demande)* : l'envoi **« SUITE 3 » de Nejla du 05/10/2026 est marqué
« contenu non relevé » dans sa fiche** — à inventorier dans la boîte mail avant toute nouvelle
demande (il contient peut-être déjà une partie de ce qui précède).

### B. Veille de publication (rien à faire, surveiller)

- **RAPAM 33 et 34** de la Cour des comptes : remis au Président (actualité) mais pas de PDF en
  ligne (404) ; surveiller `rapports-resultats/?r_cat=2&r_subcat=84` via
  `tunisia-data/scripts/scrape_cour_des_comptes.py --catalog`.
- **Rapport de loi de règlement gestion 2025** (sous-cat 18) : relever le programme 2
  « Sécurité sociale » comme fait pour 2022 et 2024.
- **OTE** : site en maintenance — plus rien à y chercher pour les caisses (fausse piste actée).

### C. Déjà en corpus, exploitation à finir (pas de téléchargement)

- ~~Décomposition des recettes CNRPS 2020~~ **Traité le 26/11 au soir** : le rapport 2020 ne la
  publie pas (narratif en deltas ; vérifié à l'image) — raffinement fait avec les composantes
  reconstituées de la série. **Test généralisé 2015-2020** fait : D.62 à ±2 % sur six ans ;
  sur-compte D.61 croissant +1,2 → +4 % (fiche-pont de `tunisia-data`). ~~Reste la décomposition
  CNSS~~ **Fait le 26/11 au soir** (notes 5/6 des états financiers CNSS : produits = cotisations
  pures, charges avec deux postes en nature). **Le canal C est entièrement soldé** — tout le reste
  dépend du canal A (demandes d'accès à l'information) ou de la veille (canal B).
- ~~Programme 2 des gestions 2020 et 2023~~ **Traité le 26/11 au soir** : 2020 = nomenclature
  pré-GBO, deux lignes CNRPS transcrites (arriérés 200 MD, subvention 87 MD) ; 2023 = programme 2
  **non ventilé** par le rapport (total mission seulement, 2 306,959 MD) — série non prolongeable
  sur 2023 avec ce document.
- **Hors caisses, repris de la collecte du 25/11** : recettes DGI ventilées par secteur (aucune
  série officielle — abandonner ou passer par une demande d'accès à la DGI) ; CPSCL pour les
  comptes communaux antérieurs à 2020 ; CGSS / CMF pour les comptes CNAM (pistes non explorées).
