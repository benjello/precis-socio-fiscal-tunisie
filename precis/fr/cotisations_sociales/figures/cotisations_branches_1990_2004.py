"""Figure « cotisations de la CNSS par branche, 1990-2004 » (source CNSS, comptes de bilan).

    from figures import cotisations_branches_1990_2004 as cb
    cb.fig_branches()   # cotisations par branche, MD courants, et la série encaissée 2000-2004
    cb.table()          # les montants de la figure (onglet Données)

D'OÙ VIENNENT LES DONNÉES. La Rétrospective financière 1990-2004 de la CNSS (série
`cnss-retrospective-ressources-emplois` de tunisia-data), tableaux de l'ensemble des
régimes, comptabilité des « Bilans » — droits constatés, non encaissements —, en milliers de
dinars courants convertis en millions :
  - prestations familiales (page 60), assurances sociales (page 61) et pensions hors régime
    complémentaire (page 64), ensemble des régimes sans la convention tuniso-française. Leur
    somme est exactement la ligne « Cotisations » du tableau de l'ensemble (page 78) : le
    découpage ne compte rien deux fois ;
  - régime complémentaire, accidents du travail et maladies professionnelles, protection
    sociale des travailleurs : lignes propres du tableau de l'ensemble (page 78).
La « participation française » de la convention tuniso-française n'est pas une cotisation et
n'est pas tracée. Les quatre lignes de cotisations de la page 78 sont celles que la fiche de
tunisia-data compare, de 2000 à 2004, à la série des cotisations encaissées (`cnss-cotisations`) :
l'écart va de −1,13 % à −0,81 % selon l'année, sans explication établie. Les points de cette
série sont tracés pour le montrer.

LES COLONNES MASQUÉES. Une cellule que la reliure masque porte une estimation provisoire ;
l'année est alors hachurée, et la table laisse la valeur publiée vide en donnant
l'estimation à part. Le statut est lu cellule par cellule : rien n'est codé en dur.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "cnss-retrospective-ressources-emplois"
SERIE_ENCAISSEES = "cnss-cotisations"

BLEU, ORANGE, GRIS, VERT, ROUGE, VIOLET = ("#08519c", "#bc4c00", "#6e7781", "#1a7f37",
                                           "#cf222e", "#8250df")
BLEU_CLAIR, ORANGE_CLAIR = "#6baed6", "#fdae6b"

# (nom, page, branche attendue, clé, couleur), dans l'ordre d'empilement.
_BRANCHES = (
    ("pensions", 64, "pensions", "cotisations", BLEU),
    ("rc", 78, None, "cotisations_rc", BLEU_CLAIR),
    ("as", 61, "assurances sociales", "cotisations", VERT),
    ("pf", 60, "prestations familiales", "cotisations", ORANGE),
    ("atmp", 78, None, "cotisations_atmp", ROUGE),
    ("pst", 78, None, "cotisations_pst", VIOLET),
)

_L = {
    "titre": {"fr": "Cotisations de la CNSS par branche, comptes de bilan, 1990-2004",
              "ar": "اشتراكات الصندوق الوطني للضمان الاجتماعي حسب الفرع، حسب الموازنات، "
                    "1990-2004"},
    "y": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "x": {"fr": "Année", "ar": "السنة"},
    "pensions": {"fr": "Pensions, régimes légaux", "ar": "الجرايات، الأنظمة القانونية"},
    "rc": {"fr": "Régime complémentaire", "ar": "النظام التكميلي"},
    "as": {"fr": "Assurances sociales", "ar": "التأمينات الاجتماعية"},
    "pf": {"fr": "Prestations familiales", "ar": "المنافع العائلية"},
    "atmp": {"fr": "Accidents du travail et maladies professionnelles",
             "ar": "حوادث الشغل والأمراض المهنية"},
    "pst": {"fr": "Protection sociale des travailleurs",
            "ar": "الحماية الاجتماعية للعمّال"},
    "encaissees": {"fr": "Cotisations encaissées, tous régimes (série 2000-2020)",
                   "ar": "الاشتراكات المستخلصة، كلّ الأنظمة (سلسلة 2000-2020)"},
    "estime": {"fr": "{annees} : valeur en partie estimée (reliure du document)",
               "ar": "{annees}: قيمة مقدّرة جزئياً (تجليد الوثيقة)"},
    "debut_atmp": {"fr": "{a} : première année\ndes accidents du travail", "ar": "{a}: أوّل سنة\nلفرع حوادث الشغل"},
    "debut_pst": {"fr": "{a} : première année de la\nprotection sociale des travailleurs",
                  "ar": "{a}: أوّل سنة للحماية\nالاجتماعية للعمّال"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_total": {"fr": "Total (MD)", "ar": "المجموع (م.د)"},
    "col_encaissees": {"fr": "Cotisations encaissées, série 2000-2020 (MD)",
                       "ar": "الاشتراكات المستخلصة، سلسلة 2000-2020 (م.د)"},
    "col_ecart": {"fr": "Écart du total à la série encaissée (%)",
                  "ar": "فارق المجموع عن السلسلة المستخلصة (٪)"},
    "col_estimations": {"fr": "Estimations provisoires (MD)", "ar": "تقديرات مؤقّتة (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str, **valeurs) -> list[str]:
    return [figtools.fig_text(l) for l in _lab(key).format(**valeurs).split("\n")]


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _donnees() -> dict[str, dict[int, tuple[float, bool]]]:
    """{branche: {année: (MD, estimé ?)}} ; une branche pas encore instituée vaut zéro."""
    import pandas as pd
    d = figtools.series(SERIE)
    d = d[d["page"].isin({p for _, p, _, _, _ in _BRANCHES})]
    for nom, page, branche, _, _ in _BRANCHES:
        s = d[d["page"] == page]
        assert set(s["regime"]) == {"ENSEMBLE"}, f"page {page} : ensemble des régimes attendu"
        if branche:
            assert set(s["branche"]) == {branche}, f"page {page} : branche {branche} attendue"
    c = {(int(r.page), r.cle, int(r.annee)): (float(r.valeur_ou_estimation) / 1000,
                                               bool(pd.isna(r.valeur)))
         for r in d.itertuples() if not pd.isna(r.valeur_ou_estimation)}
    annees = sorted({a for _, _, a in c})
    return {nom: {a: c.get((page, cle, a), (0.0, False)) for a in annees}
            for nom, page, _, cle, _ in _BRANCHES}


def _encaissees() -> dict[int, float]:
    return {int(r.annee): float(r.cotisations_md)
            for r in figtools.series(SERIE_ENCAISSEES).itertuples()}


def table():
    import pandas as pd
    g = _donnees()
    enc = _encaissees()
    ans = sorted(g["pensions"])
    lignes = []
    for a in ans:
        ligne = {_lab("col_annee"): a}
        estimes = []
        for nom, *_ in _BRANCHES:
            v, est = g[nom][a]
            ligne[_lab(nom) + " (MD)"] = None if est else round(v, 1)
            if est:
                estimes.append(f"{_lab(nom)} : {_nombre(v)}")
        tot = sum(g[n][a][0] for n, *_ in _BRANCHES)
        est = any(g[n][a][1] for n, *_ in _BRANCHES)
        ligne[_lab("col_total")] = None if est else round(tot, 1)
        if est:
            estimes.append(f"{_lab('col_total').split(' (')[0]} : {_nombre(tot)}")
        ligne[_lab("col_encaissees")] = enc.get(a)
        ligne[_lab("col_ecart")] = (round(100 * (tot - enc[a]) / enc[a], 2)
                                    if a in enc and not est else None)
        ligne[_lab("col_estimations")] = " ; ".join(estimes)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def fig_branches():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _donnees()
    ans = sorted(g["pensions"])
    fig, ax = plt.subplots(figsize=(9.5, 6.4))

    bas = {a: 0.0 for a in ans}
    poignees = []
    for nom, _, _, _, couleur in _BRANCHES:
        for a in ans:
            v, est = g[nom][a]
            if v:
                ax.bar(a, v, bottom=bas[a], width=0.72, color=couleur,
                       hatch="////" if est else None, edgecolor="white", lw=0.4)
            bas[a] += v
        poignees.append(Patch(color=couleur, label=ft(_lab(nom))))

    enc = {a: v for a, v in _encaissees().items() if a in bas}
    if enc:
        ax.plot(list(enc), list(enc.values()), "D", color="#24292f", ms=5, mfc="#24292f")
        poignees.append(Line2D([], [], color="#24292f", marker="D", lw=0, ms=5,
                               label=ft(_lab("encaissees"))))
    estimees = sorted({a for s in g.values() for a, (_, e) in s.items() if e})
    if estimees:
        poignees.append(Patch(facecolor="white", edgecolor=GRIS, hatch="////",
                              label=ft(_lab("estime").format(
                                  annees=", ".join(map(str, estimees))))))

    # Apparition des branches AT/MP et PST : première année non nulle.
    for nom, cle in (("atmp", "debut_atmp"), ("pst", "debut_pst")):
        premiere = next((a for a in ans if g[nom][a][0] > 0), None)
        if premiere is not None:
            ax.annotate("\n".join(_lignes(cle, a=premiere)), (premiere, bas[premiere]),
                        xytext=(premiere - 1.6, bas[premiere] + 230), fontsize=7.5,
                        color="#57606a", ha="center",
                        arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8))
    for a in (ans[0], ans[-1]):
        ax.annotate(_nombre(bas[a], 0), (a, max(bas[a], enc.get(a, 0))),
                    textcoords="offset points", xytext=(0, 7), ha="center", fontsize=8,
                    color="#24292f")

    ax.set_ylim(0, max(bas.values()) * 1.18)
    ax.set_xticks(ans)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2,
              fontsize=8, frameon=False)
    fig.tight_layout()
    return fig
