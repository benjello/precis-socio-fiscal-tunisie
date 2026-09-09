"""Sync bibliographies from a Zotero group library to local CSL-JSON files.

Usage:
    python scripts/sync_biblio.py [--key KEY] [--group GROUP_ID]

Environment variables (fallback):
    ZOTERO_API_KEY  – API key with read access to the group
    ZOTERO_GROUP_ID – Group library ID (default: 6529669)

The script maps Zotero collections to book directories:
    Collection "Fiscalité"            → precis/{lang}/fiscalite/references.json
    Collection "Retraites"            → precis/{lang}/retraites/references.json
    Collection "Prestations sociales" → precis/{lang}/prestations_sociales/references.json
    Collection "Rémunérations publiques" → precis/{lang}/remunerations_publiques/references.json

Items not in any collection (or in "Commun") go to:
    precis/{lang}/references.json     (shared across books)

Citation keys are read from the "Extra" field in Zotero (citation-key: xxx).
"""

import argparse
import copy
import json
import os
import re
import sys
import urllib.request
import urllib.error

BASE_URL = "https://api.zotero.org"
DEFAULT_GROUP_ID = "6529669"
LANGUAGES = ["fr", "ar"]

COLLECTION_TO_BOOK = {
    "fiscalité": "fiscalite",
    "fiscalite": "fiscalite",
    "retraites": "retraites",
    "prestations sociales": "prestations_sociales",
    "rémunérations publiques": "remunerations_publiques",
    "remunerations publiques": "remunerations_publiques",
}


def zotero_get(path, api_key, params=None):
    """Fetch from Zotero API, handling pagination."""
    if params is None:
        params = {}
    params.setdefault("limit", "100")

    results = []
    start = 0

    while True:
        params["start"] = str(start)
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{BASE_URL}{path}?{query}"

        req = urllib.request.Request(url)
        req.add_header("Zotero-API-Key", api_key)

        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                total = int(resp.headers.get("Total-Results", 0))
        except urllib.error.HTTPError as e:
            print(f"Error fetching {url}: {e.code} {e.reason}")
            sys.exit(1)

        if isinstance(data, dict) and "items" in data:
            results.extend(data["items"])
        elif isinstance(data, list):
            results.extend(data)
        else:
            results.append(data)

        start += 100
        if start >= total:
            break

    return results


def extract_citation_key(extra):
    """Extract citation-key from Zotero Extra field."""
    if not extra:
        return None
    match = re.search(r"citation-key:\s*(\S+)", extra, re.IGNORECASE)
    return match.group(1) if match else None


def get_collections(group_id, api_key):
    """Return {collection_key: collection_name} mapping."""
    path = f"/groups/{group_id}/collections"
    req = urllib.request.Request(f"{BASE_URL}{path}?format=json")
    req.add_header("Zotero-API-Key", api_key)

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())

    return {c["key"]: c["data"]["name"] for c in data}


def build_citation_key_map(group_id, api_key):
    """Fetch all items as JSON and return {zotero_key: citation_key}."""
    items = zotero_get(
        f"/groups/{group_id}/items",
        api_key,
        params={"format": "json"},
    )
    key_map = {}
    for item in items:
        zkey = item["key"]
        extra = item.get("data", {}).get("extra", "")
        cite_key = extract_citation_key(extra)
        if cite_key:
            key_map[zkey] = cite_key
    return key_map


# Variables CSL qu'aucun champ Zotero ne peut accueillir pour le type visé, et qui
# vivent donc dans le champ Extra. Le numéro de fascicule du JORT est dans ce cas pour
# les textes législatifs : le type `statute` n'a pas de champ `issue`.
VARIABLES_EXTRA = ("issue", "authority", "event-date", "collection-title", "genre")


def parse_date_extra(texte):
    morceaux = [int(x) for x in str(texte).split("-") if x.strip().isdigit()]
    return {"date-parts": [morceaux]} if morceaux else None


def build_extra_map(group_id, api_key):
    """{zotero_key: {variable CSL: valeur}} lues dans le champ Extra."""
    items = zotero_get(
        f"/groups/{group_id}/items",
        api_key,
        params={"format": "json"},
    )
    extras = {}
    for item in items:
        variables = {}
        for ligne in (item.get("data", {}).get("extra", "") or "").splitlines():
            m = re.match(r"^([A-Za-z-]+):\s*(.+)$", ligne)
            if m and m.group(1) in VARIABLES_EXTRA:
                valeur = m.group(2).strip()
                variables[m.group(1)] = (
                    parse_date_extra(valeur) if m.group(1).endswith("date") else valeur
                )
        if variables:
            extras[item["key"]] = variables
    return extras


