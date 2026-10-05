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
  - La série brute `marche-travail-smig-smag` (`_seriescache/`), que lisent les figures de
    la longue période, et ses liens « Base législative » en deux langues.

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
    return serie_figures()


if __name__ == "__main__":
    raise SystemExit(main())
