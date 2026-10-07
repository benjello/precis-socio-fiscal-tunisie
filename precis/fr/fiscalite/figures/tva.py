"""Figure « ce que rapporte la TVA » du livre *Fiscalité*.

LA RUPTURE DE SÉRIE EST LE SUJET, PAS UN DÉTAIL — comme pour l'impôt sur le revenu, mais
deux ans plus tôt. La rubrique « 2.2 TVA » du ministère des Finances est continue depuis
1986, et c'est le ministère lui-même qui l'intitule ainsi ; or la taxe sur la valeur
ajoutée est créée par la loi n° 88-61 du 2 juin 1988 et n'entre en vigueur qu'au
1er juillet 1988. Les exercices 1986 et 1987 portent donc les taxes sur le chiffre
d'affaires que le code de 1988 remplace, non la TVA.

La figure le montre au lieu de le taire : ces deux années sont tracées en pointillé gris,
séparées du reste par une bande verticale, et la légende nomme ce qu'elles mesurent
réellement.

DEUX RAPPORTS, DEUX AXES. L'axe gauche rapporte la taxe au produit intérieur brut, l'axe
droit aux dépenses totales de l'État. Le second ne commence qu'en 1990 : le ministère ne
publie pas les dépenses totales avant cette date. Les exercices 1988 et 1989 n'ont donc
qu'un seul des deux ratios, et la courbe de droite ne pénètre jamais la zone grisée.

DEUX DÉNOMINATEURS DE PIB, ET C'EST VOULU. Le PIB n'est publié par aucune des deux
sources : il se déduit du fichier d'indicateurs du ministère (déficit en dinars ÷ déficit
en points de PIB). Celui des comptes nationaux de l'INS, base 2015, ne coïncide pas pour
2012-2014. La figure retient le PIB du ministère — c'est celui sur lequel il calcule
lui-même ses ratios —, et le tableau conserve les deux colonnes côte à côte : le
dénominateur d'un ratio se choisit, il ne se devine pas.
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

SERIE_COMPOSITION = "recettes-fiscales-composition"
SERIE_RATIOS = "irpp-ratios"

# Première année d'application de la TVA : le code promulgué par la loi n° 88-61 du
# 2 juin 1988 s'applique à compter du 1er juillet 1988. L'exercice 1988 n'est donc taxé
# qu'au second semestre, et l'assujettissement s'étend ensuite par paliers — commerce de
# gros en 1989, commerce de détail en 1996 seulement.
ANNEE_TVA = 1988

# Les dépenses totales de l'État ne sont publiées qu'à partir de 1990 : la courbe de
# droite commence donc deux ans après la création de la taxe.
ANNEE_DEPENSES = 1990

_L = {
    "lg_avant": {
        "fr": "Taxes antérieures sur le chiffre d'affaires / PIB",
        "ar": "الأداءات السابقة على رقم المعاملات / الناتج المحلي الإجمالي"},
    "lg_pib": {
        "fr": "TVA / PIB (éch. gauche)",
        "ar": "الأداء على القيمة المضافة / الناتج المحلي الإجمالي (يسار)"},
    "lg_dep": {
        "fr": "TVA / dépenses de l'État (éch. droite)",
        "ar": "الأداء على القيمة المضافة / نفقات الدولة (يمين)"},
    "y_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_dep": {"fr": "En % des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "title": {"fr": "Ce que rapporte la taxe sur la valeur ajoutée, 1986-2025",
              "ar": "مردود الأداء على القيمة المضافة، 1986-2025"},
    "rupture": {"fr": "création de la TVA\n(loi n° 88-61, 1er juillet 1988)",
                "ar": "إحداث الأداء على القيمة المضافة\n(القانون عدد 88-61، 1 جويلية 1988)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_pib": {"fr": "% du PIB (ministère des Finances)",
                "ar": "% من الناتج المحلي الإجمالي (وزارة المالية)"},
    "col_pib_cnat": {"fr": "% du PIB (comptes nationaux)",
                     "ar": "% من الناتج المحلي الإجمالي (الحسابات القومية)"},
    "col_dep": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "col_rec": {"fr": "% des recettes fiscales", "ar": "% من المداخيل الجبائية"},
    "col_mdt": {"fr": "TVA (MDT)", "ar": "الأداء على القيمة المضافة (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    """Les deux séries jointes sur l'année, avec les ratios au PIB et aux dépenses.

    La composition des recettes porte le montant de TVA ; les ratios de l'impôt sur le
    revenu portent les deux PIB et les dépenses totales. Aucune des deux ne porte tout.
    """
    comp = figtools.series(SERIE_COMPOSITION)
    rat = figtools.series(SERIE_RATIOS)
    d = comp[["annee", "tva_MDT", "tva_pct"]].merge(
        rat[["annee", "pib_minfin_MDT", "pib_cnat_MDT", "depenses_totales_MDT"]],
        on="annee", how="left")
    d["tva_sur_pib_pct"] = 100 * d["tva_MDT"] / d["pib_minfin_MDT"]
    d["tva_sur_pib_cnat_pct"] = 100 * d["tva_MDT"] / d["pib_cnat_MDT"]
    d["tva_sur_depenses_pct"] = 100 * d["tva_MDT"] / d["depenses_totales_MDT"]
    return d


def table():
    d = _donnees()
    cols = ["annee", "tva_sur_pib_pct", "tva_sur_depenses_pct",
            "tva_sur_pib_cnat_pct", "tva_pct", "tva_MDT"]
    w = d[cols].copy()
    for c in ("tva_sur_pib_pct", "tva_sur_depenses_pct",
              "tva_sur_pib_cnat_pct", "tva_pct"):
        w[c] = w[c].round(2)
    return w.rename(columns={
        "annee": _lab("col_annee"),
        "tva_sur_pib_pct": _lab("col_pib"),
        "tva_sur_depenses_pct": _lab("col_dep"),
        "tva_sur_pib_cnat_pct": _lab("col_pib_cnat"),
        "tva_pct": _lab("col_rec"),
        "tva_MDT": _lab("col_mdt"),
    })


def prepare(generated: str | None = None):
    d = _donnees()
    figtools.write_figdata(
        table(), FIGDATA / "fig_tva_rendement.csv", SERIE_COMPOSITION, SERIE_RATIOS,
        note=("rendement de la TVA en points de PIB et en part des dépenses de l'État, "
              "1986-2025 ; rupture de série en 1988, les exercices antérieurs portant les "
              "taxes sur le chiffre d'affaires remplacées par le code de 1988 ; les "
              "dépenses totales ne sont publiées qu'à partir de 1990"),
        generated=generated)
    return d


def fig_rendement():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    avant = d[d["annee"] < ANNEE_TVA]
    apres = d[d["annee"] >= ANNEE_TVA]
    depenses = d[d["annee"] >= ANNEE_DEPENSES]

    fig, ax1 = plt.subplots(figsize=(9.5, 5.2))
    ax2 = ax1.twinx()

    # La bande grise couvre les années où la rubrique mesure autre chose que la TVA.
    ax1.axvspan(d["annee"].min() - 0.5, ANNEE_TVA - 0.5, color="#8b949e", alpha=0.13, lw=0)
    ax1.axvline(ANNEE_TVA - 0.5, color="#57606a", lw=1.2, ls="--")

    l0, = ax1.plot(avant["annee"], avant["tva_sur_pib_pct"], "o:", color="#57606a",
                   lw=1.6, ms=4, label=ft(_lab("lg_avant")))
    # Le vert est celui de la bande « TVA » de la figure de composition du chapitre : une
    # même couleur pour un même impôt, d'une figure à l'autre. Le rouge de l'axe droit
    # reprend la convention de la figure de l'impôt sur le revenu, où il porte déjà le
    # rapport aux dépenses de l'État.
    l1, = ax1.plot(apres["annee"], apres["tva_sur_pib_pct"], "o-", color="#2da44e",
                   lw=2, ms=4, label=ft(_lab("lg_pib")))
    l2, = ax2.plot(depenses["annee"], depenses["tva_sur_depenses_pct"], "s--",
                   color="#d1242f", lw=1.8, ms=3, label=ft(_lab("lg_dep")))

    # L'annotation se place dans la moitié basse du cadre de gauche : les deux courbes
    # occupent le haut sur toute la fin de période.
    bas, haut = ax1.get_ylim()
    y_texte = bas + 0.15 * (haut - bas)
    ax1.annotate(ft(_lab("rupture")), xy=(ANNEE_TVA - 0.5, y_texte),
                 xytext=(ANNEE_TVA + 2.0, y_texte),
                 fontsize=8, color="#57606a", va="center",
                 arrowprops=dict(arrowstyle="->", color="#57606a", lw=1))

    ax1.set_ylabel(ft(_lab("y_pib")), color="#2da44e")
    ax2.set_ylabel(ft(_lab("y_dep")), color="#d1242f")
    ax1.set_xlabel(ft(_lab("xlabel")))
    ax1.set_title(ft(_lab("title")))
    ax1.grid(True, alpha=0.3)
    ax1.legend(handles=[l0, l1, l2], loc="lower right", fontsize=8.5)
    fig.tight_layout()
    return fig


# --- Crédit de TVA, restitutions et retenue à la source selon les sources, 2009-2014 ---------
#
# TOUTES LES SOURCES CÔTE À CÔTE, AUCUN RACCORD. Quatre documents portent sur les mêmes
# grandeurs et ne s'accordent pas : deux séries de TVA restituée, trois valeurs de la retenue à
# la source pour 2012. La figure ne choisit pas : une ligne ne relie jamais deux documents, et
# une série ne déborde pas les années que son document imprime.
#
# UNE SOURCE, UNE COULEUR, d'une vue à l'autre ; la grandeur se lit à la forme du marqueur et
# au style du trait. Le tableau « Source DGCPR » reproduit par le FMI est une donnée de
# l'administration relayée par un rapport extérieur : marqueur creux, trait tireté, barre
# hachurée, et la légende le dit.
SERIE_CREDIT = "tva-credit-restitutions-sources"

BLEU, ORANGE, VERT, VIOLET = "#08519c", "#bc4c00", "#1a7f37", "#6639ba"

S_GT = "minfin-cnf-2013-impots-indirects"
S_SYNTHESE = "minfin-cnf-2013-synthese"
S_CONTROLE = "minfin-controle-fiscal-2016"
S_FMI = "fmi-2013-modernisation-administration-fiscale"

# source → (couleur, relais d'un rapport extérieur ?, clé de libellé, localisateur imprimé)
_SOURCES = {
    S_GT: (BLEU, False, "s_gt", "loc_diapo"),
    S_SYNTHESE: (VERT, False, "s_synthese", "loc_page"),
    S_CONTROLE: (ORANGE, False, "s_controle", "loc_page"),
    S_FMI: (VIOLET, True, "s_fmi", "loc_fmi"),
}

# La réserve du catalogue est récrite pour le lecteur du volume ; le reste de la provenance
# (sources, fiche, fichiers bruts) est celui du catalogue, inchangé.
figtools.register_provenance(SERIE_CREDIT, **{
    **figtools.meta(SERIE_CREDIT),
    "titre_ar": ("فائض الأداء على القيمة المضافة وإرجاعه والخصم من المورد بعنوان الأداء على "
                 "القيمة المضافة حسب المصادر، 2009-2014"),
    "unite_ar": "ملايين الدنانير الجارية",
    "perimetre_ar": ("فائض الأداء المسجّل (2010-2012)، المبالغ المطلوب إرجاعها والمبالغ المرجَعة "
                     "(2010-2012)، إرجاع الأداءات من قبل الإدارة العامة للأداءات، المجموع وحصّة "
                     "الأداء على القيمة المضافة (2010-2014)، مردود الخصم من المورد (2009-2012)؛ "
                     "سطر لكلّ سنة ومقدار ووثيقة"),
    "caveats": ("Les sources sont gardées côte à côte, sans raccord ni arbitrage. Les deux "
                "séries de TVA restituée ne coïncident pas (320,8 et 349,9 MD en 2010 ; 301,2 "
                "et 268,3 en 2011 ; 179,2 et 287,7 en 2012), et la retenue à la source de 2012 "
                "a trois valeurs (305,5 ; 298,9 ; 272,7 MD, cette dernière arrêtée avant la "
                "clôture de l'exercice). Aucun document ne décrit sa méthode : ni la date à "
                "laquelle le crédit est arrêté, ni s'il s'agit du crédit reporté ou du seul "
                "crédit demandé en restitution. Le tableau « Source DGCPR » est un tableau de "
                "l'administration reproduit par le FMI : une donnée administrative, non une "
                "estimation du FMI."),
    "caveats_ar": ("أُبقيت المصادر جنبًا إلى جنب دون وصل ولا ترجيح. سلسلتا الأداء على القيمة "
                   "المضافة المرجَع لا تتطابقان، وللخصم من المورد لسنة 2012 ثلاث قيم (305,5 ؛ "
                   "298,9 ؛ 272,7 م.د، والأخيرة مضبوطة قبل ختم السنة المالية). لا تصف أيّ وثيقة "
                   "منهجيتها. الجدول المنسوب إلى الإدارة العامة للمحاسبة العمومية والاستخلاص "
                   "جدول إداري نقله صندوق النقد الدولي، وليس تقديرًا للصندوق."),
})

_L.update({
    # Sources (légendes, colonne « Source » des données).
    "s_gt": {"fr": "groupe de travail « impôts indirects », août 2013",
             "ar": "فريق العمل «الأداءات غير المباشرة»، أوت 2013"},
    "s_synthese": {"fr": "rapport de synthèse des groupes de travail, novembre 2013",
                   "ar": "التقرير التأليفي لفرق العمل، نوفمبر 2013"},
    "s_controle": {"fr": "rapport d'activité sur le contrôle fiscal",
                   "ar": "تقرير النشاط حول المراقبة الجبائية"},
    "s_fmi": {"fr": "tableau de l'administration (« Source DGCPR ») relayé par le FMI, "
                    "février 2013",
              "ar": "جدول للإدارة (الإدارة العامة للمحاسبة العمومية والاستخلاص) نقله صندوق "
                    "النقد الدولي، فيفري 2013"},
    "loc_diapo": {"fr": "diapositive {}", "ar": "الشريحة {}"},
    "loc_page": {"fr": "p. {}", "ar": "ص. {}"},
    "loc_fmi": {"fr": "tableau 10, p. {}", "ar": "الجدول 10، ص. {}"},
    "fam_budgetaire": {"fr": "budgétaire", "ar": "ميزانية"},
    "fam_relais": {"fr": "extérieur (relais d'une donnée de l'administration)",
                   "ar": "خارجي (ناقل لمعطى إداري)"},
    # Grandeurs.
    "g_credit_enregistre": {"fr": "Crédit de TVA enregistré",
                            "ar": "فائض الأداء على القيمة المضافة المسجّل"},
    "g_restitution_demandee": {"fr": "Crédit demandé en restitution",
                               "ar": "الفائض المطلوب إرجاعه"},
    "g_restitution_tva": {"fr": "TVA restituée", "ar": "الأداء على القيمة المضافة المرجَع"},
    "g_restitution_tous_impots": {"fr": "Restitutions, tous impôts",
                                  "ar": "إرجاع الأداءات، المجموع"},
    "g_retenue_source": {"fr": "Retenue à la source de TVA",
                         "ar": "الخصم من المورد بعنوان الأداء على القيمة المضافة"},
    # Vues, axes.
    "vue_restitutions": {"fr": "Restitutions", "ar": "الإرجاع"},
    "vue_credit": {"fr": "Crédit et restitution", "ar": "الفائض وإرجاعه"},
    "vue_retenue": {"fr": "Retenue à la source", "ar": "الخصم من المورد"},
    "vue_pct": {"fr": "En % des recettes de TVA",
                "ar": "% من مداخيل الأداء على القيمة المضافة"},
    "y_md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "y_pct_tva": {"fr": "En % des recettes de TVA de l'année",
                  "ar": "% من مداخيل الأداء على القيمة المضافة للسنة"},
    "p_credit": {"fr": "Crédit enregistré", "ar": "الفائض المسجّل"},
    "p_restitution": {"fr": "TVA restituée", "ar": "الأداء المرجَع"},
    "p_retenue": {"fr": "Retenue à la source", "ar": "الخصم من المورد"},
    "part_demandee": {"fr": "demandé : {} % du crédit", "ar": "المطلوب: {} % من الفائض"},
    "md": {"fr": "MD", "ar": "م.د"},
    # Colonnes des données.
    "c_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "c_source": {"fr": "Source", "ar": "المصدر"},
    "c_famille": {"fr": "Famille", "ar": "الصنف"},
    "c_loc": {"fr": "Localisation", "ar": "الموضع"},
    "c_valeur": {"fr": "Valeur (MD)", "ar": "القيمة (م.د)"},
    "c_recettes": {"fr": "Recettes de TVA de l'année (MD)",
                   "ar": "مداخيل الأداء على القيمة المضافة للسنة (م.د)"},
    "c_pct": {"fr": "En % des recettes de TVA",
              "ar": "% من مداخيل الأداء على القيمة المضافة"},
})

# Ordre des grandeurs dans les données : le stock, ce qui est demandé, ce qui est rendu.
_GRANDEURS = ["credit_enregistre", "restitution_demandee", "restitution_tva",
              "restitution_tous_impots", "retenue_source"]


_FINE = chr(0x202F)  # espace fine insécable, séparateur des milliers


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", _FINE).replace(".", ",")


def _credit():
    """La série longue, chaque ligne rapportée aux recettes de TVA de son année."""
    d = figtools.series(SERIE_CREDIT).copy()
    rec = figtools.series(SERIE_COMPOSITION)[["annee", "tva_MDT"]]
    d = d.merge(rec, on="annee", how="left")
    d["pct_recettes_tva"] = 100 * d["valeur_MD"] / d["tva_MDT"]
    # Le total des restitutions, tous impôts confondus, ne se rapporte pas à la seule TVA.
    d.loc[d["grandeur_id"] == "restitution_tous_impots", "pct_recettes_tva"] = float("nan")
    return d


def _points(d, grandeur: str, source: str, colonne: str = "valeur_MD"):
    s = d[(d["grandeur_id"] == grandeur) & (d["source_id"] == source)].sort_values("annee")
    return [(int(a), float(v)) for a, v in zip(s["annee"], s[colonne])]


def _lg(grandeur: str | None, source: str) -> str:
    """Libellé de légende : « grandeur — source », ou la source seule."""
    s = _lab(_SOURCES[source][2])
    return s if grandeur is None else f"{_lab('g_' + grandeur)} — {s}"


def _bulle(artiste, annee, grandeur, source, v, pct: bool):
    unite = " %" if pct else f" {_lab('md')}"
    figtools.infobulle(artiste, f"{annee} · {_lab('g_' + grandeur)} : {_nombre(v)}{unite} · "
                                f"{_lab(_SOURCES[source][2])}")


def _courbe(ax, d, grandeur, source, marque, style, *, pct=False, dy=7, places=None, ms=5.5):
    """Trace une série d'UN document : trait entre ses seules années, un point par valeur.

    Chaque point est tracé à part, pour porter son infobulle. `dy` place l'étiquette de
    valeur au-dessus (positif) ou au-dessous (négatif) du point, en points ; `places` déroge
    année par année — `{année: (dx, dy)}`, un `dx` non nul posant l'étiquette à côté du point —
    là où deux documents donnent des valeurs voisines.
    """
    places = places or {}
    ft = figtools.fig_text
    couleur, relais = _SOURCES[source][:2]
    pts = _points(d, grandeur, source, "pct_recettes_tva" if pct else "valeur_MD")
    if relais:
        style = (0, (5, 2))
    ax.plot([a for a, _ in pts], [v for _, v in pts], color=couleur, lw=1.7, ls=style,
            zorder=2)
    for a, v in pts:
        p, = ax.plot([a], [v], marque, color=couleur, ms=ms + (2.5 if relais else 0),
                     mfc="white" if relais else couleur, mew=1.5, zorder=3 - relais)
        _bulle(p, a, grandeur, source, v, pct)
        ex, ey = places.get(a, (0, dy))
        ax.annotate(_nombre(v), xy=(a, v), xytext=(ex, ey), textcoords="offset points",
                    ha="center" if ex == 0 else ("left" if ex > 0 else "right"),
                    va="center" if ex != 0 else ("bottom" if ey > 0 else "top"),
                    fontsize=7.5, color=couleur, zorder=4)
    from matplotlib.lines import Line2D
    return Line2D([], [], color=couleur, marker=marque, ms=ms + (1.5 if relais else 0),
                  mfc="white" if relais else couleur, mew=1.5, lw=1.7, ls=style,
                  label=ft(_lg(grandeur, source)))


def _legende(fig_ou_ax, poignees, ncol=2, y=-0.13):
    fig_ou_ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y),
                     fontsize=8, frameon=False, ncol=ncol)


def _fig_restitutions():
    """Ce qui est demandé et ce qui est rendu, document par document."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _credit()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    # En 2010, quatre valeurs en moins de 110 MD : les étiquettes vont à gauche des points.
    gauche = (-9, 0)
    poignees = [
        _courbe(ax, d, "restitution_tous_impots", S_CONTROLE, "s", (0, (1, 1.5)),
                places={2010: gauche}),
        _courbe(ax, d, "restitution_demandee", S_GT, "^", (0, (1, 1.5)),
                places={2010: gauche, 2011: (9, 3), 2012: (9, 0)}),
        _courbe(ax, d, "restitution_tva", S_CONTROLE, "o", "-",
                places={2010: gauche, 2011: (0, -8)}),
        _courbe(ax, d, "restitution_tva", S_GT, "o", "-", dy=-8,
                places={2010: gauche, 2011: (0, 7)}),
    ]
    ax.set_ylim(0, 740)
    ax.set_xticks(range(2010, 2015))
    ax.set_xlim(2009.45, 2014.4)
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("y_md")))
    ax.grid(True, alpha=0.3)
    _legende(ax, poignees)
    fig.tight_layout()
    return fig


