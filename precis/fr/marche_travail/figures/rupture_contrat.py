"""Figures et tableaux de la longue période du chapitre « La rupture du contrat de travail ».

    from figures import rupture_contrat as rc
    rc.vues_contrats(), rc.table_contrats()            # occupés par type de contrat, INS, 2011-2012
    rc.vues_temporaires(), rc.table_temporaires()      # part des salariés temporaires, OIT
    rc.vues_licenciements(), rc.table_licenciements()  # demandes de licenciement économique, 1998-2001
    rc.tableau_licenciements_source()                  # le tableau 30 de la source, voie « total »

D'OÙ VIENNENT LES DONNÉES. Le module ne lit que `figtools.series()` — l'entrepôt
`tunisia-data` s'il est installé, sinon le snapshot `precis/_seriescache/` :

  - `ins-enquete-emploi-occupes-type-contrat` : INS, Enquête nationale sur l'emploi 2012,
    tableau 31, p. 31 ; milliers d'occupés par type de contrat (CDD, CDI, pas de contrat, non
    déclaré, total), moyennes annuelles 2011 et 2012 et six trimestres. DÉNOMINATEUR : tous les
    occupés, indépendants compris ; jamais rapproché des parts de l'OIT ;
  - `oit-ilostat-part-salaries-temporaires` : OIT, ILOSTAT, EES_XTMP_RT ; part des salariés
    temporaires en 2010, 2014, 2019 et 2021, tirée de TROIS enquêtes (colonne `segment`).
    AUCUNE LIGNE n'est tracée, même entre les deux points de la même enquête (2010 et 2019) :
    elle passerait par-dessus la rupture de méthode que l'OIT signale en 2014 ;
  - `banque-mondiale-2004-licenciements-economiques` : Banque mondiale 2004, tableau 30, p. 60 ;
    salariés visés par les demandes de licenciement pour motif économique ou technologique et
    issues de ces demandes, 1998-2001. La série des salariés visés est « Total Layoffs » ; la
    ligne « Number of Employees » de la source (effectif des entreprises demanderesses) n'est
    pas transcrite et ne se trace jamais. Les deux parts « traitées par la commission »
    (rapportées aux salariés, rapportées aux entreprises) ne se mêlent pas : seule la première
    est tracée, la seconde reste au tableau.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_INS = "ins-enquete-emploi-occupes-type-contrat"
SERIE_OIT = "oit-ilostat-part-salaries-temporaires"
SERIE_BM = "banque-mondiale-2004-licenciements-economiques"

BLEU, ORANGE, VERT, GRIS, VIOLET, BRUN = (
    "#08519c", "#bc4c00", "#1a7f37", "#6e7781", "#6f42c1", "#8c564b")

_L = {
    # tableau de l'INS
    "c_periode": {"fr": "Période", "ar": "الفترة"},
    "c_cdd": {"fr": "Contrat à durée<br>déterminée<br>(milliers)", "ar": "عقد لمدة<br>معينة<br>(بالآلاف)"},
    "c_cdi": {"fr": "Contrat à durée<br>indéterminée<br>(milliers)", "ar": "عقد لمدة<br>غير معينة<br>(بالآلاف)"},
    "c_sans": {"fr": "Pas de<br>contrat<br>(milliers)", "ar": "دون<br>عقد<br>(بالآلاف)"},
    "c_nd": {"fr": "Non<br>déclaré<br>(milliers)", "ar": "غير<br>مصرّح به<br>(بالآلاف)"},
    "c_total": {"fr": "Total<br>des occupés<br>(milliers)", "ar": "مجموع<br>المشتغلين<br>(بالآلاف)"},
    "moy": {"fr": "{a} (moyenne annuelle)", "ar": "{a} (المعدّل السنوي)"},
    "trim": {"fr": "{a}, {t} trimestre", "ar": "{a}، الثلاثية {n}"},
    "cap_ins": {
        "fr": ("Personnes occupées selon le type de contrat, 2011-2012 "
               "(milliers, tous les occupés, indépendants compris)"),
        "ar": ("المشتغلون حسب نوع العقد، 2011-2012 "
               "(بالآلاف، كلّ المشتغلين بمن فيهم المستقلّون)")},
    "note_ins": {
        "fr": ("Source : Institut national de la statistique, *Enquête nationale sur l'emploi "
               "2012*, tableau 31, p. 31 [@ins-enquete-emploi-2012]. « Pas de contrat » "
               "comprend notamment les indépendants. Le tableau ne donne ni le premier "
               "ni le troisième trimestre de 2011. La ligne « Non déclaré » passe d'environ 38 "
               "milliers en 2011 à 2 à 4 milliers en 2012, sans explication de la source."),
        "ar": ("المصدر: المعهد الوطني للإحصاء، *المسح الوطني حول التشغيل 2012*، الجدول 31، "
               "ص. 31 [@ins-enquete-emploi-2012]. تشمل خانة «دون عقد» خاصّةً المستقلّين. لا "
               "يقدّم الجدول الثلاثيتين الأولى والثالثة لسنة 2011. ينتقل بند «غير مصرّح به» من "
               "نحو 38 ألفاً سنة 2011 إلى 2 إلى 4 آلاف سنة 2012 دون تفسير من المصدر.")},
    "x_moy": {"fr": "{a}\nmoyenne", "ar": "{a}\nالمعدّل"},
    "x_trim": {"fr": "{a}\nT{n}", "ar": "{a}\nث{n}"},
    "vue_milliers": {"fr": "Milliers d'occupés", "ar": "آلاف المشتغلين"},
    "vue_parts": {"fr": "Parts du total", "ar": "النسب من المجموع"},
    "y_milliers": {"fr": "Occupés (milliers)", "ar": "المشتغلون (بالآلاف)"},
    "y_pct_occ": {"fr": "% des occupés", "ar": "% من المشتغلين"},
    # OIT
    "x_annee": {"fr": "Année", "ar": "السنة"},
    "y_pct_sal": {"fr": "% des salariés", "ar": "% من الأجراء"},
    "ensemble": {"fr": "Ensemble", "ar": "الجملة"},
    "hommes": {"fr": "Hommes", "ar": "الرجال"},
    "femmes": {"fr": "Femmes", "ar": "النساء"},
    "enpe": {"fr": "Enquête nationale sur la population et l'emploi (INS), 2e trimestre",
             "ar": "المسح الوطني حول السكان والتشغيل (المعهد الوطني للإحصاء)، الثلاثية الثانية"},
    "lmps": {"fr": "Labor Market Panel Survey, 2e trimestre",
             "ar": "مسح لوحة سوق الشغل، الثلاثية الثانية"},
    "hies": {"fr": "Enquête nationale sur le budget et la consommation des ménages",
             "ar": "المسح الوطني حول الإنفاق والاستهلاك لدى الأسر"},
    "rupture_2014": {"fr": "rupture de méthode\nsignalée par l'OIT",
                     "ar": "قطيعة منهجية\nتشير إليها منظمة العمل الدولية"},
    "vue_points": {"fr": "Par enquête", "ar": "حسب المسح"},
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_enquete": {"fr": "Enquête", "ar": "المسح"},
    "c_rupture": {"fr": "Rupture signalée par l'OIT", "ar": "قطيعة تشير إليها المنظمة"},
    "oui_rupture": {"fr": "méthode révisée", "ar": "منهجية معدّلة"},
    # Banque mondiale 2004
    "y_salaries": {"fr": "Salariés visés par une demande", "ar": "الأجراء المعنيّون بمطلب"},
    "y_pct_comm": {"fr": "% des salariés visés", "ar": "% من الأجراء المعنيّين"},
    "licenciement_effectif": {"fr": "Licenciement effectif", "ar": "طرد فعلي"},
    "chomage_temporaire": {"fr": "Chômage temporaire", "ar": "إيقاف مؤقّت عن العمل"},
    "temps_partiel": {"fr": "Travail à temps partiel", "ar": "عمل بنصف الوقت"},
    "retraite_anticipee": {"fr": "Retraite anticipée", "ar": "تقاعد مبكّر"},
    "autres": {"fr": "Autres issues", "ar": "مآلات أخرى"},
    "total_licencies": {"fr": "Salariés visés par les demandes", "ar": "الأجراء المعنيّون بالمطالب"},
    "entreprises": {"fr": "Entreprises demanderesses", "ar": "المؤسسات الطالبة"},
    "part_licenciement_effectif_pct": {
        "fr": "Licenciements effectifs<br>(% des salariés visés)",
        "ar": "الطرد الفعلي<br>(% من الأجراء المعنيّين)"},
    "part_commission_salaries_pct": {
        "fr": "Salariés visés dont la demande<br>passe par la commission (%)",
        "ar": "الأجراء المعنيّون الذين يمرّ مطلبهم<br>باللجنة (%)"},
    "part_commission_entreprises_pct": {
        "fr": "Entreprises dont la demande<br>passe par la commission (%)",
        "ar": "المؤسسات التي يمرّ مطلبها<br>باللجنة (%)"},
    "vue_issues": {"fr": "Issues des demandes", "ar": "مآلات المطالب"},
    "vue_commission": {"fr": "Part passée par la commission", "ar": "النسبة المارّة باللجنة"},
    "c_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "cap_bm_source": {
        "fr": ("Demandes de licenciement pour motif économique ou technologique : salariés "
               "visés, issues et entreprises, 1998-2001, toutes voies confondues"),
        "ar": ("مطالب الطرد لأسباب اقتصادية أو فنية: الأجراء المعنيّون والمآلات والمؤسسات، "
               "1998-2001، كلّ المسالك")},
    "note_bm": {
        "fr": ("Source : Banque mondiale, *Employment Strategy*, 2004, vol. I, tableau 30, "
               "p. 60 [@bm-2004-employment-strategy] ; données de l'inspection du travail selon "
               "le rapport (§ 3.40, p. 59). Colonnes « Total » de la source, qui additionnent "
               "les demandes passées devant la commission de contrôle des licenciements et "
               "celles réglées hors commission. Les issues additionnées donnent les salariés "
               "visés. Les parts sont celles qu'imprime la source. L'effectif total des "
               "entreprises demanderesses, que la source imprime aussi, n'est pas un nombre de "
               "salariés licenciés et n'est pas repris."),
        "ar": ("المصدر: البنك الدولي، *استراتيجية التشغيل*، 2004، الجزء الأوّل، الجدول 30، "
               "ص. 60 [@bm-2004-employment-strategy]؛ بيانات تفقّدية الشغل حسب التقرير (الفقرة "
               "3.40، ص. 59). أعمدة «المجموع» في المصدر، وهي تجمع المطالب المعروضة على لجنة "
               "مراقبة الطرد وتلك المسوّاة خارجها. مجموع المآلات يساوي الأجراء المعنيّين. النسب "
               "كما يطبعها المصدر. أمّا العدد الجملي لأجراء المؤسسات الطالبة الذي يطبعه المصدر "
               "أيضاً فليس عدد مطرودين ولا يُعاد نشره.")},
}

ISSUES = ["licenciement_effectif", "chomage_temporaire", "temps_partiel",
          "retraite_anticipee", "autres"]
COULEURS_ISSUES = [ORANGE, BLEU, VERT, VIOLET, GRIS]
SEGMENTS = [("enpe", BLEU), ("lmps", ORANGE), ("hies", VERT)]
SEXES = [("ensemble", "o"), ("hommes", "^"), ("femmes", "v")]
# Place des étiquettes : à gauche pour l'ensemble, à droite pour les hommes et les femmes, pour
# que les valeurs voisines (2014 : 24,5 et 23,8 ; 2019 : 20,3 et 18,5) ne se chevauchent pas.
DECALAGE = {"ensemble": (-9, "right"), "hommes": (8, "left"), "femmes": (8, "left")}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _nombre(v: float, decimales: int = 1) -> str:
    """Nombre à la française : virgule décimale, espace insécable entre les milliers."""
    texte = f"{v:,.{decimales}f}"
    return texte.replace(",", "\N{NO-BREAK SPACE}").replace(".", ",")


# ---------------------------------------------------------------- INS, type de contrat

def _contrats_ins():
    d = figtools.series(SERIE_INS)
    periodes = ["2011", "2012", "2011-T2", "2011-T4", "2012-T1", "2012-T2", "2012-T3",
                "2012-T4"]
    lignes = []
    for p in periodes:
        r = d[d["periode"].astype(str) == p]
        val = {t: float(r.loc[r["type_contrat"] == t, "milliers"].iloc[0])
               for t in ("cdd", "cdi", "sans_contrat", "non_declare", "total")}
        if "-T" in p:
            a, t = p.split("-T")
            rang = "1^er^" if t == "1" else f"{t}^e^"
            libelle = _lab("trim").format(a=a, t=rang, n=t)
        else:
            libelle = _lab("moy").format(a=p)
        lignes.append((libelle, val))
    return lignes


def tableau_contrats_ins(label: str = "tbl-mt-rc-contrats-ins") -> str:
    """Tableau Markdown légendé, pour un chunk `#| output: asis`."""
    entetes = [_lab(c) for c in ("c_periode", "c_cdd", "c_cdi", "c_sans", "c_nd", "c_total")]
    sortie = ["| " + " | ".join(entetes) + " |",
              "|:---|---:|---:|---:|---:|---:|"]
    for libelle, v in _contrats_ins():
        cases = [_nombre(v[t]) for t in ("cdd", "cdi", "sans_contrat", "non_declare", "total")]
        sortie.append(f"| {libelle} | " + " | ".join(cases) + " |")
    return ("\n".join(sortie) + f"\n\n: {_lab('cap_ins')} {{#{label}}}\n\n"
            + _lab("note_ins") + "\n")


COULEURS_CONTRATS = [("cdi", BLEU), ("cdd", ORANGE), ("sans_contrat", GRIS),
                     ("non_declare", VIOLET)]
NOMS_CONTRATS = {"cdi": "c_cdi", "cdd": "c_cdd", "sans_contrat": "c_sans",
                 "non_declare": "c_nd"}


def _etiquette_courte(p: str) -> str:
    if "-T" in p:
        a, t = p.split("-T")
        return _lab("x_trim").format(a=a, n=t)
    return _lab("x_moy").format(a=p)


def _positions_contrats():
    """Les deux moyennes annuelles, un blanc, puis les six trimestres, dans l'ordre du temps."""
    codes = ["2011", "2012", "2011-T2", "2011-T4", "2012-T1", "2012-T2", "2012-T3", "2012-T4"]
    lignes = [(_etiquette_courte(c), v) for c, (_, v) in zip(codes, _contrats_ins())]
    xs = [0, 1] + [1.6 + i for i in range(1, 7)]
    return lignes, xs


