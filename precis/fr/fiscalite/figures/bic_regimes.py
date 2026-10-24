"""Impôt des BIC rapporté au chiffre d'affaires, selon le régime, réforme par réforme.

Une figure, dix panneaux — un par état du droit du régime forfaitaire (1990, 1993, 1999, 2006,
2011, 2014, 2016, 2018, 2023, 2026) — et, dans chaque panneau, une courbe par régime : le
forfait (une courbe par activité et par zone quand le texte les distingue), l'impôt forfaitaire
optionnel quand il existe (1999-2010, 2026) et le régime réel sous deux hypothèses de bénéfice.

CHOIX DE PRÉSENTATION (petits multiples, non onglets). Le sujet est la comparaison des états
entre eux : à la même échelle, l'œil lit d'un panneau à l'autre le plafond qui monte, le
tarif qui change de forme (grille par tranche → taux avec plancher → montant fixe puis 3 %)
et la place de l'option. Dix onglets séparent les états et interdisent cette lecture. Les
panneaux partagent donc leurs deux axes ; le chiffre d'affaires est en dinars de 2025
(`dinars_constants`), l'ordonnée est tronquée à 12 %.

RÈGLE DES VARIANTES, la même dans tous les panneaux : une courbe par activité quand le texte
fixe des tarifs différents (1990 : trois colonnes de l'annexe II ; 2011-2015 : 2 % et 2,5 %) ;
trait plein pour le tarif hors zones communales, tireté pour les zones communales (planchers
et montants fixes plus élevés) et, pour l'option de 2026, pour les campagnes et villages
(moitié). Le plafond particulier des services (12 000 D en 1993, 50 000 D de 2011 à 2015) est
un point sur la courbe. Les annexes III (forfait simplifié, 1992-1998), assises sur des
indices d'emplois et de zones et non sur le chiffre d'affaires, ne sont pas des courbes de
cette figure. Toutes les variantes figurent dans l'onglet « Données ».

CONVENTION. Chaque panneau décrit le droit de l'année du panneau, déflaté par l'indice des
prix de cette année : chiffre d'affaires en dinars de 2025 = chiffre d'affaires courant ×
IPC(2025) / IPC(année). L'indice de 2026 n'étant pas publié, le panneau 2026 est tracé au
niveau des prix de 2025.

Le module ne lit que `figtools.series()` ; les valeurs de droit viennent des séries écrites
par `scripts/generate_forfait_bic_series.py` (TODO modéliste : openfisca-tunisia#476).
"""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import bic_regimes as calcul  # noqa: E402
import dinars_constants  # noqa: E402
import figtools  # noqa: E402
import taux_bareme  # noqa: E402

SERIE_TARIFS = "bic-forfait-tarifs"
SERIE_MINIMUM = "bic-minimum-impot"
SERIE_HYPOTHESES = "bic-hypotheses-benefice"
SERIE_IRPP = "irpp-bareme"

ETATS = (1990, 1993, 1999, 2006, 2011, 2014, 2016, 2018, 2023, 2026)
YMAX = 12.0  # % : au-delà, les planchers et montants fixes des petits chiffres d'affaires sortent du cadre
XMIN = 1_000.0  # dinars de 2025
GRILLE_TABLEAU = (5_000, 10_000, 20_000, 30_000, 50_000, 75_000, 100_000, 150_000)

# Couleur par famille de courbe : la même dans tous les panneaux.
COULEUR_ACTIVITE = {"toutes": "#0969da", "achat_transfo": "#0a3069", "conso": "#8250df",
                    "autres": "#bf3989", "services": "#1b7c83"}
COULEUR_OPTION = "#1a7f37"
COULEURS_REEL = ("#cf222e", "#bf8700")  # du bénéfice le plus élevé au moins élevé

