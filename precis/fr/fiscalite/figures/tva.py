"""Figure « ce que rapporte la TVA » du livre *Fiscalité*.

TROIS BASES DU PIB, JAMAIS RACCORDÉES. La taxe est rapportée au PIB aux prix courants de
chacune des trois bases des comptes nationaux — 1983, 1997, 2015 —, sur les années que
chaque base porte (série `pib-courant-par-base`, annexe du site sur le PIB). Chaque base est
une courbe distincte ; aucun coefficient de passage n'est calculé ; une année publiée dans
deux bases (1997-2009, 2010-2017) porte deux points, chacun rapporté au PIB de sa base. Les
années 1986-1991 reposent sur un PIB que la série dit « présumé » de base 1983 (aucune série
de base connue avant 1992) : les points de 1988 à 1991 sont tracés en pâle. Les valeurs que
le ministère des Finances publie sans les rattacher à une base (2002-2004 et 2025) sont des
losanges gris, hors de toute courbe. Le marqueur plein dit un PIB publié dans sa base, ou dont la source ne dit pas s'il est
rétropolé (base 1983) ; le marqueur creux, un PIB recalculé pour le passé par l'INS (rétropolé).

LA RUPTURE DE SÉRIE EST LE SUJET, PAS UN DÉTAIL. La rubrique « 2.2 TVA » du ministère des
Finances est continue depuis 1986, et c'est le ministère lui-même qui l'intitule ainsi ; or la
taxe sur la valeur ajoutée est créée par la loi n° 88-61 du 2 juin 1988 et n'entre en vigueur
qu'au 1er juillet 1988. Les exercices 1986 et 1987 portent donc les taxes sur le chiffre
d'affaires que le code de 1988 remplace, non la TVA : ils sont tracés en pointillé gris,
séparés du reste par une bande verticale.

UN RAPPORT QUI NE DÉPEND D'AUCUN PIB. L'axe droit rapporte la taxe aux dépenses totales de
l'État, qui ne sont publiées qu'à partir de 1990 : la courbe de droite traverse les
changements de base sans rupture, et ne pénètre jamais la zone grisée.

LES RÉFORMES. Quatre bandes claires marquent les grandes réformes que le chapitre décrit
(1995-1996, 1998-1999, 2007, 2016-2018) ; les années de changement de base sont des traits
verticaux pointillés, avec le nom de la base.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import pandas as pd

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDATA = HERE.parent / "figdata"

SERIE_COMPOSITION = "recettes-fiscales-composition"
SERIE_RATIOS = "irpp-ratios"
SERIE_PIB = "pib-courant-par-base"
SERIES_RENDEMENT = (SERIE_COMPOSITION, SERIE_RATIOS, SERIE_PIB)

# Première année d'application de la TVA : le code promulgué par la loi n° 88-61 du
# 2 juin 1988 s'applique à compter du 1er juillet 1988. L'exercice 1988 n'est donc taxé
# qu'au second semestre, et l'assujettissement s'étend ensuite par paliers — commerce de
# gros en 1989, commerce de détail en 1996 seulement.
ANNEE_TVA = 1988

# Les dépenses totales de l'État ne sont publiées qu'à partir de 1990 : la courbe de
# droite commence donc deux ans après la création de la taxe.
ANNEE_DEPENSES = 1990

# Les quatre grandes réformes du chapitre (@sec-tva-reformes) : première et dernière année.
REFORMES = (("R1", 1995, 1996), ("R2", 1998, 1999), ("R3", 2007, 2007), ("R4", 2016, 2018))

# Une couleur par base, une forme par base : la courbe d'une base ne se confond jamais avec
# celle d'une autre, même en noir et blanc.
BASES = {
    1983: {"couleur": "#1a7f37", "marque": "o"},
    1997: {"couleur": "#8250df", "marque": "s"},
    2015: {"couleur": "#0969da", "marque": "^"},
}
ROUGE, GRIS, OR = "#d1242f", "#57606a", "#bf8700"

_L = {
    "lg_avant": {
        "fr": "Taxes antérieures sur le chiffre d'affaires / PIB (base 1983 présumée)",
        "ar": "الأداءات السابقة على رقم المعاملات / الناتج (أساس 1983 مفترض)"},
    "lg_base": {
        "fr": "TVA / PIB, base {b} (éch. gauche)",
        "ar": "الأداء على القيمة المضافة / الناتج، أساس {b} (يسار)"},
    "lg_presumee": {
        "fr": "base 1983 présumée (1988-1991)",
        "ar": "أساس 1983 مفترض (1988-1991)"},
    "lg_minfin": {
        "fr": "PIB du ministère non rattaché à une base (2002-2004, 2025)",
        "ar": "ناتج الوزارة غير المرتبط بأساس (2002-2004، 2025)"},
    "lg_dep": {
        "fr": "TVA / dépenses de l'État (éch. droite, sans PIB)",
        "ar": "الأداء على القيمة المضافة / نفقات الدولة (يمين، دون ناتج)"},
    "lg_reforme": {
        "fr": "grande réforme (R1 à R4)",
        "ar": "إصلاح كبير (R1 إلى R4)"},
    "lg_plein": {
        "fr": "plein : PIB publié dans sa base, ou rétropolation non précisée (base 1983) ; creux : PIB recalculé pour le passé",
        "ar": "مملوء: ناتج منشور في أساسه أو إعادة احتساب غير محدّدة (أساس 1983)؛ مفرغ: ناتج أعيد احتسابه للماضي"},
    "y_pib": {"fr": "En % du PIB de la base", "ar": "% من ناتج الأساس"},
    "y_dep": {"fr": "En % des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "title": {"fr": "Ce que rapporte la taxe sur la valeur ajoutée, 1986-2025",
              "ar": "مردود الأداء على القيمة المضافة، 1986-2025"},
    "rupture": {"fr": "création de la TVA\n(loi n° 88-61, 1er juillet 1988)",
                "ar": "إحداث الأداء على القيمة المضافة\n(القانون عدد 88-61، 1 جويلية 1988)"},
    "rup_pib": {"fr": "PIB : base {b}", "ar": "الناتج: أساس {b}"},
    "ib_pib": {"fr": "PIB {pib} MD", "ar": "الناتج {pib} م.د"},
    "ib_ratio": {"fr": "{a} · base {b} : {r} % du PIB ({pib} MD ; TVA {tva} MD)",
                 "ar": "{a} · أساس {b} : {r} % من الناتج (الناتج {pib} م.د ؛ الأداء {tva} م.د)"},
    "ib_minfin": {"fr": "{a} · PIB du ministère, base non rattachée : {r} % du PIB "
                        "({pib} MD ; TVA {tva} MD)",
                  "ar": "{a} · ناتج الوزارة، أساس غير مرتبط : {r} % من الناتج "
                        "(الناتج {pib} م.د ؛ الأداء {tva} م.د)"},
    "ib_dep": {"fr": "{a} · {r} % des dépenses de l'État", "ar": "{a} · {r} % من نفقات الدولة"},
    "ib_reforme": {"fr": "{nom} : {debut}-{fin}, réforme décrite au chapitre",
                   "ar": "{nom} : {debut}-{fin}، إصلاح موصوف في الفصل"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_base": {"fr": "Base du PIB", "ar": "أساس الناتج"},
    "col_pib": {"fr": "PIB de cette base (MD courants)",
                "ar": "ناتج هذا الأساس (م.د جارية)"},
    "col_retro": {"fr": "PIB recalculé pour le passé", "ar": "ناتج أعيد احتسابه للماضي"},
    "col_ratio": {"fr": "TVA en % du PIB de cette base", "ar": "الأداء % من ناتج هذا الأساس"},
    "col_dep": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "col_rec": {"fr": "% des recettes fiscales", "ar": "% من المداخيل الجبائية"},
    "col_mdt": {"fr": "TVA (MDT)", "ar": "الأداء على القيمة المضافة (م.د)"},
    "col_src": {"fr": "Source du PIB", "ar": "مصدر الناتج"},
    "b_presumee": {"fr": "1983 (présumée)", "ar": "1983 (مفترض)"},
    "b_minfin": {"fr": "non rattachée (ministère des Finances)",
                 "ar": "غير مرتبط (وزارة المالية)"},
    "r_oui": {"fr": "oui", "ar": "نعم"},
    "r_non": {"fr": "non", "ar": "لا"},
    "r_np": {"fr": "non précisé par la source", "ar": "غير محدّد في المصدر"},
}


def _lab(key: str, **kw) -> str:
    texte = _L[key].get(figtools.lang(), _L[key]["fr"])
    return texte.format(**kw) if kw else texte


def _donnees():
    """Une ligne par (année, base du PIB) : la TVA rapportée au PIB de cette base.

    La composition des recettes porte le montant de TVA ; les ratios de l'impôt sur le
    revenu portent les dépenses totales ; la série des PIB par base porte, pour chaque
    année, un PIB par base qui la publie. Une année publiée dans deux bases a deux lignes.
    """
    comp = figtools.series(SERIE_COMPOSITION)[["annee", "tva_MDT", "tva_pct"]]
    dep = figtools.series(SERIE_RATIOS)[["annee", "depenses_totales_MDT"]]
    pib = figtools.series(SERIE_PIB).copy()
    texte = pib["base"].str
    pib["base_num"] = texte.extract(r"(1983|1997|2015)", expand=False).astype("Int64")
    pib["presumee"] = texte.contains("présumée")
    pib["minfin"] = texte.startswith("non rattachée")
    d = pib.merge(comp, on="annee", how="inner").merge(dep, on="annee", how="left")
    d["tva_sur_pib_pct"] = 100 * d["tva_MDT"] / d["pib_MD"]
    d["tva_sur_depenses_pct"] = 100 * d["tva_MDT"] / d["depenses_totales_MDT"]
    return d.sort_values(["annee", "base_num"], na_position="last").reset_index(drop=True)


def _depenses():
    """TVA en % des dépenses de l'État, une ligne par année : aucun PIB n'y intervient."""
    comp = figtools.series(SERIE_COMPOSITION)[["annee", "tva_MDT"]]
    dep = figtools.series(SERIE_RATIOS)[["annee", "depenses_totales_MDT"]]
    d = comp.merge(dep, on="annee")
    d = d[d["annee"] >= ANNEE_DEPENSES].dropna(subset=["depenses_totales_MDT"])
    return d.assign(pct=100 * d["tva_MDT"] / d["depenses_totales_MDT"])


def _nom_base(r) -> str:
    if r.minfin:
        return _lab("b_minfin")
    if r.presumee:
        return _lab("b_presumee")
    return str(int(r.base_num))


def _retro(valeur: str) -> str:
    cle = {"oui": "r_oui", "non": "r_non"}.get(str(valeur), "r_np")
    return _lab(cle)


def table():
    d = _donnees()
    rec = figtools.series(SERIE_COMPOSITION).set_index("annee")["tva_pct"]
    dep = _depenses().set_index("annee")["pct"]
    lignes = []
    for r in d.itertuples(index=False):
        lignes.append({
            _lab("col_annee"): int(r.annee),
            _lab("col_base"): _nom_base(r),
            _lab("col_pib"): round(r.pib_MD, 1),
            _lab("col_retro"): _retro(r.retropole),
            _lab("col_mdt"): r.tva_MDT,
            _lab("col_ratio"): round(r.tva_sur_pib_pct, 2),
            _lab("col_dep"): round(dep[r.annee], 2) if r.annee in dep.index else None,
            _lab("col_rec"): round(rec[r.annee], 2),
            _lab("col_src"): r.publication,
        })
    return pd.DataFrame(lignes)


def prepare(generated: str | None = None):
    figtools.write_figdata(
        table(), FIGDATA / "fig_tva_rendement.csv", *SERIES_RENDEMENT,
        note=("rendement de la TVA en points du PIB de chaque base (1983, 1997, 2015), jamais "
              "raccordées, et en part des dépenses de l'État, 1986-2025 ; rupture de série en "
              "1988, les exercices antérieurs portant les taxes sur le chiffre d'affaires "
              "remplacées par le code de 1988 ; les dépenses totales ne sont publiées qu'à "
              "partir de 1990"),
        generated=generated)
    return _donnees()


def fig_rendement():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    dep = _depenses()
    annees = list(d["annee"].astype(int))
    x0, x1 = min(annees), max(annees)

    fig, ax1 = plt.subplots(figsize=(9.5, 6.0))
    ax2 = ax1.twinx()

    # La bande grise couvre les années où la rubrique mesure autre chose que la TVA.
    ax1.axvspan(x0 - 0.5, ANNEE_TVA - 0.5, color="#8b949e", alpha=0.13, lw=0)
    ax1.axvline(ANNEE_TVA - 0.5, color=GRIS, lw=1.2, ls="--")

    # Les quatre grandes réformes : des bandes claires, sous les courbes.
    for nom, debut, fin in REFORMES:
        bande = ax1.axvspan(debut - 0.5, fin + 0.5, color=OR, alpha=0.12, lw=0, zorder=0)
        figtools.infobulle(bande, _lab("ib_reforme", nom=nom, debut=debut, fin=fin))
        ax1.annotate(nom, xy=((debut + fin) / 2, 1), xycoords=("data", "axes fraction"),
                     xytext=(0, -3), textcoords="offset points", ha="center", va="top",
                     fontsize=7.5, color=OR)

    # Les courbes, base par base : un point par appel pour porter son infobulle.
    ratio = {}
    for base, st in BASES.items():
        g = d[(d["base_num"] == base) & (d["annee"] >= ANNEE_TVA)]
        ax1.plot(g["annee"], g["tva_sur_pib_pct"], color=st["couleur"], lw=1.8, zorder=2)
        for r in g.itertuples(index=False):
            pale = r.presumee
            creux = str(r.retropole) == "oui"
            p, = ax1.plot([r.annee], [r.tva_sur_pib_pct], st["marque"], ms=5,
                          color=st["couleur"], alpha=0.4 if pale else 1.0,
                          mfc="white" if creux else st["couleur"], mew=1.2, zorder=3)
            figtools.infobulle(p, _lab("ib_ratio", a=int(r.annee), b=_nom_base(r),
                                       r=f"{r.tva_sur_pib_pct:.2f}".replace(".", ","),
                                       pib=f"{r.pib_MD:,.0f}".replace(",", " "),
                                       tva=f"{r.tva_MDT:,.0f}".replace(",", " ")))
        ratio[base] = g

    # Avant la TVA : les taxes sur le chiffre d'affaires, en pointillé gris (base 1983 présumée).
    avant = d[(d["base_num"] == 1983) & (d["annee"] < ANNEE_TVA)]
    ax1.plot(avant["annee"], avant["tva_sur_pib_pct"], "o:", color=GRIS, lw=1.6, ms=4,
             zorder=2)
    for r in avant.itertuples(index=False):
        p, = ax1.plot([r.annee], [r.tva_sur_pib_pct], "o", ms=4, color=GRIS, zorder=3)
        figtools.infobulle(p, _lab("ib_ratio", a=int(r.annee), b=_nom_base(r),
                                   r=f"{r.tva_sur_pib_pct:.2f}".replace(".", ","),
                                   pib=f"{r.pib_MD:,.0f}".replace(",", " "),
                                   tva=f"{r.tva_MDT:,.0f}".replace(",", " ")))

    # Les valeurs du ministère non rattachées à une base : des losanges gris, seuls.
    for r in d[d["minfin"]].itertuples(index=False):
        p, = ax1.plot([r.annee], [r.tva_sur_pib_pct], "D", ms=5, mfc="white", mec=GRIS,
                      mew=1.2, zorder=3)
        figtools.infobulle(p, _lab("ib_minfin", a=int(r.annee),
                                   r=f"{r.tva_sur_pib_pct:.2f}".replace(".", ","),
                                   pib=f"{r.pib_MD:,.0f}".replace(",", " "),
                                   tva=f"{r.tva_MDT:,.0f}".replace(",", " ")))

    # Le rapport aux dépenses : aucune base, une seule courbe.
    ax2.plot(dep["annee"], dep["pct"], "--", color=ROUGE, lw=1.6, zorder=2)
    for r in dep.itertuples(index=False):
        p, = ax2.plot([r.annee], [r.pct], "x", ms=4, color=ROUGE, zorder=3)
        figtools.infobulle(p, _lab("ib_dep", a=int(r.annee),
                                   r=f"{r.pct:.2f}".replace(".", ",")))

    # Les changements de base : un trait vertical à la première année de la base suivante.
    for annee, base in ((1997, 1997), (2010, 2015)):
        figtools.marque_rupture(ax1, annee)
        ax1.annotate(figtools.fig_text(_lab("rup_pib", b=base)), xy=(annee - 0.5, 0),
                     xycoords=("data", "axes fraction"), xytext=(-4, 4),
                     textcoords="offset points", ha="right", va="bottom", fontsize=7,
                     color=GRIS)

    bas, haut = ax1.get_ylim()
    y_texte = bas + 0.86 * (haut - bas)
    ax1.annotate(ft(_lab("rupture")), xy=(ANNEE_TVA - 0.5, y_texte),
                 xytext=(ANNEE_TVA + 1.0, y_texte), fontsize=8, color=GRIS, va="center",
                 arrowprops=dict(arrowstyle="->", color=GRIS, lw=1))

    ax1.set_ylabel(ft(_lab("y_pib")))
    ax2.set_ylabel(ft(_lab("y_dep")), color=ROUGE)
    ax1.set_xlabel(ft(_lab("xlabel")))
    ax1.set_xlim(x0 - 0.8, x1 + 0.8)
    ax1.set_title(ft(_lab("title")))
    ax1.grid(True, alpha=0.3)

    poignees = [Line2D([], [], color=st["couleur"], marker=st["marque"], ms=5, lw=1.8,
                       label=ft(_lab("lg_base", b=base))) for base, st in BASES.items()]
    poignees.append(Line2D([], [], color=BASES[1983]["couleur"], marker="o", ms=5, lw=0,
                           alpha=0.4, label=ft(_lab("lg_presumee"))))
    poignees.append(Line2D([], [], color=GRIS, marker="o", ms=4, lw=1.6, ls=":",
                           label=ft(_lab("lg_avant"))))
    poignees.append(Line2D([], [], color=GRIS, marker="D", mfc="white", ms=5, lw=0,
                           label=ft(_lab("lg_minfin"))))
    poignees.append(Line2D([], [], color=ROUGE, marker="x", ms=4, lw=1.6, ls="--",
                           label=ft(_lab("lg_dep"))))
    poignees.append(Patch(facecolor=OR, alpha=0.25, label=ft(_lab("lg_reforme"))))
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ms=5, lw=0,
                           label=ft(_lab("lg_plein"))))
    fig.tight_layout(rect=(0, 0.2, 1, 1))
    fig.legend(handles=poignees, loc="lower center", ncol=2, fontsize=7.5, frameon=False)
    return fig


# --- La frise des réformes ----------------------------------------------------------------------
#
# DES JALONS, PAS UN CALENDRIER COMPLET. Une ligne par règle de base ou par dispositif ; sur
# chaque ligne, les ruptures que le registre du chapitre désigne ainsi (cercle plein) et la
# naissance du dispositif dans le code de 1988 (carré). Un losange creux dit une loi dont la
# date d'effet n'est pas établie (posée à l'année de la loi) ; un cercle creux, une rupture
# dont le classement attend confirmation. Le relevé est tenu à la main, ligne à ligne, d'après
# les registres du chapitre : `tva/frise-reformes.csv`.
RELEVES = HERE.parent / "tva"
FRISE = "tva-frise-reformes"
PISTES_FRISE = ["Champ et taux", "Réductions et suspensions par décret", "Forfaits",
                "Droit à déduction", "Crédit et restitution", "Régime suspensif",
                "Retenue à la source", "Déclaration et facture"]
FIN_FRISE = 2026


def _sources_frise() -> list[str]:
    import yaml
    return list(yaml.safe_load(
        (RELEVES / "frise-reformes.csv.yml").read_text(encoding="utf-8"))["sources"])


figtools.register_provenance(
    FRISE, titre="Les réformes de la TVA, 1988-2026 : jalons des registres du chapitre",
    sources=_sources_frise(), unite="dates d'effet",
    perimetre=("règles de base et dispositifs du chapitre : naissance dans le code de 1988 et "
               "ruptures que les registres désignent"),
    caveats=("Les jalons reprennent les registres du chapitre ; les étapes et les ajustements "
             "n'y figurent pas. Une loi a une date d'effet non établie (forfaits de 1993) : elle est "
             "posée à l'année de la loi. Le "
             "classement en rupture de 2014 (achats en espèces) et de 2016 (facture "
             "électronique) attend confirmation."))
_L.update({
    "f_title": {"fr": "Les réformes de la TVA, 1988-2026", "ar": "إصلاحات الأداء على القيمة المضافة، 1988-2026"},
    "f_periodes": {"fr": "Périodes du chapitre", "ar": "فترات الفصل"},
    "f_naissance": {"fr": "naissance du dispositif dans le code de 1988",
                    "ar": "نشأة الآلية في مجلة 1988"},
    "f_rupture": {"fr": "rupture désignée par le registre", "ar": "قطيعة يعيّنها السجل"},
    "f_non_etablie": {"fr": "date d'effet non établie (année de la loi)",
                      "ar": "تاريخ النفاذ غير ثابت (سنة القانون)"},
    "f_confirmer": {"fr": "rupture, classement à confirmer", "ar": "قطيعة، تصنيف قيد التأكيد"},
})


def _frise():
    d = pd.read_csv(RELEVES / "frise-reformes.csv")
    return d


def table_frise():
    d = _frise()
    return pd.DataFrame({
        "Ligne": d["piste"], "Nature": d["nature"], "État": d["etat"],
        "Date d'effet": d["date"].fillna(d["debut"].astype("Int64").astype(str) + "-"
                                         + d["fin"].astype("Int64").astype(str)),
        "Libellé": d["etiquette"], "Ce que dit le registre": d["libelle"],
        "Ancre du registre": d["ancre"], "Texte": d["texte"].fillna(""),
        "Article": d["localisateur"].fillna("")})


def fig_frise():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _frise()
    n = len(PISTES_FRISE)
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    # Les périodes, en tête.
    for k, r in enumerate(d[d["nature"] == "periode"].itertuples()):
        x0, x1 = r.debut, r.fin + 1
        bande = ax.barh([n], [x1 - x0], left=[x0], height=0.7, color=OR, alpha=0.30 + 0.1 * (k % 2),
                        edgecolor="white", lw=1, zorder=2)
        figtools.infobulle(bande[0], f"{r.etiquette} · {r.debut}-{r.fin} · {r.libelle}")
        ax.text((x0 + x1) / 2, n, ft(r.etiquette if len(r.etiquette) < 4 else
                                      r.etiquette.replace("mise en place", "mise en\nplace")),
                ha="center", va="center", fontsize=7.5 if len(r.etiquette) < 4 else 6.8,
                color="#1f2328", zorder=3)
        # Une bande légère traverse la frise : la période se lit sur chaque ligne.
        ax.axvspan(x0, x1, color=OR, alpha=0.06, lw=0, zorder=0)
    ax.text(1987.1, n + 0.62, ft(_lab("f_periodes")), ha="left", va="center", fontsize=7.6, color=GRIS)
    # Les jalons.
    couleur = {"naissance": "#57606a", "rupture": "#bc4c00"}
    haut = {}
    for r in d[d["nature"] != "periode"].itertuples():
        y = n - 1 - PISTES_FRISE.index(r.piste)
        x = figtools.abscisse_date(r.date) if "-" in str(r.date) else float(r.date) + 0.5
        marque = "s" if r.nature == "naissance" else "o"
        style = dict(ms=7, color=couleur[r.nature], zorder=4, mew=1.4)
        if r.etat == "date non établie":
            marque, style["mfc"] = "D", "white"
        elif r.etat == "classement à confirmer":
            style["mfc"] = "white"
        p, = ax.plot([x], [y], marque, **style)
        figtools.infobulle(p, f"{str(r.date)[:4]} · {r.piste} · {r.etiquette} · {r.libelle} "
                              f"({r.etat}) · {r.texte}, {r.localisateur}")
        # Le libellé est posé une fois sur deux au-dessus et au-dessous, pour ne pas se chevaucher.
        k = haut.get(y, 0)
        haut[y] = k + 1
        ax.annotate(ft(r.etiquette), xy=(x, y), xytext=(0, 8 if k % 2 == 0 else -9),
                    textcoords="offset points", ha="center",
                    va="bottom" if k % 2 == 0 else "top", fontsize=6.6, color="#1f2328")
    ax.axvline(ANNEE_TVA + 0.5, color=GRIS, lw=0.8, ls=(0, (2, 2)), zorder=1)
    ax.set_yticks(range(n))
    ax.set_yticklabels([ft(p.replace("Réductions et suspensions par décret", "Réductions et suspensions\npar décret"))
                        for p in reversed(PISTES_FRISE)], fontsize=7.6)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(1987, FIN_FRISE + 1)
    ax.set_ylim(-0.7, n + 0.7)
    ax.set_xticks(list(range(1990, 2030, 5)))
    ax.grid(True, axis="x", alpha=0.3, zorder=0)
    for cote in ("top", "right", "left"):
        ax.spines[cote].set_visible(False)
    ax.set_title(ft(_lab("f_title")), fontsize=10)
    fig.subplots_adjust(left=0.22, right=0.985, top=0.93, bottom=0.2)
    fig.legend(handles=[
        Line2D([], [], marker="s", color="#57606a", ls="", ms=7, label=ft(_lab("f_naissance"))),
        Line2D([], [], marker="o", color="#bc4c00", ls="", ms=7, label=ft(_lab("f_rupture"))),
        Line2D([], [], marker="D", color="#bc4c00", mfc="white", ls="", ms=7,
               label=ft(_lab("f_non_etablie"))),
        Line2D([], [], marker="o", color="#bc4c00", mfc="white", ls="", ms=7,
               label=ft(_lab("f_confirmer"))),
    ], loc="lower center", ncol=2, fontsize=7.6, frameon=False)
    return fig


# --- La TVA dans les recettes indirectes de l'État --------------------------------------------
#
# AUCUN PIB. Quatre rubriques du ministère des Finances — TVA, droits de douane, droits de
# consommation, « autres impôts indirects » — rapportées à leur somme. La rubrique « TVA » de
# 1986 et 1987 porte les taxes sur le chiffre d'affaires que le code de 1988 remplace (bande
# grise, comme pour le rendement). La rubrique 2.4 « Autres impôts indirects » du classeur a
# trois lignes — fonds spéciaux du Trésor, fonds de concours, autres — que le classeur ne détaille
# pas : son contenu n'est pas décrit ici.
_INDIRECTS = (
    ("tva_MDT", "i_tva", "#1a7f37"),
    ("douanes_MDT", "i_douanes", "#bc4c00"),
    ("consommation_MDT", "i_conso", "#8250df"),
    ("autres_indirects_MDT", "i_autres", "#8b949e"),
)

_L.update({
    "i_tva": {"fr": "TVA", "ar": "الأداء على القيمة المضافة"},
    "i_douanes": {"fr": "Droits de douane", "ar": "المعاليم الديوانية"},
    "i_conso": {"fr": "Droits de consommation", "ar": "المعلوم على الاستهلاك"},
    "i_autres": {"fr": "Autres impôts indirects (rubrique du ministère : fonds spéciaux du Trésor, fonds de concours, autres)",
                 "ar": "أداءات غير مباشرة أخرى (باب الوزارة: صناديق الخزينة الخاصة، صناديق المساهمة، أخرى)"},
    "i_title": {"fr": "La TVA dans les recettes indirectes de l'État, 1986-2025",
                "ar": "الأداء على القيمة المضافة ضمن المداخيل غير المباشرة للدولة، 1986-2025"},
    "i_y": {"fr": "En % des recettes indirectes", "ar": "% من المداخيل غير المباشرة"},
    "i_total": {"fr": "Recettes indirectes (MDT)", "ar": "المداخيل غير المباشرة (م.د)"},
    "i_ib": {"fr": "{a} · {nom} : {r} % des recettes indirectes ({v} MD sur {t} MD)",
             "ar": "{a} · {nom} : {r} % من المداخيل غير المباشرة ({v} م.د من {t} م.د)"},
})


def _indirects():
    d = figtools.series(SERIE_COMPOSITION).copy()
    cols = [c for c, _, _ in _INDIRECTS]
    d["indirects_MDT"] = d[cols].sum(axis=1)
    for c in cols:
        d[c.replace("_MDT", "_part")] = 100 * d[c] / d["indirects_MDT"]
    return d


def table_indirects():
    d = _indirects()
    sortie = {_lab("col_annee"): d["annee"].astype(int)}
    for c, cle, _ in _INDIRECTS:
        sortie[f"{_lab(cle)} (%)"] = d[c.replace("_MDT", "_part")].round(2)
    sortie[_lab("i_total")] = d["indirects_MDT"].round(1)
    return pd.DataFrame(sortie)


def fig_indirects():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _indirects()
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    annees = d["annee"].astype(int).tolist()
    bas = [0.0] * len(d)
    for c, cle, couleur in _INDIRECTS:
        part = d[c.replace("_MDT", "_part")].tolist()
        haut = [b + p for b, p in zip(bas, part)]
        ax.fill_between(annees, bas, haut, color=couleur, alpha=0.85, lw=0.6,
                        edgecolor="white", label=ft(_lab(cle)), zorder=2)
        # Un point par année, sur le bord supérieur de la bande, pour porter l'infobulle.
        for a, b, h, p, v, t in zip(annees, bas, haut, part, d[c], d["indirects_MDT"]):
            m, = ax.plot([a], [(b + h) / 2], "o", ms=3.5, alpha=0, zorder=3)
            figtools.infobulle(m, _lab("i_ib", a=a, nom=_lab(cle),
                                       r=f"{p:.1f}".replace(".", ","),
                                       v=f"{v:,.0f}".replace(",", " "),
                                       t=f"{t:,.0f}".replace(",", " ")))
        bas = haut
    ax.axvspan(annees[0] - 0.5, ANNEE_TVA - 0.5, color="white", alpha=0.55, lw=0, zorder=4)
    ax.axvline(ANNEE_TVA - 0.5, color=GRIS, lw=1.2, ls="--", zorder=5)
    ax.annotate(ft(_lab("rupture")), xy=(ANNEE_TVA - 0.5, 50), xytext=(ANNEE_TVA + 0.8, 50),
                fontsize=8, color="black", va="center", zorder=6,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.8),
                arrowprops=dict(arrowstyle="->", color=GRIS, lw=1))
    ax.set_xlim(annees[0], annees[-1])
    ax.set_ylim(0, 100)
    ax.set_ylabel(ft(_lab("i_y")))
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_title(ft(_lab("i_title")))
    ax.grid(True, axis="y", alpha=0.3, zorder=0)
    fig.tight_layout(rect=(0, 0.17, 1, 1))
    fig.legend(*ax.get_legend_handles_labels(), loc="lower center", ncol=2, fontsize=8,
               frameon=False)
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


def _pct(v: float) -> str:
    return f"{v:g}".replace(".", ",") + " %"


def _courbes_taux() -> dict:
    return {nom: (_lab("t_" + nom), couleur) for nom, couleur in _TAUX.items()}


def fig_taux():
    """Les quatre taux en escalier, chaque marche étiquetée de sa valeur.

    Le tracé est celui du composant commun (`figtools.fig_escalier`) ; ne sont dites ici que
    les mentions propres à la taxe : le taux de 10 % créé hors du code, son entrée dans le
    code, la suppression du taux majoré.
    """
    return figtools.fig_escalier(
        SERIE_TAUX, _courbes_taux(), colonne="taux", echelle=100, fin=FIN_TAUX,
        format_valeur=_pct, ylabel=_lab("y_taux"), xlabel=_lab("x_effet"),
        etiquettes_x={"1988-07-01": _lab("x_1988")},
        annotations={("intermediaire", "1995-01-01"): _lab("hors_code"),
                     ("intermediaire", "2002-01-01"): _lab("dans_code"),
                     ("majore", "2007-01-01"): _lab("fin_majore")},
        xlim=(1987.3, FIN_TAUX + 1.6), ylim=(0, 32), yticks=range(0, 31, 5), ncol=4,
        supprime=_lab("ib_suppression"))


def table_taux():
    """Une ligne par taux et par date d'effet, avec ce que fait le texte et sa référence."""
    return figtools.table_escalier(
        SERIE_TAUX, _courbes_taux(), colonne="taux", echelle=100,
        libelles={"parametre": _lab("c_taux"), "effet": _lab("c_effet"),
                  "valeur": _lab("c_valeur_pct"), "etat": _lab("c_etat"),
                  "texte": _lab("c_texte"), "jort": _lab("c_jort"),
                  **{e: _lab("e_" + e) for e in ("creation", "changement", "reprise",
                                                 "suppression")}})