def _fig_contrats(en_parts: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    lignes, xs = _positions_contrats()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bas = [0.0] * len(lignes)
    for t, couleur in COULEURS_CONTRATS:
        h = [(v[t] / v["total"] * 100 if en_parts else v[t]) for _, v in lignes]
        ax.bar(xs, h, bottom=bas, color=couleur, width=0.7,
               label=ft(_lab_texte(NOMS_CONTRATS[t]).replace(" (milliers)", "")))
        bas = [b + x for b, x in zip(bas, h)]
    if not en_parts:
        for x, total in zip(xs, bas):
            ax.annotate(_nombre(total, 0), (x, total), textcoords="offset points",
                        xytext=(0, 3), ha="center", fontsize=8)
    ax.set_xticks(xs)
    ax.set_xticklabels([ft(l) for l, _ in lignes], fontsize=8)
    ax.set_ylabel(ft(_lab("y_pct_occ" if en_parts else "y_milliers")))
    if en_parts:
        ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda x, _: _nombre(x, 0)))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), fontsize=8, frameon=False,
              ncol=4)
    fig.tight_layout()
    return fig


def vues_contrats():
    return [(_lab("vue_milliers"), _fig_contrats(False)),
            (_lab("vue_parts"), _fig_contrats(True))]


def table_contrats():
    import pandas as pd
    lignes, _ = _positions_contrats()
    cols = {_lab("c_periode"): [l.replace("\n", " ") for l, _ in lignes]}
    for t in ("cdd", "cdi", "sans_contrat", "non_declare", "total"):
        cle = NOMS_CONTRATS.get(t, "c_total")
        cols[_lab_texte(cle)] = [v[t] for _, v in lignes]
    return pd.DataFrame(cols)


