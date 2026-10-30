# Conventions de rédaction du précis

## 1. Le précis documente la loi, jamais le modèle

C'est la règle qui commande toutes les autres, et elle est absolue dans le texte rendu des
**volumes**. La documentation générale — le `README`, la page « À propos » du site — peut dire
d'où viennent les tableaux et nommer le modèle ; un chapitre, jamais.
`scripts/check_pas_de_modele.py` ne contrôle donc que les fichiers des volumes.

`openfisca-tunisia` **ne se mentionne pas** dans les volumes du précis : ni son nom, ni « le modèle »,
ni « les paramètres du modèle », ni le fait qu'un chiffre en soit tiré. Le lecteur du précis
lit du droit socio-fiscal tunisien ; il n'a pas à savoir qu'un modèle de microsimulation
existe, encore moins à en connaître les défauts.

Le rapport entre les deux dépôts est l'inverse de ce que cette mention laisserait croire.
**L'arborescence de paramètres du modèle sert de base de données aux paramètres de la
législation du précis**, autant que faire se peut : c'est un magasin de valeurs datées et
sourcées, alimenté par le dépouillement du *Journal officiel*. Le précis, lui, permet de
comprendre ce qu'on fait dans le modèle — pas l'inverse. Un tableau engendré depuis cette
base présente donc des **faits de droit**, appuyés sur le texte cité dans le tableau
lui-même, et non « ce que porte le modèle ».

**Une seule porte vers cette base : l'onglet « Base législative » des tableaux engendrés**
(« القاعدة التشريعية » en arabe). Il donne, pour chaque grandeur du tableau, un lien vers sa
page publique sur `parameters.tn.tax-benefit.org`, qui en montre toutes les valeurs datées
et leurs références. C'est la seule exception à la règle : l'onglet ne nomme pas le modèle,
ses liens sont engendrés avec le tableau (`tables/<nom>.liens.yml`) et jamais écrits à la
main, et la prose n'y renvoie pas. `scripts/verifier_liens_base_legislative.py` contrôle
que chaque lien répond.

### Ce qui en découle, cas par cas

**Le mot « modèle » n'est pas interdit ; c'est l'outil de calcul du précis qui l'est.** Les
modèles des économistes sont des termes de la discipline et s'écrivent tels quels : « modèle
d'équilibre général », « modèle économétrique » d'une étude citée. De même les emplois du
droit — « le modèle français de carrière », « le modèle de la déclaration ». On ne les
maquille pas en « simulation » pour passer le contrôle : `scripts/check_pas_de_modele.py`
les reconnaît, et c'est lui qu'on corrige s'il se trompe.

**Un fait vrai du seul modèle ne se publie pas comme un état du droit.** Une date qu'un
paramètre porte à tort, une valeur que le modèle calcule d'une certaine façon, un croisement
qu'il opère : rien de tout cela n'est un fait de droit. L'unique exception est la conservation
provisoire d'une série historique importante, encadrée au § 3 : elle est publiée pour rendre
son évolution repérable, sans être qualifiée d'établie.

**Ce que les textes n'établissent pas se dit sans nommer le modèle.** « Le partage des
1,20 % entre maladie, maternité et décès n'est fixé par aucun texte identifié » est une
phrase du précis. « Le modèle porte 0,24 % de maternité, sans source » n'en est pas une :
elle parle du modèle. La première dit au lecteur ce qu'il doit savoir — le tableau qu'il
lit comporte une part non attestée ; la seconde lui parle d'un outil dont il n'a que faire.

**Une incertitude sur un chiffre publié se signale par un `callout`**, en disant ce qui est
attesté et ce qui ne l'est pas, avec le niveau d'attestation. Jamais en désignant sa source
technique.

## 2. Où va ce qu'on ne publie pas

Quatre destinations, selon la nature de la remarque. C'est la seule voie : rien ne reste
dans le texte rendu.

| Nature | Destination |
|---|---|
| Manque éditorial — un texte à lire, une section à écrire | `<!-- TODO (rôle) : … -->` dans le `.qmd`, à l'endroit concerné |
| Défaut du modèle — valeur, date, assiette, formule | *Issue* sur `openfisca/openfisca-tunisia`, plus une ligne dans `docs/notes/backlog-modele.md` |
| Référence à verser ou à corriger dans Zotero | `docs/notes/biblio-a-rapatrier.md` |
| Recherche infructueuse — un texte attendu qu'on ne trouve pas | Constat neutre dans le texte (« ce décret n'est pas identifié ici »), ancre `<!-- RECHERCHE r-… : … -->` à côté, fiche rejouable dans `docs/recherches.yml` |

