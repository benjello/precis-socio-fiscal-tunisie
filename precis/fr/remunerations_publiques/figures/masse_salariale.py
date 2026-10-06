"""Figures « masse salariale du budget de l'État ».

    from figures import masse_salariale as ms
    figtools.figure_tabs(ms.fig_A(), ms.ratios_table(), ms.SERIE, slug=…)
    ms.figure_B(caption=…, note_lecture=…)

D'OÙ VIENNENT LES DONNÉES. Trois séries de `tunisia-data`, lues par `figtools.series()`
(l'entrepôt s'il est installé, sinon le cache `precis/_seriescache/`) :

  - `masse-salariale-ratios` : une ligne par année, 1990-2025 — masse salariale, dépenses de
    l'État, PIB employé, les trois parts, et pour le PIB sa source, sa base, son segment,
    s'il est rétropolé, et la rupture à marquer ;
  - `pib-courant-recouvrements` : les années où l'INS a publié le PIB dans deux bases ;
  - `masse-salariale-reconciliation` : les ratios rapportés par les rapports extérieurs.

RÈGLES DE TRACÉ (les mêmes que dans le livre *La compensation*).

  - **La part du PIB se trace par segments** (`segment_pib`) : le trait s'interrompt à chaque
    changement de source ou de base du PIB, et la base de chaque segment est écrite au-dessus
    du cadre. Rien n'est chaîné, aucun coefficient ne fait passer d'une base à l'autre.
  - **Les ruptures viennent des données** (colonne `rupture`) : trait vertical
    (`figtools.marque_rupture`), libellé court, texte complet dans l'infobulle du repère
    triangulaire.
  - **Un PIB rétropolé est un point creux.**
  - **La part dans les dépenses de l'État ne dépend d'aucun PIB** : elle reste d'un seul trait.
  - **Budgétaire et extérieur ne sont pas au même rang** : les ratios calculés sur le budget
    et les comptes de l'INS sont en traits, ceux des rapports du FMI et de la Banque mondiale
    en marques rouges sans trait.

La seule grandeur calculée ici est, pour la figure B, la masse salariale rapportée au PIB de la
base 1997 pour 2010-2017 : masse salariale de `masse-salariale-ratios` / PIB publié par l'INS
dans cette base (`pib-courant-recouvrements`). Elle retombe sur le tableau de la fiche
`docs/reconciliation-masse-salariale-pib.md` de l'entrepôt.

LA PROVENANCE AFFICHÉE. Le périmètre et les réserves du catalogue de l'entrepôt s'adressent à
qui trace la série (noms de colonnes, consignes de tracé, journal des corrections) ;
`PROVENANCE_LECTEUR` dit la même chose au lecteur, dans les deux langues.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, MaxNLocator

# helper partagé du précis (precis/scripts/figtools.py)
_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

SERIE = "masse-salariale-ratios"
SERIE_RECOUVREMENTS = "pib-courant-recouvrements"
SERIE_RECONCILIATION = "masse-salariale-reconciliation"
SERIES_B = (SERIE, SERIE_RECOUVREMENTS, SERIE_RECONCILIATION)

BLEU, VIOLET, ROUGE, GRIS, NOIR = "#0969da", "#8250df", "#cf222e", "#57606a", "#24292f"
FIN_FIGURE_B = 2020  # dernière année d'un ratio rapporté par un rapport extérieur

# libellés bilingues (FR source de vérité ; AR pour le livre arabe)
_L = {
    "x": {"fr": "Année", "ar": "السنة"},
    "y_pib": {"fr": "Masse salariale, en % du PIB",
              "ar": "كتلة الأجور، % من الناتج المحلي الإجمالي"},
    "y_dep": {"fr": "En % des dépenses\ntotales de l'État", "ar": "% من إجمالي\nنفقات الدولة"},
    # légende de la figure A
    "lg_pib": {"fr": "Masse salariale en % du PIB — trait interrompu à chaque changement de "
                     "source ou de base du PIB",
               "ar": "كتلة الأجور كنسبة من الناتج — ينقطع الخطّ عند كلّ تغيير في مصدر الناتج "
                     "أو في سنة أساسه"},
    "lg_retropole": {"fr": "point creux : PIB rétropolé par l'INS",
                     "ar": "نقطة فارغة: ناتج أعاد المعهد الوطني للإحصاء احتسابه"},
    "lg_rupture": {"fr": "trait vertical : rupture de série (infobulle sur le triangle)",
                   "ar": "خطّ عمودي: انقطاع في السلسلة (التفاصيل عند المثلّث)"},
    "lg_bandeau": {"fr": "au-dessus du cadre : base du PIB de chaque segment ; « n. r. » : "
                         "base non précisée par la source",
                   "ar": "فوق الإطار: سنة أساس الناتج لكلّ مقطع؛ «غ. م.»: سنة الأساس غير "
                         "محدَّدة في المصدر"},
    "lg_dep": {"fr": "Masse salariale en % des dépenses totales de l'État — aucun PIB : mesure "
                     "homogène sur toute la période",
               "ar": "كتلة الأجور كنسبة من إجمالي نفقات الدولة — دون ناتج: قياس متجانس على "
                     "كامل الفترة"},
    # bandeau des bases (au-dessus du cadre)
    "b_pib": {"fr": "PIB :", "ar": "الناتج:"},
    "b_base": {"fr": "base {b}", "ar": "أساس {b}"},
    "b_presumee": {"fr": "base {b}\n(présumée)", "ar": "أساس {b}\n(مفترض)"},
    "b_nr": {"fr": "n. r.", "ar": "غ. م."},
    "b_retropolee": {"fr": "base {b}\n(rétropolée par l'INS)",
                     "ar": "أساس {b}\n(أعاد المعهد احتسابه)"},
    "b_retropolee_part": {"fr": "base {b}\n(rétropolée par l'INS pour {a0}-{a1})",
                          "ar": "أساس {b}\n(أعاد المعهد احتسابه لسنوات {a0}-{a1})"},
    # libellés courts des ruptures
    "r_base": {"fr": "{a} : base {x} → {y}\n(niveau du PIB {n})",
               "ar": "{a}: من أساس {x} إلى {y}\n(مستوى الناتج {n})"},
    "r_propre": {"fr": "{a} : PIB propre\nau ministère", "ar": "{a}: ناتج خاصّ\nبالوزارة"},
    "r_retour": {"fr": "{a} : retour à\nla base {b}", "ar": "{a}: عودة إلى\nأساس {b}"},
    # infobulles
    "ib_pib": {"fr": "{a} · masse salariale : {v} % du PIB — PIB : {base} ; {retro}",
               "ar": "{a} · كتلة الأجور: {v} % من الناتج — الناتج: {base}؛ {retro}"},
    "ib_dep": {"fr": "{a} · masse salariale : {v} % des dépenses totales de l'État",
               "ar": "{a} · كتلة الأجور: {v} % من إجمالي نفقات الدولة"},
    "ib_rapporte": {"fr": "{a} · {org} : {v} % du PIB — {base}",
                    "ar": "{a} · {org}: {v} % من الناتج — {base}"},
    # valeurs des colonnes de provenance du PIB
    "v_base": {"fr": "base {b}", "ar": "أساس {b}"},
    "v_presumee": {"fr": "base {b} présumée", "ar": "أساس {b} (مفترض)"},
    "v_nr": {"fr": "base non précisée par la source (valeur propre au ministère des Finances)",
             "ar": "سنة الأساس غير محدَّدة في المصدر (قيمة خاصّة بوزارة المالية)"},
    "v_retro_oui": {"fr": "rétropolé par l'INS", "ar": "أعاد المعهد الوطني للإحصاء احتسابه"},
    "v_retro_non": {"fr": "non rétropolé", "ar": "غير معاد الاحتساب"},
    "v_retro_np": {"fr": "rétropolation non précisée par la source",
                   "ar": "إعادة الاحتساب غير محدَّدة في المصدر"},
    "v_src_minfin": {"fr": "ministère des Finances (PIB déduit du déficit publié en dinars et "
                           "en points de PIB)",
                     "ar": "وزارة المالية (ناتج مستخرج من العجز المنشور بالدينار وبنقاط الناتج)"},
    "v_src_ins": {"fr": "INS", "ar": "المعهد الوطني للإحصاء"},
    "v_publie": {"fr": "publié par l'INS", "ar": "منشور من المعهد الوطني للإحصاء"},
    # colonnes des tables
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_pib": {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "c_base": {"fr": "Base du PIB", "ar": "سنة أساس الناتج"},
    "c_retro": {"fr": "PIB rétropolé ?", "ar": "هل أُعيد احتساب الناتج؟"},
    "c_rupture": {"fr": "Rupture de série", "ar": "انقطاع في السلسلة"},
    "c_src_pib": {"fr": "Source du PIB", "ar": "مصدر الناتج"},
    "c_dep": {"fr": "% des dépenses totales", "ar": "% من إجمالي النفقات"},
    "c_fonc": {"fr": "% des dépenses de fonctionnement", "ar": "% من نفقات التسيير"},
    "c_ms": {"fr": "Masse salariale (MD)", "ar": "كتلة الأجور (م.د)"},
    "c_pib_md": {"fr": "PIB employé (MD)", "ar": "الناتج المعتمد (م.د)"},
    "c_pib_1997": {"fr": "PIB, base 1997 (MD)", "ar": "الناتج، أساس 1997 (م.د)"},
    "c_pib_2015": {"fr": "PIB, base 2015 (MD)", "ar": "الناتج، أساس 2015 (م.د)"},
    "c_rapport": {"fr": "Rapport base 2015 / base 1997", "ar": "نسبة أساس 2015 إلى أساس 1997"},
    "c_ratio_1997": {"fr": "Masse salariale, % du PIB de la base 1997",
                     "ar": "كتلة الأجور، % من ناتج أساس 1997"},
    "c_ratio_2015": {"fr": "Masse salariale, % du PIB de la base 2015",
                     "ar": "كتلة الأجور، % من ناتج أساس 2015"},
    "c_retro_2015": {"fr": "PIB de la base 2015 rétropolé ?",
                     "ar": "هل أُعيد احتساب ناتج أساس 2015؟"},
    "c_rapporte": {"fr": "Ratio rapporté par un rapport extérieur (% du PIB)",
                   "ar": "النسبة الواردة في تقرير خارجي (% من الناتج)"},
    "c_auteur": {"fr": "Auteur du ratio rapporté", "ar": "صاحب النسبة الواردة"},
    "c_base_rapporte": {"fr": "PIB du ratio rapporté", "ar": "ناتج النسبة الواردة"},
    # figure B
    "lg_bloc_budgetaire": {
        "fr": "Budget de l'État rapporté au PIB de l'INS (masse salariale du ministère des "
              "Finances)",
        "ar": "ميزانية الدولة منسوبة إلى ناتج المعهد الوطني للإحصاء (كتلة أجور وزارة المالية)"},
    "lg_bloc_exterieur": {"fr": "Rapports extérieurs (Banque mondiale, FMI) — administration "
                                "centrale",
                          "ar": "التقارير الخارجية (البنك الدولي، صندوق النقد الدولي) — "
                                "الإدارة المركزية"},
    "lg_bloc_reperes": {"fr": "Repères", "ar": "علامات"},
    "lg_b2015": {"fr": "PIB de la base 2015 (INS)", "ar": "ناتج أساس 2015 (المعهد)"},
    "lg_b1997": {"fr": "PIB de la base 1997 (dite « 2010 » par le FMI), publié par l'INS "
                       "jusqu'à 2017",
                 "ar": "ناتج أساس 1997 (المسمّى «2010» لدى صندوق النقد الدولي)، منشور من "
                       "المعهد إلى غاية 2017"},
    "lg_bm": {"fr": "Banque mondiale, revue des dépenses publiques de 2020 : base du PIB non "
                    "précisée ici",
              "ar": "البنك الدولي، مراجعة النفقات العمومية لسنة 2020: سنة أساس الناتج غير "
                    "محدَّدة هنا"},
    "lg_fmi": {"fr": "FMI, rapport de février 2021 : PIB de la base 1997 (dite « 2010 »)",
               "ar": "صندوق النقد الدولي، تقرير فيفري 2021: ناتج أساس 1997 (المسمّى «2010»)"},
    "lg_sans_1997": {"fr": "zone grisée : aucun PIB publié par l'INS en base 1997 après 2017",
                     "ar": "المنطقة الرمادية: لا ناتج منشور من المعهد على أساس 1997 بعد 2017"},
    "org_bm": {"fr": "Banque mondiale", "ar": "البنك الدولي"},
    "org_fmi": {"fr": "FMI", "ar": "صندوق النقد الدولي"},
    "base_bm": {"fr": "base du PIB non précisée ici", "ar": "سنة أساس الناتج غير محدَّدة هنا"},
    "base_fmi": {"fr": "PIB de la base 1997 (dite « 2010 » par le FMI)",
                 "ar": "ناتج أساس 1997 (المسمّى «2010» لدى صندوق النقد الدولي)"},
    "sans_1997": {"fr": "aucun PIB publié\nen base 1997",
                  "ar": "لا ناتج منشور\nعلى أساس 1997"},
}

# Texte complet des ruptures (colonne `rupture`, en français) : équivalents arabes, appliqués
# dans l'ordre ; un morceau sans équivalent reste en français plutôt que d'être deviné.
_RUPTURE_AR = (
    (r"base (\d{4}) → base (\d{4})", r"من أساس \1 إلى أساس \2"),
    (r"rétropolée par l'INS", "أعاد المعهد الوطني للإحصاء احتسابه"),
    (r"valeur propre au ministère", "قيمة خاصّة بالوزارة"),
    (r"rattachée à aucune base", "غير مرتبطة بأيّ أساس"),
    (r"par rapport à la base (\d{4})", r"مقارنة بأساس \1"),
    (r"retour à la base (\d{4})", r"عودة إلى أساس \1"),
    (r"niveau", "المستوى"),
    (r", ", "، "),
)


def _lab(key: str, **valeurs) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"]).format(**valeurs)


def _ft(key: str, **valeurs) -> str:
    return "\n".join(figtools.fig_text(ligne) for ligne in _lab(key, **valeurs).split("\n"))


def _nombre(v: float, dec: int = 2) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _vide(v) -> bool:
    return v is None or v != v


# --- provenance affichée -----------------------------------------------------------------

PROVENANCE_LECTEUR = {
    SERIE: dict(
        sources=["minfin-remunerations", "minfin-indicateurs-fp", "ins-cnat-2015",
                 "ins-pib-base-2015-2010-2020"],
        base_pib="1983 / 1997 / 2015",
        perimetre=("masse salariale = budget de l'État (« Rémunérations publiques »), hors "
                   "entreprises publiques ; PIB aux prix courants : celui de l'INS de 2010 à "
                   "2024, celui du ministère des Finances avant 2010 et en 2025 (déduit du "
                   "déficit publié en dinars et en points de PIB)"),
        caveats=("Le PIB n'est pas d'une seule base : base 1983 jusqu'en 1996 (présumée pour "
                 "1990-1991) ; base 1997 rétropolée par l'INS en 1997-2001 ; valeurs propres au "
                 "ministère des Finances en 2002-2004 et en 2025, dont la source ne précise pas "
                 "la base ; base 1997 en 2005-2009 ; base 2015 de l'INS de 2010 à 2024, "
                 "rétropolée par l'INS pour 2010-2014. Ruptures de série en 1997, 2002, 2005, "
                 "2010 et 2025 : la part du PIB se lit à l'intérieur d'un segment, les bases "
                 "n'étant ni chaînées ni raccordées. La part dans les dépenses de l'État ne "
                 "dépend d'aucune base."),
        perimetre_ar=("كتلة الأجور = ميزانية الدولة («الأجور العمومية»)، باستثناء المنشآت "
                      "العمومية؛ الناتج بالأسعار الجارية: ناتج المعهد الوطني للإحصاء من 2010 "
                      "إلى 2024، وناتج وزارة المالية قبل 2010 وفي 2025 (مستخرج من العجز "
                      "المنشور بالدينار وبنقاط الناتج)"),
        caveats_ar=("الناتج المحلي الإجمالي المعتمد ليس على أساس واحد: أساس 1983 إلى غاية 1996 "
                    "(مفترض لسنتي 1990-1991)؛ أساس 1997 أعاد المعهد الوطني للإحصاء احتسابه في "
                    "1997-2001؛ قيم خاصّة بوزارة المالية في 2002-2004 وفي 2025، لا يحدّد "
                    "المصدر سنة أساسها؛ أساس 1997 في 2005-2009؛ أساس 2015 للمعهد من 2010 إلى "
                    "2024، أعاد المعهد احتسابه لسنوات 2010-2014. انقطاعات في السلسلة في 1997 "
                    "و2002 و2005 و2010 و2025: تُقرأ النسبة إلى الناتج داخل المقطع الواحد، "
                    "والأسس غير موصولة. أمّا الحصّة من نفقات الدولة فلا تتعلّق بأيّ أساس.")),
    SERIE_RECOUVREMENTS: dict(
        sources=["ins-cnat-2015", "ins-pib-base-2015-2010-2020"],
        base_pib="1997 / 2015",
        perimetre=("années où l'INS a publié le PIB aux prix courants à la fois en base 1997 "
                   "et en base 2015 : 2010-2017"),
        caveats=("Écarts observés entre les deux bases, de + 4,89 à + 6,12 % : ils ne sont pas "
                 "constants et ne donnent pas de coefficient de passage pour d'autres années. "
                 "La base 2015 est rétropolée par l'INS pour 2010-2014."),
        perimetre_ar=("السنوات التي نشر فيها المعهد الوطني للإحصاء الناتج بالأسعار الجارية "
                      "على أساس 1997 وعلى أساس 2015 معًا: 2010-2017"),
        caveats_ar=("فوارق ملاحظة بين الأساسين، من + 4,89 إلى + 6,12 %: غير ثابتة، ولا "
                    "يُستخرج منها معامل انتقال لسنوات أخرى. أساس 2015 أعاد المعهد احتسابه "
                    "لسنوات 2010-2014.")),
    SERIE_RECONCILIATION: dict(
        titre=("Masse salariale / PIB : ratios rapportés par le FMI et la Banque mondiale, "
               "base 2015 et base 1997 (dite « 2010 » par le FMI)"),
        titre_ar=("كتلة الأجور / الناتج المحلي الإجمالي: النسب الواردة في تقارير صندوق النقد "
                  "الدولي والبنك الدولي، أساس 2015 وأساس 1997 (المسمّى «2010» لدى صندوق النقد "
                  "الدولي)"),
        base_pib="1997 / 2015",
        caveats=("Le PIB « aux prix de 2010 » du FMI est, pour ses niveaux aux prix courants, "
                 "celui de la base 1997 de l'INS : il n'existe pas de PIB aux prix courants "
                 "« en base 2010 ». La base du PIB employé par la Banque mondiale n'est pas "
                 "précisée ici. L'INS n'a publié aucun PIB en base 1997 après 2017."),
        caveats_ar=("الناتج «بأسعار 2010» لدى صندوق النقد الدولي هو، من حيث مستوياته بالأسعار "
                    "الجارية، ناتج أساس 1997 للمعهد الوطني للإحصاء: لا يوجد ناتج بالأسعار "
                    "الجارية «على أساس 2010». سنة أساس الناتج المعتمد لدى البنك الدولي غير "
                    "محدَّدة هنا. لم ينشر المعهد أيّ ناتج على أساس 1997 بعد 2017.")),
}


def _declarer() -> None:
    """Remplace, pour l'affichage, le périmètre et les réserves du catalogue de l'entrepôt."""
    for sid, champs in PROVENANCE_LECTEUR.items():
        if sid in figtools._DECLAREES:
            continue
        origine = {k: v for k, v in figtools.meta(sid).items() if k != "id"}
        figtools.register_provenance(sid, **{**origine, **champs})


_declarer()


# --- lecture des séries ------------------------------------------------------------------

def _ratios():
    return figtools.series(SERIE).sort_values("annee").reset_index(drop=True)


def _base(v) -> tuple[str, str | None]:
    """(genre, année de base) d'une valeur de `base_pib` : « base », « presumee » ou « nr »."""
    s = str(v)
    m = re.match(r"base (\d{4})", s)
    if not m:
        return "nr", None
    return ("presumee" if "présumée" in s else "base"), m.group(1)


