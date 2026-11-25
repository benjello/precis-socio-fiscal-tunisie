#!/usr/bin/env python3
"""Étendue des séries des postes et nombre de postes chiffrés par année, sur toute la période des séries.

Deux tableaux engendrés depuis le registre `precis/fr/postes-comptables.csv` et le cache des séries :

- `precis/fr/postes-etendue.csv` : pour chaque poste, première et dernière année où sa série a une valeur
  (fenêtre « …|AAAA-AAAA » du registre respectée), nombre d'années chiffrées et liste des plages. Un poste
  sans série a des années vides. L'étendue est celle du poste, non celle de la série entière (colonne
  `annees` du registre) : une colonne peut commencer après la série qui la porte.
- `precis/fr/compte-couverture-postes-annees.csv` : pour chaque année et chaque secteur, postes rattachés
  au secteur (qui verse ou qui reçoit, comme scripts/couverture_comptes.py) et postes chiffrés cette
  année-là. La période va de la première année chiffrée d'un poste de la sécurité sociale (les comptes des
  caisses) à la dernière année que l'INS publie en base 2015. Aucune part du montant n'y figure : elle
  n'existe que pour les années d'un compte des secteurs du cache, base 1997 puis base 2015, chaque année
  dans une seule base (precis/fr/compte-couverture-annees.csv) ; les bases ne sont pas raccordées
  (question M10).

    uv run python scripts/etendue_postes.py            # écrit
    uv run python scripts/etendue_postes.py --verifier # échoue si un des deux fichiers n'est pas à jour
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import couverture_comptes as cc  # noqa: E402
import reconstruire_comptes as rc  # noqa: E402

ETENDUE = rc.FR / "postes-etendue.csv"
PAR_ANNEE = rc.FR / "compte-couverture-postes-annees.csv"
# S13 : réunion des postes des trois sous-secteurs (un poste versé et reçu entre administrations compte une fois).
SECTEURS = {"S13": ("apu_centrale", "apu_locale", "apu_secu"),
            **{code: membres for code, (_, membres) in cc.SECTEURS.items() if code != "S13-consolide"}}


def chiffre(p: dict, annee: int) -> bool:
    """Le poste a une valeur dans sa série cette année-là (le critère de montant_reference)."""
    return bool(p.get("serie")) and rc.montant(p["serie"], p["colonne"], annee)[0] is not None


def etendue(postes: list[dict]) -> list[dict]:
    out = []
    for p in postes:
        ans = rc.annees_chiffrees(p)
        out.append({"poste": p["poste"], "operation": p["operation"], "cote": p["cote"],
                    "secteur_verse": p["secteur_verse"], "secteur_recoit": p["secteur_recoit"],
                    "serie": p["serie"], "colonne": p["colonne"],
                    "premiere_annee": ans[0] if ans else "", "derniere_annee": ans[-1] if ans else "",
                    "annees_chiffrees": len(ans), "plages": rc.liste_annees(ans) if ans else ""})
    return out


def rattache(p: dict, membres: tuple[str, ...]) -> bool:
    return any(s in membres for champ in ("secteur_verse", "secteur_recoit") for s in p[champ].split(";") if s)


def premiere_annee_caisses(lignes_etendue: list[dict]) -> int:
    """Première année chiffrée d'un poste de la sécurité sociale (S1314)."""
    ans = [int(l["premiere_annee"]) for l in lignes_etendue
           if l["premiere_annee"] != "" and rattache(l, ("apu_secu",))]
    return min(ans)


def par_annee(postes: list[dict], annees: range) -> list[dict]:
    out = []
    for y in annees:
        for code, membres in SECTEURS.items():
            du_sec = [p for p in postes if rattache(p, membres)]
            n = sum(1 for p in du_sec if chiffre(p, y))
            out.append({"annee": y, "secteur": code, "postes": len(du_sec), "postes_chiffres": n,
                        "part_postes_chiffres_pct": round(100 * n / len(du_sec), 1) if du_sec else ""})
    return out


def calculer() -> tuple[list[dict], list[dict]]:
    postes = rc.lire_csv(rc.REGISTRE)
    et = etendue(postes)
    secteurs = rc.lire_csv(rc.CACHE / "cnat-secteurs.csv")
    fin = max(rc.annees_base2015(secteurs))
    return et, par_annee(postes, range(premiere_annee_caisses(et), fin + 1))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args(argv)
    sorties = dict(zip((ETENDUE, PAR_ANNEE), calculer()))
    if a.verifier:
        faux = [c.name for c, rows in sorties.items()
                if not c.exists() or rc.lire_csv(c) != [{k: str(v) for k, v in r.items()} for r in rows]]
        for nom in faux:
            print(f"ERREUR : {nom} n'est pas à jour : relancer scripts/etendue_postes.py")
        return 1 if faux else 0
    for chemin, rows in sorties.items():
        with chemin.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    et, pa = sorties[ETENDUE], sorties[PAR_ANNEE]
    print(f"{len(et)} postes, dont {sum(1 for l in et if l['premiere_annee'] != '')} chiffrés au moins une année ; "
          f"postes chiffrés par année : {pa[0]['annee']}-{pa[-1]['annee']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
