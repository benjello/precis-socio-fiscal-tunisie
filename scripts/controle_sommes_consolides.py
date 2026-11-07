"""Contrôle de cohérence (règles de somme) des comptes CONSOLIDÉS des groupes publics cotés, sur tous les
exercices disponibles en local.

Règle reine, universelle et indépendante de l'unité : le bilan s'équilibre, soit
    total de l'actif (net) = total des capitaux propres et passifs.
On relève aussi le total des capitaux propres consolidés (et on signale s'il est négatif).

Une somme qui boucle prouve que les chiffres sont bien recopiés, PAS que les comptes sont sincères (c'est
le travail des commissaires aux comptes) ni que l'entreprise est saine : Tunisair boucle avec des fonds
propres de ‑1,7 Md DT.

    uv run python scripts/controle_sommes_consolides.py           # écrit le rapport et le relevé
    uv run python scripts/controle_sommes_consolides.py --check   # échoue si un bilan lu ne s'équilibre pas

Les PDF (hors git) : tunisia-data/data/raw/entreprises-publiques/bvmt-etats-financiers/<entité>/<année>_consolide.pdf
Sorties : docs/exemples-soes/controle-sommes-consolides.md et .csv
"""

from __future__ import annotations

import csv
import os
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DONNEES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques/bvmt-etats-financiers"
)
SORTIE = RACINE / "docs/exemples-soes"

NOMS = {
    "stb": "STB", "bna": "BNA", "bh-bank": "BH", "bte-adp": "BTE",
    "star": "STAR", "tunisair": "Tunisair",
}

ACTIF = re.compile(r"total\s+(?:de\s+l['’]\s*|des\s+)?actifs?\b(?!\s+[A-Za-zÀ-ÿ])", re.I)
# Grand total du passif : « capitaux propres » ET « passif » sur la même ligne, dans un ordre ou l'autre
# (« … capitaux propres et passifs », « total passif & capitaux propres »…). Les sous-totaux « Total
# Passif » seul ou « passifs éventuels » n'ont pas les deux termes et sont donc écartés.
CP_PASSIFS = re.compile(
    r"total\b[^\n]*?(?:capitaux\s+propres[^\n]*?passif|passif[^\n]*?capitaux\s+propres)", re.I)
CP = re.compile(r"total\s+(?:des\s+)?capitaux\s+propres(?:\s+consolid\w*)?\b(?!\s+et\s+(?:du\s+)?passif)", re.I)


def texte(chemin: Path) -> str:
    try:
        return subprocess.run(
            ["pdftotext", "-layout", str(chemin), "-"], capture_output=True, text=True, check=True
        ).stdout
    except subprocess.CalledProcessError:
        return ""


def entier(jeton: str) -> int | None:
    s = re.sub(r"[\u2010\u2011\u2012\u2013\u2014\u2212]", "-", jeton.strip()).replace("\u00a0", " ")
    negatif = (s.startswith("(") and s.endswith(")")) or s.lstrip().startswith("-")
    s = re.sub(r"[()\-\s]", "", s)
    if not s.isdigit():
        return None
    return -int(s) if negatif else int(s)


def nombres(contenu: str, motif: re.Pattern) -> list[int]:
    """Nombres de colonne de la PREMIÈRE ligne dont le libellé correspond à `motif`."""
    for ligne in contenu.splitlines():
        trouve = motif.search(ligne)
        if not trouve:
            continue
        reste = ligne[trouve.end():]
        vals = [entier(t) for t in re.split(r"\s{2,}", reste.strip())]
        vals = [v for v in vals if v is not None]
        if vals:
            return vals
    return []


def controle(contenu: str) -> dict:
    # Garde-fou : au-delà du vraisemblable (100 milliards), des colonnes ont été collées par un simple
    # espace et le nombre lu est un artefact ; on dit alors « non exploité » plutôt que « déséquilibré ».
    plausible = lambda n: n is not None and 0 < abs(n) < 10**11
    actifs = [a for a in nombres(contenu, ACTIF) if plausible(a)]
    passifs = [p for p in nombres(contenu, CP_PASSIFS) if plausible(p)]
    # un total de capitaux propres se compte en milliers ou millions : on écarte les petits nombres
    # (numéro de note capté par erreur, ex. « 12 ») et les artefacts de colonnes collées.
    cp = [c for c in nombres(contenu, CP) if 1000 <= abs(c) < 10**11]
    equilibre = None
    if actifs and passifs:
        # le total de l'actif NET est celui qui égale le total capitaux propres + passifs (à l'arrondi près)
        equilibre = any(abs(a - passifs[0]) <= 1 for a in actifs)
    return {"actif": actifs[0] if actifs else None,
            "passifs_cp": passifs[0] if passifs else None,
            "capitaux_propres": cp[0] if cp else None,
            "equilibre": equilibre}


