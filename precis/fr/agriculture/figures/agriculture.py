"""Figures du livre « L'agriculture — le soutien au producteur ».

D'OÙ VIENNENT LES DONNÉES. Les séries sont de petites séries déjà sourcées dans les
chapitres (agridata.tn, états financiers CTAMA au CMF, rapports sur les fonds spéciaux du
ministère des Finances, rapports d'activité de l'APIA, lois de finances). Elles ne sont pas
publiées comme séries de l'entrepôt `tunisia-data` : leur provenance est donc **déclarée
localement** par `figtools.register_provenance` (mêmes champs que le catalogue de
l'entrepôt), et leurs valeurs — déjà établies et citées — sont portées ici, inline. Chaque
valeur est celle du tableau correspondant du chapitre ; la clé de citation renvoie à la
source primaire.

PARTS DES DÉPENSES DE L'ÉTAT ET DU PIB. Les figures de montants publics (budget, exécution,
encouragements, primes APIA, fonds de calamités) ont trois vues : millions de dinars, part
des dépenses de l'État, part du PIB. Les dénominateurs sont lus dans la série
`denominateurs-depenses-etat-pib` de `tunisia-data` (dépenses de l'État **réalisées** hors
service de la dette, ministère des Finances ; PIB retenu avec sa base) — les mêmes que les
volumes fiscalité et compensation. Règles (docs/conventions-redaction.md) : la part du PIB
se trace **par segment de base**, chaque changement de base est un trait de rupture et la
base de chaque segment est écrite au-dessus du cadre ; aucun PIB n'est chaîné. Une
prévision de loi de finances rapportée à des dépenses réalisées donne un ordre de grandeur.
Les primes CTAMA (assureur mutuel) et le prix de l'eau ne sont pas des dépenses de l'État :
leurs figures restent en valeur.

Appel depuis un chunk Quarto `#| output: asis` étiqueté `#| label: fig-…` :

    import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")
    from figures import agriculture as ag
    ag.fig_eau_secadenord(caption="…", note_lecture="…")
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

BLEU, BLEU_CLAIR, ORANGE, GRIS = "#08519c", "#9ecae1", "#bc4c00", "#6e7781"


def _nombre(v: float, dec: int = 0) -> str:
    """Nombre à la française : virgule décimale, espace insécable pour les milliers."""
    if v is None:
        return ""
    texte = f"{v:,.{dec}f}"
    return texte.replace(",", "\N{NO-BREAK SPACE}").replace(".", ",")


def _lab(d: dict) -> str:
    return d.get(figtools.lang(), d["fr"])


# =========================================================================================
# Eau d'irrigation : prix de gros SECADENORD, médiane et fourchette, 2014-2025
# =========================================================================================
SERIE_EAU = "agri-eau-secadenord-tarif"

figtools.register_provenance(
    SERIE_EAU,
    titre=("Prix de vente de l'eau en gros par la SECADENORD aux gestionnaires régionaux : "
           "médiane et fourchette sur les points de livraison, 2014-2025"),
    titre_ar=("سعر بيع الماء بالجملة من قبل الشركة الوطنية لاستغلال وتوزيع المياه بالشمال "
              "للمتصرّفين الجهويّين: الوسيط والمجال، 2014-2025"),
    sources=["secadenordTarif2025"],
    unite="millime par m³",
    unite_ar="مليم للمتر المكعّب",
    perimetre=("prix de gros facturé par la SECADENORD à chaque commissariat régional au "
               "développement agricole et à la SONEDE, avant distribution à l'exploitant ; "
               "médiane, minimum et maximum calculés chaque année sur les 21 à 22 points de "
               "livraison suivis"),
    perimetre_ar=("سعر الجملة المحتسب من قبل الشركة لكلّ مندوبية جهوية للتنمية الفلاحية "
                  "وللشركة الوطنية لاستغلال وتوزيع المياه، قبل التوزيع على المستغلّ"),
    caveats=("Le prix de gros n'est pas le tarif facturé à l'agriculteur ; il en donne le "
             "plancher de coût. Les années 2014 à 2021 portent le même barème."),
    caveats_ar=("سعر الجملة ليس التعريفة المحتسبة على الفلاح؛ فهو يمثّل الحدّ الأدنى للكلفة. "
                "السنوات 2014 إلى 2021 تحمل نفس التعريفة."),
)

# annee : (médiane, minimum, maximum) en millime/m³, calculés sur les points de livraison.
_EAU = {
    2014: (54.4, 21.4, 110.4), 2015: (54.4, 21.4, 110.4), 2016: (54.4, 21.4, 110.4),
    2017: (54.4, 21.4, 110.4), 2018: (54.4, 21.4, 110.4), 2019: (54.4, 21.4, 110.4),
    2020: (54.4, 21.4, 110.4), 2021: (54.4, 21.4, 110.4),
    2022: (69.4, 36.4, 125.4), 2023: (65.3, 31.4, 120.4),
    2024: (74.4, 41.4, 130.4), 2025: (79.4, 46.4, 135.4),
}

_L_EAU = {
    "y": {"fr": "Prix de gros (millime/m³)", "ar": "سعر الجملة (مليم/م³)"},
    "med": {"fr": "Médiane", "ar": "الوسيط"},
    "band": {"fr": "Fourchette selon la zone (min–max)",
             "ar": "المجال حسب المنطقة (أدنى–أقصى)"},
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_med": {"fr": "Médiane (millime/m³)", "ar": "الوسيط (مليم/م³)"},
    "c_min": {"fr": "Minimum (millime/m³)", "ar": "الأدنى (مليم/م³)"},
    "c_max": {"fr": "Maximum (millime/m³)", "ar": "الأقصى (مليم/م³)"},
}


def _fig_eau():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    annees = sorted(_EAU)
    med = [_EAU[a][0] for a in annees]
    lo = [_EAU[a][1] for a in annees]
    hi = [_EAU[a][2] for a in annees]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.fill_between(annees, lo, hi, color=BLEU_CLAIR, alpha=0.5,
                    label=ft(_lab(_L_EAU["band"])))
    ax.plot(annees, med, color=BLEU, lw=2.2, marker="o", ms=4,
            label=ft(_lab(_L_EAU["med"])))
    figtools.marque_rupture(ax, 2022)
    ax.set_ylabel(ft(_lab(_L_EAU["y"])))
    ax.set_xticks(annees)
    ax.set_xticklabels([str(a) for a in annees], rotation=45, fontsize=8)
    ax.set_ylim(0, 145)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def _table_eau():
    import pandas as pd
    annees = sorted(_EAU)
    return pd.DataFrame({
        _lab(_L_EAU["c_annee"]): annees,
        _lab(_L_EAU["c_med"]): [_EAU[a][0] for a in annees],
        _lab(_L_EAU["c_min"]): [_EAU[a][1] for a in annees],
        _lab(_L_EAU["c_max"]): [_EAU[a][2] for a in annees],
    })


def fig_eau_secadenord(caption: str, note_lecture: str | None = None,
                       generated: str | None = None) -> None:
    figtools.figure_tabs(
        _fig_eau(), _table_eau(), SERIE_EAU,
        slug="fig_agri_eau_secadenord", caption=caption, note_lecture=note_lecture,
        nominal=False, generated=generated)


# =========================================================================================
# Helpers génériques pour les figures en lignes (une ou plusieurs séries annuelles)
# =========================================================================================
def _fig_lignes(courbes, ylabel, ymax=None, ruptures=()):
    """courbes : [(label, {annee: valeur}, couleur, marker)]. Trace des lignes annuelles."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(8, 5))
    toutes = sorted({a for _, d, _, _ in courbes for a in d})
    for label, d, couleur, marker in courbes:
        xs = sorted(d)
        ys = [d[a] for a in xs]
        ax.plot(xs, ys, color=couleur, lw=2.2, marker=marker, ms=5, label=ft(_lab(label) if isinstance(label, dict) else label))
    for an in ruptures:
        figtools.marque_rupture(ax, an)
    ax.set_ylabel(ft(_lab(ylabel) if isinstance(ylabel, dict) else ylabel))
    ax.set_xticks(toutes)
    ax.set_xticklabels([str(a) for a in toutes], rotation=45, fontsize=8)
    if ymax:
        ax.set_ylim(0, ymax)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def _table_wide(annees, colonnes):
    """colonnes : [(libellé, {annee: valeur})]. Table large annee × grandeurs."""
    import pandas as pd
    out = {_lab({"fr": "Année", "ar": "السنة"}): list(annees)}
    for lib, d in colonnes:
        out[_lab(lib)] = [d.get(a) for a in annees]
    return pd.DataFrame(out)


