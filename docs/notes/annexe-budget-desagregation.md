# Conception — désagréger le budget de l'État, deux vues (chantier annexe-budget-desagregation)

Note de conception et d'inventaire, ouverte le 2026-11-09. Prolonge l'annexe
`precis/fr/annexe-budget-etat.qmd` (matière : `annexe-budget-etat.md`, documentaire :
`annexe-budget-etat-documentaire.md`). But : **désagréger les dépenses de l'État**, relier chaque
composante examinée dans le précis et suivre **son poids année par année**, sous **deux vues** :
une **vue budgétaire** (nomenclature de la loi de finances / du ministère des Finances) et une
**vue « comptes de la nation »** (regroupement par nature économique et secteur bénéficiaire, SCNT).

Les chiffres ci-dessous ont été **vérifiés le 2026-11-09** par extraction directe des séries
(`repartition_depenses.xls` et le cache `precis/_seriescache/`). Niveaux : **[réconcilié]** =
boucle sur un total lu ; **[lu]** = valeur de série ; **[à sourcer]** = pas encore établi.

---

## 1. Le socle : la vue budgétaire par nature réconcilie exactement

Source : `repartition_depenses.xls` (Ministère des Finances, « répartition économique des
dépenses », feuille `Rep eco dep`), déjà dans l'entrepôt et déjà le total de
`denominateurs-depenses-etat-pib`. Nomenclature (présentation LOB 2004-42) :

| N° | Rubrique | Couverture (réalisé) | Relié au précis |
|---|---|---|---|
| 1 | Dépenses de fonctionnement | 1986→2025 | — (agrégat) |
| 1.1 | Rémunérations publiques | **1990→2025** | **Rémunérations publiques** (identité) |
| 1.2 | Moyens des services | **1996→2025** | — |
| 1.3 | Interventions publiques | **1996→2025** | compensation, caisses, FCCL (⊂, voir §2) |
| 2 | Dépenses d'équipement (4 sous-lignes) | 1986→2025 | FBCF ; investissements EP |
| 3 | Prêts (rétrocédés EP, avances Trésor) | 1986→2025 | Entreprises publiques |
| 4 | **Total** | 1986→2025 | = **dépenses hors service de la dette** (`#fig-bud-serie`) |

**Réconciliation [réconcilié]** : `Fonctionnement + Équipement + Prêts = Total`, écart ≤ 0,1 MDT
(arrondi) sur **toutes** les années 1986-2025. Le « Total » égale la série réalisée hors dette de
l'annexe. La vue budgétaire est donc **additive et bouclée** : c'est l'ossature.

Contrôle (MDT, réalisé) :

| année | Rémun. | Moyens | Interv. | Fonct. | Équip. | Prêts | Total |
|---|---|---|---|---|---|---|---|
| 1986 | — | — | — | 1 291,6 | 989,8 | 113,6 | 2 395,0 |
| 1996 | 1 993,2 | 395,9 | 858,5 | 3 247,6 | 1 437,5 | 173,2 | 4 858,3 |
| 2010 | 6 785,2 | 841,0 | 2 374,8 | 10 001,0 | 4 302,2 | −35,7 | 14 267,4 |
| 2020 | 19 200,0 | 2 262,2 | 8 488,4 | 29 950,6 | 7 207,3 | 545,0 | 37 702,9 |
| 2025 | 23 275,8 | 2 605,7 | 16 426,2 | 42 307,7 | 9 704,4 | 482,9 | 52 495,0 |

**Hors champ** : le **service de la dette** (intérêts, titre I ; principal, titre II) est *exclu* du
Total — cohérent avec l'annexe, qui trace « hors dette ». À dire explicitement dans la figure.

---

## 2. Les dispositifs du précis NE s'emboîtent PAS sous une seule nature

Constat central du chantier, à écrire comme caveat : rapporter un dispositif du précis à **une**
ligne de nature est le plus souvent faux. Les séries composantes se filtrent, et se recoupent.

### 2.1 Masse salariale = Rémunérations publiques (identité) [lu]
`masse_salariale_ratios` (rubrique 1.1 du même fichier). S'emboîte exactement dans Fonctionnement.
Couverture 1990→2025. Aucun retraitement.

