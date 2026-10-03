"""Figure « accidents du travail et protection sociale des travailleurs, 1995-2004 » (source CNSS).

    from figures import cnss_atmp_pst_1995_2004 as ap
    ap.fig_branches()   # ressources, emplois et résultat des deux branches, MD courants
    ap.fig_branches("pib")         # les mêmes grandeurs en % du PIB
    ap.fig_branches("ressources")  # en % des ressources de la CNSS, toutes branches
    ap.vues()           # les trois, pour figtools.figure_tabs
    ap.table()          # chaque ligne des deux tableaux, et les ratios (onglet Données)

D'OÙ VIENNENT LES DONNÉES. Les tableaux « Evolution des ressources et des emplois » du régime
des accidents du travail et des maladies professionnelles (page 54 de la Rétrospective
financière 1990-2004 de la CNSS, de 1995 à 2004) et de la protection sociale des travailleurs
(page 56, de 1997 à 2004), série `cnss-retrospective-ressources-emplois` de tunisia-data,
snapshotée dans `precis/_seriescache/`. Comptabilité des « Bilans » : droits constatés, non
encaissements, en milliers de dinars courants, convertis ici en millions.

CE QUI EST TRACÉ, pour chaque branche (un panneau chacune, même axe des années) : les
emplois empilés ligne par ligne — pour les accidents du travail, les prestations, la ligne
« Provision Prest. & Mathématique » sous son intitulé du document, sans interprétation, et
les autres charges ; pour la protection sociale des travailleurs, les indemnités de
licenciement, le maintien des droits aux prestations familiales et les autres charges —,
la pile valant le total des emplois ; le total des ressources en trait plein, les
cotisations seules en tirets ; et, au-dessus de chaque année, le résultat de gestion du
tableau (ressources moins emplois, provisions comprises dans les emplois).

LES DÉNOMINATEURS DES VUES EN POURCENTAGE : ceux de `retraites/figures/
rsna_resultat_1990_2004.py`, dont l'en-tête les documente — PIB du ministère des Finances
(série `irpp-ratios`, rupture de base des comptes nationaux en 1997, marquée et non
corrigée) ; « Total des ressources » de la CNSS, toutes branches et tous régimes (page 78).

LES COLONNES MASQUÉES. Une cellule que la reliure masque porte une estimation provisoire
(`valeur_ou_estimation`, `valeur` vide) ; le segment de l'année est alors hachuré, le point
de la ligne creux, et la table laisse la valeur publiée vide en donnant l'estimation à part.
Un ratio est estimé dès que son numérateur ou son dénominateur l'est. Le statut est lu
cellule par cellule : rien n'est codé en dur.
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
PAGE_CAISSE = 78  # ensemble des régimes, toutes branches, avec CTF et RC
SERIE_PIB = "irpp-ratios"
RUPTURE_PIB = 1997  # base 1983 → base 1997 des comptes nationaux
MESURES = ("md", "pib", "ressources")

BLEU, ORANGE, GRIS, NOIR = "#08519c", "#bc4c00", "#6e7781", "#24292f"

# (nom, page, régime attendu, segments empilés (clé, couleur), lignes de la table)
_BRANCHES = (
    ("atmp", 54, "ATMP",
     (("prestations_atmp", ORANGE), ("provision_mathematique", "#fdae6b"),
      ("autres_charges", "#afb8c1")),
     ("cotisations", "produits_financiers", "autres_produits", "total_ressources",
      "prestations_atmp", "provision_mathematique", "autres_charges", "total_emplois",
      "resultat")),
    ("pst", 56, "PST",
     (("indemnites_licenciement", ORANGE), ("maintien_droits_pf", "#fdae6b"),
      ("autres_charges", "#afb8c1")),
     ("cotisations", "produits_financiers", "autres_produits", "total_ressources",
      "indemnites_licenciement", "maintien_droits_pf", "autres_charges", "total_emplois",
      "resultat")),
)

_L = {
    "titre": {"fr": "Accidents du travail et protection sociale des travailleurs, 1995-2004\n"
                    "ressources, emplois et résultat de gestion",
              "ar": "حوادث الشغل والحماية الاجتماعية للعمّال، 1995-2004\n"
                    "الموارد والاستعمالات ونتيجة التصرّف"},
    "atmp": {"fr": "Accidents du travail et maladies professionnelles",
             "ar": "حوادث الشغل والأمراض المهنية"},
    "pst": {"fr": "Protection sociale des travailleurs", "ar": "الحماية الاجتماعية للعمّال"},
    "y": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "y_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_ressources": {"fr": "% des ressources de la CNSS",
                     "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "vue_md": {"fr": "Millions de dinars", "ar": "بملايين الدنانير"},
    "vue_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "vue_ressources": {"fr": "% des ressources de la CNSS",
                       "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "rupture": {"fr": "changement de base\ndes comptes nationaux",
                "ar": "تغيير سنة أساس\nالحسابات القومية"},
    "x": {"fr": "Année", "ar": "السنة"},
    "lg_ressources": {"fr": "Total des ressources", "ar": "مجموع الموارد"},
    "lg_cotisations": {"fr": "dont cotisations", "ar": "منها الاشتراكات"},
    "lg_resultat": {"fr": "Chiffres : résultat de gestion de l'année",
                    "ar": "الأرقام: نتيجة التصرّف للسنة"},
    "lg_estime": {"fr": "{annees} : valeurs en partie estimées (reliure du document)",
                  "ar": "{annees}: قيم مقدّرة جزئياً (تجليد الوثيقة)"},
    "estime": {"fr": "estimé", "ar": "مقدّر"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_estimations": {"fr": "Estimations provisoires (MD)", "ar": "تقديرات مؤقّتة (م.د)"},
    "col_pib": {"fr": "PIB, ministère des Finances (MD)",
                "ar": "الناتج المحلي الإجمالي، وزارة المالية (م.د)"},
    "col_caisse": {"fr": "Total des ressources de la CNSS (MD)",
                   "ar": "مجموع موارد الصندوق الوطني للضمان الاجتماعي (م.د)"},
    "suffixe_pib": {"fr": "% du PIB", "ar": "% من الناتج"},
    "suffixe_ressources": {"fr": "% des ressources de la CNSS", "ar": "% من موارد الصندوق"},
    "col_estimations_ratios": {"fr": "Estimations provisoires (ratios, %)",
                               "ar": "تقديرات مؤقّتة (نسب، %)"},
    "abrege_atmp": {"fr": "AT/MP", "ar": "حوادث الشغل"},
    "abrege_pst": {"fr": "PST", "ar": "الحماية الاجتماعية"},
    # Lignes des tableaux.
    "cotisations": {"fr": "Cotisations", "ar": "الاشتراكات"},
    "produits_financiers": {"fr": "Produits financiers", "ar": "المداخيل المالية"},
    "autres_produits": {"fr": "Autres produits", "ar": "مداخيل أخرى"},
    "total_ressources": {"fr": "Total des ressources", "ar": "مجموع الموارد"},
    "prestations_atmp": {"fr": "Prestations", "ar": "المنافع"},
    "provision_mathematique": {"fr": "« Provision Prest. & Mathématique »",
                               "ar": "«مدّخرات المنافع والمدّخرات الرياضية»"},
    "indemnites_licenciement": {"fr": "Indemnités de licenciement", "ar": "منح الطرد"},
    "maintien_droits_pf": {"fr": "Maintien des droits aux prestations familiales",
                           "ar": "مواصلة الحقّ في المنافع العائلية"},
    "autres_charges": {"fr": "Autres charges (gestion, subventions, structure)",
                       "ar": "أعباء أخرى (التصرّف والمنح والهيكلة)"},
    "total_emplois": {"fr": "Total des emplois", "ar": "مجموع الاستعمالات"},
    "resultat": {"fr": "Résultat de gestion", "ar": "نتيجة التصرّف"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str, **valeurs) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key).format(**valeurs).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0  # ni « -0,00 » ni « -0,0 »
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _cellules() -> dict[str, dict[tuple[str, int], tuple[float, bool]]]:
    """{branche: {(clé, année): (MD, estimé ?)}}."""
    import pandas as pd
    d = figtools.series(SERIE)
    out = {}
    for nom, page, regime, _, _ in _BRANCHES:
        s = d[d["page"] == page]
        assert set(s["regime"]) == {regime}, f"la page {page} n'est plus le régime {regime}"
        out[nom] = {(r.cle, int(r.annee)): (float(r.valeur_ou_estimation) / 1000,
                                             bool(pd.isna(r.valeur)))
                    for r in s.itertuples() if not pd.isna(r.valeur_ou_estimation)}
    return out


def _ressources_caisse() -> dict[int, tuple[float, bool]]:
    """{année: (MD, estimé ?)} : « Total des ressources » de la CNSS (page PAGE_CAISSE)."""
    import pandas as pd
    d = figtools.series(SERIE)
    d = d[(d["page"] == PAGE_CAISSE) & (d["cle"] == "total_ressources")]
    assert set(d["regime"]) == {"ENSEMBLE"} and set(d["variante"]) == {"avec CTF & RC"} \
        and all("PST" in b for b in d["branche"]), \
        f"la page {PAGE_CAISSE} n'est plus le tableau de l'ensemble, toutes branches"
    return {int(r.annee): (float(r.valeur_ou_estimation) / 1000, bool(pd.isna(r.valeur)))
            for r in d.itertuples() if not pd.isna(r.valeur_ou_estimation)}


def _pib() -> dict[int, float]:
    """{année: PIB nominal en MD} retenu par le ministère des Finances."""
    import pandas as pd
    return {int(r.annee): float(r.pib_minfin_MDT)
            for r in figtools.series(SERIE_PIB).itertuples() if not pd.isna(r.pib_minfin_MDT)}


def _ratios(g: dict, mesure: str) -> dict:
    """Les grandeurs `g` ({nom: {année: (MD, estimé ?)}}) dans l'unité `mesure` ; un ratio
    est estimé si son numérateur ou son dénominateur l'est."""
    if mesure == "md":
        return g
    if mesure == "pib":
        den = {a: (v, False) for a, v in _pib().items()}
    elif mesure == "ressources":
        den = _ressources_caisse()
    else:
        raise ValueError(mesure)
    return {nom: {a: (100 * v / den[a][0], est or den[a][1]) for a, (v, est) in s.items()}
            for nom, s in g.items()}


