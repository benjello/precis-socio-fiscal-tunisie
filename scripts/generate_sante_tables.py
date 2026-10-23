"""Régénère les snapshots Markdown des tableaux de tarifs hospitaliers du livre « La santé ».

Même contrat que les autres générateurs : le build du site n'exécute PAS ce script, il lit les
fichiers qu'il produit, versionnés dans `precis/fr/sante/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_sante_tables.py

Exige openfisca-tunisia >= 0.147 : c'est la version qui verse `sante/tarifs_hospitaliers/`
(PR #506) — tarifs des malades payants des arrêtés de 1993, 1996, 1998, 2003 et 2008, tarifs
réduits des décrets de 1993, 1994 et 1998.

CE QUI EST ENGENDRÉ (quatre tableaux) :
  - `hopital_tarifs_malades_payants.md` : consultations et journées d'hospitalisation des
    arrêtés de 1993 et de 1996 (`tbl-hopital-tarifs-malades-payants`) ;
  - `hopital_lettres_cles.md` : valeurs des lettres clés en 1996 et en 2008
    (`tbl-hopital-lettres-cles`) ;
  - `hopital_forfaits_actes.md` : forfaits d'actes des arrêtés de 1996, 1998, 2003 et 2008
    (`tbl-hopital-forfaits-actes`) ;
  - `soins_assures_hopital.md` : tarifs réduits de 1993, contributions de 1994, tarifs des
    malades payants de 1996 et tarifs réduits de 1998 (`tbl-soins-assures-hopital`).

DEUX LECTURES DU TEMPS. Les tarifs des malades payants de 1993 et de 1996 sont lus À LA DATE
d'effet de la colonne (la valeur en vigueur : une consultation garde son tarif tant qu'un
arrêté ne le change pas). Les lettres clés et les forfaits d'actes sont lus À LA DATE EXACTE de
l'arrêté : le tiret du tableau dit un forfait que l'arrêté ne traite pas, non un forfait qui
cesse de s'appliquer, et seul l'arrêté qui le fixe ou le reprend lui donne une valeur.

CE QUE LE TABLEAU DE 1998 NE PUBLIE PAS. Le décret n° 98-409 fixe les tarifs réduits de
consultation en pourcentage du tarif des malades payants (art. 17) et les arrondit à la tranche
de 500 millimes (art. 22). Les paramètres portent les pourcentages, l'arrondi et la ligne de
l'arrêté de 1996 que le texte nomme — « consultation de médecine générale » pour les centres de
santé de base et les hôpitaux de circonscription. Ils ne tranchent pas trois choix dont dépend
le montant en dinars : le sens de l'arrondi (« la dernière tranche est comptée sur la base d'une
tranche entière »), celle des deux lignes « consultation de spécialité » que vise l'hôpital
régional (10 D ou 14 D) et le rapport de « maître de conférence » à la ligne « professeurs et
maîtres de conférence agrégés ». Le tableau engendré donne donc, pour les quatre consultations
de 1998, le pourcentage et la ligne que le texte nomme, et AUCUN montant en dinars. Pour la même
raison, la colonne de 1996 donne, à l'hôpital régional et à l'établissement universitaire, les
deux lignes de spécialité de l'arrêté (10 D, autres spécialistes ; 14 D, professeurs et maîtres de
conférence agrégés), sans en affecter une à chaque niveau. Le forfait
d'hospitalisation de 1998, égal au tarif d'une journée d'hospitalisation de 1996 (art. 18), est
lu dans les tarifs de 1996.

L'ARABE N'EST PAS ENGENDRÉ. Le livre « La santé » n'a pas encore de chapitre en arabe, et le
glossaire n'a l'arabe que de quelques-uns des termes de ces tableaux (malade payant, lettre clé,
carte de soins). Les libellés de ligne — actes, services, établissements — attendent la passe du
terminologue ; ne pas les inventer ici. Le générateur n'écrit donc que le français.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

S = "parameters/sante/tarifs_hospitaliers"
MP = f"{S}/malades_payants"
CONSULT = f"{MP}/consultation"
HOSP = f"{MP}/hospitalisation"
LC = f"{MP}/lettres_cles"
FA = f"{MP}/forfaits_actes"
TR = f"{S}/tarifs_reduits"
RACINE = Path(__file__).parent.parent / "precis" / "fr" / "sante" / "tables"

# Dates d'effet lues dans les paramètres (arrêtés et décrets du livre).
D_1993_PAYANTS, D_1996_PAYANTS = "1993-02-07", "1997-01-04"
D_1998_FORFAITS, D_2003, D_2008 = "1998-05-04", "2003-02-10", "2008-07-17"
D_1993_REDUITS, D_1994, D_1998_REDUITS = "1993-01-01", "1994-09-06", "1998-03-08"

TIRET = "—"


class Ecart(ValueError):
    """Une lecture ne rend pas ce que le tableau affirme."""


def serie(chemin: str):
    donnees = ot.serie_datee(f"{chemin}.yaml")
    if not donnees:
        raise Ecart(f"paramètre introuvable ou vide : {chemin}")
    return donnees


def montant(v: float) -> str:
    """Un tarif en dinars : « 7 », « 0,160 », « 1,400 » — les millimes s'il y en a."""
    if float(v).is_integer():
        return str(int(v))
    return f"{v:.3f}".replace(".", ",")


