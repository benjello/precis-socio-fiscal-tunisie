"""Taux marginal et taux moyen des barèmes de l'impôt sur le revenu du livre *Fiscalité*.

Deux figures, lues par `figtools.series()` seulement (séries de tranches `cpe-bareme` et
`irpp-bareme`, au format de `openfisca_tables.lignes_tranches`) et tracées par le composant
`taux_bareme` : la contribution personnelle d'État (cinq barèmes, revenus de 1962 à 1986) et
l'impôt sur le revenu (trois barèmes, revenus de 1990, 2017 et 2025).

Les seuils sont en dinars courants de l'année de chaque barème. Le taux moyen est le droit
du barème rapporté au revenu, barème appliqué par tranche ; il ne tient pas compte des
correctifs que le texte ajoute au barème (plafond de la cotisation effective, exemption
des petits revenus, minimum d'impôt).
"""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402
import taux_bareme  # noqa: E402

SERIE_CPE = "cpe-bareme"
SERIE_IRPP = "irpp-bareme"

ETATS_CPE = ("1962-01-01", "1965-01-01", "1980-01-01", "1983-01-01", "1986-01-01")
COULEURS_CPE = {"1962-01-01": "#8250df", "1965-01-01": "#bf3989", "1980-01-01": "#bf8700",
                "1983-01-01": "#0969da", "1986-01-01": "#1a7f37"}
# Deux échelles : les barèmes de 1962 à 1980 s'arrêtent au-dessous de 11 000 D, ceux de 1983 et
# de 1986 vont à 80 000 et 100 000 D.
GROUPES_CPE = (("g_cpe_ancien", ("1962-01-01", "1965-01-01", "1980-01-01"), 12_000,
                (0, 3_000, 6_000, 9_000, 12_000)),
               ("g_cpe_recent", ("1983-01-01", "1986-01-01"), 100_000,
                (0, 25_000, 50_000, 75_000, 100_000)))
ASSIETTES_CPE = {
    "g_cpe_ancien": (180, 640, 1_200, 2_000, 4_000, 6_000, 8_500, 10_200),
    "g_cpe_recent": (900, 3_000, 8_000, 25_000, 50_000, 80_000, 100_000),
}

ETATS_IRPP = ("1990-01-01", "2017-01-01", "2025-01-01")
COULEURS_IRPP = {"1990-01-01": "#bf8700", "2017-01-01": "#0969da", "2025-01-01": "#1a7f37"}
REVENU_MAX_IRPP = 80_000
ASSIETTES_IRPP = (1_500, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000, 70_000, 80_000)