def _base_lisible(v) -> str:
    genre, b = _base(v)
    return _lab("v_" + genre, b=b) if b else _lab("v_nr")


def _retro_lisible(v) -> str:
    s = str(v)
    return _lab("v_retro_oui" if s == "oui" else "v_retro_non" if s == "non" else "v_retro_np")


def _source_pib_lisible(v) -> str:
    s = str(v)
    if s.startswith("pib-minfin"):
        return _lab("v_src_minfin")
    m = re.search(r"\(INS, (.*)\)", s)
    if m and figtools.lang() == "fr":
        return f"{_lab('v_src_ins')}, {m.group(1)}"
    return _lab("v_src_ins")


def _rupture_lisible(v):
    """Texte complet d'une rupture, dans la langue du livre."""
    if _vide(v):
        return None
    t = str(v)
    if figtools.lang() == "ar":
        for motif, remplacement in _RUPTURE_AR:
            t = re.sub(motif, remplacement, t)
    return t


def _rupture_courte(annee: int, texte: str) -> str:
    """Libellé court d'une rupture, tiré du texte de la colonne `rupture`."""
    m = re.match(r"base (\d{4}) → base (\d{4}).*\(niveau ([^)]*)\)", texte)
    if m:
        return _ft("r_base", a=annee, x=m.group(1), y=m.group(2), n=m.group(3))
    m = re.match(r"retour à la base (\d{4})", texte)
    if m:
        return _ft("r_retour", a=annee, b=m.group(1))
    return _ft("r_propre", a=annee)