ARABE = re.compile(r"[\u0600-\u06FF]")

# Champs dont la version arabe est une TRADUCTION et non une donnée : les préserver.
# Le reste — URL, dates, pages, numéro de fascicule — est identique dans les deux
# langues et doit suivre la source canonique.
CHAMPS_TRADUITS = ("title", "title-short", "container-title", "publisher",
                   "publisher-place", "authority", "author", "editor")

# Le JORT paraît en deux éditions, et pist.tn les sert sous deux chemins qui ne diffèrent
# que par une lettre de répertoire et un préfixe de fichier, les chiffres étant identiques :
#
#     .../jort/2014/2014F/Jo0232014.pdf   (française)
#     .../jort/2014/2014A/Ja0232014.pdf   (arabe)
#
# Une bibliographie arabe qui renvoie à l'édition arabe ne se trompe pas : elle renvoie au
# texte que son lecteur peut lire. La conversion étant mécanique, elle se dérive au lieu de
# se saisir — deux formats coexistent, cinq chiffres avant 2000 et sept après, et le motif
# couvre les deux.
JORT_FR = re.compile(r"/(\d{4})F/Jo(\d+)\.pdf", re.I)
JORT_AR = re.compile(r"/(\d{4})A/Ja(\d+)\.pdf", re.I)

# Fascicules dont l'édition homologue n'existe pas sur pist.tn. La dérivation les laisse
# tels quels : mieux vaut renvoyer à l'autre édition qu'à un lien mort. Régénéré par
# `--verifier-urls`, versionné pour que la descente reste déterministe et hors ligne.
FICHIER_EXCEPTIONS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "precis", "urls-jort.json"
)


def charge_exceptions():
    if not os.path.exists(FICHIER_EXCEPTIONS):
        return set()
    with open(FICHIER_EXCEPTIONS, encoding="utf-8") as f:
        return set(json.load(f).get("sans_homologue", []))


def url_jort(url, langue, exceptions=()):
    """Rend l'URL du JORT dans l'édition de `langue`, ou l'URL inchangée.

    Ne touche à rien d'autre : une URL qui ne suit pas le motif du JORT — INS, article
    académique, texte hébergé ailleurs — ressort telle quelle.
    """
    if not url or url in exceptions:
        return url
    if langue == "ar":
        return JORT_FR.sub(lambda m: f"/{m.group(1)}A/Ja{m.group(2)}.pdf", url)
    return JORT_AR.sub(lambda m: f"/{m.group(1)}F/Jo{m.group(2)}.pdf", url)


def applique_edition(items, langue, exceptions):
    change = 0
    for item in items:
        avant = item.get("URL", "")
        apres = url_jort(avant, langue, exceptions)
        if apres != avant:
            item["URL"] = apres
            change += 1
    if change:
        print(f"    {change} lien(s) JORT basculé(s) vers l'édition {langue}")
    return items


def contient_arabe(valeur):
    if isinstance(valeur, str):
        return bool(ARABE.search(valeur))
    if isinstance(valeur, list):
        return any(contient_arabe(v) for v in valeur)
    if isinstance(valeur, dict):
        return any(contient_arabe(v) for v in valeur.values())
    return False


def preserve_traductions(items, chemin_existant):
    """Garde les champs déjà traduits en arabe, prend le reste de Zotero.

    La bibliothèque Zotero est en français : une descente brute remplacerait
    « قرار من وزير الشؤون الاجتماعية… » par « Arrêté du ministre des affaires
    sociales… », effaçant un travail de traduction que rien ne referait.

    La règle est mécanique et ne préserve donc que ce qui est réellement traduit :
    un champ n'est gardé que s'il est en caractères arabes localement et ne l'est pas
    dans ce qui descend. Une correction faite côté Zotero — une URL réparée, une page
    rectifiée — passe donc toujours.
    """
    if not os.path.exists(chemin_existant):
        return items
    with open(chemin_existant, encoding="utf-8") as f:
        anciens = {e.get("id"): e for e in json.load(f).get("items", [])}
    preserves = 0
    for item in items:
        ancien = anciens.get(item.get("id"))
        if not ancien:
            continue
        for champ in CHAMPS_TRADUITS:
            if champ in ancien and contient_arabe(ancien[champ]) and not contient_arabe(item.get(champ)):
                item[champ] = ancien[champ]
                preserves += 1
    if preserves:
        print(f"    {preserves} champ(s) arabes préservés dans {os.path.basename(os.path.dirname(chemin_existant))}")
    return items


