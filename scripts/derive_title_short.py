"""Dérive le champ `title-short` des entrées juridiques des bibliographies CSL-JSON.

    uv run python scripts/derive_title_short.py --dry-run   # mesure, n'écrit rien
    uv run python scripts/derive_title_short.py             # écrit

POURQUOI. Les entrées de type `legislation` n'ont pas d'`author`. Citeproc met alors le
`title` en position d'auteur, et le titre officiel d'un texte tunisien fait 150 caractères
de médiane : une citation `[@loi60-30, art. 34]` rend une parenthèse de plus de cent
caractères, qui coupe la phrase en deux.

Le titre officiel est régulier : « Loi n° 60-30 du 14 décembre 1960, relative à
l'organisation des régimes de sécurité sociale ». La forme courte est le segment qui
précède le participe — « Loi n° 60-30 du 14 décembre 1960 » —, c'est-à-dire ce qui
identifie le texte sans le décrire. Elle se dérive donc mécaniquement, et la description
reste intégralement dans la bibliographie.

CE QUE LE SCRIPT NE FAIT PAS :
  - il ne touche qu'aux entrées `legislation` : les rapports, ouvrages et jeux de données
    ont un auteur, et leur citation est déjà courte ;
  - il n'écrase jamais un `title-short` existant ;
  - il ne devine pas. Les entrées dont le titre ne porte aucun participe reconnu sont
    laissées telles quelles et listées : leur forme courte doit être écrite à la main
    (ainsi du « Code de l'IRPP et de l'IS », qui n'a pas de forme « n° X du DATE »).

AVERTISSEMENT. `scripts/sync_biblio.py` redescend les bibliographies depuis Zotero et
**écrase ce qui n'y est pas monté**. Un `title-short` posé ici est donc provisoire : sa
place définitive est le champ `shortTitle` de Zotero, où `push_biblio.py` sait le porter.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# Les participes qui ouvrent la partie descriptive d'un intitulé tunisien. L'ordre importe
# peu, l'alternance est ancrée au début du segment descriptif.
PARTICIPES = (
    "relatif", "relative", "relatifs", "relatives",
    "portant", "fixant", "modifiant", "complétant", "amendant", "abrogeant",
    "instituant", "créant", "organisant", "étendant", "prorogeant", "approuvant",
    "promulguant", "concernant", "ayant pour objet",
)
COUPE = re.compile(
    r"^(.*?),?\s+(?:" + "|".join(re.escape(p) for p in PARTICIPES) + r")\s",
    re.IGNORECASE,
)


def forme_courte(titre: str) -> str | None:
    """« Loi n° 60-30 du 14 décembre 1960, relative à … » → « Loi n° 60-30 du 14 décembre 1960 »."""
    m = COUPE.match(titre)
    if not m:
        return None
    court = m.group(1).strip().rstrip(",")
    # Un segment qui ne porterait ni numéro ni date n'identifie rien : on s'abstient.
    if not re.search(r"n°\s*\d|\bdu\s+\d", court):
        return None
    # Espace insécable après « n° », que le titre source l'ait ou non : huit entrées
    # écrivent « n°60-30 » quand les autres écrivent « n° 60-30 ». L'écart ne se voyait
    # pas tant que la citation portait tout l'intitulé ; la forme courte le met à nu.
    # On ne corrige QUE la forme courte : `title` reste l'intitulé officiel, tel que publié.
    court = re.sub(r"n°\s*(?=\d)", "n° ", court)
    return court or None


def fichiers() -> list[Path]:
    out = []
    for langue in ("fr", "ar"):
        base = RACINE / "precis" / langue
        out.append(base / "references.json")
        out.extend(sorted(base.glob("*/references.json")))
    return [f for f in out if f.exists()]


def traite(chemin: Path, ecrire: bool) -> tuple[int, int, list[str]]:
    donnees = json.loads(chemin.read_text(encoding="utf-8"))
    items = donnees["items"] if isinstance(donnees, dict) else donnees
    vus = derives = 0
    rebelles = []
    for item in items:
        if item.get("type") != "legislation":
            continue
        vus += 1
        if item.get("title-short"):          # jamais écraser
            continue
        court = forme_courte(item.get("title", ""))
        if court is None:
            rebelles.append(item.get("id", "?"))
            continue
        item["title-short"] = court
        derives += 1
    if ecrire and derives:
        # Même écriture que scripts/sync_biblio.py : ne pas reformater le fichier entier.
        chemin.write_text(
            json.dumps(donnees, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    return vus, derives, rebelles


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="mesurer sans écrire")
    args = ap.parse_args()

    total_vus = total_derives = 0
    tous_rebelles = []
    for chemin in fichiers():
        vus, derives, rebelles = traite(chemin, ecrire=not args.dry_run)
        if vus:
            rel = chemin.relative_to(RACINE)
            print(f"  {str(rel):52} {derives:3} dérivés / {vus:3} entrées juridiques")
        total_vus += vus
        total_derives += derives
        tous_rebelles.extend(rebelles)

    print(f"\n{total_derives} formes courtes dérivées sur {total_vus} entrées juridiques")
    if tous_rebelles:
        print(f"\n{len(tous_rebelles)} entrée(s) sans forme courte dérivable — à écrire à la main :")
        for cle in tous_rebelles:
            print(f"  - {cle}")
    if args.dry_run:
        print("\n(--dry-run : rien n'a été écrit)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
