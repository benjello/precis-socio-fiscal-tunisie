"""Rendement d'un impôt rapporté au PIB de chaque base des comptes nationaux.

Composant commun des figures de rendement de l'impôt sur le revenu, de l'impôt sur les
sociétés et des droits de consommation, sur le modèle de `figures/tva.py` : le PIB est celui
de chacune des trois bases des comptes nationaux (1983, 1997, 2015), série
`pib-courant-par-base` (annexe du site sur le PIB). Chaque base est une courbe distincte,
aucun coefficient de passage n'est calculé, et une année publiée dans deux bases porte deux
points, chacun rapporté au PIB de sa base.

 - 1986-1991 : PIB « présumé » de base 1983 (aucune série de base connue avant 1992), points
   pâles ;
 - 2002-2004 et 2025 : valeurs du ministère des Finances que la source ne rattache à aucune
   base, losanges gris hors de toute courbe ;
 - marqueur plein : PIB publié dans sa base, ou rétropolation non précisée ; marqueur creux :
   PIB recalculé pour le passé par l'INS ;
 - l'axe de droite rapporte l'impôt aux dépenses totales de l'État (publiées depuis 1990),
   sans aucun PIB.

Chaque figure fournit : la colonne de montant de `recettes-fiscales-composition`, l'année
de la rupture de série propre à l'impôt et ses libellés.
"""
from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import figtools

SERIE_COMPOSITION = "recettes-fiscales-composition"
SERIE_RATIOS = "irpp-ratios"
SERIE_PIB = "pib-courant-par-base"
SERIES = (SERIE_COMPOSITION, SERIE_RATIOS, SERIE_PIB)

ANNEE_DEPENSES = 1990
BASES = {
    1983: {"couleur": "#1a7f37", "marque": "o"},
    1997: {"couleur": "#8250df", "marque": "s"},
    2015: {"couleur": "#0969da", "marque": "^"},
}
ROUGE, GRIS = "#d1242f", "#57606a"

