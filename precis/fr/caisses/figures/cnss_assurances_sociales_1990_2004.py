"""Figure « branche des assurances sociales du régime général, 1990-2004 » (source CNSS).

    from figures import cnss_assurances_sociales_1990_2004 as asr
    asr.fig_assurances_sociales()   # emplois détaillés, ressources et résultat, MD courants
    asr.fig_assurances_sociales("pib")         # les mêmes grandeurs en % du PIB
    asr.fig_assurances_sociales("ressources")  # en % des ressources de la CNSS
    asr.vues()           # les trois, pour figtools.figure_tabs
    asr.table()          # les montants et les ratios de la figure (onglet Données)

D'OÙ VIENNENT LES DONNÉES. Le tableau « Evolution des ressources et des emplois » de la branche
des assurances sociales — maladie, maternité, décès — du régime des salariés non agricoles,
dans la Rétrospective financière 1990-2004 de la CNSS (page 13 du document), série
`cnss-retrospective-ressources-emplois` de tunisia-data, snapshotée dans `precis/_seriescache/`.
Comptabilité des « Bilans » : droits constatés, en milliers de dinars courants, convertis ici
en millions.

CE QUI EST TRACÉ.
  - Haut : les emplois de la branche, empilés ligne par ligne — les prestations en nature
    (forfait accordé à la Santé publique, participation aux budgets des hôpitaux, compléments
    de soins et d'hospitalisation facturés par les hôpitaux publics, renforcement des
    structures sanitaires publiques, polycliniques, autres actions sanitaires, et, réunis
    parce qu'ils sont petits, le poste « C.A.O. » et les soins à l'étranger), les prestations
    en espèces (indemnités de maladie, indemnités de couches, capital-décès et indemnité de
    décès réunis) et les autres charges (frais de gestion, subventions, charges de
    structure) ; la pile vaut le total des emplois. Par-dessus, le total des ressources et,
    en tirets, les cotisations seules : l'écart entre la ligne et la pile est le résultat.
  - Bas : le résultat de gestion du tableau, ressources moins emplois, en barres.
La table de données donne chaque ligne du tableau séparément.

LES DÉNOMINATEURS DES VUES EN POURCENTAGE : ceux de `retraites/figures/
rsna_resultat_1990_2004.py`, dont l'en-tête les documente — PIB du ministère des Finances
(série `irpp-ratios`, rupture de base des comptes nationaux en 1997, marquée et non
corrigée) ; « Total des ressources » de la CNSS, toutes branches et tous régimes (page 78).

LES COLONNES MASQUÉES. Une cellule que la reliure masque porte une estimation provisoire
(`valeur_ou_estimation`, `valeur` vide) ; le segment ou la barre de l'année est alors
hachuré, le point de la ligne est creux, et la table laisse la valeur publiée vide en
donnant l'estimation à part. Une somme est estimée dès qu'une composante l'est, un ratio dès
que son numérateur ou son dénominateur l'est. Le statut est lu cellule par cellule : rien
n'est codé en dur.
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
PAGE = 13  # régime des salariés non agricoles, branche des assurances sociales
PAGE_CAISSE = 78  # ensemble des régimes, toutes branches, avec CTF et RC
SERIE_PIB = "irpp-ratios"
RUPTURE_PIB = 1997  # base 1983 → base 1997 des comptes nationaux
MESURES = ("md", "pib", "ressources")

BLEU, ORANGE, GRIS, NOIR = "#08519c", "#bc4c00", "#6e7781", "#24292f"

# (nom, clés du tableau sommées, couleur), dans l'ordre d'empilement.
_EMPLOIS = (
    ("forfait", ("forfait_sante_publique",), BLEU),
    ("hopitaux", ("participation_hopitaux",), "#2171b5"),
    ("complements", ("complement_soins_hopitaux",), "#6baed6"),
    ("renforcement", ("renforcement_structures",), "#9ecae1"),
    ("policliniques", ("policliniques",), "#1a7f37"),
    ("actions", ("autres_actions_sanitaires",), "#74c476"),
    ("cao_etranger", ("cao", "soins_etranger"), "#c7e9c0"),
    ("maladie", ("indemnite_maladie",), ORANGE),
    ("couches", ("indemnite_couches",), "#fd8d3c"),
    ("deces", ("capital_deces", "indemnite_deces"), "#fdd0a2"),
    ("autres_charges", ("autres_charges",), "#afb8c1"),
)
# Lignes du tableau reprises une à une dans la table de données.
_LIGNES_TABLE = (
    "cotisations", "produits_financiers", "autres_produits", "total_ressources",
    "prestations_nature", "forfait_sante_publique", "participation_hopitaux",
    "complement_soins_hopitaux", "renforcement_structures", "policliniques", "cao",
    "soins_etranger", "autres_actions_sanitaires", "prestations_especes",
    "indemnite_maladie", "indemnite_couches", "capital_deces", "indemnite_deces",
    "autres_charges", "total_emplois", "resultat",
)

_L = {
    "titre": {"fr": "Branche des assurances sociales du régime général (RSNA), 1990-2004\n"
                    "emplois, ressources et résultat de gestion",
              "ar": "فرع التأمينات الاجتماعية في نظام الأجراء غير الفلاحيين، 1990-2004\n"
                    "الاستعمالات والموارد ونتيجة التصرّف"},
    "y_haut": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "y_bas": {"fr": "Résultat de gestion\n(MD courants)", "ar": "نتيجة التصرّف\n(م.د جارية)"},
    "y_haut_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_bas_pib": {"fr": "Résultat de gestion\n(% du PIB)", "ar": "نتيجة التصرّف\n(% من الناتج)"},
    "y_haut_ressources": {"fr": "% des ressources de la CNSS",
                          "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "y_bas_ressources": {"fr": "Résultat de gestion\n(% des ressources\nde la CNSS)",
                         "ar": "نتيجة التصرّف\n(% من موارد\nالصندوق)"},
    "vue_md": {"fr": "Millions de dinars", "ar": "بملايين الدنانير"},
    "vue_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "vue_ressources": {"fr": "% des ressources de la CNSS",
                       "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "rupture": {"fr": "changement de base\ndes comptes nationaux",
                "ar": "تغيير سنة أساس\nالحسابات القومية"},
    "x": {"fr": "Année", "ar": "السنة"},
    "forfait": {"fr": "Forfait accordé à la Santé publique",
                "ar": "المبلغ الجزافي الممنوح للصحة العمومية"},
    "hopitaux": {"fr": "Participation aux budgets des hôpitaux",
                 "ar": "المساهمة في ميزانيات المستشفيات"},
    "complements": {"fr": "Compléments de soins et d'hospitalisation facturés par les "
                          "hôpitaux publics",
                    "ar": "تكملة العلاج والإقامة المفوترة من المستشفيات العمومية"},
    "renforcement": {"fr": "Renforcement des structures sanitaires publiques",
                     "ar": "دعم الهياكل الصحية العمومية"},
    "policliniques": {"fr": "Polycliniques", "ar": "المصحّات المتعدّدة الاختصاصات"},
    "actions": {"fr": "Autres actions sanitaires", "ar": "أنشطة صحية أخرى"},
    "cao_etranger": {"fr": "« C.A.O. » et soins à l'étranger",
                     "ar": "«C.A.O.» والعلاج بالخارج"},
    "maladie": {"fr": "Indemnités de maladie", "ar": "منح المرض"},
    "couches": {"fr": "Indemnités de couches", "ar": "منح الولادة"},
    "deces": {"fr": "Capital-décès et indemnité de décès", "ar": "رأس مال الوفاة ومنحة الوفاة"},
    "autres_charges": {"fr": "Autres charges (gestion, subventions, structure)",
                       "ar": "أعباء أخرى (التصرّف والمنح والهيكلة)"},
    "lg_ressources": {"fr": "Total des ressources", "ar": "مجموع الموارد"},
    "lg_cotisations": {"fr": "dont cotisations", "ar": "منها الاشتراكات"},
    "lg_nature": {"fr": "Prestations en nature", "ar": "المنافع العينية"},
    "lg_especes": {"fr": "Prestations en espèces", "ar": "المنافع النقدية"},
    "lg_excedent": {"fr": "Excédent", "ar": "فائض"},
    "lg_deficit": {"fr": "Déficit", "ar": "عجز"},
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
    # Lignes du tableau (table de données).
    "cotisations": {"fr": "Cotisations", "ar": "الاشتراكات"},
    "produits_financiers": {"fr": "Produits financiers", "ar": "المداخيل المالية"},
    "autres_produits": {"fr": "Autres produits", "ar": "مداخيل أخرى"},
    "total_ressources": {"fr": "Total des ressources", "ar": "مجموع الموارد"},
    "prestations_nature": {"fr": "Prestations en nature", "ar": "المنافع العينية"},
    "forfait_sante_publique": {"fr": "Forfait accordé à la Santé publique",
                               "ar": "المبلغ الجزافي الممنوح للصحة العمومية"},
    "participation_hopitaux": {"fr": "Participation aux budgets des hôpitaux",
                               "ar": "المساهمة في ميزانيات المستشفيات"},
    "complement_soins_hopitaux": {"fr": "Compléments de soins et d'hospitalisation facturés "
                                        "par les hôpitaux publics",
                                  "ar": "تكملة العلاج والإقامة المفوترة من المستشفيات "
                                        "العمومية"},
    "renforcement_structures": {"fr": "Renforcement des structures sanitaires publiques",
                                "ar": "دعم الهياكل الصحية العمومية"},
    "policliniques": {"fr": "Polycliniques", "ar": "المصحّات المتعدّدة الاختصاصات"},
    "cao": {"fr": "« C.A.O. »", "ar": "«C.A.O.»"},
    "soins_etranger": {"fr": "Soins à l'étranger", "ar": "العلاج بالخارج"},
    "autres_actions_sanitaires": {"fr": "Autres actions sanitaires", "ar": "أنشطة صحية أخرى"},
    "prestations_especes": {"fr": "Prestations en espèces", "ar": "المنافع النقدية"},
    "indemnite_maladie": {"fr": "Indemnités de maladie", "ar": "منح المرض"},
    "indemnite_couches": {"fr": "Indemnités de couches", "ar": "منح الولادة"},
    "capital_deces": {"fr": "Capital-décès", "ar": "رأس مال الوفاة"},
    "indemnite_deces": {"fr": "Indemnité de décès", "ar": "منحة الوفاة"},
    "total_emplois": {"fr": "Total des emplois", "ar": "مجموع الاستعمالات"},
    "resultat": {"fr": "Résultat de gestion", "ar": "نتيجة التصرّف"},
}
_L["autres_charges_table"] = {"fr": "Autres charges", "ar": "أعباء أخرى"}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str, **valeurs) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key).format(**valeurs).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0  # ni « -0,00 » ni « -0,0 »
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _cellules() -> dict[tuple[str, int], tuple[float, bool]]:
    """{(clé, année): (montant en MD, estimé ?)} pour le tableau de la page PAGE."""
    import pandas as pd
    d = figtools.series(SERIE)
    d = d[d["page"] == PAGE]
    assert set(d["regime"]) == {"RSNA"} and set(d["branche"]) == {"assurances sociales"}, \
        "la page 13 n'est plus la branche des assurances sociales du RSNA"
    return {(r.cle, int(r.annee)): (float(r.valeur_ou_estimation) / 1000,
                                     bool(pd.isna(r.valeur)))
            for r in d.itertuples() if not pd.isna(r.valeur_ou_estimation)}


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


def _somme(c: dict, cles, a: int) -> tuple[float, bool]:
    return sum(c[(k, a)][0] for k in cles), any(c[(k, a)][1] for k in cles)


def _donnees() -> dict[str, dict[int, tuple[float, bool]]]:
    """{grandeur: {année: (MD, estimé ?)}} : segments de la pile, ressources, cotisations,
    total des emplois et résultat."""
    c = _cellules()
    ans = sorted({a for _, a in c})
    g = {nom: {a: _somme(c, cles, a) for a in ans} for nom, cles, _ in _EMPLOIS}
    for cle in ("total_ressources", "cotisations", "total_emplois", "resultat"):
        g[cle] = {a: c[(cle, a)] for a in ans}
    for a in ans:  # la pile redonne le total des emplois du tableau
        pile = sum(g[n][a][0] for n, _, _ in _EMPLOIS)
        assert abs(pile - g["total_emplois"][a][0]) < 0.01, (a, pile)
    return g


def table():
    import pandas as pd
    c = _cellules()
    ans = sorted({a for _, a in c})
    pib, caisse = _pib(), _ressources_caisse()
    g = {k: {a: c[(k, a)] for a in ans} for k in _LIGNES_TABLE}
    ratios = {m: _ratios(g, m) for m in ("pib", "ressources")}
    lignes = []
    for a in ans:
        ligne = {_lab("col_annee"): a}
        estimes, estimes_ratios = [], []
        for k in _LIGNES_TABLE:
            nom = _lab("autres_charges_table" if k == "autres_charges" else k)
            v, est = g[k][a]
            ligne[f"{nom} (MD)"] = None if est else round(v, 3)
            if est:
                estimes.append(f"{nom} : {_nombre(v, 3)}")
        ligne[_lab("col_estimations")] = " ; ".join(estimes)
        ligne[_lab("col_pib")] = round(pib[a], 1)
        ligne[_lab("col_caisse")] = None if caisse[a][1] else round(caisse[a][0], 1)
        for m in ("pib", "ressources"):
            for k in ("total_ressources", "prestations_nature", "prestations_especes",
                      "total_emplois", "resultat"):
                v, est = ratios[m][k][a]
                col = f"{_lab(k)} ({_lab(f'suffixe_{m}')})"
                ligne[col] = None if est else round(v, 3)
                if est:
                    estimes_ratios.append(f"{col} : {_nombre(v, 3)}")
        ligne[_lab("col_estimations_ratios")] = " ; ".join(estimes_ratios)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def vues() -> list[tuple[str, object]]:
    """Les trois vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{m}"), fig_assurances_sociales(m)) for m in MESURES]


