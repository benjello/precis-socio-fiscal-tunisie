"""Régénère les snapshots des tableaux du livre « Le marché du travail ».

Même contrat que `generate_prestations_tables.py` : le build du site n'exécute PAS ce script,
il lit les fichiers qu'il produit, versionnés dans `precis/{fr,ar}/marche_travail/tables/` et,
pour les figures, dans `precis/_seriescache/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_marche_travail_tables.py

CE QUI EST ENGENDRÉ.
  - Le SMIG des deux régimes horaires, à l'heure et au mois, une ligne par date d'effet,
    découpé en quatre périodes (`smig_<début>_<fin>.md`) que le chapitre réunit en UN tableau
    à onglets (`markdown_un_tableau_en_onglets`) : c'est la même grandeur à plusieurs dates.
  - Le SMAG journalier, découpé de même (`smag_<début>_<fin>.md`).
  - Les indemnités spéciales de 1989 et de 1991, servies en sus du SMIG et du SMAG puis
    intégrées le 1er mai 1992 (`indemnites_speciales.md`).

L'indemnité de cherté de vie de 1971 (`indemnite_cherte_de_vie_*`, versée en 0.120) n'est
pas encore engendrée : ses pages publiques n'existent pas avant la publication de la version.
  - Cinq tableaux du droit du travail : grandeurs de la rupture du contrat, durée et congés
    aux dates repères, règles au 1er janvier 2026, congé selon l'âge, jours fériés payés
    (`mt_rc_parametres`, `mt_tt_*` ; voir la section « droit du travail » ci-dessous).
  - La série brute `marche-travail-smig-smag` (`_seriescache/`), que lisent les figures de
    la longue période, et ses liens « Base législative » en deux langues.

  - Les grilles des conventions collectives de branche, case par case, pour l'annexe du
    volume : `generate_conventions_collectives_tables.py`, appelé en fin de `main()`.

CE QUI NE L'EST PAS. La composition du SMIG — salaire de base et indemnité complémentaire
provisoire — est exposée d'après les textes, en prose : la série du salaire de base ne couvre
que 2008-2014.

La colonne « Texte » cite une clé de la bibliographie du livre pour chaque date où le texte
est identifié et versé (`CLES_SMIG`, `CLES_SMAG`) ; ailleurs, elle reprend l'intitulé et le
lien que porte la valeur elle-même.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402
import generate_conventions_collectives_tables as conventions  # noqa: E402

MT = "parameters/marche_travail"
RACINE = Path(__file__).parent.parent / "precis"
CACHE = RACINE / "_seriescache"
LIVRE = "marche_travail"
LANGUES = ("fr", "ar")

SMIG = {
    "48h_horaire": f"{MT}/smig_48h_horaire.yaml",
    "48h_mensuel": f"{MT}/smig_48h_mensuel.yaml",
    "40h_horaire": f"{MT}/smig_40h_horaire.yaml",
    "40h_mensuel": f"{MT}/smig_40h_mensuel.yaml",
}
SMAG = f"{MT}/smag_journalier.yaml"
IS_SMIG = f"{MT}/indemnite_speciale_smig.yaml"
IS_SMAG = f"{MT}/indemnite_speciale_smag.yaml"

# Périodes des onglets : avant le SMIG (minima par zone, puis indemnité de cherté de vie) ;
# SMIG à taux horaire unique ; les deux régimes divergent à l'heure le 1er avril 1981.
PERIODES_SMIG = [("1961-01-01", "1973-12-31"), ("1974-01-01", "1981-03-31"),
                 ("1981-04-01", "1999-12-31"), ("2000-01-01", "2028-12-31")]
PERIODES_SMAG = [("1964-01-01", "1980-12-31"), ("1981-01-01", "1999-12-31"),
                 ("2000-01-01", "2028-12-31")]

CLES_SMIG = {
    "1961-04-01": "decret61-145, art. 6",
    "1966-01-01": "decret65-561, art. 5",
    "1968-05-01": "decret68-97",
    "1971-05-01": "decret71-164",
    "1974-01-01": "decret74-63, art. 1",
    "1975-06-01": "decret75-357",
    "1977-02-01": "decret77-115",
    "1978-05-01": "decret78-441",
    "1979-05-01": "decret79-473",
    "1980-02-01": "decret80-75",
    "1980-05-01": "decret80-609",
    "1981-04-01": "decret81-437",
    "1982-02-01": "decret82-501",
    "1990-01-01": "decret90-246",
    "1992-05-01": "decret92-1299, art. 1",
    "2000-05-01": "decret2000-949",
    "2016-08-01": "decret-2017-668-smig",
    "2019-05-01": "decret2019-454",
    "2020-10-01": "decret2020-1069",
    "2022-10-01": "decret2022-769",
    "2024-05-01": "decret2024-419",
    "2026-01-01": "decret2026-67, art. 1",
    "2027-01-01": "decret2026-67, art. 1",
    "2028-01-01": "decret2026-67, art. 1",
}
CLES_SMAG = {
    "1968-05-01": "decret68-113",
    "1969-10-01": "decret69-344, art. 8",
    "1971-05-01": "decret71-163",
    "1974-06-01": "decret74-571, art. 1",
    "1977-02-01": "decret77-116, art. 6",
    "1980-02-01": "decret80-76",
    "1992-05-01": "decret92-1300",
    "2012-07-01": "decret2012-1982",
    "2012-12-01": "decret2012-1982",
    "2016-08-01": "decret2017-669",
    "2019-05-01": "decret2019-455",
    "2026-01-01": "decret2026-66, art. 1",
    "2027-01-01": "decret2026-66, art. 1",
    "2028-01-01": "decret2026-66, art. 1",
}
CLES_INDEMNITES = {
    "1989-08-01": "decret89-1551; @decret89-1552",
    "1991-08-01": "decret91-1316",
    "1992-05-01": "decret92-1299, art. 3; @decret92-1300, art. 3",
}

MOTS = {
    "fr": {
        "effet": "Effet", "texte": "Texte",
        "48h_horaire": "48 heures, à l'heure", "48h_mensuel": "48 heures, au mois",
        "40h_horaire": "40 heures, à l'heure", "40h_mensuel": "40 heures, au mois",
        "smag": "SMAG, par journée de travail",
        "is_smig": "Indemnité spéciale, SMIG (par mois)",
        "is_smag": "Indemnité spéciale, SMAG (par jour)",
        "integree": "intégrée au minimum",
        # Libellés des liens « Base législative » de la série des figures.
        "serie_smag": "SMAG, par journée de travail",
    },
    "ar": {
        "effet": "بداية السريان", "texte": "النصّ",
        "48h_horaire": "نظام 48 ساعة، بالساعة", "48h_mensuel": "نظام 48 ساعة، بالشهر",
        "40h_horaire": "نظام 40 ساعة، بالساعة", "40h_mensuel": "نظام 40 ساعة، بالشهر",
        "smag": "الأجر الأدنى الفلاحي المضمون، عن يوم العمل",
        "is_smig": "المنحة الخاصة، الأجر الأدنى المضمون (بالشهر)",
        "is_smag": "المنحة الخاصة، الأجر الأدنى الفلاحي (باليوم)",
        "integree": "مدمجة في الأجر الأدنى",
        "serie_smag": "الأجر الأدنى الفلاحي المضمون، عن يوم العمل",
    },
}


def dinars(v: float | None) -> str:
    """Montant en dinars, toutes décimales du texte gardées : 0,21425 et non 0,214.

    `ot.formate_dinars` tronque à trois décimales ; le SMIG horaire de 1978 (214,25 millimes,
    décret n° 78-441) en a cinq.
    """
    if v is None:
        return "—"
    entier = int(v)
    texte = f"{entier:,}".replace(",", " ")
    decimales = f"{v - entier:.5f}".split(".")[1].rstrip("0")
    return f"{texte},{decimales}" if decimales else texte


def tableau_smig(langue: str):
    m = MOTS[langue]
    specs = [(chemin, m[cle], dinars) for cle, chemin in SMIG.items()]
    df = ot.tableau_evolution_datee(specs, cles=CLES_SMIG, langue=langue,
                                    colonne_periode=m["effet"], colonne_texte=m["texte"])
    return df


def tableau_smag(langue: str):
    m = MOTS[langue]
    return ot.tableau_evolution_datee([(SMAG, m["smag"], dinars)], cles=CLES_SMAG,
                                      langue=langue, colonne_periode=m["effet"],
                                      colonne_texte=m["texte"])


def tableau_indemnites(langue: str):
    """Montant 0 au 1er mai 1992 : l'indemnité cesse d'être servie à part, intégrée au minimum."""
    m = MOTS[langue]

    def montant(v):
        return m["integree"] if v == 0 else dinars(v)

    return ot.tableau_evolution_datee([(IS_SMIG, m["is_smig"], montant),
                                       (IS_SMAG, m["is_smag"], montant)],
                                      cles=CLES_INDEMNITES, langue=langue,
                                      colonne_periode=m["effet"], colonne_texte=m["texte"])


def dates_iso(chemins: list[str]) -> list[str]:
    """Dates d'effet, triées, de l'union des paramètres : l'ordre des lignes du tableau."""
    return sorted({d for c in chemins for d, *_ in ot.serie_datee(c)})


