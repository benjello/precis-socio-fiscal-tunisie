"""Tests du registre des recherches infructueuses (`scripts/recherches.py`).

Le texte du précis ne raconte plus ses recherches : il porte une ancre
`<!-- RECHERCHE r-… -->` vers une fiche de `docs/recherches.yml`, que l'outil rejoue.
Trois choses doivent tenir :

  - `verifier`, lancé en CI, attrape toute désynchronisation entre ancres et fiches —
    sinon une réserve perd sa trace, ou une trace survit à sa réserve ;
  - `relancer` n'examine que ce qui est paru depuis la couverture de la dernière passe,
    et cherche chaque terme par DEUX voies (FTS et LIKE, accents neutralisés) : le faux
    négatif du `LIKE` accentué (`docs/notes/outillage-sources.md`, § 1 c) a déjà fait
    conclure à tort à l'absence d'un texte ;
  - une fiche est « périmée » quand la base connaît des publications plus récentes que
    ce que sa dernière passe couvre.

Les tests tournent sans PyYAML (le job de CI n'installe rien) : ils passent des fiches
en dictionnaires. Seul le test de forme canonique du registre versionné l'exige.
"""

import contextlib
import io
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import recherches as r  # noqa: E402

try:
    import yaml  # noqa: F401
    AVEC_YAML = True
except ImportError:
    AVEC_YAML = False


def fiche(**autres):
    base = {
        "id": "r-exemple",
        "objet": "décret d'application de l'article 33",
        "ou": ["precis/fr/livre/chap.qmd#sec-regime"],
        "requetes": {
            "titres_fts": ['"travailleuses agricoles"'],
            "titres_like": ["%sécurité sociale des pêcheurs%"],
            "depuis": "2024-10-23",
        },
        "passes": [{
            "date": "2026-01-05",
            "role": "documentaliste",
            "sources": ["jort_cache"],
            "couverture": "jort_cache jusqu'au 31 décembre 2025",
            "couvert_jusqu_au": "2025-12-31",
            "resultat": "aucun",
        }],
    }
    base.update(autres)
    return base


class Depot(unittest.TestCase):
    """Un faux dépôt : precis/fr/livre/chap.qmd, avec ou sans ancre."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.racine = Path(self._tmp.name)
        (self.racine / "precis" / "fr" / "livre").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def chapitre(self, texte):
        (self.racine / "precis" / "fr" / "livre" / "chap.qmd").write_text(texte, encoding="utf-8")

    def verifie(self, fiches):
        return r.verifie(fiches, self.racine)


AVEC_ANCRE = """## Le régime {#sec-regime}

Ce décret n'est pas identifié ici.