_L = {
    "lg_base": {"fr": "{nom} / PIB, base {b} (éch. gauche)",
                "ar": "{nom} / الناتج، أساس {b} (يسار)"},
    "lg_presumee": {"fr": "base 1983 présumée (1986-1991)",
                    "ar": "أساس 1983 مفترض (1986-1991)"},
    "lg_minfin": {"fr": "PIB du ministère non rattaché à une base (2002-2004, 2025)",
                  "ar": "ناتج الوزارة غير المرتبط بأساس (2002-2004، 2025)"},
    "lg_dep": {"fr": "{nom} / dépenses de l'État (éch. droite, sans PIB)",
               "ar": "{nom} / نفقات الدولة (يمين، دون ناتج)"},
    "lg_plein": {"fr": "plein : PIB publié dans sa base, ou rétropolation non précisée\n"
                       "(base 1983) ; creux : PIB recalculé pour le passé",
                 "ar": "مملوء: ناتج منشور في أساسه أو إعادة احتساب غير محدّدة\n(أساس 1983)؛ "
                       "مفرغ: ناتج أعيد احتسابه للماضي"},
    "y_pib": {"fr": "En % du PIB de la base", "ar": "% من ناتج الأساس"},
    "y_dep": {"fr": "En % des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "rup_pib": {"fr": "PIB : base {b}", "ar": "الناتج: أساس {b}"},
    "ib_ratio": {"fr": "{a} · base {b} : {r} % du PIB ({pib} MD ; {nom} {m} MD)",
                 "ar": "{a} · أساس {b} : {r} % من الناتج (الناتج {pib} م.د ؛ {nom} {m} م.د)"},
    "ib_minfin": {"fr": "{a} · PIB du ministère, base non rattachée : {r} % du PIB "
                        "({pib} MD ; {nom} {m} MD)",
                  "ar": "{a} · ناتج الوزارة، أساس غير مرتبط : {r} % من الناتج "
                        "(الناتج {pib} م.د ؛ {nom} {m} م.د)"},
    "ib_dep": {"fr": "{a} · {r} % des dépenses de l'État",
               "ar": "{a} · {r} % من نفقات الدولة"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_base": {"fr": "Base du PIB", "ar": "أساس الناتج"},
    "col_pib": {"fr": "PIB de cette base (MD courants)", "ar": "ناتج هذا الأساس (م.د جارية)"},
    "col_retro": {"fr": "PIB recalculé pour le passé", "ar": "ناتج أعيد احتسابه للماضي"},
    "col_ratio": {"fr": "{nom} en % du PIB de cette base",
                  "ar": "{nom} % من ناتج هذا الأساس"},
    "col_dep": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "col_rec": {"fr": "% des recettes fiscales", "ar": "% من المداخيل الجبائية"},
    "col_mdt": {"fr": "{nom} (MDT)", "ar": "{nom} (م.د)"},
    "col_src": {"fr": "Source du PIB", "ar": "مصدر الناتج"},
    "b_presumee": {"fr": "1983 (présumée)", "ar": "1983 (مفترض)"},
    "b_minfin": {"fr": "non rattachée (ministère des Finances)",
                 "ar": "غير مرتبط (وزارة المالية)"},
    "r_oui": {"fr": "oui", "ar": "نعم"},
    "r_non": {"fr": "non", "ar": "لا"},
    "r_np": {"fr": "non précisé par la source", "ar": "غير محدّد في المصدر"},
}


def lab(key: str, **kw) -> str:
    texte = _L[key].get(figtools.lang(), _L[key]["fr"])
    return texte.format(**kw) if kw else texte


def donnees(col_mdt: str, col_pct: str) -> pd.DataFrame:
    """Une ligne par (année, base du PIB) : l'impôt rapporté au PIB de cette base."""
    comp = figtools.series(SERIE_COMPOSITION)[["annee", col_mdt, col_pct]]
    dep = figtools.series(SERIE_RATIOS)[["annee", "depenses_totales_MDT"]]
    pib = figtools.series(SERIE_PIB).copy()
    texte = pib["base"].str
    pib["base_num"] = texte.extract(r"(1983|1997|2015)", expand=False).astype("Int64")
    pib["presumee"] = texte.contains("présumée")
    pib["minfin"] = texte.startswith("non rattachée")
    d = pib.merge(comp, on="annee", how="inner").merge(dep, on="annee", how="left")
    d["mdt"] = d[col_mdt]
    d["pct_rec"] = d[col_pct]
    d["sur_pib_pct"] = 100 * d["mdt"] / d["pib_MD"]
    d["sur_dep_pct"] = 100 * d["mdt"] / d["depenses_totales_MDT"]
    return d.sort_values(["annee", "base_num"], na_position="last").reset_index(drop=True)


def depenses(col_mdt: str) -> pd.DataFrame:
    comp = figtools.series(SERIE_COMPOSITION)[["annee", col_mdt]]
    dep = figtools.series(SERIE_RATIOS)[["annee", "depenses_totales_MDT"]]
    d = comp.merge(dep, on="annee")
    d = d[d["annee"] >= ANNEE_DEPENSES].dropna(subset=["depenses_totales_MDT"])
    return d.assign(pct=100 * d[col_mdt] / d["depenses_totales_MDT"])


def _nom_base(r) -> str:
    if r.minfin:
        return lab("b_minfin")
    if r.presumee:
        return lab("b_presumee")
    return str(int(r.base_num))


def _retro(valeur) -> str:
    return lab({"oui": "r_oui", "non": "r_non"}.get(str(valeur), "r_np"))


def tableau(col_mdt: str, col_pct: str, nom: str) -> pd.DataFrame:
    d = donnees(col_mdt, col_pct)
    dep = depenses(col_mdt).set_index("annee")["pct"]
    lignes = []
    for r in d.itertuples(index=False):
        lignes.append({
            lab("col_annee"): int(r.annee),
            lab("col_base"): _nom_base(r),
            lab("col_pib"): round(r.pib_MD, 1),
            lab("col_retro"): _retro(r.retropole),
            lab("col_mdt", nom=nom): r.mdt,
            lab("col_ratio", nom=nom): round(r.sur_pib_pct, 2),
            lab("col_dep"): round(dep[r.annee], 2) if r.annee in dep.index else None,
            lab("col_rec"): round(r.pct_rec, 2),
            lab("col_src"): r.publication,
        })
    return pd.DataFrame(lignes)


def figure(col_mdt: str, col_pct: str, *, nom: str, annee_debut: int, titre: str,
           rupture: str, y_rupture: float = 0.86, legende_y: float = 0.2):
    """Trace le rendement par base : `annee_debut` est la première année du droit actuel."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees(col_mdt, col_pct)
    dep = depenses(col_mdt)
    x0, x1 = int(d["annee"].min()), int(d["annee"].max())

    fig, ax1 = plt.subplots(figsize=(9.5, 6.0))
    ax2 = ax1.twinx()
    ax1.axvspan(x0 - 0.5, annee_debut - 0.5, color="#8b949e", alpha=0.13, lw=0)
    ax1.axvline(annee_debut - 0.5, color=GRIS, lw=1.2, ls="--")

    def point(r, marque, **style):
        p, = ax1.plot([r.annee], [r.sur_pib_pct], marque, **style)
        cle = "ib_minfin" if r.minfin else "ib_ratio"
        figtools.infobulle(p, lab(cle, a=int(r.annee), b=_nom_base(r), nom=nom,
                                  r=f"{r.sur_pib_pct:.2f}".replace(".", ","),
                                  pib=f"{r.pib_MD:,.0f}".replace(",", " "),
                                  m=f"{r.mdt:,.0f}".replace(",", " ")))

    for base, st in BASES.items():
        g = d[(d["base_num"] == base) & (d["annee"] >= annee_debut)]
        ax1.plot(g["annee"], g["sur_pib_pct"], color=st["couleur"], lw=1.8, zorder=2)
        for r in g.itertuples(index=False):
            creux = str(r.retropole) == "oui"
            point(r, st["marque"], ms=5, color=st["couleur"],
                  alpha=0.4 if r.presumee else 1.0,
                  mfc="white" if creux else st["couleur"], mew=1.2, zorder=3)

    avant = d[(d["base_num"] == 1983) & (d["annee"] < annee_debut)]
    ax1.plot(avant["annee"], avant["sur_pib_pct"], "o:", color=GRIS, lw=1.6, ms=4, zorder=2)
    for r in avant.itertuples(index=False):
        point(r, "o", ms=4, color=GRIS, zorder=3)

    for r in d[d["minfin"]].itertuples(index=False):
        point(r, "D", ms=5, mfc="white", mec=GRIS, mew=1.2, zorder=3)

    ax2.plot(dep["annee"], dep["pct"], "--", color=ROUGE, lw=1.6, zorder=2)
    for r in dep.itertuples(index=False):
        p, = ax2.plot([r.annee], [r.pct], "x", ms=4, color=ROUGE, zorder=3)
        figtools.infobulle(p, lab("ib_dep", a=int(r.annee),
                                  r=f"{r.pct:.2f}".replace(".", ",")))

    for annee, base in ((1997, 1997), (2010, 2015)):
        figtools.marque_rupture(ax1, annee)
        ax1.annotate(ft(lab("rup_pib", b=base)), xy=(annee - 0.5, 0),
                     xycoords=("data", "axes fraction"), xytext=(-4, 4),
                     textcoords="offset points", ha="right", va="bottom", fontsize=7,
                     color=GRIS)

    bas, haut = ax1.get_ylim()
    y_texte = bas + y_rupture * (haut - bas)
    ax1.annotate(ft(rupture), xy=(annee_debut - 0.5, y_texte),
                 xytext=(annee_debut + 1.0, y_texte), fontsize=8, color=GRIS, va="center",
                 arrowprops=dict(arrowstyle="->", color=GRIS, lw=1))

    ax1.set_ylabel(ft(lab("y_pib")))
    ax2.set_ylabel(ft(lab("y_dep")), color=ROUGE)
    ax1.set_xlabel(ft(lab("xlabel")))
    ax1.set_xlim(x0 - 0.8, x1 + 0.8)
    ax1.set_title(ft(titre))
    ax1.grid(True, alpha=0.3)

    poignees = [Line2D([], [], color=st["couleur"], marker=st["marque"], ms=5, lw=1.8,
                       label=ft(lab("lg_base", nom=nom, b=base))) for base, st in BASES.items()]
    poignees.append(Line2D([], [], color=BASES[1983]["couleur"], marker="o", ms=5, lw=0,
                           alpha=0.4, label=ft(lab("lg_presumee"))))
    poignees.append(Line2D([], [], color=GRIS, marker="D", mfc="white", ms=5, lw=0,
                           label=ft(lab("lg_minfin"))))
    poignees.append(Line2D([], [], color=ROUGE, marker="x", ms=4, lw=1.6, ls="--",
                           label=ft(lab("lg_dep", nom=nom))))
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ms=5, lw=0,
                           label=ft(lab("lg_plein"))))
    fig.tight_layout(rect=(0, legende_y, 1, 1))
    fig.legend(handles=poignees, loc="lower center", ncol=2, fontsize=7.5, frameon=False)
    return fig