# --- éléments de tracé communs -----------------------------------------------------------

def _cadre(ax, x0: int, x1: int) -> None:
    ax.set_xlim(x0 - 0.8, x1 + 0.8)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=14))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=7, steps=[1, 2, 5, 10]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)


def _repere(ax, annee: int, texte: str) -> None:
    """Petit triangle en haut du trait de rupture, porteur de l'infobulle."""
    p, = ax.plot([annee - 0.5], [1], marker=7, ms=6, color=GRIS, clip_on=False, zorder=4,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, texte)


def _marque_ruptures(ax, d, x1: int) -> None:
    """Un trait vertical par rupture lue dans les données, son libellé court en haut du cadre
    (hauteurs alternées, à gauche du trait en fin de période), le texte complet en infobulle."""
    niveau = 0
    for r in d[d["rupture"].notna()].itertuples(index=False):
        a = int(r.annee)
        figtools.marque_rupture(ax, a)
        gauche = a >= x1 - 2
        ax.annotate(_rupture_courte(a, str(r.rupture)), xy=(a - 0.5, 1),
                    xycoords=("data", "axes fraction"),
                    xytext=(-4 if gauche else 4, -(4 + 24 * (niveau % 2))),
                    textcoords="offset points", ha="right" if gauche else "left", va="top",
                    fontsize=7, color=GRIS, zorder=5,
                    bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1))
        niveau += 1
        _repere(ax, a, f"{a} · {_rupture_lisible(r.rupture)}")