# --- Les régimes par grande catégorie de produits et de services, à cinq dates -----------
# Une MATRICE, non une courbe : vingt-cinq catégories en lignes, cinq dates repères en
# colonnes, une couleur par régime. La série dit, pour chaque catégorie et chaque date, le
# ou les régimes relevés sur les tableaux annexés au code (A : exonérations ; B : taux
# réduit ; B bis : taux intermédiaire ; C : taux majoré) ou à l'article 7 :
#   - une case à plusieurs régimes est PARTAGÉE : la catégorie réunit des opérations que la
#     loi ne traite pas de la même façon (les soins au taux réduit, les appareils pour
#     handicapés exonérés) ;
#   - une case HACHURÉE porte un taux que la loi n'écrit pas : l'opération ne figure dans
#     aucun tableau, et relève du taux normal par la règle générale de l'article 7 ;
#   - une case BLANCHE dit que la catégorie ne figure dans aucun tableau à cette date — ce
#     qui n'est pas un taux ;
#   - les colonnes de 2008 et de 2014 viennent de deux recueils non officiels du code, et un petit
#     cercle le rappelle dans chaque case.
# Les libellés longs des catégories sont ceux de la série ; la figure emploie des libellés
# courts, tenus ici dans les deux langues.
SERIE_REGIMES = "tva-regimes-par-categorie"

