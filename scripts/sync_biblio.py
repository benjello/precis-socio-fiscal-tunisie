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

Citation keys are read from the "Extra" field in Zotero (citation-key: xxx).
"""

import argparse
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

    print("Fetching citation keys from Zotero...")
    key_map = build_citation_key_map(group_id, api_key)
    print(f"  {len(key_map)} citation keys found")

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
        items = apply_citation_keys(items, key_map, group_id)
        book_items.setdefault(book, []).extend(items)
        print(f"  {collections[ckey]}: {len(items)} items → {book}")

    all_items = zotero_get(
        f"/groups/{group_id}/items",
        api_key,
        params={"format": "csljson"},
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
        if not items:
            continue
        for lang in LANGUAGES:
            out_path = os.path.join(precis_dir, lang, book, "references.json")
            write_csl_json(items, out_path)
            print(f"  Wrote {out_path}")
            written += 1

    if shared_items:
        for lang in LANGUAGES:
            out_path = os.path.join(precis_dir, lang, "references.json")
            write_csl_json(shared_items, out_path)
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