def _bandeau_bases(ax, d) -> None:
    """Au-dessus du cadre : la base du PIB de chaque segment, et ce qui y est rétropolé."""
    for _, g in d.groupby("segment_pib", sort=False):
        annees = g["annee"].astype(int)
        genre, b = _base(g["base_pib"].iloc[0])
        retro = sorted(annees[g["pib_retropole"] == "oui"])
        if genre == "nr":
            texte = _ft("b_nr")
        elif genre == "presumee":
            texte = _ft("b_presumee", b=b)
        elif retro and len(retro) == len(g):
            texte = _ft("b_retropolee", b=b)
        elif retro:
            texte = _ft("b_retropolee_part", b=b, a0=retro[0], a1=retro[-1])
        else:
            texte = _ft("b_base", b=b)
        ax.annotate(texte, xy=((annees.min() + annees.max()) / 2, 1),
                    xycoords=("data", "axes fraction"), xytext=(0, 5),
                    textcoords="offset points", ha="center", va="bottom", fontsize=6.5,
                    color=GRIS, annotation_clip=False)
    ax.annotate(_ft("b_pib"), xy=(0, 1), xycoords="axes fraction", xytext=(-6, 5),
                textcoords="offset points", ha="right", va="bottom", fontsize=6.5, color=GRIS,
                annotation_clip=False)