### 2.2 Compensation ⊂ Interventions publiques [lu]
`compensation-parts`, filtre `famille=budget, nature=budgetaire, poste=total`. La compensation
budgétaire représente **53 % à 82 % des Interventions** selon l'année (2010 : 1 500/2 375 = 63 % ;
2022 : 11 999/14 628 = 82 %). Elle tient donc **dans** Interventions — mais en occupe l'essentiel.
Le **résidu** « autres interventions » (Interventions − compensation − autres postes identifiés)
reste à ventiler (caisses, FCCL, divers).

### 2.3 Transferts aux entreprises publiques : TRANSVERSAUX, et ils chevauchent la compensation
`entreprises-publiques-transferts-budget`, filtre impératif `etat=réalisations,
ventilation=nature, cle=total, derniere_edition=True` (sans le filtre d'édition, la série
**triple-compte** : 2018 donne 24 497 au lieu de 8 392). Même filtré, le total des transferts EP
**dépasse la ligne Interventions** certaines années (2022 : EP ≈ 17 079 MDT, 37 % du budget, vs
Interventions 14 628). Raison : la ventilation EP par nature additionne **rémunération +
fonctionnement + interventions + investissement** des EP — elle **traverse** les lignes 1.1, 1.3 et
2. Les transferts EP ne sont donc **pas** un sous-ensemble d'Interventions.

**Double compte à signaler** : la compensation des carburants transite par la **STIR** (EP) et
celle des céréales/huile par les **Offices** (EP). Une partie des « transferts EP » **recouvre**
donc la ligne compensation. Sommer compensation + transferts EP **sur-compte**. C'est précisément
ce que la **vue compta nat** résout, en classant par *nature économique du flux* (subvention sur
produit) quel qu'en soit le canal.

