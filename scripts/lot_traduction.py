"""Choisit le prochain lot de fichiers à traduire : un livre, borné, priorisé.

    uv run python scripts/lot_traduction.py --dry-run               # décrit le lot, sans réseau
    uv run python scripts/lot_traduction.py --depuis-issue --liste  # liste brute, pour le workflow

Sans réseau ni clé en `--dry-run`. Avec `--depuis-issue`, lit par `gh` l'issue d'état (budget
appris, consommation du mois) et les PR de traduction ouvertes ; sans cela, il part des valeurs
initiales de `etat_traduction.py`.

LE RAISONNEMENT EST MENSUEL. Le palier gratuit plafonne par mois, pour un montant inconnu que
`etat_traduction.py` apprend. On ne dépense, par passage planifié, qu'une fraction du budget
estimé (`FRACTION_PASSAGE`), et jamais au-delà de `PART_PLANIFIEE` du budget du mois : le reste
est la marge des traductions déclenchées par les fusions sur `master`.

UN LIVRE À LA FOIS, dans cet ordre : les livres dont la structure a changé récemment
(`PRIORITE`), puis les autres livres déjà traduits en partie, puis les livres jamais traduits,
puis les pages générales. Dans un livre : d'abord les fichiers qui ont une ancienne traduction
(un arabe périmé vaut moins qu'un relais honnête), puis les autres.

REPRISE. Le retard se recalcule par dates de commit : le lundi suivant reprend où l'on s'est
arrêté, sans état à porter. Les fichiers déjà couverts par une PR de traduction ouverte sont
écartés, pour ne pas payer deux fois ce que personne n'a encore fusionné.

SONDE. Si la limite a été atteinte ce mois-ci, le lot se réduit à UN fichier, le plus petit :
on ne sait pas quand le palier se renouvelle, et un appel réussi lève la suspension d'ici
sans geste humain.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import etat_traduction as et  # noqa: E402

# Livres dont la structure a changé récemment (backlog) : traités en premier.
PRIORITE = ["prestations_sociales", "fiscalite", "finances_locales"]
MAX_FICHIERS = 8
# Part du budget estimé qu'un seul passage peut dépenser.
FRACTION_PASSAGE = 0.35


def rang_du_livre(livre: str, items: list[dict]) -> tuple[int, int, str]:
    if livre in PRIORITE:
        return (0, PRIORITE.index(livre), livre)
    if livre == "(racine)":
        return (3, 0, livre)
    if any(not i["jamais"] for i in items):
        return (1, 0, livre)
    return (2, 0, livre)


def ordre_des_livres(retard: list[dict]) -> list[str]:
    livres = et.par_livre(retard)
    return sorted(livres, key=lambda l: rang_du_livre(l, livres[l]))


def ordre_des_fichiers(items: list[dict]) -> list[dict]:
    """Périmés d'abord, `index.qmd` en tête de chaque groupe, puis ordre alphabétique."""
    def cle(i):
        return (i["jamais"], not i["fichier"].endswith("/index.qmd"), i["fichier"])
    return sorted(items, key=cle)


def choisir_lot(retard: list[dict], *, budget: int, consommation: int,
                max_fichiers: int = MAX_FICHIERS, max_caracteres: int = 0,
                exclus: set[str] | frozenset[str] = frozenset(), livre: str | None = None,
                limite_atteinte: bool = False) -> dict:
    """{'livre', 'fichiers': [dict], 'caracteres', 'raison'} ; fichiers vide si rien à faire."""
    restant = int(budget * et.PART_PLANIFIEE) - consommation
    if limite_atteinte:
        plafond = restant = None   # sonde : un fichier, le plus petit
    else:
        plafond = int(budget * FRACTION_PASSAGE)
        if max_caracteres > 0:
            plafond = min(plafond, max_caracteres)
        plafond = min(plafond, restant)
        if restant <= 0:
            return {"livre": None, "fichiers": [], "caracteres": 0,
                    "raison": "budget planifié du mois consommé (le reste est la marge des fusions)"}
    candidats = [r for r in retard if r["fichier"] not in exclus]
    if not candidats:
        return {"livre": None, "fichiers": [], "caracteres": 0,
                "raison": "rien à traduire (retard nul ou déjà couvert par une PR ouverte)"}
    livres = et.par_livre(candidats)
    ordre = [livre] if livre else ordre_des_livres(candidats)
    for nom in ordre:
        items = ordre_des_fichiers(livres.get(nom, []))
        if limite_atteinte:
            if items:
                petit = min(items, key=lambda i: i["caracteres"])
                return {"livre": nom, "fichiers": [petit], "caracteres": petit["caracteres"],
                        "raison": "sonde : limite atteinte ce mois-ci, un seul fichier"}
            continue
        lot, total = [], 0
        for i in items:
            if len(lot) >= max_fichiers:
                break
            if total + i["caracteres"] > plafond:
                continue
            lot.append(i)
            total += i["caracteres"]
        if not lot:
            # Un fichier plus gros que le plafond de passage part seul, s'il tient dans
            # ce qui reste du budget planifié du mois (sinon il attendrait indéfiniment).
            for i in items:
                if i["caracteres"] <= restant:
                    lot, total = [i], i["caracteres"]
                    break
        if lot:
            return {"livre": nom, "fichiers": lot, "caracteres": total, "raison": "lot borné"}
    return {"livre": None, "fichiers": [], "caracteres": 0,
            "raison": "aucun fichier ne tient dans le budget du passage"}


