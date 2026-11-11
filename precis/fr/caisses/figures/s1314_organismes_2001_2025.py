"""Figure « comptes des organismes de sécurité sociale (S1314), 2001-2025 » (source INS).

    from figures import s1314_organismes_2001_2025 as og
    og.fig_vue("flux")        # cotisations reçues vs prestations versées, MD courants
    og.fig_vue("solde")       # capacité (+) / besoin (-) de financement, MD courants
    og.fig_vue("solde_pib")   # capacité / besoin de financement, % du PIB
    og.fig_vue("transferts")  # transferts courants entre APU, reçus et versés, MD courants
    og.vues()                 # les quatre, pour figtools.figure_tabs
    og.table()                # format long, une ligne par année

D'OÙ VIENNENT LES DONNÉES. Le tableau « Comptes des organismes de sécurité sociale » (secteur
S1314, administrations de sécurité sociale) des éditions des comptes de la nation de l'INS,
série `ins-comptes-organismes-securite-sociale` de tunisia-data, snapshotée dans
`precis/_seriescache/`. Vue « série retenue » : une valeur par année, arbitrage « édition la
plus récente dans sa base ». Comptes consolidés de l'ensemble du sous-secteur, SANS ventilation
par caisse (CNSS/CNRPS/CNAM) ni par branche. Grandeurs ici tracées, en millions de dinars
courants : cotisations sociales reçues (ressources), prestations sociales versées (emplois ;
« prestations sociales » en base 1983 jusqu'en 2004, « prestations sociales en espèces » ensuite),
transferts courants entre administrations publiques reçus (ressources) et versés (emplois),
capacité (+) ou besoin (−) de financement (emplois).

DEUX SEGMENTS, JAMAIS RACCORDÉS. Base 1983 (années 2001-2014) et base 2015 (années 2015-2025) :
chaque segment est tracé séparément, sans trait de jonction entre 2014 et 2015, et la rupture de
base est marquée. Sur 2015-2017, la note de concordance de la série montre que cotisations,
prestations en espèce et capacité de financement sont quasi identiques d'une base à l'autre ; la
rupture n'est pas corrigée pour autant. Les transferts courants entre APU ne sont isolés qu'à
partir de 2005 (versés) et 2006 (reçus) : avant, les éditions base 1983 les fondent dans « autres
transferts courants ». Le PIB au dénominateur est celui que retient le ministère des Finances
(série `irpp-ratios`). 2024 est semi-définitif, 2025 provisoire.
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

SERIE = "ins-comptes-organismes-securite-sociale"
SERIE_PIB = "irpp-ratios"
RUPTURE = 2015  # base 1983 (2001-2014) → base 2015 (2015-2025)
VUES = ("flux", "solde", "solde_pib", "transferts")

BLEU, ORANGE, VERT, GRIS = "#08519c", "#bc4c00", "#1a7f37", "#6e7781"

# Intitulés de l'opération à retenir, d'une édition à l'autre (la nomenclature change au sein
# même de la base 1983, à partir de l'édition 2005-2009).
OPS = {
    "cotisations": ("ressources", ("Cotisations sociales",)),
    "prestations": ("emplois", ("Prestations sociales", "Prestations sociales en espece")),
    "solde": ("emplois", ("Capacité (+) ou besoin (-) de financement",
                          "Capacité + ou besoin - de financement",
                          "Capacité ou besoin de financement")),
    "transf_recus": ("ressources", ("Transferts courants entre admini. publiques",)),
    "transf_verses": ("emplois", ("Transferts courants entre admini. publiques",)),
}

_L = {
    "titre": {"fr": "Comptes des organismes de sécurité sociale (secteur S1314), 2001-2025",
              "ar": "حسابات هياكل الضمان الاجتماعي (القطاع S1314)، 2001-2025"},
    "st_flux": {"fr": "Cotisations reçues et prestations versées, millions de dinars courants",
                "ar": "المساهمات المقبوضة والمنافع المصروفة، بملايين الدنانير الجارية"},
    "st_solde": {"fr": "Capacité (+) ou besoin (−) de financement, millions de dinars courants",
                 "ar": "القدرة (+) أو الحاجة (−) للتمويل، بملايين الدنانير الجارية"},
    "st_solde_pib": {"fr": "Capacité (+) ou besoin (−) de financement, % du PIB",
                     "ar": "القدرة (+) أو الحاجة (−) للتمويل، % من الناتج المحلي الإجمالي"},
    "st_transferts": {"fr": "Transferts courants entre administrations publiques, "
                            "millions de dinars courants",
                      "ar": "التحويلات الجارية بين الإدارات العمومية، بملايين الدنانير الجارية"},
    "vue_flux": {"fr": "Cotisations et prestations", "ar": "المساهمات والمنافع"},
    "vue_solde": {"fr": "Solde, millions de dinars", "ar": "الرصيد، بملايين الدنانير"},
    "vue_solde_pib": {"fr": "Solde, % du PIB", "ar": "الرصيد، % من الناتج"},
    "vue_transferts": {"fr": "Transferts entre administrations publiques",
                       "ar": "التحويلات بين الإدارات العمومية"},
    "cotisations": {"fr": "Cotisations reçues", "ar": "المساهمات المقبوضة"},
    "prestations": {"fr": "Prestations versées", "ar": "المنافع المصروفة"},
    "transf_recus": {"fr": "Transferts reçus", "ar": "التحويلات المقبوضة"},
    "transf_verses": {"fr": "Transferts versés", "ar": "التحويلات المصروفة"},
    "rupture": {"fr": "base des\ncomptes", "ar": "أساس\nالحسابات"},
    "lg_provisoire": {"fr": "2024 semi-définitif, 2025 provisoire (points évidés)",
                      "ar": "2024 شبه نهائي، 2025 وقتي (نقاط مفرّغة)"},
    "ib_flux": {"fr": "{grandeur}, {a} : {v} MD{st}", "ar": "{grandeur}، {a}: {v} م.د{st}"},
    "ib_solde": {"fr": "{a} : {v} MD{st}", "ar": "{a}: {v} م.د{st}"},
    "ib_solde_pib": {"fr": "{a} : {v} % du PIB{st}", "ar": "{a}: {v} % من الناتج{st}"},
    "st_semidef": {"fr": " (semi-définitif)", "ar": " (شبه نهائي)"},
    "st_prov": {"fr": " (provisoire)", "ar": " (وقتي)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_base": {"fr": "Base des comptes", "ar": "أساس الحسابات"},
    "col_statut": {"fr": "Statut du compte", "ar": "حالة الحساب"},
    "col_cotisations": {"fr": "Cotisations reçues (MD)", "ar": "المساهمات المقبوضة (م.د)"},
    "col_prestations": {"fr": "Prestations versées (MD)", "ar": "المنافع المصروفة (م.د)"},
    "col_solde": {"fr": "Capacité (+) / besoin (−) de financement (MD)",
                  "ar": "القدرة (+) / الحاجة (−) للتمويل (م.د)"},
    "col_solde_pib": {"fr": "Capacité / besoin (% du PIB)",
                      "ar": "القدرة / الحاجة (% من الناتج)"},
    "col_transf_recus": {"fr": "Transferts entre APU reçus (MD)",
                         "ar": "التحويلات بين الإدارات العمومية المقبوضة (م.د)"},
    "col_transf_verses": {"fr": "Transferts entre APU versés (MD)",
                          "ar": "التحويلات بين الإدارات العمومية المصروفة (م.د)"},
    "col_pib": {"fr": "PIB, ministère des Finances (MD)",
                "ar": "الناتج المحلي الإجمالي، وزارة المالية (م.د)"},
    "base_1983": {"fr": "base 1983", "ar": "أساس 1983"},
    "base_2015": {"fr": "base 2015", "ar": "أساس 2015"},
    "statut_definitif": {"fr": "définitif", "ar": "نهائي"},
    "statut_semi_definitif": {"fr": "semi-définitif", "ar": "شبه نهائي"},
    "statut_provisoire": {"fr": "provisoire", "ar": "وقتي"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0  # ni « -0,00 » ni « -0,0 »
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _grandeur(key: str) -> dict[int, tuple[float, int, str]]:
    """{année: (MD, base, statut)} pour une grandeur, lue sur les opérations retenues."""
    import pandas as pd
    cote, ops = OPS[key]
    d = figtools.series(SERIE)
    d = d[(d["cote"] == cote) & (d["operation"].isin(ops))]
    out = {}
    for r in d.itertuples():
        a = int(r.annee)
        assert a not in out, f"{key} : deux valeurs pour {a}"
        out[a] = (float(r.valeur_md), int(r.base), str(r.statut))
    return out


def _pib() -> dict[int, float]:
    """{année: PIB nominal en MD} retenu par le ministère des Finances."""
    import pandas as pd
    return {int(r.annee): float(r.pib_minfin_MDT)
            for r in figtools.series(SERIE_PIB).itertuples() if not pd.isna(r.pib_minfin_MDT)}


def _segments(annees: list[int]) -> list[list[int]]:
    """Découpe les années présentes en deux tronçons, base 1983 puis base 2015."""
    av = [a for a in annees if a < RUPTURE]
    ap = [a for a in annees if a >= RUPTURE]
    return [s for s in (sorted(av), sorted(ap)) if s]


def _statut_suffixe(statut: str) -> str:
    return {"semi_definitif": _lab("st_semidef"),
            "provisoire": _lab("st_prov")}.get(statut, "")


def _trace_ligne(ax, serie: dict[int, tuple[float, int, str]], couleur: str, label: str,
                 ib_key: str, grandeur: str = "", pib: dict | None = None):
    """Trace une grandeur en lignes par segment ; points évidés pour les comptes non
    définitifs ; infobulle par point."""
    ft = figtools.fig_text
    for i, seg in enumerate(_segments(sorted(serie))):
        xs, ys = [], []
        for a in seg:
            v, _, _ = serie[a]
            y = 100 * v / pib[a] if pib is not None else v
            xs.append(a)
            ys.append(y)
        ax.plot(xs, ys, "-", color=couleur, lw=1.6,
                label=ft(label) if i == 0 else None, zorder=2)
        for a, y in zip(xs, ys):
            v, _, statut = serie[a]
            evide = statut != "definitif"
            p, = ax.plot([a], [y], "o", color=couleur, ms=4.5,
                         mfc="white" if evide else couleur, zorder=3)
            v_aff = y if pib is not None else v
            dec = 2 if pib is not None else 1
            texte = _lab(ib_key).format(a=a, v=_nombre(v_aff, dec), grandeur=ft(grandeur),
                                        st=_statut_suffixe(statut))
            figtools.infobulle(p, texte)


def fig_vue(vue: str = "flux"):
    """Une vue : "flux" (cotisations et prestations, MD), "solde" (capacité/besoin, MD),
    "solde_pib" (capacité/besoin, % du PIB) ou "transferts" (reçus et versés entre APU, MD)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9, 5.2))
    pib = _pib() if vue == "solde_pib" else None

    if vue == "flux":
        _trace_ligne(ax, _grandeur("cotisations"), BLEU, "cotisations", "ib_flux",
                     grandeur="cotisations")
        _trace_ligne(ax, _grandeur("prestations"), ORANGE, "prestations", "ib_flux",
                     grandeur="prestations")
    elif vue in ("solde", "solde_pib"):
        ax.axhline(0, color="#57606a", lw=0.8)
        _trace_ligne(ax, _grandeur("solde"), VERT, "vue_solde",
                     "ib_solde" if vue == "solde" else "ib_solde_pib", pib=pib)
    elif vue == "transferts":
        _trace_ligne(ax, _grandeur("transf_recus"), BLEU, "transf_recus", "ib_flux",
                     grandeur="transf_recus")
        _trace_ligne(ax, _grandeur("transf_verses"), ORANGE, "transf_verses", "ib_flux",
                     grandeur="transf_verses")
    else:
        raise ValueError(vue)

    ans = sorted(_grandeur("cotisations"))
    ax.set_xlim(ans[0] - 0.7, ans[-1] + 0.7)
    ax.set_xticks([a for a in ans if a % 2 == 1])
    ax.tick_params(axis="x", labelsize=8, rotation=45)
    ax.tick_params(axis="y", labelsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    figtools.marque_rupture(ax, RUPTURE, texte=_lab("rupture"))

    poignees = ax.get_legend_handles_labels()[0]
    poignees.append(Line2D([], [], color=GRIS, marker="o", lw=0, mfc="white",
                           label=ft(_lab("lg_provisoire"))))
    ax.legend(handles=poignees, loc="best", fontsize=8, frameon=False)
    fig.suptitle(_lignes("titre") + "\n" + _lignes(f"st_{vue}"), fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.98))
    return fig