### 2.4 Dotation FCCL : série administrative DGCT 2008-2019 [lu, documentaliste 2026-11-09]
Deux grains :
- **Voté, LF 1976-1995** : `finances-locales-fccl-lois-de-finances` (cache), prévision, trous.
- **Crédit global annuel distribué, 2008-2019** : série administrative de la DGCT (ministère de
  l'Intérieur), `tunisia-data/.../finances_locales/dgct_portail/fccl.xls`, feuille `fccl`
  (« subventions annuelles du budget de l'État aux collectivités locales », MD) : 162 (2008) →
  480 (2019). **Ni voté LF ni exécution certifiée** : grandeur administrative du gestionnaire,
  plus proche du réalisé. Réf. CSL `dgct-donnees-ouvertes` (déjà dans `references.json`).
- **Trou 1996-2007 et 2020-2025 : non sourcés** (report, §6). Le FCCL est **supprimé au 01/01/2018**
  (LF 2017-66) ; l'intitulé « subventions annuelles » persiste jusqu'en 2019 — continuité à dire
  avec prudence. Ne pas confondre avec le « Fonds de coopération entre collectivités locales »
  (LF 2013) ni la « dotation exceptionnelle ».
À traiter comme accroche + composante **partielle** (2008-2019), pas comme série réalisée bouclée.

### 2.5 Transferts aux caisses de sécurité sociale : série réalisée EN CACHE [vérifié 2026-11-09]
La donnée **existe déjà** : `entreprises-publiques-transferts-par-etablissement`, grandeur
`caisses`, directement branchable par `figtools.series()`. **Réalisé 2017-2023** (+ 2024 voté) :
1 238 (2017) → 2 331 (2023) MDT. Vérifié contre le cache le 2026-11-09 (concorde au millier).
Source : annexe n° 8 des PLF (« transferts et garanties aux EP/EPNA »), réf. CSL
`minfin-transferts-garanties` (déjà présente). Ventilation CNRPS/CNSS/CNAM dans l'entrepôt
(`.../entreprises-publiques/transferts_budget_par_etablissement_2017_2024.csv`).
**Caveats impératifs** :
- Ce n'est **pas** « la subvention d'équilibre » seule : la ligne réunit tout ce que le budget
  verse à la caisse, toutes natures, y compris remboursements de dettes — **non ventilable par
  objet**.
- **Sous-ensemble des transferts EP** (même annexe 8) → **ne jamais sommer caisses + transferts
  EP** : double compte. Transversale (traverse 1.1/1.3/2) comme les EP → `transversal=True`.
- 2024 = **voté** ; inclut 800 MDT « contribution de l'État aux caisses sociales » non ventilés.
- Avant 2017 : non sourcé (annexe 8 sans édition < LF 2020 retrouvée) → report §6.
  CNRPS seule remonte à 2016.
  Filtre : `grandeur=caisses` (déjà `derniere_edition=True` dans le cache).

---

## 3. La vue « comptes de la nation » : regrouper par nature et secteur bénéficiaire

Principe : reclasser les **mêmes** flux budgétaires selon la nomenclature SCNT (nature économique,
secteur institutionnel bénéficiaire), ce qui **dissout les doubles comptes** du §2 (un flux
compte une fois, par sa nature). Matière et périmètres : `annexe-comptes-nation.md`.

Table de correspondance (budgétaire → compta nat), à affiner :

| Flux budgétaire | Case compta nat (nature / secteur) |
|---|---|
| Rémunérations publiques (1.1) | **Rémunération des salariés** des APU |
| Moyens des services (1.2) | **Consommation intermédiaire** des APU |
| Compensation (dans 1.3) | **Subventions sur produits** |
| Transferts EP, part exploitation | **Subventions aux sociétés (SNF)** |
| Subventions caisses / prestations | **Prestations et transferts sociaux** (organismes de sécurité sociale) |
| Équipement direct (2.1) | **FBCF des APU** |
| Transferts EP, part capital ; prêts (3) | **Transferts en capital** / opérations financières |
| Dotation FCCL | **Transferts aux APU locales** (intra-APU) |

**Caveat de périmètre, décisif** [annexe-comptes-nation.md §4] : les **APU** des comptes INS
consolident administration centrale **+ collectivités locales + organismes de sécurité sociale**.
Le budget de l'État désagrégé ici est celui de l'**administration centrale**. La vue compta nat
**ne réconcilie donc pas** au Total budgétaire hors dette : ce sont deux périmètres. On la présente
comme une **relecture par nature**, pas comme une seconde partition du même total. À écrire noir
sur blanc dans la figure.

---

## 4. Logique de réconciliation et résidu

- **Vue budgétaire** : partition stricte, bouclée (`Σ natures = Total hors dette`). Chaque
  dispositif-composante s'y affiche en **part de sa ligne** (masse salariale = 1.1 ; compensation
  en part de 1.3) ou, pour les transversaux (EP), **en surimpression** avec mention explicite
  qu'il traverse plusieurs lignes et n'entre pas dans la somme.
- **Résidu non ventilé** : `Interventions − compensation − (caisses, FCCL quand sourcés)` =
  « autres interventions ». Il est **publié comme résidu**, jamais réparti au jugé.
- **Vue compta nat** : regroupement par nature, **non réconcilié** au total budgétaire (périmètre
  APU). Les deux vues se lisent côte à côte, jamais chaînées.

---

## 5. Contrat de données proposé

Deux livrables de données, engendrés (pas écrits à la main), lus par `figtools.series()` :

1. `budget-desagregation-nature` — la vue budgétaire : colonnes `annee`, `remunerations_MDT`,
   `moyens_MDT`, `interventions_MDT`, `equipement_MDT`, `prets_MDT`, `total_hors_dette_MDT`,
   extraites de `repartition_depenses.xls` (réalisé). Contrôle de bouclage en CI (Σ = Total).
2. `budget-dispositifs-poids` — l'overlay des dispositifs du précis : `annee`, `dispositif`,
   `valeur_MDT`, `ligne_budgetaire_rattachement`, `transversal` (bool), `source_serie`, `filtre`,
   `part_ligne_pct`, `part_total_pct`. Une ligne par (année, dispositif), avec le filtre d'édition
   explicite pour les EP.

La vue compta nat s'appuie sur les séries `cnat-consolide/` de `tunisia-data` (secteur APU,
subventions sur produits, rémunération des salariés) — **pas** sur une reventilation du budget.

