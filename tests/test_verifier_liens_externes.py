"""Tests de `scripts/verifier_liens_externes.py` : sans réseau, `urlopen` est simulé."""

import ssl
import sys
import unittest
import unittest.mock
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import verifier_liens_externes as v  # noqa: E402


def http(code):
    return urllib.error.HTTPError("http://x", code, "", {}, None)


class ClasserTest(unittest.TestCase):
    def classe(self, effet):
        with (
            unittest.mock.patch("urllib.request.urlopen", side_effect=effet),
            unittest.mock.patch("time.sleep"),
        ):
            return v.classer("http://x/doc.pdf")[0]

    def test_404_est_absent_sans_nouvel_essai(self):
        with unittest.mock.patch(
            "urllib.request.urlopen", side_effect=http(404)
        ) as appel:
            self.assertEqual(v.classer("http://x")[0], "absent")
        self.assertEqual(appel.call_count, 1)

    def test_403_et_429_ne_sont_pas_des_echecs(self):
        self.assertEqual(self.classe(http(403)), "limite")
        self.assertEqual(self.classe(http(429)), "limite")

    def test_certificat_invalide(self):
        erreur = ssl.SSLCertVerificationError(
            1, "unable to get local issuer certificate"
        )
        self.assertEqual(self.classe(urllib.error.URLError(erreur)), "certificat")

    def test_connexion_refusee_est_injoignable(self):
        self.assertEqual(
            self.classe(urllib.error.URLError(ConnectionRefusedError("refus"))),
            "injoignable",
        )

    def test_reponse_correcte(self):
        reponse = unittest.mock.MagicMock()
        reponse.__enter__.return_value.status = 206
        self.assertEqual(self.classe([reponse]), "ok")


if __name__ == "__main__":
    unittest.main()