def a_la_date(chemin: str, date: str):
    """Valeur en vigueur à `date`, ou None si le paramètre n'existe pas encore."""
    point = ot.en_vigueur(serie(chemin), date)
    if point is None:
        return None
    return point[1]


def a_la_date_exacte(chemin: str, date: str):
    """Valeur portée par l'arrêté de `date`, ou None s'il ne la traite pas.

    Rend (présent, valeur) : une valeur nulle à la date signifie que l'arrêté supprime le tarif.
    """
    for d, v, _titre, _lien in serie(chemin):
        if d == date:
            return True, v
    return False, None


def noter(chemins, libelle: str) -> None:
    for chemin in chemins:
        ot.releve_note(f"{chemin}.yaml", libelle)


def cellule_en_vigueur(chemins, libelle, date, mode="unique", complement=""):
    """Case d'un tarif lu à la date, sur une ou plusieurs feuilles.

    `mode` : « unique » — les feuilles doivent porter la même valeur, la case la donne une
    fois (« médecine générale ou dentaire ») ; « liste » — les valeurs s'énumèrent dans
    l'ordre des feuilles, « 150 ; 100 ; 50 » ; « fourchette » — « 30 ou 35 » quand elles
    diffèrent, une seule valeur quand elles concordent.
    """
    noter(chemins, libelle)
    valeurs = [a_la_date(c, date) for c in chemins]
    if any(v is None for v in valeurs):
        return TIRET
    texte = _assemble(valeurs, mode, libelle)
    return f"{texte}{complement}"


def _assemble(valeurs, mode, libelle):
    if mode == "unique":
        if len(set(valeurs)) != 1:
            raise Ecart(f"« {libelle} » : les feuilles divergent ({valeurs})")
        return montant(valeurs[0])
    if mode == "liste":
        return " ; ".join(montant(v) for v in valeurs)
    if mode == "fourchette":
        distinctes = sorted(set(valeurs))
        return " ou ".join(montant(v) for v in distinctes) if len(distinctes) > 1 \
            else montant(distinctes[0])
    raise ValueError(mode)


def cellule_exacte(chemins, libelle, date, mode="unique", fin=""):
    """Case d'un forfait ou d'une lettre clé lu à la date exacte de l'arrêté.

    Un tiret quand l'arrêté ne traite pas le forfait ; le texte `fin` quand il le supprime.
    """
    noter(chemins, libelle)
    lectures = [a_la_date_exacte(c, date) for c in chemins]
    if not any(present for present, _ in lectures):
        return TIRET
    if not all(present for present, _ in lectures):
        raise Ecart(f"« {libelle} » : l'arrêté du {date} ne traite qu'une partie des feuilles")
    valeurs = [v for _, v in lectures]
    if all(v is None for v in valeurs):
        if not fin:
            raise Ecart(f"« {libelle} » : suppression au {date} sans texte pour la dire")
        return fin
    return _assemble(valeurs, mode, libelle)


# ------------------------------------------------------------ tarifs des malades payants