def _fig_credit():
    """Le stock, ce qui en est demandé, ce qui en est rendu : un seul document, trois années."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    from matplotlib.patches import Patch
    d = _credit()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    # Une seule source : sa couleur, en trois intensités.
    barres = [("credit_enregistre", 1.0, None), ("restitution_demandee", 0.6, None),
              ("restitution_tva", 0.3, None)]
    largeur = 0.26
    for i, (grandeur, alpha, _) in enumerate(barres):
        for a, v in _points(d, grandeur, S_GT):
            b = ax.bar(a + (i - 1) * largeur, v, width=largeur * 0.92, color=BLEU, alpha=alpha,
                       edgecolor=BLEU, lw=0.8)
            _bulle(b.patches[0], a, grandeur, S_GT, v, False)
            ax.annotate(_nombre(v, 0 if grandeur == "credit_enregistre" else 1),
                        xy=(a + (i - 1) * largeur, v), xytext=(0, 3),
                        textcoords="offset points", ha="center", va="bottom", fontsize=8,
                        color=BLEU)
    # Ce que les demandes pèsent dans le stock, sous chaque groupe de barres.
    credit = dict(_points(d, "credit_enregistre", S_GT))
    for a, v in _points(d, "restitution_demandee", S_GT):
        ax.annotate(ft(_lab("part_demandee").format(_nombre(100 * v / credit[a], 0))),
                    xy=(a + 0.13, v), xytext=(0, 20), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5, color="#57606a")
    ax.set_xticks(sorted(credit))
    ax.set_xlim(2009.5, 2012.5)
    ax.set_ylim(0, 1900)
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("y_md")))
    ax.grid(True, axis="y", alpha=0.3)
    _legende(ax, [Patch(facecolor=BLEU, alpha=alpha, edgecolor=BLEU,
                        label=ft(_lg(g, S_GT))) for g, alpha, _ in barres], ncol=1)
    fig.tight_layout()
    return fig


def _barres_par_source(ax, d, grandeur, sources, *, pct=False, largeur=0.27, taille=7.5):
    """Barres groupées par année, une par document, la valeur au-dessus de chacune."""
    ft = figtools.fig_text
    from matplotlib.patches import Patch
    colonne = "pct_recettes_tva" if pct else "valeur_MD"
    poignees = []
    for i, source in enumerate(sources):
        couleur, relais = _SOURCES[source][:2]
        style = dict(facecolor="white", edgecolor=couleur, hatch="////", lw=1.2) if relais \
            else dict(facecolor=couleur, edgecolor=couleur, lw=1.2)
        x0 = (i - (len(sources) - 1) / 2) * largeur
        for a, v in _points(d, grandeur, source, colonne):
            b = ax.bar(a + x0, v, width=largeur * 0.9, **style)
            _bulle(b.patches[0], a, grandeur, source, v, pct)
            ax.annotate(_nombre(v), xy=(a + x0, v), xytext=(0, 3), textcoords="offset points",
                        ha="center", va="bottom", fontsize=taille, color=couleur)
        poignees.append(Patch(label=ft(_lg(None, source)), **style))
    return poignees


def _fig_retenue():
    """La retenue à la source selon ses trois documents : les trois valeurs de 2012 côte à côte."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _credit()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    poignees = _barres_par_source(ax, d, "retenue_source", [S_FMI, S_GT, S_SYNTHESE])
    ax.set_xticks(range(2009, 2013))
    ax.set_xlim(2008.5, 2012.5)
    ax.set_ylim(0, 440)
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("y_md")))
    ax.grid(True, axis="y", alpha=0.3)
    _legende(ax, poignees, ncol=1)
    fig.tight_layout()
    return fig


