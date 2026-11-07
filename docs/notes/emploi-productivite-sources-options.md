# Emploi et productivité : quelle série pour décomposer la part des salaires ?

*Note de travail — options pour la décomposition salaire réel / productivité (Askenazy-Cette-Sylvain),
en appui de `partage-valeur-ajoutee-tunisie.md`. On n'y réinvente rien : on compare d'abord à ce que
les autres mobilisent.*

## 1. Le besoin

La décomposition de la part des salaires sépare un **terme de prix** (coin prix conso / prix VA —
déjà calculé, § 4.11 de la note) et des **termes de quantité** : le **salaire réel par tête**
(rémunération ÷ salariés ÷ prix) et la **productivité** (VA en volume ÷ emploi). Les deux termes de
quantité exigent une **série d'emploi** — salariés pour le salaire par tête, emploi occupé pour la
productivité. C'est la seule pièce qui manquait.

## 2. Ce que les autres mobilisent (pour ne pas réinventer la roue)

| Travail | Emploi mobilisé | Productivité / VA | Méthode |
|---|---|---|---|
| **ITCEQ**, tableau de bord productivité ; « Croissance potentielle » | **Enquête emploi** (occupé) + comptabilité nationale | VA (CN) ÷ emploi occupé ; PGF en résidu avec stock K | macro, cadre de croissance potentielle |
| **ITCEQ**, « Hausse des salaires et productivité » (Khlifi, 2013) | **Enquête emploi** : 2 235 milliers de salariés en 2011 | salaire réel vs productivité du travail | macro |
| **ITCEQ** / « Structural change… » (RNE) ; Marouani-Mouelhi | **Microdonnées RNE** (Répertoire national des entreprises) | productivité du travail par firme | décomposition **within/between** (Olley-Pakes, Foster) |
| **Banque mondiale**, TFP in Tunisia (37103) ; *Jobs Landscape* ; *Global Productivity DB* | **Permanent employees** ; emploi occupé | VA, PGF, productivité du travail 1980-2018 | comptabilité de la croissance |
| **FMI**, Country Report 16/47 | emploi occupé | décomposition PIB / PIB par tête / productivité 1970-2010 | macro |
| **FES**, « Évolution des salaires réels… » | enquête emploi + salaires | salaire réel vs productivité | macro |
| **INS**, Enquête Emploi et Salaires auprès des Entreprises | emploi **et salaires** par secteur, panel RNE | salaire de base moyen par catégorie | enquête d'entreprises |

