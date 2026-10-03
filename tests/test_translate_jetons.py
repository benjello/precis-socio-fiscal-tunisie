"""Tests de `restore_citation_keys`, `remove_extra_glossary_links` et de l'appariement
par clé de `restore_locators` — sans appel au modèle.

Les cas sont tirés des PR auto-translate #331, #333 et #343 (octobre 2026), où ces
jetons ont été corrigés à la main : clés déformées (`@looi81-6`, `@arrete-11-18-…`),
renvoi de tableau traduit (`@tbl-somme-three-texts`), locateurs traduits
(« art. 48 إلى 50 », « art. 31 و 37 », « art. 37 (جديد) ») et liens de glossaire
ajoutés dans une liste en gras.

Les ABSTENTIONS comptent autant que les réparations : ces fonctions réécrivent du
contenu publié, et une clé rattachée à la mauvaise loi serait pire que la clé abîmée.
"""

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import (  # noqa: E402
    remove_extra_glossary_links,
    restore_citation_keys,
    restore_locators,
)


def run(fonction, source, traduction):
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        resultat = fonction(source, traduction)
    return resultat, tampon.getvalue()


class ClesDeCitationTest(unittest.TestCase):
    def test_cle_doublee_pr_343(self):
        source = ("La condition est 60 ans [@loi81-6, art. 48]. Sont assimilées "
                  "[@loi81-6, art. 45].\n")
        traduit = ("يُشترط بلوغ 60 سنة [@looi81-6, art. 48]. وتُعتبر مماثلة "
                   "[@loi81-6, art. 45].\n")
        resultat, trace = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit.replace("@looi81-6", "@loi81-6"))
        self.assertIn("« looi81-6 » → « loi81-6 »", trace)

    def test_cle_doublee_pr_333(self):
        source = "mères de trois enfants [@loi88-71, art. 1 et 2], pension [@loi88-71, art. 1 (art. 41)].\n"
        traduit = "الأمهات [@looi88-71, art. 1 et 2]، مع جراية [@loi88-71, art. 1 (art. 41)].\n"
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit.replace("@looi88-71", "@loi88-71"))

    def test_annee_amputee_pr_331(self):
        cle = "arrete-1978-11-18-retraite-complementaire"
        source = f"Le salaire [@{cle}, règlement, art. 11] et l'équilibre [@{cle}, règlement, art. 18].\n"
        traduit = (f"المرتب [@{cle}, règlement, art. 11] والتوازن "
                   f"[@arrete-11-18-retraite-complementaire, règlement, art. 18].\n")
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit.replace("@arrete-11-18-", "@arrete-1978-11-18-"))

    def test_annee_alteree(self):
        source = "[@arrete-1978-11-18-retraite-complementaire, art. 3]\n"
        traduit = "[@arrete-1918-11-18-retraite-complementaire, art. 3]\n"
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, source)

    def test_renvoi_et_ancre_de_tableau_traduits_pr_343(self):
        source = (": Les trois textes {#tbl-somme-trois-textes}\n\n"
                  "soit 23,75 % (@tbl-somme-trois-textes). Puis (@tbl-somme-trois-textes)\n")
        traduit = (": النصوص الثلاثة {#tbl-somme-three-texts}\n\n"
                   "أي 23.75% (@tbl-somme-three-texts). ثم (@tbl-somme-three-texts)\n")
        resultat, trace = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit.replace("three-texts", "trois-textes"))
        self.assertIn("(2×)", trace)  # les deux renvois
        self.assertIn("ancre restaurée", trace)  # la définition

    def test_limite_de_jeton(self):
        """`@looi81-6` ne doit pas être remplacé à l'intérieur d'une clé plus longue."""
        source = "[@loi81-6, art. 1] [@loi81-60]\n"
        traduit = "[@looi81-6, art. 1] [@loi81-60]\n"
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, source)

    def test_positionnel_quand_le_jeton_fautif_existe_dans_la_source(self):
        """`@loi85-12` mis pour `@loi85-13` : seule l'occurrence alignée sur la
        clé manquante est corrigée, pas celle qui est légitime."""
        source = "A [@loi85-12] B [@loi85-13] C [@loi59-18]\n"
        traduit = "أ [@loi85-12] ب [@loi85-12] ج [@loi59-18]\n"
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, "أ [@loi85-12] ب [@loi85-13] ج [@loi59-18]\n")

    def test_commentaires_ignores(self):
        source = "<!-- TODO : @loi81-6 -->\nTexte [@loi81-6].\n"
        traduit = "<!-- TODO : @looi81-6 -->\nنص [@loi81-6].\n"
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit)


