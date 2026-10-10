"""Figure « allocations familiales versées par la CNSS, 1990-2004 » (source CNSS).

    from figures import cnss_allocations_familiales as caf
    caf.fig_allocations()   # composantes en MD courants
    caf.fig_allocations("reel")        # composantes en MD de 2025
    caf.fig_allocations("pib")         # composantes en % du PIB
    caf.fig_allocations("ressources")  # en % des ressources de la CNSS, toutes branches
    caf.vues()              # les quatre, pour figtools.figure_tabs
    caf.table()             # les montants et les ratios de la figure (onglet Données)

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

LE DÉFLATEUR. Celui du précis (`scripts/dinars_constants.py`) : l'indice des prix à la
consommation de longue période, base 100 en 1970 (série `ipc-longue-periode`), prolongé
jusqu'à l'année de base par l'indice que relaie la Banque centrale (`bct-ipc-base2015`) ;
dinars de 2025 = montant × IPC(2025) / IPC(année). Les dinars courants et les dinars de 2025
ont chacun leur vue : un facteur de trois à cinq les sépare sur la période, et un seul axe
écraserait les premiers. Le document de la CNSS ne compte ni les allocataires ni les
enfants : le total déflaté mesure la dépense, non le montant par enfant.

LES DÉNOMINATEURS DES VUES EN POURCENTAGE. Elles se passent de déflateur : numérateur et
dénominateur sont en dinars courants de la même année.
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
    régimes, toutes branches, avec la convention tuniso-française et le régime
    complémentaire (page 78). Ses composantes en redonnent le total, et ce total est la
    somme des totaux des branches (pages 63, 67 et 75) : aucune ligne de transfert interne
    n'y figure, donc rien n'y est compté deux fois. Les accidents du travail n'y ont de
    ressources qu'à partir de 1995 et la protection sociale des travailleurs à partir de
    1997 : le dénominateur s'élargit à ces dates.

LES COLONNES MASQUÉES. Comme pour toutes les figures tirées de ce document, une cellule que la
reliure masque porte une estimation provisoire ; l'année est alors hachurée (barres) et creuse
(courbe), et la table laisse la valeur publiée vide en donnant l'estimation à part. Un ratio
est estimé dès que son numérateur ou son dénominateur l'est.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402
from dinars_constants import ANNEE_BASE, SERIES_IPC  # noqa: E402, F401

SERIE = "cnss-retrospective-ressources-emplois"
PAGE_CAISSE = 78  # ensemble des régimes, toutes branches, avec CTF et RC
SERIE_PIB = "irpp-ratios"
RUPTURE_PIB = 1997  # base 1983 → base 1997 des comptes nationaux (voir l'en-tête)
MESURES = ("md", "reel", "pib", "ressources")

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
    "y": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "y_reel": {"fr": f"Millions de dinars de {ANNEE_BASE}",
               "ar": f"بملايين دنانير سنة {ANNEE_BASE}"},
    "y_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_ressources": {"fr": "% des ressources de la CNSS",
                     "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "vue_md": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "vue_reel": {"fr": f"Millions de dinars de {ANNEE_BASE}",
                 "ar": f"بملايين دنانير سنة {ANNEE_BASE}"},
    "vue_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "vue_ressources": {"fr": "% des ressources de la CNSS",
                       "ar": "% من موارد الصندوق الوطني للضمان الاجتماعي"},
    "rupture": {"fr": "changement de base\ndes comptes nationaux",
                "ar": "تغيير سنة أساس\nالحسابات القومية"},
    "x": {"fr": "Année", "ar": "السنة"},
    "af_rsna": {"fr": "Allocations familiales, régime des salariés non agricoles",
                "ar": "المنح العائلية، نظام الأجراء غير الفلاحيين"},
    "af_autres": {"fr": "Allocations familiales, régime dit « agricole amélioré » dans les "
                        "comptes de la caisse, et étudiants",
                  "ar": "المنح العائلية، النظام الفلاحي المحسّن والطلبة"},
    "msu": {"fr": "Majoration pour salaire unique",
            "ar": "الزيادة بعنوان الأجر الوحيد"},
    "af_pensionnes": {"fr": "Allocations familiales et salaire unique des pensionnés, "
                            "imputées sur la branche des pensions jusqu'en 1994",
                      "ar": "المنح العائلية والأجر الوحيد للمتقاعدين، المحمولة على فرع "
                            "الجرايات إلى سنة 1994"},
    "af_ctf": {"fr": "Allocations familiales, convention tuniso-française",
               "ar": "المنح العائلية، الاتفاقية التونسية الفرنسية"},
    "estime": {"fr": "{annees} : valeur en partie estimée (reliure du document)",
               "ar": "{annees}: قيمة مقدّرة جزئياً (تجليد الوثيقة)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_total": {"fr": "Total, dinars courants (MD)", "ar": "المجموع، بالدينار الجاري (م.د)"},
    "col_indice": {"fr": f"Indice des prix, base 100 en {ANNEE_BASE}",
                   "ar": f"الرقم القياسي للأسعار، أساس 100 سنة {ANNEE_BASE}"},
    "col_reel": {"fr": f"Total, dinars de {ANNEE_BASE} (MD)",
                 "ar": f"المجموع، بدينار سنة {ANNEE_BASE} (م.د)"},
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


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0  # ni « -0,00 » ni « -0,0 »
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

    "md" : inchangées ; "reel" : en dinars de l'année de base ; "pib" : en % du PIB ;
    "ressources" : en % du total des ressources de la caisse. Un ratio est estimé si son
    numérateur ou son dénominateur l'est.
    """
    if mesure == "md":
        return g
    if mesure == "reel":
        ind = _indice()
        return {nom: {a: (100 * v / ind[a], est) for a, (v, est) in s.items()}
                for nom, s in g.items()}
    if mesure == "pib":
        den = {a: (v, False) for a, v in _pib().items()}
    elif mesure == "ressources":
        den = _ressources_caisse()
    else:
        raise ValueError(mesure)
    return {nom: {a: (100 * v / den[a][0], est or den[a][1]) for a, (v, est) in s.items()}
            for nom, s in g.items()}