**Constat.** Personne ne construit l'emploi de la décomposition **à partir des déclarés CNSS**. Le
dénominateur standard est l'**enquête emploi** (occupé ou salarié) ; le niveau firme passe par les
**microdonnées RNE**. La CNSS déclarée est un indicateur **du secteur formel**, ≈ la **moitié** des
salariés (1,1 M déclarés en 2011 contre 2,235 M de salariés à l'enquête emploi) : s'en servir comme
dénominateur macro **sous-estimerait l'emploi de moitié** et ne serait comparable à aucune étude.

## 3. Ce qu'on a vraiment (après ventilation)

**CNSS — salariés déclarés (secteur formel).**
- Série annuelle **longue** mais **à deux bases qui ne se raccordent pas** : l'annuaire 2006 publie
  1970-2006 sur un concept **plus large** (2006 : 1 179 025), l'annuaire 2016 et le régime RSNA
  publient 2000-2020 sur les **affiliés actifs** (2006 : 936 103 ; 2000 : 773 161 ≈ RSNA actifs).
  **Rupture de concept vers 2000** : ne pas chaîner.
- **Salariés déclarés** publiés **directement** (pas besoin de retrancher les non-salariés des
  « actifs »). Les non-assujettis sont isolés (~1 000-1 300).
- **Ventilation sectorielle** à trois années repères : **2006, 2016, 2018** (annuaires, par activité
  et par taille d'entreprise).
- **Masse salariale déclarée** publiée → **salaire moyen déclaré** (368 D/an en 1970 → 4 926 D/an en
  2006, base annuaire 2006) : un salaire par tête du formel, **sur la base large** (donc non raccordé
  à l'après-2000).

**CNRPS — affiliés actifs (public + parapublic).** Série **propre 2000-2020** (531 449 → 776 504).
Couvre les agents publics **et certains personnels d'entreprises parapubliques** : atout pour le
public marchand, mais **brouille la frontière** entre administrations et SNF.

**INS enquête emploi.** Emploi **occupé** total (`bct-emploi-occupe`, 2007-2024) ; emploi **salarié**
propre seulement **1999-2012** (`occupes_statut`). C'est le standard, mais la série salariée longue
par secteur nous manque en propre.

**Comparateur.** Banque mondiale, Global Productivity Database (productivité du travail, 1980-2018).

## 4. Les options

### Option A — Enquête emploi (le standard)
Emploi occupé (productivité) et salariés (salaire par tête) de l'enquête emploi INS + VA des comptes.
- **Pour** : comparable à **toute** la littérature tunisienne (ITCEQ, BM, FMI) ; couvre l'informel ;
  cohérent entre numérateur et dénominateur ; économie entière.
- **Contre** : la série **salariée par secteur** longue n'est pas en notre possession (propre
  1999-2012) ; il faut l'extraire des rapports annuels de l'enquête emploi (chantier de dépouillement) ;
  l'emploi occupé mêle salariés et indépendants (cohérent avec la mesure « économie entière », pas avec
  les SNF).

### Option B — Déclarés CNSS + CNRPS (secteur formel)
Salariés = CNSS salariés déclarés (privé) + CNRPS affiliés (public + parapublic) ; salaire par tête =
masse salariale déclarée ÷ déclarés.
- **Pour** : **salarié** et **formel**, donc **mieux ajusté au périmètre SNF** que l'emploi occupé ;
  série longue (depuis 1970 pour le privé) ; **salaire moyen déclaré** fourni ; ventilation sectorielle
  (2006/2016/2018) ; masse salariale cohérente avec une assiette.
- **Contre** : **non standard** — aucune étude ne s'en sert, donc **incomparable** ; ne couvre que le
  **formel** (~½ des salariés), sous-déclaration ; **rupture de concept CNSS vers 2000** (deux bases) ;
  CNRPS mêle public et parapublic ; « déclaré » ≠ emploi réel.

### Option C — Hybride (recommandée)
1. **Productivité et part des salaires économie entière** : enquête emploi occupé + VA (comme ITCEQ/BM)
   → **comparable** à la littérature.
2. **Lecture du secteur formel / SNF** : déclarés CNSS+CNRPS et **salaire moyen déclaré** en **contre-
   champ**, pour éclairer le *wage push* formel sans prétendre à l'économie entière.
3. **Si l'on veut le niveau firme** (within/between) : **microdonnées RNE**, comme « Structural
   change… » — mais c'est un autre chantier (accès microdonnées).
- **Pour** : comparable **et** adapté au périmètre ; chaque série sur son terrain ; aucune rupture
  chaînée en silence.
- **Contre** : deux dénominateurs à présenter proprement (ne pas les mélanger dans un même ratio) ;
  demande encore d'**extraire la série salariée de l'enquête emploi** par secteur (2013-2024).

## 5. Recommandation

**Option C.** Elle respecte la règle « on ne réinvente pas la roue » (le cœur reste enquête emploi +
comptabilité nationale, comme tout le monde) tout en exploitant l'avantage propre des caisses (un
salaire **déclaré** du formel, bien ajusté aux SNF) **en contre-champ**, jamais comme substitut au
dénominateur macro.

**Prochain pas minimal, sans rien chaîner à tort** : extraire la série **salariés par secteur de
l'enquête emploi 2013-2024** (rapports annuels INS) — c'est elle, pas la CNSS, qui débloque la
décomposition comparable. Les déclarés CNSS+CNRPS, déjà en main, serviront de **lecture formelle**
parallèle.

## 6. Matière pour les tests de sensibilité (toutes les pistes assemblées)

L'idée : la **part des salaires** (D.1/VA) ne dépend pas de l'emploi, mais **sa décomposition**
(salaire réel vs productivité) et le **niveau** comparé en dépendent. On teste donc la robustesse en
faisant varier (a) le dénominateur d'emploi et (b) la méthode de mesure de la part.

**(a) Dénominateurs d'emploi assemblés (milliers de personnes, années de chevauchement) :**

