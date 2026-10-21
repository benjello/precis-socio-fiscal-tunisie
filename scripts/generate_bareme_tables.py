"""Régénère les snapshots Markdown des tableaux de paramètres du livre « Fiscalité ».

Le build du site n'exécute PAS ce script : il lit les fichiers qu'il produit, versionnés
dans `precis/fr/fiscalite/tables/`. Le lancer suppose une copie d'openfisca-tunisia :

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_bareme_tables.py

Deux familles de tableaux :
  - les BARÈMES à tranches (IRPP et contribution personnelle d'État) ;
  - les SÉRIES de paramètres scalaires (abattements, déductions, plafonds), dont la colonne
    « Texte » est tirée des métadonnées `reference` du paramètre lui-même. Le tableau publié
    et le paramètre sont ainsi indissociables : corriger l'un corrige l'autre.

LES PARAMÈTRES DANS LE TEMPS. Une liste déclarée de paramètres (`ot.ParametreDate`) donne
deux sorties, par `ot.ecrire_serie_parametres` et `ot.ecrire_dates_reperes` :
  - une SÉRIE pour une figure en escalier, `precis/_seriescache/<nom>.csv` — une ligne par
    paramètre et par date d'effet —, avec ses liens « Base législative » dans
    `<nom>.liens.<langue>.yml`. Le build du site ne lit pas openfisca : la figure lit ce
    snapshot par `figtools.series()` ;
  - le tableau de l'état du droit à des dates repères, `tables/<nom>_dates_reperes.md`.
Deux déclarations : les taux de la TVA (`tva-taux`, dont la série porte le texte de chaque
date) et les déductions pour charges de famille de l'impôt sur le revenu
(`irpp-deductions-famille`).

Exige openfisca-tunisia >= 0.71 : c'est la version où les paramètres d'assiette ont été
corrigés et où les tarifs de la contribution personnelle d'État ont été ajoutés.
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

BAREME = "parameters/impot_revenu/bareme.yaml"
BAREME_CPE = "parameters/impot_revenu/contribution_personnelle_etat/bareme.yaml"
RACINE = Path(__file__).parent.parent / "precis"
LANGUES = ("fr", "ar")

# En-têtes de colonnes. Le reste du tableau — montants, taux, bornes de tranches, clés
# de citation — est identique dans les deux langues : ce sont des données, et les faire
# passer par un traducteur les exposerait à être réécrites.
MOTS = {
    "fr": {
        "tranche_net": "Tranche de revenu annuel net (dinars)",
        "tranche_imposable": "Tranche de revenu imposable (dinars)",
        "taux_tranche": "Taux de la tranche",
        "taux_effectif": "Taux d\u2019imposition du revenu global à la limite supérieure",
        "periode": "Années de revenus",
        "texte": "Texte",
        "taux": "Taux",
        "plafond_annuel": "Plafond annuel",
        "abattement": "Abattement",
        "deduction_sup": "Déduction supplémentaire",
        "deduction_forfait": "Déduction forfaitaire",
        "part_recettes": "Part des recettes brutes imposée",
        "minimum_impot": "Minimum d'impôt",
        "deduction": "Déduction",
        "enfant1": "1\u1d49\u02b3 enfant",
        "enfant4": "4\u1d49 enfant",
        "enfant2": "2\u1d49 enfant",
        "enfant3": "3\u1d49 enfant",
        "parent_ressources": "Ressources maximales du parent à charge",
        "smig_fois": "{n} SMIG",
        # Synthèse des générations du barème.
        "generation": "", "generation_cpe": "Revenus {debut} (CPE)",
        "generation_periode": "Revenus {debut} → {fin}",
        "nb_tranches": "Nombre de tranches (tranche à 0 % comprise)",
        "limite_zero": "Limite supérieure de la tranche à 0 %",
        "tms": "Taux marginal supérieur",
        "seuil_tms": "Seuil du taux marginal supérieur",
        "enfant_infirme": "Enfant infirme",
        "parent": "Parent à charge",
        # Libellés des liens vers la base législative des barèmes.
        "bareme_ir": "Barème de l\u2019impôt sur le revenu",
        "bareme_cpe": "Barème de la contribution personnelle d\u2019État",
        "revenus_depuis": "Revenus réalisés à compter du",
        "plafond_cpe": "Plafond de la cotisation effective (part du revenu global imposable)",
        # Taux de la taxe sur la valeur ajoutée.
        "effet": "Date d'effet",
        "tva_normal": "Taux normal", "tva_intermediaire": "Taux intermédiaire",
        "tva_reduit": "Taux réduit", "tva_majore": "Taux majoré",
        "tva_lien": "{taux} de la taxe sur la valeur ajoutée",
        # Déductions pour situation et charges de famille (article 40 du code).
        "chef_famille": "Chef de famille",
        "famille_ligne": "Déduction, en dinars par an",
        "famille_lien": "{nom} — déduction pour charges de famille",
    },
    "ar": {
        "tranche_net": "شريحة الدخل السنوي الصافي (بالدينار)",
        "tranche_imposable": "شريحة الدخل الخاضع للضريبة (بالدينار)",
        "taux_tranche": "نسبة الشريحة",
        "taux_effectif": "نسبة الضريبة على الدخل الجملي عند الحدّ الأعلى",
        "periode": "سنوات المداخيل",
        "texte": "النصّ",
        "taux": "النسبة",
        "plafond_annuel": "السقف السنوي",
        "abattement": "الطرح",
        "deduction_sup": "الطرح الإضافي",
        "deduction_forfait": "الطرح الجزافي",
        "part_recettes": "الجزء الخاضع للضريبة من المقابيض الخام",
        "minimum_impot": "الضريبة الدنيا",
        "deduction": "الطرح",
        "enfant1": "الطفل الأوّل",
        "enfant4": "الطفل الرابع",
        "enfant2": "الطفل الثاني",
        "enfant3": "الطفل الثالث",
        "parent_ressources": "الموارد القصوى للوالد المتكفَّل به",
        "smig_fois": "{n} × الأجر الأدنى المضمون",
        "generation": "", "generation_cpe": "مداخيل {debut} (الضريبة الشخصية للدولة)",
        "generation_periode": "مداخيل {debut} → {fin}",
        "nb_tranches": "عدد الشرائح (بما فيها الشريحة بنسبة 0 %)",
        "limite_zero": "الحدّ الأعلى للشريحة بنسبة 0 %",
        "tms": "أعلى نسبة حدّية",
        "seuil_tms": "عتبة أعلى نسبة حدّية",
        "enfant_infirme": "الطفل المعوق",
        "parent": "الوالد المتكفَّل به",
        "bareme_ir": "جدول الضريبة على الدخل",
        "bareme_cpe": "جدول الضريبة الشخصية للدولة",
        "revenus_depuis": "المداخيل المحقّقة ابتداء من",
        "plafond_cpe": "سقف الضريبة الشخصية للدولة (نسبة من الدخل الجملي الخاضع للضريبة)",
        # « النسبة العادية », « المخفضة », « المرتفعة » : termes de precis/glossaire.yml. Le
        # glossaire n'a pas d'entrée pour le taux intermédiaire, que le code ne nomme pas.
        "effet": "تاريخ النفاذ",
        "tva_normal": "النسبة العادية", "tva_intermediaire": "النسبة الوسيطة",
        "tva_reduit": "النسبة المخفضة", "tva_majore": "النسبة المرتفعة",
        "tva_lien": "{taux} للأداء على القيمة المضافة",
        # « رئيس العائلة » : terme de l'article 40 du code, repris de la description du
        # paramètre ; precis/glossaire.yml n'a pas d'entrée pour lui.
        "chef_famille": "رئيس العائلة",
        "famille_ligne": "الطرح، بالدينار في السنة",
        "famille_lien": "{nom} — الطرح بعنوان الأعباء العائلية",
    },
}

UNITES = {
    "fr": {"dinar": " D", "sans_plafond": "aucun plafond", "aucun": "aucun", "vide": "—"},
    "ar": {"dinar": " د", "sans_plafond": "دون سقف", "aucun": "لا شيء", "vide": "—"},
}

# (nom de fichier, année de revenus, colonne du taux effectif, en-tête, source JORT)
# Barèmes de la contribution personnelle d'État, supprimée pour les revenus 1990.
TABLEAUX_CPE = [
    ("bareme_cpe_1962.md", 1962),
    ("bareme_cpe_1965.md", 1965),
    ("bareme_cpe_1980.md", 1980),
    ("bareme_cpe_1983.md", 1983),
    ("bareme_cpe_1986.md", 1986),
]

# Séries de paramètres scalaires : (fichier, chemin, en-tête de la colonne, formateur).
def formateurs(langue):
    u = UNITES[langue]
    f = ot.formateurs(langue)
    dinars, taux = f.dinars, f.taux

    def plafond(v):
        if v is None or v == float("inf"):
            return u["sans_plafond"]
        return ot.formate_dinars(v) + u["dinar"]

    def plafond_ou_aucun(v):
        if v is None or v == float("inf"):
            return u["aucun"]
        return ot.formate_dinars(v) + u["dinar"]

    return dinars, taux, plafond, plafond_ou_aucun


# Tableaux d'évolution : (fichier, specs, clés de citation).
# Les clés raccrochent chaque rupture à la bibliographie du précis ; les valeurs et les
# dates, elles, viennent des paramètres. Les en-têtes sont symboliques : `MOTS` les rend
# dans la langue voulue.
def evolutions(langue):
    m = MOTS[langue]
    u = UNITES[langue]
    dinars, taux, _plafond, plafond_ou_aucun = formateurs(langue)
    ir = "parameters/impot_revenu"
    return [
        ("frais_professionnels.md",
         [(f"{ir}/tspr/abat_sal.yaml", m["taux"], taux),
          (f"{ir}/tspr/max_abat_sal.yaml", m["plafond_annuel"], plafond_ou_aucun)],
         {"1990-01-01": "code-irpp-is-1990, art. 26", "2017-01-01": "lf-2017, art. 14"}),
        ("abattement_pensions.md",
         [(f"{ir}/tspr/abat_pen.yaml", m["abattement"], taux)],
         {"1990-01-01": "code-irpp-is-1990, art. 26", "2027-01-01": "lf-2026, art. 56",
          "2028-01-01": "lf-2026, art. 56", "2029-01-01": "lf-2026, art. 56"}),
        ("abattement_salaire_minimum.md",
         [(f"{ir}/tspr/abattement_pour_salaire_minimum.yaml", m["deduction_sup"], dinars)],
         {"2004-01-01": "lf-2005, art. 49", "2009-01-01": "lf-2010, art. 39",
          "2014-01-01": "lf-2014, art. 73"}),
        ("foncier_bati.md",
         [(f"{ir}/foncier/bati/deduction_frais.yaml", m["deduction_forfait"], taux)],
         {"1990-01-01": "code-irpp-is-1990, art. 28", "2015-01-01": "lf-2016, art. 21",
          "2024-01-01": "lf-2025, art. 39"}),
        ("bnc_forfait.md",
         [(f"{ir}/bnc/forf/part_forf.yaml", m["part_recettes"], taux)],
         {"1990-01-01": "code-irpp-is-1990, art. 22", "2013-01-01": "lf-2014, art. 46"}),
        ("minimum_impot_avantages.md",
         [(f"{ir}/minimum_impot/taux.yaml", m["minimum_impot"], taux)],
         {"1999-01-01": "lf-1998, art. 62",
          "2017-04-01": "loi-avantages-fiscaux-2017, art. 2"}),
        ("famille_chef_de_famille.md",
         [(f"{ir}/deductions/famille/chef_de_famille.yaml", m["deduction"], dinars),
          (f"{ir}/deductions/famille/enf1.yaml", m["enfant1"], dinars),
          (f"{ir}/deductions/famille/enf2.yaml", m["enfant2"], dinars),
          (f"{ir}/deductions/famille/enf3.yaml", m["enfant3"], dinars),
          (f"{ir}/deductions/famille/enf4.yaml", m["enfant4"], dinars),
          (f"{ir}/deductions/famille/infirme.yaml", m["enfant_infirme"], dinars),
          (f"{ir}/deductions/famille/parent_max.yaml", m["parent"], dinars),
          (f"{ir}/deductions/famille/parent_plaf.yaml", m["parent_ressources"],
           lambda v: u["vide"] if v is None else m["smig_fois"].format(n=f"{v:g}"))],
         {"1990-01-01": "code-irpp-is-1990, art. 40", "2004-01-01": "lf-2005, art. 50",
          "2009-01-01": "lf-2010, art. 40", "2013-01-01": "lf-2014, art. 94",
          "2017-01-01": "lf-2018, art. 55", "2019-01-01": "lf-2018, art. 54"}),
    ]


# Tableaux d'évolution au JOUR près : (fichier, specs, clés de citation). Pour les
# paramètres dont chaque rupture ne vaut que pour une date et non pour une période
# connue jusqu'à la suivante — les tarifs intermédiaires de la contribution personnelle
# d'État ne sont pas tous dépouillés, une plage « 1965 → 1979 » affirmerait trop.
def evolutions_datees(langue):
    m = MOTS[langue]
    _dinars, _taux, _plafond, _aucun = formateurs(langue)
    u = UNITES[langue]

    def taux_ou_sans_plafond(v):
        # De 1983 à 1985, l'article 8 réécrit par la loi n° 82-91 ne plafonne pas la
        # cotisation : le paramètre n'a pas de valeur, le tableau dit « aucun plafond ».
        return u["sans_plafond"] if v is None else ot.formate_taux(v)

    cpe = "parameters/impot_revenu/contribution_personnelle_etat"
    return [
        ("plafond_cpe.md",
         [(f"{cpe}/plafond_cotisation.yaml", m["plafond_cpe"], taux_ou_sans_plafond)],
         {"1962-01-01": "loi-62-73-cpe, art. 2", "1965-01-01": "lf-1966, art. 10",
          "1980-01-01": "loi79-66-lf1980, art. 8", "1983-01-01": "lf-1983, art. 9",
          "1986-01-01": "lf-1986, art. 8"}),
    ]


TABLEAUX = [
    (
        "bareme_1990.md",
        1990,
        True,
        "tranche_net",
        "Article 44 § I du code de l'IRPP et de l'IS annexé à la loi n° 89-114 du "
        "30 décembre 1989, JORT n° 1 des 2-5 janvier 1990, p. 9. Inchangé jusqu'aux "
        "revenus de 2016 inclus.",
    ),
    (
        "bareme_2017.md",
        2017,
        False,
        "tranche_net",
        "Article 14 § 1 de la loi n° 2016-78 du 17 décembre 2016, JORT n° 105 du "
        "27 décembre 2016, p. 3831.",
    ),
    (
        "bareme_2025.md",
        2025,
        False,
        "tranche_net",
        "Article 36 § 1 de la loi n° 2024-48 du 9 décembre 2024, JORT n° 149 du "
        "10 décembre 2024, p. 6429.",
    ),
]

# Colonne des taux effectifs telle qu'imprimée au JORT de 1990 : garde-fou contre une
# dérive silencieuse entre les paramètres et le texte publié.
CONTROLE_1990 = ["0 %", "10,50 %", "15,25 %", "20,12 %", "26,05 %", "—"]


def bareme(chemin, annee, libelle, langue, colonne_tranche, avec_taux_effectif):
    """Barème en vigueur au 1er janvier de `annee`, noté au relevé sous `libelle`."""
    m = MOTS[langue]
    ot.releve_note(chemin, libelle)
    return ot.tableau_bareme(
        chemin,
        datetime.date(annee, 1, 1),
        colonne_tranche=colonne_tranche,
        avec_taux_effectif=avec_taux_effectif,
        langue=langue,
        colonne_taux=m["taux_tranche"],
        colonne_taux_effectif=m["taux_effectif"],
    )


# ------------------------------------------------ synthèse des générations du barème
#
# Recension des paramètres en dur, FI-01 : le tableau `tbl-bareme-irpp-generations` ne porte
# que des grandeurs DÉRIVÉES des barèmes déjà lus — nombre de tranches, limite de la tranche
# à taux nul, taux marginal supérieur et son seuil. Elles se calculent ; elles ne se saisissent
# plus. Une génération est un barème daté : la dernière de la contribution personnelle
# d'État, puis chaque barème de l'IRPP, dont les dates sont celles des références du paramètre.

DERNIERE_ANNEE = 2026
GENERATION_CPE = (BAREME_CPE, 1986, "lf-1986, art. 8",
                  {"fr": "n° 91 du 31 déc. 1985, p. 1731", "ar": "العدد 91 بتاريخ 31 ديسمبر 1985، ص. 1731"})
TEXTES_IRPP = {
    1990: ("code-irpp-is-1990, art. 44 § I",
           {"fr": "n° 1 des 2-5 janv. 1990, p. 9", "ar": "العدد 1 بتاريخ 2-5 جانفي 1990، ص. 9"}),
    2017: ("lf-2017, art. 14 § 1",
           {"fr": "n° 105 du 27 déc. 2016, p. 3831", "ar": "العدد 105 بتاريخ 27 ديسمبر 2016، ص. 3831"}),
    2025: ("lf-2025, art. 36 § 1",
           {"fr": "n° 149 du 10 déc. 2024, p. 3429-3430 (éd. fr.)",
            "ar": "العدد 149 بتاريخ 10 ديسمبر 2024، ص. 3429-3430 (النسخة الفرنسية)"}),
}
LIGNES_JORT = {"fr": ("Texte", "JORT"), "ar": ("النصّ", "الرائد الرسمي")}


def bareme_generations(langue):
    """Synthèse des générations du barème progressif, CPE de 1986 puis IRPP."""
    import pandas as pd

    m, u = MOTS[langue], UNITES[langue]
    references = (ot.charge_parametre(BAREME) or {}).get("metadata", {}).get("reference", {})
    annees = sorted(int(str(c)[:4]) for c in references)
    inconnues = [a for a in annees if a not in TEXTES_IRPP]
    if inconnues:
        print(f"✗ génération du barème sans texte déclaré (TEXTES_IRPP) : {inconnues}")
        return None
    generations = [GENERATION_CPE] + [
        (BAREME, a, *TEXTES_IRPP[a]) for a in annees]
    ot.releve_note(BAREME_CPE, m["bareme_cpe"])
    ot.releve_note(BAREME, m["bareme_ir"])
    colonnes, cellules = [], []
    for rang, (chemin, annee, cle, jort) in enumerate(generations):
        tranches = ot.bareme_a_la_date(chemin, datetime.date(annee, 1, 1))
        if not tranches:
            return None
        if chemin == BAREME_CPE:
            colonnes.append(m["generation_cpe"].format(debut=annee))
        else:
            suivante = generations[rang + 1][1] - 1 if rang + 1 < len(generations) \
                else DERNIERE_ANNEE
            colonnes.append(m["generation_periode"].format(debut=annee, fin=suivante))
        cellules.append([
            str(len(tranches)),
            ot.formate_dinars(tranches[1][0]) + u["dinar"],
            ot.formate_taux(tranches[-1][1]),
            ot.formate_dinars(tranches[-1][0]) + u["dinar"],
            f"[@{cle}]",
            jort[langue],
        ])
    libelles = [m["nb_tranches"], m["limite_zero"], m["tms"], m["seuil_tms"],
                *LIGNES_JORT[langue]]
    lignes = [{m["generation"]: libelle, **{c: cellules[j][i] for j, c in enumerate(colonnes)}}
              for i, libelle in enumerate(libelles)]
    return pd.DataFrame(lignes)


# ----------------------------------------------- impôt sur les sociétés : taux et minimum
#
# Recension, FI-18 et FI-20. Les deux tableaux du chapitre étaient imprimés depuis le relevé
# saisi `tarifs-releves-impot-societes.csv`, contrôlé par `check_tarifs_openfisca.py`. Ils
# sont désormais ENGENDRÉS : chaque case que le modèle porte est lue dans le paramètre, à la
# date d'effet de la case ; les autres — la nature du minimum, plafond puis plancher, les
# valeurs antérieures au retournement de 2006, les états « ligne inexistante » et « sans
# objet » — viennent du relevé, qui reste la source de ce que le paramètre ne peut pas porter.
# Le relevé sert aussi de GARDE-FOU : une case lue qui ne rend pas exactement la cellule du
# relevé fait échouer la génération. Les correspondances (ligne -> paramètre) sont celles du
# contrôle, importées et non recopiées.

RELEVE_IS = RACINE / "fr" / "fiscalite" / "tarifs" / "tarifs-releves-impot-societes.csv"
TABLEAUX_IS = {"is_taux.md": "taux-chronologie", "is_minimum.md": "minimum-impot"}
# Traduction des libellés et des états du relevé, qui est en français.
RELEVE_AR = {
    "Taux": "السعر", "Élément": "العنصر", "Depuis 2024": "منذ 2024", "Depuis 2014": "منذ 2014",
    "Droit commun": "السعر العادي",
    "Taux réduit": "السعر المخفّض — الصناعات التقليدية والفلاحة والصيد البحري ومناطق التنمية "
                   "الجهوية والتعاضديات",
    "Petites et moyennes sociétés": "الشركات الصغرى والمتوسطة — رقم معاملات لا يتجاوز مليون "
                                    "دينار أو 500 ألف دينار",
    "Secteurs majorés": "القطاعات الخاضعة لسعر مرفّع — المالية والاتصالات والمحروقات "
                        "والمساحات التجارية الكبرى",
    "Banques et entreprises d'assurance": "البنوك ومؤسسات التأمين",
    "Nature du minimum": "طبيعة الحدّ الأدنى",
    "Taux — sociétés non soumises": "النسبة — الشركات غير الخاضعة لسعر 10 %",
    "Taux — sociétés soumises": "النسبة — الشركات الخاضعة لسعر 10 %",
    "Montant — sociétés non soumises": "المبلغ — الشركات غير الخاضعة لسعر 10 %",
    "Montant — sociétés soumises": "المبلغ — الشركات الخاضعة لسعر 10 %",
    "plafond": "سقف", "plancher": "حدّ أدنى",
    "*(ligne inexistante)*": "*(سطر غير موجود)*",
}


def _ar_releve(texte: str) -> str:
    """Traduit une cellule du relevé : libellé (par son début), état, ou montant."""
    for debut, traduction in RELEVE_AR.items():
        if texte == debut or (len(debut) > 12 and texte.startswith(debut)):
            return traduction
    return texte.replace(" D", " د")


def tableau_is(tableau: str, langue: str):
    """Un tableau du relevé de l'IS, chaque case lue dans le paramètre quand il la porte."""
    import csv
    import pandas as pd
    import check_tarifs_openfisca as controle
    import tarifs

    spec = tarifs.TABLEAUX[tableau]
    rangs = [r for r in csv.DictReader(RELEVE_IS.open(encoding="utf-8"))
             if r["tableau"] == tableau]
    lignes: dict[int, dict[str, str]] = {}
    for r in rangs:
        publiee = tarifs.recompose(r["valeur"], r["unite"], r["statut"])
        case = publiee
        _cle, chemin = controle.cle(r)
        if (r["statut"] == "lu" and r["valeur"] and chemin
                and not controle.prefixe_hors_modele(r)):
            relatif = "parameters/impot_societes/" + chemin.replace(".", "/") + ".yaml"
            valeur = ot.valeur_a_la_date(
                (ot.charge_parametre(relatif) or {}).get("values"),
                datetime.date.fromisoformat(r["date_effet"]))
            if valeur is None:
                raise ValueError(f"{relatif} : aucune valeur au {r['date_effet']}")
            case = (ot.formate_taux(valeur) if r["unite"] == "%"
                    else ot.formate_dinars(valeur) + " " + r["unite"]).strip()
            if case != publiee:
                raise ValueError(f"{tableau} / {r['produit'][:40]} / {r['colonne']} : "
                                 f"le paramètre rend « {case} », le relevé « {publiee} »")
            libelle = r["produit"] if langue == "fr" else _ar_releve(r["produit"])
            ot.releve_note(relatif, libelle)
        ligne = lignes.setdefault(int(r["ordre"]), {})
        ligne["produit"] = r["produit"] if langue == "fr" else _ar_releve(r["produit"])
        ligne[r["colonne"]] = case if langue == "fr" else _ar_releve(case)
    entetes = spec["entetes"] if langue == "fr" else [_ar_releve(e) for e in spec["entetes"]]
    return pd.DataFrame([[lignes[o].get(c, "") for c in spec["champs"]] for o in sorted(lignes)],
                        columns=entetes)


