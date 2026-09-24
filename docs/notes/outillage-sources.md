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

### Six pièges, tous mesurés

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

**e) Quelques `jort_numero` erronés** (vérifié le 24 septembre 2026). Le n° **107 de 2026** est le
n° 7 (même date, 16 janvier 2026) ; le n° **203 de 2025** est le n° 102 (12 août 2025). Un tel
numéro se trahit par sa date, qui le fait sortir de la plus longue suite de numéros aux dates
croissantes : c'est la règle de `recherches.dernier_numero_coherent`, qui l'écarte quand il faut
connaître le dernier numéro d'une année. Une relance qui dit « absent du corpus » un de ces numéros ne signale pas un trou.

**f) Des fascicules inconnus de la base** (sondé le 24 septembre 2026) : aucun texte de
`jort_cache` ne renvoie à 9 fascicules de 2024 (n° 10, 24, 59, 65, 102, 106, 107, 123, 145), 25 de
2025 (dont les n° 5, 6, 16, 19, 33 à 36, 47 — arabe seul —, 142 et 143) et 8 de 2026 (n° 4, 8, 20,
32, 38, 66, 69, 85), qui existent tous sur pist.tn et sont tous dans le corpus local. Leurs textes
échappent donc aux requêtes sur les titres ; seul le plein texte les parcourt.
`recherches.py relancer <id> --sonder-pist` les repère : pour chaque année parcourue, il teste
sur pist.tn (requête HEAD, sans télécharger) les numéros absents de la base entre 1 et le
dernier numéro cohérent, plus cinq, et les liste comme « existants sur pist.tn, inconnus de
jort_cache ».

### Mettre la base à jour

```
uv run python scripts/corpus_jort.py crawl --from 2026 --to 2026 --a-blanc   # le plan
uv run python scripts/corpus_jort.py crawl --from 2026 --to 2026 [--delai-max 3600]
```

Le dépôt `PDFs-legislation-tunisie` appartient à un autre utilisateur ; son répertoire n'est
pas inscriptible, seuls `jort_cache.db` et `PDFs/JORT/` sont à nous. La commande en tient
compte : sauvegarde datée dans `~/sauvegardes/jort_cache.db.<date>T<heure>` ; crawl, par
`jort_api.crawl` du dépôt (`uv run --no-sync --project …`, qui ne touche ni à son `.venv` ni
à son `uv.lock`), d'une **copie** de la base ; `pragma integrity_check` et contrôle que le
nombre de textes ne baisse pas ; puis recopie du **contenu** de la copie par-dessus
`jort_cache.db` — pas de renommage, faute de droit d'écriture sur le répertoire. Le crawler
**boucle sans fin** sur une erreur réseau (il la réessaie sans limite), dont celle du
certificat échu : la commande l'encadre d'un délai maximal et tue alors tout son groupe de
processus, sans toucher à la base. **Relancer ensuite le serveur MCP `jort`** (`/mcp`), qui
garde l'ancienne base ouverte.

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

### État au 9 septembre 2026 : le certificat est échu depuis le 25 août

Ce n'est pas un défaut de chaîne de confiance mais une **expiration** : `curl` répond
« certificate has expired ». Le certificat, émis par TunTrust Services CA pour
`www.pist.tn`, couvrait du 25 août 2025 au **25 août 2026**.

Trois conséquences, dans l'ordre de gravité :

1. **Pour le lecteur du précis**, chaque lien vers le *Journal officiel* — plus de deux
   cent soixante — déclenche un avertissement de sécurité du navigateur. Rien dans le
   dépôt ne peut le corriger : cela dépend du renouvellement côté pist.tn.
2. **`http://` n'est pas une échappatoire** : le site redirige en 301 vers `https://`.
3. **Pour l'outillage**, toute vérification qui valide la chaîne TLS déclare mortes la
   quasi-totalité des URL. `check_url` de `sync_biblio.py` et `verifier_urls_jort.py`
   emploient donc un contexte permissif : ils vérifient que la ressource EXISTE, sans se
   prononcer sur la confiance. En ligne de commande, `curl -k`.

### Compléter le corpus des fascicules

```
uv run python scripts/corpus_jort.py telecharger 2025 2026 --a-blanc   # ce qui manque
uv run python scripts/corpus_jort.py telecharger 2025 2026
```

La commande télécharge de pist.tn les fascicules FR et AR que `jort_cache` connaît et que
`PDFs/JORT/<année>/<fr|ar>/` n'a pas. Elle n'écrit que ce qui commence par `%PDF`, jamais
par-dessus un fichier existant (fichier `.part`, puis lien qui échoue si la cible existe),
à raison d'une requête toutes les 0,5 s, et finit par un bilan. À blanc, elle signale aussi
les numéros erronés de la base (§ 1 e), auxquels pist.tn répondra 404.

**Le certificat échu ne se contourne qu'ici, et que pour pist.tn.** L'humain a autorisé
explicitement, le 24 septembre 2026, la désactivation de la vérification TLS pour
`www.pist.tn` seulement — des documents publics, en lecture. `scripts/pist_tls.py` est le
seul endroit où elle tombe : connexion à l'hôte écrit en dur, sans suivre de redirection, et,
pour le crawler qui emploie `requests`, désactivation requête par requête d'après l'URL
envoyée. Remettre `VERIFIER = True` quand le certificat sera renouvelé.

