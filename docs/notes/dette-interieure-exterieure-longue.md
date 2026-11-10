# Dette de l'État — ventilation intérieure / extérieure sur longue période

Note documentaire (documentaliste). Recherche d'une source **vérifiée** donnant la ventilation
**dette intérieure / dette extérieure** de la dette publique (budgétaire) de l'État sur une
profondeur historique supérieure à la série BCT en ligne `dette-etat-interieur-exterieur`
(2020-2025) déjà portée par la figure de l'annexe. Priorité au national (BCT, ministère des
Finances) ; FMI/BM en repli. Toutes les URL ci-dessous ont été testées par `curl` (code HTTP
indiqué) ; toutes les valeurs citées sont lues dans le PDF/HTML nommé.

> **Piège de périmètre à ne jamais confondre** (confirmé par les documents) :
> - **« Encours de la dette publique »** (source : *ministère des Finances / MEFAI*) = dette
>   **budgétaire** de l'État, ventilée **intérieure / extérieure** par devise et marché
>   d'émission. **C'est la série cherchée**, homogène avec la série BCT 2020-2025 en place.
> - **« Endettement total (ET) » / « Endettement intérieur / extérieur »** (sources : BCT, CMF) =
>   agrégat **monétaire** de financement de l'économie (tous agents non financiers résidents, dont
>   l'État). Périmètre **plus large**, décomposé Etat / autres agents ; **ne pas mélanger** avec la
>   dette publique budgétaire. C'est le tableau XIII-6 du Bulletin statistique des finances et le
>   tableau 2-15 du Rapport annuel BCT.

---

## 1. Source recommandée — BCT, Rapport annuel, tableau « Encours de la dette publique »

**C'est la meilleure source pour une série longue intérieur/extérieur en national.** Chaque
Rapport annuel de la BCT (pub. 109, corpus local `~/projets/tunisia-data/data/raw/bct-archives/109`)
porte un tableau **« Encours de la dette publique »** attribué au **ministère des Finances (MEFAI)**,
donnant **Dette intérieure / Dette extérieure / Total**, chacune **en MDT, en % du total et en % du
PIB**, pour **3 exercices** (année n-1, n, et n+1 en prévision/LF). En **chaînant** les rapports
successifs on reconstitue une **série annuelle continue en MDT et en % du PIB**.

- **Format / extractibilité** : PDF **français** avec **couche texte** propre ; `pdftotext -layout`
  restitue le tableau sans OCR. Vérifié sur RA 2010, 2017, 2020, 2024.
