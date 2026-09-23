"""Régénère les snapshots Markdown des tableaux de paramètres du livre « Retraites ».

Même contrat que les trois générateurs qui précèdent : le build du site n'exécute PAS ce
script, il lit les fichiers qu'il produit, versionnés dans `precis/{fr,ar}/retraites/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_retraites_tables.py

Les paramètres de retraite vivent dans l'arbre unique d'openfisca-tunisia depuis sa version
0.93, qui y a fusionné openfisca-tunisia-pension. En deçà, `parameters/retraite/` n'existe
pas et le garde-fou de version refuse la génération.

Les deux langues sont produites ici, et non par la pipeline de traduction : ces tableaux
sont des données, pas de la prose. Seuls les en-têtes et les libellés changent d'une langue
à l'autre ; les valeurs, les dates et les clés de citation sortent du même paramètre.

CE QUE CES CINQ TABLEAUX DISENT, ET CE QU'ILS NE DISENT PAS
-----------------------------------------------------------
Ils donnent des **niveaux datés** — un âge, un taux, un montant, une fraction du salaire
minimum — et le texte qui fixe chacun. Ils ne donnent pas les conditions qui entourent ces
niveaux : la durée de 35 ans de services qui s'ajoute à l'âge des fonctions astreignantes,
le caractère facultatif du maintien en activité, la nature de la prestation servie aux
carrières courtes. Ces règles sont dans la prose du chapitre, à l'endroit où le tableau
paraît, et le tableau ne s'y substitue pas.

SEPT TABLEAUX DU LIVRE RESTENT ÉCRITS À LA MAIN, et ce n'est pas un retard : les paramètres
ne portent pas la distinction que leurs colonnes affirment. Le huitième, celui des âges
militaires, est engendré depuis le 20 septembre 2026.

- `tbl-cnrps-bonifications` : les paramètres `bonifications/cadre_actif/service_*` portent
  bien le barème 5 / 4 / 3 / 2, mais non la distinction des trois catégories de l'article 32
  — bonification fixe pour les ouvriers, période restant à courir **plafonnée par ce barème**
  pour les cadres actifs, période restant à courir **sans plafond** pour les fonctions
  astreignantes. Engendrer la seule colonne des ouvriers perdrait les deux autres. Le seul
  élément versable de cet article est le repère d'âge — soixante ans, porté à soixante-deux
  par la loi n° 2019-37 —, dont la date d'effet n'est pas établie : l'article premier de
  cette loi fixe un calendrier propre aux âges civils qui ne vaut pas pour son article 2.
- `tbl-cnrps-orphelins` : les conditions d'âge et d'études de la pension d'orphelin ne sont
  pas des valeurs. Le seul paramètre du sujet, `survivants/taux_orphelin`, porte le taux de
  10 % — que ce tableau ne donne pas — et ces conditions dans sa `documentation`.
- `tbl-rsna-anticipes` : l'arbre porte désormais les DURÉES et les TAUX des départs
  anticipés — stages de 360 et 180 mois, décote par trimestre, jouissance à 55 ans de
  l'article 15 ter (PR openfisca-tunisia-pension#52). Ce que ses colonnes affirment reste
  hors de portée : les CONDITIONS de chaque cas — approbation du licenciement par la
  commission de contrôle, inscription au bureau de l'emploi, constat de l'usure, nombre
  d'enfants vivants — sont des faits de situation, non des valeurs datées.
- `tbl-rsna-reference` : `rsna/salaire_reference/duree_mois` porte désormais la fenêtre du
  régime non agricole — 60, 84 puis 120 mois en 1994, 1995 et 1996 (PR openfisca-tunisia-pension
  #51, fusionnée le 20 septembre 2026). Elle ne couvre que TROIS des cinq lignes du tableau.
  Les deux premières ne sont pas des valeurs datées : celle de 1974 offre un CHOIX entre
  trente-six et soixante mois, « selon que l'une ou l'autre de ces périodes de référence est
  plus avantageuse », et celle de 1990 énonce une NON-MODIFICATION — le décret n° 90-1455
  récrit l'article 18 et laisse l'article 19 intact. Engendrer les trois dernières lignes
  amputerait le tableau de ce qui en fait la démonstration.
- `tbl-rsna-survivants` : l'arbre a désormais sa branche « survivants » (PR
  openfisca-tunisia-pension#52), mais elle n'en porte que la moitié. Trois des six lignes
  du tableau sont des RÈGLES et non des valeurs : le sort de la réversion en cas de
  remariage, le plafond de cumul de l'article 38, qui borne un total par un autre montant,
  et l'interdiction de cumuler invalidité et survivant, levée en 1997.
- `tbl-rsna-revalo-montant` et `tbl-rsna-revalo-taux` : la série du SMIG est datée et sourcée
  chez `openfisca-tunisia`, et le cœur chiffré de ces deux tableaux en sortirait. Mais leur
  objet n'est pas le SMIG : c'est la **revalorisation des pensions**, et le paramètre ne
  porte ni la distinction entre la majoration en somme (1980-2000) et la majoration en taux
  (depuis 2001), ni les dates d'effet propres aux pensions — le 1er janvier 2001 pour la
  hausse du SMIG du 1er mai 2000 —, ni les hausses assimilées de 1981 et 1982, ni les
  indemnités spéciales de 1989 et 1991, qui ne sont pas des hausses du SMIG, ni les lignes
  dont la source n'a pas été vérifiée au Journal officiel.
"""