_DATES_REGIMES = ["1988-07-01", "2008-01-01", "2014-01-01", "2017-01-01", "2026-01-01"]

# Ordre de lecture : du plus léger au plus lourd.
_REGIMES = {
    "exonéré": ("exonere", "#e3e6ea", "#3d444d"),
    "taux réduit": ("reduit", "#b4e0be", "#0f5323"),
    "taux intermédiaire": ("intermediaire", "#fbd0a5", "#7a3200"),
    "taux normal": ("normal", "#a9cbe8", "#05386b"),
    "taux majoré": ("majore", "#cdbbea", "#3f2283"),
}

# Groupes, dans l'ordre de lecture, et leurs catégories (identifiants de la série).
_GROUPES_REGIMES = [
    ("alimentation", ["alim_base", "sucre", "alim_transformes"]),
    ("sante", ["medicaments", "sante_soins"]),
    ("education", ["enseignement", "livres_presse_culture"]),
    ("logement", ["logement_neuf", "logement_social_location"]),
    ("energie", ["electricite_gaz", "produits_petroliers", "energies_renouvelables", "eau"]),
    ("transport", ["transport_services", "transport_materiel"]),
    ("tourisme", ["hotellerie_tourisme", "restauration"]),
    ("professions", ["professions_liberales"]),
    ("agriculture", ["agriculture_peche"]),
    ("numerique", ["informatique_numerique", "equipements_investissement", "telecom_poste"]),
    ("finance", ["finance_assurance"]),
    ("tableau_c", ["alim_tableau_c", "durables_luxe_vehicules"]),
]