def sans_cle_de_citation(items):
    """Écarte les articles qui n'ont pas de clé de citation.

    Leur identifiant reste celui de Zotero — « 23975222/K2B3EV4C » —, qui ne peut pas
    s'écrire `[@…]` dans le texte. Ils ne sont donc citables par personne, et leur place
    dans une bibliographie publiée est nulle : ce sont des pièces jointes ou des
    résidus. On les écarte plutôt que de les supprimer côté Zotero, où ils peuvent
    servir à autre chose.
    """
    gardes = [i for i in items if "/" not in str(i.get("id", ""))]
    ecartes = len(items) - len(gardes)
    if ecartes:
        print(f"    {ecartes} article(s) sans clé de citation écarté(s)")
    return gardes


# Champs que l'export de l'API émet sous leur nom ZOTERO au lieu de leur nom CSL. Un
# `shortTitle` dans un fichier CSL-JSON n'est pas lu par citeproc : le titre court est
# simplement ignoré au rendu, sans erreur ni avertissement.
RENOMMAGES = {"shortTitle": "title-short"}


def normalise_noms_de_champs(csl_items):
    for item in csl_items:
        for zotero, csl in RENOMMAGES.items():
            if zotero in item:
                item.setdefault(csl, item.pop(zotero))
    return csl_items


def normalise_auteurs(csl_items):
    """Rend leur forme `literal` aux auteurs institutionnels.

    Un auteur enregistré en un seul champ dans Zotero — « Institut national de la
    statistique », « Tunisie. Ministère des finances… » — est un nom d'institution, pas
    un patronyme. CSL a `literal` pour cela, mais l'export de l'API le rend en
    `{family: "…", given: ""}`, ce qui ferait citer l'institution comme une personne.
    Le `given` vide est la signature de ce cas.
    """
    for item in csl_items:
        for role in ("author", "editor", "contributor", "translator"):
            for nom in item.get(role) or []:
                if isinstance(nom, dict) and nom.get("family") and not nom.get("given"):
                    nom["literal"] = nom.pop("family")
                    nom.pop("given", None)
    return csl_items


def apply_extra_variables(csl_items, extra_map):
    """Réinjecte les variables CSL logées dans Extra.

    L'export CSL-JSON de l'API **ne les rend pas** : vérifié sur pièce, un arrêté poussé
    avec `issue: 4`, `authority: République tunisienne` et `event-date` en Extra redescend
    sans aucun des trois. Le client Zotero, lui, les honore — la lacune est celle de
    l'exportateur de l'API. Sans cette réinjection, chaque synchronisation descendante
    amputerait les fichiers locaux de la provenance : numéro de fascicule du JORT en tête.
    """
    for item in csl_items:
        zkey = item.get("id", "").split("/")[-1]
        for variable, valeur in (extra_map.get(zkey) or {}).items():
            if valeur is not None and variable not in item:
                item[variable] = valeur
    return csl_items


def apply_citation_keys(csl_items, key_map, group_id):
    """Replace Zotero IDs with human-readable citation keys."""
    for item in csl_items:
        old_id = item.get("id", "")
        zkey = old_id.split("/")[-1] if "/" in old_id else old_id
        if zkey in key_map:
            item["id"] = key_map[zkey]
    return csl_items


def check_url(url, timeout=10):
    """Check if a URL is reachable. Returns (status_code, error_msg)."""
    try:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "Mozilla/5.0 (biblio-check)")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return None, str(e)


def check_urls(all_items, group_id):
    """Verify all URLs in bibliography items. Returns list of broken items."""
    zotero_web = f"https://www.zotero.org/groups/{group_id}"
    broken = []
    print("\nChecking URLs...")
    for item in all_items:
        cid = item.get("id", "?")
        url = item.get("URL", "")
        doi = item.get("DOI", "")

        if not url and not doi:
            continue

        check = url or f"https://doi.org/{doi}"
        status, err = check_url(check)

        if status and 200 <= status < 400:
            print(f"  ✓ {cid:25s} {status} {check[:70]}")
        elif status:
            print(f"  ✗ {cid:25s} {status} {check[:70]}")
            broken.append((cid, check, f"HTTP {status}"))
        else:
            print(f"  ✗ {cid:25s} ERR {check[:70]}")
            broken.append((cid, check, err))

    if broken:
        print(f"\n⚠ {len(broken)} broken URL(s) found:")
        for cid, url, reason in broken:
            print(f"    @{cid}: {reason}")
            print(f"      → fix in Zotero: {zotero_web}/items")
    else:
        print("  All URLs OK.")

    return broken


