"""Construction des tableaux de barèmes à partir des paramètres openfisca.

Pendant tunisien de `quarto/openfisca_tables/core.py` du dépôt `conversion_precis_ipp`,
adapté à ce dont le précis a besoin : des **barèmes à tranches** (`brackets:`), là où le
module d'origine ne traite que des paramètres scalaires (`values:`).

Principe, aligné sur celui de `figtools.py` : **le build du site est autonome.**
`openfisca-tunisia` n'est pas une dépendance déclarée du précis. Les tableaux publiés
proviennent de snapshots Markdown versionnés (`precis/fr/fiscalite/tables/`), régénérés à
la demande par `scripts/generate_bareme_tables.py`. Quand une version suffisante
d'openfisca-tunisia est installée, `get_table_or_static` bascule automatiquement sur la
lecture directe des paramètres.

UNE SEULE SOURCE DE PARAMÈTRES. Depuis la version 0.93, openfisca-tunisia porte l'arbre
entier, retraites comprises : openfisca-tunisia-pension y a été fusionné. Les deux systèmes
socio-fiscaux qu'il livre n'en lisent chacun qu'une partie, mais le précis, qui lit les
fichiers YAML et non les systèmes, n'a plus qu'un paquet, une variable d'environnement et un
garde-fou de version. Avant la fusion, il en tenait deux, qui ne se suivaient pas.

Garde-fou de version. Les paramètres n'ont atteint leur état actuel qu'en 0.71 : le barème
1990-2016 était amputé de sa tranche supérieure jusqu'en 0.68 (openfisca-tunisia#380), les
tarifs de la contribution personnelle d'État n'existaient pas avant 0.69 (#381), et une
dizaine de valeurs d'assiette étaient fausses ou mal datées jusqu'en 0.70 (#382). En deçà de
`VERSION_MINIMALE`, on refuse la lecture directe et on retombe sur le snapshot.
"""

from __future__ import annotations

import datetime
import os
import re
import urllib.parse
from pathlib import Path
from typing import Any, Callable

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

try:
    import pandas as pd
except ImportError:  # pragma: no cover
    pd = None


# Les paramètres du précis proviennent d'un seul paquet depuis la fusion des dépôts : voir
# l'en-tête. Le dictionnaire est gardé pour que les lecteurs acceptent toujours un argument
# `paquet` explicite.
PAQUETS = {
    "openfisca_tunisia": {
        "variable": "OPENFISCA_TUNISIA_PATH",
        "distribution": "openfisca-tunisia",
        # 0.93 est la version de la fusion : `parameters/retraite/` n'existe pas en deçà, et
        # le livre « Retraites » ne pourrait pas être engendré. L'arbre de retraite qu'elle
        # apporte est celui d'openfisca-tunisia-pension 7.3.0, qui avait lui-même son
        # histoire de garde-fous — daté et sourcé sur le Journal officiel depuis 5.7, deux
        # chemins déplacés en 6.0 et 7.0, les âges militaires versés en 7.2. La 0.93 les
        # porte tous. La 0.95 verse le barème d'actualisation des salaires du régime non
        # agricole (openfisca-tunisia#438), dont le livre « Retraites » tire une figure : en
        # deçà, `retraite/rsna/salaire_reference/actualisation/` n'existe pas. La 0.99 verse
        # la limite de six SMIG du salaire de référence du RSNA (openfisca-tunisia#442), que
        # le générateur des retraites lit pour la figure de la limite de calcul : en deçà,
        # `retraite/rsna/salaire_reference/limite_multiple_smig` n'existe pas. La 0.106 corrige
        # le plafond d'origine des allocations familiales (52,500 D au 1er avril 1961) et
        # supprime `af/plancher_trim`, qu'aucun texte ne fonde (openfisca-tunisia#450) : en
        # deçà, le tableau des allocations familiales publierait une bande 52-500 D fausse.
        # La 0.107 date le barème d'annuités de la CNRPS de 1959 au 1er avril 1959, et non
        # de la signature (openfisca-tunisia#452) : en deçà, la courbe de 1959 de la figure
        # des taux de liquidation perd son plafond de 60 %. La 0.111 retire le plafond de la
        # contribution personnelle d'État de 1983 à 1985, que la loi n° 82-91 ne fixe pas
        # (openfisca-tunisia#458) : en deçà, le tableau du plafond publierait 60 % dès 1983.
        # La 0.112 verse les barèmes d'actualisation des salaires de 2016, 2017 et 2019
        # (openfisca-tunisia#459) : en deçà, une lecture directe perdrait ces trois barèmes,
        # que la série de la figure et le chapitre comptent désormais. La 0.115 date l'échelle
        # des taux d'accidents du travail au 1er avril 1999 et donne à chaque taux sa
        # référence, numéro de point compris (openfisca-tunisia#465) : en deçà, le tableau
        # de l'échelle de 1999 ne trouverait pas les numéros de point dont il tire ses lignes.
        # La 0.118 verse l'échelle de 1995 (`atmp_1995`, openfisca-tunisia#469) et les taux de
        # 1999 avant transfert du point (`atmp_avant_transfert`, #470) : en deçà, le tableau de
        # 1995 et la première colonne de celui de 1999 n'existent pas. La 0.119 verse les
        # taux de la taxe de formation professionnelle et de la contribution au FOPROLOS
        # (`prelevements_sociaux/autres/`, openfisca-tunisia#477, PR #478) : en deçà, le
        # tableau des autres prélèvements sur les salaires n'existe pas. La 0.121 date et
        # source la série des taux de la TVA depuis 1988 et verse le taux intermédiaire et le
        # taux majoré (openfisca-tunisia#425, PR #480) : en deçà,
        # `fiscalite_indirecte/tva/taux_intermediaire` et `taux_majore` n'existent pas, et le
        # tableau des générations de taux comme la série de sa figure ne pourraient être
        # engendrés. La 0.122 verse les grilles de salaires de trois conventions collectives
        # sectorielles — textile, bâtiment et travaux publics, assurances —, sous
        # `marche_travail/conventions_collectives/` (openfisca-tunisia PR #482) : en deçà, ce
        # nœud n'existe pas, et l'annexe « Les conventions collectives, branche par branche »
        # du volume « Marché du travail » ne pourrait être engendrée. La 0.123 verse la grille
        # horaire du textile en entier (7 catégories, 21 échelons, 147 cases ; PR #486) : en
        # deçà, l'index de l'annexe n'en connaît que deux. La 0.123.1 et la 0.124 datent
        # l'Amen social du 25 mai 2020, jour où ses textes deviennent exécutoires, et non du
        # 20 mai, jour de leur publication ; elles datent du même jour et sourcent les plafonds
        # de ressources de l'article 5 du décret gouvernemental n° 2020-317 (PR #483), versent
        # le palier de 280 D du transfert au 1er janvier 2026 et l'allocation familiale des 6 à
        # 18 ans (`prestations/non_contributives/allocation_familiale_6_18`) : en deçà, les
        # tableaux de l'Amen social du volume « Prestations sociales » publieraient le 20 mai
        # 2020, s'arrêteraient à 260 D, et le tableau des plafonds de ressources ne pourrait
        # être engendré. La borne est la 0.125, dernière version publiée, celle dont les
        # snapshots sont tirés. Les 0.126 à 0.128 versent en entier les grilles des trois
        # conventions (openfisca-tunisia PR #487, #488 et #489) : la grille des assurances
        # (22 lignes, 14 échelons), les deux grilles du bâtiment (personnel occasionnel ;
        # personnel administratif et technique à traitement mensuel) et la grille mensuelle
        # du textile (`agents_payes_au_mois`, 18 lignes, stage et 20 échelons) ; une case
        # illisible y porte une valeur vide à sa date. En deçà, l'index de l'annexe ne connaît
        # que quelques cases des assurances et du bâtiment et ignore trois grilles : l'annexe,
        # qui décrit et trace chaque grille, ne pourrait être engendrée. La borne passe à la
        # 0.128, dernière version publiée le 9 octobre 2026, dont les snapshots sont tirés.
        # La 0.129 ajoute aux assurances les grilles antérieures au 1er juin 1993, dans deux
        # nœuds à part, frères de `salaire_base` (openfisca-tunisia PR #490) : en deçà,
        # l'index et les liens de l'annexe les ignoreraient et sortiraient différents de ceux
        # que la CI régénère. La borne passe à la 0.129, publiée le 10 octobre 2026.
        # La 0.125 verse aussi les paramètres de la fiscalité locale — taxe sur les
        # immeubles bâtis et taxe sur les terrains non bâtis, sous `fiscalite_locale/`
        # (PR #485) : en deçà, les barèmes du chapitre « Les impôts sur les immeubles »
        # du volume « Finances locales » ne pourraient être engendrés.
        "version_minimale": (0, 129),
    },
}

PAQUET_DEFAUT = "openfisca_tunisia"
_paquet_courant = PAQUET_DEFAUT

VERSION_MINIMALE = PAQUETS[PAQUET_DEFAUT]["version_minimale"]


def utiliser_paquet(nom: str) -> None:
    """Désigne le paquet lu par défaut. Un générateur l'appelle une fois, en tête.

    Les lecteurs acceptent aussi un argument `paquet` explicite ; ce réglage global
    évite de le répéter à chaque appel dans un script qui ne lit qu'une source.
    """
    if nom not in PAQUETS:
        msg = f"Paquet inconnu : {nom}. Connus : {', '.join(PAQUETS)}."
        raise ValueError(msg)
    global _paquet_courant
    _paquet_courant = nom

MESSAGE_INDISPONIBLE = (
    "*Tableau non disponible : ni openfisca-tunisia installé, ni snapshot statique.*"
)


# --------------------------------------------------------------------------- accès


def _racine_paquet(paquet: str | None = None):
    """Racine des sources d'un paquet openfisca, ou None.

    Cherche d'abord le paquet installé, puis un checkout désigné par sa variable
    d'environnement (utilisée pour régénérer les snapshots depuis une copie de travail
    non publiée).
    """
    nom = paquet or _paquet_courant
    try:
        import importlib.resources

        return importlib.resources.files(nom)
    except Exception:
        pass
    chemin = os.environ.get(PAQUETS[nom]["variable"])
    if chemin:
        racine = Path(chemin) / nom
        if racine.is_dir():
            return racine
    return None


def version_openfisca(paquet: str | None = None) -> tuple[int, ...] | None:
    """Version du paquet disponible, sous forme de tuple, ou None."""
    nom = paquet or _paquet_courant
    try:
        from importlib.metadata import version

        return tuple(int(x) for x in version(PAQUETS[nom]["distribution"]).split(".")[:2])
    except Exception:
        pass
    racine = _racine_paquet(nom)
    if racine is None:
        return None
    # Copie de travail : lire la version dans le pyproject.toml voisin.
    try:
        pyproject = Path(str(racine)).parent / "pyproject.toml"
        for ligne in pyproject.read_text(encoding="utf-8").splitlines():
            if ligne.startswith("version"):
                brut = ligne.split("=", 1)[1].strip().strip('"').strip("'")
                return tuple(int(x) for x in brut.split(".")[:2])
    except Exception:
        return None
    return None