# =========================================================================================
# Parts des dépenses de l'État et du PIB : trois vues par figure de montants publics
# =========================================================================================
SERIE_DEN = "denominateurs-depenses-etat-pib"
MESURES = ("md", "dep", "pib")

_L_PART = {
    "vue_md": {"fr": "En millions de dinars", "ar": "بملايين الدنانير"},
    "vue_dep": {"fr": "En % des dépenses de l'État", "ar": "بنسبة مئوية من نفقات الدولة"},
    "vue_pib": {"fr": "En % du PIB", "ar": "بنسبة مئوية من الناتج المحلي الإجمالي"},
    "y_dep": {"fr": "En % des dépenses de l'État\nhors service de la dette",
              "ar": "٪ من نفقات الدولة\nدون خدمة الدين"},
    "y_pib": {"fr": "En % du PIB", "ar": "٪ من الناتج المحلي الإجمالي"},
    "c_dep": {"fr": "% dépenses de l'État", "ar": "٪ نفقات الدولة"},
    "c_pib": {"fr": "% PIB", "ar": "٪ الناتج"},
    "c_den_dep": {"fr": "Dépenses de l'État hors dette (MD)", "ar": "نفقات الدولة دون الدين (م.د)"},
    "c_den_pib": {"fr": "PIB (MD)", "ar": "الناتج المحلي الإجمالي (م.د)"},
    "c_base": {"fr": "Base du PIB", "ar": "أساس الناتج"},
    "pib": {"fr": "PIB :", "ar": "الناتج:"},
    "base": {"fr": "base {b}", "ar": "أساس {b}"},
    "retro": {"fr": "rétropolée {a0}-{a1}", "ar": "معاد احتسابها {a0}-{a1}"},
    "nr": {"fr": "n. r.", "ar": "غير مرتبط"},
    "leg_base": {"fr": "au-dessus du cadre : base du PIB de chaque segment",
                 "ar": "فوق الإطار: أساس الناتج لكلّ مقطع"},
    "leg_nr": {"fr": "« n. r. » : valeur propre au ministère des Finances,\nrattachée à aucune base",
               "ar": "«غير مرتبط»: قيمة خاصّة بوزارة المالية،\nغير مرتبطة بأيّ أساس"},
}