def _trace_part_pib(ax, d, colonne: str, couleur: str, marque: str = "o") -> None:
    """La part du PIB, segment par segment ; un point par année, creux si le PIB est rétropolé."""
    for _, g in d.groupby("segment_pib", sort=False):
        ax.plot(g["annee"], g[colonne], "-", color=couleur, lw=2, zorder=2)
    for r in d.itertuples(index=False):
        v = getattr(r, colonne)
        p, = ax.plot([int(r.annee)], [v], marque, ms=4.5, color=couleur, zorder=3,
                     mfc="white" if r.pib_retropole == "oui" else couleur)
        figtools.infobulle(p, _lab("ib_pib", a=int(r.annee), v=_nombre(v),
                                   base=_base_lisible(r.base_pib),
                                   retro=_retro_lisible(r.pib_retropole)))


def _poignee(cle: str, **style) -> Line2D:
    return Line2D([], [], label=figtools.fig_text(_lab(cle)), **style)


# --- figure A : parts du PIB et des dépenses de l'État, 1990-2025 ------------------------

def fig_A():
    """Haut : la part du PIB, par segments de base. Bas : la part des dépenses de l'État."""
    figtools.apply_lang_font()
    d = _ratios()
    x0, x1 = int(d["annee"].min()), int(d["annee"].max())
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 7.2), sharex=True,
                                 gridspec_kw=dict(height_ratios=[1.5, 1], hspace=0.1))
    _trace_part_pib(ax, d, "ms_sur_pib_pct", BLEU)
    _cadre(ax, x0, x1)
    ax.set_ylabel(_ft("y_pib"))
    bas, haut = d["ms_sur_pib_pct"].min(), d["ms_sur_pib_pct"].max()
    ax.set_ylim(bas - 0.8, haut + 0.42 * (haut - bas))  # marge du haut : libellés de rupture
    _marque_ruptures(ax, d, x1)
    _bandeau_bases(ax, d)

    bx.plot(d["annee"], d["ms_sur_depenses_totales_pct"], "-", color=ROUGE, lw=1.8, zorder=2)
    for r in d.itertuples(index=False):
        p, = bx.plot([int(r.annee)], [r.ms_sur_depenses_totales_pct], "s", ms=3.5, color=ROUGE,
                     zorder=3)
        figtools.infobulle(p, _lab("ib_dep", a=int(r.annee),
                                   v=_nombre(r.ms_sur_depenses_totales_pct)))
    _cadre(bx, x0, x1)
    bx.set_ylabel(_ft("y_dep"))
    bx.set_xlabel(figtools.fig_text(_lab("x")))

    poignees = [
        _poignee("lg_pib", color=BLEU, marker="o", lw=2, ms=4.5),
        _poignee("lg_retropole", color=BLEU, marker="o", mfc="white", ls="none", ms=4.5),
        _poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5),
        _poignee("lg_bandeau", color="none"),
        _poignee("lg_dep", color=ROUGE, marker="s", lw=1.8, ms=3.5),
    ]
    bx.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.24), ncol=1,
              fontsize=7.5, frameon=False)
    fig.align_ylabels([ax, bx])
    return fig


