"""Figure « résultat de la branche des pensions du régime général, 1990-2004 » (source CNSS).

    from figures import rsna_resultat_1990_2004 as rr
    rr.fig_resultat()   # ressources, pensions servies et résultat de gestion, en MD courants
    rr.table()          # les montants de la figure (onglet Données)

D'OÙ VIENNENT LES DONNÉES. Le tableau « Evolution des ressources et des emplois » de la branche
des pensions du régime des salariés non agricoles, dans la Rétrospective financière 1990-2004
de la CNSS (page 15 du document), série `cnss-retrospective-ressources-emplois` de
tunisia-data, snapshotée dans `precis/_seriescache/`. Comptabilité des « Bilans » : droits
constatés, en milliers de dinars courants, convertis ici en millions.

CE QUI EST TRACÉ.
  - Haut : les cotisations de la branche, les pensions servies — vieillesse, invalidité,
    veuves et orphelins, sans les allocations familiales que la ligne « Prestations » des
    pensionnés comprend jusqu'en 1994 — et les produits financiers, nuls jusqu'en 1995
    et de 48 à 94 MD par an à partir de 1996 : les résultats positifs de 1996-2001 leur
    doivent l'essentiel, et la note de lecture le dit.
  - Bas : le résultat de gestion du tableau, ressources moins emplois, en barres.

LES COLONNES MASQUÉES. La reliure de l'exemplaire numérisé masque la colonne 1999 (parfois
2000) de la plupart des tableaux ; une cellule masquée y a une `valeur` vide et une
estimation provisoire dans `valeur_ou_estimation`. Une année dont une grandeur tracée est
estimée reçoit une marque creuse, ou une barre hachurée, et la table de données laisse la
valeur publiée vide en donnant l'estimation à part. Aucune année n'est codée en dur : le
module lit le statut de chaque cellule, et tout se met à jour quand l'original est relu.
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
PAGE = 15  # régime des salariés non agricoles, branche des pensions

BLEU, ORANGE, GRIS = "#08519c", "#bc4c00", "#6e7781"

# Grandeurs tracées : clé du tableau (ou somme de clés), étiquette.
_PENSIONS = ("vieillesse", "invalidites", "veuves", "orphelins")
_GRANDEURS = (
    ("cotisations", ("cotisations",)),
    ("pensions", _PENSIONS),
    ("financiers", ("produits_financiers",)),
    ("ressources", ("total_ressources",)),
    ("emplois", ("total_emplois",)),
    ("resultat", ("resultat",)),
)

_L = {
    "titre": {"fr": "Branche des pensions du régime général (RSNA), 1990-2004\n"
                    "ressources, pensions servies et résultat de gestion",
              "ar": "فرع الجرايات في نظام الأجراء غير الفلاحيين، 1990-2004\n"
                    "الموارد والجرايات المصروفة ونتيجة التصرّف"},
    "y_haut": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "y_bas": {"fr": "Résultat de gestion (MD courants)",
              "ar": "نتيجة التصرّف (م.د جارية)"},
    "x": {"fr": "Année", "ar": "السنة"},
    "lg_cotisations": {"fr": "Cotisations", "ar": "الاشتراكات"},
    "lg_pensions": {"fr": "Pensions servies (vieillesse, invalidité, veuves, orphelins)",
                    "ar": "الجرايات المصروفة (الشيخوخة والعجز والأرامل والأيتام)"},
    "lg_financiers": {"fr": "Produits financiers", "ar": "المداخيل المالية"},
    "lg_excedent": {"fr": "Excédent", "ar": "فائض"},
    "lg_deficit": {"fr": "Déficit", "ar": "عجز"},
    "lg_estime": {"fr": "{annees} : valeur en partie estimée (reliure du document)",
                  "ar": "{annees}: قيمة مقدّرة جزئياً (تجليد الوثيقة)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_cotisations": {"fr": "Cotisations (MD)", "ar": "الاشتراكات (م.د)"},
    "col_pensions": {"fr": "Pensions servies (MD)", "ar": "الجرايات المصروفة (م.د)"},
    "col_financiers": {"fr": "Produits financiers (MD)", "ar": "المداخيل المالية (م.د)"},
    "col_ressources": {"fr": "Total des ressources (MD)", "ar": "مجموع الموارد (م.د)"},
    "col_emplois": {"fr": "Total des emplois (MD)", "ar": "مجموع الاستعمالات (م.د)"},
    "col_resultat": {"fr": "Résultat de gestion (MD)", "ar": "نتيجة التصرّف (م.د)"},
    "col_estimations": {"fr": "Estimations provisoires (MD)", "ar": "تقديرات مؤقّتة (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _cellules() -> dict[tuple[str, int], tuple[float, bool]]:
    """{(clé, année): (montant en MD, estimé ?)} pour le tableau de la page PAGE."""
    import pandas as pd
    d = figtools.series(SERIE)
    d = d[d["page"] == PAGE]
    assert set(d["regime"]) == {"RSNA"} and set(d["branche"]) == {"pensions"}, \
        "la page 15 n'est plus la branche des pensions du RSNA"
    return {(r.cle, int(r.annee)): (float(r.valeur_ou_estimation) / 1000,
                                     bool(pd.isna(r.valeur)))
            for r in d.itertuples() if not pd.isna(r.valeur_ou_estimation)}


def _donnees() -> dict[str, dict[int, tuple[float, bool]]]:
    """{grandeur: {année: (MD, estimé ?)}} ; une somme est estimée si une composante l'est."""
    c = _cellules()
    annees = sorted({a for _, a in c})
    out = {}
    for nom, cles in _GRANDEURS:
        out[nom] = {a: (sum(c[(k, a)][0] for k in cles), any(c[(k, a)][1] for k in cles))
                    for a in annees}
    return out