class ClesAbstentionTest(unittest.TestCase):
    def test_appariement_ambigu(self):
        """Deux clés manquantes également proches : on ne choisit pas."""
        source = "[@loi81-6] [@loi81-7]\n"
        traduit = "[@looi81-6] [@looi81-7]\n"
        resultat, trace = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit)
        self.assertIn("ambigu", trace)

    def test_rien_de_proche(self):
        source = "[@loi81-6]\n"
        traduit = "[@decret2023-741]\n"
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit)

    def test_prefixe_de_renvoi_different(self):
        """`@sec-x` ne se répare jamais en `@tbl-x`, si proches soient-ils."""
        source = "(@tbl-cnrps-ages)\n"
        traduit = "(@sec-cnrps-ages)\n"
        resultat, _ = run(restore_citation_keys, source, traduit)
        self.assertEqual(resultat, traduit)

    def test_texte_conforme_inchange_et_muet(self):
        source = "[@loi81-6, art. 48] (@tbl-a) {#tbl-a}\n"
        resultat, trace = run(restore_citation_keys, source, source)
        self.assertEqual(resultat, source)
        self.assertEqual(trace, "")


class LocateursTest(unittest.TestCase):
    def test_connecteurs_arabes_pr_333(self):
        source = ("[@loi59-18, art. 31 et 37] [@loi85-12, art. 27 à 29] "
                  "[@loi2007-43, art. 37 (nouveau)]. [@decret2023-741, art. 2 à 10]\n")
        traduit = ("[@loi59-18, art. 31 و 37] [@loi85-12, art. 27 إلى 29] "
                   "[@loi2007-43, art. 37 (جديد)]. [@decret2023-741, art. 2 إلى 10]\n")
        resultat, _ = run(restore_locators, source, traduit)
        self.assertEqual(resultat, source)

    def test_une_cle_abimee_ailleurs_ne_bloque_plus_pr_331(self):
        """Avant : une seule clé différente dans le fichier faisait renoncer à TOUS
        les locateurs. L'appariement se fait désormais clé par clé."""
        source = "[@arrete-1978-11-18-x, art. 18] puis [@loi81-6, art. 48 à 50]\n"
        traduit = "[@arrete-11-18-x, art. 18] ثم [@loi81-6, art. 48 إلى 50]\n"
        resultat, _ = run(restore_locators, source, traduit)
        self.assertEqual(resultat, "[@arrete-11-18-x, art. 18] ثم [@loi81-6, art. 48 à 50]\n")

    def test_comptes_differents_alignement(self):
        """La clé n'apparaît pas autant de fois : on ne restaure que dans les
        plages alignées."""
        source = "[@a, art. 1 à 2] [@b, art. 3] [@a, art. 5 à 6]\n"
        traduit = "[@a, art. 1 إلى 2] [@b, art. 3]\n"
        resultat, _ = run(restore_locators, source, traduit)
        self.assertEqual(resultat, "[@a, art. 1 à 2] [@b, art. 3]\n")

    def test_comptes_differents_sans_alignement(self):
        source = "[@a, art. 1 à 2] [@a, art. 5 à 6]\n"
        traduit = "[@b, art. 0] [@a, art. 5 إلى 6]\n"
        resultat, trace = run(restore_locators, source, traduit)
        self.assertEqual(resultat, traduit)
        self.assertIn("laissé tel quel", trace)


