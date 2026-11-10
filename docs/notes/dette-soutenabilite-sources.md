# Sources pour les diagnostics de soutenabilité de la dette — note documentaire

Note documentaire (documentaliste). Objet : repérer et **vérifier** les séries budgétaires et
macro nécessaires aux diagnostics classiques posés dans `docs/notes/eco-soutenabilite-dette.md`
(décomposition Δ(dette/PIB) ; besoin brut de financement BBF ; écart r−g ; composition
devise/maturité). Elle **complète** `docs/notes/dette-pret-par-pret.md` (dette extérieure PPG, IDS
Banque mondiale) et ne couvre que ce qui manquait : **solde (primaire/global), dette totale,
intérieure/extérieure, devise/maturité, réserves, charge d'intérêt**.

Consigne du propriétaire : **priorité au national (BCT, ministère des Finances) ; FMI/WEO et Banque
mondiale en repli ou recoupement seulement.** Rien ici n'est téléchargé dans un dépôt ; ce sont des
sources **vérifiées** (URL ouverte, code HTTP, couverture, extractibilité) pour rapatriement par
`collecteur-donnees`. Vérifications exécutées le **2026-11-09** (curl + pdftotext + API en ligne).

Déjà au catalogue `tunisia-data` (ne pas refaire la découverte) : `sources/bct-catalog.csv`
(codes de tables statistiques BCT), `sources/bct-archives*` (pub 107 **Dette Extérieure
1991-2024**, pub 109 Rapport annuel, pub 108 BSF), `sources/minfinances-indicateurs.md`
(indicateurs FP depuis 1986), `sources/minfin-ep-cnrps-finances.md`. Les PDF de dette extérieure
et le BSF sont rejouables par `scripts/download_bct_archives.py` depuis `bct-archives-urls.csv`.

---

## 1. Solde global et solde primaire de l'État (recettes, dépenses, **intérêts isolés**)

**Source nationale recommandée : ministère des Finances — « Résultats de l'exécution du budget de
l'État » (mensuel/annuel).**
- URL vérifiée (PDF, HTTP 200, 9,35 Mo) : `https://www.finances.gov.tn/sites/default/files/2025-02/Décembre%202024_0.pdf`
  (page de notice : `…/fr/document/resultats-provisoires-de-lexecution-du-budget-de-letat-fin-decembre-2024`).
  Dernière édition en date vue : **Novembre 2025** (`…/2026-02/Résultats provisoires … Novembre 2025.pdf`, HTTP 200).
- **Couche texte présente et exploitable** (pdftotext -layout). Le tableau d'équilibre isole, en
  lignes distinctes et bilingues : « Total recettes & dons », « Dépenses hors services de la
  dette », « Les dépenses de rémunération », « Les dépenses d'interventions », « Les dépenses
  d'investissement », **« Les charges de Financement (Intérêts de la Dette) / فائدة الدين »** et
  **« Solde Budgétaire / النتيجة »**. → **le solde primaire est reconstructible** : solde global +
  intérêts de la dette (les deux sont des lignes séparées du même tableau).
  Valeurs citées (tableau, colonnes pluriannuelles, MDT) : Intérêts de la dette ligne 6.1 =
  6 487,0 (dernière colonne) ; Solde Budgétaire ligne III = -10 150,0.
- **Couverture** : mensuelle, millésimes récents en ligne (≈2015→2025 sur la page
  téléchargement) ; **chaque PDF porte plusieurs années de comparaison**. Pour une série longue en
  niveaux, coupler avec la fiche § 1bis.