# ------------------------------------------------- taux de la taxe sur la valeur ajoutée

TVA = "parameters/fiscalite_indirecte/tva"
# Dans l'ordre des colonnes du tableau, du taux de droit commun aux taux dérogatoires. Le
# « taux nul » du même répertoire n'est pas un taux du droit — le code ne fixe aucun taux
# de 0 %, il exonère — : ni le tableau ni la série ne le portent.
TAUX_TVA = ("normal", "intermediaire", "reduit", "majore")
# Date d'effet -> clé de citation et articles. Chaque date de la série DOIT y figurer : une
# date nouvelle versée en amont fait échouer la génération tant que son texte n'est pas
# versé à la bibliographie et inscrit ici, plutôt que de publier une ligne sans citation.
CLES_TVA = {
    "1988-07-01": "loi-88-61-tva, art. 7",
    "1995-01-01": "lf-1995, art. 56 à 58 et 100",
    "1998-01-01": "lf-1998, art. 25 et 90",
    "2002-01-01": "loi2001-123-lf2002, art. 82 à 84 et 97",
    "2007-01-01": "loi-2006-80-reduction-taux, art. 13, 17 et 19",
    "2018-01-01": "lf-2018, art. 43 et 67",
}
SERIE_TVA = "tva-taux"
CACHE = RACINE / "_seriescache"