def _fig_pct():
    """Les mêmes grandeurs rapportées aux recettes de TVA de l'année, en trois panneaux.

    Le crédit — un stock, près de 40 % des recettes — a son échelle ; la restitution et la
    retenue — des flux, de 4 à 11 % — partagent la leur.
    """
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _credit()
    fig = plt.figure(figsize=(11, 5.6))
    gs = fig.add_gridspec(1, 3, width_ratios=[0.7, 1.15, 1.45])
    ax_c = fig.add_subplot(gs[0])
    ax_r = fig.add_subplot(gs[1])
    ax_s = fig.add_subplot(gs[2], sharey=ax_r)

    _barres_par_source(ax_c, d, "credit_enregistre", [S_GT], pct=True, largeur=0.6)
    ax_c.set_xticks(range(2010, 2013))
    ax_c.set_xlim(2009.4, 2012.6)
    ax_c.set_ylim(0, 45)
    ax_c.set_ylabel(ft(_lab("y_pct_tva")))
    ax_c.set_title(ft(_lab("p_credit")), fontsize=9.5)

    _courbe(ax_r, d, "restitution_tva", S_CONTROLE, "o", "-", pct=True, places={2011: (0, -8)})
    _courbe(ax_r, d, "restitution_tva", S_GT, "o", "-", pct=True, dy=-8, places={2011: (0, 7)})
    ax_r.set_xticks(range(2010, 2015))
    ax_r.set_xlim(2009.6, 2014.4)
    ax_r.set_ylim(0, 12.5)
    ax_r.set_title(ft(_lab("p_restitution")), fontsize=9.5)

    p_s = _barres_par_source(ax_s, d, "retenue_source", [S_FMI, S_GT, S_SYNTHESE], pct=True,
                             taille=7)
    ax_s.set_xticks(range(2009, 2013))
    ax_s.set_xlim(2008.5, 2012.5)
    ax_s.set_title(ft(_lab("p_retenue")), fontsize=9.5)

    for ax in (ax_c, ax_r, ax_s):
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_xlabel(ft(_lab("xlabel")))
    # Une couleur par document : la légende n'a qu'à nommer les quatre documents.
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    poignees = [Patch(facecolor=BLEU, edgecolor=BLEU, label=ft(_lg(None, S_GT))),
                Line2D([], [], color=ORANGE, marker="o", lw=1.7,
                       label=ft(_lg(None, S_CONTROLE))),
                p_s[2], p_s[0]]
    fig.tight_layout()
    fig.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, 0.02), fontsize=8,
               frameon=False, ncol=2)
    return fig


