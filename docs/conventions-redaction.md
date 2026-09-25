# Conventions de rédaction du précis

## 1. Le précis documente la loi, jamais le modèle

C'est la règle qui commande toutes les autres, et elle est absolue dans le texte rendu.

`openfisca-tunisia` **ne se mentionne pas** dans le précis : ni son nom, ni « le modèle »,
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
passe atteint la borne, et `relancer` ne cherche pas au-delà. Quand le texte est
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
