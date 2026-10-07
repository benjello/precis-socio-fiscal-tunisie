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
        # Même correction de substantif : les impôts cédulaires sont des IMPÔTS, donc
        # ضرائب et non أداءات. L'adjectif النوعية est laissé tel quel, faute d'avoir pu
        # vérifier qu'il rend bien « cédulaire ».
        "ar": "الضرائب النوعية والمساهمة الشخصية للدولة / الناتج المحلي الإجمالي"},
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
    # « impôts » se dit أداءات, comme au Journal officiel arabe (« impôts indirects » :
    # الأداءات والمعاليم غير المباشرة, tableau A de la LF 2019) ; ضرائب rend « taxes ».
    # Décision de l'humain du 4/10/2026 (docs/agents/terminologue.md).
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


# --- Les déductions pour charges de famille dans le temps, revenus 1990-2026 -----------------
#
# UNE DÉCLARATION, PAS UNE FONCTION DE FIGURE. Le tracé est celui du composant commun
# (`figtools.figure_escalier`) : chaque montant de l'article 40 en escalier, la marche posée
# à l'année de revenus où il change. La série vient de
# `_seriescache/irpp-deductions-famille.csv`, émise par `scripts/generate_bareme_tables.py`
# — une ligne par déduction et par date d'effet.
#
# QUATRE DÉDUCTIONS SUR SEPT. Le parent à charge suit le chef de famille à 150 dinars de
# 1990 à 2018, et les deuxième et troisième enfants s'intercalent entre le premier et le
# quatrième : leurs traits se recouvriraient. Le tableau du chapitre porte les sept.
#
# DINARS COURANTS, PUIS DINARS CONSTANTS. Ces montants ne sont pas indexés : la seconde vue
# les rapporte à l'indice des prix à la consommation, en dinars de la dernière année de
# l'indice. L'axe est logarithmique dans les deux vues — de 45 à 2 000 dinars, une échelle
# linéaire écraserait les déductions par enfant.
SERIE_FAMILLE = "irpp-deductions-famille"
FIN_FAMILLE = 2026
# Année des dinars constants, FIXÉE : la légende et le texte du chapitre citent des montants
# « en dinars de 2023 », qu'un indice prolongé d'une année ne doit pas déplacer en silence.
BASE_FAMILLE = 2023

_FAMILLE = {"infirme": "#6639ba", "chef_de_famille": "#08519c", "enf1": "#bc4c00",
            "enf4": "#1a7f37"}

_L.update({
    "f_chef_de_famille": {"fr": "Chef de famille", "ar": "رئيس العائلة"},
    "f_enf1": {"fr": "1er enfant", "ar": "الطفل الأوّل"},
    "f_enf4": {"fr": "4e enfant", "ar": "الطفل الرابع"},
    "f_infirme": {"fr": "Enfant infirme", "ar": "الطفل المعوق"},
    "f_y": {"fr": "Déduction annuelle, en dinars courants (échelle logarithmique)",
            "ar": "الطرح السنوي، بالدينار الجاري (سلّم لوغاريتمي)"},
    "f_y_reel": {"fr": "Déduction annuelle, en dinars de {base} (échelle logarithmique)",
                 "ar": "الطرح السنوي، بدينار سنة {base} (سلّم لوغاريتمي)"},
    "f_x": {"fr": "Année de revenus", "ar": "سنة المداخيل"},
    "f_dinar": {"fr": "{} D", "ar": "{} د"},
})

figtools.register_provenance(
    SERIE_FAMILLE,
    titre=("Déductions pour situation et charges de famille de l'impôt sur le revenu, à "
           "chaque année de revenus où leur montant change, depuis 1990"),
    titre_ar=("الطرح بعنوان الحالة والأعباء العائلية من الضريبة على الدخل، عند كلّ سنة مداخيل "
              "يتغيّر فيها مبلغه، منذ 1990"),
    sources=["code-irpp-is-1990", "lf-2005", "lf-2010", "lf-2014", "lf-2018", "lf-2020"],
    unite="dinars par an, montant retranché du revenu net global",
    unite_ar="دينار في السنة، مبلغ يُطرح من الدخل الصافي الجملي",
    perimetre=("une ligne par déduction et par année de revenus d'effet : chef de famille, "
               "quatre premiers enfants à charge, enfant infirme, parent à charge"),
    perimetre_ar=("سطر لكلّ طرح ولكلّ سنة مداخيل يسري فيها: رئيس العائلة، الأطفال الأربعة "
                  "الأوائل في الكفالة، الطفل المعوق، الوالد المتكفَّل به"),
    caveats=("Les montants, non leurs conditions : la série ne dit ni l'âge limite des "
             "enfants à charge, ni la condition de ressources du parent. Les dates sont des "
             "années de revenus, au 1er janvier."),
    caveats_ar=("المبالغ لا شروطها: لا تبيّن السلسلة السنّ القصوى للأطفال في الكفالة ولا شرط "
                "موارد الوالد. التواريخ سنوات مداخيل، في غرّة جانفي."),
)


def _dinars(v: float) -> str:
    return _lab("f_dinar").format(f"{v:,.0f}".replace(",", chr(0x202F)))


def figure_famille(slug: str, caption: str, note_lecture: str | None = None,
                   generated: str | None = None) -> None:
    """Les déductions pour charges de famille, en dinars courants et en dinars constants."""
    figtools.figure_escalier(
        SERIE_FAMILLE, {cle: (_lab("f_" + cle), couleur) for cle, couleur in _FAMILLE.items()},
        slug=slug, caption=caption, note_lecture=note_lecture, generated=generated,
        fin=FIN_FAMILLE, constants=True, base=BASE_FAMILLE, format_valeur=_dinars, log=True,
        ylabel=_lab("f_y"), ylabel_constants=_lab("f_y_reel"), xlabel=_lab("f_x"),
        ylim=(30, 4000), yticks=(50, 100, 200, 500, 1000, 2000))