def _donnees() -> dict[str, dict[str, dict[int, tuple[float, bool]]]]:
    """{branche: {ligne: {année: (MD, estimé ?)}}}, lignes de la table de la branche."""
    c = _cellules()
    out = {}
    for nom, _, _, segments, lignes in _BRANCHES:
        ans = sorted({a for _, a in c[nom]})
        out[nom] = {k: {a: c[nom][(k, a)] for a in ans} for k in lignes}
        for a in ans:  # la pile redonne le total des emplois du tableau
            pile = sum(out[nom][k][a][0] for k, _ in segments)
            assert abs(pile - out[nom]["total_emplois"][a][0]) < 0.01, (nom, a, pile)
    return out


def table():
    import pandas as pd
    g = _donnees()
    pib, caisse = _pib(), _ressources_caisse()
    ratios = {nom: {m: _ratios(g[nom], m) for m in ("pib", "ressources")} for nom in g}
    ans = sorted({a for nom in g for a in g[nom]["resultat"]})
    lignes = []
    for a in ans:
        ligne = {_lab("col_annee"): a}
        estimes, estimes_ratios = [], []
        for nom, _, _, _, cles in _BRANCHES:
            for k in cles:
                col = f"{_lab(f'abrege_{nom}')} · {_lab(k)} (MD)"
                v, est = g[nom][k].get(a, (None, False))
                ligne[col] = None if est or v is None else round(v, 3)
                if est:
                    estimes.append(f"{col} : {_nombre(v, 3)}")
        ligne[_lab("col_estimations")] = " ; ".join(estimes)
        ligne[_lab("col_pib")] = round(pib[a], 1)
        ligne[_lab("col_caisse")] = None if caisse[a][1] else round(caisse[a][0], 1)
        for m in ("pib", "ressources"):
            for nom, *_ in _BRANCHES:
                for k in ("total_ressources", "total_emplois", "resultat"):
                    col = f"{_lab(f'abrege_{nom}')} · {_lab(k)} ({_lab(f'suffixe_{m}')})"
                    v, est = ratios[nom][m][k].get(a, (None, False))
                    ligne[col] = None if est or v is None else round(v, 3)
                    if est:
                        estimes_ratios.append(f"{col} : {_nombre(v, 3)}")
        ligne[_lab("col_estimations_ratios")] = " ; ".join(estimes_ratios)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def vues() -> list[tuple[str, object]]:
    """Les trois vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{m}"), fig_branches(m)) for m in MESURES]


def _unite(mesure: str) -> str:
    if figtools.lang() == "fr":
        return {"md": " MD", "pib": " % du PIB", "ressources": " %"}[mesure]
    return {"md": " م.د", "pib": " %", "ressources": " %"}[mesure]


def _infobulle(artiste, a, cle, v, est, mesure, dec):
    figtools.infobulle(artiste, f"{a} · {_lab(cle)} : {_nombre(v, dec)}{_unite(mesure)}"
                       + (f" ({_lab('estime')})" if est else ""))


def fig_branches(mesure: str = "md"):
    """Un panneau par branche : emplois empilés, ressources et cotisations, résultat chiffré.

    `mesure` : "md" (millions de dinars courants), "pib" (% du PIB) ou "ressources" (% du
    total des ressources de la CNSS, toutes branches).
    """
    figtools.apply_lang_font()
    ft = figtools.fig_text
    donnees = _donnees()
    dec = {"md": 1, "pib": 3, "ressources": 1}[mesure]
    ans_tous = sorted({a for nom in donnees for a in donnees[nom]["resultat"]})
    fig, axes = plt.subplots(2, 1, figsize=(9.5, 9.0), sharex=True,
                             gridspec_kw={"height_ratios": [1.6, 1]})
    for ax, (nom, _, _, segments, _) in zip(axes, _BRANCHES):
        g = _ratios(donnees[nom], mesure)
        ans = sorted(g["resultat"])
        bas = {a: 0.0 for a in ans}
        poignees = []
        for cle, couleur in segments:
            for a in ans:
                v, est = g[cle][a]
                if v:
                    b = ax.bar(a, v, bottom=bas[a], width=0.66, color=couleur,
                               hatch="////" if est else None, edgecolor="white", lw=0.4)
                    _infobulle(b.patches[0], a, cle, v, est, mesure, dec + 1)
                bas[a] += v
            poignees.append(Patch(color=couleur, label=ft(_lab(cle))))
        for cle, style, marque in (("total_ressources", "-", "o"), ("cotisations", "--", "s")):
            s = g[cle]
            ax.plot(ans, [s[a][0] for a in ans], style, color=NOIR, lw=1.6)
            for a in ans:
                v, est = s[a]
                p, = ax.plot([a], [v], marque, color=NOIR, ms=4,
                             mfc="white" if est else NOIR)
                _infobulle(p, a, cle, v, est, mesure, dec + 1)
        poignees += [Line2D([], [], color=NOIR, marker="o", ms=4, lw=1.6,
                            label=ft(_lab("lg_ressources"))),
                     Line2D([], [], color=NOIR, marker="s", ms=4, lw=1.6, ls="--",
                            label=ft(_lab("lg_cotisations")))]
        haut = max(max(bas.values()), max(v for v, _ in g["total_ressources"].values()))
        for a in ans:
            v, est = g["resultat"][a]
            sommet = max(bas[a], g["total_ressources"][a][0])
            ax.annotate(("+" if v > 0 else "") + _nombre(v, dec), (a, sommet),
                        textcoords="offset points", xytext=(0, 7), ha="center",
                        fontsize=7.5, color=BLEU if v >= 0 else ORANGE,
                        fontstyle="italic" if est else "normal")
        ax.set_ylim(0, haut * 1.5)
        ax.set_title(ft(_lab(nom)), fontsize=10)
        ax.set_ylabel(ft(_lab("y" if mesure == "md" else f"y_{mesure}")))
        ax.grid(True, axis="y", alpha=0.3)
        if mesure == "pib" and ans_tous[0] < RUPTURE_PIB <= ans_tous[-1]:
            figtools.marque_rupture(ax, RUPTURE_PIB,
                                    _lignes("rupture") if ax is axes[0] else None)
        estimees = sorted({a for s in g.values() for a, (_, e) in s.items() if e})
        if estimees:  # chaque panneau dit ses propres années estimées
            poignees.append(Patch(facecolor="white", edgecolor=GRIS, hatch="////",
                                  label=ft(_lab("lg_estime").format(
                                      annees=", ".join(map(str, estimees))))))
        poignees.append(Line2D([], [], lw=0, label=ft(_lab("lg_resultat"))))
        ax.legend(handles=poignees, loc="upper left", fontsize=7.5, ncol=2, frameon=False,
                  handlelength=1.6)
    axes[-1].set_xticks(ans_tous)
    axes[-1].tick_params(axis="x", labelsize=8)
    axes[-1].set_xlabel(ft(_lab("x")))
    fig.suptitle(_lignes("titre"), fontsize=11)
    fig.tight_layout()
    return fig
