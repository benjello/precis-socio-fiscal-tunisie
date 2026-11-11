# Série (1) — Comptes des organismes de sécurité sociale (INS), 2001-2025 : note documentaire

> Note documentaire (rôle documentaliste), 10 novembre 2026. Instruit la série (1) du § 3 de
> `cadre-budgetaire-comptable-caisses.md` : `ins-comptes-organismes-securite-sociale`, tableau
> « Comptes des organismes de sécurité sociale » des éditions des comptes de la nation de l'INS.
> Rien n'a été téléchargé ni versionné : tout le matériau est **déjà** dans l'entrepôt
> `tunisia-data` ; cette note en dresse l'inventaire vérifié, page par page, et la marche de
> construction. Aucun fichier du précis ni de `tunisia-data` n'a été modifié.
>
> Conventions : **[S]** source secondaire lue ; **[D]** déduction de la note. Pages « imprimées » =
> folio porté au bas de la page ; pages « PDF » = position dans le fichier. URL ins.tn vérifiées le
> 10 novembre 2026 (`curl -k`, requête partielle : 206, `application/pdf`).

---

## 1. Verdict de couverture

**La couverture 2001-2025 est atteignable, sans trou d'année**, à partir d'une seule famille de
sources : le tableau « Comptes des organismes de sécurité sociale » (secteur S1314), présent dans
**chacune des 19 éditions** des « Comptes de la nation » de l'INS, de 2001-2005 à 2021-2025. Les
19 PDF sont **déjà collectés** dans `tunisia-data`
(`data/raw/ins-publications/comptes-de-la-nation/*.pdf`, collecte du 18 septembre 2026, catalogue
`sources/ins-publications-urls.csv` ; doublons partiels sous
`data/raw/ins-comptes-nationaux-publications/`). J'ai vérifié la présence et les pages du tableau
dans **toutes** les éditions (pdfgrep + lecture de l'en-tête de chaque tableau).

Mais la série n'est **pas homogène d'un bout à l'autre** : elle se compose de **deux tronçons**,
base 1983 (années 2001-2014, SCN 1968/1993 ancien habillage) et base 2015 (années 2015-2025,
SCN 2008), avec un **recouvrement 2015-2017** qui permet de chiffrer la rupture (§ 4). La règle
« longue et homogène d'abord » se satisfait en publiant deux segments homogènes raccordés par une
rupture documentée et chiffrée sur les années de chevauchement — pas en épissant.

Qualité des points extrêmes : dans chaque édition, les deux dernières années sont marquées
« * compte semi-définitif » et « ** compte provisoire ». Au plus récent : **2024 = semi-définitif,
2025 = provisoire** (édition 2021-2025) ; ils seront révisés par les éditions suivantes.

## 2. Inventaire vérifié : le tableau, édition par édition

Le tableau occupe partout une double page (EMPLOIS / RESSOURCES). Vérifications faites le
10 novembre 2026 sur les copies locales de `tunisia-data` (lecture seule).

| Édition | Base | Années du tableau (\*=semi-déf., \*\*=prov.) | Pages PDF | Pages imprimées | Fichier local (`data/raw/ins-publications/comptes-de-la-nation/`) | URL (vérifiée) |
|---|---|---|---|---|---|---|
| 2001-2005 (« volume n° 11 », déc. 2006) | 1983 | 2001 2002 2003 2004\* 2005\*\* | 68-69 | 66-67 | `2001-2005.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2001_2005.pdf |
| 2002-2006 | 1983 | 2002 2003 2004 2005\* 2006\*\* | 68-69 | 66-67 | `2002-2006.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2002_2006.pdf |
| 2003-2007 | 1983 | 2003 2004 2005 2006\* 2007\*\* | 68-69 | 66-67 | `2003-2007.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2003_2007.pdf |
| 2004-2008 | 1983 | 2004 2005 2006 2007\* 2008\*\* | 68-69 | 66-67 | `2004-2008.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2004_2008.pdf |
| 2005-2009 | 1983 | 2005 2006 2007 2008\* 2009\*\* | 112-113 | 112-113 | `2005-2009.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2005_2009.pdf |
| 2006-2010 | 1983 | 2006 2007 2008 2009\* 2010\*\* | 106-107 | 106-107 | `2006-2010.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2006_2010.pdf |
| 2007-2011 | 1983 | 2007 2008 2009 2010\* 2011\*\* | 106-107 | 106-107 | `2007-2011.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2007_2011.pdf |
| 2008-2012 | 1983 | 2008 2009 2010 2011\* 2012\*\* | 106-107 | 106-107 | `2008-2012.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2008_2012_0.pdf |
| 2009-2013 | 1983 | 2009 2010 2011 2012\* 2013\*\* | 106-107 | 106-107 | `2009-2013.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/CNAT%202009-2013.pdf |
| 2010-2014 | 1983 | 2010 2011 2012 2013\* 2014\*\* | 106-107 | 106-107 | `2010-2014.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/CNAT%202010-2014.pdf |
| 2011-2015 | 1983 | 2011 2012 2013 2014\* 2015\*\* | 106-107 | 106-107 | `2011-2015.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/CNAT%202011-2015.pdf |
| 2012-2016 | 1983 | 2012 2013 2014 2015\* 2016\*\* | 106-107 | 106-107 | `2012-2016.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/CNAT%202012-2016.pdf |
| 2013-2017 | 1983 | 2013 2014 2015 2016\* 2017\*\* | 106-107 | 106-107 | `2013-2017.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/CNAT%202013-2017.pdf |
| 2015-2020 (base 2015, vol. A ; aussi vol. B, opérations financières) | 2015 | 2015 2016 2017 2018 2019\* 2020\*\* (6 colonnes) | 102-103 | 102-103 | `2015-2020-base-2015.pdf` (= `CNAT_VolA_2015-2020.pdf` dans `data/raw/ins-comptes-nationaux-publications/`, tableau aux mêmes pages 102-103) | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/comptes%20nationaux%202020.pdf |
| 2017-2021 | 2015 | 2017 2018 2019 2020\* 2021\*\* | 100-101 | 100-101 | `2017-2021.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/comptes%20nationaux%202017-2021_1.pdf |
| 2018-2022 | 2015 | 2018 2019 2020 2021\* 2022\*\* | 100-101 | 100-101 | `2018-2022.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/Rapport%20CNAT-2018-2022.pdf |
| 2019-2023 | 2015 | 2019 2020 2021 2022\* 2023\*\* | 100-101 | 100-101 | `2019-2023.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/Rapport_CNAT%202019_2023.pdf |
| 2020-2024 | 2015 | 2020 2021 2022 2023\* 2024\*\* | 100-101 | 100-101 | `2020-2024.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/Rapport_CNAT_2020_2024.pdf |
| 2021-2025 (édition 2026) | 2015 | 2021 2022 2023 2024\* 2025\*\* | 100-101 | 100-101 | `2021-2025.pdf` | https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/Rapport_CNAT_2021_2025.pdf |

URL testées le 10 novembre 2026 par requête partielle (`curl -k -r 0-2000`) : 206,
`application/pdf`, pour les quatre sondées (2001-2005, 2013-2017, base 2015 2015-2020, 2021-2025) ;
les autres adresses sont celles du catalogue `ins-publications-urls.csv` (collecte du 18 septembre
2026, tailles enregistrées). Les pages de publication `https://www.ins.tn/publication/les-comptes-de-la-nation-AAAA-AAAA`
répondaient par intermittence 500 le 10 novembre 2026 (y compris pour des éditions dont le PDF
répond 206) : l'erreur 500 ne dit rien de l'existence — citer de préférence l'URL directe du PDF.

**Éditions jamais trouvées** : il n'existe sur ins.tn **ni édition 2014-2018 ni édition
2016-2020** (le passage se fait de 2013-2017, dernière en base 1983, à 2015-2020, première en
base 2015) — constat du catalogue (collecte systématique du 18 septembre 2026) et tentatives du
10 novembre 2026 : `CNAT%202014-2018.pdf` et `cnat_2014_2018.pdf` → 404 ; pages de publication →
500 (non concluant). Ce n'est **pas un trou d'années** : 2014 est couverte par les éditions
2010-2014 à 2013-2017, et 2015-2017 par les deux bases. La page
`les-comptes-de-la-nation-en-2018` existe au catalogue mais n'expose aucun PDF.

## 3. Ce que le tableau donne (et ne donne pas)

**Contenu, tronçon base 1983 (2001-2014)** [S] — séquence : compte de production (consommation
intermédiaire, VA brute, production), compte d'exploitation (rémunération des salariés = salaires
et traitements bruts + charges sociales ; impôts indirects ; EBE ≈ 0), compte de revenu
(**ressources : cotisations sociales** — 1 795,7 MD en 2001, 2 506,0 en 2005\*\* —, intérêts,
dividendes et autres revenus distribués ; **emplois : prestations sociales, autres transferts
courants**, impôts directs, primes d'assurance-dommages),
compte d'utilisation du revenu (consommation finale, épargne brute), compte de capital (FBCF,
**capacité (+) ou besoin (−) de financement**), compte financier (variations des créances :
monnaies, dépôts non monétaires, **obligations et bons**, crédits, actions…). Lu sur l'édition
2001-2005, p. 66-67.

