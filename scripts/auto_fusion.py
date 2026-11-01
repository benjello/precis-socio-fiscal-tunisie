"""Active l'auto-fusion d'une PR de traduction, si et seulement si elle est sans risque.

    uv run python scripts/auto_fusion.py --pr 123 --parite success --rendu success --verification success

Appelé par `translation-sync.yml` en fin de passage, avec les ISSUES des étapes de contrôle du
même job. C'est là que ces résultats sont connus : une PR ouverte avec le `GITHUB_TOKEN`
ne déclenche aucun workflow (`rendre-les-livres.yml`, `verify-translation.yml` n'y tournent
jamais). Les mêmes contrôles sont donc rejoués par le job qui produit la PR : parité
déterministe (`check_translation_parity.py`, contre l'état antérieur), rendu des livres arabes
touchés, vérification de la traduction.

UNE PR EST ÉLIGIBLE SI :
  - son auteur est le robot (`github-actions`) et sa branche commence par `auto-translate/` ;
  - elle n'est pas un brouillon ;
  - tous ses fichiers (lus sur la PR, pas sur le disque) sont sous `precis/ar/` ou sont
    `translation_glossary.generated.md` : aucun script, aucun workflow, aucun texte français ;
  - la parité, le rendu et la vérification ont RÉUSSI (une étape sautée ne vaut pas succès :
    la vérification est sautée quand la limite de dépense est atteinte).

Sinon la PR reste ouverte, un commentaire en dit la raison, et l'issue d'état la liste.

L'éligibilité est une fonction pure (`eligible`), testée sans réseau. La fusion elle-même est
`gh pr merge --auto --merge` : GitHub fusionne dès que les contrôles OBLIGATOIRES de la branche
`master` sont verts. Si la PR est déjà prête (aucun contrôle en attente), GitHub refuse
`--auto` (« clean status ») et on fusionne alors directement.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

AUTEURS_ROBOT = {"github-actions[bot]", "github-actions", "app/github-actions"}
PREFIXE_BRANCHE = "auto-translate/"
PREFIXES_PERMIS = ("precis/ar/",)
FICHIERS_PERMIS = {"translation_glossary.generated.md"}
REUSSI = "success"


def fichier_permis(chemin: str) -> bool:
    return chemin in FICHIERS_PERMIS or chemin.startswith(PREFIXES_PERMIS)


def eligible(auteur: str, branche: str, fichiers: list[str], *, parite: str, rendu: str,
             verification: str, brouillon: bool = False) -> tuple[bool, list[str]]:
    """(éligible, raisons du refus). Fonction pure."""
    raisons = []
    if auteur not in AUTEURS_ROBOT:
        raisons.append(f"auteur « {auteur} » : seul le robot de traduction est admis")
    if not branche.startswith(PREFIXE_BRANCHE):
        raisons.append(f"branche « {branche} » : pas une branche {PREFIXE_BRANCHE}*")
    if brouillon:
        raisons.append("PR en brouillon")
    if not fichiers:
        raisons.append("aucun fichier modifié")
    hors = [f for f in fichiers if not fichier_permis(f)]
    if hors:
        raisons.append("fichiers hors de precis/ar/ : " + ", ".join(sorted(hors)[:5])
                       + (" …" if len(hors) > 5 else ""))
    for nom, valeur in (("parité FR/AR", parite), ("rendu du livre arabe", rendu),
                        ("vérification de la traduction", verification)):
        if valeur != REUSSI:
            raisons.append(f"{nom} : {valeur or 'inconnu'} (réussite requise)")
    return (not raisons), raisons


def _gh(*args: str) -> str:
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout).strip())
    return r.stdout


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pr", required=True)
    ap.add_argument("--parite", default="")
    ap.add_argument("--rendu", default="")
    ap.add_argument("--verification", default="")
    args = ap.parse_args()

    info = json.loads(_gh("pr", "view", args.pr, "--json",
                          "author,headRefName,files,isDraft"))
    ok, raisons = eligible(info["author"]["login"], info["headRefName"],
                           [f["path"] for f in info["files"]],
                           parite=args.parite, rendu=args.rendu,
                           verification=args.verification, brouillon=info["isDraft"])
    if not ok:
        corps = ("Non fusionnée automatiquement ; relecture humaine requise.\n\n"
                 + "\n".join(f"- {r}" for r in raisons))
        print(corps)
        try:
            _gh("pr", "comment", args.pr, "-b", corps)
        except RuntimeError as e:
            print(f"Commentaire non posté : {e}")
        return 0
    try:
        _gh("pr", "merge", args.pr, "--auto", "--merge")
        print(f"Auto-fusion activée sur #{args.pr}.")
    except RuntimeError as e:
        msg = str(e)
        if "clean status" in msg.lower():
            _gh("pr", "merge", args.pr, "--merge")
            print(f"#{args.pr} prête : fusionnée directement.")
        else:
            # Réglage de dépôt manquant (« Allow auto-merge ») ou refus : la PR reste ouverte.
            print(f"Auto-fusion impossible sur #{args.pr} : {msg}")
            try:
                _gh("pr", "comment", args.pr, "-b",
                    "Éligible à la fusion automatique, mais GitHub l'a refusée : "
                    f"`{msg[:200]}`. Vérifier le réglage « Allow auto-merge » du dépôt.")
            except RuntimeError:
                pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