_L = {
    "g_cpe_ancien": {"fr": "Revenus de 1962, 1965 et 1980", "ar": "مداخيل 1962 و1965 و1980"},
    "g_cpe_recent": {"fr": "Revenus de 1983 et 1986", "ar": "مداخيل 1983 و1986"},
    "etat_cpe_1962-01-01": {"fr": "revenus de 1962 (loi n° 62-73)",
                            "ar": "مداخيل 1962 (القانون عدد 62-73)"},
    "etat_cpe_1965-01-01": {"fr": "revenus de 1965 (loi n° 65-46)",
                            "ar": "مداخيل 1965 (القانون عدد 65-46)"},
    "etat_cpe_1980-01-01": {"fr": "revenus de 1980 (loi n° 79-66)",
                            "ar": "مداخيل 1980 (القانون عدد 79-66)"},
    "etat_cpe_1983-01-01": {"fr": "revenus de 1983 (loi n° 82-91)",
                            "ar": "مداخيل 1983 (القانون عدد 82-91)"},
    "etat_cpe_1986-01-01": {"fr": "revenus de 1986 (loi n° 85-109)",
                            "ar": "مداخيل 1986 (القانون عدد 85-109)"},
    "court_1962-01-01": {"fr": "1962", "ar": "1962"},
    "court_1965-01-01": {"fr": "1965", "ar": "1965"},
    "court_1980-01-01": {"fr": "1980", "ar": "1980"},
    "court_1983-01-01": {"fr": "1983", "ar": "1983"},
    "court_1986-01-01": {"fr": "1986", "ar": "1986"},
    "x_cpe": {"fr": "Revenu net imposable (dinars courants)",
              "ar": "الدخل الصافي الخاضع للضريبة (بالدينار الجاري)"},
    "title_cpe": {"fr": ("Contribution personnelle d'État : taux marginal et taux moyen du "
                         "barème selon le revenu, revenus de 1962 à 1986"),
                  "ar": ("المساهمة الشخصية للدولة: النسبة الحدية والنسبة المتوسّطة للجدول "
                         "حسب الدخل، مداخيل 1962 إلى 1986")},
    "c_groupe": {"fr": "Barèmes", "ar": "الجداول"},
    "c_revenu": {"fr": "Revenu net imposable (D)", "ar": "الدخل الصافي الخاضع للضريبة (د)"},
    "etat_irpp_1990-01-01": {"fr": "revenus de 1990 à 2016 (code de 1989)",
                             "ar": "مداخيل 1990 إلى 2016 (مجلة 1989)"},
    "etat_irpp_2017-01-01": {"fr": "revenus de 2017 à 2024 (loi n° 2016-78)",
                             "ar": "مداخيل 2017 إلى 2024 (القانون عدد 2016-78)"},
    "etat_irpp_2025-01-01": {"fr": "revenus à compter de 2025 (loi n° 2024-48)",
                             "ar": "مداخيل ابتداء من 2025 (القانون عدد 2024-48)"},
    "court_irpp_1990-01-01": {"fr": "1990", "ar": "1990"},
    "court_irpp_2017-01-01": {"fr": "2017", "ar": "2017"},
    "court_irpp_2025-01-01": {"fr": "2025", "ar": "2025"},
    "g_irpp": {"fr": "Impôt sur le revenu", "ar": "الضريبة على الدخل"},
    "title_irpp": {"fr": ("IRPP : taux marginal et taux moyen du barème selon le revenu, "
                          "revenus de 1990, 2017 et 2025"),
                   "ar": ("الضريبة على الدخل: النسبة الحدية والنسبة المتوسّطة للجدول حسب "
                          "الدخل، مداخيل 1990 و2017 و2025")},
    "y_taux": {"fr": "Taux (%)", "ar": "النسبة (%)"},
    "vue_taux_reel": {"fr": "Taux d'un revenu réel constant",
                      "ar": "نسب دخل حقيقي ثابت"},
    "moyen_court": {"fr": "taux moyen (trait plein)", "ar": "النسبة المتوسّطة (خط متصل)"},
    "marginal_court": {"fr": "taux marginal (tireté)", "ar": "النسبة الحدية (متقطّع)"},
    "y_seuil_d": {"fr": "Seuil (D)", "ar": "العتبة (د)"},
    "c_marg_ref": {"fr": "Taux marginal à {r} D de {base}",
                   "ar": "النسبة الحدية عند {r} د من {base}"},
    "vue_seuils": {"fr": "Seuils en dinars de {base}", "ar": "العتبات بدينار {base}"},
    "revenu_ref": {"fr": "Revenu de {r} D de {base}", "ar": "دخل بقيمة {r} د من {base}"},
    "seuil_zero": {"fr": "Fin de la tranche à taux nul", "ar": "نهاية الشريحة ذات النسبة المعدومة"},
    "seuil_haut": {"fr": "Début de la tranche au taux le plus élevé",
                   "ar": "بداية الشريحة ذات أعلى نسبة"},
    "courants": {"fr": "dinars courants", "ar": "بالدينار الجاري"},
    "constants": {"fr": "dinars de {base}", "ar": "بدينار {base}"},
    "c_annee": {"fr": "Année de revenus", "ar": "سنة المداخيل"},
    "reforme": {"fr": "Réforme {a}", "ar": "إصلاح {a}"},
    "y_taux_moyen": {"fr": "Taux du barème (%)", "ar": "نسب الجدول (%)"},
    "y_seuil": {"fr": "Seuil (dinars de {base})", "ar": "العتبة (بدينار {base})"},
    "title_annuel": {"fr": ("IRPP, année par année : taux moyen d'un même revenu réel et seuils "
                            "du barème en dinars de {base}, revenus de 1990 à {fin}"),
                     "ar": ("الضريبة على الدخل سنة بسنة: النسبة المتوسّطة لدخل حقيقي ثابت "
                            "وعتبات الجدول بدينار {base}، مداخيل 1990 إلى {fin}")},
    "c_bareme": {"fr": "Barème", "ar": "الجدول"},
    "c_tranches": {"fr": "Tranches<br>(dont la tranche à taux nul)",
                   "ar": "الشرائح<br>(منها الشريحة ذات النسبة المعدومة)"},
    "bareme_1990-01-01": {"fr": "code de 1989 (art. 44 § I)", "ar": "مجلة 1989 (الفصل 44 §I)"},
    "bareme_2017-01-01": {"fr": "loi n° 2016-78", "ar": "القانون عدد 2016-78"},
    "bareme_2025-01-01": {"fr": "loi n° 2024-48", "ar": "القانون عدد 2024-48"},
    "c_taux_max": {"fr": "Taux marginal maximal", "ar": "أعلى نسبة حدية"},
    "c_zero": {"fr": "Fin de la tranche à taux nul", "ar": "نهاية الشريحة ذات النسبة المعدومة"},
    "c_haut": {"fr": "Seuil du taux maximal", "ar": "عتبة أعلى نسبة"},
    "c_moyen_ref": {"fr": "Taux moyen à {r} D de {base}", "ar": "النسبة المتوسّطة عند {r} د من {base}"},
    "c_ipc": {"fr": "Indice des prix", "ar": "مؤشر الأسعار"},
    "u_courants": {"fr": "D courants", "ar": "د جارية"},
    "u_constants": {"fr": "D de {base}", "ar": "د {base}"},
    "u_pct": {"fr": "%", "ar": "%"},
    "u_ipc": {"fr": "base 100 en 1970", "ar": "الأساس 100 سنة 1970"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _bareme(serie: str, cle: str, date: str):
    return taux_bareme.bareme_a_la_date(figtools.series(serie), "bareme", cle, date)


def _panneaux_cpe():
    return [(_lab(g), {e: _bareme(SERIE_CPE, "cpe", e) for e in etats}, g)
            for g, etats, _m, _t in GROUPES_CPE]


def fig_cpe():
    """Deux cadres (barèmes de 1962 à 1980, de 1983 et 1986) : marginal en escalier, moyen en courbe."""
    p = _panneaux_cpe()
    return taux_bareme.fig_taux_moyens_marginaux(
        [(lib, etats) for lib, etats, _g in p], couleurs=COULEURS_CPE,
        libelles_etats={e: _lab("etat_cpe_" + e) for e in ETATS_CPE},
        assiette_max=[m for _g, _e, m, _t in GROUPES_CPE],
        xticks=[t for _g, _e, _m, t in GROUPES_CPE],
        xlabel=_lab("x_cpe"), ylabel=_lab("y_taux"), titre=_lab("title_cpe"), ymax=92)


def table_cpe():
    import pandas as pd
    p = _panneaux_cpe()
    morceaux = [
        taux_bareme.table_taux(
            [(lib, etats)], {e: _lab("court_" + e) for e in etats}, ASSIETTES_CPE[g],
            entete_panneau=_lab("c_groupe"), entete_assiette=_lab("c_revenu"))
        for lib, etats, g in p]
    return pd.concat(morceaux, ignore_index=True)


def _panneau_irpp():
    return [(_lab("g_irpp"), {e: _bareme(SERIE_IRPP, "irpp", e) for e in ETATS_IRPP})]


def fig_irpp():
    """Un cadre, trois barèmes : marginal en escalier, moyen en courbe."""
    return taux_bareme.fig_taux_moyens_marginaux(
        _panneau_irpp(), couleurs=COULEURS_IRPP,
        libelles_etats={e: _lab("etat_irpp_" + e) for e in ETATS_IRPP},
        assiette_max=REVENU_MAX_IRPP, colonnes=1, largeur=9.0,
        xticks=(0, 20_000, 40_000, 60_000, 80_000),
        xlabel=_lab("x_cpe"), ylabel=_lab("y_taux"), titre=_lab("title_irpp"), ymax=45)


def table_irpp():
    return taux_bareme.table_taux(
        _panneau_irpp(), {e: _lab("court_irpp_" + e) for e in ETATS_IRPP}, ASSIETTES_IRPP,
        entete_panneau=_lab("c_groupe"), entete_assiette=_lab("c_revenu"))


# --- L'IRPP année par année, en dinars courants et en dinars constants ------------------

REVENUS_REF = (10_000, 20_000, 40_000)  # dinars de l'année de base
COULEURS_REF = {10_000: "#bf8700", 20_000: "#0969da", 40_000: "#1a7f37"}
ANNEE_DEBUT = 1990
ANNEE_FIN = 2026


def _etat_de(annee: int) -> str:
    return max(e for e in ETATS_IRPP if int(e[:4]) <= annee)


def lignes_annuelles():
    """Une ligne par année de revenus : barème, seuils, taux ; constants à None sans indice."""
    ipc = dinars_constants.ipc()
    base = dinars_constants.ANNEE_BASE
    baremes = {e: _bareme(SERIE_IRPP, "irpp", e) for e in ETATS_IRPP}
    lignes = []
    for annee in range(ANNEE_DEBUT, ANNEE_FIN + 1):
        etat = _etat_de(annee)
        b = baremes[etat]
        zero = min(s for s, t in b if t > 0)  # première tranche taxée : fin de la tranche nulle
        taux_max = max(t for _s, t in b)
        haut = min(s for s, t in b if t == taux_max)
        k = ipc[base] / ipc[annee] if annee in ipc else None
        moyens, marginaux = {}, {}
        for r in REVENUS_REF:
            if k is None:
                moyens[r] = marginaux[r] = None
            else:
                moyens[r] = 100 * taux_bareme.taux_moyen(b, r / k)
                marginaux[r] = 100 * taux_bareme.taux_marginal(b, r / k)
        lignes.append({"annee": annee, "etat": etat, "tranches": len(b), "zero": zero,
                       "haut": haut, "taux_max": 100 * taux_max, "k": k,
                       "indice": ipc.get(annee), "moyens": moyens, "marginaux": marginaux})
    return lignes


def _marque_reformes(ax, vertical: bool = False) -> None:
    """Une ligne de rupture par réforme, libellée en haut du cadre.

    Le libellé se pose à droite du trait ; pour la dernière année, où il n'y a pas la place,
    à sa gauche. Le haut du cadre est dégagé pour qu'il ne chevauche aucune courbe.
    """
    haut = ax.get_ylim()[1]
    ax.set_ylim(0, haut * 1.12)
    for annee in (2017, 2025):
        figtools.marque_rupture(ax, annee)
        droite = annee < base_derniere() and not vertical
        ax.annotate(figtools.fig_text(_lab("reforme").format(a=annee)),
                    xy=(annee - 0.5, 1), xycoords=("data", "axes fraction"),
                    xytext=(4 if droite else -4, -4), textcoords="offset points",
                    ha="left" if droite else "right", va="top", fontsize=7.5, color="#57606a",
                    rotation=90 if vertical else 0)


def base_derniere() -> int:
    return dinars_constants.ANNEE_BASE


def _dinars(v: float) -> str:
    return f"{v:,.0f}".replace(",", " ")


def fig_irpp_taux_reel():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figtools.apply_lang_font()
    ft = figtools.fig_text
    base = dinars_constants.ANNEE_BASE
    lignes = [l for l in lignes_annuelles() if l["k"] is not None]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for r in REVENUS_REF:
        premier = True
        for etat in ETATS_IRPP:  # un segment par barème : aucun raccord entre deux textes
            seg = [l for l in lignes if l["etat"] == etat]
            courbe, = ax.plot([l["annee"] for l in seg], [l["moyens"][r] for l in seg], "-o",
                              ms=2.8, lw=1.9, color=COULEURS_REF[r],
                              label=ft(_lab("revenu_ref").format(r=_dinars(r), base=base))
                              if premier else None)
            premier = False
            figtools.infobulle(courbe, _lab("revenu_ref").format(r=_dinars(r), base=base))
            ax.step([l["annee"] for l in seg], [l["marginaux"][r] for l in seg], where="mid",
                    lw=1.0, ls=(0, (3, 2)), color=COULEURS_REF[r], alpha=0.9)
    ax.set_xlim(ANNEE_DEBUT - 0.5, base + 0.5)
    ax.set_ylim(0, None)
    _marque_reformes(ax)
    ax.set_xlabel(ft(_lab("c_annee")))
    ax.set_ylabel(ft(_lab("y_taux_moyen")))
    ax.grid(True, alpha=0.3)
    from matplotlib.lines import Line2D
    poignees, noms = ax.get_legend_handles_labels()
    poignees += [Line2D([], [], color="#57606a", lw=1.9), Line2D([], [], color="#57606a", lw=1.0,
                                                                  ls=(0, (3, 2)))]
    noms += [ft(_lab("moyen_court")), ft(_lab("marginal_court"))]
    ax.legend(poignees, noms, loc="upper center", bbox_to_anchor=(0.5, -0.13), fontsize=8,
              frameon=False, ncol=3)
    fig.tight_layout()
    return fig


def fig_irpp_seuils_constants():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figtools.apply_lang_font()
    ft = figtools.fig_text
    base = dinars_constants.ANNEE_BASE
    lignes = [l for l in lignes_annuelles() if l["k"] is not None]
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.0))
    for ax, cle, c in zip(axes, ("zero", "haut"), ("#bf8700", "#0969da")):
        for etat in ETATS_IRPP:
            seg = [l for l in lignes if l["etat"] == etat]
            xs = [l["annee"] for l in seg]
            ax.plot(xs, [l[cle] * l["k"] for l in seg], "-o", ms=2.8, lw=1.9, color=c,
                    label=ft(_lab("constants").format(base=base)) if etat == ETATS_IRPP[0] else None)
            ax.plot(xs, [l[cle] for l in seg], lw=1.2, ls=(0, (3, 2)), color=c,
                    label=ft(_lab("courants")) if etat == ETATS_IRPP[0] else None)
        ax.set_title(ft(_lab("seuil_" + cle)), fontsize=9.5)
        ax.set_xlim(ANNEE_DEBUT - 0.5, base + 0.5)
        ax.set_ylim(0, None)
        _marque_reformes(ax, vertical=True)
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, _p: _dinars(y)))
        ax.set_xlabel(ft(_lab("c_annee")))
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), fontsize=8, frameon=False,
                  ncol=2)
    axes[0].set_ylabel(ft(_lab("y_seuil_d")))
    fig.tight_layout()
    return fig


