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

### Ce qui en découle, cas par cas

**Un fait vrai du seul modèle ne se publie pas.** Une date qu'un paramètre porte à tort,
une valeur que le modèle calcule d'une certaine façon, un croisement qu'il opère : rien de
tout cela n'est un fait de droit. Ou bien l'assertion est établie sur le texte et se publie
comme telle, ou bien elle ne se publie pas.

**Ce que les textes n'établissent pas se dit sans nommer le modèle.** « Le partage des
1,20 % entre maladie, maternité et décès n'est fixé par aucun texte identifié » est une
phrase du précis. « Le modèle porte 0,24 % de maternité, sans source » n'en est pas une :
elle parle du modèle. La première dit au lecteur ce qu'il doit savoir — le tableau qu'il
lit comporte une part non attestée ; la seconde lui parle d'un outil dont il n'a que faire.

**Une incertitude sur un chiffre publié se signale par un `callout`**, en disant ce qui est
attesté et ce qui ne l'est pas, avec le niveau d'attestation. Jamais en désignant sa source
technique.

## 2. Où va ce qu'on ne publie pas

Trois destinations, selon la nature de la remarque. C'est la seule voie : rien ne reste
dans le texte rendu.

| Nature | Destination |
|---|---|
| Manque éditorial — un texte à lire, une section à écrire | `<!-- TODO (rôle) : … -->` dans le `.qmd`, à l'endroit concerné |
| Défaut du modèle — valeur, date, assiette, formule | *Issue* sur `openfisca/openfisca-tunisia`, plus une ligne dans `docs/notes/backlog-modele.md` |
| Référence à verser ou à corriger dans Zotero | `docs/notes/biblio-a-rapatrier.md` |

Le commentaire `<!-- TODO (rôle) : … -->` est la forme déjà employée dans tout le corpus :
le rôle entre parenthèses est celui qui doit reprendre le travail — `documentaliste`,
`bibliographe`, `terminologue`, `rédacteur`. Il est invisible au rendu et survit aux
passes de traduction.

`docs/notes/backlog-modele.md` tient la liste de ce que la rédaction a constaté sur le
modèle, chaque ligne renvoyant à son *issue*. Il existe pour que le constat ne se perde pas
entre le moment où on le fait et celui où quelqu'un le corrige — et pour qu'on ne le refasse
pas deux fois.

## 3. Ton et chiffres

Rappel des deux règles déjà en vigueur, parce qu'elles se combinent avec la première.

**Ton documentaire, jamais polémique.** On documente, on ne dénonce pas. Un défaut du droit
se constate ; il ne s'indigne pas.

**Jamais un chiffre ponctuel sans sa vue d'évolution** — un graphique ou un tableau daté.
Un taux en vigueur sans son histoire ne dit pas ce qu'il vaut.
