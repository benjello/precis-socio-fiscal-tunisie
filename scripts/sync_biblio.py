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

Items not in any collection (or in "Commun") go to:
    precis/{lang}/references.json     (shared across books)
"""

import argparse
import json
import os
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
}


def zotero_get(path, api_key, params=None):
    """Fetch from Zotero API, handling pagination."""
    if params is None:
        params = {}
    params.setdefault("limit", "100")
    params.setdefault("format", "csljson")

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


def get_collections(group_id, api_key):
    """Return {collection_key: collection_name} mapping."""
    path = f"/groups/{group_id}/collections"
    req = urllib.request.Request(f"{BASE_URL}{path}?format=json")
    req.add_header("Zotero-API-Key", api_key)

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())

    return {c["key"]: c["data"]["name"] for c in data}


def main():
    parser = argparse.ArgumentParser(description="Sync Zotero → CSL-JSON")
    parser.add_argument("--key", default=os.environ.get("ZOTERO_API_KEY"))
    parser.add_argument("--group", default=os.environ.get("ZOTERO_GROUP_ID", DEFAULT_GROUP_ID))
    args = parser.parse_args()

    if not args.key:
        print("Error: Zotero API key required (--key or ZOTERO_API_KEY env var)")
        sys.exit(1)

    group_id = args.group
    api_key = args.key
    precis_dir = os.path.join(os.path.dirname(__file__), "..", "precis")

    collections = get_collections(group_id, api_key)
    print(f"Found {len(collections)} collections: {list(collections.values())}")

    book_items = {}  # book_name -> [items]
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
        )
        book_items.setdefault(book, []).extend(items)
        print(f"  {collections[ckey]}: {len(items)} items → {book}")

    all_items = zotero_get(f"/groups/{group_id}/items", api_key)

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
        if not items:
            continue
        csl_data = {"items": items}
        for lang in LANGUAGES:
            out_path = os.path.join(precis_dir, lang, book, "references.json")
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(csl_data, f, ensure_ascii=False, indent=2)
            print(f"  Wrote {out_path}")
            written += 1

    if shared_items:
        csl_data = {"items": shared_items}
        for lang in LANGUAGES:
            out_path = os.path.join(precis_dir, lang, "references.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(csl_data, f, ensure_ascii=False, indent=2)
            print(f"  Wrote {out_path}")
            written += 1

    if written == 0 and not all_items:
        print("Zotero library is empty. No files written.")
    else:
        print(f"Done. {written} files written.")


if __name__ == "__main__":
    main()
