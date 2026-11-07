# Le partage de la valeur ajoutée en Tunisie — enjeux de mesure, état des connaissances et résultats

*Note de travail consolidée (7 novembre 2026), autonome du précis. Elle fusionne la fiche d'état des
connaissances et la note de mesure. Le corps met en avant **les enjeux de mesure** et **les
résultats** ; les détails techniques de construction et de robustesse sont en **annexes** (A à E).
Son insertion éventuelle dans le précis (annexe des comptes de la nation, section « Ce qu'en dit
l'économie » d'un volume) sera décidée ultérieurement.*

Séries sous-jacentes (entrepôt `tunisia-data`) : `cnat-approche-revenus`,
`cnat-approche-revenus-secteurs`, `cnat-approche-revenus-undata`.

---

## 1. Résumé

Le partage de la valeur ajoutée décrit la **répartition fonctionnelle du revenu** : quelle part de
la valeur ajoutée rémunère le **travail** et quelle part le **capital**. En Tunisie, on le
reconstruit à partir des comptes nationaux de l'Institut national de la statistique (INS), prolongés
avant 2005 par les comptes que l'INS transmet aux Nations unies.

**L'enjeu est d'abord un enjeu de mesure.** Le résultat dépend de deux choix : le **périmètre** et le
traitement du **revenu mixte** des entrepreneurs individuels, qui mêle travail et capital. On publie
donc deux mesures, et l'écart entre elles — une dizaine de points — est lui-même un résultat.

Trois constats :

1. **Dans les sociétés non financières** — le périmètre de référence, qui écarte le revenu mixte —
   la part des salaires passe d'environ **46 % de la valeur ajoutée en 2001 à 59 % en 2024** ; le
   taux de marge recule d'autant, de 54 % à 41 %.
2. **Au niveau de l'économie entière**, la part des salaires monte plus modérément, de **36 %
   (1992-2010) à 44 % (2024)** ; une partie de cette hausse reflète le **recul des impôts nets sur la
   production** (de 13 % à 7 % du PIB, montée des subventions), pas seulement un transfert du capital.
3. **Le revenu mixte des ménages pèse ~30 à 34 % du PIB** : c'est pourquoi la part des salaires de
   l'économie entière est si inférieure à celle des sociétés, et pourquoi déclarer le périmètre est
   indispensable.

---

## 2. Les enjeux de mesure

### 2.1 La question

Le partage de la valeur ajoutée répartit celle-ci entre les facteurs qui l'ont produite : la
**rémunération des salariés** (travail) et l'**excédent brut d'exploitation** (capital). Ce que l'on
cherche — le partage *économique* travail/capital — n'est pas donné tel quel par les comptes : deux
difficultés de mesure commandent tout le reste.

### 2.2 Deux difficultés qui commandent le résultat

- **Le revenu mixte.** Chez les entrepreneurs individuels, un seul solde (le « revenu mixte ») mêle
  la rémunération du travail de l'indépendant et le profit. L'inclure dans le capital **sous-estime**
  le travail, d'autant plus que le secteur non salarié est large — et il l'est en Tunisie (annexe,
  § D). D'où le choix d'un **périmètre de sociétés** (sociétés non financières, SNF), où ce solde est,
  par construction, du profit.
- **Le périmètre.** Économie entière, sociétés, SNF : le diagnostic **change avec le périmètre**
  [@askenazy-cette-sylvain-2011]. Deux raisons, non une, de préférer les SNF : elles écartent le
  revenu mixte (ci-dessus) **et** les **loyers imputés des propriétaires occupants** — un excédent
  sans travail, logé chez les ménages, qui déprime la part du travail de l'économie entière. En
  Tunisie, la branche « activités immobilières » des ménages pèse **~6 % du PIB** (§ 4.7) : la mesure
  SNF l'exclut par construction. Un agrégat national stable peut en outre masquer des évolutions
  opposées selon la taille ou le secteur des entreprises [@cas-delaveau-2009-nv133].

### 2.3 Deux mesures, et ce que chacune capte

On calcule donc **deux parts des salaires** :

- **des sociétés non financières** = rémunération des salariés des SNF ÷ valeur ajoutée des SNF —
  la mesure de référence de la littérature, sans revenu mixte ;
- **de l'économie entière** = rémunération des salariés ÷ PIB — plus simple, mais qui range le
  travail indépendant dans le capital.

**L'écart entre les deux est une mesure directe du poids du revenu mixte.** À quoi s'ajoute un
troisième terme, ni travail ni capital : les **impôts nets sur la production** (impôts sur les
produits moins subventions), dont la variation (compensation) déplace mécaniquement les parts
(§ 4.2). La définition comptable exacte et son identité sont à l'annexe A.

### 2.4 Combien pèse chaque secteur — ce que la mesure propre couvre, et ce qu'elle laisse

Avant les résultats, un chiffre de cadrage : **les sociétés non financières ne produisent qu'environ
un tiers du PIB**. La mesure « propre » (§ 4.1) est donc précise mais **partielle**. Répartition de la
valeur ajoutée par secteur institutionnel (en % du PIB) :

| Année | Sociétés non financières | Sociétés financières | Administrations publiques | Ménages (entreprises individuelles, informel) |
|---|---:|---:|---:|---:|
| 2005 (base 1997) | 32,2 | 3,2 | 15,0 | 39,7 |
| 2015 (base 2015) | ~31 | 3,9 | 18,1 | 39,5 |
| 2024 (base 2015) | **36,2** | 4,2 | 17,4 | **35,5** |

*(Le total des quatre secteurs fait ~90-93 % du PIB ; le reste est les impôts nets sur les produits.)*

Le plus gros bloc n'est pas les sociétés mais le **secteur des ménages (~36-40 %)** — entreprises
individuelles et **travail informel** —, légèrement devant les SNF. La part des SNF monte un peu
(32 → 36 %) et celle des ménages recule (40 → 35,5 %) : une **formalisation** modérée. Autrement dit,
la mesure des SNF décrit le **tiers formel et constitué en sociétés** de l'économie, et laisse de côté
le secteur où loge l'informel — dont le partage se lit autrement (§ 4.7).

---

## 3. Ce que dit l'économie — et ce qu'il faut en retenir pour un pays intermédiaire

*Arrêté à novembre 2026 ; rapporte résultats et désaccords, ne recommande rien.*

**Mise en garde liminaire.** La littérature de référence sur le partage de la valeur ajoutée décrit
des économies **avancées et profondément intégrées à la mondialisation** (France, États-Unis, zone
euro). Ses mécanismes et ses faits stylisés **ne se transposent pas tels quels** à un pays à revenu
intermédiaire comme la Tunisie, où d'autres forces dominent. On distingue donc les mécanismes des
économies avancées (§ 3.1), ceux qui commandent le partage dans un pays intermédiaire (§ 3.2), et ce
que dit l'empirique (§ 3.3).

### 3.1 Les mécanismes des économies avancées (pertinence limitée ici)

- **Élasticité de substitution capital/travail.** Sous Cobb-Douglas (élasticité = 1) la part des
  salaires est constante (fait stylisé de Kaldor) ; sous une élasticité **> 1**, l'accumulation du
  capital — automatisation, chute du prix des biens d'équipement — la fait baisser
  [@karabarbounis-neiman-2014]. Débattu : d'autres estiment l'élasticité **< 1** à long terme.
- **Pouvoir de marché, rentes, financiarisation.** Hausse des marges, *superstar firms*, montée des
  dividendes, rentes immobilières (Rognlie) dépriment la part du travail sans changement technique.
- **Mondialisation vue du siège.** Les groupes gardent sur le territoire les activités à forte
  valeur ajoutée et délocalisent le reste [@cas-delaveau-2009-nv133].

Ces ressorts supposent une économie **à la frontière technologique, siège de multinationales, à
secteur formel dominant**. La Tunisie n'est pas dans cette configuration : preneuse de prix,
**receveuse** d'activités délocalisées à faible valeur ajoutée (textile, assemblage), à large secteur
informel et public. Ces mécanismes n'y sont donc pas les premiers en jeu.