Le commentaire `<!-- TODO (rôle) : … -->` est la forme déjà employée dans tout le corpus :
le rôle entre parenthèses est celui qui doit reprendre le travail — `documentaliste`,
`bibliographe`, `terminologue`, `rédacteur`. Il est invisible au rendu et survit aux
passes de traduction.

`docs/notes/backlog-modele.md` tient la liste de ce que la rédaction a constaté sur le
modèle, chaque ligne renvoyant à son *issue*. Il existe pour que le constat ne se perde pas
entre le moment où on le fait et celui où quelqu'un le corrige — et pour qu'on ne le refasse
pas deux fois.

### Les recherches infructueuses

Le texte ne raconte pas la recherche : ni « n'a pas été retrouvé », ni « au *Journal
officiel* jusqu'au numéro du… », ni la liste des fascicules lus. Il dit le constat, court et
neutre, et en tire la conséquence de droit (« le régime n'a donc, en l'état des textes
identifiés, ni taux ni formule »). À côté, une ancre cachée renvoie à la fiche :

```
Ce décret n'est pas identifié ici.

<!-- RECHERCHE r-dl2024-4-art33 : décret d'application de l'art. 33 du décret-loi n° 2024-4 (voir docs/recherches.yml) -->
```

La fiche, dans `docs/recherches.yml`, garde la trace **exécutable** de la recherche : ce qu'on
a cherché, et chaque passe — quand, sur quelles sources, jusqu'où, avec quelles lacunes, pour
quel résultat. Elle permet de la relancer quand le *Journal officiel* a paru depuis, ou de
l'élargir à un terme neuf. Schéma (détaillé en tête du registre) :

```yaml
- id: r-dl2024-4-art33
  objet: décret fixant les taux … (décret-loi n° 2024-4, art. 33)
  ou: [precis/fr/retraites/_secteur_prive.qmd#sec-travailleuses-agricoles]
  requetes:
    titres_fts: ['"travailleuses agricoles"']   # FTS5 sur titre et objet de jort_cache
    titres_like: []                             # LIKE, accents et casse neutralisés
    iort_ar: [العاملات الفلاحيات]               # intitulés arabes (iort, jort_cache)
    plein_texte: [2024-4, 4 لسنة 2024]          # texte des fascicules du corpus local
    depuis: 2024-10-23                          # rien n'est examiné avant
  passes:
  - date: 2026-09-23
    role: documentaliste
    sources: [jort_cache, corpus_local, pist]
    couverture: "… jusqu'au n° 93 de 2026, sauf le n° 58 ; 2025 en partie seulement"
    couvert_jusqu_au: 2026-09-18                # ce que l'outil compare
    resultat: aucun                             # ou la clé CSL du texte trouvé
  a_faire: [lire le JORT n° 58 de 2026]         # facultatif : les lacunes à combler
```

Les commentaires ci-dessus n'ont pas leur place dans le registre : l'outil le réécrit sous
forme canonique et ne conserve que son en-tête.

```
uv run python scripts/recherches.py verifier            # ancres ⇔ fiches (lancé en CI)
uv run python scripts/recherches.py verifier --avertissements   # fiches exposées sans terme arabe
uv run python scripts/recherches.py lister --perimees   # couvertes moins loin que jort_cache
uv run python scripts/recherches.py relancer <id> [--depuis AAAA-MM-JJ] [--sonder-pist]
uv run python scripts/recherches.py elargir <id> --terme "…" --source iort_ar
uv run python scripts/recherches.py passe <id> --resultat aucun --couverture "…" \
    --couvert-jusqu-au AAAA-MM-JJ --sources jort_cache corpus_local pist
```

