"""Figure du chapitre « La durée du travail et les congés » : le temps de travail habituel en 2019.

    from figures import temps_travail as tt
    tt.vues_temps_travail(), tt.table_temps_travail()   # occupés selon le temps habituel, INS

D'OÙ VIENNENT LES DONNÉES. Le module ne lit que `figtools.series()` — l'entrepôt
`tunisia-data` s'il est installé, sinon le snapshot `precis/_seriescache/` :

  - `ins-emploi-duree-travail-2019` : INS, *Indicateurs de l'emploi et du chômage, quatrième
    trimestre 2019*, tableau 6, p. 5 ; milliers d'occupés selon le temps de travail HABITUEL dans
    toutes les activités (sous-emploi lié au temps du travail, temps complet, sur-emploi : plus de
    48 heures), deuxième, troisième et quatrième trimestres 2019. Trois trimestres ne font pas une
    série : la figure les montre côte à côte, sans tendance.

Les heures EFFECTIVES de l'emploi principal que publie l'OIT pour 2019 (tranche « 49 heures ou
plus ») ne se tracent pas ici : autre mesure, une seule date (décision du 20/10/2026).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_INS = "ins-emploi-duree-travail-2019"

BLEU, ORANGE, GRIS = "#08519c", "#bc4c00", "#6e7781"

PERIODES = ["2019-T2", "2019-T3", "2019-T4"]
CATEGORIES = [("temps_complet", BLEU), ("sur_emploi", ORANGE), ("sous_emploi", GRIS)]

_L = {
    "c_periode": {"fr": "Trimestre", "ar": "الثلاثية"},
    "sous_emploi": {"fr": "Sous-emploi lié au temps de travail",
                    "ar": "الشغل الناقص المرتبط بوقت العمل"},
    "temps_complet": {"fr": "Temps complet", "ar": "الشغل كامل الوقت"},
    "sur_emploi": {"fr": "Plus de 48 heures", "ar": "أكثر من 48 ساعة"},
    "ensemble": {"fr": "Ensemble des occupés", "ar": "مجموع المشتغلين"},
    "milliers": {"fr": "{nom}<br>(milliers)", "ar": "{nom}<br>(بالآلاف)"},
    "part": {"fr": "{nom}<br>(% des occupés)", "ar": "{nom}<br>(% من المشتغلين)"},
    "trim": {"fr": "{t} trimestre 2019", "ar": "الثلاثية {n} لسنة 2019"},
    "x_trim": {"fr": "T{n} 2019", "ar": "ث{n} 2019"},
    "vue_milliers": {"fr": "Milliers d'occupés", "ar": "آلاف المشتغلين"},
    "vue_parts": {"fr": "Parts des occupés", "ar": "النسب من المشتغلين"},
    "y_milliers": {"fr": "Occupés (milliers)", "ar": "المشتغلون (بالآلاف)"},
    "y_pct": {"fr": "% des occupés", "ar": "% من المشتغلين"},
}

RANGS_FR = {"2": "2^e^", "3": "3^e^", "4": "4^e^"}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _nombre(v: float, decimales: int = 1) -> str:
    """Nombre à la française : virgule décimale, espace insécable entre les milliers."""
    texte = f"{v:,.{decimales}f}"
    return texte.replace(",", "\N{NO-BREAK SPACE}").replace(".", ",")


def _donnees():
    """[(code de trimestre, {catégorie: (milliers, part imprimée)})], dans l'ordre du temps."""
    d = figtools.series(SERIE_INS)
    lignes = []
    for p in PERIODES:
        r = d[d["periode"].astype(str) == p]
        val = {}
        for c in ("sous_emploi", "temps_complet", "sur_emploi", "ensemble"):
            x = r[r["categorie"] == c]
            val[c] = (float(x["milliers"].iloc[0]), float(x["part_imprimee_pct"].iloc[0]))
        lignes.append((p, val))
    return lignes


def _fig(en_parts: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    lignes = _donnees()
    xs = list(range(len(lignes)))
    fig, ax = plt.subplots(figsize=(8, 5))
    bas = [0.0] * len(lignes)
    for c, couleur in CATEGORIES:
        # Parts : celles qu'imprime la source, non recalculées.
        h = [v[c][1] if en_parts else v[c][0] for _, v in lignes]
        ax.bar(xs, h, bottom=bas, color=couleur, width=0.6, label=ft(_lab(c)))
        for x, b, y in zip(xs, bas, h):
            if c != "sous_emploi":
                ax.annotate(_nombre(y), (x, b + y / 2), ha="center", va="center",
                            fontsize=8, color="white")
        bas = [b + y for b, y in zip(bas, h)]
    if not en_parts:
        for x, (_, v) in zip(xs, lignes):
            ax.annotate(_nombre(v["ensemble"][0]), (x, v["ensemble"][0]),
                        textcoords="offset points", xytext=(0, 3), ha="center", fontsize=8)
    ax.set_xticks(xs)
    ax.set_xticklabels([ft(_lab("x_trim").format(n=p[-1])) for p, _ in lignes])
    ax.set_ylabel(ft(_lab("y_pct" if en_parts else "y_milliers")))
    if en_parts:
        ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda x, _: _nombre(x, 0)))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), fontsize=8, frameon=False,
              ncol=3)
    fig.tight_layout()
    return fig


def vues_temps_travail():
    return [(_lab("vue_milliers"), _fig(False)), (_lab("vue_parts"), _fig(True))]


def table_temps_travail():
    import pandas as pd
    cols = {_lab("c_periode"): []}
    noms = []
    for c in ("temps_complet", "sur_emploi", "sous_emploi", "ensemble"):
        nom = _lab(c)
        noms.append((c, _lab("milliers").format(nom=nom).replace("<br>", " ")))
        if c != "ensemble":
            noms.append((c + "%", _lab("part").format(nom=nom).replace("<br>", " ")))
    for _, n in noms:
        cols[n] = []
    for p, v in _donnees():
        n = p[-1]
        cols[_lab("c_periode")].append(
            _lab("trim").format(t=RANGS_FR[n].replace("^", ""), n=n))
        for c, nom in noms:
            if c.endswith("%"):
                cols[nom].append(v[c[:-1]][1])
            else:
                cols[nom].append(v[c][0])
    return pd.DataFrame(cols)
