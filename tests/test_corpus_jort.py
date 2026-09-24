"""Tests de `scripts/corpus_jort.py` : sans réseau, sur un faux dépôt.

Ce qui doit tenir : on n'écrit que des PDF, jamais par-dessus un fichier existant, jamais
hors de `PDFs/JORT/` ; et un crawl qui dépasse son délai est tué avec ses descendants.
"""

import contextlib
import io
import sys
import tempfile
import time
import unittest
import unittest.mock
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import corpus_jort as c  # noqa: E402
import recherches as r  # noqa: E402
from test_recherches import base_de_fixture  # noqa: E402

class TelechargerTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.depot = Path(self._tmp.name)
        base_de_fixture(self.depot / "jort_cache.db")
        self._ancien = r.PDFS_LEGISLATION
        r.PDFS_LEGISLATION = self.depot
        existant = self.depot / "PDFs" / "JORT" / "2026" / "fr" / "Jo0152026.pdf"
        existant.parent.mkdir(parents=True)
        existant.write_bytes(b"%PDF ancien")
        self.existant = existant

    def tearDown(self):
        r.PDFS_LEGISLATION = self._ancien
        self._tmp.cleanup()

    def lance(self, reponses, a_blanc=False):
        appels = []

        def telecharge(url):
            appels.append(url)
            return reponses.get(url.rsplit("/", 1)[1], (404, b"<html>"))

        sortie = io.StringIO()
        env = {"JORT_CACHE_DB": str(self.depot / "jort_cache.db")}
        with (contextlib.redirect_stdout(sortie), unittest.mock.patch.dict("os.environ", env),
              unittest.mock.patch.object(c, "DELAI", 0)):
            c.cmd_telecharger([2026], a_blanc, telecharge=telecharge)
        return appels, sortie.getvalue()

    def test_a_blanc_ne_telecharge_rien(self):
        appels, texte = self.lance({}, a_blanc=True)
        self.assertEqual(appels, [])
        self.assertIn("2026 fr : 22", texte)
        self.assertIn("2026 ar : 15, 22", texte)

    def test_n_ecrit_que_des_pdf_et_jamais_par_dessus(self):
        appels, texte = self.lance({
            "Ja0152026.pdf": (200, b"%PDF-1.4 arabe"),
            "Jo0222026.pdf": (200, b"<html>maintenance</html>"),
        })
        self.assertNotIn("https://www.pist.tn/jort/2026/2026F/Jo0152026.pdf", appels)
        self.assertEqual(self.existant.read_bytes(), b"%PDF ancien")
        jort = self.depot / "PDFs" / "JORT" / "2026"
        self.assertEqual((jort / "ar" / "Ja0152026.pdf").read_bytes(), b"%PDF-1.4 arabe")
        self.assertFalse((jort / "fr" / "Jo0222026.pdf").exists())
        self.assertEqual(list(jort.rglob("*.part")), [])
        self.assertIn("téléchargés 1, absents 2", texte)

    def test_refuse_d_ecrire_hors_de_pdfs_jort(self):
        with self.assertRaises(ValueError):
            c.ecrit_sans_ecraser(self.depot / "jort_cache.db.pdf", b"%PDF")

class LanceBorneTest(unittest.TestCase):
    def test_depassement_tue_le_groupe(self):
        with tempfile.TemporaryDirectory() as d:
            temoin = Path(d) / "temoin"
            # Un petit-fils qui écrirait le témoin après 3 s : il doit mourir avec son parent.
            cmd = ["sh", "-c", f"(sleep 3; touch {temoin}) & wait"]
            debut = time.monotonic()
            self.assertIsNone(c.lance_borne(cmd, 0.5))
            self.assertLess(time.monotonic() - debut, 3)
            time.sleep(3.5)
            self.assertFalse(temoin.exists())

    def test_interruption_tue_le_groupe(self):
        """Ctrl-C n'atteint pas le groupe détaché : c'est `lance_borne` qui doit le tuer."""
        import signal
        import threading
        with tempfile.TemporaryDirectory() as d:
            temoin = Path(d) / "temoin"
            cmd = ["sh", "-c", f"(sleep 3; touch {temoin}) & wait"]
            minuterie = threading.Timer(0.5, lambda: signal.raise_signal(signal.SIGINT))
            minuterie.start()
            with self.assertRaises(KeyboardInterrupt):
                c.lance_borne(cmd, 60)
            time.sleep(3.5)
            self.assertFalse(temoin.exists())

    def test_part_residuel_ne_bloque_pas(self):
        with tempfile.TemporaryDirectory() as d, \
                unittest.mock.patch.object(r, "PDFS_LEGISLATION", Path(d)):
            dest = Path(d) / "PDFs" / "JORT" / "2026" / "fr" / "Jo0012026.pdf"
            dest.parent.mkdir(parents=True)
            dest.with_name(dest.name + ".part").write_bytes(b"tronque")
            self.assertTrue(c.ecrit_sans_ecraser(dest, b"%PDF complet"))
            self.assertEqual(dest.read_bytes(), b"%PDF complet")
            self.assertFalse(c.ecrit_sans_ecraser(dest, b"%PDF autre"))
            self.assertEqual(dest.read_bytes(), b"%PDF complet")

    def test_code_de_retour(self):
        self.assertEqual(c.lance_borne(["sh", "-c", "exit 3"], 10), 3)

if __name__ == "__main__":
    unittest.main()
