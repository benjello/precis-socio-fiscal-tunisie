# Sources, citations et séries à fenêtre

<!-- Détail déplacé d'AGENTS.md le 17/11/2026 (source unique) ; AGENTS.md y renvoie en une ligne. -->

- **Aucune valeur isolée, aucune date, aucune URL sans source vérifiée.** Une case vide honnête vaut
  mieux qu'une valeur plausible. Exception éditoriale : une **série historique importante déjà
  portée par openfisca-tunisia** peut rester visible provisoirement pour que son évolution ne
  disparaisse pas du précis. Elle est alors présentée dans son ensemble, jamais comme un état du
  droit établi, sans mention du modèle dans le rendu ; un `<!-- TODO (documentaliste) : … -->`
  adjacent renvoie à une issue ouverte sur `openfisca-tunisia` qui énumère les valeurs et dates à
  sourcer, et le constat figure aussi dans `docs/notes/backlog-modele.md`. URL du JORT sur `pist.tn`
  uniquement, dans l'édition de la langue du fichier.
- **Une note de « lacunes » / « source introuvable » n'a de valeur que confrontée au catalogue.**
  Avant d'écrire qu'un document est introuvable ou à chercher, le vérifier contre l'entrepôt
  `tunisia-data` (`sources/*-catalog.csv`, `sources/<famille>-urls.csv`, `data/raw/`) **et**
  `jort_cache.db` ; la note porte alors la mention datée « vérifié contre `tunisia-data/sources/`
  + `data/raw/` le <date> ». Sans cette confrontation, la note périme et fait répéter des
  téléchargements déjà faits (cas vécu : rapports Cour des comptes et CNRPS re-récupérés alors
  qu'ils étaient déjà catalogués et dans `data/raw/`).
- **Textes juridiques : citer une adresse publique, archiver dans la base législative.** Une citation
  donne au lecteur une source **publique** qu'il peut ouvrir : d'abord l'officiel externe quand il
  existe — le JORT sur `pist.tn`, dans l'édition de la langue —, sinon l'URL d'origine publique du
  texte. Un texte **non publié au JORT** (circulaire, note, texte ancien) est archivé dans la **base
  législative `tunisia-legislative-references`** (metadata-only : la fiche porte `external_path`,
  `sha256` et l'émetteur ; le PDF reste hors Git) et se cite `type: report` par son `id` de catalogue
  et son auteur, **sans URL inventée**. On attribue au **ministère émetteur**, jamais au canal de
  transmission ; **aucune donnée personnelle** dans ces dépôts publics. `tunisia-data` ne porte
  **aucun texte législatif**.
- **Série à fenêtre : on verse ce qui remonte à une trentaine d'années, et l'on dit que la série
  est incomplète.** Un paramètre dont les textes sont lus et datés sur une fenêtre d'environ trente
  ans (pour un état au 1er janvier 2026 : depuis 1996 environ) peut être versé dans le modèle sans
  remonter plus loin, même si des états antérieurs existent. Une seule pratique, pour tous les
  paramètres :
  1. le paramètre commence à sa première date **sourcée** — jamais une valeur antérieure sans
     référence ;
  2. ses `metadata.notes` disent, en une phrase : « Série incomplète : états antérieurs à AAAA non versés. » ;
  3. une ligne de `docs/notes/backlog-modele.md` énumère les états manquants, leurs textes et leur
     localisation (corpus, OCR, à obtenir) ;
  4. le volume garde, dans ses registres écrits à la main, l'histoire antérieure déjà sourcée ; le
     tableau engendré ne porte **aucun** `TODO` d'incomplétude et ne mentionne pas le modèle.
  Une série plus courte que la fenêtre, sans texte lisible avant sa première date, suit la même
  pratique. Le décalage entre la fenêtre et l'histoire écrite du volume se lit dans le backlog,
  pas dans le rendu.
