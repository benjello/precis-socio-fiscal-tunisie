"""Figures du volume *La compensation* tirées de tableaux du volume (deuxième lot).

    from figures import tableaux as tb
    tb.figure("lait", caption=…, note_lecture=…)

Les valeurs sont dans `transcriptions.py`, chacune avec sa source ; ces séries ne sont pas dans
l'entrepôt et leur provenance est déclarée ici. Le style et les aides de tracé sont ceux de
`compensation.py` (couleurs, légendes, monnaie de l'année de base, onglets).

  - `lait`                 : prélèvement à l'importation sur la poudre de lait, 1990-2015,
                             en escalier, en dinars courants et en dinars de 2025 ;
  - `avant_1975`           : les repères du compte de la compensation, 1965-1975, en points ;
  - `lf_commerce`          : crédits d'interventions du ministère du commerce et dotation ;
  - `lfc_2015`             : les facteurs de la subvention des carburants en 2015, en cascade ;
  - `structure_synthese`   : la structure du prix des carburants à quatre dates ;
  - `structure_2020_2022`  : la structure à chaque date, 2020-2022, et la bouteille de gaz ;
  - `subvention_unitaire`  : la subvention unitaire des budgets citoyens, 2021-2024 ;
  - `incidence`            : la subvention alimentaire par tête selon le quintile, 2010 ;
  - `bm2013_quintiles`     : la part de chaque quintile, Banque mondiale 2013 ;
  - `bm2013_par_tete`      : le bénéfice par tête, Banque mondiale 2013, prix d'avril 2013 et
                             dinars de 2025 ;
  - `wps_unitaire`         : la subvention par unité, document de 2015, prix de mai 2014 et
                             dinars de 2025 ;
  - `wps_quintiles`        : la subvention par tête, document de 2015, prix de mai 2014 et
                             dinars de 2025, et la comparaison des deux études en dinars de 2025.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compensation as cm  # noqa: E402
import transcriptions as tr  # noqa: E402

figtools = cm.figtools
BASE = cm.BASE
_lab, _ft, _nombre, _poignee, _legende = cm._lab, cm._ft, cm._nombre, cm._poignee, cm._legende
BLEU, ORANGE, VERT, VIOLET, ROUGE, GRIS, BRUN, NOIR = (
    cm.BLEU, cm.ORANGE, cm.VERT, cm.VIOLET, cm.ROUGE, cm.GRIS, cm.BRUN, cm.NOIR)
QUINTILE_COULEURS = ("#c6dbef", "#9ecae1", "#6baed6", "#3182bd", "#08519c")
COMPOSANTES = (("cession", "#9ecae1"), ("droits", "#fdae6b"), ("marges", "#a1d99b"))

# --- provenance ------------------------------------------------------------------------------

SERIE_LAIT = "compensation-prelevement-poudre-lait-1990-2015"
SERIE_AVANT_1975 = "compensation-compte-avant-1975"
SERIE_LF_COMMERCE = "compensation-lf-commerce-interventions"
SERIE_LFC_2015 = "compensation-carburants-lfc-2015-facteurs"
SERIE_STRUCTURE = "compensation-carburants-structure-prix-2020-2022"
SERIE_SUBV_UNIT = "compensation-carburants-subvention-unitaire-2021-2024"
SERIE_INCIDENCE = "compensation-incidence-ins-cres-bad-2010"
SERIE_BM2013 = "compensation-incidence-bm-2013"
SERIE_WPS = "compensation-incidence-bm-2015-wps7312"

_PROV = {
    SERIE_LAIT: dict(
        titre=("Le prélèvement à l'importation sur la poudre de lait au profit de la Caisse "
               "générale de compensation, à chaque décret, 1990-2015"),
        sources=[r[4] for r in tr.LAIT], unite="millimes courants par kilogramme",
        perimetre=("poudre de lait à 26 % et à 0 % de matière grasse ; à partir de 2002, la "
                   "poudre à 0 % destinée aux nourrissons, aux malades ou à l'alimentation "
                   "animale et celle des autres usages"),
        caveats=("Chaque montant est placé à la date de son décret ; la date d'effet n'est pas "
                 "établie. De 2002 à 2009, le prélèvement sur la poudre à 0 % des autres usages "
                 "est variable (4 450 dinars par tonne moins le prix à l'importation et les droits "
                 "de douane). Les décrets après 1993 ne disent pas au profit de qui le prélèvement "
                 "est perçu. Aucun décret postérieur à 2015 n'est lu.")),
    SERIE_AVANT_1975: dict(
        titre="Le compte de la compensation avant 1975 : les montants que relaie la Banque centrale",
        sources=[r[4] for r in tr.AVANT_1975], unite="millions de dinars courants",
        perimetre="points isolés, 1965-1975, rapports annuels de la Banque centrale",
        caveats=("Aucune série annuelle des recettes et des dépenses n'est établie avant 1970 : "
                 "seuls ces points le sont.")),
    SERIE_LF_COMMERCE: dict(
        titre=("Les crédits d'interventions publiques du chapitre du ministère chargé du commerce, "
               "lois de finances 2000-2011"),
        sources=[r[5] for r in tr.LF_COMMERCE], unite="millions de dinars courants",
        perimetre=("crédits de paiement, titre premier ; lois de finances initiales, et lois de "
                   "finances complémentaires pour 2008 et 2009"),
        caveats=("La loi ne désigne pas la Caisse dans ces lignes. Le chapitre est celui du "
                 "ministère du commerce en 2000-2002, du commerce et de l'artisanat en 2011.")),
    SERIE_LFC_2015: dict(
        titre=("Les facteurs du passage de la prévision initiale à la prévision révisée de la "
               "subvention des carburants en 2015"),
        sources=[tr.LFC_2015_CLE], unite="millions de dinars courants",
        perimetre="rapport du projet de loi de finances complémentaire pour 2015, § 17 et 19",
        caveats=("Décomposition avant exécution ; la dépense exécutée en 2015 est de 918,0 "
                 "millions de dinars.")),
    SERIE_STRUCTURE: dict(
        titre=("La structure du prix des carburants et de la bouteille de gaz à chaque structure "
               "datée, 2020-2022"),
        sources=[tr.STRUCTURE_CLE], unite="millimes par litre ; dinars par bouteille",
        perimetre=("prix de cession, droits et taxes, frais et marges et prix public, tableau "
                   "« Produits pétroliers » de la Conjoncture énergétique"),
        caveats=("Le relevé est exhaustif depuis février 2020. Un tiret de la source est une "
                 "valeur absente. Les droits et taxes et les marges du 6 février 2021 ne sont pas "
                 "repris. Deux numéros datent du 8 juillet 2020 deux jeux de prix différents.")),
    SERIE_SUBV_UNIT: dict(
        titre=("La subvention unitaire prévisionnelle des produits pétroliers selon les budgets "
               "citoyens, 2021-2024"),
        sources=list(dict.fromkeys(r[5] for r in tr.SUBVENTION_UNITAIRE)), unite="millimes",
        perimetre="coût, prix payé et subvention par litre ou par bouteille, budgets citoyens",
        caveats=("Montants prévisionnels, à l'hypothèse de prix du baril du budget (45, 75, 89 et "
                 "81 dollars). Pour la bouteille, les budgets de 2022 à 2024 arrondissent au "
                 "dinar.")),
    SERIE_INCIDENCE: dict(
        titre="La subvention alimentaire par tête selon le quintile de niveau de vie, 2010",
        sources=[tr.INCIDENCE_CLE], unite="dinars par tête et par an",
        perimetre="étude de l'INS, du CRES et de la BAD sur l'enquête de 2010",
        caveats=("Valeurs transcrites du texte de l'étude. Les valeurs par produit et l'indice de "
                 "ciblage ne sont donnés que pour les quintiles extrêmes.")),
    SERIE_BM2013: dict(
        titre=("L'incidence des subventions à l'énergie selon la Banque mondiale (note de 2013) : "
               "parts des quintiles et bénéfice direct par tête"),
        sources=[tr.BM2013_CLE], unite="% ; dinars d'avril 2013 par tête et par an",
        perimetre="effets directs, enquête de 2010, prix d'avril 2013",
        caveats=("Estimation d'un rapport extérieur. Valeurs relevées sur les figures 11 à 13 de "
                 "la note. Le pétrole lampant, nul à l'arrondi, n'est pas repris par tête.")),
    SERIE_WPS: dict(
        titre=("La subvention à l'énergie par unité et par tête selon le document de travail de "
               "la Banque mondiale de 2015"),
        sources=[tr.WPS_CLE], unite="dinars de mai 2014",
        perimetre="sous-échantillon de l'enquête de 2010 actualisé à 2014, prix de mai 2014",
        caveats=("Estimation d'un rapport extérieur. Valeurs transcrites du texte du "
                 "document.")),
}
for _sid, _champs in _PROV.items():
    figtools.register_provenance(_sid, **_champs)

cm._L.update({
    "tb_vue_courants": {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    "tb_vue_constants": {"fr": f"Dinars de {BASE}", "ar": f"بدينارات سنة {BASE}"},
    "tb_x_date": {"fr": "Date du décret", "ar": "تاريخ الأمر"},
    "tb_lait26": {"fr": "Poudre de lait à 26 % de matière grasse",
                  "ar": "مسحوق الحليب بنسبة 26 % من المادة الدسمة"},
    "tb_lait0": {"fr": "Poudre de lait à 0 % ; à partir de 2002, destinée aux nourrissons, aux "
                       "malades ou à l'alimentation animale",
                 "ar": "مسحوق الحليب بنسبة 0 %؛ ابتداءً من 2002، المخصّص للرضّع والمرضى وتغذية "
                       "الحيوانات"},
    "tb_lait0_autre": {"fr": "Poudre de lait à 0 %, autres usages, à partir de 2002",
                       "ar": "مسحوق الحليب بنسبة 0 %، استعمالات أخرى، ابتداءً من 2002"},
    "tb_lait_formule": {"fr": "2002-2009 : prélèvement\nvariable (formule)",
                        "ar": "2002-2009: معلوم\nمتغيّر (صيغة)"},
    "tb_mkg": {"fr": "Millimes courants par kilogramme\n(dinars par tonne)",
               "ar": "مليم جارٍ للكيلوغرام\n(دينار للطن)"},
    "tb_mkg_2025": {"fr": f"Millimes de {BASE} par kilogramme\n(valeurs calculées)",
                    "ar": f"مليمات سنة {BASE} للكيلوغرام\n(قيم محسوبة)"},
    "tb_avant_subventions": {"fr": "Subventions d'exploitation versées par le compte",
                             "ar": "منح الاستغلال المدفوعة من الحساب"},
    "tb_avant_versement_budget": {"fr": "Versement du compte au budget de l'État",
                                  "ar": "تحويل الحساب إلى ميزانية الدولة"},
    "tb_avant_droits_consommation": {"fr": "Droits de consommation versés au compte",
                                     "ar": "معاليم الاستهلاك المدفوعة للحساب"},
    "tb_avant_redevances_transports": {"fr": "Redevances sur les transports versées au compte",
                                       "ar": "الإتاوات على النقل المدفوعة للحساب"},
    "tb_avant_depenses": {"fr": "Dépenses de la Caisse", "ar": "نفقات الصندوق"},
    "tb_avant_recettes": {"fr": "Recettes de la Caisse", "ar": "موارد الصندوق"},
    "tb_avant_contribution_budget": {"fr": "Contribution du budget de l'État à la Caisse",
                                     "ar": "مساهمة ميزانية الدولة في الصندوق"},
    "tb_md_log": {"fr": "Millions de dinars courants\n(échelle logarithmique)",
                  "ar": "ملايين الدنانير الجارية\n(سلّم لوغاريتمي)"},
    "tb_credit": {"fr": "Crédits d'interventions publiques du ministère du commerce",
                  "ar": "اعتمادات التدخّلات العمومية لوزارة التجارة"},
    "tb_dont_social": {"fr": "dont interventions dans le domaine social (2011)",
                       "ar": "منها التدخّلات في المجال الاجتماعي (2011)"},
    "tb_dotation": {"fr": "Dotation relayée par la Banque centrale",
                    "ar": "المنحة كما ينقلها البنك المركزي"},
    "tb_lfc": {"fr": "loi de finances\ncomplémentaire", "ar": "قانون المالية\nالتكميلي"},
    "tb_md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "tb_hausse": {"fr": "facteur qui relève la subvention", "ar": "عامل يرفع الدعم"},
    "tb_baisse": {"fr": "facteur qui abaisse la subvention", "ar": "عامل يخفّض الدعم"},
    "tb_niveau": {"fr": "prévision de la loi", "ar": "تقدير القانون"},
    "tb_cession": {"fr": "Prix de cession", "ar": "سعر الإحالة"},
    "tb_droits": {"fr": "Droits et taxes", "ar": "المعاليم والأداءات"},
    "tb_marges": {"fr": "Frais et marges", "ar": "المصاريف والهوامش"},
    "tb_public": {"fr": "Prix public, tel que la source le donne",
                  "ar": "سعر البيع للعموم كما يورده المصدر"},
    "tb_mlitre": {"fr": "Millimes par litre", "ar": "مليم للتر"},
    "tb_dbouteille": {"fr": "Dinars par bouteille de 13 kg", "ar": "دينار للقارورة (13 كغ)"},
    "tb_vue_bouteille": {"fr": "Bouteille de gaz", "ar": "قارورة الغاز"},
    "tb_subvention_unitaire": {"fr": "Subvention unitaire prévisionnelle (millimes par litre)",
                               "ar": "الدعم للوحدة المتوقَّع (مليم للتر)"},
    "tb_subvention_bouteille": {"fr": "Subvention unitaire prévisionnelle\n(dinars par bouteille)",
                                "ar": "الدعم للوحدة المتوقَّع\n(دينار للقارورة)"},
    "tb_vue_litre": {"fr": "Carburants, par litre", "ar": "المحروقات، للتر"},
    "tb_budget": {"fr": "Budget", "ar": "الميزانية"},
    "tb_quintile": {"fr": "Quintile", "ar": "الخُمس"},
    "tb_q": {"fr": "{q} quintile", "ar": "الخُمس {q}"},
    "tb_d_tete": {"fr": "Dinars courants par tête et par an (2010)",
                  "ar": "دينار جارٍ للفرد في السنة (2010)"},
    "tb_part_q": {"fr": "Part du quintile dans les bénéfices directs (%)",
                  "ar": "نصيب الخُمس من المنافع المباشرة (%)"},
    "tb_d_tete_2013": {"fr": "Dinars d'avril 2013 par tête et par an",
                       "ar": "دينار أفريل 2013 للفرد في السنة"},
    "tb_d_tete_2014": {"fr": "Dinars de mai 2014 par tête et par an",
                       "ar": "دينار ماي 2014 للفرد في السنة"},
    "tb_d_tete_2025": {"fr": f"Dinars de {BASE} par tête et par an\n(valeurs calculées)",
                       "ar": f"دينارات سنة {BASE} للفرد في السنة\n(قيم محسوبة)"},
    "tb_vue_2013": {"fr": "Prix d'avril 2013", "ar": "أسعار أفريل 2013"},
    "tb_vue_2014": {"fr": "Prix de mai 2014", "ar": "أسعار ماي 2014"},
    "tb_vue_compare": {"fr": f"Les deux études, dinars de {BASE}",
                       "ar": f"الدراستان، بدينارات سنة {BASE}"},
    "tb_ensemble_note": {"fr": "ensemble, tel que la source le donne",
                         "ar": "المجموع كما يورده المصدر"},
    "tb_bm2013_total": {"fr": "Banque mondiale, note de 2013 (prix d'avril 2013)",
                        "ar": "البنك الدولي، مذكّرة 2013 (أسعار أفريل 2013)"},
    "tb_wps_total": {"fr": "Banque mondiale, document de travail de 2015 (prix de mai 2014)",
                     "ar": "البنك الدولي، ورقة عمل 2015 (أسعار ماي 2014)"},
    "tb_d_unite": {"fr": "Dinars de mai 2014 par unité", "ar": "دينار ماي 2014 للوحدة"},
    "tb_d_unite_2025": {"fr": f"Dinars de {BASE} par unité\n(valeurs calculées)",
                        "ar": f"دينارات سنة {BASE} للوحدة\n(قيم محسوبة)"},
    "tb_non_sub": {"fr": "Prix non subventionné", "ar": "السعر دون دعم"},
    "tb_vente": {"fr": "Prix de vente", "ar": "سعر البيع"},
    "tb_subvention": {"fr": "Subvention par unité", "ar": "الدعم للوحدة"},
})

# --- aides -----------------------------------------------------------------------------------


def _cadre_simple(ax, ylabel):
    ax.set_ylabel(_ft(ylabel))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)


def _fmt(dec=0):
    return FuncFormatter(lambda v, _: _nombre(v, dec))


def _q(q):
    return _lab("tb_q", q=q)


# --- 1. Le prélèvement sur la poudre de lait --------------------------------------------------

LAIT_COURBES = {"lait26": (BLEU, "-"), "lait0": (VERT, "-"), "lait0_autre": (ORANGE, "--")}
LAIT_FIN_DATE = f"{tr.LAIT_FIN + 1}-01-01"


def _lait_lignes():
    sortie = {}
    for cle in LAIT_COURBES:
        lignes = sorted((r for r in tr.LAIT if r[0] == cle), key=lambda r: r[1])
        etats = figtools.etats_escalier([(r[1], r[2], r[3], "") for r in lignes])
        # Le prélèvement variable de 2002 n'est pas une suppression : il n'a pas de montant.
        sortie[cle] = [(d, v, "variable" if (v is None and cle == "lait0_autre") else e, t, r[4],
                        r[5]) for (d, v, e, t, _l), r in zip(etats, lignes)]
    return sortie


def _lait_moyennes():
    out = {}
    for cle, lignes in _lait_lignes().items():
        out[cle] = cm._moyennes_escalier([l[0] for l in lignes], [l[1] for l in lignes],
                                         LAIT_FIN_DATE)
    return out


def fig_lait(constants=False):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    poignees = []
    for cle, lignes in _lait_lignes().items():
        couleur, ls = LAIT_COURBES[cle]
        if constants:
            moy = _lait_moyennes()[cle]
            pts = {a: m * cm._coef(a) for a, m in moy.items() if cm._coef(a)}
            for suite in cm._suites(pts):
                ax.plot([a + 0.5 for a in suite], [pts[a] for a in suite], color=couleur, ls=ls,
                        lw=1.8, zorder=2)
            for a, y in pts.items():
                p, = ax.plot([a + 0.5], [y], "o", ms=3.5, color=couleur, zorder=3)
                figtools.infobulle(p, f"{a} · {_lab('tb_' + cle)} : {_nombre(y, 0)} — "
                                      f"{_lab('calcul')} : {_nombre(moy[a], 1)} × "
                                      f"{_nombre(cm._coef(a), 3)}")
        else:
            bout = figtools.abscisse_date(LAIT_FIN_DATE)
            for i, (date, v, etat, texte, cit, loc) in enumerate(lignes):
                x = figtools.abscisse_date(date)
                if v is None:
                    if etat == "variable":
                        ax.annotate(_ft("tb_lait_formule"), xy=(x, 0), xytext=(2, 6),
                                    textcoords="offset points", fontsize=7, color=couleur)
                        p, = ax.plot([x], [0], "x", ms=6, color=couleur, zorder=4)
                        figtools.infobulle(p, f"{date} · {_lab('tb_' + cle)} : "
                                              f"{_lab('tb_lait_formule')} · {texte}")
                    continue
                x2 = figtools.abscisse_date(lignes[i + 1][0]) if i + 1 < len(lignes) else bout
                ax.plot([x, x2], [v, v], color=couleur, ls=ls, lw=2, zorder=2)
                suivant = lignes[i + 1][1] if i + 1 < len(lignes) else None
                if suivant is not None and suivant != v:
                    ax.plot([x2, x2], [v, suivant], color=couleur, lw=1, zorder=2)
                reprise = etat == "reprise"
                p, = ax.plot([x], [v], "D" if reprise else "o", ms=5, color=couleur,
                             mfc="white" if reprise else couleur, zorder=4)
                figtools.infobulle(p, f"{date} · {_lab('tb_' + cle)} : {_nombre(v, 0)} · "
                                      f"{texte}, {loc}")
                if not reprise:
                    ax.annotate(_nombre(v, 0), xy=(x, v), xytext=(3, 3),
                                textcoords="offset points", fontsize=7.5, color=couleur,
                                fontweight="bold")
        poignees.append(_poignee("tb_" + cle, color=couleur, ls=ls, lw=2, marker="o", ms=4))
    ax.set_ylim(0, None)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.1)
    ax.yaxis.set_major_formatter(_fmt())
    ax.set_xlim(1989.5, tr.LAIT_FIN + 1.5)
    ax.set_xlabel(figtools.fig_text(_lab("x" if constants else "tb_x_date")))
    _cadre_simple(ax, "tb_mkg_2025" if constants else "tb_mkg")
    ax.grid(True, alpha=0.3)
    _legende(ax, poignees, ncol=1, y=-0.13, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_lait():
    i = cm._ipc()
    lignes = []
    for cle, serie in _lait_lignes().items():
        for date, v, etat, texte, cit, loc in serie:
            lignes.append({_lab("c_grandeur"): _lab("tb_" + cle), _lab("c_ligne"):
                           _lab("tb_x_date"), _lab("tb_x_date"): date, _lab("x"): None,
                           _lab("tb_mkg").replace("\n", " "): v,
                           _lab("c_etat_texte"): (_lab("tb_lait_formule").replace("\n", " ")
                                                  if etat == "variable"
                                                  else figtools.t(f"esc_{etat}")),
                           _lab("c_moyenne_vigueur"): None, _lab("c_indice_prix"): None,
                           _lab("tb_mkg_2025").replace("\n", " "): None,
                           _lab("c_texte"): texte, _lab("c_source"): cit,
                           _lab("c_localisation"): loc})
    for cle, moy in _lait_moyennes().items():
        for a, m in moy.items():
            lignes.append({_lab("c_grandeur"): _lab("tb_" + cle),
                           _lab("c_ligne"): _lab("ligne_moyenne"), _lab("tb_x_date"): None,
                           _lab("x"): a, _lab("tb_mkg").replace("\n", " "): None,
                           _lab("c_etat_texte"): None, _lab("c_moyenne_vigueur"): round(m, 1),
                           _lab("c_indice_prix"): round(i[a], 2),
                           _lab("tb_mkg_2025").replace("\n", " "): round(m * cm._coef(a), 1),
                           _lab("c_texte"): None, _lab("c_source"): None,
                           _lab("c_localisation"): None})
    t = pd.DataFrame(lignes)
    t[_lab("x")] = t[_lab("x")].astype("Int64")
    vues = [(_lab("tb_vue_courants"), fig_lait()), (_lab("tb_vue_constants"), fig_lait(True))]
    return vues, t, {SERIE_LAIT: [r[4] for r in tr.LAIT], **cm._cles_ipc()}, \
        "fig_compensation_prelevement_lait"


# --- 2. Le compte de la compensation avant 1975 ----------------------------------------------

AVANT_STYLE = {"subventions": (BLEU, "o"), "versement_budget": (VIOLET, "s"),
               "droits_consommation": (BRUN, "^"), "redevances_transports": (VERT, "v"),
               "depenses": (ROUGE, "D"), "recettes": (NOIR, "P"),
               "contribution_budget": (ORANGE, "*")}


def fig_avant_1975():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    poignees = []
    decal = {}
    for g, (couleur, marque) in AVANT_STYLE.items():
        for a, gg, lib, v, cle in tr.AVANT_1975:
            if gg != g:
                continue
            n = decal.get(a, 0)
            decal[a] = n + 1
            x = a + (n - 1) * 0.12
            p, = ax.plot([x], [v], marque, ms=8 if marque == "*" else 6.5, color=couleur,
                         ls="none", zorder=3)
            figtools.infobulle(p, f"{a} · {lib} : {_nombre(v, 3 if v < 3 else 1)} MD — {cle}")
            ax.annotate(_nombre(v, 2 if v < 1 else 1), xy=(x, v), xytext=(5, 0),
                        textcoords="offset points", va="center", fontsize=7, color=couleur)
        poignees.append(_poignee("tb_avant_" + g, color=couleur, marker=marque, ls="none",
                                 ms=7))
    ax.set_yscale("log")
    ax.set_yticks([0.5, 1, 2, 5, 10, 20, 50])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 1 if v < 1 else 0)))
    ax.set_xlim(1964.3, 1976)
    ax.set_xticks(range(1965, 1976))
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    _cadre_simple(ax, "tb_md_log")
    ax.grid(True, alpha=0.3)
    _legende(ax, poignees, ncol=2, y=-0.13, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_avant_1975():
    t = pd.DataFrame([{_lab("x"): a, _lab("c_grandeur"): _lab("tb_avant_" + g),
                       _lab("c_texte"): lib, _lab("c_MDT"): v, _lab("c_source"): cle}
                      for a, g, lib, v, cle in tr.AVANT_1975])
    return fig_avant_1975(), t, {SERIE_AVANT_1975: [r[4] for r in tr.AVANT_1975]}, \
        "fig_compensation_avant_1975"


# --- 3. Les crédits d'interventions du ministère du commerce ----------------------------------

def _dotations(annees):
    d = cm._compte()
    d = d[(d["famille"] == "budget_dotation_cgc_bct") & d["annee"].isin(annees)]
    return {int(r.annee): r for r in d.itertuples(index=False)}


def fig_lf_commerce():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    dot = _dotations([r[1] for r in tr.LF_COMMERCE])
    for i, (lib, a, v, dont, _dt, cle, loc) in enumerate(tr.LF_COMMERCE):
        b = ax.bar([i], [v], width=0.6, color="#cfe2fb", edgecolor=BLEU, ls="--", lw=1, zorder=2)
        figtools.infobulle(b[0], f"{lib} · {_lab('tb_credit')} : {_nombre(v)} MD — {cle}, {loc}")
        ax.annotate(_nombre(v), xy=(i, v), xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5)
        if dont is not None:
            h = ax.bar([i], [dont], width=0.6, color="none", edgecolor=BLEU, hatch="///", lw=0,
                       zorder=3)
            figtools.infobulle(h[0], f"{lib} · {_lab('tb_dont_social')} : {_nombre(dont)} MD")
        r = dot.get(a)
        if r is not None:
            p, = ax.plot([i + 0.36], [r.valeur_MDT], "D", ms=7, color=NOIR, zorder=4)
            figtools.infobulle(p, f"{a} · {_lab('tb_dotation')} : {_nombre(r.valeur_MDT)} MD — "
                                  f"{r.source}")
            ax.annotate(_nombre(r.valeur_MDT), xy=(i + 0.36, r.valeur_MDT), xytext=(5, 0),
                        textcoords="offset points", va="center", fontsize=7.5, color=NOIR)
    ax.set_xticks(range(len(tr.LF_COMMERCE)))
    ax.set_xticklabels([f"{r[1]}\n{_lab('tb_lfc')}" if "complémentaire" in r[0] else str(r[1])
                        for r in tr.LF_COMMERCE], fontsize=8)
    ax.set_ylim(0, max(r[2] for r in tr.LF_COMMERCE) * 1.12)
    ax.yaxis.set_major_formatter(_fmt())
    _cadre_simple(ax, "tb_md")
    poignees = [Patch(facecolor="#cfe2fb", edgecolor=BLEU, ls="--",
                      label=figtools.fig_text(_lab("tb_credit"))),
                Patch(facecolor="white", edgecolor=BLEU, hatch="///",
                      label=figtools.fig_text(_lab("tb_dont_social"))),
                _poignee("tb_dotation", color=NOIR, marker="D", ms=7, ls="none")]
    _legende(ax, poignees, ncol=1, y=-0.15, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_lf_commerce():
    dot = _dotations([r[1] for r in tr.LF_COMMERCE])
    lignes = []
    for lib, a, v, dont, _dt, cle, loc in tr.LF_COMMERCE:
        r = dot.get(a)
        lignes.append({_lab("tb_budget"): lib, _lab("tb_credit") + " (MD)": v,
                       _lab("tb_dont_social") + " (MD)": dont, _lab("c_source"): cle,
                       _lab("c_localisation"): loc,
                       _lab("c_dotation_bct"): r.valeur_MDT if r is not None else None,
                       _lab("c_source_dotation"): r.source if r is not None else None})
    cles = {SERIE_LF_COMMERCE: [r[5] for r in tr.LF_COMMERCE],
            cm.SERIE_COMPTE: [r.source for r in dot.values()]}
    return fig_lf_commerce(), pd.DataFrame(lignes), cles, "fig_compensation_lf_commerce"


# --- 4. La cascade de 2015 ---------------------------------------------------------------------

def fig_lfc_2015():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    niveau = 0.0
    etapes = [r for r in tr.LFC_2015 if r[1] != "écart"]
    for i, (lib, nature, v) in enumerate(etapes):
        if nature in ("départ", "arrivée"):
            b = ax.bar([i], [v], width=0.62, color="#bdbdbd", edgecolor=NOIR, lw=0.8, zorder=2)
            niveau = v
            ax.annotate(_nombre(v, 0), xy=(i, v), xytext=(0, 3), textcoords="offset points",
                        ha="center", va="bottom", fontsize=8, fontweight="bold")
        else:
            bas = niveau if v >= 0 else niveau + v
            b = ax.bar([i], [abs(v)], bottom=[bas], width=0.62,
                       color=ROUGE if v > 0 else VERT, alpha=0.75, zorder=2)
            ax.plot([i - 1 + 0.31, i - 0.31], [niveau, niveau], color=GRIS, lw=0.8, ls=":",
                    zorder=1)
            niveau += v
            ax.annotate(("+" if v > 0 else "−") + _nombre(abs(v), 0), xy=(i, bas + abs(v)),
                        xytext=(0, 3), textcoords="offset points", ha="center", va="bottom",
                        fontsize=8, color=ROUGE if v > 0 else VERT)
        figtools.infobulle(b[0], f"{lib} : {_nombre(v, 0)} MD")
    ax.plot([len(etapes) - 2 + 0.31, len(etapes) - 1 - 0.31], [niveau, niveau], color=GRIS,
            lw=0.8, ls=":")
    ax.set_xticks(range(len(etapes)))
    ax.set_xticklabels([figtools.fig_text(_wrap(r[0])) for r in etapes], fontsize=7.2)
    ax.axhline(0, color=NOIR, lw=0.8)
    ax.yaxis.set_major_formatter(_fmt())
    ax.set_ylim(-650, 2150)
    _cadre_simple(ax, "tb_md")
    poignees = [Patch(facecolor="#bdbdbd", edgecolor=NOIR, label=figtools.fig_text(_lab("tb_niveau"))),
                Patch(facecolor=ROUGE, alpha=0.75, label=figtools.fig_text(_lab("tb_hausse"))),
                Patch(facecolor=VERT, alpha=0.75, label=figtools.fig_text(_lab("tb_baisse")))]
    _legende(ax, poignees, ncol=3, y=-0.24, taille=7.5)
    fig.tight_layout()
    return fig


def _wrap(texte, largeur=18):
    mots, lignes, cour = texte.split(), [], ""
    for m in mots:
        if len(cour) + len(m) + 1 > largeur and cour:
            lignes.append(cour)
            cour = m
        else:
            cour = f"{cour} {m}".strip()
    lignes.append(cour)
    return "\n".join(lignes)


def _figure_lfc_2015():
    t = pd.DataFrame([{_lab("c_grandeur"): lib, _lab("c_ligne"): nature, _lab("c_MDT"): v,
                       _lab("c_source"): tr.LFC_2015_CLE, _lab("c_localisation"): tr.LFC_2015_LOC}
                      for lib, nature, v in tr.LFC_2015])
    return fig_lfc_2015(), t, {SERIE_LFC_2015: [tr.LFC_2015_CLE]}, "fig_compensation_lfc_2015"


# --- 5. La structure du prix -------------------------------------------------------------------

def _empile(ax, x, valeurs, public, largeur, bulle):
    """Barres empilées cession / droits / marges ; une composante absente n'est pas tracée, et
    rien n'est empilé au-dessus d'elle. Le prix public est un trait noir."""
    bas = 0.0
    for (nom, couleur), v in zip(COMPOSANTES, valeurs):
        if v is None:
            break
        b = ax.bar([x], [v], bottom=[bas], width=largeur, color=couleur, edgecolor="white",
                   lw=0.5, zorder=2)
        figtools.infobulle(b[0], f"{bulle} · {_lab('tb_' + nom)} : {_nombre(v, 3 if v < 20 else 0)}")
        bas += v
    if public is not None:
        p, = ax.plot([x - largeur / 2, x + largeur / 2], [public, public], color=NOIR, lw=1.6,
                     zorder=4)
        figtools.infobulle(p, f"{bulle} · {_lab('tb_public')} : "
                              f"{_nombre(public, 2 if public < 20 else 0)}")


def _legende_structure(ax, y=-0.16):
    poignees = [Patch(facecolor=c, label=figtools.fig_text(_lab("tb_" + n))) for n, c in COMPOSANTES]
    poignees.append(Line2D([], [], color=NOIR, lw=1.6, label=figtools.fig_text(_lab("tb_public"))))
    _legende(ax, poignees, ncol=2, y=y, taille=7.5)


def fig_structure_synthese():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    dates = list(dict.fromkeys(r[0] for r in tr.STRUCTURE_SYNTHESE))
    ticks, labels = [], []
    for i, d in enumerate(dates):
        for j, p in enumerate(tr.PRODUITS_STRUCTURE):
            r = next(r for r in tr.STRUCTURE_SYNTHESE if r[0] == d and r[1] == p)
            x = i * 4 + j
            _empile(ax, x, r[2:5], r[5], 0.8, f"{d} · {p}")
            ticks.append(x)
            labels.append(_wrap(p, 10))
        ax.annotate(d, xy=(i * 4 + 1, 0), xycoords=("data", "axes fraction"), xytext=(0, -38),
                    textcoords="offset points", ha="center", fontsize=8, fontweight="bold")
    ax.set_xticks(ticks)
    ax.set_xticklabels([figtools.fig_text(l) for l in labels], fontsize=6.8)
    ax.yaxis.set_major_formatter(_fmt())
    ax.set_ylim(0, 2800)
    _cadre_simple(ax, "tb_mlitre")
    _legende_structure(ax, y=-0.2)
    fig.tight_layout()
    return fig


def _figure_structure_synthese():
    t = pd.DataFrame([{_lab("c_date_effet"): d, _lab("c_produit"): p, _lab("tb_cession"): c,
                       _lab("tb_droits"): dr, _lab("tb_marges"): m, _lab("tb_public"): pu,
                       _lab("c_unite"): _lab("u_millimes_litre"), _lab("c_source"): tr.STRUCTURE_CLE}
                      for d, p, c, dr, m, pu in tr.STRUCTURE_SYNTHESE])
    return fig_structure_synthese(), t, {SERIE_STRUCTURE: [tr.STRUCTURE_CLE]}, \
        "fig_compensation_structure_synthese"


def fig_structure_2020_2022(produit):
    figtools.apply_lang_font()
    if produit == "bouteille":
        fig, ax = plt.subplots(figsize=(9.5, 4.6))
        for i, (per, c, d, m, pu) in enumerate(tr.STRUCTURE_BOUTEILLE):
            _empile(ax, i, (c, d, m), pu, 0.5, per)
        ax.set_xticks(range(len(tr.STRUCTURE_BOUTEILLE)))
        ax.set_xticklabels([r[0] for r in tr.STRUCTURE_BOUTEILLE], fontsize=8)
        ax.set_xlim(-0.8, len(tr.STRUCTURE_BOUTEILLE) - 0.2)
        ax.yaxis.set_major_formatter(_fmt(1))
        _cadre_simple(ax, "tb_dbouteille")
        _legende_structure(ax, y=-0.14)
        fig.tight_layout()
        return fig
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    lignes = [r for r in tr.STRUCTURE_2020_2022 if r[1] == produit]
    for i, (lib, p, c, d, m, pu, rem) in enumerate(lignes):
        if rem:
            ax.annotate(rem, xy=(i, 60), rotation=90, ha="center", va="bottom", fontsize=7,
                        color=GRIS)
            continue
        if c is None:  # cession absente : rien n'est empilé, droits et marges sont en clair
            bas = 0.0
            for (nom, couleur), v in zip(COMPOSANTES[1:], (d, m)):
                b = ax.bar([i], [v], bottom=[bas], width=0.7, color=couleur, alpha=0.45,
                           edgecolor=couleur, hatch="xx", lw=0, zorder=2)
                figtools.infobulle(b[0], f"{lib} · {_lab('tb_' + nom)} : {_nombre(v, 0)} "
                                         f"(prix de cession non donné)")
                bas += v
            p_, = ax.plot([i - 0.35, i + 0.35], [pu, pu], color=NOIR, lw=1.6, zorder=4)
            figtools.infobulle(p_, f"{lib} · {_lab('tb_public')} : {_nombre(pu, 0)}")
        else:
            _empile(ax, i, (c, d, m), pu, 0.7, lib)
    ax.set_xticks(range(len(lignes)))
    ax.set_xticklabels([figtools.fig_text(_wrap(r[0], 16)) for r in lignes], fontsize=6.3,
                       rotation=90)
    ax.set_ylim(0, 2800 if "essence" in produit else 2400)
    ax.yaxis.set_major_formatter(_fmt())
    _cadre_simple(ax, "tb_mlitre")
    _legende_structure(ax, y=-0.42)
    fig.tight_layout()
    return fig


def _figure_structure_2020_2022():
    lignes = [{_lab("c_date_effet"): lib, _lab("c_produit"): p, _lab("tb_cession"): c,
               _lab("tb_droits"): d, _lab("tb_marges"): m, _lab("tb_public"): pu,
               _lab("c_unite"): _lab("u_millimes_litre"), _lab("c_remarque"): rem or None,
               _lab("c_source"): tr.STRUCTURE_CLE}
              for lib, p, c, d, m, pu, rem in tr.STRUCTURE_2020_2022]
    lignes += [{_lab("c_date_effet"): per, _lab("c_produit"): "bouteille de gaz de 13 kg",
                _lab("tb_cession"): c, _lab("tb_droits"): d, _lab("tb_marges"): m,
                _lab("tb_public"): pu, _lab("c_unite"): _lab("u_dinars_bouteille"),
                _lab("c_remarque"): None, _lab("c_source"): tr.STRUCTURE_CLE}
               for per, c, d, m, pu in tr.STRUCTURE_BOUTEILLE]
    vues = [(p, fig_structure_2020_2022(p)) for p in tr.PRODUITS_STRUCTURE]
    vues.append((_lab("tb_vue_bouteille"), fig_structure_2020_2022("bouteille")))
    return vues, pd.DataFrame(lignes), {SERIE_STRUCTURE: [tr.STRUCTURE_CLE]}, \
        "fig_compensation_structure_2020_2022"


# --- 6. La subvention unitaire des budgets citoyens ----------------------------------------------

PRODUITS_SU = (("essence, le litre", ORANGE), ("gasoil, le litre", BLEU),
               ("gasoil sans soufre, le litre", VIOLET))


def fig_subvention_unitaire(bouteille=False):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    if bouteille:
        rows = [r for r in tr.SUBVENTION_UNITAIRE if r[1] == "bouteille de gaz"]
        for r in rows:
            v = r[4] / 1000
            b = ax.bar([r[0]], [v], width=0.6, color=BRUN, alpha=0.8, zorder=2)
            figtools.infobulle(b[0], f"{r[0]} · {r[1]} : {_nombre(v, 1)} D (coût "
                                     f"{_nombre(r[2] / 1000, 1)}, prix payé {_nombre(r[3] / 1000, 1)}) — {r[5]}, {r[6]}")
            ax.annotate(_nombre(v, 1), xy=(r[0], v), xytext=(0, 3), textcoords="offset points",
                        ha="center", va="bottom", fontsize=8)
        ax.set_xticks([r[0] for r in rows])
        ax.yaxis.set_major_formatter(_fmt())
        _cadre_simple(ax, "tb_subvention_bouteille")
        ax.set_xlabel(figtools.fig_text(_lab("tb_budget")))
        fig.tight_layout()
        return fig
    annees = sorted({r[0] for r in tr.SUBVENTION_UNITAIRE if r[1] != "bouteille de gaz"})
    for j, (p, couleur) in enumerate(PRODUITS_SU):
        for r in tr.SUBVENTION_UNITAIRE:
            if r[1] != p:
                continue
            x = r[0] + (j - 1) * 0.26
            b = ax.bar([x], [r[4]], width=0.25, color=couleur, alpha=0.8, zorder=2)
            figtools.infobulle(b[0], f"{r[0]} · {p} : {_nombre(r[4], 0)} millimes (coût "
                                     f"{_nombre(r[2], 0)}, prix payé {_nombre(r[3], 0)}) — {r[5]}, {r[6]}")
            ax.annotate(_nombre(r[4], 0), xy=(x, r[4]), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7, color=couleur)
    ax.set_xticks(annees)
    ax.yaxis.set_major_formatter(_fmt())
    _cadre_simple(ax, "tb_subvention_unitaire")
    ax.set_xlabel(figtools.fig_text(_lab("tb_budget")))
    _legende(ax, [Patch(facecolor=c, alpha=0.8, label=figtools.fig_text(p)) for p, c in PRODUITS_SU],
             ncol=3, y=-0.14, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_subvention_unitaire():
    t = pd.DataFrame([{_lab("tb_budget"): a, _lab("c_produit"): p, "Coût (millimes)": c,
                       "Prix payé (millimes)": pp, "Subvention unitaire (millimes)": s,
                       _lab("c_source"): cle, _lab("c_localisation"): loc}
                      for a, p, c, pp, s, cle, loc in tr.SUBVENTION_UNITAIRE])
    vues = [(_lab("tb_vue_litre"), fig_subvention_unitaire()),
            (_lab("tb_vue_bouteille"), fig_subvention_unitaire(True))]
    return vues, t, {SERIE_SUBV_UNIT: [r[5] for r in tr.SUBVENTION_UNITAIRE]}, \
        "fig_compensation_subvention_unitaire"


# --- 7. Les études d'impact ----------------------------------------------------------------

def fig_incidence():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    styles = {0: (BLEU, ""), 1: (ORANGE, "///"), 2: (VERT, "...")}
    for k in range(3):
        lib, vals = tr.INCIDENCE[k]
        couleur, hachure = styles[k]
        for qi, v in enumerate(vals):
            if v is None:
                continue
            x = qi + (k - 1) * 0.27
            b = ax.bar([x], [v], width=0.26, color=couleur, alpha=0.8, hatch=hachure,
                       edgecolor="white", zorder=2)
            figtools.infobulle(b[0], f"{_q(tr.QUINTILES[qi])} · {lib} : {_nombre(v, 1)}")
            ax.annotate(_nombre(v, 1), xy=(x, v), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7, color=couleur)
    ax.set_xticks(range(5))
    ax.set_xticklabels([_q(q) for q in tr.QUINTILES])
    ax.yaxis.set_major_formatter(_fmt())
    _cadre_simple(ax, "tb_d_tete")
    _legende(ax, [Patch(facecolor=styles[k][0], alpha=0.8, hatch=styles[k][1], edgecolor="white",
                        label=figtools.fig_text(tr.INCIDENCE[k][0])) for k in range(3)],
             ncol=1, y=-0.1, taille=7.5)
    fig.tight_layout()
    return fig


def _table_quintiles(lignes_valeurs, cle, loc):
    out = []
    for lib, vals in lignes_valeurs:
        ligne = {_lab("c_grandeur"): lib}
        for q, v in zip(tr.QUINTILES, vals):
            ligne[_q(q)] = v
        ligne[_lab("c_source")] = cle
        ligne[_lab("c_localisation")] = loc
        out.append(ligne)
    return pd.DataFrame(out)


def _figure_incidence():
    t = _table_quintiles(tr.INCIDENCE, tr.INCIDENCE_CLE, tr.INCIDENCE_LOC)
    return fig_incidence(), t, {SERIE_INCIDENCE: [tr.INCIDENCE_CLE]}, \
        "fig_compensation_incidence_alimentaire"


def fig_bm2013_quintiles():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    for i, (lib, vals) in enumerate(tr.BM2013_QUINTILES):
        comparaison = lib.startswith("Pour comparaison")
        for qi, v in enumerate(vals):
            x = i + (qi - 2) * 0.16
            b = ax.bar([x], [v], width=0.15, color=QUINTILE_COULEURS[qi],
                       hatch="///" if comparaison else "", edgecolor="white", zorder=2)
            figtools.infobulle(b[0], f"{lib} · {_q(tr.QUINTILES[qi])} : {v} %")
            ax.annotate(str(v), xy=(x, v), xytext=(0, 1), textcoords="offset points",
                        ha="center", va="bottom", fontsize=6)
    ax.set_xticks(range(len(tr.BM2013_QUINTILES)))
    ax.set_xticklabels([figtools.fig_text(_wrap(r[0], 16)) for r in tr.BM2013_QUINTILES],
                       fontsize=7)
    ax.yaxis.set_major_formatter(_fmt())
    _cadre_simple(ax, "tb_part_q")
    _legende(ax, [Patch(facecolor=c, label=figtools.fig_text(_q(q)))
                  for q, c in zip(tr.QUINTILES, QUINTILE_COULEURS)], ncol=5, y=-0.2, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_bm2013_quintiles():
    t = _table_quintiles(tr.BM2013_QUINTILES, tr.BM2013_CLE, tr.BM2013_QUINTILES_LOC)
    return fig_bm2013_quintiles(), t, {SERIE_BM2013: [tr.BM2013_CLE]}, \
        "fig_compensation_bm2013_quintiles"


PRODUIT_COULEUR = {"Gaz de pétrole liquéfié": BRUN, "Électricité": BLEU, "Essence": ORANGE,
                   "Gasoil": VIOLET}


def _coef_etude(annee):
    return cm._coef(annee)


def fig_par_tete(etude, constants=False):
    """Barres empilées par produit, un groupe par quintile ; le total que la source donne est
    écrit au-dessus (les produits, arrondis, ne s'y additionnent pas toujours)."""
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    if etude == "bm2013":
        lignes, produits, annee = tr.BM2013_PAR_TETE, tr.BM2013_PRODUITS, 2013
        rang_total = 5
    else:
        lignes, produits, annee = tr.WPS_QUINTILES, tr.WPS_PRODUITS, 2014
        rang_total = 5
    k = _coef_etude(annee) if constants else 1.0
    for i, r in enumerate(lignes):
        bas = 0.0
        for j, p in enumerate(produits):
            v = r[1 + j] * k
            b = ax.bar([i], [v], bottom=[bas], width=0.6, color=PRODUIT_COULEUR[p], alpha=0.8,
                       edgecolor="white", lw=0.5, zorder=2)
            figtools.infobulle(b[0], f"{r[0]} · {p} : {_nombre(v, 2)}")
            bas += v
        tot = r[rang_total] * k
        ax.annotate(_nombre(tot, 0 if etude == "bm2013" and not constants else 1), xy=(i, tot),
                    xytext=(0, 3), textcoords="offset points", ha="center", va="bottom",
                    fontsize=8, fontweight="bold")
    ax.set_xticks(range(len(lignes)))
    ax.set_xticklabels([_q(r[0]) if r[0] in tr.QUINTILES else r[0] for r in lignes], fontsize=8)
    ax.yaxis.set_major_formatter(_fmt())
    _cadre_simple(ax, "tb_d_tete_2025" if constants else
                  ("tb_d_tete_2013" if etude == "bm2013" else "tb_d_tete_2014"))
    _legende(ax, [Patch(facecolor=PRODUIT_COULEUR[p], alpha=0.8, label=figtools.fig_text(p))
                  for p in produits], ncol=4, y=-0.12, taille=7.5)
    fig.tight_layout()
    return fig


def fig_compare():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    for dx, lignes, annee, cle, couleur in ((-0.2, tr.BM2013_PAR_TETE, 2013, "tb_bm2013_total", GRIS),
                                           (0.2, tr.WPS_QUINTILES, 2014, "tb_wps_total", NOIR)):
        k = _coef_etude(annee)
        for i, r in enumerate(lignes):
            v = r[5] * k
            b = ax.bar([i + dx], [v], width=0.38, color=couleur, alpha=0.75, zorder=2)
            figtools.infobulle(b[0], f"{_lab(cle)} · {r[0]} : {_nombre(v, 1)} — {_lab('calcul')} : "
                                     f"{_nombre(r[5], 2)} × {_nombre(k, 3)}")
            ax.annotate(_nombre(v, 0), xy=(i + dx, v), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7)
    ax.set_xticks(range(6))
    ax.set_xticklabels([_q(q) for q in tr.QUINTILES] + [_lab("tb_ensemble_note").split(",")[0]],
                       fontsize=8)
    ax.yaxis.set_major_formatter(_fmt())
    _cadre_simple(ax, "tb_d_tete_2025")
    _legende(ax, [Patch(facecolor=GRIS, alpha=0.75, label=figtools.fig_text(_lab("tb_bm2013_total"))),
                  Patch(facecolor=NOIR, alpha=0.75, label=figtools.fig_text(_lab("tb_wps_total")))],
             ncol=1, y=-0.12, taille=7.5)
    fig.tight_layout()
    return fig


def _table_par_tete(lignes, produits, annee, cle, loc, extra=None):
    i = cm._ipc()
    k = cm._coef(annee)
    out = []
    for r in lignes:
        ligne = {_lab("tb_quintile"): r[0]}
        for j, p in enumerate(produits):
            ligne[f"{p} (dinars de l'étude)"] = r[1 + j]
        ligne["Ensemble (dinars de l'étude)"] = r[5]
        if extra:
            ligne[extra] = r[6]
        ligne[_lab("c_indice_prix")] = round(i[annee], 2)
        ligne[f"Ensemble (dinars de {BASE}, calcul)"] = round(r[5] * k, 1)
        ligne[_lab("c_source")] = cle
        ligne[_lab("c_localisation")] = loc
        out.append(ligne)
    return pd.DataFrame(out)


def _figure_bm2013_par_tete():
    t = _table_par_tete(tr.BM2013_PAR_TETE, tr.BM2013_PRODUITS, 2013, tr.BM2013_CLE,
                        tr.BM2013_PAR_TETE_LOC)
    vues = [(_lab("tb_vue_2013"), fig_par_tete("bm2013")),
            (_lab("tb_vue_constants"), fig_par_tete("bm2013", True))]
    return vues, t, {SERIE_BM2013: [tr.BM2013_CLE], **cm._cles_ipc()}, \
        "fig_compensation_bm2013_par_tete"


def _figure_wps_quintiles():
    t = _table_par_tete(tr.WPS_QUINTILES, tr.WPS_PRODUITS, 2014, tr.WPS_CLE, tr.WPS_QUINTILES_LOC,
                        extra="Part du total (%)")
    vues = [(_lab("tb_vue_2014"), fig_par_tete("wps")),
            (_lab("tb_vue_constants"), fig_par_tete("wps", True)),
            (_lab("tb_vue_compare"), fig_compare())]
    return vues, t, {SERIE_WPS: [tr.WPS_CLE], SERIE_BM2013: [tr.BM2013_CLE], **cm._cles_ipc()}, \
        "fig_compensation_wps_quintiles"


def fig_wps_unitaire(constants=False):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    k = cm._coef(2014) if constants else 1.0
    n = len(tr.WPS_UNITAIRE)
    for i, (lib, ns, pv, s, taux) in enumerate(tr.WPS_UNITAIRE):
        y = n - 1 - i
        for dy, v, couleur, cle in ((0.22, ns * k, GRIS, "tb_non_sub"), (0, pv * k, BLEU, "tb_vente"),
                                    (-0.22, s * k, ROUGE, "tb_subvention")):
            b = ax.barh([y + dy], [v], height=0.2, color=couleur, alpha=0.8, zorder=2)
            figtools.infobulle(b[0], f"{lib} · {_lab(cle)} : {_nombre(v, 3)}"
                                     + (f" ({taux} %)" if cle == "tb_subvention" else ""))
        ax.annotate(f"{_nombre(s * k, 3)} ({taux} %)", xy=(max(s * k, 0), y - 0.22), xytext=(3, 0),
                    textcoords="offset points", va="center", fontsize=6.5, color=ROUGE)
    ax.set_yticks(range(n))
    ax.set_yticklabels([figtools.fig_text(_wrap(r[0], 38)) for r in reversed(tr.WPS_UNITAIRE)],
                       fontsize=6.6)
    ax.axvline(0, color=NOIR, lw=0.8)
    ax.xaxis.set_major_formatter(_fmt(2))
    ax.set_xlabel(_ft("tb_d_unite_2025" if constants else "tb_d_unite"))
    ax.grid(True, axis="x", alpha=0.3)
    _legende(ax, [Patch(facecolor=c, alpha=0.8, label=figtools.fig_text(_lab(k_)))
                  for c, k_ in ((GRIS, "tb_non_sub"), (BLEU, "tb_vente"), (ROUGE, "tb_subvention"))],
             ncol=3, y=-0.1, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_wps_unitaire():
    i = cm._ipc()
    k = cm._coef(2014)
    t = pd.DataFrame([{_lab("c_produit"): lib, "Prix non subventionné (dinars de mai 2014)": ns,
                       "Prix de vente (dinars de mai 2014)": pv,
                       "Subvention (dinars de mai 2014)": s, "Taux de subvention (%)": taux,
                       _lab("c_indice_prix"): round(i[2014], 2),
                       f"Prix non subventionné (dinars de {BASE}, calcul)": round(ns * k, 3),
                       f"Prix de vente (dinars de {BASE}, calcul)": round(pv * k, 3),
                       f"Subvention (dinars de {BASE}, calcul)": round(s * k, 3),
                       _lab("c_source"): tr.WPS_CLE, _lab("c_localisation"): tr.WPS_UNITAIRE_LOC}
                      for lib, ns, pv, s, taux in tr.WPS_UNITAIRE])
    vues = [(_lab("tb_vue_2014"), fig_wps_unitaire()),
            (_lab("tb_vue_constants"), fig_wps_unitaire(True))]
    return vues, t, {SERIE_WPS: [tr.WPS_CLE], **cm._cles_ipc()}, "fig_compensation_wps_unitaire"


# --- point d'entrée ----------------------------------------------------------------------------

FIGURES = {
    "lait": _figure_lait,
    "avant_1975": _figure_avant_1975,
    "lf_commerce": _figure_lf_commerce,
    "lfc_2015": _figure_lfc_2015,
    "structure_synthese": _figure_structure_synthese,
    "structure_2020_2022": _figure_structure_2020_2022,
    "subvention_unitaire": _figure_subvention_unitaire,
    "incidence": _figure_incidence,
    "bm2013_quintiles": _figure_bm2013_quintiles,
    "bm2013_par_tete": _figure_bm2013_par_tete,
    "wps_unitaire": _figure_wps_unitaire,
    "wps_quintiles": _figure_wps_quintiles,
}
# Figures qui portent une vue en monnaie constante, ou dont les montants ne sont pas des dinars
# courants de l'année : la ligne « Source » ne dit pas « valeurs courantes ».
NON_NOMINALES = {"lait", "bm2013_par_tete", "wps_unitaire", "wps_quintiles", "bm2013_quintiles"}


def cles_absentes() -> dict[str, list[str]]:
    out = {}
    for nom, fabrique in FIGURES.items():
        _, _, cles, _ = fabrique()
        plt.close("all")
        manque: list[str] = []
        for sid, liste in cles.items():
            manque += [k for k in cm._declarer(sid, liste) if k not in manque]
        out[nom] = manque
    return out


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources), dans un chunk Quarto
    étiqueté `#| label: fig-…`, `#| output: asis`."""
    vues, table, cles, slug = FIGURES[nom]()
    for sid, liste in cles.items():
        cm._declarer(sid, liste)
    figtools.figure_tabs(vues, table, *cles, slug=slug, caption=caption,
                         note_lecture=note_lecture, nominal=nom not in NON_NOMINALES)
    plt.close("all")