# Les entêtes portent le nom de l'arrêté, non sa date d'effet : les dates d'effet (7 février
# 1993, 4 janvier 1997) se lisent dans le texte du chapitre et dans la base législative.
def tarifs_malades_payants():
    import pandas as pd

    lignes = [
        ("Consultation de médecine générale ou dentaire",
         [f"{CONSULT}/medecine_generale", f"{CONSULT}/medecine_dentaire"], "unique"),
        ("Consultation de spécialité, autres spécialistes",
         [f"{CONSULT}/specialite_autres_specialistes"], "unique"),
        ("Consultation de spécialité, professeurs et maîtres de conférence agrégés",
         [f"{CONSULT}/specialite_professeurs_agreges"], "unique"),
        ("Journée d'hospitalisation, hôpital de circonscription",
         [f"{HOSP}/hopital_circonscription"], "unique"),
        ("Journée d'hospitalisation, hôpital régional, médecine",
         [f"{HOSP}/hopital_regional_medecine"], "unique"),
        ("Journée d'hospitalisation, hôpital régional, chirurgie",
         [f"{HOSP}/hopital_regional_chirurgie"], "unique"),
        ("Journée d'hospitalisation, établissement universitaire : médecine générale, "
         "pédiatrie, pneumo-phtisiologie, dermato-vénérologie, psychiatrie",
         [f"{HOSP}/universitaire_medecine"], "unique"),
        ("Journée d'hospitalisation, établissement universitaire : nutrition, endocrinologie, "
         "cardiologie, gastro-entérologie, gynécologie-obstétrique, rhumatologie, neurologie",
         [f"{HOSP}/universitaire_specialites_medicales"], "unique"),
        ("Journée d'hospitalisation, établissement universitaire : néphrologie",
         [f"{HOSP}/universitaire_nephrologie"], "unique"),
        ("Journée d'hospitalisation, établissement universitaire : chirurgie et spécialités "
         "chirurgicales, radiothérapie",
         [f"{HOSP}/universitaire_chirurgie"], "unique"),
        ("Journée d'hospitalisation, établissement universitaire : réanimation médicale et "
         "soins intensifs",
         [f"{HOSP}/universitaire_reanimation"], "unique"),
    ]
    entetes = ["Tarif", "Arrêté du 25 janvier 1993<br>(D)", "Arrêté du 19 décembre 1996<br>(D)"]
    return pd.DataFrame(
        [[libelle,
          cellule_en_vigueur(chemins, libelle, D_1993_PAYANTS, mode),
          cellule_en_vigueur(chemins, libelle, D_1996_PAYANTS, mode)]
         for libelle, chemins, mode in lignes],
        columns=entetes)


# ------------------------------------------------------------------------ lettres clés

def lettres_cles():
    import pandas as pd

    def une(nom):
        return [f"{LC}/{nom}"]

    cotations = lambda dossier, noms: [f"{LC}/{dossier}/{n}" for n in noms]  # noqa: E731
    lignes = [
        ("KC", "chirurgie opératoire (en 2008, ou anesthésie ou radiologie interventionnelle)",
         une("chirurgie"), "unique", ""),
        ("KE", "acte de spécialité d'un médecin dans la limite de ses compétences",
         une("specialite"), "unique", ""),
        ("Rd en 1996, Z en 2008", "radiodiagnostic par un médecin radiologue ou un médecin dentiste",
         une("radiodiagnostic"), "unique", ""),
        ("Ri", "radiologie interventionnelle", une("radiologie_interventionnelle"), "unique",
         "rattachée à KC"),
        ("Rt en 1996, RT en 2008", "radiothérapie", une("radiotherapie"), "unique", ""),
        ("E", "échographie", une("echographie"), "unique", ""),
        ("B", "biologie (en 1996, par un biologiste ou un pharmacien autorisé)",
         une("biologie"), "unique", ""),
        ("P", "anatomie et cytologie pathologiques", une("anatomie_cytologie_pathologiques"),
         "unique", ""),
        ("APB", "prélèvement de produits biologiques pour analyse",
         une("prelevement_produits_biologiques"), "unique", ""),
        ("D", "acte d'un médecin dentiste", une("medecin_dentiste"), "unique", ""),
        ("SF", "acte de sage-femme", une("sage_femme"), "unique", ""),
        ("AMM, AMO, AMY", "physiothérapeute, orthophoniste, orthoptiste",
         [f"{LC}/physiotherapeute", f"{LC}/orthophoniste", f"{LC}/orthoptiste"], "unique", ""),
        ("AMI", "infirmier", une("infirmier"), "unique", ""),
        ("S 10, S 20, S 30, S 35, S 40", "scanographie, par cotation",
         cotations("scanographie", ["s10", "s20", "s30", "s35", "s40"]), "liste", ""),
        ("I 3, I 10, I 15, I 20, I 25", "imagerie par résonance magnétique, par cotation",
         cotations("imagerie_resonance_magnetique", ["i3", "i10", "i15", "i20", "i25"]),
         "liste", ""),
    ]
    entetes = ["Lettre clé", "Acte", "1996<br>(D)", "2008<br>(D)"]
    return pd.DataFrame(
        [[cle, acte,
          cellule_exacte(chemins, f"{cle} : {acte}", D_1996_PAYANTS, mode, fin),
          cellule_exacte(chemins, f"{cle} : {acte}", D_2008, mode, fin)]
         for cle, acte, chemins, mode, fin in lignes],
        columns=entetes)


