"""Données de la figure « La dépense des communes » : articles d'éducation des budgets communaux.

Lit les fichiers par commune et par article de la DGCT (2022 : exécution définitive ; 2023 :
situation provisoire au 10 janvier 2024) et écrit `figdata/fig_educ_communes.csv`. Les fichiers de
2018 à 2021 s'arrêtent à la section (aucun identifiant d'article) : ils ne permettent pas la série.
Les chunks du chapitre ne lancent PAS ce script : ils lisent le figdata. Pour le relancer :

    uv run --with openpyxl python precis/fr/education/figures/fig_educ_communes_donnees.py [répertoire DGCT]

Répertoire par défaut : ~/projets/tunisia-data/data/raw/finances_locales/dgct_portail (hors git).
"""
import sys
import warnings
from pathlib import Path

import pandas as pd

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "precis/fr/education/figdata"
DATE = "2026-10-23"
FICHE = "docs/notes/education-collectivites-2026-10-23.md"
FICHIERS = {  # année : (dépenses, recettes, colonne dépenses, colonne recettes, stade)
    2022: ("Budget2022_Depenses-1.xlsx", "Budget2022_Recettes-1.xlsx",
           "depenses_realisation", "recettes_realisations", "exécution définitive"),
    2023: ("Data_Depenses_2023_10-01-2024.xlsx", "Data_Recettes_2023_10-01-2024.xlsx",
           "depenses_realisation", "recettes_realisation", "provisoire (10 janvier 2024)"),
}


def lire(chemin):
    brut = pd.read_excel(chemin, header=None)
    i = brut.index[brut.apply(lambda r: r.astype(str).str.contains("Code_Municipalite_INS").any(), axis=1)][0]
    df = brut.iloc[i + 1:].copy()
    df.columns = brut.iloc[i].tolist()
    return df


def md(s):
    return float(pd.to_numeric(s).sum()) / 1e6


def main(rep):
    rep = Path(rep)
    lignes = []
    for annee, (fd, fr, cd, cr, stade) in FICHIERS.items():
        d, r = lire(rep / fd), lire(rep / fr)
        d[cd] = pd.to_numeric(d[cd])
        r[cr] = pd.to_numeric(r[cr])
        t1d = md(d.loc[d["idtitredep"].astype(int) == 1, cd])
        t2d = md(d.loc[d["idtitredep"].astype(int) == 2, cd])
        t1r = md(r.loc[r["idtitrerec"].astype(int) == 1, cr])
        t2r = md(r.loc[r["idtitrerec"].astype(int) == 2, cr])
        a = d[d["idarticledep"].astype(int) == 3303].groupby("Code_Municipalite_INS")[cd].sum()
        b = r[r["idarticlerec"].astype(int) == 4101].groupby("Code_Municipalite_INS")[cr].sum()
        for grandeur, montant, pos, denos in (
            ("Dépenses de l'article 3303, enseignement et formation", md(a), int((a > 0).sum()),
             (("dépenses du titre I", t1d), ("dépenses totales (titres I et II)", t1d + t2d))),
            ("Recettes de l'article 4101, jardins d'enfants", md(b), int((b > 0).sum()),
             (("recettes du titre I", t1r), ("recettes totales (titres I et II)", t1r + t2r))),
        ):
            for nom, den in denos:
                lignes.append({"Année": annee, "Grandeur": grandeur, "Montant (millions D)": round(montant, 3),
                               "Communes à montant positif": pos, "Dénominateur": nom,
                               "Montant du dénominateur (millions D)": round(den, 1),
                               "Part (%)": round(100 * montant / den, 3), "Stade": stade})
    df = pd.DataFrame(lignes)
    cav = ("Fichiers par commune de la DGCT, 350 communes, niveau de l'article disponible pour 2022 et 2023 "
           "seulement ; de 2018 à 2021 les fichiers s'arrêtent à la section. 2022 : exécution définitive ; "
           "2023 : situation provisoire au 10 janvier 2024. Titre I = gestion et intérêts de la dette ; "
           "titre II = développement, remboursement du principal, crédits reportés, comptes de participation. "
           "L'article 3303 additionne quatre paragraphes dont la formation des agents locaux : majorant de "
           "la dépense d'éducation. Aucun article ne porte sur la construction ou l'entretien des écoles")
    head = [f"# Figure-data du précis socio-fiscal tunisien — généré le {DATE}",
            "# séries (tunisia_data) : ", "# sources (citation) : @dgct-donnees-ouvertes",
            f"# fiches : {FICHE}", f"# méthode/hypothèses : {cav}",
            "# note : Articles 3303 (dépenses) et 4101 (recettes) des budgets des communes en parts des dépenses et des recettes, 2022 et 2023"]
    (OUT / "fig_educ_communes.csv").write_text("\n".join(head) + "\n" + df.to_csv(index=False), encoding="utf-8")
    (OUT / "fig_educ_communes.csv.yml").write_text(
        f"series: []\nsources: [dgct-donnees-ouvertes]\nfiches: [{FICHE}]\ncaveats: [{cav}]\ngenerated: {DATE}\n",
        encoding="utf-8")
    print(df.to_string())


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else Path.home() / "projets/tunisia-data/data/raw/finances_locales/dgct_portail")
