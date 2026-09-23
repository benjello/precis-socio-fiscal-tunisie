"""Pousse vers Zotero les références créées à la main dans les fichiers CSL-JSON.

`sync_biblio.py` ne va que dans un sens : Zotero (source canonique) → `references.json`.
Les références établies au fil de la rédaction — dépouillement du JORT, lectures à l'image —
ont donc été écrites directement dans les fichiers locaux, où elles sont hors de la source
canonique : la prochaine synchronisation descendante les écraserait.

Ce script fait le chemin inverse, une fois, pour les rapatrier.

    # 1. Que permet la clé ? (rien d'autre n'a de sens si elle est en lecture seule)
    python scripts/push_biblio.py --permissions

    # 2. Conversion vérifiée hors ligne, sans clé : aucun champ ne doit se perdre
    python scripts/push_biblio.py --verifier

    # 3. Ce qui serait envoyé, sans rien envoyer
    python scripts/push_biblio.py --dry-run

    # 4. Un seul article d'abord, puis relire ce que sync_biblio.py redescend
    python scripts/push_biblio.py --pousser --limite 1

    # 5. Le reste
    python scripts/push_biblio.py --pousser

Variables d'environnement : ZOTERO_API_KEY, ZOTERO_GROUP_ID (défaut 6529669).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE_URL = "https://api.zotero.org"
DEFAULT_GROUP_ID = "6529669"
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSL -> Zotero, établi sur https://api.zotero.org/schema (version 42) et non de mémoire.
TYPES = {
    "legislation": "statute",
    "report": "report",
    "dataset": "dataset",
    "book": "book",
    "webpage": "webpage",
    "article-newspaper": "newspaperArticle",
    "article-journal": "journalArticle",
}

# Champs communs. Les alias par type (statute.nameOfAct pour `title`, par exemple) sont
# appliqués ensuite par ALIAS : Zotero refuse le champ de base quand le type a le sien.
CHAMPS = {
    "title": "title",
    "container-title": "publicationTitle",
    "page": "pages",
    "volume": "volume",
    "issue": "issue",
    "publisher": "publisher",
    "publisher-place": "place",
    "number-of-pages": "numPages",
    "title-short": "shortTitle",
    "DOI": "DOI",
    "URL": "url",
    # Provenance d'un document tiré des archives du web : `URL` porte la capture,
    # `archive_location` l'adresse d'origine. Le rapport et le livre ont ces champs ;
    # la page web et le texte législatif ne les ont pas, d'où leur place dans
    # VARIABLES_EXTRA ci-dessous.
    "archive": "archive",
    "archive_location": "archiveLocation",
}

ALIAS = {
    "statute": {"title": "nameOfAct", "date": "dateEnacted", "publicationTitle": "code",
                "volume": "codeNumber"},
    "report": {"publisher": "institution"},
    "dataset": {"publisher": "repository", "place": "repositoryLocation"},
    "webpage": {"publicationTitle": "websiteTitle"},
}

# Champs CSL qu'aucun champ Zotero ne peut accueillir pour le type visé. Zotero relit les
# lignes « variable: valeur » du champ Extra comme des variables CSL et les réémet à
# l'export : c'est le seul endroit où ces données survivent. Le numéro de fascicule du
# JORT est dans ce cas pour les textes législatifs — et c'est une donnée de provenance,
# pas un ornement.
# `number-of-pages` s'y ajoute : Zotero le porte nativement (`numPages`) pour le livre,
# mais PAS pour le rapport — et le Manuel de liquidation de la CNRPS, 149 pages, est un
# rapport. Sans cet échappement, une seule entrée faisait échouer la conversion ENTIÈRE,
# et donc le rapatriement des 119 références absentes de Zotero.
# `archive` et `archive_location` suivent le même chemin pour la page web, qui ne les a
# pas : sans cela, la provenance d'une page disparue se perdait en silence à l'envoi.
VARIABLES_EXTRA = ("issue", "authority", "event-date", "collection-title", "genre",
                   "number-of-pages", "archive", "archive_location")


def champs_du_type(type_zotero: str, schema: dict) -> set[str]:
    for t in schema["itemTypes"]:
        if t["itemType"] == type_zotero:
            return {f["field"] for f in t["fields"]}
    return set()


def charge_schema() -> dict:
    cache = os.path.join(RACINE, ".zotero-schema.json")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as f:
            return json.load(f)
    with urllib.request.urlopen(f"{BASE_URL}/schema") as resp:
        schema = json.loads(resp.read().decode())
    with open(cache, "w", encoding="utf-8") as f:
        json.dump(schema, f)
    return schema


def date_csl_vers_zotero(issued: dict) -> str:
    parties = (issued or {}).get("date-parts") or [[]]
    return "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parties[0]))


def date_zotero_vers_csl(texte: str) -> dict | None:
    if not texte:
        return None
    morceaux = [int(x) for x in texte.split("-") if x.isdigit()]
    return {"date-parts": [morceaux]} if morceaux else None


def csl_vers_zotero(entree: dict, schema: dict) -> dict:
    type_csl = entree.get("type", "document")
    type_zotero = TYPES.get(type_csl)
    if not type_zotero:
        raise ValueError(f"{entree.get('id')} : type CSL non pris en charge « {type_csl} »")
    disponibles = champs_du_type(type_zotero, schema)
    alias = ALIAS.get(type_zotero, {})

    item = {"itemType": type_zotero}
    extra_variables = []
    natifs = set()  # variables déjà logées dans un champ propre : pas de doublon en Extra

    for csl_var, champ in CHAMPS.items():
        if csl_var not in entree:
            continue
        cible = alias.get(champ, champ)
        if cible in disponibles:
            item[cible] = str(entree[csl_var])
            natifs.add(csl_var)
        elif csl_var in VARIABLES_EXTRA:
            extra_variables.append(f"{csl_var}: {entree[csl_var]}")
        else:
            raise ValueError(
                f"{entree.get('id')} : le champ « {csl_var} » n'a pas de place dans "
                f"{type_zotero} et n'est pas prévu pour Extra"
            )

    for csl_var in VARIABLES_EXTRA:
        if csl_var in natifs:
            continue
        if csl_var in entree and not any(v.startswith(f"{csl_var}:") for v in extra_variables):
            valeur = entree[csl_var]
            if csl_var.endswith("date") and isinstance(valeur, dict):
                valeur = date_csl_vers_zotero(valeur)
            extra_variables.append(f"{csl_var}: {valeur}")

    if "issued" in entree:
        champ_date = alias.get("date", "date")
        if champ_date in disponibles:
            item[champ_date] = date_csl_vers_zotero(entree["issued"])

    # Date de consultation : `accessDate` existe pour tous les types visés. Elle était
    # perdue à l'envoi (cnss-chiffres), et c'est elle qui date la lecture d'une capture.
    if "accessed" in entree and "accessDate" in disponibles:
        item["accessDate"] = date_csl_vers_zotero(entree["accessed"])

    if "author" in entree:
        item["creators"] = [
            {"creatorType": "author", "name": a["literal"]} if "literal" in a
            else {"creatorType": "author",
                  "firstName": a.get("given", ""), "lastName": a.get("family", "")}
            for a in entree["author"]
        ]

    # `citation-key:` en minuscules : c'est ce que lit extract_citation_key de
    # sync_biblio.py. La convention « Citation Key: » de Better BibTeX est une AUTRE
    # chaîne, et les confondre casse la synchronisation descendante.
    lignes_extra = [f"citation-key: {entree['id']}"] + extra_variables
    note = (entree.get("note") or "").strip()
    if note:
        # La note locale porte déjà « citation-key: … » en première ligne : on ne la
        # duplique pas. Idem des variables que l'on vient d'écrire en Extra : la descente
        # verse l'Extra dans `note`, et sans ce filtre chaque aller-retour ajoutait une
        # ligne `issue:` (ou `archive_location:`) de plus.
        emises = {v.split(":", 1)[0] for v in extra_variables}
        note = "\n".join(
            l for l in note.splitlines()
            if not l.lower().startswith("citation-key:")
            and not (re.match(r"^([A-Za-z_-]+):", l)
                     and re.match(r"^([A-Za-z_-]+):", l).group(1) in emises)
        ).strip()
    if note:
        lignes_extra.append(note)
    item["extra"] = "\n".join(lignes_extra)
    return item


def zotero_vers_csl(item: dict, schema: dict) -> dict:
    """Inverse de `csl_vers_zotero`, pour éprouver la conversion sans rien envoyer."""
    type_zotero = item["itemType"]
    type_csl = next(k for k, v in TYPES.items() if v == type_zotero)
    alias = ALIAS.get(type_zotero, {})
    inverse_alias = {v: k for k, v in alias.items()}
    entree: dict = {"type": type_csl}

    for csl_var, champ in CHAMPS.items():
        cible = alias.get(champ, champ)
        if cible in item and item[cible] != "":
            entree[csl_var] = item[cible]

    champ_date = alias.get("date", "date")
    if item.get(champ_date):
        date = date_zotero_vers_csl(item[champ_date])
        if date:
            entree["issued"] = date
    if item.get("accessDate"):
        # Zotero peut rendre un horodatage complet (« 2026-09-22T00:00:00Z »).
        date = date_zotero_vers_csl(item["accessDate"][:10])
        if date:
            entree["accessed"] = date

    lignes, note = [], []
    for ligne in (item.get("extra") or "").splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.+)$", ligne)
        if m and m.group(1) == "citation-key":
            entree["id"] = m.group(2).strip()
        elif m and m.group(1) in VARIABLES_EXTRA:
            valeur = m.group(2).strip()
            if m.group(1).endswith("date"):
                valeur = date_zotero_vers_csl(valeur)
            entree[m.group(1)] = valeur
        else:
            note.append(ligne)
        lignes.append(ligne)
    if item.get("creators"):
        entree["author"] = [
            {"literal": c["name"]} if "name" in c
            else {"given": c.get("firstName", ""), "family": c.get("lastName", "")}
            for c in item["creators"] if c.get("creatorType") == "author"
        ]
    note_texte = "\n".join(note).strip()
    if note_texte:
        entree["note"] = f"citation-key: {entree.get('id','')}\n{note_texte}"
    _ = inverse_alias
    return entree


def charge_local() -> dict[str, tuple[dict, set[str]]]:
    """{clé de citation: (entrée, livres)} — le français fait foi, dédoublonné.

    L'arabe est un miroir du français depuis la PR #108, et la même référence peut
    figurer à la fois dans un livre et dans la bibliographie partagée : compter les
    fichiers donnerait 173 entrées pour un nombre réel bien moindre.
    """
    entrees: dict[str, tuple[dict, set[str]]] = {}
    fichiers = sorted(glob.glob(os.path.join(RACINE, "precis", "fr", "*", "references.json")))
    fichiers.append(os.path.join(RACINE, "precis", "fr", "references.json"))
    for chemin in fichiers:
        if not os.path.exists(chemin):
            continue
        livre = os.path.basename(os.path.dirname(chemin))
        livre = "" if livre == "fr" else livre
        with open(chemin, encoding="utf-8") as f:
            for entree in json.load(f)["items"]:
                cle = entree.get("id")
                if not cle:
                    continue
                if cle in entrees:
                    # Une même référence peut servir PLUSIEURS livres — lf-2018 est citée
                    # par la fiscalité et par les rémunérations publiques. Un article
                    # Zotero appartient à autant de collections qu'on veut : ne retenir
                    # que le premier livre le ferait disparaître des autres à la descente.
                    if livre:
                        entrees[cle][1].add(livre)
                    continue
                entrees[cle] = (entree, {livre} if livre else set())
    return entrees


def zotero_tout(chemin: str, api_key: str, params: dict) -> list:
    """GET paginé. Sans cela, l'inventaire des clés déjà présentes s'arrête à 100 et
    tout ce qui suit serait recréé en double dans une bibliothèque partagée."""
    resultats: list = []
    debut = 0
    while True:
        query = "&".join(f"{k}={v}" for k, v in {**params, "limit": 100, "start": debut}.items())
        req = urllib.request.Request(f"{BASE_URL}{chemin}?{query}")
        req.add_header("Zotero-API-Key", api_key)
        req.add_header("Zotero-API-Version", "3")
        with urllib.request.urlopen(req) as resp:
            lot = json.loads(resp.read().decode())
            total = int(resp.headers.get("Total-Results", 0))
        resultats.extend(lot if isinstance(lot, list) else [lot])
        debut += 100
        if debut >= total:
            return resultats


def zotero(path: str, api_key: str, methode: str = "GET", corps=None):
    url = f"{BASE_URL}{path}"
    donnees = json.dumps(corps).encode() if corps is not None else None
    req = urllib.request.Request(url, data=donnees, method=methode)
    req.add_header("Zotero-API-Key", api_key)
    req.add_header("Zotero-API-Version", "3")
    if donnees:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            brut = resp.read().decode()
            return json.loads(brut) if brut else {}
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} sur {methode} {url} : {e.read().decode()[:300]}", file=sys.stderr)
        raise


# Nom de la collection Zotero par livre. `sync_biblio.py` fait le chemin inverse avec
# COLLECTION_TO_BOOK ; les deux doivent rester d'accord.
COLLECTIONS = {
    "fiscalite": "Fiscalité",
    "retraites": "Retraites",
    "prestations_sociales": "Prestations sociales",
    "remunerations_publiques": "Rémunérations publiques",
    "cotisations_sociales": "Cotisations sociales",
}


CITATION_CLE = re.compile(r"@([a-zA-Z][a-zA-Z0-9_-]*)")

# Quarto emploie la MÊME syntaxe `@nom` pour deux choses sans rapport : citer une
# référence bibliographique, et renvoyer à un élément numéroté du document — section,
# tableau, figure, équation. Les seconds ne sont pas des clés : ils ne sont ni dans
# `references.json`, ni dans Zotero, et les compter fait croire à des références
# manquantes qui n'existent pas.
#
# Mesuré le 16/09/2026 sur le corpus : 359 `@nom` relevés, dont **24 renvois**
# (11 `sec-`, 10 `tbl-`, 3 `fig-`) pour 335 citations réelles. Le contrôle de rangement
# annonçait donc 38 clés « absentes de Zotero » là où il n'y en avait que 14.
RENVOIS_QUARTO = ("sec-", "tbl-", "fig-", "eq-", "lst-",
                  "thm-", "lem-", "cor-", "prp-", "cnj-",
                  "def-", "exm-", "exr-")


def cles_citees(livre: str, racine: str | None = None) -> set[str]:
    """Clés de citation auxquelles le texte FRANÇAIS d'un livre renvoie réellement.

    TROIS sources, et aucune n'est facultative. Mesuré le 16/09/2026 :

      - la prose (`*.qmd`) ;
      - les tableaux engendrés (`tables/*.md`) — **36 clés distinctes** ne vivent que
        là, dont tous les arrêtés de transferts sociaux ;
      - l'annexe de glossaire (`_glossaire.qmd`), que `build_glossary.render_book`
        remplit de vraies `[@clé]`, résolues contre la bibliographie du livre.

    Le glossaire n'est PAS exclu, contrairement à ce que fait `ancres_utilisees`. Son
    exclusion se justifie là-bas pour les *ancres* — l'annexe se définirait elle-même,
    chaque notion y portant la sienne —, et ce motif ne vaut pas pour les *citations*.

    L'exclure ferait passer cinq clés de « partagée » à « propre à un livre » :
    `decret-2017-668-smig` (trois livres), `lf-2018`, `loi82-70`, `loi83-112`,
    `loi85-78` — le statut général de la fonction publique, le SMIG, des textes
    transversaux. Toutes dans le même sens, et le pire : le contrôle CONSERVERAIT la
    collection qui doit partir, perpétuant en silence la dérive qu'il existe pour
    détecter.

    On lit le français seul : il fait foi, l'arabe en est le miroir.
    """
    base = os.path.join(racine or RACINE, "precis", "fr", livre)
    trouvees: set[str] = set()
    if not os.path.isdir(base):
        return trouvees

    def lire(chemin: str) -> None:
        try:
            with open(chemin, encoding="utf-8") as f:
                trouvees.update(CITATION_CLE.findall(f.read()))
        except OSError:
            pass

    for nom in sorted(os.listdir(base)):
        if nom.endswith(".qmd"):
            lire(os.path.join(base, nom))
    tableaux = os.path.join(base, "tables")
    if os.path.isdir(tableaux):
        for nom in sorted(os.listdir(tableaux)):
            if nom.endswith(".md"):
                lire(os.path.join(tableaux, nom))
    return {cle for cle in trouvees if not cle.startswith(RENVOIS_QUARTO)}


def cles_du_fonds_commun() -> set[str]:
    """Les clés versées au fonds commun (`precis/fr/references.json`), qui fait foi."""
    chemin = Path(__file__).parent.parent / "precis" / "fr" / "references.json"
    return {e["id"] for e in json.loads(chemin.read_text(encoding="utf-8"))["items"]}


def classe_rangement(citations_par_livre: dict, collections_par_cle: dict,
                     communes: set | frozenset = frozenset()) -> dict:
    """Compare l'usage RÉEL d'une référence au rangement que porte Zotero.

    Fonction pure, sur données nues : `{livre: {clés citées}}` d'un côté,
    `{clé: {livres}}` de l'autre — les collections Zotero étant déjà traduites en
    identifiants de livres par l'appelant. Aucune empreinte Zotero ne remonte ici, et
    le contrôle se teste donc sans réseau ni clé d'API.

    La comparaison doit être INDÉPENDANTE. Déduire « quels livres citent cette clé »
    des `references.json` serait circulaire : c'est précisément ce que la descente y
    écrit, et le contrôle ne ferait que se confirmer lui-même. D'où `cles_citees`, qui
    lit la prose.

    Le contrat :

      - citée par **exactement 1 livre** → elle veut la collection de ce livre ;
      - citée par **2 livres ou plus**   → elle ne veut **aucune** collection, afin que
        la descente la verse dans `precis/fr/references.json` ;
      - citée par **aucun** livre         → signalée, jamais agie. Retirer une
        collection sur la foi d'une absence changerait l'état d'une bibliothèque
        partagée à partir d'une preuve qu'on n'a pas su trouver ;
      - citée mais absente de Zotero      → relève du versement, pas du rangement ;
      - **versée au fonds commun** (`communes`, les clés de `precis/fr/references.json`)
        et citée par un seul livre → **jamais rangée** dans la collection de ce livre ;
        une collection qu'elle a déjà lui reste. Décision du 23/09/2026 : les textes
        versés au fonds commun y restent, le classement fin viendra plus tard. Sans
        cette règle, le contrôle les disait « à ranger » et tout `appliquer-rangement`
        les aurait fait descendre dans le fichier d'un livre.

    Ce que cela répare : `ranger` fait `sorted(actuelles | voulues)` — il ajoute des
    collections et n'en retire aucune. Une référence devenue commune garde donc la
    collection du livre où elle est née, et chaque descente la redescend dans ce livre
    au lieu du fonds commun. C'est ce mécanisme qui a fait tomber le fonds commun à
    sept clés.

    Ne décide rien et n'écrit rien : rend un rapport, que l'humain lit.
    """
    cites: dict[str, set[str]] = {}
    for livre, cles in citations_par_livre.items():
        for cle in cles:
            cites.setdefault(cle, set()).add(livre)

    rapport: dict[str, list] = {
        "a_declasser": [], "a_ranger": [], "bien_rangee": [],
        "sans_citation": [], "absente_de_zotero": [],
    }

    for cle in sorted(set(cites) | set(collections_par_cle)):
        if cle not in collections_par_cle:
            rapport["absente_de_zotero"].append(cle)
            continue
        livres = cites.get(cle, set())
        if not livres:
            rapport["sans_citation"].append(cle)
            continue
        actuelles = set(collections_par_cle[cle])
        voulues = set(livres) if len(livres) == 1 else set()
        if cle in communes and len(livres) == 1:
            # Au fonds commun : on ne l'ajoute à aucune collection, on ne retire pas
            # non plus celle qu'elle a déjà.
            voulues &= actuelles
        en_trop = actuelles - voulues
        manquantes = voulues - actuelles
        if not en_trop and not manquantes:
            rapport["bien_rangee"].append(cle)
            continue
        if en_trop:
            rapport["a_declasser"].append((cle, sorted(en_trop)))
        if manquantes:
            rapport["a_ranger"].append((cle, sorted(manquantes)))
    return rapport


def appliquer_rangement(groupe: str, api_key: str, ecrire: bool) -> int:
    """Applique le diagnostic de `controle_rangement` : range ET déclasse.

    `ranger` ne sait qu'AJOUTER, et il déduit le livre d'une référence de l'emplacement
    de son fichier — information vide pour le fonds commun, d'où les 113 qu'il laisse
    en plan. Ici le livre vient de l'usage RÉEL dans la prose, via `cles_citees`, et la
    collection de trop est retirée.

    RÈGLE DE SÛRETÉ, héritée de `controle_rangement` : une collection absente du
    mapping n'est pas une collection de trop. Un article rangé dans une collection
    thématique ou une boîte de réception la conserve — on ne touche qu'aux collections
    de livres, jamais aux autres.

    À blanc par défaut : `ecrire=False` montre et n'envoie rien.
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import sync_biblio

    collections = zotero_tout(f"/groups/{groupe}/collections", api_key, {"format": "json"})
    livre_par_collection, cle_par_livre = {}, {}
    for c in collections:
        nom = c["data"]["name"]
        livre = sync_biblio.COLLECTION_TO_BOOK.get(nom.strip().lower())
        if livre:
            livre_par_collection[c["key"]] = livre
            cle_par_livre.setdefault(livre, c["key"])

    items = zotero_tout(f"/groups/{groupe}/items", api_key, {"format": "json"})
    item_par_cle, collections_par_cle = {}, {}
    for item in items:
        donnees = item.get("data", {})
        m = re.search(r"citation-key:\s*(\S+)", donnees.get("extra", ""), re.I)
        if not m:
            continue
        item_par_cle[m.group(1)] = donnees
        collections_par_cle[m.group(1)] = {
            livre_par_collection[k] for k in (donnees.get("collections") or [])
            if k in livre_par_collection
        }

    citations = {livre: cles_citees(livre) for livre in COLLECTIONS}
    rapport = classe_rangement(citations, collections_par_cle, cles_du_fonds_commun())

    voulu: dict[str, set[str]] = {}
    for cle, manquantes in rapport["a_ranger"]:
        voulu.setdefault(cle, set(collections_par_cle.get(cle, set()))).update(manquantes)
    for cle, en_trop in rapport["a_declasser"]:
        voulu.setdefault(cle, set(collections_par_cle.get(cle, set()))).difference_update(en_trop)

    charges = []
    for cle, livres in sorted(voulu.items()):
        donnees = item_par_cle.get(cle)
        if donnees is None:
            continue
        actuelles = set(donnees.get("collections") or [])
        # Les collections HORS mapping sont preservees telles quelles.
        hors_mapping = {k for k in actuelles if k not in livre_par_collection}
        nouvelles = hors_mapping | {cle_par_livre[l] for l in livres if l in cle_par_livre}
        if nouvelles == actuelles:
            continue
        charges.append({"key": donnees["key"], "version": donnees["version"],
                        "collections": sorted(nouvelles)})
        if not ecrire:
            avant = sorted(livre_par_collection.get(k, "(hors mapping)") for k in actuelles)
            apres = sorted(livre_par_collection.get(k, "(hors mapping)") for k in nouvelles)
            print(f"    {cle} : {avant} -> {apres}")

    print(f"{len(charges)} article(s) a reclasser.")
    if not ecrire:
        print("(a blanc : rien n'a ete envoye ; --appliquer-rangement --pousser pour ecrire)")
        return 0

    modifies = echecs = 0
    for debut in range(0, len(charges), 50):
        lot = charges[debut : debut + 50]
        reponse = zotero(f"/groups/{groupe}/items", api_key, "POST", lot)
        modifies += len(reponse.get("successful") or {})
        for indice, message in (reponse.get("failed") or {}).items():
            echecs += 1
            print(f"  X {lot[int(indice)]['key']} : {message}", file=sys.stderr)
    print(f"{modifies} reclasse(s), {echecs} en echec")
    return 1 if echecs else 0