def vues_credit_restitutions():
    return [(_lab("vue_restitutions"), _fig_restitutions()),
            (_lab("vue_credit"), _fig_credit()),
            (_lab("vue_retenue"), _fig_retenue()),
            (_lab("vue_pct"), _fig_pct())]


def table_credit_restitutions():
    """Une ligne par année, grandeur et document — la série telle qu'elle est, plus le ratio."""
    import pandas as pd
    d = _credit()
    ordre_g = {g: i for i, g in enumerate(_GRANDEURS)}
    ordre_s = {s: i for i, s in enumerate(_SOURCES)}
    d = d.assign(_g=d["grandeur_id"].map(ordre_g), _s=d["source_id"].map(ordre_s))
    d = d.sort_values(["_g", "_s", "annee"])
    return pd.DataFrame({
        _lab("c_grandeur"): [_lab("g_" + g) for g in d["grandeur_id"]],
        _lab("c_source"): [_lab(_SOURCES[s][2]) for s in d["source_id"]],
        _lab("col_annee"): [int(a) for a in d["annee"]],
        _lab("c_valeur"): [float(v) for v in d["valeur_MD"]],
        _lab("c_recettes"): [float(v) for v in d["tva_MDT"]],
        _lab("c_pct"): [None if v != v else round(float(v), 1)
                          for v in d["pct_recettes_tva"]],
        _lab("c_loc"): [_lab(_SOURCES[s][3]).format(int(p))
                        for s, p in zip(d["source_id"], d["page"])],
        _lab("c_famille"): [_lab("fam_relais" if _SOURCES[s][1] else "fam_budgetaire")
                            for s in d["source_id"]],
    })


