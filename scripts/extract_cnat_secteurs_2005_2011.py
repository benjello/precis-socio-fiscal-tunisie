#!/usr/bin/env python3
"""Extrait la sequence des comptes par secteur institutionnel depuis les PDF INS
(comptes de la nation, base 1997), pour etendre `cnat-comptes-secteurs` vers
2001-2011.

Structure des PDF : chaque secteur a une page EMPLOIS puis une page RESSOURCES.
Les soldes (valeur ajoutee, revenu d'exploitation, solde des revenus primaires,
revenu disponible, epargne, capacite/besoin) sont identiques des deux cotes ; les
flux (interets, autres transferts courants, transferts en capital, remuneration,
prestations, FBCF, depense de consommation finale) different.

Convention reproduite d'apres la serie existante (diagnostic empirique
2012-2017) pour que l'extension soit homogene :
  - snf, sf : interets / autres transferts courants / transferts en capital ->
    cote RESSOURCES ; le reste -> EMPLOIS.
  - apu, exterieur : tout -> EMPLOIS (le generateur n'utilise que la table
    emplois de l'APU).
  - menages : compte complet 'COMPTES DES MENAGES (MEN)' (PAS la sous-table
    'entreprises individuelles' que la serie actuelle reprend par collision de
    slug - voir le compte rendu), meme logique de cote que snf/sf.

Modes : --valide (rejoue 2012-2016 + 2013-2017 vs serie) ; --extrait (ecrit le
CSV de travail 2001-2011).
"""
from __future__ import annotations
import csv
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
RAW = Path.home() / "projets/tunisia-data/data/raw/ins-publications/comptes-de-la-nation"
SERIE = RACINE / "precis/_seriescache/cnat-comptes-secteurs.csv"

CIBLES = [
    "valeur ajoutee brute", "remuneration des salaries", "revenu d'exploitation",
    "interets", "solde des revenus primaires / revenu national",
    "prestations sociales en espece", "autres transferts courants",
    "revenu disponible brut", "depense de consommation finale", "epargne brute",
    "formation brute de capitale fixe", "transferts en capital",
    "capacite ou besoin de financement",
]
CIBLES_SET = set(CIBLES)

# cote RESSOURCES pour ces (secteur, indicateur) ; sinon EMPLOIS (defaut).
RESSOURCES = {
    ("snf", "interets"), ("snf", "autres transferts courants"),
    ("snf", "transferts en capital"),
    ("sf", "interets"), ("sf", "autres transferts courants"),
    ("menages", "interets"), ("menages", "autres transferts courants"),
    ("menages", "transferts en capital"),
}

# Editions base 1997 seulement (2001-2005..2004-2008 sont base 1983 : exclues).
# edition -> premiere annee (= annee la plus recente qu'elle couvre).
EDITIONS = {
    "2005-2009": 2005, "2006-2010": 2006, "2007-2011": 2007, "2008-2012": 2008,
    "2009-2013": 2009, "2010-2014": 2010, "2011-2015": 2011,
}

NUMCELL = re.compile(r"^-?\d[\d  \u00a0\u202f]*(?:[.,]\d+)?$")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s).strip().lower()


def norm_ns(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", norm(s))


def pages(pdf: Path):
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                         capture_output=True, text=True).stdout
    return out.split("\f")


def parse_number(tok: str):
    t = (tok.replace("\u202f", "").replace("\u00a0", "").replace(" ", "")
            .replace(",", "."))
    try:
        return float(t)
    except ValueError:
        return None


def header_years(line: str):
    ys = []
    for t in re.split(r"\s{2,}", line.strip()):
        m = re.match(r"^((?:19|20)\d{2})\*{0,2}$", t.strip())
        if m:
            ys.append(int(m.group(1)))
    return ys


