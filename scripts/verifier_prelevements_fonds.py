"""Contrôle de la série `log-prelevements-fonds` (figure des prélèvements sur le fonds de
promotion du logement pour les salariés).

Contrôles internes (toujours) : les statuts, une ligne au moins par année de 1987 à 2026, la
valeur zéro des années lues sans prélèvement, des clés qui existent dans la bibliographie du
livre, la somme des bénéficiaires d'une année égale au montant de l'année.

Contrôles externes (si le miroir de l'IORT et le corpus des JORT sont là, ou `--corpus`) :
  - pour chaque année `aucun`, le texte des lois de finances lues (miroir ou couche texte du
    fascicule) ne contient aucune mention du fonds près d'un mot de prélèvement, de transfert
    ou de reversement ;
  - pour chaque prélèvement ou transfert global, le montant de la ligne se retrouve, écrit à la
    française, dans le texte de sa loi.
Les années lues à l'image (1987-1994, OCR) et dans l'édition arabe (2023-2025) ne sont contrôlées
qu'en interne : leurs fascicules ne sont pas ici en texte.

Usage : uv run python scripts/verifier_prelevements_fonds.py [--corpus CHEMIN]
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
SERIE = RACINE / "precis" / "_seriescache" / "log-prelevements-fonds.csv"
BIBLIOS = [RACINE / "precis" / "fr" / "references.json",
           RACINE / "precis" / "fr" / "prestations_sociales" / "references.json"]
CORPUS = Path.home() / "projets" / "PDFs-legislation-tunisie"
STATUTS = {"prelevement", "aucun", "transfert_global"}

# clé de citation -> ("md", fichier du miroir) ou ("pdf", fascicule français, pages de texte)
TEXTES = {
    "lf-1995": ("pdf", "1994/fr/Jo10394", 12), "lf-1996": ("pdf", "1995/fr/Jo10495", 10),
    "lf-1997": ("pdf", "1996/fr/Jo10596", 9), "lf-1998": ("pdf", "1997/fr/Jo10497", 12),
    "lf-1999": ("pdf", "1998/fr/Jo10498", 13), "lf-2000": ("pdf", "1999/fr/Jo10599", 15),
    "lf-2001": ("md", "loi_2000_98_2000"), "lf-2003": ("md", "loi_2002_101_2002"),
    "lf-2005": ("md", "loi_2004_90_2004"), "lfc-2005": ("pdf", "2005/fr/Jo1002005", 400),
    "lf-2006": ("md", "loi_2005_106_2005"), "lf-2009": ("md", "loi_2008_77_2008"),
    "lfc-2009": ("md", "loi_2009_40_2009"), "lf-2010": ("md", "loi_2009_71_2009"),
    "lf-2014": ("md", "loi_2013_54_2013"), "lfc-2014": ("md", "loi_2014_54_2014"),
    "lf-2015": ("md", "loi_2014_59_2014"), "lfc-2015": ("md", "loi_2015_30_2015"),
    "lf-2016": ("md", "loi_2015_53_2015"), "lfc-2016": ("md", "loi_2017_1_2017"),
    "lf-2017": ("md", "loi_2016_78_2016"), "lfc-2017": ("md", "loi_2017_63_2017"),
    "lf-2018": ("md", "loi_2017_66_2017"), "lfc-2018": ("md", "loi_2018_55_2018"),
    "loi2018-56-lf2019": ("md", "loi_2018_56_2018"), "lfc-2019": ("md", "loi_2019_77_2019"),
    "lf-2020": ("md", "loi_2019_78_2019"), "lf-2021": ("md", "loi_2020_46_2020"),
    "lfr-2021": ("md", "dec_loi_2021_3_2021"), "dl2021-21-lf2022": ("md", "dec_loi_2021_21_2021"),
    "lfr-2022": ("md", "dec_loi_2022_69_2022"), "lfc-2023": ("pdf", "2023/fr/Jo1362023", 400),
    "lf-2026": ("md", "loi_2025_17_2025"),
    "lfc-2002": ("md", "loi_2002_100_2002"), "lfc-2004": ("md", "loi_2004_87_2004"),
    "lfc-2007": ("md", "loi_2007_64_2007"), "lfc-2008": ("md", "loi_2008_76_2008"),
    "lfc-2013": ("md", "loi_2013_51_2013"), "lfc-2012": ("md", "loi_2012_1_2012"),
    "lf-2013": ("md", "loi_2012_27_2012"),
}
NOM = re.compile(r"logements? pour les salari|promotion du logement|promotion des logements|FOPROLOS",
                 re.I)
ACTE = re.compile(r"pr[eé]l[eè]v|transf[eé]r|revien|vers[eé]", re.I)


def lignes() -> list[dict]:
    with SERIE.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def cles_biblio() -> set[str]:
    return {e["id"] for p in BIBLIOS for e in json.loads(p.read_text(encoding="utf-8"))["items"]}


def controle_interne() -> list[str]:
    erreurs = []
    cles = cles_biblio()
    par_annee: dict[int, list[dict]] = {}
    for i, r in enumerate(lignes(), start=2):
        a = int(r["annee"])
        par_annee.setdefault(a, []).append(r)
        if r["statut"] not in STATUTS:
            erreurs.append(f"ligne {i} : statut inconnu {r['statut']!r}")
        for cle in r["source"].split(";"):
            if cle not in cles:
                erreurs.append(f"ligne {i} : clé absente de la bibliographie : {cle!r}")
        if r["statut"] == "aucun" and (float(r["part_MD"]) != 0 or float(r["montant_MD"]) != 0):
            erreurs.append(f"ligne {i} : une année sans prélèvement vaut zéro")
        if r["statut"] == "transfert_global" and r["part_MD"]:
            erreurs.append(f"ligne {i} : un transfert global n'a pas de part du fonds")
    for a in range(1987, 2027):
        if a not in par_annee:
            erreurs.append(f"{a} : année absente de la série (non lue : à dire, non à omettre)")
    for a, rs in par_annee.items():
        pre = [r for r in rs if r["statut"] == "prelevement"]
        if pre and any(r["statut"] == "aucun" for r in rs):
            erreurs.append(f"{a} : à la fois un prélèvement et « aucun prélèvement »")
        if pre and abs(sum(float(r["part_MD"]) for r in pre) - float(pre[0]["montant_MD"])) > 1e-9 \
                and a != 2011:
            erreurs.append(f"{a} : les bénéficiaires ne somment pas au montant")
        if a == 2011 and abs(sum(float(r["part_MD"]) for r in pre) - 40) > 1e-9:
            erreurs.append("2011 : les deux bénéficiaires doivent sommer à 40 MD")
    return erreurs


def _texte(spec, corpus: Path) -> str | None:
    if spec[0] == "md":
        f = corpus / "data" / "iort" / "textes" / "md" / f"{spec[1]}.md"
        if not f.exists():
            return None
        t = f.read_text(encoding="utf-8")
        return re.sub(r"\s+", " ", t[:t.find("## النسخة العربية")] if "## النسخة العربية" in t else t)
    f = corpus / "PDFs" / "JORT" / f"{spec[1]}.pdf"
    if not f.exists():
        return None
    sortie = subprocess.run(["pdftotext", "-layout", str(f), "-"], check=True,
                            capture_output=True, text=True).stdout
    pages = [p for p in sortie.split("\f")[:spec[2]] if len(p) > 1500]
    return re.sub(r"\s+", " ", " ".join(pages))


def _francais(valeur: float) -> list[str]:
    """Le montant en dinars écrit comme les lois l'écrivent : 29.000.000, 29 000 000."""
    n = round(valeur * 1_000_000)
    s = f"{n:,}"
    return [s.replace(",", "."), s.replace(",", " "), s.replace(",", " ")]