| Année | Occupé (EE) | Salariés (EE) | CNSS décl. (éd2016) | CNRPS affiliés | CNSS+CNRPS (formel) |
|---|---:|---:|---:|---:|---:|
| 2007 | 3 085 | 2 144 | 992 | 615 | 1 607 |
| 2010 | 3 277 | 2 245 | 1 163 | 646 | 1 809 |
| 2012 | 3 256 | 2 295 | 1 150 | 715 | 1 865 |
| 2016 | 3 437 | — (fin 2012) | 1 181 | 780 | 1 961 |

Le **formel (CNSS+CNRPS) ≈ 81 %** des salariés de l'enquête emploi en 2012 (1 865 / 2 295) : l'écart
mesure le salariat **informel/non déclaré** (~19 %). Couvertures : occupé 2007-2024 ; salariés EE
1999-2012 ; CNSS éd2016 2000-2016 (éd2006 1970-2006, **base différente**) ; CNRPS 2000-2020.

**(b) Niveau de la part du travail selon la méthode (sensibilité de niveau) :**

| Mesure | 2010 | 2019 | 2023-24 | Ajustement non-salariat |
|---|---:|---:|---:|---|
| Notre **éco. entière** (D.1/PIB) | 38,3 % | 38,8 % | 43,8 % (2024) | aucun (biais max) |
| **OIT** (part du revenu du travail) | 43,8 % | 45,7 % | 45,9 % (2024) | imputation OIT |
| **PWT** (labsh, FRED) | 47,9 % | 52,2 % | 56,1 % (2023) | imputation Gollin |
| Notre **SNF** (hors revenu mixte) | 47,0 % | 54,0 % | 59,0 % (2024) | périmètre sociétés |

La part du travail tunisienne va, en 2019, de **38,8 % (éco. entière) à 54,0 % (SNF)**, avec l'OIT
(45,7 %) et PWT (52,2 %) entre les deux : l'essentiel du débat est un **enjeu de mesure**, pas un
désaccord sur les faits. Les quatre mesures **montent** de 2010 à 2023-24, ce qui **robustifie le
sens** de l'évolution.

**Attention — ces mesures ne sont pas indépendantes, et une seule couche est primaire.** Les seules
données **primaires** tunisiennes sont les **comptes nationaux de l'INS** (PIB, rémunération des
salariés) et l'**enquête nationale sur la population et l'emploi** (ENPE) telle que l'INS la publie.
Toutes les autres — **OIT, ILOSTAT, WDI, PWT, BM Global Productivity** — en sont **dérivées**
(re-traitements : ILOSTAT = micro-données ENPE retraitées par l'OIT ; WDI = estimations modélisées OIT ;
PWT/BM = comptes INS relayés par l'ONU/SCN, le Conference Board ou WDI). Elles ne diffèrent
que par leur **traitement du non-salariat** : aucune imputation (notre éco. entière), imputation OIT
(salaire relatif des indépendants), imputation Gollin (PWT, variable `i_labsh`), ou exclusion par le
périmètre des sociétés (notre SNF). L'écart de 38,8 à 54 % **n'est pas quatre observations qui se
confirment** — c'est **une seule donnée INS, traitée de quatre façons**. (Fiche de méthodologie
détaillée des sources secondaires : en cours, `data/scratch/…/methodologie-sources-secondaires.md`
côté tunisia-data.) (Sources : OIT via OWID ; PWT 11.0,
`LABSHPTNA156NRUG` ; comptes INS.)

**(c) Comparateurs de productivité** : Banque mondiale, Global Productivity Database (productivité du
travail **niveau et croissance**, 1980-2018 : 8 528 → 13 313 → 14 635 $/travailleur en 1990/2010/2018) ;
PWT (PIB réel + personnes engagées 1960-2023 : 2,89 → 3,50 → 3,97 M en 2000/2010/2019) ; ITCEQ
(indice sectoriel, à récupérer autrement — site qui bloque).

**(d) Récupération faite (dossier `tunisia-data/data/scratch/compta-nat-emploi-productivite/`, non
indexé) et trous.** Quinze séries récupérées (PWT part du travail / PIB réel / emploi / capital ;
BM GPD productivité et PGF ; ILOSTAT ; INS primaire) + fiche `methodologie-sources-secondaires.md`.
- **ILOSTAT prolonge le salarié** au-delà de 2012 : 2013=2 386, 2015=2 466, 2016=2 467, 2017=2 599,
  2019=2 606 (milliers). Contrôle de filiation : ILOSTAT 2010 = **2 245,0**, identique à l'enquête
  emploi — c'est l'**ENPE harmonisée**, pas une source neuve.