def _chemin_tva(taux: str) -> str:
    return f"{TVA}/taux_{taux}/taux.yaml"


def tva_taux(langue):
    """Les générations de la grille des taux : une ligne par date d'effet, au jour près."""
    m = MOTS[langue]
    taux = ot.formateurs(langue).taux
    specs = [(_chemin_tva(t), m[f"tva_{t}"], taux) for t in TAUX_TVA]
    dates = {d for chemin, _e, _f in specs for d, *_ in ot.serie_datee(chemin)}
    sans_cle = sorted(dates - set(CLES_TVA))
    if sans_cle:
        raise ValueError(f"taux de la TVA : date d'effet sans clé de citation : {sans_cle}")
    df = ot.tableau_evolution_datee(specs, cles=CLES_TVA, langue=langue,
                                    colonne_periode=m["effet"], colonne_texte=m["texte"])
    if df is None:
        return None
    # Le relevé prend l'en-tête de colonne pour libellé ; le lien, lu hors du tableau,
    # doit dire de quelle taxe il s'agit.
    for t in TAUX_TVA:
        ot.releve_note(_chemin_tva(t), m["tva_lien"].format(taux=m[f"tva_{t}"]))
    return df


def parametres_tva() -> list:
    """Les quatre taux, déclarés pour la série longue et le tableau aux dates repères."""
    return [ot.ParametreDate(
        t, _chemin_tva(t), {l: MOTS[l][f"tva_{t}"] for l in LANGUES}, unite="taux",
        lien={l: MOTS[l]["tva_lien"].format(taux=MOTS[l][f"tva_{t}"]) for l in LANGUES})
        for t in TAUX_TVA]