def openfisca_utilisable(paquet: str | None = None) -> bool:
    """Vrai si le paquet est disponible ET assez récent pour être lu."""
    nom = paquet or _paquet_courant
    if yaml is None or _racine_paquet(nom) is None:
        return False
    version = version_openfisca(nom)
    return version is not None and version >= PAQUETS[nom]["version_minimale"]


# ------------------------------------------------ base législative en ligne des tableaux

# LE LECTEUR REMONTE DE LA VALEUR À SA SOURCE. Chaque tableau engendré est accompagné d'une
# liste de liens, un par grandeur, vers la page publique qui en donne toutes les valeurs
# datées et leurs références. Le générateur ouvre un relevé avant de fabriquer un tableau ;
# les fonctions qui lisent une série y notent le chemin et l'en-tête de colonne ; le relevé
# est écrit à côté du tableau (`<nom>.liens.yml`) et `markdown_avec_legende` en fait un
# onglet. Le lien est engendré comme la valeur : jamais écrit à la main.
#
# Un générateur n'appelle que deux fonctions : `avec_liens(fabrique)`, qui fabrique le
# tableau sous relevé, puis `ecrire_tableau(...)`, qui écrit le snapshot et ses liens. Une
# lecture qui ne passe pas par un tableau à en-têtes — un barème, un total parcourant une
# arborescence — se note à la main par `releve_note(chemin, libellé)`.
BASE_LEGISLATIVE = "https://parameters.tn.tax-benefit.org"
_releve: dict[str, str | None] | None = None


def url_parametre(chemin_relatif: str, langue: str = "fr") -> str:
    """Vue en tableau d'un paramètre : `parameters/a/b.yaml` -> `…/parameters/a.b/table/`."""
    nom = chemin_relatif.removeprefix("parameters/").removesuffix(".yaml").replace("/", ".")
    prefixe = "/ar" if langue == "ar" else ""
    # Quelques fichiers du modèle portent une espace ou une lettre accentuée dans leur nom
    # (`atmp/construction_et_reparation navale.yaml`) : l'URL doit les encoder.
    return f"{BASE_LEGISLATIVE}{prefixe}/parameters/{urllib.parse.quote(nom)}/table/"


def releve_debut() -> None:
    global _releve
    _releve = {}


def releve_note(chemin_relatif: str, libelle: str | None = None) -> None:
    """Note un paramètre lu par le tableau en cours ; un libellé explicite l'emporte."""
    if _releve is None:
        return
    if libelle:
        libelle = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", libelle).strip()
    if libelle or chemin_relatif not in _releve:
        _releve[chemin_relatif] = libelle or _releve.get(chemin_relatif)


def releve_fin() -> list[tuple[str, str | None]]:
    global _releve
    liens, _releve = list((_releve or {}).items()), None
    return liens


def ecrire_liens(chemin_tableau: str | Path, liens: list[tuple[str, str | None]],
                 langue: str) -> None:
    """Écrit `<nom>.liens.yml` à côté du tableau. Tout lien doit porter un libellé."""
    ecrire_fichier_liens(Path(chemin_tableau).with_suffix(".liens.yml"), liens, langue)


def ecrire_fichier_liens(fichier: str | Path, liens: list[tuple[str, str | None]],
                         langue: str) -> None:
    """Écrit une liste de liens « Base législative » dans `fichier`, nommé tel quel.

    Sert aux séries brutes des figures (`_seriescache/<série>.liens.<langue>.yml`), dont
    le nom porte la langue : `with_suffix` l'effacerait.
    """
    sans = [c for c, l in liens if not l]
    if sans:
        raise ValueError(f"paramètre lu sans libellé : {sans}")
    Path(fichier).write_text(yaml.safe_dump(
        [{"libelle": l, "parametre": c, "url": url_parametre(c, langue)} for c, l in liens],
        allow_unicode=True, sort_keys=False), encoding="utf-8")


def avec_liens(fabrique: Callable[[], Any]) -> tuple[Any, list[tuple[str, str | None]]]:
    """Fabrique un tableau sous relevé : rend le tableau et les paramètres qu'il a lus.

    Le relevé est refermé même si la fabrique lève : un relevé resté ouvert capterait
    les lectures du tableau suivant.
    """
    releve_debut()
    try:
        tableau = fabrique()
    finally:
        liens = releve_fin()
    return tableau, liens


def ecrire_tableau(chemin_tableau: str | Path, df: "pd.DataFrame",
                   liens: list[tuple[str, str | None]], langue: str,
                   entete: str = "", autres_livres: tuple[str, ...] = (),
                   a_gauche: bool = False) -> None:
    """Écrit le snapshot Markdown d'un tableau, puis ses liens (`<nom>.liens.yml`).

    `entete` : commentaire HTML placé avant le tableau ; un snapshot qui en porte un se
    termine par une ligne vide, comme les générateurs l'ont toujours écrit.

    `autres_livres` : RÉEMPLOI D'UN TABLEAU DANS UN AUTRE LIVRE. Le même snapshot est écrit
    aussi dans `precis/<langue>/<livre>/tables/`, pour chaque livre nommé — les indemnités
    familiales du secteur public servent aux retraites et aux prestations, les taux de la
    CNRPS aux cotisations et aux rémunérations. La fabrique reste unique : le tableau ne se
    duplique pas dans un second générateur, il est émis deux fois. Les clés de citation du
    tableau doivent exister dans le `references.json` de chaque livre qui le reçoit.
    """
    corps = tableau_vers_markdown(df, a_gauche=a_gauche)
    texte = f"{entete}{corps}\n" if entete else corps
    chemin = Path(chemin_tableau)
    cibles = [chemin] + [chemin.parents[2] / livre / "tables" / chemin.name
                         for livre in autres_livres]
    for cible in cibles:
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(texte, encoding="utf-8")
        ecrire_liens(cible, liens, langue)


def cles_manquantes(df: "pd.DataFrame", dossier_livre: str | Path) -> list[str]:
    """Clés de citation `[@clé]` du tableau absentes de la bibliographie du livre.

    `dossier_livre` : `precis/<langue>/<livre>`. Le livre cite son `references.json` et
    celui, partagé, de sa langue (`precis/<langue>/references.json`). Un tableau réemployé
    dans un autre livre (`ecrire_tableau(..., autres_livres=…)`) doit y résoudre aussi :
    sinon la citation s'imprime telle quelle dans la page.
    """
    import json

    dossier = Path(dossier_livre)
    connues: set[str] = set()
    for fichier in (dossier / "references.json", dossier.parent / "references.json"):
        if fichier.is_file():
            donnees = json.loads(fichier.read_text(encoding="utf-8"))
            entrees = donnees.get("items", []) if isinstance(donnees, dict) else donnees
            connues |= {e.get("id") for e in entrees}
    citees = {c for v in df.astype(str).to_numpy().ravel()
              for c in re.findall(r"@([\w:.#$%&+?<>~/-]+?)(?=[,;\]\s]|$)", v)}
    return sorted(citees - connues)


def ecrire_dans_livres(racine: str | Path, langue: str, livres: tuple[str, ...], nom: str,
                       df: "pd.DataFrame", liens: list[tuple[str, str | None]],
                       entete: str = "") -> str | None:
    """Écrit un tableau dans `precis/<langue>/<livre>/tables/` pour chaque livre de `livres`.

    Le premier livre est celui du tableau ; les suivants le reçoivent en réemploi. Avant
    d'écrire quoi que ce soit, contrôle que les clés de citation résolvent dans CHAQUE livre :
    rend le message d'erreur à afficher, ou None si tout est écrit.
    """
    racine = Path(racine)
    for livre in livres:
        absentes = cles_manquantes(df, racine / langue / livre)
        if absentes:
            return (f"✗ {langue}/{livre}/{nom} : clés absentes de la bibliographie — "
                    f"{', '.join(absentes)}")
    premier, *autres = livres
    ecrire_tableau(racine / langue / premier / "tables" / nom, df, liens, langue,
                   entete=entete, autres_livres=tuple(autres))
    return None


def charge_parametre(chemin_relatif: str, paquet: str | None = None) -> dict[str, Any] | None:
    """Charge un YAML de paramètre, chemin relatif à la racine du paquet.

    Exemple : "parameters/impot_revenu/bareme.yaml".

    PARAMÈTRE LOGÉ DANS UN FICHIER DE NŒUD. Un fichier peut porter plusieurs paramètres, un
    par clé — `…/salaire_base/echelle_1.yaml` porte `echelon_1`. Un tel paramètre se désigne
    comme s'il avait son fichier, `…/salaire_base/echelle_1/echelon_1.yaml` : quand ce
    fichier n'existe pas, le fichier du nœud est chargé et l'on y descend clé par clé. Le
    chemin reste ainsi celui de la page publique du paramètre (`url_parametre`).
    """
    if yaml is None:
        return None
    racine = _racine_paquet(paquet)
    if racine is None:
        return None

    def lit(elements):
        ref = racine
        for element in elements:
            ref = ref / element
        return yaml.safe_load(ref.read_text(encoding="utf-8"))

    elements = chemin_relatif.split("/")
    try:
        return lit(elements)
    except Exception:
        pass
    noms = elements[:-1] + [elements[-1].removesuffix(".yaml")]
    for coupe in range(len(noms) - 1, 0, -1):
        try:
            donnees = lit(noms[:coupe - 1] + [f"{noms[coupe - 1]}.yaml"])
        except Exception:
            continue
        return descend(donnees, noms[coupe:])
    return None


def descend(donnees: Any, cles: list[str]) -> dict[str, Any] | None:
    """Le paramètre logé sous `cles` dans un fichier de nœud déjà chargé, ou None. Pure."""
    for cle in cles:
        if not isinstance(donnees, dict) or cle not in donnees:
            return None
        donnees = donnees[cle]
    return donnees if isinstance(donnees, dict) else None


# ------------------------------------------------------------------- lecture datée


def _annee(cle: Any) -> int:
    return cle.year if hasattr(cle, "year") else int(str(cle)[:4])


def _date_de_cle(cle: Any) -> datetime.date:
    """Date d'effet d'une clé de paramètre, à la JOURNÉE près.

    Les clés arrivent tantôt en objets `date` (PyYAML convertit `2014-01-01`), tantôt
    en chaînes. `datetime` étant une sous-classe de `date`, il se teste en premier.
    """
    if isinstance(cle, datetime.datetime):
        return cle.date()
    if isinstance(cle, datetime.date):
        return cle
    texte = str(cle)[:10]
    annee = int(texte[:4])
    mois = int(texte[5:7]) if len(texte) >= 7 else 1
    jour = int(texte[8:10]) if len(texte) >= 10 else 1
    return datetime.date(annee, mois, jour)


