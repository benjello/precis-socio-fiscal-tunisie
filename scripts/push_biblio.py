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
VARIABLES_EXTRA = ("issue", "authority", "event-date", "collection-title", "genre")


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

    for csl_var, champ in CHAMPS.items():
        if csl_var not in entree:
            continue
        cible = alias.get(champ, champ)
        if cible in disponibles:
            item[cible] = str(entree[csl_var])
        elif csl_var in VARIABLES_EXTRA:
            extra_variables.append(f"{csl_var}: {entree[csl_var]}")
        else:
            raise ValueError(
                f"{entree.get('id')} : le champ « {csl_var} » n'a pas de place dans "
                f"{type_zotero} et n'est pas prévu pour Extra"
            )

    for csl_var in VARIABLES_EXTRA:
        if csl_var in entree and not any(v.startswith(f"{csl_var}:") for v in extra_variables):
            valeur = entree[csl_var]
            if csl_var.endswith("date") and isinstance(valeur, dict):
                valeur = date_csl_vers_zotero(valeur)
            extra_variables.append(f"{csl_var}: {valeur}")

    if "issued" in entree:
        champ_date = alias.get("date", "date")
        if champ_date in disponibles:
            item[champ_date] = date_csl_vers_zotero(entree["issued"])

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
        # duplique pas.
        note = "\n".join(l for l in note.splitlines()
                         if not l.lower().startswith("citation-key:")).strip()
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

    lignes, note = [], []
    for ligne in (item.get("extra") or "").splitlines():
        m = re.match(r"^([A-Za-z-]+):\s*(.+)$", ligne)
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
}


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
        reponse = zotero(f"/groups/{args.groupe}/items", api_key, "POST", charges)
        print(f"{len(reponse.get('successful') or {})} corrigée(s), "
              f"{len(reponse.get('failed') or {})} en échec")
        for indice, message in (reponse.get("failed") or {}).items():
            print(f"  ✗ {charges[int(indice)]['key']} : {message}", file=sys.stderr)
        return 1 if reponse.get("failed") else 0

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