---

## 6. Couverture et lacunes (à verser au backlog)

- **Sous-rubriques** : rémunérations dès 1990, moyens/interventions dès **1996** seulement. Avant
  1996, seule la partition de tête (Fonctionnement/Équipement/Prêts) est disponible → la vue
  désagrégée fine commence en 1996.
- **Transferts EP** : impérativement `derniere_edition=True` (sinon double/triple compte). Le total
  EP **traverse** les natures et **chevauche** la compensation (STIR, Offices) → ne jamais sommer
  compensation + EP sans retraiter.
- **FCCL** : voté LF 1976-1995 + série administrative DGCT 2008-2019 (`dgct_portail/fccl.xls`).
  **Trous non sourcés : 1996-2007 et 2020-2025** (reports). Pistes post-2018 : documents
  budgétaires par programme de la mission Intérieur (programme « Affaires locales »), arrêtés
  annuels de répartition au JORT, rapports HIFL, comptes INS des collectivités locales.
- **Caisses** : réalisé 2017-2023 **en cache** (`…par-etablissement`, grandeur `caisses`), réf.
  `minfin-transferts-garanties`. **Avant 2017 non sourcé** (report : annexes transferts LF
  2014-2019). Nature non ventilable par objet (report : RAP Affaires sociales).
- **Double compte caisses ⊂ transferts EP** (même annexe 8) : marquer caisses `transversal=True`
  et ne jamais l'ajouter au total EP. Confirme l'intérêt de la vue compta nat (§3) qui classe
  chaque flux une seule fois par sa nature.
- **Édition LF2026** de `repartition_depenses.xls` disponible (ajoute LF 2026) ; pipeline encore
  sur l'édition 2026-06-09 — rafraîchissement à arbitrer (cf. `tunisia-data/sources/
  minfinances-indicateurs-urls.csv`).
- **Service de la dette** exclu du Total : si le récit « entrées/sorties » doit l'inclure, série à
  sourcer (indicateurs minfin / BCT).
- **Vue compta nat** : périmètre APU ≠ budget central → non réconciliable ; à présenter comme
  relecture, pas comme partition.

---

## 7. Ordre de travail

1. **(cette note)** conception des deux vues + contrat de données. — *fait*
2. Générateur `scripts/…` → `budget-desagregation-nature` + `budget-dispositifs-poids`, avec
   contrôle de bouclage. Prototype validé inline le 2026-11-09 (réconciliation exacte).
3. Module de figure `annexe_budget.py` : `vues_desagregation()` (vue budgétaire empilée, part du
   total, par an) + table ; `vues_comptanat()` (regroupement par nature, périmètre APU) + table.
4. Ancres d'annexe : `#sec-bud-desagregation`, `#fig-bud-desag-budgetaire`,
   `#fig-bud-desag-comptanat` (stables, non traduites) ; section de lecture + caveats §2, §3, §4.
5. Accroches dans les volumes (une PR par volume), après validation de l'annexe.

Ancres proposées (à réserver dans l'en-tête de l'annexe, comme les existantes) :
```
#sec-bud-desagregation      — désagréger les dépenses : deux vues
#fig-bud-desag-budgetaire    — vue budgétaire (par nature, part du total, par an)
#fig-bud-desag-comptanat     — vue comptes de la nation (par nature économique / secteur)
#tbl-bud-desag-correspondance — table budgétaire ↔ compta nat
```

---

## Suivi documentaire (2026-11-09) — caisses < 2017 et FCCL : verdicts

Passe documentaliste pour combler les reports du §6. Conclusion : **aucune valeur réalisée
sourcée à ajouter à l'overlay** ; les gaps sont confirmés non comblables en l'état. Détail :