def controle_externe(corpus: Path) -> tuple[list[str], int]:
    erreurs, lus = [], 0
    for i, r in enumerate(lignes(), start=2):
        for cle in r["source"].split(";"):
            spec = TEXTES.get(cle)
            if spec is None:
                continue
            t = _texte(spec, corpus)
            if t is None:
                continue
            lus += 1
            if r["statut"] == "aucun":
                for m in NOM.finditer(t):
                    fen = t[max(0, m.start() - 350): m.end() + 350]
                    if "Autoroutes" in fen or "TABLEAU" in fen:
                        continue          # ligne d'un tableau de fonds
                    if ACTE.search(fen):
                        erreurs.append(f"ligne {i} ({r['annee']}, {cle}) : le fonds près d'un mot "
                                       f"de prélèvement : {fen[250:520]!r}")
            else:
                if not any(x in t for x in _francais(float(r["montant_MD"]))):
                    erreurs.append(f"ligne {i} ({r['annee']}, {cle}) : montant {r['montant_MD']} "
                                   f"introuvable dans le texte")
    return erreurs, lus


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=Path, default=CORPUS)
    args = ap.parse_args(argv)
    erreurs = controle_interne()
    externe, lus = controle_externe(args.corpus)
    for e in erreurs + externe:
        print("✗", e)
    print(f"{len(lignes())} ligne(s) ; {lus} lecture(s) de texte au contrôle externe ; "
          f"{len(erreurs) + len(externe)} erreur(s).")
    return 1 if erreurs or externe else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