_L.update({
    # Régimes.
    "r_exonere": {"fr": "Exonéré", "ar": "معفى"},
    "r_reduit": {"fr": "Taux réduit", "ar": "النسبة المخفضة"},
    "r_intermediaire": {"fr": "Taux intermédiaire", "ar": "النسبة الوسيطة"},
    "r_normal": {"fr": "Taux normal", "ar": "النسبة العادية"},
    "r_majore": {"fr": "Taux majoré", "ar": "النسبة المرتفعة"},
    "exo": {"fr": "exo.", "ar": "معفى"},
    "lg_deduit": {"fr": "Taux que la loi n'écrit pas : règle générale de l'article 7",
                  "ar": "نسبة لا ينصّ عليها القانون: القاعدة العامة للفصل 7"},
    "lg_prive": {"fr": "D'après un recueil non officiel du code",
                 "ar": "حسب مجموعة غير رسمية للمجلة"},
    "lg_vide": {"fr": "Catégorie absente des tableaux à cette date",
                "ar": "صنف غير وارد بالجداول في هذا التاريخ"},
    # Colonnes : date repère, nature de la source.
    "d_1988-07-01": {"fr": "1er juillet\n1988", "ar": "1 جويلية\n1988"},
    "d_2008-01-01": {"fr": "janvier\n2008", "ar": "جانفي\n2008"},
    "d_2014-01-01": {"fr": "janvier\n2014", "ar": "جانفي\n2014"},
    "d_2017-01-01": {"fr": "1er janvier\n2017", "ar": "1 جانفي\n2017"},
    "d_2026-01-01": {"fr": "1er janvier\n2026", "ar": "1 جانفي\n2026"},
    "n_jort": {"fr": "Journal officiel", "ar": "الرائد الرسمي"},
    "n_prive": {"fr": "recueil\nnon officiel", "ar": "مجموعة غير رسمية"},
    "n_officielle": {"fr": "édition officielle\ndu code", "ar": "الطبعة الرسمية\nللمجلة"},
    # Groupes.
    "gr_alimentation": {"fr": "Alimentation", "ar": "التغذية"},
    "gr_sante": {"fr": "Santé", "ar": "الصحة"},
    "gr_education": {"fr": "Éducation et culture", "ar": "التعليم والثقافة"},
    "gr_logement": {"fr": "Logement", "ar": "السكن"},
    "gr_energie": {"fr": "Énergie et eau", "ar": "الطاقة والماء"},
    "gr_transport": {"fr": "Transport", "ar": "النقل"},
    "gr_tourisme": {"fr": "Tourisme", "ar": "السياحة"},
    "gr_professions": {"fr": "Professions", "ar": "المهن"},
    "gr_agriculture": {"fr": "Agriculture", "ar": "الفلاحة"},
    "gr_numerique": {"fr": "Équipements et numérique", "ar": "التجهيزات والرقميات"},
    "gr_finance": {"fr": "Finance", "ar": "المالية"},
    "gr_tableau_c": {"fr": "Anciens biens du tableau C", "ar": "مواد الجدول ج سابقا"},
    # Catégories, en libellés courts.
    "k_alim_base": {"fr": "Farines, pain, pâtes, lait, huiles",
                    "ar": "الفارينة والخبز والعجين والحليب والزيوت"},
    "k_sucre": {"fr": "Sucre", "ar": "السكر"},
    "k_alim_transformes": {"fr": "Conserves, fruits et légumes transformés, maïs",
                           "ar": "المصبرات والخضر والغلال المحوّلة والذرة"},
    "k_medicaments": {"fr": "Médicaments et produits pharmaceutiques",
                      "ar": "الأدوية والمواد الصيدلية"},
    "k_sante_soins": {"fr": "Soins, cliniques, appareils pour handicapés",
                      "ar": "العلاج والمصحات وأجهزة المعوقين"},
    "k_enseignement": {"fr": "Enseignement et garderies", "ar": "التعليم والمحاضن"},
    "k_livres_presse_culture": {"fr": "Livres, presse, culture, cinéma",
                                "ar": "الكتب والصحافة والثقافة والسينما"},
    "k_logement_neuf": {"fr": "Logements neufs des promoteurs",
                        "ar": "المساكن الجديدة لدى الباعثين العقاريين"},
    "k_logement_social_location": {"fr": "Logement social, loyers, prêts au logement",
                                   "ar": "السكن الاجتماعي والكراء وقروض السكن"},
    "k_electricite_gaz": {"fr": "Électricité", "ar": "الكهرباء"},
    "k_produits_petroliers": {"fr": "Produits pétroliers, gaz de pétrole",
                              "ar": "المواد البترولية وغاز البترول"},
    "k_energies_renouvelables": {"fr": "Solaire, énergies renouvelables",
                                 "ar": "الطاقة الشمسية والطاقات المتجددة"},
    "k_eau": {"fr": "Eau", "ar": "الماء"},
    "k_transport_services": {"fr": "Services de transport", "ar": "خدمات النقل"},
    "k_transport_materiel": {"fr": "Aéronefs, navires, matériel ferroviaire",
                             "ar": "الطائرات والسفن والمعدات الحديدية"},
    "k_hotellerie_tourisme": {"fr": "Hôtellerie et activités touristiques",
                              "ar": "النزل والأنشطة السياحية"},
    "k_restauration": {"fr": "Restauration", "ar": "المطاعم"},
    "k_professions_liberales": {"fr": "Professions libérales non médicales",
                                "ar": "المهن الحرة غير الطبية"},
    "k_agriculture_peche": {"fr": "Agriculture et pêche : intrants, équipements",
                            "ar": "الفلاحة والصيد البحري: المدخلات والتجهيزات"},
    "k_informatique_numerique": {"fr": "Informatique, services numériques, formation",
                                 "ar": "الإعلامية والخدمات الرقمية والتكوين"},
    "k_equipements_investissement": {"fr": "Équipements d'investissement",
                                     "ar": "تجهيزات الاستثمار"},
    "k_telecom_poste": {"fr": "Télécommunications, radio-télévision, poste",
                        "ar": "الاتصالات والإذاعة والتلفزة والبريد"},
    "k_finance_assurance": {"fr": "Finance et assurance", "ar": "المالية والتأمين"},
    "k_alim_tableau_c": {"fr": "Café, thé, épices, cacao, boissons, tabacs",
                         "ar": "القهوة والشاي والتوابل والكاكاو والمشروبات والتبغ"},
    "k_durables_luxe_vehicules": {"fr": "Biens durables et de luxe, voitures",
                                  "ar": "المواد المعمّرة والكمالية والسيارات"},
    # Colonnes des données.
    "c_groupe": {"fr": "Groupe", "ar": "المجموعة"},
    "c_categorie": {"fr": "Catégorie", "ar": "الصنف"},
    "c_date_repere": {"fr": "Date repère", "ar": "التاريخ المرجعي"},
    "c_regime": {"fr": "Régime", "ar": "النظام"},
    "c_taux_pct": {"fr": "Taux (%)", "ar": "النسبة (%)"},
    "c_tableau": {"fr": "Tableau ou article", "ar": "الجدول أو الفصل"},
    "c_numeros": {"fr": "Numéros", "ar": "الأعداد"},
    "c_source_etat": {"fr": "Source de l'état", "ar": "مصدر الحالة"},
    "c_pages": {"fr": "Pages", "ar": "الصفحات"},
    "c_nature": {"fr": "Nature de la source", "ar": "طبيعة المصدر"},
    # Nature de la source, en clair.
    "l_JORT lu": {"fr": "Journal officiel", "ar": "الرائد الرسمي"},
    "l_édition officielle": {"fr": "édition du code publiée par le ministère des Finances",
                             "ar": "طبعة المجلة الصادرة عن وزارة المالية"},
    "l_recueil non officiel": {"fr": "d'après un recueil non officiel du code",
                        "ar": "حسب مجموعة غير رسمية للمجلة"},
    "l_déduit": {"fr": "la loi n'écrit pas le taux : il résulte de la règle générale de "
                       "l'article 7",
                 "ar": "لا ينصّ القانون على النسبة: تنتج عن القاعدة العامة للفصل 7"},
    # Tableau ou article.
    "tb_A": {"fr": "tableau A", "ar": "الجدول « أ »"},
    "tb_B": {"fr": "tableau B", "ar": "الجدول « ب »"},
    "tb_B bis": {"fr": "tableau B bis", "ar": "الجدول « ب مكرر »"},
    "tb_C": {"fr": "tableau C", "ar": "الجدول « ج »"},
    "tb_art. 7-3": {"fr": "article 7, numéro 3", "ar": "الفصل 7، العدد 3"},
    "tb_aucun (art. 7, al. 1er)": {"fr": "aucun tableau (article 7, premier alinéa)",
                                   "ar": "دون جدول (الفصل 7، الفقرة الأولى)"},
    "tb_hors tableau (décret annuel, art. 8)": {
        "fr": "hors tableau (décret annuel, article 8)",
        "ar": "خارج الجداول (أمر سنوي، الفصل 8)"},
    "tb_hors tableau (décret, art. 8)": {"fr": "hors tableau (décret, article 8)",
                                         "ar": "خارج الجداول (أمر، الفصل 8)"},
    "tb_hors tableau (loi n° 2002-103)": {"fr": "hors tableau (loi n° 2002-103)",
                                          "ar": "خارج الجداول (القانون عدد 103 لسنة 2002)"},
    "src_decrets": {"fr": "décrets annuels pris en application de l'article 8 du code",
                    "ar": "الأوامر السنوية المتخذة تطبيقا للفصل 8 من المجلة"},
})

