"""Liste les fichiers français dont la traduction arabe a pris du retard.

    python scripts/traduction_en_retard.py          # la liste, séparée par des espaces
    python scripts/traduction_en_retard.py --detail # une ligne par fichier, avec les dates

SANS RÉSEAU NI CLÉ. C'est tout l'intérêt : décider s'il faut appeler le traducteur ne
doit rien coûter. Le passage hebdomadaire de `translation-sync.yml` s'en sert pour
sortir à zéro appel quand l'arabe est à jour.

LE CRITÈRE. Un fichier est en retard si son dernier commit est PLUS RÉCENT que celui de
son homologue arabe. C'est la définition littérale de « l'arabe n'a pas suivi ».

Pourquoi pas le contrôle de parité, qui existe déjà et ne coûte rien non plus : il
vérifie les ancres, les étiquettes de figures et les clés de citation. Un paragraphe
français ajouté sans nouvelle étiquette lui est invisible — or c'est le cas le plus
fréquent. Il attrape les régressions, pas le retard. Les deux se complètent.

CE QUE LE CRITÈRE NE VOIT PAS, et qu'il faut savoir :

  - une correction faite à la main sur l'arabe seul le rajeunit, et masque donc un
    retard réel du français antérieur à elle. Le cas est rare et sans gravité : la
    passe de traduction repart de toute façon de la traduction existante ;
  - un commit qui touche les deux langues d'un coup — ce que produit précisément une
    PR de traduction fusionnée — laisse les deux dates égales, donc « à jour ». C'est
    correct.

Les `_glossaire.qmd` sont écartés : ils sont engendrés par `build_glossary.py` depuis
`precis/glossaire.yml`, qui porte déjà les deux langues. Les traduire écraserait la
source unique.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def _horodatage(chemin: Path) -> int | None:
    """Date du dernier commit touchant ce fichier, en secondes. None s'il n'en a pas."""
    r = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", str(chemin.relative_to(RACINE))],
        cwd=RACINE, capture_output=True, text=True,
    )
    sortie = r.stdout.strip()
    return int(sortie) if sortie else None


def en_retard() -> list[tuple[Path, int | None, int | None]]:
    """[(fichier FR, date FR, date AR)] pour les seuls fichiers dont l'arabe a décroché."""
    base = RACINE / "precis" / "fr"
    retard = []
    for fr in sorted(base.rglob("*.qmd")):
        if fr.name.startswith("_glossaire"):
            continue
        ar = Path(str(fr).replace("/precis/fr/", "/precis/ar/"))
        d_fr = _horodatage(fr)
        if d_fr is None:
            continue
        if not ar.exists():
            # Jamais traduit : c'est le retard maximal.
            retard.append((fr, d_fr, None))
            continue
        d_ar = _horodatage(ar)
        if d_ar is None or d_fr > d_ar:
            retard.append((fr, d_fr, d_ar))
    return retard


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--detail", action="store_true",
                    help="une ligne par fichier, avec les dates, au lieu de la liste")
    args = ap.parse_args()

    retard = en_retard()
    if args.detail:
        if not retard:
            print("L'arabe est à jour : aucun fichier en retard.")
            return 0
        from datetime import datetime, timezone
        def quand(d):
            return datetime.fromtimestamp(d, timezone.utc).strftime("%Y-%m-%d") if d else "jamais"
        print(f"{len(retard)} fichier(s) dont la traduction a pris du retard :")
        for fr, d_fr, d_ar in retard:
            rel = fr.relative_to(RACINE)
            print(f"  {rel}\n      français {quand(d_fr)}  >  arabe {quand(d_ar)}")
        return 0

    # Sortie brute, faite pour être injectée dans une commande.
    print(" ".join(str(fr.relative_to(RACINE)) for fr in (f for f, _, _ in retard)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