def fig_irpp_annuel():
    """Deux vues : taux moyen d'un même revenu réel ; seuils en dinars constants."""
    base = dinars_constants.ANNEE_BASE
    return [(_lab("vue_taux_reel"), fig_irpp_taux_reel()),
            (_lab("vue_seuils").format(base=base), fig_irpp_seuils_constants())]


def table_irpp_annuel_plat():
    """Le même tableau, en-têtes sur une ligne (onglet « Données », exports, figdata)."""
    df = table_irpp_annuel()
    return df.rename(columns=lambda c: c.replace("<br>(", " (").replace("<br>", " "))


def table_irpp_annuel():
    """Une ligne par année de revenus, 1990-2026, tout engendré depuis la série de tranches."""
    import pandas as pd
    base = dinars_constants.ANNEE_BASE
    cou, cst = _lab("u_courants"), _lab("u_constants").format(base=base)
    pct = _lab("u_pct")
    lignes = []
    for l in lignes_annuelles():
        k = l["k"]
        ligne = {_lab("c_annee"): l["annee"],
                 _lab("c_bareme"): _lab("bareme_" + l["etat"]),
                 _lab("c_tranches"): l["tranches"],
                 f"{_lab('c_zero')}<br>({cou})": round(l["zero"]),
                 f"{_lab('c_zero')}<br>({cst})": None if k is None else round(l["zero"] * k),
                 f"{_lab('c_haut')}<br>({cou})": round(l["haut"]),
                 f"{_lab('c_haut')}<br>({cst})": None if k is None else round(l["haut"] * k),
                 f"{_lab('c_taux_max')}<br>({pct})": round(l["taux_max"], 1)}
        for r in REVENUS_REF:
            m, mg = l["moyens"][r], l["marginaux"][r]
            ligne[f"{_lab('c_marg_ref').format(r=_dinars(r), base=base)}<br>({pct})"] = (
                None if mg is None else round(mg, 1))
            ligne[f"{_lab('c_moyen_ref').format(r=_dinars(r), base=base)}<br>({pct})"] = (
                None if m is None else round(m, 2))
        ligne[f"{_lab('c_ipc')}<br>({_lab('u_ipc')})"] = (
            None if l["indice"] is None else round(l["indice"], 1))
        lignes.append(ligne)
    df = pd.DataFrame(lignes)
    for c in df.columns:
        if "<br>(" + cou + ")" in c or "<br>(" + cst + ")" in c:
            df[c] = df[c].astype("Int64")
    return df