def ecrire_decoupe(langue, nom, fabrique, chemins, periodes) -> int:
    df, liens = ot.avec_liens(fabrique)
    if df is None or df.empty:
        print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
        return 1
    dates = dates_iso(chemins)
    if len(dates) != len(df):
        print(f"✗ {langue}/{nom} : {len(df)} lignes pour {len(dates)} dates.")
        return 1
    import pandas as pd

    serie_dates = pd.Series(dates)
    for debut, fin in periodes:
        masque = (serie_dates >= debut) & (serie_dates <= fin)
        morceau = df[masque.values].reset_index(drop=True)
        if morceau.empty:
            print(f"✗ {langue}/{nom} : période {debut} → {fin} vide.")
            return 1
        fichier = f"{nom}_{debut[:4]}_{fin[:4]}.md"
        erreur = ot.ecrire_dans_livres(RACINE, langue, (LIVRE,), fichier, morceau, liens)
        if erreur:
            print(erreur)
            return 1
    if sum(((serie_dates >= d) & (serie_dates <= f)).sum() for d, f in periodes) != len(df):
        print(f"✗ {langue}/{nom} : des dates tombent hors des périodes.")
        return 1
    return 0


def serie_figures() -> int:
    """Série brute des figures : SMIG des deux régimes et SMAG, à chaque date d'effet.

    Valeurs brutes, sans langue ; une ligne par date de l'union des cinq paramètres, chaque
    colonne portant la valeur en vigueur à cette date (vide avant la première valeur).
    """
    import pandas as pd

    chemins = {**{f"smig_{k}": c for k, c in SMIG.items()}, "smag_journalier": SMAG}
    series = {col: ot.serie_datee(c) for col, c in chemins.items()}
    if not all(series.values()):
        print("✗ marche-travail-smig-smag : paramètre vide, snapshot conservé.")
        return 1
    dates = sorted({d for s in series.values() for d, *_ in s})
    lignes = []
    for date in dates:
        ligne = {"date": date}
        for col, s in series.items():
            retenue = None
            for d, v, *_ in s:
                if d <= date:
                    retenue = v
            ligne[col] = retenue
        lignes.append(ligne)
    CACHE.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(lignes).to_csv(CACHE / "marche-travail-smig-smag.csv", index=False)
    for langue in LANGUES:
        m = MOTS[langue]
        liens = [(c, m[k]) for k, c in SMIG.items()] + [(SMAG, m["serie_smag"])]
        ot.ecrire_fichier_liens(CACHE / f"marche-travail-smig-smag.liens.{langue}.yml",
                                liens, langue)
    print(f"✓ série marche-travail-smig-smag : {len(lignes)} dates, "
          f"{dates[0]} → {dates[-1]}")
    return 0


# ------------------------------------------------------------------ droit du travail
#
# Les tableaux des chapitres « La rupture du contrat de travail » et « La durée du travail
# et les congés » : cinq tableaux, un fichier chacun (`mt_<nom>.md`).
#
#   mt_rc_parametres      grandeurs de la rupture, aux dates des réformes (1966, 1973, 1994,
#                         1996, 2025) ;
#   mt_tt_parametres      durée, majoration, congé, jours fériés, aux dates repères ;
#   mt_tt_etat_du_droit   règles au 1er janvier 2026 ;
#   mt_tt_conge           congé annuel selon l'âge ;
#   mt_tt_feries          jours fériés payés, une ligne par date d'effet.
#
# Chaque case chiffrée lit la série en vigueur à sa date : `ot.Lecture` échoue sur une valeur
# vide. Une case qui annonce « idem », « inchangé » ou la fin d'une règle (« après la période
# d'essai », « interdit ») le fait par comparaison avec la case précédente, ou par contrôle
# que la série est close à cette date : ni l'un ni l'autre ne s'écrit sans la série.
#
# Restent écrits ici, sans paramètre qui les porte : la colonne de 1973 du tableau de la
# rupture (convention cadre, qui renvoie aux conventions de branche), les lignes « juge » et
# « conventions », le traitement pendant le congé, la ligne de 1964 des jours fériés, l'âge
# auquel on apprécie le congé, la colonne « Population couverte » et la ligne du travail
# domestique.

RC = f"{MT}/rupture_contrat"
TT = f"{MT}/temps_travail"
EFFET_2026 = "2026-01-01"


def _fr(v: float) -> str:
    return f"{v:g}".replace(".", ",")


def _nom_compte(sing: str, plur: str, sing_ar: tuple[str, ...], seuil: float = 2):
    """Formateur « nombre + nom » : « 1 jour ouvrable », « 2 jours ouvrables », « 1,5 jour »."""
    def rendre(v, langue):
        if langue == "ar":
            if float(v).is_integer():
                return ot.compte(int(v), sing_ar, "ar")
            return f"{_fr(v)} {sing_ar[0]}"
        return f"{_fr(v)} {sing if v < seuil else plur}"
    return rendre


def _unite(cle: str):
    return lambda v, langue: ot.compte(int(v), cle, langue)


F_MOIS, F_JOURS, F_HEURES, F_ANS = _unite("mois"), _unite("jours"), _unite("heures"), _unite("ans")
F_JOURS_OUVRABLES = _nom_compte("jour ouvrable", "jours ouvrables",
                                ("يوم عمل", "يوما عمل", "أيام عمل", "يوم عمل"))
F_JOURS_DEC = _nom_compte("jour", "jours", ("يوم", "يومان", "أيام", "يومًا"))
F_ENTIER = lambda v, langue: str(int(v))  # noqa: E731
F_ENTIER_LETTRES = lambda v, langue: (  # noqa: E731
    {8: "huit"}.get(int(v), str(int(v))) if langue == "fr"
    else {8: "الثماني"}.get(int(v), f"الـ{int(v)}"))
# Bornes d'une fourchette en mois : « من شهر إلى شهرين », « إلى 4 أشهر » (génitif, accord du nom).
F_MOIS_BORNE = lambda v, langue: (  # noqa: E731
    str(int(v)) if langue == "fr"
    else ot.compte(int(v), ("شهر", "شهرين", "أشهر", "شهرا"), "ar"))