def ratios_table():
    """Tableau (onglet Données) : les parts, et pour le PIB sa base, sa source, sa rupture."""
    import pandas as pd

    d = _ratios()
    return pd.DataFrame({
        _lab("c_annee"): d["annee"],
        _lab("c_pib"): d["ms_sur_pib_pct"],
        _lab("c_base"): d["base_pib"].map(_base_lisible),
        _lab("c_retro"): d["pib_retropole"].map(_retro_lisible),
        _lab("c_rupture"): d["rupture"].map(_rupture_lisible),
        _lab("c_dep"): d["ms_sur_depenses_totales_pct"],
        _lab("c_fonc"): d["ms_sur_depenses_fonctionnement_pct"],
        _lab("c_ms"): d["masse_salariale_MDT"],
        _lab("c_pib_md"): d["pib_nominal_MDT"],
        _lab("c_src_pib"): d["source_pib"].map(_source_pib_lisible),
    })


# --- figure B : la même masse salariale rapportée au PIB de chaque base ------------------

# Auteur d'un ratio rapporté, reconnu dans le libellé de la série ; un ratio d'un autre auteur
# (ministère, presse) n'est pas un rapport extérieur et n'est ni tracé ni affiché.
_AUTEURS = (("BM", "bm"), ("FMI", "fmi"))


