"""Snapshote les deux séries Banque mondiale 1985-1991 et 1990-1996 des finances communales.

Pourquoi un script à part. L'entrée `finances-locales-bm-1985-2012` du catalogue de
`tunisia-data` réunit trois fichiers séparés — rapports de 1992, de 1997 et de 2014 —, mais
son champ `output` ne désigne que le dernier : `tunisia_data.load()`, donc
`figtools.refresh_cache()`, ne rend que la série 2002-2012. Les deux autres fichiers sont
pourtant traités, contrôlés et décrits par la même fiche de source
(`sources/finances-locales-banque-mondiale.md`).

Ce script copie ces deux fichiers, tels quels, dans le cache du précis, sous deux
identifiants propres : `finances-locales-bm-1992` et `finances-locales-bm-1997`. Leur
provenance est déclarée par le module de figure (`figtools.register_provenance`), avec les
clés de citation et la fiche de l'entrée parente. `figtools.series()` les lit alors comme
toute autre série : l'entrepôt ne les connaissant pas sous ces identifiants, il retombe
sur le cache.

À retirer le jour où `tunisia-data` déclarera ces deux fichiers comme séries distinctes
du catalogue : `refresh_cache()` suffira alors.

    uv run python scripts/snapshot_finances_locales_bm.py [--entrepot ~/projets/tunisia-data]
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

CACHE = Path(__file__).resolve().parent.parent / "precis" / "_seriescache"
FICHIERS = {
    "finances-locales-bm-1992": "data/processed/finances_locales/bm1992_communes_1985_1991.csv",
    "finances-locales-bm-1997": "data/processed/finances_locales/bm1997_communes_1990_1996.csv",
}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--entrepot", type=Path, default=Path.home() / "projets" / "tunisia-data",
                    help="racine du dépôt tunisia-data")
    args = ap.parse_args()
    for sid, rel in FICHIERS.items():
        src = args.entrepot / rel
        if not src.exists():
            raise SystemExit(f"fichier absent : {src}")
        shutil.copyfile(src, CACHE / f"{sid}.csv")
        print(f"{sid} ← {rel}")


if __name__ == "__main__":
    main()