figtools.register_provenance(
    SERIE_REGIMES,
    titre=("Régimes de taxe sur la valeur ajoutée de vingt-cinq catégories de produits et de "
           "services à cinq dates repères, du 1er juillet 1988 au 1er janvier 2026, d'après "
           "les tableaux annexés au code"),
    titre_ar=("أنظمة الأداء على القيمة المضافة لخمسة وعشرين صنفا من المواد والخدمات في خمسة "
              "تواريخ مرجعية، من 1 جويلية 1988 إلى 1 جانفي 2026، حسب الجداول الملحقة بالمجلة"),
    sources=["loi-88-61-tva", "recueil-tva-bm-2008", "recueil-codes-sefac-2014", "lf-2016",
             "lf-2017", "dgelf-code-tva-2025", "lf-2026", "loi-2006-80-reduction-taux",
             "loi2001-123-lf2002", "decret-2002-3356-tva-telecom", "lf-2018", "lf-2023", "lf-2025"],
    unite="régime (exonération ou taux), et taux en pourcentage de la base imposable",
    unite_ar="النظام (إعفاء أو نسبة)، والنسبة من القاعدة الخاضعة",
    perimetre=("une ligne par catégorie, par date repère et par régime, avec le tableau et "
               "les numéros où le régime se lit, la source de l'état et ses pages ; 173 lignes"),
    perimetre_ar=("سطر لكلّ صنف ولكلّ تاريخ مرجعي ولكلّ نظام، مع الجدول والأعداد التي يُقرأ "
                  "فيها النظام ومصدر الحالة وصفحاته؛ 173 سطرا"),
    caveats=("Les états de janvier 2008 et de janvier 2014 sont ceux de deux recueils non officiels "
             "du code, qui ne valent pas Journal officiel et n'ont pas été rapprochées de lui "
             "numéro par numéro. L'état du 1er janvier 2026 est celui de l'édition du code "
             "publiée par le ministère des Finances à jour au 1er janvier 2025, complétée par "
             "la loi de finances pour 2026. Dix-huit lignes portent un taux que la loi n'écrit "
             "pas : l'opération ne figure dans aucun tableau et relève du taux normal par la "
             "règle générale de l'article 7. La série ne couvre ni les opérations hors du "
             "champ de la taxe, ni l'exonération à la revente au détail, ni les régimes "
             "suspensifs ; une catégorie absente des tableaux à une date n'a pas de ligne, ce "
             "qui ne vaut pas taux normal. Un régime appliqué entre deux dates repères "
             "n'apparaît pas."),
    caveats_ar=("حالتا جانفي 2008 وجانفي 2014 مأخوذتان من طبعتين خاصتين للمجلة لا تقومان مقام "
                "الرائد الرسمي ولم تُقابلا به عددا عددا. حالة 1 جانفي 2026 هي حالة طبعة المجلة "
                "الصادرة عن وزارة المالية والمحيّنة في 1 جانفي 2025، مع إضافة قانون المالية "
                "لسنة 2026. ثمانية عشر سطرا تحمل نسبة لا ينصّ عليها القانون: العملية غير واردة "
                "بأيّ جدول وتخضع للنسبة العادية بمقتضى القاعدة العامة للفصل 7. لا تشمل السلسلة "
                "العمليات الخارجة عن ميدان تطبيق الأداء ولا الإعفاء عند البيع بالتفصيل ولا "
                "أنظمة توقيف العمل بالأداء؛ والصنف غير الوارد بالجداول في تاريخ ما لا سطر له، "
                "ولا يعني ذلك خضوعه للنسبة العادية. ولا يظهر نظام طُبّق بين تاريخين مرجعيين."),
)


