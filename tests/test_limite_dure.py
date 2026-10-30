"""Le plafond de dépense mensuel arrête la passe, sans faire rougir la CI pour rien.

Ces épreuves lancent LE VRAI script, contre un faux `google.genai` qui refuse comme
l'API refuse. Une version antérieure de ces tests rejouait la boucle au lieu de
l'exécuter ; elle validait un correctif qui, lancé pour de bon, avalait une erreur
de troncature. D'où la règle suivie ici : on éprouve le script, jamais son imitation.

Trois comportements sont en jeu, et les trois ont manqué le 20 septembre 2026 :
la passe tentait un appel par fichier sur un refus qui valait pour tous ; elle
faisait échouer la CI à chaque poussée pour une cause connue et non actionnable ;
et rien ne contredisait le message de commit qui promettait l'inverse.
"""

import os
import subprocess
import sys
import textwrap
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

PLAFOND = (
    "429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'Your project has "
    "exceeded its monthly spending cap.', 'status': 'RESOURCE_EXHAUSTED'}}"
)

# Trois fichiers français réels, pris au dépôt : le script lit la source avant
# d'appeler l'API, un chemin inventé ne prouverait rien.
FICHIERS = [
    "precis/fr/fiscalite/_tva.qmd",
    "precis/fr/retraites/_secteur_prive.qmd",
    "precis/fr/remunerations_publiques/_regime_indiciaire.qmd",
]


def _faux_genai(racine_faux: Path, premier_reussit: bool) -> None:
    """Écrit un paquet `google.genai` qui compte ses appels et refuse sur plafond."""
    (racine_faux / "google" / "genai").mkdir(parents=True, exist_ok=True)
    (racine_faux / "google" / "__init__.py").write_text("", encoding="utf-8")
    (racine_faux / "google" / "genai" / "types.py").write_text(
        "class GenerateContentConfig:\n    def __init__(self, **kw): pass\n"
        "class ThinkingConfig:\n    def __init__(self, **kw): pass\n",
        encoding="utf-8")
    (racine_faux / "google" / "genai" / "__init__.py").write_text(
        textwrap.dedent(f'''
        import os, pathlib
        APPELS = []
        MSG = os.environ.get('MSG_FAUX') or {PLAFOND!r}
        import time
        time.sleep = lambda s: None   # pas d'attente réelle entre les réessais
        PREMIER_REUSSIT = {premier_reussit!r}

        class _Reponse:
            def __init__(self, texte): self.text = texte

        class _Models:
            def generate_content(self, **kw):
                APPELS.append(1)
                pathlib.Path(os.environ["COMPTEUR"]).write_text(str(len(APPELS)))
                if PREMIER_REUSSIT and len(APPELS) == 1:
                    # Trop courte : le garde-fou de troncature la refusera. C'est
                    # volontaire — on veut une panne D'UNE AUTRE NATURE que le plafond.
                    return _Reponse("# عنوان\\n\\nنص قصير.")
                raise RuntimeError(MSG)

        class Client:
            def __init__(self, *a, **k): self.models = _Models()
        ''').lstrip(), encoding="utf-8")


def _lance(tmp_path, premier_reussit, msg=None):
    faux = tmp_path / "faux"
    _faux_genai(faux, premier_reussit)
    compteur = tmp_path / "compteur"
    compteur.write_text("0", encoding="utf-8")
    env = {
        **os.environ,
        "PYTHONPATH": str(faux),
        "GEMINI_API_KEY": "factice",
        "COMPTEUR": str(compteur),
        "TRADUCTION_BILAN": str(tmp_path / "bilan.json"),
    }
    if msg:
        env["MSG_FAUX"] = msg
    env.pop("GITHUB_STEP_SUMMARY", None)
    r = subprocess.run(
        [sys.executable, "scripts/translate_sync.py", "HEAD~1", "HEAD", *FICHIERS],
        cwd=RACINE, env=env, capture_output=True, text=True)
    return r.returncode, int(compteur.read_text()), r.stdout