### 3.2 Ce qui commande le partage dans un pays intermédiaire

- **La mesure du non-salariat domine tout.** Avec un revenu mixte de ~30 % du PIB (§ 4.4), la part
  des salaires dépend d'abord de la façon dont on traite le revenu des indépendants — le point de
  **Gollin (2002)** : l'estimation est très sensible à l'imputation du travail indépendant, et les
  mesures « naïves » sous-estiment le travail d'autant plus que le non-salariat est large (l'écart
  entre mesures peut dépasser dix points). C'est pourquoi la mesure sur les sociétés (sans revenu
  mixte) est ici la seule robuste.
- **La transformation structurelle (dualisme).** La part agrégée des salaires reflète surtout la
  **composition** de l'économie — déplacement de main-d'œuvre entre agriculture, informel, formel et
  secteur public (Lewis, Kuznets) — plus que la substitution capital/travail à l'intérieur des
  secteurs. Une formalisation ou un recul de l'agriculture déplacent mécaniquement la part mesurée.
- **Le rôle de l'État.** Large emploi public (part des salaires des administrations ~85 %, § 4.3) et
  prix administrés / subventions (compensation), qui déplacent la composante fiscale du partage
  (§ 4.2). En Tunisie, le partage se lit autant à travers l'État qu'à travers le marché.
- **L'ouverture et le taux de change.** Petite économie ouverte, preneuse de prix : la dépréciation
  du dinar et les termes de l'échange pèsent sur le salaire réel et sur le déflateur de la valeur
  ajoutée, donc sur le partage.

### 3.3 Ce que dit l'empirique — et ses limites pour les pays en développement

- **Le « déclin mondial » est d'abord un fait des économies avancées.** Pour les pays émergents et
  en développement, l'évidence est **hétérogène et plus mince** : certains voient leur part du travail
  monter, d'autres baisser, sans tendance uniforme (Guerriero & Sen 2012 ; Guerriero 2019 ; BIT,
  *Global Labour Income Share*). Il n'y a pas de tendance établie pour la région arabe / MENA.
- **Les niveaux et les comparaisons sont fragiles.** Les parts de facteurs varient fortement selon
  la construction (Gollin 2002 ; Guerriero : six mesures, moyenne de l'ordre de 0,73 pour la mesure
  brute, mais forte dispersion). Toute comparaison internationale exige d'harmoniser l'imputation du
  non-salariat, le périmètre et les impôts sur la production (Trapp 2015 pour les pays en
  développement).
- **France, pour mémoire.** Sur le périmètre des SNF, le partage **fluctue autour d'un niveau
  stable** de 1990 à 2007, taux de marge ~30-33 % [@cotis-2009 ; @askenazy-cette-sylvain-2011] ;
  la note du CAS souligne l'hétérogénéité PME / groupes et la montée des dividendes
  [@cas-delaveau-2009-nv133]. Ce point de référence sert de **repère de méthode**, non de terme de
  comparaison directe (§ 4.5).
- **Tunisie.** Les travaux sur le partage fonctionnel y sont rares ; on dispose des comptes nationaux
  (cette note) et de données ILOSTAT (part du revenu du travail), mais pas d'étude de référence.

### 3.4 Établi / débattu (pour un pays intermédiaire)

- **Établi** : la mesure dépend d'abord du traitement du non-salariat (Gollin) ; la composition
  sectorielle (dualisme) pèse autant que la substitution capital/travail ; pas de tendance mondiale
  uniforme pour les émergents.
- **Débattu** : l'interprétation de la hausse tunisienne (formalisation ? compression des marges ?
  recomposition sectorielle ? qualité des comptes ?) ; le bon traitement du revenu mixte — non
  tranché ici.

---

## 4. Les résultats pour la Tunisie