from __future__ import annotations

import datetime
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

ot.utiliser_paquet("openfisca_tunisia")

PAQUET = "openfisca_tunisia"
CNRPS = "parameters/retraite/cnrps"
RSNA = "parameters/retraite/rsna"
RACINE = Path(__file__).parent.parent / "precis"
LANGUES = ("fr", "ar")

# En-têtes de colonnes et libellés. Les équivalents arabes des notions sont ceux du
# glossaire bilingue (`precis/glossaire.yml`), source unique des deux langues.
MOTS = {
    "fr": {
        "effet": "Effet",
        "texte": "Texte",
        # Les en-têtes portent l'ancre du glossaire, comme le faisaient les cellules du
        # tableau écrit à la main : l'ancre `#g-<id>` est commune aux deux langues.
        "cadre_commun": "Cadre commun (art. 24)",
        "penibles": "[Travaux pénibles et insalubres](#g-travaux-penibles-insalubres) (art. 27)",
        "astreignantes": "[Fonctions astreignantes](#g-fonctions-astreignantes) (art. 28)",
        "cadres_actifs": "[Cadres actifs](#g-cadres-actifs) (art. 29)",
        "superieur": "Enseignants du supérieur (art. 29 bis)",
        "mil_troupe": "Hommes de troupe, quartiers-maîtres et matelots",
        "mil_sous_officiers": "Sous-officiers et officiers mariniers",
        "mil_subalternes": "Officiers subalternes",
        "mil_superieurs": "Officiers supérieurs",
        "mil_generaux": "Officiers généraux",
        "tranche_services": "Tranche de services",
        "par_an": "Par année",
        "par_trimestre": "Par trimestre",
        "cumul": "Taux cumulé en fin de tranche",
        "plafond": "Plafond du taux de la pension",
        "minimum": "[Pension minimale garantie](#g-pension-minimale-garantie)",
        "enfant1": "1^er^ enfant",
        "enfant2": "2^e^ enfant",
        "enfant3": "3^e^ enfant",
        "enfant4": "4^e^ enfant (droits acquis avant 1989)",
        "plancher_sup": "Pension de vieillesse ou d'invalidité",
        "plancher_inf": ("Retraite anticipée (art. 15 bis a et b) et "
                         "[pension proportionnelle](#g-pension-proportionnelle)"),
        "intervalle": "{bas} à {haut}",
        "au_dela": "au-delà de {bas}",
        "smig": "du SMIG",
        "vide": "—",
    },
    "ar": {
        "effet": "بداية السريان",
        "texte": "النصّ",
        "cadre_commun": "الإطار العام (الفصل 24)",
        "penibles": "[الأشغال الشاقّة وغير الصحّية](#g-travaux-penibles-insalubres) (الفصل 27)",
        "astreignantes": "[الوظائف المرهقة](#g-fonctions-astreignantes) (الفصل 28)",
        "cadres_actifs": "[الأسلاك النشيطة](#g-cadres-actifs) (الفصل 29)",
        "superieur": "أساتذة التعليم العالي (الفصل 29 مكرّر)",
        "mil_troupe": "رجال الجيش، رؤساء عرفاء وبحارة",
        "mil_sous_officiers": "ضباط الصف وضباط البحرية",
        "mil_subalternes": "الضباط الأعوان",
        "mil_superieurs": "الضباط السامون",
        "mil_generaux": "الضباط العامون",
        "tranche_services": "شريحة الخدمات",
        "par_an": "عن كلّ سنة",
        "par_trimestre": "عن كلّ ثلاثية",
        "cumul": "النسبة المتراكمة في نهاية الشريحة",
        "plafond": "سقف نسبة تصفية الجراية",
        "minimum": "[الجراية الدنيا المضمونة](#g-pension-minimale-garantie)",
        "enfant1": "الطفل الأوّل",
        "enfant2": "الطفل الثاني",
        "enfant3": "الطفل الثالث",
        "enfant4": "الطفل الرابع (حقوق مكتسبة قبل 1989)",
        "plancher_sup": "جراية الشيخوخة أو العجز",
        "plancher_inf": ("التقاعد المبكّر (الفصل 15 مكرّر أ وب) و"
                         "[الجراية النسبية](#g-pension-proportionnelle)"),
        "intervalle": "من {bas} إلى {haut}",
        "au_dela": "ما يفوق {bas}",
        "smig": "من الأجر الأدنى المضمون",
        "vide": "—",
    },
}