def _den():
    return figtools.series(SERIE_DEN).set_index("annee")


def _en_mesure(d: dict, mesure: str) -> dict:
    """{annee: MD} → {annee: valeur dans la mesure} (MD, % dépenses de l'État, % PIB)."""
    if mesure == "md":
        return dict(d)
    den = _den()
    col = "depenses_etat_hors_dette_MDT" if mesure == "dep" else "pib_MDT"
    return {a: 100 * v / den.loc[a, col] for a, v in d.items()
            if a in den.index and den.loc[a, col] == den.loc[a, col]}


def _segment(a: int) -> str:
    return str(_den().loc[a, "segment_pib"])


def _morceaux(xs, mesure: str):
    """Suites d'années consécutives ; en % du PIB, coupées à chaque changement de base."""
    courant: list = []
    for a in xs:
        if courant and not (a == courant[-1] + 1
                            and (mesure != "pib" or _segment(a) == _segment(courant[-1]))):
            yield courant
            courant = []
        courant.append(a)
    if courant:
        yield courant


def _bases_du_pib(ax, annees) -> None:
    """Trait à chaque changement de base du PIB, base de chaque segment au-dessus du cadre."""
    import re
    den = _den().loc[min(annees):max(annees)]
    segments: list[list] = []
    for a, r in den.iterrows():
        if segments and segments[-1][2] == r["segment_pib"]:
            segments[-1][1] = a
        else:
            segments.append([a, a, r["segment_pib"]])
    ft = figtools.fig_text
    for i, (a0, a1, segment) in enumerate(segments):
        if i:
            trait = figtools.marque_rupture(ax, a0)
            rupture = den.loc[a0, "rupture_pib"]
            if isinstance(rupture, str) and rupture:
                figtools.infobulle(trait, f"{a0} · PIB : {rupture}")
        m = re.search(r"\((.*)\)", str(segment))
        base = m.group(1) if m else str(segment)
        if base.startswith("non rattach"):
            texte = _lab(_L_PART["nr"])
        else:
            texte = _lab(_L_PART["base"]).format(b=base.replace("base ", ""))
        retro = den.loc[a0:a1]
        retro = sorted(retro[retro["pib_retropole"] == "oui"].index)
        if retro:
            texte += "\n" + _lab(_L_PART["retro"]).format(a0=retro[0], a1=retro[-1])
        ax.annotate(ft(texte), xy=((a0 + a1) / 2, 1), xycoords=("data", "axes fraction"),
                    xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                    fontsize=6.5, color=GRIS, annotation_clip=False)
    ax.annotate(ft(_lab(_L_PART["pib"])), xy=(0, 1), xycoords="axes fraction", xytext=(-6, 5),
                textcoords="offset points", ha="right", va="bottom", fontsize=6.5, color=GRIS,
                annotation_clip=False)