# --- Les taux de la TVA dans le temps, 1988-2026 ---------------------------------------------
#
# DES MARCHES, PAS DES PENTES. Un taux légal vaut du jour de son effet à la veille du suivant :
# chaque taux est tracé en escalier, la marche posée à la date d'effet. La série vient de
# `_seriescache/tva-taux.csv`, émise par `scripts/generate_bareme_tables.py` — une ligne par
# taux et par date d'effet, avec le texte qui la fixe. Deux lignes n'y sont pas des marches :
#   - une ligne SANS valeur dit la suppression du taux à cette date (taux majoré, 1er janvier
#     2007) : le trait s'arrête, sur un marqueur creux ;
#   - une ligne qui RÉPÈTE la valeur précédente dit un texte qui reprend le taux sans le
#     changer (le taux de 10 %, entré dans le code au 1er janvier 2002) : un losange creux
#     sur le trait, sans marche.
# L'exonération n'est pas un taux : la série ne la porte pas, la figure non plus.
SERIE_TAUX = "tva-taux"

# Dernière année tracée : celle de la rédaction, comme le tableau des générations de taux.
FIN_TAUX = 2026

_TAUX = {"normal": BLEU, "intermediaire": ORANGE, "reduit": VERT, "majore": VIOLET}

_L.update({
    "t_normal": {"fr": "Taux normal", "ar": "النسبة العادية"},
    "t_intermediaire": {"fr": "Taux intermédiaire", "ar": "النسبة الوسيطة"},
    "t_reduit": {"fr": "Taux réduit", "ar": "النسبة المخفضة"},
    "t_majore": {"fr": "Taux majoré", "ar": "النسبة المرتفعة"},
    "y_taux": {"fr": "Taux de la taxe, en %", "ar": "نسبة الأداء، %"},
    "x_effet": {"fr": "Date d'effet", "ar": "تاريخ النفاذ"},
    "x_1988": {"fr": "1er juil.\n1988", "ar": "1 جويلية\n1988"},
    "fin_majore": {"fr": "supprimé au 1er janvier 2007\n(dernier jour : 31 décembre 2006)",
                   "ar": "أُلغيت في 1 جانفي 2007\n(آخر يوم: 31 ديسمبر 2006)"},
    "hors_code": {"fr": "1995 : créé hors du code", "ar": "1995: أُحدثت خارج المجلة"},
    "dans_code": {"fr": "2002 : entre dans le code\n(tableau B bis), sans changer",
                  "ar": "2002: أُدرجت في المجلة\n(الجدول « ب مكرر ») دون تغيير"},
    "c_taux": {"fr": "Taux", "ar": "النسبة"},
    "c_effet": {"fr": "Date d'effet", "ar": "تاريخ النفاذ"},
    "c_valeur_pct": {"fr": "Valeur (%)", "ar": "القيمة (%)"},
    "c_etat": {"fr": "Ce que fait le texte", "ar": "أثر النصّ"},
    "c_texte": {"fr": "Texte", "ar": "النصّ"},
    "c_jort": {"fr": "Journal officiel", "ar": "الرائد الرسمي"},
    "e_creation": {"fr": "fixe le taux", "ar": "يضبط النسبة"},
    "e_changement": {"fr": "change le taux", "ar": "يغيّر النسبة"},
    "e_reprise": {"fr": "reprend le taux sans le changer", "ar": "يُبقي النسبة دون تغيير"},
    "e_suppression": {"fr": "supprime le taux", "ar": "يلغي النسبة"},
    "ib_suppression": {"fr": "supprimé", "ar": "أُلغيت"},
})