- **Extractibilité** : PDF à **couche texte** (scraping pdftotext -layout fiable ; colonnes en
  ordre droite→gauche à cause du bilingue AR, à remettre dans l'ordre).
- **Pièges** : périmètre **administration centrale (budget de l'État)**, pas administrations
  publiques ; « Déficit selon les normes internationales (hors privatisation et dons, y compris
  recouvrement du principal et prêts) » ≠ solde budgétaire brut — définitions à lire en note de bas
  de tableau ; chiffres **provisoires** révisés d'une édition à l'autre (la série signale une mise
  à jour 2022-2024). Base PIB : non fournie par ce PDF (le rapporter au PIB INS/BCT, voir § 2).

**§ 1bis — Série longue agrégée, même producteur : « Indicateurs des finances publiques »
(synthèse).**
- Page vérifiée (HTTP 200) : `https://www.finances.gov.tn/fr/les-indicateurs/synthese-des-resultats-des-finances-publiques-budget-de-letat`.
  Fichier **XLS** lié et vérifié (HTTP 200) : `https://www.finances.gov.tn/sites/default/files/users/user93/indicateurs%20des%20fin%20pub%20LF2026.xls`.
- La page rend déjà, en HTML scrapable, « Déficit Budgétaire (MDT et % PIB) », « Pression Fiscale
  (% PIB) », « Encours de la Dette Publique (MDT et % PIB) ». Valeurs citées (HTML, 4 années) :
  déficit % PIB -7,8 / -6,7 / -5,4 / -6,0 ; encours dette 84,6 / 84,9 / 82,1 / 83,4 % du PIB.
- **Couverture** : **séries annuelles depuis 1986** (XLS ; cf. `sources/minfinances-indicateurs.md`).
- **Extractibilité** : **XLS directement exploitable** + table HTML. **Attention** : la synthèse
  donne le **déficit global**, pas la charge d'intérêt séparée → le solde primaire long doit venir
  du couplage avec le § 1 (exécution) ou du BSF/Rapport annuel BCT.
- **Repli international** : voir § 6 ; **non nécessaire** pour le solde global (national long et
  propre). Pour un **solde primaire** en série longue homogène, le WEO est le recoupement le plus
  commode (une seule série % PIB), mais le FMI ne publie pas la primaire de la Tunisie dans
  l'API DataMapper (cf. § 6) → reconstruction nationale privilégiée.

## 2. Dette publique totale et part dans le PIB (intérieure + extérieure)

**Source nationale recommandée : ministère des Finances (synthèse, § 1bis) pour la dette publique
« budgétaire » ; BCT (table « Endettement total ») pour la vue monétaire/financière.**
- **MdF** : « Encours de la Dette Publique (MDT et % PIB) », **depuis 1986** (XLS § 1bis), HTTP 200.
  C'est la **dette de l'administration centrale** au sens budgétaire (celle que cite le PLF).
- **BCT, table statistique « Endettement total »**, codes `PL060010,PL060020`,
  viewer `tableau_n.jsp` :
  `https://www.bct.gov.tn/bct/siteprod/tableau_n.jsp?params=PL060010,PL060020` (HTTP 200, **table
  rendue en HTML statique, scrapable**). Valeurs citées (MDT, colonnes 2020→2025) : Endettement
  total 197 291 … **266 414** ; dont **État 84 480 … 131 055** ; Endettement intérieur État
  23 189 … **75 498** ; Endettement extérieur État 61 291 … **55 557**. ⚠ Concept **monétaire**
  (endettement de l'économie, État = agent) ≠ définition budgétaire de la dette publique du MdF :
  **les deux ne coïncident pas** (périmètre, valorisation). À utiliser pour la **ventilation
  intérieur/extérieur** cohérente, pas comme total officiel.
- **Couverture** : table BCT en ligne 2020→2025 seulement (série courte « temps réel ») ; la
  profondeur longue est dans le **BSF** (pub 108, rétrospectives ~1970→2026) et le **Rapport annuel
  BCT** (pub 109) — PDF à extraire.
- **Extractibilité** : MdF XLS = facile ; BCT `tableau_n.jsp` = **HTML statique scrapable** (valeurs
  dans la page) ; BSF/RA = PDF couche texte à parser.
- **Pièges** : MdF **administration centrale** ; BCT **monétaire**. Base PIB différente selon
  producteur (cf. `catalog.yml`, ruptures de base INS 1997/2010/2015) → **ne pas mélanger** un
  encours MdF avec un PIB d'une autre base.
- **Repli international** : WEO `GGXWDG_NGDP` (dette brute administrations publiques, % PIB),
  vérifié (§ 6) ; **non nécessaire** pour le national, **utile en recoupement** (périmètre APU vs
  administration centrale : niveaux proches mais non identiques).

## 3. Dette intérieure vs extérieure (encours, parts)

**Source nationale recommandée : BCT `PL060010,PL060020` (vue monétaire, § 2) et MdF — Rapport sur
la dette publique (annexe au PLF).**
- BCT : ventilation intérieur/extérieur de l'État **déjà citée au § 2** (État intérieur 75 498 ;
  extérieur 55 557 MDT en 2025 ; HTML scrapable).
- MdF : « Rapport sur la dette publique » annexé au PLF (annexe 7 ; portail budget par objectifs
  `gbo.tn`, en **arabe**). **Non ouvert dans cette passe** → fiche à vérifier/rapatrier (voir
  Lacunes). La page MdF `…/fr/les-indicateurs/chiffres-cles` expose « الدين الداخلي / الدين العام
  الخارجي » (dette intérieure / extérieure), HTML.
- **Couverture / extractibilité** : BCT 2020→2025 (HTML) + BSF long (PDF) ; MdF annexe PLF = PDF
  arabe, extractibilité à confirmer.
- **Pièges** : la dette **extérieure** se valorise en devises puis convertie en dinars → l'effet
  change y est logé (cf. fiche économiste § 2c, terme stock-flux). Ne pas additionner un extérieur
  « en devises converties » avec un intérieur sans vérifier l'unité.

## 4. Composition de la dette extérieure par **devise** et **maturité / durée de vie moyenne**

**Source nationale recommandée : BCT — Rapport annuel sur la Dette Extérieure (pub 107).**
- PDF vérifié (HTTP 200, 1,66 Mo, `Last-Modified` 2025-12-09) :
  `https://www.bct.gov.tn/bct/siteprod/documents/dette2024.pdf`. Millésimes **1991→2024**
  catalogués (`sources/bct-archives-urls.csv`, pattern `dette<AAAA>.pdf`), rejouables.
- Tables BCT en ligne correspondantes (viewer `tableau_n_ne.jsp`, chargées en **AJAX**, non
  rendues en statique → POST `chercher.jsp` renvoie **HTTP 404**, donc **à prendre dans le PDF**,
  pas par scraping de la page) : `PL236010` « Structure de la dette extérieure par monnaie de
  règlement », `PL235010` « Principaux paramètres de la dette extérieure » (durée de vie moyenne,
  taux moyen), `PL234010,PL234020,PL234030` « Structure du service de la dette extérieure »,
  `PL130200` « Position de la dette extérieure brute ».
- **Couverture** : annuelle **1991→2024** (PDF). 
- **Extractibilité** : **PDF** (couche texte à vérifier millésime par millésime ; tableaux denses →
  camelot/tabula probable). Les tables `.jsp` ne sont **pas** scrapables en statique (AJAX).
- **Pièges** : « monnaie de règlement » ≠ monnaie d'émission ; périmètre dette extérieure (publique
  vs totale, PPG vs privée) à lire dans l'ours du rapport ; cohérence avec l'IDS Banque mondiale
  (note `dette-pret-par-pret.md`) à faire.
- **Repli international** : la décomposition devise n'est pas servie proprement par le WEO ;
  World Bank IDS donne le service par créancier mais **pas** la part par devise de l'encours total.
  → **le national (BCT pub 107) est la seule source propre par devise** : à rapatrier.

## 5. Réserves de change (mois/jours d'importation) et exportations

**Source nationale recommandée : BCT — table « Principaux indicateurs de paiements extérieurs »
(`PL237010`) + Rapport annuel.**
- URL vérifiée (HTTP 200, **table rendue en HTML statique**) :
  `https://www.bct.gov.tn/bct/siteprod/tableau_statistique.jsp?params=PL237010`. Lignes citées :
  « Avoirs nets en devises (en MDT) » 25 003,1 … 23 679,2 ; **« Avoirs nets en devises (en jours
  d'importation) » 103 / 103 / 98 / 90 / 100 / 91** (2020→2025).
- Exportations/importations : tables BCT annuelles `PL203190` (Exportations FOB) et `PL203200`
  (Importations CAF) ; viewer `tableau_statistique_a.jsp`. Aussi dans la balance des paiements
  (`PL231010…`, `tab_trimestriel.jsp`) et le Rapport annuel.
- **Couverture** : table en ligne 2020→2025 ; long historique dans BSF/RA (PDF).
- **Extractibilité** : `PL237010` **HTML statique scrapable** (valeurs courantes dans la page) ;
  séries longues → PDF.
- **Pièges** : « jours » vs « mois » d'importation (BCT publie en **jours** ; diviser par ~30) ;
  avoirs nets vs bruts ; méthodologie commerce extérieur INS (SCIM 2010) signalée en note de table.

## 6. Charge d'intérêt (taux apparent = intérêts / encours)

**Source nationale recommandée : MdF — exécution du budget (§ 1, ligne « Intérêts de la Dette »)
pour le flux d'intérêts ; encours au § 2 pour le dénominateur.** Recoupement BCT (BSF / RA, service
de la dette).
- Flux d'intérêts **isolé et vérifié** dans le PDF d'exécution (§ 1, ligne 6.1 = 6 487,0 MDT).
- **Taux apparent** = intérêts(t) / encours(t-1) : calculable **entièrement en national** (MdF
  exécution + MdF/BCT encours). ⚠ Mélanger un taux apparent global avec un r en devises reste
  incohérent pour r−g (fiche éco § 2c) : pour la part extérieure, prendre le **taux moyen** du
  rapport BCT dette extérieure (`PL235010`, § 4).

---

## Repli international (testé) — WEO / DataMapper FMI

- **Dette** : `GGXWDG_NGDP` (General Government Gross Debt, % GDP) — **API vérifiée, HTTP 200** :
  `https://www.imf.org/external/datamapper/api/v1/GGXWDG_NGDP/TUN` → **41 points**, dont 2024 = 85,6 ;
  2025 = 81,7 ; 2026 = 86,1 ; … 2031 = 88,7 (JSON direct, incluant projections). **Extractibilité :
  JSON, trivial.**
- **Solde primaire** : `GGXONLB_NGDP` **n'existe pas dans DataMapper** — la requête renvoie HTTP 200
  mais **sans bloc `values`** (seulement la liste des pays), donc **série primaire non servie par
  l'API DataMapper**. Le solde primaire WEO existe dans la **base WEO complète** (fichier
  `WEOApr/Oct.xls`, indicateur « General government primary net lending/borrowing », code concept
  variable selon millésime) et dans les rapports Article IV / SRDSF — à récupérer autrement que par
  DataMapper. **Recoupement, non source primaire** (consigne : national d'abord).
- **Banque mondiale** : WDI `GC.*` (central government) et IDS (déjà exploité, note
  `dette-pret-par-pret.md`). Non nécessaire pour les séries budgétaires nationales.

## Verdict — peut-on faire la décomposition et le BBF à partir du national ?

**Oui pour la décomposition Δ(dette/PIB)** : solde primaire (MdF exécution, intérêts isolés +
solde global), dette/PIB (MdF synthèse depuis 1986, XLS), intérieur/extérieur (BCT), effet change
(BCT dette extérieure par devise, pub 107). Toutes les briques sont **nationales et vérifiées**, à
l'exception d'une série primaire **longue et homogène** prête à l'emploi (à reconstruire à partir
de l'exécution ou à recouper au WEO).

**BBF (déficit + amortissements venant à échéance)** : le **déficit** est national (MdF) ; **les
amortissements/tombées de principal** ne sont PAS dans l'exécution synthétique ni dans les tables
BCT en ligne → il faut l'**échéancier** (loi de finances : tableau des ressources d'emprunt et
remboursements en principal ; Rapport sur la dette publique MdF annexe PLF ; IDS pour l'extérieur
PPG déjà en main). **BBF reconstructible mais au prix d'un assemblage** (voir Lacunes).