# Dates repères du tableau de l'état de la grille : les dates d'effet qui en changent un
# niveau ou la structure, et l'année de la rédaction. Le 1er janvier 2002 n'en est pas : le
# taux de 10 % y entre dans le code sans changer de valeur.
REPERES_TVA = ["1988-07-01", "1995-01-01", "1998-01-01", "2007-01-01", "2018-01-01",
               f"{DERNIERE_ANNEE}-01-01"]


# ------------------------------- déductions pour charges de famille : série et dates repères
#
# Les sept montants en dinars de l'article 40 du code, que publie déjà, date par date, le
# tableau `famille_chef_de_famille.md`. Leur historique est complet depuis les revenus de
# 1990 et aucun n'est supprimé. La série ne porte pas les textes (`avec_textes=False`) : les
# références du paramètre ne renvoient pas toutes au Journal officiel, et le chapitre cite
# chaque rupture par sa clé — ce sont elles que la figure donne pour sources.
SERIE_FAMILLE = "irpp-deductions-famille"
FAMILLE = (("chef_de_famille", "chef_famille"), ("enf1", "enfant1"), ("enf2", "enfant2"),
           ("enf3", "enfant3"), ("enf4", "enfant4"), ("infirme", "enfant_infirme"),
           ("parent_max", "parent"))