<!-- RECHERCHE r-exemple : décret d'application de l'art. 33 -->
"""


class VerifierTest(Depot):
    def test_registre_coherent(self):
        self.chapitre(AVEC_ANCRE)
        self.assertEqual(self.verifie([fiche()]), [])

    def test_ancre_orpheline(self):
        self.chapitre(AVEC_ANCRE + "\n<!-- RECHERCHE r-inconnue : rien -->\n")
        erreurs = self.verifie([fiche()])
        self.assertEqual(len(erreurs), 1)
        self.assertIn("ancre orpheline", erreurs[0])
        self.assertIn("r-inconnue", erreurs[0])

    def test_fiche_orpheline(self):
        self.chapitre("## Le régime {#sec-regime}\n\nSans ancre.\n")
        erreurs = self.verifie([fiche()])
        self.assertEqual(len(erreurs), 1)
        self.assertIn("fiche orpheline", erreurs[0])

    def test_fiche_resolue_sans_ancre_admise(self):
        self.chapitre("## Le régime {#sec-regime}\n\nLa règle, sourcée.\n")
        self.assertEqual(self.verifie([fiche(resolu="decret2026-12")]), [])

    def test_fiche_resolue_dont_l_ancre_subsiste(self):
        self.chapitre(AVEC_ANCRE)
        erreurs = self.verifie([fiche(resolu="decret2026-12")])
        self.assertEqual(len(erreurs), 1)
        self.assertIn("résolue", erreurs[0])

    def test_champ_manquant(self):
        self.chapitre(AVEC_ANCRE)
        f = fiche()
        del f["objet"]
        erreurs = self.verifie([f])
        self.assertTrue(any("« objet »" in e for e in erreurs), erreurs)

    def test_champ_manquant_dans_une_passe(self):
        self.chapitre(AVEC_ANCRE)
        f = fiche()
        del f["passes"][0]["couvert_jusqu_au"]
        erreurs = self.verifie([f])
        self.assertTrue(any("couvert_jusqu_au" in e for e in erreurs), erreurs)

    def test_date_non_iso(self):
        self.chapitre(AVEC_ANCRE)
        f = fiche()
        f["passes"][0]["date"] = "18 septembre 2026"
        f["requetes"]["depuis"] = "2024-13-01"
        erreurs = self.verifie([f])
        self.assertEqual(len(erreurs), 2, erreurs)

    def test_id_en_double(self):
        self.chapitre(AVEC_ANCRE)
        erreurs = self.verifie([fiche(), fiche()])
        self.assertTrue(any("en double" in e for e in erreurs), erreurs)

    def test_source_inconnue(self):
        self.chapitre(AVEC_ANCRE)
        f = fiche()
        f["passes"][0]["sources"] = ["google"]
        self.assertTrue(any("source inconnue" in e for e in self.verifie([f])))

    def test_ancre_hors_du_fichier_designe(self):
        self.chapitre("## Le régime {#sec-regime}\n")
        (self.racine / "precis" / "fr" / "livre" / "autre.qmd").write_text(
            "<!-- RECHERCHE r-exemple : ailleurs -->\n", encoding="utf-8")
        erreurs = self.verifie([fiche()])
        self.assertTrue(any("pas dans le fichier désigné" in e for e in erreurs), erreurs)

    def test_section_apres_une_classe(self):
        self.chapitre(AVEC_ANCRE.replace("{#sec-regime}", "{.unnumbered #sec-regime}"))
        self.assertEqual(self.verifie([fiche()]), [])

    def test_section_prefixe_ne_suffit_pas(self):
        self.chapitre(AVEC_ANCRE.replace("{#sec-regime}", "{#sec-regime-suite}"))
        erreurs = self.verifie([fiche()])
        self.assertTrue(any("#sec-regime " in e for e in erreurs), erreurs)

    def test_id_prefixe_ne_vaut_pas_ancre(self):
        """L'ancre « r-exemple-2 » ne tient pas lieu de « r-exemple »."""
        self.chapitre(AVEC_ANCRE.replace("r-exemple", "r-exemple-2"))
        erreurs = self.verifie([fiche(), fiche(id="r-exemple-2")])
        self.assertTrue(any(e.startswith("r-exemple : fiche orpheline") for e in erreurs), erreurs)

    def test_section_absente(self):
        self.chapitre(AVEC_ANCRE.replace("{#sec-regime}", "{#sec-autre}"))
        erreurs = self.verifie([fiche()])
        self.assertTrue(any("#sec-regime" in e for e in erreurs), erreurs)


