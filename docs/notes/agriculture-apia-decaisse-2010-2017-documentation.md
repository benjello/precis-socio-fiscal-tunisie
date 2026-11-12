# Documentation — primes d'investissement agricole **décaissées** par l'APIA, trou **2010-2017**

Rôle : documentaliste. Date : 11 novembre 2026. Livre : « L'agriculture — le soutien au
producteur », chapitre 5 (encouragements à l'investissement). Objet : combler le **trou 2010-2017**
de la série des primes d'investissement agricole **effectivement décaissées / versées** par l'APIA
(صرف المنح / أذون بالصرف), par opposition aux primes **approuvées** (المصادق عليها). État antérieur
(note `agriculture-apia-primes-versees-documentation.md`) : série décaissée **homogène 2018-2023**
(rapports d'activité annuels APIA, section صرف المنح) + **un point 2009** (54 MD, Banque mondiale).
Manquants : **2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017**.

## Résultat : **série décaissée 2010-2017 NON trouvée** — indisponibilité motivée et datée

Au terme des recherches ci-dessous (Wayback CDX, 11/11/2026), **aucune valeur de primes décaissées
APIA pour 2010-2017 n'a pu être sourcée**. Le trou **reste ouvert**, et il se laisse honnête. Trois
constats, convergents, l'expliquent et le motivent :

1. **Aucun rapport d'activité annuel de l'APIA (تقرير نشاط الوكالة) pour 2010-2017 n'a jamais été mis
   en ligne.** Le CDX sur le dossier `apia.com.tn/medias/files/Rapports-Apia/*` ne rend, pour les
   *rapports d'activité*, **que les millésimes 2018 à 2023** (+ rapports de conseil d'administration
   2020-2025, + « Rapport statistique année 2024 »). La page-liste `rapports-apia.html`, dans sa
   **plus ancienne capture (2021-07-30)**, ne listait déjà aucun rapport d'activité antérieur à
   2018 (seulement des rapports de conseil 2020-2021).
2. **La section « décaissement des primes » (صرف المنح) n'existe dans les rapports APIA qu'à partir
   de 2018, et le rapport 2018 le dit explicitement** : 2018 est « **السنة األولى لصرف المنح في إطار
   قانون اإلستثمار** » — *la première année de décaissement des primes dans le cadre de la loi de
   l'investissement* [loi n° 2016-71, en vigueur depuis le nouveau régime 2017]. Le dispositif de
   décaissement tel que **rapporté** (ordres de paiement أذون بالصرف adressés à la BNA, suivi du
   صرف) démarre donc en 2018 ; il n'existe pas d'équivalent publié pour le régime antérieur (Code
   d'incitation aux investissements / FOSDA/FOSDAP), du moins pas en ligne.
3. **Les publications APIA pré-2018 réellement en ligne ne portent que l'approuvé, jamais le
   décaissé.** Le bulletin statistique annuel (`ANNEE_YYYY.pdf`) ne contient **aucune** occurrence
   de صرف/أذون (vérifié sur l'édition 2018 : 0 occurrence) — il chiffre les primes المصادق عليها.
   Les bulletins de conjoncture mensuels et le `tableau-activites-2017.pdf` ne portent pas non plus
   de décaissé (ce dernier est une liste d'**événements** — tables rondes, formations —, pas de
   chiffres financiers).

**Conclusion.** Le décaissé 2010-2017 ne se comble **pas par le web**. La série décaissée homogène
publiée commence en 2018 ; avant cela, seules des primes **approuvées** sont publiques (agridata
2010-2016, `apia_investissements_subventions_par_gouv_delegation_2010-2016.csv` et
`apia_repartition_doa_2010-2017.xls`, déjà à l'entrepôt). **Ne pas tracer de ligne continue
2009 → 2018** sur le décaissé : laisser les cases 2010-2017 vides et sourcées comme indisponibles.

### Pourquoi l'approximation n'est pas proposée ici
Pas de proxy borné disponible. Le seul candidat serait de dériver le décaissé 2010-2017 d'un ratio
décaissé/approuvé observé en 2018-2023 — mais ce ratio est **très instable** (de ~20 % pour 2018 à
des années où le décaissé approche l'approuvé) et, surtout, il porte sur le **régime post-2016-71**,
étranger au mécanisme de versement d'avant. Appliquer ce ratio à l'approuvé pré-2016 fabriquerait une
valeur dont l'écart n'est pas bornable et pourrait renverser la lecture. **Approximation refusée** :
le trou honnête vaut mieux. La **source qui comblerait** : un rapport d'activité APIA 2010-2017 (s'il
en existe un non numérisé) ou une série de décaissements du FOSDAP/FOSDA via le **Rapport sur
l'activité des Fonds spéciaux du Trésor** (annexe au PLF, كشف الحساب du fonds, ligne تدخّلات) — piste
non épuisée, voir Backlog.

## Documents indexés dans `tunisia-data/data/raw/apia/`
**Aucun nouveau document pertinent récupéré** (donc aucune nouvelle ligne au catalogue
`sources/apia-agridata-urls.csv`). Un PDF a été téléchargé pour vérification puis **écarté** (hors
sujet, non indexé) : `tableau-activites-2017.pdf` (liste d'événements 2017, aucun chiffre de
décaissé). Les rapports d'activité 2018-2023 et bulletins statistiques 2018-2025 restent indexés de
la passe précédente (note sœur).

## Références CSL candidates
- Aucune nouvelle **référence de donnée décaissée 2010-2017** (série introuvable).
- Référence de **contexte** utile au rédacteur (déjà récupérée, déjà indexée) :
```json
{"id":"apia-rapport-activite-2018","type":"report",
 "title":"Rapport d'activité de l'APIA — année 2018 (تقرير نشاط الوكالة بعنوان سنة 2018)",
 "author":[{"literal":"Agence de promotion des investissements agricoles (APIA)"}],
 "issued":{"date-parts":[[2019]]},
 "URL":"https://www.apia.com.tn/medias/files/Rapports-Apia/Rapport-ActivitEs-2018.pdf",
 "note":"Atteste que 2018 est la PREMIÈRE année de décaissement des primes (صرف المنح) sous la loi de l'investissement 2016-71 (« السنة األولى لصرف المنح في إطار قانون اإلستثمار »). Fonde le constat d'absence d'une série décaissée publiée pour 2010-2017. Copie locale : tunisia-data/data/raw/apia/apia_rapport_activite_2018.pdf. Consulté le 11/11/2026."}
```

## Notions à glossaire (vérifier/ajouter)
- **Prime décaissée / versée** (صرف المنح ; أذون بالصرف = ordres de paiement) — *vs* **prime
  approuvée / octroyée** (المنح المصادق عليها). Distinction centrale du chapitre 5 ; source canonique
  pressentie : rapport d'activité APIA 2018, §III-1.
- **FOSDAP / Fonds spécial de développement agricole et de la pêche** — support budgétaire des
  primes et prêts d'investissement servis via l'APIA (cf. fiche recherches existante, loi n° 63-17
  du 27 mai 1963). C'est par ce fonds qu'une série de décaissements pré-2018 pourrait exister.

## Lacunes (TODO, ne rien inventer)
- **Décaissé APIA 2010-2017** : introuvable en ligne au 11/11/2026. À tenter hors web : demande
  directe à l'APIA (service suivi/décaissement) ; **Rapport sur l'activité des Fonds spéciaux du
  Trésor** (FOSDAP, ligne تدخّلات / décaissements de primes agricoles), éditions PLF couvrant
  2010-2017 ; bibliothèques de dépôt (INS, ministère de l'Agriculture).
- **Rupture de concept à conserver** : même retrouvée, une série de décaissements FOSDAP serait d'une
  **autre famille** (Trésor, pas rapport d'activité APIA) et sous régime pré-2016-71 ; à ne pas
  épisser muettement avec la série APIA 2018-2023.

## Recherches infructueuses (requêtes CDX, couverture datée)
Toutes lancées le **2026-11-11** via `web.archive.org/cdx/search/cdx`. Couverture : captures Wayback
indexées jusqu'au 2026-11-11.
1. `url=apia.com.tn/medias/files/Rapports-Apia*` (`collapse=digest`) → rapports d'activité **2018-2023
   seulement** ; aucun 2010-2017. **Couvre** tout le dossier Rapports-Apia tel qu'archivé.
2. `url=apia.com.tn` `matchType=domain` `filter=original:.*\.pdf` (784 PDF distincts) → grep
   `activit|rapport|bilan|نشاط` : seuls rapports d'activité 2018+, études filières, rapports de
   conseil. Aucun rapport d'activité ni « décaissé » 2010-2017.
3. `url=apia.com.tn/rapports-apia.html` (`collapse=digest`, 24 captures, **plus ancienne
   2021-07-30**) → page-liste ne référence aucun rapport d'activité < 2018.
4. `url=apia.nat.tn` `matchType=domain` (ancien domaine Joomla) → **10 URL distinctes seulement**
   (pages d'accueil ar/en/fr 2009-2024, 2 logos, robots.txt, 2 `index.php?` de contenu) ; **aucun
   PDF archivé**. Le site historique n'a pas conservé de rapports/statistiques téléchargeables.
5. Vérifications de contenu (fetch brut `…id_/…`) : `tableau-activites-2017.pdf` (événements, pas de
   chiffres) ; bulletin statistique 2018 `grep صرف/أذون` = 0 (confirme que l'approuvé seul y figure) ;
   `ANNEE_2016.pdf` = **302 puis 404** sur Wayback, **aucune capture 200** (non récupérable ; et de
   toute façon bulletin = approuvé).
*Note méthodo* : le CDX rend des candidats, pas une preuve de non-existence. Le constat « pas en
ligne » est solide ; il n'exclut pas un rapport APIA 2010-2017 **non numérisé** (→ Backlog, demande
directe). *Ne pas relancer la chasse web sans élément nouveau (nouveau dossier d'URL, nouveau
domaine).*

## Backlog
*(À router par l'archiviste-backlog / l'agent data ; je propose, je n'écris pas dans
`backlog-precis.md`.)*
- **Chapitre précis (`backlog-precis.md`)** : série « primes APIA **décaissées** » — cases
  **2010-2017 vides et sourcées « indisponible, non publié en ligne »** (ce constat daté 11/11/2026).
  État : *à obtenir hors web*. Ne pas interpoler.
- **Entrepôt `tunisia-data` (note + PR)** : piste non épuisée — extraire les **décaissements de
  primes agricoles du FOSDAP** depuis le *Rapport sur l'activité des Fonds spéciaux du Trésor*
  (annexe PLF), éditions couvrant 2010-2017, كشف الحساب du fonds, ligne تدخّلات ; vérifier si le
  périmètre recoupe le « صرف المنح » APIA. Si oui → série décaissée reconstituée d'une autre famille,
  à documenter en note de concordance.
- **Demande directe APIA** : solliciter le service suivi/décaissement pour une série annuelle
  décaissée 2010-2017 (ordres de paiement exécutés). Noté comme piste, non engagée.