# ---------------------------------------------------------------- OIT, salariés temporaires

def _temporaires():
    d = figtools.series(SERIE_OIT)
    return d.sort_values(["annee", "sexe"])


def _fig_temporaires():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _temporaires()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    for segment, couleur in SEGMENTS:
        for sexe, marqueur in SEXES:
            r = d[(d["segment"] == segment) & (d["sexe"] == sexe)]
            if r.empty:
                continue
            # Des points, jamais de ligne : voir l'en-tête du module.
            ax.scatter(r["annee"], r["part_salaries_temporaires_pct"], color=couleur,
                       marker=marqueur, s=70 if sexe == "ensemble" else 45, zorder=3,
                       edgecolor="white", linewidth=0.6)
            for _, x in r.iterrows():
                ax.annotate(f"{x['part_salaries_temporaires_pct']:.1f}".replace(".", ","),
                            (x["annee"], x["part_salaries_temporaires_pct"]),
                            textcoords="offset points", xytext=(DECALAGE[sexe][0], -3),
                            ha=DECALAGE[sexe][1], fontsize=7,
                            color=couleur)
    figtools.marque_rupture(ax, 2014, ft(_lab("rupture_2014")))
    # Deux légendes : la couleur dit l'enquête, la forme dit le groupe.
    from matplotlib.lines import Line2D
    poignees = [Line2D([], [], color=c, marker="s", ls="", ms=8, label=ft(_lab(s)))
                for s, c in SEGMENTS]
    poignees += [Line2D([], [], color=GRIS, marker=m, ls="", ms=7, label=ft(_lab(s)))
                 for s, m in SEXES]
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8,
              frameon=False, ncol=2)
    ax.set_xlim(2008.5, 2022.5)
    ax.set_xticks([2010, 2014, 2019, 2021])
    ax.set_ylim(0, 40)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_pct_sal")))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def vues_temporaires():
    return [(_lab("vue_points"), _fig_temporaires())]