def base_de_fixture(chemin: Path) -> None:
    """Une petite `jort_cache` : même schéma utile, même tokeniseur FTS."""
    cnx = sqlite3.connect(chemin)
    cnx.executescript("""
        create table textes (recid integer primary key, type text, numero text, titre text,
            objet text, ministere text, date_signature text, date_publication text,
            jort_annee integer, jort_numero integer, jort_tome integer, pages text,
            pdf_fr text, pdf_ar text);
        create virtual table textes_fts using fts5(titre, objet, numero, ministere, keywords_fr,
            tokenize='unicode61 remove_diacritics 2');
    """)
    lignes = [
        # Antérieur à la couverture de la passe : ne doit pas revenir.
        (1, "Decret", "2025-100", "Decret n° 2025-100 relatif aux travailleuses agricoles",
         "2025-03-04", 2025, 20, "/jort/2025/2025F/Jo0202025.pdf"),
        # Postérieur : candidat, par FTS (titre non accentué) et par le LIKE qui le double.
        (2, "Decret", "2026-12", "Decret n° 2026-12 fixant les taux du regime des travailleuses agricoles",
         "2026-02-10", 2026, 15, "/jort/2026/2026F/Jo0152026.pdf"),
        # Postérieur, titre NON accentué : le LIKE accentué de la fiche doit le trouver.
        (3, "Arrete", None, "Arrete relatif a la securite sociale des pecheurs",
         "2026-03-01", 2026, 22, None),
        # Postérieur, hors sujet.
        (4, "Decret", "2026-13", "Decret relatif aux marches publics",
         "2026-03-02", 2026, 22, "/jort/2026/2026F/Jo0222026.pdf"),
    ]
    for recid, type_, numero, titre, date, annee, num, pdf in lignes:
        cnx.execute("insert into textes (recid, type, numero, titre, objet, date_publication, "
                    "jort_annee, jort_numero, pages, pdf_fr, pdf_ar) values (?,?,?,?,?,?,?,?,?,?,?)",
                    (recid, type_, numero, titre, titre, date, annee, num, "12-13", pdf,
                     pdf.replace("F/Jo", "A/Ja") if pdf else None))
        cnx.execute("insert into textes_fts (rowid, titre, objet, numero) values (?,?,?,?)",
                    (recid, titre, titre, numero))
    cnx.commit()
    cnx.close()


class BaseTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dossier = Path(self._tmp.name)
        self.base = self.dossier / "jort_cache.db"
        base_de_fixture(self.base)
        self.cnx = r.ouvre_base(self.base)

    def tearDown(self):
        self.cnx.close()
        self._tmp.cleanup()


class RelancerTest(BaseTest):
    def candidats(self, f, depuis=None):
        trouves, avert = r.cherche_base(self.cnx, f["requetes"], r.seuil_de(f, depuis))
        self.assertEqual(avert, [])
        return trouves

    def test_seuil_lendemain_de_la_couverture(self):
        self.assertEqual(r.seuil_de(fiche(), None), "2026-01-01")

    def test_seuil_jamais_avant_la_naissance_de_l_objet(self):
        f = fiche(passes=[])
        self.assertEqual(r.seuil_de(f, None), "2024-10-23")

    def test_trouve_le_posterieur_et_ignore_l_anterieur(self):
        trouves = self.candidats(fiche())
        self.assertIn(2, trouves)
        self.assertNotIn(1, trouves)
        self.assertNotIn(4, trouves)

    def test_depuis_elargit_la_periode(self):
        self.assertIn(1, self.candidats(fiche(), depuis="2025-01-01"))

    def test_double_voie_fts_et_like(self):
        voies = self.candidats(fiche())[2][1]
        self.assertTrue(any(v.startswith("fts ") for v in voies), voies)
        self.assertTrue(any(v.startswith("like ") for v in voies), voies)

    def test_like_accentue_trouve_le_titre_non_accentue(self):
        """`like '%sécurité sociale%'` rendait 9 textes, sans accents 228 (§ 1 c)."""
        trouves = self.candidats(fiche())
        self.assertIn(3, trouves)
        voies = trouves[3][1]
        self.assertTrue(any(v.startswith("like %sécurité") for v in voies), voies)
        self.assertTrue(any("doublant like" in v for v in voies), voies)

    def test_numero_nul_ne_fait_pas_disparaitre_le_texte(self):
        """42 % des textes ont un `numero` NULL (§ 1 a)."""
        self.assertEqual(self.candidats(fiche())[3][0]["numero"], "")

    def test_fts_mal_forme_signale_sans_planter(self):
        f = fiche()
        f["requetes"] = {"titres_fts": ['"non ferme']}
        _, avert = r.cherche_base(self.cnx, f["requetes"], "2020-01-01")
        self.assertEqual(len(avert), 1)

    def test_sortie_de_relance(self):
        corpus = self.dossier / "corpus"
        md = corpus / "markdown_output" / "JORT" / "2026" / "fr"
        md.mkdir(parents=True)
        (md / "Jo0302026.md").write_text(
            "Décret fixant les taux. " * 20 + "Vu le décret-loi n° 2024-4 du 22 octobre 2024.",
            encoding="utf-8")
        (md / "Jo0312026.md").write_text("Vu le décret n° 2024-45. " * 20, encoding="utf-8")
        f = fiche()
        f["requetes"]["plein_texte"] = ["2024-4"]
        f["requetes"]["iort_ar"] = ["العاملات الفلاحيات"]
        sortie = io.StringIO()
        with contextlib.redirect_stdout(sortie):
            r.relance(f, base=self.base, corpus=corpus)
        texte = sortie.getvalue()
        self.assertIn("[2] Decret 2026-12", texte)
        self.assertIn("https://www.pist.tn/jort/2026/2026F/Jo0152026.pdf", texte)
        self.assertIn("[3] Arrete (sans numéro)", texte)
        self.assertNotIn("[1]", texte)
        self.assertIn("JORT n° 30/2026 (fr)", texte)
        self.assertNotIn("JORT n° 31/2026", texte)  # « 2024-45 » n'est pas « 2024-4 »
        self.assertIn("miroir absent", texte)       # source non parcourue : dit, pas conclu