def markdown_irpp_annuel() -> str:
    """Le tableau annuel en Markdown : milliers séparés, virgule décimale, « — » sans indice."""
    import pandas as pd
    df = table_irpp_annuel()
    virgule = figtools.lang() != "ar"
    entetes = list(df.columns)

    def cellule(c, v):
        if v is None or pd.isna(v):
            return "—"
        if c in (entetes[0], entetes[2]):
            return str(int(v))
        if isinstance(v, str):
            return v
        if "<br>(%)" in c or "indice" in c.lower() or c.startswith(_lab("c_ipc")):
            t = (f"{float(v):.2f}" if c.startswith(_lab("c_moyen_ref")[:9])
                 else f"{float(v):.1f}") if "<br>(%)" in c else f"{float(v):.1f}"
            return t.replace(".", ",") if virgule else t
        return _dinars(float(v))

    lignes = ["| " + " | ".join(entetes) + " |",
              "|---|---|" + "|".join(["---:"] * (len(entetes) - 2)) + "|"]
    for _i, r in df.iterrows():
        lignes.append("| " + " | ".join(cellule(c, r[c]) for c in entetes) + " |")
    return "\n".join(lignes)


figtools.register_provenance(
    SERIE_CPE,
    titre=("Tarif de la contribution personnelle d'État, par tranche de revenu net imposable, "
           "pour les revenus de 1962, 1965, 1980, 1983 et 1986"),
    titre_ar=("تعريفة المساهمة الشخصية للدولة، حسب شريحة الدخل الصافي الخاضع للضريبة، "
              "لمداخيل 1962 و1965 و1980 و1983 و1986"),
    sources=["loi-62-73-cpe", "lf-1966", "loi79-66-lf1980", "lf-1983", "lf-1986"],
    unite="taux fixé pour la tranche, en pourcentage ; seuils en dinars courants",
    unite_ar="النسبة المحدَّدة للشريحة بالمائة؛ والعتبات بالدينار الجاري",
    perimetre=("cinq tarifs, une ligne par tranche et par tarif, avec le texte du Journal "
               "officiel qui le fixe ; les tarifs antérieurs à 1962 et ceux des revenus de 1966 "
               "à 1979 ne sont pas publiés ici"),
    perimetre_ar=("خمس تعريفات، سطر لكلّ شريحة ولكلّ تعريفة، مع نصّ الرائد الرسمي الذي يضبطها؛ "
                  "ولا تُنشر هنا التعريفات السابقة لسنة 1962 ولا تعريفات مداخيل 1966 إلى 1979"),
    caveats=("Le taux moyen est celui du tarif, barème appliqué par tranche. Il ne tient pas "
             "compte du plafond de la cotisation effective, ni de l'exemption des revenus qui "
             "ne dépassent pas 100 dinars en 1965, ni du SMIG en 1986."),
    caveats_ar=("النسبة المتوسّطة هي نسبة التعريفة بتطبيق الجدول حسب الشرائح، دون اعتبار سقف "
                "الأداء الفعلي ولا إعفاء المداخيل التي لا تتجاوز 100 دينار في 1965 ولا الأجر "
                "الأدنى المضمون في 1986."),
)