def valeur_a_la_date(bloc: dict[str, Any] | None, date: datetime.date) -> float | None:
    """Valeur en vigueur à `date` dans un bloc daté {date: {value: x}}.

    La comparaison porte sur la DATE COMPLÈTE. Elle ne portait que sur l'année (#215) :
    un palier daté du 1er juillet s'appliquait alors dès janvier, alors qu'il n'était pas
    encore en vigueur.

    Le changement est sans effet là où la convention « année de revenus » a du sens — les
    paramètres fiscaux sont datés au 1er janvier, et les deux lectures y coïncident. Il ne
    modifie que les six blocs porteurs de paliers infra-annuels : les cinq du SMIG/SMAG,
    révisés deux fois en 1980, 1992, 1993, 1996, 1997, 1999 et 2012, et l'allocation du
    PNAFN en 2009 — 53,333 D au 1er janvier, 56,666 D au 1er juillet. C'est là, et là
    seulement, que l'ancienne lecture renvoyait un montant qui n'était pas en vigueur.

    Renvoie None si la valeur en vigueur est nulle : dans openfisca, `value: null`
    signifie que le paramètre cesse d'exister à cette date. On ne remonte alors pas
    au-delà — c'est ce qui permet à une tranche de disparaître d'un barème.
    """
    if not bloc:
        return None
    for cle in sorted(bloc.keys(), key=lambda k: (_date_de_cle(k), str(k)), reverse=True):
        if _date_de_cle(cle) > date:
            continue
        brut = bloc[cle]
        if brut is None:
            return None
        if isinstance(brut, dict):
            valeur = brut.get("value")
            return None if valeur is None else float(valeur)
        if isinstance(brut, (int, float)):
            return float(brut)
    return None


def bareme_a_la_date(
    chemin_relatif: str, date: datetime.date
) -> list[tuple[float, float]] | None:
    """Barème en vigueur à `date` : liste de (seuil, taux), triée par seuil croissant.

    Les tranches dont le seuil ou le taux est nul à cette date sont écartées.
    """
    donnees = charge_parametre(chemin_relatif)
    if not donnees or "brackets" not in donnees:
        return None
    tranches: list[tuple[float, float]] = []
    for tranche in donnees["brackets"]:
        seuil = valeur_a_la_date(tranche.get("threshold"), date)
        taux = valeur_a_la_date(tranche.get("rate"), date)
        if seuil is None or taux is None:
            continue
        tranches.append((seuil, taux))
    if not tranches:
        return None
    return sorted(tranches)


# ------------------------------------------------------------------------ calculs


def taux_effectifs_limite_superieure(
    tranches: list[tuple[float, float]],
) -> list[float | None]:
    """Taux d'imposition du revenu global à la limite supérieure de chaque tranche.

    Troisième colonne des barèmes publiés au JORT jusqu'en 1990. Elle n'est pas dans
    openfisca : on la recalcule. La dernière tranche étant ouverte, elle n'en a pas.
    """
    resultats: list[float | None] = []
    cumul = 0.0
    for indice, (seuil, taux) in enumerate(tranches):
        if indice + 1 >= len(tranches):
            resultats.append(None)
            continue
        limite = tranches[indice + 1][0]
        cumul += (limite - seuil) * taux
        resultats.append(cumul / limite if limite else 0.0)
    return resultats


# ---------------------------------------------------------------------- formatage


def formate_dinars(montant: float) -> str:
    """1500.0 -> '1 500' ; 1500.001 -> '1 500,001'."""
    entier = int(montant)
    decimales = montant - entier
    texte = f"{entier:,}".replace(",", " ")
    if decimales:
        texte += "," + f"{decimales:.3f}".split(".")[1].rstrip("0")
    return texte


def formate_taux(taux: float) -> str:
    """0.15 -> '15 %' ; 0.005 -> '0,5 %'."""
    pourcentage = taux * 100
    if abs(pourcentage - round(pourcentage)) < 1e-9:
        return f"{round(pourcentage)} %"
    return f"{pourcentage:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " %"


def formate_taux_effectif(taux: float | None) -> str:
    """Deux décimales, **tronquées** et non arrondies, comme au JORT.

    Contrôle : 20,125 % est imprimé « 20,12 % » dans le barème de 1990, et 2,667 %
    « 2,66 % » dans celui de 1986 — c'est bien une troncature.
    """
    if taux is None:
        return "—"
    if taux == 0:
        return "0 %"
    pourcentage = taux * 100
    tronque = int(pourcentage * 100 + 1e-9) / 100
    return f"{tronque:.2f}".replace(".", ",") + " %"


BORNES = {
    "fr": ("{bas} à {haut}", "au-delà de {bas}"),
    "ar": ("من {bas} إلى {haut}", "ما يفوق {bas}"),
}


def libelle_tranche(seuil: float, seuil_suivant: float | None, langue: str = "fr") -> str:
    """'0 à 1 500', '1 500,001 à 5 000', 'au-delà de 50 000' ; en arabe 'من … إلى …'."""
    intervalle, au_dela = BORNES.get(langue, BORNES["fr"])
    if seuil_suivant is None:
        return au_dela.format(bas=formate_dinars(seuil))
    bas = formate_dinars(seuil) if seuil == 0 else formate_dinars(seuil + 0.001)
    return intervalle.format(bas=bas, haut=formate_dinars(seuil_suivant))


# ------------------------------------------------------- séries de valeurs datées


def _reference_a_la_date(donnees: dict[str, Any], cle_date: Any) -> tuple[str, str]:
    """Titre et lien de la référence attachée à une date d'effet, sinon ("", "")."""
    refs = ((donnees.get("metadata") or {}).get("reference")) or {}
    for cle, valeur in refs.items():
        if str(cle)[:10] == str(cle_date)[:10]:
            if isinstance(valeur, list):
                valeur = valeur[0] if valeur else {}
            if isinstance(valeur, dict):
                return valeur.get("title", ""), valeur.get("href", "")
            if isinstance(valeur, str):
                return valeur, ""
    return "", ""


_PIST_FR_AR = re.compile(r"(/jort/\d{4}/\d{4})F(/)Jo(\w+\.pdf)$")


def lien_reference(titre: str, lien: str, langue: str = "fr") -> str:
    """Titre de référence d'un paramètre, rendu en LIEN vers le Journal officiel.

    Les tableaux affichaient le titre seul, sans lien, alors que le paramètre porte l'adresse
    du fascicule : le lecteur ne pouvait pas remonter au texte. En arabe, l'adresse de
    l'édition française de pist.tn (`…/AAAAF/JoNNNAA.pdf`) est remplacée par celle de
    l'édition arabe (`…/AAAAA/JaNNNAA.pdf`), comme le veut la convention du précis. Sans
    lien, le titre seul ; sans titre, rien.
    """
    if not titre:
        return ""
    if not lien:
        return titre
    if langue == "ar":
        lien = _PIST_FR_AR.sub(r"\1A\2Ja\3", lien)
    titre_md = titre.replace("[", "\\[").replace("]", "\\]")
    return f"[{titre_md}]({lien})"


def serie_datee(chemin_relatif: str) -> list[tuple[str, float | None, str, str]]:
    """Série (date d'effet, valeur, titre de la référence, lien) d'un paramètre scalaire.

    Les dates sont rendues telles qu'elles figurent dans le paramètre : ce sont, dans ce
    dépôt, des **années de revenus**. Les références proviennent de `metadata.reference`,
    ce qui rend le tableau publié et le paramètre indissociables : corriger l'un corrige
    l'autre.
    """
    donnees = charge_parametre(chemin_relatif)
    if not donnees or "values" not in donnees:
        return []
    sortie = []
    for cle in sorted(donnees["values"].keys(), key=lambda k: (_annee(k), str(k))):
        brut = donnees["values"][cle]
        valeur = None
        if isinstance(brut, dict):
            valeur = brut.get("value")
        elif isinstance(brut, (int, float)):
            valeur = brut
        titre, lien = _reference_a_la_date(donnees, cle)
        sortie.append((str(cle)[:10], None if valeur is None else float(valeur), titre, lien))
    return sortie


def tableau_serie(
    chemin_relatif: str,
    colonne_valeur: str = "Valeur",
    formateur: Callable[[float | None], str] | None = None,
    avec_reference: bool = True,
) -> "pd.DataFrame | None":
    """Un paramètre scalaire, sous forme de tableau d'évolution daté et sourcé."""
    if pd is None:
        return None
    serie = serie_datee(chemin_relatif)
    if not serie:
        return None
    releve_note(chemin_relatif, colonne_valeur)
    if formateur is None:
        formateur = lambda v: "—" if v is None else formate_dinars(v)
    lignes = []
    for date, valeur, titre, lien in serie:
        ligne = {
            "À compter des revenus de": date[:4],
            colonne_valeur: formateur(valeur),
        }
        if avec_reference:
            ligne["Texte"] = lien_reference(titre, lien) or "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_evolution(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    cles: dict[str, str] | None = None,
    colonne_periode: str = "Années de revenus",
    derniere_annee: str = "2026",
    colonne_texte: str = "Texte",
    langue: str = "fr",
) -> "pd.DataFrame | None":
    """Plusieurs paramètres côte à côte, une ligne par période homogène.

    `specs` : (chemin du paramètre, en-tête de colonne, formateur).
    `cles`  : date d'effet -> clé de citation du précis, par exemple
              {"2017-01-01": "lf-2017, art. 14"}. La colonne « Texte » émet alors
              `[@clé]`, ce qui raccroche le tableau à la bibliographie ; à défaut,
              elle reprend le titre de la référence portée par le paramètre.

    Les bornes de période sont calculées sur l'union des dates de changement de tous
    les paramètres : une ligne couvre un intervalle pendant lequel aucune valeur ne bouge.
    """
    if pd is None:
        return None
    series = {}
    for chemin, entete, _f in specs:
        s = serie_datee(chemin)
        if not s:
            return None
        series[chemin] = s
        releve_note(chemin, entete)
    dates = sorted({d for s in series.values() for d, *_ in s})
    if not dates:
        return None

    def valeur_a(chemin, date):
        retenue = None
        for d, v, _t, _h in series[chemin]:
            if d <= date:
                retenue = v
        return retenue

    lignes = []
    for indice, date in enumerate(dates):
        debut = date[:4]
        fin = str(int(dates[indice + 1][:4]) - 1) if indice + 1 < len(dates) else derniere_annee
        periode = debut if debut == fin else f"{debut} → {fin}"
        ligne = {colonne_periode: periode}
        for chemin, entete, formateur in specs:
            ligne[entete] = formateur(valeur_a(chemin, date))
        texte = ""
        if cles and date in cles:
            texte = f"[@{cles[date]}]"
        else:
            for chemin, _e, _f in specs:
                for d, _v, titre, h in series[chemin]:
                    if d == date and titre:
                        texte = lien_reference(titre, h, langue)
                        break
                if texte:
                    break
        ligne[colonne_texte] = texte or "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# ------------------------------------------------------------------------ tableau