# ------------------------------------------------------------------- forfaits d'actes

def forfaits_actes():
    import pandas as pd

    def f(nom):
        return f"{FA}/{nom}"

    lignes = [
        ("Hémodialyse, par séance (dont 2 D affectés à la lutte contre l'insuffisance rénale)",
         [f("hemodialyse_seance")], "unique", ""),
        ("Lithotripsie, par acte et par localisation", [f("lithotripsie")], "unique", ""),
        ("Imagerie par résonance magnétique", [f("imagerie_resonance_magnetique")], "unique",
         "forfait abrogé"),
        ("Accouchement normal : établissement universitaire ; hôpital régional ; hôpital de "
         "circonscription ou maternité périphérique",
         [f("accouchement_normal/universitaire"), f("accouchement_normal/hopital_regional"),
          f("accouchement_normal/hopital_circonscription")], "liste", ""),
        ("Accouchement par césarienne : établissement universitaire ; hôpital régional",
         [f("accouchement_cesarienne/universitaire"),
          f("accouchement_cesarienne/hopital_regional")], "liste", ""),
        ("Scanner du crâne ; scanner du reste du corps",
         [f("scanner_crane"), f("scanner_reste_corps")], "liste", ""),
        ("Fécondation in vitro, par essai", [f("fecondation_in_vitro")], "unique", ""),
        ("Insémination avec sperme du conjoint, par essai",
         [f("insemination_sperme_conjoint")], "unique", ""),
        ("Photo-kératectomie au laser, par œil (100 D de plus en cas de reprise)",
         [f("photokeratectomie_laser")], "unique", ""),
        ("Kératomileusis in situ au laser, par œil ; les deux yeux opérés ensemble",
         [f("keratomileusis_laser"), f("keratomileusis_laser_deux_yeux")], "liste", ""),
    ]
    # La reprise de la photo-kératectomie est un supplément dit dans le libellé : sa feuille est
    # lue, et le libellé doit porter la valeur qu'elle rend.
    supplement = a_la_date_exacte(f("photokeratectomie_laser_reprise"), D_2003)
    if supplement != (True, 100):
        raise Ecart(f"supplément de reprise de la photo-kératectomie : {supplement}, 100 attendu")
    ot.releve_note(f"{f('photokeratectomie_laser_reprise')}.yaml",
                   "Photo-kératectomie au laser, supplément en cas de reprise")
    dates = [D_1996_PAYANTS, D_1998_FORFAITS, D_2003, D_2008]
    entetes = ["Acte", "Arrêté de 1996<br>(D)", "Arrêté de 1998<br>(D)", "Arrêté de 2003<br>(D)",
               "Arrêté de 2008<br>(D)"]
    return pd.DataFrame(
        [[libelle] + [cellule_exacte(chemins, libelle, date, mode, fin) for date in dates]
         for libelle, chemins, mode, fin in lignes],
        columns=entetes)


# -------------------------------------------------------- tarifs réduits et contributions

def taux(chemin: str, date: str) -> float:
    valeur = a_la_date(chemin, date)
    if valeur is None:
        raise Ecart(f"{chemin} : aucune valeur au {date}")
    return valeur