# L'arabe accorde le nom compté avec le nombre : singulier à 1, duel à 2, pluriel de 3 à 10,
# singulier à l'accusatif au-delà. « 60 سنوات » est une faute que le lecteur voit, et elle
# serait recopiée à chaque régénération.
COMPTE_AR = ("سنة", "سنتان", "سنوات", "سنة")


def annees(n: int, langue: str) -> str:
    if langue != "ar":
        return f"{n} ans" if n > 1 else f"{n} an"
    if n == 1:
        return COMPTE_AR[0]
    if n == 2:
        return COMPTE_AR[1]
    return f"{n} {COMPTE_AR[2]}" if 3 <= n <= 10 else f"{n} {COMPTE_AR[3]}"


def formateurs(langue):
    m = MOTS[langue]

    def age(v):
        """Un âge, rendu en années accordées."""
        return m["vide"] if v is None else annees(int(v), langue)

    def taux(v):
        return m["vide"] if v is None else ot.formate_taux(v)

    def dinars(v):
        """Montant en dinars et millimes, sur trois décimales.

        `ot.formate_dinars` élague les zéros de queue — faux ici : les indemnités
        familiales s'écrivent en millimes, et « 7,6 D » pour 7 dinars 600 millimes n'est
        pas ce qu'imprime le Journal officiel.
        """
        if v is None:
            return m["vide"]
        brut = f"{v:,.3f}".replace(",", " ").replace(".", ",")
        return brut + (" D" if langue == "fr" else " د")

    def part_smig(v):
        """Une fraction du salaire minimum, rendue comme fraction et non en pourcentage.

        Les textes écrivent « les deux tiers du SMIG » et « la moitié du SMIG » ; le
        paramètre les approche par 0,66666 et 0,5. Imprimer « 66,67 % » donnerait un
        chiffre que ne porte aucun texte.
        """
        if v is None:
            return m["vide"]
        fraction = Fraction(v).limit_denominator(12)
        return f"{fraction.numerator}/{fraction.denominator} {m['smig']}"

    return age, taux, dinars, part_smig