- **Trou salarié comblé du mieux possible, en TROIS niveaux de provenance**
  (`salarie_occupe_consolide_2007_2024.csv`) : **(i) INS primaire publié** (occupes_statut) 2007-2012 ;
  **(ii) ILOSTAT — dérivé** (micro-données ENPE retraitées par l'OIT) 2013, 2015-2017, 2019 ;
  **(iii) estimé signalé** = ratio salarié/occupé (interpolé, ~73 %) × **emploi occupé primaire INS**
  pour 2014, 2018, 2020-2024. Contrôle : le ratio (68,5 → 74,7 %) colle au WDI modélisé (70-75 %) à
  1-2 points. **Le salarié INS primaire direct s'arrête en 2012** (la table « statut » disparaît des
  annuaires après 2012) ; au-delà, tout est **dérivé (ILOSTAT) ou estimé** — à ne jamais présenter
  comme une observation INS. Seules deux séries d'emploi sont **primaires INS** : l'**occupé total**
  (2007-2024) et le **salarié par statut 1999-2012** (+ instantanés RGPH 2014/2024).
- **Trous non comblables** : **heures (avh) PWT absentes** de FRED → pas de décomposition *en heures* ;
  **BM GPD s'arrête en 2018**. À porter au backlog.
- **Piège** : PWT part du travail **plate à 0,5512 avant les premières observations** (extrapolation
  arrière `i_labsh2`) — les décennies anciennes ne sont pas des observations ; le RGPH 2024
  (2,43 M, 66 %) mesure la **couverture contributive**, pas le statut salarié (ne pas chaîner avec le
  78,7 % de 2014).

## 6 bis. Carte institutionnelle vérifiée (comptes INS) et corrections « billes »

**Vérifié sur la méthodo INS (SCN 2008).** Le critère de classement n'est **ni déclaré/informel, ni
petit/grand, mais la COMPTABILITÉ COMPLÈTE** : « Le secteur informel est constitué des unités
économiques […] ne disposant […] d'aucune comptabilité complète (de flux) ». D'où :

| Unité | Secteur comptable | Dans les SNF ? |
|---|---|---|
| Sociétés + indépendants **au réel** (liasse fiscale = quasi-sociétés) + entreprises publiques commerciales | **SNF** | oui |
| Banques, assurances | SF | non |
| Fonction publique, collectivités, établissements administratifs, hôpitaux | APU | non |
| Indépendants **au forfait** + informel (sans comptes) + loyers imputés | **Ménages (revenu mixte)** | non |

Conséquences : (i) l'**informel du secteur** est hors SNF, **mais les salariés non déclarés d'une
firme formelle sont dans les SNF** (emploi informel du secteur formel — déf. OIT reprise par l'INS) ;
(ii) le **revenu mixte ≠ tous les indépendants déclarés** : les déclarés **au réel** sont des
quasi-sociétés **dans les SNF**, seuls les forfaitaires + informels sont en ménages ; (iii) **aucune
caisse ne découpe les SNF** — le critère INS (comptabilité complète) ne se lit pas dans les fichiers
de caisses.

**Billes de correction (effectifs, vérifications croisées), année de calage 2018 :**

| Élément | 2018 (milliers) | Usage |
|---|---:|---|
| CNRPS affiliés actifs | 766 | public (APU + qq entreprises) |
| − Fonction publique (hors collectivités) | 631 | APU central |
| − Collectivités locales | 21 | APU local |
| **= résidu CNRPS** | **~114** | **EPA/hôpitaux (APU) + entreprises publiques (SNF)** |
| Effectifs EP (chantier EP) | ~100 | SNF-public (dont une part en CNSS, une en CNRPS) |
| CNSS salariés déclarés | ~1 240 | privé + public commercial (≈ SNF + SF) |

**Premier calage, et pourquoi ça se compense.** Pour l'emploi des **SNF** (dénominateur de la
décomposition), partir des **CNSS salariés déclarés** (~1 240 k) ; **retirer** les sociétés
financières (~40-50 k) ; **ajouter** la part entreprises publiques affiliée CNRPS (~40-50 k du résidu,
le reste étant hôpitaux/EPA = APU). Les deux ajustements étant **du même ordre**, ils **se
compensent** : **emploi des SNF ≈ CNSS salariés déclarés**, à ±5 % près. Biais résiduel à porter :
les **non-déclarés des firmes formelles** sont dans D.1/VA des SNF mais **hors** CNSS → le salaire par
tête SNF calculé sur CNSS est légèrement **surestimé**. Billes pour affiner : emploi des banques/
assurances (SF), split hôpitaux/entreprises du résidu CNRPS, split réel/forfait des indépendants
(comptes fiscaux IRPP, pour la frontière VA ménages/SNF).

