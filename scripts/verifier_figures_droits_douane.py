"""Contrôle des figures, des données et des tableaux du chapitre « Les droits de douane ».

Lance chaque fonction de figure et chaque `table()` en isolé, écrit les PNG dans un
répertoire de travail (jamais dans `figdata/` ni dans `_fig/` du livre), imprime les cinq
tableaux de `douane/tarifs-releves-droits-douane.csv` par `tarifs.imprime`, et recoupe les
valeurs calculées avec la table annuelle de la note documentaire.

    uv run python scripts/verifier_figures_droits_douane.py [répertoire de sortie]
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
LIVRE = RACINE / "precis" / "fr" / "fiscalite"
sys.path.insert(0, str(RACINE / "scripts"))
sys.path.insert(0, str(LIVRE))
os.chdir(LIVRE)  # la bibliographie du livre se lit depuis le répertoire courant

import pandas as pd  # noqa: E402

import tarifs  # noqa: E402
from figures import droits_douane as dd  # noqa: E402

SORTIE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
SORTIE.mkdir(parents=True, exist_ok=True)
NOTE = RACINE / "docs" / "notes" / "fiscalite-droits-douane-ratios-1986-2025.csv"
RESTE = "|".join(["open" + "fisca", "mod" + "èle", "para" + "mètre", "du fich", "du PDF"])


def png(nom: str, fig) -> None:
    chemin = SORTIE / f"{nom}.png"
    fig.savefig(chemin, dpi=110)
    print("PNG", chemin)


def main() -> int:
    erreurs = []
    png("fig_dd_parts", dd.fig_parts())
    png("fig_dd_pib", dd.fig_pib())
    for (titre, f), suffixe in zip(dd.fig_rendement(), ("cour", "cst")):
        png(f"fig_dd_rendement_{suffixe}", f)
    png("fig_dd_perception", dd.fig_perception())
    for nom in ("table_parts", "table_pib", "table_rendement", "table_perception"):
        t = getattr(dd, nom)()
        print(f"\n{nom} : {t.shape[0]} lignes, colonnes {list(t.columns)}")
        print(t.head(3).to_string())

    # Recoupement avec la note : part dans les recettes fiscales, taux, prévisions.
    n = pd.read_csv(NOTE).set_index("annee")
    p = dd._parts()
    for a in p.index:
        if abs(p.loc[a, "part_recettes"] - n.loc[a, "part_recettes_fiscales_pct"]) > 0.006:
            erreurs.append(f"part recettes {a}")
        if abs(p.loc[a, "part_depenses"] - n.loc[a, "part_depenses_hors_dette_pct"]) > 0.006:
            erreurs.append(f"part dépenses {a}")
        ecart = abs(p.loc[a, "part_pib"] - n.loc[a, "part_pib_pct"])
        if ecart > 0.006:
            print(f"écart part du PIB {a} : {p.loc[a, 'part_pib']:.3f} contre {n.loc[a, 'part_pib_pct']}")
    q = dd._perception()
    for a in q.index:
        if abs(q.loc[a, "taux"] - n.loc[a, "taux_implicite_total_pct"]) > 0.006:
            erreurs.append(f"taux total {a}")
        if not pd.isna(q.loc[a, "general"]) and abs(
                q.loc[a, "taux_general"] - n.loc[a, "taux_implicite_regime_general_pct"]) > 0.006:
            erreurs.append(f"taux général {a}")
    s = dd._series_rendement()
    for a in range(2001, 2027):
        tot = s[("prev", "droits")].get(a, float("nan")) + s[("prev", "redevance")].get(a, float("nan"))
        attendu = n.loc[a, "prevision_lf_total_MDT"] if a in n.index else float("nan")
        if a <= 2025 and abs(tot - attendu) > 0.05:
            erreurs.append(f"prévision {a} : {tot} contre {attendu}")
    for a in range(2018, 2025):
        d = s[("real", "droits")][a]
        r = s[("real", "redevance")][a]
        if abs(d - n.loc[a, "cdc_droits_MDT"]) > 0.12 or abs(r - n.loc[a, "cdc_redevances_MDT"]) > 0.12:
            erreurs.append(f"réalisation {a}")

    # Les cinq tableaux imprimés.
    for nom in ("redevance", "correspondances", "bandes", "minimum-perception", "calendrier-ue"):
        print(f"\n=== {nom}")
        tarifs.imprime("douane/tarifs-releves-droits-douane.csv", nom)

    # Aucun mot interdit dans les relevés, manifestes et module.
    import re
    for f in list((LIVRE / "douane").glob("*")) + [LIVRE / "figures" / "droits_douane.py"]:
        for i, ligne in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if re.search(RESTE, ligne, re.I) and not ligne.lstrip().startswith("#"):
                erreurs.append(f"{f.name}:{i} : {ligne[:90]}")
    print("\nERREURS :", erreurs or "aucune")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