# Clés de citation du précis, par date d'effet : elles raccrochent chaque rupture à la
# bibliographie du livre, identique dans les deux langues. Toute date d'effet d'un paramètre
# lu doit y figurer — à défaut, la colonne « Texte » reprendrait le titre du paramètre, long
# de cent cinquante caractères. `verifie_texte` le contrôle avant d'écrire le snapshot.
CLES_AGES = {
    "1959-04-01": "loi59-18, art. 9, § I, et 52",
    "1985-09-12": "loi85-12, art. 24 et 27 à 29",
    "2009-04-19": "loi2009-20, art. 2",
    "2019-07-01": "loi2019-37, art. 5",
    "2020-01-01": "loi2019-37, art. 1 et 5",
}
CLES_MILITAIRES = {
    "1985-09-12": "loi85-12, art. 61",
    "1989-01-01": "loi88-71, art. 1",
    # Les deux paliers du calendrier transitoire de 2019, comme pour les âges civils : un an
    # de plus au 1er juillet 2019 (art. 5), puis les âges de l'article 61 nouveau (art. 1).
    "2019-07-01": "loi2019-37, art. 5",
    "2020-01-01": "loi2019-37, art. 1 et 5",
}
CLES_PLAFOND_PLANCHER = {
    "1959-04-01": "loi59-18, art. 22, § II, et 52",
    "1970-07-01": "decretloi70-1, art. 1 et 2",
    "1981-05-01": "loi81-70, art. 4-5",
    "1985-09-12": "loi85-12, art. 38 et 39",
}
CLES_INDEMNITES = {
    "1986-05-01": "decret86-611, art. 1 et 3",
    "1989-01-01": "decret88-1136, art. 1-2 ; @loi88-39",
    "1996-11-01": "decret96-1906, art. 1 à 5",
}
CLES_RSNA_PLANCHERS = {
    "1974-01-01": "decret74-499, art. 45",
    "1982-07-22": "decret82-1030, art. 3 et 5",
}


