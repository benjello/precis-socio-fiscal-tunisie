"""Figure « résultat de la branche des pensions du régime général, 1990-2004 » (source CNSS).

    from figures import rsna_resultat_1990_2004 as rr
    rr.fig_resultat()   # ressources, pensions servies et résultat de gestion, en MD courants
    rr.fig_resultat("pib")         # les mêmes grandeurs en % du PIB
    rr.fig_resultat("ressources")  # en % des ressources de la CNSS, toutes branches
    rr.vues()           # les trois, pour figtools.figure_tabs
    rr.table()          # les montants et les ratios de la figure (onglet Données)

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

LES RÉALLOCATIONS DU TAUX GLOBAL. Trois lignes verticales marquent, sur les deux panneaux,
les dates d'effet des trois relèvements de la quote-part du taux global de la loi n° 60-30
affectée à la branche des pensions : 1er janvier 1988 (décret n° 88-1137, 1,25/20e →
4,25/20e), 1er janvier 1994 (décret n° 94-1429, 4,25/20e → 6,25/20e, avec les paliers de la
part salariale de la cotisation propre aux 1ers juillets 1994, 1995 et 1996) et 1er janvier
2003 (décret n° 2003-1212, 6,25/20e → 7,25/20e). Ces dates sont celles qu'établissent les
chapitres du précis (cotisations_sociales/index.qmd, tbl-pensions-quote-part ;
retraites/_secteur_prive.qmd, annexe des textes) ; elles coïncident avec les notes du
document (pages 14, 15 et 60). Les libellés donnent le taux de la branche selon la caisse
(note (1) et (3) de la page 15 : 5 → 8 %, 8 → 10 %, 11,5 → 12,5 %), lecture en points
qu'expose le chapitre des cotisations. L'axe des années commence en 1988 pour montrer la
première ; le tableau, lui, commence en 1990.

LES DÉNOMINATEURS DES VUES EN POURCENTAGE.
  - PIB : le PIB nominal retenu par le ministère des Finances (série `irpp-ratios`,
    colonne `pib_minfin_MDT`, en millions de dinars courants), déduit du déficit budgétaire
    publié en dinars et en points de PIB (fiche `sources/minfinances-recettes-fiscales.md`
    de tunisia-data). Il passe en 1997 de la base 1983 à la base 1997 des comptes
    nationaux : 19 066,2 MD en 1996, valeur de la base 1983 (série 30 d'UNdata, annuaire
    statistique de l'INS 1995-2001) ; 22 943,9 MD en 1997, valeur de la base 1997 (série 100
    d'UNdata), quand la base 1983 donnait 20 898 pour la même année — environ 10 % de plus
    du seul fait de la base (tunisia-data, `docs/croissances-revenus-prix.md`, et les
    réserves des séries `undata-pib` et `cnat-pib-nominal`). Rien n'est converti d'une base
    à l'autre : la rupture est marquée sur la vue, entre 1996 et 1997.
  - Ressources de la CNSS : la ligne « Total des ressources » du tableau de l'ensemble des
    régimes, toutes branches — prestations familiales, assurances sociales, pensions,
    accidents du travail et maladies professionnelles, protection sociale des travailleurs,
    avec la convention tuniso-française et le régime complémentaire (page 78). Ses
    composantes en redonnent le total, et ce total est la somme des totaux des branches
    (pages 63, 67 et 75) : aucune ligne de transfert interne n'y figure, donc rien n'y est
    compté deux fois. Le tableau existe de 1990 à 2004 ; les accidents du travail n'y ont de
    ressources qu'à partir de 1995 et la protection sociale des travailleurs à partir de
    1997 : le dénominateur s'élargit à ces dates.

LES COLONNES MASQUÉES. La reliure de l'exemplaire numérisé masque la colonne 1999 (parfois
2000) de la plupart des tableaux ; une cellule masquée y a une `valeur` vide et une
estimation provisoire dans `valeur_ou_estimation`. Une année dont une grandeur tracée est
estimée reçoit une marque creuse, ou une barre hachurée, et la table de données laisse la
valeur publiée vide en donnant l'estimation à part. Un ratio est estimé dès que son
numérateur ou son dénominateur l'est. Aucune année n'est codée en dur : le
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
PAGE_CAISSE = 78  # ensemble des régimes, toutes branches, avec CTF et RC
SERIE_PIB = "irpp-ratios"
RUPTURE_PIB = 1997  # base 1983 → base 1997 des comptes nationaux (voir l'en-tête)
MESURES = ("md", "pib", "ressources")
# Relèvements de la quote-part du taux global affectée à la branche (date d'effet, clé du
# libellé) — dates établies au chapitre des cotisations, voir l'en-tête.
REALLOCATIONS = ((1988, "realloc_1988"), (1994, "realloc_1994"), (2003, "realloc_2003"))
VIOLET = "#8250df"

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
    "y_haut_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_bas_pib": {"fr": "Résultat de gestion (% du PIB)",
                  "ar": "نتيجة التصرّف (% من الناتج)"},
    "y_haut_ressources": {"fr": "% des ressources de la CNSS",
                          "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "y_bas_ressources": {"fr": "Résultat de gestion\n(% des ressources de la CNSS)",
                         "ar": "نتيجة التصرّف\n(% من موارد الصندوق)"},
    "vue_md": {"fr": "Millions de dinars", "ar": "بملايين الدنانير"},
    "vue_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "vue_ressources": {"fr": "% des ressources de la CNSS",
                       "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "rupture": {"fr": "changement de base\ndes comptes nationaux",
                "ar": "تغيير سنة أساس\nالحسابات القومية"},
    "x": {"fr": "Année", "ar": "السنة"},
    "realloc_1988": {"fr": "1er janv. 1988 : 5 → 8 %", "ar": "غرّة جانفي 1988: من 5 إلى 8 %"},
    "realloc_1994": {"fr": "1er janv. 1994 : 8 → 10 %\npuis part salariale, juil. 1994-1996",
                     "ar": "غرّة جانفي 1994: من 8 إلى 10 %\nثمّ حصّة الأجير، جويلية 1994-1996"},
    "realloc_2003": {"fr": "1er janv. 2003 : 11,5 → 12,5 %", "ar": "غرّة جانفي 2003: من 11,5 إلى 12,5 %"},
    "lg_realloc": {"fr": "Points du taux global réaffectés à la branche\n(taux de la branche selon la caisse)",
                   "ar": "نقاط من النسبة الجملية أُعيد تخصيصها للفرع\n(نسبة الفرع حسب الصندوق)"},
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
    "col_pib": {"fr": "PIB, ministère des Finances (MD)",
                "ar": "الناتج المحلي الإجمالي، وزارة المالية (م.د)"},
    "col_caisse": {"fr": "Total des ressources de la CNSS (MD)",
                   "ar": "مجموع موارد الصندوق الوطني للضمان الاجتماعي (م.د)"},
    "suffixe_pib": {"fr": "% du PIB", "ar": "% من الناتج"},
    "suffixe_ressources": {"fr": "% des ressources de la CNSS", "ar": "% من موارد الصندوق"},
    "col_estimations_ratios": {"fr": "Estimations provisoires (ratios, %)",
                               "ar": "تقديرات مؤقّتة (نسب، %)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0  # ni « -0,00 » ni « -0,0 »
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


def _ressources_caisse() -> dict[int, tuple[float, bool]]:
    """{année: (MD, estimé ?)} : « Total des ressources » de la CNSS, toutes branches et tous
    régimes (page PAGE_CAISSE)."""
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


def _ratios(g: dict, mesure: str) -> dict[str, dict[int, tuple[float, bool]]]:
    """Les grandeurs `g` ({nom: {année: (MD, estimé ?)}}) dans l'unité `mesure`.

    "md" : inchangées ; "pib" : en % du PIB ; "ressources" : en % du total des ressources de
    la caisse. Un ratio est estimé si son numérateur ou son dénominateur l'est.
    """
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
    pib, caisse = _pib(), _ressources_caisse()
    ratios = {m: _ratios(g, m) for m in ("pib", "ressources")}
    lignes = []
    for a in sorted(g["resultat"]):
        ligne = {_lab("col_annee"): a}
        estimes, estimes_ratios = [], []
        for nom, _ in _GRANDEURS:
            v, est = g[nom][a]
            ligne[_lab(f"col_{nom}")] = None if est else round(v, 1)
            if est:
                estimes.append(f"{_lab(f'col_{nom}').split(' (')[0]} : {_nombre(v)}")
        ligne[_lab("col_estimations")] = " ; ".join(estimes)
        ligne[_lab("col_pib")] = round(pib[a], 1)
        ligne[_lab("col_caisse")] = None if caisse[a][1] else round(caisse[a][0], 1)
        for m in ("pib", "ressources"):
            for nom, _ in _GRANDEURS:
                v, est = ratios[m][nom][a]
                col = f"{_lab(f'col_{nom}').split(' (')[0]} ({_lab(f'suffixe_{m}')})"
                ligne[col] = None if est else round(v, 3)
                if est:
                    estimes_ratios.append(f"{col} : {_nombre(v, 3)}")
        ligne[_lab("col_estimations_ratios")] = " ; ".join(estimes_ratios)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def _courbe(ax, serie: dict[int, tuple[float, bool]], couleur, marque, label):
    ans = sorted(serie)
    ax.plot(ans, [serie[a][0] for a in ans], "-", color=couleur, lw=1.8)
    for a in ans:
        v, est = serie[a]
        ax.plot([a], [v], marque, color=couleur, ms=4.5, mfc="white" if est else couleur)
    return Line2D([], [], color=couleur, marker=marque, lw=1.8, ms=4.5, label=label)


def vues() -> list[tuple[str, object]]:
    """Les trois vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{m}"), fig_resultat(m)) for m in MESURES]