F_DECIMAL = lambda v, langue: _fr(v)  # noqa: E731
F_TAUX = lambda v, langue: ot.formate_taux(v)  # noqa: E731
F_ANS_DE_MOIS = lambda v, langue: ot.compte(int(v) // 12, "ans", langue)  # noqa: E731
F_MILLIERS = lambda v, langue: ot.compte(int(v), "heures", langue).replace(  # noqa: E731
    f"{int(v)}", f"{int(v):,}".replace(",", " "), 1)
F_DIVISEUR = lambda v, langue: f"1/{int(v)}"  # noqa: E731
F_PAR_PERIODE = lambda v, langue: (  # noqa: E731
    {5: "cinq ans"}.get(int(v), f"{int(v)} ans") if langue == "fr" else ot.compte(int(v), "ans", langue))


def _fois(v, langue):
    n = int(v)
    if langue == "ar":
        return "مرة واحدة" if n == 1 else ot.compte(n, ("مرة", "مرتان", "مرات", "مرة"), "ar")
    return "une fois" if n == 1 else f"{n} fois"


def _indemnite_ferie(v, langue):
    if v == 1:
        return "égale au salaire" if langue == "fr" else "تساوي الأجر"
    return ot.formate_taux(v)


def _liste_feries(v, langue):
    def un(jour):
        if langue == "fr":
            return jour.replace("1er ", "1^er^ ")
        sp = jour.split(" ", 1)
        if sp[0].replace("er", "").isdigit():
            n = sp[0].replace("er", "")
            mois = ot.MOIS["fr"].index(sp[1])
            return f"{n} {ot.MOIS['ar'][mois]}"
        return JOURS_AR[jour]
    return ", ".join(un(j) for j in v) if langue == "fr" else "، ".join(un(j) for j in v)


JOURS_AR = {"Aïd El Fitr": "عيد الفطر", "Aïd El Idha": "عيد الأضحى"}


class LectureListe(ot.Lecture):
    """Lecture d'un paramètre dont la valeur est une liste (jours fériés)."""

    def valeur(self):
        donnees = ot.charge_parametre(self.chemin)
        points = sorted((str(k)[:10], v.get("value") if isinstance(v, dict) else v)
                        for k, v in donnees["values"].items())
        point = ot.en_vigueur([(d, v) for d, v in points], self.date)
        if point is None or point[1] is None:
            raise ValueError(f"{self.chemin} : aucune valeur au {self.date}")
        return point[1]


# Libellés « Base législative » : un par paramètre lu, dans chaque langue.
LIB = {
    f"{RC}/preavis/duree": ("Préavis de rupture du contrat à durée indéterminée",
                            "أجل الإعلام بإنهاء عقد الشغل لمدة غير معينة"),
    f"{RC}/preavis/duree_salaries_non_mensuels": (
        "Préavis, salariés non payés au mois", "أجل الإعلام، الأجراء غير الخالصين بالشهر"),
    f"{RC}/gratification_fin_service/jours_par_mois_service": (
        "Gratification de fin de service, jours par mois de service",
        "مكافأة نهاية الخدمة، عدد الأيام عن كل شهر خدمة"),
    f"{RC}/gratification_fin_service/plafond": (
        "Gratification de fin de service, plafond", "مكافأة نهاية الخدمة، السقف"),
    f"{RC}/gratification_fin_service/anciennete_minimale": (
        "Gratification de fin de service, ancienneté minimale",
        "مكافأة نهاية الخدمة، الأقدمية الدنيا"),
    f"{RC}/dommages_interets/minimum_par_annee_anciennete": (
        "Dommages-intérêts du licenciement abusif, minimum par année d'ancienneté",
        "غرامات الطرد التعسفي، الحد الأدنى عن كل سنة أقدمية"),
    f"{RC}/dommages_interets/maximum_par_annee_anciennete": (
        "Dommages-intérêts du licenciement abusif, maximum par année d'ancienneté",
        "غرامات الطرد التعسفي، الحد الأقصى عن كل سنة أقدمية"),
    f"{RC}/dommages_interets/plafond": (
        "Dommages-intérêts du licenciement abusif, plafond", "غرامات الطرد التعسفي، السقف"),
    f"{RC}/dommages_interets/vice_procedure_minimum": (
        "Dommages-intérêts du vice de procédure, minimum", "غرامات خرق الإجراءات، الحد الأدنى"),
    f"{RC}/dommages_interets/vice_procedure_maximum": (
        "Dommages-intérêts du vice de procédure, maximum", "غرامات خرق الإجراءات، الحد الأقصى"),
    f"{RC}/contrat_duree_determinee/duree_maximale_hors_cas_recours": (
        "Contrat à durée déterminée, durée maximale hors cas de recours",
        "عقد الشغل لمدة معينة، المدة القصوى خارج حالات اللجوء إليه"),
    f"{RC}/periode_essai/duree_maximale": ("Période d'essai, durée maximale",
                                           "فترة التجربة، المدة القصوى"),
    f"{RC}/periode_essai/renouvellements_maximum": (
        "Période d'essai, nombre maximal de renouvellements",
        "فترة التجربة، العدد الأقصى للتجديدات"),
    f"{TT}/duree/hebdomadaire_maximale": ("Durée hebdomadaire maximale du travail",
                                          "المدة القصوى للشغل في الأسبوع"),
    f"{TT}/duree/hebdomadaire_plancher_reduction": (
        "Durée hebdomadaire jusqu'à laquelle la durée du travail peut être réduite",
        "المدة الأسبوعية التي يمكن تخفيض مدة الشغل إلى حدها"),
    f"{TT}/duree/hebdomadaire_plafond_heures_supplementaires": (
        "Plafond hebdomadaire, heures supplémentaires comprises",
        "السقف الأسبوعي بما في ذلك الساعات الإضافية"),
    f"{TT}/duree/agriculture_annuelle_maximale": ("Durée annuelle maximale du travail agricole",
                                                  "المدة السنوية القصوى للشغل الفلاحي"),
    f"{TT}/heures_supplementaires/regime_48h": ("Majoration, régime de 48 heures",
                                                "الزيادة، نظام 48 ساعة"),
    f"{TT}/heures_supplementaires/regime_40h/taux_premieres_heures": (
        "Majoration, régime de 40 heures, premières heures", "الزيادة، نظام 40 ساعة، الساعات الأولى"),
    f"{TT}/heures_supplementaires/regime_40h/taux_heures_suivantes": (
        "Majoration, régime de 40 heures, heures suivantes", "الزيادة، نظام 40 ساعة، الساعات اللاحقة"),
    f"{TT}/heures_supplementaires/regime_40h/nombre_premieres_heures": (
        "Régime de 40 heures, nombre de premières heures supplémentaires",
        "نظام 40 ساعة، عدد الساعات الإضافية الأولى"),
    f"{TT}/heures_supplementaires/regimes_inferieurs_48h/seuil": (
        "Régimes inférieurs à 48 heures, seuil", "الأنظمة الأقل من 48 ساعة، العتبة"),
    f"{TT}/heures_supplementaires/regimes_inferieurs_48h/taux_jusqu_au_seuil": (
        "Régimes inférieurs à 48 heures, majoration jusqu'au seuil",
        "الأنظمة الأقل من 48 ساعة، الزيادة إلى حدود العتبة"),
    f"{TT}/heures_supplementaires/regimes_inferieurs_48h/taux_au_dela_du_seuil": (
        "Régimes inférieurs à 48 heures, majoration au-delà du seuil",
        "الأنظمة الأقل من 48 ساعة، الزيادة فوق العتبة"),
    f"{TT}/heures_supplementaires/temps_partiel": ("Majoration, temps partiel",
                                                   "الزيادة، العمل لوقت جزئي"),
    f"{TT}/heures_supplementaires/agriculture": ("Majoration, travail agricole",
                                                 "الزيادة، الشغل الفلاحي"),
    f"{TT}/conge_annuel/jours_par_mois/adultes": ("Congé annuel, jours par mois, 21 ans et plus",
                                                  "الرخصة السنوية، الأيام عن كل شهر، 21 سنة فأكثر"),
    f"{TT}/conge_annuel/jours_par_mois/de_18_a_20_ans": (
        "Congé annuel, jours par mois, 18 à 20 ans", "الرخصة السنوية، الأيام عن كل شهر، من 18 إلى 20 سنة"),
    f"{TT}/conge_annuel/jours_par_mois/moins_18_ans": (
        "Congé annuel, jours par mois, moins de 18 ans",
        "الرخصة السنوية، الأيام عن كل شهر، أقل من 18 سنة"),
    f"{TT}/conge_annuel/plafond_jours_ouvrables/adultes": (
        "Congé annuel, plafond en jours ouvrables, 21 ans et plus",
        "الرخصة السنوية، السقف بأيام العمل، 21 سنة فأكثر"),
    f"{TT}/conge_annuel/plafond_jours_ouvrables/de_18_a_20_ans": (
        "Congé annuel, plafond en jours ouvrables, 18 à 20 ans",
        "الرخصة السنوية، السقف بأيام العمل، من 18 إلى 20 سنة"),
    f"{TT}/conge_annuel/plafond_jours_ouvrables/moins_18_ans": (
        "Congé annuel, plafond en jours ouvrables, moins de 18 ans",
        "الرخصة السنوية، السقف بأيام العمل، أقل من 18 سنة"),
    f"{TT}/conge_annuel/plafond_jours/adultes": (
        "Congé annuel, plafond en jours, 21 ans et plus",
        "الرخصة السنوية، السقف بالأيام، 21 سنة فأكثر"),
    f"{TT}/conge_annuel/plafond_jours/de_18_a_20_ans": (
        "Congé annuel, plafond en jours, 18 à 20 ans",
        "الرخصة السنوية، السقف بالأيام، من 18 إلى 20 سنة"),
    f"{TT}/conge_annuel/plafond_jours/moins_18_ans": (
        "Congé annuel, plafond en jours, moins de 18 ans",
        "الرخصة السنوية، السقف بالأيام، أقل من 18 سنة"),
    f"{TT}/conge_annuel/anciennete/jours_ouvrables_par_periode": (
        "Congé d'ancienneté, jours par période", "رخصة الأقدمية، الأيام عن كل فترة"),
    f"{TT}/conge_annuel/anciennete/duree_periode": (
        "Congé d'ancienneté, durée de la période", "رخصة الأقدمية، مدة الفترة"),
    f"{TT}/conge_annuel/anciennete/plafond_total_jours_ouvrables": (
        "Congé d'ancienneté, plafond total", "رخصة الأقدمية، السقف الجملي"),
    f"{TT}/conge_annuel/indemnite_diviseur/adultes": (
        "Indemnité de congé, diviseur, 21 ans et plus", "منحة الرخصة، المقسوم عليه، 21 سنة فأكثر"),
    f"{TT}/conge_paternite/duree": ("Congé de paternité, durée", "عطلة الأبوة، المدة"),
    f"{TT}/jours_feries/nombre": ("Nombre de jours fériés payés de la loi",
                                  "عدد أيام عطلة خالصة الأجر بحكم القانون"),
    f"{TT}/jours_feries/liste": ("Liste des jours fériés payés de la loi",
                                 "قائمة أيام عطلة خالصة الأجر بحكم القانون"),
    f"{TT}/jours_feries/indemnite_jour_ferie_travaille": (
        "Indemnité du jour férié travaillé, code du travail",
        "منحة يوم العيد المشغول، مجلة الشغل"),
    f"{TT}/convention_cadre/jours_feries": ("Jours fériés payés de la convention cadre",
                                            "أيام عطلة خالصة الأجر بالاتفاقية المشتركة الإطارية"),
    f"{TT}/convention_cadre/majoration_jour_ferie_travaille": (
        "Majoration du jour férié travaillé, convention cadre",
        "زيادة يوم العيد المشغول، الاتفاقية المشتركة الإطارية"),
}


def _libelle(chemin: str) -> dict[str, str]:
    fr, ar = LIB[chemin]
    return {"fr": fr, "ar": ar}


def lire(chemin: str, date: str, formateur) -> ot.Lecture:
    """Lecture de la série en vigueur à `date` ; échoue si la valeur est vide."""
    classe = LectureListe if chemin.endswith("/jours_feries/liste") else ot.Lecture
    return classe(f"{chemin}.yaml", date, formateur, _libelle(chemin))


def close(chemin: str, date: str, langue: str) -> None:
    """Contrôle que la série de `chemin` est CLOSE (valeur vide) à `date`, et la relève."""
    point = ot.en_vigueur(ot.serie_datee(f"{chemin}.yaml"), date)
    if point is None or point[1] is not None:
        raise ValueError(f"{chemin} : la série devrait être close au {date}, "
                         f"elle porte {point}")
    ot.releve_note(f"{chemin}.yaml", _libelle(chemin)[langue])


def vide_avant(chemin: str, date: str) -> None:
    """Contrôle que la série de `chemin` n'a pas commencé à `date` (case « — »)."""
    if ot.en_vigueur(ot.serie_datee(f"{chemin}.yaml"), date) is not None:
        raise ValueError(f"{chemin} : la série a commencé avant le {date}")


def _signature(case):
    """Contenu d'une case de gabarit : son texte et les valeurs lues, sans les dates."""
    _g, texte, lectures = case
    return (str(texte), tuple((n, l.chemin, l.valeur()) for n, l in lectures.items()))


def compacter(cases: list, mot: dict[str, str]) -> list:
    """Remplace par `mot` toute case de gabarit identique à la dernière case de gabarit."""
    sortie, precedente = [], None
    for case in cases:
        if isinstance(case, tuple) and case and case[0] == "gabarit":
            signature = _signature(case)
            sortie.append(mot if signature == precedente else case)
            precedente = signature
        else:
            sortie.append(case)
    return sortie


def g(fr: str, ar: str, **lectures):
    return ot.gabarit({"fr": fr, "ar": ar}, **lectures)


def h(fr: str, ar: str | None = None) -> dict[str, str]:
    """Case écrite à la main."""
    return {"fr": fr, "ar": ar if ar is not None else fr}


IDEM = {"fr": "idem", "ar": "مثله"}
VIDE_CASE = h("—")


def entete_date(date: str, etiquette: dict[str, str] | None, langue: str,
                ancre: str | None = None) -> str:
    texte = ot.formate_date(date, langue)
    texte = f"[{texte}]{{.insecable}}" if langue == "fr" else texte
    if etiquette:
        texte += "<br>" + (f"[{etiquette[langue]}](#{ancre})" if ancre else etiquette[langue])
    return texte


# --- rupture du contrat : grandeurs aux dates des réformes
RC_COLONNES = [
    ("1966-05-01", {"fr": "code", "ar": "المجلة"}, "r-mt-rc-loi-1966"),
    ("1973-06-01", {"fr": "convention cadre", "ar": "الاتفاقية المشتركة الإطارية"}, "r-mt-rc-loi-1973"),
    ("1994-03-01", {"fr": "loi n° 94-29", "ar": "القانون عدد 94-29"}, "r-mt-rc-loi-1994"),
    ("1996-07-31", {"fr": "loi n° 96-62", "ar": "القانون عدد 96-62"}, "r-mt-rc-loi-1996"),
    ("2025-05-24", {"fr": "loi n° 2025-9", "ar": "القانون عدد 2025-9"}, "r-mt-rc-loi-2025"),
]
D66, D73, D94, D96, D25 = (c[0] for c in RC_COLONNES)


def _ligne_rc(libelle: dict, cases: list, mot: dict | None = None) -> tuple:
    return libelle, compacter(cases, mot) if mot else cases


def rc_parametres(langue: str):
    P = f"{RC}/preavis"
    GF = f"{RC}/gratification_fin_service"
    DI = f"{RC}/dommages_interets"
    inch_m = {"fr": "inchangé", "ar": "دون تغيير"}
    inch_f = {"fr": "inchangée", "ar": "دون تغيير"}
    inch_p = {"fr": "inchangés", "ar": "دون تغيير"}

    lignes = [
        ({"fr": "Préavis", "ar": "أجل الإعلام"}, compacter([
            g("{m} (salariés payés au mois) ; {j} (autres)",
              "{m} (الأجراء الخالصون بالشهر)؛ {j} (غيرهم)",
              m=lire(f"{P}/duree", D66, F_MOIS),
              j=lire(f"{P}/duree_salaries_non_mensuels", D66, F_JOURS)),
            h("délai des conventions de branche, à défaut celui de la loi",
              "أجل الاتفاقيات القطاعية، وفي غيابه أجل القانون"),
            (close(f"{P}/duree_salaries_non_mensuels", D94, langue) or
             g("{m} pour tous", "{m} للجميع", m=lire(f"{P}/duree", D94, F_MOIS))),
            g("{m} pour tous", "{m} للجميع", m=lire(f"{P}/duree", D96, F_MOIS)),
            g("{m} pour tous", "{m} للجميع", m=lire(f"{P}/duree", D25, F_MOIS)),
        ], inch_m)),
        ({"fr": "Gratification de fin de service<br>(taux et plafond)",
          "ar": "مكافأة نهاية الخدمة<br>(النسبة والسقف)"}, compacter([
            g("{j} de salaire par mois de services effectifs ; plafond de {p} de salaire",
              "{j} من الأجر عن كل شهر من الخدمة الفعلية؛ السقف {p} من الأجر",
              j=lire(f"{GF}/jours_par_mois_service", D66, F_JOURS),
              p=lire(f"{GF}/plafond", D66, F_MOIS)),
            h("calcul renvoyé aux conventions de branche", "الاحتساب محال على الاتفاقيات القطاعية"),
            *[g("{j} de salaire par mois de services effectifs ; plafond de {p} de salaire",
                "{j} من الأجر عن كل شهر من الخدمة الفعلية؛ السقف {p} من الأجر",
                j=lire(f"{GF}/jours_par_mois_service", d, F_JOURS),
                p=lire(f"{GF}/plafond", d, F_MOIS)) for d in (D94, D96, D25)],
        ], inch_p)),
        ({"fr": "Gratification<br>(condition)", "ar": "المكافأة<br>(الشرط)"}, compacter([
            g("{m} de services ; hors faute lourde", "{m} من الخدمة؛ باستثناء الخطأ الجسيم",
              m=lire(f"{GF}/anciennete_minimale", D66, F_MOIS)),
            h("inchangée", "دون تغيير"),
            *[(close(f"{GF}/anciennete_minimale", d, langue) or
               g("après la période d'essai ; hors faute grave",
                 "بعد انقضاء فترة التجربة؛ باستثناء الخطأ الفادح")) for d in (D94, D96, D25)],
        ], inch_f)),
        ({"fr": "Dommages-intérêts<br>(licenciement abusif)",
          "ar": "الغرامات<br>(الطرد التعسفي)"}, compacter([
            h("appréciés par le juge", "يقدّرها القاضي"),
            h("inchangés", "دون تغيير"),
            *[g("{a} à {b} mois de salaire par année d'ancienneté ; plafond de {p} de salaire",
                "أجر من {a} إلى {b} عن كل سنة أقدمية؛ السقف {p} من الأجر",
                a=lire(f"{DI}/minimum_par_annee_anciennete", d, F_MOIS_BORNE),
                b=lire(f"{DI}/maximum_par_annee_anciennete", d, F_MOIS_BORNE),
                p=lire(f"{DI}/plafond", d, F_ANS_DE_MOIS)) for d in (D94, D96, D25)],
        ], inch_p)),
        ({"fr": "Dommages-intérêts<br>(vice de procédure seul)",
          "ar": "الغرامات<br>(خرق الإجراءات فقط)"}, compacter([
            VIDE_CASE, VIDE_CASE,
            *[g("{a} à {b} mois de salaire", "أجر من {a} إلى {b}",
                a=lire(f"{DI}/vice_procedure_minimum", d, F_MOIS_BORNE),
                b=lire(f"{DI}/vice_procedure_maximum", d, F_MOIS_BORNE)) for d in (D94, D96, D25)],
        ], inch_p)),
        ({"fr": "Contrat à durée déterminée<br>(hors cas de recours)",
          "ar": "عقد الشغل لمدة معينة<br>(خارج حالات اللجوء إليه)"}, [
            h("ni cas ni durée", "لا حالات ولا مدة"),
            h("inchangé", "دون تغيير"),
            h("inchangé", "دون تغيير"),
            g("{a} au plus, renouvellements compris", "{a} على الأكثر، بما في ذلك التجديدات",
              a=lire(f"{RC}/contrat_duree_determinee/duree_maximale_hors_cas_recours", D96,
                     F_ANS_DE_MOIS)),
            (close(f"{RC}/contrat_duree_determinee/duree_maximale_hors_cas_recours", D25, langue) or
             h("interdit ; trois cas de recours, sans durée maximale",
               "ممنوع؛ ثلاث حالات للجوء إليه، دون مدة قصوى")),
        ]),
        ({"fr": "Période d'essai", "ar": "فترة التجربة"}, [
            h("renvoyée aux conventions, à l'usage ou à la loi",
              "محالة على الاتفاقيات أو العرف أو القانون"),
            h("3 mois, renouvelable une fois", "3 أشهر، قابلة للتجديد مرة واحدة"),
            h("inchangée", "دون تغيير"),
            h("inchangée", "دون تغيير"),
            g("{d} au plus, renouvelable {n}", "{d} على الأكثر، قابلة للتجديد {n}",
              d=lire(f"{RC}/periode_essai/duree_maximale", D25, F_MOIS),
              n=lire(f"{RC}/periode_essai/renouvellements_maximum", D25, _fois)),
        ]),
    ]
    entetes = [{"fr": "Grandeur", "ar": "المقدار"}[langue]] + [
        entete_date(d, e, langue, a) for d, e, a in RC_COLONNES]
    return ot.tableau_gabarit(entetes, [[lib[langue]] + cases for lib, cases in lignes], langue)


# --- temps de travail : grandeurs aux dates repères
TT_COLONNES = [
    ("1966-05-01", {"fr": "code", "ar": "المجلة"}, "r-mt-tt-loi-1966"),
    ("1973-06-01", {"fr": "convention cadre", "ar": "الاتفاقية المشتركة الإطارية"}, "r-mt-tt-cc-1973"),
    ("1984-11-17", {"fr": "avenant n° 1", "ar": "الملحق التعديلي عدد 1"}, "r-mt-tt-feries-1984"),
    ("1988-06-05", {"fr": "loi n° 88-55", "ar": "القانون عدد 88-55"}, "r-mt-tt-feries-1988"),
    ("1996-07-31", {"fr": "loi n° 96-62", "ar": "القانون عدد 96-62"}, "r-mt-tt-loi-1996"),
    (EFFET_2026, None, None),
]
TDATES = [c[0] for c in TT_COLONNES]
T66 = TDATES[0]
T96 = TDATES[4]
DU = f"{TT}/duree"
HS = f"{TT}/heures_supplementaires"
CA = f"{TT}/conge_annuel"
JF = f"{TT}/jours_feries"
CC = f"{TT}/convention_cadre"


def tt_parametres(langue: str):
    lignes = []

    lignes.append(({"fr": "Durée maximale<br>(par semaine)", "ar": "المدة القصوى<br>(في الأسبوع)"},
                   [g("{h}", "{h}", h=lire(f"{DU}/hebdomadaire_maximale", d, F_HEURES))
                    for d in TDATES]))

    def reduction(d):
        if d < T96:
            return g("à {p}, par décret", "إلى {p}، بأمر",
                     p=lire(f"{DU}/hebdomadaire_plancher_reduction", d, F_HEURES))
        return g("jusqu'à {p}, par convention ou texte réglementaire",
                 "إلى حدود {p}، باتفاقية أو بنص ترتيبي",
                 p=lire(f"{DU}/hebdomadaire_plancher_reduction", d, F_HEURES))
    lignes.append(({"fr": "Réduction possible", "ar": "التخفيض الممكن"},
                   compacter([reduction(d) for d in TDATES], IDEM)))

    def maj48(d):
        t = lire(f"{HS}/regime_48h", d, F_TAUX)
        return (g("{t}", "{t}", t=t) if d < T96 else
                g("{t} du salaire de base horaire", "{t} من الأجر الأساسي بالساعة", t=t))
    lignes.append(({"fr": "Majoration<br>(régime de 48 heures)",
                    "ar": "الزيادة<br>(نظام 48 ساعة)"},
                   [maj48(d) for d in TDATES if d < T96]
                   + compacter([maj48(d) for d in TDATES if d >= T96], IDEM)))

    def majcourt(d):
        if d < T96:
            return g("régime de 40 heures : {a} les {n} premières heures supplémentaires, {b} au-delà",
                     "نظام 40 ساعة: {a} للساعات الإضافية {n} الأولى، و{b} بعدها",
                     a=lire(f"{HS}/regime_40h/taux_premieres_heures", d, F_TAUX),
                     n=lire(f"{HS}/regime_40h/nombre_premieres_heures", d, F_ENTIER_LETTRES),
                     b=lire(f"{HS}/regime_40h/taux_heures_suivantes", d, F_TAUX))
        R = f"{HS}/regimes_inferieurs_48h"
        return g("{a} jusqu'à {s}, {b} au-delà", "{a} إلى حدود {s}، و{b} بعدها",
                 a=lire(f"{R}/taux_jusqu_au_seuil", d, F_TAUX),
                 s=lire(f"{R}/seuil", d, F_HEURES),
                 b=lire(f"{R}/taux_au_dela_du_seuil", d, F_TAUX))
    lignes.append(({"fr": "Majoration<br>(régimes de moins de 48 heures)",
                    "ar": "الزيادة<br>(الأنظمة الأقل من 48 ساعة)"},
                   compacter([majcourt(d) for d in TDATES], IDEM)))

    cases = []
    for d in TDATES:
        if d < T96:
            vide_avant(f"{HS}/temps_partiel", d)
            cases.append(VIDE_CASE)
        else:
            cases.append(g("{t}", "{t}", t=lire(f"{HS}/temps_partiel", d, F_TAUX)))
    lignes.append(({"fr": "Majoration<br>(temps partiel)", "ar": "الزيادة<br>(العمل لوقت جزئي)"},
                   cases))

    lignes.append(({"fr": "Congé annuel<br>(adultes)", "ar": "الرخصة السنوية<br>(الراشدون)"},
                   compacter([g("{j} par mois, {p} au plus",
                                "{j} عن كل شهر، {p} على الأكثر",
                                j=lire(f"{CA}/jours_par_mois/adultes", d, F_JOURS_OUVRABLES),
                                p=lire(f"{CA}/plafond_jours_ouvrables/adultes", d,
                                       F_JOURS_OUVRABLES)) for d in TDATES], IDEM)))

    def indemnite(d):
        D = f"{CA}/indemnite_diviseur/adultes"
        if d < T96:
            return g("{q} de la rémunération de la période", "{q} من أجر الفترة",
                     q=lire(D, d, F_DIVISEUR))
        close(D, d, langue)
        return g("salaire et indemnités habituels", "الأجر والمنح المعتادة")
    lignes.append(({"fr": "Indemnité de congé<br>(loi)", "ar": "منحة الرخصة<br>(القانون)"},
                   compacter([indemnite(d) for d in TDATES], IDEM)))

    lignes.append(({"fr": "Traitement pendant le congé<br>(convention cadre)",
                    "ar": "الأجر خلال الرخصة<br>(الاتفاقية المشتركة الإطارية)"},
                   [VIDE_CASE, h("intégral", "كامل")] + [IDEM] * 4))

    lignes.append(({"fr": "Jours fériés payés<br>(loi)", "ar": "أيام عطلة خالصة الأجر<br>(القانون)"},
                   [g("{n}", "{n}", n=lire(f"{JF}/nombre", d, F_ENTIER)) for d in TDATES]))

    cases = []
    for d in TDATES:
        if d < "1973-06-01":
            vide_avant(f"{CC}/jours_feries", d)
            cases.append(VIDE_CASE)
        else:
            cases.append(g("{n}", "{n}", n=lire(f"{CC}/jours_feries", d, F_ENTIER)))
    lignes.append(({"fr": "Jours fériés payés<br>(convention cadre)",
                    "ar": "أيام عطلة خالصة الأجر<br>(الاتفاقية المشتركة الإطارية)"}, cases))

    entetes = [{"fr": "Grandeur", "ar": "المقدار"}[langue]] + [
        entete_date(d, e, langue, a) for d, e, a in TT_COLONNES]
    return ot.tableau_gabarit(entetes, [[lib[langue]] + cases for lib, cases in lignes], langue)


# --- temps de travail : règles au 1er janvier 2026
def lien_art(fr: str, ar: str, ancre: str) -> dict[str, str]:
    return {"fr": f"[{fr}](#{ancre})", "ar": f"[{ar}](#{ancre})"}


def tt_etat_du_droit(langue: str):
    e = EFFET_2026
    code = h("salariés non agricoles régis par le code", "الأجراء غير الفلاحيين الخاضعون للمجلة")
    meme = h("idem", "مثله")
    regis = h("salariés régis par le code", "الأجراء الخاضعون للمجلة")
    A = f"{CA}/jours_par_mois"
    Pl = f"{CA}/plafond_jours_ouvrables"
    R = f"{HS}/regimes_inferieurs_48h"
    for age in ("adultes", "de_18_a_20_ans", "moins_18_ans"):
        pass
    close(f"{CA}/indemnite_diviseur/adultes", e, langue)
    lignes = [
        [h("Durée maximale", "المدة القصوى"),
         g("{h} par semaine, réductible jusqu'à {p}", "{h} في الأسبوع، قابلة للتخفيض إلى {p}",
           h=lire(f"{DU}/hebdomadaire_maximale", e, F_HEURES),
           p=lire(f"{DU}/hebdomadaire_plancher_reduction", e, F_HEURES)),
         lien_art("art. 79", "الفصل 79", "r-mt-tt-duree-1996"), code],
        [h("Plafond hebdomadaire", "السقف الأسبوعي"),
         g("{h}, heures supplémentaires comprises", "{h}، بما في ذلك الساعات الإضافية",
           h=lire(f"{DU}/hebdomadaire_plafond_heures_supplementaires", e, F_HEURES)),
         lien_art("art. 93", "الفصل 93", "r-mt-tt-plafond-1966"), meme],
        [h("Majoration<br>(régime de 48 heures)", "الزيادة<br>(نظام 48 ساعة)"),
         g("{t} du salaire de base horaire", "{t} من الأجر الأساسي بالساعة",
           t=lire(f"{HS}/regime_48h", e, F_TAUX)),
         lien_art("art. 90", "الفصل 90", "r-mt-tt-hs-1996"), meme],
        [h("Majoration<br>(régimes plus courts)", "الزيادة<br>(الأنظمة الأقصر)"),
         g("{a} jusqu'à {s}, {b} au-delà", "{a} إلى حدود {s}، و{b} بعدها",
           a=lire(f"{R}/taux_jusqu_au_seuil", e, F_TAUX), s=lire(f"{R}/seuil", e, F_HEURES),
           b=lire(f"{R}/taux_au_dela_du_seuil", e, F_TAUX)),
         lien_art("art. 90", "الفصل 90", "r-mt-tt-hs-1996"),
         h("salariés des branches à durée réduite", "أجراء القطاعات ذات المدة المخفضة")],
        [h("Majoration<br>(temps partiel)", "الزيادة<br>(العمل لوقت جزئي)"),
         g("{t}", "{t}", t=lire(f"{HS}/temps_partiel", e, F_TAUX)),
         lien_art("art. 90 et 94-6", "الفصلان 90 و94-6", "r-mt-tt-tp-1996"),
         h("salariés à temps partiel", "الأجراء لوقت جزئي")],
        [h("Durée et majoration<br>(agriculture)", "المدة والزيادة<br>(الفلاحة)"),
         g("{h} par an ; {t}", "{h} في السنة؛ {t}",
           h=lire(f"{DU}/agriculture_annuelle_maximale", e, F_MILLIERS),
           t=lire(f"{HS}/agriculture", e, F_TAUX)),
         lien_art("art. 88 et 94", "الفصلان 88 و94", "r-mt-tt-agri-1966"),
         h("salariés agricoles", "الأجراء الفلاحيون")],
        [h("Congé annuel<br>(adultes)", "الرخصة السنوية<br>(الراشدون)"),
         g("{j} par mois, {p} au plus", "{j} عن كل شهر، {p} على الأكثر",
           j=lire(f"{A}/adultes", e, F_JOURS_OUVRABLES),
           p=lire(f"{Pl}/adultes", e, F_JOURS_OUVRABLES)),
         lien_art("art. 113", "الفصل 113", "r-mt-tt-conge-1996"), regis],
        [h("Congé annuel<br>(moins de 18 ans ; 18 à 20 ans)",
           "الرخصة السنوية<br>(أقل من 18 سنة؛ من 18 إلى 20 سنة)"),
         g("{j1} par mois, {p1} au plus ; {j2}, {p2} au plus",
           "{j1} عن كل شهر، {p1} على الأكثر؛ {j2}، {p2} على الأكثر",
           j1=lire(f"{A}/moins_18_ans", e, F_JOURS_DEC),
           p1=lire(f"{Pl}/moins_18_ans", e, F_JOURS_OUVRABLES),
           j2=lire(f"{A}/de_18_a_20_ans", e, F_JOURS_DEC),
           p2=lire(f"{Pl}/de_18_a_20_ans", e, F_ENTIER)),
         lien_art("art. 113", "الفصل 113", "r-mt-tt-conge-1996"), meme],
        [h("Congé d'ancienneté", "رخصة الأقدمية"),
         g("{j} par {d}, {p} au plus au total", "{j} عن كل {d}، {p} على الأكثر في المجموع",
           j=lire(f"{CA}/anciennete/jours_ouvrables_par_periode", e, F_JOURS_OUVRABLES),
           d=lire(f"{CA}/anciennete/duree_periode", e, F_PAR_PERIODE),
           p=lire(f"{CA}/anciennete/plafond_total_jours_ouvrables", e, F_JOURS_OUVRABLES)),
         lien_art("art. 115", "الفصل 115", "r-mt-tt-conge-1966"), meme],
        [h("Indemnité de congé", "منحة الرخصة"),
         h("salaire et indemnités habituels", "الأجر والمنح المعتادة"),
         lien_art("art. 119", "الفصل 119", "r-mt-tt-conge-1996"), meme],
        [h("Jours fériés payés<br>(loi)", "أيام عطلة خالصة الأجر<br>(القانون)"),
         g("{n} : {l}", "{n}: {l}", n=lire(f"{JF}/nombre", e, F_ENTIER),
           l=lire(f"{JF}/liste", e, _liste_feries)),
         lien_art("art. 445", "الفصل 445", "r-mt-tt-feries-2021"), meme],
        [h("Jours fériés payés<br>(convention cadre)",
           "أيام عطلة خالصة الأجر<br>(الاتفاقية المشتركة الإطارية)"),
         g("{n}", "{n}", n=lire(f"{CC}/jours_feries", e, F_ENTIER)),
         lien_art("avenant n° 2", "الملحق التعديلي عدد 2", "r-mt-tt-feries-1992"),
         h("salariés couverts par la convention cadre (@sec-mt-cc-couverture)",
           "الأجراء المشمولون بالاتفاقية المشتركة الإطارية (@sec-mt-cc-couverture)")],
        [h("Jour férié travaillé", "يوم العيد المشغول"),
         g("code : indemnité {i}, en plus du salaire, dans les activités continues ; "
           "convention cadre : majoration de {m}",
           "المجلة: منحة {i}، علاوة على الأجر، في الأنشطة المستمرة؛ "
           "الاتفاقية المشتركة الإطارية: زيادة بنسبة {m}",
           i=lire(f"{JF}/indemnite_jour_ferie_travaille", e, _indemnite_ferie),
           m=lire(f"{CC}/majoration_jour_ferie_travaille", e, F_TAUX)),
         {"fr": "[art. 109](#r-mt-tt-feries-paiement) ; [art. 29](#r-mt-tt-feries-1973)",
          "ar": "[الفصل 109](#r-mt-tt-feries-paiement)؛ [الفصل 29](#r-mt-tt-feries-1973)"},
         h("salariés des activités continues ; salariés couverts par la convention cadre",
           "أجراء الأنشطة المستمرة؛ الأجراء المشمولون بالاتفاقية المشتركة الإطارية")],
        [h("Congé de paternité", "عطلة الأبوة"),
         g("{d}", "{d}", d=lire(f"{TT}/conge_paternite/duree", e, F_JOURS)),
         lien_art("loi n° 2024-44", "القانون عدد 2024-44", "r-mt-tt-paternite-2024"),
         h("salariés affiliés à la caisse (@sec-mt-tt-conges-familiaux)",
           "الأجراء المنخرطون بالصندوق (@sec-mt-tt-conges-familiaux)")],
        [h("Travail domestique", "العمل المنزلي"),
         h("employeur unique : 48 heures par semaine, 10 heures par jour ; 1 jour de congé par mois",
           "مؤجر وحيد: 48 ساعة في الأسبوع، 10 ساعات في اليوم؛ يوم رخصة عن كل شهر"),
         {"fr": "[art. 13 et 19](#r-mt-tt-dom-duree) ; [art. 14](#r-mt-tt-dom-conge)",
          "ar": "[الفصلان 13 و19](#r-mt-tt-dom-duree)؛ [الفصل 14](#r-mt-tt-dom-conge)"},
         h("travailleurs domestiques", "العمال المنزليون")],
    ]
    entetes = [
        {"fr": "Règle", "ar": "القاعدة"}[langue],
        ({"fr": f"Valeur au [{ot.formate_date(e, 'fr')}]{{.insecable}}",
          "ar": f"القيمة في {ot.formate_date(e, 'ar')}"}[langue]),
        {"fr": "Texte", "ar": "النص"}[langue],
        {"fr": "Population couverte", "ar": "الفئة المشمولة"}[langue],
    ]
    return ot.tableau_gabarit(entetes, lignes, langue)


# --- temps de travail : le congé annuel selon l'âge
def tt_conge(langue: str):
    e = EFFET_2026
    # Une seule valeur par case : elle doit valoir à chacune des deux dates du tableau.
    ages = [
        ("moins_18_ans", {"fr": "Moins de 18 ans", "ar": "أقل من 18 سنة"}),
        ("de_18_a_20_ans", {"fr": "18 à 20 ans", "ar": "من 18 إلى 20 سنة"}),
        ("adultes", {"fr": "21 ans et plus", "ar": "21 سنة فأكثر"}),
    ]
    for age, _ in ages:
        for rubrique in ("jours_par_mois", "plafond_jours_ouvrables", "plafond_jours"):
            valeurs = {ot.en_vigueur(ot.serie_datee(f"{CA}/{rubrique}/{age}.yaml"), d)[1]
                       for d in ("1966-05-01", "1996-07-31", e)}
            if len(valeurs) != 1:
                raise ValueError(f"{CA}/{rubrique}/{age} : valeur changeante {valeurs}")
    apprecie = {
        "moins_18_ans": h("31 mai (1966) → 31 décembre (1996)", "31 ماي (1966) ← 31 ديسمبر (1996)"),
        "de_18_a_20_ans": h("31 mai (1966) → 31 décembre (1996)", "31 ماي (1966) ← 31 ديسمبر (1996)"),
        "adultes": h("—"),
    }
    lignes = []
    for age, nom in ages:
        lignes.append([
            nom,
            g("{j}", "{j}", j=lire(f"{CA}/jours_par_mois/{age}", e, F_DECIMAL)),
            g("{p}", "{p}", p=lire(f"{CA}/plafond_jours_ouvrables/{age}", e, F_ENTIER)),
            g("{p}", "{p}", p=lire(f"{CA}/plafond_jours/{age}", e, F_ENTIER)),
            apprecie[age],
        ])
    entetes = [{"fr": x, "ar": y}[langue] for x, y in [
        ("Âge", "السن"), ("Jours par mois", "الأيام عن كل شهر"),
        ("Plafond<br>(jours ouvrables)", "السقف<br>(أيام العمل)"),
        ("Plafond<br>(jours)", "السقف<br>(الأيام)"), ("Âge apprécié au", "السن المعتبرة في")]]
    return ot.tableau_gabarit(entetes, lignes, langue)


# --- temps de travail : jours fériés payés, une ligne par date d'effet
FERIES_TEXTES = {
    "1966-05-01": ("code du travail", "مجلة الشغل", "r-mt-tt-feries-1966"),
    "1973-06-01": ("convention cadre", "الاتفاقية المشتركة الإطارية", "r-mt-tt-feries-1973"),
    "1984-11-17": ("avenant n° 1", "الملحق التعديلي عدد 1", "r-mt-tt-feries-1984"),
    "1988-06-05": ("loi n° 88-55", "القانون عدد 88-55", "r-mt-tt-feries-1988"),
    "1991-03-07": ("loi n° 91-15", "القانون عدد 91-15", "r-mt-tt-feries-1991"),
    "1992-10-15": ("avenant n° 2", "الملحق التعديلي عدد 2", "r-mt-tt-feries-1992"),
    "2011-06-16": ("décret-loi n° 2011-51", "المرسوم عدد 2011-51", "r-mt-tt-feries-2011"),
    "2021-12-15": ("décret-loi n° 2021-11", "المرسوم عدد 2021-11", "r-mt-tt-feries-2021"),
}
# Loi n° 91-15 : le JORT porte « 1er et 5 mars 1991 » ; la série est vide du 3 au 6 mars et vaut
# 6 dès le 7 mars, premier jour certain. Le tableau écrit « mars 1991 ».
FERIES_1991 = ("1991-03-03", "1991-03-07")


def tt_feries(langue: str):
    series = {c: ot.serie_datee(f"{c}.yaml") for c in (f"{JF}/nombre", f"{CC}/jours_feries")}
    dates = sorted({d for s in series.values() for d, *_ in s} - {FERIES_1991[0]})
    attendues = set(FERIES_TEXTES)
    if set(dates) != attendues:
        raise ValueError(f"jours fériés : dates {sorted(set(dates) ^ attendues)} sans texte "
                         "ou sans valeur ; compléter FERIES_TEXTES")
    lignes = [[
        h("[2 janvier 1964]{.insecable}", "2 جانفي 1964"),
        {"fr": "[loi n° 63-55](#r-mt-tt-1963-feries)",
         "ar": "[القانون عدد 63-55](#r-mt-tt-1963-feries)"},
        h("4"), VIDE_CASE]]
    for d in dates:
        fr, ar, ancre = FERIES_TEXTES[d]
        if d == FERIES_1991[1]:
            date = h("mars 1991", "مارس 1991")
        else:
            date = {"fr": f"[{ot.formate_date(d, 'fr')}]{{.insecable}}",
                    "ar": ot.formate_date(d, "ar")}
        if ot.en_vigueur(series[f"{CC}/jours_feries"], d) is None:
            vide_avant(f"{CC}/jours_feries", d)
            conv = VIDE_CASE
        else:
            conv = g("{n}", "{n}", n=lire(f"{CC}/jours_feries", d, F_ENTIER))
        lignes.append([date, {"fr": f"[{fr}](#{ancre})", "ar": f"[{ar}](#{ancre})"},
                       g("{n}", "{n}", n=lire(f"{JF}/nombre", d, F_ENTIER)), conv])
    entetes = [{"fr": x, "ar": y}[langue] for x, y in [
        ("Date d'effet", "تاريخ النفاذ"), ("Texte", "النص"), ("Loi", "القانون"),
        ("Convention cadre", "الاتفاقية المشتركة الإطارية")]]
    return ot.tableau_gabarit(entetes, lignes, langue)


TABLEAUX_DROIT_TRAVAIL = [
    ("mt_rc_parametres", rc_parametres, f"{RC}/*"),
    ("mt_tt_parametres", tt_parametres, f"{TT}/*"),
    ("mt_tt_etat_du_droit", tt_etat_du_droit, f"{TT}/*"),
    ("mt_tt_conge", tt_conge, f"{CA}/*"),
    ("mt_tt_feries", tt_feries, f"{JF}/*, {CC}/jours_feries"),
]


def tableaux_droit_travail(langue: str) -> int:
    for nom, fabrique, lus in TABLEAUX_DROIT_TRAVAIL:
        try:
            df, liens = ot.avec_liens(lambda: fabrique(langue))
        except ValueError as erreur:
            print(f"✗ {langue}/{nom}.md : {erreur}")
            return 1
        if df is None or df.empty:
            print(f"✗ {langue}/{nom}.md : paramètre introuvable ou vide.")
            return 1
        ot.ecrire_tableau(
            RACINE / langue / LIVRE / "tables" / f"{nom}.md", df, liens, langue,
            entete="<!-- Généré par scripts/generate_marche_travail_tables.py — ne pas éditer "
                   f"à la main.\n     Paramètres : {lus} -->\n\n")
    print(f"✓ {langue} : {len(TABLEAUX_DROIT_TRAVAIL)} tableaux du droit du travail")
    return 0


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    for langue in LANGUES:
        code = ecrire_decoupe(langue, "smig", lambda: tableau_smig(langue),
                              list(SMIG.values()), PERIODES_SMIG)
        code = code or ecrire_decoupe(langue, "smag", lambda: tableau_smag(langue),
                                      [SMAG], PERIODES_SMAG)
        if code:
            return code
        df, liens = ot.avec_liens(lambda: tableau_indemnites(langue))
        if df is None or df.empty:
            print(f"✗ {langue}/indemnites_speciales.md : paramètre introuvable ou vide.")
            return 1
        erreur = ot.ecrire_dans_livres(RACINE, langue, (LIVRE,), "indemnites_speciales.md",
                                       df, liens)
        if erreur:
            print(erreur)
            return 1
        print(f"✓ {langue} : SMIG ({len(PERIODES_SMIG)} périodes), SMAG "
              f"({len(PERIODES_SMAG)} périodes), indemnités spéciales")
        if tableaux_droit_travail(langue):
            return 1
    # Les grilles des conventions collectives de branche : un générateur à part, qui
    # parcourt son nœud sans nommer de branche ; lancé d'ici pour être gardé par le
    # contrôle de fraîcheur, qui n'appelle que ce script pour le livre.
    return serie_figures() or conventions.main()


if __name__ == "__main__":
    raise SystemExit(main())
