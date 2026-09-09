# Outillage et sources — ce qui marche, et les pièges vérifiés

> **Toutes les affirmations de cette note ont été vérifiées par exécution le 8 septembre 2026.**
> Trois constats qui circulaient dans les notes précédentes se sont révélés faux et sont
> corrigés ici. Revérifier avant de s'y fier : la moitié de ces faits porte sur un
> environnement local qui peut changer.

## 1. `jort_cache.db` — la source de métadonnées la plus utile, longtemps ignorée

`/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db`, **78 953 textes**, interrogeable
en SQL sans risque d'écriture :

```
sqlite3 'file:/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db?immutable=1' "..."
```

Table `textes` : `recid, type, numero, titre, objet, ministere, date_signature, date_publication,
jort_annee, jort_numero, jort_tome, pages, pdf_fr, pdf_ar`. Plus `keywords` (index matière),
`textes_fts` (FTS5) et `textes_dedup`.

C'est elle qui donne, pour chaque texte, **le fascicule et la page** — donc le ciblage exact
d'une océrisation.

### Quatre pièges, tous mesurés

**a) 42 % des textes ont un `numero` NULL.** 33 014 sur 78 953, dont **31 259 arrêtés**. Toute
concaténation `||` non protégée par `coalesce()` les fait disparaître silencieusement. Or ce sont
les arrêtés qui portent une part substantielle du droit des prestations sociales — financement du
PNAFN, aides aux personnes âgées, montants des subventions.

**b) Le champ `type` a deux orthographes.** `Arrete` (28 264) **et** `Arrêté` (2 995). Une requête
`where type = 'Arrete'` manque 10 % des arrêtés. Utiliser `type like 'Arr%'` ou `type_norm`.

**c) Accents : la règle diffère entre FTS et LIKE.**
- `textes_fts` est **insensible aux accents** (`remove_diacritics 2`) : `match 'sécurité'` et
  `match 'securite'` renvoient tous deux 786 résultats.
- `LIKE` ne l'est **pas**, et les titres sont majoritairement **non accentués dans le corps**
  tout en portant des accents sur les noms de mois :
  `titre like '%sécurité sociale%'` → **9** résultats, `like '%securite sociale%'` → **228**.

  → Pour un `LIKE`, chercher **sans accents**. Pour le FTS, peu importe.

  **Cas réel, qui a coûté cher.** La recherche du texte fondateur du programme national d'aide
  aux familles nécessiteuses a d'abord conclu qu'il n'existait aucune mention du programme au
  JORT. Le compte exact :

  | Requête | Résultats |
  |---|---:|
  | `titre like '%familles nécessiteuses%'` | **0** |
  | `titre like '%familles necessiteuses%'` | **4** |
  | `textes_fts match 'necessiteuses'` | **6** |

  Le faux négatif a été propagé dans une note de plan puis dans le brief d'un agent, avant
  d'être rattrapé. **Toujours doubler un `LIKE` par une requête FTS** avant de conclure à une
  absence.

**d) Quelques `jort_annee` aberrantes** : 150, 199, 201, 975, 1070, 1075, 1775, 1870. Filtrer par
`jort_annee between 1956 and 2026`.

## 2. Le miroir iort.tn — ce qu'il contient vraiment

`PDFs-legislation-tunisie/data/iort/textes/md/`, **32 118 fichiers**.

**Correction d'un constat faux.** Une note antérieure affirmait que les fichiers antérieurs à
2000 « ne contiennent que l'habillage du site ». Ils portent en réalité **l'intitulé arabe
intégral**. Ce qui manque avant 2000, c'est le **corps** du texte et la version française.

**Correction d'un second constat faux.** Le titre est à la **ligne 40**, non 39 — l'écart vient
d'un décompte à partir de zéro. Vérifié sur `loi_60_30_1960.md` et `loi_58_130_1958.md`.
Extraction robuste : la première ligne non vide **après le marqueur `دليل`**.

**Préfixes de nommage**, plus nombreux que la convention simple ne le laisse deviner —
c'est ce qui avait fait conclure à tort à l'absence de la loi organique sur l'AMEN social :

| Préfixe | Nombre | | Préfixe | Nombre |
|---|---:|---|---|---:|
| `dec` | 23 623 | | `loi_org` | 260 |
| `loi` | 4 532 | | `arr` | 232 |
| `dec_gouv` | 2 423 | | `avis`, `dec_pres`, `decision`, `loi_const`, `amr`, `loi_orient` | < 250 |
| `dec_loi` | 481 | | | |