def _unite(mesure: str) -> str:
    return {"md": " MD", "pib": " % du PIB", "ressources": " %"}[mesure] \
        if figtools.lang() == "fr" else {"md": " م.د", "pib": " %", "ressources": " %"}[mesure]


def fig_assurances_sociales(mesure: str = "md"):
    """Haut : emplois empilés, ressources et cotisations ; bas : résultat de gestion.

    `mesure` : "md" (millions de dinars courants), "pib" (% du PIB) ou "ressources" (% du
    total des ressources de la CNSS, toutes branches).
    """
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _ratios(_donnees(), mesure)
    ans = sorted(g["resultat"])
    suffixe = "" if mesure == "md" else f"_{mesure}"
    dec = {"md": 1, "pib": 2, "ressources": 1}[mesure]
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 9.4), sharex=True,
                                 gridspec_kw={"height_ratios": [3, 1.3]})

    bas = {a: 0.0 for a in ans}
    poignees = []
    for nom, _, couleur in _EMPLOIS:
        for a in ans:
            v, est = g[nom][a]
            if v:
                barre = ax.bar(a, v, bottom=bas[a], width=0.72, color=couleur,
                               hatch="////" if est else None, edgecolor="white", lw=0.4)
                figtools.infobulle(barre.patches[0],
                                   f"{a} · {_lab(nom)} : {_nombre(v, dec + 1)}{_unite(mesure)}"
                                   + (f" ({_lab('estime')})" if est else ""))
            bas[a] += v
        poignees.append(Patch(color=couleur, label=ft(_lab(nom))))

    for cle, style, marque in (("total_ressources", "-", "o"), ("cotisations", "--", "s")):
        s = g[cle]
        ax.plot(ans, [s[a][0] for a in ans], style, color=NOIR, lw=1.6)
        for a in ans:
            v, est = s[a]
            p, = ax.plot([a], [v], marque, color=NOIR, ms=4, mfc="white" if est else NOIR)
            figtools.infobulle(p, f"{a} · {_lab(cle)} : {_nombre(v, dec + 1)}{_unite(mesure)}"
                               + (f" ({_lab('estime')})" if est else ""))
    poignees += [Line2D([], [], color=NOIR, marker="o", ms=4, lw=1.6,
                        label=ft(_lab("lg_ressources"))),
                 Line2D([], [], color=NOIR, marker="s", ms=4, lw=1.6, ls="--",
                        label=ft(_lab("lg_cotisations")))]
    haut = max(max(bas.values()), max(v for v, _ in g["total_ressources"].values()))
    ax.set_ylim(0, haut * (1.25 if mesure == "pib" else 1.08))
    ax.set_ylabel(_lignes("y_haut" + suffixe))
    ax.set_title(_lignes("titre"))
    ax.grid(True, axis="y", alpha=0.3)

    res = g["resultat"]
    for a in ans:
        v, est = res[a]
        barre = bx.bar(a, v, width=0.7, color=BLEU if v >= 0 else ORANGE,
                       hatch="////" if est else None, edgecolor="white", lw=0)
        figtools.infobulle(barre.patches[0],
                           f"{a} · {_lab('resultat')} : {_nombre(v, dec + 1)}{_unite(mesure)}"
                           + (f" ({_lab('estime')})" if est else ""))
        bx.annotate(_nombre(v, dec), (a, v), textcoords="offset points",
                    xytext=(0, 3 if v >= 0 else -10), ha="center", fontsize=7,
                    color="#57606a")
    bx.axhline(0, color="#57606a", lw=0.8)
    bas_r, haut_r = min(v for v, _ in res.values()), max(v for v, _ in res.values())
    bx.set_ylim(bas_r * 1.25 if bas_r < 0 else 0, haut_r * 1.3 if haut_r > 0 else 1)
    bx.set_ylabel(_lignes("y_bas" + suffixe))
    if mesure == "pib" and ans[0] < RUPTURE_PIB <= ans[-1]:
        figtools.marque_rupture(ax, RUPTURE_PIB, _lignes("rupture"))
        figtools.marque_rupture(bx, RUPTURE_PIB)
    bx.set_xlabel(ft(_lab("x")))
    bx.set_xticks(ans)
    bx.tick_params(axis="x", labelsize=8)
    bx.grid(True, axis="y", alpha=0.3)

    estimees = sorted({a for s in g.values() for a, (_, est) in s.items() if est})
    if estimees:
        poignees.append(Patch(facecolor="white", edgecolor=GRIS, hatch="////",
                              label=ft(_lab("lg_estime").format(
                                  annees=", ".join(map(str, estimees))))))
    bx.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig
