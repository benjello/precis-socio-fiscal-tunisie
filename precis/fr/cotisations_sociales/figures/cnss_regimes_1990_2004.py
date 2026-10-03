"""Figure « ressources et emplois par régime de la CNSS, 1990-2004 » (source CNSS).

    from figures import cnss_regimes_1990_2004 as rg
    rg.fig_regimes()                 # taux de couverture des emplois par les ressources
    rg.fig_regimes("md")             # résultat de gestion, MD courants
    rg.fig_regimes("pib")            # résultat de gestion en % du PIB
    rg.fig_regimes("ressources")     # résultat en % des ressources de la CNSS
    rg.vues()                        # les quatre, pour figtools.figure_tabs
    rg.table()                       # format long, une ligne par année et par régime

D'OÙ VIENNENT LES DONNÉES. Le tableau de l'ensemble des régimes qui donne, régime par régime,
le total des ressources, le total des emplois et le résultat de gestion (page 79 de la
Rétrospective financière 1990-2004 de la CNSS, avec la convention tuniso-française et le
régime complémentaire), série `cnss-retrospective-ressources-emplois` de tunisia-data,
snapshotée dans `precis/_seriescache/`. Comptabilité des « Bilans » : droits constatés, en
milliers de dinars courants, convertis ici en millions. Chaque régime y est pris toutes
branches confondues — prestations familiales, assurances sociales et pensions, selon les
branches qu'il a. Ses lignes redonnent les tableaux propres de chaque régime (pages 16, 22,
26, 32, 36, 40, 44, 48 et 52), et leur somme le total de l'ensemble : le document est
construit par sommation des régimes. Aucune ligne n'y transfère de ressource d'un régime à
un autre.

CE QUI EST TRACÉ. Neuf panneaux, un par régime, chacun à son échelle : le régime général
pèse cent fois plus que les petits régimes, dont les montants se comptent en milliers de
dinars et dont les ratios varient d'autant plus.
  - Vue « taux de couverture » : ressources ÷ emplois, en %, avec la ligne de 100 % où les
    ressources de l'année couvrent exactement ses emplois.
  - Vues du résultat : le résultat de gestion du tableau en millions de dinars, en % du PIB
    (série `irpp-ratios`, rupture de base des comptes nationaux en 1997, marquée et non
    corrigée) et en % du « Total des ressources » de la CNSS, toutes branches et tous
    régimes (page 78) — dénominateurs documentés dans l'en-tête de
    `retraites/figures/rsna_resultat_1990_2004.py`.
Une année où le régime n'a ni ressources ni emplois n'est pas tracée : le régime n'existe
pas encore, ou n'a pas encore de comptabilité séparée (étudiants avant 1995, d'après la note
du document, page 22). Le régime complémentaire, la convention tuniso-française, les
accidents du travail et la protection sociale des travailleurs, qui figurent aussi au
tableau, ne sont pas tracés ici.

LES COLONNES MASQUÉES. Une cellule que la reliure masque porte une estimation provisoire
(`valeur_ou_estimation`, `valeur` vide) ; le point ou la barre de l'année est alors creux
ou hachuré, et la table laisse la valeur publiée vide en donnant l'estimation à part. Un
ratio est estimé dès que son numérateur ou son dénominateur l'est. Le statut est lu cellule
par cellule : rien n'est codé en dur.
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

SERIE = "cnss-retrospective-ressources-emplois"
PAGE = 79  # ensemble des régimes, par régime : ressources, emplois, résultat
PAGE_CAISSE = 78  # ensemble des régimes, toutes branches, avec CTF et RC
SERIE_PIB = "irpp-ratios"
RUPTURE_PIB = 1997  # base 1983 → base 1997 des comptes nationaux
MESURES = ("couverture", "md", "pib", "ressources")

BLEU, ORANGE, GRIS = "#08519c", "#bc4c00", "#6e7781"

# Suffixe des clés de la page 79, dans l'ordre des panneaux.
REGIMES = ("RSNA", "RSA", "RAA", "RTNS_NA", "RTNS_A", "RTTE", "RTFR", "ARTISTES", "ETUD")

_L = {
    "titre": {"fr": "Ressources et emplois par régime de la CNSS, toutes branches, 1990-2004",
              "ar": "الموارد والاستعمالات حسب أنظمة الصندوق الوطني للضمان الاجتماعي، "
                    "كلّ الفروع، 1990-2004"},
    "sous_titre_couverture": {"fr": "Taux de couverture des emplois par les ressources "
                                    "(ressources ÷ emplois, %)",
                              "ar": "نسبة تغطية الاستعمالات بالموارد (الموارد ÷ الاستعمالات، %)"},
    "sous_titre_md": {"fr": "Résultat de gestion, millions de dinars courants",
                      "ar": "نتيجة التصرّف، بملايين الدنانير الجارية"},
    "sous_titre_pib": {"fr": "Résultat de gestion, % du PIB",
                       "ar": "نتيجة التصرّف، % من الناتج المحلي الإجمالي"},
    "sous_titre_ressources": {"fr": "Résultat de gestion, % des ressources de la CNSS",
                              "ar": "نتيجة التصرّف، % من موارد الصندوق"},
    "vue_couverture": {"fr": "Taux de couverture", "ar": "نسبة التغطية"},
    "vue_md": {"fr": "Résultat, millions de dinars", "ar": "النتيجة، بملايين الدنانير"},
    "vue_pib": {"fr": "Résultat, % du PIB", "ar": "النتيجة، % من الناتج"},
    "vue_ressources": {"fr": "Résultat, % des ressources de la CNSS",
                       "ar": "النتيجة، % من موارد الصندوق"},
    "rupture": {"fr": "base des\ncomptes", "ar": "أساس\nالحسابات"},
    "RSNA": {"fr": "Salariés non agricoles", "ar": "الأجراء غير الفلاحيين"},
    "RSA": {"fr": "Salariés agricoles", "ar": "الأجراء الفلاحيون"},
    "RAA": {"fr": "Régime agricole amélioré", "ar": "النظام الفلاحي المحسَّن"},
    "RTNS_NA": {"fr": "Non-salariés, secteur non agricole",
                "ar": "العملة غير الأجراء، القطاع غير الفلاحي"},
    "RTNS_A": {"fr": "Non-salariés, secteur agricole",
               "ar": "العملة غير الأجراء، القطاع الفلاحي"},
    "RTTE": {"fr": "Tunisiens à l'étranger", "ar": "العملة التونسيون بالخارج"},
    "RTFR": {"fr": "Travailleurs à faibles revenus", "ar": "العملة ذوو الدخل المحدود"},
    "ARTISTES": {"fr": "Artistes, créateurs et intellectuels",
                 "ar": "الفنانون والمبدعون والمثقفون"},
    "ETUD": {"fr": "Étudiants", "ar": "الطلبة"},
    "lg_couvert": {"fr": "Ressources ≥ emplois", "ar": "الموارد ≥ الاستعمالات"},
    "lg_non_couvert": {"fr": "Ressources < emplois", "ar": "الموارد < الاستعمالات"},
    "lg_excedent": {"fr": "Excédent", "ar": "فائض"},
    "lg_deficit": {"fr": "Déficit", "ar": "عجز"},
    "lg_estime": {"fr": "{annees} : valeur en partie estimée (reliure du document)",
                  "ar": "{annees}: قيمة مقدّرة جزئياً (تجليد الوثيقة)"},
    "estime": {"fr": "estimé", "ar": "مقدّر"},
    "ib_couverture": {"fr": "{regime}, {a} : ressources {r} MD, emplois {e} MD, couverture {c} %",
                      "ar": "{regime}، {a}: الموارد {r} م.د، الاستعمالات {e} م.د، التغطية {c} %"},
    "ib_resultat": {"fr": "{regime}, {a} : résultat {v}", "ar": "{regime}، {a}: النتيجة {v}"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_regime": {"fr": "Régime", "ar": "النظام"},
    "col_ressources": {"fr": "Total des ressources (MD)", "ar": "مجموع الموارد (م.د)"},
    "col_emplois": {"fr": "Total des emplois (MD)", "ar": "مجموع الاستعمالات (م.د)"},
    "col_resultat": {"fr": "Résultat de gestion (MD)", "ar": "نتيجة التصرّف (م.د)"},
    "col_couverture": {"fr": "Taux de couverture (%)", "ar": "نسبة التغطية (%)"},
    "col_resultat_pib": {"fr": "Résultat (% du PIB)", "ar": "النتيجة (% من الناتج)"},
    "col_resultat_ressources": {"fr": "Résultat (% des ressources de la CNSS)",
                                "ar": "النتيجة (% من موارد الصندوق)"},
    "col_estimations": {"fr": "Estimations provisoires", "ar": "تقديرات مؤقّتة"},
    "col_pib": {"fr": "PIB, ministère des Finances (MD)",
                "ar": "الناتج المحلي الإجمالي، وزارة المالية (م.د)"},
    "col_caisse": {"fr": "Total des ressources de la CNSS (MD)",
                   "ar": "مجموع موارد الصندوق الوطني للضمان الاجتماعي (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str, **valeurs) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key).format(**valeurs).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0  # ni « -0,00 » ni « -0,0 »
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _cellules() -> dict[tuple[str, int], tuple[float, bool]]:
    """{(clé, année): (MD, estimé ?)} pour le tableau de la page PAGE."""
    import pandas as pd
    d = figtools.series(SERIE)
    d = d[d["page"] == PAGE]
    assert set(d["regime"]) == {"ENSEMBLE"} and set(d["variante"]) == {"avec CTF & RC"}, \
        f"la page {PAGE} n'est plus le tableau de l'ensemble, par régime"
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


def _donnees() -> dict[str, dict[int, dict[str, tuple[float, bool]]]]:
    """{régime: {année: {"ress"|"empl"|"res": (MD, estimé ?)}}}, années où le régime a des
    ressources ou des emplois."""
    c = _cellules()
    ans = sorted({a for _, a in c})
    out = {}
    for r in REGIMES:
        out[r] = {}
        for a in ans:
            x = {k: c[(f"{k}_{r}", a)] for k in ("ress", "empl", "res")}
            if x["ress"][0] == 0 and x["empl"][0] == 0:
                continue  # régime pas encore institué, ou sans comptabilité séparée
            assert abs(x["ress"][0] - x["empl"][0] - x["res"][0]) < 0.01, (r, a)
            out[r][a] = x
    return out


def _serie(x: dict, a: int, mesure: str, pib: dict, caisse: dict) -> tuple[float | None, bool]:
    """La grandeur tracée pour l'année `a` d'un régime, et si elle est estimée ; le taux de
    couverture n'est pas défini sans emplois."""
    if mesure == "couverture":
        if x["empl"][0] == 0:
            return None, False
        return 100 * x["ress"][0] / x["empl"][0], x["ress"][1] or x["empl"][1]
    v, est = x["res"]
    if mesure == "md":
        return v, est
    if mesure == "pib":
        return 100 * v / pib[a], est
    if mesure == "ressources":
        return 100 * v / caisse[a][0], est or caisse[a][1]
    raise ValueError(mesure)


def table():
    import pandas as pd
    g = _donnees()
    pib, caisse = _pib(), _ressources_caisse()
    lignes = []
    for a in sorted({a for r in g for a in g[r]}):
        for r in REGIMES:
            if a not in g[r]:
                continue
            x = g[r][a]
            ligne = {_lab("col_annee"): a, _lab("col_regime"): _lab(r)}
            estimes = []
            for k, col in (("ress", "col_ressources"), ("empl", "col_emplois"),
                           ("res", "col_resultat")):
                v, est = x[k]
                ligne[_lab(col)] = None if est else round(v, 3)
                if est:
                    estimes.append(f"{_lab(col)} : {_nombre(v, 3)}")
            for m, col, dec in (("couverture", "col_couverture", 1),
                                ("pib", "col_resultat_pib", 4),
                                ("ressources", "col_resultat_ressources", 3)):
                v, est = _serie(x, a, m, pib, caisse)
                ligne[_lab(col)] = None if est or v is None else round(v, dec)
                if est and v is not None:
                    estimes.append(f"{_lab(col)} : {_nombre(v, dec)}")
            ligne[_lab("col_estimations")] = " ; ".join(estimes)
            ligne[_lab("col_pib")] = round(pib[a], 1)
            ligne[_lab("col_caisse")] = None if caisse[a][1] else round(caisse[a][0], 1)
            lignes.append(ligne)
    return pd.DataFrame(lignes)