def test_le_plafond_seul_vaut_attente_et_non_echec(tmp_path):
    """Trois fichiers, plafond d'emblée : UN appel, code 0, message sans ambiguïté."""
    code, appels, sortie = _lance(tmp_path, premier_reussit=False)
    assert appels == 1, "le refus vaut pour toute la passe : un seul appel suffit"
    assert code == 0, "rien n'a été écrit, aucune PR ne s'ouvrira : ce n'est pas un échec"
    assert "LIMITE DE DÉPENSE ATTEINTE" in sortie
    assert "non tenté (plafond atteint)" in sortie, "les fichiers sautés sont nommés"


def test_une_panne_d_une_autre_nature_fait_toujours_echouer(tmp_path):
    """Une troncature puis le plafond : le silence du plafond ne doit pas la couvrir."""
    code, appels, sortie = _lance(tmp_path, premier_reussit=True)
    assert appels == 2
    assert code == 1, "une panne étrangère au plafond reprend ses droits"
    assert "traduction tronquée" in sortie
    assert "Synchro incomplète" in sortie
    assert "LIMITE DE DÉPENSE ATTEINTE" not in sortie


def test_le_plafond_n_est_pas_pris_pour_un_debit():
    """Un 429 qui parle de plafond n'est pas transitoire ; un 429 de débit l'est."""
    sys.path.insert(0, str(RACINE / "scripts"))
    from translate_sync import est_transitoire

    assert est_transitoire(PLAFOND) is False
    assert est_transitoire("429 RESOURCE_EXHAUSTED: quota exceeded, retry later") is True


def test_pas_d_echappement_unicode_dans_la_source():
    """Les commentaires doivent se lire ; seule la regex arabe garde ses échappements."""
    source = (RACINE / "scripts" / "translate_sync.py").read_text(encoding="utf-8")
    restants = [l for l in source.split("\n") if "\\u0" in l and "re.compile" not in l]
    assert restants == [], f"échappements \\uXXXX hors regex : {restants}"


CREDIT_402 = ("402 RESOURCE_EXHAUSTED. Your prepayment credits are depleted. Please go to "
              "AI Studio to manage your project and billing.")


def _bilan(tmp_path):
    import json
    return json.loads((tmp_path / "bilan.json").read_text(encoding="utf-8"))


def test_le_402_arrete_la_passe_en_succes_et_dit_pourquoi(tmp_path):
    code, appels, sortie = _lance(tmp_path, premier_reussit=False, msg=CREDIT_402)
    assert appels == 1
    assert code == 0
    bilan = _bilan(tmp_path)
    assert bilan["etat"] == "suspendue" and bilan["nature"] == "credit_prepaye"
    assert bilan["traduits"] == [] and len(bilan["non_traduits"]) == 3


def test_le_plafond_mensuel_ecrit_son_bilan(tmp_path):
    code, _appels, _sortie = _lance(tmp_path, premier_reussit=False)
    assert code == 0
    assert _bilan(tmp_path)["nature"] == "plafond_mensuel"


def test_un_429_persistant_finit_en_suspension_apres_les_reessais(tmp_path):
    code, appels, sortie = _lance(
        tmp_path, premier_reussit=False,
        msg="429 RESOURCE_EXHAUSTED: quota exceeded, retry later")
    assert appels == 5, "cinq essais sur le premier fichier, puis arrêt de toute la passe"
    assert code == 0
    assert _bilan(tmp_path)["nature"] == "quota_persistant"


def test_nature_des_limites():
    sys.path.insert(0, str(RACINE / "scripts"))
    from translate_sync import est_limite_dure, est_transitoire, nature_limite

    assert nature_limite(PLAFOND) == "plafond_mensuel"
    assert nature_limite(CREDIT_402) == "credit_prepaye"
    assert nature_limite("quota exceeded") is None
    assert nature_limite("503 UNAVAILABLE") is None
    assert nature_limite("HTTP 4021 bizarre") is None, "402 doit être un code, pas un morceau"
    assert est_limite_dure(CREDIT_402) and not est_transitoire(CREDIT_402)
