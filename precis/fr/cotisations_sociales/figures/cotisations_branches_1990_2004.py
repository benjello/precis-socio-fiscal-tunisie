"""Figure « cotisations de la CNSS par branche, 1990-2004 » (source CNSS, comptes de bilan).

    from figures import cotisations_branches_1990_2004 as cb
    cb.fig_branches()   # cotisations par branche, MD courants, et la série encaissée 2000-2004
    cb.fig_branches("pib")         # cotisations par branche en % du PIB
    cb.fig_branches("ressources")  # en % des ressources de la CNSS, toutes branches
    cb.vues()           # les trois, pour figtools.figure_tabs
    cb.table()          # les montants et les ratios de la figure (onglet Données)

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
série sont tracés pour le montrer, dans la vue en dinars seulement : rapportés au total des
ressources des comptes de bilan, ils mêleraient deux comptabilités.

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
  - Ressources de la CNSS : la ligne « Total des ressources » du même tableau de l'ensemble
    (page 78), toutes branches, avec la convention tuniso-française et le régime
    complémentaire. Ses composantes en redonnent le total, et ce total est la somme des
    totaux des branches (pages 63, 67 et 75) : aucune ligne de transfert interne n'y
    figure, donc rien n'y est compté deux fois. Le dénominateur s'élargit aux accidents du
    travail en 1995 et à la protection sociale des travailleurs en 1997, comme le
    numérateur.

LES COLONNES MASQUÉES. Une cellule que la reliure masque porte une estimation provisoire ;
l'année est alors hachurée, et la table laisse la valeur publiée vide en donnant
l'estimation à part. Un ratio est estimé dès que son numérateur ou son dénominateur l'est. Le statut est lu cellule par cellule : rien n'est codé en dur.
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
PAGE_CAISSE = 78  # ensemble des régimes, toutes branches, avec CTF et RC
SERIE_PIB = "irpp-ratios"
RUPTURE_PIB = 1997  # base 1983 → base 1997 des comptes nationaux (voir l'en-tête)
MESURES = ("md", "pib", "ressources")

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
    "col_pib": {"fr": "PIB, ministère des Finances (MD)",
                "ar": "الناتج المحلي الإجمالي، وزارة المالية (م.د)"},
    "col_caisse": {"fr": "Total des ressources de la CNSS (MD)",
                   "ar": "مجموع موارد الصندوق الوطني للضمان الاجتماعي (م.د)"},
    "total": {"fr": "Total", "ar": "المجموع"},
    "suffixe_pib": {"fr": "% du PIB", "ar": "% من الناتج"},
    "suffixe_ressources": {"fr": "% des ressources de la CNSS", "ar": "% من موارد الصندوق"},
    "col_estimations_ratios": {"fr": "Estimations provisoires (ratios, %)",
                               "ar": "تقديرات مؤقّتة (نسب، %)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str, **valeurs) -> list[str]:
    return [figtools.fig_text(l) for l in _lab(key).format(**valeurs).split("\n")]


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0  # ni « -0,00 » ni « -0,0 »
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


def _ratios(g: dict, mesure: str) -> dict:
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


def _total(g: dict) -> dict[int, tuple[float, bool]]:
    ans = sorted(g["pensions"])
    return {a: (sum(g[n][a][0] for n, *_ in _BRANCHES), any(g[n][a][1] for n, *_ in _BRANCHES))
            for a in ans}


def _encaissees() -> dict[int, float]:
    return {int(r.annee): float(r.cotisations_md)
            for r in figtools.series(SERIE_ENCAISSEES).itertuples()}


def table():
    import pandas as pd
    g = _donnees()
    enc = _encaissees()
    ans = sorted(g["pensions"])
    pib, caisse = _pib(), _ressources_caisse()
    ratios = {m: _ratios({**g, "total": _total(g)}, m) for m in ("pib", "ressources")}
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
        ligne[_lab("col_pib")] = round(pib[a], 1)
        ligne[_lab("col_caisse")] = None if caisse[a][1] else round(caisse[a][0], 1)
        estimes_ratios = []
        for m in ("pib", "ressources"):
            for nom in [n for n, *_ in _BRANCHES] + ["total"]:
                v, e = ratios[m][nom][a]
                col = f"{_lab(nom)} ({_lab(f'suffixe_{m}')})"
                ligne[col] = None if e else round(v, 3)
                if e:
                    estimes_ratios.append(f"{col} : {_nombre(v, 3)}")
        ligne[_lab("col_estimations_ratios")] = " ; ".join(estimes_ratios)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def vues() -> list[tuple[str, object]]:
    """Les trois vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{m}"), fig_branches(m)) for m in MESURES]


def fig_branches(mesure: str = "md"):
    """Cotisations empilées par branche ; `mesure` : "md" (millions de dinars courants, avec
    la série encaissée), "pib" (% du PIB) ou "ressources" (% du total des ressources de la
    CNSS, toutes branches)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _ratios(_donnees(), mesure)
    ans = sorted(g["pensions"])
    dec = {"md": 0, "pib": 2, "ressources": 1}[mesure]
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

    # Série encaissée : vue en dinars seulement (un ratio mêlerait deux comptabilités).
    enc = {a: v for a, v in _encaissees().items() if a in bas} if mesure == "md" else {}
    if enc:
        ax.plot(list(enc), list(enc.values()), "D", color="#24292f", ms=5, mfc="#24292f")
        poignees.append(Line2D([], [], color="#24292f", marker="D", lw=0, ms=5,
                               label=ft(_lab("encaissees"))))
    estimees = sorted({a for s in g.values() for a, (_, e) in s.items() if e})
    if estimees:
        poignees.append(Patch(facecolor="white", edgecolor=GRIS, hatch="////",
                              label=ft(_lab("estime").format(
                                  annees=", ".join(map(str, estimees))))))

    # Apparition des branches AT/MP et PST : première année non nulle. Dans la vue en
    # dinars, les totaux croissent et le libellé se pose 230 MD au-dessus de la barre ; en
    # pourcentage, les barres sont de hauteur voisine : les libellés vont au-dessus de la
    # plus haute, en deux étages, à gauche de la rupture de 1997.
    haut = max(bas.values())
    for etage, (nom, cle) in enumerate((("atmp", "debut_atmp"), ("pst", "debut_pst"))):
        premiere = next((a for a in ans if g[nom][a][0] > 0), None)
        if premiere is not None:
            xy_texte = ((premiere - 1.6, bas[premiere] + 230) if mesure == "md"
                        else (premiere - 2.2, haut * (1.12 + 0.14 * etage)))
            ax.annotate("\n".join(_lignes(cle, a=premiere)), (premiere, bas[premiere]),
                        xytext=xy_texte,
                        fontsize=7.5,
                        color="#57606a", ha="center",
                        arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8))
    for a in (ans[0], ans[-1]):
        ax.annotate(_nombre(bas[a], dec), (a, max(bas[a], enc.get(a, 0))),
                    textcoords="offset points", xytext=(0, 7), ha="center", fontsize=8,
                    color="#24292f")

    ax.set_ylim(0, haut * (1.18 if mesure == "md" else 1.45))
    if mesure == "pib" and ans[0] < RUPTURE_PIB <= ans[-1]:
        figtools.marque_rupture(ax, RUPTURE_PIB,
                                "\n".join(ft(l) for l in _lab("rupture").split("\n")))
    ax.set_xticks(ans)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y" if mesure == "md" else f"y_{mesure}")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2,
              fontsize=8, frameon=False)
    fig.tight_layout()
    return fig