figtools.register_provenance(
    SERIE_TAUX,
    titre=("Taux de la taxe sur la valeur ajoutée à chaque date d'effet, depuis le "
           "1er juillet 1988 : taux normal, taux intermédiaire, taux réduit, taux majoré"),
    titre_ar=("نسب الأداء على القيمة المضافة عند كلّ تاريخ نفاذ، منذ 1 جويلية 1988: النسبة "
              "العادية والنسبة الوسيطة والنسبة المخفضة والنسبة المرتفعة"),
    sources=["loi-88-61-tva", "decret-88-1109-calendrier-tva", "lf-1995", "lf-1998",
             "loi2001-123-lf2002", "loi-2006-80-reduction-taux", "lf-2018"],
    unite="taux de la taxe, en pourcentage de la base imposable",
    unite_ar="نسبة الأداء من القاعدة الخاضعة",
    perimetre=("une ligne par taux et par date d'effet, avec le texte du Journal officiel qui "
               "la fixe ; l'exonération, qui n'est pas un taux, n'y figure pas"),
    perimetre_ar=("سطر لكلّ نسبة ولكلّ تاريخ نفاذ، مع نصّ الرائد الرسمي الذي يضبطها؛ ولا يرد "
                  "فيها الإعفاء، وهو ليس نسبة"),
    caveats=("Les taux, non leur périmètre : la série ne dit pas quelles opérations relèvent "
             "de chaque taux, ni les réductions annuelles accordées par décret. Le taux de "
             "10 % est posé hors du code de 1995 à 2001 ; la ligne du 1er janvier 2002 marque "
             "son entrée dans le code, à valeur inchangée."),
    caveats_ar=("النسب لا مجال تطبيقها: لا تبيّن السلسلة العمليات الخاضعة لكلّ نسبة ولا "
                "التخفيضات السنوية الممنوحة بأمر. نسبة 10 % وُضعت خارج المجلة من 1995 إلى "
                "2001؛ وسطر 1 جانفي 2002 يوافق إدراجها في المجلة دون تغيير قيمتها."),
)