def table_temporaires():
    import pandas as pd
    d = _temporaires()
    lignes = []
    for annee in sorted(d["annee"].unique()):
        r = d[d["annee"] == annee]
        seg = r["segment"].iloc[0]
        ligne = {_lab("c_annee"): int(annee), _lab("c_enquete"): _lab(seg)}
        for sexe, _ in SEXES:
            v = r.loc[r["sexe"] == sexe, "part_salaries_temporaires_pct"]
            ligne[_lab(sexe)] = None if v.empty else round(float(v.iloc[0]), 1)
        ligne[_lab("c_rupture")] = (_lab("oui_rupture")
                                    if str(r["rupture"].iloc[0]) == "B" else "")
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# ---------------------------------------------------------------- Banque mondiale 2004

ANNEES_BM = [1998, 1999, 2000, 2001]


def _bm(voie: str = "total"):
    d = figtools.series(SERIE_BM)
    d = d[d["voie"] == voie]
    return {(g, int(a)): float(v) for g, a, v in zip(d["grandeur"], d["annee"], d["valeur"])}


def _fig_issues():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    v = _bm()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bas = [0.0] * len(ANNEES_BM)
    for issue, couleur in zip(ISSUES, COULEURS_ISSUES):
        hauteurs = [v[(issue, a)] for a in ANNEES_BM]
        ax.bar(ANNEES_BM, hauteurs, bottom=bas, color=couleur, width=0.6,
               label=ft(_lab(issue)))
        bas = [b + h for b, h in zip(bas, hauteurs)]
    for a, total in zip(ANNEES_BM, bas):
        ax.annotate(_nombre(total, 0), (a, total), textcoords="offset points", xytext=(0, 3),
                    ha="center", fontsize=8)
    ax.set_xticks(ANNEES_BM)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_salaries")))
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda x, _: _nombre(x, 0)))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False,
              ncol=3)
    fig.tight_layout()
    return fig