# Années de revenus, de cinq en cinq à partir de la première pleine décennie du code.
REPERES_FAMILLE = ["1990-01-01", "2005-01-01", "2010-01-01", "2015-01-01", "2020-01-01",
                   f"{DERNIERE_ANNEE}-01-01"]


def parametres_famille() -> list:
    return [ot.ParametreDate(
        nom, f"parameters/impot_revenu/deductions/famille/{nom}.yaml",
        {l: MOTS[l][mot] for l in LANGUES}, unite="dinars",
        lien={l: MOTS[l]["famille_lien"].format(nom=MOTS[l][mot]) for l in LANGUES})
        for nom, mot in FAMILLE]


# ------------------------------- droit d'enregistrement sur les successions : deux séries
#
# Le TARIF, par degré de parenté : six tranches de part nette au 1er janvier 1984, un taux
# unique au 17 mai 1993 (code des droits d'enregistrement et de timbre, art. 20, n° 16), la
# ligne directe à 2,5 % au 17 août 1998. Barème à plusieurs tranches : la série est écrite
# tranche par tranche (`ot.ecrire_serie_tranches`), chaque date avec son texte.
# Les ABATTEMENTS sur les parts recueillies en ligne directe ou entre époux (code, art. 51) :
# trois montants en dinars, de 1975, 1993 et 1998 ; la ligne de 1993 reprend ceux de 1975.
SUCCESSIONS = "parameters/fiscalite_indirecte/droits_enregistrement/successions"
SERIE_SUCC_TARIF = "successions-tarif"
SERIE_SUCC_ABATTEMENTS = "successions-abattements"
_SUCC_TARIF_LIEN = {
    "ligne_directe_epoux": {"fr": "Droit sur les successions — tarif, ligne directe et époux",
                            "ar": "معلوم التسجيل على التركات — التعريفة، الخط المباشر والزوجان"},
    "freres_soeurs": {"fr": "Droit sur les successions — tarif, frères et sœurs",
                      "ar": "معلوم التسجيل على التركات — التعريفة، الإخوة والأخوات"},
    "oncles_neveux_cousins": {
        "fr": "Droit sur les successions — tarif, oncles, neveux et cousins",
        "ar": "معلوم التسجيل على التركات — التعريفة، الأعمام والأخوال وأبناء الإخوة وأبناء العمومة"},
    "au_dela_quatrieme_degre": {
        "fr": "Droit sur les successions — tarif, au-delà du quatrième degré et non-parents",
        "ar": "معلوم التسجيل على التركات — التعريفة، ما بعد الدرجة الرابعة وغير الأقارب"},
}
_SUCC_ABATTEMENTS = {
    "par_enfant_ascendant_conjoint": {
        "fr": "Abattement par enfant, ascendant à charge ou conjoint survivant",
        "ar": "الطرح عن كلّ ابن أو أصل في الكفالة أو قرين باقٍ على قيد الحياة"},
    "plafond": {"fr": "Plafond de l'abattement total", "ar": "سقف الطرح الجملي"},
    "supplement_heritier_handicape": {
        "fr": "Abattement supplémentaire par héritier handicapé",
        "ar": "الطرح الإضافي عن كلّ وارث ذي إعاقة"},
}
_SUCC_PREFIXE = {"fr": "Droit sur les successions — ", "ar": "معلوم التسجيل على التركات — "}


def baremes_successions() -> list[tuple[str, str, dict[str, str]]]:
    return [(cle, f"{SUCCESSIONS}/tarif/{cle}.yaml", liens)
            for cle, liens in _SUCC_TARIF_LIEN.items()]


# ------------------------------- barèmes de l'impôt sur le revenu : séries à tranches
#
# IRPP (1990, 2017, 2025) et contribution personnelle d'État (1962-1986) : barèmes appliqués
# par tranche. Les séries nourrissent les figures « taux marginal et taux moyen ».
SERIE_IRPP_BAREME = "irpp-bareme"
SERIE_CPE_BAREME = "cpe-bareme"
_LIEN_IRPP = {"fr": "Impôt sur le revenu — barème", "ar": "الضريبة على الدخل — الجدول"}
_LIEN_CPE = {"fr": "Contribution personnelle d'État — barème",
             "ar": "المساهمة الشخصية للدولة — الجدول"}