def _abscisse(date_iso: str) -> float:
    """Date d'effet -> année décimale : le 1er juillet 1988 tombe au milieu de 1988."""
    import datetime
    d = datetime.date.fromisoformat(date_iso)
    return d.year + (d.timetuple().tm_yday - 1) / (366 if d.year % 4 == 0 else 365)


def _taux():
    """La série, par taux : [(date ISO, taux en % ou None, état, texte, lien)], dates croissantes.

    L'état se déduit de la valeur précédente : `creation`, `changement`, `reprise` (même
    valeur, autre texte) ou `suppression` (plus de valeur).
    """
    d = figtools.series(SERIE_TAUX)
    sortie = {}
    for nom in _TAUX:
        s = d[d["taux"] == nom].sort_values("date_effet")
        lignes, precedente = [], None
        for date, v, texte, lien in zip(s["date_effet"], s["valeur"], s["texte"], s["lien"]):
            v = None if v != v else round(100 * float(v), 4)
            if v is None:
                etat = "suppression"
            elif precedente is None:
                etat = "creation"
            else:
                etat = "reprise" if v == precedente else "changement"
            lignes.append((str(date)[:10], v, etat, texte, lien))
            precedente = v
        if lignes:
            sortie[nom] = lignes
    return sortie


def _pct(v: float) -> str:
    return f"{v:g}".replace(".", ",") + " %"


