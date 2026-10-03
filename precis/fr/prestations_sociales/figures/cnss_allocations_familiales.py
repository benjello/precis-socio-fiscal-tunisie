"""Figure « allocations familiales versées par la CNSS, 1990-2004 » (source CNSS).

    from figures import cnss_allocations_familiales as caf
    caf.fig_allocations()   # composantes en MD courants, total en MD constants de 1990
    caf.table()             # les montants de la figure (onglet Données)

D'OÙ VIENNENT LES DONNÉES. La Rétrospective financière 1990-2004 de la CNSS (série
`cnss-retrospective-ressources-emplois` de tunisia-data), comptabilité des « Bilans », en
milliers de dinars courants convertis en millions :
  - page 14 : branche des prestations familiales du régime des salariés non agricoles
    (allocations familiales, majoration pour salaire unique) ;
  - pages 28 et 20 : allocations familiales du régime agricole amélioré et du régime des
    étudiants. Avec la page 14, elles composent exactement les allocations familiales de
    l'ensemble des régimes (page 60) ; la majoration pour salaire unique n'est servie, en
    montants significatifs, que par le régime non agricole ;
  - page 15 : la ligne « Allocation famil. + Sal. unique » de la branche des pensions du
    régime non agricole, servie aux pensionnés et imputée sur cette branche jusqu'en 1994,
    nulle ensuite ;
  - page 58 : les allocations familiales de la convention tuniso-française.
Les congés de naissance (0,1 MD par an au plus) et les actions sociales de la branche ne sont
pas des allocations et ne sont pas tracés.

LE DÉFLATEUR. L'indice général des prix à la consommation familiale de l'INS, base 100 en
1970, lu dans les annuaires statistiques (série `ins-annuaire-ipc`, lignes retenues), ramené
à 1990. Le document de la CNSS ne compte ni les allocataires ni les enfants : le total
déflaté mesure la dépense, non le montant par enfant.

LES COLONNES MASQUÉES. Comme pour toutes les figures tirées de ce document, une cellule que la
reliure masque porte une estimation provisoire ; l'année est alors hachurée (barres) et creuse
(courbe), et la table laisse la valeur publiée vide en donnant l'estimation à part.
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
SERIE_PRIX = "ins-annuaire-ipc"
ANNEE_BASE = 1990

BLEU, ORANGE, GRIS, VERT, VIOLET = "#08519c", "#bc4c00", "#6e7781", "#1a7f37", "#8250df"
BLEU_CLAIR = "#6baed6"

# (nom, [(page, régime attendu, clé)], couleur), dans l'ordre d'empilement.
_COMPOSANTES = (
    ("af_rsna", [(14, "RSNA", "allocations_familiales")], BLEU),
    ("af_autres", [(28, "RSAA", "allocations_familiales"),
                   (20, "ETUD", "allocations_familiales")], VERT),
    ("msu", [(14, "RSNA", "majorations_salaire_unique"),
             (20, "ETUD", "majorations_salaire_unique")], BLEU_CLAIR),
    ("af_pensionnes", [(15, "RSNA", "allocations_familiales_su")], VIOLET),
    ("af_ctf", [(58, "CTF", "prestations_especes_af")], GRIS),
)

_L = {
    "titre": {"fr": "Allocations familiales et majoration pour salaire unique versées par "
                    "la CNSS, 1990-2004",
              "ar": "المنح العائلية والزيادة بعنوان الأجر الوحيد التي صرفها الصندوق الوطني "
                    "للضمان الاجتماعي، 1990-2004"},
    "y": {"fr": "Millions de dinars (barres : courants ; courbe : constants de 1990)",
          "ar": "بملايين الدنانير (الأعمدة: جارية؛ المنحنى: ثابتة لسنة 1990)"},
    "x": {"fr": "Année", "ar": "السنة"},
    "af_rsna": {"fr": "Allocations familiales, régime des salariés non agricoles",
                "ar": "المنح العائلية، نظام الأجراء غير الفلاحيين"},
    "af_autres": {"fr": "Allocations familiales, régime agricole amélioré et étudiants",
                  "ar": "المنح العائلية، النظام الفلاحي المحسّن والطلبة"},
    "msu": {"fr": "Majoration pour salaire unique",
            "ar": "الزيادة بعنوان الأجر الوحيد"},
    "af_pensionnes": {"fr": "Allocations familiales et salaire unique des pensionnés, "
                            "imputées sur la branche des pensions jusqu'en 1994",
                      "ar": "المنح العائلية والأجر الوحيد للمتقاعدين، المحمولة على فرع "
                            "الجرايات إلى سنة 1994"},
    "af_ctf": {"fr": "Allocations familiales, convention tuniso-française",
               "ar": "المنح العائلية، الاتفاقية التونسية الفرنسية"},
    "reel": {"fr": "Total en dinars constants de 1990",
             "ar": "المجموع بالدينار الثابت لسنة 1990"},
    "estime": {"fr": "{annees} : valeur en partie estimée (reliure du document)",
               "ar": "{annees}: قيمة مقدّرة جزئياً (تجليد الوثيقة)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_total": {"fr": "Total, dinars courants (MD)", "ar": "المجموع، بالدينار الجاري (م.د)"},
    "col_indice": {"fr": "Indice des prix, base 100 en 1990",
                   "ar": "الرقم القياسي للأسعار، أساس 100 سنة 1990"},
    "col_reel": {"fr": "Total, dinars constants de 1990 (MD)",
                 "ar": "المجموع، بالدينار الثابت لسنة 1990 (م.د)"},
    "col_estimations": {"fr": "Estimations provisoires (MD)", "ar": "تقديرات مؤقّتة (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _cellules():
    """{(page, clé, année): (MD, estimé ?)}, après contrôle du régime de chaque page."""
    import pandas as pd
    d = figtools.series(SERIE)
    pages = {p for _, refs, _ in _COMPOSANTES for p, _, _ in refs}
    d = d[d["page"].isin(pages)]
    attendu = {p: r for _, refs, _ in _COMPOSANTES for p, r, _ in refs}
    for p, r in attendu.items():
        assert set(d.loc[d["page"] == p, "regime"]) == {r}, f"page {p} : régime {r} attendu"
    return {(int(r.page), r.cle, int(r.annee)): (float(r.valeur_ou_estimation) / 1000,
                                                  bool(pd.isna(r.valeur)))
            for r in d.itertuples() if not pd.isna(r.valeur_ou_estimation)}


def _donnees():
    """{composante: {année: (MD, estimé ?)}} ; une cellule absente (régime pas encore
    institué) vaut zéro, publiée."""
    c = _cellules()
    annees = sorted({a for _, _, a in c})
    out = {}
    for nom, refs, _ in _COMPOSANTES:
        out[nom] = {}
        for a in annees:
            vals = [c.get((p, k, a), (0.0, False)) for p, _, k in refs]
            out[nom][a] = (sum(v for v, _ in vals), any(e for _, e in vals))
    return out


def _indice() -> dict[int, float]:
    """IPC annuel ramené à 100 en ANNEE_BASE (lignes retenues des annuaires de l'INS)."""
    d = figtools.series(SERIE_PRIX)
    d = d[d["retenu"] == "oui"]
    ipc = {int(r.annee): float(r.indice_base1970) for r in d.itertuples()}
    return {a: 100 * v / ipc[ANNEE_BASE] for a, v in ipc.items()}


def _totaux():
    g = _donnees()
    ind = _indice()
    ans = sorted(g[_COMPOSANTES[0][0]])
    tot = {a: (sum(g[n][a][0] for n, _, _ in _COMPOSANTES),
               any(g[n][a][1] for n, _, _ in _COMPOSANTES)) for a in ans}
    return g, ind, ans, tot


def table():
    import pandas as pd
    g, ind, ans, tot = _totaux()
    lignes = []
    for a in ans:
        ligne = {_lab("col_annee"): a}
        estimes = []
        for nom, _, _ in _COMPOSANTES:
            v, est = g[nom][a]
            ligne[_lab(nom) + " (MD)"] = None if est else round(v, 2)
            if est:
                estimes.append(f"{_lab(nom)} : {_nombre(v, 2)}")
        v, est = tot[a]
        ligne[_lab("col_total")] = None if est else round(v, 2)
        ligne[_lab("col_indice")] = round(ind[a], 1)
        ligne[_lab("col_reel")] = None if est else round(100 * v / ind[a], 2)
        if est:
            estimes.append(f"{_lab('col_total').split(',')[0]} : {_nombre(v, 2)} ; "
                           f"{_lab('col_reel').split(' (')[0]} : {_nombre(100 * v / ind[a], 2)}")
        ligne[_lab("col_estimations")] = " ; ".join(estimes)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def fig_allocations():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g, ind, ans, tot = _totaux()
    fig, ax = plt.subplots(figsize=(9.5, 6.4))

    bas = {a: 0.0 for a in ans}
    poignees = []
    for nom, _, couleur in _COMPOSANTES:
        for a in ans:
            v, est = g[nom][a]
            if v:
                ax.bar(a, v, bottom=bas[a], width=0.72, color=couleur,
                       hatch="////" if est else None, edgecolor="white", lw=0.4)
            bas[a] += v
        poignees.append(Patch(color=couleur, label=ft(_lab(nom))))

    reel = {a: 100 * tot[a][0] / ind[a] for a in ans}
    ax.plot(ans, [reel[a] for a in ans], "-", color=ORANGE, lw=2)
    for a in ans:
        ax.plot([a], [reel[a]], "o", color=ORANGE, ms=4.5,
                mfc="white" if tot[a][1] else ORANGE)
    poignees.append(Line2D([], [], color=ORANGE, marker="o", lw=2, label=ft(_lab("reel"))))
    for a in (ans[0], ans[-1]):
        ax.annotate(_nombre(tot[a][0]), (a, tot[a][0]), textcoords="offset points",
                    xytext=(0, 4), ha="center", fontsize=8, color="#24292f")
        if a != ANNEE_BASE:  # l'année de base : même montant que la barre
            ax.annotate(_nombre(reel[a]), (a, reel[a]), textcoords="offset points",
                        xytext=(0, -13), ha="center", fontsize=8, color=ORANGE)
    estimees = [a for a in ans if tot[a][1]]
    if estimees:
        poignees.append(Patch(facecolor="white", edgecolor=GRIS, hatch="////",
                              label=ft(_lab("estime").format(
                                  annees=", ".join(map(str, estimees))))))

    ax.set_ylim(0, max(v for v, _ in tot.values()) * 1.15)
    ax.set_xticks(ans)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=1,
              fontsize=8, frameon=False)
    fig.tight_layout()
    return fig