class PerimeeTest(BaseTest):
    def test_perimee_si_la_base_va_plus_loin(self):
        fin = r.derniere_publication(self.cnx)
        self.assertEqual(fin, "2026-03-02")
        self.assertTrue(r.est_perimee(fiche(), fin))

    def test_a_jour_si_la_passe_couvre_la_base(self):
        f = fiche()
        f["passes"][0]["couvert_jusqu_au"] = "2026-09-18"
        self.assertFalse(r.est_perimee(f, "2026-03-02"))

    def test_derniere_passe_est_la_plus_couvrante(self):
        f = fiche()
        f["passes"].append(dict(f["passes"][0], date="2026-09-20", couvert_jusqu_au="2026-09-18"))
        self.assertFalse(r.est_perimee(f, "2026-03-02"))

    def test_resolue_jamais_perimee(self):
        self.assertFalse(r.est_perimee(fiche(resolu="decret2026-12"), "2026-03-02"))

    def test_lister_perimees(self):
        a_jour = fiche(id="r-a-jour")
        a_jour["passes"][0]["couvert_jusqu_au"] = "2026-09-18"
        ancienne = fiche(id="r-ancienne")
        sortie = io.StringIO()
        ancien = os.environ.get("JORT_CACHE_DB")
        os.environ["JORT_CACHE_DB"] = str(self.base)
        try:
            with contextlib.redirect_stdout(sortie):
                r.cmd_lister([a_jour, ancienne], perimees_seules=True)
        finally:
            if ancien is None:
                del os.environ["JORT_CACHE_DB"]
            else:
                os.environ["JORT_CACHE_DB"] = ancien
        texte = sortie.getvalue()
        self.assertIn("r-ancienne — PÉRIMÉE", texte)
        self.assertNotIn("r-a-jour", texte)
        self.assertIn("1 fiche(s) périmée(s) sur 2", texte)