def page_role(page: str):
    # premier marqueur emplois/ressources dans l'entete (fenetre large : certaines
    # editions ont un bandeau 'Volume N / Base 1997' avant le titre).
    for ln in page.splitlines()[:12]:
        h = norm_ns(ln)
        if h == "emplois" or h.startswith("emplois"):
            return "emplois"
        if h == "ressources" or h.startswith("ressources"):
            return "ressources"
    head = norm_ns("\n".join(page.splitlines()[:12]))
    if "ressources" in head and "emplois" not in head:
        return "ressources"
    # certaines editions (ex. 2008-2012) n'impriment pas 'EMPLOIS' sur la page
    # des emplois : par defaut une page-compte sans marqueur = emplois.
    return "emplois"


def classify(page: str):
    # on exige le TITRE de compte ('COMPTE(S) DES ...') dans l'entete, pas une
    # simple mention du secteur (qui apparait comme libelle de ligne dans des
    # tableaux d'agregats : 'REVENUS PRIMAIRES', etc.).
    head_ns = norm_ns("\n".join(page.splitlines()[:12]))
    excl_apu = any(x in head_ns for x in ("centrale", "locales", "securitesociale",
                                          "collectivites"))
    excl_men = any(x in head_ns for x in ("entreprisesindividuelles", "individuelles",
                                          "menagespurs", "collectivites"))
    if "comptedesadministrationspubliques" in head_ns and not excl_apu:
        return "apu"
    if "comptesdessocietesnonfinancieres" in head_ns:
        return "snf"
    if "comptesdessocietesfinancieres" in head_ns and "nonfinancieres" not in head_ns:
        return "sf"
    if "comptesdesmenages" in head_ns and not excl_men:
        return "menages"
    if "comptedesoperations" in head_ns and "exterieur" in head_ns:
        return "exterieur"
    return None


def parse_page(page: str):
    lines = page.splitlines()
    years = None
    for ln in lines:
        ys = header_years(ln)
        if len(ys) >= 3:
            years = ys
            break
    if not years:
        return None, {}
    vals = {}
    for ln in lines:
        cells = [c for c in re.split(r"\s{2,}", ln.strip()) if c]
        if len(cells) < 2:
            continue
        label = norm(cells[0])
        # certaines editions tronquent '/ Revenu national' en '/ Revenu'
        if label.startswith("solde des revenus primaires"):
            label = "solde des revenus primaires / revenu national"
        if label not in CIBLES_SET or label in vals:
            continue
        nums = [parse_number(c) for c in cells[1:] if NUMCELL.match(c.strip())]
        nums = [n for n in nums if n is not None]
        vals[label] = nums
    return years, vals


def extract_pdf(pdf: Path):
    """-> {secteur: {'annees':[...], 'emplois':{ind:[vals],page}, 'ressources':...}}"""
    sides = defaultdict(dict)  # secteur -> role -> (page_no, years, vals)
    for i, page in enumerate(pages(pdf), start=1):
        n = norm(page)
        if "millions de dinars" not in n or "evolution en %" in n:
            continue
        sec = classify(page)
        if not sec:
            continue
        role = page_role(page)
        years, vals = parse_page(page)
        if not years or not vals:
            continue
        if role not in sides[sec]:          # 1re page de ce cote
            sides[sec][role] = (i, years, vals)
    return sides


def value_rows(sec, sides, target_years):
    """Applique la convention de cote et renvoie (ind, annee, valeur, page)."""
    out = []
    role_pages = sides.get(sec, {})
    if not role_pages:
        return out
    any_years = next(iter(role_pages.values()))[1]
    for ind in CIBLES:
        want_res = (sec, ind) in RESSOURCES
        order = ["ressources", "emplois"] if want_res else ["emplois", "ressources"]
        chosen = None
        for role in order:
            if role in role_pages:
                pno, years, vals = role_pages[role]
                if ind in vals and len(vals[ind]) == len(years):
                    chosen = (pno, years, vals[ind])
                    break
        if not chosen:
            continue
        pno, years, vlist = chosen
        for y, v in zip(years, vlist):
            if y in target_years:
                out.append((ind, y, round(v, 1), pno))
    return out