def fig_resultat(mesure: str = "md"):
    """Haut : cotisations, pensions servies, produits financiers ; bas : résultat de gestion.

    `mesure` : "md" (millions de dinars courants), "pib" (% du PIB) ou "ressources" (% du
    total des ressources de la CNSS, toutes branches).
    """
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _ratios(_donnees(), mesure)
    ans = sorted(g["resultat"])
    suffixe = "" if mesure == "md" else f"_{mesure}"
    dec = {"md": 1, "pib": 2, "ressources": 1}[mesure]
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 7.6), sharex=True,
                                 gridspec_kw={"height_ratios": [3, 2]})

    poignees = [
        _courbe(ax, g["cotisations"], BLEU, "o", ft(_lab("lg_cotisations"))),
        _courbe(ax, g["pensions"], ORANGE, "s", ft(_lab("lg_pensions"))),
        _courbe(ax, g["financiers"], GRIS, "^", ft(_lab("lg_financiers"))),
    ]
    if mesure != "pib":
        ax.set_ylim(0, None)
    else:  # place pour le libellé de la rupture, en haut du cadre
        ax.set_ylim(0, max(v for n in ("cotisations", "pensions", "financiers")
                           for v, _ in g[n].values()) * 1.3)
    ax.set_ylabel("\n".join(ft(l) for l in _lab("y_haut" + suffixe).split("\n")))
    ax.set_title("\n".join(ft(l) for l in _lab("titre").split("\n")), pad=30)
    ax.grid(True, alpha=0.3)

    res = g["resultat"]
    for a in ans:
        v, est = res[a]
        bx.bar(a, v, width=0.7, color=BLEU if v >= 0 else ORANGE,
               hatch="////" if est else None, edgecolor="white", lw=0)
        bx.annotate(_nombre(v, dec), (a, v), textcoords="offset points",
                    xytext=(0, 3 if v >= 0 else -10), ha="center", fontsize=7,
                    color="#57606a")
    bx.axhline(0, color="#57606a", lw=0.8)
    bas, haut = min(v for v, _ in res.values()), max(v for v, _ in res.values())
    bx.set_ylim(bas * 1.25 if bas < 0 else 0, haut * 1.35 if haut > 0 else 1)
    bx.set_ylabel("\n".join(ft(l) for l in _lab("y_bas" + suffixe).split("\n")))
    if mesure == "pib" and ans[0] < RUPTURE_PIB <= ans[-1]:
        figtools.marque_rupture(ax, RUPTURE_PIB,
                                "\n".join(ft(l) for l in _lab("rupture").split("\n")))
        figtools.marque_rupture(bx, RUPTURE_PIB)
    for annee, cle in REALLOCATIONS:
        x = annee - 0.5  # date d'effet au 1er janvier : entre deux exercices
        for axe in (ax, bx):
            axe.axvline(x, color=VIOLET, ls=(0, (6, 2, 1, 2)), lw=1, zorder=1)
        # Au-dessus du cadre, hors des courbes et de la légende.
        ax.annotate("\n".join(ft(l) for l in _lab(cle).split("\n")), xy=(x, 1),
                    xycoords=("data", "axes fraction"), xytext=(0, 3),
                    textcoords="offset points", va="bottom", fontsize=7, color=VIOLET,
                    ha="left" if annee == REALLOCATIONS[0][0] else "center")
    bx.set_xlim(REALLOCATIONS[0][0] - 0.8, ans[-1] + 0.6)
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
    poignees.append(Line2D([], [], color=VIOLET, ls=(0, (6, 2, 1, 2)), lw=1,
                           label="\n".join(ft(l) for l in _lab("lg_realloc").split("\n"))))
    ax.legend(handles=poignees, loc="upper left", fontsize=8)
    fig.tight_layout()
    return fig
