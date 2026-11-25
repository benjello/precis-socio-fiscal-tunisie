"""Passage d'un poste de l'ouvrage au montant des comptes de la nation, année par année.

Les blocs « passage » des chapitres (quatrième bloc du gabarit d'une section de dispositif,
docs/notes/plan-par-operations.md, règle 6) rapprochent le montant d'un poste de la case des comptes
des secteurs à laquelle le registre `precis/fr/postes-comptables.csv` le rattache. Ce module lit le
registre, la série du poste et les comptes des secteurs (`precis/_seriescache/cnat-secteurs.csv`) par
les fonctions de `scripts/reconstruire_comptes.py` : même lecture des séries (`montant`), même édition
des comptes pour chaque année (`edition_pour` : la dernière où l'année est définitive). Aucune valeur
n'est saisie ici.

Appelé depuis une cellule Python d'un chapitre (dossier du livre) :

    import sys; sys.path.insert(0, "../../../scripts")
    import passage_comptes as pc
    pc.lignes("remunerations-collectivites")
"""
from __future__ import annotations

from functools import lru_cache

import reconstruire_comptes as rc

fr = rc.fr


@lru_cache(maxsize=1)
def registre() -> dict:
    return {l["poste"]: l for l in rc.lire_csv(rc.REGISTRE)}


@lru_cache(maxsize=1)
def secteurs() -> tuple:
    return tuple(rc.lire_csv(rc.CACHE / "cnat-secteurs.csv"))


@lru_cache(maxsize=1)
def libelles() -> dict:
    """Intitulé de l'INS par opération, d'après le sommaire engendré."""
    return {l["operation"]: l["libelle_ins"] for l in rc.lire_csv(rc.FR / "sommaire-comptes.csv")}


def secteur_ins(p: dict) -> str:
    """Secteur du compte où le poste s'inscrit : celui qui verse en emplois, celui qui reçoit en ressources."""
    return p["secteur_verse"] if p["cote"] == "emplois" else p["secteur_recoit"]


def cible(secteur: str, cote: str, code: str, operation: str, an: int) -> tuple[float | None, str, str]:
    """Montant de l'INS, édition retenue et statut de l'année dans cette édition."""
    ls = [l for l in secteurs() if str(l["annee"]) == str(an)]
    if not ls:
        return None, "", ""
    ed = rc.edition_pour(ls, an)
    v = [l for l in ls if l["edition"] == ed and l["secteur"] == secteur and l["cote"] == cote
         and l["code_scn2008"] == code and l["operation"] == operation]
    return (float(v[-1]["valeur"]), ed, v[-1]["statut_annee"]) if v else (None, ed, "")


def montant(poste: str, an: int) -> float | None:
    p = registre()[poste]
    return rc.montant(p["serie"], p["colonne"], an)[0]


def annees() -> list[int]:
    """Années publiées par les comptes des secteurs, toutes éditions confondues."""
    return sorted({int(l["annee"]) for l in secteurs()})


def lignes(poste: str, annees_=None) -> list[dict]:
    """Une ligne par année où le poste et la case de l'INS sont tous deux chiffrés."""
    p = registre()[poste]
    annees_ = annees() if annees_ is None else annees_
    out = []
    for an in annees_:
        m = montant(poste, an)
        if m is None:
            continue
        i, ed, st = cible(secteur_ins(p), p["cote"], p["code_scn"], p["operation"], an)
        if i is None:
            continue
        out.append({"annee": an, "montant": m, "ins": i, "edition": ed, "statut": st,
                    "part": 100 * m / i if i else None})
    return out


def pct(v: float | None) -> str:
    """Pourcentage à la française. L'espace insécable est écrit en entité HTML : une chaîne rendue par une
    expression en ligne `{python}` passe par sa représentation, qui imprimerait « \\xa0 » en toutes lettres."""
    return "—" if v is None else f"{v:.1f}".replace(".", ",") + "&nbsp;%"


def annee_reference() -> int:
    """Année de référence du compte reconstruit (precis/fr/annee-reference.yml)."""
    return int(rc.yaml.safe_load(rc.CONFIG.read_text(encoding="utf-8"))["annee"])


def extremes(d: dict, cle: str = "part") -> dict:
    """Plus bas et plus haut d'un dictionnaire {année: ligne}, mis en forme ; « — » si vide."""
    if not d:
        return {"min": "—", "max": "—", "an_min": "—", "an_max": "—", "premier": "—", "dernier": "—"}
    a_min = min(d, key=lambda a: d[a][cle])
    a_max = max(d, key=lambda a: d[a][cle])
    return {"min": pct(d[a_min][cle]), "max": pct(d[a_max][cle]), "an_min": str(a_min), "an_max": str(a_max),
            "premier": str(min(d)), "dernier": str(max(d))}


def table(colonnes: list[str], lignes_: list[list[str]]) -> str:
    """Tableau markdown : première colonne à gauche, les autres alignées à droite."""
    out = ["| " + " | ".join(colonnes) + " |", "|---|" + "--:|" * (len(colonnes) - 1)]
    out += ["| " + " | ".join(l) + " |" for l in lignes_]
    return "\n".join(out)


def terme(poste: str) -> str:
    """« Rémunération des salariés (D.1) » : terme de l'INS suivi du code de l'opération."""
    p = registre()[poste]
    return f"{libelles().get(p['operation'], p['operation'])} ({p['code_scn']})"