def load_serie():
    d = {}
    with SERIE.open() as f:
        for r in csv.DictReader(f):
            if r["base_pib"] != "1997":
                continue
            d[(r["secteur"], r["indicateur"], int(r["annee"]))] = float(r["valeur"])
    return d


def cmd_valide():
    serie = load_serie()
    repro = {}
    for ed, yrs in [("2012-2016", {2012}),
                    ("2013-2017", {2013, 2014, 2015, 2016, 2017})]:
        sides = extract_pdf(RAW / f"{ed}.pdf")
        for sec in ["snf", "sf", "apu", "menages", "exterieur"]:
            for ind, y, v, pno in value_rows(sec, sides, yrs):
                repro[(sec, ind, y)] = (v, ed, pno)

    print("== VALIDATION 2012-2017 (base 1997) : extraction vs serie ==")
    ok = bad = extra = 0
    bads = []
    for key, (v, ed, pno) in sorted(repro.items()):
        sv = serie.get(key)
        if sv is None:
            extra += 1
        elif abs(sv - v) > 0.05:
            bad += 1
            bads.append((key, v, sv, ed, pno))
        else:
            ok += 1
    miss = []
    for key, sv in sorted(serie.items()):
        if key[1] in CIBLES_SET and 2012 <= key[2] <= 2017 and key not in repro:
            miss.append((key, sv))
    print(f"  concordances OK (cellule en serie et extraite, memes valeurs) = {ok}")
    print(f"  ECARTS (valeur differente) = {bad}")
    for key, v, sv, ed, pno in bads:
        print(f"    ECART {key}: extrait {v} vs serie {sv}  [{ed} p{pno}]")
    print(f"  cellules extraites absentes de la serie = {extra} "
          f"(serie lacunaire : extraction lossy d'origine)")
    print(f"  cellules en serie non reproduites = {len(miss)}")
    for key, sv in miss[:40]:
        print(f"    MANQUE {key} = {sv}")


def cmd_extrait():
    rows = []
    rapport = []
    for ed, first_year in EDITIONS.items():
        pdf = RAW / f"{ed}.pdf"
        if not pdf.exists():
            rapport.append(f"[!] absent: {pdf}")
            continue
        sides = extract_pdf(pdf)
        target = {first_year}
        for sec in ["snf", "sf", "apu", "menages", "exterieur"]:
            vr = value_rows(sec, sides, target)
            if not vr:
                rapport.append(f"[{ed}] {sec}: NON TROUVE "
                               f"(pages detectees: {list(sides.get(sec, {}).keys())})")
                continue
            for ind, y, v, pno in vr:
                rows.append({"secteur": sec, "indicateur": ind, "annee": y,
                             "base_pib": 1997, "valeur": v,
                             "edition": f"cnat_{ed}", "source_pdf": f"{ed}.pdf",
                             "page": pno})
    out = RACINE / "docs/notes/cnat-secteurs-2001-2011-extrait.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["secteur", "indicateur", "annee",
                                          "base_pib", "valeur", "edition",
                                          "source_pdf", "page"])
        w.writeheader()
        for r in sorted(rows, key=lambda r: (r["secteur"], r["indicateur"], r["annee"])):
            w.writerow(r)
    print(f"ecrit {len(rows)} lignes -> {out}")
    grid = defaultdict(set)
    for r in rows:
        grid[r["secteur"]].add(r["annee"])
    for sec in ["snf", "sf", "apu", "menages", "exterieur"]:
        print(f"  {sec}: annees {sorted(grid[sec])} ({len(grid[sec])}/11), "
              f"{sum(1 for r in rows if r['secteur']==sec)} lignes")
    for line in rapport:
        print("  " + line)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "--valide"
    {"--valide": cmd_valide, "--extrait": cmd_extrait}.get(mode, cmd_valide)()