def vues() -> list[tuple[str, object]]:
    """Les quatre vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{v}"), fig_vue(v)) for v in VUES]


def table():
    import pandas as pd
    cot, pre = _grandeur("cotisations"), _grandeur("prestations")
    sol = _grandeur("solde")
    tr, tv = _grandeur("transf_recus"), _grandeur("transf_verses")
    pib = _pib()
    lignes = []
    for a in sorted(cot):
        base = sol[a][1]
        statut = sol[a][2]
        ligne = {
            _lab("col_annee"): a,
            _lab("col_base"): _lab(f"base_{base}"),
            _lab("col_statut"): _lab(f"statut_{statut}"),
            _lab("col_cotisations"): round(cot[a][0], 1) if a in cot else None,
            _lab("col_prestations"): round(pre[a][0], 1) if a in pre else None,
            _lab("col_solde"): round(sol[a][0], 1),
            _lab("col_solde_pib"): round(100 * sol[a][0] / pib[a], 2) if a in pib else None,
            _lab("col_transf_recus"): round(tr[a][0], 1) if a in tr else None,
            _lab("col_transf_verses"): round(tv[a][0], 1) if a in tv else None,
            _lab("col_pib"): round(pib[a], 1) if a in pib else None,
        }
        lignes.append(ligne)
    return pd.DataFrame(lignes)