def write_csl_json(items, path):
    """Write CSL-JSON file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"items": items}, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Sync Zotero → CSL-JSON")
    parser.add_argument("--key", default=os.environ.get("ZOTERO_API_KEY"))
    parser.add_argument("--group", default=os.environ.get("ZOTERO_GROUP_ID", DEFAULT_GROUP_ID))
    parser.add_argument("--no-check", action="store_true", help="Skip URL verification")
    args = parser.parse_args()

    if not args.key:
        print("Error: Zotero API key required (--key or ZOTERO_API_KEY env var)")
        sys.exit(1)

    group_id = args.group
    api_key = args.key
    precis_dir = os.path.join(os.path.dirname(__file__), "..", "precis")

    exceptions = charge_exceptions()
    if exceptions:
        print(f"{len(exceptions)} fascicule(s) sans édition homologue, laissés tels quels")

    print("Fetching citation keys from Zotero...")
    key_map = build_citation_key_map(group_id, api_key)
    print(f"  {len(key_map)} citation keys found")

    extra_map = build_extra_map(group_id, api_key)
    print(f"  {len(extra_map)} item(s) carrying CSL variables in Extra")

    collections = get_collections(group_id, api_key)
    print(f"Found {len(collections)} collections: {list(collections.values())}")

    book_items = {}
    shared_items = []

    collection_key_to_book = {}
    for ckey, cname in collections.items():
        book = COLLECTION_TO_BOOK.get(cname.lower().strip())
        if book:
            collection_key_to_book[ckey] = book

    for ckey, book in collection_key_to_book.items():
        items = zotero_get(
            f"/groups/{group_id}/collections/{ckey}/items",
            api_key,
            params={"format": "csljson"},
        )
        items = normalise_noms_de_champs(
            normalise_auteurs(apply_extra_variables(items, extra_map))
        )
        items = apply_citation_keys(items, key_map, group_id)
        book_items.setdefault(book, []).extend(items)
        print(f"  {collections[ckey]}: {len(items)} items → {book}")

    all_items = zotero_get(
        f"/groups/{group_id}/items",
        api_key,
        params={"format": "csljson"},
    )
    all_items = normalise_noms_de_champs(
        normalise_auteurs(apply_extra_variables(all_items, extra_map))
    )
    all_items = apply_citation_keys(all_items, key_map, group_id)

    collected_ids = set()
    for items in book_items.values():
        for item in items:
            collected_ids.add(item.get("id"))

    for item in all_items:
        if item.get("id") not in collected_ids:
            shared_items.append(item)

    if shared_items:
        print(f"  Shared/Commun: {len(shared_items)} items")

    written = 0
    for book, items in book_items.items():
        items = sans_cle_de_citation(items)
        if not items:
            continue
        for lang in LANGUAGES:
            out_path = os.path.join(precis_dir, lang, book, "references.json")
            # Chaque langue reçoit sa propre copie : `preserve_traductions` modifie les
            # items en place, et l'arabe ne doit pas contaminer le français.
            a_ecrire = applique_edition(copy.deepcopy(items), lang, exceptions)
            if lang == "ar":
                a_ecrire = preserve_traductions(a_ecrire, out_path)
            write_csl_json(a_ecrire, out_path)
            print(f"  Wrote {out_path}")
            written += 1

    shared_items = sans_cle_de_citation(shared_items)
    if shared_items:
        for lang in LANGUAGES:
            out_path = os.path.join(precis_dir, lang, "references.json")
            a_ecrire = applique_edition(copy.deepcopy(shared_items), lang, exceptions)
            if lang == "ar":
                a_ecrire = preserve_traductions(a_ecrire, out_path)
            write_csl_json(a_ecrire, out_path)
            print(f"  Wrote {out_path}")
            written += 1

    if written == 0 and not all_items:
        print("Zotero library is empty. No files written.")
    else:
        print(f"Done. {written} files written.")

    if not args.no_check:
        broken = check_urls(all_items, group_id)
        if broken:
            sys.exit(1)


if __name__ == "__main__":
    main()