### 6 bis.1 Retirer les entreprises publiques des SNF : second ordre (vérifié)

Pour isoler les **SNF privées**, on retire les **EP classées en SNF** (marché, non financières —
donc **hors banques publiques** = SF). On a la **D.1 EP complète** (rapport MdF, ~3 400-4 300 MD =
16-19 % de la D.1 des SNF) mais **pas la VA EP agrégée** : elle n'est **pas publiée**, seulement
**reconstructible** par le bas depuis les comptes primaires (~20 grandes EP, couverture ~30-37 % de la
D.1). Trois estimations indépendantes de la VA EP (bottom-up grossé par la couverture ; ρ du panel ;
part VA = part D.1) **convergent** : **part des salaires des SNF privées ≈ SNF totale, à ±2-3 points**.

**Réserve décisive — la compensation et les prix distordent la VA comptable des EP.** ETAP (VA pilotée
par le prix du pétrole : +106 % en 2022), STIR et Office des céréales (achat/vente subventionné,
subventions d'exploitation) ont une VA d'états financiers **inutilisable** pour un ratio — d'où un
artefact à 75 % en 2022. **Mais c'est NOTRE reconstruction qui est bruitée, pas la mesure INS** : la
VA des SNF de l'INS est à **prix de base**, la **compensation y est traitée en D.31 (subventions sur
les produits), HORS VA du producteur**. Donc la **part des salaires des SNF de l'INS est propre**.

**Conclusion de la vérification institutionnelle** (informel / CNRPS / réel-forfait / SNF-EP /
compensation) : la **part des salaires des SNF de l'INS (totale) est la référence robuste** ; les
corrections EP / caisse / compensation sont **de second ordre (±2-3 pts)** et de **signe
indéterminé** faute de VA EP propre, mais **ne déplacent pas le diagnostic**. On ne sur-ingéniere
**pas** le retrait des EP depuis des comptes distordus. La **bonne façon** (CKP/ACS) tient : mesure
sur les **SNF** (hors immobilier ; informel et revenu mixte au forfait dehors), emploi ≈ **CNSS
déclarés**.

## 7. Pièges à porter (quelle que soit l'option)

- **CNSS : deux bases** (annuaire 2006 vs 2016/RSNA) — ne pas chaîner autour de 2000.
- **Déclaré ≠ occupé** : facteur ~2 entre CNSS déclarés et salariés de l'enquête emploi (formel vs
  total).
- **CNRPS = public + parapublic** : ne pas l'assimiler aux seules administrations.
- **Numérateur et dénominateur de même périmètre** : VA des SNF avec salariés du formel ; VA économie
  entière avec emploi occupé — jamais un ratio qui croise les deux.

## Sources

Données : `cnss_rsna_annuaires`, `cnss_annuaire_2006/2016/2018_*` (dont ventilation par activité),
`cnss_effectifs_par_regime`, `cnrps_pensions` (affiliés actifs), `bct-emploi-occupe`,
`occupes_statut` (tunisia-data). Littérature : ITCEQ (tableau de bord productivité ; « Hausse des
salaires et productivité », 2013 ; « Croissance potentielle ») ; Banque mondiale (TFP in Tunisia
37103 ; *Tunisia's Jobs Landscape* ; Global Productivity Database) ; FMI *Country Report* 16/47 ;
FES, « Évolution des salaires réels en Tunisie » ; INS, Enquête Emploi et Salaires auprès des
Entreprises 2022 ; « Structural change, productivity and jobs » (microdonnées RNE).