def tableaux(langue):
    m = MOTS[langue]
    age, taux, dinars, part_smig = formateurs(langue)
    datee = dict(langue=langue, colonne_periode=m["effet"], colonne_texte=m["texte"])

    def ages():
        """L'âge de mise à la retraite par catégorie, depuis le 1er avril 1959.

        Le tableau suit les paramètres tels qu'ils sont datés : le cadre commun depuis la loi
        n° 59-18 (art. 9, § I, applicable au 1er avril 1959, art. 52), les autres catégories
        depuis la loi n° 85-12. Une catégorie sans valeur à une date reste vide : pour les
        cadres actifs avant 1985, l'âge dépendait des décrets de classement de l'article 10
        de la loi de 1959, qui ne sont pas versés.
        """
        specs = [
            (f"{CNRPS}/age_legal/civil/cadre_commun.yaml", m["cadre_commun"], age),
            (f"{CNRPS}/age_legal/civil/ouvriers_travaux_penibles.yaml", m["penibles"], age),
            (f"{CNRPS}/age_legal/civil/fonctions_astreignantes/age.yaml", m["astreignantes"], age),
            (f"{CNRPS}/age_legal/civil/cadres_actifs.yaml", m["cadres_actifs"], age),
            (f"{CNRPS}/age_legal/civil/enseignants_du_superieur.yaml", m["superieur"], age),
        ]
        return ot.tableau_evolution_datee(specs, cles=CLES_AGES, **datee)

    def annuites():
        """Le barème des annuités de l'article 38, lu comme un barème à tranches.

        Le paramètre compte en TRIMESTRES : la tranche se rend en années, le taux annuel
        est le quadruple du taux trimestriel, et le taux cumulé en fin de tranche est la
        somme des taux de toutes les tranches parcourues. La dernière tranche, de taux nul,
        n'est pas un oubli : c'est ainsi que le barème rencontre le plafond de 90 % au
        terme de quarante années, sans qu'aucun autre paramètre ait à l'imposer.
        """
        import pandas as pd

        tranches = ot.bareme_a_la_date(
            f"{CNRPS}/bareme_annuite.yaml", datetime.date(1985, 9, 12)
        )
        if not tranches:
            return None
        lignes, cumul = [], 0.0
        for indice, (seuil, trimestriel) in enumerate(tranches):
            suivant = tranches[indice + 1][0] if indice + 1 < len(tranches) else None
            # Le nom compté porte l'accord sur la borne haute : « 0 à 10 ans », et en arabe
            # « من 0 إلى 10 سنوات » — pluriel à dix, singulier à vingt.
            if suivant is None:
                libelle = m["au_dela"].format(bas=annees(int(seuil // 4), langue))
            else:
                libelle = m["intervalle"].format(
                    bas=int(seuil // 4), haut=annees(int(suivant // 4), langue)
                )
                cumul += (suivant - seuil) * trimestriel
            lignes.append({
                m["tranche_services"]: libelle,
                m["par_an"]: taux(trimestriel * 4),
                m["par_trimestre"]: taux(trimestriel),
                m["cumul"]: taux(cumul),
            })
        return pd.DataFrame(lignes)

    return {
        "cnrps_ages.md": ages,
        # Cinq valeurs attachées à cinq positions statutaires, et deux dates. Le tableau
        # est orienté comme celui des âges civils — une ligne par date d'effet — plutôt que
        # comme la version tenue à la main, qui mettait les grades en lignes : deux
        # tableaux voisins qui disent la même sorte de chose doivent se lire pareil.
        "cnrps_militaires_ages.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{CNRPS}/age_legal/militaire/hommes_de_troupe.yaml", m["mil_troupe"], age),
                (f"{CNRPS}/age_legal/militaire/sous_officiers.yaml", m["mil_sous_officiers"], age),
                (f"{CNRPS}/age_legal/militaire/officiers_subalternes.yaml", m["mil_subalternes"], age),
                (f"{CNRPS}/age_legal/militaire/officiers_superieurs.yaml", m["mil_superieurs"], age),
                (f"{CNRPS}/age_legal/militaire/officiers_generaux.yaml", m["mil_generaux"], age),
            ],
            cles=CLES_MILITAIRES, **datee,
        ),
        "cnrps_annuites.md": annuites,
        "cnrps_plafond_plancher.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{CNRPS}/plaf_taux_pension.yaml", m["plafond"], taux),
                (f"{CNRPS}/pension_minimale/minimum_garanti.yaml", m["minimum"], part_smig),
            ],
            cles=CLES_PLAFOND_PLANCHER, **datee,
        ),
        "cnrps_indemnites_familiales.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_1.yaml",
                 m["enfant1"], dinars),
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_2.yaml",
                 m["enfant2"], dinars),
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_3.yaml",
                 m["enfant3"], dinars),
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_4.yaml",
                 m["enfant4"], dinars),
            ],
            cles=CLES_INDEMNITES, **datee,
        ),
        "rsna_planchers.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{RSNA}/pension_minimale/sup.yaml", m["plancher_sup"], part_smig),
                (f"{RSNA}/pension_minimale/inf.yaml", m["plancher_inf"], part_smig),
            ],
            cles=CLES_RSNA_PLANCHERS, **datee,
        ),
    }


def verifie_texte(df, colonne: str) -> str | None:
    """Refuse un tableau dont une ligne n'a pas de clé de citation.

    Sans ce garde-fou, une date d'effet ajoutée au paramètre et oubliée dans les `CLES_`
    ferait passer le titre entier de la référence dans la colonne — cent cinquante
    caractères de fascicule au milieu du tableau, et une citation qui ne se résout pas.
    """
    if colonne not in df.columns:
        return None
    for valeur in df[colonne]:
        texte = str(valeur)
        if not texte.startswith("[@"):
            return texte
    return None