figtools.register_provenance(
    SERIE_IRPP,
    titre=("Barème de l'impôt sur le revenu des personnes physiques (art. 44 § I du code), par "
           "tranche de revenu net imposable, pour les revenus de 1990, 2017 et 2025"),
    titre_ar=("جدول الضريبة على دخل الأشخاص الطبيعيين (الفصل 44 §I من المجلة)، حسب شريحة "
              "الدخل الصافي الخاضع للضريبة، لمداخيل 1990 و2017 و2025"),
    sources=["code-irpp-is-1990", "lf-2017", "lf-2025"],
    unite="taux fixé pour la tranche, en pourcentage ; seuils en dinars courants",
    unite_ar="النسبة المحدَّدة للشريحة بالمائة؛ والعتبات بالدينار الجاري",
    perimetre=("trois barèmes, une ligne par tranche et par date d'effet ; les dates sont des "
               "années de revenus, au 1er janvier"),
    perimetre_ar="ثلاثة جداول، سطر لكلّ شريحة ولكلّ تاريخ نفاذ؛ والتواريخ سنوات مداخيل في غرّة جانفي",
    caveats=("Le taux moyen est celui du barème, barème appliqué par tranche, avant déductions "
             "pour charges de famille, minimum d'impôt et régimes dérogatoires."),
    caveats_ar=("النسبة المتوسّطة هي نسبة الجدول بتطبيقه حسب الشرائح، قبل الطروحات العائلية "
                "والحدّ الأدنى للضريبة والأنظمة الاستثنائية."),
)