_L = {
    "etat_1990": {"fr": "1990 : code de l'IRPP et de l'IS", "ar": "1990: مجلة الضريبة على الدخل"},
    "etat": {"fr": "{a} : loi de finances pour {a}", "ar": "{a}: قانون المالية لسنة {a}"},
    "prix_2025": {"fr": " (prix de 2025)", "ar": " (بأسعار 2025)"},
    "x": {"fr": "Chiffre d'affaires annuel (dinars de {base})",
          "ar": "رقم المعاملات السنوي (بدينار {base})"},
    "y": {"fr": "Impôt rapporté au chiffre d'affaires (%)",
          "ar": "الضريبة منسوبة إلى رقم المعاملات (%)"},
    "title": {"fr": ("Bénéfices industriels et commerciaux : impôt rapporté au chiffre "
                     "d'affaires selon le régime, état du droit de 1990 à 2026"),
              "ar": ("الأرباح الصناعية والتجارية: الضريبة منسوبة إلى رقم المعاملات حسب النظام، "
                     "وضع القانون من 1990 إلى 2026")},
    "f_toutes": {"fr": "forfait", "ar": "النظام التقديري"},
    "f_achat_transfo": {"fr": "forfait, achat-revente et transformation",
                        "ar": "النظام التقديري، الشراء للبيع والتحويل"},
    "f_conso": {"fr": "forfait, consommation sur place", "ar": "النظام التقديري، الاستهلاك بعين المكان"},
    "f_autres": {"fr": "forfait, autres activités", "ar": "النظام التقديري، الأنشطة الأخرى"},
    "f_services": {"fr": "forfait, services", "ar": "النظام التقديري، الخدمات"},
    "option": {"fr": "impôt forfaitaire optionnel", "ar": "الضريبة التقديرية الاختيارية"},
    "reel": {"fr": "régime réel, bénéfice égal à {t} % du chiffre d'affaires",
             "ar": "النظام الحقيقي، ربح يساوي {t} % من رقم المعاملات"},
    "zone_communale": {"fr": "zones communales", "ar": "المناطق البلدية"},
    "campagnes": {"fr": "campagnes et villages", "ar": "الأرياف والقرى"},
    "hors_communale": {"fr": "hors zones communales", "ar": "خارج المناطق البلدية"},
    "plafond_services": {"fr": "plafond particulier des services",
                         "ar": "السقف الخاص بالخدمات"},
    "trait_plein": {"fr": "trait plein : hors zones communales",
                    "ar": "خط متصل: خارج المناطق البلدية"},
    "trait_tirete": {"fr": "tireté : zones communales ; campagnes et villages (option 2026)",
                     "ar": "خط متقطّع: المناطق البلدية؛ الأرياف والقرى (خيار 2026)"},
    "c_plafond_cour": {"fr": "Plafond du forfait<br>(D courants)", "ar": "سقف النظام التقديري<br>(د جارية)"},
    "c_plafond_const": {"fr": "Plafond du forfait<br>(D de {base})",
                        "ar": "سقف النظام التقديري<br>(د {base})"},
    "c_reforme": {"fr": "Réforme", "ar": "الإصلاح"},
    "c_regime": {"fr": "Régime", "ar": "النظام"},
    "c_ca_const": {"fr": "Chiffre d'affaires (D de {base})", "ar": "رقم المعاملات (د {base})"},
    "c_ca_cour": {"fr": "Chiffre d'affaires (D courants)", "ar": "رقم المعاملات (د جارية)"},
    "c_impot": {"fr": "Impôt (D courants)", "ar": "الضريبة (د جارية)"},
    "c_impot_const": {"fr": "Impôt (D de {base})", "ar": "الضريبة (د {base})"},
    "c_taux": {"fr": "Impôt rapporté au chiffre d'affaires (%)",
               "ar": "الضريبة منسوبة إلى رقم المعاملات (%)"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _pct(t: float) -> str:
    return f"{100 * t:g}".replace(".", ",") if figtools.lang() != "ar" else f"{100 * t:g}"


# ------------------------------------------------------------------------------- données


class Donnees:
    """Les quatre séries lues, et les grandeurs communes à tous les panneaux."""

    def __init__(self):
        self.tarifs = figtools.series(SERIE_TARIFS)
        self.minimum = figtools.series(SERIE_MINIMUM)
        self.taux_benefice = sorted((float(t) for t in figtools.series(SERIE_HYPOTHESES)["taux_benefice"]),
                                    reverse=True)
        self.irpp = figtools.series(SERIE_IRPP)
        self.ipc = dinars_constants.ipc()
        self.base = dinars_constants.ANNEE_BASE

    def k(self, annee: int) -> float:
        """Dinars constants = dinars courants × k. 1 en 2026, dont l'indice n'est pas publié."""
        return self.ipc[self.base] / self.ipc[annee] if annee in self.ipc else 1.0

    def bareme(self, annee: int):
        return taux_bareme.bareme_a_la_date(self.irpp, "bareme", "irpp", f"{annee}-01-01")

    def plafond_max_constant(self) -> float:
        """Plus haut plafond du forfait, en dinars constants (l'option garde sa propre borne)."""
        forfait = self.tarifs[self.tarifs["regime"] == "forfait"]
        return max(self.k(e) * float(forfait[forfait["etat"] == e]["haut"].max()) for e in ETATS)


def _courbes(d: Donnees, etat: int) -> list[dict]:
    """Les courbes d'un panneau : clé de couleur, libellé, tiret, fonction chiffre d'affaires courant -> impôt."""
    courbes = []
    for regime, activite, zone in calcul.variantes_a_l_etat(d.tarifs, etat):
        morceaux = calcul.morceaux_a_l_etat(d.tarifs, etat, regime, activite, zone)
        ps = d.tarifs[(d.tarifs["etat"] == etat) & (d.tarifs["activite"] == activite)]["plafond_services"].max()
        courbes.append(dict(
            regime=regime, activite=activite, zone=zone,
            couleur=COULEUR_OPTION if regime == "option" else COULEUR_ACTIVITE[activite],
            tirete=zone in ("communale", "campagnes"),
            f=(lambda ca, m=morceaux: calcul.impot_forfait(m, ca)),
            plafond=calcul.plafond(morceaux),
            plafond_services=None if ps != ps else float(ps)))
    minimum = calcul.minimum_a_l_annee(d.minimum, etat)
    bareme = d.bareme(etat)
    for i, tau in enumerate(d.taux_benefice):
        courbes.append(dict(
            regime="reel", activite="", zone="", tau=tau, couleur=COULEURS_REEL[i], tirete=False,
            f=(lambda ca, t=tau: calcul.impot_reel(bareme, minimum, ca, t)),
            plafond=None, plafond_services=None))
    return courbes


def _libelle_courbe(c: dict) -> str:
    if c["regime"] == "reel":
        return _lab("reel").format(t=_pct(c["tau"]))
    base = _lab("option") if c["regime"] == "option" else _lab("f_" + c["activite"])
    zone = {"communale": _lab("zone_communale"), "campagnes": _lab("campagnes"),
            "hors_communale": _lab("hors_communale")}.get(c["zone"])
    return f"{base}, {zone}" if zone else base


def _etat_lab(annee: int) -> str:
    return _lab("etat_1990") if annee == 1990 else _lab("etat").format(a=annee)


# --------------------------------------------------------------------------------- figure


def fig_bic_regimes():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.lines import Line2D

    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = Donnees()
    xmax = 10_000 * np.ceil(d.plafond_max_constant() / 10_000)
    xs = np.linspace(XMIN, xmax, 1800)
    colonnes, rangs = 3, 4
    fig, axes = plt.subplots(rangs, colonnes, figsize=(12.6, 12.4), sharex=True, sharey=True,
                             squeeze=False)
    legende: dict[str, tuple[str, Line2D]] = {}
    for ax, etat in zip(axes.flat, ETATS):
        k = d.k(etat)
        for c in _courbes(d, etat):
            cours = xs / k
            ys = np.array([np.nan if (v := c["f"](float(ca))) is None else 100 * v / ca
                           for ca in cours])
            ligne, = ax.plot(xs, ys, color=c["couleur"], lw=1.9 if c["regime"] != "reel" else 1.6,
                             ls=(0, (4, 2.5)) if c["tirete"] else "-",
                             zorder=4 if c["regime"] != "reel" else 3)
            nom = _libelle_courbe(c)
            figtools.infobulle(ligne, f"{etat} · {nom}")
            sans_zone = _libelle_courbe({**c, "zone": ""})  # la zone se lit au tracé, tireté ou plein
            legende.setdefault(sans_zone, (sans_zone, Line2D([], [], color=c["couleur"], lw=2)))
            if c["plafond_services"] and c["zone"] in ("", "hors_communale"):
                ca_s = c["plafond_services"]
                v = c["f"](ca_s)
                ax.plot([ca_s * k], [100 * v / ca_s], marker="v", ms=5, color=c["couleur"],
                        zorder=6, ls="none")
                legende.setdefault("plafond_services", (_lab("plafond_services"), Line2D(
                    [], [], color="#57606a", marker="v", ms=5, ls="none")))
        titre = _etat_lab(etat) + (_lab("prix_2025") if etat not in d.ipc else "")
        ax.set_title(ft(titre), fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, xmax)
        ax.set_ylim(0, YMAX)
        ax.tick_params(labelsize=8, labelbottom=True)  # une graduation sous chaque panneau
        ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
            lambda x, _p: ft(f"{x:,.0f}".replace(",", " "))))
    for ax in axes[:, 0]:
        ax.set_ylabel(ft(_lab("y")), fontsize=8)
    for ax in axes[-1]:
        ax.set_xlabel(ft(_lab("x").format(base=d.base)), fontsize=8)
    # Les deux cases libres de la dernière ligne portent la légende.
    libres = list(axes.flat)[len(ETATS):]
    for ax in libres:
        ax.axis("off")
    ordre = sorted(legende.values(), key=lambda p: (p[0].startswith("régime") or p[0].startswith("النظام الحقيقي"), p[0]))
    poignees = [h for _n, h in ordre]
    noms = [ft(n) for n, _h in ordre]
    poignees += [Line2D([], [], color="#57606a", lw=2), Line2D([], [], color="#57606a", lw=2,
                                                                 ls=(0, (4, 2.5)))]
    noms += [ft(_lab("trait_plein")), ft(_lab("trait_tirete"))]
    fig.legend(poignees, noms, loc="lower center", bbox_to_anchor=(0.62, 0.0), fontsize=8,
               frameon=False, ncol=1)
    fig.suptitle(ft(_lab("title")), fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return fig


# --------------------------------------------------------------------------------- données


def table_bic_regimes():
    """Tableau de l'onglet « Données » : toutes les variantes de tous les états, huit chiffres d'affaires."""
    import pandas as pd
    d = Donnees()
    cols = (_lab("c_reforme"), _lab("c_regime"), _lab("c_ca_const").format(base=d.base),
            _lab("c_ca_cour"), _lab("c_impot"), _lab("c_impot_const").format(base=d.base),
            _lab("c_taux"))
    lignes = []
    for etat in ETATS:
        k = d.k(etat)
        sans_indice = etat not in d.ipc  # 2026 : prix de 2025, aucun montant en dinars constants
        for c in _courbes(d, etat):
            for x in GRILLE_TABLEAU:
                ca = x / k
                v = c["f"](ca)
                lignes.append({cols[0]: etat, cols[1]: _libelle_courbe(c),
                               cols[2]: None if sans_indice else x, cols[3]: round(ca),
                               cols[4]: None if v is None else round(v, 2),
                               cols[5]: None if (v is None or sans_indice) else round(v * k, 2),
                               cols[6]: None if v is None else round(100 * v / ca, 2)})
    return pd.DataFrame(lignes)


def markdown_plafonds() -> str:
    """Plafond de chiffre d'affaires du forfait à chaque état, en dinars courants et en dinars constants.

    Le plus haut plafond de l'état : 1990, la colonne de la production et de l'achat-revente ;
    1993 et 2011-2015, le plafond des activités autres que les services.
    """
    d = Donnees()
    virgule = figtools.lang() != "ar"
    entetes = (_lab("c_reforme"), _lab("c_plafond_cour"), _lab("c_plafond_const").format(base=d.base))
    lignes = ["| " + " | ".join(entetes) + " |", "|---|---:|---:|"]
    forfait = d.tarifs[d.tarifs["regime"] == "forfait"]
    for etat in ETATS:
        haut = float(forfait[forfait["etat"] == etat]["haut"].max())
        const = haut * d.k(etat)
        cell = lambda v: f"{v:,.0f}".replace(",", " ")
        const_txt = cell(round(const, -2)) if etat in d.ipc else "—"
        lignes.append(f"| {_etat_lab(etat)} | {cell(haut)} | {const_txt} |")
    return "\n".join(lignes)


def liste_valeurs_texte(etat: int, ca_constant: float) -> dict:
    """Taux (%) de chaque courbe d'un état au chiffre d'affaires `ca_constant` (D de 2025) : sert à contrôler le texte."""
    d = Donnees()
    ca = ca_constant / d.k(etat)
    return {_libelle_courbe(c): (None if (v := c["f"](ca)) is None else 100 * v / ca)
            for c in _courbes(d, etat)}


figtools.register_provenance(
    SERIE_TARIFS,
    titre=("Tarif de l'impôt forfaitaire des bénéfices industriels et commerciaux, par tranche "
           "de chiffre d'affaires, pour les états du droit de 1990 à 2026"),
    titre_ar=("تعريفة الضريبة التقديرية للأرباح الصناعية والتجارية، حسب شريحة رقم المعاملات، "
              "لأوضاع القانون من 1990 إلى 2026"),
    sources=["code-irpp-is-1990", "lf-1993", "lf-1999", "lf-2006", "lf-2011", "lf-2014",
             "lf-2016", "lf-2018", "lf-2023", "lf-2026"],
    unite="dinars courants de l'année de chaque état ; taux en pourcentage du chiffre d'affaires",
    unite_ar="بالدينار الجاري لسنة كلّ وضع؛ والنسب بالمائة من رقم المعاملات",
    perimetre=("dix états du droit, une ligne par morceau de tarif, avec le texte et la page qui "
               "le fixent ; les annexes III du code (forfait simplifié, 1990-1998), assises sur "
               "des indices d'emplois et de zones, ne sont pas reprises"),
    perimetre_ar=("عشرة أوضاع قانونية، سطر لكلّ جزء من التعريفة، مع النصّ والصفحة اللذين يحدّدانه؛ "
                  "ولا تُستعاد ملاحق III من المجلة (النظام التقديري المبسّط، 1990-1998) "
                  "المبنيّة على مؤشرات الأجراء والمناطق"),
    caveats=("Le tarif de 2016 à 2026 est lu comme le montant fixe, augmenté de 3 % de la "
             "fraction du chiffre d'affaires au-dessus de 10 000 D, comme l'applique la note "
             "commune n° 27/2016 (p. 5 ; exemples p. 11-12). Cette note ne commente que le tarif de 2016 : "
             "les lois de 2018 et de 2023 ne modifient que le montant fixe, et l'application du même "
             "mode de calcul à ces états prolonge la note."),
    caveats_ar=("تُقرأ تعريفة 2016 إلى 2026 على أنّها المبلغ القار مضافًا إليه 3 % من الجزء من "
                "رقم المعاملات الذي يفوق 10 000 د، كما تطبّقها المذكرة العامة عدد 27 لسنة 2016 "
                "(ص. 5 ؛ أمثلة ص. 11-12). لا تعلّق هذه المذكرة إلا على تعريفة 2016، ولا تعدّل قوانين 2018 "
                "و2023 إلا المبلغ القار، وتطبيق طريقة الحساب نفسها على هذه الأوضاع امتداد للمذكرة."),
)

figtools.register_provenance(
    SERIE_MINIMUM,
    titre=("Minimum d'impôt assis sur le chiffre d'affaires (art. 44 § II du code de l'IRPP et "
           "de l'IS), de 1990 à 2014"),
    titre_ar=("الحدّ الأدنى للضريبة المبني على رقم المعاملات (الفصل 44 §II من مجلة الضريبة على "
              "دخل الأشخاص الطبيعيين والضريبة على الشركات)، من 1990 إلى 2014"),
    sources=["code-irpp-is-1990", "lf-1998", "lf-2006", "lf-2011", "lf-2014"],
    unite="taux en pourcentage du chiffre d'affaires ; montants en dinars courants",
    unite_ar="النسبة بالمائة من رقم المعاملات؛ والمبالغ بالدينار الجاري",
    perimetre="cinq états, une ligne par modificatif, avec le texte qui le fixe",
    perimetre_ar="خمسة أوضاع، سطر لكلّ تعديل، مع النصّ الذي يحدّده",
    caveats=("Le taux de 0,2 % de 2014 vise le chiffre d'affaires local ; les exonérations "
             "(entreprises nouvelles, zones de développement régional) ne sont pas reprises."),
    caveats_ar=("نسبة 0,2 % لسنة 2014 تخصّ رقم المعاملات المحلّي؛ ولا تُستعاد الإعفاءات "
                "(المؤسسات الجديدة، مناطق التنمية الجهوية)."),
)

figtools.register_provenance(
    SERIE_HYPOTHESES,
    titre="Taux de bénéfice supposés du régime réel, en part du chiffre d'affaires",
    titre_ar="نسب الربح المفترضة للنظام الحقيقي، كحصّة من رقم المعاملات",
    sources=["lf-2026"],
    unite="part du chiffre d'affaires",
    unite_ar="حصّة من رقم المعاملات",
    perimetre=("deux hypothèses : 25 %, plafond du taux de bénéfice net estimé de l'impôt "
               "forfaitaire optionnel fixé par l'article 91 de la loi de finances pour 2026, et "
               "10 %, hypothèse de lecture"),
    perimetre_ar=("فرضيّتان: 25 %، سقف نسبة الربح الصافي المقدّر للضريبة التقديرية الاختيارية "
                  "الذي يحدّده الفصل 91 من قانون المالية لسنة 2026، و10 %، فرضيّة قراءة"),
    caveats="Le taux de 10 % n'est fixé par aucun texte.",
    caveats_ar="لا يحدّد أيّ نصّ نسبة 10 %.",
)