def _fig_commission():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    v = _bm()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    parts = [v[("part_commission_salaries_pct", a)] for a in ANNEES_BM]
    ax.bar(ANNEES_BM, parts, color=BLEU, width=0.6)
    for a, p in zip(ANNEES_BM, parts):
        ax.annotate(f"{p:.1f}".replace(".", ","), (a, p), textcoords="offset points",
                    xytext=(0, 3), ha="center", fontsize=8)
    ax.set_xticks(ANNEES_BM)
    ax.set_ylim(0, 100)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_pct_comm")))
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return fig


def vues_licenciements():
    return [(_lab("vue_issues"), _fig_issues()),
            (_lab("vue_commission"), _fig_commission())]


def _lab_texte(cle: str) -> str:
    """Libellé sans saut de ligne HTML, pour les en-têtes du tableau de données."""
    return _lab(cle).replace("<br>", " ")


def table_licenciements():
    import pandas as pd
    v = _bm()
    colonnes = {_lab("c_annee"): ANNEES_BM}
    for g in ["total_licencies"] + ISSUES + ["part_commission_salaries_pct"]:
        colonnes[_lab_texte(g)] = [v[(g, a)] for a in ANNEES_BM]
    return pd.DataFrame(colonnes)


def tableau_licenciements_source(label: str = "tbl-mt-rc-licenciements-source") -> str:
    """Le tableau de la source, voie « total », en Markdown légendé."""
    v = _bm()
    grandeurs = (["total_licencies"] + ISSUES
                 + ["part_licenciement_effectif_pct", "part_commission_salaries_pct",
                    "entreprises", "part_commission_entreprises_pct"])
    sortie = ["| " + _lab("c_grandeur") + " | " + " | ".join(str(a) for a in ANNEES_BM) + " |",
              "|:---|" + "---:|" * len(ANNEES_BM)]
    for g in grandeurs:
        pct = g.endswith("_pct")
        cases = [_nombre(v[(g, a)], 1 if pct else 0) for a in ANNEES_BM]
        sortie.append(f"| {_lab(g)} | " + " | ".join(cases) + " |")
    return ("\n".join(sortie) + f"\n\n: {_lab('cap_bm_source')} {{#{label}}}\n\n"
            + _lab("note_bm") + "\n")
