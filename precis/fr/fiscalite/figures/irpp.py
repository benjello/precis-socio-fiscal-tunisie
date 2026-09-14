"""Figure « rendement de l'IRPP » du livre *Fiscalité*.

Frontière habituelle : la série vient de `tunisia_data` (entrepôt `irpp-ratios`) ; ici on
prépare le figdata téléchargeable et on rend la figure.

LA RUPTURE DE SÉRIE EST LE SUJET, PAS UN DÉTAIL. La rubrique « impôts sur le revenu » du
ministère des Finances est continue depuis 1986, mais elle ne désigne pas la même chose
avant et après 1990 : l'IRPP naît du code annexé à la loi n° 89-114 et ne s'applique
qu'aux revenus réalisés à compter du 1er janvier 1990. Avant, la ligne agrège les impôts
cédulaires et la contribution personnelle d'État, que ce code abroge — c'est-à-dire
l'objet de la section précédente du chapitre.

La figure le montre au lieu de le taire : les quatre premières années sont tracées en
pointillé gris, séparées du reste par une bande verticale, et la légende nomme ce qu'elles
mesurent réellement.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDATA = HERE.parent / "figdata"
SERIE = "irpp-ratios"
SERIE_COMPOSITION = "recettes-fiscales-composition"

# Première année d'application de l'IRPP : revenus réalisés à compter du 1er janvier 1990,
# code annexé à la loi n° 89-114 du 30 décembre 1989.
ANNEE_IRPP = 1990

_L = {
    "lg_pib_avant": {
        "fr": "Impôts cédulaires et contribution personnelle d'État / PIB",
        "ar": "الأداءات النوعية والمساهمة الشخصية للدولة / الناتج المحلي الإجمالي"},
    "lg_pib": {"fr": "IRPP / PIB (éch. gauche)",
               "ar": "الضريبة على دخل الأشخاص الطبيعيين / الناتج المحلي الإجمالي (يسار)"},
    "lg_dep": {"fr": "IRPP / dépenses de l'État (éch. droite)",
               "ar": "الضريبة على الدخل / نفقات الدولة (يمين)"},
    "y_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_dep": {"fr": "En % des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "title": {"fr": "Ce que rapporte l'impôt sur le revenu, 1986-2025",
              "ar": "مردود الضريبة على الدخل، 1986-2025"},
    "rupture": {"fr": "création de l'IRPP\n(code de 1989, revenus 1990)",
                "ar": "إحداث الضريبة على دخل الأشخاص الطبيعيين\n(مجلة 1989، مداخيل 1990)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_mdt": {"fr": "Impôt sur le revenu (MDT)", "ar": "الضريبة على الدخل (م.د)"},
    "col_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "col_dep": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "col_rec": {"fr": "% des recettes fiscales", "ar": "% من المداخيل الجبائية"},
    "col_sal": {"fr": "Part des salaires dans l'impôt (%)",
                "ar": "حصة الأجور في الضريبة (%)"},
}


_C = {
    "irpp": {"fr": "Impôt sur le revenu", "ar": "الضريبة على الدخل"},
    "is": {"fr": "Impôt sur les sociétés", "ar": "الضريبة على الشركات"},
    "tva": {"fr": "TVA", "ar": "الأداء على القيمة المضافة"},
    "consommation": {"fr": "Droits de consommation", "ar": "معاليم الاستهلاك"},
    "douanes": {"fr": "Droits de douanes", "ar": "المعاليم الديوانية"},
    "autres": {"fr": "Autres impôts indirects", "ar": "أداءات غير مباشرة أخرى"},
    "y": {"fr": "Part des recettes fiscales (%)", "ar": "الحصة من المداخيل الجبائية (%)"},
    "titre": {"fr": "Composition des recettes fiscales de l'État, 1986-2025",
              "ar": "تركيبة المداخيل الجبائية للدولة، 1986-2025"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
}


def _labc(key: str) -> str:
    return _C[key].get(figtools.lang(), _C[key]["fr"])


def table_composition():
    df = figtools.series(SERIE_COMPOSITION)
    cols = ["annee", "irpp_pct", "is_pct", "tva_pct", "consommation_pct",
            "douanes_pct", "autres_indirects_pct"]
    w = df[[c for c in cols if c in df.columns]].copy()
    return w.rename(columns={
        "annee": _labc("col_annee"), "irpp_pct": _labc("irpp"), "is_pct": _labc("is"),
        "tva_pct": _labc("tva"), "consommation_pct": _labc("consommation"),
        "douanes_pct": _labc("douanes"), "autres_indirects_pct": _labc("autres"),
    })


def fig_composition():
    """Aires empilées : ce que pèse chaque impôt dans le prélèvement, année par année.

    L'ordre d'empilement va des impôts directs aux indirects, et place les droits de
    douanes juste au-dessus : c'est là que se lit le basculement du prélèvement, de la
    frontière vers la consommation intérieure et le revenu.
    """
    figtools.apply_lang_font()
    ft = figtools.fig_text
    df = figtools.series(SERIE_COMPOSITION)
    postes = [("irpp_pct", "irpp", "#1f6feb"), ("is_pct", "is", "#54aeff"),
              ("douanes_pct", "douanes", "#d1242f"), ("tva_pct", "tva", "#2da44e"),
              ("consommation_pct", "consommation", "#bf8700"),
              ("autres_indirects_pct", "autres", "#8b949e")]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.stackplot(df["annee"], *[df[c] for c, _, _ in postes],
                 labels=[ft(_labc(k)) for _, k, _ in postes],
                 colors=[c for _, _, c in postes], alpha=0.92)
    ax.set_xlim(df["annee"].min(), df["annee"].max())
    ax.set_ylim(0, 100)
    ax.set_ylabel(ft(_labc("y")))
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_title(ft(_labc("titre")))
    ax.grid(True, axis="y", alpha=0.25)
    # Sous le cadre : à l'intérieur, la légende masque la bande de l'impôt sur le revenu,
    # qui est précisément celle que le lecteur vient chercher.
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=8.5,
              frameon=False)
    fig.tight_layout()
    return fig


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def table():
    """Onglet « Données » : le montant et les trois ratios, plus la part des salaires."""
    df = figtools.series(SERIE)
    cols = ["annee", "irpp_MDT", "irpp_sur_pib_pct", "irpp_sur_depenses_totales_pct",
            "irpp_sur_recettes_fiscales_pct", "part_salaires_dans_irpp_pct"]
    w = df[[c for c in cols if c in df.columns]].copy()
    return w.rename(columns={
        "annee": _lab("col_annee"),
        "irpp_MDT": _lab("col_mdt"),
        "irpp_sur_pib_pct": _lab("col_pib"),
        "irpp_sur_depenses_totales_pct": _lab("col_dep"),
        "irpp_sur_recettes_fiscales_pct": _lab("col_rec"),
        "part_salaires_dans_irpp_pct": _lab("col_sal"),
    })


def prepare(generated: str | None = None):
    df = figtools.series(SERIE)
    figtools.write_figdata(
        table(), FIGDATA / "fig_irpp_rendement.csv", SERIE,
        note="rendement de l'impôt sur le revenu, 1986-2025 ; rupture de série en 1990",
        generated=generated)
    return df


def fig_rendement():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    df = figtools.series(SERIE)
    avant = df[df["annee"] < ANNEE_IRPP]
    apres = df[df["annee"] >= ANNEE_IRPP]

    fig, ax1 = plt.subplots(figsize=(9.5, 5.2))
    ax2 = ax1.twinx()

    # La bande grise couvre les années où la rubrique mesure autre chose que l'IRPP.
    ax1.axvspan(df["annee"].min() - 0.5, ANNEE_IRPP - 0.5, color="#8b949e", alpha=0.13, lw=0)
    ax1.axvline(ANNEE_IRPP - 0.5, color="#57606a", lw=1.2, ls="--")

    l0, = ax1.plot(avant["annee"], avant["irpp_sur_pib_pct"], "o:", color="#57606a",
                   lw=1.6, ms=4, label=ft(_lab("lg_pib_avant")))
    l1, = ax1.plot(apres["annee"], apres["irpp_sur_pib_pct"], "o-", color="#1f6feb",
                   lw=2, ms=4, label=ft(_lab("lg_pib")))
    l2, = ax2.plot(apres["annee"], apres["irpp_sur_depenses_totales_pct"], "s--",
                   color="#d1242f", lw=1.8, ms=3, label=ft(_lab("lg_dep")))

    # L'annotation se place sous la légende, dans la zone vide que laisse la montée des
    # courbes : au-dessus, elle passerait derrière la légende — vérifié au rendu.
    bas, haut = ax1.get_ylim()
    y_texte = bas + 0.62 * (haut - bas)
    ax1.annotate(ft(_lab("rupture")), xy=(ANNEE_IRPP - 0.5, y_texte),
                 xytext=(ANNEE_IRPP + 1.5, y_texte),
                 fontsize=8, color="#57606a", va="center",
                 arrowprops=dict(arrowstyle="->", color="#57606a", lw=1))

    ax1.set_ylabel(ft(_lab("y_pib")), color="#1f6feb")
    ax2.set_ylabel(ft(_lab("y_dep")), color="#d1242f")
    ax1.set_xlabel(ft(_lab("xlabel")))
    ax1.set_title(ft(_lab("title")))
    ax1.grid(True, alpha=0.3)
    ax1.legend(handles=[l0, l1, l2], loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig
