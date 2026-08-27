# Rapport INS « Caractéristiques des agents de la fonction publique et leurs salaires 2010-2021 » — analyse et suggestions d'illustration

Source : INS, publication bilingue AR/FR, juin 2023 (effectifs) + novembre 2022 (salaires).
Réf. CSL : `ins-fonction-publique-2021`. Données brutes : dépôt `tunisia-data`,
`data/raw/ins-fonction-publique-salaires-2010-2021/` (26 tableaux `tabN` + annexes
annuelles 2010-2020). Libellés FR en dernière colonne de chaque tableau.

## 1. Périmètre et réserves (à rappeler à chaque usage)

- **Champ = fonction publique civile de l'État** (+ collectivités locales). N'inclut
  **pas** les corps à statut autonome (militaires, FSI, magistrats — cf. B.2) ni les
  entreprises/établissements publics (B.3/B.4). Cohérent avec la statistique du
  **régime indiciaire** (les agents sont classés en catégories A1→D).
- **Rupture de série « collectivités locales »** : 6,7 k (2016) → 17,7 k (2017) dans
  tab1/tab11 — changement de périmètre/comptage, à signaler avant tout graphe en série
  longue incluant les CL.
- **Coquille source repérée** : tab20 (salaire par catégorie) étiquette « Catégorie A2 »
  la ligne A3 en français — corriger au retraitement (l'arabe الصّنف الفرعي أ3 fait foi).
- Le rapport donne **effectifs + salaires moyens**, mais **pas** la masse salariale en
  % du PIB/budget (cf. autres sources : minfin, FMI, BM).

## 2. Synthèse des données disponibles (26 tableaux)

### Effectifs et structure
- **tab1** — effectifs totaux 2015-2021 : 601,9 k → 669,3 k (hors CL : 595 → 641,9 k ;
  CL : voir rupture). Taux d'accroissement décroissant : 2,1 % (2015) → 0,77 % (2021).
- **tab2** — par sexe : femmes 217,3 k → 248,6 k ; **part féminine ≈ 37 %** stable
  (36,1 % en 2015 → 37,2 % en 2021).
- **tab3 / tab4** — structure d'âge (2021 et série %) : **vieillissement** net — les
  55-59 ans passent de 8,1 % (2015) à 11,0 % (2021) ; moins de 25 ans ≈ 4 %. Cœur de
  pyramide 40-54 ans (≈ 48 %).
- **tab5 / tab6 / tab7 / tab8** — par catégorie statutaire (déjà exploité en B.1,
  @fig-categories-statutaires). Bascule A1↑ (98,7 → 198,3 k) / A3↓ (78 → 36,4 k).
- **tab9** — ouvriers par unité (1/2/3) : total 107,1 → 125,3 k ; bascule unité 1↓
  (57,8 → 55,8 k) / unité 2↑ (34,2 → 54,3 k).
- **tab10** — **agents par ministère × statut (fonc./ouvriers/autres), 2021** : Éducation
  196,7 k (29 %), Intérieur 90,3 k, Défense 86,4 k, Santé 81,8 k, Enseignement sup.
  34,3 k, CL 27,4 k. C'est la table qui fonde le **recoupement Défense** de B.1
  (fonctionnaires Défense = 69,243 k = Σ A1-D, hors militaires).
- **tab11** — agents par ministère 2015-2021 (série).
- **tab12 / tab13** — par **fonction d'encadrement** (خطة وظيفية) : SG/DG ≈ 9,7 k,
  directeurs 2,4 k, sous-directeurs 5,3 k, chefs de service 11,2 k ; total postes
  fonctionnels 21,8 → 28,6 k (forte hausse des chefs de service).
- **tab14-17** — **flux entrants/sortants 2021** : 34 096 entrants, 29 001 sortants
  (solde +5 095). Par statut (tab16) : fonctionnaires 19 927 entrants / 15 001 sortants.
  Par âge/sexe (tab14/15) et par ministère (tab17).

### Salaires (2015-2020, dinars courants)
- **tab18** — salaire mensuel : brut avec contributions 1 461,8 → 2 261,5 ; brut sans
  contributions 1 248,7 → 1 905,2 ; **net 916,7 → 1 309,4** (+42,8 % sur 2015-2020).
- **tab19** — salaire brut par type (fonctionnaires / ouvriers / autres).
- **tab20** — **salaire brut par catégorie** 2015-2020 : A1 2 446 → 3 126 ; A2 1 655 →
  2 481 ; A3 1 369 → 2 139 ; B 1 238 → 2 135 ; C 1 142 → 1 888 ; D 1 144 → 1 804.
  **Resserrement de l'éventail** : ratio A1/D 2,14 (2015) → 1,73 (2020).
- **tab21** — salaire brut des ouvriers par unité.
- **tab22 / tab23** — **distribution par tranches de salaire** (%) : déformation nette
  vers le haut — « moins de 1200 d » 22,3 % (2015) → 0,1 % (2020) ; « 2400 d et + »
  passe de ~5 % à ~53 %. Effet de la compression vers le haut + inflation.
- **tab24** — distribution du salaire en dinars (déciles/tranches).
- **tab25** — **salaire brut+contrib / brut / net par ministère, 2020** : éventail de
  2 910 (Ens. sup.) / 2 755 (Justice) / 2 741 (Présidence) à 1 820 (Aff. sociales) /
  1 630 (CL) / 1 518 (autres établ.). Moyenne 2 262 / 1 905 / 1 309.
- **tab26** — salaire brut par sexe × ministère, 2020 (permet un écart H/F par ministère).

## 3. Suggestions d'illustration par chapitre

> Règle éditoriale : jamais un chiffre ponctuel sans vue d'évolution ; périmètre rappelé
> (FP civile indiciaire) ; toujours via `figtools.figure_tabs` (graphe + tableau + note de
> lecture), données figées dans `_seriescache/`.

### Introduction du livre (agrégats)
- **[déjà fait]** effectifs FP (@fig-effectifs-fp), catégories (@fig-categories-statutaires),
  masse salariale/PIB (@fig-masse-salariale-ratios).
- **[NOUVEAU] Pyramide / structure par âge 2015-2021** (tab4) — illustre le
  vieillissement (enjeu retraites + renouvellement). Aire empilée des tranches d'âge.
- **[NOUVEAU] Part des femmes 2015-2021** (tab2) — courbe simple ≈ 37 %, avec lecture
  « féminisation stable, contrastée par ministère » (renvoi tab26).

### B.1 — Régime indiciaire (chapitre le plus directement servi par l'INS)
- **[NOUVEAU] Effectifs par ministère 2021** (tab10) — barres horizontales empilées
  fonc./ouvriers/autres ; sert de support visuel à la section « ventilation par
  ministère et ses limites » (#sec-ventilation-ministere) et au recoupement Défense.
- **[NOUVEAU] Salaire net moyen par ministère 2020** (tab25) — barres triées ;
  éventail Ens. sup./Justice ↔ Aff. sociales/CL. Réserve : moyennes, hétérogénéité des
  corps.
- **[NOUVEAU] Salaire brut moyen par catégorie 2015-2020** (tab20, après correction du
  libellé A3) — illustre concrètement la hiérarchie indiciaire **et** son resserrement
  (ratio A1/D 2,14→1,73). Très complémentaire du tableau des grilles.
- **[NOUVEAU] Distribution des fonctionnaires par tranche de salaire 2015 vs 2020**
  (tab22) — deux histogrammes ou aires empilées ; montre la translation vers le haut.
- **[NOUVEAU] Encadrement : postes fonctionnels 2015-2021** (tab13) — optionnel, montre
  la croissance des chefs de service / sous-directeurs.

### B.2 — Régime statutaire autonome
- **Pas de données INS exploitables** (corps exclus du champ). À illustrer **en creux** :
  un encadré méthodologique rappelant que ces corps n'apparaissent pas dans l'INS
  (recoupement Défense de tab10) — pas un graphe, mais un schéma de périmètre possible.
  Le proxy chiffré reste SIPRI (dépense militaire), déjà signalé en TODO B.2.

### B.3 / B.4 — Régime conventionnel public / marché contrôlé
- **Hors champ INS** (entreprises/établissements publics non couverts). Aucune
  illustration depuis ce rapport ; chercher du côté du *Rapport sur les entreprises
  publiques* (minfin) et de la BCT/INS comptes par branche « activités financières ».

## 4. Prochaines étapes techniques (si on retient ces figures)
1. Étendre `tunisia-data/scripts/clean_ins_fonction_publique.py` pour produire les
   `processed/` manquants : `ministere_effectifs.csv` (tab10/11),
   `salaire_par_categorie.csv` (tab20, **corriger A3**), `salaire_par_ministere.csv`
   (tab25), `structure_age.csv` (tab4), `sexe.csv` (tab2),
   `distribution_salaire.csv` (tab22).
2. Pousser ces séries dans `precis/_seriescache/` (snapshot versionné).
3. Créer les modules `figures/*.py` correspondants + blocs `{python}` dans les `.qmd`,
   sur le modèle de `categories_statutaires.py` / `@fig-categories-statutaires`.
4. Note de lecture systématique + réserve de périmètre. Rendre FR puis laisser le CI
   traduire l'AR.