def _rapportes() -> dict[int, tuple[float, str]]:
    """{année: (ratio, auteur)} des ratios du FMI et de la Banque mondiale."""
    out = {}
    for r in figtools.series(SERIE_RECONCILIATION).itertuples(index=False):
        m = re.match(r"\s*(\d+(?:,\d+)?)\s*%\s*\((.*)\)", str(r.ratio_rapporte_FMI_BM))
        if not m:
            continue
        for sigle, auteur in _AUTEURS:
            if sigle in m.group(2):
                out[int(r.annee)] = (float(m.group(1).replace(",", ".")), auteur)
    return out


def _deux_bases():
    """Une ligne par année, 2010-2020 : masse salariale, PIB et ratio dans chaque base.

    Le PIB de la base 1997 n'existe que pour les années où l'INS l'a publié (2010-2017) ; aucune
    valeur n'est calculée au-delà par un coefficient."""
    d = _ratios()
    d = d[d["base_pib"].astype(str).str.startswith("base 2015") & (d["annee"] <= FIN_FIGURE_B)]
    r = figtools.series(SERIE_RECOUVREMENTS)
    r = r[(r["base_ancienne"] == "base 1997") & (r["base_nouvelle"] == "base 2015")]
    r = r.set_index("annee")
    d = d.assign(
        pib_base1997_MD=d["annee"].map(r["pib_base_ancienne_MD"]),
        rapport=d["annee"].map(r["rapport"]),
    )
    d["ms_sur_pib_base1997_pct"] = (100 * d["masse_salariale_MDT"] / d["pib_base1997_MD"]).round(2)
    rapportes = _rapportes()
    d["ratio_rapporte_pct"] = d["annee"].map(lambda a: rapportes.get(int(a), (None, None))[0])
    d["auteur_rapporte"] = d["annee"].map(lambda a: rapportes.get(int(a), (None, None))[1])
    return d.reset_index(drop=True)