**Caisses avant 2017 — non sourçable (agrégat).** La seule édition de l'annexe 8 des PLF
antérieure à LF 2021 est **LF 2020**, en **ancien périmètre** : sous le ministère des Affaires
sociales, elle ne liste **que la CNRPS** (+ un « Fonds national de sécurité sociale » distinct),
**sans CNSS ni CNAM** (vérifié par balayage du PDF). Le portail GBO ne publie que 3 éditions du
rapport transferts (LF 2020, 2024, 2025) : **aucune LF 2014-2019**. Donc l'agrégat `caisses`
(CNRPS+CNSS+CNAM) **ne peut pas remonter avant 2017**. Seul point disponible avant : **CNRPS seule
2016 = 352,6 MD** (déjà en cache `cnrps-transferts-etat`) — utilisable comme point isolé à rupture
de périmètre explicite (CNRPS seule 2016 → agrégat dès 2017), jamais comme continuité. → **overlay
inchangé** ; report maintenu avec cette cause précise.

**FCCL 1996-2007 — montant non lu, reconstructible par proxy seulement.** Depuis la LF 1996, la loi
de finances n'imprime plus le montant du fonds. Deux proxies **convergent** : réserve par décret ÷
taux légal (25 % jusqu'en 2006, 18 % dès 2007) et crédit de l'article « interventions » du chapitre
Intérieur → **≈110 MD (1996) → ≈156 MD (2006)**. À ne publier, s'il l'est, que comme **fourchette
reconstruite `[reconstruit, non lu]`**, jamais comme réalisé ni raccordée aux séries LF/DGCT. →
**non intégré** à l'overlay (règle « aucune valeur sans source »). Piste : lois de règlement
1996-2005 (identifiées, non lues) → fiche recherche `r-fccl-montant-1996-2007` à créer.

**FCCL 2020-2025 — la dotation a disparu (suppression 2018).** La série DGCT s'arrête en 2019
(480 MD). Trois substituts sourcés, dans **trois périmètres non raccordables** : (i) **Fonds d'appui
à la décentralisation** (compte spécial, art. 13 LF 2021), subvention de l'État 334→680 MD
(2021-2022, estimations ; `minfin-fonds-speciaux-2022`) ; (ii) **programme « Affaires locales »** de
la mission Intérieur, CP **votés** 977→1 132 MD (LF 2022-2026 ; `lf-2022`…`lf-2026`), périmètre plus
large ; (iii) **comptes INS** du sous-secteur collectivités, transferts courants reçus 484→664 MD
(2020-2025 ; `ins-cnat-2015`), comptabilité nationale. Aucun n'est la « dotation FCCL ». → **overlay
inchangé** ; ces substituts restent des accroches contextuelles, à ne pas chaîner.

**Reports de collecte** (documents ministériels, pas JORT) : éditions annexe 8 < LF 2020 ;
rapports fonds spéciaux annexés aux PLF 2023-2026 ; rapports HIFL ; étude transferts
`bibliotheque.collectiviteslocales.gov.tn/.../Etude sur transferts financiers_Fr.pdf` (à indexer
dans tunisia-data si un chiffrage académique post-2018 est voulu). **Clés CSL** : toutes déjà
présentes (aucune création). **Glossaire** : notions « FCCL » et « Fonds d'appui à la
décentralisation » proposées au terminologue (à vérifier contre le glossaire existant).

---

## Feuille de route « développer l'aspect budgétaire » (arbitrée le 2026-11-10)

Ordre retenu : **1 → 2 → accroches volumes** ; 3 et 4 en second étage.

1. **Boucler le circuit entrées–sorties–solde** — **FAIT le 2026-11-10** (section
   `#sec-bud-solde`, figures `fig-bud-solde` et `fig-bud-service-dette`, séries
   `budget-solde-dette` et `budget-service-dette`, source `service_dette.xls` indexée dans
   tunisia-data, clés CSL `minfin-indicateurs-fp-xls` et `minfin-service-dette-xls` FR+AR).
   Reste du point 1 : **recettes totales non sourcées** (TODO documentaliste dans l'annexe).
   Conception d'origine : Recettes totales (fiscales + non
   fiscales + dons), déficit et dette (`indicateurs_fp_*.xls`, déjà dans l'entrepôt, séries depuis
   1986) ; service de la dette : figure « dépenses hors dette + intérêts » (intérêts APU déjà dans
   `budget-comptanat-apu`). Nouvelle section `#sec-bud-solde` + figures.
2. **Écart voté → rectifié → réalisé, par nature** — **FAIT le 2026-11-10** (section
   `#sec-bud-execution`, figure `fig-bud-execution`, série `budget-vote-realise` ; motif des
   colonnes validé : LF/LFC précèdent leur année ; LF disponibles 2014-2025, LFC 2012-2022).
   Constat versé : dépassements 2017-2022 (pic +10,8 % en 2021), portés par les interventions
   (+20 % en 2020, +41 % en 2022), rémunérations et équipement au voté.
3. **Jonction budget ↔ compta nat, périmètre central.** Tables « Administration centrale »
   (096/097) des mêmes éditions INS ; colonne `perimetre ∈ {apu, central}` dans
   `budget-comptanat-apu` ; réconciliation approchée budget ↔ compte du central.
4. **Vue mission/programme (2020→).** PAP/RAP par mission (entrepôt `pap/` + collecte) ; vue
   « qui dépense » complémentaire de « quoi ». Plus lourd (PDF arabes).
5. **Fond de panier** : fonds spéciaux du Trésor (rapport PLF) ; accroches des volumes vers
   `#fig-bud-dispositifs` (§7 de la conception, une PR par volume) ; reports caisses/FCCL déjà
   documentés ci-dessus.

**État au 2026-11-10 (nuit)** : points 1 (sauf recettes totales) et 2 livrés, rendu FR 0 [?].
Point « accroches volumes » (todo #6) **gaté sur la validation humaine de l'annexe** (règle du
§7 de la conception : une PR par volume, après validation). Points 3-5 non entamés.
Non committé (git bloqué en session) ; figdata à restaurer au déblocage.

**Complément du 2026-11-10 (nuit, suite)** : le point 1 est désormais **entièrement** livré —
recettes totales sourcées (`Série Recettes_non_fiscales.xls` du portail minfin, page
« ressources », indexée dans tunisia-data ; série `budget-recettes-totales` = fiscales +
non fiscales ; figure `fig-bud-recettes-totales` face aux dépenses ; clé CSL
`minfin-recettes-non-fiscales-xls` FR+AR). Caveat porté : dons et privatisation sont DANS les
non fiscales (présentation LOB 2004-42) quand le déficit publié les exclut. Constat vérifié :
les recettes dépassent les dépenses hors dette 13 années sur 40 (dernière : 2010), jamais les
dépenses + intérêts. Également disponible mais non versé : `Série ressources_emprunts_fr.xls`
(même page) — à verser si le récit de trésorerie (emprunt) doit être bouclé.

**Chantier nouveau versé à la feuille de route — « Voies et moyens » (voté).** Le tableau A des
lois de finances (l'évaluation des recettes, côté voté) permettrait une série votée des recettes
par lecture JORT, pendant symétrique de `jort-lf-budget-ordinaire` (titre I des dépenses). Chantier
documentaliste lourd (lecture loi par loi, 1959→) ; gisement GBO (gbo.tn) = documents par mission
(PAP/RAP), pas de séries longues. Non prioritaire tant que le réalisé porte le récit.

**Point 3 livré (2026-11-10, nuit)** : `budget-comptanat-apu` porte désormais une colonne
`perimetre ∈ {apu, central}` — le sous-secteur « administration centrale » est extrait des mêmes
éditions INS (tables 096/097 base 2015, 102/103 base 1997), 2012-2024. **Jonction validée** :
rémunération des salariés du central (20 584 MD en 2021) vs masse salariale budgétaire
(20 175 MD) = écart 2,0 %. Le central est exposé dans l'onglet données de `fig-bud-desag-comptanat`
(empilement inchangé, périmètre APU). Une figure de réconciliation dédiée (central vs budget,
nature par nature) reste possible — second étage.

**Réconciliation central ↔ budget, nature par nature : NON retenue (2026-11-10).** Sondage sur
base 2015, 2017-2024 : seules les **rémunérations** concordent (écart 0,5-4 % entre la
rémunération des salariés du sous-secteur central et la masse salariale budgétaire). Les autres
paires divergent structurellement — « moyens des services » vs consommation intermédiaire du
central : +40 à +105 % (la CI des comptes couvre bien plus que les moyens budgétaires) ;
« équipement » vs FBCF du central : −17 à −50 % (l'équipement budgétaire porte des transferts en
capital et du financement public qui ne sont pas de la FBCF). Une figure de réconciliation
nature par nature serait trompeuse : on s'en tient à la convergence des rémunérations, déjà dite
dans la note de lecture de `fig-bud-desag-comptanat`, et au périmètre `central` exposé dans les
données. Pour aller plus loin il faudrait une table de passage budgétaire↔SCN par opération
(économiste), pas un rapprochement direct des lignes.

**Point 4 — inventaire missions/programmes (documentaliste, 2026-11-10).** Verdict : la vue
« qui dépense » est constructible en trois segments. (a) **Voté par mission 2020-2026 : faible
coût** — tableau unique « répartition des crédits par missions » (~34 missions + 7 spéciales,
engagement + paiement + rappel LF n−1) du Rapport sur le projet de budget annexé au PLF, couche
texte arabe propre ; 5 éditions sur 7 déjà en entrepôt (2021-2025 ; manquent 2020 et 2026 →
collecte) ; contrôle par totaux contre `jort-lf-budget-etat` ; secours : tableau « C » des LF au
JORT (lecture image). (b) **Exécuté par mission : PAS de série agrégée** — le rapport mensuel
d'exécution ne ventile pas par mission (vérifié) ; RAP = 1 PDF/mission/an, jusqu'à 2023 ; lois de
règlement 2021+ introuvables (fiches relancées, 0 candidat). (c) **Avant 2020 : BOOST 2008-2016**
(voté ET payé par chapitre/ministère, 144 029 lignes) — **versé et indexé dans tunisia-data le
2026-11-10** (`data/raw/mizaniatouna/boost_fr.xlsx`, SHA vérifié contre le relevé, portail
d'origine HS 503, copie Wayback ; fiche `sources/mizaniatouna-boost.md`). **Trou 2017-2019**
(fin de BOOST → début des missions) : rapports PLF 2017-2019 par chapitre (celui de 2018 en
entrepôt, couche texte corrompue → OCR) ou décrets de répartition. Autres reports : table de
passage chapitres→missions à documenter pièce par pièce (rupture 2020) ; sens exact des colonnes
du tableau missions à relever à l'en-tête ; clés CSL `mizaniatouna-boost`,
`minfin-rapport-budget-2021`, `-2023` à créer (bibliographe) ; notions glossaire : mission,
mission spéciale, programme, chapitre, crédits d'engagement/de paiement (terminologue).

**Point 4 — vue missions LIVRÉE pour le segment 2021-2025 (2026-11-10, nuit).** Transcription du
tableau « répartition des crédits par missions » des rapports PLF 2021-2025 (documentaliste ;
`docs/notes/budget-missions-vote-2021-2025.{csv,md}` ; **toutes les sommes contrôlées exactes**
contre les totaux imprimés, re-vérifiées indépendamment). Série `budget-missions-vote` (168
lignes, 44 missions ; PLF complet, LF votée recollée par rappel de l'édition n+1 pour 120 lignes
— les scissions/renommages de missions cassent le recollement, surtout 2021). Section
`#sec-bud-missions` + figure `fig-bud-missions` (répartition 2025, évolution des 6 premières).
Correction d'inventaire : le tableau ne distingue PAS engagement/paiement (une colonne de crédits
par exercice). Clés CSL `minfin-rapport-budget-2021` et `-2023` créées FR+AR. **Reports** :
rapports 2020 et 2026 à collecter ; sens « paiement » des تقديرات à contre-éprouver sur un
tableau C ; écarts −200 MD récurrents vs `budget-vote-realise` (périmètre prêts) à trancher ;
exécuté par mission sans série agrégée (RAP un à un, jusqu'à 2023) ; segment chapitres
avant 2020 (BOOST versé) + table de passage ; URLs des clés `-2022/-2024/-2025` à compléter ;
notions glossaire (mission, mission spéciale, programme, chapitre, crédits
d'engagement/paiement) pour le terminologue.

**Segment « chapitres » BOOST livré (2026-11-10, 06 h).** Série `budget-chapitres-paye`
(265 lignes, 41 chapitres, payé 2008-2014 — 2015/2016 partiels écartés) tirée du classeur BOOST
versé ; figure `fig-bud-chapitres` (répartition payée 2014, évolution des 6 premiers) ajoutée à
`#sec-bud-missions`. Constat vérifié : le chapitre de la dette publique est le premier poste payé
chaque année 2008-2014. Clé CSL `mizaniatouna-boost` créée FR+AR. Caveats écrits : payé ≠ voté,
dette comprise (non comparable aux séries hors dette), nomenclature ≠ missions, trou 2015-2020.

**CHANTIER GBO LANCÉ le 2026-11-10 (~06 h 30) — exécuté par mission.** Phase 1 (collecte RAP des missions manquantes, bornée 120 PDF, indexée) en cours ; L'entrepôt (récup 2026-11-04)
détient PAP/RAP/budgets pour les **11 missions de tutelle EP** (RAP : 5 à 9 éditions chacune) ;
les grandes missions hors EP (Éducation, Intérieur, Défense, Affaires sociales, Enseignement
supérieur, Justice) n'y sont **pas**. `gbo.tn` répond en direct (552 PDF listés, politesse
10-12 s/requête ; 1 022 PDF connus de l'Internet Archive). Un « exécuté par mission » complet
2017-2023 exigerait une collecte élargie (~15 missions × ~7 éditions de RAP) puis une extraction
PDF par PDF — chantier data dédié, non lancé (arbitrage humain requis sur le volume). **Cadrage prêt le jour
venu** : (1) collecte bornée sur gbo.tn — RAP seulement, missions manquantes (Éducation,
Intérieur, Défense, Affaires sociales, Enseignement supérieur, Justice, + petites missions),
politesse 10-12 s, indexation dans tunisia-data sur le modèle de gbo-recup-2026-11-04 (fiche +
csv SHA) ; (2) extraction limitée au tableau de synthèse des crédits exécutés de chaque RAP ;
(3) contrôle des totaux contre budget-missions-vote (rappels LF) ; livrable : série
budget-missions-execute, segment 2017-2023.

**CHANTIER GBO LIVRÉ (2026-11-10, matin).** Phase 1 : 98 RAP nouveaux collectés et indexés
(12 missions ; fiches gbo-recuperation-2026-11-10.{md,csv} + manifeste ; Intérieur, Défense et
présidence de la République ne publient AUCUN RAP ; gbo.tn a rétréci ses listages depuis le 04/11
— passer par l'index CDX à l'avenir). Phase 2 : exécution dépouillée en deux lots indépendants
(`budget-missions-execute-lot{A,B}.{csv,md}`, 66 + 75 lignes, chaque valeur fichier+page) ; les
deux couples extraits en double (affaires-religieuses 2021, finances 2020) **concordent
exactement**. Série `budget-missions-execute` (139 lignes, 25 missions, 2016-2023 ; deux régimes
étiquetés : paiements seuls ≤2019, LOB 2019 hors ressources propres ensuite) ; figure
`fig-bud-missions-execute` (payé 2016-2023 des grandes missions ; taux payé/PLF 2021-2023) ; clé
CSL collective `gbo-rap-missions` FR+AR. Todo #7 soldé.
**Reports** : RAP manquants à viser en prochaine passe (AE 2017/2021 ; relig. 2020/2022 ;
culture 2017/2023 ; PG 2017-2019 ; 2017 de la plupart ; agriculture 2019/2021 ; équipement 2017 ;
transport 2017 ; énergie-mines 2018-2019 ; éco-planification 2022-2023 ; finances hors 2020) ;
engagé industrie 2018 non fiabilisé ; 10 PDF à polices corrompues lus via traduction FR (OCR arabe
de revérification souhaitable) ; MAS 2022 à confirmer visuellement ; écart Affaires sociales 2023
(LF 3 302 vs prévu RAP 2 605 MD) à élucider ; **anomalies d'index de la récup 04/11 à reverser
dans tunisia-data** (MAR=Affaires religieuses classés agriculture ; MFFES=Femme-famille classés
finances ; 3 MIME classés environnement ; 4 années d'index fausses — détail dans lotB.md).