`relancer` rend des **candidats** — texte, fascicule, pages, adresse pist.tn —, jamais une
conclusion : chacun se lit au fascicule. Il dit aussi ce qu'il n'a pas pu parcourir
(fascicules absents du corpus local, fichiers « fr » qui sont en réalité l'arabe, base
arrêtée avant la période ; avec `--sonder-pist`, fascicules parus que la base ignore). Un
objet borné dans le temps — « texte antérieur au décret n° 81-939 » — porte une `periode`
(`jusqu_au`, et le `motif` tiré de l'objet) : la fiche cesse d'être périmée quand sa dernière
passe atteint la borne, et `relancer` ne cherche pas au-delà. Une recherche dont la période
croise 2011 ou 2013 et après porte des termes arabes dans `iort_ar`, joué aussi sur les titres
de l'index : une part des notices n'y a qu'un intitulé arabe
(`docs/notes/outillage-sources.md`, § 1 g) ; `verifier` avertit, sans échouer, des fiches qui
n'en portent aucun. Quand le texte est
trouvé, la passe porte sa clé CSL, la fiche devient `resolu`, et la réserve du `.qmd` cède
la place à la règle sourcée ; `verifier` refuse une ancre qui survit à sa fiche résolue.
`check_jargon_depouillement.py` refuse, dans le texte rendu, les tournures du récit de
recherche.

## 3. Ton et chiffres

Rappel des deux règles déjà en vigueur, parce qu'elles se combinent avec la première.

**Ton documentaire, jamais polémique.** On documente, on ne dénonce pas. Un défaut du droit
se constate ; il ne s'indigne pas.

**Jamais un chiffre ponctuel sans sa vue d'évolution** — un graphique ou un tableau daté.
Un taux en vigueur sans son histoire ne dit pas ce qu'il vaut.

**Le budgétaire, les rapports extérieurs et les évaluations économiques ne sont pas au même
niveau.** Trois familles de chiffres portent sur un même dispositif et ne disent pas la même
chose : le *budgétaire* — lois de finances, lois de règlement, exécution du budget, évaluations
du ministère des Finances — ; les *rapports extérieurs*, c'est-à-dire ceux des institutions
internationales, FMI, Banque mondiale et OCDE en particulier ; les *évaluations économiques* —
études d'incidence, d'impact, de coût, d'auteurs ou d'institutions. Un organisme tunisien qui
ne fait que reprendre les chiffres du ministère des Finances — la Banque centrale dans son
rapport annuel — reste du budgétaire : on le dit relais, et on nomme la source qu'il cite. Elles ne se mêlent ni dans un même tableau ni
dans un même fil de récit, et ne se présentent pas sur le même plan : le budgétaire d'abord, en
entonnoir (la dépense globale, sa décomposition par type, puis les gros plans) ; les autres
ensuite, dans des sections titrées comme telles. Toute étude extérieure vient avec **sa
méthode**, en une phrase au moins avant ses chiffres : qui, quelles années de données, quel
périmètre, comment la grandeur est calculée (déclarations fiscales ou enquête, coût brut ou net,
hypothèses). Une estimation dont la source ne décrit pas la méthode le dit — « méthode non
décrite par la source qui la rapporte » — ou ne figure pas.

La comparaison reste permise, et utile : **sur un graphique**, on peut superposer des séries de
familles différentes dès lors qu'elles sont censées traiter des mêmes dispositifs, à condition
que la légende distingue les familles et que les changements de méthode et les ruptures de série
soient expliqués. Pour le temps long, on préfère une mesure cohérente — part du PIB, part des
dépenses publiques — aux niveaux en dinars courants.

**Tout PIB dit sa base, et s'il est rétropolé.** Chaque fois qu'une grandeur est rapportée au
PIB — dans un tableau, une figure, une phrase —, on sait et on dit dans quelle base de comptes
nationaux ce PIB est exprimé, et si la valeur est celle de la base d'origine ou une valeur
rétropolée dans une base postérieure. Quand la source ne le dit pas, on l'écrit : « base non
précisée par la source ». Deux PIB de bases différentes ne se chaînent jamais en silence : une
série en part du PIB se trace par segments de base, et le changement de base se signale comme
une rupture de série. L'explication des bases, de leurs écarts de niveau et des rétropolations
n'est pas répétée de chapitre en chapitre : elle vit dans l'annexe du site consacrée au PIB
(`precis/fr/annexe-pib.qmd`), à laquelle renvoie toute rupture de série qui tient à un
changement de base. La part des dépenses de l'État, qui ne dépend d'aucune base, se donne à
côté de la part du PIB dès que les deux existent.

**Les études citées sont récupérées, systématiquement.** Toute étude, tout rapport cité dans un
volume a sa copie locale — le PDF lui-même, non une page qui le résume — rangée dans l'entrepôt
`tunisia-data` (`data/raw/<source>/`, hors git, avec son adresse d'origine, sa date de collecte
et son empreinte dans le catalogue `sources/`). On ne cite pas de seconde main ce qu'on peut
obtenir : quand un rapport en rapporte un autre, on va chercher l'autre. Un document
introuvable est dit tel dans `docs/notes/biblio-a-rapatrier.md`, avec les adresses essayées.

**Une page se cite par son numéro, sans dire « du PDF ».** « p. » pour une page, « pp. » dès
qu'il y en a plusieurs ou une plage (« p. 34 », « pp. 34-36 », « pp. 120 et 136-137 »), dans les
locators `[@clé, pp. 34-36]` comme dans le texte. On écrit « p. 34 », ou l'on nomme
la section du rapport (« chapitre 3, tableau 12 ») quand elle situe mieux le passage ; jamais
« p. 34 du PDF », « du fichier PDF » ni « PDF p. 34 ». Dans un tableau de sources, la colonne
s'appelle « Page » ; quand les données d'une figure gardent aussi le rang de la page dans le
fichier, à côté de la page imprimée, sa colonne s'appelle « Page du fichier ». Que le numéro
cité soit celui du fichier plutôt que celui imprimé se note, s'il le faut, dans un
`<!-- TODO (documentaliste) : … -->`, pas dans le texte rendu.

**Une série importante déjà portée par `openfisca-tunisia` ne disparaît pas faute de références.**
Elle peut être publiée provisoirement pour rendre son évolution repérable, à trois conditions :
la série entière est montrée plutôt qu'une valeur isolée ; la prose ne nomme pas le modèle et ne
présente pas les états non sourcés comme du droit établi ; un commentaire invisible adjacent
renvoie à une issue `openfisca-tunisia` qui énumère les valeurs et dates à fiabiliser. Le même
signalement est inscrit dans `docs/notes/backlog-modele.md`. Une fois les sources retrouvées, elles
sont versées au paramètre et le tableau est régénéré.

**Des formules en symboles, des valeurs en égalités.** Une formule `$$ … $$` ne porte que des
symboles, ni valeur ni mot (pas de `\text{}` : seule la prose se traduit), et écrit `\%`, jamais
`%` nu. Les valeurs vont à part, en égalités datées et indicatives (« $\bar\tau = 90\,\%$ depuis
1985 »), en légende ou sur une ligne qui suit, avec les mêmes citations et le renvoi au tableau
daté. Notation unique par chapitre (un symbole, une grandeur) : chaque symbole est défini à sa
première formule, ou juste après sa mention, jamais avant ; la liste complète va en annexe de
chapitre, non à la première formule.

## 4. Le découpage des livres

Décidé le 17 octobre 2026. Le détail, les phases et l'arborescence cible à trois niveaux vivent
dans `docs/notes/chantier-decoupage-livres.md` ; cette section en donne les règles, que chaque
rôle applique.

**Six parties.** Les livres se rangent par ce que le texte documente, non par l'ordre où ils ont
été écrits.

| Partie | Livres | Principe |
|---|---|---|
| I. Les revenus primaires | Le marché du travail ; les rémunérations publiques ; l'informel | flux |
| II. Les prélèvements | La fiscalité ; les finances locales ; les cotisations sociales | flux |
| III. Les transferts sociaux : prestations en espèces et prestations en nature | Les retraites ; les prestations sociales | flux |
| IV. Les politiques sectorielles | La santé ; la compensation ; l'éducation ; plus tard le transport, le logement, l'environnement | secteur |
| V. Les institutions | Les caisses de sécurité sociale ; les entreprises publiques | institution |
| VI. La synthèse | Le cadre des finances publiques ; la redistribution | ensemble |

**La règle de domicile entre livres.** Un dispositif vit dans un seul livre ; l'autre en reçoit
une phrase et un lien en tête de section, ou, quand la lecture ne peut pas avancer sans, une figure
ou un tableau court tiré des mêmes données, jamais la prose recopiée.

- Ce qui est prélevé (taux, assiette, ventilation entre branches), l'organisme qui le gère et ses
  comptes : le livre du financement et des caisses de la sécurité sociale.
- Ce qui est servi en espèces (pension, allocation, indemnité) : les retraites ou les prestations
  sociales.
- Ce qui est servi en nature (les soins) : la santé.
- Un prix ou un tarif administré : la compensation.
- Une règle de salaire : les revenus du travail (marché du travail, rémunérations publiques).
- Le statut et les comptes d'une entreprise publique : les entreprises publiques.

**Les livres sectoriels.** Un dispositif vit dans le livre sectoriel quand il n'existe que pour ce
secteur (bourses, cantines, tarif du transport public) ; il vit dans le livre de flux quand il est
un cas d'un instrument général (déduction fiscale pour frais de scolarité : fiscalité ; salaire des
enseignants : rémunérations publiques). Leur épine est budgétaire plus que législative :
institution, dépense sur la longue période, dispositifs à flux monétaire, études. La
réglementation sans effet budgétaire ni distributif n'y entre pas.