def _regimes():
    """{(catégorie, date): [(régime, taux ou None, lecture)]}, régimes du plus léger au plus lourd."""
    d = figtools.series(SERIE_REGIMES)
    ordre = list(_REGIMES)
    cases = {}
    for cat, date, regime, taux, lecture in zip(
            d["categorie_id"], d["date_repere"], d["regime"], d["taux_pct"], d["lecture"]):
        taux = None if taux != taux else float(taux)
        cases.setdefault((cat, str(date)[:10]), []).append((regime, taux, lecture))
    for segments in cases.values():
        segments.sort(key=lambda s: ordre.index(s[0]))
    return cases


def fig_regimes():
    """La matrice : catégories en lignes, dates repères en colonnes, une couleur par régime."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    from matplotlib.patches import Patch, Rectangle
    from matplotlib.lines import Line2D
    cases = _regimes()
    arabe = figtools.lang() == "ar"
    lignes = [(g, c) for g, cats in _GROUPES_REGIMES for c in cats]
    m = len(_DATES_REGIMES)
    L, H, TITRE = 1.42, 1.0, 0.78       # largeur et hauteur d'une case, hauteur d'un titre de groupe
    ETIQ = 5.3                           # largeur réservée aux libellés des catégories
    fig, ax = plt.subplots(figsize=(8.8, 13.4))
    # Ordonnée du haut de chaque ligne ; chaque groupe est précédé de son titre.
    y, hauts, titres = 0.0, {}, {}
    for i, (g, c) in enumerate(lignes):
        if not i or lignes[i - 1][0] != g:
            titres[g] = y
            y += TITRE
        hauts[c] = y
        y += H
    total = y
    signe = -1 if arabe else 1           # en arabe, la matrice se lit de droite à gauche

    def abscisse(j):
        return signe * j * L - (L if arabe else 0)

    for j, date in enumerate(_DATES_REGIMES):
        x = abscisse(j)
        nature = {"1988-07-01": "n_jort", "2017-01-01": "n_jort",
                  "2026-01-01": "n_officielle"}.get(date, "n_prive")
        ax.text(x + L / 2, -0.72, ft(_lab("d_" + date)), ha="center", va="bottom",
                fontsize=10, fontweight="bold", linespacing=1.05)
        ax.text(x + L / 2, -0.62, ft(_lab(nature)), ha="center", va="top", fontsize=8,
                color="#57606a", style="italic", linespacing=1.0)
        for g, c in lignes:
            y0 = hauts[c]
            segments = cases.get((c, date), [])
            if not segments:
                ax.add_patch(Rectangle((x, y0), L, H, fc="white", ec="#c9d1d9", lw=0.6,
                                       ls=(0, (2, 2)), zorder=1))
                continue
            largeur = L / len(segments)
            ordre = segments[::-1] if arabe else segments
            for k, (regime, taux, lecture) in enumerate(ordre):
                cle, fond, encre = _REGIMES[regime]
                deduit = lecture == "déduit"
                p = Rectangle((x + k * largeur, y0), largeur, H, fc=fond, ec="white", lw=1.2,
                              zorder=2)
                ax.add_patch(p)
                if deduit:
                    ax.add_patch(Rectangle((x + k * largeur, y0), largeur, H, fc="none",
                                           ec=encre, lw=0, hatch="////", alpha=0.45, zorder=3))
                texte = _lab("exo") if taux is None else _pct(taux)
                ax.text(x + (k + 0.5) * largeur, y0 + H / 2, ft(texte), ha="center",
                        va="center", fontsize=9.6 if len(segments) < 3 else 7.6,
                        fontweight="bold" if taux is not None else "normal", color=encre,
                        zorder=5,
                        bbox=dict(boxstyle="round,pad=0.12", fc=fond, ec="none") if deduit
                        else None)
                figtools.infobulle(p, f"{_lab('k_' + c)} · "
                                      + _lab("d_" + date).replace("\n", " ") + " : "
                                      f"{_lab('r_' + cle)}"
                                      + ("" if taux is None else f" {_pct(taux)}")
                                      + f" · {_lab('l_' + lecture)}")
            if nature == "n_prive":
                ax.plot([x + (0.08 if arabe else L - 0.08)], [y0 + 0.14], "o", ms=3.4,
                        mfc="white", mec="#57606a", mew=0.8, zorder=6)
    # Libellés des lignes, et titre de chaque groupe au-dessus de ses lignes.
    bord = abscisse(0) + (L + 0.12 if arabe else -0.12)
    loin = bord + (ETIQ if arabe else -ETIQ)
    fin = abscisse(m - 1) + (0 if arabe else L)
    for g, c in lignes:
        ax.text(bord, hauts[c] + H / 2, ft(_lab("k_" + c)), ha="left" if arabe else "right",
                va="center", fontsize=9.6)
    for g, haut in titres.items():
        ax.text(loin, haut + TITRE - 0.2, ft(_lab("gr_" + g)),
                ha="right" if arabe else "left", va="bottom", fontsize=9.8, fontweight="bold",
                color="#24292f")
        ax.plot([loin, fin], [haut + TITRE - 0.1, haut + TITRE - 0.1], color="#8b949e", lw=0.8)
    gauche, droite = sorted([loin, fin])
    ax.set_xlim(gauche - 0.05, droite + 0.05)
    ax.set_ylim(total + 0.1, -1.9)
    ax.axis("off")
    poignees = [Patch(fc=fond, ec="#8b949e", lw=0.5, label=ft(_lab("r_" + cle)))
                for cle, fond, _e in _REGIMES.values()]
    poignees += [
        Patch(fc="white", ec="#3d444d", lw=0.5, hatch="////", label=ft(_lab("lg_deduit"))),
        Line2D([], [], ls="none", marker="o", ms=4.5, mfc="white", mec="#57606a", mew=0.9,
               label=ft(_lab("lg_prive"))),
        Patch(fc="white", ec="#c9d1d9", lw=0.8, ls=(0, (2, 2)), label=ft(_lab("lg_vide"))),
    ]
    fig.legend(handles=poignees[:5], loc="lower center", bbox_to_anchor=(0.5, 0.058),
               fontsize=9, frameon=False, ncol=5, handlelength=1.5, columnspacing=1.2)
    fig.legend(handles=poignees[5:], loc="lower center", bbox_to_anchor=(0.5, 0.004),
               fontsize=9, frameon=False, ncol=1, handlelength=1.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.995, bottom=0.092)
    return fig


def table_regimes():
    """Les 173 lignes de la série, en mots de lecteur : une par catégorie, date et régime."""
    import pandas as pd
    d = figtools.series(SERIE_REGIMES)
    refs = figtools._ref_index()
    groupe = {c: g for g, cats in _GROUPES_REGIMES for c in cats}
    rang = {c: i for i, c in enumerate(c for _g, cats in _GROUPES_REGIMES for c in cats)}
    ordre = list(_REGIMES)

    def source(cles: str) -> str:
        noms = []
        for cle in str(cles).split(";"):
            cle = cle.strip()
            if cle.startswith("fiscalite-tva-documentation.md"):
                # Seule source de la série qui ne soit pas une clé : les décrets annuels.
                noms.append(_lab("src_decrets"))
                continue
            ref = refs[cle]                      # une clé inconnue doit faire échouer le rendu
            noms.append(ref.get("title-short") or ref.get("title"))
        return " ; ".join(noms)

    d = d.assign(_rang=d["categorie_id"].map(rang), _reg=d["regime"].map(ordre.index))
    d = d.sort_values(["_rang", "date_repere", "_reg"])
    francais = figtools.lang() != "ar"
    lignes = []
    for r in d.itertuples(index=False):
        lignes.append({
            _lab("c_groupe"): _lab("gr_" + groupe[r.categorie_id]).replace("\n", " "),
            _lab("c_categorie"): r.categorie if francais else _lab("k_" + r.categorie_id),
            _lab("c_date_repere"): str(r.date_repere)[:10],
            _lab("c_regime"): _lab("r_" + _REGIMES[r.regime][0]),
            _lab("c_taux_pct"): None if r.taux_pct != r.taux_pct else float(r.taux_pct),
            _lab("c_tableau"): _lab("tb_" + r.tableau),
            _lab("c_numeros"): r.numeros,
            _lab("c_source_etat"): source(r.source_id),
            _lab("c_pages"): r.page,
            _lab("c_nature"): _lab("l_" + r.lecture),
        })
    return pd.DataFrame(lignes)