def documents() -> list[tuple[str, int, Path]]:
    """(entité, exercice, chemin) pour chaque PDF consolidé, du plus récent au plus ancien."""
    docs = []
    for dossier in sorted(DONNEES.glob("*")):
        if not dossier.is_dir():
            continue
        for pdf in dossier.glob("*consolide*.pdf"):
            an = re.search(r"(20\d{2})", pdf.name)
            if an:
                docs.append((dossier.name, int(an.group(1)), pdf))
    return sorted(docs, key=lambda d: (NOMS.get(d[0], d[0]), -d[1]))


def mdt(n: int | None) -> str:
    return "—" if n is None else f"{n:,}".replace(",", " ")


def rapport(releve: list[dict]) -> str:
    par_entite: dict[str, list[dict]] = {}
    for r in releve:
        par_entite.setdefault(r["entite"], []).append(r)
    lus = [r for r in releve if r["equilibre"] is not None]
    ok = [r for r in lus if r["equilibre"]]
    L = [f"# Les comptes consolidés des groupes publics bouclent-ils ?", "",
         "Contrôle produit par `scripts/controle_sommes_consolides.py` (rien saisi : tout est lu aux PDF "
         "des états financiers consolidés, hors git). Règle vérifiée pour chaque exercice disponible : "
         "**total de l'actif (net) = total des capitaux propres et passifs**. Une somme qui boucle prouve "
         "la recopie, non la santé : Tunisair boucle avec des fonds propres très négatifs.", "",
         f"**{len(ok)} bilans sur {len(lus)} lus s'équilibrent** "
         f"({len(releve) - len(lus)} exercice(s) non exploitable(s) : PDF image ou tronqué).", ""]
    for entite in sorted(par_entite):
        rs = sorted(par_entite[entite], key=lambda r: -r["exercice"])
        annees = ", ".join(str(r["exercice"]) for r in rs)
        L += [f"## {entite}", "",
              "| Exercice | Total actif | Capitaux propres et passifs | Capitaux propres consolidés | Équilibré ? |",
              "|---|---:|---:|---:|:--:|"]
        for r in rs:
            cp = r["capitaux_propres"]
            cp_txt = mdt(cp) + (" ⚠️ négatifs" if cp is not None and cp < 0 else "")
            eq = "—" if r["equilibre"] is None else ("✅" if r["equilibre"] else "❌")
            L.append(f"| {r['exercice']} | {mdt(r['actif'])} | {mdt(r['passifs_cp'])} | {cp_txt} | {eq} |")
        negatifs = [r["exercice"] for r in rs if r["capitaux_propres"] is not None and r["capitaux_propres"] < 0]
        L += ["", f"Exercices lus : {annees}."
              + (f" Fonds propres consolidés **négatifs** en {', '.join(map(str, sorted(negatifs)))}." if negatifs else ""), ""]
    L += ["## Ce qu'on en retient", "",
          "La règle de somme est un contrôle de **recopie**, pas de sincérité ni de santé financière. Elle "
          "détecte une ligne mal lue (une somme casse), et c'est tout. Les fonds propres négatifs qu'elle "
          "laisse voir (Tunisair, et selon les exercices BTE) sont des faits de gestion, pas des erreurs.", ""]
    return "\n".join(L)


def main(arguments: list[str]) -> int:
    verifier = "--check" in arguments
    SORTIE.mkdir(parents=True, exist_ok=True)
    releve, casse = [], 0
    for entite_dir, exercice, pdf in documents():
        contenu = texte(pdf)
        r = controle(contenu) if contenu.strip() else {"actif": None, "passifs_cp": None,
                                                        "capitaux_propres": None, "equilibre": None}
        r.update({"entite": NOMS.get(entite_dir, entite_dir), "exercice": exercice, "fichier": pdf.name})
        releve.append(r)
        if r["equilibre"] is False:
            casse += 1
            print(f"{r['entite']} {exercice} — BILAN DÉSÉQUILIBRÉ : actif {r['actif']} ≠ passifs+CP {r['passifs_cp']}",
                  file=sys.stderr)
    if not verifier:
        (SORTIE / "controle-sommes-consolides.md").write_text(rapport(releve), encoding="utf-8")
        with (SORTIE / "controle-sommes-consolides.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["entite", "exercice", "actif", "passifs_cp",
                                              "capitaux_propres", "equilibre", "fichier"])
            w.writeheader()
            for r in releve:
                w.writerow({k: r.get(k) for k in w.fieldnames})
        lus = sum(1 for r in releve if r["equilibre"] is not None)
        ok = sum(1 for r in releve if r["equilibre"])
        print(f"{ok}/{lus} bilans équilibrés sur {len(releve)} exercices ({len(releve) - lus} non exploitables).")
    return 1 if casse else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