def fichiers_en_pr_ouverte() -> set[str]:
    """Fichiers français dont une PR `auto-translate/*` ouverte porte déjà l'arabe."""
    import subprocess
    r = subprocess.run(["gh", "pr", "list", "--state", "open", "--limit", "100",
                        "--json", "headRefName,files"], capture_output=True, text=True)
    if r.returncode != 0:
        return set()
    sortie = set()
    for pr in json.loads(r.stdout or "[]"):
        if not pr["headRefName"].startswith("auto-translate/"):
            continue
        for f in pr.get("files", []):
            chemin = f.get("path", "")
            if chemin.startswith("precis/ar/"):
                sortie.add(chemin.replace("precis/ar/", "precis/fr/", 1))
    return sortie


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="décrit le lot, sans rien traduire")
    ap.add_argument("--liste", action="store_true", help="fichiers séparés par des espaces")
    ap.add_argument("--depuis-issue", action="store_true",
                    help="lire l'issue d'état et les PR ouvertes (gh) ; sinon valeurs initiales")
    ap.add_argument("--corps-precedent", help="fichier : corps de l'issue (hors ligne)")
    ap.add_argument("--livre", help="forcer le livre")
    ap.add_argument("--max-fichiers", type=int, default=MAX_FICHIERS)
    ap.add_argument("--max-caracteres", type=int, default=0, help="0 = selon le budget")
    ap.add_argument("--budget", type=int, default=0, help="forcer le budget mensuel (caractères)")
    args = ap.parse_args()

    maintenant = datetime.now(timezone.utc)
    mois = et.mois_de(maintenant)
    corps = None
    exclus: set[str] = set()
    if args.corps_precedent:
        corps = Path(args.corps_precedent).read_text(encoding="utf-8")
    elif args.depuis_issue:
        iss = et.issue_courante()
        corps = (iss or {}).get("body")
    if args.depuis_issue:
        exclus = fichiers_en_pr_ouverte()
    donnees = et.lire_donnees(corps)
    hist = donnees["historique"]
    budget = args.budget or et.budget_estime(hist, mois)[0]
    lot = choisir_lot(et.collecter_retard(), budget=budget,
                      consommation=et.consommation(hist, mois),
                      max_fichiers=args.max_fichiers, max_caracteres=args.max_caracteres,
                      exclus=exclus, livre=args.livre,
                      limite_atteinte=bool(hist.get(mois, {}).get("limite_atteinte")))
    fichiers = [f["fichier"] for f in lot["fichiers"]]
    if args.dry_run:
        print(f"Budget mensuel estimé : {et.fmt(budget)} caractères ; consommé : "
              f"{et.fmt(et.consommation(hist, mois))}.")
        print(f"Lot : {lot['livre'] or '(aucun)'} — {lot['raison']}.")
        for f in lot["fichiers"]:
            print(f"  {f['fichier']}  ({et.fmt(f['caracteres'])} caractères"
                  f"{', jamais traduit' if f['jamais'] else ''})")
        if fichiers:
            print(f"Total : {len(fichiers)} fichier(s), {et.fmt(lot['caracteres'])} caractères.")
        return 0
    print(" ".join(fichiers))
    return 0


if __name__ == "__main__":
    sys.exit(main())