class LiensDeGlossaireTest(unittest.TestCase):
    # Cas de la PR #333, abrégé : la liste française est en gras, sans liens ; le
    # paragraphe qui la précède porte, lui, les liens.
    SOURCE = (
        "Trois catégories : les ouvriers [effectuant des travaux pénibles et insalubres]"
        "(#g-travaux-penibles-insalubres), les [fonctions astreignantes]"
        "(#g-fonctions-astreignantes) [@loi85-12, art. 27 à 29].\n"
        "\n"
        "- Les **ouvriers effectuant des travaux pénibles et insalubres** (art. 27) "
        "[@decret85-1177].\n"
        "- Les **agents exerçant des fonctions astreignantes** (art. 28) [@decret85-1178].\n"
    )
    TRADUIT = (
        "ثلاث فئات: العملة الذين يقومون [بأشغال شاقّة وغير صحّية]"
        "(#g-travaux-penibles-insalubres)، و[وظائف مرهقة]"
        "(#g-fonctions-astreignantes) [@loi85-12, art. 27 à 29].\n"
        "\n"
        "- [العملة القائمون بأشغال شاقة وغير صحية](#g-travaux-penibles-et-insalubres) "
        "(الفصل 27) [@decret85-1177].\n"
        "- [الأعوان المباشرون لوظائف مرهقة](#g-fonctions-astreignantes) (الفصل 28) "
        "[@decret85-1178].\n"
    )

    def test_liens_ajoutes_rendus_en_gras(self):
        resultat, trace = run(remove_extra_glossary_links, self.SOURCE, self.TRADUIT)
        attendu = (self.TRADUIT
                   .replace("[العملة القائمون بأشغال شاقة وغير صحية](#g-travaux-penibles-et-insalubres)",
                            "**العملة القائمون بأشغال شاقة وغير صحية**")
                   .replace("[الأعوان المباشرون لوظائف مرهقة](#g-fonctions-astreignantes) (",
                            "**الأعوان المباشرون لوظائف مرهقة** ("))
        self.assertEqual(resultat, attendu)
        self.assertEqual(trace.count("lien ajouté retiré"), 2)
        # Le lien légitime du paragraphe est gardé.
        self.assertIn("[وظائف مرهقة](#g-fonctions-astreignantes)", resultat)

    def test_sans_gras_a_la_source(self):
        source = "Le [salaire](#g-salaire) est dû.\n\nIl est versé.\n"
        traduit = "[الأجر](#g-salaire) مستحق.\n\n[يُصرف](#g-versement).\n"
        resultat, _ = run(remove_extra_glossary_links, source, traduit)
        self.assertEqual(resultat, "[الأجر](#g-salaire) مستحق.\n\nيُصرف.\n")

    def test_abstention_si_le_lien_en_trop_nest_pas_identifiable(self):
        """Deux liens vers la même cible sur la ligne qui en porte un à la source :
        lequel est en trop ? On ne tranche pas."""
        source = "Le [salaire](#g-salaire) et le salaire.\n"
        traduit = "[الأجر](#g-salaire) و[الأجر](#g-salaire).\n"
        resultat, trace = run(remove_extra_glossary_links, source, traduit)
        self.assertEqual(resultat, traduit)
        self.assertIn("aucun retrait", trace)

    def test_autres_liens_internes_intouches(self):
        source = "Voir la section.\n"
        traduit = "انظر [القسم](#sec-cnrps).\n"
        resultat, _ = run(remove_extra_glossary_links, source, traduit)
        self.assertEqual(resultat, traduit)

    def test_texte_conforme_inchange_et_muet(self):
        resultat, trace = run(remove_extra_glossary_links, self.SOURCE, self.SOURCE)
        self.assertEqual(resultat, self.SOURCE)
        self.assertEqual(trace, "")


if __name__ == "__main__":
    unittest.main()
