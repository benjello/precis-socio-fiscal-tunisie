"""Construction des tableaux de barèmes à partir des paramètres openfisca-tunisia.

Pendant tunisien de `quarto/openfisca_tables/core.py` du dépôt `conversion_precis_ipp`,
adapté à ce dont le précis a besoin : des **barèmes à tranches** (`brackets:`), là où le
module d'origine ne traite que des paramètres scalaires (`values:`).

Principe, aligné sur celui de `figtools.py` : **le build du site est autonome.**
`openfisca-tunisia` n'est pas une dépendance déclarée du précis. Les tableaux publiés
proviennent de snapshots Markdown versionnés (`precis/fr/fiscalite/tables/`), régénérés à
la demande par `scripts/generate_bareme_tables.py`. Quand une version suffisante
d'openfisca-tunisia est installée, `get_table_or_static` bascule automatiquement sur la
lecture directe des paramètres.

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


VERSION_MINIMALE = (0, 76)

MESSAGE_INDISPONIBLE = (
    "*Tableau non disponible : ni openfisca-tunisia installé, ni snapshot statique.*"
)


# --------------------------------------------------------------------------- accès


def _racine_paquet():
    """Racine des sources openfisca-tunisia, ou None.

    Cherche d'abord le paquet installé, puis un checkout désigné par la variable
    d'environnement `OPENFISCA_TUNISIA_PATH` (utilisée pour régénérer les snapshots
    depuis une copie de travail non publiée).
    """
    try:
        import importlib.resources

        return importlib.resources.files("openfisca_tunisia")
    except Exception:
        pass
    chemin = os.environ.get("OPENFISCA_TUNISIA_PATH")
    if chemin:
        racine = Path(chemin) / "openfisca_tunisia"
        if racine.is_dir():
            return racine
    return None


def version_openfisca() -> tuple[int, ...] | None:
    """Version d'openfisca-tunisia disponible, sous forme de tuple, ou None."""
    try:
        from importlib.metadata import version

        return tuple(int(x) for x in version("openfisca-tunisia").split(".")[:2])
    except Exception:
        pass
    racine = _racine_paquet()
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


def openfisca_utilisable() -> bool:
    """Vrai si openfisca-tunisia est disponible ET assez récent pour être lu."""
    if yaml is None or _racine_paquet() is None:
        return False
    version = version_openfisca()
    return version is not None and version >= VERSION_MINIMALE


def charge_parametre(chemin_relatif: str) -> dict[str, Any] | None:
    """Charge un YAML de paramètre, chemin relatif à la racine du paquet.

    Exemple : "parameters/impot_revenu/bareme.yaml".
    """
    if yaml is None:
        return None
    racine = _racine_paquet()
    if racine is None:
        return None
    try:
        ref = racine
        for element in chemin_relatif.split("/"):
            ref = ref / element
        return yaml.safe_load(ref.read_text(encoding="utf-8"))
    except Exception:
        return None


# ------------------------------------------------------------------- lecture datée


def _annee(cle: Any) -> int:
    return cle.year if hasattr(cle, "year") else int(str(cle)[:4])


def valeur_a_la_date(bloc: dict[str, Any] | None, date: datetime.date) -> float | None:
    """Valeur en vigueur à `date` dans un bloc daté {date: {value: x}}.

    Renvoie None si la valeur en vigueur est nulle : dans openfisca, `value: null`
    signifie que le paramètre cesse d'exister à cette date. On ne remonte alors pas
    au-delà — c'est ce qui permet à une tranche de disparaître d'un barème.
    """
    if not bloc:
        return None
    for cle in sorted(bloc.keys(), key=lambda k: (_annee(k), str(k)), reverse=True):
        if _annee(cle) > date.year:
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
    if formateur is None:
        formateur = lambda v: "—" if v is None else formate_dinars(v)
    lignes = []
    for date, valeur, titre, _lien in serie:
        ligne = {
            "À compter des revenus de": date[:4],
            colonne_valeur: formateur(valeur),
        }
        if avec_reference:
            ligne["Texte"] = titre or "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_evolution(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    cles: dict[str, str] | None = None,
    colonne_periode: str = "Années de revenus",
    derniere_annee: str = "2026",
    colonne_texte: str = "Texte",
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
    for chemin, _entete, _f in specs:
        s = serie_datee(chemin)
        if not s:
            return None
        series[chemin] = s
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
                for d, _v, titre, _h in series[chemin]:
                    if d == date and titre:
                        texte = titre
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
    motif = re.compile(r"^[\d\s.,%—–-]+$|^.*\d.*(%|D)$")
    return all(motif.match(str(v).strip()) for v in df[colonne])


