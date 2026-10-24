"""Contrôle de la série `amen-social-allocataires-tableau` contre le tableau du chapitre.

Le tableau « Allocataires de l'aide monétaire permanente, par date et par source »
(`tbl-nc-effectifs`, `_non_contributives.qmd`) est la référence ; la figure, l'onglet Données
et la provenance lisent le CSV versionné. Ce script vérifie, dans les deux sens, que le CSV
donne exactement les valeurs du tableau : mêmes nombres, aux mêmes dates, dans la même
colonne (allocataires du ministère, ménages de la Banque mondiale), et que la clé de chaque
ligne figure dans la colonne « Source » de la ligne du tableau. Il compare aussi les stocks de
décembre du ministère à la série `mas-amen-social-2023-beneficiaires-bruts`.

Usage : uv run python scripts/verifier_effectifs_tableau.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
QMD = RACINE / "precis" / "fr" / "prestations_sociales" / "_non_contributives.qmd"
SERIE = RACINE / "precis" / "_seriescache" / "amen-social-allocataires-tableau.csv"
BRUTS = RACINE / "precis" / "_seriescache" / "mas-amen-social-2023-beneficiaires-bruts.csv"
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
        "octobre", "novembre", "décembre"]


def nombres(cellule: str) -> list[int]:
    """Les nombres écrits « 124 000 » d'une cellule, hors années et hors numéros de page."""
    texte = re.sub(r"\[@[^\]]*\]", " ", cellule)           # citations
    texte = re.sub(r"\ben \d{4}\b", " ", texte)            # « 260 000 en 2020 » : l'année
    return [int(re.sub(r"\s", "", m)) for m in re.findall(r"\d{1,3}(?:[  ]\d{3})+|\d{4,}", texte)]


def lignes_du_tableau() -> list[dict]:
    texte = QMD.read_text(encoding="utf-8")
    fin = texte.index("{#tbl-nc-effectifs")
    debut = texte.rfind("\n\n", 0, texte.rfind("\n\n", 0, fin)) + 2
    bloc = texte[debut:fin].strip().splitlines()
    lignes = []
    for ligne in bloc[2:]:
        if not ligne.startswith("|"):
            continue
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        date = re.sub(r"\{[^}]*\}|[\[\]]", "", c[0]).strip()
        lignes.append({"date": date, "ministere": nombres(c[1]), "menages": nombres(c[2]),
                       "source": c[3]})
    return lignes


def etiquette(date_reference: str) -> tuple[int, int | None]:
    """(année, mois ou None) d'une date du CSV."""
    p = date_reference.split("-")
    return int(p[0]), (int(p[1]) if len(p) > 1 else None)


def etiquette_tableau(date: str) -> tuple[int, int | None]:
    annee = int(re.search(r"\d{4}", date).group())
    mois = next((i + 1 for i, m in enumerate(MOIS) if m in date), None)
    return annee, mois


def controle() -> list[str]:
    erreurs = []
    tableau = lignes_du_tableau()
    with SERIE.open(encoding="utf-8", newline="") as f:
        csv_lignes = list(csv.DictReader(f))
    attendu = {"allocataires_ministere": [], "menages_banque_mondiale": []}
    for r in tableau:
        a, m = etiquette_tableau(r["date"])
        attendu["allocataires_ministere"] += [(a, m, v, r["source"]) for v in r["ministere"]]
        attendu["menages_banque_mondiale"] += [(a, m, v, r["source"]) for v in r["menages"]]
    vus = {k: [] for k in attendu}
    for i, r in enumerate(csv_lignes, start=2):
        a, m = etiquette(r["date_reference"])
        v = int(float(r["valeur"]))
        vus[r["grandeur"]].append((a, m, v))
        # La ligne du tableau : même année, et même mois quand les deux en portent un.
        candidats = [x for x in attendu[r["grandeur"]]
                     if x[0] == a and x[2] == v and (x[1] is None or m is None or x[1] == m
                                                     or r["precision_date"] == "annee")]
        if not candidats:
            erreurs.append(f"ligne {i} : {r['grandeur']} {r['date_reference']} {v} absent du tableau")
        elif not any(r["source"] in x[3] for x in candidats):
            erreurs.append(f"ligne {i} : la clé {r['source']} n'est pas dans la colonne Source de la ligne du tableau")
    for grandeur, lst in attendu.items():
        # Un nombre repris par deux documents n'a qu'une valeur au tableau, deux clés à sa Source.
        csv_set = sorted({(a, v) for a, m, v in vus[grandeur]})
        tab_set = sorted({(a, v) for a, m, v, s in lst})
        if csv_set != tab_set:
            erreurs.append(f"{grandeur} : le CSV et le tableau diffèrent\n  CSV     {csv_set}\n  tableau {tab_set}")
    # Les stocks de décembre se retrouvent dans la série des totaux du ministère.
    with BRUTS.open(encoding="utf-8", newline="") as f:
        bruts = {int(r["annee"]): int(float(r["valeur"])) for r in csv.DictReader(f)
                 if r["indicateur"] == "bénéficiaires du transfert mensuel"
                 and r["dimension"] == "stock décembre"}
    for a, m, v in vus["allocataires_ministere"]:
        if bruts.get(a) != v:
            erreurs.append(f"stock de décembre {a} : {v} au tableau, {bruts.get(a)} dans la série des totaux")
    return erreurs


def main() -> int:
    erreurs = controle()
    for e in erreurs:
        print("✗", e)
    print(f"{len(lignes_du_tableau())} ligne(s) de tableau ; {len(erreurs)} erreur(s).")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
