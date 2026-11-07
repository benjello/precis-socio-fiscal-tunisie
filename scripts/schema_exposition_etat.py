"""Schéma du circuit d'exposition de l'État aux entreprises publiques : ce qui est mesuré (document
public), ce qui est approximé/borné, et ce qui manque (le net consolidé, incalculable sans consolidation).

    uv run python scripts/schema_exposition_etat.py

Écrit docs/exemples-soes/schema-exposition-etat.png et .pdf. Rien n'est saisi : les montants sont ceux,
déjà sourcés, du dossier (annexe 8, Cour des comptes, FMI Article IV 2021, états financiers STEG).
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

SORTIE = Path(__file__).resolve().parent.parent / "docs/exemples-soes"

BLEU, GRIS, ROUGE, VERT = "#1a4f8a", "#5b6670", "#b02418", "#2e7d32"

# nœuds : clé -> (x, y, largeur, hauteur, libellé)
N = {
    "choc":  (5.0, 7.3, 2.6, 0.7, "Choc\nprix du baril · change"),
    "comp":  (5.0, 6.0, 2.6, 0.7, "Caisse de compensation\n~12 Md DT (2022)"),
    "ep":    (5.0, 4.4, 3.2, 0.9, "STIR · STEG · Office des Céréales\n(≈ 40 % des transferts)"),
    "banq":  (1.4, 2.4, 2.4, 0.8, "Banques publiques\n(NPL 17 %)"),
    "caiss": (8.6, 2.4, 2.4, 0.8, "Caisses sociales"),
    "comm":  (8.9, 4.4, 2.0, 0.8, "Communes\n& autres EP"),
    "etat":  (5.0, 1.0, 3.0, 0.8, "État / Trésor"),
}


def boite(ax, cle, couleur=BLEU):
    x, y, w, h, texte = N[cle]
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.04,rounding_size=0.12",
                                linewidth=1.3, edgecolor=couleur, facecolor="white", zorder=3))
    ax.text(x, y, texte, ha="center", va="center", fontsize=8.2, zorder=4, color="#15232e")


def bord(a, b):
    xa, ya, wa, ha, _ = N[a]
    xb, yb, wb, hb, _ = N[b]
    return (xa, ya - ha / 2 if yb < ya else ya + ha / 2), (xb, yb + hb / 2 if yb < ya else yb - hb / 2)


def fleche(ax, a, b, couleur, style, texte, rad=0.0, dx=0.0, dy=0.0, pos=0.5):
    (x0, y0), (x1, y1) = bord(a, b)
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), connectionstyle=f"arc3,rad={rad}",
                 arrowstyle="-|>", mutation_scale=13, linewidth=1.5, linestyle=style,
                 color=couleur, zorder=2, shrinkA=2, shrinkB=2))
    mx, my = x0 + (x1 - x0) * pos + dx, y0 + (y1 - y0) * pos + dy
    ax.text(mx, my, texte, ha="center", va="center", fontsize=7, color=couleur, zorder=5,
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))


def main() -> int:
    fig, ax = plt.subplots(figsize=(9.6, 8.2))
    ax.set_xlim(0, 10); ax.set_ylim(0.05, 8.1); ax.axis("off")

    for cle in N:
        boite(ax, cle)

    # --- flux MESURÉS (trait plein) : documents publics, chiffre exact ---
    fleche(ax, "choc", "comp", GRIS, "-", "incontrôlable (×8 vs budget)", dx=1.9, pos=0.5)
    fleche(ax, "comp", "ep", BLEU, "-", "7 628 MD (2022) = transferts, exact", dx=2.2, pos=0.45)
    fleche(ax, "ep", "etat", BLEU, "-", "EP → État\n10 692 MD", rad=-0.55, dx=-1.15, dy=-0.55)
    fleche(ax, "etat", "ep", BLEU, "-", "État → EP\n7 044 MD", rad=-0.55, dx=1.2, dy=-0.9)

    # --- flux APPROXIMÉS / BORNÉS (tireté) ---
    fleche(ax, "ep", "banq", GRIS, (0, (5, 3)), "créances classées", rad=0.15, dx=-0.2, dy=0.35)
    fleche(ax, "ep", "caiss", GRIS, (0, (5, 3)), "impayés ~0,9 Md", rad=-0.15, dx=0.2, dy=0.35)
    fleche(ax, "comm", "ep", GRIS, (0, (5, 3)), "factures impayées ~2 Md", dy=0.28, pos=0.5)
    fleche(ax, "etat", "banq", GRIS, (0, (5, 3)), "recapitalisation", rad=0.3, dx=-0.35, dy=-0.15)
    fleche(ax, "etat", "caiss", GRIS, (0, (5, 3)), "transferts", rad=-0.3, dx=0.35, dy=-0.15)

    # --- ce qui MANQUE : le net consolidé (pointillé rouge, au centre) ---
    ax.add_patch(FancyBboxPatch((3.75, 2.85), 2.5, 0.8, boxstyle="round,pad=0.05,rounding_size=0.12",
                 linewidth=1.6, edgecolor=ROUGE, facecolor="#fdf1ef", linestyle=(0, (1, 2)), zorder=6))
    ax.text(5.0, 3.25, "NET du secteur public\nincalculable sans consolidation",
            ha="center", va="center", fontsize=8.0, color=ROUGE, fontweight="bold", zorder=7)

    # --- légende ---
    y = 0.78
    for coul, sty, lib in [(BLEU, "-", "mesuré — document public (chiffre exact, recoupé Cour des comptes · FMI)"),
                           (GRIS, (0, (5, 3)), "approximé / borné — à partir des données disponibles"),
                           (ROUGE, (0, (1, 2)), "manquant — ce que seule la consolidation révélerait")]:
        ax.plot([0.25, 0.95], [y, y], color=coul, linestyle=sty, linewidth=1.8)
        ax.text(1.05, y, lib, fontsize=7.3, va="center", color="#15232e")
        y -= 0.3

    ax.text(10.0, 0.25, "Reconstruit à partir des seuls documents publics (annexe 8 du PLF, Cour des comptes,\n"
            "FMI Article IV 2021, états financiers publiés).", ha="right", va="bottom",
            fontsize=6.6, color=GRIS, style="italic")

    fig.tight_layout()
    SORTIE.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(SORTIE / f"schema-exposition-etat.{ext}", dpi=190, bbox_inches="tight")
    print("écrit :", SORTIE / "schema-exposition-etat.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
