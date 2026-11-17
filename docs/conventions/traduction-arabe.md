# Traduction arabe : câblage et pipeline

<!-- Détail déplacé d'AGENTS.md le 17/11/2026 (source unique) ; AGENTS.md y renvoie en une ligne. -->

- **Ne remets jamais les `_quarto.yml` dans la synchronisation de traduction.** Ils en sont exclus
  par le filtre du workflow *et* par `translate_sync.fichier_a_traduire()`. Motif : le fichier arabe
  porte des éléments qui n'ont **aucun original français** — `dir: rtl`, le bloc `language:` des
  libellés d'interface, les titres des parties du livre. Le traducteur ne peut pas les déduire du
  fichier français et les effaçait à chaque passage ; le livre arabe rendait alors 404 jusqu'au
  rattrapage à la main. Conséquence pratique : **quand tu ajoutes, retires ou renommes un chapitre côté
  français, lance `uv run python scripts/arabe_cablage.py`** et commite le résultat. Le script
  réécrit les seules listes `chapters:` et `appendices:` du `_quarto.yml` arabe d'après le français
  (ce qui n'a pas d'original français est conservé) et pose une page-relais (avis « pas encore
  traduit » et lien vers le français) pour tout chapitre sans arabe ; la CI le rejoue après chaque
  passage de traduction, et `verifier-conventions.yml` le vérifie sur les PR (`--verifier`). Une
  page-relais porte un commentaire HTML de tête ; ni `traduction_en_retard.py`, ni la parité ne la
  prennent pour une traduction, et `translate_sync` l'écrase. Un fichier malformé ou des chapitres qui dérivent sont attrapés par
  `rendre-les-livres.yml`, qui rend les livres disponibles sur chaque PR.
- **La traduction se traite seule ; l'état se lit dans une issue.** Le palier gratuit de Gemini
  plafonne par mois. Au premier refus de limite de dépense (plafond mensuel, 402, ou 429 qui ne
  cède pas), `translate_sync` s'arrête, sort en succès et écrit son bilan ; le retard se recalcule
  par dates de commit (`scripts/traduction_en_retard.py`) et est repris au passage suivant. Rien à
  relancer à la main. L'issue épinglée « Traductions arabes : état » (marqueur HTML caché ;
  `scripts/etat_traduction.py`, appelé par `translation-sync.yml`) dit le retard par livre, l'état,
  le budget mensuel appris et la consommation du mois ; elle ne se ferme pas.
  **Rattrapage par lots** : le lundi et le 1er du mois, `scripts/lot_traduction.py` choisit UN
  livre (structure récemment changée d'abord : prestations sociales, fiscalité, finances locales),
  borné en fichiers (8) et en caractères (35 % du budget estimé, jamais au-delà de 75 % du budget
  du mois : le reste est la marge des fusions), sans les fichiers déjà portés par une PR de
  traduction ouverte. `uv run python scripts/lot_traduction.py --dry-run` montre le lot sans
  réseau. Les chapitres de plus de 90 000 caractères sont traduits par morceaux (`decouper`).
  Réglages en `workflow_dispatch` : `livre`, `max_fichiers`, `max_caracteres`, `budget_mensuel`.
  **Auto-fusion** : en fin de passage, `scripts/auto_fusion.py` active `gh pr merge --auto --merge`
  sur la PR du robot si tous ses fichiers sont sous `precis/ar/` (ou le glossaire engendré) et si
  parité, rendu des livres arabes touchés et vérification ont réussi ; sinon la PR reste ouverte,
  commentée, et l'issue d'état la liste. Ne contourne jamais ce filtre pour une PR qui touche autre
  chose que l'arabe. Le filet `deploiement-rattrapage.yml` relance `deploy.yml` si une fusion faite
  par le robot n'a pas déclenché le déploiement.