## Lacunes et reports (pour le backlog — `docs/backlog-routage.md`)

1. **Solde primaire long homogène** : aucune source nationale ne le publie « clé en main » en % PIB
   sur longue période ; à reconstruire (exécution MdF année par année) ou recouper WEO base
   complète. **WEO DataMapper ne sert pas la primaire** (vérifié). → report : fiche série dédiée.
2. **Amortissements / tombées de principal** (pour le BBF) : non trouvés dans les tables en ligne ;
   à extraire des lois de finances (tableaux d'emprunts/remboursements) et du Rapport sur la dette
   publique MdF (annexe PLF `gbo.tn`, arabe) — **page non ouverte dans cette passe**. → à vérifier
   et rapatrier.
3. **Rapport sur la dette publique MdF (annexe 7 PLF, `gbo.tn`, arabe)** : cité mais **non vérifié**
   ici (URL exacte à confirmer). C'est la source nationale la plus complète pour maturité/devise/
   échéancier côté MdF ; doublonne/recoupe la pub 107 BCT. → fiche à ouvrir.
4. **PDF BCT dette extérieure (pub 107, par devise & durée de vie moyenne)** : couche texte et
   structure des tableaux **non vérifiées millésime par millésime** ; tables `.jsp` associées
   **AJAX non scrapables** (POST `chercher.jsp` → HTTP 404). → extraction PDF à chantier (camelot),
   risque OCR sur anciens millésimes 1991-2000.
5. **Incohérence de périmètre à documenter** : dette « Endettement total » BCT (monétaire) vs dette
   publique MdF (budgétaire) vs dette APU WEO — niveaux différents, à expliciter avant tout
   graphe comparatif. Base PIB (ruptures INS 1997/2010/2015, cf. `catalog.yml`) à harmoniser.
6. **Séries BCT en ligne limitées à 2020→2025** (tables `tableau_*.jsp`) : le long historique est
   dans BSF (pub 108) et RA (pub 109), **PDF à parser** — chantier `collecteur-donnees`.