class OutilsTest(unittest.TestCase):
    def test_normalisation_commune(self):
        self.assertEqual(r.sans_accents("Sécurité  SOCIALE"), "securite sociale")
        # Marques bidirectionnelles de pdftotext, chadda, tatweel.
        self.assertEqual(r.sans_accents("عدد ‪4‬ لسنة ‪2024‬"), "عدد 4 لسنة 2024")
        self.assertEqual(r.sans_accents("الجمهوريّة"), r.sans_accents("الجمهورية"))
        self.assertEqual(r.sans_accents("الفلاحـيات"), r.sans_accents("الفلاحيات"))

    def test_bornes_numeriques(self):
        m = r.motif("2024-4")
        self.assertTrue(m.search("decret-loi n° 2024-4 du"))
        self.assertFalse(m.search("decret n° 2024-48 du"))
        # Pas de borne de mot : la particule collée (و، ب) ne cache pas le terme…
        self.assertTrue(r.motif("العاملات الفلاحيات").search(r.sans_accents("والعاملات الفلاحيات")))
        # … mais « ل » + « ال » s'écrit « لل » : l'alif tombe, et il faut chercher sans l'article.
        self.assertFalse(r.motif("العاملات الفلاحيات").search(r.sans_accents("للعاملات الفلاحيات")))
        self.assertTrue(r.motif("عاملات الفلاحيات").search(r.sans_accents("للعاملات الفلاحيات")))

    def test_phrase_fts(self):
        self.assertEqual(r.phrase_fts("%travailleuses agricoles%"), '"travailleuses agricoles"')
        self.assertIsNone(r.like_depuis_fts("a AND b"))
        self.assertEqual(r.like_depuis_fts('"a b"'), "%a b%")

    def test_intitules_iort(self):
        ancien = "# 60-30\n\n## النسخة العربية\n\nخدمات\n\nدليل\n\nيتعلق بتنظيم أنظمة الضمان الاجتماعي\n\nالسنة\n"
        self.assertEqual(r.intitules_iort(ancien)[0], "يتعلق بتنظيم أنظمة الضمان الاجتماعي")
        recent = ("# 2024-4\n\n## Version française\n\nDécret-loi n° 2024-4\n\n## النسخة العربية\n\n"
                  "للعاملات الفلاحيات\nالرائد  الرسمي للقوانين\nدليل\nالجديد\n")
        ar, fr, corps = r.intitules_iort(recent)
        self.assertEqual((ar, fr), ("", "Décret-loi n° 2024-4"))
        self.assertIn("للعاملات الفلاحيات", corps)
        self.assertNotIn("الجديد", corps)

    def test_url_fascicule(self):
        self.assertEqual(r.url_fascicule(2026, "fr", 93), "https://www.pist.tn/jort/2026/2026F/Jo0932026.pdf")
        self.assertEqual(r.url_fascicule(2000, "ar", 39), "https://www.pist.tn/jort/2000/2000A/Ja03900.pdf")
        self.assertEqual(r.url_fascicule(1989, "fr", 60), "https://www.pist.tn/jort/1989/1989F/Jo06089.pdf")

    def test_date_fascicule_inferee(self):
        dates = {(2026, 20): "2026-03-01"}
        self.assertEqual(r.date_fascicule(dates, 2026, 20), "2026-03-01")
        self.assertEqual(r.date_fascicule(dates, 2026, 12), "2026-03-01")  # borne sûre
        self.assertEqual(r.date_fascicule(dates, 2026, 60), "9999")        # inconnu : parcouru
        dates[(2026, 107)] = "2026-01-16"                                  # numéro aberrant
        self.assertEqual(r.date_fascicule(dates, 2026, 50), "9999")        # ne borne rien

    def test_elargir_et_passe(self):
        f = fiche()
        self.assertTrue(r.elargit(f, "العاملات الفلاحيات", "iort_ar"))
        self.assertFalse(r.elargit(f, "العاملات الفلاحيات", "iort_ar"))
        r.ajoute_passe(f, "aucun", "jusqu'au n° 93", "2026-09-18", ["pist"], date="2026-09-24")
        self.assertNotIn("resolu", f)
        r.ajoute_passe(f, "decret2026-12", "lu", "2026-09-30", ["pist"], date="2026-10-01")
        self.assertEqual(f["resolu"], "decret2026-12")
        self.assertEqual(len(f["passes"]), 3)


@unittest.skipUnless(AVEC_YAML, "PyYAML absent : lancer par `uv run pytest`")
class RegistreTest(unittest.TestCase):
    def test_registre_versionne_sous_forme_canonique(self):
        """Sinon la première réécriture par `elargir` ou `passe` toucherait tout le fichier."""
        entete, fiches = r.charger()
        self.assertEqual(r.formate(entete, fiches), r.REGISTRE.read_text(encoding="utf-8"))

    def test_aller_retour(self):
        with tempfile.TemporaryDirectory() as d:
            chemin = Path(d) / "recherches.yml"
            r.ecrire("# en-tête\n", [fiche()], chemin)
            entete, fiches = r.charger(chemin)
            self.assertEqual(entete, "# en-tête\n")
            self.assertEqual(fiches, [fiche()])
            self.assertIn("date: 2026-01-05\n", chemin.read_text(encoding="utf-8"))

    def test_registre_versionne_coherent(self):
        _, fiches = r.charger()
        self.assertEqual(r.verifie(fiches), [])


if __name__ == "__main__":
    unittest.main()
