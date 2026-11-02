#!/usr/bin/env python3
"""Une même clé de références dit la même chose dans tous les livres.

Chaque livre a son `references.json`, et le fonds commun (`precis/fr/references.json`,
`precis/ar/references.json`) s'y ajoute. Une clé définie dans plusieurs fichiers d'une même
langue doit porter les mêmes champs d'identification : type, titre, titre du recueil, volume,
numéro, pages, date, adresse. Sinon la notice affichée change selon le livre, et une page
fausse dans un livre passe inaperçue (cas du 1er novembre 2026 : `lfc-2014` avec les pages
2183-2232 dans un livre et 2095-2142 dans les trois autres ; le fascicule français s'arrête à
la page 2181).

Un champ absent d'une définition et présent dans l'autre compte comme une divergence : la
notice la plus pauvre est à compléter. Les titres se comparent sans majuscules ni ponctuation.
`note`, `title-short`, `accessed` et `author` ne sont pas comparés : ils varient d'un livre à
l'autre sans changer ce qu'est le texte.

Un cas qu'on ne peut pas résoudre tout de suite se déclare dans `scripts/references_tolerances.yml`,
avec une date et une raison ; le contrôle refuse une tolérance sans date, sans raison, ou qui ne
sert plus (la divergence a disparu) : elle doit alors être retirée.

    uv run python scripts/check_references_coherentes.py
"""

from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TOLERANCES = Path(__file__).resolve().parent / "references_tolerances.yml"
CHAMPS = ("type", "title", "container-title", "volume", "issue", "page", "issued", "URL")
NORMALISES = {"title"}
LANGUES = ("fr", "ar")


def normalise(champ: str, valeur) -> str:
    if valeur is None:
        return ""
    texte = json.dumps(valeur, sort_keys=True, ensure_ascii=False)
    if champ in NORMALISES:
        return re.sub(r"[\W_]+", "", texte.casefold())
    return texte


def charger(racine: Path = RACINE) -> dict[str, dict[str, dict[str, dict]]]:
    """langue -> clé -> fichier relatif -> entrée."""
    jeux: dict[str, dict[str, dict[str, dict]]] = {}
    for langue in LANGUES:
        fichiers = sorted(racine.glob(f"precis/{langue}/references.json")) + sorted(
            racine.glob(f"precis/{langue}/*/references.json")
        )
        jeu: dict[str, dict[str, dict]] = {}
        for fichier in fichiers:
            rel = fichier.relative_to(racine).as_posix()
            for entree in json.loads(fichier.read_text(encoding="utf-8")).get("items", []):
                jeu.setdefault(entree["id"], {})[rel] = entree
        jeux[langue] = jeu
    return jeux


def divergences(jeu: dict[str, dict[str, dict]]) -> dict[str, dict[str, dict[str, object]]]:
    """clé -> champ -> fichier -> valeur, pour les seuls champs qui diffèrent."""
    sortie: dict[str, dict[str, dict[str, object]]] = {}
    for cle, definitions in jeu.items():
        if len(definitions) < 2:
            continue
        for champ in CHAMPS:
            valeurs = {fichier: e.get(champ) for fichier, e in definitions.items()}
            if len({normalise(champ, v) for v in valeurs.values()}) > 1:
                sortie.setdefault(cle, {})[champ] = valeurs
    return sortie


def charger_tolerances(chemin: Path = TOLERANCES) -> list[dict]:
    if not chemin.exists():
        return []
    import yaml

    return yaml.safe_load(chemin.read_text(encoding="utf-8")) or []


def ecarts(jeux, tolerances: list[dict]) -> list[str]:
    problemes: list[str] = []
    tol: dict[tuple[str, str], set[str]] = {}
    for t in tolerances:
        for cle in ("langue", "cle", "champs", "date", "raison"):
            if not t.get(cle):
                problemes.append(f"tolérance incomplète (« {cle} » manque) : {t}")
                break
        else:
            try:
                datetime.date.fromisoformat(str(t["date"]))
            except ValueError:
                problemes.append(f"tolérance : date illisible {t['date']!r} ({t['cle']})")
            tol[(t["langue"], t["cle"])] = set(t["champs"])
    vues: set[tuple[str, str, str]] = set()
    for langue, jeu in jeux.items():
        for cle, champs in divergences(jeu).items():
            for champ, valeurs in champs.items():
                vues.add((langue, cle, champ))
                if champ in tol.get((langue, cle), ()):
                    continue
                detail = " ; ".join(f"{f.removeprefix('precis/')} : {v!r}" for f, v in valeurs.items())
                problemes.append(f"[{langue}] {cle}, champ « {champ} » : {detail}")
    for (langue, cle), champs in tol.items():
        for champ in sorted(champs):
            if (langue, cle, champ) not in vues:
                problemes.append(
                    f"tolérance inutile : [{langue}] {cle}, champ « {champ} » ne diverge plus (à retirer)"
                )
    return problemes


def main() -> int:
    problemes = ecarts(charger(), charger_tolerances())
    if problemes:
        print(f"✗ {len(problemes)} divergence(s) entre les définitions d'une même clé de références :")
        for p in problemes:
            print(f"  - {p}")
        print("  Harmonise d'après la source primaire, ou déclare le cas dans scripts/references_tolerances.yml.")
        return 1
    print("✓ Les clés de références définies dans plusieurs livres disent la même chose.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