def _ylabel(ylabel_md: dict, mesure: str) -> dict:
    return ylabel_md if mesure == "md" else _L_PART[f"y_{mesure}"]


def _legende(ax, mesure: str, annees=()) -> None:
    from matplotlib.lines import Line2D
    poignees, libelles = ax.get_legend_handles_labels()
    if mesure == "pib":
        texte = _lab(_L_PART["leg_base"])
        if any(_segment(a).find("non rattach") >= 0 for a in annees):
            texte += " ;\n" + _lab(_L_PART["leg_nr"])
        poignees.append(Line2D([], [], color="none"))
        libelles.append("\n".join(figtools.fig_text(ligne) for ligne in texte.split("\n")))
    ax.legend(poignees, libelles, loc="upper left", fontsize=8, frameon=False)


def _vues(trace) -> list:
    """trace(mesure) → figure ; rend les trois vues [(titre, figure)]."""
    return [(_lab(_L_PART[f"vue_{m}"]), trace(m)) for m in MESURES]


def _table_parts(annees, colonnes):
    """Table large : pour chaque grandeur, MD, % dépenses de l'État, % PIB ; puis dénominateurs."""
    import pandas as pd
    den = _den()
    out = {_lab({"fr": "Année", "ar": "السنة"}): list(annees)}
    for lib, d in colonnes:
        dep, pib = _en_mesure(d, "dep"), _en_mesure(d, "pib")
        out[_lab(lib)] = [d.get(a) for a in annees]
        nom = _lab(lib).replace(" (MD)", "").replace(" (م.د)", "")
        out[f"{nom}, {_lab(_L_PART['c_dep'])}"] = [
            round(dep[a], 3) if a in dep else None for a in annees]
        out[f"{nom}, {_lab(_L_PART['c_pib'])}"] = [
            round(pib[a], 3) if a in pib else None for a in annees]
    out[_lab(_L_PART["c_den_dep"])] = [den.loc[a, "depenses_etat_hors_dette_MDT"] for a in annees]
    out[_lab(_L_PART["c_den_pib"])] = [den.loc[a, "pib_MDT"] for a in annees]
    out[_lab(_L_PART["c_base"])] = [den.loc[a, "segment_pib"] for a in annees]
    return pd.DataFrame(out)