def table():
    import pandas as pd
    g = _donnees()
    lignes = []
    for a in sorted(g["resultat"]):
        ligne = {_lab("col_annee"): a}
        estimes = []
        for nom, _ in _GRANDEURS:
            v, est = g[nom][a]
            ligne[_lab(f"col_{nom}")] = None if est else round(v, 1)
            if est:
                estimes.append(f"{_lab(f'col_{nom}').split(' (')[0]} : {_nombre(v)}")
        ligne[_lab("col_estimations")] = " ; ".join(estimes)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def _courbe(ax, serie: dict[int, tuple[float, bool]], couleur, marque, label):
    ans = sorted(serie)
    ax.plot(ans, [serie[a][0] for a in ans], "-", color=couleur, lw=1.8)
    for a in ans:
        v, est = serie[a]
        ax.plot([a], [v], marque, color=couleur, ms=4.5, mfc="white" if est else couleur)
    return Line2D([], [], color=couleur, marker=marque, lw=1.8, ms=4.5, label=label)


def fig_resultat():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _donnees()
    ans = sorted(g["resultat"])
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 7.6), sharex=True,
                                 gridspec_kw={"height_ratios": [3, 2]})

    poignees = [
        _courbe(ax, g["cotisations"], BLEU, "o", ft(_lab("lg_cotisations"))),
        _courbe(ax, g["pensions"], ORANGE, "s", ft(_lab("lg_pensions"))),
        _courbe(ax, g["financiers"], GRIS, "^", ft(_lab("lg_financiers"))),
    ]
    ax.set_ylim(0, None)
    ax.set_ylabel(ft(_lab("y_haut")))
    ax.set_title("\n".join(ft(l) for l in _lab("titre").split("\n")))
    ax.grid(True, alpha=0.3)

    res = g["resultat"]
    for a in ans:
        v, est = res[a]
        bx.bar(a, v, width=0.7, color=BLEU if v >= 0 else ORANGE,
               hatch="////" if est else None, edgecolor="white", lw=0)
        bx.annotate(_nombre(v), (a, v), textcoords="offset points",
                    xytext=(0, 3 if v >= 0 else -10), ha="center", fontsize=7,
                    color="#57606a")
    bx.axhline(0, color="#57606a", lw=0.8)
    bas, haut = min(v for v, _ in res.values()), max(v for v, _ in res.values())
    bx.set_ylim(bas * 1.25 if bas < 0 else 0, haut * 1.35 if haut > 0 else 1)
    bx.set_ylabel(ft(_lab("y_bas")))
    bx.set_xlabel(ft(_lab("x")))
    bx.set_xticks(ans)
    bx.tick_params(axis="x", labelsize=8)
    bx.grid(True, axis="y", alpha=0.3)
    bx.legend(handles=[Patch(color=BLEU, label=ft(_lab("lg_excedent"))),
                       Patch(color=ORANGE, label=ft(_lab("lg_deficit")))],
              loc="lower left", fontsize=8)

    estimees = sorted({a for s in g.values() for a, (_, est) in s.items() if est})
    if estimees:
        poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", lw=0,
                               label=ft(_lab("lg_estime").format(
                                   annees=", ".join(map(str, estimees))))))
    ax.legend(handles=poignees, loc="upper left", fontsize=8)
    fig.tight_layout()
    return fig
