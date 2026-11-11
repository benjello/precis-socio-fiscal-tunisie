"""Figure « versements des caisses au budget de l'État (tableau A des lois de finances), 1985-2005 ».

    from figures import tableau_a_caisses_1985_2005 as ta
    ta.fig_vue("composantes")  # forfaits + familles nécessiteuses, puis agrégat, MD courants
    ta.fig_vue("pib")          # total des versements, % du PIB
    ta.vues()                  # les deux, pour figtools.figure_tabs
    ta.table()                 # une ligne par gestion

D'OÙ VIENNENT LES DONNÉES. Le tableau A (recettes du budget général) de chaque loi de finances,
gestions 1985 à 2005, série `lf-tableau-a-caisses` de tunisia-data, snapshotée dans
`precis/_seriescache/`. Ce sont des PRÉVISIONS de loi de finances, non des réalisations.

DEUX PÉRIMÈTRES, JAMAIS RACCORDÉS. De 1985 à 1994, trois lignes détaillées — forfait hospitalier
CNSS, forfait hospitalier CNRPS, contribution au programme des familles nécessiteuses incluant le
produit de la majoration FSE de 0,5 point. De 1995 à 2005, une seule ligne agrégée, « versements
et contributions des caisses de sécurité sociale ». Le total détaillé de 1994 (37,0 MD) saute à
57,0 MD en agrégat (1995) : la rupture de périmètre est marquée, jamais lissée. Le PIB au
dénominateur de la vue au PIB est celui que retient le ministère des Finances (série `irpp-ratios`).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "lf-tableau-a-caisses"
SERIE_PIB = "irpp-ratios"
RUPTURE = 1995  # détail en trois composantes (1985-1994) → ligne agrégée (1995-2005)
VUES = ("composantes", "pib")

BLEU, VERT, ORANGE, GRIS = "#08519c", "#1a7f37", "#bc4c00", "#6e7781"

# Les trois composantes détaillées, dans l'ordre de l'empilement, puis l'agrégat.
COMPOSANTES = ("forfait_hospitalier_cnss", "forfait_hospitalier_cnrps",
               "familles_necessiteuses_fse")

_L = {
    "titre": {"fr": "Versements des caisses au budget de l'État (tableau A des lois de finances), "
                    "1985-2005",
              "ar": "مساهمات الصناديق في ميزانية الدولة (الجدول أ لقوانين المالية)، 1985-2005"},
    "st_composantes": {"fr": "Prévisions des lois de finances, millions de dinars courants",
                       "ar": "تقديرات قوانين المالية، بملايين الدنانير الجارية"},
    "st_pib": {"fr": "Total des versements prévus, % du PIB",
               "ar": "جملة المساهمات المقدّرة، % من الناتج المحلي الإجمالي"},
    "vue_composantes": {"fr": "Composantes puis agrégat", "ar": "المكوّنات ثم المجمّع"},
    "vue_pib": {"fr": "Total, % du PIB", "ar": "الجملة، % من الناتج"},
    "forfait_hospitalier_cnss": {"fr": "Forfait hospitalier CNSS",
                                 "ar": "المساهمة الاستشفائية للصندوق الوطني للضمان الاجتماعي"},
    "forfait_hospitalier_cnrps": {"fr": "Forfait hospitalier CNRPS",
                                  "ar": "المساهمة الاستشفائية للصندوق الوطني للتقاعد والحيطة"},
    "familles_necessiteuses_fse": {"fr": "Familles nécessiteuses + FSE 0,5 %",
                                   "ar": "العائلات المعوزة + المساهمة 0,5 %"},
    "agregat_caisses": {"fr": "Versements et contributions des caisses (ligne agrégée)",
                        "ar": "مساهمات ومشاركات الصناديق (سطر مجمّع)"},
    "total": {"fr": "Total des versements", "ar": "جملة المساهمات"},
    "rupture": {"fr": "détail →\nagrégat", "ar": "تفصيل →\nمجمّع"},
    "ib_comp": {"fr": "{grandeur}, {a} : {v} MD", "ar": "{grandeur}، {a}: {v} م.د"},
    "ib_total": {"fr": "Total, {a} : {v} MD", "ar": "الجملة، {a}: {v} م.د"},
    "ib_pib": {"fr": "{a} : {v} % du PIB", "ar": "{a}: {v} % من الناتج"},
    "col_annee": {"fr": "Gestion", "ar": "التصرّف"},
    "col_forfait_hospitalier_cnss": {"fr": "Forfait hospitalier CNSS (MD)",
                                     "ar": "المساهمة الاستشفائية للـCNSS (م.د)"},
    "col_forfait_hospitalier_cnrps": {"fr": "Forfait hospitalier CNRPS (MD)",
                                      "ar": "المساهمة الاستشفائية للـCNRPS (م.د)"},
    "col_familles_necessiteuses_fse": {"fr": "Familles nécessiteuses + FSE (MD)",
                                       "ar": "العائلات المعوزة + المساهمة 0,5 % (م.د)"},
    "col_agregat": {"fr": "Agrégat caisses (MD)", "ar": "مجمّع الصناديق (م.د)"},
    "col_total": {"fr": "Total des versements (MD)", "ar": "جملة المساهمات (م.د)"},
    "col_pib": {"fr": "Total, % du PIB", "ar": "الجملة، % من الناتج"},
    "col_cle": {"fr": "Loi de finances", "ar": "قانون المالية"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _d():
    return figtools.series(SERIE)


def _pib() -> dict[int, float]:
    import pandas as pd
    return {int(r.annee): float(r.pib_minfin_MDT)
            for r in figtools.series(SERIE_PIB).itertuples() if not pd.isna(r.pib_minfin_MDT)}


def _par_annee() -> dict[int, dict]:
    """{année: {poste: MD, 'total': MD, 'cle': …}}."""
    d = _d()
    out: dict[int, dict] = {}
    for r in d.itertuples():
        a = int(r.annee)
        rec = out.setdefault(a, {"total": float(r.total_caisses_md), "cle": str(r.cle)})
        rec[str(r.poste)] = float(r.montant_md)
    return out


def fig_vue(vue: str = "composantes"):
    """Une vue : "composantes" (empilement des trois lignes, puis agrégat, MD courants) ou
    "pib" (total des versements prévus en % du PIB retenu par le ministère des Finances)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9, 5.2))
    data = _par_annee()
    annees = sorted(data)

    if vue == "composantes":
        couleurs = {"forfait_hospitalier_cnss": BLEU, "forfait_hospitalier_cnrps": VERT,
                    "familles_necessiteuses_fse": ORANGE}
        vus: set[str] = set()
        for a in annees:
            rec = data[a]
            if "agregat_caisses" in rec:
                lab = _lab("agregat_caisses")
                b = ax.bar(a, rec["agregat_caisses"], color=GRIS, width=0.8,
                           label=ft(lab) if "agregat_caisses" not in vus else None)
                vus.add("agregat_caisses")
                figtools.infobulle(b[0], _lab("ib_comp").format(
                    grandeur=ft(_lab("agregat_caisses")), a=a,
                    v=_nombre(rec["agregat_caisses"])))
            else:
                bas = 0.0
                for poste in COMPOSANTES:
                    if poste not in rec:
                        continue
                    v = rec[poste]
                    b = ax.bar(a, v, bottom=bas, color=couleurs[poste], width=0.8,
                               label=ft(_lab(poste)) if poste not in vus else None)
                    vus.add(poste)
                    figtools.infobulle(b[0], _lab("ib_comp").format(
                        grandeur=ft(_lab(poste)), a=a, v=_nombre(v)))
                    bas += v
            ax.annotate(_nombre(rec["total"], 0), xy=(a, rec["total"]),
                        xytext=(0, 3), textcoords="offset points", ha="center",
                        va="bottom", fontsize=6.5, color="#24292f")
        ax.set_ylabel(ft(_lab("st_composantes")), fontsize=8)
    elif vue == "pib":
        pib = _pib()
        xs, ys = [], []
        for a in annees:
            if a not in pib:
                continue
            y = 100 * data[a]["total"] / pib[a]
            xs.append(a)
            ys.append(y)
        for seg in (_segment(xs, lambda a: a < RUPTURE), _segment(xs, lambda a: a >= RUPTURE)):
            if not seg:
                continue
            sx = seg
            sy = [ys[xs.index(a)] for a in sx]
            ax.plot(sx, sy, "-o", color=BLEU, lw=1.6, ms=4.5)
        for a, y in zip(xs, ys):
            p, = ax.plot([a], [y], "o", color=BLEU, ms=4.5)
            figtools.infobulle(p, _lab("ib_pib").format(a=a, v=_nombre(y, 3)))
        ax.set_ylabel(ft(_lab("st_pib")), fontsize=8)
    else:
        raise ValueError(vue)

    ax.set_xlim(annees[0] - 0.7, annees[-1] + 0.7)
    ax.set_xticks([a for a in annees if a % 2 == 1])
    ax.tick_params(axis="x", labelsize=8, rotation=45)
    ax.tick_params(axis="y", labelsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    figtools.marque_rupture(ax, RUPTURE, texte=_lab("rupture"))
    if ax.get_legend_handles_labels()[0]:
        ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.suptitle(_lignes("titre") + "\n" + _lignes(f"st_{vue}"), fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.98))
    return fig