def main() -> int:
    minimum = ot.PAQUETS[PAQUET]["version_minimale"]
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien "
            f"(version {ot.version_openfisca()}, minimum {minimum}). "
            f"Les snapshots existants sont conservés."
        )
        return 1
    for langue in LANGUES:
        sortie = RACINE / langue / "retraites" / "tables"
        sortie.mkdir(parents=True, exist_ok=True)
        fabriques = tableaux(langue)
        for nom, fabrique in fabriques.items():
            df = fabrique()
            if df is None or df.empty:
                print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
                return 1
            manquante = verifie_texte(df, MOTS[langue]["texte"])
            if manquante is not None:
                print(f"✗ {langue}/{nom} : date d'effet sans clé de citation — {manquante}")
                return 1
            (sortie / nom).write_text(ot.tableau_vers_markdown(df), encoding="utf-8")
        print(f"✓ {langue} : {len(fabriques)} tableaux")
    # Chaque série est émise quoi qu'il arrive aux autres, et le code de retour les
    # combine : une série vide ne doit pas en masquer une autre.
    codes = [serie_actualisation(), serie_taux_liquidation(), serie_smig_planchers()]
    return max(codes)


def serie_actualisation() -> int:
    """Émet la série brute du barème d'actualisation des salaires, pour la figure.

    Un paramètre par année de salaire, dont chaque valeur est celle d'un arrêté. La figure
    en tire des taux, qui ne se lisent pas dans un tableau markdown : la série est donc
    émise ici, hors du build — le site se construit sans openfisca (#165) —, une seule fois
    puisque des valeurs brutes n'ont pas de langue. Chaque ligne porte l'arrêté qui fixe
    le coefficient et son lien au Journal officiel.
    """
    lignes = []
    for annee in range(1961, datetime.date.today().year):
        chemin = f"{RSNA}/salaire_reference/actualisation/annee_{annee}.yaml"
        for date, valeur, titre, lien in ot.serie_datee(chemin):
            if valeur is not None:
                lignes.append((date, annee, valeur, titre, lien))
    if not lignes:
        print("✗ rsna-actualisation-salaires : série vide, snapshot conservé.")
        return 1
    lignes.sort()
    cache = RACINE / "_seriescache"
    cache.mkdir(parents=True, exist_ok=True)
    import pandas as pd

    pd.DataFrame(lignes, columns=["bareme", "annee_salaires", "coefficient", "arrete", "lien"]
                 ).to_csv(cache / "rsna-actualisation-salaires.csv", index=False)
    print(f"✓ série rsna-actualisation-salaires : {len(lignes)} coefficients, "
          f"{len({l[0] for l in lignes})} barèmes")
    return 0



# --------------------------------------------------- séries des figures « paramètres »

MARCHE = "parameters/marche_travail"
CACHE = RACINE / "_seriescache"

# Les salaires minimums des pensions sont exprimés en fraction du SMIG « rapporté à une
# durée d'occupation annuelle de 2 400 heures » — 200 heures par mois. Le SMIG mensuel du
# régime de 48 heures (`smig_48h_mensuel`) compte, lui, 208 heures : il n'est pas la base
# de ces montants, qui se calculent sur le SMIG HORAIRE.
HEURES_PAR_MOIS = 2400 / 12


# Une ligne par barème : (régime, chemin du barème, du plafond, de la durée minimale, de
# la durée des carrières courtes ou None). La durée minimale est celle qui ouvre la
# pension au taux du barème ; la figure en tire le tracé plein.
BAREMES = (
    ("cnrps", f"{CNRPS}/bareme_annuite.yaml", f"{CNRPS}/plaf_taux_pension.yaml",
     f"{CNRPS}/duree_de_service_minimale.yaml", None),
    ("rsna", f"{RSNA}/bareme_annuite.yaml", f"{RSNA}/plaf_taux_pension.yaml",
     f"{RSNA}/stage_requis.yaml", f"{RSNA}/stage_derog.yaml"),
)
DUREE_MAX_ANNEES = 45


