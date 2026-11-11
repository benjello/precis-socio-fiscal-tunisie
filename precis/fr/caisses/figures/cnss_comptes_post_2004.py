"""Figure « comptes de la CNSS après 2004, 2005-2023 » (produits/charges techniques, solde).

    from figures import cnss_comptes_post_2004 as cp
    cp.fig_vue("flux")        # produits et charges techniques, MD courants, 2000-2021
    cp.fig_vue("solde")       # solde technique (R−D) et résultat de l'exercice, MD courants
    cp.fig_vue("solde_pib")   # résultat de l'exercice, % du PIB
    cp.vues()                 # les trois, pour figtools.figure_tabs
    cp.table()                # format long, une ligne par année 2000-2023

D'OÙ VIENNENT LES DONNÉES. Deux séries snapshotées dans `precis/_seriescache/` :
`cnss-produits-charges-techniques` (produits techniques R et charges techniques D, tous régimes
gérés par la CNSS, MD courants, 2000-2020, prolongée 2021 pour les produits) et
`cnss-resultat-exercice` (résultat de l'exercice de la caisse, lacunaire, 2009-2023 ; une ligne
par (année, source), valeur retenue = colonne `retenu`). Le PIB au dénominateur est celui que
retient le ministère des Finances (série `irpp-ratios`).

LE SOLDE TECHNIQUE N'EST PAS LE RÉSULTAT. R − D est le solde technique : il ignore les frais de
gestion, les provisions et les placements. Le résultat de l'exercice, lui, en tient compte, et
s'en écarte de plusieurs dizaines à plusieurs centaines de millions de dinars. Les deux grandeurs
sont tracées côte à côte, dans des couleurs distinctes, et jamais présentées l'une pour l'autre.

TROUS HONNÊTES, jamais interpolés : les charges techniques manquent pour 2000-2008, 2011 et 2014 ;
le résultat de l'exercice pour 2005-2008, 2011 et 2014 (aucune source lue). Ces années ne sont pas
tracées. Les points 2009-2010 et 2015 du résultat viennent d'un budget (« موازنة الصندوق »), non
d'un bilan : marqueurs évidés, signalés « budget ». Le point 2023 est provisoire.

RUPTURE DE CHAMP CNAM (2006). À partir de 2006, les branches maladie et accidents du travail
passent à la CNAM (loi n° 2004-71, décret n° 2005-321, application par étapes à partir du 1er
juillet 2007) : les produits techniques de la CNSS n'en portent plus la part. Les deux tronçons
ne couvrent pas le même champ ; la rupture est marquée, jamais raccordée en silence.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_PC = "cnss-produits-charges-techniques"
SERIE_RES = "cnss-resultat-exercice"
SERIE_PIB = "irpp-ratios"
RUPTURE = 2006  # champ CNAM : branches maladie et AT-MP transférées
VUES = ("flux", "solde", "solde_pib")

BLEU, ORANGE, VERT, GRIS = "#08519c", "#bc4c00", "#1a7f37", "#6e7781"

_L = {
    "titre": {"fr": "Comptes de la CNSS après 2004, 2005-2023",
              "ar": "حسابات الصندوق الوطني للضمان الاجتماعي بعد 2004، 2005-2023"},
    "st_flux": {"fr": "Produits et charges techniques, tous régimes, millions de dinars courants",
                "ar": "المنتوجات والأعباء الفنية، كلّ الأنظمة، بملايين الدنانير الجارية"},
    "st_solde": {"fr": "Solde technique (produits − charges) et résultat de l'exercice, "
                       "millions de dinars courants",
                 "ar": "الرصيد الفني (المنتوجات − الأعباء) ونتيجة السنة المحاسبية، "
                       "بملايين الدنانير الجارية"},
    "st_solde_pib": {"fr": "Résultat de l'exercice, % du PIB",
                     "ar": "نتيجة السنة المحاسبية، % من الناتج المحلي الإجمالي"},
    "vue_flux": {"fr": "Produits et charges", "ar": "المنتوجات والأعباء"},
    "vue_solde": {"fr": "Solde technique et résultat", "ar": "الرصيد الفني والنتيجة"},
    "vue_solde_pib": {"fr": "Résultat, % du PIB", "ar": "النتيجة، % من الناتج"},
    "produits": {"fr": "Produits techniques", "ar": "المنتوجات الفنية"},
    "charges": {"fr": "Charges techniques", "ar": "الأعباء الفنية"},
    "solde_tech": {"fr": "Solde technique (produits − charges)",
                   "ar": "الرصيد الفني (المنتوجات − الأعباء)"},
    "resultat": {"fr": "Résultat de l'exercice", "ar": "نتيجة السنة المحاسبية"},
    "rupture": {"fr": "champ\nCNAM", "ar": "مجال\nالتأمين على المرض"},
    "lg_budget": {"fr": "Point évidé : solde d'un budget, non d'un bilan (2009, 2010, 2015), "
                        "ou provisoire (2023)",
                  "ar": "نقطة مفرّغة: رصيد من موازنة لا من حساب ختامي (2009، 2010، 2015)، "
                        "أو وقتي (2023)"},
    "ib_flux": {"fr": "{grandeur}, {a} : {v} MD", "ar": "{grandeur}، {a}: {v} م.د"},
    "ib_solde": {"fr": "{grandeur}, {a} : {v} MD{st}", "ar": "{grandeur}، {a}: {v} م.د{st}"},
    "ib_solde_pib": {"fr": "{a} : {v} % du PIB{st}", "ar": "{a}: {v} % من الناتج{st}"},
    "st_budget": {"fr": " (budget)", "ar": " (موازنة)"},
    "st_prov": {"fr": " (provisoire)", "ar": " (وقتي)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_produits": {"fr": "Produits techniques (MD)", "ar": "المنتوجات الفنية (م.د)"},
    "col_charges": {"fr": "Charges techniques (MD)", "ar": "الأعباء الفنية (م.د)"},
    "col_solde_tech": {"fr": "Solde technique, produits − charges (MD)",
                       "ar": "الرصيد الفني، المنتوجات − الأعباء (م.د)"},
    "col_resultat": {"fr": "Résultat de l'exercice (MD)",
                     "ar": "نتيجة السنة المحاسبية (م.د)"},
    "col_statut": {"fr": "Statut du résultat", "ar": "حالة النتيجة"},
    "col_resultat_pib": {"fr": "Résultat (% du PIB)", "ar": "النتيجة (% من الناتج)"},
    "col_pib": {"fr": "PIB, ministère des Finances (MD)",
                "ar": "الناتج المحلي الإجمالي، وزارة المالية (م.د)"},
    "statut_realise": {"fr": "réalisé", "ar": "منجَز"},
    "statut_budget": {"fr": "budget (fragile)", "ar": "موازنة (هشّ)"},
    "statut_provisoire": {"fr": "provisoire", "ar": "وقتي"},
    "statut_trou": {"fr": "aucune source lue", "ar": "لا مصدر مقروء"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _pc() -> dict[int, tuple[float | None, float | None]]:
    """{année: (produits techniques, charges techniques|None)} en MD."""
    import pandas as pd
    out = {}
    for r in figtools.series(SERIE_PC).itertuples():
        a = int(r.annee)
        p = None if pd.isna(r.produits_techniques_MD) else float(r.produits_techniques_MD)
        c = None if pd.isna(r.charges_techniques_MD) else float(r.charges_techniques_MD)
        out[a] = (p, c)
    return out


def _resultat() -> dict[int, tuple[float, str]]:
    """{année: (résultat retenu en MD, statut)} — valeur retenue, trous exclus."""
    import pandas as pd
    out = {}
    for r in figtools.series(SERIE_RES).itertuples():
        if not bool(r.retenu) or pd.isna(r.resultat_MD):
            continue
        a = int(r.annee)
        assert a not in out, f"deux valeurs retenues pour {a}"
        out[a] = (float(r.resultat_MD), str(r.statut))
    return out


def _pib() -> dict[int, float]:
    import pandas as pd
    return {int(r.annee): float(r.pib_minfin_MDT)
            for r in figtools.series(SERIE_PIB).itertuples() if not pd.isna(r.pib_minfin_MDT)}


def _segments(annees: list[int]) -> list[list[int]]:
    """Découpe une liste d'années en tronçons d'années consécutives (les trous coupent)."""
    annees = sorted(annees)
    out, cur = [], []
    for a in annees:
        if cur and a != cur[-1] + 1:
            out.append(cur)
            cur = []
        cur.append(a)
    if cur:
        out.append(cur)
    return out


def _trace_points(ax, serie: dict[int, float], couleur: str, label: str, ib_key: str,
                  grandeur: str = "", pib: dict | None = None,
                  statut: dict[int, str] | None = None):
    """Trace une grandeur en segments d'années consécutives, un point (et une infobulle) par
    année ; marqueur évidé pour un point « budget » ou « provisoire »."""
    ft = figtools.fig_text
    premier = True
    for seg in _segments(list(serie)):
        xs = seg
        ys = [100 * serie[a] / pib[a] if pib is not None else serie[a] for a in seg]
        ax.plot(xs, ys, "-", color=couleur, lw=1.6,
                label=ft(label) if premier else None, zorder=2)
        premier = False
        for a, y in zip(xs, ys):
            s = statut.get(a, "realise") if statut else "realise"
            evide = s in ("budget", "provisoire")
            p, = ax.plot([a], [y], "o", color=couleur, ms=4.5,
                         mfc="white" if evide else couleur, zorder=3)
            v_aff = y if pib is not None else serie[a]
            dec = 2 if pib is not None else 1
            st = {"budget": _lab("st_budget"), "provisoire": _lab("st_prov")}.get(s, "")
            texte = _lab(ib_key).format(a=a, v=_nombre(v_aff, dec),
                                        grandeur=ft(grandeur), st=st)
            figtools.infobulle(p, texte)


def fig_vue(vue: str = "flux"):
    """Une vue : "flux" (produits et charges techniques, MD), "solde" (solde technique R−D et
    résultat de l'exercice, MD) ou "solde_pib" (résultat de l'exercice, % du PIB)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9, 5.2))
    pc = _pc()
    res = _resultat()
    res_val = {a: v for a, (v, _) in res.items()}
    res_statut = {a: s for a, (_, s) in res.items()}

    if vue == "flux":
        produits = {a: p for a, (p, _) in pc.items() if p is not None}
        charges = {a: c for a, (_, c) in pc.items() if c is not None}
        _trace_points(ax, produits, BLEU, "produits", "ib_flux", grandeur="produits")
        _trace_points(ax, charges, ORANGE, "charges", "ib_flux", grandeur="charges")
        figtools.marque_rupture(ax, RUPTURE, texte=_lab("rupture"))
        ans = sorted(produits)
    elif vue == "solde":
        ax.axhline(0, color="#57606a", lw=0.8)
        solde_tech = {a: p - c for a, (p, c) in pc.items()
                      if p is not None and c is not None}
        _trace_points(ax, solde_tech, VERT, "solde_tech", "ib_solde", grandeur="solde_tech")
        _trace_points(ax, res_val, BLEU, "resultat", "ib_solde", grandeur="resultat",
                      statut=res_statut)
        ans = sorted(set(solde_tech) | set(res_val))
    elif vue == "solde_pib":
        ax.axhline(0, color="#57606a", lw=0.8)
        pib = _pib()
        _trace_points(ax, res_val, BLEU, "resultat", "ib_solde_pib", pib=pib,
                      statut=res_statut)
        ans = sorted(res_val)
    else:
        raise ValueError(vue)

    ax.set_xlim(ans[0] - 0.7, ans[-1] + 0.7)
    ax.set_xticks([a for a in ans if a % 2 == 1])
    ax.tick_params(axis="x", labelsize=8, rotation=45)
    ax.tick_params(axis="y", labelsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    poignees = ax.get_legend_handles_labels()[0]
    if vue != "flux":
        poignees.append(Line2D([], [], color=GRIS, marker="o", lw=0, mfc="white",
                               label=ft(_lab("lg_budget"))))
    ax.legend(handles=poignees, loc="best", fontsize=8, frameon=False)
    fig.suptitle(_lignes("titre") + "\n" + _lignes(f"st_{vue}"), fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.98))
    return fig


def vues() -> list[tuple[str, object]]:
    """Les trois vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{v}"), fig_vue(v)) for v in VUES]


def table():
    import pandas as pd
    pc = _pc()
    res = _resultat()
    pib = _pib()
    annees = sorted(set(pc) | set(res))
    lignes = []
    for a in annees:
        p, c = pc.get(a, (None, None))
        solde = (p - c) if (p is not None and c is not None) else None
        if a in res:
            rv, rs = res[a]
        else:
            rv, rs = None, ("trou" if a in (2005, 2006, 2007, 2008, 2011, 2014) else None)
        lignes.append({
            _lab("col_annee"): a,
            _lab("col_produits"): round(p, 1) if p is not None else None,
            _lab("col_charges"): round(c, 1) if c is not None else None,
            _lab("col_solde_tech"): round(solde, 1) if solde is not None else None,
            _lab("col_resultat"): round(rv, 1) if rv is not None else None,
            _lab("col_statut"): _lab(f"statut_{rs}") if rs else None,
            _lab("col_resultat_pib"): round(100 * rv / pib[a], 2)
            if (rv is not None and a in pib) else None,
            _lab("col_pib"): round(pib[a], 1) if a in pib else None,
        })
    return pd.DataFrame(lignes)
