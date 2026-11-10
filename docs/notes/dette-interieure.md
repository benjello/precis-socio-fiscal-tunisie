# Dette intérieure — note de faisabilité sourcée

Note documentaire (documentaliste). Objet : **à quelle maille** la dette **intérieure** de l'État
tunisien (titres émis en dinars sur le marché local) est reconstituable à partir de sources
publiques, et avec quel effort d'extraction. Pendant intérieur de `dette-pret-par-pret.md`
(extérieur) et de `annexe-dette-publique.md` (cadrage). Rien n'est avancé sans source vérifiée ;
les valeurs citées sont datées et renvoient à l'URL qui les rend.

Vérifications exécutées le **2026-11-09** : `jort_cache.db` local (SQLite immuable) ; pages BCT,
ministère des Finances (MdF), Tunisie Clearing, BVMT en ligne, URL vérifiées par requête HTTP.

---

## 1. Les titres d'État et leur maille (ligne de BTA = pendant intérieur du « prêt par prêt »)

La dette intérieure de l'État est émise en **titres d'État en dinars**, par **adjudication**, dans
le cadre du **décret n° 97-2462 du 22 décembre 1997** (fixant les conditions et modalités
d'émission et de remboursement des bons du Trésor), modifié en 1999, 2000 et 2006. Deux familles
vivantes :

- **BTA — Bons du Trésor assimilables** : moyen/long terme, **valeur nominale 1000 DT**, taux de
  coupon **fixe** fixé avant la première adjudication, intérêts annuels à terme échu sur base
  réelle/365 [MdF, *Produits*, https://www.finances.gov.tn/fr/produits, consulté 2026-11-09].
  Une **ligne** = « BTA X% <mois aaaa> » identifiée par un **code ISIN**, avec **coupon, date
  d'échéance, date de jouissance, encours**. Exemples de lignes réelles, admises à la cote BVMT :
  - **BTA 8% Janvier 2029**, ISIN **TNHUVZNLATV4** [Kapitalis, 2023-01-07,
    https://kapitalis.com/tunisie/2023/01/07/bourse-de-tunis-demarrage-de-negociation-dune-ligne-de-bta/].
  - **BTA 9,70% Oct 2027**, ISIN **TN9EGII9CQ82**, nominal 1000 TND, jouissance du 16 octobre 2024
    au 14 octobre 2027 [Managers, 2024-10-21,
    https://managers.tn/2024/10/21/bvmt-demarrage-de-negociation-dune-ligne-de-bta/].
- **BTCT — Bons du Trésor à court terme** : 13 / 26 / 52 semaines, par adjudication.

**Verdict de maille (titres)** : l'équivalent intérieur du « prêt par prêt » est la **ligne de
titre** (ISIN + coupon + échéance). Cette maille est **publique et vivante** pour les lignes
cotées — c'est **plus fin** que l'extérieur (où le registre JORT ne descend qu'au texte
d'approbation). Ce qui n'est pas public à cette maille : la **détention** (qui porte chaque ligne),
seulement agrégée banques / assurances / OPCVM par ailleurs.

## 2. Tunisie Clearing (dépositaire central) / BVMT — testé

**URL testée** : *Analyse de la courbe des taux des valeurs du Trésor*,
https://www.tunisieclearing.com/upload/202602/638a9f44-96ef-4de0-95de-9ab24416c16f.pdf
(HTTP 200, `application/pdf`, 633 353 octets, consulté 2026-11-09). Le bulletin descend à la
**ligne** et cite coupon + échéance + taux de rendement + volume traité, p. ex. :

> « BTA 9.40% août 2033 avec un volume de 131,323 MDT et un taux de rendement de 9,25% » ;
> « BTA 7.75% 05 mars 2036 avec un volume de 93,794 MDT et un taux de rendement de 8,80% »
> [Tunisie Clearing, courbe des taux, fév. 2026, URL ci-dessus].

Attention de lecture : le **volume** cité est le **volume de transaction** sur le marché
(primaire/secondaire) du jour, **pas l'encours de la ligne**. La courbe donne donc coupon +
échéance + **taux de rendement** par ligne ; l'**encours par ligne** se lit dans le *Bulletin
Quotidien des Avis* / la liste des valeurs du Trésor de Tunisie Clearing et sur la fiche BVMT de
chaque ligne (admission, ISIN, nominal, jouissance). **Format** : PDF texte (extractible) pour la
courbe ; les listes d'encours par ligne sont en PDF/portail, extraction au cas par cas.
**Effort** : moyen (PDF à parser, nouvelle émission ≈ hebdomadaire).

→ **À rapatrier/indexer** dans `tunisia-data` : bulletins quotidiens + courbe des taux Tunisie
Clearing (série d'encours ligne-à-ligne), avec URL d'origine et date de collecte.

## 3. Ministère des Finances (DGGDCF) — adjudications : calendrier + résultats

- **Calendrier indicatif** des émissions BTA/BTCT, annuel [MdF, *Adjudications*,
  https://www.finances.gov.tn/fr/adjudications, HTTP 200, consulté 2026-11-09 ; calendriers listés
  au moins depuis 2013-2015].
- **Produits / mécanique d'adjudication** : « le trésor diffuse via Reuters les principaux
  résultats (montant global émis pour chaque catégorie de titres, **prix moyen pondéré**, prix
  limite accepté…) » [MdF, *Produits*, https://www.finances.gov.tn/fr/produits, consulté
  2026-11-09].
- **Résultats par adjudication** (montant retenu, **taux moyen pondéré** TMP, maturité) : diffusés
  par le Trésor et repris par les intermédiaires (SVT) — p. ex. une adjudication BTA à échéances
  2031/2036/2038 avec **TMP compris entre 8,34 % et 8,79 %** [TeraFinances,
  https://terafinances.com/adjudication-de-bta-le-tresor-leve-223-5-mdt-385] ; fiches SVT type
  Tunisie Valeurs (TMP par ligne, montant levé vs annoncé).

**Maille** : par **adjudication** et par **ligne** (montant retenu, TMP, maturité). **Format** :
HTML (calendrier) + bulletins PDF des SVT. **Effort** : moyen ; une **série temporelle** de TMP /
montants levés est reconstituable mais dispersée (MdF + SVT). → **À rapatrier** : page MdF
adjudications + bulletins d'adjudication (série TMP par date).

## 4. BCT — encours Bons du Trésor (agrégé) — testé

**URL testée** : *Indicateurs monétaires et financiers quotidiens*,
https://www.bct.gov.tn/bct/siteprod/indicateurs.jsp (HTTP 200, consulté 2026-11-09, page « Mis à
jour le 09/11/2026 »). Rubrique **V — BONS DU TRESOR** (en MDT) :

| Indicateur | Donnée (06/11/2026) | Un an avant |
|---|---:|---:|
| Encours Bons du Trésor à court terme (BTCT) | **1 645,6** | 3 010,6 |
| Encours Bons du Trésor Assimilables (BTA) | **36 689,6** | 28 355,7 |

[BCT, indicateurs quotidiens, URL ci-dessus, consulté 2026-11-09]. Recoupe la presse spécialisée
(encours total des Bons du Trésor ≈ 37,5 Md DT à fin août 2026, dont BTA ≈ 35,8 Md DT, +25 % sur un
an [businessnews.com.tn, 2026-09-02 ; leconomistemaghrebin.com, 2026-09-03], qui citent la BCT).

La BCT publie aussi des **tables rétrospectives** « Encours Bons du Trésor » et « Bons du Trésor »
sous `stat_page.jsp?id=136` et `tableau_n.jsp` (séries PL130xxx) — **maille agrégée** (encours
total, par échéance/instrument), **pas** par ligne ni par détenteur. **Format** : HTML
(JSP, séries interrogeables). **Effort** : faible (scrape de table). → **À rapatrier** : séries
BCT « Encours Bons du Trésor » (BTA / BTCT), mensuelles/quotidiennes.

## 5. Rapport sur la dette publique (annexe n° 7 au PLF, gbo.tn) — ventilation par instrument

Le **Rapport sur la dette publique** annexé au projet de loi de finances (annexe n° 7, *gbo.tn*,
**arabe seulement**, « التقرير حول الدين العمومي ») ventile la dette **intérieure par instrument**
(BTA, BTCT, emprunts nationaux…), **agrégée** par année. Clés CSL déjà au projet : `minfin-dette-2022`,
`minfin-dette-2025` (cf. `annexe-dette-publique.md` § 2.1). **Maille** : par instrument, par année,
pour le stock et le service. **Format** : PDF (arabe). **Effort** : moyen (tables arabes à relever).
C'est la source **officielle** de la ventilation agrégée intérieur/instrument ; le détail
ligne-à-ligne n'y figure pas.

## 6. JORT — census des emprunts intérieurs (cadre légal + ère pré-BTA)

Requête de référence (rejouable), base
`sqlite3 'file:/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db?immutable=1'` ;
`LIKE` écrit **sans accent** (piège `outillage-sources.md` §1 c) :

```sql
SELECT recid,type,numero,jort_annee,jort_numero,pages,objet,titre,pdf_fr
FROM textes
WHERE jort_annee BETWEEN 1956 AND 2026
  AND ( titre LIKE '%emprunt national%'
     OR titre LIKE '%emprunt obligataire%'
     OR titre LIKE '%bons du tr%sor%'       -- absorbe l'accent de « Trésor »
     OR titre LIKE '%bons d%quipement%'     -- titres d'État pré-BTA (1956-1992)
     OR titre LIKE '%رقاعي%'                -- intitulés arabes seuls (2016+)
     OR titre LIKE '%رقاع الخزينة%' )
ORDER BY jort_annee, jort_numero;
```

**Résultat : 198 textes** (registre `dette-interieure-registre-jort.csv`), dont les **118** de la
requête à quatre familles françaises demandée (= emprunt national 6 + emprunt obligataire 97 + bons
du Trésor 15 ; « emprunt intérieur » / « emprunt de l'État » : 0 occurrence dans les titres).

**Caveat taxonomique majeur** (vérifié par lecture des titres) : les **97 « emprunt obligataire »
sont très majoritairement des émissions obligataires d'entreprises et de banques** (sociétés, BCT,
BDET, CNEL…), autorisées / garanties / rétrocédées à l'État — **pas** de la dette d'État émise au
guichet. Elles ne sont dette **intérieure de l'État** que lorsque le titre porte **rétrocession à
l'État** (25) ou **garantie de l'État** (2). La colonne `categorie` du registre distingue :
`etat_emprunt_national`, `etat_bons_tresor`, `etat_bons_equipement`, `obligataire_corporatif`,
`obligataire_retrocede_etat`, `obligataire_garanti_etat`, `ar_rqaai`.

Compte par catégorie : obligataire_corporatif 70 · bons d'équipement 63 · obligataire rétrocédé
État 25 · arabe رقاعي 17 · bons du Trésor 15 · emprunt national 6 · obligataire garanti État 2.

Compte par décennie (198) :

| Décennie | textes |
|---|---:|
| 1950 | 10 |
| 1960 | 15 |
| 1970 | 28 |
| 1980 | 28 |
| 1990 | 27 |
| 2000 | 28 |
| 2010 | 37 |
| 2020 (→2026) | 25 |

Ce que le JORT apporte réellement pour la dette **intérieure de l'État** :
- le **cadre légal des bons du Trésor** : décret-loi n° 63-14 du 9 août 1963 (première émission de
  bons du Trésor) ; **décret n° 97-2462 du 22 décembre 1997** (cadre BTA/BTCT), modifié 1999/2000/2006 ;
- l'**ère pré-BTA** des titres d'État souscrits au guichet : **bons d'équipement** (tranches
  annuelles 1956-1992) et **emprunts nationaux** (emprunt national pour l'industrialisation 1957 ;
  emprunt national 5 % 1967, clôturé par la loi n° 70-11 ; emprunts nationaux 1986, 1988) ;
- le retour récent de l'**emprunt national obligataire souscrit** (arabe « القرض الرقاعي الوطني ») :
  p. ex. **arrêté/amr n° 33 de 2023** portant émission du *Crédit obligataire national 2023*
  [JORT 2023, https://www.pist.tn/jort/2023/2023A/Ja0092023.pdf, édition arabe].

Le titre JORT **ne porte pas** l'encours, le taux ni le ventilation par détenteur ; il date et
fonde les instruments. Comme à l'extérieur, un même emprunt peut générer plusieurs textes
(autorisation + modalités + clôture).

URL JORT vérifiées (pist.tn, édition de la langue, 2026-11-09) :
- décret 97-2462 : https://www.pist.tn/jort/1997/1997F/Jo10497.pdf (JORT n° 104/1997)
- décret-loi 63-14 : https://www.pist.tn/jort/1963/1963F/Jo03763.pdf (JORT n° 37/1963)
- emprunt national industrialisation 1957 : https://www.pist.tn/jort/1957/1957F/Jo11557.pdf (n° 115/1957)
- crédit obligataire national 2023 (ar) : https://www.pist.tn/jort/2023/2023A/Ja0092023.pdf (n° 9/2023)

## 7. Verdict de maille — jusqu'où descend le public

- **Ligne de titre vivante (BTA/BTCT)** : OUI, **publique** — ISIN, coupon, échéance, jouissance,
  nominal 1000 DT, taux de rendement (Tunisie Clearing, BVMT) ; montant retenu + TMP par
  adjudication (MdF + SVT). C'est **plus désagrégé que l'extérieur**.
- **Encours par instrument (BTA / BTCT), quotidien et rétrospectif** : OUI — **BCT** (indicateurs
  quotidiens + séries PL130xxx), agrégé.
- **Encours par ligne (stock par ISIN)** : OUI mais **à collecter** dans les bulletins Tunisie
  Clearing / fiches BVMT (pas de table unique téléchargeable ; effort moyen, PDF).
- **Ventilation intérieur / instrument par année** : OUI — **annexe 7 au PLF** (arabe, agrégé).
- **Ère pré-BTA (bons d'équipement, emprunts nationaux)** : cadre et émissions **datés** par le
  JORT ; **encours** historiques non ligne-à-ligne.

Ce qui **n'est PAS public** à maille fine :
- **détenteurs** d'une ligne (banques, assurances, OPCVM, non-résidents) : seulement agrégés
  ailleurs, jamais par ISIN ;
- **ventilation fine banques / non-banques** de l'encours intérieur : non publiée à la ligne ;
- encours **ligne-à-ligne historisé** en série longue téléchargeable : à reconstituer par collecte.

**Conclusion** : la dette intérieure est reconstituable **à la ligne de titre pour le stock
vivant** (via Tunisie Clearing/BVMT + MdF), **à l'instrument et à l'année pour les séries**
(BCT + annexe 7), et **au texte** pour le cadre et l'ère pré-BTA (JORT). Le point aveugle est la
**détention** (qui porte la dette), non publique à maille fine.

---

## Lacunes / reports (pour backlog durable)

- **Encours par ligne (ISIN)** : pas de table unique publique ; à collecter dans les bulletins
  Tunisie Clearing. → rapatrier série dans `tunisia-data`.
- **Série TMP / montants d'adjudication** : dispersée MdF + SVT ; à consolider.
- **Annexe 7 (dette publique)** : PDF arabe, tables à relever ; clés `minfin-dette-2022/2025`.
- **Détenteurs par ligne / ventilation banques-non-banques fine** : **non public** — à acter comme
  limite structurelle, ne pas chercher à l'instrument.
- **Séries BCT PL130xxx** : identifier les codes exacts de l'encours BTA/BTCT (table rétrospective)
  pour scrape reproductible.

## À rapatrier / indexer dans `tunisia-data` (signalé, non téléchargé ici)
- Bulletins quotidiens + courbe des taux Tunisie Clearing (encours & rendement ligne-à-ligne), URL
  https://www.tunisieclearing.com/ , avec date de collecte + SHA-256.
- Séries BCT « Encours Bons du Trésor » (BTA/BTCT), https://www.bct.gov.tn/bct/siteprod/ .
- Page MdF adjudications + calendriers + résultats, https://www.finances.gov.tn/fr/adjudications .
- Rapport sur la dette publique (annexe 7), gbo.tn (arabe).
- Décret 97-2462 et modificatifs (cadre BTA/BTCT) — déjà citables via pist.tn.