def _indice() -> dict[int, float]:
    """IPC annuel du précis, ramené à 100 en ANNEE_BASE."""
    ipc = dinars_constants.ipc()
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
    pib, caisse = _pib(), _ressources_caisse()
    ratios = {m: _ratios({**g, "total": tot}, m) for m in ("pib", "ressources")}
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
        ligne[_lab("col_pib")] = round(pib[a], 1)
        ligne[_lab("col_caisse")] = None if caisse[a][1] else round(caisse[a][0], 1)
        estimes_ratios = []
        for m in ("pib", "ressources"):
            for nom in [n for n, _, _ in _COMPOSANTES] + ["total"]:
                v, est = ratios[m][nom][a]
                col = f"{_lab(nom)} ({_lab(f'suffixe_{m}')})"
                ligne[col] = None if est else round(v, 3)
                if est:
                    estimes_ratios.append(f"{col} : {_nombre(v, 3)}")
        ligne[_lab("col_estimations_ratios")] = " ; ".join(estimes_ratios)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def vues() -> list[tuple[str, object]]:
    """Les quatre vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{m}"), fig_allocations(m)) for m in MESURES]


def fig_allocations(mesure: str = "md"):
    """Composantes empilées ; `mesure` : "md" (millions de dinars courants), "reel" (millions
    de dinars de l'année de base), "pib" (% du PIB) ou "ressources" (% du total des
    ressources de la CNSS, toutes branches)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g, ind, ans, tot = _totaux()
    if mesure != "md":
        r = _ratios({**g, "total": tot}, mesure)
        tot = r.pop("total")
        g = r
    dec = {"md": 1, "reel": 1, "pib": 3, "ressources": 1}[mesure]
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

    for a in (ans[0], ans[-1]):
        ax.annotate(_nombre(tot[a][0], dec), (a, tot[a][0]), textcoords="offset points",
                    xytext=(0, 4), ha="center", fontsize=8, color="#24292f")
    estimees = [a for a in ans if tot[a][1]]
    if estimees:
        poignees.append(Patch(facecolor="white", edgecolor=GRIS, hatch="////",
                              label=ft(_lab("estime").format(
                                  annees=", ".join(map(str, estimees))))))

    ax.set_ylim(0, max(v for v, _ in tot.values()) * (1.25 if mesure == "pib" else 1.15))
    if mesure == "pib" and ans[0] < RUPTURE_PIB <= ans[-1]:
        figtools.marque_rupture(ax, RUPTURE_PIB,
                                "\n".join(ft(l) for l in _lab("rupture").split("\n")))
    ax.set_xticks(ans)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y" if mesure == "md" else f"y_{mesure}")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=1,
              fontsize=8, frameon=False)
    fig.tight_layout()
    return fig
