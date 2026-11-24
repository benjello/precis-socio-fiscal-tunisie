#!/usr/bin/env python3
"""Écrire une série dans le cache de l'ouvrage et sa fiche dans `catalog.snapshot.yml`.

Les générateurs de séries (`scripts/generate_*.py`) répétaient le même code : écrire le CSV dans
`precis/_seriescache/`, puis relire, compléter et réécrire le snapshot du catalogue. Ce module le fait
une fois :

    from cache_series import ecrire_serie
    ecrire_serie("ma-serie", table, {"titre": "…", "sources": ["cle-csl"], "source_ligne": "…",
                                     "unite": "millions de dinars courants"})

`table` est un DataFrame pandas ou une liste de dictionnaires. La fiche remplace celle qui porte le
même identifiant, à sa place dans le snapshot ; une fiche nouvelle s'ajoute à la fin. La fiche doit
porter `titre` et `sources` (au moins une clé de citation) ; le script refuse sinon.

Ce module n'est pas sous `scripts/figtools.py` à dessein : un fichier de ce préfixe fait rendre tous
les livres par verifier.sh.
"""
from __future__ import annotations

import csv
from pathlib import Path

import yaml

CACHE = Path(__file__).resolve().parent.parent / "precis" / "_seriescache"


def ecrire_serie(series_id: str, table, fiche: dict, cache: Path = CACHE) -> Path:
    if not fiche.get("titre") or not fiche.get("sources"):
        raise ValueError(f"{series_id} : la fiche doit porter un titre et au moins une source")
    cache.mkdir(parents=True, exist_ok=True)
    chemin = cache / f"{series_id}.csv"
    if hasattr(table, "to_csv"):
        table.to_csv(chemin, index=False)
    else:
        lignes = list(table)
        if not lignes:
            raise ValueError(f"{series_id} : table vide")
        with chemin.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(lignes[0]))
            w.writeheader()
            w.writerows(lignes)
    snap = cache / "catalog.snapshot.yml"
    entrees = (yaml.safe_load(snap.read_text("utf-8")) or []) if snap.exists() else []
    nouvelle = {"id": series_id, **{k: v for k, v in fiche.items() if k != "id"}}
    for i, e in enumerate(entrees):
        if e.get("id") == series_id:
            entrees[i] = nouvelle
            break
    else:
        entrees.append(nouvelle)
    snap.write_text(yaml.safe_dump(entrees, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return chemin