def fig_B():
    figtools.apply_lang_font()
    d = _deux_bases()
    x0, x1 = int(d["annee"].min()), int(d["annee"].max())
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    _trace_part_pib(ax, d, "ms_sur_pib_pct", BLEU)
    b = d[d["ms_sur_pib_base1997_pct"].notna()]
    ax.plot(b["annee"], b["ms_sur_pib_base1997_pct"], "-", color=VIOLET, lw=2, zorder=2)
    for r in b.itertuples(index=False):
        p, = ax.plot([int(r.annee)], [r.ms_sur_pib_base1997_pct], "s", ms=4.5, color=VIOLET,
                     zorder=3)
        figtools.infobulle(p, _lab("ib_pib", a=int(r.annee),
                                   v=_nombre(r.ms_sur_pib_base1997_pct),
                                   base=_lab("v_base", b="1997"), retro=_lab("v_publie")))
    marques = {"bm": "P", "fmi": "X"}
    for r in d[d["ratio_rapporte_pct"].notna()].itertuples(index=False):
        p, = ax.plot([int(r.annee)], [r.ratio_rapporte_pct], marques[r.auteur_rapporte], ms=9,
                     color=ROUGE, zorder=4)
        figtools.infobulle(p, _lab("ib_rapporte", a=int(r.annee),
                                   org=_lab("org_" + r.auteur_rapporte),
                                   v=_nombre(r.ratio_rapporte_pct, 1),
                                   base=_lab("base_" + r.auteur_rapporte)))
    _cadre(ax, x0, x1)
    ax.set_xticks(range(x0, x1 + 1))
    ax.set_ylim(top=ax.get_ylim()[1] + 0.5)  # la marque la plus haute ne touche pas le cadre
    ax.set_ylabel(_ft("y_pib"))
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    fin_1997 = int(b["annee"].max())
    if fin_1997 < x1:
        ax.axvspan(fin_1997 + 0.5, x1 + 0.8, color=GRIS, alpha=0.08, lw=0, zorder=0)
        ax.annotate(_ft("sans_1997"), xy=(fin_1997 + 0.5, 0), xycoords=("data", "axes fraction"),
                    xytext=(5, 5), textcoords="offset points", ha="left", va="bottom",
                    fontsize=7, color=GRIS)
    # Légende en blocs titrés : budgétaire, rapports extérieurs, repères.
    poignees: list = []
    titres = []

    def titre(cle):
        titres.append(len(poignees))
        poignees.append(_poignee(cle, color="none"))

    titre("lg_bloc_budgetaire")
    poignees.append(_poignee("lg_b2015", color=BLEU, marker="o", lw=2, ms=4.5))
    poignees.append(_poignee("lg_b1997", color=VIOLET, marker="s", lw=2, ms=4.5))
    auteurs = list(dict.fromkeys(d["auteur_rapporte"].dropna()))
    if auteurs:
        titre("lg_bloc_exterieur")
        for a in auteurs:
            poignees.append(_poignee("lg_" + a, color=ROUGE, marker=marques[a], ls="none", ms=8))
    titre("lg_bloc_reperes")
    poignees.append(_poignee("lg_retropole", color=BLEU, marker="o", mfc="white", ls="none",
                             ms=4.5))
    if fin_1997 < x1:
        poignees.append(_poignee("lg_sans_1997", color=GRIS, alpha=0.3, lw=6))
    legende = ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, 0),
                        borderaxespad=4.2, ncol=1, fontsize=7.2, frameon=False)
    for i in titres:
        legende.get_texts()[i].set_fontweight("bold")
    fig.tight_layout()
    return fig


def reconciliation_table():
    """Tableau (onglet Données) de la figure B : les deux PIB, les deux ratios, le rapport
    observé entre les bases, et les ratios des rapports extérieurs."""
    import pandas as pd

    d = _deux_bases()
    auteur = d["auteur_rapporte"]
    return pd.DataFrame({
        _lab("c_annee"): d["annee"],
        _lab("c_ms"): d["masse_salariale_MDT"],
        _lab("c_pib_2015"): d["pib_nominal_MDT"],
        _lab("c_retro_2015"): d["pib_retropole"].map(_retro_lisible),
        _lab("c_ratio_2015"): d["ms_sur_pib_pct"],
        _lab("c_pib_1997"): d["pib_base1997_MD"],
        _lab("c_ratio_1997"): d["ms_sur_pib_base1997_pct"],
        _lab("c_rapport"): d["rapport"],
        _lab("c_rapporte"): d["ratio_rapporte_pct"],
        _lab("c_auteur"): auteur.map(lambda a: None if _vide(a) else _lab("org_" + a)),
        _lab("c_base_rapporte"): auteur.map(lambda a: None if _vide(a) else _lab("base_" + a)),
    })


def figure_B(caption: str, note_lecture: str | None = None, generated: str | None = None,
             slug: str = "fig_masse_salariale_reconciliation") -> None:
    """Émet la figure B en onglets. À appeler dans un chunk `#| label: fig-…`, `#| output: asis`.

    Le temps de l'appel, la ligne « Source » ne nomme que les deux bases que la figure trace
    (1997 et 2015) : la série longue, lue ici pour 2010-2020 seulement, en annonce trois."""
    avant = {sid: figtools._DECLAREES[sid] for sid in SERIES_B}
    try:
        for sid in SERIES_B:
            champs = {k: v for k, v in avant[sid].items() if k not in ("id", "base_pib")}
            if sid == SERIE:
                champs["base_pib"] = "1997 / 2015"
            figtools.register_provenance(sid, **champs)
        figtools.figure_tabs(fig_B(), reconciliation_table(), *SERIES_B, slug=slug,
                             caption=caption, note_lecture=note_lecture, generated=generated)
    finally:
        figtools._DECLAREES.update(avant)