def _lien_pist(lien: str) -> str:
    """Le lien au Journal officiel, s'il est sur pist.tn ; sinon rien."""
    return lien if lien.startswith("https://www.pist.tn/") else ""


def _valeur(chemin: str, date: datetime.date) -> float | None:
    donnees = ot.charge_parametre(chemin)
    if not donnees or "values" not in donnees:
        return None
    return ot.valeur_a_la_date(donnees["values"], date)


def _taux_cumule(tranches, trimestres: float) -> float:
    """Taux acquis au terme de `trimestres`, somme des tranches parcourues."""
    total = 0.0
    for indice, (seuil, taux) in enumerate(tranches):
        haut = tranches[indice + 1][0] if indice + 1 < len(tranches) else None
        borne = trimestres if haut is None else min(trimestres, haut)
        if borne > seuil:
            total += (borne - seuil) * taux
    return total


def serie_taux_liquidation() -> int:
    """Émet τ(n), le taux de liquidation selon la durée, pour chaque barème daté.

    Une ligne par (régime, barème, durée en années entières de 0 à 45). Le barème est lu
    à sa date d'effet, en trimestres ; le taux est plafonné par le plafond EN VIGUEUR À
    CETTE DATE s'il en existe un, et reste celui du barème sinon — c'est le cas du barème
    de 1959, dont le plafond de 60 % n'a pas de valeur datée : la figure le dit.

    L'année seule du barème est émise, et non sa date : celle du barème de 1959 est la
    date de signature de la loi n° 59-18, quand le chapitre retient partout le 1er avril
    1959 (voir `ages` plus haut, qui écarte la même date pour la même raison).
    """
    import pandas as pd

    lignes = []
    for regime, bareme, plafond, minimum, courte in BAREMES:
        donnees = ot.charge_parametre(bareme) or {}
        references = (donnees.get("metadata") or {}).get("reference") or {}
        dates = sorted({ot._date_de_cle(cle) for cle in references})
        for date in dates:
            tranches = ot.bareme_a_la_date(bareme, date)
            if not tranches:
                continue
            titre, lien = ot._reference_a_la_date(donnees, date.isoformat())
            p = _valeur(plafond, date)
            n0 = _valeur(minimum, date)
            n1 = _valeur(courte, date) if courte else None
            for annees in range(DUREE_MAX_ANNEES + 1):
                brut = _taux_cumule(tranches, 4 * annees)
                lignes.append({
                    "regime": regime,
                    "annee_bareme": date.year,
                    "duree_annees": annees,
                    "taux_bareme": round(brut, 6),
                    "plafond": None if p is None else round(p, 6),
                    "taux": round(brut if p is None else min(brut, p), 6),
                    "duree_minimale": n0,
                    "duree_carriere_courte": n1,
                    "texte": titre,
                    "lien": _lien_pist(lien),
                })
    if not lignes:
        print("✗ retraites-taux-liquidation : série vide, snapshot conservé.")
        return 1
    CACHE.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(lignes)
    df.to_csv(CACHE / "retraites-taux-liquidation.csv", index=False)
    print(f"✓ série retraites-taux-liquidation : "
          f"{df.groupby(['regime', 'annee_bareme']).ngroups} barèmes")
    return 0