def tableau_bareme(
    chemin_relatif: str,
    date: datetime.date,
    colonne_tranche: str = "Tranche de revenu annuel net (dinars)",
    avec_taux_effectif: bool = False,
    langue: str = "fr",
    colonne_taux: str = "Taux de la tranche",
    colonne_taux_effectif: str = "Taux d’imposition du revenu global à la limite supérieure",
) -> "pd.DataFrame | None":
    """Barème en vigueur à `date`, sous forme de DataFrame prêt à publier."""
    if pd is None:
        return None
    tranches = bareme_a_la_date(chemin_relatif, date)
    if not tranches:
        return None
    effectifs = taux_effectifs_limite_superieure(tranches)
    lignes = []
    for indice, (seuil, taux) in enumerate(tranches):
        suivant = tranches[indice + 1][0] if indice + 1 < len(tranches) else None
        ligne = {
            colonne_tranche: libelle_tranche(seuil, suivant, langue),
            colonne_taux: formate_taux(taux),
        }
        if avec_taux_effectif:
            ligne[colonne_taux_effectif] = formate_taux_effectif(effectifs[indice])
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def _colonne_numerique(df: "pd.DataFrame", colonne: str) -> bool:
    """Vrai si toutes les cellules tiennent du nombre (chiffres, %, dinars, tiret)."""
    motif = re.compile(r"^[\d\s.,%—–+−-]+$|^.*\d.*(%|D)$")
    return all(motif.match(str(v).strip()) for v in df[colonne])


def tableau_vers_markdown(df: "pd.DataFrame", a_gauche: bool = False) -> str:
    """DataFrame -> tableau Markdown pipe.

    Seules les colonnes dont toutes les cellules sont numériques sont alignées à droite ;
    une colonne de texte, comme la référence du texte de loi, reste alignée à gauche.
    `a_gauche` aligne tout à gauche : un tableau dont les colonnes de périodes mêlent des
    valeurs et des états (« ligne inexistante ») se lit mieux d'un seul alignement.
    """
    colonnes = list(df.columns)
    lignes = ["| " + " | ".join(str(c) for c in colonnes) + " |"]
    lignes.append(
        "|"
        + "|".join(
            "---:" if i > 0 and not a_gauche and _colonne_numerique(df, c) else "---"
            for i, c in enumerate(colonnes)
        )
        + "|"
    )
    for _, ligne in df.iterrows():
        lignes.append("| " + " | ".join(str(ligne[c]) for c in colonnes) + " |")
    return "\n".join(lignes)


def lit_markdown_statique(chemin: str | Path) -> "pd.DataFrame | None":
    """Relit un snapshot Markdown pipe en DataFrame (lignes de commentaire ignorées)."""
    if pd is None:
        return None
    fichier = Path(chemin)
    if not fichier.is_file():
        return None
    lignes = [
        ligne.strip()
        for ligne in fichier.read_text(encoding="utf-8").splitlines()
        if ligne.strip().startswith("|")
    ]
    cellules = []
    for ligne in lignes:
        contenu = [c.strip() for c in ligne.split("|")[1:-1]]
        if contenu and not all(set(c) <= set("-:") for c in contenu if c):
            cellules.append(contenu)
    if not cellules:
        return None
    return pd.DataFrame(cellules[1:], columns=cellules[0])


# ------------------------------------------------------------------- prestations
#
# Les tableaux du livre « Fiscalité » sont datés en ANNÉES DE REVENUS : le mois est sans
# objet, une loi de finances prenant effet au 1er janvier. Ceux du livre « Prestations
# sociales » ne le supportent pas — la majoration pour salaire unique prend effet au 1er mai
# 1980, le plafond d'assiette au 1er mai 1986, la contribution aux frais de crèche au
# 1er octobre 1994. Réduire ces dates à l'année les rendrait fausses. D'où les fonctions
# ci-dessous, qui rendent la date d'effet au jour près et exposent l'attestation.

