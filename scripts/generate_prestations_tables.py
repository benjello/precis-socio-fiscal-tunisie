"""Régénère les snapshots Markdown des tableaux de paramètres du livre « Prestations sociales ».

Même contrat que `generate_bareme_tables.py` : le build du site n'exécute PAS ce script, il
lit les fichiers qu'il produit, versionnés dans `precis/{fr,ar}/prestations_sociales/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_prestations_tables.py

Les deux langues sont produites ici, et non par la pipeline de traduction : ces tableaux
sont des données, pas de la prose. Les traduire ferait passer des montants et des dates par
un modèle de langue, avec le risque de voir « 122 D » ou « 1er mai 1986 » réécrits. Seuls
les en-têtes et les libellés changent d'une langue à l'autre ; les valeurs, elles, sortent
du même paramètre.

Exige openfisca-tunisia >= 0.76 : c'est la version où les prestations familiales ont été
datées sur leurs textes (PR #392), où les prestations d'assistance ont été corrigées et
sourcées (PR #393), et où la borne basse d'âge du supplément par enfant a été ajoutée
(PR #395). Avant elles, toute la branche contributive était un cliché unique daté de 1960
dont aucune valeur ne datait de 1960.

Ne sont PAS générés, faute de contrepartie dans le modèle : les tableaux de structure
juridique (conditions d'âge de l'enfant à charge, congés de maternité, multiplicateurs du
capital décès, tarifs de l'aide médicale, matrice régime × prestation) et les aides
ponctuelles de l'AMEN social, dont les cinq paramètres ne portent aucune référence et sont
datés de 2019 alors que l'arrêté qui les fixe est de 2020.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

AF = "parameters/prestations/contributives/prestations_familiales"
NC = "parameters/prestations/non_contributives"
RACINE = Path(__file__).parent.parent / "precis"
LANGUES = ("fr", "ar")

# En-têtes de colonnes et libellés de lignes. Le reste du tableau — valeurs, dates,
# clés de citation — est identique dans les deux langues.
MOTS = {
    "fr": {
        "effet": "Effet", "texte": "Texte", "attestation": "Attestation",
        "parametre": "Paramètre", "valeur": "Valeur",
        "rang1": "1^er^", "rang2": "2^e^", "rang3": "3^e^", "rang4": "4^e^",
        "assiette": "Assiette trimestrielle", "rangs_servis": "Rangs servis",
        "su1": "Un enfant à charge", "su2": "Deux enfants à charge",
        "su3": "Trois enfants à charge ou plus",
        "creche_montant": "Montant, par enfant et par mois",
        "creche_duree": "Durée de service, par an",
        "creche_age_min": "Âge minimal de l'enfant",
        "creche_age_max": "Âge maximal de l'enfant",
        "creche_plaf": "Plafond de revenu de la mère",
        "pnafn": "Allocation mensuelle",
        "amen_base": "Allocation de base mensuelle",
        "occasion": "Occasion", "montant": "Montant", "unite": "Unité",
        "ramadan": "Mois de Ramadan", "fitr": "Aïd al-Fitr", "adha": "Aïd al-Idha",
        "rentree_scolaire": "Rentrée scolaire",
        "rentree_universitaire": "Rentrée universitaire",
        "par_famille": "individu ou famille",
        "par_enfant_scolarise": "par enfant scolarisé",
        "par_enfant_superieur": "par enfant dans le supérieur",
        "supp": "Supplément mensuel", "handicap": "Carte de handicap",
        "age_min": "Âge minimal", "age_max": "Âge maximal",
        "age_etudiant": "Âge maximal en études, apprentissage ou formation",
        "amen_transfert": "Base mensuelle du transfert AMEN",
        "afnc": "Allocation familiale non contributive, par enfant",
    },
    "ar": {
        "effet": "بداية السريان", "texte": "النصّ", "attestation": "الإثبات",
        "parametre": "المعيار", "valeur": "القيمة",
        "rang1": "الأوّل", "rang2": "الثاني", "rang3": "الثالث", "rang4": "الرابع",
        "assiette": "الوعاء الثلاثي", "rangs_servis": "الترتيبات المصروفة",
        "su1": "طفل واحد متكفَّل به", "su2": "طفلان متكفَّل بهما",
        "su3": "ثلاثة أطفال متكفَّل بهم أو أكثر",
        "creche_montant": "المبلغ عن كلّ طفل وكلّ شهر",
        "creche_duree": "مدّة الصرف في السنة",
        "creche_age_min": "السنّ الدنيا للطفل",
        "creche_age_max": "السنّ القصوى للطفل",
        "creche_plaf": "سقف دخل الأمّ",
        "pnafn": "المنحة الشهرية",
        "amen_base": "المنحة القاعدية الشهرية",
        "occasion": "المناسبة", "montant": "المبلغ", "unite": "الوحدة",
        "ramadan": "شهر رمضان", "fitr": "عيد الفطر", "adha": "عيد الأضحى",
        "rentree_scolaire": "العودة المدرسية",
        "rentree_universitaire": "العودة الجامعية",
        "par_famille": "عن الفرد أو العائلة",
        "par_enfant_scolarise": "عن كلّ طفل متمدرس",
        "par_enfant_superieur": "عن كلّ طفل بالتعليم العالي",
        "supp": "الزيادة الشهرية", "handicap": "بطاقة إعاقة",
        "age_min": "السنّ الدنيا", "age_max": "السنّ القصوى",
        "age_etudiant": "السنّ القصوى في حالة الدراسة أو التمهين أو التكوين",
        "amen_transfert": "القاعدة الشهرية لتحويل الأمان الاجتماعي",
        "afnc": "المنحة العائلية غير المساهماتية عن كلّ طفل",
    },
}

UNITES = {
    "fr": {"dinar": " D", "aucune": "aucune",
           "smig": "{n} fois le salaire minimum garanti", "vide": "—"},
    "ar": {"dinar": " د", "aucune": "لا شيء",
           "smig": "{n} ضعف الأجر الأدنى المضمون", "vide": "—"},
}

# L'arabe accorde le nom compté avec le nombre : singulier à 1, duel à 2, pluriel de 3 à
# 10, singulier à l'accusatif au-delà. Écrire « 2 أشهر » ou « 36 أشهر » est une faute que
# le lecteur voit immédiatement, et elle serait recopiée à chaque régénération.
COMPTE_AR = {
    "mois": ("شهر", "شهران", "أشهر", "شهرًا"),
    "ans": ("سنة", "سنتان", "سنوات", "سنة"),
}
COMPTE_FR = {"mois": "mois", "ans": "ans"}


def compte(n: int, unite: str, langue: str) -> str:
    if langue != "ar":
        return f"{n} {COMPTE_FR[unite]}"
    singulier, duel, pluriel, accusatif = COMPTE_AR[unite]
    if n == 1:
        return singulier
    if n == 2:
        return duel
    return f"{n} {pluriel}" if 3 <= n <= 10 else f"{n} {accusatif}"


def formateurs(langue):
    u = UNITES[langue]

    def nombre(v, decimales=0):
        """Séparateur de milliers par espace insécable fine, décimal par virgule."""
        if decimales:
            return f"{v:,.{decimales}f}".replace(",", " ").replace(".", ",")
        return f"{int(v):,}".replace(",", " ")

    def dinars(v):
        """Montant en dinars et millimes, sur trois décimales.

        `ot.formate_dinars` élague les zéros de queue — bon pour un plafond fiscal en
        milliers de dinars, faux ici : les prestations s'écrivent en millimes, et
        « 18,75 D » pour 18 dinars 750 millimes n'est pas ce qu'imprime le JORT.
        """
        if v is None:
            return u["vide"]
        brut = nombre(v) if float(v).is_integer() else nombre(v, 3)
        return brut + u["dinar"]

    def taux(v):
        return u["vide"] if v is None else ot.formate_taux(v)

    def entier(v):
        return u["vide"] if v is None else str(int(v))

    def mois(v):
        return u["vide"] if v is None else compte(int(v), "mois", langue)

    def ans(v):
        if v is None:
            return u["vide"]
        return u["aucune"] if int(v) == 0 else compte(int(v), "ans", langue)

    def smig(v):
        if v is None:
            return u["vide"]
        n = str(int(v)) if float(v).is_integer() else str(v).replace(".", ",")
        return u["smig"].format(n=n)

    def coefficient(v):
        return u["vide"] if v is None else f"× {int(v)}"

    return dinars, taux, entier, mois, ans, smig, coefficient


# Clés de citation du précis, par date d'effet : elles raccrochent chaque rupture à la
# bibliographie du livre, identique dans les deux langues. À défaut, la colonne « Texte »
# reprend le titre porté par le paramètre lui-même — en français, faute de mieux.
CLES_AF = {
    "1960-01-01": "loi60-30, art. 52 et 61",
    "1976-01-01": "loi75-82, art. 1-2",
    "1986-05-01": "loi86-75, art. 1-2",
    "1989-01-01": "loi88-38, art. 1 et 5",
}
CLES_CRECHE = {
    f"{AF}/creche/montant.yaml": "decret95-114, art. 1",
    f"{AF}/creche/duree.yaml": "loi94-88, art. 4",
    f"{AF}/creche/age_min.yaml": "loi94-88, art. 4",
    f"{AF}/creche/age_max.yaml": "loi94-88, art. 4",
    f"{AF}/creche/plaf.yaml": "decret95-114, art. 1",
}
CLES_SALAIRE_UNIQUE = dict.fromkeys(
    (f"{AF}/salaire_unique/enf{i}.yaml" for i in (1, 2, 3)), "loi80-36, art. 1"
)
CLES_AMEN = {
    "2020-05-20": "arrete-2020-05-19-transferts, art. 2",
    "2022-01-01": "arrete-2022-04-01-transferts, art. 1",
    "2023-01-01": "arrete-2023-04-03-transferts, art. 1-2",
    "2024-01-01": "arrete-2024-02-28-transferts, art. 1-2",
    "2025-01-01": "arrete-2025-01-29-transferts, art. 1-2",
}
CLES_PNAFN = {"2018-04-01": "arrete-2024-07-10-allocation-pauvres, art. 1"}
CLES_SUPPLEMENT = {
    "2020-05-20": "arrete-2020-05-19-transferts, art. 2",
    "2022-02-01": "arrete-2022-04-01-transferts, art. 1",
}
# L'allocation familiale non contributive naît le 8 avril 2022, entre deux revalorisations
# du transfert : sa ligne a sa propre clé.
CLE_APPUI = "arrete-2022-12-08-appui-occasionnel, art. 4"
CLES_APPUI = dict.fromkeys(
    (
        f"{NC}/amen_social/aides_ponctuelles/fetes_religieuses/ramadan.yaml",
        f"{NC}/amen_social/aides_ponctuelles/fetes_religieuses/aid_al_fitr.yaml",
        f"{NC}/amen_social/aides_ponctuelles/fetes_religieuses/aid_al_adha.yaml",
        f"{NC}/amen_social/aides_ponctuelles/scolarite/rentree_scolaire.yaml",
        f"{NC}/amen_social/aides_ponctuelles/scolarite/rentree_universitaire.yaml",
    ),
    CLE_APPUI,
)
CLES_AMEN_ET_AFNC = dict(
    CLES_AMEN, **{"2022-04-08": "arrete-2022-04-01-allocation-familiale, art. 2-3"}
)


def tableaux(langue):
    m = MOTS[langue]
    dinars, taux, entier, mois, ans, smig, coefficient = formateurs(langue)
    entetes_verticales = (m["parametre"], m["valeur"], m["texte"])

    def af_evolution():
        """Taux par rang, assiette trimestrielle et rangs servis, de 1960 à nos jours."""
        df = ot.tableau_evolution_datee(
            [
                (f"{AF}/af/taux/enf1.yaml", m["rang1"], taux),
                (f"{AF}/af/taux/enf2.yaml", m["rang2"], taux),
                (f"{AF}/af/taux/enf3.yaml", m["rang3"], taux),
                (f"{AF}/af/taux/enf4.yaml", m["rang4"], taux),
                (f"{AF}/af/plancher_trim.yaml", "_plancher_", dinars),
                (f"{AF}/af/plaf_trim.yaml", "_plafond_", dinars),
                (f"{AF}/af/nb_enfants_max.yaml", m["rangs_servis"], entier),
            ],
            cles=CLES_AF, langue=langue,
            colonne_periode=m["effet"], colonne_texte=m["texte"],
        )
        if df is None:
            return None
        # Plancher et plafond décrivent une seule chose — la bande d'assiette — et se
        # lisent ensemble : « 52 D – 500 D » à l'origine, un plafond simple après 1976.
        assiette = [
            ligne["_plafond_"] if ligne["_plancher_"] == UNITES[langue]["vide"]
            else f"{ligne['_plancher_']} – {ligne['_plafond_']}"
            for _, ligne in df.iterrows()
        ]
        df = df.drop(columns=["_plancher_", "_plafond_"])
        df.insert(len(df.columns) - 2, m["assiette"], assiette)
        return df

    def aides_ponctuelles():
        """Les cinq aides, avec l'unité à laquelle chacune se rapporte.

        L'unité n'est pas dans les paramètres et ne peut pas y être : ce n'est pas une
        valeur datée mais la définition du montant — 50 dinars « par enfant scolarisé »
        n'est pas 50 dinars par famille. Elle est donc portée ici, en regard du
        paramètre dont elle qualifie la valeur.
        """
        base = f"{NC}/amen_social/aides_ponctuelles"
        df = ot.tableau_a_la_date(
            [
                (f"{base}/fetes_religieuses/ramadan.yaml", m["ramadan"], dinars),
                (f"{base}/fetes_religieuses/aid_al_fitr.yaml", m["fitr"], dinars),
                (f"{base}/fetes_religieuses/aid_al_adha.yaml", m["adha"], dinars),
                (f"{base}/scolarite/rentree_scolaire.yaml", m["rentree_scolaire"], dinars),
                (f"{base}/scolarite/rentree_universitaire.yaml",
                 m["rentree_universitaire"], dinars),
            ],
            "2022-12-09",
            cles=CLES_APPUI,
            entetes=(m["occasion"], m["montant"], m["texte"]),
        )
        if df is None:
            return None
        df.insert(2, m["unite"], [
            m["par_famille"], m["par_famille"], m["par_famille"],
            m["par_enfant_scolarise"], m["par_enfant_superieur"],
        ])
        return df

    return {
        "af_evolution.md": af_evolution,
        "aides_ponctuelles.md": aides_ponctuelles,
        "salaire_unique.md": lambda: ot.tableau_a_la_date(
            [
                (f"{AF}/salaire_unique/enf1.yaml", m["su1"], dinars),
                (f"{AF}/salaire_unique/enf2.yaml", m["su2"], dinars),
                (f"{AF}/salaire_unique/enf3.yaml", m["su3"], dinars),
            ],
            "1980-05-01", cles=CLES_SALAIRE_UNIQUE, entetes=entetes_verticales,
        ),
        "creche.md": lambda: ot.tableau_a_la_date(
            [
                (f"{AF}/creche/montant.yaml", m["creche_montant"], dinars),
                (f"{AF}/creche/duree.yaml", m["creche_duree"], mois),
                (f"{AF}/creche/age_min.yaml", m["creche_age_min"], mois),
                (f"{AF}/creche/age_max.yaml", m["creche_age_max"], mois),
                (f"{AF}/creche/plaf.yaml", m["creche_plaf"], smig),
            ],
            "1994-10-01", cles=CLES_CRECHE, entetes=entetes_verticales,
        ),
        "pnafn_allocation.md": lambda: ot.tableau_evolution_datee(
            [(f"{NC}/pnafn/allocation.yaml", m["pnafn"], dinars)],
            cles=CLES_PNAFN, avec_attestation=True, langue=langue,
            colonne_periode=m["effet"], colonne_texte=m["texte"],
            colonne_attestation=m["attestation"],
        ),
        "amen_base.md": lambda: ot.tableau_evolution_datee(
            [(f"{NC}/amen_social/allocation_base.yaml", m["amen_base"], dinars)],
            cles=CLES_AMEN, langue=langue,
            colonne_periode=m["effet"], colonne_texte=m["texte"],
        ),
        "amen_supplement_enfant.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{NC}/amen_social/supplements/enfant_a_charge.yaml", m["supp"], dinars),
                (f"{NC}/amen_social/supplements/handicap.yaml", m["handicap"], coefficient),
                (f"{NC}/amen_social/supplements/age_min_enfant.yaml", m["age_min"], ans),
                (f"{NC}/amen_social/supplements/limite_age_enfant.yaml", m["age_max"], ans),
                (f"{NC}/amen_social/supplements/limite_age_etudiant.yaml",
                 m["age_etudiant"], ans),
            ],
            cles=CLES_SUPPLEMENT, langue=langue,
            colonne_periode=m["effet"], colonne_texte=m["texte"],
        ),
        "amen_vs_afnc.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{NC}/amen_social/allocation_base.yaml", m["amen_transfert"], dinars),
                (f"{NC}/allocation_familiale.yaml", m["afnc"], dinars),
            ],
            cles=CLES_AMEN_ET_AFNC, langue=langue,
            colonne_periode=m["effet"], colonne_texte=m["texte"],
        ),
    }


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    for langue in LANGUES:
        sortie = RACINE / langue / "prestations_sociales" / "tables"
        sortie.mkdir(parents=True, exist_ok=True)
        for nom, fabrique in tableaux(langue).items():
            df = fabrique()
            if df is None or df.empty:
                print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
                return 1
            (sortie / nom).write_text(ot.tableau_vers_markdown(df), encoding="utf-8")
        print(f"✓ {langue} : {len(tableaux(langue))} tableaux")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