Année sur **deux chiffres avant 2000**, quatre ensuite : `loi_89_114_1989.md`,
`loi_2013_54_2013.md`.

## 3. pist.tn — le certificat n'est jamais le problème

Le certificat TLS est **expiré** : un client strict échoue (`curl` sans `-k` renvoie le code 000).
Passer `-k` suffit, et les fascicules répondent normalement.

**Un code 200 ne prouve rien, et le champ `pdf_fr` de la base non plus.** Vérifier le
**type de contenu et la taille** :

```
curl -sk -o /dev/null -w "%{http_code} %{content_type} %{size_download}\n" -L --max-time 120 "<url>"
```

| Cas | Signature |
|---|---|
| Fascicule réel | `200 application/pdf 2277815` |
| Absent | `404 text/html; charset=iso-8859-1 289` |

**Le contrôle par taille ne suffit pas.** `2025F/Jo1482025.pdf` et `2025F/Jo0882025.pdf`
répondent 200 avec plusieurs mégaoctets en `application/pdf` — et **servent le fascicule
arabe**. Une URL en « F » n'est donc une garantie ni par son code, ni par son type, ni par son
poids : il faut **ouvrir le fichier et lire son contenu** avant de citer une pagination
française.

Le 404 fait **exactement 289 octets de HTML**. Et une URL en « F » peut servir un fascicule
**arabe** : c'est arrivé pour le JORT n° 148 de 2025. Le champ `pdf_fr` existe pour le fascicule
n° 141 de 2022 alors que le fichier répond 404.

**Éditions françaises confirmées absentes** : JORT n° 104/2015, n° 104/2019, n° 141/2022,
n° 144/2023, n° 149/2024. Pour celles-ci, l'URL arabe, et la pagination française relevée sur le
corpus local.

**Convention d'URL** : `/jort/<année>/<année>{F|A}/{Jo|Ja}<n° sur 3 chiffres><année sur 2 chiffres
jusqu'en 1999, 4 ensuite>.pdf`.

## 3 bis. Les dates de `jort_cache` ne font pas foi contre le fascicule

Sur 29 textes contrôlés lors du dossier « assistance sociale », **8 dates de publication de la
base divergent du pied de page du fascicule**. Le pied de page fait foi. Vérifier dès qu'une
date de publication est citée dans le précis.

## 4. Deux paginations coexistent

Un même article porte deux numéros de page selon l'édition. Pour l'article 36 de la loi de
finances 2025 : **p. 3429-3430 en français**, **p. 6429 en arabe**. Les deux sont exactes ; la
notice `jort_cache` donne la pagination **arabe**. Toute citation doit préciser l'édition — une
session entière a propagé une « correction » qui n'en était pas.

## 5. Océrisation — disponible et efficace

`ocrmypdf`, `tesseract` avec le pack **`fra`**, `pdftoppm` sont installés. « Sans couche texte »
n'est donc jamais une impasse :

```
ocrmypdf -l fra --skip-text --jobs 4 in.pdf out.pdf && pdftotext out.pdf out.txt
```

**Mais l'OCR abîme les chiffres et détruit les tableaux.** Toute valeur chiffrée doit être relue
à l'image : l'outil `Read` accepte un paramètre `pages` sur les PDF et les rend visuellement
(20 pages maximum par appel). C'est ainsi qu'ont été établis les barèmes de 1962, 1965, 1980,
1983, 1986 et 1990.

Cas particulier rencontré : certains fascicules (années 2000-2006, JORT n° 105/2004) ont une
**couche texte à police décalée qui n'expose pas les chiffres**. Un `grep` y est structurellement
incapable d'aboutir et un résultat nul n'y a **aucune valeur probante**. Lire à l'image.

## 6. Chaîne de rendu

**`build.sh`** produit les PDF **par défaut** ; l'option est `--no-pdf`, il n'existe pas de
`--pdf`. Une option inconnue sort en code 2 avec l'aide sur stderr.
**Piège** : appelé en pipeline (`./build.sh | tail`), le code de retour est celui de la dernière
commande et masque l'échec. Utiliser `set -o pipefail` ou tester `${PIPESTATUS[0]}`.