MOIS = {
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin",
           "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
    # Noms de mois en usage en Tunisie, hérités du calendrier grégorien tel qu'il est
    # imprimé au Journal officiel arabe — et non les noms du Machrek (كانون الثاني, …),
    # qui dérouteraient un lecteur tunisien.
    "ar": ["جانفي", "فيفري", "مارس", "أفريل", "ماي", "جوان",
           "جويلية", "أوت", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
}


def formate_date(date_iso: str, langue: str = "fr") -> str:
    """« 1980-05-01 » -> « 1^er^ mai 1980 » en français, « 1 ماي 1980 » en arabe.

    L'ordinal en exposant est une convention typographique française ; l'arabe
    n'ordinalise pas le premier jour du mois.
    """
    try:
        annee, mois, jour = (int(x) for x in str(date_iso)[:10].split("-"))
    except ValueError:
        return str(date_iso)
    if langue == "ar":
        return f"{jour} {MOIS['ar'][mois - 1]} {annee}"
    ordinal = "1^er^" if jour == 1 else str(jour)
    return f"{ordinal} {MOIS['fr'][mois - 1]} {annee}"


def formate_date_fr(date_iso: str) -> str:
    """Conservé pour compatibilité : `formate_date(date, "fr")`."""
    return formate_date(date_iso, "fr")


ATTESTATION = {
    "fr": ("texte établi", "**non établie**"),
    "ar": ("نصّ ثابت", "**غير ثابتة**"),
}


def attestation(titre: str, langue: str = "fr") -> str:
    """Niveau d'attestation d'une valeur, déduit de la présence d'une référence.

    Convention de lecture n° 3 du chapitre : une valeur que le paramètre ne rattache à
    aucun texte n'est pas présentée comme attestée. La colonne se calcule donc, elle ne
    se saisit pas — ajouter la référence au paramètre suffit à la faire basculer.
    """
    atteste, non_etabli = ATTESTATION.get(langue, ATTESTATION["fr"])
    return atteste if titre else non_etabli


def tableau_evolution_datee(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    cles: dict[str, str] | None = None,
    colonne_periode: str = "Effet",
    avec_attestation: bool = False,
    langue: str = "fr",
    colonne_texte: str = "Texte",
    colonne_attestation: str = "Attestation",
) -> "pd.DataFrame | None":
    """Comme `tableau_evolution`, mais une ligne par DATE D'EFFET rendue au jour près.

    `cles` : date ISO -> clé de citation du précis. À défaut, la colonne « Texte »
    reprend le titre de la référence portée par le paramètre lui-même.
    """
    if pd is None:
        return None
    series = {}
    for chemin, entete, _f in specs:
        s = serie_datee(chemin)
        if not s:
            return None
        series[chemin] = s
        releve_note(chemin, entete)
    dates = sorted({d for s in series.values() for d, *_ in s})
    if not dates:
        return None

    def valeur_a(chemin, date):
        retenue = None
        for d, v, _t, _h in series[chemin]:
            if d <= date:
                retenue = v
        return retenue

    def titre_a(date):
        for chemin, _e, _f in specs:
            for d, _v, titre, h in series[chemin]:
                if d == date and titre:
                    return titre, h
        return "", ""

    lignes = []
    for date in dates:
        ligne = {colonne_periode: formate_date(date, langue)}
        for chemin, entete, formateur in specs:
            ligne[entete] = formateur(valeur_a(chemin, date))
        titre, lien = titre_a(date)
        if cles and date in cles:
            ligne[colonne_texte] = f"[@{cles[date]}]"
        else:
            ligne[colonne_texte] = lien_reference(titre, lien, langue) or "—"
        if avec_attestation:
            ligne[colonne_attestation] = attestation(titre, langue)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_a_la_date(
    specs: list[tuple[str | tuple[str, ...], str, Callable[[float | None], str]]],
    date: str,
    cles: dict[str, str] | None = None,
    entetes: tuple[str, str, str] = ("Paramètre", "Valeur", "Texte"),
    colonne_effet: str | None = None,
    langue: str = "fr",
    separateur: str = " ; ",
) -> "pd.DataFrame | None":
    """Rendu VERTICAL — un paramètre par ligne — d'un dispositif à millésime unique.

    La contribution aux frais de crèche ou les aides ponctuelles de l'AMEN social n'ont
    qu'une seule date d'effet : les mettre en colonnes donnerait un tableau d'une ligne et
    de cinq colonnes hétérogènes (un montant, une durée, deux âges, un plafond). La lecture
    par ligne « Paramètre / Valeur / Texte » est celle du chapitre. Elle sert aussi de fiche
    d'un régime entier — âge, stage, taux, plafond, minimum —, à l'état en vigueur à `date`.

    `cles` : chemin du paramètre -> clé de citation ; à défaut, titre de la référence.
    Un chemin peut être un TUPLE de paramètres parallèles (les classes de revenus d'un
    régime) : la case aligne leurs valeurs, séparées par `separateur`, et la clé est celle
    du premier. `colonne_effet` : en-tête d'une colonne qui donne la date d'effet de la
    valeur retenue — utile quand les lignes n'ont pas toutes la même.
    """
    if pd is None:
        return None
    lignes = []
    for chemins, libelle, formateur in specs:
        groupe = chemins if isinstance(chemins, tuple) else (chemins,)
        valeurs, effet, titre_retenu, lien_retenu = [], "", "", ""
        for rang, chemin in enumerate(groupe, start=1):
            serie = serie_datee(chemin)
            if not serie:
                return None
            releve_note(chemin, libelle if len(groupe) == 1 else f"{libelle} ({rang})")
            retenue = None
            for d, v, titre, h in serie:
                if d <= date:
                    retenue = v
                    if rang == 1:
                        titre_retenu, lien_retenu = titre, h
                    if retenue is not None:
                        effet = max(effet, d)
            valeurs.append(formateur(retenue))
        premier = groupe[0]
        if cles and premier in cles:
            texte = f"[@{cles[premier]}]"
        else:
            texte = lien_reference(titre_retenu, lien_retenu, langue) or "—"
        ligne = {entetes[0]: libelle}
        if colonne_effet:
            ligne[colonne_effet] = formate_date(effet, langue) if effet else VIDE
        ligne[entetes[1]] = separateur.join(valeurs)
        ligne[entetes[2]] = texte
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# ----------------------------------------------- tableau mixte : gabarit de cellules
#
# MOTIF « VALEURS ENGENDRÉES + RÈGLES SAISIES » (recension du 2 octobre 2026, motif 1). Bien
# des tableaux du précis mêlent, dans une même case, une règle et une valeur : « la veuve,
# et le veuf invalide : 50 % », « salaires des trois ou cinq dernières années ». Ni un
# tableau de valeurs datées, qui perdrait la règle, ni un tableau écrit à la main, qui
# figerait la valeur, ne leur conviennent. Le gabarit garde le texte de la case, dans les
# deux langues, et y injecte chaque valeur lue dans le paramètre à la date qui la fonde :
# corriger le paramètre corrige la case.


class Lecture:
    """Une valeur de paramètre à une date, à injecter dans une case de gabarit.

    `formateur` : le nom d'une méthode de `Formateurs` (« taux », « age », « part_smig »,
    « coefficient »…), « duree:<unité> » (« duree:mois »), ou une fonction `(valeur, langue)
    -> texte`. `libelle` : {langue: libellé} du lien « Base législative ». Une valeur
    absente à la date — paramètre inconnu, valeur nulle — fait échouer le tableau : une case
    qui annonce une valeur ne se publie pas vide.
    """

    def __init__(self, chemin: str, date: str, formateur: str | Callable = "taux",
                 libelle: dict[str, str] | str | None = None):
        self.chemin, self.date, self.formateur, self.libelle = chemin, date, formateur, libelle

    def valeur(self) -> float:
        serie = serie_datee(self.chemin) or taux_datee(self.chemin)
        point = en_vigueur(serie, self.date)
        if point is None or point[1] is None:
            raise ValueError(f"{self.chemin} : aucune valeur au {self.date}")
        return point[1]

    def rendre(self, langue: str) -> str:
        v = self.valeur()
        if callable(self.formateur):
            return self.formateur(v, langue)
        f = formateurs(langue)
        if self.formateur.startswith("duree:"):
            return f.duree(self.formateur.split(":", 1)[1])(v)
        return getattr(f, self.formateur)(v)


def gabarit(texte: str | dict[str, str], **lectures: Lecture) -> tuple:
    """Une case de gabarit : un texte par langue, dont les `{nom}` reçoivent les lectures."""
    return ("gabarit", texte, lectures)


def tableau_gabarit(
    entetes: list[str],
    lignes: list[list[Any]],
    langue: str = "fr",
) -> "pd.DataFrame | None":
    """Tableau mixte : chaque case est un texte, ou un gabarit qui reçoit des valeurs lues.

    `lignes` : une liste de cases par ligne, dans l'ordre de `entetes`. Une case est
    - un texte commun aux deux langues (une clé de citation, un tiret) ;
    - un dictionnaire {langue: texte} ;
    - `gabarit(texte, nom=Lecture(...))`, dont les `{nom}` reçoivent la valeur lue.
    Chaque lecture est notée au relevé, sous le libellé de sa langue : l'onglet « Base
    législative » mène à chaque paramètre injecté.
    """
    if pd is None:
        return None

    def rendre(case: Any) -> str:
        if isinstance(case, tuple) and case and case[0] == "gabarit":
            _g, texte, lectures = case
            modele = texte[langue] if isinstance(texte, dict) else texte
            valeurs = {}
            for nom, lecture in lectures.items():
                valeurs[nom] = lecture.rendre(langue)
                libelle = lecture.libelle
                if isinstance(libelle, dict):
                    libelle = libelle.get(langue)
                releve_note(lecture.chemin, libelle)
            return modele.format(**valeurs)
        if isinstance(case, dict):
            return case[langue]
        return str(case)

    return pd.DataFrame([{e: rendre(c) for e, c in zip(entetes, cases)} for cases in lignes])


def taux_datee(chemin_relatif: str) -> list[tuple[str, float | None, str, str]]:
    """Série datée du taux d'un barème à UNE tranche : (date, taux, titre, lien).

    Les cotisations sociales sont encodées en `brackets` et non en `values`, même quand
    elles n'ont qu'un taux unique : `serie_datee` ne les voit donc pas. Ce lecteur prend
    le taux de la première tranche, ce qui couvre tous les régimes sauf celui des
    travailleurs à faibles revenus — le seul plafonné, qui relève de `tableau_bareme`.
    """
    donnees = charge_parametre(chemin_relatif)
    if not donnees or not donnees.get("brackets"):
        return []
    taux = donnees["brackets"][0].get("rate") or {}
    sortie = []
    for cle in sorted(taux.keys(), key=lambda k: (_annee(k), str(k))):
        brut = taux[cle]
        valeur = brut.get("value") if isinstance(brut, dict) else brut
        titre, lien = _reference_a_la_date(donnees, cle)
        sortie.append((str(cle)[:10], None if valeur is None else float(valeur), titre, lien))
    return sortie


def formate_points(ecart: float | None) -> str:
    """Écart entre deux taux, en points de pourcentage, signé : 0.012 -> « +1,2 »."""
    if ecart is None:
        return VIDE
    points = round(ecart * 100, 6)
    texte = f"{abs(points):.4f}".rstrip("0").rstrip(".").replace(".", ",")
    return ("+" if points > 0 else "−" if points < 0 else "") + texte


def tableau_taux_datee(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    cles: dict[str, str] | None = None,
    colonne_periode: str = "Effet",
    colonne_texte: str = "Texte",
    langue: str = "fr",
    colonne_variation: str | None = None,
    sans_maintien: bool = False,
    depuis: str | None = None,
    colonne_total: str | None = None,
) -> "pd.DataFrame | None":
    """Comme `tableau_evolution_datee`, mais pour des barèmes à une tranche.

    `sans_maintien` : écarte les dates où aucun taux ne change — un texte qui reconduit un
    taux n'est pas une étape de son évolution.

    `depuis` : première date d'effet publiée ; la première ligne porte les taux en vigueur à
    cette date. Sert à ne pas publier des états antérieurs qu'aucun texte n'établit.
    `colonne_total` : en-tête d'une colonne qui somme, ligne par ligne, les taux des `specs`
    (part de l'employeur et part de l'assuré).

    `colonne_variation` : en-tête d'une colonne qui donne, ligne par ligne, l'écart en points
    avec la ligne précédente — le changement concret qu'opère le texte de la ligne. Elle suit
    la colonne du premier taux, et reste vide à la première ligne.
    """
    if pd is None:
        return None
    series = {chemin: taux_datee(chemin) for chemin, _e, _f in specs}
    if not all(series.values()):
        return None
    for chemin, entete, _f in specs:
        releve_note(chemin, entete)
    dates = sorted({d for s in series.values() for d, *_ in s})

    def valeur_a(chemin, date):
        retenue = None
        for d, v, _t, _h in series[chemin]:
            if d <= date:
                retenue = v
        return retenue

    if sans_maintien:
        dates = [d for i, d in enumerate(dates) if i == 0 or any(
            valeur_a(c, d) != valeur_a(c, dates[i - 1]) for c, _e, _f in specs)]
    if depuis:
        dates = [d for d in dates if d >= depuis]
    lignes = []
    for date in dates:
        ligne = {colonne_periode: formate_date(date, langue)}
        for chemin, entete, formateur in specs:
            ligne[entete] = formateur(valeur_a(chemin, date))
        titre, lien = "", ""
        for chemin, _e, _f in specs:
            for d, _v, t, h in series[chemin]:
                if d == date and t:
                    titre, lien = t, h
                    break
            if titre:
                break
        if colonne_total:
            valeurs = [valeur_a(c, date) for c, _e, _f in specs]
            presentes = [v for v in valeurs if v is not None]
            ligne[colonne_total] = specs[0][2](sum(presentes) if presentes else None)
        if colonne_variation:
            chemin = specs[0][0]
            precedente = [d for d in dates if d < date]
            ligne[colonne_variation] = VIDE if not precedente else formate_points(
                (valeur_a(chemin, date) or 0) - (valeur_a(chemin, precedente[-1]) or 0))
        if cles and date in cles:
            ligne[colonne_texte] = f"[@{cles[date]}]"
        else:
            ligne[colonne_texte] = lien_reference(titre, lien, langue) or "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# ------------------------------------------- composants communs des générateurs de livres
#
# Remontés des générateurs des retraites, des prestations et de la fiscalité, où ils
# vivaient en deux ou trois versions divergentes (recension du 2 octobre 2026, « Composants
# restés locaux »). Un générateur les emploie tels quels ; il ne garde en propre que ce qui
# est propre à son livre — un libellé, une forme de cellule composée.

# L'arabe accorde le nom compté avec le nombre : singulier à 1, duel à 2, pluriel de 3 à 10,
# singulier à l'accusatif au-delà. « 60 سنوات » ou « 36 أشهر » sont des fautes que le
# lecteur voit, et elles seraient recopiées à chaque régénération. Le français n'a que le
# singulier et le pluriel.
NOMS_COMPTES = {
    "fr": {
        "ans": ("an", "ans"),
        "mois": ("mois", "mois"),
        "trimestres": ("trimestre", "trimestres"),
        "jours": ("jour", "jours"),
        "heures": ("heure", "heures"),
    },
    "ar": {
        "ans": ("سنة", "سنتان", "سنوات", "سنة"),
        "mois": ("شهر", "شهران", "أشهر", "شهرًا"),
        "trimestres": ("ثلاثية", "ثلاثيتان", "ثلاثيات", "ثلاثية"),
        "jours": ("يوم", "يومان", "أيام", "يومًا"),
        "heures": ("ساعة", "ساعتان", "ساعات", "ساعة"),
    },
}


def compte(n: int, unite: str | tuple[str, ...], langue: str = "fr") -> str:
    """Un nombre et son nom compté : « 120 mois », « 1 an », « 40 ثلاثية », « 10 ثلاثيات ».

    `unite` : une clé de `NOMS_COMPTES` (« ans », « mois », « trimestres »…), ou les formes
    elles-mêmes — (singulier, pluriel) en français, (singulier, duel, pluriel, accusatif)
    en arabe. En arabe, le singulier et le duel s'emploient seuls, sans chiffre.
    """
    formes = NOMS_COMPTES["ar" if langue == "ar" else "fr"][unite] \
        if isinstance(unite, str) else unite
    if langue != "ar":
        return f"{n} {formes[0] if n == 1 else formes[-1]}"
    if n == 1:
        return formes[0]
    if n == 2:
        return formes[1]
    # Au-delà de cent, le nom s'accorde avec la dernière composante du nombre : « 300 يوم »
    # (centaine pleine : singulier au génitif), « 103 أيام », « 180 يومًا ».
    reste = n % 100 if n > 100 else n
    if n > 100 and reste == 0:
        return f"{n} {formes[0]}"
    return f"{n} {formes[2]}" if 3 <= reste <= 10 else f"{n} {formes[3]}"


def annees(n: int, langue: str = "fr") -> str:
    """Un âge ou une durée en années accordées : « 60 ans », « 1 an », « 60 سنة »."""
    return compte(n, "ans", langue)


VIDE = "—"
UNITE_DINAR = {"fr": " D", "ar": " د"}
# Le salaire minimum auquel une fraction se rapporte, tel que l'écrivent les textes.
DU_SMIG = {"fr": "du SMIG", "ar": "من الأجر الأدنى المضمون"}


class Formateurs:
    """Les formateurs de cellules communs aux générateurs, dans la langue du livre.

    Une case sans valeur rend « — », jamais « 0 » : l'absence de règle n'est pas une valeur
    nulle. Les montants se déclinent en trois écritures, parce que les textes n'écrivent pas
    tous les sommes de la même façon :

    - `dinars` élague les zéros de queue — « 1 500 D », « 2,5 D » —, comme les plafonds
      fiscaux en dinars ;
    - `millimes` garde toujours trois décimales — « 7,600 D » —, comme le *Journal officiel*
      écrit les indemnités et les pensions ;
    - `montant` n'écrit les millimes que s'il y en a — « 50 D », « 18,750 D » —, comme les
      prestations.
    """

    def __init__(self, langue: str = "fr"):
        self.langue = langue
        self.unite = UNITE_DINAR.get(langue, UNITE_DINAR["fr"])

    def taux(self, v):
        return VIDE if v is None else formate_taux(v)

    def dinars(self, v):
        return VIDE if v is None else formate_dinars(v) + self.unite

    def millimes(self, v):
        if v is None:
            return VIDE
        return f"{v:,.3f}".replace(",", " ").replace(".", ",") + self.unite

    def montant(self, v):
        if v is None:
            return VIDE
        if float(v).is_integer():
            return f"{int(v):,}".replace(",", " ") + self.unite
        return self.millimes(v)

    def entier(self, v):
        return VIDE if v is None else str(int(v))

    def age(self, v):
        """Un âge, rendu en années accordées."""
        return VIDE if v is None else annees(int(v), self.langue)

    def duree(self, unite: str) -> Callable[[float | None], str]:
        """Formateur d'une durée comptée dans `unite` (« mois », « trimestres »…)."""
        return lambda v: VIDE if v is None else compte(int(v), unite, self.langue)

    def part_smig(self, v):
        """Une fraction du salaire minimum, rendue comme fraction et non en pourcentage.

        Les textes écrivent « les deux tiers du SMIG » et « la moitié du SMIG » ; le
        paramètre les approche par 0,66666 et 0,5. Imprimer « 66,67 % » donnerait un
        chiffre que ne porte aucun texte.
        """
        if v is None:
            return VIDE
        from fractions import Fraction

        fraction = Fraction(v).limit_denominator(12)
        return f"{fraction.numerator}/{fraction.denominator} {DU_SMIG[self.langue]}"

    def coefficient(self, v):
        """Un multiple d'un salaire minimum : « 2/3 », « 1 », « 1,5 », « 18 »."""
        if v is None:
            return VIDE
        from fractions import Fraction

        fraction = Fraction(v).limit_denominator(12)
        if fraction.denominator == 1:
            return str(fraction.numerator)
        if fraction.denominator == 3:
            return f"{fraction.numerator}/3"
        return f"{v:g}".replace(".", ",")


def formateurs(langue: str = "fr") -> Formateurs:
    return Formateurs(langue)


def en_vigueur(serie, date: str):
    """(date d'effet, valeur) en vigueur à `date` dans une série de `serie_datee`, ou None."""
    retenue = None
    for d, v, *_ in serie:
        if d <= date:
            retenue = (d, v)
    return retenue


def enchaine(segments, date: str):
    """Valeur en vigueur à `date` le long de séries successives, et son formateur.

    `segments` : [(série, formateur)], de la plus ancienne à la plus récente. Le régime des
    non-salariés en est l'exemple : l'état de 1982 prend fin, par une valeur nulle, le jour
    où commence celui du décret n° 95-1166. À date d'effet égale, la valeur non nulle
    l'emporte — la fin d'un état n'efface pas le début du suivant. Rend (None, None) quand
    aucune série n'a de valeur : la case restera vide, jamais à zéro.
    """
    meilleur = None
    for serie, formateur in segments:
        point = en_vigueur(serie, date)
        if point is None:
            continue
        rang = (point[0], point[1] is not None)
        if meilleur is None or rang >= meilleur[0]:
            meilleur = (rang, point[1], formateur)
    if meilleur is None or meilleur[1] is None:
        return None, None
    return meilleur[1], meilleur[2]


def cellule(*segments: tuple[str, Callable[[float | None], str]]):
    """Case d'une grandeur lue le long de séries successives : [(chemin, formateur)].

    Rend une fonction `(séries, date) -> texte`, la forme qu'attend `tableau_enchaine`.
    """
    def rendre(series, date):
        valeur, formateur = enchaine([(series[c], f) for c, f in segments], date)
        return VIDE if valeur is None else formateur(valeur)
    return rendre


def tableau_enchaine(lectures, colonnes, cles, langue="fr", colonne_periode="Effet",
                     colonne_texte="Texte") -> "pd.DataFrame | None":
    """Tableau daté — une ligne par date d'effet — dont une cellule peut lire plusieurs séries.

    Même forme que `tableau_evolution_datee`, dont il est le complément : colonne « Effet »,
    une colonne par grandeur, colonne « Texte » tirée des clés de citation. Il sert aux
    grandeurs qui commencent et s'arrêtent à des dates différentes : une case est vide quand
    la règle n'existe pas encore ou n'existe plus.

    `lectures` : [(chemin, libellé du lien)] — chaque paramètre lu, noté au relevé ; un
    libellé vide laisse la fabrique noter elle-même le nœud qui le contient.
    `colonnes` : [(en-tête, cellule)] où `cellule(séries, date)` rend le texte de la case.
    `cles` : date ISO -> clé de citation. Une date sans clé laisse la date elle-même dans la
    colonne « Texte », ce qu'un générateur doit refuser avant d'écrire le snapshot.
    """
    if pd is None:
        return None
    series = {}
    for chemin, libelle in lectures:
        serie = serie_datee(chemin)
        if not serie:
            print(f"✗ paramètre introuvable ou vide : {chemin}")
            return None
        series[chemin] = serie
        if libelle:
            releve_note(chemin, libelle)
    dates = sorted({d for serie in series.values() for d, *_ in serie})
    lignes = []
    for date in dates:
        ligne = {colonne_periode: formate_date(date, langue)}
        for entete, rendre in colonnes:
            ligne[entete] = rendre(series, date)
        ligne[colonne_texte] = f"[@{cles[date]}]" if date in cles else date
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# ------------------------------------------------------- les paramètres dans le temps
#
# DEUX VUES D'UNE MÊME DÉCLARATION. Un générateur déclare une liste de paramètres numériques
# — `ParametreDate` : chemin, libellés des deux langues, unité — et en tire :
#   - la SÉRIE LONGUE `precis/_seriescache/<nom>.csv`, une ligne par paramètre et par date
#     d'effet, que trace en escalier `figtools.figure_escalier` (`ecrire_serie_parametres`) ;
#   - le tableau de L'ÉTAT DU DROIT À DES DATES REPÈRES, un paramètre par ligne, une date par
#     colonne, `tables/<nom>_dates_reperes.md` (`ecrire_dates_reperes`).
# Les deux se lisent à la même règle : la valeur à une date est la dernière dont la date
# d'effet est antérieure ou égale ; une valeur nulle dit que le paramètre cesse d'exister, et
# l'on ne remonte pas au-delà (`etat_a_la_date`).
#
# CE QUE LA DÉCLARATION ENGAGE. Une marche d'escalier et une case de date repère affirment
# toutes deux qu'une valeur court de sa date d'effet à la suivante. Elles ne conviennent donc
# qu'à un paramètre dont l'historique est COMPLET : aucun texte intermédiaire non versé, et
# une fin datée quand la valeur a cessé de s'appliquer. Un paramètre qui encode une
# suppression par 0 plutôt que par une valeur nulle y tracerait une fausse marche à zéro.


class ParametreDate:
    """Un paramètre numérique daté, déclaré pour la série longue et le tableau aux dates repères.

    `cle`     : identifiant court du paramètre dans la série (« normal », « chef_de_famille »).
    `chemin`  : chemin du YAML, relatif au paquet (« parameters/…/taux.yaml »).
    `libelle` : {langue: libellé de ligne}.
    `unite`   : nom d'un formateur de `Formateurs` — « taux », « dinars », « montant »,
                « millimes », « entier » —, qui porte l'unité dans la case (« 17 % », « 150 D »).
    `format`  : fonction `(valeur, langue) -> texte`, quand aucun formateur commun ne convient.
    `lien`    : {langue: libellé du lien « Base législative »} ; à défaut, le libellé de ligne.
    """

    def __init__(self, cle: str, chemin: str, libelle: dict[str, str], unite: str = "taux",
                 format: Callable[[float, str], str] | None = None,
                 lien: dict[str, str] | None = None):
        self.cle, self.chemin, self.libelle, self.unite = cle, chemin, libelle, unite
        self.format, self.lien = format, lien or libelle

    def rendre(self, valeur: float | None, langue: str) -> str:
        """La case : la valeur dans son unité, ou « — » quand le paramètre n'existe pas."""
        if valeur is None:
            return VIDE
        if self.format is not None:
            return self.format(valeur, langue)
        return getattr(formateurs(langue), self.unite)(valeur)

    def serie(self) -> list[tuple[str, float | None, str, str]]:
        """(date d'effet, valeur, titre, lien) — paramètre scalaire ou barème à une tranche."""
        return serie_datee(self.chemin) or taux_datee(self.chemin)


def etat_a_la_date(serie, date: str) -> float | None:
    """Valeur en vigueur à `date` (ISO) dans une série de `serie_datee`, ou None.

    None dans deux cas, que le tableau rend tous deux par « — » : le paramètre n'est pas
    encore créé (aucune date d'effet antérieure ou égale), ou il est abrogé (la dernière
    valeur d'effet est nulle). Le jour même d'une date d'effet, c'est la valeur nouvelle
    qui vaut ; la veille, la précédente.
    """
    point = en_vigueur(serie, date)
    return None if point is None else point[1]


def lignes_serie_longue(series, colonne: str = "parametre",
                        avec_textes: bool = True) -> list[dict[str, Any]]:
    """Lignes de la série longue : une par paramètre et par date d'effet. Fonction pure.

    `series` : [(clé, série de `serie_datee`)], dans l'ordre de la déclaration — la série
    garde cet ordre, puis celui des dates. `colonne` : nom de la colonne qui porte la clé.
    Une ligne sans valeur dit la suppression du paramètre à cette date ; une ligne qui
    répète la valeur précédente dit un texte qui la reprend sans la changer.

    `avec_textes` : chaque ligne porte le premier texte que le paramètre cite à cette date
    et son lien au Journal officiel ; une date sans texte, ou dont le lien n'est pas sur
    pist.tn, lève une erreur — la série ne s'écrit pas avec une ligne sans source. Sans
    `avec_textes`, la série ne porte que les valeurs : ses textes sont alors ceux que cite
    la figure qui la trace.
    """
    lignes = []
    for cle, serie in series:
        for date, valeur, titre, lien in serie:
            ligne = {colonne: cle, "date_effet": date,
                     "valeur": None if valeur is None else round(valeur, 6)}
            if avec_textes:
                if not titre or not lien.startswith("https://www.pist.tn/"):
                    raise ValueError(f"{cle} au {date} sans texte au Journal officiel.")
                ligne["texte"], ligne["lien"] = titre, lien
            lignes.append(ligne)
    return lignes


def ecrire_csv_serie(fichier: str | Path, lignes: list[dict[str, Any]]) -> None:
    """Écrit la série longue en CSV, une valeur absente donnant une case vide.

    Par le module `csv`, et non par pandas : l'écriture se teste sans dépendance, et rend
    les mêmes octets (nombres par `repr`, guillemets au besoin seulement, fin de ligne LF).
    """
    import csv

    with Path(fichier).open("w", encoding="utf-8", newline="") as f:
        ecrivain = csv.DictWriter(f, fieldnames=list(lignes[0]), lineterminator="\n")
        ecrivain.writeheader()
        for ligne in lignes:
            ecrivain.writerow({c: "" if v is None else v for c, v in ligne.items()})


def ecrire_serie_parametres(nom: str, parametres: list[ParametreDate], cache: str | Path,
                            colonne: str = "parametre", avec_textes: bool = True,
                            langues: tuple[str, ...] = ("fr", "ar")) -> int:
    """Émet la série longue `<cache>/<nom>.csv` et ses liens `<nom>.liens.<langue>.yml`.

    Les valeurs sont brutes et n'ont pas de langue : la série est émise une fois ; seuls les
    libellés des liens « Base législative » sont écrits dans chaque langue. Rend 0, ou 1
    après avoir dit pourquoi la série n'est pas écrite — le snapshot existant est conservé.
    """
    series = [(p.cle, p.serie()) for p in parametres]
    vides = [p.chemin for p, (_c, s) in zip(parametres, series) if not s]
    if vides:
        print(f"✗ {nom} : paramètre introuvable ou vide : {vides}")
        return 1
    try:
        lignes = lignes_serie_longue(series, colonne=colonne, avec_textes=avec_textes)
    except ValueError as erreur:
        print(f"✗ {nom} : {erreur}")
        return 1
    cache = Path(cache)
    cache.mkdir(parents=True, exist_ok=True)
    ecrire_csv_serie(cache / f"{nom}.csv", lignes)
    for langue in langues:
        ecrire_fichier_liens(cache / f"{nom}.liens.{langue}.yml",
                             [(p.chemin, p.lien[langue]) for p in parametres], langue)
    print(f"✓ série {nom} : {len(lignes)} lignes, {len(parametres)} paramètres")
    return 0


def tableau_dates_reperes(
    parametres: list[ParametreDate],
    dates: list[str],
    langue: str = "fr",
    entete: str = "Paramètre",
    entetes_dates: dict[str, str] | None = None,
) -> "pd.DataFrame | None":
    """L'état du droit à des dates repères : un paramètre par ligne, une date par colonne.

    `dates` : dates ISO choisies par l'appelant, dans l'ordre des colonnes. Ce sont des
    CONSTANTES : une date mobile — celle du jour — ferait différer le snapshot d'une semaine
    à l'autre, et le contrôle de fraîcheur échouerait sans que rien n'ait changé.
    `entetes_dates` : date -> en-tête de colonne ; à défaut, la date au jour près
    (« 1^er^ juillet 1988 »). Une case rend la valeur en vigueur à la date, ou « — » quand
    le paramètre n'existe pas encore ou n'existe plus (`etat_a_la_date`).

    Chaque paramètre est noté au relevé sous le libellé de son lien : l'onglet « Base
    législative » du tableau mène à toutes ses valeurs datées et à leurs références.
    """
    if pd is None:
        return None
    lignes = []
    for p in parametres:
        serie = p.serie()
        if not serie:
            print(f"✗ paramètre introuvable ou vide : {p.chemin}")
            return None
        releve_note(p.chemin, p.lien[langue])
        ligne = {entete: p.libelle[langue]}
        for date in dates:
            colonne = (entetes_dates or {}).get(date) or formate_date(date, langue)
            ligne[colonne] = p.rendre(etat_a_la_date(serie, date), langue)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def ecrire_dates_reperes(racine: str | Path, livre: str, nom: str,
                         parametres: list[ParametreDate], dates: list[str],
                         entete: dict[str, str], generateur: str,
                         entetes_dates: dict[str, dict[str, str]] | None = None,
                         langues: tuple[str, ...] = ("fr", "ar")) -> int:
    """Écrit `precis/<langue>/<livre>/tables/<nom>_dates_reperes.md` et ses liens.

    `racine` : le dossier `precis`. `entete` : {langue: en-tête de la colonne des
    paramètres}. `entetes_dates` : {langue: {date: en-tête}}. `generateur` : nom du script
    appelant, inscrit dans le commentaire d'en-tête du snapshot. Rend 0, ou 1 en cas d'échec.
    """
    for langue in langues:
        df, liens = avec_liens(lambda: tableau_dates_reperes(
            parametres, dates, langue, entete=entete[langue],
            entetes_dates=(entetes_dates or {}).get(langue)))
        if df is None:
            print(f"échec : {langue}/{nom}_dates_reperes.md")
            return 1
        ecrire_tableau(
            Path(racine) / langue / livre / "tables" / f"{nom}_dates_reperes.md", df, liens,
            langue,
            entete=f"<!-- Généré par scripts/{generateur} — ne pas éditer à la main.\n"
                   f"     État en vigueur aux dates : {', '.join(dates)}.\n"
                   f"     Paramètres : {', '.join(p.chemin for p in parametres)} -->\n\n")
    return 0


def _enfants(chemin_noeud: str) -> list[tuple[str, bool]]:
    """Enfants d'un nœud de paramètres : [(nom, est_un_nœud)], dans l'ordre de son index.

    L'ordre est celui de `metadata.order` dans `index.yaml` — l'ordre du texte, que le
    tableau doit suivre ; les enfants qu'il omet suivent, par ordre alphabétique.
    """
    racine = _racine_paquet()
    if racine is None:
        return []
    ref = racine
    for element in chemin_noeud.split("/"):
        ref = ref / element
    if not ref.is_dir():
        return []
    noms = {}
    for enfant in ref.iterdir():
        if enfant.is_dir():
            noms[enfant.name] = True
        elif enfant.name.endswith(".yaml") and enfant.name != "index.yaml":
            noms[enfant.name.removesuffix(".yaml")] = False
    index = charge_parametre(f"{chemin_noeud}/index.yaml") or {}
    ordre = [n for n in ((index.get("metadata") or {}).get("order") or []) if n in noms]
    ordre += sorted(n for n in noms if n not in ordre)
    return [(n, noms[n]) for n in ordre]


def arborescence(chemin_noeud: str, prefixe: str = "") -> list[tuple[str, int, bool]]:
    """Parcours en profondeur d'un nœud : [(chemin relatif au nœud, profondeur, est_un_nœud)]."""
    sortie = []
    for nom, est_noeud in _enfants(chemin_noeud):
        relatif = f"{prefixe}{nom}"
        sortie.append((relatif, relatif.count("/"), est_noeud))
        if est_noeud:
            sortie += arborescence(f"{chemin_noeud}/{nom}", f"{relatif}/")
    return sortie


def tableau_arborescence(
    noeud_lignes: str,
    colonnes: list[tuple[str, str, str, Callable[[float | None], str]]],
    libelles: dict[str, str] | None = None,
    entete_libelle: str = "Secteur",
    retrait: str = "— ",
    numeros: dict[str, str] | None = None,
    entete_numero: str = "",
) -> "pd.DataFrame | None":
    """Pivot « catégorie × colonne » : une ligne par feuille d'un nœud, une colonne par lecture.

    Sert aux échelles de taux par secteur (accidents du travail) et, plus largement, à tout
    nœud dont les feuilles sont des catégories parallèles. Les lignes suivent l'arborescence
    de `noeud_lignes`, dans l'ordre de ses `index.yaml` ; un sous-nœud donne une ligne de
    regroupement, sans valeur, et ses feuilles sont mises en retrait.

    `colonnes` : (nœud, date ISO, en-tête, formateur). Chaque colonne lit, sous son nœud,
    la feuille de même chemin relatif que la ligne, au taux de sa première tranche, à la
    date donnée — ce qui permet de juxtaposer deux nœuds de même arborescence (avant et
    après un transfert) ou un même nœud à deux dates. Une feuille absente d'un nœud, ou sans
    valeur à la date, donne « — ».

    `libelles` : chemin relatif -> libellé de ligne. À défaut, le `short_label` du paramètre
    (ou de l'`index.yaml` du sous-nœud). Un libellé introuvable fait échouer le tableau :
    une ligne sans nom ne se publie pas. En arabe, le générateur fournit TOUS les libellés,
    transcrits de l'édition arabe du texte — les `short_label` sont en français.

    `numeros` : chemin relatif -> numéro de la ligne dans le texte (« 3-1 »), rendu dans une
    première colonne `entete_numero`.
    """
    if pd is None:
        return None
    lignes_arbre = arborescence(noeud_lignes)
    if not lignes_arbre:
        return None
    libelles = libelles or {}
    lignes = []
    for relatif, profondeur, est_noeud in lignes_arbre:
        if relatif in libelles:
            libelle = libelles[relatif]
        else:
            fichier = f"{noeud_lignes}/{relatif}/index.yaml" if est_noeud else f"{noeud_lignes}/{relatif}.yaml"
            libelle = ((charge_parametre(fichier) or {}).get("metadata") or {}).get("short_label")
        if not libelle:
            raise ValueError(f"ligne sans libellé : {noeud_lignes}/{relatif}")
        ligne = {entete_numero: numeros.get(relatif, "")} if numeros is not None else {}
        ligne[entete_libelle] = retrait * profondeur + libelle
        for noeud, date, entete, formateur in colonnes:
            if est_noeud:
                ligne[entete] = ""
                continue
            chemin = f"{noeud}/{relatif}.yaml"
            serie = taux_datee(chemin)
            retenue = None
            for d, v, _t, _h in serie:
                if d <= date:
                    retenue = v
            if serie:
                releve_note(chemin, f"{libelle} — {entete}")
            ligne[entete] = formateur(retenue) if retenue is not None else "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# COLONNE DE TEXTES. Tout tableau engendré est inséré dans un bloc `.tableau-engendre`. En HTML,
# le script de `precis/legendes.html` y repère la colonne des textes de loi — celle dont l'en-tête
# est exactement « Texte » ou « النصّ », les deux seuls qu'emploient les générateurs —, la masque
# et en reporte le contenu rendu dans une infobulle portée par la première cellule de la ligne.
# Le snapshot, lui, ne change pas : la colonne reste dans le Markdown, où Pandoc résout ses
# citations. Sans script, et en PDF, elle s'affiche telle quelle. Un tableau fait main adopte le
# même comportement en se plaçant dans un bloc de cette classe.
CLASSE_ENGENDRE = "tableau-engendre"


def bloc_engendre(tableau: str) -> str:
    """Enveloppe un tableau Markdown du bloc `.tableau-engendre`."""
    return f"::: {{.{CLASSE_ENGENDRE}}}\n\n{tableau.rstrip()}\n\n:::\n"


def markdown_avec_legende(
    chemin: str | Path, legende: str, label: str, colonnes: str = "",
    niveau: int = 2, arborescence: bool = False,
) -> str:
    """Rend un snapshot en tableau Markdown légendé, pour un chunk `#| output: asis`.

    POURQUOI PASSER PAR LÀ. Un DataFrame stylé est émis en HTML : Pandoc reçoit du balisage
    déjà cuit, et les citations qu'il contient — `[@lf-2017, art. 14]` — ne sont jamais vues
    par citeproc. Elles s'impriment alors telles quelles dans la page. En émettant du
    Markdown, la table et ses citations sont analysées par Pandoc : les clés se résolvent et
    la légende porte une ancre `@tbl-…` référençable dans le texte.

    `colonnes` : spécification facultative de largeur, par exemple `{tbl-colwidths="[20,80]"}`.

    `niveau` : niveau de titre des onglets « Tableau / Base législative » ; 3 quand le tableau
    est lui-même placé sous un onglet (`markdown_onglets`).

    `arborescence` : le tableau vient de `tableau_arborescence` ; en HTML, ses lignes de
    regroupement deviennent dépliables (voir `SCRIPT_ARBORESCENCE`). Ailleurs — PDF, Markdown —
    il reste un tableau ordinaire, ses retraits « — » disant la hiérarchie.
    """
    fichier = Path(chemin)
    if not fichier.is_file():
        return MESSAGE_INDISPONIBLE
    corps = fichier.read_text(encoding="utf-8").rstrip()
    attributs = f"{{#{label}}}" if not colonnes else f"{{#{label} {colonnes}}}"
    tableau = f"{corps}\n\n: {legende} {attributs}\n"
    if arborescence:
        tableau = (f"{_script_arborescence()}::: {{.{CLASSE_ENGENDRE} .tableau-arborescence}}"
                   f"\n\n{tableau}\n:::\n")
    else:
        tableau = bloc_engendre(tableau)
    liens = fichier.with_suffix(".liens.yml")
    if not liens.is_file() or yaml is None:
        return tableau
    langue = "ar" if "ar" in fichier.resolve().parts[-4:-2] else "fr"
    m = ONGLETS[langue]
    items = "\n".join(f"- [{e['libelle']}]({e['url']})"
                       for e in yaml.safe_load(liens.read_text(encoding="utf-8")) or [])
    titre = "#" * niveau
    return (f"::: {{.panel-tabset}}\n\n{titre} {m['tableau']}\n\n{tableau}\n"
            f"{titre} {m['base']}\n\n{m['intro']}\n\n{items}\n\n:::\n")


def markdown_onglets(panneaux: list[tuple[str, str | Path, str, str]], **options) -> str:
    """Plusieurs tableaux sous des onglets — une période, une année, une échelle par onglet.

    Évite d'empiler dans la page des tableaux qui se lisent l'un OU l'autre, et d'élargir un
    tableau d'autant de colonnes que de dates. `panneaux` : (titre de l'onglet, snapshot,
    légende, label) ; chaque tableau garde sa légende, son ancre `@tbl-…` et ses propres
    onglets « Tableau / Base législative », un niveau de titre plus bas. `options` passe à
    `markdown_avec_legende` (`colonnes`, `arborescence`).
    """
    corps = "".join(f"## {titre}\n\n{markdown_avec_legende(chemin, legende, label, niveau=3, **options)}\n"
                    for titre, chemin, legende, label in panneaux)
    return f"::: {{.panel-tabset}}\n\n{corps}:::\n"


def markdown_un_tableau_en_onglets(
    panneaux: list[tuple[str, str | Path, str]], legende: str, label: str,
) -> str:
    """UN tableau dont les états successifs — un barème par année, par exemple — sont des onglets.

    À la différence de `markdown_onglets`, qui juxtapose des tableaux distincts, chacun avec sa
    légende et son ancre, celui-ci n'a qu'une légende et qu'une ancre `@tbl-…` : c'est la même
    grandeur à plusieurs dates. Un seul onglet « Base législative » réunit, sans doublon, les
    liens de tous les états, qui renvoient d'ordinaire au même paramètre.

    `panneaux` : (titre de l'onglet, snapshot, note) ; la note — la source de cet état, par
    exemple — s'imprime sous le tableau de l'onglet, et peut être vide.

    Quarto accepte un tableau légendé fait d'un bloc `::: {#tbl-…}` dont le contenu est
    libre : ici des onglets, chacun portant un tableau sans légende (vérifié le 4 octobre 2026).
    """
    onglets, liens = [], {}
    for titre, chemin, note in panneaux:
        fichier = Path(chemin)
        if not fichier.is_file():
            return MESSAGE_INDISPONIBLE
        corps = fichier.read_text(encoding="utf-8").rstrip()
        corps = bloc_engendre(corps).rstrip()
        onglets.append(f"### {titre}\n\n{corps}\n\n{note}\n" if note else f"### {titre}\n\n{corps}\n")
        fichier_liens = fichier.with_suffix(".liens.yml")
        if fichier_liens.is_file() and yaml is not None:
            for e in yaml.safe_load(fichier_liens.read_text(encoding="utf-8")) or []:
                liens.setdefault(e["url"], e["libelle"])
    tableau = (f"::: {{#{label}}}\n\n::: {{.panel-tabset}}\n\n" + "\n".join(onglets)
               + f"\n:::\n\n{legende}\n\n:::\n")
    if not liens:
        return tableau
    langue = "ar" if "ar" in Path(panneaux[0][1]).resolve().parts[-4:-2] else "fr"
    m = ONGLETS[langue]
    items = "\n".join(f"- [{libelle}]({url})" for url, libelle in liens.items())
    return (f"::: {{.panel-tabset}}\n\n## {m['tableau']}\n\n{tableau}\n"
            f"## {m['base']}\n\n{m['intro']}\n\n{items}\n\n:::\n")


# LIGNES DÉPLIABLES. Un tableau d'arborescence (`tableau_arborescence`) marque ses niveaux par
# un retrait « — » en tête du libellé. En HTML, ce script lit ce retrait : une ligne suivie de
# lignes plus profondes devient un regroupement, replié par défaut, qui se déplie au clic ;
# le retrait textuel est remplacé par une marge. Il ne dépend que de ce marquage : tout tableau
# placé dans un bloc `.tableau-arborescence` en bénéficie. Émis une fois par page.
SCRIPT_ARBORESCENCE = """```{=html}
<style>
.tableau-arborescence tr.groupe { cursor: pointer; font-weight: 600; }
.tableau-arborescence tr.groupe .bascule { display: inline-block; width: 1.2em; }
.tableau-arborescence tr.masque { display: none; }
.tableau-arborescence .tout { font-size: .85em; margin: .3em 0; }
</style>
<script>
document.addEventListener("DOMContentLoaded", () => {
  const ar = (document.documentElement.lang || "").startsWith("ar");
  const mots = ar ? ["عرض الكلّ", "طيّ الكلّ"] : ["Tout déplier", "Tout replier"];
  const fleches = { ferme: ar ? "◂" : "▸", ouvert: "▾" };
  document.querySelectorAll(".tableau-arborescence table").forEach((table) => {
    const lignes = [...table.querySelectorAll("tbody tr")];
    const col = (() => {
      for (const tr of lignes) {
        const i = [...tr.cells].findIndex((td) => td.textContent.trim().startsWith("—"));
        if (i >= 0) return i;
      }
      return -1;
    })();
    if (col < 0) return;
    const entete = table.querySelector("thead tr");
    if (entete && entete.cells[col]) entete.cells[col].style.textAlign = "start";
    const infos = lignes.map((tr) => {
      const td = tr.cells[col];
      const m = td.textContent.trim().match(/^((?:—\s*)*)/);
      const prof = (m[1].match(/—/g) || []).length;
      td.style.textAlign = "start";
      if (prof) {
        const w = document.createTreeWalker(td, NodeFilter.SHOW_TEXT);
        let n;
        while ((n = w.nextNode()) && !n.textContent.trim());
        if (n) n.textContent = n.textContent.replace(/^(\s*—\s*)+/, "");
        td.style.paddingInlineStart = (prof * 1.4 + 0.4) + "em";
      }
      return { tr, prof };
    });
    const parents = [];
    const pile = [];
    infos.forEach((info, i) => {
      while (pile.length && infos[pile[pile.length - 1]].prof >= info.prof) pile.pop();
      parents.push(pile.length ? pile[pile.length - 1] : -1);
      pile.push(i);
    });
    const groupes = new Set(parents.filter((p) => p >= 0));
    const rafraichir = () => infos.forEach((info, i) => {
      const b = info.tr.querySelector(".bascule");
      if (b) b.textContent = info.tr.classList.contains("ouvert") ? fleches.ouvert : fleches.ferme;
      let p = parents[i], visible = true;
      while (p >= 0) {
        if (!infos[p].tr.classList.contains("ouvert")) { visible = false; break; }
        p = parents[p];
      }
      info.tr.classList.toggle("masque", !visible);
    });
    groupes.forEach((i) => {
      const tr = infos[i].tr;
      tr.classList.add("groupe");
      tr.cells[col].insertAdjacentHTML("afterbegin", '<span class="bascule">▸</span>');
      tr.addEventListener("click", () => { tr.classList.toggle("ouvert"); rafraichir(); });
    });
    rafraichir();
    const bouton = document.createElement("button");
    bouton.className = "btn btn-sm btn-outline-secondary tout";
    bouton.textContent = mots[0];
    bouton.addEventListener("click", () => {
      const tout = bouton.textContent === mots[0];
      groupes.forEach((i) => infos[i].tr.classList.toggle("ouvert", tout));
      rafraichir();
      bouton.textContent = tout ? mots[1] : mots[0];
    });
    table.before(bouton);
  });
});
</script>
```

"""
_script_arborescence_emis = False


def _script_arborescence() -> str:
    """Le script des lignes dépliables, la première fois seulement dans la page."""
    global _script_arborescence_emis
    if _script_arborescence_emis:
        return ""
    _script_arborescence_emis = True
    return SCRIPT_ARBORESCENCE


# Intitulés des onglets d'un tableau engendré, dans la langue du livre.
ONGLETS = {
    "fr": {"tableau": "📋 Tableau", "base": "⚖️ Base législative",
           "intro": "Chaque grandeur du tableau, avec toutes ses valeurs datées et leurs "
                    "références :"},
    "ar": {"tableau": "📋 الجدول", "base": "⚖️ القاعدة التشريعية",
           "intro": "كلّ مقدار في الجدول، بجميع قيمه المؤرّخة ومراجعها:"},
}


def get_table_or_static(
    fonction_openfisca: Callable[[], "pd.DataFrame | None"],
    chemin_statique: str | Path,
    variable_env: str = "PRECIS_USE_OPENFISCA_TABLES",
) -> "pd.DataFrame | None":
    """Lit le barème dans openfisca s'il est disponible et assez récent, sinon le snapshot.

    Mettre `PRECIS_USE_OPENFISCA_TABLES=false` force le snapshot.
    """
    autorise = os.environ.get(variable_env, "true").lower() in ("true", "1", "yes")
    if autorise and openfisca_utilisable():
        df = fonction_openfisca()
        if df is not None and not df.empty:
            return df
    return lit_markdown_statique(chemin_statique)
