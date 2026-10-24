"""Contrôle de la série `pnafn-montants-etudes` : chaque valeur contre son texte.

Deux contrôles :
  - interne (toujours) : la valeur de chaque ligne se retrouve, au format français, dans sa
    citation ; la famille et la source sont connues ; la source est une clé de la
    bibliographie du livre ;
  - externe (si les PDF sont rangés dans `tunisia-data/data/raw/`, ou `--raw`) : la
    citation se retrouve mot pour mot, aux espaces près, dans la couche texte du PDF.
    Les lignes de presse n'ont pas de PDF : elles ne sont contrôlées qu'en interne.

Usage : uv run python scripts/verifier_pnafn_montants_etudes.py [--raw CHEMIN]
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
SERIE = RACINE / "precis" / "_seriescache" / "pnafn-montants-etudes.csv"
BIBLIO = RACINE / "precis" / "fr" / "prestations_sociales" / "references.json"
PDF = {
    "mas-bm-ciblage-2021": "banque-mondiale-rapports/mas_bm_2021_identification_menages_pauvres_ciblage.pdf",
    "bad-2013-subventions-aides-directes": "banque-mondiale-rapports/bad_2013_subventions_alimentaires_aides_sociales_directes_draft.pdf",
    "unicef-2019-garantie-allocation-enfants": "banque-mondiale-rapports/unicef_2019_garantie_allocation_enfants_tunisie.pdf",
}
FAMILLES = {"ciblage-2021", "bad-cres-2013", "unicef-2019", "presse-2018"}


def fr(valeur: float) -> str:
    texte = f"{valeur:g}"
    return texte.replace(".", ",")


def _normalise(texte: str) -> str:
    return re.sub(r"\s+", " ", texte.replace(" ", " "))


def lignes() -> list[dict]:
    with SERIE.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def controle_interne() -> list[str]:
    cles = {e["id"] for e in json.loads(BIBLIO.read_text(encoding="utf-8"))["items"]}
    erreurs = []
    for i, r in enumerate(lignes(), start=2):
        if r["famille"] not in FAMILLES:
            erreurs.append(f"ligne {i} : famille inconnue {r['famille']!r}")
        if r["source"] not in cles:
            erreurs.append(f"ligne {i} : source absente de la bibliographie {r['source']!r}")
        if fr(float(r["valeur"])) not in r["citation"]:
            erreurs.append(f"ligne {i} : valeur {r['valeur']} absente de la citation")
    return erreurs


def controle_externe(raw: Path) -> tuple[list[str], int]:
    erreurs, verifiees = [], 0
    textes: dict[str, list[str]] = {}
    for i, r in enumerate(lignes(), start=2):
        chemin = PDF.get(r["source"])
        if chemin is None:
            continue
        pdf = raw / chemin
        if not pdf.exists():
            continue
        if r["source"] not in textes:
            # Deux ordres de lecture : colonnes à plat (mise en page) et flux du PDF. Une
            # citation sur deux colonnes ne se lit que dans le second.
            sorties = [subprocess.run(["pdftotext", *opt, str(pdf), "-"], check=True,
                                      capture_output=True, text=True).stdout
                       for opt in (["-layout"], [])]
            textes[r["source"]] = [_normalise(x) for x in sorties]
        # La citation est entre guillemets français ; on enlève les guillemets et les « … ».
        citation = _normalise(r["citation"].strip("« »"))
        morceaux = [m for m in re.split(r"…", citation) if m.strip()]
        verifiees += 1
        for m in morceaux:
            if not any(m.strip() in t for t in textes[r["source"]]):
                erreurs.append(f"ligne {i} : citation absente du PDF : {m.strip()!r}")
    return erreurs, verifiees


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path.home() / "projets/tunisia-data/data/raw")
    args = ap.parse_args(argv)
    erreurs = controle_interne()
    externe, n = controle_externe(args.raw)
    erreurs += externe
    for e in erreurs:
        print("✗", e)
    print(f"{len(lignes())} ligne(s) ; contrôle externe de {n} ligne(s) ; "
          f"{len(erreurs)} erreur(s).")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