def vues() -> list[tuple[str, object]]:
    """Les quatre vues de la figure, pour `figtools.figure_tabs`."""
    return [(_lab(f"vue_{m}"), fig_regimes(m)) for m in MESURES]


def fig_regimes(mesure: str = "couverture"):
    """Un panneau par régime ; `mesure` : "couverture" (ressources ÷ emplois, %), "md"
    (résultat, MD courants), "pib" (résultat, % du PIB) ou "ressources" (résultat, % du
    total des ressources de la CNSS)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _donnees()
    pib, caisse = _pib(), _ressources_caisse()
    ans_tous = sorted({a for r in g for a in g[r]})
    dec = {"couverture": 0, "md": 2, "pib": 4, "ressources": 3}[mesure]
    fig, axes = plt.subplots(3, 3, figsize=(10, 9), sharex=True)
    estimees = set()
    for ax, r in zip(axes.flat, REGIMES):
        ans = sorted(g[r])
        serie = {a: _serie(g[r][a], a, mesure, pib, caisse) for a in ans}
        serie = {a: v for a, v in serie.items() if v[0] is not None}
        estimees |= {a for a, (_, e) in serie.items() if e}
        if mesure == "couverture":
            ax.axhline(100, color="#57606a", lw=0.9, ls=(0, (4, 2)))
            pts = sorted(serie)
            ax.plot(pts, [serie[a][0] for a in pts], "-", color=GRIS, lw=1.2)
            for a in pts:
                v, est = serie[a]
                couleur = BLEU if v >= 100 else ORANGE
                p, = ax.plot([a], [v], "o", color=couleur, ms=4.5,
                             mfc="white" if est else couleur)
                x = g[r][a]
                figtools.infobulle(p, _lab("ib_couverture").format(
                    regime=_lab(r), a=a, r=_nombre(x["ress"][0], 3),
                    e=_nombre(x["empl"][0], 3), c=_nombre(v, 0))
                    + (f" ({_lab('estime')})" if est else ""))
            haut = max([v for v, _ in serie.values()] + [100])
            ax.set_ylim(0, haut * 1.15)
        else:
            for a, (v, est) in serie.items():
                b = ax.bar(a, v, width=0.72, color=BLEU if v >= 0 else ORANGE,
                           hatch="////" if est else None, edgecolor="white", lw=0)
                figtools.infobulle(b.patches[0], _lab("ib_resultat").format(
                    regime=_lab(r), a=a, v=_nombre(v, dec + 1))
                    + (f" ({_lab('estime')})" if est else ""))
            ax.axhline(0, color="#57606a", lw=0.8)
            valeurs = [v for v, _ in serie.values()]
            bas, haut = min(valeurs + [0]), max(valeurs + [0])
            marge = 0.12 * (haut - bas or 1)
            ax.set_ylim(bas - marge, haut + marge)
            if mesure == "pib" and ans_tous[0] < RUPTURE_PIB <= ans_tous[-1]:
                figtools.marque_rupture(ax, RUPTURE_PIB)
        ax.set_title(ft(_lab(r)), fontsize=9)
        ax.tick_params(labelsize=7)
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_xlim(ans_tous[0] - 0.7, ans_tous[-1] + 0.7)
    for ax in axes[-1]:
        ax.set_xticks([a for a in ans_tous if a % 2 == 0])
        ax.tick_params(axis="x", labelsize=7, rotation=45)

    if mesure == "couverture":
        poignees = [plt.Line2D([], [], color=BLEU, marker="o", lw=0,
                               label=ft(_lab("lg_couvert"))),
                    plt.Line2D([], [], color=ORANGE, marker="o", lw=0,
                               label=ft(_lab("lg_non_couvert")))]
    else:
        poignees = [Patch(color=BLEU, label=ft(_lab("lg_excedent"))),
                    Patch(color=ORANGE, label=ft(_lab("lg_deficit")))]
    if estimees:
        poignees.append(Patch(facecolor="white", edgecolor=GRIS, hatch="////",
                              label=ft(_lab("lg_estime").format(
                                  annees=", ".join(map(str, sorted(estimees)))))))
    fig.legend(handles=poignees, loc="lower center", ncol=len(poignees), fontsize=8,
               frameon=False, bbox_to_anchor=(0.5, 0))
    fig.suptitle(_lignes("titre") + "\n" + _lignes(f"sous_titre_{mesure}"), fontsize=11)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    return fig