def fig_taux():
    """Les quatre taux en escalier, chaque marche étiquetée de sa valeur."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    from matplotlib.lines import Line2D
    from matplotlib.ticker import FuncFormatter
    series = _taux()
    fin = FIN_TAUX + 1.0  # le 31 décembre de la dernière année tracée
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    poignees, dates = [], set()
    for nom, couleur in _TAUX.items():
        lignes = series.get(nom, [])
        for i, (date, v, etat, texte, _lien) in enumerate(lignes):
            x = _abscisse(date)
            dates.add(date)
            bulle = f"{date} · {_lab('t_' + nom)} : "
            if v is None:
                # Fin du taux : marqueur creux sur le dernier niveau, le trait ne va pas plus loin.
                dernier = lignes[i - 1][1]
                p, = ax.plot([x], [dernier], "o", color=couleur, mfc="white", ms=7, mew=1.8,
                             zorder=4)
                figtools.infobulle(p, bulle + f"{_lab('ib_suppression')} · {texte}")
                ax.annotate(ft(_lab("fin_majore")), xy=(x, dernier), xytext=(9, 0),
                            textcoords="offset points", ha="left", va="center", fontsize=7.5,
                            color=couleur)
                continue
            x_suivant = _abscisse(lignes[i + 1][0]) if i + 1 < len(lignes) else fin
            ax.plot([x, x_suivant], [v, v], color=couleur, lw=2.2, solid_capstyle="butt",
                    zorder=2)
            suivant = lignes[i + 1][1] if i + 1 < len(lignes) else None
            if suivant is not None and suivant != v:
                ax.plot([x_suivant, x_suivant], [v, suivant], color=couleur, lw=1.2, zorder=2)
            if etat == "reprise":
                p, = ax.plot([x], [v], "D", color=couleur, mfc="white", ms=5.5, mew=1.5,
                             zorder=4)
                # À droite du losange : la mention de 1995 occupe déjà la gauche.
                ax.annotate(ft(_lab("dans_code")), xy=(x, v), xytext=(-4, -8),
                            textcoords="offset points", ha="left", va="top", fontsize=7.5,
                            color=couleur)
            else:
                p, = ax.plot([x], [v], "o", color=couleur, ms=5, zorder=4)
                ax.annotate(_pct(v), xy=(x, v), xytext=(4, 4), textcoords="offset points",
                            ha="left", va="bottom", fontsize=8.5, fontweight="bold",
                            color=couleur, zorder=5)
                if nom == "intermediaire" and etat == "creation":
                    ax.annotate(ft(_lab("hors_code")), xy=(x, v), xytext=(-4, -8),
                                textcoords="offset points", ha="left", va="top",
                                fontsize=7.5, color=couleur)
            figtools.infobulle(p, bulle + f"{_pct(v)} · {texte}")
        if lignes:
            poignees.append(Line2D([], [], color=couleur, lw=2.2, marker="o", ms=5,
                                   label=ft(_lab("t_" + nom))))
    # Les graduations sont les dates d'effet elles-mêmes, et la dernière année tracée.
    graduations = sorted(dates)
    ax.set_xticks([_abscisse(g) for g in graduations] + [FIN_TAUX])
    ax.set_xticklabels([ft(_lab("x_1988")) if g == "1988-07-01" else g[:4]
                        for g in graduations] + [str(FIN_TAUX)])
    for g in graduations:
        ax.axvline(_abscisse(g), color="#8b949e", lw=0.6, ls=(0, (1, 3)), zorder=1)
    ax.set_xlim(1987.3, fin + 0.6)
    ax.set_ylim(0, 32)
    ax.set_yticks(range(0, 31, 5))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _p: f"{y:g}"))
    ax.set_xlabel(ft(_lab("x_effet")))
    ax.set_ylabel(ft(_lab("y_taux")))
    ax.grid(True, axis="y", alpha=0.3)
    _legende(ax, poignees, ncol=4)
    fig.tight_layout()
    return fig


def table_taux():
    """Une ligne par taux et par date d'effet, avec ce que fait le texte et sa référence."""
    import pandas as pd
    lignes = []
    for nom, serie in _taux().items():
        for date, v, etat, texte, lien in serie:
            lignes.append({
                _lab("c_taux"): _lab("t_" + nom),
                _lab("c_effet"): date,
                _lab("c_valeur_pct"): v,
                _lab("c_etat"): _lab("e_" + etat),
                _lab("c_texte"): texte,
                _lab("c_jort"): lien,
            })
    return pd.DataFrame(lignes)