*Par base des comptes (1983, 1997, 2015) ; les niveaux ne se raccordent pas d'une base à l'autre, les
ratios si (robustesse à l'annexe C). Figures 1 à 4, module `partage_va.py`.*

### 4.1 Part des salaires : sociétés non financières contre économie entière (figure 1)

| Année | Base | Salaires, économie entière (% PIB) | Salaires des SNF (% VA) | Taux de marge SNF |
|---|---|---:|---:|---:|
| 1992 | 1983 | 36,3 | — | — |
| 2000 | 1997 | 35,5 | — | — |
| 2005 | 1997 | 35,8 | 45,7 | 54,3 |
| 2010 | 1997 | 38,3 | 47,0 | 53,0 |
| 2015 | 2015 | 39,6 | 55,7 | 44,3 |
| 2021 | 2015 | 42,3 | 55,3 | 44,7 |
| 2024 | 2015 | 43,8 | 59,0 | 41,0 |

La part des salaires des SNF **monte nettement** (~45-47 % dans les années 2000 → 54-59 % depuis
2015) ; le taux de marge recule symétriquement (~54 → 41 %). La part de l'économie entière monte
aussi, plus modérément (36 → 44 %), et reste très inférieure — effet du revenu mixte (§ 4.4). Cette
hausse comporte une **forte part conjoncturelle**, liée à l'atonie de la croissance post-2011
(§ 4.6) : à ne pas lire trop vite comme un gain structurel du travail.

### 4.2 Distribution fonctionnelle de l'économie entière (figure 2)

| Année | Base | Travail (%) | Capital (%) | Impôts nets (%) |
|---|---|---:|---:|---:|
| 1992 | 1983 | 36,3 | 50,4 | 13,3 |
| 2000 | 1997 | 35,5 | 52,2 | 12,2 |
| 2008 | 1997 | 36,1 | 56,1 | 7,8 |
| 2015 | 2015 | 39,6 | 52,0 | 8,4 |
| 2021 | 2015 | 42,3 | 49,2 | 8,5 |
| 2024 | 2015 | 43,8 | 49,6 | 6,7 |

Les trois parts somment à 100. Fait notable : **la part des impôts nets recule fortement** (13 % →
7 % du PIB, sous l'effet de la montée des subventions sur les produits — compensation). Sur
2004-2024, la part du travail gagne environ 8 points, dont **près de la moitié provient du repli des
impôts nets**, non d'un transfert du capital. Pour isoler le seul mouvement travail/capital, la
mesure sur la valeur ajoutée des SNF est la bonne, car elle ne contient pas les impôts sur les
produits.

### 4.3 Part des salaires par secteur institutionnel (figure 3)

| Année | SNF | Sociétés financières | Administrations publiques | Ménages |
|---|---:|---:|---:|---:|
| 2005 (base 1997) | 45,8 | 43,8 | 79,7 | 19,5 |
| 2015 (base 2015) | 55,7 | 58,7 | 80,4 | 16,5 |
| 2021 (base 2015) | 55,3 | 60,7 | 85,6 | 15,1 |
| 2024 (base 2015) | 59,0 | 57,0 | 85,7 | 14,4 |

Structure cohérente : les **administrations publiques** sont intensives en travail (~80-86 %) ; les
**ménages** affichent une part basse (~15 %), leur valeur ajoutée étant dominée par le **revenu
mixte** ; les sociétés se situent entre 45 % et 60 %. Faute de pouvoir distinguer les entreprises par
taille (ce que recommanderait l'alerte de la note du CAS), cette décomposition par secteur joue le
rôle d'avertissement : l'agrégat recouvre des structures très différentes.

### 4.4 Le poids du revenu mixte (figure 4)

| Année | Base | Revenu mixte des ménages (% du PIB) |
|---|---|---:|
| 2005 | 1997 | 31,9 |
| 2015 | 2015 | 33,6 |
| 2021 | 2015 | 30,4 |
| 2024 | 2015 | 30,4 |

Le revenu mixte pèse **~30 à 34 % du PIB** : l'ordre de grandeur du « capital » qui est, pour partie,
du travail indépendant. Il rend compte de l'écart d'une dizaine de points entre les deux mesures
(§ 4.1), et justifie que la référence soit celle des SNF.

### 4.5 Mise en perspective : la Tunisie parmi les pays à revenu intermédiaire (figure 10)

Le terme de comparaison pertinent n'est **pas** les économies avancées (France, États-Unis), dont
les ressorts diffèrent (§ 3.1), mais d'autres **pays à revenu intermédiaire**. La part du revenu du
travail harmonisée de l'OIT (SL_EMP_GTOTL, qui **impute** le travail des indépendants — une mesure
de type Gollin) permet cette mise en regard :

| Part du travail (OIT, % du PIB) | 2010 | 2015 | 2019 | 2024 |
|---|---:|---:|---:|---:|
| **Tunisie** | 43,8 | 46,5 | 45,7 | 45,9 |
| Égypte | 36,1 | 43,2 | 42,9 | 42,1 |
| Jordanie | 41,9 | 42,9 | 44,8 | 45,0 |
| Turquie | 35,3 | 36,7 | 39,2 | 35,4 |
| Moyenne Afrique du Nord + Asie de l'Ouest | 33,3 | 38,2 | 38,7 | 37,0 |
| France (pour mémoire) | 63,4 | 62,2 | 59,6 | 60,6 |

Trois lectures : (i) la Tunisie se situe **au-dessus de la moyenne régionale** (~37 %) et de la
Turquie (~35 %), proche de l'Égypte et de la Jordanie ; (ii) sa hausse se **concentre sur 2010-2015**
(43,8 → 46,5), la fenêtre post-révolution, cohérent avec nos résultats ; (iii) elle reste **très
en-dessous des économies avancées** (France ~60 %), ce qui situe l'enjeu dans un cadre de pays
intermédiaire. **Ancrage utile** : la mesure OIT (ajustée du non-salariat, ~46 % en 2024) dépasse de
quelques points notre mesure « économie entière » naïve (~44 %), ce qui donne une idée de l'ampleur
de l'ajustement Gollin pour la Tunisie (quelques points), sans atteindre la mesure SNF (~59 %).

![](partage/partage_10_pairs_ilo.png)

*Source : OIT, part du revenu du travail (SL_EMP_GTOTL), via Our World in Data ; mesure modélisée,
ajustée du non-salariat.*

Trois précautions subsistent :

- la **hausse** de la part des salaires des SNF se lit d'abord à travers la **transformation
  structurelle** et le **rôle de l'État** (emploi public, compensation), non à travers des mécanismes
  de marges propres aux économies avancées ;
- le **niveau** du taux de marge tunisien (~41-54 %) excède le français (~30-33 %), ce qui est
  courant dans une économie à bas salaires, mais **non comparable** sans harmoniser définitions et
  champ ;
- l'interprétation de la trajectoire (formalisation, recomposition sectorielle, qualité des comptes)
  reste ouverte (§ 3.4). La référence française (Cotis, Askenazy) sert de **repère de méthode** — le
  périmètre des SNF, l'exclusion du revenu mixte — non de point de comparaison substantiel.

---

### 4.6 Structurel ou conjoncturel ? La part du travail est contracyclique (figure 5)

La hausse mesurée (§ 4.1) ne doit pas être lue trop vite comme un gain structurel du travail. Un fait
stylisé bien établi veut que la **part du travail soit contracyclique** : le profit (l'excédent) est
le **résidu** qui absorbe les chocs, tandis que la rémunération est plus **rigide** (rétention de
main-d'œuvre, inertie salariale, et ici un **large secteur public**). Quand la croissance faiblit,
l'excédent recule plus vite que la rémunération, et la part des salaires monte — mécaniquement.

Les données tunisiennes le confirment. La corrélation entre la croissance du PIB en volume et la
variation annuelle de la part des salaires est **−0,70** pour l'économie entière et **−0,51** pour les
SNF (2005-2024, figure 5). Les épisodes de rupture sont les plus parlants :

| Année | Croissance PIB (volume) | Δ part salaires éco. entière | Δ part salaires SNF |
|---|---:|---:|---:|
| 2011 (révolution) | −1,7 % | +1,3 | +2,4 |
| 2020 (COVID) | −8,7 % | +4,3 | +2,8 |
| 2012 (reprise) | +3,9 % | −0,7 | −2,3 |
| 2021 (rebond) | +4,7 % | −0,8 | −1,5 |

**Une part importante de la hausse coïncide donc avec l'atonie de la croissance post-2011**
(révolution de 2011, troubles sociaux et politiques, attentats de 2015, puis choc COVID de 2020) :
elle est, pour partie, la contrepartie comptable d'un **capital qui s'ajuste plus vite que le
travail** à la stagnation du PIB.

**Mais pas seulement.** À croissance comparable, le niveau a aussi dérivé vers le haut : la part des
salaires des SNF vaut ~44-47 % en 2005-2008 (croissance 4-6 %), ~54-55 % en 2015-2019 (croissance
1-2,6 %), 58-59 % en 2023-2024. Le pic conjoncturel de 2020 s'est **partiellement** résorbé
(2021-2022 en baisse) sans ramener le niveau à celui des années 2000. Il y a donc **une composante
conjoncturelle forte et une dérive structurelle** ; les données annuelles sur une vingtaine d'années
ne permettent pas de les séparer proprement, et l'interprétation reste ouverte (§ 3.4).

### 4.7 Le secteur des ménages, le revenu mixte et le travail informel

Le secteur des ménages (~38 % du PIB, § 2.4) est le plus grand, et sa valeur ajoutée est dominée par
le **revenu mixte** (~30-34 % du PIB, § 4.4). Comptablement, **le revenu du travail informel et
indépendant n'apparaît pas dans la rémunération des salariés (D.1) : il est dans le revenu mixte
(B.2g) des ménages**. Trois conséquences :

- la part des salaires de l'économie entière (D.1/PIB) **exclut** le travail informel et le
  sous-estime ;
- la part des salaires des SNF est propre mais **ignore** le secteur des ménages / informel ;
- **l'écart entre les deux mesures est l'effet de mesure de ce secteur**.

**Trois réserves, pour ne pas sur-interpréter.**

1. **Revenu mixte ≠ travail informel.** Le revenu d'exploitation des ménages mêle (a) le revenu mixte
   entrepreneurial (dont l'informel — part travail et part capital) **et** (b) les **loyers imputés
   des propriétaires occupants** (capital pur). Les comptes publiés ne détaillent pas la branche, mais
   la logent dans « Autres activités des ménages », que le volume détaillé des *Comptes de la nation*
   étiquette « activités immobilières » (l'INS y inclut explicitement « l'occupation des logements par
   leurs propriétaires (loyers imputés) », estimée via l'enquête budget-consommation) : elle pèse
   **~6 % du PIB** (8 415 MD en 2021, série `ins-va-branche-base2015`) — borne haute des loyers
   imputés. Autrement dit, sur les ~30 % du PIB de revenu mixte, une part de l'ordre de six points est
   du **capital-logement**, pas du « travail informel » : la mesure de l'économie entière le
   **surestime**, et la mesure SNF l'exclut, loyers imputés compris.
2. **Isoler le travail informel** supposerait d'**imputer** une part travail au revenu mixte (méthode
   de Gollin 2002) — hypothèse explicite — et de retrancher les loyers imputés ; ni l'un ni l'autre
   n'est possible proprement ici.
3. **Une vraie analyse de l'informel** passe par d'**autres sources** — enquêtes emploi et
   micro-entreprises de l'INS (`ins-enquete-emploi`, `ins-micro-entreprises`), qui donnent des
   **effectifs** et non un partage de valeur ajoutée. Relier le revenu mixte des comptes à l'emploi
   informel mesuré par les enquêtes est un exercice distinct, non mené ici.

Ce que l'on peut dire sans hypothèse : la **légère formalisation** (part des SNF qui monte, part des
ménages qui recule, § 2.4) déplace une fraction de l'activité du revenu mixte vers la rémunération
salariée des sociétés, ce qui contribue, à la marge, à la hausse de la part des salaires mesurée sur
l'économie entière.

### 4.8 Effet de structure ou mouvement interne ? (décomposition shift-share)

La hausse de la part des salaires **agrégée** (économie entière) peut venir de deux sources : les
secteurs deviennent plus intensifs en travail (effet **intra-secteur**, *within*), ou l'économie se
déforme vers des secteurs à forte part des salaires (effet de **composition**, *between*). Une
décomposition shift-share de la part des salaires de la valeur ajoutée totale les sépare :

| Période | Base | Δ part salaires agrégée | dont *within* (intra) | dont *between* (composition) |
|---|---|---:|---:|---:|
| 2005→2017 | 1997 | +4,6 pts | +3,3 (71 %) | +1,4 (29 %) |
| 2015→2024 | 2015 | +3,6 pts | +1,2 (34 %) | +2,4 (66 %) |

- **Sur la période récente (2015-2024), la composition domine** (66 %) : la part des SNF dans la
  valeur ajoutée passe d'environ **34 % à 39 %** — une **formalisation** (les SNF, à part des salaires
  ~55 %, grossissent au détriment des ménages à ~15 %). Les deux tiers de la hausse de la part des
  salaires de l'économie entière viennent de ce **déplacement de structure**, non d'un mouvement
  interne généralisé.
- **Mais la part des salaires des SNF, elle, monte vraiment à l'intérieur du secteur** (55 → 59 % sur
  2015-2024). Cette mesure est *intra-secteur* par construction, **insensible au poids des SNF** :
  elle n'est pas un effet de composition.
- **Sur 2005-2017 (base 1997), c'était l'inverse** : l'effet intra-secteur dominait (71 %), la
  composition tenant surtout à la **montée du poids des administrations** (l'État).

**La part des SNF dans le PIB évolue donc bien, et de façon non monotone** : elle recule dans la base
1997 (de ~36 % en 2005 à ~30 % en 2017 de la valeur ajoutée totale) puis remonte dans la base 2015
(de ~34 % à ~39 %) ; le changement de base limite la comparaison longue. Ce mouvement du poids des
SNF est **l'une des causes** de l'évolution du partage mesuré sur l'économie entière.

La version **dynamique** (contributions annuelles *within* / *between*, **figure 9**) confirme ce
partage : les barres *between* (composition) dominent surtout 2015-2024, les barres *within* le début
de période.

![](partage/partage_9_shiftshare_dyn.png)

**Au total, deux mesures, deux histoires complémentaires.** La mesure SNF capte un **mouvement
interne réel** (hausse de la part des salaires des sociétés, en partie conjoncturelle — § 4.6). La
mesure économie entière, elle, est **gonflée par la formalisation** (effet de composition) autant que
par les mouvements internes. Dire que « le partage de la valeur ajoutée évolue » recouvre donc trois
choses distinctes : un mouvement intra-SNF, une recomposition sectorielle, et un cycle — qu'il faut
tenir séparés.

### 4.9 Un effet d'ajustement transitoire ? (le sens est contre-intuitif)

On pourrait penser que la croissance du poids des SNF (formalisation) **déforme transitoirement** leur
part des salaires : si, pendant l'expansion du secteur, le **travail entre plus vite que le capital
ne s'accumule** (salariés formalisés avant que l'excédent ne se construise, coûts d'ajustement du
capital), la part des salaires des SNF serait gonflée le temps de la transition. Le mécanisme — des
**vitesses d'ajustement différentes** du capital et du travail — est réel et important.

Mais le sens empirique est **l'inverse** de cette intuition. La corrélation entre la variation du
poids des SNF et la variation de leur part des salaires est **négative** : **−0,67** en base 1997
(2005-2017), **−0,29** en base 2015 (2015-2024). La part des salaires des SNF **monte surtout quand
le secteur stagne ou recule, et baisse quand il s'étend** — p. ex. 2022 (poids SNF +3,9 pts, part des
salaires −2,6) ou 2013-2014 (poids en recul, part des salaires en forte hausse).

C'est cohérent avec la lecture conjoncturelle (§ 4.6) : l'expansion des SNF coïncide avec de bons
millésimes où l'excédent croît (part des salaires qui baisse) ; la stagnation, avec un excédent
comprimé (part des salaires qui monte). **La déformation transitoire existe donc bien — mais c'est
celle du cycle** (l'excédent, résidu, s'ajuste plus vite que la rémunération), non celle de la
**formalisation-entrée** : on ne voit pas, dans les comptes, le travail entrer plus vite que le
capital dans les SNF en expansion.

Deux réserves : (i) l'excédent des SNF figure à la fois au **numérateur du poids** et au
**dénominateur de la part des salaires**, ce qui rend une part de cette corrélation mécanique ;
(ii) les comptes annuels ne permettent pas d'identifier proprement la dynamique d'ajustement
structurelle — cela demanderait des données d'entreprises ou un modèle.

### 4.10 Révolution, rapport de force salarial, et entreprises publiques dans les SNF

Deux facteurs proprement tunisiens peuvent porter une part **structurelle** de la hausse, au-delà du
cycle (§ 4.6) et de la composition (§ 4.8).

**Un déplacement du rapport de force post-2011.** Après la révolution de 2011, les négociations
salariales (rounds de l'UGTT), les hausses du SMIG et la pression sociale ont pu renforcer
durablement la position du travail. Les comptes montrent une **divergence persistante** : à partir de
2013, la rémunération des SNF croît de 5 à 9 % par an pendant que l'excédent stagne ou recule
(2013 : rém. +9,1 %, exc. −4,3 % ; 2014 : +8,9 % / −2,7 % ; 2023 : rém. +18,6 %, exc. −3,4 %). La part
des salaires monte par ce **décalage rémunération > excédent** (figure 7) — compatible avec un *wage push*
post-révolution, qu'on ne peut toutefois pas séparer proprement de l'effet d'atonie de la croissance
(§ 4.6), les deux poussant dans le même sens.

**Les entreprises publiques pèsent lourd dans les SNF.** Les grandes entreprises publiques (STEG,
SONEDE, Transtu, Tunisair, CPG, SNCFT, offices…) appartiennent au secteur des SNF, avec ~100 000
agents et des salaires administrés. Ces ~100 000 agents ne pèsent que **~2,8 % de l'emploi total
occupé** (stable, 2018-2022) mais leur charge de personnel représente **~16-19 % de la rémunération
totale des SNF** (2017-2022) : des salaires **très au-dessus de la moyenne**, concentrés dans le
secteur formel constitué en sociétés. Le détail :

| Année | Charges de personnel des entreprises publiques (MD) | Rémunération des SNF (MD) | Poids |
|---|---:|---:|---:|
| 2017 | 3 373 | 17 914 | 18,8 % |
| 2020 | 4 113 | 21 594 | 19,0 % |
| 2022 | 4 279 | 26 864 | 15,9 % |

Sur la période visible (2017-2022), ce poids est **stable, voire en léger recul** (18,8 → 15,9 %) :
la rémunération privée des SNF a cru plus vite. La dynamique **récente** n'est donc pas d'abord
publique.

**La fenêtre 2011-2016 est, elle, documentée — par une source de réforme, non par un agrégat.** Le
Livre blanc de la Présidence du gouvernement [@pm-livre-blanc-ep-2018] chiffre le secteur public
marchand pour **2014** : contribution économique **~9,5 % du PIB** (contre **13 % en 2010**), **~4 %
de la population active occupée**, et **~12 % de la masse salariale totale**. Surtout, il date une
**hausse de la masse salariale « à un rythme inhabituel » entre 2010 et 2014** (recrutements, recours
aux sous-traitants, amnistie), pendant que les bénéfices agrégés chutaient de 55 %. C'est précisément
le sens d'une montée de la part des salaires : les salaires progressent quand l'excédent recule.

**Le mécanisme se lit au niveau de l'entreprise.** Sur les états financiers primaires d'un panel de
grandes EP (STEG, Tunisair…), la masse salariale **rattrape puis dépasse** la valeur ajoutée : à la
STEG, l'excédent brut d'exploitation passe de **+555 MD (2014) à −34 MD (2018)**, la masse salariale
(462,7 MD) **dépassant** la VA (446,7 MD) en 2018, et la VA par agent recule de **67 811 à 37 133
DT** ; à Tunisair, la masse salariale (239,3 MD) talonne la VA (242,2 MD) en 2018. Quand les salaires
absorbent une part croissante de la VA, la part du travail **dans ces entreprises** monte
mécaniquement — ce qui alimente la hausse côté SNF.

**Limite à dire franchement.** On ne peut **pas reconstituer l'agrégat** des EP avant 2017 : les
états primaires ne couvrent que les entreprises qui publient (4 à 7 grandes EP par an sur 2010-2016),
on « complète par le bas » sans reconstituer le total. Le Livre blanc **borne et oriente** donc la
contribution publique à la hausse 2011-2016, sans la **mesurer** comme un pourcentage de la
rémunération des SNF. Sources : macro — [@pm-livre-blanc-ep-2018] ; micro — états financiers primaires
des EP (`comptes_primaires_ep`, `grandeurs-productivite-ep`) ; agrégat récent —
`entreprises-publiques-resultats-agreges`, `entreprises-publiques-effectifs-ensemble` ; emploi occupé
— `bct-emploi-occupe`.

---

### 4.11 Décomposition canonique : salaire réel et productivité

La méthode canonique [@askenazy-cette-sylvain-2011 ; @cette-koehl-philippon-2019] décompose la
variation de la part des salaires en **deux termes**, sur le périmètre
des **sociétés** (où les salariés ≈ les travailleurs, sans revenu mixte) :

> Δln(part des salaires) = Δln(**salaire réel au prix du produit**) − Δln(**productivité du travail**)

les deux déflatés par le **même** prix (le déflateur de la valeur ajoutée, qui s'annule donc dans
l'identité). La part monte quand le salaire réel croît plus vite que la productivité. On l'applique
aux **SNF**, avec l'emploi des SNF ≈ **salariés déclarés à la CNSS** (la carte institutionnelle vérifiée,
annexe G) et le déflateur du PIB. Fenêtre propre :
base 1997, 2005-2016 (SNF par secteur **et** CNSS disponibles ; pas de chaînage de base).

| Cumul 2005→2016 (base 1997) | points de log |
|---|---:|
| **Part des salaires des SNF** (45,7 % → 55,3 %) | **+19** |
| = salaire réel au prix du produit | **+21** |
| − productivité du travail | **+2** |

**La hausse de la part des salaires est entièrement un salaire réel qui dépasse une productivité quasi
plate** — le profil d'un *wage push* non accompagné de gains de productivité.

**Réserve décisive — l'emploi, et la formalisation.** Le partage entre les deux termes dépend du
dénominateur d'emploi. Ici l'emploi des SNF (CNSS déclarés) croît de **+32 %** sur 2005-2016, en partie
par **formalisation** (des travailleurs passent du non-déclaré au déclaré) : cela **gonfle l'emploi
mesuré et déprime la productivité mesurée**. La productivité « plate » est donc en partie un artefact
de formalisation ; le vrai partage *wage push* / productivité ne se tranche pas sans série d'emploi
corrigée (annexe B.4). C'est **le** test de sensibilité à porter — et il est décisif :

| 2005-2016 (SNF, Δpart = **+19,2** log pts, invariant) | emploi | salaire réel | productivité |
|---|---:|---:|---:|
| **CNSS déclarés** | +32 % | +20,9 | **+1,7** |
| **RNE sociétés** (SNF privé, registre INS) | +26 % | +25,3 | **+6,1** |
| **enquête emploi salarié** | +22 % | +28,3 | **+9,1** |

**La hausse de la part est un fait invariant ; son attribution, non.** Selon le dénominateur, la
productivité a crû de **+2 %** (CNSS, gonflé par la formalisation) à **+9 %** (enquête) — **jamais
plate**. Le meilleur périmètre, le **RNE « sociétés »** (emploi salarié formel des sociétés privées,
Répertoire national des entreprises de l'INS, 2000-2024, dont le total recoupe la CNSS déclarée),
donne **+6 %**. Le diagnostic « *wage push* sur productivité stagnante » n'est donc **pas robuste** au
choix de l'emploi ; ce qui l'est : les **salaires réels ont dépassé une productivité qui, elle, a bien
crû**.

**Le segment récent le confirme.** En **base 2015 (2015-2024)**, avec le RNE sociétés (emploi +19 %),
la part des SNF monte de **+5,6 log pts** (55,7 → 59,0 %) par un salaire réel **+17** sur une
productivité **+11** — les deux croissent, la part monte par un léger dépassement. (Deux bases,
**jamais chaînées**.)

**Complément — le coin prix conso / prix VA.** On peut scinder le salaire réel *au prix du produit*
en salaire réel *à la consommation* × (prix conso / prix VA). Depuis 2023, les prix à la consommation
dépassent le déflateur de la VA de **2 à 4 points par an** (IPC +9,3 % contre VA +5,1 % en 2023) : ce
**terme de prix** a poussé la part des salaires à la hausse, distinct d'un gain de salaire réel à la
consommation. Que les SNF excluent par construction l'immobilier et le non-salariat rejoint le choix
de périmètre de [@cette-koehl-philippon-2019]. Sources : SNF `cnat-approche-revenus-secteurs` ;
déflateur `ins-va-branche-base2015` / PWT ; IPC `bct-ipc-base2015` ; emploi CNSS.

## 5. Ce que le praticien retient

1. **Toujours dire le périmètre** (économie entière / sociétés / SNF) et le **traitement du revenu
   mixte** : sans cela, un chiffre de « part des salaires » ne veut rien dire.
2. **Ne pas comparer les niveaux** entre pays ni entre bases sans harmoniser définitions et champ.
3. **Un agrégat stable peut masquer des évolutions opposées** par taille ou secteur
   [@cas-delaveau-2009-nv133] ; en Tunisie, la décomposition par secteur institutionnel (§ 4.3) joue
   ce rôle d'alerte.
4. **Pour un pays intermédiaire, lire le partage à travers la composition** (informel, secteur
   public, agriculture) et l'**imputation du non-salariat**, non à travers les marges des entreprises :
   les ressorts des économies avancées (automatisation, dividendes, délocalisation de siège) n'y sont
   pas les premiers en jeu (§ 3).
5. **Ce que les données tunisiennes ne permettent pas** : distinguer marges et dividendes ; isoler le
   logement ; remonter la mesure SNF avant 2001, l'économie entière avant 1992 ; décomposer par
   taille d'entreprise ; décomposer salaire réel / productivité (annexe B, § limites).

---

## 6. Limites

- **Niveaux non comparables** entre bases (ruptures 1997, 2015) ni entre pays (taux de marge SNF
  tunisien > français, non comparable sans harmonisation).
- **Avant 2005**, seule la mesure de l'économie entière existe (l'ONU ne ventile pas par secteur) :
  le biais du revenu mixte y est entier. La mesure SNF ne remonte qu'à **2001** ; avant, il faudrait
  les volumes INS 1 à 10 (papier) ou le CD du volume 2005-2009, non disponibles en ligne.
- **Décomposition salaire réel / productivité** non produite : la seule série d'emploi (emploi
  occupé, 2007-2024) est trop courte et non salariée. En revanche, le **terme de prix relatif** de
  cette décomposition (coin prix conso / prix VA) **est** calculé (§ 4.11) : seules manquent les
  grandeurs de **quantité**.
- **Revenu mixte non imputé** : on s'en tient à la mesure robuste « sociétés seules » ; une
  imputation (hypothèse explicite) relèverait la part du travail de l'économie entière, mais serait
  conventionnelle.
- **Révisions et millésimes** : incertitude de révision ≈ un demi-point (annexe C) ; léger écart
  ONU/INS en 2010-2011.
- **Public / privé dans les SNF** : les comptes ne séparent pas les entreprises publiques des
  privées au sein des SNF ; la donnée propre aux entreprises publiques ne commence qu'en 2017, de
  sorte que leur contribution à la hausse de 2011-2016 n'est pas mesurable (§ 4.10). On ne peut pas
  non plus séparer le *wage push* post-révolution de l'effet conjoncturel (§ 4.6), les deux agissant
  dans le même sens.

---

## 8. Ce qu'on pourrait faire selon les données récupérées

L'analyse actuelle est contrainte **par les données, non par les techniques** (annexe C). Voici,
par donnée à récupérer, la technique qu'elle débloquerait et la question qu'elle trancherait.

| Donnée à récupérer | Source | Technique débloquée | Ce que ça trancherait |
|---|---|---|---|
| **Emploi salarié par secteur, 2013-2024** | INS Enquête nationale sur l'emploi (on a 1999-2012 propre) | **complète** la décomposition salaire réel / productivité (le terme de prix est déjà fait, § 4.11) ; effet-emploi vs effet-salaire | si la hausse vient du **salaire par tête** (wage push) ou de l'**emploi** |
| **Agrégat EP charges de personnel par année, 2010-2016** (le panel d'EP et le Livre blanc 2018 sont déjà exploités, § 4.10) | Rapports Cour des comptes « clôture » ; annexes 9 des LF | part **agrégée** du public dans la rémunération des SNF, année par année | passer du cadrage **borné** (Livre blanc) à une contribution **mesurée** 2011-2016 |
| **SNF publiques / privées** et **loyers imputés** (B.2 vs B.3) | comptes INS détaillés / dataportal | part des salaires **privée** pure ; **ajustement Gollin** maison | séparer marché, État et logement dans le partage |
| **Éditions INS pré-2001 / CD 2005-2009** | volumes 1-10 (papier) ; CD des comptes 1997-2007 | séries plus longues ; **tests de rupture** (Chow/Bai-Perron), **filtre cycle/tendance** | la part **structurelle** de la hausse, nette du cycle |
| **Données pairs harmonisées complètes** (déjà amorcé § 4.5) | ILOSTAT, Penn World Table, base Guerriero | comparaison de **niveaux** harmonisés | où se situe vraiment la Tunisie parmi ses pairs |

**Techniques immédiatement applicables, déjà faites ici** : bandes d'incertitude (figure 8),
shift-share dynamique (figure 9), comparaison pairs OIT (figure 10, § 4.5). **Techniques à écarter
tant que les séries sont courtes** : filtre HP, cointegration, tests de rupture — elles donneraient
une fausse précision sur ~20-25 points annuels traversés par deux changements de base.

**Priorités** : (1) l'emploi salarié 2013-2024 (débloque la décomposition salaire/productivité) ;
(2) l'agrégat annuel des charges de personnel des EP 2010-2016 — le cadrage macro (Livre blanc) et le
panel d'entreprises sont déjà en main (§ 4.10), reste à agréger pour **mesurer** la contribution
publique plutôt que la borner.

---

# Annexes — construction, contrôles et robustesse de la mesure

## Annexe A — Cadre comptable

Les comptes décomposent la valeur ajoutée (et, agrégée, le PIB) selon l'**approche des revenus**
(codes du Système de comptabilité nationale entre parenthèses) :

> **PIB = rémunération des salariés (D.1) + impôts sur la production et les importations nets de
> subventions (D.2 − D.3) + excédent brut d'exploitation et revenu mixte (B.2g)**

- **D.1** : rétribution du **travail** salarié (salaires et traitements bruts + cotisations sociales
  employeur) ;
- **B.2g** : rétribution du **capital** ; pour les entrepreneurs individuels, **revenu mixte** (profit
  + travail indépendant mêlés) ;
- **D.2 − D.3** : troisième terme, ni travail ni capital.

## Annexe B — Données et construction

### B.1 Sources

| Jeu | Contenu | Couverture | Série d'entrepôt |
|---|---|---|---|
| Éditions INS, approche revenus **par secteur** | VA, rémunération, excédent par secteur institutionnel | base 1997 : 2005-2017 ; base 2015 : 2015-2025 | `cnat-approche-revenus-secteurs` |
| Éditions INS **base 1983**, comptes des SNF | VA, rémunération, excédent des SNF | 2001-2008 | *(idem, secteur `snf`, base 1983)* |
| **ONU** (UNdata), compte de génération du revenu | D.1, B.2g, D.2−D.3 de l'**économie entière** | base 1983 : 1992-2008 ; 1997 : 1997-2011 ; 2015 : 2015-2023 | `cnat-approche-revenus-undata` |

Parsers : `parse_cnat_approche_revenus.py` (éditions, y compris SNF base 1983),
`parse_undata_approche_revenus.py` (ONU).

### B.2 Extraction et contrôles

**Éditions INS (base 1997/2015).** Le tableau « PIB selon l'approche des revenus » donne, par
secteur, rémunération et revenu d'exploitation, puis un bloc total. L'extraction impose l'**identité
comptable** PIB = rémunération + impôts − subventions + revenu d'exploitation : écart maximal
**0,1 MD** (arrondi) sur 76 lignes-éditions. Ancres lues à la main et retrouvées exactement :
rémunération 2021 = 55 588,7 MD, 2015 = 35 572,6 MD, 2020 = 50 242,1 MD ; PIB 2012 = 70 354,5 MD.

**Comptes des SNF, base 1983 (2001-2008).** Les éditions base 1983 portent une section « Comptes des
sociétés non financières » (compte de production + exploitation). On y prend rémunération et
excédent, et l'on pose **VA_SNF = rémunération + excédent** (on exclut les impôts indirects que le
SCN 1968 impute au secteur ; justification à l'annexe C.2). Garde-fou par ligne. L'édition 2003-2007
(OCR corrompu) est écartée ; ses années sont couvertes ailleurs.

**ONU (économie entière, 1992-2023).** Le compte de génération du revenu (table 4.1 UNdata) donne
D.1, B.2g, D.2−D.3 par version du SCN (1968→1983, 1993→1997, 2008→2015), en dinars (÷10⁶).
**Contrôle de raccord décisif** : sur 2005-2009 (base 1997), la rémunération ONU est **identique au
dixième** à l'INS (2005 : 14 998,9 MD des deux côtés).

### B.3 Règles de raccordement

- **Jamais de chaînage entre bases** (base 1997 ≈ +10 % sur 1983, base 2015 ≈ +6 % sur 1997) ; tracé
  **par segments**, trait vertical aux ruptures.
- **Un an, une base.** Économie entière : 1983 ≤1996, 1997 de 1997 à 2014, 2015 ≥2015. SNF : 1983
  (2001-2004), 1997 (2005-2014), 2015 (≥2015).
- **Priorité INS sur ONU** sur les recouvrements (2005+).

### B.4 Données manquantes (à récupérer)

Récapitulatif des trous identifiés, avec ce que chacun bloque. **Rappel de provenance** : **trois**
séries d'emploi sont **primaires INS** — l'emploi occupé total (2007-2024), le salarié par statut
1999-2012, et le **salarié formel privé par forme juridique du RNE** (2000-2024 ; les formes sociétés
≈ emploi des SNF privées) ; OIT, ILOSTAT, WDI, PWT, BM en sont **dérivées**. Détail des pistes
d'emploi : annexe G ; définition et source de chaque série : annexe H.

| Donnée manquante | Ce que ça bloque | État |
|---|---|---|
| ~~Salarié par statut 2013-2024 pour les SNF~~ **— comblé** | décomposition salaire réel / productivité des SNF | **Résolu** : le **RNE sociétés** (primaire INS, 2000-2024) donne l'emploi des SNF privées, et sert la décomposition (§ 4.11). Reste dérivé/estimé : le salarié **économie entière** par statut après 2012 (ILOSTAT → 2019) |
| **Heures travaillées, série annuelle** — **immatériel** | décomposition **en heures** (vs en têtes) | mesurées seulement en **2019 (44,3 h/sem, ENPE INS) et 2021 (43,3, autre enquête)** — pas de série ; ni l'INS ni ILOSTAT (dérivé de l'ENPE) n'en publient en continu. **Mais ~44 h/sem stables** → décomposition par tête ≈ par heure : gap **sans effet** sur § 4.11 |
| **Salarié par secteur d'activité, série longue** — **en partie comblé** | shift-share salaire/productivité **sectoriel** | le **RNE** donne l'emploi salarié formel privé par **forme juridique** (2000-2024) et par **activité** dans les éditions récentes (2024) ; reste à consolider la ventilation sectorielle longue |
| **Loyers imputés / immobilier isolés** | part des salaires **hors logement** ; ajustement Gollin maison | non publié ; noyé dans « Autres activités des ménages » (~6 % du PIB, **borne haute**, `ins-va-branche-base2015`) |
| **SNF publiques / privées (VA)** | isoler les SNF privées | emploi privé : **RNE sociétés** ; VA : retirer les EP ne déplace la part que de **±2-3 pts** mais la **VA EP agrégée n'est pas publiée** — **vérifié par OCR arabe du rapport MdF** (produits, charges, résultats seulement ; ni VA, ni achats consommés, ni dotations agrégés) ; reconstructible seulement par le bas (comptes primaires, incomplet). Second ordre (§ 4.10, annexe G) |
| **SNF avant 2001 ; économie entière avant 1992** | prolonger les séries ; part structurelle nette du cycle | volumes INS 1-10 (papier) / CD 2005-2009 ; l'ONU ne remonte pas avant 1992 |
| **Entreprises publiques avant 2017** | contribution des EP à la hausse **2011-2016** | bornée par le Livre blanc (§ 4.10), non mesurée ; agrégat annuel à reconstituer (Cour des comptes, annexes 9 LF) |
| **Comparateurs** | contre-champ international | BM Global Productivity DB s'arrête en **2018** ; indices ITCEQ à récupérer (site bloque) |

## Annexe C — Robustesse de la mesure

### C.1 Robustesse au changement de base

Les **niveaux** changent fortement à chaque rebasage, mais ce sont des **ratios** qu'on publie. Sur
les années où deux bases coexistent, on calcule le ratio dans les deux bases.

**Part des salaires des SNF** :

| Recouvrement | Années | Écart base à base (points) |
|---|---|---|
| base 1983 → 1997 | 2005-2008 | −0,24 ; −0,06 ; +0,10 ; +0,54 |
| base 1997 → 2015 | 2015-2017 | +1,16 ; −0,01 ; −1,19 |

**Part des salaires de l'économie entière** :

| Recouvrement | Années | Écart base à base (points) |
|---|---|---|
| base 1983 → 1997 | 1997-2004 | entre −0,82 et +0,20 (|écart| < 1) |
| base 1997 → 2015 | 2015-2017 | −0,58 ; −0,37 ; +0,81 |

L'écart entre bases reste **inférieur à ~1 point** alors que les niveaux diffèrent de 6 à 10 % : le
changement de base déplace les niveaux mais **quasi pas les ratios**. La part des salaires et le taux
de marge se lisent donc en continu à travers 1983 → 1997 → 2015, à condition de ne jamais chaîner les
niveaux et de tracer par segments.

**Zone fragile, écartée par construction.** Pour l'économie entière, la série base 1983 (ONU) s'écarte
de **2 à 3 points** de la base 1997 sur **2005-2007** (base en voie d'abandon) : le raccord n'emploie
la base 1983 que **jusqu'en 2004**. (Pour les SNF, l'écart 2005-2008 reste < 0,6 point ; simple
contrôle.)

### C.2 Robustesse aux révisions d'édition et au choix du dénominateur

**Révisions entre millésimes.** À base égale, la dispersion de la part des salaires d'une édition à
l'autre est faible : médiane **0,5 point** (SNF, 24 couples base-année multi-éditions), **0,3 point**
(économie entière) ; maxima ~2-3 points sur années fortement révisées (SNF 2012 base 1997 :
47,1→49,5 % ; économie entière 2010 : 36,4→38,3 %). On retient l'édition la plus récente ;
incertitude de révision ≈ **demi-point**. La **figure 8** trace la part des salaires des SNF avec,
autour de la médiane, l'étendue entre éditions — une **bande d'incertitude**, non une ligne.

![](partage/partage_8_bande_revision.png)

**Choix du dénominateur en base 1983.** La base 1983 impute des impôts indirects au secteur, pas les
bases 1997/2015. Le contrôle, au raccord 2005-2008, est sans appel : seule `VA = rémunération +
excédent` reproduit la base 1997.

| Année | rém/(rém+EBE) **[retenu]** | rém/VA de production | rém/(rém+impôts+EBE) | base 1997 (réf.) |
|---|---:|---:|---:|---:|
| 2005 | 45,9 | 40,9 | 38,8 | 45,7 |
| 2006 | 46,8 | 41,8 | 39,7 | 46,8 |
| 2007 | 44,3 | 40,0 | 37,7 | 44,4 |
| 2008 | 43,9 | 40,0 | 37,1 | 44,4 |

La définition retenue coïncide avec la base 1997 à **0,1-0,5 point** ; inclure les impôts indirects
éloigne de **4 à 7 points**. Le choix de dénominateur est **la condition de la comparabilité
inter-bases**.

## Annexe D — Formules de calcul

Pour une année et une base : `D1` rémunération des salariés, `B2g` excédent + revenu mixte,
`TAX = D.2 − D.3` impôts nets, `PIB = D1 + B2g + TAX`. Pour un secteur `s` : `rem_s`, `exc_s`,
`VA_s = rem_s + exc_s`.

| Indicateur | Formule | Couverture |
|---|---|---|
| Part du travail (économie entière) | `100 × D1 / PIB` | 1992-2025 |
| Part du capital (économie entière) | `100 × B2g / PIB` | idem |
| Part des impôts nets | `100 × TAX / PIB = 100 − travail − capital` | idem |
| **Part des salaires des SNF** | `100 × rem_snf / VA_snf` | 2001-2025 |
| **Taux de marge des SNF** | `100 × exc_snf / VA_snf = 100 − part_salaires_snf` | 2001-2025 |
| Part des salaires d'un secteur | `100 × rem_s / VA_s` | 2005-2025 |
| Poids du revenu mixte | `100 × exc_menages / PIB` | 2005-2025 |

## Annexe E — Reproductibilité

- **Séries** : `cnat-approche-revenus`, `cnat-approche-revenus-secteurs`, `cnat-approche-revenus-undata`.
- **Parsers** : `parse_cnat_approche_revenus.py`, `parse_undata_approche_revenus.py`.
- **Calculs et figures** : `precis/fr/figures/partage_va.py` (`figure`, `figure_distribution`,
  `figure_secteurs`, `figure_revenu_mixte`, `figure_cyclicite` + tables). La contracyclicité croise
  `pib-croissance-volume`.
- **Figures PNG + tables CSV** : `~/relecture-compta-nat/partage/`.

## Annexe F — Notions à glossaire

Partage de la valeur ajoutée / répartition fonctionnelle du revenu ; part des salaires (*labour
share*) ; taux de marge ; excédent brut d'exploitation ; revenu mixte ; élasticité de substitution
capital-travail. (Valeur ajoutée, EBE, revenu mixte sont déjà ouverts en passe 1 du glossaire pour
l'annexe des comptes de la nation.)

---

## Références

**Méthode** (choix du périmètre des sociétés non financières, traitement du revenu mixte) :
- Cotis, J.-P. (2009), *Partage de la valeur ajoutée, partage des profits et écarts de rémunérations
  en France*, INSEE / La Documentation française. Figures 1.1.a (part des salaires dans la VA des
  SNF) et 1.1.b (taux de marge des SNF), 1949-2007. [@cotis-2009]
- Askenazy, P., Cette, G., Sylvain, A. (2011), *Le partage de la valeur ajoutée*, Repères, La
  Découverte. [@askenazy-cette-sylvain-2011]

**Mise en perspective** :
- Delaveau, B. (2009), « Faut-il rééquilibrer le partage de la valeur ajoutée et des profits en
  faveur des salariés ? », *La Note de veille* n° 133, Centre d'analyse stratégique.
  [@cas-delaveau-2009-nv133]
- Karabarbounis, L., Neiman, B. (2014), « The Global Decline of the Labor Share », *Quarterly Journal
  of Economics*, 129(1). [@karabarbounis-neiman-2014]

**Pays en développement et méthode d'imputation du non-salariat** (à verser dans la bibliographie) :
- Gollin, D. (2002), « Getting Income Shares Right », *Journal of Political Economy*, 110(2),
  p. 458-474 — sensibilité de la part du travail à l'imputation du revenu mixte.
- Guerriero, M., Sen, K. (2012), « What Determines the Share of Labour in National Income? A
  Cross-Country Analysis », IZA DP 6643 ; et Guerriero, M. (2019), *The Labor Share of Income Around
  the World*, ADBI Working Paper 920 — panel incluant les pays en développement, hétérogénéité des
  mesures.
- Trapp, K. (2015), *Measuring the Labour Income Share of Developing Countries*, WIDER WP —
  construction pour les pays en développement.
- Organisation internationale du travail, *The Global Labour Income Share and Distribution* (ILOSTAT).

**Données primaires** : INS, *Les comptes de la nation* (éditions 2001-2005 à 2021-2025)
[@ins-cnat-2015] ; comptes transmis aux Nations unies (UNSD) [@undata-sna].

*PDF à récupérer dans `tunisia-data` (règle du précis) : Cotis 2009, Note de veille 133,
Karabarbounis-Neiman 2014, Gollin 2002, Guerriero 2019, Trapp 2015.*

## Annexe G — Emploi, productivité et carte institutionnelle

(Résumé autonome ; la version longue vit hors de cette note.)

**La question.** La décomposition salaire réel / productivité (§ 4.11) exige une série d'**emploi des
SNF**. Aucune caisse ni enquête ne la donne directement — d'où des choix à expliciter.

**Ce que mobilise la littérature.** Les travaux tunisiens sur la productivité (ITCEQ, Banque mondiale,
FMI) prennent l'**emploi de l'enquête emploi** (occupé ou salarié) et la **comptabilité nationale** ;
le niveau firme passe par les **microdonnées du Répertoire national des entreprises** (décompositions
within/between). Personne ne construit l'emploi à partir des déclarés sociaux.

**Primaire vs dérivé.** Seules deux séries d'emploi sont **primaires INS** : l'emploi occupé total
(enquête emploi, 2007-2024) et le salarié par statut (1999-2012), plus les instantanés du recensement
(2014, 2024). **OIT, ILOSTAT, WDI, PWT, Banque mondiale en sont toutes dérivées** (re-traitements des
mêmes comptes INS et de l'enquête emploi) : leur désaccord sur la part du travail (de 39 % à 54 % en
2019) n'est **pas** une triangulation, mais une seule donnée traitée de plusieurs façons (traitement
du non-salariat).

**Carte institutionnelle (vérifiée sur la méthodo INS).** Le critère de classement est la
**comptabilité complète** : sociétés + indépendants **au réel** (quasi-sociétés) + entreprises
publiques commerciales → **SNF** ; banques, assurances → SF ; fonction publique, collectivités,
établissements administratifs, hôpitaux → APU ; indépendants **au forfait** + informel + loyers
imputés → **Ménages** (revenu mixte). Conséquences : l'informel du *secteur* est hors SNF, mais les
salariés non déclarés d'une firme formelle y sont ; la CNRPS est surtout l'**APU** (plus ~113 000
agents d'établissements/entreprises publics non étatiques, mesurés par écart aux effectifs de la
fonction publique).

**Options d'emploi et choix retenu.** (A) enquête emploi (standard, comparable) ; (B) déclarés
CNSS+CNRPS (formel, mais non standard et CNRPS = APU) ; (C) **hybride, retenu** : enquête emploi pour
l'économie entière, **CNSS déclarés** comme proxy de l'emploi des SNF (les ajustements − sociétés
financières / + entreprises publiques en CNRPS se compensent, à ±5 %). Biais à porter : les
non-déclarés des firmes formelles gonflent D.1/VA des SNF mais pas les déclarés CNSS, et la
**formalisation** gonfle la croissance de l'emploi CNSS (§ 4.11).

**Entreprises publiques dans les SNF.** Les retirer des SNF (pour isoler les SNF privées) ne déplace
la part des salaires que de **±2-3 points**, de signe indéterminé faute de VA EP agrégée propre (la
VA comptable des EP de compensation — Office des céréales, STIR — et à prix volatils — ETAP — est
distordue). La VA des SNF de l'INS, elle, est à prix de base (compensation en D.31, hors VA du
producteur) : elle est propre. **La part des salaires des SNF de l'INS reste la référence robuste.**

