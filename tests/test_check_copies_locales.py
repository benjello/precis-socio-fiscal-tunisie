"""Tests du contrôle des copies locales annoncées dans les notices."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_copies_locales as cl  # noqa: E402

SHA = "a" * 64
AUTRE = "b" * 64


def _item(cle, note):
    return {"id": cle, "note": note}


class CopiesLocalesTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.racine = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def _refs(self, langue, livre, items):
        d = self.racine / "precis" / langue / livre
        d.mkdir(parents=True)
        (d / "references.json").write_text(json.dumps({"items": items}), encoding="utf-8")

    def test_gabarits_et_dossiers_ne_sont_pas_des_fichiers(self):
        note = ("sous tunisia-data/data/raw/c/<édition>.pdf, data/raw/c/x_AAAA_MM.pdf, data/raw/c/LF20{20,21}.pdf, "
                "dans data/raw/c/dossier/ et data/raw/c/a.pdf.")
        self.assertEqual(cl.fichiers_annonces(note), ["c/a.pdf"])

    def test_les_trois_categories(self):
        self._refs("fr", "livre", [
            _item("sha-absent", f"SHA-256 {AUTRE}"),
            _item("sha-connu", f"SHA-256 {SHA}"),
            _item("sans-sha", "Copie : data/raw/c/a.pdf."),
            _item("hors", "Copie : data/raw/c/inconnu.pdf."),
            _item("legislation", f"PDFs-legislation-tunisie/x.pdf (SHA-256 {AUTRE})"),
        ])
        r = cl.ecarts(self.racine, {SHA}, {"c/a.pdf"})
        self.assertEqual(r["sha_absent"], [("livre", "sha-absent", AUTRE[:12])])
        self.assertEqual(r["chemin_sans_sha"], [("livre", "sans-sha", "c/a.pdf")])
        self.assertEqual(r["chemin_hors_manifeste"], [("livre", "hors", "c/inconnu.pdf")])

    def test_la_note_arabe_n_est_jamais_lue(self):
        self._refs("ar", "livre", [_item("arabe", f"SHA-256 {AUTRE}")])
        (self.racine / "precis" / "fr").mkdir(parents=True)
        self.assertEqual(cl.ecarts(self.racine, set(), set())["sha_absent"], [])

    def test_manifestes_lus_depuis_le_dossier(self):
        d = self.racine / "manifeste"
        d.mkdir()
        (d / "c.csv").write_text(f"sha,chemin,octets\n{SHA},c/a.pdf,1\n", encoding="utf-8")
        self.assertEqual(cl.lire_manifestes(d), ({SHA}, {"c/a.pdf"}))

    def test_sans_manifestes_le_controle_est_saute(self):
        import os
        ancien = os.environ.get("TUNISIA_DATA_DIR")
        os.environ["TUNISIA_DATA_DIR"] = str(self.racine / "absent")
        try:
            self.assertEqual(cl.main([]), 0)
            self.assertEqual(cl.main(["--strict"]), 0)
        finally:
            if ancien is None:
                del os.environ["TUNISIA_DATA_DIR"]
            else:
                os.environ["TUNISIA_DATA_DIR"] = ancien


if __name__ == "__main__":
    unittest.main()