def _fig_lignes_mesure(courbes, ylabel_md, mesure, ymax=None, ruptures=()):
    """Comme `_fig_lignes`, dans la mesure voulue ; en % du PIB, segments par base."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(8, 5.2))
    toutes = sorted({a for _, d, _, _ in courbes for a in d})
    for label, d, couleur, marker in courbes:
        v = _en_mesure(d, mesure)
        xs = sorted(v)
        premier = True
        for morceau in _morceaux(xs, mesure):
            ax.plot(morceau, [v[a] for a in morceau], color=couleur, lw=2.2, marker=marker,
                    ms=5, label=ft(_lab(label)) if premier else None)
            premier = False
    for an in ruptures:
        figtools.marque_rupture(ax, an)
    if mesure == "pib":
        _bases_du_pib(ax, toutes)
    ax.set_ylabel(ft(_lab(_ylabel(ylabel_md, mesure))))
    ax.set_xticks(toutes)
    ax.set_xticklabels([str(a) for a in toutes], rotation=45, fontsize=8)
    ax.set_xlim(min(toutes) - 0.7, max(toutes) + 0.7)
    if mesure == "md" and ymax:
        ax.set_ylim(0, ymax)
    else:
        ax.set_ylim(0, ax.get_ylim()[1] * 1.25)   # place pour la légende
    ax.grid(True, axis="y", alpha=0.3)
    _legende(ax, mesure, toutes)
    fig.tight_layout()
    return fig


# =========================================================================================
# Budget de la mission Agriculture, 2020-2025 (prévision, million de dinars)
# =========================================================================================
SERIE_BUDGET = "agri-budget-mission"
figtools.register_provenance(
    SERIE_BUDGET,
    titre="Budget de la mission Agriculture, crédits de paiement sur ressources de l'État, 2020-2025",
    titre_ar="ميزانية مهمة الفلاحة، اعتمادات الدفع على موارد الدولة، 2020-2025",
    sources=["tn-pap-agriculture-2020", "tn-pap-agriculture-2021", "tn-pap-agriculture-2022",
             "tn-pap-agriculture-2024", "tn-pap-agriculture-2025"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("crédits de paiement de la mission, sur ressources de l'État, hors ressources "
               "propres des établissements ; montant de la loi de finances initiale de chaque année"),
    perimetre_ar="اعتمادات الدفع للمهمة على موارد الدولة، دون الموارد الذاتية للمؤسسات",
    caveats="Dinars courants. Nomenclature budget-programme stable depuis 2020.",
    caveats_ar="بالدينار الجاري. تبويب الميزانية حسب البرامج قارّ منذ 2020.",
)
_BUDGET = {2020: 1726.9, 2021: 1780.0, 2022: 1850.0, 2023: 1965.0, 2024: 2202.1, 2025: 2279.1}


def fig_budget_mission(caption, note_lecture=None, generated=None):
    courbes = [({"fr": "Budget de la mission", "ar": "ميزانية المهمة"}, _BUDGET, BLEU, "o")]
    ylabel = {"fr": "Crédits de paiement (millions de dinars)", "ar": "اعتمادات الدفع (مليون دينار)"}
    vues = _vues(lambda m: _fig_lignes_mesure(courbes, ylabel, m, ymax=2500))
    df = _table_parts(sorted(_BUDGET),
                      [({"fr": "Budget de la mission (MD)", "ar": "ميزانية المهمة (م.د)"}, _BUDGET)])
    figtools.figure_tabs(vues, df, SERIE_BUDGET, SERIE_DEN, slug="fig_agri_budget_mission",
                         caption=caption, note_lecture=note_lecture, generated=generated)


# =========================================================================================
# Primes d'investissement APIA : approuvées (2010-2016) et décaissées (2018-2023)
# =========================================================================================
SERIE_APIA = "agri-apia-primes"
figtools.register_provenance(
    SERIE_APIA,
    titre="Primes d'investissement agricole de l'APIA : approuvées (2010-2016) et décaissées (2018-2023)",
    titre_ar="منح الاستثمار الفلاحي للوكالة: المصادق عليها (2010-2016) والمصروفة (2018-2023)",
    sources=["apia-repartition-doa-2010-2017", "apia-rapport-activite-2018",
             "apia-rapport-activite-2019", "apia-rapport-activite-2020",
             "apia-rapport-activite-2021", "apia-rapport-activite-2022",
             "apia-rapport-activite-2023", "banquemondiale2014-revolution-inachevee"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("primes approuvées : périmètre agricole (agriculture, pêche, aquaculture, première "
               "transformation) ; primes décaissées : ordres de paiement exécutés par l'APIA ; "
               "point 2009 = primes versées d'après la Banque mondiale, base différente"),
    perimetre_ar=("المنح المصادق عليها: النطاق الفلاحي؛ المنح المصروفة: أذون الصرف المنفّذة من الوكالة"),
    caveats=("Approuvé et décaissé ne se chaînent pas (2017 manquant) ; le point 2009 est d'une "
             "autre source. Dinars courants."),
    caveats_ar="المصادق عليه والمصروف لا يتّصلان (2017 مفقودة)؛ ونقطة 2009 من مصدر آخر. بالدينار الجاري.",
)
_APIA_APPR = {2010: 38, 2011: 40, 2012: 35, 2013: 36, 2014: 46, 2015: 44, 2016: 63}
_APIA_VERS = {2009: 54, 2018: 52.8, 2019: 112.5, 2020: 62, 2021: 89, 2022: 44.2, 2023: 60.1}


def fig_apia_primes(caption, note_lecture=None, generated=None):
    courbes = [
        ({"fr": "Primes approuvées (périmètre agricole)", "ar": "المنح المصادق عليها"},
         _APIA_APPR, BLEU, "o"),
        ({"fr": "Primes décaissées", "ar": "المنح المصروفة"}, _APIA_VERS, ORANGE, "s"),
    ]
    ylabel = {"fr": "Primes (millions de dinars)", "ar": "المنح (مليون دينار)"}
    vues = _vues(lambda m: _fig_lignes_mesure(courbes, ylabel, m, ymax=130))
    annees = sorted(set(_APIA_APPR) | set(_APIA_VERS))
    df = _table_parts(annees, [
        ({"fr": "Approuvées (MD)", "ar": "المصادق عليها (م.د)"}, _APIA_APPR),
        ({"fr": "Décaissées (MD)", "ar": "المصروفة (م.د)"}, _APIA_VERS)])
    figtools.figure_tabs(vues, df, SERIE_APIA, SERIE_DEN, slug="fig_agri_apia_primes",
                         caption=caption, note_lecture=note_lecture, generated=generated)


# =========================================================================================
# Fonds de calamités : dotation de l'État et indemnisations versées, 2018-2023
# =========================================================================================
SERIE_FONDS = "agri-fonds-calamites"
figtools.register_provenance(
    SERIE_FONDS,
    titre="Fonds d'indemnisation des calamités agricoles : dotation de l'État et indemnisations versées, 2018-2023",
    titre_ar="صندوق التعويض عن الجوائح الفلاحية: منحة الدولة والتعويضات المصروفة، 2018-2023",
    sources=["tn-minfin-fonds-speciaux-2022", "tn-minfin-fonds-speciaux-2025"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("réalisations d'exécution du compte spécial du Trésor (Trésorerie Générale, CTAMA) ; "
               "le fonds démarre le 28 octobre 2019"),
    perimetre_ar="إنجازات تنفيذ الحساب الخاصّ للخزينة (الخزينة العامة، كتاما)؛ انطلق الصندوق في 28 أكتوبر 2019",
    caveats="Dinars courants. Dotation et indemnités nulles en 2018, le fonds n'ayant pas démarré.",
    caveats_ar="بالدينار الجاري. المنحة والتعويضات منعدمة في 2018 قبل انطلاق الصندوق.",
)
_FONDS_DOT = {2018: 0, 2019: 30, 2020: 30, 2021: 30, 2022: 30, 2023: 30}
_FONDS_IND = {2018: 0, 2019: 0, 2020: 20.3, 2021: 20.0, 2022: 28.4, 2023: 59.3}


def _fig_fonds(mesure: str):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    annees = sorted(_FONDS_DOT)
    dot, ind = _en_mesure(_FONDS_DOT, mesure), _en_mesure(_FONDS_IND, mesure)
    fig, ax = plt.subplots(figsize=(8, 5.2))
    ax.bar([a - 0.2 for a in annees], [dot[a] for a in annees], width=0.4, color=BLEU,
           label=ft(_lab({"fr": "Dotation de l'État", "ar": "منحة الدولة"})))
    ax.bar([a + 0.2 for a in annees], [ind[a] for a in annees], width=0.4, color=ORANGE,
           label=ft(_lab({"fr": "Indemnisations versées", "ar": "التعويضات المصروفة"})))
    if mesure == "pib":
        _bases_du_pib(ax, annees)
    ax.set_ylabel(ft(_lab(_ylabel({"fr": "Millions de dinars", "ar": "مليون دينار"}, mesure))))
    ax.set_xticks(annees)
    ax.set_xticklabels([str(a) for a in annees], fontsize=9)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.2)
    ax.grid(True, axis="y", alpha=0.3)
    _legende(ax, mesure, annees)
    fig.tight_layout()
    return fig


def fig_fonds_calamites(caption, note_lecture=None, generated=None):
    annees = sorted(_FONDS_DOT)
    df = _table_parts(annees, [
        ({"fr": "Dotation de l'État (MD)", "ar": "منحة الدولة (م.د)"}, _FONDS_DOT),
        ({"fr": "Indemnisations versées (MD)", "ar": "التعويضات المصروفة (م.د)"}, _FONDS_IND)])
    figtools.figure_tabs(_vues(_fig_fonds), df, SERIE_FONDS, SERIE_DEN,
                         slug="fig_agri_fonds_calamites", caption=caption,
                         note_lecture=note_lecture, generated=generated)


# =========================================================================================
# CTAMA : primes encaissées auprès des assurés, 2017-2020
# =========================================================================================
SERIE_CTAMA = "agri-ctama-primes"
figtools.register_provenance(
    SERIE_CTAMA,
    titre="Primes encaissées par la CTAMA auprès de ses assurés, 2017-2020",
    titre_ar="المبالغ المقبوضة من المؤمَّن لهم لدى كتاما، 2017-2020",
    sources=["CtamaEF2018", "CtamaEF2020"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("encaissements de primes reçues des assurés (tableau de flux de trésorerie), tous "
               "risques de la caisse confondus ; la CTAMA est l'assureur dominant du risque agricole"),
    perimetre_ar="المبالغ المقبوضة من المؤمَّن لهم (جدول التدفّقات)، لكامل أخطار الصندوق",
    caveats="Dinars courants.", caveats_ar="بالدينار الجاري.",
)
_CTAMA = {2017: 80.0, 2018: 90.5, 2019: 100.1, 2020: 123.1}


def fig_ctama_primes(caption, note_lecture=None, generated=None):
    fig = _fig_lignes([({"fr": "Primes encaissées", "ar": "المبالغ المقبوضة"}, _CTAMA, BLEU, "o")],
                      {"fr": "Millions de dinars", "ar": "مليون دينار"}, ymax=140)
    df = _table_wide(sorted(_CTAMA),
                     [({"fr": "Primes encaissées (MD)", "ar": "المبالغ المقبوضة (م.د)"}, _CTAMA)])
    figtools.figure_tabs(fig, df, SERIE_CTAMA, slug="fig_agri_ctama_primes",
                         caption=caption, note_lecture=note_lecture, generated=generated)


# =========================================================================================
# Encouragements à l'agriculture dans les lois de finances : trois découpages non chaînables
# =========================================================================================
SERIE_ENC = "agri-encouragements-lf"
figtools.register_provenance(
    SERIE_ENC,
    titre="Crédits d'encouragement à l'agriculture des lois de finances : trois découpages successifs, 2010-2019",
    titre_ar="اعتمادات التشجيع على الفلاحة بقوانين المالية: ثلاثة تقسيمات متعاقبة، 2010-2019",
    sources=["lf-2010", "lf-2011", "lf-2012", "lf-2013", "lf-2014", "lf-2015", "lf-2016",
             "lf-2017", "loi2018-56-lf2019"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("lignes de crédits d'encouragement des tableaux des lois de finances ; trois "
               "découpages de périmètre distincts : ligne « secteur » (2010-2013), ligne "
               "« investissement » (2014-2016), faisceau de quatre lignes thématiques (depuis "
               "2017, total)"),
    perimetre_ar="سطور اعتمادات التشجيع بجداول قوانين المالية؛ ثلاثة تقسيمات مختلفة للنطاق",
    caveats=("Les trois découpages NE SE CHAÎNENT PAS : les niveaux ne sont pas comparables d'un "
             "segment à l'autre (redéfinition de périmètre, non évolution réelle). Dinars courants."),
    caveats_ar=("التقسيمات الثلاثة لا تتّصل: المستويات غير قابلة للمقارنة من مقطع إلى آخر "
                "(إعادة تعريف للنطاق، لا تطوّر حقيقي). بالدينار الجاري."),
)
_ENC1 = {2010: 119.3, 2011: 120.4, 2012: 138.5, 2013: 142.9}   # ligne unique « secteur »
_ENC2 = {2014: 70.0, 2015: 70.0, 2016: 79.0}                    # ligne « investissement »
_ENC3 = {2017: 81.0, 2019: 113.0}                              # total des 4 lignes thématiques


def fig_encouragements(caption, note_lecture=None, generated=None):
    L1 = {"fr": "Ligne « secteur » (2010-2013)", "ar": "سطر «القطاع» (2010-2013)"}
    L2 = {"fr": "Ligne « investissement » (2014-2016)", "ar": "سطر «الاستثمار» (2014-2016)"}
    L3 = {"fr": "Quatre lignes thématiques, total (depuis 2017)",
          "ar": "أربعة سطور موضوعية، المجموع (منذ 2017)"}
    courbes = [(L1, _ENC1, BLEU, "o"), (L2, _ENC2, ORANGE, "s"), (L3, _ENC3, GRIS, "^")]
    ylabel = {"fr": "Crédits d'encouragement (millions de dinars)",
              "ar": "اعتمادات التشجيع (مليون دينار)"}
    vues = _vues(lambda m: _fig_lignes_mesure(courbes, ylabel, m, ymax=160, ruptures=(2014, 2017)))
    annees = sorted(set(_ENC1) | set(_ENC2) | set(_ENC3))
    df = _table_parts(annees, [
        ({"fr": "Ligne « secteur » (MD)", "ar": "سطر «القطاع» (م.د)"}, _ENC1),
        ({"fr": "Ligne « investissement » (MD)", "ar": "سطر «الاستثمار» (م.د)"}, _ENC2),
        ({"fr": "Quatre lignes, total (MD)", "ar": "أربعة سطور، المجموع (م.د)"}, _ENC3)])
    figtools.figure_tabs(vues, df, SERIE_ENC, SERIE_DEN, slug="fig_agri_encouragements",
                         caption=caption, note_lecture=note_lecture, generated=generated)


# =========================================================================================
# Exécution du budget du ministère : BOOST (2008-2014) et RAP (2019-2023)
# =========================================================================================
SERIE_EXEC = "agri-budget-execution"
figtools.register_provenance(
    SERIE_EXEC,
    titre="Exécution du budget du ministère de l'Agriculture : crédits payés sur ressources de l'État, 2008-2023",
    titre_ar="تنفيذ ميزانية وزارة الفلاحة: الاعتمادات المدفوعة على موارد الدولة، 2008-2023",
    sources=["boost-tunisie-minfin-bm", "tn-rap-agriculture-2019", "tn-rap-agriculture-2020",
             "tn-rap-agriculture-2022", "tn-rap-agriculture-2023"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("crédits payés (exécution), ressources de l'État, hors ressources propres ; 2008-2014 "
               "base BOOST (chapitres ministère + commissariats régionaux), 2019-2023 rapports annuels "
               "de performance ; nomenclatures différentes de part et d'autre de 2019"),
    perimetre_ar="الاعتمادات المدفوعة (التنفيذ)، موارد الدولة، دون الموارد الذاتية",
    caveats=("Deux sources et deux nomenclatures : BOOST (exécution par chapitre) avant 2014, RAP "
             "après 2019 ; années 2015-2018 et 2021 non disponibles. Dinars courants."),
    caveats_ar="مصدران وتبويبان: BOOST قبل 2014، تقارير الأداء بعد 2019؛ سنوات 2015-2018 و2021 غير متوفّرة. بالدينار الجاري.",
)
_EXEC_BOOST = {2008: 706.5, 2009: 770.3, 2010: 792.4, 2011: 905.7, 2012: 1095.8, 2013: 956.8, 2014: 959.2}
_EXEC_RAP = {2019: 1482.2, 2020: 1971.4, 2022: 1890.3, 2023: 1900.9}


def fig_budget_execution(caption, note_lecture=None, generated=None):
    courbes = [
        ({"fr": "Exécution (base BOOST), 2008-2014", "ar": "التنفيذ (قاعدة BOOST)، 2008-2014"},
         _EXEC_BOOST, GRIS, "o"),
        ({"fr": "Exécution (rapports de performance), 2019-2023",
          "ar": "التنفيذ (تقارير الأداء)، 2019-2023"}, _EXEC_RAP, BLEU, "s"),
    ]
    ylabel = {"fr": "Crédits payés (millions de dinars)", "ar": "الاعتمادات المدفوعة (مليون دينار)"}
    vues = _vues(lambda m: _fig_lignes_mesure(courbes, ylabel, m, ymax=2200, ruptures=(2019,)))
    annees = sorted(set(_EXEC_BOOST) | set(_EXEC_RAP))
    df = _table_parts(annees, [
        ({"fr": "Exécution BOOST (MD)", "ar": "تنفيذ BOOST (م.د)"}, _EXEC_BOOST),
        ({"fr": "Exécution RAP (MD)", "ar": "تنفيذ تقارير الأداء (م.د)"}, _EXEC_RAP)])
    figtools.figure_tabs(vues, df, SERIE_EXEC, SERIE_DEN, slug="fig_agri_budget_execution",
                         caption=caption, note_lecture=note_lecture, generated=generated)