## Annexe H — Séries mobilisées (définition et source)

| Code | Contenu | Source |
|---|---|---|
| `cnat-approche-revenus` | PIB par l'approche des revenus (rémunération des salariés, revenu d'exploitation, impôts nets), totaux, par base | INS, *Comptes de la nation* |
| `cnat-approche-revenus-secteurs` | Mêmes grandeurs par secteur institutionnel (SNF, SF, APU, ménages) | INS, *Comptes de la nation* |
| `cnat-approche-revenus-undata` | Compte de génération du revenu, économie entière, 1992-2023 | ONU (données INS transmises, UNdata) |
| `ins-va-branche-base2015` | VA par branche d'activité, prix courants et de l'année précédente, 2020-2025 (déflateur de la VA) | INS, banque de données (statistiques/75) |
| `bct-ipc-base2015` | Indice des prix à la consommation, base 100 = 2015 | Banque centrale de Tunisie |
| `bct-emploi-occupe` | Emploi occupé total, 2007-2024 | INS, enquête emploi (via BCT) |
| `ins-enquete-emploi` | Population occupée par statut (salarié, indépendant, aide familial…), 1999-2012 | INS, enquête nationale population-emploi |
| `ins-micro-entreprises` | Enquête quinquennale sur les micro-entreprises (part des salariés sous le SMIG) | INS |
| `comptes_primaires_ep` | VA et ses composantes, états financiers primaires de ~20 grandes entreprises publiques | États financiers EP (BVMT, rapports) |
| `entreprises-publiques-resultats-agreges` | Produits/charges d'exploitation, charges de personnel, résultats du secteur EP (77-88 entreprises), 2017-2022 | Ministère des finances, rapport EP (Annexe 9 LF) |
| `entreprises-publiques-effectifs-ensemble` | Effectif total des entreprises publiques (hors banques et caisses) | Ministère des finances, rapport EP |
| `grandeurs-productivite-ep` | VA, masse salariale, VA par agent d'un panel d'EP | États financiers EP |
| RNE sociétés (emploi salarié formel privé par forme juridique) | Emploi salarié formel du secteur privé par forme juridique (sociétés = SA, SARL, SUARL ; personnes physiques), 2000-2024 ; les formes **sociétés** ≈ emploi des SNF privées | INS, Répertoire national des entreprises |
| CNSS salariés déclarés | Salariés déclarés (secteur privé + public commercial), annuel | CNSS, annuaires statistiques |
| CNRPS affiliés actifs | Affiliés actifs (agents publics + établissements/entreprises publics), 2000-2020 | CNRPS, guides statistiques |
| PWT (`rgdpna`, `labsh`) | PIB réel et part du travail (ajustée Gollin), Tunisie, 1960-2023 | Penn World Table 11.0 (via FRED) |

Les codes en minuscules-tirets renvoient aux séries de l'entrepôt `tunisia-data` (chacune avec sa
fiche de provenance et son contrôle d'extraction) ; les autres sont nommées par leur source.

---

## Arrêt et revue

Note arrêtée au **7 novembre 2026**. À revoir à la prochaine revue annuelle : actualisation des
synthèses internationales sur la part du travail (post-2020) ; extension de la mesure SNF avant 2001
si l'on obtient les volumes INS 1-10 ou le CD 2005-2009 ; décomposition salaire réel / productivité
si une série d'emploi salarié longue devient disponible.