- **Périmètre** : dette publique **budgétaire** de l'État (= série cherchée), source MinFin.
- **Couverture** : tableau présent au moins de l'exercice 2008 (RA 2010) à 2025 (RA 2024, prévision
  LF 2025). Les rapports locaux vont de `RA_fr_1986.pdf` à `RA_2025_fr.pdf` ; la **forme tabulée
  intérieure/extérieure** est nette à partir des années 2000 (voir § Lacunes pour l'avant-2008).

### Échantillon de valeurs lues (MDT ; % du total ; % du PIB)

Fichier `109/RA_2024_fr.pdf`, **Tableau 2-14 « Encours de la dette publique »** (Source :
Ministère des Finances) :

| Exercice | Dette intérieure | Dette extérieure | Total | Total % PIB |
|---|---|---|---|---|
| 2023 | 59 797,4 (47,2 % ; 39,9 % PIB) | 66 874,2 (52,8 % ; 44,7 % PIB) | 126 671,6 | 84,6 % |
| 2024 | 72 688,6 (53,8 % ; 43,7 % PIB) | 62 343,7 (46,2 % ; 37,5 % PIB) | 135 032,3 | 81,2 % |
| 2025* | 85 984,0 (58,3 % ; 47,0 % PIB) | 61 418,0 (41,7 % ; 33,5 % PIB) | 147 402,0 | 80,5 % |

(* provisoire, LF 2025.)

Fichier `109/RA_2020_fr.pdf`, **Tableau 2-15 « Encours de la dette publique »** (Source : MEFAI) :

| Exercice | Dette intérieure | Dette extérieure | Total | Total % PIB |
|---|---|---|---|---|
| 2019 | 24 727,3 (29,7 % ; 22,3 % PIB) | 58 606,3 (70,3 % ; 52,8 % PIB) | 83 333,6 | 72,5 % |
| 2020 | 31 681,8 (34,1 % ; 28,7 % PIB) | 61 277,0 (65,9 % ; 55,6 % PIB) | 92 958,8 | 84,3 % |
| 2021* | 35 024,0 (32,1 % ; 28,9 % PIB) | 74 212,0 (67,9 % ; 61,2 % PIB) | 109 236,0 | 90,1 % |

Fichier `109/rapport2010.pdf`, **tableau « ENCOURS DE LA DETTE PUBLIQUE »** :

| Exercice | Dette extérieure | Dette intérieure | Total | Total % PIB |
|---|---|---|---|---|
| 2008 | 14 559,9 (60,9 % ; 26,3 % PIB) | 9 366,6 (39,1 % ; 17,0 % PIB) | 23 926,5 | 43,3 % |
| 2009 | 14 715,7 (58,4 % ; 25,1 % PIB) | 10 474,3 (41,6 % ; 17,8 % PIB) | 25 190,0 | 42,9 % |
| 2010 | 15 550,5 (60,7 % ; 24,5 % PIB) | 10 089,1 (39,3 % ; 15,9 % PIB) | 25 639,6 | 40,4 % |
| 2011 (LFC) | 17 593,0 (59,6 %) | 11 935,8 (40,4 %) | 29 528,8 | 44,1 % |

> **Rupture lisible et à commenter, pas à lisser** : la structure bascule sur la période. Jusque
> ~2019 l'**extérieure domine** (≈ 60-70 % du total) ; à partir de 2021-2023 l'**intérieure** passe
> majoritaire (58 % en 2025), effet du recours massif au financement local et de la contraction de
> l'encours extérieur. Deux retraitements à signaler à la rédaction : (a) l'encours **2019** vaut
> 83 333,6 MDT dans RA 2020 (MEFAI) mais 82 554,4 MDT dans l'annexe 7 LF 2021 (§ 3) — révision de
> périmètre/millésime entre sources MinFin ; (b) la part intérieure 2019 est de 29,7 % du total
> (RA 2020) contre 21,04 % du PIB rapporté autrement dans l'annexe 7. Chaîner **une seule famille**
> (idéalement les RA BCT successifs) pour une série homogène, et dater chaque valeur par son rapport
> d'origine.

---

## 2. Source nationale de recoupement — ministère des Finances, « Rapport sur la dette publique » (annexe 7 à la LF), gbo.tn

Le document de référence sur les périmètres (déjà cité dans `annexe-dette-publique.md`,
clés `minfin-dette-2022` / `minfin-dette-2025`). Publié annuellement sur **gbo.tn** (rubrique
« قانون المالية للسنة و الملاحق » → type « تقرير حول الدين العمومي »). Donne la dette
intérieure/extérieure **en % du PIB** (graphiques « Ratios d'endettement ») et des tableaux
d'encours/service, pour **3 exercices** par millésime. Couverture par rapport courte : intérêt =
**recoupement** du tableau BCT, pas série longue.

URL **vérifiées** (code HTTP, taille) — millésimes non devinables par motif régulier, pris dans la
liste officielle `http://www.gbo.tn/ar/Loi-de-Finance-et-rapports-annexes` (200) :

| Millésime | Langue | URL (vérifiée) | HTTP | Extractibilité |
|---|---|---|---|---|
| LF 2021 (exercice 2019 + S1 2020) | **FR** (traduction Expertise France ; « version arabe officielle fait foi ») | `http://www.gbo.tn/sites/default/files/2021-04/Annexe%207%20LF2021%20Dette%20Publique.pdf` | 200 (4,87 Mo) | couche texte FR propre (`pdftotext`) |
| LF 2022 (exercice 2020) | AR | `http://www.gbo.tn/sites/default/files/2022-01/ANNEXE_07%20Dette%20publique.pdf` | 200 (2,39 Mo) | couche texte **arabe** (RTL, formes de présentation) — exploitable mais parsing AR requis |
| LF 2022 (miroir) | AR | `https://www.finances.gov.tn/sites/default/files/2022-02/ANNEXE_07.pdf` | 200 (2,39 Mo) | idem (fichier identique) |
| LF 2024 | AR | `http://www.gbo.tn/sites/default/files/2024-01/التقرير%20حول%20الدين%20العمومي%20%20%20%20ملحق%20عدد_07.pdf` | 200 (11,2 Mo) | couche texte arabe |
| LF 2025 (rapport 2023) | AR | `http://www.gbo.tn/sites/default/files/2025-03/ملحق%207%20الدين%20العمومي.pdf` | 200 (5,22 Mo) | couche texte arabe |

Valeurs lues dans l'annexe 7 **FR** LF 2021 (graphique « Taux d'endettement en % du PIB »,
`Annexe 7 LF2021 Dette Publique.pdf`) — dette intérieure / extérieure / publique **en % du PIB** :
2017 : 21,81 / 48,63 / 70,44 ; 2018 : 20,95 / 57,25 / 78,20 ; 2019 : 21,04 / 51,48 / 72,51 ;
juin 2020 : 25,62 / 53,43 / 79,05. (Valeurs portées par un **graphique** à étiquettes entremêlées :
lecture à re-vérifier case par case avant tout usage chiffré ; le tableau « Chiffres clés » du même
PDF ne donne en MDT que le **total** de l'encours, pas la ventilation.) Tableau cherché en arabe :
« الدين الداخلي » / « الدين الخارجي ».

---

## 3. Ministère des Finances — page « chiffres clés » (HTML)

`https://www.finances.gov.tn/fr/les-indicateurs/chiffres-cles` → **HTTP 200**. Expose en HTML
« الدين الداخلي / الدين العام الخارجي » et un bloc « Encours / Dette Extérieure / Dette Intérieure ».
**Mais page statique figée sur un millésime** : au test, « Chiffres 2016 » — Encours 55 921,4 MDT,
Dette Extérieure 36 413,4, Dette Intérieure 19 508 (+ répartition 36,3 % / 63,7 %). **Pas de série
longue** : un point ponctuel, utile tout au plus comme valeur isolée 2016. Les mêmes libellés
apparaissent aussi dans les **résultats d'exécution du budget** (p. ex.
`.../2026-02/Résultats provisoires ... fin Décembre 2025.pdf`, 200), mais là « Dette Intérieure /
Dette Extérieure » désigne le **service de la dette (flux mensuel)**, pas l'encours — **à ne pas
confondre**.

---

## 4. Repli international (recoupement uniquement)

- **FMI WEO** : donne la **dette publique brute en % du PIB** (`GGXWDG_NGDP`), **sans** ventilation
  intérieure/extérieure. Utile pour le seul total, pas pour la partition cherchée.
- **Banque mondiale, International Debt Statistics / WDI** : donne la **dette extérieure publique et
  garantie (PPG)** en USD et en % du RNB, soit seulement la **jambe extérieure** d'un périmètre
  « dette extérieure du pays » (créancier non-résident), **différent** de la dette budgétaire
  intérieure/extérieure du ministère des Finances. À n'utiliser qu'en contrôle d'ordre de grandeur
  de l'extérieure, jamais comme substitut de la série nationale.
- Conclusion : l'international **ne fournit pas** la ventilation intérieur/extérieur de la dette
  **publique budgétaire** ; rester sur BCT + MinFin.

---

## Lacunes et travail à verser au backlog

- **Avant 2008** : la ventilation tabulée intérieure/extérieure de la dette publique dans les RA BCT
  antérieurs n'est pas confirmée sous la même forme. RA_fr_2000 : pas de tableau int/ext repéré (le
  texte porte surtout le coefficient de service de la dette extérieure). RA_fr_1995 : « Encours de
  la dette » (total, source ministère du Développement) + mentions dette intérieure/extérieure
  éparses, pas de tableau homogène. **TODO** : dépouiller RA 1990-2007 un par un pour établir
  jusqu'où remonte la forme « Encours de la dette publique » ventilée ; à défaut, la série longue
  homogène démarrera vers 2000/2008. Les PDF ont une couche texte FR (pas d'OCR).
- **Alternative série longue en une passe** : le **Bulletin statistique des finances** (pub. 108,
  `.../108`) porte le tableau **XIII-6 « Endettement total »** avec colonnes longues
  (endettement intérieur / extérieur sur ~7 ans par fascicule) — mais c'est le **périmètre monétaire
  large** (financement de l'économie), **pas** la dette budgétaire. À ne retenir que si l'annexe
  assume explicitement ce second périmètre, présenté à part. **TODO** : vérifier si le BSF publie
  aussi un tableau « dette de l'État » intérieur/extérieur budgétaire exploitable en série.
- **Chaînage à faire** (travail de données, pas documentaire) : extraire par `pdftotext -layout` le
  tableau « Encours de la dette publique » de chaque RA BCT 2015→2024 (et rapport2003→2014) pour
  bâtir la série MDT + % PIB continue 2008-2025, en traçant les révisions inter-millésimes.
- **Annexe 7 en arabe (OCR non requis mais parsing AR)** : les millésimes LF 2022, 2024, 2025 ont
  une **couche texte arabe** (pas besoin d'OCR), mais RTL + formes de présentation + chiffres :
  extraction du tableau « الدين الداخلي / الدين الخارجي » à scripter prudemment. Seul **LF 2021**
  existe en **traduction française** vérifiée. **TODO backlog** : repérer d'éventuelles traductions
  FR des autres millésimes, sinon prévoir un extracteur AR.
- **Archivage** : par consigne, **rien n'a été téléchargé dans les dépôts**. Fichiers seulement
  testés/lus en `/tmp`. Pour versement ultérieur dans `tunisia-data` (`data/raw/minfin-dette/`) avec
  ligne au catalogue : SHA-256 relevés — `Annexe 7 LF2021 Dette Publique.pdf` =
  `65d47d3166c1026ee31e5e5a0402bd6878817277b7dc34fb291d366642eee837` ;
  `ANNEXE_07 Dette publique.pdf` (LF2022) =
  `cb865d4a48c31bdbd0115d2e9831c321bb19acc79f0b7186765515a4cad7809c`.