def _segment(annees: list[int], garde) -> list[int]:
    return sorted(a for a in annees if garde(a))


def vues() -> list[tuple[str, object]]:
    return [(_lab(f"vue_{v}"), fig_vue(v)) for v in VUES]


def table():
    import pandas as pd
    data = _par_annee()
    pib = _pib()
    lignes = []
    for a in sorted(data):
        rec = data[a]
        lignes.append({
            _lab("col_annee"): a,
            _lab("col_forfait_hospitalier_cnss"):
                round(rec["forfait_hospitalier_cnss"], 1)
                if "forfait_hospitalier_cnss" in rec else None,
            _lab("col_forfait_hospitalier_cnrps"):
                round(rec["forfait_hospitalier_cnrps"], 1)
                if "forfait_hospitalier_cnrps" in rec else None,
            _lab("col_familles_necessiteuses_fse"):
                round(rec["familles_necessiteuses_fse"], 1)
                if "familles_necessiteuses_fse" in rec else None,
            _lab("col_agregat"):
                round(rec["agregat_caisses"], 1) if "agregat_caisses" in rec else None,
            _lab("col_total"): round(rec["total"], 1),
            _lab("col_pib"): round(100 * rec["total"] / pib[a], 3) if a in pib else None,
            _lab("col_cle"): rec["cle"],
        })
    return pd.DataFrame(lignes)