def parametres_abattements_successions() -> list:
    return [ot.ParametreDate(
        cle, f"{SUCCESSIONS}/abattement/{cle}.yaml", libelles, unite="dinars",
        lien={l: _SUCC_PREFIXE[l] + libelles[l] for l in LANGUES})
        for cle, libelles in _SUCC_ABATTEMENTS.items()]


# ------------------------- revenus de l'épargne et du capital : taux à chaque réforme
#
# Le tableau `irpp_epargne_taux` du chapitre de l'impôt sur le revenu. Une ligne par date
# d'effet de l'une des séries versées, plus l'année de rédaction. Chaque case ne lit que la
# série en vigueur à sa date : `ot.Lecture` échoue sur une valeur vide, et une série fermée
# (retenue imputable en 2021, libératoire en 2022…) ne s'affiche pas.
#
# Hors tableau : la plus-value des actions cotées. Son régime dépend d'une condition de
# détention (art. 38-17, 2011 ; 2023), qu'aucune feuille ne porte ; le chapitre la donne à
# la main sous le tableau.

CAP = "parameters/impot_revenu/capitaux_mobiliers/retenue_source"
VM = "parameters/impot_revenu/valeurs_mobilieres"
EPARGNE_DATES = ["1990-01-01", "1992-01-02", "1997-01-01", "2004-01-01", "2015-01-01",
                 "2018-01-01", "2020-06-10", "2021-01-01", "2022-01-01", "2023-01-01",
                 "2025-01-01"]
# Registre du chapitre auquel renvoie la case, par colonne et par date.
ANCRES_EPARGNE = {
    "interets": {"1990-01-01": "r-epargne-interets-1990", "1992-01-02": "r-epargne-interets-1992",
                 "1997-01-01": "r-epargne-interets-1997", "2004-01-01": "r-epargne-interets-2004",
                 "2020-06-10": "r-epargne-interets-2020", "2021-01-01": "r-epargne-interets-2021",
                 "2022-01-01": "r-epargne-interets-2022"},
    "anonymes": {"1990-01-01": "r-epargne-interets-1990", "1992-01-02": "r-epargne-interets-1992"},
    "dividende": {"1990-01-01": "r-epargne-distribues-1990", "2015-01-01": "r-epargne-distribues-2014",
                  "2018-01-01": "r-epargne-distribues-2018"},
    "plus_value": {"2004-01-01": "r-epargne-pv-2004", "2023-01-01": "r-epargne-pv-2023"},
}
MOTS_EPARGNE = {
    "fr": {
        "entetes": ["Date d'effet", "Dernière tranche du barème",
                    "Intérêts : dépôt, obligation, bon du Trésor", "Titre anonyme au porteur",
                    "Dividende", "Plus-value, action non cotée, part sociale"],
        "revenus": "revenus {annee}", "bareme": "barème", "imputable": "{t} imputable",
        "liberatoire": "{t}, libératoire", "comptes": " ({s} sur les comptes spéciaux d'épargne)",
        "depots": " ; dépôts à terme rémunérés au-delà du TMM moins un point : {lien}",
        "obligations": "{o} (obligations) ou {t}, libératoire", "commun": "régime commun",
        "exonere": "exonéré", "hors_champ": "hors champ",
        "pv_franchise": "{t}, au-delà de {f} par an",
        "pv_courte": "{t} si détenue au-delà, sinon {c} ; sans franchise",
        "lien_bareme": "Barème de l'impôt sur le revenu, dernière tranche",
        "taux": "Taux", "fixe": "{t}",
    },
    "ar": {
        "entetes": ["تاريخ النفاذ", "الشريحة الأخيرة من الجدول",
                    "الفوائد: الإيداعات والسندات وأذون الخزينة",
                    "السند لحامله المجهول", "الأرباح الموزعة",
                    "القيمة الزائدة، سهم غير مدرج، حصة اجتماعية"],
        "revenus": "مداخيل {annee}", "bareme": "الجدول", "imputable": "{t} قابل للطرح",
        "liberatoire": "{t}، تحرري", "comptes": " ({s} على حسابات الادخار الخاصة)",
        "depots": " ؛ الودائع لأجل التي تفوق مكافأتها معدل السوق النقدية ناقص نقطة: {lien}",
        "obligations": "{o} (الرقاع) أو {t}، تحرري", "commun": "النظام العام",
        "exonere": "معفى", "hors_champ": "خارج المجال",
        "pv_franchise": "{t}، فوق {f} في السنة",
        "pv_courte": "{t} إذا احتُفظ بها لما بعد ذلك، وإلا {c}؛ دون عتبة إعفاء",
        "lien_bareme": "جدول الضريبة على الدخل، الشريحة الأخيرة",
        "taux": "النسبة", "fixe": "{t}",
    },
}
LIBELLES_EPARGNE = {
    "imputable": {"fr": "Retenue imputable sur les revenus de capitaux mobiliers",
                  "ar": "الخصم القابل للطرح على مداخيل رؤوس الأموال المنقولة"},
    "liberatoire": {"fr": "Retenue libératoire sur les revenus de capitaux mobiliers",
                    "ar": "الخصم التحرري على مداخيل رؤوس الأموال المنقولة"},
    "comptes": {"fr": "Retenue sur les comptes spéciaux d'épargne",
                "ar": "الخصم على حسابات الادخار الخاصة"},
    "depots": {"fr": "Retenue sur les dépôts à terme",
               "ar": "الخصم على الودائع لأجل"},
    "obligations": {"fr": "Retenue sur les obligations au porteur anonymes",
                    "ar": "الخصم على الرقاع لحامله المجهول"},
    "titres": {"fr": "Retenue sur les titres au porteur anonymes",
               "ar": "الخصم على السندات لحامله المجهول"},
    "dividende": {"fr": "Retenue sur les revenus distribués",
                  "ar": "الخصم على الأرباح الموزعة"},
    "pv": {"fr": "Taux de la plus-value de cession de titres",
           "ar": "نسبة القيمة الزائدة المتأتية من التفويت في السندات"},
    "pv_courte": {"fr": "Taux de la plus-value de titres non cotés détenus peu de temps",
                  "ar": "نسبة القيمة الزائدة للسندات غير المدرجة المحتفظ بها مدة قصيرة"},
    "franchise": {"fr": "Franchise annuelle de la plus-value de titres",
                  "ar": "العتبة السنوية المعفاة من القيمة الزائدة للسندات"},
}