def controle_rangement(groupe: str, api_key: str) -> int:
    """Rapporte l'écart entre l'usage réel des références et leur rangement Zotero.

    LECTURE SEULE : n'écrit ni dans Zotero, ni dans le dépôt. Le déclassement lui-même
    est une action sortante et irréversible sur une bibliothèque partagée ; il demande
    un feu vert humain, et n'est pas ici.

    C'est ici, et nulle part ailleurs, que les noms de collections Zotero deviennent des
    identifiants de livres. Deux règles y vivent :

      - on passe par `sync_biblio.COLLECTION_TO_BOOK`, qui porte les variantes
        accentuées (« fiscalité » ET « fiscalite ») ; l'inverse de `COLLECTIONS` ne
        connaîtrait que l'orthographe canonique et manquerait une collection
        préexistante accentuée ;
      - une collection absente de ce mapping n'est **pas** une collection de trop. Un
        article rangé dans une collection thématique ou dans une boîte de réception
        n'a rien à se voir reprocher : on l'ignore en silence.
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import sync_biblio

    collections = zotero_tout(f"/groups/{groupe}/collections", api_key, {"format": "json"})
    livre_par_collection = {}
    for c in collections:
        nom = c["data"]["name"]
        livre = sync_biblio.COLLECTION_TO_BOOK.get(nom.strip().lower())
        if livre:
            livre_par_collection[c["key"]] = livre

    items = zotero_tout(f"/groups/{groupe}/items", api_key, {"format": "json"})
    collections_par_cle: dict[str, set[str]] = {}
    for item in items:
        donnees = item.get("data", {})
        m = re.search(r"citation-key:\s*(\S+)", donnees.get("extra", ""), re.I)
        if not m:
            continue
        collections_par_cle[m.group(1)] = {
            livre_par_collection[k] for k in (donnees.get("collections") or [])
            if k in livre_par_collection
        }

    citations = {livre: cles_citees(livre) for livre in COLLECTIONS}
    rapport = classe_rangement(citations, collections_par_cle, cles_du_fonds_commun())

    # Les deux listes de défaut SE CHEVAUCHENT : une clé rangée dans la collection d'un
    # mauvais livre doit à la fois perdre celle-là et gagner la sienne, donc elle figure
    # dans les deux. Additionner les quatre catégories dépasse alors le total annoncé.
    #
    # Première exécution réelle, 16/09/2026 : 175 + 40 + 108 + 12 = 335 pour 333 clés.
    # L'écart n'était pas une erreur de classement — il disait que deux clés étaient
    # rangées dans le mauvais livre. Mais rien ne le disait, et un rapport qui ne
    # s'additionne pas se fait soupçonner tout entier. On compte donc les clés
    # DISTINCTES en défaut, et on nomme le chevauchement.
    en_defaut = ({cle for cle, _ in rapport["a_declasser"]}
                 | {cle for cle, _ in rapport["a_ranger"]})
    doublement = len(rapport["a_declasser"]) + len(rapport["a_ranger"]) - len(en_defaut)

    print(f"{len(collections_par_cle)} référence(s) dans Zotero, "
          f"{sum(len(c) for c in citations.values())} citation(s) relevées dans le texte.\n")
    print(f"✓ bien rangées      : {len(rapport['bien_rangee'])}")
    print(f"⚠ en défaut         : {len(en_defaut)} clé(s) distinctes")
    if doublement:
        print(f"    dont {doublement} rangée(s) dans le mauvais livre : elles figurent "
              f"ci-dessous DEUX fois, une par correction à apporter")
    print(f"⚠ à déclasser       : {len(rapport['a_declasser'])} "
          f"(citées par plusieurs livres, mais rattachées à un livre)")
    for cle, en_trop in rapport["a_declasser"]:
        print(f"    {cle} — retirer : {', '.join(en_trop)}")
    print(f"⚠ à ranger          : {len(rapport['a_ranger'])} "
          f"(citées par un seul livre, sans sa collection)")
    for cle, manquantes in rapport["a_ranger"]:
        print(f"    {cle} — ajouter : {', '.join(manquantes)}")
    print(f"  sans citation     : {len(rapport['sans_citation'])} "
          f"(aucune position prise — une absence n'est pas une preuve)")
    print(f"  absentes de Zotero: {len(rapport['absente_de_zotero'])} "
          f"(relève du versement, pas du rangement)")
    return 0


def ranger(groupe: str, api_key: str, locales: dict) -> int:
    """Classe dans la collection de son livre chaque article déjà créé.

    Un article créé sans collection tombe, à la descente, dans la bibliographie
    PARTAGÉE et non dans celle de son livre : les 153 références poussées d'un coup
    l'ont toutes été ainsi, ce que seul le diff de la descente a montré.
    """
    collections = zotero_tout(f"/groups/{groupe}/collections", api_key, {"format": "json"})
    par_nom = {c["data"]["name"]: c["key"] for c in collections}

    for livre, nom in COLLECTIONS.items():
        if nom in par_nom:
            continue
        if not any(livre in livres for _e, livres in locales.values()):
            continue
        cree = zotero(f"/groups/{groupe}/collections", api_key, "POST", [{"name": nom}])
        par_nom[nom] = list((cree.get("successful") or {}).values())[0]["key"]
        print(f"collection créée : {nom}")

    items = zotero_tout(f"/groups/{groupe}/items", api_key, {"format": "json"})
    par_cle = {}
    for item in items:
        m = re.search(r"citation-key:\s*(\S+)", item.get("data", {}).get("extra", ""), re.I)
        if m:
            par_cle[m.group(1)] = item

    a_ranger = []
    for cle, (_entree, livres) in sorted(locales.items()):
        item = par_cle.get(cle)
        if not item or not livres:
            continue
        voulues = {par_nom[COLLECTIONS[l]] for l in livres
                   if l in COLLECTIONS and COLLECTIONS[l] in par_nom}
        actuelles = set(item["data"].get("collections") or [])
        if not voulues or voulues <= actuelles:
            continue
        donnees = item["data"]
        a_ranger.append({
            "key": donnees["key"],
            "version": donnees["version"],
            "collections": sorted(actuelles | voulues),
        })

    print(f"{len(a_ranger)} article(s) à classer.")
    for debut in range(0, len(a_ranger), 50):
        lot = a_ranger[debut : debut + 50]
        reponse = zotero(f"/groups/{groupe}/items", api_key, "POST", lot)
        echecs = reponse.get("failed") or {}
        print(f"lot {debut // 50 + 1} : {len(reponse.get('successful') or {})} classé(s), "
              f"{len(echecs)} en échec")
        for indice, message in echecs.items():
            print(f"  ✗ {lot[int(indice)]['key']} : {message}", file=sys.stderr)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--permissions", action="store_true", help="que permet la clé ?")
    p.add_argument("--verifier", action="store_true", help="aller-retour CSL, hors ligne")
    p.add_argument("--dry-run", action="store_true", help="montre sans envoyer")
    p.add_argument("--pousser", action="store_true", help="envoie réellement")
    p.add_argument("--limite", type=int, default=0, help="n'envoyer que N entrées")
    p.add_argument("--groupe", default=os.environ.get("ZOTERO_GROUP_ID", DEFAULT_GROUP_ID))
    p.add_argument("--rapport", default="", help="fichier où consigner les clés créées")
    p.add_argument("--comparer", default="", help="relit une référence depuis Zotero et la "
                                                  "compare à l'entrée locale")
    p.add_argument("--corriger", default="", help="écrase dans Zotero une référence par "
                                                  "sa version locale (clés séparées par "
                                                  "des virgules)")
    p.add_argument("--ranger", action="store_true",
                   help="classe les articles déjà créés dans la collection de leur livre")
    p.add_argument("--appliquer-rangement", action="store_true",
                   help="applique le diagnostic du controle : range ET declasse "
                        "(a blanc sans --pousser)")
    p.add_argument("--controle-rangement", action="store_true",
                   help="compare l'usage réel des références au rangement Zotero "
                        "(LECTURE SEULE, n'écrit rien)")
    args = p.parse_args()

    schema = charge_schema()
    locales = charge_local()

    if args.verifier:
        pertes = 0
        for cle, (entree, _livre) in sorted(locales.items()):
            try:
                item = csl_vers_zotero(entree, schema)
            except ValueError as e:
                print(f"✗ {e}")
                pertes += 1
                continue
            retour = zotero_vers_csl(item, schema)
            for champ, valeur in entree.items():
                if champ == "note":
                    continue
                obtenu = retour.get(champ)
                # Comparaison structurelle : `str()` sur un dict compare aussi l'ordre
                # des clés, ce qui signalerait une perte là où il n'y a qu'un
                # {family, given} devenu {given, family}.
                def normalise(v):
                    if isinstance(v, dict):
                        return {k: normalise(x) for k, x in sorted(v.items())}
                    if isinstance(v, list):
                        return [normalise(x) for x in v]
                    return str(v)

                egal = normalise(obtenu) == normalise(valeur)
                if not egal:
                    print(f"✗ {cle} : « {champ} » — envoyé {valeur!r}, relu {obtenu!r}")
                    pertes += 1
        print(f"\n{len(locales)} entrée(s) éprouvées, {pertes} perte(s) de champ.")
        return 1 if pertes else 0

    api_key = os.environ.get("ZOTERO_API_KEY", "")

    if args.permissions:
        if not api_key:
            print("ZOTERO_API_KEY absente.", file=sys.stderr)
            return 1
        infos = zotero("/keys/current", api_key)
        infos.pop("key", None)  # ne jamais réafficher le secret
        print(json.dumps(infos, ensure_ascii=False, indent=2))
        return 0

    if args.corriger:
        items = zotero_tout(f"/groups/{args.groupe}/items", api_key, {"format": "json"})
        par_cle = {}
        for item in items:
            m = re.search(r"citation-key:\s*(\S+)", item.get("data", {}).get("extra", ""), re.I)
            if m:
                par_cle[m.group(1)] = item
        charges = []
        for cle in [c.strip() for c in args.corriger.split(",") if c.strip()]:
            if cle not in locales:
                print(f"✗ {cle} : absente des fichiers locaux", file=sys.stderr)
                return 1
            if cle not in par_cle:
                print(f"✗ {cle} : absente du groupe Zotero", file=sys.stderr)
                return 1
            item = csl_vers_zotero(locales[cle][0], schema)
            item["key"] = par_cle[cle]["data"]["key"]
            item["version"] = par_cle[cle]["data"]["version"]
            item["collections"] = par_cle[cle]["data"].get("collections") or []
            charges.append(item)
        # L'API refuse au-delà de cinquante articles par requête (HTTP 413), et le
        # refus porte sur le lot ENTIER : corriger trois cents références d'un bloc
        # n'en écrit aucune. Même découpage que le versement, plus bas.
        corrigees = inchangees = echecs = 0
        for debut in range(0, len(charges), 50):
            lot = charges[debut : debut + 50]
            reponse = zotero(f"/groups/{args.groupe}/items", api_key, "POST", lot)
            corrigees += len(reponse.get("successful") or {})
            inchangees += len(reponse.get("unchanged") or {})
            for indice, message in (reponse.get("failed") or {}).items():
                echecs += 1
                print(f"  ✗ {lot[int(indice)]['key']} : {message}", file=sys.stderr)
        # « inchangée » n'est pas un échec : Zotero range ainsi un article déjà
        # identique. Le taire ferait lire un déficit là où il n'y a rien à écrire.
        print(f"{corrigees} corrigée(s), {inchangees} inchangée(s), {echecs} en échec")
        return 1 if echecs else 0

    if args.appliquer_rangement:
        return appliquer_rangement(args.groupe, api_key, ecrire=args.pousser)

    if args.controle_rangement:
        return controle_rangement(args.groupe, api_key)

    if args.ranger:
        return ranger(args.groupe, api_key, locales)

    if args.comparer:
        items = zotero_tout(f"/groups/{args.groupe}/items", api_key, {"format": "json"})
        zkey = None
        for item in items:
            m = re.search(r"citation-key:\s*(\S+)", item.get("data", {}).get("extra", ""), re.I)
            if m and m.group(1) == args.comparer:
                zkey = item["key"]
        if not zkey:
            print(f"« {args.comparer} » introuvable dans le groupe.", file=sys.stderr)
            return 1
        redescendu = zotero(
            f"/groups/{args.groupe}/items/{zkey}?format=csljson", api_key
        )
        redescendu = (redescendu.get("items") or [redescendu])[0]
        # Même réinjection que la synchronisation descendante : comparer sans elle
        # éprouverait un chemin que personne n'emprunte.
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import sync_biblio

        extra_map = sync_biblio.build_extra_map(args.groupe, api_key)
        sync_biblio.apply_extra_variables([redescendu], extra_map)
        # Zotero rend le titre court sous `shortTitle` ; la descente le renomme en
        # `title-short`. Sans ce renommage, chaque titre court passait pour un écart.
        sync_biblio.normalise_noms_de_champs([redescendu])
        redescendu["id"] = args.comparer
        local = locales[args.comparer][0]
        ecarts = 0
        for champ in sorted(set(local) | set(redescendu)):
            if champ == "note":
                continue
            a, b = local.get(champ), redescendu.get(champ)
            if json.dumps(a, sort_keys=True, ensure_ascii=False) != json.dumps(
                b, sort_keys=True, ensure_ascii=False
            ):
                print(f"  ✗ {champ}\n      local  : {a!r}\n      Zotero : {b!r}")
                ecarts += 1
        print(f"\n« {args.comparer} » : {ecarts} écart(s) après aller-retour réel.")
        return 1 if ecarts else 0

    if not (args.dry_run or args.pousser):
        p.print_help()
        return 0

    existantes: dict[str, str] = {}
    if args.pousser or api_key:
        items = zotero_tout(f"/groups/{args.groupe}/items", api_key, {"format": "json"})
        for item in items:
            m = re.search(r"citation-key:\s*(\S+)", item.get("data", {}).get("extra", ""), re.I)
            if m:
                existantes[m.group(1)] = item["key"]
        print(f"{len(items)} article(s) dans le groupe {args.groupe}, "
              f"dont {len(existantes)} portant une clé de citation.")

    a_pousser = [(c, e) for c, (e, _livres) in sorted(locales.items()) if c not in existantes]
    if args.limite:
        a_pousser = a_pousser[: args.limite]
    print(f"{len(locales)} référence(s) locales, {len(a_pousser)} à créer.")

    charges = [csl_vers_zotero(e, schema) for _c, e in a_pousser]

    if args.dry_run:
        for cle, item in zip((c for c, _ in a_pousser), charges):
            print(f"\n--- {cle} ---")
            print(json.dumps(item, ensure_ascii=False, indent=2)[:900])
        return 0

    creees = {}
    for debut in range(0, len(charges), 50):
        lot = charges[debut : debut + 50]
        cles_lot = [c for c, _ in a_pousser][debut : debut + 50]
        reponse = zotero(f"/groups/{args.groupe}/items", api_key, "POST", lot)
        # L'échec partiel est le cas normal : la réponse porte trois dictionnaires.
        for indice, item in (reponse.get("successful") or {}).items():
            creees[cles_lot[int(indice)]] = item["key"]
        for indice, message in (reponse.get("failed") or {}).items():
            print(f"✗ {cles_lot[int(indice)]} : {message}", file=sys.stderr)
        print(f"lot {debut // 50 + 1} : {len(reponse.get('successful') or {})} créée(s), "
              f"{len(reponse.get('failed') or {})} en échec, "
              f"{len(reponse.get('unchanged') or {})} inchangée(s)")

    if args.rapport and creees:
        with open(args.rapport, "w", encoding="utf-8") as f:
            json.dump(creees, f, ensure_ascii=False, indent=2)
        print(f"Clés Zotero créées consignées dans {args.rapport} (permet un retour arrière).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