**TinyTeX** est en TeX Live 2025 alors que le dépôt CTAN sert 2026 ; `tlmgr` refuse toute
installation inter-versions. Le dépôt est donc **épinglé sur le tlnet figé de 2025** :
`https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2025/tlnet-final`. `koma-script` est
installé, les huit livres compilent en PDF. Conséquence : plus de mise à jour de paquets tant que
TinyTeX n'est pas migré vers 2026.

**`downloads: [pdf]`** est posé dans les **huit** `_quarto.yml`. Sans cette clé, Quarto produit le
PDF mais aucun lien n'y mène.

**La pipeline de traduction ne synchronise pas les `_quarto.yml`.** Trois réglages ont dû être
appliqués à la main côté arabe : le chapitre `_glossaire.qmd`, `number-depth`/`toc-depth`, et
`downloads`. Toute clé de configuration ajoutée en français doit l'être en arabe.

## 7. Glossaire et bibliographie

`scripts/build_glossary.py` — `BOOKS = ["remunerations_publiques", "fiscalite"]`. Le livre
**prestations sociales n'y est pas** : l'y ajouter avant de poser des ancres `#g-…`. L'annexe de
chaque livre est restreinte aux notions que son texte utilise ;
`translation_glossary.generated.md` reste global.

`scripts/sync_biblio.py` est en **lecture seule** : Zotero → `references.json`, **aucun endpoint
d'écriture** (vérifié : zéro `POST`/`PUT`). Il exige `ZOTERO_API_KEY`, absente de l'environnement.
Conséquence : les clés ajoutées à la main dans `references.json` **seront écrasées** au prochain
sync tant qu'elles ne sont pas montées dans Zotero. Inbox : `docs/notes/biblio-a-rapatrier.md`.

## 8. openfisca-tunisia

`master` est en **0.76** (9 septembre 2026). `scripts/openfisca_tables.py` porte
`VERSION_MINIMALE = (0, 76)` : en deçà, les tableaux du précis sont lus depuis les snapshots
versionnés et non depuis le paquet. Ce garde-fou existe parce que la 0.67 publiée sur PyPI
contient un barème 1990-2016 amputé.

### Le piège des snapshots : ils survivent à la correction du paramètre

Le build ne lance **jamais** les générateurs : il lit `precis/{fr,ar}/*/tables/*.md`, versionnés.
C'est délibéré — le site se construit sans openfisca-tunisia, et le tableau publié est celui qu'on
a relu. Le revers est qu'un snapshot **survit à la correction du paramètre qu'il reflète**, sans
que rien ne le signale.

Cas réel, et il ne sera pas le dernier : la PR openfisca #386 a établi que le minimum d'impôt au
titre des avantages fiscaux passe à 60 % à partir des **revenus de 1999**, et non de 2014. Le
paramètre a été corrigé ; le tableau publié est resté sur « 2014 → 2016 » pendant plusieurs jours,
et n'a été rattrapé que parce qu'une autre tâche a fait régénérer les snapshots par hasard.

**Régénérer après toute PR de paramètres**, sans exception :

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_bareme_tables.py
    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_prestations_tables.py

Le workflow `verifier-snapshots.yml` monte la garde : il régénère depuis `openfisca-tunisia`
master et échoue si le résultat diffère du contenu versionné — sur les PR qui touchent aux
tableaux ou aux générateurs, et **chaque lundi**, parce que le cas le plus fréquent est celui où
le paramètre bouge sans que le précis change.

**Les paramètres ne font jamais autorité.** Sur l'IRPP seul, cette session a établi une douzaine
de valeurs ou de dates fausses, dont trois fois le même motif : **une valeur juste rattachée à la
mauvaise date** — plafond d'assurance-vie de 1998 daté de 1990, plafond d'épargne de 1992 daté de
1990, plafond de frais professionnels de 2017 daté de 1990. Vérifier systématiquement sur le
texte.

## 9. Convention de datation

Les paramètres sont datés en **années de revenus**. Quand un article de loi de finances énonce sa
propre date d'effet, elle vaut ; **quand il est muet et que seul joue l'article final de la loi,
la doctrine administrative rattache la mesure aux revenus de l'année précédente**. Établi sur huit
notes communes couvrant vingt ans. Une lecture naïve « loi de finances pour N ⇒ revenus N »
décale d'un an la moitié des séries.

Marquer chaque valeur **attestée** (par une note commune ou une clause propre) ou **dérivée**
(de cette règle).