def irpp_epargne_taux(langue):
    m = MOTS_EPARGNE[langue]

    def en_cours(chemin, date):
        point = ot.en_vigueur(ot.serie_datee(f"{chemin}.yaml"), date)
        return point is not None and point[1] is not None

    def lire(chemin, date, cle, formateur="taux"):
        return ot.Lecture(f"{chemin}.yaml", date, formateur, LIBELLES_EPARGNE[cle])

    def lien(colonne, date, texte):
        ancre = ANCRES_EPARGNE[colonne].get(date)
        return f"[{texte}](#{ancre})" if ancre else texte

    def lien_gabarit(colonne, date, modele):
        """Place le lien autour de la valeur lue : `{t}` devient `[{t}](#ancre)`."""
        ancre = ANCRES_EPARGNE[colonne].get(date)
        return modele.replace("{t}", f"[{{t}}](#{ancre})") if ancre else modele

    lignes = []
    for d in EPARGNE_DATES:
        annee = int(d[:4])
        tranches = ot.bareme_a_la_date(BAREME, datetime.date.fromisoformat(d))
        if not tranches:
            raise ValueError(f"barème de l'IRPP : aucune tranche au {d}")
        ot.releve_note(BAREME, m["lien_bareme"])
        derniere = ot.formate_taux(tranches[-1][1])
        if d in ("1990-01-01", "2025-01-01"):
            date_txt = m["revenus"].format(annee=annee)
        else:
            date_txt = ("[" + ot.formate_date(d, langue) + "]{.insecable}") if langue == "fr" \
                else ot.formate_date(d, langue)

        # Intérêts
        if en_cours(f"{CAP}/taux_liberatoire", d):
            interets = ot.gabarit(lien_gabarit("interets", d, m["liberatoire"]),
                                  t=lire(f"{CAP}/taux_liberatoire", d, "liberatoire"))
        else:
            modele = m["bareme"]
            lectures = {}
            if en_cours(f"{CAP}/taux_imputable", d):
                modele += " ; " + lien_gabarit("interets", d, m["imputable"])
                lectures["t"] = lire(f"{CAP}/taux_imputable", d, "imputable")
                if en_cours(f"{CAP}/taux_comptes_speciaux_epargne", d):
                    cs = ot.en_vigueur(ot.serie_datee(f"{CAP}/taux_comptes_speciaux_epargne.yaml"), d)[1]
                    imp = ot.en_vigueur(ot.serie_datee(f"{CAP}/taux_imputable.yaml"), d)[1]
                    if cs != imp:
                        modele += m["comptes"]
                        lectures["s"] = lire(f"{CAP}/taux_comptes_speciaux_epargne", d, "comptes")
            if en_cours(f"{CAP}/taux_depots_terme", d):
                ancre = ANCRES_EPARGNE["interets"].get(d)
                texte_lien = m["liberatoire"].replace("{t}", "{d}")
                texte_lien = f"[{texte_lien}](#{ancre})" if ancre else texte_lien
                modele += m["depots"].format(lien=texte_lien)
                lectures["d"] = lire(f"{CAP}/taux_depots_terme", d, "depots")
            interets = ot.gabarit(modele, **lectures)
        # Titres anonymes
        titres_ok = en_cours(f"{CAP}/taux_titres_porteur_anonymes", d)
        if titres_ok:
            t = ot.en_vigueur(ot.serie_datee(f"{CAP}/taux_titres_porteur_anonymes.yaml"), d)[1]
            lectures = {"t": lire(f"{CAP}/taux_titres_porteur_anonymes", d, "titres")}
            if en_cours(f"{CAP}/taux_obligations_porteur_anonymes", d):
                o = ot.en_vigueur(ot.serie_datee(f"{CAP}/taux_obligations_porteur_anonymes.yaml"), d)[1]
            else:
                o = None
            if o is not None and o != t:
                modele = m["obligations"]
                lectures["o"] = lire(f"{CAP}/taux_obligations_porteur_anonymes", d, "obligations")
            else:
                modele = m["liberatoire"]
            if d == "1990-01-01" and langue == "fr":
                # Le paramètre ne vise que les bons de caisse jusqu'au 1er janvier 1992
                # (art. 52-I d du code) ; le terme arabe n'est pas établi.
                modele += " (bons de caisse)"
            anonymes = ot.gabarit(lien_gabarit("anonymes", d, modele), **lectures)
        else:
            anonymes = m["commun"] if d == "1997-01-01" else "—"
        # Dividendes
        if en_cours(f"{VM}/revenus_distribues/taux_retenue_source", d):
            dividende = ot.gabarit(lien_gabarit("dividende", d, m["liberatoire"]),
                                   t=lire(f"{VM}/revenus_distribues/taux_retenue_source", d,
                                          "dividende"))
        else:
            dividende = lien("dividende", d, m["exonere"])
        # Plus-value de titres non cotés
        pv = f"{VM}/plus_value_cession_titres"
        if not en_cours(f"{pv}/taux", d):
            plus_value = m["hors_champ"]
        elif en_cours(f"{pv}/taux_non_cotes_detention_courte", d):
            plus_value = ot.gabarit(lien_gabarit("plus_value", d, m["pv_courte"]),
                                    t=lire(f"{pv}/taux", d, "pv"),
                                    c=lire(f"{pv}/taux_non_cotes_detention_courte", d, "pv_courte"))
        else:
            plus_value = ot.gabarit(lien_gabarit("plus_value", d, m["pv_franchise"]),
                                    t=lire(f"{pv}/taux", d, "pv"),
                                    f=lire(f"{pv}/franchise", d, "franchise", "dinars"))
        lignes.append([date_txt, derniere, interets, anonymes, dividende, plus_value])
    return ot.tableau_gabarit(m["entetes"], lignes, langue)