**Pourquoi le corpus avait des trous** (constaté le 24 septembre 2026). `download_jort.py`, le
téléchargeur du dépôt, teste les numéros de 1 à **120 au plus** (`MAX_NUM`) — or 2024 et 2025
comptent chacune plus de 140 numéros — et **abandonne l'année après trois numéros absents
consécutifs** (`MAX_CONSECUTIVE_MISSING`, au-delà du n° 10). Et il valide le certificat : depuis
le 25 août 2026, chaque requête échoue et compte pour un numéro absent : l'année s'arrête trois
numéros après le dernier fascicule déjà présent. Ni l'une ni l'autre limite ne concerne `corpus_jort.py telecharger`, qui part des
numéros que la base connaît ; les numéros qu'elle ignore (§ 1 f) se repèrent par
`relancer --sonder-pist`.

**Faux fascicules français.** pist.tn sert parfois le fichier arabe à l'adresse française
(ci-dessus). Au 24 septembre 2026, douze fichiers « fr » du corpus sont en fait l'arabe, octet
pour octet : 2024 n° 8, 130, 145 ; 2025 n° 4, 88, 90, 95, 96, 148 ; 2026 n° 10, 62, 76. Le plein
texte de `recherches.py relancer` les reconnaît (empreinte identique au PDF arabe du même
numéro, ou texte extrait majoritairement arabe) et les compte « FR absent (fichier arabe) » :
ils ne valent pas lecture de l'édition française.

### L'édition ARABE de l'an 2000 ne suit pas la règle de nommage

`sync_biblio.url_jort` dérive l'adresse arabe de l'adresse française en changeant `F/Jo` en
`A/Ja`. La dérivation est bonne **sauf pour l'année 2000**, où l'édition arabe est servie sous
`Ja<numéro><aa>` — deux chiffres d'année — alors que le français est en `Jo<numéro><aaaa>` :

| | français | arabe |
|---|---|---|
| JORT n° 39 de **2000** | `Jo0392000.pdf` ✅ | `Ja0392000.pdf` ❌ → `Ja03900.pdf` ✅ |
| JORT n° 1 de **2001** | `Jo0012001.pdf` ✅ | `Ja0012001.pdf` ✅ |

Mesuré le 20 septembre 2026 sur quatre adresses ; 2001 suit déjà la règle générale, 2000 est donc
l'année de bascule côté arabe. Rencontré deux fois dans la même séance, sur le JORT n° 14 et le
n° 39 de 2000. **Une entrée arabe dont l'URL est en `Ja<numéro>2000.pdf` est fausse** : corriger
à la main, la dérivation ne le fait pas.

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
**couche texte à police décalée**. Un `grep` y est structurellement incapable d'aboutir et un
résultat nul n'y a **aucune valeur probante**.

**Ce décalage se décode, et l'océrisation n'est alors pas nécessaire.** Vérifié le 20 septembre
2026 sur le JORT n° 97 de 2002 et le n° 8 de 2004 : l'encodage est décalé d'une constante de 29,
lettres ET chiffres. Le fascicule paraît illisible — `pdftotext` rend
`75$'8&7,21)5$1d$,6(` — et se relit intégralement en ajoutant 29 à chaque code :
« TRADUCTION FRANÇAISE ».

**Les accents ne sortent pas toujours corrects.** Sur le JORT n° 22 de 2002 (21 septembre 2026),
ils sont codés hors de la plage décalée, sur des lettres minuscules qu'il faut rétablir par une
table ; le « ° » est codé `\x83`. Les espaces et sauts de ligne réels ne sont pas décalés et
doivent être laissés tels quels, faute de quoi le texte se colle. La table ci-dessous est établie
sur ce seul fascicule ; sur un autre, relire quelques accents à l'image
avant de faire confiance à la table.

```python
AUTRES = {"p": "é", "j": "à", "k": "â", "q": "è", "r": "ê", "d": "ç", "l": "î",
          "x": "ô", "u": "ù", "\x83": "°"}

def decode(s):  # sur la sortie de `pdftotext fascicule.pdf -`
    sortie = []
    for c in s:
        o = ord(c)
        if c in " \n":
            sortie.append(c)                      # espaces réels : non décalés
        elif o < 0x62 and 0x20 <= o + 0x1D < 0x7F:
            sortie.append(chr(o + 0x1D))          # seuls les codes < 0x62 sont décalés
        else:
            sortie.append(AUTRES.get(c, c))       # accents et « ° »
    return "".join(sortie)
```

**Conséquence de méthode** : avant de déclarer un fascicule « sans couche texte » et de lancer une
océrisation, tester le décalage. Deux des cinq décrets modifiant le décret n° 95-1166 auraient été
déclarés illisibles à tort, dont celui qui récrit son article 30. Un test de lisibilité fondé sur
la seule longueur du texte extrait classe ces fascicules parmi les scans, à tort — le test doit
décoder avant de mesurer. Si le décalage ne donne rien, alors seulement lire à l'image.

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
