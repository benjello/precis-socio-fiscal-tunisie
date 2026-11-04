"""Tests de `scripts/notices_rapports_finance.py` : clés, textes « cité pour » et notices déjà présentes."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import notices_rapports_finance as n  # noqa: E402


def ligne(sigle, ex, nature, cac="oui, p. 3"):
    return {
        "sigle": sigle,
        "exercice": ex,
        "nature": nature,
        "url_origine": "https://exemple.tn/a.pdf",
        "url_archive": "",
        "fichier": f"{sigle.lower()}/{ex}_{nature}.pdf",
        "octets": "10",
        "sha256": "ab" * 32,
        "consultation": "2026-11-04",
        "rapport_cac": cac,
    }


class NoticesTest(unittest.TestCase):
    def test_cles_par_nature(self):
        lignes = [
            ligne("BTS", "2016", "rapport_annuel"),
            ligne("BTS", "2021", "etats_financiers", "non"),
            ligne("BFPME", "2018", "etats_financiers_bourse"),
            ligne("CPSCL", "2015", "rapport_activite", "non lu"),
            ligne("BTS", "2013", "etats_financiers_cmf_remplace"),
        ]
        cles = [x["id"] for x in n.notices(lignes, set())]
        self.assertEqual(
            cles,
            [
                "ra-bts-2016",
                "es-bts-2021",
                "bvmt-ef-bfpme-2018-individuel",
                "ra-cpscl-2015",
                "cmf-efr-bts-2013",
            ],
        )

    def test_notice_existante_non_reecrite(self):
        self.assertEqual(
            n.notices([ligne("BTS", "2016", "rapport_annuel")], {"ra-bts-2016"}), []
        )

    def test_extrait_du_reviseur_seulement_pour_la_cpscl(self):
        cpscl = n.notices([ligne("CPSCL", "2010", "etats_financiers")], set())[0]
        bts = n.notices([ligne("BTS", "2012", "etats_financiers")], set())[0]
        self.assertIn("réviseur", cpscl["note"])
        self.assertIn("opinion des commissaires aux comptes", bts["note"])
        self.assertNotIn("réviseur", bts["note"])

    def test_document_non_lu_n_est_pas_un_document_sans_rapport(self):
        notice = n.notices(
            [ligne("CPSCL", "2016", "rapport_activite", "non lu")], set()
        )[0]
        self.assertIn("non lu", notice["note"])
        self.assertNotIn("n'y figure pas", notice["note"])

    def test_capture_de_l_archive(self):
        x = ligne("BTS", "2012", "etats_financiers")
        x["url_archive"] = "https://web.archive.org/web/2018/https://exemple.tn/a.pdf"
        notice = n.notices([x], set())[0]
        self.assertEqual(notice["URL"], x["url_archive"])
        self.assertEqual(notice["archive_location"], x["url_origine"])


if __name__ == "__main__":
    unittest.main()
