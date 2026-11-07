# Chantier C — l'annexe « Les comptes de la nation » (plan d'architecte)

Note de plan, ouverte le 6 novembre 2026. État : **en cours**. Elle fixe la forme et la structure
de l'option C de la vision compta-nat (`docs/notes/vision-compta-nationale.md`) avant toute
rédaction. Elle ne rédige pas l'annexe ; elle dit quoi écrire, où, et dans quel ordre de la chaîne
éditoriale. Décision humaine « go C » du 06/11/2026.

---

## 1. La décision de forme : une annexe, pas un volume (pour commencer)

La vision posait C comme « volume transversal *Le cadre macroéconomique* ou grande annexe ». On
tranche pour **une annexe du site**, sœur de `annexe-pib.qmd`, et non un volume — pour trois
raisons :

1. **Cohérence de nature.** Un volume du précis documente un champ de l'action publique par sa
   **loi** (fiscalité, retraites…). Les comptes de la nation sont un **système statistique**, pas un
   corps de droit : leur place est une annexe méthodologique, comme l'annexe PIB, pas un dixième
   volume de « droit ».
2. **Non-duplication.** La cohérence transversale (rôle 3 de la vision) est déjà en grande partie
   servie par le **registre des dénominateurs** (`registre-denominateurs-pib.yml`) et par l'annexe
   PIB. Une annexe qui ajoute les comptes des secteurs institutionnels suffit à compléter le
   dispositif sans réécrire les volumes.
3. **Réversibilité.** Commencer par une annexe est peu risqué. Si le contenu grossit (séries
   publiées, figures, section « ce qu'en dit l'économie » des agrégats), on pourra la promouvoir en
   volume ; l'inverse serait coûteux.

**Nom proposé** : « Les comptes de la nation » (fichier `precis/fr/annexe-comptes-nation.qmd`).
Sous-titre dans l'esprit de l'annexe PIB : « Annexe commune aux volumes : secteurs institutionnels,
les trois approches du PIB, et les grandeurs auxquelles le précis rapporte ses chiffres ».

**Frontière avec l'annexe PIB.** L'annexe PIB garde tout ce qui touche au **PIB-dénominateur et aux
bases** (1983/1997/2015, écarts, rétropolation, « quel PIB dans quelle source », « comment lire une
part du PIB »). La nouvelle annexe renvoie à elle pour les bases et traite **le reste des comptes** :
secteurs, séquence des comptes, approches du PIB, agrégats de revenu et d'épargne, concordance avec
les volumes. Aucune section ne doit se chevaucher ; chaque mention de base renvoie à l'annexe PIB.

## 2. Structure proposée de l'annexe (sections et ancres stables)

Ordre « rupture au premier plan, détail replié » des conventions (§ 4) adapté à une annexe
méthodologique :

| Section | Ancre stable | Contenu | Source |
|---|---|---|---|
| Pourquoi cette annexe | `#sec-cn-pourquoi` | ce que les comptes apportent au lecteur du précis ; renvoi à l'annexe PIB pour les bases | — |
| Les secteurs institutionnels | `#sec-cn-secteurs` | ménages, SNF, SF, administrations publiques, ISBLSM, reste du monde ; ce que chacun regroupe | note doc. § 1 |
| La séquence des comptes | `#sec-cn-sequence` | production → exploitation → revenu → utilisation → capital ; VA → PIB → RNDB → épargne | note doc. § 1 |
| Les trois approches du PIB | `#sec-cn-approches` | production/VA, dépense/emplois, revenus ; bouclage, une année récente chiffrée | note doc. § 2 |
| Les grandeurs citables | `#sec-cn-agregats` | RNB, RDB des ménages, consommation finale, VA par secteur : définition, base, série d'entrepôt | note doc. § 3 |
| Quel volume touche quel compte | `#sec-cn-concordance` | table de concordance volumes ↔ comptes (voir § 3 ci-dessous) | note doc. § 4 |
| Ce que les comptes ne disent pas | `#sec-cn-limites` | informel, économie non observée, révisions, délais ; renvoi annexe PIB pour les ruptures | note doc. § 5 |