**Contenu, tronçon base 2015 (2015-2025)** [S] — séquence SCN 2008 : production (marchande / non
marchande), exploitation, **affectation des revenus primaires** (intérêts, revenus distribués),
**distribution secondaire du revenu** (**cotisations sociales** en ressources ; **prestations
sociales en espèces**, **transferts courants entre administrations publiques** — en ressources
*et* en emplois —, coopération internationale, autres transferts divers), utilisation du revenu
(**dépense de consommation finale**), capital (transferts en capital, FBCF, **capacité ou besoin
de financement**, écart statistique), compte financier (numéraire et dépôts, crédits, actions et
titres d'OPC, réserves techniques d'assurance, autres comptes à recevoir/payer). Lu sur les
éditions 2015-2020 (p. 102-103) et 2021-2025 (p. 100-101).

Ordres de grandeur relevés (millions de dinars, pour contrôle d'extraction) : cotisations sociales
reçues 12 197,7 (2021) → 15 165,5 (2025\*\*) ; prestations en espèces 10 577,5 (2021) → 13 235,6
(2025\*\*) ; transferts courants entre APU reçus/versés — les versés 891,8 (2021) ; capacité de
financement 132,5 (2021), 53,3 (2025\*\*) ; en base 1983, prestations sociales 1 403,6 (2001),
capacité de financement 217,8 (2001).

**Ce que le tableau ne donne pas** : aucune ventilation **par caisse** (CNSS/CNRPS/CNAM) ni par
branche ou régime ; pas de bilan (stocks de réserves) — seulement des flux et des variations de
créances ; pas de détail des « transferts courants entre APU » (qui mêlent concours de l'État,
contributions aux hôpitaux, CSS reversée via le compte spécial…). Le volume B 2015-2020
(opérations financières) ne contient **pas** de tableau financier dédié S1314 : seulement la
nomenclature (« S1314 Administrations de Sécurité sociale ») et la mention des sources (« les
rapports annuels des fonds de sécurité sociale ») [S]. Les séries fines du portail
dataportal.ins.tn restent derrière l'API Knoema (cf. `tunisia-data
docs/strategie-acquisition-donnees-ins.md`) ; la page https://www.ins.tn/statistiques/153 publie
les agrégats base 2015 mais pas, à ma connaissance, le compte S1314 isolé.

## 4. Couverture année par année, 2001-2025 (règle « édition la plus récente, dans sa base »)

| Année | Édition retenue (la plus récente qui porte l'année, dans sa base) | Statut au tableau | Pages | Recouvrement disponible |
|---|---|---|---|---|
| 2001 | 2001-2005 (base 1983) | définitif | impr. 66-67 | aucune autre édition ne porte 2001 |
| 2002 | 2002-2006 | définitif | 66-67 | 2001-2005 |
| 2003 | 2003-2007 | définitif | 66-67 | 2001-2005, 2002-2006 |
| 2004 | 2004-2008 | définitif | 66-67 | 3 éditions antérieures |
| 2005 | 2005-2009 | définitif | 112-113 | 4 éditions antérieures |
| 2006 | 2006-2010 | définitif | 106-107 | idem (jusqu'à 4) |
| 2007 | 2007-2011 | définitif | 106-107 | — |
| 2008 | 2008-2012 | définitif | 106-107 | — |
| 2009 | 2009-2013 | définitif | 106-107 | — |
| 2010 | 2010-2014 | définitif | 106-107 | — |
| 2011 | 2011-2015 | définitif | 106-107 | — |
| 2012 | 2012-2016 | définitif | 106-107 | — |
| 2013 | 2013-2017 | définitif | 106-107 | — |
| 2014 | 2013-2017 | définitif (2e colonne) | 106-107 | 2010-2014 (\*\*), 2011-2015 (\*), 2012-2016 (déf.) |
| 2015 | 2015-2020 (base 2015) | définitif | 102-103 | base 1983 : 2011-2015 (\*\*), 2012-2016 (\*), 2013-2017 (déf.) → **chevauchement inter-bases** |
| 2016 | 2015-2020 | définitif | 102-103 | base 1983 : 2012-2016 (\*\*), 2013-2017 (\*) → chevauchement |
| 2017 | 2017-2021 | définitif | 100-101 | base 1983 : 2013-2017 (\*\*) ; base 2015 : 2015-2020 → chevauchement |
| 2018 | 2018-2022 | définitif | 100-101 | 2015-2020, 2017-2021 |
| 2019 | 2019-2023 | définitif | 100-101 | — |
| 2020 | 2020-2024 | définitif | 100-101 | — |
| 2021 | 2021-2025 | définitif | 100-101 | — |
| 2022 | 2021-2025 | définitif (2e colonne) | 100-101 | 2018-2022 (\*\*), 2019-2023 (\*), 2020-2024 (déf.) |
| 2023 | 2021-2025 | définitif (3e colonne) | 100-101 | 2019-2023 (\*\*), 2020-2024 (\*) |
| 2024 | 2021-2025 | **semi-définitif (\*)** | 100-101 | 2020-2024 (\*\*) |
| 2025 | 2021-2025 | **provisoire (\*\*)** | 100-101 | aucune — sera révisé par l'édition 2022-2026 |

**Rupture de base, à chiffrer sur 2015-2017.** Les deux tronçons diffèrent par la base (1983 vs
2015), le cadre (nomenclature des opérations : « prestations sociales » vs « prestations sociales
en espèces » + consommation finale ; « compte de revenu » vs affectation/distribution ;
« obligations et bons » vs « titres de créance »/« crédits ») et sans doute le périmètre des
unités. Les années 2015, 2016 et 2017 existent **dans les deux bases** : la note de concordance de
la série devra publier l'écart, opération par opération, sur ces trois années (en gardant à
l'esprit que les points base 1983 de 2016\* et 2017\*\* ne sont pas définitifs). Appui
méthodologique déjà dans l'entrepôt : `INS_2021-08-15_note_changement_de_base_2015.pdf` et
`INS_2021-03_cnat_presentation_SCNT97.pdf` (`data/raw/ins-publications/comptes-de-la-nation/`).
**Aucune approximation n'est nécessaire** pour cette série : pas de case à estimer.

**Révisions intra-base.** Chaque année figure dans jusqu'à 5 éditions ; les chevauchements
intra-base (colonnes définitives successives) permettent de vérifier la stabilité des valeurs et
de documenter les révisions — à conserver dans les données (une ligne par année × édition), le
« point retenu » n'étant qu'un arbitrage de lecture.

## 5. Marche de construction dans `tunisia-data` (à faire par l'entrepôt, pas ici)

1. **Extraction** : `pdftotext -layout` (les 19 PDF ont une couche texte exploitable — vérifié sur
   2001-2005, 2005-2009, 2010-2014, 2013-2017, 2015-2020, 2017-2021…2021-2025) sur les doubles
   pages du § 2 ; attention aux colonnes décalées (séparateur décimal : point en base 1983,
   virgule en base 2015 ; espaces de milliers en base 2015).
2. **Modèle de données** : une ligne par (édition, base, année, côté emplois/ressources, compte,
   opération, valeur MD, statut `definitif|semi_definitif|provisoire` d'après les astérisques,
   page imprimée, page PDF). Garder **toutes** les éditions, pas seulement la retenue.
3. **Vue « série retenue »** : arbitrage « édition la plus récente dans sa base » (§ 4), comme pour
   `ins-cnat-2015` ; deux segments (2001-2014 base 1983 ; 2015-2025 base 2015), **jamais raccordés
   silencieusement**.
4. **Note de concordance** : tableau des écarts 2015-2017 entre bases, opération par opération ;
   carte de correspondance des nomenclatures (prestations espèces + consommation finale ↔
   prestations sociales ; etc.) ; invariants de contrôle (totaux de comptes, VA = production − CI,
   épargne = RDB − consommation).
5. **Fiche source** : compléter `sources/ins-comptes-nationaux-publications.md` (ou fiche dédiée)
   avec l'index des pages du § 2 — c'est l'équivalent de l'« index des tableaux » de
   `bct-archives.md` pour cette publication.
6. **Contrôles externes** : capacité/besoin de financement S1314 à recouper avec le TOFE du FMI
   (clé `fmi-1997-selected-issues`, tableau 6, pour la méthode ; rapports Article IV récents) et,
   par caisse, avec le rapport entreprises publiques du ministère des Finances (`minfin-ep*`) —
   la somme des trois caisses doit approcher le S1314, l'écart mesurant le champ (autres unités
   classées S1314, le cas échéant CRES, etc.) ; écart à documenter, pas à forcer.

## 6. Références candidates pour le bibliographe

**Déjà présente — aucune clé nouvelle nécessaire.** La clé **`ins-cnat-2015`**
(`precis/fr/references.json`) couvre déjà « l'ensemble des dix-neuf éditions glissantes… de
2001-2005 à 2021-2025 ». **Complément proposé à sa note** (sans changer la clé) :

> Portent aussi, dans chaque édition, le tableau « Comptes des organismes de sécurité sociale »
> (secteur S1314) : édition 2001-2005, p. 66-67 ; 2002-2006 à 2004-2008, p. 66-67 ; 2005-2009,
> p. 112-113 ; 2006-2010 à 2013-2017, p. 106-107 (base 1983, années 2001-2017) ; 2015-2020
> (base 2015, vol. A), p. 102-103 ; 2017-2021 à 2021-2025, p. 100-101 (années 2015-2025).
> Les citations d'année désignent l'édition la plus récente portant l'année, dans sa base.

Si le rédacteur préfère citer le tronçon base 1983 sous une clé distincte (le titre de couverture
diffère : « Les Comptes de la Nation Base 1983, agrégats et tableaux d'ensemble AAAA-AAAA »),
proposition :

```json
{"id": "ins-cnat-1983", "type": "report",
 "title": "Les comptes de la nation, base 1983 : agrégats et tableaux d'ensemble (éditions 2001-2005 à 2013-2017)",
 "author": [{"literal": "Institut national de la statistique (Tunisie)"}],
 "issued": {"date-parts": [[2006]]},
 "URL": "https://www.ins.tn/sites/default/files-ftp3/files/publication/pdf/cnat_2001_2005.pdf",
 "note": "citation-key: ins-cnat-1983\nTreize éditions glissantes en base 1983 (2001-2005, décembre 2006, « volume n° 11 », à 2013-2017). Tableau « Comptes des organismes de sécurité sociale » : p. 66-67 (éditions 2001-2005 à 2004-2008), p. 112-113 (2005-2009), p. 106-107 (2006-2010 à 2013-2017). Fichiers et URL par édition : tunisia-data, sources/ins-publications-urls.csv (collecte du 18 septembre 2026) et note documentaire caisses-serie-comptes-organismes-notedoc-2026-11-10.md. URL = édition 2001-2005 (vérifiée le 10 novembre 2026)."}
```

À défaut, tout tient sous `ins-cnat-2015` avec le complément de note — c'est mon option
recommandée (une seule clé pour la publication, pages par édition dans la note).

## 7. Notions à glossaire

Rien de neuf par rapport au § 6 de `cadre-budgetaire-comptable-caisses.md`, qui propose déjà
« Administrations de sécurité sociale (S1314) ». Ajouts possibles à la même entrée : préciser que
l'INS publie pour ce sous-secteur un compte complet (production → financier) dans chaque édition
des comptes de la nation. Termes d'appoint, facultatifs : « compte semi-définitif » / « compte
provisoire » (conventions INS, lues en pied des tableaux) — utiles si le précis cite 2024-2025.

## 8. Lacunes et reports (pour le backlog durable)

- **L-s1.1 — Détail du S1314 par caisse : hors de cette source.** Le tableau INS est consolidé ;
  la ventilation CNSS/CNRPS/CNAM passera par les séries (3) et (4) du § 3 (états financiers des
  caisses, rapport EP du ministère des Finances, CRES « statistiques de la sécurité sociale » —
  des fiches CRES existent déjà au catalogue : `cres-lettre-8-atmp-2023.md`,
  `cres-bad-2016-protection-sociale-informel.md`). À traiter avec la série (3), pas ici.
- **L-s1.2 — Composition du sous-secteur S1314.** Aucune édition lue ne liste les unités classées
  S1314 (les trois caisses, sûrement ; le CRES, la CREP d'avant 2004 ?). La note méthodologique
  2021-2025 dit seulement que les sources sont « les états financiers des caisses de sécurité
  sociales ». À demander à l'INS ou à chercher dans le rapport méthodologique du changement de
  base (la présentation SCNT97 et la note d'août 2021 sont dans l'entrepôt, à lire sous cet angle
  au moment de la note de concordance).
- **L-s1.3 — Années 2024-2025 non définitives.** 2024 semi-définitif, 2025 provisoire (édition
  2021-2025). Prévoir la mise à jour à la parution de l'édition 2022-2026 (page
  `les-comptes-de-la-nation-2022-2026` à surveiller sur ins.tn).
- **L-s1.4 — Page `les-comptes-de-la-nation-en-2018` sans PDF** (catalogue, collecte du
  18 septembre 2026) : contenu inconnu, peut-être une publication annuelle isolée. Sans effet sur
  la couverture ; à élucider à l'occasion.
- **L-s1.5 — Pages de publication ins.tn en erreur 500 intermittente** (constaté le 10 novembre
  2026, y compris pour des éditions existantes) : pour le précis, citer les URL directes des PDF ;
  pour l'entrepôt, les copies locales font foi (empreintes au catalogue).

## 9. Recherches infructueuses

Aucune fiche `docs/recherches.yml` à créer : la source visée a été trouvée, complète, dans
l'entrepôt ; les seules requêtes restées vaines sont les tentatives d'éditions 2014-2018 et
2016-2020 (§ 2 : 404 sur deux motifs d'URL de fichier, 500 non concluant sur les pages), dont
l'inexistence s'explique par le changement de base — consignée ici, pas matière à fiche JORT.