# Les fractions du SMIG, colonne par colonne : (colonne de la fraction, colonne du montant,
# chemin). Les montants sont mensuels : fraction × SMIG horaire × 200 heures.
FRACTIONS = (
    ("pi_cnrps", "minimum_cnrps", f"{CNRPS}/pension_minimale/minimum_garanti.yaml"),
    ("pi_cnrps_allocation", "allocation_cnrps",
     f"{CNRPS}/pension_minimale/allocation_vieillesse.yaml"),
    ("pi_rsna", "minimum_rsna", f"{RSNA}/pension_minimale/sup.yaml"),
    ("pi_rsna_reduit", "minimum_rsna_reduit", f"{RSNA}/pension_minimale/inf.yaml"),
)
SMIG_HORAIRE = f"{MARCHE}/smig_48h_horaire.yaml"
# Le multiple ℓ de la limite de calcul du RSNA : six SMIG rapportés à 2 400 heures depuis le
# 1er janvier 1974, trois rédactions de l'article 18 du décret n° 74-499 (1974, 1990, 1994),
# versé et daté par openfisca-tunisia#442 (version 0.99).
LIMITE_MULTIPLE = f"{RSNA}/salaire_reference/limite_multiple_smig.yaml"


def serie_smig_planchers() -> int:
    """Émet, date par date, le SMIG horaire et les montants mensuels qui en dépendent.

    Une ligne par date à laquelle l'un d'eux change, depuis le 1er janvier 1974 : hausse
    du SMIG, ou création d'une fraction. Chaque montant est la fraction EN VIGUEUR à la
    date appliquée au SMIG horaire du régime de 48 heures, rapporté à 200 heures par mois ;
    il est vide avant le texte qui crée la fraction. Toutes les dates d'effet sont émises,
    paliers déjà publiés des années à venir compris : une série coupée au jour du calcul
    changerait d'une semaine à l'autre sans que rien n'ait bougé.

    La ligne porte le décret qui fixe le SMIG en vigueur, et son lien au Journal officiel
    lorsqu'il est sur pist.tn.
    """
    import pandas as pd

    smig = ot.serie_datee(SMIG_HORAIRE)
    if not smig:
        print("✗ retraites-smig-planchers : SMIG introuvable, snapshot conservé.")
        return 1
    dates = {datetime.date.fromisoformat(d) for d, *_ in smig}
    for _, _, chemin in FRACTIONS:
        dates |= {datetime.date.fromisoformat(d) for d, *_ in ot.serie_datee(chemin)}
    limite = ot.serie_datee(LIMITE_MULTIPLE)
    if not limite:
        print("✗ retraites-smig-planchers : limite de calcul du RSNA introuvable, "
              "snapshot conservé.")
        return 1
    limite_depuis = min(datetime.date.fromisoformat(d) for d, *_ in limite)
    dates |= {datetime.date.fromisoformat(d) for d, *_ in limite}
    dates = sorted(d for d in dates if d >= limite_depuis)

    lignes = []
    for date in dates:
        horaire = _valeur(SMIG_HORAIRE, date)
        if horaire is None:
            continue
        mensuel = horaire * HEURES_PAR_MOIS
        _d, _v, titre, lien = max(
            (s for s in smig if datetime.date.fromisoformat(s[0]) <= date),
            key=lambda s: s[0])
        ligne = {"date": date.isoformat(), "smig_horaire": round(horaire, 5),
                 "smig_200h": round(mensuel, 3)}
        for col_pi, col_montant, chemin in FRACTIONS:
            pi = _valeur(chemin, date)
            ligne[col_pi] = None if pi is None else round(pi, 6)
            ligne[col_montant] = None if pi is None else round(pi * mensuel, 3)
        ell = _valeur(LIMITE_MULTIPLE, date)
        ligne["ell_rsna"] = None if ell is None else float(ell)
        ligne["limite_calcul_rsna"] = None if ell is None else round(ell * mensuel, 3)
        ligne["texte_smig"] = titre
        ligne["lien_smig"] = _lien_pist(lien)
        lignes.append(ligne)
    CACHE.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(lignes)
    df.to_csv(CACHE / "retraites-smig-planchers.csv", index=False)
    print(f"✓ série retraites-smig-planchers : {len(df)} dates, "
          f"{df['date'].iloc[0]} → {df['date'].iloc[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