**La loi là où elle fixe un revenu ou un droit.** Là où elle ne fait que prélever, le livre de
l'instrument suffit, et la synthèse montre la composition des revenus.

**La population couverte.** L'état du droit de chaque dispositif a une colonne « population
couverte », avec son complément et sa série. L'informel n'est pas un livre : c'est cette colonne,
un chapitre de formalisation dans le marché du travail, un chapitre de couverture dans la
synthèse.

**Les types de chapitres**, reconnaissables à leur titre : dispositif (plan type à épine
chronologique) ; institution (naissance, statut, ce qu'elle sert, comptes, longue période) ;
cadre (notions, un seul par livre, en tête) ; longue période du livre (budgétaire seul) ; rapports
et études (chacun avec sa méthode). Les notations, listes, textes modificatifs et tableaux annexés
sont des annexes, déclarées comme telles dans `_quarto.yml`.

**Le critère de scission.** Un chapitre suit une seule épine chronologique — trois à six grandes
réformes d'un même dispositif — et ses fiches. Au-delà d'environ 25 000 mots de fichier, ou quand
un fichier porte plusieurs épines, il se scinde, avant toute conversion au format « ruptures au
premier plan ».

**La présentation d'un livre** comporte : l'objet en une phrase ; la carte des dispositifs ou
institutions (texte fondateur, date d'application, où lire) ; une figure de ce que pèse
l'ensemble ; le plan ; les conventions de lecture ; un tableau de voisinage (sujet limitrophe,
livre où il vit), qui remplace les sections « ce que ce livre ne traite pas ».

**Rien ne naît ex nihilo.** Trois niveaux.
- *Le chapitre* : la mise en place commence par l'antécédent — le régime, l'impôt ou le prix que le
  texte fondateur remplace, transforme ou étend, Protectorat compris — et dit ce que le texte
  reprend et ce qu'il écarte. Chaque grande réforme donne son contexte (déficit, plan de
  développement, ajustement, accord international, événement politique, modèle étranger) avec les
  mots des sources de l'époque, jamais en interprétation. « Ce que la loi cherche » (ses mots) et
  « le contexte » (ce qu'en disent les sources) restent distincts.
- *Le livre* : la présentation porte une frise des dates clés de tous ses dispositifs sur un seul
  axe, avec la filiation des régimes et des institutions.
- *Le site* : le cadre des finances publiques ouvre sur une périodisation commune (Protectorat ;
  indépendance et État bâtisseur ; expérience collectiviste et son abandon ; années 1970 ;
  ajustement structurel de 1986 ; années 1990-2000 ; 2011 et après), que toute épine se lit contre.

**« Ce qu'en dit l'économie ».** Dernière section d'un chapitre de dispositif, après la longue
période, une page au plus : un état des connaissances sur le *type* de dispositif, pour le
praticien. Gabarit fixe : la question ; ce que dit la théorie (deux ou trois résultats, avec leurs
hypothèses) ; ce que mesure l'empirique (synthèses internationales avec plages, puis Tunisie) ; ce
que le praticien retient (établi, débattu, ce que les données tunisiennes ne tranchent pas).
Dernière ligne : « Littérature arrêtée au <mois année> ». Garde-fous : aucun « on sait que » sans
référence ; aucun chiffre sans sa plage, son pays et sa période ; la section ne se mêle ni au
budgétaire ni au droit, et aucun de ses chiffres n'entre dans un tableau de paramètres ou une
figure de série ; aucune recommandation, même implicite. Elle est tirée d'une fiche datée
`docs/notes/eco-<dispositif>.md` du rôle « économiste » ; les PDF cités vont dans `tunisia-data`.
