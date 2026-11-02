"""Tests du générateur de l'annexe de la circulaire n° 42 de 1996.

Le générateur lit le module du modèle comme du texte (`ast`) : sont figés ici cette lecture, sur
un module imitant celui de la PR n° 518 d'openfisca-tunisia, la mise en forme d'une ligne, et ce
que doit tenir le snapshot versionné (81 codes, 7 tableaux, ancre de registre). Le modèle n'est
pas là : aucune importation d'openfisca.
"""

import re
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

import generate_circulaire_42_tables as g  # noqa: E402

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

SOURCE = '''
from openfisca_tunisia.variables.base import *

class SituationParents(Enum):
    __order__ = "a b"
    a = "Père et mère en vie, non divorcés (I)"
    b = "Père décédé, mère non remariée (II)"

class Allocataire(Enum):
    non_servie = "Non servie"
    pere = "Servie au père"

_N = ("N", None)
_c, _ap = "communs", "agent_public"
_S = SituationParents

CAS_ANNEXE_2 = [
    (1, "I-A", "a", _ap, _ap, _c, None, ("P", "C"), _N),
]
'''

META = {
    "payeurs": {"cnss": "par la CNSS"},
    "garde_partagee": {"G": "servie au père et à la mère{payeur}"},
    "libelles_circulaire": {7: {"indemnite_familiale": "texte de la circulaire"}},
}
MODELE = {"libelles": {"Allocataire": {
    "non_servie": "Non servie", "pere": "Servie au père"}}, "cas": []}


class LectureDuModule(unittest.TestCase):
    def test_table_et_libelles_sont_lus_sans_importer_le_module(self):
        modele = g.lire_modele(SOURCE)
        self.assertEqual(
            modele["cas"], [(1, "I-A", "a", "agent_public", "agent_public", "communs", None,
                             ("P", "C"), ("N", None))])
        self.assertEqual(
            modele["libelles"]["Allocataire"]["pere"], "Servie au père")
        self.assertNotIn("__order__", modele["libelles"]["SituationParents"])

    def test_une_table_non_litterale_fait_echouer(self):
        with self.assertRaises(g.Ecart):
            g.lire_modele("CAS_ANNEXE_2 = [(1, inconnu)]")

    def test_table_absente(self):
        with self.assertRaises(g.Ecart):
            g.lire_modele("x = 1")


class MiseEnForme(unittest.TestCase):
    def test_beneficiaire_et_payeur(self):
        self.assertEqual(
            g.cellule_indemnite(MODELE, META, 1, "indemnite_familiale", ("P", "C")),
            "servie au père par la CNSS")
        self.assertEqual(
            g.cellule_indemnite(MODELE, META, 1, "salaire_unique", ("N", None)), "non servie")

    def test_la_surcharge_de_la_circulaire_l_emporte(self):
        self.assertEqual(
            g.cellule_indemnite(MODELE, META, 7, "indemnite_familiale", ("P", None)),
            "texte de la circulaire")

    def test_garde_partagee(self):
        self.assertEqual(
            g.cellule_indemnite(MODELE, META, 68, "salaire_unique", ("G", None)),
            "servie au père et à la mère")

    def test_bénéficiaire_inconnu(self):
        with self.assertRaises(g.Ecart):
            g.cellule_indemnite(MODELE, META, 1, "salaire_unique", ("Z", None))

    def test_position_indifferente_et_qualificatif(self):
        sit = {"mere": "décédée"}
        self.assertEqual(g.position_parent({}, {}, sit, "mere", None), "décédée")
        with self.assertRaises(g.Ecart):
            g.position_parent({}, {}, {}, "mere", None)

    def test_libelle_de_position_des_metadonnees_puis_du_modele(self):
        modele = {"libelles": {"StatutParent": {
            "salarie": "Salarié(e), sans distinction", "sans_activite": "N'exerce pas"}}}
        meta = {"positions": {"salarie": "salarié(e)"}}
        self.assertEqual(g.position_parent(modele, meta, {}, "pere", "salarie"), "salarié(e)")
        self.assertEqual(
            g.position_parent(modele, meta, {"pere": "décédé"}, "pere", "sans_activite"),
            "n'exerce pas, décédé")


@unittest.skipIf(yaml is None, "PyYAML absent")
class Metadonnees(unittest.TestCase):
    def setUp(self):
        self.meta = yaml.safe_load(g.METADONNEES.read_text(encoding="utf-8"))

    def test_chaque_piece_citee_est_definie(self):
        for code, noms in self.meta["pieces_par_cas"].items():
            self.assertTrue(1 <= code <= 81)
            for nom in noms:
                self.assertIn(nom, self.meta["pieces"], f"cas {code}")

    def test_sept_situations_avec_pages(self):
        self.assertEqual(len(self.meta["situations"]), 7)
        for sit in self.meta["situations"].values():
            self.assertTrue(sit["pages"].startswith("p. "))


class SnapshotVersionne(unittest.TestCase):
    def setUp(self):
        self.texte = g.SORTIE.read_text(encoding="utf-8")

    def test_quatre_vingt_un_codes_dans_l_ordre(self):
        codes = []
        for ligne in self.texte.splitlines():
            cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
            if ligne.startswith("|") and len(cellules) in (7, 8):
                code = cellules[4] if len(cellules) == 8 else cellules[3]
                if code.isdigit():
                    codes.append(int(code))
        self.assertEqual(codes, list(range(1, 82)))

    def test_sept_tableaux_legendes_et_ancre(self):
        legendes = re.findall(r"\{#(tbl-pf-public-annexe2-[a-z]+)\}", self.texte)
        self.assertEqual(
            legendes, [f"tbl-pf-public-annexe2-{r}" for r in
                       ("i", "ii", "iii", "iv", "v", "vi", "vii")])
        self.assertEqual(self.texte.count("{#r-pf-public-annexe2}"), 1)

    def test_aucune_mention_du_modele_hors_commentaire(self):
        visible = re.sub(r"<!--.*?-->", "", self.texte, flags=re.S).lower()
        self.assertNotIn("openfisca", visible)


if __name__ == "__main__":
    unittest.main()