Blocs longs (séquence complète d'un compte, nomenclatures) en `.chronologie-repliable` ou tableaux
repliés, comme ailleurs dans le précis.

## 3. La table de concordance volumes ↔ comptes (cœur transversal)

C'est l'apport propre de C. Elle relie chaque volume à sa « case » des comptes, pour que le lecteur
situe une grandeur du précis dans l'ensemble macro. Esquisse (à sourcer et compléter par la note
documentaire, § 4) :

| Volume du précis | Compte / agrégat des comptes de la nation | Nature du lien |
|---|---|---|
| Rémunérations publiques | rémunération des salariés ; VA des administrations publiques | la masse salariale publique est une part de ces agrégats |
| Prestations sociales | compte des organismes de sécurité sociale (prestations, cotisations) | transferts sociaux en nature et en espèces |
| Cotisations sociales | compte des OSS (ressources) ; revenu des ménages | prélèvements sociaux |
| Compensation | subventions sur les produits (compte des administrations) | dépense de subvention |
| Finances locales | administrations publiques locales | sous-secteur des APU |
| Fiscalité | impôts sur la production et les importations, impôts sur le revenu | ressources des APU |
| Retraites / caisses | compte des OSS ; revenu des ménages (pensions) | prestations et équilibres |
| Entreprises publiques | sociétés non financières et financières publiques | sous-ensemble des SNF/SF |
| Marché du travail | emploi, rémunération des salariés | lien emploi ↔ comptes |

La concordance **documente**, elle ne recalcule pas : chaque ligne renvoie au volume et au compte,
sans réconcilier les périmètres (une réconciliation chiffrée serait un chantier distinct, à part).

## 4. Place dans la chaîne éditoriale, et ordre des pas

L'annexe est un contenu éditorial : elle suit la chaîne, et **s'arrête à la revue humaine**. Aucun
`.qmd` n'est écrit avant que la matière sourcée existe.

| Pas | Rôle | Livrable | État |
|---|---|---|---|
| 1 | documentaliste | `docs/notes/annexe-comptes-nation.md` (note sourcée) | **lancé le 06/11/2026** |
| 2 | bibliographe (versement) | clés CSL des éditions INS citées, dans les `references.json` | à lancer après la note |
| 3 | terminologue (passe 1) | ancres des notions à glossaire (secteur institutionnel, RDB, épargne nationale…) | après versement |
| 4 | architecte | plan détaillé de l'annexe à partir de la note (affine le § 2 ci-dessus) | après la note |
| 5 | rédacteur | `precis/fr/annexe-comptes-nation.qmd` | après 2-4 |
| 6 | terminologue (passe 2) | définitions au glossaire | après rédaction |
| 7 | bibliographe (clôture) | résolution des `[@clés]`, dry-run | après rédaction |
| 8 | humain | revue, câblage arabe (`scripts/arabe_cablage.py`), rendu FR/AR | fusion |

**Garde-fous rappelés** : le français est la source (pas de `.qmd` arabe à la main) ; au moment où
le chapitre est ajouté, lancer `uv run python scripts/arabe_cablage.py` et rendre FR **et** AR ;
aucune valeur sans source ; le précis ne nomme pas le modèle ; aucun commit ni PR sans l'humain.

## 5. Ce que ce plan ne tranche pas (pour la revue humaine)

1. **Annexe seule, ou amorce d'un futur volume ?** Le plan fait le pari de l'annexe ; à confirmer.
2. **Jusqu'où va la concordance** (§ 3) : simple table de renvois, ou amorce d'une réconciliation
   chiffrée des périmètres (masse salariale publique vs rémunération des salariés, etc.) ? La
   réconciliation est un chantier lourd, à décider à part.
3. **Figures** : l'annexe publie-t-elle des figures de séries (VA par secteur, RDB des ménages) via
   `figtools`, ou reste-t-elle textuelle en v1 ? Des figures supposent des séries d'entrepôt propres
   (certaines existent, d'autres seraient à construire — voir la note documentaire, § 5).
4. **Lien avec le registre B3** : la section concordance et le registre des dénominateurs se
   recoupent ; décider lequel fait foi pour quoi (le registre par ratio reste l'outil machine ;
   l'annexe en est la lecture).