def tableau_vers_markdown(df: "pd.DataFrame") -> str:
    """DataFrame -> tableau Markdown pipe.

    Seules les colonnes dont toutes les cellules sont numériques sont alignées à droite ;
    une colonne de texte, comme la référence du texte de loi, reste alignée à gauche.
    """
    colonnes = list(df.columns)
    lignes = ["| " + " | ".join(str(c) for c in colonnes) + " |"]
    lignes.append(
        "|"
        + "|".join(
            "---:" if i > 0 and _colonne_numerique(df, c) else "---"
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
    "fr": ("texte lu", "**non établie**"),
    "ar": ("نصّ مقروء", "**غير ثابتة**"),
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
    for chemin, _entete, _f in specs:
        s = serie_datee(chemin)
        if not s:
            return None
        series[chemin] = s
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
            for d, _v, titre, _h in series[chemin]:
                if d == date and titre:
                    return titre
        return ""

    lignes = []
    for date in dates:
        ligne = {colonne_periode: formate_date(date, langue)}
        for chemin, entete, formateur in specs:
            ligne[entete] = formateur(valeur_a(chemin, date))
        titre = titre_a(date)
        if cles and date in cles:
            ligne[colonne_texte] = f"[@{cles[date]}]"
        else:
            ligne[colonne_texte] = titre or "—"
        if avec_attestation:
            ligne[colonne_attestation] = attestation(titre, langue)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_a_la_date(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    date: str,
    cles: dict[str, str] | None = None,
    entetes: tuple[str, str, str] = ("Paramètre", "Valeur", "Texte"),
) -> "pd.DataFrame | None":
    """Rendu VERTICAL — un paramètre par ligne — d'un dispositif à millésime unique.

    La contribution aux frais de crèche ou les aides ponctuelles de l'AMEN social n'ont
    qu'une seule date d'effet : les mettre en colonnes donnerait un tableau d'une ligne et
    de cinq colonnes hétérogènes (un montant, une durée, deux âges, un plafond). La lecture
    par ligne « Paramètre / Valeur / Texte » est celle du chapitre.

    `cles` : chemin du paramètre -> clé de citation ; à défaut, titre de la référence.
    """
    if pd is None:
        return None
    lignes = []
    for chemin, libelle, formateur in specs:
        serie = serie_datee(chemin)
        if not serie:
            return None
        retenue, titre_retenu = None, ""
        for d, v, titre, _h in serie:
            if d <= date:
                retenue, titre_retenu = v, titre
        if cles and chemin in cles:
            texte = f"[@{cles[chemin]}]"
        else:
            texte = titre_retenu or "—"
        lignes.append(dict(zip(entetes, (libelle, formateur(retenue), texte))))
    return pd.DataFrame(lignes)


def markdown_avec_legende(
    chemin: str | Path, legende: str, label: str, colonnes: str = ""
) -> str:
    """Rend un snapshot en tableau Markdown légendé, pour un chunk `#| output: asis`.

    POURQUOI PASSER PAR LÀ. Un DataFrame stylé est émis en HTML : Pandoc reçoit du balisage
    déjà cuit, et les citations qu'il contient — `[@lf-2017, art. 14]` — ne sont jamais vues
    par citeproc. Elles s'impriment alors telles quelles dans la page. En émettant du
    Markdown, la table et ses citations sont analysées par Pandoc : les clés se résolvent et
    la légende porte une ancre `@tbl-…` référençable dans le texte.

    `colonnes` : spécification facultative de largeur, par exemple `{tbl-colwidths="[20,80]"}`.
    """
    fichier = Path(chemin)
    if not fichier.is_file():
        return MESSAGE_INDISPONIBLE
    corps = fichier.read_text(encoding="utf-8").rstrip()
    attributs = f"{{#{label}}}" if not colonnes else f"{{#{label} {colonnes}}}"
    return f"{corps}\n\n: {legende} {attributs}\n"


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