def parametres_dans_le_temps() -> int:
    """Les séries longues et les tableaux aux dates repères. Rend 0, ou 1 au premier échec."""
    generateur = Path(__file__).name
    annees = {l: {d: d[:4] for d in REPERES_FAMILLE} for l in LANGUES}
    return (
        ot.ecrire_serie_tranches(SERIE_SUCC_TARIF, baremes_successions(), CACHE,
                                 colonne="parente")
        or ot.ecrire_serie_tranches(SERIE_IRPP_BAREME, [("irpp", BAREME, _LIEN_IRPP)], CACHE,
                                    colonne="bareme")
        or ot.ecrire_serie_tranches(SERIE_CPE_BAREME, [("cpe", BAREME_CPE, _LIEN_CPE)], CACHE,
                                    colonne="bareme")
        or ot.ecrire_serie_parametres(SERIE_SUCC_ABATTEMENTS,
                                      parametres_abattements_successions(), CACHE)
        or
        ot.ecrire_serie_parametres(SERIE_TVA, parametres_tva(), CACHE, colonne="taux")
        or ot.ecrire_dates_reperes(
            RACINE, "fiscalite", "tva_taux", parametres_tva(), REPERES_TVA,
            entete={l: MOTS[l]["taux"] for l in LANGUES}, generateur=generateur)
        or ot.ecrire_serie_parametres(SERIE_FAMILLE, parametres_famille(), CACHE,
                                      avec_textes=False)
        or ot.ecrire_dates_reperes(
            RACINE, "fiscalite", "deductions_famille", parametres_famille(), REPERES_FAMILLE,
            entete={l: MOTS[l]["famille_ligne"] for l in LANGUES}, entetes_dates=annees,
            generateur=generateur))


def main() -> int:
    if not ot.openfisca_utilisable():
        version = ot.version_openfisca()
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {version}, "
            f"minimum {ot.VERSION_MINIMALE}). Définir OPENFISCA_TUNISIA_PATH.",
            file=sys.stderr,
        )
        return 1

    for langue in LANGUES:
        m = MOTS[langue]
        sortie = RACINE / langue / "fiscalite" / "tables"
        sortie.mkdir(parents=True, exist_ok=True)

        for fichier, annee in TABLEAUX_CPE:
            df, liens = ot.avec_liens(lambda: bareme(
                BAREME_CPE, annee, m["bareme_cpe"], langue,
                colonne_tranche=m["tranche_imposable"], avec_taux_effectif=True))
            if df is None:
                print(f"échec : {langue}/{fichier}", file=sys.stderr)
                return 1
            ot.ecrire_tableau(
                sortie / fichier, df, liens, langue,
                entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                f"     Tarif de la contribution personnelle d'État applicable aux revenus de {annee}.\n"
                "     Source : voir les métadonnées du paramètre\n"
                "     impot_revenu/contribution_personnelle_etat/bareme.yaml -->\n\n",
            )

        for fichier, specs, cles in evolutions(langue):
            df, liens = ot.avec_liens(lambda: ot.tableau_evolution(
                specs, cles=cles, colonne_periode=m["periode"], colonne_texte=m["texte"],
                langue=langue
            ))
            if df is None:
                print(f"échec : {langue}/{fichier}", file=sys.stderr)
                return 1
            origines = ", ".join(c for c, _e, _f in specs)
            ot.ecrire_tableau(
                sortie / fichier, df, liens, langue,
                entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                f"     Paramètres : {origines} -->\n\n",
            )

        for fichier, specs, cles in evolutions_datees(langue):
            df, liens = ot.avec_liens(lambda: ot.tableau_evolution_datee(
                specs, cles=cles, langue=langue,
                colonne_periode=m["revenus_depuis"], colonne_texte=m["texte"]
            ))
            if df is None:
                print(f"échec : {langue}/{fichier}", file=sys.stderr)
                return 1
            origines = ", ".join(c for c, _e, _f in specs)
            ot.ecrire_tableau(
                sortie / fichier, df, liens, langue,
                entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                f"     Paramètres : {origines} -->\n\n",
            )

        for fichier, annee, taux_effectif, entete, source in TABLEAUX:
            df, liens = ot.avec_liens(lambda: bareme(
                BAREME, annee, m["bareme_ir"], langue,
                colonne_tranche=m[entete], avec_taux_effectif=taux_effectif))
            if df is None:
                print(f"échec : {langue}/{fichier}", file=sys.stderr)
                return 1
            if annee == 1990:
                obtenu = list(df[df.columns[-1]])
                assert obtenu == CONTROLE_1990, (
                    "Les taux effectifs calculés ne correspondent plus au barème publié au "
                    f"JORT de 1990.\n  attendu : {CONTROLE_1990}\n  obtenu  : {obtenu}"
                )
            ot.ecrire_tableau(
                sortie / fichier, df, liens, langue,
                entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                f"     Source : {source} -->\n\n",
            )

        df, liens = ot.avec_liens(lambda: bareme_generations(langue))
        if df is None:
            print(f"échec : {langue}/bareme_generations.md", file=sys.stderr)
            return 1
        ot.ecrire_tableau(
            sortie / "bareme_generations.md", df, liens, langue,
            entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                   "     Grandeurs dérivées des barèmes de la CPE (1986) et de l'IRPP. -->\n\n")

        for fichier, tableau in TABLEAUX_IS.items():
            df, liens = ot.avec_liens(lambda: tableau_is(tableau, langue))
            ot.ecrire_tableau(
                sortie / fichier, df, liens, langue,
                entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                       "     Cases lues dans parameters/impot_societes ; les autres viennent du "
                       "relevé\n     precis/fr/fiscalite/tarifs/tarifs-releves-impot-societes.csv, "
                       "qui sert de garde-fou. -->\n\n",
                a_gauche=True)

        try:
            df, liens = ot.avec_liens(lambda: tva_taux(langue))
        except ValueError as erreur:
            print(f"échec : {langue}/tva_taux.md : {erreur}", file=sys.stderr)
            return 1
        if df is None:
            print(f"échec : {langue}/tva_taux.md", file=sys.stderr)
            return 1
        manquantes = ot.cles_manquantes(df, RACINE / langue / "fiscalite")
        if manquantes:
            print(f"échec : {langue}/tva_taux.md : clés absentes de la bibliographie : "
                  f"{manquantes}", file=sys.stderr)
            return 1
        ot.ecrire_tableau(
            sortie / "tva_taux.md", df, liens, langue,
            entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                   f"     Paramètres : {TVA}/taux_*/taux.yaml -->\n\n")

        try:
            df, liens = ot.avec_liens(lambda: irpp_epargne_taux(langue))
        except ValueError as erreur:
            print(f"échec : {langue}/irpp_epargne_taux.md : {erreur}", file=sys.stderr)
            return 1
        if df is None:
            print(f"échec : {langue}/irpp_epargne_taux.md", file=sys.stderr)
            return 1
        ot.ecrire_tableau(
            sortie / "irpp_epargne_taux.md", df, liens, langue,
            entete="<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                   f"     Paramètres : {CAP}/*, {VM}/* -->\n\n")

        total = (len(TABLEAUX_CPE) + len(evolutions(langue))
                 + len(evolutions_datees(langue)) + len(TABLEAUX) + 1 + len(TABLEAUX_IS) + 2)
        print(f"✓ {langue} : {total} tableaux")
    return parametres_dans_le_temps()


if __name__ == "__main__":
    raise SystemExit(main())