def soins_assures_hopital():
    import pandas as pd

    def reduit(chemin, libelle, date):
        """Tarif réduit ou contribution en dinars ; un tiret avant la création de la ligne."""
        return cellule_en_vigueur([chemin], libelle, date)

    consultations = [
        # (libellé, feuille en dinars, feuille du taux de 1998, ligne nommée par l'art. 17)
        ("Consultation externe, centre de santé de base",
         f"{TR}/consultation/centre_sante_base", f"{TR}/taux_consultation/centre_sante_base",
         "de la consultation de médecine générale"),
        ("Consultation externe, hôpital de circonscription",
         f"{TR}/consultation/hopital_circonscription",
         f"{TR}/taux_consultation/hopital_circonscription",
         "de la consultation de médecine générale"),
        ("Consultation externe, hôpital régional",
         f"{TR}/consultation/hopital_regional", f"{TR}/taux_consultation/hopital_regional",
         "de la consultation de spécialité"),
        ("Consultation externe, établissement universitaire",
         f"{TR}/consultation/universitaire", f"{TR}/taux_consultation/universitaire",
         "de la consultation d'un maître de conférence"),
    ]
    medecine_generale = [f"{CONSULT}/medecine_generale"]
    specialites = [f"{CONSULT}/specialite_autres_specialistes",
                   f"{CONSULT}/specialite_professeurs_agreges"]
    lignes = []
    for libelle, reduits, taux_1998, ligne_nommee in consultations:
        if reduits.endswith(("centre_sante_base", "hopital_circonscription")):
            payant = cellule_en_vigueur(medecine_generale, libelle, D_1996_PAYANTS,
                                        complement=" (médecine générale)")
        else:
            # Le texte de 1998 ne dit pas laquelle des deux lignes de spécialité s'applique à
            # quel niveau : la case donne les deux lignes de l'arrêté de 1996, nommées, sans
            # en affecter une au niveau de la ligne.
            autres = cellule_en_vigueur([specialites[0]], libelle, D_1996_PAYANTS)
            agreges = cellule_en_vigueur([specialites[1]], libelle, D_1996_PAYANTS)
            payant = (f"{autres} (autres spécialistes) ; "
                      f"{agreges} (professeurs et maîtres de conférence agrégés)")
        ot.releve_note(f"{taux_1998}.yaml", f"{libelle}, tarif réduit de 1998 en pourcentage")
        lignes.append([
            libelle,
            reduit(reduits, libelle, D_1993_REDUITS),
            reduit(reduits, libelle, D_1994),
            payant,
            f"{ot.formate_taux(taux(taux_1998, D_1998_REDUITS))} {ligne_nommee}",
        ])

    def hospitalisation(libelle, reduits, journees, mode="unique"):
        """Trois dates en dinars, puis le forfait de 1998 égal à la journée de 1996 (art. 18)."""
        payant = cellule_en_vigueur(journees, libelle, D_1996_PAYANTS, mode,
                                    complement=" selon le service" if mode == "fourchette" else "")
        forfait_1998 = cellule_en_vigueur(journees, libelle, D_1998_REDUITS, mode,
                                          complement=" selon le service"
                                          if mode == "fourchette" else "")
        if payant != forfait_1998:
            raise Ecart(f"« {libelle} » : la journée de 1996 ne tient plus en 1998")
        return [libelle,
                reduit(reduits, libelle, D_1993_REDUITS) if reduits else TIRET,
                reduit(reduits, libelle, D_1994) if reduits else TIRET,
                payant, forfait_1998]

    # La ligne de réanimation n'existe qu'en 1994 : sa feuille commence à cette date, et la
    # case de 1993 reste un tiret.
    u = f"{HOSP}/universitaire"
    lignes += [
        hospitalisation("Hospitalisation en médecine, hôpital de circonscription",
                        f"{TR}/hospitalisation/hopital_circonscription_medecine",
                        [f"{HOSP}/hopital_circonscription"]),
        hospitalisation("Hospitalisation en médecine, hôpital régional",
                        f"{TR}/hospitalisation/hopital_regional_medecine",
                        [f"{HOSP}/hopital_regional_medecine"]),
        hospitalisation("Hospitalisation en médecine, établissement universitaire",
                        f"{TR}/hospitalisation/universitaire_medecine",
                        [f"{u}_medecine", f"{u}_specialites_medicales", f"{u}_nephrologie"],
                        "fourchette"),
        hospitalisation("Hospitalisation en chirurgie, hôpital de circonscription",
                        f"{TR}/hospitalisation/hopital_circonscription_chirurgie",
                        [f"{HOSP}/hopital_circonscription"]),
        hospitalisation("Hospitalisation en chirurgie, hôpital régional",
                        f"{TR}/hospitalisation/hopital_regional_chirurgie",
                        [f"{HOSP}/hopital_regional_chirurgie"]),
        hospitalisation("Hospitalisation en chirurgie, établissement universitaire",
                        f"{TR}/hospitalisation/universitaire_chirurgie",
                        [f"{u}_chirurgie"]),
        hospitalisation("Réanimation, établissement universitaire",
                        f"{TR}/hospitalisation/universitaire_reanimation",
                        [f"{u}_reanimation"]),
    ]

    # Examens complémentaires, interventions et actes de la nomenclature.
    libelle = "Examens complémentaires, interventions et actes de la nomenclature"
    plafond_1994 = f"{TR}/actes/taux_maximal_conventionnels"
    taux_actes, plafond_actes = f"{TR}/actes/taux", f"{TR}/actes/plafond"
    noter([plafond_1994, taux_actes, plafond_actes], libelle)
    lignes.append([
        libelle,
        TIRET,
        f"en sus, dans la limite de {ot.formate_taux(taux(plafond_1994, D_1994))} des tarifs "
        "en vigueur",
        "en sus, au tarif de l'acte",
        f"{ot.formate_taux(taux(taux_actes, D_1998_REDUITS))} du tarif de l'acte, "
        f"{montant(taux(plafond_actes, D_1998_REDUITS))} D au plus",
    ])
    # Les feuilles des malades payants servent à plusieurs lignes : elles reçoivent leur propre
    # libellé, non celui de la dernière ligne qui les a lues.
    for chemin, nom in [
        (f"{CONSULT}/medecine_generale", "Consultation de médecine générale, malades payants"),
        (f"{CONSULT}/specialite_autres_specialistes",
         "Consultation de spécialité, autres spécialistes, malades payants"),
        (f"{CONSULT}/specialite_professeurs_agreges",
         "Consultation de spécialité, professeurs et maîtres de conférence agrégés, "
         "malades payants"),
        (f"{HOSP}/hopital_circonscription",
         "Journée d'hospitalisation, hôpital de circonscription, malades payants"),
        (f"{HOSP}/hopital_regional_medecine",
         "Journée d'hospitalisation, hôpital régional, médecine, malades payants"),
        (f"{HOSP}/hopital_regional_chirurgie",
         "Journée d'hospitalisation, hôpital régional, chirurgie, malades payants"),
        (f"{u}_medecine",
         "Journée d'hospitalisation, établissement universitaire, médecine, malades payants"),
        (f"{u}_specialites_medicales",
         "Journée d'hospitalisation, établissement universitaire, spécialités médicales, "
         "malades payants"),
        (f"{u}_nephrologie",
         "Journée d'hospitalisation, établissement universitaire, néphrologie, malades payants"),
        (f"{u}_chirurgie",
         "Journée d'hospitalisation, établissement universitaire, chirurgie, malades payants"),
        (f"{u}_reanimation",
         "Journée d'hospitalisation, établissement universitaire, réanimation, malades payants"),
    ]:
        ot.releve_note(f"{chemin}.yaml", nom)
    entetes = ["Établissement et acte", "1993 : tarif réduit<br>(D)",
               "1994 : contribution directe<br>(D)",
               "1996 : tarif des malades payants<br>(D)", "1998 : tarif réduit<br>(D, ou part du tarif de 1996)"]
    return pd.DataFrame(lignes, columns=entetes)


TABLEAUX = {
    "hopital_tarifs_malades_payants.md": tarifs_malades_payants,
    "hopital_lettres_cles.md": lettres_cles,
    "hopital_forfaits_actes.md": forfaits_actes,
    "soins_assures_hopital.md": soins_assures_hopital,
}


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    RACINE.mkdir(parents=True, exist_ok=True)
    for nom, fabrique in TABLEAUX.items():
        try:
            df, liens = ot.avec_liens(fabrique)
        except Ecart as erreur:
            print(f"✗ {nom} : {erreur}", file=sys.stderr)
            return 1
        ot.ecrire_tableau(RACINE / nom, df, liens, "fr", a_gauche=True)
        print(f"✓ fr/{nom} : {len(df)} lignes, {len(liens)} paramètres lus")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
